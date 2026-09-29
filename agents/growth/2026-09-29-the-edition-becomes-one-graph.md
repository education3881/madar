# Growth — the edition becomes one graph: six pieces, six rails, one continent's argument

**Date:** 2026-09-29 · **Owner:** Growth, with the Editor writing the claims
**Type:** structural improvement to the site graph. Read without anyone else's permission.

---

## The finding this closes

From the 2026-09-27 weekly review's rail-graph audit, and it is the one finding in that review
that no assertion could have produced:

> Rows 1–4 are mutually bound and flip atomically. **Rows 5 and 6 are bound to nothing.** Every
> target they name is already approved and live, so no rail carries a dead end, `qa_body_links`
> passes, and **it passes correctly** — there is nothing wrong to find. The gap is the absence of
> an edge, and a check that asserts every rail resolves cannot see a rail that was never written.

The consequence, stated plainly at the time: the edition's claim is that six pieces are one
continent's story, and on flip day **two of the six would point at none of the other five, and none
of the other five would point at them.**

That is the 2026-08-17 orphan sweep one graph over — *a link sweep checks pages that are pointed
at; it can never find a page nothing points to* — except the orphan here is not a page, it is an
argument.

## What was added, and the argument each edge carries

Six directed edges, **three pairs**, in **both languages** (#42), appended so
`qa_stable_order` reads them in frontmatter sequence. The ledger asked for "the Editor's call on
which pairings carry an argument rather than a mechanical six-way mesh," and three is the answer:
every pairing below is a claim that two pieces make each other sharper, and the ones I did not
write are the ones where I could not say that with a straight face.

**1. Rwanda ↔ Sierra Leone (row 6 ↔ row 2).** The strongest edge in the set, and the reason it is
first. Both pieces are about a state that measured its own teachers and published the number that
did not flatter it: Sierra Leone paid what its measurement said, and Rwanda counted the teachers it
had not trained — twice, and printed the second count beside the first. They are the same virtue
observed in two currencies, and each makes the other look less like an accident. Row 6 already
named the *older* Sierra Leone piece (TSC teacher matching, June); this adds the edition's own.

**2. Rwanda ↔ the continental ruler (row 6 ↔ row 4).** Row 4 asks what a system produces given its
means and refuses to average the rulers that answer. Row 6 is a system that published its own
means — the workforce, the untrained share, the school year beside each — in the annual it prints
anyway. The ruler piece argues that a claim without its register's scope is an opinion with decimal
places; Rwanda is what it looks like when a ministry supplies the scope itself.

**3. Egypt ↔ the continental ruler (row 5 ↔ row 4).** Egypt published the tracks, the subject lists,
the exam format, the faculty map, the admissions arithmetic and an international agreement for a
certificate — and has published nowhere we can find how many students are in it. Row 4's whole
subject is the boundary of what a published number can be made to support. Read together they are
the two halves of one question: what a state chooses to measure, and what it chooses to announce
instead.

**Deliberately not written:** Egypt ↔ Rwanda, Egypt ↔ Sierra Leone, Egypt ↔ Zambia or Sudan, and
Rwanda ↔ Zambia or Sudan. Each is defensible in a sentence and none is a claim I would put my name
to. A mesh where every piece points at every other piece tells a reader nothing about which two
belong together, which is the entire function of the rail.

## The result, measured

| Row | Rail entries | **Held siblings** |
|---|---|---|
| 1 Zambia | 4 | 1 |
| 2 Sierra Leone | 5 | **3** (was 2) |
| 3 Sudan | 4 | 3 |
| 4 slot 3 | 5 | **5** (was 3) |
| **5 Egypt** | 4 | **1** (was **none**) |
| **6 Rwanda** | 5 | **2** (was **none**) |

**Every row in the edition now has at least one inbound and one outbound edge inside the wave.**
The six pieces are a connected graph rather than four plus two. EN and AR rails verified identical,
row by row, and every target verified to exist in both collections.

## Why this is the growth action and not merely editorial housekeeping

Three reasons, in the order a reader experiences them:

1. **It is the only inbound path a held piece can be given before it exists.** The wave has no
   external inbound links, no social posts, no newsletter — nothing posts before the gate and a
   green `verify`. On flip day the *only* thing carrying a reader from one Africa piece to the next
   is this graph. Rows 5 and 6 would have been served with no way in from the edition they belong
   to and no way out into it.
2. **It is a discoverability surface we own outright.** No third-party tracker, no platform, no
   algorithm, no permission. The rails are rendered into the served HTML of every article page and
   they are what a crawler and a serious reader both follow. The charter's instruction — *prefer
   bets whose outcome the operation can read without anyone else's permission* — describes this
   exactly: the outcome is a property of `dist`, and two standing assertions read it.
3. **It removes work from the flip commit.** The ledger records these rails as *owed in the flip
   commit*. That is the most expensive place to do anything. Adding them twelve days early — the
   same choice the 09-20 run made with the three reciprocal edges into row 4 — means the flip
   commit moves flags and nothing else. Nothing time-sensitive is staged against a same-day deploy
   (the 08-30 rule); this is the opposite, and the safe direction.

## What is honestly not claimed

**No traffic figure, no reach estimate, no projection.** The site carries no third-party tracker by
design, so nobody here knows how many readers follow a rail, and this note does not pretend
otherwise. What is verifiable is structural and it is stated as such: **two pieces that would have
been served unconnected to their own edition are now connected to it, in both languages, and two
assertions will fail the build if that stops being true.**

The measurable thing to watch after the flip is the one signal we can read without permission:
whether the Africa pieces appear in each other's rails on the **live origin**, which
`qa_live_drift` and `qa_body_links` both cover. Return rate and country distribution remain
unavailable until Issue 01 sends, and are not estimated here.

## Carried forward

- **The weekly review should ask the rail question of the corpus, not just the wave.** This finding
  was made by reading all six rails in one sitting. The other 38 published pieces have never been
  read as a graph — nothing knows whether an older piece is bound to nothing. *A check that asserts
  every rail resolves cannot see a rail that was never written*, and that is as true of 2026-05 as
  of Edition 05. Named as a candidate instrument: **inbound-edge count per piece, from the content
  collection**, which is cheap and which no existing assertion computes.
- Bet item 2 from the 09-28 week (a demonstrated `qa_sources_alive` ceiling against the full held
  set) is **still owed** and is named again rather than quietly dropped. It matters for flip day:
  the ledger makes that sweep the last step before the flip commit.

— Growth, with the Editor · 2026-09-29
