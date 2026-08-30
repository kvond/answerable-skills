# Feedback prompts — paste these into your AI

*Marker version · replaces prompts 1 and 2 · written 30 August 2026 against the
**finished** deck standard, not against the decks as they stand today*

---

## Why this document is ahead of the decks

The decks are mid-rebuild. Claude Code is still bringing them back online; the
compensatory pair and the conflict case have not been added; the Concept Bank is
not in the live decks yet; the three removed slide types are still in some of
them. Writing these prompts against that moving state would mean rewriting them
every time a deck changed.

So they are written against the standard the decks are converging on. Each deck
becomes readable by these prompts the moment it meets that standard, and not
before.

**The risk that creates, and what is done about it.** A prompt written for the
finished state, run on an unfinished deck, does not announce a problem — it
returns zeros, and a deck that was never markered looks exactly like a class that
wrote nothing. That failure is silent and it lands on students.

Every prompt below therefore opens with a readiness check that runs *before* any
scoring, and stops rather than scoring a deck that is not ready. Prompt 0 is that
check on its own, for when you want to know where a deck stands without scoring
anything.

---

## The standard these prompts assume

A deck is ready for the pipeline when all of this is true:

1. **Slide 1 carries a `[[MARKER-INVENTORY:CNN]]` line** giving the cycle, the
   NOTES total, the DRAFT total, the OPTIONAL total, `BANK_TERMS`, and the list
   of every question id the deck contains.
2. **Every student writing box carries a marker** in the label immediately above
   it, in the form `[[KIND:CYCLE:QUESTION-ID]]`.
3. **Every Concept Bank term carries a `[[BANK:CNN:term]]` marker.** The bank
   counts as one NOTES item however many terms it holds.
4. **The three removed slide types are gone** — Then and Now, Think → Write →
   Submit, Turn your answer into a draft.
5. **A Concept Bank sits before the Day 3 divider**, asking the student to fill
   in blanks and nothing more.
6. **The conflict case, where the cycle carries one, follows the Concept Bank**,
   and carries its own what-if.
7. **Every response slide and every what-if slide has the revision prompt in its
   speaker notes**, with the `QUESTION:` line filled in.

[As of 30 August: item 7 is done on all 24. Item 4 is done in the built files.
Items 1, 2 and 3 are done in Cycles 02 and 03 only. Items 5 and 6 are done in the
built files but not in the live decks, because the import has not run. So no deck
currently passes the readiness check, and that is the correct answer for today
rather than a fault in the prompts.]

---

## What the markers mean

Every tag reads `[[KIND:CYCLE:QUESTION-ID]]`. No slide numbers anywhere — answer
types move around between decks and the tags don't, so one prompt reads any
cycle, and the NOTES score and the DRAFT score can never be read off the same
boxes by mistake.

**`[[NOTES:C02:CA1-MASTERY]]`** — an in-class writing box, including the *first
answer* on a response slide. These are the NOTES formative.

**`[[DRAFT:C02:CA1-MASTERY]]`** — the *revised answer* to that same question,
same id, so the pair survives any reshuffling. These, and only these, are the
DRAFT summative.

**`[[OPTIONAL:C02:OPT-SQUID]]`** — optional challenge and "relates to me" boxes.
Reported as bonus, never scored.

**`[[BANK:C02:niche]]`** — one Concept Bank term.

**`[[MARKER-INVENTORY:C02]]`** — on slide 1. What the deck should contain, so a
deck the AI half-read shows as a mismatch instead of as a low score.

---

## Prompt 0 — Readiness check

Run this on one deck before you score a class set. It scores nothing.

---

I am a high school teacher. I am attaching one student slide deck.

Do not score anything. Tell me whether this deck is ready for the feedback
pipeline, and answer these in order:

1. Is there a `[[MARKER-INVENTORY:` line on slide 1? Quote it. If there is none,
   say so and stop — nothing below can be checked without it.
2. How many `[[NOTES:` markers did you find? Does that match the inventory's
   NOTES total?
3. How many `[[DRAFT:` markers? Does that match the DRAFT total?
4. How many `[[BANK:` markers? Does that match `BANK_TERMS`?
5. List any question id in the inventory that you could not find in the deck, and
   any marker you found that the inventory does not list.
6. Does a slide headed `Define these in your own words` appear before the slide
   headed `Day 3 of 3`?
7. Do any of these still appear: `Then and Now`, `Think → Write → Submit`, `Turn
   your answer into a draft`? Name the slide if so.

Finish with one line: READY, or NOT READY and the first reason.

---

## Prompt 1 — Completion check

Fills your ROSTER & SCORES sheet. Two independent numbers per student.

---

I am a high school teacher. I am attaching student slide decks from one lesson.

**Before scoring anything, check readiness on the first file.** Find the
`[[MARKER-INVENTORY:` line on slide 1. If it is missing, or if the number of
`[[NOTES:` markers you find does not match its NOTES total, **stop and tell me
that, and do not produce any scores.** A deck without markers reads identically
to a student who wrote nothing, and I would rather have the warning than the
table.

The decks contain hidden text markers that tell you which boxes to read. A marker
sits immediately above the box it names, in the text of the label. Every marker
reads `[[KIND:CYCLE:QUESTION-ID]]` — for example `[[NOTES:C02:CA1-MASTERY]]`.
Find them by that literal bracket form:

- **NOTES** — the student's in-class writing box, including a first answer
- **DRAFT** — the student's revised answer, written after working with an AI
- **OPTIONAL** — optional work
- **BANK** — one Concept Bank term
- **MARKER-INVENTORY** — on slide 1

The text belonging to a marker is the student writing that follows it, up to the
next marker. Identify every box by its marker, never by slide number or page
position.

Use the inventory's NOTES and DRAFT totals as your denominators. Check the
question ids you found against its id lists; if any are missing, say which, for
that student, before you give a number.

For EACH file, give me one table row:

1. Student name, from the file name.
2. **NOTES SCORE, 0 to 10.** Look ONLY at NOTES markers plus the Concept Bank.
   Count how many carry writing in the student's own words — not blank, not the
   printed question, not the word bank, not the placeholder text. Count the
   Concept Bank as ONE item, credited if at least two thirds of its `[[BANK:`
   terms are defined in the student's own words. Score = that count divided by
   the NOTES total, times 10, rounded to a whole number.
3. **DRAFT SCORE, 0 to 10.** Look ONLY at DRAFT markers. Never let a NOTES box
   contribute to this number, even when it sits on the same slide. Same
   arithmetic against the DRAFT total.
4. **OPTIONAL** — list the question ids of the OPTIONAL boxes that have writing.
   No score.
5. **FLAG** — only if a NOTES answer is word-for-word the printed slide text. Do
   not flag weak grammar, short answers or unusual phrasing; those are not
   evidence of anything.
6. One short quote of the student's own words from a DRAFT box.

Do not score correctness. These numbers measure how much of the deck the student
filled in, nothing else. Do not rank students. Do not rewrite anything. Do not
include the markers themselves in any quote.

---

## Prompt 2 — Growth Reports

Only the opening changes from your current Prompt 2. Everything after "Write ONE
report per student" stays exactly as you have it.

---

I am a high school teacher. I am attaching student slide decks from one lesson.

**First, confirm the decks are markered.** If you cannot find a
`[[MARKER-INVENTORY:` line on slide 1, stop and say so rather than writing
reports from what you can see. An unmarkered deck produces a report about a
student who appears not to have revised anything, which is a false statement
about that student.

The decks carry hidden text markers naming each student writing box. Every marker
reads `[[KIND:CYCLE:QUESTION-ID]]`. A marker sits in the label immediately above
its box, and the writing that follows it, up to the next marker, belongs to it:

- **NOTES** — written in class, before instruction. The student's first thinking.
- **DRAFT** — written after the student worked with an AI that questioned them.
  The revision.
- **OPTIONAL** — optional work; mention it only if there is writing there.
- **BANK** — a Concept Bank definition.

A NOTES and a DRAFT sharing the same QUESTION-ID are the same question, before
and after. Pair them by that id — never by slide number, never by position.

"Where my thinking started" comes from NOTES. "How my thinking changed" and every
quote in "Evidence from my final answer" come from DRAFT. Never quote a marker
itself, and never quote a NOTES box as if it were the revision.

Give one Current understanding line per DRAFT question id, and name the id you
are judging.

If a marker's box is empty, say that box is empty rather than filling it in.

---

The over-20-decks compiling paragraph gets simpler — replace "list every question
in the deck" with: for every NOTES / DRAFT pair sharing a question id, give the
id, the slide title, the NOTES text copied exactly, and the DRAFT text copied
exactly.

---

## What the student runs

*In the speaker notes of every response slide and every what-if slide — 77 slides
across the 24 built decks, done 30 August. The `QUESTION:` line carries the
question that slide actually asked, so the student is not asked to retype it.*

---

REVISION PROMPT — Open an AI and copy and paste the following:

QUESTION: *(the question that slide asked)*

`-----`

[PASTE IN YOUR FIRST ANSWER]:

`-----`

I am a high school student. Below is a science question and my first answer. Do
NOT rewrite my answer and do NOT give me the answer. Instead:

1. Tell me one thing I got right, or was interesting.
2. Quote my own words back to me as You said, "".
3. Ask me two questions that make me look again at one idea I might have wrong or
   left out or could be made more complete.
4. Illustrate it with one distinction or example worth thinking about.

—-

Keep it short and in plain language, then stop so I can write my own revised
answer.

`-----`

Once you get your feedback: write your revised answer in "Your revised answer" on
the slide — in your own words.

---

[Two notes on that prompt. Your draft numbered the items 1, 2, 2, 3; renumbered
1–4, which is the only substantive edit. And item 2 ends on an empty pair of
quotation marks — `You said, ""` — which reads as the slot the AI fills. It works
as a template; a student may read it as a typo. An ellipsis inside the quotes
would settle it either way.]

---

## Two things to check on your first real run

Open one markered deck in presentation view and confirm you cannot see the tags.
They are 1pt grey at 6% opacity, sitting under the label text — visible at 400%
in the editor, invisible to a room.

Run Prompt 0 on one deck before you run Prompt 1 on a class set. If it says
READY, the pipeline will read everything. If it says NOT READY, it names the
reason, and that reason is a deck problem rather than a student problem.
