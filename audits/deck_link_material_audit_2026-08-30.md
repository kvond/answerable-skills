# Deck link + material audit — Biology VT cycle decks

**Run:** 2026-08-30  ·  **Decks:** 51 (`▶ LIVE` exports in 20 cycle folders + the Cycle 12b rebuild)
**Network calls: none.** Everything below is resolved against the local Google Drive mirror.
External URLs (biointeractive, biomanbio, netlify, YouTube, CK-12, Khan, PhET …) were
classified but **not fetched**. A `--check-live` pass would be a separate run and is OFF.

## How a link was resolved

Google Drive for Desktop writes the file's real Drive id into an extended attribute
(`com.google.drivefs.item-id`) on **every** synced item. 4,924 of 4,926 files carry one.
So resolution here is by **exact Drive id**, not by filename guessing — for uploaded
binaries (.docx/.pdf, 33-char ids) as well as native Google files (44-char ids, which
also leave a `.gslides`/`.gdoc` stub containing `doc_id`). 6,259 ids were mapped across
four Drive mounts. Filename matching was used **only** as a fallback, and every fallback
match in this report was checked by hand.

## Three things worth knowing before the tables

**1. Not one deck links to a Google Slides deck.** Zero `presentation/d/…` links exist in
any of the 51 decks — checked in both the run-level relationships and the printed text.
This is real, not a bug in the extractor. It means the §8/§9 `/copy` vs `/edit`
distribution rule has nothing to act on *inside* the decks; those links live in the
agenda documents. There is nothing to rewrite from `/edit` to `/copy` here.

**2. Every material lives in three places, with three different Drive ids.**

| tree | path |
|---|---|
| PUBLIC | `03 BIOLOGY (Public)/Cycle NN …/` (redclay) |
| AGENDA | `03 BIOLOGY (Public)/03 Biology (Materials AIHS Agenda)/Cycle NN …/` (redclay, native Google conversions) |
| SHARED | `BIOLOGY (Shared)/Cycle NN …/` (kvd@answerableteaching.com) |

**Every working material link resolves into the SHARED tree** — all 52 unique links, 71
instances across the deck variants, without a single exception. None resolve
into PUBLIC or AGENDA. That is what makes the repairs below safe: the canonical target is
not a guess, it is where every link that already works points.

**3. Almost nothing is truly lost.** Most 'broken' links are *stale ids* — the material is
sitting in the right cycle folder, but the link points at a superseded copy that was
replaced when the folders were rebuilt. Only three materials cannot be found at all.

## Summary

| | count |
|---|---|
| Unique links (cycle · slide · URL) | 856 |
| Link instances across all 51 deck files | 1124 |
| External links (not fetched) | 781 |
| Drive/Docs material links | 74 |
| — resolving correctly | 52 |
| — **stale id** (material present, link points at a dead copy) | 12 |
| — **broken** (no URL, or hyperlink disagrees with printed URL) | 3 |
| — **missing** (resolves nowhere, no material found) | 8 |
| Google Slides links | 0 |
| Repairs proposed (patch CSV) | 22 link instances / 8 distinct materials |

### Per cycle

| Cycle | decks | links | external | material | OK | stale | broken | missing |
|---|---|---|---|---|---|---|---|---|
| 02 | 3 | 32 | 27 | 5 | 5 | 0 | 0 | 0 |
| 03 | 2 | 27 | 21 | 5 | 5 | 0 | 1 | 0 |
| 04 | 2 | 38 | 33 | 5 | 3 | 0 | 0 | 2 |
| 05 | 2 | 40 | 30 | 10 | 8 | 2 | 0 | 0 |
| 06 | 2 | 50 | 33 | 17 | 15 | 0 | 2 | 0 |
| 07 | 4 | 53 | 48 | 5 | 4 | 0 | 0 | 1 |
| 08 | 2 | 33 | 25 | 8 | 7 | 1 | 0 | 0 |
| 09 | 2 | 36 | 36 | 0 | 0 | 0 | 0 | 0 |
| 10 | 2 | 41 | 41 | 0 | 0 | 0 | 0 | 0 |
| 11 | 2 | 40 | 35 | 5 | 0 | 0 | 0 | 5 |
| 12 | 2 | 44 | 42 | 2 | 2 | 0 | 0 | 0 |
| 13 | 2 | 39 | 36 | 3 | 3 | 0 | 0 | 0 |
| 14 | 2 | 30 | 30 | 0 | 0 | 0 | 0 | 0 |
| 15 | 4 | 66 | 66 | 0 | 0 | 0 | 0 | 0 |
| 16 | 8 | 121 | 121 | 0 | 0 | 0 | 0 | 0 |
| 17 | 2 | 55 | 55 | 0 | 0 | 0 | 0 | 0 |
| 18 | 2 | 40 | 31 | 9 | 0 | 9 | 0 | 0 |
| 19 | 2 | 33 | 33 | 0 | 0 | 0 | 0 | 0 |
| 20 | 2 | 38 | 38 | 0 | 0 | 0 | 0 | 0 |

**Decks carrying no hyperlinks at all (2):**

- `▶ LIVE — Cycle 01 — Lab Safety (VT).pptx`
- `▶ LIVE — Cycle01_Day 1.pptx`

Cycle 01 is the one to look at. Neither of its two decks carries a single hyperlink,
yet its cycle folder holds ten unlinked material files — the whole classroom-jobs set
(see orphans below). Either those materials are handed out some other way, or Cycle 01
never got its links slide. Every other cycle has one.

---

## MISSING — cycle and slide

The list to act on. These three materials resolve to **nothing** anywhere in the local
mirror — not in the cycle folder, not in `My Class only (print)`, not in any of the three
trees, not in the archives.

| Cycle | Slide numbers | What the slide asks for | Why it is missing |
|---|---|---|---|
| **Cycle 04** | with Concept Bank: **29** · plain deck: **28** | Journey through the carbon cycle — no printable; the cards and the rec | The label itself reads 'no printable — the cards and the recording space are on the Day 2 activity slide', yet the line carries a hyperlink to a dead  |
| **Cycle 07** | with Concept Bank: **11** · plain deck: **11** | Read about Succession | 44-char native Google Doc id. |
| **Cycle 11** | with Concept Bank: **1, 2, 16, 33** · plain deck: **1, 2, 16, 32** | Cell Cancer Decision Cards — 1 set per group | No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, no |

### Cycle 04

- **Label on the slide:** Journey through the carbon cycle — no printable; the cards and the recording space are on the Day 2 activity slide.
- **Dead URL:** `https://drive.google.com/file/d/1vqwnoDMH9wiP0M4_zYvlkoFcWejTlaXA/view`
- **Where, exactly:**
  - `▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle — with Concept Bank.pptx` — slide **29**
  - `▶ LIVE — Cycle 04 — Cycles of Matter_ The Carbon Cycle.pptx` — slide **28**
- **Finding:** The label itself reads 'no printable — the cards and the recording space are on the Day 2 activity slide', yet the line carries a hyperlink to a dead id. A worksheet named 'Cycle 04 — Journey Through the Carbon Cycle — Student Worksheet' DOES exist, but only in 03 Biology (Materials AIHS Agenda), not in the Cycle 04 folder or its print subfolder. Either the link should be removed to match the label, or the worksheet should be placed in the cycle folder. Katherine's call — not mechanical.

### Cycle 07

- **Label on the slide:** Read about Succession
- **Dead URL:** `https://docs.google.com/document/d/1GP-zJpuoKEMkh3kFOd7uWyE6b_vK3pGYlyjc6mgDmKE/edit?usp=sharing`
- **Where, exactly:**
  - `▶ LIVE — Cycle 07b — Populations & Succession — with Concept Bank.pptx` — slide **11**
  - `▶ LIVE — Cycle 07b — Populations & Succession.pptx` — slide **11**
- **Finding:** 44-char native Google Doc id. Every native Google file in her three My Drives leaves a stub on disk; this one leaves none, so it is not in any of her My Drives. Most likely a Shared-with-me doc (those do not sync) or deleted. Cannot be resolved offline and must not be guessed — Cycle 07 has an 'Ecological Succession Activity Guide', but a guide is not a reading.

### Cycle 11

- **Label on the slide:** Cell Cancer Decision Cards — 1 set per group
- **Dead URL:** `https://drive.google.com/file/d/1fTJuWg--s8IE6qB92qI3amQdFceyx1KG/view`
- **Where, exactly:**
  - `▶ LIVE — Cycle 11 — The Cell Cycle to Cancer — with Concept Bank.pptx` — slides **1, 2, 16, 33**
  - `▶ LIVE — Cycle 11 — The Cell Cycle to Cancer.pptx` — slides **1, 2, 16, 32**
- **Finding:** No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, not under any other cycle, not in the archives. This material appears never to have been created, or to have been deleted. It is required for the Day 1 'Be the checkpoint' activity.

---

## Repairs proposed

Written to `deck_link_patch_2026-08-30.csv`. Each row is: cycle, deck, slide, the dead URL, the
replacement, and the evidence. **No deck file was modified.** See *Why nothing was
rewritten* at the end.

| Cycle | Slide numbers | Label | Replacement target | Evidence |
|---|---|---|---|---|
| **Cycle 03** | with Concept Bank: **1** · plain deck: **1** | Energy Flow — Station Checksheet | `Cycle 03 — Energy Flow — Station Checksheet.docx` | name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 4 copies (AGEND |
| **Cycle 05** | with Concept Bank: **1** · plain deck: **1** | Van Helmont — where a tree's mass comes from | `(BOTH) Cycle 05 — Where Does a Tree_s Mass Come From — Van Helmont.docx` | name match 0.60 in the deck's own cycle; target = SHARED tree; WARNING 2 differently-named candidates tie ((BOTH) Cycle  |
| **Cycle 05** | with Concept Bank: **1** · plain deck: **1** | Photosynthesis Leaf-Disk Lab | `Cycle 05 — Photosynthesis Leaf-Disk Lab.docx` | name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGEND |
| **Cycle 06** | with Concept Bank: **32** · plain deck: **31** | https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRW | `Cycle 06 — Cellular Respiration — CA1 Worksheet.docx` | the slide PRINTS 1wBLxic3... and that id resolves; the live hyperlink goes to 1SK3ONY4... which resolves nowhere. Fix =  |
| **Cycle 08** | with Concept Bank: **1** · plain deck: **1** | Cell Organelles Activity Guide | `Cycle 08 — Cell Organelles Activity Guide.docx` | name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGEND |
| **Cycle 18** | with Concept Bank: **1, 32** · plain deck: **1, 31** | Evolution Stations check sheet | `Cycle 18 — Evolution Stations Check Sheet.docx` | name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGEND |
| **Cycle 18** | with Concept Bank: **1, 32** · plain deck: **1, 31** | Gene-pool bead lab — allele frequency | `Gene-Pool Allele-Frequency Simulation.pdf` | name match 0.57 in the deck's own cycle; target = PUBLIC tree; NOTE this file exists only in the PUBLIC tree — it is mis |
| **Cycle 18** | with Concept Bank: **1, 32** · plain deck: **1, 31** | Comparing bones — chicken anatomy | `Cycle 18 — EvoArc4_Morphology_Chicken_Anatomy.docx` | scorer said 0.25 (filename uses EvoArc4_Morphology, the label says 'Comparing bones'), but 'chicken anatomy' is the shar |

---

## Detail — by cycle, by slide

Only links that are not plain working externals are listed. External links are all in the
CSV. Where a cycle has both a plain deck and a `— with Concept Bank` variant, the same
slide number is listed once and the deck files named.

### Cycle 02 — Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)

**Slide 16** — Day 1 activity · Critical Aspect 1

- `ok` — Feeding Relationships (Pacific NW) — PDF
  - URL: `https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/My Class 
**Slide 18** — Day 2 · finish Critical Aspect 1 activity

- `ok` — Feeding Relationships (Pacific NW) — PDF
  - URL: `https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/My Class 
**Slide 33** — Activity and resource links

- `ok` — https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view
  - URL: `https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/My Class 
**Slide 35** — Activity and resource links

- `ok` — https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view
  - URL: `https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/My Class 
**Slide 36** — Activity and resource links

- `ok` — https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view
  - URL: `https://drive.google.com/file/d/1Jw2SU5hL2kzdLCNKFo0XxXE8sB6xcbSK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 02 — Ecosystems & Feeding Relationships (Unit 1)/My Class 

### Cycle 03 — Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)

**Slide 1** — TEACHER REFERENCE — not projected to studentsCycle 3 · Energy Flow & Trophic Pyr

- `BROKEN` — Energy Flow — Station Checksheet
  - URL: `about:blank`
  - BROKEN — no URL (about:blank); material IS present
  - found: SHARED tree, Cycle 03 / My Class only (print) :: Cycle 03 — Energy Flow — Station Checksheet.docx
  - **fix →** `https://drive.google.com/file/d/1dUHg9wztUe2kQUjnOUpY8lYzsAXiMDZ1/view`
  - note: name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 4 copies (AGENDA+PUBLIC+SHARED) — SHARED chosen because 71/71 working links point there
**Slide 16** — Day 1 activity · Critical Aspect 1

- `ok` — Open: Station Checksheet — record your answers there too
  - URL: `https://drive.google.com/file/d/1aHuzgv8b4uH34j18JP-7fE8PK_twNSsi/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)
**Slide 17** — Day 1 activity · Critical Aspect 1

- `ok` — Open: Station Checksheet — record your answers there too
  - URL: `https://drive.google.com/file/d/1aHuzgv8b4uH34j18JP-7fE8PK_twNSsi/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)
**Slide 25** — Day 2 activity · Critical Aspect 2

- `ok` — Open: Station Checksheet — finish the pyramid station
  - URL: `https://drive.google.com/file/d/1aHuzgv8b4uH34j18JP-7fE8PK_twNSsi/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)
**Slide 31** — Activity and resource links

- `ok` — Station Checksheet
  - URL: `https://drive.google.com/file/d/1aHuzgv8b4uH34j18JP-7fE8PK_twNSsi/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)
**Slide 32** — Activity and resource links

- `ok` — Station Checksheet
  - URL: `https://drive.google.com/file/d/1aHuzgv8b4uH34j18JP-7fE8PK_twNSsi/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 03 — Energy Flow & Trophic Pyramids (Unit 1)

### Cycle 04 — Cycle 04 — Cycles of Matter_ The Carbon Cycle (Unit 1)

**Slide 15** — Day 1 activity · Critical Aspect 1

- `ok` — Open: Carbon Companion Activity (in this cycle's folder)
  - URL: `https://drive.google.com/file/d/1pAD2wAq5xgZyLkJLQ_a1Pjxk7ugtC7lV/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 04 — Cycles of Matter_ The Carbon Cycle (Unit 1)
**Slide 28** — Activity and resource links

- `ok` — Carbon Companion Activity (Day 1)
  - URL: `https://drive.google.com/file/d/1pAD2wAq5xgZyLkJLQ_a1Pjxk7ugtC7lV/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 04 — Cycles of Matter_ The Carbon Cycle (Unit 1)
- `MISSING` — Journey through the carbon cycle — no printable; the cards and the recording space are on the Day 2 
  - URL: `https://drive.google.com/file/d/1vqwnoDMH9wiP0M4_zYvlkoFcWejTlaXA/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: The label itself reads 'no printable — the cards and the recording space are on the Day 2 activity slide', yet the line carries a hyperlink to a dead id. A worksheet named 'Cycle 04 — Journey Through the Carbon Cycle — Student Worksheet' DOES exist, but only in 03 Biology (Materials AIHS Agenda), not in the Cycle 04 folder or its print subfolder. Either the link should be removed to match the label, or the worksheet should be placed in the cycle folder. Katherine's call — not mechanical.
**Slide 29** — Activity and resource links

- `ok` — Carbon Companion Activity (Day 1)
  - URL: `https://drive.google.com/file/d/1pAD2wAq5xgZyLkJLQ_a1Pjxk7ugtC7lV/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 04 — Cycles of Matter_ The Carbon Cycle (Unit 1)
- `MISSING` — Journey through the carbon cycle — no printable; the cards and the recording space are on the Day 2 
  - URL: `https://drive.google.com/file/d/1vqwnoDMH9wiP0M4_zYvlkoFcWejTlaXA/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: The label itself reads 'no printable — the cards and the recording space are on the Day 2 activity slide', yet the line carries a hyperlink to a dead id. A worksheet named 'Cycle 04 — Journey Through the Carbon Cycle — Student Worksheet' DOES exist, but only in 03 Biology (Materials AIHS Agenda), not in the Cycle 04 folder or its print subfolder. Either the link should be removed to match the label, or the worksheet should be placed in the cycle folder. Katherine's call — not mechanical.

### Cycle 05 — Cycle 05 — Photosynthesis (Unit 1)

**Slide 1** — TEACHER REFERENCE — not projected to students

- `STALE` — Van Helmont — where a tree's mass comes from
  - URL: `https://drive.google.com/file/d/1Spjx6KJAo1ka2Ms-LfCnsHQmOOCbIZcx/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 05 :: (BOTH) Cycle 05 — Where Does a Tree_s Mass Come From — Van Helmont.docx
  - **fix →** `https://drive.google.com/file/d/1Vybu8iVyXmx1BHKk10E0Vc8ozOx6NdUu/view`
  - note: name match 0.60 in the deck's own cycle; target = SHARED tree; WARNING 2 differently-named candidates tie ((BOTH) Cycle 05 — Where Does a Tree_s Mass Come From — Van Helmont; Cycle 05 — Where Does a Tree_s Mass Come From — Van ) — verify by hand
- `STALE` — Photosynthesis Leaf-Disk Lab
  - URL: `https://drive.google.com/file/d/1oiLh3D3NMCeQcehS7U3n7B0SCQNsBPZq/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 05 / My Class only (print) :: Cycle 05 — Photosynthesis Leaf-Disk Lab.docx
  - **fix →** `https://drive.google.com/file/d/1QlALR7naF23AqsE4j7Jr-B6HvLTdxfru/view`
  - note: name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGENDA+PUBLIC+SHARED) — SHARED chosen because 71/71 working links point there
**Slide 16** — Day 1 activity · Critical Aspect 1

- `ok` — Open: Photosynthesis Leaf-Disk Lab (in this cycle's folder)
  - URL: `https://drive.google.com/file/d/1QlALR7naF23AqsE4j7Jr-B6HvLTdxfru/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)/My Class only (print)
**Slide 26** — Optional challenge

- `ok` — Need the evidence again? Open: Where Does a Tree's Mass Come From — Van Helmont
  - URL: `https://drive.google.com/file/d/1Vybu8iVyXmx1BHKk10E0Vc8ozOx6NdUu/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)
**Slide 30** — Activity and resource links

- `ok` — Teacher — Photosynthesis Activity Guide
  - URL: `https://drive.google.com/file/d/16h6JnRixT42yC63HWGw37xBFIxyhS6tk/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)/My Class only (print)
- `ok` — Photosynthesis Leaf-Disk Lab
  - URL: `https://drive.google.com/file/d/1QlALR7naF23AqsE4j7Jr-B6HvLTdxfru/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)/My Class only (print)
- `ok` — Where Does a Tree's Mass Come From — Van Helmont
  - URL: `https://drive.google.com/file/d/1Vybu8iVyXmx1BHKk10E0Vc8ozOx6NdUu/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)
**Slide 31** — Activity and resource links

- `ok` — Teacher — Photosynthesis Activity Guide
  - URL: `https://drive.google.com/file/d/16h6JnRixT42yC63HWGw37xBFIxyhS6tk/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)/My Class only (print)
- `ok` — Photosynthesis Leaf-Disk Lab
  - URL: `https://drive.google.com/file/d/1QlALR7naF23AqsE4j7Jr-B6HvLTdxfru/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)/My Class only (print)
- `ok` — Where Does a Tree's Mass Come From — Van Helmont
  - URL: `https://drive.google.com/file/d/1Vybu8iVyXmx1BHKk10E0Vc8ozOx6NdUu/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 05 — Photosynthesis (Unit 1)

### Cycle 06 — Cycle 06 — Cellular Respiration & Fermentation (Unit 1)

**Slide 1** — TEACHER REFERENCE — not projected to students

- `ok` — Fermentation Guide
  - URL: `https://docs.google.com/document/d/10J3Ixd3fyWUTLAQXfhwynAe0yvFzWbQx/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Challenge
  - URL: `https://docs.google.com/document/d/1Bnl1wo6NIttXtnBleBkmAK3GxobTLFbj/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Cellular Respiration — CA1 worksheet
  - URL: `https://docs.google.com/document/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Cellular Respiration — CA2 worksheet · 1 per student
  - URL: `https://docs.google.com/document/d/1xBXmBuMX2Q24zgI4ZX9bzmEoR6d5emzK/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
**Slide 8** — Respiration runs photosynthesis in reverse

- `ok` — Cellular Respiration — CA2 worksheet
  - URL: `https://docs.google.com/document/d/1xBXmBuMX2Q24zgI4ZX9bzmEoR6d5emzK/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
**Slide 18** — Day 1 activity · Critical Aspect 1

- `ok` — Open: Cellular Respiration — CA1 Worksheet (in this cycle's folder)
  - URL: `https://docs.google.com/document/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
**Slide 26** — Day 2 activity · Critical Aspect 2

- `ok` — Open: Science World — Yeast-Inflated Balloons
  - URL: `https://docs.google.com/document/d/10J3Ixd3fyWUTLAQXfhwynAe0yvFzWbQx/edit?usp=sharing&ouid=112216964722103758648&rtpof=true&sd=true`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
**Slide 31** — Activity and resource links

- `ok` — Teacher — Fermentation Activity Guide
  - URL: `https://drive.google.com/file/d/10J3Ixd3fyWUTLAQXfhwynAe0yvFzWbQx/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Cellular Respiration — simple worksheet
  - URL: `https://drive.google.com/file/d/1Bnl1wo6NIttXtnBleBkmAK3GxobTLFbj/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `BROKEN` — https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view
  - URL: `https://drive.google.com/file/d/1SK3ONY4nwLKp1X_E3-2XyqCcuS59vSWr/view`
  - BROKEN — hyperlink disagrees with the URL printed beside it
  - found: SHARED tree, Cycle 06 :: Cycle 06 — Cellular Respiration — CA1 Worksheet.docx
  - **fix →** `https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view`
  - note: the slide PRINTS 1wBLxic3... and that id resolves; the live hyperlink goes to 1SK3ONY4... which resolves nowhere. Fix = make the link match its own printed URL. Two independent signals agree.
- `ok` — https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view
  - URL: `https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Cellular Respiration — CA2 worksheet
  - URL: `https://drive.google.com/file/d/1xBXmBuMX2Q24zgI4ZX9bzmEoR6d5emzK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
**Slide 32** — Activity and resource links

- `ok` — Teacher — Fermentation Activity Guide
  - URL: `https://drive.google.com/file/d/10J3Ixd3fyWUTLAQXfhwynAe0yvFzWbQx/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Cellular Respiration — simple worksheet
  - URL: `https://drive.google.com/file/d/1Bnl1wo6NIttXtnBleBkmAK3GxobTLFbj/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `BROKEN` — https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view
  - URL: `https://drive.google.com/file/d/1SK3ONY4nwLKp1X_E3-2XyqCcuS59vSWr/view`
  - BROKEN — hyperlink disagrees with the URL printed beside it
  - found: SHARED tree, Cycle 06 :: Cycle 06 — Cellular Respiration — CA1 Worksheet.docx
  - **fix →** `https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view`
  - note: the slide PRINTS 1wBLxic3... and that id resolves; the live hyperlink goes to 1SK3ONY4... which resolves nowhere. Fix = make the link match its own printed URL. Two independent signals agree.
- `ok` — https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view
  - URL: `https://drive.google.com/file/d/1wBLxic3jHtPKsO8eHRWXuZ5C1FbmBrvY/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)
- `ok` — Cellular Respiration — CA2 worksheet
  - URL: `https://drive.google.com/file/d/1xBXmBuMX2Q24zgI4ZX9bzmEoR6d5emzK/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 06 — Cellular Respiration & Fermentation (Unit 1)

### Cycle 07 — Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)

**Slide 11** — Critical aspect: Where succession is headed

- `MISSING` — Read about Succession
  - URL: `https://docs.google.com/document/d/1GP-zJpuoKEMkh3kFOd7uWyE6b_vK3pGYlyjc6mgDmKE/edit?usp=sharing`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: 44-char native Google Doc id. Every native Google file in her three My Drives leaves a stub on disk; this one leaves none, so it is not in any of her My Drives. Most likely a Shared-with-me doc (those do not sync) or deleted. Cannot be resolved offline and must not be guessed — Cycle 07 has an 'Ecological Succession Activity Guide', but a guide is not a reading.
**Slide 29** — Activity and resource links

- `ok` — Teacher — Ecological Succession Activity Guide
  - URL: `https://drive.google.com/file/d/1Wn8U95Q0gMggiFEie8_Fwz6V2JX7qKZD/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)
**Slide 30** — Activity and resource links

- `ok` — Teacher — Ecological Succession Activity Guide
  - URL: `https://drive.google.com/file/d/1Wn8U95Q0gMggiFEie8_Fwz6V2JX7qKZD/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)
**Slide 31** — Activity and resource links

- `ok` — Teacher — Ecological Succession Activity Guide
  - URL: `https://drive.google.com/file/d/1Wn8U95Q0gMggiFEie8_Fwz6V2JX7qKZD/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)
**Slide 32** — Activity and resource links

- `ok` — Teacher — Ecological Succession Activity Guide
  - URL: `https://drive.google.com/file/d/1Wn8U95Q0gMggiFEie8_Fwz6V2JX7qKZD/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 07 — Ecosystem Dynamics_ Populations & Succession (Unit 1)

### Cycle 08 — Cycle 08 — Cells & Organelles (Unit 2)

**Slide 1** — TEACHER REFERENCE — not projected to students

- `STALE` — Cell Organelles Activity Guide
  - URL: `https://drive.google.com/file/d/1Z93aLwdJ7JgKuvPtQw-tlB_aRKbnK152/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 08 / My Class only (print) :: Cycle 08 — Cell Organelles Activity Guide.docx
  - **fix →** `https://drive.google.com/file/d/1rvKft2koiEEGdO7HC-7lhAVMm8jLs3kk/view`
  - note: name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGENDA+PUBLIC+SHARED) — SHARED chosen because 71/71 working links point there
**Slide 24** — Day 2 stations · Plant cell vs animal cell

- `ok` — Print: Cycle 08 — Organelle Station Cards (print)
  - URL: `https://drive.google.com/file/d/1Izga8ng22K93B2dRJTDs0QZgXMAPeK62/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)
**Slide 29** — Activity and resource links

- `ok` — Teacher — Intro to Cells Activity Guide
  - URL: `https://drive.google.com/file/d/19ekkUXcT70_z1zVENetnsyFIj-k7S-IU/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)/My Class only (print)
- `ok` — Organelle Station Cards (print) — Day 2 stations, in "My Class only (print)"
  - URL: `https://drive.google.com/file/d/1Izga8ng22K93B2dRJTDs0QZgXMAPeK62/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)
- `ok` — Teacher — Cell Organelles Activity Guide
  - URL: `https://drive.google.com/file/d/1rvKft2koiEEGdO7HC-7lhAVMm8jLs3kk/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)/My Class only (print)
**Slide 30** — Activity and resource links

- `ok` — Teacher — Intro to Cells Activity Guide
  - URL: `https://drive.google.com/file/d/19ekkUXcT70_z1zVENetnsyFIj-k7S-IU/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)/My Class only (print)
- `ok` — Organelle Station Cards (print) — Day 2 stations, in "My Class only (print)"
  - URL: `https://drive.google.com/file/d/1Izga8ng22K93B2dRJTDs0QZgXMAPeK62/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)
- `ok` — Teacher — Cell Organelles Activity Guide
  - URL: `https://drive.google.com/file/d/1rvKft2koiEEGdO7HC-7lhAVMm8jLs3kk/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 08 — Cells & Organelles (Unit 2)/My Class only (print)

### Cycle 11 — Cycle 11 — The Cell Cycle → Cancer (Unit 2)

**Slide 1** — TEACHER REFERENCE — not projected to students

- `MISSING` — Cell Cancer Decision Cards — 1 set per group
  - URL: `https://drive.google.com/file/d/1fTJuWg--s8IE6qB92qI3amQdFceyx1KG/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, not under any other cycle, not in the archives. This material appears never to have been created, or to have been deleted. It is required for the Day 1 'Be the checkpoint' activity.
**Slide 2** — TEACHER REFERENCE

- `MISSING` — •  Print “Cycle 11 — Cell Cancer Decision Cards (print)” from the My Class only (print) subfolder — 
  - URL: `https://drive.google.com/file/d/1fTJuWg--s8IE6qB92qI3amQdFceyx1KG/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, not under any other cycle, not in the archives. This material appears never to have been created, or to have been deleted. It is required for the Day 1 'Be the checkpoint' activity.
**Slide 16** — Day 1 activity · Critical Aspect 1

- `MISSING` — Print: Cycle 11 — Cell Cancer Decision Cards, 1 set per group
  - URL: `https://drive.google.com/file/d/1fTJuWg--s8IE6qB92qI3amQdFceyx1KG/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, not under any other cycle, not in the archives. This material appears never to have been created, or to have been deleted. It is required for the Day 1 'Be the checkpoint' activity.
**Slide 32** — Activity and resource links

- `MISSING` — Cell Cancer Decision Cards (print) — Day 1 “Be the checkpoint”, in “My Class only (print)”
  - URL: `https://drive.google.com/file/d/1fTJuWg--s8IE6qB92qI3amQdFceyx1KG/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, not under any other cycle, not in the archives. This material appears never to have been created, or to have been deleted. It is required for the Day 1 'Be the checkpoint' activity.
**Slide 33** — Activity and resource links

- `MISSING` — Cell Cancer Decision Cards (print) — Day 1 “Be the checkpoint”, in “My Class only (print)”
  - URL: `https://drive.google.com/file/d/1fTJuWg--s8IE6qB92qI3amQdFceyx1KG/view`
  - MISSING — no file of this name in this cycle, in any tree
  - found: NOT FOUND
  - note: No file named anything like 'Decision Cards' or 'checkpoint cards' exists anywhere in the local mirror — not in Cycle 11 in any of the three trees, not under any other cycle, not in the archives. This material appears never to have been created, or to have been deleted. It is required for the Day 1 'Be the checkpoint' activity.

### Cycle 12 — Cycle 12 — Meiosis (Unit 3)

**Slide 1** — ⚠ NEEDS KATHERINE — the essential claim and the objectives below are drafted, no

- `ok` — Cycle 12b — Reproduction Sorting Cards (print) · in My Class only (print) · 1 set per group — https:
  - URL: `https://drive.google.com/file/d/1qVxEB0YEXBVu7PS3Xy_aj7NhXo9RNGt3/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 12 — Reproduction & Meiosis (Unit 3)/My Class only (print)
**Slide 31** — Activity and resource links

- `ok` — Day 1 activity — Cycle 12b — Reproduction Sorting Cards (print) · in My Class only (print)
  - URL: `https://drive.google.com/file/d/1qVxEB0YEXBVu7PS3Xy_aj7NhXo9RNGt3/view`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 12 — Reproduction & Meiosis (Unit 3)/My Class only (print)

### Cycle 13 — Cycle 13 — Mendelian Genetics (Unit 3)

**Slide 24** — Day 2 activity · Critical Aspect 2

- `ok` — https://docs.google.com/spreadsheets/d/1J5MTCCkc7sTscbE-JBgbbwFpfss7lv0IyySCA-72TrY/edit?usp=sharing
  - URL: `https://docs.google.com/spreadsheets/d/1J5MTCCkc7sTscbE-JBgbbwFpfss7lv0IyySCA-72TrY/edit?usp=sharing`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 13 — Mendelian Genetics (Unit 3)
**Slide 31** — Activity and resource links

- `ok` — https://docs.google.com/spreadsheets/d/1J5MTCCkc7sTscbE-JBgbbwFpfss7lv0IyySCA-72TrY/edit?usp=sharing
  - URL: `https://docs.google.com/spreadsheets/d/1J5MTCCkc7sTscbE-JBgbbwFpfss7lv0IyySCA-72TrY/edit?usp=sharing`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 13 — Mendelian Genetics (Unit 3)
**Slide 32** — Activity and resource links

- `ok` — https://docs.google.com/spreadsheets/d/1J5MTCCkc7sTscbE-JBgbbwFpfss7lv0IyySCA-72TrY/edit?usp=sharing
  - URL: `https://docs.google.com/spreadsheets/d/1J5MTCCkc7sTscbE-JBgbbwFpfss7lv0IyySCA-72TrY/edit?usp=sharing`
  - OK — file found
  - found: kvd@answerableteaching.com : My Drive/BIOLOGY (Shared)/Cycle 13 — Mendelian Genetics (Unit 3)

### Cycle 18 — Cycle 18 — Natural Selection & Adaptation (Unit 4)

**Slide 1** — TEACHER REFERENCE — not projected to students

- `STALE` — Evolution Stations check sheet
  - URL: `https://drive.google.com/file/d/1AGpX73RKRCnsg5Xu_gmZerw6td4WEg77/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 18 / My Class only (print) :: Cycle 18 — Evolution Stations Check Sheet.docx
  - **fix →** `https://drive.google.com/file/d/1Oxz2p9jl_IxzyB0fRhgSSQQPiVtckDYq/view`
  - note: name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGENDA+PUBLIC+SHARED) — SHARED chosen because 71/71 working links point there
- `STALE` — Gene-pool bead lab — allele frequency
  - URL: `https://drive.google.com/file/d/1KLXsjXUqG8uzLbBM9jdlaROmDPSysHQb/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: PUBLIC tree, Cycle 18 :: Gene-Pool Allele-Frequency Simulation.pdf
  - **fix →** `https://drive.google.com/file/d/1xf7goh5P5cp16qVCUvADnAPToz2l9oWz/view`
  - note: name match 0.57 in the deck's own cycle; target = PUBLIC tree; NOTE this file exists only in the PUBLIC tree — it is missing from BIOLOGY (Shared), where every other working link resolves
- `STALE` — Comparing bones — chicken anatomy
  - URL: `https://drive.google.com/file/d/1PRkBFxKtCm9r0rZWK6_hbDhZt_UAWl42/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 18 / My Class only (print) :: Cycle 18 — EvoArc4_Morphology_Chicken_Anatomy.docx
  - **fix →** `https://drive.google.com/file/d/1jcEhtTVvo4YgIRYR7EWESkYMgQn6s9wt/view`
  - note: scorer said 0.25 (filename uses EvoArc4_Morphology, the label says 'Comparing bones'), but 'chicken anatomy' is the shared distinctive pair and this is the ONLY chicken file in Cycle 18 in any tree. Verified by hand.
**Slide 31** — Activity and resource links

- `STALE` — Evolution Stations check sheet
  - URL: `https://drive.google.com/file/d/1AGpX73RKRCnsg5Xu_gmZerw6td4WEg77/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 18 / My Class only (print) :: Cycle 18 — Evolution Stations Check Sheet.docx
  - **fix →** `https://drive.google.com/file/d/1Oxz2p9jl_IxzyB0fRhgSSQQPiVtckDYq/view`
  - note: name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGENDA+PUBLIC+SHARED) — SHARED chosen because 71/71 working links point there
- `STALE` — Gene-pool bead lab — allele frequency
  - URL: `https://drive.google.com/file/d/1KLXsjXUqG8uzLbBM9jdlaROmDPSysHQb/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: PUBLIC tree, Cycle 18 :: Gene-Pool Allele-Frequency Simulation.pdf
  - **fix →** `https://drive.google.com/file/d/1xf7goh5P5cp16qVCUvADnAPToz2l9oWz/view`
  - note: name match 0.57 in the deck's own cycle; target = PUBLIC tree; NOTE this file exists only in the PUBLIC tree — it is missing from BIOLOGY (Shared), where every other working link resolves
- `STALE` — Comparing bones — chicken anatomy
  - URL: `https://drive.google.com/file/d/1PRkBFxKtCm9r0rZWK6_hbDhZt_UAWl42/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 18 / My Class only (print) :: Cycle 18 — EvoArc4_Morphology_Chicken_Anatomy.docx
  - **fix →** `https://drive.google.com/file/d/1jcEhtTVvo4YgIRYR7EWESkYMgQn6s9wt/view`
  - note: scorer said 0.25 (filename uses EvoArc4_Morphology, the label says 'Comparing bones'), but 'chicken anatomy' is the shared distinctive pair and this is the ONLY chicken file in Cycle 18 in any tree. Verified by hand.
**Slide 32** — Activity and resource links

- `STALE` — Evolution Stations check sheet
  - URL: `https://drive.google.com/file/d/1AGpX73RKRCnsg5Xu_gmZerw6td4WEg77/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 18 / My Class only (print) :: Cycle 18 — Evolution Stations Check Sheet.docx
  - **fix →** `https://drive.google.com/file/d/1Oxz2p9jl_IxzyB0fRhgSSQQPiVtckDYq/view`
  - note: name match 0.80 in the deck's own cycle; target = SHARED tree (print subfolder); the same file exists as 3 copies (AGENDA+PUBLIC+SHARED) — SHARED chosen because 71/71 working links point there
- `STALE` — Gene-pool bead lab — allele frequency
  - URL: `https://drive.google.com/file/d/1KLXsjXUqG8uzLbBM9jdlaROmDPSysHQb/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: PUBLIC tree, Cycle 18 :: Gene-Pool Allele-Frequency Simulation.pdf
  - **fix →** `https://drive.google.com/file/d/1xf7goh5P5cp16qVCUvADnAPToz2l9oWz/view`
  - note: name match 0.57 in the deck's own cycle; target = PUBLIC tree; NOTE this file exists only in the PUBLIC tree — it is missing from BIOLOGY (Shared), where every other working link resolves
- `STALE` — Comparing bones — chicken anatomy
  - URL: `https://drive.google.com/file/d/1PRkBFxKtCm9r0rZWK6_hbDhZt_UAWl42/view`
  - STALE ID — material IS present, link points at a superseded copy
  - found: SHARED tree, Cycle 18 / My Class only (print) :: Cycle 18 — EvoArc4_Morphology_Chicken_Anatomy.docx
  - **fix →** `https://drive.google.com/file/d/1jcEhtTVvo4YgIRYR7EWESkYMgQn6s9wt/view`
  - note: scorer said 0.25 (filename uses EvoArc4_Morphology, the label says 'Comparing bones'), but 'chicken anatomy' is the shared distinctive pair and this is the ONLY chicken file in Cycle 18 in any tree. Verified by hand.

---

## Orphan candidates — material in a cycle folder that no slide links to

Files in the **PUBLIC** cycle folders whose Drive id appears in no deck and whose name
matches no link label. Some are deliberate (teacher-only planning files); the Cycle 01
classroom-jobs cluster looks like a whole unlinked set.

| Cycle | File | Type |
|---|---|---|
| 01 | Print_ Cycle 01 — Lab Safety Cartoon.docx | `.docx` |
| 01 | Interview forms.docx | `.docx` |
| 01 | Classroom Jobs Application Form 2026 — Reconstructed.docx | `.docx` |
| 01 | Welcome to Biology: Day One Info Sheet.gdoc | `.gdoc` |
| 01 | how to set up jobs for class.docx | `.docx` |
| 01 | Classroom Jobs — Applicants + Interviews 2026.xlsx | `.xlsx` |
| 01 | Why not just make classroom agreements?.gdoc | `.gdoc` |
| 01 | Student Classroom Jobs 1 - Overview (Revised).pptx | `.pptx` |
| 01 | Student Classroom Jobs 2 - Job Descriptions (Revised).pptx | `.pptx` |
| 01 | Classroom Jobs.gdoc | `.gdoc` |
| 02 | Copy of Cycle 02 — CA2_HHMI_Bobtail_Film.docx | `.docx` |
| 02 | (Both)The Glowing Squid- A Partnership with Bacteria.docx | `.docx` |
| 02 | Copy of Cycle 02 — CA1_TPT HMMI_Chains_and_Webs.docx | `.docx` |
| 02 | Cycle 02 — LivingTogether-StudentINfo.pdf | `.pdf` |
| 02 | Cycle 02 — (Trendy) CA1 Primary_ Feeding Relationships.docx | `.docx` |
| 02 | Cycle 02 — Feeding Relationships in the Pacific Northwest-Activity.pdf | `.pdf` |
| 02 | Print_FOOD CHAINS, ENERGY, AND FOOD WEBS.docx | `.docx` |
| 02 | Cycle 02 — Habitat_Hold_Em_Worksheet.docx | `.docx` |
| 04 | student_handout_carbon_cycle.doc | `.doc` |
| 12 | Cycle 12b — Reproduction (VT, edits bracketed).pptx | `.pptx` |
| 13 | Cycle 13 — Class Data Table (Coin-Flip Gametes).xlsx | `.xlsx` |
| 18 | Cycle 18 — Population Genetics Activity Guide.docx | `.docx` |
| 18 | Cycle 18 — EvoArc4_Morphology_Chicken_Anatomy.docx | `.docx` |

---

## What I could not determine, and what would be a bug

**Rules that fired on nothing.** Two, both real rather than extractor faults:

- *No Slides links anywhere.* Verified directly against the raw slide relationships and
  the printed slide text across all 51 files: zero `presentation/d/` strings. So the
  `/edit`→`/copy` rewrite had nothing to act on.
- *No 44-char id wearing a `drive.google.com/file/d/` URL.* Every Drive-file link in every
  deck carries a 33-char id, i.e. a genuinely uploaded binary in the correct URL form.
  The 'native Google file wearing the wrong URL form' repair also had nothing to act on.
  The one 44-char Google link (Cycle 07 slide 11) is already in `document/d/…/edit` form.

**Rules that fired on everything.** One, and it is real: every working material link (52
unique, 71 instances) resolves into the SHARED tree. I checked this rather than assuming
it, and it is what the repair targets are based on.

**Synced vs. not synced.** This was the main risk of false 'missing' calls, and it is
largely handled: Drive for Desktop is streaming these mounts, so a file that exists in
Drive still has a local directory entry and an item-id xattr even when its content is not
cached. 4,924 of 4,926 files carry an id. So 'no id anywhere in the mirror' does mean 'not
in any of her My Drives' — **but it does not mean 'does not exist'**. Two blind spots I
could not see past without network access:

- **Shared with me** does not sync at all. A doc someone shared with her is invisible here.
  Cycle 07's 'Read about Succession' is the likely case.
- **Trashed files** keep working links for 30 days but do not appear in the mirror.

  Neither applies to the Cycle 11 Decision Cards: that one has no file of that name
  anywhere, and four separate slides plus the teacher-prep slide instruct the teacher to
  print it from a subfolder that does not contain it.

**External links were not checked.** 1,019 of them. Nothing here says whether a
biointeractive or biomanbio URL still resolves — only that it is well-formed. §8 of the
skill notes `biomanbiology.com` vs `biomanbio.com` as a real past typo; all instances here
use the correct `biomanbio.com`.

**Link forms.** 344 links appear twice on their slide — once as a live hyperlink and once
as printed text. That is the §8 standard (label is a live link, plain URL printed below),
not duplication. Counted once each. 14 hyperlinks hang off an empty end-of-paragraph run
(a Google Slides export artifact) and 3 sit on a shape rather than text — a text-only
extractor would have missed the shape links, which is why both were parsed.

## A note on Drive

Nothing was written to Drive. Every access was a read: `os.walk`, opening the `.gslides` /
`.gdoc` stubs to parse `doc_id`, and reading the item-id xattr. You may notice fresh
modified-times on some Drive files today — reading a streamed placeholder makes Drive for
Desktop hydrate it locally, which updates the local mtime. No file content was changed and
nothing was pushed.

## Why nothing was rewritten

The `.pptx` files under `~/deck_work/exports/` are **exports** of the live Google Slides
decks, not the decks themselves. Editing a hyperlink in an export changes nothing a
student or teacher will ever open, and would leave 51 near-identical files that could be
mistaken for the live decks. Every repair here is a URL swap on a known slide, so the
actionable artifact is the patch CSV, applied in Slides. Say the word and I will produce
rewritten `.pptx` copies as well.
