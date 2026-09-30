p="/Users/makiko/Documents/exam/downloads/pages/5dea3a848dc0.md"
t=open(p,encoding="utf-8",errors="replace").read()
print("chars",len(t))
out="/Users/makiko/Documents/exam/nodes/r_5b1357a9c6/cards/t_27c409/esdaile_spanisharmy_folded.txt"
lines=[]
for para in t.split("\n"):
    while len(para)>240:
        cut=para.rfind(" ",0,240)
        if cut<80: cut=240
        lines.append(para[:cut]); para=para[cut:].lstrip()
    lines.append(para)
open(out,"w",encoding="utf-8").write("\n".join(lines))
print("folded lines",len(lines))
for kw in ["Contents","Bailen","levies","conscription","guerrilla","provincial militia","Introduction"]:
    i=t.lower().find(kw.lower())
    print(kw,i)
