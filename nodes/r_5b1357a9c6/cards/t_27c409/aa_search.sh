#!/bin/bash
# SP2 card: batch Anna's Archive searches (read-only member session searches)
PY=/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/runtime/python/bin/python
SCRIPT="/Users/makiko/.misaka/state/tasks/t_27c409/.skills-ro/annas-archive/scripts/annas.py"
run() {
  echo "=== $1"
  "$PY" "$SCRIPT" search-book "$1" 2>/dev/null | "$PY" -c '
import json,sys
try:
    d=json.load(sys.stdin)
except Exception as e:
    print("PARSE FAIL", e); sys.exit(0)
if d.get("status")!="ok":
    print("STATUS", d.get("status"), d.get("code")); sys.exit(0)
for r in d.get("results",[])[:5]:
    print(r["title"][:88],"|",r["authors"][:42],"|",r["language"][:12],r["format"],r["size"],"|",r["hash"])
'
}
run "Fraser Napoleon Cursed War Popular Resistance Spanish"
run "Fontana quiebra de la monarquia absoluta"
run "Mark Lawrence Spain First Carlist War"
run "Portillo Valdes Crisis atlantica monarquia hispana"
run "Esdaile Peninsular War New History"
run "Callahan Church Politics Society Spain"
run "Moreno Alonso Junta Suprema Sevilla"
run "Hamnett politica espanola epoca revolucionaria 1790"
