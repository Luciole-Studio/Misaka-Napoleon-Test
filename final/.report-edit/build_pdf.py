from pathlib import Path
import json, re, subprocess, html, sys
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, CondPageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader, PdfWriter

ROOT=Path('/Users/makiko/Documents/exam/final')
WORK=ROOT/'.report-edit'
OUT=ROOT/'output/pdf'
SRC=ROOT/'r_b55f2c1cf5-report-polished.md'
PDF=OUT/'拿破仑反事实研究报告-学术润色版.pdf'
for name,path in [('CN','/System/Library/Fonts/STHeiti Light.ttc'),('CNBold','/System/Library/Fonts/STHeiti Medium.ttc'),('Unicode','/System/Library/Fonts/Supplemental/Arial Unicode.ttf')]:
    pdfmetrics.registerFont(TTFont(name,path))
pdfmetrics.registerFontFamily('CN',normal='CN',bold='CNBold',italic='CN',boldItalic='CNBold')
pdfmetrics.registerFontFamily('CNBold',normal='CNBold',bold='CNBold',italic='CNBold',boldItalic='CNBold')
INK=HexColor('#24313D'); ACCENT=HexColor('#215D70'); MUTED=HexColor('#536472'); LINE=HexColor('#CFDCE0'); TINT=HexColor('#F0F5F6')
PAGE_W,PAGE_H=A4
MARGIN=59
WIDTH=PAGE_W-2*MARGIN
styles={}
def style(name,**kw):
    base=dict(fontName='CN',fontSize=11,leading=18,textColor=INK,alignment=TA_LEFT,wordWrap='CJK',splitLongWords=True,spaceAfter=7,allowWidows=0,allowOrphans=0)
    base.update(kw); styles[name]=ParagraphStyle(name,**base);return styles[name]
style('body')
style('small',fontSize=9.5,leading=15,spaceAfter=6)
style('meta',fontSize=9.5,leading=16,textColor=MUTED,spaceAfter=7)
style('h2',fontName='CNBold',fontSize=20,leading=28,textColor=ACCENT,spaceBefore=14,spaceAfter=18,keepWithNext=True)
style('h3',fontName='CNBold',fontSize=13.2,leading=20,textColor=ACCENT,spaceBefore=13,spaceAfter=8,keepWithNext=True)
style('h4',fontName='CNBold',fontSize=11.5,leading=18,spaceBefore=10,spaceAfter=6,keepWithNext=True)
style('quote',fontSize=11,leading=19,leftIndent=13,borderColor=LINE,borderWidth=0.6,borderPadding=9,backColor=TINT,spaceBefore=4,spaceAfter=10)
style('list',leftIndent=15,firstLineIndent=0,bulletIndent=1,spaceAfter=6)
style('ref',fontSize=9.4,leading=15,leftIndent=10,firstLineIndent=-10,spaceAfter=8)
style('table',fontSize=9.5,leading=15,spaceAfter=0)
style('th',fontName='CNBold',fontSize=9.5,leading=15,textColor=ACCENT,spaceAfter=0)
style('cardtitle',fontName='CNBold',fontSize=10.8,leading=17,textColor=ACCENT,spaceBefore=8,spaceAfter=5,keepWithNext=True)
style('field',fontSize=10.3,leading=16.5,leftIndent=10,spaceAfter=4)
style('toc',fontSize=10.7,leading=17,spaceBefore=4,spaceAfter=3,rightIndent=24)
style('covertitle',fontName='CNBold',fontSize=30,leading=43,textColor=ACCENT,spaceAfter=20)
style('coversub',fontSize=16,leading=25,textColor=MUTED,spaceAfter=25)
style('covertext',fontSize=11.5,leading=21,spaceAfter=18)

seen_inline=set();seen_blocks=set()
def esc(s):
    s=html.escape(s)
    for ch in ('⁻','✓'):
        s=s.replace(ch,f'<font name="Unicode">{ch}</font>')
    return s

def inline(xs):
    out=[]
    for a in xs:
        t=a['t'];c=a.get('c');seen_inline.add(t)
        if t=='Str':out.append(esc(c))
        elif t in ('Space','SoftBreak'):out.append(' ')
        elif t=='LineBreak':out.append('<br/>')
        elif t=='Strong':out.append('<b>'+inline(c)+'</b>')
        elif t=='Emph':out.append('<i>'+inline(c)+'</i>')
        elif t=='Code':out.append('<font size="9.2" color="#4D5966">'+esc(c[1])+'</font>')
        elif t=='Link':
            url=c[2][0]
            content=inline(c[1])
            if url.startswith(('http:','https:','file:')):
                out.append('<link href="'+html.escape(url,quote=True)+'" color="#215D70">'+content+'</link>')
            else:out.append(content)
        elif t=='Quoted':out.append('“'+inline(c[1])+'”')
        elif t=='Span':out.append(inline(c[1]))
        elif t=='Superscript':out.append('<super>'+inline(c)+'</super>')
        elif t=='Subscript':out.append('<sub>'+inline(c)+'</sub>')
        elif t=='Math':out.append(esc(c[1]))
        elif t=='Note':out.append('（'+blocks_text(c)+'）')
        elif t=='RawInline':out.append(esc(c[1]))
        elif t=='Strikeout':out.append('<strike>'+inline(c)+'</strike>')
        else:raise ValueError(('Unhandled inline',t,a))
    return ''.join(out)

def blocks_text(blocks):
    out=[]
    for b in blocks:
        if b['t'] in ('Plain','Para'):out.append(inline(b['c']))
        elif b['t']=='LineBlock':out.extend(inline(x) for x in b['c'])
        else:raise ValueError(('Unhandled table/list block',b))
    return '<br/>'.join(out)

def plain(s):return html.unescape(re.sub('<[^>]*>','',s))

class Report(BaseDocTemplate):
    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        self.section=''; self.counter=0;self.heading_pages=[]
        frame=Frame(MARGIN,57,WIDTH,PAGE_H-113,id='body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id='report',frames=frame,onPage=self.paint))
    def beforeDocument(self):
        self.section='';self.counter=0;self.heading_pages=[]
        self.canv.setTitle('拿破仑自1803年起改变历史进程的可能路径｜学术润色版')
        self.canv.setAuthor('基于研究运行 r_b55f2c1cf5 的语言编辑版')
    def paint(self,canvas,doc):
        canvas.saveState()
        if doc.page>1:
            canvas.setStrokeColor(LINE);canvas.setLineWidth(.5)
            canvas.line(MARGIN,PAGE_H-36,PAGE_W-MARGIN,PAGE_H-36)
            canvas.setFillColor(MUTED);canvas.setFont('CN',8)
            canvas.drawString(MARGIN,PAGE_H-27,'拿破仑反事实研究 / 1803–1848')
            canvas.drawRightString(PAGE_W-MARGIN,PAGE_H-27,'学术润色版')
            canvas.drawString(MARGIN,32,'证据 • 路径 • 制度 • 来源')
            canvas.drawRightString(PAGE_W-MARGIN,32,str(doc.page))
        else:
            canvas.setFillColor(ACCENT);canvas.rect(MARGIN,PAGE_H-80,50,4,fill=1,stroke=0)
            canvas.setFillColor(MUTED);canvas.setFont('CN',9)
            canvas.drawString(MARGIN,39,'研究运行 r_b55f2c1cf5  /  语言编辑与阅读排版')
        canvas.restoreState()
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and hasattr(f,'navlevel'):
            level=f.navlevel;key=f.navkey;label=f.getPlainText()
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(label,key,level=level,closed=True)
            if level==0:
                self.section=label
                self.notify('TOCEntry',(0,label,self.page,key))
                self.heading_pages.append([label,self.page])

story=[]
def para(s,key='body',**kw):return Paragraph(s,styles[key],**kw)
def heading(s,level=0,key=None):
    p=para(s,('h2','h3','h4')[min(level,2)])
    p.navlevel=level;p.navkey=key or f'section-{len(story)}'
    return p

def table(b):
    c=b['c'];headers=c[3][1];rows=[]
    for body in c[4]: rows.extend(body[2]+body[3])
    rows.extend(c[5][1])
    def rowtext(row):return [blocks_text(cell[4]) for cell in row[1]]
    hs=rowtext(headers[0]) if headers else []
    rs=[rowtext(r) for r in rows]
    if not rs:return
    cols=len(rs[0]); assert all(len(r)==cols for r in rs)
    # Long narrative tables become stacked field records, retaining every cell.
    lengths=[len(plain(v)) for r in rs for v in r]
    if cols>=4 or max(lengths,default=0)>115 or (cols==3 and sum(lengths)/len(rs)>145):
        for row in rs:
            lead=(hs[0]+'：' if hs and plain(hs[0]) in ('路径','文件','数字') else '')+row[0]
            story.append(para(lead,'cardtitle'))
            for i,v in enumerate(row[1:],1):
                label=hs[i] if i<len(hs) else ''
                story.append(para(f'<b>{label}</b>　{v}' if label else v,'field'))
            story.append(Spacer(1,4))
        return
    data=[[para(x,'th') for x in hs]] if hs else []
    data.extend([[para(x,'table') for x in r] for r in rs])
    if cols==2: widths=[WIDTH*.51,WIDTH*.49]
    elif cols==3:
        # Text/data/reference tables need a wider explanatory column.
        avg=[sum(len(plain(r[j])) for r in rs)/len(rs) for j in range(cols)]
        if avg[1]<10 and avg[2]>15:widths=[WIDTH*.26,WIDTH*.16,WIDTH*.58]
        else:widths=[WIDTH*.34,WIDTH*.29,WIDTH*.37]
    else:widths=[WIDTH/cols]*cols
    t=Table(data,colWidths=widths,repeatRows=1 if hs else 0,hAlign='LEFT',splitByRow=1)
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('BACKGROUND',(0,0),(-1,0),TINT),('LINEBELOW',(0,0),(-1,0),.7,ACCENT),('LINEBELOW',(0,1),(-1,-1),.3,LINE)]))
    if t.wrap(WIDTH,700)[1] < 320:
        story.append(KeepTogether([t,Spacer(1,10)]))
    else:
        story.extend([t,Spacer(1,10)])

in_refs=False
chapter_num=0

def render(blocks,in_list=False):
    global in_refs,chapter_num
    for b in blocks:
        t=b['t'];c=b.get('c');seen_blocks.add(t)
        if t=='Header':
            level,attr,ins=c;txt=inline(ins)
            if level==1:continue
            if level==2:
                chapter_num+=1;in_refs=plain(txt).startswith('参考文献')
                story.append(CondPageBreak(460))
            navlevel=max(0,min(level-2,2))
            story.append(heading(txt,navlevel,key=f'h-{chapter_num}-{attr[0]}'))
        elif t in ('Plain','Para'):
            story.append(para(inline(c),'ref' if in_refs else 'body'))
        elif t=='HorizontalRule':pass
        elif t=='BlockQuote':
            text=blocks_text(c)
            story.append(KeepTogether([para(text,'quote')]))
        elif t in ('BulletList','OrderedList'):
            items=c if t=='BulletList' else c[1]
            start=1 if t=='BulletList' else c[0][0]
            for i,item in enumerate(items,start):
                bullet='•' if t=='BulletList' else f'{i}.'
                if all(x['t'] in ('Para','Plain') for x in item):
                    story.append(para(blocks_text(item),'ref' if in_refs else 'list',bulletText=None if in_refs else bullet))
                else:render(item,True)
        elif t=='Table':table(b)
        elif t=='CodeBlock':story.append(para(esc(c[1]).replace('\n','<br/>'),'small'))
        elif t=='Div':render(c[1])
        elif t=='LineBlock':story.append(para('<br/>'.join(inline(v) for v in c)))
        else:raise ValueError(('Unhandled block',t,b))

# A quiet cover introduces the central result; all source content follows.
story += [Spacer(1,85),para('拿破仑自1803年起<br/>改变历史进程的可能路径','covertitle'),para('基于证据约束的反事实研究报告','coversub'),Spacer(1,25),para('战争路径 / 欧洲秩序 / 海军与财政 / 区域政治','meta'),Spacer(1,20),para('现有材料尚未证成一条通向全欧控制与长期维持的完整路径。在已审路线中，受约束的法国优势秩序相对最有根据；其持续执行与继承期运行仍待验证。','covertext'),Spacer(1,25),para('证据基础：18张专题研究卡、1次独立红队审查、478项本地原材料。','meta'),para('本版仅编辑语言与版式，不新增史料核验；保留数值口径、证据限定、研究缺口、附录及来源索引。','meta'),PageBreak(),para('目录','h2')]
toc=TableOfContents();toc.levelStyles=[styles['toc']];toc.dotsMinLevel=0;story.append(toc)

ast=json.loads(subprocess.check_output(['/opt/homebrew/bin/pandoc','-f','markdown+pipe_tables+autolink_bare_uris-yaml_metadata_block-simple_tables-multiline_tables-smart','-t','json',str(SRC)]))
blocks=ast['blocks']
assert len([b for b in blocks if b['t']=='Header' and b['c'][0]==2]) == 21, 'Unexpected top-level heading count'
# Treat the subtitle and original metadata as front matter, not chapter headings.
first_chapter=next(i for i,b in enumerate(blocks) if b['t']=='Header' and b['c'][0]==2 and plain(inline(b['c'][2])).startswith('0.'))
metadata=[b for b in blocks[:first_chapter] if b['t'] not in ('Header','HorizontalRule')]
story.extend([PageBreak(),para('研究信息','h2')])
for b in metadata:
    if b['t'] in ('Para','Plain'):story.append(para(inline(b['c']),'meta'))
    else:render([b])
story.append(Spacer(1,16))
story.append(para('阅读导航','h3'))
story.append(para('先读第1节掌握综合判断；第2节比较战争路径；第3–10节分析秩序与区域问题；第11–15节列出竞争解释、方法限制与补证条件。附录与来源目录保留材料追溯信息。','body'))
story.append(para('PDF支持文字检索、章节书签和目录跳转。完整478项材料索引以原CSV附件保存在PDF中；外部网址与原报告的材料定位一并保留。','meta'))
render(blocks[first_chapter:])
raw=WORK/'rendered.pdf'
doc=Report(str(raw),pagesize=A4,leftMargin=MARGIN,rightMargin=MARGIN,topMargin=56,bottomMargin=57,pageCompression=1)
doc.multiBuild(story)
reader=PdfReader(raw)
writer=PdfWriter();writer.clone_document_from_reader(reader)
for f in [ROOT/'r_b55f2c1cf5-material-index.csv',SRC]:
    writer.add_attachment(f.name,f.read_bytes())
writer.add_metadata({'/Title':'拿破仑反事实研究报告｜学术润色版','/Subject':'语言润色与阅读排版；保留原报告证据与材料索引','/Author':'研究运行 r_b55f2c1cf5'})
with PDF.open('wb') as f:writer.write(f)
(WORK/'heading-pages.json').write_text(json.dumps(doc.heading_pages,ensure_ascii=False,indent=2))
(WORK/'render-statistics.json').write_text(json.dumps({'pages':len(reader.pages),'inline_types':sorted(seen_inline),'block_types':sorted(seen_blocks)},ensure_ascii=False,indent=2))
print(PDF);print('pages',len(reader.pages),'bytes',PDF.stat().st_size)
