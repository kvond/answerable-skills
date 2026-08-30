# TPT Drive snapshot — 2026-08-30

A byte-for-byte copy of `My Drive / 06 TPT / TEACHERS PAY TEACHERS (Shared)` as it
stood before it was reorganised, taken so that nothing could be lost in the
reorganisation. 58 files, 8.7 MB.

It is a **record of the before state**. Do not update it to match Drive — if a
later reorganisation needs a backup, take a new dated snapshot beside this one.

## Why it exists

The curated pull earlier the same day took 37 files into `docs/tpt/`. This folder
held 58. Twenty-one of them — the deployed pipeline scripts, the Cowork prompt
set, the pre-migration originals — existed nowhere else.

The `.gitignore` at the repo root ignores `.docx`, `.xlsx`, `.pptx`, `.zip` and
`.gdoc` by extension, which would have silently swallowed most of this folder. The
exception `!docs/tpt-drive-snapshot/**` is deliberate. Do not narrow it.

## What was done to Drive afterwards

**Moved** — 17 files, from `Start here files (shared)` and
`Teacher Facing Docs (public)` (including its `Skills (access removed)`
subfolder), flat into `My Drive / Answerable Biology — MASTERS (TPT)`. Drive keeps
a file's ID across a move, so anything linking to these still resolves.

**Deleted** — 13 Claude skill files superseded by live skills in this repo
(`vt-bio-skill`, `vt-deck-authoring`, `formative-pipeline-v2`, `ste`), three
exact-duplicate `(1)` copies verified identical by checksum, and five folders left
empty. Every deletion was checked against this snapshot first; the script refused
to delete anything it could not find here.

**Kept on Drive** — 24 working records that are not skill files: the MANIFEST, the
deployed pipeline scripts, the TPT listing prompts, the grading references, and
the two spreadsheets named "(do not delete)".

## The limitation this snapshot has

Four files here are Google-native (`.gdoc`, `.gsheet`, `.gslides`, `.gscript`).
On disk those are 191-byte pointers holding a `doc_id`, not the document. **This
snapshot does not contain their content.** Nothing Google-native was deleted, so
nothing was lost — but a backup of this folder is not a backup of those four
documents, and never will be while it is taken from the filesystem. All four are
owned by the school account, not the expiring one.

## The larger problem this surfaced

`MANIFEST_2026-08-09 (answerableteaching).md` indexes the shared drive
`Answerable Teaching TPT` on `kvd@answerableteaching.com`, the account with about
a month left. Its own opening line says every ID in the manifest before it was
dead and had to be replaced wholesale. The same is about to be true of this one.
Anything the start-here documents point at by ID on that account needs re-pointing
before the account closes.
