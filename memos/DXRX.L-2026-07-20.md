# DXRX.L — Diaceutics PLC — §5 OPUS Adversarial Deep-Dive
**Run #49 · 2026-07-20 · AIM London**

---

## Summary Block

```
GRADE: C  ·  TIER: PARK
Q 3/5 · F 2/5 · R 2/5 · C 2/5

Financial baseline (as-of 2026-07-20; financials/DXRX.L.md):
  Revenue: £19.5M(FY22) → £23.7M(FY23) → £32.2M(FY24) → £38.4M(FY25, +20%/+24%CC)
  GM: 82% FY2025 (↓ from 88% FY2024 — £2M incremental data cost, expansion into new disease areas)
  Adj EBITDA: £7.6M (20% margin); statutory PBT: £0.3M; net income: £97k
  Net cash: ~£6.15M (£7.3M cash − £1.15M lease liabilities)
  Shares: 84.67M [✓ filing-anchored]
  Dilution: ~ (share-based payments material adj-back; trajectory UNVERIFIED)
  FCF: NEGATIVE (OCF ~£1.18M − ~£4–5M capitalised dev = materially negative)
  P/E: >500x on clean earnings; 15x flattering adj EBITDA
  EV/adj-EBITDA: ~15x (EV £115M at 146p)
  P/S: ~3.2x
  [Source: RNS Final Results 26 May 2026 (revenue, EBITDA, PBT, ARR, cash); aggregators for OCF/capex; 146p price web search Jul 2026]

Financials verified against primary filing: PARTIAL — RNS confirms revenue £38.4M, adj EBITDA £7.6M,
  PBT £0.3M, NI ~£97k, cash £7.3M (from £12.7M), ARR £20.0M, order book £38.9M, NRR 105%.
  Cash-flow detail (capitalised-development line, working-capital breakdown) NOT parsed —
  all primary sources 403-blocked in-environment. C rule-capped at 2.

Base rate: "AIM pharma-data/clinical-analytics platforms re-rated ~1 of 5–6 in 5yr;
  swing factor = proof of real cash conversion, not revenue growth headline"
  (Instem range-bound then taken private cheaply; Ebiquity slow; GlobalData slow;
   Craneware re-rated then de-rated hard; Diaceutics itself IPO'd 2019 at 76p, spent
   2021–2024 range-bound — a known AIM name, not a fresh undiscovered story.)

Skeptic's checklist: 0 CONFIRMED · 4 PLAUSIBLE · 3 UNVERIFIED · 3 RED-FLAG
  (3 RED-FLAGs: revenue recognition lumpy, customer concentration PMx/2-contracts, accounting quality/capitalised-dev)

Open questions (what would raise C to 3–4):
  1. Read FY2025 cash-flow statement — get capitalised development line and WC movement.
     If FCF positive after capdev: C raises materially; if FCF structurally negative: PARK → KILL.
  2. Reconcile £7.6M adj EBITDA → −£5.3M cash bridge line by line.
  3. Confirm analyst count at ≤4 (aggregators 3–5; ≤4 needed to clear coverage gate).
  4. Confirm PMx contract terms — BIZENGRI guaranteed vs. success-contingent split.
  5. Share dilution trajectory from primary filing (SBC add-back is material).

Buy-zone / upgrade trigger / downgrade trigger:
  Buy-zone: ~95–110p (~2.0–2.4x EV/sales; ~£80–93M EV) — at that level, a 2x to analyst
    consensus PTs (205p) becomes mathematically available.
  Upgrade trigger: (a) H1 2026 results (Sept 2026) show positive OCF after capitalised dev,
    OR (b) FY2026 results confirm genuine FCF-positive year — the ONLY test of the load-bearing
    assumption (cash conversion). Revenue growth alone does not qualify.
  Downgrade trigger (PARK → KILL): FCF remains negative in FY2026 despite 20–25% rev growth;
    or capitalised-development line revealed as structurally £4–5M/yr;
    or analyst count confirmed ≥5 (COVERAGE_KILL).

Asymmetry-to-risk in one sentence:
  Do not buy at 146p — an adj-EBITDA margin story that the cash-flow statement contradicts
  (negative FCF, £97k net income, £5.3M cash outflow), trading inside fair value at 3.0x
  EV/sales with no dated catalyst and a moat that fades past 5 years; Asymmetry Gate fails
  all four tests; revisit only at ~95–110p or on proof of genuine positive free cash flow.

HUMAN VERIFICATION CHECKLIST (before any capital):
  1. Read FY2025 audited Annual Report cash-flow statement (26 May 2026 RNS/AR). Get:
     — capitalised development / intangibles-additions (the "real capex")
     — working-capital movement
     Confirm if FCF is positive or negative. This single fact is the THESIS-BREAKER.
  2. Reconcile adj EBITDA (£7.6M) → cash outflow (−£5.3M) line by line:
     SBC quantum, D&A split, exceptional items, lease payments, tax paid, WC movement.
     Understand how much "EBITDA" is real cash.
  3. Verify analyst count precisely — Shore Capital (Jan 2026), Canaccord (Jun 2026),
     RBC (~Jul 2025), Stifel (May 2025 status?). If confirmed ≥5 → COVERAGE_KILL.
  4. Confirm PMx contract terms for BIZENGRI/Partner Therapeutics (£2.6M ARR):
     what portion is guaranteed milestone vs. success-contingent on drug commercial ramp?
     Ultra-rare NRG1+ cancer drug (zenocutuzumab) has limited patient population.
  5. Read the customer-concentration note: FY2025 top client %, any change from FY2024 14.5%.
```

---

## Context

Diaceutics PLC (AIM: DXRX) operates the Precision Medicine Implementation (PMI) platform, connecting pharmaceutical companies to diagnostic laboratory networks for companion diagnostic (CDx) testing programs. The company has agreements with 2,500+ labs globally and 18 of the top 20 pharma companies as customers. FY2025 was the first profitable year (PBT £0.3M after a −£1.9M loss in FY2024). AIM-listed, ~£121M market cap at 146p.

§4 financial baseline completed run #48 (2026-07-20). Analyst count confirmed 3 active firms (Shore Capital, Canaccord Genuity, RBC Capital Markets) → PASSES ≤4 coverage gate. §5 OPUS adversarial red-team completed run #49 (2026-07-20).

---

## A. THE 12 RED-TEAM RESULTS

**1. Re-derive load-bearing numbers — CONCERN (numbers confirmed, baseline file had errors).**
RNS 26 May 2026 primary-sourced: revenue £38.4M (+20%/+24%CC) ✓; GM **82%, prior year 88%** (baseline file said 87% — **error corrected**); adj EBITDA £7.6M ✓; **PBT £0.3M up from −£1.9M FY2024** ✓; net income £97k ✓; cash £7.3M from £12.7M = −£5.3M outflow ✓; ARR £20.0M ✓; order book £38.9M ✓; NRR 105% ✓; price 146p (52-wk 112–180p) ✓. The financials/DXRX.L.md file carried three errors (87% GM, "+16%" growth, FY2024 GM "85%"). Numbers now anchored.

**2. "Too good to be true" DATA ALARM — CONCERN.**
Two alarms: (a) 40–48% gap to analyst PTs (avg 205p) on a name covered 3–5 brokers for years is not free money — either aggressive broker multiples or market pricing cash-conversion risk PTs ignore; (b) "20% adj EBITDA margin" alongside £5.3M cash outflow is the classic tell — the cash statement wins.

**3. Strip to CLEAN operating earnings — FAIL (for the bull case).**
Adj EBITDA £7.6M → PBT £0.3M = **~£7.3M (96% of EBITDA) consumed by D&A, SBC, and exceptionals.** Much of D&A is amortisation of capitalised development — a genuinely recurring cost of a data platform. Clean net income: £97k. After ~£4–5M capitalised development (the real capex, not the aggregator-cited £71k tangible figure), **FCF is materially negative.** "Return to profitability" is technically true and economically hollow.

**4. Score each item once — PASS.** No fact double-counted below.

**5. Absence of catalyst ≠ catalyst — CONCERN.** Bull case leans on "coverage/multiple could expand" and "SaaS mix rising." Neither is dated or mechanistic. The only dated event is H1 2026 results (~Sept 2026) — incremental, not a 2x re-rate trigger.

**6. Base rate includes failures — CONCERN.** AIM pharma-data platforms that stayed cheap or de-rated are the majority. Diaceutics itself IPO'd at 76p (2019) and spent 2021–2024 range-bound — it is a known name, not a fresh discovery. Base rate for re-rate: mediocre.

**7. No hard-rule overrides — ENFORCED.** Non-US/non-English-equivalent AIM filer, no primary PDF parsed (all sources 403-blocked), unreconciled cash bridge → **C capped at 2 by rule.** This caps the grade regardless of other scores. Resolvable ≠ resolved.

**8. Decompose revenue quality — FAIL (for "recurring SaaS" framing).** ARR £20.0M = only **52% of £38.4M revenue**; recurring was 61% at H1 2025; **NRR 105% — weak for SaaS** (good SaaS = 110–120%+). ~£15–18M is project/milestone execution work. H1 2025 revenue was only ~£14.6M vs £38.4M full-year → **~60%+ lands in H2** — lumpy, back-half-weighted, project-driven profile. This is a data-services business with a SaaS overlay, not a SaaS business.

**9. Moat durability 3/5/10yr — CONCERN at 5yr, FAIL at 10yr.** (See B.4 below.)

**10. Hunt the disclosure that flips it — DONE.** The cash-flow statement is the flip — capitalised development + working capital consume the "profit." Also: the "£2M data cost reclassification" story (COGS shift) is wrong per the RNS — it is **incremental data acquired in new (non-PM) disease areas**, a real expansion cost. The benign "cosmetic reclassification" narrative is false; the 6pp GM compression is partly structural.

**11. Trigger must test the load-bearing variable — the provisional trigger FAILS.** Revenue +25% does not test cash conversion. Revenue can grow 25% while FCF stays negative if capitalised development and working capital keep absorbing it. Correct trigger = cash generation, specifically OCF after capitalised development.

**12. Asymmetry already captured? — PARTIAL.** Stock ran to 180p (June 2026) and pulled back to 146p — some froth is out. But 146p is still mid-range at 3.0x EV/sales with near-zero clean earnings. The "first-profit" catalyst is reported and largely priced in.

---

## B. THE RISK PROFILE

**1. Load-bearing assumption:** The platform grows revenue 20%+ **while converting to cash** — that current negative FCF is a temporary investment phase, not the steady-state cost of continuously buying data and capitalising development. The entire bull case rests on operating leverage that has **not yet appeared in cash.**

**2. Clean operating earnings / what it's worth today:** Statutory PBT £0.3M, NI £97k, OCF ~£1.2M, FCF negative. At EV ~£115M that is >500x honest earnings and ~15x flattering adj EBITDA. A defensible fair value for a 20%-grower, 82%-GM, cash-breakeven data-services business: **2.5–3.5x sales (~£96–134M EV → ~118–160p) — 146p is already inside fair value.** No margin of safety.

**3. Informative trigger:** H1 2026 operating cash flow (Sept 2026) or FY2026 FCF (spring 2027). **If revenue grows 20–25% AND genuine positive FCF materialises after capitalised development → re-rate justified.** If revenue grows but FCF stays negative → platform is a treadmill and thesis is dead. This tests the load-bearing variable directly off the cash-flow statement.

**4. Moat durability:**
- **3-year (3/5):** Real. 2,500+ lab agreements, proprietary CDx testing dataset, 18/20 top pharma embedded, switching cost = re-onboarding the lab network.
- **5-year (3/5):** Eroding. **ConcertAI + Foundation Medicine integrated Jan 2026** (500k+ patient-linked genomic+clinical records) is a direct threat; IQVIA (£50B+, 1.2B patient records) and Veeva (Crossix/Compass) can extend into PMI. Diaceutics' data edge is narrow and niche versus these balance sheets.
- **10-year (2/5):** Weak. No regulatory moat. "World's first PMI platform" is marketing, not monopoly. The data-brokering layer is exactly what LLM-native analytics and data giants commoditise. Nothing makes this a hard-to-replicate asset a decade out.

**5. Revenue quality decomposition:**
- £20.0M ARR (52% of £38.4M) — NRR 105% (minimal net expansion)
- £18.4M project/execution/milestone work (48%) — back-half-weighted, must be re-won
- Within ARR: PMx commercialization = £4.3M ARR (~21% of ARR) from **just 2 contracts**:
  - Partner Therapeutics / BIZENGRI (zenocutuzumab-zbco, ultra-rare NRG1+ cancer): ARR £2.6M, total up to £11.5M through Sept 2028
  - Unnamed US biotech: ARR £1.7M
- Concentration: fastest-growing ARR segment is tied to third-party drug commercial success that Diaceutics does not control

**6. The disclosure that flips it:** The **cash-flow statement** — specifically the capitalised development / intangibles-additions line and WC movement that turn £7.6M adj EBITDA into −£5.3M cash. If capitalised development is a permanent ~£4–5M/yr requirement, the business is structurally FCF-negative at this scale and the "20% margin" is fiction.

**7. Return if nothing re-rates:** Near-zero dividend, near-zero clean earnings, negative FCF → **~0% annual return to holder** plus risk of multiple compression. Not a CORE own-and-wait quality compounder.

---

## C. GRADE & TIER

| Sub-score | Score | Evidence |
|-----------|-------|----------|
| Q — Business Quality | 3/5 | Genuine data/network asset, 18/20 top pharma, 82% GM, real order-book; BUT 48% non-recurring lumpy revenue, weak 105% NRR, near-zero clean earnings, capital-intensive (capitalised dev eats cash). Good, not franchise-grade. |
| F — Downside Floor | 2/5 | First profit year wafer-thin (PBT £0.3M, NI £97k) off −£1.9M loss; negative FCF; cash £7.3M (~£6M net = 5% of cap); pharma-budget sensitivity already bit in 2025. Thin earnings floor, modest asset floor. |
| R — Re-Rate Likelihood | 2/5 | No dated 2x catalyst; only incremental prints ahead; already covered 3–5 analysts (not undiscovered); stock ran to 180p; first-profit catalyst is reported. "Leverage could show up" is not R-high. |
| C — Confidence | 2/5 | Non-US AIM filer; no primary PDF parsed (all 403s); unreconciled cash bridge; baseline data errors found; analyst count borderline 3–5 near ≤4 gate. **Rule-capped at 2.** |

**GRADE: C** (gated by C=2 and thin F). **TIER: PARK.** Not CORE (Q<4, F<4), not CATALYST (R<4).

**ASYMMETRY GATE CHECK:**
1. Mispriced NOW at 146p? **NO** — 3.0x EV/sales, near-zero clean earnings; price inside defensible 118–160p fair-value band.
2. Realistic bull ≥2x (→292p)? **NO** — requires 20–25% sustained growth AND expansion to premium 5–6x sales multiple the revenue quality (lumpy, 105% NRR, 48% project) does not support.
3. Upside > downside? **NO** — ~+40% to analyst PTs vs ~−30% to de-rate (2x sales / profit reversal ≈ 98p); roughly symmetric-to-inverted skew.
4. Discrete trigger or CORE quality? **NO** — no dated 2x catalyst; not CORE-grade (Q<4, F<4).

**GATE RESULT: FAILS all four.** QUALITY BENCH requires Q≥4 and durable moat — neither applies (Q=3, 10-yr moat weak). **→ PARK.**

---

## D. SKEPTIC'S CONFIRMATION CHECKLIST

| # | Item | Rating | Evidence |
|---|------|--------|----------|
| 1 | Revenue recognition | RED-FLAG (quality) | ~48% project/milestone work, back-half-weighted (H1 ~£14.6M vs FY £38.4M); recognition lumpy, not smooth subscription |
| 2 | Revenue durability | PLAUSIBLE | £38.9M order book (+56%), £21.1M 12-mo contracted, NRR 105%; but NRR just above 100% = limited expansion; project revenue must be re-won each year |
| 3 | Competitive capture | UNVERIFIED→CONCERN | ConcertAI+Foundation Medicine (Jan 2026), IQVIA, Veeva all targeting PMI; "sole PMI platform" unproven as durable exclusive |
| 4 | Moat stickiness over time | CONCERN | Strong 3yr, eroding 5–10yr; no regulatory lock; data-broker layer is commoditisation-prone |
| 5 | Customer concentration | RED-FLAG | Top client ~14.5% FY2024; PMx = 21% of ARR from 2 contracts tied to drug commercial success of an ultra-rare cancer therapy |
| 6 | Pricing power | CONCERN | GM fell 88%→82% on incremental data cost; new disease-area expansion is margin-dilutive, not accretive |
| 7 | Accounting quality | RED-FLAG | Adj EBITDA £7.6M vs −£5.3M cash; ~96% of "EBITDA" consumed below the line; capitalised development inflates profit vs cash; primary filing NOT parsed |
| 8 | Ownership & dilution | UNVERIFIED | SBC is material EBITDA add-back; dilution trajectory and insider ownership not confirmed from filing |
| 9 | Input/supply dependency | PLAUSIBLE | Data-sourcing dependency (£2.0M new-area spend proves continuous data acquisition); FX drag (~4pp reported vs CC) |
| 10 | Management credibility | PLAUSIBLE | Delivered return-to-profit and record order book; but "profit" is presentation-flattered; 6 years public before first thin profit tempers track record |

**Tally: 0 CONFIRMED · 4 PLAUSIBLE · 3 UNVERIFIED · 3 RED-FLAG.** Any thesis-core RED-FLAG caps grade at C — satisfied (3 RED-FLAGs present).

---

## E. HUMAN VERIFICATION CHECKLIST

*Before any capital — the 5 things a person must independently confirm:*

1. **Read FY2025 audited Annual Report cash-flow statement.** Extract the exact capitalised development / intangibles-additions figure and working-capital movement. Confirm whether this is a recurring ~£4–5M/yr requirement. *If FCF is structurally negative at current revenue scale → PARK becomes KILL.*
2. **Reconcile adj EBITDA £7.6M → cash outflow −£5.3M line by line** (SBC, D&A split by category, exceptional items, lease payments, tax paid, working capital). Confirm how much of "EBITDA" is real cash.
3. **Confirm analyst count precisely** — Shore Capital (Jan 2026 ✓), Canaccord Genuity (Jun 2026 ✓), RBC (~Jul 2025 ✓), Stifel (May 2025 — 2026 status unknown). If ≥5 confirmed active: COVERAGE_KILL.
4. **Confirm PMx contract terms for BIZENGRI / Partner Therapeutics** — what proportion of the up-to-£11.5M contract is guaranteed vs. contingent on zenocutuzumab commercial ramp in an ultra-rare NRG1+ cancer indication? This drives ~21% of ARR.
5. **Read customer-concentration disclosure in FY2025 Annual Report** — confirm FY2025 top-client % (FY2024 was ~14.5%) and confirm 53 customers / 95 therapeutic brands as stated.

---

## Sources

- Investegate FY2025 Final Results RNS (26 May 2026): https://www.investegate.co.uk/announcement/rns/diaceutics--dxrx/final-results/9583877
- MarketBeat Shore Capital analyst note (Jan 2026): https://www.marketbeat.com/instant-alerts/diaceutics-londxrx-stock-price-expected-to-rise-shore-capital-analyst-says-2026-01-15/
- Investing.com H1 2025 interim results: https://www.investing.com/news/stock-market-news/diaceutics-maintains-fy-targets-with-22-revenue-growth-in-h1-93CH-4145089
- TipRanks FY2025 return-to-profit announcement
- Quartr: quartr.com/companies/diaceutics-plc_16329
- Stockopedia price (Jul 2026): stockopedia.com/share-prices/diaceutics-LON:DXRX/

*Note: FY2025 cash-flow statement could not be parsed in-environment (all primary-source URLs 403-blocked). C capped at 2 by rule (non-US filer + unresolved cash bridge). This is the primary reason this is PARK (not CANDIDATE) despite a real underlying moat.*
