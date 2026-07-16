# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 4
Universe size: 8 (HURC CANDIDATE, ANIK CANDIDATE, OFLX QUEUED, KMK QUEUED, PDEX QUEUED, CPSH PARK, KRMD PARK)
WATCH count: 0
QUEUED_HOT pending deep-dive: 0

## Deferred Deep-Dive Queue
(QUEUED_HOT names awaiting a deep-dive when a future run has budget — highest promise score first)

| Ticker | Promise Score | Sector | Added |
|--------|---------------|--------|-------|
| OFLX | 8/12 | Industrial Precision (CSST gas piping) | 2026-07-15 — deep-dive when new construction cycle catalyst identified |
| KMK | 8/12 | Nuclear & Radiological Civil (CZT detection) | 2026-07-16 — deep-dive when CBRN contract win or FY results catalyst confirmed |

## Run Log
(UTC · sector · #names_processed · #killed · #queued · #deep-dived · top promise score · push status)
Throughput target: ≥20 names processed per run.

| UTC | Sector | Processed | Killed | Queued | Deep | Top Score | Push |
|-----|--------|-----------|--------|--------|------|-----------|------|
| 2026-07-15T23:52 | 3-Industrial Precision | 4 (HURC,OFLX,NNBR,LIQT) | 1 (NNBR INTEGRITY) | 2 (HURC HOT, OFLX Q) | 0 | 10/12 HURC | OK |
| 2026-07-16T00:00 | 0-Specialty Chem/Materials | 30+ (both sessions: AMVAC,AXTI,NTIC,IPI,FTK,CMT,TREC,FSI,ECVT,ASIX,GSM,APDN,SND,UFPT,ULBI,SOLS,CCF,IOSP,HAYN,MTRN,BCPC,APFC,KOPN,AP,HCCI,MYE,SLCA,ROG,CBT,CPSH,GURE,NVEC,HDSN,SRDX,NANX,LWLG,LXU,SYNL,KOP,ACNT,UUUU,PLL,GEVO,AMSC,PPTA,KRO,SLI) | ~46 kills/parks (2 SECTOR, 10 NO_MOAT, 12 CAP, 6 COVERAGE, 7 INTEGRITY, 8 NO_CATALYST, 1 PARK/PASS) | 0 new | 1 deferred (HURC → WATCH 9/12 cautious; memo written) | 9/12 HURC (WATCH) | PENDING |
| 2026-07-16T01:17 | 1-Medical Dx & Consumables | 36 (MDXH,KRMD,IRIX,DRAD,PDEX,SMLR,MLAB,HBIO,QTRX,MASS,ICAD,ANIK,AXDX,OSUR,LNTH,NURO,BASS,INFU,ATRI,CATX,ECOR,RCEL,SENS,POAI,ORGO,TCMD,RMTI,VREX,TELA,MDXG,CLPT,NYXH,BVS,VNDA,HSKA,HROW) | 33 killed (6 NO_MOAT, 9 CAP, 9 COVERAGE, 3 INTEGRITY, 6 NO_CATALYST) | 2 new QUEUED: ANIK 9/12, PDEX 7/12; 1 PARK: KRMD 4/12 | 0 (no QUEUED_HOT; deferred queue was empty) | 9/12 ANIK | PENDING |
| 2026-07-16T02:17 | 2-Nuclear & Radiological Civil | 24 (ASPI,LEU,NNE,LTBR,EU,URG,UROY,ARAY,GVP,OKLO,SMR,UEC,DNN,NXE,ATNM,WUC,GLATF,MIR,BWXT,PESI,XE,BOSSF,PALAF,KMK) | 23 killed (12 CAP, 1 SECTOR, 5 INTEGRITY, 1 NO_MOAT, 3 NO_CATALYST, 1 COVERAGE) | 1 new QUEUED: KMK 8/12 | 1 deferred deep-dive (ANIK → CANDIDATE 10/12; memo memos/ANIK-2026-07-16.md; catalyst impaired by Phase III endpoint miss + FDA deficiency letter) | 10/12 ANIK (downgraded from QUEUED HOT to CANDIDATE; catalyst=0) | PENDING |
