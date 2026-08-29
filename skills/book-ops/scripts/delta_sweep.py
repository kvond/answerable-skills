#!/usr/bin/env python3
"""delta_sweep.py — NIGHTLY sweep. O(new pages), not O(all pairs).

Checks only pages created/edited since the watermark against the whole
inventory (each new title gets an on-create-style top-k check), plus
pairwise among the new pages themselves. This is the right cost model for
a nightly cadence: duplicates enter the graph through new pages.

Usage:
  python3 delta_sweep.py --inventory inventory.json --watermark 1783120000000
                         [--vocab vocabulary.json] [--flagged flagged_pairs.txt]
                         [--fuzzy-threshold 88] [--out delta_report.json]

Watermark = epoch ms of the last successful run (stored on [[book-ops state]]).
Emits delta_report.json + markdown summary on stdout, including the NEW
watermark to write back. Never writes to Roam itself.
"""

import argparse
import json
import sys
import time
from itertools import combinations

from matching import (is_date_page, is_pinned, is_system_page,
                      load_flagged, load_vocab, pair_key)
from on_create_check import check_title

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", required=True)
    ap.add_argument("--watermark", type=int, required=True)
    ap.add_argument("--vocab", default=None)
    ap.add_argument("--flagged", default=None)
    ap.add_argument("--fuzzy-threshold", type=int, default=88)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--out", default="delta_report.json")
    args = ap.parse_args()

    with open(args.inventory) as f:
        inv = json.load(f)
    vocab = load_vocab(args.vocab)
    flagged = load_flagged(args.flagged)

    pages = [p for p in inv["pages"]
             if not is_date_page(p["title"]) and not is_system_page(p["title"])]

    def ts(p):
        return max(p.get("created", 0), p.get("edited", 0))

    new_pages = [p for p in pages if ts(p) > args.watermark]
    findings, pinned_notes = [], []

    # each new title vs the whole graph (on-create check semantics)
    for p in new_pages:
        others = [q for q in pages if q["title"] != p["title"]]
        res = check_title(p["title"], others, vocab, k=args.k,
                          fuzzy_threshold=args.fuzzy_threshold)
        for n in res["neighbors"]:
            k = pair_key(p["title"], n["title"])
            if k in flagged:
                continue
            if is_pinned(p["title"], n["title"], vocab):
                pinned_notes.append({"a": p["title"], "b": n["title"],
                                     "note": "pinned never-merge — related-but-distinct"})
                continue
            findings.append({"new_page": p["title"], "neighbor": n["title"],
                             "layer": n["layer"], "score": n["score"],
                             "reason": n["reason"], "pair_key": k,
                             "backlinks_new": p.get("backlinks", 0),
                             "backlinks_neighbor": n.get("backlinks", 0)})

    # new-vs-new (both sides entered since last run)
    seen = {f["pair_key"] for f in findings}
    for a, b in combinations(new_pages, 2):
        k = pair_key(a["title"], b["title"])
        if k in seen or k in flagged:
            continue
        res = check_title(a["title"], [b], vocab, k=1,
                          fuzzy_threshold=args.fuzzy_threshold)
        for n in res["neighbors"]:
            findings.append({"new_page": a["title"], "neighbor": b["title"],
                             "layer": n["layer"], "score": n["score"],
                             "reason": n["reason"], "pair_key": k,
                             "backlinks_new": a.get("backlinks", 0),
                             "backlinks_neighbor": b.get("backlinks", 0)})

    # quarantine check only for the new pages
    quarantine_adds = [{"title": p["title"], "backlinks": p.get("backlinks", 0)}
                       for p in new_pages
                       if not p.get("typed") and p.get("backlinks", 0) <= 1]

    findings.sort(key=lambda c: -c["score"])
    new_watermark = max([ts(p) for p in pages] + [int(time.time() * 1000)])
    out = {"findings": findings, "pinned_related": pinned_notes,
           "quarantine_adds": quarantine_adds,
           "new_watermark": new_watermark,
           "stats": {"pages_total": len(pages), "pages_new_or_edited": len(new_pages),
                     "findings": len(findings)}}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)

    s = out["stats"]
    print(f"**Delta sweep:** {s['pages_new_or_edited']} new/edited of {s['pages_total']} pages "
          f"· {s['findings']} findings · new watermark {new_watermark}\n")
    for c in findings:
        print(f"- `{c['new_page']}` ({c['backlinks_new']}bl, new) ✕ `{c['neighbor']}` "
              f"({c['backlinks_neighbor']}bl) | L{c['layer']} {c['score']} | {c['reason']}")
    for n in pinned_notes:
        print(f"- ⛔ `{n['a']}` ✕ `{n['b']}` — {n['note']}")
    for q in quarantine_adds:
        print(f"- 🗃️ quarantine add: `{q['title']}` ({q['backlinks']}bl, untyped)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
