# Ruling #134 — A name's MORPHOLOGY is a read; a name's SOUND is not

**Filed** 2026-11-08, from the standing queue's own head — **item 85**, the board's one DEFECT, at 1 day.
**Family** non-numeric (#45, #46, #47, #49, #51, #53, #62, #64, #86, #87, #101, #102, #104, #117, #120,
#132, #133, **#134**) — **eighteenth member**, and the sixth consecutive one in which the Arabic edition
held something no instrument of ours could read.
**Lane** content, from a served repair. **Amends** #86 clause 1.

---

## The rule

**#86 clause 1 reads *the Arabic composer reads a named human's gender off the register's own pronoun or
gendered title, never off the name*. The last four words are too wide, and the correction is a distinction
rather than a loosening.**

> A name's **sound** is not evidence of anything. A name's **morphology, as the register prints it**, is —
> and reading it is exactly as much a read as reading a pronoun.

`بن` / `bin` and `بنت` / `bint` are not how a name sounds. They are morphemes, obligatory in Arabic
naming, **printed by the register**, and each one states a gender as flatly as `she` does. So do the
Omani royal style `Sayyid` / `Sayyida` and the feminine nisba ending `ـية`. A composer who reads `bint`
out of `H.E Dr Jokha bint Abdullah Al Shukaili` on the issuing body's own management page has gone to the
register and come back with what the register prints. A composer who decided `وليد` sounds male has not.

**The test is one question, and it is about the artefact rather than about the name:** *is the token I am
reading printed by the register, or supplied by me?* `bint` passes. A name's phonology does not, and
neither does a name's statistical distribution across a language's population, which is the same
inference wearing a number.

## What earned it

Standing-queue item 85 names **32 gender determinations served in 14 of the 44 Arabic pieces with no
evidence on file.** This run took the four pieces the row sends first — **10 honorific tokens, 6 named
humans** — and read every one against the register its own annotation names
(`content-drafts/recon/2026-11-08-item-85-gender-provenance-the-four-one-channel-pieces.md`).

**8 of 10 evidenced. 2 of 10 undetermined by their registers. 0 of 10 wrong.**

**And only ONE of the eight evidenced determinations rests on a pronoun.**

| What carries the evidence | Count | Instance |
|---|---|---|
| A pronoun | **1** | *"But she noted…"* — Grace Chua, The Straits Times via STOMP |
| A gendered title | **4** | *"added Ms. Ahmad"*; *"Mrs Grace Chua"*; *"Mr Mohamed Ashiq"* |
| **A morpheme inside the name, as printed** | **4** | *"HH Sayyid Theyazin bin Haitham Al Said"* ×3; *"H.E Dr Jokha bint Abdullah Al Shukaili"* |
| Nothing — register silent | **2** | *"Dr. Anna-Christine Janke"*; *"Dr. Waleed Al Ali"*, then *"Dr. Al Ali said"* |

Half of the evidence this class actually has is in the fourth row, and #86 clause 1 as written forbade
reading it. A rule that forbids the register's own printed token is a rule that sends the composer back
to the one thing it was written to stop them using: a guess.

## Why clause 1 was written that way, and why the error is not carelessness

#86's two confirmed errors were **Alex Maclean**, printed masculine against a register that says *she
said*, and the **Benin minister**, printed feminine against a register whose French says *le ministre*.
Both were read off how the name sounds, in exactly the way clause 1 names. The clause generalised from
two instances of **one** mechanism to the whole category *name* — and a name is not one thing. It is a
string with a sound, and, in Arabic and in Arabic transliterated into Latin script, a string with
**grammar in it**. The generalisation is #57's shape on a prohibition rather than on a count: *a bucket
set cannot report a distinction it cannot hold*, and `name` was one bucket doing the work of two.

## The second half, and it inverts #101

Two of the four pieces item 85 called **one-channel** are not.

**Oman** was never one-channel: its **English** annotation already printed `HH Sayyid Theyazin bin
Haitham`. The row's detector reads a closed class of English honorifics — `Dr|Professor|Minister|Sheikh|
Mr|Mrs|Ms|…` — and neither `Sayyid` nor `bin` is in it. That is **#113's own lesson** arriving from the
other side: a closed class cannot see a title outside it, and the gap is the detector's, not the corpus's.

**Singapore is the sharper case.** The register prints **`Mrs Grace Chua`** and **`Mr Mohamed Ashiq`**.
The English annotation had reduced both to **`Principal Grace Chua and Year Head Mohamed Ashiq`**. So
the evidence was in the register, the **Arabic** edition kept it, and **the English edition deleted its
own second channel at compose time** — not by error, but by the ordinary editorial reflex of preferring
a role to a courtesy title.

That inverts **#101**, where Arabic was *forced* back to the register because it cannot carry a Latin
acronym, and English took the cheap token. Here Arabic was forced to choose a gender and therefore had
to read, and English — free to omit — omitted, **and in omitting destroyed the evidence for the other
edition's forced choice.** #86 asked which questions only one edition can answer; #101 which questions
one edition is *forced* to answer; #117 which it is forced to answer wrongly. This adds: **which edition
is free to DISCARD the evidence the other one is forced to need.** Freedom is the hazard, not the
constraint.

**Binding, and it is one line of the hand-off:** where a register prints a gendered title or a gendered
name morpheme for a named human, **the annotation carries that token verbatim in BOTH editions** — the
English annotation does not get to substitute a role for it. The evidence and the determination ship
together, which is #101 clause 1 applied to a courtesy title instead of to an acronym.

## Where the rule declines

**It cannot be gated, and the reason is not #93's cost.** `bint` is a string, and finding it is trivial;
deciding that a given `bint` is *the register's* `bint` rather than our transliteration of it requires
comparing our annotation against somebody else's bytes, which is `qa_citation_identity`'s subject — and
that instrument declines 128 of 134 Arabic tokens by construction (#112). So the asserting half of this
rule lives on the **English** annotation, where the register's token is in the register's own script, and
the Arabic half is a read. **That is #132 one day later and from the opposite direction:** #132 says
English supplies the name boundary and commits no gender while Arabic commits the gender and supplies no
name boundary. This says the **evidence** for Arabic's commitment is almost always in English's script —
so the two editions are not two channels on this property. They are one channel and one obligation.

## Cost, recorded

The run's own gates refused this work twice and were right twice. `qa_citation_identity` demanded
register rows for the two new verbatim quotations, then found one was **not** verbatim — a comma I had
inserted into `gov.om`'s own run of text, which is #112's subject committed by the run writing about it.
`qa_annotation_figures` then caught **14 internal rule numbers** (`#86`) and two HTTP status codes
leaking into **served** annotations, where no reader can resolve them; the prose now states the
provenance in plain words and the rule citations live in this file. *A served annotation is read by a
reader, not by the operation that wrote it.*
