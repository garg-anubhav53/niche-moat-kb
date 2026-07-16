# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 2
Universe size: 3 (HURC WATCH cautious, OFLX QUEUED, CPSH PARK)
WATCH count: 1 (HURC — cautious, Sept 4 2026 catalyst)
QUEUED_HOT pending deep-dive: 0

## Deferred Deep-Dive Queue
(QUEUED_HOT names awaiting a deep-dive when a future run has budget — highest promise score first)

| Ticker | Promise Score | Sector | Added |
|--------|---------------|--------|-------|
| *(empty — HURC deep-dived 2026-07-16, promoted to WATCH; no new QUEUED_HOT this run)* | | | |

## Run Log
(UTC · sector · #names_processed · #killed · #queued · #deep-dived · top promise score · push status)
Throughput target: ≥20 names processed per run.

| UTC | Sector | Processed | Killed | Queued | Deep | Top Score | Push |
|-----|--------|-----------|--------|--------|------|-----------|------|
| 2026-07-15T23:52 | 3-Industrial Precision | 4 (HURC,OFLX,NNBR,LIQT) | 1 (NNBR INTEGRITY) | 2 (HURC HOT, OFLX Q) | 0 | 10/12 HURC | OK |
| 2026-07-16T00:00 | 0-Specialty Chem/Materials | 30+ (both sessions: AMVAC,AXTI,NTIC,IPI,FTK,CMT,TREC,FSI,ECVT,ASIX,GSM,APDN,SND,UFPT,ULBI,SOLS,CCF,IOSP,HAYN,MTRN,BCPC,APFC,KOPN,AP,HCCI,MYE,SLCA,ROG,CBT,CPSH,GURE,NVEC,HDSN,SRDX,NANX,LWLG,LXU,SYNL,KOP,ACNT,UUUU,PLL,GEVO,AMSC,PPTA,KRO,SLI) | ~46 kills/parks (2 SECTOR, 10 NO_MOAT, 12 CAP, 6 COVERAGE, 7 INTEGRITY, 8 NO_CATALYST, 1 PARK/PASS) | 0 new | 1 deferred (HURC → WATCH 9/12 cautious; memo written) | 9/12 HURC (WATCH) | PENDING |
