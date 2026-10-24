# Growth — 2026-10-24 · five cited registers now exist in a second copy

**Function:** growth (c) · **Queue item:** **32**, raised 2026-10-21 as the *action* half of item 15 and
deliberately not taken by the run that found it · **Outcome: 5 of 28 saved, confirmed, and the other 23
were refused by our own request rate.**

## Why this is a growth action and not a QA one

The growth loop's first clause is *publish slowly, verifiably — trust is the moat.* Ruling #111 measured
what that moat is actually made of and found a hole in it: of 342 cited registers, **40 exist in exactly
one copy** — 28 readable today, 12 already walled — so for those 40 the publication's own re-verifiability
depends on somebody else's hosting decision. Nothing about that is a check; it is an **action**, and item
15's closing run said so in writing and declined to take it.

It is also the kind of bet this operation prefers: **its outcome is readable without anyone's
permission.** No tracker, no platform, no founder decision. The archive either holds a copy or it does
not, and one API call says which.

## What was done, and what it returned

All **28** `live-only` registers were submitted to the Internet Archive's Save Page Now endpoint, four at
a time. Then every acceptance was re-checked against the availability API rather than trusted.

| | |
|---|---|
| submitted | 28 |
| accepted (HTTP 200) | **5** |
| confirmed present, timestamp 2026-10-24 09:06–09:07Z | **5 of 5** |
| HTTP 429, too many requests | 9 |
| connection refused outright | 14 |

The five now holding a second copy:

1. `archivespasec.confemen.org/.../Rapport-*` — **the PASEC report**, the register behind the continental
   ruler piece and the one a superlative was bounded against (#49).
2. `ccetkuwait.wixsite.com/ccet-english/about-us`
3. `dailynewsegypt.com/2026/08/16/...ibo-approval`
4. `documents.worldbank.org/...documentdetail/...`
5. `documents1.worldbank.org/curated/en/099063025153091285/txt/P175036-...`

`agents/stats/claim-registers.json` is updated for exactly those five, with `archive_note` recording that
the snapshot was **requested by this operation** rather than found — a snapshot we caused is a different
fact from a snapshot we discovered, and a later run must be able to tell them apart. The register now
reads **archived 170 · archive-unknown 137 · live-only 23 · walled-no-snapshot 12**.

## The finding, which is #111's own lesson one step further on

**23 of 28 failed inside 90 seconds of the first submission, and none of the failures is about the
archive's willingness to keep our citations.** Nine were an explicit 429; fourteen had the connection
refused, which is what a throttle looks like once it stops answering politely. Two of the "failures" were
not even candidates — they are already `web.archive.org` URLs, so the submission asked the archive to
archive itself.

#111 wrote: *a row that reads `archive-unknown` because we were throttled is an observation about us, not
about the world*, and gave its read path a request budget for exactly that reason. The write path needed
the same thing and did not have it, because nobody had ever used it. **A durability action has a request
rate the same way a measurement does**, and 28 is above it.

**So the action is paced, not abandoned:** the remaining 23 are topped up across runs on a budget, the
same shape `--emit` already uses, and the state file carries the note that says why the number moves
slowly. Five a day clears the live-only backlog inside a week without ever being refused.

## What is deliberately not claimed

- **No traffic figure.** The site carries no third-party tracker by design.
- **No claim that the 12 walled registers are recoverable.** They refuse us and they refuse the archive;
  a snapshot request cannot fix a paywall, and #43 still says a document we cannot read cannot outrank one
  we can.
- **No claim that a snapshot makes a figure true.** It makes the figure *re-openable*, which is the
  property #111 named and the only one this action buys.

**Carried to tomorrow:** item 32 stays open at 23 of 40, with the per-run budget named here. The 12 walled
ones need a different instrument and probably a different answer.
