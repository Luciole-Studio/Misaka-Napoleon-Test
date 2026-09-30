#!/usr/bin/env python3
"""Search archive.org for identifiers. Usage: python3 ia_search.py "query" [rows]"""
import sys, json, urllib.parse, urllib.request

def search(q, rows=8):
    params = {
        "q": q,
        "fl[]": "identifier",
        "rows": str(rows),
        "output": "json",
    }
    url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(
        [("q", q), ("fl[]", "identifier"), ("fl[]", "title"), ("fl[]", "year"),
         ("fl[]", "creator"), ("rows", str(rows)), ("output", "json")])
    req = urllib.request.Request(url, headers={"User-Agent": "misaka-research/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    for x in d["response"]["docs"]:
        print(x.get("identifier"), "|", x.get("year"), "|", str(x.get("creator"))[:40], "|", str(x.get("title"))[:90])

if __name__ == "__main__":
    queries = sys.argv[1:]
    for q in queries:
        print("=== " + q + " ===")
        try:
            search(q)
        except Exception as e:
            print("ERR", e)
