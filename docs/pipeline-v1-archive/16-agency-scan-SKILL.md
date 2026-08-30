# Workflow D — Agency Scan (participatory-agency coding + dialogic email)

**Status:** deployed spec. Judgment layer = the Agency Codebook (below, v1
approved 2026-07-13). `.py` scripts stay dumb; all coding judgment lives here.

**What it does, in one line:** over student text the pipeline has *already
fetched and extracted* (NOTES, DRAFT) plus opt-in email threads, flag segments
that show participatory agency, log them to the **Agency Watch** sheet for
Katherine's pre-class review, optionally draft a dialogic reply per student
(Composio Gmail draft, never sent), and accrete everything into a dated
per-student transcript on demand.

This is **not** a grading workflow. It never writes to the Dashboard, never
touches scores, and is independent of Workflow A/B outcomes. A blank rewrite
can still carry an agentive move; a perfect rewrite can carry none.

---

## Assets (live IDs)

| Thing | ID |
|---|---|
| Agency Watch spreadsheet (do not delete) | `18Cc-edFsozcn_04-1r1oUCouy6kFhUuFdeWOO3HWa3s` |
| — tab `Coding Master` (source of truth) | long format, one row per coded segment |
| — tab `Before Class` (auto-view) | formula-driven; NEVER type here |
| Teacher Dashboard (class membership, source of truth) | `1W0s8YjcIt7h8ezICAF6SndTj97PiMcfjpXrmVmV8cBA` |
| Gmail label for dialogue replies | `Agency-Dialogue` (`Label_179`) |

All Google ops route through **Composio (kvond12)**. Retry transient
"upstream MCP server" blips before reporting a disconnection.

---

## The two triggers

**D1 — coding pass (rides inside PIPE).** Runs only when Katherine runs the
grading pipeline. Codes the same artifacts the scan/grade step already pulled —
zero extra downloads. Appends new rows to `Coding Master` with
`status = new`. See PIPELINE_CHECKLIST.md → "2.5 — Agency coding pass".

**D2 — agency sweep (on demand, never automatic).** Trigger phrase:
**"agency sweep"**. Reads inbound student replies to the dialogic emails, codes
them (`source_type = EMAIL_IN`), and logs any class-improvement suggestions.
NEVER scans the inbox unasked — same rule as the grading scan.

Neither trigger fires proactively at session start.

---

## Agency Codebook (v1 — judgment layer)

Segment = smallest span of student text carrying the move (a sentence to a
short paragraph). **Every coded segment MUST include a verbatim excerpt that is
a substring of the student's own text** — same standard as B1 praise:
student-generated, not echoed prompt text, no template rationale. Codes are
**not mutually exclusive** — double-code a segment that does two things, sharing
one `segment_id`. Code for **presence, not quality**.

### ENG — Engaged agency
*Student contributes their own thinking beyond what the prompt required.*
Include: unprompted example (esp. from own life/observation); self-made
connection to another lesson/class/phenomenon; a substantive position ("I don't
buy that…"); an answer that runs past the question because the idea carried
them; pushback on the material or framing.
Exclude: restated prompt/slide text however fluent; long-but-compliant answers
fully inside the ask; "I think" as filler.

### EPI — Epistemic agency
*Student sees or frames something in a new way — acts on knowledge itself.*
Include: self-generated question that opens inquiry ("but then wouldn't…?");
noticing a contradiction/anomaly and saying so; revising an earlier idea *with
the reasoning shown*; building their own analogy/model (not one taught);
commenting on how their thinking changed ("I used to think… now I see…").
Exclude: correct application of a taught reframe (that's mastery); rhetorical
questions with no follow-through; hedging with no idea attached.

### AUT — Authorial agency
*Student directs their own study — they chose it.*
Include: sought sources themselves ("I looked it up / watched a video about…");
did unassigned work by choice; proposes a topic/project/direction for their own
learning; **suggests how the class could work better** (class-improvement
replies from D2 code here).
Exclude: completing an offered optional extension (directed, not chosen);
additions that read as tutor/parent-driven where discernible.

### CAND — candidate / unclear
Promising but ambiguous; flag for Katherine's eyes. Use sparingly. A confirmed
CAND is recoded to its real code; a rejected CAND is dropped. Both outcomes are
kept as validation data (via the `verdict` column), not deleted.

### Decision rules
1. Verbatim or nothing — no paraphrase in the `excerpt` field.
2. Presence, not polish — casual/misspelled text codes the same as fluent.
3. ENG vs EPI when torn: ENG *adds* own thinking; EPI *changes/questions* the
   frame. Both → double-code.
4. One row per code per segment; double-codes share `segment_id`.
5. Every AI-assigned code is provisional until `verdict` = confirm/reject/recode.
   Verdict disagreements are analyzable data.

---

## Coding Master schema (tab 1)

`date` (of the artifact, not of coding) · `student` (Dashboard name) · `class`
(Dashboard lookup — never inferred from filename/folder) · `source_type`
(NOTES / DRAFT / EMAIL_OUT / EMAIL_IN) · `artifact` (lesson name or email
subject) · `segment_id` · `code` (ENG/EPI/AUT/CAND) · `excerpt` (verbatim
substring) · `why_promising` (student-specific memo, no template phrases) ·
`discussion_opener` (how to open it in class; blank for email-only) ·
`verdict` (Katherine: confirm/reject/recode) · `status`
(new / opened-in-class / emailed / replied).

**Segment-id convention:** `<studentinitials>-<YYYYMMDD>-<artifactslug>-<n>`,
e.g. `MJ-20260713-evidence-evolution-2`. Double-coded rows reuse the id.

**Class membership [HARD]:** look each student up across the Dashboard class
tabs before writing a row. Skip inactive students (Sha'rod Watson, A_Day Bio).

---

## Model routing

- **Extraction** (which files exist, pull raw answer text): the pipeline's
  existing deterministic extractors already do this — reuse their output; do not
  re-extract. Haiku if a standalone extraction is ever needed.
- **Coding judgment** (assign ENG/EPI/AUT, write memo + opener): **Sonnet**.
  Conceptual, needs the codebook in context.

---

## Step-by-step

### D1 coding pass (inside PIPE)
1. Take the already-extracted student text from the current grading run
   (per lesson, per class). Do NOT trigger new downloads.
2. For each student answer, segment and apply the codebook. Most answers code
   to nothing — that is expected and correct; do not force a code.
3. For each hit, build a row: verbatim `excerpt`, student-specific
   `why_promising`, and a one-line `discussion_opener` (a way Katherine could
   open it with the class — a question, not a summary).
4. **SELF_CHECK before writing** (mirrors B1 praise check): drop any row whose
   `excerpt` is not a substring of that student's text, is echoed prompt text,
   or whose `why_promising` uses a template phrase.
5. Append rows to `Coding Master` with `status = new`, `verdict` blank.
   Append only — never rewrite existing rows (preserves Katherine's verdicts).
6. Report a one-line count per class ("Evidence of Evolution B_Day: 4 ENG,
   1 EPI, 2 CAND across 18 students"). The `Before Class` tab now shows them.

### Dialogic email (opt-in, drafts only)
Trigger: Katherine says "draft agency replies" (or picks students from the
`Before Class` view). For each selected coded segment:
1. Compose a short reply that **answers the student's idea dialogically** —
   engages the actual thought, asks one genuine follow-up question, and invites
   a reply. Warm, specific, 9th-grade register. No grades, no rubric language.
2. Every email closes with a standing invitation: *"…and if there's anything
   you'd change about how this class runs, tell me — I read every one."*
   (This is the class-improvement prompt; replies code AUT under D2.)
3. Create it as a **Gmail draft via Composio `GMAIL_CREATE_EMAIL_DRAFT`
   (kvond12)** — subject `A thought on your work — [Lesson]`, addressed to the
   student's roster email (`@redclay.k12.de.us`), and apply the label
   `Agency-Dialogue` to the draft so the reply thread later surfaces under it.
   **NEVER call GMAIL_SEND_*.** Katherine reviews and sends. Drafts-only is the
   safety invariant — identical to Workflow B.
4. Mark those `Coding Master` rows `status = emailed`.

### D2 agency sweep (on demand)
Trigger: "agency sweep". Find threads by searching
`label:Agency-Dialogue OR subject:"A thought on your work"` (kvond12) — the
outbound draft carries the `Agency-Dialogue` label, so Gmail surfaces the whole
reply thread under it; **no mail filter is required**. Code inbound replies
(`source_type = EMAIL_IN`), append rows, flag class-improvement suggestions as
AUT. Mark the original outbound rows `status = replied`.

### Transcript on demand
Trigger: "build agency transcript for [student]" (or "for all"). Read that
student's `Coding Master` rows, order by `date`, render a readable dated
transcript as **.docx** (one dated entry per segment: source, verbatim excerpt,
code, memo, and any email exchange). This is the qualitative-coding artifact for
the book. **Pseudonymize at export, not in the working sheet** — the .docx uses
a stable pseudonym; `Coding Master` keeps real names for Katherine's use.

---

## Invariants that must not drift

- **Verbatim excerpt only** — substring of the student's own words, no paraphrase.
- **Append-only writes to Coding Master** — never overwrite a row (protects verdicts).
- **Never write to `Before Class`** — it's formula-driven.
- **Drafts-only email** — Composio Gmail drafts, kvond12, never SEND; first-party
  Gmail MCP forbidden for student email.
- **Class membership from the Dashboard**, never filename/folder.
- **Presence, not quality** — coding is orthogonal to grading; never let a score
  influence a code or vice-versa.
- **On-demand only** — D1 rides PIPE; D2 and email drafting run only when asked.
- **Pseudonymize at transcript export** for anything feeding the book.
