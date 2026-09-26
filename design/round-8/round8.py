"""Round 8: Learn with the Vault as a tab, the Hub at the centre, goals of every kind, real stories and a
Community feed (D-037, D-038). Every board is written natively in the Round 7 language and passed through
Round 7's transform for the shared CSS and the `hand` Tweak.

Usage: python3 round8.py <project dir> [Board ...]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'round-7'))

import round7  # noqa: E402  (transform: Round 7 CSS, the hand link and Tweak)
from lib8 import write, nb_text  # noqa: E402
import icons8  # noqa: E402  (batch 1: the Hub's icon, three directions)
import ia8  # noqa: E402  (batch 2: the IA and the tab bar)
import learn8  # noqa: E402  (batch 2: Learn with Paths, Words and Stories; a topic; the decoder)
import hub8  # noqa: E402  (batch 3: the Hub landing in both modes; the tool skeleton)
import tools8  # noqa: E402  (batch 3: the Me tools)
import biz8  # noqa: E402  (batch 3: the business tools and Shop)
import goals8  # noqa: E402  (batch 3: the goals studio and Home)
import stories8  # noqa: E402  (batch 4: the story reader, the podcast, my worst money mistake)
import feed8  # noqa: E402  (batch 4: the Community feed, composer, a thread, the parts)

BOARDS = icons8.BOARDS + ia8.BOARDS + learn8.BOARDS + hub8.BOARDS + tools8.BOARDS + biz8.BOARDS + goals8.BOARDS + stories8.BOARDS + feed8.BOARDS

if __name__ == '__main__':
    out = sys.argv[1]
    only = sys.argv[2:]
    for name, fn in BOARDS:
        if only and name not in only:
            continue
        html = fn()
        if 'baseVals()' not in html:  # Home is built from Round 7's, which already carries the transform
            html = round7.transform(name, html, native=True)
        write(os.path.join(out, name + '.dc.html'), nb_text(html))
