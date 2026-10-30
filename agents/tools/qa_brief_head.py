#!/usr/bin/env python3
r"""
qa_brief_head.py — standing assertion 40. Owner: Assertions Engineer.

Closes standing-queue **item 51**, raised 2026-10-28 by the brief function, taken from
the DEFECT head at 2 days — the youngest head this board has ever handed out. Ruling
**#121**.

WHAT IT ASSERTS. The `<head>` of a founder-facing brief agrees with the brief's own
visible face. Four limbs, all of them exact, all of them derived from the artefact
rather than from a list kept anywhere:

  LIMB 1 — TITLE DATE.  Every brief's `<title>` carries a date, and it equals the
  date in its own filename.

  LIMB 2 — BRIEF NUMBER.  Where the description identifies itself with `Brief NN.`
  immediately after its date clause, NN equals the masthead's own `No. NN`.

  LIMB 3 — DESCRIPTION DATE.  The long-form date in that same self-identifying
  prefix equals the filename's date, weekday included.

  LIMB 4 — ONE SUMMARY PER DAY.  No two briefs of DIFFERENT dates carry the same
  description summary. A description summarises one day's artefact; when two dates
  share one summary, at most one of them is described and the other is describing
  somebody else's day.

WHY THIS IS A GATE AND NOT A HABIT. `qa_artefact_render` (assertion 33) renders all
138 founder-facing artefacts in a real browser on every build and asserts nothing
whatever about their `<head>`. Nothing else reads one. The brief is the single
artefact the CHARTER names as the founder's proof-of-work contract, and its `<head>`
is the half of it that reaches a search engine, a link preview and a browser tab —
the half nobody looks at. The mechanism is #119's exactly: each run copies the
previous brief, updates the masthead because it is visible, and leaves the tab title
and the description because they are not. The error then COMPOUNDS, because the next
run copies the stale one forward.

THE POPULATION, MEASURED ON THE DAY THIS WAS WRITTEN (2026-10-30), and it is six
files larger than the row that asked for it:

  * item 51 named THREE briefs carrying an earlier day's summary — 10-19, 10-26,
    10-27. Limb 4 found **NINE**, in seven collisions: 09-09 (from 09-08), 09-11
    (09-10), 10-12 (10-10), 10-14 (10-13), 10-18 and 10-19 (10-17), 10-21 (10-20),
    10-26 and 10-27 (10-25). All nine rewritten from each brief's own Today section
    in the same commit as this file.
  * limbs 1 and 3 found **2026-06-08**, whose `<title>` and description both carry
    **2026-06-07** while its masthead reads *Monday · 08 June 2026 · No. 11*. That
    one is derivable, and it is the eleventh instance of a class the 10-28 run
    repaired ten of **by hand** — which is this operation's own rule back again: a
    hand pass over a population is a measurement of the ten it looked at.

WHY LIMB 2's KNOWN FALSE POSITIVES ARE NOT AN EXEMPTION LIST. Three briefs mention
an earlier brief's number in their description ON PURPOSE and are correct —
`2026-07-09` (*Brief 28 planned to hold them*), `2026-08-03` (*yesterday's daily
commit (Brief 41 + Australia AR) never landed*), `2026-08-10` (*Brief 48 and the
weekly review ride today's block*). A check that grepped the description for
`Brief NN` would have to carry those three as exceptions forever. It does not need
to: the brief's self-identification is a POSITION, not a string — `Brief NN.`
immediately after the date clause — and a reference in running prose is never in
that position. The boundary is the artefact's own, which is #113's method applied
to a description instead of to a name.

LIMB 4's ONE EXCEPTION IS A LITERAL, FOR THE SAME REASON. Fourteen briefs from
2026-05-28 to 2026-06-11 carry the template's placeholder — the exact string
`Yesterday, today, tomorrow.` — which describes no day and therefore misdescribes
none. The exception is that literal string, counted and printed on every run, not a
list of fourteen filenames: a filename list would hide a fifteenth placeholder
written tomorrow, and the literal cannot.

WHAT IS MEASURED AND DELIBERATELY NOT ASSERTED, with the reason (#93). The sharp
question behind item 51 is whether a description's CLAIM is drawn from the brief it
sits on, and the obvious instrument is vocabulary provenance: the share of the
description's distinctive words that appear nowhere in the brief's own rendered
text. It was built, measured over all 104 briefs that carry a summary, and it does
not separate — median 7%, and the highest-scoring file in the corpus (`2026-09-27`,
75%) is a perfectly correct description written in paraphrase, while two of item
51's three known defects sit below ten correct ones. A floor anywhere on that
distribution either reds the build on good prose or passes the defect. It is printed
with its top rows so that no later run re-derives it as a gate and believes it found
something; the honest negative result is the finding.

ALSO PRINTED, NOT ASSERTED — the coverage gap this tool can see and not close:
**15 of the 20 weekly reviews in `agents/reviews/` carry no `<meta
name="description">` at all.** The founder reads the weekly review; a link to one
previews with whatever the client invents. Their `<title>` dates ARE asserted here,
because they exist. Writing 15 descriptions is editorial work and is queued (item
56) rather than done by the instrument that found it — a check whose author also
writes the prose it checks is #75's defect one desk over.

WHY IT TAKES THE REPOSITORY ROOT, not `dist`: a brief is never built. It is in
`postbuild` because that is where a gate this identity can wire lives (an autonomous
run is refused write access to `.github/workflows/**`), not because it has anything
to do with the build. **It is the TWELFTH gate handed the root, and `CLAUDE.md`
says fifth** — that file numbered the first five as they landed (`qa_packet_figures`,
`qa_pair_frontmatter`, `qa_patch_queue`, `qa_register_shape`, `qa_bridge_coverage`)
and then stopped on 2026-10-10, so the sixth through eleventh
(`qa_artefact_render`, `qa_composition`, `qa_claim_registers`,
`qa_citation_identity`, `qa_acronym_evidence`, `qa_annotation_figures`) were never
numbered. An ordinal in prose is a running count, and a running count with no named
maintainer is #57 — derived here from `web/package.json` rather than read from that
sentence.

EXIT CODES.  0 = clean · 1 = a limb failed · 4 = refused (no briefs found).

PROVED BOTH WAYS (#35), on copies in /tmp, every injection asserted to have changed
the file before the check ran on it (#35's 09-14 addendum):
  control  the repaired tree, 118 briefs                              exit 0
  bite 1   one brief's title date set back one day                    exit 1  limb 1
  bite 2   one brief's description `Brief NN` set to its neighbour's   exit 1  limb 2
  bite 3   one brief's description weekday changed, date left alone    exit 1  limb 3
  bite 4   the 10-25 summary restored onto 10-26, as it really was     exit 1  limb 4
  control  a description that MENTIONS `Brief 28` in running prose     exit 0  limb 2
  control  a fifteenth brief carrying the placeholder literal          exit 0  limb 4
"""

import datetime
import glob
import html
import os
import re
import statistics
import sys

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# The template's placeholder. A literal, not a filename list - see the header.
PLACEHOLDER = "Yesterday, today, tomorrow."

# The self-identifying prefix: a date clause, then optionally this brief's own
# number. Anything after this is the summary; anything inside it is the brief
# naming itself.
PREFIX = re.compile(
    r"^(?P<lead>Manager\s*(?:→|to|->)\s*Founder\s+[a-z- ]*brief\s+for\s+"
    r"(?:(?P<weekday>[A-Z][a-z]+day)\s+)?"
    r"(?P<day>\d{1,2})\s+(?P<month>[A-Z][a-z]+)\s+(?P<year>\d{4})\s*\.\s*"
    r"(?:Brief\s+(?P<num>\d+)\s*\.\s*)?)"
)

STOP = {"founder", "manager", "yesterday", "tomorrow", "madar"}


def strip_tags(raw):
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", s))


def read_artefact(path):
    raw = open(path, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", raw, re.S)
    desc = re.search(r'<meta\s+name="description"\s+content="(.*?)"\s*/?>', raw, re.S)
    mast = re.search(r"No\.\s*(\d+)", raw)
    return {
        "path": path,
        "name": os.path.basename(path),
        "title": html.unescape(title.group(1)).strip() if title else None,
        "desc": html.unescape(desc.group(1)).strip() if desc else None,
        "masthead": mast.group(1) if mast else None,
        "body": strip_tags(raw),
    }


def file_date(name):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", name)
    if not m:
        return None
    return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    brief_paths = sorted(glob.glob(os.path.join(root, "agents/briefs/*daily-brief*.html")))
    review_paths = sorted(glob.glob(os.path.join(root, "agents/reviews/*.html")))
    other = [p for p in sorted(glob.glob(os.path.join(root, "agents/briefs/*.html")))
             if p not in brief_paths]

    if not brief_paths:
        print("REFUSED qa_brief_head — no briefs found under agents/briefs/. "
              "This tool asserts nothing about an empty population; it refuses "
              "rather than passing vacuously (08-16 silent-pass trap).")
        sys.exit(4)

    briefs = [read_artefact(p) for p in brief_paths]
    reviews = [read_artefact(p) for p in review_paths]

    print("qa_brief_head — the founder-facing head, the half of a brief nobody looks at")
    print("  briefs read ................ %d  (agents/briefs/*daily-brief*.html)" % len(briefs))
    print("  weekly reviews read ........ %d  (agents/reviews/*.html)" % len(reviews))
    for p in other:
        print("  out of scope ............... %s — in agents/briefs/ and not a brief: "
              "no masthead number, so limbs 2 and 4 have no subject" % os.path.basename(p))

    fail = []

    # ---- LIMB 1 + 3 ------------------------------------------------------
    no_title_date = []
    for a in briefs + reviews:
        fd = file_date(a["name"])
        if a["title"] is None:
            fail.append("limb 1 — %s has no <title> at all" % a["name"])
            continue
        m = re.search(r"\d{4}-\d{2}-\d{2}", a["title"])
        if not m:
            no_title_date.append(a["name"])
            continue
        if m.group(0) != fd.isoformat():
            fail.append("limb 1 — %s: <title> says %s, the filename says %s"
                        % (a["name"], m.group(0), fd.isoformat()))
    if no_title_date:
        fail.append("limb 1 — %d artefact(s) carry a <title> with no date: %s"
                    % (len(no_title_date), ", ".join(no_title_date)))

    # ---- LIMB 2 + 3 (the self-identifying prefix) ------------------------
    placeholders = []
    summaries = {}
    no_prefix = []
    for a in briefs:
        fd = file_date(a["name"])
        if a["desc"] is None:
            fail.append("limb 3 — %s carries no <meta name=\"description\">; the "
                        "brief is the artefact the CHARTER names as the proof-of-work "
                        "contract and its preview text is not optional" % a["name"])
            continue
        m = PREFIX.match(a["desc"])
        if not m:
            no_prefix.append(a["name"])
            continue
        want = "%d %s %d" % (fd.day, MONTHS[fd.month - 1], fd.year)
        got = "%d %s %s" % (int(m.group("day")), m.group("month"), m.group("year"))
        if got != want:
            fail.append("limb 3 — %s: description says %s, the filename says %s"
                        % (a["name"], got, want))
        wd = m.group("weekday")
        if wd and wd != fd.strftime("%A"):
            fail.append("limb 3 — %s: description says %s, %s was a %s"
                        % (a["name"], wd, fd.isoformat(), fd.strftime("%A")))
        num = m.group("num")
        if num is not None:
            if a["masthead"] is None:
                fail.append("limb 2 — %s: description says Brief %s and the page "
                            "carries no masthead number to agree with" % (a["name"], num))
            elif num.lstrip("0") != a["masthead"].lstrip("0"):
                fail.append("limb 2 — %s: description says Brief %s, the masthead says "
                            "No. %s" % (a["name"], num, a["masthead"]))
        tail = a["desc"][m.end():].strip()
        if tail == PLACEHOLDER:
            placeholders.append(a["name"])
        elif tail:
            summaries.setdefault(tail, []).append((fd, a))

    if no_prefix:
        fail.append("limb 3 — %d brief(s) carry a description with no self-identifying "
                    "date clause, so nothing in the head can be compared with the face: "
                    "%s" % (len(no_prefix), ", ".join(no_prefix)))

    # ---- LIMB 4 ----------------------------------------------------------
    collisions = []
    for tail, members in summaries.items():
        dates = sorted({fd for fd, _ in members})
        if len(dates) > 1:
            collisions.append((dates, [a["name"] for _, a in members], tail))
    for dates, names, tail in sorted(collisions):
        fail.append("limb 4 — %d briefs on %d different dates share one summary (%s): "
                    "%s — at most one of them is describing its own day, and this check "
                    "cannot say which; the run that wrote them can"
                    % (len(names), len(dates), ", ".join(d.isoformat() for d in dates),
                       tail[:90] + ("…" if len(tail) > 90 else "")))

    print("  limb 4 — %d distinct summaries over %d briefs; %d carrying the template "
          "placeholder %r, which describes no day"
          % (len(summaries), len(briefs), len(placeholders), PLACEHOLDER))

    # ---- MEASURED, NOT ASSERTED: vocabulary provenance -------------------
    rates = []
    for tail, members in summaries.items():
        for _, a in members:
            words = {w for w in re.findall(r"[a-z][a-z'’-]{5,}", tail.lower())}
            words -= STOP
            if not words:
                continue
            body = a["body"].lower()
            missing = sorted(w for w in words if w not in body)
            rates.append((len(missing) / len(words), a["name"][:10], len(words), missing))
    if rates:
        rates.sort(reverse=True)
        med = statistics.median(r[0] for r in rates)
        print()
        print("  MEASURED, NOT ASSERTED — vocabulary provenance: the share of a "
              "description's distinctive words that appear NOWHERE in the brief's own "
              "rendered text. Median %.0f%% over %d briefs. It does NOT separate a "
              "stale summary from honest paraphrase and must not become a floor "
              "(#93): the top row below is a CORRECT description." % (med * 100, len(rates)))
        for r in rates[:5]:
            print("      %5.0f%%  %s  %2d distinctive word(s)  absent: %s"
                  % (r[0] * 100, r[1], r[2], ", ".join(r[3][:6])))

    # ---- MEASURED, NOT ASSERTED: the reviews' missing descriptions -------
    bare = [a["name"] for a in reviews if a["desc"] is None]
    if bare:
        print()
        print("  MEASURED, NOT ASSERTED — %d of %d weekly reviews carry NO "
              "<meta name=\"description\"> at all, so a link to one previews with "
              "whatever the client invents. The founder reads the weekly review. "
              "Writing them is editorial work and is standing-queue item 56; an "
              "instrument that wrote the prose it checks would be reading its answer "
              "off its own field." % (len(bare), len(reviews)))

    if fail:
        print()
        print("qa_brief_head: FAIL — %d finding(s):" % len(fail))
        for f in fail:
            print("  %s" % f)
        print()
        print("A brief's head is the half that reaches a tab, a link preview and a "
              "search engine. It is copied forward every morning and it is never "
              "looked at, which is why it compounds and why this is a gate.")
        sys.exit(1)

    print()
    print("CLEAN qa_brief_head — %d briefs and %d reviews: every title date matches "
          "its own filename, every self-identified brief number matches its own "
          "masthead, every description date matches its own weekday, and no two days "
          "share a summary." % (len(briefs), len(reviews)))
    sys.exit(0)


if __name__ == "__main__":
    main()
