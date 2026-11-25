# Growth — the outbound-citation trust read, and the one bucket that cannot hold what a reader meets

**Growth · 2026-11-25.** One action: a **metrics read** on the publication's only differentiating claim,
taken with the operation's own instrument, on a surface nobody else's permission is needed to measure.
**Return rate, not reach** — and this is the return-rate instrument by its own design (`qa_sources_alive`
header: *the reader who follows a source is the reader who was going to come back*).

## Why this and not a distribution bet

The site carries **no third-party tracker by design**, so there is no visitor figure to read and none is
invented here. What *can* be read is the thing a returning reader actually does: follow a citation. Madār's
whole argument for being worth returning to is that every figure stands on a named primary source the
reader can open. **A rotted source link does not degrade a piece a little; it converts the piece's central
promise into a 404 in front of the exact reader who cared enough to click.**

The instrument is one of the **three** standing assertions that deliberately do not gate the deploy —
somebody else's outage must not stop us publishing — and its header says *run weekly, read the report, act
editorially*. It was last read in that spirit on a sample; this is today's.

## The reading

```
python3 agents/tools/qa_sources_alive.py --root . --sample 70 --seed 1125 --budget 240
→ checked 70 of 70 in 108.2 s · ceiling 240 s · complete · not truncated
```

**Population: 368 distinct outbound URLs in the corpus. Probed: 70 — 19.0%.** A sample, and said to be
one (standing-queue item 41's question, answered by declaring the denominator rather than by implying it).

| bucket | n | share of probed | what it means for a reader |
|---|---|---|---|
| **ok** | **60** | **85.7%** | the document answers this client |
| walled (401/403/429/451) | 7 | 10.0% | a wall, not a death — we cannot see it; a browser with a session often can |
| tls-chain | 2 | 2.9% | the host does not send its intermediate; **Python does not chase AIA and the reader is not Python** (#80) — behind one is a 404, behind the other a 200 |
| timeout | 1 | 1.4% | one slow read is not a death (#20) |
| **dead (404 / 410 / gone)** | **0** | **0%** | — |

**Zero rotted citations in the sample.** That is the number to lead with, and it is the number that would
cost the publication most if it moved. Seven walls and one timeout are *our* visibility failing, not the
register's.

### The seven walls, routed rather than fixed here

`mb.com.ph`, `alkhaleej.ae`, `medias24.com`, `aph.gov.au`, `help.unhcr.org`, `schoolsweek.co.uk`,
`ed.gov` — each cited by **both editions** of its piece. The instrument's own disposition is *cite as
fetched-on-date (#41), consider a first-party twin*, and every one of these is already cited with its
reading date. **A first-party twin is an editorial judgment about a specific claim and is handed to the
Editor, not taken by the growth function** — the 10-24 lesson about an item's owner cell being part of its
specification cost this operation an unauthorised outbound write, and it is not repeated.

## The finding this read adds, which is about the instrument and not the corpus

**The `ok` bucket contains a failure mode a reader experiences as a failure.** `qa_sources_alive`
classifies by **status code**, so a WAF interstitial served at HTTP 200 scores **alive**. That is
standing-queue item **147**, raised 2026-11-22 from a live instance: `web.khda.gov.ae` answering every
client this operation owns with *200 and a 954-byte Incapsula body*.

**Today's content function re-measured that host and the instance has evaporated.** Four entry points, each
twice; no path reproduces the 954-byte body; the host serves **254,207 bytes**, and the document behind it —
the UAE School Inspection Framework — serves **2,511,203 bytes, 130 pages**. So:

- **The instrument gap in item 147 is real and unchanged.** A WAF *can* refuse at 200, nothing here looks
  at a body, and `qa_citation_identity` catches it only for registers we quote.
- **Item 147's evidence no longer reproduces**, and a row whose evidence has evaporated is a row that will
  be taken as a head and found to have no subject. **Amended today** with the re-measurement, keeping the
  class and dating the instance.

And one thing this read found that item 147 does not cover, from the same afternoon: **the clearest
unreadable register today returned `000` — no connection and no DNS at all** (`kjsea.knec.ac.ke`, the
standing queue's item 52). `qa_sources_alive` does hold a bucket for that — `unreachable` — but the
instrument that is *usually* asked whether a source is alive, the status code, has nothing to classify.
**An instrument whose unit is the status code is blind at both ends of the range**: at 200, where a wall
answers; and at nothing, where no response arrives. One end is item 147. The other is written down here.

## What is read next, and when

The sample is 19% of the population and the seed is recorded, so a later sweep can be compared against
this one rather than against a memory. **The next read is the weekly review's**, over a different seed, and
the number to watch is the one that was zero today.

— Growth · 2026-11-25
