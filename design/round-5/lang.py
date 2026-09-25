from lib import *

P = 'lk'


def col(bg, fg, name, art, means, moves, ic):
    return f'''<article style="display: flex; flex-direction: column; gap: 18px">
  <div style="position: relative; height: 420px; border-radius: 32px; background: {bg}; color: {fg}; overflow: hidden">
    {art}
    <span class="d" style="position: absolute; left: 24px; bottom: 22px; font-size: 56px">{name}</span>
  </div>
  <div style="display: flex; flex-direction: column; gap: 14px; padding: 0 4px">
    <p style="font-size: 17px; line-height: 1.45"><strong style="font-weight: 600">Means</strong><br>{means}</p>
    <p style="font-size: 17px; line-height: 1.45"><strong style="font-weight: 600">Moves</strong><br>{moves}</p>
    <span style="display: flex; align-items: center; gap: 10px; font-size: 15px; color: {SEC}"><span style="width: 44px; height: 30px; border-radius: 999px; background: {ACTIVE[name][0]}; color: {ACTIVE[name][1]}; display: flex; align-items: center; justify-content: center">{icon(ic)}</span>Its tab</span>
  </div>
</article>'''


def build():
    home_art = f'<div style="position: absolute; left: 50%; top: 40px; transform: translateX(-50%)">{pool(150, 262, "lkPool", rimw=4, hole="waterY", label="poolLabel")}</div>'
    learn_art = (f'<div aria-hidden="true" style="position: absolute; right: -40px; top: 26px; filter: drop-shadow(0 0 30px rgba(134,227,196,.3))">{moon(250, "half", craters=True, dark=DEEP)}</div>'
                 f'<div style="position: absolute; left: 30px; top: 170px; animation: bob 3.2s ease-in-out infinite">{ola(P, 104, look=10)}</div>')
    vault_art = (f'<div aria-hidden="true" style="position: absolute; left: 50%; top: 44px; transform: translateX(-50%); width: 190px; height: 250px; border-radius: 95px 95px 18px 18px; background: {EVG}; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 34px; box-sizing: border-box">'
                 f'<span class="d" style="font-size: 40px; color: {LIME}">Stokvel</span></div>')
    rings = ''.join(f'<span aria-hidden="true" style="position: absolute; left: {160 - r}px; top: {180 - r}px; width: {2 * r}px; height: {2 * r}px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: {o}"></span>' for r, o in ((42, .3), (90, .18), (140, .1)))
    comm_art = (rings + f'<span aria-hidden="true" style="position: absolute; left: 118px; top: 138px; width: 84px; height: 84px; border-radius: 999px; border: 2px solid {BLUSH_INK}; animation: spread 3.6s cubic-bezier(.2,.8,.2,1) infinite"></span>'
                f'<img class="face" src="{IMG["wanjiru"]}" alt="" style="position: absolute; left: 136px; top: 156px; width: 48px; height: 48px">'
                f'<img class="face" src="{IMG["thandi"]}" alt="" style="position: absolute; left: 56px; top: 82px; width: 44px; height: 44px; box-shadow: 0 0 0 3px {BLUSH}">'
                f'<img class="face" src="{IMG["grace"]}" alt="" style="position: absolute; left: 226px; top: 232px; width: 44px; height: 44px; box-shadow: 0 0 0 3px {BLUSH}">')
    st = stones(270, 190, [(36, 164, 30, 14), (104, 124, 36, 16), (176, 86, 33, 15), (238, 50, 27, 12)], [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='6 6')
    waves = ''.join(f'<path d="M{x} {y}q9-6 18 0t18 0" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" opacity=".85"></path>' for x, y in ((54, 186), (128, 146), (196, 106)))
    me_art = (f'<div style="position: absolute; left: 18px; top: 92px; width: 270px; height: 190px"><svg width="270" height="200" viewBox="0 0 270 200" aria-hidden="true" style="position: absolute; left: 0; top: 0; overflow: visible">{waves}</svg><div style="position: absolute; inset: 0">{st}</div>'
              f'<img class="face" src="{IMG["naledi"]}" alt="" style="position: absolute; left: 78px; top: 56px; width: 52px; height: 52px; box-shadow: 0 0 0 3px {LIME}; animation: bob 3.4s ease-in-out infinite"></div>')
    cols = ''.join([
        col(EVG, '#FFFFFF', 'Home', home_art, "Money you're building: the safety net and goals.", 'Fills and ripples when money goes in.', 'pool'),
        col(NIGHT, MOON, 'Learn', learn_art, 'Learning in progress. Ola lives here and in Ask, nowhere else.', 'Waxes as a lesson goes on. Ola looks, blinks and cheers.', 'moon'),
        col(LIME, EVG, 'Vault', vault_art, "Money words you've kept.", 'Flips over to show an example.', 'arch'),
        col(BLUSH, BLUSH_INK, 'Community', comm_art, 'Other women, and their words.', 'Spreads out when someone cheers.', 'ripple'),
        col(POOL, EVG, 'Me', me_art, 'Where you stand: your stage and your versions.', 'Steps forward when a new version of your profile lands.', 'stones'),
    ])
    rules = [
        'A shape means one thing. The pool is never used for learning, and the moon never for money.',
        'A tile wears the colour of the area it opens, so Home becomes a map of the app.',
        'One main button per screen.',
        'Ola lives only in Learn and Ask, never beside results or amounts.',
        'No chips over faces, no streak counts, no red for a month that went down.',
        'Cover the logo: a screen should still look like AWO.',
    ]
    rule_html = ''.join(f'<li style="padding: 14px 0; border-top: 1px solid {LINE}; font-size: 17px; line-height: 1.45">{r}</li>' for r in rules)
    W, H = 1760, 1400
    logic = """class Component extends DCLogic {
  renderVals() { return { waterY: 168, poolLabel: 'A pool about a third full' }; }
}"""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>One language, five areas</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{BASE_CSS}
body{{background:{MIST}}}
</style>
</helmet>
<div style="position: relative; width: {W}px; height: {H}px; box-sizing: border-box; padding: 64px; background: {MIST}; color: {INK}; display: flex; flex-direction: column; gap: 44px">
  <svg width="0" height="0" style="position: absolute" aria-hidden="true"><defs>{ola_defs(P)}</defs></svg>
  <header style="display: flex; flex-direction: column; gap: 16px">
    <h1 class="d" style="font-size: 88px">One language, five areas</h1>
    <p style="max-width: 1060px; font-size: 21px; line-height: 1.45; color: {SEC}">Each area has a colour and a shape. A shape means one thing and moves one way. A tile always wears the colour of the area it opens, so you can tell where you are, and where a tap will take you, before you read a word.</p>
  </header>
  <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px">{cols}</div>
  <div style="display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); gap: 56px">
    <section style="display: flex; flex-direction: column; gap: 18px">
      <h2 style="font-size: 24px; font-weight: 600">Two typefaces, two jobs</h2>
      <div style="display: flex; align-items: flex-end; gap: 28px; flex-wrap: wrap">
        <span class="d" style="font-size: 104px; color: {EVG}">R 1 800</span>
        <span class="d" style="font-size: 72px">Stokvel</span>
        <span class="d" style="font-size: 52px">It's payday.</span>
      </div>
      <p style="font-size: 17px; line-height: 1.45; color: {SEC}">Bricolage Grotesque, extra bold and narrow: numbers, the names of things and big moments. Never paragraphs.</p>
      <p style="font-size: 19px; line-height: 1.5; max-width: 640px">Move R 100 to your safety net before anything else. Only you see these numbers.</p>
      <p style="font-size: 17px; line-height: 1.45; color: {SEC}">Geist: everything you read. 15 to 17 pixels for reading, 13 for small print, never under 12.</p>
    </section>
    <section style="display: flex; flex-direction: column; gap: 6px">
      <h2 style="font-size: 24px; font-weight: 600; margin-bottom: 8px">Rules that keep it meaningful</h2>
      <ul style="margin: 0; padding: 0; list-style: none">{rule_html}</ul>
    </section>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{H}}}}}'>
{logic}
</script>
</body>
</html>
'''


if __name__ == '__main__':
    import sys
    open(sys.argv[1], 'w').write(build())
    print('wrote', sys.argv[1])
