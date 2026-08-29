"""
aspect_extractor.py  —  Aspect-Anchored Conceptual Grader: the EXTRACTOR (deterministic half)
================================================================================================
Role in the architecture (keep volatile judgment OUT of this file):
  - This script is a DUMB, STABLE extractor. It finds sections, pulls the critical aspect,
    pulls the student's VERBATIM answers (first attempt + rewrite), flags blanks, and counts.
  - It makes NO conceptual judgment. All scoring/feedback/tiers live in the SPEC
    (aspect_grader_spec.md), applied by the reasoning layer (Sonnet). This file should rarely change.

Handles the feedback-rewrite template family seen in this pipeline:
  - Biology:   headers "Slide N: <aspect>", blocks "YOUR ANSWER" (first) / "YOUR REWRITE" (rewrite)
  - Forensics: headers "<Lesson> — Slide N: <aspect>", blocks "YOUR FIRST ANSWER" / "YOUR IMPROVED ANSWER"
  - Both as .docx (answers live in the table after the marker) and as Google-Doc/Slides text export.

Usage (in the pipeline runner / Composio workbench):
    raw = download_bytes(file_id)                      # docx bytes, OR
    txt = download_text(file_id)                       # gdoc/slides text export
    result = extract_sections(docx_bytes=raw)          # or extract_sections(text=txt)
    # result = {"sections": [ {slide, aspect, first, rewrite}, ... ], "counts": {...}}
    # Feed result["sections"] to the reasoning layer with aspect_grader_spec.md.

Dependencies: python-docx (for the .docx path only).
------------------------------------------------------------------------------------------------
CHANGELOG
  v1.1  2026-06-12  text path: lift answer capture cap 5->40 lines (was silently
                    truncating long answers before the grader saw them; docx path unchanged).
  v1.0  2026-05-31  Initial. Bio + forensics feedback-rewrite templates, docx + text paths.
                    Table-only answer capture on the docx path (avoids grabbing marker labels).
                    Blank detection: "(No answer submitted)" / empty. Counts emitted.
"""

import re, io

HDR     = re.compile(r'^(?:.*?\u2014\s*)?Slide\s+(\d+)\s*:\s*(.+?)\s*$', re.I)   # "Slide 7: x" and "... — Slide 4: x"
FIRST   = re.compile(r'YOUR (?:FIRST )?ANSWER', re.I)                            # first attempt marker
REWRITE = re.compile(r'YOUR (?:IMPROVED ANSWER|REWRITE)', re.I)                  # rewrite marker
STOP    = re.compile(r'WHAT YOU DID WELL|WHAT WOULD MAKE|PUSH YOURSELF|THINK ABOUT|Continued|_{6,}|\u2605|\U0001f52c|\u270f|\U0001f4dd|^QUESTION$', re.I | re.M)
_BLANKS = {"", "(no answer submitted)", "continued...", "continued", "n/a"}
_LABELS = ("question", "your answer", "your first answer", "your rewrite",
           "your improved answer", "what you did well", "what would make",
           "push yourself", "think about")


def _is_label(s):
    sl = s.strip().lower()
    return (not sl) or any(sl.startswith(b) for b in _LABELS) or sl.startswith(("\u2022", "- ")) or HDR.match(s.strip()) is not None


def _clean(s):
    s = re.sub(r'\s+', ' ', (s or '')).strip()
    return "" if s.lower() in _BLANKS else s


# ---------- plain-text path (Google Doc / Slides text export) ----------
def _grab_text(block, mark, also_stop=None):
    m = mark.search(block)
    if not m:
        return ""
    rest = STOP.split(block[m.end():])[0]
    if also_stop:                       # e.g. stop the first answer at the rewrite marker
        rest = also_stop.split(rest)[0]
    lines = [l.strip() for l in rest.splitlines()
             if l.strip() and not _is_label(l) and l.strip().lower() not in _BLANKS]
    return _clean(" ".join(lines[:40]))


def sections_from_text(txt):
    lines = txt.splitlines()
    hi = [i for i, l in enumerate(lines) if HDR.match(l.strip())]
    out = []
    for n, st in enumerate(hi):
        en = hi[n + 1] if n + 1 < len(hi) else len(lines)
        block = "\n".join(lines[st:en])
        m = HDR.match(lines[st].strip())
        out.append({"slide": m.group(1), "aspect": m.group(2).strip(),
                    "first": _grab_text(block, FIRST, also_stop=REWRITE),
                    "rewrite": _grab_text(block, REWRITE)})
    return out


# ---------- .docx path (answers live in the table after the marker) ----------
def sections_from_docx(docx_bytes):
    from docx import Document
    from docx.oxml.ns import qn
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = Document(io.BytesIO(docx_bytes))
    blocks = []
    for ch in d.element.body.iterchildren():
        if ch.tag == qn('w:p'):
            blocks.append(("P", Paragraph(ch, d).text))
        elif ch.tag == qn('w:tbl'):
            t = Table(ch, d)
            blocks.append(("T", " ".join(c.text.strip() for r in t.rows for c in r.cells if c.text.strip())))
    hi = [j for j, (k, t) in enumerate(blocks) if k == "P" and HDR.match(t.strip())]
    out = []

    def next_table(j, en):
        for q in range(j + 1, en):
            if blocks[q][0] == "T":
                return _clean(blocks[q][1])
        return ""

    for n, st in enumerate(hi):
        en = hi[n + 1] if n + 1 < len(hi) else len(blocks)
        m = HDR.match(blocks[st][1].strip())
        first = rew = ""
        for j in range(st + 1, en):
            k, t = blocks[j]
            if k != "P":
                continue
            if REWRITE.search(t):
                rew = next_table(j, en)
            elif FIRST.search(t):
                first = next_table(j, en)
        out.append({"slide": m.group(1), "aspect": m.group(2).strip(), "first": first, "rewrite": rew})
    return out


# ---------- dispatcher ----------
def extract_sections(docx_bytes=None, text=None):
    """Auto-detect and parse. Pass docx_bytes (raw .docx) OR text (gdoc/slides export)."""
    secs = []
    if docx_bytes:
        if docx_bytes[:4] == b"PK\x03\x04":
            try:
                secs = sections_from_docx(docx_bytes)
            except Exception:
                secs = []
        if not secs:  # not a real docx (e.g. a PDF export) — try as text
            try:
                text = text or docx_bytes.decode("utf-8", "ignore")
            except Exception:
                text = text or ""
    if not secs and text:
        secs = sections_from_text(text)
    counts = {
        "sections": len(secs),
        "first_answered": sum(1 for s in secs if s["first"]),
        "rewrite_answered": sum(1 for s in secs if s["rewrite"]),
        "blank_both": sum(1 for s in secs if not s["first"] and not s["rewrite"]),
    }
    return {"sections": secs, "counts": counts}


if __name__ == "__main__":
    import sys, json
    path = sys.argv[1]
    if path.lower().endswith(".docx"):
        with open(path, "rb") as f:
            print(json.dumps(extract_sections(docx_bytes=f.read()), indent=2, ensure_ascii=False))
    else:
        with open(path, encoding="utf-8", errors="ignore") as f:
            print(json.dumps(extract_sections(text=f.read()), indent=2, ensure_ascii=False))
