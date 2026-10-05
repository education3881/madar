# Growth — the first complete census of every outbound promise this publication has made

**2026-10-05 · Growth lane · read without anyone's permission, which is the point**

## Why this was possible today and not before

`qa_sources_alive`'s own header calls it a **return-rate instrument, not a traffic one**: *the reader
who follows a source is the reader who was going to come back.* It has run **sampled at 60** since
2026-09-10, because a full sweep had no stated duration and therefore no way to be scheduled.

**Ruling #88 landed this morning and gave it a total ceiling.** The full corpus became affordable the
same day, and this is the first time the publication has ever looked at **all** of it:

```
343 distinct URLs · 684 citations · 88 content files
checked 343 of 343 in 609.2s · ceiling 1200s · complete
```

Ten minutes. The thing that could not be scheduled turns out to take ten minutes — *which is itself the
finding about the eighteen days, and it is not a flattering one.*

## What the census says

| Bucket | n | What it means |
|---|---|---|
| `ok` | **278** → **281** after re-reads | answers cleanly |
| `walled` | 40 | 401/403/429 — an institutional bot wall. **A wall is not a death** (#70) |
| `tls-chain` | 7 | certificate fine, intermediate unsent. **The reader meets nothing** (#80) |
| `tls` | 2 | genuinely bad certificate; browser shows an interstitial |
| `timeout` | 6 | slow or unreachable from here |
| `error` | 8 | 4xx/5xx |
| `unreachable` | 2 | **our own defect — see below** |

**Lead with return rate, never raw counts:** of every promise this publication has made to a reader who
cares enough to click, **~82% answer cleanly on a first read, ~12% sit behind a wall we cannot see
through but a reader often can, and five are simply gone.**

## The five that are gone — confirmed on two reads (#20), on PUBLISHED pieces

These are hard 404s, stable across two independent reads taken ~15 minutes apart:

| URL | Cited by | Both languages |
|---|---|---|
| `ei-ie.org/en/item/29865:just-wages-for-public-school-teachers-in-lebanon` | `2026-07-07-lebanon-crisis-schooling` | yes |
| `men.gov.ma/docs/Etablabellises2025117Col.pdf` | `2026-07-06-morocco-ecoles-pionnieres` | yes |
| `men.gov.ma/docs/Etablabellises2025117Prm.pdf` | `2026-07-06-morocco-ecoles-pionnieres` | yes |
| `osym.gov.tr/TR,25547/2023-yuksekogretim-kurumlari-sinavi-...` | `2026-07-07-turkiye-earthquake-school-recovery` | yes |
| `unicef.org.uk/press-releases/unicef-goodwill-ambassador-orlando-bloom-visits...` | `2026-07-07-rohingya-myanmar-curriculum` | yes |

**Four published pieces, both languages — eight live pages — carry a citation that 404s today.** This is
exactly the failure the tool was built to catch: *a rotted source link does not degrade the piece a
little; it converts the piece's central promise into a 404 in front of the exact reader who cared
enough to click.*

**Not fixed in this run, deliberately, and the reason is a standing rule rather than a shortage of
time.** These are **served bytes on published pieces**, and the split's standing exception is explicit:
*a fix that changes served bytes is the Web Developer's even when an assertion found it.* It is also an
**editorial** call per #41 — *supersede, don't resurrect*: each needs a replacement register read in
served text, or an annotation that records the 404 as a dated observation, and that is the Editor's
disposition to make, not Growth's. **Filed to the standing queue with the evidence attached.** Rushing
five annotation rewrites into the tail of a run six days before a wave flip is how a correction becomes
the next defect.

## Three that the SECOND read changed — and two of them were our own fault

**#20 earned its keep three separate times today.** *Never declare rot on one read:*

- `youm7.com/story/2025/10/20/-/7165289` — **503 → 200.** Transient. One read would have recorded a
  dead Egyptian daily.
- `almodon.com/.../روابط-المعلمين-...` — **`unreachable` → 200.**
- `mehe.gov.lb/ar/.../الوزيرة-كرامي-...` — **`unreachable` → 200.**

**The last two were not about the hosts at all.** Both are Arabic-path URLs, and `urllib` cannot put a
non-ASCII URL on the wire — it raises `UnicodeEncodeError` *before a single byte is sent*. Our tool was
reporting **its own inability to form the request** as a fact about a Lebanese ministry and a Lebanese
newspaper. Percent-encoded, both serve **200**.

**And the shape of that blindness is the real finding here.** The corpus contains exactly **two**
non-ASCII URLs. **Both are Arabic-language registers. Both were mis-reported. Two of two.** A
source-health instrument that fails precisely on Arabic paths is not randomly wrong — it is
systematically blind to the registers **one of our two editions is built on**, and for a publication
whose Arabic is *composed from the sources* rather than translated, that is the worst available place
to be blind. It would have degraded in exactly the wrong direction, too: the more Arabic primaries we
cite, the more of our own source-health report becomes noise.

**Fixed today** (`_to_uri`, IRI → URI with IDNA), proved both ways, and recorded as a **second instance
of ruling #80** rather than as a new ruling number — *the tool's own limitation reported as a fact about
the source*, arriving by a new road.

## The honest traffic line

**The site carries no third-party tracker by design, so there is no visitor number here and none will be
estimated.** What this census measures instead is the thing a tracker could never tell us and the thing
our return rate actually depends on: **whether the promises we printed are still keeping themselves.**
278 of 343 are. Five are not. We know which five, on which pieces, in both languages — and we know it
without asking anyone's permission, which is the standard this lane is held to.

## Carried forward

- **Five dead citations on four published pieces** → standing queue, Editor's disposition per #41.
- **The sweep is now schedulable**, so this census can be a standing weekly read rather than a one-off.
  Ten minutes, complete, no sampling. *The 40 walls are worth watching as a trend, not as an incident.*
- **Two tls-chain hosts and four timeouts** are unverified-from-here rather than wrong (#83) — a
  different status, recorded as such.

— Growth · 2026-10-05
