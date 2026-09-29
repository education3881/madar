# Ruling #76 — A serving state is an observation with a date, not a fact about a host

**Filed:** 2026-09-29, by the Editor's pair verdict on Edition 05 row 6.
**Family:** sourcing discipline / the clock. Direct limb of **#70**, and the inverse of it.

---

## The finding

Ruling #70 was filed on 2026-09-27 because `mineduc.gov.rw` served every document at HTTP 200 while
its TLS certificate had expired on 23 September 2026 — **a 200 is not a connection a reader can
make.** The ruling was right, the observation was right, and the piece drafted that day did the
honest thing with it: it recorded the serving state in `sources[]`, six times, once per MINEDUC
register.

Two days later, at the pair verdict, Test 1 re-probed all eight URLs — *does every cited URL
resolve, today, to the document the piece claims it does?* — and the answer had changed:

```
subject   = CN = mineduc.gov.rw
issuer    = C = US, O = DigiCert Inc, CN = RapidSSL TLS RSA CA G1
notBefore = Sep 23 00:00:00 2026 GMT
notAfter  = Apr  9 23:59:59 2027 GMT
serial    = 08C5F3EEE50C8CF981221D5B9C21AB76
```

Same common name, same issuer, **new serial**, valid to April 2027. All six MINEDUC URLs return 200
**with certificate validation enabled**, at byte counts identical to the drafter's. The host was
renewed between the draft and the verdict.

**What the pair would have shipped:** six annotations in each language stating that a reader
following those links "meets a full-page security interstitial", that validation-disabled is "the
only way to obtain it today", and — in source 3 — that the World Bank is "the only source for this
piece whose host serves a valid certificate". Three claims, all false, all about a wall the reader
does not meet. Twelve annotations across the pair.

## The ruling

**The observation was never wrong. The tense was.** Each annotation stated a host's momentary
failure as a **standing property**, in the present tense, with the word *today* doing all the
dating — and *today* is the one word in a citation that cannot mean anything by the time a reader
arrives.

> **A register's serving state is recorded as a dated observation, in the past tense of
> observation, never as a present-tense condition of the host. It decays faster than the document
> does, and it decays in both directions.**

#70 established that a refusal can hide behind a 200. **This is #70's inverse and the more
dangerous half: a refusal can also simply end.** A document's *content* is stable — that is why we
cite it, and why identical byte counts across three days are worth recording. Its *reachability* is
a property of somebody else's operations calendar, and a certificate renewal is a ten-minute
administrative act. Of the two facts an annotation carries, we had been writing the durable one in
a hedged past tense and the volatile one in the present.

**The practical shape, as applied to row 6 and binding on every annotation from today:**

1. **Date every serving-state clause**, on both sides of a change. Not *"the certificate has
   expired"* but *"on 26 and 27 September 2026 the certificate served had expired on 23 September;
   re-probed 29 September 2026, the host serves a valid certificate, new serial, valid to 9 April
   2027."* Two observations, two dates, neither superseding the other as a record.
2. **Never let *today* carry a date.** It is the same defect as a bare month (see the pair verdict's
   note 2, filed the same hour): a word whose referent is the writer's present, printed for a reader
   whose present is different.
3. **A serving-state fact used for a uniqueness claim inherits the decay and amplifies it.** Source
   3's *"the only source whose host serves a valid certificate"* was true for three days and became
   false without anything in source 3 changing — the claim was about the *other seven*. A
   superlative built on a volatile property is a superlative with a shelf life (**#29**, *a
   superlative is a figure*, meeting **#49**, *read the bound*). Bound it to its dates or do not
   write it.
4. **State why the shape is what it is, in the annotation.** Row 6's now closes: *a serving state is
   an observation with a date, not a fact about a host.* A reader meeting a dated two-part
   observation should not have to guess whether we know that.

## Why no gate caught it, and which one could

Nothing we own looks at this. `qa_sources_alive` probes URLs and — since #70 — reports the layer
that failed; it is one of the three assertions that deliberately do **not** gate the deploy, because
someone else's 404 is not our build's failure. That reasoning still holds. But it means the
operation has an instrument that can see a serving state and **no instrument that compares a
serving state against what an annotation claims about it.** The figure-trace axes are numeric; the
four non-numeric rows added on 09-13 are noun, quotation, clock and description-date. This is a
fifth: **serving-state date**, and it belongs beside them on the Verifier's trace.

Named as the forward surface rather than built today, because the fix that mattered was in the
prose and the prose is the Editor's.

## The clock family, and the fuse length

This is the **third** instance of the clock class open on Edition 05 and the first found at a pair
verdict rather than at a later calendar re-read.

| | sentence true at compose | false by | fuse |
|---|---|---|---|
| Item A (Zambia ¶103) | 25 Aug 2026 | Sep 2026 | ~2 months |
| Item B (slot 3 ¶94) | 14 Sep 2026 | — (narrowing, not decay) | n/a |
| **This** | 27 Sep 2026 | **29 Sep 2026** | **2 days** |

**The fuse can be shorter than the gap between drafting and the verdict**, which is the part worth
carrying. The operation had been treating the clock as an edition-scale risk — something a wave
accumulates while it waits for a gate. A certificate renewal shows it is not about waiting. Any
sentence about somebody else's infrastructure is stale-able **within the drafting week**, and the
cheapest place to catch it is the re-probe the pair verdict already performs for Test 1. That
re-probe was already required. What is new is that its output must be read against **what the
annotations say**, not only against whether the document is there.
