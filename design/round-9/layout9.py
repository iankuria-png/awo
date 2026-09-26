"""Lay out canvas page r9 row by row, and make the canvas open on it.
Usage: python3 layout9.py <live canvas.json> <out canvas.json> <folder of .dc.html boards>
Read the live canvas.json with the Artifact tool first, so the editor's changes are kept. Rows are listed top to
bottom; boards not yet built are skipped. Other pages are never touched."""
import json
import os
import re
import sys

PAGE = 'r9'

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
}
STATIC = ('R9-Status-',)  # images, not interactive screens

ROWS = [
    ('r9t1', 'The 30-day loop, end to end', ['R9-Loop-Flow']),
    ('r9t2', "The loop's new screens: the reminder, notifications, what changed, one step, a milestone", ['R9-Lock-Reminder', 'R9-Notifications', 'R9-What-Changed', 'R9-Next-Step', 'R9-Milestone']),
    ('r9t3', 'Sharing to WhatsApp status: a milestone, the word of the week, a story', ['R9-Status-Milestone', 'R9-Status-Word', 'R9-Status-Story']),
    ('r9t4', 'One search, help, and reporting a problem', ['R9-Search', 'R9-Help', 'R9-Help-Report']),
    ('r9t5', 'Batch 2, the rest of the Hub: all tools, and new tools for your own money', ['R9-Hub-All', 'R9-Tool-Remit', 'R9-Tool-Loan', 'R9-Tool-Offers', 'R9-Tool-Pension', 'R9-Tool-Owe']),
    ('r9t6', 'For a business, and a savings-group record book (Q-45)', ['R9-Tool-Worth', 'R9-Tool-Setup', 'R9-Group-Book']),
]

HOWTO = ("Round 9: connecting the pieces, and everything around the app.\n\n"
         "Batch 1 is the 30-day loop as one flow: the reminder, notifications, the check-in, what changed, this month's step, "
         "a milestone and sharing it to WhatsApp status. Then one search, help, and reporting a problem.\n\n"
         "Batch 2 is the rest of the Hub: All tools (the Hub's button now opens it), sending money home, a loan's real cost with "
         "explain my agreement, two job offers, the retirement pulse, what I own and owe, is it worth it, business setup, and "
         "a savings-group record book where AWO never holds the money.\n\n"
         "The flow board at the top shows the whole loop with the gaps it found. Home now has a bell, and the check-in ends on "
         "What changed.\n\n"
         "Every Round 9 board is also on the Round 7 board, in its topic section, marked (Round 9).\n\n"
         "The brief and decisions are in docs/00-discovery/15-round-9.md. All content is sample content.")


def size(proj, name):
    s = open(os.path.join(proj, name + '.dc.html')).read()
    m = re.search(r'"\$preview"\s*:\s*\{\s*"width"\s*:\s*(\d+)\s*,\s*"height"\s*:\s*(\d+)', s.replace('&quot;', '"'))
    return int(m.group(1)), int(m.group(2))


if __name__ == '__main__':
    src, out, proj = sys.argv[1:4]
    c = json.load(open(src))
    B, N = c['boards'], c['notes']
    if not any(p['id'] == PAGE for p in c['pages']):
        c['pages'].append({'id': PAGE, 'name': 'Round 9'})
    c['launch'] = {'view': 'canvas', 'page': PAGE}
    N.setdefault('r9howto', {'fill': 'gray', 'page': PAGE, 'w': 400, 'x': -480, 'y': 0})
    N['r9howto']['text'] = HOWTO
    y = 0
    for key, text, boards in ROWS:
        present = [b for b in boards if os.path.exists(os.path.join(proj, b + '.dc.html'))]
        if not present:
            continue
        N[key] = {'kind': 'title1', 'page': PAGE, 'w': 240, 'x': 0, 'y': y, 'text': text}
        by, x, bottom = y + 300, 0, y + 300
        for b in present:
            w, h = size(proj, b)
            e = {'x': x, 'y': by, 'w': w, 'h': h, 'page': PAGE, 'title': TITLES.get(b, b[3:])}
            if not b.startswith(STATIC):
                e['is_interactive'] = True
            B[b + '.dc.html'] = e
            if b + '.dc.html' not in c['order']:
                c['order'].append(b + '.dc.html')
            x += w + 80
            bottom = max(bottom, by + h)
        N[key]['maxW'] = max(1200, min(8000, x - 80))
        y = bottom + 300
    json.dump(c, open(out, 'w'), ensure_ascii=False)
    print('page r9 laid out; the last row ends at', y - 300)
