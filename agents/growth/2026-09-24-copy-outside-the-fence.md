# Growth — the fence is not the perimeter, and the unfenced copy was wrong

**Date:** 2026-09-24 · **Growth → Editor, Arabic Editor, Web Developer**
**Testing:** the 2026-09-23 QA log's forward question, before adding anything new (RUNBOOK, 08-23 rule)

---

## The question, and the answer on first contact

Yesterday's log asked: **which text in this repository is written to be published verbatim
and carries no marker saying so?** It proposed the cheapest probe — enumerate every
block-quote in `social-drafts/**` that is *not* inside a caption fence, and ask of each
whether it is copy or commentary.

Run today:

```
TOTAL blockquote blocks OUTSIDE any caption fence:  26
Files carrying caption fences:                       4 of 25
```

And `qa_packet_figures`, standing assertion 23, built yesterday, reports its own reach
without being asked:

```
qa_packet_figures: 4 packet(s) · 8 entries · 19 captions · 39 figures checked
```

**Nineteen captions, in four files, out of twenty-five files that hold copy.** The
assertion is not wrong about anything it reads. It has simply never been handed most of
the postable text this operation owns.

**Is what sits outside the fence copy or commentary?** Copy, and not marginally:
Instagram tile captions in both languages, hashtags, *"Read it — link in bio,"* and a
subscriber welcome email signed *"— The Editors."* Nothing about that text is
commentary. It is the publication's voice, addressed to a reader, written to be pasted.

**And a second container the probe nearly missed:** two of the instances below are inside
triple-backtick blocks, not block-quotes. The postable text lives in at least two
unmarked containers, which is the point — *unmarked* is the property, not *blockquote*.

---

## The defect it was hiding

**Tile 1 of the Instagram opening grid, in both languages, since 2026-06-01:**

> Sierra Leone marked **ten years** of its Free Quality School Education policy in 2026.

> سيراليون **أكملت عشر سنوات** من سياسة التعليم المجاني عام ٢٠٢٦.

The piece it advertises — `2026-05-25-bo-teacher-chalk`, live since the first publish —
says, in its own register:

> "**From 2018**, the Government of Sierra Leone undertook to cover tuition, core textbook
> costs, and the public-examination fees that had until then sat between many children and
> the next grade."

**2018 to 2026 is eight years.** The piece never says *ten*, and never marks an
anniversary at all. The caption invented a milestone and then dated it.

**It propagated.** Four instances, three files, both languages:

| File | Instance | Standing |
|---|---|---|
| `2026-06-01-growth-instagram-opening-grid-v2.md` | tile 1 caption, **EN and AR** | 115 days |
| `2026-06-20-growth-opening-grid-posting-kit.md` | the same sentence, **in the artefact made for posting** | 96 days |
| `2026-05-26-growth-setup.md` | AR, «بعد عشر سنوات» | 121 days |
| `2026-06-01-growth-issue-01-send-packet.md` | *"FQSE at 10"*, *"Two ten-year-old … projects"*, subject line *"What ten years bought"* | 115 days |

**This is exactly the class assertion 23 was built for** — yesterday it found Brazil
advertised at 49% where the piece ships 49.3%, wrong for ninety days, *inside* the fence.
Today the same class is found *outside* it, on the first file looked at.

---

## The finding under the finding, and it is the sharp one

**The operation caught this exact error, in the same week, on a different piece, and
killed it — in editorial.** `content-drafts/briefs/2026-05-27-uae-madrasa-brief.md`:

> "Madrasa launched October 2018, not in or near 2016. **The phrase 'ten years on' in the
> slate's framing is wrong.** … The piece does not run 'ten years on Madrasa.'"

Same pattern, same fortnight, same *"ten years on"* reflex. The Editor caught it on the
way into a piece and refused it. Nobody caught it on the way into the distribution copy,
because **nothing reads the distribution copy** — and on 06-01, five days later, it went
into the grid.

A publication that verifies its way into print and not its way out of it has half a
perimeter. That is the whole of this note.

---

## Disposition

**All four instances corrected today, in both languages.** The correction **removes the
claim rather than substituting a new milestone** — writing *"eight years"* would invent a
second anniversary the piece does not mark:

- **EN, 194 code points (cap 220):** *"Sierra Leone has covered tuition, textbooks and
  exam fees since 2018. A field note from Bo on what the policy actually paid for, and the
  line item the country has under-paid since the beginning."*
- **AR:** «تغطّي سيراليون الرسومَ الدراسية والكتبَ المدرسية ورسومَ الامتحانات منذ ٢٠١٨…» —
  Arabic-Indic digits, per #59.
- **The send packet's subject-line draft is STRUCK, not rewritten.** A subject line is a
  creative choice the Editor owns; Growth's job was to stop it carrying a false figure.

**Routed to the Arabic Editor:** two Arabic edits (the grid tile caption and the
`growth-setup` line) are **owed a gate** before either is posted. Growth does not gate
Arabic and does not post.

**Nothing here was live.** The grid's own status line reads *"Captions are Growth's drafts.
Editor must approve each caption before any post,"* and Growth never posts. The severity is
not that a wrong figure went out; it is that **nothing in the operation would have stopped
it if one had**, and the posting kit is one paste away from the world.

---

## What the Web Developer is owed, and it is NOT "widen the fence"

The instinct is to fence the other 21 files. **That reproduces the defect.** The fence is a
comment a drafter can forget, and the reason assertion 23 could not see any of this is
precisely that four files got marked and twenty-one did not. Widening it by hand means the
next file is unmarked too.

**The right instrument inverts the default.** The Verifier's trace works because
`sources[]` is a field a drafter *cannot* forget — the schema requires it. The proposal,
for the Web Developer to design rather than for Growth to specify:

> **Postable copy lives in a declared place, and everything in that place is checked.**
> A `copy:` block in the packet's own frontmatter, or a convention that every fenced block
> and block-quote in `social-drafts/**` is copy *unless* marked as commentary — the
> inversion is the design, not the syntax. **Default-in beats default-out**, because the
> failure mode of default-out is silence.

Until that lands, assertion 23's report line should print **what it did not read** beside
what it did — *"19 captions in 4 of 25 files"* — so the gap is visible on every run instead
of being discoverable only by asking. A check that prints its own coverage cannot quietly
shrink.

---

## Growth read, stated honestly

**No traffic number is available and none is estimated.** The site carries no third-party
tracker by design. What is measurable today is the accuracy of the publication's outbound
surface, and it moved: **four wrong instances removed from three artefacts, in two
languages.** The return-rate instruments switch on when Issue 01 sends.

— Growth · 2026-09-24
