#!/usr/bin/env python3
"""
qa_packet_figures.py — standing assertion #23: every figure in a distribution
caption appears in the shipped text of the piece that caption advertises.

WHY (2026-09-23)
----------------
The forward question written into the 2026-09-22 QA log, tested here before
anything new was added:

    Does every figure in `social-drafts/**` appear in the shipped text of the
    piece it names?

It was written because the same defect had just been committed twice in the
same file, five weeks apart, and both times it was found by a human re-reading
rather than by anything that checks:

  * **2026-09-14** — the Sudan captions still said the 2014 programme taught
    *"Arabic and maths"* eleven days after the Verifier's verdict struck exactly
    that claim from the piece in both languages. Filed as ruling #50, *a
    correction has a blast radius*.
  * **2026-09-22** — the Egypt caption still said *"the 120-year-old Thanaweya
    Amma"* a day after the Arabic composition struck the figure from both bodies
    under #41 (no source this piece read carries it). **#50 committed a second
    time inside the document #50 was filed on.**

The reason neither was caught is structural and it is the enumeration family's
own shape, stated three ways in the RUNBOOK: *a green check is scoped to what it
enumerates.* A distribution packet has no `sources[]`, so the Verifier's trace
cannot reach it; it is never built, so all twenty-two standing assertions miss
it; it is not rendered HTML, so the 2026-08-23 artefact-perimeter rule misses it
too. **Three perimeters, and the packet falls outside all three** — while being
the one artefact in the repository whose entire purpose is to be read by people
who will not read the piece.

A caption is not a working note. It is text this publication puts into the world
in its own voice, about a piece, at the moment the piece is least likely to be
re-read. It takes the same figure discipline the prose takes.

WHAT THIS CHECK ENUMERATES
--------------------------
1. Every `<!-- piece: SLUG -->` entry in `social-drafts/**/*.md`. The slug is
   declared, never inferred from a heading — a binding a machine has to guess is
   a binding that silently unbinds when somebody edits a title (#37).
2. Every `<!-- caption:en -->` / `<!-- caption:ar -->` block inside an entry.
3. Every numeral in every caption, against the numerals in the **shipped text**
   of the piece in that same language: its `title`, its `dek` and its body.

WHAT IT DELIBERATELY DOES NOT READ, AND WHY
-------------------------------------------
* **The piece's `sources[]` block.** The annotations are shipped, but they are
  citations *about* registers, and they legitimately carry figures the piece
  does not claim — the superseded value, the rejected pair, the figure a note
  exists to fence off. A caption figure that appears only inside an annotation
  is not a claim the piece makes. Including the block would let a struck figure
  go on passing because its own correction note still names it, which is exactly
  the masking trap of 2026-09-14: *where does the string I am looking for also
  legitimately appear?* The check is scoped to the thing it checks.
* **Everything in the packet that is not inside a caption fence.** Growth's own
  prose about a packet is full of figures that are properties of the packet and
  not of the piece — card dimensions, byte counts, ruling numbers, dates. An
  assertion scoped wider than the caption would drown in true positives about
  the wrong subject and be turned off within a week.
* **`content-drafts/**`.** The second half of the forward question, and the
  answer is no, on purpose. A recon, a verdict and a commission are *working*
  documents whose job is to record figures the piece does not carry — what was
  rejected, what was fenced, what the disagreeing reproduction said. Requiring
  their figures to appear in the piece would invert their function. The
  distribution packet is the artefact that speaks *as the publication*, and it
  is the one that takes this rule.

WHAT IT CANNOT STRUCTURALLY SEE (named, per the 2026-08-23 rule)
----------------------------------------------------------------
* **A figure spelled in words.** «ثمانية عشر مليون دولار» and *twenty years*
  are figures to a reader and invisible here. The Arabic captions carry more of
  these than the English ones, so this check is weaker on the Arabic side by
  construction, and the report prints that asymmetry rather than hiding it.
* **A non-numeric claim.** The 09-14 Sudan defect — *games that teach Arabic and
  maths* — contains no number, and this check would not have caught it. It would
  have caught the 09-22 Egypt defect, and the proof below is that historical
  defect, not a synthetic one.
* **A short figure.** A caption's `3` will match almost any body. The report
  splits the figures it checked into discriminating (≥3 digits) and incidental
  (1–2 digits) so nobody reads a green here as stronger than it is.

PROVED BOTH WAYS (#35), against the real defect rather than an injected one
--------------------------------------------------------------------------
* **Control** — the packet as it stands at 2026-09-23: exit 0.
* **Bite** — the packet as it stood at commit `b4a983f` (2026-09-21), whose
  Egypt caption carried *"the 120-year-old Thanaweya Amma"* while the piece, in
  both languages, no longer did: exit 1, naming `120`. The bite is checked for
  having actually changed the input before the check is run on it, per the
  2026-09-14 rule that a bite which fails to change the artefact reads exactly
  like a passing control.

NOT IN `qa_census` (#19), and here is the reason at the point of exclusion
--------------------------------------------------------------------------
The census computes its populations from `dist` and asserts each instrument's
printed number against a named subset of the served pages. This assertion has no
population in `dist` at all — a distribution packet is never built. It is gated
from `postbuild` in `web/package.json`, the second equal home for gates, because
`.github/workflows/**` is unwritable by the autonomous identity (2026-09-14).

Usage:  python3 agents/tools/qa_packet_figures.py [repo-root]
Exit 0 clean, 1 on any defect. No third-party dependencies.
"""

import os
import re
import sys

ARABIC_INDIC = {ord("\u0660") + i: str(i) for i in range(10)}

PIECE_RE = re.compile(r"<!--\s*piece:\s*([A-Za-z0-9\-]+)\s*-->")
CAPTION_RE = re.compile(
    r"<!--\s*caption:(en|ar)\s*-->(.*?)<!--\s*/caption\s*-->", re.DOTALL
)
# A numeral run, with , . ، and the Arabic thousands separator ٬ allowed INSIDE
# it so "1,911" and "13,705" are one token rather than four.
NUMERAL_RE = re.compile(r"[0-9]+(?:[.,\u060c\u066b\u066c][0-9]+)*")


def normalise(text):
    """Arabic-Indic digits to ASCII. Both sides get this, so a caption written
    in one digit set and a body written in the other still compare."""
    return text.translate(ARABIC_INDIC)


def figures(text):
    """The numeral multiset of a stretch of text, as normalised tokens.

    Group separators are stripped (1,911 -> 1911) so the same value written two
    ways is the same token; a decimal point is kept, because 0.359 and 0359 are
    not the same figure."""
    out = []
    for raw in NUMERAL_RE.findall(normalise(text)):
        tok = raw.replace(",", "").replace("\u060c", "").replace("\u066c", "")
        tok = tok.replace("\u066b", ".")
        out.append(tok)
    return out


def split_frontmatter(raw):
    """Return (frontmatter, body). Articles open with a --- fence."""
    if not raw.startswith("---"):
        return "", raw
    end = raw.find("\n---", 3)
    if end == -1:
        return "", raw
    return raw[3:end], raw[end + 4 :]


def shipped_text(path):
    """Title + dek + date + edition + body. Not sources[] — see the header.

    `date` and `edition` are in because the build renders both on the page and a
    caption legitimately names them (*"New in Edition 02"*, the dateline). They
    were added after the first run of this check reported `02` as missing from
    three live pieces — a true statement about the body and a false one about
    the piece, which is the 2026-09-14 masking trap running the other way: an
    assertion scoped *narrower* than the thing it checks reports the right
    absence for the wrong reason. `sources[]` stays out; it is the only
    frontmatter block whose figures are deliberately not the piece's claims."""
    raw = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(raw)
    parts = [body]
    for field in ("title", "dek", "date", "edition"):
        m = re.search(r"^%s:\s*(.+)$" % field, fm, re.MULTILINE)
        if m:
            parts.append(m.group(1))
    return "\n".join(parts)


def variants(tok):
    """A token and its leading-zero-stripped form. `Edition 02` and
    `edition: 2` are the same edition; `09` and `9` are the same month. Applied
    to the caption side only, and only for all-digit tokens, so a decimal or a
    thousands-grouped value is never rewritten."""
    out = {tok}
    if tok.isdigit():
        out.add(tok.lstrip("0") or "0")
    return out


def collect_corpus(root):
    corpus = {}
    for lang, rel in (("en", "web/src/content/articles"),
                      ("ar", "web/src/content/articles-ar")):
        d = os.path.join(root, rel)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md"):
                continue
            corpus.setdefault(name[:-3], {})[lang] = os.path.join(d, name)
    return corpus


def entries(text):
    """Split a packet into (slug, body) entries at each piece marker."""
    marks = list(PIECE_RE.finditer(text))
    out = []
    for i, m in enumerate(marks):
        stop = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out.append((m.group(1), text[m.end():stop]))
    return out


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    packets_dir = os.path.join(root, "social-drafts")
    corpus = collect_corpus(root)

    defects = []
    notes = []
    n_packets = n_entries = n_captions = 0
    checked = []          # (slug, lang, token)
    one_language = []

    if not os.path.isdir(packets_dir):
        print("qa_packet_figures: FAIL — no social-drafts/ directory at %s" % root)
        return 1
    if not corpus:
        print("qa_packet_figures: FAIL — no article corpus found under web/src/content")
        return 1

    paths = []
    for dirpath, _dirnames, filenames in os.walk(packets_dir):
        for name in sorted(filenames):
            if name.endswith(".md"):
                paths.append(os.path.join(dirpath, name))

    for path in sorted(paths):
        text = open(path, encoding="utf-8").read()
        found = entries(text)
        if not found:
            continue
        n_packets += 1
        rel = os.path.relpath(path, root)
        for slug, body in found:
            n_entries += 1
            if slug not in corpus:
                defects.append(
                    "%s: entry names slug '%s', which is not a piece in either "
                    "collection" % (rel, slug))
                continue
            caps = CAPTION_RE.findall(body)
            if not caps:
                defects.append(
                    "%s [%s]: entry declares a piece and carries no caption "
                    "fence — an entry a machine cannot read is an entry nothing "
                    "checks" % (rel, slug))
                continue
            langs = set(lang for lang, _ in caps)
            if len(langs) < 2:
                one_language.append("%s [%s]: caption in %s only"
                                    % (rel, slug, "/".join(sorted(langs))))
            for lang, caption in caps:
                n_captions += 1
                if lang not in corpus[slug]:
                    defects.append(
                        "%s [%s]: a %s caption exists and the %s piece does not"
                        % (rel, slug, lang.upper(), lang.upper()))
                    continue
                piece = set(figures(shipped_text(corpus[slug][lang])))
                for tok in figures(caption):
                    checked.append((slug, lang, tok))
                    if not (variants(tok) & piece):
                        defects.append(
                            "%s [%s] %s caption: the figure %s does not appear "
                            "in the shipped text of the piece it advertises"
                            % (rel, slug, lang.upper(), tok))

    if n_packets == 0 or n_entries == 0:
        print("qa_packet_figures: FAIL — 0 packet entries found. An assertion "
              "with nothing to check has failed, not passed.")
        return 1

    discriminating = [t for _s, _l, t in checked if len(t.replace(".", "")) >= 3]
    incidental = len(checked) - len(discriminating)
    en = sum(1 for _s, l, _t in checked if l == "en")
    ar = len(checked) - en

    print("qa_packet_figures: %d packet(s) · %d entries · %d captions · "
          "%d figures checked (EN %d / AR %d)"
          % (n_packets, n_entries, n_captions, len(checked), en, ar))
    print("  %d discriminating (3+ digits) · %d incidental (1-2 digits, which "
          "will match almost any body — a green on those is weak and is printed "
          "as weak)" % (len(discriminating), incidental))
    for line in one_language:
        print("  note: %s — reported, not failed: a packet entry may be "
              "legitimately mid-composition, and a gate that blocks a deploy on "
              "an unfinished draft would be turned off within a week." % line)
    for line in notes:
        print("  note: %s" % line)

    if defects:
        print("FAIL qa_packet_figures — %d defect(s):" % len(defects))
        for d in defects:
            print("  - %s" % d)
        return 1

    print("CLEAN qa_packet_figures — every numeral in every distribution "
          "caption appears in the shipped text of the piece that caption "
          "advertises, in that caption's own language.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
