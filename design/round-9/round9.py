"""Round 9: the loop end to end, sharing, help and search; the rest of the Hub tools; other channels and sizes;
components; and the material around the app. Every board is written in the Round 7 language and passed through
Round 7's transform for the shared CSS and the `hand` Tweak, like Round 8.

Usage: python3 round9.py <project dir> [Board ...]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'round-8'))
sys.path.insert(0, os.path.join(HERE, '..', 'round-7'))

import round7  # noqa: E402  (transform: Round 7 CSS, the hand link and Tweak)
from lib8 import write, nb_text  # noqa: E402
import loop9  # noqa: E402  (batch 1: the loop, sharing, help, search)
import tools9  # noqa: E402  (batch 2: Hub tools 10 to 18, the savings-group book, all tools)
import channels9  # noqa: E402  (batch 3: desktop, tablet, WhatsApp, USSD, one question everywhere)

BOARDS = loop9.BOARDS + tools9.BOARDS + channels9.BOARDS

if __name__ == '__main__':
    out = sys.argv[1]
    only = sys.argv[2:]
    for name, fn in BOARDS:
        if only and name not in only:
            continue
        html = fn()
        if 'baseVals()' not in html:
            html = round7.transform(name, html, native=True)
        write(os.path.join(out, name + '.dc.html'), nb_text(html))
