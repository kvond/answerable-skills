# deck_apply_changes — dryrun run, 2026-08-29

Applies the 2026-08-29 changes. Input decks are never modified; every change is written to a new file alongside the original.

- decks considered: 50
- REFUSED: 28
- would change (dry run): 22
- format gate: strict

## What this tool applies, flags, and refuses

APPLIES  the teacher note slide, and the relating prompt on a Concept Bank that only lists terms.
FLAGS    a move-1 Critical Aspect question carrying no difference. The slide is not touched.
REFUSES  a deck that fails the §13 format tokens, or whose canvas is not 4:3.
NEVER    invents what is held invariant, what breaks if an example is substituted, or the visibility rung.

## Cycle 1 — ▶ LIVE — Cycle 01 — Lab Safety (VT).pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 01 — Course Launch & Lab Safety (Unit 1)/▶ LIVE — Cycle 01 — Lab Safety (VT).pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri; Overlock
- SKIPPED: format tokens (§13): off-palette text colors: 000000; 17365D; 1D1B10; 1E1C11; 7030A0; 999999; D68910; D9383A; F9F6FC
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 1 — ▶ LIVE — Cycle01_Day 1.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 01 — Course Launch & Lab Safety (Unit 1)/▶ LIVE — Cycle01_Day 1.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri; Inter; Inter ExtraBold
- SKIPPED: format tokens (§13): off-palette text colors: 1A202C; 2D3748; 4A5568; 718096
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 2 — ▶ LIVE — Cycle 02 — Ecosystems & Feeding Relationships (VT deck).pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/▶ LIVE — Cycle 02 — Ecosystems & Feeding Relationships (VT deck).pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/▶ LIVE — Cycle 02 — Ecosystems & Feeding Relationships (VT deck) — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 2, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S7: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 2 — ▶ LIVE — Cycle 02 — Ecosystems & Feeding Relationships (VT deck) — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/▶ LIVE — Cycle 02 — Ecosystems & Feeding Relationships (VT deck) — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/▶ LIVE — Cycle 02 — Ecosystems & Feeding Relationships (VT deck) — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 27 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 2, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S7: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: teacher note body set to 11pt (from 12pt) so the seven declarations fit on one slide
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 3 — ▶ LIVE — Cycle 03 — Energy Flow & Trophic Pyramids.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)/▶ LIVE — Cycle 03 — Energy Flow & Trophic Pyramids.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Inter; Inter ExtraBold; Inter Medium
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 3 — ▶ LIVE — Cycle 03 — Energy Flow & Trophic Pyramids — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)/▶ LIVE — Cycle 03 — Energy Flow & Trophic Pyramids — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Inter; Inter ExtraBold; Inter Medium
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 4 — ▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 04 — Cycles of Matter_ The Carbon Cycle (Unit 1)/▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 0000FF
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 4 — ▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 04 — Cycles of Matter_ The Carbon Cycle (Unit 1)/▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 0000FF
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 5 — ▶ LIVE — Cycle 05 — Photosynthesis.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 05 — Photosynthesis (Unit 1)/▶ LIVE — Cycle 05 — Photosynthesis.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 05 — Photosynthesis (Unit 1)/▶ LIVE — Cycle 05 — Photosynthesis — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: teacher note body set to 11pt (from 12pt) so the seven declarations fit on one slide
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.
- FLAGGED (no change made): move-1 carries no difference, slide S8
    - inventory: NO CONTRAST DEVICE / independent check: NO CONTRAST DEVICE
    - verbatim: The Sun's energy arrives as light. The plant's food is a sugar. What has to happen to that light for it to end up stored inside the food?
    - suggested reframing (accept or reject): Rebuild move 1 as a choice, so the question carries the difference: "Which of these two — <case A> or <case B> — <the thing that differs>? Why did you choose?" Take <case A> and <case B> from this cycle's own Contrast Set. Aspect at stake: Light energy becomes chemical energy in glucose. (08: an aspect IS a difference. A question that names the thing and waits for the Contrast Set to supply the contrast is the polar bear question and produces silence. Accept, edit, or reject.)
- FLAGGED (no change made): move-1 carries no difference, slide S18
    - inventory: NO CONTRAST DEVICE / independent check: NO CONTRAST DEVICE
    - verbatim: About 400 years ago Van Helmont planted a 5 lb willow tree in 200 lb of dried soil and gave it only water for 5 years. The tree ended up weighing 169 lb — it gained 164 lb. The soil weighed about 199.9 lb; it lost only about 2 ounces. If almost none of the tree came from the soil, where did those pounds of wood, leaves, and sugar actually come from?
    - suggested reframing (accept or reject): Rebuild move 1 as a choice, so the question carries the difference: "Which of these two — <case A> or <case B> — <the thing that differs>? Why did you choose?" Take <case A> and <case B> from this cycle's own Contrast Set. Aspect at stake: A plant's material comes from air and water, not soil. (08: an aspect IS a difference. A question that names the thing and waits for the Contrast Set to supply the contrast is the polar bear question and produces silence. Accept, edit, or reject.)

## Cycle 5 — ▶ LIVE — Cycle 05 — Photosynthesis — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 05 — Photosynthesis (Unit 1)/▶ LIVE — Cycle 05 — Photosynthesis — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 05 — Photosynthesis (Unit 1)/▶ LIVE — Cycle 05 — Photosynthesis — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 28 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: teacher note body set to 11pt (from 12pt) so the seven declarations fit on one slide
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.
- FLAGGED (no change made): move-1 carries no difference, slide S8
    - inventory: NO CONTRAST DEVICE / independent check: NO CONTRAST DEVICE
    - verbatim: The Sun's energy arrives as light. The plant's food is a sugar. What has to happen to that light for it to end up stored inside the food?
    - suggested reframing (accept or reject): Rebuild move 1 as a choice, so the question carries the difference: "Which of these two — <case A> or <case B> — <the thing that differs>? Why did you choose?" Take <case A> and <case B> from this cycle's own Contrast Set. Aspect at stake: Light energy becomes chemical energy in glucose. (08: an aspect IS a difference. A question that names the thing and waits for the Contrast Set to supply the contrast is the polar bear question and produces silence. Accept, edit, or reject.)
- FLAGGED (no change made): move-1 carries no difference, slide S18
    - inventory: NO CONTRAST DEVICE / independent check: NO CONTRAST DEVICE
    - verbatim: About 400 years ago Van Helmont planted a 5 lb willow tree in 200 lb of dried soil and gave it only water for 5 years. The tree ended up weighing 169 lb — it gained 164 lb. The soil weighed about 199.9 lb; it lost only about 2 ounces. If almost none of the tree came from the soil, where did those pounds of wood, leaves, and sugar actually come from?
    - suggested reframing (accept or reject): Rebuild move 1 as a choice, so the question carries the difference: "Which of these two — <case A> or <case B> — <the thing that differs>? Why did you choose?" Take <case A> and <case B> from this cycle's own Contrast Set. Aspect at stake: A plant's material comes from air and water, not soil. (08: an aspect IS a difference. A question that names the thing and waits for the Contrast Set to supply the contrast is the polar bear question and produces silence. Accept, edit, or reject.)

## Cycle 6 — ▶ LIVE — Cycle 06 — Cellular Respiration & Fermentation.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)/▶ LIVE — Cycle 06 — Cellular Respiration & Fermentation.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 6 — ▶ LIVE — Cycle 06 — Cellular Respiration & Fermentation — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)/▶ LIVE — Cycle 06 — Cellular Respiration & Fermentation — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 8 — ▶ LIVE — Cycle 08 — Cells & Organelles.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 08 — Cells & Organelles (Unit 2)/▶ LIVE — Cycle 08 — Cells & Organelles.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 08 — Cells & Organelles (Unit 2)/▶ LIVE — Cycle 08 — Cells & Organelles — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S17: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 8 — ▶ LIVE — Cycle 08 — Cells & Organelles — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 08 — Cells & Organelles (Unit 2)/▶ LIVE — Cycle 08 — Cells & Organelles — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 08 — Cells & Organelles (Unit 2)/▶ LIVE — Cycle 08 — Cells & Organelles — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 28 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S17: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 9 — ▶ LIVE — Cycle 09 (review) — Cell Membrane & Transport.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 09 — Cell Membrane & Transport (Unit 2)/▶ LIVE — Cycle 09 (review) — Cell Membrane & Transport.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: format tokens (§13): off-palette text colors: 000000; 1A1A1A
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 9 — ▶ LIVE — Cycle 09 (review) — Cell Membrane & Transport — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 09 — Cell Membrane & Transport (Unit 2)/▶ LIVE — Cycle 09 (review) — Cell Membrane & Transport — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: format tokens (§13): off-palette text colors: 000000; 1A1A1A
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 10 — ▶ LIVE — Cycle 10 — Enzymes.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 10 — Enzymes (Unit 2)/▶ LIVE — Cycle 10 — Enzymes.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 10 — Enzymes (Unit 2)/▶ LIVE — Cycle 10 — Enzymes — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 10 — ▶ LIVE — Cycle 10 — Enzymes — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 10 — Enzymes (Unit 2)/▶ LIVE — Cycle 10 — Enzymes — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 10 — Enzymes (Unit 2)/▶ LIVE — Cycle 10 — Enzymes — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 31 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 11 — ▶ LIVE — Cycle 11 — The Cell Cycle to Cancer.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 11 — The Cell Cycle → Cancer (Unit 2)/▶ LIVE — Cycle 11 — The Cell Cycle to Cancer.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 11 — ▶ LIVE — Cycle 11 — The Cell Cycle to Cancer — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 11 — The Cell Cycle → Cancer (Unit 2)/▶ LIVE — Cycle 11 — The Cell Cycle to Cancer — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 12 — ▶ LIVE — Cycle 12 — The Process of Meiosis (VT deck, rebuilt).pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 12 — Meiosis (Unit 3)/▶ LIVE — Cycle 12 — The Process of Meiosis (VT deck, rebuilt).pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 12 — Cycle 12 — Meiosis (VT deck, rebuilt) — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 12 — Meiosis (Unit 3)/Cycle 12 — Meiosis (VT deck, rebuilt) — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 13 — ▶ LIVE — Cycle 13— Mendelian Genetics.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 13 — Mendelian Genetics (Unit 3)/▶ LIVE — Cycle 13— Mendelian Genetics.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: format tokens (§13): off-palette text colors: 999999
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 13 — ▶ LIVE — Cycle 13— Mendelian Genetics — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 13 — Mendelian Genetics (Unit 3)/▶ LIVE — Cycle 13— Mendelian Genetics — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: format tokens (§13): off-palette text colors: 999999
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 14 — ▶ LIVE — Cycle 14 — DNA Structure & Replication.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 14 — DNA Structure & Replication (Unit 3)/▶ LIVE — Cycle 14 — DNA Structure & Replication.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: format tokens (§13): off-palette text colors: 999999
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 14 — ▶ LIVE — Cycle 14 — DNA Structure & Replication — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 14 — DNA Structure & Replication (Unit 3)/▶ LIVE — Cycle 14 — DNA Structure & Replication — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): non-Arial fonts: Calibri
- SKIPPED: format tokens (§13): off-palette text colors: 999999
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 17 — ▶ LIVE — Cycle 17 — Darwin & Evidence of Evolution.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 17 — Darwin & Evidence of Evolution (Unit 4)/▶ LIVE — Cycle 17 — Darwin & Evidence of Evolution.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 17 — Darwin & Evidence of Evolution (Unit 4)/▶ LIVE — Cycle 17 — Darwin & Evidence of Evolution — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S8: inventory says 'change condition, comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 17 — ▶ LIVE — Cycle 17 — Darwin & Evidence of Evolution — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 17 — Darwin & Evidence of Evolution (Unit 4)/▶ LIVE — Cycle 17 — Darwin & Evidence of Evolution — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 17 — Darwin & Evidence of Evolution (Unit 4)/▶ LIVE — Cycle 17 — Darwin & Evidence of Evolution — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 29 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S8: inventory says 'change condition, comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 18 — ▶ LIVE — Cycle 18 — Natural Selection & Adaptation.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 18 — Natural Selection & Adaptation (Unit 4)/▶ LIVE — Cycle 18 — Natural Selection & Adaptation.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 18 — Natural Selection & Adaptation (Unit 4)/▶ LIVE — Cycle 18 — Natural Selection & Adaptation — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S8: inventory says 'change condition, comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S19: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 18 — ▶ LIVE — Cycle 18 — Natural Selection & Adaptation — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 18 — Natural Selection & Adaptation (Unit 4)/▶ LIVE — Cycle 18 — Natural Selection & Adaptation — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 18 — Natural Selection & Adaptation (Unit 4)/▶ LIVE — Cycle 18 — Natural Selection & Adaptation — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 30 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S8: inventory says 'change condition, comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S19: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 19 — ▶ LIVE — Cycle 19 — Speciation & Biodiversity.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 19 — Speciation & Biodiversity (Unit 4)/▶ LIVE — Cycle 19 — Speciation & Biodiversity.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 333333
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 19 — ▶ LIVE — Cycle 19 — Speciation & Biodiversity — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 19 — Speciation & Biodiversity (Unit 4)/▶ LIVE — Cycle 19 — Speciation & Biodiversity — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 333333
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 20 — ▶ LIVE — Cycle 20 — Human Impact Capstone.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 20 — Human Impact (Capstone) (Unit 4)/▶ LIVE — Cycle 20 — Human Impact Capstone.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 20 — Human Impact (Capstone) (Unit 4)/▶ LIVE — Cycle 20 — Human Impact Capstone — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S8: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 20 — ▶ LIVE — Cycle 20 — Human Impact Capstone — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 20 — Human Impact (Capstone) (Unit 4)/▶ LIVE — Cycle 20 — Human Impact Capstone — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 20 — Human Impact (Capstone) (Unit 4)/▶ LIVE — Cycle 20 — Human Impact Capstone — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 28 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S8: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 7a — ▶ LIVE — Cycle 07a — Population Ecology.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07a — Population Ecology.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07a — Population Ecology — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.
- FLAGGED (no change made): move-1 carries no difference, slide S8
    - inventory: NO CONTRAST DEVICE / independent check: NO CONTRAST DEVICE
    - verbatim: Twenty-four rabbits became hundreds of millions in about 70 years — a curve shooting straight up. No population in the wild keeps that up forever. What makes a curve like that bend over and flatten?
    - suggested reframing (accept or reject): Rebuild move 1 as a choice, so the question carries the difference: "Which of these two — <case A> or <case B> — <the thing that differs>? Why did you choose?" Take <case A> and <case B> from this cycle's own Contrast Set. Aspect at stake: Why growth bends — J vs S. (08: an aspect IS a difference. A question that names the thing and waits for the Contrast Set to supply the contrast is the polar bear question and produces silence. Accept, edit, or reject.)

## Cycle 7a — ▶ LIVE — Cycle 07a — Population Ecology — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07a — Population Ecology — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07a — Population Ecology — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 29 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.
- FLAGGED (no change made): move-1 carries no difference, slide S8
    - inventory: NO CONTRAST DEVICE / independent check: NO CONTRAST DEVICE
    - verbatim: Twenty-four rabbits became hundreds of millions in about 70 years — a curve shooting straight up. No population in the wild keeps that up forever. What makes a curve like that bend over and flatten?
    - suggested reframing (accept or reject): Rebuild move 1 as a choice, so the question carries the difference: "Which of these two — <case A> or <case B> — <the thing that differs>? Why did you choose?" Take <case A> and <case B> from this cycle's own Contrast Set. Aspect at stake: Why growth bends — J vs S. (08: an aspect IS a difference. A question that names the thing and waits for the Contrast Set to supply the contrast is the polar bear question and produces silence. Accept, edit, or reject.)

## Cycle 7b — ▶ LIVE — Cycle 07b — Populations & Succession.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07b — Populations & Succession.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07b — Populations & Succession — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S8: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 7b — ▶ LIVE — Cycle 07b — Populations & Succession — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07b — Populations & Succession — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)/▶ LIVE — Cycle 07b — Populations & Succession — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 28 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S8: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 15a — ▶ LIVE — Cycle 15a — Genes & Chromosomes.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15a — Genes & Chromosomes.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15a — Genes & Chromosomes — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 15a — ▶ LIVE — Cycle 15a — Genes & Chromosomes — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15a — Genes & Chromosomes — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15a — Genes & Chromosomes — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 29 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 15b — ▶ LIVE — Cycle 15b — Protein Synthesis.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15b — Protein Synthesis.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15b — Protein Synthesis — with 2026-08-29 changes.pptx`
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- SKIPPED: relating prompt: no Concept Bank slide in this deck (build_concept_banks.py has to run first)
- WARNING: move-1 S8: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 15b — ▶ LIVE — Cycle 15b — Protein Synthesis — with Concept Bank.pptx

- status: **would change (dry run)**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15b — Protein Synthesis — with Concept Bank.pptx`
- output: `/Users/katherinevonduyke/deck_work/exports/Cycle 15 — Protein Synthesis (Central Dogma) (Unit 4)/▶ LIVE — Cycle 15b — Protein Synthesis — with Concept Bank — with 2026-08-29 changes.pptx`
- CHANGED: relating prompt appended to Concept Bank slide 29 (co-presence is the precondition, not the achievement)
- CHANGED: teacher note slide inserted at position 3, carrying the seven declarations; 3 left for Katherine
- WARNING: move-1 S8: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- WARNING: move-1 S18: inventory says 'comparison', independent check says 'NO CONTRAST DEVICE'
- FOR KATHERINE: 3 placeholder(s) on the teacher note, in C0392B. The linter can find them on the string `NEEDS KATHERINE:`.

## Cycle 16a — ▶ LIVE — Cycle 16a — Stem Cells and Differentiation.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16a — Stem Cells and Differentiation.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16a — ▶ LIVE — Cycle 16a — Stem Cells and Differentiation — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16a — Stem Cells and Differentiation — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16b — ▶ LIVE — Cycle 16b — Genetic Mutations.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16b — Genetic Mutations.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16b — ▶ LIVE — Cycle 16b — Genetic Mutations — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16b — Genetic Mutations — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16c — ▶ LIVE — Cycle 16c — Mutations and Genetic Disorders.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16c — Mutations and Genetic Disorders.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16c — ▶ LIVE — Cycle 16c — Mutations and Genetic Disorders — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16c — Mutations and Genetic Disorders — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16d — ▶ LIVE — Cycle 16d — Biotechnology.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16d — Biotechnology.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

## Cycle 16d — ▶ LIVE — Cycle 16d — Biotechnology — with Concept Bank.pptx

- status: **REFUSED**
- input: `/Users/katherinevonduyke/deck_work/exports/Cycle 16 — Mutations & Gene Expression (Unit 4)/▶ LIVE — Cycle 16d — Biotechnology — with Concept Bank.pptx`
- SKIPPED: format tokens (§13): off-palette text colors: 000000
- SKIPPED: refused rather than patched. Re-run with --format-gate geometry to apply anyway, which records the debt instead of hiding it.

