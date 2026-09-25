"""R7-Type: the Round 7 key board. Geist does the work, a hand appears only at special moments, corners are restricted."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import (EVG, EVG_D, LIME, BLUSH, BLUSH_INK, POOL, NIGHT, MOON, NMUTED, INK, SEC, MUTED, MIST, IMG,  # noqa: E402
                  icon, holes, write)
from round7 import HANDS  # noqa: E402

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300..700&amp;family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800'
         '&amp;family=Kalam:wght@400;700&amp;family=Nanum+Pen+Script&amp;family=Delicious+Handrawn&amp;display=swap" rel="stylesheet">')

G = "font-family: 'Geist', ui-sans-serif, system-ui, sans-serif"
BRIC = "font-family: 'Bricolage Grotesque', ui-sans-serif, sans-serif; font-weight: 800; font-stretch: 82%; letter-spacing: -0.03em; line-height: .9"
HF = "font-family: '[[ handFont ]]', cursive; font-size-adjust: .5; font-weight: 400; line-height: 1.15"


def g(size, weight=600, track='-0.045em', lh='.95', extra=''):
    return f'{G}; font-size: {size}px; font-weight: {weight}; letter-spacing: {track}; line-height: {lh}; {extra}'


def card(title, body, note=''):
    n = f'<p style="font-size: 15px; line-height: 1.45; color: {SEC}">{note}</p>' if note else ''
    return f'<section style="border-radius: 14px; background: #FFFFFF; padding: 28px; display: flex; flex-direction: column; gap: 20px"><h2 style="{g(34)}">{title}</h2>{n}{body}</section>'


def build():
    scale = [('Display', '56, 600, -0.045em', f'<span style="{g(56)}">Hey Naledi</span>'),
             ('Numbers', '44, 600, tabular', f'<span style="{g(44)}; color: {EVG}; font-variant-numeric: tabular-nums">R 1 800</span>'),
             ('Titles', '28, 600, -0.025em', f'<span style="{g(28, track="-0.025em", lh="1.1")}">Savings groups, in three minutes</span>'),
             ('Body', '17, 400', f'<span style="{g(17, 400, "0", "1.5")}">Each evening, write down what the stall took in and what you took home.</span>'),
             ('Secondary', '15, 400', f'<span style="{g(15, 400, "0", "1.45")}; color: {SEC}">Only you see these numbers. Your circle sees first names.</span>'),
             ('Caption', '13, the floor is 12', f'<span style="{g(13, 400, "0", "1.4")}; color: {MUTED}">Stored in South Africa.</span>')]
    rows = ''.join(f'<div style="display: grid; grid-template-columns: 170px minmax(0, 1fr); gap: 20px; align-items: center; padding: 14px 0; {"border-bottom: 1px solid #EEF2EF;" if i < len(scale) - 1 else ""}"><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">{a}<br>{b}</span>{c}</div>' for i, (a, b, c) in enumerate(scale))
    compare = f'''<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="border-radius: 14px; background: {MIST}; padding: 20px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 600; color: {MUTED}">Round 6: Bricolage, condensed</span><span style="{BRIC}; font-size: 54px">Stokvel</span><span style="{BRIC}; font-size: 40px; color: {EVG}">R 1 800</span></div>
      <div style="border-radius: 14px; background: {MIST}; padding: 20px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 600; color: {EVG}">Round 7: Geist</span><span style="{g(48)}">Stokvel</span><span style="{g(36)}; color: {EVG}; font-variant-numeric: tabular-nums">R 1 800</span></div>
    </div>'''
    type_card = card('Geist does the work', f'''<div style="display: flex; align-items: flex-end; gap: 28px"><span style="{g(180, 600, "-0.05em", ".8")}; color: {EVG}">Aa</span>
      <div style="display: flex; flex-direction: column; gap: 8px; padding-bottom: 10px"><span style="{g(26, 600, "-0.025em", "1.1")}">Where am I, and what's next?</span><span style="{g(16, 400, "0", "1.5")}; color: {SEC}">Plain words first, numbers second. From Round 1's Oasis board.</span>
      <span style="display: flex; gap: 16px; font-size: 15px"><span style="font-weight: 400">Regular 400</span><span style="font-weight: 500">Medium 500</span><span style="font-weight: 600">Semibold 600</span></span></div></div>
      <div>{rows}</div>{compare}''', 'One family for everything, from 12px captions to 180px moments. Tight tracking on the big sizes gives it character; tabular figures keep money aligned.')

    switch = ''.join(f'<button onClick="[[ h{i} ]]" aria-pressed="[[ hOn{i} ]]" style="height: 44px; padding: 0 18px; border-radius: 10px; background: [[ hBg{i} ]]; color: [[ hFg{i} ]]; box-shadow: inset 0 0 0 1px [[ hBd{i} ]]; font-size: 15px; font-weight: 600; font-family: inherit; border: 0; cursor: pointer">{h}</button>' for i, h in enumerate(HANDS))
    stone = f'<svg width="120" height="46" viewBox="0 0 120 46" aria-hidden="true"><ellipse cx="60" cy="28" rx="44" ry="15" fill="{EVG_D}"></ellipse><ellipse cx="60" cy="24" rx="44" ry="15" fill="{LIME}"></ellipse></svg>'
    moments = [
        ('Welcome', EVG, '#FFFFFF', f'<div style="position: relative; height: 150px"><span style="position: absolute; left: 6px; top: 6px; {HF}; font-size: 34px; color: {LIME}; transform: rotate(-7deg)">start here</span><svg aria-hidden="true" width="70" height="70" viewBox="0 0 70 70" style="position: absolute; left: 24px; top: 44px"><path d="M14 4c-6 18 0 34 22 44" fill="none" stroke="{LIME}" stroke-width="2.6" stroke-linecap="round"></path><path d="M28 50l9-1-3-9" fill="none" stroke="{LIME}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path></svg><span style="position: absolute; left: 60px; top: 96px">{stone}</span></div>'),
        ('The first profile', POOL, EVG, f'<div style="display: flex; flex-direction: column; gap: 6px"><span style="{HF}; font-size: 32px">Here\'s where you start.</span><span style="{g(44)}">Stage 2 of 4</span></div>'),
        ('A win, in her words', BLUSH, BLUSH_INK, f'<div style="display: flex; gap: 12px; align-items: flex-start"><img src="{IMG["wanjiru"]}" alt="" style="width: 44px; height: 44px; border-radius: 999px; object-fit: cover; flex-shrink: 0"><span style="{HF}; font-size: 30px">Seven evenings of notes. Now I know what the stall really earns.</span></div>'),
        ('A step done', '#FFFFFF', INK, f'<div style="display: flex; gap: 12px; align-items: flex-start"><span style="width: 26px; height: 26px; border-radius: 999px; background: {EVG}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{icon("check", 14, "#FFFFFF", 3)}</span><span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px">R 100 a week, from today</span><span style="{HF}; font-size: 28px; color: {EVG}">Done for this week. Nicely done!</span></span></div>'),
        ('Learn', NIGHT, MOON, f'<span style="{HF}; font-size: 30px">You showed up three evenings this week.</span>'),
        ('Her answer', BLUSH, BLUSH_INK, f'<span style="align-self: flex-end; padding: 12px 16px; border-radius: 14px 6px 14px 14px; background: {BLUSH_INK}; color: {BLUSH}; {HF}; font-size: 26px">Takeaway on Friday. Cooked instead, and it was nicer.</span>'),
    ]
    mcards = ''.join(f'<div style="border-radius: 14px; background: {bg}; color: {fg}; padding: 20px; min-height: 190px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px; {"box-shadow: inset 0 0 0 1px #DCE4DF;" if bg == "#FFFFFF" else ""}"><span style="font-size: 13px; font-weight: 600; opacity: .8">{t}</span>{b}</div>' for t, bg, fg, b in moments)
    rules = f'''<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="border-radius: 14px; background: {MIST}; padding: 20px; display: flex; flex-direction: column; gap: 8px"><span style="font-size: 16px; font-weight: 600">Use it for</span><span style="font-size: 15px; line-height: 1.5; color: {SEC}">Someone's own words at a moment that matters: a win, her answer, her first page. A short note from AWO at a real milestone: a first profile, a step done, a week of showing up.</span></div>
      <div style="border-radius: 14px; background: {MIST}; padding: 20px; display: flex; flex-direction: column; gap: 8px"><span style="font-size: 16px; font-weight: 600">Never for</span><span style="font-size: 15px; line-height: 1.5; color: {SEC}">Numbers, buttons or instructions. Results, scores or stages. Anything Ola or AI writes. Anything under 20px. At most one handwritten line on a screen, always real text so it can be read aloud and translated.</span></div>
    </div>'''
    hand_card = card('A hand, for special moments', f'''<div role="group" aria-label="Handwriting candidates" style="display: flex; gap: 8px; align-items: center">{switch}<span style="font-size: 14px; color: {MUTED}; margin-left: 8px">Also a Tweak on every Round 7 screen</span></div>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">{mcards}</div>{rules}''',
                     "Kalam is the default: warm, grown-up and the most legible at small sizes. Nanum Pen Script feels like a real felt-tip note. Delicious Handrawn is a bold marker, better for ads than for the app. Tap to compare.")

    radii = [(6, 'Chips, tags, small controls', f'<span style="height: 32px; padding: 0 12px; border-radius: 6px; border: 1px dashed {MUTED}; color: {MUTED}; font-size: 13px; font-weight: 600; display: inline-flex; align-items: center">Sample</span>'),
             (10, 'Buttons, inputs, list rows', f'<span style="height: 52px; padding: 0 22px; border-radius: 10px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: inline-flex; align-items: center">Continue</span>'),
             (14, 'Cards, tiles, sheets', f'<span style="width: 150px; height: 96px; border-radius: 14px; background: {LIME}; display: block"></span>'),
             ('circle', 'Faces, dots and the five shapes', f'<img src="{IMG["amara"]}" alt="" style="width: 72px; height: 72px; border-radius: 999px; object-fit: cover">')]
    rspec = ''.join(f'<div style="display: flex; flex-direction: column; gap: 14px; align-items: flex-start"><span style="{g(40)}">{r if r == "circle" else str(r) + "px"}</span>{ex}<span style="font-size: 15px; line-height: 1.4; color: {SEC}">{n}</span></div>' for r, n, ex in radii)
    tile_before = f'<div style="border-radius: 28px; background: {EVG}; color: #FFFFFF; padding: 20px; display: flex; flex-direction: column; gap: 12px"><span style="font-size: 13px; color: #BFDCCF">Round 6: 28, 24, pill</span><span style="{BRIC}; font-size: 40px; color: {LIME}">R 1 800</span><div style="height: 8px; border-radius: 99px; background: rgba(255,255,255,.2)"><div style="width: 36%; height: 8px; border-radius: 99px; background: {LIME}"></div></div><span style="height: 48px; border-radius: 999px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center; font-weight: 600">I moved R 100</span></div>'
    tile_after = f'<div style="border-radius: 14px; background: {EVG}; color: #FFFFFF; padding: 20px; display: flex; flex-direction: column; gap: 12px"><span style="font-size: 13px; color: #BFDCCF">Round 7: 14, 10, square bar ends</span><span style="{g(36)}; color: {LIME}">R 1 800</span><div style="height: 8px; border-radius: 2px; background: rgba(255,255,255,.2)"><div style="width: 36%; height: 8px; border-radius: 2px; background: {LIME}"></div></div><span style="height: 48px; border-radius: 10px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center; font-weight: 600">I moved R 100</span></div>'
    corner_card = card('Corners: three sizes and a circle', f'<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px">{rspec}</div><div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">{tile_before}{tile_after}</div>',
                       'Round 6 used seven radii, from 16 to 44 plus pills. Round 7 keeps three, and the shapes keep their own curves: the pool is still a capsule and faces are still round.')

    body = f'''<header style="display: flex; flex-direction: column; gap: 14px"><h1 style="{g(84, 600, "-0.05em", ".9")}">Type and corners</h1>
    <p style="font-size: 20px; line-height: 1.45; color: {SEC}; max-width: 1100px">Round 7 is an experiment on top of Round 6: Geist does all the work, as on Round 1's Oasis board. A handwritten face appears only at a few moments that matter, and corners come in three sizes and a circle.</p></header>
  <div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 28px; align-items: start">{type_card}{corner_card}</div>
  {hand_card}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const hands = %(hands)s;
    const def = hands.indexOf(this.props.hand ?? 'Kalam');
    const h = st.h == null ? (def < 0 ? 0 : def) : st.h;
    const v = { handFont: hands[h] };
    for (let i = 0; i < hands.length; i++) {
      v['h' + i] = () => this.setState({ h: i }); v['hOn' + i] = h === i;
      v['hBg' + i] = h === i ? '%(evg)s' : '#FFFFFF'; v['hFg' + i] = h === i ? '#FFFFFF' : '%(ink)s'; v['hBd' + i] = h === i ? '%(evg)s' : '#DCE4DF';
    }
    return v;
  }
}''' % dict(hands=str(HANDS).replace("'", '"'), evg=EVG, ink=INK)
    prop = '{"hand":{"editor":"enum","options":' + str(HANDS).replace("'", '"') + ',"default":"Kalam","section":"Round 7"},"$preview":{"width":1600,"height":2060}}'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Type and corners</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0;{G};background:#E4EAE6;color:{INK}}}
h1,h2,p{{margin:0}}
button:focus-visible{{outline:2px solid {EVG};outline-offset:3px}}
</style>
</helmet>
<div style="width: 1600px; height: 2060px; box-sizing: border-box; padding: 64px; background: #E4EAE6; color: {INK}; {G}; display: flex; flex-direction: column; gap: 32px">
{holes(body)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{prop}'>
{logic}
</script>
</body>
</html>
'''


if __name__ == '__main__':
    write(os.path.join(sys.argv[1], 'R7-Type.dc.html'), build())
