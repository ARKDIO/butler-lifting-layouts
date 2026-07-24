#!/usr/bin/env python3
"""Assemble agent part files into index.html: replace each section's v1..v5 and inject CSS."""
import re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(ROOT, 'index.html')
PARTS = os.path.join(ROOT, 'parts')
FILES = ['AB.html', 'CDE.html', 'FGH.html', 'IJKL.html']

def parse(fn):
    txt = open(os.path.join(PARTS, fn)).read()
    css = ''
    m = re.search(r'<<<CSS>>>(.*?)<<<END CSS>>>', txt, re.S)
    if m: css = m.group(1).strip()
    secs = {}
    for sm in re.finditer(r'<<<SEC ([A-L])>>>(.*?)<<<END SEC \1>>>', txt, re.S):
        secs[sm.group(1)] = sm.group(2).strip()
    return css, secs

def main():
    s = open(IDX).read()
    all_css = []
    all_secs = {}
    for fn in FILES:
        p = os.path.join(PARTS, fn)
        if not os.path.exists(p):
            print('MISSING', fn); sys.exit(1)
        css, secs = parse(fn)
        if css: all_css.append(f'/* ==== {fn} ==== */\n' + css)
        all_secs.update(secs)

    # replace each section's v1..v5 region (from first `<div class="variant vv v1">` to `</section>`)
    for label, block in all_secs.items():
        pat = re.compile(
            r'(<section class="sec" id="sec' + label + r'".*?<div class="variant vv v0 active">.*?</div>\s*)'
            r'(<div class="variant vv v1">.*?)(\n</section>)', re.S)
        def repl(mm):
            return mm.group(1) + block.strip() + mm.group(3)
        s2, n = pat.subn(repl, s)
        if n != 1:
            print(f'WARN section {label}: replaced {n} (expected 1)')
        s = s2

    # inject CSS before </style>
    css_join = '\n'.join(all_css)
    s = s.replace('</style>', '\n/* ===== AGENT VARIANT CSS ===== */\n' + css_join + '\n</style>', 1)

    open(IDX, 'w').write(s)
    print('assembled. sections:', sorted(all_secs.keys()), 'css blocks:', len(all_css))

if __name__ == '__main__':
    main()
