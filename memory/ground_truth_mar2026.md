# GROUND TRUTH — Verified March 6, 2026
# Source: full codebase audit (grep, make, pytest, agent cross-checks)
# DO NOT RE-AUDIT. This file IS the audit. Verified to the line.

## Census (exact)
| Status | Count |
|--------|-------|
| ProvedHere | 698 |
| ProvedElsewhere | 334 |
| Conjectured | 115 |
| Heuristic | 19 |
| Open | 0 |
| **Total** | **1166** |

## Build
- Pages: 1310 (1-pass clean), ~1370 estimated 6-pass
- LaTeX errors: 0
- Undefined citations: 2 (`LurieHA` on pages 91-92)
- Undefined refs: 0 on clean build (161 forward-refs resolve on multi-pass)
- Overfull hbox: 81
- Proof sketches: 2 (deformation_theory:957, holomorphic_topological:77 — both correctly scoped)
- Bibliography: 260 \bibitem entries (CLAUDE.md says 289 — overcounted)

## Tests
- 1187 passing (`cd compute && .venv/bin/python -m pytest tests/ -q`)

## Audit 5 Status
- 4 CRITICAL: ALL FIXED (C1-C4)
- 28 HIGH: 20 FIXED, 6 STILL PRESENT, 1 PARTIAL (see fix_queue.md)
- 17 MEDIUM: M1 mostly fixed (1 remaining), M2 fixed, M3 ~50 PE without cites, M4 still present

## What Has NEVER Been Done (targeted in v6/v7/DEEP_SESSION/DEEP_SYNTHESIS, never reached)
1. Module computation: Phi on non-vacuum Verma M(lambda) for sl2
2. Module computation: Ext^1 at fractional level via bar
3. Discriminant spectral interpretation: Delta = det(1-xT_rec) — PARTIALLY DONE (conj:discriminant-spectral formulated, Schur obstruction for T_KS identified, transfer matrix picture verified in Python)
4. Genus-graded Verma dimensions (genus-1 layer)
5. Motzkin combinatorial model for Virasoro bar
6. HC spectral for Master Table (A15)
7. Pentagon m4 for Virasoro (A18)
8. ~~BRST=bar chain map (Programme VI-a)~~ **DONE** (thm:brst-bar-genus0)
9. Langlands H^2 (Programme I)
10. sl3 H^4 / W3 H^5 verification (Programme IX)

## The Pattern That Kills Sessions
Orient (15-20%) -> Audit fixes (40-60%) -> CRASH before math depth
FIX: Skip orientation (this file). Warmup fixes max 30 min. Then DEPTH.

## Known Pitfalls (verified, not speculative)
- Bar d_bracket^2 != 0 (all 2048 signs). Use PBW SS, not matrix rank.
- H! = Sym^ch(V*), NOT self-dual. F! = beta-gamma, NOT Heisenberg.
- FF involution: k <-> -k-2h^v (NOT -k-h^v).
- Curved A-inf: m1^2(a) = [m0, a] with MINUS sign.
- P-inf-chiral != Coisson. Different quantization levels.
- Python: use .venv/bin/python, NOT system python.
- Build watcher may spawn competing pdflatex. Kill before manual builds.
