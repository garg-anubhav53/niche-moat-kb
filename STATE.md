# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 3
Universe size: 6 (HURC CANDIDATE, OFLX QUEUED, CPSH PARK, PDEX QUEUED, ANIK QUEUED, KRMD PARK)
WATCH count: 0
QUEUED_HOT pending deep-dive: 0

## Deferred Deep-Dive Queue
(QUEUED_HOT names awaiting a deep-dive when a future run has budget — highest promise score first)

| Ticker | Promise Score | Sector | Added |
|--------|---------------|--------|-------|
| ANIK | 9/12 | Medical Dx & Consumables (HA platform) | 2026-07-16 — promote to QUEUED_HOT if Hyalofast resubmission accepted (PDUFA date set) |

## Run Log
(UTC · sector · #names_processed · #killed · #queued · #deep-dived · top promise score · push status)
Throughput target: ≥20 names processed per run.

| UTC | Sector | Processed | Killed | Queued | Deep | Top Score | Push |
|-----|--------|-----------|--------|--------|------|-----------|------|
| 2026-07-15T23:52 | 3-Industrial Precision | 4 (HURC,OFLX,NNBR,LIQT) | 1 (NNBR INTEGRITY) | 2 (HURC HOT, OFLX Q) | 0 | 10/12 HURC | OK |
| 2026-07-16T00:00 | 0-Specialty Chem/Materials | 30+ (both sessions: AMVAC,AXTI,NTIC,IPI,FTK,CMT,TREC,FSI,ECVT,ASIX,GSM,APDN,SND,UFPT,ULBI,SOLS,CCF,IOSP,HAYN,MTRN,BCPC,APFC,KOPN,AP,HCCI,MYE,SLCA,ROG,CBT,CPSH,GURE,NVEC,HDSN,SRDX,NANX,LWLG,LXU,SYNL,KOP,ACNT,UUUU,PLL,GEVO,AMSC,PPTA,KRO,SLI) | ~46 kills/parks (2 SECTOR, 10 NO_MOAT, 12 CAP, 6 COVERAGE, 7 INTEGRITY, 8 NO_CATALYST, 1 PARK/PASS) | 0 new | 1 deferred (HURC → WATCH 9/12 cautious; memo written) | 9/12 HURC (WATCH) | PENDING |
| 2026-07-16T01:17 | 1-Medical Dx & Consumables | 36 (MDXH,KRMD,IRIX,DRAD,PDEX,SMLR,MLAB,HBIO,QTRX,MASS,ICAD,ANIK,AXDX,OSUR,LNTH,NURO,BASS,INFU,ATRI,CATX,ECOR,RCEL,SENS,POAI,ORGO,TCMD,RMTI,VREX,TELA,MDXG,CLPT,NYXH,BVS,VNDA,HSKA,HROW) | 33 killed (6 NO_MOAT, 9 CAP, 9 COVERAGE, 3 INTEGRITY, 6 NO_CATALYST) | 2 new QUEUED: ANIK 9/12, PDEX 7/12; 1 PARK: KRMD 4/12 | 0 (no QUEUED_HOT; deferred queue was empty) | 9/12 ANIK | PENDING |
