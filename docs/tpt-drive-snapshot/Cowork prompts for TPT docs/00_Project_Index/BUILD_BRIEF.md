# ANSWERABLE BIOLOGY — BUILD BRIEF (read this before doing anything)

You are one agent in a team building the complete teacher-facing documentation system for **Answerable Biology**, a full-year NGSS high-school biology curriculum by Dr. Katherine von Duyke, sold on TeachersPayTeachers (TPT). This is a production build. Never stop to ask questions; make the best-supported decision from source material, mark assumptions inline, and continue.

## The system in one paragraph
Answerable Biology organizes a year of biology into **20 flexible instructional cycles** (not a day-by-day pacing guide). Every cycle runs each core idea through one **Variation Theory (VT) arc**: students commit to a **first answer**, the lesson develops the idea through deliberate **contrasts** and a **pattern-break** (a case that breaks the too-simple rule), then students **revise**. The finished student deck — first answer beside revised answer — is the single artifact that runs through one AI feedback step (the revision prompt lives in the response slide's speaker Notes) to produce a one-page **Conceptual Growth Report** per student and a **class summary** for the teacher. Grading distinguishes **completion** (participation in thinking) from **proficiency** (demonstrated understanding). AI is **human-gated**: teachers retain responsibility for instructional decisions and proficiency judgments.

## Deck anatomy (every "VT deck, v2")
- Slide 1: TEACHER REFERENCE (not projected) — cycle number, unit, blocks, dates, ESSENTIAL CLAIM, NGSS Performance Expectations, objectives.
- Day-divider slides: "Day 1 of 3 — the most teaching", etc. The 3-block rhythm: Day 1 longer conceptual lesson + shorter activity; Day 2 shorter lesson + longer activity/lab; Day 3 finish activity + return to prior answers + feedback + revision.
- Bellringer slides; KEY TERMS boxes; short sims.
- "Critical aspect:" slides — contrasts (CASE A / CASE B), rule-building ("finish this sentence as a rule"), pattern-break slides, "Keep going" stretch questions.
- Three-tier concept questions: **Getting Started / Working On It / Mastery** with a word bank ("use any, modify any, or use none").
- "Your answer —" response slides: first answer + revised answer side by side; the AI REVISION PROMPT is in that slide's Notes (the AI must NOT give the answer; 1 thing right quoted back, 2 questions, 1 distinction).

## Source corpus (already extracted; do NOT re-extract)
- `/root/ab_build/extracted/*.txt` — full text+notes+links of all 27 decks. Filename = deck name.
- `/root/ab_build/extracted/_all_links.json` — every external link per deck.
- `/root/ab_build/sources/Answerable_Biology_Unit_Descriptions.md` — Katherine's own paste-ready TPT descriptions of all 19 units, incl. critical aspects and included materials. Authoritative for unit framing.
- `/root/ab_build/sources/Answerable Teaching-Chapter 5 — Intellectual Mentorship.md` — book chapter: her pedagogy (answerability, intellectual mentorship).
- `/root/ab_build/sources/Answerable Teaching-Chapter 6 — Doable, Not the Doer - AI.md` — book chapter: her AI philosophy and workflows.
- Original decks (for reference only): `/root/ab_build/sources/incoming/*.pptx`.

## Unit/cycle facts
19 units across 20 cycles. Decks present: Classifying Organisms (45 slides — check its teacher slide for cycle placement; likely Cycle 1), Cycles 02–20. Several units offer a CORE deck plus EXTEND deck(s) chosen by pace: Cycle 07 (Population Ecology core; Populations & Succession extend), Cycle 08 (Cells & Organelles intro core; Cell Organelles extend), Cycle 12 (meiosis), Cycle 13 (Mendelian core; Punnett extend), Cycle 15 (Genes & Chromosomes; Protein Synthesis), Cycle 16 (four decks: Genetic Mutations; Gene Expression; Genetic Disorders; Stem Cells). Trust each deck's own slide-1 teacher reference over the filename when they conflict — and log the conflict.

## Ecology = the free demonstration unit
Cycles 1–7 (Classifying Organisms through Population Ecology) form the ecology arc. The free TPT product is the Ecosystems & Feeding Relationships unit (Cycle 2) plus the Year Arc; the Ecology documentation must be genuinely teachable, not a sampler.

## Design rules (apply everywhere)
1. Curriculum is organized around questions and critical aspects students must discern. 2. Students repeatedly stop and formulate developing understanding in their own words. 3. Explanation, examples, contrasts, demonstrations, simulations, activities, labs each have different instructional jobs. 4. Matching/card activities establish a shared floor (vocabulary, classifications, structures); they are completion work, not proof of deep proficiency. 5. Open activities let students manipulate, compare, explore, model, change variables, notice critical relationships. 6. Labs must not be procedurally complicated when directions distract from critical aspects. 7. Some activities deliberately allow productive "messing around." 8. **Fiddles** provide meaningful exploratory work during attendance, transitions, waiting, early-finisher time — and an alternative to phones and off-task Chromebook use. 9. Faster students get relevant extensions so slower students get time without dragging the class. 10. Lessons need breathing room: attendance, late arrivals, passes, office calls, behavior, tech problems, drills, assemblies, individual help. Designed for actual classrooms. 11. Formative completion ≠ demonstrated proficiency. 12. Students need safety to expose incomplete thinking; grading every developing answer for correctness discourages intellectual risk. 13. Copying loses payoff when students must formulate, explain, apply, distinguish, receive targeted feedback, and revise. 14. AI makes frequent targeted formative feedback possible at realistic teacher workload; AI is human-gated. 15. Classroom technology extends teacher noticing, not merely polices behavior. 16. Master Agenda and Unit Agendas are operating documents — simple, readable during class. Standards/theory/administrative justification live in separate documents. 17. Cycles carry CORE, EXTEND, and EXPLORE/CHALLENGE options; teachers may move faster or slower. 18. Complexity belongs in the design, not in directions teachers must decipher.

## Drafting rules (teacher-facing docs)
Write directly; ordinary language over jargon; no padding; don't repeatedly re-justify choices; use Katherine's own reasoning and wording from the sources when it is strong — do not replace it with generic educational prose; use real Ecology examples wherever possible; flexible cycles, never rigid pacing; make the teacher's next action obvious; link outward rather than duplicating explanations. Agendas: never minute-by-minute scripts, no NGSS strings, no research citations, no admin-template formatting. Plain markdown, minimal bold, no emoji.

## Flags (use these exact labels inline; never block on them)
`REVIEW WITH KATHERINE` · `SOURCE NOT YET LOCATED` · `RIGHTS REVIEW NEEDED` · `WORKFLOW DEMONSTRATION NEEDED` · `LINK NEEDED` · `EXAMPLE NEEDED` · `GAP — NOT IN SOURCE NOTES`

## Known source gaps (already flagged; don't hunt for these)
- `VT_Decks_Illustrated.zip` is an un-downloaded iCloud placeholder — SOURCE NOT YET LOCATED.
- No dedicated Cycle 01 deck file was found beyond Classifying Organisms; verify from its teacher slide.
- Teaching notes on classroom jobs, first week, seating, GoGuardian, Schoology workflow may be thin in this corpus — extract what exists (deck notes, chapters), mark the rest GAP rather than inventing.

## Output
Write finished documents into `/root/ab_build/output/<numbered folder>/` as markdown (spreadsheets as xlsx+csv). Filenames: `SCREAMING_SNAKE` for system docs (e.g. `ANSWERABLE_BIOLOGY_SOURCE_MAP.md`), Title_Case for teacher-facing docs. Every doc starts with a one-line purpose and a "Sources used" line at the bottom listing the corpus files it drew from.
