"""Copy every Round 8 board onto canvas page r7, so Round 7 is one full board with all of Ian's ideas.

Round 7's own boards and notes are never moved or changed, and page r8 stays as it is. Each copy is named
R7-R8-<name>, and its links point at the other copies. The copies sit below Round 7's last row, keeping Round 8's
own arrangement and section titles, under one heading and a note.

Usage:
  python3 design/round-8/round8.py <gen dir>        # build Round 8 as published
  python3 design/round-7/pull8.py <live canvas.json> <gen dir> <out dir>
  python3 design/round-7/group7.py <out dir>/project/canvas.json <out dir>/project/canvas.json
Then publish <out dir>/project/canvas.json with the R7-R8-*.dc.html files. Read the live canvas.json first.
group7.py puts the copies back into the board's topic sections and drops the heading and note added here."""
import json
import os
import sys

src, gen, out = sys.argv[1:4]
c = json.load(open(src))
B, N = c['boards'], c['notes']
proj = os.path.join(out, 'project')
os.makedirs(proj, exist_ok=True)
r8 = {k: v for k, v in B.items() if v.get('page') == 'r8'}

for k in r8:
    html = open(os.path.join(gen, k)).read().replace('href="R8-', 'href="R7-R8-')
    open(os.path.join(proj, 'R7-R8-' + k[3:]), 'w').write(html)

r7_bottom = max(v['y'] + v['h'] for k, v in B.items() if v.get('page') == 'r7' and not k.startswith('R7-R8-'))
head_y = r7_bottom + 700
off = head_y + 500  # Round 8's first title sits at y 0, its boards at 300
for k, v in r8.items():
    e = dict(v, page='r7', y=v['y'] + off)
    B['R7-R8-' + k[3:]] = e
    if 'R7-R8-' + k[3:] not in c['order']:
        c['order'].append('R7-R8-' + k[3:])
for k, v in list(N.items()):
    if v.get('page') == 'r8' and v.get('kind') == 'title1':
        N['r7x' + k[2:]] = dict(v, page='r7', y=v['y'] + off)
N['r7x-head'] = {'kind': 'title1', 'page': 'r7', 'w': 240, 'x': 0, 'y': head_y, 'maxW': 8000,
                 'text': 'Round 8 ideas: the Hub, Learn with Words and Stories, goals of every kind, real stories and the feed'}
N['r7x-note'] = {'fill': 'gray', 'page': 'r7', 'w': 400, 'x': -480, 'y': off, 'text': (
    "Round 8, pulled into the full board.\n\n"
    "Everything from here down is Round 8, copied in unchanged and linked between the copies: the Hub's icon, the new tabs "
    "(Home, Learn, Hub, Community, Me), Learn with Paths, Words and Stories, the Hub for a job and for a business with nine tools, "
    "goals of every kind, real stories and the AWO Podcast, Community as a feed, Companies explained, and Round 8's marketing.\n\n"
    "Everything above is Round 7, untouched. The Round 8 page is still there as it was.\n\n"
    "The Round 8 brief and research are in docs/00-discovery/14-round-8.md. All content is sample content.")}
json.dump(c, open(os.path.join(proj, 'canvas.json'), 'w'), ensure_ascii=False)
print(f'{len(r8)} boards copied; the Round 8 block starts at y {head_y}')
