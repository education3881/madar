#!/usr/bin/env python3
r"""
qa_acronym_evidence.py — standing assertion 37. Owner: Assertions Engineer.

Closes standing-queue **item 17**, raised 2026-10-15 by the daily's content function,
displaced from the head five times, 8 days open. Ruling **#113**.

WHAT IT ASSERTS, in one sentence.  Where an English body expands an acronym, the
piece's own `sources[]` carries that expansion — ruling **#101** clause 1 (*either
the annotation carries the full name as the register prints it, or the body keeps
the acronym; the expansion and its evidence ship together or not at all*) made into
a gate instead of a hand-off checkbox.

WHY IT EXISTS, AND WHY TWO EARLIER ATTEMPTS FAILED.  #101 was earned by a published
error: `2026-07-04-kenya-cbe-grade10-pathways` printed *Kenya **Senior** School Heads
Association* for the register's *Kenya **Secondary** Schools Heads Association* for
103 days through four gates, and nothing we own could have caught it, because the EN
annotation named the body only as `KESSHA` — **the annotation's silence read as
agreement** (#57 moved off a count and onto a name). The item then asked whether a
name-boundary assertion is possible at all, and two detectors answered no:

  2026-10-15 — require the acronym to equal the name's word initials.  Found **3**
    instances across 44 pieces and **would have missed the one that earned the
    ruling**, because `KESSHA` is not `KSSHA`.
  2026-10-16 — recognise any 3+ word institution name absent from the piece's own
    frontmatter.  Found **46 candidates across 28 of 44 pieces** where the narrow
    detector found 10 across 10. Two detectors over one population, disagreeing by
    36, with nothing able to say which was right. Filed as a negative result: **a
    name's boundary is not a textual property** (#85's shape on the input side).

THE TURN THIS TOOL MAKES, and it is the whole finding.  A name's boundary is not a
textual property **in general**. It is a textual property **exactly when the name
carries an acronym**, because the acronym is a written specification of the span:
it says how many words, and it says which letter each one starts with. So the
detector stops guessing where a name ends and reads the answer off the acronym.

  KESSHA  ->  KE·nya  S·econdary  S·chools  H·eads  A·ssociation
  KJSEA   ->  K·enya  J·unior  S·chool  E·ducation  A·ssessment
  PSLE    ->  P·rimary  S·chool  L·eaving  E·xamination

The 10-15 detector failed on the first of these because it allowed each word exactly
one letter. Allow a word to supply a **prefix** of any length and the same anchor
that defeated it becomes the thing that makes it exact. There is no threshold, no
head-noun list and no judgment anywhere in the recogniser.

WHAT IT CANNOT SEE, stated here rather than left to be rediscovered (the 09-13 rule,
and item 26's subject — a declined scope is a dated claim about a subject that moves).

  (a) NAMES WITH NO ACRONYM.  The 46-candidate population of 10-16 is untouched and
      remains unactionable for the reason that review found. This instrument is
      strictly smaller than item 17 asked for, and the smallness is the reason it
      is exact. Measured 2026-10-23: 15 expansions anchored, against 46 candidate
      names the wider detector proposed.
  (b) THE ARABIC EDITION, ENTIRELY, AND BY CONSTRUCTION.  Arabic cannot carry a
      Latin-script acronym as a name — that is precisely why #101 clause 3 makes the
      Arabic rendering the control for a disputed institution. An instrument anchored
      on the acronym therefore has no purchase on the edition #101 trusts most.
      Counted 2026-10-23 across all 44 AR bodies: **0 acronym-anchored expansions**
      — and that zero is a measurement, not an assumption: the first build of this
      tool reported **1**, `KYK` anchored across `KPSS … YKS` in the Türkiye piece,
      180 characters of Arabic apart. WORD_RE emits only Latin words, so in an
      Arabic body two unrelated Latin acronyms are *consecutive tokens*, and the
      adjacency guard was counting token indices rather than text. **A recogniser's
      notion of "next word" is a claim about the script it was written for**, which
      is #109's lesson (*a composition check's error rate is set by whether it knows
      the intended assembly*) arriving on the input side. Fixed by measuring the gap
      in the source text; the claim above only became true after the fix.
      This is the same asymmetry #112 found from the other side — 128 of its 134
      declined quotation tokens are Arabic. **The edition that is FORCED to answer
      the name question is the edition no instrument of ours can read the answer
      from**, and that is now true twice.
  (c) AN ACRONYM THAT DOES NOT SPELL ITS OWN EXPANSION. The anchor is the whole
      method, so an acronym whose letters do not appear as the word-prefixes of the
      name it stands for supplies no boundary and is invisible here. **Measured
      2026-10-23, on the afternoon of the morning this tool shipped: 123 acronym
      tokens across the 44 EN bodies, and only 15 anchor — 12.2%.** The live case
      is in the Bahrain commission being drafted the same day: the body expands
      `BQA` as *Education & Training Quality Authority*, which shares not one
      word-initial with it, and this tool sees nothing. Most of the other 107 are
      compliant (the body simply keeps the acronym, which is #101 clause 1's second
      branch), and nothing here separates those from the BQA shape. **So this
      instrument gates a defect class it can see one eighth of, and the share is
      written down rather than left to be inferred from a green exit.** Standing-
      queue item 37.
  (d) WHETHER THE EXPANSION IS *RIGHT*.  This tool compares the body against the
      piece's own annotation. It cannot compare either against the register — that
      is `qa_citation_identity`'s subject (#112) and it needs the network. An
      expansion wrong in BOTH places passes here, correctly, and is #86's floor
      restated: parity is not a verdict.

THE EXCEPTION LIST, and why it can only shrink.  **Four of fifteen anchored
expansions — 26.7% — are not evidenced in their own piece's annotations**, found by
this tool on its first sweep and handed to the Web Developer and the Editor as
standing-queue **item 35** — because a fix that changes served bytes is the
Web Developer's even when an assertion found it (the 09-27 split), and because two of
the three registers cannot be read from this runner today (KNEC refuses the
connection, MOE answers 202 to every client here), so the expansion cannot be written
*as the register prints it*, which is what clause 1 actually requires. They are named
in KNOWN_OPEN below with the date and the queue item. **A name in that list that no
longer fails is itself a FAILURE** — the list is asserted to be a subset of the
findings, so a repair forces its own bookkeeping and the list cannot outlive the
debt. Same shape as assertion 33's membership list, and for the same reason: an
exception nobody is forced to delete is a permanent exemption wearing a date.

EXIT CODES.  0 clean · 1 an expansion has no evidence in its own sources[], or the
exception list has gone stale · 4 refused (no corpus found).

USAGE.  python3 agents/tools/qa_acronym_evidence.py .          # the gate
        python3 agents/tools/qa_acronym_evidence.py . --list    # print every anchor
"""

import os
import re
import sys

EN_DIR = os.path.join("web", "src", "content", "articles")
AR_DIR = os.path.join("web", "src", "content", "articles-ar")

# Findings that are real, served, and handed over rather than fixed by the tool that
# found them. (slug, acronym) -> why. Asserted to be a SUBSET of today's findings.
KNOWN_OPEN = {}
# EMPTY SINCE 2026-10-29, when queue item 35 closed at 6 days from the DEFECT head.
# All four findings of this tool's first sweep are repaired, and the two branches of
# #101 clause 1 were BOTH needed — which is ruling #120.
#
#   PSLE  — seab.gov.sg/psle/ prints 'The Primary School Leaving Examination (PSLE)
#           is an annual national examination…' in its own served text.  moe.gov.sg
#           still answers 202 to every client here (re-measured 2026-10-29), so the
#           expansion is cited from the BOARD THAT CONDUCTS THE EXAM rather than from
#           the ministry: a readable first-party register outranks an unreadable one
#           (#43), and the owner of a name is not always the owner of the policy.
#   TMIS  — tsctmis.org serves `<h1>Teacher Management Information System / Sierra
#           Leone`.  Per #119 the `<h1>` is the form the document PRINTS, which is
#           the strongest evidence form available; the EdTech Hub registers the piece
#           already cited never print it.
#   J-PAL — povertyactionlab.org prints 'The Abdul Latif Jameel Poverty Action Lab
#           (J-PAL)…'.  The anchor was always SHORT by two words and that was the
#           finding's point: an acronym that drops a word cannot evidence it.
#   KJSEA — took clause 1's OTHER branch: THE BODY KEEPS THE ACRONYM, in both
#           editions.  kjsea.knec.ac.ke does not resolve from this runner, its one
#           archive snapshot (2026-02-07) is a shell serving a `<title>` and nothing
#           else, knec.ac.ke's own snapshot never prints the name, nation.africa
#           answers 403 — and the readable third-party registers DISAGREE, between
#           `Junior School` and `Junior Secondary`.  #101 clause 3 settles a
#           disagreement by re-opening the register; when the register cannot be
#           re-opened clause 3 has NO OUTPUT, and the second branch is the only exit.
#           The Arabic edition had rendered it «تقييم للتعليم الإعدادي في كينيا» —
#           إعدادي being the term for the PREPARATORY stage, i.e. the other reading —
#           so the FORCED edition (#101 clause 3) was quietly voting the other way
#           for 117 days and nothing compared them.
#
# The dict stays here, empty, because the next finding needs a home and because an
# exception list deleted outright is an exception list that has to be re-argued.

# A word may supply a prefix of any length. These may be skipped without supplying
# one — they are the connectives institution names carry and acronyms drop.
SKIPPABLE = {
    "of", "and", "for", "the", "in", "on", "to", "at",
    "de", "du", "des", "la", "le", "les", "et", "da", "do", "dos", "y",
}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'’\-]*")
# What may legitimately sit between two words of one name, in the raw text.
INTERWORD_RE = re.compile(r"^[\s\-‐-―'’“”\"(),.&/]*$")
# An acronym token, hyphens included so J-PAL is one token rather than a stray PAL.
ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*\b")


def split_frontmatter(text):
    """Return (frontmatter, body). Raises if the file is not a frontmatter doc."""
    if not text.startswith("---"):
        raise ValueError("no frontmatter")
    end = text.index("\n---", 3)
    return text[3:end], text[end + 4:]


def acronym_tokens(body):
    """Acronym-shaped tokens of three or more letters, hyphen-joined forms kept whole."""
    out = set()
    for m in ACRONYM_RE.finditer(body):
        tok = m.group(0)
        if len(re.sub(r"[^A-Z]", "", tok)) >= 3:
            out.add(tok)
    return out


def anchored_expansion(acronym, text):
    """The span of capitalised words whose prefixes concatenate to `acronym`.

    Returns the span's text, or None. Where several spans qualify, the one using the
    MOST words wins — a one-letter-per-word reading is the ordinary shape of a name,
    and preferring the shortest character span instead reads `Primary School Leaving`
    for PSLE by letting `Leaving` supply `LE`. Char length breaks the remaining ties.
    """
    target = re.sub(r"[^A-Z0-9]", "", acronym.upper())
    toks = [(m.start(), m.end(), m.group(0)) for m in WORD_RE.finditer(text)]
    found = []
    for start in range(len(toks)):
        first = toks[start][2]
        if not first[:1].isupper() or first[0].upper() != target[0]:
            continue
        stack = [(start, 0, [])]
        while stack:
            ti, pos, chosen = stack.pop()
            if pos == len(target):
                if len(chosen) >= 2:
                    s, e = toks[chosen[0]][0], toks[chosen[-1]][1]
                    found.append((len(chosen), -(e - s), text[s:e]))
                continue
            if ti >= len(toks):
                continue
            # The words of a name are adjacent. Adjacency is measured in the SOURCE
            # TEXT, never in the token index: WORD_RE emits only Latin words, so in
            # an Arabic body two Latin acronyms hundreds of characters apart are
            # consecutive tokens. Measured 2026-10-23, before this guard existed:
            # one AR "anchor", `KYK` spanning `KPSS … YKS` across 180 characters of
            # Arabic. The gap must be whitespace and light punctuation only.
            if chosen:
                if ti - chosen[-1] > 1:
                    continue
                gap = text[toks[chosen[-1]][1]:toks[ti][0]]
                if not INTERWORD_RE.match(gap):
                    continue
            word = toks[ti][2]
            if chosen and word.lower() in SKIPPABLE:
                stack.append((ti + 1, pos, chosen))
            if not word[:1].isupper():
                continue
            for plen in range(min(len(word), len(target) - pos), 0, -1):
                if word[:plen].upper() == target[pos:pos + plen]:
                    stack.append((ti + 1, pos + plen, chosen + [ti]))
    # A span that contains the acronym itself is the acronym being read as its own
    # expansion (`NAEP Proficient` for NAEP, `MINEDUC's Education` for MINEDUC).
    bare = re.compile(r"\b" + re.escape(acronym) + r"\b")
    found = [f for f in found if not bare.search(f[2])]
    if not found:
        return None
    found.sort(reverse=True)
    return found[0][2]


def normalise(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def sweep(root, directory):
    """Return [(slug, acronym, expansion, supported)] for one edition."""
    base = os.path.join(root, directory)
    if not os.path.isdir(base):
        return None
    rows = []
    for name in sorted(os.listdir(base)):
        if not name.endswith(".md"):
            continue
        text = open(os.path.join(base, name), encoding="utf-8").read()
        try:
            frontmatter, body = split_frontmatter(text)
        except ValueError:
            continue
        slug = name[:-3]
        haystack = normalise(frontmatter)
        for acronym in sorted(acronym_tokens(body)):
            expansion = anchored_expansion(acronym, body)
            if expansion is None:
                continue
            rows.append((slug, acronym, expansion,
                         normalise(expansion) in haystack))
    return rows


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    listing = "--list" in sys.argv
    root = args[0] if args else "."

    en = sweep(root, EN_DIR)
    if en is None:
        print("REFUSED qa_acronym_evidence — no %s under %r. This assertion reads "
              "SOURCE files, not dist: an acronym's evidence lives in frontmatter, "
              "which is never built." % (EN_DIR, root))
        sys.exit(4)
    ar = sweep(root, AR_DIR) or []

    print("qa_acronym_evidence — standing assertion 37 (ruling #113)")
    print("  the acronym supplies the name's boundary; the annotation must supply "
          "its evidence (#101 clause 1)\n")

    print("  EN bodies swept .............. %d" % len(
        [f for f in os.listdir(os.path.join(root, EN_DIR)) if f.endswith(".md")]))
    print("  acronym-anchored expansions .. %d" % len(en))
    print("  evidenced in own sources[] ... %d" % sum(1 for r in en if r[3]))
    print("  AR bodies swept .............. %d  (0 anchors expected, by "
          "construction — see (b) in the header)" % len(
              [f for f in os.listdir(os.path.join(root, AR_DIR))
               if f.endswith(".md")] if os.path.isdir(os.path.join(root, AR_DIR))
              else []))
    print("  AR acronym-anchored .......... %d" % len(ar))

    if listing:
        print("\n  every anchor found:")
        for slug, acronym, expansion, ok in en:
            print("    %-44s %-8s %-46s %s"
                  % (slug[:44], acronym, expansion[:46],
                     "evidenced" if ok else "UNEVIDENCED"))

    failures = [r for r in en if not r[3]]
    found_keys = {(r[0], r[1]) for r in failures}

    unexpected = [r for r in failures if (r[0], r[1]) not in KNOWN_OPEN]
    stale = [k for k in KNOWN_OPEN if k not in found_keys]

    failed = False

    if unexpected:
        failed = True
        print("\n  FAIL — %d body expansion(s) with no evidence in the piece's own "
              "sources[]:" % len(unexpected))
        for slug, acronym, expansion, _ in unexpected:
            print("    %s" % slug)
            print("      body expands %s as %r" % (acronym, expansion))
            print("      sources[] carries no such string — #101 clause 1: the "
                  "expansion and its evidence ship together or not at all")

    if stale:
        failed = True
        print("\n  FAIL — %d entry(ies) in KNOWN_OPEN no longer fail. An exception "
              "nobody is forced to delete is a permanent exemption wearing a date; "
              "remove them:" % len(stale))
        for slug, acronym in sorted(stale):
            print("    %s / %s" % (slug, acronym))

    carried = sorted(found_keys & set(KNOWN_OPEN))
    if carried:
        print("\n  %d known-open finding(s) carried, handed over rather than fixed "
              "by the instrument that found them (the 09-27 split):" % len(carried))
        for key in carried:
            print("    %s / %s" % key)
            print("      %s" % KNOWN_OPEN[key])

    if failed:
        print("\nqa_acronym_evidence: FAIL — see above.")
        sys.exit(1)

    print("\nCLEAN qa_acronym_evidence — every acronym this corpus expands in a body "
          "is expanded in that piece's own annotations, except the %d carried above."
          % len(carried))
    sys.exit(0)


if __name__ == "__main__":
    main()
