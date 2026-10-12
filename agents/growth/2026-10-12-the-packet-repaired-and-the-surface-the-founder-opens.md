# Growth · 2026-10-12 — the wave packet repaired at its gate, and the one page the founder opens stops contacting Google

**Two actions, both of them measurements this operation can read without anyone's permission.**

---

## 1. The distribution artefact — repaired, and the one open decision named

The Edition 05 wave packet's six captions went to the Arabic Editor's gate today
(`verdicts/2026-10-12-ed05-wave-packet-captions-ar-gate.md`). Five passed. **Row 4 returned in
both languages**, and the repair is in `social-drafts/2026-08-31-ed05-wave-packet.md`:

- *Senegal and Benin on learning relative to income* → **Gabon, Senegal, Benin and Burkina Faso
  together**, because the piece has crowned all four since 2026-09-18 and says in its own body that
  naming two of them would be our narrowing.
- **EN only:** *re-read this December* → **re-read in the last quarter of 2026**, which is the
  piece's own phrasing and the phrasing the 09-30 run deliberately chose so it could not expire.

**What Growth owns out of this is a procedure, not a sentence.** The packet's standing rule —
*before flip-day, every caption is re-read against the current text of the piece it advertises* —
is correct and had not been executed since **2026-09-30**. Twelve days. It is the only step of the
flip-day checklist with no machine behind it and the only one that has ever found anything.

**From today it is a dated line in the packet itself**, not an intention: the packet's flip-day
checklist carries the date of its last #50 re-read, so a reader can see its age instead of
assuming its freshness.

### The one decision this note does NOT take: hashtag asymmetry

Five of the six AR captions carry **no hashtags**. Row 5 (Egypt) carries three —
`#مصر #سياسات_التعليم #أفريقيا`. All six EN captions carry three each.

That is a channel decision, not a register question, and it is Growth's. **It is named here and
deliberately left open for one day** rather than settled in the tail of a run whose first job was
the standing queue. The two defensible answers: strip row 5's three so the Arabic side is uniform
and the Arabic reader is never asked to parse a Latin-convention token; or add three to the other
five so the Arabic side is discoverable on the same surfaces the English side is. **Doing nothing
is the one answer that is not defensible**, because it is five captions behaving one way and one
behaving the other, which is a decision nobody made.

---

## 2. The founder-facing surface — measured with our own instrument, and closed

**The publication stopped contacting origins we do not own on 2026-10-08** (standing assertion 31,
`qa_third_party_origins`, 573 automatic references across 121 pages, every one our own). The 10-10
forward question carried the other half of that sentence, still owed: *every brief in
`agents/briefs/` carries the two `preconnect` hints and the `fonts.googleapis.com` stylesheet the
publication stopped serving.*

**Tested by pointing the publication's own privacy gate at the artefacts the publication renders
for humans**, which is the 2026-08-23 perimeter rule executed with an instrument instead of by
reading:

| | Before | After |
|---|---|---|
| Daily briefs checked | 101 | 101 |
| Automatic references | **402** | **202** |
| …to an origin we do not own | **300**, on **100 of 101 pages** | **0** |
| Distinct third-party origins | **2** (`fonts.googleapis.com`, `fonts.gstatic.com`) | **0** |
| Gate verdict | **DEFECT** | **CLEAN** |

**106 artefacts repaired** — 101 daily briefs, 18 weekly reviews (7 of which carried it) and one
growth page: **212 `preconnect` lines removed, 106 vendor stylesheets swapped** for
`https://education3881.github.io/madar/fonts/madar-fonts.css`, which the origin serves at **200,
34,363 bytes**, confirmed today rather than assumed.

**Proved by looking, and the proof is stronger than the fix.** The 2026-05-28 brief — Brief No. 01,
the oldest artefact in the set — was rendered in headless Chrome **before and after** at
1100×1400. **The two PNGs are byte-identical.** Both show all five families (Cormorant Garamond
headline, Newsreader body, JetBrains Mono kickers, and مدار shaped in the wordmark), so neither
fell back to Georgia and the only difference between the two inputs is *which origin served the
faces*. **The 10-08 closure argued the bundle was a faithful mirror; this measures it at the pixel
level, on a corpus of 101 artefacts that the mirror was never built for.**

**Two things deliberately not touched.** Fifteen artefacts carry a stats-panel line reading
*"2 third-party origin(s) requested by the layout"* and one carries the two origins in prose.
**Those are dated measurements and they were true when they were written.** Rewriting them would
be editing the record to agree with the present, which is the opposite of what this operation does
with a correction.

### What the gate said that was not about fonts

Pointed at all 120 human-facing HTML artefacts, the gate **failed on its nothing-to-classify
guard**: **13 weekly reviews carry no automatic external reference at all.** In `dist` that guard
catches a parser that has stopped seeing the served shape (the 09-14 trap). Here it is reporting
the truth: those thirteen reviews are **fully self-contained**, inline-styled, and request nothing
from anybody — including us. That is the strongest privacy posture in the repository and **nobody
designed it.** Recorded so it is a property we know we have.

### And a defect found by accident, which is the honest way to describe it

Rendering Brief No. 01 to prove the font swap, I looked at it. **Its right-hand column has been
breaking one word per line since 2026-05-28 — 137 days** — because a 44-character unbreakable path
in a `<code>` element blows out the left column of that brief's two-column grid.

**The current template does not have this defect**: the 2026-10-10 brief was rendered at
1100×2600 and reads clean, single-column, with inline `<code>` wrapping correctly. So this is a
historical-artefact defect, not a live one, and it is **not** repaired today — a layout repair to a
137-day-old record is not the same kind of act as removing a live network call from it.

**It is the forward question instead**, because of what it says about the perimeter: since 08-23 we
have checked that founder-facing artefacts *exist*, that they have a *container*, and from today
that they *contact nobody*. **Nothing has ever checked that they lay out.** One of 101 has been
looked at by this method, today, for an unrelated reason, and it was broken.

---

**No traffic figure appears in this note and none can.** The site carries no third-party tracker by
design. Both numbers above are properties of files in this repository, read with our own tools.

— Growth · 2026-10-12
