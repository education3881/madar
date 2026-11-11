# Recon — the Bahrain successor question, and the register that can actually settle it

**Researcher · 2026-11-11 · for the Editor, who commissions or parks on this**

The standing ledger's in-flight table emptied on 2026-11-09 when `bahrain-bqa-five-cycles` shipped, and
the ledger's own standing rule says the run that empties it names the next commission's candidate. The
2026-11-10 run named the *question* and recorded that it had no recon on it. This is that recon.

## The question, taken from the piece that closed on it

The Bahrain single ends on a sharpened version of its predecessor's question, and it ends by saying its
own register cannot answer it:

> **how much of the movement in a published distribution belongs to the schools, and how much to the
> instrument** — which no amount of the Authority's admirable openness can settle, because the register
> that would settle it is one nobody publishes anywhere.

That last clause is a claim about the world, and it is the thing recon exists to test. **It is wrong, and
it is wrong in a useful way:** one regulator does publish the register, because one regulator ran the
natural experiment on itself and then printed both sides of it.

## Candidate 1 — KHDA Dubai. ~~PARKED~~ **UN-PARKED the same run — the park was WRONG (ruling #139).**

> **Correction, 2026-11-11, by the research function two hours after this section was written.** The park below is withdrawn. The failure it rests on is a **`tls-chain`** failure, which this operation ruled on **2026-10-01 (#80)** and which is **not an access failure**: the host sends only its leaf certificate and publishes the intermediate at the CA Issuers address printed inside that leaf, so Chrome, Edge and Safari complete the chain and show the reader nothing, while Python, curl and openssl do not. Tested the way #80 tested `parliament.gov.zm`: the leaf's AIA names `http://secure.globalsign.com/cacert/gsrsaovsslca2018.crt`, and `openssl verify -untrusted inter.pem leaf.pem` returns **`leaf.pem: OK`**. The certificate is valid **2 June 2026 → 18 December 2026**. **The register is served, the certificate is sound, and every reader we have can read it — only our client could not.** This section even wrote the browser half down and parked the candidate anyway, because the bucket that holds the distinction fires on URLs already cited and park-or-proceed is decided here, before anything is cited. Ruling **#139**. KHDA returns to the candidate pool with its access objection withdrawn; it is still not commissioned, because Ofsted is the better frame on its merits and not because KHDA was unreadable. The measurement below stands as a measurement and is **struck as a verdict**.

### The original section follows, unaltered, because a withdrawn verdict is kept visible as one.

The obvious successor on shape: Dubai's Knowledge and Human Development Authority has published per-school
inspection ratings since 2008-09, changed its framework in 2015-16, and re-inspects the same schools year
on year — the same four-grade archive shape as Bahrain's BQA, in the same region, with an Arabic face.

**It is parked because we cannot read it in served text.** Measured today, not inferred:

```
$ openssl s_client -connect web.khda.gov.ae:443 -servername web.khda.gov.ae -showcerts
 0 s:C=AE, ST=Dubai, L=Dubai, O=Knowledge and Human Development Authority, CN=*.khda.gov.ae
   Verification error: unable to verify the first certificate
   Verify return code: 21
```

The server sends **the leaf certificate and nothing else** — no intermediate, so the chain cannot be
built by any client that verifies one. `https://www.khda.gov.ae/en/` returns **302** to that same host, so
there is no verifying route in. `WebFetch` returned `unable to verify the first certificate`; `curl`
returned exit 60.

**This is not a dead register and it is not a refusal.** A browser renders it fine, because browsers chase
the issuer named in the leaf's AIA extension or hold the intermediate in cache from another site. Every
instrument this operation owns verifies the chain and gets nothing. So KHDA is a register that is **served
to readers and unverifiable to us** — and under this publication's own non-negotiable (*named primary
sources read in served text*) a piece cannot lean on it. Handed to the Assertions Engineer as a queue row,
because all four of our `sources[]` instruments would score this register as dead or refusing, which is a
different fact about the world than the one that is true.

## Candidate 2 — Ofsted, England. PROCEED, and the register prints both sides.

Between **May 2012 and November 2020** the English government exempted outstanding primary and secondary
schools from routine inspection. In **November 2020** it lifted the exemption, and Ofsted then went back
and graded the schools whose grade had been frozen for up to eight years. The regulator published the
yield against the stock in the same document.

Read in served text today from Ofsted's own official statistics, *State-funded schools inspections and
outcomes as at 31 August 2022*, main findings (gov.uk), quoted as printed:

- **The stock:** *"Eighty-eight per cent of all schools are good or outstanding."* The same release's
  Figure 1 table gives, as at 31 August 2022, 21,725 schools at **18% outstanding, 70% good, 9% requires
  improvement, 3% inadequate**, and records that the 88% *"has increased from 86% in August 2021, and had
  been stable at 86% since 2019."*
- **The yield:** *"Only 17% of previously exempt schools that had a graded inspection this year remained
  outstanding."* And: *"Of these, 17% retained their outstanding grade, while 21% were judged requires
  improvement or inadequate. The remainder were judged to be good."*
- **Split by phase:** *"Fourteen per cent of previously exempt primary schools inspected this year remained
  outstanding"*, *"compared with 25% of secondary schools."* Figure 3's table: primary **263 schools**, 14%
  outstanding / 65% good / 18% RI / 3% inadequate; secondary **104 schools**, 25% / 54% / 14% / 7%.
- **The exemption, dated in the register's own words:** *"Between May 2012 and November 2020, outstanding
  primary and secondary schools were exempt from routine inspection."* *"In November 2020, the government
  lifted its exemption."*
- **And the register says the stock is stale, in its own numbers:** *"Sixty-four per cent of all schools
  have not had a graded inspection in the last five academic years."*
- **The frameworks are dated too:** *"We carried out inspections between September 2015 and August 2019
  under the common inspection framework."* *"Since September 2019, we have carried out inspections under
  the education inspection framework."* Figure 1's note: *"Dotted lines on the chart indicate a change to
  the inspection framework"* — *"in January and September 2012, September 2015 and September 2019."*

**Why this settles the Bahrain question where Bahrain's own archive could not.** Bahrain publishes verdicts
and dates and nothing else, so cycle four's 40.6% cannot be decomposed. Ofsted published a cohort whose
grade was held constant by **rule** rather than by performance, then measured it with the current
instrument: 18% of the stock is outstanding, and **17% of the frozen cohort survived contact with a
re-inspection**. The decomposition is the regulator's own arithmetic, not ours.

**What the register does NOT say, recorded now so no draft invents it (#49, #117):** the page does not
state that the current stock of grades reflects inspections from different periods — that is implied by
the 64% sentence and by the framework notes, and **it is implied, not printed**. It does not compare
outcomes across frameworks; the framework changes appear **only in chart notes**. And Figure 7's note
says *"We have not compared the data with the 2020/21 academic year"* because *"we only carried out a
small number of inspections during this year."* A piece may not do a comparison the register declines to
do and attribute it to the register.

## What the Editor still needs before a brief can go to a drafter

1. **The current release.** The 31 August 2022 release is the clearest statement of the exemption yield,
   and it is **four years old**. The piece is read in the reader's present (#117), so the newest
   `state-funded-schools-inspections-and-outcomes` release must be read and the stock figure taken from
   there, with the 2022 release cited for the exemption cohort and labelled by its own date.
2. **The September 2024 change.** Ofsted stopped awarding single-word overall judgements for state schools
   from September 2024. That is a second, later instrument change on the same register, and it bears
   directly on the frame: the thing being measured changed again. Must be read first-party, not from a
   news summary.
3. **No MENA anchor yet.** This publication's centre of gravity is MENA and this candidate is England.
   Bahrain's BQA archive is the natural comparison partner and is already read and published, so the piece
   has its anchor **inside our own corpus** — which is the first time a single can lean on a predecessor
   that way. The Editor decides whether that is sufficient or whether a Gulf register must carry it.

## Park-or-proceed

**PROCEED on candidate 2, with the three reads above owed before drafting.** **PARK candidate 1** on
register-access grounds, with the measurement on file, and keep it parked until the chain is fixed by
somebody at KHDA — which is not a thing this operation can cause.

**No figure in this recon may reach a draft without being re-read at compose time with the register open
(#41, 2026-09-13).** Everything above is quoted from one served document and is the recon's evidence, not
the piece's.
