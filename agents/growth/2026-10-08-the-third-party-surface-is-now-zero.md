# Growth — the third-party surface is now zero, and the Arabic edition has been measured on the reader's side of the network

**2026-10-08 · measured from `web/dist`, 121 built pages, and from headless Chrome with every
external host blackholed · needs nobody's permission**

The 2026-09-18 audit counted this publication's third-party surface for the first time and found
**two origins, 360 references, 120 of 121 pages** — `fonts.googleapis.com` and
`fonts.gstatic.com`, for the five typefaces. It recommended self-hosting and deliberately did not
do it, filing a P1 with a defined shape. **That P1 reached the head of the standing queue today at
20 days and three displacements, and it is closed.**

## What the audit's own table reads now

| Origin | References, 2026-09-18 | References, today |
|---|---|---|
| `fonts.googleapis.com` | 240 | **0** |
| `fonts.gstatic.com` | 120 | **0** |
| **anything the browser fetches without being asked** | **360** | **0** |

Asserted rather than observed, from today on: **`qa_third_party_origins`, standing assertion 31,
28 of 31 gating.** 573 automatic references across 121 pages, every one resolving to our own origin
or to a relative path. Put a vendor `<link>` back and the build reds.

## What the audit said could not be measured, and now can

The audit's finding was *not* primarily the privacy one. It was a **distribution** finding, and
this is Growth's subject:

> "A reader whose network cannot reach Google gets a different Arabic edition. […] Assertion 18
> measures the font **this runner** resolved. It cannot measure the reader's."

Self-hosting makes those the same file. So the measurement the audit could not take was taken
today: a served Arabic article loaded in headless Chrome with **every host blackholed at the
resolver except our own loopback origin** — which *is* the reader the audit described.

| | bundle served (today) | bundle unreachable (every reader behind a blocked vendor, 2026-05-25 → 2026-10-08) |
|---|---|---|
| font faces loaded | **15** — Amiri 3, Cairo 4, Cormorant Garamond 2, JetBrains Mono 4, Newsreader 2 | **0** |
| Amiri joined/de-joined ratio | **0.428** | 0.571 |
| Cairo joined/de-joined ratio | **0.612** | 0.571 |
| `document.fonts.check('16px Amiri')` | true | **true** |

**The right-hand column is not a hypothetical.** It is the state of the Arabic edition for any
reader whose network throttles or blocks `fonts.gstatic.com`, on every page, for 136 days — falling
through a four-face fallback stack (`"Greta Arabic"`, `"Geeza Pro"`, Damascus, `"Noto Naskh
Arabic"`) that is three Apple system faces and one Noto face, to a generic serif on any Windows or
Android device. The Arabic edition is *written for* readers in MENA, and until today its typeface
was the one asset in it we did not control.

**Two Arabic families collapsing to one identical 0.571 is the signature**, and it is worth
keeping as a technique: where two things that should differ report the same number, something
underneath them is substituting. The last row is why that technique was needed — the browser's own
`check()` says yes in both columns, which became **ruling #92**.

## What this costs, stated rather than glossed

**1.4 MB in the repository**, 34 woff2 files. **Nothing extra on the wire for a reader**, because
the `unicode-range` subsetting is preserved exactly: an English page still fetches the Latin cuts
only, an Arabic page the Arabic cuts. That preservation is the whole reason the bundle is a
*mirror* of the vendor's response rather than five hand-written `@font-face` rules — five rules
would have been shorter and would have shipped the entire Arabic face to every English reader.

**And one request fewer, plus two handshakes.** The three vendor `<link>`s (two `preconnect`, one
stylesheet) become one same-origin `<link>`, and the DNS lookup and TLS negotiation against a
second origin are gone. This is a performance improvement as well as a privacy one, and it is
asserted as neither — only the origin count is gated.

## What this is not

**It is not a traffic read, and no visitor number is estimated here.** The site carries no
third-party tracker by design, so there are none to report; every count above is a count of our
own bytes and of our own rendering. The CHARTER's privacy-clean signals — Substack opens, return
rate, country distribution, attributable inbound — switch on when Issue 01 sends and are read in
the weekly review.

**It does not make the privacy claim newly true.** The 09-18 audit established that the claim *the
site carries no third-party tracker by design* was **true as stated** — there was never a tracker.
What was true as stated and uncomfortable as read was that the site made one request on a reader's
behalf that the reader had not asked for. It no longer makes any. **The publication now contacts
nothing but itself, and that is a gate rather than a sentence.**

`/madar/valence/` is no longer the exception that proves the point. It has company.

— Growth · 2026-10-08
