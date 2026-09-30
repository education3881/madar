# Ruling #79 — a bite run once is a claim about the day it ran; and some of an instrument's history stops being freezable

**Filed:** 2026-09-30, by the QA lane, testing the 2026-09-29 forward question before adding anything new.
**Artefact:** `agents/tools/qa_a11y_lang.py` — the first of the twenty-six fixture-free assertions to
gain a self-test, proved seven ways with one experiment reported as void.
**Family:** assertion discipline — the register's largest, now eighteen of seventy-nine.
**Cousins:** #35 (prove an assertion both ways), #74 (a hash proves the injection landed, not where),
#75 (*a check whose population can legitimately be empty cannot use "found nothing" as its failure
signal — it needs a fixture*), and the 08-16 silent-pass trap.

---

## The ruling, in two halves

**First half.** `qa_census` can tell you an assertion **enumerated** its population; nothing can tell you
the assertion can still **recognise** the defect. Those are two different failure modes and only one of
them has ever been instrumented. Every scope decision inside a check — a class name, a tag set, an
exemption regex — is a guess about served markup, and a template change can quietly move a string out of
scope, after which the check enumerates everything, finds nothing, and passes. **So: a check whose
judgment is a pure function of a string carries fixtures of the readings it has really made, and it
proves the recogniser before it judges the tree.**

**Second half, and it is a caution against the obvious programme.** *Not every historical bite can be
frozen, because a later defence can make an earlier bug unreproducible — and a fixture you cannot make
fail is not a fixture.* Freezing the whole of an instrument's history is not available; what is available
is freezing the part that still discriminates, and **saying in the file which part did not and why.**

---

## What was done, and what the numbers were

The 09-29 log asked which of the twenty-six could have its bite frozen and which was cheapest first.
`qa_a11y_lang` on three counts: its judgment (`LangAudit`) is a pure function of an HTML string, so a
fixture needs no fake `dist`; four distinct historical wrong-readings were **already written down in its
own docstring as prose**; and the two real bites that proved it on 2026-09-13 are one line each.

**Eight fixtures**, each a reading this check has really made, and each carrying `checked` as well as its
findings. **Control:** silent on the real 121-page build — 4,673 text nodes, 0 defects, exit 0.

**Six bites, each aimed at one named fixture, each hitting the one it named (#74):**

| bite | fixture that failed |
|---|---|
| drop `skip-link` from the chrome class list | the 09-13 *Skip to content* bite |
| drop `figcaption` from the chrome tags | the 38 real colophon defects |
| resolve `lang` from the parent before the element | the inherited-correct Arabic span (**2 fixtures**) |
| void the sources carve-out | *Elsevier* inside Arabic article chrome |
| drop the mixed-script allowance | the Arabic caption that also carries Latin |
| put body prose in scope | the Spanish pull-quote wolf-cry |

**Two findings from running the bites, and both are the point of the exercise:**

- **A seventh bite exited 1 and bit nothing.** Injecting a blind stack pop through a shell heredoc put a
  literal `\n` into the source; the file did not compile, Python exited 1, and *the exit code alone reads
  exactly like a successful bite.* Counting the failing fixtures separated them. Re-injected properly —
  with `py_compile` asserting the file still runs — it failed exactly its fixture. **#74 restated for the
  injector rather than the injection: assert that the bitten instrument still executes, or a syntax error
  will pass for a finding.**
- **Two fixtures are silent in both the correct and the broken code and differ only in `checked`.** The
  blind-pop bite left the findings identical — *no finding* both ways — and collapsed the text nodes
  examined from **2 to 0**. A fixture comparing findings alone would have read green through a recogniser
  whose scope had silently emptied. **A fixture must pin the population it looked at, not only the verdict
  it reached.**

**And the experiment that was void, reported rather than dropped.** The docstring records a VOID-element
stack bug (`<img>` pushed and never popped). Removing the `VOID` guard today changes **nothing**:
identical 4,673 text nodes, identical 0 defects, identical exit — because the later `handle_endtag`, which
pops to the nearest *matching* open tag, makes the earlier bug unreachable. The guard stays; the stack
discipline is frozen through a stray-close reading instead; and the file says which bite could not be
frozen and why.

---

## The general form

*A bite is an experiment; a fixture is a standing claim.* An operation that proves each new assertion once
and throws the proof away is holding twenty-six claims about days that have passed. Converting them is
cheap where the judgment is a pure function of a string and impossible where it is not — and the honest
audit says which, rather than reporting a percentage.

**The narrower limb worth carrying to the next conversion:** the cheapest candidate is not the simplest
check, it is the one whose **own docstring already records its wrong readings**. Four of this tool's eight
fixtures were transcribed out of prose somebody had already written. *An instrument that documented its own
mistakes has already paid for its fixtures; it just never cashed them.*
