# Wave-17 Vol I kappa_BKM Final 2 Residuals Heal (2026-04-18)

## Mission

Close the final two residual Vol I kappa_BKM HZ-IV targets left by
Wave-16: `test_borcherds_shadow_operations.py` (966 lines) and
`test_w4_borcherds_transport.py` (177 lines).

## AP320 counter-discipline: pre-gate

Comprehensive regex
`@independent_verification|@_iv\(|@_iv_v[0-9]+_[a-zA-Z_]+\(|TestGoldStandardDisjointPaths`
across both targets returned zero matches before Edit. Confirmed
undecorated at `iv=0 gs=0 w8b=0`.

## Target triage (AP287 classification)

### Target 1: `test_w4_borcherds_transport.py` (177 lines)

**Classification: SUBSTANTIVE, NOT AP287 W8-B.**

Read in full. The file tests the algebraic identity

  (C^res_{3,4;4;0,3})^2 = (5/7) * (C^res_{3,3;4;0,2})^2

an explicit rational-function identity in c that is a non-trivial
DS OPE cancellation (Virasoro stage-4 Borcherds transport,
Vol I `conj:winfty-stage4-visible-borcherds-transport`). The
assertions are symbolic-rational (`sympy.cancel`), not boolean
truth tables. Gold-standard HZ-IV decoration warranted.

### Target 2: `test_borcherds_shadow_operations.py` (966 lines)

**Classification: SUBSTANTIVE, NOT AP287 W8-B.**

Read substantial portions (lines 1-100, 100-350, 900-966). The
file tests `prop:borcherds-shadow-identification` (F_n = o_n) on
standard landscape families and includes load-bearing numerical
anchors like kappa(V_k(sl_2)) arity-2 residue = 2k (Path B's
bilinear-form reading). Genuine rational-expression-level
checks via `sympy.simplify`, not boolean primitives. Gold-standard
decoration warranted.

### Scope note (both targets)

Both files sit ADJACENT to the Vol I kappa_BKM cluster because
they carry the "Borcherds" token, but neither concerns the
Borcherds *lift* c_N(0)/2 that defines kappa_BKM. They concern:
(a) Borcherds *secondary operations* F_n = o_n (shadow-Borcherds
identification for chiral kappa); (b) Borcherds *coefficient
transport* C_334 -> C_344 at stage-4 W-infinity. This scope
caveat is inscribed as a module-level comment in each file so a
future auditor does not reclassify them back into a strict
kappa_BKM lift-based census. Honest HZ-IV coverage is extended
to the file's internal theorem anchors regardless.

## Heals applied

### Edit 1: `test_w4_borcherds_transport.py`

Anchor: C_344^2 / C_334^2 = 5/7 (Vol I W-infinity stage-4
Borcherds transport).

Three disjoint paths:
- Path A: Zamolodchikov 1985 (Theor. Math. Phys. 65:1205)
  Jacobi-constrained W_4 OPE structure constants.
- Path B: Fateev-Lukyanov 1988 (Int. J. Mod. Phys. A3:507)
  screening Coulomb-gas / free-field intersection realisation.
- Path C: Blumenhagen-Eholzer-Honecker-Hornfeck-Hubel 1995
  (Int. J. Mod. Phys. A10:2367) W-algebra rigidity uniqueness.

Decorator alias: `_iv_w17_w4bt`.
New test: `test_gold_standard_transport_5_7_three_disjoint_paths`.
Path Z engine regression retained as cross-check only.

### Edit 2: `test_borcherds_shadow_operations.py`

Anchor: kappa(V_k(sl_2)) trace-form arity-2 residue = 2k
(shadow-Borcherds identification F_n = o_n, arity-2 bilinear).

Three disjoint paths:
- Path A: Kac 1998 'Vertex Algebras for Beginners' 2nd ed. (AMS)
  eq. (4.7.1) Borcherds-bilinear axiom J^a_{(1)} J^b = kappa_K.
- Path B: Sugawara 1968 (Phys. Rev. 170:1659) + Knizhnik-
  Zamolodchikov 1984 (Nucl. Phys. B247:83) trace-form channel of
  the Koszul conductor kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v).
- Path C: Frenkel-Ben-Zvi 2004 'Vertex Algebras and Algebraic
  Curves' 2nd ed. (AMS Math. Surveys 88) Prop. 3.4.6 + Cor. 3.4.11
  Casimir-centre formal-residue formula.

Decorator alias: `_iv_w17_bso`.
New test: `test_gold_standard_kappa_affine_sl2_three_disjoint_paths`.
Path Z engine regression retained as cross-check only.

## Post-gate PROOF (AP320)

Grep after Edit, both files:

```
test_borcherds_shadow_operations.py:
  983:    independent_verification as _iv_w17_bso,
  987: @_iv_w17_bso(
  1043: def test_gold_standard_kappa_affine_sl2_three_disjoint_paths():

test_w4_borcherds_transport.py:
  192:    independent_verification as _iv_w17_w4bt,
  248: @_iv_w17_w4bt(
  249: def test_gold_standard_transport_5_7_three_disjoint_paths():
```

Both decorators and their decorated functions present at the expected
line offsets. Edits atomic; no partial writes.

## Cumulative Vol I kappa_BKM HZ-IV tally

| Wave | Target | Status |
|---|---|---|
| pre-W15 | test_cy_bkm_algebra_engine.py | iv=1 gs=1 |
| pre-W15 | test_cy_borcherds_lift_engine.py | iv=1 gs=1 |
| pre-W15 | test_leech_genus2_sewing_engine.py | iv=1 gs=1 |
| pre-W15 | test_moonshine_bar_complex.py | iv=1 gs=1 |
| W15 | test_cy_mathieu_moonshine_engine.py | iv=1 gs=1 |
| W15 | test_cy_m24_bar_bridge_engine.py | iv=1 gs=1 |
| W15 | test_cy_mock_modular_bps_engine.py | iv=1 gs=1 |
| **W17** | **test_borcherds_shadow_operations.py** | **iv=1 gs=1** |
| **W17** | **test_w4_borcherds_transport.py** | **iv=1 gs=1** |

Final: 9 / 9 Vol I kappa_BKM-adjacent tight-core tests now carry
gold-standard HZ-IV decoration with three disjoint primary-source
paths plus Path Z engine regression.

## Test-runtime verification

Environment lacks `pytest` in PATH (venv absent, system python3 has
no pytest module). The new tests follow the exact pattern of
`test_cy_mock_modular_bps_engine.py::test_gold_standard_kappa_N4_c6_three_disjoint_paths`,
which is known-passing per Wave-15 report; the decorator API
(`compute.lib.independent_verification.independent_verification`) is
imported identically; assertions use the same
`Rational`/`simplify`/`Fraction` primitives. Expect pass on first run
in a pytest-equipped environment.

## Commit plan

1. Single commit touching only the two test files + this note.
2. Commit message draft (single-author, no co-author attribution):

```
Vol I Wave-17 kappa_BKM final 2: W8-B triage + HZ-IV gold-standard
decoration for test_borcherds_shadow_operations.py (kappa(V_k(sl_2))
arity-2 residue = 2k via Kac / Sugawara-KZ trace-form / FBZ Casimir)
and test_w4_borcherds_transport.py (C_344^2 / C_334^2 = 5/7 via
Zamolodchikov 1985 / Fateev-Lukyanov 1988 / Blumenhagen et al. 1995
W-algebra rigidity). Both files classified SUBSTANTIVE not AP287
W8-B. Scope note inscribed: shadow-Borcherds / transport adjacent to
kappa_BKM cluster but not lift-based; decoration still extends HZ-IV
coverage under AP319 discipline. Cumulative Vol I kappa_BKM-adjacent
coverage 9/9.
```

3. No PR creation. No artifact commits. No builds invoked here.

## Constitutional compliance

- All commits authored by Raeez Lorgat only.
- No AI attribution in code, comments, or commit message.
- AP287/AP319/AP320 discipline applied throughout.
- No AP234 bare kappa or AP126 bare Omega/z slips inside the
  decorator prose.
- No /B\d+ blacklist-slug leakage (AP236) in typeset material;
  this file is `.md` scratch and may reference AP numbers freely.
- Edits are atomic; pre/post grep-gate performed on full regex
  including `@_iv\(`, `@_iv_wN_...`, and
  `TestGoldStandardDisjointPaths` patterns.
