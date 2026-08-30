---
name: workflow-c-growth-tracking
description: >
  Run Workflow C on accumulated B2 rubric data files to produce or update the
  longitudinal student growth tracking doc. Use this skill whenever a teacher
  says "run C", "update the growth doc", "show me student rubric trends",
  "who's improving", "growth tracking", or "run the growth workflow."
  Workflow C reads all B2 rubric-data JSON files for a class (or all classes),
  appends any new lesson data to the master Google Doc, and recomputes
  per-student and whole-class trajectory markers. It is idempotent — running it
  twice on the same data produces the same result.
  Formerly called Workflow B3.
---

# Workflow C — Longitudinal Growth Tracking

The end of the per-lesson pipeline. Reads B2 rubric data accumulated across
lessons and updates a single master Google Doc with 🟥🟨🟩 trajectories
per student and per class. Append-only and idempotent.

---

## When to Use

- After B2 has run for at least one lesson
- Teacher says "run C," "update the growth doc," "show me rubric trends," or "who's improving"
- Periodic review: end of unit, mid-quarter, or before parent conferences
- Always runs **after** B2 — C has nothing to read until B2 has produced rubric data files

---

## Step 1 — Identify Inputs

### Required

1. **B2 rubric data files** — one per student per lesson, stored in each lesson's `04_Workflow_B2_Summary/` folder. Filename pattern: `rubric_data.<lesson>.<student_id>.json`
2. **Teacher Dashboard Config** — to resolve folder IDs and the roster. File ID in `dashboard_file_id` Config key. Match rows by `(Student Name, Lesson)` composite key.
3. **Workflow C master Google Doc** — the accumulating growth doc. File ID stored as `c_growth_doc_id` in Dashboard Config. If the key is missing, C creates a new doc, saves it to the AI workspace, and writes the ID back to Config.

### Scope

C can run:
- **All classes** (default) — scans all four class B2 output folders
- **Single class** — teacher specifies, e.g., "run C for B_Day Biology only"
- **Re-run** — teacher asks to recompute trajectories after a B2 correction; C is idempotent so a re-run is safe

---

## Step 2 — Collect and Deduplicate Rubric Data

For each class in scope:

1. List all files in `04_Workflow_B2_Summary/` whose names match `rubric_data.*.json`
2. Parse each file (schema below)
3. Build an in-memory map: `student_id → list of lesson rubric records`, sorted by `lesson_date` ascending
4. **Deduplication:** if two records share the same `(student_id, lesson_slug)`, use the one with the later `b2_run_timestamp`. Mark it `(updated <date>)` in the growth doc.

### B2 rubric data file schema (input)

```json
{
  "student_id": "penn_saphira",
  "student_name": "Saphira Penn",
  "class": "B_Day Biology",
  "lesson_slug": "natural_selection",
  "lesson_name": "Natural Selection",
  "lesson_date": "2026-05-07",
  "b2_run_timestamp": "2026-05-17T14:00:00Z",
  "rubrics": {
    "conceptual": "yellow",
    "depth": "red",
    "writing": "yellow"
  },
  "composite": "yellow"
}
```

Color values: `"red"` | `"yellow"` | `"green"` → mapped to 🟥 🟨 🟩 in the doc.

---

## Step 3 — Compute Trajectory Markers

For each student, for each rubric, compute a trajectory marker across their lessons (sorted oldest → newest):

| Marker | Trigger |
|---|---|
| 🚀 Climbing | Last 3 lessons show consistent improvement in rubric color (no holds, no drops) |
| 📈 Improving | Net upward trend across all lessons (more 🟩 in recent half than earlier half) |
| ➖ Steady | Modal color unchanged across last 3 lessons, no net shift |
| ⚠️ Declining | Last 2 lessons show a regression in rubric color |
| 🔵 Too few lessons | Fewer than 3 lessons available |

Color ordering for comparison: red < yellow < green.

**Composite marker** is derived from whichever rubric is most representative (modal across the three) on a per-lesson basis; the trajectory of the composite follows the same rules.

For each **class**, compute trajectory per rubric across all students:

| Marker | Trigger |
|---|---|
| 🚀 Climbing | Two consecutive lessons showed > 10% increase in 🟩 students OR > 10% decrease in 🟥 |
| 📈 Improving | Net upward shift in distribution from first to most recent lesson |
| ➖ Steady | Distribution roughly unchanged across last 3 lessons |
| ⚠️ Sliding | Last 2 lessons show distribution moving toward 🟥 |
| 🔵 Too few lessons | Fewer than 3 lessons for this class |

---

## Step 4 — Read the Existing Growth Doc

1. Fetch the master Google Doc (`c_growth_doc_id` from Config)
2. Parse the existing per-student lesson tables to identify what's already written
3. For each student + lesson already present: skip (unless flagged as updated per Step 2)
4. Collect the list of new (student, lesson) pairs to append

If the doc does not exist yet, create it with the header block and empty sections (see Format Reference).

---

## Step 5 — Update the Growth Doc

### What to write

For each student with new lesson data:

1. Find (or create) the student's section
2. Append the new lesson row to their lessons table, keeping rows sorted oldest → newest
3. Recompute and rewrite the student's trajectory line and header marker
4. If a lesson row was updated (deduplicated): append `(updated <date>)` to that lesson name cell

After all students are updated:

1. Recompute and rewrite each class summary table and narrative paragraph
2. Update the "Last updated" timestamp at the top of the doc

### What NOT to write

- ❌ Letter grades or percentages
- ❌ Individual student comments or feedback (those live in B2's emails)
- ❌ Rewrite directions or rubric definitions
- ❌ Emails, IDs, or identifying info beyond first/last name and class
- ❌ Charts, images, or statistics beyond distribution tables

### Append-only rule

Never delete or replace existing rows in the growth doc. If data changes, mark rows as `(updated <date>)`. The doc is a longitudinal record — past states are intentional history.

---

## Step 6 — Write Summary to Dashboard

After updating the growth doc:

1. Open the Teacher Dashboard
2. For each student row that was updated, set `Last Updated` to today's date
3. **Do not** modify any score columns — C reads scores, it does not produce them

---

## Step 7 — Output Summary

Print a brief summary:

```
Workflow C complete — <date>

Classes processed: B_Day Biology, A_Day Biology
New lesson records appended: 14 (B_Day) + 11 (A_Day)
Updated records (B2 re-run): 0
Students with 🔵 Too few lessons: 3 (only 1 lesson each)
Growth doc updated: https://docs.google.com/...

Class trajectory highlights:
  B_Day Biology — Conceptual: 🚀 Climbing | Depth: 📈 Improving | Writing: ➖ Steady
  A_Day Biology — Conceptual: 🔵 Too few | Depth: 🔵 Too few | Writing: 🔵 Too few
```

---

## Format Reference

See `workflow-c-growth-doc-format.md` for the exact document structure,
including section headers, table layouts, and example output. That file is
authoritative when this skill and the format reference conflict.

---

## Error conditions

| Condition | Action |
|---|---|
| `c_growth_doc_id` missing from Config | Create new doc, save ID to Config, proceed |
| B2 rubric data file is malformed | Log the filename, skip that file, continue — report in summary |
| Student in rubric data not in Dashboard roster | Log the mismatch, include in growth doc anyway (orphaned record note), report in summary |
| Growth doc is not accessible | Halt and report — do not create a second doc |
| Bad email domain detected in any roster read | Halt per email-domain defense rule (see master spec §7) |

---

## Dependencies

- B2 must have run for at least one lesson in the target class
- Dashboard Config must have `dashboard_file_id` and folder IDs for B2 output folders
- kvond12 Drive connector must be active (C reads from kvond12-owned script folders)
- Growth doc must be accessible via Drive connector (school account)
