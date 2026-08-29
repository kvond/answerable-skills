---
name: daily-agenda
description: >
  DEPRECATED — superseded by `daily-brief`, which does everything below plus the Gmail pass, the
  HTML page, and the Roam daily-page stamp. Do NOT use this skill for "daily brief", "morning
  brief", "plan my day", "run the DB", or any scheduled morning run; those all go to `daily-brief`.
  Use only if Katherine names this skill directly and wants the bare time-blocked agenda as chat
  text, with no HTML file and no Roam write.
---

# Daily Agenda

> **v2, 2026-08-01.** Adds the **LIVE MINTS** trigger + age escalation. Katherine: *"if the review
> queue doesn't show up on my daily brief it's not likely to happen."* Live capture in
> `chapter-bank` v3 only works if this line renders.

ONE time-blocked agenda for the target day (default today). After the day-type step, read ONLY the
matching schedule file: A → `reference/a-day.md` · B → `reference/b-day.md` · no Master-Agenda week
row covers the date → `reference/summer.md`.

## SOURCES (read-only · read live every run · never copied into the sheet · Google Tasks retired)

- **Master Agenda — 2026-27 v5** Sheet `1Tqh7eB_I3z-eP9FYMCPvNVclmR9VGXVaae0ZdRICy1g`: weekly grid
  (Wk, MP, Dates/Off-days, Biology + A&P topic/day). Off-days ⚠ "OFF"/"IN-SERVICE"; "Notes due" /
  "DRAFT due" embedded in cells.
- **Google Calendar** — today + look-ahead horizon.

## CONFIG

```
bell: pd1 7:30-9:00 · pd2 9:05-10:35 · pd3 10:40-12:10 · lunch 12:15-12:45 · pd4 12:45-2:15 (arrival 7:25)
day_type: Mon/Wed=A · Tue/Thu=B · Fri = A or B, read from agenda/school calendar
writing_cap_hours: 2
learning hints: spanish "×4 (fixed)" · voice: next micro-focus from [[Voice Practice]] rotation ·
        uke: verbatim `Stu Fuchs goal::` from [[Ukulele]]
route hints: since = [[daily-route]] watermark (read-only) · count of untagged routable blocks (count only, never the list)
emit_order: [route, book-distill, mint-review, learning-block-agenda, wilmu-update, aihs-update, tasks, sweep]
mint_review: source = count of blocks tagged #minted-live · page = [[📋 Live mints — review queue]] · age_escalation_days: 7
lookahead_days: 14 · output_target: draft   # draft | roam_api | email | drive_doc
```

## ALGORITHM

1. **Mode.** Week row containing target date: none → SUMMER/BREAK (`reference/summer.md`); date in
   off-days or cell says OFF/IN-SERVICE → OFF-DAY; else SCHOOL DAY.
2. **Day type** per config; load that day's `reference/` file.
3. **Teaching = locked.** Each `capacity: teach` period fixed; topic + Notes/Draft due from Master
   Agenda.
4. **Non-teaching = filled by capacity** (details + weekday rhythm in the day file):
   `deep` → rhythm's deep items — WilmU grad class (seminar prep + grading) is DEEP, never IEP.
   `short_tasks` (IEP coverage, B days, pd1) → per day file; mark "(tentative — adjust after you
   live it)".
5. **Today's calendar** at real times; flag collisions with teaching.
6. **Look-ahead & pull-forward** (coordination only — inputs stay in their own apps): Calendar
   across `lookahead_days`. Spare deep/work capacity → surface dated `[[📋 TASKS]]` items (this
   month's bucket) as PULL-FORWARD, quick wins first.
7. **Triggers** per `emit_order` (see RULES).
8. **Assemble → `output_target`.**

## OUTPUT

```
📅 [Weekday], [Date] — [SCHOOL · A-day | B-day | OFF-DAY | SUMMER]
Wk [n] · [MP] · [Bio] / [A&P]
⏰  pd1 [time]  [slot] — [teach topic | rhythm focus | short tasks]
    pd2 …   pd3 …   pd4 …
✅ ATTEND-TO-FIRST (max 3)
── TRIGGERS ──  (tap when ready; emitting a line writes nothing)
🧭 ROUTE → run `daily-route`                    ·  [n] untagged blocks since [date]
📖 BOOK DISTILL → run `chapter-bank`            ·  [n] #Book captures to file
📇 LIVE MINTS → [[📋 Live mints — review queue]] ·  [n] provisional · oldest [d]d
🎧 LEARNING BLOCK AGENDA → run `learning-block` ·  Spanish ×4 · Voice: [micro-focus] · Uke: [goal]
🎓 WILMU UPDATE → run `block-update` (WilmU)    ·  refresh [[WilmU Block]] status
🍎 AIHS UPDATE → run `block-update` (AIHS)      ·  refresh [[AIHS Block]] status
📋 TASKS → run `task-distill`                   ·  [n] open · [m] dated this month
🧹 SWEEP → run `book-ops`                       ·  tags + pages (also runs auto 8 pm)
🔁 CARRY-FORWARD: due today [Notes/Drafts] · prep for next wk [Thu/Fri links/setup]
👀 LOOK-AHEAD (next [lookahead_days]d) — ONE DATE PER LINE:
   [Weekday M/D] — [event · time] [· second event]
   [Weekday M/D] — …
⏩ PULL-FORWARD (only if a block is open today): [dated 📋 TASKS item] — could do now
```

## RULES

- [HARD] **LIVE MINTS line is not optional.** Whenever any block carries `#minted-live`, the
  trigger line renders with the count and the age of the oldest item. Claims minted under
  chapter-bank v3 live capture are *provisional* until Katherine looks at them; a queue that
  surfaces only in Roam's Linked References does not get looked at, which defeats live capture.
  Render it even on OFF-DAY and SUMMER — reviewing is not teaching work.
- [HARD] **Escalate on age.** If any `#minted-live` item is older than `age_escalation_days`, the
  queue also takes one of the three ✅ ATTEND-TO-FIRST slots, phrased with the oldest item's title.
  A backlog of provisional claims is the failure mode live capture trades for, and it is only
  acceptable while it stays short.
- [HARD] Every block stamped with its bell time. Lunch 12:15–12:45 fixed, never scheduled over.
- [HARD] Thu review + Fri setup always reference the NEXT week.
- [HARD] IEP coverage block = short tasks only, never deep work.
- [HARD] Book block ≤ `writing_cap_hours` (~2h) deep writing/day — surface the rest of its state,
  never schedule past the cap or fill a whole day with it.
- [HARD] TRIGGERS block per `emit_order`, each trigger its own line, never folded together.
  Lightweight hints only (counts · since-date · learning micro-focus); never expand full
  detail inline (no listing the four Spanish tasks or the routable blocks) — the morning stays for
  musings. Emitting writes nothing; running the named skill does the work + its confirm-gated
  write. Any new page is minted only via the book-ops on-create check. 🧹 SWEEP also auto-runs
  at 20:00.
- [FORBIDDEN] Don't touch the grading pipeline (Teacher Dashboard) — separate system.
- [FORBIDDEN] No sends/writes to mail, Roam, or calendar without per-run confirmation unless
  `output_target` is preset on an approved scheduled routine.
- [HARD] LOOK-AHEAD renders one date per line, never run together.
- Inputs stay sovereign: coordinate; never own or duplicate a source.
- OFF-DAY: never fabricate classes. SUMMER: no classes or bell times (`reference/summer.md`).
