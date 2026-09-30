import subprocess, os
DL="/Users/makiko/Documents/exam/downloads/SP2_Callahan_Church__abea90f07578.pdf"
OUT="/Users/makiko/Documents/exam/nodes/r_5b1357a9c6/cards/t_27c409/texts/callahan_church.txt"
r=subprocess.run(["pdftotext","-layout",DL,"-"],capture_output=True,timeout=600)
t=r.stdout.decode("utf-8",errors="replace")
if len(t)<10000:
    import pymupdf
    doc=pymupdf.open(DL); t="\n".join(f"\n===== PAGE {i+1} =====\n"+p.get_text() for i,p in enumerate(doc))
lines=[]
for para in t.split("\n"):
    para=para.rstrip()
    while len(para)>230:
        cut=para.rfind(" ",0,230)
        if cut<60: cut=230
        lines.append(para[:cut]); para=para[cut:].lstrip()
    lines.append(para)
open(OUT,"w",encoding="utf-8").write("\n".join(lines))
print(OUT,len(t),"chars",len(lines),"lines")
