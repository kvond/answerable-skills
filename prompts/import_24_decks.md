# Prompt for a local Claude Code session — import the 24 finished Biology decks

Paste everything below the line into Claude Code, running on Katherine's Mac.

---

You are working on Katherine von Duyke's Biology curriculum. There are 24 live
Google Slides decks that students open, and 24 finished `.pptx` files that
should replace their contents. Your job is to get each finished file into its
live deck without breaking any link that points at it.

## Read these first

- `~/code/answerable-skills/docs/import_runbook.md` — the procedure.
- `~/code/answerable-skills/docs/decks_live_ids.csv` — one row per deck: `key`,
  `live_name`, `doc_id`, `import_file`, `new_slides`. This file is the source of
  truth for what to open and what to verify. Do not work from deck names.

The repository is at `~/code/answerable-skills` and is up to date on GitHub
(`kvond/answerable-skills`).

## Where the files are

The 24 finished decks are on disk at:

    ~/deck_work/IMPORT_FINAL/IMPORT — Cycle NN FINAL.pptx

They are **not** in Google Drive. The folder that held them was deleted. Your
first step is to put them somewhere Drive's picker can see:

1. Create `My Drive / ZZ import staging` on the school account
   (`katherine.vonduyke@redclay.k12.de.us`). Its local path is
   `~/Library/CloudStorage/GoogleDrive-katherine.vonduyke@redclay.k12.de.us/My Drive/ZZ import staging`.
2. Copy all 24 files into it.
3. Wait for Drive for Desktop to finish syncing before starting any import. A
   file that has not synced will not appear in the picker, and a half-synced
   `.pptx` will import as a corrupt deck.

Delete that folder when all 24 imports are verified.

## Why the procedure is shaped this way

Google Slides' **Import slides** only *adds* slides. It cannot delete one, move
one, or edit one. Most of what changed in these decks is deletion and
reordering, so importing a few slides would leave a hybrid deck.

So: import the whole finished deck as extra slides, then delete the old block.
The live file keeps its own ID, which means every link pointing at it — the
Schoology posts, the `/copy` links, anything in a lesson plan — keeps working
and nothing has to be relinked. That is the entire reason for doing it this way
rather than uploading a new file and repointing.

## Before you start

- Chrome must be signed in as `katherine.vonduyke@redclay.k12.de.us`. Check the
  avatar at the top right, or the `/u/0/` in the address bar. If a deck opens
  **View only**, you are on the wrong Google account — stop and say so. Do not
  request access.
- Open the Claude side panel from the Chrome toolbar and leave it open. The
  connection drops when it closes, silently.

## Per deck, in this order

1. Read the deck's row in `decks_live_ids.csv`. Note `doc_id` and `new_slides`.

2. Open `https://docs.google.com/presentation/d/<doc_id>/edit`.

3. **Record the current slide count from the filmstrip before touching
   anything.** Call it `N_old`. Every check below depends on it.

4. `File` → `Import slides` → the `Google Drive` tab → search the file name from
   the `import_file` column → select it → `Select slides` → `All` → **tick
   `Keep original theme`** → `Import slides`.

   The tick matters. Without it Google restyles every imported slide to the
   destination theme, which destroys the palette and the type scale.

5. Wait for the filmstrip to settle. **Verify the count is now
   `N_old + new_slides`.** If it is anything else, stop and report. Do not
   delete.

6. In the filmstrip, click slide 1, scroll to slide `N_old`, shift-click it,
   press `Delete`. That removes the old deck as one contiguous block.

7. Verify: the deck has exactly `new_slides` slides; slide 1 is
   `TEACHER REFERENCE — not projected to students`; and near the end the order
   runs **Concept Bank → `Day 3 of 3` divider → `TEACHER NAVIGATION — do not
   project` → Activity and resource links → Image credits**.

8. Record for the report: deck key, `N_old`, `new_slides`, final count, and
   anything that looked wrong.

## What is in the finished decks that is not in the live ones

This is what the import is delivering, and it is what to spot-check:

- **A Concept Bank slide**, immediately above the Day 3 divider — a fourteen-term
  grid with an empty writing box beside each term. No live deck has one.
- **A slide index**, immediately after the Day 3 divider, headed `Slide index`
  under the kicker `TEACHER NAVIGATION — do not project`. It lists only the VT
  questions, in deck order, each with what kind of question it is and Katherine's
  wording verbatim, grouped by critical aspect.
- **Three slide types removed**: `Then and Now`, `Think → Write → Submit`, and
  `Turn your answer into a draft`. If you still see any of those three after an
  import, the delete step in 6 removed the wrong block — stop and report.
- Concept Bank terms capitalised to match the KEY TERMS convention on the
  Bellringer.

Cycle 02 additionally has its corner slide numbers stripped, its `What if?`,
`Optional challenge` and `Relates to me` slides moved above the Day 3 divider,
and its marker inventory corrected. It is the only deck that needed those.

## Rules

- **Do not empty the trash, and do not delete anything outside step 6.** The old
  slides go to the file's own version history, which is the rollback.
- Every deck has full history at `File` → `Version history`. A bad import is
  recoverable — but only if you notice and say so rather than continuing.
- If the extension drops mid-deck, finish the deck you are on before
  reconnecting. A half-imported deck with the old slides still present is safe;
  a deck where the delete ran against the wrong range is not.
- Work through the CSV in order and report after every deck, not at the end.

## Known wrinkle

The live Cycle 12 file is still named `▶ LIVE — Cycle 12 — The Process of
Meiosis (VT deck, rebuilt)`. Katherine renamed the cycle to **Meiosis**. The CSV
maps it correctly by ID; the file name is hers to change or leave.

## When you finish

Report a table: deck, `N_old`, final count, pass or fail. Then say which decks,
if any, you did not complete and why.
