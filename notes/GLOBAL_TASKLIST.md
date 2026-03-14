# GLOBAL TASKLIST — Single Source of Truth
# Updated: 2026-03-14 (Session 8, continuation)
# Compiled from: HITLIST, SESSION8_FINDINGS, autonomous_state, PROGRAMMES, companion volume

## COMPLETED (this session)

| ID | Item | Evidence |
|----|------|----------|
| A.1 | Theorem A verification | PASS, all 6 deps |
| A.2 | Theorem B verification | PASS, all 6 deps |
| A.3 | Theorem C verification | PASS, 132 tests |
| A.4 | Theorem D verification | PASS, 428 tests |
| A.5 | MC1 audit | PASS, all 4 sub-theorems |
| A.6 | MC2 audit | PASS, all 7 deps |
| A.7 | DS-KD intertwining fix | 4 issues FIXED |
| A.0.8-12 | Convention audit | 4/6 PASS, 2 FIXED |
| B.2 | H^2_cyc(W_infinity) = 1 | ESTABLISHED + WRITTEN |
| B.7 | E_2 collapse promotion | lem:e2-collapse-higher-genus WRITTEN |
| C.4 | Formula verification sweep | ALL formulas verified |
| C.2.1 | Bar-side extraction tests | 14 tests, all passing |
| C.1.4 | c334^2 derivation | 23 tests, Gram+bootstrap characterization |
| D.3 | Concordance scalar saturation note | WRITTEN |

## ALSO COMPLETED (continuation)

| ID | Item | Evidence |
|----|------|----------|
| A.12 | Heisenberg frame | PASS + 2 issues FIXED (c+c' was 50->100, dim(g)->2dim(g)) |
| A.13 | KM examples | PASS |
| A.14 | W-algebra examples | PASS |
| A.17 | Configuration spaces | PASS, 56/56 tests |
| D.4 | "One verifies" audit | All 5 instances benign (followed by explicit verification) |
| D.5 | Multiply-defined label | FIXED (eq:modular-deformation-complex in concordance) |

## REMAINING — PRIORITY ORDER

### P0: IMMEDIATE (next session)

| ID | Item | File | Complexity | Depends |
|----|------|------|-----------|---------|
| A.0.1-7 | Sign/convention verification sweep (remaining items) | all chapters/*.tex | M | none |
| A.18 | Connections chapters verification | bv_brst.tex, feynman_*.tex | M | none |

### P1: HIGH

| ID | Item | File | Complexity | Depends |
|----|------|------|-----------|---------|
| A.15 | Yangian examples verification | yangians.tex (12632 lines, 153 PH) | XL | none |
| A.16 | Free field examples verification | free_fields.tex (4739 lines, 56 PH) | L | none |
| A.10 | Stage-4 packet analysis (40 props) | bar_cobar_construction.tex:6100-8700 | XL | none |
| A.11 | Stage-5 packet analysis (60 claims) | bar_cobar_construction.tex:8700-11100 | XL | none |
| B.1 | Construct H-level target W^{ht} | w_algebras_deep.tex (new) | XL | new math |
| B.3 | Bar-side residue extraction at stage 4 | compute/lib (new) | L | A.10 |
| B.4 | DS derivation of c444^2 | compute/lib (new) | L | C.1.4 |
| B.5 | Promote stage-4 conjectures | bar_cobar_construction.tex | L-XL | B.1 |
| C.1.1 | W_3 bar complex module | compute/lib/w3_bar_complex.py | M | none |
| C.1.5 | H^2_cyc computational verification | compute/lib (new) | M | none |

### P2: MEDIUM

| ID | Item | File | Complexity | Depends |
|----|------|------|-----------|---------|
| A.9 | M-level MC4 machinery verification | bar_cobar_construction.tex:5400-5900 | L | none |
| A.19 | Appendices verification | appendices/*.tex (15 files) | L | none |
| B.6 | Promote stage-5 conjectures | bar_cobar_construction.tex | XL | B.5 |
| B.8 | Yangian-W_infinity bridge | yangians.tex + w_algebras_deep.tex | XL | new math |
| B.9 | Periodicity verification | higher_genus.tex | M | none |
| C.1.2 | W_4 bar complex module | compute/lib (new) | L | C.1.1 |
| C.1.3 | W_5 OPE module | compute/lib (new) | XL | none |
| C.1.6 | Miura map module | compute/lib (new) | L | none |
| C.3 | Existing test audit (coverage matrix) | compute/tests/ | L | none |
| D.1 | Computation-first exposition rewrite | w_algebras_deep.tex | L | none |
| D.2 | Geometric realization (Slodowy slice) | w_algebras_deep.tex (new section) | XL | new math |
| D.4 | Complete all "one verifies" shortcuts | chapters/*.tex (6 instances) | S | none |
| D.5 | Cross-reference integrity audit | all .tex | M | none |
| D.6 | Bibliography verification | bibliography/references.tex | S | none |

### P3: FUTURE / COMPANION VOLUME

| ID | Item | File | Complexity | Depends |
|----|------|------|-----------|---------|
| CV.1 | Fix free multiplet H^0 contradiction | ainfinity companion | M | none |
| CV.2 | Implement LG cubic m_3, m_4 stubs | ainfinity companion | L | none |
| CV.3 | Formalize hypothesis (H4) | ainfinity companion | M | none |
| CV.4 | Consolidate PVA descent proofs | ainfinity companion | M | none |
| CV.5 | Fix broken cross-references | ainfinity companion | S | none |
| CV.6 | Fill empty appendix stubs | ainfinity companion | M | none |
| CV.7 | Prove Virasoro truncation at m_7 | ainfinity companion | M | none |
| PROG.I | Langlands programme (critical level) | new | XL | MC3/MC4 |
| PROG.II | KL programme (root of unity) | new | XL | MC3 |
| PROG.III | Fusion programme (monoidality) | new | XL | MC3 |
| PROG.IV | E_n programme (higher dimension) | new | XL | new math |
| PROG.VI-e | W-infinity/higher-spin programme | w_algebras_deep.tex | XL | MC4 |

## STATISTICS

- Total remaining items: ~39
- P0 (immediate): 2
- P1 (high): 10
- P2 (medium): 14
- P3 (future/companion): 12
- Completed this session: 20
- Core theorems verified: 6/6 (A, B, C, D, MC1, MC2)
- Example chapters verified: 4/4 (Heisenberg, KM, W-algebra, Config spaces)
- Issues found and fixed: 8 (6 from Session 8 + 2 from continuation)
- New tests created: 37 (14 bar-side + 23 c334)
- Working notes expanded: +280 lines of mathematical construction
