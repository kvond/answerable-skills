# Supply System README

Purpose: how the Master Supply System works — one editable list that produces every quarter checklist, the year shopping view, and the cost totals, so you never maintain supply lists in five places.

## The one rule

Edit only the MASTER sheet. Every other sheet in `Master_Supply_System.xlsx` — the four quarter views, the Full Year view, the COSTS sheet — is built from formulas that read MASTER. Change a quantity, a class count, or a cost once, and every view and every total updates. If you ever find yourself retyping a supply into a second list — a lab-prep sheet, a shopping note, a quarter plan — stop and use a view instead. Two lists always drift; the one that drifted is always the one you grab on lab day.

This is the same one-source-of-truth pattern the rest of the system runs on: the deck is the single student artifact, the Master Agenda is the single operating calendar, and MASTER is the single supply inventory. The Master Agenda and each Unit Agenda carry a one-line supply summary per cycle; the full checklists live here and only here.

## What is in the workbook

- **README** (in-workbook) — the short version of this document, including the editing legend.
- **MASTER** — one row per supply per cycle: quarter, unit, cycle, lesson/deck, activity, supply, quantity per group, groups per class, number of classes, calculated total, reusable/consumable, preparation, storage, safety, approximate cost, substitute, and store link. Sorted by cycle; filter arrows are on the header row.
- **VIEW_Q1 through VIEW_Q4** — what to gather before each quarter. Formulas only; edit MASTER, the view follows.
- **VIEW_FULL_YEAR** — every row, live, for the one big summer shopping pass.
- **COSTS** — initial reusable setup (one-time), recurring consumables (per year), first-year and later-year annual totals, and per-quarter breakdowns. All computed by SUMIF from MASTER.

`Master_Supply_System.csv` is a flat export of MASTER (totals computed) for anything that wants plain data.

## Changing class counts — the two blue columns

The blue cells are yours: **Groups per class** (default 8) and **Number of classes** (default 3). The **Total needed** column is a formula — quantity per group × groups per class × number of classes — so changing either blue number updates the total, the quarter views, and nothing else needs touching.

Two deliberate conventions make the arithmetic honest:

- **Reusable rows have Number of classes = 1.** One physical set serves every class: the Cycle 02 Pacific NW card sets go back in their zip bags and come out again next block (and again in Cycle 07), the Cycle 05 goggles are sanitized between classes, the same eight lamps light every section's leaf-disk lab. Multiplying reusables by your class count would triple-buy equipment you own once. If you teach five sections instead of three, your consumables scale; your card sets don't.
- **Per-class rows have Groups per class = 1.** A teacher demo or a shared stock isn't per-group: one borrowed fish runs the Cycle 06 BTB demo for every class, one box of baking soda mixes every class's leaf-disk solution. These rows say so in their Preparation cell.

Handout rows assume 4 students per group — "Qty per group = 4" means one per student at 8 groups × 4 = 32 students. If your sections run larger, bump the quantity, not a second list. REVIEW WITH KATHERINE.

## Reusable vs. consumable, and what COSTS tells you

Every row is marked **Reusable** (buy once: card sets, goggles, lamps, model kits, pop beads, beans) or **Consumable** (rebought each year: spinach, peroxide, yeast, balloons, PTC strips, pipe cleaners — and every printed handout, which costs $0 on the school copier). COSTS splits the money accordingly: what starting up costs once, what each September costs after that, and which quarter each purchase belongs to. The expensive lines are few and all have cheap substitutes on their MASTER rows — lamps (window light or shared lamps), molecular model kits (paper circles and tape), pop bead kits (chained paper clips). Costs are rough estimates, not quotes — REVIEW WITH KATHERINE.

The shape of the year is worth knowing: Q1 ends with the year's first wet lab (Cycle 05, where the goggles and lamps get bought), Q2 is the wet-lab stretch (fish and BTB, yeast balloons, potato and peroxide), Q3 is genetics and almost entirely print-and-laminate plus the pop beads (HOLD this purchase — the Process of Meiosis deck that carries the Pop Bead lab is SOURCE NOT YET LOCATED), and Q4 is the Cycle 18 kit (beans, beaks, beads) followed by a paper-only capstone.

## Assumptions and flags carried on the sheet

- **Quarter mapping assumed: Q1 = Cycles 1–5, Q2 = 6–10, Q3 = 11–15, Q4 = 16–20.** This is the build's assumption, not Katherine's — the cycles are deliberately flexible, and a real year may land Cycle 16's four decks earlier or later. Stated in the workbook README and flagged REVIEW WITH KATHERINE.
- Store links are **LINK NEEDED** placeholders except where a source deck carries a real URL (the Cycle 02 Pacific NW PDF, the Cycle 03 station checksheet, the Cycle 06 CA1 worksheet, the Cycle 14 activity guides).
- Rows whose printed materials are not yet in the corpus say so inline: the Cycle 07 research assignment, Cycle 08 organizer and coloring sheet, Cycle 11 case study, Cycle 12 CORE deck, Cycle 13 traits inventory, Cycle 15 activity guide, Cycle 16 Desert Bones case, and the Cycle 20 argument template are SOURCE NOT YET LOCATED; the Cycle 07 quadrat materials and the Cycle 06 marshmallow burn are GAP — NOT IN SOURCE NOTES; the Pacific NW PDF is RIGHTS REVIEW NEEDED; the missing Station 3 in Cycle 03 is REVIEW WITH KATHERINE.

## Adding a row

Add it at the bottom of its quarter's block on MASTER (the table is sorted by cycle), then extend that quarter's view down one row by copying the view's last formula row. If you'd rather not touch the views, just work from MASTER with the quarter filter — the views are a convenience, not the data.

## Where this fits

Start Here orients new teachers; the Year Arc shows what each cycle needs in context; Schedule Options places cycles on your calendar; the Master Agenda and Unit Agendas carry the one-line supply summaries that point back here; the Ecology Unit Guide (Cycles 01–07) carries per-cycle supply detail in teaching context; "Set Up Answerable Biology" tells you which of these rows you need before Day 1 — for the ecology arc, nearly all paper and devices.

Sources used: /root/ab_build/output/17_Source_Audit/ANSWERABLE_BIOLOGY_SOURCE_MAP.md (per-deck "Supplies implied" fields) · /root/ab_build/output/04_Ecology/Ecology_Unit_Guide.md (per-cycle supply lists) · /root/ab_build/output/02_Year_Arc/Year_Arc_20_Cycles.md (materials lines, cycle/unit/deck naming) · /root/ab_build/sources/Answerable_Biology_Unit_Descriptions.md (Pop Bead Meiosis lab) · /root/ab_build/BUILD_BRIEF.md
