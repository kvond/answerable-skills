---
name: workflow-b2-rubric-summary
description: Score each student's lesson rewrite on three rubrics (Conceptual Accuracy & Vocabulary, Depth of Explanation, Scientific Writing Quality), compare to their original work to show improvement, and produce a per-student summary (Gmail draft) plus a whole-class report. Use this skill whenever Workflows A and B1 have both finished for a lesson and the teacher asks to "run Workflow B2," "score the rubrics," "summarize improvement," or "do B2 on this lesson." B2 reads A's per-student JSON (original answers) and B1's per-student JSON (rewrite text) to compare. Output also feeds into Workflow C's longitudinal growth tracking.
---

# Workflow B2 — Per-Assignment Rubric Summary

The rubric-scoring stage. Where the system actually judges student work on the dimensions that matter for growth: conceptual accuracy, depth of reasoning, and writing quality.

For each student, B2 reads the original answers (from A) and the rewrite (from B1), scores both versions on three rubrics, identifies improvement, and produces a student-facing summary plus a whole-class report. The class report shows the rubric distribution so Dr. von Duyke can see what the class is and isn't getting yet.

---

## ⚠️ Pre-flight (MANDATORY — do this FIRST, before any other step)

B2 creates per-student Gmail drafts in Step 4. The same hard rule as Workflow B applies:

1. Call `tool_search` with query `"composio gmail draft email"`
2. Confirm a Composio Gmail draft tool (`GMAIL_CREATE_EMAIL_DRAFT` or equivalent Composio-prefixed name) is returned and loaded
3. **If found:** proceed to Step 1
4. **If NOT found:** HALT IMMEDIATELY. Output verbatim:

   > Composio Gmail tool not loaded — Workflow B2 cannot create rubric summary drafts. The first-party Gmail MCP connector is authenticated to the school account and is **forbidden** for student emails. Please verify Composio is connected and enabled in **Settings → Connectors**, then re-run this prompt.

5. **Never** fall back to the first-party Gmail connector. **Never** "do the scoring and skip the emails" silently — if you can't draft, halt and ask the user what to do.

If the user explicitly says "score the rubrics but skip the email step," then the pre-flight can be skipped and B2 runs in scoring-only mode (Steps 1–3, 5, 6, 7 — skipping Step 4).

---

## When to Use

- Workflows **A and B1 have both run** for a given lesson (B2 needs both inputs)
- Teacher says "run Workflow B2," "score the rubrics," "summarize improvement," or "do B2 on this lesson"
- Teacher uploads or references a lesson folder with both A's and B1's outputs

**Do not run B2 if either A or B1 is missing.** B2 compares original to rewrite; without both, the comparison is impossible.

---

## Step 1 — Identify Inputs

Four inputs needed:

1. **A's output folder** — contains `answers/<student>.json` files. These hold the *original* annotated-slide answers per diagnostic slide.
2. **B1's output folder** — contains `rewrites/<student>.json` files (B1's canonical extraction format). These hold the *rewrite* text per diagnostic slide.
3. **Lesson + class context** — e.g., "Evidence of Evolution / B_Day Biology". Used to read the right Dashboard sheet for the roster, and to know where to write outputs.
4. **Teacher signature** — Katherine's preferred sign-off. Default: `— Dr. von Duyke`.

### Roster source: the Teacher Dashboard
Read the appropriate class sheet (`A_Day Biology` / `B_Day Biology` / `A_Day Forensics` / `B_Day Forensics`) for student emails and to confirm which students should have rubric summaries generated. Dashboard file ID comes from Config; do not hardcode it.

### If a student has A's JSON but no B1 JSON
They submitted Notes but no Draft. **Skip them** — there's no rewrite to score. Log in summary: "student_id: original submitted, no rewrite yet."

### If a student has B1 JSON but no A JSON
Unusual. Could mean their Notes file was renamed or missed by A. Flag in summary: "student_id: rewrite submitted, original not found in A's output."

### If both are present
Process the student.

---

## Step 2 — Read Each Student's Data

For each student where both inputs exist:

- From A's JSON: pull `slides` filtered to `is_diagnostic: true`. Capture `student_text` per slide — this is the *original answer*.
- From B1's JSON: pull the rewrite text per slide. Schema is keyed by `slide_number`.
- Pair them: for each diagnostic slide, you now have `original_answer` and `rewrite_answer`.

If a student rewrote some slides but not others, that's fine — score what's there, note what's missing.

---

## Step 3 — Score Each Rubric on Both Versions

Three rubrics, each scored on a 🟥🟨🟩 scale. Score the **rewrite** as the primary judgment; score the **original** as a baseline for measuring improvement.

Read `references/rubric_scoring.md` for full criteria, indicators, and calibration examples.

### Quick reference

| Rubric | What it measures |
|---|---|
| **Conceptual Accuracy & Vocabulary** | Right biological concept, accurate use of lesson-specific terms |
| **Depth of Explanation** | Causal reasoning — the "because", not just "the what" |
| **Scientific Writing Quality** | Complete sentences, precise language, no vague pronouns |

### Scoring philosophy
- Score the **rewrite** (final product) — that's the per-assignment grade
- Compare to the **original** to identify improvement (or regression)
- A student can be 🟩 on one rubric and 🟥 on another — score each independently
- Don't average. Each rubric tells a different story.

### Composite score
After the three individual scores, derive a composite:
- 🟩 composite = 2 or more rubrics at 🟩 AND no rubric at 🟥
- 🟨 composite = otherwise, as long as no two rubrics are 🟥
- 🟥 composite = two or more rubrics at 🟥

The composite is worth recording but the three individual scores carry the diagnostic weight.

### Improvement signal
For each rubric, compare original → rewrite:
- ⬆ improved (e.g., 🟥 → 🟨)
- → held (same color)
- ⬇ regressed (e.g., 🟨 → 🟥) — rare but worth flagging

---

## Step 4 — Generate Per-Student Summary (Gmail Drafts via Composio)

For each student, draft a brief, encouraging Gmail summary **using the Composio `GMAIL_CREATE_EMAIL_DRAFT` tool verified in pre-flight**. Different tone and content from Workflow B's rewrite-direction emails — B2 is about reflection, not action.

**Forbidden:** any first-party Gmail MCP tool. Same rule as Workflow B — Composio (kvond12) or nothing.

### If Composio errors partway through
Don't fall back. Don't skip ahead. Halt and tell the user exactly which students were drafted, which were not, and ask whether to retry once Composio is restored.

### Email structure

```
Subject: Your <Lesson Name> rubric summary

Hi <first_name>,

You finished the rewrite on <Lesson Name>. Here's how it scored:

🟥 / 🟨 / 🟩  Conceptual Accuracy & Vocabulary    <improvement signal>
🟥 / 🟨 / 🟩  Depth of Explanation                <improvement signal>
🟥 / 🟨 / 🟩  Scientific Writing Quality          <improvement signal>

<2–3 sentences naming specifically what got better between original and rewrite, citing a slide if useful.>

<1–2 sentences on the next stretch — what to keep working on, what mastery would look like.>

<Composite line, casual: "Overall this is solid Working On It territory" or similar — match the actual composite.>

<teacher signature>
```

### Tone guidance
- Warm, specific, future-oriented
- **Quote one specific moment from their rewrite** that showed growth or strength
- Name *what* moved them up a tier when something did — not just that it did
- For students who held at 🟥 or 🟨, frame as "here's the next stretch" — not "you didn't improve"
- For students who regressed on a rubric, mention it gently and ask what happened — don't accuse

### Anti-patterns
- ❌ Don't list the rewrite directions again — that was B's email
- ❌ Don't grade. No percentages, no letter grades
- ❌ Don't compare students to each other in this email
- ❌ Don't write more than ~150 words. This is a summary, not an essay.

---

## Step 5 — Generate Whole-Class Report

A single Google Doc placed in the lesson's `04_Workflow_B2_Summary/` folder showing class-wide rubric distribution.

### Class report structure

```
# <Lesson Name> — Class Rubric Summary
**Class:** <A_Day Biology | etc.>
**Date:** <ISO date>
**Students included:** N (out of M on roster)

## Distribution by rubric

| Rubric | 🟩 Mastery | 🟨 Working On It | 🟥 Starting |
|---|---|---|---|
| Conceptual Accuracy & Vocabulary | N (X%) | N (X%) | N (X%) |
| Depth of Explanation | N (X%) | N (X%) | N (X%) |
| Scientific Writing Quality | N (X%) | N (X%) | N (X%) |

## Improvement from original → rewrite

| Rubric | ⬆ Improved | → Held | ⬇ Regressed |
|---|---|---|---|
| ... | ... | ... | ... |

## Per-student table (sortable)

| Student | Conceptual | Depth | Writing | Composite | Improvement signal |
|---|---|---|---|---|---|

## What the class is and isn't getting yet

<2–4 paragraphs. Pattern observations: which rubric is the class strongest on? Weakest? Are particular critical aspects driving low scores? Any students whose pattern is unusual (e.g., 🟩 on writing but 🟥 on depth — they can write but they're not reasoning yet)?>

## Suggested next moves

<1–3 short suggestions for what to address in the next lesson or in re-teaching — grounded in the rubric distribution.>
```

### Tone for the class report
- Teacher-facing, direct
- Identify patterns, not just numbers
- Flag specific students worth following up with (e.g., "3 students regressed on Depth — worth checking in")
- Honest about what the rewrite cycle is and isn't moving

---

## Step 6 — Write to Tracking Surfaces

### Update the Teacher Dashboard
For each student processed, add rubric scores to a **new column block** on their row. Suggested columns (will be added if not present):

| Column | Value |
|---|---|
| `Rubric_Conceptual_<lesson>` | 🟥 / 🟨 / 🟩 |
| `Rubric_Depth_<lesson>` | 🟥 / 🟨 / 🟩 |
| `Rubric_Writing_<lesson>` | 🟥 / 🟨 / 🟩 |
| `Rubric_Composite_<lesson>` | 🟥 / 🟨 / 🟩 |
| `Last Updated` | timestamp |

Don't touch NOTES, DRAFT, or Email Sent columns (those belong to A, B1, B respectively).

### Create the rubric data file (for Workflow C to consume)
Write `rubric_data.<lesson_slug>.<student_id>.json` to the `04_Workflow_B2_Summary/` folder. Schema:

```json
{
  "student_id": "smith_jane",
  "student_name": "Jane Smith",
  "class": "B_Day Biology",
  "lesson_slug": "evidence_of_evolution",
  "lesson_name": "Evidence of Evolution",
  "lesson_date": "2026-05-21",
  "b2_run_timestamp": "2026-05-21T14:00:00Z",
  "rubrics": {
    "conceptual": "yellow",
    "depth": "green",
    "writing": "yellow"
  },
  "composite": "yellow",
  "original_rubrics": {
    "conceptual": "red",
    "depth": "yellow",
    "writing": "red"
  },
  "improvement": {
    "conceptual": "up",
    "depth": "up",
    "writing": "up"
  }
}
```

**This file is Workflow C's primary input.** Schema must stay stable; if it changes, C needs to update with it.

---

## Step 7 — Output Summary & Present Files

Write `workflow_b2_summary.md` to the output directory describing the run, then `present_files` showing the class report first.

```
# Workflow B2 — Run Summary

**Lesson:** <lesson_name>
**Class:** <class>
**Email tool used:** Composio GMAIL_CREATE_EMAIL_DRAFT (kvond12@gmail.com)
**Students processed:** N
**Skipped (no rewrite):** [list]
**Drafts created:** N
**Class report:** <link>
**Dashboard updated:** Yes/No
**Rubric data files for Workflow C:** <list of filenames>

## Pattern callouts
<1-3 things worth Katherine noticing — biggest improvements, surprising regressions, etc.>
```

---

## Edge Cases

- **Student rewrote only some slides** — score the rubrics on what they wrote. Note in their summary email that some slides weren't rewritten yet.
- **Student's original was 🟥🟥🟥 and rewrite is 🟩🟩🟩** — huge improvement. Celebrate specifically in their email, naming what moved.
- **Student's original was already 🟩🟩🟩 and rewrite is the same** — frame as "you held mastery; here's the next stretch beyond this lesson." Don't ask them to improve from already-mastery.
- **Student regressed on a rubric** — flag in their email gently. In the class report, note "N regressed on rubric X" as a pattern to investigate (could be the lesson framing, not the students).
- **Vocabulary anomaly or originality flag from B's email** — if B previously flagged this student, B2 should be aware. Consider whether the rewrite "improvement" might actually be increased copying. Quietly mention in Katherine's class report, never in the student email.
- **All three rubrics at 🟥 on the rewrite** — student didn't engage. Generate a shorter, warmer email asking them to come talk. No improvement framing, no detailed feedback — just an invitation.
- **Class size is very small (under 5)** — class report still runs but skip percentages (use just counts). Distribution percentages are noise at small N.
- **Lesson has no rewrites submitted at all** — B2 doesn't run. Tell Katherine and stop.
- **Dashboard rubric columns don't exist yet** — add them. The Dashboard accumulates columns over time as more lessons are scored.
- **Composio Gmail tool disappears mid-run** — HALT. Do not switch tools. Report what was completed.

---

## Quality Floor

Every per-student email should pass these checks:

- [ ] Pre-flight Composio check completed (mandatory)
- [ ] All three rubrics scored explicitly (not "you did well overall")
- [ ] Email quotes at least one specific moment from the rewrite
- [ ] Improvement (or held / regressed) is named, not implied
- [ ] No grades, no percentages
- [ ] No comparison to other students
- [ ] Under ~150 words
- [ ] Tone is warm and future-oriented

If any check fails, revise before drafting.

---

## Reference Files

- `references/rubric_scoring.md` — detailed scoring criteria for each rubric, with calibration examples (🟥/🟨/🟩 indicators per rubric, strong and weak examples)
