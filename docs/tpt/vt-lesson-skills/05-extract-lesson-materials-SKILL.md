---
name: extract-lesson-materials
description: Extracts structured lesson materials — vocabulary with definitions, critical aspects, and causal chains — from a Google Slides lesson deck and produces a polished, formatted Word (.docx) document. Use this skill whenever a teacher uploads or links a lesson deck (especially VT Insert slides, biology or science units, or any structured instructional presentation) and asks to extract content, pull vocabulary, document key concepts, build a reference doc, make materials for Cowork to use, or create a study guide. Trigger even if the user phrases it casually — "pull the vocab", "grab the key ideas", "make a doc from this deck", "extract the lesson stuff", or "do the same as before for this one."
---

# Extract Lesson Materials

Reads a lesson deck (Google Slides) from Google Drive, extracts all vocabulary terms with definitions, Critical Aspects with student prompts and explanations, and causal chains showing the if-then logic of the content. Outputs a structured, styled Word document (.docx).

## When to Use

- Teacher links or references a Google Slides lesson deck
- User asks to extract vocab, key concepts, critical aspects, or causal chains from a lesson
- User says "do the same as before for this one" — referring to a prior extraction run
- User wants a reference doc, study guide, or Cowork-ready summary of a lesson deck

---

## Step 1 — Get the File

### If the user provides a Google Drive URL:
Extract the file ID from the URL. Examples:
- `https://drive.google.com/file/d/FILE_ID/view` → use `FILE_ID`
- `https://docs.google.com/presentation/d/FILE_ID/edit` → use `FILE_ID`
- Folder URL → search for the target file with `parentId = 'FOLDER_ID'`

Use the **Google Drive: download_file_content** tool with `exportMimeType: "text/plain"` to get the slide text. The result will be base64-encoded — decode it in bash:

```bash
echo "BASE64_STRING" | base64 -d
```

### If the user provides a file ID directly:
Use it as-is with `download_file_content`.

### If the deck is already in context (from a prior folder scan):
Use the `contentSnippet` already retrieved — but if it was truncated, fetch the full content with `download_file_content`.

---

## Step 2 — Parse the Content

From the decoded text, identify and extract:

### Vocabulary Terms
Look for slides labeled "Key Vocab", "Vocab", or definitions introduced with a dash (e.g., `Chromosome - A condensed DNA molecule...`). Also extract terms defined inline in recap or intro slides.

For each term capture:
- **Term** (the word or phrase)
- **AKA / Symbol / Phase** (alternate names, symbols like `2n`, or phase context like "Meiosis I, Phase 2")
- **Definition** — complete, student-friendly, including examples and sub-points if present

### Critical Aspects
Look for slides whose breadcrumb header reads **`Critical aspect: [name]`** (lowercase "Critical aspect" followed by a colon and the aspect name). This format is produced by the `vt-insert-slides` skill and appears on five slide types per VT arc:

- Critical Aspect intro slides (open inquiry — the first slide of each arc)
- Contrast Set slides
- Build a Rule slides (section title: "Build a rule from what you just saw")
- Pattern Break slides (header switches to red, prefix `Pattern break  /  Critical aspect: ...`)
- 3-Tier Concept Question slides (closing slide of each arc — carry `Getting Started`, `Working On It`, `Mastery` labels)

The **same critical aspect name repeats across all five slides in one arc** (e.g., all slides in Arc 1 say `Critical aspect: Why we classify`). De-duplicate when extracting — each lesson has 1–3 critical aspects, not 5–15.

For each Critical Aspect capture:
- **The exact wording** (the aspect name from the breadcrumb)
- **The open inquiry** from the intro slide (the 15pt bold question that opens the arc)
- **The student thinking prompt** — the main question from the 3-Tier Concept Question slide (the most polished phrasing of the critical aspect as a question)
- **Why it matters** — a 2–4 sentence explanation of the conceptual significance, written at teacher level
- **The Mastery-tier prompt** from the 3-Tier slide — this is the most distilled version of what mastery of the critical aspect looks like in student writing

### Legacy format note
Older decks used `CRITICAL ASPECT` (all caps) headers or `Focus: [title]` framing. The skill should still recognize these patterns for backward compatibility, but assume new decks use the lowercase `Critical aspect: [name]` breadcrumb format produced by current `vt-insert-slides`.

### Compare / Contrast Slides
Two patterns to recognize:
1. **VT Contrast Set slides** (current format from `vt-insert-slides`) — two-column layout, each column with a teal subtitle naming the framing (e.g., "Way A — group by where they live" / "Way B — group by how they're related"). Treat each Contrast Set as supplementary detail under its associated Critical Aspect — not a separate aspect.
2. **Compare slides** (older format) — slides labeled **"Compare: X vs. Y"** or **"After X vs. After Y"** function as embedded critical aspects. Extract them as a named distinction with a two-column summary and the associated student prompt.

### Causal Chains
Look for:
- Slides labeled "Wait — ..." or "But wait..." — these introduce productive contradictions or causal resolutions
- "Put It All Together" synthesis slides
- Sequential phase slides (Interphase → Prophase → Metaphase → ...) that together form a process chain

For each causal chain, identify 3–5 named steps with a label and a 1–3 sentence explanation per step. The final step should always be marked as the resolution or conclusion (fill: green).

### Comparison Tables
If the deck contains a **Mitosis vs. Meiosis** or similar comparison table, extract it verbatim as a structured table.

---

## Step 3 — Generate the Word Document

Install docx if needed: `npm install -g docx`

Use the **docx** npm library to produce a `.docx` file. Follow all rules from the docx skill (US Letter, DXA widths, no unicode bullets, ShadingType.CLEAR, etc.).

### Document Structure

```
Title block (deck name, subtitle, source)
Section 1: Vocabulary & Definitions   → styled table, alternating row fills
Section 1B: Phase Reference Table     → if deck covers sequential phases
Section 1C: Comparison Table          → if deck contains a comparison (e.g., Mitosis vs. Meiosis)
Section 2: Critical Aspects           → one heading2 per CA; box with the open inquiry, the polished question from the 3-Tier slide, the Mastery-tier prompt (as a marker of what mastery looks like), and "Why it matters"
Section 3: Causal Chains              → one heading2 per chain; step-box layout with arrows
```

### Color Scheme
Pick an accent color that is **different from any prior deck** in the same unit — so documents are visually distinguishable when used side by side. Suggested palette:

| Deck | Accent |
|------|--------|
| Introduction / Deck 1 | `2E4D7B` (navy blue) |
| Process / Deck 2 | `5B2C6F` (deep purple) |
| Deck 3+ | `1E8449` (green), `A04000` (amber), etc. |

### Key Styling Rules
- **Vocab table header**: accent color background, white text, 3 columns (Term | AKA | Definition)
- **Critical Aspect box**: light tint of accent color background, `CRITICAL ASPECT` label in small caps, bold statement lines
- **Causal chain steps**: light tint rows with `▼` arrows between steps; final step gets green fill (`D5F5E3`)
- **Compare tables**: two-column, each column header in its own accent color (e.g., blue for mitosis, purple for meiosis)
- Always use `WidthType.DXA` — never `PERCENTAGE`
- Always use `ShadingType.CLEAR` — never `SOLID`

### Output Path
Save to `/home/claude/`, then copy to `/mnt/user-data/outputs/`. Name the file clearly:
`[topic]_vocab_critical_aspects.docx`

---

## Step 4 — Present the File

Use `present_files` to deliver the `.docx`. Follow with a brief summary of what was extracted:
- Number of vocabulary terms
- Number of Critical Aspects (and their titles)
- Number of Causal Chains (and what each one traces)

---

## Notes & Edge Cases

- **Truncated snippets**: If `contentSnippet` from a folder scan is cut off mid-slide, always fetch the full file with `download_file_content` before extracting.
- **Multiple decks in one session**: Keep color schemes distinct per deck. Check what color was used in prior runs.
- **RECAP slides**: Terms re-introduced in RECAP slides from a prior deck should still be included with a brief note (e.g., "carried from Deck 1") — don't silently drop them.
- **Implied causal chains**: Not all chains are explicitly labeled. Sequences of phase slides (Prophase I → Metaphase I → ...) or "But wait..." slides that resolve a prior contradiction should be captured as chains even without a label.
- **"Put It All Together" word banks**: These synthesis prompts reveal which terms the deck considers load-bearing. Note them at the end of the relevant causal chain as the synthesis vocabulary.
- **Page breaks**: Never needed for this document type — let content flow naturally.
