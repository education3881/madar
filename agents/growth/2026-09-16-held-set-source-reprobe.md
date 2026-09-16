# Growth — held-set source re-probe from a second client, 2026-09-16

**Re-runs:** `agents/growth/2026-09-10-source-promise-decay-sweep.md` (28 distinct URLs across the held set — 20 `ok`, 3 `walled`, 4 `unreachable` on one host, **1 hard 404**).
**Why today, and why from here:** the Edition 05 ledger carries two probe obligations that are explicitly *client-and-day* dependent, not code dependent — **"four `parliament.gov.zm` URLs unreachable on 09-10 — re-probe on a different day, different client (#20)"** and **"the Save the Children blog now returns HTTP 404 — supersede or carry as fetched-on-date (#41)"**. Six days have passed and this run is a different client on a different network from the one that probed on 09-10. That makes this the cheapest thing this run could do that no other run could do as well, and it closes the more consequential of the two.

**Result in one line: the hard 404 is not a death — the publisher re-slugged the post, and a stronger register exists beside it. The unreachable host is still unreachable, and now at a lower layer than "unreachable" implies.**

---

## 1. The egress was proved before anything was concluded from it

An unreachable third-party host and a blocked egress produce the same silence. Before reading a single failure as a fact about the world, four control fetches from this client:

| Probe | Result |
|---|---|
| `https://example.com` | **200** in 0.35s |
| `https://www.savethechildren.org.uk` (root) | **200** in 0.51s |
| `https://www.unicef.org` | **403** in 0.38s — a bot wall, i.e. a *server* answering |
| `https://www.parliament.gov.zm` | **000** — connection refused, after 20s |

Three hosts answered, one of them by refusing us politely. The egress is open. Whatever `parliament.gov.zm` is doing, it is not this client's doing. **This paragraph exists because ruling #52 is six days old and its whole content is *say which instrument read what*** — a sweep that reports "unreachable" without proving its own network is reporting on itself.

## 2. `parliament.gov.zm` — unreachable, and the failure has a shape worth recording

All four URLs re-probed individually with a browser user-agent, 45s budget, redirects followed:

| URL | 09-10 | 09-16 |
|---|---|---|
| `/node/12505` | unreachable | **connection refused :443**, 30s |
| `/node/12930` | unreachable | **connection refused :443**, 30s |
| `/sites/default/files/documents/bills/N. A. B. 6 of 2026.pdf` | unreachable | **connection refused :443**, 30s |
| `/sites/default/files/images/publication_docs/Ministerial Statement - Update on Recruitment of 30,000 Teachers.pdf` | unreachable | **connection refused :443**, 30s |

**The distinction that matters, and that "unreachable" flattens:** this is *connection refused*, not a timeout and not a 404. A refusal means the path to the host exists and the port is closed to us — a host-level outage, a firewall, or a geography/ASN block. It is emphatically **not** the signature of a deleted page, and it carries no information about whether the documents still exist. **Six days, two clients, two networks, identical refusal** makes this a sustained condition rather than a blip, which is exactly what #20 sends a second probe to establish.

**Disposition for the confirmation read:** the four Zambia sources are carried **as fetched on their original dates**, with the host's state named. They are not superseded — nothing has replaced them and nothing suggests the documents are gone. A national parliament's own bill text and ministerial statement have no better register anywhere, which is why they were chosen.

**One thing this run did not do and is naming rather than quietly skipping:** it did not attempt the same fetch from a third route (a different country's egress, or an archive). Both are available and neither was run today, because a third *failure* would add little and a third *success* would immediately raise a question this operation cannot answer from a sandbox — whether the block is geographic. That question belongs in the confirmation read, with the answer stated either way.

## 3. The hard 404 is closed — and it was never a death

`https://www.savethechildren.org.uk/blogs/2026/the-results-are-out-sierra-leone-education-innovation-challenge` — cited by the held Sierra Leone pair, **404 on 09-10, 404 again today** (87 KB of branded error page, which is a real 404 and not a soft one).

The publisher's root serves 200. So the post was searched for rather than mourned, and it is **alive at a different slug**:

**`https://www.savethechildren.org.uk/blogs/2026/results-are-out-summary-save-childrens-evaluation-results-sierra-leone-education-innovation` — 200, 116 KB, fetched 2026-09-16.**

Same publisher, same year-segment, same post: *"The results are out! A summary of Save the Children's evaluation results for the Sierra Leone Education Innovation Challenge (SLEIC)."* The old slug opened with `the-results-are-out-…`; the new one drops the leading article and carries the full headline. **A re-slug with no redirect left behind.** The publisher broke its own link; the document never moved.

**And the hunt returned something better than what it went for.** Three further live registers on the same programme, none of them in the held pair's source list:

- `resourcecentre.savethechildren.net/document/sierra-leone-education-innovation-challenge-final-learning-report-2026` — **200, 136 KB.** A **final learning report**, i.e. a *document*, which outranks a blog post outright on #43's hierarchy (document > tables > first-party written > reported speech > mirror).
- `savethechildren.org.uk/blogs/2026/learning-sierra-leone-education-innovation-challenge` — *"What SLEIC Has Taught Us About Outcomes Contracts in Education."*
- `savethechildren.org.uk/blogs/2026/what-have-we-learned-lessons-implementation-sierra-leone-education-innovation-challenge-sleic`.

**Routed to the Verifier, for the Sierra Leone confirmation read:** replace the dead slug with the live one, and consider whether the **Final Learning Report 2026** should ride *instead of* the blog for anything the blog was carrying — a provider's own summary of its own evaluation is reported speech about a document we can now read directly. That is a citation upgrade, not a correction, and it is the Verifier's call, not Growth's. **No source line was edited by this run.**

## 4. Held-set state after today

| 09-10 | 09-16 |
|---|---|
| 20 `ok` | unchanged |
| 3 `walled` (bot walls, not deaths) | unchanged in kind — `unicef.org` re-confirmed as a 403 wall, i.e. a server answering |
| 4 `unreachable`, one host | **4 still unreachable, now characterised: connection refused at :443, two clients, six days apart** |
| **1 hard 404** | **CLOSED — re-slugged, live URL on file, three better registers found beside it** |

`qa_sources_alive.py --held-only --sample 0` is still the instrument of record and is re-run immediately before the flip commit, per the ledger. This memo is the *interpretation* layer the tool deliberately does not have: the tool reports status codes, and a status code is a fact about a URL.

## 5. What this is worth to Growth, stated honestly

Nothing here moves a reader. It is filed under Growth because **source promises are the only distribution asset this publication actually owns** — a piece whose citations resolve is the entire reason a serious reader or a search engine would return, and the site carries no third-party tracker by design, so there is no traffic figure to set against this and none is invented. What it buys is concrete: the wave's flip is one blocking item lighter, and the blocking item that remains is now described precisely enough that the confirmation read can dispose of it in a sentence instead of re-running the probe a third time.

**The ruling this earned is filed separately: #54, `a-404-is-not-a-death-certificate`.**

— Growth · 2026-09-16
