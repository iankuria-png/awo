"""Put every Round 9 board on the Round 7 board (page r7) as R7-R9-<name>. Round 9 has no page of its own (D-042):
its work belongs on the Round 7 board, beside the screens it changes. design/round-7/group7.py then puts each board
in its topic section.

Links are rewritten so the boards point at each other and at the Round 8 copies: href="R9-..." becomes
href="R7-R9-..." and href="R8-..." becomes href="R7-R8-...". Round 7's own boards keep their links.
The same rewrite (to_r7) refreshes R7-R8 copies of Round 8 boards that link to Round 9.

The first run also retired the old Round 9 page (its boards, notes and the page itself); its files stay in the
artifact, unused. The canvas opens on the Round 7 board.

Usage:
  python3 design/round-9/pull9.py <live canvas.json> <folder of built R9 boards> <out dir> [R8 board ...]
Then run group7.py on <out dir>/project/canvas.json and publish it with the boards that changed."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

TITLES = {  # board: title shown on the canvas (with what to try)
    'R9-Loop-Flow': 'The 30-day loop, end to end (tap a screen to open it)',
    'R9-Lock-Reminder': 'The reminder, on the lock screen (try Tonight, or Skip a month)',
    'R9-Notifications': 'Notifications (filter them, mark all read)',
    'R9-What-Changed': 'What changed: version 4 (try a month that went down)',
    'R9-Next-Step': "This month's step (pick one, start it)",
    'R9-Milestone': 'A milestone, and sharing it (try WhatsApp status)',
    'R9-Status-Milestone': 'WhatsApp status: a milestone (1080 by 1920)',
    'R9-Status-Word': 'WhatsApp status: the word of the week',
    'R9-Status-Story': 'WhatsApp status: a Rise story',
    'R9-Search': 'One search (type, filter, or try Stokvel)',
    'R9-Help': 'Help (pick a topic, open a question)',
    'R9-Help-Report': 'Report a problem (hide amounts in the screenshot, send)',
    'R9-Hub-All': 'All tools, by the job they do (Me, My business, everything)',
    'R9-Tool-Remit': 'Sending money home: the real cost (change the quotes)',
    'R9-Tool-Loan': "A loan's real cost, and explain my agreement (switch parts)",
    'R9-Tool-Offers': 'Two job offers (count the medical aid and the commute)',
    'R9-Tool-Pension': 'Retirement pulse (retire at, growth, add more)',
    'R9-Tool-Owe': 'What I own and owe (tick items, count the pension)',
    'R9-Tool-Worth': 'Is it worth it? A sewing machine (try the slow weeks)',
    'R9-Tool-Setup': 'Business setup checklist (Kenya or South Africa; tick steps)',
    'R9-Group-Book': 'Savings group book: a stokvel record (mark paid, remind, payout order)',
    'R9-Desktop-Home': 'Home, on a computer (1440 wide)',
    'R9-Desktop-Me': 'Your DIVA profile, on a computer',
    'R9-Tablet-Learn': 'Learn on a tablet: the path and the lesson side by side',
    'R9-WhatsApp-Checkin': 'The check-in on WhatsApp (Start, choose an amount, answer)',
    'R9-USSD': 'The check-in on USSD (press 1, answer with numbers, Send)',
    'R9-One-Question': 'One question, every channel',
    'R9-Comp-Overlays': 'Sheets, dialogs and toasts (all live)',
    'R9-Comp-Inputs': 'Dates, files, loading and two currencies (all live)',
    'R9-Empty-States': 'Empty states, from the five shapes',
    'R9-Email-Welcome': 'Welcome email (try halfway, and a dark mail app)',
    'R9-Email-Reminder': 'Check-in reminder email (scroll the phone)',
    'R9-Email-Summary': 'Monthly summary email',
    'R9-Flyer-A5': 'A5 flyer, front and back (three audiences; try the photocopier)',
    'R9-Workshop-Slides': 'Workshop slides, with speaker notes (use the arrows)',
    'R9-Place-Stall': 'At a market stall (try full sun)',
    'R9-Place-Commute': 'On a commute (try the Underground)',
    'R9-Place-Table': 'The printed report on a kitchen table (try the photocopier)',
    'R9-Place-Lock': 'The reminder on a lock screen (try a dark room)',
    'R9-Carousel-Diva': 'Carousel: the DIVA score, explained (1080 by 1350)',
    'R9-Carousel-Loan': 'Carousel: before you sign for a loan',
    'R9-Status-Question': "WhatsApp status: this week's question",
    'R9-Status-Quiz': 'WhatsApp status: a quick quiz',
    'R9-Podcast-Cover': 'The AWO Podcast: cover art, at every size',
    'R9-Podcast-Tiles': 'The AWO Podcast: episode tiles',
    'R9-Notebook': 'Money in and out: a notebook for traders (flip the pages; try blank)',
    'R9-Checkin-Magnet': 'The check-in on the fridge: a magnet and a printed year (tick a stone)',
    'R9-Stickers-Pins': 'Stickers and pins of the five shapes (try black nickel)',
    'R9-Tote': 'A tote bag (try the colours and the two prints)',
    'R9-Tshirts': 'Ambassador T-shirts and a name badge (try the colours)',
}
STATIC = ('R9-Status-', 'R9-Carousel-', 'R9-Podcast-')  # images, not interactive screens


def to_r7(html):
    return html.replace('href="R9-', 'href="R7-R9-').replace('href="R8-', 'href="R7-R8-')


def size(path):
    s = open(path).read().replace('&quot;', '"')
    m = re.search(r'"\$preview"\s*:\s*\{\s*"width"\s*:\s*(\d+)\s*,\s*"height"\s*:\s*(\d+)', s)
    return int(m.group(1)), int(m.group(2))


if __name__ == '__main__':
    src, gen, out = sys.argv[1:4]
    r8_boards = sys.argv[4:]
    import round9  # noqa: E402  (the list of Round 9 boards)
    c = json.load(open(src))
    B, N = c['boards'], c['notes']
    old = [k for k, v in B.items() if v.get('page') == 'r9']
    for k in old:
        del B[k]
    c['order'] = [k for k in c['order'] if k not in old]
    for k in [k for k, v in N.items() if v.get('page') == 'r9']:
        del N[k]
    c['pages'] = [p for p in c['pages'] if p['id'] != 'r9']
    c['launch'] = {'view': 'canvas', 'page': 'r7'}
    proj = os.path.join(out, 'project')
    os.makedirs(proj, exist_ok=True)
    names = [n for n, _fn in round9.BOARDS]
    for n in names:
        path = os.path.join(gen, n + '.dc.html')
        copy = 'R7-R9-' + n[3:] + '.dc.html'
        open(os.path.join(proj, copy), 'w').write(to_r7(open(path).read()))
        w, h = size(path)
        was = B.get(copy, {})
        e = {'page': 'r7', 'x': was.get('x', 0), 'y': was.get('y', 0), 'w': w, 'h': h, 'title': TITLES.get(n, n[3:])}
        if not n.startswith(STATIC):
            e['is_interactive'] = True
        B[copy] = e
        if copy not in c['order']:
            c['order'].append(copy)
    for name in r8_boards:  # Round 8 boards that now link to Round 9
        open(os.path.join(proj, 'R7-R8-' + name[3:] + '.dc.html'), 'w').write(to_r7(open(os.path.join(gen, name + '.dc.html')).read()))
    json.dump(c, open(os.path.join(proj, 'canvas.json'), 'w'), ensure_ascii=False)
    print(f'{len(names)} Round 9 boards on r7; {len(old)} old r9 entries retired; {len(r8_boards)} Round 8 copies refreshed')
