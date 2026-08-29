# task-distill reference — leftover sweep (culling the raw-import remnant)

Propose-then-delete. The bottom-of-page import remnant (the old `My Tasks` / `ERRANDS` /
`CALLS` / `FINANCE` / `Book Tasks` dumps from the Google Takeout import) is disposable, **but
some of those blocks are the live source behind the Admin Queue embeds** — deleting an
embed-source blanks the embed up top. So the sweep never blanket-deletes; it sorts the remnant
into three buckets and you act on the safe one:

- **Orphans (safe to delete)** — open or done blocks with **no inbound block-reference / embed**
  anywhere in the graph and no unique open work. Listed for one-click removal on your OK.
- **Embed-sources / referenced (must stay)** — blocks that **any `((ref))` or `{{[[embed]]}}`
  points to** (the Admin Queue is full of these). Flagged "keep — referenced by N place(s)";
  never offered for deletion.
- **Loose-but-unique (promote, don't delete)** — open TODOs at the bottom that carry real work
  and are *not* yet represented up top (e.g. the `Book Tasks` PHASE items). Surfaced as
  "promote into the organized layer first," not deleted.

[HARD] Deletion is destructive and confirm-gated per item; the skill only ever deletes from the
**Orphans** bucket, and only after you approve the list.
