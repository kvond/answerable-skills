# Runbook — importing the finished VT decks into the live Google Slides files

Written 2026-08-29 for a **local** Claude Code session on Katherine's Mac, because
the Chrome extension will not hold a connection from the cloud session.

## What this does, and why it is shaped this way

Each Biology cycle exists twice: as a live Google Slides file the students open,
and as a `.pptx` that has been repaired offline. The repairs are mostly deletions,
reorderings and edits to slides that already exist — and Google's **Import slides**
only ever *adds* slides. It cannot delete one, move one, or change one.

So the route is: import the whole finished deck into the live file as extra slides,
then delete the old slides. The live file keeps its own ID, which means every link
that points at it — Schoology, `/copy` links, anything in a lesson plan — keeps
working, and nothing has to be relinked. That is the entire reason for doing it
this way rather than uploading a new file.

## Before you start

- Chrome must be signed in as `katherine.vonduyke@redclay.k12.de.us`.
- Open the Claude side panel from the toolbar icon and **leave it open**. The
  connection drops when it closes.
- `docs/decks_live_ids.csv` in this repo maps each deck to its live `doc_id`,
  the name of its import file, and `new_slides` - the count to verify against.
- **The finished files are at `~/deck_work/IMPORT_FINAL/`, not in Drive.** The
  Drive folder that held them was deleted on 30 August. Copy all 24 into a
  staging folder in the school My Drive and let it sync before importing;
  `prompts/import_24_decks.md` gives the full instruction.

## Per deck

1. Read the deck's row in `docs/decks_live_ids.csv`. Skip the row if no file
   named in its `import_file` column exists in Drive under
   `03 BIOLOGY (Public) / ZZ Concept Bank source (temporary)`. A missing file
   means that deck has not been swept yet — it is not an error.

2. Open `https://docs.google.com/presentation/d/<doc_id>/edit`.

3. **Record the current slide count** from the filmstrip before touching anything.
   Call it `N_old`. Everything below depends on it.

4. `File` → `Import slides` → the `Google Drive` tab → search the import file's
   name → select it → `Select slides` → `All` → **tick `Keep original theme`** →
   `Import slides`.

   The tick matters. Without it Google restyles every imported slide to the
   destination theme, which loses the palette and the type scale.

5. Wait for the filmstrip to settle, then **verify** the count is `N_old + N_new`.
   `N_new` is the `new_slides` column of that deck's row in
   `docs/decks_live_ids.csv`. If the count is anything else, stop and report —
   do not delete anything.

6. In the filmstrip, click slide 1, scroll to slide `N_old`, shift-click it, press
   `Delete`. That removes the old deck as one contiguous block.

7. Verify the deck now has exactly `N_new` slides and that slide 1 is the
   `TEACHER REFERENCE — not projected to students` slide. Spot-check that the
   Concept Bank sits immediately above the `Day 3 of 3` divider.

8. Report per deck: `doc_id`, `N_old`, `N_new`, final count, and anything that
   looked wrong.

## Rules

- **Do not empty the trash, and do not delete anything outside step 6.** The old
  slides go to the file's own version history, which is the rollback.
- **Do not touch a deck whose import file is missing.**
- If a deck opens `View only`, the session is signed into the wrong Google
  account. Stop and say so — do not try to request access.
- If the extension drops mid-deck, finish the deck you are on before reconnecting;
  a half-imported deck with the old slides still present is safe, a deck where the
  delete ran against the wrong range is not.
- Every deck has full version history at `File` → `Version history`, so a bad
  import is recoverable — but only if you notice and say so rather than
  continuing.

## Known wrinkle

The live Cycle 12 file is still named `▶ LIVE — Cycle 12 — The Process of Meiosis
(VT deck, rebuilt)`. Katherine renamed the cycle to **Meiosis**. The CSV maps it
correctly by ID; the file name itself is hers to change or leave.
