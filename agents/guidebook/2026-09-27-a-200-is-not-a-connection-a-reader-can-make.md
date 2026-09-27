# Ruling #70 — a 200 is not a connection a reader can make

**Filed:** 2026-09-27 · daily run, Researcher + QA lanes, from one finding
**Family:** assertion discipline (*what is this check's answer actually about*) — with a limb in *which register speaks for the owner*
**Extends:** #54 (a 404 is not a death certificate), #20 (never declare rot on one read), #41 (fetched-on-date), #69 (the cause of an absence is a claim)

---

## The ruling

**A status code is produced by the client that asked, not by the host that answered.** When a run
records a register as *"200, read in served text,"* it has recorded what **our** fetcher was willing
to accept — and our fetchers are more forgiving than a reader's browser in at least one way that
matters. Between *200* and *404* lies a whole layer the operation had never named: the **transport**.
An expired certificate, a hostname mismatch, a broken chain. The document is right there; a reader
cannot get to it without being shown a full-page security warning first, and most will not.

Two things follow, and the second is the one with teeth.

**1. A register's serving state is recorded with the layer that failed, never as a bare verb.**
*Serves*, *unreachable*, *dead* are verdicts about a stack of four or five independent things. The
record names which one: DNS, TCP, TLS, HTTP status, content. The editorial disposition is different
at every layer, and opposite at two of them — a name that no longer resolves is superseded, while a
host with a lapsed certificate still holds the document, so the citation stands and the annotation
states the certificate's state instead.

**2. A check's bucket set is an enumeration like any other, and it cannot report a distinction it
cannot hold.** `qa_sources_alive` ran, was green-lit, had been run and read — and reported a host
whose certificate had expired while it went on serving every document, and a hostname that does not
exist anywhere in DNS, as the **identical string**: `unreachable · URLError`. Nothing was wrong with
the probe. The wrong thing was the vocabulary it had to answer in. *A green check is scoped to what
it enumerates* has been stated nine ways about **inputs**; this is the first statement of it about
**outputs**.

## The origin

On 2026-09-27 the Rwanda draft's source URLs were probed before the piece carried them. Six of its
eight registers live on `mineduc.gov.rw`, and all six returned nothing to `curl`. The cause, read
off the handshake rather than guessed at (#69):

```
subject=CN = mineduc.gov.rw     issuer=RapidSSL TLS RSA CA G1
notBefore=Sep 24 00:00:00 2025 GMT
notAfter =Sep 23 23:59:59 2026 GMT      <- four days before this piece was composed
```

With verification disabled, every one of the six returns **HTTP 200**, and the 2024/25 yearbook
returns **4,023,048 bytes** — the same byte count the 09-26 recon recorded, which is an independent
confirmation of that read from a different day and a different client. The documents are fine. The
host is not.

**And the operation had already recorded the opposite, three times.** The 09-24 re-verification
records three MINEDUC registers as *"200, unchanged."* The 09-25 hunt reads four MINEDUC pages in
served text. The 09-26 recon records the yearbook at *"HTTP 200, 4,023,048 bytes."* **All three ran
after the certificate expired.** Nobody wrote anything false about a figure; every figure in those
recons is confirmed and stands. What is wrong is a column in our own record, and it is wrong in the
direction that matters: it says a reader can reach these registers, on days when a reader could not.

## The corollaries

- **The failure layer is a fact about the world; the bucket is a fact about our tool.** When they
  disagree, the tool is the thing to change. Widening a tolerance so the check stops complaining is
  #63's mistake in a second costume.
- **A TLS failure is re-probed with verification disabled, once, to establish whether the document is
  still there** — and the answer is printed beside the failure, because *reader is warned but can
  click through* and *there is nothing behind it* are opposite editorial dispositions that the old
  bucket collapsed into one.
- **An expired certificate is a dated fact and belongs in the annotation with its date**, exactly as
  a fetched-on-date does (#41). It is also the most likely of all these failures to be fixed by
  someone else within days, which is precisely why it must not be recorded as a death (#54).
- **A first-party register can become unreadable without becoming wrong.** Nothing about the
  yearbook's figures changed on 23 September. The citation's *usefulness to a reader* changed
  completely, and only a check that reads the transport can see that.
- **Our clients are not the reader's client.** Anything that reports on the reader's experience
  should fail the way the reader's software fails, or say in its own header how it differs.

## The companion finding — the same shape, one layer further out

The same tool carried a second defect of the identical kind, and it had been filed as a P1 since
**2026-09-16**: *"`qa_sources_alive --held-only --sample 0` did not complete in this run (40 minutes,
no output, no JSON — it prints only after the final URL)."* Read today, **it always printed per
URL.** The sweep was never silent. Its stdout was **block-buffered**, because the run redirected it
to a file rather than a terminal, so nothing reached the file until the process exited — and a step
the ledger requires as *the last thing before the wave flip* was diagnosed as unbounded and
un-observable when it was neither.

**The tool was observable; the pipe was not.** A P1 stood for eleven days against the wrong
component, and the fix is one keyword. Generalised, and it belongs beside the ruling rather than
under it: **when an instrument appears to tell you nothing, establish whether it is the instrument or
the channel before you write down a cause** — which is #69 arriving in the toolchain instead of in a
recon.

## Proved both ways, per #35 — against a live defect rather than an injected one

`probe()` was run against seven cases, two bites and five controls, before and after the change. The
*before* run is the evidence and was captured first:

| Case | Before | After |
|---|---|---|
| **BITE 1** — mineduc yearbook: cert expired, document served | `unreachable · URLError` | `tls · cert: certificate has expired · document still served (200)` |
| **BITE 2** — mineduc news index, same host, HTML | `unreachable · URLError` | `tls · cert: certificate has expired · document still served (200)` |
| CONTROL 1 — World Bank feature, valid cert, alive | `ok · 200` | `ok · 200` |
| CONTROL 2 — allAfrica story, valid cert, alive | — | `ok · 200` |
| CONTROL 3 — a hostname that does not resolve | `unreachable · URLError` | `dns · name does not resolve` |
| CONTROL 4 — resolves, nothing listening on the port | — | `refused · connection refused at :443` |
| CONTROL 5 — valid cert, genuine 404 | — | `error · HTTP 404` |

The bite is proved as carefully as the control (#35 as amended 09-14): **bites 1 and 3 were the same
string before the change** — that identity *is* the defect, and it is what the table has to show.
The controls exist to prove the new `tls` bucket is not simply swallowing every failure: three
distinct non-TLS failures land in three distinct non-TLS buckets, and the two live hosts are
untouched.

**Limit, stated rather than left to be found.** This names the layer for failures the probe can
*observe*. It says nothing about a host that serves a valid certificate and wrong content, about a
bot wall that returns 200 with a challenge page, or about a document that has been silently edited —
three surfaces nothing we own reads. The first of those is [[2026-09-26-inject-the-defect-that-shipped-not-the-bite-you-wrote]]'s
territory; the third is the one to name next.

## What changed on disk

- `agents/tools/qa_sources_alive.py` — `classify()` names the failure layer (`tls` / `dns` /
  `refused` / `timeout` / `unreachable`); `_root_cause()` walks `URLError.reason` to the thing that
  actually failed; `_still_served()` re-probes a TLS failure once, unverified, and reports whether
  the document is behind it; per-URL output is flushed; each new bucket carries its own editorial
  disposition in the findings list.
- The Rwanda draft's `sources[]` states the certificate's expiry date and its consequence for a
  reader, on all six MINEDUC registers, in the annotation.
- Still **not** a deploy gate, and the reason in the workflow file is unchanged and still correct:
  someone else's expired certificate is not our build's failure. It is now a finding our own sweep
  can *say*.

Related: [[2026-09-16-a-404-is-not-a-death-certificate]] · [[2026-09-26-the-cause-of-an-absence-is-a-claim]] · [[2026-09-25-run-it-twice-and-the-verdict-is-not-the-record]]
