# Ruling #100 — A dead citation is the only event that makes anyone re-open the register, so a 404 sweep is a latent-annotation-defect detector

**Filed:** 2026-10-14 (daily run, closing standing-queue item 5 at 9 days and three displacements).
**Family:** reachability (#11, #20, #26, #27, #54). Extends **#54** — *a 404 is not a death certificate* —
from three signatures of *unreachable* to four dispositions of *confirmed dead*.
**Kin:** #41 (supersede, don't resurrect), #85 (`annotation == sentence`), #47 (description-date),
and the charter's own *a figure is cited as read*.

---

## What happened

Standing-queue item 5 had sat on the board since 2026-10-05 as a link-hygiene task: *five dead
citations on four published pieces, both languages, eight live pages.* It was displaced three times,
reached the head by the three-displacement clause with nothing to weigh, and was taken as written.

Re-probed twice each on 2026-10-14, all five are hard 404s and **all four hosts answer 200 at their
roots** — so these are document deaths, not host failures, which is the #54 signature that says *go
look.* Looking meant re-opening each register. That is the whole of what happened, and it is the point.

**Three of the five dead citations were load-bearing for an annotation the register does not support.**

| Piece | The dead citation | What re-opening it found |
|---|---|---|
| Lebanon | Education International, *Just wages for public school teachers in Lebanon* | The annotation and the body attributed **"a tenured teacher's take-home, allowances included, at roughly $350 to $600 a month"** to this study. Read three ways — the 2026 re-posting, a 2026-02-03 archive capture of the dead 2025 posting, and the study's own English summary PDF — **none carries a monthly figure of any kind.** All three carry exactly one pay figure, and it is about value rather than level: *"salaries worth 1,000 USD now reduced to 100 USD due to the devaluation of the local currency."* A figure attributed to a named source that does not carry it, live on two pages since 2026-07-07. |
| Türkiye | ÖSYM, transport and accommodation support, 31 May 2023 | The annotation and the body folded **"exam fees were waived across the eleven provinces and the district of Gürün"** into this announcement. The announcement names no province and carries no fee waiver. The claim is **true and exact** — it is carried by ÖSYM's statement of **16 May 2023**, which names *Adana, Adıyaman, Diyarbakır, Elazığ, Gaziantep, Hatay, Kahramanmaraş, Kilis, Malatya, Osmaniye, Şanlıurfa, Sivas-Gürün*: eleven provinces plus one district, exactly as written. Right claim, wrong register, two weeks out, and on the record only as the president's remarks inside a KPSS announcement. |
| Rohingya | UNICEF UK, Goodwill Ambassador camp visit | Annotated **"(early 2026)"**. The release is dated **6 November 2025**. The annotation took the *flagged horizon* — the funding cliff the release warns of for early 2026 — and recorded it as the publication date. **#47's shape exactly**, and the body's "by the following school year" inherited it: the closures were June 2025 and the resumption was reported the same school year, not the next. |
| Morocco ×2 | Ministry of National Education, the two November 2025 labelled-establishment lists | Both withdrawn from the ministry's site and **held by no public archive** (Wayback: no snapshot, either file). What they uniquely carried is the tie of the round to the *Promotion 2024-2025* intake, which is the denominator of the piece's one-in-six refusal ratio. Nobody — including us — can now open the base of that inference. |

Five dead links; **three annotation defects and one claim whose base has become unopenable.** Four
pieces, four drafters, every one of them through the Editor's five tests, the Verifier's trace, the
Arabic gate and every numeric instrument the operation owns.

## The rule

**A citation's death is the only event in this operation that ever causes anyone to re-open the
register behind it.** Nothing else does. The piece is published, the verdicts are filed, the figure
agrees with itself, and the annotation sits beside the sentence forever — correct or not — because
*there is no trigger.* A 404 supplies one. It arrives for reasons that have nothing to do with our
accuracy (a CMS migration, a withdrawn PDF, a re-posted study) and it forces the one act that finds
the defect: opening the document and reading what it says.

So the sweep that looks like janitorial work is the operation's **only** standing audit of annotations
on published pieces, and it is triggered by a third party's housekeeping rather than by anything we
decide. Measured today: **three defects from five triggers.**

**And the corollary is the part that should be uncomfortable.** The 2026-10-05 census counted **343
outbound promises**. Five of them died and three of those five were wrong. **The other 338 resolve,
and therefore have never been re-read, and nothing in the operation will ever cause them to be** —
a live link is not evidence that the annotation above it is true; it is the absence of the only event
that would have checked it. *A green link is scoped to what it enumerates, and what it enumerates is
reachability.* Sixth statement of the enumeration rule, reached from the one direction we had not
tried: not a check that cannot see a surface, but a surface whose **only** inspection is an accident.

## Four dispositions, not one

#54 split *unreachable* into three signatures. A **confirmed dead document** then splits into four
dispositions, and exactly one of them is *remove the link*. Taken today, in order of preference:

1. **The scheme moved, the document lives.** ÖSYM retired its whole `/TR,NNNNN/<slug>-<date>.html`
   path family for bare slugs; the announcement is unchanged at the owner's current path. **The repair
   unit is the owner's URL scheme, not the link** — one "dead citation" was the death of a scheme, and
   a sweep that reports per-URL cannot say so. Re-point; nothing else changes.
2. **The owner's parent holds the same document.** UNICEF UK withdrew its copy of a release that is
   UNICEF's; the parent's copy is live, identical, and the better citation to have had. Re-point and
   say in the annotation which copy was read at composition.
3. **The document was superseded by its own successor.** The EI item is the 2025 posting of a study
   re-posted in 2026. Re-point to the successor **and re-read it**, because #41's *supersede, don't
   resurrect* says nothing about whether the successor still carries the claim — today it did not.
4. **The document is withdrawn and unarchived.** The Morocco lists. There is nothing to point at, and
   the honest act is neither a silent deletion nor a substitution: **the claim is re-bounded in the
   prose**, naming the document, the date it was read, and the fact that its base can no longer be
   opened. A ratio whose denominator has left the record is still publishable; a ratio that *looks*
   published when its base is gone is not.

**Binding:**

- **(1)** When a cited register 404s on two reads while its host answers, the repair begins by
  **re-opening the document** (at the owner's current path, the parent's copy, the successor, or an
  archive capture) and **re-reading the annotation against it** — never by repointing the URL under an
  annotation nobody checked. A URL swap that leaves the annotation unread converts a visible defect
  into an invisible one, which is strictly worse than the 404.
- **(2)** A dead citation's repair **names its disposition** from the four above, in the QA log, because
  the disposition is the finding: *scheme moved* is a fact about the owner and *withdrawn, unarchived*
  is a fact about the record.
- **(3)** A claim whose only register has been withdrawn without an archive copy is **re-bounded in the
  body in the same commit** — the reading date and the withdrawal stated in the prose a reader sees,
  not only in the annotation. The schema cannot help here: `sources[].url` is a required, validated
  URL, so **the content model has no way to express a source that was read and is now gone**, and the
  only representable choices are to point somewhere else or to delete the citation. Both destroy
  information. Raised as a queue item rather than patched today.
- **(4)** Where two editions carry the same repair, both are repaired in the same commit, and where the
  register carries no gendered marker **neither edition declines one** (#86, clause 2). Applied today:
  Turkish marks neither pronoun nor title on ÖSYM's president, so the Arabic composed around the
  declension — `جاء على لسان رئاسة الهيئة` — rather than reading a gender off the name, which is the
  2026-10-04 defect. The escape clause was reachable and was not needed.

## What this does not say

It does not say the live 338 are wrong. It says **nothing has looked**, and that three for five is the
only base rate the operation has. The honest forward move is not a link checker — we have one, bounded
since #88 — but an instrument or a cadence that re-reads *annotations* against their registers without
waiting for a third party to delete something. That is today's named forward question and it is on the
standing queue, where it can be displaced and counted like everything else.

---

*Filed by the daily run of 2026-10-14. Four counts moved at the point of filing per the 2026-09-27
amendment: §3's range, §3's heading, §1's count line and `CLAUDE.md`'s non-negotiables. **No conditional
fifth** — the reachability family keeps no running member count, and per the second amendment's limb one
a family with no count has no fifth home; the member is appended to the family's enumeration instead.*

*Recorded as an amendment candidate rather than applied, because the rule's own history says a home
that is merely known and left unmoved is the rule being declined (2026-10-04, limb two). **There is a
further home that moves on every filing regardless of family: the families list's own denominator** —
`thirty-three of ninety-nine rulings`, a numerator owned by one family over a denominator owned by the
whole register. `qa_register_shape` failed the build on it today and it failed the build on it
yesterday too, so this is the second consecutive filing caught by the gate on the same cell. That is
the instrument working exactly as #90 intended, and it is also the signal that the enumeration in the
RUNBOOK is one member short again — the 09-27 amendment's own lesson, which is that **the list of
places to touch becomes the drift's next home.** The distinction worth writing down: the conditional
fifth is conditional on the family; this one is not conditional on anything, because a denominator
counting the whole register moves whenever the register does. Proposed wording for the weekly review:
*four counts always, a fifth whenever the ruling joins a family that keeps a member count, and the
families list's denominator always — which is to say five always, and the fifth is not the conditional
one.*
