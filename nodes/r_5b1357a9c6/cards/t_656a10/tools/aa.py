#!/usr/bin/env python3
"""Thin wrapper around the annas-archive skill script (shared fixed deployment path).

Usage:
  aa.py search "query one" "query two" ...
  aa.py detail MD5
  aa.py get MD5 "Title" format outdir
"""
import json
import subprocess
import sys

PY = "/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/runtime/python/bin/python"
SCRIPT = "/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/skills/research-infra/annas-archive/scripts/annas.py"


def run(args):
    p = subprocess.run([PY, SCRIPT] + args, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def main():
    mode = sys.argv[1]
    if mode == "search":
        for q in sys.argv[2:]:
            print("=== %s ===" % q)
            rc, out, err = run(["search-book", q])
            try:
                d = json.loads(out)
            except Exception:
                print("RAW rc=%s %s %s" % (rc, out[:500], err[:500]))
                continue
            if d.get("status") != "ok":
                print("STATUS", d.get("status"), d.get("code"), str(d)[:400])
                continue
            for r in d.get("results", [])[:8]:
                print("%-6s %-9s %-10s | %-78s | %-32s | %s" % (
                    r.get("format"), r.get("size"), r.get("language"),
                    (r.get("title") or "")[:78], (r.get("authors") or "")[:32], r.get("hash")))
            print()
    elif mode == "searcha":
        for q in sys.argv[2:]:
            print("=== article: %s ===" % q)
            rc, out, err = run(["search-article", q])
            try:
                d = json.loads(out)
            except Exception:
                print("RAW rc=%s %s %s" % (rc, out[:500], err[:500]))
                continue
            for r in d.get("results", [])[:8]:
                print("%-6s %-9s | %-78s | %-40s | %s" % (
                    r.get("format"), r.get("size"), (r.get("title") or "")[:78],
                    (r.get("journal") or r.get("authors") or "")[:40], r.get("hash")))
            print()
    elif mode == "detail":
        rc, out, err = run(["detail", sys.argv[2]])
        print(out[:4000], err[:500])
    elif mode == "get":
        md5, title, fmt, outdir = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        rc, out, err = run(["download-book", md5, "--title", title, "--format", fmt, "--outdir", outdir])
        print(out[:3000], err[:1000])
    else:
        print("unknown mode")


main()
