# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 2
Universe size: 2
WATCH count: 1 (HURC — conditional)
QUEUED_HOT pending deep-dive: 0

## Deferred Deep-Dive Queue
(QUEUED_HOT names awaiting a deep-dive when a future run has budget — highest promise score first)

| Ticker | Promise Score | Sector | Added |
|--------|---------------|--------|-------|
| *(empty — HURC deep-dived 2026-07-16, promoted to WATCH)* | | | |

## Run Log
(UTC · sector · #names_processed · #killed · #queued · #deep-dived · top promise score · push status)
Throughput target: ≥20 names processed per run.

| UTC | Sector | Processed | Killed | Queued | Deep | Top Score | Push |
|-----|--------|-----------|--------|--------|------|-----------|------|
| 2026-07-15T23:52 | 3-Industrial Precision | 4 (HURC,OFLX,NNBR,LIQT) | 1 (NNBR INTEGRITY) | 2 (HURC HOT, OFLX Q) | 0 | 10/12 HURC | OK |
| 2026-07-16T00:00 | 0-Specialty Chem/Materials | 30 (AMVAC,AXTI,NTIC,IPI,FTK,CMT,TREC,FSI,ECVT,ASIX,GSM,APDN,SND,UFPT,ULBI,SOLS,CCF,IOSP,HAYN,MTRN,BCPC,APFC,KOPN,AP,HCCI,MYE,SLCA,ROG,CBT,CPSH) | 30 (3 SECTOR, 7 NO_MOAT, 10 CAP, 1 COVERAGE, 2 INTEGRITY, 7 NO_CATALYST) | 0 new | 1 deferred (HURC → WATCH) | 0 new survivors; HURC confirmed WATCH | PENDING |
