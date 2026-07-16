# METHOD — Scoring, Skeptic's Checklist, Base Rates, Risk-Adjusted Asymmetry

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

## The Skeptic's Confirmation Checklist (apply to every moat/contract/milestone)

Never take a claim at face value. For each item, assign **CONFIRMED / PLAUSIBLE / UNVERIFIED / RED-FLAG** with a one-line evidence note:

1. **Revenue recognition** — will the claimed revenue actually be *booked*? Acceptance criteria, milestone conditions, financing contingencies, %-of-completion assumptions.
2. **Revenue durability** — can it be *lost*? Contract cancelability, re-tender/recompete risk, customer distress, backlog quality (firm orders vs. LOIs/ceilings).
3. **Competitive capture** — could it go to a *rival*? Is "sole-source" truly sole, or is a second source being qualified? Design-win lock vs. just a current PO.
4. **Moat stickiness over time** — durable or just *now*? Patent cliff, tech obsolescence, requalification-cycle length, and the **in-source/license-away risk** (the Kromek↔Siemens pattern: is the big customer learning to make it themselves?).
5. **Customer concentration** — single-customer / single-end-market dependency; what happens if the top account leaves.
6. **Pricing power persistence** — can they hold price, or is the margin a temporary shortage rent?
7. **Accounting quality** — aggressive rev-rec, capitalized costs, one-time items flattering earnings, related-party dealings.
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
Base rate: "companies like this re-rated X of N; swing factor = ___"
Skeptic's checklist: N CONFIRMED, N PLAUSIBLE, N UNVERIFIED, N RED-FLAG
Open questions (what would raise C): ...
Buy-zone / upgrade trigger / downgrade trigger: ...
Asymmetry-to-risk in one sentence: ...
```
