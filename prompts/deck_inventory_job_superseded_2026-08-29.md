# Claude Code — Job 1: Deck Inventory (read-only)

Paste this into Claude Code. Fill in the two paths first.

Prerequisite: Google Drive for Desktop installed and synced, so the cycle
folders exist as real files on disk. Your source of truth is `.pptx`, which syncs
as real bytes. Native Google Slides files sync as pointer stubs with no content
and are not usable here.

---

## The prompt

```
Read ~/.claude/skills/vt-bio-skill/SKILL.md first. It defines the 5 core
questions, the slide types, the marker strings, the format tokens, and the
.pptx twin test that identifies a live deck. Follow its vocabulary exactly:
these are "core questions" and "slide types". The word "beat" is not used.

Also read ~/.claude/skills/vt-fusion-retrofit/SKILL.md for the definitions of
separation, fusion, synchronic and diachronic simultaneity, and the three
coordination structures.

TASK: Build a read-only inventory of every live Biology cycle deck.

Root: <PATH TO SYNCED BIOLOGY FOLDER>
Output: <PATH FOR OUTPUT>/deck_inventory_YYYY-MM-DD.csv plus a readable
summary at the same path.

THIS JOB WRITES NOTHING BUT THOSE TWO FILES. Do not modify, move, rename, or
delete any deck. Do not create backups. Open every .pptx read-only.

Use python-pptx. Install it if needed.

For each cycle folder:

1. Apply the .pptx twin test from vt-bio-skill §0 to identify the live deck.
   Record which decks are CORE and which are EXTEND. Note any cycle folder
   with no .pptx at all — expect Cycle 01 (Lab Safety) and Cycle 13.

2. For each live deck record:
   - cycle number, deck filename, CORE or EXTEND, slide count
   - the ordered list of slide types you can identify, by title text and by
     the marker strings vt-bio-skill specifies
   - which of the 5 core questions are present, and for which critical aspect
   - Continuity question present? (yes/no)
   - Stock-and-flow model present? (yes/no)
   - Concept Bank present? position relative to the Day 3 divider
   - Teacher Prep slide present? (yes/no)
   - response slides present? do their speaker notes carry the revision prompt?
   - links slide present? how many links, and how many are /copy vs /edit,
     /view, or /edit?usp=sharing
   - format check: slide dimensions 4:3, fonts used, hex colors used

3. Two additional checks, both advisory:

   a. MOVE 1 CARRIES A DIFFERENCE. Read the text of the Critical Aspect
      question slide. Does it contain a comparison, a choice between named
      alternatives, or a stated change condition? A question that names the
      aspect and leaves the contrast to the next slide is structurally "how
      are polar bears adapted?" and produces silence in a room. Record
      yes/no and quote the question text so I can judge the borderline ones.

   b. COORDINATION. Does the deck contain any slide where two critical
      aspects must be held together to answer? Record which structure if so
      (stock-and-flow / compensatory pair / conflict case), or "none".
      Do not judge whether one SHOULD be there. Only record what is there.

4. Emit the CSV with one row per live deck, and a readable summary that
   answers:
   - which cycles are missing a required slide type
   - which links slides have non-/copy links
   - which decks fail a format token
   - the distribution of coordination structures across the arc
   - which decks fail check 3a

Do not propose fixes. Do not edit anything. Report only.

When you are done, tell me the count of live decks found and whether it
matches the 24 decks in 19 folders that vt-bio-skill §0 expects.
```

---

## Two things to fill in

- `<PATH TO SYNCED BIOLOGY FOLDER>` — the local path once Drive for Desktop is
  syncing. Usually under `~/Library/CloudStorage/GoogleDrive-<account>/My Drive/`.
- `<PATH FOR OUTPUT>` — somewhere outside the synced folder, so a partial write
  never syncs back.

## Why this job first

Four things wait on it: the linter rules, the retrofit skill's diagnostic logic,
the fusion table across the arc, and the NGSS coverage question. All four are
currently guesses about what is in the decks.

It also touches nothing, which makes it a safe first use of the tool.
