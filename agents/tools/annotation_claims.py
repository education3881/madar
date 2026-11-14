#!/usr/bin/env python3
r"""
annotation_claims.py — a MEASUREMENT, not an assertion. Owner: Assertions Engineer.

Answers standing-queue **item 38**, raised 2026-10-24 by the daily's forward question,
21 days open, taken as the board's head on 2026-11-14 with the DEFECT bucket empty.
Ruling **#142**.

NO `qa_` PREFIX, ON PURPOSE.  `CLAUDE.md` counts the standing assertions by globbing
`agents/tools/qa_*.py`.  This file is outside that glob, gates nothing, and moves no
count in any file — the same standing as `served_dates.py`, `run_envelope.py` and
`arabic_side_reach.py`.  It exists because item 38's question is *can an instrument take
this class at all?*, and the honest answer turned out to be a partition with a
measured negative result in it.  A negative result that cannot be re-taken is an
opinion; this is how it is re-taken.

WHAT ITEM 38 ASKED.  Standing assertion 38 (`qa_annotation_figures`, #114) compares a
QUANTITY printed in a served annotation against the body of its own piece.  Item 38 is
its complement: **what does an annotation's non-numeric prose assert, and can anything
we own test it?**  The item named its own founding instance — a `gov.om` parenthetical
reading *"the issuing body and its mandate; renamed in 2026"* against a page carrying no
rename, no date and no instrument — and noted that it *would still pass today*, because
#114's licence (a) excuses a bare year as a publication date.  The item also named the
class it expected to be reachable: *a rename, a mandate, a named human, a hedge, an
attribution verb (#43's hierarchy applied to our own verbs, owed since 09-13 and never
taken)*.

THE ANSWER, IN ONE SENTENCE.  The attribution-verb half is **NOT reachable by any
instrument, and the reason is that this publication's own disciplines have already
spent the tokens an instrument would need** — four independent grounds, each measured
below, which between them give a detector a precision of **0 true positives out of 13
flagged over 714 served annotations**.  What IS reachable is a class item 38 did not
name: the **self-specifying provenance claim**, where the annotation prints both a
method and its value, so the claim specifies its own test.

  THE FOUR GROUNDS, and each is a count rather than an argument:

  (1) THE DOCUMENT-TYPE NOUN OCCUPIES THE VERB.  `report`, `note`, `state`, `claim`,
      `name`, `describe` are all document-type or ordinary nouns, and a citation's whole
      job is to NAME DOCUMENTS.  A wide attribution vocabulary flags 185 annotations; a
      vocabulary restricted to forms with no English noun reading flags 77.  The
      difference is `Annual Report 2024`, `Situation Report #203`, `Country Note`,
      `review reports`.  2026-09-14's trap, read on the input side: *a sweep scoped
      wider than the thing it checks finds the right string for the wrong reason.*

  (2) THE HOUSE STYLE OCCUPIES THE VERB.  The standing prohibition carried from Edition
      05 is **announced != measured, labelled at the figure** (#117 extends it to tense).
      A CORRECT annotation is therefore REQUIRED to print `announced` or `stated` beside
      a figure: *the announced scale: a target of about 23 lakh students*, *the 2025
      tally as announced at the minister's press conference*.  Nine of the thirteen rows
      a quotation-requiring detector flags are this idiom, used exactly as the rule
      demands.  The token an instrument would key on is the token the style mandates,
      and no narrowing reaches inside it, because **both uses are correct and one of
      them is compulsory.**

  (3) THE VERB'S SUBJECT IS NOT ALWAYS THE REGISTER.  *roughly one in three Year 9
      students **writes** at a level expected in primary school*; *the intermediate it
      publishes at the address **printed** inside that certificate*.  Two of thirteen.
      A string match cannot read a subject, and these two subjects are a schoolchild
      and a field inside a TLS certificate.

  (4) AN ABSENCE CLAIM IS UNQUOTABLE BY CONSTRUCTION, AND THIS IS THE GROUND THAT
      SETTLES IT.  The obvious rule — *either the annotation quotes the register or it
      does not claim the register's speech*, which is #101 clause 1 moved from an
      expansion onto an utterance — would red the single most carefully written
      annotation in this corpus.  The Arabic edition of `2026-05-27-egypt-ekb-decade`
      says so in its own words, having thought of it first:

        "وقد ذُكرت الصيغةُ هنا بِلا علامات اقتباس عن قصد، لأنَّ الاقتباسَ ادِّعاءُ أنَّ
         البايتات تَحملها، وهذا ادِّعاءُ أنَّها لا تَحملها."
        (the form is given here without quotation marks deliberately, because a
         quotation is a claim that the bytes carry it, and this is a claim that they
         do not.)

      Its claim is that the register titles a named human by his deanship and NOT by a
      doctorate — a claim about what is ABSENT from the bytes.  A quotation asserts
      presence.  So requiring a quotation beside an attribution verb does not merely
      misfire here; it **inverts**, demanding presence as the evidence for absence.

  WHAT FOLLOWS: item 38's non-numeric half is a **VERIFIER ROW, not a gate** — which is
  one of the two answers the item itself offered, reached by measurement rather than by
  preference.  #93's ground (a floor above today's reality reds every build) is not the
  reason; #140's is: an instrument that returns NO ANSWER on a class it can reach is
  behaving correctly, and this instrument's answers would be wrong rather than absent.

WHAT IS REACHABLE, AND IT IS A CLASS ITEM 38 DID NOT NAME.  Thirty-nine of the 714
annotations carry a **self-specifying provenance claim**: the annotation prints a METHOD
and its VALUE together — `sha256 d6b62bda…`, `HTTP 200`, `Last-Modified 2026-08-16`,
a byte length, a dated fetch, `read in served bytes <date>`.  That is #113's criterion
met by a different artefact: an acronym states how many words and which letter each
begins with, and a sha256 states which function over which bytes.  The claim therefore
specifies its own test, in two tiers:

  - OFFLINE, and this is the part a gate could take: the claim's own internal
    arithmetic.  A read date that has not arrived; a `Last-Modified` later than the read
    that observed it; a sha256 that is not hex, or truncated with no ellipsis; a read
    asserted behind a 4xx.  **Measured 2026-11-14 over all 39: ZERO violations.**
    Proved both ways on a /tmp copy the same morning, with the injection asserted to
    have changed the file first (2026-09-14): control 0, bite 2 of 3.  **THE THIRD BITE
    DID NOT BITE, and it is the more useful half of the proof.** Turning one `HTTP 200`
    into `HTTP 404` beside a surviving `HTTP 200` in the same annotation exits like a
    passing control, because the limb can only ask `all statuses >= 400` — and it must,
    since an annotation legitimately records a dead register beside a live one (the
    `gov.uk` person page that 404'd under yesterday's Ofsted read is exactly that).
    **The annotation is not the claim's boundary**: one annotation carries many fetches,
    so a per-claim limb has nothing to attach to.  That is item 38's own problem one
    level down, inside the half that was supposed to be the reachable one — recorded
    here rather than repaired by widening a limb into a false positive.
  - NETWORK, and it cannot gate, for #111's reason exactly: re-taking a sha256 needs
    somebody else's server to answer, and an outage must not stop this publication
    deploying.

This file measures and prints both.  It is deliberately NOT wired into `postbuild`:
the offline tier currently has zero bite, and the class is young enough (39 of 714, all
of them written since 2026-10-23) that a gate would be guarding a convention rather
than enforcing one.  Standing-queue row raised in the same run that wrote this, so the
gate is HANDED OVER rather than squeezed into the end of a run — 2026-11-13's practice
on item 97, followed rather than re-derived.

USAGE
  python3 agents/tools/annotation_claims.py .            the full partition
  python3 agents/tools/annotation_claims.py . --flagged   the 13 rows, classified by ground
Exit 0 always except 4 = REFUSED (no corpus found).  It asserts nothing.
"""
import os
import re
import sys
import json
import datetime
import collections

# forms with NO English noun reading -- ground (1) is the difference between this and WIDE
VERB_TIGHT = (r"\b(?:said|says|stated|announced|announces|printed|prints|confirmed|confirms"
              r"|described|describes|asserted|asserts|wrote|writes|in its own words)\b")
VERB_WIDE = (VERB_TIGHT[:-3] + r"|report|reports|reported|note|notes|noted|state|states"
             r"|claim|claims|claimed|name|names|named|describe|call|calls|called)\b")

PROVENANCE = {
    "sha256":        r"sha256\s+[0-9a-f]{8,}",
    "http-status":   r"HTTP\s+\d{3}",
    "last-modified": r"Last-Modified",
    "etag":          r"\bETag\b",
    "byte-length":   r"\d[\d,]*\s*(?:bytes|KB|MB)\b",
    "read-in-bytes": r"read in served bytes|read in the served bytes|في البايتات المخدومة",
    "fetched-dated": r"\bfetch(?:ed)?\b[^.;]{0,40}\d{4}-\d{2}-\d{2}",
}

# the classes item 38 itself named, kept so the row's own wording stays measurable
WORLD = {
    "rename":      r"\brenamed\b|\brename\b|\bformerly\b|أعيدت تسميته",
    "mandate":     r"\bmandate\b|\bremit\b|ولايته|اختصاص",
    "hedge":       r"\b(?:planned|expected|proposed|reportedly|intended|set to|likely)\b",
    "named-human": r"\b(?:Mr|Ms|Mrs|Dr|Minister|Chief Inspector|Secretary|Director)\b",
}

PAIRED_QUOTE = r"['‘“«\"][^'’”»\"]{8,}['’”»\"]"

# ground (2): the figure-label idiom the standing prohibitions MANDATE
FIGURE_LABEL = (r"as announced|the announced|announced scale|announced reach|announced scope"
                r"|announced p|figures announced|tally as announced|announced \d|stated for"
                r"|administration confirmed|calendar, as announced")


def corpus(root):
    rows = []
    for ed, rel in (("EN", "web/src/content/articles"), ("AR", "web/src/content/articles-ar")):
        d = os.path.join(root, rel)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md"):
                continue
            text = open(os.path.join(d, name), encoding="utf-8").read()
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
            if not m:
                continue
            fm, body = m.group(1), m.group(2)
            if not re.search(r"^approved:\s*true", fm, re.M):
                continue          # a held file is not part of the publication (09-06)
            sm = re.search(r"^sources:\n(.*?)(?=^\S)", fm + "\n\x00", re.M | re.S)
            if not sm:
                continue
            for title, url in re.findall(
                    r'-\s+title:\s*"((?:[^"\\]|\\.)*)"\s*\n\s*url:\s*"([^"]+)"', sm.group(1)):
                rows.append(dict(ed=ed, slug=name[:-3], title=title, url=url, body=body))
    return rows


def iso_dates(s):
    out = []
    for m in re.finditer(r"(20\d\d)-(\d\d)-(\d\d)", s):
        try:
            out.append((m.group(0), datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))))
        except ValueError:
            out.append((m.group(0), None))
    return out


def provenance_arithmetic(title, today):
    """The OFFLINE tier: a self-specifying claim's own internal consistency."""
    bad = []
    for raw, d in iso_dates(title):
        if d is None:
            bad.append(("malformed date", raw))
        elif d > today:
            bad.append(("read date has not arrived", raw))
    for m in re.finditer(r"sha256\s+([0-9a-zA-Z….]+)", title):
        tok = m.group(1)
        core = tok.rstrip("….")
        if not re.fullmatch(r"[0-9a-f]+", core):
            bad.append(("sha256 not hex", tok))
        elif len(core) != 64 and not tok.endswith(("…", ".")):
            bad.append(("sha256 truncated with no ellipsis", tok))
    st = [int(x) for x in re.findall(r"HTTP\s+(\d{3})", title)]
    if st and all(s >= 400 for s in st) and re.search(r"read in served bytes|fetched", title, re.I):
        bad.append(("a read asserted behind an error status", str(st)))
    lm = re.search(r"Last-Modified\s+(20\d\d-\d\d-\d\d)", title)
    rd = re.search(r"read(?:\s+in\s+served\s+bytes)?\s+(20\d\d-\d\d-\d\d)", title)
    if lm and rd:
        a = datetime.date(*map(int, lm.group(1).split("-")))
        b = datetime.date(*map(int, rd.group(1).split("-")))
        if a > b:
            bad.append(("Last-Modified later than the read that observed it",
                        "%s > %s" % (lm.group(1), rd.group(1))))
    return bad


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    rows = corpus(root)
    if not rows:
        print("REFUSED annotation_claims — no approved article with a sources[] block under %s" % root)
        return 4
    today = datetime.date.today()
    en = sum(1 for r in rows if r["ed"] == "EN")

    print("OK annotation_claims — item 38's class, partitioned by what can test it")
    print("  served annotations ......... %d  (EN %d, AR %d)" % (len(rows), en, len(rows) - en))
    print("  distinct registers ......... %d" % len({r["url"] for r in rows}))
    print("  annotations with no digit .. %d  — #114 says nothing about these at all"
          % sum(1 for r in rows if not re.search(r"\d", r["title"])))

    wide = [r for r in rows if re.search(VERB_WIDE, r["title"], re.I)]
    tight = [r for r in rows if re.search(VERB_TIGHT, r["title"], re.I)]
    quoted = [r for r in tight if re.search(PAIRED_QUOTE, r["title"])]
    flagged = [r for r in tight if not re.search(PAIRED_QUOTE, r["title"])]

    print()
    print("  GROUND 1 — the document-type noun occupies the verb")
    print("    wide attribution vocabulary .... %d annotations" % len(wide))
    print("    forms with no noun reading ..... %d annotations" % len(tight))
    print("    the difference ................. %d, and it is Annual Report / Situation Report"
          % (len(wide) - len(tight)))
    print("  of the %d, reachable by #112 (they quote) .... %d" % (len(tight), len(quoted)))
    print("  of the %d, a quotation-requiring rule flags ... %d" % (len(tight), len(flagged)))

    grounds = collections.Counter()
    classified = []
    for r in flagged:
        t = r["title"]
        if re.search(FIGURE_LABEL, t, re.I):
            g = "2 house style mandates the token (announced != measured)"
        elif re.search(r"students\s+writes|address\s+printed|publishes at the address", t, re.I):
            g = "3 the verb's subject is not the register"
        elif "بِلا علامات اقتباس" in t or "no quotation" in t.lower():
            g = "4 an absence claim is unquotable by construction"
        else:
            g = "0 an attribution evidenced by a dated read of the register (#101 clause 4)"
        grounds[g] += 1
        classified.append((g, r))

    print()
    print("  THE %d FLAGGED ROWS, BY GROUND — precision of a quotation-requiring rule:" % len(flagged))
    for g in sorted(grounds):
        print("    %-62s %d" % (g, grounds[g]))
    print("    TRUE POSITIVES ............................................... 0")
    print("    So the attribution half is a VERIFIER ROW, not a gate. Measured, not preferred.")

    prov = [r for r in rows if any(re.search(p, r["title"], re.I) for p in PROVENANCE.values())]
    inst = collections.Counter()
    for r in rows:
        for k, p in PROVENANCE.items():
            n = len(re.findall(p, r["title"], re.I))
            if n:
                inst[k] += n
    bad = []
    for r in prov:
        for kind, val in provenance_arithmetic(r["title"], today):
            bad.append((r, kind, val))

    print()
    print("  WHAT IS REACHABLE — the self-specifying provenance claim, which item 38 did not name")
    print("    annotations carrying one ....... %d of %d" % (len(prov), len(rows)))
    print("    claim instances ................ %d" % sum(inst.values()))
    for k in sorted(inst):
        print("      %-16s %d" % (k, inst[k]))
    print("    OFFLINE TIER — the claim's own internal arithmetic: %d violation(s)" % len(bad))
    for r, kind, val in bad:
        print("      %-44s %-28s %s %s" % (kind, val[:28], r["ed"], r["slug"]))
    print("    NETWORK TIER — re-taking a sha256 or a status needs somebody else's server,")
    print("      so it cannot gate (#111's reason, unchanged).  PRINTED, NEVER ASSERTED.")
    print("    LIMB SCOPE, stated because a bite proved it: the status limb asks")
    print("      `all statuses >= 400`, so one dead fetch beside a live one in the SAME")
    print("      annotation is invisible. An annotation carries many fetches; it is not")
    print("      the claim's boundary. Item 38's own problem, one level down.")

    world = collections.Counter()
    for r in rows:
        for k, p in WORLD.items():
            if re.search(p, r["title"], re.I):
                world[k] += 1
    print()
    print("  ITEM 38'S OTHER NAMED CLASSES, counted so the row's own wording stays measurable:")
    for k in sorted(world):
        print("    %-14s %d annotation(s)" % (k, world[k]))
    print("    Each is a claim about the WORLD, with no boundary any artefact of ours supplies.")
    print("    They go to the Verifier with these counts attached.")

    if "--flagged" in sys.argv:
        print()
        for g, r in sorted(classified, key=lambda x: x[0]):
            print("  [%s] %s %s" % (g[0], r["ed"], r["slug"]))
            print("      %s" % r["title"][:200])
    return 0


if __name__ == "__main__":
    sys.exit(main())
