# Publish gate — `2026-11-12-england-ofsted-exempt-cohort`, both editions

**Run 2026-11-21 (Asia/Dubai). Cell 8 of eight, the flip. Written BEFORE the commit, per the skill.**
This is the first piece to ship as a **single against the standing ledger** — no edition, no wave, no
all-or-nothing flip (`content-drafts/_STANDING_LEDGER.md`, opened 2026-11-08 on issue #13's default B).
The last piece to ship was `bahrain-bqa-five-cycles` on **2026-11-09**, twelve days ago.

## The eight cells

| Cell | State | Evidence |
|---|---|---|
| 1 · Editor's brief | FILLED 2026-11-12 | `content-drafts/briefs/2026-11-12-england-ofsted-exempt-cohort-brief.md` |
| 2 · EN draft | FILLED 2026-11-14, rev 3 2026-11-18 | `content-drafts/drafts/2026-11-14-england-ofsted-exempt-cohort.md` |
| 3 · Editor five-test verdict | FILLED 2026-11-16 — APPROVE on all five | `content-drafts/verdicts/2026-11-16-england-ofsted-exempt-cohort-tests-3-4-5.md` |
| 4 · AR composition | FILLED 2026-11-17 | `content-drafts/drafts/2026-11-17-england-ofsted-exempt-cohort-ar.md` |
| 5 · Arabic Editor's gate | FILLED 2026-11-18 — APPROVE, conditions A and B | `content-drafts/verdicts/2026-11-18-england-ofsted-exempt-cohort-arabic-gate.md` |
| 6 · Verifier verdict | FILLED 2026-11-19 — PASS WITH FOUR ITEMS | `content-drafts/verdicts/2026-11-19-england-ofsted-exempt-cohort-verification.md` |
| 7 · Hero still + og card | FILLED 2026-11-20 | `content-drafts/briefs/2026-11-20-england-ofsted-exempt-cohort-hero-brief.md` |
| 8 · `approved: true` both editions | **FILLED TODAY** | this gate |

## The six conditions cell 8 carried, each discharged by name

**A · the eleven grade renderings declared in the SERVED Arabic annotation** (Arabic gate, #86 clause 2 /
#114). Done: the Arabic `sources[]` entry for register 1 now carries all eleven as this edition's own
determination, **dated 2026-11-17**, names Ofsted's non-publication in Arabic as the reason no register
can carry them, and names the two — `غير ملائم` and `جيد` — that a **different** regulator publishes in
Arabic on `2026-10-23-bahrain-bqa-five-cycles`, where they are a quotation and not ours. A reader of the
served page can now tell which is which; before today only the Editor could.

**B · sources 3 and 4 marked SINGLE-CHANNEL.** Done, in both editions. The Arabic desk did not re-open the
Department's 2 September 2024 release or the parents' guidance, so both annotations carry the **English**
read-date of 2026-11-14 and say in their own text that they are not a second channel.

**C · §A1 rewritten.** Done in the draft. The register **does** print *"Only 17% of previously exempt
schools that had a graded inspection this year remained outstanding"* — in its own Key findings block —
and it **states its denominator explicitly**, which is the denominator the body uses. Both of §A1's
original limbs were wrong; the body was right for a reason it had stated wrongly.

**D · §A4's first two strikes withdrawn.** Done. The 86% series sentence and the *"not met"* safeguarding
half are both in their registers. The third strike **stands** (the Department's page carries nothing about
retrospectivity, verified absent twice). All three are kept on the page because nothing distinguished the
correct one from the two that were not — ruling #151.

**E · source 5's annotation repaired — the one of the four that REACHES A READER** (#114). Done in both
editions. It read *"Not carried, because it was not read"* about wording the register does carry. It now
states what register 5 carries **in both directions** — the 99% sentence and the 18 schools (0.6%) — and
what this piece chose not to use, so the omission is a visible editorial choice rather than an implied
silence in Ofsted.

**F · hand-off line 1 corrected to `dek: 198/200`.** Done. It read `188`; the dek is `198`. A transposed
digit inside the rule that exists to stop exactly this. Queue item 133.

**The rail step (`_STANDING_LEDGER.md`, 2026-11-12) — forward edges written in the SAME commit as the
flip, both editions.** Backward: `2026-10-23-bahrain-bqa-five-cycles`, `2026-05-26-bahrain-bqa-public-grades`,
`2026-07-28-england-report-cards-first-term`. Forward, into those three: two were added at 3 → 4 rails.
**The third hit the cap and forced a judgment, recorded rather than silently taken:**
`2026-07-28-england-report-cards-first-term` already carried **6 rails, the proven maximum**, so a seventh
was not available. `2026-08-28-sierra-leone-sleic-outcomes` was displaced for the new piece, in both
editions, on this reasoning: of that page's six rails it is the only one about **pupil examination
outcomes** rather than about an instrument that grades schools or systems, while the new piece is the same
country, the same regulator and the direct counterpart — one piece watched the grade being withdrawn, this
one measures what the old grade had managed to say before it went. *A displacement nobody writes down is
how a curation decision becomes an accident.*

## Caps, counted at the desk and re-counted here

| | EN | AR | Cap |
|---|---|---|---|
| `title` | **34** | **25** | 100 |
| `dek` | **198** | **162** | 200 |

Code points, tashkeel +1 each, counted with `len()` over the composed strings in the shipped files.

## THE QUOTATION AUDIT — EVERY QUOTED SPAN IN BOTH EDITIONS AGAINST ITS REGISTER'S OWN BYTES, TODAY

Not required by the gate and run anyway, because the two instruments that would eventually ask this
(`qa_citation_identity`, `qa_claim_registers`) had **no row for any of this piece's registers** — the piece
is new, so both gates correctly **failed the build** rather than narrowing in silence. Emitting those rows
asked the world about our quotations for the first time, and it is worth recording what came back.

**All five first-party registers plus our own two pages were fetched and read as served text.
65 of 65 quoted Latin spans in the EN body are byte-identical to a register's served bytes. 29 of 29
Latin annotation tokens EN, 5 of 5 AR. Zero absent.**

**And six defects were found and repaired in the hour before the flip, five of them MINE, written this
morning:**

1. `It's` / `can't` in the guidance quotation — the register serves **U+2019** and the body carried
   **U+0027**, three occurrences. Repaired to the register's own characters.
2. The guidance's nested quotes — the register prints `‘good’, ‘outstanding’ or ‘requires improvement’`
   with U+2018/U+2019; the annotation had straight double quotes. Repaired.
3. `Ofsted’s Chief Inspector, Amanda Spielman, said:` — **U+2019** on register 2, U+0027 in both editions'
   annotations. Repaired. **Ruling #150's fourth firing, and the first inside a SERVED annotation.**
4. `His Majesty’s` — same, same page as 5 below but the opposite convention. Repaired.
5. The standfirst quotation carried our own markdown `**her**` **inside the quotation marks**, which makes
   a quotation of nobody's bytes. Repaired, and the asymmetry recorded in the annotation itself: **register
   6 serves U+0027 and register 2 serves U+2019 — one publisher, two conventions, on two pages.**
6. The 2026 release titles itself *"Main findings: **state-funded** schools…"* in lower case where its 2022
   predecessor capitalises. Our annotation had copied the 2022 convention onto the 2026 title. Repaired,
   and each is now reproduced as its own page prints it.

**One false positive of my own probe, recorded because it read exactly like 37 defects.** The first run
reported 37 of 65 spans absent. The needles carried the **source markdown's hard line wraps**; the register
text is whitespace-normalised. *A bite wider than the rule it targets manufactures the defect it was aimed
at* (#115), met here on the input side within one minute of the output being believed.

**Also confirmed, by machine, independently of the Verifier:** the three sentences the Verifier's items 1–3
said were present and the draft said were absent are **all three FOUND** in their registers' served bytes
today — *"Only 17% of previously exempt schools…"*, *"The proportion has increased from 86%…"*, *"In the 18
schools (0.6%) where safeguarding standards were not met"*. #151 was filed on a second human reading; this
is the same conclusion from a different instrument.

## Build and assertions

- `npm run build` — **exit 0**, all **28** `postbuild` assertions green.
- `npm run gates` — **CLEAN, all 12 build-job gates** green against this tree's `dist`, so the local gate
  set is the deploy's gate set rather than two-thirds of it (#110).
- `qa_claim_registers --emit` → **CLEAN at 368 cited registers, every one with a dated observation**; the
  seven new registers were asked for the first time today.
- `qa_citation_identity --emit` → 250 rows, the new piece's **8** registers added.
- `qa_annotation_figures` — **OK**. Eight annotation-only quantities were hand-written into
  `agents/stats/annotation-figures.json` with their provenance, as that register requires: the 86% series
  and the 0.6% are **deliberately annotation-only** under conditions D and E, and `404`, `0027`, `150`,
  `151`, `114` are an HTTP status, a Unicode code point and three ruling numbers — *digits that are not
  quantities about the world*, which is the boundary #114's register exists to hold.
- `qa_held_assets` — CLEAN. **No held piece contributes bytes, and every approved asset is served.**
- `qa_pair_frontmatter` — CLEAN, held pieces included.
- **Held-slug leak: zero.** The corpus moves 45 EN / 45 AR → **46 / 46**, parity 100%.

## Assets

`web/public/stills/2026-11-12-england-ofsted-exempt-cohort.svg` (6,266 b) and
`web/public/og/2026-11-12-england-ofsted-exempt-cohort.png` (1200×600, 7,800 b), copied across from
`design-assets/` **in this commit, with the article text** — the 2026-06-14 rule. They were staged outside
`web/public/` from 11-20 to today because a piece mid-gate is neither held nor approved and nothing
withholds it (ruling #152, queue item 140).

## Verdict

**PASS. Both editions ship.** All eight cells filled, all six conditions discharged by name, the rail step
executed in both directions with its one displacement written down, every quoted span traced to served
bytes, 40 of 43 assertions green and the twelve build-job gates run locally.

— Manager, for the record · 2026-11-21
