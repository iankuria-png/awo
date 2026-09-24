# 07 · Brand, illustration and motion (Round 2)

> **Status:** Draft v0 for discussion (24 Sep 2026).
> **Canvas:** [AWO Direction Explorations](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9), page **Round 2**. Round 1 is kept on its own page for comparison.

## What Round 1 taught us (owner feedback)

| Direction | Verdict | What changed in Round 2 |
|---|---|---|
| **A · Oasis** | Liked. The Home screen could improve. | New Home built around the 30-day loop, a "how does money feel" check, and a floating glass nav. Added a welcome screen and a tappable starter-check question. The background moved off cream. |
| **B · Night Oasis** | The Ask screen is strong but weak on micro-interaction and animation. Could be the Learn page. | Re-cast as the **Learn and Ask** area, with a mascot (Ola), a lesson path, typing and voice states, and an animated composer. |
| **C · Editorial Violet** | Rejected: text-heavy, "like a 2005 app". | Retired. Replaced by **D · Human**, a people-first direction. |

## Avoiding "AI-made" tells (new rule D13)

The `frontend-design` plugin lists the traits that make generated design look generated. Round 1 had several:

- a warm cream background (#F4F1EA-ish),
- a near-black background with one acid accent,
- ALL-CAPS eyebrow labels above every heading,
- "A · B · C" meta strings, and
- numbered 01/02/03 markers on content that isn't a sequence.

Round 2 removes them. **D13:** where the brief leaves a choice open, don't spend it on a default. Labels are sentence case, numbering appears only for real sequences, and each surface has one bold idea.

## Wordmark directions

| | Idea | Motion idea | Strength | Watch-out |
|---|---|---|---|---|
| **Ripple** | AWO in capitals; the O is a ripple | Rings breathe while loading | Confident, institutional | Capitals can feel corporate |
| **Wave** | Lowercase awo; the w is water, the o a ripple | The w draws itself like a wave | Friendly, ownable, tells the oasis story | Needs careful drawing to stay legible at small sizes |
| **Stepping stones** | Three growing stones as the mark | Stones land one by one | App icon works without letters | Less distinctive as a wordmark |

My lean: **Wave** as the wordmark, with the **Stepping stones** or **Ripple O** as the app icon. They can mix.

## Iconography

- **Hand-drawn set (16 icons):** ink line on an offset soft blob, with a subtle wobble (an SVG displacement filter, so the drawing stays editable). Used for features, onboarding, goals and empty states. The blob colour follows the direction.
- **Clean line set:** used for navigation and small UI at 24px, where hand-drawn detail becomes noise. It is drawn on the same shapes, so the two families feel related.
- **Savings group icon:** a circle of people around a coin. Stokvels, chamas and susus appear as real financial instruments, which is local truth rather than decoration (D5).

## Illustration and people

- **D · Human** uses faceless, flat cut-paper portraits drawn for this round. They show a range of skin tones, ages and hair (afro, braids, locs, puff, short crop, grey curls). They are **placeholders**; the photo libraries are blocked from Claude's environment, and real people deserve better than an AI sketch.
- **Recommendation:** commission an illustrator for a small people system (6–10 characters, several poses), or run a photography shoot with real members. The Round 2 portraits act as the brief: dignified, contemporary and specific (D4).
- **Brand illustration (A):** stepping stones across water with ripples and a sprout. It is abstract, calm and meaningful, and uses no stereotyped motifs.

## Ola, the mascot (proposal)

- A **water drop** from the oasis, with five states: idle, listening, thinking, celebrating and resting.
- **Lives only in Learn and Ask.** It never appears on a DIVA result, so results stay calm and serious (D8).
- Celebrates **effort** (lessons, actions), never scores.
- Is built for **Rive**: one file, one state machine, runtimes for web, iOS and Android. It falls back to still poses when motion is reduced.
- The name is a working name (see Q-26).

## Motion principles

| # | Principle | Example on the canvas |
|---|---|---|
| M1 | **Every tap answers back.** A ripple spreads from the touch point and the control dips slightly. | Motion board, "Every tap answers back" |
| M2 | **Progress grows once.** Rings fill and numbers count up when a screen first opens, never on every scroll. | Journey ring, loop tracker on A · Home v2 |
| M3 | **Waiting feels alive.** AI work shows the companion thinking, never a bare spinner. | Ola thinking, typing dots |
| M4 | **Celebrate the step, not the score.** Bursts for finished lessons and actions; nothing for DIVA results. | "Step done" badge |
| M5 | **The nav floats, then gets out of the way.** Frosted glass that shrinks while reading. | Floating nav demo |
| M6 | **Less motion, same meaning.** With reduce-motion on, slides become cross-fades and loops stop. Nothing important depends on animation. | Reduced-motion tile |

**Tokens (draft):** 90 ms tap feedback · 180 ms toggles and chips · 280 ms cards and sheets · 600 ms wins and onboarding. Ease-out for arrivals; spring only for wins.

## Tooling for motion and illustration

| Need | Tool | Why |
|---|---|---|
| Interactive character and state machines (Ola) | **Rive** | One file with states; runtimes for web, React Native and native. Small files. |
| Illustrative loops (onboarding, empty states, success) | **Lottie / dotLottie** (LottieFiles) | Industry standard. Designers export from After Effects or Figma plugins. |
| UI transitions on web | **Motion** (motion.dev, formerly Framer Motion) | Layout animations, gestures, reduced-motion support. |
| UI transitions on native | **React Native Reanimated** (+ Skia for custom drawing) | 60fps on the UI thread, which matters on mid-range Android. |
| Design and prototyping | **Figma** (with its motion features) | The owner's tool. The Figma plugin is installed here; connect the Figma connector to let Claude work in your files. |
| People | An **illustrator** and/or a **motion designer** (freelance) | These are craft roles. Claude can brief, prototype and implement, but a signature character and people system are worth commissioning. |

**Performance guardrail:** animation assets have budgets too. Rive and Lottie files are loaded lazily, never block first paint, and are skipped on "data saver".
