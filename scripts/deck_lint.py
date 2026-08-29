#!/usr/bin/env python3
"""
deck_lint.py  —  VT deck validator (run as the LAST step of every VT insert build)
==================================================================================
Purpose: catch drift that silently breaks the feedback pipeline WEEKS later.
Workflow A keys off verbatim marker strings and the 3-Tier concept-question
format. If a VT build mangles a tier label, drops a diagnostic marker, or ships
a tier label in black instead of its required hex, grading breaks downstream with
no error. This linter makes that loud at build time.

Checks (all HARD rules from the VT authoring spec):
  1. Tier labels present VERBATIM: "Getting Started" / "Working On It" / "Mastery"
  2. Tier label colors applied (never black):
        Getting Started = #C0392B (red)
        Working On It   = #EFDF85 (soft pastel yellow)
        Mastery         = #1E8449 (green)
     (label TEXT itself may be black; the check targets the tier heading runs.)
  3. Each of the five Workflow-A diagnostic markers parseable somewhere in deck:
        "Critical aspect:", 3-tier block, "Pattern break",
        "Finish this sentence as a rule", "What if?"
  4. Reports diagnostic-slide count (sanity vs. expected arc count).
  5. Non-diagnostic nav slides ("do not project") AND standing end-of-lesson
     reflections ("Continuation question:", "Relates to me:") are EXCLUDED
     from all counts, mirroring extract_and_grade.py so lint and grader agree.
     [2026-08-06] The Relates to Me slide legitimately repeats "Critical
     aspect:" once per aspect it lists as an option -- the marker check
     below runs before that pattern is ever tested, so the repetition can't
     phantom-inflate the diagnostic count the way old nav slides once did.

Exit code 0 = clean, 1 = warnings/errors found. Prints a report either way.

Usage:  python deck_lint.py <deck.pptx>
"""
import sys, re
from pptx import Presentation
from pptx.util import Pt  # noqa

TIER_LABELS = ("Getting Started", "Working On It", "Mastery")
TIER_HEX = {
    "Getting Started": "C0392B",
    "Working On It":   "EFDF85",
    "Mastery":         "1E8449",
}
NON_DIAGNOSTIC = ("do not project", "teacher navigation")
# Standing end-of-lesson reflections (Continuation Question, Relates to Me):
# real, projected, student-facing content -- but never scored for diagnostic
# completion. Kept as a separate tuple from NON_DIAGNOSTIC (teacher-nav
# slides that aren't even projected) so an audit can tell the two exclusion
# reasons apart. Must stay in sync with extract_and_grade.py's
# STANDING_REFLECTION_MARKERS -- lint and grader have to agree. [2026-08-06]
STANDING_REFLECTION = ("continuation question:", "relates to me:")
MARKERS = {
    "Critical aspect":  re.compile(r"critical aspect\s*:", re.I),
    "Pattern break":    re.compile(r"pattern break", re.I),
    "Build-a-rule":     re.compile(r"finish this sentence as a rule", re.I),
    "What-if":          re.compile(r"what if\?", re.I),
}


def _slide_text(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                t = "".join(r.text for r in p.runs)
                if t.strip():
                    out.append(t)
    return "\n".join(out)


def _run_hex(run):
    """Return uppercase RRGGBB for a run's font color, or None if unset/theme."""
    try:
        c = run.font.color
        if c and c.type is not None and c.rgb is not None:
            return str(c.rgb).upper()
    except Exception:
        pass
    return None


def lint(path):
    prs = Presentation(path)
    errors, warnings, notes = [], [], []
    diagnostic_slides = 0
    markers_seen = set()
    tier_slides = 0

    for idx, slide in enumerate(prs.slides, start=1):
        text = _slide_text(slide)
        low = text.lower()
        if any(m in low for m in NON_DIAGNOSTIC) or any(m in low for m in STANDING_REFLECTION):
            continue  # nav slide or standing reflection — excluded, matches grader

        has_all_tiers = all(lbl in text for lbl in TIER_LABELS)
        slide_is_diag = False

        if has_all_tiers:
            slide_is_diag = True
            tier_slides += 1
            # verbatim + color check on tier heading runs
            for sh in slide.shapes:
                if not sh.has_text_frame:
                    continue
                for p in sh.text_frame.paragraphs:
                    line = "".join(r.text for r in p.runs).strip()
                    for lbl, want_hex in TIER_HEX.items():
                        if line == lbl or line.startswith(lbl):
                            hexes = [_run_hex(r) for r in p.runs if r.text.strip()]
                            hexes = [h for h in hexes if h]
                            if not hexes:
                                warnings.append(f"slide {idx}: tier '{lbl}' has no explicit color set "
                                                f"(theme/auto) — expected #{want_hex}; verify it isn't rendering black")
                            elif want_hex not in hexes:
                                if "000000" in hexes:
                                    errors.append(f"slide {idx}: tier '{lbl}' is BLACK (#000000); "
                                                  f"must be #{want_hex}")
                                else:
                                    warnings.append(f"slide {idx}: tier '{lbl}' color {hexes} "
                                                    f"!= required #{want_hex}")
        for mname, rx in MARKERS.items():
            if rx.search(text):
                markers_seen.add(mname)
                slide_is_diag = True
        if slide_is_diag:
            diagnostic_slides += 1

    # verbatim tier-label presence across deck (typo guard)
    all_text = "\n".join(_slide_text(s) for s in prs.slides)
    for lbl in TIER_LABELS:
        if lbl not in all_text:
            errors.append(f"tier label '{lbl}' never appears verbatim anywhere in deck "
                          f"(typo or wrong casing will break grader classification)")

    missing_markers = [m for m in ("Critical aspect", "Pattern break", "Build-a-rule", "What-if")
                       if m not in markers_seen]
    if missing_markers:
        notes.append(f"diagnostic markers not found in deck: {missing_markers} "
                     f"(fine if this arc doesn't use them; flagged for eyeball)")

    print("=" * 60)
    print(f"deck_lint: {path}")
    print(f"  total slides:        {len(prs.slides.__iter__.__self__._sldIdLst)}")
    print(f"  3-tier CQ slides:    {tier_slides}")
    print(f"  diagnostic slides:   {diagnostic_slides}")
    print(f"  markers present:     {sorted(markers_seen)}")
    print("-" * 60)
    for e in errors:   print("  ERROR   ", e)
    for w in warnings: print("  WARNING ", w)
    for n in notes:    print("  note    ", n)
    if not (errors or warnings):
        print("  clean — no tier/marker/color problems found")
    print("=" * 60)
    return 1 if (errors or warnings) else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr); sys.exit(2)
    sys.exit(lint(sys.argv[1]))
