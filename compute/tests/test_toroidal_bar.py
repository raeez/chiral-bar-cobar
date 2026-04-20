"""Tests for compute/lib/toroidal_bar.py -- elliptic/toroidal bar complex.

Non-trivial identities tested:
  (i)   Eisenstein series q-expansion: E_2 = 1 - 24q - 72q^2 - ...
                                       E_4 = 1 + 240q + 2160q^2 + ...
                                       E_6 = 1 - 504q - 16632q^2 - ...
  (ii)  Rational-limit curvature: m_0^rat = 0 (no B-cycle on C).
  (iii) Bar decomposition depth at degree n: exactly n components with max
        modular weight 2(n-1); B^{(k)}_n = 0 for k >= n.
  (iv)  Fay d^2 = 0 identity role.
"""

from __future__ import annotations

from compute.lib.toroidal_bar import (
    bar_decomposition_by_weight,
    eisenstein_q_expansion,
    elliptic_bar_diff_deg,
    elliptic_curvature,
    elliptic_vs_rational,
    fay_d_squared_zero,
    verify_toroidal,
)


def test_smoke_verify_toroidal_all_pass():
    """Smoke: internal sanity suite returns all-True."""
    results = verify_toroidal()
    assert all(results.values()), [k for k, v in results.items() if not v]


def test_eisenstein_e4_first_coeffs():
    """E_4 = 1 + 240 sigma_3(n) q^n. First three: 1, 240, 2160 (240*(1+8))."""
    c = eisenstein_q_expansion(4, 5)
    assert c[0] == 1
    assert c[1] == 240
    # sigma_3(2) = 1 + 8 = 9, so a_2 = 240*9 = 2160
    assert c[2] == 2160
    # sigma_3(3) = 1 + 27 = 28, so a_3 = 240*28 = 6720
    assert c[3] == 6720


def test_eisenstein_e6_first_coeffs():
    """E_6 = 1 - 504 sigma_5(n) q^n."""
    c = eisenstein_q_expansion(6, 4)
    assert c[0] == 1
    assert c[1] == -504
    # sigma_5(2) = 1 + 32 = 33, so a_2 = -504*33 = -16632
    assert c[2] == -16632


def test_eisenstein_e2_first_coeffs():
    """E_2 = 1 - 24 sigma_1(n) q^n."""
    c = eisenstein_q_expansion(2, 4)
    assert c[0] == 1
    assert c[1] == -24
    # sigma_1(2) = 1 + 2 = 3, so a_2 = -72
    assert c[2] == -72


def test_rational_curvature_is_zero_limit():
    """Rational bar (on C) has m_0^rat = 0."""
    info = elliptic_vs_rational()
    assert "= 0" in info["rational_curvature"]


def test_elliptic_curvature_carries_E2():
    """Elliptic curvature comes from E_2(tau) (quasi-modular weight 2)."""
    curv = elliptic_curvature()
    assert curv["eisenstein"] == "E_2(tau)"
    # E_2 nome expansion: 1, -24, -72, -96 ...
    assert curv["nome_expansion_first_terms"][:2] == [1, -24]


def test_bar_diff_weight_graded_structure():
    """At degree n, elliptic correction uses E_{2n-2}: deg 2 -> E_2, deg 3 -> E_4."""
    d2 = elliptic_bar_diff_deg(2)
    assert d2["modular_weight"] == 2
    assert d2["quasi_modular"] is True

    d3 = elliptic_bar_diff_deg(3)
    assert d3["modular_weight"] == 4
    assert d3["quasi_modular"] is False


def test_bar_decomposition_counts():
    """B^{ell}_n has exactly n components; max weight 2(n-1)."""
    for n in [2, 3, 5]:
        d = bar_decomposition_by_weight(n)
        assert d["n_components"] == n
        assert d["max_modular_weight"] == 2 * (n - 1)
        assert d["finitely_many_terms"] is True


def test_fay_identity_ensures_d_squared_zero():
    """Fay trisecant identity is the elliptic analog of Arnold relation."""
    info = fay_d_squared_zero()
    assert "d^2 = 0" in info["role"]
    assert "Arnold" in info["rational_analog"]
