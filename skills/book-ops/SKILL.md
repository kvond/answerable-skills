---
name: book-ops
description: "Tag/page vocabulary hygiene for the Roam book graph: dedup sweeps (delta or full), QUE-- question extraction, and the mandatory on_create_check gate that runs before minting ANY book- graph page. Triggers: \"dedup\", \"tag sweep\", \"book-ops\", tag inventory, or before creating any page in the book graph."
---

# Book-Ops — Vocabulary Cleanup, Dedup & Question Extraction

Keeps the book graph's vocabulary honest. Scope: **concept/definition pages** + **question pages**
(`QUE — …`, em-dash). **PROPOSE-THEN-APPLY**: reads the whole graph, never merges/renames/creates
on its own — review surface → user adjudicates → only approved changes written. A false merge
silently destroys a distinction (worse than a missed duplicate), so the pipeline is tuned for
recall + human confirmation. **Roam is canonical.** Git `source/`/`writing/` export and the
daily-brief finishing map are out of scope.

## Reference file — load on demand

`reference/extras.md`: Roam MCP fallback for inventory pulls (no API token), apply mechanics for
approved merges/creations, question extraction, quarantine enumerator. The nightly delta run
needs none of it.

## Three modes

| Mode | When | Cost | Script |
|---|---|---|---|
| Delta sweep | nightly scheduled run | O(new) | `scripts/delta_sweep.py` |
| Full sweep | one-time migration + ~monthly safety net | O(all pairs) | `scripts/dedup_sweep.py` |
| On-create check | before minting ANY page, forever | O(1) | `scripts/on_create_check.py` |

Never run the full sweep nightly — whole-graph cost + re-surfaces adjudicated items; it stays
the monthly net for drift the delta model can't see.

## Bundled scripts — run them, never re-implement the matching by reasoning

Same inventory → same candidates every time; judgment enters only at layer 5 + review.

- `scripts/matching.py` — shared normalization/fuzzy/citation/alias/pin logic; edit matching
  HERE so modes never drift. All others import it.
- `scripts/roam_pull.py` — builds `inventory.json` (schema at its head = the downstream contract).
- `scripts/delta_sweep.py` — nightly; needs `--watermark` (epoch ms).
- `scripts/dedup_sweep.py` — full sweep, ranked candidates + quarantine.
- `scripts/on_create_check.py` — one title vs the set; `clear` or top-k neighbors.
- `scripts/roam_bulk_write.py` — idempotent batch block writes via the backend API; see the
  write-path section below.

Citation variants (curly/straight quotes, trailing periods, ellipses, `@Author`) are caught
deterministically by `norm_citation()` (surname+year keys) — never eyeball citations (the
Matusov-2011 residue class).

## Inventory

**Backend API preferred:** export `ROAM_GRAPH` + `ROAM_API_TOKEN` (token page:
`[[Local API Token: book-ops read]]`), run `roam_pull.py` — one HTTP pull, graph never enters
model context, matching runs locally. No token → MCP fallback in `reference/extras.md`.

**Skip-pull shortcut:** before pulling, run `DELTA_Q` (in `roam_pull.py`) with the stored
watermark. No non-daily rows → graph unchanged → log "no delta" on the review page and stop.
Most nights this is the whole run.

⚠ **A stale inventory is a broken gate, not a slow one.** On Aug 1 2026 `on_create_check` passed
a duplicate practice-gap title as `clear` against an inventory holding 250 📇 pages against 304
live. Rebuild before any run that may mint. If the token is missing and the MCP fallback is in
use, say so in the run summary — four consecutive distills (Jun 27, Jul 6, Aug 1, Aug 2) recorded
the same caveat and it read as boilerplate rather than as a gate that was not running.

## Roam write path — the MCP is not the first choice [HARD]

`roam_process_batch_actions` hangs mid-run without warning (Aug 3 2026: a 9-action batch timed
out, reads failed for ~60s, then the connection recovered with nothing restarted). The stall is
in the MCP layer, not Roam's API. **The hang is survivable; the retry is not** — a blind re-run
duplicates every block in the batch, and Roam has no undo for that.

- **Preferred:** `scripts/roam_bulk_write.py` with `ROAM_GRAPH` + `ROAM_API_TOKEN` set. It asks
  whether each block already exists under its parent before creating it, so re-running the same
  actions file is safe by construction. `--verify` reports what landed without writing;
  `--dry-run` plans without writing.
- **Falling back to the MCP:** never blind-retry a timed-out batch. Read the target parent
  (`roam_fetch_block` on the parent uid) and confirm what landed first. Keep batches to around 3
  actions — not because size is the proven cause (an 11-action batch landed minutes before a
  9-action batch hung) but because a small batch is cheap to verify and cheap to redo.
- **Report any stall in the run summary**, with what was verified before retrying. A silent
  recovery hides a degrading connection until it costs a page.

## State lives in Roam — `[[book-ops state]]`

- `watermark:: <epoch ms>` — read at start, updated at end.
- `flagged::` — one pair-key per child (`pair_key()`: normalized titles sorted, `|`-joined);
  already-surfaced pairs never re-flagged (approved merges can't recur; rejected pairs not
  re-proposed).
- `alias::` — approved `alias → canonical` lines → fed into `vocabulary.json` at start.
- Pinned never-merge pairs on `[[never_merge registry]]` — read every run into `never_merge`.

At start, rebuild `vocabulary.json` from `[[🏷️ TAGS]]` + state aliases + never_merge registry —
three cheap fetches; no file survives between sessions.

## Nightly delta run

1. Read `[[book-ops state]]` (watermark, flagged) + `[[never_merge registry]]` + `[[🏷️ TAGS]]` →
   `vocabulary.json`.
2. `DELTA_Q` with watermark; no non-daily changes → "no delta" line, stop.
3. Pull inventory (API preferred); run `delta_sweep.py`.
4. Layer 5 (semantic), delta's new titles ONLY: conceptual duplicates with no surface overlap
   ("student agency" vs "learner autonomy"), one-line reasons; proposes only, never collapses.
5. Write findings to `[[book-ops review]]` (new section, top). Daily note gets ONE pointer line
   only — never the candidate list:
   `🏷️ book-ops: auto-applied N · open M (your call) → [[book-ops review]] · archived K`
   (counts from state, not the block list). Add surfaced pair-keys to `flagged::`; update
   `watermark::`.
6. **Auto-apply policy — two tiers.**

   **Auto-apply (no confirm)** — reversible, no distinction lost:
   - Tag/citation normalizations to canonical `[[🏷️ TAGS]]` on **non-structural** blocks. A bare
     `[[TAG]]` section header on a system page ([[📋 TASKS]], banks, launchers) is structural —
     other skills may key on it — demote to review.
   - Alias-locked repoints (pair already on `alias::`): repoint refs + stub the loser — already
     ruled; re-confirming is friction.
   - Quarantine of 0-backlink stubs (never deleted).

   **Gated (confirm) [HARD]:**
   - New concept-page merges not yet in `alias::`.
   - `QUE —` mints and CLM/EVD promotions (chapter-bank / on_create_check gate).
   - Anything touching a template/convention (e.g. the `Spanish::` habit-stamp).

## Safety — snapshot before gated applies

Before applying ANY gated merge: export the graph (or confirm git `source/` holds a current
snapshot) — gated merges repoint refs and delete the loser; the snapshot is the only restore
point. The auto-apply tier uses reversible repoint→stub (no hard deletes) — no export needed.
Re-running pull/sweep stages is always safe (report files only, never the graph).

## 🛑 STOP-AND-CONFIRM

No gated merges, renames, or creations until the user reviews `[[book-ops review]]`. Per item:
merge candidates (both titles, layer + score, backlink counts, recommendation: merge → which
canonical / keep separate / make-alias); proposed `QUE —` pages (title, source critique,
near-neighbors). Default keep-separate when in doubt — a split is recoverable, a merge is not.
Scheduled autonomous runs never reach gated apply: they stop at the review surface, applying
only the auto-apply tier.

## Pinned no-merge guard [HARD]

Same word at two levels must never be offered as a merge, however hard layers 1–3 collide it.
Registry `[[never_merge registry]]` → vocab `never_merge`; pins reported as related-but-distinct,
merge suppressed. Current pins: `Auctor` ✕ `auctor` (Provenance:: value), `Auctor` ✕
`[[Authorial-Agency]]`, `family` ✕ `FAMILY`. A `::` attribute value and a same-named concept
page are different node kinds, never the same atom. New pins on the user's ruling only.

## `Final:` supersession guard (ruled Aug 7 2026)

Revised manuscript sections are posted as new blocks prefixed `Final:` alongside the superseded
draft blocks, which stay in place as zettelkasten link targets — chapter-bank holds the full
rule. For book-ops this means: a `Final:` block colliding with its unprefixed counterpart on the
same page is **deliberate duplication** — suppress it, never surface it as a merge/dedup
candidate, and never quarantine or stub the superseded blocks. If a `Final:` section is later
promoted to its own page, an `on_create_check` collision with the old draft's page title is
expected supersession — surface it as "supersedes <old>," not as a merge candidate. First
instance: the Preface on the Answerable Teaching page (Aug 7 2026).

Same suppression for `Draft:`-headed trees (ruled Aug 7 2026): a `Draft:` parent on a chapter
page marks a rewrite in progress beside the frozen old prose — the collision is deliberate, so
never surface Draft-vs-old as a dedup/merge candidate, never quarantine or stub either side,
and never treat the `Draft:` tree's sentences as mintable candidates. On settlement Katherine
edits the prefix to `Final:` and the `Final:` rule above takes over.

## Archive exclusion + API renames (2026-07-29)

- `🗄 Archive/` pages and pages stamped `Status:: archived` are excluded from inventory,
  matching, and merge proposals — archives are provenance, never candidates (Decision 5 lineage).
- Page renames: the MCP rename tool remains broken — never use it. Roam UI rename or backend-API
  `update-page` (bulk-ops path, validated 2026-07-29 — repoints refs) are both safe. API renames
  end with the verification protocol: old title gone · refs carried · zero stale literal strings.

## Outputs

- `[[book-ops review]]` — rolling short surface, not append-only: two live sections — **🟡 Open
  — your call** (gated, awaiting ruling) + **✅ Cleared today** (one line → state). Each run
  archives sweep-sections older than 48h to `[[book-ops review archive · <date>]]`. If Open > ~7
  items: "N open, oldest first" + link the rest, don't render inline.
- `[[book-ops state]]` — watermark, flagged pair-keys, aliases.
- Quarantine list — inside the review section; never auto-deleted.
- `inventory.json`, `delta_report.json`/`candidates.json` — disposable per-run artifacts.

## Notes

- Reached from two chapters = cross-cutting, not duplicate: backlink overlap is the merge
  signal, meaning overlap is not.
- Full sweep is recall-tuned (expect noise); delta should be near-silent on a quiet graph — if
  not, `flagged::` probably wasn't loaded.
- Clearly stale vs the graph → ask, don't guess.
- The gate matches **titles, not meanings**. Two sentences stating one claim in different words
  pass as `clear` however fresh the inventory. The Aug 1 practice-gap near-miss was this, not
  staleness alone — do not report the gate as anti-fork protection it does not provide.

## RUN STAMP [HARD]

At the end of every sweep — delta or full, scheduled or manual — write ONE line to
`[[book-ops state]]`, updating it in place rather than appending a new one:

```
last-run:: [[Month Dth, YYYY]] · <delta | full> · <n> adds · <n> pairs open
```

This is the only artifact that dates a sweep. `[[book-ops state]]` otherwise holds vocabulary
rulings and registries, which get edited without a sweep having run, so its page edit-time is not
a substitute. Without this line the `daily-brief` SWEEP trigger renders `last run unknown` and the
sweep can go weeks unnoticed — the same failure the route watermark had when it sat at July 18 for
fifteen days.

