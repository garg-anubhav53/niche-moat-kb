# STATE — Run Cursor & Log

Sector is chosen statelessly by (UTC hour mod 5) — see ROUTINE.md §1. This file is the append-only run log and counters.

## Counters
Total runs: 0
Universe size: 0
WATCH count: 0
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
