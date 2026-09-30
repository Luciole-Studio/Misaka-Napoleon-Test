#!/usr/bin/env python3
import json, re
from pathlib import Path
from collections import Counter, defaultdict
W = Path("/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised/audit/20260926_草稿补回")
DRAFT = Path("/Users/makiko/Documents/exam/final/r_5b1357a9c6-report")
BOOK = Path("/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised-backup-20260926-003436/chapters")
FILES = ["10_第一部_跨国机器.md", "11_第一部_并合省实绩.md"]
VERD = {"present","partial","missing","corrected","book_wrong","structural"}
KINDS = {"heading","paragraph","table_row","list_item","quote","other"}
book = {}
for p in BOOK.glob("*.md"):
    book[p.name.split("_")[0]] = p.read_text().splitlines()
chapters = {p.name for p in BOOK.glob("*.md")}
recs = [json.loads(l) for l in (W/"ledger/S5.jsonl").read_text().splitlines()]
errs = []
cov = defaultdict(list)
for i, r in enumerate(recs, 1):
    tag = f"#{i} {r['draft_file'][:2]}:L{r['draft_line']}" + (f"p{r['part']}" if 'part' in r else "")
    if r["slice"] != "S5": errs.append(f"{tag} slice")
    if r["verdict"] not in VERD: errs.append(f"{tag} bad verdict {r['verdict']}")
    if r["kind"] not in KINDS: errs.append(f"{tag} bad kind")
    cov[(r["draft_file"], r["draft_line"])].append(r)
    v = r["verdict"]
    if v in ("partial","missing") and (not r["missing"] or not r["target"] or not r["anchor"]):
        errs.append(f"{tag} {v} needs missing/target/anchor")
    if v == "corrected":
        if not r["book_differs"]: errs.append(f"{tag} corrected needs book_differs")
        if r["missing"] and not r["target"]: errs.append(f"{tag} corrected+missing needs target")
    if v in ("present","structural") and (r["missing"] or r["target"] or r["book_differs"]):
        errs.append(f"{tag} {v} should have empty missing/target/differs")
    if v == "present" and not r["book_refs"]: errs.append(f"{tag} present needs book_refs")
    if r["target"] and r["target"] not in chapters: errs.append(f"{tag} target not a chapter file: {r['target']}")
    for ref in r["book_refs"]:
        m = re.fullmatch(r"(\d\d[ab]?):L(\d+)", ref)
        if not m: errs.append(f"{tag} bad ref {ref}"); continue
        ch, ln = m.group(1), int(m.group(2))
        lines = book.get(ch)
        if lines is None or ln > len(lines) or not lines[ln-1].strip():
            errs.append(f"{tag} ref {ref} missing/empty in snapshot")
# coverage
for f in FILES:
    lines = (DRAFT/f).read_text().splitlines()
    ne = [i for i, l in enumerate(lines, 1) if l.strip()]
    got = {k[1] for k in cov if k[0] == f}
    miss = [i for i in ne if i not in got]
    extra = [i for i in got if i not in ne]
    print(f"{f}: nonempty={len(ne)} covered={len(got & set(ne))} uncovered={miss} extra={extra}")
    if miss or extra: errs.append(f"{f} coverage problem")
    # parts consistency
for k, rs in cov.items():
    if len(rs) > 1:
        if len({r['verdict'] for r in rs}) > 1: errs.append(f"{k} parts have differing verdicts")
        if any('part' not in r for r in rs): errs.append(f"{k} multi-record without part")
print("records:", len(recs))
print("verdict counts (records):", dict(Counter(r["verdict"] for r in recs)))
line_v = {k: rs[0]["verdict"] for k, rs in cov.items()}
print("verdict counts (draft lines):", dict(Counter(line_v.values())))
for f in FILES:
    print(f"  {f}:", dict(Counter(v for k, v in line_v.items() if k[0]==f)))
cm = [k for k, rs in cov.items() if rs[0]['verdict']=='corrected' and any(r['missing'] for r in rs)]
print("corrected with non-empty missing (lines):", len(cm))
print("targets:", dict(Counter(r['target'] for r in recs if r['target'])))
print("ERRORS:", len(errs))
for e in errs: print("  ", e)
