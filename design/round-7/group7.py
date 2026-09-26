"""Group page r7 by topic: onboarding together, every Home together, marketing together, and so on.

Only positions, board titles, the section titles and the two notes change. No board file changes, nothing is removed,
and other pages are untouched. Round 8's copies keep their files and gain " (Round 8)" in their titles, so Ian can
see which idea each screen comes from once they sit next to Round 7's.

Usage:
  python3 design/round-7/group7.py <live canvas.json> <out canvas.json>
Read the live canvas.json first, then publish the output on its own."""
import json
import sys

src, out = sys.argv[1:3]
c = json.load(open(src))
B, N = c['boards'], c['notes']

# Sections top to bottom. Each is a title and its rows; a row is a list of board names without ".dc.html".
GROUPS = [
    ('Foundations, brand and the app\'s structure', [
        ['R7-Type', 'R7-Foundations', 'R7-Brand', 'R7-Icons', 'R7-Motion'],
        ['R7-R8-Hub-Icons', 'R7-R8-IA']]),
    ('Onboarding: welcome, sign in, the first profile, the first step, coming back', [
        ['R7-Entry', 'R7-Welcome', 'R7-Auth-Signin', 'R7-Auth-Code', 'R7-Auth-Profile', 'R7-Auth-Consent', 'R7-Goals',
         'R7-Starter', 'R7-Reveal', 'R7-FirstStep', 'R7-Auth-Notify', 'R7-Auth-Lock', 'R7-Auth-Back']]),
    ('Home in every version, goals, and the hard moments', [
        ['R7-Home', 'R7-R8-Home', 'R7-Biz-Home', 'R7-R8-Goals', 'R7-Hard']]),
    ('Learn: the tab, lessons, topics, words and Ask', [
        ['R7-Learn', 'R7-R8-Learn', 'R7-Lesson', 'R7-R8-Topic-Shares', 'R7-Vault', 'R7-R8-Words-Decoder', 'R7-Ask']]),
    ('Learn: real stories, the AWO Podcast and companies explained', [
        ['R7-R8-Story', 'R7-R8-Podcast', 'R7-R8-Mistake', 'R7-R8-Companies', 'R7-R8-Company-Brief', 'R7-R8-Startup']]),
    ('The Hub and its tools, for a job', [
        ['R7-R8-Tool-Skeleton', 'R7-R8-Hub', 'R7-R8-Tool-Payslip', 'R7-R8-Tool-Payday', 'R7-R8-Tool-Debt',
         'R7-R8-Tool-Fees', 'R7-R8-Tool-Statement', 'R7-Simulator', 'R7-Offer']]),
    ('Business: the profile, the check, the Hub, the tools and Shop', [
        ['R7-Biz-Profile', 'R7-Biz-Check', 'R7-R8-Hub-Biz', 'R7-R8-Tool-Price', 'R7-R8-Tool-Invoice',
         'R7-R8-Shop-Edit', 'R7-R8-Shop-Public']]),
    ('Community: the tab, the buddy, the feed and posting', [
        ['R7-Community', 'R7-Buddy', 'R7-R8-Feed-Parts', 'R7-R8-Feed', 'R7-R8-Compose', 'R7-R8-Post']]),
    ('Me: the profile, progress, the check-in, the report and settings', [
        ['R7-Me', 'R7-Progress', 'R7-Checkin', 'R7-Compare', 'R7-Report', 'R7-Settings']]),
    ('Components and widgets', [
        ['R7-Components', 'R7-Data', 'R7-Widgets']]),
    ('AWO Admin (desktop)', [
        ['R7-Admin-Overview', 'R7-Admin-Approvals', 'R7-Admin-Scoring', 'R7-Admin-Members'],
        ['R7-Admin-Moderation', 'R7-Admin-Content', 'R7-Admin-Audit']]),
    ('Marketing: store screenshots', [
        [f'R7-Store-{i}' for i in range(1, 9)],
        [f'R7-R8-Store-{i}' for i in range(1, 9)]]),
    ('Marketing: listing, feature graphic, icon and device hero', [
        ['R7-Listing', 'R7-Feature-Graphic', 'R7-App-Icon', 'R7-Hero-Device'],
        ['R7-R8-Listing', 'R7-R8-Feature-Graphic', 'R7-R8-Hero-Device']]),
    ('Marketing: ads', [
        ['R7-Ad-Diva', 'R7-Ad-Photo', 'R7-Ad-Pool', 'R7-Ad-Word', 'R7-Ad-Story'],
        ['R7-R8-Ad-Diva', 'R7-R8-Ad-Payslip', 'R7-R8-Ad-Goals', 'R7-R8-Ad-Words', 'R7-R8-Ad-Shop', 'R7-R8-Ad-Explained', 'R7-R8-Ad-Podcast']]),
]
GAP, ROW_GAP, GROUP_GAP, TITLE = 80, 200, 400, 300

r7 = {k for k, v in B.items() if v.get('page') == 'r7'}
placed = [b + '.dc.html' for _, rows in GROUPS for row in rows for b in row]
missing, extra = sorted(r7 - set(placed)), sorted(set(placed) - r7)
dupes = sorted({f for f in placed if placed.count(f) > 1})
if missing or extra or dupes:
    sys.exit(f'not placed: {missing}; not on r7: {extra}; placed twice: {dupes}')

# The old section titles and the Round 8 note go; the new titles replace them.
for k in [k for k, v in N.items() if v.get('page') == 'r7' and k not in ('r7howto', 'r7mkt')]:
    del N[k]

y = -TITLE  # the first section's boards start at y 0, beside the how-to note
for i, (text, rows) in enumerate(GROUPS, 1):
    by, widest = y + TITLE, 0
    for r, row in enumerate(rows):
        x, bottom = 0, by
        for b in row:
            e = B[b + '.dc.html']
            e.update(x=x, y=by)
            if b.startswith('R7-R8-') and not e.get('title', '').endswith('(Round 8)'):
                e['title'] = (e.get('title') or b[6:]) + ' (Round 8)'
            x += e['w'] + GAP
            bottom = max(bottom, by + e['h'])
        widest = max(widest, x - GAP)
        if text.startswith('Marketing: store') and r == 0:
            N['r7mkt'].update(x=x, y=by)
        by = bottom + ROW_GAP
    N[f'r7g{i:02d}'] = {'kind': 'title1', 'page': 'r7', 'w': 240, 'x': 0, 'y': y, 'maxW': min(8000, widest), 'text': text}
    y = by - ROW_GAP + GROUP_GAP

# The canvas lists boards in this order, so the list follows the sections too. Other pages keep their slots.
slots = [i for i, k in enumerate(c['order']) if k in r7]
rest = [k for k in (c['order'][i] for i in slots) if k not in placed]
for i, k in zip(slots, [f for f in placed if f in c['order']] + rest):
    c['order'][i] = k

sections = '\n'.join(f'{i}. {t}' for i, (t, _) in enumerate(GROUPS, 1))
N['r7howto'].update(x=-480, y=0, text=(
    "Round 7: the full board, for UI and UX reference, grouped by topic.\n\n"
    f"{sections}\n\n"
    "Round 7's screens and Round 8's ideas sit side by side in each section. A title ending in (Round 8) marks a "
    "Round 8 screen, copied from that page and linked to the other copies; the Round 8 page itself is unchanged.\n\n"
    "Geist does all the type. A handwritten face (Kalam by default; switch it in any board's Tweaks) appears only at a "
    "few special moments: someone's own words, or AWO's short note at a real milestone. Never on numbers, buttons, "
    "results or anything AI writes. Corners come in three sizes (6, 10, 14) and a circle.\n\n"
    "All content is sample content."))
N['r7mkt']['text'] = (
    "How the marketing is made\n\n"
    "Every screenshot is a 2x capture of a live screen, so nothing starts stale: the top row from Round 7's screens, "
    "the row under it from Round 8's. Change a screen, recapture it, and the store boards follow.\n\n"
    "Corners scale with the canvas: 14 at phone width becomes 40 on a 1080 canvas.\n\n"
    "The hand appears only in a member's own words.\n\n"
    "PNG exports are in design/marketing/round-7 and round-8. Store copy and the app name are still open (Q-31); "
    "every number is a sample.")

json.dump(c, open(out, 'w'), ensure_ascii=False)
print(f'{len(placed)} boards in {len(GROUPS)} sections; the last ends at y {y - GROUP_GAP}')
