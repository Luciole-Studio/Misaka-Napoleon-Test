#!/usr/bin/env python3
"""Extract text from SP2 downloaded books into card dir as .txt for chunked reading."""
import subprocess, zipfile, re, html, os, sys

DL = "/Users/makiko/Documents/exam/downloads"
OUT = "/Users/makiko/Documents/exam/nodes/r_5b1357a9c6/cards/t_27c409/texts"
os.makedirs(OUT, exist_ok=True)

def fold(text, width=230):
    lines = []
    for para in text.split("\n"):
        para = para.rstrip()
        while len(para) > width:
            cut = para.rfind(" ", 0, width)
            if cut < 60: cut = width
            lines.append(para[:cut]); para = para[cut:].lstrip()
        lines.append(para)
    return "\n".join(lines)

def epub_to_text(path):
    z = zipfile.ZipFile(path)
    names = [n for n in z.namelist() if re.search(r"\.(x?html?|xml)$", n) and "toc" not in n.lower()]
    names.sort()
    chunks = []
    for n in names:
        try:
            raw = z.read(n).decode("utf-8", errors="replace")
        except Exception:
            continue
        raw = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", raw, flags=re.S|re.I)
        raw = re.sub(r"<br[^>]*>", "\n", raw, flags=re.I)
        raw = re.sub(r"</(p|div|h[1-6]|li|tr)>", "\n", raw, flags=re.I)
        raw = re.sub(r"<[^>]+>", " ", raw)
        raw = html.unescape(raw)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n\s*\n+", "\n\n", raw)
        chunks.append(f"\n===== FILE: {n} =====\n" + raw.strip())
    return "\n".join(chunks)

def pdf_to_text(path):
    for tool in (["pdftotext", "-layout", path, "-"], ["pdftotext", path, "-"]):
        try:
            r = subprocess.run(tool, capture_output=True, timeout=600)
            if r.returncode == 0 and len(r.stdout) > 10000:
                return r.stdout.decode("utf-8", errors="replace")
        except FileNotFoundError:
            break
        except Exception:
            continue
    # fallback: pymupdf
    try:
        import fitz
        doc = fitz.open(path)
        out = []
        for i, page in enumerate(doc):
            out.append(f"\n===== PAGE {i+1} =====\n" + page.get_text())
        return "\n".join(out)
    except Exception as e:
        return f"EXTRACTION FAILED: {e}"

jobs = [
    ("SP2_Tone_Fatal_Knot__01cd60c2f24c.epub", "tone_fatal_knot.txt"),
    ("SP2_Fraser_Cursed_War__9ee10514803d.epub", "fraser_cursed_war.txt"),
    ("SP2_Esdaile_Peninsular_War__d271505b095f.epub", "esdaile_peninsular_war.txt"),
    ("SP2_Esdaile_Fighting_Napoleon__0ce763fec93d.pdf", "esdaile_fighting_napoleon.txt"),
    ("SP2_Lawrence_First_Carlist_War__fe68c4ce7f6e.pdf", "lawrence_carlist.txt"),
    ("SP2_Fontana_Quiebra__324203e0811f.pdf", "fontana_quiebra.txt"),
    ("SP2_Portillo_Crisis_Atlantica__821420f29964.pdf", "portillo_crisis.txt"),
    ("SP2_Hamnett_Politica_Espanola__ee4f570e810e.pdf", "hamnett_politica.txt"),
]
for src, dst in jobs:
    p = os.path.join(DL, src)
    if not os.path.exists(p):
        print("MISSING", src); continue
    if src.endswith(".epub"):
        t = epub_to_text(p)
    else:
        t = pdf_to_text(p)
    t = fold(t)
    o = os.path.join(OUT, dst)
    open(o, "w", encoding="utf-8").write(t)
    print(dst, len(t), "chars", t.count("\n")+1, "lines")
