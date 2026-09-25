"""Lay out canvas page r8 row by row. Usage: python3 layout8.py <live canvas.json> <out canvas.json> <folder of .dc.html boards>
Read the live canvas.json with the Artifact tool first, so the editor's changes are kept.
Rows are listed top to bottom; boards that don't exist in the folder yet are skipped. Adds page r8 if missing
and makes the canvas open on it."""
import json
import os
import re
import sys

src, out, proj = sys.argv[1:4]
c = json.load(open(src))
B, N = c['boards'], c['notes']
PAGE = 'r8'

if not any(p['id'] == PAGE for p in c.get('pages', [])):
    c.setdefault('pages', []).append({'id': PAGE, 'name': 'Round 8'})
c['launch'] = {'view': 'canvas', 'page': PAGE}

TITLES = {  # board file: title shown on canvas
    'R8-Hub-Icons': "The Hub's icon: keystone (picked), dial or awning (tap the tab bars)",
    'R8-IA': 'Five tabs, one new centre (tap the tab bar)',
    'R8-Learn': 'Learn: Paths, Words and Stories (switch tabs)',
    'R8-Topic-Shares': 'A topic: shares and dividends (step through the bakery)',
    'R8-Words-Decoder': 'Words: the buzzword decoder (type, or try Rug pull and Staking)',
}

ROWS = [
    ('r8title1', "The Hub's icon: three directions, and the pick", ['R8-Hub-Icons']),
    ('r8title2', 'The new IA, and Learn with three tabs', ['R8-IA', 'R8-Learn', 'R8-Topic-Shares', 'R8-Words-Decoder']),
]

HOWTO = ("Round 8: Learn with Words and Stories, the Hub at the centre, goals of every kind, real stories and a feed (D-037, D-038).\n\n"
         "Same language as Round 7: Geist, Kalam for rare moments, corners 6, 10 and 14 and a circle.\n\n"
         "Top row: the Hub's icon in three directions. Ian picked the keystone, in lime (D-039). Choosing the Hub plays its move once.\n\n"
         "Next row: the new IA and tab bar, then Learn with three tabs (Paths, Words, Stories) and its animated switch, a topic page and the buzzword decoder.\n\n"
         "The brief, the research and the ranked Hub tools are in docs/00-discovery/14-round-8.md.\n\n"
         "All content is sample content.")


def size(name):
    """Width and height from the board's own $preview."""
    s = open(os.path.join(proj, name + '.dc.html')).read()
    m = re.search(r'"\$preview"\s*:\s*\{\s*"width"\s*:\s*(\d+)\s*,\s*"height"\s*:\s*(\d+)', s.replace('&quot;', '"'))
    return int(m.group(1)), int(m.group(2))


N.setdefault('r8howto', {'fill': 'gray', 'page': PAGE, 'w': 400, 'x': -480, 'y': 0})
N['r8howto']['text'] = HOWTO
y = 0
for key, text, boards in ROWS:
    present = [b for b in boards if os.path.exists(os.path.join(proj, b + '.dc.html'))]
    if not present:
        continue
    N.setdefault(key, {'kind': 'title1', 'page': PAGE, 'w': 240})
    N[key].update({'text': text, 'x': 0, 'y': y})
    by = y + 300
    x, bottom = 0, by
    for b in present:
        w, h = size(b)
        f = b + '.dc.html'
        old = B.get(f, {})
        entry = {'x': x, 'y': by, 'w': w, 'h': h, 'page': PAGE, 'title': TITLES.get(b) or old.get('title') or b[3:], 'is_interactive': True}
        B[f] = entry
        if f not in c['order']:
            c['order'].append(f)
        x += w + 80
        bottom = max(bottom, by + h)
    N[key]['maxW'] = max(1200, min(8000, x - 80))
    y = bottom + 300

json.dump(c, open(out, 'w'), ensure_ascii=False)
print('laid out; last row ends at', y - 300)
