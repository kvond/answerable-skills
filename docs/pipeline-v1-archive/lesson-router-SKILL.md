---
name: lesson-router
description: >
  Content-based router that identifies the (student, class, lesson, type)
  of every student submission, regardless of filename or folder. Runs as
  Step 0 before Workflow A or B1 — pre-sorts files into per-lesson queues
  and flags ambiguous or unidentifiable files for teacher review.
  Use this skill whenever the teacher asks to "scan for new submissions,"
  "check what's pending," "route the new files," or "find what's where."
  Also use as the FIRST step whenever running Workflow A or B1 on any
  lesson — never trust the folder a file lives in.
---

# Lesson Router — Content-Based Submission Identification

A pre-processing step that fixes a recurring real-world problem: students
submit work to the wrong folders with the wrong filenames, sometimes mixing
up which lesson they're answering. The router ignores filenames and folders
entirely and identifies the lesson from each file's **content**.

---

## When to Use

- Teacher asks "scan for new submissions" or "what's pending"
- As Step 0 before any Workflow A or B1 invocation
- When investigating why a student's score is unexpectedly low or missing
- When deciding which submissions belong to which Schoology assignment

---

## What It Does

For each file in the Schoology Drive root (or a specified folder):

1. **Identifies file type** by mime type: Google Slides = NOTES, Word .docx = DRAFT, everything else skipped
2. **Identifies the student** by matching the filename prefix against the Teacher Dashboard roster (HARD rule: Dashboard is source of truth for class membership)
3. **Identifies the lesson by content** — reads the file's text and matches against per-lesson fingerprint phrases
4. **Falls back to filename hints** if content matching fails
5. **Flags ambiguous or unidentifiable files** for teacher review

---

## Inputs Required

- **Schoology Drive root ID** (default: `18ZOnISxkNmDVrjxJjCpaZLeTqVYF6fK7`) or a specific subfolder
- **Lesson fingerprints** (defined in `lesson_router.py` — see "Maintaining Lesson Fingerprints" below)
- **Class roster** — built at runtime from the Teacher Dashboard **All-page** ("ALL-open to sync before import", columns A–E: Class, First Name, Last Name, Student email, Unique User ID). NEVER hardcoded. Default 2026–27 Dashboard: `1TSPmNUpI7n9c3MWgDVLtxEnypB5k6FA865F_JjOQD1U`.

---

## Steps

### Step 1 — Scan target folder(s)

Use `Google Drive:search_files` with the parent ID. Capture every file's:
- `drive_id`
- `title`
- `mimeType`
- `owner`
- `modifiedTime`

Recurse into subfolders if needed (each course has nested lesson folders).

### Step 2 — Build the roster, then route

First build the roster ONCE from the Dashboard All-page, then pass it into every `route_file()` call (the roster is NEVER hardcoded — it lives only in the Dashboard):
- Fetch the All-page rows via Composio: `GOOGLESHEETS_BATCH_GET`, range `'ALL-open to sync before import'!A:E`.
- `roster, roster_meta = build_roster_from_all_page(rows)` — returns `{}` until the Dashboard is populated. `roster_meta` carries the source-of-truth email + Unique User ID per student.
- For each file, call `route_file(file, content_text=<text>, roster=roster)`. The router needs:
  - The `FileRecord` (Drive metadata)
  - The file's text content (for fingerprint matching)
  - The `roster` dict (class membership; source of truth = Dashboard)

If the roster is empty, every file returns `needs-review-no-student` — populate the Dashboard All-page first.

Get the content:
- For Slides: `Google Drive:download_file_content` with `exportMimeType: text/plain`
- For .docx: `Google Drive:read_file_content` (which gives the doc as text)

### Step 3 — Build the per-lesson queues

After all files are routed, group by `(class_section, lesson, file_type)`. Each queue is the input list for Workflow A (NOTES queues) or Workflow B1 (DRAFT queues).

### Step 4 — Report to teacher

Produce a structured report:
- Per-lesson queues with file counts
- Needs-review queue with reason
- Skipped files (non-student work)
- Surprises (e.g., file with NOTES content in a DRAFT folder — Kimora Pochvatilla scenario)

### Step 5 — Optional: write router output to Dashboard

Add a row to the Activity Log for this router run with:
- Timestamp
- Folders scanned
- File count
- Queue counts per lesson
- Needs-review count

---

## Routing Output Categories

| Status | Meaning | Next action |
|---|---|---|
| `routed-by-content` | Strong fingerprint match — high confidence | Add to per-lesson queue, ready for processing |
| `routed-by-title-fallback` | Content matching failed, used filename hint | Add to queue but flag in report — verify before processing |
| `needs-review-ambiguous` | Two lessons matched equally — can't decide | Teacher decides; do not process |
| `needs-review-no-lesson` | No fingerprint matched any known lesson | Teacher decides; could be new lesson or off-topic |
| `needs-review-no-student` | Filename prefix doesn't match any roster | Teacher decides; could be new student or junk file |
| `skip-not-student-work` | Mime type isn't slides or .docx | Skip — not in scope |
| `skip-out-of-scope` | Lesson is permanently out of scope (Pig Autopsy, Stages of Decomposition) | Skip — never queued |

---

## Maintaining Lesson Fingerprints

The fingerprints live in `LESSON_FINGERPRINTS` at the top of `lesson_router.py`. Each lesson needs **4-8 distinctive phrases** that:

- Appear in the lesson's diagnostic slides OR Workflow B rewrite-direction emails
- Do NOT appear in other lessons
- Are stable across student rewordings (i.e., they appear in slide text the student didn't write, so even an empty student doc will match)

### Adding a new lesson

1. Open the teacher template for the new lesson
2. Pick 4-8 short, distinctive phrases from diagnostic slide text (questions, prompt headers, vocabulary in word banks)
3. Confirm each phrase doesn't appear in already-defined lessons (the router scores ALL lessons and picks the winner — overlapping phrases cause ambiguity)
4. Add to `LESSON_FINGERPRINTS` dict in alphabetical order
5. Run the demo function to sanity-check

### Tuning thresholds

- `MIN_MATCHES = 2` — files need at least 2 phrase hits to be routed. Lower → more aggressive; higher → more needs-review.
- `TIE_GAP = 1` — if two lessons are within 1 phrase of each other at the top, treat as ambiguous.

If you're getting too many false positives, raise `MIN_MATCHES`. If too many needs-review, expand fingerprints or lower `MIN_MATCHES`.

---

## Edge cases and how the router handles them

- **Student submitted NOTES to a DRAFT folder** (Kimora scenario from 2026-05-26): router catches it because content matches NOTES patterns, not filename. File goes to NOTES queue regardless of folder.
- **Student renamed their file weirdly** ("Biology homework.gslides"): no filename hint, fingerprint matching from content still works.
- **Student wrote answers but the slide template text still matches**: the fingerprints are slide-template phrases, so a student who barely engaged will still get routed correctly (their content has the template phrases). Their score is low because Workflow A scoring looks at the answer fields — that's separate from routing.
- **Student name has apostrophes or hyphens** (Son'jai, Sha'rod, Castro-Santos): router normalizes by stripping non-alpha characters before matching against roster. As long as the roster includes both punctuated and unpunctuated variants, match succeeds.
- **Same student appears in multiple class rosters**: this should not happen but if it does, router picks the first match and adds a note. Fix the roster.
- **Lesson named differently across classes** ("Pig Autopsy" A_Day vs "Pig Autopsy report" B_Day): use the same canonical lesson name in `LESSON_FINGERPRINTS`. Add multiple TITLE_HINTS variants if needed.

---

## Anti-patterns

- ❌ Don't assume the folder a file is in tells you the lesson. Always run the router first.
- ❌ Don't add fingerprints that appear in multiple lessons. Specificity matters more than count.
- ❌ Don't process anything in the `needs-review` queue automatically. Ambiguity = teacher decides.
- ❌ Don't skip students whose names have non-standard punctuation — add their variants to the roster.

---

## Reference

The router code lives at `lesson_router.py`. Demo command:

```
python lesson_router.py
```

It runs against a set of synthetic test cases including the real B_Day Evidence of Evolution mis-filed NOTES from May 2026. Use this as a regression test when changing fingerprints or thresholds.
