#!/usr/bin/env python3
"""Archive.org 'search inside' for a lending-restricted item.
Usage: python3 ia_inside.py IDENT "query"
Returns page numbers + matched text snippets (no borrowing, no full text download)."""
import sys, json, urllib.parse, urllib.request

ident = sys.argv[1]
query = sys.argv[2]

meta_url = "https://archive.org/metadata/" + ident
req = urllib.request.Request(meta_url, headers={"User-Agent": "misaka-research/1.0"})
with urllib.request.urlopen(req, timeout=60) as r:
    m = json.load(r)
server = m.get("server")
d1 = m.get("dir")
url = ("https://" + server + "/BookReader/BookReaderSearch.php?url=ia600000.us.archive.org"
       "/fulltext/inside.php?item_id=" + ident + "&doc=" + ident + "&path=" + urllib.parse.quote(d1)
       + "&q=" + urllib.parse.quote(query))
alt = ("https://" + server + "/fulltext/inside.php?item_id=" + ident + "&doc=" + ident
       + "&path=" + urllib.parse.quote(d1) + "&q=" + urllib.parse.quote(query))
for u in (alt, url):
    try:
        rq = urllib.request.Request(u, headers={"User-Agent": "misaka-research/1.0"})
        with urllib.request.urlopen(rq, timeout=90) as r:
            data = json.load(r)
        ms = data.get("matches", [])
        print("URL OK:", u[:110])
        print("matches:", len(ms))
        for x in ms[:12]:
            pg = x.get("par", [{}])[0].get("page")
            txt = x.get("text", "").replace("\n", " ")
            print("--- page", pg, ":", txt[:400])
        break
    except Exception as e:
        print("ERR", u[:90], e)
