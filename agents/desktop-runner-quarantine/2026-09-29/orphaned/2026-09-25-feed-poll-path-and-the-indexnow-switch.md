# Growth — the feed poll path measured from outside, and the IndexNow switch put to the founder

**Filed:** 2026-09-25 · desktop session, workflow lane · **Function (c), one concrete action**
**Traffic honesty:** the site carries **no third-party tracker by design**. Nothing below is a
visitor number, and none is estimated. Every figure is a measurement of a *surface*, taken
today against the live origin.

---

## 1. The one distribution channel that needs no account was, until today, ungated

Madār has exactly one reader-facing distribution path that requires no platform, no account
and no permission: **the two RSS feeds.** A reader who subscribes polls them; whether that
poll is cheap or expensive is decided entirely by cache validators.

Measured today, from an outside client, against the live origin:

| Feed | HTTP | Bytes | Content-Type | Connections | Distinct validators | Revalidated 304 |
|---|---|---|---|---|---|---|
| `/madar/rss.xml` | 200 | 29,508 | `application/xml` | 8 | 1 across 7 edges | **8 / 8** |
| `/madar/ar/rss.xml` | 200 | 37,390 | `application/xml` | 8 | 1 across 8 edges | **8 / 8** |

**16 of 16 revalidations honoured.** A subscriber's client pays the full body once and
`304 Not Modified` thereafter. That is the good news and it is not the finding.

**The finding is that this was never gated, and today it is.** Since the feeds shipped, the
step meant to protect this path was a coin flip (#63) — and the fix for it had been staged
since 09-24 and unapplied, because the autonomous identity cannot write workflow files. It
was applied in this session. From the next dispatch, **a regression in the reader's poll path
fails the deploy** instead of failing quietly at the reader.

Worth stating plainly, because it is easy to read the table above as "nothing was wrong":
today the origin served **one** validator per feed. Yesterday it served two. The mechanism
that produced yesterday's red has not changed — the difference is which way the coin landed.
What changed is that we no longer depend on the coin.

## 2. The IndexNow switch — a founder decision, with the cost of leaving it off named

`INDEXNOW: "off"` in `astro-pages.yml`, staged off deliberately (2026-09-06): submitting our
URL set to an external index is a binding (#7) and an action in the publication's name, so it
is the founder's word, not a run's. That reasoning stands and this note does not reopen it.

What this note adds is a **date**, because the decision has one now:

- The key file is hosted and **served**: `/madar/66ec26c5232c206b2c4714fd916a29a8.txt` → **200**.
  `robots.txt` → **200**, one `Sitemap:` line, resolving. The mechanism is ready and idle.
- With the switch off, the step does a **dry run** and logs what it would submit. It has been
  doing that for nineteen days.
- **Edition 05's wave gate targets 2026-10-11** — six pieces, both languages, flipping
  atomically in one commit. That is the single largest batch of new URLs this publication will
  ever have published at once, and it is the one moment where telling an index *the day it
  happens* differs most from waiting to be crawled.

So the decision is not "should we ever" but **"before or after the wave"**. Stated as the
trade rather than as a recommendation:

| | Turn it on before the gate | Leave it off |
|---|---|---|
| The wave's URLs | announced the hour they ship | found whenever a crawler returns |
| Binding incurred | one POST in the publication's name, per deploy | none |
| Reversible | yes — one word back to `"off"` | n/a |
| What we can measure | **nothing directly** — no tracker, and IndexNow reports no traffic | nothing |

That last row is the honest one and it cuts against acting. **We cannot measure the result.**
Turning IndexNow on will not produce a number we can read, now or later; it changes when an
index learns a URL exists, and our instruments cannot see an index. Anyone arguing for it is
arguing from mechanism, not from evidence, and should say so.

**Manager's view, for the record and not as an instruction:** turn it on *after* the wave is
live and a `verify` job is green, not before — the gate day already carries six pieces, an
atomic flag flip, three confirmation reads and a source-promise sweep, and adding the
operation's first outbound binding to that list puts a new failure mode on the most crowded
day in the calendar. **The founder decides, and nothing happens until he says a word.**

## 3. Lead with return rate, not raw counts — restated, because there is still nothing to lead with

The standing instruction is to lead with return rate. **We cannot compute one**, and will not
be able to while the site carries no tracker — which is the design, not a gap to be closed
quietly. The feed is the nearest honest proxy we will ever have: a subscriber who polls is a
returning reader by definition. We still cannot count them, because a conditional GET that
returns 304 is served by Fastly and never reaches anything we own.

**What this means, said once so it is not rediscovered:** the operation's audience evidence is
structurally limited to *surface health* — does the feed serve, does it revalidate, does the
sitemap resolve, does the 404 return people to the front door. Every growth note should be
read as a statement about the surface, never about the audience. Today's is.
