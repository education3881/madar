# Growth — 2026-11-23 · the in-degree census, and the CHARTER's bilingual claim measured for the first time

**The action:** a new standing **measurement** — `agents/tools/site_graph_indegree.py` — that reads
`web/dist` and reports, per article page, how thickly it is woven into the publication's own graph. Plus
the first reading, over all **92 article pages (46 EN, 46 AR), 142 served documents.**

**It is a measurement and NOT an assertion** (no `qa_` prefix, outside the counting glob, so **no count in
`CLAUDE.md` moves**). The reason is #93's and it is specific rather than generic: **a rail is editorial
curation, and a tool that demanded "at least N inbound rails" would be an instrument commissioning
content.** Every floor available here is either already guaranteed — `qa_reachability` asserts every page
is reachable from its own front door, `qa_body_links` asserts every declared rail and source URL renders —
or belongs to the Editor.

## Why no instrument we own could already answer this

`qa_reachability` asks whether a page can be reached **at all**: a floor of one, satisfied by the listing
that must contain it. The 2026-08-17 orphan sweep asks whether a served page has any inbound path at all,
and found VALENCE with none. **Neither asks how thickly a piece is woven in** — and that is the quantity a
reader walks. *A piece reachable only from the listing obliged to contain it is reachable the way a filing
cabinet is reachable.*

So the census splits inbound edges **by the kind of page they come from**, because summing them hides the
only distinction that matters: **an edge from a listing is automatic; an edge from another piece is a
judgment somebody made.**

## The first reading

| Inbound, EN edition | Distribution |
|---|---|
| from another **piece** | `3:1 · 4:8 · 5:15 · 6:4 · 7:10 · 8:2 · 9:3 · 10:3` |
| from a **browse** listing | `2:27 · 3:11 · 4:8` — every piece sits in at least two |
| from an **editions** page | `1:46` — exactly one, uniformly |
| from the **front door** | `0:40 · 1:6` — the home page shows six of forty-six |

**Same-language piece-to-piece in-degree** (the language switcher excluded, because an EN page linking its
own AR twin is chrome and not curation): **min 1 · median 3 · max 8 · sum 180**, identically in both
editions.

## The CHARTER's own claim, made falsifiable — and it holds

The CHARTER says Arabic is *a distribution advantage, not just a translation cost*. **Nothing had ever
measured that**, and the publication could have been bilingual in its text and monolingual in its graph
without any gate noticing. It is not:

> **0 of 46 slugs disagree on distinct inbound source pieces.** The EN and AR distributions are
> identical — `{1:1, 2:8, 3:17, 4:4, 5:9, 6:1, 7:3, 8:3}` on both sides, 180 and 180. **The Arabic reader
> walks exactly the same publication the English reader does.**

## And the unit nearly produced a false headline — #111, one desk over

**The first draft of this tool counted LINKS and reported `2 of 46 slugs disagree`**, which would have been
published as *the Arabic reader walks a different publication*. It does not. The two slugs are
`2026-05-26-bahrain-bqa-public-grades` (EN 5 / AR 4) and `2026-10-23-bahrain-bqa-five-cycles` (EN 4 / AR 3),
and the difference is **multiplicity, not reachability**: the same page links the same piece twice, once as
a `related:` rail and once as a `sources[]` URL — the corpus's one **self-citation**, already carried as a
declared asymmetry in `qa_pair_frontmatter` (2026-11-09).

**A reader who can arrive from the same four pieces is not walking a thinner publication because one of
those pieces offers two doors.** The tool now reports **both units and names which one carries the claim**:
distinct source pieces for reachability, links for multiplicity. *That is #111's denominator lesson in a
third costume — the same number wearing the wrong unit — and it is the second time today one measurement
has been saved by asking what its unit is* (the other being item 48's token count restated against a grown
corpus rather than carried forward).

## The one real gap, handed over rather than repaired

**`2026-07-06-morocco-ecoles-pionnieres` is the thinnest-walked piece in the corpus: ONE inbound rail**, in
both editions, against a median of three. Eight more sit at two. Every one of them clears every gate we
own — in the sitemap, in two browse listings, on an editions page, reachable from its front door — and a
reader browsing the publication will meet it through one door only.

**This is handed to the Editor as standing-queue item 158, not fixed here.** A forward rail is written when
a later piece genuinely follows an earlier one; the standing ledger's rail step says cell 1 **names** and
cell 8 **writes**, and the 22 declined backward edges from item 72 are declined on exactly this ground.
*The Manager routes; it does not curate.* The in-flight ADEK single already names four forward edges owed,
and none of them is Morocco — which is the honest answer and the reason this is a queue row with a
measurement attached rather than a rail invented by a tool.

## Read without anyone's permission

No tracker, no third-party origin, no account, no API key, and **no estimate of a visitor number** — the
site carries no third-party tracker by design and this note invents no traffic figure. The census runs
offline against `dist` in under two seconds and will answer the same question on every run from today,
which is the CHARTER's standing preference: *bets whose outcome the operation can read without anyone
else's permission.*

— Growth, 2026-11-23
