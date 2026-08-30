# Pipeline Checklist — Grading Run (with Grades Preflight)

Open a **new chat in the Feedback project** so Sonnet has the full spec and all workflow skills. Work top to bottom. Don't skip the preflight — it's the step that catches the problems that cost the most time later (missed submissions, wrong-folder work, stale IDs, broken sync).

The single source of truth is **Teacher Dashboard** (the workbook with the four class tabs + the `ALL-open to sync before import` tab). You grade in the class tabs; the All tab assembles itself by formula.

---

## 0 — Session setup

- [ ] New chat in the Feedback project (full spec + skills in context).
- [ ] Confirm Composio is connected (answerableteaching). If a Drive/Sheets call errors, **retry first** — transient "upstream MCP server" blips are common — before reporting a disconnection.
- [ ] Default all Drive/Sheets/Docs through **Composio (answerableteaching)**, never the first-party Google Drive connector (it blocks AI-restricted school files).
- [ ] Read the **Config + Pipeline Reference** sheet for current asset/folder/script IDs. Never reconstruct script IDs or pipeline scripts from memory — use the deployed scripts.
- [ ] Start a visible session checklist and keep it updated as you go.
- [ ] **Model routing:** grading (Workflow A / B1 / B2, Aspect-Anchored Grader) stays on **Sonnet** — it's the judgment layer. Route bulk/mechanical work (Roam dedup sweeps, citation formatting, CSV/Schoology-import prep) through **Haiku** instead — 3x cheaper, no Sonnet-level reasoning needed there. Reserve **Opus** for the manuscript's hardest conceptual passages only — never this pipeline.
- [ ] **Batch size cap:** grade **one class section per session** (~25–35 students) rather than all four classes back to back in one thread — long threads re-send full context every turn, which is where cost compounds. The preflight (step 1) may still scan all four classes for awareness; **actual grading (step 2) stays scoped to one section per run.** Split further at a roster boundary if a section runs 40+.

---

## 1 — GRADES PREFLIGHT  *(do this before any grading or importing)*

The preflight answers one question: **"Is the dashboard a true and complete picture of what students actually submitted?"** Run every box before processing new work or building an import.

### 1a. Fresh scan, never grade off stale state
- [ ] Run a **fresh scan** for new work across all four classes. Never email or import off a previous run's state.
- [ ] Check the **Schoology Submissions tab** for work orphaned by any Schoology↔Drive sync break (signature: a duplicated root folder with the course noun doubled, or a "Back up <assignment>" filename prefix).

### 1b. Wrong-folder / missed-work sweep  *(this is where real work hides)*
- [ ] For any student who looks like a non-submitter on a tracked lesson, **search Drive by their name across all folders** — not just the lesson folder. Misfiled work won't appear in a lesson-scoped scan.
- [ ] When a file is found, **open and read it** before concluding anything. A file existing ≠ work done; a blank-looking extract ≠ truly blank. Confirm by reading the actual answer fields.
- [ ] Distinguish three cases explicitly: **(1) real work, missed** (grade it), **(2) file present but blank/template** (not submitted), **(3) wrong lesson content** (record where the content actually belongs, not where the filename says).

### 1c. Scope check  *[HARD]*
- [ ] Only process **NOTES** and **DRAFT** submissions. For any other file type, note only whether NOTES/DRAFT is present or missing.
- [ ] **Tracked lessons only:** Biology — Natural Selection, Introduction to Evolution, Evidence of Evolution, Classifying Organisms. Forensics — Time of Death, What is Death?.
- [ ] **Never process:** Pig Autopsy, Stages of Decomposition. Don't add them back without an explicit request.

### 1d. Identity & roster integrity  *[HARD]*
- [ ] **Class membership:** look up each student across the Dashboard class tabs to determine class and existing NOTES/DRAFT columns. **Never assume class from filename or folder.**
- [ ] **Emails** come only from the master rosters at Schoology Masters/ — never from `extracted_responses.xlsx` or a Drive file's owner. Validate the domain is `@redclay.k12.de.us` (not `@redclayschools.com`).
- [ ] **Unique User IDs** must be present on each class-tab row for the All tab to sync. If any are missing, harvest them from existing per-lesson Schoology import CSVs / gradebook exports before importing. (UIDs are NOT stored anywhere except those CSVs and the dashboard's UID column.)
- [ ] **Inactive students:** Sha'rod Watson (A_Day Biology) — skip all pipeline runs; keep his row for record only.

### 1e. Authenticity & similarity pass
- [ ] Flag answers that read copied/textbook/AI vs. a 9th-grader's own voice as **authenticity: suspect** — do not award Mastery on those words.
- [ ] Honor any **similarity notice** embedded in a rewrite doc (students matching each other). Decide per Katherine: grade-as-is-with-flag, or copied-work note.
- [ ] Remember a high score can still be an innocent mix-up (e.g., a strong rewrite filed under the wrong lesson). Record where the **content** belongs; don't assume bad intent.

### 1f. Preflight sign-off
- [ ] Produce a short **preflight report**: per class/lesson — new NOTES, new DRAFTS, missed/recovered work, blanks, flagged students, any missing UIDs or bad emails.
- [ ] **Stop and get Katherine's confirmation** on anything ambiguous (recovered work, flagged/suspect, wrong-lesson content) **before** writing grades.

---

## 2 — Grade  *(after preflight sign-off)*

- [ ] Scoring is **0–100**, denominator always 100, regardless of slide count. `(answered/total)×100`, round to nearest int.
- [ ] **NOTES** (Workflow A) and **DRAFT/rewrite** (B1/B2) per the deployed workflow skills.
- [ ] **Drafts** are judged on **conceptual sense only** (sound/partial/not-yet/blank) — no word-count, length, or polish scoring. Grammar is separate informational feedback. Drafts done under testing conditions are authentic.
- [ ] **Praise [HARD]:** evidence-specific, with a verbatim quote of the student's **own** words (a real substring, not echoed prompt text), and a student-specific explanation after the em-dash — no template phrases. Run the SELF_CHECK: drop any quote that isn't the student's own or is shared across students.
- [ ] Color-code tiers everywhere: 🟩 Mastery `#1E8449` / 🟨 Working On It `#D68910` / 🟥 Getting Started `#C0392B` / ⬜ Blank `#7F8C8D`.

---

## 2.5 — Agency coding pass (Workflow D1)  *(rides on the already-extracted text)*

- [ ] Over the SAME student text this run already extracted (NOTES + DRAFT), run the **Agency Scan** codebook (`16-agency-scan-SKILL.md`). No new downloads.
- [ ] This is **not grading** — it never writes to the Dashboard and is orthogonal to A/B scores. Most answers code to nothing; that is correct.
- [ ] Flag segments of participatory agency — **ENG** (engaged), **EPI** (epistemic), **AUT** (authorial), **CAND** (unclear) — each with a **verbatim excerpt** (substring of the student's own words), a student-specific note, and a one-line discussion opener.
- [ ] Run the SELF_CHECK (same as praise): drop any excerpt that isn't the student's own words or is echoed prompt text.
- [ ] **Append** rows to the **Agency Watch** sheet → `Coding Master` tab (`DEAD_ID_2026-08-09:18Cc-edFsozcn_04-1r1oUCouy6kFhUuFdeWOO3HWa3s`), `status = new`. Append-only — never overwrite (protects Katherine's verdicts). The `Before Class` tab surfaces them automatically for pre-class review.
- [ ] Report a one-line count per class. Dialogic-reply drafting and the inbound "agency sweep" are **separate on-demand triggers** — do not run them here.

---

## 3 — Write back to the dashboard  *(class tabs only)*

- [ ] Write grades to the **class tab** only: Workflow A → NOTES Submitted/Score/Words/Date (+ NOTES Tier). B2 → DRAFT Submitted/Score/Date (+ DRAFT Tier, rubric columns).
- [ ] **Never write to the `ALL-open to sync before import` tab** — it's formula-driven. Overwriting a formula cell with a static number silently breaks that student's sync.
- [ ] **Blank = not submitted; 0 = submitted but answered nothing.** Keep them distinct.
- [ ] If a brand-new lesson is graded for the first time, the All tab needs a one-time `Notes.<lesson>` / `DRAFT.<lesson>` column-pair addition. Flag it; don't restructure the All tab mid-run.
- [ ] Bump the dashboard version; keep one canonical copy with a changelog (no divergent copies).

---

## 4 — Feedback emails  *(human sends)*

- [ ] Produce a **Word (.docx)** with one section per student: clear header with student name + email, color-coded tiers. Subject: `Your work on [Lesson] — where your thinking landed`.
- [ ] **Katherine sends** via the Claude Chrome extension. **Never auto-send** student grade emails through Gmail — minors, parents, and authenticity-flagged messages need human approval. No Composio Gmail, no school Gmail MCP for distribution.
- [ ] Give the flagged/blank/copied messages an extra read before sending.

---

## 5 — Schoology import

- [ ] 🔔 **SCHOOLOGY IMPORT — YOUR TURN.** Gradebook import is a manual step (Option C): the pipeline produces the data, Katherine imports.
- [ ] **OPEN the dashboard first so the `ALL-open to sync before import` tab recalculates**, then import from that tab. The tab name itself is the reminder: `ALL-open to sync before import`.
- [ ] The All tab is **one row per student, one column per assignment** — the format Schoology expects. Blanks are left empty (no overwrite); zeros import as zeros on purpose.
- [ ] If you ever copy the All tab out to a separate file, **paste as values** so scores survive without the class-tab formulas.

---

## 6 — Growth documentation

- [ ] Update the **Growth Tracker** (Notes sheet for NOTES, Drafts sheet for DRAFTS) with conceptual tiers and rubric source.
- [ ] For admin reporting, the **Technical Writing Growth Report** is the confirmed format for formal data submission.

---

## 7 — Close out

- [ ] Re-list the current canonical versions (Dashboard vN, Growth Tracker vN) and what Katherine still needs to do: send emails (Chrome extension), open-and-import (Schoology), re-upload dashboard/tracker if applicable.
- [ ] Note anything held for Katherine's decision (recovered work, flagged students, ungraded lessons).
- [ ] Drop the orphaned-work reminder once the relevant pending item is resolved and Katherine confirms nothing else was affected.

---

### Why the preflight matters
Almost everything recovered in past sessions **existed but was unprocessed, misfiled, or had blank rewrite boxes** — not lost. The preflight is the cheap insurance against shipping an incomplete gradebook. Week-by-week assignment windows reduce this problem at the source; until then, the wrong-folder sweep (1b) is the highest-value box on this list.
