# book-ops reference — MCP fallback · apply mechanics · question extraction · quarantine

## Roam MCP fallback (inventory without the API token)

Run the same queries (constants at the top of `roam_pull.py`) through `roam_datomic_query` and
assemble the identical `inventory.json`. Two rules that keep MCP results inside token limits:

- **Exclude dailies server-side** with a `not` clause:
  `(not [(clojure.string/includes? ?title ", 202")])`
- **Batch lookups with `or`** — backlink counts for ~40 named titles per query
  (`(or [(= ?title "A")] [(= ?title "B")] …)`) instead of pulling the full edge set.

If a result still overflows to a dump file, page through it with offset/limit grep — but treat
that as a signal to push more filtering into the query.

## Apply (approved items only)

- **Merges** — Roam has no native merge. Repoint every `[[loser]]` reference to the canonical
  title, then stub or alias the loser page.
- **New `QUE —` pages** — create and place under the chapter structure note.
- Update `alias::` on `[[book-ops state]]` with approved aliases, and append one line per change
  to the run's section on `[[book-ops review]]`.

Snapshot rule from SKILL.md applies: export the graph (or confirm the git `source/` snapshot is
current) before applying ANY merge.

## Question extraction (full-sweep companion, or on request)

Read the critique pages — `[[Addressing Criticisms]]` (primary), `[[Beyond Motivation — the
active book's conceptual core.]]`, `[[Author Block - finishing Map]]`,
`[[Anthropic prospectus]]`, `[[Book Summary]]`. For each criticism or unresolved spot, draft a
`QUE — …` title naming the open question. Run each drafted title through the **on-create check**
BEFORE proposing it. Add survivors to `[[book-ops review]]` as proposed creations, each linked
to the chapter or spot it came from.

## Quarantine enumerator — untyped / orphan pages

Finds the non-duplicate failure: **untyped or orphaned** pages (no `Type::`, ≤1 backlink).
Produces a **quarantine list, never a deletion [HARD]** — surfaced for the daily visual glance;
some entries are seeds, some typos with real backlinks, some duds; only the user's eye tells
them apart. Default retrieval (on-create checks, lookups) excludes quarantined pages;
`--search-wide` pulls them back in. Known reconcile-candidates (duplicate `Chapter 9`,
`NEW chapter 2 insert`, lowercase `Answerable teaching/Chapter 5`) are a chapter-bank manifest,
not duds — the enumerator lists them as already-known and never quarantines or merges them.
`daily-route` handles the block-level half of the same leak; the two report into the same
morning glance.
