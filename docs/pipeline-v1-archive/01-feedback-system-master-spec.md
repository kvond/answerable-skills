# Feedback System — Master Spec

**Owner:** Katherine von Duyke (Dr. von Duyke)
**Subjects:** 9th Grade Biology + Forensics
**Sections:** A_Day Biology, B_Day Biology, A_Day Forensics, B_Day Forensics
**Last updated:** 2026-05-25

This document is the single source of truth for the student-feedback pipeline. Any Claude model working in this project — Sonnet, Opus, Haiku — should read this first to understand the system before acting on any workflow request.

---

## 1. What this system does

Students annotate lesson slides → submit to Schoology → an automated pipeline grades completion, generates personalized rewrite emails, tracks completion of rewrites, scores three rubrics per assignment, and tracks rubric growth across assignments over time in a teacher-facing view.

The system is built around **Variation Theory (VT)** lesson structure: each lesson has critical-aspect concept questions where conceptual understanding is visible. Those slides are the diagnostic ones — not vocab boxes, not notes, not bellringers. The same VT structure is used in both biology and forensics lessons.

**Historical note:** A predecessor system called **PIPE** was a monolithic runner. PIPE has been decomposed into the current A / B / B1 / B2 / C workflows. References to "PIPE" in older artifacts (Dashboard README, Activity Log) are legacy. What was formerly called B3 is now **Workflow C**.

---

## 2. The five workflows

| ID | Name | Input | Output | Run timing |
|---|---|---|---|---|
| **A** | Completion Grading | Teacher template + student annotated decks | Completion CSV + per-student JSON | After student submission |
| **B** | Personalized Email Generator | A's per-student JSON | Email to each student | Pipeline with A |
| **B1** | Rewrite Completion Grading | Student rewrite Word docs (DRAFTS folder) | Completion score | After student rewrites |
| **B2** | Per-Assignment Rubric Summary | A + B1 outputs | Student summary + class report | Separate run |
| **C** | Longitudinal Growth Tracking | Accumulated B2 outputs | Per-student rubric growth view + class trajectory | Separate run, periodic |

### Pipeline structure

```
[vt-insert-slides skill]      [extract-lesson-materials skill]
       │                                │
       ↓                                ↓
  Lesson deck                  Lesson reference doc
       │                                │
       ↓                                │
 Students annotate ──► [A] ──► [B]      │
                                │       │
                                ↓       ↓
                       Email to student + ref doc
                                │
                                ↓
                       Student rewrites in Word doc
                                │
                                ↓
                       Schoology DRAFTS folder ──► [B1]
                                                    │
                                                    ↓
                                                 [B2] ──► Master Growth Doc ──► [C]
```

---

## 3. The student experience

This is what makes the system work pedagogically — keep it in mind when designing or modifying any workflow:

1. Student annotates lesson slides (during/after class)
2. Submits to Schoology lesson folder
3. Receives personalized email: specific praise + the lesson's 5 diagnostic slides with every question (verbatim from the template) + a single rewrite ask + a one-line tier steer
4. Cuts & pastes email into a Word document
5. Opens original assignment alongside (sees the question + their annotated answer + lesson reference doc)
6. Rewrites answers in the Word doc
7. Submits Word doc to Schoology DRAFTS folder

**Why this design:** Personal email feels manageable, not overwhelming. Cut-and-paste into Word gives them context and ownership. The Word doc is editable and analyzable (unlike paper) for teacher review. Five rewrite directions is the sweet spot — focused enough to do, broad enough to learn from.

---

## 4. Detection logic (critical-aspect slides)

The VT insert workflow produces consistent structural patterns. The script in Workflow A detects four diagnostic slide types from the teacher template:

| Slide type | Detection signal |
|---|---|
| **3-tier concept question** *(primary diagnostic)* | All three labels `Getting Started`, `Working On It`, `Mastery` appear on the same slide |
| **Pattern break** | Slide contains the phrase `Pattern Break` in title or body |
| **Build-a-rule / What-if** | Slide contains `Build a Rule` or `What If` in title or body |
| **Contrast set** | Slide contains `Contrast` in title or body |

Non-diagnostic slides (vocab boxes, image slides, bellringers, agendas) are skipped by A.

---

## 5. Scoring — Workflow A (completion)

A measures **completion** of the lesson's diagnostic slides, not conceptual quality. Quality scoring is B2's job.

| Metric | Description |
|---|---|
| `answered_diagnostic_slides` | # of diagnostic slides where student wrote ≥ 15 words |
| `total_diagnostic_slides` | # of diagnostic slides in the teacher template |
| `completion_percent` | `answered / total × 100`, rounded to nearest int |
| `total_words` | Total word count across all student-typed text in the deck |

Completion percent is what gets written to the Dashboard's `NOTES Score` column and to the Schoology Master Import `Notes.<lesson>` column.

---

## 6. Rubric scoring — Workflow B2

B2 scores three rubrics on each student's rewrite. Each rubric produces a color (🟥 🟨 🟩).

| Rubric | What it measures |
|---|---|
| **Conceptual Accuracy & Vocabulary** | Correct use of lesson vocabulary; accurate description of mechanism or relationship |
| **Depth of Explanation** | Causal reasoning: does the student explain *why* or *how*, not just *what* |
| **Scientific Writing Quality** | Complete sentences, specific claims, appropriate hedging, no vague filler |

The student's chosen tier is itself a signal; the rubric scoring then assesses whether their explanation matches the tier they attempted.

---

## 6b. Originality watch

Not a rubric. Conditional callout in **Workflow B's email** when triggered:

- **Answer match** — student's text is too similar to another student's, or to verbatim slide text
- **Vocabulary anomaly** — words appear that are outside the student's normal writing baseline

These are flags, not scored growth dimensions. If they trip, B notes it in the email; it doesn't carry into rubric tracking.

---

## 7. Storage architecture

### Two accounts, distinct roles

| Account | Role |
|---|---|
| **`katherine.vonduyke@redclay.k12.de.us`** (school Workspace) | Operational hub: lessons, student work, outputs, Dashboard, Schoology Master imports. Where the day-to-day pipeline lives. |
| **`kvond12@gmail.com`** (personal / AI Workspace) | AI scaffolding + **email sending**: skills, scripts, Composio integration, Gmail drafts. **All outbound student emails are drafted from this account via Composio.** |

School account *cannot* connect to Composio (district policy). Personal account *can*. This is why the split exists.

### Email sending rule — HARD

All student emails (Workflow B) are drafted via **Composio → kvond12@gmail.com**. The school Gmail account (`katherine.vonduyke@redclay.k12.de.us`) is **never** used for sending. Do not use the Gmail MCP connector (which authenticates to the school account) for draft creation.

### Key files and folders

| Location | File ID (where useful) | Account | Purpose |
|---|---|---|---|
| **Teacher Dashboard 4** | `1FMWx8ueSgcJVAXc5IzuR9F1Wb5JG92LM-Bj7rMiZAwE` | school | Central tracking artifact. **Source of truth for student rosters, lesson list, folder IDs, and per-student-per-lesson state.** Read Config sheet first to resolve any folder ID. After uploading a new Dashboard version, update `dashboard_file_id` in Config with the new file's ID. |
| FEEDBACK_AI_WORKSPACE | `1DtpJZuQvlabCGgBm6GdmB9SfAK5Z0rg4` | kvond12 | Top-level home of AI scaffolding. Contains Dashboard and `VT Lesson Skills/`. |
| Bio_Pipeline (Do NOT Delete) | `1ey4ZCc1fAU75kQJDhBxVxv6oKOmBn87S` | kvond12 | Container for `scripts (Do NOT Delete)/`. |
| scripts (Do NOT Delete) | `1SEe_chKL1lQ2anjoj0QoDNGkfKXBzvDS` | kvond12 (shared anyone-can-edit) | Holds workflow skill files in per-workflow subfolders (`Workflow A/`, `Workflow B/`, `Workflow B1/`, `Workflow B2/`, `Workflow C/`). |
| VT Lesson Skills | `1en8trGm5GgpxCHbxuMbWzlY5jeJ2T6ce` | school | Holds upstream skill files: `vt-insert-slides/` and `extract-lesson-materials/`. |
| Schoology Masters folder | `1zZWhsdm5RVxPObOqFquSVbTf2kR84rib` | school | Per-class Schoology Master Import spreadsheets. Workflow A writes the `Notes.<lesson>` column; Workflow B1 writes the `DRAFT.<lesson>` column. |
| Schoology Google Drive root | `18ZOnISxkNmDVrjxJjCpaZLeTqVYF6fK7` | school | Schoology's automatic sync target. Student NOTES and DRAFT submissions land here. |

### File naming convention for student submissions

The pipeline only looks at student files whose names start with **`Notes`** or **`Draft`**. Everything else is ignored — exemplars, teacher notes, lesson decks, scratch files, etc.

| Prefix | Type | Consumed by |
|---|---|---|
| **`Notes...`** | Annotated lesson slides (the original assignment) | Workflow A |
| **`Draft...`** | Rewrite Word documents (the revised work after receiving feedback) | Workflow B1 |

This is a hard filter — neither Workflow A nor B1 processes a file without the correct prefix. If a student names their submission incorrectly, it doesn't get scored. Teacher can rename and re-run.

### Student email construction — HARD rules

- Email format: `s.firstname.lastname@redclay.k12.de.us`
- **Strip hyphens from last names.** Example: `Gillison-Wallace` → `gillisonwallace`. Confirmed 2026-05-20.
- All recipient emails MUST come from master rosters at Schoology Masters/ (`1zZWhsdm5RVxPObOqFquSVbTf2kR84rib`), NEVER from extracted_responses.xlsx or Drive file owner.
- Domain must be `@redclay.k12.de.us` — NOT `@redclayschools.com` (that is the Workspace login domain, not delivery domain).
- Three defense layers: A §3.2 (canonical at source), B1 §2.5 + B2 §2.4 (re-verify), B1 §14.3 + B2 §13 (halt on bad domain).

### Teacher template file IDs in Dashboard Config

Each lesson's VT-inserted teacher template **must have an explicit file ID stored in the Dashboard Config sheet.**

| Class | Config key pattern |
|---|---|
| A_Day Biology | `a_day_<lesson_slug>_template_id` |
| B_Day Biology | `b_day_<lesson_slug>_template_id` |
| A_Day Forensics | `a_day_forensics_<lesson_slug>_template_id` |
| B_Day Forensics | `b_day_forensics_<lesson_slug>_template_id` |

Workflow A reads this field as the authoritative pointer to the template. **Do not let any workflow guess by filename.**

---

### Per-lesson folder convention

```
[<Lesson Name>] <Class> Output/        ← e.g., [Evidence of Evolution] B_Day Output
├── 01_Input_Student_Work/             ← submissions (sometimes via Schoology folder instead)
├── 02_Workflow_A_Output/               ← A's CSV + JSON outputs land here
├── 03_Workflow_B1_Feedback/            ← B1's outputs land here
└── 04_Workflow_B2_Summary/             ← B2's rubric summary lands here
```

There's no 02b folder for B's emails — those go directly to Gmail drafts (kvond12). There's no 05 folder for C — its output is the master Google Doc.

### (Do NOT Delete) naming rule

Any folder or file the pipeline depends on must have `(Do NOT Delete)` in its name. Katherine is prone to reorganizing files; this label is the only protection.

### Dual-account ownership artifact (when Claude creates files)

When Claude operates through the native Google Drive connector, it acts as the **school account**. Files created inside kvond12-owned folders end up school-owned. These surface in school's "My Drive" root view as a side effect.

**Cleanup pattern:** right-click → `Remove from My Drive` (NOT `Delete`).

---

## 8. Tracking surfaces

Four artifacts get updated by the pipeline.

### Teacher Dashboard (per-class sheet) — v2 structure

Dashboard v2 (uploaded 2026-05-25) has a **lesson-row structure**: one row per student per lesson (not one row per student). This allows multi-lesson tracking without column proliferation.

Columns per row:
`Student Name | Email | Lesson | NOTES Submitted | NOTES Score | NOTES Words | NOTES Date | DRAFT Submitted | DRAFT Score | DRAFT Words | DRAFT Date | Email Sent | Last Updated`

- **Workflow A writes:** `NOTES Submitted, NOTES Score, NOTES Words, NOTES Date, Last Updated`
- **Workflow B writes:** `Email Sent, Last Updated`
- **Workflow B1 writes:** `DRAFT Submitted, DRAFT Score, DRAFT Words, DRAFT Date, Last Updated`
- **NOTES Effort / DRAFT Effort:** **Archived.** Do not populate from any new workflow run.
- Match rows by `(Student Name, Lesson)` composite key — a student will have one row per lesson.

### All Classes sheet (Dashboard tab)

New in Dashboard v2. Schoology import master view across all four classes. Columns:
`Class | First Name | Last Name | Email | Unique User ID | Notes.<lesson> | DRAFT.<lesson> | ...`

- Pipeline writes `Notes.<lesson>` and `DRAFT.<lesson>` columns (completion percent).
- `Unique User ID` is populated from the Schoology Master Import files — the pipeline cannot generate these IDs.
- Katherine copies each class block into the matching Schoology Master Import sheet and posts grades as 100.

### Schoology Master Import (per-class spreadsheet)

Columns: `First Name | Last Name | Student email | Unique User ID | Notes.<lesson> | DRAFT.<lesson> | ...`

- **Workflow A writes:** `Notes.<lesson>` (completion percent)
- **Workflow B1 writes:** `DRAFT.<lesson>` (rewrite completion percent)

### Workflow C Master Growth Doc (single Google Doc, accumulating)

Owned by Workflow C exclusively. Stores the 3-rubric 🟥🟨🟩 trajectory per student plus whole-class trajectory across all lessons. Append-only — never delete or replace. See `workflow-c-growth-doc-format.md` for the exact layout.

---

## 9. Related skills (upstream of this pipeline)

Both are foundational and feed the pipeline. Do not delete.

- **`vt-insert-slides`** — Builds the source decks. Produces the consistent R/Y/G three-tier structure that Workflow A detects.
- **`extract-lesson-materials`** — Builds the lesson reference doc (vocabulary, critical aspects, causal chains) that students consult during the rewrite step.

---

## 10. Build status

| Workflow | Status | Notes |
|---|---|---|
| A | ✅ Built + Dashboard-integrated | `workflow-a-completion-grading` skill. Filters Notes-prefixed files. Writes to Dashboard NOTES columns and Schoology Master `Notes.<lesson>` column. |
| B | ✅ Designed + documented | `workflow-b-personalized-emails` skill. Reads roster from Dashboard, creates Gmail drafts via Composio (kvond12), updates `Email Sent` column. |
| B1 | ✅ Built + Dashboard-integrated | `workflow-b1-rewrite-grading` skill. Filters Draft-prefixed files. Output schema (`rewrites/<student>.json`) is locked — this is what B2 consumes. |
| B2 | ✅ Designed + documented | `workflow-b2-rubric-summary` skill. Scores 3 rubrics on rewrite, writes rubric data file for C to consume. |
| C | ✅ Designed + documented | `workflow-c-growth-tracking` skill *(formerly B3)*. Reads accumulated B2 rubric data files. Updates master Google Doc with per-student 🟥🟨🟩 trajectories + class trajectory. Append-only. Idempotent. |

**Pipeline order:** A → B (emails) → student rewrites → B1 → B2 → C.

---

## 11. Operating conventions

- **For Claude (any model) working in this project:**
  - Read this spec before starting any workflow task
  - When a workflow needs a roster, lesson list, or folder ID, **read the Teacher Dashboard Config sheet first** — that's the source of truth. File ID is in the Config tab `dashboard_file_id` row (check Config for the current ID after any Dashboard upload).
  - Confirm which class section before reading or writing to the Dashboard
  - Dashboard row lookup: match on `(Student Name, Lesson)` composite key
  - **Email drafts: always use Composio (kvond12@gmail.com), never the Gmail MCP connector**
  - Do NOT populate `NOTES Effort` or `DRAFT Effort` columns — archived
  - The `(Do NOT Delete)` suffix on folders is load-bearing — never strip it, never create pipeline-critical folders without it
  - Pipeline scripts: always use deployed versions from `scripts (Do NOT Delete)/` folder `1SEe_chKL1lQ2anjoj0QoDNGkfKXBzvDS` — never reconstruct from memory

- **For Katherine:**
  - After uploading a new Dashboard to Drive: copy the new file ID from the URL and paste it into Config tab, row `dashboard_file_id`, Value column. That's it — one cell.
  - Skill files live in `scripts (Do NOT Delete)/Workflow X/` subfolders
  - Pipeline operational state lives in the Teacher Dashboard (school account)
  - Lesson outputs go to per-lesson folders in school account, structured as `[Lesson Name] <Class> Output/`
  - C master Google Doc is the longitudinal record — never delete or replace, only append
  - When files show up in your school My Drive root view after pipeline runs: **right-click → Remove from My Drive (NOT Delete)**
  - Schoology sync-break signature: doubled course noun in folder title (e.g., `Forensics 0476 1 Forensics - …`). Fix by aligning Drive to Schoology or editing course mapping in Schoology UI.
