
## Manual edits, 30 August 2026 — conflict case

Three passages in `Answerable Teaching — Teacher's Manual (draft)` were changed
so the manual and the decks agree:

- Appendix B, Skill 1: `THE WHAT-IF IS NOT A SLIDE` became `WHERE THE WHAT-IF
  GOES`. The old text said a what-if belongs in spoken dialogue and "never on a
  student slide", which every deck already contradicted - each has a What if?
  slide with two writing boxes. It now says the what-if goes on a slide, with
  its own box, where a conflict case makes it the written evidence that two
  aspects were held together, and stays a spoken suggestion otherwise.
- Appendix B, Skill 3: a `Conflict case` row was added to the slide-type marker
  table. `deck_lint` has matched that string since 29 August.
- Appendix B, Skill 4, PART 1: the completion prompt now knows the conflict
  case adds two writing boxes on thirteen decks, that both are first thinking,
  and that a deck without one is not incomplete.

**Still outstanding.** Prompt 0's readiness check, the `MARKER-INVENTORY`
format, and the `CONFLICT` / `CONFLICT-WHATIF` question ids are not written
yet. They belong with the marker embedding rather than ahead of it, because
the totals they check are set by that job.
