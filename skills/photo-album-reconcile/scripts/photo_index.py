#!/usr/bin/env python3
"""
photo_index.py — Stage 1 of the album pipeline.

Walks a photo library (point it at your T7), records one row per image in a
SQLite manifest, flags exact duplicates by content hash, and groups photos into
"events" by gaps in time. It is READ-ONLY on your photos: it never moves,
edits, or deletes anything. Re-running resumes where it left off.

Usage (run via Claude Code on your laptop, drive plugged in):
    python3 photo_index.py --root "/Volumes/T7/WORKING_COPY" --db manifest.db
    python3 photo_index.py --root "/Volumes/T7/WORKING_COPY" --db manifest.db --export catalog.csv

Then query it, e.g. all photos from the Montessori years:
    SELECT path, taken FROM photos WHERE taken >= '2002-01-01' AND taken < '2010-01-01';
"""
import argparse, csv, hashlib, os, sqlite3, sys
from datetime import datetime, timedelta
from PIL import Image, ExifTags

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic", ".webp", ".bmp", ".gif"}
DATE_TAG = next(k for k, v in ExifTags.TAGS.items() if v == "DateTimeOriginal")  # 36867


def exif_taken(path):
    """Return ISO date string from EXIF DateTimeOriginal, else None."""
    try:
        with Image.open(path) as im:
            exif = im.getexif()
            raw = exif.get(DATE_TAG)
            if raw:
                # EXIF format: 'YYYY:MM:DD HH:MM:SS'
                return datetime.strptime(str(raw), "%Y:%m:%d %H:%M:%S").isoformat(sep=" ")
    except Exception:
        pass
    return None


def file_hash(path, blocksize=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            h.update(block)
    return h.hexdigest()


def init_db(db):
    con = sqlite3.connect(db)
    con.execute("""CREATE TABLE IF NOT EXISTS photos(
        path TEXT PRIMARY KEY, size INTEGER, mtime REAL,
        sha256 TEXT, taken TEXT, source_date TEXT,
        event_id INTEGER, is_dup INTEGER DEFAULT 0)""")
    con.commit()
    return con


def index_root(con, root, rehash_changed=True):
    cur = con.cursor()
    seen = {r[0]: (r[1], r[2]) for r in cur.execute("SELECT path,size,mtime FROM photos")}
    added = skipped = 0
    for dirpath, _, files in os.walk(root):
        for name in files:
            if os.path.splitext(name)[1].lower() not in IMAGE_EXTS:
                continue
            full = os.path.join(dirpath, name)
            try:
                st = os.stat(full)
            except OSError:
                continue
            prev = seen.get(full)
            # Resume: skip unchanged files we've already indexed (avoids rehashing
            # the whole library off a slow USB drive on every run).
            if prev and abs(prev[0] - st.st_size) == 0 and abs(prev[1] - st.st_mtime) < 1:
                skipped += 1
                continue
            sha = file_hash(full)
            taken = exif_taken(full)
            src = "exif" if taken else "filesystem"
            if not taken:
                taken = datetime.fromtimestamp(st.st_mtime).isoformat(sep=" ")
            cur.execute("""INSERT INTO photos(path,size,mtime,sha256,taken,source_date)
                           VALUES(?,?,?,?,?,?)
                           ON CONFLICT(path) DO UPDATE SET
                             size=excluded.size, mtime=excluded.mtime,
                             sha256=excluded.sha256, taken=excluded.taken,
                             source_date=excluded.source_date""",
                        (full, st.st_size, st.st_mtime, sha, taken, src))
            added += 1
            if added % 500 == 0:
                con.commit()
                print(f"  ...{added} indexed", file=sys.stderr)
    con.commit()
    return added, skipped


def flag_duplicates(con):
    con.execute("UPDATE photos SET is_dup=0")
    # Mark every copy after the first (oldest-by-path) of each identical hash.
    con.execute("""UPDATE photos SET is_dup=1 WHERE path IN (
        SELECT path FROM (
          SELECT path, ROW_NUMBER() OVER (PARTITION BY sha256 ORDER BY path) rn
          FROM photos) WHERE rn > 1)""")
    con.commit()
    return con.execute("SELECT COUNT(*) FROM photos WHERE is_dup=1").fetchone()[0]


def assign_events(con, gap_hours):
    rows = con.execute("SELECT path, taken FROM photos ORDER BY taken").fetchall()
    gap = timedelta(hours=gap_hours)
    event_id, prev = 0, None
    for path, taken in rows:
        t = datetime.fromisoformat(taken)
        if prev is None or (t - prev) > gap:
            event_id += 1
        con.execute("UPDATE photos SET event_id=? WHERE path=?", (event_id, path))
        prev = t
    con.commit()
    return event_id


def export_csv(con, out):
    rows = con.execute("""SELECT path,taken,source_date,event_id,is_dup,sha256
                          FROM photos ORDER BY taken""").fetchall()
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["path", "taken", "date_source", "event_id", "is_duplicate", "sha256"])
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="Folder to index (e.g. the T7 path)")
    ap.add_argument("--db", default="manifest.db", help="SQLite manifest file")
    ap.add_argument("--gap-hours", type=float, default=6.0,
                    help="A time gap larger than this starts a new event")
    ap.add_argument("--export", help="Optional CSV catalog to write")
    args = ap.parse_args()

    con = init_db(args.db)
    print(f"Indexing {args.root} ...", file=sys.stderr)
    added, skipped = index_root(con, args.root)
    dups = flag_duplicates(con)
    events = assign_events(con, args.gap_hours)
    total = con.execute("SELECT COUNT(*) FROM photos").fetchone()[0]
    no_exif = con.execute("SELECT COUNT(*) FROM photos WHERE source_date='filesystem'").fetchone()[0]

    print(f"\nManifest: {args.db}")
    print(f"  {total} photos indexed ({added} new this run, {skipped} unchanged/skipped)")
    print(f"  {dups} exact duplicates flagged (kept 1 of each)")
    print(f"  {events} events detected (gap > {args.gap_hours}h)")
    print(f"  {no_exif} photos missing EXIF date (fell back to file date)")
    if args.export:
        export_csv(con, args.export)
        print(f"  CSV written: {args.export}")
    con.close()


if __name__ == "__main__":
    main()
