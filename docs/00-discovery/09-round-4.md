# 09 · Round 4: five moments, three directions

> **Status:** Published on canvas page `r4`, 25 Sep 2026. Built from the [Round 3 review](08-round-3-review.md). Every board was rendered and clicked through locally before publishing (D-026).
> **Ian's brief:** "Let's iterate Round 4. I don't know which human direction; I'd love to see what this looks like. Mentor and Circle sound good."

## What's on the page

There are 11 boards instead of Round 3's 35. Nine of them are interactive (press Play).

| Row | Boards | What it answers |
|---|---|---|
| 1 | **Members**, **E, tightened** | Who we design for; the rules every screen follows |
| 2 | **Moment 1 three ways**: Mentor, Journal, Circle | Q-29: who is AWO to her? Same result, same member, three tellings |
| 3 | **Today**, **Moments 2–5** | Mentor as the spine and Circle as the heart, across the rest of the loop |
| 4 | **The hard moments** | Day one, a missed week, coming back after a month, offline |

## The three directions, on the same moment

All three show Naledi's first result (sample values: stage 2 of 4, readiness 63, Resilience lowest). Each one asks how the result lands. "Lower than I hoped" is its own branch, not an afterthought.

- **Mentor:** one idea at a time, words before numbers. Earlier sentences fade as the next one arrives. The result is four plain rows, then the one step on an evergreen card.
- **Journal:** the result is page one of her story. Her words from the starter check ("I want to stop dreading the end of the month") are highlighted inside the interpretation. She writes or records how it feels, and it becomes the first entry on her timeline.
  - Her words are set in a serif italic (Newsreader) and AWO's in Geist. This is an idea to test, not yet part of E.
- **Circle:** the result arrives with faces. A member voice sits beside the result ("I started at stage 2 in March"), and the hard branch answers with another woman's words ("I cried a bit when I saw mine"). It ends by inviting her to a circle of eight, with an explicit privacy line: first names and lessons, never numbers.

## The loop in Mentor + Circle

| Board | Member | The moment |
|---|---|---|
| Today | Naledi | One step on an evergreen card (choosing an amount completes it), the circle (cheer Amara, Grace's voice note), and a three-point story line |
| Moment 2 | Wanjiru, Nairobi, KSh | A takings note for a week: choose when, log tonight's numbers, see the week. Her buddy's message arrives, not confetti. Then "what did you notice?" |
| Moment 3 | Amara, London, £ | A check-in where the safety net went down (£1,200 to £650) because she sent money home. "Your safety net did its job this month." No red: decreases are neutral grey, and only gains use lime |
| Moment 4 | Thandi (lesson) | Dark, with Ola. Savings groups in three minutes: a ring of twelve members and months, the pot moving to December, a March surprise, one question with nuanced feedback, one reflection, and Ola's jump |
| Moment 5 | The circle | Amara's milestone with a cheer, Grace's voice note (waveform, "show the words"), and the week's question: "What did you say no to this week?" |

## Rules applied (the "E, tightened" board)

- **One job per colour.**
  - Evergreen is the main action on light screens.
  - Lime is for progress and wins, and is the main action on dark screens. It never sits on white.
  - Blush is for people only.
  - Pool is water.
  - Iris is only for Ola's glow.
  - Learn and Ask are always dark (proposed, Q-30).
- **Calmer type.**
  - Bricolage 600 at 26px for titles, and 44px only for a real moment.
  - Geist for body text at 17px, with 13px for secondary text and a 12px floor.
  - Heavy condensed display type stays in marketing.
- **One main button per screen,** with touch targets of at least 44px.
- **Four speeds of motion:** 90 ms for a touch, 180 ms for a change, 280 ms for a new screen, 600 ms for a moment. Reduce motion turns loops off.
- **Retired:**
  - ripple rings on results;
  - arches on every photo;
  - chips floating over faces;
  - points and streak counts;
  - iris on everyday screens;
  - stepping stones outside the logo;
  - red for a month that went down.

## Members (sample)

- **Naledi, 29, Johannesburg:** salaried, helps her brother with university costs. Her currency formats as `R 12 500,00`.
- **Wanjiru, 34, Nairobi:** runs a homeware stall and pays into a chama. Her currency formats as `KSh 12,500.00`.
  - Changed from the review's "salon owner" because the free stock library had no salon photos. Either works.
- **Amara, 38, London:** a nurse who sends money home to Enugu. Her currency formats as `£1,250.00`.
- **Supporting cast:**
  - Thandi (lesson and circle);
  - Grace, 61 (the circle's older voice);
  - Lindiwe, Zodwa and Palesa (day one).

Photos are stand-ins from nappy.co, chosen for range: focused, determined, working it out, tired at sixty, calm. The photo brief is on the Members board (Q-27).

## Self-review: what rendering caught before publishing

- Text inside SVG that is bound to data does not render in the canvas runtime. The lesson ring's month letters and centre amounts were invisible, so they are now HTML laid over a static SVG ring.
- An image `src` or an SVG `width` bound to data inside a loop throws errors on the first parse. Write repeated images out literally, and size SVGs with a style binding.
- Flex children shrink by default. The circle's cheer card was squashed until the cards were set not to shrink and the board was made taller.
- The Today screen's story line sat under the tab bar at 844px, so that board is 940px tall.
- On the hard-moments board, four phones didn't fit at 64px padding. It now uses 48px.

## Known gaps

- Grace's portrait is black and white, the only older-woman photo in the free library. A real shoot fixes this (Q-27).
- The voice-note and microphone buttons are visual only.
- The ring chart uses single-letter month labels, and its accessible label carries the meaning.
- All interpretations, stages, amounts and lesson content are samples. The governed library, scoring rules and lesson review are Q-13, Q-14 and Q-07.
