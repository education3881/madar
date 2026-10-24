#!/usr/bin/env python3
r"""
qa_annotation_figures.py — standing assertion 38. Owner: Assertions Engineer.

Closes standing-queue **item 19**, raised 2026-10-16 by the daily's forward question,
displaced from the head seven times, 8 days open. Ruling **#114**.

WHAT IT ASSERTS, in one sentence.  Every QUANTITY printed inside a served annotation
is either printed in the body of the piece that serves it — where the Verifier's eight
trace axes can see it — or recorded, by hand, in a register that says where it was read
from.

WHY IT EXISTS.  Item 19 asked *which of our annotations assert something their own URL
does not support?*, after a `gov.om` citation was found whose parenthetical read "the
issuing body and its mandate; renamed in 2026" against a page that carries no rename,
no date and no instrument.  The item's own sentence named the mechanism: **the
annotation is the ruler every check measures against, and nothing measures the ruler.**

  `qa_sources_alive`      — does the URL answer?
  `qa_claim_registers`    — can the register be re-opened by anybody, ever?
  `qa_citation_identity`  — are the bytes still the document we cited?
  `annotation == sentence` (#45–#47, 09-13) — does the body match the annotation?

All four take the annotation's prose **as given**.  The fourth is the sharp one: it
compares the body against the annotation in the direction body→annotation, so a hedge
dropped from a body is caught and **a claim that exists only in an annotation is not**,
because there is no body sentence to compare it to.  Every numeric instrument this
operation owns reads a body: the numeral-multiset comparison, the one-sided-figure
grep, the prohibited-figure grep, the eight trace axes, #27's two channels.  The
annotation block is **served** — it renders on every article page in both editions —
so a figure that lives only there is a published figure standing outside every numeric
check we have ever built.

THE BOUNDARY, AND WHY IT IS THE ARTEFACT'S RATHER THAN THIS CHECK'S.  #113's lesson one
day old: do not guess where a claim begins; find the boundary the artefact supplies.
Item 19 as written asks the check to classify a parenthetical as *claim* or
*description*, which is a judgment, and the 10-16 negative result on name boundaries is
what judgment-by-detector buys.  It is not needed.  A quantity is **exactly**
extractable — a digit is a digit — and the piece's own body is **exactly** searchable.
So the check never decides whether a parenthetical makes a claim; it asks whether a
number the publication printed is anywhere the publication's own figure discipline can
reach it.

  "~1 million resources"                        -> 1 million, nowhere in the body
  "45.5% -> 32.4% -> 13.9%; ~1.38m students"    -> four quantities, none in the body
  "programme description and goals"             -> no quantity, nothing to assert

WHAT IS LICENSED, AND WHY EACH LICENCE IS A COORDINATE RATHER THAN A CLAIM.  Three
classes of numeral are bibliographic coordinates of the document being cited, not
statements about the world, and the register would drown in them:

  (a) DATES — `6 September 2025`, `May 2025`, `14 Oct 2024`, `2026-05-22`, bare years,
      and year spans `2024/25`, `2024-26`.  A publication date describes the document.
      **Limitation (i), stated rather than hidden:** item 19's own founding instance is
      a date claim (*renamed in 2026*), so this licence cannot see the instance that
      earned the item.  The licence is still right — a bare year in an annotation is a
      publication date far more often than it is an assertion — and what it costs is
      written here instead of being discovered later.
  (b) IDENTIFIERS — a numeral touching a letter: `534IRQ1002`, `PP39`, `QH15`,
      `217/2025/QH15`.  These name the document; they assert nothing.
  (c) PAGE AND SECTION POINTERS — `p. 12`, `pp. 4-7`, `Article 23`, `Table 3`.  A
      pointer into the document is part of the citation.

THE REGISTER IS HAND-WRITTEN, AND THAT IS THE WHOLE DESIGN.  `--emit` prints the rows
it cannot satisfy and **writes nothing**.  If this tool wrote its own register the gate
would be a check reading its answer off the field it supplements — the 09-14 trap in a
new costume: run emit, go green, learn nothing.  A new annotation quantity therefore
reds the build until a human either prints it in the body or records in
`agents/stats/annotation-figures.json` where it was read from.  Provenance must be a
real sentence: the placeholder strings below are refused.

THE SEEDED BACKLOG IS A KNOWN ERROR WITH A KNOWN SIZE.  The register is seeded
2026-10-24 from the population as it stands, every entry marked `UNTRACED
2026-10-24`, because 2026-10-04's limb two is explicit that a point-of-filing rule
leaves a step discontinuity where it was written and never reconciles backward — so the
discontinuity is written down with its size instead of being left to look like
arithmetic.  What the gate buys from today is that the backlog **cannot grow in
silence**.  Working it down is standing-queue work for the Verifier, not this tool's.

USAGE
  python3 agents/tools/qa_annotation_figures.py .            # --check, gated
  python3 agents/tools/qa_annotation_figures.py . --emit     # print unsatisfied rows

EXITS
  0  every annotation quantity is in its own body or carries a provenance
  1  at least one is in neither — the assertion bites
  2  the corpus could not be read (no articles, no frontmatter)
  4  REFUSED — register present but malformed
"""

import json
import pathlib
import re
import sys

REGISTER = pathlib.Path("agents/stats/annotation-figures.json")

EN_DIR = "web/src/content/articles"
AR_DIR = "web/src/content/articles-ar"

PAREN = re.compile(r"\(([^()]*)\)")
TITLE = re.compile(r"-\s+title:\s*\"(.*?)\"\s*\n", re.S)

MONTH = (
    r"(?:January|February|March|April|May|June|July|August|September|October|"
    r"November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)"
)

# (a) dates, (c) pointers — stripped from the parenthetical before tokens are read.
LICENCES = [
    re.compile(r"\d{4}-\d{2}-\d{2}"),                                  # ISO
    re.compile(r"\b\d{1,2}\s+" + MONTH + r"\.?,?\s+\d{4}\b"),          # 6 September 2025
    re.compile(r"\b" + MONTH + r"\.?\s+\d{1,2},?\s+\d{4}\b"),          # September 6, 2025
    re.compile(r"\b" + MONTH + r"\.?\s+\d{4}\b"),                      # May 2025
    re.compile(r"\b\d{1,2}\s+" + MONTH + r"\b"),                       # 14 Oct
    re.compile(r"\b(?:19|20)\d{2}\s*[/–—-]\s*(?:\d{2}|\d{4})\b"),  # 2024/25, 2024-2026
    re.compile(r"\b(?:19|20)\d{2}\b"),                                 # bare year
    re.compile(r"\bp{1,2}\.?\s*\d+(?:\s*[–-]\s*\d+)?", re.I),     # p. 12, pp. 4-7
    re.compile(r"\b(?:Article|Art\.|Table|Figure|Fig\.|Annex|Section|Chapter|Clause)"
               r"s?\s*\d+(?:\.\d+)*", re.I),
    # (d) named legal instruments: the number IS the document's name.
    re.compile(r"\b(?:RA|Resolution|Decree|Decision|Act|Law|Circular|Order|Regulation|"
               r"Directive|Ordinance|Statute|No\.|Project ID)\s*[\d][\d/.–-]*", re.I),
]

# A quantity: a digit run, optionally with thousands separators, decimals or a range.
QUANTITY = re.compile(r"\d[\d.,]*(?:\s*[–—-]\s*\d[\d.,]*)?")

PLACEHOLDERS = {"", "-", "--", "tbd", "todo", "unknown", "n/a", "na", "?", "xxx"}


def read_corpus(root):
    """Approved pieces only. A held file is not part of the publication (09-06)."""
    out = []
    for d, lang in ((EN_DIR, "en"), (AR_DIR, "ar")):
        for path in sorted((root / d).glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if "approved: true" not in text:
                continue
            end = text.find("\n---", 4)
            if end < 0:
                continue
            out.append((path.stem, lang, text[:end], text[end:]))
    return out


def annotations(frontmatter):
    block = re.search(r"\nsources:\n(.*)$", frontmatter, re.S)
    if not block:
        return []
    return [t for t in TITLE.findall(block.group(1) + "\n")]


def quantities(parenthetical):
    """Tokens left after the three licences. Identifiers die on the boundary test."""
    masked = parenthetical
    for pat in LICENCES:
        masked = pat.sub(lambda m: " " * len(m.group(0)), masked)
    found = []
    for m in QUANTITY.finditer(masked):
        tok = m.group(0).strip()
        before = masked[m.start() - 1] if m.start() else " "
        after = masked[m.end()] if m.end() < len(masked) else " "
        if before.isalpha() or after.isalpha():
            continue                       # (b) identifier: a numeral touching a letter
        tok = tok.strip(".,")
        if not tok or not any(c.isdigit() for c in tok):
            continue
        found.append(tok)
    return found


def load_register(root):
    """Returns (slug -> {tokens}, entries, error). Hand-written; never written here."""
    path = root / REGISTER
    if not path.exists():
        return {}, [], None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        entries = raw["entries"]
    except Exception as exc:                                  # noqa: BLE001
        return None, [], f"register at {REGISTER} is not readable: {exc}"
    reg = {}
    for e in entries:
        try:
            slug, token, prov = e["slug"], str(e["token"]), e["provenance"]
        except (KeyError, TypeError):
            return None, [], f"register entry missing slug/token/provenance: {e!r}"
        if prov.strip().lower() in PLACEHOLDERS:
            return None, [], (f"register entry for {slug} / {token} carries a "
                              f"placeholder provenance")
        reg.setdefault(slug, set()).add(token)
    return reg, entries, None


def sweep(root):
    corpus = read_corpus(root)
    rows = []
    for slug, lang, frontmatter, body in corpus:
        for ann in annotations(frontmatter):
            # The WHOLE annotation, not only its parentheticals. Item 19 named the
            # parenthetical because that is where its own instance was; the first
            # bite proved the narrower scope silently: an injected quantity outside
            # the brackets changed the file and the check still exited 0, which is
            # the 09-14 trap exactly. The non-bracketed half of a title is almost
            # always the document's own name, and licences (a) and (d) take those.
            for tok in quantities(ann):
                rows.append({
                    "slug": slug, "lang": lang, "token": tok,
                    "paren": ann, "in_body": tok in body,
                })
    return corpus, rows


def main(argv):
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".").resolve()
    mode = "--emit" if "--emit" in argv else "--check"

    corpus, rows = sweep(root)
    if not corpus:
        print(f"FAIL qa_annotation_figures — no approved articles read under {root}")
        return 2
    if not rows:
        print("FAIL qa_annotation_figures — zero annotation quantities read; "
              "an assertion with nothing to check has failed, not passed (09-13)")
        return 2

    reg, reg_entries, err = load_register(root)
    if reg is None:
        print(f"REFUSED qa_annotation_figures — {err}")
        return 4

    unsatisfied = [r for r in rows
                   if not r["in_body"] and r["token"] not in reg.get(r["slug"], ())]
    annotation_only = [r for r in rows if not r["in_body"]]

    pieces = len({c[0] for c in corpus})
    print(f"qa_annotation_figures — {len(rows)} annotation quantities over "
          f"{pieces} approved pieces ({len(corpus)} files, both editions)")
    print(f"  printed in their own body ..... {len(rows) - len(annotation_only)}")
    print(f"  annotation-only .............. {len(annotation_only)}"
          f" across {len({r['slug'] for r in annotation_only})} pieces")
    print(f"  of those, registered ......... {len(annotation_only) - len(unsatisfied)}")
    untraced = sum(1 for e in reg_entries
                   if e["provenance"].strip().upper().startswith("UNTRACED"))
    if untraced:
        print(f"  registered but UNTRACED ...... {untraced}  <- the 2026-10-24 seeded "
              f"backlog, printed on every run so it cannot shrink out of sight")

    if mode == "--emit":
        print(f"\n  {len(unsatisfied)} row(s) this register does not cover. "
              f"--emit WRITES NOTHING: a gate that seeds its own register is a check "
              f"reading its answer off the field it supplements (09-14).\n")
        for r in unsatisfied:
            print(json.dumps({"slug": r["slug"], "token": r["token"],
                              "provenance": "", "paren": r["paren"][:120]},
                             ensure_ascii=False))
        return 0

    if unsatisfied:
        print(f"\nFAIL qa_annotation_figures — {len(unsatisfied)} annotation quantit"
              f"{'y is' if len(unsatisfied) == 1 else 'ies are'} neither printed in "
              f"their own body nor recorded in {REGISTER}:\n")
        for r in unsatisfied[:40]:
            print(f"  {r['slug']} [{r['lang']}]  {r['token']}")
            print(f"    in: ({r['paren'][:140]})")
        if len(unsatisfied) > 40:
            print(f"  ... and {len(unsatisfied) - 40} more")
        print("\n  Either print the figure in the body, where the Verifier's trace "
              "axes reach it,\n  or record in the register where it was read from "
              "(#114 clause 2). Run --emit for rows.")
        return 1

    print("\nOK qa_annotation_figures — every annotation quantity is in its own body "
          "or carries a provenance")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
