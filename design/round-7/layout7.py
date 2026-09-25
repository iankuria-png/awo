"""Lay out canvas page r7 row by row. Usage: python3 layout7.py <live canvas.json> <out canvas.json> <folder of .dc.html boards>
Read the live canvas.json with the Artifact tool first, so the editor's changes are kept.
Rows are listed top to bottom; boards that don't exist in root/project yet are skipped."""
import json
import os
import re
import sys

src, out, proj = sys.argv[1:4]
c = json.load(open(src))
B, N = c['boards'], c['notes']

TITLES = {  # board file: title shown on canvas
    'R7-Type': None, 'R7-Foundations': 'Foundations: colour, shapes, people, space', 'R7-Brand': 'Brand: app icon A and the wordmark in Geist',
    'R7-Icons': 'Icons', 'R7-Motion': 'Motion, M1 to M6 (every card works)',
    'R7-Entry': 'Welcome, photo-led (the front door)', 'R7-Auth-Signin': 'Sign in: phone first, or Google and Apple (type a number, change the country)',
    'R7-Auth-Code': 'The code (type 123456)', 'R7-Auth-Profile': 'About you: name, where you live, currency', 'R7-Auth-Consent': 'Your data, in plain words (consent)',
    'R7-Goals': 'What brings you here (tap to pick)', 'R7-Starter': None, 'R7-Reveal': 'Your first profile: the result reveal',
    'R7-FirstStep': 'Choose your first step', 'R7-Auth-Notify': 'Reminders, asked for after the first step', 'R7-Auth-Lock': 'Keep AWO private: a PIN (enter it twice)',
    'R7-Auth-Back': 'Welcome back (PIN 2580, or the fingerprint)',
    'R7-Welcome': 'Welcome, three slides', 'R7-Home': None, 'R7-Learn': 'Learn', 'R7-Ask': None, 'R7-Vault': None, 'R7-Community': None, 'R7-Me': None,
    'R7-Progress': 'Your progress (tap a stone)',
    'R7-Lesson': 'Lesson player: story cards, Ola, a quick check, done (tap through)', 'R7-Compare': 'Compare two versions (pick from and to)',
    'R7-Simulator': 'What if: safety net runway and a loan\'s real cost (drag)', 'R7-Offer': 'Check an offer: AI against the red-flag list (tap check)',
    'R7-Report': 'DIVA report, one printable page (A4)',
    'R7-Admin-Overview': 'Admin overview: needs you first (filter it, press Search or jump to)', 'R7-Admin-Approvals': 'Approvals: two people, a diff and checks (approve, or ask for changes)',
    'R7-Admin-Scoring': 'Scoring draft and its impact on test profiles (run the preview)', 'R7-Admin-Members': 'Members, private by default (reveal needs a reason)',
    'R7-Admin-Moderation': 'Moderation: AI flags, people decide (keep, hide, remove)', 'R7-Admin-Content': 'Lessons and Vault: draft, review, publish', 'R7-Admin-Audit': 'Audit log and AI log',
    'R7-Biz-Profile': 'Your business: a two-minute profile', 'R7-Biz-Check': 'Business check (sample questions; answer all four)', 'R7-Biz-Home': 'Home, business view (add today\'s numbers)', 'R7-Hard': 'Hard moments: day one, a late check-in, coming back, a month down, offline', 'R7-Checkin': '30-day check-in (drag, answer, finish)', 'R7-Buddy': 'Your buddy (cheer, then reply)', 'R7-Settings': 'Settings (the switches work)',
}

ROWS = [
    ('r7title0', 'Foundations and brand', 'fixed'),
    ('r7title7', 'Accounts and the first loop', ['R7-Entry', 'R7-Auth-Signin', 'R7-Auth-Code', 'R7-Auth-Profile', 'R7-Auth-Consent', 'R7-Goals', 'R7-Starter', 'R7-Reveal', 'R7-FirstStep', 'R7-Auth-Notify', 'R7-Auth-Lock', 'R7-Auth-Back']),
    ('r7title1', 'The app: the five areas, Ask, and inside them', ['R7-Welcome', 'R7-Home', 'R7-Learn', 'R7-Ask', 'R7-Vault', 'R7-Community', 'R7-Me', 'R7-Progress', 'R7-Checkin', 'R7-Buddy', 'R7-Settings']),
    ('r7title8', 'Learning and the loop, deeper', ['R7-Lesson', 'R7-Compare', 'R7-Simulator', 'R7-Offer', 'R7-Report', 'R7-Hard']),
    ('r7title9', 'Entrepreneurs', ['R7-Biz-Profile', 'R7-Biz-Check', 'R7-Biz-Home']),
    ('r7title3', 'Components and widgets', ['R7-Components', 'R7-Data', 'R7-Widgets']),
    ('r7title10', 'AWO Admin (desktop)', ['R7-Admin-Overview', 'R7-Admin-Approvals', 'R7-Admin-Scoring', 'R7-Admin-Members', 'R7-Admin-Moderation', 'R7-Admin-Content', 'R7-Admin-Audit']),
    ('r7title4', 'Marketing in Geist: store screenshots, from the live screens', [f'R7-Store-{i}' for i in range(1, 9)]),
    ('r7title5', 'Marketing: listing, feature graphic, icon, device hero', ['R7-Listing', 'R7-Feature-Graphic', 'R7-App-Icon', 'R7-Hero-Device']),
    ('r7title6', 'Marketing: campaign ads', ['R7-Ad-Photo', 'R7-Ad-Pool', 'R7-Ad-Word', 'R7-Ad-Story']),
]


def size(name):
    """Width and height from the board's own $preview."""
    s = open(os.path.join(proj, name + '.dc.html')).read()
    m = re.search(r'"\$preview"\s*:\s*\{\s*"width"\s*:\s*(\d+)\s*,\s*"height"\s*:\s*(\d+)', s.replace('&quot;', '"'))
    return int(m.group(1)), int(m.group(2))


y = 0
for key, text, boards in ROWS:
    if boards == 'fixed':
        # The top row keeps its hand-set positions; find its bottom.
        bottom = max(v['y'] + v['h'] for k, v in B.items() if v.get('page') == 'r7' and k[:-8] in ('R7-Type', 'R7-Foundations', 'R7-Brand', 'R7-Icons', 'R7-Motion'))
        y = bottom + 300
        continue
    present = [b for b in boards if os.path.exists(os.path.join(proj, b + '.dc.html'))]
    if not present:
        continue
    N.setdefault(key, {'kind': 'title1', 'page': 'r7', 'w': 240})
    N[key].update({'text': text, 'x': 0, 'y': y})
    by = y + 300
    x, bottom = 0, by
    for b in present:
        w, h = size(b)
        f = b + '.dc.html'
        old = B.get(f, {})
        t = TITLES.get(b, 'keep')
        entry = {'x': x, 'y': by, 'w': w, 'h': h, 'page': 'r7', 'title': old.get('title') if (t is None or t == 'keep') and old.get('title') else (t if t not in (None, 'keep') else b[3:])}
        if not b.startswith(('R7-Store', 'R7-Listing', 'R7-Feature', 'R7-App-Icon', 'R7-Hero', 'R7-Ad-')):
            entry['is_interactive'] = True
        B[f] = entry
        if f not in c['order']:
            c['order'].append(f)
        x += w + 80
        bottom = max(bottom, by + h)
    N[key]['maxW'] = min(8000, x - 80)
    if key == 'r7title4' and 'r7mkt' in N:
        N['r7mkt'].update({'x': x + 80, 'y': by})
    y = bottom + 300

N.pop('r7title2', None)  # "Inside the areas" now shares the app row
json.dump(c, open(out, 'w'), ensure_ascii=False)
print('laid out; last row ends at', y - 300)
