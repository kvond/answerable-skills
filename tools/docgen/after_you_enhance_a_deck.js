const {Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
       Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
       LevelFormat, PageOrientation} = require('docx');
const fs = require('fs');

const TEAL = "028090", INK = "111111", GREY = "6B6B6B";

const H1 = t => new Paragraph({heading: HeadingLevel.HEADING_1, spacing:{before:360,after:140},
  children:[new TextRun({text:t, font:"Arial", size:30, bold:true, color:INK})]});
const H2 = t => new Paragraph({heading: HeadingLevel.HEADING_2, spacing:{before:280,after:100},
  children:[new TextRun({text:t, font:"Arial", size:24, bold:true, color:TEAL})]});
const P = (t, opt={}) => new Paragraph({spacing:{after:opt.after===undefined?140:opt.after},
  indent: opt.indent ? {left: opt.indent} : undefined,
  children:[new TextRun({text:t, font:"Arial", size:21, color: opt.color||INK,
                         italics: !!opt.italics, bold: !!opt.bold})]});
const RUNS = (parts, opt={}) => new Paragraph({spacing:{after:opt.after===undefined?140:opt.after},
  indent: opt.indent ? {left: opt.indent} : undefined,
  children: parts.map(p => new TextRun({text:p[0], font:"Arial", size:21,
    bold: !!p[1], italics: !!p[2], color: p[3]||INK}))});
const BOX = t => new Paragraph({spacing:{before:60, after:160}, indent:{left:360},
  border:{left:{style:BorderStyle.SINGLE, size:12, color:TEAL, space:12}},
  children:[new TextRun({text:t, font:"Consolas", size:19, color:INK})]});
const CHECK = (t, sub) => [
  new Paragraph({spacing:{before:120, after: sub?40:80}, indent:{left:200, hanging:200},
    children:[new TextRun({text:"☐  ", font:"Arial", size:22, color:TEAL}),
              new TextRun({text:t, font:"Arial", size:21, color:INK})]}),
  ...(sub ? [new Paragraph({spacing:{after:80}, indent:{left:560},
    children:[new TextRun({text:sub, font:"Arial", size:19, color:GREY})]})] : [])];
const RULE = () => new Paragraph({spacing:{before:200, after:200},
  border:{bottom:{style:BorderStyle.SINGLE, size:6, color:"DDDDDD", space:6}},
  children:[new TextRun({text:"", size:2})]});

const cell = (t, {bold, width, shade, color}={}) => new TableCell({
  width:{size:width, type:WidthType.DXA},
  shading: shade ? {type: ShadingType.CLEAR, fill: shade, color:"auto"} : undefined,
  margins:{top:80,bottom:80,left:120,right:120},
  children:[new Paragraph({children:[new TextRun({text:t, font:"Arial", size:19,
    bold:!!bold, color: color||INK})]})]});

const W = [2200, 6800];
const table = rows => new Table({
  columnWidths: W,
  width:{size: W[0]+W[1], type: WidthType.DXA},
  rows: rows.map((r,i) => new TableRow({children:[
    cell(r[0], {bold:i===0, width:W[0], shade: i===0 ? "F2F6F6" : undefined}),
    cell(r[1], {bold:i===0, width:W[1], shade: i===0 ? "F2F6F6" : undefined})]}))});

const doc = new Document({
  styles:{default:{document:{run:{font:"Arial", size:21, color:INK}}}},
  sections:[{
    properties:{page:{size:{width:12240, height:15840}, margin:{top:1080,bottom:1080,left:1080,right:1080}}},
    children:[

new Paragraph({spacing:{after:60}, children:[new TextRun({
  text:"ANSWERABLE BIOLOGY · DECK OPERATIONS", font:"Arial", size:18, bold:true, color:TEAL})]}),
new Paragraph({spacing:{after:60}, children:[new TextRun({
  text:"After you enhance a deck", font:"Arial", size:40, bold:true, color:INK})]}),
new Paragraph({spacing:{after:280}, children:[new TextRun({
  text:"What to do once you have added anything to a live deck in Google Slides · 30 August 2026",
  font:"Arial", size:19, color:GREY})]}),

P("Anything you add to a deck inside Google Slides is attached to a slide, not to the file. It survives every kind of change I make from now on, and it does not survive a full re-import, which deletes the old slides. This page is the short procedure that keeps both facts true."),

H1("1. Does this page apply?"),
P("It applies if you did any of these in a live deck:"),
...CHECK("Added a transition or an animation"),
...CHECK("Embedded a video or audio clip"),
...CHECK("Added an image, a shape, a drawn arrow or a link"),
...CHECK("Typed into the speaker notes"),
...CHECK("Left a comment"),
...CHECK("Used a Gemini or “enhance” feature on any slide"),
P("It does not apply to changes I make through the Slides API, or to a deck you only looked at.", {italics:true, color:GREY}),

H1("2. Do these three things"),

H2("Step one · Tell me which decks"),
P("One line is enough. I mark the deck in the deck register so no later session can full-re-import it and take your work with it."),
BOX("I enhanced Cycles 09 and 14."),
RUNS([["The register is ",false],["docs/decks_live_ids.csv",false,false,TEAL],[" in the answerable-skills repo, column ",false],["google_native",false,false,TEAL],[". You never have to open it — telling me is the whole step.",false]]),

H2("Step two · Ask me to run the live check"),
P("The offline linter reads the built .pptx files and cannot see anything you did in Google Slides. The live check reads the live deck through the Slides API. Those exact words are enough:"),
BOX("Run the live deck check on 09 and 14."),
P("It reports, per deck: slide count, 4:3, every slide type still detectable by the string the grading prompts match on, the retired slide types absent, both Critical aspect labels and the slide 1 block, the Day 3 divider free of the old checklist, the grading markers, and every font and size. It also compares against the last recorded fingerprint, so a change neither of us predicted still shows up."),

H2("Step three · Read the one line that matters"),
P("Each deck comes back as OK or FAIL with the reason under it. What the reasons mean:"),
table([
  ["Finding", "What it means and what to do"],
  ["no 3-Tier Question slide detected",
   "A heading was rewritten. The grading prompts can no longer find that slide. Undo it in Slides, or send it to me to repair."],
  ["<type> slides detected 2 → 1",
   "Same problem, caught by comparison rather than by rule. One slide of that type stopped matching."],
  ["new font appeared",
   "An enhancement restyled something. Cosmetic on a content slide; on a question slide it usually means the text was rebuilt, so check that slide."],
  ["Day 3 divider still carries the old checklist",
   "Not your doing — that deck has not been re-imported yet. No action."],
  ["slide count N, expected M",
   "Either the deck is mid-import, or a slide was added or deleted. If you added one deliberately, tell me and I will update the register."],
  ["slide 1 has no CRITICAL ASPECTS block",
   "Not your doing on a deck still waiting on its import. On a finished deck it means the block was deleted."],
]),

H1("3. If something did break"),
P("Google keeps every version. Nothing you do in Slides is unrecoverable:"),
RUNS([["File → Version history → See version history",true],[", then pick the version from before you started and click Restore this version.",false]]),
P("Restoring rolls back the whole deck, including good work you did in the same session. If you would rather keep the session and fix the one slide, send me the cycle number and the slide number and I will repair the string in place."),

H1("4. Two standing rules"),
...CHECK("Never enhance a question slide, a response slide, the Day 3 divider, the Concept Bank, or slide 1.",
         "Those carry the literal strings the feedback pipeline matches on. Content and image slides are free."),
...CHECK("Cycles 02, 03 and 04 are not ready yet.",
         "They are queued for a re-import that will delete their current slides. Wait until I tell you they are through."),

RULE(),
P("The failure this page prevents is silent. A restyled slide looks right in the room and returns nothing at grading, three weeks later, on a whole class set. The check takes a minute and is the only thing that catches it.",
  {italics:true, color:GREY}),

]}]});

Packer.toBuffer(doc).then(b => fs.writeFileSync("/home/claude/doc/After you enhance a deck.docx", b));
