# Slide Layouts

Exact layout, spacing, and generation patterns for each insert slide type. Read this before generating slides.

## Global design rules (Minimalist White Mode)

These apply to every insert slide. Non-negotiable.

- **Slide size: 7.5 × 5.625 in (4:3)** — narrow format
- Background: `#FFFFFF`
- Text: `#000000`
- Font: Arial only
- **Accent (teal): `#028090`** — breadcrumb headers, section titles, label highlights
- **Pattern Break accent (red): `#C0392B`** — used only on Pattern Break breadcrumb headers
- Box fills (optional, pick one if using a box): `#F5F5F5`, `#F2F6F9`, `#FAF9F6`
- Box borders: `#CCCCCC`, thin (0.75pt)
- **Font sizes (calibrated to 4:3 narrow canvas):**
  - Breadcrumb header (top-left, after slide number): 9pt bold, teal (or red for Pattern Break)
  - Section title: 14pt bold (teal for build-arc titles, black otherwise)
  - Main question / question box: 11–15pt bold
  - Tier labels (3-tier slides): 10pt bold — **color-coded, not black** (see below)
  - Tier prompts: 10pt regular black
  - Body / contrast captions: 11–12pt
  - Word bank label: 8pt gray
  - Bracketed word bank terms / hint phrases: 9pt
  - Image captions: 9pt gray
  - Collaboration reminder: 9pt gray, italic optional
  - Slide number: 9pt gray (`#999999`), top-left corner
- Line spacing: 1.15
- Space after each line/bullet
- No sub-bullets, no paragraphs
- Margins: ~0.3–0.4 in
- Images (when used): rounded frames with thin `#CCCCCC` border
- Plenty of writing space — students write on the slide itself

## Tier label colors (HARD RULE — updated 2026-05-27)

On 3-Tier Concept Question slides, tier labels must be **color-coded**:
- `Getting Started` — red `#C0392B` bold, with a small colored rounded square swatch
- `Working On It` — amber `#D68910` bold, with a small colored rounded square swatch
- `Mastery` — green `#1E8449` bold, with a small colored rounded square swatch

**Do not use black for tier labels.** Color-coded is the correct behavior.

## Placeholder removal (HARD RULE — applies to every build script)

When using python-pptx, always strip all placeholder shapes from every new blank slide before adding content. "Click to Add Title" and similar placeholder text boxes are inherited from the slide layout and will show up in PowerPoint if not removed.

```python
def blank_slide(prs):
    """Add a blank slide with ALL placeholders removed."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    for ph in slide.placeholders:
        sp = ph._element
        sp.getparent().remove(sp)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    return slide
```

**This function must be used for every new slide in every build script. Never call `prs.slides.add_slide()` directly.**

## Writing space boxes (HARD RULE)

Every slide that asks students to write must have a proper writing space box:
- Use `#F5F5F5` for question boxes
- Use `#F2F6F9` for writing spaces (visually distinguishes the two)
- Border: `#CCCCCC`, 0.75pt
- Never use loose dashed lines or connector shapes as a substitute

---

## Layout 1 — Bellringer + Agenda (opening slide)

Two-column layout, teal `#028090` accent. Slide is 7.5 × 5.625 in.

**Left column (~55% width, ~0.4 in margin):**
- Small label: "Bellringer" (teal `#028090`, 18pt bold)
- Fun question (12pt, wraps to a few lines)
- Writing space: large blank block below, `#F2F6F9` fill, `#CCCCCC` border, ~3in tall

**Right column (~40% width):**
- Small label: "Today" (teal `#028090`, 18pt bold)
- "Topic" header (9pt bold `#666666`) → topic name (14pt bold black)
- Lab/activity header (9pt bold `#666666`) → placeholder (12pt regular `#666666`) — leave blank for Katherine
- Optional: small school-themed icon or accent in teal

10 minutes allotted in class — the space should feel generous.

## Layout 2 — Critical Aspects List (second slide)

Single-column. Names the critical aspects the lesson will target, so students know what to watch for.

- Title: "What we're looking for today" (14pt bold)
- Short lead-in: "This lesson focuses on:" (11pt)
- 2–4 critical aspects listed, each one line, 12pt
- The collaboration reminder at the bottom: "Think first. Discuss with a partner. Then write." (9pt, `#666666`)

Keep it plain. This is a wayfinding slide.

## Layout 3 — Critical Aspect slide

Simple, narrow, one aspect. This is the "intro" slide that opens a VT arc.

- Breadcrumb header top-left (9pt bold teal): `Critical aspect: [aspect name]`
- Slide number top-left in corner (9pt gray)
- Main question (15pt bold black) — the open inquiry that introduces the aspect, written as a real question students can think about. E.g., "Why bother grouping organisms at all? Couldn't we just learn about each one as we find it?"
- Generous writing space below the question (~2.5–3 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom (9pt gray)

No light-gray box around the question — recent decks keep this slide visually quiet, just typeset on white.

## Layout 4 — Contrast Set slide

Two-column comparison. Images preferred but not required — recent decks use clean text-based contrasts when the comparison is symbolic (e.g., two grouping schemes).

- Breadcrumb header top-left (9pt bold teal): `Critical aspect: [aspect name]`
- Slide number top-left
- **Left column (~45% width):**
  - Column subtitle (11pt bold teal): the framing — e.g., "Way A — group by where they live"
  - Group label (11pt bold black): e.g., "Ocean group:"
  - Group items (11pt regular): the items in that group, space-separated
  - Repeat for second group within the column if needed
- **Right column (~45% width):** same structure, contrasting framing
- **Integration question (12pt bold, full-width row below the columns):** one or two short prompts that force comparison
- Writing space below (~1.5–2 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom

**When using images instead of text contrasts:** two image blocks side-by-side, equal size, rounded frames with thin `#CCCCCC` border, small captions (9pt gray).

## Layout 5 — Build a Rule slide

Student articulates the critical aspect as a rule. Comes right after the Contrast Set.

- Breadcrumb header top-left (9pt bold teal): `Critical aspect: [aspect name]`
- Slide number top-left
- Section title (14pt bold teal `#028090`): "Build a rule from what you just saw"
- Lead-in (12pt black): "Finish this sentence as a rule:"
- Rule frame (14pt bold black, indented slightly), wrapped in quote marks, with a blank to complete:
  - `"A grouping is useful when _______________________________________."`
  - `"DNA gives us better groupings than appearance because _______________________________________."`
- Writing space below (~2.5 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom (9pt gray)

## Layout 6 — Pattern Break slide

A case that breaks the simple rule students just built. The breadcrumb header **switches to red**.

- Breadcrumb header top-left (9pt bold **red `#C0392B`**): `Pattern break  /  Critical aspect: [aspect name]`
- Slide number top-left
- Two side-by-side label blocks (no images required, but supported):
  - Organism / case name (12pt bold black)
  - Trait descriptors below each (9pt regular `#666666`)
- Explanation block (11pt bold black, full width below the two labels)
- The Pattern Break question (12–14pt bold, in a `#F5F5F5` box) — "If [simple rule], why [break]?" structure
- Writing space below (~1.5–2 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom

## Layout 7 — 3-Tier Concept Question slide (closing — load-bearing)

**This is the structural signature for the entire downstream pipeline.** Workflow A detects diagnostic slides by pattern-matching on the three tier labels. Keep the labels exact and on the same slide.

- Breadcrumb header top-left (9pt bold teal): `Critical aspect: [aspect name]`
- Slide number top-left
- Main question (14pt bold black, ~0.5 in from top): the critical aspect restated as a direct question
- **Three tier blocks**, vertically stacked, each:
  - **Tier label** (10pt bold, color-coded — see Tier label colors above):
    - `Getting Started` in red `#C0392B` with red swatch
    - `Working On It` in amber `#D68910` with amber swatch
    - `Mastery` in green `#1E8449` with green swatch
  - **Tier prompt** (10pt regular black, full width): the prompt at that tier's depth
- Word bank label (8pt gray `#666666`): `Word bank (use any, modify any, or use none):`
- Word bank terms (9pt black): bracketed single-word terms separated by triple spaces — `[ classify ]   [ trait ]   [ ancestor ]   [ predict ]   [ related ]` — 4–6 terms total
- Optional hint phrases (9pt black, lowercase, in brackets, on a new line)
- Collaboration reminder at bottom (9pt gray): `Think first. Discuss with a partner. Then write.`

**Tier prompt scaffolding:**

| Tier | Depth | Example |
|---|---|---|
| Getting Started | Concrete recall / example identification, answerable from lesson memory | "Name two animals that look alike but DON'T belong in the same group. Why don't they?" |
| Working On It | Apply the rule — why isn't the simple version enough? | "Why isn't 'looks the same' enough to put two organisms in the same group?" |
| Mastery | Explain the critical aspect with mechanism, causal reasoning required | "If a grouping has to predict things about an organism, what specifically does that grouping have to be based on?" |

**Why the exact labels matter:** Workflow A checks for all three of `Getting Started`, `Working On It`, `Mastery` appearing together on a slide. Renaming, reordering, or splitting these breaks the pipeline.

## Layout 8 — What-If slide (optional, one per lesson)

Standalone, not part of the main five-step sequence.

- Breadcrumb header top-left (9pt bold teal): `What if?  /  Critical aspect: [aspect name]`
- Slide number top-left
- The counterfactual scenario + question (14pt bold black), full width, several lines
- Generous writing space below (~2 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom (9pt gray)

Prefer evolution flavor (trade-offs, variation) where the concept allows.

## Layout 9 — Continuation Question slide (standing, one per lesson, end of deck) [2026-08-06]

Placed after the last 3-Tier Concept Question slide, before the Relates to Me slide. Generative — no answer key, never scored for completion.

- Breadcrumb header top-left (9pt bold teal): `Continuation question:` — verbatim, by itself, no `Critical aspect:` segment
- Slide number top-left
- The question (14pt bold black), full width, several lines — frames this lesson's phenomenon forward toward next lesson's topic (storyline-arc rule, VT_Lesson_Rebuild_Spec.md §7)
- Generous writing space below (~2 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom (9pt gray)

**Non-diagnostic (HARD RULE):** carries the `continuation question:` marker in `deck_lint.py`'s `STANDING_REFLECTION` tuple and `extract_and_grade.py`'s `STANDING_REFLECTION_MARKERS` tuple. Checked before diagnostic classification, the same position as the teacher-nav exclusion — never remove or reword.

## Layout 10 — Relates to Me slide (standing, every lesson, end of deck) [2026-08-06]

Placed last, after the Continuation Question slide. Self-generated connection to the student's own life — the slide lists options, the student supplies the connection.

- Breadcrumb header top-left (9pt bold teal): `Relates to me:` — verbatim
- Slide number top-left
- Lead-in (12pt black): "Pick ONE of this lesson's critical aspects. In your own words, how does it connect to you?" — open, non-leading; never "why this matters" framing
- All of this lesson's critical aspects listed as options (11pt black), each line prefixed `Critical aspect: [name]`
- Generous writing space below (~2–2.5 in) — `#F2F6F9` fill, `#CCCCCC` border
- Collaboration reminder at the bottom (9pt gray)

**Non-diagnostic (HARD RULE):** this slide legitimately contains the `Critical aspect:` string multiple times — one per aspect it lists. The `relates to me:` marker is checked first in both `deck_lint.py` and `extract_and_grade.py`'s classification, before the `Critical aspect:` pattern gets a chance to match — this is what keeps the aspect list from phantom-inflating the completion score, the same bug pattern the old nav slides caused for `pattern_break`. Never omit or reword the marker.

---

## pptxgenjs patterns

Preferred library: `pptxgenjs`. Fallback: `python-pptx`.

**Slide size: 7.5 × 5.625 in (4:3).**

```js
pres.defineLayout({ name: 'CUSTOM', width: 7.5, height: 5.625 });
pres.layout = 'CUSTOM';
```

**Color tokens** (use these exact values, don't improvise):

```js
const COLOR = {
  bg: 'FFFFFF',
  text: '000000',
  muted: '999999',
  caption: '666666',
  boxQuestion: 'F5F5F5',   // question boxes
  boxWrite: 'F2F6F9',      // writing space boxes
  boxWarm: 'FAF9F6',
  border: 'CCCCCC',
  teal: '028090',           // accent — breadcrumbs, section titles
  patternRed: 'C0392B',     // pattern-break breadcrumb AND Getting Started label
  amber: 'D68910',          // Working On It label
  green: '1E8449',          // Mastery label
};
```

**Reusable helpers:**

```js
function addSlideNumber(slide, n) {
  slide.addText(String(n), {
    x: 0.18, y: 0.13, w: 0.4, h: 0.25,
    fontFace: 'Arial', fontSize: 9, color: COLOR.muted,
  });
}

function addBreadcrumb(slide, text, isPatternBreak = false) {
  slide.addText(text, {
    x: 0.55, y: 0.13, w: 6.7, h: 0.25,
    fontFace: 'Arial', fontSize: 9, bold: true,
    color: isPatternBreak ? COLOR.patternRed : COLOR.teal,
  });
}

function addCollabReminder(slide) {
  slide.addText('Think first. Discuss with a partner. Then write.', {
    x: 0.4, y: 5.33, w: 6.7, h: 0.25,
    fontFace: 'Arial', fontSize: 9, color: COLOR.caption,
  });
}

function addQuestionBox(slide, text, { x, y, w, h }) {
  slide.addShape('roundRect', {
    x, y, w, h, fill: { color: COLOR.boxQuestion },
    line: { color: COLOR.border, width: 0.75 },
    rectRadius: 0.05,
  });
  slide.addText(text, {
    x: x + 0.15, y: y + 0.08, w: w - 0.3, h: h - 0.16,
    fontFace: 'Arial', fontSize: 12, color: COLOR.text,
    valign: 'middle', lineSpacingMultiple: 1.15,
  });
}

function addWritingBox(slide, x, y, w, h) {
  slide.addShape('rect', {
    x, y, w, h, fill: { color: COLOR.boxWrite },
    line: { color: COLOR.border, width: 0.75 },
  });
}

// 3-Tier Concept Question — color-coded tier labels with swatch
function addTierBlock(slide, label, prompt, y, tierColor) {
  // Small color swatch
  slide.addShape('roundRect', {
    x: 0.3, y: y + 0.04, w: 0.18, h: 0.18,
    fill: { color: tierColor }, line: { color: tierColor },
    rectRadius: 0.03,
  });
  // Tier label — colored and bold
  slide.addText(label, {
    x: 0.55, y, w: 2.0, h: 0.25,
    fontFace: 'Arial', fontSize: 10, bold: true, color: tierColor,
  });
  // Tier prompt — black regular
  slide.addText(prompt, {
    x: 0.35, y: y + 0.26, w: 6.8, h: 0.55,
    fontFace: 'Arial', fontSize: 10, color: COLOR.text,
    lineSpacingMultiple: 1.15,
  });
}

// Usage:
// addTierBlock(slide, 'Getting Started', 'Name two animals...', 1.4, COLOR.patternRed);
// addTierBlock(slide, 'Working On It',   'Why isn\'t...', 2.25, COLOR.amber);
// addTierBlock(slide, 'Mastery',         'If a grouping...', 3.1, COLOR.green);
```

**Image placement** for Contrast Set (side-by-side):

```js
slide.addImage({ path: leftImgPath, x: 0.4, y: 0.85, w: 3.2, h: 2.5, rounding: true });
slide.addText(leftLabel, { x: 0.4, y: 3.4, w: 3.2, h: 0.25, fontSize: 9, color: COLOR.caption, align: 'center' });

slide.addImage({ path: rightImgPath, x: 3.9, y: 0.85, w: 3.2, h: 2.5, rounding: true });
slide.addText(rightLabel, { x: 3.9, y: 3.4, w: 3.2, h: 0.25, fontSize: 9, color: COLOR.caption, align: 'center' });
```

## Inserting into an existing deck (python-pptx)

pptxgenjs builds new decks, not insertions into existing ones. For inserting into an existing .pptx, use **python-pptx** with direct XML manipulation:

```python
def blank_slide(prs):
    """ALWAYS use this — never call add_slide() directly."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Remove ALL placeholders ("Click to Add Title" etc.)
    for ph in slide.placeholders:
        sp = ph._element
        sp.getparent().remove(sp)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    return slide

def move_slide(prs, from_idx, to_idx):
    xml_slides = prs.slides._sldIdLst
    slides = list(xml_slides)
    elem = slides[from_idx]
    xml_slides.remove(elem)
    xml_slides.insert(to_idx, elem)
```

## Visual QA pass

Before delivery:

1. Convert .pptx to PDF: `python3 /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf <deck>.pptx --outdir /home/claude/`
2. Convert PDF to JPEG thumbnails: `pdftoppm -jpeg <deck>.pdf thumb`
3. Scan every slide for: text overruns, truncated questions, missing writing space, placeholder text ("Click to Add Title"), duplicate questions, font-size drift, wrong teal color, black tier labels (should be color-coded)
4. Fix and re-render if needed

## File naming

Deliver as `<Lesson Name> — Student Slides.pptx` in `/mnt/user-data/outputs/`, then call `present_files`.
