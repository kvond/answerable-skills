# Aspect-Anchored Conceptual Grader — GRADING SPEC (the reasoning layer)

**Version 1.1 · 2026-05-31**

*v1.1 — added the four feedback cases (§8a–8d): authentic, copied/inauthentic, blank, and rotating encouragement, with SELF_CHECK verifying no closing repeats. v1.0 was the initial spec.*

This spec is the *thinking* half of the grader. The script (`aspect_extractor.py`) is deliberately dumb: it finds sections, pulls the critical aspect and the student's verbatim answers, flags blanks, and counts — nothing more. **Every judgment lives here**, applied by the reasoning layer (Sonnet), so the code never has to be rewritten when the grading philosophy is refined.

Model routing: the extractor's rote work can run on Haiku; this spec is applied on Sonnet. (In chat, stay on Sonnet — the model does not auto-switch.)

---

## 1. Core principle — the critical aspect is the spine

Grade each answer **only** on whether it shows conceptual sense of *its section's critical aspect* (the `aspect` field the extractor pulled from the slide header). Not completion. Not length. Not polish. Not grammar. A two-line answer that nails the aspect beats a paragraph that misses it.

---

## 2. Tiers (always color-coded — never plain black)

| Tier | Color | Swatch | What it looks like *relative to the section's aspect* |
|------|-------|--------|--------------------------------------------------------|
| **Mastery** | green `#1E8449` | 🟩 | States/explains the aspect correctly in the student's own terms, usually with a reason or example. |
| **Working On It** | amber `#D68910` | 🟨 | Touches the aspect but partial, vague, or correct alongside a misconception. |
| **Getting Started** | red `#C0392B` | 🟥 | Attempts the section but misses the aspect — off-target, restates the prompt, or a not-yet guess. |
| **Blank** | grey | ⬜ | No substantive answer (extractor flagged blank). |

Use the colored **bold** label + matching swatch everywhere this surfaces (student feedback, rubric summaries, dashboards).

---

## 3. Authenticity gate (before awarding any tier)

If an answer does not read in the student's **own voice** — textbook/AI phrasing out of step with their other answers (e.g. "phenotypic plasticity," flawless clauses among otherwise simple writing) — do **not** award Mastery on the strength of those words. Flag `authenticity: suspect`. Mastery and praise require the student's own thinking (ties to the praise rule and the copied-work lesson). When in doubt, judge the authentic-voiced answers and note the concern.

---

## 4. Judging a section

For each section, read `first` and `rewrite` against `aspect`. Assign a tier to the **best authentic answer available** (the rewrite if present and authentic, else the first attempt). Record the tier per `(slide, aspect)`. Ignore spelling/grammar for the tier — those are separate, informational feedback only.

---

## 5. Score (0–100; denominator always 100)

Per answered section, tier weight: **Mastery 1.0 · Working On It 0.6 · Getting Started 0.3 · Blank 0.0**.

```
score = round( (sum of section weights / number of sections) * 100 )
```

- The denominator is the **actual section count** for that lesson (it flexes; do not assume a fixed number).
- Compute two scores when both exist:
  - **NOTES Score** from the `first` answers.
  - **DRAFT Score** from the `rewrite` answers.
- **DRAFT is the authentic measure** (done under testing conditions). **NOTES is cheatable** → treat it as a baseline only.

---

## 6. Push deeper vs. remediate (gated on the DRAFT, not the Notes)

- DRAFT shows **Mastery** on an aspect → **push deeper**: a causal/"why" follow-up that extends the idea.
- DRAFT shows **Working On It / Getting Started / Blank** → **remediate**: re-teach that aspect with a targeted redraft prompt.
- Offer **up to 5 redrafts**, worst conceptual gaps first (Getting Started before Working On It; prioritize aspects central to the lesson). Never gate this on the Notes score.

---

## 7. Notes-high / Draft-low divergence

If the NOTES tier is higher than the DRAFT tier on an aspect, surface it to **both teacher and student as growth, not gotcha**: e.g. "You had this on your notes — the rewrite under test conditions is where to lock it in." This is the most useful signal the grader produces.

---

## 8. Student-facing feedback rules

Every graded submission falls into one of four feedback cases. Pick by what the extractor + authenticity gate found.

### 8a. Authentic work (has real, own-voice answers)
- **Name the aspect** the feedback is about.
- **Praise** must be evidence-specific: (1) a verbatim quote of the student's words that is a real substring of their answer, (2) student-generated content (not prompt text echoed back), (3) a specific, non-template explanation after the em-dash (no "you're on the right track" / "this is exactly right").
- For each gap (worst-first, ≤5): name the aspect + one targeted redraft prompt.
- **Grammar** feedback is separate, informational, and never affects the tier or score.

### 8b. Copied / inauthentic (turned something in, but `authenticity: suspect`)
Be direct — the student should feel the missed chance, not be scolded into a corner.
- Quote the most obviously-not-theirs line and name plainly that it doesn't read as their own thinking.
- State the consequence honestly: because it isn't in their voice, you **cannot see what they understand**, so you cannot give the credit or the praise that **could have been theirs**.
- No fake praise, no pretending the aspect was met. Close with a **rotating encouragement** line (§8d).
- Score: do not award Mastery on inauthentic content (per §3); tier the authentic remainder only.

### 8c. Blank / nothing submitted (extractor `blank_both` across the section, or whole submission empty)
Direct, but never cruel — no guilt-trip, no tallying of everything missing.
- State plainly there's nothing here to grade on this aspect/lesson.
- Frame it as a **missed chance you genuinely wanted**: you'd have liked to see what they could do, and you couldn't, because the work isn't here.
- Close with a **rotating encouragement** line (§8d).

### 8d. Rotating encouragement (for 8b and 8c — MUST vary per student)
Never reuse the same closing line across a class set; a class doc must not read like a form letter. Each closing is a single warm, forward-looking sentence about *their capability and the next chance to show it*. Generate fresh per student; do not draw from a fixed list. Spirit (not templates to copy):
- a belief-in-them note tied to next time,
- an invitation to put their own thinking on the page,
- a "your real answer is worth more than a perfect borrowed one" note,
- a "I know there's a thinker in there" note.
Keep each distinct in wording from the others in the same run; the SELF_CHECK (§10) verifies no two closings repeat.

---

## 9. Outputs the grader produces

1. **Per-student, per-lesson record** for the dashboards / growth files: tier per aspect, **NOTES Score /100**, **DRAFT Score /100**, divergence flags, authenticity flags.
2. **Student-facing feedback** delivered as the formatted `.docx` (one section per student, name + email header), per the standing email-output rule — sent via the Chrome extension.

---

## 10. SELF_CHECK gate (required, logged in chat)

For each scored student, before emitting:

> 🔍 **[SELF_CHECK]** Re-read tier definitions → applied to the actual extracted answers → every praise quote verified as a real substring of the student's answer → authenticity considered → correct feedback case (8a/8b/8c) chosen → for 8b/8c, closing encouragement is distinct from every other closing in this run → **PASS/FAIL**.

On FAIL, regenerate (up to 3×) and log the result. This makes the grading auditable.

---

### How it runs end to end
1. `aspect_extractor.py` parses each submission → `{sections:[{slide, aspect, first, rewrite}], counts}`.
2. The reasoning layer applies this spec to each section → tiers, scores, feedback, redraft list, divergence/authenticity flags.
3. Records post to the dashboards + Schoology import; feedback compiles into the per-class `.docx`.
