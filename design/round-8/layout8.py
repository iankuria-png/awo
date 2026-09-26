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
    'R8-Hub': 'Hub: Naledi, employed (Me; her business tab is empty)', 'R8-Hub-Biz': 'Hub: Wanjiru, a market stall (My business)',
    'R8-Tool-Skeleton': 'One skeleton for every tool', 'R8-Home': 'Home, with several goals and the Hub', 'R8-Goals': 'Goals studio (pick a template, make it a goal)',
    'R8-Tool-Payslip': 'Payslip decoder (tick the lines, tap a part)', 'R8-Tool-Payday': 'Pay-day plan, family included (use + and -)',
    'R8-Tool-Debt': 'Debt payoff (drag, switch strategy)', 'R8-Tool-Fees': 'Fee eater (drag the fee)', 'R8-Tool-Statement': 'Statement insights (consent, reading, results)',
    'R8-Tool-Price': 'Price it right (drag the margin)', 'R8-Tool-Invoice': 'Quotes and invoices (turn the quote into an invoice)',
    'R8-Shop-Edit': 'Shop: the editor (publish it)', 'R8-Shop-Public': 'Shop: what a buyer sees (order a vase)',
    'R8-Story': 'A Rise story (listen, save, react)', 'R8-Podcast': 'The AWO Podcast (play, chapters, transcript, key lessons)',
    'R8-Mistake': 'My worst money mistake (tell it, choose how it shows)', 'R8-Feed-Parts': 'The feed, in parts',
    'R8-Feed': 'Community: the feed (react, read a letter, report, Circles)', 'R8-Compose': 'New post (try the AI check, then a milestone)',
    'R8-Post': 'A question with replies (reply, report a reply)',
    'R8-Companies': 'Companies explained: the path (and AWO\'s editorial rules)', 'R8-Company-Brief': 'A company brief (tap the revenue split)',
    'R8-Startup': 'How a startup raises money (step through the rounds)',
    **{f'R8-Store-{i}': f'Store screenshot {i}' for i in range(1, 9)},
    'R8-Listing': 'Store listing, Round 8', 'R8-Feature-Graphic': 'Feature graphic, 1024 by 500', 'R8-Hero-Device': 'Device hero',
    'R8-Ad-Diva': 'Square ad: the DIVA score', 'R8-Ad-Payslip': 'Square ad: the payslip', 'R8-Ad-Goals': 'Square ad: goals', 'R8-Ad-Words': 'Square ad: words',
    'R8-Ad-Shop': 'Square ad: shop local', 'R8-Ad-Explained': 'Square ad: explained, never sold', 'R8-Ad-Podcast': 'Story ad: the podcast',
}

ROWS = [
    ('r8title1', "The Hub's icon: three directions, and the pick", ['R8-Hub-Icons']),
    ('r8title2', 'The new IA, and Learn with three tabs', ['R8-IA', 'R8-Learn', 'R8-Topic-Shares', 'R8-Words-Decoder']),
    ('r8title3', 'The Hub in two modes, Home and goals', ['R8-Tool-Skeleton', 'R8-Hub', 'R8-Hub-Biz', 'R8-Home', 'R8-Goals']),
    ('r8title4', 'Hub tools for Me', ['R8-Tool-Payslip', 'R8-Tool-Payday', 'R8-Tool-Debt', 'R8-Tool-Fees', 'R8-Tool-Statement']),
    ('r8title5', 'Hub tools for My business, and Shop', ['R8-Tool-Price', 'R8-Tool-Invoice', 'R8-Shop-Edit', 'R8-Shop-Public']),
    ('r8title6', 'Real stories and the AWO Podcast, in Learn', ['R8-Story', 'R8-Podcast', 'R8-Mistake']),
    ('r8title7', 'Community as a feed to read and post in', ['R8-Feed-Parts', 'R8-Feed', 'R8-Compose', 'R8-Post']),
    ('r8title8', 'Companies explained, in Learn', ['R8-Companies', 'R8-Company-Brief', 'R8-Startup']),
    ('r8title9', 'Marketing in the Round 8 IA: store screenshots', [f'R8-Store-{i}' for i in range(1, 9)]),
    ('r8title10', 'Marketing: listing, feature graphic, device hero', ['R8-Listing', 'R8-Feature-Graphic', 'R8-Hero-Device']),
    ('r8title11', 'Marketing: ads', ['R8-Ad-Diva', 'R8-Ad-Payslip', 'R8-Ad-Goals', 'R8-Ad-Words', 'R8-Ad-Shop', 'R8-Ad-Explained', 'R8-Ad-Podcast']),
]

HOWTO = ("Round 8: Learn with Words and Stories, the Hub at the centre, goals of every kind, real stories and a feed (D-037, D-038).\n\n"
         "Same language as Round 7: Geist, Kalam for rare moments, corners 6, 10 and 14 and a circle.\n\n"
         "Top row: the Hub's icon in three directions. Ian picked the keystone, in lime (D-039). Choosing the Hub plays its move once.\n\n"
         "Next row: the new IA and tab bar, then Learn with three tabs (Paths, Words, Stories) and its animated switch, a topic page and the buzzword decoder.\n\n"
         "Then the Hub: the tool skeleton, the Hub for Naledi (employed) and Wanjiru (a market stall), Home with several goals, and the goals studio. "
         "Below it, nine tools on the same six beats, each linked from the Hub.\n\n"
         "Then real stories (a Rise story, the AWO Podcast, My worst money mistake) and Community as a feed: its parts, the feed, the composer and a thread.\n\n"
         "Last: Companies explained (the path, a company brief and a startup explainer), and the marketing refreshed for the Round 8 IA.\n\n"
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
        entry = {'x': x, 'y': by, 'w': w, 'h': h, 'page': PAGE, 'title': TITLES.get(b) or old.get('title') or b[3:]}
        if not b.startswith(('R8-Store', 'R8-Listing', 'R8-Feature', 'R8-Hero', 'R8-Ad-')):
            entry['is_interactive'] = True
        B[f] = entry
        if f not in c['order']:
            c['order'].append(f)
        x += w + 80
        bottom = max(bottom, by + h)
    N[key]['maxW'] = max(1200, min(8000, x - 80))
    y = bottom + 300

json.dump(c, open(out, 'w'), ensure_ascii=False)
print('laid out; last row ends at', y - 300)
