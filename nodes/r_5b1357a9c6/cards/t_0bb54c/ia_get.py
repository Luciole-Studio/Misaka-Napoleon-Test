#!/usr/bin/env python3
"""Download archive.org djvu.txt for identifiers into downloads/ with sha256 receipts.
Usage: python3 ia_get.py IDENT:outname [IDENT:outname ...]
"""
import sys, os, hashlib, urllib.request

DL = "/Users/makiko/Documents/exam/downloads"

def get(ident, out):
    url = "https://archive.org/download/" + ident + "/" + ident + "_djvu.txt"
    path = os.path.join(DL, out)
    if os.path.exists(path):
        print("EXISTS", path, os.path.getsize(path))
        return
    req = urllib.request.Request(url, headers={"User-Agent": "misaka-research/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r, open(path, "wb") as f:
            data = r.read()
            f.write(data)
    except Exception as e:
        print("ERR", ident, e)
        return
    h = hashlib.sha256(data).hexdigest()
    print("OK", path, len(data), "bytes sha256", h[:16], "url", url)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        ident, out = arg.split(":", 1)
        get(ident, out)
