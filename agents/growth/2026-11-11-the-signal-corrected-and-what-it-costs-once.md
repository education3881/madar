# The change signal, corrected — and the one-time cost of correcting it

**Growth · 2026-11-11 · reads the result of the same day's quality function, by a different instrument**

Yesterday's growth read measured the only discoverability lever this publication fully owns and found it
**28% precise**: of 65 sitemap dates that moved, 18 had a changed byte behind them and 47 did not. It
raised that as standing-queue item 96 and said the fix was an output-bounded date. This morning's quality
function shipped the sitemap half. This is the audience-side read of what that changed, and it is taken
**sitemap against sitemap** — the live origin's bytes against the built artefact — rather than from the
register that was just written, because an instrument reporting on its own output is the trap that cost
three red builds two hours ago.

## What the origin is serving right now

| | |
|---|---|
| URLs in the live sitemap | **138** |
| distinct `<lastmod>` dates among them | **3** |
| 2026-11-09 | 72 URLs |
| 2026-11-10 | 65 URLs |
| 2026-10-31 | 1 URL (`/valence/`) |

Three dates for a 138-page corpus built over six months. That is the provenance resolver's whole
signature: a page's date is not its own, it is the newest thing anywhere near it.

## What the next deploy will serve

| | |
|---|---|
| dates **unchanged** | 19 |
| dates **changed** | **119** |
| of those, moved **earlier** | **119** |
| of those, moved **later** | **0** |
| distinct dates after | **17** |

**Zero dates move forward, and that number is the honesty check on the whole repair.** An output-bounded
date can only ever withdraw a claim the provenance date was already making; it can never invent one,
because a page's bytes changing is a strictly stronger condition than a file near it changing. If even one
date had moved later, the register would be asserting a change nothing observed, and the repair would be
the defect wearing a better name.

## The two instruments agree, and they were built two months apart

Of the **65** URLs the live sitemap dates to 2026-11-10, the register keeps **18** and withdraws **47**.

Those are yesterday's numbers exactly — 18 backed, 47 unbacked — derived today by a completely different
route: yesterday by `qa_served_manifest --check` comparing per-page content hashes against the origin,
today by differencing two sitemaps and asking which dated claims survive. Two instruments, two operands,
one answer. And the 18 resolve to **nine pieces in both editions**, which is precisely the nine amended
yesterday under the gender-provenance repair. The signal now names the work that was actually done.

## The cost, named rather than buried

**119 dates will move backwards in one deploy, and a crawler has no way to be told why.** Google's
documentation says it discounts a `lastmod` it judges unreliable, and a sitemap in which 86% of entries
revise their own date downwards at once is, from outside, indistinguishable from a sitemap that has
started lying in a new direction. We think the trade is right and we are writing down why rather than
assuming it:

1. **It happens once.** The correction is a single event; the precision is permanent. Every deploy after
   this one moves a date only when that page's own bytes move.
2. **The alternative was paying it every day.** An unreliable `lastmod` is not discounted on the noise —
   it is discounted on the *signal*, so yesterday's 18 genuine amendments were being spent to carry 47
   that said nothing. The cost of the old state was borne entirely by real work.
3. **It is measurable from here, without anyone's permission.** The same sitemap-against-sitemap
   comparison runs on any future deploy with no tracker, no console and no third party. The number to
   watch is the one this note introduces: **dates moved later with no byte behind them**, which should be
   **0** on every deploy from now on, and is a build-visible falsification if it is not.

## What is still wrong, and it is not small

**The JSON-LD half is untouched and is now the board's only DEFECT (item 98).** All 90 served article
pages claim a `dateModified` later than their `datePublished`, and 78 of them claim 2026-11-09. The
sitemap and the structured data now **disagree with each other on the same page** — `bo-teacher-chalk`'s
sitemap entry will say 2026-05-25 and its JSON-LD will go on saying 2026-11-09 — and a machine reading
both gets a cleaner signal from one and the old noise from the other. That is a worse-looking state than
yesterday for exactly one deploy's worth of the corpus, and it is the honest consequence of fixing the
half that can be fixed without a migration. It is tomorrow's head.

## And the reader-facing notice is still deliberately not built

Yesterday's note deferred a visible *amended on* line until the signal under it was worth publishing, on
the ground that a notice built on a 28%-precise signal publishes the noise to readers too. Half that
condition is now met and half is not: the sitemap half is output-bounded, the JSON-LD half is not, and
**the register's 91 article entries are still seeded from their own source file's last commit rather than
from an observed byte change**. A reader-facing claim about when a piece was amended must rest on an
observation, not on a seed. The flag `seeded: true` is in the register precisely so that condition is
checkable rather than remembered: when an article's entry clears it, that page has a date a reader could
be shown. **Decision recorded: no amended-on notice until item 98 closes and the piece's own entry is no
longer seeded.**
