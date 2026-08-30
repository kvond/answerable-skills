# The written work — what each document is

Nine documents, renamed 2026-08-30. They were numbered `01`–`12` by the order
they were captured, which stopped meaning anything once `04`, `05` and `11` were
never written and the series split across three directories — `08` sat in
`docs/curriculum/` while cross-referencing `10` in `docs/book/`. The names now
say what each document is, and every cross-reference in the prose and in the
three scripts was rewritten to match.

## docs/book — the argument

**`coordination_judgment_and_the_package.md`**
The sequenced synthesis, written for communication rather than in the order it
was thought. Runs from the problem — "she doesn't conceptualize it" is a verdict
with no next move — through simultaneity, the nine moves, the question form, the
coordination structures, visibility, what the artifacts carry, feedback, teacher
judgment, and the package's central risk. Ends with the build sequence and the
open decisions. Start here.

**`the_visibility_ladder.md`**
Exposure as a graduated dimension with its own clock, separate from cognitive
demand. Five rungs, each gated by what a teacher can observe rather than by week
number, plus the visibility ceiling for each of the nine moves, group work as a
visibility reducer, assessment, and the observation problem.

**`simultaneity_research_base.md`**
The construct and its positioning: synchronic and diachronic simultaneity, and
where the claim sits against Marton.

**`biology_education_research_reading.md`**
The evidence base — what to read and why it bears on the argument.

**`the_snake_question_book_notes.md`**
Working notes on the classroom episode as it functions in the book.

## docs/curriculum — the build

**`nine_thinking_moves_attribution.md`**
The lineage table. Nine moves, each with a cognitive purpose and a source, the
line running Marton and Tsui → Moore-Anderson → von Duyke, the flag on move 1,
the three coordination structures correctly distinguished, the missing enactment
protocol, and what is distinctly hers stated plainly.

**`deck_work_order_of_operations.md`**
The order the deck work runs in, and what waits on what.

**`the_snake_question_curriculum_case.md`**
The same episode as a curriculum case — the worked case with the decision
withheld.

## prompts

**`deck_inventory_job.md`**
Job 1, read-only, written against the actual file layout.

## What still points at these

`scripts/deck_inventory.py`, `scripts/deck_lint.py` and `scripts/fusion_table.py`
each cite these documents in their headers for the rule they implement. Those
citations were rewritten with the renames; if a document is renamed again, the
scripts need the same pass.

## Which manual is the manual — 30 August 2026

There are three documents with manual-like names, and only one is real.

**The manual** is `Answerable_Teaching_Manual`, doc id
`1kUWjxAnxK1qrTNlmI72ugYYOj85EGRA2gc5M0bwhYZA`, roughly 113k characters. It is
the one Katherine works in, and the whole folder is shared with kvond12, which
is the account that can edit it. The answerableteaching account cannot see it.

Its skills are each one paragraph with soft line breaks (\x0b), not separate
paragraphs, so an insert has to go inside the block or it lands outside the
monospace styling. Compute offsets inside the paragraph and add them to the
paragraph's start index.

Two decoys:

- `Answerable Teaching — Teacher's Manual (draft)`, id
  `1nI8bBqRd0QKPcGUcZwUWVynk_TpCM8s9Qg0KQKekqBE`, at the root of the kvond12
  Drive. Created 30 August. Searching Drive by name returns this one first, and
  it took five edits on 30 August that belonged in the real manual. Its Version
  history has them if they ever need lifting out.
- `Answerable_Teaching_Manual.gdoc` in `06 Answerable Biology — MASTERS (TPT)`
  on the school Drive. The mount cannot read the pointer, so its target is
  unconfirmed. Do not assume it is the same file as either of the above.

**The rule this cost:** find a document by id, not by name search. Where only a
name is known, check `parents` and `owners` before writing to it.
