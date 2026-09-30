#!/bin/bash
# SP2 card: download source-strategy books named in card contract
PY=/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/runtime/python/bin/python
SCRIPT="/Users/makiko/.misaka/state/tasks/t_27c409/.skills-ro/annas-archive/scripts/annas.py"
OUT=/Users/makiko/Documents/exam/downloads
dl() {
  echo "=== $2 ($3)"
  "$PY" "$SCRIPT" download-book "$1" --title "$2" --format "$3" --outdir "$OUT" 2>&1 | tail -3
}
dl 01cd60c2f24cc07fd30fc019fc480470 "SP2_Tone_Fatal_Knot" epub
dl 0ce763fec93d106d9ce50d385d77946b "SP2_Esdaile_Fighting_Napoleon" pdf
dl 9ee10514803d7c9f835412496570bc31 "SP2_Fraser_Cursed_War" epub
dl fe68c4ce7f6e00066fb65b20ee5a43df "SP2_Lawrence_First_Carlist_War" pdf
dl 324203e0811fc8278b78bcb7a6ec14ac "SP2_Fontana_Quiebra" pdf
dl 821420f2996465971196a9c29a0df8fb "SP2_Portillo_Crisis_Atlantica" pdf
dl ee4f570e810e478bf90c8c05185f269b "SP2_Hamnett_Politica_Espanola" pdf
dl 3f8901fcebdb83bf70f552d87f6f068b "SP2_Callahan_Church" pdf
dl d271505b095f23cc93d38774061c47f6 "SP2_Esdaile_Peninsular_War" epub
