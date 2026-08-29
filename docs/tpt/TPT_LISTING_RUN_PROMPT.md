# Claude Code — create the five Answerable Biology listings on TPT

You are the orchestrator for this run. Use subagents where they genuinely parallelise,
and do the browser work yourself, serially. Read all of §1 before starting.

**The full field-by-field spec is a separate file. Read it first:**

```
/Users/katherinevonduyke/Library/CloudStorage/GoogleDrive-kvd@answerableteaching.com/My Drive/Teacher Pay Teachers/CLAUDE SKILL FILES/TPT_listing_handoff.md
```

It carries the titles, descriptions, prices, NGSS codes, tags, custom categories, and the
three failure modes. This file governs *how the run is organised*; that file governs
*what goes in each field*. Where they disagree, that file wins on content and this file
wins on procedure.

---

## 1. The constraint that shapes everything

There is **one Chrome, one TPT session, one seller account, and one form.** TPT's new-item
page is a single stateful form on a single tab.

So: **do not fan out the form-filling.** Parallel agents driving one browser will steal
each other's tabs, submit half-filled forms, and produce listings you cannot untangle. The
bottleneck here is the browser, not thinking, and adding agents to a serial resource makes
it slower and less safe, not faster.

Agents earn their keep on the two phases that touch no browser state:

| Phase | Parallel? | Why |
|---|---|---|
| A — pre-flight verification | **Yes, 5 agents** | Five independent PDFs, five independent link sets. No shared state. |
| B — form entry | **No, serial, you** | One browser, one session, one form. |
| C — post-flight audit | **Yes, 5 agents** | Five independent draft URLs, read-only. |

---

## 2. What a "product" is here

Each product is **one PDF flyer**, and the flyer is the entire deliverable. A buyer
downloads a single page whose links open the Drive folder holding the actual curriculum.
Nothing else is uploaded. The product type is **Digital Download**, never Google Drive —
the reason is in the spec file and it is not negotiable.

The five PDFs live inside their product folders:

```
My Drive/Teacher Pay Teachers/Teacher Facing Docs/
  Answerable Biology — Ecology Starter (FREE)/Ecology Starter (FREE) — Answerable Biology/
      Answerable Biology — Ecology Starter (FREE) — one sheet.pdf
  Answerable Biology — The Cell as a System/The Cell as a System — Answerable Biology/
      Answerable Biology — The Cell as a System — one sheet.pdf
  Answerable Biology — From Sunlight to Populations/From Sunlight to Populations — Answerable Biology/
      Answerable Biology — From Sunlight to Populations — one sheet.pdf
  Answerable Biology — Inheritance & Information/Inheritance & Information — Answerable Biology/
      Answerable Biology — Inheritance & Information — one sheet.pdf
  Answerable Biology — Change Over Time/Change Over Time — Answerable Biology/
      Answerable Biology — Change Over Time — one sheet.pdf
```

Note each unit sits **two folders deep** — an outer `Answerable Biology — <Unit>` wrapper
containing an inner `<Unit> — Answerable Biology`. The PDFs are in the inner one.

**First action, before anything else:** copy all five to `~/tpt-upload/` and upload from
there. Those paths are inside Google Drive for Desktop, which streams files on demand; a
synced file can become an online-only placeholder, and a file picker handed a placeholder
uploads a stub. Verify each copy is **≈130 KB**. A file under 20 KB is a placeholder — stop
and say so rather than uploading it.

---

## 3. Phase A — pre-flight, five agents in parallel

Spawn one agent per unit. Each gets its unit name and its PDF path, and does this:

1. Extract every URL from the PDF (`pdftotext -raw`, or parse the link annotations —
   `pdftotext` alone drops link targets, so read the annotations).
2. Fetch each URL **as a signed-out visitor would see it.** This is the whole point of the
   check. A link that works because you are signed in as Katherine is a link that will fail
   for a buyer.
3. Report per URL: the final HTTP status, whether it lands on the intended resource, and —
   for any Drive `/copy` link — whether it produces the "Make a copy" prompt rather than a
   permission wall.
4. Confirm the flyer is exactly one page and that no text is clipped at the page edge.
5. Report the page count and file size.

Each agent returns a table: URL, status, verdict, and any problem. Nothing else. Agents
must **not** open a browser tab or touch TPT.

**Gate: if any link fails, stop the whole run and report.** Do not create a listing whose
flyer contains a dead link — the flyer *is* the product, so a broken link is a broken
product, and TPT buyers leave one-star reviews for exactly this.

---

## 4. Phase B — form entry, serial, you

Do the custom categories first, once, in the seller dashboard — all seven from the spec
file. Then create the listings **one at a time, in this order**:

1. Ecology Starter (FREE)
2. The Cell as a System
3. From Sunlight to Populations
4. Inheritance & Information
5. Change Over Time

Ecology is first deliberately: it is the free listing, so if the form fights you, you find
out on the product with the least at stake.

Follow the numbered procedure in the spec file exactly. Three things it stresses, repeated
here because they are the ones that break runs:

- **Never click a file input.** That opens a native macOS dialog the extension cannot see
  or dismiss, and the session is dead until Katherine rescues it by hand. Locate the input
  with `read_page` or `find`, then pass its element ref to `file_upload`.
- **Never trigger a JavaScript dialog.** Same failure, same rescue.
- **Re-read the entire form before submitting.** TPT silently drops select values that are
  set too soon after a page mutation. A field you set is not a field that took.

**Leave "Make Listing Active" unchecked on all five.** Every one saves as a draft.

After each listing: record the draft URL, then stop and confirm the draft exists before
starting the next. Do not batch five submissions and check at the end.

**If the same field fails twice, stop and ask.** Do not attempt a third time and do not
work around it by putting the value somewhere else.

---

## 5. Phase C — post-flight audit, five agents in parallel

Once all five drafts exist, spawn one read-only agent per draft. Each opens its draft's
edit page and checks, against the spec file, field by field:

- Title matches character for character
- Description present, formatting intact, no truncation
- The correct PDF is attached — check the filename, and that its size is ≈130 KB
- Price correct (Ecology: Free Resource ticked; the other four: $24.95)
- Tax code: Other digital goods
- Grades 9 and 10 both ticked
- Subject: Science → Biology
- Custom category assigned, and the right one
- NGSS codes exactly as listed for that unit, none extra, none missing
- Teaching duration 90 minutes
- Answer key N/A
- **Make Listing Active UNCHECKED**

Agents **read only**. They do not fix anything. A discrepancy is reported to you and you
fix it serially in the one browser.

---

## 6. Report back

One table: unit, draft URL, and per-field pass/fail. Then, separately, a list of anything
you changed from the spec and why, and anything the form refused.

---

## 7. Listing 6 — the Full Year Bundle

Create this **last, after all five drafts exist**, because a TPT Bundle can only contain
products that are already listed.

Use TPT's **Bundle** product type, not Digital Download. Bundles are built from existing
listings in the same store, TPT prices the difference for buyers who already own a
component, and TPT re-delivers a component automatically whenever you update it.

1. Create a new Bundle listing.
2. Select all five products as components.
3. Attach `Answerable Biology — Full Year Bundle — one sheet.pdf` as the Bundle's
   **bonus file**. TPT allows one file of the Bundle's own alongside the components; that
   is where the year-level sheet goes. Its path:
   `My Drive/Teacher Pay Teachers/Teacher Facing Docs/Answerable Biology --Full Year Bundle/Answerable Biology — Full Year Bundle — one sheet.pdf`
   (that folder uses a double hyphen, not an em dash — copy the path exactly)
4. Title, price, category, tags and NGSS: from the spec file's Listing 6 section.
5. **Make Listing Active stays UNCHECKED.**

Then stop and report.
