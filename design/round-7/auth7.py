"""Round 7, batch 1: accounts and the first loop (D-035: phone number first, Google and Apple as the
social options). Flow: Entry, sign in with phone or social, code, about you, consent, goals, starter check,
the first result reveal, choose your first step, reminders, PIN lock, Home. Returning: welcome back."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from screens7 import ic, back, switch, switch_js, mark, R_S, R_M, R_L, LINE7  # noqa: E402

HF = "font-family: '[[ handFont ]]', cursive"
SR = 'position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)'

COUNTRIES = [('South Africa', '+27', 9, '82 123 4567'), ('Kenya', '+254', 9, '712 345 678'), ('Botswana', '+267', 8, '71 234 567'),
             ('Namibia', '+264', 9, '81 234 5678'), ('Zimbabwe', '+263', 9, '77 123 4567'), ('United Kingdom', '+44', 10, '7700 900123')]

GOOGLE = ('<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.3z" fill="#4285F4"></path>'
          '<path d="M12 22c2.7 0 5-.9 6.6-2.5l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z" fill="#34A853"></path>'
          '<path d="M6.4 13.9a6 6 0 0 1 0-3.8V7.5H3.1a10 10 0 0 0 0 9z" fill="#FBBC05"></path>'
          '<path d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.9-2.9A10 10 0 0 0 3.1 7.5l3.3 2.6C7.2 7.7 9.4 5.9 12 5.9z" fill="#EA4335"></path></svg>')
APPLE = ('<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.2-2.8.8-3.5.8-.7 0-1.8-.8-3-.8-1.5 0-3 .9-3.8 2.3-1.6 2.8-.4 7 1.2 9.3.8 1.1 1.7 2.4 2.9 2.3 1.2 0 1.6-.7 3-.7s1.8.7 3 .7c1.3 0 2.1-1.1 2.8-2.3.9-1.3 1.3-2.6 1.3-2.7 0 0-2.5-1-2.5-3.6z" fill="currentColor"></path>'
         '<path d="M14.1 5.8c.6-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.1 1.8-1 2.9 1.1.1 2.1-.6 2.8-1.4z" fill="currentColor"></path></svg>')
FINGER = ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true">'
          '<path d="M6.5 7.5A7 7 0 0 1 19 12v1.5M5 12a7 7 0 0 1 .4-2.4M8.5 20a14 14 0 0 1-1.5-6.5 5 5 0 0 1 10 0v.5M12 13.5c0 3 .8 5.4 2.2 7.5M15.8 19.8c.5-1 .9-2.2 1-3.6"></path></svg>')


def title(t, sub=None, size=36):
    s = f'<h1 class="d" style="font-size: {size}px">{t}</h1>'
    if sub:
        s += f'<p style="font-size: 16px; line-height: 1.45; color: {SEC}; margin-top: -4px">{sub}</p>'
    return s


def primary(label, href=None, hole=None, h=56):
    if href:
        return f'<a href="{href}" style="height: {h}px; flex-shrink: 0; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">{label}</a>'
    return f'<button onClick="[[ {hole} ]]" style="height: {h}px; flex-shrink: 0; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600">{label}</button>'


def disabled(label, h=56):
    return f'<button aria-disabled="true" style="height: {h}px; flex-shrink: 0; width: 100%; border-radius: {R_M}px; background: #DCE4DF; color: {MUTED}; font-size: 16px; font-weight: 600">{label}</button>'


def steps_bar(n, of=4):
    return (f'<div role="img" aria-label="Step {n} of {of}" style="flex-grow: 1; display: flex; gap: 6px">'
            + ''.join(f'<span style="flex: 1 1 0; height: 6px; border-radius: 2px; background: {EVG if i < n else "#DCE4DF"}"></span>' for i in range(of)) + '</div>')


def keypad(finger=False):
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'f' if finger else '', '0', 'del']
    out = []
    for k in keys:
        if k == '':
            out.append('<span></span>')
        elif k == 'del':
            out.append(f'<button onClick="[[ kDel ]]" aria-label="Delete" style="height: 60px; border-radius: {R_M}px; display: flex; align-items: center; justify-content: center; color: {INK}"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5h11v14H9l-6-7z"></path><path d="m12.5 9.5 5 5M17.5 9.5l-5 5"></path></svg></button>')
        elif k == 'f':
            out.append(f'<button onClick="[[ kFinger ]]" aria-label="Use fingerprint" style="height: 60px; border-radius: {R_M}px; display: flex; align-items: center; justify-content: center; color: {EVG}">{FINGER}</button>')
        else:
            out.append(f'<button class="press" onClick="[[ k{k} ]]" style="height: 60px; border-radius: {R_M}px; background: #FFFFFF; font-size: 26px; font-weight: 500">{k}</button>')
    return f'<div role="group" aria-label="Number pad" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{"".join(out)}</div>'


def dots():
    return ('<div role="img" aria-label="[[ dotsLabel ]]" style="display: flex; gap: 16px; justify-content: center; animation: [[ shake ]]">'
            + ''.join(f'<span style="width: 16px; height: 16px; border-radius: 999px; box-sizing: border-box; border: 2px solid {EVG}; background: [[ d{i} ]]; transition: background-color .12s"></span>' for i in range(4)) + '</div>')


PIN_CSS = '@keyframes shake{0%,100%{transform:none}20%,60%{transform:translateX(-8px)}40%,80%{transform:translateX(8px)}}'


def with_css(html, css):
    return html.replace('</style>', css + '</style>', 1)


# ---------------------------------------------------------------- Sign in: phone first, or social

def signin():
    opts = ''.join(f'''<button onClick="[[ c{i} ]]" aria-pressed="[[ cOn{i} ]]" style="min-height: 52px; padding: 0 16px; border-radius: {R_M}px; background: [[ cBg{i} ]]; display: flex; align-items: center; justify-content: space-between; font-size: 16px; font-weight: 500; text-align: left">
            <span>{n}</span><span style="color: {MUTED}; font-variant-numeric: tabular-nums">{code}</span></button>''' for i, (n, code, _l, _p) in enumerate(COUNTRIES))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 18px">
    <header style="display: flex; align-items: center; justify-content: space-between">{back('R7-Entry.dc.html')}<span style="display: flex; align-items: center; gap: 8px; color: {EVG}">{mark(28, EVG, LIME)}<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.05em">awo</span></span><span style="width: 44px"></span></header>
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 12px">{title('Your number is your key.', "We'll text you a code. There's no password to remember.", 38)}</div>
    <div style="display: flex; flex-direction: column; gap: 8px">
      <label for="au-phone" style="font-size: 13px; font-weight: 600">Mobile number</label>
      <div style="display: flex; gap: 8px">
        <button onClick="[[ openSheet ]]" aria-haspopup="dialog" aria-label="Country code [[ code ]]. Change" style="height: 56px; padding: 0 12px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; display: flex; align-items: center; gap: 6px; font-size: 17px; font-weight: 600; font-variant-numeric: tabular-nums">[[ code ]]<span style="display: flex; transform: rotate(90deg)">{icon('chev', 16, MUTED)}</span></button>
        <input id="au-phone" type="tel" inputmode="tel" autocomplete="tel-national" value="[[ shown ]]" onInput="[[ type ]]" placeholder="[[ ph ]]" style="flex-grow: 1; min-width: 0; height: 56px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ fieldBw ]]px [[ fieldBd ]]; padding: 0 16px; font-size: 19px; font-weight: 500; letter-spacing: .02em; font-variant-numeric: tabular-nums; color: {INK}">
      </div>
      <span style="font-size: 13px; color: [[ hintCol ]]">[[ hint ]]</span>
    </div>
    <sc-if value="[[ valid ]]" hint-placeholder-val="[[ false ]]">{primary('Send me a code', 'R7-Auth-Code.dc.html')}</sc-if>
    <sc-if value="[[ notValid ]]" hint-placeholder-val="[[ true ]]">{disabled('Send me a code')}</sc-if>
    <div aria-hidden="true" style="display: flex; align-items: center; gap: 12px; color: {MUTED}; font-size: 13px"><span style="flex-grow: 1; height: 1px; background: #DCE4DF"></span>or<span style="flex-grow: 1; height: 1px; background: #DCE4DF"></span></div>
    <a href="R7-Auth-Profile.dc.html" style="height: 52px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 16px; font-weight: 600">{GOOGLE}Continue with Google</a>
    <a href="R7-Auth-Profile.dc.html" style="height: 52px; border-radius: {R_M}px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 16px; font-weight: 600">{APPLE}Continue with Apple</a>
    <div style="flex-grow: 1"></div>
    <p style="font-size: 13px; line-height: 1.45; color: {MUTED}; text-align: center">By continuing you agree to the <a href="#" style="color: {EVG}; font-weight: 600; text-decoration: underline">Terms</a> and <a href="#" style="color: {EVG}; font-weight: 600; text-decoration: underline">Privacy Policy</a>. Your data is stored in South Africa.</p>
  </div>
  <sc-if value="[[ sheet ]]" hint-placeholder-val="[[ false ]]">
    <div style="position: absolute; inset: 0; z-index: 20; background: rgba(11,15,14,.45)">
      <div role="dialog" aria-label="Choose your country code" style="position: absolute; left: 0; right: 0; bottom: 0; border-radius: {R_L}px {R_L}px 0 0; background: {MIST}; padding: 12px 16px 28px; display: flex; flex-direction: column; gap: 8px; animation: sheetUp .28s cubic-bezier(.2,.8,.2,1) both">
        <span aria-hidden="true" style="align-self: center; width: 40px; height: 5px; border-radius: 3px; background: #C9D3CE"></span>
        <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 18px; font-weight: 600">Where is your number from?</span><button onClick="[[ closeSheet ]]" aria-label="Close" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('close', 20, INK, 2.2)}</button></div>
        {opts}
      </div>
    </div>
  </sc-if>'''
    cs = [[n, c, l, p] for n, c, l, p in COUNTRIES]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const cs = %(cs)s;
    const ci = st.ci || 0, c = cs[ci];
    const digits = (st.digits == null ? '821234567' : st.digits).slice(0, c[2]);
    const groups = c[3].split(' ').map((g) => g.length);
    let shown = '', k = 0;
    for (const g of groups) { if (k >= digits.length) break; shown += (shown ? ' ' : '') + digits.slice(k, k + g); k += g; }
    const valid = digits.length === c[2];
    const v = {
      code: c[1], ph: c[3], shown, valid, notValid: !valid,
      type: (e) => this.setState({ digits: e.target.value.replace(/\\D/g, '').replace(/^0/, '') }),
      hint: valid ? 'We will text a 6-digit code to ' + c[1] + ' ' + shown + '.' : (digits.length ? (c[2] - digits.length) + ' more digits' : 'Leave out the first 0.'),
      hintCol: valid ? '%(evg)s' : '%(mut)s', fieldBw: valid ? 2 : 1, fieldBd: valid ? '%(evg)s' : '#C9D3CE',
      sheet: !!st.sheet, openSheet: () => this.setState({ sheet: true }), closeSheet: () => this.setState({ sheet: false })
    };
    for (let i = 0; i < cs.length; i++) {
      v['c' + i] = () => this.setState({ ci: i, sheet: false, digits: '' }); v['cOn' + i] = ci === i;
      v['cBg' + i] = ci === i ? '%(pool)s' : '#FFFFFF';
    }
    return v;
  }
}''' % dict(cs=cs, evg=EVG, mut=MUTED, pool=POOL)
    return phone('Sign in', body, logic, h=844)


# ---------------------------------------------------------------- The code

def code():
    boxes = ''.join(f'<span style="flex: 1 1 0; height: 64px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ bw{i} ]]px [[ bc{i} ]]; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 600; font-variant-numeric: tabular-nums; transition: box-shadow .12s">[[ g{i} ]]</span>' for i in range(6))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 18px">
    <header style="display: flex; align-items: center; gap: 14px">{back('R7-Auth-Signin.dc.html')}{steps_bar(1)}</header>
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 8px">{title('Enter the code.')}
      <p style="font-size: 16px; line-height: 1.45; color: {SEC}; margin-top: -4px">We sent it to <b style="color: {INK}; font-variant-numeric: tabular-nums">+27 82 123 4567</b>. <a href="R7-Auth-Signin.dc.html" style="color: {EVG}; font-weight: 600; text-decoration: underline">Change</a></p></div>
    <div style="position: relative">
      <label for="au-code" style="{SR}">6-digit code</label>
      <div aria-hidden="true" style="display: flex; gap: 8px; animation: [[ shake ]]">{boxes}</div>
      <input id="au-code" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" value="[[ digits ]]" onInput="[[ type ]]" style="position: absolute; inset: 0; width: 100%; height: 64px; opacity: 0; border: 0">
    </div>
    <span style="display: flex; align-items: center; gap: 8px; font-size: 14px; color: [[ msgCol ]]; min-height: 20px">[[ msg ]]</span>
    <sc-if value="[[ ok ]]" hint-placeholder-val="[[ false ]]">
      <div style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 16px; display: flex; align-items: center; gap: 12px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
        <span style="width: 40px; height: 40px; border-radius: {R_M}px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 22, EVG, 2.8)}</span>
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Number confirmed</span><span style="font-size: 13px; color: {SEC}">It stays private. Community sees your first name only.</span></span></div>
    </sc-if>
    <sc-if value="[[ notOk ]]" hint-placeholder-val="[[ true ]]"><button style="align-self: flex-start; height: 44px; font-size: 15px; font-weight: 600; color: {EVG}">Send a new code</button></sc-if>
    <div style="flex-grow: 1"></div>
    <span style="display: flex; justify-content: center">{sample_chip(MUTED, 'Sample: the code is 123456')}</span>
    <sc-if value="[[ ok ]]" hint-placeholder-val="[[ false ]]">{primary('Continue', 'R7-Auth-Profile.dc.html')}</sc-if>
    <sc-if value="[[ notOk ]]" hint-placeholder-val="[[ true ]]">{disabled('Continue')}</sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const digits = st.digits || '';
    const full = digits.length === 6, ok = full && digits === '123456', bad = full && !ok;
    const v = {
      digits, ok, notOk: !ok, shake: bad ? 'shake .4s' : 'none',
      type: (e) => this.setState({ digits: e.target.value.replace(/\\D/g, '').slice(0, 6) }),
      msg: ok ? '' : (bad ? "That code doesn't match. Check the message and try again." : 'It can take a minute to arrive.'),
      msgCol: bad ? '%(wine)s' : '%(mut)s'
    };
    for (let i = 0; i < 6; i++) {
      v['g' + i] = digits[i] || '';
      const cur = i === digits.length && !full;
      v['bw' + i] = bad ? 2 : (cur || (ok && i < 6) ? 2 : 1);
      v['bc' + i] = bad ? '%(wine)s' : (ok ? '%(evg)s' : (cur ? '%(evg)s' : '#C9D3CE'));
    }
    return v;
  }
}''' % dict(evg=EVG, mut=MUTED, wine=BLUSH_2)
    return with_css(phone('Enter the code', body, logic, h=844), PIN_CSS)


# ---------------------------------------------------------------- About you

PLACES = [('South Africa', 'rand', 'R'), ('Kenya', 'shilling', 'KSh'), ('Botswana', 'pula', 'P'), ('United Kingdom', 'pound', '£'), ('Somewhere else', '', '')]


def profile():
    cards = ''.join(f'''<button onClick="[[ p{i} ]]" aria-pressed="[[ pOn{i} ]]" style="min-height: 52px; padding: 0 16px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ pBw{i} ]]px {EVG}; display: flex; align-items: center; justify-content: space-between; gap: 10px; font-size: 16px; font-weight: 500; text-align: left">
          <span>{n}</span><span style="font-size: 14px; color: {MUTED}">{sym}</span></button>''' for i, (n, _c, sym) in enumerate(PLACES))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 16px">
    <header style="display: flex; align-items: center; gap: 14px">{back('R7-Auth-Code.dc.html')}{steps_bar(2)}</header>
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 8px">{title('What should we call you?', 'Your first name is all Community ever sees.')}</div>
    <div style="display: flex; flex-direction: column; gap: 6px">
      <label for="au-name" style="font-size: 13px; font-weight: 600">First name</label>
      <input id="au-name" autocomplete="given-name" value="[[ name ]]" onInput="[[ type ]]" style="height: 56px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 0 16px; font-size: 18px; font-weight: 500; color: {INK}">
    </div>
    <span style="font-size: 17px; font-weight: 600; margin-top: 6px">Where do you live now?</span>
    <div role="radiogroup" aria-label="Where you live" style="display: flex; flex-direction: column; gap: 8px">{cards}</div>
    <span style="display: flex; align-items: center; gap: 8px; font-size: 14px; color: {SEC}">{icon('check', 16, EVG, 2.6)}[[ cur ]]</span>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ ready ]]" hint-placeholder-val="[[ true ]]">{primary('Continue', 'R7-Auth-Consent.dc.html')}</sc-if>
    <sc-if value="[[ notReady ]]" hint-placeholder-val="[[ false ]]">{disabled('Add your first name')}</sc-if>
  </div>'''
    places = [[n, c, s] for n, c, s in PLACES]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const pl = %(pl)s;
    const p = st.p == null ? 0 : st.p, name = st.name == null ? 'Naledi' : st.name;
    const ready = name.trim().length > 0;
    const v = {
      name, type: (e) => this.setState({ name: e.target.value }), ready, notReady: !ready,
      cur: pl[p][1] ? 'Money will show in ' + pl[p][1] + ' (' + pl[p][2] + '). You can change it in Settings.' : "You'll choose your currency next."
    };
    for (let i = 0; i < pl.length; i++) { v['p' + i] = () => this.setState({ p: i }); v['pOn' + i] = p === i; v['pBw' + i] = p === i ? 2 : 0; }
    return v;
  }
}''' % dict(pl=places)
    return phone('About you', body, logic, h=844)


# ---------------------------------------------------------------- Consent

def consent():
    promises = [('pin', POOL, 'Stored in South Africa', 'Your answers and their backups stay in the country.'),
                ('lock', MIST, 'Only you see your numbers', 'Your buddy and circles see lessons and first names, never amounts.'),
                ('download', MIST, 'Yours to take or delete', 'Download everything, or delete your account, from Settings.')]
    ph = ''.join(f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 14px 0; {f"border-bottom: 1px solid {LINE7};" if i < 2 else ""}"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {bg}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic(n, 20)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {MUTED}">{d}</span></span></div>'
                 for i, (n, bg, t, d) in enumerate(promises))
    optional = [('Explain things more simply', 'Uses AI to reword AWO-reviewed text. Always labelled, and the original is one tap away.'),
                ('Help improve AWO', 'Share anonymised answers. You can stop at any time.')]
    opts = ''.join(f'''<div style="min-height: 64px; display: flex; align-items: center; gap: 12px; padding: 8px 0; {f"border-bottom: 1px solid {LINE7};" if i == 0 else ""}">
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">{d}</span></span>{switch(i, t)}</div>''' for i, (t, d) in enumerate(optional))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 14px">
    <header style="display: flex; align-items: center; gap: 14px">{back('R7-Auth-Profile.dc.html')}{steps_bar(3)}</header>
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 8px">{title('Your data, in plain words.', None, 34)}</div>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 2px 16px">{ph}</section>
    <span style="font-size: 15px; font-weight: 600; margin: 4px 0 -6px 4px">Your choice, off until you say so</span>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 12px 0 16px">{opts}</section>
    <button role="checkbox" aria-checked="[[ agreed ]]" onClick="[[ toggleAgree ]]" style="min-height: 48px; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; line-height: 1.4">
      <span aria-hidden="true" style="width: 24px; height: 24px; flex-shrink: 0; box-sizing: border-box; border-radius: {R_S}px; background: [[ agreeBg ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center"><sc-if value="[[ agreed ]]" hint-placeholder-val="[[ false ]]">{icon('check', 16, '#FFFFFF', 3)}</sc-if></span>
      <span>I agree to the <span style="color: {EVG}; font-weight: 600; text-decoration: underline">Terms</span> and <span style="color: {EVG}; font-weight: 600; text-decoration: underline">Privacy Policy</span>.</span></button>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ agreed ]]" hint-placeholder-val="[[ false ]]">{primary('Agree and continue', 'R7-Goals.dc.html')}</sc-if>
    <sc-if value="[[ notAgreed ]]" hint-placeholder-val="[[ true ]]">{disabled('Agree and continue')}</sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = { agreed: !!st.agreed, notAgreed: !st.agreed, toggleAgree: () => this.setState({ agreed: !st.agreed }), agreeBg: st.agreed ? '%(evg)s' : '#FFFFFF' };
%(sw)s
    return v;
  }
}''' % dict(evg=EVG, sw=switch_js(2, [False, False]))
    return phone('Your data, in plain words', body, logic, h=844)


# ---------------------------------------------------------------- Reminders

def notify():
    times = ''.join(f'<button onClick="[[ t{i} ]]" aria-pressed="[[ tOn{i} ]]" style="flex: 1 1 0; min-height: 64px; border-radius: {R_M}px; background: [[ tBg{i} ]]; color: [[ tFg{i} ]]; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; transition: background-color .18s"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 12px; opacity: .8">{t}</span></button>'
                    for i, (n, t) in enumerate([('Morning', '07:30'), ('Lunch', '12:30'), ('Evening', '19:00')]))
    days = ''.join(f'<button onClick="[[ dd{i} ]]" aria-pressed="[[ ddOn{i} ]]" aria-label="{full}" style="flex: 1 1 0; height: 44px; border-radius: {R_M}px; background: [[ ddBg{i} ]]; color: [[ ddFg{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{d}</button>'
                   for i, (d, full) in enumerate(zip('MTWTFSS', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 16px">
    <header style="display: flex; align-items: center; gap: 14px">{back('R7-FirstStep.dc.html')}<span style="flex-grow: 1"></span></header>
    <div style="display: flex; flex-direction: column; gap: 10px">{title('When should we nudge you?', 'One reminder on the days you pick. Never more than one a day.')}</div>
    <div style="position: relative; height: 150px; border-radius: {R_L}px; overflow: hidden; background: {EVG}">
      <img src="{IMG['naledi_cafe']}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 45% 30%; opacity: .55">
      <div style="position: absolute; left: 12px; right: 12px; bottom: 12px; border-radius: {R_L}px; background: rgba(244,248,245,.94); padding: 12px 14px; display: flex; gap: 12px; align-items: flex-start">
        <span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: {R_M}px; background: {EVG}; display: flex; align-items: center; justify-content: center">{mark(22, '#FFFFFF', LIME)}</span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; justify-content: space-between"><span style="font-size: 14px; font-weight: 600">AWO</span><span style="font-size: 12px; color: {MUTED}">[[ when ]]</span></span><span style="font-size: 14px; line-height: 1.35">Your step this week: move R 100 on payday. It takes a minute.</span></span>
      </div>
    </div>
    <div role="group" aria-label="Time of day" style="display: flex; gap: 8px">{times}</div>
    <div role="group" aria-label="Days" style="display: flex; gap: 6px">{days}</div>
    <span style="display: flex; align-items: center; gap: 8px; font-size: 14px; color: {SEC}">{ic('bell', 16, EVG)}Quiet hours are on, 21:00 to 07:00.</span>
    <div style="flex-grow: 1"></div>
    {primary('Turn on reminders', 'R7-Auth-Lock.dc.html')}
    <a href="R7-Auth-Lock.dc.html" style="height: 44px; flex-shrink: 0; margin-top: -6px; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600; color: {EVG}">Not now</a>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const t = st.t == null ? 2 : st.t, on = st.on || [true, false, true, false, true, false, false];
    const tt = ['07:30', '12:30', '19:00'], names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    const first = on.indexOf(true);
    const v = { when: first < 0 ? 'Off' : names[first] + ' ' + tt[t] };
    for (let i = 0; i < 3; i++) { v['t' + i] = () => this.setState({ t: i }); v['tOn' + i] = t === i; v['tBg' + i] = t === i ? '%(evg)s' : '#FFFFFF'; v['tFg' + i] = t === i ? '#FFFFFF' : '%(ink)s'; }
    for (let i = 0; i < 7; i++) {
      v['dd' + i] = () => { const n = on.slice(); n[i] = !n[i]; this.setState({ on: n }); };
      v['ddOn' + i] = on[i]; v['ddBg' + i] = on[i] ? '%(lime)s' : '#FFFFFF'; v['ddFg' + i] = on[i] ? '%(evg)s' : '%(mut)s';
    }
    return v;
  }
}''' % dict(evg=EVG, ink=INK, lime=LIME, mut=MUTED)
    return phone('Reminders', body, logic, h=844)


# ---------------------------------------------------------------- PIN lock, and welcome back

PIN_LOGIC = """
    const st = this.state || {};
    const pin = st.pin || '';
    const press = (d) => { if (pin.length >= 4) return; const n = pin + d; this.setState({ pin: n, err: false }); if (n.length === 4) setTimeout(() => this.full(n), 220); };
    const v = { kDel: () => this.setState({ pin: pin.slice(0, -1), err: false }), shake: st.err ? 'shake .4s' : 'none', dotsLabel: pin.length + ' of 4 digits entered' };
    for (let d = 0; d < 10; d++) v['k' + d] = () => press(String(d));
    for (let i = 0; i < 4; i++) v['d' + i] = i < pin.length ? 'EVG_HEX' : 'transparent';
""".replace('EVG_HEX', EVG)

def lock():
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 16px">
    <header style="display: flex; align-items: center; justify-content: space-between">{back('R7-Auth-Notify.dc.html')}<a href="R7-Home.dc.html" style="height: 44px; display: flex; align-items: center; font-size: 15px; font-weight: 600; color: {EVG}">Skip for now</a></header>
    <sc-if value="[[ notDone ]]" hint-placeholder-val="[[ true ]]">
      <div style="display: flex; flex-direction: column; gap: 22px">
        <div style="display: flex; flex-direction: column; gap: 10px; text-align: center; align-items: center">
          <span style="width: 56px; height: 56px; border-radius: {R_L}px; background: {POOL}; color: {EVG}; display: flex; align-items: center; justify-content: center">{icon('lock', 26, EVG)}</span>
          <h1 class="d" style="font-size: 32px">[[ heading ]]</h1>
          <p style="font-size: 15px; line-height: 1.45; color: [[ subCol ]]; max-width: 300px">[[ sub ]]</p></div>
        {dots()}
        {keypad(finger=False)}
        <div style="min-height: 64px; border-radius: {R_L}px; background: #FFFFFF; padding: 0 12px 0 16px; display: flex; align-items: center; gap: 12px"><span style="color: {EVG}; display: flex">{FINGER}</span><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Use fingerprint too</span>{switch(0, 'Use fingerprint too')}</div>
      </div>
    </sc-if>
    <sc-if value="[[ done ]]" hint-placeholder-val="[[ false ]]">
      <div style="display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding-top: 120px; animation: rise .45s cubic-bezier(.2,.8,.2,1) both">
        <span style="width: 88px; height: 88px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both">{icon('lock', 38, EVG, 2.2)}</span>
        <h1 class="d" style="font-size: 34px">AWO is locked.</h1>
        <p style="font-size: 16px; line-height: 1.45; color: {SEC}; max-width: 290px">You'll need your PIN or fingerprint to open it. Handy on a shared phone.</p>
      </div>
    </sc-if>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ done ]]" hint-placeholder-val="[[ false ]]">{primary('Go to Home', 'R7-Home.dc.html')}</sc-if>
  </div>'''
    logic = ('''class Component extends DCLogic {
  full(n) {
    const st = this.state || {};
    if ((st.stage || 'create') === 'create') this.setState({ stage: 'confirm', first: n, pin: '' });
    else this.setState(n === st.first ? { stage: 'done' } : { stage: 'create', pin: '', err: true, first: '' });
  }
  renderVals() {''' + PIN_LOGIC + '''
    const stage = st.stage || 'create';
    v.done = stage === 'done'; v.notDone = stage !== 'done';
    v.heading = stage === 'confirm' ? 'Enter it again.' : 'Keep AWO private.';
    v.sub = st.err ? "Those didn't match. Choose a PIN again." : (stage === 'confirm' ? 'Just to be sure.' : 'Phones get shared. Choose a 4-digit PIN to open AWO.');
    v.subCol = st.err ? '%(wine)s' : '%(sec)s';
%(sw)s
    return v;
  }
}''') % dict(wine=BLUSH_2, sec=SEC, sw=switch_js(1, [True]))
    return with_css(phone('Keep AWO private', body, logic, h=844), PIN_CSS)


def welcome_back():
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 20px; align-items: stretch">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; padding-top: 30px">
      <span style="position: relative; width: 84px; height: 84px"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid {LIME}"></span><img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 6px; top: 6px; width: 72px; height: 72px"></span>
      <h1 class="d" style="font-size: 34px">Welcome back, Naledi.</h1>
      <p style="font-size: 15px; color: [[ subCol ]]">[[ sub ]]</p></div>
    {dots()}
    <sc-if value="[[ open ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 12px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{primary('Open AWO', 'R7-Home.dc.html')}</div></sc-if>
    {keypad(finger=True)}
    <div style="flex-grow: 1"></div>
    <span style="display: flex; justify-content: center">{sample_chip(MUTED, 'Sample: the PIN is 2580')}</span>
    <a href="R7-Auth-Signin.dc.html" style="height: 44px; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600; color: {EVG}">Forgot your PIN? Sign in with your number</a>
  </div>'''
    logic = ('''class Component extends DCLogic {
  full(n) { if (n !== '2580') this.setState({ pin: '', err: true }); }
  renderVals() {''' + PIN_LOGIC + '''
    const ok = pin === '2580' || !!st.finger;
    v.open = ok; v.kFinger = () => this.setState({ finger: true, pin: '2580', err: false });
    v.sub = ok ? 'Unlocked.' : (st.err ? "That PIN didn't work. Try again." : 'Enter your PIN, or use your fingerprint.');
    v.subCol = st.err ? '%(wine)s' : '%(sec)s';
    return v;
  }
}''') % dict(wine=BLUSH_2, sec=SEC)
    return with_css(phone('Welcome back', body, logic, h=844), PIN_CSS)


# ---------------------------------------------------------------- The first result reveal

def reveal():
    pts = [(36, 118, 28, 11), (122, 92, 32, 12), (210, 64, 32, 12), (292, 36, 26, 10)]
    dash = ' stroke-dasharray="5 5"'
    st_svg = ''.join(
        f'<g style="animation: stepIn .6s cubic-bezier(.2,.8,.2,1) {0.2 + i * 0.18:.2f}s both">'
        f'<ellipse cx="{x}" cy="{y + 6}" rx="{rx}" ry="{ry}" fill="{"#BFD9D2" if i < 2 else "none"}"></ellipse>'
        f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{[EVG, LIME, "none", "none"][i]}" stroke="{EVG}" stroke-width="2.5"{dash if i > 1 else ""}></ellipse></g>'
        for i, (x, y, rx, ry) in enumerate(pts))
    labels = ''.join(f'<span style="position: absolute; left: {x - 40}px; top: {y + 20}px; width: 80px; text-align: center; font-size: 12px; color: {SEC}; animation: rise .4s ease-out {0.4 + i * 0.18:.2f}s both">Stage {i + 1}</span>' for i, (x, y, _rx, _ry) in enumerate(pts))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 14px">
    <header style="display: flex; align-items: center; justify-content: space-between"><span class="lbl" style="color: {EVG}">Your first profile</span>{sample_chip()}</header>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 22px 16px 16px; display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 16px; font-weight: 600; animation: rise .5s ease-out .1s both">You're at</span>
      <span style="display: flex; align-items: baseline; gap: 10px; animation: rise .6s cubic-bezier(.2,.8,.2,1) .2s both"><span class="d" style="font-size: 72px">Stage 2</span><span style="font-size: 18px; font-weight: 600">of 4</span></span>
      <div role="img" aria-label="Four stepping stones. You are on stage 2." style="position: relative; height: 160px; margin-top: 4px">
        <svg width="326" height="150" viewBox="0 0 326 150" aria-hidden="true" style="position: absolute; left: 0; top: 0; overflow: visible">{st_svg}</svg>{labels}
        <img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 104px; top: 44px; width: 36px; height: 36px; box-shadow: 0 0 0 3px {LIME}; animation: stepIn .7s cubic-bezier(.2,.8,.2,1) 1s both">
      </div>
      <div style="display: flex; align-items: center; gap: 14px; border-top: 1px solid rgba(15,74,54,.14); padding-top: 12px">
        <div role="img" aria-label="DIVA score 63 of 100" style="position: relative; width: 64px; height: 64px; flex-shrink: 0">{arc(64, 63, '#B7D5CE', EVG, sw=6)}<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 600; letter-spacing: -0.03em; padding-top: 2px">63</span></div>
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">DIVA score 63</span><span style="font-size: 13px; color: {SEC}">Learning readiness, not a credit score.</span></span>
      </div>
    </section>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
      <div style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; color: {MUTED}">Your strength</span><span style="font-size: 17px; font-weight: 600; line-height: 1.2">Everyday money</span></div>
      <div style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 14px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px">Your focus</span><span style="font-size: 17px; font-weight: 600; line-height: 1.2">Ready for surprises</span></div>
    </div>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: center; gap: 8px"><span style="font-size: 17px; font-weight: 600">What this means</span><span class="chip" style="background: {EVG}; color: #FFFFFF">{icon('check', 13, '#FFFFFF', 2.6)}Reviewed by AWO</span></span>
      <p style="font-size: 16px; line-height: 1.5">[[ meaning ]]</p>
      <span style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap"><button onClick="[[ toggleSimple ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 14px; font-weight: 600">[[ simpleLabel ]]</button><sc-if value="[[ simple ]]" hint-placeholder-val="[[ false ]]"><span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span></sc-if></span>
    </section>
    <div style="display: flex; align-items: center; gap: 12px; padding: 0 4px"><span style="color: {EVG}; display: flex">{ic('shield', 20)}</span><span style="flex-grow: 1; font-size: 14px; color: {SEC}">Evidence: early. Check-ins add more, apart from the score.</span></div>
    <div style="flex-grow: 1"></div>
    {primary('Choose your first step', 'R7-FirstStep.dc.html')}
    <a href="R7-Me.dc.html" style="height: 44px; flex-shrink: 0; margin-top: -6px; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600; color: {EVG}">See your full profile</a>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const simple = !!st.simple;
    return {
      simple, toggleSimple: () => this.setState({ simple: !simple }), simpleLabel: simple ? 'Show the original' : 'Explain it more simply',
      meaning: simple ? 'You manage day-to-day money well. A surprise cost would be hard right now. A small cushion is the next thing to learn about.'
        : 'Your everyday money habits are a real strength. The most room to grow is being ready for surprises: an unexpected cost would likely knock your plans off course.'
    };
  }
}'''
    return phone('Your first profile', body, logic, h=1090)


# ---------------------------------------------------------------- Choose your first step

FIRST = [('pool', LIME, 'Start a starter safety net', 'Move R 100 into a separate pocket on payday.', '5 min a week'),
         ('moon', NIGHT, 'Learn where to keep one', 'A six-minute lesson on safe places for a safety net.', '6 min'),
         ('doc', MIST, "List last year's surprises", "Write down three costs you didn't see coming.", '10 min')]
PLAN = [('This week', '[[ stepName ]]'), ('Next week', 'A lesson that goes with it'), ('Week 3', 'One small action, your size'), ('13 Oct', 'Your 30-day check-in')]


def first_step():
    cards = ''
    for i, (icn, bg, t, d, tm) in enumerate(FIRST):
        fg = MOON if bg == NIGHT else EVG
        glyph = icon(icn, 22, fg) if icn in ('pool', 'moon') else ic(icn, 22, fg)
        cards += f'''<button onClick="[[ f{i} ]]" aria-pressed="[[ fOn{i} ]]" style="border-radius: {R_L}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ fBw{i} ]]px {EVG}; padding: 14px; display: flex; gap: 14px; align-items: flex-start; text-align: left; transition: box-shadow .18s">
          <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {bg}; display: flex; align-items: center; justify-content: center">{glyph}</span>
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {MUTED}">{d}</span><span class="chip" style="align-self: flex-start; height: 24px; background: {MIST}; color: {SEC}; margin-top: 2px">{tm}</span></span>
          <span aria-hidden="true" style="width: 24px; height: 24px; flex-shrink: 0; box-sizing: border-box; border-radius: 999px; border: 2px solid [[ fRc{i} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: [[ fRf{i} ]]"></span></span>
        </button>'''
    plan = ''.join(f'''<div style="display: flex; gap: 12px; align-items: flex-start">
          <span style="display: flex; flex-direction: column; align-items: center; align-self: stretch"><span style="width: 14px; height: 14px; border-radius: 999px; box-sizing: border-box; {f"background: {LIME}; border: 2px solid {EVG};" if i == 0 else f"border: 2px solid {EVG};" if i < 3 else f"border: 2px dashed {EVG};"}"></span>{f'<span style="flex-grow: 1; width: 2px; background: #BFD9D2; margin: 2px 0"></span>' if i < 3 else ''}</span>
          <span style="display: flex; flex-direction: column; gap: 2px; padding-bottom: 10px; margin-top: -3px"><span style="font-size: 12px; color: {SEC}">{w}</span><span style="font-size: 15px; font-weight: 600">{t}</span></span></div>''' for i, (w, t) in enumerate(PLAN))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 14px">
    <header style="display: flex; align-items: center; justify-content: space-between">{back('R7-Reveal.dc.html')}<span style="font-size: 17px; font-weight: 600">Your first step</span>{sample_chip()}</header>
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 4px">{title('Pick one step for this week.', 'Chosen for your focus: ready for surprises. You can change it next week.', 32)}</div>
    <div role="radiogroup" aria-label="Your first step" style="display: flex; flex-direction: column; gap: 8px">{cards}</div>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {INK}; padding: 16px 16px 6px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 16px; font-weight: 600; color: {EVG}">Your next 30 days</span><span class="hand" style="font-size: 22px; color: {EVG}; {HF}">One step is enough.</span></span>
      <div style="display: flex; flex-direction: column">{plan}</div>
    </section>
    <div style="flex-grow: 1"></div>
    {primary('Start this step', 'R7-Auth-Notify.dc.html')}
  </div>'''
    names = [t for _i, _b, t, _d, _m in FIRST]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const f = st.f == null ? 0 : st.f;
    const names = %(names)s;
    const v = { stepName: names[f] };
    for (let i = 0; i < 3; i++) {
      v['f' + i] = () => this.setState({ f: i }); v['fOn' + i] = f === i; v['fBw' + i] = f === i ? 2 : 0;
      v['fRc' + i] = f === i ? '%(evg)s' : '#A9B6AF'; v['fRf' + i] = f === i ? '%(evg)s' : 'transparent';
    }
    return v;
  }
}''' % dict(names=names, evg=EVG)
    return phone('Your first step', body, logic, h=1000)


BOARDS = [('R7-Auth-Signin', signin), ('R7-Auth-Code', code), ('R7-Auth-Profile', profile), ('R7-Auth-Consent', consent),
          ('R7-Reveal', reveal), ('R7-FirstStep', first_step), ('R7-Auth-Notify', notify), ('R7-Auth-Lock', lock), ('R7-Auth-Back', welcome_back)]
