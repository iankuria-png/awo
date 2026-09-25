from lib import *

P = 'v3'


def floatbar(active, bg, idle, line='rgba(255,255,255,.08)'):
    out = [f'<nav aria-label="Main" style="position: absolute; left: 8px; right: 8px; bottom: 14px; height: 66px; box-sizing: border-box; border-radius: 33px; background: {bg}; box-shadow: inset 0 0 0 1px {line}; padding: 5px 4px; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); font-size: 12px; text-align: center; color: {idle}">']
    for name, ic in AREAS:
        if name == active:
            pb, fg, _ = ACTIVE[name]
            out.append(f'<span aria-current="page" style="border-radius: 28px; background: {pb}; color: {fg}; font-weight: 600; letter-spacing: -0.01em; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px">{icon(ic, 20)}{name}</span>')
        else:
            out.append(f'<span style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px">{icon(ic, 20)}{name}</span>')
    out.append('</nav>')
    return ''.join(out)


def home():
    stick = 'position: absolute; top: 648px; width: 108px; height: 96px; box-sizing: border-box; border-radius: 20px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between'
    return f'''<div class="ph" style="background: {EVG}; color: #FFFFFF">
  <span style="position: absolute; left: 20px; top: 56px; font-size: 15px; font-weight: 500; color: {ON_EVG}">Hi Naledi</span>
  <img class="face" src="{IMG['naledi']}" alt="Naledi" style="position: absolute; right: 20px; top: 46px; width: 40px; height: 40px; box-shadow: 0 0 0 2px {LIME}">
  <h2 class="d" style="position: absolute; left: 20px; top: 88px; font-size: 64px">It's payday.</h2>
  <div style="position: absolute; right: 18px; top: 168px; width: 164px; height: 290px">
    {pool(164, 290, 'v3Pool', rimw=4)}
    <sc-if value="{{{{ moved }}}}" hint-placeholder-val="{{{{ false }}}}">
      <span class="drop" style="left: 52px; top: 110px"></span><span class="drop" style="left: 78px; top: 96px; animation-delay: .12s"></span><span class="drop" style="left: 104px; top: 112px; animation-delay: .24s"></span>
      <span class="splash" style="left: 34px; top: 170px; width: 96px; height: 20px"></span>
    </sc-if>
  </div>
  <span class="d" style="position: absolute; left: 18px; top: 206px; font-size: 104px; color: {LIME}; font-variant-numeric: tabular-nums; text-shadow: 3px 0 0 {EVG}, -3px 0 0 {EVG}, 0 3px 0 {EVG}, 0 -3px 0 {EVG}, 2px 2px 0 {EVG}, -2px -2px 0 {EVG}, 2px -2px 0 {EVG}, -2px 2px 0 {EVG}">{{{{ amountText }}}}</span>
  <span style="position: absolute; left: 20px; top: 314px; width: 170px; font-size: 16px; line-height: 1.4; color: {ON_EVG}">of R 5 000 in your safety net</span>
  <span class="d" style="position: absolute; left: 20px; top: 486px; font-size: 36px">Pay yourself first.</span>
  <span style="position: absolute; left: 20px; top: 526px; font-size: 15px; color: {ON_EVG}">Move R 100 in before anything else.</span>
  <div style="position: absolute; left: 20px; right: 20px; top: 568px">
    <sc-if value="{{{{ notMoved }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="pill" onClick="{{{{ doMove }}}}" style="height: 56px; font-size: 17px; background: {LIME}; color: {EVG}">I moved R 100</button></sc-if>
    <sc-if value="{{{{ moved }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="pill" onClick="{{{{ undoMove }}}}" aria-label="Done for this week. Tap to undo." style="height: 56px; font-size: 17px; background: transparent; color: {LIME}; box-shadow: inset 0 0 0 2px {LIME}; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{icon('check', 20, LIME, 2.4)}Done for this week</button></sc-if>
  </div>
  <section style="{stick}; left: 18px; background: {NIGHT}; color: {MOON}; transform: rotate(-4deg)">{moon(26, 'half', now=True)}<span class="d" style="font-size: 19px; line-height: .95">Where to keep it</span></section>
  <section style="{stick}; left: 141px; background: {LIME}; color: {EVG}; transform: rotate(3deg)"><span aria-hidden="true" style="width: 22px; height: 28px; box-sizing: border-box; border-radius: 11px 11px 3px 3px; border: 3px solid {EVG}"></span><span class="d" style="font-size: 26px">Stokvel</span></section>
  <section style="{stick}; left: 264px; background: {BLUSH}; color: {BLUSH_INK}; transform: rotate(-2deg)"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 32px; height: 32px"><span style="font-size: 13px; font-weight: 600; line-height: 1.25">Wanjiru cheered you</span></section>
  {floatbar('Home', EVG_D, ON_EVG)}
</div>'''


def learn():
    arc = [8, 3, 0, 0, 3, 8]
    moons = ''.join(f'<span style="display: block; margin-top: {o}px">{m}</span>' for o, m in zip(arc, [moon(26, 'full'), moon(26, 'full'), moon(26, 'half', now=True), moon(26, 'new'), moon(26, 'new'), moon(26, 'new')]))
    return f'''<div class="ph dk" style="background: {NIGHT}; color: {MOON}">
  <div aria-hidden="true" style="position: absolute; right: -44px; top: 24px; filter: drop-shadow(0 0 40px rgba(134,227,196,.3))">{moon(360, 'half', craters=True, dark=DEEP)}</div>
  <h2 class="d" style="position: absolute; left: 20px; top: 56px; font-size: 32px">Learn</h2>
  <button onClick="{{{{ doOla }}}}" aria-label="Say hello to Ola" style="position: absolute; left: 26px; top: 236px; width: 124px; height: 124px">
    <sc-if value="{{{{ olaIdle }}}}" hint-placeholder-val="{{{{ true }}}}"><span style="display: block; animation: bob 3.2s ease-in-out infinite">{ola(P, 124, look=10)}</span></sc-if>
    <sc-if value="{{{{ ola }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="jump" style="display: block">{ola(P, 124, happy=True)}</span></sc-if>
  </button>
  <sc-if value="{{{{ olaIdle }}}}" hint-placeholder-val="{{{{ true }}}}"><span style="position: absolute; left: 34px; top: 372px; font-size: 13px; color: {NMUTED}">Tap Ola to say hello</span></sc-if>
  <sc-if value="{{{{ ola }}}}" hint-placeholder-val="{{{{ false }}}}"><span style="position: absolute; left: 156px; top: 226px; padding: 10px 14px; border-radius: 18px 18px 18px 4px; background: {MOON}; color: {NIGHT}; font-size: 15px; font-weight: 500; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">Ready when you are.</span></sc-if>
  <h3 class="d" style="position: absolute; left: 20px; top: 410px; width: 350px; font-size: 80px">Where to keep it</h3>
  <span style="position: absolute; left: 20px; top: 568px; font-size: 15px; color: {NMUTED}">Lesson 3 of 6 in Safety nets. 6 minutes.</span>
  <div role="img" aria-label="Lessons 1 and 2 done, lesson 3 next, 3 more to come" style="position: absolute; left: 20px; top: 600px; display: flex; gap: 14px">{moons}</div>
  <button class="pill" style="position: absolute; left: 20px; right: 20px; top: 670px; width: auto; height: 56px; font-size: 17px; background: {LIME}; color: {INK}">Start the lesson</button>
  {floatbar('Learn', DEEP, NMUTED)}
</div>'''


def vault():
    arch = 'border-radius: 175px 175px 32px 32px'
    mini = 'position: absolute; top: 666px; width: 108px; height: 84px; box-sizing: border-box; border-radius: 54px 54px 16px 16px; padding: 0 8px 12px; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; text-align: center'
    return f'''<div class="ph" style="background: {LIME}; color: {EVG}">
  <h2 class="d" style="position: absolute; left: -6px; top: 34px; font-size: 168px; line-height: .8">Vault</h2>
  <span style="position: absolute; left: 22px; top: 170px; font-size: 14px; font-weight: 600">12 words kept</span>
  <div style="position: absolute; left: 20px; top: 196px; width: 350px; height: 452px; perspective: 1600px">
    <div class="flipper" style="transform: {{{{ flipTf }}}}">
      <section class="face-f" aria-hidden="{{{{ flipped }}}}" style="{arch}; background: {EVG}; color: #FFFFFF; padding: 118px 26px 24px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px">
        <span class="d" style="font-size: 88px; color: {LIME}">Stokvel</span>
        <span style="font-size: 15px; color: {ON_EVG}">Say it: stok-fel</span>
        <span style="font-size: 17px; line-height: 1.45">A savings group. Members pay in every month and take turns to receive the pot.</span>
        <button class="pill" tabindex="{{{{ frontTab }}}}" onClick="{{{{ doFlip }}}}" style="margin-top: auto; background: {LIME}; color: {EVG}">{icon('flip', 18, EVG)}Flip for an example</button>
      </section>
      <section class="face-b" aria-hidden="{{{{ notFlipped }}}}" style="{arch}; background: #FFFFFF; color: {INK}; padding: 118px 26px 24px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 14px">
        <span style="font-size: 14px; font-weight: 600; color: {EVG}">For example</span>
        <span style="font-size: 20px; line-height: 1.45">Thandi and eleven neighbours each pay R 500 a month. Each month one of them takes home R 6 000. December is Thandi's turn.</span>
        <span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">Sample</span>
        <button class="pill" tabindex="{{{{ backTab }}}}" onClick="{{{{ doFlip }}}}" style="margin-top: auto; background: {EVG}; color: #FFFFFF">{icon('flip', 18, '#FFFFFF')}Flip back</button>
      </section>
    </div>
  </div>
  <span style="position: absolute; right: 12px; top: 214px; padding: 9px 14px; border-radius: 999px; background: {BLUSH}; color: {BLUSH_INK}; font-size: 14px; font-weight: 600; transform: rotate(8deg); box-shadow: 0 6px 16px -8px rgba(42,15,24,.5)">Word of the week</span>
  <span style="{mini}; left: 20px; background: #FFFFFF"><span class="d" style="font-size: 20px">Safety net</span></span>
  <span style="{mini}; left: 141px; background: {POOL}"><span class="d" style="font-size: 20px">Chama</span></span>
  <span style="{mini}; left: 262px; background: transparent; box-shadow: inset 0 0 0 3px {EVG}"><span class="d" style="font-size: 20px">Interest</span></span>
  {floatbar('Vault', EVG, '#CFE9A0')}
</div>'''


def community():
    rings = ''.join(f'<span aria-hidden="true" style="position: absolute; left: {195 - r}px; top: {500 - r}px; width: {2 * r}px; height: {2 * r}px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: {o}"></span>' for r, o in ((70, .16), (140, .11), (210, .08), (280, .05)))
    bubble = 'position: absolute; max-width: 230px; padding: 12px 14px; background: #FFFFFF; color: ' + INK + '; font-size: 15px; line-height: 1.4'
    return f'''<div class="ph" style="background: {BLUSH}; color: {BLUSH_INK}">
  {rings}
  <span aria-hidden="true" style="position: absolute; left: 125px; top: 430px; width: 140px; height: 140px; border-radius: 999px; border: 2px solid {BLUSH_INK}; animation: spread 3.6s cubic-bezier(.2,.8,.2,1) infinite"></span>
  <span style="position: absolute; left: 20px; top: 56px; font-size: 15px; font-weight: 600; color: {BLUSH_2}">This week in the Safety net circle</span>
  <h2 class="d" style="position: absolute; left: 20px; top: 86px; width: 350px; font-size: 58px">What did you say no to this week?</h2>
  <img class="face" src="{IMG['thandi']}" alt="Thandi" style="position: absolute; left: 20px; top: 300px; width: 54px; height: 54px; box-shadow: 0 0 0 3px {BLUSH}">
  <span style="{bubble}; left: 84px; top: 300px; border-radius: 20px 20px 20px 6px"><strong style="font-weight: 600">Thandi</strong> A second pair of work shoes. The first pair is fine.</span>
  <img class="face" src="{IMG['wanjiru']}" alt="Wanjiru" style="position: absolute; right: 20px; top: 400px; width: 54px; height: 54px; box-shadow: 0 0 0 3px {BLUSH}">
  <div style="position: absolute; right: 84px; top: 400px; display: flex; flex-direction: column; align-items: flex-end; gap: 8px">
    <span style="{bubble}; position: static; border-radius: 20px 20px 6px 20px"><strong style="font-weight: 600">Wanjiru</strong> Lending to my cousin again. I said: after the school fees.</span>
    <button onClick="{{{{ doCheer }}}}" aria-pressed="{{{{ cheered }}}}" style="position: relative; height: 40px; padding: 0 14px; border-radius: 999px; background: {{{{ cheerBg }}}}; color: {{{{ cheerFg }}}}; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s">
      <sc-if value="{{{{ cheered }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span><span class="rp" style="inset: 0; color: {BLUSH_INK}; animation-delay: .18s"></span></sc-if>
      {icon('ripple', 18)}{{{{ cheerLabel }}}}<span style="font-weight: 500; opacity: .75">{{{{ cheerCount }}}}</span>
    </button>
  </div>
  <img class="face" src="{IMG['grace']}" alt="Grace" style="position: absolute; left: 20px; top: 548px; width: 54px; height: 54px; box-shadow: 0 0 0 3px {BLUSH}">
  <span style="{bubble}; left: 84px; top: 548px; border-radius: 20px 20px 20px 6px"><strong style="font-weight: 600">Grace</strong> Takeaway on Friday. Cooked instead, and it was nicer.</span>
  <div style="position: absolute; left: 20px; right: 20px; top: 660px; display: flex; gap: 8px">
    <span style="flex-grow: 1; height: 48px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; padding: 0 18px; font-size: 15px; color: {MUTED}">Share yours</span>
    <span aria-hidden="true" style="width: 48px; height: 48px; border-radius: 999px; background: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('send', 18, BLUSH)}</span>
  </div>
  <span style="position: absolute; left: 20px; right: 20px; top: 720px; font-size: 13px; color: {BLUSH_2}">Your circle sees first names and answers. Never amounts.</span>
  {floatbar('Community', BLUSH_INK, '#E7A9BC')}
</div>'''


def me():
    st = stones(390, 130, [(52, 104, 38, 16), (150, 78, 46, 19), (256, 52, 42, 17), (346, 28, 34, 14)],
                [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='6 6')
    waves = ''.join(f'<path d="M{x} {y}q10-6 20 0t20 0" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" opacity=".8"></path>' for x, y in ((80, 124), (190, 100), (296, 74)))
    chip = 'height: 54px; box-sizing: border-box; border-radius: 18px; background: #FFFFFF; padding: 0 14px; display: flex; align-items: center; gap: 10px'
    dims = [('Everyday money', 71), ('Ready for surprises', 48), ('Knowing your options', 60), ('Clear goals', 69)]
    chips = ''.join(f'<div style="{chip}; {"box-shadow: inset 0 0 0 2px " + EVG if v == 48 else ""}"><span class="d" style="font-size: 28px">{v}</span><span style="font-size: 13px; line-height: 1.2; color: {SEC}">{n}</span></div>' for n, v in dims)
    return f'''<div class="ph" style="background: {POOL}; color: {EVG}">
  <span style="position: absolute; left: 20px; top: 58px; font-size: 16px; font-weight: 600">Naledi</span>
  <span aria-label="Settings" role="img" style="position: absolute; right: 20px; top: 48px; width: 44px; height: 44px; border-radius: 999px; background: rgba(255,255,255,.7); display: flex; align-items: center; justify-content: center">{icon('gear', 20, INK)}</span>
  <span class="d" style="position: absolute; left: 20px; top: 104px; font-size: 64px">Stage</span>
  <span class="d" style="position: absolute; left: 12px; top: 150px; font-size: 232px; line-height: .78">2</span>
  <span class="d" style="position: absolute; left: 140px; top: 262px; font-size: 64px; opacity: .55">of 4</span>
  <span class="chip" style="position: absolute; right: 20px; top: 116px; border: 1px dashed {EVG}; color: {EVG}">Sample</span>
  <div role="img" aria-label="Stage 2 of 4, shown as four stepping stones across water" style="position: absolute; left: 0; top: 330px; width: 390px; height: 130px">
    <svg width="390" height="130" viewBox="0 0 390 130" aria-hidden="true" style="position: absolute; left: 0; top: 0; overflow: visible">{waves}</svg>
    <div style="position: absolute; inset: 0">{st}</div>
    <img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 118px; top: 8px; width: 64px; height: 64px; box-shadow: 0 0 0 4px {LIME}; animation: bob 3.4s ease-in-out infinite">
  </div>
  <span style="position: absolute; left: 20px; right: 20px; top: 480px; font-size: 19px; line-height: 1.4; color: {INK}">Everyday money is a real strength. Most room to grow: being ready for surprises.</span>
  <div style="position: absolute; left: 20px; right: 20px; top: 574px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{chips}</div>
  <div style="position: absolute; left: 20px; right: 20px; top: 706px; display: flex; gap: 8px"><span class="chip" style="background: #FFFFFF; color: {EVG}">{icon('check', 14, EVG, 2.6)}Reviewed by AWO</span><span class="chip" style="background: rgba(255,255,255,.55); color: {SEC}">Evidence: early</span></div>
  {floatbar('Me', EVG, ON_EVG)}
</div>'''


if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    logic = LOGIC % dict(poolH=290, cheerOn=BLUSH_INK, cheerOff='#FFFFFF', cheerOnFg=BLUSH, cheerOffFg=BLUSH_INK)
    html = board('Volume 3: Playful',
                 'Every area wears its colour edge to edge. Type becomes the image, the shapes break the frame and a few things move on their own. Still one main button per screen.',
                 None, [home(), learn(), vault(), community(), me()], 2190, 1150, '#E4EAE6', logic, extra_defs=ola_defs(P))
    open(out, 'w').write(html)
    print('wrote', out, len(html))
