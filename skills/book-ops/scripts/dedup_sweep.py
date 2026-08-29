#!/usr/bin/env python3
"""dedup_sweep.py — FULL all-pairs sweep (migration + monthly fallback).

Nightly runs should use delta_sweep.py instead; this is O(n²) and re-surfaces
the whole graph. Run it once over an existing graph, then monthly as a safety
net for anything the delta path missed.

Usage:
  python3 dedup_sweep.py --inventory inventory.json [--vocab vocabulary.json]
                         [--flagged flagged_pairs.txt] [--fuzzy-threshold 88]
                         [--thin-backlinks 1] [--out candidates.json]

Reads inventory.json (schema in roam_pull.py). Emits:
  - candidates.json  : ranked merge candidates + quarantine list
  - stdout           : compact markdown summary for the review page
Never writes to Roam. Pinned pairs are reported as related-but-distinct.
"""

import argparse
import json
import sys
from collections import defaultdict
from itertools import combinations

from matching import (alias_expand, is_date_page, is_pinned, is_subset_pair,
                      is_system_page, lemma_key, load_flagged, load_vocab,
                      looks_like_citation, norm_citation, normalize_title,
                      pair_key, prefix_canonical, raw_subset, token_set_ratio)

KNOWN_RECONCILE_MARKERS = ("chapter 9", "new chapter 2 insert",
                           "answerable teaching/chapter 5")


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", required=True)
    ap.add_argument("--vocab", default=None)
    ap.add_argument("--flagged", default=None)
    ap.add_argument("--fuzzy-threshold", type=int, default=88)
    ap.add_argument("--thin-backlinks", type=int, default=1)
    ap.add_argument("--out", default="candidates.json")
    args = ap.parse_args()

    with open(args.inventory) as f:
        inv = json.load(f)
    vocab = load_vocab(args.vocab)
    flagged = load_flagged(args.flagged)

    pages = [p for p in inv["pages"]
             if not is_date_page(p["title"]) and not is_system_page(p["title"])]
    by_title = {p["title"]: p for p in pages}
    edges = inv.get("edges", {})  # title -> [referrer titles]

    candidates, pinned_notes = [], []
    seen = set()

    def emit(a, b, layer, score, reason):
        k = pair_key(a, b)
        if k in seen or k in flagged:
            return
        seen.add(k)
        if is_pinned(a, b, vocab):
            pinned_notes.append({"a": a, "b": b, "note": "pinned never-merge — related-but-distinct"})
            return
        pa, pb = by_title[a], by_title[b]
        c = {"a": a, "b": b, "layer": layer, "score": score, "reason": reason,
             "backlinks_a": pa.get("backlinks", 0), "backlinks_b": pb.get("backlinks", 0),
             "pair_key": k}
        if edges:
            c["backlink_overlap"] = round(jaccard(edges.get(a, []), edges.get(b, [])), 2)
        winner = a if c["backlinks_a"] >= c["backlinks_b"] else b
        loser_bl = min(c["backlinks_a"], c["backlinks_b"])
        c["recommend"] = (f"merge -> {winner}" if score >= 95 and loser_bl <= 2
                          else "review")
        candidates.append(c)

    # Layer 1 — normalized-exact (incl. lemma) ------------------------------
    buckets = defaultdict(list)
    for p in pages:
        buckets[lemma_key(p["title"])].append(p["title"])
    for key, titles in buckets.items():
        if len(titles) > 1 and key:
            for a, b in combinations(sorted(titles), 2):
                emit(a, b, 1, 100, "normalized-exact collision")

    # Layer 1b — citation collisions ---------------------------------------
    cite_buckets = defaultdict(list)
    for p in pages:
        if looks_like_citation(p["title"]):
            cite_buckets[norm_citation(p["title"])].append(p["title"])
    for key, titles in cite_buckets.items():
        if len(titles) > 1:
            for a, b in combinations(sorted(titles), 2):
                emit(a, b, 1, 97, f"citation collision ({key})")

    # Layer 3 — alias/acronym + canonical-prefix (SEPTEMBER -> SEPT) ---------
    for p in pages:
        canon = alias_expand(p["title"], vocab)
        if canon != p["title"] and canon in by_title:
            emit(p["title"], canon, 3, 96, "registered alias/acronym")
        pc = prefix_canonical(p["title"], vocab)
        if pc and pc in by_title:
            emit(p["title"], pc, 3, 95, f"extends canonical tag `{pc}`")

    # Layer 2 — fuzzy -------------------------------------------------------
    titles = sorted(by_title)
    for a, b in combinations(titles, 2):
        if pair_key(a, b) in seen:
            continue
        r = token_set_ratio(a, b)
        if r >= args.fuzzy_threshold:
            if raw_subset(a, b):
                if is_subset_pair(a, b):  # signal-filtered; else noise, skip
                    emit(a, b, 2, min(r, 80), "token subset — related, low confidence")
            else:
                emit(a, b, 2, r, "fuzzy token-set match")

    # Quarantine enumerator -------------------------------------------------
    quarantine = []
    for p in pages:
        if p.get("typed"):
            continue
        if p.get("backlinks", 0) <= args.thin_backlinks:
            t = p["title"]
            known = any(m in t.casefold() for m in KNOWN_RECONCILE_MARKERS)
            quarantine.append({"title": t, "backlinks": p.get("backlinks", 0),
                               "already_known_reconcile": known})

    candidates.sort(key=lambda c: -c["score"])
    out = {"merge_candidates": candidates, "pinned_related": pinned_notes,
           "quarantine": quarantine,
           "stats": {"pages_swept": len(pages), "candidates": len(candidates),
                     "suppressed_already_flagged": len(flagged & seen),
                     "quarantine_count": len(quarantine)}}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)

    # markdown summary to stdout
    s = out["stats"]
    print(f"**Full sweep:** {s['pages_swept']} pages · {s['candidates']} candidates "
          f"· {s['quarantine_count']} quarantine\n")
    for c in candidates[:25]:
        print(f"- `{c['a']}` ({c['backlinks_a']}bl) ✕ `{c['b']}` ({c['backlinks_b']}bl) "
              f"| L{c['layer']} {c['score']} | {c['reason']} | → {c['recommend']}")
    for n in pinned_notes:
        print(f"- ⛔ `{n['a']}` ✕ `{n['b']}` — {n['note']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
