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
from lib8 import write  # noqa: E402
import icons8  # noqa: E402  (batch 1: the Hub's icon, three directions)

BOARDS = icons8.BOARDS

if __name__ == '__main__':
    out = sys.argv[1]
    only = sys.argv[2:]
    for name, fn in BOARDS:
        if only and name not in only:
            continue
        write(os.path.join(out, name + '.dc.html'), round7.transform(name, fn(), native=True))
