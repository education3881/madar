# Verifier verdict — Netherlands: "The test that grades the advice"

**Date:** 2026-07-27 · **Stage:** independent post-draft audit (drafter ≠ verifier) for the Edition-04 wave.
**Slug:** `2026-07-07-netherlands-doorstroomtoets` · **Drafter:** Content Creator II · **Editor five-test:** APPROVE-for-the-wave on file (`content-drafts/verdicts/2026-07-22-netherlands-doorstroomtoets.md`).
**Recovery-run note:** this verdict is the first run after a 4-day dark gap (2026-07-23 → 26). The gap re-triggered a live re-fetch of every load-bearing primary before clearing — recovery-rule discipline, not a re-run of the Editor's compose-time check.

## VERDICT: **CLEARED** — held `approved: false` (Ed04 ships only as a complete gated wave).

Every load-bearing figure re-fetched **live this run** and traced verbatim against the two primaries. No item failed; one figure (the revision-rate series) correctly stays in qualitative form because its exact 2026 value is not reachable in a citable primary — the draft already carries it that way with the denominator stated. Netherlands enters the verified column. **Ed04 = 7 drafted / 7 verified** (drafted-slate verification complete again, bench draft 1 included).

## Trace list — resolved against the live primaries

**Primary A — Inspectie van het Onderwijs, De Staat van het Onderwijs 2026 speech** (onderwijsinspectie.nl; re-fetched 2026-07-27, read as text; page date metadata `2026-04`):
- "In het Utrechtse **IJsselstein** wordt in **acht van de tien** gevallen het schooladvies bijgesteld als de doorstroomtoets een hoger advies laat zien." → draft "eight of ten." **✓ verbatim.**
- "in **Stadskanaal** gebeurt dat in **vier van de tien** gevallen." → draft "four of ten." **✓ verbatim.**
- "...terwijl bijstellen in zulke situaties wettelijk verplicht is, **tenzij dat niet in het belang van de leerling is**." → draft's "unless it is not in the pupil's interest." **✓ verbatim.**
- "Dat roept de vraag op **waarom het in de ene regio zo anders uitpakt dan in de andere**." → draft's "why it plays out so differently in one region than in another." **✓ verbatim.**
- "Wij zien **zowel over- als onderadvisering**." → draft's "both over- and under-advising survive." **✓ verbatim.**
- Speaker attribution on page: "**inspecteur-generaal van het Onderwijs, Alida Oppers**." → draft's "Inspector-General Alida Oppers." **✓.** Date: article body says "15 April 2026"; the live page carries `2026-04` metadata and the De Staat van het Onderwijs 2026 congress attribution (day-precision confirmed by the Editor at compose 07-22 on the page metadata; not re-derivable from the parsed body this run — carried as **confirmed-at-compose + month corroborated live**, not load-bearing beyond attribution).

**Primary B — PO-Raad, "Rapportage doorstroomtoets 2026: verschillen tussen kansen en toetsen blijven," 23 June 2026** (poraad.nl; re-fetched 2026-07-27, full body read):
- Eligibility spread: "Er zijn bijvoorbeeld gemeenten waar **nog geen één op de tien** leerlingen in aanmerking komt voor bijstelling, terwijl er ook gemeenten zijn waar **meer dan de helft** in aanmerking komt." → draft's "from under one in ten to more than half per municipality." **✓ verbatim.**
- Geography of the top: "...het aandeel leerlingen dat in aanmerking komt voor een bijstelling het hoogst op **Schiermonnikoog, Ameland en Vlieland, waar geen middelbare scholen zijn met een havo-, havo/vwo- of vwo-bovenbouw**." → draft names all three islands + "where no havo/vwo upper school exists locally." **✓ verbatim.**
- Dries quote: "**Jouw achtergrond mag niet bepalen of je toetsadvies wordt bijgesteld of niet.**" → draft's "Your background must not determine whether your test advice gets revised or not." **✓ verbatim, faithful translation.**
- Provider divergence: "...het behalen van vergelijkbare referentieniveaus in de praktijk **nog altijd kan betekenen dat er verschillende toetsadviezen worden gegeven**" — largest providers **IEP** and **LiB**. → draft's "two children with equivalent mastery ... can receive different track advices depending on which test their school happened to buy." **✓.**
- Cabinet plan + motion: "Het plan is vooralsnog om pas in **2029 of 2030** naar één doorstroomtoets over te stappen" + "de motie van **D66, SP, GroenLinks-PvdA, DENK en JA21** ... om al in **2027** naar één aanbieder ... te gaan." → draft's "2029 or 2030 ... a parliamentary motion pressing for one provider as early as 2027." **✓ verbatim; party list matches the frontmatter source note.**

## The one figure held qualitative — trace-list item 1 (revision-rate series)
The draft states "roughly one in ten [pre-reform] → around a quarter [since 2024], and it has stayed near that level," **denominator stated in the sentence** ("share of all advices revised"). Live check: the PO-Raad news primary confirms the *direction* verbatim — "Sindsdien stellen scholen **veel vaker** adviezen bij" (schools revise much more often since 2024) — but gives **no exact 2026 percentage**. The exact figure lives only in the themarapportage dashboard (`sectorrapportage.poraad.nl/p/Doorstroomtoets`), which **redirect-cancelled on fetch** — an *observation, not a verdict* (ruling #20): a JS dashboard, not a citable text primary. **Decision:** keep the qualitative form exactly as drafted. The recon's flagged 22.5% stays uncommitted. This is the correct, conservative call and matches the Editor's own trace-list instruction (item 1: "either bank the number or keep the qualitative form").

## Ruling #25 discipline — conditional vs eligibility rate (item 2): **held, confirmed**
The two rate types stay apart in-sentence, and the live source vindicates the distinction:
- **Conditional (given the test shows higher):** the 8/10-vs-4/10 town figures. The draft frames the schoolweging finding as a **conversion-given-qualification** rate — "the schools with the fewest disadvantaged pupils convert a qualifying test result into an actual upgrade most reliably of all." The source supports this exactly: "als leerlingen van scholen met een **lage schoolweging** in aanmerking komen voor bijstelling, hun advies **vaker wordt bijgesteld** dan bij leerlingen op scholen met een hogere schoolweging." **✓.**
- **Eligibility (qualifies for revision):** the <1-in-10-to->half municipal spread. Kept distinct. **✓.**
- **One honest nuance for the record:** the source also reports that **high-schoolweging (disadvantaged) schools revise more often than *average*-weging schools** in raw terms — a countervailing fact the draft omits. This does **not** falsify the draft: the draft's specific claim is the *conversion-given-qualification* rate (lowest-weging highest), which the source states directly, and the draft never claims disadvantaged schools revise less in absolute terms. The framing is defensible as written; flagged so the weekly can decide whether one clause acknowledging the two-part finding would strengthen it. **Not a hold.**

## Items 3–5
- **Item 3 (scale decimals ~164,000 / LiB / IEP):** draft uses "**about** 164,000 pupils across six approved tests, the two largest being LiB and IEP" — hedged as scale, not headline; provider raw scores **never juxtaposed** (draft explicitly: "a LiB score and an IEP score are not the same kind of number and cannot be compared directly"). Non-comparability of scales corroborated on Primary B. Exact 164,000 not re-traced on OCW-in-cijfers this run; carried as "about," so the hedge covers it. **✓ (scale, hedged).**
- **Item 4 (negative/absence claim):** none load-bearing; draft imports no norming-error claim. Absence held. **✓.**
- **Item 5 (background gradient — higher-educated/-income parents get vwo/havo more often):** used as one clause of context; consistent with the whole kansengelijkheid premise of Primary B (the reform exists to counter background-linked under-advising). Long-documented CBS/OCW direction; not re-derived live this run, but non-load-bearing and directionally confirmed by the source's framing. **✓ (context clause).**

## Flag state (ruling #18)
`approved: false` confirmed on disk (`web/src/content/articles/2026-07-07-netherlands-doorstroomtoets.md`). No AR yet (joins the Ed04 AR batch). `related:` → us-naep (resolves the forward ref), singapore-psle (in-wave), oman (live). No orphan. Piece stays held; the verdict gates the *future* flip, it does not flip anything today.

— Verifier · 2026-07-27
