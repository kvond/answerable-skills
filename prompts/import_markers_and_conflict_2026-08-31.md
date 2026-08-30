# Prompt for a local Claude Code session — re-import all 24 Biology decks

Paste everything below the line into Claude Code, running on Katherine's Mac.

---

## Engine start-up — where things are before you do anything

Check each of these and say what you found. If any is missing, stop and say so
rather than guessing.

| What | Where |
|---|---|
| The repo | `~/code/answerable-skills` — up to date on GitHub (`kvond/answerable-skills`) |
| The 24 finished decks | `~/deck_work/IMPORT_FINAL/IMPORT — Cycle NN FINAL.pptx` |
| The register | `~/code/answerable-skills/docs/decks_live_ids.csv` |
| The procedure | `~/code/answerable-skills/docs/import_runbook.md` |
| School Drive on disk | `~/Library/CloudStorage/GoogleDrive-katherine.vonduyke@redclay.k12.de.us/My Drive` |
| Staging folder | **does not exist yet — you create it, step 1 below** |

The live decks are owned by `katherine.vonduyke@redclay.k12.de.us`. Chrome must
be signed in as that account. If a deck opens **View only** you are on the wrong
account — stop and say so. Do not request access.

## Why every deck needs this, not just some

Two things went into all 24 built files on 30 August and are in **no** live deck:

- **The grading markers.** Every student writing box now carries a hidden
  `[[NOTES:...]]`, `[[DRAFT:...]]` or `[[OPTIONAL:...]]` tag, every Concept Bank
  term carries `[[BANK:...]]`, and slide 1 carries one `[[MARKER-INVENTORY:...]]`
  line. Without these the feedback prompts return nothing, and a class that
  filled in every box reads as a class that wrote nothing.
- **A CRITICAL ASPECTS block on slide 1**, listing the deck's two critical
  aspects verbatim.

And in 13 of the 24, a third thing:

- **A conflict case slide**, sitting between the Concept Bank and the Day 3
  divider. Those 13 are marked `yes` in the `conflict_case` column.

The markers are 1pt white text. **You cannot see them and neither can a
student.** Do not judge an import by whether they appear — judge it by the
slide count, which is what the table below is for.

## Step 1 — staging

The old staging folder was deleted. Create a new one on the school account:

    ~/Library/CloudStorage/GoogleDrive-katherine.vonduyke@redclay.k12.de.us/My Drive/ZZ import staging

Copy all 24 files from `~/deck_work/IMPORT_FINAL/` into it. Then **wait for
Drive for Desktop to finish syncing before starting any import.** A file that
has not synced does not appear in the picker, and a half-synced `.pptx` imports
as a corrupt deck. Delete the folder when all 24 are verified.

## Step 2 — per deck, in this order

1. Read the deck's row in `decks_live_ids.csv`. Note `doc_id` and `new_slides`.
2. Open `https://docs.google.com/presentation/d/<doc_id>/edit`.
3. **Record the current slide count from the filmstrip before touching
   anything.** Call it `N_old`. Every check below depends on it.
4. `File` → `Import slides` → `Google Drive` tab → search the name in the
   `import_file` column → select it → `Select slides` → `All` → **tick
   `Keep original theme`** → `Import slides`.
   Without that tick Google restyles every imported slide to the destination
   theme, which destroys the palette and the type scale.
5. Wait for the filmstrip to settle. **Verify the count is now
   `N_old + new_slides`.** If it is anything else, stop and report. Do not
   delete.
6. Click slide 1 in the filmstrip, scroll to slide `N_old`, shift-click it,
   press `Delete`. That removes the old deck as one contiguous block.
7. Verify three things: the deck has exactly `new_slides` slides; slide 1 reads
   `TEACHER REFERENCE — not projected to students` and carries a
   `CRITICAL ASPECTS` line near the foot; and the order near the end runs
   **Concept Bank → [Conflict case, on the 13] → `Day 3 of 3` divider →
   `TEACHER NAVIGATION — do not project` → Activity and resource links →
   Image credits**.
8. Record: deck key, `N_old`, `new_slides`, final count, conflict case seen or
   not, and anything that looked wrong.

## The expected counts

`new_slides` is the number the deck should have **after** step 6.

| Deck | new_slides | conflict case | Deck | new_slides | conflict case |
|---|---|---|---|---|---|
| Cycle 02 | 35 | yes | Cycle 13 | 33 | — |
| Cycle 03 | 33 | — | Cycle 14 | 33 | — |
| Cycle 04 | 31 | — | Cycle 15a | 33 | — |
| Cycle 05 | 33 | yes | Cycle 15b | 34 | yes |
| Cycle 06 | 35 | yes | Cycle 16a | 39 | yes |
| Cycle 07a | 34 | yes | Cycle 16b | 34 | yes |
| Cycle 07b | 32 | — | Cycle 16c | 35 | yes |
| Cycle 08 | 32 | — | Cycle 16d | 35 | yes |
| Cycle 09 | 40 | yes | Cycle 17 | 33 | — |
| Cycle 10 | 35 | — | Cycle 18 | 35 | yes |
| Cycle 11 | 36 | yes | Cycle 19 | 33 | yes |
| Cycle 12 | 33 | — | Cycle 20 | 32 | — |

The CSV is the source of truth. If it disagrees with this table, follow the CSV
and say so.

## Why the procedure is shaped this way

Google Slides' **Import slides** only *adds* slides. It cannot delete, move or
edit one. So: import the whole finished deck as extra slides, then delete the
old block. The live file keeps its own ID, so every link pointing at it — the
Schoology posts, the `/copy` links, anything in a lesson plan — keeps working
and nothing has to be relinked.

## Rules

- **Do not empty the trash, and do not delete anything outside step 6.** The old
  slides go to the file's own version history, which is the rollback.
- If the extension drops mid-deck, finish the deck you are on before
  reconnecting. A half-imported deck with the old slides still present is safe;
  a deck where the delete ran against the wrong range is not.
- Work through the CSV in order and report after every deck, not at the end.
- Where a slide looks different from what you expected, say so rather than
  assuming the import failed. The live decks and the built files have drifted in
  places before.

## One thing that is not a fault

Cycles 04 through 16b already carry a `CRITICAL ASPECTS` block on slide 1, added
through the Slides API on 30 August. It will be deleted with the old block in
step 6 and the imported deck brings its own. Seeing it before the import is
expected; seeing two after the import is not.

## When you finish

Report a table: deck, `N_old`, final count, conflict case seen, pass or fail.
Then say which decks, if any, you did not complete and why.

Then tell Katherine to ask her other Claude to run the live deck check, which
reads every deck through the Slides API and confirms the markers arrived.
