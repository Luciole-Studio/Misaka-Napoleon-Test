from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
w=Path(__file__).parent
files=sorted(w.glob('page-*.png'))
for st in range(0,len(files),16):
 sheet=Image.new('RGB',(1400,2080),'#d0d0d0');d=ImageDraw.Draw(sheet)
 for i,p in enumerate(files[st:st+16]):
  im=Image.open(p).convert('RGB');im.thumbnail((340,480));x=(i%4)*350+(350-im.width)//2;y=(i//4)*520+24;sheet.paste(im,(x,y));d.text(((i%4)*350+12,(i//4)*520+6),f'Page {st+i+1}',fill='black')
 sheet.save(w/f'contact-{st//16+1}.png')
