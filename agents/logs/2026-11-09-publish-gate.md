# Publish gate — `2026-10-23-bahrain-bqa-five-cycles`, EN + AR

**Date:** 2026-11-09 · **Gate run by:** the Manager · **Verdict: PASS — the flag moves.**

**This is the first piece Madār has shipped since 2026-09-27** (43 days) and the **first single** under
the standing ledger, which opened 2026-11-08 when GitHub issue #13's stated default fell due in silence.
It is also **the first piece in this publication's history to ship with no `edition:` field at all.**

---

## The eight cells

| # | Cell | State | Evidence |
|---|---|---|---|
| 1 | Editor's brief | ✅ | `content-drafts/briefs/2026-10-21-bahrain-bqa-five-cycles-brief.md` |
| 2 | EN draft | ✅ | `content-drafts/drafts/2026-10-23-bahrain-bqa-five-cycles.md` |
| 3 | Editor five-test verdict | ✅ | `2026-11-02`, + dispositions 1–2 (11-05), 3 (11-07), **4 (11-09)** |
| 4 | AR composition | ✅ | `content-drafts/drafts/2026-11-07-bahrain-bqa-five-cycles-ar.md` |
| 5 | Arabic Editor's gate | ✅ | `2026-11-09-bahrain-bqa-five-cycles-arabic-gate.md` — PASS, three binding corrections, all executed |
| 6 | Verifier verdict | ✅ | `2026-11-03`, + retrace `2026-11-07` |
| 7 | Hero still + og card | ✅ | `web/public/stills/…svg` and `web/public/og/…png`, 1200×600, 1,849 bytes, **rendered and looked at** |
| 8 | `approved: true` both editions, assets in the same commit | ✅ | this gate |

## The build

`cd web && npm run build` → **exit 0**, with **all 39 gating assertions green**, the twelve build-job
gates included via `build_job_gates` (which is why a green local build is the deploy's gate set and not
two-thirds of it, 2026-10-21).

**Five gates bit on this piece before it could ship, and every one of them was right.** Recorded in the
order they fired, because a gate that catches a real defect on a real ship is the only evidence that the
gate set is load-bearing:

1. **`qa_pair_frontmatter`** — *the pair's sources cite different registers and nothing declares why: 3 EN-only, 3 AR-only.* True. **Declared**, with its exact URL sets, as the fourth declared asymmetry in the corpus: three documents, each cited in each edition's own first-party edition — the Authority's open-data page in both languages, its Performance Report 2024-25 in the Arabic and English editions it publishes side by side, and our own predecessor piece in each language. The Morocco shape three times over, and the third could not be anything else.
2. **`qa_claim_registers --check`** — *8 cited registers have no row.* The piece's registers had never been asked about, by construction (they were not in the corpus). `--emit` asked all 8. **Result in the risk row below.**
3. **`qa_citation_identity --check`** — *6 registers supply a quoted identity token and have no row.* `--emit` asked. **Two came back wrong, and both were real.** See the two findings below.
4. **`qa_annotation_figures`** — *46 annotation quantities neither printed in their own body nor registered.* Disposed in two classes, below.
5. **`build_job_gates`** — three of the twelve red: `qa_body_links` (no piece points at the new slug), `qa_jsonld` (Article missing image, both editions), `qa_consumer_surface` (`og:image` MISSING, both editions). All three were one missing `hero:` block and one missing reciprocal rail. **The still existed on disk and the card existed on disk, and the page still shared with no image** — which is the 08-18 lesson in its exact original shape: *a resolving asset is not a usable asset*, and the thing that makes it usable is the frontmatter that points at it.

## The two citation findings, both caught by an instrument and neither by a reader

**Finding 1 — we composed the Arabic title of our own predecessor instead of reading it.**
`qa_citation_identity` reported the Arabic annotation's quoted title as **absent** from the page it names.
Checked by hand against the served bytes: the annotation said
*«البحرين تُصدِر درجاتِ مدارسِها، بالاسم، في العَلَن»* and the served Arabic page is titled
*«البحرين تُقَيِّم مدارسها، بالاسم، على الملأ»* — a different verb, a different adverbial, and a
different object. **The English token on the English page came back `confirmed`.** So the Arabic
annotation's title was composed from the English title rather than read off the Arabic page, in the one
annotation of this composition whose register is *our own page* — in a composition whose own hand-off
line says every register was read and the English draft never was. **Corrected to the served title.**
*This is #101 pointed at ourselves: the free rendering was available, and it was taken.*

**Finding 2 — the licence sentence quoted a string the served bytes do not carry.**
Both editions stated that the portal *prints `Licence unknown`*. The dataset page is a client-rendered
application; its metadata is not in the served HTML and the literal appears nowhere in 160,101 bytes.
The claim was read in a rendered view during recon and then quoted as though it were in the register's
text (#112, and #131 on the other side). **Restated in both editions** as what can be defended — the
metadata is not in the served bytes, no licence was shown in the rendered view read 2026-10-23, and
*what is not known is not assumed* — with the operative restraint **unchanged and strengthened**: counts
are reported, the table is not reproduced, excerpted, charted or embedded.

## The annotation-figure disposal, in two classes

46 quantities were annotation-only. They are not one population and were not disposed as one.

- **Our own apparatus — REMOVED, not registered.** Byte lengths, cmap glyph counts, the sum-closes-at-100 check. This is the piece's own standing decision of 2026-10-25 (*a reader of the article page is being told the byte length of a PDF we opened*), re-applied — and it had to be re-applied because the draft **reacquired** those numerals through the #112 and disposition-3 work after it had already stripped them once. *A removal is not a state; it is an event, and the next edit can undo it.*
- **The register's own counts — REGISTERED, with real provenance.** The twenty per-cycle × per-grade cells and the three monitoring-scale counts are the Authority's data, carried in both editions after disposition 4, and the body's percentages are arithmetic over them. 24 entries written by hand into `agents/stats/annotation-figures.json`, each naming the column it was counted in and the date, plus two non-quantities (a filename fragment, and the day of a `Last-Modified` date written with an Arabic month name — the same blindness #117 clause 4 records for the Arabic future prefix, one licence over).

Register now: **455 annotation-only quantities across 41 pieces, 455 registered, 228 still UNTRACED**
from the 10-24 seeded backlog.

## ACCEPTED RISK — the archival row, and disposition 1 named the wrong registers

Editor disposition 1 (2026-11-05) accepted *"registers with no archival snapshot: 2 of 5, both
first-party PDFs"* and bound this gate to write the two URLs out. **Measured this morning for the first
time, because the registers had never been asked: it is 3 of 8 across the pair, and the composition is
not what the disposition guessed.**

| Register | Archive state |
|---|---|
| **`data.gov.bh` dataset — THE PIECE'S SPINE** | **live-only, no snapshot anywhere** |
| **BQA Annual Report 2025 (EN)** | **live-only, no snapshot** |
| **BQA Performance Report 2024-25 (AR)** | **live-only, no snapshot** |
| BQA Performance Report 2024-25 (EN) | archived 2026-07-17 |
| `bqa.gov.bh/open-data/` | archived 2026-01-18 |
| `bqa.gov.bh/ar/open-data/` | archived 2026-01-10 |
| our EN and AR predecessor pages | `ours-git-archived` — this repository is their archive |

**The disposition guessed two PDFs; the PDF it was most confident about is archived, and the register it
did not consider at all is the one every count in the piece rests on.** That is #111's own lesson
arriving one more time: *a per-URL sweep reports a rate spread over a corpus; the claim-level join
reports which piece's spine cannot be re-opened.*

**Why the spine is not archived, and it is our constraint rather than the register's.** Issue #12's
option B was applied 2026-11-04: *the standing question comes back to you before any new URL is ever
sent.* The `data.gov.bh` export is a new URL. **This operation is forbidden to preserve the register its
own publication stands on**, by a default it adopted to discipline an earlier overstep. The cost of that
default has arrived on the first piece shipped after it.

**Why the piece ships anyway, and it is not a judgment made this morning.** The re-made issue #12
comment already ruled on exactly this case, in writing, before it occurred:

> *If the piece's Arabic composition and gates complete sooner, the piece does not wait on this: it
> ships under the Editor's disposition with the single-copy state recorded, because an unanswered
> question about archiving must not become a hold on publication.*

And holding does not help: **the window in which a document can be preserved is the window in which it
is still there**, so a hold spends the thing it would be protecting. The register is live, first-party,
a state open-data portal; its counts were read four times across 18 days and counted independently in
two languages by two desks, agreeing cell for cell. The risk is **re-verifiability, not accuracy**, and
it is disclosed in the annotation a reader sees.

**Conditions carried forward:** issue #12's B′ default falls due **2026-11-11**. If it passes in
silence, B′ is applied and **these three URLs are the first three sent** — and disposition 1 clause 3
then supersedes itself *by the snapshot rather than by a new judgment*.

## Held-slug leak

**Zero.** `qa_held_assets`: held slugs 0, approved slugs 45. `qa_census`: content pieces 90, approved 90,
held 0. The corpus is in all-approved mode and the 2026-08-09 inverted assertion is the one that applies.

## What does NOT change, recorded so no one looks for it

- **The registry stays at five editions, all `closed`, `hasOpenEdition` false.** There is no Edition 06 and this piece joins none. `/editions/` skips a null edition by code that has always been there.
- **No code change was needed to ship a piece with no edition.** That is the operational proof of what the standing ledger asserted in prose: option B was the only option executable without a word from the founder.
- **One consequence, raised and not patched here:** from today `/editions/` is no longer an index of the published corpus, and its own standing sentence — *"Madār publishes in monthly editions. Each one gathers the issue's pieces"* — is now false about the corpus. Routed to Growth.

---

**PASS. The flag moves in the same commit as the article text, both editions, and the still and the og
card travel with them** (the 2026-06-14 rule).

— Manager · 2026-11-09
