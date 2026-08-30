const L = require('./build_docs.js');
const { Document, Packer, LETTER, h1, kicker, h2, h3, p, mono, bullet, table, spacer } = L;
const fs = require('fs');

const body = [
  h1("The Claude Folder On Your Desktop"),
  kicker("What was in it · where each part went · 30 August 2026"),

  p("~/Desktop/Claude held 284 files and 156 megabytes across three folders. It had become the place things landed rather than the place anything lived, which is the specific problem this document closes: none of it was backed up, and some of it was the only copy."),
  p("This account says what was there, what was already safe, and where each part went."),

  h2("What was in it"),
  table(
    [{ t: "Folder", w: 3000 }, { t: "Files", w: 900 }, { t: "Size", w: 900 }, { t: "What it held", w: 5280 }],
    [
      ["AT_docs/", "17", "308 KB", "The written work — the nine documents, in four numbered subfolders, plus a stale copy of three skills and an inventory prompt."],
      ["Projects/", "7", "88 KB", "The book project: instructions, a finishing map, decisions and citations, and a manuscript skill with two scripts."],
      ["Answerable Teaching TPT/", "251", "156 MB", "A local copy of the TPT shared drive and the Biology deck archive. Seven zip archives account for about 110 MB of it."],
    ],
    { code: [0] }
  ),

  h2("AT_docs — the written work"),
  p("This is the folder the nine documents came from. Comparing every file against the repository:"),
  h3("Already in the repository, identical"),
  bullet("02_lezir_curriculum_case, 10_visibility_ladder, coordination_judgment_and_the_package, 03_lezir_book_notes, 06_simultaneity_positioning, 07_bio_ed_research_reading, and skills_audit.py. Seven files, all matched byte for byte.", ""),
  h3("In the repository, but the repository copy is newer"),
  bullet("01_deck_work_sequence, 08_nine_moves_attribution and 09_synthesis_sequenced differ only because the repository copies were edited on 30 August — cross-references rewritten in all three, and two restored passages added to section 9 of the synthesis. The Desktop copies are the earlier versions.", ""),
  h3("Only on the Desktop"),
  bullet("the inventory prompt that deck_inventory_job.md supersedes. Worth keeping as the record of what changed and why.", "11_claude_code_prompt_inventory.md — "),
  bullet("says the three skills beside it are stale. It was right — they are earlier versions of vt-bio-skill, vt-deck-authoring and vt-fusion-retrofit, which live in the repository.", "README_STALE_WARNING.md — "),
  bullet("Desktop copies of vt-bio-skill and vt-deck-authoring. Superseded, and the warning file beside them says so.", ""),

  h2("Where each part went"),
  table(
    [{ t: "What", w: 3000 }, { t: "Went to", w: 3000 }, { t: "Why", w: 4080 }],
    [
      ["The nine documents", "Already there — docs/book and docs/curriculum", "Named and committed on 30 August. The Desktop copies are the earlier drafts."],
      ["The superseded inventory prompt", "prompts/ in the repository", "It is the record of what the current job prompt replaced."],
      ["The stale skill copies and their warning", "archive/ in the repository", "Kept as the record that they were stale, not as working files."],
      ["The book project instructions", "docs/book-project/ in the repository", "Decisions & Citations and the Finishing Map were already in reference/, identical."],
      ["render_reading.py and check_consistency.py", "skills/manuscript-ops/ — the only copy now", "See below. This is the one that mattered."],
      ["The TPT local copy", "Already covered", "docs/tpt-drive-snapshot holds the Drive folder it mirrors. The deck archive is the Aug 17 build, superseded by the 24 swept decks."],
      ["The zip archives", "Left on the Desktop", "About 110 MB of opaque build archives. See below."],
    ]
  ),

  h2("The one that mattered"),
  p("The manuscript-ops skill names scripts/render_reading.py and scripts/check_consistency.py in four separate places — twice in its description of what it does, twice as commands to run. Neither script was in the repository. A live skill had been documenting two capabilities it could not perform."),
  p("Searching for them turned up three copies, not one:"),
  table(
    [{ t: "Where", w: 4200 }, { t: "What it was", w: 5880 }],
    [
      ["~/Desktop/Claude/Projects/…/SKILLS/", "The working copy. Unbacked-up, and the reason this was worth finding."],
      ["~/code/katherine-ops/plugins/…/", "Inside the retired plugin folder, which had been merged into the repository but not removed."],
      ["~/code/answerable-skills/skills/manuscript-ops/", "Added on 30 August from the Desktop copy."],
    ],
    { code: [0] }
  ),
  p("All three were byte-identical, so nothing had drifted yet — which is luck rather than design, and the reason to consolidate now rather than after a divergence."),
  p("The repository is now the only copy. The other two were deleted, each checked against the repository file first. sample_chapter.md moved from scripts/ to tests/, matching where katherine-ops kept it; the SKILL.md names neither path, so a fixture did not belong beside the scripts."),
  h3("What is left of katherine-ops"),
  p("23 of its 29 files already matched the repository. The six that did not are plugin scaffolding — marketplace.json, plugin.json, .mcp.json and the READMEs — which is what makes it an installable plugin rather than a folder of skills. Those are preserved in archive/katherine-ops-plugin-scaffolding/."),
  p("The folder itself is still at ~/code/katherine-ops. It now holds nothing the repository lacks, so it can be deleted — but retiring a git repository is a decision rather than a cleanup, so it was left alone.", { soft: true }),
  h3("The copy that could not be checked"),
  p("Your Answerable-Teaching repository has its own scripts/ folder and is not cloned on this machine, so whether a fourth copy lives there could not be verified from here. If it does, that is the one that will drift, because nothing above touched it.", { soft: true }),

  h2("The zip archives, and why they were left"),
  p("Four zips in VT_v2_deck_build come to about 100 MB, and a fifth holds the v1 pipeline workspace. They are compressed snapshots of deck builds that have since been superseded twice — once by the v3 relinked decks, and again by the 24 decks swept on 29 August."),
  p("Putting them in the repository would roughly double its size with material that cannot be read, diffed, or searched, and that duplicates work already done. Leaving them where they are costs nothing until the Desktop is cleared."),
  p("If you want them kept, the right home is a cold archive rather than the working repository — a single folder on Drive, or an external disk. Say which and it takes one command.", { soft: true }),

  h2("What this means for the Desktop folder"),
  p("Everything in ~/Desktop/Claude except the zip archives is now either in the repository or verifiably duplicated by something that is. The folder is no longer the only copy of anything."),
  p("Eight stale files were deleted from it — the four in the book project's SKILLS folder, and the four skill copies in AT_docs/3_SKILLS_desktop that a README beside them had correctly flagged as stale. Each was compared against its repository copy before deletion, and the check was written to refuse rather than proceed on a mismatch."),
  p("That was the risk worth closing. What to do with the folder itself is yours — it can be deleted, or left as a working scratch space now that nothing depends on it."),
];

const doc = new Document({
  creator: "Katherine von Duyke",
  title: "The Claude Folder On Your Desktop — 30 August 2026",
  styles: { default: { document: { run: { font: "Aptos", size: 21 } } } },
  sections: [{ properties: { page: LETTER }, children: body }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("/home/claude/out/2026-08-30 — The Claude Folder On Your Desktop.docx", b);
  console.log("written");
});
