const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, ShadingType, AlignmentType, BorderStyle, PageOrientation } = require('docx');
const fs = require('fs');

const TEAL = "027A86";
const INK = "14201F";
const SOFT = "4E605E";
const FAINT = "7D8F8D";
const RULE = "D3DCDA";
const PANEL = "F2F5F4";

const LETTER = { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 } };

function h1(text) {
  return new Paragraph({
    spacing: { before: 0, after: 120 },
    children: [new TextRun({ text, bold: true, size: 40, color: INK, font: "Aptos" })],
  });
}
function kicker(text) {
  return new Paragraph({
    spacing: { before: 0, after: 300 },
    children: [new TextRun({ text, size: 18, color: FAINT, font: "Aptos", allCaps: true, characterSpacing: 30 })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 140 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } },
    children: [new TextRun({ text, bold: true, size: 24, color: TEAL, font: "Aptos" })],
  });
}
function h3(text) {
  return new Paragraph({
    spacing: { before: 260, after: 80 },
    children: [new TextRun({ text, bold: true, size: 21, color: INK, font: "Aptos" })],
  });
}
function p(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 0, after: 140, line: 300 },
    children: [new TextRun({ text, size: 21, color: opts.soft ? SOFT : INK, font: "Aptos", italics: !!opts.italic })],
  });
}
function mono(text) {
  return new Paragraph({
    spacing: { before: 0, after: 100 },
    children: [new TextRun({ text, size: 19, color: SOFT, font: "Consolas" })],
  });
}
function bullet(text, boldLead) {
  const kids = [];
  if (boldLead) kids.push(new TextRun({ text: boldLead, bold: true, size: 21, color: INK, font: "Aptos" }));
  kids.push(new TextRun({ text, size: 21, color: INK, font: "Aptos" }));
  return new Paragraph({ bullet: { level: 0 }, spacing: { before: 0, after: 90, line: 290 }, children: kids });
}

function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.w, type: WidthType.DXA },
    shading: opts.head ? { type: ShadingType.CLEAR, fill: PANEL } : undefined,
    margins: { top: 90, bottom: 90, left: 130, right: 130 },
    children: [new Paragraph({
      spacing: { before: 0, after: 0, line: 260 },
      children: [new TextRun({
        text,
        bold: !!opts.head || !!opts.bold,
        size: opts.head ? 17 : 19,
        color: opts.head ? FAINT : (opts.soft ? SOFT : INK),
        font: opts.code ? "Consolas" : "Aptos",
        allCaps: !!opts.head,
      })],
    })],
  });
}
function table(cols, rows, opts = {}) {
  const total = cols.reduce((a, b) => a + b.w, 0);
  return new Table({
    columnWidths: cols.map(c => c.w),
    width: { size: total, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: RULE },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: RULE },
      insideVertical: { style: BorderStyle.NONE },
    },
    rows: [
      new TableRow({ tableHeader: true, children: cols.map(c => cell(c.t, { w: c.w, head: true })) }),
      ...rows.map(r => new TableRow({
        children: r.map((t, i) => cell(t, { w: cols[i].w, code: opts.code && opts.code.includes(i), bold: i === 0 && opts.boldFirst })),
      })),
    ],
  });
}
function spacer() { return new Paragraph({ spacing: { after: 160 }, children: [] }); }

module.exports = { Document, Packer, Paragraph, TextRun, LETTER, h1, kicker, h2, h3, p, mono, bullet, table, spacer, TEAL, INK, SOFT, FAINT };
