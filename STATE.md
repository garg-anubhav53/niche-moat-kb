# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 1
Universe size: 2
WATCH count: 0
QUEUED_HOT pending deep-dive: 1

## Deferred Deep-Dive Queue
(QUEUED_HOT names awaiting a deep-dive when a future run has budget — highest promise score first)

| Ticker | Promise Score | Sector | Added |
|--------|---------------|--------|-------|
| HURC | 10/12 (scout, unverified — NEEDS deep-dive before WATCH) | 3-Industrial Precision | 2026-07-15 |

## Run Log
(UTC · sector · #names_processed · #killed · #queued · #deep-dived · top promise score · push status)
Throughput target: ≥20 names processed per run.

| UTC | Sector | Processed | Killed | Queued | Deep | Top Score | Push |
|-----|--------|-----------|--------|--------|------|-----------|------|
| 2026-07-15T23:52 | 3-Industrial Precision | 4 (HURC,OFLX,NNBR,LIQT) | 1 (NNBR INTEGRITY) | 2 (HURC HOT, OFLX Q) | 0 | 10/12 HURC | OK |
