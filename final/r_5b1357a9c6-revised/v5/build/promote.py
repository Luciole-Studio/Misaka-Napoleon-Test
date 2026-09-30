#!/usr/bin/env python3
"""把 v5/drafts 中的章节文件清理后写入 v5/chapters（定稿库）。
清理：注释里指向内部规划文件、旧版快照路径、会话暂存目录的字样，改成读者可用的出处；正文不改。
用法：python3 promote.py [文件名 ...]   （缺省处理全部 NN_*.md，交稿说明除外）"""
import re, sys
from pathlib import Path
V5 = Path(__file__).resolve().parents[1]
SRC, DST = V5 / "drafts", V5 / "chapters"
OLD = {"00_导论": "旧版《导论》", "01_法国的能力与代价": "旧版第一章", "02a_英国海权与和平_国家财政与社会": "旧版第二章",
       "02b_英国海权与和平_舰队海峡与帝国": "旧版第三章", "03_大陆诸国": "旧版第四章", "04_西班牙与意大利": "旧版第五章",
       "05_大西洋与美洲": "旧版第六章", "06_东方与印度": "旧版第七章", "07_行省化的边界": "旧版第八章",
       "08_新秩序的经济与社会": "旧版第九章", "09_另一条十九世纪": "旧版第十章", "10_资料附编": "旧版资料附编"}
AUD = r"`?(?:final/)?(?:r_5b1357a9c6-revised/)?audit/20260925_复审与修缮/"
RULES = [
    (re.compile(AUD + r"P2_三轨道设定\.md`?"), "本书资料附编第一节"),
    (re.compile(AUD + r"P0_修缮总规划\.md`?(?:第三节之4|第三节第4条)?"), "本书引言第二节"),
    (re.compile(AUD + r"E_上帝视角可行性锚点\.md`?"), "本书资料附编第三节"),
    (re.compile(r"审计报告A5（" + AUD + r"A5_外交互动_材料与书稿\.md`?）(?:第\d节第\d条)?"), "编写时的外交材料清点"),
    (re.compile(AUD + r"[A-Z]\d?_[^`）；。\s]*\.md`?"), "编写时的复审记录"),
    (re.compile(r"证据包E项(\d+)"), r"资料附编第三节项\1"),
]
NEW = {"00_引言": "本书引言", "01_法国": "本书第一章", "02_英国": "本书第二章", "03_海军与帝国": "本书第三章",
       "04_东方大国档案": "本书第四章", "05_中欧大国档案": "本书第五章", "06_德意志与北方档案": "本书第六章",
       "07_伊比利亚与意大利档案": "本书第七章", "08_外交博弈上": "本书第八章", "09_外交博弈下": "本书第九章",
       "10_行省化机器与管道": "本书第十章", "11_行省化逐地区推演": "本书第十一章", "12_行省化三轨道与总判": "本书第十二章",
       "13_上帝视角": "本书第十三章", "14_美洲": "本书第十四章", "15_东方与印度": "本书第十五章", "16_经济与社会": "本书第十六章",
       "17_世界年表": "本书第十七章", "18_资料附编": "本书资料附编"}
SNAP_PAREN = re.compile(r"（快照[^）]*）")
PATH_PREFIX = re.compile(r"（?(?:final/)?r_5b1357a9c6-revised-backup-20260926-003436/chapters/）?")
V5_PREFIX = re.compile(r"（?v5草稿\s*")
FILE_NAME = re.compile(r"`?(\d\d[ab]?_[^\s`）。；，、:：]+?)\.md`?")
SNAP_FILE = re.compile(r"快照(?:本)?\s*`?(?:final/)?(?:r_5b1357a9c6-revised-backup-20260926-003436/)?(?:chapters/)?(\d\d[ab]?_[^`\s）]*?)\.md`?")


def clean(text: str) -> tuple[str, int]:
    n = 0
    for pat, rep in RULES:
        text, k = pat.subn(rep, text); n += k
    text, k = SNAP_PAREN.subn("", text); n += k
    text, k = SNAP_FILE.subn(lambda m: OLD.get(m.group(1), "旧版书稿"), text); n += k
    text = text.replace("旧版书稿以快照为准：", "旧版书稿：").replace("旧书稿快照", "旧书稿")
    text = text.replace("旧书稿旧版", "旧版").replace("旧版书稿：旧版", "旧版书稿").replace("旧版书稿旧版", "旧版")
    text, k = PATH_PREFIX.subn("", text); n += k
    text, k = V5_PREFIX.subn("", text); n += k
    def fname(m):
        stem = m.group(1)
        return OLD.get(stem) or NEW.get(stem) or m.group(0)
    text, k = FILE_NAME.subn(fname, text); n += k
    return text, n


def main():
    names = sys.argv[1:] or [p.name for p in sorted(SRC.glob("*.md")) if re.match(r"^\d\d_", p.name) and "交稿说明" not in p.name]
    DST.mkdir(exist_ok=True)
    for name in names:
        raw = (SRC / name).read_text(encoding="utf-8")
        out, n = clean(raw)
        leftovers = re.findall(r"audit/|scratchpad|backup-20260926|快照为准|旧书稿快照|(?<!downloads/pages/)[0-9a-f]{0}\d\d[ab]?_[^\s`）。；，]+?\.md", out)
        (DST / name).write_text(out, encoding="utf-8")
        print(f"{name}: {n} replacements; leftovers {len(leftovers)}")


if __name__ == "__main__":
    main()
