# BROKEN_LINK_REPORT

Purpose: every URL found across the 27 Answerable Biology decks, with live HTTP status (checked 2026-08-08), plus a LINK NEEDED list for activities named in decks with no URL.

Method: all 103 unique URLs from `_all_links.json` plus 5 URLs found only in slide text were tested with browser-headed GET requests (redirects followed). YouTube returned proxy rate-limits (429) on direct fetch, so every video was verified individually via YouTube's oEmbed API — title and channel confirmed for all 38 videos. License pages were fetched where relevant. Statuses: OK = 200 · DEAD = 404/000/500 persistent · BLOCKED = bot-blocked but presumed live (verify once in a normal browser).

## Standard license positions for the recurring link classes

- **PhET simulations** — HTML5 sims are CC BY 4.0 (attribution: PhET Interactive Simulations, University of Colorado Boulder). Linking, embedding, redistribution, and commercial reuse permitted with attribution. Recommended handling here: link only.
- **BioMan Biology games** — free to play online; no reuse license published. Link only. Site recently upgraded platform; several old deep URLs now 500.
- **Katherine's netlify/github.io tank-and-flow models** — her original work (REVIEW WITH KATHERINE to confirm); may be included as files or hosted. Currently only the Netlify energy model is live; the entire github.io project 404s.
- **YouTube videos** — standard YouTube terms: embed/link only; no downloading or repackaging. All 38 verified live.
- **HHMI BioInteractive** — free for educational use; no redistribution, modification, or commercial use. Link only.
- **Learn.Genetics (Utah GSLC)** — copyrighted; free nonprofit educational use; link only.
- **CK-12** — CC BY-NC; cannot be included in a paid product; link only.

---

## 1. Dead or broken links (fix before publishing)

| URL | Deck(s) | Status | Diagnosis / action |
|---|---|---|---|
| https://answerable-teaching.github.io/tank-and-flow-models/energy.html | Cycle 03 | **404** | Entire github.io org root also 404s — GitHub Pages not deployed or repo renamed/private. Redeploy or repoint to Netlify. REVIEW WITH KATHERINE |
| https://answerable-teaching.github.io/tank-and-flow-models/carbon.html | Cycles 04, 20 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/photosynthesis.html | Cycle 05 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/respiration.html | Cycle 06 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/osmosis.html | Cycle 09 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/enzyme.html | Cycle 10 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/cell-cycle.html | Cycle 11 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/allele.html | Cycle 18 | **404** | same |
| https://answerable-teaching.github.io/tank-and-flow-models/speciation.html | Cycle 19 | **404** | same |
| https://biomanbiology.com | Cycle 02 | **000 (domain does not resolve)** | Wrong domain; site is biomanbio.com. Replace with direct ecology-games URL |
| https://www.biomanbio.com/HTML5/photosynthesis.html | Cycle 05 | **500 (persistent)** | BioMan platform upgrade broke old paths; find new game URL from biomanbio.com |
| https://www.biomanbio.com/HTML5/photosynthesisrespiration.html | Cycle 05 | **500 (persistent)** | same |
| https://biomanbio.com/HTML5GamesandLabs/Enzymegames/enzymegames.html | Cycle 10 | **500 (persistent)** | same |
| https://ssec.si.edu/feed-the-dingo | Cycle 03 | **404** | Feed the Dingo removed from Smithsonian SSEC; locate current host (PBS LearningMedia / PLUM Landing) or substitute a food-web sim. LINK NEEDED |
| https://scied.ucar.edu/learning-zone/how-climate-works/carbon-cycle | Cycle 04 | **403/404 (moved)** | Working replacement verified: https://scied.ucar.edu/learning-zone/earth-system/biogeochemical-cycles (200) |
| https://www.calacademy.org/educators/lesson-plans/modeling-photosynthesis | Cycle 05 | **404** | Lesson plan moved/retired; find current CalAcademy URL or drop. LINK NEEDED |
| https://www.sciencebuddies.org/science-fair-projects/project-ideas/PlantBio_p070/plant-biology/photosynthesis-in-leaf-disks | Cycle 05 | **404** | Science Buddies re-slugged project pages; search "photosynthesis leaf disks" on sciencebuddies.org. LINK NEEDED |
| https://www.sciencebuddies.org/science-fair-projects/project-ideas/BioChem_p012/biotechnology-techniques/how-enzyme-activity-changes-with-temperature | Cycle 10 | **404** | same. LINK NEEDED |
| https://www.biointeractive.org/classroom-resources/lizards-evolutionary-tree | Cycle 19 | **404** | Resource renamed/moved on biointeractive.org ("Lizards in an Evolutionary Tree"); find current URL. LINK NEEDED |
| https://media.hhmi.org/biointeractive/click/deeptime/ | Cycle 17 | **UNREACHABLE (connection failed; robots/SSL block on retry)** | Old Deep Time click-and-learn likely retired (successor: HHMI EarthViewer). Verify in browser; replace. LINK NEEDED |

## 2. Blocked but presumed live (verify once in a normal browser)

| URL | Deck(s) | Status | Note |
|---|---|---|---|
| https://quizlet.com/_9iji1e?x=1qqt&i=26upnt | Cycle 12 | 403 (bot block) | Quizlet blocks non-browser clients; also confirm the set is still public |

## 3. Live and OK

| URL | Deck(s) | Status |
|---|---|---|
| http://www.microscopy-uk.org.uk/index-no-ads.html?http://www.microscopy-uk.org.uk/ponddip/ | Classifying Organisms | 200 |
| https://www.theadvocate.com/acadiana/news/article_4f2c8962-fd3c-5fa7-87cf-048188f626e3.html | Classifying Organisms | 200 (possible paywall) |
| https://hilarious-biscuit-630a42.netlify.app | Cycle 02 | 200 — verified: "Energy Tank Model — the 10% rule" |
| https://drive.google.com/file/d/17heyT0Y6KVcezjak08wq7Zr8SSNaJyxg/view | Cycle 02 | 200, publicly viewable |
| https://www.biointeractive.org | Cycle 02 | 200 |
| https://www.biointeractive.org/classroom-resources/living-together | Cycle 02 | 200 |
| https://docs.google.com/document/d/1FkT60NzXXldA0lXlneufTsGY_3IV5_mNdaXnYkdVsnY/edit | Cycle 03 | 200, publicly viewable |
| https://docs.google.com/presentation/d/13RT17nQTZhNtQCiOu-cpeBeXrCDc71Zb9lKMc7_Gzjs/edit | Cycle 03 | 200, publicly viewable |
| https://nagt.org | Cycle 04 | 200 (homepage only — direct activity link needed, see §4) |
| https://docs.google.com/document/d/1agVVkf3bK0TWcb6yVfgGTp24AL_iQdrObjEzARqEFnQ/edit | Cycle 06 | 200, publicly viewable |
| https://www.biomanbio.com | Cycle 06 | 200 (homepage only — direct game link needed, see §4) |
| https://www.scienceworld.ca/resource/yeast-inflated-balloons/ | Cycle 06 | 200 |
| https://en.wikipedia.org/wiki/Ecological_succession | Cycle 07 P&S | 200 |
| https://biomanbio.com/HTML5GamesandLabs/Cellgames/celldefensehtml5page.html | Cycle 09 | 200 |
| https://drive.google.com/drive/folders/1BsqqCAa467Hs8Rkaenoa1z7kZT84_1Mo | Cycle 09 | 200, publicly viewable |
| https://phet.colorado.edu/en/simulations/membrane-channels | Cycle 09 | 200 (legacy sim — confirm it runs in modern browsers) |
| https://www.biointeractive.org/classroom-resources/eukaryotic-cell-cycle-and-cancer | Cycle 11 | 200 |
| https://www.ck12.org/c/biology/animals | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/body-cells?referrer=crossref | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/cells?referrer=crossref | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/characteristics-of-life | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/chromosomes?referrer=crossref | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/reproduction | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/reptiles | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/sexual-reproduction?referrer=crossref | Cycle 12 | 200 |
| https://www.ck12.org/c/biology/species | Cycle 12 | 200 |
| https://www.ck12.org/c/life-science/cell-division?referrer=crossref | Cycle 12 | 200 |
| https://www.ck12.org/c/life-science/fertilization?referrer=crossref | Cycle 12 | 200 |
| https://www.ck12.org/c/life-science/sperm?referrer=crossref | Cycle 12 | 200 |
| https://biomanbio.com/HTML5GamesandLabs/Genegames/snurflemeiosishtml5page.html | Cycle 13 Punnett | 200 |
| https://www.ck12.org/c/biology/probability?referrer=crossref | Cycle 13 Punnett | 200 |
| https://learn.genetics.utah.edu/content/basics/ | Cycle 13 Mendelian; Cycle 15 G&C | 200 |
| https://docs.google.com/document/d/13KsLi7ncyMF0_rOoAGK5bgWHHaE5QWWJyN5PuQJAm5I/edit | Cycle 14 | 200, publicly viewable |
| https://docs.google.com/document/d/1uDUphGPphtqcIG_in1NWSl26LS8JuDXmbBmMljB0GQo/edit | Cycle 14 | 200, publicly viewable |
| https://learn.genetics.utah.edu/content/basics/builddna/ | Cycle 14 | 200 |
| https://phet.colorado.edu/sims/html/natural-selection/latest/natural-selection_en.html | Cycle 17 | 200 |
| https://www.google.com/search?...q=african+tribe+neck+rings... | Cycle 17 | 200 (search page loads, but replace — see audit §7) |
| https://askabiologist.asu.edu/peppered-moths-game/play.html | Cycle 18 | 200 |
| https://phet.colorado.edu/en/simulations/natural-selection | Cycle 19 | 200 |
| https://www.onezoom.org | Cycle 19 | 200 |
| https://education.nationalgeographic.org/resource/invasive-species/ | Cycle 20 | 200 |
| https://www.footprintcalculator.org/ | Cycle 20 | 200 |
| https://www.worldometers.info/world-population/ | Cycle 07 PE; Cycle 20 | 200 |
| mailto:egmond@tip.nl | Classifying Organisms | skipped (email address, not a link) |

YouTube — all verified live via oEmbed (direct fetches hit proxy rate-limit 429, not a link problem):

| URL | Deck(s) | Verified title/channel |
|---|---|---|
| https://www.youtube.com/watch?v=lhF5G2k45vY | Classifying Organisms | How Two Microbes Changed History — PBS Eons |
| https://youtu.be/7cRgK0qG00E | Cycle 02 | What is an ecosystem? — The Wild Report |
| https://www.youtube.com/watch?v=2KZb2_vcNTg | Cycle 04 | Where Do Trees Get Their Mass? — Veritasium |
| https://www.youtube.com/watch?v=jJ0zqo1opv8 | Cycle 07 P&S (slide text) | The Rebirth of Yellowstone — Crown Council |
| https://www.youtube.com/watch?v=YmrgoCUjHAw | Cycle 07 P&S | Mt. St. Helens rebuilds — PBS NewsHour |
| https://youtu.be/eEvRLAACNz4 | Cycle 07 P&S | Glacier Bay: The Return of Life — GlacierBayNPS |
| https://youtu.be/5DTrENdWvvM | Cycle 08 C&O | Human Microbiome — NPR |
| https://www.youtube.com/watch?v=jsDxw63QqK0 | Cycle 08 CO (slide text) | A Tour of the Cell — CrashCourse |
| https://www.youtube.com/watch?v=qgVFkRn8f10 | Cycle 10 | Enzymes (Updated) — Amoeba Sisters |
| http://www.youtube.com/watch?v=Mrphn1zOWaE | Cycle 12 | Spore Rain — New Atlantis WILD |
| http://www.youtube.com/watch?v=Mxmu3phxSHw | Cycle 12 | Asexual Reproduction — MooMooMath |
| http://www.youtube.com/watch?v=VzDMG7ke69g | Cycle 12 | Meiosis (Updated) — Amoeba Sisters |
| http://www.youtube.com/watch?v=f7cXeWxxfD4 | Cycle 12 | Sea Star Regeneration — Clint Reynolds |
| http://www.youtube.com/watch?v=iOvrq6ssy2Y | Cycle 12 | Budding Yeast Time-lapse — webiocosm |
| http://www.youtube.com/watch?v=tFZeyFbBLXE | Cycle 12 | Sexual Reproduction — Mark Drollinger |
| http://www.youtube.com/watch?v=-x2oG32K2DM | Cycle 13 Punnett | Among Us Punnett part 3 — Ashley Stefanisin |
| http://www.youtube.com/watch?v=JQ6ZxuHuHxs | Cycle 13 Punnett | Genetic carrier screening — Northwell Health |
| http://www.youtube.com/watch?v=Mehz7tCxjSE | Cycle 13 Punnett | Mendel's pea plants — TED-Ed |
| http://www.youtube.com/watch?v=Wuk0W10EveU | Cycle 13 Punnett | Pedigree Charts — Mark Drollinger |
| http://www.youtube.com/watch?v=cWt1RFnWNzk | Cycle 13 Punnett | Gregor Mendel — Teacher's Pet |
| http://www.youtube.com/watch?v=pv3Kj0UjiLE | Cycle 13 Punnett | Alleles and Genes — Amoeba Sisters |
| http://www.youtube.com/watch?v=sx0M2yPpA0k | Cycle 13 Punnett | Among Us Punnett part 2 — Ashley Stefanisin |
| http://www.youtube.com/watch?v=vR-RwA9p9mQ | Cycle 13 Punnett | Among Us Punnett #1 — Ashley Stefanisin |
| https://youtu.be/co5jZId0F-g | Cycle 13 Mendelian | Sexual & Asexual Reproduction — Science Sauce |
| https://youtu.be/gAgyw72JiVA | Cycle 13 Mendelian | Advantages of Sexual & Asexual — Science Sauce |
| https://youtu.be/mnSkz8s-b44 | Cycle 13 Mendelian | Are Your Traits Dominant? — BuzzFeed Multiplayer |
| https://youtu.be/eDbK0cxKKsk | Cycle 16 GM | Mutations — Bozeman Science |
| https://youtu.be/6tw_JVz_IEc | Cycle 16 M&GE | How CRISPR lets you edit DNA — TED-Ed |
| https://youtu.be/8z_CqyB1dQo | Cycle 16 M&GE | Eyes of Nye GMO foods — unofficial re-upload (rights flag in audit) |
| https://youtu.be/vVCnukppFik | Cycle 16 M&GE (slide text) | How does DNA analysis work? — nzherald |
| https://youtu.be/0xv0CBujwZU | Cycle 16 M&GE (slide text) | Teen gene-edited — CNN |
| https://youtu.be/2G-yUuiqIZ0 | Cycle 16 M&GE (slide text) | GMO Hawaiian Papaya — GMO Answers |
| https://youtu.be/fnqMq-QCJEo | Cycle 16 M&GD | All About Hemophilia — Weird History |
| https://www.youtube.com/watch?v=FGnS-Xk0ZqU | Cycle 17 | Endosymbiotic Theory — Amoeba Sisters |
| https://youtu.be/03YKT7ytJdE | Cycle 17 | Darwin in the Galapagos — Nat Geo |
| https://youtu.be/M8V_glRW1hA | Cycle 17 | Earth's History on a Football Field — NPR Skunk Bear |
| https://youtu.be/XOiUZ3ycZwU | Cycle 17 | The Making of a Theory — HHMI biointeractive |
| https://youtu.be/R_r228ilv6Y | Cycle 20 | Easter Island Collapse — Weird History |

---

## 4. LINK NEEDED — activities named in decks with no URL (or homepage-only link)

| # | Activity as named in deck | Deck/Cycle | What's needed |
|---|---|---|---|
| 1 | HHMI Click and Learn (DNA/phylogeny) + student answer document | Classifying Organisms (Cycle 1) | Direct biointeractive.org URL (likely "Creating Phylogenetic Trees from DNA Sequences" or "Sorting Seashells"); confirm whose answer document |
| 2 | BioMan Ecology Games (food-web species-removal sim) | Cycle 02 | Direct game URL on biomanbio.com (deck links dead domain biomanbiology.com) |
| 3 | Chains & Webs (Gorongosa) — biointeractive | Cycle 02 | Direct resource URL (deck links homepage only) |
| 4 | Feed the Dingo | Cycle 03 | New host URL (ssec.si.edu page 404) |
| 5 | NAGT "The Carbon Cycle Game" (printable stations & dice) | Cycle 04 | Direct activity URL (deck links nagt.org homepage; activity likely on serc.carleton.edu) |
| 6 | Science Buddies leaf-disk photosynthesis lab guide | Cycle 05 | Re-slugged sciencebuddies.org URL |
| 7 | CalAcademy "Modeling Photosynthesis" lesson plan | Cycle 05 | New/retired — replacement URL or drop |
| 8 | BioMan Cellular Respiration game (ATP tally) | Cycle 06 | Direct game URL (deck links homepage only) |
| 9 | Anchoring Phenomena Research Assignment (sea otters) | Cycle 07 Population Ecology | Locate the actual assignment document; SOURCE NOT YET LOCATED |
| 10 | Feeding Relationships in the Pacific Northwest activity | Cycle 07 Population Ecology | Locate the activity document; SOURCE NOT YET LOCATED |
| 11 | BioMan enzyme games | Cycle 10 | New URL after BioMan upgrade (old URL 500s) |
| 12 | Science Buddies catalase extension lab ("catalase in action") | Cycle 10 | URL never present in deck |
| 13 | Cheek Cell Lab handout | Cycle 13 Punnett | Locate her lab sheet |
| 14 | Chargaff Check activity guide | Cycle 14 | Guide named but no URL (the other two Cycle 14 guides have Google Doc links) |
| 15 | Graded activity "[ADD LINK]" | Cycle 15 Genes & Chromosomes | Placeholder in teacher slide — Schoology/product link |
| 16 | Gizmo: Protein Synthesis | Cycle 15 Protein Synthesis | ExploreLearning URL + "requires Gizmos subscription" label |
| 17 | Gel electrophoresis virtual lab (warm-up) | Cycle 16 Mutations & Gene Expression | Likely learn.genetics.utah.edu — direct URL |
| 18 | Karyotype sort (LearnGenetics warm-up) | Cycle 16 Mutations & Genetic Disorders | Direct learn.genetics.utah.edu URL |
| 19 | BioMan cell specialization (warm-up) | Cycle 16 Stem Cell Differentiation | Direct game URL |
| 20 | Graded activity "[ADD DIRECT URL]" + "[ADD SCHOOLOGY URL]" | Cycle 17 Darwin & Evidence | Placeholders in teacher slide |
| 21 | Galapagos Google Earth postcard task | Cycle 17 | Google Earth link/tour URL if one exists |
| 22 | Lizards in an Evolutionary Tree | Cycle 19 | Current biointeractive.org URL (old one 404) |
| 23 | Deep Time interactive | Cycle 17 | Current HHMI URL or replacement (media.hhmi.org unreachable) |
| 24 | Tank-and-flow models x9 (8 with no working URL; the energy model's Netlify copy is live) (energy, carbon, photosynthesis, respiration, osmosis, enzyme, cell-cycle, allele, speciation) | Cycles 03–06, 09–11, 18–19, 20 | Redeploy github.io or publish Netlify URLs — only the Cycle 02 Netlify energy model is live |

Totals: 108 URLs tested (103 from _all_links.json incl. 1 mailto skipped; 5 additional from slide text). 20 dead/broken (9 of them Katherine's own sim URLs), 1 bot-blocked, 87 live (38 YouTube verified via oEmbed).

Sources used: /root/ab_build/extracted/_all_links.json; /root/ab_build/extracted/*.txt (all 27 decks); live HTTP checks 2026-08-08.
