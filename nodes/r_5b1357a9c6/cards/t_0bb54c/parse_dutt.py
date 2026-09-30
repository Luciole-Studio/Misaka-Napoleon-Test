#!/usr/bin/env python3
"""Parse the year-by-year Indian revenue/expenditure table reproduced in
R.C. Dutt, Economic History of India under Early British Rule (1906), ch. XXIII,
itself taken from 'Returns of the Gross Revenue, &c., in India since 1792',
HC printed 22 June 1855.

Output: CSV with year, presidency, land_revenue, gross_revenue, expenditure (raw OCR + cleaned).
"""
import re, csv, sys

SRC = "/Users/makiko/Documents/exam/downloads/IN1_dutt_econ_hist_early.txt"
OUT = "/Users/makiko/Documents/exam/nodes/r_5b1357a9c6/cards/t_0bb54c/dutt_revenue_raw.csv"

lines = open(SRC, encoding="utf-8", errors="replace").read().split("\n")

# chapter range
start = None
for i, l in enumerate(lines):
    if "FINANCE AND THE ECONOMIC DRAIN (1793-1837)" in l:
        start = i
        break
end = start + 1400 if start else len(lines)

year_re = re.compile(r"^\s*(1[78]\d\d)\s*[-–]\s*(\d\d)\s*[\.\-–,]?\s*")
pres_re = re.compile(r"^\s*(Bengal|Madras|Bombay|Total|N\.?\s?W\.? Provinces|N\.W\. Provinces)", re.I)
num_re = re.compile(r"\d[\d,;:'\.\s]*\d")


def clean_num(s):
    s = s.replace(";", ",").replace(":", ",").replace("'", ",")
    s = re.sub(r"[^0-9,]", "", s)
    parts = [p for p in s.split(",") if p != ""]
    if not parts:
        return None
    # rejoin: expect groups of 3 after the first
    val = "".join(parts)
    try:
        return int(val)
    except ValueError:
        return None


rows = []
cur_year = None
for i in range(start, min(end, len(lines))):
    l = lines[i]
    m = year_re.match(l)
    if m and len(l.strip()) < 30:
        cur_year = m.group(1) + "-" + m.group(2)
        continue
    if cur_year and pres_re.match(l):
        pres = pres_re.match(l).group(1)
        tail = l[pres_re.match(l).end():]
        nums = num_re.findall(tail)
        vals = [clean_num(n) for n in nums]
        vals = [v for v in vals if v and v > 1000]
        if len(vals) >= 3:
            rows.append([cur_year, pres.strip(), vals[0], vals[1], vals[2], l.strip()[:120]])
        elif vals:
            rows.append([cur_year, pres.strip(), *(vals + [None] * (3 - len(vals))), l.strip()[:120]])

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["year", "presidency", "land_revenue", "gross_revenue", "expenditure", "ocr_line"])
    w.writerows(rows)
print("rows:", len(rows), "->", OUT)
yrs = sorted(set(r[0] for r in rows))
print("years:", yrs[0], "..", yrs[-1], "n=", len(yrs))
