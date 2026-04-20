"""Tests for compute.lib.wave20_phi_n_extension_weight17_18_19_20.

Verifies Padovan dimensions, Broadhurst-Kreimer depth stratification,
phi^(n) leading values, Hardy-Ramanujan ratios, and plastic-number
asymptotic at weights n in {17, 18, 19, 20}.

Key scope threshold: weight 18 is the first weight at which a
depth-6 Brown canonical basis element (zeta(3, 3, 3, 3, 3, 3))
appears, requiring Zagier-Hoffman depth-reduction at depth 6 (open;
Brown 2012 covers depth <= 4 unconditionally, <= 5 conditionally).
"""
from __future__ import annotations

import math

import pytest

from compute.lib.wave20_phi_n_extension_weight17_18_19_20 import (
    bk_depth_check_17_20,
    bk_depth_extract,
    first_depth_six_check,
    hardy_ramanujan_exact_check_17_20,
    hardy_ramanujan_ratio_check_extension,
    hardy_ramanujan_ratio_exact_17_20,
    p24_asymptotic,
    p24_exact,
    padovan_asymptotic,
    padovan_count_check_17_20,
    padovan_dim,
    phi_n_leading_check_17_20,
    phi_n_mzv_leading,
    phi_n_richardson_check_17_20,
    plastic_asymptotic_check_17_20,
    plastic_number,
    wave20_verifier_17_20,
)


# ---------------------------------------------------------------------------
# 1. Padovan dimensions
# ---------------------------------------------------------------------------

def test_padovan_count_17_20():
    assert padovan_count_check_17_20() is True


def test_padovan_dim_17_20_values():
    d = padovan_dim(22)
    assert d[17] == 37
    assert d[18] == 49
    assert d[19] == 65
    assert d[20] == 86


def test_padovan_recurrence_17_20():
    d = padovan_dim(22)
    for n in range(17, 21):
        assert d[n] == d[n - 2] + d[n - 3], (
            f"Padovan recurrence fails at n = {n}: "
            f"d_{n} = {d[n]} vs d_{n - 2} + d_{n - 3} = {d[n - 2] + d[n - 3]}"
        )


# ---------------------------------------------------------------------------
# 2. Broadhurst-Kreimer depth stratification
# ---------------------------------------------------------------------------

def test_bk_depth_17_20():
    assert bk_depth_check_17_20() is True


def test_bk_depth_row_17():
    D = bk_depth_extract(22, 7)
    expected = [1, 0, 13, 0, 7, 0]
    got = [D.get((17, d_), 0) for d_ in range(1, 7)]
    assert got == expected


def test_bk_depth_row_18():
    D = bk_depth_extract(22, 7)
    expected = [0, 6, 0, 18, 0, 4]
    got = [D.get((18, d_), 0) for d_ in range(1, 7)]
    assert got == expected


def test_bk_depth_row_19():
    D = bk_depth_extract(22, 7)
    expected = [1, 0, 17, 0, 19, 0]
    got = [D.get((19, d_), 0) for d_ in range(1, 7)]
    assert got == expected


def test_bk_depth_row_20():
    D = bk_depth_extract(22, 7)
    expected = [0, 7, 0, 30, 0, 12]
    got = [D.get((20, d_), 0) for d_ in range(1, 7)]
    assert got == expected


def test_first_depth_six_at_18():
    """n = 18 is the first weight with D_{n, 6} > 0."""
    assert first_depth_six_check() is True


def test_odd_weight_even_depth_empty_17_19():
    """At odd n in {17, 19}, the even-depth strata D_{n, 2k} are empty (BK)."""
    D = bk_depth_extract(22, 7)
    for n in (17, 19):
        for d_even in (2, 4, 6):
            assert D.get((n, d_even), 0) == 0, (
                f"Expected D_{{{n}, {d_even}}} = 0 at odd weight, "
                f"got {D.get((n, d_even), 0)}"
            )


def test_even_weight_odd_depth_empty_18_20():
    """At even n in {18, 20}, the odd-depth strata D_{n, 2k+1} are empty (BK)."""
    D = bk_depth_extract(22, 7)
    for n in (18, 20):
        for d_odd in (1, 3, 5):
            assert D.get((n, d_odd), 0) == 0, (
                f"Expected D_{{{n}, {d_odd}}} = 0 at even weight, "
                f"got {D.get((n, d_odd), 0)}"
            )


# ---------------------------------------------------------------------------
# 3. phi^(n) leading numerical values
# ---------------------------------------------------------------------------

def test_phi_n_leading_17_20():
    assert phi_n_leading_check_17_20() is True


def test_phi_n_leading_values_match_d_over_factorial():
    """Leading estimate d_n / n! agrees with phi_n_mzv_leading to 1% relative."""
    d = padovan_dim(22)
    for n in range(17, 21):
        expected = d[n] / math.factorial(n)
        got = phi_n_mzv_leading(n)
        rel = abs(got - expected) / expected
        assert rel < 0.01, f"phi^({n}): got {got:.3e}, expected {expected:.3e}, rel {rel}"


def test_phi_n_17_magnitude():
    v = phi_n_mzv_leading(17)
    assert 5e-14 < v < 5e-13, f"phi^(17)_MZV ~ {v:.3e} out of expected range"


def test_phi_n_18_magnitude():
    v = phi_n_mzv_leading(18)
    assert 5e-15 < v < 5e-14, f"phi^(18)_MZV ~ {v:.3e} out of expected range"


def test_phi_n_19_magnitude():
    v = phi_n_mzv_leading(19)
    assert 1e-16 < v < 5e-15, f"phi^(19)_MZV ~ {v:.3e} out of expected range"


def test_phi_n_20_magnitude():
    v = phi_n_mzv_leading(20)
    assert 5e-18 < v < 5e-16, f"phi^(20)_MZV ~ {v:.3e} out of expected range"


def test_phi_n_values_dictionary_17_20():
    vals = phi_n_richardson_check_17_20()
    assert set(vals.keys()) == {17, 18, 19, 20}
    for n in range(17, 21):
        assert 0 < vals[n] < 1.0, f"phi^({n})_MZV should be a small positive real"


# ---------------------------------------------------------------------------
# 4. Hardy-Ramanujan ratios
# ---------------------------------------------------------------------------

def test_hardy_ramanujan_exact_17_20():
    assert hardy_ramanujan_exact_check_17_20() is True


def test_p24_9():
    assert p24_exact(9) == 143184000


def test_p24_10():
    assert p24_exact(10) == 639249300


def test_hardy_ramanujan_ratio_n17():
    r = hardy_ramanujan_ratio_exact_17_20()
    expected = 143184000 / 37
    assert abs(r[17] - expected) < 1e-6, f"ratio n=17: {r[17]} != {expected}"


def test_hardy_ramanujan_ratio_n18():
    r = hardy_ramanujan_ratio_exact_17_20()
    expected = 143184000 / 49
    assert abs(r[18] - expected) < 1e-6


def test_hardy_ramanujan_ratio_n19():
    r = hardy_ramanujan_ratio_exact_17_20()
    expected = 639249300 / 65
    assert abs(r[19] - expected) < 1e-6


def test_hardy_ramanujan_ratio_n20():
    r = hardy_ramanujan_ratio_exact_17_20()
    expected = 639249300 / 86
    assert abs(r[20] - expected) < 1e-6


def test_hardy_ramanujan_asym_overshoots_exact():
    """Asymptotic (4 pi)^{-1} k^{-27/4} exp(4 pi sqrt k) overshoots exact by 4-5x."""
    rs = hardy_ramanujan_ratio_check_extension()
    for n in range(17, 21):
        _exact, _asym, ratio = rs[n]
        assert 2.0 < ratio < 10.0, (
            f"asym/exact at n = {n} is {ratio:.2f}, outside expected 2-10 range"
        )


def test_hardy_ramanujan_sawtooth_17_19():
    """k = ceil(n/2) jumps from 9 to 10 at n = 19, giving a ratio jump."""
    rs = hardy_ramanujan_ratio_exact_17_20()
    # n = 17, 18 both have k = 9; n = 19, 20 both have k = 10
    # Ratio at n = 19 is bigger than ratio at n = 18 despite d_n growing,
    # because p_24(10) / p_24(9) ~ 4.5 dominates 65/49 ~ 1.33.
    assert rs[19] > rs[18], (
        f"Expected sawtooth jump at n = 18 -> 19 (k = 9 -> 10): "
        f"rs[19] = {rs[19]:.3e}, rs[18] = {rs[18]:.3e}"
    )


# ---------------------------------------------------------------------------
# 5. Plastic-number asymptotic
# ---------------------------------------------------------------------------

def test_plastic_number_value():
    rho = plastic_number()
    assert abs(rho - 1.324717957244746) < 1e-12


def test_plastic_number_root():
    rho = plastic_number()
    assert abs(rho ** 3 - rho - 1) < 1e-12


def test_padovan_asymptotic_17_20():
    results = plastic_asymptotic_check_17_20()
    assert set(results.keys()) == {17, 18, 19, 20}
    for n, (dn, asy, err) in results.items():
        # relative error should be under 20% in this range
        assert abs(err) < 0.20, f"at n = {n}: err {err:.2%} exceeds 20%"


def test_padovan_asymptotic_closed_form_matches_numerical():
    """A rho^n with A = rho^2/(2 rho + 3) matches exact d_n within 5%
    (oscillating from the complex conjugate roots of x^3 - x - 1)."""
    results = plastic_asymptotic_check_17_20()
    for n, (dn, asy, err) in results.items():
        assert abs(err) < 0.05, (
            f"at n = {n}: d_n = {dn}, A rho^n = {asy:.3f}, rel err {err:.2%}"
        )


# ---------------------------------------------------------------------------
# 6. Aggregate verifier
# ---------------------------------------------------------------------------

def test_wave20_verifier_17_20():
    result = wave20_verifier_17_20()
    assert result == {
        "padovan_count_17_20": True,
        "bk_depth_17_20": True,
        "first_depth_six_at_18": True,
        "phi_n_leading_17_20": True,
        "hardy_ramanujan_exact_17_20": True,
    }


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
