#!/usr/bin/env python3
"""
qa_patch_queue.py — standing assertion #27: a patch staged for a human hand
states nothing about our own machinery that the machinery itself contradicts.

WHY (2026-09-29)
----------------
The forward question carried from 2026-09-28, and it is the first one in this
operation's history that points at an artefact NO check has ever read:

    Every check this operation owns reads an artefact that a machine produced.
    Not one reads the artefacts a human hand will apply. `git apply --check`
    proves a patch APPLIES; nothing proves what it would then ASSERT.

Asked deliberately today, it failed on first contact, on a real staged patch,
one day after that patch was refreshed by a weekly review whose explicit job
was to refresh it.

`agents/patches/2026-09-20-issue-6-default-c-gate-register-comment.patch` adds
a comment block to `.github/workflows/astro-pages.yml` answering the question
"what gates the deploy?". Applied to a scratch tree today it writes FOUR claims,
all of them wrong:

    claim                            patch says    tree contains
    standing assertions              25            26
    of which gate the deploy         22            23
    gated from postbuild             TEN           11
    enumerated postbuild gates       10 names      11  (qa_feed_direction absent)

`git apply --check` returns 0 on it. It applies perfectly. That green is real
and it is about the wrong property — which is the whole finding: **the only
instrument we had for a staged patch measured whether it would land, never
whether what it lands is true.**

THE CADENCE IS THE DEFECT, NOT THE DILIGENCE
--------------------------------------------
The 2026-09-27 weekly review found this same patch stale by four assertions,
regenerated it, re-verified it with `git apply --check`, and wrote a standing
rule: *the weekly review re-reads every open patch against current state.* That
rule was executed correctly. It went stale again in ONE DAY, because assertion
26 (`qa_feed_direction`) landed on Monday 09-28 and the next weekly review is
Sunday 10-04 — so the patch spends six of every seven days holding a number the
tree has moved past.

That is exactly the defect the 2026-09-20 rule diagnosed for the guidebook
register and fixed: *a document maintained on a slower clock than the work it
describes is not out of date by accident — it is out of date by design, and the
fix is to move the cheapest part of the maintenance onto the faster clock.* The
guidebook's range moved to the point of filing and has been true since. The
patch queue was left on the weekly clock. Same shape, same outcome, one
directory over.

And the failure mode here is the worst one available, which is why this is a
gate and not a habit: a stale patch injects its stale numbers **at the moment a
trusting hand applies it**, into the one file the autonomous identity may not
then correct. A wrong unapplied patch is not unapplied work. It is a trap with
a delay fuse, and the identity that lights it cannot put it out.

WHAT THIS CHECK ENUMERATES
--------------------------
1. **The ground truth, derived three ways and never read from prose.** The
   count of standing assertions comes from the files in `agents/tools/`; the
   build-step set from `.github/workflows/astro-pages.yml`; the `postbuild` set
   from `web/package.json`. It never takes a number from `CLAUDE.md`, from a
   brief, or from another patch in order to judge a patch — those are all prose
   about the state, and prose is the thing under test. (The 2026-09-14 trap: an
   assertion must not be able to read its answer off the field it supplements.)

2. **Every numeric claim about the gate register made anywhere in
   `agents/patches/`.** For a `.patch` file this means the ADDED lines and the
   `Subject:` header — the lines the patch would introduce, which is the served
   shape of a patch, plus the commit subject that lands in history. Context
   lines are deliberately NOT read: they are the tree's current state quoted
   back, not a new claim. For a `.md` or `README.md` this means every line,
   because the whole file is the queue asserting things about itself.

3. **The enumerated `postbuild` list, by name and not by cardinality.** The
   issue-6 comment lists the postbuild gates one by one. A list of the right
   length naming the wrong tool is a defect that no count can see — the
   2026-09-19 census lesson (*equal cardinalities are not an agreement*) applied
   to a set of names in a comment.

4. **That each patch still applies.** Kept, because it is cheap and because a
   patch that no longer applies is also unapplied work that has rotted. It is
   reported as what it is: a claim about landing, not about truth.

5. **A superseded number is exempt, by the house marker, and the exemption is
   PRINTED.** This queue's README deliberately records what a patch *used to*
   assert — "it had been sitting here asserting 21 standing assertions of which
   19 gate" — because the staleness is the finding. A tool that reads those as
   current claims flags the record for being an accurate record, which is the
   2026-09-14 masking trap wearing this instrument's own hat: an assertion
   scoped wider than the thing it checks finds the right string for the wrong
   reason. The first draft of this file did exactly that, on its first run.
   The exemption uses the convention the RUNBOOK and the edition ledger already
   use for superseded prose — `~~strikethrough~~` — and every exempt line is
   printed with its numbers, so an exemption can never hide a live claim. Tense
   is deliberately NOT parsed: a marker a writer sets is legible, and a guess
   about "had been" versus "has" is an instrument that fails silently.

WHAT IT DELIBERATELY DOES NOT DO
--------------------------------
It does not edit or regenerate a patch. A patch's prose is the author's, exactly
as a piece's prose is the Editor's — this instrument proves the defect and hands
it over (the 2026-09-27 product-versus-instrument split). It does not judge
non-numeric prose. And it does not fail on a patch that carries no counts at
all: a patch with nothing to contradict is silent, correctly — but the count of
claims read IS printed per file, so a pattern that silently stops matching is
visible instead of green.

THE TOKENIZER CARRIES A SCAR
----------------------------
`qa_[a-z_]+` does not match `qa_a11y_lang`. That character class cost the
2026-09-28 run a wrong gate count and some minutes of believing a safety gate
was missing; this run reproduced it independently within the hour while
establishing ground truth for this very tool. The class here is
`qa_[a-z0-9_]+`, and `main()` asserts that the build-step set it derives
actually contains `qa_a11y_lang` before trusting any number built from it. A
tool that cannot see one of the things it counts has failed, not passed.

USAGE
-----
    python3 agents/tools/qa_patch_queue.py [repo-root]

Exit 0 = clean. Exit 1 = a staged patch contradicts the tree.
Handed the REPOSITORY ROOT, not `dist` — the second such gate after
`qa_packet_figures`, and for the same reason: a patch is never built.
"""

import json
import pathlib
import re
import subprocess
import sys

# Number words that appear in this queue's prose. The issue-6 comment writes
# "The other TEN are gated from postbuild" in words, not digits.
WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "twentyone": 21, "twentytwo": 22, "twentythree": 23,
    "twentyfour": 24, "twentyfive": 25, "twentysix": 26, "twentyseven": 27,
    "twentyeight": 28, "twentynine": 29, "thirty": 30,
}

TOOL_RE = re.compile(r"qa_[a-z0-9_]+")


def as_number(tok):
    """A claim's number, written as a digit or as a word. None if neither."""
    tok = tok.strip().strip("*_`").lower()
    if tok.isdigit():
        return int(tok)
    return WORDS.get(tok.replace("-", "").replace(" ", ""))


# Each pattern names the truth key it is claiming about. The key is what makes
# a match a CLAIM rather than a number that happens to be nearby.
NUM = r"(\*{0,2}[A-Za-z0-9\-]+\*{0,2})"
PATTERNS = [
    # "TOTAL: 25 standing assertions, 22 of which gate the deploy."
    (re.compile(NUM + r"\s+standing assertions,\s*" + NUM +
                r"\s+of which gate", re.I), ("total", "gating")),
    # "26 standing assertions" / "twenty-six standing assertions"
    (re.compile(NUM + r"\s+standing assertions", re.I), ("total",)),
    # "23 of 26 gate the deploy" / "the ratio 23 of 25" / "makes it 24 of 26"
    (re.compile(r"\b(?:ratio|makes it|makes the ratio|it)\s+" + NUM +
                r"\s+of\s+" + NUM, re.I), ("gating", "total")),
    (re.compile(NUM + r"\s+of\s+" + NUM + r"\s+gat(?:e|ing)", re.I),
     ("gating", "total")),
    # "the ratio (**22 gating**)" and the bare "23 gating" the briefs use
    (re.compile(r"ratio\s*\(\s*" + NUM + r"\s+gating", re.I), ("gating",)),
    # The bare "23 gating" the briefs and this README use. The lookbehind is
    # load-bearing: without it, "22 of 25 gating" yields gating=25 off the
    # TOTAL, which is the 2026-09-14 masking trap — the right string read for
    # the wrong reason. Caught in this tool's own bite 6, where it produced a
    # correct failure with one wrong line of reasoning inside it.
    # The second lookbehind is the one the fixture caught, in the same edit
    # that added the first: without `(?<![A-Za-z0-9])`, NUM can begin in the
    # MIDDLE of a number, so "22 of 25 gating" still yielded gating=5 — the
    # regex simply started one character later to get around the `of ` guard.
    # The self-test failed the pristine tree on its first run after the fix,
    # which is the whole reason it exists.
    (re.compile(r"(?<!of )(?<![A-Za-z0-9])" + NUM + r"\s+gating\b", re.I),
     ("gating",)),
    # "prints the total (**25**)"
    (re.compile(r"prints the total\s*\(\s*" + NUM, re.I), ("total",)),
    # "The other TEN are gated from `postbuild`"
    (re.compile(r"other\s+" + NUM + r"\s+(?:are\s+)?gated from", re.I),
     ("postbuild",)),
    # "names all **ten** `postbuild` gates"
    (re.compile(r"names all\s+" + NUM + r"[^.\n]{0,20}postbuild", re.I),
     ("postbuild",)),
    # "ten postbuild gates in package.json" / "eleven postbuild entries"
    (re.compile(NUM + r"\s+postbuild (?:gates|entries)", re.I),
     ("postbuild",)),
    # "twelve build steps here"
    (re.compile(NUM + r"\s+build steps", re.I), ("build",)),
]

# THE SELF-TEST FIXTURE, and why this tool needs one where its siblings do not.
#
# Every other assertion in this operation can use "I found nothing to check" as
# a failure signal — the 2026-08-16 silent-pass trap, and `qa_census` states it
# outright: a census that cannot find the numbers it exists to compare has
# failed, not passed. This tool's first draft did the same, and it was WRONG,
# for a reason that only appeared once the tool had done its job: **ruling #75
# makes an empty result the desired end state.** The correct fix for a patch
# that keeps going stale about a count is to delete the count, so a queue whose
# staged prose carries zero numeric claims is a queue that has been fixed, not
# an instrument that has broken. Within one run of writing the guard, the guard
# failed the tree for passing.
#
# So the failure signal moves off the population and onto the INSTRUMENT. These
# fixtures are the real sentences this queue has carried, with the extraction
# each must produce. If the pattern list rots, they fail, and they fail whether
# the queue holds six claims or none. Generalised, and it is the part worth
# keeping: *a check whose population can legitimately be empty cannot use
# "found nothing" as its failure signal — it needs a fixture.*
SELF_TEST = [
    ("# TOTAL: 25 standing assertions, 22 of which gate the deploy.",
     {("total", 25), ("gating", 22)}),
    ("      # The other TEN are gated from `postbuild` in web/package.json:",
     {("postbuild", 10)}),
    ("Applying it makes the ratio **23 of 25**.",
     {("gating", 23), ("total", 25)}),
    ("prints the total (**25**) and the ratio (**22 gating**)",
     {("total", 25), ("gating", 22)}),
    ("names all **ten** `postbuild` gates in `web/package.json`",
     {("postbuild", 10)}),
    ("twelve build steps here, ten postbuild gates in package.json",
     {("build", 12), ("postbuild", 10)}),
    # The lookbehind case, fixed after bite 6: 25 here is the TOTAL, and a
    # bare "N gating" pattern without the lookbehind reads it as the ratio.
    ("22 of 25 gating, counted in both homes",
     {("gating", 22), ("total", 25)}),
    ("**26 standing assertions, 23 gating**, counted in both homes.",
     {("total", 26), ("gating", 23)}),
    # A line with no claim in it must produce none. A pattern list that matches
    # prose it should ignore is as broken as one that matches nothing.
    ("The shell is proved both ways against the live origin; see the log.",
     set()),
]

# Human-readable label per truth key, printed with every verdict so a reader of
# the output knows which population was compared.
LABEL = {
    "total": "standing assertions in agents/tools/",
    "gating": "assertions gating the deploy (build steps + postbuild)",
    "postbuild": "gates wired from postbuild in web/package.json",
    "build": "assertions run as build steps in astro-pages.yml",
}


def extract(line):
    """Every (truth-key, number) claim one line makes. The single extraction
    path — the self-test fixture and the queue scan both go through here, so a
    fixture that passes is a statement about the code that actually runs."""
    out = set()
    for rx, keys in PATTERNS:
        for m in rx.finditer(line):
            for i, key in enumerate(keys):
                val = as_number(m.group(i + 1))
                if val is not None:
                    out.add((key, val))
    return out


def run_self_test():
    """The pattern list, proved against sentences this queue has really held."""
    failures = []
    for line, want in SELF_TEST:
        got = extract(line)
        if got != want:
            failures.append((line, want, got))
    return failures


def derive_truth(root):
    """Ground truth, from the three homes. Never from prose."""
    tools = {p.stem for p in (root / "agents/tools").glob("qa_*.py")}

    wf_path = root / ".github/workflows/astro-pages.yml"
    wf = wf_path.read_text(encoding="utf-8") if wf_path.exists() else ""
    build = set(re.findall(r"agents/tools/(qa_[a-z0-9_]+)\.py", wf))

    pkg = json.loads((root / "web/package.json").read_text(encoding="utf-8"))
    post = pkg.get("scripts", {}).get("postbuild", "")
    postbuild = set(re.findall(r"agents/tools/(qa_[a-z0-9_]+)\.py", post))

    return {
        "tools": tools,
        "build_set": build,
        "postbuild_set": postbuild,
        "total": len(tools),
        "gating": len(build | postbuild),
        "postbuild": len(postbuild),
        "build": len(build),
    }


def claim_lines(path):
    """The lines of a queue file that are CLAIMS, with the reason they count.

    For a .patch: added lines and the Subject: header. Context lines are the
    tree quoted back at itself, not an assertion the patch makes.
    For anything else: every line.
    """
    out = []
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix == ".patch":
        in_subject = False
        for line in text.splitlines():
            if line.startswith("Subject:"):
                in_subject = True
                out.append(line)
                continue
            if in_subject:
                # RFC822 continuation — the subject wraps across lines.
                if line.startswith(" ") and line.strip():
                    out.append(line)
                    continue
                in_subject = False
            if line.startswith("+") and not line.startswith("+++"):
                out.append(line[1:])
    else:
        out = text.splitlines()
    return out


def enumerated_postbuild(lines):
    """The postbuild gates a queue file lists BY NAME, if it lists any.

    Scoped to the lines after the phrase that introduces the list, so a tool
    name mentioned anywhere else in the file is not mistaken for a member of
    it. (2026-09-14: an assertion scoped wider than the thing it checks finds
    the right string for the wrong reason.)
    """
    blob = "\n".join(lines)
    m = re.search(r"(?:other\s+\S+\s+are\s+gated from|names all\s+\S+"
                  r"[^.\n]{0,20}postbuild[^:\n]*)[^\n]*\n((?:[^\n]*\n){1,8})",
                  blob, re.I)
    if not m:
        return None
    names = []
    for line in m.group(1).splitlines():
        stripped = line.lstrip("#+ \t")
        # A list line is tool names and nothing else. A prose line that happens
        # to contain a tool name is not a member of the enumeration.
        if not stripped or not TOOL_RE.match(stripped):
            if names:
                break
            continue
        found = TOOL_RE.findall(stripped)
        if re.fullmatch(r"(?:qa_[a-z0-9_]+[\s,]*)+", stripped.strip()):
            names.extend(found)
        elif names:
            break
    return names or None


def main(argv):
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".").resolve()
    qdir = root / "agents/patches"

    if not qdir.is_dir():
        print("qa_patch_queue: no agents/patches/ directory — nothing staged "
              "for a human hand. Clean by absence.")
        return 0

    truth = derive_truth(root)

    # The tokenizer scar, asserted rather than trusted. qa_a11y_lang is the
    # only tool whose name carries digits, and it is a real build step.
    if "qa_a11y_lang" not in truth["build_set"]:
        print("FAIL qa_patch_queue — the derived build-step set does not "
              "contain qa_a11y_lang. That tool IS wired as a build step, so "
              "this tokenizer cannot see something it counts, and every number "
              "below would be wrong in the same direction. (2026-09-28: the "
              "character class qa_[a-z_]+ silently drops it.)")
        return 1

    # The instrument is proved before the tree is judged. This replaces the
    # "found nothing = failed" guard every sibling assertion uses, because
    # ruling #75 makes an empty queue the goal: a staged patch that carries no
    # count cannot go stale, so zero claims is a fixed queue, not a broken
    # tool. The fixture separates the two states; nothing else can.
    st = run_self_test()
    if st:
        print("FAIL qa_patch_queue — the pattern list no longer reads claims "
              "it is known to have read. %d fixture(s) failed:" % len(st))
        for line, want, got in st:
            print("    line   : %s" % line.strip())
            print("    expect : %s" % (sorted(want) or "no claim"))
            print("    got    : %s" % (sorted(got) or "no claim"))
        print("  A queue that reads as clean through a broken pattern list is "
              "the 2026-08-16 silent pass. Fix the patterns, not the queue.")
        return 1
    print("qa_patch_queue — pattern list proved on %d fixture(s) drawn from "
          "sentences this queue has really carried." % len(SELF_TEST))
    print("qa_patch_queue — ground truth derived from three homes, none of "
          "them prose:")
    print("  agents/tools/*.py                         %2d standing assertions"
          % truth["total"])
    print("  astro-pages.yml build steps               %2d" % truth["build"])
    print("  web/package.json postbuild                %2d" % truth["postbuild"])
    print("  union (gating the deploy)                 %2d  -> %d of %d"
          % (truth["gating"], truth["gating"], truth["total"]))
    ungated = sorted(truth["tools"] - (truth["build_set"] |
                                       truth["postbuild_set"]))
    print("  not gating, by name                       %s" % ", ".join(ungated))
    print()

    files = sorted(p for p in qdir.iterdir()
                   if p.is_file() and p.suffix in (".patch", ".md"))
    if not files:
        print("qa_patch_queue: agents/patches/ holds no .patch or .md files. "
              "Clean by absence.")
        return 0

    defects = []
    total_claims = 0

    for path in files:
        lines = claim_lines(path)
        claims = []
        exempt = []

        for line in lines:
            # A struck-through line is the queue quoting a number it has
            # already superseded. Exempt, and printed — never silent.
            if "~~" in line:
                if any(rx.search(line) for rx, _ in PATTERNS):
                    exempt.append(line.strip())
                continue
            for key, val in sorted(extract(line)):
                frag = ""
                for rx, keys in PATTERNS:
                    m = rx.search(line)
                    if m and key in keys:
                        frag = m.group(0).strip()
                        break
                claims.append((key, val, frag, line.strip()))

        # Deduplicate: the same sentence can match two patterns.
        seen = set()
        unique = []
        for key, val, frag, line in claims:
            sig = (key, val, line)
            if sig in seen:
                continue
            seen.add(sig)
            unique.append((key, val, frag, line))

        names = enumerated_postbuild(lines)

        applies = None
        if path.suffix == ".patch":
            rc = subprocess.run(["git", "apply", "--check", str(path)],
                                cwd=str(root), capture_output=True)
            applies = (rc.returncode == 0)

        print("%s — %d numeric claim(s)%s"
              % (path.name, len(unique),
                 "" if applies is None else
                 ("; applies: YES" if applies else "; applies: NO")))

        for line in exempt:
            short = line if len(line) <= 96 else line[:93] + "..."
            print("    EXEMPT (struck through, superseded on purpose): %s"
                  % short)

        if applies is False:
            defects.append("%s no longer applies to the tree (`git apply "
                           "--check` non-zero). A patch that has rotted is "
                           "still unapplied work; refresh or withdraw it."
                           % path.name)

        for key, val, frag, _line in unique:
            total_claims += 1
            want = truth[key]
            ok = (val == want)
            print("    %-9s claims %-3d tree has %-3d  %s   [%s]"
                  % (key, val, want, "ok" if ok else "MISMATCH", frag))
            if not ok:
                defects.append(
                    "%s claims %d %s; the tree contains %d."
                    % (path.name, val, LABEL[key], want))

        if names is not None:
            want = truth["postbuild_set"]
            got = set(names)
            print("    postbuild enumerated by name: %d listed" % len(names))
            missing = sorted(want - got)
            extra = sorted(got - want)
            if missing:
                print("      MISSING: %s" % ", ".join(missing))
                defects.append(
                    "%s enumerates the postbuild gates by name and omits %s. "
                    "A list of the right length naming the wrong set is a "
                    "defect no count can see."
                    % (path.name, ", ".join(missing)))
            if extra:
                print("      NOT WIRED: %s" % ", ".join(extra))
                defects.append(
                    "%s enumerates %s as a postbuild gate; it is not wired "
                    "there." % (path.name, ", ".join(extra)))
            if not missing and not extra:
                print("      set matches web/package.json exactly")

        print()

    if defects:
        print("qa_patch_queue: %d defect(s) across %d claim(s) in %d file(s)"
              % (len(defects), total_claims, len(files)))
        for d in defects:
            print("  DEFECT: %s" % d)
        print()
        print("A staged patch is frozen prose about a moving count. These "
              "numbers land in .github/workflows/** at the moment a trusting "
              "hand applies the patch, in the one file this identity may not "
              "then correct. Refresh the patch or withdraw it; do not leave it "
              "to rot.")
        return 1

    print("CLEAN qa_patch_queue — %d claim(s) across %d staged file(s), every "
          "one agreeing with the tree it describes; %d of %d gating, counted "
          "in both homes."
          % (total_claims, len(files), truth["gating"], truth["total"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
