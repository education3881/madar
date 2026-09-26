# Growth — the privacy posture, measured instead of asserted

**Date:** 2026-09-26 · **Growth (Manager's lane) → Web Developer, Editor** · **Found by standing assertion 25 on its first run**
**Action taken today:** the claim is made precise in the brief from this run onward. **The remedy is specified and costed and is NOT applied today** — see §4 for why.

---

## 1. What the new assertion printed, and why it stopped the run

`qa_chrome_links` was written this morning to close the 08-16 chrome gap (ruling #67). It prints the
**chrome set** — every pointer carried by at least 95% of served pages — by name. Three of the ten
entries are not ours:

| Chrome target | Pages | What it is |
|---|---|---|
| `https://fonts.googleapis.com` | 120/121 | `<link rel="preconnect">` |
| `https://fonts.googleapis.com/css2?family=Cormorant+Garamond…` | 120/121 | the stylesheet request |
| `https://fonts.gstatic.com` | 120/121 | `<link rel="preconnect" crossorigin>` |

Source: `web/src/layouts/Base.astro`, lines 212–215. Five families are requested — **Cormorant
Garamond, Newsreader, JetBrains Mono, Amiri, Cairo** — across roughly fourteen weight-and-italic
combinations. `valence/index.html` is the one page outside the Astro layout and is excluded from the
count, not from the concern.

**So: every reader of every Madār page, in both languages, makes at least two requests to Google
before a glyph renders** — one for the CSS, one or more to `fonts.gstatic.com` for the font binaries,
with two `preconnect` hints opening the sockets earlier than either.

## 2. What those requests disclose

Not analytics, and this note is not going to overstate it. A font request is not a tracker: it sets no
cookie, carries no identifier we issue, and Google's stated position is that Fonts logs no
user-identifying data for ad purposes. What it does disclose, unavoidably, to a party that is not us:

- the reader's **IP address** (approximate location, and on many networks a stable household);
- the **User-Agent** (device, OS, browser version);
- the **Referer**, which on a font request is the Madār page being read — **so the third party learns
  which article, in which language**;
- and the **timing**, because the requests happen at page load.

That last one is the material fact. A reader of `‎/ar/articles/2026-09-01-sudan-cant-wait-to-learn/`
is disclosed to a third party as reading that piece, in Arabic, at that moment. This publication's
audience includes education regulators in jurisdictions where what a civil servant reads is not a
neutral fact about them.

## 3. The claim this sits against, which is the actual finding

`CLAUDE.md`, the CHARTER and **every daily brief since the cadence began** carry a version of:

> "The site carries no third-party tracker by design."

**That sentence is true and it is narrower than the impression it leaves.** No analytics script, no
pixel, no tag manager, no ad network — all correct, all worth saying, and all still true after today.
But a reader who takes "no third-party" from that sentence and opens the network tab finds two Google
origins on every page. **We would not accept that gap in a ministry's register**, and the whole of
ruling #65's first corollary is that our own record has readers and #41 does not stop applying because
the reader is us.

**This is a trust item, not a compliance item, and trust is the stated moat** — the CHARTER's growth
loop opens with *"publish slowly, verifiably — trust is the moat."* A publication whose argument is
that a claim must carry its scope cannot print an unscoped claim about itself in the one artefact the
founder reads.

**Done today, and it is the whole of today's growth action:** the brief's traffic line is rewritten to
say what is true on both limbs — no third-party **tracker**, and two third-party **font requests** per
page, named, with this audit linked. The line is now checkable by the reader against the page they are
on. That is a smaller claim and a stronger one, and it costs nothing but accuracy.

## 4. The remedy, costed — and why it is not applied in this run

**Self-host the fonts.** Fetch the five families as WOFF2, serve them from `web/public/fonts/`, replace
the two `preconnect` hints and the `css2` link with a local `@font-face` block. The third-party request
count goes to **zero**, page load gets faster (one fewer DNS lookup, one fewer TLS handshake, no
render-blocking cross-origin CSS), and nothing about the reader's experience changes.

**Why not today.** Fonts are brand-critical chrome, and two of the five families are Arabic (**Amiri**,
**Cairo**). Three standing assertions exist specifically because Arabic rendering has broken before —
`qa_arabic_shaping`, `qa_arabic_joining` and `qa_render` — and `qa_arabic_joining` measures served runs
against their own de-joined selves with a margin printed (worst served run 0.730 against a 0.9
threshold on today's build). A font swap is exactly the change those three were built to catch, and it
deserves a run whose whole subject is that swap, with the three assertions re-proved and the output
**looked at** per the 08-18 rule — the Arabic wordmark on the VALENCE card rendered with broken joins
until someone inspected the PNG. Doing it as the fourth item of a busy day is how the corpus's Arabic
gets quietly damaged.

**Filed as the Web Developer's next standing lane**, with a definition of done: zero external origins
in `qa_chrome_links`' chrome set; the three Arabic assertions green **and their margins no worse than
today's**; one Arabic article page and one Arabic card inspected by eye; the `@font-face` block carrying
`font-display: swap` and the CSS-only typographic fallback the CHARTER already requires.

## 5. What this does not claim

No traffic number is stated or estimated here, and none can be: the site carries no analytics, which is
the posture working. **This note is about what the site discloses to someone else, which is knowable
from the build, and not about who visits, which is not.** The one readable movement today is that a
sentence the operation has printed roughly eighty-five times is now scoped.

— Growth (Manager's lane) · 2026-09-26
