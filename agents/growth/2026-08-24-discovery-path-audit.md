# Growth — discovery-path audit: the site has no inbound link, and therefore no index

**Filed:** 2026-08-24 · Growth → Manager → founder (one decision escalates)
**Trigger:** yesterday's commitment — *"structured data is the first change that can actually be read back… I am not going to report it as a win until something indexes. What I will do is check."*

---

## 1. The check, and the answer

Two searches, run today:

| Query | Result |
|---|---|
| `site:education3881.github.io madar` | **Zero results from the domain.** Ten results returned, all other projects named MADAR. |
| `"Madār" education publication Arabic English "The Still" editorial` — five distinctive strings from our own copy | **Zero results from the domain.** |

**Not one of 82 URLs appears in a search index.** Not the home page, not an article, not VALENCE.

This is the honest answer to yesterday's question, and it is worse than "the structured data has not
indexed yet." **The structured data cannot index, because the pages have never been crawled.** The
same is true of the raster share cards (08-18), the reciprocal hreflang (07-11), the citation
bibliography (08-23), and the `lastmod` shipped today. Every one of those is correct. Every one of
them is currently invisible.

I want to be exact about what this does and does not prove. A public search API is not a crawler's
index and absence from it is not proof of absence from Google's. But five distinctive phrases from
our own prose returning nothing, on a domain with no results at all, is as strong a negative as this
instrument can give — and the mechanism below explains it without needing anything else.

## 2. The mechanism, and why every technical fix so far could not have helped

Crawlers reach a page one of three ways: a link from a page they already crawl, a sitemap submitted
through a verified property, or a direct submission API.

- **Inbound links: zero.** Nothing on the public web points at `education3881.github.io/madar`. The
  publication has never been distributed — Substack is not live, the Instagram grid is drafted and
  unposted, the engagement list has been built twice and engaged zero times. VALENCE was orphaned
  *inside* the site until 08-18. There is no edge into this graph.
- **Search Console: not set up.** It is blocked behind the custom-domain decision, on the correct
  reasoning that verifying a property and then moving the domain means doing it twice and
  discarding the history. Filed 12 June, open 73 days.
- **Direct submission: not attempted**, and not attempted autonomously by design — submission APIs
  are a network write, and our standing rule routes all fetching through the two sanctioned tools.

`robots.txt` is correct (`Allow: /`, absolute sitemap reference). The sitemap is well-formed and, as
of today, carries a truthful `lastmod` on all 82 URLs. **These are all instructions to a visitor who
has not arrived.**

**The uncomfortable conclusion, stated plainly:** for eleven weeks Growth has been improving a
discoverability surface while the discovery *path* was missing, and no audit we ran would have
caught it, because every one of them inspected the page rather than the route to it. It is the same
shape as the last three quality findings — the artefact was correct and the consumer never received
it — which is now a strong enough pattern that I am treating "who is the consumer, and how do they
arrive" as the standing first question of a Growth audit rather than the last.

## 3. What I fixed today, without the founder

**The repository README now links to the live site.** This is small and it is not nothing.

`github.com/education3881/madar` is a public repository page. GitHub is crawled continuously and
deeply; a repository's README is indexed. It is therefore **the one page connected to this project
that search engines certainly visit — and it did not contain the URL of the site it builds.** Not a
broken link: no link, in either the README or, as far as we can set it, anywhere else in the repo's
public surface.

Adding it creates the first inbound edge into the site's graph from a page that is already in the
index. That is the entire mechanism by which a new site gets discovered without a verified property,
and it cost one commit.

The README was also three months stale in ways that make the repo page a poor front door: it called
the project "Educational Website (working title)" when the brand has been **Madār** since 26 May, it
described a five-agent team that has been eleven since 08-16, and its folder table predated
`/agents/guidebook`, `/agents/briefs`, `/agents/stats` and `/agents/tools`. All corrected. The
sentence the founder wrote about what this project is — personal, unaffiliated, a geo-political
manifesto — is preserved verbatim.

**What I did not do, and why.** IndexNow (Bing, Yandex) accepts URL submission against a key file
without property verification, and would be the fastest legitimate route to a first crawl. It
requires an HTTP POST. Under the standing rule that all network access goes through the two
sanctioned tools, Growth does not make that call autonomously. **It is prepared, not performed** —
the key file and the exact submission are specified in §5 and take the founder about a minute, or
they can be handed to the Web Developer once a decision exists.

## 4. The reprioritisation this forces

I have been leading with on-page work because it is the work Growth can do alone. That was correct
while it was cheap and it has stopped being correct. **The ranked list, revised:**

1. **Any inbound link from a page already in the index.** The README is the first. It is worth more
   today than any further on-page improvement.
2. **The custom domain decision** — no longer a hygiene item. Every day binds more URLs to the Pages
   path, and as of today those 82 URLs carry canonical tags, hreflang pairs, 76 structured-data
   identifiers and 82 `lastmod` values that would all need reissuing. Migrating *before* a crawl is
   nearly free; migrating after means asking an index to forget and relearn.
3. **Search Console, immediately after the domain lands** — it is the only instrument that tells us
   what a crawler actually did, and until it exists Growth is guessing in both directions.
4. **Substack, or any distribution at all.** One issue sent to one list is an inbound link, a
   referral path and a return-rate measurement in a single action.
5. On-page discoverability — **now demoted, because it is finished and it is waiting.**

## 5. For the founder — one decision, one optional minute

**The decision (unchanged, now urgent for a reason it did not previously have):** custom domain,
yes or no. If yes, doing it before a crawler arrives costs nothing; doing it after costs the index.

**The optional minute, only if the domain answer is "not yet" and you want a crawl regardless:**
submit the sitemap to Bing/Yandex via IndexNow — a text file at
`web/public/<key>.txt` containing the key, then one POST of
`https://education3881.github.io/madar/sitemap-index.xml`. Say the word and the Web Developer
prepares the file in the next run; the POST is yours or his, not mine.

---

**Measurement note.** Return rate remains the metric and it remains unmeasurable: no third-party
tracker by design, no Substack, and now confirmed no index. Today's number is **zero indexed URLs
out of 82**, which is at least a real baseline and the first growth figure this operation has been
able to state honestly rather than defer.

— Growth · 2026-08-24
