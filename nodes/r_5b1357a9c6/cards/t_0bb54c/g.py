#!/usr/bin/env python3
"""Context-cheap grep: python3 g.py FILE PATTERN [MAXHITS] [WIDTH]
PATTERN is a regex, case-insensitive. Prints line-number + trimmed line."""
import sys, re

path = sys.argv[1]
pat = re.compile(sys.argv[2], re.I)
maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 40
width = int(sys.argv[4]) if len(sys.argv) > 4 else 150
n = 0
with open(path, encoding="utf-8", errors="replace") as f:
    for i, line in enumerate(f, 1):
        if pat.search(line):
            print(i, line.strip()[:width])
            n += 1
            if n >= maxhits:
                break
print("--- hits:", n)
