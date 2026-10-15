# Ruling #101 — an expansion the annotation never carries is unreachable by the check that reads the annotation

**Filed 2026-10-15, at the point of filing (the 2026-09-20 rule), by the daily run's content function.**
**Family:** non-numeric (the eleventh member). **Extends:** #86 (a forced determination is still a claim),
#45 (the noun), and the 2026-09-13 `annotation == sentence` hand-off rule.

---

## The canonical statement

**An acronym is a name with its evidence removed. When a body expands one, the expansion is a claim about a
named institution that the piece's own annotation does not contain — so the `annotation == sentence` check
cannot reach it, and the only channel that can is an edition forced to expand the acronym in order to say
anything at all.**

## What happened

`2026-07-04-kenya-cbe-grade10-pathways`, published in both editions, carried this sentence in English for
**103 days**:

> Willy Kuria, the serving principal who chairs the **Kenya Senior School Heads Association**, put it
> without varnish: "We have a serious staffing deficit… I doubt there is a school in the country that is
> fully equipped with these teachers"

The register says **Kenya Secondary Schools Heads Association**. Read today in served text:

> The **Kenya Secondary Schools Heads Association** (KESSHA), noted that the staffing challenge is universal
> across all the senior schools. "We have a serious staffing deficit. … I doubt there is a school in the
> country that is fully equipped with these teachers," said national chairperson of the association, Mr
> Willy Kuria.

The Arabic edition was **right the whole time**: *رابطةَ مديري المدارس الثانوية في كينيا (KESSHA)* — the
association of **secondary**-school principals.

## Why every gate we own passed it

Four gates read this piece and none of them could have caught it.

1. **The `annotation == sentence` check (2026-09-13) had nothing to compare against.** The English
   `sources[]` annotation named the body only as **`KESSHA`**. The body expanded it. A check whose question
   is *does the body say about this register what the citation says about it?* is silent on a claim the
   citation does not make. **The annotation's silence read as agreement** — which is #57's defect
   (*a section claiming no count cannot be caught claiming a wrong one*) relocated from a count to a name.
2. **`qa_pair_frontmatter` passed, correctly.** The error was in a **body**, and the editions' frontmatter
   agreed about every fact belonging to the piece rather than to a language. Parity is a floor; #86 already
   said so.
3. **The numeric toolkit was never in play.** There is no number in the name.
4. **The Verifier's noun row (#45) is the right row, and it fires on a noun traced to a register.** The
   institution's name was never traced, because it was never *cited* — it was expanded.

## The mechanism, which is the transferable half

**The name was composed from the piece's own vocabulary rather than from the source's.** The dominant noun
of this piece is *senior school*: the senior-school roll-out, senior-school placement, the senior school a
child is placed into — three times in the same paragraph as the error. An association whose name contains
*Secondary* was written down with the piece's own word in place of the register's, and the result reads
perfectly: it is grammatical, plausible, and consistent with every other sentence around it.

That is the 09-13 drafting mechanism exactly — *the body sentence is composed from memory of the annotation,
and memory smooths* — with one new and worse property. The hedge, the date and the figure the 09-13 ruling
is about are all things the annotation **contains**, so re-reading the annotation recovers them. An
expansion is not in the annotation at all. **There is nothing to re-read.** The only recovery path is the
register itself, and nothing routes anyone back to the register unless the link dies — which is #100,
and which is precisely what happened here: this error surfaced on the day a *different* citation on the same
piece turned 404.

## Why the Arabic edition is the channel, and why that is structural rather than lucky

#86 established that the Arabic edition is a second verification channel whose bound is that **it answers
more questions than the English one**, and that its forced determinations — gender agreement on a role noun
— are made by one edition alone. This is the same shape with the arrow reversed:

**Arabic cannot carry a Latin-script acronym as a name.** `KESSHA` is not a word in the Arabic edition's
script; it can be kept as a foreign token beside an Arabic name, but it cannot *function* as the name. So the
Arabic composer had no option but to go back to the register and render what the letters stand for. **The
English composer had the option of the acronym and took it in the annotation, then expanded it from memory in
the body.** One edition was forced to read; the other was free not to.

So the second channel paid for the second time in twelve days (10-03 the institution, 10-15 the name), and
both times **the Arabic was right**. The honest reading of that is not that one edition is better. It is
#86's general form: *when two editions check each other, first ask which questions only one of them can
answer* — and add to it, from today, **which questions one of them is FORCED to answer.** A forced answer is
a read; an optional one may be a memory.

## Binding, from today

1. **A body may not expand an acronym the piece's own `sources[]` does not expand.** Either the annotation
   carries the full name as the register prints it, or the body keeps the acronym. The expansion and its
   evidence ship together or not at all.
2. **The hand-off to the Editor carries an `acronyms expanded in the body: N, each expanded in sources[]: ☐`
   line**, and a hand-off missing it is returned unread — the same teeth as the dek/title cap (07-27), the
   `annotation == sentence` line (09-13) and the named-humans gender line (10-04).
3. **Where the two editions render the same institution, the rendering that was FORCED is the control.** If
   the composed edition had to expand or decline something the other could leave as a token, its version is
   the one that was read, and a disagreement is resolved by re-opening the register — never by preferring the
   original language.
4. **A correction to a named institution is made in the register's own words**, not in a better paraphrase.

## The population, measured today and deliberately left open

Counted against all **44** published EN pieces, three times, because the measurement's own shape had to be
corrected twice — which is itself the lesson:

| Detector | Found | Verdict |
|---|---|---|
| Expansion whose initials equal an acronym present in the annotations | **3** | **Would have missed today's defect**: `KESSHA` is not `KSSHA`. An acronym is not always its name's initials. |
| Any full institution name in a body, absent from that piece's annotations | **28 across 22 of 44** | Too wide — a visible share are back-references (*The Ministry*, *The Commission*). |
| 3+ word names, back-references filtered | **10 across 10 of 44** | Three read in context are **regex fragments of longer names the body states correctly**. |

**So the number is 10 candidates, 7 unread, and 0 confirmed defects besides today's** — and today's was found
by the Arabic edition, not by any of the three detectors. Recorded as standing-queue **item 17** rather than
closed, because a list inside a measurement is a measurement with a date on it (10-14's lesson), and because
*a detector narrower than the defect it was built for reports a clean population it never examined.*
