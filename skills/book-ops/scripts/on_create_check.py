#!/usr/bin/env python3
"""on_create_check.py — the permanent guard. One proposed title vs the set.

Run BEFORE any new page is minted (QUE pages, concepts, tags). Cheap: top-k
nearest, not all-pairs.

Usage:
  python3 on_create_check.py --title "student agency" --inventory inventory.json
                             [--vocab vocabulary.json] [--k 5] [--search-wide]

Exit prints either `clear` or a ranked neighbor list with reasons.
Quarantined pages are excluded from default retrieval; --search-wide pulls
them back in. Pinned never-merge pairs are reported related-but-distinct,
never as merge candidates.
"""

import argparse
import json
import sys

from matching import (alias_expand, is_pinned, lemma_key, load_vocab,
                      looks_like_citation, norm_citation, prefix_canonical,
                      raw_subset, token_set_ratio, is_subset_pair)


def check_title(title, pages, vocab, k=5, fuzzy_threshold=88):
    """Core reusable check. pages = list of {title, backlinks, typed, ...}.
    Returns {"clear": bool, "neighbors": [...]} — neighbors carry layer/score/reason."""
    neighbors = []
    tkey = lemma_key(title)
    canon = alias_expand(title, vocab)
    pcanon = prefix_canonical(title, vocab)
    tcite = norm_citation(title) if looks_like_citation(title) else None

    for p in pages:
        pt = p["title"]
        if pt == title:
            continue
        hit = None
        if lemma_key(pt) == tkey:
            hit = (1, 100, "normalized-exact collision")
        elif tcite and looks_like_citation(pt) and norm_citation(pt) == tcite:
            hit = (1, 97, f"citation collision ({tcite})")
        elif canon != title and pt == canon:
            hit = (3, 96, "registered alias/acronym")
        elif pcanon and pt == pcanon:
            hit = (3, 95, f"extends canonical tag `{pcanon}`")
        else:
            r = token_set_ratio(title, pt)
            if r >= fuzzy_threshold:
                if raw_subset(title, pt):
                    if is_subset_pair(title, pt):  # signal-filtered; else noise
                        hit = (2, min(r, 80), "token subset — related, low confidence")
                else:
                    hit = (2, r, "fuzzy token-set match")
        if hit:
            layer, score, reason = hit
            n = {"title": pt, "layer": layer, "score": score, "reason": reason,
                 "backlinks": p.get("backlinks", 0)}
            if is_pinned(title, pt, vocab):
                n["pinned"] = True
                n["reason"] = "pinned never-merge — related-but-distinct, do NOT merge or alias"
            neighbors.append(n)

    neighbors.sort(key=lambda n: -n["score"])
    neighbors = neighbors[:k]
    mergeable = [n for n in neighbors if not n.get("pinned")]
    return {"clear": not mergeable, "neighbors": neighbors}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--inventory", required=True)
    ap.add_argument("--vocab", default=None)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--fuzzy-threshold", type=int, default=88)
    ap.add_argument("--search-wide", action="store_true",
                    help="include quarantined (untyped, thin-backlink) pages")
    args = ap.parse_args()

    with open(args.inventory) as f:
        inv = json.load(f)
    vocab = load_vocab(args.vocab)

    pages = inv["pages"]
    if not args.search_wide:
        pages = [p for p in pages
                 if p.get("typed") or p.get("backlinks", 0) > 1]

    res = check_title(args.title, pages, vocab, k=args.k,
                      fuzzy_threshold=args.fuzzy_threshold)
    if res["clear"] and not res["neighbors"]:
        print("clear")
    elif res["clear"]:
        print("clear (pinned near-neighbors exist — related-but-distinct):")
    else:
        print(f"NOT clear — {len(res['neighbors'])} near-neighbor(s):")
    for n in res["neighbors"]:
        pin = " ⛔" if n.get("pinned") else ""
        print(f"- `{n['title']}` ({n['backlinks']}bl) | L{n['layer']} {n['score']} | {n['reason']}{pin}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
