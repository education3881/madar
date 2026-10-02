# Edition 05, row 2 — Sierra Leone (SLEIC outcomes): CONFIRMATION READ

**Filed:** 2026-10-02, by the Verifier. **The second of the five owed at the gate**, after Zambia's on
2026-10-01. Three remain: Sudan, slot 3, Egypt.
**Pair:** `2026-08-28-sierra-leone-sleic-outcomes` (EN + AR).
**What this read owed, per the ledger:** the unmarked emendation (09-09 item 1), the superseded launch
date (09-09 item 2), and the Save the Children blog's 404 — *supersede or carry as fetched-on-date*.

## RESULT: **ALL THREE OWED ITEMS CLOSED · ONE NEW DEFECT FOUND AND FIXED IN-RUN IN BOTH LANGUAGES · ONE CARRIED UPGRADE STILL OPEN, BLOCKED ON OUR CLIENT**

Body prose was **not touched in either language.** EN **1,592** words, AR **1,343** — both unchanged,
no numeral moved in either direction, no waiver sought. Every edit is in `sources[]`.

---

## §0 — The source sweep, with the client named (#80)

`curl 8.5.0`, **TLS validation enabled** (no `-k`), redirects followed, 2026-10-02 14:43 Asia/Dubai.

**All eight URLs serve 200.** Zero unreachable, zero walled, zero 404. This is the first piece in the
edition to sweep completely clean, and it is the piece whose source sweep has been the most troubled —
source 3 produced ruling #54 three weeks ago.

**One of the eight redirected, and that is where the day's finding was.** See §3.

---

## §1 — Item 1 (the unmarked emendation): **CONFIRMED, and attested twice**

The 09-09 fix printed the served word. Re-read today, EOF still serves, verbatim:

> SLEIC does not **definitely** prove that outcomes-based financing is a better way to fund education.

The body carries exactly that, in quotation marks, in English. The Arabic carries «لا يُثبِت إثباتًا
قاطعًا», which collapses both English spellings to one adverb and needed no change — correctly
recorded in September as the edition's first asymmetry arising from the *nature* of the languages
rather than from an error on one side.

**And the 09-09 verdict's own supporting evidence has changed under it.** That verdict argued the page
was typo-prone, citing a second slip on it: *"what is takes to help children learn."* **Today that
sentence reads "what it takes."** The operation cannot distinguish between the page having been
corrected and the verdict having mis-transcribed it, because no verbatim capture was kept — which is
precisely the method defect that verdict identified in the drafter and then committed, a paragraph
later, about its own evidence.

Either reading strengthens the conclusion rather than weakening it: **this register is maintained, so a
quotation from it is a reading with a date, not a property of the page.** Both annotations now carry
both read dates and the reason the second one exists. That is #80's discipline applied to prose rather
than to a certificate.

---

## §2 — Item 2 (a January plan carried as a live future): **CONFIRMED, and it has aged well**

EOF's early-childhood programme page, read today: status **Running**, term **2026–2029**, and its news
rail has grown by **four** items since the 09-09 read (*Early returns* 09 Jun, *Moved by outcomes* 15
Jun, *Beyond programmes* 16 Jun, *Rigour meets reality* 22 Jun) beside the April launch item that
settled the question in September.

The body says the successor is one *"that its own programme register now lists as running"* — a
**status**, carrying no date and no figure, exactly as the fix intended. The decision not to print
"April 2026" or "2026–2029" has paid off twice over: a launch month would now be competing with five
dated news items on the owner's own page, and the pair would be carrying two numerals for a sentence
that is not load-bearing.

**Source 8 of the pair (the programme page, added in-run on 09-09) serves 200 today.** A new claim that
arrived with its own register still has it.

---

## §3 — NEW DEFECT · an attribution read off an account handle

**Where.** `sources[]` entry 8 in EN and its twin in AR — the open analysis repository. Not in the body
of either language.

**It said:**
> Save the Children UK — SLEIC 2025 endline results, open analysis repository (a provider publishing
> the code and data behind its own reported miss)

**The register says.** The owner is a **personal** account. The README describes itself as *"Background
analysis for an SCUK published blog"* and gives a `savethechildren.org.uk` address as the contact. So
the organisation published **the blog** — source 3, correctly attributed, and genuinely the provider
publishing its own miss. The **repository** is a named staff member's working analysis for it. The
annotation promoted an individual's working file to an organisational publication.

**Where the error came from, which is the part worth keeping.** Nothing was fabricated and no research
failed. The handle was `fergalturnerSCUK` — it reads as *Fergal Turner, SCUK*, and it sat on the line
directly below the annotation. Nobody opened the README, because the address already appeared to say
who published it. Then the account was renamed to **`fergal-turner`**, dropping the organisational
marker, and GitHub serves a permanent redirect from the old address. **The rename did not create this
defect. It removed the thing that was concealing it.** Ruling **#84**.

**It passed every gate we own, correctly.** `qa_pair_frontmatter` — shipped yesterday, which asserts
both languages agree about the source URL set and about every fact belonging to the piece — passed,
because the Arabic annotation says «إنقاذُ الطفولة — المملكة المتحدة — مستودعُ...» and the English says
*Save the Children UK — ... repository*, in exact agreement, **on the same error.** Parity is a floor,
never a verdict (#42), and a check whose control is *the two sides matching* is satisfied by a defect
present on both (#78, one surface out).

**And the body was the careful side.** ¶43: *"one of the five organisations being paid published its own
shortfall, in its own words, with its own analysis code attached"* — the organisation published the
post, the code is attached, both true. ¶57: *"the endline analysis sits in a public repository under the
heading 'check our homework'"* — a public repository, no owner named. This is the **inverse** of the
09-13 shape, where the annotation is right and the body smooths it, and it is why #84's corollary
bounds that rule: **a reciprocity check has no arrow.**

**Fix applied in-run, both languages.** The annotation now names the author and his role, states that
the repository is on his own account and not the organisation's, quotes the README's self-description,
records the rename and the redirect, says plainly that the previous wording made a stronger claim than
the register supports, and notes that the body made no such claim. The URL moves to the living address
(#41). **No body prose touched; both word counts unchanged.**

---

## §4 — The Save the Children blog (the ledger's third owed item): **CLOSED**

Source 3 serves **200** at the re-slugged address, with validation enabled, no redirect. Ruling #54's
correction was applied to this file on 09-30 and is correct today. Nothing further is owed.

## §5 — The carried citation upgrade: **STILL OPEN, and blocked on our client, not on the source**

#54's routing left a candidate upgrade: the programme's *Final Learning Report 2026* on Save the
Children's resource centre is a **document** and outranks a blog post on #43's hierarchy.

Probed today. The document page serves **200 / 84 KB**, and its bibliographic text is **not readable by
any client available here** — the rendered fetch returns the site shell, and the raw response carries
the string `SLEIC` only inside escaped JSON. It is **walled by rendering, not dead** (#70).

**An upgrade under #43 requires reading the document, and a document we cannot read cannot outrank one
we can.** So it is neither applied nor dropped. Nothing is broken by leaving it: source 3 is live and
correctly cited, and this was always an improvement rather than a correction. **Second item in this
edition whose blocker is a third-party renderer rather than anything the operation owes** — the first is
row 5's unreachable statute reproduction.

---

## §6 — Disposition

| Owed item | Status |
|---|---|
| 09-09 item 1 — unmarked emendation | **CLOSED** — served word re-confirmed, now attested on two dates; register proved maintained |
| 09-09 item 2 — superseded launch date | **CLOSED** — status *Running*, 2026–2029 re-confirmed; the no-figure fix has aged well |
| StC blog 404 | **CLOSED** — 200 at the re-slugged address, correction already in file (#54) |
| **NEW** — attribution read off an account handle | **CLOSED IN-RUN**, both languages, annotation only (#84) |
| Carried upgrade — *Final Learning Report 2026* | **OPEN**, blocked on the renderer; not applied on an unread document |

**Row 2 is clear for the flip.** Nothing on this row needs a human judgment, and nothing on it blocks
the wave.

— the Verifier · 2026-10-02
