"""P7 raw extractor: pull year-table rows (markdown table lines starting with a year
1803-1848, or containing scenario-year patterns) from every unit card's main files.
Output: raw_yeartables.md grouped by card. Curation happens afterwards by hand.
"""
import re
from pathlib import Path

BASE = Path("/Users/makiko/Documents/exam/nodes/r_5b1357a9c6/cards")
OUT = BASE / "t_eaa841" / "raw_yeartables.md"

CARDS = {
 "F1": "t_08b9e7", "F2": "t_0e763d", "F3": "t_b1a536", "F4": "t_9f10b6", "F5": "t_7c3954",
 "B1": "t_c69786", "B2": "t_044211", "B3": "t_998052", "B4": "t_b9e29c", "B5": "t_87ba37",
 "B6": "t_0fed70", "IE": "t_c8b161", "R1": "t_91cbee", "R2": "t_29957a", "R3": "t_2c3192",
 "PL": "t_b5dab4", "A": "t_f4bb81", "PR": "t_3ee1b0", "G1": "t_f55d87", "G2": "t_cbaee3",
 "NL": "t_ccdcc8", "SC": "t_8b4a3e", "IT1": "t_be9258", "IT2": "t_8f2668", "IT3": "t_5b1d64",
 "SP1": "t_3282da", "SP2": "t_27c409", "PT": "t_219822", "OT": "t_66ee8d", "EG": "t_ca3e8d",
 "PS": "t_611e2b", "IN1": "t_0bb54c", "IN2": "t_05cc22", "US": "t_b0f045", "HT": "t_68821f",
 "MX": "t_9bd988", "SA": "t_f314c4", "X1": "t_656a10", "X2": "t_6f3beb", "X3": "t_86b684",
 "X4": "t_b702da", "E1": "t_02f417", "D1": "t_40198e", "D2": "t_e0038f",
}

SKIP = re.compile(r"notes|SOURCES|VALIDATION|part_|phase|quote|audit|README|checks", re.I)
# a table row whose first cell starts with a year in range, e.g. | 1807 |, |1806–08|, | **1810** |
YEAR_ROW = re.compile(r"^\|\s*\**\s*(1(?:80[3-9]|8[1-4][0-9]))")
# year in 2nd cell after an index/scenario cell: | 2 | 1804 | ... or | S2 | 1805 |
YEAR_ROW2 = re.compile(r"^\|[^|]{0,12}\|\s*\**\s*(1(?:80[3-9]|8[1-4][0-9]))")
# bold/heading year lines: **1807｜...** or #### 1807
HEAD_ROW = re.compile(r"^\s*(?:#{2,6}\s*)?\**\s*(1(?:80[3-9]|8[1-4][0-9]))[\u4e00-\u9fff\s\u3001\uff5c|:\uff1a\-\u2013]")
# also capture numbered-list year lines: "12. 1811：..." or "- 1816–17："
LIST_ROW = re.compile(r"^\s*(?:[-*]|\d+[\.、])\s*(?:\[S[0-9][^\]]*\]\s*)?\**(1(?:80[3-9]|8[1-4][0-9]))")

def main():
    out = []
    for label, tid in CARDS.items():
        d = BASE / tid
        files = sorted(p for p in d.glob("*.md") if not SKIP.search(p.name))
        got = 0
        out.append(f"\n\n## {label} ({tid})\n")
        for f in files:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                out.append(f"READ_FAIL {f.name}: {e}\n")
                continue
            hits = []
            for i, line in enumerate(text.splitlines()):
                if YEAR_ROW.match(line) or YEAR_ROW2.match(line) or LIST_ROW.match(line) or HEAD_ROW.match(line):
                    hits.append(line.rstrip())
            if hits:
                out.append(f"### file: {f.name} ({len(hits)} rows)\n")
                out.extend(h + "\n" for h in hits)
                got += len(hits)
        if got == 0:
            out.append("NO_YEAR_ROWS_FOUND (check file naming / formats manually)\n")
    OUT.write_text("".join(out), encoding="utf-8")
    print(f"wrote {OUT}, {sum(1 for l in ''.join(out).splitlines() if l.startswith('|'))} table rows")

if __name__ == "__main__":
    main()
