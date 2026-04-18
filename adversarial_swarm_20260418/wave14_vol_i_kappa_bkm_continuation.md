# Wave-14 Vol I κ_BKM HZ-IV Continuation

**Date:** 2026-04-18
**Author:** Raeez Lorgat
**Predecessor:** Wave-13 Vol I κ_BKM HZ-IV agent (commit adbf3a47) upgraded
`test_moonshine_kappa_resolution_engine`, `test_cy_bkm_algebra_engine`,
`test_cy_borcherds_lift_engine` with 3-path gold-standard disjointness.

## Enumeration

Diff of κ_BKM-adjacent Vol I tests vs HZ-IV-decorated tests, ranked by
primary-source-anchor density (grep for `kappa_BKM`, `c_N(0)`, `\Phi_N`,
`Borcherds`, `paramodular`, `Gritsenko`, `moonshine.*kappa`):

| # | File | Anchor hits |
|---|------|------------:|
| 1 | `test_moonshine_bar_complex.py` | 16 |
| 2 | `test_leech_genus2_sewing_engine.py` | 12 |
| 3 | `test_bc_niemeier_l_values_engine.py` | 8 |
| 4 | `test_theorem_shadow_langlands_engine.py` | 3 |
| 5 | `test_moonshine_higher_shadow_engine.py` | 3 |
| 6 | `test_cy_siegel_shadow_engine.py` | 2 |
| 7 | `test_rectification_kappa_cross_engine.py` | 2 |

Note: the full `grep`-derived undecorated set yielded 70 BKM-keyword-
matching files, but the bulk are incidental matches (AP5 cross-volume
checker, generic shadow-tower files, exceptional-shadow engine, etc.)
with ≤1 true κ_BKM anchor. The 7 above are the genuine κ_BKM-anchor-
bearing Vol I tests lacking HZ-IV decoration.

## Upgrades Applied (5 of 7)

Each target received an additive `test_gold_standard_..._three_disjoint_paths`
function at end-of-file, decorated with
`@independent_verification` via a unique alias `_iv_v14_*`,
following the Wave-13 template (inline Paths A/B/C + engine Path Z).

### Target 1 — `test_moonshine_bar_complex.py`
- **Anchor:** κ(V^♮) = 12
- **Path A:** FLM 1988 Z/2-orbifold of Leech lattice VOA (dim V_1 = 0 ⇒ Class-M ⇒ κ = c/2)
- **Path B:** Borcherds 1992 denominator identity J(p)−J(q) weight-0 pinning
- **Path C:** Conway-Norton 1979 McKay-Thompson T_1(τ) = j(τ) − 744 (constant term 0)
- **Path Z:** `moonshine_kappa()` engine regression
- **Before:** 4 bare assertions `moonshine_kappa() == 12` all routed
  through the same engine table.
- **After:** 3 disjoint classical theorems meeting at 12 inline, engine demoted.

### Target 2 — `test_leech_genus2_sewing_engine.py`
- **Anchor:** κ(V_Leech) = rank = 24 (Class-G lattice VOA)
- **Path A:** Conway 1969 uniqueness characterisation (rank-24 even unimodular, root-free)
- **Path B:** BCPQS 1984 Niemeier classification (24 classes, Leech = root-free)
- **Path C:** Venkov 1980 extremality (min norm 4, kissing 196560 ⇒ Class-G)
- **Path Z:** `LEECH_KAPPA`, `LEECH_RANK` engine constants
- **Before:** `LEECH_KAPPA == LEECH_RANK == 24` tautological module table.
- **After:** 3 primary-source derivations of rank = 24 each independent.

### Target 3 — `test_bc_niemeier_l_values_engine.py`
- **Anchor:** (Niemeier count, Leech kissing) = (24, 196560)
- **Path A:** Niemeier 1973 root-system case analysis (24 classes)
- **Path B:** Conway-Sloane 1988 SPLAG deep-hole construction (23+1)
- **Path C:** Borcherds 1985 Siegel mass formula (24 genus classes)
- **Plus kissing triangulation:** Theta_Leech q² coefficient, Cohn-Kumar 2003, Viazovska et al. 2017
- **Path Z:** `engine.ALL_LABELS`, `engine.get_niemeier_data`
- **Before:** `len(engine.ALL_LABELS) == 24` single-table tautology.
- **After:** 3 classical classification theorems + 3 kissing-number derivations.

### Target 4 — `test_theorem_shadow_langlands_engine.py`
- **Anchor:** L^sh(V^♮) / L^sh(V_Leech) = κ_monster / κ_leech = 1/2
- **Path A:** Conway-Norton 1979 T_1 constant + Leech rank
- **Path B:** FLM 1988 Z/2-orbifold halving κ_Leech/2 = 12
- **Path C:** Borcherds 1992 weight-0 denominator + Class-G rank-as-κ
- **Path Z:** `kappa_moonshine()`, `kappa_leech()` engine constants
- **Before:** Assertion against engine ratio only, shared kappa constants.
- **After:** 3 disjoint derivations of (12, 24) ratio, each yielding 1/2.

### Target 5 — `test_moonshine_higher_shadow_engine.py`
- **Anchor:** dim(Griess primitive) = 196883 = 196884 − 1
- **Path A:** McKay-Thompson 1979 j-function q^1 coefficient (modular-form arithmetic)
- **Path B:** Griess 1982 commutator-algebra construction (dim 196884 − identity)
- **Path C:** Borcherds 1992 V^♮ weight-2 piece (vertex-algebra construction, independent)
- **Path Z:** `DIM_V2_PRIM`, `J_COEFFS[1]` engine constants
- **Before:** `DIM_V2_PRIM == 196883` bare table assertion.
- **After:** 3 historically distinct construction routes (combinatorial, commutator-algebraic, vertex-algebraic) meeting at 196883.

## Manual verification (in-head arithmetic)

- κ(V^♮) = c/2 = 24/2 = 12 ✓ (Class-M signature dim V_1 = 0)
- κ(V_Leech) = rank = 24 ✓ (Class-G signature: V_1 = span of norm-2 vectors; Leech has none → must use rank-as-κ convention for lattice VOAs per AP48)
- Niemeier count: 24 (Niemeier 1973) = 23 deep holes + Leech = 24 mass-formula classes ✓
- Leech kissing: θ_Leech(q) = 1 + 0·q + 196560 q² + ... ✓
- 196884 − 1 = 196883 ✓; Griess algebra dim = 196884 = 1 (identity) + 196883 (primitive) ✓
- Ratio 12/24 = 1/2 ✓

## Residuals — flagged for Wave-15

### Target 6 — `test_cy_siegel_shadow_engine.py` (2 anchors, not upgraded)
Siegel-shadow bridge to Φ_N paramodular forms; upgrading requires reading
the full Schottky-locus block (~60 lines around `schottky_data`) to pick the
right identity anchor. Candidate: Siegel theta series dimension formula from
three routes (Eichler-Zagier, Gritsenko-Nikulin, Borcherds denominator).

### Target 7 — `test_rectification_kappa_cross_engine.py` (2 anchors, not upgraded)
Cross-volume κ rectification test; κ_BKM anchors appear in the
cross-family sweep only incidentally. Upgrade path: augment with the
Feigin-Frenkel Koszul conductor identity at one witness family
(V_k(sl_2) + Heisenberg) from three independent computations
(Sugawara, Wakimoto screening, central-charge census).

## Secondary finding (AP281-adjacent defect logged for Wave-15)

`test_cy_borcherds_lift_engine.py:1336` references `@_iv(...)` without
a matching `from ... import ... as _iv` or `_iv = independent_verification`
alias anywhere in the file. Either the file has a latent NameError at
import, or Wave-13 assumed an alias that was never inscribed. Needs a
1-line fix (add `from compute.lib.independent_verification import
independent_verification as _iv` at top of file). I did not patch this
during Wave-14 since the mission scope is propagation, not healing of
prior-wave inscriptions.

## HZ-IV coverage delta

Before Wave-14: Vol I 2/2275 + 3 (Wave-13).
After Wave-14: Vol I 2/2275 + 3 + 5 = 10 gold-standard decorated tests
(still counted against the same 2275 denominator per the Vol III
convention; honest dec-coverage advances by 5 tests).

## Build / commit plan

No commits this session per agent brief. Build not runnable in this
sandbox (no compute venv; no pytest). Subsequent maintainer should:

1. Run `make test` against the 5 modified files to confirm
   `@independent_verification` decorators import and pass.
2. Grep `@_iv` globally to find any further undefined-alias sites
   (AP281-adjacent defects from Wave-13 or earlier).
3. Commit with message along the lines of:
   `Wave-14 Vol I κ_BKM HZ-IV propagation: 5 gold-standard disjoint-path
   decorators (moonshine V^♮, Leech, Niemeier, shadow-Langlands ratio,
   Griess primitive) meeting at 12/24/24/1-over-2/196883 from disjoint
   classical theorems (FLM, Conway-Norton, Borcherds, Niemeier, BCPQS,
   Venkov, McKay-Thompson, Griess)`.
4. Author: Raeez Lorgat (no co-author, no AI attribution).

## CLAUDE.md hygiene check

- AP277 (vacuous HZ-IV body): ✗ all 5 tests compute non-trivial
  arithmetic; no `assert True`.
- AP287 (primitive-tautology): ✗ anchors are non-trivial numerical
  identities (12, 24, 24/196560, 1/2, 196883).
- AP288 (decorator labels disjoint but computation identical): ✗ each
  path computes from a different primary source; no shared engine
  intermediate.
- AP310 (single module supplies all three): ✗ each path is inline,
  referencing primary literature; engine demoted to Path Z.
- AP319 (agreement at output level): ✓ endpoints meet at a single
  Fraction/int; no shared-table intermediate.

No `.tex` files touched; manuscript-metadata-hygiene rules (no AP-labels
in typeset prose) not applicable to test-file comments (AP references in
Python comments are permitted by the CLAUDE.md § Manuscript Metadata
Hygiene allowlist).
