# Growth — the feed as a reader's software actually receives it

**2026-09-20 · Growth, with the Web Developer · the surface named and owed since 2026-08-18**

The feeds have been the operation's named blind spot for thirty-three days. The 08-18
rule that found the `og:image` defect closed by naming the next surface, and the 08-23
RUNBOOK rule carried it verbatim ever since:

> **The surface named and still owed, carried from 2026-08-18: the feeds.** Both are
> well-formed and serve 38 items each, and *nothing has ever verified that an item renders
> legibly in an actual reader, that Arabic items carry their direction, or that the links
> resolve from outside our own origin.*

Asked today — not because it was scheduled, but because diagnosing the red deploy put both
feeds on the desk — it bit on the first question.

## The finding

Every `<enclosure>` in both feeds declared an empty file.

```xml
<enclosure url=".../og/2026-07-28-england-report-cards-first-term.png"
           length="0" type="image/png" />
```

In RSS 2.0 `length` is the size of the enclosure **in bytes**. It is not decoration: it is
the number a reader consults before deciding whether to fetch the image, show a
placeholder, or skip the enclosure entirely — and it is the one field in the element that
a reader can act on without a round trip. **Seventy-six enclosures, two languages, 38
pieces, every one of them declaring nothing is there.** The cards themselves are fine:
1–20 KB, valid PNG, correctly typed, resolvable, and served since 08-18.

This is the 08-18 defect exactly, one surface over. There, `og:image` was a real file at a
real URL in a format no consumer renders. Here, the card is a real file at a real URL in a
format every consumer renders, and the feed tells the consumer it is empty. Both times the
URL was never the problem. **The promise about it was.** And both times every check this
operation owns passed, because every one of them asks *does it resolve*.

## What it cost, stated without a number we do not have

The site carries **no third-party tracker by design**, so there is no visitor figure here
and there will not be one. What can be said is what is structurally true rather than
estimated: a feed reader that honours `length` has had no reason to fetch a single share
card since enclosures shipped, which means **every item Madār has ever syndicated
travelled as text** in any reader that trusts the field. That is not a traffic claim; it
is a claim about what the bytes permitted.

The honest read on impact is also the smallest one: our feeds are new, the corpus is 38
pieces, and **the return-rate signal this operation actually plans to read — Substack
opens and reply rate — is not yet switched on.** The value of today's fix is not a
recovered audience. It is that the one distribution surface we own outright, that needs
nobody's permission to read, is now telling the truth.

## Fixed, and gated

`length` is now measured from the card on disk at build time, so it cannot drift from what
is served. Landed with **standing assertion 21, `qa_feed_enclosures.py`**, which checks the
declaration against the **served file in `dist`** rather than against the build's own
arithmetic — a check that re-ran the computation it audits would agree with it by
construction. It asserts four things per enclosure: the URL resolves in `dist`, the
declared `length` equals the real byte size, the declared `type` matches the file's **magic
bytes** rather than its extension, and the enclosures have not quietly disappeared.

Proved six ways per #35, every injection asserted to have changed the artefact first:
`length` reverted to 0 (the real defect) · off by a single byte · a PNG declared as JPEG ·
a card replaced with an SVG payload, which is 08-18 reopened and fails on three axes at
once · every enclosure stripped · and a `dist` with no feed, which exits 2 because a check
that finds nothing to check has failed. **The gate is proved rather than assumed: with
`length="0"` restored in `feed.ts`, `npm run build` exits 1.**

## Still owed on this surface — the two questions today did not answer

Today took the first of the three the 08-18 note named. The other two stand, and they are
named here so they are not quietly retired along with the enclosure:

1. **Do Arabic items carry their direction in a reader?** Both AR feeds wrap each
   description in `<div dir="rtl" lang="ar">`, which is present and correct **in our
   markup**. Whether a given reader honours a `div` inside an escaped description, or
   strips it to plain text and renders our Arabic left-to-right, is a property of *that
   reader* and is not knowable from `dist`. This is #16 — verify in the judging
   environment — and the judging environment here is somebody else's application.
2. **Do the links resolve from outside our origin?** Every link in both feeds is absolute
   and on `education3881.github.io`, and the `verify` job byte-compares five files against
   the live origin. Nothing has fetched a feed *item* link from outside CI.

Neither is expensive. Both need a client we do not currently own, and both are the honest
shape of the 08-18 rule: **a promise in the metadata is a promise to a machine we do not
own — verify it against that machine, never against our own filesystem.** Today's fix was
the half that `dist` can prove. The half that needs a reader is still a debt.
