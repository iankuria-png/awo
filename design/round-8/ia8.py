"""Round 8, batch 2: the new information architecture and the tab bar (D-037). Writes R8-IA."""
import json

from lib8 import *  # noqa: F401,F403

TABS = [
    ('Home', 'pool', EVG, LIME, 'Today, at a glance', ['Several goals, each its own pool', "This week's step", 'The next useful thing, from the Hub', 'Stories and the community pulse'], 'Goals of every kind, not one safety net'),
    ('Learn', 'moon', NIGHT, MINT, 'Understand money, at night', ['Paths: courses and topics', 'Words: the Vault, with the decoder', 'Stories: Rise, mistakes, the podcast', 'Ola, and Ask'], 'The Vault moves in, as Words'),
    ('Hub', 'hub', LIME, EVG, 'Tools that do things', ['Two modes: My job, My business', 'The next useful thing', 'Tools by the job they do', 'Stay safe, always last'], 'New, in the centre'),
    ('Community', 'ripple', BLUSH, BLUSH_INK, 'Women who get it', ['A feed: For you, and Circles', 'Notes, Letters, Milestones, Questions', 'Shop cards from members', 'Circles, events, the buddy'], 'A feed to read and post in'),
    ('Me', 'stones', POOL, EVG, 'Where you stand', ['DIVA profile and versions', 'The report, and your business', 'Settings', 'Your documents'], "Your documents: what you shared, and when it's deleted"),
]

MOVES = [
    (('Vault', 'arch'), ('Learn, as Words', 'moon'), 'Words sit beside the lessons that use them. The arch comes too.'),
    (('Stories on Home', 'pool'), ('Learn, as Stories', 'moon'), 'Stories get a home of their own. The best still reach Home and the feed.'),
    (('Check an offer, in Ask', 'moon'), ('Hub, Stay safe', 'hub'), 'A tool she uses with the offer in hand, not a question she asks.'),
    (('What-if simulators', 'moon'), ('Hub tools', 'hub'), "A loan's real cost and the safety net runway take her own numbers."),
    (("Home's business notebook", 'pool'), ('Hub, Money in and out', 'hub'), 'Running a business is doing, not reading.'),
    (("The week's question", 'ripple'), ('The feed, pinned', 'ripple'), 'Still there every week; now one post among many.'),
    (('DIVA check-in', 'stones'), ('Stays in Me', 'stones'), 'The Hub only opens a doorway to it. No free calculator (Q-38).'),
]


def glyph(g, size, col, anim=False):
    return hub_icon(None, size, col, 1.6 if size > 40 else 2, anim=anim) if g == 'hub' else icon(g, size, col, 1.6 if size > 40 else 2)


def tab_card(name, g, bg, fg, purpose, holds, new):
    rows = ''.join(f'<span style="display: flex; gap: 10px; align-items: baseline; font-size: 15px; line-height: 1.35"><span aria-hidden="true" style="width: 6px; height: 6px; flex-shrink: 0; border-radius: 999px; background: {EVG}; transform: translateY(-2px)"></span>{h}</span>' for h in holds)
    edge = 'box-shadow: inset 0 0 0 1px #C9D3CE;' if bg == POOL else ''
    return f'''<section class="card" style="gap: 16px; padding: 18px">
      <div style="height: 150px; border-radius: {R_M}px; background: {bg}; color: {fg}; {edge} display: flex; align-items: center; justify-content: center">{glyph(g, 72, fg, anim=True)}</div>
      <span style="display: flex; flex-direction: column; gap: 6px"><span class="d" style="font-size: 34px">{name}</span><span style="font-size: 16px; font-weight: 600">{purpose}</span></span>
      <div style="display: flex; flex-direction: column; gap: 8px">{rows}</div>
      <div style="margin-top: auto; border-top: 1px solid {LINE7}; padding-top: 12px; display: flex; flex-direction: column; gap: 6px"><span class="chip" style="align-self: flex-start; background: {LIME}; color: {EVG}">New in Round 8</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}">{new}</span></div>
    </section>'''


def chip_area(text, g):
    return (f'<span style="display: inline-flex; align-items: center; gap: 8px; min-height: 40px; padding: 0 12px; border-radius: {R_M}px; background: {MIST}; font-size: 14px; font-weight: 600">'
            f'{glyph(g, 18, EVG)}{text}</span>')


def moves():
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 250px 28px 240px minmax(0, 1fr); gap: 12px; align-items: center; padding: 10px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
        <span>{chip_area(a, ga)}</span>
        <span aria-label="moves to" style="display: flex; color: {MUTED}">{icon('send', 20, MUTED)}</span>
        <span>{chip_area(b, gb)}</span>
        <span style="font-size: 14px; line-height: 1.4; color: {SEC}">{why}</span>
      </div>''' for i, ((a, ga), (b, gb), why) in enumerate(MOVES))
    return f'<section class="card" style="gap: 10px"><span class="ktitle">What moved where</span><div>{rows}</div></section>'


def live_bar():
    items = ''
    for j, (name, g) in enumerate(AREAS8):
        if g == 'hub':
            gl = (f'<sc-if value="[[ hubPlay ]]" hint-placeholder-val="[[ true ]]">{hub_icon(None, 20, anim=True)}</sc-if>'
                  f'<sc-if value="[[ hubRest ]]" hint-placeholder-val="[[ false ]]">{hub_icon(None, 20)}</sc-if>')
        else:
            gl = icon(g)
        items += (f'<button onClick="[[ go{j} ]]" aria-pressed="[[ on{j} ]]" style="flex: 1 1 0; height: 64px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; font-size: 12px; color: [[ lc{j} ]]; font-weight: [[ fw{j} ]]; transition: color .2s">'
                  f'<span style="width: 52px; height: 30px; border-radius: 8px; background: [[ pb{j} ]]; color: [[ fg{j} ]]; display: flex; align-items: center; justify-content: center; transition: background-color .2s">{gl}</span>{name}</button>')
    return f'''<section class="card" style="gap: 14px">
      <span class="ktitle">The tab bar (tap it)</span>
      <div style="border-radius: {R_M}px; background: [[ scrBg ]]; padding: 40px 14px 0; transition: background-color .3s">
        <span style="display: block; font-size: 14px; color: [[ scrFg ]]; padding: 0 0 18px 4px; transition: color .3s">[[ scrNote ]]</span>
        <nav aria-label="Demo tab bar" style="display: flex; border-radius: {R_M}px {R_M}px 0 0; background: [[ barBg ]]; box-shadow: 0 -1px 0 [[ barLine ]]; padding: 4px 2px 8px; transition: background-color .3s">{items}</nav>
      </div>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px; line-height: 1.45; color: {SEC}">
        <span><b style="color: {INK}">Learn is night,</b> so the bar turns night with it (Q-30).</span>
        <span><b style="color: {INK}">The keystone drops in once</b> when the Hub opens. It never loops.</span>
        <span><b style="color: {INK}">Labels always show.</b> While she reads, the bar shrinks to its shapes (M5).</span>
        <span><b style="color: {INK}">Ola lives only in Learn and Ask</b>, never in the Hub or next to a result.</span>
      </div>
    </section>'''


def board():
    cards = ''.join(tab_card(*t) for t in TABS)
    body = f'''<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px; align-items: stretch">{cards}</div>
  <div style="display: grid; grid-template-columns: minmax(0, 1.9fr) minmax(0, 1fr); gap: 24px; align-items: start">{moves()}{live_bar()}</div>'''
    notes = ['Home: your goals, this week, and what the Hub thinks is useful now.', 'Learn is night. Paths, Words and Stories live here, with Ola.',
             'The Hub: tools for your job and your business.', 'Community: the feed, circles and member shops.', 'Me: your profile, versions, report and documents.']
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const P = %(pal)s, N = %(notes)s;
    const a = st.a == null ? 2 : st.a, dark = a === 1, replay = !!st.r;
    const v = { scrBg: dark ? '%(night)s' : '%(mist)s', scrFg: dark ? '%(nmuted)s' : '%(sec)s', barBg: dark ? '%(deep)s' : '#FFFFFF', barLine: dark ? '%(nline)s' : '#E1E8E4',
      scrNote: N[a], hubPlay: a === 2 && !replay, hubRest: a !== 2 || replay };
    for (let j = 0; j < 5; j++) {
      const on = a === j;
      v['on' + j] = on; v['fw' + j] = on ? 600 : 400;
      v['pb' + j] = on ? P[j][0] : 'transparent'; v['fg' + j] = on ? P[j][1] : (dark ? '%(nmuted)s' : '%(muted)s');
      v['lc' + j] = on ? (j === 1 ? '%(moon)s' : P[j][2]) : (dark ? '%(nmuted)s' : '%(muted)s');
      v['go' + j] = () => { if (j === 2 && a === 2) this.setState({ r: true }, () => this.setState({ r: false })); else this.setState({ a: j }); };
    }
    return v;
  }
}''' % dict(pal=json.dumps([list(ACTIVE8[n]) for n, _g in AREAS8]), notes=json.dumps(notes), night=NIGHT, mist=MIST, nmuted=NMUTED, sec=SEC,
            deep=DEEP, nline=NLINE, muted=MUTED, moon=MOON)
    desc = ('Five tabs, with the Hub in the centre (D-037). Learn takes the Vault in as Words, and the Hub gathers the tools that were scattered '
            'across Round 7. Each tab keeps one shape and one colour.')
    return with_css(board7('Five tabs, one new centre', desc, body, logic, 1600, 1290), HUB_CSS)


BOARDS = [('R8-IA', board)]
