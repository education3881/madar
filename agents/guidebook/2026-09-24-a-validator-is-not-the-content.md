# Ruling #63 — a validator is not the content, and two requests are two experiments

**Filed:** 2026-09-24 · **Daily run, QA lane** · **Section 1 row 58**
**Family:** assertion discipline (thirteenth member) — with a limb in *which register speaks for the owner*
**Origin case:** the 2026-09-23 deploy went red on a green publication.

---

## The statement

**An identifier minted by the server that stores a file is a property of the storage,
not of the file.** Two replicas holding byte-identical content will mint different
validators if the thing the identifier is derived from — an mtime, an inode, a path, a
build host — differs between them. The identifier is *about* the copy. The content is
about the content.

**And the operational limb, which is what actually bit:** an assertion that makes two
requests has run **two experiments**. If it requires the two to agree about something the
infrastructure is free to vary between them, it is not an assertion, it is a coin flip
with a stated expectation. **Either pin the scope that mints the identifier — one
connection, one host, one build — or compare the content itself.**

---

## The origin case

The `verify` job has long carried a step asserting that a polling reader can revalidate
the feeds cheaply:

```
HEAD /madar/ar/rss.xml            -> read the ETag
GET  /madar/ar/rss.xml  If-None-Match: <that ETag>
assert 304
```

On 2026-09-23 it returned 200 and failed the deploy. The byte-compare in the same job had
already passed on all five files: the origin was serving exactly the artefact we built.
**Nothing was wrong with the publication, and the gate said there was.**

GitHub Pages serves through Fastly over anycast, and the Pages origin unpacks each deploy
onto more than one replica. nginx mints `ETag: "<hex-mtime>-<hex-size>"`. The replicas
unpacked the 09-23 artefact **one second apart**, so every feed URL has two permanent
validators:

```
"6ab3a42c-920e"   and   "6ab3a42d-920e"
 ^^^^^^^^ mtime          ^^^^^^^^ mtime + 1s
          ^^^^ size               ^^^^ identical
```

The step's two requests are independent, so they reach independently chosen edges. When
the conditional GET lands on the other replica, that edge has **never seen the ETag it was
handed**, and a 200 with the full body is the only correct answer it can give.

Measured before anything was changed — twelve probe pairs, 2026-09-24, about 23 hours
after the deploy:

- **every 304**: the response's own ETag **equalled** the one sent
- **every 200**: the response's own ETag **differed** from the one sent, in the mtime limb
  only, never the size limb

The origin never once refused a validator it actually held. And because both mtimes were
still being served a day later, this is not propagation settling — it is a **permanent
two-valued validator**, which makes the old step a coin flip on every deploy, forever. It
passed on 09-21 and 09-22 by luck.

---

## Why the first fix was the wrong one, and what replaced it

The obvious repair is a tolerance: read the ETag off the 200, and call it a defect only
when it **equals** the one sent — because then the edge held the validator and refused it
anyway. That discriminator is correct and is kept. But it leaves the assertion "at least
one probe revalidated", which on six probes against two replicas is a **1-in-64 coin
flip**: a smaller flake, not the absence of one.

**Proving the bite is what exposed it.** The fanout control — two validators, identical
bodies, the real 09-23 condition, the one case the check *must* stay silent on — **failed
on its first run**. Per the 2026-09-14 rule, a control that fails is the cheaper half of
the lesson a failed bite teaches; this one rewrote the check.

The honest instrument was inside the question. **A polling reader does not open a new
connection for every poll; it keeps one.** And a TCP connection terminates at exactly one
edge, holding exactly one replica's validator. So do what the reader does: GET, read the
ETag, and revalidate **on the same connection**. Live origin, three trials, two distinct
validators across them:

```
trial0  "6ab3a42d-920e"  kpao1770082-PAO  -> 304
trial1  "6ab3a42c-920e"  sjc1000110-SJC   -> 304
trial2  "6ab3a42d-920e"  kpao1770071-PAO  -> 304
```

Deterministic — and **strictly stronger** than the step it replaces, which asked for one
304 and now gets all of them. Sixteen of sixteen on the live origin today.

---

## The axis this bought, which is the reason it is a ruling and not a bug report

Dropping the flake would have made the deploy green. Asking *why* it flaked bought a
question nobody had asked: **if an origin can serve two validators for one URL, does it
also serve two BODIES?** That would be far worse than the failure that went red, and the
old step could not have seen it, **because it never fetched a body.** It compared
identifiers and reported on content.

So the replacement fetches the body on every probe and hashes it. **Many validators are
tolerated; many bodies are not.** The check that existed to police a cache header now
polices the thing the cache header stands for.

---

## How to apply it

- **Never establish identity of content by comparing identifiers the infrastructure
  mints.** Compare the content. If you must compare identifiers, compare them *within the
  scope that mints them* — one connection, one host, one build.
- **Count the requests in an assertion.** Two requests are two experiments, and anything
  the infrastructure may vary between them is a variable, not a constant. Name it, pin it,
  or measure across it.
- **A gate that fails on a green publication is worse than no gate**, because it spends
  every later run's first minutes deciding whether a red deploy is real. Repair it at the
  same priority as a defect in the product.
- **When a check flakes, ask what it is actually about before you widen its tolerance.**
  The tolerance would have hidden the body axis entirely.

---

## Family placement

**Assertion discipline**, thirteenth member, and it extends that family's second question
— *what is this check's answer actually about?* — from **#52** (name the artefact it read)
and **#55** (read the resolved value, at the layer the property lives on) to the layer
below both: *the identifier you read is minted by something, and that something has a
scope.*

Nearest siblings, and all three say one thing three ways:

- **#57 equal counts are not an agreement** — two numbers matching is not the sets matching.
- **#60 a date is not a moment** — the same commit built on two machines printed different days.
- **#63** — the same bytes stored on two replicas mint different validators.

#60 is the closest: it is this ruling one layer in. There, our own build derived a
*rendered value* from a machine-local fact and printed a difference that was not a
difference. Here, someone else's storage derives an *identifier* from a machine-local fact
and our check read the difference as a defect. **In both, a value that varies with where
it was computed was mistaken for a value that varies with what it describes.**

The limb in *which register speaks for the owner*: the ETag is the **storage's** statement
about a file, not the **publication's** statement about its content. Reading it as the
latter is #43's hierarchy error committed against a machine.

---

## Action of record

`agents/tools/qa_feed_validators.py` — **standing assertion 24**, proved seven ways:
controls on an honest origin, on a fanout origin (the real 09-23 condition), and on the
live origin; bites on a validator ignored, on two bodies under two validators, on a
missing ETag, and on an origin that never honours a validator at all.

**It does not gate**, because it reads the origin and so cannot run in the build job — the
third assertion in that category, joining `qa_live_drift` and `qa_sources_alive`, reason
stated per the 2026-09-13 rule. **21 of 24 gate the deploy today.** The one-line patch
that returns it to the `verify` job — and the ratio to 22 of 24 — is staged at
`agents/tools/patches/2026-09-24-verify-feed-validators.md` and **cannot be pushed by this
identity**, which is refused write access to `.github/workflows/**`. Re-probed today on a
scratch branch; the refusal is unchanged. Escalated on **issue #7**, where it changes the
stakes: the first staged repair was an improvement that could wait, and this one repairs
**a gate that is currently failing at random.**
