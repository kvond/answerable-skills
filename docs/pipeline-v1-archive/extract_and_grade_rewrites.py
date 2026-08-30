#!/usr/bin/env python3
"""
Workflow B1 — Rewrite Completion Grading on Student Word Documents

Reads a folder of Draft-prefixed .docx files and extracts each rewrite's
slide-section text. Scores completion (out of 5 expected sections), tracks
the challenge response separately, and outputs JSON consumed by Workflow B2.

Outputs:
  output_dir/rewrite_completion_report.csv         -- per-student completion scores
  output_dir/rewrites/<student>.json               -- per-student structured rewrites (B2 input)
  output_dir/workflow_b1_summary.md                -- human-readable teacher summary

Usage:
  python extract_and_grade_rewrites.py <draft_docs_folder> <output_dir>
    [--lesson "<Lesson Name>"] [--class "<Class Name>"]
"""

import sys
import json
import csv
import re
import argparse
from pathlib import Path
from datetime import date
from docx import Document


# -- Parsing markers ---------------------------------------------------------
# Slide marker: matches "Slide 13", "**Slide 13**", "# Slide 13", "1. Slide 13", etc.
SLIDE_MARKER = re.compile(
    r"(?:^|\n)\s*(?:\d+\.\s*)?(?:#+\s*)?(?:\*\*)?Slide\s+(\d+)\b[^\n]*",
    re.IGNORECASE,
)
# Challenge marker: matches "Challenge", "**Challenge**", "Challenge:", etc.
CHALLENGE_MARKER = re.compile(
    r"(?:^|\n)\s*(?:#+\s*)?(?:\*\*)?Challenge\b[^\n]*",
    re.IGNORECASE,
)

# Substantive-content threshold
WORD_COUNT_THRESHOLD = 15

# Total rewrite sections B always asks for
EXPECTED_SECTIONS = 5


# ---------------------------------------------------------------------------
# Word document reading
# ---------------------------------------------------------------------------

def read_docx_text(path):
    """Read all paragraph text from a .docx file."""
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())


def clean_leading_punct(text):
    """Strip leading dashes, em-dashes, colons, and whitespace from a section."""
    return re.sub(r"^[\s\-\u2014:]+", "", text).strip()


# ---------------------------------------------------------------------------
# Rewrite doc parsing
# ---------------------------------------------------------------------------

def parse_rewrite_doc(text):
    """Split a rewrite doc into per-slide sections and a challenge response.

    Returns (sections, challenge) where:
      sections = list of {slide_number, rewrite_text, word_count, addressed}
      challenge = {text, word_count, addressed} or None
    """
    # Find all slide markers and the challenge marker (if any)
    slide_matches = list(SLIDE_MARKER.finditer(text))
    challenge_match = CHALLENGE_MARKER.search(text)

    sections = []
    for i, m in enumerate(slide_matches):
        slide_num = int(m.group(1))
        # Section text starts after the marker line ends.
        # Find the newline after this match's end:
        marker_line_end = text.find("\n", m.end())
        if marker_line_end == -1:
            marker_line_end = m.end()
        section_start = marker_line_end + 1

        # Section ends at the next slide marker, the challenge marker,
        # or the end of the document.
        if i + 1 < len(slide_matches):
            section_end = slide_matches[i + 1].start()
        elif challenge_match and challenge_match.start() > section_start:
            section_end = challenge_match.start()
        else:
            section_end = len(text)

        rewrite_text = clean_leading_punct(text[section_start:section_end])
        word_count = len(rewrite_text.split())
        sections.append({
            "slide_number": slide_num,
            "rewrite_text": rewrite_text,
            "word_count": word_count,
            "addressed": word_count >= WORD_COUNT_THRESHOLD,
        })

    # Challenge response: everything after the challenge marker's line
    challenge = None
    if challenge_match:
        marker_line_end = text.find("\n", challenge_match.end())
        if marker_line_end == -1:
            marker_line_end = challenge_match.end()
        challenge_start = marker_line_end + 1
        challenge_text = clean_leading_punct(text[challenge_start:])
        # Strip a trailing teacher signature if present (e.g., "— Dr. von Duyke")
        sig_match = re.search(r"\n\s*\u2014\s*Dr\.\s*von\s*Duyke", challenge_text)
        if sig_match:
            challenge_text = challenge_text[:sig_match.start()].strip()
        word_count = len(challenge_text.split())
        challenge = {
            "text": challenge_text,
            "word_count": word_count,
            "addressed": word_count >= WORD_COUNT_THRESHOLD,
        }

    return sections, challenge


# ---------------------------------------------------------------------------
# Completion scoring
# ---------------------------------------------------------------------------

def score_completion(sections, challenge, expected_sections=EXPECTED_SECTIONS):
    """Compute completion metrics from parsed sections."""
    addressed_count = sum(1 for s in sections if s["addressed"])
    # Cap at expected_sections so students who address >5 don't get >100%
    completion_percent = round(
        100.0 * min(addressed_count, expected_sections) / expected_sections, 1
    )
    total_words = sum(s["word_count"] for s in sections)
    if challenge:
        total_words += challenge["word_count"]
    return {
        "rewrite_sections_addressed": addressed_count,
        "total_rewrite_sections_expected": expected_sections,
        "completion_percent": completion_percent,
        "challenge_addressed": challenge["addressed"] if challenge else False,
        "total_word_count": total_words,
    }


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_student_json(out_dir, student_name, lesson, class_name, completion,
                        sections, challenge):
    """Write the per-student JSON file (B2's input)."""
    payload = {
        "student": student_name,
        "lesson": lesson,
        "class": class_name,
        "date": str(date.today()),
        "completion": completion,
        "rewrites": sections,
        "challenge_response": challenge,
    }
    path = out_dir / "rewrites" / f"{student_name}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)


def write_completion_csv(out_dir, rows):
    path = out_dir / "rewrite_completion_report.csv"
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "student",
                "rewrite_sections_addressed",
                "total_rewrite_sections_expected",
                "completion_percent",
                "challenge_addressed",
                "total_word_count",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_summary_md(out_dir, completion_rows, unparseable, lesson, class_name):
    lines = [
        "# Workflow B1 — Rewrite Completion Report",
        "",
        f"**Lesson:** `{lesson}`" if lesson else "",
        f"**Class:** `{class_name}`" if class_name else "",
        f"**Students processed:** {len(completion_rows)}",
        f"**Unparseable docs:** {len(unparseable)}",
        "",
        "## Student completion",
        "",
        "| Student | Addressed | Expected | % | Challenge | Words |",
        "|---|---|---|---|---|---|",
    ]
    for row in sorted(completion_rows, key=lambda r: r["student"]):
        challenge_mark = "Yes" if row["challenge_addressed"] else "No"
        lines.append(
            f"| {row['student']} | {row['rewrite_sections_addressed']} | "
            f"{row['total_rewrite_sections_expected']} | {row['completion_percent']}% | "
            f"{challenge_mark} | {row['total_word_count']} |"
        )

    if unparseable:
        lines.extend([
            "",
            "## Unparseable rewrites (no Slide N markers found)",
            "",
            "These docs need manual review — the student likely wrote their rewrite "
            "as one block without preserving the slide-section structure from the email.",
            "",
        ])
        for s in sorted(unparseable):
            lines.append(f"- {s}")

    lines.extend([
        "",
        "## Next step",
        "",
        "Per-student JSON files in `rewrites/` are ready for **Workflow B2** "
        "(rubric scoring and improvement comparison vs original).",
    ])

    with open(out_dir / "workflow_b1_summary.md", "w") as f:
        f.write("\n".join(line for line in lines if line is not None))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def derive_student_id(filename_stem):
    """Strip leading 'Draft ' or 'Draft - ' or 'Draft_' prefix from filename."""
    # Match: "Draft", optional space/dash/underscore, then rest
    m = re.match(r"^Draft[\s\-_]+(.+)$", filename_stem, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return filename_stem


def run(draft_dir, output_dir, lesson, class_name):
    draft_dir = Path(draft_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Filter: only Draft-prefixed .docx files
    all_docs = sorted(draft_dir.glob("*.docx"))
    draft_docs = [d for d in all_docs if d.stem.lower().startswith("draft")]

    if not draft_docs:
        print(f"No Draft-prefixed .docx files found in {draft_dir}", file=sys.stderr)
        sys.exit(2)

    completion_rows = []
    unparseable = []

    for docpath in draft_docs:
        student_id = derive_student_id(docpath.stem)

        try:
            text = read_docx_text(docpath)
        except Exception as e:
            print(f"Failed to read {docpath}: {e}", file=sys.stderr)
            unparseable.append(student_id)
            continue

        sections, challenge = parse_rewrite_doc(text)

        # If no slide markers found, flag as unparseable but still write a JSON
        if not sections:
            unparseable.append(student_id)
            completion = {
                "rewrite_sections_addressed": 0,
                "total_rewrite_sections_expected": EXPECTED_SECTIONS,
                "completion_percent": 0.0,
                "challenge_addressed": challenge["addressed"] if challenge else False,
                "total_word_count": challenge["word_count"] if challenge else 0,
            }
        else:
            completion = score_completion(sections, challenge)

        write_student_json(
            output_dir, student_id, lesson, class_name, completion, sections, challenge
        )

        completion_rows.append({
            "student": student_id,
            **completion,
        })

    write_completion_csv(output_dir, completion_rows)
    write_summary_md(output_dir, completion_rows, unparseable, lesson, class_name)

    print(f"Processed {len(completion_rows)} rewrite docs.")
    if unparseable:
        print(f"Flagged {len(unparseable)} unparseable: {unparseable}")
    print(f"Outputs written to {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft_dir", help="Folder containing Draft-prefixed .docx files")
    parser.add_argument("output_dir", help="Where to write outputs")
    parser.add_argument("--lesson", default="", help="Lesson name")
    parser.add_argument("--class", dest="class_name", default="", help="Class section name")
    args = parser.parse_args()
    run(args.draft_dir, args.output_dir, args.lesson, args.class_name)
