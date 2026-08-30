
## Cycle 12b — a create, not an import (2026-08-29)

Katherine confirmed 12b has **no live Google Slides deck yet**. It therefore has
no ID to preserve, which is the only thing the import route buys, so it has been
removed from `decks_live_ids.csv` rather than left blocked there. The two
candidate presentations found earlier were old builds, not a live deck.

The route for 12b is: upload the finished `.pptx` to Drive, open it as Google
Slides, and that new file's ID becomes the one to protect from then on. Add the
row to `decks_live_ids.csv` at that point, and every later repair goes through
the normal append-then-delete import so the ID never changes again.

Nothing else in this file needs to change.

## `google_native` — added 30 August 2026

A deck with anything in this column has native Google Slides work in it -
transitions, animations, embedded video, images or shapes added in Slides,
speaker notes typed there, comments. **Never full-re-import a deck marked
here.** The import route deletes the old block of slides, and everything in
that list is attached to a slide, so it dies with them.

Changes to a marked deck are made one of two ways, neither of which deletes
anything: Slides API edits in place, or an append-only import of just the new
slides followed by `updateSlidesPosition`.

Put the date in the cell, so it is clear when the work went in.

## `conflict_case` — added 30 August 2026

`yes` means the deck carries a conflict case slide between its Concept Bank and
its Day 3 divider, and `new_slides` has been raised by one to match. `none`
means the diagnosis found no genuine conflict in that cycle's content — see
`audits/conflict_cases_2026-08-30_v2.docx` for the reason, which belongs on
that deck's teacher note slide rather than in this file.

The thirteen decks marked `yes` need one more import, because a slide cannot be
added faithfully through the Slides API: element size is fixed at creation and
there is no resize request, so a duplicated shape can be moved but not made
taller. Recreating it loses the shadow the writing boxes carry. Re-importing
costs nothing today because no deck yet holds native Google work; once one
does, this stops being true and that deck's `google_native` cell says so.

## Marker totals — added 30 August 2026

`notes`, `draft`, `optional` and `bank_terms` are copied from each deck's own
`[[MARKER-INVENTORY]]` line, so the register and the deck cannot disagree
without it showing here. `scripts/embed_markers.py` writes both.

Two facts about that script worth keeping. A student writing box is identified
by its fill, `F2F6F9`, and nothing else: the drag activities are full of empty
filled boxes that are drop zones, and Cycle 17 has eleven of them. Counting
those took its NOTES denominator from 15 to 29, which would have marked every
student in the class too low with nothing in the report to say why. And the
BELLRINGER, WHATIF, CONFLICT and OPT blocks name one slide each; only the
aspect block carries forward, or Cycle 09's seven lab slides inherit WHATIF.

The derivation was validated against Cycles 02 and 03, which were marked by
hand in August: it finds the same slides, one for one.
