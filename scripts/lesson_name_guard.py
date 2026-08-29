#!/usr/bin/env python3
"""
lesson_name_guard.py  —  canonical lesson-name guard (#3)
=========================================================
The #1 silent failure in the pipeline is a lesson name that doesn't EXACTLY
match the canonical name the Dashboard's All-tab formula keys on -> blank
Schoology import cell, no error. This module makes that mismatch loud.

Use at the top of any A / B1 / B2 / PIPE run, after resolving the lesson name:

    from lesson_name_guard import resolve_lesson
    canon, note = resolve_lesson(raw_lesson_name)
    if canon is None:
        HALT(note)          # unknown lesson — do not write a blank import cell
    elif note:
        log(note)           # matched, but only after normalizing (e.g. case)

Keep the CANONICAL list in sync with the Dashboard columns + memory's
"tracked pipeline lessons". This file is dumb on purpose: no judgment,
just exact-match-after-normalize. Update the list here when a lesson is added.
"""
import re

# Canonical names — must match the Dashboard column / All-tab Lesson values verbatim.
CANONICAL = [
    # Biology
    "Natural Selection",
    "Evidence of Evolution",
    "Introduction to Evolution",
    "Classifying Organisms",
    # Forensics
    "Time of Death",
    "What is Death?",
]

# Out-of-scope: never process (memory #23 / #26).
OUT_OF_SCOPE = {"Pig Autopsy", "Stages of Decomposition"}

def _norm(s: str) -> str:
    """Lowercase, strip, collapse internal whitespace, drop trailing punctuation."""
    s = re.sub(r"\s+", " ", (s or "").strip()).rstrip(".?!")
    return s.casefold()

_LOOKUP = {_norm(c): c for c in CANONICAL}
_OOS = {_norm(c) for c in OUT_OF_SCOPE}

def resolve_lesson(raw: str):
    """
    Returns (canonical_name, note).
      - exact canonical match                  -> (canonical, "")
      - matched only after normalizing case/ws -> (canonical, "normalized 'raw' -> 'canonical'")
      - explicitly out of scope                -> (None, "OUT OF SCOPE — do not process")
      - unknown                                -> (None, "UNKNOWN LESSON ... would blank the import cell")
    """
    raw = (raw or "").strip()
    n = _norm(raw)
    if n in _OOS:
        return None, f"OUT OF SCOPE lesson '{raw}' — do not process."
    canon = _LOOKUP.get(n)
    if canon is None:
        return None, (f"UNKNOWN LESSON '{raw}' — not in the canonical list. "
                      f"Writing it would produce a blank Schoology import cell. "
                      f"Add it to CANONICAL + the Dashboard column first.")
    note = "" if canon == raw else f"normalized '{raw}' -> '{canon}'"
    return canon, note

def reconcile(names):
    """Batch helper: returns {name: (canonical, note)} for a list of lesson names."""
    return {x: resolve_lesson(x) for x in names}

if __name__ == "__main__":
    import json, sys
    tests = sys.argv[1:] or [
        "Time of Death", "Time of death", "  Evidence  of Evolution ",
        "What is Death", "Speciation", "Pig Autopsy",
    ]
    print(json.dumps(reconcile(tests), indent=2, ensure_ascii=False))
