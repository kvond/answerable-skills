# 05 — VT Deck Finishing SKILL

Runs **after** a cycle's VT arc text is final and **before** the deck is handed to
Katherine. Covers images, icons, the slide-type legend, canonical slide order, appendix
slides, and link testing. Sits above `deck_lint.py`, which remains the last gate.

Established 2026-08-06 on Cycle 2 (Ecology / Energy Flow). Standing for every
cycle unless Katherine changes it.

Reference build: `Cycle2_Ecology_Student_Slides_textfixed_model_images.pptx` (34 slides).

---

## 0. Hard prerequisites

- Work on a **real `.pptx`**, never a native Google Slides file. Native Slides
  export as PDF regardless of the MIME type passed, so there are no bytes to edit.
- **Insert into the original deck** so it inherits 10 × 7.5 in. Never build a
  standalone replacement.
- Pull specs and scripts from Drive at run time. Never reconstruct from memory.
- Before/after check on every pass: slide count, slide order, slide dimensions,
  and a shape-by-shape text comparison. Any text difference must be one you
  intended and can name.

---

## 1. Images — clarifying, not decorative

Decks are **not** text-only austere. Every deck gets scattered graphics placed
where they teach.

**Where images go**
- Contrast / case-pair slides (Case A vs Case B) — one image per case, same size,
  same vertical position.
- Definition and category slides — one image per category, in the same left-to-right
  order as the definitions above them.
- Pattern-break slides where the student cannot picture the organism (bee orchid,
  dodder, anglerfish). This is the highest-value placement in the deck: the Pattern
  Break fails if the student cannot see the anomalous case.
- Teaching slides with a real empty band below the text.

**Where images do NOT go**
- Pure question and writing slides stay clean white. The plainness there is
  deliberate and less distracting.
- Never a decorative stock photo on an info slide. If it does not clarify, leave
  the space empty.

**Sourcing**
- Wikimedia Commons only. Public domain and CC0 preferred; CC BY and CC BY-SA
  acceptable with attribution recorded.
- Never news-site photographs (licensed to the outlet or a wire service; a public
  page grants nothing).
- Never AI-generated. Generative models garble biological labels, and a mislabeled
  diagram is worse than no diagram.
- Prefer unlabeled images. A caption that names the category hands the student the
  discrimination the slide is asking them to make.

**Verification, required**
1. Build a contact sheet of every candidate and **look at it** before inserting.
   Search relevance is not depiction: "red-tailed hawk perched" returned a hawk
   two hundred metres away on a rock, useless at 1.9 inches wide.
2. Centre-crop to the target aspect ratio so nothing is distorted. Use a focus
   offset when the subject is off-centre.
3. Render the edited slides and inspect them. No image may touch a writing box.

**Record**
- Capture `LicenseShortName`, `Artist`, `LicenseUrl`, and the Commons page URL per
  image at fetch time. Losing metadata means re-querying later.
- Two outputs: a companion `.md` license table, and a condensed **Image credits**
  slide at the end of the deck.

---

## 2. Icons — Twemoji, one per slide

Small colour accents make the deck friendly without adding noise.

- Source: Twemoji (`jdecked/twemoji`), CC BY 4.0. Rasterize the SVG at 320 px and
  flatten onto white; a transparent PNG can render as a grey box in PowerPoint.
- Placement: top-right corner, 0.55 in, at approximately (8.95, 0.55). Day dividers
  take 0.80 in at (8.60, 0.55).
- Choose an icon that names the slide's content, not a mood: mushroom on the
  decomposer pattern break, flame where energy leaves as heat, crystal ball on the
  What-if, pencil on build-a-rule.
- **Skip any slide where the icon would collide** with a photograph or text. Render
  and check rather than trusting coordinates.
- Credit Twemoji on the Image credits slide.

---

## 3. Corner numbers and the slide-type legend

**Decision (2026-08-06): remove the small grey corner slide-type numbers from all slides.**
They drift out of sequence the moment slides are reordered, and a bare integer tells
a student nothing.

Replace them with one **teacher-facing Slide-type legend slide** listing every slide
in the deck by **deck position** with the kind of slide type it is. Position, not
slide-type number, because position is what the presenter shows.

**Critical constraint.** Do NOT put slide-type names in the corner of student slides.
Workflow A's parser counts diagnostic slides by matching the literal strings
`Critical aspect:`, `Pattern break`, `Finish this sentence as a rule`, `What if?`,
and the three tier labels. A corner label reading "Pattern break" makes the grader
count that slide twice — the same class of bug as the phantom navigation-slide count
fixed in `extract_and_grade.py` on 2026-07-06.

**Therefore the legend slide must carry the banner** `TEACHER NAVIGATION — do not project`,
worded to hit both non-diagnostic exclusion markers exactly. Verify after building:
count each marker across all slides, then again with nav slides excluded. The
excluded count is the one that must match the deck's real slide-type sequence.

Slide-type vocabulary used on the legend: Bellringer · Orientation · Contrast pair ·
Contrast cases · Scale · Critical Aspect intro (phenomenon question) · Interactive
model (stock and flow) · Explanation · Build a rule · Pattern break · Continuation
question · Three-tier concept question · Activity · Day divider · What if ·
Optional challenge · Relates to me · Then and Now · Closing checklist · Rewrite
into a draft.

---

## 4. Canonical slide order

Day 1 and Day 2 run as built. The **end of the deck is fixed**:

1. … What if
2. Optional challenge (harder, not required)
3. **Relates to me** — student-generated relevance
4. **Then and Now** — retrospective self-rating
5. Closing checklist — submit
6. **Turn your answer into a draft** — ALWAYS the last student-facing slide
7. Slide-type legend (teacher navigation)
8. Activity and resource links
9. Image credits

Both reflections are standing and everyone does both. Every slide that asks for
student thinking needs a **response affordance** — the standard writing box,
fill `#F2F6F9`, border `#CCCCCC`. Clone the box from an existing slide rather than
constructing one, so the style cannot drift. Slides that pose questions into empty
space are a defect; the optional challenge and Then and Now both shipped that way
before this rule existed.

Closing checklist wording:
`☐ Submit your notes to Schoology under [activity title] before class ends.`
The bracket stays literal for Katherine to fill per lesson.

---

## 5. Activity and resource links slide

- List every hyperlink in the deck, in deck order: label as a live hyperlink, with
  the bare URL printed underneath in small grey so it survives printing.
- **Link to the resource page, not the homepage.** A homepage link makes students
  hunt.
- Prefer the original source over a repackaging. If only aggregator re-uploads
  (Scribd, Studocu, CourseSidekick) can be found, that is not a source — use the
  credit line printed on Katherine's own copy.

**Link test — required, every build.** Run `deck_link_check.py` against the finished
deck. It walks every run-level hyperlink and reports the HTTP status.

```bash
python3 deck_link_check.py deck.pptx
```

Read the output with judgment: `429` from YouTube is rate limiting, not a dead link;
`URLError` on a bare domain usually means a typo (`biomanbiology.com` → `biomanbio.com`).
Fix and re-run until every line is clean or explained.

---

## 6. Licensing posture

Three different things, and the deck contains all three:
- **Open licence** — reuse, modification, redistribution granted in advance
  (CC / public domain). The images, the icons, and Katherine's own interactive models.
- **Free of charge, proprietary** — BioMan, HHMI BioInteractive. Display and link
  freely; do not republish or redistribute beyond the institution. Some individual
  BioInteractive resources carry a CC licence on their own page — check there before
  modifying one.
- **Free to link** — linking is not use, so it never needs permission.

Because the deck links out rather than embedding, it stays inside every one of these.
The line to watch is any PDF hosted in Katherine's Drive: hosting and distributing
is redistribution, not display, so its provenance must be known.

---

## 7. QA gates before delivery

1. `markitdown` or a text dump — content, order, no placeholders.
2. Text-integrity diff against the source deck; every difference named.
3. Marker counts, with and without the non-diagnostic exclusion.
4. Render the changed slides to images and inspect: overflow, collisions, images
   over writing boxes.
5. `validate.py out.pptx --original src.pptx`.
6. `deck_link_check.py out.pptx`.
7. `deck_lint.py` (Drive `1eh8cG3J1obRsDcaMhBFOhcCwS-d53m58`) — the last gate.
   If Composio is unavailable, **say so and stop**; never reconstruct the linter.
