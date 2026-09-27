# Rwanda (Ed05 row 6) — MINEDUC's own channels, enumerated; and the host that stopped serving a reader

**Date:** 2026-09-27 · **Daily run (Researcher lane) → Editor** · addendum to the 09-24, 09-25 and 09-26 recons
**Status: BLOCKER 3 CLOSES. The A2→A1 absence is UPGRADED from "not found on eight routes" to an enumeration. One NEW finding about the host, which changes no figure and changes every annotation.**

This was not a scheduled recon. It is what happened when the draft lane did the thing #69 asks for —
*prefer the publisher's own dated enumeration to a search* — and probed its own source URLs before the
piece carried them. **Fourteen days to the 10-11 gate target.**

---

## 1. THE HOST: `mineduc.gov.rw` has been refusing a correctly-behaving client since 23 September

Six of this piece's eight registers live on `mineduc.gov.rw`. All six returned nothing today. The
cause was read off the handshake rather than guessed at:

```
subject = CN = mineduc.gov.rw      issuer = C=US, O=DigiCert Inc, CN = RapidSSL TLS RSA CA G1
notBefore = Sep 24 00:00:00 2025 GMT
notAfter  = Sep 23 23:59:59 2026 GMT
```

**The certificate expired on 23 September 2026.** With verification disabled every one of the six
returns **HTTP 200**, and the 2024/25 yearbook returns **4,023,048 bytes** — byte-for-byte the count
the 09-26 recon recorded, which is an independent confirmation of that read from a different day and a
different client. Nothing about the documents changed. Nothing about the figures changed.

**What did change is what a reader can do.** Any mainstream browser now shows a full-page security
interstitial before this ministry's statistical annual, its salary communiqué, its reforms release,
its project progress note and its news index.

**And our own record already said otherwise, three times.** The 09-24 re-verification records three
MINEDUC registers as *"200, unchanged."* The 09-25 hunt reads four MINEDUC pages in served text. The
09-26 recon records the yearbook at *"HTTP 200, 4,023,048 bytes."* All three ran **after** the
certificate expired. No figure in any of them is wrong and every one still stands; what is wrong is
the serving-state column, and it is wrong in the direction that matters — it says a reader could reach
these registers on days a reader could not. **Filed as ruling #70**, together with the change to
`qa_sources_alive` that makes the distinction sayable.

**Disposition, and it is not a supersession (#54).** The registers stay. Each of the six MINEDUC
annotations in the draft now states the certificate's expiry date, that the document is still served,
and that a reader meets an interstitial. An expired certificate is the single most likely of these
failures to be repaired by somebody else within days, which is exactly why it is recorded with its
date rather than written down as a death. **Re-probe owed at the confirmation read.**

---

## 2. BLOCKER 3 — **CLOSES**, 40 days open, by the route the recon named twice and nobody had tried

The 08-18 recon and the 09-24 re-verification both name the same unattempted route: *"the MINEDUC
news index's ordering."* The reason it was never tried is recorded in the 09-25 hunt as route 7 —
`mineduc.gov.rw/news` returns **404**. **The index is at `/updates/news-2`.**

It is reverse-chronological, ten items to a page, **35 pages**, running back to **21 May 2018**. The
QBE progress note is on **page 3**, and the items around it are strictly descending:

| Item, in the index's own order | Date the index gives |
|---|---|
| The Ministry of education introduces new reforms… | Monday, 10 August, 2026 |
| ALX, Anthropic and the Government of Rwanda launch… | Monday, 17 November, 2025 |
| Rwanda's higher education emerges as innovation leader | Wednesday, 05 November, 2025 |
| **MINEDUC & World Bank report 13 model schools, 11,000 classrooms, and 621 resilience upgrades…** | **Wednesday, 05 November, 2025** |
| Minister Irere hails GS Ruhango ADEPR… | Thursday, 30 October, 2025 |
| …and on, monotonically, to Friday, 03 October, 2025 |  |

**The pairing method is proved on a control inside the same list**, which is why it is trusted at all:
the index dates the first item to **Monday, 10 August, 2026**, and that is the date the reforms release
prints **on its own page** — read there on 09-24 and again on 09-25. The method is shown correct on the
one item in the list whose date is independently known.

**The scope of what closes, stated narrowly.** The article page **still serves no date of its own** —
re-read today, and every date string on it belongs to the sidebar's latest-news rail, not to the
article. So the date is **the index's, not the article's**, and the draft's annotation says exactly
that. It is enough for the 11,000-classroom figure that anchors ruling #32 to stop being undated; it
is not the article acquiring a dateline.

---

## 3. The A2→A1 absence — **UPGRADED from a hunt to an enumeration**

The 09-25 hunt stated its own limit honestly: *"the ministry's news index did not serve at the obvious
path, so the MINEDUC corpus could not be enumerated by date — four named pages were read, not a list.
A future run with a working index path should re-ask."* This is that run, and the path works.

Re-asked today, across all four of the ministry's publication channels on its own domain:

| Channel | Path | Shape | Newest item |
|---|---|---|---|
| News | `/updates/news-2` | 35 pages, reverse-chronological, 10 per page, back to 21 May 2018 | **Monday, 10 August, 2026** |
| Speeches | `/updates/speeches` | PDF library | **December 2024** |
| Press releases | `/updates/press-releases` | PDF library | **November 2024** |
| Announcements | `/publications/announcement` | image library | **January 2026** |

**MINEDUC's news channel carries nothing at all after 10 August 2026.** No release for the 20 August
2026 results ceremony at which the State Minister announced the upgrade window, and no register for the
window itself. The other three channels end earlier still, and none mentions A1, A2 or an upgrade.

**This is an enumeration, and it is still not a verdict.** Four channels on one domain are not the
whole of a state's voice: REB has its own site, the cabinet publishes elsewhere, and a ministerial
instruction may live in an official gazette this run did not read. **What can be said flatly is what a
reader can reach** — and it is now a much stronger statement than the 09-25 hunt could make, because
it rests on the publisher's own dated listing rather than on the routes we happened to try. That is
#69 executed rather than cited.

**Consequence for the commission: none.** The Editor's ruling 3 stands untouched and is now better
supported. The upgrade window remains one attributed sentence in the body, carrying The New Times and
24 August 2026 in the same clause, and does not carry the close.

---

## 4. Two source details confirmed while probing, recorded because they are cheap and load-bearing

- **The New Times / allAfrica register is live and unchanged.** `allafrica.com/stories/202608240232.html`,
  HTTP 200, headline *"Rwanda: Teachers With Secondary Education Given Five Years to Attain A1 Diploma"*,
  **by Shallon Mwiza, 24 August 2026**. The speech-dating licence (#62) holds on a third read; the quote
  is verbatim as the 09-25 hunt recorded it; and re-asked directly, the article still cites **no written
  ministry document** and states **no number of teachers affected**. It also carries the two-phase
  sequence (A2→A1, then A1→A0) as part of a ten-year plan, attributed to *officials* — reported speech
  about reported speech, and the draft does not use it.
- **The World Bank feature is the only register in this piece whose host serves a valid certificate.**
  HTTP 200, unchanged.

---

## 5. What this addendum does NOT close

- **The funnel** (enrolled / sat / passed / still uncertified). Unchanged and unpublished; the route-2
  precedent (#11) applies and the draft states the absence in print.
- **NESA's own Wave II announcement** on `nesa.gov.rw`. Not attempted today. The draft is written so
  that it does not need it: the duration is carried as April 2024 → March 2026, from two registers that
  were read, rather than as the October 2025 Wave II date that reaches us only through an aggregator
  mirror. Recorded so the omission is not later read as an oversight.
- **Umwalimu SACCO's membership figure at source.** Not attempted; not in the draft.

— Daily run (Researcher lane) · 2026-09-27 · Ed05 row 6 · East Africa
