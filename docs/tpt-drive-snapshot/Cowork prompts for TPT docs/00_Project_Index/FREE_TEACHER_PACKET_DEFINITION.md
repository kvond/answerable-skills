# FREE TEACHER PACKET — DEFINITION AND BUILD STATE

Status: **Proposed, 2026-08-09. Awaiting Katherine's approval.** Nothing here is published; all go/no-go gates stand.

Purpose: to say exactly which files make up the free Ecology product, which stay paid, and which never ship — and to name what is not yet built, against the file it blocks. This is the definition of done for the free release.

## The decision this document records

Katherine, 2026-08-09: the free Ecology unit ships with **the whole teacher packet**, not a five-component subset.

This supersedes decision 2 as written in `RESUME_HERE.md`, which named five components (Cycle 02 deck, Free Unit Guide, Year Arc, Start Here, AI Feedback and Conceptual Growth). Those five remain in the packet; the packet is larger. The reasoning behind decision 2 still holds and now holds more strongly: a free-unit teacher must be able to run the loop end to end, bellringer through Growth Report, without buying anything.

## Group A — the free teacher packet

Seventeen documents. All are built. All are Draft — first build, dated 2026-08-08, and **none has been reviewed by Katherine**, which is a gate on the whole group rather than on any one file.

| # | Document | Folder | Built | Blocking flags |
|---|---|---|---|---|
| 1 | Start_Here_How_Answerable_Biology_Works.md | 01_Start_Here | yes | SNL 1 |
| 2 | How_to_Teach_a_VT_Cycle.md | 03_Setup | yes | cross-refs not inserted; AI-feedback wording to be checked against AI_Feedback doc and the formative-pipeline-v2 spec |
| 3 | Set_Up_Answerable_Biology.md | 03_Setup | yes | **WDN 5** · RWK 2 · SNL 1 · LN 1 · GAP 2 |
| 4 | Year_Arc_20_Cycles.md | 02_Year_Arc | yes | RWK 13 · SNL 12 · RRN 3 · LN 20 · EN 2 · GAP 5 |
| 5 | Master_Agenda.md | 02_Year_Arc | yes | LN 40 (paste-back targets) · RWK 11 · SNL 10 · RRN 4 · EN 2 · GAP 4 |
| 6 | Schedule_Options.md | 02_Year_Arc | yes | SNL 1 |
| 7 | Unit_Agenda_Template.md | 06_Unit_Guides | yes (template) | the **filled** Cycle 02 agenda does not exist — see Blocker 2 |
| 8 | First_Week_Classroom_Conditions.md | 05_First_Week | yes | RWK 7 · EN 1 · GAP 6 — largest build-drafted share in the set; artifacts must be checked against Katherine's real ones |
| 9 | Assessment_Completion_Copying_Proficiency.md | 09_Assessment_Proficiency | yes | RWK 3 · GAP 3 |
| 10 | AI_Feedback_and_Conceptual_Growth.md | 10_AI_Feedback | yes | **WDN 2** · RWK 3 · EN 1 |
| 11 | Activities_Models_and_Labs_Guide.md | 07_Activities_Labs | yes | RWK 12 · SNL 4 · RRN 4 · LN 6 · EN 3 · GAP 7 |
| 12 | Fiddles_Extensions_and_YouTube.md | 08_Fiddles_Extensions | yes | RWK 6 · SNL 2 · RRN 1 · LN 20 · GAP 1 |
| 13 | LMS_Platform_Implementation_Guide.md | 11_Technology_LMS | yes | **WDN 13** · RWK 2 · GAP 3 |
| 14 | Claude_LMS_Gradebook_Workflow.md | 11_Technology_LMS | yes | **WDN 17** · GAP 2 — highest video dependency in the set |
| 15 | Classroom_Technology_for_Formative_Noticing.md | 12_Classroom_Technology | yes | RWK 1 · GAP 3 |
| 16 | Standards_and_Alignment.md | 14_Standards_Alignment | yes | RWK 19 · SNL 5 · EN 1 · GAP 3 |
| 17 | Master_Supply_System.xlsx / .csv + Supply_System_README.md | 13_Supplies | yes | LN 41 rows · quarter-assumption flags still in the README and the xlsx though decision 5 confirmed the mapping |

Plus two unit-level files that ship free with the packet:

| | Item | Built | Note |
|---|---|---|---|
| A | Cycle 02 deck (the free unit) | yes | Not one of the four decks carrying inherited third-party content. Its **visuals** are unregistered — see Blocker 3. |
| B | Free Unit Guide | **no** | An export of the Cycle 02 portion of `Ecology_Unit_Guide.md`. Not yet cut. |
| C | Cycle 02 filled Unit Agenda | **no** | See Blocker 2. |

## Group B — paid, unchanged

The 20 unit listings: each deck plus its filled Unit Agenda and unit-specific materials. Cycle 01 gets its own listing, the twentieth (decision 4). Protein Synthesis is the Cycle 15 EXTEND deck and ships inside the Genes & Chromosomes listing rather than separately (decision 6). Quarter bundles: Q1 = Cycles 01–05, Q2 = 06–10, Q3 = 11–15, Q4 = 16–20 (decision 5); Q1 buyers receive 01, 03, 04, 05 plus infrastructure, with 02 already theirs free.

`Ecology_Unit_Guide.md` in full (Cycles 01–07) stays paid; only the Cycle 02 export goes free.

## Group C — internal, never ships

`PROJECT_INDEX.md`, `REVIEW_REGISTER.md`, `RESUME_HERE.md`, `ANSWERABLE_BIOLOGY_SOURCE_MAP.md`, `ACTIVITY_SOURCE_AND_RIGHTS_AUDIT.md`, `Visual_Rights_and_Credits_Guide.md`, `BROKEN_LINK_REPORT.md`, `TEACHING_REASONING_EXTRACTION.md`, `TPT_Product_Architecture.md`, `TPT_Sales_Copy_and_Preview_Plan.md`, `Video_Setup_Plan.md`, and `Answerable_Biology_Teacher_Lesson_Planning.md` (Katherine's author source, © 2026).

## Blockers, in the order they bind

**1. Video placeholders — 37 flags, closed by 17 recordings.** Of the 48 WORKFLOW DEMONSTRATION NEEDED occurrences in the build, 37 sit in four packet documents: Claude_LMS_Gradebook_Workflow (17), LMS_Platform_Implementation_Guide (13), Set_Up_Answerable_Biology (5), AI_Feedback_and_Conceptual_Growth (2). The other 11 are in Video_Setup_Plan itself, TPT_Sales_Copy, and the Source Map, none of which ship.

Per the coverage table in `Video_Setup_Plan.md`, those 37 flags resolve to **17 distinct recordings, not 28**: Videos 1, 2, 3, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 22, 24, 27, 28. Recording those 17 clears every placeholder a free-packet teacher would encounter. The remaining 11 videos serve paid products and sales previews.

This is the binding constraint, and it is Katherine's alone — the recordings are of her working.

**2. The Cycle 02 filled Unit Agenda does not exist.** The template is built; the 19–20 filled agendas are registered as a GAP in `TPT_Product_Architecture` §3.1 and gate every product, free included. Cycle 02's is the one the packet needs, and building it first tests whether the template survives contact with a real cycle before nineteen more are filled.

**3. Deck visuals are unregistered.** By the rule in `Visual_Rights_and_Credits_Guide` — no CC BY-NC in a product sold on TPT, no ND where a visual is cropped or labeled, "free for teachers" is not commercial-redistribution permission — every photograph and diagram already sitting in the Cycle 02 deck is RIGHTS REVIEW NEEDED until recorded. The Visual Source Register that guide specifies (eighteen fields per placed visual) does not exist as a file. None of these visuals are counted in the 60 RRN occurrences in the flag totals, because that count covers activities, sims, labs, and links only.

Giving the deck away free does not remove this exposure. A free download is still commercial distribution when it drives paid sales, and it is the most widely copied file you will publish.

**4. The Free Unit Guide has not been cut** from `Ecology_Unit_Guide.md`.

**5. No document in the packet has been reviewed by Katherine.** All seventeen are first-draft, and `First_Week_Classroom_Conditions` in particular expands relayed design direction into sections the sources are silent on.

**6. The doc set still describes the pre-decision state.** Both editor agents assigned to apply decisions 1–6 died when the org spend limit was reached (RESUME_HERE item 3). Packet documents currently misstate the tank-model hosting, the quarter mapping, and the free-product contents.

## Definition of done for the free release

1. Seventeen recordings made and linked; 37 WDN flags closed.
2. Cycle 02 filled Unit Agenda built.
3. Visual Source Register created; every Cycle 02 deck visual recorded or replaced.
4. Free Unit Guide cut from the Ecology guide.
5. Decisions 1–6 plus this one applied across the packet documents; coherence QA re-run.
6. Katherine's review pass on all seventeen.

## Open, for Katherine

- **Does the packet ship as seventeen separate files or as one compiled PDF?** Seventeen files match how the build is organized; one compiled document is easier for a teacher to keep and harder for you to update.
- **Is `Answerable_Biology_Teacher_Lesson_Planning.md` staying internal?** It is your author source and carries a copyright line, but it also holds the core-deck rule, which no shipped document states.
- [Not a decision needed today, but it will need one: with the packet free, `TPT_Product_Architecture` §7's product matrix describes a split that no longer exists. That document is the one that will need the most rewriting, and it is also the one every listing is built from.]
