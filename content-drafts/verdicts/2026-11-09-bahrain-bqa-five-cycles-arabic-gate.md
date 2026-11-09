# Arabic Editor — Gate 4 · `bahrain-bqa-five-cycles`

**Gate:** 4 of 8 on the standing ledger (`content-drafts/_STANDING_LEDGER.md`) — the Arabic Editor's gate.
**Composition under gate:** `content-drafts/drafts/2026-11-07-bahrain-bqa-five-cycles-ar.md`
**EN pair:** `content-drafts/drafts/2026-10-23-bahrain-bqa-five-cycles.md` (Editor-approved 2026-11-02;
dispositions 1–2 on 11-05, 3 on 11-07; Verifier verdict 11-03 with a retrace 11-07)
**Date:** 2026-11-09 · **Verdict: PASS, with THREE binding corrections, all three executed today.**

The Arabic Editor is a pure verifier (RUNBOOK, the 2026-05-26 compose-vs-judgment split). This desk did
not compose a line of the Arabic and does not here.

---

## 1 · The hand-off lines — all five present, and two measured rather than accepted

| Line | Claimed | This gate's reading |
|---|---|---|
| Caps (07-27) | `dek: 158/200 · title: 47/100` | **Re-counted in code points: 158 and 47.** Exact. |
| `annotation == sentence` (09-13) | every figure read in the Arabic column or the Arabic edition | Verified against the EN pair cell by cell — see §2 |
| Named humans, gender from register (#86/#134) | **0 of 0** | Correct and **vacuous, and it says so**. The body names no individual; the predecessor's Dr. Maryam Hasan Mustafa is established there and is referred to, not re-run. **The transliteration duty this gate exists for had nothing to transliterate** — recorded because a gate that reports a clean limb it never exercised is the 08-16 silent-pass trap. |
| Acronyms (#101) | **0 expanded, vacuously ☑** | Correct, and it is the strongest instance of #101 this operation has: the body carries **no Latin-script token at all**, and names the regulator as the Authority names itself in Arabic, **هيئة جودة التعليم والتدريب**, read from the Authority's own Arabic open-data page. The EN edition expands `BQA` once and carries the expansion in its annotation 2. |
| Editorial futures (#117) | — | **Read by this gate rather than by a string match.** One future-marked verb in the whole body, `سيجد`, and it is generic and about a reader (*anybody who wants to say how much will find that this register cannot tell them*) — not an editorial future about a dated event. C5 is carried in the **present** (`تجري`) and bounded by the register's own most recent publication, April 2026. **PASS.** |

**The caps line is worth one more sentence.** The EN pair's own hand-off records that its first dek came
out at 225 and was cut before it left the drafter's hand — the fourth strike of the 07-27 shape caught at
the ruler rather than at the backstop. The Arabic came in at 158 with tashkeel already counted, and the
Arabic is the edition where that cap bites earliest (a fully-voweled dek fails at ~150 visible
characters). Both measured here, both true.

## 2 · Composition, not translation — and for the first time the EVIDENCE IS ARITHMETIC

This gate's hardest standing question is the one it can rarely answer: *was this composed from the
register or rendered from the English draft?* Every previous pair has been judged on grammar, register
and idiom — on how the Arabic reads. **This one can be judged on what the Arabic KNOWS.**

Annotation 1 of the Arabic edition carries **twenty-three quantities that appear nowhere in the English
edition**: the full per-cycle × per-grade counts, and the three-band monitoring scale.

| | `(1)` | `(2)` | `(3)` | `(4)` | AR total | EN table |
|---|---|---|---|---|---|---|
| C1 | 7 | 60 | 94 | 41 | **202** | 202 ✓ |
| C2 | 14 | 48 | 89 | 55 | **206** | 206 ✓ |
| C3 | 31 | 39 | 70 | 67 | **207** | 207 ✓ |
| C4 | 10 | 25 | 41 | **52** | **128** | 128 ✓ |
| C5 | 23 | 30 | 56 | 30 | **139** | 139 ✓ |
| **Column** | **85** | **202** | **350** | **245** | **882** | 85 / 202 / 350 / 245 ✓ |

Monitoring, the other instrument: `(B) قيد التقدم` 97 + `(C) تقدم غير كافٍ` 23 + `(A) تقدم كافٍ` 20 =
**140**, and 882 + 140 = **1,022**. Every margin closes, in both directions, against a table the English
edition prints only as percentages.

**A translation cannot produce a figure its source does not carry.** The English draft's §"THE PER-CYCLE
DISTRIBUTION" is draft apparatus and is not served; the English *annotation* says only *"per-cycle counts
as tabulated above"*. So these twenty-three numbers came out of the Arabic column of the register, by
hand, and they reconcile to the English count cell for cell. **PASS, and this is the first time in
forty-five pairs that the compose-not-translate claim has been settled by arithmetic instead of by
reading.** Recorded as a method: *ask what the second channel knows that the first never printed.*

## 3 · Correction 1 — `edition:` is prose in a numeric field, and the question it holds was answered yesterday

Both editions carry:

```
edition: HELD — there is no Edition 06 and the registry exports hasOpenEdition false.
         Blocked on founder issue #13, default 2026-11-08. Do NOT guess this field.
```

Two things are now true of that string. **It would not build:** `web/src/content.config.ts` declares
`edition: z.number().int().positive().optional()`, so prose in this field is a schema failure, not a
holding note. And **the holding is over:** issue #13's stated default fell due on 2026-11-08, no reply
arrived, option B was applied, and `_STANDING_LEDGER.md` is the live ledger. Pieces ship as singles.

**The correct value is the field's ABSENCE**, and the schema anticipated exactly this — *optional so
non-edition drafts never break*. Verified against every consumer before striking it, rather than assumed:

- `web/src/pages/editions/index.astro` groups by edition number and **skips `n == null`** (`if (n == null) continue;`). Same in the Arabic route.
- `web/src/pages/articles/[...slug].astro` never reads the field at all.
- `web/src/lib/editions.ts` holds the five registry rows and derives `hasOpenEdition` from their own `status`; a piece with no number touches none of it.

So **option B costs no code change**, which is the operational proof of the thing the ledger asserted in
prose: B was the only option this operation could execute without a word from the founder. **Executed in
both editions: the field is struck.**

**And one consequence nobody had written down, which this gate raises rather than fixes.** From the first
single, `/editions/` stops being an index of the published corpus — it indexes the five closed editions,
and the piece will be reachable from both home pages, both browse surfaces, both feeds and the sitemap,
but from no edition. The 08-17 orphan rule is satisfied (an inbound path exists, several). What is *not*
satisfied is the Editions page's own standing sentence, **"Madār publishes in monthly editions. Each one
gathers the issue's pieces"**, which becomes false about the corpus on the day this ships. **Routed to
Growth today, not patched here** — a served sentence about what this publication is is not the Arabic
Editor's to rewrite.

## 4 · Correction 2 — the pair publishes asymmetric figures, and the FORCED edition is the complete one

Under **#114** an annotation quantity is a *published* quantity; under **#42** a pair carries only what
both languages share. As handed to this gate the Arabic edition would publish the full cross-tabulation
(§2's twenty-three numbers) and the English edition would publish none of it — and the English annotation
would ship the words **"per-cycle counts as tabulated above"**, pointing at a draft table that is not
served. A dangling pointer in a served citation.

**This is #101's shape on an annotation instead of on a name.** Arabic could not carry the Latin acronym,
so the composer went to the register — and having gone there, counted, and printed the counts. The English
drafter had the option of a back-reference and took it. *The forced edition is the complete one; the free
edition is the one with the dangling pointer.*

**Routed to the Editor, who owns the English edition, and settled by disposition 4 today**
(`content-drafts/verdicts/2026-11-09-bahrain-bqa-five-cycles-disposition-4.md`): the English annotation 1
carries the same twenty-three counts explicitly. The Arabic annotation stands **unchanged** — this gate
proposes no cut to the complete edition to reach symmetry with the incomplete one, which is the wrong
direction and would have deleted §2's evidence.

## 5 · Correction 3 — a self-citation may not carry a byte length, because WE change those bytes

Arabic annotation 5 cites this publication's own served Arabic predecessor page, and states
*HTTP 200 و45,656 بايتًا*, read 2026-11-07.

Checked today, as #112 requires a quotation to be checked — against the bytes the annotation attributes
it to:

- The quotation is **exact**. 296 code points, matched verbatim in the served HTML after tag-stripping.
- The **byte length is already false.** The page serves **46,033 bytes** today.

Nothing happened to the register. **We happened to it:** commit `ffa3e0d` (2026-11-07 content function)
rewrote part of that very page, which is why the annotation's read date and its byte count are 48 hours
and 377 bytes apart. The piece already knows this lesson from the other side — its English annotation 1
says the CSV's own byte length moved 183,242 → 183,191 *"outside every field this piece reads — so the
stability claimed here is of the COUNTS and not of the bytes"*. The same discipline applied to our own
page gives a stronger result, because the moving party is us.

**Measured across the corpus before ruling on it:** `grep` for `education3881` over all 88 published
bodies returns **zero**. **This pair is the first in forty-four to cite Madār itself as a register**, in
both editions — necessarily, since the whole piece answers the predecessor's own closing question.
Twenty-six byte-length figures are published in annotations across the corpus and **every one of them is
about somebody else's document.**

**Executed: the byte length is struck from Arabic annotation 5.** What replaces it is the claim the byte
count was there to support and which survives our own edits — *read in logical order from the served HTML
on 2026-11-09, the quoted passage verbatim*. The HTTP code and the read date stay; both are true of the
fetch. **Handed to Research as the day's ruling candidate**, because the class is general and the corpus
is about to acquire its first two members.

## 6 · What this gate carried forward unchanged

- **Hand-off line 5 binds the publish gate: FOUR URLs, not two.** The Arabic edition cites the **Arabic** edition of source 4 (`Performance-Report-24-25-AR.pdf`) as its own register, and names the Arabic annual report as existing-and-unread. A snapshot risk accepted on the English pair's URLs is not accepted on the Arabic pair's. The publish gate's accepted-risk row names all four PDFs.
- **Hand-off line 7 stands and is right.** The Arabic edition of the Annual Report 2025 is served (12,967,817 bytes) and **carries zero `/ToUnicode` CMaps** — 14,497 text-showing strings mapping to nothing any client here can read. Under **#131** a rendering nobody has read is not evidence, so the Gold Seals pair stays attributed to the English edition it was read in, with the Arabic URL carried beside it as existing-and-unread. *This falsifies the 11-06 recon's own instruction that sources 3 and 4 would both be cited in Arabic — an instruction written before anybody opened the file.* The gate endorses the falsification.
- **Hand-off line 8 stands.** No Arabic verbatim quotation is taken from any PDF extraction (#129): both Arabic PDFs yield text in visual order, reversing is *our* normalisation, and a reconstructed string is not the register's bytes (#112). The Arabic edition therefore **describes** those documents and quotes neither. The one quotation it does carry is from our own HTML, in logical order — and §5 checked it.
- **The standing prohibitions hold.** No school named by its grade; no causal claim about C4, the pandemic or the 2024 framework; no improvement claim (3.5% → 16.5% is written nowhere as improvement — *improvement never without its floor*); the batch shape and the cycle shape never set side by side (Editor disposition 3).

---

## Verdict

**PASS.** The Arabic composition is composed, not translated, and §2 settles that arithmetically for the
first time. Three corrections were binding and all three are executed today: the `edition:` field struck
in both editions, the English annotation brought up to the Arabic's completeness by Editor disposition 4,
and the self-citation's byte length struck from the Arabic.

**Gate 4 of 8 is CLOSED.** Open cells: **the hero still and og card, and the flag.** Neither has a
dependency in front of it now.

— Arabic Editor · 2026-11-09 · *the gate I was hired for had nothing to transliterate, and the evidence
that this was composed rather than translated turned out to be twenty-three numbers the English edition
never printed.*
