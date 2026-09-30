#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《胜利之后的欧洲》交付体检。

四组检查：结构保真（与源稿逐项对齐）、版面缺陷（溢出/稀疏/孤行/跨页表）、
字体承载、导航（目录页码、注释锚点、回跳链接）。
任何一项不合格即以退出码 1 终止。
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import fitz

WS = Path(__file__).resolve().parent
SOURCE = WS.parent / "胜利之后的欧洲_完整修订稿.md"
HTML = WS / "胜利之后的欧洲.html"
PDF = WS / "胜利之后的欧洲.pdf"
REPORT = WS / "build_report.json"

PAGE_W, PAGE_H = 524.41, 737.01      # 185x260mm in pt
MARGIN_L, MARGIN_R = 51.0, 473.4     # 18mm 边距
MARGIN_T, MARGIN_B = 56.7, 686.0

fails: list[str] = []
warns: list[str] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}" + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(label)


def warn(ok: bool, label: str, detail: str = "") -> None:
    if ok:
        print(f"  [PASS] {label}" + (f" — {detail}" if detail else ""))
    else:
        print(f"  [WARN] {label}" + (f" — {detail}" if detail else ""))
        warns.append(label)


md = SOURCE.read_text(encoding="utf-8")
html_text = HTML.read_text(encoding="utf-8")
report = json.loads(REPORT.read_text(encoding="utf-8"))
doc = fitz.open(PDF)

print("\n=== 1. 结构保真（源稿 → 成品） ===")

src_h1 = re.findall(r"(?m)^# (.+)$", md)
src_h2 = re.findall(r"(?m)^## (.+)$", md)
src_h3 = re.findall(r"(?m)^### (.+)$", md)
check(len(src_h1) == report["chapters"] == 12, "章数", f"源 {len(src_h1)} / 成品 {report['chapters']}")
check(len(src_h2) == report["h2_sections"], "节数(h2)", f"源 {len(src_h2)} / 成品 {report['h2_sections']}")
check(len(src_h3) == report["h3_sections"], "小节数(h3)", f"源 {len(src_h3)} / 成品 {report['h3_sections']}")

src_tables = len(re.findall(r"(?m)^\|[-: |]+\|\s*$", md))
check(src_tables == report["tables"] == html_text.count("<table "),
      "表格数", f"源 {src_tables} / HTML {html_text.count('<table ')}")

src_defs = re.findall(r"(?m)^\[\^([^\]]+)\]:", md)
src_calls = re.findall(r"\[\^([^\]]+)\](?!:)", md)
check(len(src_defs) == report["notes"], "注释定义", f"源 {len(src_defs)} / 成品 {report['notes']}")
check(len(src_calls) == report["note_calls"], "注释引用", f"源 {len(src_calls)} / 成品 {report['note_calls']}")
check(len(set(src_defs)) == len(src_defs), "注释无重复定义")
check(set(src_calls) <= set(src_defs), "注释引用全部有定义",
      f"缺失 {sorted(set(src_calls) - set(src_defs))[:5]}")
check(set(src_defs) <= set(src_calls), "注释定义全部被引用",
      f"未引用 {sorted(set(src_defs) - set(src_calls))[:5]}")

# 全书正文汉字量（PDF 提取 vs 源稿，允许目录/页眉页脚带来的增量）
pdf_text = "".join(p.get_text() for p in doc)
pdf_han = len(re.findall(r"[\u4e00-\u9fff]", pdf_text))
src_han = len(re.findall(r"[\u4e00-\u9fff]", md))
ratio = pdf_han / src_han
check(1.0 <= ratio <= 1.12, "汉字总量覆盖",
      f"源 {src_han:,} → PDF {pdf_han:,}（{ratio:.3f}×，增量来自目录与页眉）")

# 每章首段必须在 PDF 中原样出现
missing_paras = []
for chunk in re.split(r"(?m)^# ", md)[1:]:
    body = chunk.split("\n", 1)[1]
    for line in body.split("\n"):
        s = line.strip()
        if s and not s.startswith(("#", "|", ">", "-", "[^", "*")):
            probe = re.sub(r"[*`\[\]]|\(https?://[^)]+\)|\[\^[^\]]+\]", "", s)[:24]
            if probe and probe.replace(" ", "") not in pdf_text.replace("\n", "").replace(" ", ""):
                missing_paras.append(probe)
            break
check(not missing_paras, "每章首段落地 PDF", f"缺失 {missing_paras[:3]}")

print("\n=== 2. 版面缺陷 ===")

overflow, sparse, tight = [], [], []
# 页眉/页脚是 @page 的运行元素，按设计就住在页边距盒内（页脚基线 y≈706），
# 不属于正文版心。只检查正文块，否则每页都会误报一次。
RUNNING_RE = re.compile(r"^\s*\d+\s*·\s*胜利之后的欧洲\s*$")

for idx, page in enumerate(doc, 1):
    blocks = [b for b in page.get_text("blocks")
              if b[4].strip() and not RUNNING_RE.match(b[4].strip())]
    if not blocks:
        continue
    for b in blocks:
        if b[2] > MARGIN_R + 2 or b[0] < MARGIN_L - 2 or b[3] > MARGIN_B + 12:
            overflow.append((idx, round(b[0], 1), round(b[2], 1), round(b[3], 1), b[4][:30]))
    bottom = max(b[3] for b in blocks)
    fill = (bottom - MARGIN_T) / (MARGIN_B - MARGIN_T)
    # 封面(1)、目录(2-5)、章首页与末页允许留白
    if idx > 5 and idx < doc.page_count and fill < 0.5:
        sparse.append((idx, round(fill, 2)))

check(not overflow, "无内容越出版心", f"{len(overflow)} 处 {overflow[:3]}")

# 稀疏页扣除章首页（break-before: page 后的首页天然短）
chapter_starts = set()
for idx, page in enumerate(doc, 1):
    t = page.get_text()[:80]
    if re.search(r"·\s*(CHAPTER|INTRODUCTION|APPENDIX|NOTES)", t):
        chapter_starts.add(idx)
# 章末页同样豁免：kami 的末页规则允许自然收尾留白，靠塞内容填满是 draft 缺陷而非修复。
# colophon 用 .colophon 而非 .chapter，不带 chapter-num，必须单独识别，
# 否则它前一页（注释章末页）会被误判成异常稀疏页。
colophon_pages = {idx for idx, page in enumerate(doc, 1)
                  if page.get_text().lstrip().startswith("版本说明")}
section_starts = chapter_starts | colophon_pages
chapter_ends = {s - 1 for s in section_starts if s - 1 >= 1} | {doc.page_count}
real_sparse = [s for s in sparse
               if s[0] not in chapter_starts
               and s[0] + 1 not in chapter_starts
               and s[0] not in chapter_ends]
check(not real_sparse, "无异常稀疏页", f"{len(real_sparse)} 页 {real_sparse[:5]}")

# 孤行：页面仅剩一行正文
orphans = []
for idx, page in enumerate(doc, 1):
    if idx in chapter_starts or idx <= 5:
        continue
    lines = [l for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])]
    if 0 < len(lines) <= 2:
        orphans.append(idx)
check(not orphans, "无孤行页", f"{orphans[:5]}")

# 标题不得落在页面最后一行
dangling = []
for idx, page in enumerate(doc, 1):
    spans = [(l["bbox"], s) for b in page.get_text("dict")["blocks"]
             for l in b.get("lines", []) for s in l["spans"]]
    if not spans:
        continue
    body_spans = [(bb, s) for bb, s in spans if bb[3] < MARGIN_B]
    if not body_spans:
        continue
    last_bbox, last_span = max(body_spans, key=lambda x: x[0][3])
    if last_span["size"] >= 13 and last_span["font"].endswith("Medium"):
        dangling.append((idx, last_span["text"][:24]))
check(not dangling, "无标题孤悬页尾", f"{dangling[:3]}")

# 每章必须另起一页：章首标记只能出现在页面顶部，且各章首页互不相同。
# 少了这条，"章间不分页"这类缺陷会连同稀疏页豁免一起被悄悄放过。
chapter_head_pages: list[int] = []
head_not_at_top = []
for idx, page in enumerate(doc, 1):
    for b in page.get_text("blocks"):
        if re.search(r"·\s*(CHAPTER|INTRODUCTION|APPENDIX|NOTES)", b[4]):
            chapter_head_pages.append(idx)
            if b[1] > MARGIN_T + 30:
                head_not_at_top.append((idx, round(b[1], 1), b[4].strip()[:24]))
check(len(chapter_head_pages) == report["chapters"] + 1,
      "章首标记数等于章数(+注释章)",
      f"{len(chapter_head_pages)} / {report['chapters'] + 1}")
check(len(set(chapter_head_pages)) == len(chapter_head_pages),
      "每章各自另起一页", f"同页多章首 {chapter_head_pages}")
check(not head_not_at_top, "章首标记位于页顶",
      f"{head_not_at_top[:3]}")

# 表格跨页时表头需重复：抽查含表且连续两页的情况（结构性保证由 CSS thead 承担，此处验存在）
check("display: table-header-group" in html_text, "跨页表重复表头规则在位")

# 零宽色块（WeasyPrint 伪元素坑）
zero_rects = []
for idx, page in enumerate(doc, 1):
    for d in page.get_drawings():
        f = d.get("fill")
        if f and f[2] > 0.3 and f[0] < 0.2:
            r = d["rect"]
            if r.width == 0 or r.height == 0:
                zero_rects.append((idx, r.width, r.height))
check(not zero_rects, "无零宽/零高色块", f"{zero_rects[:3]}")

print("\n=== 3. 字体承载 ===")

han_by_font: Counter = Counter()
for page in doc:
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                n = len(re.findall(r"[\u4e00-\u9fff]", s["text"]))
                if n:
                    han_by_font[s["font"]] += n
total_han = sum(han_by_font.values())
tsanger = sum(v for k, v in han_by_font.items() if k.startswith("TsangerJinKai02"))
check(tsanger == total_han, "汉字全部由仓耳今楷承载",
      f"{tsanger:,}/{total_han:,}（{tsanger / total_han:.5%}）")
check(not any(k.startswith(("DejaVu", "Bitstream")) for k in han_by_font),
      "无系统兜底字体")

# 粗体必须真由 W05 承载。
# 本机实测（最小复现，逐条排除后的结论）：
#   · 纯系统字体（不写 @font-face）拿不到粗体——两个 TTF 的 style 都报 Regular，
#     fontconfig 按 weight=medium 只返回 W04；
#   · 有 @font-face 时 W05 才进得来，来源有三路：本地相对路径、jsDelivr 兜底、
#     以及 fontconfig 按全名 "TsangerJinKai02 W05" 命中 ~/Library/Fonts。
# 所以「有粗体」在本机较易满足，但换一台没装该字体、又断网的机器就会静默丢失。
# 断言同时盯住结果（Medium 实际承载量）与可移植性（本地路径正确、文件在位）。
medium_han = sum(v for k, v in han_by_font.items() if k.endswith("Medium"))
check(medium_han > 0, "粗体由 W05 实际承载",
      f"Medium 汉字 {medium_han:,}（0 表示三路来源都没取到 W05）")
strong_count = html_text.count("<strong>")
check(medium_han >= strong_count, "粗体覆盖量不少于 <strong> 数",
      f"Medium {medium_han:,} vs <strong> {strong_count}")
check('url("fonts/' in html_text and 'url("../fonts/' not in html_text,
      "@font-face 本地路径相对 HTML 正确（换机器不靠系统装没装）")
for name in ("TsangerJinKai02-W04.ttf", "TsangerJinKai02-W05.ttf"):
    check((WS / "fonts" / name).exists(), f"字体文件在位：{name}")

print("\n=== 4. 导航 ===")

toc_entries = re.findall(r'<span class="toc-page" data-href="#([^"]+)"></span>', html_text)
check(len(toc_entries) == report["toc_entries"], "目录条目数",
      f"{len(toc_entries)}")
missing_anchor = [t for t in toc_entries if f'id="{t}"' not in html_text]
check(not missing_anchor, "目录锚点全部存在", f"{missing_anchor[:3]}")

# 目录页码必须全部实算出数字。按版面坐标取右栏：章序号(00/01/…)在左栏 x≈51，
# 页码在右栏贴右边界 x≈473，两者用 x 坐标区分，不能只按「一行一个数字」抓。
toc_page_numbers: list[int] = []
for page in list(doc)[1:5]:
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                txt = s["text"].strip()
                if txt.isdigit() and s["bbox"][2] > MARGIN_R - 30:
                    toc_page_numbers.append(int(txt))
check(len(toc_page_numbers) == report["toc_entries"],
      "目录页码已实算", f"{len(toc_page_numbers)} 个 / {report['toc_entries']} 条目")
check(all(1 <= n <= doc.page_count for n in toc_page_numbers),
      "目录页码在有效范围内",
      f"越界 {[n for n in toc_page_numbers if not 1 <= n <= doc.page_count][:3]}")
check(toc_page_numbers == sorted(toc_page_numbers), "目录页码单调递增")

# 抽验：每个目录条目的页码，必须真的落在该锚点标题所在页
head_probe = []
for entry_idx, target in enumerate(toc_entries):
    m = re.search(rf'id="{re.escape(target)}"[^>]*>(?:<[^>]+>)*([^<]{{4,40}})', html_text)
    if m:
        head_probe.append((target, m.group(1).strip(), toc_page_numbers[entry_idx]))
mismatched = []
for target, text, claimed in head_probe[:40]:
    probe = re.sub(r"\s+", "", text)[:12]
    if not probe:
        continue
    found = [i + 1 for i, p in enumerate(doc)
             if probe in re.sub(r"\s+", "", p.get_text())]
    body_hits = [f for f in found if f > 5]
    if body_hits and claimed not in body_hits:
        mismatched.append((target, claimed, body_hits[:3]))
check(not mismatched, "目录页码指向正确页面（抽验前 40 条）", f"{mismatched[:3]}")

fn_ids = set(re.findall(r'<div class="note-item" id="(fn-[^"]+)"', html_text))
fn_hrefs = set(re.findall(r'<a href="#(fn-[^"]+)"', html_text))
check(fn_hrefs <= fn_ids, "注释正向链接全部有目标", f"{sorted(fn_hrefs - fn_ids)[:3]}")
check(len(fn_ids) == report["notes"], "注释条目数", f"{len(fn_ids)}")

back_hrefs = set(re.findall(r'class="note-back" href="#(fnref-[^"]+)"', html_text))
ref_ids = set(re.findall(r'<sup class="fn-ref" id="(fnref-[^"]+)"', html_text))
check(back_hrefs == ref_ids, "回跳链接与引用锚一一对应",
      f"多余 {sorted(back_hrefs - ref_ids)[:3]} / 缺失 {sorted(ref_ids - back_hrefs)[:3]}")
check(len(ref_ids) == report["note_calls"], "引用锚点数", f"{len(ref_ids)}")

# 注释编号必须 1..N 连续，且正文上标与注释条目编号一致
note_nums = [int(n) for n in re.findall(r'<span class="note-num">(\d+)</span>', html_text)]
check(note_nums == list(range(1, report["notes"] + 1)), "注释编号 1..N 连续")

pdf_links = sum(len(p.get_links()) for p in doc)
check(pdf_links >= report["note_calls"], "PDF 内部链接已生成", f"{pdf_links} 个")

# 页眉：必须取章的主标题，不得把主副标题黏成一句，也不得串到下一章
header_by_page: dict[int, str] = {}
for idx, page in enumerate(doc, 1):
    hdr = [b[4].strip() for b in page.get_text("blocks") if b[3] < MARGIN_T and b[4].strip()]
    if hdr:
        header_by_page[idx] = " ".join(hdr)

chapter_titles = {}
for m in re.finditer(r'<section class="chapter[^"]*" id="(ch\d+|notes)">.*?'
                     r'<span class="title-main">([^<]+)</span>', html_text, re.S):
    chapter_titles[m.group(1)] = m.group(2).strip()

glued = [(p, h) for p, h in header_by_page.items()
         if any(h.replace(" ", "") == (t + s).replace(" ", "")
                for t in chapter_titles.values()
                for s in re.findall(r'<span class="title-sub">([^<]+)</span>', html_text))]
check(not glued, "页眉未把主副标题黏连", f"{glued[:2]}")

known_headers = set(chapter_titles.values()) | {"版本说明"}
unknown = {p: h for p, h in header_by_page.items() if h not in known_headers}
check(not unknown, "页眉文本全部为合法章标题",
      f"{list(unknown.items())[:3]}")

colophon_page = doc.page_count
check(header_by_page.get(colophon_page) == "版本说明",
      "版本说明页页眉未沿用前章",
      f"实际 {header_by_page.get(colophon_page)!r}")

# 无未渲染的 Markdown 残留
residue = {
    "脚注标记 [^x]": len(re.findall(r"\[\^[^\]]+\]", pdf_text)),
    "粗体 **": pdf_text.count("**"),
    "表格分隔行 |---": len(re.findall(r"\|\s*-{2,}", pdf_text)),
    "占位符 {{": pdf_text.count("{{"),
    "本机路径": pdf_text.count("/Users/"),
}
for label, count in residue.items():
    check(count == 0, f"无残留：{label}", f"{count} 处")

print("\n" + "=" * 56)
print(f"体检结果：{len(fails)} 项不合格，{len(warns)} 项提醒")
print(f"成品：{PDF}（{doc.page_count} 页，{PDF.stat().st_size / 1e6:.1f} MB）")
if fails:
    print("不合格项：" + "；".join(fails))
sys.exit(1 if fails else 0)
