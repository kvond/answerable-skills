# Workflow C — Growth Doc Format Reference

*(Formerly the B3 growth doc format. Renamed 2026-05-25.)*

The master growth tracking doc has a specific layout that Workflow C enforces. This file is the canonical reference — when in doubt about formatting, this file wins.

---

## Document title and header

The doc title is always:
> **Feedback System — Growth Tracking**

The header block under the title:
```
**System:** Dr. von Duyke's biology & forensics feedback pipeline
**Last updated:** <ISO date>
```

The "Last updated" line is rewritten on every C run.

---

## Class summary section

One subsection per class, in this fixed order:
1. A_Day Biology
2. B_Day Biology
3. A_Day Forensics
4. B_Day Forensics

Header format: `### <Class Name> — <N students tracked, M lessons covered>`

Below the header, a table with one row per rubric:

| Rubric | Class trajectory | Current mode | 🟩 / 🟨 / 🟥 (latest lesson) |
|---|---|---|---|

Followed by a 2–3 sentence narrative paragraph. The narrative should:
- Be plain English, not jargon
- Name the rubric that's strongest and the rubric that's lagging
- Not include any individual student names

Example narrative:
> The class is strongest on Writing — most students have moved from 🟥 to 🟨 over four lessons, and a few have reached 🟩. Depth of Explanation is the lagging rubric — half the class is still at 🟥 and the others are 🟨. Conceptual is improving but slowly.

---

## Class trajectory markers

Heuristics for how the class is moving overall (across all students for a given rubric):

| Marker | Trigger |
|---|---|
| 🚀 Climbing | Two consecutive lessons showed an increase in the percentage of students at 🟩 OR a decrease in 🟥 (more than 10% movement) |
| 📈 Improving | Net upward shift in distribution from first to most recent lesson (looking at composite center) |
| ➖ Steady | Distribution roughly unchanged across the last 3 lessons |
| ⚠️ Sliding | Last 2 lessons show movement toward 🟥 |
| 🔵 Too few lessons | Fewer than 3 lessons available for this class |

The "Current mode" cell shows the modal color of the class on this rubric on the most recent lesson.

---

## Per-student section

One section per student, ordered alphabetically by last name within their class.

### Section header
Format: `### <Last, First> (<Class>) — <overall trajectory>`

Where `<overall trajectory>` is the marker computed from the student's composite scores across their lessons:

| Marker | Trigger |
|---|---|
| 🚀 Climbing | Last 3 lessons show consistent improvement on composite (no holds, no drops) |
| 📈 Improving | Net upward trend across lessons (more 🟩 in recent half than earlier half) |
| ➖ Steady | Composite held the same color for last 3 lessons |
| ⚠️ Declining | Last 2 lessons show a regression in composite |
| 🔵 Too few lessons | Fewer than 3 lessons |

### Per-student detail block
Directly under the header:

```
**Trajectory:** Conceptual <marker> · Depth <marker> · Writing <marker>
**Lessons completed:** N
```

The per-rubric trajectory markers use the same set as composite (🚀 / 📈 / ➖ / ⚠️ / 🔵).

### Lessons table
| Lesson | Date | Conceptual | Depth | Writing | Composite |
|---|---|---|---|---|---|

Rows ordered chronologically (oldest first, most recent at the bottom). Date in ISO format.

### Annotations
If a row is updated by a B2 re-run, append `(updated <date>)` to the lesson cell.

If a student moved classes mid-year, add a note line below the table:
> *Note: Moved from A_Day Biology to B_Day Biology on 2026-03-15.*

### Section separator
A horizontal rule (`---`) separates each student from the next.

---

## Color codes — fixed mapping

| Color | Tier | Symbol |
|---|---|---|
| Red | Starting | 🟥 |
| Yellow | Working On It | 🟨 |
| Green | Mastery | 🟩 |

Always use the colored square emoji. Never substitute words for symbols inside the tables — visual scanning depends on the colored squares being there.

In narrative prose, you can use the words "starting," "working on it," "mastery" naturally, lowercase, no symbols required.

---

## Trajectory marker mapping — fixed

| Marker | Meaning |
|---|---|
| 🚀 | Climbing (sustained improvement) |
| 📈 | Improving (net upward trend) |
| ➖ | Steady |
| ⚠️ | Declining or sliding |
| 🔵 | Too few lessons |

These are visual markers, not formal grades. Don't add additional markers; don't reuse for other meanings.

---

## What goes in the doc

- Student names (Last, First format)
- Lesson names
- Dates
- Rubric scores (color squares)
- Trajectory markers (climbing/improving/steady/declining/too-few)
- Class-level summary tables and brief narrative
- Annotation notes (class change, score update)
- A single "Last updated" timestamp at the top

## What does NOT go in the doc

- ❌ Letter grades or percentages
- ❌ Individual student comments or feedback (those live in B2's emails)
- ❌ Rewrite directions or rubric definitions
- ❌ Identifying information beyond first/last name and class (no emails, no IDs)
- ❌ Editorial notes about specific students
- ❌ Photos or images
- ❌ Statistics beyond the distribution tables (no charts, no percentile rankings)

The doc is intentionally minimal. It's a tracking surface, not a feedback surface.

---

## Example doc fragment

```
## Class trajectory summary

### B_Day Biology — 16 students tracked, 4 lessons covered

| Rubric | Class trajectory | Current mode | 🟩 / 🟨 / 🟥 (latest lesson) |
|---|---|---|---|
| Conceptual Accuracy & Vocabulary | 🚀 Climbing | 🟨 Working on it | 6 / 8 / 2 |
| Depth of Explanation | 📈 Improving | 🟨 Working on it | 3 / 9 / 4 |
| Scientific Writing Quality | ➖ Steady | 🟨 Working on it | 4 / 10 / 2 |

The class is moving on Conceptual — six students reached 🟩 on the most recent lesson, up from two on the first. Depth is improving more slowly. Writing has stayed roughly the same across all four lessons; it might be worth a focused mini-lesson on sentence completeness.

## Per-student trajectories

### Carter, Jordan (B_Day Biology) — 🚀 Climbing
**Trajectory:** Conceptual 🚀 · Depth 📈 · Writing 📈
**Lessons completed:** 4

| Lesson | Date | Conceptual | Depth | Writing | Composite |
|---|---|---|---|---|---|
| Classifying Organisms | 2026-04-15 | 🟥 | 🟥 | 🟨 | 🟥 |
| Evidence of Evolution | 2026-05-08 | 🟨 | 🟨 | 🟨 | 🟨 |
| Natural Selection | 2026-05-22 | 🟨 | 🟨 | 🟨 | 🟨 |
| Speciation | 2026-06-05 | 🟩 | 🟩 | 🟨 | 🟩 |

---

### Hassan, Layla (B_Day Biology) — ➖ Steady
**Trajectory:** Conceptual ➖ · Depth ➖ · Writing 📈
**Lessons completed:** 4

| Lesson | Date | Conceptual | Depth | Writing | Composite |
|---|---|---|---|---|---|
| Classifying Organisms | 2026-04-15 | 🟨 | 🟨 | 🟥 | 🟨 |
| Evidence of Evolution | 2026-05-08 | 🟨 | 🟨 | 🟨 | 🟨 |
| Natural Selection | 2026-05-22 | 🟨 | 🟨 | 🟨 | 🟨 |
| Speciation | 2026-06-05 | 🟨 | 🟨 | 🟩 | 🟨 |

---
```

This is what Workflow C produces. Same shape, every time, accumulating row by row.
