# Ruling #58 — a comparator that returns zero is a decision delegated

**Filed:** 2026-09-20 · **Status:** binding · **Section 1, row 53**
**Earned on:** the same commit, built twice on two runners, serving **five sitemap pages
and both feeds** with the same pieces in a different order — and on the fact that nothing
this operation owns could see it, because every check we have ever written asks *what is
on the page*, never *in what order*.

---

## The rule

**Sorting is not a filter. A comparator that can return 0 has not ordered the tied
elements — it has handed the decision to whoever supplied the input, silently. Where the
sort key is not unique, the tiebreak is part of the contract and is written down; a sort
whose output depends on enumeration order is a build that is not a function of its
sources.**

Two corollaries, both earned within the hour:

1. **A stable sort does not make a partial order total.** Stability guarantees only that
   equals keep their *incoming* relative order. That reads like determinism and is the
   opposite: it means the answer is exactly as determined as the input was, and the input
   here was `readdir`.
2. **Order is a property of a LIST, not of a page or of a corpus.** Two adjacent lists may
   each be correctly ordered and their concatenation may not be. Any instrument that
   judges order must be scoped to the list whose contract it is checking.

Stated as the failure it prevents: *every piece in the publication can be present,
correct, linked, dated, cited and served, and the publication can still tell two readers
two different stories about what it published first.*

---

## How it was found

Not by looking for it. The 09-19 deploy went **red** on the `verify` job's feed-cache step
— a conditional GET returning 200 where 304 was required. Diagnosing that meant asking
the obvious question: *is the feed we serve the feed we built?* Today's build was
byte-compared against the live origin at commit `8208eb7`, which is the commit today's
build was made from.

**Five of 120 sitemap URLs differed, and so did both feeds** — identical byte lengths,
identical piece sets, different order.

The cause is one line, repeated eight times across six files:

```js
.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf())
```

`Array.prototype.sort` is stable, so two pieces dated the same day were not randomised;
their order was inherited from whatever sequence `getCollection()` returned, which is
filesystem enumeration order. **24 of the 38 approved English pieces sit in a tie group —
16 share 2026-07-07 alone** — so most of the corpus had no defined position, and had not
had one since the first publish on 2026-05-25.

**The ninth sort site already had it right.** `facetsFor` in `taxonomy.ts` breaks its
count ties on the key: `b[1] - a[1] || a[0].localeCompare(a[0])`. The shape was known in
this codebase, in a file the other eight import from. It was never carried across, and
nothing asked.

---

## Why nothing caught it, which is the part worth keeping

Nine assertions read these exact pages on every build. Every one of them is a claim about
**membership**: every page reachable, every URL in exactly one hreflang cluster, every
`related:` slug rendered, every sitemap entry served, every count against its named
population — **#57, filed yesterday, asserts the set relations element for element by
name.** A set has no order. Not one of these checks could have failed on this, and the
census that compares eleven instruments' populations by name would have been *right* every
time.

This is the enumeration family's seventh member, and the first where the missing
enumeration is not a set at all:

> *a green check is scoped to what it enumerates* — the flag-sweep inversion (08-09), the
> chrome 404 (08-16), the orphan sweep (08-17), the consumer-format rule (08-18), the
> brief's own container (08-23), the held file's date (09-06), and now **the sequence**.

#57 said two sets of the same size are not the same set. This says **the same set, twice,
is not the same page.**

---

## The instrument, and the trap it had to avoid

Standing assertion 20, `qa_stable_order.py`, wired into `postbuild` in the same commit
that proves it (09-13 rule; `postbuild` and not the workflow, per 09-14 clause 4).

**The obvious instrument is the wrong one.** "Build it twice and compare" was tried in
principle and rejected in fact: two builds on the same runner share a filesystem order, so
the control passes for a reason that has nothing to do with the property. That was
confirmed today rather than assumed — two consecutive builds on this runner are
**byte-identical**, on a tree whose comparator had just been proved defective. An
experiment whose negative result is indistinguishable from a healthy one is the 09-14
trap, and it would have certified this defect as fixed.

So the assertion checks the stronger property from a *single* build: **the served order IS
the canonical order**, with the expectation derived from frontmatter (date + slug, #36)
and never read back off the page being judged (the 09-14 masking trap).

**Its first draft false-failed on the real build**, and the reason is corollary 2 above:
it compared each page's whole link sequence, and the editions page renders one block per
edition, where Edition 04's block ends on `2026-07-07-us-naep-honesty-gap` and Edition
03's begins on `2026-07-07-chad-sudanese-refugee-schooling`. A tie run spans that boundary
legitimately. **Its second draft judged the `related:` rails by the date order too** — 76
defects on 76 correct pages, the right check applied to the wrong list. A rail's order is
editorial, declared in frontmatter, and it now has its own contract rather than an
exemption: every list on the site is judged against the order **its own source** declares,
and a list matching neither contract is a defect and not a skip.

---

## Proved eight ways, per #35, every injection asserted to have changed the artefact first

| | injection | result |
|---|---|---|
| control | none — the real 121-page build | **CLEAN**; 45 dated lists, 2 feeds, 76 rails, **42 tie groups actually exercised** |
| **bite A** | **the tiebreak removed — the real historical defect, rebuilt** | **5 defects**, and `npm run build` **exits 1**. The footprint matches the five surfaces measured against the live origin |
| bite B | a tiebreak that is total but wrong (descending) | **24 defects**; build exits 1 |
| bite C | two same-date pieces swapped in a built page | 1 defect, naming page and position |
| bite D | two same-date items swapped in `rss.xml` | 1 defect, naming the feed and position |
| bite E | a related rail reordered | 1 defect, against the frontmatter sequence |
| bite F | a rail item deleted | 1 defect, naming what is served against what is declared |
| floors | empty dist · no feed · no content collection · **a corpus with no tie anywhere** | **exit 2** on each — a check that cannot bite has failed, not passed (08-16) |

**The tie floor had to be proved twice.** Its first fixture exited 2 for the *rails* floor
instead — the right exit code for the wrong reason, which is a bite that fires by
accident. Rebuilt with rails present, the tie floor fires on its own terms. That is the
09-14 discipline turned on a floor rather than on a bite, and the **third consecutive run**
in which asserting the injection took effect has paid.

---

## What this does not fix, said plainly

GitHub Pages derives its `ETag` from file mtime and size, and every deploy rewrites every
file. **Both feeds will get a new `ETag` and `Last-Modified` on every deploy whether or not
a single byte of their content changed**, and that is the host's behaviour, not ours to
repair. What was ours is that the bytes behind those validators *also* churned, for no
editorial reason. The honest instrument for the remaining half is the output-bounded
manifest named on 09-06, 09-18 and 09-19 and still owed.

---

## Where it binds

- **Web Developer.** One exported comparator, `web/src/lib/order.ts`, used at all eight
  date sort sites. A new list surface imports it; it does not write its own. A sort key
  that is not unique gets its tiebreak written down at the point of sorting.
- **Editor / Verifier.** A `related:` rail's order is now asserted against frontmatter, in
  both languages. Reordering a rail in the markup is a defect; reordering it in the
  frontmatter is an edit.
- **Everyone.** When an instrument reports a set, ask what else the reader receives besides
  membership. Order, adjacency and position are all served, and none of them is a set.
