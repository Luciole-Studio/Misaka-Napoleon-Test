#!/usr/bin/env python3
"""Print bounded windows around regex matches in a text file.

Usage: win.py FILE PATTERN [WIN] [MAXHITS]
"""
import re
import sys

path = sys.argv[1]
pat = sys.argv[2]
win = int(sys.argv[3]) if len(sys.argv) > 3 else 900
maxhits = int(sys.argv[4]) if len(sys.argv) > 4 else 8

data = open(path, encoding="utf-8", errors="replace").read()
n = 0
for m in re.finditer(pat, data, re.I):
    a = max(0, m.start() - win // 3)
    b = min(len(data), m.end() + win)
    print("--- @%d ---" % m.start())
    print(data[a:b].replace("\n", " "))
    print()
    n += 1
    if n >= maxhits:
        break
if n == 0:
    print("NO MATCH for", pat)
