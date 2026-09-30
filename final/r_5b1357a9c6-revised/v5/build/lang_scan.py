#!/usr/bin/env python3
"""扫描用户不希望出现的句式：对比否定、不下结论、元叙述。只扫正文（章末注释之前）。"""
import re, sys
from pathlib import Path
PAT = [
 ("对比否定", r"不是[^。；]{0,60}而是|并非[^。；]{0,60}而是|与其说[^。]{0,60}不如说|不在于[^。]{0,60}而在于|不是[^。；]{0,40}，[^。；]{0,4}是"),
 ("否定判断", r"(?:这|它|那)(?:并)?不是|并不是|绝不是|也不是"),
 ("不等于类", r"不等于|并不意味着|不意味着|不代表|并不说明|不能说明"),
 ("不下结论", r"无法给出|无法判断|难以判断|不能断言|尚不能|没有足够(?:依据|证据)|不足以证明|不能证明|无从判断|尚待证实"),
 ("不宜不应", r"不宜|不应把|不应当把|不冒充|不能把|不可把"),
 ("元叙述", r"本书不|这里需要说明|必须区分|必须分开"),
]
files = [Path(a) for a in sys.argv[1:]]
tot = 0
for f in files:
    s = f.read_text(encoding="utf-8")
    body = re.split(r"^### 本章注释", s, flags=re.M)[0]
    for n, line in enumerate(body.splitlines(), 1):
        for name, p in PAT:
            for m in re.finditer(p, line):
                tot += 1
                a = max(0, m.start() - 25); b = min(len(line), m.end() + 25)
                print(f"{f.name}:{n}:{name}: …{line[a:b]}…")
print("TOTAL", tot)
