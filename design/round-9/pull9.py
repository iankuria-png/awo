"""Copy every Round 9 board onto page r7 as R7-R9-<name>, so the Round 7 board keeps every idea, then let
design/round-7/group7.py put each copy in its topic section.

Links are rewritten so the copies point at each other and at the Round 8 copies: href="R9-..." becomes
href="R7-R9-..." and href="R8-..." becomes href="R7-R8-...". Round 7's own boards keep their links.
The same rewrite (to_r7) refreshes R7-R8 copies of Round 8 boards that link to Round 9.

Usage:
  python3 design/round-9/pull9.py <canvas.json with page r9 laid out> <folder of R9 boards> <out dir> [R8 board ...]
Then run group7.py on <out dir>/project/canvas.json and publish it with the copies."""
import json
import os
import sys


def to_r7(html):
    return html.replace('href="R9-', 'href="R7-R9-').replace('href="R8-', 'href="R7-R8-')


if __name__ == '__main__':
    src, gen, out = sys.argv[1:4]
    r8_boards = sys.argv[4:]
    c = json.load(open(src))
    B = c['boards']
    proj = os.path.join(out, 'project')
    os.makedirs(proj, exist_ok=True)
    r9 = {k: v for k, v in B.items() if v.get('page') == 'r9'}
    for k, v in r9.items():
        open(os.path.join(proj, 'R7-R9-' + k[3:]), 'w').write(to_r7(open(os.path.join(gen, k)).read()))
        copy = 'R7-R9-' + k[3:]
        old = B.get(copy, {})
        B[copy] = dict(v, page='r7', x=old.get('x', 0), y=old.get('y', 0))
        if copy not in c['order']:
            c['order'].append(copy)
    for name in r8_boards:  # Round 8 boards that now link to Round 9
        open(os.path.join(proj, 'R7-R8-' + name[3:] + '.dc.html'), 'w').write(to_r7(open(os.path.join(gen, name + '.dc.html')).read()))
    json.dump(c, open(os.path.join(proj, 'canvas.json'), 'w'), ensure_ascii=False)
    print(f'{len(r9)} Round 9 boards copied to r7; {len(r8_boards)} Round 8 copies refreshed')
