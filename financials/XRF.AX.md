# XRF Scientific (ASX: XRF) — Financial Baseline
*Run #53 · 2026-07-21 · §3.5 Financial Baseline*

## Provenance
- ASX annual report / half-year report / quarterly report: ✓ (revenue, NPAT, OCF, net cash directly from filings)
- Gross margin, PBT margin, ROCE: ~ (aggregator; not confirmed from filing line items)
- Price, market cap: ~ (Investing.com single-source; Yahoo Finance 403 proxy-blocked)
- 1 sell-side analyst (Eureka Report / Taylor Collison); PT A$2.26–A$2.42 ~
- fin_check.py: ⚑ NOT filing-anchored (GM, EV, P/S computed from aggregator inputs) — multiple SKIP flags; C capped ≤2

## Business Description
XRF Scientific manufactures and sells XRF (X-ray fluorescence) scientific instruments and consumables to the mining, minerals, and analytical laboratory industry. Primary segment: platinum-group crucibles and molds used in sample fusion (fire assay) — consumable razor-blade model with 10,000+ machines installed globally. Additional segments: Precious Metals trading, Capital Equipment (furnaces/instruments), Orbis Mining (elemental handheld analyzer).

Headquartered Perth, Western Australia. Founded 1973. ASX-listed. ~180 employees.

## Financial Summary (FY2025 = year ended 30 June 2025)

| Metric | Value | Trust | Source |
|--------|-------|-------|--------|
| Revenue | A$59.45M | ✓ | ASX annual report Aug 2025 |
| Revenue (FY2024) | A$60.1M | ✓ | ASX filing |
| Revenue growth FY25 | -1.1% (flat) | ✓ | derived from filings |
| Revenue 5yr CAGR (FY21→FY25) | ~17.5% | ~ | FY2021 ~$31M (aggregator) |
| Gross profit | A$28.79M | ~ | aggregator |
| Gross margin | 48.43% | ~ | aggregator |
| NPBT | ~A$14.4M | ~ | derived (~24% × $59.45M) |
| NPBT margin | ~24% | ~ | aggregator |
| NPAT | A$10.4M | ✓ | ASX annual report |
| NPAT margin | ~17.5% | ~ | derived |
| OCF | A$10.1M | ✓ | ASX annual report |
| Capex (FY2025) | ~A$2–3M | ~ | aggregator est |
| FCF (est) | ~A$7–8M | ~ | derived |
| Cash | A$12.2M | ✓ | ASX annual report |
| Debt | A$1.1M | ✓ | ASX annual report |
| Net cash | A$11.1M | ✓ | ASX annual report |
| Shares outstanding | ~142M | ~ | aggregator |
| Dilution (5yr avg) | <0.5%/yr | ~ | aggregator |
| ROCE | 25.2% | ~ | aggregator |
| Market cap | ~A$323M (~US$207M) | ~ | price A$2.28 × ~142M sh |

## Segment Breakdown (FY2025 ~, aggregator)

| Segment | Revenue ~ | NPBT margin ~ | Notes |
|---------|-----------|---------------|-------|
| Consumables | ~A$19.3M | ~37% | XRF fusion crucibles/molds — razor-blade |
| Precious Metals | ~A$21.5M | ~16% | Trading + refining |
| Capital Equipment | ~A$22.6M | ~18% | XRF furnaces, instruments |
| Orbis Mining | ~A$7.0M | ~34% | Handheld elemental analyzers |

*Note: Segment breakdown is aggregator-sourced (~); NOT confirmed from annual report segment disclosures.*

## Recent Performance

### H1 FY2026 (6 months ended 31 Dec 2025)
| Metric | H1 FY2026 | H1 FY2025 | Chg | Trust |
|--------|-----------|-----------|-----|-------|
| Revenue | A$31.3M | A$28.7M | +9.1% | ✓ |
| NPAT | A$5.3M | A$5.1M | +5% | ✓ |
| OCF | A$6.4M | A$4.4M | +44% | ✓ |

### Q3 FY2026 (3 months ended 31 Mar 2026)
| Metric | Q3 FY2026 | Q3 FY2025 | Chg | Trust |
|--------|-----------|-----------|-----|-------|
| Revenue | A$15.8M | A$13.9M | +13.8% | ✓ |
| PBT | A$3.7M | ~A$3.1M | +~19% | ✓ |
| 9M PBT (cumulative) | A$11.2M | ~A$9.8M | +14% | ✓ |

*9M FY2026 revenue: A$47.0M (+10.6% on 9M FY2025 ~$42.5M)*

### FY2026 Implied Run Rate (9M extrapolated)
- Revenue: ~A$62–64M (~+5–8% on FY2025 $59.5M)
- NPAT: ~A$11–12M (based on 9M PBT + tax at ~28%)
- EPS (diluted): ~A$0.077–0.085

## Valuation (as of A$2.28 ~, 2026-07-21 ~)
| Multiple | Value | Notes |
|----------|-------|-------|
| P/E (FY2026e) | ~27–30x | NPAT A$11–12M est |
| P/S (FY2026e) | ~5.0–5.3x | Revenue A$62–64M est |
| EV/EBITDA (FY2026e) | ~22–26x | EBITDA ~A$16–18M est |
| 52-wk range | A$1.83–A$2.40 | ~ |
| Analyst PT | A$2.26–A$2.42 | ~ (1 analyst) |
| Current vs PT | AT consensus | no meaningful discount |

## Corporate Events
- **Bruker CGA acquisition** (April 2026): Acquired Bruker's Carbon/Gas analyzer (CGA) business for USD$4.0M + USD$1.0M earnout. Business generated USD$5.3M revenue in 2025 (acquired at 0.75x revenue). Manufacturing to transfer to Perth Q3 FY2026; revenue contribution expected Q4 FY2026. Tuck-in acquisition; adds CGA instrumentation to Capital Equipment segment.
- **India office** (January 2026): First international office opened in India. South Asian mining market expansion.
- **No dividend guidance change noted**: historical dividend policy maintained.

## fin_check.py Output (2026-07-21)
```
Inputs: revenue=59.45M, gp=28.79M, npat=10.4M, ocf=10.1M, cash=12.2M, debt=1.1M
  gm=28.79/59.45=48.43% ← aggregator (SKIP file-anchor check)
  EV=323M+1.1M-12.2M=311.9M ← uses ~price (SKIP)
  FCF=10.1M-2.5M=7.6M ← capex aggregator (SKIP)
  P/S=323M/59.45M=5.43x ← ~price (SKIP)
  P/E=323M/10.4M=31.1x ← ~price (SKIP)
Provenance: revenue ✓ / gp ~ / npat ✓ / ocf ✓ / cash ✓ / debt ✓ / shares ~ / price ~
⚑ NOT filing-anchored: gp, capex, shares — figures tagged ~; C capped ≤2
PASS: FCF positive, net cash, no dilution flag, OCF>NPAT (no accruals concern)
```

## Trust Summary
| Category | Trust | Notes |
|----------|-------|-------|
| Revenue (FY2025) | ✓ | ASX filing |
| NPAT (FY2025) | ✓ | ASX filing |
| OCF / Net cash | ✓ | ASX filing |
| H1+Q3 FY2026 top-line | ✓ | ASX quarterly/half-year reports |
| Gross margin | ~ | Aggregator only |
| Segment breakdown | ~ | Aggregator only |
| Price / Market cap | ~ | Single-source (Investing.com) |
| Analyst PT | ~ | Single-source |

*C score capped at 2 (ASX foreign filer, non-SEC; no filing-anchored GM or segment data verified from primary ASX PDF)*
