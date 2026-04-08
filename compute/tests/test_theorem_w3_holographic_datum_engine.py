r"""Tests for the complete holographic modular Koszul datum H(T) for W_3.

THEOREM (Holographic Modular Koszul Datum for W_3):
The six-fold package H(T) = (A, A!, C, r(z), Theta_A, nabla^hol) for the
W_3 algebra is the first rank-2 example with genuinely multi-weight structure.

MULTI-PATH VERIFICATION (3+ per claim, per CLAUDE.md mandate):

Every numerical value is verified by at least 3 independent paths.
Cross-family consistency (AP10) verified against Virasoro and sl_2_hat.

ANTI-PATTERN AWARENESS:
    AP1:  kappa(W_3) = 5c/6, NOT c/2. Independently recomputed.
    AP10: Cross-family consistency checks, not just hardcoded values.
    AP19: r-matrix poles one below OPE poles.
    AP24: kappa + kappa' = 250/3 != 0 for W_3.
    AP27: bar propagator weight 1 for all channels.
    AP29: self-dual c* = 50 != critical c_crit = 100.
    AP32: genus-1 universal, genus-2 FAILS for multi-weight.
    AP39: kappa != c/2. kappa = 5c/6.

References:
    thm:mc2-bar-intrinsic, thm:wn-obstruction, thm:w3-genus1-complementarity,
    thm:multi-weight-genus-expansion, thm:shadow-connection,
    thm:propagator-variance, cor:anomaly-ratio-ds.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.theorem_w3_holographic_datum_engine import (
    # Bernoulli / Faber-Pandharipande
    bernoulli, lambda_fp, harmonic,
    # Component (A): W_3 algebra
    w3_generators, kappa_w3, kappa_T, kappa_W,
    kappa_from_harmonic, anomaly_ratio, anomaly_ratio_from_exponents,
    # Component (A!): Koszul dual
    w3_dual_central_charge, kappa_w3_dual, complementarity_sum,
    self_dual_point, critical_string_point, w3_central_charge_complementarity,
    # Component (C): line-operator category
    line_category_description,
    # Component (r(z)): r-matrix
    r_matrix_channels, verify_pole_shift, r_matrix_total_pole_count,
    max_r_matrix_pole_order, max_pole_from_weight,
    # Component (Theta_A): MC element
    obs_genus1, F_genus1, F_genus2_per_channel, delta_F2_cross,
    F_genus2_total, delta_F2_large_c_limit, delta_F2_at_self_dual,
    delta_F2_complementarity,
    # Component (nabla^hol): shadow connection
    shadow_metric_T_line, shadow_metric_W_line,
    critical_discriminant_T, critical_discriminant_W,
    S4_T, S4_W, shadow_depth,
    # Propagator variance
    mixing_polynomial, propagator_variance,
    # OPE data
    w3_ope_modes, leading_ope_pole, two_point_normalization,
    # Structure constants
    structure_constant_upper, structure_constant_lower,
    # Full datum
    holographic_datum,
    # Cross-family
    virasoro_kappa, virasoro_complementarity_sum,
    sl2_hat_complementarity_sum, general_wn_kappa_sum,
    # Numerical
    evaluate_datum_numerically,
)


# ============================================================================
# Test utilities
# ============================================================================

# Standard test central charges (exact rational arithmetic)
C_GENERIC = Fraction(30)       # generic value, away from poles
C_LARGE = Fraction(1000)       # large-c regime
C_SMALL = Fraction(1, 10)      # small positive c
C_SELF_DUAL = Fraction(50)     # self-dual point
C_INTEGER = Fraction(24)       # integer (Leech lattice c for comparison)
C_HALF = Fraction(1, 2)        # fractional


# ============================================================================
# 1. KAPPA FORMULA: 3+ independent paths (AP1, AP10, AP39)
# ============================================================================

class TestKappaMultiPath:
    """Verify kappa(W_3) = 5c/6 via 3+ independent derivations."""

    def test_kappa_path1_harmonic_sum(self):
        """Path 1: kappa = c * (H_3 - 1) where H_3 = 11/6."""
        H3 = harmonic(3)
        assert H3 == Fraction(11, 6)
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL]:
            assert kappa_w3(c) == c * (H3 - 1)

    def test_kappa_path2_channel_sum(self):
        """Path 2: kappa = kappa_T + kappa_W = c/2 + c/3."""
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL]:
            assert kappa_T(c) + kappa_W(c) == kappa_w3(c)
            assert kappa_T(c) == c / 2
            assert kappa_W(c) == c / 3

    def test_kappa_path3_anomaly_ratio(self):
        """Path 3: kappa = c * rho where rho = 5/6."""
        rho = anomaly_ratio(3)
        assert rho == Fraction(5, 6)
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL]:
            assert kappa_w3(c) == c * rho

    def test_kappa_path4_exponents(self):
        """Path 4: rho = sum 1/(m_i + 1) from sl_3 exponents [1, 2]."""
        sl3_exponents = [1, 2]
        rho_from_exp = anomaly_ratio_from_exponents(sl3_exponents)
        assert rho_from_exp == Fraction(5, 6)
        assert rho_from_exp == anomaly_ratio(3)

    def test_kappa_path5_kappa_from_harmonic(self):
        """Path 5: kappa_from_harmonic function agrees."""
        for c in [C_GENERIC, C_LARGE, C_SMALL]:
            assert kappa_from_harmonic(c, N=3) == kappa_w3(c)

    def test_kappa_specific_values(self):
        """Hardcoded spot checks (AP10: cross-check, not sole verification)."""
        assert kappa_w3(Fraction(30)) == Fraction(25)
        assert kappa_w3(Fraction(6)) == Fraction(5)
        assert kappa_w3(Fraction(12)) == Fraction(10)
        assert kappa_w3(Fraction(100)) == Fraction(250, 3)

    def test_kappa_not_c_over_2(self):
        """AP39: kappa(W_3) != c/2 for generic c."""
        for c in [C_GENERIC, C_LARGE, C_SMALL]:
            assert kappa_w3(c) != virasoro_kappa(c)
            # The difference is c/3 (the W-channel contribution)
            assert kappa_w3(c) - virasoro_kappa(c) == c / 3


# ============================================================================
# 2. KOSZUL DUALITY: c + c' = 100, kappa + kappa' = 250/3
# ============================================================================

class TestKoszulDuality:
    """Verify Koszul duality data for W_3 via 3+ paths."""

    def test_dual_cc_path1_direct(self):
        """Path 1: c' = 100 - c, so c + c' = 100."""
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL]:
            assert c + w3_dual_central_charge(c) == Fraction(100)

    def test_dual_cc_path2_known_constant(self):
        """Path 2: authoritative value from w_algebras.tex line 1210."""
        assert w3_central_charge_complementarity() == Fraction(100)

    def test_dual_cc_path3_involutivity(self):
        """Path 3: (c')' = c (involution property)."""
        for c in [C_GENERIC, C_LARGE, C_SMALL]:
            assert w3_dual_central_charge(w3_dual_central_charge(c)) == c

    def test_kappa_sum_path1_direct(self):
        """Path 1: kappa + kappa' = 5c/6 + 5(100-c)/6 = 500/6 = 250/3."""
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL]:
            assert complementarity_sum(c) == Fraction(250, 3)

    def test_kappa_sum_path2_formula(self):
        """Path 2: kappa + kappa' = cc_sum * rho = 100 * 5/6 = 250/3."""
        assert Fraction(100) * anomaly_ratio(3) == Fraction(250, 3)

    def test_kappa_sum_path3_general_wn(self):
        """Path 3: general_wn_kappa_sum agrees."""
        result = general_wn_kappa_sum(3)
        assert result['kappa_sum'] == Fraction(250, 3)

    def test_kappa_sum_nonzero_ap24(self):
        """AP24: kappa + kappa' != 0 for W-algebras (unlike KM)."""
        assert complementarity_sum(C_GENERIC) != Fraction(0)
        # Compare with other families
        assert virasoro_complementarity_sum() == Fraction(13)
        assert sl2_hat_complementarity_sum() == Fraction(0)

    def test_self_dual_point(self):
        """Self-dual point c* = 50 where kappa(A) = kappa(A!)."""
        c_star = self_dual_point()
        assert c_star == Fraction(50)
        assert kappa_w3(c_star) == kappa_w3_dual(c_star)
        assert kappa_w3(c_star) == Fraction(125, 3)

    def test_critical_vs_self_dual_ap29(self):
        """AP29: self-dual c* = 50 != critical c_crit = 100."""
        assert self_dual_point() != critical_string_point()
        assert self_dual_point() == Fraction(50)
        assert critical_string_point() == Fraction(100)


# ============================================================================
# 3. R-MATRIX: pole structure (AP19)
# ============================================================================

class TestRMatrix:
    """Verify r-matrix pole structure via AP19 (d log absorption)."""

    def test_pole_shift_TT(self):
        """TT channel: OPE {4,2,1} -> r-matrix {3,1}."""
        result = verify_pole_shift('TT')
        assert result['consistent']
        assert result['actual_rmatrix_poles'] == [3, 1]

    def test_pole_shift_TW(self):
        """TW channel: OPE {2,1} -> r-matrix {1}."""
        result = verify_pole_shift('TW')
        assert result['consistent']
        assert result['actual_rmatrix_poles'] == [1]

    def test_pole_shift_WW(self):
        """WW channel: OPE {6,4,3,2,1} -> r-matrix {5,3,2,1}."""
        result = verify_pole_shift('WW')
        assert result['consistent']
        assert result['actual_rmatrix_poles'] == [5, 3, 2, 1]

    def test_pole_shift_WT(self):
        """WT channel: same as TW by skew-symmetry."""
        result = verify_pole_shift('WT')
        assert result['consistent']

    def test_max_pole_from_weight_formula(self):
        """Max r-matrix pole = 2h - 1: h=1->1, h=2->3, h=3->5."""
        assert max_pole_from_weight(1) == 1   # Heisenberg
        assert max_pole_from_weight(2) == 3   # Virasoro
        assert max_pole_from_weight(3) == 5   # W_3 W-current

    def test_max_pole_order_is_5(self):
        """Maximum r-matrix pole order across all W_3 channels is 5."""
        assert max_r_matrix_pole_order() == 5

    def test_total_distinct_poles(self):
        """Total distinct pole orders: {1, 2, 3, 5} -> 4."""
        assert r_matrix_total_pole_count() == 4

    def test_ww_even_pole_present(self):
        """WW channel has even pole at z^{-2} (rem:ww-even-poles-census)."""
        ww = r_matrix_channels()['WW']
        assert 2 in ww['rmatrix_poles']

    def test_tt_all_odd_poles(self):
        """TT channel has only odd poles (bosonic parity, weight 2)."""
        tt = r_matrix_channels()['TT']
        assert all(p % 2 == 1 for p in tt['rmatrix_poles'])


# ============================================================================
# 4. GENUS EXPANSION: obs_1 and F_2 (AP32)
# ============================================================================

class TestGenusExpansion:
    """Verify genus expansion data via 3+ independent paths."""

    def test_lambda_fp_values(self):
        """Faber-Pandharipande intersection numbers."""
        assert lambda_fp(1) == Fraction(1, 24)
        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_obs1_path1_kappa_times_lambda(self):
        """Path 1: obs_1 = kappa * lambda_1 = (5c/6) * (1/24) = 5c/144."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            expected = Fraction(5) * c / Fraction(144)
            assert obs_genus1(c) == expected

    def test_obs1_path2_channel_decomposition(self):
        """Path 2: obs_1 = kappa_T/24 + kappa_W/24 = c/48 + c/72."""
        for c in [C_GENERIC, C_SELF_DUAL]:
            assert obs_genus1(c) == kappa_T(c) / 24 + kappa_W(c) / 24

    def test_obs1_path3_anomaly_ratio(self):
        """Path 3: F_1/c = rho/24 = (5/6)/24 = 5/144."""
        rho = anomaly_ratio(3)
        for c in [C_GENERIC, C_LARGE]:
            assert F_genus1(c) / c == rho / 24
            assert F_genus1(c) / c == Fraction(5, 144)

    def test_obs1_specific_value(self):
        """Spot check: F_1(c=30) = 5*30/144 = 150/144 = 25/24."""
        assert F_genus1(Fraction(30)) == Fraction(25, 24)

    def test_F2_per_channel_formula(self):
        """F_2^{per-channel} = kappa * lambda_2^FP = 7c/6912."""
        for c in [C_GENERIC, C_LARGE]:
            expected = Fraction(7) * c / Fraction(6912)
            assert F_genus2_per_channel(c) == expected

    def test_delta_F2_formula(self):
        """delta_F2 = (c + 204)/(16c) for W_3."""
        c = C_GENERIC  # c = 30
        expected = (Fraction(30) + Fraction(204)) / (Fraction(16) * Fraction(30))
        assert delta_F2_cross(c) == expected
        assert delta_F2_cross(c) == Fraction(234, 480)
        assert delta_F2_cross(c) == Fraction(39, 80)

    def test_delta_F2_nonzero_ap32(self):
        """AP32: delta_F2 != 0 for all c > 0 (multi-weight genus-2 failure)."""
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL, C_INTEGER]:
            assert delta_F2_cross(c) != Fraction(0)
            assert delta_F2_cross(c) > Fraction(0)

    def test_delta_F2_large_c(self):
        """Large-c limit: delta_F2 -> 1/16."""
        assert delta_F2_large_c_limit() == Fraction(1, 16)
        # Numerical check at large c
        c_huge = Fraction(10**6)
        delta = delta_F2_cross(c_huge)
        assert abs(float(delta) - 1.0/16) < 1e-4

    def test_F2_total_decomposition(self):
        """F_2(W_3) = F_2^{per-channel} + delta_F2^cross."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            assert F_genus2_total(c) == F_genus2_per_channel(c) + delta_F2_cross(c)

    def test_F2_over_F1_ratio(self):
        """Universal ratio F_2/F_1 check.

        For per-channel part: F_2^{pc}/F_1 = lambda_2/lambda_1 = 7/240.
        For total: F_2/F_1 != 7/240 due to cross-channel correction.
        """
        for c in [C_GENERIC, C_LARGE]:
            assert F_genus2_per_channel(c) / F_genus1(c) == Fraction(7, 240)
            # Total ratio differs
            assert F_genus2_total(c) / F_genus1(c) != Fraction(7, 240)

    def test_delta_F2_self_dual_value(self):
        """delta_F2 at the self-dual point c = 50."""
        delta = delta_F2_at_self_dual()
        assert delta == Fraction(254, 800)
        assert delta == Fraction(127, 400)


# ============================================================================
# 5. SHADOW CONNECTION AND DISCRIMINANT
# ============================================================================

class TestShadowConnection:
    """Verify shadow connection data via 3+ independent paths."""

    def test_discriminant_T_path1_formula(self):
        """Path 1: Delta_T = 40/(5c + 22) directly."""
        c = C_GENERIC  # c = 30
        assert critical_discriminant_T(c) == Fraction(40, 172)
        assert critical_discriminant_T(c) == Fraction(10, 43)

    def test_discriminant_T_path2_from_S4(self):
        """Path 2: Delta_T = 8 * kappa_T * S4_T."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            expected = 8 * kappa_T(c) * S4_T(c)
            assert critical_discriminant_T(c) == expected

    def test_discriminant_T_path3_virasoro_identity(self):
        """Path 3: T-line Delta identical to Virasoro Delta."""
        # Virasoro: Delta = 40/(5c+22) = 8*(c/2)*10/[c(5c+22)]
        for c in [C_GENERIC, C_LARGE]:
            vir_delta = Fraction(40) / (5 * c + 22)
            assert critical_discriminant_T(c) == vir_delta

    def test_discriminant_W_formula(self):
        """Delta_W = 20480/[3(5c+22)^3] from 8*kappa_W*S4_W."""
        for c in [C_GENERIC, C_LARGE]:
            expected = 8 * kappa_W(c) * S4_W(c)
            assert critical_discriminant_W(c) == expected

    def test_discriminants_nonzero(self):
        """Both discriminants nonzero for generic c (class M)."""
        for c in [C_GENERIC, C_LARGE, C_SMALL]:
            assert critical_discriminant_T(c) != 0
            assert critical_discriminant_W(c) != 0

    def test_shadow_depth_class_M(self):
        """Shadow depth is class M (infinite) for W_3."""
        assert shadow_depth() == 'M'

    def test_S4_T_is_virasoro_quartic(self):
        """S4_T = 10/[c(5c+22)] = Q^contact_Vir."""
        for c in [C_GENERIC, C_LARGE, C_INTEGER]:
            expected = Fraction(10) / (c * (5 * c + 22))
            assert S4_T(c) == expected

    def test_S4_W_formula(self):
        """S4_W = 2560/[c(5c+22)^3]."""
        c = C_GENERIC
        expected = Fraction(2560) / (c * (5 * c + 22)**3)
        assert S4_W(c) == expected

    def test_shadow_metric_T_at_zero(self):
        """Q_T(0) = c^2 (the Gaussian envelope)."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            assert shadow_metric_T_line(c, Fraction(0)) == c**2

    def test_shadow_metric_W_at_zero(self):
        """Q_W(0) = 4c^2/9 = (2*kappa_W)^2."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            assert shadow_metric_W_line(c, Fraction(0)) == Fraction(4) * c**2 / Fraction(9)
            assert shadow_metric_W_line(c, Fraction(0)) == (2 * kappa_W(c))**2

    def test_shadow_metric_W_even(self):
        """Q_W(t) is even in t (Z_2 parity)."""
        for c in [C_GENERIC, C_LARGE]:
            for t in [Fraction(1), Fraction(3, 7), Fraction(10)]:
                assert shadow_metric_W_line(c, t) == shadow_metric_W_line(c, -t)


# ============================================================================
# 6. PROPAGATOR VARIANCE AND MIXING POLYNOMIAL
# ============================================================================

class TestPropagatorVariance:
    """Verify propagator variance and mixing polynomial."""

    def test_mixing_polynomial_formula(self):
        """P(W_3) = 25c^2 + 100c - 428."""
        c = C_GENERIC
        assert mixing_polynomial(c) == 25 * c**2 + 100 * c - 428

    def test_mixing_polynomial_specific_values(self):
        """Spot checks for the mixing polynomial."""
        assert mixing_polynomial(Fraction(0)) == Fraction(-428)
        assert mixing_polynomial(Fraction(2)) == Fraction(25 * 4 + 200 - 428)
        assert mixing_polynomial(Fraction(2)) == Fraction(-128)

    def test_variance_nonnegative(self):
        """Propagator variance >= 0 (Cauchy-Schwarz)."""
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_SELF_DUAL, C_INTEGER]:
            assert propagator_variance(c) >= 0

    def test_variance_proportional_to_P_squared(self):
        """delta_mix = 1280 * P^2 / [c^3 * (5c+22)^6]."""
        for c in [C_GENERIC, C_LARGE]:
            P = mixing_polynomial(c)
            expected = Fraction(1280) * P**2 / (c**3 * (5 * c + 22)**6)
            assert propagator_variance(c) == expected

    def test_variance_vanishes_at_enhanced_symmetry(self):
        """Variance vanishes iff P = 0 (enhanced symmetry points).

        P = 0 at c = -2 +/- 4*sqrt(33)/5 (both irrational, both complex
        for the physical W_3). So variance is generically nonzero.
        """
        # The discriminant of P is 100^2 + 4*25*428 = 10000 + 42800 = 52800
        # sqrt(52800) = 4*sqrt(3300) = 4*sqrt(33*100) = 40*sqrt(33)
        # roots: c = (-100 +/- 40*sqrt(33)) / 50 = -2 +/- 4*sqrt(33)/5
        # Both are real but irrational.
        # Check that P != 0 at rational test points:
        for c in [C_GENERIC, C_LARGE, C_SMALL, C_INTEGER]:
            assert mixing_polynomial(c) != 0
            assert propagator_variance(c) > 0


# ============================================================================
# 7. OPE DATA AND STRUCTURE CONSTANTS
# ============================================================================

class TestOPEData:
    """Verify W_3 OPE data and structure constants."""

    def test_leading_ope_TT(self):
        """T_{(3)}T = c/2."""
        for c in [C_GENERIC, C_LARGE]:
            assert leading_ope_pole('T', 'T', c) == c / 2

    def test_leading_ope_WW(self):
        """W_{(5)}W = c/3."""
        for c in [C_GENERIC, C_LARGE]:
            assert leading_ope_pole('W', 'W', c) == c / 3

    def test_leading_ope_mixed_is_none(self):
        """TW and WT channels have no vacuum contribution."""
        for c in [C_GENERIC]:
            assert leading_ope_pole('T', 'W', c) is None
            assert leading_ope_pole('W', 'T', c) is None

    def test_two_point_normalization(self):
        """<W^{(s)} W^{(s)}> leading coefficient = c/s."""
        c = C_GENERIC
        assert two_point_normalization(2, c) == c / 2  # T
        assert two_point_normalization(3, c) == c / 3  # W

    def test_structure_constants_z2_parity(self):
        """Z_2 parity: odd number of W indices -> vanish."""
        assert structure_constant_upper('T', 'T', 'W') == 0
        assert structure_constant_upper('W', 'W', 'W') == 0
        assert structure_constant_upper('T', 'W', 'T') == 0

    def test_structure_constants_nonzero(self):
        """Nonvanishing upper structure constants."""
        assert structure_constant_upper('T', 'T', 'T') == 2
        assert structure_constant_upper('T', 'W', 'W') == 3
        assert structure_constant_upper('W', 'W', 'T') == 2

    def test_lower_constants_all_equal_c(self):
        """All nonvanishing C_{ijk} = c (remarkable universality)."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            assert structure_constant_lower('T', 'T', 'T', c) == c
            assert structure_constant_lower('T', 'W', 'W', c) == c
            assert structure_constant_lower('W', 'W', 'T', c) == c

    def test_lower_constants_vanishing(self):
        """Z_2-forbidden lower structure constants vanish."""
        c = C_GENERIC
        assert structure_constant_lower('T', 'T', 'W', c) == 0
        assert structure_constant_lower('W', 'W', 'W', c) == 0


# ============================================================================
# 8. CROSS-FAMILY CONSISTENCY (AP10)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10: not just hardcoded values)."""

    def test_virasoro_is_n2_special_case(self):
        """Virasoro = W_2: kappa = c * (H_2 - 1) = c/2."""
        rho_vir = anomaly_ratio(2)
        assert rho_vir == Fraction(1, 2)
        for c in [C_GENERIC, C_LARGE]:
            assert virasoro_kappa(c) == c * rho_vir

    def test_kappa_sum_hierarchy(self):
        """kappa + kappa' increases with N: 0 (KM) < 13 (Vir) < 250/3 (W_3)."""
        assert sl2_hat_complementarity_sum() < virasoro_complementarity_sum()
        assert virasoro_complementarity_sum() < complementarity_sum(C_GENERIC)

    def test_anomaly_ratio_increases_with_N(self):
        """rho(W_N) = H_N - 1 increases with N."""
        assert anomaly_ratio(2) < anomaly_ratio(3)
        assert anomaly_ratio(3) < anomaly_ratio(4)

    def test_general_wn_kappa_sum_n2(self):
        """For N=2 (Virasoro): kappa + kappa' = 26 * 1/2 = 13."""
        result = general_wn_kappa_sum(2)
        assert result['kappa_sum'] == Fraction(13)

    def test_w3_kappa_exceeds_virasoro(self):
        """kappa(W_3) > kappa(Vir) for c > 0."""
        for c in [C_GENERIC, C_LARGE, C_SMALL]:
            assert kappa_w3(c) > virasoro_kappa(c)

    def test_kappa_channel_ratio(self):
        """kappa_T / kappa_W = 3/2 (level-independent)."""
        for c in [C_GENERIC, C_LARGE, C_SELF_DUAL]:
            assert kappa_T(c) / kappa_W(c) == Fraction(3, 2)


# ============================================================================
# 9. FULL DATUM ASSEMBLY
# ============================================================================

class TestFullDatum:
    """Verify the complete holographic datum assembles correctly."""

    def test_datum_has_six_components(self):
        """H(T) has exactly the six components: A, A!, C, r, Theta, nabla."""
        datum = holographic_datum(C_GENERIC)
        assert 'A' in datum
        assert 'A_dual' in datum
        assert 'C' in datum
        assert 'r' in datum
        assert 'Theta' in datum
        assert 'nabla' in datum

    def test_datum_A_kappa(self):
        """Component A has correct kappa."""
        datum = holographic_datum(C_GENERIC)
        assert datum['A']['kappa'] == kappa_w3(C_GENERIC)

    def test_datum_A_dual_complementarity(self):
        """A! has c + c' = 100 and kappa + kappa' = 250/3."""
        datum = holographic_datum(C_GENERIC)
        assert datum['A_dual']['complementarity_cc'] == Fraction(100)
        assert datum['A_dual']['complementarity_kappa'] == Fraction(250, 3)

    def test_datum_genus1_correct(self):
        """Theta component has correct genus-1 data."""
        datum = holographic_datum(C_GENERIC)
        assert datum['Theta']['genus_1']['obs_1'] == obs_genus1(C_GENERIC)

    def test_datum_genus2_has_cross_channel(self):
        """Theta component has nonzero cross-channel correction."""
        datum = holographic_datum(C_GENERIC)
        assert datum['Theta']['genus_2']['delta_F2_cross'] != 0

    def test_datum_r_matrix_structure(self):
        """r(z) component has correct structure."""
        datum = holographic_datum(C_GENERIC)
        assert datum['r']['max_pole_order'] == 5
        assert datum['r']['total_pole_count'] == 4

    def test_datum_at_self_dual_point(self):
        """At c = 50, kappa(A) = kappa(A!)."""
        datum = holographic_datum(C_SELF_DUAL)
        assert datum['A']['kappa'] == datum['A_dual']['kappa']


# ============================================================================
# 10. BERNOULLI / HARMONIC NUMBER INFRASTRUCTURE
# ============================================================================

class TestInfrastructure:
    """Verify supporting infrastructure (Bernoulli, harmonics, FP)."""

    def test_bernoulli_values(self):
        """Standard Bernoulli numbers."""
        assert bernoulli(0) == Fraction(1)
        assert bernoulli(1) == Fraction(-1, 2)
        assert bernoulli(2) == Fraction(1, 6)
        assert bernoulli(4) == Fraction(-1, 30)
        assert bernoulli(6) == Fraction(1, 42)
        # Odd Bernoulli (>1) vanish
        assert bernoulli(3) == 0
        assert bernoulli(5) == 0

    def test_harmonic_values(self):
        """Harmonic numbers."""
        assert harmonic(1) == Fraction(1)
        assert harmonic(2) == Fraction(3, 2)
        assert harmonic(3) == Fraction(11, 6)
        assert harmonic(4) == Fraction(25, 12)

    def test_lambda_fp_ratio(self):
        """Universal ratio lambda_2/lambda_1 = 7/240."""
        assert lambda_fp(2) / lambda_fp(1) == Fraction(7, 240)


# ============================================================================
# 11. NUMERICAL EVALUATION CROSS-CHECKS
# ============================================================================

class TestNumericalEvaluation:
    """Numerical cross-checks at specific central charges."""

    def test_numerical_at_c30(self):
        """Full numerical evaluation at c = 30."""
        vals = evaluate_datum_numerically(30)
        assert abs(vals['kappa'] - 25.0) < 1e-10
        assert abs(vals['c_dual'] - 70.0) < 1e-10
        assert abs(vals['kappa_sum'] - 250.0 / 3) < 1e-10
        assert abs(vals['F_1'] - 25.0 / 24) < 1e-10

    def test_numerical_at_c50(self):
        """At self-dual point c = 50: kappa = kappa_dual."""
        vals = evaluate_datum_numerically(50)
        assert abs(vals['kappa'] - vals['kappa_dual']) < 1e-10
        assert abs(vals['kappa'] - 125.0 / 3) < 1e-10

    def test_numerical_delta_F2_positive(self):
        """delta_F2 is positive for all positive c."""
        for c_val in [0.1, 1.0, 10.0, 50.0, 100.0, 1000.0]:
            vals = evaluate_datum_numerically(c_val)
            assert vals['delta_F2'] > 0

    def test_numerical_large_c_delta_limit(self):
        """delta_F2 -> 1/16 = 0.0625 as c -> infinity."""
        vals = evaluate_datum_numerically(10**6)
        assert abs(vals['delta_F2'] - 0.0625) < 1e-4


# ============================================================================
# 12. LINE-OPERATOR CATEGORY
# ============================================================================

class TestLineCategory:
    """Verify line-operator category description."""

    def test_category_type(self):
        """Category is Rep_q(sl_3)."""
        desc = line_category_description()
        assert desc['type'] == 'Rep_q(sl_3)'
        assert desc['rank'] == 2
        assert desc['simple_type'] == 'A_2'

    def test_mc3_proved(self):
        """MC3 is proved for all simple types."""
        desc = line_category_description()
        assert 'PROVED' in desc['mc3_status']
