#!/usr/bin/env python3
"""sample_coverage.py — how much of its own subject does each assertion load?

Standing-queue item 41, raised 2026-10-25 as the daily's forward question and taken
at the head on 2026-11-19 at 25 days old. The question, in its own words:

    Which of our gating assertions read a SAMPLE rather than a population, and how
    many instances live outside each sample?

and the first cut it asked for:

    for each assertion, print `N of M` beside its verdict, the way
    `qa_bridge_coverage` prints 2.3% instead of implying 100%.

THIS IS A MEASUREMENT, NOT AN ASSERTION.  No `qa_` prefix, so it is outside the
counting glob and no count in CLAUDE.md moves.  It fails no build.  It could not
honestly gate anything: a floor on coverage would red the build on every instrument
this operation has deliberately built as a sample, which is #93's reasoning, and the
right response to a sample is to know its fraction rather than to forbid it.

WHAT IS CLASSIFIED, AND WHY NOT WHAT THE HEADERS SAY
----------------------------------------------------
Ruling #150 (2026-11-18) is one day old and its lesson applies directly: an
instrument that decides what KIND of thing something is must test the property it
means, not the label the thing happens to sit under.  Several of our tools say in
their own headers whether they read a sample.  Those sentences are prose, they were
true the day they were written, and item 67 is a whole queue row about exactly that
class.  So nothing here reads a header.

The property this tool actually means is:

    DOES THE SET OF DOCUMENTS THIS INSTRUMENT READS GROW WHEN THE CORPUS GROWS?

That is decidable from the source and it is the thing a reader cares about, because
it is the difference between a gate that will see the next page we publish and one
that will not.  A tool that enumerates its input by globbing or walking a directory
grows; a tool that names its documents in a literal written into the file does not,
and cannot, until somebody edits it.

    POPULATION   the instrument enumerates its documents from the tree
    MIXED        it does both — it enumerates from the tree AND carries a literal
                 list of documents.  This is the dangerous shape and it is why the
                 bucket exists: a sampled limb sitting inside an instrument whose
                 verdict reads as a population statement.  #57 earned on this tool
                 the day it was written — a bucket set is an enumeration too, and a
                 three-bucket version of this would have printed those tools as
                 POPULATION and hidden the very thing item 41 asked for.
    SAMPLE       the instrument names its documents in a source literal and never
                 enumerates; N is the size of that literal and M is the served
                 population
    NOT PAGE-SCOPED
                 the instrument's subject is not a set of served documents at all
                 (a feed, a stylesheet, a workflow file, a register, frontmatter,
                 this repository's own prose).  N of M is not a defined quantity
                 for these and inventing one would be worse than printing none.

The classification is static, which is a real limit and is printed as one: a tool
that built its target list at runtime would be misread, and the evidence for every
call is printed beside it so the reader can check rather than trust.

PROVED BOTH WAYS (2026-11-19, and recorded in agents/tools/proofs/):
  control  the five instruments item 41 names by hand come back at exactly the
           figures item 41 states — qa_render 4, qa_arabic_shaping 7,
           qa_arabic_joining 4, qa_font_payload 6, qa_artefact_render POPULATION.
  bite     a literal target list injected into a globbing tool is reclassified
           SAMPLE; a target removed from a sample moves its N; a glob added to a
           sample reclassifies it POPULATION.  Each injection is asserted to have
           changed the file before the tool is re-run on it (2026-09-14).
"""

import argparse
import ast
import pathlib
import re
import sys

# A string literal that names a served document: an absolute site route, or a
# dist-relative path at an index.html.  Deliberately narrow — a partial match is
# printed as evidence, never silently counted.
ROUTE = re.compile(r"^/madar(/|$)|(^|/)index\.html$|\.html$")

# A bare file EXTENSION is not a document.  `qa_css_tokens` carries
# MARKUP_EXT = ['.html', '.astro', ...] and the first version of this tool
# classified it MIXED at 4 of 139 on the strength of `.html`.  That is ruling
# #150's own trap sprung inside the instrument written to answer a question about
# it: the pattern tested the SHAPE of the string and not the property meant, which
# is `does this name a document we serve`.  A string with no path separator and a
# leading dot names a kind of file, never a file.
EXT = re.compile(r"^\.[A-Za-z0-9]+$")

GLOBBY = {"glob", "rglob", "iterdir", "walk", "scandir"}


def string_literals(node):
    """Every str constant anywhere inside an AST node."""
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            out.append(n.value)
    return out


def analyse(path):
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src)

    # --- does it enumerate from the tree? -------------------------------------
    globs = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            fn = n.func
            name = getattr(fn, "attr", None) or getattr(fn, "id", None)
            if name in GLOBBY:
                args = string_literals(n)
                globs.append("%s(%s)" % (name, ", ".join(repr(a) for a in args) or ""))

    # --- does it name its documents in a module-level literal? ----------------
    samples = []
    for n in tree.body:
        if not isinstance(n, ast.Assign):
            continue
        targets = [t.id for t in n.targets if isinstance(t, ast.Name)]
        if not targets or not all(t.isupper() for t in targets):
            continue
        if not isinstance(n.value, (ast.List, ast.Tuple)):
            continue
        routes = [s for s in string_literals(n.value)
                  if ROUTE.search(s) and not EXT.match(s)]
        if routes:
            samples.append((targets[0], len(n.value.elts), routes))

    return globs, samples


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="the repository root")
    ap.add_argument("--verbose", action="store_true",
                    help="print each instrument's evidence, not just its verdict")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    tools = sorted((root / "agents" / "tools").glob("qa_*.py"))
    if not tools:
        print("FAIL  no qa_*.py under agents/tools", file=sys.stderr)
        return 1

    dist = root / "web" / "dist"
    served = sorted(dist.rglob("*.html")) if dist.is_dir() else []
    M = len(served)
    if not M:
        print("REFUSED  web/dist holds no html — the denominator is the SERVED\n"
              "         population and there is nothing served to count.  Build first;\n"
              "         a coverage fraction over an absent corpus is a number about\n"
              "         this machine, not about the publication.", file=sys.stderr)
        return 4

    pop, mix, smp, nps = [], [], [], []
    for t in tools:
        globs, samples = analyse(t)
        if globs and samples:
            n = max(s[1] for s in samples)
            mix.append((t.name, n, samples, globs))
        elif globs:
            pop.append((t.name, globs))
        elif samples:
            n = max(s[1] for s in samples)
            smp.append((t.name, n, samples))
        else:
            nps.append(t.name)

    print("sample_coverage — N of M for every standing assertion, derived from the "
          "sources\n  and never from their headers (#150: test the property, not the label)")
    print("  served population M ........ %d documents under web/dist" % M)
    print("  instruments read ........... %d  (agents/tools/qa_*.py)" % len(tools))
    print()

    print("  POPULATION — enumerates its documents from the tree, so it grows with "
          "the corpus (%d)" % len(pop))
    for name, globs in pop:
        print("    %-28s %s" % (name[:-3], globs[0][:60]))
        if args.verbose:
            for g in globs[1:]:
                print("    %-28s %s" % ("", g[:60]))
    print()

    print("  MIXED — enumerates from the tree AND carries a literal document list, so "
          "part of\n    its verdict is a population statement and part of it is a sample (%d)"
          % len(mix))
    for name, n, samples, globs in sorted(mix, key=lambda r: r[1]):
        print("    %-28s %3d of %-4d %5.1f%%   %s   beside %s"
              % (name[:-3], n, M, 100.0 * n / M, samples[0][0], globs[0][:28]))
        if args.verbose:
            for r in samples[0][2]:
                print("    %-28s   %s" % ("", r))
    print()

    print("  SAMPLE — names its documents in a source literal and never enumerates, so it "
          "does NOT\n    grow with the corpus (%d)" % len(smp))
    for name, n, samples in sorted(smp, key=lambda r: r[1]):
        print("    %-28s %3d of %-4d %5.1f%%   %s"
              % (name[:-3], n, M, 100.0 * n / M, samples[0][0]))
        if args.verbose:
            for r in samples[0][2]:
                print("    %-28s   %s" % ("", r))
    print()

    print("  NOT PAGE-SCOPED — subject is not a set of served documents, so N of M "
          "is undefined (%d)" % len(nps))
    line = "    "
    for name in nps:
        if len(line) + len(name) > 92:
            print(line); line = "    "
        line += name[:-3] + "  "
    if line.strip():
        print(line)
    print()

    allsmp = [(n, nm) for nm, n, _ in smp] + [(n, nm) for nm, n, _, _ in mix]
    covered = sum(n for n, _ in allsmp)
    print("  THE ANSWER TO ITEM 41's FIRST HALF, in one line:")
    print("    %d of %d instruments are page-scoped: %d read the population, %d are "
          "MIXED and %d\n    read nothing but a sample.  (A MIXED count of zero is a "
          "result, not an absence.)"
          % (len(pop) + len(mix) + len(smp), len(tools), len(pop), len(mix), len(smp)))
    if allsmp:
        print("    The sampled limbs load %d document-slots in total against a served "
              "population\n    of %d, and the widest of them sees %.1f%% of what it is "
              "a statement about."
              % (covered, M, 100.0 * max(n for n, _ in allsmp) / M))
    print()
    print("  LIMIT, printed rather than left to be discovered: this is a STATIC read of")
    print("    the sources.  An instrument that assembled its targets at runtime would")
    print("    be classified wrongly here, and the evidence above is printed so that a")
    print("    reader can check the verdict instead of trusting it.  Nothing in this")
    print("    tool reads a header sentence, because a header is prose and prose was")
    print("    true the day it was written (standing-queue item 67).")
    print("    The known instance, found by hand-reading on the day this tool was")
    print("    written: qa_live_drift derives its URL SET from the sitemap it fetches,")
    print("    which no glob can show, while its byte-compare limb reads the literal")
    print("    four below.  A static read sees the half that is written down.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
