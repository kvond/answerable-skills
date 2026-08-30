---
name: vt-post-import
description: Pick up each live Biology deck as Claude Code finishes importing it, and run the post-import work on it through the Google Slides API - replace the Day 3 checklist with links to that deck's revision slides, verify the links resolve, and report which decks are imported, which were fixed, and which are still waiting. Idempotent, so it is safe to run repeatedly while an import is in progress. Use when asked to check on the import, to sweep the finished decks, or after Claude Code reports progress. Triggers - "check the decks", "sweep the imports", "post-import", "what has Code finished", "run the deck sweep".
---

# Post-import sweep — the live Biology decks

Claude Code imports the finished `.pptx` decks into their live Google Slides
files one at a time, over hours. This skill does the work that has to happen
*after* an import lands, on whichever decks are ready, and leaves the rest alone.

It is safe to run at any point during an import and safe to run twice. A deck
that has already been swept drops out of the list on its own.

## Why the work cannot go in the `.pptx`

It mostly can, and where it can it should — the sweep scripts do that, and the
import carries it in. This skill exists for the cases where the `.pptx` is
already imported and the change still has to be made, which happens whenever an
edit lands after a deck was staged. On 30 August three decks imported from a
staging copy that predated two edits, and this is what repaired them.

## Access

The live decks belong to `katherine.vonduyke@redclay.k12.de.us`, and the Slides
API connection is **kvond12**, which has editing rights on them. In Composio the
account slug is `googleslides_katha-rusine`. The school account itself is not
connected, and the `answerableteaching` account cannot see these files.

Deck IDs come from `docs/decks_live_ids.csv` in this repo — `key`, `doc_id`,
`import_file`, `new_slides`. Never work from deck names.

## How to tell an imported deck from one that has not been done

Google assigns new object IDs to imported slides. A deck that has never been
imported has slides whose `objectId` is `p1`, `p2`, `p3`… — plain `p` followed by
digits. An imported deck's slides look like `g3f8adb8b078_3_146`.

    imported = not all(s['objectId'][1:].isdigit() and s['objectId'][0]=='p'
                       for s in slides)

Slide count matching `new_slides` in the CSV is corroboration, not proof — a deck
can have the right count and the wrong content.

## The work, per ready deck

### 1. The Day 3 divider

Some decks carry a checklist on the Day 3 divider that tells the student to go
and find her own response slides:

    ☐ Reopen this deck to your response slides — your first answers are already there.
    ☐ On each, open the slide's Notes and copy the revision prompt you find there.
    ☐ Run it in the class AI. Read what it pushes you to reconsider.
    ☐ Write your revised answer in the "Your revised answer" area…

Katherine's decision, 30 August: delete it, and put links to the revision slides
in its place. One line per slide — `Slide 15 — Critical Aspect 1 · <aspect>` —
with the number and dash in bold ink and the label a teal underlined internal
link to that slide.

**Do it by replacing the text inside the existing box.** Do not create a shape.
An earlier attempt to build Concept Bank cells through this API produced shapes
that came back `NOT_RENDERED`, because `shadow` is read-only on a created shape.
`deleteText` + `insertText` + `updateTextStyle` on a box that already exists has
none of that problem.

    deleteText     objectId=<box>  textRange=ALL
    insertText     objectId=<box>  insertionIndex=0  text=<the lines>
    updateTextStyle  per range, fields="bold,underline,fontFamily,fontSize,
                     foregroundColor,link"  style.link={"pageObjectId": <target>}

Teal is `{"red":0.007843138,"green":0.5019608,"blue":0.5647059}`; ink is
`0.06666667` on all three channels. 16pt Arial.

**Not every deck has the checklist.** Cycles 02, 06, 12 and 16a–16d word that
slide differently and must be left alone. Detect the block, never assume it.

### 2. Verify before reporting

Read the box back with `presentations.pages.get` and confirm every line carries
a `link.pageObjectId` matching the slide it names. A `batchUpdate` returning
`successful` means the request was accepted, not that the link points where you
meant.

## Which slides are the revision slides

The slides whose first text run starts `Your answer` or `What if?`. Most decks
have three; Cycle 16a has five and 16b–16d have four. Strip the leading
`Your answer — ` from the label so the line reads as the aspect.

## Report

One row per deck: slide count, imported or not, checklist present or not, number
of revision slides, and what was done. Then the three lists — fixed this pass,
already done, still waiting on the import.

## What this skill does NOT do

- **It does not import.** That is Claude Code, from `prompts/import_24_decks.md`.
- **It does not embed the grading markers.** `NOTES`, `DRAFT`, `BANK` and the
  `MARKER-INVENTORY` line exist in Cycles 02 and 03 only, and the feedback
  prompts return nothing without them. That is a separate job and a larger one.
- **It does not add the teacher note**, which fails `deck_lint` on all 24, or the
  conflict case, which the fusion retrofit has to find in the content first.

Say which of those are outstanding when reporting, so the sweep is not mistaken
for the deck being finished.

## Known wrinkles

- Cycle 04's live divider carried a fifth checkbox, `☐ Don't forget to submit!`,
  that appears in no built file. Live decks and built files have drifted in
  places the offline sweep never saw. Report a difference; do not treat it as a
  failed import.
- LibreOffice renders these links blue, applying its theme hyperlink colour over
  the run colour. Google Slides reads back teal. Trust the read-back.
- A full 24-deck survey is about 13k tokens of response. Use a narrow `fields`
  selector — `slides(objectId,pageElements(objectId,shape(text(textElements(textRun(content))))))`
  — and process it in the workbench rather than inline.
