#!/usr/bin/env python3
r"""
qa_register_shape.py — standing assertion 30. Owner: Assertions Engineer.

Closes standing-queue **item 3**, raised 2026-09-13 at the weekly review, displaced
from the head six times, 24 days open. Ruling **#90**.

WHAT IT ASSERTS, in two limbs that share one input and nothing else.

  LIMB 1 — SHAPE.  Every data row of every table in every hand-maintained markdown
  file the operation keeps carries exactly as many pipe-fields as the header that
  governs it. Twenty-one malformed rows have been repaired by hand in three days
  (five in guidebook §3 on 10-04, twelve in guidebook §1 on 10-05, three wrapped
  rows in the Edition 05 ledger plus one queue row on 10-06) and every one of them
  was invisible to every row count and every range check ever run. A row with a
  missing cell renders with that column silently blank; a row that wraps across
  physical lines TERMINATES its table and dumps the remainder into the page as
  loose prose. Neither has ever changed a number.

  LIMB 2 — REGISTER.  The ruling register's range and §1's row count are DERIVED
  from the rows on disk and compared against every place the operation quotes
  them. This is the 2026-09-20 four-count rule — *a filing run moves §3's range,
  §3's heading, §1's count line, and the ruling range quoted in CLAUDE.md* — made
  into a gate instead of a habit. Seven runs executed it correctly by hand and the
  rule still leaked twice in its first three days (09-23, 09-25), which is the
  2026-09-13 ruling exactly: *a hand-run assertion is a habit, not a gate.*

WHY THE TWO LIMBS ARE ONE TOOL. Limb 2 cannot be trusted without limb 1 and the
operation has already paid to learn it. On 2026-10-04 five §3 rows (#80–#84) were
three columns wide in a four-column table, so five rulings were unreachable from
the canonical register **while every range check passed** — the range counted the
rows and the rows were malformed. A count over rows whose shape is unasserted is a
count over a population it cannot see the edge of.

WHY IT IS NOT IN qa_census. The census cross-checks a tool's printed number against
a population it derives independently from the content collection or from `dist`.
This tool's populations are markdown table rows and ruling numbers; the census has
no independent derivation for either, and a census row whose "expected" value is
read from the same file the tool reads is the self-agreement defect (#57) with two
names on it. Stated here rather than left unexplained, per the 2026-09-13 rule.

THREE THINGS FOUND BY MEASUREMENT WHILE BUILDING IT, each of which changed the code:

  (a) FENCES MUST BE SKIPPED.  `|| [ $? -eq 3 ]` inside a bash fence in
      `agents/patches/2026-10-06-build-served-manifest-check.md` is a shell
      or-operator, not a one-cell table row. A shape check that does not know
      about ``` reports every piped shell command in the operation's own
      documentation as a defect. This is 2026-09-14's input-side question —
      *where does the string I am looking for also legitimately appear?*

  (b) CONTINUATION BLOCKS INHERIT, BUT ONLY WITHIN THEIR HEADING.  The
      guidebook's §1 and §3 "tables" are not tables; they are 11 and 9
      pipe-blocks separated by prose, one header between them. A checker that
      demands a header per block reports 18 of INDEX.md's 21 blocks as
      headerless. So a header governs the rows that follow it — but it is RESET
      at the next ATX heading of any level, because a header governing to
      end-of-file lets a genuinely orphaned table two sections below pass on a
      coincidentally equal width. That narrowing was found by this tool's own
      proof harness failing on the headerless-row bite, and all three candidate
      scopes (end-of-file, end-of-h2, end-of-any-heading) are equally silent on
      the real tree — so the strictest one was free.

  (c) ESCAPED PIPES ARE NOT DELIMITERS.  `re.split(r'(?<!\\)\|', row)`, and the
      specification carried in the queue for 23 days said `row.split("|")`,
      which false-positives on exactly the rows that escape a pipe correctly.
      Found on 2026-10-06 by the row that specifies the check failing it.

SCOPE. `DOC_GLOBS` below, which is every hand-maintained markdown tree and is
printed by name on every run. The 10-06 hand-run covered 7 files, 34 tables and
255 rows; this covers 715 files and 2,867 data rows — and the three real malformed
rows it found on first contact were all outside those 7 files, two of them in
Edition 05 verification verdicts four days before the wave flip.

EXIT CODES
  0  clean
  1  a malformed row, or a quoted count disagreeing with the rows on disk
  2  usage
  3  failure to check — the register's own structure could not be located at all
     (a missing §3 table is not a clean register; #16's silent-pass trap)

USAGE
  python3 agents/tools/qa_register_shape.py .            # both limbs
  python3 agents/tools/qa_register_shape.py . --shape    # limb 1 only
  python3 agents/tools/qa_register_shape.py . --register # limb 2 only
"""

import glob
import os
import re
import sys

# Every hand-maintained markdown tree. `web/` is in because the few .md files
# under it are hand-written notes; node_modules is excluded by name below.
DOC_GLOBS = [
    "*.md",
    "agents/**/*.md",
    "content-drafts/**/*.md",
    "docs/**/*.md",
    "design-assets/**/*.md",
    "social-drafts/**/*.md",
    "web/**/*.md",
    ".github/**/*.md",
]
EXCLUDE_PARTS = ("node_modules", ".git")

DELIM = re.compile(r"^\|[\s:|\-]+\|$")
FENCE = re.compile(r"^\s*(```|~~~)")
# A header's authority ends at the next heading of ANY level. See note (b).
HEADING = re.compile(r"^#{1,6}\s")

INDEX = "agents/guidebook/INDEX.md"
CLAUDE = "CLAUDE.md"

WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90,
}


def fields(row):
    """Pipe-fields of a table row. An ESCAPED pipe is not a delimiter."""
    return re.split(r"(?<!\\)\|", row)


def words_to_int(text):
    """'Eighty-five' -> 85, 'One hundred four' -> 104. None if not a number word.

    `hundred` MULTIPLIES rather than adds, so it cannot be folded into WORDS:
    a plain sum would read 'one hundred' as 101. It was added 2026-10-17, the
    day Section 1 reached a hundred rows and this check became unable to pass
    for any true value — it refused the count correctly and then had no number
    to accept, which is the right failure and still a failure. A ceiling that
    is only reached once is still a ceiling.
    """
    # `and` is a connective, never a value: "one hundred and one" is 101 and
    # "one hundred one" is the same number written by someone else. Dropped
    # before the sum rather than mapped to 0, so an unknown word still refuses.
    parts = [p for p in re.split(r"[\s-]+", text.strip().lower()) if p and p != "and"]
    if not parts or not all(p in WORDS or p == "hundred" for p in parts):
        return None
    total = 0
    current = 0
    for p in parts:
        if p == "hundred":
            current = (current or 1) * 100
            total += current
            current = 0
        else:
            current += WORDS[p]
    return total + current


def doc_files(root):
    out = set()
    for pattern in DOC_GLOBS:
        for path in glob.glob(os.path.join(root, pattern), recursive=True):
            rel = os.path.relpath(path, root)
            if any(part in EXCLUDE_PARTS for part in rel.split(os.sep)):
                continue
            if os.path.isfile(path):
                out.add(rel)
    return sorted(out)


def scan_tables(lines):
    """
    Walk a file's lines and yield one record per table data row:
        (lineno_1based, n_fields, expected_or_None, kind)
    `kind` is "row" or "wrapped". `expected` is the governing header's field
    count, or None when no header governs the row yet.

    A block of pipe-lines whose second line is a delimiter sets a new header.
    Any other pipe-line is a data row governed by the last header seen under the
    CURRENT heading — the guidebook's sections are a single table interrupted by
    prose, so authority has to survive prose; it does not survive a heading.
    Fenced code is skipped entirely: a shell pipe is not a cell boundary.
    """
    expected = None
    header_line = None
    tables = 0
    in_fence = False
    i = 0
    while i < len(lines):
        raw = lines[i]
        if FENCE.match(raw):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        if HEADING.match(raw):
            expected = None          # a header's authority stops at a heading
            header_line = None
        stripped = raw.strip()
        if not stripped.startswith("|"):
            i += 1
            continue
        # A header is a pipe-line immediately followed by a delimiter line.
        if i + 1 < len(lines) and DELIM.match(lines[i + 1].strip()):
            expected = len(fields(stripped))
            header_line = i + 1
            tables += 1
            i += 2
            continue
        if DELIM.match(stripped):
            i += 1
            continue
        kind = "row" if stripped.endswith("|") else "wrapped"
        yield (i + 1, len(fields(stripped)), expected, kind, header_line, stripped)
        i += 1
    yield ("__tables__", tables, None, None, None, None)


def limb_shape(root):
    """Returns (findings, n_files, n_tables, n_rows)."""
    findings = []
    n_tables = n_rows = 0
    files = doc_files(root)
    for rel in files:
        with open(os.path.join(root, rel), encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for rec in scan_tables(lines):
            if rec[0] == "__tables__":
                n_tables += rec[1]
                continue
            lineno, got, expected, kind, header_line, text = rec
            n_rows += 1
            if kind == "wrapped":
                findings.append((rel, lineno,
                                 "row wraps across physical lines — it terminates "
                                 "its table and dumps the remainder into the page",
                                 text))
                continue
            if expected is None:
                findings.append((rel, lineno,
                                 "table row with no header governing it", text))
            elif got != expected:
                findings.append((rel, lineno,
                                 "%d pipe-fields against a %d-field header on line %s"
                                 % (got, expected, header_line), text))
    return findings, len(files), n_tables, n_rows


def section_spans(lines):
    """Map '## ' heading text -> (start_idx, end_idx) over the first occurrence."""
    heads = [(n, ln) for n, ln in enumerate(lines) if ln.startswith("## ")]
    spans = {}
    for k, (n, text) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        spans.setdefault(text, (n, end))
    return spans


def data_rows(lines, start, end):
    """Pipe data rows in [start, end), fences and header/delimiter lines removed."""
    out = []
    in_fence = False
    i = start
    while i < end:
        raw = lines[i]
        if FENCE.match(raw):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        stripped = raw.strip()
        if not stripped.startswith("|"):
            i += 1
            continue
        if i + 1 < len(lines) and DELIM.match(lines[i + 1].strip()):
            i += 2  # header + its delimiter
            continue
        if DELIM.match(stripped):
            i += 1
            continue
        out.append((i + 1, stripped))
        i += 1
    return out


FAMILIES_CUE = "families the register makes visible"

# A family DECLARES its membership with one of these cues. They are written on
# purpose and they are the only place this check will read a numerator from; a
# family that carries a count and no cue is listed as unchecked rather than
# passed. See the long note at the call site (ruling #106).
MEMBERSHIP_CUES = ("MEMBERSHIP OF RECORD", "enumerated here in full",
                   "Count line:")

# <count> members ... : or -- ... #N [sep #N]*
#   The gap between the count and the first token must carry a colon or a dash,
#   which is what distinguishes a DECLARATION ("thirty-five members, reconciled
#   against the population 2026-10-18: #16 . #35 . ...") from a historical
#   aside ("named 2026-08-30 with five members and standing at THIRTY-FIVE").
#   A separator is whitespace, a middot, a comma or the word "and" - never a
#   full stop and never a dash, so the run ends where the list ends.
#
#   THE DASH AND MIDDOT CLASSES CARRY LITERAL CHARACTERS, and the first draft
#   did not. Written as "\u2014" inside a RAW string, the escape is not an
#   escape: the class held a backslash, a "u" and four digits, and no em dash
#   at all. The check then read **2 of the 3 declarations on disk** and printed
#   CLEAN - which is #106 reproduced inside the tool that #106 was filed about,
#   on the same morning, by its author. **The claim-count line is the only
#   reason it was visible**, and it was visible within one run of being added.
INTRO = ":\u2014\u2013-"              # colon, em dash, en dash, hyphen
SEP = "\\s\u00b7,"                    # whitespace, middot, comma
_CUE = r"(?P<cue>" + "|".join(re.escape(c) for c in MEMBERSHIP_CUES) + r")"
_COUNT = r"(?:\*{0,2})(?P<count>[A-Za-z][A-Za-z\-]*)(?:\*{0,2})\s+members"
_RUN = (r"[^.#]{0,120}?[" + INTRO + r"]\s*(?:\*{0,2}\s*)"
        r"(?P<run>\*{0,2}#\d+\*{0,2}"
        r"(?:[" + SEP + r"]+(?:and\s+)?\*{0,2}#\d+\*{0,2})*)")

# THE CUE MAY SIT ON EITHER SIDE OF THE COUNT, and the first draft allowed only
# one order. `MEMBERSHIP OF RECORD - thirty-five members: #16 ...` puts the cue
# first; `THIRTEEN members, enumerated here in full: #45 ...` puts the count
# first. One order read 2 of the 3 declarations and printed clean - the same
# shape as the dash bug above and the same reason it was caught: the claim
# count. Three declarations is the number on disk today; the check says how
# many it read on every run so that a fourth going unread is visible.
MEMBERSHIP = [re.compile(_CUE + r"[^.#]{0,80}?" + _COUNT + _RUN, re.S),
              re.compile(_COUNT + r"[^.#]{0,40}?" + _CUE + _RUN, re.S)]


def membership_declarations(seg):
    """Declared membership lists in `seg`, de-duplicated by the count's span."""
    seen, out = set(), []
    for pat in MEMBERSHIP:
        for m in pat.finditer(seg):
            key = m.span("count")
            if key in seen:
                continue
            seen.add(key)
            out.append(m)
    return out


def families_block(lines, start, end):
    """
    The families list inside §3: the contiguous run of top-level bullets that
    follows the 'families the register makes visible' paragraph. Returns "" if
    the cue is absent, which makes the ratio check silent rather than wrong —
    its absence is reported by the caller as a missing structure, not as a pass.
    """
    cue = None
    for i in range(start, end):
        if FAMILIES_CUE in lines[i]:
            cue = i
            break
    if cue is None:
        return ""
    out = []
    for i in range(cue + 1, end):
        raw, s = lines[i], lines[i].strip()
        if s.startswith("- "):
            out.append(raw)
        elif not s:
            if out:
                out.append(raw)        # blank lines live inside the list
        elif raw[:1] in " \t":
            # An INDENTED paragraph is a continuation of the bullet above it,
            # not the end of the list. Until 2026-10-18 this branch did not
            # exist and the loop broke here, so the block stopped at the first
            # sub-paragraph and returned **five of nine** bullets — and the four
            # it never reached were the four that carry the membership
            # declarations. The structure moved under the parser (ruling #106,
            # limb 2): sub-paragraphs were written beneath the bullets after the
            # parser was written, and a parser that stops at the first thing it
            # does not recognise reports a prefix as the whole.
            if out:
                out.append(raw)
        elif out:
            break                      # un-indented prose ends the list
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out)


def limb_register(root):
    """
    Derive the register from the rows on disk, then check every home that quotes
    it. Returns (findings, derived) where derived carries the numbers for the log.
    """
    findings = []
    path = os.path.join(root, INDEX)
    if not os.path.exists(path):
        print("qa_register_shape: FAILURE TO CHECK — %s is absent" % INDEX)
        sys.exit(3)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.splitlines()
    spans = section_spans(lines)

    s1 = next((t for t in spans if t.startswith("## 1.")), None)
    s3 = next((t for t in spans if t.startswith("## 3. The ruling register")), None)
    if not s1 or not s3:
        print("qa_register_shape: FAILURE TO CHECK — §1 or §3 heading not found "
              "in %s; the register's structure is not where this assertion "
              "looks, which is not a clean register" % INDEX)
        sys.exit(3)

    # --- derive §3: the ruling numbers themselves -------------------------
    start, end = spans[s3]
    rows3 = data_rows(lines, start, end)
    nums = []
    for lineno, row in rows3:
        cells = fields(row)
        if len(cells) > 1 and cells[1].strip().isdigit():
            nums.append(int(cells[1].strip()))
    if not nums:
        print("qa_register_shape: FAILURE TO CHECK — §3 has no numbered rows")
        sys.exit(3)
    lo, hi = min(nums), max(nums)
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    missing = [n for n in range(lo, hi + 1) if n not in nums]
    if lo != 1:
        findings.append("§3's ruling rows start at #%d, not #1" % lo)
    if dupes:
        findings.append("§3 carries duplicate ruling numbers: %s"
                        % ", ".join("#%d" % n for n in dupes))
    if missing:
        findings.append("§3 is missing ruling rows: %s"
                        % ", ".join("#%d" % n for n in missing))

    # --- derive §1: its row count ----------------------------------------
    start1, end1 = spans[s1]
    rows1 = data_rows(lines, start1, end1)
    n1 = len(rows1)

    # --- home 1: §3's heading --------------------------------------------
    m = re.search(r"#1[–\-]#(\d+)", s3)
    if not m:
        findings.append("§3's heading quotes no #1-#N range at all")
    elif int(m.group(1)) != hi:
        findings.append("§3's heading says #1-#%s; its rows end at #%d"
                        % (m.group(1), hi))

    # --- home 2: the series-integrity line -------------------------------
    m = re.search(r"\*\*Series integrity:\s*#1[–\-]#(\d+)", text)
    if not m:
        findings.append("no 'Series integrity: #1-#N' line found in %s" % INDEX)
    elif int(m.group(1)) != hi:
        findings.append("the series-integrity line says #1-#%s; §3's rows end at #%d"
                        % (m.group(1), hi))

    # --- home 3: §1's count line (word form AND numerals) ----------------
    seg = "\n".join(lines[start1:end1])
    # Up to four words, and `and` is allowed between them. The 2026-10-17 fix
    # taught `words_to_int` to multiply by `hundred` on the day §1 reached 100
    # — and left THIS regex at a two-word ceiling, which `One hundred` happens
    # to fit exactly. So the ceiling moved by precisely one row and the check
    # failed again on the very next filing (2026-10-18, `One hundred and one`).
    # A ceiling raised to the value that reached it is not a ceiling removed.
    m = re.search(r"\*\*((?:[A-Za-z\-]+[ \-]){0,3}[A-Za-z\-]+)\s+rows,\s*1\s*→\s*(\d+)", seg)
    if not m:
        findings.append("§1 carries no '**<word> rows, 1 → N**' count line")
    else:
        word, numeral = m.group(1), int(m.group(2))
        if numeral != n1:
            findings.append("§1's count line says 1 → %d; the section holds %d rows"
                            % (numeral, n1))
        spelled = words_to_int(word)
        if spelled is None:
            findings.append("§1's count line opens with '%s', which is not a "
                            "number word this check can read" % word)
        elif spelled != n1:
            findings.append("§1's count line spells '%s' (%d) against %d rows"
                            % (word, spelled, n1))

    # --- the CONDITIONAL FIFTH home, in the half of it that is derivable --
    #
    # The 2026-10-04 amendment's limb one adds a fifth count a filing run owes:
    # the register family's own running member count. The NUMERATOR of that
    # count is not derivable — the 10-06 reconciliation got 24 of 27 members
    # from this register's own labels and recorded the remaining three as a debt
    # rather than inventing them, so asserting it would be asserting a number
    # nobody can check. **The DENOMINATOR is derivable, and it is a count too.**
    #
    # §3's families list carries quotable ratios of the form "twenty-six of
    # eighty-eight rulings". The 2026-10-04 consolidation found exactly this
    # sentence five members stale while the count line three sentences above it
    # in the same bullet was right, and repaired it. It was moved correctly on
    # 10-05 and missed again on 10-06. **So the fifth home has two halves inside
    # one bullet, and only one half is in anyone's enumeration.**
    #
    # SCOPE — and the first scope chosen for this was WRONG, which the tool
    # found on its own first use. "§3 only" excludes the preamble's "Prior
    # consolidation" blocks and the dated consolidation sections, all of which
    # quote ratios that were true when written and must stay as written. But §3
    # itself holds BOTH live claims and narrative about past ones: the
    # series-integrity line's own history quotes every superseded value by
    # design, so scoping to §3 made the register's record of its own drift a
    # build failure. Scoped instead to the FAMILIES LIST — the bullet block
    # introduced by "The eight families the register makes visible" and ending
    # at the next blank-line-separated non-bullet paragraph. A check on
    # hand-maintained prose must be scoped to the structure that holds the
    # claims, never to the section that contains it, because a section contains
    # its own history too.
    seg3 = families_block(lines, start, end)
    ratios_seen = 0
    if not seg3:
        findings.append("§3's families list could not be located (the cue '%s' "
                        "is absent), so its ratio denominators are unchecked — "
                        "which is a missing structure, not a clean one"
                        % FAMILIES_CUE)
    ratio = re.compile(
        r"([A-Za-z][A-Za-z\-]*(?:[ \-][A-Za-z]+)?)\s+of\s+"
        r"([A-Za-z][A-Za-z\-]*(?:[ \-][A-Za-z]+)?)\s+rulings", re.I)
    for m in ratio.finditer(seg3):
        denom = words_to_int(m.group(2))
        if denom is None:
            continue          # not a number word; not a claim about the register
        ratios_seen += 1
        if denom != hi:
            findings.append(
                "§3's families list says '%s' — the denominator is a count of "
                "the whole register and the register holds %d"
                % (m.group(0), hi))

    # --- the FIFTH home's NUMERATOR, and why this code exists -------------
    #
    # The comment forty lines above says the numerator "is not derivable" and
    # gives a real reason: on 2026-10-06 a hand reconciliation recovered 24 of
    # 27 members from this register's own labels and recorded the other three as
    # a debt rather than inventing them, so asserting a count against a list
    # nobody could build would have been asserting an uncheckable number.
    #
    # **That reason expired on 2026-10-11 and the exemption did not.** Ruling
    # #95 established that the three were never missing, and the repair wrote
    # the assertion-discipline family a MEMBERSHIP OF RECORD — an explicit list
    # beside the count — which is precisely the thing whose absence made the
    # numerator undecidable. Nothing re-read this comment. Within six days the
    # count word and its own list disagreed by one (#103 moved the count on
    # 10-17 and did not append), and the operating-cost family's count line sat
    # at *two* for the hours after #105 joined it. Both were found by hand at
    # the 10-18 consolidation, which is the cadence the gate exists to replace.
    # Ruling **#106**: an exemption outlives the reason written beside it,
    # because the reason is prose at the site of the decision and the thing that
    # falsifies it happens somewhere else.
    #
    # WHAT IS ASSERTED, and it is deliberately narrower than "every count":
    # a family that DECLARES its membership must agree with what it declared.
    # The declaration is recognised by one of three cues the operation writes on
    # purpose (below), the count is the `<word> members` claim attached to it,
    # and the population is the run of `#N` tokens that follows — a run ends at
    # the first text that is not a token or a separator, so the `#N`s in the
    # prose *after* a list ("not a member: #91", "kin: #88") are outside it by
    # construction. That boundary is the whole difficulty and it is why this
    # asserts a CONVENTION rather than a count: a family with no declared list
    # is reported as unchecked by name, never silently passed (the silent-pass
    # trap, 08-16).
    declared = membership_declarations(seg3)
    for m in declared:
        word, run = m.group("count"), m.group("run")
        spelled = words_to_int(word)
        members = sorted(set(int(x) for x in re.findall(r"#(\d+)", run)))
        if spelled is None:
            findings.append("a family declares '%s members' and '%s' is not a "
                            "number word this check can read" % (word, word))
        elif spelled != len(members):
            findings.append(
                "a family's declared count says '%s members' (%d) and the list "
                "beside it enumerates %d: %s"
                % (word, spelled, len(members),
                   " ".join("#%d" % n for n in members)))
        for n in members:
            if n > hi:
                findings.append("a family's membership list names #%d and the "
                                "register ends at #%d" % (n, hi))

    # THE SILENT-PASS GUARD, and it is limb 3 of #106. On 2026-10-18 the ratio
    # check was found to have had **zero live claims to read** for eleven days:
    # the only "X of Y rulings" string left in the families list is the literal
    # `N of M rulings` in the preamble, which `words_to_int` correctly refuses,
    # so the limb ran, matched nothing and reported clean. The form it looks for
    # had moved — the families now write "standing at THIRTY-FIVE" and
    # "THIRTEEN members" — and a check whose pattern its subject has stopped
    # using is indistinguishable from a check whose subject is correct.
    # *A ruling that finds nothing to check has failed, not passed* (08-16).
    # The fifth home is not allowed to be entirely unread: zero of BOTH forms
    # is a finding, while zero of one form and some of the other is normal and
    # is printed rather than asserted.
    if ratios_seen == 0 and not declared:
        findings.append(
            "§3's families list carries no count claim this check can read — "
            "no 'X of Y rulings' ratio and no declared membership list (cues: "
            "%s). The fifth home is entirely unchecked, which is a check with "
            "nothing to check rather than a clean one"
            % ", ".join(MEMBERSHIP_CUES))

    # --- home 4: the range quoted in CLAUDE.md's non-negotiables ---------
    cpath = os.path.join(root, CLAUDE)
    if not os.path.exists(cpath):
        findings.append("%s is absent — the fourth home of the range cannot be "
                        "checked" % CLAUDE)
    else:
        with open(cpath, encoding="utf-8") as fh:
            ctext = fh.read()
        m = re.search(r"currently \*\*#1[–\-]#(\d+)\*\*", ctext)
        if not m:
            findings.append("%s quotes no 'currently **#1-#N**' range in its "
                            "non-negotiables" % CLAUDE)
        elif int(m.group(1)) != hi:
            findings.append("%s says the register is currently #1-#%s; §3's rows "
                            "end at #%d" % (CLAUDE, m.group(1), hi))

    return findings, {"rulings": len(nums), "hi": hi, "s1_rows": n1,
                      "s3_blocks_rows": len(rows3),
                      "declared": len(declared), "ratios": ratios_seen}


def main():
    args = [a for a in sys.argv[1:]]
    want_shape = "--register" not in args
    want_register = "--shape" not in args
    positional = [a for a in args if not a.startswith("--")]
    if len(positional) != 1:
        print(__doc__.strip().splitlines()[-4].strip())
        print("usage: qa_register_shape.py <repo-root> [--shape|--register]")
        sys.exit(2)
    root = positional[0]
    if not os.path.isdir(root):
        print("qa_register_shape: FAILURE TO CHECK — %s is not a directory" % root)
        sys.exit(3)

    failed = False

    if want_shape:
        findings, n_files, n_tables, n_rows = limb_shape(root)
        if n_rows == 0:
            print("qa_register_shape: FAILURE TO CHECK — no table rows found "
                  "under %s; the scope found nothing to judge" % root)
            sys.exit(3)
        print("qa_register_shape SHAPE — %d hand-maintained file(s), %d table(s), "
              "%d data row(s)" % (n_files, n_tables, n_rows))
        print("  scope: %s" % " ".join(DOC_GLOBS))
        if findings:
            failed = True
            print("  FAIL — %d malformed row(s):" % len(findings))
            for rel, lineno, why, textrow in findings:
                print("    %s:%d — %s" % (rel, lineno, why))
                print("        %s" % textrow[:140])
        else:
            print("  ok — every data row matches the header that governs it, "
                  "escaped pipes excluded and fenced code skipped")

    if want_register:
        findings, d = limb_register(root)
        print("qa_register_shape REGISTER — derived from the rows on disk: "
              "§3 holds %d ruling row(s) contiguous 1 → %d; §1 holds %d row(s)"
              % (d["rulings"], d["hi"], d["s1_rows"]))
        # Printed BEFORE the verdict and on every run, clean or not: the
        # whole of #106 is that an unread claim and a correct one look the
        # same from outside, so the count of claims read is not a detail of a
        # passing run - it is the only place a decayed check shows.
        print("  fifth home — %d declared membership list(s) read, "
              "%d ratio denominator(s) read" % (d["declared"], d["ratios"]))
        if findings:
            failed = True
            print("  FAIL — %d count(s) disagree with the rows:" % len(findings))
            for why in findings:
                print("    %s" % why)
        else:
            print("  ok — all four homes of the range agree with the rows: "
                  "§3's heading, the series-integrity line, §1's count line "
                  "(word and numeral) and CLAUDE.md's non-negotiables")

    if failed:
        print("\nqa_register_shape: FAIL — see above. A missing cell renders as a "
              "blank column and a wrapped row ends its table; neither ever moved "
              "a number, which is why this is a gate and not a habit.")
        sys.exit(1)

    print("\nCLEAN qa_register_shape — the operation's hand-maintained tables are "
          "well-formed, and the ruling register's range is derived from its own "
          "rows rather than copied between four files.")
    sys.exit(0)


if __name__ == "__main__":
    main()
