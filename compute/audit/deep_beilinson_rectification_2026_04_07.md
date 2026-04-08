# Deep Beilinson Rectification — 2026-04-07

## Summary

Comprehensive audit of ~55 compute engines and ~8500+ tests.
Previous session found 12 kappa bugs, 1 CRITICAL SVir formula error, 1 false Koszulness claim.
This audit found and fixed 6 additional bugs across 5 engines.

## Findings

### F1. CRITICAL — Stokes engine: Borel-Pade applied to convergent series (theorem_stokes_mc_engine.py)

**Class**: B (formula/algorithm), AP10 (test with wrong methodology)  
**Severity**: CRITICAL (12 test failures, fundamental mathematical error)

The Borel-Pade proof (Proof 4) applied the Borel transform to Z(u) = sum F_g u^g,
which is a CONVERGENT series (radius (2pi)^2). The Borel transform of a convergent
series is entire (no singularities), making the Pade pole-finding completely wrong.
The Pade found a spurious pole at ~796 instead of (2pi)^2 = 39.5.

**Fix**: Apply Pade approximant to Z(u) directly. Z(u) has simple poles at u_n = (2pi*n)^2.
After fix: pole found at 39.478... with relative error ~7e-15, residue matches
R_1 = -8*pi^2*kappa to machine precision.

### F2. SERIOUS — Stokes engine: Cauchy integral normalization (theorem_stokes_mc_engine.py)

**Class**: B (formula)  
**Severity**: SERIOUS (Cauchy cross-check returned 0 for all genera)

The Cauchy integral extracted F_g via `fg_cauchy.real / (2.0 * PI)` but the correct
normalization is `(fg_cauchy / (2.0j * PI)).real`. The factor of i was missing from
the denominator, causing the integral to vanish identically.

**Fix**: `fg_cauchy = (fg_cauchy / (2.0j * PI)).real`

### F3. SERIOUS — Stokes engine: ratio test with spurious factorial (theorem_stokes_mc_engine.py)

**Class**: B (formula)  
**Severity**: SERIOUS (returned A = 406707 instead of 39.48)

`_verify_instanton_action_numerical` computed `(2g+2)(2g+1) * F_g / F_{g+1}`,
which would be correct for a FACTORIALLY DIVERGENT series. But F_g decreases
geometrically (~1/A^g), so the correct ratio test is simply `F_g / F_{g+1} -> A`.

**Fix**: Removed the spurious `(2g+2)*(2g+1)` factor.

### F4. MODERATE — Stokes engine: partial fraction convergence (theorem_stokes_mc_engine.py)

**Class**: B (numerical)  
**Severity**: MODERATE (1 test failure at g=1 due to slow alternating convergence)

The partial fraction sum `sum (-1)^{n+1} * 2*kappa / (2*pi*n)^{2g}` used 100 terms,
giving only ~5 digits at g=1. Replaced with exact formula using Dirichlet eta function:
`F_g = 2*kappa * eta(2g) / (2pi)^{2g}` where `eta(s) = (1 - 2^{1-s}) * zeta(s)`.

### F5. MODERATE — Large-N engine: two docstring formula errors (theorem_large_n_delta_f2_engine.py)

**Class**: E (editorial), B (formula in documentation)  
**Severity**: MODERATE (code correct, docstring wrong)

Line 25: `A(N) = N^4/8 + N^3/3 - N^4/4 - ...` had N^4/4 instead of N^2/4 (typo: N^4 twice).
Line 29: `A(N)/B(N) = 12N^2 + 4N - 58 + O(1/N)` should be `12N^2 + 20N + 28 + O(1/N)`.
Both verified by exact polynomial division; code was correct, only docstrings wrong.

### F6. MODERATE — Logarithmic VOA engine: generator count (logarithmic_voa_shadow_engine.py)

**Class**: C (structural), AP9 (same name, different object)  
**Severity**: MODERATE (docstring and code both wrong)

The triplet W(p) has 4 strong generators (T + sl_2 triplet W+, W0, W-), not 2.
The engine conflated the sl_2 triplet as a single "W" generator. This affected
`n_generators`, `generator_weights`, and downstream PBW character comparisons.
Cross-checked against triplet_koszulness_engine.py which correctly had 4.
Tests had AP10 violations (hardcoded n_generators=2).

**Fix**: Changed n_generators from 2 to 4, generator_weights from [2, 2p-1] to
[2, 2p-1, 2p-1, 2p-1], updated 3 test assertions.

## Verified Clean

All 25 theorem engines audited. The following were verified free of scope/formula issues:
- theorem_delta_f3_universal_engine.py: N=2 vanishing confirmed, W_3 values verified
- theorem_bethe_mc_engine.py: R(u) = uI + iP verified via YBE (error ~9e-16)
- theorem_bv_sewing_engine.py: scope correctly qualified (G/L proved, C/M conditional)
- theorem_admissible_sl3_libar_engine.py: Koszulness correctly marked as conditional
- theorem_w4_full_ope_delta_f2_engine.py: manuscript formulas algebraically verified
- theorem_burns_f2_engine.py: F_2 = 7/1440 confirmed
- All lambda_g^FP values independently verified (g=1..4)
- W_4 irrational decomposition R(c) + I_1(c) + I_2(c) verified algebraically
- Large-c limit (3*sqrt(10)+28)/192 ~ 0.195 confirmed

## Test Suite Status

Modified engines: 532 passed, 2 skipped, 0 failed.
Full suite: running (8500+ tests expected).

## Files Modified

1. compute/lib/theorem_stokes_mc_engine.py — F1, F2, F3, F4 (4 bugs fixed)
2. compute/lib/theorem_large_n_delta_f2_engine.py — F5 (2 docstring fixes)
3. compute/lib/logarithmic_voa_shadow_engine.py — F6 (generator count fix)
4. compute/tests/test_logarithmic_voa_shadow_engine.py — F6 (3 AP10 test fixes)
