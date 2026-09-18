# Growth — the third-party surface of the served site, counted

**2026-09-18 · measured from `web/dist`, 121 built pages · needs nobody's permission**

The CHARTER's growth loop says two things about this audit's subject and has never had a
number for either: *"Privacy posture is intact: no third-party trackers, ever"*, and
*"Arabic is a distribution advantage, not just a translation cost."* Today's quality work
put a third-party dependency in front of both sentences by accident — standing assertion
18 measures the Arabic typeface, and the Arabic typeface is not ours.

So: every `href` and `src` in every built page, grouped by origin, classified by whether
the reader's browser fetches it **automatically** or only when the reader **acts**.

## What the site loads without being asked

| Origin | References | Pages | How |
|---|---|---|---|
| `fonts.googleapis.com` | 240 | **120 of 121** | `preconnect` + the stylesheet `<link>` |
| `fonts.gstatic.com` | 120 | **120 of 121** | `preconnect` (the font files themselves) |

**That is the entire list.** Two origins, one vendor, and nothing else. No analytics, no
tag manager, no embed, no pixel, no CDN for our own assets, no comment widget, no A/B
script. The privacy claim the publication makes in every brief — *the site carries no
third-party tracker by design* — is **true as stated**, verified from the bytes rather
than from memory, for the first time.

## What the site links but does not load

| Origin | References | Pages | How |
|---|---|---|---|
| `wa.me` | 152 | 76 | `<a href>` share rail — fires only on a click |
| `x.com` | 152 | 76 | `<a href>` share rail — fires only on a click |
| ~180 further origins | 1–30 each | 1–14 each | **`sources[]` citations** |

The long tail is the publication working exactly as designed: `www.unicef.org`,
`www.moe.gov.sg`, `mbsse.gov.sl`, `archivespasec.confemen.org` and a hundred and seventy
others are the named primary registers every piece stands on. A citation is a link a
reader chooses to follow. It is not a third-party request and must never be counted as
one — conflating the two would make our own method look like a privacy problem.

## The finding, and it is not the privacy one

**The Arabic edition's typeface is fetched from a third party at read time.** Amiri —
with Cormorant Garamond, Newsreader, JetBrains Mono and Cairo — is loaded from
`fonts.googleapis.com` on 120 of 121 pages. The consequence is not primarily about
tracking. It is about **distribution**, which is Growth's subject:

1. **A reader whose network cannot reach Google gets a different Arabic edition.** The
   fallback stack is `"Greta Arabic", "Geeza Pro", Damascus, "Noto Naskh Arabic", serif`
   — three of those are Apple system faces and one is a Noto face. A reader on a Windows
   or Android device behind a network that blocks or throttles `fonts.gstatic.com` falls
   through all four to a generic serif. The Arabic edition is *written for* readers in
   MENA, and this is the one asset in it we do not control.
2. **Today's own instrument has the same blind spot, and says so.** Assertion 18 measures
   the font **this runner** resolved. It cannot measure the reader's. A shaping check that
   is green in CI proves our bytes do not break Arabic; it proves nothing about a reader
   whose font never arrived. That limit is written into the tool's own head rather than
   discovered later.
3. **Every page load tells a third party the reader's IP and User-Agent.** No tracking
   intent, no cookie, and the posture is still honest as written — but this is the one
   request the site makes on a reader's behalf that the reader did not ask for, and until
   today the operation had never counted it. A posture that has never been measured is a
   belief.

**`/madar/valence/` is the exception and the proof:** it contacts **zero** third-party
origins, because it was built as a standalone file with its own inline stylesheet. The
one page nobody designed for privacy is the only one that has it.

## Recommendation — self-host the five families. Not today.

All five are openly licensed and redistributable (Amiri and Cairo under the SIL Open Font
License; Cormorant Garamond, Newsreader and JetBrains Mono likewise). Self-hosting would:
remove **360 third-party references across 120 pages**, leave the site contacting nothing
but its own origin, remove the Arabic edition's single point of failure, and let assertion
18's font probe measure the actual served face instead of whatever the runner resolved.

**Deliberately not done in this run, and the reason is the day's own lesson.** Today's P0
was a deploy that went red on 09-17 and left the site serving stale bytes for a day. A
font migration touches the rendering of every page in both editions, and bundling it into
the push that repairs the deploy would put the repair behind the riskiest change the site
could make. **Filed as a P1 to the Web Developer** with a defined shape: subset woff2 files
under `web/public/fonts/`, `@font-face` with `font-display: swap` in `global.css`, the
`preconnect` and stylesheet `<link>` removed from `Base.astro`, and — per #35 — proved
both ways, with assertion 18's font probe as the ready-made control on the Arabic side.

## What this is not

It is not a traffic read. **The site carries no third-party tracker by design, so there
are no visitor numbers to report, and none is estimated here.** Every count above is a
count of our own bytes. The privacy-clean signals the CHARTER names — Substack opens,
return rate, country distribution, attributable inbound — switch on when Issue 01 sends,
and are read in the weekly review, not invented in a daily.

— Growth · 2026-09-18
