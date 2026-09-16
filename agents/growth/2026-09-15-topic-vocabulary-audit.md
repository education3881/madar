# Growth — the topic vocabulary audit: half the corpus has no topic page

**Date:** 2026-09-15
**Owner:** Growth · routed to the Editor, whose vocabulary it is
**Occasion:** the 09-14 bet (taxonomy index pages) shipped and is live. This is its read, one day later — the discipline the CHARTER asks for: *one bet per week, and the review reads its result.*
**Status of the bet itself:** shipped, live, verified on the origin today (`/browse/topic/ai-readiness/` fetched as served — 6 pieces listed, the "Elsewhere in the archive" rail resolving, the `--color-accent` fix from 09-14 serving, canonical and hreflang correct).

---

## 1. What the bet bought

Live and confirmed on the origin: `/browse/` and `/ar/browse/`, plus **18 index pages per language** — 7 regions, 8 topics, 3 countries. Sitemap **82 → 120**. `qa_reachability` reports **zero orphans across the 120-page graph**. The bet did what it said.

## 2. What reading it found

The 09-14 run flagged, correctly and in one line, that `government-led programs` sits on the entire corpus and therefore carries zero information. Counted properly today, that observation is the small end of a bigger one.

**38 approved English pieces · 14 distinct tags · 127 applications · 3.34 tags per piece.**

| tag | n | share of corpus | earns a page? |
|---|---:|---:|---|
| government-led programs | 38 | **100%** | no — true of the entire corpus |
| access | 34 | 89% | no — true of most of it |
| value of teachers | 26 | 68% | no — true of most of it |
| language and heritage preservation | 8 | 21% | yes |
| AI-readiness | 6 | 16% | yes |
| ECE access · female education · national identity · sustainability · student wellbeing · education for displaced children | 2 each | 5% | yes |
| inspiring stories · parent-led projects · curriculum | 1 each | 3% | no — one piece, a dead end |

**The finding: 20 of 38 pieces — 53% of the published corpus — are reachable from no topic page at all.** Every one of those 20 carries *only* the three universal tags, and 23 pieces carry all three together. The eight topic pages that exist cover 18 pieces between them.

**Stated precisely, because the distinction matters:** those 20 pieces are *not orphaned*. Every one is reachable from its region page and from the front door, and `qa_reachability` is right to pass. What they lack is the **subject** axis — the one a reader uses when they have just finished a piece and want another about the same thing. A reader who finishes the US NAEP piece and wants more on assessment honesty has a region page to South-America-and-back and nothing about the subject.

## 3. Why it happened, and why it is not a tagging mistake

The vocabulary is doing two jobs at once and only one of them well.

`government-led programs`, `access` and `value of teachers` are not bad tags. They are the publication's **editorial commitments** — the three things Madār has decided it is about. Being true of the whole corpus is a sign that the commitments held, not that the tagging slipped. But a commitment and a facet are different instruments: a commitment says *what we publish*, a facet says *which of the things we published you want next*, and the schema has one field for both. A term true of everything is a perfect statement of identity and a useless filter.

The evidence that this is structural, not sloppy: **the ruler piece drafted on 09-14 — 2,170 words whose entire subject is measurement — is filed under `government-led programs`, `access` and `value of teachers`, and none of the three is `assessment`.** There is no `assessment` tag. There is no `curriculum reform`, no `examinations`, no `teacher workforce`. The drafter did not mis-tag it; the vocabulary had nothing else to offer.

Counted, the missing facets are visible in the corpus already. On a skim of the 20 unreachable pieces, at least four clusters are large enough to earn a page under the browse surface's own rules (≥2 pieces, <50% of the corpus) the moment a term exists for them: **assessment and examinations** (NAEP, NAPLAN, PSLE, SIMCE, the doorstroomtoets, PARAKH, the ruler piece — seven at a glance), **education in conflict and displacement** (Gaza, Ukraine, Syria, Yemen, Lebanon, Sudan, Chad, Poland, Rohingya — nine, against the existing `education for displaced children` which holds two), **curriculum reform** (Ghana CBE, Kenya CBE, Indonesia, Morocco), and **teacher workforce and pay** (Sierra Leone TSC, Yemen, England).

## 4. Why it is a growth finding and not only an editorial one

Three reasons, in order of size:

1. **Edges are the discoverability instrument this site actually has.** With 0 of 120 URLs indexed at the last `site:` observation, the first crawler to arrive walks the graph. Four new topic pages at current corpus size would add roughly 26 article edges and ~32 index-to-index edges, and — unlike the region axis, which is nearly saturated — the topic axis grows with every piece.
2. **It compounds with the Edition 05 flip at no extra cost.** Six pieces land at once; on the topic axis as it stands they would arrive carrying the three universal tags and appear on no new page.
3. **It is the return-rate surface, not the reach surface.** The CHARTER measures return, not raw counts. A reader who came for one piece and found a page of five more on the same subject is the only mechanism this site has for a second visit, and it currently works for 47% of the corpus.

## 5. The ask — the Editor's call, not Growth's

Growth proposes and does not decide, because a controlled vocabulary is editorial doctrine (`/docs/20_topics.md`).

1. **Split the field's two jobs.** Either retire the three universal terms from `themes` and record the editorial commitments where they belong — in the charter, not in per-piece frontmatter — or keep them and mark them `commitment: true` so the browse derivation excludes them by declaration rather than by the 50% heuristic. The heuristic is currently doing doctrine's job silently, which is the wrong place for a decision this size.
2. **Add the facets the corpus has already earned**, on evidence rather than on taste: `assessment` first, since it is the largest cluster and the publication's most distinctive beat; then `conflict and displacement` (or widen the existing term), `curriculum reform`, `teacher workforce`.
3. **Re-tag on the way past, never in a batch.** Each piece gains its facet when a run next touches it — at the Ed05 flip for the six, and opportunistically otherwise. A 38-file sweep is the kind of change that lands unverified.
4. **Set the rule for new terms**, so this does not recur: a term enters the vocabulary when it is true of at least two pieces and false of at least half. A term that fails the second test is a commitment, not a facet.

**Not proposed, deliberately:** no new page is built until the vocabulary decision is made. Building topic pages on terms the Editor has not approved would be Growth setting editorial doctrine by shipping, which is exactly the move the routing rules exist to prevent.

## 6. This week's bet, and the honesty line

**Bet for the week of 09-15:** the topic vocabulary decision, and the pages that follow it. It is stated as a bet rather than a task because its outcome is readable: *does the share of the corpus reachable by a topic page rise from 47%?* That is a number the operation owns end to end — unlike the 09-06 IndexNow bet, which was dropped for the opposite reason (**a bet whose outcome the operation does not own is a request, not a bet**).

**Traffic:** the site carries no third-party tracker by design, so there are no visitor numbers to report, and none are estimated here. The figures above are counts of our own corpus and our own graph, which are the only things we can honestly count. The fifth `site:` observation stands at zero indexed URLs.

— Growth · 2026-09-15
