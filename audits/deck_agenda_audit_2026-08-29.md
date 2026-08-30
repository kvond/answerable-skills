# Deck / agenda audit — 2026-08-29

Decks are **not finalized**. Everything ADVISORY below is work not done, not a defect. Only HARD blocks.

| | |
|---|---|
| agenda | `/Users/katherinevonduyke/deck_work/agenda_work/Agenda__BACKUP_2026-08-29.xlsx` |
| exports | `/Users/katherinevonduyke/deck_work/exports`, `/Users/katherinevonduyke/deck_work/12b_rebuild` |
| live ids | `/Users/katherinevonduyke/code/answerable-skills/docs/decks_live_ids.csv` (24 rows) |
| inventory | `/Users/katherinevonduyke/code/answerable-skills/audits/deck_inventory_2026-08-29b.csv` |
| agenda rows | 82 |
| decks on disk | 53 (26 canonical) |
| network | OFF |
| HARD | 3 |
| ADVISORY | 182 |

## Needs its own deck

Katherine's ruling: *later units need their own decks.* The earlier date is canonical.

| unit | topic | date | currently reuses |
|---|---|---|---|
| C06e | Cellular Respiration & Glycolysis | 2027-01-08 | C06 Fermentation (2026-10-21) |
| C10 | Cell Transport | 2026-12-14 | C09 Cell Membrane (2026-12-02) |
| C13e | Genetics Continued: Punnett Squares | 2027-03-01 | C13 Introduction to Heredity (2027-02-17) |

## C. Readiness roll-up

| cycle | deck | lint | agenda rows | links | student /copy | live doc_id | verdict |
|---|---|---|---|---|---|---|---|
| Cycle 01 | yes | DOES NOT SHIP | 0 | NO | yes | NO | deck_lint HARD x7; no agenda row; link defects x2; no live doc_id (no import route) |
| Cycle 02 | yes | DOES NOT SHIP | 3 | NO | yes | yes | deck_lint HARD x4; link defects x1 |
| Cycle 03 | yes | DOES NOT SHIP | 1 | yes | yes | yes | deck_lint HARD x3 |
| Cycle 04 | yes | DOES NOT SHIP | 3 | yes | yes | yes | deck_lint HARD x3 |
| Cycle 05 | yes | DOES NOT SHIP | 2 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 06 | yes | DOES NOT SHIP | 7 | yes | yes | yes | deck_lint HARD x3; this deck's day-1 is reused by a later unit, which needs its own |
| Cycle 07a | yes | DOES NOT SHIP | 2 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 07b | yes | DOES NOT SHIP | 3 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 08 | yes | DOES NOT SHIP | 4 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 09 | yes | DOES NOT SHIP | 4 | yes | yes | yes | deck_lint HARD x5; this deck's day-1 is reused by a later unit, which needs its own |
| Cycle 10 | yes | DOES NOT SHIP | 2 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 11 | yes | DOES NOT SHIP | 4 | yes | yes | yes | deck_lint HARD x3 |
| Cycle 12 | yes | DOES NOT SHIP | 3 | yes | yes | yes | deck_lint HARD x5 |
| Cycle 12b | yes | ships | 0 | yes | yes | NO | no agenda row; no live doc_id (no import route) |
| Cycle 13 | yes | DOES NOT SHIP | 9 | yes | yes | yes | deck_lint HARD x3; this deck's day-1 is reused by a later unit, which needs its own |
| Cycle 14 | yes | DOES NOT SHIP | 4 | yes | yes | yes | deck_lint HARD x3 |
| Cycle 15a | yes | DOES NOT SHIP | 2 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 15b | yes | DOES NOT SHIP | 3 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 16a | yes | DOES NOT SHIP | 3 | yes | yes | yes | deck_lint HARD x3 |
| Cycle 16b | yes | DOES NOT SHIP | 0 | yes | yes | yes | deck_lint HARD x3; no agenda row |
| Cycle 16c | yes | DOES NOT SHIP | 0 | yes | yes | yes | deck_lint HARD x3; no agenda row |
| Cycle 16d | yes | DOES NOT SHIP | 0 | yes | yes | yes | deck_lint HARD x3; no agenda row |
| Cycle 17 | yes | DOES NOT SHIP | 1 | yes | yes | yes | deck_lint HARD x2 |
| Cycle 18 | yes | DOES NOT SHIP | 0 | yes | yes | yes | deck_lint HARD x2; no agenda row |
| Cycle 19 | yes | DOES NOT SHIP | 0 | yes | yes | yes | deck_lint HARD x2; no agenda row |
| Cycle 20 | yes | DOES NOT SHIP | 0 | yes | yes | yes | deck_lint HARD x2; no agenda row |

## A. Link integrity

### H-LINK-EMPTY — HARD (1)

- `Biology!H6` — student deck cell shows label text '🎞 Deck ↗' with no URL — the link looks live and goes nowhere

### H-DECK-MISSING — HARD (2)

- `Biology!G3:H3` — scheduled meeting (1 of 2 / School Intro) 2026-08-31 — 'Schedules set up + science sheet' — has NO deck link
- `Biology!G4:H4` — scheduled meeting (2 of 2 / Class intro) 2026-09-02 — 'Look through jobs - interview form-self page' — has NO deck link

### A-BIOLIST-FILEFORM — ADVISORY (15)

- `BioAsList!F4` — Wk 01 'Introduction to Biology' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/open?id=1_DcK-YZWG5AFM7FLykNX71qNe8gP8EejhgnTJaXRQlA
- `BioAsList!F5` — Wk 02 'Ecosystems & Change' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/open?id=1aTfajRO2lX8DrC_oUFm6q3esbv4aABcwxYm8FT6Xh0o
- `BioAsList!F6` — Wk 03 'Intro to Energy' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/open?id=1aTfajRO2lX8DrC_oUFm6q3esbv4aABcwxYm8FT6Xh0o
- `BioAsList!F10` — Wk 07 'Cellular Respiration' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1zhfptAZDoxYNYBHQAAWRv9nAtZgYJSeV/view
- `BioAsList!F14` — Wk 11 'Intro to Cells' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1n_gDVHMbpzn2CPCG6xgP1gOZ4Drp9hVc/view
- `BioAsList!F15` — Wk 12 'Cell Organelles' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1n_gDVHMbpzn2CPCG6xgP1gOZ4Drp9hVc/view
- `BioAsList!F17` — Wk 14 'Cell Membrane' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1g0j8ImOZfuoEv5eeAWBPWfdn12tvmkNS/view
- `BioAsList!F25` — Wk 22 'Introduction to Heredity' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1bAofwJw-zGbjt_7Qb8c2d6_kTMx8rzwz/view
- `BioAsList!F26` — Wk 23 'Intro to Genetics & Mendel' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1taMSu024ussGe1LwynV9D92JFFOfaaGv/view
- `BioAsList!F28` — Wk 25 'Dihybrid Crosses' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/1EV6VsLP0tcYX7QIRxpzU6u5tTD0qqovg/view
- `BioAsList!F35` — Wk 32 'Cell Differentiation and Gene Expression' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/158ZrxKmAsLWB7OnAP6b5_8gKGLkGSI_d/view
- `BioAsList!F36` — Wk 33 'Darwin and the Development of a Theory' VT link is a Drive file link, not presentation/d — cannot be /copy distributed: https://drive.google.com/file/d/158ZrxKmAsLWB7OnAP6b5_8gKGLkGSI_d/view
- _... and 3 more; full list in the findings CSV._

### A-BIOLIST-VT-DRIFT — ADVISORY (6)

- `BioAsList!F4/K4` — Wk 01 'Introduction to Biology': visible VT link (1_DcK-YZWG5AFM7FLykNX71qNe8gP8EejhgnTJaXRQlA) and the _vtURL helper column (1HkyGoPNLN68dT8MBYTcWRBefOa1wlbCXbPfUuGxMxq4) name different decks
- `BioAsList!F6/K6` — Wk 03 'Intro to Energy': visible VT link (1aTfajRO2lX8DrC_oUFm6q3esbv4aABcwxYm8FT6Xh0o) and the _vtURL helper column (16_tL1KMCYRkpZb5UPargPeVRvVxE7_fU5l2sGHc7O9g) name different decks
- `BioAsList!F25/K25` — Wk 22 'Introduction to Heredity': visible VT link (1bAofwJw-zGbjt_7Qb8c2d6_kTMx8rzwz) and the _vtURL helper column (1taMSu024ussGe1LwynV9D92JFFOfaaGv) name different decks
- `BioAsList!F35/K35` — Wk 32 'Cell Differentiation and Gene Expression': visible VT link (158ZrxKmAsLWB7OnAP6b5_8gKGLkGSI_d) and the _vtURL helper column (19AHpmEJe_gWG2gOrUrCeZk5V_lvxOK8f) name different decks
- `BioAsList!F36/K36` — Wk 33 'Darwin and the Development of a Theory': visible VT link (158ZrxKmAsLWB7OnAP6b5_8gKGLkGSI_d) and the _vtURL helper column (19AHpmEJe_gWG2gOrUrCeZk5V_lvxOK8f) name different decks
- `BioAsList!F39/K39` — Wk 36 'The Genetic Basis of Adaptation': visible VT link (1a17iweYkbESLbbebVQ-3hoF3eMvnj5vn) and the _vtURL helper column (1RBHGbts0EJNNXoK5E_tC6a45c0bM6G8P) name different decks

### A-BIOLIST-ORPHAN — ADVISORY (31)

- `BioAsList!F4` — Wk 01 'Introduction to Biology' points at deck 1_DcK-YZWG5AFM7FLykNX71qNe8gP8EejhgnTJaXRQlA, which the dated Biology tab never uses
- `BioAsList!F7` — Wk 04 'Energy Flow' points at deck 13RT17nQTZhNtQCiOu-cpeBeXrCDc71Zb9lKMc7_Gzjs, which the dated Biology tab never uses
- `BioAsList!F8` — Wk 05 'Biogeochemical Cycles' points at deck 1dRdAXmX9u2L-0qKLeW-o9OwoMaaJsik74C9nhysu_GY, which the dated Biology tab never uses
- `BioAsList!F10` — Wk 07 'Cellular Respiration' points at deck 1zhfptAZDoxYNYBHQAAWRv9nAtZgYJSeV, which the dated Biology tab never uses
- `BioAsList!F11` — Wk 08 'Fermentation' points at deck 1EKjFh0ZgeOjEwatzXTbmNXcIXvx6UzP53KkTttmj_Yw, which the dated Biology tab never uses
- `BioAsList!F12` — Wk 09 'Ecological Succession' points at deck 1nl_G0kH65BVa0Jnni0NKn32Y6EjgKXQkYaJA9vpugQM, which the dated Biology tab never uses
- `BioAsList!F13` — Wk 10 'Population Ecology' points at deck 1JhfjicmaKUwJpG6_yzfPZkQ63XvgJ92Nhkm0eZV9dpU, which the dated Biology tab never uses
- `BioAsList!F14` — Wk 11 'Intro to Cells' points at deck 1n_gDVHMbpzn2CPCG6xgP1gOZ4Drp9hVc, which the dated Biology tab never uses
- `BioAsList!F15` — Wk 12 'Cell Organelles' points at deck 1n_gDVHMbpzn2CPCG6xgP1gOZ4Drp9hVc, which the dated Biology tab never uses
- `BioAsList!F17` — Wk 14 'Cell Membrane' points at deck 1g0j8ImOZfuoEv5eeAWBPWfdn12tvmkNS, which the dated Biology tab never uses
- `BioAsList!F18` — Wk 15 'Cell Transport' points at deck 1XZ7F-K9hq1xt65xCHe8WhTxPnnUw2HMrTrT7AJmt2Eo, which the dated Biology tab never uses
- `BioAsList!F20` — Wk 17 'Cellular Respiration & Glycolysis' points at deck 10H4lgRBHqvSIOA_xWwXzxFA-un-UPfImGYr0IzZqEqY, which the dated Biology tab never uses
- _... and 19 more; full list in the findings CSV._

## B. Deck ↔ agenda agreement

### A-DECK-NO-AGENDA — ADVISORY (8)

- `deck:Cycle 01` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 01 — Lab Safety (VT).pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 12b` — built but never scheduled — no agenda row links to 'Cycle 12b — Asexual & Sexual Reproduction (VT deck).pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 16b` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 16b — Genetic Mutations.pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 16c` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 16c — Mutations and Genetic Disorders.pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 16d` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 16d — Biotechnology.pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 18` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 18 — Natural Selection & Adaptation.pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 19` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 19 — Speciation & Biodiversity.pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)
- `deck:Cycle 20` — built but never scheduled — no agenda row links to '▶ LIVE — Cycle 20 — Human Impact Capstone.pptx' (note: 5 agenda deck id(s) could not be resolved — this deck may in fact be scheduled under an id that is missing from decks_live_ids.csv)

### A-AGENDA-NO-DECK — ADVISORY (14)

- `Biology!G71:H71` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-03 — 'Darwin and the Development of a Theory'
- `Biology!G72:H72` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-05 — 'Using Fossil Evidence to Investigate Whale Evolution'
- `Biology!G73:H73` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-10 — 'Using Fossil Evidence to Investigate Whale Evolution'
- `Biology!G74:H74` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-12 — 'Natural Selection'
- `Biology!G75:H75` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-14 — 'Natural Selection'
- `Biology!G76:H76` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-17 — 'Natural Selection'
- `Biology!G77:H77` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-19 — 'The Genetic Basis of Adaptation'
- `Biology!G78:H78` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-24 — 'The Genetic Basis of Adaptation'
- `Biology!G79:H79` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-26 — 'The Processes and Outcomes of Evolution'
- `Biology!G80:H80` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-05-28 — 'The Processes and Outcomes of Evolution'
- `Biology!G81:H81` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-06-02 — 'The Processes and Outcomes of Evolution'
- `Biology!G82:H82` — no deck link; row is not yet a scheduled meeting (block='' phase='') 2027-06-07 — 'Human Impact (Capstone)'
- _... and 2 more; full list in the findings CSV._

### A-ID-UNKNOWN — ADVISORY (5)

- `Biology!G/H` — deck id 11xtdivdeQ_j_JK3Cp2nHCt0wZ5veL5CNF22zxnQiJ1E is in neither decks_live_ids.csv nor any deck on disk; used on 1 row(s): r68 'Cell Differentiation and Gene Expr'
- `Biology!G/H` — deck id 1B40j2p6MtkA-Z_sWDKOUIBpBPHuI0LolDSm9bY8XXQs is in neither decks_live_ids.csv nor any deck on disk; used on 1 row(s): r10 'Intro to Energy'
- `Biology!G/H` — deck id 1CzypbmFAouMpSl-XRAhQp-cdeXbzpVLOQCqMJkigeUw is in neither decks_live_ids.csv nor any deck on disk; used on 1 row(s): r36 'Semester 1 buffer (Year Grid row W'
- `Biology!G/H` — deck id 1GG7e8GszVG4DS0yb51sHsgsnafnwoFMrT7CQcsyBaCk is in neither decks_live_ids.csv nor any deck on disk; used on 1 row(s): r69 'Cell Differentiation and Gene Expr'
- `Biology!G/H` — deck id 1WndV0isfYQzBgk5vjC3RRJfEXB9dz16vlF4F-ru9_M4 is in neither decks_live_ids.csv nor any deck on disk; used on 1 row(s): r5 'Lab Safety + comic + train jobs'

### A-DUP-DAY1 — ADVISORY (3)

- `Biology!H38` — NEEDS ITS OWN DECK — C06e 'Cellular Respiration & Glycolysis' (2027-01-08) reuses the day-1 deck of C06 'Fermentation' (2026-10-21, canonical). Reused deck: Cycle 06 / 1T_T_NqLy3spEa...
- `Biology!H33` — NEEDS ITS OWN DECK — C10 'Cell Transport' (2026-12-14) reuses the day-1 deck of C09 'Cell Membrane' (2026-12-02, canonical). Reused deck: Cycle 09 / 1RukmpUkUEzi2Y...
- `Biology!H53` — NEEDS ITS OWN DECK — C13e 'Genetics Continued: Punnett Squares' (2027-03-01) reuses the day-1 deck of C13 'Introduction to Heredity' (2027-02-17, canonical). Reused deck: Cycle 13 / 1tCPGT4_4CPtHf...

### A-DAY1-NO-DECK — ADVISORY (1)

- `Biology!G3:H3` — first meeting of a 2-meeting cycle (1 of 2) issues no deck: 2026-08-31 — 'Schedules set up + science sheet'

### A-LATER-NEW-DECK — ADVISORY (17)

- `Biology!G11` — meeting 2 of 3 issues a NEW deck (14LaNgK7spPJ..., Cycle 03) — only a '1 of N' row should. 2026-09-28 — 'Energy Flow'
- `Biology!G12` — meeting 3 of 3 issues a NEW deck (1Le0Qf8JEfer..., Cycle 04) — only a '1 of N' row should. 2026-09-30 — 'Biogeochemical Cycles'
- `Biology!G17` — meeting 3 of 4 issues a NEW deck (1T_T_NqLy3sp..., Cycle 06) — only a '1 of N' row should. 2026-10-14 — 'Cellular Respiration'
- `Biology!G21` — meeting 3 of 3 issues a NEW deck (1Q5rshN0etSw..., Cycle 07b) — only a '1 of N' row should. 2026-10-28 — 'Ecological Succession'
- `Biology!G24` — meeting 3 of 3 issues a NEW deck (1OL8oNP1dbgq..., Cycle 07a) — only a '1 of N' row should. 2026-11-04 — 'Population Ecology'
- `Biology!G34` — meeting 2 of 2 issues a NEW deck (189YlTOuF2K9..., Cycle 10) — only a '1 of N' row should. 2026-12-16 — 'Enzymes'
- `Biology!G36` — meeting 2 of 3 issues a NEW deck (1CzypbmFAouM..., unknown id) — only a '1 of N' row should. 2027-01-04 — 'Semester 1 buffer (Year Grid row Wk 16b)'
- `Biology!G37` — meeting 3 of 3 issues a NEW deck (1T_T_NqLy3sp..., Cycle 06) — only a '1 of N' row should. 2027-01-06 — 'Cellular Respiration & Glycolysis'
- `Biology!G40` — meeting 3 of 4 issues a NEW deck (1QP67RSEujgC..., Cycle 11) — only a '1 of N' row should. 2027-01-13 — 'Cell Regulation & Cancer'
- `Biology!G44` — meeting 3 of 4 issues a NEW deck (1Yo1TK_OiCj8..., Cycle 12) — only a '1 of N' row should. 2027-02-01 — 'Asexual & Sexual Reproduction'
- `Biology!G45` — meeting 4 of 4 issues a NEW deck (1lAtQxV4ofC6..., Cycle 16a) — only a '1 of N' row should. 2027-02-03 — 'Stem Cell Differentiation'
- `Biology!G48` — meeting 3 of 3 issues a NEW deck (1tCPGT4_4CPt..., Cycle 13) — only a '1 of N' row should. 2027-02-10 — 'Introduction to Heredity'
- _... and 5 more; full list in the findings CSV._

### A-NO-DAY1 — ADVISORY (6)

- `Biology!G/H` — deck 11xtdivdeQ_j_J... (id unknown) never appears on a '1 of N' row — it is only ever issued mid-cycle: r68 3 of 3
- `Biology!G/H` — deck Cycle 03 (▶ LIVE — Cycle 03 — Energy Flow & Trophic Py) never appears on a '1 of N' row — it is only ever issued mid-cycle: r11 2 of 3
- `Biology!G/H` — deck 1CzypbmFAouMpS... (id unknown) never appears on a '1 of N' row — it is only ever issued mid-cycle: r36 2 of 3
- `Biology!G/H` — deck Cycle 07a (▶ LIVE — Cycle 07a — Population Ecology) never appears on a '1 of N' row — it is only ever issued mid-cycle: r24 3 of 3, r25 option
- `Biology!G/H` — deck Cycle 17 (▶ LIVE — Cycle 17 — Darwin & Evidence of Evo) never appears on a '1 of N' row — it is only ever issued mid-cycle: r70 2 of 2
- `Biology!G/H` — deck Cycle 15a (▶ LIVE — Cycle 15a — Genes & Chromosomes) never appears on a '1 of N' row — it is only ever issued mid-cycle: r63 2 of 4, r64 3 of 4

### A-CYCLE-MISMATCH — ADVISORY (15)

- `Biology!C11` — row is labelled C04 but links to Cycle 03 ('▶ LIVE — Cycle 03 — Energy Flow & Trophic Pyramids')
- `Biology!C14` — row is labelled C05 but links to Cycle 04 ('▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle')
- `Biology!C16` — row is labelled C06 but links to Cycle 05 ('▶ LIVE — Cycle 05 — Photosynthesis')
- `Biology!C20` — row is labelled C07 but links to Cycle 06 ('▶ LIVE — Cycle 06 — Cellular Respiration & Fermentation')
- `Biology!C25` — row is labelled C08 but links to Cycle 07a ('▶ LIVE — Cycle 07a — Population Ecology')
- `Biology!C29` — row is labelled C09 but links to Cycle 08 ('▶ LIVE — Cycle 08 — Cells & Organelles')
- `Biology!C33` — row is labelled C10 but links to Cycle 09 ('▶ LIVE — Cycle 09 (review) — Cell Membrane & Transport')
- `Biology!C39` — row is labelled C11 but links to Cycle 06 ('▶ LIVE — Cycle 06 — Cellular Respiration & Fermentation')
- `Biology!C43` — row is labelled C12 but links to Cycle 11 ('▶ LIVE — Cycle 11 — The Cell Cycle to Cancer')
- `Biology!C44` — row is labelled C16 but links to Cycle 12 ('▶ LIVE — Cycle 12 — The Process of Meiosis (VT deck, reb')
- `Biology!C47` — row is labelled C13 but links to Cycle 16a ('▶ LIVE — Cycle 16a — Stem Cells and Differentiation')
- `Biology!C56` — row is labelled C14 but links to Cycle 13 ('▶ LIVE — Cycle 13— Mendelian Genetics')
- _... and 3 more; full list in the findings CSV._

### A-TOPIC-DRIFT — ADVISORY (6)

- `Biology!D44` — topic 'Asexual & Sexual Reproduction' shares no content word with Cycle 12 ('▶ LIVE — Cycle 12 — The Process of Meiosis (VT d') or its critical aspects ('Two divisions, two different separations | One diploid cell becomes fo')
- `Biology!D48` — topic 'Introduction to Heredity' shares no content word with Cycle 13 ('▶ LIVE — Cycle 13— Mendelian Genetics') or its critical aspects ('Genotype vs. phenotype | One allele per parent (chance)')
- `Biology!D49` — topic 'Introduction to Heredity' shares no content word with Cycle 13 ('▶ LIVE — Cycle 13— Mendelian Genetics') or its critical aspects ('Genotype vs. phenotype | One allele per parent (chance)')
- `Biology!D54` — topic 'Dihybrid Crosses' shares no content word with Cycle 13 ('▶ LIVE — Cycle 13— Mendelian Genetics') or its critical aspects ('Genotype vs. phenotype | One allele per parent (chance)')
- `Biology!D55` — topic 'Dihybrid Crosses' shares no content word with Cycle 13 ('▶ LIVE — Cycle 13— Mendelian Genetics') or its critical aspects ('Genotype vs. phenotype | One allele per parent (chance)')
- `Biology!D56` — topic 'Dihybrid Crosses' shares no content word with Cycle 13 ('▶ LIVE — Cycle 13— Mendelian Genetics') or its critical aspects ('Genotype vs. phenotype | One allele per parent (chance)')

### A-TOPIC-ASPECT-DRIFT — ADVISORY (26)

- `Biology!D7` — topic 'Ecosystems & Change' matches the deck TITLE but none of Cycle 02's critical aspects ('Energy flow through trophic levels | Symbiosis and species relationshi')
- `Biology!D15` — topic 'Photosynthesis' matches the deck TITLE but none of Cycle 05's critical aspects ("Light energy becomes chemical energy in glucose | A plant's material c")
- `Biology!D16` — topic 'Photosynthesis' matches the deck TITLE but none of Cycle 05's critical aspects ("Light energy becomes chemical energy in glucose | A plant's material c")
- `Biology!D17` — topic 'Cellular Respiration' matches the deck TITLE but none of Cycle 06's critical aspects ('Releasing the energy in glucose | Oxygen and how much ATP you get')
- `Biology!D18` — topic 'Cellular Respiration' matches the deck TITLE but none of Cycle 06's critical aspects ('Releasing the energy in glucose | Oxygen and how much ATP you get')
- `Biology!D19` — topic 'Fermentation' matches the deck TITLE but none of Cycle 06's critical aspects ('Releasing the energy in glucose | Oxygen and how much ATP you get')
- `Biology!D20` — topic 'Fermentation' matches the deck TITLE but none of Cycle 06's critical aspects ('Releasing the energy in glucose | Oxygen and how much ATP you get')
- `Biology!D24` — topic 'Population Ecology' matches the deck TITLE but none of Cycle 07a's critical aspects ('Why growth bends — J vs S | What sets carrying capacity')
- `Biology!D25` — topic 'Population Ecology' matches the deck TITLE but none of Cycle 07a's critical aspects ('Why growth bends — J vs S | What sets carrying capacity')
- `Biology!D30` — topic 'Cell Membrane' matches the deck TITLE but none of Cycle 09's critical aspects ('Selective permeability | Bilayer structure')
- `Biology!D31` — topic 'Cell Membrane' matches the deck TITLE but none of Cycle 09's critical aspects ('Selective permeability | Bilayer structure')
- `Biology!D32` — topic 'Cell Transport' matches the deck TITLE but none of Cycle 09's critical aspects ('Selective permeability | Bilayer structure')
- _... and 14 more; full list in the findings CSV._

### A-CYCLE-MULTI-DECK — ADVISORY (1)

- `deck:Cycle 01` — 2 distinct base decks share this cycle key, so only one could be rolled up: ▶ LIVE — Cycle 01 — Lab Safety (VT).pptx; ▶ LIVE — Cycle01_Day 1.pptx

### A-NOT-IN-INVENTORY — ADVISORY (1)

- `deck:Cycle 12b` — 'Cycle 12b — Asexual & Sexual Reproduction (VT deck).pptx' is not in deck_inventory_2026-08-29b.csv — its critical aspects could not be compared against the agenda topic

### A-NO-LIVE-ID — ADVISORY (2)

- `deck:Cycle 01` — no row in decks_live_ids.csv — there is no import route for this deck ('▶ LIVE — Cycle 01 — Lab Safety (VT).pptx')
- `deck:Cycle 12b` — no row in decks_live_ids.csv — there is no import route for this deck ('Cycle 12b — Asexual & Sexual Reproduction (VT deck).pptx')

### A-LINT-HARD — ADVISORY (25)

- `deck:Cycle 01` — deck_lint says DOES NOT SHIP — 7 hard finding(s): H-CONCEPT-BANK, H-FORMAT-FONT, H-FORMAT-HEX, H-FORMAT-SCALE, H-LINKS-SLIDE, H-TEACHER-NOTE, H-TEACHER-PREP (run deck_lint.py for detail; it owns these)
- `deck:Cycle 02` — deck_lint says DOES NOT SHIP — 4 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE, H-TEACHER-PREP, H-VOCAB (run deck_lint.py for detail; it owns these)
- `deck:Cycle 03` — deck_lint says DOES NOT SHIP — 3 hard finding(s): H-CONCEPT-BANK, H-FORMAT-FONT, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 04` — deck_lint says DOES NOT SHIP — 3 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE, H-TEACHER-PREP (run deck_lint.py for detail; it owns these)
- `deck:Cycle 05` — deck_lint says DOES NOT SHIP — 2 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 06` — deck_lint says DOES NOT SHIP — 3 hard finding(s): H-CONCEPT-BANK, H-FORMAT-FONT, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 07a` — deck_lint says DOES NOT SHIP — 2 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 07b` — deck_lint says DOES NOT SHIP — 2 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 08` — deck_lint says DOES NOT SHIP — 2 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 09` — deck_lint says DOES NOT SHIP — 5 hard finding(s): H-CONCEPT-BANK, H-FORMAT-FONT, H-FORMAT-HEX, H-FORMAT-SCALE, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 10` — deck_lint says DOES NOT SHIP — 2 hard finding(s): H-CONCEPT-BANK, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- `deck:Cycle 11` — deck_lint says DOES NOT SHIP — 3 hard finding(s): H-CONCEPT-BANK, H-FORMAT-FONT, H-TEACHER-NOTE (run deck_lint.py for detail; it owns these)
- _... and 13 more; full list in the findings CSV._

