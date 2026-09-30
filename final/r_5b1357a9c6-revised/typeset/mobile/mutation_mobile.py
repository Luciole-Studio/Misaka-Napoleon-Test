#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手机版变异测试：验证 verify_mobile.py 的手机专有断言不是恒真。

往 build_mobile.py 副本植入 8 个已知缺陷，各自在沙箱重建 + 复检，
verify_mobile.py 必须对每一个都报 FAIL。逃逸即说明该维度未被守住。

否定用例取对抗性取值（贴近正例的错），而非明显离谱的值：
开本只错一档（改 A4 / 改 16 开）、字号只降到临界线下、分档阈值只挪一列。
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
    ("开本退回 16 开（不再是手机视口）", "build_mobile.py",
     "    size: 155.22mm 337.34mm;\n    /* 左右 12mm",
     "    size: 185mm 260mm;\n    /* 左右 12mm",
     "竖排页尺寸 = 440x956"),

    ("宽表分档阈值挪到 ≥8 列（6、7 列被塞回竖排页）", "build_mobile.py",
     "    is_wide = len(header) >= 6",
     "    is_wide = len(header) >= 8",
     "表格按列数正确分档 / 越出版心"),

    ("宽表不再进横向页（去掉 page: landscape）", "build_mobile.py",
     "  .table-wrap.wide {\n    page: landscape;",
     "  .table-wrap.wide {\n    page: auto;",
     "宽表数 = 横向页数"),

    ("去掉转屏提示", "build_mobile.py",
     '        out.append(\'<div class="table-rotate-note">横向表 · 建议横屏查看</div>\')',
     '        pass',
     "每张宽表都带转屏提示"),

    ("正文字号降到 10.4pt（手机上偏吃力）", "build_mobile.py",
     "  body { font-size: 12.2pt; line-height: 1.78; letter-spacing: 0.2pt; }",
     "  body { font-size: 10.4pt; line-height: 1.78; letter-spacing: 0.2pt; }",
     "正文字号 ≥ 11pt / 行长区间"),

    ("边距压到 5mm（行变长、留白不足）", "build_mobile.py",
     "    margin: 12mm 12mm 11mm 12mm;",
     "    margin: 12mm 5mm 11mm 5mm;",
     "左右边距占页宽 6-8%"),

    ("丢失最后 1 条注释", "build_mobile.py",
     '    note_html.append("</section>")',
     '    note_html.pop()\n    note_html.append("</section>")',
     "注释条目数 / 编号连续"),

    ("@font-face 指向不存在的目录（粗体静默消失）", "build_mobile.py",
     '    head = head.replace(\'url("../fonts/\', \'url("fonts/\')',
     '    head = head.replace(\'url("../fonts/\', \'url("absent-fonts/\')',
     "粗体由 W05 实际承载"),
]


def run(sandbox: Path) -> tuple[int, str]:
    build = subprocess.run([PY, "build_mobile.py"], cwd=sandbox,
                           capture_output=True, text=True)
    if build.returncode != 0:
        return 1, "BUILD-FAILED: " + (build.stderr or build.stdout)[-300:]
    verify = subprocess.run([PY, "verify_mobile.py"], cwd=sandbox,
                            capture_output=True, text=True)
    return verify.returncode, verify.stdout


def prepare(sandbox: Path) -> None:
    for name in ("build_mobile.py", "verify_mobile.py"):
        shutil.copy2(WS / name, sandbox / name)
    (sandbox / "fonts").mkdir(exist_ok=True)
    for f in (WS / "fonts").resolve().glob("*.ttf"):
        target = sandbox / "fonts" / f.name
        if not target.exists():
            target.symlink_to(f)
    # build_mobile.py 以 WS.parent.parent 定位源稿；沙箱需要同构的两级父目录。
    source = WS.parent.parent / "胜利之后的欧洲_完整修订稿.md"
    link = sandbox.parent.parent / source.name
    if not link.exists():
        try:
            link.symlink_to(source)
        except OSError:
            pass


def main() -> int:
    print("=== 基线：未变异的副本必须全绿 ===")
    escaped = []
    with tempfile.TemporaryDirectory(prefix="hermes-mobmut-base-") as tmp:
        sandbox = Path(tmp) / "mobile"
        sandbox.mkdir()
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
        with tempfile.TemporaryDirectory(prefix=f"hermes-mobmut-{idx}-") as tmp:
            sandbox = Path(tmp) / "mobile"
            sandbox.mkdir()
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
                print(f"  [无效] {idx}. {name} — 构建崩溃，未验证 verify：{out[:90]}")
                escaped.append(name + "（构建崩溃）")
            elif code == 0:
                print(f"  [逃逸] {idx}. {name} — 套件仍全绿，未守住「{expect}」")
                escaped.append(name)
            else:
                first = fails[0][:58] if fails else out.strip().splitlines()[-1][:58]
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
