---
name: workflow-b-personalized-emails
description: Generate personalized rewrite-feedback emails as Gmail drafts for each student, based on Workflow A's per-student JSON output. Reads the class roster from the Teacher Dashboard and updates the Email Sent column after drafts are created. Use this skill whenever Workflow A has finished and the teacher asks to "run Workflow B," "create the feedback emails," "draft the rewrite emails," "send feedback to students," or "do B on this lesson." Each draft contains specific praise referencing what the student wrote, the lesson's 5 diagnostic slides with every question reproduced verbatim, a single rewrite instruction, a one-line per-student tier steer, and a conditional originality note. Drafts land in Gmail for the teacher to review and send.
---

# Workflow B â Personalized Email Generator

The content-judgment partner of Workflow A. A extracts; B writes.

For each student, B reads A's per-student JSON, analyzes their answers on the diagnostic slides, and drafts a personalized email containing specific praise, the lesson's 5 diagnostic slides with every question verbatim, a rewrite instruction, a one-line tier steer, and (when triggered) an originality callout. Drafts are created in the teacher's Gmail for review before sending.

---

## â ï¸ Pre-flight (MANDATORY â do this FIRST, before any other step)

This is a hard requirement. Skip it and the workflow fails or â worse â drafts emails from the wrong account.

1. Call `tool_search` with query `"composio gmail draft email"`
2. Confirm a Composio Gmail draft tool (named `GMAIL_CREATE_EMAIL_DRAFT` or equivalent Composio-prefixed name) is returned and loaded
3. **If found:** proceed to Step 1
4. **If NOT found:** HALT IMMEDIATELY. Output verbatim:

   > Composio Gmail tool not loaded â Workflow B cannot create drafts. The first-party Gmail MCP connector is authenticated to the school account (`katherine.vonduyke@redclay.k12.de.us`) and is **forbidden** for student emails. Please verify Composio is connected and enabled in **Settings â Connectors**, then re-run this prompt.

5. **Never** fall back to the first-party Gmail connector for student emails. Never offer to draft via the school account. Never say "I'll just use the available Gmail tool instead." The rule is: Composio (kvond12) or nothing.

**Why this matters:** The school Gmail connector and the Composio Gmail tool both surface in this chat. The school one is wrong (sends from Katherine's school identity, breaks the kvond12 convention, may hit district mail filters). The pre-flight is the only thing that prevents silent fallback to the wrong tool.

---

## When to Use

- Workflow A has finished and produced `answers/<student>.json` files
- Teacher says "run Workflow B," "draft the rewrite emails," "create the feedback emails," or similar
- Teacher uploads or references A's output folder

**Do not run B before A.** B consumes A's output; without it there's nothing to read.

---

## Step 1 â Identify Inputs

Three inputs needed:

1. **A's output folder** â contains `answers/<student>.json` files (one per student), plus optionally `completion_report.csv` and `workflow_a_summary.md`.
2. **Lesson + class context** â which lesson and which class section (e.g., "Evidence of Evolution / B_Day Biology"). Used to know which Dashboard sheet to read for the roster, which lesson name to use in the email subject, and which row to update with `Email Sent`. If not explicitly stated, infer from the lesson folder name (e.g., `[Evidence of Evolution] B_Day Output` â lesson=`Evidence of Evolution`, class=`B_Day Biology`).
3. **Teacher signature** â Katherine's preferred sign-off. If not provided, default to `â Dr. von Duyke`.

### Roster source: the Teacher Dashboard
Open the **Teacher Dashboard** (file ID resolved from Config) and read the appropriate class sheet:
- `A_Day Biology` / `B_Day Biology` for biology lessons
- `A_Day Forensics` / `B_Day Forensics` for forensics lessons

The sheet has columns `Student Name | Email | Lesson | NOTES Submitted | NOTES Score | ...`. Match A's per-student JSON files to roster rows by `student_id` â first/last name derived from `Email` (email format is `s.firstname.lastname@redclay.k12.de.us`, so reverse-engineer the ID from there).

**Strip every non-letter (hyphens, apostrophes, spaces) from names when constructing emails.** `Gillison-Wallace` → `gillisonwallace`, `Son'jai` → `sonjai`. `workflow_b_lint.py` rejects any recipient that isn't `s.first.last@redclay.k12.de.us`.

### If a student's JSON has no matching roster row
Skip that student and report them in the summary at the end. Example: "3 students processed, 2 skipped â no roster entry: ['jones_alex', 'doe_pat']". Do not guess email addresses from filenames.

### If the Dashboard sheet is empty or missing
Stop and ask Katherine. Without the roster, B can't address emails.

---

## Step 2 â Read Each Student's Data

For each student JSON in `answers/`:

- Pull `student`, `completion`, and the `slides` array
- Filter `slides` to only `is_diagnostic: true` AND `answered: true`
- For each diagnostic slide:
  - Note `slide_type` (critical_aspect_concept_question, pattern_break, build_a_rule, what_if)
  - Note `critical_aspect` (the named aspect)
  - Read `student_text` (the actual answer)
  - For 3-tier slides: note `word_bank` and infer `tier_attempted` from content (see Step 3)

---

## Step 3 â Analyze Each Answer

### Tier detection (3-tier concept question slides only)

A leaves `tier_attempted: null` because tier judgment requires content reading. B does it by comparing the student's answer against the three tier prompts and deciding which one the answer is *actually attempting*:

- **Getting Started** â the answer names an example, identifies a case, or restates something from the lesson without explaining mechanism
- **Working On It** â the answer engages with *why* the simple rule isn't enough, but stops short of explaining what specifically the rule has to be based on
- **Mastery** â the answer explains the critical aspect with causal reasoning, connecting cause to effect or function to mechanism

A short, surface-level answer almost always = Getting Started even if the student wrote it under the Mastery prompt. Length matters less than depth of reasoning.

**Do not score rubrics here.** B2 does the formal rubric scoring (Conceptual Accuracy & Vocabulary, Depth of Explanation, Scientific Writing Quality). B's job is to identify *what to rewrite*, not to assign ð¥ð¨ð© colors.

### Originality watch

For each diagnostic slide answer, check two flags:

1. **Slide-text match** â does the student's answer copy phrasing directly from the slide (other than the word bank, which is meant to be used)? Look for verbatim sequences of 5+ words from the slide.
2. **Vocabulary anomaly** â does the answer use terminology that's notably outside this student's normal writing? Compare against their answers on *other* slides in the same submission. If a student writes "convergent evolution caused phenotypic similarity" on one slide and writes "they look the same" on every other slide, that's anomalous and worth a gentle note.

Originality flags are **conditional callouts** in the email, not scored dimensions. Note them when triggered, otherwise omit.

---

## Step 4 — Generate Email Content

The email is a **lesson-constant block** (the 5 diagnostic slides with *every* question, reproduced verbatim from the template deck — identical for every student in the lesson) wrapped in **per-student** content (praise + a one-line tier steer + an optional originality note). Build the lesson-constant block **once** per lesson from the template deck; never paraphrase a question, drop a tier, or invent a slide. The rewrite is the heaviest cognitive lift we ask of students — the email hands them the exact prompts and gets out of the way.

### Email structure (every email follows this)

```
Subject: Your work on <Lesson Name> — what to rewrite

Hi <first_name>,

<Praise — 2–3 sentences, quotes the student's own words, slide cited>

Here are the 5 slides and every question on them. Rewrite your answer to each one — your own words, full sentences. On the slides with three levels, answer the one you can reach, then try to push to the last one.

Slide <N> — <critical aspect>
• <question, verbatim from the template>
  (3-tier slides: all three tier questions with their Getting Started / Working On It / Mastery labels, then the "Word bank — …" line)

… all 5 diagnostic slides, in slide order …

<one-line tier steer — per student>
<optional originality note — only if a flag is triggered>

When you're ready: open your slides and your lesson notes side-by-side, rewrite your answers in a Word document, and submit it to the DRAFTS folder in Schoology.

— Dr. von Duyke
```

### Lesson-constant slide/question block — build it ONCE per lesson

- Take the 5 diagnostic slides from A's JSON (`is_diagnostic: true`), in slide order.
- For each, read the slide text **from the template deck** (not a student deck — student decks carry answers and reflow noise) and reproduce the prompt(s) **verbatim**:
  - `build_a_rule` → the "Finish this rule…" stem.
  - `critical_aspect_concept_question` (3-tier) → all three tier questions with their labels, then the "Word bank — use any, modify any, use none:" line and its terms.
  - `what_if` → the What-If question plus its "reason it through" line.
- This block is **identical for every student**. Generate once, reuse. Drift here corrupts the assignment for the whole class.

### Praise paragraph — guidance

- 2–3 sentences, warm but not gushing.
- **Must quote the student's own words** — a verbatim substring of their `student_text`, in double quotes, slide cited. Student-generated content only, never echoed prompt text. (HARD rule; `workflow_b_lint.py` enforces the substring check in Step 4.5.)
- If they reached Mastery on any 3-tier slide, name it. If completion was high, note the effort.
- Never generic ("Great job!" / "Nice work!").
- **Blank deck (0 diagnostic answers):** no quote is possible — replace praise with a short, warm "let's get your thinking down" line. Do **not** fabricate a quote.

### Tier steer — guidance (replaces the old per-slide rewrite directions)

One line, per student, telling them where to aim on the shared question set. Differentiation lives here and *only* here — the question block itself never changes per student.

- **Strong / reached Mastery across the board** → "Go straight for the Mastery question on the three-level slides — and the What-If slide is where I most want your thinking."
- **Mixed** → "Answer every slide; on the three-level ones, reach for at least Working On It."
- **Weak / blank** → "Start with the *Getting Started* question on each slide. Come find me and we'll do the first two together." — lowers the *entry* demand, not the ceiling; the Mastery questions stay on the page.

Do not rewrite, paraphrase, or scaffold individual questions per student. The scaffold is the steer line; the prompts are constant.

### Originality note (conditional) — guidance

Only include if triggered (see Step 3). Keep it short and non-accusatory:

- Slide-text match → "Quick note: some of your answer on slide <N> looked very close to what's written on the slide itself. In the rewrite, put it in your own words — that's how I can tell what *you* understand."
- Vocabulary anomaly → "Quick note: the wording on slide <N> sounds different from how you usually write. If a friend or another source helped, that's fine to mention — just make sure the rewrite reflects your own understanding."

Never both flags in one email — pick the stronger signal.

## Step 4.5 — Validate before drafting (workflow_b_lint.py) [MANDATORY]

Run the deployed `workflow_b_lint.py` on each composed email **before** creating its Gmail draft. It is a dumb deterministic validator — the Workflow-B analogue of `deck_lint.py` — and fails an email on any of:

1. any of the lesson's diagnostic-slide questions missing verbatim from the body;
2. the praise quote not being a substring of that student's `student_text`;
3. subject not exactly `Your work on <Lesson> — what to rewrite`;
4. recipient not `s.first.last@redclay.k12.de.us` with hyphens stripped;
5. any rubric **score** or 🟥/🟨/🟩 color assigned by B (tier *labels* inside the questions are allowed — those are the prompt, not a score);
6. the rewrite instruction or the DRAFTS submission line missing.

On any failure: fix the email and re-lint. Do **not** create the draft until it passes. This is the fidelity gate that guarantees drafts match these directions.

## Step 5 â Create Gmail Drafts via Composio

**Use the Composio `GMAIL_CREATE_EMAIL_DRAFT` tool verified in pre-flight.** Required fields:

- `to`: student email from Dashboard roster (with hyphens stripped from last names)
- `subject`: `Your work on <Lesson Name> â what to rewrite`
- `body`: the composed email text from Step 4

**Do not send.** Drafts only. Katherine reviews and sends from her kvond12 Gmail.

**Forbidden:** any first-party Gmail MCP tool. Even if it appears in the available toolset. Even if Composio fails mid-run. If Composio stops working partway through, HALT and report which students got drafts and which did not.

### If Composio errors partway through
Don't fall back. Don't skip ahead. Halt and tell the user exactly which students were drafted, which were not, and ask whether to retry once Composio is restored.

### After draft creation: update the Dashboard
For each student whose draft was successfully created, update their row in the appropriate class sheet of the Teacher Dashboard:

| Column | Value |
|---|---|
| `Email Sent` | `Draft created` plus today's date (e.g., `Draft created 2026-05-21`). Don't write `Yes` â Katherine still has to actually hit send from Gmail. |
| `Last Updated` | Current timestamp |

Don't touch any other columns. NOTES columns belong to Workflow A; DRAFT columns belong to Workflow B1.

If a draft creation failed for a student (Composio error, malformed email, etc.), leave their `Email Sent` column blank and log them in the summary as "draft failed."

---

## Step 6 â Output Summary

After all drafts are created, write `workflow_b_summary.md` to the output directory:

```markdown
# Workflow B â Run Summary

**Lesson:** <lesson_name>
**Class:** <A_Day Biology | B_Day Biology | A_Day Forensics | B_Day Forensics>
**Email tool used:** Composio GMAIL_CREATE_EMAIL_DRAFT (kvond12@gmail.com)
**Students processed:** N
**Drafts created:** N
**Skipped (no roster):** [list]
**Draft creation failed:** [list, if any]
**Dashboard Email Sent column updated:** Yes/No

## Per-student notes

| Student | Tier mix (3-tier slides) | Originality flag | Skipped slides |
|---|---|---|---|
| smith_jane | M: 1, W: 1, G: 0 | none | 0 |
| ... | | | |
```

Then call `present_files` with the summary so Katherine sees a quick overview.

---

## Edge Cases

- **Student answered weakly or left slides blank** → no per-slide surgery. The question block is constant; set the **tier steer** to the "start at Getting Started, come find me" variant.
- **Student answered no diagnostic slides / fully blank deck** → still send the full slide/question block (that *is* the assignment). Replace praise with a warm "we missed your work this lesson — let's get your thinking down" line; steer = start at Getting Started + an in-person offer. No quote, no stretch framing.
- **Student reached Mastery on every diagnostic slide** → same block; steer points them at the Mastery questions and the What-If slide. No refinement directions — the Mastery prompts already are the stretch.
- **Lesson has fewer than 5 diagnostic slides** → use all available diagnostic slides; do not invent slides to pad. The lint's question check adapts to the actual diagnostic count from A's JSON.
- **Student's email in the Dashboard is malformed or missing** → skip that student, log in summary.
- **A's JSON contains a student not on the Dashboard roster** → skip in B's run, flag in summary.
- **Dashboard `Email Sent` update fails** → don't fail the run; drafts already exist in Gmail. Flag the write failure in the summary.
- **Composio Gmail tool disappears mid-run** → HALT. Do not switch tools. Report what was completed.

## Quality Floor

Every draft must pass `workflow_b_lint.py` (Step 4.5) before it is created. The checks:

- [ ] Pre-flight Composio check completed (mandatory)
- [ ] All diagnostic-slide questions reproduced **verbatim** from the template (no paraphrase, no dropped tier, no invented slide)
- [ ] Praise quote is a real substring of the student's own answer, student-generated, slide cited
- [ ] Tier steer (if present) points to real tiers on real diagnostic slides
- [ ] Rewrite instruction + DRAFTS submission line present
- [ ] No rubric scores or 🟥🟨🟩 assignments by B (tier labels inside the questions are fine — scoring is B2's job)
- [ ] Reading level ~7th grade for the praise and steer prose
- [ ] Subject exactly "Your work on <Lesson> — what to rewrite"
- [ ] Recipient uses `@redclay.k12.de.us` with hyphens stripped from the last name

## Reference Files

- `references/email_examples.md` â concrete examples of strong vs. weak praise paragraphs, rewrite directions, and challenge questions from real student responses
