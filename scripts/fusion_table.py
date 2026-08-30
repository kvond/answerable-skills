#!/usr/bin/env python3
"""
fusion_table.py — the fusion table across the arc
=================================================
Falls out of job 1 (`deck_inventory.py`) per `deck_work_order_of_operations.md`
§"Fusion table across the arc". One row per CYCLE: cycle, deck, critical
aspects, coordination structure or none, the reason for none, whether the
cycle carries a what-if, and its NGSS codes.

WHAT THIS TABLE IS FOR, AND WHAT IT IS NOT
------------------------------------------
It REPORTS. It does not judge.

  "An absence in that table is not automatically a hole. A standard addressed
   without a fusion device because the content carries no compensatory
   relationship and no genuine conflict case is a design decision, not a gap.
   The table tells you which one you are looking at."
                                     — deck_work_order_of_operations.md

So: a "none" in the coordination column is a measurement. The reason column is
left BLANK wherever the deck does not state a reason. A blank there means
"not stated", never "no reason exists" — and this script will not invent one.
Deciding whether a "none" is a design decision or a hole is job 3, the fusion
retrofit, done one deck at a time with the content in view.

The three coordination structures are different kinds of object, which is what
decides whether one can be retrofitted at all (nine_thinking_moves_attribution.md):

  stock-and-flow model  a REPRESENTATION — can be ADDED to any cycle whose
                        content accumulates
  compensatory pair     a CASE SET — must be FOUND in the content
  conflict case         a SINGLE CASE with opposing pulls — must be FOUND

The what-if column is reported beside them because the what-if is not a fusion
device: it tests coordination rather than creating it, and is the required
companion to whichever structure a cycle carries.

ROW COLLAPSING
--------------
One row per cycle. The "▶ LIVE" file and its "— with Concept Bank" sibling are
the same cycle and collapse into one row; the richer file wins (more slide
types present, then more slides). Cycles 07, 15 and 16 ship as lettered
sub-cycles (07a/07b, 15a/15b, 16a-d); those stay separate rows, because each is
its own cycle with its own critical aspects.

USAGE
-----
  python3 fusion_table.py [inventory.csv] [-o OUT_STEM]

  inventory.csv  default: newest audits/deck_inventory_*.csv
  -o             output stem; default audits/fusion_table_<today>
                 writes <stem>.csv and <stem>.md

Dependencies: none beyond the standard library. Reads one CSV, writes two
report files, touches nothing else.
"""
from __future__ import print_function

import argparse
import csv
import datetime
import glob
import os
import re
import sys
from collections import OrderedDict

COLUMNS = [
    "cycle",
    "deck",
    "critical_aspects",
    "n_critical_aspects",
    "coordination_structures",
    "coordination_detail",
    "reason_for_none",
    "what_if_present",
    "what_if_individual_written",
    "ngss_codes",
    "source_file",
]

# Richness: how many distinct cycle slide types the file carries, then slides.
RICHNESS_TYPES = ("Concept Bank", "Teacher note", "Teacher Prep", "Links slide",
                  "Response slide", "Day divider", "Contrast Set",
                  "Critical Aspect question", "3-Tier Question")


def cycle_sort_key(c):
    m = re.match(r"(\d+)([a-d]?)", c or "")
    return (int(m.group(1)), m.group(2)) if m else (999, "")


def richness(row):
    types = row.get("slide_types_ordered", "").split(" > ")
    have = sum(1 for t in RICHNESS_TYPES if any(x.startswith(t) for x in types))
    try:
        n = int(row.get("slides") or 0)
    except ValueError:
        n = 0
    return (have, n)


def deck_name(row):
    n = re.sub(r"^▶ LIVE — ", "", row["file"])
    n = re.sub(r"\.pptx$", "", n)
    n = re.sub(r"\s*— with Concept Bank.*$", "", n)
    n = re.sub(r"\s*\(VT deck[^)]*\)|\s*\(VT\)", "", n)
    n = re.sub(r"^Cycle\s*\d+[a-d]?\s*[—–-]?\s*", "", n)
    return n.strip(" —–-") or row["file"]


def reason_for_none(row):
    """Only a reason the DECK states counts. Per the spec the place a cycle
    declares which conditional slide types were left out and why is the teacher
    note slide (declaration 5, the slide-type map). No teacher note, or a
    teacher note that does not carry that declaration, means the reason is not
    stated — and this script leaves it blank rather than inventing one."""
    if row.get("teacher_note_slide") != "present":
        return ""
    if "slide-type map" not in (row.get("teacher_note_declares") or ""):
        return ""
    return "stated in the teacher note slide (see deck)"


def build(rows):
    by_cycle = OrderedDict()
    for r in rows:
        c = r.get("cycle") or ""
        if not c:
            continue
        prev = by_cycle.get(c)
        if prev is None or richness(r) > richness(prev):
            by_cycle[c] = r

    out = []
    for c in sorted(by_cycle, key=cycle_sort_key):
        r = by_cycle[c]
        struct = r.get("advisory2_structure") or "none"
        out.append(OrderedDict([
            ("cycle", c),
            ("deck", deck_name(r)),
            ("critical_aspects", r.get("critical_aspects", "")),
            ("n_critical_aspects", r.get("n_aspects", "")),
            ("coordination_structures", struct),
            ("coordination_detail", r.get("advisory2_detail", "")),
            ("reason_for_none", reason_for_none(r) if struct == "none" else ""),
            ("what_if_present", r.get("what_if_present", "")),
            ("what_if_individual_written", r.get("what_if_individual_written", "")),
            ("ngss_codes", r.get("ngss_codes", "")),
            ("source_file", r["file"]),
        ]))
    return out


def write_md(table, path, src, csv_path):
    carry = [t for t in table if t["coordination_structures"] != "none"]
    none = [t for t in table if t["coordination_structures"] == "none"]
    stated = [t for t in none if t["reason_for_none"]]

    L = []
    A = L.append
    A("# Fusion table across the arc")
    A("")
    A("Built from `%s` on %s. Machine-readable copy: `%s`."
      % (os.path.basename(src), datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
         os.path.basename(csv_path)))
    A("")
    A("## How to read this table")
    A("")
    A("**This table reports. It does not judge.** An absence in the coordination")
    A("column is a measurement, not a verdict. A standard addressed without a")
    A("coordination structure — because the content carries no compensatory")
    A("relationship and no genuine conflict case — is a design decision, not a gap.")
    A("The table tells you which one you are looking at; it does not tell you which")
    A("one it is.")
    A("")
    A("**The reason column is blank wherever the deck does not state a reason.**")
    A("Blank means *not stated*. It does not mean *no reason*. Nothing in this")
    A("column is inferred, guessed, or written by the script.")
    A("")
    A("The three structures are different kinds of object, and that decides what")
    A("can be retrofitted:")
    A("")
    A("| Structure | Kind | Retrofit |")
    A("|---|---|---|")
    A("| Stock-and-flow model | a representation | can be ADDED to any cycle whose content accumulates |")
    A("| Compensatory pair | a case set | must be FOUND in the content; cannot be manufactured |")
    A("| Conflict case | a single case with opposing pulls | must be FOUND |")
    A("")
    A("The what-if is **not** a fusion device. It tests coordination rather than")
    A("creating it, and it must be individual and written or the diagnosis is empty.")
    A("It is reported here as the companion to whichever structure a cycle carries.")
    A("")
    A("---")
    A("")
    A("## The table")
    A("")
    A("| Cycle | Deck | Critical aspects | Coordination structure(s) | Reason for none | What-if | NGSS |")
    A("|---|---|---|---|---|---|---|")
    for t in table:
        aspects = t["critical_aspects"].replace("|", "·") or "*none labelled*"
        wi = t["what_if_present"]
        if wi == "yes":
            wi = "yes (%s)" % t["what_if_individual_written"]
        A("| %s | %s | %s | %s | %s | %s | %s |" % (
            t["cycle"], t["deck"][:42], aspects, t["coordination_structures"],
            t["reason_for_none"], wi, t["ngss_codes"] or "—"))
    A("")
    A("---")
    A("")
    A("## Headline")
    A("")
    A("- **%d of %d cycles carry a coordination structure.**" % (len(carry), len(table)))
    A("- **%d of %d carry none.** Of those, %d state a reason in the deck; %d do not."
      % (len(none), len(table), len(stated), len(none) - len(stated)))
    A("")
    counts = {}
    for t in table:
        for s in [x.strip() for x in t["coordination_structures"].split(";")]:
            if s and s != "none":
                counts[s] = counts.get(s, 0) + 1
    A("| Structure | Cycles carrying it |")
    A("|---|---|")
    for k in sorted(counts):
        A("| %s | %d |" % (k, counts[k]))
    if not counts:
        A("| *none found* | 0 |")
    A("")
    A("### Cycles with no coordination structure")
    A("")
    A("Listed so the retrofit pass has a worklist. Being on this list is not a")
    A("finding against the cycle.")
    A("")
    for t in none:
        A("- **Cycle %s — %s** · aspects: %s · NGSS: %s"
          % (t["cycle"], t["deck"], t["critical_aspects"].replace("|", "·") or "none labelled",
             t["ngss_codes"] or "none in deck"))
    A("")
    A("### What-if coverage")
    A("")
    wi_missing = [t for t in table if t["what_if_present"] != "yes"]
    wi_notind = [t for t in table
                 if t["what_if_present"] == "yes"
                 and t["what_if_individual_written"] not in ("yes",)]
    A("- cycles with a what-if: %d of %d" % (len(table) - len(wi_missing), len(table)))
    A("- cycles whose what-if is individual and written: %d"
      % (len(table) - len(wi_missing) - len(wi_notind)))
    if wi_missing:
        A("- no what-if: %s" % ", ".join(t["cycle"] for t in wi_missing))
    if wi_notind:
        A("- what-if present but not clearly individual and written: %s"
          % ", ".join("%s (%s)" % (t["cycle"], t["what_if_individual_written"])
                      for t in wi_notind))
    A("")
    A("### NGSS across the arc")
    A("")
    all_codes = {}
    for t in table:
        for code in [c.strip() for c in t["ngss_codes"].split(";") if c.strip()]:
            all_codes.setdefault(code, []).append(t["cycle"])
    A("| Code | Cycles | Any coordination structure in those cycles |")
    A("|---|---|---|")
    for code in sorted(all_codes):
        cyc = all_codes[code]
        withs = [t["cycle"] for t in table
                 if t["cycle"] in cyc and t["coordination_structures"] != "none"]
        A("| %s | %s | %s |" % (code, ", ".join(cyc),
                                ", ".join(withs) if withs else "none"))
    A("")
    A("This is the NGSS view the table exists to make visible. It states which")
    A("standards are currently addressed without a coordination structure. It does")
    A("not claim those are gaps — name a standard you suspect and it can be checked")
    A("directly against the content.")
    with open(path, "w") as fh:
        fh.write("\n".join(L) + "\n")


def newest_inventory():
    here = os.path.dirname(os.path.abspath(__file__))
    audits = os.path.join(os.path.dirname(here), "audits")
    files = sorted(glob.glob(os.path.join(audits, "deck_inventory_*.csv")))
    return files[-1] if files else None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("inventory", nargs="?", default=None)
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args(argv)

    src = os.path.expanduser(args.inventory) if args.inventory else newest_inventory()
    if not src or not os.path.isfile(src):
        print("no inventory CSV found; run deck_inventory.py first", file=sys.stderr)
        return 2

    with open(src) as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        print("empty inventory: %s" % src, file=sys.stderr)
        return 1
    for need in ("cycle", "advisory2_structure"):
        if need not in rows[0]:
            print("inventory %s has no '%s' column" % (src, need), file=sys.stderr)
            return 1

    table = build(rows)

    stem = args.out
    if not stem:
        here = os.path.dirname(os.path.abspath(__file__))
        stem = os.path.join(os.path.dirname(here), "audits",
                            "fusion_table_%s" % datetime.date.today().isoformat())
    outdir = os.path.dirname(os.path.abspath(stem))
    if outdir and not os.path.isdir(outdir):
        os.makedirs(outdir)

    csv_path, md_path = stem + ".csv", stem + ".md"
    with open(csv_path, "w") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        for t in table:
            w.writerow(t)
    write_md(table, md_path, src, csv_path)

    carry = sum(1 for t in table if t["coordination_structures"] != "none")
    print("%d cycles -> %s" % (len(table), csv_path))
    print("%d cycles -> %s" % (len(table), md_path))
    print("carry a coordination structure: %d ; carry none: %d"
          % (carry, len(table) - carry))
    return 0


if __name__ == "__main__":
    sys.exit(main())
