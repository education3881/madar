# Growth — the held wave's source promises, read the way a reader meets them

**Date:** 2026-09-27 · **Growth → Editor, Verifier, Web Developer**
**Instrument:** `qa_sources_alive --held-only --sample 0`, with the failure-layer classifier filed today (ruling #70)
**This is the sweep the Edition 05 ledger requires immediately before the flip commit. Run early, deliberately, because a fix found now is free and a fix found at the flip is not.**

---

## Why this is the growth action and not a QA line item

Madār's whole argument for being worth returning to is that every figure stands on a named primary
source the reader can open. That is not a traffic claim, it is a **return-rate** claim: the reader who
follows a citation is the reader who was going to come back. A rotted citation does not degrade a piece
slightly — it converts the publication's central promise into a dead end in front of the one reader who
cared enough to click.

The site carries **no third-party tracker by design**, so this operation cannot read how many readers
click a source. What it *can* read, without anyone's permission, is **what happens to the reader who
does** — and that is the whole of the measurement below. It is the kind of bet this operation prefers:
the outcome is legible from our own side of the wire.

## The read — 57 distinct promises across the six held pieces, every one of them, no sampling

| Bucket | Count | What the reader experiences |
|---|---|---|
| `ok` | **41** | The document opens. |
| `tls` | **10** | A full-page browser security warning **before** the document. The document is behind it — all ten confirmed still served at 200. |
| `timeout` | **3** | A spinner, then nothing, on this reading. |
| `walled` | **2** | HTTP 403 — a bot wall, which a human reader may well pass and this runner cannot. |
| `error` | **1** | A hard 404. |

**41 of 57 open cleanly. Ten do not, and until today all ten were invisible as a class.**

## The finding, and it is not the one this sweep was run to get

**Zambia's four `parliament.gov.zm` URLs are not unreachable, and the documents are all still there.**

The ledger has carried them since 2026-09-10 as `unreachable`, re-probed on 09-16 from a second client
six days on (#20 satisfied) and recorded as *"connection refused at :443, not 404, not a timeout"* — an
open confirmation-read item with a third route named and not attempted, and an unanswered question
about whether the cause was our egress geography. Read today with a probe that can name the layer:

```
tls · cert: unable to get local issuer certificate · document still served (200)   ×4
```

The chain the Zambian parliament serves does not validate against this client's trust store. **Behind
it, all four documents — the bill, the two node pages and the 30,000-teacher ministerial statement —
return 200.** That is a different fact from *refused*, it carries a different editorial disposition,
and it has been sitting in the wrong bucket for seventeen days because the sweep had no bucket to
put it in. The geography question is moot; it was never about geography.

**Six more are Rwanda's**, all on `mineduc.gov.rw`, whose certificate expired on **23 September 2026**
while the ministry went on serving every document. Those annotations were written correctly in the
draft today, because the draft lane found it first.

## What each bucket is owed, routed

| Owed to | Item |
|---|---|
| **Verifier** | Zambia's four parliament URLs move off the confirmation-read list as *unreachable* and onto it as **`tls`, documents served**. The annotation states the chain's state; the citation stands. **The third-route / egress-geography question is closed, and closed as moot.** |
| **Verifier** | Sierra Leone's Save the Children URL still returns **404** — as expected: #54 (09-16) found the piece re-slugged and live elsewhere, and the frontmatter still carries the old address. This is the sweep confirming an open item, not a new one. The upgrade candidate (the programme's Final Learning Report) is still the Verifier's call, not Growth's. |
| **Editor / Verifier** | Three `timeout`s, all on Egypt (row 5): **two `dailynewsegypt.com` articles** and **`lawhub.info/eg/?p=15517`**. The last is Egypt's **source 1**, the statute reproduction the fee clause is taken from, already carried as fetched-on-date with the host's state stated in its own annotation since 09-23 — today's read is *consistent with* that annotation rather than new information, and it is now named as a timeout rather than as an undifferentiated failure. One slow read is not a death (#20): re-probe at the confirmation read, and note that two hosts timing out is two facts, not one. |
| **Web Developer** | Nothing. The 09-16 P1 against this tool — *"40 minutes, no output, no JSON"* — is **closed**, and it was never the tool's pace: its stdout was block-buffered because the run redirected it to a file. Today's run printed every line as it went and wrote its JSON. The step the ledger puts immediately before the flip commit is now watchable while it runs. |

## The number Growth will not give you

**No visitor count, no impression estimate, no reach figure.** The site carries no third-party tracker
by design, so no such number exists to read and this operation does not compose one. What is measured
above is a property of our own corpus against the live web, and it is reported as exactly that.

## The bet this proposes for the week of 09-28

**Run this sweep against the *approved* corpus too — 338 distinct URLs, of which 57 have been read.**
Every figure in the piece above concerns six pieces nobody outside this operation can read yet. The
other 281 promises sit on 38 published pieces that readers *can* open, and no run has ever read them
with an instrument that could name a TLS failure. If ten of fifty-seven held promises were in the wrong
bucket, the published corpus is the place that matters. Sampled at 60 per run it is five runs; run
whole it is one long one. **Growth's recommendation: whole, once, before the wave flips**, so the
number the wave lands against is known rather than assumed.

— Growth · 2026-09-27
