---
name: daily-route
description: >
  Route untagged blocks on daily pages to their owning skills (chapter-bank, literature, QUE-
  split, task-distill, personal wall, #unrouted), tracked by watermark so one run sweeps any gap.
  Delegates every write; mints nothing. Triggers: "route my dailies", "daily route", 🧭 ROUTE,
  scheduled run.
---

# daily-route — route the untagged daily-page blocks, delegate every write

The capture leak has two halves: untagged **blocks** stranded on daily pages, and untyped
**pages** that confuse retrieval. This skill owns the **block** half: it scans daily pages,
finds thoughts that never got routed, proposes a destination for each, and hands the actual
write to the skill that owns that destination. A **router, not a home** — it creates nothing,
moves almost nothing, never learns another skill's internals. In particular it **keeps
`task-distill` book-agnostic**: this skill does the book-aware routing and hands `task-distill`
only the task blocks.

## What it scans

- **Daily (date) pages only.** Project pages, the book namespace, `[[TASKS]]`, and concept
  pages are out of scope — already owned.
- **Since the last run, via a single watermark on the `[[daily-route]]` log page [HARD]**
  (last-processed date + run timestamp) — **not** per-daily markers. You miss days; one run
  sweeps *every* unprocessed date since the watermark, which advances only on your approval.

## What counts as a routable block

Both: **(a) untagged for routing** — none of the tags the other skills recognize: not `#Book`,
not a chapter link (`[[ch5]]` / chapter page), not a registry category tag, not a
`#next` / `#near` / `#parking lot` horizon tag; and **(b) not structural** — not a heading,
embed/ref, or `{{[[DONE]]}}`. Anything already carrying a routing tag is left alone.

- **Half-routed blocks are caught:** a horizon tag with no area/destination (`#next` with
  nothing saying *where*) is "horizon set, destination missing" — surfaced and prioritized, not
  treated as routed.
- **Priority signal:** blocks leading with status / next-action prose ("next:", "need to…",
  "follow up…") float to the top of the proposal list — you've already said they're live.

## Route targets — who gets the handoff

| Block reads as | Routes to | Owner does |
|---|---|---|
| **Book thought** (matches a chapter `Scope::`, or reads as claim / example / phrasing) | **chapter-bank** | scope-routing into the bank; any gated CLM/EVD promotion |
| **Reading note / source material** | **literature** | via chapter-bank's reference-page tending |
| **Question** | **QUE-split** | router proposes reading-Q vs argument-Q; **you confirm** |
| **Task** | **task-distill**'s organized layer | proposes promotion into the Admin Queue / area lines |
| **Personal / non-work** | **`#[[🏡 Personal]]`** wall | marked, left in place, excluded from future scans |
| **No clear destination** | **`#unrouted`** hold | never force-fit |

**QUE-split [HARD].** Reading-question (what does the literature say?) → literature;
argument-question (what must the book answer?) → discourse graph. The router only **proposes**
the side — you confirm before any QUE is minted, and the mint is chapter-bank / book-ops'
write, not this skill's.

## The personal wall [HARD]

A personal block is marked **`#[[🏡 Personal]]`**, **stays exactly where it is** (nothing
moves), and is **excluded from every future scan**. The tag auto-becomes a page, so the
material gathers as backlinks — re-taggable later if a thread ever wants structure. A personal
block **never enters a book or task pipeline** — "if it's not writing, it doesn't touch book
pages" is enforced here, at the router.

## Mint discipline [HARD]

`daily-route` **never mints a page.** The **destination skill** creates pages, only through
**book-ops `on_create_check`** — the single chokepoint that stops the dud-page problem from
regrowing. The only in-place marks this skill applies are the routing tags themselves
(`#[[🏡 Personal]]`, `#unrouted`), on your approval; those tags becoming pages is Roam's native
auto-page behavior, not a mint.

## Missed-days handling

A run after a long gap surfaces a large list by design. To keep it reviewable it offers:
**chunk by date** (one day at a time, oldest first) or **priority-first** (status-prose /
half-routed blocks across the whole gap first, the rest after). Either way the watermark
advances only over the dates you actually clear.

## Quarantine pointer — reported, not owned

The page-level untyped/orphan sweep is **book-ops'** job. This skill's run summary just
surfaces a pointer to the latest book-ops quarantine list, so both halves of the leak land in
the same morning glance without merging responsibilities.

**One-line rule [shared with book-ops].** book-ops stamps the daily note with a single pointer —
`🏷️ book-ops: auto-applied N · open M (your call) → [[book-ops review]] · archived K` — counts
from `[[book-ops state]]`, never the block list, the same rule this skill's `🧭 ROUTE` line uses
for its count. daily-route surfaces that pointer in the morning glance; it never expands it into
the candidate list.

## 🛑 Confirm + safety

- **Roam is canonical. Confirm-before-write.** Per-run proposal surface: each routable block
  with proposed destination + one-line reason, grouped destination-first, priority up top. You
  approve / correct / defer per block; nothing is written until you approve, and the write that
  follows is the **destination skill's** (through its own confirm + `on_create_check`).
- [HARD] **Mint nothing.**
- [HARD] **Personal blocks never move, never enter a book/task pipeline**, and once tagged are
  excluded from all future scans.
- [HARD] **Never force-fit** — no clear destination → `#unrouted`, surfaced, held.
- [HARD] **Keep task-distill book-agnostic** — hand it only task blocks, never book context.
- Deferred blocks stay untagged and resurface next run; the watermark doesn't pass an
  unadjudicated date you chose to hold.

## Trigger line & scheduling

The daily brief carries one on-demand launcher (daily-agenda owns the line):
`🧭 ROUTE → run daily-route · [n] untagged blocks since [date]` — count + since-date from the
watermark, never the block list. Emitting writes nothing; running does the scan + confirm-gated
proposal.

- **Schedulable** (e.g. Sunday sweep) or manual ("route my dailies"); self-chunks after a gap.
- **Outputs:** the proposal surface; on approval, the handoffs + in-place `#[[🏡 Personal]]` /
  `#unrouted` marks; the advanced watermark; a run summary (routed per destination · personal ·
  unrouted · deferred · pointer to book-ops' latest quarantine list).
