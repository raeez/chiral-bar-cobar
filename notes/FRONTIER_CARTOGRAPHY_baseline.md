# FRONTIER CARTOGRAPHY — Orientation Baseline
# Date: 2026-03-14
# Commit: 8e5ccd7 (main)
# Session: v33

## Volume I: Chiral Bar-Cobar Monograph

| Metric | Value |
|--------|-------|
| Pages | 1803 |
| Build status | Clean (0 undef cit, 0 undef ref, 0 multiply-defined, 0 overfull, 1 underfull) |
| Source lines | 127,671 |
| Active .tex files | 61 |
| Total .tex files | 70 |

### Claim Census (generate_metadata.py — authoritative)

| Status | Count |
|--------|-------|
| ProvedHere | 1101 |
| ProvedElsewhere | 318 |
| Conjectured | 152 |
| Heuristic | 24 |
| Open | 0 |
| **Total** | **1595** |

### Claim Census (grep cross-check — raw string occurrences, higher due to inline mentions)

| Status | Grep Count | Structured Count | Delta |
|--------|------------|------------------|-------|
| ProvedHere | 1140 | 1101 | +39 |
| ProvedElsewhere | 348 | 318 | +30 |
| Conjectured | 185 | 152 | +33 |
| Heuristic | 27 | 24 | +3 |
| Open | 0 | 0 | 0 |
| **Total** | **1700** | **1595** | **+105 (6.6%)** |

Delta is expected: grep counts inline mentions in proofs/remarks, not just theorem-env tags.

### Labels

| Metric | Count |
|--------|-------|
| Total labels | 4515 |

### Tests

| Metric | Value |
|--------|-------|
| Fast tests | ~5,973-6,005 (pending recount) |
| Slow tests (deselected) | ~737 |

## Volume II: A-infinity Chiral Hochschild Cohomology

| Metric | Value |
|--------|-------|
| Pages | 173 |
| Build status | Clean |
| Tests | 133 |

## Cross-Volume Bridges

5 bridges to check (G12):
1. Bar-cobar: Vol II ↔ Vol I Theorem A
2. Hochschild: Vol II ↔ Vol I Theorem H
3. DK/Yang-Baxter: Vol II ↔ Vol I DK-0
4. W-algebras: Vol II ↔ Vol I MC5
5. Physics functor: Vol II ↔ Vol I framework

## Phase 1 Quick Checks (already done)

| Gap Type | Automated Result |
|----------|-----------------|
| G6 (Display-Mismatch) | **0 findings** — all cross-type patterns clean |
| G10 (Phantom-Ref) | **0 findings** — build log fully clean |
| Build warnings | 0 undefined references, 0 undefined citations, 0 multiply-defined labels |

## Agents Launched (Phase 1)

- G1 (Untagged theorem envs): running
- G4 (Label/env prefix mismatch): running
- G5 (Unlabeled theorem envs): running
- G6+G10 (Display mismatch + phantom refs — deep agent): running
- G12 (Cross-volume bridge audit): running
