# Growth — 2026-10-27 · Which served claims live in code rather than in content?

**The action:** standing-queue item 43's enumeration, taken by the growth function because every item
in it is a sentence a reader is served in this publication's voice, and two of them are about to stop
being true. **One repair shipped in the same run**, and it is the one nobody outside this operation had
to approve.

**No traffic number appears below, and none exists.** The site carries no third-party tracker by
design; what this function can read without anyone's permission is what the site *says*, and that is
what was measured.

---

## Why the question is a growth question and not a QA one

A reader's trust in a publication is set by whether its own furniture is true. Item 43 came out of
#117's sweep by **scope rather than by result**: that sweep read `web/src/content/**` — 1,545 dated
mentions, both editions — and that is the population every figure instrument this operation owns
reads. It is not the population a reader is served. Thirty-four of our thirty-nine assertions read
`dist`, where a code-resident claim is already rendered and looks exactly like prose; the other five
read `web/src/content/**` or the repository root, where it does not appear at all. **A claim that lives
in a template is outside both.**

## The enumeration

Every literal year, date and present-tense status word in `web/src/**` outside `content/`, asked the
one question that matters — *on what date does this become false?*

| Claim | Where | Served on | Goes false |
|---|---|---|---|
| `periodEn: 'October 2026'` / `periodAr: 'أكتوبر ٢٠٢٦'` on Edition 05 | `src/lib/editions.ts` | both home pages, masthead and section meta | **2026-11-01**, in four days |
| `status: 'current'` on Edition 05 | `src/lib/editions.ts` | both home pages, via `currentEdition` | the day a sixth edition opens, **or 2026-11-01**, whichever is first |
| `periodEn`/`periodAr` on Editions 01–04 | `src/lib/editions.ts` | `/editions/`, `/ar/editions/`, the previous-edition rail | **never** — a closed edition's period is a historical fact |
| `© ${new Date().getFullYear()}` | `src/components/SiteFooter.astro` | **all 134 pages, both editions** | has no expiry date, because it has no fixed value — see below |
| Literal years in `Base.astro`, `feed.ts`, `structuredData.ts`, `global.css`, route templates | 21 / 15 / 10 / 8 / rest | nothing | they are comment dates, provenance notes and hex colours. Checked, not asserted, and listed so the next reader does not re-check them |

## The two classes, and only one of them is what item 43 expected

**Class A — a frozen literal with a known expiry date.** Edition 05's period label and status. This is
the class the item named, and it is **not repairable here**: what the next piece is an edition of is a
founder decision, open as **GitHub issue #13** since 2026-10-25. On 2026-11-01 both home pages begin
telling every reader that the current issue is a month that has ended. That is ruling #102 (*a name is
a claim about now*) on the one surface #117's sweep could not reach. **It is named at the top of
today's brief with its date, and the default stated in issue #13 applies if nobody answers.**

**Class B — a build-clock claim, and it is worse, because it cannot be caught.** The footer's
copyright year was `new Date().getFullYear()`, served on all 134 pages since 2026-05-25. It has the one
property that defeats everything we own: **it agrees with itself.** `qa_live_drift`, the verify job's
byte-compare, `qa_date_identity`, `qa_served_manifest` — every instrument here puts one byte beside
another byte, and two builds run in the same calendar year produce identical bytes no matter what the
repository contains. On **1 January 2027**, every page served from a December-2026 build quietly begins
carrying a wrong year, nothing goes red, and nothing can, because nothing changed.

*A claim that cannot be wrong in a way anything can detect is not a strong claim. It is an unfalsifiable
one, and this publication's whole method is the opposite of that.*

## The repair, and why its control is that nothing changed

`SiteFooter.astro` now takes its year from `createLastmodResolver()` — the sitemap's own git-derived
resolver, the same one `articleJsonLd` was wired to yesterday — through a memoised
`src/lib/copyrightYear.mjs`, because the component renders on all 134 pages and the resolver walks git
history.

Measured:

* `createLastmodResolver()('/')` → `2026-10-27T10:24:10.000Z`; `copyrightYear()` → **2026**; `new
  Date().getFullYear()` → **2026**.
* Built before and after: the footer markup of `dist/index.html` is **byte-identical**.
* Build exit 0, all twelve build-job gates and all twenty-four postbuild gates green.

**Byte-identical is the right control for this repair and not a sign that nothing happened.** The value
is unchanged and its *provenance* is not: it was a function of the machine's clock and is now a
function of the tree. Two properties follow, and the second is the one that matters for growth —
**deterministic** (the same tree yields the same byte on any day, which is what the verify job's
byte-compare assumes about every other byte on the page) and **falsifiable** (the year can now disagree
with the repository, so an instrument can be pointed at it; a build-clock year could not).

## What is handed on

* **Item 43 closes**, and it closes with its scope widened by one class it did not name: the
  enumeration found not only *frozen literals with an expiry date* but *claims with no fixed value at
  all*, and the second class is the one no comparison can see.
* **Raised: the Class A repair is blocked on issue #13**, and it is a DEFECT from 2026-11-01 rather
  than today — the first row this board has ever carried with a date on which it changes bucket by
  itself.
* **Raised: nothing gates `copyrightYear`.** 134 of 134 pages carry the derived year and 0 disagree
  with the sitemap's own date for `/` — a measurement, not an assertion, and the same shape as item 44
  raised yesterday about `dateModified`. The two should be closed by one instrument: *every date a
  template emits is derived from the tree, and none from the clock.*
