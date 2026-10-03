# Ruling #85 — a tool exempted for the cost of its ACTION is not exempted for the cost of its INPUT

**Filed:** 2026-10-03, by the QA lane, executing the 2026-10-02 forward question before anything new
was added.
**Artefact:** `agents/tools/qa_sources_alive.py` — standing assertion 26, one of the three that
deliberately do not gate the deploy.
**Family:** assertion discipline (twenty-two of eighty-five).
**Cousins:** #81 (an assertion scoped to the served corpus is blind to the corpus about to be served —
this is its third mechanism in three days), #57 (equal cardinalities are not an agreement), #13's rule
in the RUNBOOK (an assertion kept out of CI carries its reason), #65 (an assertion has two outputs),
#35 and #74 (prove the bite as carefully as the control), #83 (a stale list fails silently, filed
yesterday from the same forward-question practice).

---

## The ruling

> **An assertion exempted from the build because its *action* is expensive or unowned is not thereby
> exempted for its *input*.** A tool that fetches third-party hosts is correctly kept out of CI — a
> UNESCO outage must never turn our build red. But that exemption was earned by the **probing** half.
> The **collection** half — the parser that reads our own frontmatter, costs milliseconds and touches
> no network — inherited an exemption it never earned, and so went un-gated and un-censused for 23
> days. Split the tool at the seam: the half that reads what we own is gated like everything else
> that reads what we own.

> **Corollary — the three kinds of singleton, and only one of them is a defect.** A population figure
> that exactly one instrument computes is a number nobody can catch being wrong. Three cases, and the
> enumeration must say which: a **declared** singleton (the census names why it will not cover it — the
> two element censuses need a second and third Chrome in `postbuild`); a **ground-truth** singleton
> (`qa_patch_queue` derives the gate register from three filesystem homes, and a second instrument
> would only be a second reading of the same directory listing — the derivation *is* the cross-check);
> and an **undeclared** singleton, which is a number with no second instrument and no stated reason.
> Only the third is a defect, and it is where #81's family lives.

---

## What happened, measured

The 10-02 forward question was: *which of our 28 assertions derives a population count that no other
assertion can contradict?* Enumerate the population figures, mark which are computed twice from
genuinely different inputs, name the singletons.

The enumeration split the toolkit exactly in half: **`qa_census` reads 14 of the 28 tools; 14 it does
not.** Inside the uncovered half, one tool reads `web/src/content/**` — `qa_sources_alive` — and its
frontmatter parser read, from its first commit on 2026-09-10 until today:

```python
head = text.split("---", 2)[1] if text.startswith("---") else text
```

**That is yesterday's scratch-script bug, shipped.** `---` is not a delimiter in this corpus; it is a
substring. One source URL contains it —
`.../tijdpad-doorstroomtoets-en-overgang-po-vo-schooljaar-2025---2026-vastgesteld` — so the split cut
the Netherlands pair's frontmatter at **3,182 of 4,646 characters, mid-URL**, in both languages.

| | |
|---|---|
| Source promises the shipped sweep collected | **678** |
| Source promises in the corpus | **684** |
| Lost | **6** — three per language |

The three lost per language: the ministry newsletter that contains the hyphens, the PO-Raad
back-to-2030 page, and the Tweede Kamer motion. **The URL that broke the parser was the first of the
three it stopped checking** — the sweep went blind at the exact source that blinded it, and then to
everything behind it.

**And the cut discarded `approved:` too**, which is the last key in the block. The held flag read
`bool(m and m.group(1) == "false")`, so an unreachable flag meant **not held** — the opposite of
`content.config.ts`, where `approved` is `z.boolean().default(false)`, and the opposite of what
`qa_census` does with the same absence. Proved on a fixture: a **held** piece with three sources, one
URL containing `---`:

| | citations collected | cited by a held piece |
|---|---|---|
| shipped until today | 1 of 3 | **0** |
| fixed | 3 of 3 | 3 |

So a held piece whose frontmatter contained `---` would have had **none** of its sources checked by
`--held-only` — the mode the Edition 05 ledger names as the **last step before the flip commit**, eight
days out, on the six most heavily annotated pieces this publication has ever produced. Latent today
only because no held piece happens to contain the substring. Two independent faults compounding in the
same direction, which is #81's signature: the parser loses the URLs *and* the piece loses the flag that
would have made anyone look for them.

## The finding under the finding, and it indicts the cross-check rather than the parser

**Two instruments were already computing this population and disagreeing by six.**
`qa_pair_frontmatter` prints *684 source URLs*; `qa_sources_alive` printed *678*. Both numbers were
correct readings of their own code and one of them was wrong about the corpus. Nothing compared them —
not because no second instrument existed, but because the second instrument **never ran where the
comparison happens.**

That is `qa_census`'s own founding thesis turned on the census: it was built on 09-19 because *three
instruments printed 120 for three different sets of 120 pages*, and its lesson was that **equal
cardinalities are not an agreement**. Here the cardinalities were *unequal* — a louder signal, freely
available for 23 days — and it went unread because one of the two tools was outside `ROWS`. A census is
scoped to what it enumerates, which is the enumeration family's own rule arriving at the instrument
built to end it.

Yesterday's log wrote: *"every shipped content-reading gate was checked against it… none has the
defect."* **That sentence is true as written and the population it names is the defect.** It says
*gate*. `qa_sources_alive` is not a gate — it is one of the three tools that deliberately do not gate —
so the check that cleared the toolkit ran on a population the bug had already stepped outside of.
**Name the population your instrument actually reads** was 10-02's own closing lesson, filed about a
badly chosen credential probe, and it applied one paragraph further out than the run that wrote it
could see.

## What shipped

1. **The parser reads the frontmatter block** — the opening fence to the first fence that *starts a
   line*. A fence is a line; matching it as one costs nothing and is the only reading true of YAML.
2. **An absent `approved:` is HELD**, mirroring the schema rather than guessing, as `qa_census` does.
3. **`--collect-only`** — the collection half, separated at the seam: it parses the corpus, prints the
   population, and touches no network. Proved network-free by running it with `socket.socket.connect`,
   `socket.create_connection` and `socket.getaddrinfo` replaced by raisers: exit 0, same line.
4. **`qa_census` gains a fifteenth instrument**, reading that line. The census derives the citation
   count with its own block parse, so the tool that reports the number and the tool that checks it
   share no code. Counted as **citations, not distinct URLs**, on purpose: a URL cited in both
   languages is two promises to two readers, and the EN/AR symmetry of a correction is exactly what the
   number must be able to show — it is how 10-02's own URL fix was confirmed to have landed on both
   sides.

**Proved both ways (#35), with the injection asserted to have changed the file before the check ran on
it (#74), and the bytes compared rather than a summary of them (#82):**

| | | |
|---|---|---|
| CONTROL | the real 121-page build | **exit 0** — 22 numbers from 15 instruments |
| BITE 1 | the 23-day-old split restored **verbatim** | **exit 1** — *`qa_sources_alive` printed 678 for 'source citations'; the population it means has 684* |
| BITE 2 | a held fixture whose frontmatter contains `---` | old: 1 of 3 citations, **0** held-cited · fixed: 3 of 3, 3 held-cited |

Restored byte-identical by SHA after each bite.

## The enumeration, kept because the next run needs it rather than the argument

Of the population figures the toolkit prints: **22 are now censused** across 15 instruments; **4 are
declared out** with a reason (`qa_arabic_shaping`'s 7 targets and 310 Arabic-bearing elements,
`qa_arabic_joining`'s 4 targets and 12 measured runs); **5 are ground-truth derivations**
(`qa_patch_queue`'s 28 / 12 / 13 / 25 and its 4 staged files). The **undeclared singletons** that
remain, named so they are not rediscovered:

| Tool | Singleton population figures |
|---|---|
| `qa_css_tokens` | 174 files scanned · 69 read without a fallback / 77 defined / 1 runtime-set / 3 with a fallback |
| `qa_chrome_links` | 4,755 pointers · 804 distinct targets |
| `qa_stable_order` | 45 dated lists · 76 related rails · 38 browse pages · 42 date and 6 facet tie groups exercised |
| `qa_pair_frontmatter` | 432 identity fields · 44 rails · 338 shared annotations |
| `qa_packet_figures` | 4 packets · 9 entries · 21 captions · 45 figures (EN 28 / AR 17) |
| `qa_date_identity` | 232 listing dates |
| `qa_sources_alive` | 343 distinct URLs · 59 cited by a held piece |
| `qa_render` | 5 render targets |
| `qa_feed_enclosures` | 2 feeds · 76 items · 76 enclosures |

**Two of these are numerically equal to a censused figure and count a different set**, which is #57's
trap sitting in the open: `qa_stable_order`'s *76 related rails* and `qa_body_links`' *76 approved
pages*; `qa_feed_enclosures`' *76 items* and `qa_feed_direction`'s *38 + 38*. And
**`qa_stable_order` prints *121 pages* — the served set, three other instruments' censused
population — while the census does not read it.** None of these is today a defect. They are where to
look first the next time a count is plausible and wrong.

## Deliberately not done

A rule that every printed integer must be censused. The census would then run `qa_css_tokens` to check
that it scanned 174 files, which is a reading of a directory listing checked against a reading of the
same directory listing — ceremony, not a cross-check, and the kind of green that teaches runs to stop
reading. The honest instrument is the **enumeration above, maintained**: a singleton is acceptable with
a reason, and unacceptable silently.
