#!/usr/bin/env python3
"""
skills_audit.py — audit and organize a Claude skills directory.

Reports what makes a skill hard for a model to read: oversized SKILL.md files,
missing or weak frontmatter, missing triggers, cross-references to skills that
do not exist, and overlapping trigger phrases between skills.

Read-only by default. --fix only creates reference/ subdirectories and moves
nothing; splitting a large SKILL.md is a judgment call and stays manual.

Usage:
    python3 skills_audit.py                       # audit ~/.claude/skills
    python3 skills_audit.py --path /some/dir
    python3 skills_audit.py --fix                 # create missing reference/ dirs
"""

import argparse
import os
import re
import sys
from collections import defaultdict

# A SKILL.md above this is likely to be skimmed rather than read.
SIZE_WARN = 15_000
SIZE_ERROR = 30_000


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    out = {}
    key = None
    for line in block.splitlines():
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            out[key] = m.group(2).strip()
        elif key and line.startswith(" "):
            out[key] += " " + line.strip()
    return out


def extract_triggers(desc):
    m = re.search(r"[Tt]riggers?\s*[-:]\s*(.+)$", desc)
    if not m:
        return []
    return [t.strip().strip('."') for t in re.split(r'[,;]', m.group(1)) if t.strip()]


def audit(root):
    skills = {}
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if not os.path.isdir(d) or name.startswith("."):
            continue
        sk = os.path.join(d, "SKILL.md")
        if not os.path.isfile(sk):
            skills[name] = {"error": "no SKILL.md"}
            continue
        text = open(sk, encoding="utf-8", errors="replace").read()
        fm = parse_frontmatter(text)
        refs = []
        refdir = os.path.join(d, "reference")
        if os.path.isdir(refdir):
            refs = sorted(f for f in os.listdir(refdir) if f.endswith(".md"))
        skills[name] = {
            "path": sk,
            "size": os.path.getsize(sk),
            "mtime": os.path.getmtime(sk),
            "fm": fm,
            "text": text,
            "refs": refs,
            "triggers": extract_triggers(fm.get("description", "")),
        }
    return skills


def report(skills):
    names = set(skills)
    issues = defaultdict(list)

    print(f"\n{'SKILL':<28}{'SIZE':>8}  {'REFS':>4}  TRIGGERS")
    print("-" * 72)
    for name, s in skills.items():
        if "error" in s:
            print(f"{name:<28}{'--':>8}  {'--':>4}  {s['error']}")
            issues["structure"].append(f"{name}: {s['error']}")
            continue
        print(f"{name:<28}{s['size']:>8}  {len(s['refs']):>4}  {len(s['triggers'])}")

    print("\n== SIZE ==")
    for name, s in skills.items():
        if "error" in s:
            continue
        if s["size"] >= SIZE_ERROR:
            print(f"  [SPLIT] {name}: {s['size']:,} bytes. Move stable detail into "
                  f"{name}/reference/*.md and leave decision rules in SKILL.md.")
            issues["size"].append(name)
        elif s["size"] >= SIZE_WARN:
            print(f"  [watch] {name}: {s['size']:,} bytes.")

    print("\n== FRONTMATTER ==")
    for name, s in skills.items():
        if "error" in s:
            continue
        fm = s["fm"]
        if not fm:
            print(f"  [MISSING] {name}: no frontmatter block.")
            continue
        if fm.get("name") and fm["name"] != name:
            print(f"  [MISMATCH] {name}: frontmatter name is '{fm['name']}'.")
        if not fm.get("description"):
            print(f"  [MISSING] {name}: no description.")
        elif len(fm["description"]) < 120:
            print(f"  [THIN] {name}: description is {len(fm['description'])} chars. "
                  f"Short descriptions cause missed triggering.")
        if not s["triggers"]:
            print(f"  [NO TRIGGERS] {name}: description states no trigger phrases.")

    print("\n== CROSS-REFERENCES TO SKILLS THAT DO NOT EXIST ==")
    found_any = False
    for name, s in skills.items():
        if "error" in s:
            continue
        mentioned = set(re.findall(r"`([a-z][a-z0-9-]{3,})`", s["text"]))
        for m in mentioned:
            if m.endswith("-skill") or m.endswith("-ops") or m.endswith("-bank"):
                if m not in names:
                    print(f"  {name} -> `{m}` (not present)")
                    found_any = True
    if not found_any:
        print("  none")

    print("\n== OVERLAPPING TRIGGERS ==")
    seen = defaultdict(list)
    for name, s in skills.items():
        if "error" in s:
            continue
        for t in s["triggers"]:
            seen[t.lower()].append(name)
    overlap = {t: n for t, n in seen.items() if len(n) > 1}
    if overlap:
        for t, n in sorted(overlap.items()):
            print(f"  \"{t}\" -> {', '.join(n)}")
        print("  Two skills firing on one phrase means neither reliably wins.")
    else:
        print("  none")

    print("\n== SUGGESTED READING ORDER (smallest first) ==")
    ordered = sorted(
        ((n, s) for n, s in skills.items() if "error" not in s),
        key=lambda kv: kv[1]["size"],
    )
    for n, s in ordered:
        print(f"  {s['size']:>7,}  {n}")


def fix(root, skills):
    for name, s in skills.items():
        if "error" in s:
            continue
        if s["size"] >= SIZE_WARN and not s["refs"]:
            d = os.path.join(root, name, "reference")
            os.makedirs(d, exist_ok=True)
            print(f"  created {d}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=os.path.expanduser("~/.claude/skills"))
    ap.add_argument("--fix", action="store_true")
    a = ap.parse_args()
    if not os.path.isdir(a.path):
        sys.exit(f"Not a directory: {a.path}")
    skills = audit(a.path)
    if not skills:
        sys.exit(f"No skills found in {a.path}")
    report(skills)
    if a.fix:
        print("\n== FIX ==")
        fix(a.path, skills)
    print()


if __name__ == "__main__":
    main()
