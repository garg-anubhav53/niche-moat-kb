# COVERAGE — the denominator, and how much of it we've seen

The point of the top-of-funnel rework: stop *hoping* web search surfaces names, and instead **enumerate a known universe and march through it best-first**, so we can answer "what % of the worthwhile microcaps have we actually looked at?"

## The worthwhile universe (the denominator)

**US — fully enumerable via SEC frames (`tools/screen.py`, deterministic, ~4 API calls, zero LLM):**
- All filers reporting revenue: ~4,200
- Worthwhile subset — revenue $20–400M, gross margin 45–95%, **profitable**: **~78** (as of CY2025; ~236 if you include cash-burners)
- This is the denominator. Coverage % = (US names deep-reviewed) ÷ 78. **A run that reviews the top-10 unreviewed covers ~13% of the worthwhile US universe.** By a handful of passes we can honestly cover the *majority* of profitable high-margin US microcaps — and know it.
- The screen is ranked by a quality proxy (operating margin, gross margin, capped growth), so we march **best-first** — even partial coverage captures the best names.

**International data sources — VERIFIED (probed 2026-07-18):**

| Market | Bulk source | Key? | Status |
|--------|-------------|------|--------|
| **US** | SEC XBRL `frames` API | none | ✅ built+tested (`screen.py`) — full GM+profit filter, ~78 names |
| **Taiwan** | TWSE OpenAPI (keyless) | none | ✅ built+tested (`screen_tw.py`) — full GM filter, ~64 names |
| **Europe** (EU exchanges + UK) | filings.xbrl.org ESEF/UKSEF (keyless) | none | ✅ built+tested (`screen_eu.py`) — enumeration; per-name fundamentals |
| **Japan** | EDINET API v2 | free key | ✅ built+tested (`screen_jp.py`) — key set in env; **BUT proxy blocks outbound to EDINET (403 Forbidden run #42 and run #43)** — web search fallback used for both Japan runs; 0% EDINET systematic coverage to date; fix: allow `api.edinet-fsa.go.jp` in environment network policy |
| **Korea** | OpenDART (`opendart.fss.or.kr`) | free key | ⏳ `screen_kr.py` pending `OPENDART_KEY` |
| **Canada** | mostly via SEC (many TSX names file 40-F/20-F, already in US frames) + per-name Yahoo (.TO) | none | partial |
| **Australia/NZ** | no free bulk fundamentals; per-name Yahoo (.AX/.NZ) | none | per-name |
| **UK (also)** | Companies House API (free key) — but UK already covered by filings.xbrl.org UKSEF | free key | redundant |

**Build order:** Europe (filings.xbrl.org) + Taiwan (TWSE) are keyless → build next. Japan/Korea → build once the free keys are set as env vars in the routine environment. Canada is largely absorbed by the US frames (cross-listed 40-F filers); pure-domestic TSX names go per-name. For any market without bulk fundamentals, the denominator is "all listed in cap band" (exchange list) and we march per-name with `snapshot.py` price + the filing.

## Ledger — reviewed vs. remaining (updated by the routine)

| Universe | Denominator | Reviewed | Coverage % | Cursor (next best-unreviewed) |
|----------|-------------|----------|-----------|-------------------------------|
| US profitable high-GM microcaps | ~78 | 0 | 0% | run `screen.py`, start rank 1 |
| Japan (EDINET) | TBD (needs key) | 0 | — | pending EDINET key |
| Korea (OpenDART) | TBD (needs key) | 0 | — | pending OpenDART key |
| Other exchanges (list-enumerated) | per exchange | — | — | rotate |

*The routine refreshes `screen.py` periodically (the universe drifts as filings update), marks each reviewed CIK in SEEN, and advances the cursor down the ranked worklist. Never re-screen a SEEN ticker.*

## Sector 18 (Precision instruments & sensing) — Pass 2 Coverage Notes (run #46, 2026-07-20)

**US geo lens (Nasdaq/NYSE):** Structurally sparse. M&A wave removed most quality public micro-caps:
- FARO Technologies → acquired by Ametek, delisted Nasdaq July 2025 (sole-source 3D metrology moat was real)
- Luna Innovations (LUNA) → Nasdaq suspended Jan 2025; Form 25 + Form 15 filed; went dark (ODiSI OFDR moat real but thesis unexecutable)
- MTS Systems → acquired by Amphenol 2021; NI (National Instruments) → acquired by Emerson 2023; Thermon → acquired by CECO; Starrett → pending privatization
- Remaining public names (MLAB, TRNS, VPG, INTT, COHU, MASS) all either over-capped or already reviewed in prior runs
- Net result: **0 new QUEUED from US; 1 PARK (CLIR dev-stage INTEGRITY_KILL); 1 CAP_SOFT (Mistras Group ~$580M)**

**Taiwan geo lens (TWSE/TPEx):** Similarly thin. Most precision instrument names either >$1B cap (Chroma ATE 2360.TW, MPI Corp, Hiwin) or failed other gates:
- 6830.TW (MSSCorps) → INTEGRITY_KILL + CAP_SOFT: net losses, "CPO monopoly" investor narrative refuted (iST + Hongkang competing)
- 4537.TWO (Shuz Tung Machinery) → PARK 5/12: WisePioneer inspection niche real but not sole-source; legacy pipe bender dilutes moat; non-EN filing
- Net result: **0 new QUEUED from Taiwan; 1 PARK**

**Deferred queue resolutions:**
- HVO.L → COVERAGE_KILL: triage "0-1 analysts" was a data error; financial fetch confirmed 7 analyst estimates
- CML.L → PARK Grade D after §5: real PMR qualification moat; but adj PBT -£1.76m; rev declining -11%; sole analyst target 223p < 265p market price; asymmetry gate FAIL 4/4

**Sector 18 status: 2 passes complete. Next pass should use European geo lens (German XTRA precision instruments, Swiss SIX) or Japan non-EN secondary names (6853.T and 6858.T from deferred queue first).**

---

## Sector 19 (Specialty healthcare services & niche pharma) — Pass 2 Coverage Notes (run #47, 2026-07-20)

**UK AIM + ASX + Nordic/Canada geo lens:** ~38 names processed; ~27 killed; 4 advanced to QUEUED/WATCH; 1 Quality Bench addition (RX.V BioSyent).

**Coverage kills — notable high-quality names excluded by analyst count:**
- PHO.OL (Photocure ASA, Oslo Bors): sole FDA+EMA approved blue-light cystoscopy agent (Hexvix/Cysview, HAL); 94% gross margin; debt-free; patent to 2036. COVERAGE_KILL: 5-7 Norwegian regional analysts (Pareto, DNB Markets, ABG Sundal Collier, Arctic, Carnegie). KB baseline written at financials/PHO.OL.md.
- CUV.AX (Clinuvel Pharmaceuticals, ASX): sole FDA+EMA approved EPP treatment (afamelanotide/SCENESSE); REGULATORY MONOPOLY. COVERAGE_KILL: 7 ASX analysts.

**QUEUEDs advancing to §4/§5:**
- STX.L (Shield Therapeutics, AIM): ACCRUFeR #1 branded oral iron US; +54% FY2025 revenue; QUEUED_HOT → §5 → **WATCH Grade C** (Q2/F2/R3/C2). REMS moat fabricated; polymorph-only patent; 5x dilution; AOP controlling at 3.0p; Viatris terms confidential. Asymmetry Gate FAIL (cond3: fat downside). Buy-zone ~3.0–4.0p. memos/STX.L-2026-07-20.md.
- DXRX.L (Diaceutics, AIM): Precision Medicine Implementation (PMI) platform connecting pharma to lab networks; ~£120M cap; 4-5 analysts (borderline). QUEUED ~6-7/12; next §4 financial baseline.
- SEDANA.ST (Sedana Medical, Nasdaq Stockholm): AnaConDa inhaler device for volatile ICU sedation (isoflurane/sevoflurane); sole approved device for prolonged ICU volatile anaesthesia; ~$75M cap; 3 analysts. QUEUED ~7/12; next §4 financial baseline.
- MDP.TO (Medexus Pharmaceuticals, TSX): Gleolan (5-ALA fluorescence-guided glioma surgery; sole FDA/EMA approved); IXINITY, Rupall; ~C$120M cap; 3-4 analysts. QUEUED ~6/12; next §4 financial baseline. Moat concentration check needed (Gleolan vs. other drugs).

**IHC.L reclassification:** IHC.L (Inspiration Healthcare Group, AIM) reclassified from NO_MOAT_KILL to PARK. Prior kill description was applied without reading primary AIM filing; 0.4x P/S discount warrants investigation before full kill; SLE neonatal ICU ventilator specialist position may differentiate from general neonatal respiratory competitors (Dräger, F&P, Intersurgical). CAP_KILL concurrent at ~£20M. Revived to PARK pending primary filing read.

**Quality Bench addition:** RX.V (BioSyent Inc, TSX-V): Canadian specialty pharma; 62-quarter consecutive profit streak; 21% net income margin; net cash; high quality (Q≥4) but Asymmetry Gate fails at current price (at/near fair value; no discrete catalyst). Added to WATCHLIST Quality Bench. Buy-zone: ~C$5-6 (~30%+ cap correction).

**Notable PARK from §4 baseline (run #47b):**
- EAH.L (ECO Animal Health Group, AIM): Aivlosin/tylvalosin veterinary antibiotic; REGULATORY moat genuine but generic tylvalosin erosion is active (off-patent API; China generic entrants); EV/EBITDA ~4x structurally discounted not mispriced; NI margin 4.2% thin; Asymmetry Gate 4/4 fail. PARK 5/12. REVISIT IF generic erosion arrested ≥2 qtrs + cap below £40M. financials/EAH.md.

**Deferred queue update (run #47b):** 6853.T Kyowa Electronic Instruments resolved PARK Grade D (FCF negative; P/E 22.8x premium; Asymmetry Gate 4/4 fail; memo memos/6853.T-2026-07-20.md). Active deferred queue now: 6858.T only.

**Sector 19 status: 2 passes complete. Deferred queue: 6858.T Ono Sokki 6/12 (⚑non-EN yuho required before §5). Next sector rotation: Sector 10 (2nd pass, UK/European wholesale distributors).**

---

## Why this matters
- **Measurable coverage** — we can state "we've reviewed X% of the worthwhile US universe," not "we searched a lot."
- **No wasted re-looks** — SEEN keyed by CIK/ticker; the ranked worklist is marched once.
- **Best-first** — even if we never hit 100%, we've covered the highest-quality names first.
- **Spend shifts to the top** — deterministic enumeration/pre-screen is nearly free; LLM tokens go only to names that already pass the hard numeric gates.
