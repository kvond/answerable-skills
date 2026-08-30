# TPT listing spec — handoff for Claude Code

Everything needed to create six TPT listings. Self-contained: no prior conversation required.

**Prerequisite.** This is entirely browser work. Claude-in-Chrome MCP must be connected, and Chrome must be signed in to the TPT account. If it isn't, stop and say so — there is nothing here that can be done without it.

**Store:** https://www.teacherspayteachers.com/store/answerable-teaching

---

## Read this before starting — three things learned the hard way

**1. Do NOT use the "Google Drive" product type.** Its file picker will not open from browser automation. It failed silently across six attempts, two tabs and three page loads — the page scrolls to the Files section and nothing happens, with no console error. The picker also only lists My Drive, and it rejects folders containing subfolders and any `.docx`/`.pptx`.

**Use "Digital Download" instead** and upload the one-sheet PDF. That is an ordinary `<input type=file>`, which automation handles fine. Locate it with `read_page` or `find`, then use the `file_upload` tool with the element ref — **never click a file input**, that opens a native dialog you cannot see or control.

**2. Never trigger a JavaScript dialog.** A modal blocks all further extension commands and the session has to be rescued by hand.

**3. Verify every field after entry.** TPT's form silently drops values when a select is set too fast after a page mutation. Re-read the form before submitting.

---

## The product, in one paragraph

Answerable Biology is a full-year high school biology curriculum. Each lesson is a Google Slides deck that is simultaneously the lesson and the worksheet: students open their own copy and write on the slides while being taught. They write a first answer during instruction, then revise it between classes using a prompt in the speaker notes that makes an AI question them rather than answer for them. Both answers stay visible. Grading is completion, not correctness. The pedagogy is Variation Theory — each lesson turns on one *critical aspect*, the single discernment a concept depends on, worked through five questions.

The deliverable a buyer downloads is a **one-page PDF** containing live links to a Google Drive folder holding everything. All folders and files are already shared "Anyone with the link — Viewer" and verified working from a signed-out browser.

---

## Fields identical across all six listings

| Field | Value |
|---|---|
| Product type | **Digital Download** |
| File to upload | the unit's one-sheet PDF (see each listing) |
| Tax Code | **Other digital goods** |
| Grade Level | **9th Grade**, **10th Grade** |
| Subject Area | **Science → Biology** |
| Teaching Duration | **2 Days** |
| Answer Key | **N/A — Does not apply** |
| Number of Pages or Slides | per listing — see table below |
| Make Listing Active | **UNCHECKED** — every listing saves as a draft |

**Make Listing Active: TICK IT.** All six go live. Note that TPT activates a Free Resource
regardless of this checkbox, so a free listing cannot be saved as a draft.

### Number of Pages or Slides

Counted from the canonical `.pptx` cycle decks on 20 Aug 2026. This is the number of
student-facing lesson slides in the unit, not the page count of the one-sheet PDF.

| Listing | Cycles counted | Slides |
|---|---|---|
| Ecology Starter (FREE) | 02 (35), 03 (32) | **67** |
| The Cell as a System | 08, 09, 10, 11 | **134** |
| From Sunlight to Populations | 01 (24), 04, 05, 06, 07a, 07b | **179** |
| Inheritance & Information | 12, 13a, 14, 15a, 15b, 16a–16d | **290** |
| Change Over Time | 17, 18, 19, 20 | **123** |
| Full Year Bundle | all twenty | **793** |

Inheritance uses `Cycle 12 — The Process of Meiosis (VT deck, rebuilt).pptx` (31 slides).
The other Cycle 12 file in that folder, `Cycle 12 — Reproduction & Meiosis.pptx`
(33 slides), would make the total 292. Confirm before publishing.

Cycles 01 and 02 exist only as Google Slides; every other cycle was counted from `.pptx`.

### The standing block — append to EVERY description

Every listing's description ends with the same block. It is held in a separate file so it
is edited once:

`My Drive/Teacher Pay Teachers/CLAUDE SKILL FILES/TPT_PROMISES_BLOCK.md`

Read that file and paste its fenced block verbatim below the unit-specific copy in all six
descriptions. Do not paraphrase it and do not vary it between listings.

---

## Custom categories — create these first

TPT custom categories are made once in the seller dashboard and then assigned per listing.

1. Start Here — Free Samples
2. Biology — Full Year & Bundles
3. Biology — Cells & Energy
4. Biology — Genetics & Evolution
5. Forensics
6. Anatomy & Physiology
7. How These Lessons Work

Categories 5 and 6 will be empty for now; they exist so the store structure is right as those courses arrive.

---

## A note on the Tag field

TPT's "Tag (Theme, Audience, Language)" field is a **fixed vocabulary**, not free text. It maps to search filter checkboxes and is a holiday/audience calendar — Earth Day, Back to school, Homeschool, En español. There is **no** tag for NGSS, Google Slides, or formative assessment. Do not invent tags; pick only from the dropdown. If a tag named below is unavailable, skip it rather than substituting.

---

# LISTING 1 — Ecology Starter (FREE)

**Upload:** `eco4.pdf`
**Price:** tick **Free Resource**
**Custom category:** Start Here — Free Samples
**Tags:** Homeschool · Back to school
**NGSS:** HS-LS2-3, HS-LS2-4, HS-LS2-6

**Title**
```
Ecology FREE Lesson Set | Food Webs & Energy Pyramids | High School Biology
```

**Description**
```
Two complete ecology lessons for high school biology, built as Google Slides decks that are the lesson and the worksheet at the same time. Students write directly on the slides while you teach, then revise their own answers before the work is handed in. Free, complete, and structured exactly like the paid units, so you can run the method before you buy it.

WHAT YOU GET
• Cycle 02 — Ecosystems and Feeding Relationships
• Cycle 03 — Energy Flow and Trophic Pyramids
• A ten-slide teacher setup file. Everything needed to run the set is in that one file.
• A ROSTER & SCORES sheet with a column for every lesson, formatted so most gradebooks import it directly
• The revision prompts, in the speaker notes of the slides students write on
• A complete worked example: five students, their decks, their Growth Reports, the class summary
• The full Teacher Manual, the method in one page, and the Ten Questions guide

HOW ONE LESSON RUNS
Two class meetings on a ninety-minute block. You teach, and students write a first answer in their own words while the lesson is happening. You collect that copy, which is the formative score. Between classes students open the speaker notes on their response slides and paste the prompt into any AI, which asks them questions rather than answering for them. They write a revised answer underneath, and the first answer stays visible. You collect the whole assignment, which is the quiz score.

WHY STUDENTS ANSWER DURING THE LESSON
The first answer is where a misconception becomes visible, which gives the rest of the lesson something to work on. A confidently wrong first answer is doing its job. Grade that answer for accuracy and students write what they think is safe instead of what they actually think.

GRADING
Completion, not correctness. Both boxes filled in the student's own words earns full credit, and the check takes about twenty seconds per student. Proficiency is real, and it belongs in the feedback you give rather than in the gradebook.

WHAT YOU NEED
A device per student and a Google account. A projector for the bellringer simulations. Two printed pages per student across both cycles. No wet lab, no chemicals, no consumables beyond paper. The card sorts are draggable tiles inside the deck, so there is nothing to print and cut.

The worked example is fabricated throughout. Five invented students, invented answers. No real student work appears anywhere in this product.
```

---

# LISTING 2 — The Cell as a System

**Upload:** `cell.pdf`
**Price:** **$24.95**
**Custom category:** Biology — Cells & Energy
**Tags:** Homeschool
**NGSS:** HS-LS1-2, HS-LS1-3, HS-LS1-4, HS-LS1-6

**Title**
```
Cell Structure Transport & Enzymes Unit | High School Biology NGSS Slides
```

**Description**
```
Four complete lessons on cell structure, membrane transport, enzymes, and the cell cycle, built as Google Slides decks that serve as the lesson and the worksheet at once. Students write on the slides while you teach and revise their own answers before the work is scored. Built for a ninety-minute block.

WHAT YOU GET
• Cycle 08 — Cells and Organelles
• Cycle 09 — Cell Membrane and Transport
• Cycle 10 — Enzymes
• Cycle 11 — The Cell Cycle and Cancer
• A teacher setup file with the copy link for each lesson
• A ROSTER & SCORES sheet with a formative column and a revision column for every lesson
• Revision prompts in the speaker notes of every response slide
• A complete worked example showing what the feedback process produces
• The full Teacher Manual, the method in one page, and the Purchase & Prep one-sheet

HOW EVERY LESSON IS BUILT
Each lesson turns on one critical aspect, meaning the single discernment the concept depends on. Five questions work that discernment in order, so a contrast does the teaching rather than a definition. This is Variation Theory: students learn a concept by discerning what varies against what stays the same.

1. Critical aspect — an open question that puts the concept on the table before any explanation
2. Contrast set — two cases side by side that differ in exactly the one feature that matters
3. Build a rule — students put the pattern they just saw into their own words
4. Pattern break — a case that breaks their rule and forces them to sharpen it
5. Three-tier question — the same idea at Getting Started, Working On It and Mastery, so differentiation sits inside the question rather than beside it

GRADING
Completion, not correctness. Both answers present, in the student's own words, earns full credit.

STANDARDS
NGSS HS-LS1-2, HS-LS1-3, HS-LS1-6, and HS-LS1-4 in part — Cycle 11 covers the mitosis half of that expectation. Membrane transport has no performance expectation of its own; it sits inside disciplinary core idea LS1.A and feeds HS-LS1-3.

WHAT YOU NEED
A device per student and a Google account. A projector. These are the wet-lab cycles: goggles, clear cups and paper towels recur across all four, with a full item list in the supply sheet included in the folder.
```

---

# LISTING 3 — From Sunlight to Populations

**Upload:** `sun.pdf`
**Price:** **$24.95**
**Custom category:** Biology — Cells & Energy
**Tags:** Homeschool · Earth Day
**NGSS:** HS-LS1-5, HS-LS1-7, HS-LS2-1, HS-LS2-2, HS-LS2-3, HS-LS2-4, HS-LS2-5, HS-LS2-6

**Title**
```
Photosynthesis Respiration & Populations Unit | High School Biology NGSS
```

**Description**
```
Six complete lessons tracing energy from sunlight through photosynthesis and respiration into ecosystems and population dynamics. Each lesson is a Google Slides deck that is the lesson and the worksheet together. Students write while you teach, then revise their own answers before the work is scored.

WHAT YOU GET
• Cycle 01 — Course Launch and Lab Safety
• Cycle 04 — Cycles of Matter: The Carbon Cycle
• Cycle 05 — Photosynthesis
• Cycle 06 — Cellular Respiration and Fermentation
• Cycle 07a — Population Ecology
• Cycle 07b — Populations and Succession
• A teacher setup file with the copy link for each lesson
• A ROSTER & SCORES sheet with two columns per lesson
• Revision prompts in the speaker notes of every response slide
• A complete worked example showing what the feedback process produces
• The full Teacher Manual, the method in one page, and the Purchase & Prep one-sheet

HOW ONE LESSON RUNS
Two class meetings on a ninety-minute block. You teach and students write a first answer in their own words. You collect that copy, which is the formative score. Between classes students open the speaker notes and paste the prompt into any AI, which asks them questions rather than supplying an answer. They write a revised answer underneath and both answers stay visible. You collect the whole assignment, which is the quiz score.

STANDARDS
Eight NGSS performance expectations: HS-LS1-5, HS-LS1-7, HS-LS2-1, HS-LS2-2, HS-LS2-3, HS-LS2-4, HS-LS2-5, HS-LS2-6. Six of the eight are in HS-LS2. HS-LS2-2 asks students to support and revise explanations based on evidence, which is exactly what the two-answer structure produces on paper.

GRADING
Completion, not correctness. The first answer is where the misconception shows, so grading it for accuracy would teach students to hide what they think.

WHAT YOU NEED
A device per student and a Google account. A projector. The first wet lab is Cycle 05; Cycles 01, 04 and 07 need paper only. Full item list in the supply sheet included in the folder.
```

---

# LISTING 4 — Inheritance & Information

**Upload:** `inh.pdf`
**Price:** **$24.95**
**Custom category:** Biology — Genetics & Evolution
**Tags:** Homeschool
**NGSS:** HS-LS1-1, HS-LS1-4, HS-LS3-1, HS-LS3-2, HS-LS3-3

**Title**
```
DNA Protein Synthesis & Genetics Unit | High School Biology NGSS Slides
```

**Description**
```
Nine complete lessons from meiosis and Mendelian inheritance through DNA structure, protein synthesis, differentiation, mutation and biotechnology. Each lesson is a Google Slides deck that functions as the lesson and the worksheet at once. Students write while you teach, then revise their own answers using prompts that question rather than answer.

WHAT YOU GET
• Cycle 12 — The Process of Meiosis
• Cycle 13a — Mendelian Genetics
• Cycle 14 — DNA Structure and Replication
• Cycle 15a — Genes and Chromosomes
• Cycle 15b — Protein Synthesis and the Central Dogma
• Cycle 16a — Stem Cell Differentiation
• Cycle 16b — Mutations and Gene Expression
• Cycle 16c — Mutations and Genetic Disorders
• Cycle 16d — Biotechnology
• A teacher setup file with the copy link for each lesson
• A ROSTER & SCORES sheet with two columns per lesson
• Revision prompts in the speaker notes of every response slide
• A complete worked example showing what the feedback process produces
• The full Teacher Manual, the method in one page, and the Purchase & Prep one-sheet

WHY THE TWO ANSWERS MATTER HERE
Genetics is where students most often produce a fluent sentence they do not understand. Because the first answer is written during instruction and stays visible beside the revision, you can see whether the second answer is a real change in thinking or a copy of the slide. That distinction is invisible on a worksheet handed in once.

STANDARDS
NGSS HS-LS1-1, HS-LS3-1, HS-LS3-2, HS-LS3-3, and HS-LS1-4 in part — Cycle 16a covers the differentiation half of that expectation. All three HS-LS3 expectations are covered.

GRADING
Completion, not correctness. Both answers present, in the student's own words, earns full credit.

WHAT YOU NEED
A device per student and a Google account. A projector. Mostly paper: the only bought items across nine lessons are a DNA pop bead kit for the meiosis lab, for which paper clips substitute, and modeling clay for the tissue models. Full item list in the supply sheet included in the folder.
```

---

# LISTING 5 — Change Over Time

**Upload:** `cot.pdf`
**Price:** **$24.95**
**Custom category:** Biology — Genetics & Evolution
**Tags:** Homeschool · Earth Day
**NGSS:** HS-LS4-1, HS-LS4-2, HS-LS4-3, HS-LS4-4, HS-LS4-5

**Title**
```
Evolution Natural Selection & Speciation | High School Biology NGSS Slides
```

**Description**
```
Four complete lessons on the evidence for evolution, natural selection, speciation and human impact, ending in a capstone. Each lesson is a Google Slides deck that is the lesson and the worksheet together. Students write while you teach and revise their own answers before the work is scored.

WHAT YOU GET
• Cycle 17 — Darwin and the Evidence of Evolution
• Cycle 18 — Natural Selection and Adaptation
• Cycle 19 — Speciation and Biodiversity
• Cycle 20 — Human Impact, a capstone
• A teacher setup file with the copy link for each lesson
• A ROSTER & SCORES sheet with two columns per lesson
• Revision prompts in the speaker notes of every response slide
• A complete worked example showing what the feedback process produces
• The full Teacher Manual, the method in one page, and the Purchase & Prep one-sheet

STANDARDS
NGSS HS-LS4-1, HS-LS4-2, HS-LS4-3, HS-LS4-4 and HS-LS4-5 — five of the six performance expectations in HS-LS4, the strongest standards coverage in this course.

GRADING
Completion, not correctness. Both answers present, in the student's own words, earns full credit.

WHAT YOU NEED
A device per student and a Google account. A projector. No wet lab. Cycles 19 and 20 need nothing but paper. The bought items are craft beads for the allele lab and simple tools for the beak activity, both in Cycle 18. Full item list in the supply sheet included in the folder.
```

---

# LISTING 6 — Full Year Bundle

**Product type: TPT Bundle, not Digital Download.** Build it only after the five listings above exist — a Bundle can only be assembled from products already listed in the store. Select all five as components, and attach the year-level sheet as the Bundle's bonus file:

`My Drive/Teacher Pay Teachers/Teacher Facing Docs/Answerable Biology --Full Year Bundle/Answerable Biology — Full Year Bundle — one sheet.pdf`

**Price:** **$79.95** · **Custom category:** Biology — Full Year & Bundles · **Tags:** Homeschool · Back to school · End of year
**NGSS:** the union of all five units above — HS-LS1-1 through HS-LS1-7 except HS-LS1-4 in whole, HS-LS2-1 through HS-LS2-6, all of HS-LS3, and HS-LS4-1 through HS-LS4-5.

**Title**
```
Full Year High School Biology Curriculum | NGSS | Google Slides | 20 Cycles
```

---

## Procedure per listing

1. Go to https://www.teacherspayteachers.com/My-Products/New-Item
2. Choose **Digital Download**
3. Paste the Title
4. Paste the Description into the rich-text box
5. Upload the PDF via `file_upload` with the file input's element ref — do not click the input
6. Set Price, or tick Free Resource for listing 1
7. Set Tax Code to Other digital goods
8. Tick Grade Level 9th and 10th
9. Set Subject Area to Science → Biology
10. Add Tags from the dropdown only
11. Assign the Custom Category
12. Select the NGSS codes listed for that unit
13. Set Teaching Duration to 90 minutes
14. Set Answer Key to N/A
15. **Leave Make Listing Active unchecked**
16. Re-read the whole form and confirm every value took before clicking Submit
17. Submit, confirm the draft saved, and report the listing URL

## Report back

For each listing: the URL, and any field the form refused or silently dropped. If the same field fails twice, stop and ask rather than retrying a third time.
