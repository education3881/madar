# Verifier's verdict: `2026-11-26-jordan-pisa-2025-counts-from-2022`

**VERDICT: VERIFIED WITH CORRECTIONS REQUIRED — five corrections, all applied in-run, in both editions.**

Verifier, 2026-11-26. I did not write this piece. I read the brief, both drafts, the Editor's verdict and
the Arabic Editor's gate. **I re-fetched every register myself rather than reading the run's copies**: the
three OECD snapshots from the Internet Archive and the Jordanian notice direct from `nchrd.gov.jo`. The
Jordanian page is live and un-archived, so I re-fetched it a second time at the end of the audit and
diffed: **identical text on both reads**, which is the only staleness control available for a register
nobody has snapshotted.

**No quotation is wrong and no figure is wrong.** All five corrections are about what a sentence claims
beyond its register — and **two of the five were visible only because the two editions disagreed**, which
is #86 arriving as a method rather than as a principle.

## 1. Quoted spans

| edition | quoted spans | verbatim against register | not comparable |
|---|---|---|---|
| English | 27 | **8 of 8 comparable** | 19 (translations of an Arabic register) |
| Arabic | 30, of which 29 are quotations | **29 of 29** | 0 |

Normalisation ledger (#159), English: whitespace only on 7; sentence-initial case folded on 1
(*"further PISA analysis will follow in 2027"*, register prints *Further*); terminal punctuation moved
outside the quotation on 2; **words changed: 0**. Arabic: whitespace only on 27; tashkeel absent from the
register and absent from the quoted spans, so no folding was needed on any; the register's own inner double
quotes are reproduced as the register prints them on 2 ("بيزا", "كورونا", "بؤرة العناية"); **words changed: 0.**
The thirtieth Arabic «...» span is the OECD volume's Arabic title, not a quotation, and is declared rather
than counted.

**I did not attempt to verify the English edition's nineteen.** No instrument this operation owns can, and
the translation check is the Arabic Editor's and is on file at cell 5. I read it and I concur with its
routing: the Editor was right to decline a verdict there.

## 2. Figures

Fifteen quantities are taken from the Jordanian register. I checked each against my own fetch of it:
**375, 407, 361, 388, 342, 363, 365, 400, 353, 382, 332, 358, 8,290, 276, 91** — all fifteen present as
printed, each once except 91, twice.

**The numeral multisets of the two editions are identical**, element for element:
`12, 19, 2015, 2018, 2022, 2025, 2026, 2027, 276, 332, 342, 353, 358, 361, 363, 365, 375, 382, 388, 400,
407, 8, 8,290, 91`. (`19` is COVID-19, `12` is R3's "12 other countries and economies", `8` is 8 September.)

**No figure in either edition is computed.** I checked for the whole class, not for instances: no
difference, no percentage, no ratio, no average-of-averages appears in either body. `contains_composites:
false` holds in the strong sense.

## 3. The five corrections

**(a) "closed" where the register says "narrowed". ENGLISH ONLY.** The English read *"Two gaps are reported
as having closed"* and headed a later section *"Which way the two narrowed gaps closed."* The register says
`تقلصت بشكل واضح` — narrowed clearly. A narrowed gap is not a closed one. **The Arabic edition had it right
the whole time** (`فجوتان ضاقتا`, `في أيِّ اتّجاهٍ ضاقت الفجوتان`), so the error was invisible to any
single-edition read and visible immediately to a paired one. Corrected in English.

**(b) A cross-scale ranking of the three domains. BOTH EDITIONS.** Both read that reading at 363 was *the
lowest of the three averages the centre reports*, and the English went on to call reading *"its weakest
subject"*. **PISA scales each domain separately**, so 363 in reading and 407 in science are not two points
on one ruler and neither is "lower" than the other in any sense a reader will take from that sentence. This
is #29 (a ranking is not a measurement) in the one place the piece did not look for it — inside a single
register, across its own three figures. Both bodies now state in their own words that the three domains are
reported on three separate scales and that the piece does not rank them, and both rest the paragraph on what
the two officials actually said. **The cleanest form of this correction is that the piece now has a reason
not to rank, where before it had an ordering and no reason.**

**(c) "the public sector alone" for government schools. ENGLISH ONLY.** The register's category is
`المدارس الحكومية`, government schools, and it names UNRWA and the private sector as the other authorities
beside them. "Public sector" is a gloss that silently moves UNRWA. Corrected to *government schools*.

**(d) Two attributions of carefulness. ENGLISH, and one in Arabic.** *"On ranks the centre is careful too"*
and *"the caution that any ministry reporting a two-round gain owes its readers"* both attribute a motive
and an obligation to the register. Replaced with what is observable: *the centre prints no rank at all*, and
*one more caution*. The Arabic's matching clause was recomposed, not translated.

**(e) A venue and a convener. Both already struck at cell 3**, and I confirm the register supports neither:
it names who attended and gives no venue and no convener. I re-read the register for this specifically
because the Editor's note said so, per #53 — *the fact a re-read misses is the one that was never in
dispute*.

## 4. The eight trace axes and the four non-numeric rows

| axis | result |
|---|---|
| vintage | PASS. Every Jordanian figure is a 2022-to-2025 pair and says so. The OECD list is dated 2022 by R3 and the body says which register dates it. |
| scope | PASS. National averages and government-school averages are never mixed. The Schools for Excellence claim is scoped to a school category in both editions. |
| direction | PASS. Every figure runs 2022 then 2025, in that order, in both editions. |
| position | PASS. No rank is printed or implied in either edition. |
| condition | PASS. "Statistically significant" is carried as the centre's statement wherever a gain is called significant. |
| units | PASS. Points are points, students are students, schools are schools. **See 3(b): the one units failure was across domains, which this axis has never had a row for.** |
| population | PASS. 8,290 students, 276 schools, four named authorities, 91 participants. |
| arithmetic | PASS, vacuously — there is none. |
| noun (#45) | PASS. "Badia schools" and "educational authorities" are the register's own categories, not smoothed. |
| quotation (#46) | PASS, English at 8 of 8 comparable; Arabic at 29 of 29. |
| clock (#46) | **FAIL, corrected — 3(a).** |
| description-date (#47) | PASS. The notice's own date, 8/9/2026, is rendered 8 September 2026 and matches the day the OECD launched. The day name the register prints, Tuesday, is the correct weekday for that date. |

## 5. Flag state, schema and assets (#18, and the 2026-06-14 rule)

- Both files carry `approved: false` at the time of this verdict and flip in the same commit as each other.
- Hero still on disk at `web/public/stills/2026-11-26-jordan-pisa-2025-counts-from-2022.svg`, raster share
  card at `web/public/og/2026-11-26-jordan-pisa-2025-counts-from-2022.png`, 1200x600, both written before
  this verdict and shipping in the flip commit.
- `related:` — all three targets exist in both collections and all three are `approved: true`. Rail counts
  before the forward edges: 2, 5, 4. After: 3, 6, 5. **All under the cap of 6, and `us-naep-honesty-gap`
  reaches it exactly** — the next piece that wants to rail to it must displace something.
- Caps: EN title 23, dek 193 of 200. AR title 21, dek 198 of 200 code points, tashkeel counted.
- `country: Jordan` resolves in `i18n-geo.ts`. `region: MENA`, `level: K-12`, both themes mapped.

## 6. What this audit could not see

**Whether the Jordanian register still says this in a month.** It is live, un-archived and served from a
site with no snapshot of this page anywhere. Every other register in this piece has an Internet Archive
snapshot standing behind it and this one has none, so the citation this piece leans on hardest is the one
with the weakest re-verifiability — which is `qa_claim_registers`'s subject arriving on a piece rather than
in a sweep. **And the obvious repair is forbidden, which is the part worth writing down.** Asking archive.org to
keep a copy of this page is exactly what founder issue **#12** is about, and that issue's stated default —
option B, applied in silence on 2026-11-01 — closed the backlog of 23 named registers and said in writing
that *the standing question comes back to him before any new URL is ever sent.* `News_PISA_2025.aspx` is a
new URL. So this run did **not** send it, and `qa_claim_registers` carries the register as
`archive-unknown / not yet asked` on purpose rather than by omission. **The piece ships with its spine
resting on one copy of one page, and that is a decision the operation is not permitted to reverse by
itself.** Named in the brief; it belongs on issue #12 and nowhere else.
