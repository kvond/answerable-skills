# Kickoff Prompt — Scan for New Student Work
## Step 0 — Consistency gate (run FIRST)

Run `pipeline_lint.py` (scripts folder) against `pipeline_invariants.json`. It is the rules analogue of deck_lint / workflow_b_lint: a deterministic check that every rule surface (onboarding doc, grading-rules reference, deployed SKILL.md files) still matches the MANIFEST invariants — flagging retired phrasings, dead dashboard IDs, and missing required rules. Resolve any FAIL before proceeding.

Open a **new chat in the Feedback project** (so Sonnet has the full system spec and all workflow skills in its context). Paste one of these prompts.

---

## The short version (paste this most of the time)

> Scan for new student work across all four classes and tell me what's pending.

That's it. If your project knowledge is current (master spec + all workflow SKILLs uploaded), Sonnet has everything it needs to know what "scan" means.

---

## The explicit version (paste this if the short version misbehaves, or if you've just updated the spec)

> Scan for new student work across all four classes (A_Day Biology, B_Day Biology, A_Day Forensics, B_Day Forensics).
>
> For each lesson in the Teacher Dashboard Config sheet (Dashboard file ID `1FMWx8ueSgcJVAXc5IzuR9F1Wb5JG92LM-Bj7rMiZAwE`):
>
> 1. Look in the lesson's `01_Input_Student_Work` folder (or the Schoology assignment folder if there's no separate input folder).
> 2. **Filter:** only count files whose names start with `Notes` or `Draft`. Ignore everything else.
> 3. Cross-reference against the appropriate class sheet in the Dashboard. A file is "new" (needs processing) if:
>    - **Notes**-prefixed file → the student's `NOTES Score` for this lesson is blank
>    - **Draft**-prefixed file → the student's `DRAFT Score` for this lesson is blank
>
> Report what you found as a table, grouped by lesson and class:
>
> | Lesson | Class | New Notes (run Workflow A) | New Drafts (run Workflow B1) |
> |---|---|---|---|
>
> Then ask me which lesson and which workflow to run next. **Do not process anything without my confirmation.**

---

## Variants for specific tasks

### Just process a specific lesson (skip the scan)
> Run Workflow A on the [Evidence of Evolution] B_Day Output lesson folder.

### Just check one class
> Scan for new Notes-prefixed and Draft-prefixed student work in A_Day Biology only.

### Process everything pending without asking
> Run Workflow A on every lesson where there are unprocessed Notes-prefixed files. Update the Dashboard and Schoology Master after each. Show me the summary when done.
>
> ⚠️ Don't use this one unless you trust the current state of the Dashboard — it commits all writes without review.

---

## What Sonnet needs to do this

- Read access to the Teacher Dashboard (file ID `1FMWx8ueSgcJVAXc5IzuR9F1Wb5JG92LM-Bj7rMiZAwE`)
- Read access to all the lesson folders listed in the Dashboard Config
- Project knowledge containing the master spec + Workflow A SKILL.md + Workflow B SKILL.md (when built: also B1, B2, B3)

If Sonnet says it can't access something, the most likely culprit is the Dashboard Config not having the folder ID, or the folder not being shared with the active Drive connector.

---

## When to use this

- **Daily** — paste the short version each morning to see what came in overnight
- **Mid-week check** — see who's behind on rewrites (lots of Notes processed, no matching Drafts yet)
- **End of unit** — final pass before grading to make sure nothing was missed

---

*If Sonnet can't do something cleanly because a workflow isn't built yet (B1, B2, B3), it'll tell you. That's expected — the kickoff prompt is forward-compatible with the full system once everything is built.*
