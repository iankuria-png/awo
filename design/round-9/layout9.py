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

ROWS = [
    ('r9t1', 'The 30-day loop, end to end', ['R9-Loop-Flow']),
    ('r9t2', "The loop's new screens: the reminder, notifications, what changed, one step, a milestone", ['R9-Lock-Reminder', 'R9-Notifications', 'R9-What-Changed', 'R9-Next-Step', 'R9-Milestone']),
    ('r9t3', 'Sharing to WhatsApp status: a milestone, the word of the week, a story', ['R9-Status-Milestone', 'R9-Status-Word', 'R9-Status-Story']),
    ('r9t4', 'One search, help, and reporting a problem', ['R9-Search', 'R9-Help', 'R9-Help-Report']),
    ('r9t5', 'Batch 2, the rest of the Hub: all tools, and new tools for your own money', ['R9-Hub-All', 'R9-Tool-Remit', 'R9-Tool-Loan', 'R9-Tool-Offers', 'R9-Tool-Pension', 'R9-Tool-Owe']),
    ('r9t6', 'For a business, and a savings-group record book (Q-45)', ['R9-Tool-Worth', 'R9-Tool-Setup', 'R9-Group-Book']),
    ('r9t7', 'Batch 3, other sizes: a computer and a tablet', ['R9-Desktop-Home', 'R9-Desktop-Me', 'R9-Tablet-Learn']),
    ('r9t8', 'Other channels: the check-in on WhatsApp and USSD, and one question everywhere (Q-21)', ['R9-WhatsApp-Checkin', 'R9-USSD', 'R9-One-Question']),
    ('r9t9', 'Batch 4, components: sheets, dialogs and toasts; dates, files, loading and two currencies', ['R9-Comp-Overlays', 'R9-Comp-Inputs']),
    ('r9t10', 'Empty states, from the five shapes', ['R9-Empty-States']),
    ('r9t11', 'Batch 5, around the app: three emails', ['R9-Email-Welcome', 'R9-Email-Reminder', 'R9-Email-Summary']),
    ('r9t12', 'Print: an A5 flyer with a QR code, and workshop slides', ['R9-Flyer-A5', 'R9-Workshop-Slides']),
    ('r9t13', 'The app in real places: a market stall, a commute, a kitchen table, a lock screen', ['R9-Place-Stall', 'R9-Place-Commute', 'R9-Place-Table', 'R9-Place-Lock']),
    ('r9t14', 'Social: two carousels', ['R9-Carousel-Diva', 'R9-Carousel-Loan']),
    ('r9t15', "Two more WhatsApp status cards, and the AWO Podcast's cover and episode tiles", ['R9-Status-Question', 'R9-Status-Quiz', 'R9-Podcast-Cover', 'R9-Podcast-Tiles']),
    ('r9t16', 'Batch 6, merchandise: a money notebook for traders, and the check-in on the fridge', ['R9-Notebook', 'R9-Checkin-Magnet']),
    ('r9t17', 'Stickers and pins of the five shapes, a tote bag, and ambassador T-shirts (Q-48)', ['R9-Stickers-Pins', 'R9-Tote', 'R9-Tshirts']),
]

HOWTO = ("Round 9: connecting the pieces, and everything around the app.\n\n"
         "Batch 1 is the 30-day loop as one flow: the reminder, notifications, the check-in, what changed, this month's step, "
         "a milestone and sharing it to WhatsApp status. Then one search, help, and reporting a problem.\n\n"
         "Batch 2 is the rest of the Hub: All tools (the Hub's button now opens it), sending money home, a loan's real cost with "
         "explain my agreement, two job offers, the retirement pulse, what I own and owe, is it worth it, business setup, and "
         "a savings-group record book where AWO never holds the money.\n\n"
         "Batch 3 is other sizes and channels: Home and the DIVA profile on a computer, Learn on a tablet, and the check-in on "
         "WhatsApp and USSD, with one board showing the same question drawn in every channel.\n\n"
         "Batch 4 is components: sheets, dialogs (are you sure?), toasts, a date picker, file upload, loading placeholders and an "
         "amount in two currencies, all working; and ten empty states drawn from the five shapes.\n\n"
         "Batch 5 is around the app: a welcome, a check-in reminder and a monthly summary email (on a computer and a phone, "
         "light and dark); an A5 flyer with a QR code and workshop slides; the app in four real places; two carousels, two "
         "more status cards and the AWO Podcast's art. No email or print shows an amount, the DIVA score or the stage (Q-47).\n\n"
         "Batch 6 is merchandise: a money-in-and-out notebook for traders (the Hub's notebook on paper), a check-in magnet "
         "and a printed year, stickers and pins of the five shapes, a tote bag, and ambassador T-shirts with a badge that says "
         "an ambassador shows the app and never gives advice (Q-48).\n\n"
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
