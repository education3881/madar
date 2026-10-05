# Ruling #80 — a serving state is observed by a client, and the client is part of the observation; and a check's remediation advice is a claim that ships into prose

**Filed:** 2026-10-01, by the Verifier's confirmation read on Edition 05 row 1 (Zambia), with the fix
landing in the Assertions Engineer's lane the same run.
**Artefact:** `agents/tools/qa_sources_alive.py` — its `tls` bucket split into `tls` and `tls-chain`,
and the advice attached to the old bucket deleted because it was measured false.
**Family:** assertion discipline (nineteen of eighty-two), reaching into the register-hierarchy family
through #76.
**Cousins:** #76 (*a serving state is an observation with a date, not a fact about a host*), #70 (*a
check's bucket set is an enumeration too, and cannot report a distinction it cannot hold*), #65 (*an
assertion has two outputs — the verdict the build gates on and the record later runs read as true*),
#41 (cite as read), #20 (one slow read is not a death).

---

## The ruling, in two halves

**First half, which extends #76 by one clause.** #76 says a serving state is an observation with a
**date**. It is also an observation by a **client**, with that client's trust configuration, at a
moment. *Unreachable*, *refused*, *invalid certificate* are verdicts a particular program reached;
they are not properties of a host, and the gap between them and what a reader meets can be total.
**So a serving state is cited as read, like a figure: by a named client, with its configuration
stated, on a date.**

**Second half, and it is the half that nearly shipped a false sentence.** An assertion has a third
output beside the two #65 named. Not only the verdict the build gates on and the record later runs
read as true, but **the instruction a later run follows** — and that instruction is a claim, written
in advance, about a situation its author was imagining. Ours told the operation what the reader would
see. It was wrong, and it was wrong in the one place where being wrong costs a citation: the sweep's
finding is designed to be copied into an annotation.

---

## The case

The held Zambia pair cites four documents on `parliament.gov.zm`. This operation has recorded that
host three times in twenty-one days, each time in its own vocabulary, and **each time wrongly**:

| when | what we wrote | what was true |
|---|---|---|
| 2026-09-10 | `unreachable` (4 URLs, one host) | not established either way; the sweep had one failure mode and used it |
| 2026-09-16 | *"connection refused at :443, not 404, not a timeout"* — re-probed from a second client, #20 satisfied | plausibly true that day; the host's state is not ours to know |
| 2026-09-30 | `tls` — *"invalid cert, document still served 200"*, with the standing advice *a reader meets a browser interstitial either way, so say so* | **the certificate was valid** |

Measured on 2026-10-01, in this order, with every step recorded rather than inferred:

1. All four URLs return **HTTP 200** with validation disabled — 304,258 / 30,833 / 31,709 / 55,842
   bytes — and fail with validation enabled. So the document is not the question.
2. The failure is `unable to get local issuer certificate`, openssl verify code **20/21**, not
   `certificate has expired`. Those are different strings and we had been reading them as one.
3. The host sends **exactly one certificate** — the leaf, no intermediate.
4. The leaf is **valid 26 May 2026 → 10 December 2026**, CN `*.parliament.gov.zm`, issuer *RapidSSL
   TLS RSA CA G1*. Nothing is expired.
5. The leaf's own **Authority Information Access** extension prints where the issuer lives:
   `http://cacerts.rapidssl.com/RapidSSLTLSRSACAG1.crt`.
6. Fetch that and the chain closes: `openssl verify -untrusted <issuer> <leaf>` → **OK**, and Python
   with the same intermediate loaded returns **HTTP 200 with validation enabled**.

**So the host is misconfigured and the reader is fine.** Chrome, Edge and Safari follow the AIA
address or already hold the intermediate; Python, `curl` and `openssl s_client` do not. The sweep was
failing where a reader succeeds, and then telling us to write that the reader meets an interstitial.

Had the confirmation read taken the advice, twelve annotations across the Zambia pair — six per
language, the same count as the Rwanda pair on 09-29 — would have asserted a security interstitial
no reader meets, in a publication whose first rule is that a claim is cited as read. **Rwanda's
interstitial clause was right** (that certificate had genuinely expired, and the renewal was verified
on 09-29). The clause is only right when the certificate is actually bad, and nothing in the sweep's
output distinguished the two cases until today.

### A third limb, cheap and worth having: one probe is not a measurement

While re-reading the IICBA brief in the same confirmation read, three identical requests twelve
seconds apart returned **500, 200, 200**. A serving state recorded from a single request is a sample
of size one, and this register's language — *read as served text on <date>* — quietly implies more
than one. Where the state is the finding, probe more than once and say how many times.

---

## What changed

* **`qa_sources_alive.py` gains a `tls-chain` bucket**, selected on the verify message, and the two
  buckets now carry opposite advice. `tls` keeps the interstitial sentence, because for an expired,
  self-signed or mis-hostnamed certificate it is true. `tls-chain` says *measure before writing
  anything*, names the AIA step, and states plainly that **the reader is not Python**.
* **Proved both ways against five live hosts** rather than against an injection: `expired`,
  `self-signed` and `wrong.host` on badssl.com must stay in `tls` and do; `incomplete-chain` on
  badssl.com and the live `parliament.gov.zm` must move to `tls-chain` and do.
* **Zambia's annotations**, both languages, now carry the measurement as a dated observation —
  including the sentence that the two earlier readings did not survive checking, because a correction
  that hides its own history teaches nobody.

## The general form

Two sentences, and the second is the one that generalises furthest:

*A serving state is cited as read — by a named client, with its trust configuration, on a date.*

*And the remediation note attached to a check's finding is prose this publication will eventually
print. Prove it the way the verdict is proved, or do not write it.* A check that is right about the
layer and wrong about the consequence has not found a defect; it has drafted one.

---

## SECOND INSTANCE — 2026-10-05, a new mechanism and a worse property

**No new ruling number was minted. This is #80 arriving by a different road**, and the operation does
not number a lesson twice for that.

The **first complete sweep of the corpus** — 343 distinct URLs, affordable for the first time because
ruling #88 gave the sweep a total ceiling that morning — returned two URLs as
`unreachable · UnicodeEncodeError`. **That is not a fact about either host.** `urllib` must hand a
request line to a socket as ASCII, so a path containing Arabic raises *before a single byte leaves the
machine*. Percent-encoded, **both documents are served**: `mehe.gov.lb` answers HEAD **200** and
`almodon.com` answers GET **200**.

So: #80 was *the certificate is fine and only Python sees a problem.* This is *the URL is fine and only
Python cannot write it down.* Same ruling — **the tool's own limitation reported as a fact about the
source** — and, as #80's own second sentence warned, it would have been reported in the register where
it does damage, since this check's findings are editorial advice about whether a citation still stands.

**The property that makes this instance worse than the original, and it is the part worth carrying.**
The blindness is **language-correlated**. The corpus contains exactly **two** non-ASCII URLs; **both are
Arabic-language registers; both were mis-reported. Two of two, one hundred per cent.** A source-health
instrument that fails precisely on Arabic paths is not randomly wrong — it is **systematically blind to
the registers one of our two editions is built on**, and for a publication whose Arabic is *composed
from the sources* rather than translated, that is the worst available place for an instrument to be
blind. It would also have degraded in exactly the wrong direction over time: the more Arabic-language
primaries the publication cites, the more of its own source-health report becomes noise.

**Fixed** (`_to_uri`, IRI → URI with IDNA on the host), and proved both ways: ASCII URLs pass through
**byte-identical**, including one already carrying percent-escapes — so nothing is double-encoded — and
genuine redirects still print their arrow, while the two Arabic URLs now return a clean `200` with no
spurious self-redirect.

> **The general form, restated once more and now third-hand:** *every negative result a tool reports is
> a claim about two things — the subject, and the tool's ability to ask.* #80 separated them at the TLS
> layer. This separates them at the **encoding** layer. Before writing down any `unreachable`, ask
> whether the request was ever actually made.
