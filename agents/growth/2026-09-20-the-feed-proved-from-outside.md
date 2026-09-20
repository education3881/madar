# Growth — the feed, fetched from outside our own origin

**2026-09-20 · weekly review · Growth, with the Web Developer**
**Closes:** the second of the three debts the 2026-08-18 rule named and the 09-20 daily
re-stated — *do the links resolve from outside our origin?*

---

## Why this was owed

The 08-18 rule found that every share card had been declared to social consumers as an SVG
for 83 days — a real file, at a real URL, in a format no consumer renders. It closed by
naming the next surface: **the feeds**, of which nothing had ever been verified beyond
well-formedness. The 09-20 daily took the first of the three questions and found that all
**76 enclosures declared `length="0"`** for cards that are 1–20 KB of valid PNG. Its own
note then named what it had *not* done:

> Neither is expensive. Both need a client we do not currently own.

That sentence was true of the desktop cadence and is **no longer true of this one.** The
cloud runner *is* a client outside our origin: it reaches `education3881.github.io` over
the public internet, with no privileged path, exactly as a reader's feed application would.
The instrument was already in the room.

## The reading, taken today

Every `<link>` and every `<enclosure url="…">` in both served feeds, fetched by HEAD from
this runner's egress against the **live origin** — not against `dist`, and not against the
build this review produced.

| Probe | Result |
|---|---|
| Item + channel links, both feeds | **78 / 78 → HTTP 200, `text/html`** |
| Enclosures, both feeds | **76 / 76 → HTTP 200, `image/png`** |
| Declared `length` vs the origin's `Content-Length` | **76 / 76 exact, 0 mismatches** |
| Failures of any kind | **0** |

The third row is the one worth keeping. Assertion 21 landed this morning and checks each
declared `length` against **the file in `dist`**. This check compares the same declaration
against **what the origin actually serves**, which is ruling #16 applied one layer out: a
build that computes the number correctly and an origin that serves a different file would
pass assertion 21 and fail here. Today they agree, byte for byte, on all 76.

## What this does *not* say

- **No traffic figure.** The site carries no third-party tracker by design. This is a
  statement about what the bytes permit, not about anybody fetching them.
- **It does not close the Arabic-direction question.** Whether a reader honours
  `<div dir="rtl" lang="ar">` inside an escaped description is a property of *that reader's*
  rendering, and a HEAD request cannot see it. That is the remaining debt and it is this
  week's bet.
- **It is a reading, not yet an instrument.** A review that runs a sweep once has a habit,
  not a gate (the 09-13 rule). Making today's four numbers reproducible by something
  scheduled is part of the same bet.

## Carried

The one genuinely unownable part of the surface stays named rather than quietly dropped:
a feed item's appearance inside somebody else's application is theirs, and the honest
substitute is to assert the **properties** our markup promises — direction, language,
encoding, enclosure type and size — in a rendering engine we do run, and to stop there
rather than claim what a reader sees.

— Growth · 2026-09-20
