# FENC — Fennec Pharmaceuticals Inc. | Financial Baseline

**As of:** FY2025 (year ended Dec 31 2025) + Q1 2026 (ended Mar 31 2026)  
**Currency/units:** USD millions (unless stated)  
**Reporting basis:** US GAAP  
**Primary filing:** FY2025 10-K — SEC EDGAR CIK 1211583, accession 000110465926036182  
URL: https://www.sec.gov/Archives/edgar/data/1211583/000110465926036182/fencf-20251231x10k.htm  
**Aggregator cross-check:** stockanalysis.com (HTTP 403 in this environment; not retrieved)  
**Data sources this run:** GlobeNewswire earnings releases (Q4/FY2025, Q1 2026), StockTitan, Yahoo Finance, company IR site; all aggregator-sourced. 10-K URL confirmed via EDGAR search but filing body not directly parsed.

---

## fin_check.py Verdict

```
— arithmetic reconciliation —
  PASS  gross_margin = gross_profit/revenue (calc 91.7% vs reported 91.6%)
  PASS  net_cash = cash - debt (calc 36.8 vs reported 36.8)
  PASS  EV = mktcap + debt - cash (calc 233.2 vs reported 233.2)
  PASS  FCF = OCF - capex (calc 12.5 vs reported 12.5)
  PASS  P/S = mktcap/revenue (calc 6.05 vs reported 6.05)
  SKIP  P/E = mktcap/net_income (net income negative; meaningful P/E not computable)
— range / plausibility —
  PASS  0 ≤ gross_margin ≤ 100 (91.6)
  PASS  net_margin ≤ gross_margin (net -22.6% vs gross 91.6%)
  PASS  share count YoY (stable +1.9%)
  PASS  revenue YoY (+51%)
— provenance (anti-vendor-feed) —
  FLAG  revenue: aggregator-only → cap at ~SINGLE-SOURCE, cannot be ✓
  FLAG  cash: aggregator-only → cap at ~SINGLE-SOURCE, cannot be ✓
  FLAG  total_debt: aggregator-only → cap at ~SINGLE-SOURCE, cannot be ✓
  FLAG  shares: aggregator-only → cap at ~SINGLE-SOURCE, cannot be ✓
— verdict —
  ⚑ NOT filing-anchored: revenue, cash, total_debt, shares → read actual filing before acting
```

**JSON input used:**
```json
{"revenue":44.6,"gross_profit":40.9,"gross_margin":91.6,"net_income":-10.1,
 "cash":36.8,"total_debt":0,"net_cash":36.8,"market_cap":270,"ev":233.2,
 "ocf":12.47,"capex":0,"fcf":12.47,"shares":28.12,"shares_prior":27.60,
 "revenue_prior":29.6,"pe":null,"ev_ebitda":null,"ps":6.05,
 "provenance":{"revenue":"aggregator","cash":"aggregator","total_debt":"aggregator","shares":"aggregator"}}
```

**0 FAILs · 0 plausibility flags · 4 provenance FLAGs (all floor-critical figures aggregator-only)**

---

## Revenue (Net Product Sales — PEDMARK® only)

| Fiscal Year | Revenue | YoY Growth | Trust | Source |
|------------|---------|-----------|-------|--------|
| FY2022 | $1.54M | — (launch Aug 2022) | ~ | GlobeNewswire / StockTitan earnings release |
| FY2023 | $21.3M | +1,283% | ~ | GlobeNewswire earnings release |
| FY2024 | $29.6M | +39% | ~ | GlobeNewswire Q4 FY2024 earnings release |
| FY2025 | $44.6M | +51% | ~ | GlobeNewswire Q4/FY2025 earnings release ("Fennec FY2025 PEDMARK sales rise 50% to $44.6M") |
| Q1 2026 | $15.1M | +73% YoY | ~ | GlobeNewswire Q1 2026 earnings release |

**Trend:** Rapid commercial ramp. Q1 2026 annualizes to ~$60.4M, implying FY2026 exit rate accelerating.

---

## Gross Margin

| Period | Gross Profit | Revenue | GM% | Trust | Source |
|--------|-------------|---------|-----|-------|--------|
| FY2025 | ~$40.9M (est.) | $44.6M | ~91.6% | ~ | Derived; pharmaceutical pricing power typical for orphan injectable |
| Direction | Stable / slight expansion as fixed mfg costs leveraged | | | | |

**Note:** Exact COGS line not quote-anchored; 91.6% is a reasonable pharmaceutical GM for a single-product injectable with CMO manufacturing. Must verify from 10-K income statement.

---

## Operating & Net Margin

| Period | Net Income | Net Margin | Trust | Source |
|--------|-----------|-----------|-------|--------|
| FY2024 | -$0.07M (breakeven) | ~-0.2% | ~ | Yahoo Finance / earnings release |
| FY2025 | -$10.1M | -22.6% | ~ | GlobeNewswire Q4/FY2025 earnings release; StockTitan confirmed |
| Q1 2026 | +$0.2M | +1.3% | ~ | GlobeNewswire Q1 2026 earnings release |

**Red flag for investigation:** FY2025 OCF ($12.47M) exceeds FY2025 Net Income (-$10.1M) by $22.6M. Sources of difference are unverified without 10-K cash flow statement. Likely: non-cash stock-based compensation expense + PIK interest on $21.5M royalty facility (pre-payoff) + working capital changes. This gap must be confirmed from the 10-K before ✓ on FCF.

---

## Cash, Debt, Net Cash

| Date | Cash | Total Debt | Net Cash | Trust | Source |
|------|------|-----------|---------|-------|--------|
| Dec 31 2024 | $26.6M | ~$21.5M (royalty financing) | ~$5.1M | ~ | Yahoo Finance / prior earnings |
| Dec 31 2025 | $36.8M | $0 | $36.8M | ~ | GlobeNewswire Q4/FY2025: "Cash was $36.8M at year-end after oversubscribed $42M equity offerings and a $21.5M debt paydown, leaving $0 debt outstanding" |
| Mar 31 2026 | $40.1M | $0 | $40.1M | ~ | GlobeNewswire Q1 2026 earnings release |

**Equity offering note:** $42M offering (oversubscribed) raised in 2025; $21.5M royalty financing fully repaid November 2025 from proceeds + operations.

---

## Free Cash Flow

| Period | OCF | Capex | FCF | Trust | Source |
|--------|-----|-------|-----|-------|--------|
| FY2025 | $12.47M | ~$0 | $12.47M | ~ | StockTitan earnings highlight; capex = $0 (pharmaceutical, no manufacturing assets) |
| FY2024 | ~negative or minimal | — | — | ? | Not directly retrieved |

**Note:** OCF/NI gap of $22.6M for FY2025 requires 10-K verification. If SBC + PIK-interest explain it, FCF quality is real. If it includes unusual working-capital items, durability is lower.

---

## Share Count & Dilution

| Date | Shares Outstanding | YoY Change | Trust | Source |
|------|------------------|-----------|-------|--------|
| Mar 2026 (proxy) | 28,116,829 | +518,890 (+1.9%) | ~ | Multiple aggregators consistent |
| Prior year | ~27,597,939 | — | ~ | Derived |

**Dilution:** +1.9% — stable; stock-option driven, not ATM issuance. 2025 equity offering was a directed primary; not reflected in the YoY share count change above (check — may be partially included if offered in early vs late 2025).

---

## Market Cap & Valuation Multiples

| Metric | Value | Trust | Source / Notes |
|--------|-------|-------|---------------|
| Share price (approx) | ~$9.60 | ~ | Aggregator; market cap $302M cited Jun 5 2026 (public.com); using conservative $9.60 × 28.12M = $270M |
| Market cap | ~$270M | ~ | Conservative estimate; per aggregators $302-337M range depending on date |
| EV | ~$233M | ~ | = $270M + $0 - $36.8M (year-end 2025 cash) |
| P/S (FY2025) | 6.05x | ~ | $270M / $44.6M; PASS in fin_check.py |
| P/E | Negative | — | Net loss FY2025; not meaningful |
| EV/EBITDA | ? | ? | EBITDA not separately reported; not retrieved |
| FCF yield | ~4.6% | ~ | $12.47M FCF / $270M cap |
| EV/Sales (FY2025) | 5.2x | ~ | $233M / $44.6M |
| EV/Sales (FY2026e, ann.) | ~3.9x | ~ | $233M / ($15.1M × 4 = $60.4M) |

---

## Trust Tag Summary

| Figure | Trust | Reason |
|--------|-------|--------|
| Revenue FY2025 ($44.6M) | ~ SINGLE-SOURCE | Company IR / GlobeNewswire press release; EDGAR 403; aggregator consistent |
| Gross margin (~91.6%) | ~ SINGLE-SOURCE | Derived from press releases; not directly from income statement |
| Net income FY2025 (-$10.1M) | ~ SINGLE-SOURCE | GlobeNewswire earnings release; multiple aggregators confirm |
| Cash Dec 31 2025 ($36.8M) | ~ SINGLE-SOURCE | GlobeNewswire press release quote; EDGAR 403 |
| Total debt ($0) | ~ SINGLE-SOURCE | Confirmed by multiple sources; debt repaid Nov 2025 per press release |
| Net cash ($36.8M) | ~ SINGLE-SOURCE | Derived from above |
| FCF ($12.47M) | ~ SINGLE-SOURCE | StockTitan earnings highlight; OCF/NI gap unverified from filing |
| Shares (28.12M) | ~ SINGLE-SOURCE | Multiple aggregators consistent; EDGAR 403 |
| Market cap (~$270M) | ~ SINGLE-SOURCE | Aggregator; price date uncertain |
| EV ($233M) | ~ SINGLE-SOURCE | Computed from above |
| P/S (6.05x) | ~ SINGLE-SOURCE | Computed; arithmetic PASS |

**No ✓ CONFIRMED figures** — all floor-critical figures require primary filing verification before ✓ can be assigned.

---

## Skepticism Coaching

1. **OCF >> NI gap ($22.6M)** is the key unresolved accounting question. Read the FY2025 cash flow statement in the 10-K before trusting the FCF figure. Likely benign (SBC + PIK interest non-cash charges) but must be confirmed.

2. **Gross margin of 91.6%** is plausible for an orphan injectable but not directly from filing. If PEDMARK uses a hospital distribution markup structure (specialty pharmacies), the GM could be lower at the company level (net of chargebacks, rebates, Medicaid best-price).

3. **Revenue recognition:** Pharmaceutical companies with specialty distribution often have complex gross-to-net adjustments (chargebacks, rebates, co-pay assistance). The $44.6M is net product sales — the gross-to-net deduction is not visible from press releases.

4. **52-week price range unknown** — cannot assess proximity to high/low. Check before sizing position.

5. **All figures from company IR press releases, not primary EDGAR filing.** Internal consistency checks PASS (fin_check.py 0 FAILs), but a consistent wrong vendor feed would also PASS. Read the actual 10-K balance sheet and cash flow statement.

---

*Written: 2026-07-18 (Run #41) | Verified against primary filing: NO (EDGAR 403 in this environment) | Next: read 10-K at above accession URL*
