# Ruling #139 — a distinction the instrument holds is not a distinction the operation has

**Filed 2026-11-11, by the research function, from the content function's own error earlier the same
run.** Family: **how a check earns trust** (assertion discipline), as its first member about a
distinction the instrument holds *correctly* while the decision it exists to inform is made without it.
Second family: **which register speaks for the owner**, since what it ultimately decides is whether a
register is readable at all.

## What happened, in order, inside one run

**09:00-ish.** The content function went looking for the next commission. The obvious candidate on shape
was KHDA Dubai — per-school inspection ratings published since 2008-09, a dated framework change, the
same four-grade archive as the Bahrain single, in the Gulf, with an Arabic face.

**It would not fetch.** `WebFetch` returned `unable to verify the first certificate`; `curl` returned exit
60; `openssl s_client` showed a chain of depth 0 — the server sends its leaf certificate and nothing
else. `https://www.khda.gov.ae/en/` 302s to that same host, so there was no verifying route in.

**The run parked the candidate**, wrote the measurement into the recon brief, and reasoned as follows:
this publication stands on *named primary sources read in served text*, and a register we cannot fetch
cannot be read in served text, so the candidate fails on access. It even wrote down the sophisticated
half — *a browser renders it fine, because browsers chase the issuer named in the leaf's AIA extension* —
and parked it anyway.

**Two hours later**, while looking for something else entirely, the research function opened
`agents/tools/qa_sources_alive.py` and found this, written on **2026-10-01** under **ruling #80**:

> *The certificate is FINE and the host simply does not send the issuing intermediate, publishing it
> instead at the CA Issuers address printed inside the leaf. Clients that follow that address — Chrome,
> Edge, Safari — complete the chain and show the reader nothing at all. Python, curl and openssl(1) do
> not, so this sweep fails where a reader succeeds.*

The tool carries a dedicated `tls-chain` bucket for exactly this, separated from `tls` by exactly the two
substrings this morning's failure printed. It was built against a live instance — the four
`parliament.gov.zm` URLs in the held Zambia pair, which this same bucket had reported *for three weeks*
as unreachable, then refused, then "invalid certificate", before anybody checked.

**Tested against KHDA, the same way #80 tested Zambia:**

```
leaf AIA → CA Issuers - URI: http://secure.globalsign.com/cacert/gsrsaovsslca2018.crt
openssl verify -untrusted inter.pem leaf.pem   →   leaf.pem: OK
leaf valid 2 June 2026 → 18 December 2026, GlobalSign RSA OV SSL CA 2018
```

**The certificate is valid. The register is served. Every reader we have can read it. The park was
wrong**, and it was wrong in the one way the operation had already written down, thirty-one days
earlier, in a file this run had open.

## The ruling

**#80 taught an instrument to tell `tls-chain` from `tls`. It did not teach the operation anything.**
The distinction lives in one Python file, fires only when that file sweeps a URL that is already cited,
and is invisible to the path where it actually decides something — **recon**, where a candidate is parked
or proceeded before any URL is ever cited. The knowledge was in the repository and was not in the
method, so the decision it was built for was made without it by the only function that needed it.

So, binding:

1. **A fetch failure is not an access verdict until its LAYER is named.** Recon may not park a candidate
   on "it would not fetch." It records which layer failed, in the vocabulary `qa_sources_alive.classify`
   already uses — `tls-chain`, `tls`, `dns`, `refused`, `timeout`, an HTTP status — because those buckets
   are opposite facts about the reader and the editorial decision turns on which one it is.
2. **`tls-chain` is NOT an access failure.** It is a misconfiguration on the owner's side that every
   mainstream browser repairs silently. A register in that state is read, cited and quoted normally; what
   changes is that our own instruments will keep declining it, so the piece's hand-off says so.
3. **The test is one command and it is written here so nobody re-derives it:** pull the CA Issuers URI
   out of the leaf's `authorityInfoAccess`, fetch it, and `openssl verify -untrusted <that> <leaf>`. If
   it returns OK, the reader is fine and we are not.
4. **When an instrument learns a distinction, the run that teaches it names the DECISION PATHS that
   consume it** — in the ruling, by name. #80 named its own bucket and stopped there. This clause is the
   part that generalises, and it is the opposite of the queue's propagation finding yesterday (item 93,
   where the premise *no instrument distinguishes this* turned out to be wrong because exactly one
   already did): **both are the same defect seen from the two ends — a capability that exists in one
   instrument and nowhere else is, operationally, a capability the operation does not have.**

## What this does NOT say

It does not say to trust a register our client cannot verify. The three conditions stay distinct and only
one of them is benign: a **bad** certificate (expired, wrong host, self-signed) shows every reader a
full-page interstitial and is a real access failure; an **AIA-only chain** shows the reader nothing; a
404 or a 403 is neither. #80 drew that line correctly. This ruling is about the line not being where the
decision was made.

And it does not retroactively license the KHDA commission. The candidate is **un-parked on access
grounds and still not commissioned**: the Ofsted candidate was chosen on the strength of its register —
a regulator that froze a cohort by rule, lifted the freeze, re-graded it, and printed the yield beside the
stock — and that remains the better frame. KHDA returns to the candidate pool with its access objection
withdrawn and its measurement on file.

## The cost, stated plainly

Nothing shipped wrong and nothing was published. What it cost is a **candidate**, for about two hours,
and the cost is worth recording because it is the cheap version: the expensive version of this defect is
a register cited as dead in an annotation, or a figure dropped from a piece, on the strength of a failure
that was ours. `qa_claim_registers` already scores 12 registers as refusing us and
`qa_citation_identity` declines 128 of 134 Arabic tokens; **neither population has ever been separated by
layer.** That is the measurement this ruling owes and does not take today — **standing-queue item 100**.

*Related: #80 (the bucket), #100 (a dead citation re-opened is an audit), #111 (re-verifiability is a
property of the world), #112 (a citation that dies softly at 200), #137 (the register we falsify
ourselves), #138 (an instrument's unit is a claim). And the Researcher's own standing instruction, which
this run executed to the letter and still got wrong: a candidate's park-or-proceed call is made on
evidence, early.*
