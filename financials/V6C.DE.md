# V6C.DE — Viscom SE
*§3.5 Financial Baseline — Run #68 | orig. 2026-07-27 | **CORRECTED 2026-07-27 by §5 red-team** (memos/V6C.DE-2026-07-27.md)*
*C=2 (egress policy blocked WebFetch/curl on every host; zero primary-filing pages read; web-search baseline only)*

> **⚠ THIS FILE WAS MATERIALLY WRONG IN ITS FIRST VERSION.** The §5 deep-dive found 4 re-derivation errors, 3 double-counted score items, and 2 entirely missed risks. Corrections marked **[CORR]**. Outcome: 9/12 QUEUED → **rescored ~5.5-6/12 → GRADE D / TIER PARK.**

## Identity
- Exchange: XTRA (Frankfurt) · ISIN DE0007846867 · Sector 18 (precision instruments & sensing)
- AOI/SPI/AXI/inline-CT inspection systems for PCB & electronics manufacturing; OEM X-ray tubes
- ~460-500 employees (⚠ mwb research ~462; company ~500) · listed 1998 · AG→SE conversion completed 5 Jun 2024

## Price & Cap (Jul 27, 2026)
| Item | Value | Trust |
|---|---|---|
| Price | €4.98 (€5.50 on Jul 6 → **-9% in 3 weeks**) | ✓ |
| Shares issued | **9,020,000** (Satzung, €1.00/share) | ✓ **[CORR]** |
| Treasury | **1.50%** (~135,300 sh, bought back 2008/09) | ✓ **[CORR]** |
| Shares outstanding | **~8,885,000** | ✓ **[CORR]** — orig. 8.88M was back-solved circularly from cap÷price |
| Market cap | **€44.25M** (9.02M × 0.985 × €4.98 — reconciles exactly) | ✓ |
| Ownership | **Founders Heuser+Pape 60.36%** (incl. foundations) · free float 38.14% ≈ **€17M** | ✓ **[NEW]** |
| Liquidity | **~€10-30k/day** traded value | ⚠ **[NEW]** near-disqualifying |

## Income Statement
| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Trust |
|---|---|---|---|---|---|
| Revenue | €105.5M | €118.78M | €84.082M | **€81.705M** | ✓ |
| YoY | +32% | +12.6% | -29.2% | -2.8% | ✓ |
| Gross margin (German *Rohertrag* — personnel BELOW the line) | — | 62.5% | 61.2% | ~64.7% | **⚠ [CORR]** aggregator-only, NOT filing-confirmed (was ✓) |
| EBIT reported | **€8.1M (7.6%)** | €6.611M (5.6%) | **-€11.818M (-14.1%)** | **-€1.815M (-2.2%)** | ✓ **[CORR]** — orig. said FY24 "~-€14M" |
| EBIT before special effects | — | — | **-€7.095M** (ex €4.723M restructuring) | -€1.815M (no add-back) | ✓ **[NEW]** |
| Net result | — | €3.04M ~ | **-€9.629M** (EPS -€1.06) | **-€5.625M** | ✓ **[CORR]** — orig. said FY25 "~-€6.6M implied" |
| Order intake | — | — | €75.050M | **€80.982M (+8%)** | ✓ |

**PEAK EBIT MARGIN IS 7.6% (FY2022 @ €105.5M revenue)** — not 5.6%. Material to the 2x case.

## Quarterly bridge (derived, all cross-checks reconcile)
| Period | Revenue | EBIT |
|---|---|---|
| Q1 2025 | €19.789M | +€0.024M (0.1%) |
| 9M 2025 | €56.751M | -€1.769M (-3.1%) |
| FY2025 | €81.705M | -€1.815M (-2.2%) |
| **⇒ Q4 2025 (derived)** | **€24.954M** (≈€100M annualised) | **-€0.046M (≈ZERO)** |
| **Q1 2026** | **€14.360M (-27.4%)** | **-€3.994M** |

Q1 2026: order intake €21.808M (+7.0%) · backlog €26.644M (+29.9%) · **book-to-bill 1.52** — all ✓

## Regional P&L **[NEW — the decomposition that matters]**
| Region | FY2024 rev | FY24 EBIT % | FY2025 rev | FY25 EBIT % | Rev YoY |
|---|---|---|---|---|---|
| **Europe** | €49.869M (59.3%) | **-26.1%** | €46.849M (**57.3%**) | **-7.5%** | -6.1% |
| Asia | €21.624M (25.7%) | -0.1% | €24.175M (29.6%) | **+2.7%** | +11.8% |
| Americas | €12.589M (15.0%) | +4.7% | €10.681M (13.1%) | +1.8% | -15.2% |
| **Total** | **€84.082M ✓** | -14.1% | **€81.705M ✓** | -2.2% | -2.8% |

Regional revenue sums to group revenue **exactly** both years → split ✓ CONFIRMED (margins ~).
**57% of revenue is in a shrinking, structurally loss-making region.**
Concentration: top-5 customers **~62%** of revenue (FY2023 ~, AG single-entity) · automotive **~70%** ~

## Balance Sheet
| Metric | Dec 31, 2024 | Dec 31, 2025 | Mar 31, 2026 (est.) | Trust |
|---|---|---|---|---|
| Total assets | €94.64M ~ | **€90.648M** | — | ✓ Dec-25 |
| Current assets | — | **€59.810M** | — | ✓ |
| Current liabilities | — | **€35.585M** | — | ✓ |
| Total equity | €50.68M ~ | **€44.022M** | **~€39.8M (derived)** | ✓ Dec-25 |
| Equity ratio | 53.6% | **48.6%** | ~46% | ✓ |
| Cash | €5.53M ~ | **€3.908M** | — | ✓ Dec-25 |
| Bank overdraft | €9.88M ~ | **UNCONFIRMED** (Jun-25: €15.88M ~) | — | **? floor-critical** |
| Net debt incl. IFRS16 | ~€16M est. | **~€18-25M est.** | — | **⚠ UNVERIFIED** |
| **NCAV** (CA − total liabs) | — | **€13.184M = €1.48/sh** | — | ✓ derived |

- **BVPS: €4.95 (Dec-25) → ~€4.48 (Mar-26 est.) · P/B ~1.11x · 3.4x NCAV**
- **NOT trading at book [CORR]** — orig. claimed "cap €44.248M ≈ equity €44.022M = at book". Stale: it ignored the Q1 2026 loss. **Not a net-net, not close.**
- **Dividend:** cut 27 Feb 2024 *"to preserve liquidity"*; last paid €0.05 on 3 Jun 2024; **none since** ✓
- **⚠ DILUTION OVERHANG [NEW]:** AGM 5 Jun 2026 tabled authorised capital of **€4,500,000 / 4,500,000 new shares ≈ 50% of share capital**, cash and/or non-cash. Vote outcome UNVERIFIED. Orig. baseline recorded "dilution: none identified."

## Derived operating model
OpEx = (Revenue × GM) − EBIT: **~€57.3M (FY22) → €67.63M (FY23) → €63.28M (FY24) → €54.69M (FY25)** — restructuring real, **-19.1% vs FY23** (145 staff, €4.723M charge).

**Breakeven revenue = 81.705 + 1.815/GM ≈ €84.5-84.7M — ROBUST to the GM assumption.**
FY2026 EBIT ≈ (Revenue − €84.6M) × 0.647:
| FY26 revenue | EBIT | In guided band €1.6-4.5M? |
|---|---|---|
| €80M (guidance low) | **-€2.98M** | ✗ |
| €84.4M (analyst est.) | -€0.07M | ✗ |
| €85M (guidance MID) | +€0.32M | ✗ |
| €87.1M | +€1.68M | ✓ just |
| €90M (guidance high) | +€3.49M | ✓ |

**The FY2026 EBIT band is only reachable at ~€87-90M revenue — the top ~30% of the guided revenue range. At the midpoint, EBIT ≈ ZERO.**

## Guidance track record — **RED FLAG [NEW]**
| FY | Guidance (last confirmed) | Actual | Verdict |
|---|---|---|---|
| 2022 | rev €95-100M, EBIT €4.7-8.0M | €105.5M / €8.1M (7.6%) | **BEAT** |
| 2023 | rev €110-120M, EBIT 5-10% (conf. 14 Nov 2023) | €118.78M / €6.611M (5.6%) — **bottom** | HIT AT FLOOR (dividend cut 3mo later) |
| 2024 | **CUT TWICE** (23 May, 6 Aug 2024) → EBIT b.s.e. -3% to -9% | order intake €75.05M **below corridor even after 2 cuts**; EBIT b.s.e. -€7.095M | **DOUBLE CUT, STILL MISSED** |
| 2025 | rev €80-90M, **EBIT 2-5% (€1.6-4.5M)** — conf. May, Aug, **13 Nov 2025** | rev €81.705M ✓; **EBIT -€1.815M** — sign flip | **SEVERE MISS** |
| **2026** | rev €80-90M, **EBIT 2-5% — NUMERICALLY IDENTICAL to FY2025** | Q1 EBIT **-€3.994M** (€4.0M worse than Q1'25); conf. 12 May & 4 Jun | in progress |

**EBIT has landed at or below the bottom of the guided range three years running. Reaffirmed +€1.6-4.5M on 13 Nov 2025 — seven weeks from year-end — then printed -€1.815M.** Zero management turnover throughout; co-founder Pape on the supervisory board oversees co-founder Heuser on the management board, with 60.36% of the votes between them.
**[CORR] Orig. baseline called FY2026 "first positive EBIT guidance in 2+ years." FALSE — FY2025 carried the identical guidance and missed it.**

## Competitive position **[NEW]**
| Player | FY2025 revenue | FY2025 growth | Q1 2026 |
|---|---|---|---|
| Koh Young | ≈€145-155M | **+14.9%** | **+42%** (OP +209%); core SMT ≈**+38%** |
| ViTrox (board-inspection segment) | ≈€105M | group **+52.7%** | Q4'25 +95% |
| **Viscom** | **€81.7M** | **-2.9%** | **-27.4%** |

**Viscom is #4-6 globally, not "top three worldwide."** Koh Young's *core SMT* grew ~38% in the exact quarter Viscom fell 27.4% → share loss, not merely a cycle. Coverage: 3-4 analysts, loudest is **mwb research — ISSUER-PAID** (PT €4.80→€5.00→€6.00→**€8.00**, a 67% raise in ~6 weeks, the last raise *after* the FY2025 miss).

## §4 Promise Score — **RESCORED [CORR]**
Original 9/12 double-counted three facts (failure mode #4): "trading at book" lifted both Valuation gap and Floor quality; "first positive EBIT guidance" lifted Valuation gap, Catalyst proximity and Business quality; "64.7% GM" lifted Moat clarity and Business quality. Scored once each, and with the corrected facts:

| Axis | Orig | **Corrected** | Rationale |
|---|---|---|---|
| Moat clarity | 1.5 | **1.0** | AXI/CT real; AOI algorithm moat being commoditized by AI; #4-6 not top-3 |
| Business quality | 1.5 | **1.0** | Peak EBIT 7.6%; Europe (57%) loss-making; top-5 ~62%; no recurring base |
| Coverage void | 1.5 | **1.0** | Covered by 3-4 analysts incl. issuer-paid; not a void — and 60% control means no M&A path |
| Valuation gap | 2.0 | **0.5** | ~1.11x book, 3.4x NCAV, 0.80x EV/S, negative clean EBIT; at/above fair value |
| Catalyst proximity | 1.0 | **1.0** | H1 2026 report ~mid-Aug 2026 is genuinely dated |
| Floor quality | 1.5 | **0.5** | Above book, eroding ~€4M/qtr, net debt unverified, **50% dilution authority** |
| **TOTAL** | **9/12** | **~5.0-6.0/12** | below QUEUED threshold — should not have reached the deferred queue |

## Routing — **[CORR] QUEUED 9/12 → GRADE D / TIER PARK**
**Asymmetry Gate: 1 of 4 PASS → FAIL.** (1) not mispriced — at/above a €3.50-4.50 fair-value centre; (2) 2x needs €96-99M revenue AND 12-15x on a 60%-controlled, €10-30k/day-liquidity micro-cap with 3 straight missed EBIT guides — the *multiple* is heroic (the 7.6% margin itself is precedented); (3) skew ~symmetric (+33% consensus vs -25/-40%); (4) ✓ dated trigger (H1 2026 report), but asymmetric in the wrong direction — guidance was also "confirmed" at the half-year in both 2024 and 2025.

Not Bench (requires Q≥4 + durable moat failing only on price). **PARK** with a re-entry trigger, since order momentum (+8% FY25, +7% Q1'26, backlog +30%, book-to-bill 1.52, order guidance raised to €90-100M) and the FY2027 inline-CT battery order are genuinely real.

- **Buy-zone:** ≤ **€3.30/sh ≈ €29M cap ≈ 0.74x book** — even then the €17M free float caps size at token.
- **Upgrade:** H1 2026 EBIT ≥ -€1.0M on H1 revenue ≥ €38M · OR FY2027 guidance ≥ €95M rev @ ≥6% EBIT · OR Europe at EBIT breakeven · OR authorised capital left unused through FY2027.
- **Downgrade → KILL:** FY2026 guidance cut at the H1 print (base case) · OR net debt confirmed >€28M · OR ANY drawdown of the ~50% authorised capital · OR H1 2026 EBIT worse than -€5M · OR a 3rd straight year of inventory/receivable write-downs.

**Full §5 adversarial memo: `memos/V6C.DE-2026-07-27.md`**

*Sources: EQS ad-hoc 23 Feb 2026 · EQS corporate 31 Mar 2026 (audited FY2025) · EQS 12 May 2026 (Q1 2026) · EQS ad-hoc 4 Jun 2026 (order guidance raise) · EQS 13 Nov 2025 (9M) · EQS 14 Aug 2025 (H1) · EQS 20 May 2025 (Q1 2025) · EQS 25 Mar 2025 (FY2024 + FY2025 guidance) · EQS ad-hoc 23 May & 6 Aug 2024 (FY2024 guidance cuts) · EQS ad-hoc 27 Feb 2024 (dividend cut) · EQS AGM convocation 5 Jun 2026 · Viscom SE Satzung · Viscom IR shareholder structure · Viscom AG Lagebericht 2023 (customer concentration) · mwb research initiation 26 May 2025 + 05/2026 raise · Koh Young FY2025/Q1 2026 · ViTrox FY2025 · Manz AG insolvency 18 Dec 2024.*
*Trust: ✓ headline P&L, order data, regional revenue split, share count/cap chain (all internally reconcile). ⚠ gross margin (aggregator-only), net debt (unverified). ? Dec-25 overdraft, FY25 OCF/FCF, Q1'26 balance sheet, AGM vote outcome. **NO primary-filing page was read — egress policy blocked WebFetch/curl on every host.***
