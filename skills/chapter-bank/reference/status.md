# chapter-bank reference — Writing Status & the reconfigure path

Read this file when stamping `Writing Status::` or handling a reconfigure flag.

## Writing Status — what writing-block reads (confirm-gated)

chapter-bank stamps a `Writing Status::` block on each chapter (page or notes bank): notes-bank
+ claims **depth**, the milestone checklist, and the **reconfigure flag**. Read current state
from the chapters' existing `Writing Status::` blocks — do not re-seed from the historical
State-of-book note. Rough map as of Jul 12 2026 (verify against the live blocks; this dates
fast):

- Ch 1–2 — finishing pass done (provenance + continuity checked, final read-through Jul 5–6);
  revision flagged for older material being pulled in.
- Ch 3 / 3b — restaged Jul 5 with heavy draft-notes; ACTIVE.
- Ch 5 → Ch 11 — the priority order before the Panama retreat (Jul 23 2026).
- Ch 6 — thin. Front Matter / Introduction — held, dependent.

## Reconfigure path

When a chapter's structure changes (heavy restructures are expected):

1. **Set the reconfigure flag** in that chapter's `Writing Status::` so `writing-block` stops
   proposing it for writing until re-routing is done.
2. Re-route that chapter's banked material to the new chapter(s) by the updated `Scope::`.
3. Clear that chapter's milestone checklist in `Writing Status::`.
4. Re-enter the bank loop, then **clear the reconfigure flag**. 📇 durable notes and EVD are
   **not** deleted — they're area-level and survive chapter churn; only their hub / structure-note
   placement is re-sequenced.
