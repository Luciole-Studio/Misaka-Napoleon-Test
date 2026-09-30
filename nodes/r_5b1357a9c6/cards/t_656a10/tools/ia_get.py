#!/usr/bin/env python3
"""Fetch archive.org item full texts (djvu.txt) into downloads/ with a prefix."""
import os
import sys
import urllib.request

OUT = "/Users/makiko/Documents/exam/downloads"
PAIRS = [
    ("cu31924088008499", "X1_Herries_memoir_v1"),
    ("memoirofpublicli02herriala", "X1_Herries_memoir_v2"),
    ("fiftyyearsinboth00noltuoft", "X1_Nolte_FiftyYears"),
    ("mmoiresdegjouvr11ouvrgoog", "X1_Ouvrard_memoires_A"),
    ("mmoiresdegjouvr09ouvrgoog", "X1_Ouvrard_memoires_B"),
]

if len(sys.argv) > 1:
    PAIRS = []
    for a in sys.argv[1:]:
        ident, name = a.split("=", 1)
        PAIRS.append((ident, name))

for ident, name in PAIRS:
    url = "https://archive.org/download/%s/%s_djvu.txt" % (ident, ident)
    dest = os.path.join(OUT, name + ".txt")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research"})
        with urllib.request.urlopen(req, timeout=240) as r:
            data = r.read()
        with open(dest, "wb") as f:
            f.write(data)
        print("OK  %-34s %10d bytes -> %s" % (ident, len(data), dest))
        print("    head:", data[:180].decode("utf-8", "replace").replace("\n", " "))
    except Exception as e:
        print("ERR %-34s %s" % (ident, e))
