---
name: block-update
description: >
  Status-only updater for a life block — AIHS (high-school teaching) or WilmU. Refreshes the
  Status:: note atop [[AIHS Block]] or [[WilmU Block]] from recent [[TASKS]] + daily-page
  activity: done · where you are · single next action. Never tags, promotes, or mints.
  Triggers: 🍎 AIHS UPDATE, 🎓 WILMU UPDATE, "aihs update", "wilmu update",
  "where am I on school / WilmU".
---

# block-update — keep a block's status pointer current

An **Update**, not a Distill: never tags into the discourse graph, never mints a page. One job —
refresh the block page's **Status::** so you always know where to pick up. The block page holds
the long list; this refreshes the pointer on top.

## Block parameter — resolve from the trigger

| Trigger said | Block page | Task tags on [[TASKS]] |
|---|---|---|
| 🍎 / "aihs" / "school" | [[AIHS Block]] | #AIHS, #[[Curriculum 26-27]] |
| 🎓 / "wilmu" | [[WilmU Block]] | #[[Wilmington University 7106]] |

Ambiguous → ask which block before reading anything.

## What it reads (read-only)

- The block page (reservoir) and its current Status:: (carry forward what's unresolved).
- The block's tagged tasks on [[TASKS]] (Admin Queue + area lines).
- Block-related captures on recent daily pages.

## What it writes (confirm-gated)

A refreshed **Status::** at the top of the block page — three fields, one line each:
**Done** (since last update) · **Where you are** (current open thread) ·
**Next** (the single next action, naming any gate).

## Feeds State of the Blocks

The Brief's block line (`AIHS — did X · next Y → [[AIHS Block]]`) is drawn from this Status::.

## 🛑 Confirm + safety

- Roam is canonical. Show the proposed Status::; write only on OK.
- [HARD] Status only — no zettel/CLM/EVD tagging, no page mints.
- [HARD] Never moves, re-statuses, or deletes the block's tasks.
- [HARD] AIHS only: don't touch the grading pipeline (Teacher Dashboard) — separate system.
- AIHS note: a school journal is a separate database + tag system; this tracks task/status only
  and never folds journaling into the book graph.

## Triggers / outputs

Brief TRIGGERS lines: `🍎 AIHS UPDATE → run block-update (AIHS)` ·
`🎓 WILMU UPDATE → run block-update (WilmU)`. Manual, not scheduled.
Outputs: refreshed Status::, the one-liner for State of the Blocks, short run summary.
