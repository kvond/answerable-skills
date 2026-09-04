# Claude, the LMS, and the Gradebook — Katherine's Working Process

Purpose: how Katherine actually uses Claude (the desktop app and the Chrome extension) to wire each cycle's assignments into Schoology and the gradebook — what she hands it, what she asks of it, and what she personally verifies before anything reaches a student or a grade.

## What this document is, and one caveat before anything else

This is a record of one teacher's working process, offered so you can see the shape of it and adapt the parts that fit your school. Katherine's own caveat governs the whole document: "I am not describing a product, and I am not recommending a particular tool. I am describing what one teacher does when she points a general-purpose machine at the specific, stubborn production problem that was eating her presence. The principle is portable; the particular way I do it probably is not."

The principle is this: LMS setup, gradebook entry, and communication drafting are production work — part of the "roughly forty percent" of the job that used to consume her hours. "AI helps make the work doable. It is not the doer." Claude drafts, organizes, and carries the repetitive pattern; she decides, verifies, and publishes. Every word that reaches a student or the gradebook passes through her first.

Where a specific operation below is not documented in her materials, it is marked WORKFLOW DEMONSTRATION NEEDED. There are many such marks. That is deliberate: this document records what the sources support and requests a demonstration for the rest, rather than inventing click-paths she may not use.

## The setup, briefly

Two pieces of Claude, doing different jobs:

- **Claude desktop** — where the thinking-and-drafting work happens: assignment text, the teacher batch over submitted decks, Growth Reports and class summaries, the completion CSV, email drafts.
- **The Chrome extension** — where the browser work happens: Claude operating inside her own logged-in Chrome session, so it can work in Schoology, Drive, and Gmail as her, on screen, while she watches. Her documented submission flow already runs this way: student decks come in by "Chrome-extension Drive upload, as now" (her v2 pipeline spec), landing in a class folder — the student checklist in every deck reads "I turned the deck in to the folder."

The exact configuration — which folders are connected, how sessions are set up, what the extension is permitted to touch — is not documented. WORKFLOW DEMONSTRATION NEEDED (one screen recording of a cycle's setup session would close most of the gaps in this document at once).

## 1. What context she provides Claude

Claude is only as reliable as what it is looking at, so each working session starts from the operating documents, not from memory:

- **The current Unit Agenda** (and the Master Agenda as the year index) — what this cycle is, which activities are graded, what the link lines still need. See the Unit Agenda template and the Ecology Unit Guide for what these carry.
- **The deck's own teacher slide** — the authoritative record per cycle: "Cycle 2 · Ecosystems & Feeding Relationships — Unit 1 · 3 blocks," essential claim, objectives, and the graded-activity line ("Graded activity (assign via Schoology): [ADD LINK]").
- **The Dashboard for class membership.** Her pipeline rule is explicit: "Class membership from the Dashboard (source of truth), never from filename/folder." Rosters never come from guessing at file names.
- **The folder of submitted decks** for the batch run — one annotated deck per student, first answer and revised answer on the response slides.
- **The standing conventions** that must not drift: the completion-only gradebook rule, the column naming (`DRAFT.<Lesson>` or `Notes.<Lesson>`, matching the existing gradebook column), and the report standards (no coding vocabulary reaches a student).

How this context is packaged per session — pasted in, attached, held in a standing project — is not documented. WORKFLOW DEMONSTRATION NEEDED.

## 2. What she asks Claude to help enter or organize

The recurring asks, from the sources:

- **The teacher batch.** After Day 3, the submitted decks run through the batch prompt: extract each student's first and revised answers, run the integrity gate on the first answer only, draft one Conceptual Growth Report per student, the class summary, and the completion CSV. The full flow and prompts live in "AI Feedback and Conceptual Growth"; this is the single biggest job Claude carries.
- **The completion CSV** — "the only thing that reaches Schoology": one row per student, header `DRAFT.<Lesson>` (or `Notes.<Lesson>`), completion = both answer areas filled. How the CSV actually gets into the Schoology gradebook — import, or entry via the Chrome extension — is not documented. WORKFLOW DEMONSTRATION NEEDED.
- **Folder organization.** The submission system is folder-based: class folders receiving Chrome-extension Drive uploads of finished decks. What Claude does to create, name, or tidy these folders per cycle is not documented. WORKFLOW DEMONSTRATION NEEDED.
- **Schoology assignment work.** The decks' teacher slides show the pattern — one Schoology assignment per graded activity, plus the deck-submission assignment ("Schoology assignment link: [ADD URL]"). Whether Claude drives the Schoology screens through the Chrome extension while she watches, or drafts the text for her to paste, is not documented either way. WORKFLOW DEMONSTRATION NEEDED — this is the demonstration teachers will ask for first.
- **Student email as Gmail drafts.** When a student needs an individual message — a flagged first answer to talk through, a missing submission, a follow-up on a report — Claude prepares the message as a Gmail draft. Drafts only: nothing sends until she has read it and presses send herself. This is the human gate applied to email. Which occasions get an email rather than her documented in-person habit ("When I grade their work and find a problem, I hunt them down to talk about it") is not written down. WORKFLOW DEMONSTRATION NEEDED.

## 3. How she uses Claude while creating assignments

Her own account, from the book, of what the AI produces during creation: "It drafts lesson outlines I then adjust. It generates slides I scan and talk over rather than read. It drafts feedback in a register I have specified. It writes IEP-accessible versions of an assessment I would otherwise have written by hand at midnight. None of that is teaching."

Applied to assignment wiring, that means:

- **Assignment text drafted from the deck's own language, then adjusted.** The description for a Cycle 02 deck-submission assignment does not need composing from scratch: the deck already says what students must do ("Think → Write → Submit"; "Completion = both answers present. Your growth shows in your printed Growth Report, not the grade") and why notes are due before the bell ("When you wait until later: you remember less, you're more likely to copy, you miss the learning that the notes are designed to create"). Claude assembles; she adjusts.
- **Due dates that carry the policy.** Deck submission due end of Day 3; notes due before students leave — the due time is the class period, not midnight.
- **IEP-accessible versions on the same conceptual bar.** Her stance: "I differentiate not by lowering the conceptual bar but by removing the linguistic obstacles." Claude drafts the accessible version; she checks that the bar did not move.
- **The wiring step the placeholders mark.** The decks carry `[ADD LINK]`, `[ADD URL]`, `[ADD SCHOOLOGY URL]` on their teacher slides, and the Unit Agenda carries matching link lines. Creating the assignment produces the URL; the URL goes back into the agenda (and the teacher slide where the deck expects it). Whether Claude does the paste-back or she does is not documented. WORKFLOW DEMONSTRATION NEEDED.

## 4. How it reduces repetitive LMS setup

The per-cycle administrative loop (see "Set Up Answerable Biology," step 12) has the same shape twenty times a year: open the next Unit Agenda, create the cycle's two assignments, paste the links, distribute student deck copies, print from the Master Supply System list, queue the fiddle tab. Nothing in that loop is intellectually hard; all of it is exactly the kind of "invisible labor that consumes teacher attention" the book describes — "if AI can help organize materials, generate drafts, process repetitive workflows, create feedback structures, or assist with planning, then something more important may become possible: the teacher can remain cognitively available inside the classroom itself."

Concretely, the repetition Claude absorbs:

- The cycle-to-cycle sameness: Cycle 03's setup is Cycle 02's setup with new names, new links, one new graded activity (the station checksheet instead of the food-web build). Claude carries the pattern; she supplies only the differences.
- The batch, the reports, the CSV — the entire post-Day-3 processing that used to be "a stack of papers to grade."
- Drafting that repeats with variations: assignment descriptions, parent-facing versions, accessible versions, individual emails.

And the boundary that keeps this honest: the freed time is for presence, not more production. "Standing at the counter, crouching beside a stuck student, running the dialogic register for more of the room." A setup workflow that generates more setup has missed the point.

## 5. How assignments connect back to the Unit Agenda

The Unit Agenda is the operating document — the page she teaches from — so it is also the index of record for what exists in Schoology:

- The agenda names the cycle's assignments before they exist: for Cycle 02, the deck submission (due end of Day 3) and the food-web build if graded. The agenda is the instruction; Schoology is where the instruction gets executed.
- Once created, the assignment URLs go back into the agenda's link lines. The rule from the setup document holds: fill the link lines before Day 1. An agenda with live links is the difference between teaching from one page and hunting through the LMS mid-class.
- The Master Agenda holds the year view; the Year Arc explains what each cycle is for. Claude can read all three, which is what lets it draft the next cycle's assignments without being re-briefed — but the agenda, not the LMS, stays the source of truth for what a cycle contains.

## 6. How completion and proficiency are represented

This is the one place where the rule is hard and documented in full:

- **The gradebook records completion only.** "Schoology records completion: both answer areas filled = done. Never quality." One column per cycle deck, header `DRAFT.<Lesson>` (or `Notes.<Lesson>`), one row per student. The student-facing statement, on the closing checklist of every deck: "Completion = both answers present. Your growth shows in your printed Growth Report, not the grade."
- **Proficiency lives only in the Growth Report** — the per-aspect progression a student holds in their hands — and in the class summary and rollups on the teacher's side. "All proficiency/growth lives in the Growth Report, never the gradebook." Nothing Claude produces for Schoology carries a quality judgment.
- **Integrity flags never post as flags — a flagged entry is held until you resolve it.** A flagged first answer is a teacher-review item in the batch output, visible to her and resolvable by her ("detection misfires, on ESL students and atypical writers especially"); the completion entry stays held pending that review, nothing posts automatically, and an AI-written first answer fails the entry only after she confirms — auto-flagged for failure, confirmed by you. Because the gradebook is completion-only, "a wrong flag costs a cycle's feedback, not a grade."
- **Grades stay heavy enough to matter.** "I am not going to pretend ninth-graders will engage purely for intrinsic reasons, and they need the grades to navigate the system." Completion-only is not grade-free.
- Category structure, weights, and the Schoology configuration for any of this are not in her materials — GAP — NOT IN SOURCE NOTES. If your school requires a graded proficiency column, "Assessment: Completion, Copying, and Proficiency" lays out that variant (Option B); it is the build's derivation, not her practice.

## 7. What she personally verifies before publishing — the human gate

Her words, and they are the whole architecture, not a caveat: "I read every piece of it before it goes to a student, and I adjust it as needed... The AI's draft is exactly that: a draft, produced fast, for me to check against what I actually know about the student and the concept... The reading is not quality control bolted on. It is the place the human judgment lives."

Applied to this workflow, the gate means every one of these is read, in full, by her, before it goes anywhere:

- **Every Growth Report**, before printing and handing back. The dangerous failure is not clumsy output but persuasive error: the AI "can affirm reasoning that is actually mistaken, or invent a 'real part' of a student's answer that is not there, in fluent, encouraging prose." Only someone who knows the student and the concept catches that.
- **Every assignment before it publishes to students** — text, link, due date, and (where it applies) that the accessible version kept the conceptual bar.
- **The completion CSV against the roster** before it touches the gradebook — Dashboard membership, one row per student, completion marks matching what was actually submitted. The verification step itself is not documented as a procedure. WORKFLOW DEMONSTRATION NEEDED.
- **Every Gmail draft** before she presses send. Claude never sends.
- **Every integrity flag**, personally resolved — restore the false positives, act on the real ones.
- **Timing stays hers.** The batch runs when she runs it — "on-demand only... never at session start." Nothing in this workflow fires on its own schedule.

The register instructions and report standards "are not set once; they have to be reasserted, and checked, against the grain of what the tool wants to do" — so the gate includes spot-checking every batch against the standards, not just the first one.

## The undocumented operations, gathered

For the demonstration session (screen recordings, one per item, most under five minutes):

1. How context is packaged per Claude session (project, files, pasted agenda). WORKFLOW DEMONSTRATION NEEDED.
2. Creating a cycle's two Schoology assignments — extension-driven or draft-and-paste. WORKFLOW DEMONSTRATION NEEDED.
3. Creating and naming the class submission folders; the Chrome-extension Drive upload from the student side. WORKFLOW DEMONSTRATION NEEDED.
4. Getting the completion CSV into the Schoology gradebook, and the pre-import roster check. WORKFLOW DEMONSTRATION NEEDED.
5. Pasting assignment URLs back into the Unit Agenda and teacher slides (who does the paste-back). WORKFLOW DEMONSTRATION NEEDED.
6. The Gmail-draft flow for student email: occasions, drafting, review, send. WORKFLOW DEMONSTRATION NEEDED.
7. Distributing per-student editable deck copies (also flagged in "Set Up Answerable Biology," step 6). WORKFLOW DEMONSTRATION NEEDED.
8. Gradebook category setup in Schoology for completion-only grading. WORKFLOW DEMONSTRATION NEEDED; structure itself GAP — NOT IN SOURCE NOTES.

## Teacher checklist — per cycle

Before Day 1:

- Open the Unit Agenda; give Claude the agenda and the deck's teacher slide.
- Create the two assignments (deck submission, due end of Day 3; the graded activity if the cycle has one — Cycle 02: the food-web build). Read the assignment text before publishing.
- Paste both URLs into the agenda's link lines. Links live before Day 1.
- Distribute student deck copies; confirm the submission folder is ready.

After Day 3:

- Run the batch over the submitted decks — when you choose, not automatically.
- Resolve every integrity flag yourself.
- Read every Growth Report, every word, against what you know about the student. Adjust. Then print.
- Check the completion CSV against the Dashboard roster; enter completion only. No proficiency, no quality, no flags in the gradebook.
- Read and adjust any student email drafts; you press send.
- Skim the class summary for the next instructional contrast — that read is what the whole pipeline is for.

The standing rule over all of it: if a word is going to reach a student or the gradebook, you have read it first.

---

Sources used: `Answerable Teaching-Chapter 6 — Doable, Not the Doer - AI.md` (what AI produces vs. what teaching is; the feedback register; the human gate; the three cautions; the workload and presence framing; the portability caveat); Katherine's formative-pipeline-v2 skill spec (teacher batch flow, integrity gate, completion CSV and `DRAFT.<Lesson>` header, Dashboard as membership source of truth, Chrome-extension Drive upload, on-demand rule, two-rail split); deck extracts in `/root/ab_build/extracted/` (teacher-slide Schoology patterns and `[ADD LINK]`/`[ADD SCHOOLOGY URL]` placeholders — Cycle 15 slide 1, Cycle 17 slide 3; "I turned the deck in to the folder" checklists; completion rule on closing slides); `Answerable Teaching-Chapter 5 — Intellectual Mentorship.md` (hunt-them-down habit; grades heavy enough to matter; IEP differentiation stance); `TEACHING_REASONING_EXTRACTION.md` and `ANSWERABLE_BIOLOGY_SOURCE_MAP.md` in `17_Source_Audit/` (LMS/gradebook gap register); cross-referenced build documents: `Set_Up_Answerable_Biology.md`, `AI_Feedback_and_Conceptual_Growth.md`, `Assessment_Completion_Copying_Proficiency.md`, `Year_Arc_20_Cycles.md`, `Unit_Agenda_Template.md`.
