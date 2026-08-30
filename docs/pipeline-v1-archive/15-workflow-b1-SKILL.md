---
name: workflow-b1-rewrite-grading
description: Grade completion on student rewrite Word documents (Draft-prefixed files). Extracts rewrite text per slide section, scores how many of the 5 expected rewrite sections were substantively addressed, and writes results back to the Teacher Dashboard DRAFT columns and Schoology Master Import DRAFT.<lesson> column. Use this skill whenever Workflow B has run (so emails went out and students are submitting rewrites) and the teacher asks to "run Workflow B1," "grade the rewrites," "score the drafts," or "do B1 on this lesson." Per-student JSON output is consumed by Workflow B2 for rubric scoring.
---

# Workflow B1 — Rewrite Completion Grading

The completion-grading partner of Workflow A, but for the *rewrite* side. A scores annotated slides; B1 scores rewrite Word docs. Same structural role, different input format.

For each student, B1 reads their Draft-prefixed Word document, parses out the 5 rewrite sections (and optional challenge response), scores completion based on how many were substantively addressed, and outputs per-student JSON that Workflow B2 will consume for rubric judgment. B1 also writes back to the Dashboard's DRAFT columns and the Schoology Master Import.

---

## Email policy (no email step today, but pre-flight applies if ever added)

**B1 currently does NOT create student emails** — completion grading only, no drafts. If a future revision adds email notifications to B1, the same Composio-only rule from Workflows B and B2 applies:

- ALWAYS use Composio `GMAIL_CREATE_EMAIL_DRAFT` (kvond12@gmail.com)
- NEVER use any first-party Gmail MCP tool (school account)
- Mandatory pre-flight tool_search before any email step
- HALT cleanly if Composio is not loaded — no silent fallback

Do not add email functionality to B1 without also adding the pre-flight section that exists in Workflow B and Workflow B2.

---

## When to Use

- Workflow B has finished (emails sent out, students are responding with rewrites)
- Students have submitted Draft-prefixed Word docs (or Google Docs) to the lesson's Schoology DRAFTS folder
- Teacher says "run Workflow B1," "grade the rewrites," "score the drafts," or "do B1 on this lesson"
- Always runs **before** Workflow B2, since B2 consumes B1's per-student JSON

---

## Step 1 — Identify Inputs

Three inputs are required:

1. **Student rewrite documents** — Draft-prefixed files, one per student. **Filter rule: only consider files whose names start with `Draft`.** Everything else is ignored (Notes files belong to A, lesson handouts are background, etc.).
   - **Already-DOCX files** (uploaded directly): use as-is.
   - **Google Docs on Drive** (typical Schoology DRAFTS folder content — files appear as `application/vnd.google-apps.document`): download each one with **Google Drive: download_file_content** specifying `exportMimeType: application/vnd.openxmlformats-officedocument.wordprocessingml.document`, decode the base64, and save to a local `.docx`. Composio's Drive integration normally does this conversion automatically on download; the native Drive API needs the explicit `exportMimeType` parameter.
2. **A's output folder** (optional but useful) — contains `answers/<student>.json` from Workflow A. If available, B1 can cross-reference student IDs and confirm A processed the same students. Not required for B1 to run.
3. **Lesson + class context** — e.g., "Evidence of Evolution / B_Day Biology". Used to know which Dashboard sheet to update and which Schoology Master column.

### Resolving folder IDs and Dashboard context
Read the Teacher Dashboard Config sheet (file ID from Config) for:
- Lesson confirmation (does this lesson exist in Config?)
- Folder IDs for the lesson's `01_Input_Student_Work` (or DRAFTS folder) and `03_Workflow_B1_Feedback`
- The Schoology Masters folder

### If no Draft-prefixed files exist
Tell Katherine "no Draft-prefixed files found in [folder]" and stop. Don't grade nothing.

---

## Step 2 — Run the Script

The extractor lives at `scripts/extract_and_grade_rewrites.py`. It uses `python-docx` (install with `pip install python-docx --break-system-packages` if not present).

```bash
python scripts/extract_and_grade_rewrites.py \
    /path/to/draft_docs_folder \
    /path/to/output_dir \
    --lesson "Evidence of Evolution" \
    --class "B_Day Biology"
```

The script:
1. Walks each Draft-prefixed .docx in the input folder
2. Extracts all paragraph text
3. Parses for `Slide N` section markers (the structure students inherit when they paste B's email into their doc)
4. Captures each rewrite section's text, word count, and "addressed" flag
5. Captures the challenge response separately if present
6. Computes completion (5 expected sections, denominator fixed)
7. Writes outputs (see Step 4)

---

## Step 3 — Parsing Logic (How B1 Reads a Rewrite Doc)

Students cut-and-paste Workflow B's email into a Word document and rewrite their answers below each `Slide N — ...` line. The doc structure B1 looks for:

```
Hi <name>,

<praise paragraph from B>

Here are 5 things to make your thinking stronger:

1. Slide 13 — <B's direction>
<STUDENT'S REWRITE OF SLIDE 13>

2. Slide 26 — <B's direction>
<STUDENT'S REWRITE OF SLIDE 26>

3. Slide 11 — <B's direction>
<STUDENT'S REWRITE OF SLIDE 11>

... (etc, up to 5)

Challenge: <B's challenge question>
<STUDENT'S CHALLENGE RESPONSE>

— Dr. von Duyke
```

### Detection markers
- **Section boundaries:** Lines matching `Slide N` (case-insensitive, optionally numbered or bolded). The script uses regex `(?:^|\n)\s*(?:#+\s*)?(?:\*\*)?Slide\s+(\d+)\b`.
- **Challenge marker:** Line beginning with `Challenge` (case-insensitive). The script splits any text after the last slide section into the challenge response if a challenge marker is present.

### "Addressed" threshold
A rewrite section is considered **addressed** if it has **15+ words** of substantive text after the slide marker. This catches:
- Empty sections (zero words) → not addressed
- Single-word answers ("ok", "yes", "I don't know") → not addressed
- "Same as above" or other dodge text → not addressed
- Real attempts at rewriting → addressed

The threshold is a heuristic for *completion*, not for *quality*. B2 judges quality.

### Expected sections denominator
The completion denominator is **always 5** (B always asks for 5 rewrites + 1 challenge). So:
- 5 sections addressed → 100%
- 4 sections addressed → 80%
- 3 → 60%
- 0 → 0%

The challenge response is **tracked separately**, not folded into the completion percentage. It's a bonus signal — addressed or not.

### If the student wrote sections without slide markers
Edge case. If a student wrote a single blob of text without `Slide N` markers, B1 can't map to slides and treats the whole thing as a single unparseable submission. Mark `addressed_count: 0`, flag in the summary, and let Katherine review.

---

## Step 4 — Outputs

```
output_dir/
├── rewrite_completion_report.csv        ← per-student completion scores
├── workflow_b1_summary.md               ← teacher-facing summary
└── rewrites/
    ├── <student_1>.json                 ← consumed by Workflow B2
    ├── <student_2>.json
    └── ...
```

### `rewrite_completion_report.csv`
Columns: `student, rewrite_sections_addressed, total_rewrite_sections_expected, completion_percent, challenge_addressed, total_word_count`

### `rewrites/<student>.json` — the canonical schema (B2's input)

```json
{
  "student": "smith_jane",
  "lesson": "Evidence of Evolution",
  "class": "B_Day Biology",
  "date": "2026-05-21",
  "completion": {
    "rewrite_sections_addressed": 4,
    "total_rewrite_sections_expected": 5,
    "completion_percent": 80.0,
    "challenge_addressed": true,
    "total_word_count": 423
  },
  "rewrites": [
    {
      "slide_number": 13,
      "rewrite_text": "Dolphins and sharks look similar because of convergent evolution...",
      "word_count": 87,
      "addressed": true
    },
    {
      "slide_number": 26,
      "rewrite_text": "...",
      "word_count": 122,
      "addressed": true
    }
    // ...
  ],
  "challenge_response": {
    "text": "If a fourth domain were found, I think...",
    "word_count": 45,
    "addressed": true
  }
}
```

**This schema is the locked contract between B1 and B2.** B2 reads `rewrites[]` keyed by `slide_number` to pair with A's original answers per slide. Don't change it without updating B2 in parallel.

### `workflow_b1_summary.md`
Human-readable Markdown table showing per-student completion and a flag for any docs that couldn't be parsed.

---

## Step 5 — Write Results Back to the Teacher Dashboard

For each student, find their row in the appropriate class sheet (`A_Day Biology`, `B_Day Biology`, `A_Day Forensics`, `B_Day Forensics`) and set:

| Column | Value |
|---|---|
| `DRAFT Submitted` | `Yes` if the student had a Draft-prefixed file in the input folder |
| `DRAFT Score` | The `completion_percent` (0–100) |
| `DRAFT Words` | `total_word_count` from the JSON |
| `DRAFT Date` | Today's date (ISO format) |
| `DRAFT Effort` | **Leave blank — archived metric.** Do not populate. |
| `Last Updated` | Current timestamp |

### Don't touch
- `NOTES *` columns (owned by Workflow A)
- `Email Sent` column (owned by Workflow B)
- `Rubric_*` columns (owned by Workflow B2)

---

## Step 6 — Update the Schoology Master Import

Find the per-class Schoology Master Import spreadsheet in the Schoology Masters folder (from Dashboard Config). For each student row (match by `Student email` or `Unique User ID`), write the completion_percent to the **`DRAFT.<lesson_name>`** column.

Create the column if it doesn't exist (Schoology Master accumulates two columns per lesson over the year: `Notes.<lesson>` from A and `DRAFT.<lesson>` from B1).

### What not to do
- Do not touch `Notes.<lesson>` columns — those belong to Workflow A
- Do not modify roster columns
- Do not add students who aren't already in the import file

---

## Step 7 — Present Files & Next Step

Use `present_files` with:
1. `workflow_b1_summary.md` (most relevant to teacher)
2. `rewrite_completion_report.csv` (archival)

Then tell the teacher:
- How many rewrites were processed
- Dashboard sheet updated, Schoology Master file updated
- Per-student JSON in `rewrites/` is ready for **Workflow B2** (rubric scoring + improvement comparison)
- If any docs couldn't be parsed (no slide markers), flag those students by name so Katherine can investigate

---

## Edge Cases

- **Student submitted a Google Doc, not a Word doc**: Common case — Schoology DRAFTS folders often store student work as Google Docs. Per Step 1, export each one to .docx via `download_file_content` with the Word export mime type before running the script.
- **Student doc has no `Slide N` markers** (one big blob of text): B1 can't map to slides. Treat the doc as 0 addressed sections, flag in summary as "unparseable structure: [student]." Katherine can review manually. Don't fail the whole run for this one student.
- **Student doc has more than 5 slide sections** (they rewrote everything): Score completion as 5/5 (capped at 100%). Pass all sections through to B2 — B2 can score them all on rubrics.
- **Student doc has slide sections out of order** (e.g., Slide 26 first, then Slide 13): Parse them in document order, but B2 reads by `slide_number`, not order. Order doesn't matter for downstream consumption.
- **Student kept B's email intact** (didn't write any rewrites): All sections have only B's direction text after the marker, below the word threshold. Score as 0% addressed. Generate a row in the Dashboard so the student is on record.
- **Student wrote one massive paragraph that addresses multiple slides without markers**: B1 captures whatever's parseable. If only some slide markers are present, score those. If none, flag as unparseable.
- **Two Draft files exist for the same student** (e.g., they submitted twice): Use the most recently modified. Log both in the summary so Katherine can verify.
- **Student didn't get an email from B yet but submitted a Draft anyway**: Process the Draft as-is. The student is engaged; B1 doesn't care about the order in which B and B1 ran for any particular student.
- **A's JSON is missing for a student who submitted a Draft**: Process the Draft. B2 will be the one to flag the mismatch (it needs both A and B1 outputs).
- **Dashboard write fails**: Continue with file outputs but flag the write failure prominently so Katherine knows to update the Dashboard manually.

---

## Notes

- **B1 is more mechanical than B**. No LLM judgment needed for completion — it's text extraction and counting. The script does the work; the SKILL.md just describes the contract and edge cases.
- **B1 does not score rubrics.** That's B2's job. B1 just answers "did the student do the rewrite?" — not "how well did they do?"
- **B1 does not send emails.** No Composio pre-flight needed unless a future revision adds email functionality (in which case the rule from Workflows B and B2 applies in full).
- **The `rewrites[]` schema is load-bearing for B2.** When B1 was built (2026-05-21), this schema was locked. If it changes, update B2's SKILL.md in parallel.
- **Word count is captured but not used in completion math.** It's a useful signal for B2 (long Mastery-tier answers vs short Getting Started answers) and worth preserving in the JSON.

---

## Reference Files

This skill has no reference subfolder — the parsing logic is in the script and the schema is documented inline in this SKILL.md.
