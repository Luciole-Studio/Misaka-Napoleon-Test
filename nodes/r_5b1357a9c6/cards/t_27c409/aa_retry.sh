#!/bin/bash
PY=/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/runtime/python/bin/python
SCRIPT="/Users/makiko/.misaka/state/tasks/t_27c409/.skills-ro/annas-archive/scripts/annas.py"
OUT=/Users/makiko/Documents/exam/downloads
"$PY" "$SCRIPT" download-book abea90f07578e868b9239eb7889cd2cf --title "SP2_Callahan_Church" --format pdf --outdir "$OUT" 2>&1 | tail -4
