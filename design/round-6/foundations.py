"""R6-Foundations: Direction E at Volume 1 (Clean). Colour, type, shapes, people, motion, radius."""
from lib6 import *
from kit import kit_board

FOUND_CSS_KEYS = """
@keyframes fillLoop{0%,100%{transform:translateY(110px)}50%{transform:translateY(40px)}}
@keyframes flipLoop{0%,35%{transform:rotateY(0)}50%,85%{transform:rotateY(180deg)}100%{transform:rotateY(360deg)}}
@keyframes waxLoop{0%,15%{opacity:.25}30%,100%{opacity:1}}
@keyframes stepLoop{0%,20%{fill:#FFFFFF}30%,100%{fill:#D8F36A}}
@keyframes demo{0%,20%{transform:translateX(0)}50%,70%{transform:translateX(150px)}100%{transform:translateX(0)}}
@keyframes squeeze{0%,40%,100%{transform:scale(1)}45%{transform:scale(.9)}}
"""

AREA_INFO = [
    ('Home', EVG, '#FFFFFF', LIME, 'pool', '#0F4A36', 'Money she is building: the safety net and goals.', 'Fills and ripples when money goes in.'),
    ('Learn', NIGHT, MOON, MOON, 'moon', '#0B0F0E', 'Learning in progress. Ola lives here and in Ask.', 'Waxes as a lesson goes on.'),
    ('Vault', LIME, EVG, EVG, 'arch', '#D8F36A', 'Money words she has kept.', 'Flips over to show an example.'),
    ('Community', BLUSH, BLUSH_INK, BLUSH_INK, 'ripple', '#FFC7D6', 'Other women and their words. Only people are blush.', 'Spreads out when someone cheers.'),
    ('Me', POOL, EVG, EVG, 'stones', '#D3E8E4', 'Where she stands: her stage and her versions.', 'Steps forward when a new version lands.'),
]


def foundations():
    areas = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 12px">
        <div style="height: 210px; border-radius: 28px; background: {bg}; color: {fg}; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; {'box-shadow: inset 0 0 0 1px #C9D3CE;' if bg == POOL else ''}">
          <span style="display: flex; justify-content: space-between; align-items: center"><span class="d" style="font-size: 40px">{n}</span>{icon(ic, 34, sh, 2)}</span>
          <span style="font-size: 14px; font-weight: 600">{hx}</span>
        </div>
        <span style="font-size: 15px; line-height: 1.45"><strong>Means:</strong> {m}</span>
        <span style="font-size: 15px; line-height: 1.45; color: {SEC}"><strong style="color: {INK}">Moves:</strong> {mv}</span>
      </div>''' for n, bg, fg, sh, ic, hx, m, mv in AREA_INFO)
    neutrals = ''.join(f'<div style="display: flex; align-items: center; gap: 12px"><span style="width: 48px; height: 48px; flex-shrink: 0; border-radius: 14px; background: {c}; box-shadow: inset 0 0 0 1px #C9D3CE"></span><span style="font-size: 14px; line-height: 1.35"><strong>{n}</strong><br>{r}</span></div>'
                       for c, n, r in [(MIST, 'Mist #EEF3F0', 'every light ground'), ('#FFFFFF', 'White', 'cards and sheets'), (INK, 'Ink #101814', 'text, 16 to 1'), (SEC, 'Secondary #3F4B45', 'supporting text'), (MUTED, 'Muted #56625C', 'captions, 5.7 to 1'), (MINT, 'Mint and iris', "Ola's glow only")])
    type_rows = [
        ('Display 800, condensed', '96', f'<span class="d" style="font-size: 96px">Hey Naledi</span>'),
        ('Numbers', '64', f'<span class="d" style="font-size: 64px; color: {EVG}; font-variant-numeric: tabular-nums">R 1 800</span>'),
        ('Screen titles', '50', '<span class="d" style="font-size: 50px">Community</span>'),
        ('Card titles', '34', '<span class="d" style="font-size: 34px">Savings groups, in three minutes</span>'),
        ('Geist body', '17', '<span style="font-size: 17px; line-height: 1.5">Each evening, write down what the stall took in and what you took home.</span>'),
        ('Geist secondary', '15', f'<span style="font-size: 15px; line-height: 1.45; color: {SEC}">Only you see these numbers. Your circle sees first names.</span>'),
        ('Caption, the floor is 12', '13', f'<span style="font-size: 13px; color: {MUTED}">Stored in South Africa. Nothing on screen is smaller than 12px.</span>'),
    ]
    types = ''.join(f'<div style="padding: 16px 0; {"border-bottom: 1px solid #EEF2EF;" if i < len(type_rows) - 1 else ""} display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 20px; align-items: center"><span style="font-size: 13px; line-height: 1.35; color: {MUTED}">{a}<br>{b}px</span>{c}</div>' for i, (a, b, c) in enumerate(type_rows))
    pool_demo = pool(64, 150, 'fPool', rimw=2.5).replace('transform: translateY({{ waterY }}px); transition: transform .6s cubic-bezier(.34,1.56,.64,1)', 'animation: fillLoop 5s ease-in-out infinite').replace('{{ poolLabel }}', 'A pool filling and emptying')
    phases = ''.join(f'<span style="animation: waxLoop 4s ease-out {k * 0.4:.1f}s infinite">{moon(40, p)}</span>' for k, p in enumerate(['new', 'cres', 'half', 'full']))
    stones_demo = ''.join(f'<ellipse cx="{x}" cy="{y + 4}" rx="{rx}" ry="{ry}" fill="{EVG_D}"></ellipse><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#FFFFFF" stroke="{EVG}" stroke-width="2.5" style="animation: stepLoop 4s ease-out {k * 0.5:.1f}s infinite"></ellipse>'
                          for k, (x, y, rx, ry) in enumerate([(26, 110, 20, 8), (78, 82, 22, 9), (132, 54, 22, 9), (184, 26, 18, 7)]))
    shape_cards = [
        ('The pool', 'Home', f'<div style="height: 160px; display: flex; align-items: center; justify-content: center; background: {EVG}; border-radius: 20px">{pool_demo}</div>'),
        ('The moon', 'Learn', f'<div style="height: 160px; display: flex; align-items: center; justify-content: center; gap: 12px; background: {NIGHT}; border-radius: 20px">{phases}</div>'),
        ('The arch', 'Vault', f'<div style="height: 160px; display: flex; align-items: center; justify-content: center; background: {MIST}; border-radius: 20px; perspective: 600px"><span style="width: 96px; height: 120px; border-radius: 48px 48px 14px 14px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: flipLoop 4s cubic-bezier(.34,1.3,.64,1) infinite">{icon("arch", 40, EVG)}</span></div>'),
        ('The ripple', 'Community', f'<div style="position: relative; height: 160px; display: flex; align-items: center; justify-content: center; background: {BLUSH}; border-radius: 20px; overflow: hidden"><span style="position: absolute; left: 50%; top: 50%; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 999px; border: 2px solid {BLUSH_INK}; animation: spread 2.4s ease-out infinite"></span><span style="position: absolute; left: 50%; top: 50%; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 999px; border: 2px solid {BLUSH_INK}; animation: spread 2.4s ease-out 1.2s infinite"></span><img class="face" src="{IMG["wanjiru"]}" alt="" style="position: relative; width: 64px; height: 64px"></div>'),
        ('The stones', 'Me', f'<div style="height: 160px; display: flex; align-items: center; justify-content: center; background: {POOL}; border-radius: 20px"><svg width="210" height="130" viewBox="0 0 210 130" aria-hidden="true">{stones_demo}</svg></div>'),
    ]
    shapes = ''.join(f'<div style="display: flex; flex-direction: column; gap: 10px">{demo}<span style="font-size: 16px; font-weight: 600">{t} <span style="font-weight: 400; color: {MUTED}">{a}</span></span></div>' for t, a, demo in shape_cards)
    moods = ''.join(f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 8px"><img src="{src}" alt="{alt}" style="width: 100%; height: 170px; object-fit: cover; object-position: {pos}; border-radius: 20px"><figcaption style="font-size: 14px; font-weight: 600">{cap}</figcaption></figure>'
                    for src, alt, pos, cap in [
                        (IMG['naledi_cafe'], 'A woman absorbed in her tablet', '45% 30%', 'Focused'),
                        (IMG['amara_coat'], 'A woman in a winter coat', '60% 40%', 'Determined'),
                        (IMG['wanjiru_stall'], 'A woman at her market stall', '62% 35%', 'At work'),
                        (IMG['grace_dancing'], 'An older woman dancing in the street', '40% 20%', 'Joy at sixty'),
                    ])
    motions = ''.join(f'<div style="display: grid; grid-template-columns: 180px minmax(0, 1fr); gap: 16px; align-items: center"><span style="font-size: 15px; line-height: 1.35"><strong>{ms} ms</strong> {what}</span><span style="height: 36px; border-radius: 999px; background: {MIST}; display: flex; align-items: center; padding: 0 6px"><span style="width: 26px; height: 26px; border-radius: 99px; background: {col}; animation: {anim}"></span></span></div>'
                      for ms, what, col, anim in [
                          ('90', 'a touch', EVG, 'squeeze 1.6s cubic-bezier(.2,.8,.2,1) infinite'),
                          ('180', 'a change', EVG, 'demo .9s cubic-bezier(.2,.8,.2,1) infinite'),
                          ('280', 'a new screen', EVG, 'demo 1.4s cubic-bezier(.2,.8,.2,1) infinite'),
                          ('600', 'a win', LIME, 'demo 3s cubic-bezier(.34,1.56,.64,1) infinite')])
    radius = ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-start"><span style="width: 96px; height: 72px; border-radius: {r}px; background: #FFFFFF; box-shadow: inset 0 0 0 1.5px {EVG}"></span><span style="font-size: 13px; line-height: 1.35">{n}<br><span style="color: {MUTED}">{r if r < 999 else "pill"}{"px" if r < 999 else ""}</span></span></div>'
                     for r, n in [(28, 'Hero block'), (24, 'Tile'), (20, 'List card'), (999, 'Action')])
    body = f'''  <section style="display: flex; flex-direction: column; gap: 18px">
    <h2 class="d" style="font-size: 44px">Colour: five areas, one job each</h2>
    <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px">{areas}</div>
    <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px; padding-top: 6px">{neutrals}</div>
    <p style="font-size: 15px; line-height: 1.45; color: {SEC}; max-width: 1100px">Lime marks progress and wins, and is the main button on dark surfaces. Evergreen is the main button on light ones. No red for a month that went down: decreases are grey, and only gains use lime.</p>
  </section>
  <div style="display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 40px; align-items: start">
    <section class="card"><h2 class="d" style="font-size: 44px">Type</h2><span class="knote">Bricolage Grotesque 800 at 82% width, for names, numbers and the one thing that matters. Geist for everything read. Never condensed paragraphs.</span><div>{types}</div></section>
    <section class="card"><h2 class="d" style="font-size: 44px">Shapes</h2><span class="knote">Each shape means one thing and moves one way. The tab bar is made of them, so the navigation teaches the language.</span>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">{shapes}</div></section>
  </div>
  <div style="display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 40px; align-items: start">
    <section class="card"><h2 class="d" style="font-size: 44px">People</h2><span class="knote">Real women, ages 25 to 65, at work and at home. Focused, tired, determined and calm, not only laughing. Faces are never covered by chips. Blush belongs to people. Community shows first names only.</span>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px">{moods}</div>
      <span class="knote">Stand-ins from nappy.co until AWO photographs real members (Q-27).</span></section>
    <div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card"><h2 class="d" style="font-size: 44px">Motion</h2><span class="knote">Motion answers a touch, shows progress or marks a win. Arrivals ease out; only wins spring. Reduce motion turns every loop off.</span>{motions}</section>
      <section class="card"><h2 class="d" style="font-size: 44px">Radius follows rank</h2><div style="display: flex; gap: 20px">{radius}</div><span class="knote">Spacing steps: 4, 8, 12, 16, 20, 24. Touch targets are at least 44px.</span></section>
    </div>
  </div>'''
    return kit_board('E foundations', 'Direction E at Volume 1 (Clean): calm mist screens, one block in each area colour, condensed type for the one thing that matters. Everything here is used in the Round 6 screens.', body, static_logic(), 1600, 2240, css=FOUND_CSS_KEYS, chip='Sample content')


if __name__ == '__main__':
    write(os.path.join(sys.argv[1], 'R6-Foundations.dc.html'), foundations())
