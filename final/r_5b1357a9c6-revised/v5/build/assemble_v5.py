#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第五版组装：v5/chapters/*.md -> 完整稿（Markdown，pandoc 脚注）＋阅读版HTML＋校验报告。

用法：python3 assemble_v5.py [--src chapters|drafts]
- 章节文件按文件名排序；每章一级标题形如「# 第N章　标题」或「# 引言　…」「# 资料附编　…」。
- 章内脚注写作〔前缀n〕，章末「### 本章注释」下逐条以〔前缀n〕开头；本脚本转成 [^前缀n]。
- 只读章节文件；写出 v5/ 下的完整稿、阅读版与 build/assemble_report.json。
"""
from __future__ import annotations
import collections, hashlib, json, re, subprocess, sys
from pathlib import Path

V5 = Path(__file__).resolve().parents[1]
BOOK = V5.parent
SRC = V5 / ("drafts" if "--src" in sys.argv and "drafts" in sys.argv else "chapters")
OUT_MD = V5 / "胜利之后的欧洲_第五版_完整稿.md"
OUT_HTML = V5 / "胜利之后的欧洲_第五版_阅读版.html"
REPORT = V5 / "build" / "assemble_report.json"
STYLE = BOOK / "audit" / "book_style.html"
INTER = BOOK / "audit" / "book_interactions.html"
NOTE_HEAD = re.compile(r"^#{2,3} (?:引言注释|本章注释|本编引文与资料|本编引文与数据出处|本章文献说明|资料附编注释)\s*\n", re.M)
LABEL = r"[一-鿿]+\d+"


RUN = re.compile(rf"(?:〔{LABEL}(?:、{LABEL})*〕)+")
DEF_LINE = re.compile(rf"^〔({LABEL})〕(?!\s*(?:〔{LABEL}(?:、{LABEL})*〕\s*)*$)")
# 旧版书稿独有的注释前缀：在第五版里不存在，一律按旧版引用处理
OLD_ONLY = {"统", "省", "英政", "英财", "英贸", "英市", "补", "法海", "海技", "欧", "南", "美补", "帝"}


def protect_nested(text: str) -> str:
    """注释定义行内再出现的〔标签〕：
    - 指向旧版书稿的（前文20字内有"旧"或"快照"）改成纯文字"注X"，不参与编号，避免误指新版同名注释；
    - 其余改成［标签］，组装时换成全书编号"注N"。"""
    out = []
    for line in text.split("\n"):
        m = DEF_LINE.match(line)
        if m:
            head, rest = line[:m.end()], line[m.end():]
            def sub(mm: re.Match) -> str:
                labels = re.findall(LABEL, mm.group(0))
                before = rest[max(0, mm.start() - 20):mm.start()]
                old_only = all(re.match(r"^([^\d]+)", lab).group(1) in OLD_ONLY for lab in labels)
                if "旧" in before or "快照" in before or old_only:
                    return ("" if before.endswith("注") else "注") + "、".join(labels)
                return "［" + "、".join(labels) + "］"
            line = head + RUN.sub(sub, rest)
        out.append(line)
    return "\n".join(out)


def convert(text: str) -> str:
    text = protect_nested(text)
    text = NOTE_HEAD.sub("", text)
    text = re.sub(rf"^〔({LABEL})〕(?!\s*(?:〔{LABEL}(?:、{LABEL})*〕\s*)*$)\s*", lambda m: f"[^{m[1]}]: ", text, flags=re.M)
    text = re.sub(rf"〔({LABEL}(?:、{LABEL})*)〕", lambda m: "".join(f"[^{v}]" for v in m[1].split("、")), text)
    return text


def number_nested(text: str) -> tuple[str, list[str]]:
    """把［标签］换成 pandoc 的脚注序号（按正文首次引用顺序），返回未能解析的标签。"""
    order: dict[str, int] = {}
    for m in re.finditer(r"\[\^([^\]]+)\](?!:)", text):
        order.setdefault(m.group(1), len(order) + 1)
    bad: list[str] = []
    def sub(m: re.Match) -> str:
        labels = m.group(1).split("、")
        nums = []
        for lab in labels:
            if lab in order:
                nums.append(str(order[lab]))
            else:
                bad.append(lab); nums.append(lab)
        return "注" + "、".join(nums)
    return re.sub(rf"注?［({LABEL}(?:、{LABEL})*)］", sub, text), bad


def main() -> None:
    files = sorted(p for p in SRC.glob("*.md") if not p.name.endswith("_交稿说明.md") and re.match(r"^\d\d_", p.name))
    if not files:
        sys.exit(f"no chapter files in {SRC}")
    parts, per_file = [], []
    for p in files:
        raw = p.read_text(encoding="utf-8")
        h1 = re.findall(r"^# (.+)$", raw, re.M)
        if len(h1) != 1:
            sys.exit(f"{p.name}: expected exactly one H1, found {len(h1)}")
        conv = convert(raw).strip()
        per_file.append({"file": p.name, "h1": h1[0], "han": len(re.findall(r"[一-鿿]", conv))})
        parts.append(conv)
    text = "\n\n".join(parts) + "\n"
    defs = re.findall(r"^\[\^([^\]]+)\]:", text, re.M)
    refs = re.findall(r"\[\^([^\]]+)\](?!:)", text)
    missing = sorted(set(refs) - set(defs))
    _, unresolved_nested = number_nested(text)
    dups = [k for k, v in collections.Counter(defs).items() if v > 1]
    unused = sorted(set(defs) - set(refs))
    # 表格列数检查
    errors, inside, cols = [], False, None
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("|"):
            c = len(re.split(r"(?<!\\)\|", line)) - 2
            if not inside:
                cols = c
            elif c != cols:
                errors.append([n, cols, c])
            inside = True
        else:
            inside = False
    meta = '---\ntitle: "胜利之后的欧洲"\nsubtitle: "拿破仑的另一条道路，1803—1848"\nlang: zh-CN\ndate: "2026年9月 第五版"\n---\n\n'
    OUT_MD.write_text(meta + text, encoding="utf-8")
    report = {"source_dir": str(SRC), "files": per_file, "han_total": sum(f["han"] for f in per_file),
              "note_definitions": len(defs), "note_calls": len(refs), "missing_notes": missing,
              "duplicate_notes": dups, "unused_notes": unused, "table_column_errors": errors[:50],
              "unresolved_nested_refs": sorted(set(unresolved_nested)),
              "markdown_sha256": hashlib.sha256(OUT_MD.read_bytes()).hexdigest()}
    ok = not missing and not dups and not errors and not unresolved_nested
    if ok and "--html" in sys.argv:
        tmp_md = V5 / "build" / "_pandoc_input.md"
        tmp_md.write_text(meta + number_nested(text)[0], encoding="utf-8")
        subprocess.run(["/opt/homebrew/bin/pandoc", str(tmp_md), "--standalone", "--toc", "--toc-depth=2",
                        "--section-divs", "--metadata", "toc-title=全书目录", "--include-in-header", str(STYLE),
                        "--include-after-body", str(INTER), "-o", str(OUT_HTML)], check=True)
        html = OUT_HTML.read_text(encoding="utf-8")
        html = re.sub(r"<table\b([^>]*)>", r'<div class="table-scroll" tabindex="0" role="region" aria-label="数据表，可横向滚动"><table\1>', html).replace("</table>", "</table></div>")
        OUT_HTML.write_text(html, encoding="utf-8")
        report["html"] = str(OUT_HTML)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "files"}, ensure_ascii=False, indent=2))
    for f in per_file:
        print(f"{f['file']}: {f['han']} 汉字")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
