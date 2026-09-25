# Ruling #65 — run it twice: a correct verdict does not make a reproducible record

**Filed:** 2026-09-25 · **Daily run, QA lane** · **Section 1 row 60**
**Family:** assertion discipline (fourteenth member)
**Origin case:** the 2026-09-24 forward question, tested first, on all twenty-four standing assertions.

---

## The statement

**An assertion has two outputs and only one of them is usually checked.** There is the
**verdict** — the exit code, the pass or fail the build gates on — and there is the **record**,
the lines it prints into a QA log that later runs read as true. The verdict can be a pure
function of the artefact while the record is not, and nothing in a green build will ever tell
you.

**The probe, and it costs one loop:** run each assertion **twice against a byte-identical
artefact** and compare the two outputs, exit code included. Anything that differs is reading
something that is not the artefact — a clock, a network, an enumeration order, a locale, a
replica, a hash seed. An assertion *about* the origin will differ and should say so in its own
header; every other difference is a defect or a confession.

**And the probe's own limit, which must be stated wherever the probe is described, because a
reader will otherwise take a clean run for more than it is:** two runs a second apart cannot see
a **coarse** clock. A tool printing `2026-09-25` prints it identically in both runs and differently
tomorrow. **The probe's resolution is the interval between its two runs**, and everything slower
than that interval is invisible to it. Close that half **statically** — read the sources for what
they consult — or the probe's green is an answer to a smaller question than it appears to answer.

---

## The origin case

The 09-24 log named it: *"we have never checked whether a check is still wired to anything… which
of our checks has an answer that is not a function of the thing it claims to measure?"*

**Result: 21 of 21 locally-run assertions byte-identical across two runs, exit codes included,
against a `dist` whose SHA-256 was confirmed unchanged before and after.** Hash randomisation was
live and varying between runs, so the set-iteration axis was genuinely exercised rather than
assumed; no assertion prints a set in iteration order. The three origin-facing tools were run
separately and are *about* the origin by design.

**The probe was proved before its result was believed** (#35). Control: a scratch tool printing a
constant — SAME. Three bites, all of which bit: a clock (`datetime.now()`), a set printed in
iteration order, and a tool with **identical stdout and a varying exit code** — that last one
because a probe comparing only text would have called it clean. A fourth scratch tool printing
`date.today()` came back **SAME**, which is the limit above, proved rather than asserted.

**What the static half found, in the half the probe cannot see.** `qa_dist_input` rendered its
timestamps through `time.localtime`. The same artefact printed `newest source 2026-09-25 09:38:48`
on the runner and `13:38:48` on a desktop in Asia/Dubai. **Its verdict never depended on it** — the
comparison is `d_m < s_m` on raw mtimes and is timezone-free — but its *record* went into a QA log
that future runs read as true. That is **ruling #60's defect, in an instrument, three days after
#60 closed it in the publication.** Fixed to UTC with an explicit `Z`; proved both ways, including
the FAIL path, which prints through the same function and is now identical across three timezones.

**Two further candidates were traced and both cleared, and they are recorded because "we looked"
is worth more than "it was fine":** `qa_held_assets` builds sets from an unsorted `os.listdir` and
sorts every one before printing; `qa_stable_order` reads its expectations in `os.listdir` order and
sorts facets on `(-count, collation_key, key)` — a **total** order, so no tie ever falls back to
enumeration order. The second matters more than it looks: that is the assertion whose entire
subject is that no list may depend on filesystem enumeration order, and it does not commit its own
offence.

---

## The corollaries

**Corollary 1 — the record is an artefact with readers.** `agents/logs/**` and `agents/briefs/**`
are read by every future run as established fact. A line in a QA log that two machines disagree
about is a figure composed from the environment, and #41 does not stop applying because the reader
is us.

**Corollary 2 — a clean determinism result is not a claim that the check is correct**, only that
it is *about* the artefact. A check can be reproducibly wrong. This probe and #35's both-ways proof
answer different questions and neither substitutes for the other.

**Corollary 3 — an instrument inherits the publication's rulings.** #60 was filed against eight
date formatters in `web/src/`, and nobody swept the twenty-four tools that watch them. **A ruling
closed in the product is not closed in the toolchain until the toolchain is read.**

---

**How to apply it.** Run the probe whenever an assertion is added or edited, and at any weekly
review that touches the gate count. Two runs, byte-compare, exit code included; then read the
sources for coarse clocks, locales, network reads and enumeration order, because that is the half
two runs a second apart will never show you. An assertion that differs and has no reason written
in its own header is unwired from its artefact.

*Related:* [[2026-09-22-a-date-is-not-a-moment]] (#60, the defect this found surviving in an
instrument), [[2026-09-24-a-validator-is-not-the-content]] (#63, a check whose answer was about
the storage), [[2026-09-21-a-comparator-with-no-locale-asks-the-machine]] (#59).
