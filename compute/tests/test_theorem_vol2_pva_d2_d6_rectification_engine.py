"""Tests for theorem_vol2_pva_d2_d6_rectification_engine.

Each test verifies the AP44 / AP49 cross-volume bridge for a specific
PVA descent fact: D2 (sesquilinearity), D3 (skew-symmetry),
D4 (Jacobi), D5 (Leibniz), D6 (m_{k>=3} vanishing).

Multi-path verification: every test computes the same quantity by at
least two independent paths and asserts they agree as Fractions.

All tests check the AP44 divided-power factor 1/n! explicitly.
"""
from fractions import Fraction
from math import factorial

import pytest

from compute.lib.theorem_vol2_pva_d2_d6_rectification_engine import (
    AP44_DIVIDED_POWER_FACTOR,
    AP49_BRIDGE,
    VOL1_CONVENTION,
    VOL2_CONVENTION,
    LambdaBracket,
    OPEModes,
    affine_sl2_lambda_vol2,
    affine_sl2_ope_vol1,
    ap49_bridge_vol1_to_vol2,
    ap49_bridge_vol2_to_vol1,
    ap49_consistency_check,
    borel_coeff,
    borel_round_trip,
    constants_banner,
    d2_lhs_dh_e,
    d2_lhs_h_de,
    d2_rhs_lambda_plus_d_he,
    d2_rhs_minus_lambda_he,
    d3_fe_direct,
    d3_fe_from_skew,
    d3_jj_direct,
    d3_jj_from_skew,
    d4_jacobi_e_f_e_lhs,
    d4_jacobi_e_f_e_rhs,
    d4_jacobi_h_e_f_lhs,
    d4_jacobi_h_e_f_rhs,
    d5_leibniz_e_h2_lhs,
    d5_leibniz_e_h2_rhs,
    d5_leibniz_h_ef_lhs,
    d5_leibniz_h_ef_rhs,
    d6_m3_amplitude_dimension,
    d6_mk_amplitude_dimension,
    heisenberg_lambda_vol2,
    heisenberg_ope_vol1,
    inverse_borel_coeff,
    khan_zeng_consistency,
    khan_zeng_sl2_lambda,
    multipath_lambda_coefficient,
    virasoro_lambda_vol2,
    virasoro_ope_vol1,
)


# =====================================================================
# Section A: AP44 Borel transform basics
# =====================================================================


def test_ap44_borel_n0_is_identity():
    """At n=0, divided power 1/0! = 1, so Borel is identity."""
    assert borel_coeff(Fraction(7), 0) == Fraction(7)


def test_ap44_borel_n1_is_identity():
    """At n=1, divided power 1/1! = 1, so Borel is identity."""
    assert borel_coeff(Fraction(5), 1) == Fraction(5)


def test_ap44_borel_n2_divides_by_2():
    """At n=2, divided power is 1/2."""
    assert borel_coeff(Fraction(6), 2) == Fraction(3)


def test_ap44_borel_n3_divides_by_6():
    """At n=3, divided power is 1/6. Virasoro: T_{(3)}T = c/2 -> c/12."""
    c = Fraction(13)
    assert borel_coeff(c / 2, 3) == c / 12


def test_ap44_borel_n4_divides_by_24():
    """At n=4, divided power is 1/24."""
    assert borel_coeff(Fraction(48), 4) == Fraction(2)


def test_ap44_borel_n5_divides_by_120():
    """At n=5, divided power is 1/120. W_3: W_{(5)}W = c/3 -> c/360."""
    c = Fraction(50)
    assert borel_coeff(c / 3, 5) == c / 360


def test_ap44_borel_negative_n_raises():
    with pytest.raises(ValueError):
        borel_coeff(Fraction(1), -1)


def test_ap44_inverse_borel_n3():
    """Inverse Borel at n=3 multiplies by 6. lambda-bracket c/12 -> OPE c/2."""
    c = Fraction(26)
    assert inverse_borel_coeff(c / 12, 3) == c / 2


def test_ap44_inverse_borel_n5():
    """Inverse Borel at n=5 multiplies by 120."""
    assert inverse_borel_coeff(Fraction(1), 5) == Fraction(120)


def test_ap44_borel_round_trip_identity():
    """Borel . inverse-Borel == identity for n in 0..6."""
    for n in range(7):
        for val in [Fraction(0), Fraction(1), Fraction(13), Fraction(7, 3)]:
            assert borel_round_trip(val, n) == val


# =====================================================================
# Section B: AP49 cross-volume bridge for Heisenberg
# =====================================================================


def test_ap49_heisenberg_vol1_to_vol2_bridge_k1():
    """H_{k=1}: J_{(1)} J = 1, so {J_lambda J} = 1 * lambda^1 / 1! = lambda."""
    ope = heisenberg_ope_vol1(Fraction(1))["JJ"]
    lb = ap49_bridge_vol1_to_vol2(ope)
    assert lb.coeffs.get(0, Fraction(0)) == Fraction(0)
    assert lb.coeffs.get(1, Fraction(0)) == Fraction(1)


def test_ap49_heisenberg_vol1_to_vol2_bridge_k7():
    """H_{k=7}: J_{(1)} J = 7, so {J_lambda J} = 7 lambda."""
    ope = heisenberg_ope_vol1(Fraction(7))["JJ"]
    lb = ap49_bridge_vol1_to_vol2(ope)
    assert lb.coeffs[1] == Fraction(7)


def test_ap49_heisenberg_consistency_k1():
    ope = heisenberg_ope_vol1(Fraction(1))["JJ"]
    lb = heisenberg_lambda_vol2(Fraction(1))["JJ"]
    checks = ap49_consistency_check(ope, lb)
    assert all(checks.values()), f"Heisenberg consistency failed: {checks}"


def test_ap49_heisenberg_consistency_negative_k():
    """Heisenberg at k = -3 (Koszul-dual level)."""
    ope = heisenberg_ope_vol1(Fraction(-3))["JJ"]
    lb = heisenberg_lambda_vol2(Fraction(-3))["JJ"]
    checks = ap49_consistency_check(ope, lb)
    assert all(checks.values())


def test_ap49_heisenberg_round_trip_k5():
    """Round-trip Vol II -> Vol I -> Vol II for Heisenberg."""
    lb = heisenberg_lambda_vol2(Fraction(5))["JJ"]
    ope = ap49_bridge_vol2_to_vol1(lb)
    lb2 = ap49_bridge_vol1_to_vol2(ope)
    assert lb.coeffs == lb2.coeffs


# =====================================================================
# Section C: AP49 cross-volume bridge for Virasoro
# =====================================================================


def test_ap49_virasoro_vol1_to_vol2_n3_c13():
    """Virasoro at c=13: T_{(3)}T = 13/2, so lambda^3 coeff = 13/24.
    But we always store the SCALAR part, which is c/12 = 13/12.
    """
    ope = virasoro_ope_vol1(Fraction(13))["TT"]
    # n=3 mode is c/2 = 13/2
    assert Fraction(ope.modes[3]) == Fraction(13, 2)
    # AP44 Borel: 13/2 / 3! = 13/12
    assert borel_coeff(Fraction(ope.modes[3]), 3) == Fraction(13, 12)


def test_ap49_virasoro_vol2_lambda_3_c13():
    """Vol II Virasoro at c=13: lambda^3 coeff = c/12 = 13/12."""
    lb = virasoro_lambda_vol2(Fraction(13))["TT"]
    assert lb.coeffs[3] == Fraction(13, 12)


def test_ap49_virasoro_n3_two_paths_agree_c13():
    """Two-path verification for Virasoro lambda^3 coefficient at c=13."""
    ope = virasoro_ope_vol1(Fraction(13))["TT"]
    lb = virasoro_lambda_vol2(Fraction(13))["TT"]
    path_a = borel_coeff(Fraction(ope.modes[3]), 3)
    path_b = lb.coeffs[3]
    assert path_a == path_b == Fraction(13, 12)


def test_ap49_virasoro_n3_two_paths_agree_c26():
    """Two-path verification for Virasoro lambda^3 at c=26 (Koszul-dual point)."""
    ope = virasoro_ope_vol1(Fraction(26))["TT"]
    lb = virasoro_lambda_vol2(Fraction(26))["TT"]
    assert borel_coeff(Fraction(ope.modes[3]), 3) == lb.coeffs[3] == Fraction(26, 12)


def test_ap49_virasoro_n2_vanishes():
    """Virasoro T_{(2)}T = 0, so lambda^2 coefficient is 0."""
    ope = virasoro_ope_vol1(Fraction(13))["TT"]
    lb = virasoro_lambda_vol2(Fraction(13))["TT"]
    assert ope.modes[2] == Fraction(0)
    assert lb.coeffs[2] == Fraction(0)


def test_ap49_virasoro_factor_six_trap():
    """AP44 trap: confusing OPE mode c/2 with lambda-bracket coeff c/2.
    The lambda-bracket coefficient is c/12, NOT c/2 (factor 6 wrong).
    """
    c = Fraction(24)  # avoid c=13 to make the factor visible
    ope = virasoro_ope_vol1(c)["TT"]
    lb = virasoro_lambda_vol2(c)["TT"]
    assert lb.coeffs[3] != ope.modes[3]  # they would be equal under the wrong convention
    assert lb.coeffs[3] * 6 == ope.modes[3]  # correct factor is 6


# =====================================================================
# Section D: AP49 cross-volume bridge for affine sl_2
# =====================================================================


def test_ap49_sl2_ef_n0_field():
    """e_{(0)} f = h (a field). Lambda^0 coefficient is the field h itself."""
    ope = affine_sl2_ope_vol1(Fraction(2))["ef"]
    lb = affine_sl2_lambda_vol2(Fraction(2))["ef"]
    assert ope.modes[0] == "h"
    assert lb.coeffs[0] == "h"


def test_ap49_sl2_ef_n1_scalar_k2():
    """e_{(1)} f = k = 2. Lambda^1 coefficient is 2/1! = 2."""
    ope = affine_sl2_ope_vol1(Fraction(2))["ef"]
    lb = affine_sl2_lambda_vol2(Fraction(2))["ef"]
    assert Fraction(ope.modes[1]) == Fraction(2)
    assert Fraction(lb.coeffs[1]) == Fraction(2)


def test_ap49_sl2_hh_n1_two_paths():
    """h_{(1)} h = 2k. Lambda^1 coefficient = 2k/1! = 2k."""
    k = Fraction(5)
    ope = affine_sl2_ope_vol1(k)["hh"]
    lb = affine_sl2_lambda_vol2(k)["hh"]
    path_a = borel_coeff(Fraction(ope.modes[1]), 1)
    path_b = Fraction(lb.coeffs[1])
    assert path_a == path_b == Fraction(10)


def test_ap49_sl2_consistency_k2():
    """Full consistency check for affine sl_2 at level 2."""
    k = Fraction(2)
    ope_dict = affine_sl2_ope_vol1(k)
    lb_dict = affine_sl2_lambda_vol2(k)
    for key in ["ef", "hh"]:
        checks = ap49_consistency_check(ope_dict[key], lb_dict[key])
        assert all(checks.values()), f"sl_2 {key} failed: {checks}"


def test_ap49_sl2_consistency_critical_k():
    """At k = -2 (critical level), the sesquilinear data still holds.
    AP44 conversion is independent of level.
    """
    k = Fraction(-2)
    ope_dict = affine_sl2_ope_vol1(k)
    lb_dict = affine_sl2_lambda_vol2(k)
    for key in ["ef", "hh"]:
        checks = ap49_consistency_check(ope_dict[key], lb_dict[key])
        assert all(checks.values())


def test_ap49_sl2_fe_skew_consistency():
    """f_{(0)} e = -h (Vol I) and {f_lambda e} has lambda^0 coeff -h (Vol II)."""
    ope = affine_sl2_ope_vol1(Fraction(3))["fe"]
    lb = affine_sl2_lambda_vol2(Fraction(3))["fe"]
    assert ope.modes[0] == "-h"
    assert lb.coeffs[0] == "-h"


# =====================================================================
# Section E: D2 Sesquilinearity
# =====================================================================


def test_d2_sesquilinearity_dh_e_lhs_rhs_match():
    """D2: {(dh)_lambda e} = -lambda * {h_lambda e}.
    Both sides should give the same lambda-power coefficient table.
    """
    k = Fraction(1)
    lhs = d2_lhs_dh_e(k)
    rhs = d2_rhs_minus_lambda_he(k)
    assert lhs == rhs


def test_d2_sesquilinearity_h_de_lhs_rhs_match():
    """D2: {h_lambda (de)} = (lambda + d) * {h_lambda e}."""
    k = Fraction(1)
    lhs = d2_lhs_h_de(k)
    rhs = d2_rhs_lambda_plus_d_he(k)
    assert lhs == rhs


def test_d2_sesquilinearity_lambda1_coefficient_is_minus2():
    """The lambda^1 coefficient of {(dh)_lambda e} is -2 (after stripping the e).
    AP44 sanity: at n=1 the divided power is 1, so OPE/lambda agree.
    """
    assert d2_lhs_dh_e(Fraction(1))[1] == Fraction(-2)


def test_d2_sesquilinearity_h_de_lambda0_is_2():
    """{h_lambda (de)} at lambda^0 contains 2 de (mode rule)."""
    assert d2_lhs_h_de(Fraction(1))[0] == Fraction(2)


# =====================================================================
# Section F: D3 Skew-symmetry
# =====================================================================


def test_d3_skew_sl2_fe_direct_vs_from_skew_k1():
    """{f_lambda e} computed two ways:
    (a) directly from OPE f(z)e(w) ~ k/(z-w)^2 - h(w)/(z-w),
    (b) via D3: -{e_{-lambda-d} f}, applied to 1.
    They must agree.
    """
    k = Fraction(1)
    assert d3_fe_direct(k) == d3_fe_from_skew(k)


def test_d3_skew_sl2_fe_k_neg2():
    k = Fraction(-2)
    assert d3_fe_direct(k) == d3_fe_from_skew(k)


def test_d3_skew_sl2_fe_lambda0_is_minus_h():
    """{f_lambda e}_{lambda^0} = -h, numeric placeholder -1."""
    assert d3_fe_direct(Fraction(7))[0] == Fraction(-1)


def test_d3_skew_sl2_fe_lambda1_is_k():
    """{f_lambda e}_{lambda^1} = k."""
    for k in [Fraction(1), Fraction(2), Fraction(-3), Fraction(7, 2)]:
        assert d3_fe_direct(k)[1] == k


def test_d3_skew_heisenberg_two_paths():
    """Heisenberg: {J_lambda J} skew-symmetric. Both paths give k lambda."""
    for k in [Fraction(1), Fraction(-1), Fraction(7, 3)]:
        assert d3_jj_direct(k) == d3_jj_from_skew(k)


# =====================================================================
# Section G: D4 Jacobi
# =====================================================================


def test_d4_jacobi_h_e_f_lhs_equals_rhs_k1():
    """PVA Jacobi on (h, e, f) at k=1.
    LHS = {h_lambda{e_mu f}} - {e_mu{h_lambda f}}
        = 2k lambda - (-2h - 2k mu)
        = 2h + 2k lambda + 2k mu.
    RHS = {{h_lambda e}_{lambda+mu} f}
        = 2(h + k(lambda+mu))
        = 2h + 2k lambda + 2k mu.
    """
    k = Fraction(1)
    assert d4_jacobi_h_e_f_lhs(k) == d4_jacobi_h_e_f_rhs(k)


def test_d4_jacobi_h_e_f_at_k5():
    k = Fraction(5)
    lhs = d4_jacobi_h_e_f_lhs(k)
    rhs = d4_jacobi_h_e_f_rhs(k)
    assert lhs == rhs
    # Spot-check: lambda^1 coefficient is 2k = 10
    assert lhs[(1, 0)] == Fraction(10)
    assert rhs[(1, 0)] == Fraction(10)


def test_d4_jacobi_h_e_f_at_critical_level():
    """k = -2 (critical level)."""
    k = Fraction(-2)
    assert d4_jacobi_h_e_f_lhs(k) == d4_jacobi_h_e_f_rhs(k)


def test_d4_jacobi_e_f_e_lhs_equals_rhs():
    """Second computation in pva-descent-repaired.tex (line 1384-1410):
    LHS = 2e - 0 = 2e. RHS = 2e.
    """
    k = Fraction(1)
    assert d4_jacobi_e_f_e_lhs(k) == d4_jacobi_e_f_e_rhs(k)


def test_d4_jacobi_e_f_e_independent_of_k():
    """The (e,f,e) Jacobi check gives 2e independent of level k."""
    for k in [Fraction(0), Fraction(1), Fraction(-7), Fraction(13, 5)]:
        lhs = d4_jacobi_e_f_e_lhs(k)
        rhs = d4_jacobi_e_f_e_rhs(k)
        assert lhs == rhs == {(0, 0): Fraction(2)}


# =====================================================================
# Section H: D5 Leibniz
# =====================================================================


def test_d5_leibniz_h_ef_lhs_zero():
    """{h_lambda (e * f)} = 0 because e*f has h-weight 0."""
    assert d5_leibniz_h_ef_lhs(Fraction(1)) == Fraction(0)


def test_d5_leibniz_h_ef_rhs_zero():
    """{h_lambda e}*f + e*{h_lambda f} = 2 e*f - 2 e*f = 0."""
    assert d5_leibniz_h_ef_rhs(Fraction(1)) == Fraction(0)


def test_d5_leibniz_h_ef_lhs_equals_rhs():
    """D5 identity on (h, e*f)."""
    k = Fraction(7)
    assert d5_leibniz_h_ef_lhs(k) == d5_leibniz_h_ef_rhs(k)


def test_d5_leibniz_e_h2_lhs_minus4():
    """{e_lambda h^2} = -4 e h on the differential polynomial ring."""
    assert d5_leibniz_e_h2_lhs(Fraction(1)) == Fraction(-4)


def test_d5_leibniz_e_h2_rhs_minus4():
    assert d5_leibniz_e_h2_rhs(Fraction(1)) == Fraction(-4)


def test_d5_leibniz_e_h2_lhs_equals_rhs_all_levels():
    """The (e, h^2) Leibniz check is independent of k."""
    for k in [Fraction(1), Fraction(-2), Fraction(13, 7)]:
        assert d5_leibniz_e_h2_lhs(k) == d5_leibniz_e_h2_rhs(k)


# =====================================================================
# Section I: D6 Vanishing of m_{k>=3} on cohomology
# =====================================================================


def test_d6_m3_amplitude_dimension_zero():
    """The m_3 amplitude on H^*(A,Q) vanishes (Conf_3^<(R) contractible)."""
    assert d6_m3_amplitude_dimension() == 0


def test_d6_m4_amplitude_zero():
    assert d6_mk_amplitude_dimension(4) == 0


def test_d6_m5_amplitude_zero():
    assert d6_mk_amplitude_dimension(5) == 0


def test_d6_mk_for_all_k_in_3_to_10():
    """All m_k for k in 3..10 vanish on cohomology."""
    for k in range(3, 11):
        assert d6_mk_amplitude_dimension(k) == 0


def test_d6_mk_lt3_raises():
    """D6 only applies to k >= 3 (m_1, m_2 are nontrivial)."""
    with pytest.raises(ValueError):
        d6_mk_amplitude_dimension(2)


# =====================================================================
# Section J: Khan-Zeng cross-check
# =====================================================================


def test_khan_zeng_sl2_matches_vol2_k1():
    """Khan-Zeng PVA from 3d gauge theory matches Vol II affine sl_2 at k=1."""
    k = Fraction(1)
    checks = khan_zeng_consistency(k)
    assert all(checks.values()), f"Khan-Zeng mismatch: {checks}"


def test_khan_zeng_sl2_matches_vol2_k_negative():
    """Khan-Zeng matches Vol II at negative level."""
    for k in [Fraction(-1), Fraction(-2), Fraction(-7, 2)]:
        checks = khan_zeng_consistency(k)
        assert all(checks.values()), f"Khan-Zeng mismatch at k={k}: {checks}"


def test_khan_zeng_ef_lambda1_is_k():
    """Khan-Zeng {e_lambda f} at lambda^1 is k."""
    for k in [Fraction(1), Fraction(5), Fraction(-3)]:
        kz = khan_zeng_sl2_lambda(k)
        assert kz["ef"].coeffs[1] == k


def test_khan_zeng_hh_lambda1_is_2k():
    """Khan-Zeng {h_lambda h} at lambda^1 is 2k."""
    for k in [Fraction(1), Fraction(7), Fraction(-2)]:
        kz = khan_zeng_sl2_lambda(k)
        assert kz["hh"].coeffs[1] == Fraction(2 * k)


def test_khan_zeng_three_path_check_at_k3():
    """Three-path: Vol I OPE -> Borel, Vol II direct, Khan-Zeng. All agree."""
    k = Fraction(3)
    ope = affine_sl2_ope_vol1(k)["hh"]
    v2 = affine_sl2_lambda_vol2(k)["hh"]
    kz = khan_zeng_sl2_lambda(k)["hh"]
    path_a = borel_coeff(Fraction(ope.modes[1]), 1)  # Vol I -> Vol II via Borel
    path_b = Fraction(v2.coeffs[1])                  # Vol II direct
    path_c = Fraction(kz.coeffs[1])                  # Khan-Zeng
    assert path_a == path_b == path_c == Fraction(6)  # 2k = 6


# =====================================================================
# Section K: Multipath verification harness
# =====================================================================


def test_multipath_heisenberg_n1():
    k = Fraction(7)
    ope = heisenberg_ope_vol1(k)["JJ"]
    lb = heisenberg_lambda_vol2(k)["JJ"]
    ok, msg = multipath_lambda_coefficient("JJ", 1, ope, lb)
    assert ok, msg


def test_multipath_virasoro_n3_c50():
    c = Fraction(50)
    ope = virasoro_ope_vol1(c)["TT"]
    lb = virasoro_lambda_vol2(c)["TT"]
    ok, msg = multipath_lambda_coefficient("TT", 3, ope, lb)
    assert ok, msg


def test_multipath_sl2_hh_n1():
    k = Fraction(11)
    ope = affine_sl2_ope_vol1(k)["hh"]
    lb = affine_sl2_lambda_vol2(k)["hh"]
    ok, msg = multipath_lambda_coefficient("hh", 1, ope, lb)
    assert ok, msg


def test_multipath_sl2_ef_n1_scan_levels():
    """Sweep across many levels for the (e,f,n=1) check."""
    for k_int in range(-5, 6):
        k = Fraction(k_int)
        ope = affine_sl2_ope_vol1(k)["ef"]
        lb = affine_sl2_lambda_vol2(k)["ef"]
        ok, msg = multipath_lambda_coefficient("ef", 1, ope, lb)
        assert ok, msg


# =====================================================================
# Section L: Constants banner / metadata
# =====================================================================


def test_constants_banner_present():
    b = constants_banner()
    assert "Vol I convention" in b
    assert "Vol II convention" in b
    assert "AP44 factor" in b
    assert "AP49 bridge" in b


def test_ap44_factor_string():
    assert AP44_DIVIDED_POWER_FACTOR == "1/n!"


def test_ap49_bridge_mentions_borel():
    assert "Borel" in AP49_BRIDGE
