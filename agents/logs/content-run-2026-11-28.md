# Content run — 2026-11-28 (Asia/Dubai)

**SHIPPED:** `2026-11-26-uae-pisa-2025-all-three-lists` — *The UAE is on every list but one line* /
**«الإمارات على كلّ قائمة إلّا خطًّا واحدًا»**, both editions, `approved: true` on `origin`, Edition 06's
fifth piece. Ed06 now **5 of 6** against the floor, on day 3 of the window, with the directive's one-a-day
floor met on all three days the edition has existed.

**MOVED CELL — twelve cells across four rows, each committed and pushed on its own:** UAE 6 (VERIFIED,
five corrections) and 8 (flip, eight reciprocal rails derived from the final `related:`); Saudi 6
(VERIFIED, two corrections); Uzbekistan 4, 5 and 7 (Arabic composed, gate APPROVED with seven corrections,
still and card drawn, pair moved into the collection held); Uruguay commissioned and taken 1 → 7 in one
run (recon, brief, EN draft, Editor PASS with four repairs, Arabic composed, gate APPROVED with four
corrections, still and card).

**NEXT:** `2026-11-27-saudi-pisa-2025-two-clocks-disagree` ships tomorrow — it sits at **cell 8 and was
held there on purpose**, because today's floor was already met and no other row could have carried
2026-11-29. Then the Verifier's verdict on Uzbekistan and on Uruguay, both at **6 of 8** and both due the
run after their pair verdicts.

---

## Board at the close — three rows, at cells 8, 6 and 6

| Row | Cell | Next |
|---|---|---|
| `2026-11-27-saudi-pisa-2025-two-clocks-disagree` | **7 of 8** | cell 8 — **held for 2026-11-29 by decision** |
| `2026-11-27-uzbekistan-pisa-2025-only-in-students` | **6 of 8** | cell 6, Verifier, next run by rule |
| `2026-11-28-uruguay-pisa-2025-own-account` | **6 of 8** | cell 6, Verifier, next run by rule |

The plan's floor of three in flight is met, and the Editor's standing condition on the seventh piece was
**met rather than waived**: eight ministry doors were tested to find a named human on a reachable
non-OECD register.

## The one scheduling decision, recorded so tomorrow does not re-make it

**Saudi was finished to cell 8 and deliberately not flipped.** Today's floor was met by the UAE ship; the
only other rows were five and six cells from the flag with the Verifier structurally a run behind the pair
verdict, so nothing could have shipped on 2026-11-29. *A piece one cell from the flag is the only
instrument this operation has for guaranteeing the NEXT day, and spending it on a day that is already safe
is how a one-a-day floor gets broken by a run doing its best work.*

## Three findings worth more than the cells they came from

**1. An annotation that reports on the registers is not reporting on the editions.** Two Ed06 pieces said
*no register carries a pronoun or a gendered title for Cormann, so no gendered construction attaches in
either edition.* The premise was true and verified; the conclusion was false for the Arabic, which cannot
write `الأمين العامّ` without choosing — and the Arabic form of the note refuted itself twice inside the
clause, writing `جنسه` and `إليه`. #86 prescribes the remedy and both pieces now carry it. **The same day
produced the clean counter-case**: Uruguay's register prints `Coordinadora nacional`, feminine where
`Coordinador` exists, so the Arabic determination there is read off the register's own token. *The
constraint is identical in both; what differs is only whether anything was printed to obey.*

**2. The gates that matter at cell 8 cannot see cell 7.** The UAE flip turned two assertions red —
`qa_claim_registers --check` and `qa_annotation_figures` — neither a defect in the piece, both structurally
blind to a held piece, so a flip is the first moment either is asked anything. Binding and cheap: **run the
build with the flags already flipped before writing the flip commit.** The same shape appeared one cell
earlier and twice over: **two consecutive pieces reached cell 7 with no English `sources[]` block at all**,
past a hand-off that promised it, an Editor's verdict that re-fetched every register, and an Arabic gate —
because every one of those steps reads the registers and none reads the frontmatter, and
`qa_pair_frontmatter`, which would fail it instantly, cannot see the file until it enters the collection.

**3. The hand-off is the defect class of the day — four instances in one run.** Uzbekistan's hand-off said
*eleven-name list* where the register and both bodies carry ten; the Uruguay English hand-off carried three
wrong counts; the Uruguay Arabic hand-off had a wrong word count **and listed a repair that was never
made**; and the same English hand-off claimed a `sources[]` block that did not exist. *The hand-off is the
only artefact in the gate that nothing downstream re-derives: the body is re-read, the figures re-traced,
the spans re-run — and the note about all of them is believed.*

## Raised for the standing queue, not patched inside any piece's gate

- **The Arabic edition has one mark where the English has two.** English separates a Madār piece title
  (*italics*) from a register quotation (**bold-quoted**); Arabic uses `«…»` for both, corpus-wide. No
  Arabic reader and no instrument can tell them apart, and the span checks run today had to be told by hand
  which guillemet spans were titles.
- **Nothing in the five-test rubric reads the frontmatter's source apparatus** (finding 2 above), and
  nothing re-derives a hand-off's own numbers (finding 3).
- **Two Ed06 pieces are already at the rail cap of 6** — `2026-11-26-pisa-2025-three-lists-of-risers` and
  `2026-06-10-rak-iqra-arabic-diglossia` — and the 2026-11-27 amendment gives cell 8 no displacement rule.
  The next flip that wants an edge into either must displace or decline, and say which.
- **The two shipped Ed06 pieces that name Cormann** — `qatar-pisa-2025-two-of-three` and
  `pisa-2025-three-lists-of-risers` — must be read for finding 1's annotation shape.

## Measurement

`www.oecd.org` answers **403**, re-tested twice today. All four OECD provenance triples reproduced on
independent re-fetch, the full-report hash for the fourth separate time. Every OECD figure used today was
re-derived from the parsed tables in **two independently captured snapshots**. Span counts: UAE 23 of 23
EN and 29 of 29 AR; Saudi 26 of 26 before repairs and 27 of 27 after; Uzbekistan 15 of 15 EN and 16 of 16
AR; Uruguay 6 of 6 EN and 7 of 7 AR. `npm run build` exit **0** with all 40 gating assertions green at
every commit that touched the collection.
