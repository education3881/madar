# Ruling #152 — a two-state flag cannot name the state the work is in

**Filed 2026-11-20** by the content function, from the cell-7 placement question on
`2026-11-12-england-ofsted-exempt-cohort`.
**Family:** enumeration (*a green check is scoped to what it enumerates*), which keeps no running member
count, so this filing moves **four** homes and not five (10-04 second amendment, limb 1).

---

## The rule

**A PIPELINE'S INSTRUMENTS ARE SCOPED TO THE STATES ITS FLAG CAN HOLD, AND A FLAG WITH TWO VALUES CANNOT
NAME A THIRD. Where the work spends most of its life in that third state, every instrument built on the
flag is silent about the thing it was built to govern — and silent in the direction of a green light,
because an item in no enumerated set fails no limb.**

`approved: true | false` has governed publication since ruling #18. Two values, and the whole apparatus
reads them: `heldAssets.mjs` withholds a held piece's assets from `dist`; `qa_held_assets` asserts that no
held slug contributes bytes and that every approved slug's assets are served; `sitemapLastmod.mjs`
classifies held files out of every date; `qa_pair_frontmatter` reads source files *"held pieces
included"*; `qa_date_identity` builds its expectations from approved pieces only. Six instruments, one
field, two states.

**The eight-cell gate has eight.** A piece that has cleared its brief, its draft, the Editor's five tests,
its Arabic composition, the Arabic gate and the Verifier's verdict — six of eight — has no file in
`web/src/content/` at all. It is not approved. **It is not held either. It is absent**, and absent is not
a value the field has.

## What that cost, measured this morning

Cell 7 of the England piece is the hero still and the og card. The obvious place for them is
`web/public/stills/` and `web/public/og/`, which is where every shipped piece's assets live and where the
publish gate looks for them. Put them there today and they are copied into `dist` whole, because
`heldAssets.mjs` builds its withhold list from **held slugs read out of the content collection** and this
slug is in no collection. So:

```
/madar/og/2026-11-12-england-ofsted-exempt-cohort.png      -> 200
/madar/articles/2026-11-12-england-ofsted-exempt-cohort/   -> 404
```

That is the **2026-09-09 defect verbatim** — a derivable promise (#36) for an article that does not
exist, with the still's own `<title>` serving the unshipped piece's subject in readable text at a
guessable URL — and it is the defect `heldAssets.mjs` was written to close.

**Proved rather than argued.** A card for this slug was copied into a scratch `dist` and
`qa_held_assets` was run against it. It **exited 0 and printed CLEAN**:

```
qa_held_assets: 0 held slug(s), 45 approved slug(s), 90 control asset(s) checked
CLEAN — no held piece contributes bytes; every approved asset is served
```

Both limbs are correct and both are blind. Limb 1 enumerates **held** slugs — there are none. Limb 3
enumerates **approved** slugs — this is not one. *The file sat in the middle of the sweep's own output
directory while the sweep reported the population it had been given.*

## Why this is not just a missing check

It is **#57 and #70 pointed at a LIFECYCLE instead of at a count**. The 09-27 amendment's general form
was *a bucket set is an enumeration too, and it cannot report a distinction it cannot hold*; #116 said the
same of a queue's three buckets. Here the bucket set is a **boolean**, and the distinction it cannot hold
is **where the work actually is**: one of the eight cells is `approved: true`, one is the hold, and the
other six have no representation in any field any instrument reads. The operation's own ledger has carried
all eight cells since 2026-11-08 — and the ledger is **prose**, which is why the standing rule in
`CLAUDE.md` exists to stop it going stale and why #144 had to be filed when it did.

**The sharper half, and it is the part that generalises past assets.** A two-state field is not merely
coarse; it is *coarse in a direction*. Both of its values are enumerated by somebody, so anything the
field can name is governed. What it cannot name is governed by nothing, and an instrument that enumerates
sets reports *nothing found* in exactly the same words whether the set is clean or the member was never in
it. **A gap in a classification does not announce itself as a gap. It announces itself as a pass.**

## Binding

1. **An article-bound asset for a piece that has no file in `web/src/content/` is staged OUTSIDE
   `web/public/`** — `design-assets/stills/` and `design-assets/og/` — and cell 8 copies it across in the
   same commit as the flip. The 2026-06-14 rule (*an article's assets ship in the same commit as its
   text*) is satisfied: the asset is on disk from the moment it is drawn, and it reaches the served
   perimeter at the moment the article does.
2. **Any instrument whose subject is governed by `approved` states which of the THREE states it
   enumerates** — approved, held, absent — in its own CLEAN line, so a reader sees *45 approved, 0 held,
   1 absent and not read* rather than inferring a population from a green. This is #123's limb 1 (*an
   assertion with a fixed probe set declares that fact*) applied to a field rather than to a page list.
3. **The absent set is DERIVED, never listed.** It is the in-flight rows of `_STANDING_LEDGER.md` by slug,
   which is the only register that holds the eight cells — and a hand-kept list of pieces mid-gate is the
   2026-06-07 drift defect by construction.
4. **Where a flag stands in for a state machine, the number of values it can hold is compared against the
   number of states before any instrument is built on it**, and the difference is written down. Two
   against eight is not a defect in the flag — the flag is a publication switch and should stay one — it
   is a statement about how much of the pipeline the flag can be asked to govern.

**Not gated today, and the reason is #93's floor.** The honest assertion is *no asset in `dist` names a
slug that no approved piece declares*, which is limb 1 of `qa_held_assets` with its enumeration inverted
from a list to a complement — and inverting it is a change to what reds the deploy, which is the Web
Developer's and the Assertions Engineer's call under the 09-27 split, not the content function's. Handed
over as standing-queue item **140**, with this ruling as its evidence and the scratch-`dist` reading as
its bite.

---

## Cross-references

Extends **#18** (`approved: false` is the hold) by naming what the field cannot say. The enumeration
family's defect shape, from the flag-sweep inversion (08-09) onward: *a green check is scoped to what it
enumerates*. **#57 / #70 / #116** are the same error on counts, pointers and queue buckets; this one is on
a lifecycle. **#36** (a promise is derived, not declared) is what the served card would have been. Sits
beside **#123**, whose limb 1 asks every instrument to declare its own population, and beside
**#144**, because the ledger that holds all eight cells is prose and a maintenance rule is all that keeps
it true.
