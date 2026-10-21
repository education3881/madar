# Growth — a second route to every citation the archive has kept

**2026-10-21 · the daily growth function · under ruling #111**

## The bet, and why it is a growth bet rather than a QA fix

`qa_sources_alive`'s own header states the thing this publication's growth actually rests on: *the
reader who follows a source is the reader who was going to come back.* Return rate, not reach.

This morning's queue work measured how fragile that is — of 342 cited registers, 205 have been asked
and **40 of those hold no snapshot anywhere.** The *other* side of the same measurement had nobody
looking at it: **165 registers ARE snapshotted**, and the reader was never told. A ministry PDF that
404s next year was going to take a figure with it and leave the reader at a dead end, while a copy
sat at a public URL nobody linked.

So the source list now offers the archived copy beside the live register, both editions:

> MINEDUC — 2024/2025 Education Statistical Yearbook … · *archived copy, 2026-08-31*
>
> …  · *نسخة محفوظة، 2026-08-31*

## Measured on the built output, not predicted

| | |
|---|---|
| EN article pages carrying at least one archive route | **42 of 44** |
| AR article pages | **43 of 44** |
| Archive anchors served | **169 EN + 170 AR = 339** |
| Registers with a known snapshot | **165 of 342** · 137 not yet asked |
| Pages with no route at all | `2026-07-07-singapore-psle-sbb`, `2026-09-01-sudan-cant-wait-to-learn` (EN) |

The two bare pages are a finding, not an omission to fix by hand: their registers are in the 137 the
paced emit has not reached. The number rises on its own as the register fills, which is the point of
building it as a register rather than as a one-off sweep.

## Three design calls, recorded because each could have gone the other way

1. **The live register stays first and keeps the title link.** The archive is an *offer*. A cached
   copy is evidence about what a page said; the owner's own URL is what the piece cites, and
   demoting it would be a quiet change to what this publication claims.
2. **It is an `<a href>`, and nothing is fetched automatically.** `qa_third_party_origins` classifies
   by *who initiates the fetch*, never by origin, and it now counts **4,238 reader-initiated anchors
   across 230 external origins** — web.archive.org among them — with the automatic set still clean at
   **641 references across 135 pages, all first-party.** The privacy posture is unchanged: no image,
   no script, no font, no beacon.
3. **`rel="nofollow"` on the archive link only.** We are vouching for the register, not for a mirror
   of it.

## What the operation can read from this without anyone's permission

Nothing here needs a tracker, a platform or a founder decision — which is why it was chosen. The
readable outcome is the coverage number above, and it moves for two reasons we can tell apart: the
emit answering more registers (ours), and registers losing or gaining snapshots (the world's). Both
are in `agents/stats/claim-registers.json` with dates.

**Not done, deliberately.** Asking the archive to *take* a snapshot of the 40 registers that have
none is the obvious next move and it is an outbound write to a third-party service. It would be
defensible — the URLs are public and the archive exists for this — and it is still an action this
operation has never taken against an external service, so it is written down here as a recommendation
rather than performed quietly in a growth function. **Queued, not done.**
