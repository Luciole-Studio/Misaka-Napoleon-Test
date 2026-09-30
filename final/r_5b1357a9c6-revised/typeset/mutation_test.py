#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""变异测试：全绿的检查套件可能只是恒真。

往 build_book.py 的副本里植入 8 个已知缺陷，各自在沙箱重建 + 复检，
verify_book.py 必须对每一个都报 FAIL（退出码 1）。逃逸即说明该维度未被守住。

否定用例取值刻意贴近正例（对抗性取值），而不是随手挑个明显不同的值：
例如页码只错 1 页、稀疏阈值只降一档、注释只丢 1 条。
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

WS = Path(__file__).resolve().parent
PY = "/opt/homebrew/bin/python3"

MUTATIONS = [
    # (名称, 目标文件, 原文, 替换, 预期被哪一维度抓住)
    # 变异体必须让 verify 面对一个"构建成功但有缺陷"的成品；
    # 若变异导致 build 崩溃，就只证明了构建脆弱，没证明 verify 守得住。
    ("丢失最后 1 条注释（构建成功，仅成品少一条）", "build_book.py",
     '    note_html.append("</section>")',
     '    note_html.pop()\n    note_html.append("</section>")',
     "注释条目数 / 编号连续"),

    ("页眉黏连主副标题（回归上一轮已修缺陷）", "build_book.py",
     "    string-set: none;\n  }\n  .chapter h1 .title-main {\n    display: block;\n    string-set: section-title content();\n  }",
     "    string-set: section-title content();\n  }\n  .chapter h1 .title-main {\n    display: block;\n  }",
     "页眉未把主副标题黏连"),

    ("版本说明页沿用前章页眉", "build_book.py",
     "  .colophon h2 { string-set: section-title content(); }",
     "  .colophon h2 { }",
     "版本说明页页眉未沿用前章"),

    ("正文越出右版心 6pt", "build_book.py",
     "  .table-wrap { margin: 12pt 0 14pt; break-inside: auto; }",
     "  .table-wrap { margin: 12pt 0 14pt; break-inside: auto; width: 103%; }",
     "无内容越出版心"),

    ("目录页码停用实算（退回占位）", "build_book.py",
     "  .toc-page::after { content: target-counter(attr(data-href), page); }",
     "  .toc-page::after { content: \"—\"; }",
     "目录页码已实算"),

    ("丢弃 1 张表格", "build_book.py",
     '        out.append(rendered)\n            stats["tables"] += 1',
     '        out.append(rendered if stats["tables"] else "")\n            stats["tables"] += 1',
     "表格数"),

    ("正文改用系统黑体（字体兜底）", "build_book.py",
     '  body { font-size: 10.2pt; line-height: 1.62; letter-spacing: 0.25pt; }',
     '  body { font-size: 10.2pt; line-height: 1.62; letter-spacing: 0.25pt;\n         font-family: "Songti SC", serif; }',
     "汉字全部由仓耳今楷承载"),

    ("章间不分页（制造异常稀疏/串页）", "build_book.py",
     "  .chapter { break-before: page; }",
     "  .chapter { break-before: avoid; }",
     "章首页/页眉相关"),

    # 本轮实弹：@font-face 路径错会让两个字重一起失效，正文仍是仓耳今楷、
    # 「无 sans 兜底」照样通过，只有粗体静默消失。变异绕开构建期守卫、
    # 只让成品退化，才能证明 verify 自己守得住这一维度。
    ("@font-face 指向不存在的目录（粗体静默消失）", "build_book.py",
     '    head = head.replace(\'url("../fonts/\', \'url("fonts/\')',
     '    head = head.replace(\'url("../fonts/\', \'url("absent-fonts/\')',
     "粗体由 W05 实际承载"),
]


def run(sandbox: Path) -> tuple[int, str]:
    build = subprocess.run([PY, "build_book.py"], cwd=sandbox,
                           capture_output=True, text=True)
    if build.returncode != 0:
        return 1, "BUILD-FAILED: " + (build.stderr or build.stdout)[-300:]
    verify = subprocess.run([PY, "verify_book.py"], cwd=sandbox,
                            capture_output=True, text=True)
    return verify.returncode, verify.stdout


def prepare(sandbox: Path) -> None:
    for name in ("build_book.py", "verify_book.py"):
        shutil.copy2(WS / name, sandbox / name)
    (sandbox / "fonts").mkdir(exist_ok=True)
    for f in (WS / "fonts").glob("*.ttf"):
        target = sandbox / "fonts" / f.name
        if not target.exists():
            target.symlink_to(f)
    # build_book.py 以 WS.parent 定位源稿；沙箱的 parent 是系统临时目录，
    # 必须把源稿链过去，否则连基线都构建不起来。
    source = WS.parent / "胜利之后的欧洲_完整修订稿.md"
    link = sandbox.parent / source.name
    if not link.exists():
        link.symlink_to(source)


def main() -> int:
    print("=== 基线：未变异的副本必须全绿 ===")
    escaped = []
    with tempfile.TemporaryDirectory(prefix="hermes-mutation-base-") as tmp:
        sandbox = Path(tmp)
        prepare(sandbox)
        code, out = run(sandbox)
        fails = re.findall(r"\[FAIL\] (.+)", out)
        print(f"  基线退出码={code}，FAIL={len(fails)}")
        if code != 0:
            print("  基线就不绿，变异测试无意义：")
            print(out[-1500:])
            return 1

    print("\n=== 变异体 ===")
    for idx, (name, target, old, new, expect) in enumerate(MUTATIONS, 1):
        with tempfile.TemporaryDirectory(prefix=f"hermes-mutation-{idx}-") as tmp:
            sandbox = Path(tmp)
            prepare(sandbox)
            path = sandbox / target
            text = path.read_text(encoding="utf-8")
            if old not in text:
                print(f"  [SKIP] {idx}. {name} — 锚点未命中，变异未植入（测试本身失效）")
                escaped.append(name + "（锚点未命中）")
                continue
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
            code, out = run(sandbox)
            fails = re.findall(r"\[FAIL\] (.+)", out)
            if out.startswith("BUILD-FAILED"):
                # 构建崩溃只证明构建脆弱，不证明 verify 守得住这一维度。
                print(f"  [无效] {idx}. {name} — 变异使构建崩溃，未验证 verify：{out[:80]}")
                escaped.append(name + "（构建崩溃，未验证 verify）")
            elif code == 0:
                print(f"  [逃逸] {idx}. {name} — 套件仍全绿，未守住「{expect}」")
                escaped.append(name)
            else:
                first = fails[0][:60] if fails else out.strip().splitlines()[-1][:60]
                print(f"  [捕获] {idx}. {name} — {len(fails)} 项 FAIL，首条：{first}")

    print("\n" + "=" * 56)
    if escaped:
        print(f"变异测试：{len(escaped)}/{len(MUTATIONS)} 个变异体逃逸")
        for e in escaped:
            print("  - " + e)
        return 1
    print(f"变异测试：{len(MUTATIONS)}/{len(MUTATIONS)} 个变异体全部被捕获")
    return 0


if __name__ == "__main__":
    sys.exit(main())
