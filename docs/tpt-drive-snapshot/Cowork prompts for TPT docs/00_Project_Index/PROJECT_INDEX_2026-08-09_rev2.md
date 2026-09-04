# PROJECT_INDEX — Answerable Biology Documentation Build

Purpose: the master index of every document in the build — what it is for, what it depends on, what it links to, what remains unresolved in it, and its review status.

## State of the build

First pass complete: 26 files across folders 01–18, built 2026-08-08 from the 27 extracted decks, Katherine's Unit Descriptions, and Answerable Teaching Chapters 5–6, QA-passed with fixes applied. All inline flags are preserved for review rather than resolved silently: across the doc set there are 803 raw flag occurrences — REVIEW WITH KATHERINE 214 · SOURCE NOT YET LOCATED 89 · RIGHTS REVIEW NEEDED 60 · WORKFLOW DEMONSTRATION NEEDED 48 · LINK NEEDED 231 · EXAMPLE NEEDED 30 · GAP 131. Counts are raw grep occurrences per label, so the audit documents (17_Source_Audit), whose job is to register flags, carry the largest numbers; the same underlying issue can appear in several documents. Everything Katherine must decide, locate, clear, or repair is consolidated in `REVIEW_REGISTER.md` in this folder. Every document is Draft — first build; all need teacher review; all dated 2026-08-08.

Amended 2026-08-09. Three documents were added to the index. Two were recovered from a superseded parallel build (`answerable_biology_build 2`, since deleted) and filed into the numbered folders: `Visual_Rights_and_Credits_Guide.md` into 17_Source_Audit and `How_to_Teach_a_VT_Cycle.md` into 03_Setup. The third, `Answerable_Biology_Teacher_Lesson_Planning.md`, was already sitting in 02_Year_Arc but had never been indexed. The set is now 29 indexed documents. The visual rights guide is the material addition: nothing else in the build covers image rights, and the 60 RIGHTS REVIEW NEEDED occurrences counted above concern activities, sims, labs, and links — not the photographs and diagrams inside the decks, which remain entirely unregistered.

**Authority note, 2026-08-09.** `RESUME_HERE.md` in this folder is the decision record and supersedes this index wherever the two disagree. It carries seven standing decisions Katherine made on 2026-08-08 and 2026-08-09. Both editor agents assigned to apply those decisions across the doc set died when the org monthly spend limit was reached, so every document below still describes the pre-decision state, and the flag counts above were taken before the decisions were made. Entries corrected against the decision record are marked *(decision applied)* — that marks the index as current, not the document it describes. Applying the decisions to the documents themselves is item 3 on the RESUME_HERE "Left to do" list and is not done.

Field key for the entries below — Purpose: one line. Dependencies: build documents it draws on. Status: all Draft — first build. Sources: corpus files used. Internal links: build documents it references. External links: count of http(s) URLs in the file. Unresolved: flag counts by label (RWK = REVIEW WITH KATHERINE, SNL = SOURCE NOT YET LOCATED, RRN = RIGHTS REVIEW NEEDED, WDN = WORKFLOW DEMONSTRATION NEEDED, LN = LINK NEEDED, EN = EXAMPLE NEEDED, GAP = GAP — NOT IN SOURCE NOTES). Teacher review needed: yes for every document (first build). Last revision: 2026-08-08 for every document.

---

## 00_Project_Index

### PROJECT_INDEX.md (this file)
- Purpose: master index of the build — every document's purpose, dependencies, links, and unresolved issues.
- Dependencies: every document below. Status: Draft — first build. Sources: the built doc set itself; BUILD_BRIEF.md. Internal links: all documents. External links: 0. Unresolved: none of its own (tracks all). Teacher review needed: yes. Last revision: 2026-08-09.

### REVIEW_REGISTER.md
- Purpose: the working-session register of everything Katherine must decide, locate, clear, repair, or confirm before publishing.
- Dependencies: TPT_Product_Architecture, ACTIVITY_SOURCE_AND_RIGHTS_AUDIT, ANSWERABLE_BIOLOGY_SOURCE_MAP, BROKEN_LINK_REPORT, Video_Setup_Plan, Year_Arc_20_Cycles, First_Week_Classroom_Conditions. Status: Draft — first build. Sources: consolidated flags across the doc set; Answerable_Biology_Unit_Descriptions.md. Internal links: the flagged documents. External links: 0. Teacher review needed: yes — it is the review. Last revision: 2026-08-08.
- Not yet reflected in it (2026-08-09): the Visual Source Register specified by Visual_Rights_and_Credits_Guide does not exist as a file. Per RESUME_HERE, two drafts also belong here and are unwritten — the Cycle 01 paid listing (decision 4) and a bracketed suggested included-list sentence for the Cycle 15 listing (decision 6). §a should shed the items decisions 2 and 5 have now settled. Katherine's `Answerable_Biology_Unit_Descriptions.md` is never edited directly; drafts go here for approval.

## 01_Start_Here

### Start_Here_How_Answerable_Biology_Works.md
- Purpose: the ten-minute introduction — what the curriculum is organized around, what each part of a lesson is for, where to go next.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- Status: Draft — first build.
- Sources: Answerable Teaching Ch. 5 and Ch. 6; Answerable_Biology_Unit_Descriptions.md; deck extracts via the Source Map (Cycle 02, Classifying Organisms, Cycles 03/06/10).
- Internal links: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: SNL 1.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 02_Year_Arc

### Year_Arc_20_Cycles.md
- Purpose: the full year cycle by cycle — what each cycle asks, what students do and revise, what the teacher needs.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- Status: Draft — first build.
- Sources: Source Map; Teaching Reasoning Extraction; Answerable_Biology_Unit_Descriptions.md; BUILD_BRIEF.md.
- Internal links: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 73 (per-cycle resource links carried from the decks). *(decision applied)* The tank-model URLs it inherits are no longer dead — see BROKEN_LINK_REPORT. This document still carries the 404 framing and needs it replaced.
- Unresolved: RWK 13 · SNL 12 · RRN 3 · LN 20 · EN 2 · GAP 5.
- Teacher review needed: yes. Last revision: 2026-08-08.

### Answerable_Biology_Teacher_Lesson_Planning.md
- Purpose: Katherine's own working notes on how the year is grouped and paced — the cycle system, the rule distinguishing a core deck from additional decks, and the cycle-by-cycle topic and deck map.
- Dependencies: none. This is an author source document, not built from the doc set. Year_Arc_20_Cycles and Master_Agenda should be read against it, since it is the pacing authority behind them.
- Status: Author source — supplied 2026-08-08, not build-drafted. Carries a © 2026 Katherine von Duyke line.
- Sources: written by Katherine and supplied in chat, 2026-08-08.
- Internal links: none.
- External links: 0.
- Unresolved: no inline flags. *(decision applied)* Two of its statements are settled by the decision record rather than open. It lists Cycle 15 as Genes & Chromosomes, and decision 6 confirms Protein Synthesis as the Cycle 15 EXTEND deck shipping inside the Genes & Chromosomes listing rather than as a separate one — so the two are not in conflict, and the "possible missing 20th listing" speculation elsewhere in the build should be removed. It records Cycle 1 as not yet in the deck set; `Cycle 01 — Lab Safety (VT deck)` exists, and decision 4 gives Cycle 01 its own paid listing, the twentieth, to be drafted into REVIEW_REGISTER in the voice and structure of the existing nineteen. Its record of Cycle 12a as The Process of Meiosis matches the deck recovered on 2026-08-09.
- Carries one product rule recorded nowhere else in the build: cycle terminology is teacher-facing and does not go on the TPT product listings. This bears on TPT_Sales_Copy_and_Preview_Plan and TPT_Product_Architecture.
- Teacher review needed: no — it is hers. Last revision: 2026-08-08. Indexed 2026-08-09.

### Master_Agenda.md
- Purpose: the year's operating page — every deck, material, activity, fiddle, and challenge by cycle; kept open during class.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, Year_Arc_20_Cycles, TEACHING_REASONING_EXTRACTION.
- Status: Draft — first build.
- Sources: Source Map; Year Arc; Teaching Reasoning Extraction; Answerable_Biology_Unit_Descriptions.md; BUILD_BRIEF.md.
- Internal links: Start_Here, Year_Arc_20_Cycles, Ecology_Unit_Guide, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 1 (most agenda rows intentionally carry LINK NEEDED placeholders until canonical URLs are pasted in).
- Unresolved: RWK 11 · SNL 10 · RRN 4 · LN 40 · EN 2 · GAP 4. The 40 LINK NEEDED entries are the paste-back targets for the repaired link inventory.
- Teacher review needed: yes. Last revision: 2026-08-08.

### Schedule_Options.md
- Purpose: three worked examples of the 20 cycles on real bell schedules (alternating block, daily 90-minute, 45-minute periods) — examples, not a pacing guide.
- Dependencies: Year_Arc_20_Cycles, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; Source Map (Cycle 02 blocks/dates evidence); Teaching Reasoning Extraction; Year Arc.
- Internal links: Year_Arc_20_Cycles, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: SNL 1.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 03_Setup

### Set_Up_Answerable_Biology.md
- Purpose: technical onboarding — what to open, decide, configure, and test, in order, to begin Cycle 1 without rebuilding the curriculum.
- Dependencies: Year_Arc_20_Cycles, Master_Agenda, Schedule_Options, Start_Here, Unit_Agenda_Template, Assessment doc, AI_Feedback doc, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; Source Map (Schoology placeholders, supplies, submit-to-folder checklists); Teaching Reasoning Extraction.
- Internal links: nine build docs (see Dependencies).
- External links: 0.
- Unresolved: RWK 2 · SNL 1 · WDN 5 · LN 1 · GAP 2. The five WDN flags resolve to Videos 1, 3, 9, 10–14, 18 (Video Setup Plan coverage table). *(decision applied)* Under decision 2 the free-unit step list can now honestly include the AI feedback step; not yet written in.
- Teacher review needed: yes. Last revision: 2026-08-08.

### How_to_Teach_a_VT_Cycle.md
- Purpose: the day-by-day procedural walkthrough of one Variation Theory cycle — what to read and locate before teaching, then Day 1 (establish the whole, get a first answer), Day 2 (manipulate the idea, deliver the pattern-break), and Day 3 (return, feedback, revise) — plus four teacher moves sorted by what a stuck student actually has, and a what-not-to-do list.
- Dependencies: Answerable_Biology_Teacher_Lesson_Planning (cycle length and the core-deck rule), BUILD_BRIEF.
- Status: Draft — recovered 2026-08-09 from the superseded parallel build and filed here. It is the only procedural, day-by-day walkthrough in the set; Start_Here explains what the parts are for, this explains what to do with them.
- Sources: Answerable Biology Teacher Lesson Planning Notes supplied in chat 2026-08-08; ANSWERABLE BIOLOGY BUILD BRIEF; Answerable Teaching (final 7_10_26).
- Internal links: none as written. It overlaps Start_Here_How_Answerable_Biology_Works, Assessment_Completion_Copying_Proficiency, and AI_Feedback_and_Conceptual_Growth without citing any of them.
- External links: 0.
- Unresolved: the cross-references above are not yet inserted. Its statement of the AI feedback constraint — name one thing that is right in the student's own words, ask two questions, offer one distinction, do not write the revised answer — should be checked for agreement with the wording in AI_Feedback_and_Conceptual_Growth and in the formative-pipeline-v2 skill spec. Whether it ships in the free product or only in paid bundles was open (REVIEW_REGISTER §a). [Inference, not a stated decision: decision 2 names the free product as exactly five components and this document is not among them, which makes it paid-only by implication. Worth confirming rather than assuming — a teacher who cannot run a cycle has no use for the free unit.]
- Teacher review needed: yes. Last revision: 2026-08-08. Filed and indexed 2026-08-09.

## 04_Ecology

### Ecology_Unit_Guide.md
- Purpose: the complete teaching guide for the ecology arc, Cycles 01–07, with Cycle 02 (the free TPT unit) documented in full teaching depth.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION, ACTIVITY_SOURCE_AND_RIGHTS_AUDIT.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; Cycle 02 full extract; per-deck Source Map entries for Classifying Organisms and Cycles 03–07; Answerable Teaching Chs. 5–6 via the extraction.
- Internal links: ACTIVITY_SOURCE_AND_RIGHTS_AUDIT, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 18 (ecology-arc resources; includes the wrong-domain BioMan URL — see BROKEN_LINK_REPORT). *(decision applied)* The github.io tank models are recovered and served from Netlify; this document still describes them as dead. Decision 2 also adds a Free Unit Guide export note here.
- Unresolved: RWK 18 · SNL 3 · RRN 6 · LN 17 · EN 2 · GAP 6.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 05_First_Week

### First_Week_Classroom_Conditions.md
- Purpose: the classroom conditions that make the system work — names, seats, visible responsibilities, jobs — established during the first week while Cycle 01 runs.
- Dependencies: TEACHING_REASONING_EXTRACTION, ANSWERABLE_BIOLOGY_SOURCE_MAP.
- Status: Draft — first build. Largest build-drafted share in the set: the sources are silent on door routines, seating philosophy, task cards, new-student arrival, the jobs system, and the job application, so those sections expand Katherine's design direction and are each flagged in place.
- Sources: Answerable Teaching Ch. 5 (refusable-task passage, workmates stance, Jair passage) and Ch. 6; deck extracts (cup sort, lab-safety rules, closing checklists); the gap register; Katherine's relayed design direction.
- Internal links: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: RWK 7 · EN 1 · GAP 6. All artifacts here must be checked against her real ones (see REVIEW_REGISTER §f).
- Teacher review needed: yes — priority. Last revision: 2026-08-08.

## 06_Unit_Guides

### Unit_Agenda_Template.md
- Purpose: the reusable one-per-unit operating document — copy, fill from the deck's teacher-reference slide and the Year Arc, teach from it.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, Year_Arc_20_Cycles, TEACHING_REASONING_EXTRACTION.
- Status: Draft — first build. Note: the 19–20 filled Unit Agendas are not yet built (registered as a GAP in TPT_Product_Architecture §3.1) — a cross-cutting gate on every paid product.
- Sources: Source Map; Year Arc; Teaching Reasoning Extraction; Answerable_Biology_Unit_Descriptions.md; BUILD_BRIEF.md.
- Internal links: Year_Arc_20_Cycles, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 5.
- Unresolved: RWK 1 · SNL 1 · LN 4.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 07_Activities_Labs

### Activities_Models_and_Labs_Guide.md
- Purpose: what each activity type is for (matching/card, open activities, models, labs have different jobs), with real deck examples and a full activity catalog with rights status.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION, ACTIVITY_SOURCE_AND_RIGHTS_AUDIT, Year_Arc_20_Cycles, Ecology_Unit_Guide.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; deck extracts via the Source Map; Answerable Teaching Chs. 5–6 via the extraction.
- Internal links: Year_Arc_20_Cycles, Ecology_Unit_Guide, ACTIVITY_SOURCE_AND_RIGHTS_AUDIT, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 1 (catalog defers URLs to the audit and Master Agenda).
- Unresolved: RWK 12 · SNL 4 · RRN 4 · LN 6 · EN 3 · GAP 7.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 08_Fiddles_Extensions

### Fiddles_Extensions_and_YouTube.md
- Purpose: what Fiddles are and how to run them, plus three year-long catalogs — Fiddles by cycle (with no-tech alternatives), challenges/extensions by cycle, and a curated YouTube list with each video's reason.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION, ACTIVITY_SOURCE_AND_RIGHTS_AUDIT, Year_Arc_20_Cycles.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; the four audit/arc docs listed above.
- Internal links: Year_Arc_20_Cycles, ACTIVITY_SOURCE_AND_RIGHTS_AUDIT, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 54 (all 38 YouTube links verified live via oEmbed 2026-08-08; sims and games carried from decks).
- Unresolved: RWK 6 · SNL 2 · RRN 1 · LN 20 · GAP 1.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 09_Assessment_Proficiency

### Assessment_Completion_Copying_Proficiency.md
- Purpose: how grading works — completion vs. proficiency, why they are kept apart, what to do about copying, and gradebook setup either way a school requires.
- Dependencies: TEACHING_REASONING_EXTRACTION, ANSWERABLE_BIOLOGY_SOURCE_MAP.
- Status: Draft — first build.
- Sources: Answerable Teaching Chs. 5–6; deck extracts (Cycle 02 response slides, why-notes-are-due slides, Then-and-Now); Katherine's formative-pipeline-v2 skill spec (integrity gate, completion CSV, two-rail rule).
- Internal links: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: RWK 3 · GAP 3.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 10_AI_Feedback

### AI_Feedback_and_Conceptual_Growth.md
- Purpose: the AI feedback system — finished deck to targeted feedback, Conceptual Growth Report per student, class summary — and where human judgment sits, on purpose.
- Dependencies: TEACHING_REASONING_EXTRACTION, ANSWERABLE_BIOLOGY_SOURCE_MAP.
- Status: Draft — first build. *(decision applied)* Decision 2 settles this: the document **is included free**. The free Ecology product is five components — Cycle 02 deck, Free Unit Guide, Year Arc, Start Here, and this document — so a free-unit teacher can run the loop end to end, bellringer through Growth Report. Neither this document nor the product architecture says so yet.
- Sources: Answerable Teaching Ch. 6 (feedback register, three cautions, human gate, workload numbers) and Ch. 5; formative-pipeline-v2 skill spec (revision prompt verbatim, batch flow, report standards); Unit Descriptions; Cycle 02 response slides.
- Internal links: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: RWK 3 · WDN 2 · EN 1. WDN resolves to Video 12 (student AI run). Added 2026-08-09: check its statement of the feedback constraint against the one in How_to_Teach_a_VT_Cycle.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 11_Technology_LMS

### LMS_Platform_Implementation_Guide.md
- Purpose: wiring Answerable Biology into any LMS (Schoology, Google Classroom, Canvas, Moodle) so the deck-native submission pattern survives and links stay canonical.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION, Master_Agenda, Year_Arc_20_Cycles, Start_Here, Assessment doc, AI_Feedback doc.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; Source Map (Schoology placeholders, submit checklists); Teaching Reasoning Extraction (LMS setup §6).
- Internal links: seven build docs (see Dependencies).
- External links: 0.
- Unresolved: RWK 2 · WDN 13 · GAP 3. The 13 WDN flags resolve to Videos 1, 2, 3, 9, 13, 17, 27, 28.
- Teacher review needed: yes. Last revision: 2026-08-08.

### Claude_LMS_Gradebook_Workflow.md
- Purpose: Katherine's working process — how she uses Claude (desktop app + Chrome extension) to wire each cycle's assignments into Schoology and the gradebook, and what she personally verifies.
- Dependencies: Set_Up_Answerable_Biology, AI_Feedback doc, Assessment doc, Year_Arc_20_Cycles, Unit_Agenda_Template, TEACHING_REASONING_EXTRACTION, ANSWERABLE_BIOLOGY_SOURCE_MAP.
- Status: Draft — first build. Highest WDN density in the set — this document is largely the script for the Tier 2–3 videos.
- Sources: Answerable Teaching Ch. 6; formative-pipeline-v2 skill spec; deck teacher-slide Schoology patterns; Ch. 5.
- Internal links: seven build docs (see Dependencies).
- External links: 0.
- Unresolved: WDN 17 · GAP 2. The 17 WDN flags resolve to Videos 1, 2, 3, 10, 17, 19, 20, 22, 24.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 12_Classroom_Technology

### Classroom_Technology_for_Formative_Noticing.md
- Purpose: using the smartboard and screen systems (GoGuardian and similar) to extend noticing of student thinking — and what to do when devices aren't there.
- Dependencies: TEACHING_REASONING_EXTRACTION, ANSWERABLE_BIOLOGY_SOURCE_MAP, Year_Arc_20_Cycles, LMS_Platform_Implementation_Guide.
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md (design rules 12, 14, 15); Answerable Teaching Chs. 5–6 via the extraction; Cycle 02 per-deck entry.
- Internal links: Year_Arc_20_Cycles, LMS_Platform_Implementation_Guide, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: RWK 1 · GAP 3 (the sources are thin on GoGuardian specifics; the gaps are marked, not invented over).
- Teacher review needed: yes. Last revision: 2026-08-08.

## 13_Supplies

### Master_Supply_System.xlsx / Master_Supply_System.csv (the supply workbook)
- Purpose: one editable master supply list producing every quarter checklist, the year shopping view, and cost totals.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP ("Supplies implied" fields), Ecology_Unit_Guide, Year_Arc_20_Cycles.
- Status: Draft — first build. *(decision applied)* Decision 5 confirms the quarter mapping — Q1 = Cycles 01–05, Q2 = 06–10, Q3 = 11–15, Q4 = 16–20 — so it is no longer an assumption. Cycle 02 is the free unit and also sits inside Q1, and Cycle 01 is part of the Q1 bundle, so Q1 buyers receive Cycles 01, 03, 04, 05 plus infrastructure and do not pay twice for Cycle 02. The assumption flags still stand in the README and in the xlsx and need removing (openpyxl, keep formulas, regenerate the CSV from MASTER, verify it reopens).
- Sources: Source Map; Ecology Unit Guide; Year Arc; Unit Descriptions (Pop Bead Meiosis lab); BUILD_BRIEF.md.
- Internal links: none (data file); the README is its documentation.
- External links: 41 rows carry LINK NEEDED instead of URLs (in the csv; xlsx mirrors it).
- Unresolved (csv): RWK 2 · SNL 9 · RRN 1 · LN 41 · GAP 3, as counted 2026-08-08. *(decision applied)* The 9 SNL rows no longer stand. The Cycle 12 CORE deck, The Process of Meiosis, 28 slides, was recovered from Katherine's Google Slides (Drive id `1pN08QqPJbhP6T8QbCKNjfQOS3JmQrLq60GeH1oCkktE`), exported to pptx, added to the Desktop folder, and propagated through the Source Map, Year Arc, Master Agenda, Standards, Supply System, Setup, TPT Architecture, Project Index, and Review Register. It is not SOURCE NOT YET LOCATED anywhere. Only the unlocated handouts remain.
- Teacher review needed: yes. Last revision: 2026-08-08.

### Supply_System_README.md
- Purpose: how the Master Supply System works and how to maintain it in one place.
- Dependencies: the workbook above; ANSWERABLE_BIOLOGY_SOURCE_MAP, Ecology_Unit_Guide, Year_Arc_20_Cycles.
- Status: Draft — first build.
- Sources: same as the workbook.
- Internal links: Master_Supply_System, Year_Arc_20_Cycles, Ecology_Unit_Guide, ANSWERABLE_BIOLOGY_SOURCE_MAP.
- External links: 0.
- Unresolved: RWK 4 · SNL 2 · RRN 1 · LN 1 · GAP 1.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 14_Standards_Alignment

### Standards_and_Alignment.md
- Purpose: complete NGSS documentation — PEs mapped to every unit and cycle, DCIs/SEPs/CCCs, assessment evidence locations, and a section for administrators and observers.
- Dependencies: ANSWERABLE_BIOLOGY_SOURCE_MAP (per-deck NGSS PE fields), TEACHING_REASONING_EXTRACTION, Year_Arc_20_Cycles.
- Status: Draft — first build. RWK count is high because several legacy decks carry no NGSS block, so PE assignments there are build-inferred and flagged.
- Sources: Source Map; Teaching Reasoning Extraction; Year Arc; BUILD_BRIEF.md; published NGSS HS Life Science structure.
- Internal links: Year_Arc_20_Cycles, ANSWERABLE_BIOLOGY_SOURCE_MAP, TEACHING_REASONING_EXTRACTION.
- External links: 0.
- Unresolved: RWK 19 · SNL 5 · EN 1 · GAP 3.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 15_TPT_Product_System

### TPT_Product_Architecture.md
- Purpose: the selling structure — what each product contains file by file; how the free unit, 19 units, four quarter bundles, and year bundle relate; which rights verdicts gate what.
- Dependencies: ACTIVITY_SOURCE_AND_RIGHTS_AUDIT (all packaging verdicts), ANSWERABLE_BIOLOGY_SOURCE_MAP, and nearly every teacher-facing doc (they are its shipped contents).
- Status: Draft — first build. Carries the §10 open-decisions roll-up that seeds REVIEW_REGISTER §a.
- Sources: BUILD_BRIEF.md; Unit Descriptions (the 19 listings); the audit trio; deck filename inventory.
- Internal links: 22 build documents — the widest-linking document in the set.
- External links: 1.
- Unresolved: RWK 22 · SNL 6 · RRN 14 · LN 3 · EN 2 · GAP 2, as counted 2026-08-08. *(decision applied)* Five decisions land in this document and none are written in yet: decision 2 (the five-component free product — §2 and the §7 matrix), decision 4 (Cycle 01 gets its own paid listing, a twentieth), decision 5 (quarter mapping confirmed), decision 6 (no separate Protein Synthesis listing; remove the "possible missing 20th listing" speculation), and decision 3 (the rights gate on the four inherited-content decks becomes "ships once the cleaned copy is approved" rather than RIGHTS REVIEW NEEDED with no path). Separately, its rights gating covers activities and linked resources only; deck visuals are gated by Visual_Rights_and_Credits_Guide, which is not yet cited here.
- Teacher review needed: yes — priority (every open product decision lives here). Last revision: 2026-08-08.

## 16_TPT_Sales_Materials

### TPT_Sales_Copy_and_Preview_Plan.md
- Purpose: the sales layer — storefront copy, free-product listing, paid-listing template in Katherine's voice, and a preview-PDF plan per product, organized around real teacher complaints.
- Dependencies: TPT_Product_Architecture (structure), Unit Descriptions (voice), Ecology_Unit_Guide, AI_Feedback doc, Year_Arc_20_Cycles, and the docs it previews.
- Status: Draft — first build. EN count is the highest in the set: preview screenshots and worked examples wait on final decks and live models.
- Sources: BUILD_BRIEF.md; Unit Descriptions; Source Map; Teaching Reasoning Extraction; twelve build docs.
- Internal links: 12 build documents.
- External links: 0.
- Unresolved: RWK 7 · SNL 3 · RRN 1 · WDN 4 · EN 10. *(decision applied)* Decision 2 rewrites §3 and the free listing to the five-component free product; decision 4 adds a twentieth paid listing for Cycle 01. Also check the copy against the rule in Answerable_Biology_Teacher_Lesson_Planning that cycle terminology stays teacher-facing and does not appear on the listings.
- Teacher review needed: yes. Last revision: 2026-08-08.

## 17_Source_Audit

### ANSWERABLE_BIOLOGY_SOURCE_MAP.md
- Purpose: canonical inventory of every source deck — placement, verbatim contents, anomalies, and the consolidated flag registers every other document cites.
- Dependencies: none (it is the root of the dependency tree).
- Status: Draft — first build.
- Sources: BUILD_BRIEF.md; the three source_map work parts; all 27 deck extracts; Unit Descriptions.
- Internal links: none outward (everything links to it).
- External links: 175 (it logs every deck link).
- Unresolved: RWK 49 · SNL 25 · RRN 11 · WDN 1 · LN 36 · EN 6 · GAP 58 — the registers, not new issues; most downstream flags cite these.
- Teacher review needed: yes. Last revision: 2026-08-08.

### ACTIVITY_SOURCE_AND_RIGHTS_AUDIT.md
- Purpose: one entry per activity/sim/lab/video/resource across all 27 decks, with source, rights status, and TPT packaging verdict (INCLUDE FILE / LINK ONLY / RIGHTS REVIEW NEEDED).
- Dependencies: BROKEN_LINK_REPORT (reachability), _all_links.json, deck extracts.
- Status: Draft — first build; live license checks run 2026-08-08.
- Sources: _all_links.json; all 27 extracts; live HTTP and license-page fetches.
- Internal links: BROKEN_LINK_REPORT.
- External links: 92.
- Unresolved: RWK 17 · SNL 2 · RRN 14 · LN 34. Scope note added 2026-08-09: this audit covers activities, sims, labs, videos, and linked resources. It does not cover photographs, diagrams, or other visuals placed inside the decks — those are governed by Visual_Rights_and_Credits_Guide below and are not yet audited at all.
- *(decision applied)* Decision 3 changes the verdict on the four decks carrying inherited third-party content: the gate becomes "ships once the cleaned copy is approved," not RIGHTS REVIEW NEEDED with no path. Originals are never modified; cleaned copies are `(v3 cleaned)` with a slide-by-slide change manifest. Three are done — Cycle 12 Reproduction & Meiosis (28 of 47 slides rebuilt, 97 third-party images removed, 16 replacement diagrams drawn, 15.7 MB to 1.3 MB), Cycle 12 The Process of Meiosis (20 of 28 slides rebuilt), and Cycle 16 Stem Cell Differentiation (26 slides, clean, **but its change manifest was never written** — regenerate by diffing v2 against v3). Cycle 13 Genetics Continued / Punnett, 86 slides, is not started.
- Teacher review needed: yes — priority (all of REVIEW_REGISTER §c cites it). Last revision: 2026-08-08.

### Visual_Rights_and_Credits_Guide.md
- Purpose: the rights standard governing the photographs, diagrams, and scientific visuals placed inside the decks — when a visual earns its place instructionally, which licenses are permissible in a product sold commercially, which repositories to draw from, and the per-visual record to keep.
- Dependencies: none as written. It is the visual-side counterpart to ACTIVITY_SOURCE_AND_RIGHTS_AUDIT and gates the same TPT packaging decisions as TPT_Product_Architecture.
- Status: Draft — recovered 2026-08-09 from the superseded parallel build and filed here. It fills a gap the first build did not cover: no other document in the set addresses image rights.
- Sources: ANSWERABLE BIOLOGY BUILD BRIEF; Answerable_Biology_Visual_Source_Standard_and_Cowork_Prompt.docx.
- Internal links: none as written; it should cite ACTIVITY_SOURCE_AND_RIGHTS_AUDIT and TPT_Product_Architecture.
- External links: 0 (repositories are named, not linked).
- Rules it sets, which govern every deck visual: no CC BY-NC in a product sold on TPT; no ND material where the visual will be cropped, labeled, or otherwise altered; ShareAlike flagged RIGHTS REVIEW NEEDED unless a downstream licensing plan is clear; "free online," "free for teachers," and "open access" are not commercial-redistribution permission; Google Images may help locate a source but is never the source record; OpenStax by manual exception only, because its licensing and generative-AI ingestion terms need separate attention.
- Preferred repositories, each with an item-level caveat: Smithsonian Open Access (CC0-marked items only), NOAA, USGS, CDC PHIL, NCI Visuals Online, Wikimedia Commons, NLM.
- Unresolved: the Visual Source Register it specifies — eighteen fields per placed visual, from critical aspect served through license, modification permitted, attribution text, and date verified — does not yet exist as a file. Until it does, every visual already sitting in the 27 decks is RIGHTS REVIEW NEEDED by this document's own rule, and none of them are counted in the 60 RRN occurrences recorded above. This is not yet entered in REVIEW_REGISTER.
- Teacher review needed: yes. Last revision: 2026-08-08. Filed and indexed 2026-08-09.

### BROKEN_LINK_REPORT.md
- Purpose: every URL across the 27 decks with live HTTP status (checked 2026-08-08), plus the LINK NEEDED list for activities named with no URL.
- Dependencies: _all_links.json, deck extracts.
- Status: Draft — first build.
- Sources: _all_links.json; all 27 extracts; live checks (38 YouTube links verified via oEmbed).
- Internal links: none.
- External links: 104 (that is the report).
- Unresolved: RWK 2 · SNL 2 · LN 8, as checked 2026-08-08. *(decision applied)* The headline finding is obsolete. The nine github.io tank models were not lost: the repo `github.com/Answerable-Teaching/tank-and-flow-models` was found intact and self-contained, GitHub Pages was abandoned after four builds failed on GitHub's own side, and serving moved to Netlify — all eleven pages verified HTTP 200 at `answerable-biology-models.netlify.app`. Ten decks were relinked (Cycles 03, 04, 05, 06, 09, 10, 11, 18, 19, 20); Cycle 02 was left alone because its energy model already points at a working address. Canonical masters live in the Drive folder "Answerable Biology — Interactive Models." Still true: biomanbiology.com does not resolve, and seven resources moved or retired. This document should carry one LINK NEEDED note, not nine alarm flags.
- Teacher review needed: yes — priority (drives REVIEW_REGISTER §d). Last revision: 2026-08-08.

### TEACHING_REASONING_EXTRACTION.md
- Purpose: the quarry file — Katherine's own teaching reasoning, verbatim where strong, by topic, with every unsupported topic marked GAP rather than invented.
- Dependencies: none (root document).
- Status: Draft — first build.
- Sources: Answerable Teaching Chs. 5–6; Unit Descriptions; all 27 deck extracts (teacher-voice slides cited individually).
- Internal links: none outward.
- External links: 2.
- Unresolved: RWK 8 · GAP 21 (the honest register of what the corpus does not say — first week, jobs, GoGuardian, gradebook mechanics).
- Teacher review needed: yes. Last revision: 2026-08-08.

## 18_Video_Plan

### Video_Setup_Plan.md
- Purpose: the complete list of short screen recordings to make — 28 videos in five priority tiers, one operation each, with exact link-back targets in the documentation.
- Dependencies: every document carrying a WORKFLOW DEMONSTRATION NEEDED flag (Set Up, AI Feedback, Claude LMS Workflow, LMS Platform Guide) plus Master_Agenda, Year_Arc, Classroom_Technology.
- Status: Draft — first build. Its flag-coverage table maps all 48 WDN occurrences to videos; recording a video closes every flag that shares its operation.
- Sources: BUILD_BRIEF.md; the nine build docs listed in its Sources used line.
- Internal links: nine build documents.
- External links: 0.
- Unresolved: RWK 5 · WDN 6 · GAP 1.
- Teacher review needed: yes — the recordings themselves are hers to make (REVIEW_REGISTER §g). Last revision: 2026-08-08.

---

Sources used: every file under /root/ab_build/output/ (26 files, inventoried 2026-08-08); flag counts by raw grep per label; /root/ab_build/BUILD_BRIEF.md. Amended 2026-08-09 from three documents read in full: Answerable_Biology_Teacher_Lesson_Planning.md (already in 02_Year_Arc, previously unindexed), and Visual_Rights_and_Credits_Guide.md and How_to_Teach_a_VT_Cycle.md, both recovered from the superseded `answerable_biology_build 2` folder and filed into 17_Source_Audit and 03_Setup respectively. Deck-existence checks in this amendment come from a title search of the live Google Drive deck folders, 2026-08-09. Corrected later the same day against `00_Project_Index/RESUME_HERE.md`, which is the decision record and takes precedence over this file: entries marked *(decision applied)* record a decision that is settled but not yet written into the document being described. Nothing has been published to TPT; all go/no-go gates stand.
