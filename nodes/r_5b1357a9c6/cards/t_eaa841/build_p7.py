# -*- coding: utf-8 -*-
"""P7 builder: merge fragment ROWS -> P7_chronicle.csv; validate; report year*column coverage gaps.
Deterministic output. Run: python3 build_p7.py [--csv-only]
"""
import csv, sys, importlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

FRAGS = ["frag_france", "frag_britain", "frag_east", "frag_central", "frag_south",
         "frag_orient", "frag_asia", "frag_atlantic", "frag_cross"]
try:
    import frag_fill  # optional gap-filler
    HAVE_FILL = True
except ImportError:
    HAVE_FILL = False

COLS = ["欧洲", "大西洋", "东方", "亚洲"]
CATS = {"边界", "君主", "条约", "军力", "财政", "经济", "科技", "社会"}
CONF = {"高", "中高", "中", "中低", "低", "低-中", "低中"}
YEARS = list(range(1803, 1849))

PREFIX = {"欧洲": "EU", "大西洋": "AT", "东方": "OR", "亚洲": "AS"}

def load_rows():
    rows = []
    for name in FRAGS:
        mod = importlib.import_module(name)
        for r in mod.ROWS:
            rows.append((name,) + tuple(r))
    if HAVE_FILL:
        for r in frag_fill.ROWS:
            rows.append(("frag_fill",) + tuple(r))
    return rows

def validate(rows):
    errs = []
    for i, (src, year, col, cat, entry, anchor, mech, conf, cards) in enumerate(rows):
        if year not in YEARS: errs.append(f"{src}#{i}: bad year {year}")
        if col not in COLS: errs.append(f"{src}#{i}: bad column {col}")
        if cat not in CATS: errs.append(f"{src}#{i}: bad category {cat}")
        if conf not in CONF: errs.append(f"{src}#{i}: bad confidence {conf}")
        for field, label in ((entry, "entry"), (anchor, "anchor"), (mech, "mechanism"), (cards, "cards")):
            if not str(field).strip(): errs.append(f"{src}#{i}: empty {label}")
    return errs

def main():
    rows = load_rows()
    errs = validate(rows)
    if errs:
        print("VALIDATION ERRORS:")
        for e in errs: print(" ", e)
        sys.exit(1)
    # sort: year, column order, category-stable
    col_order = {c: i for i, c in enumerate(COLS)}
    rows.sort(key=lambda r: (r[1], col_order[r[2]]))
    # assign ids
    counters = {}
    out_rows = []
    for src, year, col, cat, entry, anchor, mech, conf, cards in rows:
        key = (year, col)
        counters[key] = counters.get(key, 0) + 1
        rid = f"{PREFIX[col]}{year}-{counters[key]:02d}"
        out_rows.append({"id": rid, "year": year, "column": col, "category": cat,
                         "entry": entry, "anchor": anchor, "mechanism": mech,
                         "confidence": conf, "source_cards": cards})
    # coverage report
    gaps = []
    for y in YEARS:
        for c in COLS:
            if (y, c) not in counters:
                gaps.append(f"{y}×{c}")
    with open(HERE / "P7_chronicle.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["id","year","column","category","entry","anchor","mechanism","confidence","source_cards"])
        w.writeheader()
        for r in out_rows: w.writerow(r)
    print(f"rows={len(out_rows)}  cells_covered={len(counters)}/{len(YEARS)*4}")
    if gaps:
        print("GAPS (" + str(len(gaps)) + "):")
        for g in gaps: print(" ", g)
    # per-column counts
    from collections import Counter
    cc = Counter(r["column"] for r in out_rows)
    print("per-column:", dict(cc))
    yc = Counter(r["year"] for r in out_rows)
    print("min/yr:", min(yc.values()), "max/yr:", max(yc.values()))

if __name__ == "__main__":
    main()
