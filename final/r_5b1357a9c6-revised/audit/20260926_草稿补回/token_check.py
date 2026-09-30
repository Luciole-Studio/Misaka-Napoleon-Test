#!/usr/bin/env python3
"""Heuristic first pass: for each non-empty draft line, list its distinctive tokens
(numbers, dates, Latin-script words/phrases, quoted strings, CJK proper-name-ish runs)
and where each occurs in the v4 book snapshot.

Usage:
  python3 token_check.py 02_第一部_法国_中枢与陆军.md            # whole file
  python3 token_check.py 20_第六部_上一轮成果与改判.md 1 108     # line range
  python3 token_check.py --grep "蒙特耶尔"                        # search book

Book snapshot = the pre-edit backup, so line numbers are stable while the
book is being edited.  This is only a finding aid: a token hit does not prove the
substance is present, and a miss does not prove it is absent (the book rewrites
numbers as words, converts dates, and translates names).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FINAL = HERE.parents[2]
DRAFT = FINAL / "r_5b1357a9c6-report"
BOOK = FINAL / "r_5b1357a9c6-revised-backup-20260926-003436" / "chapters"

book = []
for p in sorted(BOOK.glob("*.md")):
    for i, line in enumerate(p.read_text().splitlines(), 1):
        book.append((p.name[:3].rstrip("_"), i, line, re.sub(r"[,，]", "", line)))


def where(tok, norm=False, limit=4):
    hits = []
    for f, i, line, nline in book:
        if (tok in nline) if norm else (tok in line):
            hits.append(f"{f}:{i}")
            if len(hits) >= limit:
                break
    return hits


def tokens(line):
    out = []
    # numbers: strip thousands separators; keep decimals; >=3 significant chars
    for m in re.finditer(r"\d[\d,，.]*\d|\d", line):
        t = re.sub(r"[,，]", "", m.group())
        if len(t) >= 3 and not re.fullmatch(r"1[78]\d\d", t):
            out.append(("num", t))
    # ISO-ish dates 1803-11-19 -> 1803年11月19日
    for m in re.finditer(r"(1[78]\d\d)[-–](\d{1,2})[-–](\d{1,2})", line):
        out.append(("date", f"{m[1]}年{int(m[2])}月{int(m[3])}日"))
    # Latin phrases inside «» “” "" or italics
    for m in re.finditer(r"[«“\"]([^»”\"]{6,80})[»”\"]", line):
        seg = m.group(1).strip()
        if re.search(r"[A-Za-zÀ-ÿА-я]{4}", seg):
            out.append(("quote", seg[:40]))
    # Latin-script words (names, titles) >= 5 letters
    for m in re.finditer(r"[A-Z][A-Za-zÀ-ÿ'’\-]{4,}", line):
        out.append(("latin", m.group()))
    seen, res = set(), []
    for k, t in out:
        if (k, t) not in seen:
            seen.add((k, t))
            res.append((k, t))
    return res


def check(fname, a=None, b=None):
    lines = (DRAFT / fname).read_text().splitlines()
    for i, line in enumerate(lines, 1):
        if not line.strip() or (a and i < a) or (b and i > b):
            continue
        toks = tokens(line)
        found, miss = [], []
        for k, t in toks:
            h = where(t, norm=(k == "num"))
            (found if h else miss).append(f"{t}@{','.join(h)}" if h else t)
        print(f"L{i} [{len(line)}c] tokens={len(toks)} hit={len(found)} miss={len(miss)} :: {line[:90]}")
        if found:
            print("   HIT : " + " | ".join(found[:25]))
        if miss:
            print("   MISS: " + " | ".join(miss[:40]))


if __name__ == "__main__":
    if sys.argv[1] == "--grep":
        for f, i, line, _ in book:
            if sys.argv[2] in line:
                print(f"{f}:{i}: {line[:300]}")
    else:
        check(sys.argv[1], *(int(x) for x in sys.argv[2:4]))
