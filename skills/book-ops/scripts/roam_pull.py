#!/usr/bin/env python3
"""roam_pull.py — build inventory.json from the Roam backend API.

PREFERRED nightly path when a read token is available: one pull, all
matching runs locally, and the full graph never enters the model's context.
(The token lives on [[Local API Token: book-ops read]]; export it before
running.) Falls back cleanly: if the MCP is the only access path, run the
same queries below through mcp__roam__roam_datomic_query and assemble the
identical schema — the schema is the only contract downstream.

Usage:
  export ROAM_GRAPH=<graph-name> ROAM_API_TOKEN=<read token>
  python3 roam_pull.py --out inventory.json [--with-edges]

inventory.json schema (the downstream contract):
{
  "pulled_at": 1783120000000,
  "pages": [ {"title": str, "uid": str, "backlinks": int,
              "created": epoch_ms, "edited": epoch_ms, "typed": bool} ],
  "edges": {"Page A": ["Referrer 1", "Referrer 2"], ...}   # only with --with-edges
}
Daily (date) pages are excluded here so no downstream consumer has to.
"""

import argparse
import json
import os
import sys
import time
import urllib.request

from matching import is_date_page

API = "https://api.roamresearch.com/api/graph/{graph}/q"

# The three reads. If pulling via the MCP instead, run these same queries.
PAGES_Q = """[:find ?title ?uid ?ct ?et
             :where [?p :node/title ?title] [?p :block/uid ?uid]
                    [?p :create/time ?ct] [?p :edit/time ?et]]"""

BACKLINK_COUNT_Q = """[:find ?title (count ?b)
                      :where [?b :block/refs ?p] [?p :node/title ?title]]"""

TYPED_Q = """[:find (distinct ?title)
             :where [?b :block/string ?s]
                    [(clojure.string/starts-with? ?s "Type::")]
                    [?b :block/page ?p] [?p :node/title ?title]]"""

EDGES_Q = """[:find ?dst ?src
             :where [?b :block/refs ?p] [?p :node/title ?dst]
                    [?b :block/page ?pg] [?pg :node/title ?src]]"""

# Delta helper — used by the nightly runner to skip the pull when nothing
# changed: pages created/edited after the watermark.
DELTA_Q = """[:find ?title ?et
             :where [?p :node/title ?title] [?p :edit/time ?et]
                    [(> ?et {watermark})]]"""


def q(graph, token, query):
    """POST a Datalog query. Roam's API 308-redirects to a peer host and
    urllib won't re-POST through that, so follow up to 3 redirects manually."""
    url = API.format(graph=graph)
    body = json.dumps({"query": query}).encode()
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {token}",
               "X-Authorization": f"Bearer {token}"}
    for _ in range(4):
        req = urllib.request.Request(url, data=body, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)["result"]
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 307, 308) and e.headers.get("Location"):
                url = e.headers["Location"]
                continue
            raise
    raise RuntimeError("too many redirects from Roam API")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="inventory.json")
    ap.add_argument("--with-edges", action="store_true",
                    help="pull referrer edges for layer-4 backlink overlap (heavier)")
    args = ap.parse_args()

    graph, token = os.environ.get("ROAM_GRAPH"), os.environ.get("ROAM_API_TOKEN")
    if not (graph and token):
        sys.exit("Set ROAM_GRAPH and ROAM_API_TOKEN "
                 "(read token: see [[Local API Token: book-ops read]]).")

    pages_raw = q(graph, token, PAGES_Q)
    counts = dict((t, c) for t, c in q(graph, token, BACKLINK_COUNT_Q))
    typed_rows = q(graph, token, TYPED_Q)
    typed = set(typed_rows[0][0]) if typed_rows else set()

    pages = []
    for title, uid, ct, et in pages_raw:
        if is_date_page(title):
            continue
        pages.append({"title": title, "uid": uid,
                      "backlinks": counts.get(title, 0),
                      "created": ct, "edited": et,
                      "typed": title in typed})

    inv = {"pulled_at": int(time.time() * 1000), "pages": pages}

    if args.with_edges:
        edges = {}
        for dst, src in q(graph, token, EDGES_Q):
            if not is_date_page(dst):
                edges.setdefault(dst, []).append(src)
        inv["edges"] = edges

    with open(args.out, "w") as f:
        json.dump(inv, f, ensure_ascii=False)
    print(f"{len(pages)} non-daily pages -> {args.out}"
          + (f" (+edges for {len(inv.get('edges', {}))} pages)" if args.with_edges else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
