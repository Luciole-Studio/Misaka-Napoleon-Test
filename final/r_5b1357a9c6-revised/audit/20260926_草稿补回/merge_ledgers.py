#!/usr/bin/env python3
"""Merge slice ledgers, verify every non-empty draft line is covered, and cut
per-chapter work packets for the writers.

  python3 merge_ledgers.py            # check + write packets/ and 台账_合并.csv
  python3 merge_ledgers.py --check    # check only
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

W = Path(__file__).resolve().parent
DRAFT = W.parents[2] / "r_5b1357a9c6-report"
CHAPTERS = sorted(p.name for p in (W.parents[1] / "chapters").glob("*.md"))
VERDICTS = {"present", "partial", "missing", "corrected", "book_wrong", "structural"}
ACTION = {"partial", "missing", "book_wrong", "corrected"}


def chapter_of(target):
    t = (target or "").strip()
    if not t:
        return ""
    if t in CHAPTERS:
        return t
    m = re.match(r"^(\d\d[ab]?)", t)
    if m:
        key = m[1] + ("" if m[1][-1] in "ab" else "_")
        cands = [c for c in CHAPTERS if c.startswith(key)]
        if len(cands) == 1:
            return cands[0]
    return "?" + t


rows, bad_json = [], []
for f in sorted(W.glob("ledger/S*.jsonl")):
    for n, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            bad_json.append(f"{f.name}:{n} {e}")
            continue
        r["_src"] = f.name
        rows.append(r)

covered = defaultdict(set)
for r in rows:
    covered[r.get("draft_file")].add(int(r.get("draft_line", 0)))

gaps = {}
for p in sorted(DRAFT.glob("*.md")):
    need = {i for i, l in enumerate(p.read_text().splitlines(), 1) if l.strip()}
    miss = sorted(need - covered.get(p.name, set()))
    if miss:
        gaps[p.name] = miss

problems = []
for r in rows:
    v = r.get("verdict")
    if v not in VERDICTS:
        problems.append(f"{r['_src']} {r.get('draft_file')}:{r.get('draft_line')} bad verdict {v!r}")
    needs = v in {"partial", "missing", "book_wrong"} or (v == "corrected")
    if needs:
        ch = chapter_of(r.get("target"))
        if not ch or ch.startswith("?"):
            problems.append(f"{r['_src']} {r.get('draft_file')}:{r.get('draft_line')} verdict={v} target={r.get('target')!r}")
    if v in {"partial", "missing"} and not (r.get("missing") or "").strip():
        problems.append(f"{r['_src']} {r.get('draft_file')}:{r.get('draft_line')} verdict={v} but empty 'missing'")

print("rows:", len(rows), "| bad json:", len(bad_json))
print("verdicts:", dict(Counter(r.get("verdict") for r in rows)))
print("draft files with uncovered lines:", {k: (len(v), v[:12]) for k, v in gaps.items()})
print("problems:", len(problems))
for x in problems[:60]:
    print("  ", x)
for x in bad_json[:20]:
    print("  JSON", x)

if "--check" in sys.argv:
    sys.exit(0)

packets = defaultdict(list)
for r in rows:
    if r.get("verdict") in ACTION:
        ch = chapter_of(r.get("target"))
        if ch and not ch.startswith("?"):
            packets[ch].append(r)


def anchor_key(r):
    m = re.search(r"L(\d+)", r.get("anchor") or "")
    return (int(m[1]) if m else 10**6, r.get("draft_file"), int(r.get("draft_line", 0)))


(W / "packets").mkdir(exist_ok=True)
for ch, lst in packets.items():
    lst.sort(key=anchor_key)
    with open(W / "packets" / (ch[:-3] + ".jsonl"), "w") as fh:
        for r in lst:
            fh.write(json.dumps({k: v for k, v in r.items() if k != "_src"}, ensure_ascii=False) + "\n")
print("packets:", {k: len(v) for k, v in sorted(packets.items())})

fields = ["slice", "draft_file", "draft_line", "part", "kind", "verdict", "book_refs", "missing",
          "book_differs", "target", "anchor", "note"]
with open(W / "台账_合并.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in sorted(rows, key=lambda r: (r.get("draft_file"), int(r.get("draft_line", 0)))):
        r = dict(r)
        r["book_refs"] = " ".join(r.get("book_refs") or []) if isinstance(r.get("book_refs"), list) else r.get("book_refs")
        w.writerow(r)
