# Ruling #84 — an identifier is not an attribution, and a reciprocity check has no arrow

**Filed:** 2026-10-02, by the Verifier, at Edition 05 row 2's confirmation read — the second of the
five, and the first to find a defect in an annotation the body had been more careful than.
**Artefact:** `verdicts/2026-10-02-ed05-sierra-leone-confirmation-read.md`, `sources[]` entry 8 in both
languages.
**Family:** which register speaks for the owner (#38, #40, #41, #42, #43) — and it touches the
non-numeric family through its second half.
**Cousins:** #40 (*a mirror can misname the instrument*), #43 (the register hierarchy), #54 (*a 404 is
not a death certificate* — the ruling filed on this same piece's source 3), #78 (*a control satisfied
by the component the claim is about*), #42 (a pair carries only what both languages share).

---

## The ruling

> **An account handle, a URL slug and a filename are identifiers. They are not published claims by
> anybody.** They frequently *contain* strings that look like provenance — an organisation's initials,
> a department, a year — and reading an attribution off one is reading it off a string its owner may
> change at will, has never asserted, and is under no obligation to keep true. The attribution comes
> from the document: a README, a masthead, an about page, an affiliation statement. **If the only place
> the organisation's name appears is in the address, the organisation has not said it.**

> **Corollary — a reciprocity check has no arrow.** The 2026-09-13 rule pairs each body sentence against
> its `sources[]` annotation, on the reasoning that the annotation is composed *with the register open*
> and the body afterwards from memory, so the annotation is the more trustworthy of the two. **That
> reasoning is a tendency, not a direction.** Here the body was right and the annotation was wrong, and
> an `annotation == sentence` test compares them without knowing which one to believe. Agreement is not
> correctness — including agreement between languages.

---

## The case

Row 2's eight source URLs were re-probed today with TLS validation enabled, redirects followed, the
client named (#80). **All eight serve 200.** Source 3, the Save the Children blog that produced ruling
#54, is live at its re-slugged address and the correction is already in the file. Nothing in this piece
is unreachable.

**One of the eight redirected**, and that is the whole finding. Source 8 —
`github.com/fergalturnerSCUK/2025_SCUK_SLEIC_Results` — answers through a permanent redirect to
`github.com/fergal-turner/2025_SCUK_SLEIC_Results`. **The account was renamed, and the old handle
contained `SCUK` while the new one does not.**

Our annotation read, in both languages:

> Save the Children UK — SLEIC 2025 endline results, open analysis repository (a provider publishing
> the code and data behind its own reported miss)

The register, read today: the owner is a **personal** account. The README says *"Background analysis
for an SCUK published blog"* and gives a `savethechildren.org.uk` address as the contact. So the
organisation published **the blog** — which is source 3, correctly attributed, and which genuinely is
the provider publishing its own miss. The **repository** is a named staff member's working analysis for
it. Our annotation promoted an individual's working file to an organisational publication.

**Where the wrong attribution came from is the part worth keeping.** Nothing was fabricated and no
research failed. The handle was `fergalturnerSCUK`. It reads as *Fergal Turner, SCUK*, and it was
right there in the URL on the line below the annotation. Nobody opened the README, because the address
already seemed to say who published it. **The rename did not create this defect — it removed the thing
that was concealing it.** A citation that had looked self-evidently attributed for five weeks stopped
looking that way the moment its owner edited a string we had been treating as evidence.

**And it passed every gate we own, correctly.** `qa_pair_frontmatter`, shipped yesterday, asserts that
both languages agree about the source URL set and about every fact belonging to the piece rather than
to a language. It passed: the Arabic annotation says «إنقاذُ الطفولة — المملكة المتحدة — مستودعُ...» and
the English says *Save the Children UK — ... repository*, in exact agreement, **on the same error.**
That is #78 one surface out: a check whose control is *the two sides matching* is satisfied by a defect
present on both sides. Parity (#42) is a floor, never a verdict.

**The body is clean in both languages and was never corrected.** ¶43 says *"one of the five
organisations being paid published its own shortfall, in its own words, with its own analysis code
attached"* — the organisation published the post, the code is attached, both true. ¶57 says *"the
endline analysis sits in a public repository under the heading 'check our homework'"* — a public
repository, no owner named. The drafter was *more* careful in the prose than in the citation, which is
the exact inverse of the shape the 09-13 rule was written to catch, and the reason the corollary above
is worth stating as a limit on that rule rather than as a new rule.

**Fix applied in-run, both languages:** the annotation now names the author and his role, states that
the repository is published on his own account rather than the organisation's, quotes the README's own
description of itself, records the rename and the redirect, says plainly that the previous annotation
made a stronger claim than the register supports, and notes that the body made no such claim. The URL
moves to the living address (#41 — supersede, don't resurrect). **No body prose was touched in either
language, so both word counts are unchanged** (EN 1,592 / AR 1,343) and no numeral moved in either
direction.

---

## What else the confirmation read closed, and the one thing it could not

**Item 1 (the unmarked emendation) — CONFIRMED, and better than confirmed.** The 09-09 fix printed the
served word, *definitely*. Re-read today, EOF still serves *"SLEIC does not definitely prove that
outcomes-based financing is a better way to fund education."* The word is right and is now attested on
two dates twenty-three days apart.

**And the 09-09 verdict's own supporting evidence has changed under it.** That verdict argued the page
was typo-prone by citing a second slip on it, *"what is takes to help children learn."* **Today that
sentence reads "what it takes."** The operation cannot now distinguish between the page having been
corrected and the verdict having mis-transcribed it, because no verbatim capture was kept — which is
*precisely* the method defect that verdict identified about the drafter and then committed itself, one
paragraph later, about its own evidence. Either way the conclusion is reinforced rather than weakened:
**this register is maintained, so a quotation from it is a reading with a date and not a property of
the page.** The annotation now says so in both languages, carrying both read dates and the reason the
second one exists.

**Item 2 (the January plan carried as a live future) — CONFIRMED.** The EOF early-childhood programme
page still serves status **Running**, term **2026–2029**, and its news rail has grown by four items
since the 09-09 read. The body's *"its own programme register now lists as running"* is a status and
carries no date or figure, exactly as the fix intended. The fix has also aged well in the one way that
mattered: had the piece printed a launch month, it would now be competing with five dated news items.

**The carried citation upgrade — STILL OPEN, and blocked on our client rather than on the source.**
Ruling #54's routing left a candidate upgrade: the programme's *Final Learning Report 2026* on Save the
Children's resource centre is a **document** and outranks a blog post on #43's hierarchy. The document
page serves **200**, and its bibliographic text is **not readable by any client available here** — the
rendered page returns the site shell, and the raw response carries the string only inside escaped JSON.
It is walled by rendering, not dead (#70). **An upgrade under #43 requires reading the document, and a
document we cannot read cannot outrank one we can**, so the upgrade is not applied and is not dropped.
Nothing is broken by leaving it: source 3 is live at 200 and correctly cited. This was always an
improvement, never a correction — and it is now the second confirmation-read item in this edition whose
blocker is the state of a third-party renderer rather than anything the operation owes.
