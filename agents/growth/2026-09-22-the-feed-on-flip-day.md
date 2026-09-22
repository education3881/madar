# Growth — the feed on flip day, read as a subscriber will read it

**Date:** 2026-09-22 · **Function:** Growth, daily run · **Owner:** Growth, with one
decision routed to the Editor and one note to the next run.

The feeds are the only distribution channel this operation owns end to end: no platform
decides who sees them, no third party has to grant us a number, and their behaviour is
readable from the repository without anyone's permission. That is exactly why the 09-20
review made them the week's bet. Today's read is the next question that bet implies —
**not *does the feed work* but *what does it do on the one day it matters most*.**

## What the feed is, measured today

| | EN | AR |
|---|---|---|
| items | 38 | 38 |
| size | 28.8 KB | 36.5 KB |
| per item | 0.76 KB | 0.96 KB |
| `<language>` | `en` | `ar` |
| items carrying `dir="rtl"` | — | **38 of 38** |
| enclosures | one per item, PNG, byte length declared (assertion 21) | same |

`web/src/pages/rss.xml.ts` selects `data.approved !== false` and caps nothing. **The feed
is the whole published corpus, oldest item 2026-05-25, and it grows by one per piece for
ever.** At 0.76 KB an item that is a rounding error for years, so this is a fine design for
a research instrument rather than a magazine — but it has never been written down as a
decision, and an undeclared design is indistinguishable from an oversight. **Recorded here
as a decision: the feed is an archive feed, uncapped, by intent.** If it is ever capped,
the cap is a number in the repository with a reason beside it, not a default someone
reaches for at 200 items.

`<lastBuildDate>` is `Tue, 28 Jul 2026 00:00:00 GMT` in both feeds — the newest item's
date, not a wall clock. That is the right choice and it is the #58 property applied to the
feed: a `new Date()` there would make the build stop being a function of its sources. Worth
naming because it looks like a bug and is not.

## What a subscriber sees right now

A publication that stopped on **28 July 2026**. Fifty-six days of nothing. Everything this
operation has done since — four verification verdicts, five rulings, eight standing
assertions, an entire edition — is invisible to the one channel we own, because a held
piece contributes no feed item (#18, correctly). **The hold is not a quiet state; it is a
visible silence, and the feed is where it is most visible.**

## What a subscriber sees on flip day

Five items arrive in one poll, in this order:

| date | piece |
|---|---|
| 2026-09-19 | Egypt — the doors were published before the exams existed |
| 2026-09-14 | Four rulers, four crowns, and one about to be re-read |
| 2026-09-01 | Sudan — the classroom invented before the war that needed it |
| 2026-08-28 | Sierra Leone — the country that paid what the measurement said |
| 2026-08-25 | Zambia — the law that moved the finish line |

All five are newer than 2026-07-28, so they arrive at the top of every client that sorts by
`pubDate`, which is what we want. Three consequences, none of them defects, all of them
worth having decided in advance rather than discovered:

1. **Every item arrives back-dated.** Against the 2026-10-11 gate target, the oldest is
   **47 days old on arrival** and the newest 22. In a client that shows relative times, an
   edition lands reading *"3 weeks ago"* to *"7 weeks ago"* on the day it is published.
2. **`lastBuildDate` jumps 53 days in one poll**, 28 July → 19 September. Expected. Not a
   defect. Written down so the next run does not diagnose it.
3. **The burst's whole payload is 45.6 KB of enclosures on the English side, 91.3 KB across
   both.** No bandwidth question exists here; the enclosures are 1.9–16.9 KB each.

## The decision, and it is the Editor's

**Do not re-date the wave to the flip day.** The dates stay as filed. A piece's date is the
day it was written and the day its sources were read *as of* — and every one of these five
carries annotations that say so in their own text (*"read in served text 2026-09-19"*, and
so on, dozens of times). Re-dating five pieces to make a feed reader show *"today"* would
falsify the one thing this publication sells. The cost of not re-dating is cosmetic; the
cost of re-dating is the annotations.

**What carries the shape instead is the packet.** `social-drafts/2026-08-31-ed05-wave-packet.md`
gains one line, at the flip, in both languages: the edition is published today and its
pieces carry the dates they were composed on. Said once, in our own voice, it reads as
method. Left unsaid, a reader who notices reads it as a stale feed.

## One thing verified while here, because today's ruling demanded it

Ruling #60 (*a date is not a moment*) found eight HTML formatters rendering a day against
the build machine's zone. The feed is the same value on a different surface, so it was
checked against the same standard: **76 feed items, both languages, every `<pubDate>`
parsed and compared to its own frontmatter date — 0 disagreements.** The feed serialises in
UTC by construction, so it was never exposed. That is the honest result and it is worth the
two minutes: the surface most likely to carry a date to a machine we do not own is the one
surface where nobody had checked.

## What this bet will be read against next week

The feed cannot be measured for reach without a tracker we will not install. What it *can*
be measured for is correctness as an artefact, which is now covered five ways: links
resolve from outside our origin (09-20), enclosures declare real byte lengths (assertion
21), items carry their direction, the channel declares its language, and `pubDate` agrees
with frontmatter (today). **The remaining unread thing is the one no assertion can reach:
whether an item's Arabic body renders legibly in an actual reader application.** Named
again rather than quietly dropped — it has been owed since 2026-08-18 and today is the
fifth time it has been named and not closed. It needs a reader client, which this runner
does not have; it is a desktop-lane job or it is an honest permanent limitation, and the
weekly review should say which.

— Growth · 2026-09-22
