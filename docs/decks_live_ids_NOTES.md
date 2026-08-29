
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
