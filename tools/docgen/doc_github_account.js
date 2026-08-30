const L = require('./build_docs.js');
const { Document, Packer, LETTER, h1, kicker, h2, h3, p, mono, bullet, table, spacer } = L;
const fs = require('fs');

const W = 10080; // usable width in DXA

const body = [
  h1("What Is In GitHub"),
  kicker("Answerable Skills · repository account · 30 August 2026"),

  p("This is a reading copy. The repository itself is a private GitHub repo called answerable-skills, and it is the canonical home for every script, skill and working document behind the Biology curriculum. Canonical means that when a file exists both here and on Drive, this is the one that counts."),
  p("The reason it is canonical was your decision on 29 August, and it holds up: you reorganise Drive for readability, which breaks paths and IDs that scripts depend on, and you work from a machine where you do not want every Drive account syncing down. A repository does not care how it is arranged on screen, and it can be cloned to one machine without dragging four accounts with it."),
  p("The cost is the one that produced this document: a repository is not readable the way a Drive folder is. So this account gets written whenever the repository changes materially, and it lives on Drive, where you can open it."),

  h2("Where it is"),
  mono("GitHub    kvond/answerable-skills  (private)"),
  mono("Your Mac  ~/code/answerable-skills"),
  mono("Skills    ~/.claude/skills  reads from the repo, so every surface uses one copy"),
  spacer(),
  p("Seventeen commits, sixteen of them from 29 and 30 August. Nothing is on GitHub until a push runs from ~/code/answerable-skills, and as of this writing seven commits are local only.", { soft: true }),

  h2("What is in it"),
  table(
    [{ t: "Folder", w: 2000 }, { t: "Files", w: 1000 }, { t: "What it is", w: 7080 }],
    [
      ["skills/", "19", "The interactive skills. This folder is what ~/.claude/skills points at, so editing a skill here changes it on every machine and in every Claude surface at once."],
      ["scripts/", "18", "The deck and feedback pipeline. Everything that reads, checks, or rewrites a deck."],
      ["docs/", "110", "The written work, the TPT material, the deck-ID map and the import runbook."],
      ["audits/", "17", "Dated read-only outputs. Records of what a deck set looked like on a given day."],
      ["prompts/", "1", "Standalone job prompts written to be handed to another session."],
      ["tools/", "1", "skills_audit.py, which reports what skills exist and where."],
      ["reference/", "3", "Reference material that is not a skill and not a script."],
      ["archive/", "1", "Retired material kept deliberately."],
    ],
    { code: [0], boldFirst: false }
  ),

  h2("The nineteen skills"),
  p("A skill is a folder holding a SKILL.md that tells Claude how to do one recurring job. They are grouped here by what they serve."),
  h3("Biology deck work"),
  bullet("finishes a Biology cycle deck to the shipping standard. The largest and most exacting of them.", "vt-bio-skill — "),
  bullet("builds a new Variation Theory cycle deck from content, for any science course.", "vt-deck-authoring — "),
  bullet("diagnoses an existing deck for coordination work and proposes one fusion slide to accept or reject.", "vt-fusion-retrofit — "),
  bullet("the student feedback pipeline, A to B1 to B2 to C, human-gated at each step.", "formative-pipeline-v2 — "),
  h3("Book and research"),
  bullet("tag and page hygiene for the Roam book graph, and the gate that runs before any page is created.", "book-ops — "),
  bullet("routes captures into chapter banks and registers new zettels.", "chapter-bank — "),
  bullet("stages, renders and checks the manuscript. Never writes prose.", "manuscript-ops — "),
  bullet("critique against Harvard Education Press standards. Applies to any manuscript question, including a bare \"what do you think?\"", "hep-scout — "),
  h3("Writing and daily work"),
  bullet("writing-block, learning-block, block-update, daily-brief, daily-agenda, activity-scout, task-distill.", ""),
  h3("Other"),
  bullet("Simplified Technical English, on explicit invocation only.", "ste — "),
  bullet("photo-album-reconcile, panama-grocery-order, wegmans-grocery-order.", ""),

  h2("The eighteen scripts"),
  table(
    [{ t: "Script", w: 3450 }, { t: "What it does", w: 6630 }],
    [
      ["vt_standard_sweep.py", "Applies the 29 August change set to every built deck: deletes the three removed slide types, cleans the Concept Bank, builds the slide index. Writes new files, never overwrites."],
      ["build_concept_banks.py", "Builds the Concept Bank grid from the deck's own word banks."],
      ["deck_changeset_audit.py", "Read-only. Reports what the change set still has to do to each deck."],
      ["deck_inventory.py", "Read-only walk of the cycle folders. Job 1 — everything else waits on it."],
      ["deck_lint.py", "Two-tier check. Hard failures block shipping; advisory items are reported."],
      ["deck_link_check.py", "Checks that every link in a deck still resolves."],
      ["deck_apply_changes.py", "Applies a reviewed change set to decks."],
      ["deck_agenda_audit.py", "Checks decks against the agenda spreadsheet."],
      ["fusion_table.py", "One row per cycle: critical aspects, coordination structure or none, and why none."],
      ["aspect_extractor.py", "Pulls the critical aspects out of a deck."],
      ["extract_and_grade.py", "Scores the first submission. Classifies every slide; only diagnostic slides are scored."],
      ["extract_and_grade_rewrites.py", "Scores the rewrite. Separate, so the same thing is not measured twice."],
      ["lesson_router.py", "Routes a lesson to the right handling."],
      ["lesson_name_guard.py", "Stops a lesson being filed under the wrong name."],
      ["pipeline_lint.py", "Checks the pipeline's own configuration."],
      ["workflow_b_lint.py", "Checks Workflow B — the student email step."],
      ["bio_v3_extract.py", "Extraction for the v3 deck format."],
      ["pipeline_invariants.json", "The facts the pipeline is not allowed to violate. Not a script; read by several."],
    ],
    { code: [0] }
  ),

  h2("The written work"),
  p("Nine documents, renamed on 30 August. They had been numbered 01 to 12 by the order they were captured, which stopped meaning anything once 04, 05 and 11 were never written and the series split across three folders. docs/README.md in the repository says the same thing in more detail."),
  h3("docs/book — the argument"),
  bullet("The sequenced synthesis. Start here: the problem, simultaneity, the nine moves, the question form, the coordination structures, visibility, what the artifacts carry, feedback, teacher judgment, and the package's central risk.", "coordination_judgment_and_the_package — "),
  bullet("Exposure as a graduated dimension with its own clock, separate from cognitive demand. Five rungs, each gated by what a teacher can observe rather than by week number.", "the_visibility_ladder — "),
  bullet("Synchronic and diachronic simultaneity, and where the claim sits against Marton.", "simultaneity_research_base — "),
  bullet("The evidence base, and why each piece bears on the argument.", "biology_education_research_reading — "),
  bullet("Working notes on the classroom episode as it functions in the book.", "the_snake_question_book_notes — "),
  h3("docs/curriculum — the build"),
  bullet("The lineage table. Nine moves, each with a purpose and a source, running Marton and Tsui to Moore-Anderson to von Duyke.", "nine_thinking_moves_attribution — "),
  bullet("The order the deck work runs in, and what waits on what.", "deck_work_order_of_operations — "),
  bullet("The same episode as a curriculum case, with the decision withheld.", "the_snake_question_curriculum_case — "),
  h3("prompts"),
  bullet("Job 1, read-only, written against the actual file layout.", "deck_inventory_job — "),

  h2("What else is in docs/"),
  bullet("Every deck's live Google Slides ID, its import file, and its expected slide count. This is what makes an import verifiable rather than hopeful.", "decks_live_ids.csv — "),
  bullet("How to import a finished deck into its live Google Slides file without breaking its links. Written for a Claude Code session on your Mac.", "import_runbook.md — "),
  bullet("The start-up card: which drive is where, which surface reaches it, and six things that looked broken and were not.", "engine_startup.html — "),
  bullet("The Drive IDs of all nineteen Google-native files in the TPT tree. Those documents live only on Drive, so an ID index is the only backup they can have.", "tpt_google_native_index.md — "),
  bullet("A byte-for-byte copy of the TPT Drive folder as it stood before the 30 August reorganisation. 58 files. A record of the before state, not a folder to keep updated.", "tpt-drive-snapshot/ — "),
  bullet("The curated TPT material: the MANIFEST, the pipeline specs, the listing prompts, the teacher-facing documents.", "tpt/ — "),

  h2("What changed on 29 and 30 August"),
  p("Sixteen commits. In sequence:"),
  table(
    [{ t: "When", w: 1500 }, { t: "What", w: 8580 }],
    [
      ["Aug 29", "Pipeline scripts moved off Drive; git becomes canonical."],
      ["Aug 29", "deck_link_check.py recovered; vt-bio-skill corrected for the move."],
      ["Aug 29", "The ~/answerable clone reconciled into this one and retired."],
      ["Aug 29", "23 files rescued from the school Drive, then the governing .docx and .xlsx set, with scoped gitignore exceptions so they were not silently dropped."],
      ["Aug 29", "daily-route removed — no longer used."],
      ["Aug 29", "The Concept Bank builder, the 50-deck inventory and the export log."],
      ["Aug 29", "All 24 Biology decks swept to the change set: three slide types deleted, Concept Banks cleaned and capitalised, a slide index built for every deck."],
      ["Aug 30", "The engine start-up card."],
      ["Aug 30", "The TPT Drive folder snapshotted, then reorganised — 17 documents to MASTERS, 13 superseded skill files off Drive, MASTERS moved into 06 TPT."],
      ["Aug 30", "The nine written documents named; the capture numbering retired."],
      ["Aug 30", "Two lines restored into section 9 from a conversation no longer in your history."],
    ]
  ),

  h2("The one thing to check"),
  p("Seven commits are on your Mac and not on GitHub. Until a push runs, the repository is not a backup — it is a local folder with good history. The command, run in ~/code/answerable-skills:"),
  mono("git push"),
];

const doc = new Document({
  creator: "Katherine von Duyke",
  title: "What Is In GitHub — 30 August 2026",
  styles: { default: { document: { run: { font: "Aptos", size: 21 } } } },
  sections: [{ properties: { page: LETTER }, children: body }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("/home/claude/out/2026-08-30 — What Is In GitHub.docx", b);
  console.log("written");
});
