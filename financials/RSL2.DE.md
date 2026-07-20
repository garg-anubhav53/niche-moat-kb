# RSL2.DE — R. Stahl AG — Financial Baseline

**As-of: 2026-07-20** · Source: Company press releases / IR / web search (snapshot.py blocked — Yahoo Finance proxy-403) · Currency: EUR · IFRS · German XTRA listing

---

## Price & Capitalization

| Metric | Value | Trust | Source / Note |
|--------|-------|-------|---------------|
| Live price | ~€16.87 | ~ SINGLE-SOURCE | web search 2026-07-20 (was €13.10 at triage May 2026; +28.8% already) |
| Shares outstanding | 6,440,000 | ~ SINGLE-SOURCE | companiesmarketcap.com / FY2025 annual report |
| Market cap (computed) | ~€108.6M | ~ | computed: €16.87 × 6.44M |
| Net debt FY2025 | €34.9M | ~ SINGLE-SOURCE | FY2025 results press release |
| EV (approx) | ~€145M | ~ | computed: €108.6M + €34.9M + ~€1.6M Q1 FCF additional burn |

---

## Income Statement

| Metric | FY2024 | FY2025 | Q1 2026 | Trust | Notes |
|--------|--------|--------|---------|-------|-------|
| Revenue | €344.1M | €313.0M (-9.1%) | €73.4M (flat YoY) | ~ | press releases; webdisclosure.com |
| Gross margin | — | ~66%? | — | ? UNVERIFIED | triage estimate only; needs primary annual report |
| EBITDA pre-exceptionals | €34.4M (10.0%) | €34.4M (11.0%) | €6.7M (9.2%) | ~ ⚠ | see NOTE below |
| D&A (derived) | — | ~€27.8M | — | ~ | computed: EBITDA €34.4M − EBIT €6.6M |
| EBIT | €15.8M (4.6%) | €6.6M (2.1%) | €1.8M | ~ | press releases |
| Net income | €5.8M | €3.0M | ~€0M (break-even) | ~ | press releases |

**⚠ NOTE on FY2025 EBITDA:** Company explicitly stated: *"The high EBITDA pre exceptionals is due to temporary positive one-time items in the area of material and personnel costs as well as a short-term increase in sales in December from major projects. The positive development of EBITDA pre exceptionals and profitability in the fourth quarter of 2025 does NOT reflect R. STAHL's global business development."* — The FY2025 EBITDA €34.4M is therefore NOT the normalized run rate. FY2026 guided EBITDA of €22-27M (midpoint €24.5M) is the forward proxy for normalized earnings.

---

## Balance Sheet & Cash Flow

| Metric | FY2024 | FY2025 | Q1 2026 | Trust |
|--------|--------|--------|---------|-------|
| Net financial debt | €28.7M | €34.9M (+€6.2M) | ~€36.5M est. | ~ |
| Free cash flow | +€14.8M | -€0.3M | -€1.6M | ~ |

**FCF reconciliation gap (⚠ UNVERIFIED):** EBITDA pre-ex was €34.4M but FCF was -€0.3M — a €34.7M gap. Even after subtracting estimated taxes, interest, and capex (typical for a mfg company: ~€12-15M capex + ~€3M interest + ~€3M taxes = €18-21M), the implied working capital build would be ~€13-16M. Nature of this working capital build is NOT explained in press releases — needs primary annual report read.

---

## FY2026 Guidance

| Metric | Guidance | Trust | Notes |
|--------|----------|-------|-------|
| Revenue | €285M–€300M (midpt ~€292M) | ~ | -6.7% from FY2025 at midpoint |
| EBITDA pre-exceptionals | €22M–€27M (midpt €24.5M) | ~ | -29% from FY2025 "stable" headline; reflects true normalized earnings |
| Implied EBIT (derived) | ~(€5)M to ~(€1)M | ~ computed | EBITDA guide minus D&A ~€28M → near-zero to slightly negative |
| Implied net income | Likely near-zero to negative | ~ computed | based on EBIT trajectory |

---

## Valuation Matrix (at €16.87 / ~€108.6M mktcap / ~€145M EV)

| Multiple | Value | Notes |
|----------|-------|-------|
| EV/EBITDA (FY2025 reported) | ~4.2x | MISLEADING — reported EBITDA contained temporary items |
| EV/EBITDA (FY2026 guided midpt €24.5M) | **~5.9x** | Better normalized proxy |
| EV/Revenue (FY2026 guided midpt €292M) | ~0.50x | Cheap on sales; sales still declining |
| P/E (FY2025 net income €3.0M) | ~36x | Thin earnings; FY2026 likely loss year |
| Analyst consensus PT | €18.875 avg (2 analysts, all Strong Buy) | +**11.9%** upside from €16.87 |
| 2x scenario price | €33.74 | Requires EV/EBITDA ~10.3x on guided EBITDA: heroic multiple on a declining business |

---

## Analyst Coverage

- **2 German-language analysts** (both Strong Buy, avg PT €18.875)
- 0 English-language analyst initiations known
- Coverage gate: 2 analysts = PASS (≤4 required)

---

## NEXUS Transformation Program

Launched Q1 2026; three-stage roadmap:
- **Stage 1 "Foundation & Stabilization" (2026-2027):** Cost reduction, organizational streamlining, leaner hierarchy; social partner negotiations underway. Q1 2026 cost savings already contributing (+€3.1M EBITDA vs Q1 2025).
- **Stage 2 "Transformation & Building" (2027-2028):** Market repositioning, megatrend portfolio focus (LNG/H2 for hazardous environments)
- **Stage 3 "Growth & Leadership" (2028+):** Target €500M revenue by 2030 (vs €313M FY2025)

Target repositioning: "component expert" → "global leader for solutions in explosion protection & harsh environments."

---

## Triage Price vs. Current Price

| Date | Price | Market Cap | EV |
|------|-------|------------|-----|
| Triage (May 2026) | €13.10 | €84.4M | ~€119M |
| Current (2026-07-20) | **€16.87** | **€108.6M** | **~€145M** |
| Change | **+28.8%** | +€24.2M | +€26M |

A significant portion of the discoverable gap has already closed between triage and deep-dive.

---

## fin_check.py / snapshot.py Status

**NOT RUN** — snapshot.py and fin_check.py blocked (Yahoo Finance proxy-403). All figures are ~SINGLE-SOURCE from press releases / web search. Primary German annual report (AR2025) not directly parsed. Gross margin and FCF decomposition remain ? UNVERIFIED.

**Financials: PROVISIONAL — primary filing verification required before any capital decision.**

---

## Sources

- FY2025 results press release: webdisclosure.com "Weak demand in financial year 2025 reflected in R. STAHL's figures"
- FY2025 EBITDA clarification: webdisclosure.com "R. STAHL Surpasses EBITDA Expectations for 2025 as a result of temporary effects"
- Q1 2026 press release: eqs-news.com / webdisclosure.com "R. STAHL reports generally stable business development in the first quarter of 2026 – NEXUS program for the future launched"
- NEXUS details: tradingview.com EQS; investing.com Q1 2026 slides / earnings call transcript
- Shares outstanding: companiesmarketcap.com (FY2025)
- Current price / market cap: stockanalysis.com, investing.com (2026-07-20 web search)
- Analyst PT: web search result (2 analysts, avg €18.875, Strong Buy)
