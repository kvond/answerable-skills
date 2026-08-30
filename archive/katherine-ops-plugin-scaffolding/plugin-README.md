# katherine-ops

Sixteen skills, one Roam MCP server, and the two Python scripts `manuscript-ops` depends on.

## What is here

**Book — the Answerable Teaching pipeline**

| Skill | What it does |
|---|---|
| `book-ops` | Tag and page vocabulary hygiene for the Roam book graph; the `on_create_check` gate that runs before any page is minted |
| `chapter-bank` | Routes `#Book` captures into chapter banks; the Zettelkasten sweep and registration |
| `manuscript-ops` | Renders reading copies, runs continuity and citation passes, compiles deliverable docx. Never writes prose. |
| `writing-block` | Builds the ≤2-hour Writing Brief; picks one focus chapter and sequences prep → write → place |
| `hep-scout` | Harvard Education Press acquisitions critique, applied to all manuscript feedback |

**Teaching**

| Skill | What it does |
|---|---|
| `formative-pipeline-v2` | Conceptual Growth Reports from annotated decks; class summary, agency coding, integrity gate |
| `activity-scout` | Monthly opportunity calendar scored against the life-design spec |

**Daily operations**

| Skill | What it does |
|---|---|
| `daily-brief` | The single morning page — A/B day, bell schedule, Gmail pass, Roam stamp |
| `daily-route` | Routes untagged daily-page blocks to their owning skills |
| `task-distill` | Rebuilds `[[📋 TASKS]]` as an ordered area → month → day view |
| `block-update` | Status-only refresh for the AIHS or WilmU block |
| `learning-block` | Spanish, voice, and ukulele practice slice |
| `daily-agenda` | Deprecated; superseded by `daily-brief`. Carried here so nothing that references it breaks. |

**Household and archive**

`photo-album-reconcile`, `wegmans-grocery-order`, `panama-grocery-order`.

## The scripts

`manuscript-ops` calls two Python scripts by relative path. Until now the skill declared them as built while shipping without them, so any run reaching the render or consistency step failed on a missing file. They are bundled here:

- `skills/manuscript-ops/scripts/render_reading.py` — Roam export → clean reading prose. Strips brackets, workflow tags, components, block refs, attributes, highlights; flattens bullets to paragraphs; keeps headings, bold, italics.
- `skills/manuscript-ops/scripts/check_consistency.py` — extracts chapter cross-references, vague back-references with no number, and every tracked-term occurrence with context. Extraction only; Claude adjudicates.
- `skills/manuscript-ops/tests/sample_chapter.md` — the fixture both were developed against.

Both are standard library only, no dependencies. Verified running under Python 3 at package time:

```
python3 scripts/render_reading.py    --in tests/sample_chapter.md
python3 scripts/check_consistency.py --in tests/sample_chapter.md
```

`check_citations.py` is still marked **planned** in the skill. It is not written, and there is no `sources.json` for it to run against — `Answerable Teaching/References` in Roam is the material a manifest would be built from.

## The Roam connection

`.mcp.json` declares the Roam MCP server ([`roam-research-mcp`](https://github.com/2b3pro/roam-research-mcp)), which is the one whose tool names the skills already use — `roam_fetch_page_by_title`, `roam_import_markdown`, `roam_process_batch_actions`, `roam_datomic_query`, `roam_remember`.

It reads two environment variables:

| Variable | Purpose |
|---|---|
| `ROAM_API_TOKEN` | Roam graph API token |
| `ROAM_GRAPH_NAME` | Defaults to `kvond` if unset |

Set them in your shell profile or a `.env` file. Do not commit the token — `.gitignore` excludes `.env`.

Gmail, Google Calendar, and Google Drive are account connectors rather than plugin-declared servers, so they are authorized once in Cowork and are not carried in this repo. See `CONNECTORS.md`.
