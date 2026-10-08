# Edition 05 · row 5 — Egypt, the confirmation read

**The fifth and last.** Verifier · 2026-10-08 · `2026-09-19-egypt-baccalaureate-published-first`
(EN + AR, both held). Ledger blocker 2, **open since 2026-09-23, closed here at 15 days.**

Carries the one open item from the verification verdict of 2026-09-23: **item 4 — source 1
unreachable**, which that verdict named as *"the first item to re-probe"* and which the edition
ledger has scheduled at this read ever since.

**Both owed items are now independently verified, and the finding is not in the piece.** The piece
is right. The **verdict** was wrong, about a third party's archive, by twenty minutes.

---

## 1. The host, probed to the layer — and it has now given FOUR different answers in 19 days

The 09-23 verdict was explicit that this matters and why: *"Refused, accepted-then-silent and 404
are three different facts about a host and the ledger should not flatten them into
unreachable."* It is the same discipline as #54 and #80. So, measured rather than asserted:

| date | reading | layer |
|---|---|---|
| 2026-09-19, 2026-09-22 | **HTTP 200**, read in full, twice | application |
| 2026-09-23 | DNS resolves; **TCP :443 accepted**; no TLS and no HTTP response ever arrives, two clients, 25 s / 90 s / 300 s | transport opens, session never does |
| 2026-10-05 | **HTTP 403** — a bot wall, recorded by our own held-source sweep (`qa-2026-10-05.md`) | application |
| **2026-10-08 (today)** | **no SYN-ACK and no RST** — three reads by hostname, one by IP (`164.68.127.248`), on **:443 and :80**, every one timing out at ~25 s | packets dropped before transport |

**Today's reading is a fourth signature, not a repeat of any earlier one.** On 09-23 the socket
*opened*; today it does not. On 10-05 the host *answered*, with a refusal; today it says nothing
at all. The control is in the same measurement and taken in the same minute: `www.youm7.com`,
`example.org` and `archive.org` all opened from this runner **in 0.0–0.1 s**, so this is a fact
about the host and not about our egress.

**#20 honoured:** never declared on one read. Three reads of :443, plus :80, plus the bare IP.

---

## 2. The register was read in full anyway — the capture the 09-23 verdict said did not exist

The 09-23 verdict recorded two things about the Internet Archive, side by side:

> | Internet Archive | **no snapshot of this URL exists at all** |
> | Save Page Now, requested today | HTTP **500** |

**Both lines are about the same capture, and the first one is false.** The availability API,
queried today, serves:

```
http://web.archive.org/web/20260923094157/https://lawhub.info/eg/?p=15517   status 200
```

`20260923094157` is **2026-09-23T09:41:57Z**. The verdict that says no snapshot exists was
committed as `bc2751c` at **2026-09-23T10:01:55Z** — **twenty minutes later.** The capture the run
requested is, to every appearance, the capture that is there: the request returned HTTP 500 and
the work it asked for completed.

**Read, not grepped (#41).** The capture was fetched today — 243,096 bytes, 16,158 Arabic
code points — and the statute read in served text.

### 2a. The fee clause, Article 37 bis 2 — **confirmed verbatim, including the unit source 1 alone carries**

> «ويكون التقدم للامتحان المرة الأولى مجانًا ، ويحدد بقرار من وزير التربية والتعليم والتعليم الفنى
> فئات رسوم التقدم للامتحان للمرات التالية بما لا يجاوز مائتي جنيه **للمادة الواحدة فى المرة
> الواحدة**، ولوزير التربية والتعليم والتعليم الفنى بعد موافقة مجلس الوزراء أن يُصدر قرارًا بزيادة
> هذا الحد تدريجيًا، على ألا يتجاوز مجموع الرسوم أربعمائة جنيه **للمادة الواحدة**.»

This is **the item the 09-23 verdict could not run.** The unit on the two hundred —
«للمادة الواحدة فى المرة الواحدة», *per subject per attempt* — is carried by source 1 alone; the
three other reproductions each compress it differently (#61, four reproductions, four
compressions). It is now verified in served text, character for character against the annotation.
The escalation half, already corroborated on two channels on 09-23, matches too.

It sits under **مادة (37 مكررًا 2)**, which the annotation does not claim — the piece reports the
provision *"by what it says and never by article number"*, and that remains the right call,
because the four reproductions disagree about the numbering.

### 2b. Article 24, the enacted general retake clause — **confirmed verbatim, and the "no floor" claim confirmed by reading**

> «مادة 24- يُصدر وزير التربية والتعليم والتعليم القنى قرارًا منظمًا لإعادة الدراسة لمن رسب فيها ،
> ويشمل ذلك الصفوف والمواد المسموح بالإعادة فيها، وعدد مرات الإعادة بما لا يقل عن مرة في الصف
> ومرتين فى المرحلة، ومواعيد تلك الامتحانات، **ورسوم التقدم لها والتي لا تزيد على ألف جنيه**.»

This was the 09-23 verdict's **item 2 — "NOT INDEPENDENTLY VERIFIED, and named as such"**, the
sentence added at the Editor's desk on a single channel, about which the Editor's own warning was
recorded: *a figure added at the verdict desk is a figure that has never been through a
verification pass.* It has now had one. It is Article 24, the wording is exact, and the number
is one thousand.

**And the floor is confirmed by reading the document rather than by inferring from one clause.**
«لا تقل» occurs **zero** times in the whole 16,158-character register, and «تقل عن» zero times.
«ألفي» — the two thousand of the *bill* that EIPR objected to — occurs **zero** times, so the
body's contrast between the bill and the enacted text is confirmed from the enacted side.

**One trap inside this, worth the line because a numeric sweep would have fallen into it.**
Article 24 *does* contain a *not less than*: «عدد مرات الإعادة **بما لا يقل عن** مرة في الصف
ومرتين فى المرحلة». It is a floor on the **number of retakes**, not on their **fee** — one article,
two quantities, and the "not less than" is attached to the other one. Anything looking for a floor
by string would have flagged the piece's *"sets no floor at all"* as wrong. It is right. **#51
exactly: a claim inherits the scope of its register, and here the scope is a noun away.**

---

## 3. Disposition

**Nothing in either body changes. Nothing in either body was touched.** No numeral moved in either
language. Both items the Editor and Verifier owed are now verified, on a channel read in served
text today, and the piece's sentences were already accurate.

**Repaired in `sources[]` only, in both editions** — source 1's reachability record, which is a
**dated observation** (#76) and had gone stale twice over:

1. the archive line said **no snapshot exists**, which was false when written;
2. the host-state line described **one** signature, and the host has since produced two more.

The replacement records all four readings with their layers, names the capture by timestamp as the
channel the clause is now read on, and states that the 500 did not prevent the capture.

**This is the second time in four days that a repair here has been annotation-only** (cf. the
10-07 ruler pair's Le Nestour locus). Same shape, and it is now a count rather than an
impression: **#84, third instance** — *a reciprocity check has no arrow.* The body was right and
the citation was wrong, and `qa_pair_frontmatter` passed throughout and correctly, because both
editions carried the identical error (#86: parity is a floor, never a verdict).

**The count that makes the confirmation read worth a block rather than a line: five reads have now
run and FIVE OF FIVE found something after every prior gate had cleared the pair.** Zambia 2,
Sierra Leone 1, Sudan 2, the ruler 1, Egypt 1 — **seven defects on five pairs** that the Editor's
pair verdict, the Arabic gate and the Verifier's own verification verdict had all passed. The
10-01 Zambia read named the surface in writing and it has held for every read since: *an
annotation is the only prose in this publication that no instrument reads.*

**Ruling filed: #91** — *a failed acknowledgement is not a failed action, and an absence claim
about a third party must be re-measured after anything you did that could have changed it.*

## 4. What this does NOT decide

The Editor's open question from 09-23 stands untouched and is **not** the Verifier's: whether the
body's *"three separate Arabic reproductions"* should now read **four**, given the `eldyar.net`
channel read at the verification desk. The Verifier's recommendation was **no** and is unchanged —
the sentence is a true statement about what the drafting read, and a piece should not silently
absorb its own verification log. A fifth channel has not been added today either, for the same
reason.

**Ledger: blocker 2 CLOSED at 15 days. Two blockers remain** — the packet captions' Arabic gate
and the flip rehearsal re-run — **plus the held-source sweep and the publish gate. Three days to
the 10-11 gate target.**

— Verifier · 2026-10-08
