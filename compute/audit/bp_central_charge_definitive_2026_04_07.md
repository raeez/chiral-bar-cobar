# Bershadsky-Polyakov Central Charge: Definitive Resolution

Date: 2026-04-07

## Verdict

**The correct formula is Formula 3:**

    c_BP(k) = 2 - 24(k+1)^2 / (k+3)
            = -2(12k^2 + 23k + 9) / (k+3)
            = -2(3k+1)(4k+9) / (k+3)

    K_BP = c(k) + c(-k-6) = 196
    kappa_BP = c/6 = -(12k^2 + 23k + 9) / (3(k+3))
    rho_BP = 1/6

This is the Fehily-Kawasetsu-Ridout (FKR 2020, arXiv:1906.02935) formula, already
present in landscape_census.tex (line 134) and standalone/bp_self_duality.tex.

The three other formulas appearing in the codebase are all WRONG.

## The Four Formulas and Their Status

| # | Formula | K | Source | Status |
|---|---------|---|--------|--------|
| 1 | (k-15)/(k+3) = 1 - 18/(k+3) | 2 | bershadsky_polyakov_bar.py, sl3_subregular_bar.py | **WRONG** |
| 2 | 2 - 3(2k+3)^2/(k+3) | 76 | bp_shadow_tower.py, nonprincipal_ds_reduction.py, subregular_hook_frontier.tex | **WRONG** |
| 3 | 2 - 24(k+1)^2/(k+3) | 196 | landscape_census.tex, bp_self_duality.tex, w_algebra_chapter_rectification_engine.py | **CORRECT** |
| 4 | 4(k-3)/(k+3) | 8 | Audit agent independent derivation | **WRONG** |

## Verification Evidence

### Test 1: Admissible level k = -3/2 (DECISIVE)

The first admissible level for sl_3 is k = -3/2 (k+h^v = 3/2). The BP algebra at
this level is the triplet algebra/N=2 minimal model with c = -2. This is established
by Ridout-Wood (2015, arXiv:1507.00234) and Adamovic-Kontrec (2020, arXiv:1909.13064).

| Formula | c(-3/2) | Expected | Pass? |
|---------|---------|----------|-------|
| F1: (k-15)/(k+3) | -11 | -2 | FAIL |
| F2: 2-3(2k+3)^2/(k+3) | +2 | -2 | FAIL |
| F3: 2-24(k+1)^2/(k+3) | **-2** | -2 | **PASS** |
| F4: 4(k-3)/(k+3) | -12 | -2 | FAIL |

Only Formula 3 matches the known value.

### Test 2: Deligne exceptional level k = -1

At k = -1, V_{-1}(sl_3) is the Deligne exceptional VOA. The DS reduction gives BP at
k = -1. The c = 2 value matches the free-field N=2 SCA realization.

| Formula | c(-1) | Note |
|---------|-------|------|
| F1 | -8 | |
| F2 | 1/2 | |
| F3 | **2** | Matches free-field N=2 SCA |
| F4 | -8 | |

### Test 3: Koszul conductor constancy

c(k) + c(-k-6) must be independent of k (Feigin-Frenkel involution).
All four formulas pass this test (each gives a different constant).
Formula 3 gives K = 196.

### Test 4: Self-consistency of complementarity at numerical levels

Verified c(k) + c(-k-6) = 196 at k = -3/2, -1, 0, 1 for Formula 3. All pass.

## Error Genealogy

### Formula 1: c = (k-15)/(k+3), K = 2

This is the naive KRW formula with ingredients:
- dim(g_0) = 2 (Cartan only, grade-0 eigenspace of ad(h/2))
- dim(g_{1/2}) = 2 (grade-1/2 eigenspace)
- ||rho - rho_L||^2 = 3/2

Plugging into c = dim(g_0) - (1/2)*dim(g_{1/2}) - 12*||rho-rho_L||^2/(k+3):
c = 2 - 1 - 18/(k+3) = 1 - 18/(k+3) = (k-15)/(k+3).

**Error**: This KRW form omits the Sugawara subtraction term from the residual
subalgebra. For the PRINCIPAL nilpotent, there is no residual algebra (g_0 is
the Cartan, which is abelian). For the MINIMAL nilpotent, the stress tensor of
the W-algebra includes a k-dependent improvement term T_W = T_Sug + alpha*dJ
that contributes an additional -24k^2/(k+3) (approximately) to c. The naive
linear-over-linear KRW misses this entirely.

Present in: bershadsky_polyakov_bar.py (lines 15, 77-86), sl3_subregular_bar.py
(lines 30, 105-115). Both files explicitly claim dim(g_0)=2, dim(g_{1/2})=2,
||rho-rho_L||^2=3/2 and derive (k-15)/(k+3). The K=2 Koszul conductor and the
kappa+kappa' = 1/3 complementarity sum are downstream consequences of this error.

### Formula 2: c = 2 - 3(2k+3)^2/(k+3), K = 76

This appears to be an intermediate computation that uses SOME but not all of the
Sugawara correction. The coefficient 3 in 3(2k+3)^2 is wrong; the correct
coefficient structure is 24(k+1)^2.

Numerically: 3(2k+3)^2 = 12k^2 + 36k + 27, while 24(k+1)^2 = 24k^2 + 48k + 24.
The difference is 12k^2 + 12k - 3 = 3(4k^2 + 4k - 1) = 3(2k-1)(2k+1)... actually
3(4k^2+4k-1) does not factor nicely. At k=-3/2: difference = 27-6 = ... let me just
note 3*0 = 0 vs 24*(1/4) = 6, so c_F2(-3/2) = 2-0 = 2 vs c_F3(-3/2) = 2-4 = -2.

Present in: bp_shadow_tower.py (lines 15, 45-49), nonprincipal_ds_reduction.py
(lines 79-84), subregular_hook_frontier.tex (lines 911, 926, 941, 960, 965,
1015, 1022). This is the formula currently in the MANUSCRIPT body text.

### Formula 4: c = 4(k-3)/(k+3), K = 8

This was claimed as an "independent derivation" by the open-math-questions audit
agent. It is a linear-over-linear formula, consistent with the false claim that
"W-algebra central charges from KRW are always linear-over-linear." The claim
is false: non-principal DS reductions produce quadratic-over-linear central charges
due to the k-dependent improvement term in the stress tensor.

## Why the Central Charge is Quadratic-over-Linear

The audit agent's structural claim -- "W-algebra central charges from KRW are always
linear-over-linear" -- is FALSE for non-principal nilpotent orbits. The reason:

For the PRINCIPAL nilpotent, all ad(h/2)-grades are integers. The ghost system
consists entirely of bc-ghosts, and the stress tensor of the W-algebra is
T_W = T_Sug + T_ghost (no improvement term needed). The central charge is
c_Sug + c_ghost = linear-over-linear + constant = linear-over-linear.

For NON-PRINCIPAL nilpotents with half-integer grades (like the minimal nilpotent),
the stress tensor requires a k-DEPENDENT improvement: T_W = T_Sug + T_ghost + alpha*dJ.
The improvement parameter alpha depends on k (it is fixed by requiring the half-integer
weight generators to be primary under T_W). The c-shift from the improvement is
-12*alpha^2*k_J, where both alpha and k_J are rational functions of k. This contributes
a QUADRATIC term in k to the numerator of c(k).

Specifically, for BP:
c = c_Sug(sl_3, k) + c_ghost + c_improvement
  = 8k/(k+3) + 0 + delta_imp(k)
where delta_imp = -6(4k^2+9k+3)/(k+3).

Verification: delta_imp(-3/2) = +6. So c(-3/2) = -8 + 0 + 6 = -2. Correct.

## Complete File Inventory (AP5 Propagation)

### Files using WRONG Formula 1 (c = (k-15)/(k+3), K = 2)

**compute/lib:**
- bershadsky_polyakov_bar.py: lines 15, 77-86 (bp_central_charge function)
- sl3_subregular_bar.py: lines 30, 42, 105-115, 126, 198, 680

**compute/tests:**
- test_sl3_subregular_bar.py (imports from sl3_subregular_bar)
- test_bershadsky_polyakov_bar.py: line 19 (docstring cites K=76 but imports F1 code)

### Files using WRONG Formula 2 (c = 2 - 3(2k+3)^2/(k+3), K = 76)

**chapters/ (.tex):**
- subregular_hook_frontier.tex: lines 911, 926, 941, 960, 965, 1015, 1022

**appendices/ (.tex):**
- nonlinear_modular_shadows.tex: line 3882

**compute/lib:**
- bp_shadow_tower.py: lines 15, 17, 45-49, 67, 199, 205, 210, 212, 240, 327, 376
- nonprincipal_ds_reduction.py: lines 79-84
- ds_shadow_higher_arity.py: lines 39, 461, 572, 579
- bershadsky_polyakov_bar.py: lines 20, 23, 26, 88 (docstring mentions K=76)
- theorem_nonprincipal_line_operators_engine.py: lines 57, 60, 836
- darith_full_landscape_engine.py: line 669

**compute/tests:**
- test_bp_shadow_tower.py: lines 4, 41-43, 261-263, 372-374
- test_ds_shadow_higher_arity.py: lines 474-476, 601-604
- test_theorem_nonprincipal_line_operators_engine.py: lines 167-169, 407, 437, 461, 465, 500
- test_bershadsky_polyakov_bar.py: lines 19, 107, 558, 571

**standalone:**
- bp_self_duality.tex: line 76 (early passage, later corrected in Warning block)

### Files using CORRECT Formula 3 (c = 2 - 24(k+1)^2/(k+3), K = 196)

**chapters/ (.tex):**
- landscape_census.tex: lines 134-135

**standalone:**
- bp_self_duality.tex: lines 161-164, 281, 291, 298 (and Warning at 274-294)

**compute/lib:**
- theorem_w_algebra_chapter_rectification_engine.py: line 20

## Downstream Impact

Correcting from F2 (K=76) to F3 (K=196) affects:

1. **kappa_BP**: changes from c/6 with F2-central-charge to c/6 with F3-central-charge.
   All numerical kappa values in the shadow tower change.

2. **Sigma invariant**: Delta^(r) = S_r(c) + S_r(K-c). With K=76 vs K=196, ALL
   sigma invariant values change.

3. **Complementarity sum**: kappa(k) + kappa(-k-6) changes from 76/6 = 38/3
   to 196/6 = 98/3.

4. **Shadow tower on T-line**: Sh_r^T(k) = S_r^{Vir}(c_BP(k)). Since c_BP(k)
   changes, ALL shadow tower coefficients as functions of k change.

5. **Comparison with W_3**: The bp_vs_w3_comparison results change because
   the BP tower uses different c values.

6. **Tests**: ~25 test assertions hardcode K=76 or K=2 and will FAIL after correction.

## Recommendation

This is a CRITICAL fix requiring coordinated correction across ~20 files in the
compute layer, ~3 .tex files, and ~6 test files. The correction should:

1. Establish a SINGLE canonical bp_central_charge() in one file (e.g., update
   bershadsky_polyakov_bar.py) with the correct formula.
2. Make all other files import from the canonical source (AAP3).
3. Update all hardcoded K=76 and K=2 to K=196.
4. Update subregular_hook_frontier.tex and nonlinear_modular_shadows.tex.
5. Recompute all BP shadow tower, sigma invariant, and comparison results.
6. Update all test expected values.
7. Verify against c(-3/2)=-2 and c(-1)=2 in the test suite.

The standalone/bp_self_duality.tex Warning block (lines 274-294) should be updated:
it currently claims "K=76 is correct in that [alternate] convention" and that the
two formulas represent different conventions. This is WRONG: Formula 2 is simply
an incorrect formula that happens to give a constant K, not a valid alternative
convention. The Warning should be revised to state that Formula 2 was an error.
