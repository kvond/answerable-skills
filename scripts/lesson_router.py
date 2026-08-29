"""
Lesson Router — content-based identification of student submissions.

Purpose:
  Students submit work to the wrong folders, with the wrong filenames, and
  sometimes mixing up which lesson they're answering. This router ignores
  filenames and folders entirely and identifies the lesson from the file's
  CONTENT.

Pipeline position:
  Runs as Step 0 before any Workflow A or B1 invocation. Scans the Schoology
  Drive root, identifies (file, student, class, lesson, type), and produces
  per-lesson queues for downstream workflows.

Types:
  - NOTES (slides) — Google Slides files
  - DRAFT (docs)   — Word .docx files

Key inputs:
  - Lesson fingerprints (see LESSON_FINGERPRINTS below)
  - Class rosters (from Teacher Dashboard)
  - Schoology Drive root

Output:
  - JSON-serializable router report with each file tagged
  - "needs-review" queue for ambiguous or unidentifiable files
"""

from __future__ import annotations
import io
import json
import re
import sys
from dataclasses import dataclass, field
from typing import Optional

# ─────────────────────────────────────────────────────────────────────
# LESSON FINGERPRINTS
# ─────────────────────────────────────────────────────────────────────
# Each lesson has 4-8 distinctive phrases that should appear in its
# diagnostic slides or rewrite-direction emails. Phrases must be specific
# enough that they DON'T appear in other lessons.
#
# Matching rules:
#   - Case-insensitive substring match (after normalization)
#   - Each phrase counts ONCE per file (not per occurrence)
#   - Lesson with most matches wins, IF it has at least MIN_MATCHES
#   - If two lessons tie at the top, file goes to needs-review
#
# Add new lessons here as you build them out — keep phrases distinctive,
# pulled from actual slide text or rewrite-email content.

LESSON_FINGERPRINTS = {
    "Natural Selection": {
        "subject": "Biology",
        "phrases": [
            "variation is the raw material",
            "moths blend in",
            "long-necked giraffe",
            "lamarck",
            "long-necked giraffes just happen to survive",
            "every moth looked exactly the same",
            "antibiotic-resistant",
            "pale birch forest",
            "darwin's idea",
            "the environment decides which traits survive",
        ],
    },
    "Evidence of Evolution": {
        "subject": "Biology",
        "phrases": [
            "homologous structures",
            "vestigial",
            "fossil record",
            "comparative anatomy",
            "transitional fossil",
            "embryological",
            "biogeography",
            "common ancestor",
            "analogous structures",
            "molecular evidence",
        ],
    },
    "Introduction to Evolution": {
        "subject": "Biology",
        "phrases": [
            "what is evolution",
            "darwin's voyage",
            "galapagos",
            "finch",
            "descent with modification",
            "origin of species",
            "beagle",
            "natural selection vs artificial selection",
        ],
    },
    "Classifying Organisms": {
        "subject": "Biology",
        "phrases": [
            "binomial nomenclature",
            "domain bacteria",
            "domain archaea",
            "domain eukarya",
            "linnaeus",
            "kingdom phylum class order family genus species",
            "dichotomous key",
            "taxonomy",
            "cladogram",
        ],
    },
    "Pig Autopsy": {
        "subject": "Forensics",
        "phrases": [
            "pig autopsy",
            "fetal pig",
            "incision",
            "liver kidney spleen",
            "scalpel",
            "lividity",
            "rigor mortis",
            "external examination",
            "thoracic cavity",
            "manner of death",
        ],
    },
    "Stages of Decomposition": {
        "subject": "Forensics",
        "phrases": [
            "fresh stage",
            "bloat stage",
            "active decay",
            "advanced decay",
            "skeletal stage",
            "decomposition timeline",
            "putrefaction",
            "adipocere",
        ],
    },
    "What is Death?": {
        "subject": "Forensics",
        "phrases": [
            "brain death",
            "cardiac death",
            "circulatory death",
            "irreversible cessation",
            "harvard criteria",
            "persistent vegetative state",
            "uniform determination of death",
        ],
    },
    "Time of Death": {
        "subject": "Forensics",
        "phrases": [
            "algor mortis",
            "post-mortem interval",
            "post mortem interval",
            "body temperature drop",
            "henssge nomogram",
            "stomach contents",
            "insect activity",
            "core body temperature",
        ],
    },
}

# Minimum number of distinct phrase matches required to assign a lesson.
# Lower → more aggressive matching but more false positives.
# Higher → safer but more "needs-review" files.
MIN_MATCHES = 2

# Tie-break threshold: if top lesson has X matches and second lesson has
# (X - TIE_GAP) or more, treat as ambiguous.
TIE_GAP = 1


# ─────────────────────────────────────────────────────────────────────
# CLASS ROSTER — read LIVE from the Teacher Dashboard (NEVER hardcoded)
# ─────────────────────────────────────────────────────────────────────
# HARD rule: the Dashboard All-page ("ALL-open to sync before import") is the
# single source of truth for class membership AND student emails. This module
# holds NO baked-in roster. The orchestrator fetches the All-page via Composio
# and builds the roster with build_roster_from_all_page(); until then ROSTER is
# empty and every file routes to needs-review-no-student.
#
# 2026–27 Dashboard (roster source):
DASHBOARD_SHEET_ID = "1yW8AHGNaZSHP_kf_HS9xyoVwIkCAoC-HFuze3huSHzE"

# Permanently out of scope (mirror of lesson_name_guard.OUT_OF_SCOPE).
OUT_OF_SCOPE = {"pig autopsy", "stages of decomposition"}

# Empty by design — populated at runtime from the Dashboard, not in source.
ROSTER: dict = {}

def _norm_name(name):
    """Lowercase, drop every non-letter (apostrophes, hyphens, spaces)."""
    return re.sub(r"[^a-z]+", "", (name or "").lower())

def _is_out_of_scope(lesson):
    return bool(lesson) and lesson.strip().lower() in OUT_OF_SCOPE

def build_roster_from_all_page(rows):
    """
    Build the roster from Teacher Dashboard All-page rows (including header row).
    Columns resolved BY HEADER (order-independent): Class, First Name, Last Name,
    Student email, Unique User ID.
    Returns (roster, roster_meta):
      roster      = {class_section: [full_name, ...]}
      roster_meta = {_norm_name(full_name): {"name","class","email","uuid"}}
    Empty or header-only input -> ({}, {}). Unrecognized layout -> ({}, {}) (fail safe).
    """
    roster, meta = {}, {}
    if not rows:
        return roster, meta
    header = [str(h).strip().lower() for h in rows[0]]
    def col(*names):
        for n in names:
            if n in header:
                return header.index(n)
        return None
    ci, fi, li = col("class"), col("first name"), col("last name")
    ei, ui = col("student email", "email"), col("unique user id", "uuid")
    if ci is None or fi is None or li is None:
        return roster, meta
    def g(r, i):
        return r[i].strip() if (i is not None and i < len(r) and r[i]) else ""
    for r in rows[1:]:
        cls, first, last = g(r, ci), g(r, fi), g(r, li)
        name = (first + " " + last).strip()
        if not cls or not name:
            continue
        roster.setdefault(cls, []).append(name)
        meta[_norm_name(name)] = {"name": name, "class": cls, "email": g(r, ei), "uuid": g(r, ui)}
    return roster, meta


# ─────────────────────────────────────────────────────────────────────
# Data classes
# ─────────────────────────────────────────────────────────────────────
@dataclass
class FileRecord:
    drive_id: str
    title: str
    mime_type: str
    owner: Optional[str] = None
    modified_time: Optional[str] = None
    # Filled by router
    student_name: Optional[str] = None
    class_section: Optional[str] = None
    lesson: Optional[str] = None
    file_type: Optional[str] = None  # "NOTES" | "DRAFT" | "UNKNOWN"
    lesson_match_scores: dict = field(default_factory=dict)
    routing_status: str = "unrouted"
    routing_notes: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "drive_id": self.drive_id,
            "title": self.title,
            "mime_type": self.mime_type,
            "owner": self.owner,
            "modified_time": self.modified_time,
            "student_name": self.student_name,
            "class_section": self.class_section,
            "lesson": self.lesson,
            "file_type": self.file_type,
            "lesson_match_scores": self.lesson_match_scores,
            "routing_status": self.routing_status,
            "routing_notes": self.routing_notes,
        }


# ─────────────────────────────────────────────────────────────────────
# Step 1 — Identify file type (NOTES vs DRAFT) from mime type
# ─────────────────────────────────────────────────────────────────────
def identify_file_type(file: FileRecord) -> str:
    """NOTES = Google Slides. DRAFT = Word .docx. Everything else = UNKNOWN."""
    if file.mime_type == "application/vnd.google-apps.presentation":
        return "NOTES"
    elif file.mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return "DRAFT"
    else:
        return "UNKNOWN"


# ─────────────────────────────────────────────────────────────────────
# Step 2 — Identify student from filename
# ─────────────────────────────────────────────────────────────────────
# Schoology naming convention: "First Last - <assignment text> - <id>"
# So we strip everything after the FIRST " - " and try to match against roster.

def identify_student_and_class(file: FileRecord, roster: Optional[dict] = None) -> tuple[Optional[str], Optional[str], list[str]]:
    """
    Returns (student_name, class_section, notes).
    Matches the filename name-prefix against the roster read LIVE from the
    Dashboard All-page (HARD rule: Dashboard is the source of truth for class
    membership). `roster` is {class_section: [full_name, ...]}; when None, falls
    back to module ROSTER (empty until build_roster_from_all_page() is run).
    """
    roster = roster if roster is not None else ROSTER
    notes = []
    title = file.title.strip()
    candidate = title.split(" - ", 1)[0].strip() if " - " in title else title.strip()
    candidate_norm = _norm_name(candidate)

    if not roster:
        notes.append("Roster is empty — populate the Dashboard All-page first.")
        return None, None, notes

    matches = []
    for class_section, students in roster.items():
        for s in students:
            if _norm_name(s) == candidate_norm:
                matches.append((s, class_section))

    if not matches:
        notes.append(f"No roster match for prefix '{candidate}'")
        return None, None, notes

    if len(set(c for _, c in matches)) > 1:
        notes.append(f"Student name appears in multiple classes: {matches}")

    return matches[0][0], matches[0][1], notes


# ─────────────────────────────────────────────────────────────────────
# Step 3 — Identify lesson from CONTENT (fingerprint matching)
# ─────────────────────────────────────────────────────────────────────
def score_lesson_fingerprints(text: str) -> dict[str, int]:
    """
    Returns {lesson_name: match_count} for each lesson whose fingerprints
    are found in the text. Case-insensitive substring matching.
    """
    if not text:
        return {}

    normalized = text.lower()
    scores = {}
    for lesson, config in LESSON_FINGERPRINTS.items():
        count = 0
        for phrase in config["phrases"]:
            if phrase.lower() in normalized:
                count += 1
        if count > 0:
            scores[lesson] = count
    return scores


def assign_lesson_from_scores(scores: dict[str, int]) -> tuple[Optional[str], str, list[str]]:
    """
    Given fingerprint match scores, decide which lesson the file belongs to.
    Returns (lesson, status, notes).
    Status: "routed" | "needs-review-ambiguous" | "needs-review-no-match"
    """
    notes = []
    if not scores:
        return None, "needs-review-no-match", ["No lesson fingerprints matched"]

    sorted_scores = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    top_lesson, top_score = sorted_scores[0]

    if top_score < MIN_MATCHES:
        notes.append(f"Top match '{top_lesson}' had only {top_score} matches (min {MIN_MATCHES})")
        return None, "needs-review-no-match", notes

    if len(sorted_scores) > 1:
        second_lesson, second_score = sorted_scores[1]
        if (top_score - second_score) < TIE_GAP:
            notes.append(
                f"Ambiguous: '{top_lesson}' ({top_score}) vs '{second_lesson}' ({second_score})"
            )
            return None, "needs-review-ambiguous", notes

    return top_lesson, "routed", notes


# ─────────────────────────────────────────────────────────────────────
# Step 4 — Tier-2 fallback: title hints when content is empty
# ─────────────────────────────────────────────────────────────────────
# If a file's content fingerprint match fails (zero hits or weak), we fall
# back to looking at the filename itself. This is less reliable but better
# than punting to needs-review.

TITLE_HINTS = {
    "Natural Selection": ["natural selection", "naturalselection"],
    "Evidence of Evolution": ["evidence of evolution", "evidenceofevolution"],
    "Introduction to Evolution": ["intro_evolution", "introduction to evolution", "intro to evolution"],
    "Classifying Organisms": ["classifying organisms"],
    "Pig Autopsy": ["pig autopsy"],
    "Stages of Decomposition": ["stages of decomposition", "stagesofdecomposition"],
    "What is Death?": ["what is death"],
    "Time of Death": ["time of death", "timeofdeath"],
}

def lesson_from_title(title: str) -> Optional[str]:
    t = title.lower()
    for lesson, hints in TITLE_HINTS.items():
        for h in hints:
            if h in t:
                return lesson
    return None


# ─────────────────────────────────────────────────────────────────────
# Main router
# ─────────────────────────────────────────────────────────────────────
def route_file(
    file: FileRecord,
    content_text: Optional[str] = None,
    roster: Optional[dict] = None,
) -> FileRecord:
    """
    Route a single file. Content_text is the text extracted from the file
    (None if not yet read — router will rely on title hints only).
    Mutates and returns the FileRecord.
    """
    # Step 1: file type
    file.file_type = identify_file_type(file)
    if file.file_type == "UNKNOWN":
        file.routing_status = "skip-not-student-work"
        file.routing_notes.append(f"Mime type {file.mime_type} is not slides or .docx")
        return file

    # Step 2: student and class
    student, class_section, notes = identify_student_and_class(file, roster)
    file.routing_notes.extend(notes)
    file.student_name = student
    file.class_section = class_section
    if not student:
        file.routing_status = "needs-review-no-student"
        return file

    # Step 3: lesson by content fingerprint
    if content_text:
        scores = score_lesson_fingerprints(content_text)
        file.lesson_match_scores = scores
        lesson, status, notes = assign_lesson_from_scores(scores)
        file.routing_notes.extend(notes)
        if lesson:
            file.lesson = lesson
            if _is_out_of_scope(lesson):
                file.routing_status = "skip-out-of-scope"
                file.routing_notes.append(f"'{lesson}' is permanently out of scope — not queued.")
            else:
                file.routing_status = "routed-by-content"
            return file

    # Step 4: fallback to title hint
    title_lesson = lesson_from_title(file.title)
    if title_lesson:
        file.lesson = title_lesson
        if _is_out_of_scope(title_lesson):
            file.routing_status = "skip-out-of-scope"
            file.routing_notes.append(f"'{title_lesson}' is permanently out of scope — not queued.")
        else:
            file.routing_status = "routed-by-title-fallback"
            file.routing_notes.append(
                "Content fingerprints failed/unavailable — used filename hint."
                " Verify before processing."
            )
        return file

    # No match at all
    file.routing_status = "needs-review-no-lesson"
    return file


# ─────────────────────────────────────────────────────────────────────
# Demo / test harness
# ─────────────────────────────────────────────────────────────────────
def demo():
    """Smoke test on a synthetic set of files matching real Drive items."""
    test_files = [
        # The 10 mis-filed B_Day Evidence of Evolution NOTES files
        FileRecord(
            drive_id="18Jdx2jgXL-1K5JWSRsUwfe-sxKPLIx7GrHJAroilWhU",
            title="Aydin Speleos - NOTESEvidence of Evolution - 15392390",
            mime_type="application/vnd.google-apps.presentation",
        ),
        FileRecord(
            drive_id="1BeZaGGHYcc74PdOUWpFlBuXfYPf10oBPs14JrCM4WDY",
            title="Zariah White - NOTESEvidence of Evolution - 19939514",
            mime_type="application/vnd.google-apps.presentation",
        ),
        # Kimora's actual DRAFT
        FileRecord(
            drive_id="1yTAdYV1e67Ve99oqA5PXYf4pK6ygRu6tZ8vifIEHW6s",
            title="Kimora Pochvatilla - DRAFTEvidence of Evolution - 17609333",
            mime_type="application/vnd.google-apps.presentation",
        ),
        # An A_Day student in the right place
        FileRecord(
            drive_id="aaa-pretend-id-1",
            title="Phenix Collins - NotesNaturalSelection - 12345",
            mime_type="application/vnd.google-apps.presentation",
        ),
        # Wrong-name scenario: student named file wrong
        FileRecord(
            drive_id="bbb-pretend-id-2",
            title="Tyaire Herring - Biology homework",  # No lesson in filename
            mime_type="application/vnd.google-apps.presentation",
        ),
        # Word doc rewrite
        FileRecord(
            drive_id="ccc-pretend-id-3",
            title="Mariana Romero Cruz - DraftNaturalSelection - 99999",
            mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ),
        # Unknown student
        FileRecord(
            drive_id="ddd-pretend-id-4",
            title="John Doe - NotesPig Autopsy - 555",
            mime_type="application/vnd.google-apps.presentation",
        ),
    ]

    # Fake content for the content-routing test cases
    SAMPLE_CONTENT_NS = """
    Slide 7: Why can't natural selection work if every organism has identical traits?
    Slide 18: A giraffe with a longer neck can reach more leaves. Did the giraffe
    evolve a longer neck because it stretched? Or did long-necked giraffes just
    happen to survive better? Lamarck's idea vs Darwin's idea. The environment
    decides which traits survive.
    """
    SAMPLE_CONTENT_EE = """
    Vestigial structures, homologous structures, fossil record, transitional fossil,
    common ancestor, comparative anatomy, embryological evidence, biogeography.
    """
    SAMPLE_CONTENT_GENERIC = "This is just some biology homework about cells."

    file_content_map = {
        "18Jdx2jgXL-1K5JWSRsUwfe-sxKPLIx7GrHJAroilWhU": SAMPLE_CONTENT_EE,
        "1BeZaGGHYcc74PdOUWpFlBuXfYPf10oBPs14JrCM4WDY": SAMPLE_CONTENT_EE,
        "1yTAdYV1e67Ve99oqA5PXYf4pK6ygRu6tZ8vifIEHW6s": SAMPLE_CONTENT_EE,
        "aaa-pretend-id-1": SAMPLE_CONTENT_NS,
        "bbb-pretend-id-2": SAMPLE_CONTENT_GENERIC,  # generic content — should fall back to title (also fails)
        "ccc-pretend-id-3": SAMPLE_CONTENT_NS,
        "ddd-pretend-id-4": "",  # no content yet
    }

    # synthetic roster (mimics the Dashboard All-page) so the demo is self-contained
    demo_roster = {
        "A_Day Biology": ["Phenix Collins"],
        "B_Day Biology": ["Aydin Speleos", "Zariah White", "Kimora Pochvatilla",
                          "Tyaire Herring", "Mariana Romero Cruz"],
    }
    routed = []
    for f in test_files:
        content = file_content_map.get(f.drive_id)
        routed.append(route_file(f, content, roster=demo_roster))

    # Pretty-print results
    print("=" * 80)
    print("LESSON ROUTER — DEMO RESULTS")
    print("=" * 80)
    for f in routed:
        print(f"\n📄 {f.title}")
        print(f"   ID: {f.drive_id}")
        print(f"   Type: {f.file_type}")
        print(f"   Student: {f.student_name or '—'}")
        print(f"   Class: {f.class_section or '—'}")
        print(f"   Lesson: {f.lesson or '—'}")
        print(f"   Status: {f.routing_status}")
        if f.lesson_match_scores:
            print(f"   Fingerprint scores: {f.lesson_match_scores}")
        if f.routing_notes:
            for n in f.routing_notes:
                print(f"   Note: {n}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY BY STATUS")
    print("=" * 80)
    from collections import Counter
    by_status = Counter(f.routing_status for f in routed)
    for status, count in by_status.most_common():
        print(f"  {status}: {count}")

    # Queue view
    print("\n" + "=" * 80)
    print("PER-LESSON QUEUES (ready for Workflow A / B1)")
    print("=" * 80)
    queues = {}
    for f in routed:
        if f.routing_status.startswith("routed"):
            key = (f.class_section, f.lesson, f.file_type)
            queues.setdefault(key, []).append(f)
    for key in sorted(queues.keys(), key=lambda k: (k[0] or "", k[1] or "", k[2])):
        cls, lesson, ftype = key
        files = queues[key]
        print(f"\n  {cls} • {lesson} • {ftype}  ({len(files)} file{'s' if len(files) != 1 else ''})")
        for f in files:
            print(f"    - {f.student_name}: {f.title[:60]}")

    # Needs-review queue
    print("\n" + "=" * 80)
    print("NEEDS REVIEW QUEUE (teacher decision required)")
    print("=" * 80)
    nr = [f for f in routed if f.routing_status.startswith("needs-review") or f.routing_status == "skip-not-student-work"]
    if not nr:
        print("  (empty)")
    else:
        for f in nr:
            print(f"\n  📄 {f.title}")
            print(f"     Why: {f.routing_status}")
            for n in f.routing_notes:
                print(f"     - {n}")


if __name__ == "__main__":
    demo()
