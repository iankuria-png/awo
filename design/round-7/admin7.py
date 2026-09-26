"""Round 7, batch 5: AWO Admin, for a small non-technical team (desktop, 1440 wide).

Patterns borrowed from the best tools, and why:
- Inbox first (Linear, GitHub): the overview answers "what needs me?" before any chart.
- Maker-checker approvals (banking's four-eyes rule, GitHub reviews): whoever writes a change to results
  text or scoring can't approve it; the reviewer sees a diff, automatic checks and the impact first.
- Preview before publish (Vercel previews): a scoring draft runs against a fixed set of test profiles.
  Past results never change.
- Private by default (Stripe, Okta): sensitive fields stay masked; revealing one needs a reason and is logged.
- Keyboard first (Linear, Superhuman): Cmd+K to jump anywhere; single keys in queues.
- Everything leaves a trail: an audit log, and a log of every AI output.
The approval rule itself is a proposal until Ian decides (Q-34). All names and numbers are samples."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from screens7 import ic, EXTRA_ICONS, mark, R_S, R_M, R_L, LINE7  # noqa: E402

BG, PANEL, EDGE = '#F4F7F5', '#FFFFFF', '#E4EAE6'
ADD_BG, DEL_BG, WINE = '#E3F3EC', '#F7E6EC', BLUSH_2
NB = ' '

EXTRA_ICONS.update({
    'grid': '<rect x="4" y="4" width="7" height="7" rx="1.5"></rect><rect x="13" y="4" width="7" height="7" rx="1.5"></rect><rect x="4" y="13" width="7" height="7" rx="1.5"></rect><rect x="13" y="13" width="7" height="7" rx="1.5"></rect>',
    'book': '<path d="M5 4.5h9a3 3 0 0 1 3 3V20H8a3 3 0 0 1-3-3z"></path><path d="M5 17a3 3 0 0 1 3-3h9"></path>',
    'sliders': '<path d="M5 7h9M18 7h1M5 17h3M12 17h7"></path><circle cx="16" cy="7" r="2"></circle><circle cx="10" cy="17" r="2"></circle>',
    'flag': '<path d="M6 21V4"></path><path d="M6 4h11l-2 4 2 4H6"></path>',
    'clock': '<circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3 2"></path>',
    'chip': '<rect x="7" y="7" width="10" height="10" rx="2"></rect><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"></path>',
    'approve': '<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"></path><path d="m9 12 2.2 2.2L15.5 10"></path>',
    'eye': '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"></path><circle cx="12" cy="12" r="2.8"></circle>',
    'export': '<path d="M12 15V4M7.5 8.5 12 4l4.5 4.5"></path><path d="M5 14v6h14v-6"></path>',
    'filter': '<path d="M4 6h16M7 12h10M10 18h4"></path>',
    'dots': '<circle cx="6" cy="12" r="1.3" fill="currentColor"></circle><circle cx="12" cy="12" r="1.3" fill="currentColor"></circle><circle cx="18" cy="12" r="1.3" fill="currentColor"></circle>',
    'warn': '<path d="M12 4 2.5 20h19z"></path><path d="M12 10v4.5M12 17.5h.01"></path>',
    'info': '<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5.5M12 7.8h.01"></path>',
})

NAV = [
    (None, [('grid', 'Overview', 'R7-Admin-Overview', None), ('people', 'Members', 'R7-Admin-Members', '2')]),
    ('Results', [('book', 'Interpretation library', 'R7-Admin-Approvals', None), ('sliders', 'Scoring', 'R7-Admin-Scoring', None)]),
    ('Content', [('moon', 'Lessons and Vault', 'R7-Admin-Content', None)]),
    ('Community', [('flag', 'Moderation', 'R7-Admin-Moderation', '4')]),
    ('Oversight', [('approve', 'Approvals', 'R7-Admin-Approvals', '3'), ('clock', 'Audit and AI log', 'R7-Admin-Audit', None)]),
]

CSS = f"""
.kbd{{display:inline-flex;align-items:center;justify-content:center;min-width:22px;height:22px;padding:0 6px;box-sizing:border-box;border-radius:{R_S}px;border:1px solid #C9D3CE;background:#FFFFFF;font-size:12px;font-weight:600;color:{SEC}}}
.pn{{background:{PANEL};border-radius:{R_L}px;box-shadow:0 0 0 1px {EDGE}}}
.th{{font-size:12px;font-weight:600;color:{MUTED};text-align:left}}
.st{{height:24px;padding:0 8px;border-radius:{R_S}px;font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}}
.btn{{height:40px;padding:0 14px;border-radius:{R_M}px;font-size:14px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;gap:8px;white-space:nowrap}}
.b1{{background:{EVG};color:#FFFFFF}}
.b2{{background:#FFFFFF;box-shadow:inset 0 0 0 1px #C9D3CE;color:{INK}}}
.b3{{background:#FFFFFF;box-shadow:inset 0 0 0 1px {WINE};color:{WINE}}}
.row{{transition:background-color .12s}}
.row:hover{{background:#F7FAF8}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes paletteIn{{from{{opacity:0;transform:translateY(-8px) scale(.98)}}to{{opacity:1;transform:none}}}}
"""

STATUS = {'Live': (EVG, '#FFFFFF'), 'Approved': (LIME, EVG), 'In review': (POOL, EVG), 'Draft': ('#EEF2EF', SEC),
          'Changes requested': (DEL_BG, WINE), 'Published': (EVG, '#FFFFFF'), 'Retired': ('#EEF2EF', MUTED)}


def st(label, key=None):
    bg, fg = STATUS[key or label]
    return f'<span class="st" style="background: {bg}; color: {fg}">{label}</span>'


def initials(t, bg=POOL, fg=EVG, size=32):
    return f'<span aria-hidden="true" style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: 999px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center; font-size: {max(12, round(size * .38))}px; font-weight: 600">{t}</span>'


def sidebar(active):
    groups = ''
    for g, items in NAV:
        if g:
            groups += f'<span style="font-size: 12px; font-weight: 600; color: {MUTED}; padding: 14px 12px 4px">{g}</span>'
        for icn, label, href, count in items:
            on = label == active
            glyph = icon(icn, 18) if icn == 'moon' else ic(icn, 18)
            badge = f'<span style="margin-left: auto; min-width: 22px; height: 22px; padding: 0 6px; box-sizing: border-box; border-radius: {R_S}px; background: {LIME if on else "#EEF2EF"}; color: {EVG if on else SEC}; font-size: 12px; font-weight: 600; display: flex; align-items: center; justify-content: center">{count}</span>' if count else ''
            cur = ' aria-current="page"' if on else ''
            groups += (f'<a href="{href}.dc.html"{cur} style="height: 40px; padding: 0 12px; border-radius: {R_M}px; display: flex; align-items: center; gap: 10px; font-size: 14px; '
                       f'font-weight: {600 if on else 500}; color: {EVG if on else SEC}; background: {MIST if on else "transparent"}">{glyph}{label}{badge}</a>')
    return f'''<aside style="position: absolute; left: 0; top: 0; bottom: 0; width: 248px; box-sizing: border-box; background: {PANEL}; border-right: 1px solid {EDGE}; padding: 20px 14px; display: flex; flex-direction: column; gap: 2px">
    <div style="display: flex; align-items: center; gap: 8px; padding: 0 8px 16px; color: {EVG}">{mark(28, EVG, LIME)}<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.05em">awo</span><span class="st" style="background: #EEF2EF; color: {SEC}; margin-left: 4px">Admin</span></div>
    <button onClick="[[ openPalette ]]" style="height: 40px; margin-bottom: 8px; padding: 0 8px 0 12px; border-radius: {R_M}px; background: {BG}; box-shadow: inset 0 0 0 1px {EDGE}; display: flex; align-items: center; gap: 8px; font-size: 14px; color: {MUTED}">{icon('search', 16, MUTED)}<span style="flex-grow: 1; text-align: left">Search or jump to</span><span class="kbd">⌘K</span></button>
    {groups}
    <div style="flex-grow: 1"></div>
    <div style="border-radius: {R_M}px; background: {BG}; padding: 10px 12px; display: flex; align-items: center; gap: 8px; font-size: 13px; color: {SEC}">{ic('pin', 16, EVG)}Data region: South Africa</div>
    <div style="display: flex; align-items: center; gap: 10px; padding: 12px 8px 0">{initials('IK', EVG, LIME, 34)}<span style="display: flex; flex-direction: column"><span style="font-size: 14px; font-weight: 600">Ian K.</span><span style="font-size: 12px; color: {MUTED}">Owner</span></span></div>
  </aside>'''


PALETTE = f'''<sc-if value="[[ palette ]]" hint-placeholder-val="[[ false ]]">
    <div style="position: absolute; inset: 0; z-index: 30; background: rgba(16,24,20,.28); animation: fadeIn .15s ease-out both">
      <div role="dialog" aria-label="Search or jump to" style="position: absolute; left: 50%; top: 110px; width: 620px; margin-left: -310px; border-radius: {R_L}px; background: {PANEL}; box-shadow: 0 24px 60px rgba(16,24,20,.25); overflow: hidden; animation: paletteIn .18s cubic-bezier(.2,.8,.2,1) both">
        <div style="height: 56px; display: flex; align-items: center; gap: 10px; padding: 0 16px; border-bottom: 1px solid {EDGE}">{icon('search', 20, MUTED)}<span style="flex-grow: 1; font-size: 16px; color: {INK}">nal<span style="display: inline-block; width: 2px; height: 20px; background: {EVG}; vertical-align: middle; margin-left: 1px"></span></span><button onClick="[[ closePalette ]]" aria-label="Close" style="height: 40px; min-width: 44px; display: flex; align-items: center; justify-content: center"><span class="kbd">Esc</span></button></div>
        <div style="padding: 8px; display: flex; flex-direction: column; gap: 2px">
          <span class="th" style="padding: 8px 10px 4px">Members</span>
          <div style="height: 48px; border-radius: {R_M}px; background: {MIST}; display: flex; align-items: center; gap: 12px; padding: 0 10px">{initials('N', POOL, EVG, 28)}<span style="flex-grow: 1; font-size: 14px"><b>Nal</b>edi <span style="color: {MUTED}">M-4821, South Africa</span></span><span class="kbd">↵</span></div>
          <span class="th" style="padding: 10px 10px 4px">Jump to</span>
          <div style="height: 44px; border-radius: {R_M}px; display: flex; align-items: center; gap: 12px; padding: 0 10px; font-size: 14px">{ic('approve', 18, SEC)}Approvals<span style="margin-left: auto; font-size: 12px; color: {MUTED}">3 waiting</span></div>
          <div style="height: 44px; border-radius: {R_M}px; display: flex; align-items: center; gap: 12px; padding: 0 10px; font-size: 14px">{ic('flag', 18, SEC)}Moderation queue<span style="margin-left: auto; font-size: 12px; color: {MUTED}">4 flagged</span></div>
          <span class="th" style="padding: 10px 10px 4px">Actions</span>
          <div style="height: 44px; border-radius: {R_M}px; display: flex; align-items: center; gap: 12px; padding: 0 10px; font-size: 14px">{ic('export', 18, SEC)}Export the audit log</div>
        </div>
        <div style="height: 40px; border-top: 1px solid {EDGE}; display: flex; align-items: center; gap: 14px; padding: 0 16px; font-size: 12px; color: {MUTED}"><span><span class="kbd">↑</span> <span class="kbd">↓</span> to move</span><span><span class="kbd">↵</span> to open</span><span style="margin-left: auto">Every search is logged</span></div>
      </div>
    </div>
  </sc-if>'''

PALETTE_JS = "palette: !!st.palette, openPalette: () => this.setState({ palette: true }), closePalette: () => this.setState({ palette: false }),"


def page(title, sub, active, actions, main, logic, h=920):
    body = holes(f'''<div style="position: relative; width: 1440px; height: {h}px; background: {BG}; color: {INK}; font-family: 'Geist', ui-sans-serif, system-ui, sans-serif; overflow: hidden">
  {sidebar(active)}
  <div style="position: absolute; left: 248px; right: 0; top: 0; bottom: 0; display: flex; flex-direction: column">
    <header style="height: 76px; flex-shrink: 0; box-sizing: border-box; padding: 0 32px; display: flex; align-items: center; gap: 16px; border-bottom: 1px solid {EDGE}; background: {BG}">
      <span style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1"><h1 style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">{title}</h1><span style="font-size: 13px; color: {MUTED}">{sub}</span></span>
      {actions}<span class="st" style="height: 28px; border: 1px dashed {SEC}; color: {SEC}; background: transparent">Sample data</span>
    </header>
    <main style="flex-grow: 1; min-height: 0; padding: 24px 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px">{main}</main>
  </div>
  {PALETTE}
</div>''')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AWO Admin: {title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{BASE_CSS}{EXTRA_CSS}{CSS}
body{{background:{BG}}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{h}}}}}'>
{logic}
</script>
</body>
</html>
'''


def logic_with(extra_js, loops=''):
    return '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = { %s %s };
%s
    return v;
  }
}''' % (PALETTE_JS, extra_js, loops)


def spark(vals, w, h, col=EVG):
    lo, hi = min(vals), max(vals)
    pts = [(round(i * w / (len(vals) - 1), 1), round(h - 3 - (x - lo) / (hi - lo or 1) * (h - 6), 1)) for i, x in enumerate(vals)]
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display: block; overflow: visible"><path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path><circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="3.5" fill="{col}"></circle></svg>'


# ---------------------------------------------------------------- Overview

INBOX = [('approve', 'Approval', 'Interpretation library v2.2', 'Rewording for "Ready for surprises". Lerato S. wrote it; it needs a second person.', '2 h', 'Review', 'R7-Admin-Approvals', 0),
         ('approve', 'Approval', 'Scoring v1.4, a draft', 'Moves the Stage 2 boundary. The impact preview is ready.', '1 d', 'Review', 'R7-Admin-Scoring', 0),
         ('flag', 'Moderation', '4 posts flagged', 'One reported by members, three flagged by AI. One mentions guaranteed returns.', '35 m', 'Open queue', 'R7-Admin-Moderation', 1),
         ('download', 'Data request', 'Download request from M-4821', 'A member asked for all her data. Received 3 days ago.', '3 d', 'Handle', 'R7-Admin-Members', 2),
         ('moon', 'Content', 'Lesson "Pricing for profit" is ready', 'Drafted with AI help, edited by Ama O. Needs one reviewer.', '5 h', 'Review', 'R7-Admin-Content', 0)]


def overview():
    tabs = ''.join(f'<button onClick="[[ ft{i} ]]" aria-pressed="[[ ftOn{i} ]]" style="height: 40px; padding: 0 12px; border-radius: 8px; background: [[ ftBg{i} ]]; box-shadow: [[ ftSh{i} ]]; font-size: 13px; font-weight: 600; color: [[ ftFg{i} ]]">{t}</button>' for i, t in enumerate(['All 5', 'Approvals 2', 'Community 1', 'Requests 1']))
    items = ''
    for k, (icn, kind, t, d, age, act, href, grp) in enumerate(INBOX):
        glyph = icon(icn, 18, EVG) if icn == 'moon' else ic(icn, 18, EVG)
        items += f'''<sc-if value="[[ show{k} ]]" hint-placeholder-val="[[ true ]]"><div class="row" style="display: flex; align-items: center; gap: 14px; padding: 14px 18px; border-top: 1px solid {EDGE}">
          <span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: {R_M}px; background: {MIST}; display: flex; align-items: center; justify-content: center">{glyph}</span>
          <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 12px; font-weight: 600; color: {MUTED}">{kind}</span><span style="font-size: 15px; font-weight: 600">{t}</span></span><span style="font-size: 13px; color: {SEC}">{d}</span></span>
          <span style="font-size: 12px; color: {MUTED}; width: 36px; text-align: right">{age}</span>
          <a href="{href}.dc.html" class="btn {'b1' if k < 2 else 'b2'}" style="min-width: 108px">{act}</a></div></sc-if>'''
    kpis = [('Active members this week', '1' + NB + '284', '+6% on last week', [980, 1010, 1060, 1120, 1150, 1210, 1284]),
            ('Check-ins done this week', '70%', '148 of 212 due', [58, 61, 66, 63, 68, 69, 70]),
            ('Chose a first step', '81%', '+3 points on last week', [72, 74, 75, 78, 77, 79, 81]),
            ('Lessons finished', '3' + NB + '906', '+11% on last week', [2400, 2650, 2900, 3100, 3350, 3600, 3906])]
    ktiles = ''.join(f'<div class="pn" style="padding: 16px 18px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; color: {SEC}">{t}</span><span style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 28px; font-weight: 600; letter-spacing: -0.03em; font-variant-numeric: tabular-nums">{v}</span><span style="font-size: 12px; font-weight: 600; color: {EVG}">{d}</span></span>{spark(s, 96, 36)}</span></div>' for t, v, d, s in kpis)
    weeks = [96, 104, 118, 111, 125, 131, 128, 139, 142, 136, 144, 148]
    bars = ''.join(f'<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="font-size: 12px; color: {INK if k == 11 else "transparent"}; font-weight: 600">{w}</span><span style="width: 100%; max-width: 30px; height: {round(w / 160 * 150)}px; border-radius: 4px 4px 0 0; background: {EVG if k == 11 else "#BFD9D2"}"></span><span style="font-size: 12px; color: {MUTED}">{"W" + str(k + 1) if k % 2 == 0 or k == 11 else ""}</span></div>' for k, w in enumerate(weeks))
    stages = [('Stage 1', 312), ('Stage 2', 604), ('Stage 3', 281), ('Stage 4', 87)]
    sbars = ''.join(f'<div style="display: flex; align-items: center; gap: 12px"><span style="width: 64px; font-size: 13px; color: {SEC}">{n}</span><span style="flex-grow: 1; height: 14px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="display: block; height: 100%; width: {round(c / 604 * 100)}%; background: {EVG}"></span></span><span style="width: 40px; text-align: right; font-size: 13px; font-weight: 600; font-variant-numeric: tabular-nums">{c}</span></div>' for n, c in stages)
    system = [('Scoring', st('v1.3 live', 'Live'), 'since 1 Sep'), ('Interpretation library', st('v2.1 live', 'Live'), 'since 14 Aug'), ('AI features', st('On, with guard rails', 'Approved'), '3 features'), ('Last audit export', '<span style="font-size: 14px; font-weight: 600">1 Sep</span>', 'by Ian K.')]
    sys_rows = ''.join(f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 0; {f"border-top: 1px solid {EDGE};" if i else ""}"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 600">{t}</span><span style="font-size: 12px; color: {MUTED}">{s}</span></span>{c}</div>' for i, (t, c, s) in enumerate(system))
    main = f'''<div style="display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 20px; align-items: start">
      <section class="pn" style="overflow: hidden">
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px 18px">
          <span style="display: flex; align-items: baseline; gap: 10px"><span style="font-size: 17px; font-weight: 600">Needs you</span><span style="font-size: 13px; color: {MUTED}">Oldest first within a day</span></span>
          <div role="group" aria-label="Filter" style="display: flex; gap: 4px; padding: 3px; border-radius: {R_M}px; background: {BG}">{tabs}</div></div>
        {items}
      </section>
      <section class="pn" style="padding: 6px 18px 8px"><span style="display: block; font-size: 17px; font-weight: 600; padding: 12px 0 4px">What's live</span>{sys_rows}
        <div style="display: flex; align-items: center; gap: 8px; padding: 12px 0 8px; border-top: 1px solid {EDGE}; font-size: 13px; color: {SEC}">{ic('pin', 16, EVG)}All data and backups in South Africa</div></section>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px">{ktiles}</div>
    <div style="display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 20px">
      <section class="pn" style="padding: 18px; display: flex; flex-direction: column; gap: 14px"><span style="display: flex; justify-content: space-between"><span style="font-size: 17px; font-weight: 600">Check-ins completed, last 12 weeks</span><span style="font-size: 13px; color: {MUTED}">Members, not money</span></span><div role="img" aria-label="Check-ins completed each week, rising from 96 to 148" style="display: flex; gap: 8px; align-items: flex-end; height: 190px">{bars}</div></section>
      <section class="pn" style="padding: 18px; display: flex; flex-direction: column; gap: 14px"><span style="font-size: 17px; font-weight: 600">Where members are</span><div style="display: flex; flex-direction: column; gap: 12px">{sbars}</div><span style="font-size: 12px; color: {MUTED}">Stages describe learning readiness. Counts only; no one is ranked.</span></section>
    </div>'''
    actions = f'<button onClick="[[ openPalette ]]" class="btn b2">{icon("search", 16, INK)}Jump to<span class="kbd">⌘K</span></button>'
    logic = logic_with('', '''    const f = st.f || 0, grp = %s;
    for (let i = 0; i < 4; i++) { v['ft' + i] = () => this.setState({ f: i }); v['ftOn' + i] = f === i; v['ftBg' + i] = f === i ? '#FFFFFF' : 'transparent'; v['ftSh' + i] = f === i ? '0 1px 3px rgba(16,24,20,.12)' : 'none'; v['ftFg' + i] = f === i ? '%s' : '%s'; }
    for (let k = 0; k < grp.length; k++) v['show' + k] = f === 0 || grp[k] === f - 1;''' % (json.dumps([g for *_x, g in INBOX]), INK, MUTED))
    return page('Good morning, Ian', 'Thursday 25 September. 5 things need you.', 'Overview', actions, main, logic, h=1000)


# ---------------------------------------------------------------- Approvals: an interpretation change, reviewed

DIFF = [('Ready for surprises, stage 2',
         'A surprise cost would likely knock your plans off course.', 'An unexpected cost could knock your plans off course right now.',
         'Building a cushion for surprises is the next thing to learn.', 'A small cushion, built a little at a time, is the next thing to learn about.'),
        ('Ready for surprises, stage 3',
         'You could cover a small surprise, but a large one would be hard.', 'You could cover a small surprise. A larger one would still be hard.',
         None, None)]


def approvals():
    queue = [('Interpretation library v2.2', 'Lerato S.', 'In review', True), ('Scoring v1.4', 'Kagiso D.', 'In review', False), ('Vault: 12 new words', 'Ama O.', 'In review', False)]
    qhtml = ''.join(f'<a href="{"R7-Admin-Scoring.dc.html" if "Scoring" in t else "#"}" style="display: flex; flex-direction: column; gap: 6px; padding: 14px 16px; border-radius: {R_M}px; background: {MIST if on else "transparent"}; box-shadow: {f"inset 3px 0 0 {EVG}" if on else "none"}"><span style="font-size: 14px; font-weight: 600">{t}</span><span style="display: flex; align-items: center; gap: 8px; font-size: 12px; color: {MUTED}">{st(s)}by {a}</span></a>' for t, a, s, on in queue)
    blocks = ''
    for name, old1, new1, old2, new2 in DIFF:
        lines = f'<div style="display: flex; gap: 10px; padding: 6px 10px; background: {DEL_BG}; border-radius: {R_S}px"><span style="color: {WINE}; font-weight: 700; width: 12px">−</span><span style="color: {WINE}; text-decoration: line-through; text-decoration-color: rgba(107,43,64,.4)">{old1}</span></div><div style="display: flex; gap: 10px; padding: 6px 10px; background: {ADD_BG}; border-radius: {R_S}px"><span style="color: {EVG}; font-weight: 700; width: 12px">+</span><span style="color: {EVG_D}">{new1}</span></div>'
        if old2:
            lines += f'<div style="display: flex; gap: 10px; padding: 6px 10px; background: {DEL_BG}; border-radius: {R_S}px"><span style="color: {WINE}; font-weight: 700; width: 12px">−</span><span style="color: {WINE}; text-decoration: line-through; text-decoration-color: rgba(107,43,64,.4)">{old2}</span></div><div style="display: flex; gap: 10px; padding: 6px 10px; background: {ADD_BG}; border-radius: {R_S}px"><span style="color: {EVG}; font-weight: 700; width: 12px">+</span><span style="color: {EVG_D}">{new2}</span></div>'
        blocks += f'<div class="pn" style="padding: 16px 18px; display: flex; flex-direction: column; gap: 8px"><span style="display: flex; justify-content: space-between"><span style="font-size: 14px; font-weight: 600">{name}</span><span style="font-size: 12px; color: {MUTED}">Shown on Me, the reveal and the report</span></span><div style="display: flex; flex-direction: column; gap: 4px; font-size: 14px; line-height: 1.5">{lines}</div></div>'
    checks = [('ok', 'Plain words', 'Reads at about grade 6. The target is grade 8 or below.'),
              ('ok', 'No advice words', 'No "you should", "buy", "switch to" or "invest in".'),
              ('ok', 'Complete', 'Every stage and dimension still has text.'),
              ('warn', 'Translation', 'English only for now. Other languages follow launch.')]
    chtml = ''.join(f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 10px 0; {f"border-top: 1px solid {EDGE};" if i else ""}"><span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: {R_S}px; background: {LIME if k == "ok" else "#EEF2EF"}; display: flex; align-items: center; justify-content: center">{icon("check", 13, EVG, 3) if k == "ok" else ic("warn", 13, SEC, 2.4)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 600">{t}</span><span style="font-size: 13px; line-height: 1.4; color: {SEC}">{d}</span></span></div>' for i, (k, t, d) in enumerate(checks))
    main = f'''<div style="display: grid; grid-template-columns: 250px minmax(0, 1fr) 330px; gap: 20px; align-items: start; min-height: 0">
      <section class="pn" style="padding: 8px; display: flex; flex-direction: column; gap: 2px"><span class="th" style="padding: 8px 8px 6px">Waiting for review</span>{qhtml}</section>
      <div style="display: flex; flex-direction: column; gap: 14px">
        <div style="display: flex; align-items: center; gap: 12px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em">Interpretation library v2.2</span><span class="st" style="background: [[ stBg ]]; color: [[ stFg ]]">[[ stLabel ]]</span></div>
        <div style="display: flex; gap: 18px; font-size: 13px; color: {SEC}"><span>Proposed by <b style="color: {INK}">Lerato S.</b>, content lead</span><span>2 entries changed</span><span>Applies to new results only</span></div>
        <div role="tablist" style="display: flex; gap: 20px; border-bottom: 1px solid {EDGE}">{"".join(f'<span role="tab" aria-selected="{"true" if i == 0 else "false"}" style="height: 40px; display: flex; align-items: center; font-size: 14px; font-weight: 600; color: {INK if i == 0 else MUTED}; box-shadow: {f"inset 0 -2px 0 {EVG}" if i == 0 else "none"}">{t}</span>' for i, t in enumerate(["Changes", "Where it shows", "History"]))}</div>
        {blocks}
        <div class="pn" style="padding: 14px 18px; display: flex; gap: 12px; align-items: center"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: {R_M}px; background: {POOL}; display: flex; align-items: center; justify-content: center">{ic('eye', 18, EVG)}</span><span style="flex-grow: 1; font-size: 14px; line-height: 1.45">Preview it as a member sees it: <b>Me</b>, the <b>result reveal</b> and the <b>one-page report</b>.</span><a href="R7-Reveal.dc.html" class="btn b2">Open preview</a></div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 16px">
        <section class="pn" style="padding: 8px 18px"><span style="display: block; font-size: 15px; font-weight: 600; padding: 10px 0 2px">Automatic checks</span>{chtml}</section>
        <section class="pn" style="padding: 16px 18px; display: flex; flex-direction: column; gap: 12px">
          <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Approvals</span><span style="font-size: 13px; color: {MUTED}">[[ approvedCount ]] of 2</span></span>
          <div style="display: flex; align-items: center; gap: 10px">{initials('LS', '#EEF2EF', SEC)}<span style="flex-grow: 1; font-size: 14px">Lerato S. <span style="color: {MUTED}">wrote this, so can't approve it</span></span></div>
          <div style="display: flex; align-items: center; gap: 10px">{initials('AO', LIME, EVG)}<span style="flex-grow: 1; font-size: 14px">Ama O. <span style="color: {MUTED}">approved, 1 h ago</span></span>{icon('check', 18, EVG, 2.6)}</div>
          <div style="display: flex; align-items: center; gap: 10px">{initials('IK', EVG, LIME)}<span style="flex-grow: 1; font-size: 14px">You <span style="color: {MUTED}">[[ youState ]]</span></span><sc-if value="[[ youDone ]]" hint-placeholder-val="[[ false ]]">{icon('check', 18, EVG, 2.6)}</sc-if></div>
          <sc-if value="[[ deciding ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 8px">
            <label for="ap-note" style="font-size: 13px; font-weight: 600">A note for Lerato <span style="font-weight: 400; color: {MUTED}">(needed to ask for changes)</span></label>
            <textarea id="ap-note" onInput="[[ typeNote ]]" rows="2" placeholder="What should change, and why" style="border: 0; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 10px 12px; font: inherit; font-size: 14px; resize: none"></textarea>
            <div style="display: flex; gap: 8px"><button onClick="[[ approve ]]" class="btn b1" style="flex: 1 1 0">{icon('check', 16, '#FFFFFF', 2.6)}Approve</button><button onClick="[[ changes ]]" class="btn b3" style="flex: 1 1 0">Request changes</button></div></div></sc-if>
          <sc-if value="[[ approved ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 8px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both"><span style="font-size: 13px; line-height: 1.45; color: {SEC}">Two approvals. It goes live for new results when you publish; results already given keep v2.1.</span><button class="btn b1">Publish v2.2</button></div></sc-if>
          <sc-if value="[[ sentBack ]]" hint-placeholder-val="[[ false ]]"><span style="font-size: 13px; line-height: 1.45; color: {WINE}; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">Sent back to Lerato with your note. Nothing changes for members.</span></sc-if>
          <sc-if value="[[ needNote ]]" hint-placeholder-val="[[ false ]]"><span style="font-size: 13px; color: {WINE}">Add a note so Lerato knows what to change.</span></sc-if>
        </section>
        <span style="display: flex; gap: 8px; align-items: flex-start; font-size: 12px; line-height: 1.45; color: {MUTED}">{ic('info', 14, MUTED)}Proposal (Q-34): two people approve results text and scoring; the author never approves their own change. Lessons and Vault words need one reviewer.</span>
      </div>
    </div>'''
    logic = logic_with('', '''    const d = st.d || 0, note = st.note || '';
    v.deciding = d === 0 || d === 3; v.approved = d === 1; v.sentBack = d === 2; v.needNote = d === 3;
    v.typeNote = (e) => this.setState({ note: e.target.value, d: d === 3 ? 0 : d });
    v.approve = () => this.setState({ d: 1 }); v.changes = () => this.setState({ d: note.trim() ? 2 : 3 });
    v.approvedCount = d === 1 ? 2 : 1; v.youDone = d === 1;
    v.youState = d === 1 ? 'approved, just now' : (d === 2 ? 'asked for changes' : 'your review is needed');
    v.stLabel = d === 1 ? 'Approved' : (d === 2 ? 'Changes requested' : 'In review');
    v.stBg = d === 1 ? '%s' : (d === 2 ? '%s' : '%s'); v.stFg = d === 1 ? '%s' : (d === 2 ? '%s' : '%s');''' % (LIME, DEL_BG, POOL, EVG, WINE, EVG))
    actions = f'<a href="R7-Admin-Audit.dc.html" class="btn b2">{ic("clock", 16, INK)}History</a>'
    return page('Approvals', 'Changes to what members see as results need two people.', 'Approvals', actions, main, logic, h=1000)


# ---------------------------------------------------------------- Scoring: a draft version and its impact

WEIGHTS = [('Financial Health', 'Everyday money', 40, 40), ('Risk and Resilience', 'Ready for surprises', 25, 25), ('Capital Positioning', 'Knowing your options', 20, 20), ('Goal Clarity', 'Clear goals', 15, 15)]
BOUNDS = [('Stage 1', '0 to 44', '0 to 47'), ('Stage 2', '45 to 64', '48 to 64'), ('Stage 3', '65 to 79', '65 to 79'), ('Stage 4', '80 to 100', '80 to 100')]
BEFORE, AFTER = [41, 98, 47, 14], [53, 86, 47, 14]


def scoring():
    wrows = ''.join(f'<div style="display: grid; grid-template-columns: minmax(0, 1.6fr) 1fr 1fr; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid {EDGE}"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 600">{n}</span><span style="font-size: 12px; color: {MUTED}">Members see "{s}"</span></span><span style="font-size: 14px; font-variant-numeric: tabular-nums">{a}%</span><span style="font-size: 14px; font-variant-numeric: tabular-nums; color: {MUTED}">{b}%, unchanged</span></div>' for n, s, a, b in WEIGHTS)
    brows = ''.join(f'<div style="display: grid; grid-template-columns: minmax(0, 1.6fr) 1fr 1fr; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid {EDGE}; {f"background: {ADD_BG}; margin: 0 -18px; padding-left: 18px; padding-right: 18px;" if a != b else ""}"><span style="font-size: 14px; font-weight: 600">{n}</span><span style="font-size: 14px; font-variant-numeric: tabular-nums; {f"color: {WINE}; text-decoration: line-through;" if a != b else ""}">{a}</span><span style="font-size: 14px; font-weight: {600 if a != b else 400}; font-variant-numeric: tabular-nums; color: {EVG if a != b else MUTED}">{b}{"" if a != b else ", unchanged"}</span></div>' for n, a, b in BOUNDS)
    hist = ''.join(f'''<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 8px">
          <span style="height: 150px; display: flex; align-items: flex-end; gap: 6px"><span style="width: 26px; height: {round(b / 100 * 140)}px; border-radius: 4px 4px 0 0; background: #BFD9D2"></span><span style="width: 26px; height: [[ h{i} ]]px; border-radius: 4px 4px 0 0; background: {EVG}; transition: height .5s cubic-bezier(.2,.8,.2,1)"></span></span>
          <span style="font-size: 13px; font-weight: 600">Stage {i + 1}</span><span style="font-size: 12px; color: {MUTED}; font-variant-numeric: tabular-nums">{b} to [[ a{i} ]]</span></div>''' for i, b in enumerate(BEFORE))
    steps = [('Draft', 'Kagiso D. changed one boundary', True), ('Preview on test profiles', 'Run it before anyone reviews', None), ('Two approvals', 'Neither can be Kagiso', False), ('Publish', 'New check-ins only, from the date you choose', False)]
    shtml = ''
    for i, (t, d, state) in enumerate(steps):
        if state is True:
            dot = f'background: {EVG};'
        elif state is None:
            dot = f'background: [[ pvDot ]]; border: 2px solid {EVG};'
        else:
            dot = 'border: 2px solid #C9D3CE;'
        tick = icon('check', 12, '#FFFFFF', 3) if state is True else ''
        line = f'<span style="flex-grow: 1; width: 2px; background: {EDGE}; margin: 2px 0"></span>' if i < 3 else ''
        shtml += (f'<div style="display: flex; gap: 12px"><span style="display: flex; flex-direction: column; align-items: center"><span style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 999px; {dot} display: flex; align-items: center; justify-content: center">{tick}</span>{line}</span>'
                  f'<span style="display: flex; flex-direction: column; gap: 2px; padding-bottom: 16px"><span style="font-size: 14px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {SEC}">{d}</span></span></div>')
    main = f'''<div style="display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 20px; align-items: start">
      <div style="display: flex; flex-direction: column; gap: 16px">
        <div style="display: flex; align-items: center; gap: 12px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em">Scoring v1.4</span>{st('Draft')}<span style="font-size: 13px; color: {MUTED}">compared with</span>{st('v1.3 live', 'Live')}</div>
        <section class="pn" style="padding: 6px 18px 4px"><div class="th" style="display: grid; grid-template-columns: minmax(0, 1.6fr) 1fr 1fr; gap: 12px; padding: 10px 0">Dimension<span>Weight in v1.3</span><span>Weight in v1.4</span></div>{wrows}</section>
        <section class="pn" style="padding: 6px 18px 4px; overflow: hidden"><div class="th" style="display: grid; grid-template-columns: minmax(0, 1.6fr) 1fr 1fr; gap: 12px; padding: 10px 0">Stage<span>DIVA score in v1.3</span><span>DIVA score in v1.4</span></div>{brows}</section>
        <section class="pn" style="padding: 18px; display: flex; flex-direction: column; gap: 14px">
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600">Impact on the 200 test profiles</span><span style="font-size: 13px; color: {SEC}">Made-up profiles, fixed for every preview. Real members are never used.</span></span><button onClick="[[ run ]]" class="btn b1">{ic('sliders', 16, '#FFFFFF')}[[ runLabel ]]</button></div>
          <div role="img" aria-label="[[ histLabel ]]" style="display: flex; gap: 12px; padding: 4px 20px 0">{hist}</div>
          <sc-if value="[[ ran ]]" hint-placeholder-val="[[ false ]]"><div style="border-radius: {R_M}px; background: {BG}; padding: 12px 14px; display: flex; gap: 10px; align-items: flex-start; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{ic('info', 18, EVG)}<span style="font-size: 14px; line-height: 1.45"><b>12 of 200</b> test profiles would move from Stage 2 to Stage 1. None move up. The same answers always give the same result.</span></div></sc-if>
          <span style="display: flex; gap: 14px; font-size: 12px; color: {MUTED}"><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: #BFD9D2"></span>v1.3</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: {EVG}"></span>v1.4</span></span>
        </section>
      </div>
      <div style="display: flex; flex-direction: column; gap: 16px">
        <section class="pn" style="padding: 16px 18px"><span style="display: block; font-size: 15px; font-weight: 600; padding-bottom: 14px">Before it goes live</span>{shtml}<button class="btn b2" style="width: 100%" aria-disabled="true">Send for approval</button></section>
        <section class="pn" style="padding: 16px 18px; display: flex; gap: 10px; align-items: flex-start">{ic('lock', 18, EVG)}<span style="font-size: 13px; line-height: 1.5; color: {SEC}"><b style="color: {INK}">Results never change after they're given.</b> v1.4 applies to new check-ins once published. Every result records the version that made it.</span></section>
        <section class="pn" style="padding: 16px 18px; display: flex; gap: 10px; align-items: flex-start">{ic('warn', 18, SEC)}<span style="font-size: 13px; line-height: 1.5; color: {SEC}">Weights and boundaries here are samples. The real scoring method is AWO's to supply.</span></section>
      </div>
    </div>'''
    logic = logic_with('', '''    const ran = !!st.ran, before = %s, after = %s;
    v.ran = ran; v.run = () => this.setState({ ran: true }); v.runLabel = ran ? 'Run again' : 'Run the preview'; v.pvDot = ran ? '%s' : 'transparent';
    v.histLabel = ran ? 'Test profiles per stage, v1.3 against v1.4: stage 1 from 41 to 53, stage 2 from 98 to 86, stages 3 and 4 unchanged' : 'Test profiles per stage in v1.3';
    for (let i = 0; i < 4; i++) { const n = ran ? after[i] : before[i]; v['h' + i] = ran ? Math.round(n / 100 * 140) : 0; v['a' + i] = ran ? n : '?'; }''' % (BEFORE, AFTER, EVG))
    actions = f'<button class="btn b2">{ic("clock", 16, INK)}Versions</button>'
    return page('Scoring', 'Deterministic and versioned. Drafts are previewed on test profiles before review.', 'Scoring', actions, main, logic, h=1130)


# ---------------------------------------------------------------- Members, with a data request

MEMBERS = [('Naledi', 'M-4821', 'South Africa', '2 Jul', 'Stage 2', 'Today', 'Download request'),
           ('Wanjiru', 'M-4790', 'Kenya', '28 Jun', 'Stage 2', 'Yesterday', ''),
           ('Amara', 'M-4655', 'United Kingdom', '11 Jun', 'Stage 3', '3 days ago', ''),
           ('Thandi', 'M-4512', 'South Africa', '30 May', 'Stage 3', 'Today', ''),
           ('Lindiwe', 'M-4499', 'South Africa', '29 May', 'Stage 1', '31 days ago', 'Inactive'),
           ('Zodwa', 'M-4380', 'Botswana', '21 May', 'Stage 2', 'Today', ''),
           ('Adaeze', 'M-4307', 'United Kingdom', '14 May', 'Stage 4', '2 days ago', ''),
           ('Grace', 'M-4211', 'South Africa', '2 May', 'Stage 3', 'Today', 'Circle host')]


def members():
    filters = ''.join(f'<button onClick="[[ mf{i} ]]" aria-pressed="[[ mfOn{i} ]]" class="btn" style="height: 40px; background: [[ mfBg{i} ]]; color: [[ mfFg{i} ]]; box-shadow: inset 0 0 0 1px [[ mfBd{i} ]]">{t}</button>' for i, t in enumerate(['All', 'New 46', 'Data requests 2', 'Inactive 131']))
    rows = ''
    for k, (n, mid, c, j, s, last, tag) in enumerate(MEMBERS):
        tg = f'<span class="st" style="background: {DEL_BG if "request" in tag else "#EEF2EF"}; color: {WINE if "request" in tag else SEC}">{tag}</span>' if tag else ''
        rows += f'''<button onClick="[[ sel{k} ]]" aria-pressed="[[ selOn{k} ]]" class="row" style="display: grid; grid-template-columns: minmax(0, 1.4fr) 1fr 0.8fr 0.8fr 1fr 1.2fr; gap: 12px; align-items: center; width: 100%; min-height: 52px; padding: 0 18px; border-top: 1px solid {EDGE}; text-align: left; background: [[ selBg{k} ]]; box-shadow: [[ selSh{k} ]]">
          <span style="display: flex; align-items: center; gap: 10px">{initials(n[0], POOL, EVG, 30)}<span style="display: flex; flex-direction: column"><span style="font-size: 14px; font-weight: 600">{n}</span><span style="font-size: 12px; color: {MUTED}; font-variant-numeric: tabular-nums">{mid}</span></span></span>
          <span style="font-size: 14px">{c}</span><span style="font-size: 14px; color: {SEC}">{j}</span><span style="font-size: 14px">{s}</span><span style="font-size: 14px; color: {SEC}">{last}</span><span>{tg}</span></button>'''
    main = f'''<div style="display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: 20px; align-items: start">
      <div style="display: flex; flex-direction: column; gap: 14px">
        <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap"><label style="height: 44px; width: 240px; border-radius: {R_M}px; background: {PANEL}; box-shadow: inset 0 0 0 1px {EDGE}; display: flex; align-items: center; gap: 8px; padding: 0 12px; color: {MUTED}">{icon('search', 16, MUTED)}<input placeholder="Name or member ID" style="border: 0; background: transparent; font-size: 14px; flex-grow: 1; min-width: 0; height: 42px"></label>{filters}</div>
        <section class="pn" style="overflow: hidden"><div class="th" style="display: grid; grid-template-columns: minmax(0, 1.4fr) 1fr 0.8fr 0.8fr 1fr 1.2fr; gap: 12px; padding: 12px 18px">Member<span>Lives in</span><span>Joined</span><span>Stage</span><span>Last active</span><span>Needs</span></div>{rows}</section>
        <span style="font-size: 12px; color: {MUTED}">First names only in lists. Stages describe learning readiness. Amounts members enter never appear here.</span>
      </div>
      <section class="pn" style="padding: 20px; display: flex; flex-direction: column; gap: 16px">
        <div style="display: flex; align-items: center; gap: 12px">{initials('N', POOL, EVG, 48)}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 18px; font-weight: 600">[[ pName ]]</span><span style="font-size: 13px; color: {MUTED}">[[ pId ]], joined [[ pJoined ]]</span></span></div>
        <div style="display: flex; flex-direction: column; gap: 0">
          <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-top: 1px solid {EDGE}"><span style="font-size: 13px; color: {MUTED}">Mobile number</span><span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums">[[ phone ]]</span><sc-if value="[[ masked ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ askReveal ]]" class="btn b2" style="height: 40px; padding: 0 12px; font-size: 13px">{ic('eye', 14, INK)}Reveal</button></sc-if></span></div>
          <div style="display: flex; justify-content: space-between; padding: 10px 0; border-top: 1px solid {EDGE}"><span style="font-size: 13px; color: {MUTED}">Signed in with</span><span style="font-size: 14px">Phone number</span></div>
          <div style="display: flex; justify-content: space-between; padding: 10px 0; border-top: 1px solid {EDGE}"><span style="font-size: 13px; color: {MUTED}">Consents</span><span style="font-size: 14px; text-align: right">AI explanations on<br>Research off</span></div>
          <div style="display: flex; justify-content: space-between; padding: 10px 0; border-top: 1px solid {EDGE}"><span style="font-size: 13px; color: {MUTED}">Answers and amounts</span><span style="display: flex; align-items: center; gap: 6px; font-size: 14px">{icon('lock', 14, SEC)}Hidden</span></div>
        </div>
        <sc-if value="[[ hasRequest ]]" hint-placeholder-val="[[ true ]]"><div style="border-radius: {R_M}px; background: {DEL_BG}; padding: 14px; display: flex; flex-direction: column; gap: 10px">
          <span style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: {WINE}">{ic('download', 16, WINE)}She asked for all her data</span>
          <span style="font-size: 13px; line-height: 1.45; color: {INK}">Received 3 days ago. The export includes every version of her profile, her answers and her consents.</span>
          <button onClick="[[ prep ]]" class="btn b1" style="align-self: flex-start">[[ prepLabel ]]</button></div></sc-if>
        <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 14px; font-weight: 600">Recent</span>
          {''.join(f'<div style="display: flex; gap: 10px; font-size: 13px; line-height: 1.4"><span style="width: 64px; flex-shrink: 0; color: {MUTED}">{d}</span><span>{t}</span></div>' for d, t in [('Today', 'Asked for a download of her data'), ('13 Sep', 'Check-in: version 3 made with scoring v1.3'), ('2 Sep', 'Finished lesson 6, Savings groups'), ('13 Aug', 'Check-in: version 2 made with scoring v1.3')])}</div>
      </section>
    </div>
    <sc-if value="[[ revealing ]]" hint-placeholder-val="[[ false ]]"><div style="position: absolute; inset: 0; z-index: 25; background: rgba(16,24,20,.28); animation: fadeIn .15s ease-out both">
      <div role="dialog" aria-label="Why do you need to see this?" style="position: absolute; left: 50%; top: 220px; width: 460px; margin-left: -230px; border-radius: {R_L}px; background: {PANEL}; padding: 22px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 24px 60px rgba(16,24,20,.25); animation: paletteIn .18s cubic-bezier(.2,.8,.2,1) both">
        <span style="font-size: 18px; font-weight: 600">Why do you need to see this?</span>
        <span style="font-size: 14px; line-height: 1.45; color: {SEC}">Revealing a number is logged with your name and reason, and the member can see it in her history.</span>
        {''.join(f'<button onClick="[[ why{i} ]]" aria-pressed="[[ whyOn{i} ]]" style="min-height: 44px; padding: 0 14px; border-radius: {R_M}px; box-shadow: inset 0 0 0 [[ whyBw{i} ]]px {EVG}; background: {BG}; text-align: left; font-size: 14px; font-weight: 500">{t}</button>' for i, t in enumerate(['Handling her data request', 'She contacted support', 'Something else']))}
        <div style="display: flex; gap: 8px; justify-content: flex-end"><button onClick="[[ cancelReveal ]]" class="btn b2">Cancel</button><button onClick="[[ doReveal ]]" class="btn b1">Reveal and log it</button></div>
      </div></div></sc-if>'''
    ms = [[n, mid, j, bool(tag and 'request' in tag)] for n, mid, c, j, s, last, tag in MEMBERS]
    logic = logic_with('', '''    const ms = %s;
    const sel = st.sel || 0, m = ms[sel], f = st.f || 0, why = st.why == null ? 0 : st.why;
    const shown = !!st.shown && sel === 0;
    v.pName = m[0]; v.pId = m[1]; v.pJoined = m[2]; v.hasRequest = m[3];
    v.masked = !shown; v.phone = shown ? '+27 82 123 4567' : '+27 82 \\u2022\\u2022\\u2022 \\u2022\\u202267';
    v.askReveal = () => this.setState({ revealing: true }); v.cancelReveal = () => this.setState({ revealing: false });
    v.doReveal = () => this.setState({ revealing: false, shown: true }); v.revealing = !!st.revealing;
    v.prep = () => this.setState({ prep: true }); v.prepLabel = st.prep ? 'Export ready: send it to her' : 'Prepare the export';
    for (let i = 0; i < 3; i++) { v['why' + i] = () => this.setState({ why: i }); v['whyOn' + i] = why === i; v['whyBw' + i] = why === i ? 2 : 0; }
    for (let k = 0; k < ms.length; k++) { v['sel' + k] = () => this.setState({ sel: k }); v['selOn' + k] = sel === k; v['selBg' + k] = sel === k ? '%s' : 'transparent'; v['selSh' + k] = sel === k ? 'inset 3px 0 0 %s' : 'none'; }
    for (let i = 0; i < 4; i++) { v['mf' + i] = () => this.setState({ f: i }); v['mfOn' + i] = f === i; v['mfBg' + i] = f === i ? '%s' : '#FFFFFF'; v['mfFg' + i] = f === i ? '#FFFFFF' : '%s'; v['mfBd' + i] = f === i ? '%s' : '%s'; }''' % (json.dumps(ms), MIST, EVG, EVG, INK, EVG, EDGE))
    actions = f'<button class="btn b2">{ic("export", 16, INK)}Export list</button>'
    return page('Members', '1 284 members. Private by default: sensitive fields need a reason to reveal.', 'Members', actions, main, logic, h=920)


# ---------------------------------------------------------------- Moderation queue

QUEUE = [('ai', 'Guaranteed returns', 'Side hustles', 'Sibongile', '12 m', 'Join my group! Put in R 1 000 and get R 3 000 back in 2 weeks, guaranteed. DM me, only 5 spots.', 'The post promises a guaranteed return and a deadline. Both are on the red-flag list.'),
         ('member', 'Reported as unkind', 'Safety net', 'Nomsa', '35 m', "If you can't save R 500 a month you're just not trying hard enough.", 'Two members reported it as unkind.'),
         ('ai', 'Shares a phone number', 'Stokvel treasurers', 'Beatrice', '1 h', 'Anyone in Soweto who wants to join, call me on 071 555 0123.', 'Personal phone numbers in public posts can be misused.'),
         ('ai', 'Mentions a specific product', 'Safety net', 'Palesa', '2 h', 'Which bank account is best for a safety net? I heard one pays more interest.', 'Might invite product recommendations, which AWO avoids.')]


def moderation():
    items = ''
    for k, (src, why, circle, who, age, _text, _r) in enumerate(QUEUE):
        tag = f'<span class="st" style="background: {"#EEF2EF" if src == "ai" else DEL_BG}; color: {SEC if src == "ai" else WINE}">{"AI flag" if src == "ai" else "Member report"}</span>'
        items += f'''<button onClick="[[ pick{k} ]]" aria-pressed="[[ pOn{k} ]]" style="display: flex; flex-direction: column; gap: 6px; padding: 12px 14px; border-radius: {R_M}px; text-align: left; background: [[ pBg{k} ]]; box-shadow: [[ pSh{k} ]]; opacity: [[ pOp{k} ]]">
          <span style="display: flex; justify-content: space-between; align-items: center">{tag}<span style="font-size: 12px; color: {MUTED}">{age}</span></span>
          <span style="font-size: 14px; font-weight: 600">{why}</span><span style="font-size: 12px; color: {MUTED}">{who} in {circle}</span>
          <sc-if value="[[ doneT{k} ]]" hint-placeholder-val="[[ false ]]"><span style="font-size: 12px; font-weight: 600; color: {EVG}">[[ outcome{k} ]]</span></sc-if></button>'''
    reasons = ''.join(f'<span class="st" style="height: 28px; background: {BG}; color: {SEC}; box-shadow: inset 0 0 0 1px {EDGE}">{r}</span>' for r in ['Scam signs', 'Unkind', 'Personal details', 'Product promotion'])
    main = f'''<div style="display: grid; grid-template-columns: 300px minmax(0, 1fr) 300px; gap: 20px; align-items: start">
      <section class="pn" style="padding: 8px; display: flex; flex-direction: column; gap: 4px"><span class="th" style="padding: 8px 8px 4px">[[ left ]] left in the queue</span>{items}</section>
      <div style="display: flex; flex-direction: column; gap: 14px">
        <section class="pn" style="padding: 20px; display: flex; flex-direction: column; gap: 14px">
          <div style="display: flex; align-items: center; gap: 12px">{initials('[[ initial ]]', BLUSH, BLUSH_INK, 40)}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">[[ who ]]</span><span style="font-size: 13px; color: {MUTED}">In [[ circle ]], [[ age ]] ago. First post flagged.</span></span></div>
          <p style="font-size: 18px; line-height: 1.5; border-left: 3px solid {BLUSH}; padding-left: 14px">[[ text ]]</p>
          <div style="border-radius: {R_M}px; background: {BG}; padding: 12px 14px; display: flex; gap: 10px; align-items: flex-start">{ic('chip', 18, SEC)}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; font-weight: 600">[[ srcLabel ]]</span><span style="font-size: 14px; line-height: 1.45; color: {SEC}">[[ reason ]]</span></span></div>
        </section>
        <section class="pn" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 12px">
          <span style="font-size: 14px; font-weight: 600">Decide</span>
          <div style="display: flex; gap: 8px"><button onClick="[[ keep ]]" class="btn b2" style="flex: 1 1 0">Keep<span class="kbd">K</span></button><button onClick="[[ hide ]]" class="btn b2" style="flex: 1 1 0">Hide<span class="kbd">H</span></button><button onClick="[[ remove ]]" class="btn b3" style="flex: 1.4 1 0">Remove and tell her why<span class="kbd">R</span></button></div>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center"><span style="font-size: 12px; color: {MUTED}">Reason she will see:</span>{reasons}</div>
          <span style="font-size: 12px; color: {MUTED}"><span class="kbd">J</span> <span class="kbd">K</span> move between posts. AI only flags; a person always decides.</span>
        </section>
        <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div role="status" style="height: 48px; border-radius: {R_M}px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 14px; font-size: 14px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both"><span style="width: 24px; height: 24px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 14, EVG, 3)}</span>[[ toastText ]]<button onClick="[[ undo ]]" style="margin-left: auto; height: 40px; padding: 0 10px; font-weight: 600; color: {LIME}">Undo</button></div></sc-if>
      </div>
      <div style="display: flex; flex-direction: column; gap: 16px">
        <section class="pn" style="padding: 16px 18px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 15px; font-weight: 600">Community rules</span>
          {''.join(f'<span style="display: flex; gap: 8px; font-size: 13px; line-height: 1.45; color: {SEC}"><span style="color: {EVG}">{icon("check", 14, EVG, 2.6)}</span>{r}</span>' for r in ['Share your own story, not advice to buy or switch.', 'No promises of returns, and no recruiting.', 'First names only. No phone numbers or addresses.', 'Kind, even when you disagree.'])}</section>
        <section class="pn" style="padding: 16px 18px; display: flex; flex-direction: column; gap: 8px"><span style="font-size: 15px; font-weight: 600">This week</span>
          <span style="display: flex; justify-content: space-between; font-size: 13px"><span style="color: {SEC}">AI flags a person agreed with</span><b>31 of 40</b></span>
          <span style="display: flex; justify-content: space-between; font-size: 13px"><span style="color: {SEC}">Median time to decide</span><b>22 min</b></span>
          <span style="font-size: 12px; color: {MUTED}">Low agreement means the flags need tuning, not faster clicking.</span></section>
      </div>
    </div>'''
    qs = [[who[0], who, circle, age, text, r, 'Flagged by AI' if src == 'ai' else 'Reported by members'] for src, why, circle, who, age, text, r in QUEUE]
    logic = logic_with('', '''    const qs = %s;
    const cur = st.cur || 0, done = st.done || {};
    const q = qs[cur];
    v.initial = q[0]; v.who = q[1]; v.circle = q[2]; v.age = q[3]; v.text = q[4]; v.reason = q[5]; v.srcLabel = q[6];
    v.left = qs.length - Object.keys(done).length;
    const act = (label, msg) => { const d = Object.assign({}, done); d[cur] = label; let n = cur; for (let i = 1; i <= qs.length; i++) { const j = (cur + i) %% qs.length; if (!(j in d)) { n = j; break; } } this.setState({ done: d, cur: n, toast: msg, last: cur }); };
    v.keep = () => act('Kept', 'Kept. The flag is closed.'); v.hide = () => act('Hidden', 'Hidden while you look into it.'); v.remove = () => act('Removed', 'Removed. She was told why.');
    v.toast = !!st.toast; v.toastText = st.toast || ''; v.undo = () => { const d = Object.assign({}, done); delete d[st.last]; this.setState({ done: d, cur: st.last, toast: '' }); };
    for (let k = 0; k < qs.length; k++) {
      v['pick' + k] = () => this.setState({ cur: k }); v['pOn' + k] = cur === k; v['pBg' + k] = cur === k ? '%s' : 'transparent';
      v['pSh' + k] = cur === k ? 'inset 3px 0 0 %s' : 'none'; v['pOp' + k] = (k in done) ? .55 : 1; v['doneT' + k] = k in done; v['outcome' + k] = done[k] || '';
    }''' % (json.dumps(qs), MIST, EVG))
    actions = '<span style="display: flex; gap: 6px; align-items: center; font-size: 13px; color: ' + MUTED + '"><span class="kbd">J</span><span class="kbd">K</span>next and previous</span>'
    return page('Moderation', '4 flagged posts. AI flags, people decide, and members are told why.', 'Moderation', actions, main, logic, h=900)


# ---------------------------------------------------------------- Lessons and Vault content

CARDS = {
    'Draft': [('Pricing for profit', 'Lesson', 'Ama O.', True), ('Credit record', 'Vault word', 'Kagiso D.', True)],
    'In review': [('Where to keep a safety net', 'Lesson', 'Lerato S.', False), ('Remittance fee', 'Vault word', 'Ama O.', True), ('Float', 'Vault word', 'Ama O.', False)],
    'Changes requested': [('Your first payslip, part 2', 'Lesson', 'Lerato S.', False)],
    'Published': [('Savings groups', 'Lesson', 'Lerato S.', False), ('Stokvel', 'Vault word', 'Ama O.', False), ('Interest', 'Vault word', 'Kagiso D.', False)],
}


def content():
    tabs = ''.join(f'<button onClick="[[ ct{i} ]]" aria-pressed="[[ ctOn{i} ]]" style="height: 40px; padding: 0 14px; border-radius: 8px; background: [[ ctBg{i} ]]; box-shadow: [[ ctSh{i} ]]; font-size: 13px; font-weight: 600">{t}</button>' for i, t in enumerate(['Everything', 'Lessons', 'Vault words']))
    cols = ''
    for c, cards in CARDS.items():
        chtml = ''
        for t, kind, who, ai in cards:
            key = 'L' if kind == 'Lesson' else 'W'
            chtml += f'''<sc-if value="[[ show{key} ]]" hint-placeholder-val="[[ true ]]"><div class="pn" style="padding: 14px; display: flex; flex-direction: column; gap: 10px">
              <span style="display: flex; justify-content: space-between; align-items: center"><span style="display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600; color: {MUTED}">{icon("moon" if kind == "Lesson" else "arch", 14, MUTED)}{kind}</span>{f'<span class="st" style="border: 1px dashed {EVG}; color: {EVG}; background: transparent">AI-drafted</span>' if ai else ''}</span>
              <span style="font-size: 15px; font-weight: 600; line-height: 1.3">{t}</span>
              <span style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 8px; font-size: 12px; color: {SEC}">{initials("".join(p[0] for p in who.replace(".", "").split()), "#EEF2EF", SEC, 24)}{who}</span>{f'<span class="st" style="background: {EVG}; color: #FFFFFF">{icon("check", 11, "#FFFFFF", 3)}Reviewed by AWO</span>' if c == "Published" else ''}</span>
            </div></sc-if>'''
        if c == 'Changes requested':
            chtml += f'<sc-if value="[[ noWords ]]" hint-placeholder-val="[[ false ]]"><div style="border-radius: {R_L}px; border: 1.5px dashed #C9D3CE; padding: 18px 14px; font-size: 13px; color: {MUTED}; text-align: center">No words waiting on changes.</div></sc-if>'
        cols += f'<div style="display: flex; flex-direction: column; gap: 10px; min-width: 0"><span style="display: flex; align-items: center; gap: 8px; padding: 0 2px">{st(c)}<span style="font-size: 13px; color: {MUTED}">{len(cards)}</span></span>{chtml}</div>'
    main = f'''<div style="display: flex; justify-content: space-between; align-items: center"><div role="group" aria-label="Show" style="display: flex; gap: 4px; padding: 3px; border-radius: {R_M}px; background: {PANEL}; box-shadow: inset 0 0 0 1px {EDGE}">{tabs}</div>
      <span style="font-size: 13px; color: {MUTED}">One reviewer for lessons and words. AI drafts are labelled until a person rewrites and approves them.</span></div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; align-items: start">{cols}</div>'''
    logic = logic_with('', '''    const t = st.t || 0;
    v.showL = t !== 2; v.showW = t !== 1; v.noWords = t === 2;
    for (let i = 0; i < 3; i++) { v['ct' + i] = () => this.setState({ t: i }); v['ctOn' + i] = t === i; v['ctBg' + i] = t === i ? '%s' : 'transparent'; v['ctSh' + i] = t === i ? 'inset 0 0 0 1px %s' : 'none'; }''' % (MIST, EDGE))
    actions = f'<button class="btn b1">{icon("moon", 16, "#FFFFFF")}New lesson</button><button class="btn b2">{icon("arch", 16, INK)}New word</button>'
    return page('Lessons and Vault', 'Draft, review, publish. Only published content says "Reviewed by AWO".', 'Lessons and Vault', actions, main, logic, h=760)


# ---------------------------------------------------------------- Audit log and AI log

AUDIT = [('09:42', 'Ian K.', 'Approved', 'Interpretation library v2.2', 'Second approval. Author: Lerato S.'),
         ('09:15', 'Kagiso D.', 'Revealed a phone number', 'Member M-4821', 'Reason: handling her data request'),
         ('08:58', 'Ama O.', 'Hid a post', 'Side hustles circle', 'Reason shown to author: scam signs'),
         ('Yesterday', 'System', 'Published', 'Scoring v1.3 stays live', 'Scheduled check, nothing changed'),
         ('Yesterday', 'Lerato S.', 'Sent for review', 'Lesson "Where to keep a safety net"', 'Reviewer: Ama O.'),
         ('22 Sep', 'Ian K.', 'Exported', 'Audit log, August', 'CSV, 1 412 rows')]
AILOG = [('09:40', 'Explain more simply', 'Member M-4655', 'AWO-reviewed text v2.1, stage 3', 'Shown, labelled AI-assisted', 'Kept'),
         ('09:31', 'Check an offer', 'Member M-4790', 'Red-flag list v1.2', 'Found 3 signs; no verdict given', 'Member read it'),
         ('09:12', 'Moderation flag', 'Post in Side hustles', 'Red-flag list v1.2', 'Flagged: guaranteed returns', 'Person agreed'),
         ('08:47', 'Content draft', 'Lesson "Pricing for profit"', 'Style guide v3', 'Draft for Ama O.', 'Rewritten, in review')]


def audit():
    tabs = ''.join(f'<button onClick="[[ at{i} ]]" aria-pressed="[[ atOn{i} ]]" role="tab" style="height: 44px; min-width: 64px; padding: 0 4px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; color: [[ atFg{i} ]]; box-shadow: [[ atSh{i} ]]">{t}</button>' for i, t in enumerate(['Audit log', 'AI log']))
    arows = ''.join(f'<div class="row" style="display: grid; grid-template-columns: 90px 130px 190px minmax(0, 1fr) minmax(0, 1fr); gap: 14px; align-items: center; min-height: 52px; padding: 0 18px; border-top: 1px solid {EDGE}; font-size: 14px"><span style="color: {MUTED}; font-variant-numeric: tabular-nums">{t}</span><span style="display: flex; align-items: center; gap: 8px">{initials("S" if w == "System" else "".join(p[0] for p in w.replace(".", "").split()), "#EEF2EF", SEC, 24)}{w}</span><span style="font-weight: 600">{a}</span><span>{o}</span><span style="color: {SEC}">{d}</span></div>' for t, w, a, o, d in AUDIT)
    irows = ''.join(f'<div class="row" style="display: grid; grid-template-columns: 70px 160px 170px minmax(0, 1fr) minmax(0, 1fr) 150px; gap: 14px; align-items: center; min-height: 52px; padding: 0 18px; border-top: 1px solid {EDGE}; font-size: 14px"><span style="color: {MUTED}; font-variant-numeric: tabular-nums">{t}</span><span style="font-weight: 600">{f}</span><span style="color: {SEC}">{who}</span><span>{src}</span><span>{out}</span><span class="st" style="background: {LIME if "agreed" in res or "Kept" in res else "#EEF2EF"}; color: {EVG if "agreed" in res or "Kept" in res else SEC}; justify-self: start">{res}</span></div>' for t, f, who, src, out, res in AILOG)
    main = f'''<div role="tablist" style="display: flex; gap: 24px; border-bottom: 1px solid {EDGE}; margin-top: -8px">{tabs}</div>
    <div style="display: flex; gap: 8px; align-items: center"><label style="height: 44px; width: 280px; border-radius: {R_M}px; background: {PANEL}; box-shadow: inset 0 0 0 1px {EDGE}; display: flex; align-items: center; gap: 8px; padding: 0 12px; color: {MUTED}">{icon('search', 16, MUTED)}<input placeholder="Person, action or object" style="border: 0; background: transparent; font-size: 14px; flex-grow: 1; min-width: 0; height: 42px"></label>{''.join(f'<button class="btn b2" style="height: 40px">{t}{icon("chev", 14, MUTED)}</button>' for t in ['Anyone', 'Any action', 'Last 7 days'])}</div>
    <sc-if value="[[ a0 ]]" hint-placeholder-val="[[ true ]]"><section class="pn" style="overflow: hidden"><div class="th" style="display: grid; grid-template-columns: 90px 130px 190px minmax(0, 1fr) minmax(0, 1fr); gap: 14px; padding: 12px 18px">When<span>Who</span><span>Did</span><span>To</span><span>Details</span></div>{arows}</section>
      <span style="font-size: 12px; color: {MUTED}">Entries can't be edited or deleted. Each one records who, what, when and why.</span></sc-if>
    <sc-if value="[[ a1 ]]" hint-placeholder-val="[[ false ]]"><section class="pn" style="overflow: hidden"><div class="th" style="display: grid; grid-template-columns: 70px 160px 170px minmax(0, 1fr) minmax(0, 1fr) 150px; gap: 14px; padding: 12px 18px">When<span>Feature</span><span>For</span><span>Based on</span><span>What it did</span><span>Outcome</span></div>{irows}</section>
      <span style="font-size: 12px; color: {MUTED}">Every AI output is kept with the source it was allowed to use. AI never scores, picks a stage or recommends a product.</span></sc-if>'''
    logic = logic_with('', '''    const a = st.a || 0;
    for (let i = 0; i < 2; i++) { v['a' + i] = a === i; v['at' + i] = () => this.setState({ a: i }); v['atOn' + i] = a === i; v['atFg' + i] = a === i ? '%s' : '%s'; v['atSh' + i] = a === i ? 'inset 0 -2px 0 %s' : 'none'; }''' % (INK, MUTED, EVG))
    actions = f'<button class="btn b2">{ic("export", 16, INK)}Export CSV</button>'
    return page('Audit and AI log', 'Who did what, when and why, plus every AI output and the source it used.', 'Audit and AI log', actions, main, logic, h=720)


BOARDS = [('R7-Admin-Overview', overview), ('R7-Admin-Approvals', approvals), ('R7-Admin-Scoring', scoring), ('R7-Admin-Members', members),
          ('R7-Admin-Moderation', moderation), ('R7-Admin-Content', content), ('R7-Admin-Audit', audit)]
