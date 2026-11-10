# Growth — 2026-11-10 · the change signal is 28% precise, and it is the only discoverability lever this publication fully owns

**Function:** Growth. **Type:** metrics read (CHARTER's list) + the instrument repair that makes the
read trustworthy. **Permission needed from anybody:** none, which is why it was chosen.

---

## The bet's shape, and why this one

This publication has **no third-party tracker by design**, so there is no return rate to lead with and
no visitor number to report — and none is estimated here. What that leaves is the class of growth signal
the operation can read **without anyone else's permission**, which the CHARTER explicitly prefers. There
is exactly one such signal that reaches a search engine on every deploy and that we author end to end:
**the `<lastmod>` we put in our own sitemap, and the `dateModified` we put in our own JSON-LD.**

Nobody had ever measured whether it is true.

## The read

Measured by `qa_served_manifest --check`, which fetches the per-URL fingerprint of the bytes **the origin
is currently serving** and joins it against this build's own manifest and sitemap dates. This is a
comparison of served bytes against served bytes; no provenance is trusted on either side.

| | |
|---|---|
| pages compared against the live origin | **138** |
| rendered content changed **and** the date moved — a correct signal | **18** |
| date moved and the rendered bytes are **byte-identical** | **47** |
| rendered content changed and the date did **not** move | **0** |
| **precision of today's change signal** | **18 of 65 = 28%** |

**Of the 65 pages whose date moves on this deploy, 47 have nothing behind them.** The 18 that are real
are exactly the nine pieces whose annotations this run amended, in both editions — so the signal is not
broken, it is swamped.

The JSON-LD half is worse because it has no complement to hide in: **100% of the 90 article pages claim
a `dateModified` later than their `datePublished`**, and **78 of them claim `2026-11-09`** — the day the
*site chrome* changed when the Bahrain single shipped. `2026-05-25-bo-teacher-chalk` tells every machine
that reads it that it was modified on 2026-11-09. Its own bytes have not changed since May.

## Why, and the cause is a resolver doing exactly what it says

`web/src/lib/sitemapLastmod.mjs` resolves a page's date as **max(chrome, newest file under
`web/src/content/`)**. That is provenance-derived and it is honest about being so: any template,
registry or content change moves every page that depends on it. The 2026-09-06 review already named the
consequence in writing — *the resolver derives change from source provenance, while the truth of "did
this page change" lives in the served bytes* — and recorded it as **a design question for the Web
Developer, not a defect.**

**That was the right call then and it is the wrong call now, for one reason: the question has acquired a
count.** On 2026-09-06 the honest instrument did not exist. `qa_served_manifest` was built 2026-10-06 and
the origin has been carrying a baseline manifest ever since, so the number is no longer a hypothesis:
**47 served sitemap entries currently make a claim with nothing behind them, on every deploy.** Under
#116's own boundary — *N > 0 artefacts, currently served, that are wrong* — that is a **DEFECT** and it
is raised as one (item 96), where it will take tomorrow's head.

## Why this is a growth item and not housekeeping

The downside is not cosmetic and it does not require inventing a traffic figure to state. A crawler that
finds a `lastmod` unreliable **stops believing it** — the resolver's own header says so, which is how the
operation knew to write the 09-06 rule. The cost is therefore paid on the **real** changes: the 18 pages
amended today are indistinguishable, from outside, from the 47 that were not. A publication whose entire
moat is *every piece stands on named primary sources read in served text* is sending a change signal
that is 72% noise, and the thing it most needs crawled promptly — an amended citation — is the thing
hiding inside the noise.

**The structural statement needs nobody's permission and is the one made here:** today 9 pieces × 2
editions had their sourcing amended, and from outside the origin that is 18 true signals inside 65.

## And the reader side of the same asymmetry, named and not solved

The machine is told the piece changed. **The reader is told nothing.** No article page carries a visible
amended-on line in either edition; `grep` over the built HTML returns no `Updated`, `Corrected`,
`Revised` or `آخر تحديث` anywhere in the chrome. A reader who read the Ghana piece in May and returns
today reads **amended annotations with no signal that they were amended** — in a publication that asks
to be audited.

Deliberately **not** fixed in this run, and the reason is this operation's own 2026-06-07 rule: anything
that must equal *the current set of amended pieces* is build-generated or it is a drift defect waiting to
happen, and the only honest operand for it is the output-bounded date that item 96 is about. **Building a
visible notice on top of a 28%-precise signal would publish the noise to readers as well as to
crawlers.** Order matters: item 96 first, the reader-facing notice after it, and it is written down here
so the sequence is a decision rather than an omission.

## The instrument repair this read required first

The first run of this measurement reported **6 pages as SILENT CONTENT CHANGE** — the one direction
`qa_served_manifest` calls its assertion, and the one no other instrument of ours can see. **All six were
false**, and `lastmod_tree_guard.py` — the precondition built on 2026-10-15 to refuse exactly this class
of comparison — allowed it, because it asks *is the working tree clean NOW* when the question is *does
`dist` contain what the tree now contains*. This run had edited, built, committed, and then compared: the
tree was spotless and every date in that `dist` had been resolved against a HEAD one commit behind.

**Limb 2 added today:** HEAD's committer timestamp against `dist`'s newest file mtime — both already on
disk in both callers, no new artefact, no served byte touched. Proved per #35 with the two states this
run happened to have: **one bite red** (clean tree, `dist` stamped before the HEAD commit → `REFUSED(4)`
with the lag printed) and **three controls** (the real post-commit build → silent; the same copy stamped
after HEAD → silent; no `dist` at all → refused for the cannot-establish reason, not assumed clean).
Rebuilding from the identical committed tree returns **CLEAN · 0 silent content changes**, which is the
measurement reported above.

*A precondition that measures the wrong operand reads exactly like a precondition that passed* — and the
report it green-lights is a manufactured defect indistinguishable from a real one.

## What to read next week

Item 96's repair, if it lands, is measurable the same way and by the same instrument: **precision should
go from 18 of 65 toward 18 of 18**, read off the origin, needing nobody's cooperation. That is the
outcome the operation owns, which is the test the CHARTER sets for a bet.

— Growth · 2026-11-10
