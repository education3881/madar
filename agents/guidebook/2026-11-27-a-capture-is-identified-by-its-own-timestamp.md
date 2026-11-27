# Ruling #161 — a capture is identified by its own timestamp, and one capture has three byte counts

**Filed 2026-11-27 by the daily run, at the Editor's desk, during cell 3 of
`2026-11-26-qatar-pisa-2025-two-of-three`.** Family: **reachability** (*whether the number can be read at
all*), which keeps no running member count, so four homes move and there is no conditional fifth — a
deliberate reading of limb 1 of the 2026-10-04 second amendment rather than an omission.

## The statement

**A PROVENANCE TRIPLE IS CAPTURE TIMESTAMP + OBJECT + HASH. A TRIPLE THAT NAMES ONLY A DATE HAS NAMED A
MOVING TARGET, AND A BYTE COUNT WITHOUT ITS OBJECT IS A MEASUREMENT OF SOMETHING NOBODY ELSE WILL FETCH.**

## What happened

`www.oecd.org` has answered this runner **403** all month, so Edition 06 reads the OECD's PISA 2025
registers from the Internet Archive and records, for each one, the date, the byte count and the sha256 — the
discipline that makes a figure re-checkable by anyone with this repository and a shell. Four registers were
banked that way on 2026-11-26 and three of the four reproduced **to the byte** when this desk re-fetched
them for Test 1 on 2026-11-27.

The fourth, R2 — the *PISA 2025 Results (Volume I)* full-report page — did not. Its row read *snapshot of 16
November 2026, 1,614,913 bytes, sha256 `01b2bd4aa78bf802…`*. Measured today:

| What was asked for | What the archive returns | Bytes | sha256 (first 16) |
|---|---|---|---|
| `/web/20261116id_/…` | capture **20261116235912** | 1,634,885 | `766441db01c15257` |
| capture **20261114165129** | itself, twice, identical | **1,614,913** | `1c3018b4d17e205b` |
| capture 20261112193517 | itself | 1,618,973 | `1e6eb36b054625a2` |
| capture 20261113171658 | itself | 1,635,393 | `ebd980ecda49fdee` |

So the **byte count was right** and belongs to the capture of **14 November**; the date recorded was the date
*asked for*; and the hash reproduces from no capture of that page.

## The two causes, both of them method

**1. A Wayback request without a full fourteen-digit timestamp is resolved to the nearest capture, and which
capture that is changes as the archive indexes more of them.** `…/web/20261116id_/` resolved to the 11-14
capture when the read was banked and resolves to the 11-16 capture today — the 11-16 capture was taken
before the bank and indexed after it. **The request string is not the provenance. The response's own
timestamp is.**

**2. One capture has three objects, and therefore three byte counts.** For Chapter 2 of the same report:

| Object | How fetched | Bytes |
|---|---|---|
| playback page — toolbar injected, every URL rewritten | `/web/<ts>/…` | 2,544,478 |
| raw snapshot as stored, still gzipped | `/web/<ts>id_/…` | 279,017 |
| **raw snapshot decompressed — the document the owner served** | `/web/<ts>id_/…` then `gunzip` | **2,426,000** |

The third is the one the house cites and the one that reproduced R1, R3 and R8 exactly. A fourth number,
2,420,884, comes from `curl --compressed` on the raw path and is not the house method. **Nine times the
smallest and 95% of the largest are all honest measurements of the same capture; only one of them is a
measurement of the document.**

## Why this one is worth a number

Nothing was fabricated and nothing was stale. The URL resolved, the document was the right document, the
quoted spans were verbatim, and `qa_claim_registers` and `qa_citation_identity` were both CLEAN on it. **The
only wrong thing in the row was the evidence that the row could be checked again — and it read exactly like
evidence that it could.** That is the reachability family's own shape turned inward: #20, #54 and #100 are
about whether somebody else's document can still be read; this is about whether **our own record of having
read it** survives contact with a second reader.

It had already shipped. Both editions of `2026-11-27-thailand-pisa-2025-fourth-list` carried the triple when
they went live two hours before this run opened, which makes it a published figure that does not reproduce
(#114 clause: a figure printed only in an annotation is still published). Both were repaired in the run that
found it, with the correction stated in the annotation rather than made silently.

## Binding

1. **An archived register is cited by its capture's own fourteen-digit timestamp**, read from the response,
   never by the date requested. A citation reading *"snapshot of <date>"* alone is incomplete.
2. **A byte count is cited with the object it measures.** The house object is the raw snapshot decompressed;
   where another is measured, the annotation says which.
3. **A hash is recorded only if it was computed in the run that records it**, and the run states that it
   re-fetched rather than trusted the bank (#101's requirement, which R8, R1 and R3 satisfied today and R2
   had not).
4. **A banked read is re-fetched at compose time and at verdict**, and a disagreement between the bank and
   the re-fetch is a finding to write down, not a number to overwrite — the Editor's desk is where this one
   became visible, because it is the second reader.

## The general form

*A provenance record is an instrument like any other, and it has a population: the set of fetches that would
reproduce it. A record whose population is "whichever capture the archive thinks is nearest today" has a
population that moves, so it can be true when written and false when read, with no byte changing on either
side.* That is **#117's time-dependence** (a served tense expires) applied to a citation's own metadata
instead of to its prose — and like #117, no comparison of two bytes can see it, because both bytes are ours.
