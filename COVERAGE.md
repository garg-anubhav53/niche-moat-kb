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

## Sector 10 (Value-added/sole-line distribution) — Pass 2 Coverage Notes (run #48, 2026-07-20)

**UK AIM + European exchanges geo lens:** ~38 names processed; 0 new QUEUED. Structural thinness confirmed as a durable characteristic of the sector, not a data gap.

**Why UK/European sole-line distribution is structurally thin for this screen:**
- **PE consolidation wave (2015-2023):** most quality micro-cap distributors with genuine niche exclusivity have been acquired by private equity (Bunzl, DCC, Diploma, Wolseley successors now large-cap; numerous former AIM distributors delisted/privatised). What remains public is either commodity-ish distribution or over-covered mid-cap.
- **Dominant moated names are private:** RS Group (formerly Electrocomponents), Brammer/Rubix, Würth, Hagemeyer all private or >£1.5B. The genuine "sole-line specialist with contractual switching costs" names tend to go private quickly.
- **AIM small-cap distributors reviewed:** ~20 UK AIM names at £20-300M cap; near-universal result: thin margins (3-8% EBIT), commodity product ranges, no contractual lock-in, multi-supplier switching easy. No QUEUED names survived.
- **European exchange names reviewed:** ~18 names on Xetra, Euronext, Nasdaq Stockholm in cap range; same structural result — food/industrial distributors with GM 15-30%, regional competitors, no moat claim.

**Net result: 0 new QUEUED from ~38 names; 1st consecutive 0-new pass for Sector 10 2nd pass.**

**Sector 10 status:** ACTIVE (not yet EXHAUSTED — ROUTINE.md requires 2 consecutive 0-new passes). Next pass should try Nordic specialist distributors (Stockholm/Oslo micro-cap) or Australian ASX distribution niche if any moated names remain unlisted.

---

## Sector 12 (Life-science tools & lab consumables) — Pass 3 Coverage Notes (run #49, 2026-07-20)

**Nordic / Canada / Australia geo lens:** ~20-25 names processed; 0 new QUEUED. 1st consecutive 0-new pass for Sector 12.

**Why Nordic/Canada/Australia life-sci tools is structurally thin at this cap range:**
- **Nordic:** Quality names are either (a) private/subsidiary of large-cap (Gyros Protein Technologies → Hamilton subsidiary; DIATEC Monoclonal → private; Nordic Bioscience → private), (b) development-stage INTEGRITY_KILL (pre-revenue biotech making up bulk of Nasdaq Stockholm life-sci listings), or (c) over-capped (Biotage AB ~SEK 7B; CELLINK/BICO ~SEK 5B). Names that survive Nordic screens often have thin revenues or are essentially lab services (not platform/consumable with moat). Israel explicitly excluded (JURISDICTION_KILL — hard rule applies to all Nordic-adjacent Israeli life-sci tools, which form a large part of the "Nordic" biotech pool, e.g., many dual-listed names).
- **Canada:** TSX/TSX-V life-sci tool names are sparse. Most quality Canadian life-sci tools either (a) cross-listed on Nasdaq/NYSE (already in SEEN set via US pass), (b) development-stage (no revenue), or (c) service-based CRO/CMO (no platform moat).
- **Australia:** ASX life-sci tool names at A$20-300M are predominantly development-stage (pre-clinical or Phase I/II therapeutics that happen to have "tools" in marketing materials) → INTEGRITY_KILL. Genuine ASX life-sci equipment/consumable manufacturers that might have moats are either private (Hologic ANZ subsidiary, BD ANZ subsidiary) or over-capped (CSL at A$130B).
- **Israel excluded (JURISDICTION_KILL):** Numerous Israeli life-sci tools companies (Given Imaging, Orbotech successors, many Nasdaq dual-listed diagnostics names) are excluded per JURISDICTION_KILL hard rule regardless of quality.

**Net result: 0 new QUEUED from ~20-25 names; 1st consecutive 0-new pass.**

**Sector 12 status:** ACTIVE (not yet EXHAUSTED — ROUTINE.md requires 2 consecutive 0-new passes). 1 pass to go before EXHAUSTED. Next pass options: US micro-cap life-sci tools (systematic SEC XBRL screen) or Japanese secondary OTC life-sci tool names (EDINET when proxy access restored). Do not attempt another Nordic/Canada/Australia pass — structural thinness now well-established.

**Deferred queue note (run #49):** DXRX.L (Diaceutics, AIM — Sector 19 crossover, not pure Sector 12) was the Sector 12/19 §5 deep-dive completed this run. Sector 12's own candidates (TSTL.L, 6823.T Rion) were previously resolved (TSTL.L → COVERAGE_KILL run #44; 6823.T → CANDIDATE Grade B run #40).

---

## Taiwan GEO OVERRIDE — Run #50 (2026-07-21)

**Screen:** `tools/screen_tw.py --min-gm 45 --min-om 12` → **TWSE OpenAPI proxy-blocked (403 Forbidden)**; fell back to §2B web-search scout for all Taiwan names. All data tagged ~.

**Coverage:** ~17 Taiwan names processed across TWSE (main board) and TPEX (OTC board), covering precision instruments (Sector 18 geo lens), semiconductor testing services, medical devices, specialty chemicals, and semiconductor equipment.

**Result: 0 new QUEUED. All names killed at §3 triage.**

### Kill summary (Taiwan run #50)

**No-Moat Kills (GM below 45% gate) — 7 names:**
- 8021.TW Topoint Technology — archery equipment OEM; GM ~27%; NO_MOAT_KILL
- 3289.TWO iST International — semiconductor testing services; GM 26.96%; NO_MOAT_KILL
- 8103.TW CviLux — electrical connectors; GM ~20%; NO_MOAT_KILL
- 3055.TW Spirox Medical — ENT devices; GM ~16%; NO_MOAT_KILL + CAP_SOFT concurrent
- 1733.TW Apex Biotech — OEM rapid diagnostic kits + glucose meters; GM ~28%; NO_MOAT_KILL
- 4746.TW Formosa Laboratories — API pharmaceutical intermediates CDMO; GM ~41.9%; NO_MOAT_KILL (below 45% gate)
- 3583.TW Scientech Electronics — semiconductor equipment agency + own-brand wet process equipment; GM ~30-32%; DUAL-KILL: NO_MOAT + CAP ($2.03B)

**Cap/Extended-Zone Kills — 5 names:**
- 4749.TWO Advanced Echem Materials — specialty semiconductor photoresists; cap ~$1.8B; CAP_KILL
- 7769.TW Hon. Precision — IC test handlers; cap well above $300M; CAP_SOFT_KILL
- 6146.TWO Sporton International — EMC/safety certification lab; cap ~$624M extended zone; declining revenue; CAP_SOFT_KILL
- 4736.TW TaiDoc Technology — OEM glucose meters/CGM; cap ~$377M extended zone; declining revenue; CAP_SOFT_KILL
- 5536.TWO Acter Group — fab EPC services; cap ~$4.7B + GM ~21% + revenue $1.3B; TRIPLE-KILL

**Coverage Kill — 1 name:**
- 4772.TWO Taiwan Speciality Chemicals Corporation — specialty semiconductor chemicals; ~5 analysts; COVERAGE_KILL

**Quality Kill — 1 name:**
- 6934.TWO HCmed Innovations Co. — vibrating mesh nebulizer CDMO; GM ~62% passes gate; cap ~$83M in zone; BUT pre-commercial losses (quality=0); $3-4M USD revenue (dev-stage); one-client concentration; QUALITY_KILL

**Triple-Kill — 2 names:**
- 6223.TWO MPI Corporation — probe cards; cap ~$18B + 11 analysts + revenue $418M; TRIPLE-KILL (cap + coverage + revenue)
- 5536.TWO Acter Group — (also counted above); TRIPLE-KILL (cap + no-moat + revenue)

### Notable near-misses
- **6223.TWO MPI Corporation:** Highest-quality Taiwan name encountered — probe cards 72% revenue, GM 53.8%, OP 28.5%. But cap ~$18B = 60x limit; 11 analysts. Would be high-priority QUEUED if cap corrects below $300M. Monitor for spinoff/restructuring.
- **6934.TWO HCmed:** Genuine niche CDMO moat structure (3 global players; FDA regulatory lock-in once device co-filed; multi-year CDMO relationships). Revisit if: (a) revenue reaches $20M+ USD, (b) net income positive, (c) second US client relationship confirmed.

### Deferred queue update (run #50)
- 6858.T Ono Sokki: **revised 6/12 → 8/12** with FY2026 guidance data (fwd P/E ~11x; net cash 31% of cap; orders > revenue; H1 FY2026 earnings July 29 2026 hard-dated). §5 STILL BLOCKED: (a) EDINET proxy-blocked; (b) GM unverified from primary filing. financials/6858.T.md written this run.

**Sector 18 status:** 2 passes complete. Taiwan geo lens EXHAUSTED (0 survivors from ~17 names). Next Sector 18 pass: European geo lens (German XTRA precision instruments / Swiss SIX) or Japan secondary names (post-EDINET access).

**GEO OVERRIDE cleared.** Next scheduled rotation: Sector 10 3rd pass (Nordic specialist distributors or ASX niche). Sector 15 now EXHAUSTED (2 consecutive 0-new passes).

---

## Sector 15 (Exchanges/data/niche financials) — Pass 3 Coverage Notes (run #51, 2026-07-21) → **EXHAUSTED**

**US geo lens:** ~20 names processed; 0 new QUEUED. 2nd consecutive 0-new pass → Sector 15 → **EXHAUSTED**.

**Why US exchanges/data/niche financials is structurally exhausted at $20-300M:**
- Exchange/clearing operators all large-cap ($7B+): CME, ICE, Cboe, Nasdaq, MarketAxess all massively above ceiling
- Specialty insurance (E&S/admitted) is extended zone: quality US E&S/specialty insurers (SKWD ~$1.5-2B, PLMR ~$2-3B, KNSL ~$6B, JRVR ~$400-600M, GBLI ~$500M, PRA ~$750M) are $400M+ extended zone or carry reserve quality concerns
- Financial data/analytics absorbed or private: S&P Global/MSCI/FactSet/Morningstar all >$10B; DFIN ~$1B coverage-heavy remaining
- Specialty financial services small-caps: RIAs/fund managers (SAMG, HNNA, GAMCO) have AUM-stickiness but floors are AUM-dependent not earnings-floor; secular passive/ETF pressure erodes pricing

**Net result: 0 new QUEUED; 2nd consecutive 0-new pass → SECTOR 15 EXHAUSTED.**
Best survivors: SAMG 5/12 PARK (Silvercrest UHNW RIA; moat real; fair-valued ~21x PE; AUM-dependent floor disqualifies); HNNA 4/12 PARK (Hennessy Advisors; weaker moat; thin AUM-dependent margins).

**REVIVE condition:** new geo lens required — Nordic/Scandinavian financial data niche (Oslo Bors/Nasdaq Stockholm micro-cap financial infrastructure) or ASX Australian securities infrastructure — before attempting another pass.

---

## Sector 10 (Value-added/sole-line distribution) — Pass 3 Coverage Notes (run #52, 2026-07-21) → **ACTIVE**

**Nordic specialist distributors + ASX niche geo lens:** ~17 names processed; 1 new QUEUED (ASX:XRF 9/12). Consecutive-0-new streak from 2nd pass BROKEN — Sector 10 remains **ACTIVE**.

**Names processed:**

**Cap Kills — 5 names (CAP_SOFT: $500M–$1.5B, limited asymmetry):**
- OEM-B.ST (OEM AB, Sweden) — Swedish industrial distributor; ~$1.1B USD cap; CAP_SOFT_KILL
- BIOG-B.ST (Biogaia, Sweden) — probiotic distributor/IP; ~$700M+ cap + >4 analysts; dual CAP_SOFT+COVERAGE_KILL
- MUSTI.HE (Musti Group, Finland) — Nordic pet products distributor; ~$760M USD cap; CAP_SOFT_KILL
- BERG-B.ST (Bergman & Beving, Sweden) — industrial specialist distributor; ~$735M USD cap + revenue ceiling; CAP_SOFT_KILL
- ASX:SNL (Supply Network Limited, Australia) — heavy truck parts distributor; ~$940M USD cap; CAP_SOFT_KILL

**Coverage Kill — 1 name:**
- ASX:NAN (Nanosonics, Australia) — medical device disinfection; 5-7 analysts; COVERAGE_KILL

**No-Moat Kills — 6 names:**
- ALLIGO-B.ST (Alligo AB, Sweden) — broadline workwear/industrial supplies distributor; 41% GM fails moat gate; NO_MOAT_KILL
- NORBT.OL (Norbit ASA, Norway) — hardware manufacturer not distributor; sector misclassification; NO_MOAT_KILL
- NZX:PGW (PGG Wrightson, NZ) — agricultural products distributor; 26% GM fails gate; NO_MOAT_KILL
- ASX:MXI (MaxiTRANS Industries, Australia) — trailer equipment distributor; 34% GM fails gate; NO_MOAT_KILL
- ASX:CYG (Coventry Group, Australia) — industrial distribution; GM uncertain; NO_MOAT_KILL
- VOLO.ST (Volati AB, Sweden) — industrial conglomerate; 30-35% GM fails specialty distributor gate; NO_MOAT_KILL

**Park — 1 name:**
- MMGR-B.ST (Momentum Group, Sweden) — technical industrial distribution; PARK 5/12 (quality borderline; margins thin; no hard-dated catalyst)

**Already Seen — 1 name:**
- ASX:DGL (DGL Group) — already killed in prior run; NOT duplicated

**Quality Bench Additions — 3 names (above buy-zone but durable moat; monitor for dip):**
- MEDI.OL (Medistim ASA, Norway) — patented TTFM cardiac surgery flow measurement; 80%+ global monopoly; 82% GM; above buy-zone (~$390-450M cap vs buy-zone ~$230-290M cap)
- SECARE.ST (Secare AB, Sweden) — ⚑non-EN conditional bench spot pending business/moat confirmation
- NZX:SKL (Skellerup Holdings, NZ) — diversified niche rubber/polymer OEM; quality real but ~NZD $720M cap extended zone

**1 new QUEUED:**
- **ASX:XRF (XRF Scientific Limited)** — 9/12; mining laboratory captive consumables (fusion discs, beads, platinum-ware for XRF/fire assay sample preparation); ~$207M USD cap; 48% GM; 1-2 analysts; English-language ASX filing; captive razor-blade model (lab equipment + consumable lock-in); §5 deep-dive deferred to run #53+

**Sector 10 status:** ACTIVE (3 passes complete; 1 new QUEUED this pass breaks consecutive-0-new streak). Next pass: Sector 10 4th pass with new geo lens (e.g. Southern Europe/DACH specialty distributors or Canadian TSX niche distributors).

---

## Deferred Queue Resolution + Sector 10 Pass 3 → ASX:XRF BENCH (run #53, 2026-07-21)

**ASX:XRF (XRF Scientific Limited)** — §5 deep-dive completed run #53. Outcome: **BENCH (WATCHLIST.md)**.
- Q4/F4/R1/C2 = 11/20. Asymmetry Gate FAIL 4/4.
- Moat: 10,000+ installed machines globally; platinum-group crucible consumable lock-in; process-certification switching cost (6-12 months re-validation); 50yr operating history. Q=4 is defensible.
- Financials confirmed: Revenue A$59.45M ✓; NPAT A$10.4M ✓; OCF A$10.1M ✓; net cash A$11.1M ✓ (ASX annual report). GM 48.43% ~ (aggregator).
- Price A$2.28 ~ = AT analyst consensus PT A$2.26-2.42 (1 analyst). No margin of safety.
- Buy-zone: A$1.40-1.65/sh (~A$200-235M cap). Promote to QUEUED_HOT on §7 REFLECT price check.
- memo: memos/XRF.AX-2026-07-21.md; financials: financials/XRF.AX.md.

---

## Sector 17 (Semiconductor & electronics supply chain) — Pass 3 Coverage Notes (run #53, 2026-07-21) — COMPLETE

**US micro-cap IC designers / semiconductor supply chain geo lens:** 32 names processed; 32 killed; **0 new QUEUED**.

**Structural finding:** The AI semiconductor supercycle 2025–2026 has pushed the vast majority of US-listed semiconductor supply chain companies above $1.5B. SIZE_KILL dominated (24 of 32). The $20–300M zone yields only ~6 genuine candidates (CVV, GSIT, INTT, MX, SVCO, RELL) after all gates — these require §3-§4 diligence in a future US semiconductor deep-dive pass.

**Complete kill table (32 names):**

| Ticker | Company | Cap (July 2026) | Kill Reason |
|--------|---------|----------------|-------------|
| CRDO | Credo Technology Group | ~$39.5B | SIZE_KILL |
| ALAB | Astera Labs | ~$10–40B | SIZE_KILL |
| MTSI | MACOM Technology | ~$19–29B | SIZE_KILL |
| VICR | Vicor Corporation | ~$12.9B | SIZE_KILL (+385%/1yr) |
| RMBS | Rambus Inc | ~$10B | SIZE_KILL |
| SMTC | Semtech Corporation | ~$11.64–14.59B | SIZE_KILL |
| MXL | MaxLinear Inc | ~$6.66–8.27B | SIZE_KILL |
| SIMO | Silicon Motion Technology | ~$3.54B | SIZE_KILL |
| PI | Impinj Inc | ~$4.81B | SIZE_KILL |
| VECO | Veeco Instruments | ~$4.2–4.86B | SIZE_KILL + M&A_KILL (being acquired by ACLS) |
| ACLS | Axcelis Technologies | ~$2.93–3.99B | SIZE_KILL |
| POWI | Power Integrations | ~$3.93–4.85B | SIZE_KILL |
| ACMR | ACM Research | ~$4.2–5.8B | SIZE_KILL + JURISDICTION concern (China-centric) |
| UCTT | Ultra Clean Holdings | ~$2.63–5.4B | SIZE_KILL |
| ICHR | Ichor Holdings | ~$3.2–3.9B | SIZE_KILL |
| AEHR | Aehr Test Systems | ~$2.2–2.76B | SIZE_KILL |
| NVTS | Navitas Semiconductor | ~$1.89–2.79B | SIZE_KILL |
| AXTI | AXT Inc | ~$2.0B | SIZE_KILL |
| ROG | Rogers Corporation | ~$2.4–2.9B | SIZE_KILL |
| KLIC | Kulicke & Soffa | ~$3.65–4.59B | SIZE_KILL |
| PLAB | Photronics | ~$2.65B | SIZE_KILL |
| COHU | Cohu Inc | ~$2.4–3.3B | SIZE_KILL |
| FORM | FormFactor | ~$3.5B+ | SIZE_KILL |
| PDFS | PDF Solutions | ~$2.14B | SIZE_KILL |
| BELFB | Bel Fuse Inc | ~$2.82B | SIZE_KILL |
| FEIM | Frequency Electronics | ~$642M | SECTOR_KILL (defense/space primary) |
| ULBI | Ultralife Corp | ~$109M | SECTOR_KILL (military primary) |
| PRKR | ParkerVision | ~$32M | SECTOR_KILL (patent assertion entity; no products) |
| PKE | Park Electrochemical | ~$423–588M | CAP_SOFT_KILL (extended zone) |
| LEDS | SemiLEDs | ~$12.8M | CAP_SOFT_KILL (below $20M minimum) |
| MRAM | Everspin Technologies | ~$344–700M | PRICE_KILL (+285%/1yr) |
| ASYS | Amtech Systems | ~$385M | PRICE_KILL (+430-572%/1yr) |

**Non-kills flagged for next US semiconductor pass (§3-§4 diligence required before QUEUED):**
- RELL (~$241-252M): Richardson Electronics — potential sole-source in plasma etch RF generator power tubes; SiC distribution JV; if verified, strong QUEUED candidate
- NVEC (~$444-474M): NVE Corporation — spintronic sensors + IsoLoop galvanic isolators; ~70% GM; proprietary IP; extended zone borderline
- SVCO (~$110-390M): Silvaco Group — TCAD process simulation EDA software; IPO 2024; high switching-cost tools for fabs/IDMs; cap range needs pinning
- GSIT (~$96-220M): GSI Technology — SRAM + Gemini APU (in-memory AI); 129 patents; but wide cap range and R&D-stage AI chip uncertain
- INTT (~$131M): inTEST Corporation — multi-segment semiconductor test/thermal/environmental; $53.9M backlog; Russell 2000 inclusion June 2026

**Sector 17 status:** ACTIVE (3 passes complete: pass 1 Korea/Taiwan, pass 2 European, pass 3 US micro-cap); next: 4th pass Japan secondary OEMs or US-listed non-killed names §3-§4 diligence. Pattern: zero new QUEUED from pass 3 (structural AI re-rating), 1 QUEUED (CML.L) from pass 2.

---

## Why this matters
- **Measurable coverage** — we can state "we've reviewed X% of the worthwhile US universe," not "we searched a lot."
- **No wasted re-looks** — SEEN keyed by CIK/ticker; the ranked worklist is marched once.
- **Best-first** — even if we never hit 100%, we've covered the highest-quality names first.
- **Spend shifts to the top** — deterministic enumeration/pre-screen is nearly free; LLM tokens go only to names that already pass the hard numeric gates.
