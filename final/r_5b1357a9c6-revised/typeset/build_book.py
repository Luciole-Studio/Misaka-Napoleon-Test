#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《胜利之后的欧洲》书籍排版构建脚本。

来源：../胜利之后的欧洲_完整修订稿.md（pandoc 风格 Markdown + [^key] 脚注）
体例：kami long-doc 模板的 head/CSS 原样取用，改 16 开 185x260mm；
      封面 / 目录（章-节两级，target-counter 实算页码）/ 十二章 / 书末注释与文献。
输出：胜利之后的欧洲.html + 胜利之后的欧洲.pdf
"""
from __future__ import annotations

import html
import json
import re
import subprocess
from collections import Counter, OrderedDict
from pathlib import Path

import fitz

WS = Path(__file__).resolve().parent
BOOK_DIR = WS.parent
SOURCE = BOOK_DIR / "胜利之后的欧洲_完整修订稿.md"
HTML_OUT = WS / "胜利之后的欧洲.html"
PDF_OUT = WS / "胜利之后的欧洲.pdf"
REPORT_OUT = WS / "build_report.json"
KAMI = Path("/Users/makiko/.hermes/profiles/index/skills/creative-media/kami")
TEMPLATE = KAMI / "assets" / "templates" / "long-doc.html"
WEASYPRINT = Path("/opt/homebrew/bin/weasyprint")

TITLE = "胜利之后的欧洲"
SUBTITLE = "拿破仑的另一条道路，1803—1848"
EDITION = "2026 年 9 月修订本"

# 章序号标签：引言与资料附编不参与「第N章」编号。
CHAPTER_LABELS = {
    "引言": ("00", "INTRODUCTION"),
    "资料附编": ("附", "APPENDIX"),
}


# ---------------------------------------------------------------- 行内渲染

FOOTNOTE_KEYS: "OrderedDict[str, int]" = OrderedDict()   # key -> 定义顺序
NOTE_TEXT: dict[str, str] = {}                            # key -> 定义正文（原始 md）
NOTE_CALLS: dict[str, list[str]] = {}                     # key -> 各次引用的锚 id


def inline(text: str, allow_notes: bool = True) -> str:
    """Markdown 行内语法 -> HTML。转义先行，避免稿件里的 < > & 破坏结构。"""
    value = html.escape(text.strip(), quote=False)
    # 链接：[显示文本](url)
    value = re.sub(
        r"\[([^\]\[]+)\]\((https?://[^)\s]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        value,
    )
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)", r"<cite>\1</cite>", value)
    value = re.sub(r"`([^`]+?)`", r"<code>\1</code>", value)
    if allow_notes:
        value = re.sub(r"\[\^([^\]]+)\]", _note_call, value)
    return value


def _note_call(match: re.Match) -> str:
    key = match.group(1)
    seq = NOTE_CALLS.setdefault(key, [])
    anchor = f"fnref-{slugify_key(key)}-{len(seq) + 1}"
    seq.append(anchor)
    # 注释编号在全书注释章统一编定，此处先留占位，回填阶段替换。
    return f'<sup class="fn-ref" id="{anchor}"><a href="#fn-{slugify_key(key)}">@@{key}@@</a></sup>'


KEY_SLUGS: dict[str, str] = {}


def slugify_key(key: str) -> str:
    if key not in KEY_SLUGS:
        KEY_SLUGS[key] = f"n{len(KEY_SLUGS) + 1:04d}"
    return KEY_SLUGS[key]


# ---------------------------------------------------------------- 块级解析

def pipe_cells(line: str) -> list[str]:
    body = line.strip().strip("|")
    return [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", body)]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(
        re.fullmatch(r":?-{2,}:?", cell.replace(" ", "")) for cell in cells
    )


def render_table(lines: list[str], start: int) -> tuple[str, int, int]:
    header = pipe_cells(lines[start])
    if start + 1 >= len(lines) or not is_separator_row(pipe_cells(lines[start + 1])):
        return f"<p>{inline(lines[start])}</p>", start + 1, 0
    align_spec = pipe_cells(lines[start + 1])
    rows: list[list[str]] = []
    i = start + 2
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append(pipe_cells(lines[i]))
        i += 1

    aligns = [
        "align-right" if idx < len(align_spec) and align_spec[idx].strip().endswith(":") else ""
        for idx in range(len(header))
    ]
    classes = ["kami-table"]
    if len(rows) > 16:
        classes.append("compact")
    if len(header) >= 5:
        classes.append("narrow")
    out = [f'<div class="table-wrap"><table class="{" ".join(classes)}"><thead><tr>']
    for idx, cell in enumerate(header):
        out.append(f'<th class="{aligns[idx]}">{inline(cell)}</th>')
    out.append("</tr></thead><tbody>")
    for row in rows:
        row = row + [""] * (len(header) - len(row))
        # 全行加粗 = 小计/合计行，走 kami 的 .total 样式。
        is_total = any(re.fullmatch(r"\*\*.+\*\*", c.strip()) for c in row[:1]) and any(
            re.fullmatch(r"\*\*.+\*\*", c.strip()) for c in row[1:2] or [""]
        )
        out.append('<tr class="total">' if is_total else "<tr>")
        for idx, cell in enumerate(row[: len(header)]):
            out.append(f'<td class="{aligns[idx]}">{inline(cell)}</td>')
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out), i, len(rows)


def render_body(lines: list[str], counters: Counter, slug: str) -> tuple[list[str], dict]:
    out: list[str] = []
    stats = {"tables": 0, "table_rows": 0, "paragraphs": 0, "h2": 0, "h3": 0,
             "lists": 0, "quotes": 0, "headings": []}
    i = 0
    first_para = True
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue

        heading = re.match(r"^(#{2,4})\s+(.+?)\s*$", stripped)
        if heading:
            depth = len(heading.group(1))
            text = heading.group(2).strip()
            counters[slug] += 1
            hid = f"{slug}-s{counters[slug]:03d}"
            out.append(
                f'<h{depth} id="{hid}" class="lvl{depth}">{inline(text)}</h{depth}>'
            )
            stats[f"h{depth}"] = stats.get(f"h{depth}", 0) + 1
            stats["headings"].append({"level": depth, "id": hid, "text": text})
            i += 1
            first_para = False
            continue

        if stripped.startswith("|"):
            rendered, i, rows = render_table(lines, i)
            out.append(rendered)
            stats["tables"] += 1
            stats["table_rows"] += rows
            continue

        if stripped.startswith(">"):
            parts = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                parts.append(lines[i].strip().lstrip(">").strip())
                i += 1
            body = "<br>".join(inline(p) for p in parts if p)
            out.append(f"<blockquote>{body}</blockquote>")
            stats["quotes"] += 1
            continue

        if stripped.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                item = lines[i].strip()[2:].strip()
                i += 1
                # 续行（缩进或非块首的裸行）并入同一列表项
                while (i < len(lines) and lines[i].strip()
                       and not lines[i].strip().startswith(("- ", "|", ">", "#"))
                       and lines[i].startswith(("  ", "\t"))):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            out.append("<ul>")
            out.extend(f"<li>{inline(item)}</li>" for item in items)
            out.append("</ul>")
            stats["lists"] += 1
            continue

        if stripped == "---":
            out.append('<hr class="rule">')
            i += 1
            continue

        para = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip():
            nxt = lines[i].strip()
            if re.match(r"^#{2,4}\s+", nxt) or nxt.startswith(("|", ">", "- ")) or nxt == "---":
                break
            para.append(nxt)
            i += 1
        text = " ".join(para)
        klass = ' class="lead"' if first_para else ""
        out.append(f"<p{klass}>{inline(text)}</p>")
        stats["paragraphs"] += 1
        first_para = False

    return out, stats


# ---------------------------------------------------------------- 主流程

def split_front_matter(raw: str) -> str:
    if raw.startswith("---"):
        end = raw.index("\n---", 3)
        return raw[end + 4 :]
    return raw


def collect_notes(raw: str) -> str:
    """抽出所有 [^key]: 定义，返回去掉定义行的正文。"""
    lines = raw.split("\n")
    body: list[str] = []
    current: str | None = None
    for line in lines:
        m = re.match(r"^\[\^([^\]]+)\]:\s*(.*)$", line)
        if m:
            current = m.group(1)
            if current in NOTE_TEXT:
                raise RuntimeError(f"duplicate footnote definition: {current}")
            NOTE_TEXT[current] = m.group(2).strip()
            FOOTNOTE_KEYS[current] = len(FOOTNOTE_KEYS) + 1
            continue
        if current is not None:
            if line.strip() == "":
                current = None
                continue
            if line.startswith(("    ", "\t")) or not re.match(r"^[#|>-]", line.strip()):
                NOTE_TEXT[current] += " " + line.strip()
                continue
            current = None
        body.append(line)
    return "\n".join(body)


def chapter_meta(title: str, index: int) -> tuple[str, str, str, str]:
    """返回 (slug, 编号, 英文标签, 主标题)。标题形如「第一章　法国：…」。"""
    head, _, rest = title.partition("　")
    if head in CHAPTER_LABELS:
        num, label = CHAPTER_LABELS[head]
    else:
        m = re.match(r"^第([一二三四五六七八九十]+)章$", head)
        if not m:
            raise RuntimeError(f"unrecognised chapter head: {title!r}")
        digits = "一二三四五六七八九十"
        cn = m.group(1)
        value = 10 if cn == "十" else (10 + digits.index(cn[-1]) + 1 if cn.startswith("十") else digits.index(cn) + 1)
        num, label = f"{value:02d}", "CHAPTER"
    return f"ch{index:02d}", num, label, rest.strip()


UTILITY_CSS = r"""

  /* ========== 书籍体例：16 开 185x260mm ========== */
  @page {
    size: 185mm 260mm;
    margin: 20mm 18mm 18mm 18mm;
  }
  @page:first {
    margin: 0;
    @top-right { content: ""; }
    @bottom-center { content: ""; }
  }

  @media screen {
    body { max-width: 185mm; padding: 20mm 18mm 18mm; }
  }

  body { font-size: 10.2pt; line-height: 1.62; letter-spacing: 0.25pt; }
  p { text-align: justify; text-justify: inter-ideograph; margin-bottom: 8pt; }
  a { color: inherit; text-decoration: none; }
  cite { font-style: normal; color: var(--dark-warm); }

  /* ---------- 封面 ---------- */
  .cover {
    min-height: 260mm;
    padding: 46mm 20mm 24mm;
    break-after: page;
    border-top: 6pt solid var(--brand);
  }
  .cover-eyebrow { display: block; margin-bottom: 20pt; }
  .cover-eyebrow::before { content: none; }
  .cover-eyebrow .rule {
    display: inline-block;
    width: 9pt; height: 1.5pt;
    background: var(--brand);
    vertical-align: .2em;
    margin-right: 8pt;
  }
  .cover-title { font-size: 40pt; letter-spacing: 2pt; margin-bottom: 14pt; }
  .cover-sub { font-size: 13.5pt; letter-spacing: .6pt; max-width: 100%; margin-bottom: 26pt; }
  .cover-facts {
    font-family: var(--sans);
    font-size: 9.5pt;
    color: var(--stone);
    letter-spacing: .4pt;
    border-top: .6pt solid var(--border);
    padding-top: 10pt;
  }
  .cover-meta .imprint { margin-top: 6pt; }

  /* ---------- 目录 ---------- */
  .toc { break-after: page; }
  .toc h2 { font-size: 20pt; margin-bottom: 16pt; }
  .toc-entry {
    display: grid;
    grid-template-columns: 26pt 1fr auto;
    align-items: baseline;
    column-gap: 7pt;
    padding: 5pt 0 4pt;
    font-size: 10.6pt;
    line-height: 1.3;
    break-inside: avoid;
    border-bottom: none;
  }
  .toc-entry.chapter-row {
    margin-top: 11pt;
    padding-bottom: 4pt;
    border-bottom: .5pt solid var(--border);
  }
  .toc-entry.chapter-row .toc-label {
    font-weight: 500;
    color: var(--near-black);
  }
  .toc-entry.chapter-row .toc-index {
    font-family: var(--sans);
    font-size: 9pt;
    color: var(--brand);
    letter-spacing: .6pt;
  }
  .toc-entry.section-row {
    padding: 2.6pt 0;
    font-size: 9.4pt;
    color: var(--olive);
  }
  .toc-entry.section-row .toc-index { color: transparent; }
  .toc-entry.section-row .toc-label { padding-left: 8pt; color: var(--olive); }
  .toc-page {
    font-variant-numeric: tabular-nums;
    font-size: 9.4pt;
    color: var(--stone);
    text-align: right;
  }
  .toc-page::after { content: target-counter(attr(data-href), page); }

  /* ---------- 章 ---------- */
  .chapter { break-before: page; }
  .chapter-head {
    margin-bottom: 20pt;
    padding-bottom: 12pt;
    border-bottom: .8pt solid var(--border);
  }
  .chapter-num { margin-bottom: 8pt; }
  .chapter h1 {
    font-size: 21pt;
    line-height: 1.32;
    border-left: none;
    padding-left: 0;
    margin: 0;
    /* 页眉只取主标题：h1 本身不再 string-set，否则 content() 会把主副标题
       两个 span 的文本直接黏成一句（「法国胜利所需要的国家」丢掉冒号）。 */
    string-set: none;
  }
  .chapter h1 .title-main {
    display: block;
    string-set: section-title content();
  }
  .chapter h1 .title-sub {
    display: block;
    font-size: 13pt;
    color: var(--olive);
    margin-top: 6pt;
    line-height: 1.4;
  }
  /* 版本说明页自成一体，不沿用前一章的页眉。 */
  .colophon h2 { string-set: section-title content(); }

  h2.lvl2 {
    font-size: 14.5pt;
    margin: 22pt 0 8pt;
    padding-left: 7pt;
    border-left: 2pt solid var(--brand);
    border-radius: 1pt;
  }
  h3.lvl3 {
    font-size: 11.6pt;
    margin: 15pt 0 5pt;
    color: var(--brand);
  }
  h4.lvl4 { font-size: 10.6pt; margin: 12pt 0 4pt; color: var(--dark-warm); }

  .lead { font-size: 10.6pt; color: var(--dark-warm); margin-bottom: 11pt; }

  blockquote {
    font-size: 9.8pt;
    margin: 11pt 0;
    padding: 2pt 0 2pt 13pt;
  }
  hr.rule {
    border: none;
    border-top: .5pt solid var(--border);
    margin: 16pt 0;
  }
  ul { margin: 7pt 0 9pt; padding-left: 16pt; }
  ul li { margin-bottom: 5pt; line-height: 1.6; }

  /* ---------- 表格 ---------- */
  .table-wrap { margin: 12pt 0 14pt; break-inside: auto; }
  .table-wrap table { margin: 0; break-inside: auto; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
  table, .kami-table {
    font-size: 8.8pt;
    line-height: 1.45;
    border-top: 1pt solid var(--brand);
    border-bottom: 1pt solid var(--brand);
  }
  table th, .kami-table th {
    font-size: 8.6pt;
    padding: 5pt 6pt;
    border-bottom: .8pt solid var(--border);
  }
  table td, .kami-table td { padding: 4pt 6pt; }
  table.narrow th, .kami-table.narrow th,
  table.narrow td, .kami-table.narrow td { font-size: 8.2pt; padding: 3.4pt 5pt; }
  table .align-right, .kami-table .align-right {
    text-align: right;
    font-variant-numeric: tabular-nums;
  }
  table tr.total td, .kami-table tr.total td {
    font-weight: 500;
    border-top: .8pt solid var(--brand);
    border-bottom: none;
  }

  /* ---------- 注释 ---------- */
  .fn-ref {
    font-family: var(--sans);
    font-size: 7pt;
    vertical-align: super;
    line-height: 0;
    color: var(--brand);
    padding: 0 .4pt;
  }
  .notes-chapter .note-item {
    display: grid;
    grid-template-columns: 24pt 1fr;
    column-gap: 5pt;
    font-size: 8.6pt;
    line-height: 1.55;
    color: var(--olive);
    margin-bottom: 7pt;
    break-inside: avoid;
  }
  .notes-chapter .note-num {
    font-family: var(--sans);
    font-size: 8pt;
    color: var(--brand);
    text-align: right;
  }
  .notes-chapter .note-body { text-align: left; }
  .notes-chapter .note-body a { color: var(--brand); }
  .notes-chapter .note-back {
    font-size: 7.6pt;
    color: var(--stone);
    margin-left: 3pt;
    white-space: nowrap;
  }
  .notes-group-label {
    font-family: var(--sans);
    font-size: 9pt;
    font-weight: 500;
    color: var(--brand);
    letter-spacing: 1.4pt;
    margin: 22pt 0 9pt;
    padding-bottom: 3.5pt;
    border-bottom: .7pt solid var(--brand);
    break-after: avoid;
  }
  .notes-group-label:first-of-type { margin-top: 6pt; }

  /* ---------- 版本记录 ---------- */
  .colophon {
    break-before: page;
    min-height: 200mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    color: var(--stone);
    font-size: 9pt;
    line-height: 1.6;
  }
  .colophon h2 { color: var(--near-black); font-size: 14pt; margin-bottom: 10pt; }
  .colophon p { text-align: left; margin-bottom: 5pt; }
"""


def build() -> dict:
    for path in (SOURCE, TEMPLATE, WEASYPRINT):
        if not path.exists():
            raise FileNotFoundError(path)

    raw = SOURCE.read_text(encoding="utf-8").replace("\r\n", "\n")
    raw = split_front_matter(raw)
    body_md = collect_notes(raw)

    parts = re.split(r"(?m)^# (.+?)\s*$", body_md)
    if parts[0].strip():
        raise RuntimeError("content before first H1")
    chapters = [(parts[i].strip(), parts[i + 1].splitlines()) for i in range(1, len(parts), 2)]

    counters: Counter = Counter()
    sections_html: list[str] = []
    toc_rows: list[str] = []
    chapter_reports = []

    for index, (title, lines) in enumerate(chapters):
        slug, num, label, main = chapter_meta(title, index)
        head, _, sub = main.partition("：")
        body_html, stats = render_body(lines, counters, slug)

        toc_rows.append(
            f'<div class="toc-entry chapter-row">'
            f'<span class="toc-index">{num}</span>'
            f'<a class="toc-label" href="#{slug}">{html.escape(main)}</a>'
            f'<span class="toc-page" data-href="#{slug}"></span></div>'
        )
        for item in stats["headings"]:
            if item["level"] != 2:
                continue
            toc_rows.append(
                f'<div class="toc-entry section-row">'
                f'<span class="toc-index">·</span>'
                f'<a class="toc-label" href="#{item["id"]}">{html.escape(item["text"])}</a>'
                f'<span class="toc-page" data-href="#{item["id"]}"></span></div>'
            )

        title_html = (
            f'<span class="title-main">{html.escape(head)}</span>'
            f'<span class="title-sub">{html.escape(sub)}</span>'
            if sub
            else f'<span class="title-main">{html.escape(head)}</span>'
        )
        sections_html.append(
            f'<section class="chapter" id="{slug}">'
            f'<div class="chapter-head">'
            f'<div class="chapter-num">{num} · {label}</div>'
            f"<h1>{title_html}</h1>"
            f"</div>\n" + "\n".join(body_html) + "\n</section>"
        )
        chapter_reports.append({"title": title, "slug": slug, "num": num, **{
            k: v for k, v in stats.items() if k != "headings"}, "h2_count": stats.get("h2", 0)})

    # ---- 全书注释章 -------------------------------------------------
    missing = [k for k in NOTE_CALLS if k not in NOTE_TEXT]
    if missing:
        raise RuntimeError({"missing_note_definitions": missing})
    unused = [k for k in NOTE_TEXT if k not in NOTE_CALLS]
    if unused:
        raise RuntimeError({"unused_note_definitions": unused})

    # 按正文首次引用顺序编号（读者顺序），而非定义顺序。
    ordered_keys = sorted(NOTE_CALLS, key=lambda k: FOOTNOTE_KEYS[k])
    note_numbers = {key: idx + 1 for idx, key in enumerate(ordered_keys)}

    group_titles = {
        "导": "引言", "法": "第一章　法国", "法海": "第一章　法国海军",
        "英政": "第二章　英国政治", "英财": "第二章　英国财政", "英市": "第二章　英国市场",
        "海": "第三章　舰队与海峡", "海技": "第三章　海军技术",
        "欧": "第四章　欧洲大陆诸国", "南": "第五章　南欧与罗马",
        "美补": "第六章　美洲", "帝": "第七章　东方与帝国", "省": "第八章　行省化",
    }
    note_html = ['<section class="chapter notes-chapter" id="notes">',
                 '<div class="chapter-head"><div class="chapter-num">注释 · NOTES &amp; SOURCES</div>',
                 "<h1><span class=\"title-main\">全书注释与文献</span>"
                 "<span class=\"title-sub\">按正文出现顺序编号；箭头返回引用处</span></h1></div>"]
    current_group = None
    for key in ordered_keys:
        prefix = re.match(r"^([^\d]+)", key).group(1)
        if prefix != current_group:
            current_group = prefix
            label = group_titles.get(prefix, prefix)
            note_html.append(f'<div class="notes-group-label">{html.escape(label)}</div>')
        num = note_numbers[key]
        backs = "".join(
            f'<a class="note-back" href="#{anchor}" '
            f'aria-label="返回正文引用{idx}">↩{idx if len(NOTE_CALLS[key]) > 1 else ""}</a>'
            for idx, anchor in enumerate(NOTE_CALLS[key], 1)
        )
        note_html.append(
            f'<div class="note-item" id="fn-{slugify_key(key)}">'
            f'<span class="note-num">{num}</span>'
            f'<span class="note-body">{inline(NOTE_TEXT[key], allow_notes=False)}{backs}</span>'
            f"</div>"
        )
    note_html.append("</section>")
    toc_rows.append(
        '<div class="toc-entry chapter-row">'
        '<span class="toc-index">注</span>'
        '<a class="toc-label" href="#notes">全书注释与文献</a>'
        '<span class="toc-page" data-href="#notes"></span></div>'
    )

    # ---- 装配 -------------------------------------------------------
    han = len(re.findall(r"[\u4e00-\u9fff]", body_md))
    cover = f"""
<section class="cover" id="cover">
  <div>
    <div class="cover-eyebrow"><span class="rule"></span>历史研究 · 反事实史</div>
    <div class="cover-title">{TITLE}</div>
    <div class="cover-sub">{SUBTITLE}</div>
  </div>
  <div class="cover-meta">
    <div class="cover-facts">约 {han // 10000} 万字 · 引言与十章 · 资料附编 ·
      {sum(r["tables"] for r in chapter_reports)} 表 · {len(ordered_keys)} 条注释</div>
    <div class="imprint">{EDITION}</div>
  </div>
</section>""".strip()

    toc = ('<section class="toc" id="book-toc"><h2>目录</h2>\n'
           + "\n".join(toc_rows) + "\n</section>")

    colophon = f"""
<section class="colophon" id="colophon">
  <div>
    <h2>版本说明</h2>
    <p>本书为《{TITLE}》{EDITION}，正文 {han:,} 汉字，含 {len(chapters)} 个部分、
      {sum(r["tables"] for r in chapter_reports)} 张数据表与 {len(ordered_keys)} 条注释
      （正文引用 {sum(len(v) for v in NOTE_CALLS.values())} 处）。</p>
    <p>排版取自 Kami long-doc 模板，开本 16 开 185×260mm；目录页码由渲染器实算，
      注释按正文出现顺序编号并保留回跳链接。</p>
    <p>本书为反事实史研究：史料、推断与未核数值分开标注，推演不冒充已发生的历史。</p>
  </div>
</section>""".strip()

    template_text = TEMPLATE.read_text(encoding="utf-8")
    head = template_text.split("<body>", 1)[0]
    head = head.replace("{{文档标题}}", TITLE)
    head = head.replace("{{作者}}", "Luciole Studio")
    head = head.replace("{{摘要}}", f"{TITLE}：{SUBTITLE}。检验拿破仑胜利之后的欧洲秩序可能性的反事实史研究。")
    head = head.replace("{{关键词}}", "拿破仑, 反事实史, 欧洲秩序, 海军史, 帝国治理")
    head = head.replace("</style>", UTILITY_CSS + "\n</style>")
    # 模板的 @font-face 写的是 ../fonts/（kami 仓库布局）；本工作区字体在
    # typeset/fonts/，与 HTML 同级。本机即使不改也能出粗体（fontconfig 会按全名
    # 命中 ~/Library/Fonts 里的 W05，模板另有 jsDelivr 兜底），但那是在借环境的力：
    # 换一台没装该字体又断网的机器就会静默丢粗体。改成本地可解析，构建才自足。
    head = head.replace('url("../fonts/', 'url("fonts/')
    if 'url("../fonts/' in head:
        raise RuntimeError("font path rewrite failed")

    html_text = (head + "<body>\n" + cover + "\n" + toc + "\n"
                 + "\n".join(sections_html) + "\n" + "\n".join(note_html) + "\n"
                 + colophon + "\n</body>\n</html>\n")

    # 回填注释序号占位
    def fill(match: re.Match) -> str:
        return str(note_numbers[match.group(1)])

    html_text = re.sub(r"@@([^@]+)@@", fill, html_text)
    if "{{" in html_text or "@@" in html_text:
        raise RuntimeError("placeholder residue in output")
    HTML_OUT.write_text(html_text, encoding="utf-8")

    subprocess.run(
        [str(WEASYPRINT), "--dpi", "300", "--pdf-tags", "--quiet",
         str(HTML_OUT), str(PDF_OUT)],
        check=True, cwd=WS,
    )

    doc = fitz.open(PDF_OUT)
    report = {
        "title": TITLE,
        "html": str(HTML_OUT),
        "pdf": str(PDF_OUT),
        "pdf_pages": doc.page_count,
        "pdf_bytes": PDF_OUT.stat().st_size,
        "han_characters": han,
        "chapters": len(chapters),
        "h2_sections": sum(r.get("h2", 0) for r in chapter_reports),
        "h3_sections": sum(r.get("h3", 0) for r in chapter_reports),
        "tables": sum(r["tables"] for r in chapter_reports),
        "table_rows": sum(r["table_rows"] for r in chapter_reports),
        "paragraphs": sum(r["paragraphs"] for r in chapter_reports),
        "notes": len(ordered_keys),
        "note_calls": sum(len(v) for v in NOTE_CALLS.values()),
        "toc_entries": len(toc_rows),
        "chapter_reports": chapter_reports,
    }
    REPORT_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    r = build()
    print(json.dumps({k: v for k, v in r.items() if k != "chapter_reports"},
                     ensure_ascii=False, indent=2))
