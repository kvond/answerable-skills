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


def looks_like_citation(title: str) -> bool:
    """Author, X. (1999). Title...  OR  Author, 1999 — Title patterns."""
    return bool(re.search(r"\(\d{4}\)|,\s*\d{4}\s*[—\-]", title))


def norm_citation(title: str) -> str:
    """Citation collision key: author surname + year. Catches curly-vs-straight
    quotes, trailing periods, ellipsis truncations, formatting variants."""
    s = normalize_title(title)
    s = _ELLIPSIS.sub("", s)
    m = re.match(r"^@?([a-z\-']+)", s)
    surname = m.group(1) if m else s[:20]
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
