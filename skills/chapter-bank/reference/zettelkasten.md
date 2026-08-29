# chapter-bank reference — the Zettelkasten layer (post Jul 10–11 2026 reconfigure)

Read this file for zettel-sweep mechanics: templates, registry, hub threading, Folgezettel
relations, the harvest pipeline, and topic maps.

## Registration — what "in the Zettelkasten" means

A zettel is registered when it has ALL of:

1. **Canonical form** — claims: `📇 {bare-sentence claim}` title + [[Template - Zettel Claim]]
   body. Concepts: concept-note form (plain title; Type/Core idea/Why it matters/Connections/
   Questions/Source trail — attribute or heading style both live in the graph).
2. **`Meta::`** — `Provenance::` (forced: auctor | grounded), `Index::`, `Origin::` (source page
   + ((block-ref)) + date).
3. **`Index:: [[🌿 Evergreen Notes]]`** — this backlink IS the complete registry. There is no
   list to maintain.
4. Attribute names plain — `Field::`, never `**Field::**` (bold in attribute names mints junk
   pages; a known accident class).

## Selective hub threading (ruled Jul 12 2026, Luhmann architecture)

`[[🗂️ ZettleKasten]]` (note the spelling) holds **entry points, not a registry** — spine claims,
live questions, doorways. Conventions: areas → threads; anchors ❓ question · 📌 claim ·
👁 observation/case · 📓 journal; notes under an anchor carry a role phrase. 📖 = source note
pending migration to its source page. Index-term pages carry selective `Entry points::` blocks.
A thread that ripens toward an article **graduates to its own 📋 structure-note page** (embed
canonical `Claim::` blocks there); the hub stays links-only. Do not thread every new zettel —
propose an entry point only for spine-level notes.

## Folgezettel relations

"Continued by" = **`Refines-into::` / `Extends::`** — never mint a new relation. Full pinned
vocabulary: Supports · Grounds · Extends · Tensions-with · Refines-into · Contrasts-with ·
Depends on · Guarded-by · Resolves · Related (last resort). An IA sequence exists from the
Folgezettel pilot — extend it, don't fork it.

## The harvest pipeline (adjudication is Katherine's)

Existing pages: `[[Zettel-harvest]]` (process) · `[[zettel-harvest state]]` (watermark) ·
`[[zettel-harvest review]]` (queue) · `[[reject-zettel]]` (ruling tag) · `[[Zettel-ID]]`.
Harvest waves surface candidate zettels for **review-in-place**; accepted notes get minted via
the gate. chapter-bank's zettel sweep feeds this pipeline — it does not adjudicate.

## 🧭 Topic maps (legend v4, ruled Jul 13 2026)

- **What they are:** the fifth node kind — a Map of Content. A topic map curates a topic area's
  atoms (zettels · cases · sources · QUEs) and **points, never claims**. Judged by **coverage
  and findability, not correctness**.
- **Template:** [[Template - Topic Map]]. Intro = 2–4 sentences locating the topic (where the
  field splits, where to start reading). Carries `Current as of::` — a topic map is never
  finished, only current; refresh the date when adding pointers.
- **Registry:** every page stamped `Type:: [[Topic Map]]` appears in that page's linked
  references — the backlink list IS the registry. Nothing to maintain.
- **Titling:** new maps = `🧭 {Topic}`, through on_create_check. Grandfathered high-traffic
  titles ([[Democratic Pedagogy]], [[Dialogic Pedagogy]]) keep their names + Type:: stamp until
  Katherine UI-renames them.
- **The extraction rule:** the moment a topic map says something of its own, that sentence is a
  📇 zettel trying to be born — propose extraction through the gate, leave a pointer behind.

## Tooling constraints

- **MCP page rename is broken** (book-ops state, Jul 13 2026). Propose renames for Katherine's
  UI action — UI rename repoints all refs.
- New pages minted live in working sessions get folded into book-ops `vocabulary.json` at the
  next sweep — flag them in the run summary so the sweep catches them.
