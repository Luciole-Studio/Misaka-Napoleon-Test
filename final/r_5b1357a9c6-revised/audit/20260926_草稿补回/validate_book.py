#!/usr/bin/env python3
"""Dry-run of audit/build_book.py's manuscript checks, without writing any output.

Applies the same per-chapter footnote rewriting as the real build, then reports:
missing footnote definitions, duplicate definitions, table column mismatches,
absolute paths, and card codes / workspace paths leaking into the book text.

  python3 validate_book.py            # whole book
  python3 validate_book.py 03         # only report problems located in 03_*.md
"""
import collections
import re
import sys
from pathlib import Path

B = Path(__file__).resolve().parents[2]
chapters = sorted((B / "chapters").glob("*.md"))
only = sys.argv[1] if len(sys.argv) > 1 else None


def convert(i, p):
    s = p.read_text()
    if i == 0:
        s = re.sub(r"^### (?!引言注释)", "## ", s, flags=re.M)
        s = re.sub(r"^#### ", "### ", s, flags=re.M)
    if p.name.startswith(("03_", "04_")):
        pref = "欧" if p.name.startswith("03_") else "南"
        s = re.sub(r"^\[(\d+)\]\s+", lambda m: f"[^{pref}{m[1]}]: ", s, flags=re.M)
        s = re.sub(r"\[(\d+)\](?!\()", lambda m: f"[^{pref}{m[1]}]", s)
    s = re.sub(r"^- \*\*\[([一-鿿]+\d+)\]\*\*\s*", lambda m: f"[^{m[1]}]: ", s, flags=re.M)
    s = re.sub(r"\[([一-鿿]+\d+)\](?!\()", lambda m: f"[^{m[1]}]", s)
    s = re.sub(r"^〔([一-鿿]+\d+)〕\s*", lambda m: f"[^{m[1]}]: ", s, flags=re.M)
    s = re.sub(r"〔([一-鿿]+\d+(?:、[一-鿿]+\d+)*)〕",
               lambda m: "".join("[^" + v + "]" for v in m[1].split("、")), s)
    return s


texts = {p.name: convert(i, p) for i, p in enumerate(chapters)}
defs_at = collections.defaultdict(list)
refs_at = collections.defaultdict(list)
for name, s in texts.items():
    for n, line in enumerate(s.splitlines(), 1):
        for k in re.findall(r"^\[\^([^\]]+)\]:", line):
            defs_at[k].append(f"{name[:3]}:{n}")
        for k in re.findall(r"\[\^([^\]]+)\](?!:)", line):
            refs_at[k].append(f"{name[:3]}:{n}")

problems = []
for k, locs in refs_at.items():
    if k not in defs_at:
        problems += [(loc, f"footnote call [^{k}] has no definition") for loc in locs]
for k, locs in defs_at.items():
    if len(locs) > 1:
        problems += [(loc, f"duplicate footnote definition [^{k}] ({', '.join(locs)})") for loc in locs]
    if k not in refs_at:
        problems += [(loc, f"footnote [^{k}] defined but never called (allowed, but check)") for loc in locs]

CODE = re.compile(r"(?<![A-Za-z])(?:[FBRGDPQMXE][1-8]b?|IT[123]|SP[12]|OT|EG|PS|IN[12]|HT|MX|SA|PL|NL|SC|IE|K[123]|M-B\d|S[0-6]′?|C1[0-8]|C[1-9])卡|(?:downloads|nodes)/|t_[0-9a-f]{6}|/Users/")
SNAP = B.parent / "r_5b1357a9c6-revised-backup-20260926-003436" / "chapters"
baseline = set()
for q in SNAP.glob("*.md"):
    baseline.update(q.read_text().splitlines())
raw = {p.name: p.read_text().splitlines() for p in chapters}
for name, s in texts.items():
    inside, cols = False, None
    for n, line in enumerate(s.splitlines(), 1):
        if line.startswith("|"):
            c = len(re.split(r"(?<!\\)\|", line)) - 2
            if not inside:
                cols = c
            elif c != cols:
                problems.append((f"{name[:3]}:{n}", f"table row has {c} columns, header has {cols}"))
            inside = True
        else:
            inside = False
    for n, line in enumerate(raw[name], 1):
        if CODE.search(line) and line not in baseline:
            problems.append((f"{name[:3]}:{n}", f"card code / workspace path in book text: {CODE.search(line).group()}"))

shown = [p for p in problems if not only or p[0].startswith(only)]
hard = [p for p in shown if "never called" not in p[1]]
for loc, msg in sorted(shown):
    print(f"{loc}\t{msg}")
print(f"\n{len(hard)} blocking problem(s), {len(shown) - len(hard)} warning(s)"
      + (f" in chapter {only}" if only else ""))
sys.exit(1 if hard else 0)
