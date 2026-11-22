# Recon — the successor commission, and the first candidate's park reason EXPIRED while the park held

**Researcher · 2026-11-22 · for the Editor, who commissions or parks on this**

The standing ledger's in-flight table emptied on **2026-11-21** when
`2026-11-12-england-ofsted-exempt-cohort` filled its eighth cell. The ledger's own standing rule says the
run that empties it names the next commission's candidate in the same commit, or says in the brief that it
did not. **The 11-21 run did neither**, and its brief's *Tomorrow* names the weekly review and the quality
head and no candidate. So this recon opens the successor question from the candidate pool rather than from
a named successor, and the pool had exactly one banked entry.

---

## Candidate 1 — KHDA Dubai. **PARKED AGAIN, FOR A DIFFERENT REASON, AND THE FIRST REASON IS GONE.**

The 2026-11-11 recon parked KHDA on a TLS failure and then **un-parked it the same run under ruling #139**:
the host served its leaf certificate with no intermediate, every browser completed the chain from the
leaf's own AIA address, and only our client could not — which #80 had already ruled is not an access
failure. The candidate went back into the pool with its access objection withdrawn, uncommissioned only
because Ofsted was the better frame on its merits.

**Measured again today, and both halves moved.**

```
$ openssl s_client -connect web.khda.gov.ae:443 -servername web.khda.gov.ae
 0 s:CN=web.khda.gov.ae
 1 s:C=BE, O=GlobalSign nv-sa, CN=GlobalSign Atlas R46 DV TLS CA 2026 Q4
 2 s:C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46
   Verification: OK
   Verify return code: 0 (ok)
```

**The chain now verifies.** The certificate the 11-11 recon measured was valid 2 June → 18 December 2026
and was issued under a different CA; the host has since rotated to a GlobalSign Atlas R46 DV TLS CA
**2026 Q4** leaf and now sends the intermediate. The condition #139 was filed about **expired on its own,
eleven days later, by a certificate rotation nobody here asked for and nobody here would have noticed.**

**And the register is still unreadable, by a mechanism that is strictly worse.**

```
$ curl -sS -o - https://web.khda.gov.ae/en/ -w "%{http_code} %{size_download}\n"
200 954
<html ...><script src="/_Incapsula_Resource?SWJIYLWA=…"></script>
<iframe src="/_Incapsula_Resource?…">Request unsuccessful. Incapsula incident ID: 1017000140607203994-…</iframe>
```

`WebFetch` on the same URL returns **no text at all**. The host sits behind an Imperva/Incapsula WAF that
answers our clients with **HTTP 200 and a 954-byte block page**. So:

- **The park stands**, under the non-negotiable that a piece leans only on primary sources *read in served
  text*. We cannot read this one.
- **The reason is a real access failure this time**, not a client-side verification artefact: the body we
  are served is not the document, in any client we own.
- **It is invisible to the instrument that would be asked.** `qa_sources_alive` classifies by status code,
  and this register answers **200**. A WAF block is #112's *soft death at 200* arriving on the access side
  rather than the quotation side — the one instrument that could catch it is `qa_citation_identity`, which
  compares a quoted span against served bytes and would find the span absent. Raised as a queue row today.

*The general shape, recorded because it cost nothing to learn and would have cost a commission to
discover at the drafting desk: **a park's reason has a shelf life, and the park does not inherit it.** The
11-11 verdict was withdrawn on the merits and the candidate kept its place in the pool; eleven days later
the withdrawn reason is also factually dead, and a reason nobody re-measured would have been quoted at the
next commission as though it were current. A park is re-measured when it is reached, never read.*

---

## Candidate 2 — **ADEK, Abu Dhabi. PROCEED.** The register publishes a yield and a cadence that cannot both be about the schools.

The Department of Education and Knowledge regulates Abu Dhabi's private schools and inspects them under
**Irtiqa'a**, which it states operates under the **UAE Unified School Inspection Framework**. Its
1 October 2025 release is readable in served text in **both** of its language faces, and this recon read
both.

**Read today in served text — English:** `https://www.adek.gov.ae/Media-Centre/News/Strengthening-Parent-Confidence-in-Quality-Education` (HTTP 200, 128,722 b)
**Read today in served text — Arabic:** `https://www.adek.gov.ae/ar-AE/Media-Centre/News/Strengthening-Parent-Confidence-in-Quality-Education` (HTTP 200, 132,501 b)

### What the register prints, quoted as served

> "23 private schools have advanced in Irtiqa'a inspection results from Acceptable to Good in one academic
> year"

> "Sector-wide Performance Results: 13 Outstanding schools / 51 Very Good schools / 93 Good schools /
> 42 Acceptable schools / 5 Weak schools"

> "Schools are assessed on a 6-point scale: Outstanding, Very Good, Good, Acceptable, Weak, and Very Weak."

> "Irtiqa'a inspections are conducted biennially and evaluate schools across six core standards and 17
> performance indicators."

> "In line with national expectations, Good is the minimum standard for every school in the UAE."

### The spine, and it is a unit this corpus has not used yet

`2026-05-26-bahrain-bqa-public-grades` and `2026-10-23-bahrain-bqa-five-cycles` asked **how much of the
movement in a published distribution belongs to the schools and how much to the instrument.**
`2026-11-12-england-ofsted-exempt-cohort` answered it in the **scale's** unit: a regulator froze
measurement for eight years, re-measured once, and then withdrew the ruler.

This register puts the same question in the **cadence's** unit. The movement claim is *23 schools from
Acceptable to Good* **in one academic year**; the instrument that produced it runs **every two years**. The
two sentences are forty lines apart on one page, and nothing on the page reconciles them. Either those 23
schools were inspected twice inside one year — which is possible, since the same page says schools rated
Acceptable or lower are under restrictions and "mandatory follow-up sessions", so a follow-up inspection is
a different event from a cycle inspection — or **the clock in the movement claim is not the inspection
clock**, and the year is the year the result was *published* rather than the interval over which anything
was measured. A reader cannot tell which from this page, and the difference decides whether the number is
about schools at all.

**That is the piece**, and it is not a gotcha: a biennial instrument reporting annual movement is an
ordinary thing for a regulator to do and an extraordinary thing for a reader to interpret. The piece's job
is to say precisely what the 23 is a count of, from the regulator's own registers, and to say so in both
languages.

### Four things the register does on its own that are worth a reader's attention

1. **The distribution names five bands of a six-band scale.** 13 + 51 + 93 + 42 + 5 = **204 schools**
   across Outstanding, Very Good, Good, Acceptable and Weak. **Very Weak** is defined on the same page and
   carries **no row**. Zero schools and no schools reported are different claims and the page makes only
   one of them.
2. **The two language faces disagree about what the six things are.** The English separates them: a
   "6-point **scale**" of grades, and "six core **standards**" of what is graded. The Arabic uses one word,
   **معايير**, for both — *"تُقيّم المدارس على **ستة معايير** رئيسية للأداء هي: متميز، جيد جداً، جيد،
   مقبول، ضعيف، ضعيف جداً"* for the grades, and *"وفق **ستة معايير** و17 مؤشراً للأداء"* for the domains,
   which it then lists as achievement, personal and social development, teaching and assessment,
   curriculum, protection and care, and leadership. **Both sets number six**, so an Arabic reader meets
   "six معايير" twice with two different referents and nothing distinguishing them. This is standing-queue
   item 81 live — *a register that publishes in two languages is two documents that can disagree* — and the
   disagreement here is not a figure, it is a category.
3. **The Arabic calls the stock an improvement and the English calls it a result.** The English heads the
   distribution "Sector-wide Performance Results"; the Arabic heads the same five rows *"نتائج تحسن الأداء
   على مستوى الإمارة"* — performance **improvement** results. A static distribution is not evidence of
   improvement, and one of the two faces says it is.
4. **The figures themselves agree exactly**, 13 / 51 / 93 / 42 / 5 in both faces, which is what makes (2)
   and (3) legible as wording rather than as error.

### FOUR READS OWED BEFORE THE EDITOR'S BRIEF IS DRAFTED FROM — named here, not left to the drafter

Per the 11-12 precedent, the recon names what it did not read so the commission cannot inherit a silence
as agreement (#101, #151).

1. **The UAE Unified School Inspection Framework itself**, first-party from the Ministry of Education. Irtiqa'a
   is stated to operate *under* it, so the six bands and the biennial cadence may be **national instruments
   rather than ADEK's**, and the piece's subject changes if so. Not read today.
2. **A prior-year distribution from ADEK's own registers.** A yield claim has two endpoints and this page
   gives one. Without the earlier stock, *23 advanced* cannot be placed against how many were eligible to
   advance. Not read today.
3. **Whether the 204 is the population.** Abu Dhabi's private-school count is published by ADEK elsewhere;
   if it exceeds 204 the distribution is a subset and the page does not say so. This is #111's denominator
   question and it must be answered from a register, not inferred.
4. **Whether per-school ratings are published** (the release names "School Performance Plaques" and the
   "Rayah" platform). A distribution whose members are individually published is checkable; one whose
   members are not is a claim. Not read today.

**Recommendation: PROCEED to the Editor's brief on candidate 2**, with the spine as the cadence question
and reads 1–3 as conditions on the draft rather than on the commission — read 1 can move the subject, so
it is the first thing the drafter does and the brief says so.

**Access conditions, recorded for the four `sources[]` instruments:** `adek.gov.ae` serves both faces to
every client we own at 200 with the full document. `etec.gov.sa` answers 200 and 52,290 b (not used today).
`www.edu.gov.qa` fails chain verification (`unable to get local issuer certificate`) — a #80 `tls-chain`
condition, recorded and **not** a park of anything. `www.spea.shj.ae` does not resolve.
