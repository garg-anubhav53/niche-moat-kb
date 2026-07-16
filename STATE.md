# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 1
Universe size: 2
WATCH count: 1
QUEUED_HOT pending deep-dive: 0

## Deferred Deep-Dive Queue
(QUEUED_HOT names awaiting a deep-dive when a future run has budget — highest promise score first)

| Ticker | Promise Score | Sector | Added |
|--------|---------------|--------|-------|
| | | | |

## Run Log
(UTC · sector · #found · #killed · #queued · top promise score · push status)

| UTC | Sector | Found | Killed | Queued | Top Score | Push |
|-----|--------|-------|--------|--------|-----------|------|
| — | — | — | — | — | — | init |
| 2026-07-15T23:xx | 3-Industrial Precision | 4 raw (HURC,OFLX,NNBR,LIQT) | 1 INTEGRITY_KILL (NNBR) | 2 (HURC WATCH, OFLX QUEUED) | 10/12 HURC | PENDING |
