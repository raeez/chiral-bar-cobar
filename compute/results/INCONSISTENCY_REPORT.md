# Bar Complex Dimension Report — RESOLVED

## Resolution

The apparent inconsistency between examples_summary.tex and kac_moody_framework.tex is **resolved**: they report different quantities.

- **Master Table** (examples_summary.tex, Table 2): reports **bar COHOMOLOGY** dim H^n(B̄(A))
- **Proved formula** (kac_moody_framework.tex, rem:bar-dims-level-independent): gives **chain GROUP** dim B̄^n = dim(g)^n · (n-1)!

The table header explicitly says "Bar cohomology dimensions dim H^n(B̄(A))" (line 270), and Remark rem:bar-growth-koszul (line 317) notes: "the bar *chain-group* dimensions grow much faster; for Kac-Moody algebras dim B̄^n = (dim g)^n · (n-1)! is super-exponential."

## Corrected Values

### Chain Groups (PROVED, level-independent)

| Algebra | deg 1 | deg 2 | deg 3 | deg 4 | deg 5 |
|---------|-------|-------|-------|-------|-------|
| sl₂ | 3 | 9 | 54 | 486 | 5832 |
| sl₃ | 8 | 64 | 1024 | 24576 | — |
| G₂ | 14 | 196 | 5488 | — | — |
| B₂ | 10 | 100 | 2000 | — | — |

### Bar Cohomology (from Master Table)

| Algebra | deg 1 | deg 2 | deg 3 | deg 4 | deg 5 |
|---------|-------|-------|-------|-------|-------|
| sl₂ | 3 | 6 | 15 | 36 | 91 |
| sl₃ | 8 | 36 | 204 | — | — |
| Virasoro | 1 | 2 | 5 | 12 | 30 |
| W₃ | 2 | 5 | 16 | 52 | — |

## Files Updated

- `compute/lib/bar_complex.py`: KNOWN_BAR_DIMS now stores cohomology dims; KNOWN_CHAIN_GROUP_DIMS added for chain groups
- `compute/tests/test_bar_complex.py`: Tests updated to use correct values; chain group test added
- 85 tests passing
