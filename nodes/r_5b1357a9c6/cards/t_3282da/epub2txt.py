import sys, zipfile, re, html
from pathlib import Path

def epub_to_text(epub_path, out_path):
    z = zipfile.ZipFile(epub_path)
    # find spine order via container/opf
    names = z.namelist()
    opf = [n for n in names if n.endswith('.opf')]
    order = []
    if opf:
        opf_data = z.read(opf[0]).decode('utf-8', 'ignore')
        base = opf[0].rsplit('/', 1)[0] + '/' if '/' in opf[0] else ''
        ids = {}
        for m in re.finditer(r'<item[^>]+id="([^"]+)"[^>]+href="([^"]+)"[^>]*>', opf_data):
            ids[m.group(1)] = base + m.group(2)
        for m in re.finditer(r'<itemref[^>]+idref="([^"]+)"', opf_data):
            if m.group(1) in ids:
                order.append(ids[m.group(1)])
    if not order:
        order = [n for n in names if n.endswith(('.html', '.xhtml', '.htm'))]
    out = []
    for name in order:
        try:
            data = z.read(name).decode('utf-8', 'ignore')
        except KeyError:
            continue
        data = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', data, flags=re.S)
        data = re.sub(r'<br[^>]*>', '\n', data)
        data = re.sub(r'</(p|div|h[1-6]|li|tr|blockquote)>', '\n', data)
        data = re.sub(r'<[^>]+>', '', data)
        data = html.unescape(data)
        data = re.sub(r'[ \t]+', ' ', data)
        data = re.sub(r'\n\s*\n+', '\n\n', data)
        out.append(f"\n===== FILE: {name} =====\n" + data.strip())
    Path(out_path).write_text('\n'.join(out), encoding='utf-8')
    print(out_path, 'chars:', sum(len(x) for x in out))

if __name__ == '__main__':
    epub_to_text(sys.argv[1], sys.argv[2])
