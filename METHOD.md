# METHOD — Scoring, Skeptic's Checklist, Base Rates, Risk-Adjusted Asymmetry

## Purpose — what this system is (and isn't)

**The goal is to surface companies that are quite likely to be very strong candidates — high-quality *leads for a human to vet* — not to fully vet a company end-to-end with AI and output a "buy."** An AI pipeline over web/financial data cannot be trusted as the final word; that is not the intention. So we optimize for two things: **(1) finding the genuinely strong ones** (don't miss a great business over imperfect data — when in doubt on a *quality* name, surface it, don't silently kill it), and **(2) an honest handoff** — every candidate comes with clearly-flagged trust levels and a short list of what a person must independently confirm before capital. Better to present a strong candidate with its open questions than to falsely certify it *or* falsely bury it. The trust-tags, confidence score, and the human-verification checklist exist to make the handoff honest, not to simulate a verdict.

The §5 deep-dive reads and applies this file. The §4 scout score (/12) is only a cheap funnel filter; **this is where conviction is actually formed.**

---

## Philosophy: two independent questions, then risk-adjust

1. **Is this a business worth owning at all?** (Quality + Floor) — a genuinely high-quality, well-protected business is interesting to own **even if we have no confidence in a near-term re-rate**. Quality compounds; the re-rate is optional upside. Do NOT kill a high-quality name for lacking a catalyst.
2. **Will the market reprice it, and how soon?** (Re-rate likelihood) — a near-term catalyst adds urgency and IRR, but its absence does not disqualify a high-quality name; it only changes *how we hold it* (CORE vs CATALYST).

Then fold both into one **Risk-Adjusted Asymmetry grade**, discounted by our **Confidence** in the data. The most interesting companies have the highest asymmetric value *relative to risk* — not the highest raw factor count.

---

## Size Discipline (a gradient, not a cliff)

Smaller cap = more likely to have flown under institutional radar (liquidity floors, mandate minimums, 5% disclosure thresholds). That structural exclusion is a real edge, so **cap is a graded input, not a hard wall.** The vast majority of effort goes to small-cap, but a larger name with *exceptional* asymmetry is still worth owning.

- **$20M–$300M — core exclusion zone.** Full funnel; this is where most analysis lives. Smallest end gets the biggest structural-exclusion bonus (feeds a higher **R** via discovery runway, and supports **C** only if data is adequate).
- **$300M–$1.5B — extended zone.** Allowed, but must clear a **higher bar**: only advance past triage if the asymmetry looks **exceptional** (moat wide, floor real, a genuine catalyst or franchise quality). A larger cap means the discovery/coverage-void edge is weaker, so it must be earned on quality + valuation gap, not on obscurity. An ~$800M name with grade-A asymmetry absolutely qualifies.
- **>$1.5B — generally out.** Institutions can own it; the structural-exclusion edge is gone. Kill unless it is a rare, genuinely under-covered special situation with a specific mispricing — and say why explicitly.
- **<$20M — usually too small/illiquid** to enter/exit safely; allow only with a clear liquidity path.

Reflect size in the write-up: note cap, why it is (or isn't) still off institutional radar, and — for extended-zone names — the one-line justification for why the asymmetry overrides the weaker exclusion edge.

## Financial Baseline — the basics, quote-anchored & arithmetic-checked (MANDATORY before qualify/disqualify)

**Rule #1: never qualify a name, or kill it on a financial gate (cap/floor/valuation/integrity), from a snippet.** Get the reported numbers first. Keep it to the basics — but make them *verifiable*, not just careful.

**Fetch cheap, reason well.**
- **Fetcher (haiku) — retrieval only.** Pull each figure from **the primary filing** (SEC EDGAR 10-K/10-Q/20-F or company IR) *and* one structured cross-check (stockanalysis.com). **Return each number quote-anchored** — the figure with its source line and location, e.g. `Cash: $50.1M — FY25 10-K, Consolidated Balance Sheets`. A bare number with no quote is untrusted. No interpretation.
- **Reasoner (sonnet/opus) — triangulate & judge.** The filing is the source of truth; the aggregator's job is to *disagree* and trigger a dig, not to be averaged in.

**The basics (not an exhaustive audit):** revenue 3–5 yrs + trend · gross margin + direction · operating & net margin · **net cash/debt** · **share count + YoY change** (dilution) · **FCF** · verified market cap → P/E, EV/EBITDA, P/S · **52-wk range + % below high** and **analyst PT/consensus** (these two feed the Asymmetry Gate — is the entry still open?).

**Run the deterministic checker** on the fetched figures — `python3 tools/fin_check.py` (JSON via stdin). It reconciles GM = gross_profit/revenue, EV = mktcap+debt−cash, FCF = OCF−capex, P/S, P/E, margin ranges, dilution, growth plausibility. This catches misreads, wrong units, and transposed digits that "be careful" cannot. **Any FAIL → that figure is ⚠, never ✓.**

**Trust-tag each figure, calibrated (not vibes):**
- **✓ CONFIRMED** — from the filing (quote-anchored) AND passes the checker AND the aggregator agrees within tolerance.
- **~ SINGLE-SOURCE** — one source only, or filing-only with no cross-check.
- **⚠ DISCREPANT** — sources disagree or a checker assertion FAILs (e.g. the SHMD €110M-vs-€67M split); do NOT average — dig until resolved, flag loudly.
- **? UNVERIFIED** — couldn't get it.

**Anchor discipline (internal consistency ≠ truth).** The checker only proves the numbers are consistent *with each other* — a set from one wrong vendor feed reconciles perfectly. The only defense is **filing provenance**: the floor-critical figures (revenue, cash, total debt, shares) must trace to the **primary filing itself** (EDGAR accession/URL + statement line, or a verbatim quote), not an aggregator. Pass a `provenance` map to `fin_check.py` (`"revenue":"filing"|"aggregator"|"none"`); it FAILs if none of the floor-critical figures are filing-anchored. A figure that only reconciles, or is aggregator-only, **cannot be ✓ — cap it at ~ SINGLE-SOURCE.** ✓ = filing-anchored AND checker-pass AND aggregator-agrees.

**Foreign micro-cap ceiling (our new geo terrain — AIM/Japan/Korea/Nordics).** These have no EDGAR and thin, error-prone aggregator coverage — the worst data terrain, and exactly where we're now hunting. Rules: the primary must be the company's **actual annual/interim report** (IR PDF), not an aggregator; if only aggregator data exists, **cap C ≤ 2** and hold floor-critical figures at ~ SINGLE-SOURCE — a lead, not a high-confidence CANDIDATE/CORE. Always state the **reporting currency, units, and GAAP-vs-IFRS/adjusted** basis explicitly (foreign filings mix these constantly).

**Coach the skepticism:** state plainly which numbers are solid and which to doubt, and why. That coaching is part of the deliverable.

**Write `financials/[TICKER].md`** (quote-anchored figures + checker verdict + trust tags + sources + as-of). If the basics can't be obtained, or key figures stay ⚠/?, the name is **NEEDS-DATA** — not CANDIDATE — with **C low**. Every §4 score rests on this baseline, never on snippets.

## The four sub-assessments (each 1–5, with evidence)

**Q — Business Quality (worth owning?)**
Returns on capital; margin level & direction; reinvestment runway; revenue durability & recurrence; moat DURABILITY (stays sticky, not just today); management & capital allocation; insider alignment.
`5` = franchise compounder · `3` = solid, defensible · `1` = commodity/melting.

**F — Downside Floor (how protected?)**
Earnings floor (profitable at trough) > asset/book floor > thin. Net cash vs leverage; dilution/going-concern/delisting risk.
`5` = earns through trough + net cash, hard to lose money permanently · `1` = fragile.

**R — Re-Rate Likelihood & Proximity (reprice soon?)**
Specific catalyst with a date/trigger inside ~6–12 months; valuation gap vs. moat-justified fair value; discovery runway (coverage void an initiation/print can close); **historical base rate** (below).
`5` = dated near-term catalyst + wide gap + strong base rate · `1` = no visible path.

**C — Confidence / Data Quality (do we trust our read?)**
Quality & recency of disclosure (audited, English, granular segments); skeptic's-checklist pass rate; did we find the true comparable set / are we watching the right universe; number & severity of unresolved unknowns.
`5` = thesis rests on confirmed, high-quality data · `1` = mostly unverified claims.

---

## The Asymmetry Gate — is the asymmetry actually AVAILABLE today?

*(Learned from culling 33 deep-dived names to 10: almost every reject was a genuinely good business where the asymmetry simply wasn't there at today's price. A moat + a floor is necessary but NOT sufficient — the mispricing has to still be on the table.)*

Using the §3.5 baseline (real price, multiples, 52-wk range, analyst PT), a name is **only "truly interesting" (CANDIDATE or better) if it passes ALL four:**

1. **Entry still open** — NOT within ~15% of the 52-wk high, NOT at/above analyst PT or your fair-value estimate, and hasn't *already* re-rated ~2x off its lows. If the move already happened, the asymmetry is spent.
2. **Magnitude** — a realistic bull case is roughly **≥2x**, not capped at +30–60%.
3. **Skew** — plausible upside meaningfully **exceeds** downside (not symmetric, not inverted). A 10–15%-up / 30%-down name fails even with a moat.
4. **Trigger** — either a **discrete** catalyst (dated event / mandate / contract / print), OR **CORE-grade standalone quality** (Q≥4 & F≥4) you'd own while waiting. A *diffuse* catalyst does NOT count: "the cycle turns eventually," "governance reform / buyback someday," "an analyst may initiate," or coverage-void alone.

**Fail the gate → PARK ("good business, no asymmetric entry — track the buy-zone"), not CANDIDATE.** This is how we keep the shortlist lean and honest: quality-at-a-fair-price is a watch-for-pullback item, not a live idea. The named anti-patterns to reject on sight: *already re-rated / near 52-wk high · at consensus fair value · upside capped <2x · symmetric-or-inverted payoff · slow multi-year grind with no dated trigger · structural-discount value trap (controlled co / MLM) · 2x only via a heroic multiple.*

---

## The Skeptic's Confirmation Checklist (apply to every moat/contract/milestone)

Never take a claim at face value. For each item, assign **CONFIRMED / PLAUSIBLE / UNVERIFIED / RED-FLAG** with a one-line evidence note:

1. **Revenue recognition** — will the claimed revenue actually be *booked*? Acceptance criteria, milestone conditions, financing contingencies, %-of-completion assumptions.
2. **Revenue durability** — can it be *lost*? Contract cancelability, re-tender/recompete risk, customer distress, backlog quality (firm orders vs. LOIs/ceilings).
3. **Competitive capture** — could it go to a *rival*? Is "sole-source" truly sole, or is a second source being qualified? Design-win lock vs. just a current PO.
4. **Moat stickiness over time** — durable or just *now*? Patent cliff, tech obsolescence, requalification-cycle length, and the **in-source/license-away risk** (the Kromek↔Siemens pattern: is the big customer learning to make it themselves?).
5. **Customer concentration** — single-customer / single-end-market dependency; what happens if the top account leaves.
6. **Pricing power persistence** — can they hold price, or is the margin a temporary shortage rent?
7. **Accounting quality (read the ACTUAL filing, not just an aggregator)** — open the latest 10-K/10-Q/20-F (or annual report) and check: revenue-recognition policy, receivables & inventory growth vs. revenue, capitalized vs. expensed costs, one-time items flattering earnings, cash conversion (does net income become FCF?), related-party dealings, restatements, going-concern/covenant language. The Financial Baseline (§ above) must be *verified against the primary filing* in the deep-dive, not taken from a snippet.
8. **Ownership & dilution** — insider alignment; serial issuance/ATM/converts; lock-up expiries; control/take-under risk.
9. **Input & supply dependency** — single-source input, geopolitical exposure (e.g., China-controlled material), FX.
10. **Management credibility** — track record of delivering prior guidance; capital-allocation history.

Every UNVERIFIED or RED-FLAG lowers **C**. Any RED-FLAG that threatens the thesis core **caps the grade at C or below** regardless of the other scores. Record which items are UNVERIFIED as explicit "open questions to resolve."

---

## Historical Base-Rate / Analog Process (directional confidence)

Moats and catalysts are hypotheses. Test them against history:

- Name **2–4 historical companies** that shared this one's pattern — same moat type, same setup (coverage void / niche monopoly / cert lock-in / consumable razor-blade / capacity-constraint), same catalyst type (initiation, margin inflection, contract award, cycle turn).
- For each analog: did it re-rate? **how fast, how far, and what determined success vs. failure?**
- Consult the sibling **rerating-situations-kb** (`github.com/garg-anubhav53/rerating-situations-kb`) for logged ≥2x precedents where relevant.
- Output a one-line **base rate**: *"Companies like this re-rated X of N times; the swing factor was ___."* This is the directional-confidence input to **R**.
- If no credible analog re-rated, **R is low even with a real moat** — say so explicitly. A great business that historically stays cheap is a CORE hold, not a catalyst trade.

---

## The Output: Risk-Adjusted Asymmetry Grade

Combine into the headline — asymmetric value *relative to* risk, scaled by confidence:

- **Upside** = plausible 2x+ magnitude × R (re-rate likelihood) × Q (quality worth owning)
- **Downside** = (6 − F) severity × probability of permanent capital loss
- **Confidence multiplier** = C ⁄ 5
- **Asymmetry-to-Risk (A/R)** ≈ (Upside ÷ Downside) × Confidence multiplier

Translate to a letter grade (this is what we rank on):

- **A — Exceptional**: Q≥4 AND F≥4 AND C≥4, with either a near-term catalyst (R≥4) OR quality high enough to own while waiting. Protected, confirmed, genuinely asymmetric.
- **B — Strong**: high on three of four sub-scores, one soft spot (e.g. R low but Q+F+C high = own-and-wait compounder; or R high but C medium = verify more).
- **C — Interesting, gated**: real asymmetry but a material gap — usually low C (data holes) or F (thin floor), or entry near 52-wk high. Needs verification or a better price.
- **D — Pass/Park**: asymmetry too thin, risk too high, or confidence too low.

---

## Tiers (how we would hold it) — the decoupling in practice

- **CORE** — Q≥4 & F≥4: own-and-hold quality with a protected floor. **A catalyst is optional upside; own it while you wait.** This is the "high quality even without a re-rate is still interesting" bucket the whole method exists to capture.
- **CATALYST** — R≥4 with a dated near-term re-rate and F≥3: tactical; time the catalyst.
- **WATCH** — would be CORE or CATALYST but **C is low**: high potential, thesis not yet verified. Do the confirmation work (resolve the UNVERIFIED checklist items) before conviction.
- **CANDIDATE** — good business but entry/timing off (e.g., near 52-wk high, or catalyst is a multi-year grind): track the named buy-zone.
- **PARK / KILL** — asymmetry too thin / quality too low / integrity fail.

**Key rule:** a high-quality name with no catalyst is **CORE**, never a NO_CATALYST kill. Only *low-quality* names (Q≤2) are killed for lacking a catalyst — for them, the catalyst was the only reason to look.

---

## What every deep-dive memo must end with

```
GRADE: [A/B/C/D]  ·  TIER: [CORE/CATALYST/WATCH/CANDIDATE/PARK]
Q _/5 · F _/5 · R _/5 · C _/5
Financial baseline: rev [3-5yr] · GM% · op margin · net income · net cash/debt · shares Δ (dilution) · FCF · P/E · EV/EBITDA · P/S  [source + as-of date; financials/[TICKER].md]
Financials verified against primary filing: [YES 10-K/20-F / PARTIAL / NO — why]
Base rate: "companies like this re-rated X of N; swing factor = ___"
Skeptic's checklist: N CONFIRMED, N PLAUSIBLE, N UNVERIFIED, N RED-FLAG
Open questions (what would raise C): ...
Buy-zone / upgrade trigger / downgrade trigger: ...
Asymmetry-to-risk in one sentence: ...
HUMAN VERIFICATION CHECKLIST (before any capital — the 3–5 things a person must independently confirm):
  - every ⚠/? figure and the load-bearing assumption behind the grade
  - the primary-filing checks not yet done (e.g. read the debt/lease footnote, customer-concentration note, subsequent events)
  - the single fact that, if wrong, breaks the thesis
```
**We surface strong candidates for human vetting — not finished verdicts.** A memo without a primary-source-verified baseline is provisional (NEEDS-DATA), and every memo hands off an explicit verification checklist. The system's success = *this looks quite likely to be a very strong candidate; here is exactly what to confirm*, not "buy."
