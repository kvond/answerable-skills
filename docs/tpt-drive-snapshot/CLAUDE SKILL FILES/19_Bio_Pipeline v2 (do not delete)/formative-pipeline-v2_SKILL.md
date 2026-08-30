---
name: formative-pipeline-v2
description: The v2 formative pipeline that replaces Workflow A→B1→B2→C. From one annotated deck per student, produce a printable Conceptual Growth Report (student) plus a class summary and agency coding (teacher); gradebook is completion-only and proficiency lives only in the report. Carries the student revision-coaching prompt (speaker notes), the teacher batch prompt, the integrity gate (first-answer copied→flag, AI→auto-fail), the Growth Report standards (deeply positive, 9th-grade readable, no coding vocabulary to students), the document build specs, and cross-unit rollups. Also maintains a running Master Completion Roster across cycles for marking-period grading. Applies to Biology, Anatomy & Physiology, and Forensics. Triggers: "formative pipeline", "v2 pipeline", "run the growth reports", "batch the decks", "growth report run", "completion roster", "grade roster", "how much did they complete", teacher batch over annotated decks.
---

# Formative Pipeline v2 — Answerable growth-report flow (SKILL)

**Status:** authored 2026-08-07. **Revised 2026-08-10** after a full end-to-end build and
review on fabricated Cycle 10 (Enzymes) data. **Revised 2026-08-11** to add the Master
Completion Roster step — a cross-cycle completion rollup that turns the per-cycle completion
CSV into a marking-period grade. Consolidated spec for the pipeline that
**replaces Workflow A→B1→B2→C**. Judgment layer lives here; `.py` stays dumb (deterministic
extraction only). Applies to **Biology, Anatomy & Physiology, and Forensics** (Forensics keeps
its case-first opener). Resolves the v2 PENDING INPUTS in the MANIFEST.

**One line:** from one annotated deck per student, produce one **printable Growth Report**
(student) and one **research/class output** (teacher) — grading is completion-only, and the
student's proficiency lives only in the report.

> **What changed on 2026-08-10.** Everything under *Growth Report standards*, *Document build
> specs*, *Reading the deck*, and *Known failure modes* is either new or corrected against a
> working build. The flow, the integrity gate, the two-rail split, and the completion-only
> gradebook are unchanged from the 2026-08-07 authoring.

> **What changed on 2026-08-11.** Added step 9a and the *Master Completion Roster* section.
> The completion CSV (step 9) answers "did this student finish this one cycle's task." It does
> not answer "how much of the marking period has this student completed," which is what a grade
> needs. The roster closes that gap by appending each cycle's completion column to a running
> sheet rather than requiring a second, separate data-entry pass at grading time.

---

# RUN CHECKLIST

**Run these in order. Everything after this section is reference — read it when a step sends
you there.**

[Deliberately *not* called "Task Agenda" — that name is taken by the Year Task Grid week view
at `/` on the feedback-system site, and the two are unrelated.]

## Before the first real cycle (once — all five are blocking)

- [x] **1. ~~Add `"then and now"` to `NON_DIAGNOSTIC_MARKERS`~~** in
      `engine/scripts/extract_and_grade.py` — **done 2026-08-10** (commit `753fbd7`, backup at
      `extract_and_grade.py.bak-2026-08-10`). Was marking every student Incomplete.
- [x] **2. ~~Deploy the v2 extraction layer~~** — **done 2026-08-10**, commit `d07c4dc`,
      `engine/scripts/extract_v2.py`. Detects response slides by **both answer labels on the
      teacher template**, not by `classify_slide()`, and emits the printed slide number.
- [x] **3. ~~Fix `Config!B2`~~** — **done 2026-08-10**. Now the LIVE Dashboard's own ID.
      Every Composio Sheets call must pass `account: "kvond12"`; three accounts are connected.
- [~] **4. Answer areas — built, awaiting approval.** The deployed deck has **no labeled
      answer areas at all**, only one unlabeled `Rectangle 15`. `build_v3_deck.py` adds two
      labeled areas (top 4.98in / 6.00in, 0.95in each, **`auto_size = MSO_AUTO_SIZE.NONE`** —
      the default collapses a new text box to its empty content) and compresses the tiers and
      word bank to pay for them. Output `C10_TEACHER_v3.pptx`.
- [~] **5. Reword slides 20, 21 and 25** — done in the same build, **awaiting Katherine's
      approval before either goes to Drive.**

## Every cycle (the batch run)

- [ ] **1. Read the live Dashboard.** Class membership comes from it, never from a filename or
      folder. Never rebuild it from scratch; never write to `All-page`.
- [ ] **2. Pull the deployed extractor from the scripts folder.** Never reconstruct it. If the
      download fails, retry; if it fails again, HALT and report.
- [ ] **3. Confirm the response slides and their printed numbers** for this deck. The printed
      number is not the deck position, and it differs per cycle. → *Reading the deck*
- [ ] **4. Extract** first answer + revised answer per response slide. No judgment in this step.
- [ ] **5. Run the integrity gate** on first answers only. → *Integrity gate*
- [ ] **6. Write the Growth Reports**, one per student, 3 pages. Flagged students route to
      `HELD_for_teacher_review/`. → *Growth Report standards*, *Document build specs*
- [ ] **7. Write the Class Summary**, 3 pages, `.docx`. → *Document build specs*
- [ ] **8. Write the agency coding** as `.xlsx` and append to `Coding Master`. Append-only;
      never write to `Before Class`. → *Document build specs*
- [ ] **9. Write the completion CSV** — whole roster including non-submitters. This is the only
      file that reaches Schoology. → *Gradebook*
- [ ] **9a. Append to the Master Completion Roster.** Add this cycle's column to the roster
      sheet — reuse the values just written to the completion CSV, never retype them — and
      recompute `% Complete`. → *Master Completion Roster*
- [ ] **10. Update the cross-unit accumulation layer** and regenerate both rollup charts.
- [ ] **11. Print and hand back** the Growth Reports. Students complete the last line and
      return page 1.

## Standing conditions

- **On-demand only.** This batch runs when Katherine runs it — never at session start, never
  proactively, never as a "helpful" scan.
- **Submission window:** 5 days after the first submission appears. Hold the rest in a pending
  list with the open date.
- **Scope:** NOTES and DRAFT submissions only. No lab reports, no activity sheets.

---

## The three outputs

1. **One artifact — the annotated deck.** Students answer on the slides. Each response slide
   has two stacked, labeled areas: **"Your first answer"** and **"Your revised answer."** The
   revision-coaching prompt lives in that slide's **speaker notes**.
2. **One summary — the Conceptual Growth Report.** Per student, printable, handed back.
3. **One research output.** Class summary (proficiency spread, misconceptions, next
   instructional contrast) + agency coding + the cross-unit rollups.

---

## Student flow (in class + one day later)

1. In class, the student writes the **first answer** on the response slide.
2. They open the slide's **speaker notes**, copy the **revision-coaching prompt** (below) into
   their own AI, and use the feedback to think again — the prompt is built so the AI will
   **not** write the answer for them.
3. **The next A/B class**, they write the **revised answer** in the second area on the same
   slide. Both answers stay visible — seeing their own thinking change is the point, and they
   are told this.
4. The deck is submitted (Chrome-extension Drive upload, as now). No separate doc, no email.

### Revision-coaching prompt — goes verbatim in each response slide's speaker notes

```
Copy everything between the lines into your AI, and paste your first answer where it says
[YOUR FIRST ANSWER]. The AI will NOT give you the answer — it will help you see your own
thinking so you can improve it yourself.
-----
I am a high school student. Below is a science question and my first answer. Do NOT rewrite my
answer and do NOT give me the answer. Instead:
1. Tell me one thing I got right, and quote my own words back to me.
2. Ask me two questions that make me look again at one idea I might have wrong or left out.
3. Name one distinction or example worth thinking about.
Keep it short and in plain language, then stop so I can write my own revised answer.

QUESTION: [the slide's question]
[YOUR FIRST ANSWER]:
-----
Now write your revised answer in "Your revised answer" on the slide — in your own words.
```

---

## Reading the deck — facts the batch depends on

**Use the deployed extractor from the scripts folder. Never reconstruct it, not even partially,
not even after a failed download.** Reconstruction silently drops bug fixes. If the download
fails, retry; if it fails again, HALT and report.

### Response slides vs. reflection slides

A deck carries two kinds of slide with a writing area, and only one kind is analysed:

- **Response slides** — the two-area slides (*Your first answer* / *Your revised answer*).
  These are the pipeline's input. Cycle 10 has two, at deck positions **9** and **17**.
  **A deck straight out of the VT build does not have these areas** — it carries one unlabeled
  rectangle. They are added by the v2 deck build (`build_v3_deck.py`), and `extract_v2.py`
  refuses to run without them. Check this first when a deck extracts nothing.
- **Standing reflection slides** — a single writing area for a recurring prompt that is not a
  content question. These route to `"other"` and are excluded from analysis while staying in the
  deck for students. They are caught by `NON_DIAGNOSTIC_MARKERS`, which
  `classify_slide` tests FIRST — before the tier-label test.

### The printed number is not the deck position [HARD]

Response slides carry a number **printed on the slide** that does not match their position in
the file. In Cycle 10, deck positions 9 and 17 print **7** and **13**.

- **Student-facing documents cite the printed number.** It is the only number the student can
  see; a report citing the deck position sends them to the wrong slide.
- **Teacher and research rails use the deck position**, including the `Slide` column of the
  agency coding.
- Read the printed number off the slide rather than assuming an offset — the offset is a
  consequence of that deck's section dividers and will differ per cycle.

---

## Teacher batch (over the folder of submitted decks)

Model routing: **Haiku** for deterministic extraction, **Sonnet** for report + coding judgment.
Class membership from the **Dashboard** (source of truth), never from filename/folder — look up
every student across class sheets before processing.

1. **Extract** — reuse the deployed deterministic extractor to pull, per response slide, the
   first answer and the revised answer. No new judgment here.
2. **Integrity gate (first answer only)** — see below. Sets each first answer to
   `clean | flag-copied | fail-ai`, visible to the teacher.
3. **Growth Report** — generate one per student from the two answers, under the report
   standards below. Deeply positive, plain, no coding vocabulary.
4. **Agency coding** — code the answers into `Coding Master` (research rail; technical
   vocabulary allowed here only). Codebook per `16-agency-scan-SKILL.md`, refined:
   presence codes **ENG / EPI / AUT + DEC + CAND**; two axes recorded beside the presence
   code and **never gating it** — capability/warrant (practical / interpretive / epistemic)
   and generativity (does the idea open a distinction, a shared misconception, or a testable
   case — by what it opens, not by correctness); provenance (student / AI / prompt / peer).
   Verbatim excerpt only; SELF_CHECK before writing; append-only.
5. **Class summary** — proficiency spread, recurring misconceptions, the next instructional
   contrast to teach.
6. **Completion CSV** — the only thing that reaches Schoology (below).
7. **Cross-unit rollups** — update the accumulation layer and regenerate the two rollups.

**Held output.** A student whose first answers are flagged gets a Growth Report like everyone
else, but it is written to `HELD_for_teacher_review/` rather than the handout folder. Katherine
releases or withholds it. Nothing auto-fails a student out of feedback without her seeing it.

---

## Integrity gate

- Runs on the **first answer only** — written in class, should be the student's own. The
  **revision is exempt**: students are told to run the coaching prompt through their AI, so
  "AI" in the revision is the design, not a violation.
- **Copied first answer → flag** for teacher review. **AI-authored first answer → auto-fail.**
- The copy check compares the first answer against **printed slide text**, never against writing
  fluency. This is what protects ESL and atypical writers: plainly worded, non-standard grammar
  is not evidence of anything and must not raise a flag.
- **Flags stay visible to the teacher.** Automated AI-detection misfires, so the teacher can see
  a flagged case and, if it is a false positive, restore that student's authentic feedback.
  Because the gradebook is completion-only, a wrong flag costs a cycle's feedback, not a grade.
- **Completion and integrity are separate rails [HARD].** A flagged student still reads
  *Complete* in the completion CSV. The flag governs whether the report is handed back, never
  whether the gradebook records the work as done.
- Rationale: authentic feedback requires authentic work — an AI-written first answer can only
  yield a hollow report, so failing it protects the feedback loop, not a score.

---

## Growth Report standards (student-facing) — every report, no exceptions

### Structure (first-person, plain headers)

- *Where my thinking started* — their initial idea, in plain terms.
- *How my thinking changed* — the distinction or correction between first and revised answer.
- *Evidence from my final answer* — a verbatim quote of their own words carrying the change,
  attributed to the **printed** slide number it was written on.
- *Current understanding* — proficiency bars with **plain labels** (Developing / Almost there /
  Proficient — [final wording still open; these are the working labels and they have not been
  ruled on]).
- *My next step* — see the rule below.
- *An idea worth chasing* (when present) — see the rule below.
- *What I understand now that I didn't before* — **left blank for the student to complete**,
  under the instruction *"Write this yourself, then hand this page back to me. This is the part
  I read."* This is the one place the report asks for something back; Katherine reads the
  returned line as formative assessment.

### "My next step" is forward-looking [HARD]

It must name a **transferable move the student carries into the next cycle**. It must **never**
ask them to go back and repair work they have already submitted — they will not, and a step they
will not take is dead text on the page.

- Good: *"Next time a question asks you to compare two setups, write what is the SAME at the end
  before you write what is different."*
- Wrong: *"Go back to the stomach enzyme slide and fill in your revised answer."*

A forward-framed step also works for a student whose deck was incomplete, which the backward
version cannot do.

### "An idea worth chasing" must land somewhere [HARD]

An idea with no concrete destination is not useful. Every instance names **both**:

1. the **printed slide number** the idea grew from, and
2. the **named activity** where the student can go do something with it.

Activity slides carry titles rather than printed numbers, so activities are referenced by name
(Cycle 10: the Activation-Energy Hill, Lock & Key Match, Temperature & pH Lab, and the Optional
Challenge Liver-Catalase Lab).

Example: *"This came from what you wrote on slide 13. Take it further in the Temperature & pH
Lab, where you run catalase across several temperatures and several pH levels and watch where it
stops working."*

[Open question worth deciding: the section currently appears only for students who produced a
generative idea, which means its presence is itself a proficiency signal students can read off
each other's pages. Either give every student one — there is almost always a chaseable thread,
including in a wrong idea — or accept the signal deliberately.]

### Rules

- **Deeply positive AND true.** Every affirming line anchored to something they actually did
  (verbatim quote or named move). Proficiency is a position on a path, never a deficit. No
  generic or unearned praise — teenagers read that as fake and it buries the next step.
- **The praise quote must be a substring of the student's own answer** and must be
  student-generated content, not echoed prompt text.
- **Understandable by them.** Written for a striving 9th-grader; plain, without dumbing down
  the science.
- **No coding vocabulary reaches the student.** No NGSS codes, no "epistemic," "warrant,"
  "agency," or proficiency jargon. That vocabulary lives ONLY on the research/teacher rail
  (two-rail split).
- **Print-friendly** — the teacher prints and hands it back.

---

## Document build specs

Arial throughout, teal `#028090` for headings, US Letter, 0.625in margins. Proficiency fills:
Proficient `#C9E7D2`, Almost there `#EFDF85`, Developing `#E8E8E8`.

### Growth Report — 3 pages, `.docx`

| Page | Contents |
|---|---|
| 1 | The report: the seven sections above, ending with the blank writing lines |
| 2 | **Rubric key — "What Good Thinking Looks Like"** [HARD: rubric key is page 2 of every student summary doc] |
| 3 | **Cross-unit growth chart** — this student's arc across cycles |

The chart takes page 3 because page 2 is spoken for by the standing rubric-key rule.

### Class Summary — 3 pages, `.docx` (not markdown)

| Page | Contents |
|---|---|
| 1 | Participation · proficiency spread · recurring misconceptions · next instructional contrast · integrity |
| 2 | **Every student on the roster**, including those with no deck in: completion, the four proficiency bars, integrity state |
| 3 | **Course trend chart** — class mean with a band from lowest to highest student |

Page 2 exists so Katherine can see the whole class on one sheet rather than reconciling the
handouts against the roster. Column headers must be short enough not to break mid-word.

### Agency coding — `.xlsx`, not `.csv` [HARD]

Column width is a property of the file, and the verbatim-excerpt column is the one that has to
be readable. A CSV cannot carry this.

| Col | Header | Width | Notes |
|---|---|---|---|
| A | Cycle | 8 | |
| B | Lesson | 20 | |
| C | Student | 26 | |
| D | Slide | 7 | **deck position** — teacher/research rail |
| E | Presence code | 15 | |
| F | Capability/warrant | 18 | |
| G | Generativity | 42 | wrapped |
| H | Provenance | 12 | |
| I | **Verbatim excerpt** | **95** | **wrapped** |

Header row frozen, autofilter on, Arial 10, row height 30.

### Cross-unit growth chart spec

Built for print and grayscale, because these are handed back on paper.

- Form: line over cycles. Ordinal y-axis with the three proficiency labels, **not** a number
  line — the levels are positions, not quantities.
- **Student chart:** one teal series, no legend (the document heading names it), final point
  direct-labeled.
- **Class chart:** class mean as the single teal line plus a light-gray min–max band, annotated
  inline. Still legend-free.
- Render charts **without an internal title** — the document supplies the heading, and a titled
  PNG duplicates it.
- Where a rollup is exercised with fabricated history, **say so on the chart page in red.**

---

## Cross-unit rollups

An accumulation layer keyed by **student × cycle** (fed by the per-cycle reports + the
append-only `Coding Master`, re-collecting nothing) produces:

- **Student year-arc** — "how your thinking has grown across the year," under the same
  positive + readable rules; a longitudinal companion to the per-cycle report. Ships as page 3
  of the Growth Report.
- **Course-level trend** (teacher) — recurring misconceptions, and agency + capability moving
  across the 20 cycles / four marking periods. Ships as page 3 of the Class Summary.

---

## Gradebook = completion only [HARD]

- Schoology records **completion**: both answer areas filled = done. Never quality.
- Completion CSV reuses the repurposed Workflow A completion logic; header `DRAFT.<Lesson>`
  (or `Notes.<Lesson>` per the existing gradebook column), one row per student, **whole roster
  including non-submitters**.
- All proficiency/growth lives in the Growth Report, never the gradebook.

---

## Master Completion Roster [NEW — 2026-08-11]

**Purpose.** The completion CSV above answers "did this student finish this one cycle's task."
It does not answer "how much of the marking period has this student completed," which is what a
grade actually needs. This section is the cross-cycle rollup that closes that gap, run as
step 9a of every cycle batch — never a separate manual pass at grading time.

- **One Google Sheet, deliberately separate from the Dashboard.** This pipeline is structurally
  blocked from reading or writing the Dashboard (see the Dashboard exclusion elsewhere in this
  graph), so the roster is its own file, not a new Dashboard tab.
- **One tab per class** — Biology A Day, Biology B Day, Forensics B Day. *[Assumption — confirm
  this matches your actual class list; add or rename tabs if not.]*
- **Wide format, one column per cycle.** Rows = students, whole roster, non-submitters included
  — same population as the completion CSV. Columns = `DRAFT.Cycle01`, `DRAFT.Cycle02`, ...,
  one added per cycle run.
- **Populated by appending, never retyping.** Step 9a takes the exact values just written to
  that cycle's completion CSV and adds them as the next column. The roster is a running log of
  CSVs, not a second data-entry pass — if a CSV was wrong, fix the CSV and re-append; never
  hand-edit the roster directly.
- **Rollup columns, computed by formula:**
  - `# Assigned to date` — count of cycle columns filled in so far this marking period
  - `# Complete` — count of "complete" cells for that student across those columns
  - `% Complete` — `# Complete ÷ # Assigned to date`
  - `Grade` — a lookup against your school's percentage-to-grade cutoffs. *[Open input — supply
    the cutoffs once and this becomes a fixed formula, not a recurring manual step.]*
- **Marking-period boundary.** *[Open decision — does the roster reset to zero columns at the
  start of each new marking period, or run continuously across all four with a filter/view per
  period? Either is a formula choice, not a redesign — say which when you're ready and it gets
  fixed once.]*
- **Same completion-only boundary as the gradebook [HARD].** The roster carries completion
  counts only — never proficiency, Growth Report content, or agency coding. Those stay on the
  research rail per the two-rail split. A student's `% Complete` here and their proficiency in
  their Growth Report are two different numbers answering two different questions; this roster
  only ever answers the completion one.

---

## Known failure modes

- **A standing reflection slide is scored as a concept question.** Symptom: every student
  reads Incomplete. Cause: `classify_slide` returns `critical_aspect_concept_question` for any
  slide containing all three tier labels, and the Then-and-Now self-rating slide **reprints all
  three** ("Before this lesson: Getting Started / Working On It / Mastery"). Fix: add a
  distinguishing phrase to `NON_DIAGNOSTIC_MARKERS`, which is tested before the tier check.
  Fixed 2026-08-10 by adding `"then and now"`. [A more durable marker would be `"rate yourself"`,
  which is the construct rather than the title and would survive a retitled slide — not added,
  because it widens the net and that is your call.]
- **Citing the deck position to a student.** Sends them to the wrong slide. See the printed-number
  rule above.
- **Adjacent paragraphs carrying identical borders merge into one rule** in Word and
  LibreOffice. The student writing lines need an unbordered spacer paragraph between them.
- **Narrow `.docx` table columns break header words mid-word** ("denaturin g"). Widen to the
  full text width and shorten headers rather than letting them wrap.
- **A chart PNG carrying its own title duplicates the document heading.** Render titleless.
- **Rebuilding the Dashboard from scratch overwrites manual edits.** Read the live Dashboard
  before any rebuild. `All-page` is formula-driven — never write to it directly; write only to
  individual class sheets.

---

## Invariants that must not drift

- **Two-rail split** — technical/coding vocabulary never appears in a student report; only on
  the research rail.
- **Presence, not quality, for the agency codes** — the capability and generativity axes sit
  beside the presence code and never gate it (a wrong-but-original move still codes as
  origination).
- **Integrity on the first answer only; revision exempt; flags visible; completion unaffected.**
- **Append-only `Coding Master`; never write to `Before Class`** (formula view).
- **Pseudonymize at transcript/rollup export** for anything feeding the book.
- **Completion-only gradebook**; proficiency never posts to Schoology.
- **Master Completion Roster appends only** — a cycle's column, once written, is never retyped
  or reshaped; corrections happen by fixing that cycle's source completion CSV and
  re-appending, not by hand-editing the roster.
- **On-demand only** — batch runs when Katherine runs it, never at session start, never
  proactively.
- **Deployed scripts only** — never reconstruct a `.py` from memory.
- **Student-facing cites printed slide numbers; teacher/research rails cite deck positions.**

---

## Staging (do not skip)

Build and validate this flow on **one real cycle** before retiring the old scripts. Until then,
`01/08/11/15`, `PIPELINE_CHECKLIST`, and `KICKOFF_SCAN` keep a "superseded by v2" pointer but
are not deleted, so there is no mid-year gap in grade-posting.

**Blocking before this can touch real work:**

1. Add `"then and now"` to `STANDING_REFLECTION_MARKERS` in the deployed `extract_and_grade.py`.
2. Deploy the v2 extraction layer — the deployed extractor cannot yet tell a first answer from
   a revised one.
3. Fix `Config!B2` in the LIVE Dashboard (still points at a superseded file).
4. Settle the answer-area layout — 1.03in on the response slide is the real constraint.
5. Reword slides 20, 21 and 25 of the Cycle 10 deck, which still carry the retired
   "read the feedback / Schoology DRAFT / check your email" language.
6. **New:** create the Master Completion Roster sheet itself (one tab per class, headers only)
   before the first cycle that runs step 9a — the step assumes the sheet already exists.
