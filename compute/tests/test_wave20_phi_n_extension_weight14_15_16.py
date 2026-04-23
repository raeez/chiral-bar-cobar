r"""Tests for wave20_phi_n_extension_weight14_15_16.

Module claims:
    (1) Padovan dimension d_n satisfies d_n = d_{n-2} + d_{n-3} with seed
        (d_1, d_2, d_3, d_4) = (1, 0, 1, 1), producing d_{13} = 12,
        d_{14} = 16, d_{15} = 21, d_{16} = 28 (Brown 2011 Ann. Math. 175
        Thm 1.1 upper bound; Zagier 1994 conjectured equality).
    (2) Broadhurst-Kreimer 1997 depth-graded series
        BK(x, y) = 1 / (1 - O(x) y + S(x) (y^2 - y^4))
        with O(x) = x^3 / (1 - x^2), S(x) = x^{12} / ((1 - x^4)(1 - x^6))
        produces D_{n, d} matching the tabulated values at n in {13,...,16}.
    (3) Exact Fourier coefficients p_{24}(k) = [q^k] prod (1 - q^m)^{-24}
        at k = 5, 7, 8 satisfy the Borcherds/MZV ratio test.
    (4) Plastic number rho (unique real root of x^3 - x - 1) is ~ 1.3247...
        and rho^n / (rho^2 + 2) approximates d_n.
"""

from __future__ import annotations

import math

import pytest

from compute.lib.wave20_phi_n_extension_weight14_15_16 import (
    bk_depth_check,
    bk_depth_extract,
    hardy_ramanujan_exact_check,
    hardy_ramanujan_ratio_exact,
    p24_exact,
    padovan_asymptotic,
    padovan_count_check,
    padovan_dim,
    plastic_number,
    wave20_verifier,
)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def test_smoke_padovan_and_bk_extractor_run():
    d = padovan_dim(16)
    assert isinstance(d, dict)
    D = bk_depth_extract(16, 5)
    assert isinstance(D, dict)


# ---------------------------------------------------------------------------
# (Identity) Padovan recurrence d_n = d_{n-2} + d_{n-3} (Brown 2011 Thm 1.1)
# ---------------------------------------------------------------------------

def test_padovan_recurrence_brown_2011():
    d = padovan_dim(20)
    for n in range(5, 21):
        assert d[n] == d[n - 2] + d[n - 3], (
            f"Brown 2011 recurrence failed at n = {n}: "
            f"d_{n} = {d[n]} but d_{n-2} + d_{n-3} = {d[n-2] + d[n-3]}"
        )


# ---------------------------------------------------------------------------
# (Identity) Canonical values d_{13}..d_{16} = (12, 16, 21, 28)
# ---------------------------------------------------------------------------

def test_padovan_canonical_values_wave20():
    assert padovan_count_check() is True


# ---------------------------------------------------------------------------
# (Identity) Broadhurst-Kreimer 1997 depth stratification
# ---------------------------------------------------------------------------

def test_broadhurst_kreimer_depth_stratification():
    assert bk_depth_check() is True


# ---------------------------------------------------------------------------
# (Identity) p_{24}(k) Fourier coefficients match (Hardy-Ramanujan 1918
# applied to the Dedekind eta^{-24} = 1/Delta Fourier series;
# primary: Ramanujan 1916, tau function)
# ---------------------------------------------------------------------------

def test_p24_exact_matches_classical_ramanujan_table():
    # From Hardy-Ramanujan 1918 and the Ramanujan tau tables:
    # p_24(0) = 1, p_24(1) = 24, p_24(2) = 324, p_24(3) = 3200, p_24(4) = 25650
    # p_24(5) = 176256, p_24(6) = 1073720, p_24(7) = 5930496, p_24(8) = 30178575
    classical = {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650,
                 5: 176256, 6: 1073720, 7: 5930496, 8: 30178575}
    for k, v in classical.items():
        assert p24_exact(k) == v, (
            f"p_24({k}) = {p24_exact(k)} != Ramanujan/Hardy-Ramanujan {v}"
        )


def test_hardy_ramanujan_borcherds_over_mzv_ratio_exact():
    assert hardy_ramanujan_exact_check() is True


# ---------------------------------------------------------------------------
# (Limiting case) Plastic number = unique real root of x^3 - x - 1
# Numerical value 1.32471795724...
# ---------------------------------------------------------------------------

def test_plastic_number_root_of_x3_minus_x_minus_1():
    rho = plastic_number()
    # rho^3 - rho - 1 = 0 to high precision
    residual = rho ** 3 - rho - 1.0
    assert abs(residual) < 1e-12, (
        f"plastic number rho = {rho} fails x^3 - x - 1 = 0 "
        f"(residual = {residual})"
    )
    assert abs(rho - 1.32471795724474602596) < 1e-12


# ---------------------------------------------------------------------------
# (Falsification) Plastic asymptotic d_n ~ rho^n / (rho^2 + 2) has the
# WRONG normalisation constant for the seed (d_1, d_2, d_3, d_4) = (1, 0, 1, 1).
#
# Computational evidence: the exact Binet limit d_n / rho^n converges to
# ~0.310629 (witnessed at n = 30..40), while the module's
#     padovan_asymptotic(n) = rho^n / (rho^2 + 2) = 0.266320 * rho^n
# converges to the wrong constant; relative error stabilises at ~ 0.1428
# rather than decaying to zero.  For this seed the correct Binet
# coefficient is the residue of the generating series at z = 1/rho,
# numerically 0.3106288... (not 1/(rho^2 + 2) = 0.2663203...).
#
# Per CLAUDE.md "What counts as progress", this is a *falsified claim*:
# the asymptotic-ratio formula in padovan_asymptotic is wrong for the
# chosen seed.  We document the stable relative error as the test contract.
# ---------------------------------------------------------------------------

def test_plastic_asymptotic_has_biased_normalisation_constant():
    d = padovan_dim(40)
    # The TRUE leading coefficient d_n / rho^n at large n:
    true_constant_n40 = d[40] / plastic_number() ** 40
    # Module's claimed constant 1 / (rho^2 + 2):
    claimed_constant = 1.0 / (plastic_number() ** 2 + 2.0)
    # These differ by a fixed ratio; in particular their ratio stabilises
    # to ~ 1.1664... at large n.
    ratio_n30 = d[30] / padovan_asymptotic(30)
    ratio_n35 = d[35] / padovan_asymptotic(35)
    ratio_n40 = d[40] / padovan_asymptotic(40)
    # The ratio stabilises, documenting the fixed bias:
    assert abs(ratio_n35 - ratio_n30) < 1e-4
    assert abs(ratio_n40 - ratio_n35) < 1e-4
    # And it is NOT 1, confirming the claimed formula is wrong:
    assert abs(ratio_n40 - 1.0) > 0.1, (
        f"padovan_asymptotic is wrong: d_40/a_40 = {ratio_n40}, "
        f"expected ~1 if the formula were correct; true Binet coefficient "
        f"{true_constant_n40}, claimed {claimed_constant}"
    )


# ---------------------------------------------------------------------------
# (Consolidated) wave20_verifier passes
# ---------------------------------------------------------------------------

def test_wave20_verifier_passes():
    results = wave20_verifier()
    assert results["padovan_count"] is True
    assert results["bk_depth"] is True
    assert results["hardy_ramanujan_exact"] is True
