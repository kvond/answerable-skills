# RESUME HERE — Answerable Biology build, state as of 2026-08-08

Hand this file to the next session. It records what was decided, what is finished, and the exact work left. Nothing has been published to TPT.

## The seven decisions Katherine made (standing — treat as settled)

1. **Tank models — RESOLVED 2026-08-09. Live and working.** The repo `github.com/Answerable-Teaching/tank-and-flow-models` was found intact; all ten models plus `index.html` are self-contained. Canonical master copies live in her Google Drive folder **"Answerable Biology — Interactive Models"** (folder id `1FOzcJ4ZN2xRshAdviQnkMU7t9z7JWDIP`).
   - **GitHub Pages was abandoned.** It was configured correctly the whole time (public repo, main / root, index.html present). All four builds failed on GitHub's side: *"The job was not acquired by Runner of type hosted even after multiple attempts"* plus *"Internal server error"* (correlation ID `833ee156-a784-4534-9853-cb4b1dea059d`). A re-run on 2026-08-09 also sat in Queued indefinitely. Not a configuration problem — do not spend time re-diagnosing it.
   - **Serving is now Netlify.** Site `answerable-biology-models` (id `f851b6f8-eef4-4312-a0d3-509173205c2e`) on her Netlify account (kvond12@gmail.com). All eleven pages verified HTTP 200 at `https://answerable-biology-models.netlify.app/<model>.html`.
   - **Ten decks relinked** from the dead github.io URL to the Netlify one, in `Biology Lesson Decks/_relinked working model URLs/` on the shared drive: Cycles 03, 04, 05, 06, 09, 10, 11, 18, 19, 20. Each had exactly one text occurrence and one hyperlink relationship updated; nothing else in the decks changed.
   - **Cycle 02 was deliberately left alone** — its energy model already points at a working address (`hilarious-biscuit-630a42.netlify.app`). Consolidating it onto the `answerable-biology-models` host would put all eleven models in one place; that is Katherine's call, not done.
   - **Open, optional:** a branded custom domain (e.g. `models.answerableteaching.com` — she owns answerableteaching.com through Google Workspace). Needs a CNAME at her registrar plus adding the domain in Netlify. The netlify.app addresses keep working after a custom domain is added, so the relinked decks will not break either way; re-running the relink script would swap them to the branded address.
2. **Free bundle** — the AI Feedback and Conceptual Growth document **is included free**. The free Ecology product is five components: Cycle 02 deck, Free Unit Guide, Year Arc, Start Here, AI Feedback and Conceptual Growth. A free-unit teacher can run the loop end to end, bellringer through Growth Report.
3. **Deck rights** — clean the four decks carrying inherited third-party content by rewriting the affected slides; originals never modified; cleaned copies are `(v3 cleaned)` with a slide-by-slide change manifest for her review.
4. **Cycle 01** — gets its own paid TPT listing, a 20th, drafted in the voice and structure of her existing nineteen. Draft goes in the Review Register for approval; her `Answerable_Biology_Unit_Descriptions.md` is never edited directly.
5. **Quarter mapping** — confirmed, no longer an assumption: Q1 = Cycles 01–05, Q2 = 06–10, Q3 = 11–15, Q4 = 16–20. Cycle 02 is the free unit *and* sits inside Q1; Cycle 01 is part of the Q1 bundle. Q1 buyers get Cycles 01, 03, 04, 05 plus infrastructure, with Cycle 02 already theirs free — so they do not pay twice.
6. **Protein Synthesis** — confirmed as the Cycle 15 EXTEND deck, shipping inside the Genes & Chromosomes listing, as Cycles 07/08/13/16 handle their companions. No separate listing.
7. **Nothing goes live on TPT yet.** All go/no-go gates stay in place.

## Finished

- Full 22-document build, folders 00–18, QA-passed with 36 findings fixed.
- **Cycle 12 CORE deck recovered.** "The Process of Meiosis" (28 slides) was found in her Google Slides (Drive id `1pN08QqPJbhP6T8QbCKNjfQOS3JmQrLq60GeH1oCkktE`), exported to pptx, added to the Desktop folder, and propagated through the Source Map, Year Arc, Master Agenda, Standards, Supply System, Setup, TPT Architecture, Project Index, and Review Register. It is no longer SOURCE NOT YET LOCATED anywhere.
- Ten interactive models uploaded to the Drive folder above.
- **Three of four decks cleaned**, verified to open, correct slide counts, zero residual third-party strings:
  - Cycle 12 — Reproduction & Meiosis (v3 cleaned) — 28 of 47 slides rebuilt, 97 third-party images removed, 16 replacement diagrams drawn, file 15.7 MB → 1.3 MB. Manifest written.
  - Cycle 12 — The Process of Meiosis (v3 cleaned) — 20 of 28 slides rebuilt, every removed figure redrawn (no placeholders needed), Google-Slides export artifacts repaired. Manifest written.
  - Cycle 16 — Stem Cell Differentiation (v3 cleaned) — 26 slides, file written and verified clean, **but its change manifest was never written** because the agent hit the spend limit at the final step. Regenerate the manifest by diffing v2 against v3.

## Left to do

1. **Clean Cycle 13 — Genetics Continued / Punnett (86 slides).** Not started. Known content: CK-12-derived text, Mrs. Stefanisin identity and photographs, possible legacy worksheet material. Use the same cleaning rules; work from the extraction at `/root/ab_build/extracted/` to locate affected slides before opening the pptx.
2. **Write the Cycle 16 Stem Cell change manifest** (diff v2 → v3).
3. **Apply decisions 1, 2, 4, 5, 6 across the documentation.** Both editor agents died before making any edits, so the doc set still reflects the pre-decision state. Files needing edits:
   - Decision 2 (five-component free product): `15_TPT_Product_System/TPT_Product_Architecture.md` (section 2, section 7 matrix), `16_TPT_Sales_Materials/TPT_Sales_Copy_and_Preview_Plan.md` (section 3 and the free listing), `03_Setup/Set_Up_Answerable_Biology.md` (the free-unit step list can now honestly include the AI feedback step), `04_Ecology/Ecology_Unit_Guide.md` (Free Unit Guide export note).
   - Decision 1 (models recovered): `02_Year_Arc/Year_Arc_20_Cycles.md`, `02_Year_Arc/Master_Agenda.md`, `08_Fiddles_Extensions/Fiddles_Extensions_and_YouTube.md`, `07_Activities_Labs/Activities_Models_and_Labs_Guide.md`, `17_Source_Audit/ACTIVITY_SOURCE_AND_RIGHTS_AUDIT.md`, `17_Source_Audit/BROKEN_LINK_REPORT.md`. Replace "404 / permanently dead / redeploy unknown" framing with: recovered, canonical copies in Drive, served by Pages at the existing URL, awaiting only the Pages switch. One LINK NEEDED note, not nine alarm flags.
   - Decision 5 (quarters confirmed): remove the assumption flags from `13_Supplies/Supply_System_README.md`, `13_Supplies/Master_Supply_System.xlsx` (use openpyxl, keep formulas, regenerate the CSV from MASTER, verify it reopens), and the TPT architecture.
   - Decisions 4 and 6: draft the Cycle 01 listing into `00_Project_Index/REVIEW_REGISTER.md`; note Cycle 01's individual listing in the TPT architecture; remove the "possible missing 20th listing" speculation about Protein Synthesis and add a bracketed suggested included-list sentence for the Cycle 15 listing to the Review Register.
   - Decision 3: update the rights entries for the four decks — the gate becomes "ships once the cleaned copy is approved," not RIGHTS REVIEW NEEDED with no path.
4. **Re-run the coherence QA** after those edits, then refresh the zip and the Desktop folder.

## Why the work stopped

The org monthly spend limit was reached (`claude.ai/settings/usage`). Four agents failed mid-pass on the first attempt and four more on the retry. Everything above is recorded so no analysis has to be redone — the source map, rights audit, and teaching extraction are all still valid and should not be rebuilt.
