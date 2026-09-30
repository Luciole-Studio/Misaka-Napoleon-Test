#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P2笔记08：第十一章合稿脚本。

把分段稿 P2_notes_稿01—07 连成正文，按首次出现的顺序给〔区…〕注重新编号，
把注释中"见注X/按注X"的交叉引用改成新编号，写出 11_行省化逐地区推演.md，
并打印注的数目与汉字数。改动任何分段稿或 P2_notes_稿99_注释.md 以后重跑即可。

用法：python3 P2_notes_08_合稿脚本.py
"""
import os, re, sys
D=os.path.dirname(os.path.abspath(__file__))+'/'
parts=['P2_notes_稿01_开篇与读法.md','P2_notes_稿02_内圈.md','P2_notes_稿03_小单位.md','P2_notes_稿04_北海德西.md','P2_notes_稿05_南方东南.md','P2_notes_稿06_假想区.md','P2_notes_稿07_总表与模型.md']
body='\n\n'.join(open(D+p,encoding='utf-8').read().strip('\n') for p in parts)+'\n'
notes_raw=open(D+'P2_notes_稿99_注释.md',encoding='utf-8').read()
# parse notes
entries={}
order_in_file=[]
for m in re.finditer(r'^〔区([^〕]+)〕(.*?)(?=^\s*〔区|\Z)', notes_raw, flags=re.S|re.M):
    lab=m.group(1); txt=m.group(2).strip()
    if lab in entries: print('DUP NOTE',lab); 
    entries[lab]=txt; order_in_file.append(lab)
labels=[]
for m in re.finditer(r'〔区([^〕]+)〕', body):
    if m.group(1) not in labels: labels.append(m.group(1))
missing=[l for l in labels if l not in entries]
unused=[l for l in order_in_file if l not in labels]
print('body labels',len(labels),'notes',len(entries),'missing',missing,'unused',unused)
if missing: sys.exit(1)
mp={old:str(i+1) for i,old in enumerate(labels)}
body2=re.sub(r'〔区([^〕]+)〕', lambda m:'〔区'+mp[m.group(1)]+'〕', body)
def fixref(t):
    return re.sub(r'(见|按)注([0-9]+|[a-c][0-9]+)', lambda m: m.group(1)+'注'+mp.get(m.group(2),'??'+m.group(2)), t)
out=[body2.rstrip('\n'),'','### 本章注释','']
for old in labels:
    out.append('〔区'+mp[old]+'〕'+fixref(entries[old]))
    out.append('')
final='\n'.join(out).rstrip('\n')+'\n'
assert '??' not in final, 'unresolved cross-ref'
open(D+'11_行省化逐地区推演.md','w',encoding='utf-8').write(final)
cjk=len(re.findall(r'[一-鿿]',final))
bcjk=len(re.findall(r'[一-鿿]',body2))
print('written; total CJK',cjk,'body CJK',bcjk,'nonspace',len(re.sub(r'\s','',final)),'notes',len(labels))
