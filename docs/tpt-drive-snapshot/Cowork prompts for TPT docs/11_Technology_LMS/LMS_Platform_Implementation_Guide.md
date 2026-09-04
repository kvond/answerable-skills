# LMS Platform Implementation Guide

Purpose: how to wire Answerable Biology into your LMS — Schoology, Google Classroom, Canvas, Moodle, or similar — so the deck-native submission pattern survives, links stay canonical, teacher materials stay private, and you never fight version chaos.

This guide assumes you have read Start Here and have the Master Agenda open. It does not assume your platform can do what another platform can. Section 1 is the pattern every platform must preserve; Section 2 is the rules that hold everywhere; Sections 3–7 are per-platform; Section 8 covers device and printing environments. Katherine teaches on Schoology, so the Schoology section is written from her actual practice; the other platforms are written from their documented capabilities, with anything unverified marked `WORKFLOW DEMONSTRATION NEEDED` rather than invented.

## 1. The pattern your LMS must preserve

Whatever platform you use, one workflow is non-negotiable, because everything downstream depends on it:

**Each student works in their own copy of the cycle's slide deck and submits the deck.** Notes are due before class ends — the standing policy slide says it to students directly: "The purpose of the notes is to help your brain process today's lesson while it is still fresh... For that reason, students who are present complete and submit their notes before leaving class." On Day 3 the student reopens their response slides, runs the AI revision prompt that lives in that slide's speaker Notes, and writes the revised answer under the first — "leave both showing." The annotated deck — first answer beside revised answer — is the single artifact. It is the completion evidence ("Completion = both answers present. Your growth shows in your printed Growth Report, not the grade."), and it is what your batch run reads to produce each student's Conceptual Growth Report and your class summary (see the AI Feedback folder). Even the Cycle 20 capstone proposal rides this pattern: "turn it in with your deck to the class folder — no separate upload."

So your LMS has exactly four jobs per cycle:

1. Get an **editable copy** of the deck to every student (speaker Notes intact — the revision prompt lives there).
2. Give students **one obvious place** to submit that same file, and collect it before the bell on each block.
3. Hand you back the **finished decks in one folder** for the Day-3 batch run.
4. Post **completion** (both boxes filled), and nothing about answer quality.

Anything your platform adds beyond those four jobs is convenience. Anything that breaks one of them — a submission flow that flattens the deck to PDF, a copy step that strips speaker Notes, a folder structure that scatters the decks — breaks the system, not just the logistics.

**One hard rule that follows: never distribute or collect decks as PDF.** A PDF has no speaker Notes (no revision prompt), no editable answer boxes, and cannot be revised on Day 3. The deck must travel as a live slide file — PowerPoint (.pptx) or Google Slides — end to end.

## 2. Rules that hold on every platform

**One canonical copy of every file.** Each deck, each printable (the Pacific NW species-cards PDF, the station checksheets, the activity guides), lives in exactly one place — your cloud drive. The LMS holds links to that place, or platform-generated student copies of it — never a second uploaded original. The Master Agenda names the canonical file per cycle ("**Slides** is the canonical file... the deck filename is the name of record"). The moment the same deck exists as an upload in three assignments, you have three things to update and no way to know which one a student opened.

**Links live on the deck slides; the LMS repeats only what students must click directly.** The decks already carry the sim, game, and reading links (Master Agenda: "the deck you are projecting already carries them"). Do not rebuild the link list inside the LMS — you will maintain it twice and they will drift. What the LMS needs per cycle: the deck copy/submission point, and at most the Fiddle URL (the tab students open on arrival).

**Teacher-facing materials never enter the student-visible course.** The Master Agenda, Unit Agendas, the Ecology Unit Guide, the Master Supply System, Standards and Alignment, your batch prompts, and the class summaries are your operating documents. Keep them in your own drive and bookmark them (the Master Agenda is meant to be "open during class" — a browser bookmark or a pinned tab beats any LMS page for that). Conceptual Growth Reports are per-student private: printed and handed back, or delivered individually — never posted to a shared space. One deliberate exception: the deck's slide 1 TEACHER REFERENCE (cycle, essential claim, NGSS PEs, objectives) travels with every student copy. That is by design — it is reference, not secret, and it is what supports absent students and administrators. Nothing on it needs hiding; just never project it.

**Organize by cycle, in arc order.** Mirror the Master Agenda: four arcs — Ecology (Cycles 01–07), Cells (08–11), Genetics (12–16), Evolution & Human Impact (17–20) — with one folder/topic/module per cycle inside. Name them exactly as the Master Agenda does ("Cycle 02 — Ecosystems & Feeding Relationships") so your LMS, your drive, and your agendas all speak the same names. Do not organize by week or date — cycles are flexible and your calendar will move (see Schedule Options); a date-based structure has to be rebuilt every time it does.

**Name student copies so the batch run can read them.** The batch step needs to know whose deck is whose. Use one convention all year, set in the assignment directions on Cycle 01 or 02 and never changed — for example `P3 - Rivera - Cycle 02`. Platforms that auto-copy (Google Classroom) prepend the student's name for you; platforms that don't (Schoology file upload, Moodle) need the convention stated and enforced early. (The specific convention is a build suggestion, not Katherine's documented practice — `GAP — NOT IN SOURCE NOTES`.)

**Update between cycles, never under students mid-cycle.** Once students have copied a deck, their copies are forked — replacing the master changes nothing for them and creates two truths. When an updated deck ships (a TPT product update, or your own edit), swap it during the gap between cycles: replace the canonical file's contents behind the same link where your platform allows (Drive "Manage versions" for .pptx keeps the link stable), or re-link once in the one place the link lives. If you must fix something mid-cycle — a broken sim link, a typo in a question — announce it and fix forward; do not recall student copies.

**Version chaos is a symptom of duplicate uploads.** If you find yourself with `Cycle02_final`, `Cycle02_final2`, and `Cycle02_USE_THIS`, the cause is always the same: the file was uploaded into the LMS instead of linked from the drive. Go back to one canonical copy and links.

## 3. Schoology — Katherine's platform, folder-based, no API

This section describes the system as Katherine actually runs it: folder-based course organization, no API access, Drive uploads via Chrome extension. Her sourced footprint is thin — the deck template carries "Graded activity (assign via Schoology): [ADD LINK]" and "Schoology assignment link: [ADD URL]" on the teacher slide, and the Cycle 20 checklist says "I turned the deck in to the folder" — so the structure below is her working pattern plus build-completed detail. The full Schoology workflow is `GAP — NOT IN SOURCE NOTES` in the corpus; anything below marked `WORKFLOW DEMONSTRATION NEEDED` awaits her screen recording.

**Course structure.** In Course Materials, one folder per cycle, named as the Master Agenda names it, grouped under the four arcs (either four parent folders or a numbered flat list — flat is fine, cycle numbers keep order). Inside each cycle folder:

- The deck access point (below).
- One Schoology **assignment** for the deck submission — this is "the class folder" students turn in to. One per cycle is the default; the notes-due-before-the-bell policy can run as one submission updated each block or as per-block assignments — Katherine's exact split between per-block and per-cycle collection is `WORKFLOW DEMONSTRATION NEEDED`.
- One assignment per **graded activity** where the deck's teacher slide calls for it ("assign via Schoology: [ADD LINK]") — e.g., the Cycle 02 food-web build if you collect it separately. Most cycles need nothing beyond the deck.
- Optionally a link to the Fiddle (e.g., BioMan Ecology Games for Cycle 02) so arriving students click one thing.

**Getting the deck to students (no API, so no auto-copy).** Two working routes; pick one and keep it all year:

- *Drive route:* the canonical deck lives in your Google Drive. Post a view-only link; each student opens it and makes their own copy (File → Make a copy in Slides, which preserves speaker Notes). First-week training makes this a 30-second routine.
- *File route:* attach the .pptx to the assignment; students download, work in PowerPoint, and upload the file back.

Either way the copy is editable and Notes-intact. Which route Katherine uses, and the exact student click path she trains, is `WORKFLOW DEMONSTRATION NEEDED`.

**Submission.** Students submit to the cycle's assignment. Students working in Drive submit via the Schoology Google Drive Assignments Chrome extension (upload from Drive into the Schoology submission), or download-and-upload the file. This is the "Chrome-extension Drive upload" in Katherine's actual workflow; the exact extension configuration and student-side steps are `WORKFLOW DEMONSTRATION NEEDED`.

**Getting decks back for the batch run.** With no API, collection is manual: bulk-download the assignment's submissions from Schoology (or, on the Drive route, collect from the students' submitted Drive files) into one local/Drive folder per cycle, then run the batch (AI Feedback folder). This download step is the price of the no-API environment; it is minutes, not hours, but it is why the naming convention in Section 2 matters — the batch reads names from files. `WORKFLOW DEMONSTRATION NEEDED` for the bulk-download click path on your district's Schoology version.

**Posting completion.** The gradebook entry is completion only. Katherine's pipeline produces a CSV — one row per student, one column per lesson (`DRAFT.<Lesson>` / `Notes.<Lesson>`) — posted to Schoology via gradebook import; a hand-kept column works identically (see Assessment: Completion, Copying, and Proficiency, section 5). Import mechanics vary by district configuration — `WORKFLOW DEMONSTRATION NEEDED`.

**What not to do in Schoology.** Do not upload the deck into multiple assignments (version chaos); do not use Schoology's document viewer as the student working surface (it renders, it does not edit); do not post Unit Agendas or the Master Agenda into Course Materials — they are yours, not the students'.

## 4. Google Classroom

Classroom is the platform whose native mechanics match the pattern best, because copy-per-student is built in.

- **Deck distribution:** create the assignment, attach the deck (as Google Slides), and choose **"Make a copy for each student."** Classroom copies it into each student's Drive, prepends their name, and collects it on Turn In. Speaker Notes survive the copy. This one setting replaces the entire make-a-copy training from the Schoology route. If your canonical deck is .pptx, convert it to Slides once and spot-check that the response-slide Notes (the revision prompt) and the answer boxes survived conversion — they normally do, but verify on your first cycle before trusting it for twenty — `WORKFLOW DEMONSTRATION NEEDED` (one-time check, your file, your domain).
- **Structure:** Topics = cycles, named as the Master Agenda names them, in arc order (Classroom lists newest-first by default; drag topics into cycle order once). One assignment per cycle for the deck; Materials posts only for what students click (the Fiddle link).
- **Submission and return:** students Turn In the deck; you download the assignment folder from Drive (Classroom keeps all copies in a per-assignment Drive folder) for the batch run. After the batch, Return the decks so students keep ownership of their artifact.
- **The Day-3 wrinkle:** a Turned In deck locks for the student. Because the deck spans three blocks with revision on Day 3, either have students Turn In only at end of Day 3 (with the notes-due policy enforced by your walk-through, not the platform, on Days 1–2), or Return decks after each block so they stay editable. Pick one and be consistent. Katherine's practice is Schoology, so there is no sourced answer here — build guidance only, `GAP — NOT IN SOURCE NOTES`.
- **Privacy:** anything attached to a post is visible to the class — keep teacher materials out of Classroom entirely; they live in your Drive.
- **Grading:** create the assignment ungraded or graded on completion points only; proficiency never posts (see Assessment: Completion, Copying, and Proficiency).

## 5. Canvas

- **Structure:** Modules = cycles, in arc order, named as the Master Agenda names them. Inside each module: an external link to the deck's copy point, the submission assignment, and the Fiddle link. Keep Pages minimal — do not transcribe the Unit Agenda into a Canvas Page; it is a teacher document, and a copy inside Canvas is a copy that drifts.
- **Deck distribution:** Canvas has no native copy-per-student for slide files. Two routes: (a) if your school runs the Google Apps LTI, a **Cloud Assignment** with a Google Slides file distributes a per-student copy Classroom-style — availability and behavior are district-dependent, `WORKFLOW DEMONSTRATION NEEDED`; (b) otherwise use the view-only-link + File → Make a copy routine from the Schoology section, or attach the .pptx for download.
- **Submission:** an Assignment with File Upload submission type (accept .pptx), or the Cloud Assignment's own collection if you used one. SpeedGrader will preview slides but not reliably their speaker Notes — read decks in the batch run, not in SpeedGrader; use SpeedGrader only to mark completion.
- **Collection for the batch:** Canvas can bulk-download all submissions for an assignment as a zip — that zip is your batch input folder. (Canvas appends student names to filenames on download, which substitutes for the naming convention.)
- **Privacy:** unpublished Files and Modules are invisible to students, but the safer rule stands — teacher materials stay out of the course shell altogether.

## 6. Moodle

- **Structure:** course format "Topics," one section per cycle in arc order. Inside each section: a URL resource to the deck copy point, an **Assignment** activity (File submissions, .pptx accepted), and a URL resource for the Fiddle.
- **Deck distribution:** no native copy-per-student. Use the view-only-link + Make a copy routine, or a File resource holding the .pptx for download. Train the routine in week one, same as Schoology.
- **Submission:** the Assignment activity collects files; "Download all submissions" gives you the batch input folder, with student names folded into filenames.
- **Privacy:** hidden sections and "stealth" activities exist but their behavior varies by theme and version — do not rely on them for teacher materials; keep those out of the course. `WORKFLOW DEMONSTRATION NEEDED` if you want to use hidden sections at all.
- **Caution:** Moodle's default upload size limits are often below a media-heavy deck (some decks run 45–57 slides). Check the course's maximum upload size before Cycle 01, and raise it or switch to the Drive-link route if student decks bounce.

## 7. Any other platform (Brightspace, Teams for Education, itslearning, ...)

Do not look for feature parity; ask the four questions from Section 1 and wire the answers:

1. Can it put an **editable, Notes-intact copy** of a slide file in each student's hands? (Native copy-per-student, or the view-link + Make a copy routine.)
2. Can students **submit that file** to one obvious place, per cycle?
3. Can you **bulk-retrieve** all submissions into one folder?
4. Can you post a **completion-only** entry?

If all four are yes, the platform works; organize by cycle, keep one canonical copy of every file, keep teacher materials out, and apply Section 2. If any is no, the paper variants in Section 8 fill the gap. Never let a platform limitation push you to PDF distribution — that is the one substitution that silently kills the revision loop.

## 8. Environment variants

The decks assume 1:1 devices (sims, LMS links, deck submission) — that assumption is in the source decks, not negotiable elsewhere in the design, so every other environment below is an adaptation. The adaptations are build-provided, not Katherine's documented practice — `REVIEW WITH KATHERINE` — and each names what it costs.

**1:1 Chromebooks (the designed environment).** Fiddle tab open on arrival (Cycle 02: BioMan's remove-a-species game), deck copy per student, sims run at desks, notes due and submitted before the bell. Build the submit step into the last five minutes of every block — the decks' own Think → Write → Submit checklist slide is that buffer made visible.

**Shared devices (one per pair or station).** Protect two things: the sims can be shared; the artifact cannot. Run contrasts, sims, and activities on the shared device; stagger the writing so each student types their own first answer into their own deck during the activity rotation (while partner A runs the Energy Tank Model sliders, partner B writes; swap). If rotation time is too tight, first answers go on paper during the block and are typed into the deck at the next device turn — before Day 3, because the revision prompt needs the first answer in the deck. Cost: transcription time and a weaker before-the-bell guarantee.

**No student devices.** The paper variant: print the response slides as a per-cycle answer sheet — question, first-answer box, revised-answer box, both staying visible, exactly the slide layout on paper. Sims and games become teacher-projected with students calling the moves ("drag the transfer efficiency down — what happened to the hawks' tank?"); Fiddles shift to the no-tech ones every cycle already carries (the Cycle 01 cup sort, THE DOG SAT puzzle, PTC strips). Day 3 revision without student AI access: run the revision prompt yourself on a projected sample of (anonymous) first answers so the room sees the move, then students revise on paper from the contrast, pattern-break, and discussion. The batch run can read photographed/scanned sheets, but expect friction with handwriting. Cost: the single-artifact elegance and the per-student AI pass — this is the heaviest adaptation; `REVIEW WITH KATHERINE` before documenting it as supported.

**Printer-rich.** Print liberally where the design calls for print anyway: species card sets, station cards, sort cards, lab sheets, the Cycle 20 argument template — and above all the Conceptual Growth Reports, where print is the designed artifact ("something a ninth grader holds, keeps, and shows"). Laminate the reusable sets (cards, checksheets) once; the Master Supply System tracks what is print-once vs. print-per-class.

**Limited printing.** Priority order when pages are rationed: (1) Growth Reports — the one print the system is built around; (2) card sets and station cards — print once, laminate, reuse all year and next year; (3) lab sheets — these can go digital (linked Google Docs already exist for several: Cycle 03's station checksheet, Cycle 06's trace worksheet) or be projected with answers in the deck; (4) everything else stays on screen. Never spend the ration duplicating what the deck already shows.

**Home access allowed.** Home access is for absence recovery, not homework shifting. The slides "carry a fair amount of text — to support students who were absent or are reviewing"; an absent student opens their deck copy from home, reads the slides, writes their first answers, and catches the revision step on return. The notes-due-before-the-bell policy stands for students who are present — its rationale is cognitive, not logistical ("help your brain process today's lesson while it is still fresh"), and moving the writing home defeats it.

**In-class only (no home access).** The system already works this way — everything is designed to finish in the block. What you must protect: the submit buffer at the end of every block (devices out of hands after submitting, not before), and a catch-up seat — an absent student's first move on return is their own deck copy during the Fiddle window and activity time, not a take-home packet.

## 9. Quick reference

| Job | Schoology (Katherine's) | Google Classroom | Canvas | Moodle |
|---|---|---|---|---|
| Editable copy per student | View link + Make a copy, or .pptx download — `WORKFLOW DEMONSTRATION NEEDED` | Native: "Make a copy for each student" | Google LTI Cloud Assignment if available, else view link + copy | View link + copy, or .pptx download |
| Deck submission | Assignment; Drive upload via Chrome extension — `WORKFLOW DEMONSTRATION NEEDED` | Turn In (auto-collected in Drive) | Assignment, File Upload | Assignment activity |
| Bulk retrieval for batch | Manual bulk-download — `WORKFLOW DEMONSTRATION NEEDED` | Assignment's Drive folder | Download submissions (zip) | Download all submissions |
| Completion posting | CSV gradebook import / hand column | Points or ungraded | SpeedGrader, completion mark | Gradebook, completion mark |
| Organize by cycle | Folders per cycle | Topics per cycle | Modules per cycle | Sections per cycle |
| Teacher materials | Out of Course Materials | Out of Classroom | Out of course shell | Out of course; don't trust hidden |

Where to go next: Start Here for the system in ten minutes; the Master Agenda for the per-cycle operating view your LMS structure should mirror; the Unit Agenda for what each cycle's folder must contain; AI Feedback (../10_AI_Feedback/) for the batch run the collected decks feed; Assessment: Completion, Copying, and Proficiency (../09_Assessment_Proficiency/) for the gradebook rules the completion posting follows.

---

Sources used: `/root/ab_build/BUILD_BRIEF.md`; `/root/ab_build/output/17_Source_Audit/ANSWERABLE_BIOLOGY_SOURCE_MAP.md` (Schoology placeholders on Cycle 15/17 teacher slides; Cycle 20 "turn it in with your deck to the class folder — no separate upload"; Cycle 02 Think → Write → Submit checklist; deck link inventories); `/root/ab_build/output/17_Source_Audit/TEACHING_REASONING_EXTRACTION.md` (LMS setup §6 — one Schoology assignment per graded activity, deck submitted to the folder; notes-due rationale; slides-support-absent-students; Chromebook/GoGuardian gaps); `/root/ab_build/output/02_Year_Arc/Master_Agenda.md`; `/root/ab_build/output/02_Year_Arc/Year_Arc_20_Cycles.md`; `/root/ab_build/output/01_Start_Here/Start_Here_How_Answerable_Biology_Works.md`; `/root/ab_build/output/09_Assessment_Proficiency/Assessment_Completion_Copying_Proficiency.md` (CSV-to-Schoology completion posting); `/root/ab_build/output/10_AI_Feedback/AI_Feedback_and_Conceptual_Growth.md` (batch flow, Growth Report print-as-designed-artifact).
