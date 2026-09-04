# ACTIVITY_SOURCE_AND_RIGHTS_AUDIT

Purpose: one entry per activity, simulation, lab, video, and external resource used across all 27 Answerable Biology decks, with source, rights status, and a TPT packaging verdict.

How to read this audit. Resources are grouped by source family. Each family header states the rights fields shared by every entry in it (creator/publisher, status, attribution, redistribution, modification, commercial reuse, include-file vs link-only, and whether independently written simplified directions can be sold). Per-resource rows carry the fields that vary: name, deck(s), URL, reachability, and verdict. Verdicts: **INCLUDE FILE** (the file may ship inside the TPT product), **LINK ONLY** (product links out; nothing copied in), **RIGHTS REVIEW NEEDED**.

The governing rule, applied to every entry below: **independently written, simplified directions for using a linked resource are Katherine's own instructional design and can be sold — almost always yes.** The one limit: never copy a protected resource's own directions, screenshots, worksheets, or answer keys closely enough to reproduce another creator's expression. Write directions from the classroom's point of view ("open the game, remove one species, record what happens"), not by paraphrasing the publisher's page.

Live checks were run 2026-08-08; full URL-by-URL results are in `BROKEN_LINK_REPORT.md` in this folder.

---

## 1. Katherine's own interactive models — the tank-and-flow sims

Creator/publisher: presumed Dr. Katherine von Duyke / Answerable Teaching (the decks present them as "Tap to open the interactive model and drag the sliders"; the GitHub org is `answerable-teaching`; the one live deployment carries no third-party branding). Status: **my original work — REVIEW WITH KATHERINE** to confirm she owns the code and any libraries used permit commercial distribution. Attribution: none required if hers. Redistribution: yes (hers). Modification: yes (hers). Commercial reuse: yes (hers). May include original file?: yes — she may ship the HTML or keep sims hosted and link; either is her call. Simplified directions sellable: yes (they are already hers).

Verified: the Netlify deployment (`hilarious-biscuit-630a42.netlify.app`) is live and is the **"Energy Tank Model — the 10% rule"** — a custom tank-and-flow teaching sim with sliders, no third-party author or license notice. This matches the deck's "Tap to open" language. Classified as her original work. `REVIEW WITH KATHERINE`

**Critical finding: every `answerable-teaching.github.io/tank-and-flow-models/*.html` URL returns 404, including the org root.** The GitHub Pages site is not deployed (or the repo was renamed/made private). Only the Netlify copy of the energy model is live. Eight of nine models currently have no working URL. `REVIEW WITH KATHERINE` — redeploy GitHub Pages or repoint all decks to Netlify URLs before publishing. `LINK NEEDED` for the eight dead models.

| Model | Deck(s)/Cycle(s) | URL | Live? | Verdict |
|---|---|---|---|---|
| Energy Tank Model (10% rule) — Netlify deploy | Cycle 02 Ecosystems & Feeding Relationships | https://hilarious-biscuit-630a42.netlify.app | 200 OK | INCLUDE FILE (or keep hosted + link) |
| Energy tank model — GitHub Pages | Cycle 03 Energy Flow & Trophic Pyramids | https://answerable-teaching.github.io/tank-and-flow-models/energy.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Carbon tank model | Cycle 04 Carbon Cycle; Cycle 20 Human Impact Capstone | https://answerable-teaching.github.io/tank-and-flow-models/carbon.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Photosynthesis tank model | Cycle 05 Photosynthesis | https://answerable-teaching.github.io/tank-and-flow-models/photosynthesis.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Respiration tank model | Cycle 06 Cellular Respiration & Fermentation | https://answerable-teaching.github.io/tank-and-flow-models/respiration.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Osmosis tank model | Cycle 09 Cell Membrane & Transport | https://answerable-teaching.github.io/tank-and-flow-models/osmosis.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Enzyme tank model | Cycle 10 Enzymes | https://answerable-teaching.github.io/tank-and-flow-models/enzyme.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Cell-cycle tank model | Cycle 11 The Cell Cycle to Cancer | https://answerable-teaching.github.io/tank-and-flow-models/cell-cycle.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Allele tank model | Cycle 18 Natural Selection & Adaptation | https://answerable-teaching.github.io/tank-and-flow-models/allele.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |
| Speciation tank model | Cycle 19 Speciation & Biodiversity | https://answerable-teaching.github.io/tank-and-flow-models/speciation.html | **404** | INCLUDE FILE once redeployed; LINK NEEDED now |

---

## 2. Katherine's own activities, card sets, labs, and handouts (no external source)

Creator/publisher: Dr. Katherine von Duyke (activities described entirely in her own slides, with her own card sets, stations, and guides; no external URL or publisher named). Status: **my original work — REVIEW WITH KATHERINE** to confirm none were adapted from a colleague's or district's materials. Attribution: n/a. Redistribution/modification/commercial: yes (hers). May include original file?: **yes — these should ship as printable files inside the TPT product.** Directions sellable: yes.

| Activity | Deck(s)/Cycle(s) | Materials | Verdict |
|---|---|---|---|
| Cups sorting / taxonomy lab-station activity | Classifying Organisms (Cycle 1) | cups at lab stations | INCLUDE FILE (write up as printable) |
| Species cards food-web build (Start/Finish your food web) | Cycle 02 | printable species card set | INCLUDE FILE |
| Symbiosis activity (short, Day 2) | Cycle 02 | slides + notes | INCLUDE FILE |
| Energy Flow Stations (4 stations, incl. Build the Pyramid card sort; Photosynthesis vs. Respiration card sort) | Cycle 03 | station cards | INCLUDE FILE |
| Do the Energy Math | Cycle 03 | worksheet | INCLUDE FILE |
| Where do trees get their mass? | Cycle 04 | discussion/writing activity | INCLUDE FILE |
| Van Helmont's willow tree | Cycle 05 | data-interpretation activity | INCLUDE FILE |
| Build a sugar molecule | Cycle 05 | molecular model kits (physical, purchased — see §8) | INCLUDE FILE (directions); kits purchased separately |
| Releasing the Energy in Food + CA1 Worksheet | Cycle 06 | Google Doc worksheet (see §3) | INCLUDE FILE |
| Screen-Door Sort (cards: oxygen, water, protein, salt ion, virus, CO2) | Cycle 09 | printable card set + Activity Guide | INCLUDE FILE |
| Build-a-Bilayer + Activity Guide | Cycle 09 | activity guide | INCLUDE FILE |
| Challenge: Oil, Water & the Bilayer | Cycle 09 | household materials | INCLUDE FILE |
| The Activation-Energy Hill | Cycle 10 | activity | INCLUDE FILE |
| Lock & Key Match | Cycle 10 | matching cards | INCLUDE FILE |
| Be the checkpoint (cell-condition cards) | Cycle 11 | printable card set | INCLUDE FILE |
| Case study: mitosis, cancer & vaccines | Cycle 11 | case study | INCLUDE FILE |
| PTC taste-paper activity | Cycle 13 Punnett | PTC paper (purchased consumable — see §8) | INCLUDE FILE (directions) |
| Cheek Cell Lab | Cycle 13 Punnett | microscopes, slides; no handout URL — `LINK NEEDED` (locate her lab sheet) | INCLUDE FILE once located |
| Drag-and-drop activities (x2) | Cycle 13 Punnett | in-deck slides | INCLUDE FILE |
| Unzip and Rebuild + Activity Guide | Cycle 14 | Google Doc guide (see §3) | INCLUDE FILE |
| Replication Assembly Line + Activity Guide | Cycle 14 | Google Doc guide (see §3) | INCLUDE FILE |
| Chargaff Check + Activity Guide | Cycle 14 | guide — no URL in deck; `LINK NEEDED` | INCLUDE FILE once located |
| Pipe-cleaner chromosome build · gene map · class allele survey | Cycle 15 Genes & Chromosomes | craft materials; graded activity marked `[ADD LINK]` — `LINK NEEDED` | INCLUDE FILE |
| Modeling Transcription with letter tiles | Cycle 15 Protein Synthesis | letter tiles (alternative to Gizmo, §7) | INCLUDE FILE |
| Galapagos Google Earth postcard task | Cycle 17 | Google Earth (free tool, link only); graded activity `[ADD DIRECT URL]` — `LINK NEEDED` | INCLUDE FILE (task sheet); LINK ONLY (Google Earth) |
| Variation vs. No Variation | Cycle 18 | activity | INCLUDE FILE |
| Same Trait, Two Environments (trait + environment cards) | Cycle 18 | printable cards | INCLUDE FILE |
| Battle of the Beaks | Cycle 18 | tweezers/clothespins/spoons + "seeds" | INCLUDE FILE — but see note below |
| HHMI lizards check sheet (for Lizards in an Evolutionary Tree, §6) | Cycle 19 | her check sheet alongside the linked HHMI activity | INCLUDE FILE if independently written — REVIEW WITH KATHERINE; must not paraphrase HHMI's worksheet (no-derivatives terms) |
| Anchoring Phenomena Research Assignment (sea otter / Aleutians) | Cycle 07 Population Ecology | no URL — `LINK NEEDED` / `SOURCE NOT YET LOCATED` | RIGHTS REVIEW NEEDED (see note) |
| Feeding Relationships in the Pacific Northwest activity | Cycle 07 Population Ecology | no URL — `LINK NEEDED` / `SOURCE NOT YET LOCATED` | RIGHTS REVIEW NEEDED (see note) |
| Measure your footprint | Cycle 20 | uses footprintcalculator.org (§7) | INCLUDE FILE (her directions); LINK ONLY (calculator) |
| Track an invader | Cycle 20 | uses NatGeo invasive-species page (§7) | INCLUDE FILE (her directions); LINK ONLY (NatGeo) |

Note on Battle of the Beaks: this is a widely circulated classic activity concept (beak tools competing for seeds). Activity *concepts* are not copyrightable; her slide directions are already written in her own words, so INCLUDE FILE is safe. Do not import any published Battle of the Beaks handout. `REVIEW WITH KATHERINE` only if her printed handout was taken from a published version.

Note on the Cycle 07 sea otter / Aleutian Islands anchoring-phenomena sequence: this storyline resembles published NGSS storyline units. The deck names two assignments with no URL and no author. Before packaging, confirm the research assignment and the Feeding Relationships activity are her own documents, not a district's or a published unit's. `REVIEW WITH KATHERINE` · `RIGHTS REVIEW NEEDED`.

---

## 3. Katherine's Google Docs / Drive materials

Creator/publisher: presumed Katherine (linked from her decks as the activity worksheets/guides; all publicly viewable without sign-in as of the check). Status: **my original work — REVIEW WITH KATHERINE** to confirm authorship of each. Rights: hers, so include-file is permitted — **convert each to a product file (PDF/DOCX) rather than selling links to live Google URLs**, and check each doc for pasted third-party images or text before packaging. Directions sellable: yes.

| Resource | Deck/Cycle | URL | Live? | Verdict |
|---|---|---|---|---|
| Worksheet/handout (Google Doc) | Cycle 03 | https://docs.google.com/document/d/1FkT60NzXXldA0lXlneufTsGY_3IV5_mNdaXnYkdVsnY/edit | 200, public | INCLUDE FILE after authorship + content check |
| Concept-question practice deck (Google Slides) | Cycle 03 | https://docs.google.com/presentation/d/13RT17nQTZhNtQCiOu-cpeBeXrCDc71Zb9lKMc7_Gzjs/edit | 200, public | INCLUDE FILE after check |
| Cellular Respiration — CA1 Worksheet (Google Doc) | Cycle 06 | https://docs.google.com/document/d/1agVVkf3bK0TWcb6yVfgGTp24AL_iQdrObjEzARqEFnQ/edit | 200, public | INCLUDE FILE after check |
| Activity Guide: Unzip and Rebuild (Google Doc) | Cycle 14 | https://docs.google.com/document/d/13KsLi7ncyMF0_rOoAGK5bgWHHaE5QWWJyN5PuQJAm5I/edit | 200, public | INCLUDE FILE after check |
| Activity Guide: Replication Assembly Line (Google Doc) | Cycle 14 | https://docs.google.com/document/d/1uDUphGPphtqcIG_in1NWSl26LS8JuDXmbBmMljB0GQo/edit | 200, public | INCLUDE FILE after check |
| Worksheet file (Google Drive PDF) | Cycle 02 | https://drive.google.com/file/d/17heyT0Y6KVcezjak08wq7Zr8SSNaJyxg/view | 200, public | RIGHTS REVIEW NEEDED — open and identify author before including |
| Materials folder (Google Drive) | Cycle 09 | https://drive.google.com/drive/folders/1BsqqCAa467Hs8Rkaenoa1z7kZT84_1Mo | 200, public | RIGHTS REVIEW NEEDED — inventory folder contents before including |

---

## 4. BioMan Biology games

Creator/publisher: BioMan Biology (biomanbio.com; independent teacher-built site). Status: **freely accessible but copyrighted** — the site states everything is "completely FREE to use" online, but publishes no redistribution or reuse license. Standard position: free-to-play online, **link-only**. Attribution: name the site when linking (courtesy, not a stated requirement). Redistribution of files: no (nothing to download anyway; games are hosted). Modification: no. Commercial reuse of their content: no. May include original file?: no — **LINK ONLY**. Simplified directions sellable: **yes** — e.g., "Open Snurfle Meiosis, complete the meiosis section, screenshot your completion screen" is her instructional design; never reproduce BioMan's in-game text or worksheets.

Site note: BioMan ran a platform upgrade (announced on the homepage); several old deep URLs now return persistent 500 errors while others work. Every dead BioMan link below needs its new URL looked up from the biomanbio.com menu. Also, one deck links `biomanbiology.com` — that domain does not resolve; the working domain is `biomanbio.com`.

| Game | Deck(s)/Cycle(s) | URL in deck | Live? | Verdict |
|---|---|---|---|---|
| BioMan Ecology Games (food web — remove one species) | Cycle 02 | https://biomanbiology.com (dead domain; also homepage-level only) | **000/dead** | LINK ONLY — `LINK NEEDED` (correct domain + direct game URL) |
| Photosynthesis game | Cycle 05 | https://www.biomanbio.com/HTML5/photosynthesis.html | **500** | LINK ONLY — `LINK NEEDED` (new URL after site upgrade) |
| Photosynthesis & Respiration game | Cycle 05 | https://www.biomanbio.com/HTML5/photosynthesisrespiration.html | **500** | LINK ONLY — `LINK NEEDED` |
| Cellular Respiration game (aerobic vs. anaerobic ATP tally) | Cycle 06 | https://www.biomanbio.com (homepage only) | 200 (homepage) | LINK ONLY — `LINK NEEDED` (direct game URL) |
| Cell Defense (membrane game) | Cycle 09 | https://biomanbio.com/HTML5GamesandLabs/Cellgames/celldefensehtml5page.html | 200 | LINK ONLY |
| Enzyme games | Cycle 10 | https://biomanbio.com/HTML5GamesandLabs/Enzymegames/enzymegames.html | **500** | LINK ONLY — `LINK NEEDED` |
| Snurfle Meiosis (& Genetics) | Cycle 12 (warm-up); Cycle 13 Punnett (fiddle) | https://biomanbio.com/HTML5GamesandLabs/Genegames/snurflemeiosishtml5page.html | 200 | LINK ONLY |
| BioMan cell specialization (warm-up) | Cycle 16 Stem Cell Differentiation | none in deck | — | LINK ONLY — `LINK NEEDED` |

---

## 5. PhET Interactive Simulations

Creator/publisher: PhET, University of Colorado Boulder. Status: **Creative Commons — CC BY 4.0** on the HTML5 sims (PhET's standard license; sim source code is separately licensed, some GPL). Attribution: required — "PhET Interactive Simulations, University of Colorado Boulder, https://phet.colorado.edu". Redistribution: **yes, permitted with attribution** (CC BY even allows bundling the HTML5 sim file). Modification: yes with attribution (but modifying sims is not needed here). Commercial reuse: **yes, permitted under CC BY 4.0** (PhET asks commercial users to follow the license terms). May include original file?: technically yes under CC BY — but recommended practice is **LINK ONLY** so students always get the current version; linking is simpler and unambiguous. Directions sellable: yes.

| Sim | Deck(s)/Cycle(s) | URL | Live? | Verdict |
|---|---|---|---|---|
| Membrane Channels | Cycle 09 | https://phet.colorado.edu/en/simulations/membrane-channels | 200 | LINK ONLY (note: legacy sim — verify it still runs in modern browsers; PhET runs legacy sims via emulation) |
| Natural Selection (direct HTML5) | Cycle 17 (bellringer/fiddle, "Bunny Lab" part 2) | https://phet.colorado.edu/sims/html/natural-selection/latest/natural-selection_en.html | 200 | LINK ONLY |
| Natural Selection (landing page) | Cycle 19 | https://phet.colorado.edu/en/simulations/natural-selection | 200 | LINK ONLY |

---

## 6. HHMI BioInteractive

Creator/publisher: Howard Hughes Medical Institute, BioInteractive. Status: **freely accessible but copyrighted** — HHMI terms (verified live 2026-08-08): free download/display **for educational purposes only**; **no redistribution beyond your institution**, **no derivative works/modification**, **no commercial use under any circumstances** without written permission; copyright notices must stay intact with attribution. May include original file?: **no — never package an HHMI PDF, video file, or Click & Learn inside a paid TPT product.** LINK ONLY. Simplified directions sellable: **yes** — her own student-facing prompts around a linked BioInteractive resource are her product; do not reproduce HHMI's worksheets or educator materials.

| Resource | Deck(s)/Cycle(s) | URL | Live? | Verdict |
|---|---|---|---|---|
| Living Together (bobtail squid, symbiosis) | Cycle 02 (Day 2 activity, ~20 min) | https://www.biointeractive.org/classroom-resources/living-together | 200 | LINK ONLY |
| Chains & Webs (Gorongosa) | Cycle 02 (linked only as biointeractive.org homepage) | https://www.biointeractive.org | 200 (homepage) | LINK ONLY — `LINK NEEDED` (direct resource URL) |
| The Eukaryotic Cell Cycle and Cancer (Click & Learn) | Cycle 11 (Day 2 case study support) | https://www.biointeractive.org/classroom-resources/eukaryotic-cell-cycle-and-cancer | 200 | LINK ONLY |
| Lizards in an Evolutionary Tree ("Lizards on Islands" activity) | Cycle 19 (Day 1 activity) | https://www.biointeractive.org/classroom-resources/lizards-evolutionary-tree | **404** | LINK ONLY — `LINK NEEDED` (find current URL on biointeractive.org) |
| Deep Time interactive (Click & Learn) | Cycle 17 | https://media.hhmi.org/biointeractive/click/deeptime/ | **unreachable** (connection failed; possibly retired/replaced by EarthViewer) | LINK ONLY — `LINK NEEDED` |
| HHMI Click and Learn on DNA/phylogeny + student answer document | Classifying Organisms (Cycle 1) | none in deck | — | LINK ONLY — `LINK NEEDED` (likely "Creating Phylogenetic Trees from DNA Sequences" or "Sorting Seashells"). The "student answer document" — if it is HHMI's, LINK ONLY; if hers, INCLUDE FILE. `REVIEW WITH KATHERINE` |
| The Making of a Theory: Darwin & Wallace (video, HHMI's own YouTube) | Cycle 17 | https://youtu.be/XOiUZ3ycZwU | live (verified via oEmbed) | LINK ONLY |

---

## 7. Other external free web resources (all LINK ONLY)

Shared position for this whole section unless noted: freely accessible but copyrighted by their publishers; no redistribution, no modification, no commercial reuse of their files/pages; attribution = name the source next to the link (good practice, required only where noted); may include original file? **no — LINK ONLY**; independently written simplified directions sellable: **yes**, for every entry.

| Resource | Creator/Publisher | Deck(s)/Cycle(s) | URL | Live? | Notes / Verdict |
|---|---|---|---|---|---|
| Pond Dip / "What's in a Drop?" microscopy pages | Microscopy-UK (Mic-UK; images Wim van Egmond) | Classifying Organisms | http://www.microscopy-uk.org.uk/index-no-ads.html?http://www.microscopy-uk.org.uk/ponddip/ | 200 | LINK ONLY. Deck credits a Wim van Egmond image and includes his contact email (egmond@tip.nl) — if his micrograph appears **inside the deck**, that embedded image is `RIGHTS REVIEW NEEDED` (get/confirm permission or replace) |
| News article (Acadiana) | The Advocate (commercial newspaper) | Classifying Organisms | https://www.theadvocate.com/acadiana/news/article_4f2c8962-fd3c-5fa7-87cf-048188f626e3.html | 200 | LINK ONLY; possible paywall for students — consider replacing. `REVIEW WITH KATHERINE` |
| Feed the Dingo (ecosystem game) | Smithsonian Science Education Center / PBS PLUM Landing (WGBH) | Cycle 03 (short sim) | https://ssec.si.edu/feed-the-dingo | **404** | LINK ONLY — `LINK NEEDED`; game has moved; find current host (PBS LearningMedia) or substitute |
| The Carbon Cycle Game (printable stations & dice) | NAGT (National Association of Geoscience Teachers) | Cycle 04 (Day 2 activity) | https://nagt.org (homepage only in deck) | 200 (homepage) | LINK ONLY — `LINK NEEDED` (direct activity URL, likely on serc.carleton.edu). NAGT/SERC materials are typically CC BY-NC-SA: even so, do NOT include their printables in a paid product (NC term); link and write her own directions |
| The Carbon Cycle (reference page) | UCAR Center for Science Education | Cycle 04 | https://scied.ucar.edu/learning-zone/how-climate-works/carbon-cycle | **403/404 — moved** | LINK ONLY — working replacement verified: https://scied.ucar.edu/learning-zone/earth-system/biogeochemical-cycles (200) |
| Modeling Photosynthesis lesson plan | California Academy of Sciences | Cycle 05 | https://www.calacademy.org/educators/lesson-plans/modeling-photosynthesis | **404** | LINK ONLY — `LINK NEEDED` (page moved or retired) |
| Photosynthesis in Leaf Disks (Leaf-Disk Float Lab source) | Science Buddies | Cycle 05 (Day 1 lab) | https://www.sciencebuddies.org/science-fair-projects/project-ideas/PlantBio_p070/plant-biology/photosynthesis-in-leaf-disks | **404** | LINK ONLY — `LINK NEEDED`. Science Buddies content is copyrighted, free for personal/classroom use only; never include their procedure PDF. Her lab handout must be independently written (it already is, per the deck) |
| Enzyme activity vs. temperature lab guide | Science Buddies | Cycle 10 (Day 2 lab) | https://www.sciencebuddies.org/science-fair-projects/project-ideas/BioChem_p012/biotechnology-techniques/how-enzyme-activity-changes-with-temperature | **404** | LINK ONLY — `LINK NEEDED` |
| Liver-Catalase extension lab ("catalase in action") | Science Buddies | Cycle 10 (optional challenge) | none in deck | — | LINK ONLY — `LINK NEEDED` |
| Yeast-Inflated Balloons (fermentation lab source) | Science World (British Columbia) | Cycle 06 (Day 2 lab) | https://www.scienceworld.ca/resource/yeast-inflated-balloons/ | 200 | LINK ONLY |
| Ecological succession article/image | Wikipedia (CC BY-SA) | Cycle 07 Populations & Succession (image credit) | https://en.wikipedia.org/wiki/Ecological_succession | 200 | Image reuse permitted incl. commercially **with CC BY-SA attribution and share-alike on the image**; keep the credit line on the slide. Verdict: INCLUDE (image w/ attribution) / LINK for article |
| Quizlet set | Quizlet (user-generated) | Cycle 12 | https://quizlet.com/_9iji1e?x=1qqt&i=26upnt | 403 (bot-blocked; presumed live — verify in browser) | LINK ONLY. If the set is Katherine's own, still LINK ONLY (Quizlet hosts it); if another user's, confirm it stays public. `REVIEW WITH KATHERINE` |
| CK-12 Biology concept pages (13 links) | CK-12 Foundation | Cycle 12 (12 links), Cycle 13 Punnett (1 link) | ck12.org/c/biology/... and /c/life-science/... (full list in BROKEN_LINK_REPORT) | all 200 | LINK ONLY. **CK-12 content is CC BY-NC + CK-12 curriculum license — NC means it cannot be included in a paid TPT product.** See deck-content flag below |
| Tour of the Basics (DNA/gene/chromosome warm-up game) | Learn.Genetics — Genetic Science Learning Center, University of Utah | Cycle 13 Mendelian; Cycle 15 Genes & Chromosomes (fiddle sim) | https://learn.genetics.utah.edu/content/basics/ | 200 | LINK ONLY. Utah GSLC content is copyrighted; free for nonprofit educational use; commercial redistribution requires permission (permissions page unreachable through proxy — position stated from standard GSLC policy) |
| Build a DNA Molecule (sim) | Learn.Genetics (Utah) | Cycle 14 (Day 1 short sim) | https://learn.genetics.utah.edu/content/basics/builddna/ | 200 | LINK ONLY |
| Gel electrophoresis virtual lab (warm-up) | Learn.Genetics (Utah), presumed | Cycle 16 Mutations & Gene Expression | none in deck | — | LINK ONLY — `LINK NEEDED` (likely learn.genetics.utah.edu gel electrophoresis page) |
| Karyotype sort (warm-up) | Learn.Genetics (Utah) — named "LearnGenetics" in deck | Cycle 16 Mutations & Genetic Disorders | none in deck | — | LINK ONLY — `LINK NEEDED` |
| Peppered Moths Game | Ask A Biologist, Arizona State University | Cycle 18 (bellringer + Day 1 one-minute hunt) | https://askabiologist.asu.edu/peppered-moths-game/play.html | 200 | LINK ONLY. ASU Ask A Biologist is free for classroom use; content copyrighted |
| OneZoom Tree of Life explorer | OneZoom CIO (UK charity; open-source viewer) | Cycle 19 (Day 2 activity) | https://www.onezoom.org | 200 | LINK ONLY |
| Invasive Species resource page | National Geographic Education | Cycle 20 (Track an invader) | https://education.nationalgeographic.org/resource/invasive-species/ | 200 | LINK ONLY |
| Ecological Footprint Calculator | Global Footprint Network | Cycle 20 (Measure your footprint) | https://www.footprintcalculator.org/ | 200 | LINK ONLY |
| World population live counter | Worldometers | Cycle 07 Population Ecology; Cycle 20 | https://www.worldometers.info/world-population/ | 200 | LINK ONLY |
| Google Earth (postcard task tool) | Google | Cycle 17 | no URL in deck (tool reference) | — | LINK ONLY (free tool; standard Google terms) |
| Google Images search link ("african tribe neck rings") | Google search URL | Cycle 17 | long google.com/search?... URL | 200 (search page) | **RIGHTS REVIEW NEEDED / REVIEW WITH KATHERINE** — a raw image-search URL is not a stable or classroom-safe resource, and the topic (Lamarckism example using Kayan neck rings) deserves a curated, respectful source. Replace before publishing |

---

## 8. Commercially licensed / purchased items

| Resource | Creator/Publisher | Deck(s)/Cycle(s) | URL | Status | Verdict |
|---|---|---|---|---|---|
| Gizmo: Protein Synthesis (transcription + translation) | ExploreLearning (Gizmos) | Cycle 15 Protein Synthesis (main activity, both days) | none in deck | **Commercially licensed — subscription required.** Schools must own a Gizmos license; no free public access beyond limited trials. No redistribution, no file inclusion, no reproduction of Gizmo student sheets | **RIGHTS REVIEW NEEDED** — the deck's central activity depends on a paid product buyers may not have. LINK ONLY + label "requires Gizmos subscription," and the deck already offers letter tiles as the no-subscription alternative — make that the default path. `REVIEW WITH KATHERINE` |
| Molecular model kits | lab-supply vendors | Cycle 05 (Build a sugar molecule) | — | Purchased physical supply | INCLUDE FILE (her directions); list kit as "materials needed" |
| PTC taste paper | lab-supply vendors | Cycle 13 Punnett | — | Purchased consumable | INCLUDE FILE (her directions); list as materials |
| Lab consumables (cups, spinach/baking soda, yeast/balloons, liver, tweezers/clothespins/spoons, pipe cleaners, microscope slides) | vendors | Cycles 1, 05, 06, 10, 13, 18 | — | Purchased supplies | No rights issue; materials lists ship in product |

---

## 9. YouTube videos (all LINK ONLY)

Creator/publisher: per-video channels (verified live via YouTube oEmbed 2026-08-08; titles and channels confirmed). Status: freely accessible but copyrighted; standard YouTube position — **embed/link only**; no downloading, re-uploading, clipping into the product, or including video files. Attribution: the link itself plus channel name. Redistribution/modification/commercial reuse of the videos: no. May include original file?: no — LINK ONLY. Simplified directions/viewing prompts sellable: yes.

| Video (verified title | channel) | Deck(s)/Cycle(s) | URL | Live? |
|---|---|---|---|
| How Two Microbes Changed History | PBS Eons | Classifying Organisms | https://www.youtube.com/watch?v=lhF5G2k45vY | yes |
| Ecosystems Ep. 1: What is an ecosystem? | The Wild Report | Cycle 02 | https://youtu.be/7cRgK0qG00E | yes |
| Where Do Trees Get Their Mass? | Veritasium | Cycle 04 | https://www.youtube.com/watch?v=2KZb2_vcNTg | yes |
| The Rebirth of Yellowstone | Crown Council | Cycle 07 Populations & Succession (slide text; not in links JSON) | https://www.youtube.com/watch?v=jJ0zqo1opv8 | yes |
| Mt. St. Helens: Mother Nature rebuilds | PBS NewsHour | Cycle 07 Populations & Succession | https://www.youtube.com/watch?v=YmrgoCUjHAw | yes |
| Glacier Bay: The Return of Life | GlacierBayNPS (NPS — US gov; video itself likely public domain, but treat as LINK ONLY) | Cycle 07 Populations & Succession | https://youtu.be/eEvRLAACNz4 | yes |
| The Invisible Universe of the Human Microbiome | NPR | Cycle 08 Cells & Organelles | https://youtu.be/5DTrENdWvvM | yes |
| A Tour of the Cell | CrashCourse | Cycle 08 Cell Organelles (slide text only) | https://www.youtube.com/watch?v=jsDxw63QqK0 | yes |
| Enzymes (Updated) | Amoeba Sisters | Cycle 10 | https://www.youtube.com/watch?v=qgVFkRn8f10 | yes |
| Spore Rain | New Atlantis WILD | Cycle 12 | http://www.youtube.com/watch?v=Mrphn1zOWaE | yes |
| Asexual Reproduction | MooMooMath and Science | Cycle 12 | http://www.youtube.com/watch?v=Mxmu3phxSHw | yes |
| Meiosis (Updated) | Amoeba Sisters | Cycle 12 | http://www.youtube.com/watch?v=VzDMG7ke69g | yes |
| Sea Star Regeneration | Clint Reynolds | Cycle 12 | http://www.youtube.com/watch?v=f7cXeWxxfD4 | yes |
| Budding Yeast Time-lapse | webiocosm | Cycle 12 | http://www.youtube.com/watch?v=iOvrq6ssy2Y | yes |
| Sexual Reproduction | Mark Drollinger | Cycle 12 | http://www.youtube.com/watch?v=tFZeyFbBLXE | yes |
| Among Us Punnett Square Practice part 3 | Ashley Stefanisin | Cycle 13 Punnett | http://www.youtube.com/watch?v=-x2oG32K2DM | yes |
| Routine genetic carrier screening | Northwell Health | Cycle 13 Punnett | http://www.youtube.com/watch?v=JQ6ZxuHuHxs | yes |
| How Mendel's pea plants helped us understand genetics | TED-Ed | Cycle 13 Punnett | http://www.youtube.com/watch?v=Mehz7tCxjSE | yes |
| What are Pedigree Charts | Mark Drollinger | Cycle 13 Punnett | http://www.youtube.com/watch?v=Wuk0W10EveU | yes |
| Gregor Mendel | Teacher's Pet | Cycle 13 Punnett | http://www.youtube.com/watch?v=cWt1RFnWNzk | yes |
| Alleles and Genes | Amoeba Sisters | Cycle 13 Punnett | http://www.youtube.com/watch?v=pv3Kj0UjiLE | yes |
| Punnett Square Practice AMONG US part 2 | Ashley Stefanisin | Cycle 13 Punnett | http://www.youtube.com/watch?v=sx0M2yPpA0k | yes |
| Among Us Punnett Square Practice #1 | Ashley Stefanisin | Cycle 13 Punnett | http://www.youtube.com/watch?v=vR-RwA9p9mQ | yes |
| Sexual and Asexual Reproduction Explained | Science Sauce | Cycle 13 Mendelian | https://youtu.be/co5jZId0F-g | yes |
| Advantages of Sexual and Asexual Reproduction | Science Sauce | Cycle 13 Mendelian | https://youtu.be/gAgyw72JiVA | yes |
| Are Your Traits Dominant? | BuzzFeed Multiplayer | Cycle 13 Mendelian | https://youtu.be/mnSkz8s-b44 | yes |
| Mutations | Bozeman Science | Cycle 16 Genetic Mutations | https://youtu.be/eDbK0cxKKsk | yes |
| How CRISPR lets you edit DNA | TED-Ed | Cycle 16 Mutations & Gene Expression | https://youtu.be/6tw_JVz_IEc | yes |
| Eyes of Nye — GMO foods | BallawdeQuincewold (re-upload of Disney/Nye content — **RIGHTS REVIEW NEEDED**: linking to an unofficial re-upload risks takedown; find official source) | Cycle 16 Mutations & Gene Expression | https://youtu.be/8z_CqyB1dQo | yes |
| How does DNA analysis work? | nzherald.co.nz | Cycle 16 Mutations & Gene Expression (slide text) | https://youtu.be/vVCnukppFik | yes |
| Teen gets his genes edited | CNN | Cycle 16 Mutations & Gene Expression (slide text) | https://youtu.be/0xv0CBujwZU | yes |
| How are GMOs Made? Hawaiian Papaya | GMO Answers (industry-funded source — `REVIEW WITH KATHERINE` for balance) | Cycle 16 Mutations & Gene Expression (slide text) | https://youtu.be/2G-yUuiqIZ0 | yes |
| All About Hemophilia, The Royal Blood Disease | Weird History | Cycle 16 Mutations & Genetic Disorders | https://youtu.be/fnqMq-QCJEo | yes |
| Endosymbiotic Theory | Amoeba Sisters | Cycle 17 | https://www.youtube.com/watch?v=FGnS-Xk0ZqU | yes |
| Darwin in the Galapagos | Nat Geo Animals | Cycle 17 | https://youtu.be/03YKT7ytJdE | yes |
| Earth's Entire History (Football Field) | NPR Skunk Bear | Cycle 17 | https://youtu.be/M8V_glRW1hA | yes |
| The Making of a Theory | biointeractive (HHMI official) | Cycle 17 | https://youtu.be/XOiUZ3ycZwU | yes |
| How the Civilization on Easter Island Collapsed | Weird History | Cycle 20 | https://youtu.be/R_r228ilv6Y | yes |

---

## 10. Deck-content rights flags (text and images inside the decks themselves)

These are not linked resources but expression embedded in the product files, so they belong in the rights audit:

1. **Cycle 12 (Reproduction & Meiosis) and Cycle 13 Punnett contain reading passages with embedded CK-12 crossref links** (13 ck12.org concept links woven through vocabulary text). This strongly suggests portions of the older deck prose were taken from CK-12 FlexBooks. CK-12 content is **CC BY-NC** — non-commercial — and **cannot be sold in a paid TPT product**. `RIGHTS REVIEW NEEDED` · `REVIEW WITH KATHERINE`: rewrite those passages in her own words (or verify they are original) before packaging Cycle 12/13.
2. **Cycle 16 Stem Cell Differentiation quotes/adapts NIH stem-cell reports** (NIH 2001/2002 citations throughout). US federal government works are **public domain** — inclusion is permitted; keep the citations. University of Wisconsin-Madison citation: their page text is copyrighted — verify only facts, not copied prose, were used. Low risk. `REVIEW WITH KATHERINE`
3. **Classifying Organisms deck credits a Wim van Egmond micrograph** (and carries his contact email). If his image is embedded in the deck, it is a copyrighted art photo — get permission or replace with a public-domain/CC micrograph. `RIGHTS REVIEW NEEDED`
4. **Cycle 08 / Cycle 08 Cells & Organelles image credits** point to Wikimedia Commons (CC BY-SA / public domain — fine with attribution kept), one OpenStax/cnx.org figure (CC BY — fine with attribution), and several **Google-Images redirect URLs rather than real sources** — resolve each to its actual source and license before sale. One credit points to earth.com (Cycle 16 M&GE) — copyrighted stock imagery; replace. `RIGHTS REVIEW NEEDED`
5. **Cycle 17 Google-Images search link** for a culturally sensitive example — replace with a curated source (see §7). `REVIEW WITH KATHERINE`

---

## Summary counts

- Resources inventoried: 100+ unique (103 unique URLs + 15 named activities/tools with no URL + physical kits).
- INCLUDE FILE: Katherine's own activities, card sets, guides, tank-and-flow sims (pending ownership confirmation), Wikimedia/OpenStax images with attribution.
- LINK ONLY: all BioMan, PhET (by choice; CC-BY would permit more), HHMI, Learn.Genetics, Science Buddies, CK-12, Quizlet, YouTube, and the other free web resources.
- RIGHTS REVIEW NEEDED: Gizmo dependency (Cycle 15), CK-12-derived prose (Cycles 12/13), Wim van Egmond image (Cycle 1), unresolved Google-Images credits (Cycles 08/16/17), Eyes of Nye re-upload (Cycle 16), Cycle 07 anchoring-phenomena documents, two Google Drive items of unknown authorship.
- Biggest operational finding: **all nine GitHub Pages tank-and-flow model URLs are 404** — the flagship "my original work" sims are currently unreachable except the one Netlify energy model.

Sources used: /root/ab_build/BUILD_BRIEF.md; /root/ab_build/extracted/_all_links.json; /root/ab_build/extracted/*.txt (all 27 decks); live HTTP checks and license-page fetches (phet.colorado.edu, hhmi.org/terms-of-use, biomanbio.com, hilarious-biscuit-630a42.netlify.app, scied.ucar.edu, YouTube oEmbed) run 2026-08-08.
