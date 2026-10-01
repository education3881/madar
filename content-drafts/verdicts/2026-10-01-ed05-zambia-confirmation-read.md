# Confirmation read — Edition 05, row 1 (Zambia) — **CLOSED, with two defects fixed in-run in both languages**

**Date:** 2026-10-01 (Thursday, Asia/Dubai) · **Desk:** Verifier · **Piece:**
`2026-08-25-zambia-free-education-act` — *The law that moved the finish line* / «القانونُ الذي أزاح خطَّ النهاية»
**Prior gates:** Editor pair verdict 08-27 PASS · Verifier verdict 09-08 FAIL-1 → fixed in-run
**Status after this read:** the three items the ledger owed are **closed**; two new defects were found
and closed in both languages; the pair stays `approved: false` with the wave.

**Why this read happened today:** it is the oldest item on the board. The 2026-09-30 QA log named the
surface — *an annotation is the only prose in this publication that no instrument reads* — and the
ledger has owed confirmation reads on five pairs since 09-08. This is the first of the five.

---

## The three items the ledger owed

### Item A — the four `parliament.gov.zm` URLs. **CLOSED, and all three previous readings were wrong.**

Re-probed 2026-10-01, every step measured rather than inferred.

| source | URL | verify ON | verify OFF | bytes |
|---|---|---|---|---|
| 1 | the Bill, N.A.B. 6 of 2026 (PDF) | fails | **200** | 304,258 |
| 2 | the Bill page, node/12930 | fails | **200** | 30,833 |
| 3 | the Committee report, node/12505 | fails | **200** | 31,709 |
| 4 | the Ministerial Statement (PDF) | fails | **200** | 55,842 |

The failure is `unable to get local issuer certificate` — openssl verify code **20/21** — and **not**
`certificate has expired`. The host sends **exactly one certificate**; that certificate is valid
**26 May 2026 → 10 December 2026**, CN `*.parliament.gov.zm`, issuer *RapidSSL TLS RSA CA G1*; and the
leaf's own Authority Information Access extension prints where its issuer lives. Fetch that and the
chain closes — `openssl verify -untrusted <issuer> <leaf>` → **OK**, and a Python client with the same
intermediate loaded gets **HTTP 200 with validation enabled**.

**So the document is fine, the certificate is fine, and the reader is fine.** What is broken is the
host's chain configuration, and the clients that fail on it are ours, not a reader's.

This operation had recorded this host three times and had it wrong three times: *unreachable* (09-10),
*connection refused at :443* (09-16), *invalid certificate, document still served* (09-30). **Filed as
ruling #80** — a serving state is observed by a client, and the client is part of the observation.
`qa_sources_alive`'s `tls` bucket is now split, and its old advice (*a reader meets a browser
interstitial either way, so say so*) has been deleted, because taking it would have put a false
sentence about the reader into **twelve** annotations across this pair.

**Disposition:** all four annotations carry the measurement as a dated observation in both languages,
including the sentence that the two earlier readings did not survive checking. No figure moved; no
body prose moved.

### Item B — the K15m saving / price fix, as served. **CLOSED, annotation confirmed exactly right.**

ZANIS, re-read in served text 2026-10-01 (HTTP 200, 100,401 bytes). The register's own sentence:

> "ECZ has developed a new in-house results processing system at a cost of 4.7 Million Kwacha, **a move
> that has saved Government about 15 Million Kwacha** that would have been spent on procuring an
> external system."

The annotation already said *the 15 million is stated by the source as a saving, not as the external
price*, and the body says *"a move its Executive Director **says** saved the government about
K15 million"* — attribution verb carried, hedge carried, no composite. **Nothing to fix.**

**Examined and allowed, with the reason recorded rather than left silent:** the body writes *"It counts
**full** School Certificates"* where the register writes *"obtained Grade 12 School Certificates"*, the
contrast class being *"received statements of results"*. **full** is the piece's own word. It is kept
because the sentence's whole job is to state the pass rate's scope and the register's own contrast is
what it is stating — not because nobody noticed. The Arabic carries «كاملةً» in the same place, so the
pair is symmetric.

### Item C — the IICBA attribution note. **OPEN → two defects, both closed in-run.**

The brief re-read in served text 2026-10-01 (HTTP 200, 77,238 bytes — **on the second and third
requests; the first returned HTTP 500 twelve seconds earlier**, recorded because one probe is not a
measurement).

**DEFECT 1 — an attribution upgrade, #43's verb hierarchy applied to our own sentence.**

The register says:

> "Learning poverty … **is estimated by the World Bank, UNESCO, and other organizations** at 99 percent"

The piece said:

> "UNESCO's institute for capacity building in Africa **puts** Zambian learning poverty at 99 per cent."

*Puts* asserts authorship. IICBA is the **channel** for that figure, not its estimator, and this
publication's own rule is that a figure is cited as read. Worse, the **same annotation already did this
correctly for four other figures** in the same parenthesis — *"Grade 7 completion 97% … as reported from
the 2020 Education Statistics Bulletin"* — so the discipline was applied to four numbers and not to the
fifth, inside one pair of brackets. That is the 2026-09-30 forward question answered with an instance:
nobody re-reads an annotation once it is written.

**Fixed, both languages:**
EN — *"UNESCO's institute for capacity building in Africa **reports** Zambian learning poverty at 99 per
cent, an estimate its brief attributes to the World Bank, UNESCO and others, not to itself."*
AR — «يُفيد معهدُ اليونسكو لبناء القدرات في أفريقيا بفقرِ التعلُّم الزامبيِّ عند 99 في المئة، وهو تقديرٌ
يَعزوه موجزُه إلى البنك الدولي واليونسكو وجهاتٍ أخرى، لا إلى نفسه.»
*and others* carries the register's own *and other organizations*; the hedge is not narrowed.

**DEFECT 2 — a figure printed without its scale.**

The register prints the Human Capital Index learning component as *"358 **on a scale where 625
represents advanced attainment and 300 the lowest attainment**"*. Both bodies printed **358** bare. A
number on a scale, without its scale, in a publication whose standing prohibition is *no "best" without
its ruler in the same sentence* — #29's shape, arriving by a component of an index rather than by a
superlative. A reader cannot tell whether 358 is close to the floor without the floor.

**Fixed, both languages:** EN *"a harmonised learning outcome of 358 **on a 300-to-625 scale**"*; AR
«ناتج تعلُّمٍ مُنسَّقٍ قدرُه 358 **على سلَّمٍ من 300 إلى 625**».

---

## Caps, and the arithmetic of the fix

The two edits cost words. Measured after each, by the canonical ruler (whitespace split, `##` markers
excluded — the same ruler that reads Rwanda at 2,299):

| state | EN body |
|---|---|
| at open | **2,279** / ≤2,300 |
| after both edits, first draft | **2,303** — three over, **no waiver sought** |
| after giving three back in the same paragraph | **2,298** / ≤2,300 |

The three words came out of the same sentences that spent them: *carries* → *reports* (which also
removed a repetition with *The same brief carries* two sentences later), *rather than to itself* → *not
to itself*, and *on a scale running from 300 to 625* → *on a 300-to-625 scale*. **Two words in hand.**

AR body 1,840 → **1,859**; no cap pressure.

**Numeral symmetry checked by multiset against the pre-edit files:** both bodies gained exactly `300`
and `625` and lost nothing. The edits are symmetric by measurement, not by intention.

---

## What this read did NOT do, named rather than skipped

* **It did not re-read the other six annotations' every claim.** This read was scoped to the three
  owed items and to what the new instrument surfaced. The 09-30 forward question's sharper half —
  *when a verdict corrects one clause of an annotation, is the rest of that annotation re-read?* — is
  still answered **no** by this run's behaviour, and that is recorded as a fact about the run, not
  argued away.
* **Four of this pair's registers still fail a scripted probe** and will keep doing so until
  `parliament.gov.zm` fixes its chain. That is now a *named* state with a measured consequence of
  *none for the reader*, rather than an open worry.

## Owed next

The confirmation reads on **Sierra Leone, Sudan, slot 3 and Egypt** — four of five remaining. Sudan's
is the largest (four registers riding on one channel). Egypt's carries one open verification item
(source 1 unreachable).
