#!/usr/bin/env python3
"""
reconcile_picks.py — the guardrail between selection and action.

Reads the per-kid selection files (the album canon) and checks every photo they
mention against manifest.db (the catalog). For each pick it reports one of:
  resolved  -> exactly one real file on the T7  (good; carries its path/date/event)
  ambiguous -> the same filename exists in >1 place (needs disambiguation)
  missing   -> named but not in the catalog (broken link; re-index or fix the name)

READ-ONLY. It never moves, edits, or deletes a photo or a kid file. It only
reports, and writes two CSVs you review BEFORE any ordering/editing stage runs.

Supports kid files as .md, .txt, or .docx (no external deps required).

Usage (run via Cowork / Claude Code):
    python3 reconcile_picks.py --db manifest.db --kids-dir "/path/to/kid/files" \
        --report report.csv --resolved resolved_picks.csv
"""
import argparse, csv, os, re, sqlite3, sys, zipfile
from xml.etree import ElementTree as ET

IMG_RE = re.compile(
    r"[^\n\r\t,;\"'`*\[\]()<>]*?\.(?:jpe?g|png|tiff?|heic|webp|bmp|gif)",
    re.IGNORECASE,
)


def read_text(path):
    """Return plain text from .md/.txt directly, or from .docx via its XML."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".docx":
        try:
            with zipfile.ZipFile(path) as z:
                xml = z.read("word/document.xml")
            # strip tags, keep text nodes
            text = re.sub(r"<[^>]+>", " ", xml.decode("utf-8", "ignore"))
            return re.sub(r"\s+", " ", text)
        except Exception as e:
            print(f"  ! could not read {path}: {e}", file=sys.stderr)
            return ""
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"  ! could not read {path}: {e}", file=sys.stderr)
        return ""


def candidate_keys(mention):
    """A mention like 'the shot IMG_1234.jpg' should still resolve to IMG_1234.jpg.
    Yield the basename, then progressively trim leading words, lowercased."""
    base = os.path.basename(mention.strip())
    seen = set()
    words = base.split(" ")
    for i in range(len(words)):
        key = " ".join(words[i:]).strip().lower()
        if key and key not in seen:
            seen.add(key)
            yield key


def build_index(con):
    """Map lowercased filename -> list of (path, is_dup, event_id, taken)."""
    idx = {}
    for path, is_dup, event_id, taken in con.execute(
        "SELECT path, is_dup, event_id, taken FROM photos"
    ):
        idx.setdefault(os.path.basename(path).lower(), []).append(
            (path, is_dup, event_id, taken)
        )
    return idx


def resolve(mention, idx):
    for key in candidate_keys(mention):
        if key in idx:
            hits = idx[key]
            primary = [h for h in hits if h[1] == 0]  # prefer non-duplicates
            pool = primary if primary else hits
            if len(pool) == 1:
                p, _, ev, taken = pool[0]
                return "resolved", key, p, ev, taken
            return "ambiguous", key, "|".join(h[0] for h in pool), "", ""
    return "missing", os.path.basename(mention.strip()).lower(), "", "", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="manifest.db")
    ap.add_argument("--kids-dir", required=True, help="Folder of per-kid selection files")
    ap.add_argument("--report", default="report.csv")
    ap.add_argument("--resolved", default="resolved_picks.csv")
    args = ap.parse_args()

    con = sqlite3.connect(args.db)
    idx = build_index(con)

    report_rows, resolved_rows = [], []
    counts = {"resolved": 0, "ambiguous": 0, "missing": 0}
    per_kid = {}

    kid_files = sorted(
        f for f in os.listdir(args.kids_dir)
        if os.path.splitext(f)[1].lower() in {".md", ".txt", ".docx"}
    )
    for kf in kid_files:
        kid = os.path.splitext(kf)[0]
        text = read_text(os.path.join(args.kids_dir, kf))
        mentions = []
        seen = set()
        for m in IMG_RE.findall(text):
            m = m.strip()
            if m and m.lower() not in seen:
                seen.add(m.lower())
                mentions.append(m)
        per_kid.setdefault(kid, {"resolved": 0, "ambiguous": 0, "missing": 0})
        for mention in mentions:
            status, fname, path, ev, taken = resolve(mention, idx)
            counts[status] += 1
            per_kid[kid][status] += 1
            report_rows.append([kid, mention, fname, status, path, ev, taken])
            if status == "resolved":
                resolved_rows.append([kid, fname, path, ev, taken])

    # ordering freebie: resolved picks come out chronological within each kid
    resolved_rows.sort(key=lambda r: (r[0], r[4] or ""))

    with open(args.report, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["kid", "mention", "resolved_filename", "status", "t7_path", "event_id", "taken"])
        w.writerows(report_rows)
    with open(args.resolved, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["kid", "filename", "t7_path", "event_id", "taken"])
        w.writerows(resolved_rows)

    print(f"\nChecked {len(kid_files)} kid files against {args.db}")
    for kid, c in per_kid.items():
        flags = []
        if c["ambiguous"]:
            flags.append(f"{c['ambiguous']} ambiguous")
        if c["missing"]:
            flags.append(f"{c['missing']} MISSING")
        tail = ("  <-- " + ", ".join(flags)) if flags else ""
        print(f"  {kid}: {c['resolved']} resolved{tail}")
    print(f"\nTotals: {counts['resolved']} resolved, "
          f"{counts['ambiguous']} ambiguous, {counts['missing']} missing")
    print(f"  Report (review this): {args.report}")
    print(f"  Linked selection (feeds next stage): {args.resolved}")
    if counts["ambiguous"] or counts["missing"]:
        print("\n  STOP: fix ambiguous/missing picks before any ordering or editing stage.")
    con.close()


if __name__ == "__main__":
    main()
