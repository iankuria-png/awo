"""Round 8, batch 1: the Hub's icon in three directions (keystone, dial, market awning), each animated,
tried in the real tab bar, at sizes and blurred. Writes R8-Hub-Icons."""
import json

from lib8 import *  # noqa: F401,F403

DIRECTIONS = [
    ('keystone', 'The wedge that holds the arch together.',
     "The Vault's arch moves into Learn as Words. Its keystone lifts out and becomes the Hub: the centre stone, in the centre tab. It sits in the same stone and water family as the other four shapes.",
     'A rainbow or a crown, at a glance. The raised wedge at the top keeps it a keystone. It is not the Words arch: that one stands on legs and a base.',
     'Tells a story the member can see: the arch in Learn, its keystone at the centre. "The tools that hold your money together."',
     'Picked (D-039)', LIME, EVG),
    ('dial', 'A control you turn to fit your numbers.',
     "Every Hub tool takes her own numbers: pay, prices, debts. The needle turns to her setting when the tab opens.",
     'A speedometer, a timer, or a credit-score gauge. That last one breaks rule D8 ("never a credit-score aesthetic").',
     'Reads instantly as "a tool". Moves well.',
     'Risk: looks like a score', '#FFFFFF', SEC),
    ('awning', 'A market stall, open for the day.',
     'The Hub is where things get done: invoices, a shop, a plan. The awning rolls down like a stall opening.',
     'A shop. It is almost the Business icon on the Round 7 icon board, and employed members may read the Hub as "not for me".',
     'Warm and human. Strong for the business mode, and for Shop cards in Community.',
     'Risk: says "shop" only', '#FFFFFF', SEC),
]


def tab_strip(k, kind):
    """A working tab bar: tap any tab; tapping the Hub plays its move."""
    tabs = ''
    for j, (name, icn) in enumerate(AREAS8):
        if icn == 'hub':
            glyph = (f'<sc-if value="[[ hubOn{k} ]]" hint-placeholder-val="[[ true ]]">{hub_icon(kind, 20, anim=True)}</sc-if>'
                     f'<sc-if value="[[ hubOff{k} ]]" hint-placeholder-val="[[ false ]]">{hub_icon(kind, 20)}</sc-if>')
        else:
            glyph = icon(icn)
        tabs += (f'<button onClick="[[ tab{k}_{j} ]]" aria-pressed="[[ on{k}_{j} ]]" style="flex: 1 1 0; height: 60px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; font-size: 12px; color: [[ lc{k}_{j} ]]; font-weight: [[ fw{k}_{j} ]]">'
                 f'<span style="width: 52px; height: 30px; border-radius: 8px; display: flex; align-items: center; justify-content: center; background: [[ pb{k}_{j} ]]; color: [[ fg{k}_{j} ]]; transition: background-color .18s">{glyph}</span>{name}</button>')
    return f'<nav aria-label="Tab bar with the {HUB_NAMES[kind]}" style="display: flex; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #E1E8E4; padding: 4px 2px">{tabs}</nav>'


def dark_strip(kind):
    items = ''
    for name, icn in AREAS8:
        g = hub_icon(kind, 20) if icn == 'hub' else icon(icn)
        if name == 'Learn':
            items += f'<span style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 4px; font-size: 12px; color: {MOON}; font-weight: 600"><span style="width: 52px; height: 30px; border-radius: 8px; background: {MINT}; color: {NIGHT}; display: flex; align-items: center; justify-content: center">{g}</span>{name}</span>'
        else:
            items += f'<span style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 4px; font-size: 12px; color: {NMUTED}"><span style="width: 52px; height: 30px; display: flex; align-items: center; justify-content: center">{g}</span>{name}</span>'
    return f'<div role="img" aria-label="The same bar on Learn\'s night ground, the Hub at rest" style="display: flex; border-radius: {R_M}px; background: {DEEP}; padding: 12px 2px 10px">{items}</div>'


def sizes(kind):
    return ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 8px">{hub_icon(kind, s, INK, sw)}<span style="font-size: 12px; color: {MUTED}">{s}</span></span>'
                   for s, sw in [(16, 2), (20, 2), (24, 2), (32, 1.8), (48, 1.6)])


def squint(kind):
    row = ''.join(f'<span style="display: flex">{hub_icon(kind, 24, INK) if icn == "hub" else icon(icn, 24, INK)}</span>' for _n, icn in AREAS8)
    return f'<span role="img" aria-label="The five tab icons, blurred, to test that the Hub stands apart" style="display: flex; gap: 22px; filter: blur(1.1px)">{row}</span>'


def card(k, d):
    kind, idea, story, mistaken, strength, verdict, vbg, vfg = d
    vstyle = f'background: {vbg}; color: {vfg}' if vbg != '#FFFFFF' else f'border: 1px dashed {vfg}; color: {vfg}'
    return f'''<section class="card" style="gap: 18px">
      <div style="height: 230px; border-radius: {R_M}px; background: {MIST}; position: relative; display: flex; align-items: center; justify-content: center; color: {EVG}">
        {hub_icon(kind, 120, EVG, 1.5, loop=True)}
        <span class="chip" style="position: absolute; left: 12px; top: 12px; {vstyle}">{verdict}</span>
      </div>
      <span style="display: flex; flex-direction: column; gap: 6px"><span class="d" style="font-size: 36px">{HUB_NAMES[kind]}</span><span style="font-size: 17px; font-weight: 600">{idea}</span></span>
      <p style="font-size: 15px; line-height: 1.5; color: {SEC}">{story}</p>
      <span class="ktitle" style="font-size: 15px">In the tab bar (tap the tabs)</span>
      {tab_strip(k, kind)}
      {dark_strip(kind)}
      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 12px; padding-top: 4px">
        <span style="display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 600">Sizes</span><span style="display: flex; gap: 16px; align-items: flex-end">{sizes(kind)}</span></span>
      </div>
      <span style="display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 600">Squint test: the five tabs, blurred</span>{squint(kind)}</span>
      <div style="border-top: 1px solid {LINE7}; padding-top: 14px; display: flex; flex-direction: column; gap: 10px">
        <span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 13px; font-weight: 600">Could be mistaken for</span><span style="font-size: 14px; line-height: 1.45; color: {SEC}">{mistaken}</span></span>
        <span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 13px; font-weight: 600">Its strength</span><span style="font-size: 14px; line-height: 1.45; color: {SEC}">{strength}</span></span>
      </div>
    </section>'''


STORY_CSS = """
@keyframes lift{0%,18%{transform:none}34%{transform:translateY(-34px)}58%,82%{transform:translate(150px,-34px)}100%{transform:none}}
@keyframes lblA{0%,52%{opacity:0}62%,82%{opacity:1}94%,100%{opacity:0}}
.story-ks{animation:lift 5s cubic-bezier(.2,.8,.2,1) infinite}
.story-lbl{animation:lblA 5s ease-out infinite}
"""


def story():
    """The keystone's story: the stone lifts out of the Vault's arch and moves to the centre."""
    import math
    cx, cy, ro, ri = 100, 190, 80, 46

    def P(r, a):
        return f'{cx + r * math.cos(math.radians(a)):.1f} {cy - r * math.sin(math.radians(a)):.1f}'
    half = (f'<path d="M{P(ro, 180)}A{ro} {ro} 0 0 1 {P(ro, 103)}L{P(ri, 98)}A{ri} {ri} 0 0 0 {P(ri, 180)}z" fill="{MIST}" stroke="{EVG}" stroke-width="3" stroke-linejoin="round"></path>'
            f'<path d="M{P(ro, 0)}A{ro} {ro} 0 0 0 {P(ro, 77)}L{P(ri, 82)}A{ri} {ri} 0 0 1 {P(ri, 0)}z" fill="{MIST}" stroke="{EVG}" stroke-width="3" stroke-linejoin="round"></path>')
    a, b = (cx - ro * math.cos(math.radians(77)), cy - ro * math.sin(math.radians(77))), (cx + ro * math.cos(math.radians(77)), cy - ro * math.sin(math.radians(77)))
    c, d = (cx + ri * math.cos(math.radians(82)), cy - ri * math.sin(math.radians(82))), (cx - ri * math.cos(math.radians(82)), cy - ri * math.sin(math.radians(82)))
    ks = f'M{a[0] - 9:.1f} {a[1] - 30:.1f}L{b[0] + 9:.1f} {b[1] - 30:.1f}L{c[0]:.1f} {c[1]:.1f}L{d[0]:.1f} {d[1]:.1f}z'
    art = (f'<svg width="330" height="200" viewBox="0 0 330 200" aria-hidden="true" style="display: block; overflow: visible">{half}'
           f'<g class="story-ks"><path d="{ks}" fill="{LIME}" stroke="{EVG}" stroke-width="3" stroke-linejoin="round"></path></g>'
           f'</svg>')
    return f'''<section class="card" style="gap: 14px">
      <span class="ktitle">The keystone's story, in one move</span>
      <div role="img" aria-label="The keystone lifts out of the arch and moves right, to become the Hub. The arch stays in Learn as Words." style="position: relative; height: 230px; border-radius: {R_M}px; background: {MIST}; padding: 16px 24px 0; overflow: hidden">
        {art}
        <span style="position: absolute; left: 34px; bottom: 12px; font-size: 13px; font-weight: 600; color: {EVG}">The arch stays: Words, in Learn</span>
        <span class="story-lbl" style="position: absolute; left: 236px; top: 140px; font-size: 13px; font-weight: 600; color: {EVG}; display: flex; align-items: center; gap: 6px">The keystone: the Hub</span>
      </div>
      <span class="knote">The Hub's first opening can play this once: the keystone lifts out of Learn's arch and settles in the centre tab. After that, only the small drop.</span>
    </section>'''


def spec():
    rows = [('Keystone', 'The arch\'s two halves draw in, then the keystone drops in and locks them', '300 ms, then 450 ms'),
            ('Dial', 'The needle turns to its setting, with a small overshoot; the ticks appear', '700 ms'),
            ('Market awning', 'Rolls down from the top, then the posts and counter draw', '450 ms, then 340 ms')]
    trs = ''.join(f'<div style="display: grid; grid-template-columns: 130px minmax(0, 1fr) 130px; gap: 12px; padding: 10px 0; border-top: 1px solid {LINE7}; font-size: 14px; line-height: 1.4"><span style="font-weight: 600">{a}</span><span style="color: {SEC}">{b}</span><span style="color: {SEC}">{c}</span></div>' for a, b, c in rows)
    return f'''<section class="card" style="gap: 12px">
      <span class="ktitle">How each one moves</span>
      <div>{trs}</div>
      <span class="knote">One move, once: when she chooses the Hub tab, or the Hub opens (M1, a touch answered). Never on a loop in the app; the loops on this board are only for looking. Ease out, never a spring: springs are kept for wins (M4).</span>
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; border-radius: {R_M}px; background: {MIST}; padding: 6px 6px 6px 14px">
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Reduce motion</span><span style="font-size: 13px; color: {MUTED}">Every icon appears complete, with no move (M6)</span></span>
        {switch(0, 'Reduce motion')}
      </div>
    </section>'''


def colour():
    sw_ = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 12px; color: {SEC}"><span style="width: 52px; height: 30px; border-radius: 8px; background: {pb}; color: {fg}; display: flex; align-items: center; justify-content: center; {"box-shadow: inset 0 0 0 1px #C9D3CE;" if pb == "#FFFFFF" else ""}">{hub_icon(None, 20) if n == "Hub" else icon(i)}</span>{n}</span>'
                  for (n, i), (pb, fg, _lc) in zip(AREAS8, [ACTIVE8[n] for n, _i in AREAS8]))
    return f'''<section class="card" style="gap: 14px">
      <span class="ktitle">The Hub's colour: lime</span>
      <div style="display: flex; justify-content: space-between">{sw_}</div>
      <span class="knote">Each tab keeps its colour when chosen. The Hub takes the Vault's old lime pill. In AWO, lime marks the next step, and the Hub is where she takes it. Words keeps the lime arch inside Learn, on night. Nothing new is added to the palette (rule D3).</span>
    </section>'''


def board():
    cards = ''.join(card(k, d) for k, d in enumerate(DIRECTIONS))
    body = f'''<div data-calm="[[ calm ]]" style="display: flex; flex-direction: column; gap: 24px">
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; align-items: start">{cards}</div>
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr) minmax(0, 1fr); gap: 24px; align-items: start">{story()}{spec()}{colour()}</div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
    const P = %(pal)s;
    for (let k = 0; k < 3; k++) {
      const act = st['a' + k] == null ? 2 : st['a' + k];
      const replay = !!st['r' + k];
      v['hubOn' + k] = act === 2 && !replay; v['hubOff' + k] = act !== 2 || replay;
      for (let j = 0; j < 5; j++) {
        const on = act === j;
        v['on' + k + '_' + j] = on;
        v['pb' + k + '_' + j] = on ? P[j][0] : 'transparent';
        v['fg' + k + '_' + j] = on ? P[j][1] : '%(muted)s';
        v['lc' + k + '_' + j] = on ? P[j][2] : '%(muted)s';
        v['fw' + k + '_' + j] = on ? 600 : 400;
        v['tab' + k + '_' + j] = () => {
          if (j === 2 && act === 2) this.setState({ ['r' + k]: true }, () => this.setState({ ['r' + k]: false }));
          else this.setState({ ['a' + k]: j });
        };
      }
    }
%(sw)s
    v.calm = v.sw0 ? 'true' : 'false';
    return v;
  }
}''' % dict(pal=json.dumps([list(ACTIVE8[n]) for n, _i in AREAS8]), muted=MUTED, sw=switch_js(1, [False]))
    desc = ('The Hub needs its own shape, drawn like the other four: a 2px line on a 24 grid, one meaningful move. Three directions, '
            'each tried in the real tab bar (tap the tabs), on night, at five sizes and blurred. Ian picked the keystone, in lime.')
    return with_css(board7('The Hub\'s icon: three directions', desc, body, logic, 1600, 1790, chip='Keystone picked. Try tapping.'), HUB_CSS + STORY_CSS)


BOARDS = [('R8-Hub-Icons', board)]
