#!/usr/bin/env python3
"""List files of an archive.org item. Usage: python3 ia_files.py IDENT [IDENT...]"""
import sys, json, urllib.request

for ident in sys.argv[1:]:
    print("=== " + ident + " ===")
    url = "https://archive.org/metadata/" + ident
    req = urllib.request.Request(url, headers={"User-Agent": "misaka-research/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
    except Exception as e:
        print("ERR", e)
        continue
    for f in d.get("files", []):
        n = f.get("name", "")
        if n.endswith((".txt", ".pdf", ".epub", ".gz")):
            print(" ", n, f.get("size"))
