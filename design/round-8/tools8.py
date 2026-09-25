"""Round 8, batch 3: the "Me" tools, each on the six-beat skeleton (hub8.skeleton).
Writes R8-Tool-Payslip, R8-Tool-Payday, R8-Tool-Debt, R8-Tool-Fees and R8-Tool-Statement. Sample member: Naledi,
employed in Johannesburg. Every figure is a sample; tax figures follow the 2026/27 tables as a sample (Q-41)."""
import json

from lib8 import *  # noqa: F401,F403
from learn8 import PHONE_CSS

TOOL_CSS = """
.beat{font-size:13px;font-weight:600;color:#56625C;display:flex;align-items:center;gap:8px;margin-bottom:-6px}
.card8{border-radius:14px;background:#FFFFFF;padding:16px;display:flex;flex-direction:column;gap:12px}
.rng8{-webkit-appearance:none;appearance:none;width:100%;height:44px;background:transparent;margin:0}
.rng8::-webkit-slider-runnable-track{height:8px;border-radius:2px;background:linear-gradient(to right,#0F4A36 0,#0F4A36 var(--p),#DCE4DF var(--p))}
.rng8::-webkit-slider-thumb{-webkit-appearance:none;width:30px;height:30px;margin-top:-11px;border-radius:6px;background:#D8F36A;box-shadow:0 0 0 3px #0F4A36}
.rng8:focus-visible{outline:2px solid #0F4A36;outline-offset:4px}
@keyframes barIn{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes shimmer{from{background-position:100% 0}to{background-position:0 0}}
.sk{background:linear-gradient(90deg,#E4ECE7 0,#F3F7F5 40%,#E4ECE7 80%);background-size:300% 100%;animation:shimmer 1.4s linear infinite;border-radius:6px}
"""
REVIEWED = f'<span class="chip" style="background: {EVG}; color: #FFFFFF">{icon("check", 14, "#FFFFFF", 2.6)}Reviewed by AWO</span>'
AI_CHIP = f'<span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span>'


def tool_head(title, mode, back_href='R8-Hub.dc.html'):
    return (f'<header style="display: flex; align-items: center; gap: 10px">'
            f'<a href="{back_href}" aria-label="Back to the Hub" style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic("back", 20, INK, 2.2)}</a>'
            f'<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; color: {MUTED}">{hub_icon(None, 14, MUTED)}Hub, {mode}</span><span style="font-size: 18px; font-weight: 600">{title}</span></span>'
            f'{sample_chip()}</header>')


def beat(text, g):
    return f'<span class="beat">{ic8(g, 16, MUTED)}{text}</span>'


def means(text):
    return (f'{beat("What it means", "check")}<section class="card8"><p style="font-size: 16px; line-height: 1.5">{text}</p>'
            f'<span style="display: flex; gap: 6px">{REVIEWED}</span></section>')


def learn_this(lesson, mins, words, href='R7-Lesson.dc.html'):
    chips = ''.join(f'<a href="R8-Words-Decoder.dc.html" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {MIST}; display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600">{icon("arch", 16, EVG)}{w}</a>' for w in words)
    return (f'{beat("Learn this", "moon")}<section class="card8">'
            f'<a href="{href}" style="min-height: 56px; border-radius: {R_M}px; background: {NIGHT}; color: {MOON}; padding: 0 14px; display: flex; align-items: center; gap: 12px">{moon(24, "half", now=True)}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{lesson}</span><span style="font-size: 13px; color: {NMUTED}">A lesson in Learn, {mins} minutes</span></span>{icon("play", 16, LIME)}</a>'
            f'<div style="display: flex; flex-wrap: wrap; gap: 8px">{chips}</div></section>')


def make_goal(title, sub, href, g='pool', label='Open'):
    return (f'{beat("Make it a goal or a step", "stones")}'
            f'<a href="{href}" style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px 16px; display: flex; align-items: center; gap: 12px">'
            f'<span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {EVG}; color: {LIME}; display: flex; align-items: center; justify-content: center">{ic8(g, 22)}</span>'
            f'<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{title}</span><span style="font-size: 13px; line-height: 1.35; color: {MUTED}">{sub}</span></span>'
            f'<span style="height: 44px; flex-shrink: 0; white-space: nowrap; padding: 0 14px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 14px; font-weight: 600; display: flex; align-items: center">{label}</span></a>')


def milestone(text, circle='Safety net circle', face='naledi'):
    return (f'{beat("Share a milestone", "ripple")}'
            f'<section class="card8" style="background: {BLUSH}; color: {BLUSH_INK}">'
            f'<span style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG[face]}" alt="" style="width: 36px; height: 36px"><span style="font-size: 17px; font-weight: 600; line-height: 1.3">{text}</span></span>'
            f'<span style="font-size: 13px">Amounts are never shared.</span>'
            f'<sc-if value="[[ notShared ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ share ]]" style="height: 48px; width: 100%; border-radius: {R_M}px; background: {BLUSH_INK}; color: #FFFFFF; font-size: 15px; font-weight: 600">Share with your {circle}</button></sc-if>'
            f'<sc-if value="[[ shared ]]" hint-placeholder-val="[[ false ]]"><span style="height: 48px; display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600; animation: rise .3s cubic-bezier(.2,.8,.2,1) both"><span style="width: 32px; height: 32px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon("check", 18, BLUSH_INK, 2.8)}</span>Shared. Your circle can cheer it.</span></sc-if>'
            f'</section>')


SHARE_JS = "shared: !!st.shared, notShared: !st.shared, share: () => this.setState({ shared: true }),"


def foot(text):
    return f'<p style="font-size: 13px; line-height: 1.5; color: {MUTED}; padding: 0 2px">{text}</p>'


def result(label, big_hole, sub_hole, extra=''):
    return (f'{beat("One plain result", "pool")}<section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">'
            f'<span style="font-size: 14px; font-weight: 600">{label}</span><span class="d" style="font-size: 56px; font-variant-numeric: tabular-nums">[[ {big_hole} ]]</span>'
            f'<span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ {sub_hole} ]]</span>{extra}</section>')


def tool_page(title, body, logic, h, mode='Me', back='R8-Hub.dc.html', css=''):
    page = f'''  <div class="scr" style="gap: 16px">
    {tool_head(title, mode, back)}
{body}
  </div>
  {tabbar8('Hub')}'''
    return with_css(phone(title, page, logic, h=h), PHONE_CSS + HUB_CSS + TOOL_CSS + css)


def rands_js():
    return "const R = (n) => 'R\\u00a0' + Math.round(n).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, '\\u00a0');"


# ---------------------------------------------------------------- Payslip decoder

GROSS = 18500
LINES = [('Basic salary', 18500.00, 'earn', 'What you earned this month, before anything comes off. Also called gross pay.'),
         ('Pension fund', 1387.50, 'pension', 'Still your money: it goes into your pension fund, and it lowers the tax you pay.'),
         ('PAYE (income tax)', 1595.25, 'tax', "Income tax, paid to SARS for you. It's worked out as if this month's pay were your pay all year."),
         ('UIF', 177.12, 'uif', '1% of your pay, up to R 177,12. It can pay you for a while if you lose your job, or on maternity leave.'),
         ('Medical aid', 1250.00, 'med', 'Your share of medical aid. Some employers pay a part too; your contract says.'),
         ('Net pay', 14090.13, 'net', 'What reaches your account. Also called take-home pay.')]
SEGS = [('Pension', 1388, EVG, '#FFFFFF'), ('PAYE', 1595, '#3E7A63', '#FFFFFF'), ('Medical aid', 1250, '#8DBFAE', INK), ('UIF', 177, '#C9E2DA', INK)]


def fmt_r(v, cents=True):
    whole = int(v)
    s = f'{whole:,}'.replace(',', NB)
    return f'R{NB}{s},{round((v - whole) * 100):02d}' if cents else f'R{NB}{s}'


def payslip():
    rows = ''
    for i, (n, v, k, why) in enumerate(LINES):
        sign = '' if k in ('earn', 'net') else '−'
        rows += f'''<div style="{"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <div style="min-height: 56px; display: flex; align-items: center; gap: 10px">
            <button role="checkbox" aria-checked="[[ ok{i} ]]" onClick="[[ tick{i} ]]" aria-label="{n} is right" style="width: 44px; height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center"><span style="width: 24px; height: 24px; border-radius: {R_S}px; background: [[ okBg{i} ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center; transition: background-color .18s">{icon("check", 16, "#FFFFFF", 3)}</span></button>
            <button onClick="[[ why{i} ]]" aria-expanded="[[ whyOn{i} ]]" style="flex-grow: 1; min-height: 44px; display: flex; align-items: center; justify-content: space-between; gap: 8px; text-align: left"><span style="font-size: 15px; font-weight: {600 if k in ("earn", "net") else 500}">{n}</span><span style="font-size: 15px; font-weight: 600; font-variant-numeric: tabular-nums; white-space: nowrap">{sign}{fmt_r(v)}</span></button>
          </div>
          <sc-if value="[[ whyOn{i} ]]" hint-placeholder-val="[[ false ]]"><p style="margin: 0 0 12px 54px; font-size: 14px; line-height: 1.45; color: {SEC}; animation: rise .25s cubic-bezier(.2,.8,.2,1) both">{why}</p></sc-if>
        </div>'''
    total_off = sum(s[1] for s in SEGS)
    bar = ''.join(f'<span style="height: 36px; flex: {v} 1 0; min-width: 8px; background: {c}; box-shadow: inset 0 0 0 [[ segBw{j} ]]px {LIME}; transform-origin: 0 0; animation: barIn .6s cubic-bezier(.2,.8,.2,1) {0.2 + j * 0.08:.2f}s both"></span>' for j, (n, v, c, _f) in enumerate(SEGS))
    legend = ''.join(f'<button onClick="[[ seg{j} ]]" aria-pressed="[[ segOn{j} ]]" style="min-height: 44px; padding: 0 10px 0 8px; border-radius: 8px; background: [[ segBg{j} ]]; display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; transition: background-color .18s"><span style="width: 12px; height: 12px; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(16,24,20,.25)"></span>{n} {fmt_r(v, False)}</button>' for j, (n, v, c, _f) in enumerate(SEGS))
    raises = ''.join(f'<button onClick="[[ ra{j} ]]" aria-pressed="[[ raOn{j} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: [[ raBg{j} ]]; color: [[ raFg{j} ]]; font-size: 14px; font-weight: 600">{fmt_r(r, False)}</button>' for j, r in enumerate((500, 1000, 2000)))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8">
      <div style="display: flex; gap: 12px; align-items: center">
        <span aria-hidden="true" style="width: 56px; height: 72px; flex-shrink: 0; border-radius: {R_S}px; background: {MIST}; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 8px 7px; box-sizing: border-box; display: flex; flex-direction: column; gap: 5px">
          <span style="height: 5px; width: 70%; border-radius: 2px; background: #9FB0A8"></span><span style="height: 4px; border-radius: 2px; background: #C9D3CE"></span><span style="height: 4px; border-radius: 2px; background: #C9D3CE"></span><span style="height: 4px; width: 80%; border-radius: 2px; background: #C9D3CE"></span><span style="height: 4px; border-radius: 2px; background: #C9D3CE"></span><span style="height: 5px; width: 60%; border-radius: 2px; background: {EVG}"></span></span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><span style="display: flex; gap: 6px; align-items: center"><span style="font-size: 15px; font-weight: 600">Read from your photo</span>{AI_CHIP}</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">September payslip. Tick each line if it matches. Nothing counts until you do.</span></span>
      </div>
      <div style="display: flex; flex-direction: column">{rows}</div>
      <span style="display: flex; gap: 8px; align-items: flex-start; font-size: 13px; line-height: 1.45; color: {SEC}; background: {MIST}; border-radius: {R_M}px; padding: 10px 12px">{ic8('pin', 16, EVG)}Read in South Africa. The photo is deleted once you've checked it; only your ticked lines stay. Sample policy (Q-37).</span>
    </section>
    <sc-if value="[[ locked ]]" hint-placeholder-val="[[ false ]]"><section class="card8" style="align-items: center; text-align: center; animation: rise .3s cubic-bezier(.2,.8,.2,1) both"><span style="font-size: 16px; font-weight: 600">[[ lockText ]]</span><span style="font-size: 14px; color: {MUTED}">AWO only works with lines you've checked.</span></section></sc-if>
    <sc-if value="[[ unlocked ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: rise .35s cubic-bezier(.2,.8,.2,1) both">
    {result('You take home', 'net', 'netSub', f'<div aria-hidden="true" style="display: flex; gap: 3px; margin-top: 8px; border-radius: {R_S}px; overflow: hidden">{bar}</div><div role="group" aria-label="Where R 4 410 went: tap a part" style="display: flex; flex-wrap: wrap; gap: 4px; margin-left: -8px">{legend}</div><p style="font-size: 15px; line-height: 1.45; color: {INK}; min-height: 44px; border-top: 1px solid rgba(15,74,54,.2); padding-top: 10px">[[ segText ]]</p>')}
    <section class="card8">
      <span style="font-size: 16px; font-weight: 600">A raise, in real terms</span>
      <div role="group" aria-label="Raise before tax" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {MIST}">{raises}</div>
      <p style="font-size: 16px; line-height: 1.45"><b>[[ raiseNet ]] more</b> would reach you each month. [[ raiseRest ]]</p>
      <span style="font-size: 12px; color: {MUTED}">An illustration with sample 2026/27 tables.</span>
    </section>
    <section class="card8" style="gap: 8px">
      <span style="font-size: 16px; font-weight: 600">Not on this payslip</span>
      <span style="font-size: 15px; line-height: 1.45; color: {SEC}">Your leave balance, and what your employer adds to your pension. Both are worth asking for.</span>
    </section>
    {means("Of every R 100 you earn, about R 76 reaches your account. R 7,50 is saved for you in your pension. The rest pays for tax, medical aid and UIF.")}
    {learn_this('Your first payslip', 4, ['PAYE', 'UIF', 'Gross pay', 'Net pay'])}
    {make_goal('Plan this R 14 090', 'Give every rand a job, family included', 'R8-Tool-Payday.dc.html', 'calc', 'Plan it')}
    {milestone('Naledi can read her payslip now.')}
    </div></sc-if>
    {foot("Payslip decoder, version 0.1. Sample tax tables for 2026/27, checked 1 March 2026 (Q-41). In Kenya you'd see SHIF, NSSF and the Housing Levy instead of UIF.")}'''
    seg_text = [nbs(f'Pension {fmt_r(1388, False)}: ' + LINES[1][3]), nbs(f'PAYE {fmt_r(1595, False)}: ' + LINES[2][3]),
                nbs(f'Medical aid {fmt_r(1250, False)}: ' + LINES[4][3]), nbs(f'UIF {fmt_r(177, False)}: ' + LINES[3][3])]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const ok = st.ok || [true, true, true, true, true, true];
    const n = ok.filter(Boolean).length;
    const seg = st.seg == null ? -1 : st.seg, ra = st.ra == null ? 1 : st.ra;
    const SEG = %(segs)s, RA = [500, 1000, 2000];
    const v = { %(share)s
      locked: n < 6, unlocked: n === 6, lockText: 'Tick ' + (6 - n) + ' more ' + (6 - n === 1 ? 'line' : 'lines') + ' to see your result',
      net: R(14090), netSub: 'of ' + R(%(gross)d) + '. Tap a part to see where ' + R(%(off)d) + ' went.',
      segText: seg < 0 ? 'Pension, PAYE, medical aid and UIF came off. Tap one.' : SEG[seg],
      raiseNet: R(RA[ra] * 0.7585), raiseRest: 'Of a ' + R(RA[ra]) + ' raise, ' + R(RA[ra] * 0.075) + ' goes to your pension and the rest to tax.'
    };
    for (let i = 0; i < 6; i++) {
      v['ok' + i] = ok[i]; v['okBg' + i] = ok[i] ? '%(evg)s' : '#FFFFFF';
      v['tick' + i] = () => { const o = ok.slice(); o[i] = !o[i]; this.setState({ ok: o }); };
      v['whyOn' + i] = st.why === i; v['why' + i] = () => this.setState({ why: st.why === i ? -1 : i });
    }
    for (let j = 0; j < 4; j++) { v['seg' + j] = () => this.setState({ seg: j }); v['segOn' + j] = seg === j; v['segBw' + j] = seg === j ? 3 : 0; v['segBg' + j] = seg === j ? 'rgba(255,255,255,.7)' : 'transparent'; }
    for (let j = 0; j < 3; j++) { v['ra' + j] = () => this.setState({ ra: j }); v['raOn' + j] = ra === j; v['raBg' + j] = ra === j ? '%(evg)s' : 'transparent'; v['raFg' + j] = ra === j ? '#FFFFFF' : '%(ink)s'; }
    return v;
  }
}''' % dict(R=rands_js(), segs=json.dumps(seg_text, ensure_ascii=False), share=SHARE_JS, gross=GROSS, off=total_off, evg=EVG, ink=INK)
    return tool_page('Payslip decoder', body, logic, h=2560)


# ---------------------------------------------------------------- Pay-day plan

NEEDS = [('Rent', 4500), ('Food', 2200), ('Transport', 1400), ('Electricity', 500), ('Phone and data', 300)]
FAMILY = [('Mama, every month', 1500), ("Lerato's school fees", 800)]
GOALS = [('Moving out', 1000), ('Safety net', 500)]


def payday():
    need_rows = ''.join(f'<span style="display: flex; justify-content: space-between; font-size: 15px; min-height: 32px; align-items: center"><span>{n}</span><span style="font-variant-numeric: tabular-nums">{fmt_r(v, False)}</span></span>' for n, v in NEEDS)
    fam_rows = ''.join(f'<span style="display: flex; justify-content: space-between; font-size: 15px; min-height: 32px; align-items: center"><span>{n}</span><span style="font-variant-numeric: tabular-nums">{fmt_r(v, False)}</span></span>' for n, v in FAMILY)

    def stepper(key, label):
        return (f'<span style="display: flex; align-items: center; gap: 6px"><button onClick="[[ {key}Down ]]" aria-label="Less for {label}" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {MIST}; font-size: 22px; font-weight: 500">−</button>'
                f'<span style="min-width: 88px; text-align: center; font-size: 20px; font-weight: 600; letter-spacing: -0.02em; font-variant-numeric: tabular-nums">[[ {key}Amt ]]</span>'
                f'<button onClick="[[ {key}Up ]]" aria-label="More for {label}" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {MIST}; font-size: 22px; font-weight: 500">+</button></span>')
    jars = [('Needs', 'home', POOL, EVG, 'needW'), ('Family', 'people', BLUSH, BLUSH_INK, 'famW'), ('Goals', 'pool', EVG, LIME, 'goalW'), ('Yours to spend', 'heart', LIME, EVG, 'freeW')]
    bar = ''.join(f'<span style="height: 44px; width: [[ {w} ]]%; background: {bg}; transition: width .45s cubic-bezier(.2,.8,.2,1); {"box-shadow: inset 0 0 0 1.5px " + EVG + ";" if bg == LIME else ""}"></span>' for _n, _g, bg, _fg, w in jars)
    legend = ''.join(f'<span style="display: flex; align-items: center; gap: 6px; font-size: 13px"><span style="width: 10px; height: 10px; border-radius: 2px; background: {bg}; box-shadow: inset 0 0 0 1px rgba(16,24,20,.25)"></span>{n}</span>' for n, _g, bg, _fg, _w in jars)
    body = f'''    {beat("Your numbers", "calc")}
    <a href="R8-Tool-Payslip.dc.html" class="card8" style="flex-direction: row; align-items: center; gap: 12px">
      <span style="width: 44px; height: 44px; border-radius: {R_M}px; background: {POOL}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8('doc', 22)}</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {MUTED}">Pay that reached you, from your payslip</span><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">R 14 090</span></span>{icon('chev', 18, MUTED)}</a>
    {result('Every rand has a job', 'free', 'freeSub', f'<div role="img" aria-label="[[ barLabel ]]" style="display: flex; gap: 3px; margin-top: 8px; border-radius: {R_S}px; overflow: hidden">{bar}</div><div style="display: flex; flex-wrap: wrap; gap: 6px 14px">{legend}</div>')}
    <sc-if value="[[ over ]]" hint-placeholder-val="[[ false ]]"><section style="border-radius: {R_L}px; background: {WARN_BG}; color: {WARN_FG}; padding: 14px 16px; display: flex; gap: 10px; font-size: 15px; line-height: 1.45; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">{ALERT}<span>[[ overText ]]</span></section></sc-if>
    <section class="card8">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600">{ic8('home', 18, EVG)}Needs</span><span style="font-size: 16px; font-weight: 600">R 8 900</span></span>
      <div style="display: flex; flex-direction: column">{need_rows}</div>
    </section>
    <section class="card8" style="box-shadow: inset 0 0 0 2px {BLUSH}">
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600">{ic8('people', 18, BLUSH_INK)}Family support</span>{stepper('fam', 'family support')}</span>
      <div style="display: flex; flex-direction: column">{fam_rows}</div>
      <span style="font-size: 14px; line-height: 1.45; color: {SEC}">A planned line, like rent. Planning it makes both "yes" and "not this month" easier to say.</span>
      <span style="display: flex; gap: 8px; flex-wrap: wrap"><a href="R7-Lesson.dc.html" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {NIGHT}; color: {MOON}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{moon(18, 'half')}The conversation, a lesson</a><a href="R8-Story.dc.html" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {BLUSH}; color: {BLUSH_INK}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{ic8('ring', 18)}Thandi's story</a></span>
    </section>
    <section class="card8">
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600">{icon('pool', 18, EVG)}Goals</span>{stepper('goal', 'goals')}</span>
      <span style="font-size: 14px; color: {SEC}">Moving out, R 1 000 a month. Safety net, R 500. Extra goes to the safety net first.</span>
    </section>
    {means("When family support is planned, it stops being the thing that breaks the month. What's left is yours to spend without guilt.")}
    {learn_this('Give every rand a job', 5, ['Black tax', 'Needs and wants', 'Sinking fund'])}
    {make_goal('A family emergency pot', 'For the call that comes mid-month', 'R8-Goals.dc.html')}
    {milestone('Naledi planned her first pay-day.')}
    {foot("Pay-day plan, version 0.1. Your own numbers, kept on your phone and in South Africa. The plan never moves money.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const NET = 14090, NEED = 8900;
    const fam = st.fam == null ? 2300 : st.fam, goal = st.goal == null ? 1500 : st.goal;
    const free = NET - NEED - fam - goal;
    const pct = (x) => Math.max(0, Math.round(x / NET * 1000) / 10);
    return { %(share)s
      famAmt: R(fam), goalAmt: R(goal),
      famDown: () => this.setState({ fam: Math.max(0, fam - 100) }), famUp: () => this.setState({ fam: fam + 100 }),
      goalDown: () => this.setState({ goal: Math.max(0, goal - 100) }), goalUp: () => this.setState({ goal: goal + 100 }),
      free: free >= 0 ? R(free) : '−' + R(-free), freeSub: free >= 0 ? 'is yours to spend freely this month, after needs, family and goals.' : 'more than came in. Something has to give.',
      over: free < 0, overText: 'That plan is ' + R(-free) + ' more than your pay. Try a smaller goal amount this month; the goal waits, it does not disappear.',
      needW: pct(NEED), famW: pct(fam), goalW: pct(goal), freeW: pct(Math.max(0, free)),
      barLabel: 'Needs ' + R(NEED) + ', family ' + R(fam) + ', goals ' + R(goal) + ', yours ' + R(Math.max(0, free))
    };
  }
}''' % dict(R=rands_js(), share=SHARE_JS)
    return tool_page('Pay-day plan', body, logic, h=2350)


# ---------------------------------------------------------------- Debt payoff

DEBTS = [('Store card', 6200, 21.0, 350), ('Clothing account', 2400, 22.5, 150), ('Personal loan', 18000, 26.5, 780)]


def debt():
    rows = ''.join(f'''<div style="min-height: 60px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
        <span style="width: 40px; height: 40px; border-radius: {R_M}px; background: {WARN_BG}; color: {WARN_FG}; display: flex; align-items: center; justify-content: center">{ic8('down', 20)}</span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {MUTED}">{r:g}% a year, at least {fmt_r(m, False)} a month</span></span>
        <span style="font-size: 16px; font-weight: 600; font-variant-numeric: tabular-nums">{fmt_r(b, False)}</span></div>''' for i, (n, b, r, m) in enumerate(DEBTS))
    tl = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 6px">
        <span style="display: flex; justify-content: space-between; font-size: 14px"><span style="font-weight: 600">{n}</span><span style="color: {SEC}">[[ end{i} ]]</span></span>
        <span style="height: 12px; border-radius: 2px; background: {MIST}; overflow: hidden"><span style="display: block; height: 100%; width: [[ w{i} ]]%; background: [[ c{i} ]]; transition: width .5s cubic-bezier(.2,.8,.2,1)"></span></span></div>''' for i, (n, _b, _r, _m) in enumerate(DEBTS))
    strat = ''.join(f'<button role="tab" onClick="[[ s{j} ]]" aria-selected="[[ sOn{j} ]]" style="flex: 1 1 0; min-height: 56px; border-radius: 8px; background: [[ sBg{j} ]]; color: [[ sFg{j} ]]; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; transition: background-color .18s"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 12px">{d}</span></button>'
                    for j, (t, d) in enumerate([('Snowball', 'Smallest first'), ('Avalanche', 'Dearest first')]))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 4px"><div style="display: flex; flex-direction: column">{rows}</div></section>
    <section class="card8">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><label for="debt-x" style="font-size: 16px; font-weight: 600">Extra each month</label><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">[[ extraAmt ]]</span></span>
      <input id="debt-x" class="rng8" type="range" min="0" max="1500" step="100" value="[[ extra ]]" onInput="[[ setExtra ]]" style="--p: [[ extraP ]]%">
      <span style="font-size: 13px; color: {MUTED}">On top of the minimums (R 1 280). When a debt is paid off, its minimum rolls on to the next.</span>
      <div role="tablist" aria-label="Which debt first" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {MIST}">{strat}</div>
    </section>
    {result('Debt-free by', 'free', 'freeSub')}
    <section class="card8" style="gap: 14px"><span style="font-size: 16px; font-weight: 600">Paid off, one by one</span>{tl}</section>
    {means("Snowball clears the smallest debt first: quick wins keep people going. Avalanche clears the dearest first: it saves the most interest. Both work; the one you'll keep doing is the right one.")}
    {learn_this('Snowball or avalanche', 4, ['Interest', 'Annual rate', 'Credit life'])}
    {make_goal('Debt-free by [[ freeShort ]]', 'A goal that shrinks instead of fills', 'R8-Goals.dc.html', 'down', 'Make it')}
    {milestone('Naledi paid off her first debt.')}
    {foot("Debt payoff planner, version 0.1. An illustration: interest is worked out monthly and rates stay the same. Your lender's statement is the real number.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const D = %(debts)s;
    const extra = st.extra == null ? 500 : st.extra, s = st.s == null ? 0 : st.s;
    const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const label = (m) => { const t = 8 + m; return MONTHS[t %% 12] + ' ' + (2026 + Math.floor(t / 12)); };
    const run = (extraPay, roll, order) => {
      const bal = D.map((d) => d[1]); const done = D.map(() => 0); let interest = 0, m = 0;
      while (bal.some((b) => b > 0.5) && m < 480) {
        m++;
        bal.forEach((b, i) => { if (b > 0) { const it = b * D[i][2] / 1200; interest += it; bal[i] = b + it; } });
        let pool = extraPay;
        D.forEach((d, i) => { if (bal[i] > 0) { const p = Math.min(d[3], bal[i]); bal[i] -= p; } else if (roll) pool += d[3]; });
        for (const i of order) { if (pool <= 0) break; if (bal[i] > 0) { const p = Math.min(pool, bal[i]); bal[i] -= p; pool -= p; } }
        bal.forEach((b, i) => { if (b <= 0.5 && !done[i]) { bal[i] = 0; done[i] = m; } });
      }
      return { months: m, interest, done };
    };
    const order = s === 0 ? [1, 0, 2] : [2, 1, 0];
    const plan = run(extra, true, order), base = run(0, false, order);
    const saved = base.interest - plan.interest;
    const v = { %(share)s
      extra, extraAmt: R(extra), extraP: Math.round(extra / 15), setExtra: (e) => this.setState({ extra: +e.target.value }),
      free: label(plan.months), freeShort: label(plan.months),
      freeSub: 'That is ' + plan.months + ' months. You would pay ' + R(saved) + ' less interest than with minimums only.'
    };
    for (let j = 0; j < 2; j++) { v['s' + j] = () => this.setState({ s: j }); v['sOn' + j] = s === j; v['sBg' + j] = s === j ? '%(evg)s' : 'transparent'; v['sFg' + j] = s === j ? '#FFFFFF' : '%(ink)s'; }
    D.forEach((d, i) => { v['end' + i] = label(plan.done[i]); v['w' + i] = Math.round(plan.done[i] / plan.months * 100); v['c' + i] = order[0] === i ? '%(evg)s' : '#8DBFAE'; });
    return v;
  }
}''' % dict(R=rands_js(), debts=json.dumps(DEBTS), share=SHARE_JS, evg=EVG, ink=INK)
    return tool_page('Debt payoff', body, logic, h=2160)


# ---------------------------------------------------------------- Fee eater

def fees():
    bars = ''.join(f'''<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 6px">
        <div style="height: 180px; width: 100%; display: flex; align-items: flex-end; justify-content: center; gap: 4px">
          <span style="width: 40%; height: [[ a{i} ]]%; border-radius: 4px 4px 2px 2px; background: #C9E2DA; transition: height .45s cubic-bezier(.2,.8,.2,1)"></span>
          <span style="width: 40%; height: [[ b{i} ]]%; border-radius: 4px 4px 2px 2px; background: {EVG}; transition: height .45s cubic-bezier(.2,.8,.2,1)"></span></div>
        <span style="font-size: 12px; color: {MUTED}">[[ y{i} ]]</span></div>''' for i in range(4))
    yrs = ''.join(f'<button onClick="[[ yr{j} ]]" aria-pressed="[[ yrOn{j} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: [[ yrBg{j} ]]; color: [[ yrFg{j} ]]; font-size: 14px; font-weight: 600">{y} years</button>' for j, y in enumerate((10, 20, 30)))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 14px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><label for="fee-m" style="font-size: 16px; font-weight: 600">Each month</label><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">[[ monthAmt ]]</span></span>
      <input id="fee-m" class="rng8" type="range" min="200" max="2000" step="100" value="[[ m ]]" onInput="[[ setM ]]" style="--p: [[ mP ]]%">
      <div role="group" aria-label="For how long" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {MIST}">{yrs}</div>
      <span style="display: flex; justify-content: space-between; align-items: baseline"><label for="fee-f" style="font-size: 16px; font-weight: 600">Yearly fee</label><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">[[ feeTxt ]]</span></span>
      <input id="fee-f" class="rng8" type="range" min="25" max="300" step="25" value="[[ f ]]" onInput="[[ setF ]]" style="--p: [[ fP ]]%">
    </section>
    {result('The fee takes about', 'cost', 'costSub')}
    <section class="card8" style="gap: 12px">
      <span style="font-size: 16px; font-weight: 600">What it could grow to</span>
      <div role="img" aria-label="[[ chartLabel ]]" style="display: flex; gap: 10px; padding-top: 6px">{bars}</div>
      <span style="display: flex; gap: 14px; font-size: 13px"><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: #C9E2DA"></span>With no fee</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: {EVG}"></span>With [[ feeTxt ]] a year</span></span>
    </section>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 14px 16px; font-size: 14px; line-height: 1.5">An illustration, not a promise. It assumes growth of 9% a year before fees; real returns go up and down, and some years go down. AWO never names a fund or a platform.</section>
    {means("A fee comes off every year, from your money and from the growth it has already made. That's why a fee that sounds small takes a big bite over 20 years.")}
    {learn_this('Fees, the quiet cost', 3, ['TER', 'Compound interest', 'ETF'], 'R8-Topic-Shares.dc.html')}
    {make_goal('Start investing', 'A goal template, with a readiness check first', 'R8-Goals.dc.html', 'grow', 'Open')}
    {foot("Fee eater, version 0.1. Monthly amounts, growth worked out monthly. This tool has no milestone to share.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const m = st.m == null ? 500 : st.m, f = st.f == null ? 200 : st.f, yi = st.yi == null ? 1 : st.yi;
    const Y = [10, 20, 30][yi];
    const fv = (rate, years) => { const r = Math.pow(1 + rate, 1 / 12) - 1, n = years * 12; return m * (Math.pow(1 + r, n) - 1) / r; };
    const gross = fv(0.09, Y), net = fv(0.09 - f / 10000, Y);
    const v = {
      m, f, monthAmt: R(m), mP: Math.round((m - 200) / 18), setM: (e) => this.setState({ m: +e.target.value }),
      fP: Math.round((f - 25) / 2.75), setF: (e) => this.setState({ f: +e.target.value }), feeTxt: String(f / 100).replace('.', ',') + '%%',
      cost: R(Math.round((gross - net) / 1000) * 1000), costSub: 'over ' + Y + ' years, of what ' + R(m) + ' a month could grow to. You put in ' + R(m * 12 * Y) + '.',
      chartLabel: 'After ' + Y + ' years: about ' + R(Math.round(gross / 1000) * 1000) + ' with no fee, ' + R(Math.round(net / 1000) * 1000) + ' with the fee'
    };
    for (let i = 0; i < 4; i++) { const yy = Math.round(Y * (i + 1) / 4); v['y' + i] = 'Year ' + yy; v['a' + i] = Math.max(2, Math.round(fv(0.09, yy) / gross * 100)); v['b' + i] = Math.max(2, Math.round(fv(0.09 - f / 10000, yy) / gross * 100)); }
    for (let j = 0; j < 3; j++) { v['yr' + j] = () => this.setState({ yi: j }); v['yrOn' + j] = yi === j; v['yrBg' + j] = yi === j ? '%(evg)s' : 'transparent'; v['yrFg' + j] = yi === j ? '#FFFFFF' : '%(ink)s'; }
    return v;
  }
}''' % dict(R=rands_js(), evg=EVG, ink=INK)
    return tool_page('Fee eater', body, logic, h=1950)


# ---------------------------------------------------------------- Statement insights

CATS = [('Rent', 4500), ('Debit orders', 2465), ('Food', 2450), ('Transport', 1380), ('Cash', 800), ('Eating out', 690), ('Airtime and data', 420), ('Bank fees', 214)]
DEBITS = [('Funeral cover', '1 Sep', 189, True), ('Funeral cover', '1 Sep', 189, True), ('Personal loan', '1 Sep', 780, False), ('Cellphone contract', '3 Sep', 459, False),
          ('Gym', '5 Sep', 399, False), ('Store card', '7 Sep', 350, False), ('Streaming', '12 Sep', 99, False)]


def statement():
    consent = ''.join(f'<span style="display: flex; gap: 12px; align-items: flex-start; font-size: 15px; line-height: 1.4"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: {R_M}px; background: {MIST}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8(g, 18)}</span><span style="display: flex; flex-direction: column; gap: 2px"><b style="font-weight: 600">{t}</b><span style="font-size: 13px; color: {MUTED}">{d}</span></span></span>'
                      for g, t, d in [('pin', 'Read in South Africa', 'By AI, labelled, and logged'), ('close', 'Deleted once read', 'Only the totals you confirm are kept'), ('shield', 'Never used to score you', 'And never shared with anyone')])
    top = max(v for _n, v in CATS)
    cats = ''.join(f'''<div style="display: grid; grid-template-columns: 120px minmax(0, 1fr) 72px; gap: 10px; align-items: center; min-height: 32px">
        <span style="font-size: 14px">{n}</span><span style="height: 12px; border-radius: 2px; background: {MIST}"><span style="display: block; height: 100%; width: {round(v / top * 100)}%; border-radius: 2px; background: {WARN_FG if n == "Bank fees" else EVG}; transform-origin: 0 0; animation: barIn .6s cubic-bezier(.2,.8,.2,1) {0.1 + k * 0.05:.2f}s both"></span></span>
        <span style="font-size: 14px; font-weight: 600; text-align: right; font-variant-numeric: tabular-nums">{fmt_r(v, False)}</span></div>''' for k, (n, v) in enumerate(CATS))
    debits = ''.join(f'''<div style="min-height: 52px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""} {"background: " + WARN_BG + "; margin: 0 -16px; padding: 0 16px;" if flag else ""}">
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {WARN_FG if flag else MUTED}">{d}{", twice on the same day" if flag else ""}</span></span>
        <span style="font-size: 15px; font-weight: 600; font-variant-numeric: tabular-nums">{fmt_r(v, False)}</span></div>''' for i, (n, d, v, flag) in enumerate(DEBITS))
    body = f'''    <sc-if value="[[ s0 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: fadeIn .3s ease-out both">
      <h1 class="d" style="font-size: 40px">Where did September go?</h1>
      <p style="font-size: 16px; line-height: 1.5; color: {SEC}">Add one bank statement as a PDF. AWO finds where the money went, your debit orders, and what the bank charged.</p>
      <section class="card8" style="gap: 14px">{consent}</section>
      <button role="checkbox" aria-checked="[[ agreed ]]" onClick="[[ agree ]]" style="min-height: 56px; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; line-height: 1.4"><span style="width: 24px; height: 24px; flex-shrink: 0; border-radius: {R_S}px; background: [[ agreeBg ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center">{icon('check', 16, '#FFFFFF', 3)}</span>Yes, read this one statement. I can change my mind in Me, under Your documents.</button>
      <sc-if value="[[ agreed ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ start ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('upload', 20, '#FFFFFF')}Choose a PDF</button></sc-if>
      <sc-if value="[[ notAgreed ]]" hint-placeholder-val="[[ true ]]"><span style="height: 56px; border-radius: {R_M}px; background: #DCE4DF; color: {MUTED}; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">Choose a PDF</span></sc-if>
      <span style="font-size: 13px; line-height: 1.45; color: {MUTED}">A sample policy for design. The real one waits on AWO's decisions about documents and AI providers (Q-37, Q-09).</span>
    </div></sc-if>
    <sc-if value="[[ s1 ]]" hint-placeholder-val="[[ false ]]"><section class="card8" style="gap: 14px; animation: fadeIn .3s ease-out both">
      <span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 17px; font-weight: 600">Reading your statement</span>{AI_CHIP}</span>
      <span style="height: 8px; border-radius: 2px; background: {MIST}; overflow: hidden"><span style="display: block; height: 100%; width: 100%; background: {EVG}; transform-origin: 0 0; animation: barIn 1.6s cubic-bezier(.4,0,.2,1) both"></span></span>
      <span class="sk" style="height: 14px; width: 80%"></span><span class="sk" style="height: 14px; width: 64%"></span><span class="sk" style="height: 14px; width: 72%"></span>
      <span style="font-size: 13px; color: {MUTED}">In South Africa. About 20 seconds.</span>
    </section></sc-if>
    <sc-if value="[[ s2 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: rise .35s cubic-bezier(.2,.8,.2,1) both">
      <section style="border-radius: {R_L}px; background: {MIST}; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 12px 14px; display: flex; align-items: center; gap: 10px; font-size: 14px; line-height: 1.4">{ic8('close', 18, EVG)}<span style="flex-grow: 1">Your statement was deleted at 14:32. Only these totals are kept.</span><a href="R7-Me.dc.html" style="min-height: 44px; display: flex; align-items: center; font-weight: 600; color: {EVG}">Your documents</a></section>
      {beat("One plain result", "pool")}
      <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">
        <span style="font-size: 14px; font-weight: 600">Before you spent a rand</span>
        <span class="d" style="font-size: 56px">R 2 465</span>
        <span style="font-size: 16px; line-height: 1.4; color: {INK}">went out in seven debit orders. One looks like it's there twice.</span>
      </section>
      <section class="card8" style="gap: 4px"><span style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px"><span style="font-size: 16px; font-weight: 600">Debit orders</span>{AI_CHIP}</span><div style="display: flex; flex-direction: column">{debits}</div>
        <span style="font-size: 14px; line-height: 1.45; color: {SEC}; padding-top: 10px">Two the same on one day can be a mistake. Your bank can tell you, and can reverse one that shouldn't be there.</span></section>
      <section class="card8" style="gap: 8px"><span style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px"><span style="font-size: 16px; font-weight: 600">Where September went</span><span style="font-size: 13px; color: {MUTED}">Tap to fix a category</span></span>{cats}</section>
      <section class="card8" style="gap: 6px"><span style="font-size: 16px; font-weight: 600">Bank fees: R 214</span><span style="font-size: 14px; line-height: 1.45; color: {SEC}">Monthly fee R 115, cash withdrawals R 64, notifications R 35.</span></section>
      {means("Debit orders go before anything else each month. Knowing each one, and what it's for, is how people decide which ones still earn their place.")}
      {learn_this('Where does it go?', 4, ['Debit order', 'Bank charges'])}
      {make_goal('Plan October with this', 'Your debit orders go straight into the pay-day plan', 'R8-Tool-Payday.dc.html', 'calc', 'Plan it')}
      <button onClick="[[ restart ]]" style="height: 48px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 15px; font-weight: 600">See the consent screen</button>
    </div></sc-if>
    {foot("Statement insights, version 0.1. Categories are AI-assisted and she can change any of them; totals are worked out from her confirmed lines. There is no milestone: this stays private.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const s = st.s == null ? 2 : st.s, agreed = !!st.agreed;
    return {
      s0: s === 0, s1: s === 1, s2: s === 2, agreed, notAgreed: !agreed, agreeBg: agreed ? '%(evg)s' : '#FFFFFF',
      agree: () => this.setState({ agreed: !agreed }),
      start: () => this.setState({ s: 1 }, () => setTimeout(() => this.setState({ s: 2 }), 1700)),
      restart: () => this.setState({ s: 0, agreed: false })
    };
  }
}''' % dict(evg=EVG)
    return tool_page('Statement insights', body, logic, h=2330)


BOARDS = [('R8-Tool-Payslip', payslip), ('R8-Tool-Payday', payday), ('R8-Tool-Debt', debt), ('R8-Tool-Fees', fees), ('R8-Tool-Statement', statement)]
