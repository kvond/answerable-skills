---
name: manuscript-ops
description: "Operations over the manuscript files: stage/export chapters from Roam, render reading copies, run continuity + citation checks against the sources manifest, compile deliverable docx. Never generates or edits prose. Triggers: staging/exporting the manuscript, consistency or citation pass, \"compile for editor/committee\"."
---

# Manuscript-Ops — operations over the manuscript files

The mechanical, structural work around the manuscript, kept strictly separate from the
thinking. This skill never writes prose and never edits a chapter — argument generation and
revision stay in the Book Project. Here Cowork only renders, checks, compiles, and flags.

Roam is canonical. `source/` is the faithful export (links intact, the backup); `writing/`
is the tag-stripped reading copy. Neither is ever hand-edited — edits happen in Roam, and
these are regenerated downstream, the same discipline as RAW_ORIGINALS.

## Bundled scripts

Run the scripts for the deterministic work; let Claude judgment enter only where noted.

- `scripts/render_reading.py` — built. Roam export → clean reading prose: brackets removed,
  workflow tags stripped, components/block-refs/attributes/highlight gone, bullets flattened
  to paragraphs; headings/bold/italics kept. Inline content tags keep their words; workflow
  tags (`#next #near #book #[[parking lot]]`…) are removed whole.
- `scripts/check_consistency.py` — built. Extracts chapter cross-references (and whether the
  target chapter exists), vague back-references with no number, and every tracked-term
  occurrence with context, into one report. Extraction only — Claude adjudicates.
- `scripts/check_citations.py` — planned. Extract in-text citations, set-difference against
  the sources manifest, flag orphans and unused entries. Author-name variants normalized by
  the same dedup logic as book-ops.
- Deliverables use the built-in **docx skill**, not a bundled script.

## Defaults for this manuscript

- **Source** — the chapter pages in Roam, pulled via the Roam MCP (scoped to chapters, not
  the whole graph).
- **Layout** — `source/` faithful export, `writing/` tag-stripped reading copy, both under git.
- **Tracked terms** for the consistency pass — Abraham, Aliyah, double booking, agency,
  perception, ecology. Add to this list as coined concepts stabilize.
- **Sources manifest** — `sources.json` (or `.bib`): Bakhtin, Scott, Lareau, Ito, Variation Theory…
- No external Python dependencies; the scripts are standard library only.

## Version retention (Drive working copies)

Roam stays canonical; the compiled Google Doc is a downstream reading/deliverable copy, not
a second source of truth. One rule keeps the Drive side from fragmenting into the kind of
`(final) + X` swarm that accumulated during the June apparatus passes:

- **One LIVE doc.** Exactly one Google Doc is the current manuscript, named
  `Answerable Teaching — LIVE`. Apparatus, formatting, APA-7, and HEP-flag passes happen
  *in place* in that doc, versioned through File → Version history (name each version per
  pass: "Ch2 notes renumbered", "APA-7", "mechanical + HEP flags"). Never clone-and-suffix
  into a new copy — that habit is what produced the swarm.
- **Archive, don't delete.** A genuinely superseded doc moves to `HOME/book/archive/`
  (dated) and stays there. The tracked-changes lineage is the HEP AI-authorship provenance
  trail and is worth keeping. Deletion is reserved for confirmed byte-duplicates (the same
  pass copied into two accounts) and only after verifying identity.
- **One account owns it.** LIVE doc and archive live in a single canonical account (udel),
  so ownership and version history don't split across kvond@udel / kvond12@gmail.
- **Reconcile back to Roam.** If a pass happens in the Doc rather than Roam (as the June
  passes did), flow it back so `source/`/`writing/` stay faithful — the Doc is never allowed
  to become a silent parallel master.

Retention convention only — never touches argument or wording.

## Invoking

One-line requests trigger the matching job with these defaults; nothing writes to Roam or
to the manuscript without showing you the result first:
- "stage the manuscript" / "sync the chapters" → job 2
- "run a consistency pass" / "check cross-references" → job 1
- "check the citations" → job 3
- "compile the manuscript" / "make a docx for the editor" → job 4

## Job 2 — staging / export (the foundation)

1. Pull the chapter pages via the Roam MCP (the `roam_pull.py` query shapes from book-ops,
   scoped to chapter pages) and write each to `source/`.
2. `python3 scripts/render_reading.py --in source/ --out writing/`
3. Commit `source/` and `writing/` to git, then push to the private remote so the reading
   copy is browsable on GitHub.

The weekly `#book` distill is a separate scheduled local task (same machinery as
daily-agenda): pull the week's `#book` captures, organize them, drop them where the writing
session expects. The MCP pull + git wrapping is the piece to wire on first run.

## Job 1 — consistency pass (on-demand, e.g. pre-submission)

`python3 scripts/check_consistency.py --in writing/ --out consistency_report.md`

Then read the report and flag the judgment calls: does each cross-reference's claim actually
live where it points; is "double booking" used consistently with its Ch. 5 definition; are
Abraham and Aliyah characterized consistently. Surface findings for the user; never edit the
manuscript — propose changes for Roam.

## Job 3 — citation integrity (on-demand)

Maintain the sources manifest. `check_citations.py` extracts every in-text citation and
diffs against it, flagging cited-but-missing and present-but-unused. Normalize author-name
variants (Scott / J.C. Scott / Scott 1998) before diffing.

## Job 4 — deliverables (on-demand)

Use the docx skill to compile `writing/` into a formatted .docx — full manuscript or
per-chapter — with table of contents and front matter, in the editor's required manuscript
format. The format is set once; this is a transform, not a judgment.

## Safety

- Never edit the manuscript. `writing/` and every report are derived and advisory; fixes go
  into Roam, by the user.
- `source/` is the faithful backup; before any git operation confirm it reflects the current
  Roam state.
- The reading render is a convenience copy, not a typeset proof — an inline editorial aside
  left next to a stripped `{{TODO}}` may survive into `writing/`. Don't treat it as final.

"""matching.py — shared deterministic matching layers for book-ops.

All sweeps (full, delta, on-create) import from here so the same inventory
always yields the same candidates. No external dependencies.

Layers implemented here:
  1. normalized-exact  — normalize_title() key collision
  2. fuzzy             — token_set_ratio() (pure-python rapidfuzz equivalent)
  3. alias/acronym     — expand via vocabulary aliases
  citation             — norm_citation() catches quote/dash/period/ellipsis variants

Layer 4 (backlink overlap) is computed in the sweep scripts from inventory
edges; layer 5 (semantic) is intentionally NOT here — it is the model's job.
"""

import json
import re
import unicodedata

# ---------------------------------------------------------------- normalize

_MD_MARKUP = re.compile(r"(\*\*|__|\^\^|~~|`)")
_WS = re.compile(r"\s+")
_TRAIL_PUNCT = re.compile(r"[\s\.\:\;\,\/\\\-–—]+$")
_LEAD_PUNCT = re.compile(r"^[\s\-–—\.\:\;\,]+")
_BRACKET_REF = re.compile(r"\[\[|\]\]|#")

MONTHS = ("january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december")
_DATE_PAGE = re.compile(
    r"^(" + "|".join(m.capitalize() for m in MONTHS) + r") \d{1,2}(st|nd|rd|th), \d{4}$")

SYSTEM_PREFIXES = ("roam/", "discourse-graph/")


def is_date_page(title: str) -> bool:
    return bool(_DATE_PAGE.match(title.strip()))


def is_system_page(title: str) -> bool:
    return title.startswith(SYSTEM_PREFIXES)


def strip_emoji(s: str) -> str:
    return "".join(c for c in s if not unicodedata.category(c).startswith(("So", "Sk", "Cs")))


def normalize_title(title: str) -> str:
    """Aggressive normalization for layer-1 collision keys."""
    s = unicodedata.normalize("NFKD", title)
    s = "".join(c for c in s if not unicodedata.combining(c))  # diacritics
    s = strip_emoji(s)
    s = _MD_MARKUP.sub("", s)
    s = _BRACKET_REF.sub("", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("…", "...")
    s = _LEAD_PUNCT.sub("", s)
    s = _TRAIL_PUNCT.sub("", s)
    # hyphen/slash/underscore are word separators (zettel hyphenation convention:
    # "Authorial-Agency" must collide with "Authorial Agency"); interior
    # punctuation is noise for collision keys ("ability, agency" == "ability agency")
    s = re.sub(r"[-/_]", " ", s)
    s = re.sub(r"[,;:!?\"'()\[\]{}]", "", s)
    s = _WS.sub(" ", s).strip().casefold()
    return s


def lemma_key(title: str) -> str:
    """normalize + naive singular/plural folding, word by word."""
    words = []
    for w in normalize_title(title).split(" "):
        if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        words.append(w)
    return " ".join(words)


# ---------------------------------------------------------------- citations

_ELLIPSIS = re.compile(r"(\.\.\.|…)+")

# Closed lexical class of surname particles. Absorbed onto the following token
# so "von Duyke 2016" keys on `von duyke`, not `von` — otherwise every
# von-/van-/de- author in the same year false-collides (von Duyke vs von
# Glasersfeld; van Manen vs van Leeuwen). Multi-particle names ("de la cruz")
# fold correctly because the loop consumes particles until a non-particle head.
# NOTE (residual): hyphenated compounds ("Sizer-Kelly") still truncate to the
# first component — normalize_title() has already turned the hyphen into a
# space by the time we get here, making "Sizer Kelly" indistinguishable from
# "Sizer, K.". Particles are recoverable (closed class); compounds are not.
_PARTICLES = {"von", "van", "de", "der", "den", "del", "della", "di", "du",
              "da", "dos", "das", "la", "le", "el", "ter", "ten", "st", "san"}


def looks_like_citation(title: str) -> bool:
    """Author, X. (1999). Title...  OR  Author, 1999 — Title patterns."""
    return bool(re.search(r"\(\d{4}\)|,\s*\d{4}\s*[—\-]", title))


def norm_citation(title: str) -> str:
    """Citation collision key: author surname + year. Catches curly-vs-straight
    quotes, trailing periods, ellipsis truncations, formatting variants.
    Particle-aware: leading surname particles are kept with the head token."""
    s = normalize_title(title)
    s = _ELLIPSIS.sub("", s)
    # normalize_title has already lowercased, de-punctuated, and space-split;
    # the leading alphabetic run is the author field (initials/year come after).
    toks = re.findall(r"[a-z]+", s)
    if toks:
        i = 0
        parts = []
        while i < len(toks) and toks[i] in _PARTICLES:
            parts.append(toks[i])
            i += 1
        if i < len(toks):            # head surname token after any particles
            parts.append(toks[i])
        surname = " ".join(parts) if parts else toks[0]
    else:
        surname = s[:20]
    ym = re.search(r"\b(1[89]\d\d|20\d\d)\b", s)
    year = ym.group(1) if ym else "????"
    return f"{surname}|{year}"


# ---------------------------------------------------------------- fuzzy

_STOPWORDS = {"the", "a", "an", "of", "to", "and", "or", "in", "on", "for"}


def _tokens(s: str) -> set:
    toks = set(normalize_title(s).split(" ")) - {""}
    content = toks - _STOPWORDS
    return content or toks  # never let stopword-stripping empty a title


def raw_subset(a: str, b: str) -> bool:
    """Unfiltered subset relation — used to keep subset pairs out of the
    full-fuzzy branch even when is_subset_pair()'s signal filter rejects them."""
    ta, tb = _tokens(a), _tokens(b)
    return bool(ta and tb) and (ta < tb or tb < ta)


def token_set_ratio(a: str, b: str) -> int:
    """Pure-python token_set_ratio (rapidfuzz-compatible enough).
    100 when one token set is a subset of the other."""
    ta, tb = _tokens(a), _tokens(b)
    if not ta or not tb:
        return 0
    inter = ta & tb
    if not inter:
        return 0
    if ta <= tb or tb <= ta:
        return 100
    union = ta | tb
    return int(round(200 * len(inter) / (len(ta) + len(tb))))  # dice, 0-100-ish


def is_subset_pair(a: str, b: str) -> bool:
    """Proper token-subset, filtered for signal: a 1-token title inside a long
    title ("agency" ⊂ "The developmental sequence — ability to agency…") is
    noise; a 1-token title inside a 2-token title ("agency" ⊂ "student agency")
    is the classic worked example and stays."""
    ta, tb = _tokens(a), _tokens(b)
    if not (ta and tb) or not (ta < tb or tb < ta):
        return False
    short, long_ = (ta, tb) if len(ta) < len(tb) else (tb, ta)
    return len(short) >= 2 or len(long_) <= 2


# ---------------------------------------------------------------- vocabulary

def load_vocab(path):
    """vocabulary.json:
    { "canonical": ["Variation Theory", ...],
      "aliases":   {"VT": "Variation Theory", ...},
      "never_merge": [["auctor", "Authorial-Agency"], ...] }
    Missing file -> empty vocab (layers 1-2 still run)."""
    try:
        with open(path) as f:
            v = json.load(f)
    except (FileNotFoundError, TypeError):
        v = {}
    v.setdefault("canonical", [])
    v.setdefault("aliases", {})
    v.setdefault("never_merge", [])
    return v


def pair_key(a: str, b: str) -> str:
    return "|".join(sorted((normalize_title(a), normalize_title(b))))


def is_pinned(a: str, b: str, vocab) -> bool:
    k = pair_key(a, b)
    return any(pair_key(x, y) == k for x, y in vocab.get("never_merge", []))


def alias_expand(title: str, vocab) -> str:
    """Return canonical form if title (normalized) is a registered alias."""
    n = normalize_title(title)
    for alias, canon in vocab.get("aliases", {}).items():
        if normalize_title(alias) == n:
            return canon
    return title


def prefix_canonical(title: str, vocab):
    """Single-word title that extends a single-word canonical entry
    (SEPTEMBER -> SEPT, AUGUST -> AUG). Restricted to single words on both
    sides so 'Book Draft 1' never collides with canonical 'Book'."""
    n = normalize_title(title)
    if " " in n or len(n) < 4:
        return None
    for c in vocab.get("canonical", []):
        cn = normalize_title(c)
        if cn != n and " " not in cn and len(cn) >= 3 and n.startswith(cn):
            return c
    return None

"""test_matching.py — pins norm_citation particle handling + core regressions.

Run: python3 test_matching.py   (no deps; exits non-zero on any failure)
The assertions below are the worked cases from matching.py's own docstrings,
made executable so the edge logic can't silently regress.
"""
import matching as m


def check(label, got, want):
    ok = got == want
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {got!r}"
          + ("" if ok else f"  (want {want!r})"))
    return ok


def main():
    fails = 0

    # --- Fix 1: particle surnames must NOT collapse to the particle ----------
    print("norm_citation — particle surnames")
    # the bug: these two must NOT share a key
    a = m.norm_citation("von Duyke, K. (2016)")
    b = m.norm_citation("von Glasersfeld, E. (2016)")
    fails += not check("von Duyke 2016", a, "von duyke|2016")
    fails += not check("von Glasersfeld 2016", b, "von glasersfeld|2016")
    fails += not check("von-authors, same year, distinct keys", a != b, True)

    c = m.norm_citation("van Manen, M. (1990)")
    d = m.norm_citation("van Leeuwen, T. (1990)")
    fails += not check("van Manen 1990", c, "van manen|1990")
    fails += not check("van Leeuwen 1990", d, "van leeuwen|1990")
    fails += not check("van-authors, same year, distinct keys", c != d, True)

    # multi-particle folds onto the head token
    fails += not check("de la Cruz 2019",
                       m.norm_citation("de la Cruz, M. (2019)"), "de la cruz|2019")

    # --- Regression: plain surnames unchanged by the rewrite -----------------
    print("norm_citation — plain surnames (regression)")
    fails += not check("Lareau 2003",
                       m.norm_citation("Lareau, A. (2003)"), "lareau|2003")
    fails += not check("Scott 1998",
                       m.norm_citation("Scott, J. C. (1998)"), "scott|1998")
    # same author + year, formatting variants still collide (the point of the key)
    fails += not check("curly/ellipsis variant collides",
                       m.norm_citation("Bakhtin, M. (1981). The Dialogic…"),
                       m.norm_citation("Bakhtin, M. (1981)"))
    # different year => different key
    fails += not check("Ito 2010 != Ito 2013",
                       m.norm_citation("Ito, M. (2010)")
                       != m.norm_citation("Ito, M. (2013)"), True)

    # --- Regression: matching layers untouched -------------------------------
    print("core matching layers (regression)")
    # lemma / normalized-exact
    fails += not check("hyphen == space (lemma)",
                       m.lemma_key("Authorial-Agency") == m.lemma_key("Authorial Agency"),
                       True)
    fails += not check("singular/plural fold",
                       m.lemma_key("agencies") == m.lemma_key("agency"), False)  # naive: agenc(ies) not folded
    # token subset signal filter: "agency" ⊂ "student agency" stays
    fails += not check("agency ⊂ student agency (kept)",
                       m.is_subset_pair("agency", "student agency"), True)
    # "agency" ⊂ long title is noise, dropped
    fails += not check("agency ⊂ long title (noise)",
                       m.is_subset_pair("agency",
                                        "the developmental sequence ability to agency"),
                       False)
    fails += not check("token_set_ratio subset == 100",
                       m.token_set_ratio("agency", "student agency"), 100)

    print(f"\n{'ALL PASS' if not fails else str(fails) + ' FAILURE(S)'}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())

def load_flagged(path):
    """flagged-pairs file: one pair_key per line (or JSON list). These were
    already surfaced in a previous review — suppress, don't re-flag."""
    try:
        with open(path) as f:
            txt = f.read().strip()
    except (FileNotFoundError, TypeError):
        return set()
    if not txt:
        return set()
    if txt.startswith("["):
        return set(json.loads(txt))
    return {ln.strip() for ln in txt.splitlines() if ln.strip()}