# Growth, 2026-10-18 — 38 of the 42 countries we have written about were not on the site

**The action:** the browse hub in both languages now carries a **country directory** — every
country measured by exactly one piece, named and linked straight to that piece. Thirty-eight
names, in both editions, for **zero new pages**.

**Measured before and after, by the gating instrument rather than by hand:**
`qa_stable_order` derives its expectations from the content collection and prints them.

| | before | after |
|---|---|---|
| Countries the corpus measures | 42 | 42 |
| Countries reachable from the browse surface | **4** | **42** |
| Pages built | 134 | **134** |
| Sitemap URLs | unchanged | unchanged |
| New thin index pages | — | **0** |

## What was wrong, and it was not a bug

`facetsFor` in `web/src/lib/taxonomy.ts` gives a country an index page at **two or more**
pieces. The reason is written in the file and it is correct: *an index page listing one article
is a dead end.* The rule has been right since 2026-09-14.

It was right about the wrong corpus. This publication moves to a **new country with nearly
every piece** — 42 countries across 44 published pieces — so for a country the `>= 2` bar is not
something a country slowly clears. **It is a bar almost nothing will ever clear.** Four
countries have cleared it in five months: Egypt, Sierra Leone, Sudan, United Arab Emirates. A
reader in Bahrain, Oman, Morocco or Kenya searching for their own country had nowhere on this
site to land, **by construction**, and would have stayed that way as the corpus doubled.

That is the failure mode the 2026-08-17 orphan rule is about, one level up: those pages were
unreachable because nothing linked them; these countries were unreachable because **the rule
that decides what gets linked was written against a corpus shape we do not have.** A threshold
is an enumeration too, and it cannot report a country it has excluded.

## The fix answers the dead-end objection rather than overruling it

A one-piece country still gets **no index page**. Nothing thin is built, no route is added, the
facet sets that the hreflang clusters are derived from are untouched, and the sitemap does not
move. It gets a **direct link to the piece**, on a hub that already exists and is already
crawled. `soloCountries()` is derived from the collection like everything else here: the day a
second Bahrain piece ships, Bahrain leaves the directory and enters `facetsFor` on its own, with
nobody editing a list.

## The new list is ASSERTED, not exempted — and that is the part worth keeping

`qa_stable_order` bit on the first build, correctly: it saw 38 article links in one container
and judged them as a **dated list**, which must be newest-first. The country directory is
alphabetical by country, because a reader scanning 38 country names is looking for a country and
not for a month.

The cheap move would have been to exempt the list. That would have left **38 article links on a
served page with no order contract at all** — and the lazy alternative, sorting the directory by
date to satisfy the existing check, would have shipped the one order this list must not be in.
So the assertion learned the list instead: `expected_solo()` derives the directory's canonical
order from the same collection, and it is the **exact complement of the country facet rule**
(`n >= 2` there, `n == 1` here), so between them every country in the corpus is accounted for on
the hub exactly once.

**Proved both ways (#35), on a copy of `dist`, bite first, each injection verified to have
changed the file before the check was run on it:**

| | result |
|---|---|
| control — the real 134-page build | **CLEAN, exit 0** |
| bite 1 — two country entries transposed, nothing else | **DEFECT, exit 1**, named the position and both slugs |
| bite 2 — the whole directory removed from the EN hub | **ERROR, exit 2** — *a list that was not found cannot have been judged* |
| bite 3 — one country dropped, 38 → 37 | **DEFECT, exit 1**, named the missing country |

The first attempt at bite 1 matched `<li>` and found **zero** items, because Astro serves
`<li data-astro-cid-acyshatf>`. That is the 2026-09-14 trap exactly, and it was caught only by
the line asserting the injection had changed the file. Without that line the bite would have
reported a clean pass.

## Two of my own figures were wrong today, in the same class, and both are on the record

1. A hand-written parser said **43** of 44 pieces were published in each edition. Its
   frontmatter split was wrong on one long file per collection. All 44 are approved.
2. A hand-written parser said **34 of 38** countries were invisible. The true figures are
   **38 of 42** — it tallied the primary `country` field, while the facet rule tallies
   `countriesOf`, the primary **plus** `countries[]`. Four countries clear the bar only through
   the continental piece's list, and **Benin is in this corpus without being any piece's
   primary at all.**

Both wrong numbers came from a one-off script written beside a **proved, gating instrument that
already derives the same thing and prints it**. The second one was written the same morning as a
recon brief whose whole middle section warns about a figure summed over one population and
labelled with another. The figures in this note are `qa_stable_order`'s own output. *(#57,
earned again, by me, twice in one function.)*

## Return rate

Still not measurable and still not estimated. The site carries no third-party tracker by design,
so this action's effect on returning readers cannot be read, and nothing here should be taken as
a traffic claim. What **is** readable without anyone's permission is the number this note leads
with: **4 → 42 countries reachable**, derived from the corpus and asserted by a gate on every
build. A reachable page is a precondition for a return, not a proof of one.

## Carried forward, deliberately not done

**The Arabic directory is ordered by the ENGLISH collation key** — أستراليا، البحرين، بنغلاديش
is Australia, Bahrain, Bangladesh, which is not alphabetical in any sense an Arabic reader has.
Seen by rendering the page and looking at it, not by reading the markup. It is not a slip: both
editions derive their order from one function on purpose, and `qa_stable_order` asserts that
single derivation. Giving the Arabic edition its own collation means the two editions' orders
diverge by design, which is a decision with a cost on the checking side. **Queued, not fixed**
— the first thing this operation would get wrong is changing it quietly.
