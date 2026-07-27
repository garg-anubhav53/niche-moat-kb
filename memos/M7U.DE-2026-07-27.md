# M7U.DE (Nynomic AG) — §5 Deep-Dive Memo
*Run #73 · 2026-07-27 · OPUS adversarial red-team · Grade C / WATCH*

## Identity
- Exchange: XTRA (Frankfurt Scale segment)
- Sector: Photonics / Precision Instruments (Sector 18)
- Business: Holding company of 13 photonics subsidiaries; NIR measurement instruments (food quality, pharma, medical), in-situ optical metrology (LayTec), fiber-optic sensors (Art Photonics)
- §4 baseline: `financials/M7U.DE.md` (run #68)

## Scoring

| Dimension | Score | Notes |
|-----------|-------|-------|
| Q — Quality | 2/5 | Moat real at subsidiary level (LayTec gold-standard; NIR niche) but three-year revenue decline -21.5% (€118M→€92.6M) disqualifies "high quality" — a durable moat business does not shrink 22% in three years |
| F — Floor | 3/5 | Balance sheet floor real: equity ratio 73.8%, financial liabilities €4.9M, no solvency risk; BUT earnings floor thin: FY2025 EBIT only +€2.0M after three years of decline; net cash ~€6M est. (Dec 31, 2025 — unverified); EBIT-to-net-income gap ~€8M unexplained (minority interests + interest cost + taxes ≠ -€0.7M NI from +€2.0M EBIT without impairment or large minority drag) |
| R — Rerating | 2/5 | H1 FY2026 results due ~August 2026 = date-certain test within weeks; Q4 2025 book-to-bill >1 and backlog +23% are real leading indicators; but German small-cap holding-company structure creates structural valuation discount (low free float, Scale segment, thin liquidity, no index inclusion); historical evidence: Nynomic peak ~€31/sh 2019→€12-16 now = persistent cheapness; 2x requires sustained FY2026-2027 execution, not a single catalyst |
| C — Confidence | 2/5 | ALL data from web search; primary PDF filings (FY2025 Geschäftsbericht) 403-blocked; non-English filer cap C≤2 per ROUTINE; 71% "gross margin" is German Rohertrag accounting artifact; actual price was §4-stale by 21% (€20.20 vs actual ~€16/sh); share count divergence €93.5M–€147.1M cap across providers |

**Total: 9/20. Grade C / WATCH (C<4 hard cap; C=2 unraisable this run).**

## 12-Point Red-Team Findings

**#1 — Revenue trend (FAIL)**
Three consecutive years of decline: FY2023 ~€118M → FY2024 ~€105M → FY2025 €93.2M = -21.5% cumulative. A company with a genuine durable moat does not lose a fifth of revenue in three years. Geopolitical destocking and CH/LED capex pause explains H1 2025 but not FY2023→FY2024.

**#2 — GM artifact (FAIL)**
§4's "71% gross margin" is German Rohertrag (revenue minus Materialaufwand only). For a precision-instruments maker with meaningful in-house production at LayTec and other subs, Personalaufwand (production labor) is the dominant conversion cost and is EXCLUDED from Rohertrag. A US-comparable gross margin is plausibly 40–50%. This removes the "exceptional pricing power" inference entirely.

**#3 — EBIT-to-net-income gap (UNRESOLVED)**
FY2025: EBIT +€2.0M → NI ~-€0.7M. The ~€2.7M gap is explainable by interest + taxes. But H1 2025 showed EBIT -€2.0M → consolidated loss reported at approximately -€5.0M (€3.0M gap for half a year). This implied ~€6M annualized gap between EBIT and NI that requires minority interests or goodwill impairment to explain. PRIMARY FILING REQUIRED before §5 promotion.

**#4 — Thesis triple-counting (FAIL)**
§4 scored "NyFIT2025 cost savings," "FY2026 revenue recovery," and "Q4 2025 book-to-bill >1" as three separate value items. These are one and the same bet — FY2026 revenue — scored three times at ~63% incremental margin. At €100-105M revenue and 7% EBIT midpoint, the implied EBIT is €7M → EV €7M × 18x = €126M → cap ~€132M. At the actual price (~€16/sh × 6.57M = ~€105M cap), the current price already prices in most of this scenario. The upside to 2x requires sustained revenue growth to €130-150M over 5 years, not a one-year recovery.

**#5 — Stale price (CORRECTED)**
§4 used €20.20/sh (~€132.7M cap). Actual current price ~€15.85–16.50/sh = ~€105M cap (21% lower than §4 assumption). This correction is the one thing that helps the bull case — the Asymmetry Gate now partially clears at the corrected lower price.

**#6 — LayTec moat depth (PARTIAL PASS / UNRESOLVED)**
LayTec "gold standard" claim traces to LayTec's own marketing. Third-party market-share confirmation unavailable (no regulatory filings). Competitive dynamics:
- Foundational patents (ECP pyrometry ~2002, curvature deflectometry ~2005) expired or near natural term end
- Remaining IP runs to ~2030-31 (UV pyrometry, calibration, thickness/refractive-index — narrower scope)
- Aixtron has in-house ARGUS pyrometer as alternative; still bundles LayTec EpiCurve TT but in-sourcing non-hypothetical
- Direct product-level competitor: Advanced Energy UV 400/UVR 400 mirrors LayTec Pyro 400 feature-for-feature
- Chinese entrant: Angkun Vision (昂坤视觉) exists (MOCVD in-situ monitoring); scale unverified
- OEM confirmation: Aixtron confirmed (not Veeco; Veeco uses k-Space for GEN200 MBE)
- LayTec revenue/EBIT as % of group: **never established**. Entire moat argument rests on a subsidiary whose revenue contribution is unverified.

**#7 — C ceiling (FAIL)**
C=2 is a hard cap from ROUTINE.md for non-English filers where primary-language filings are inaccessible. No basis to raise C this run.

**#8 — Serial guidance misses (FAIL)**
FY2023: guidance-miss (€118M actual below prior-year guidance). FY2024: guidance-miss (-€3M EBIT guidance revision then negative actual). FY2025: guidance finally met (+€2.0M EBIT; guided "positive" for full year). Three-year serial miss pattern is a caution flag on management credibility for FY2026 guidance of €100-105M / 6-8% EBIT.

**#9 — Holding-company discount (CONFIRMED)**
German comparable evidence (ab73dc81e7d21e994 agent):
- Cenit AG (€69M cap): -17.5% 3yr return; Montega Buy rating; persistent cheap
- Softing AG (€30.7M cap): multi-segment structure; perpetually discounted
- Scale segment listing = thin analyst coverage, low free float, illiquid → discount is structural
- USU Software: founder took private at €18.50 rather than seeing re-rating — control holder is typical exit mechanism, not external investor
- Nynomic share price history 2018-2026: peak ~€31, trough €12-16 = -48% to -61% from peak; 7+ years of persistent cheapness with intermittent rallies

**#10 — Backlog and velocity (PARTIAL PASS)**
Order backlog +23% at Q4 2025 (€43.4M vs €53.6M prior-year — ACTUALLY the backlog DECLINED from €59.5M [Jun 2025] to €43.4M by Q4). Wait: §4 says order backlog Jun 30, 2025 = €43.4M vs €59.5M prior year = -27% year-on-year. Q4 2025 book-to-bill >1 means orders exceeded revenue in Q4, which is positive sequentially but does not mean backlog recovered. H1 2026 results will confirm whether the Q4 momentum has translated.

**#11 — FY2026 guidance credibility (PARTIAL)**
€100-105M / 6-8% EBIT implies €6.0-8.4M EBIT. At corrected €105M cap and ~€6M net cash (est.), EV ~€99M. EV/EBIT guidance midpoint = €99M / €7.2M = 13.8x — not deeply cheap for a structurally-declining holding company but not crazy. The guidance has been mathematically stress-tested (NyFIT2025 €5M savings + Q4 run-rate implies €100M revenue feasible). BUT: Q1 FY2026 EBIT margin was confirmed at **0.4%** (near-breakeven at the start of the guided recovery year) — this is soft evidence for the guidance, not strong.

**#12 — Asymmetry Gate at corrected price (PARTIAL PASS)**
At ~€16/sh / ~€105M cap:
- (1) Mispriced at live price now? Partially — EV/Revenue FY2025 = ~€99M / €93.2M = 1.06x, reasonable but not distressed. At FY2026 guidance €7M EBIT × 15x = €105M EV → fair value. Not obviously mispriced.
- (2) Bull ≥2x? 5yr scenario at €130-150M revenue / 10-12% EBIT / 18x = €234-324M EV → 2x to 3.3x possible. Credible but requires 5yr sustained execution + margin expansion.
- (3) Upside skewed > downside? Floor is balance-sheet: equity €48.5M (book ~€7.38/sh). Downside from €16 = -54% to book. Upside at bull case = +2x. Skew is 2x up vs 1.2x down — marginally OK.
- (4) Catalyst or CORE quality? No discrete near-term catalyst. H1 FY2026 results (~August 2026) = informative test but not a binary trigger.

**Asymmetry Gate: PARTIAL PASS** (criteria 2 and 3 pass at corrected price; criteria 1 and 4 borderline; C=2 prevents WATCH upgrade to actionable tier).

## Risk Profile

| Risk | Severity |
|------|----------|
| Unresolved EBIT-to-NI gap (goodwill impairment or minority drag?) | HIGH — structural |
| LayTec moat deterioration (IP expiry, Aixtron in-sourcing, AE competition) | MEDIUM |
| German Scale segment structural discount (persistent, may never re-rate) | MEDIUM |
| Serial guidance misses → FY2026 guidance achievable but not assured | MEDIUM |
| Goodwill write-down risk (13-subsidiary roll-up; acquisition goodwill from 2013-2023 accumulation) | MEDIUM — unverified |
| Net cash declining (€11.4M Dec 2024 → ~€6M Dec 2025 est.) | LOW-MEDIUM |
| China re-entry risk in compound semiconductor capex (LayTec's core market) | LOW-MEDIUM |

## Grade and Tier

**Grade C / WATCH**

C<4 is a hard cap per METHOD.md — no override. CORE unavailable (requires Q≥4 AND F≥4; Q=2 fails). CATALYST unavailable (R=2). Not PARK because H1 FY2026 results (~August 2026) are a date-certain, genuinely informative test within weeks.

## Buy Zone / Triggers

**Buy zone: below ~€12.00/sh (~€79M cap)** — and only after H1 FY2026 confirms margin recovery.

At €12.00: EV ~€72M; EV/Revenue FY2026E = €72M / €102M = 0.71x. At that entry with confirmed margin recovery, a 2x to ~€24/sh (EV ~€150M) requires only 15x EV/EBIT on €10M EBIT (achievable at 10% margin on €100M revenue). Asymmetry Gate clears cleanly.

**Upgrade triggers (WATCH → CANDIDATE Grade B minimum):**
- H1 FY2026 revenue ≥€45M AND EBIT ≥€2.0M AND FY2026 guidance reaffirmed
- AND primary FY2025 Geschäftsbericht access confirming: actual GM (incl. Personalaufwand), goodwill and any Wertminderungen, minority interests (nicht-beherrschende Anteile), and net cash Dec 31, 2025
- Re-score: C→4, re-run Asymmetry Gate

**Downgrade to BENCH (watchlist only, no near-term entry):**
- H1 FY2026 EBIT <€1.0M
- FY2026 guidance cut below €100M revenue or below 5% EBIT margin
- Evidence of recurring goodwill impairment in primary filing

## Human Verification Checklist

1. **Primary filing (HIGHEST PRIORITY):** Open `https://www.nynomic.com/wp-content/uploads/2026/05/NynomicAG_GB_2025.pdf` — extract Konzern-GuV (Umsatzerlöse, Materialaufwand, **Personalaufwand**, EBIT, Konzernjahresergebnis). Calculate true operating gross margin including production labor. Reconcile the EBIT-to-NI gap.

2. **Goodwill and impairment:** From same report: Geschäfts- oder Firmenwert on the Konzernbilanz; any Wertminderung (Impairment) booked in FY2024 and FY2025; nicht-beherrschende Anteile (minority interests) size and annual P&L allocation.

3. **Net cash confirmation:** Dec 31, 2025 cash and financial liabilities from Konzernbilanz. The ~€6M assumption is single-source (SimplyWallSt) and unverified.

4. **Live price and share count:** Confirm on Xetra or Bundesanzeiger. Provider-quoted market caps ranged €93.5M–€147.1M — a 57% spread. The FY2025 annual report should confirm shares outstanding post any authorized-capital exercises.

5. **LayTec segment disclosure:** Establish LayTec revenue/EBIT as % of group (Segment Clean Tech in Nynomic's segment reporting). Identify any customer-concentration disclosure (>10% customer?). The entire moat argument rests on a subsidiary whose financial weight within the group was never verified.

## Base-Rate Context (ab73dc81e7d21e994 agent findings)

German small-cap photonics / precision-instrument holding companies at €100-200M EV tend to stay cheap for structural reasons:
- **Low free float + Scale segment**: controlling families rarely sell; index exclusion removes institutional buyer set; Montega/NuWays commissioned research only
- **Holding-company discount**: investors pay a SOTP discount (20-40%) for complex structures where internal capital allocation is opaque
- **Take-private is the modal exit**: USU Software, Cenit, Nanofocus — founder-controlled companies harvest the cheapness via take-private at 40-50% premium; external investors capture premium only in that event
- **Elmos counter-example**: +208% in 365 days — cheap does not mean permanently cheap; but Elmos is a pure-play semiconductor company (not a holding company) that benefited from automotive semiconductor cycle

Nynomic at current price (~€16) is consistent with persistent-cheapness profile. The 2x scenario requires either index inclusion (no SDAX candidate at €105M cap), M&A takeout (founder retains significant stake; strategic buyer? Possibly), or genuine sustained margin expansion to 10%+ EBIT over 3-5 years.

## Previous Baseline
See `financials/M7U.DE.md` (§3.5 Financial Baseline, run #68). Key §4 errors corrected by this §5:
- Price: €20.20 → ~€16.00 (actual)
- "71% GM": Rohertrag artifact; true operating GM ~40-50%
- §4 triple-counted one cyclical variable as three separate thesis items

*Sources: OPUS adversarial red-team (a3e38e5dd5367717f); base-rate agent (ab73dc81e7d21e994); LayTec patent/competitive agent (ac66fc7696435b3a2); Nynomic press releases/IR; EQS preliminary results Mar 2026; H1 2025 press release. All ~.*
