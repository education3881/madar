# Ruling #59 — a comparator with no locale asks the machine

**Filed:** 2026-09-21 (daily run) · **Section 1, row 54** · **Family:** assertion discipline / build
determinism — the eleventh member, and #58's immediate successor.

---

## The rule

**A comparison that consults the environment is not a property of the data.** Where a build sorts,
formats or folds text, the operation supplying that behaviour is named **explicitly and completely**
— the locale, the collation, the numbering system — because every one of those has a default, and
every default is read from the machine the build happens to run on. A comparator called without its
locale does not have "the obvious" answer; it has **that runner's** answer, and the next runner is
entitled to a different one.

**Corollary 1 — the defect hides behind the data you happen to have.** Today's facet keys agree
under every locale tested, so nothing on the served page is wrong. `Türkiye` has been in this
corpus since 2026-07-07 and is kept out of the sorted set by one threshold — *a country enters the
browse surface at two pieces* — which is a fact about how much we have written, not a guarantee
about anything. A latent divergence is not a smaller defect than a live one; it is the same defect
waiting for a second piece.

**Corollary 2 — the fix is chosen so the assertion can predict it.** `localeCompare(key, 'en')` is
deterministic and would have closed the build half. It would not have closed the checking half:
`qa_stable_order.py` has to state the expected order in Python, without ICU, and on display names
with diacritics the two answers diverge exactly where this defect lives. So the comparison is
normalised instead — NFD, combining marks dropped, lower-cased — which is three operations in both
languages and identical in both. **An assertion that cannot state the expected answer cannot assert
it** (#36), and that constraint is allowed to choose the implementation.

**Corollary 3 — the same slip has a second costume: formatting.** `Intl.DateTimeFormat('ar')`
resolves a default numbering system of `latn`; `'ar-EG'` resolves `arab`. One Arabic route file
asked for `'ar'` and every Arabic browse page served `7 يوليو 2026` for seven days beside an Arabic
home serving `٢٨ يوليو ٢٠٢٦`. Not latent — **served, and visible to any Arabic reader**. Same root:
a locale tag that is not the one the page means.

## The origin

The 09-20 QA log named a forward surface: *assertion 20 asserts the order of lists; nothing asserts
the order of anything else a reader receives in sequence — the `sources[]` block, the `countries:`
list, the facet rows.* Tested first thing on 09-21, before anything new was added, per the 08-23
rule.

Two of the three could not permute: both are `.map` over a frontmatter array, and a map preserves
order by construction. Verified rather than assumed — 76 article pages, served source order against
frontmatter order, zero mismatches. **The third sorts**, and `order.ts`'s own header had singled it
out eleven hours earlier:

> The ninth, `facetsFor` in taxonomy.ts, already broke its count ties on the key. The shape was
> known here; it was simply never carried across.

It broke them on `a[0].localeCompare(b[0])`. The proof, same code and same keys, two environments:

```
LC_ALL=en_US   OLD:  … Tunisia, Türkiye, Turkmenistan, Tuvalu
LC_ALL=sv_SE   OLD:  … Tunisia, Turkmenistan, Tuvalu, Türkiye
LC_ALL=tr_TR   OLD:  … Tunisia, Turkmenistan, Tuvalu, Türkiye

LC_ALL=en_US   NEW:  … Tunisia, Türkiye, Turkmenistan, Tuvalu
LC_ALL=sv_SE   NEW:  … Tunisia, Türkiye, Turkmenistan, Tuvalu
LC_ALL=tr_TR   NEW:  … Tunisia, Türkiye, Turkmenistan, Tuvalu
```

The same read also found `facetSlug` turning `Türkiye` into **`t-rkiye`** — the character class
`[^a-z0-9]` does not know what `ü` is, so it becomes a separator. Both are now derived from one
normalisation, so a row's **position** and its **URL** cannot disagree about the same key.

## Why #58 did not cover it

#58 is about a comparator that returns **0** and delegates the decision to the input. This one
never returns 0: it returns a decisive, confident answer, and the answer is a function of an input
nobody declared. The deployed shape is the same — *the build is not a function of its sources* —
and the hidden dependency has moved one layer down, from the filesystem to the environment. #58
asked *is the order determined?*; #59 asks **determined by what?**

Stated as the failure it prevents: *every comparator can be total, every list can have a written
tiebreak, every assertion can be green, and two runners can still serve two different pages.*

## What landed with it

- `collationKey` and `byKeyAsc` in `web/src/lib/order.ts` — one home, beside `newestFirst`.
- `facetSlug` and `facetsFor` in `taxonomy.ts` rebuilt on them. **Byte-identical build output**,
  proved by hash against the pre-change tree: the repair is invisible to today's reader, which is
  the control.
- `'ar'` → `'ar-EG'` on the Arabic browse route. **Not** byte-identical — it is a repair.
- **Assertion 20 extended to the facet rows**: 38 browse pages, both languages, hub and facet
  pages, each compared against the order the content collection implies, with a facet-tie-group
  floor beside the existing date-tie floor. Proved both ways — control exit 0; three bites at exit
  1 (a tied swap on the hub, a tied swap in a facet page's *Elsewhere* list, an untied swap), each
  with the injection's effect on the file asserted by hash before the check ran (the 09-14 trap).
- **`qa_ar_language` extended to the listing date slot**, and it **bit on the real defect, not an
  injection**: 70 Western-digit dates across nine Arabic pages, before the fix; clean after.

**The check's first run corrected the check.** `expected_facets` under-counted three topics because
its frontmatter parser knew only `themes: [a, b]` and six of the 86 content files write the block
form. A derived expectation is only as good as its derivation — which is the argument *for*
deriving it from the collection rather than reading it off the page, since a parser bug fails loud
and a page-read bug passes quietly.

## The forward surface this opens

Every remaining locale-sensitive call in `web/src` now passes an explicit tag, and that was
checked, not assumed. One call passes no tag and cannot: `new Date().getFullYear()` in
`SiteFooter.astro`. **The footer year is a function of when the build runs, not of what the build
reads** — the same shape as #58 and #59 with the clock in place of the filesystem and the locale.
It is almost certainly correct behaviour for a copyright line. It is also the only input to this
publication that nothing in the repository can reproduce, and on 1 January every page's bytes will
change with no commit behind them.

---

*Family: assertion discipline / build determinism (#16, #35, #36, #37, #39, #52, #55, #56, #57,
#58, #59). Its questions, in the order earned: in which environment · against which control ·
derived from what · asserted by existence or presence · probing what that varies · on which
artefact · at which layer · from which endpoint · over which set, by name · in which order ·
**decided by what.***
