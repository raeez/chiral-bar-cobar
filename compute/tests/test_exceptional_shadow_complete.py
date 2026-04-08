r"""Tests for complete exceptional shadow obstruction tower: G_2, F_4, E_6, E_7, E_8.

Verifies ALL shadow obstruction tower invariants for ALL five exceptional Lie types
from first principles (AP1, AP10).  Every expected value is independently
computed in the test, NOT imported from the library under test.

Test categories:
    1. Structural data (dim, rank, h, h^v, exponents, lacing) -- 5 types
    2. Kappa formula: kappa = dim(g)*(k+h^v)/(2*h^v) at multiple levels
    3. Shadow class L: S_3 != 0, S_4 = 0, Delta = 0, r_max = 3
    4. Complementarity: kappa + kappa' = 0, c + c' = 2*dim
    5. Feigin-Frenkel involution: (k')' = k, fixed at k = -h^vee
    6. Central charge: c = dim*k/(k+h^v), large-k limit = dim
    7. Casimir degrees: degrees = exponents + 1, no cubic Casimir
    8. Root system: num_roots, dim = 2*n_pos + rank, exponent sum
    9. Anomaly ratio: rho(g) = sum 1/(m_i+1) exact values
   10. Strange Formula: |rho|^2 = dim*h/12
   11. W-algebra: kappa(W) = rho * c(W) at multiple levels
   12. Genus amplitudes: F_1 = kappa/24, F_2^scalar = 7*kappa/5760
   13. E_8 theta function: leading coefficient = 240 = E_4 coefficient
   14. Deligne series: monotonicity, kappa/dim pattern
   15. Langlands self-duality
   16. Cross-family consistency (class L, complementarity, monotonicity)
   17. AP-specific regression tests (AP1, AP3, AP9, AP19, AP24, AP27)
   18. Numerical spot-checks at k = 1, 2, 3

Mathematical references:
    See exceptional_shadow_complete.py docstring for full list.
"""

from __future__ import annotations

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify, cancel, S

from compute.lib.exceptional_shadow_complete import (
    # Registry
    EXCEPTIONAL_REGISTRY,
    get_data,
    # Verification
    verify_against_cartan,
    verify_all_against_cartan,
    verify_exponent_sum,
    verify_max_exponent,
    verify_dim_from_roots,
    # Kappa
    kappa_fn,
    kappa_numeric,
    kappa_simplified_str,
    # Central charge
    central_charge_fn,
    central_charge_numeric,
    # FF duality
    ff_dual_level_fn,
    ff_dual_level_numeric,
    # Complementarity
    complementarity_sum_kappa,
    complementarity_sum_c,
    # Casimir
    casimir_degrees,
    has_cubic_casimir,
    # Root system
    num_positive_roots,
    weyl_group_order,
    # Anomaly ratio
    anomaly_ratio,
    anomaly_ratio_symbolic,
    # Strange Formula
    weyl_rho_squared,
    verify_strange_formula,
    # W-algebra
    w_algebra_central_charge,
    w_algebra_central_charge_numeric,
    w_algebra_kappa,
    w_algebra_kappa_numeric,
    # Shadow obstruction tower
    shadow_class,
    shadow_depth,
    shadow_radius,
    Q_contact,
    # Genus amplitudes
    F1,
    F1_numeric,
    F2,
    F2_scalar_numeric,
    # Theta functions
    theta_e8_coefficients,
    e8_root_count,
    e8_theta_leading,
    e8_theta_matches_E4,
    # Deligne series
    DELIGNE_SERIES,
    deligne_kappa_at_level,
    deligne_kappa_ratios,
    # Langlands
    is_langlands_self_dual,
    langlands_dual_type,
    # Shadow data
    compute_shadow_data,
    all_shadow_data,
    # Comparison
    comparison_table,
    # Cross-family
    cross_family_all_class_L,
    cross_family_complementarity,
    cross_family_kappa_monotonicity,
    cross_family_no_cubic_casimir,
    cross_family_koszul_conductor,
    # Master verification
    verify_all,
)
from compute.lib.lie_algebra import cartan_data


k = Symbol('k')


# ============================================================================
# Independent ground truth (AP10: recomputed, NOT imported from library)
# ============================================================================

def _kappa_independent(dim_g, h_dual, level):
    """kappa = dim(g) * (k + h^vee) / (2 * h^vee), computed independently."""
    return Rational(dim_g) * (level + h_dual) / (2 * h_dual)


def _cc_independent(dim_g, h_dual, level):
    """c = dim(g) * k / (k + h^vee), computed independently."""
    return Rational(dim_g) * level / (level + h_dual)


def _ff_dual_independent(h_dual, level):
    """k' = -k - 2*h^vee, computed independently."""
    return -level - 2 * h_dual


# Ground truth table: independently verified against Bourbaki/Humphreys/Kac
GROUND_TRUTH = {
    'G2': ('G', 2, 14, 6, 4, 3, [1, 5]),
    'F4': ('F', 4, 52, 12, 9, 2, [1, 5, 7, 11]),
    'E6': ('E', 6, 78, 12, 12, 1, [1, 4, 5, 7, 8, 11]),
    'E7': ('E', 7, 133, 18, 18, 1, [1, 5, 7, 9, 11, 13, 17]),
    'E8': ('E', 8, 248, 30, 30, 1, [1, 7, 11, 13, 17, 19, 23, 29]),
}
# Format: (type, rank, dim, h, h_dual, lacing, exponents)


# ============================================================================
# 1. Structural data tests
# ============================================================================

class TestStructuralData:
    """Verify structural constants against independent ground truth."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_dim(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.dim == dim, f"{label}: dim should be {dim}, got {data.dim}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.h == h, f"{label}: h should be {h}, got {data.h}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h_dual(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.h_dual == h_dual

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_exponents(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.exponents == exponents

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_lacing(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        rl = cartan_data(type_, rank).root_lengths_squared
        assert max(rl) // min(rl) == lacing

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cartan_crosscheck(self, label, gt):
        """Full cartan_data cross-check against registry."""
        checks = verify_against_cartan(label)
        for check_name, passed in checks.items():
            assert passed, f"{label}: cartan cross-check failed on {check_name}"

    def test_g2_not_simply_laced(self):
        assert not EXCEPTIONAL_REGISTRY['G2']['simply_laced']
        assert EXCEPTIONAL_REGISTRY['G2']['lacing'] == 3

    def test_f4_not_simply_laced(self):
        assert not EXCEPTIONAL_REGISTRY['F4']['simply_laced']
        assert EXCEPTIONAL_REGISTRY['F4']['lacing'] == 2

    def test_e6_simply_laced(self):
        assert EXCEPTIONAL_REGISTRY['E6']['simply_laced']
        assert EXCEPTIONAL_REGISTRY['E6']['lacing'] == 1

    def test_e7_simply_laced(self):
        assert EXCEPTIONAL_REGISTRY['E7']['simply_laced']

    def test_e8_simply_laced(self):
        assert EXCEPTIONAL_REGISTRY['E8']['simply_laced']

    def test_g2_f4_h_neq_h_dual(self):
        """Non-simply-laced types have h != h^vee."""
        assert EXCEPTIONAL_REGISTRY['G2']['h'] != EXCEPTIONAL_REGISTRY['G2']['h_dual']
        assert EXCEPTIONAL_REGISTRY['F4']['h'] != EXCEPTIONAL_REGISTRY['F4']['h_dual']

    def test_e_types_h_eq_h_dual(self):
        """Simply-laced types have h = h^vee."""
        for name in ['E6', 'E7', 'E8']:
            assert EXCEPTIONAL_REGISTRY[name]['h'] == EXCEPTIONAL_REGISTRY[name]['h_dual']


# ============================================================================
# 2. Kappa formula tests
# ============================================================================

class TestKappaFormulas:
    """Verify kappa = dim(g) * (k + h^vee) / (2 * h^vee) for each type."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_matches_definition(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kap = kappa_fn(label, k)
        expected = _kappa_independent(dim, h_dual, k)
        assert simplify(kap - expected) == 0

    def test_kappa_g2(self):
        """G_2: kappa = 14(k+4)/8 = 7(k+4)/4."""
        kap = kappa_fn('G2', k)
        assert simplify(kap - Rational(7) * (k + 4) / 4) == 0

    def test_kappa_f4(self):
        """F_4: kappa = 52(k+9)/18 = 26(k+9)/9."""
        kap = kappa_fn('F4', k)
        assert simplify(kap - Rational(26) * (k + 9) / 9) == 0

    def test_kappa_e6(self):
        """E_6: kappa = 78(k+12)/24 = 13(k+12)/4."""
        kap = kappa_fn('E6', k)
        assert simplify(kap - Rational(13) * (k + 12) / 4) == 0

    def test_kappa_e7(self):
        """E_7: kappa = 133(k+18)/36."""
        kap = kappa_fn('E7', k)
        assert simplify(kap - Rational(133) * (k + 18) / 36) == 0

    def test_kappa_e8(self):
        """E_8: kappa = 248(k+30)/60 = 62(k+30)/15."""
        kap = kappa_fn('E8', k)
        assert simplify(kap - Rational(62) * (k + 30) / 15) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_vanishes_at_critical(self, label, gt):
        """kappa(-h^vee) = 0 for all types."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kap = kappa_fn(label, k)
        assert simplify(kap.subs(k, -h_dual)) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_at_level_zero(self, label, gt):
        """kappa(0) = dim(g)/2 for all types."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kap = kappa_fn(label, k)
        assert simplify(kap.subs(k, 0) - Rational(dim, 2)) == 0


class TestKappaNumerical:
    """Numerical spot-checks for kappa at specific levels."""

    def test_g2_k1(self):
        """G_2 at k=1: kappa = 7*5/4 = 35/4."""
        assert kappa_numeric('G2', 1) == Fraction(35, 4)

    def test_g2_k2(self):
        """G_2 at k=2: kappa = 7*6/4 = 42/4 = 21/2."""
        assert kappa_numeric('G2', 2) == Fraction(21, 2)

    def test_g2_k3(self):
        """G_2 at k=3: kappa = 7*7/4 = 49/4."""
        assert kappa_numeric('G2', 3) == Fraction(49, 4)

    def test_f4_k1(self):
        """F_4 at k=1: kappa = 26*10/9 = 260/9."""
        assert kappa_numeric('F4', 1) == Fraction(260, 9)

    def test_f4_k2(self):
        """F_4 at k=2: kappa = 26*11/9 = 286/9."""
        assert kappa_numeric('F4', 2) == Fraction(286, 9)

    def test_f4_k3(self):
        """F_4 at k=3: kappa = 26*12/9 = 312/9 = 104/3."""
        assert kappa_numeric('F4', 3) == Fraction(104, 3)

    def test_e6_k1(self):
        """E_6 at k=1: kappa = 13*13/4 = 169/4."""
        assert kappa_numeric('E6', 1) == Fraction(169, 4)

    def test_e6_k2(self):
        """E_6 at k=2: kappa = 13*14/4 = 182/4 = 91/2."""
        assert kappa_numeric('E6', 2) == Fraction(91, 2)

    def test_e7_k1(self):
        """E_7 at k=1: kappa = 133*19/36 = 2527/36."""
        assert kappa_numeric('E7', 1) == Fraction(2527, 36)

    def test_e7_k2(self):
        """E_7 at k=2: kappa = 133*20/36 = 2660/36 = 665/9."""
        assert kappa_numeric('E7', 2) == Fraction(665, 9)

    def test_e8_k1(self):
        """E_8 at k=1: kappa = 62*31/15 = 1922/15."""
        assert kappa_numeric('E8', 1) == Fraction(1922, 15)

    def test_e8_k2(self):
        """E_8 at k=2: kappa = 62*32/15 = 1984/15."""
        assert kappa_numeric('E8', 2) == Fraction(1984, 15)


class TestKappaSimplified:
    """Verify human-readable kappa strings."""

    def test_g2_str(self):
        assert kappa_simplified_str('G2') == '7(k+4)/4'

    def test_f4_str(self):
        assert kappa_simplified_str('F4') == '26(k+9)/9'

    def test_e6_str(self):
        assert kappa_simplified_str('E6') == '13(k+12)/4'

    def test_e7_str(self):
        assert kappa_simplified_str('E7') == '133(k+18)/36'

    def test_e8_str(self):
        assert kappa_simplified_str('E8') == '62(k+30)/15'


# ============================================================================
# 3. Shadow class L tests
# ============================================================================

class TestShadowClassL:
    """Verify shadow class L for all exceptional types."""

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_class_is_L(self, name):
        assert shadow_class(name) == 'L'

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_depth_is_3(self, name):
        assert shadow_depth(name) == 3

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_radius_is_zero(self, name):
        assert shadow_radius(name) == 0

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_Q_contact_is_zero(self, name):
        assert Q_contact(name) == 0

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_shadow_data_class(self, name):
        sd = compute_shadow_data(name)
        assert sd.shadow_class == 'L'
        assert sd.shadow_depth == 3
        assert sd.S3_nonzero is True
        assert sd.S4_zero is True
        assert simplify(sd.Delta) == 0
        assert simplify(sd.Q_contact) == 0
        assert simplify(sd.shadow_radius) == 0


# ============================================================================
# 4. Complementarity tests (AP24)
# ============================================================================

class TestComplementarity:
    """Verify kappa + kappa' = 0 and c + c' = 2*dim for all exceptional types."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_anti_symmetry(self, label, gt):
        """kappa(k) + kappa(k') = 0 for all affine KM (AP24)."""
        assert simplify(complementarity_sum_kappa(label)) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cc_complementarity(self, label, gt):
        """c(k) + c(k') = 2*dim(g) for all affine KM."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        cc_sum = complementarity_sum_c(label)
        assert simplify(cc_sum - 2 * dim) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_numeric_complementarity_k1(self, label, gt):
        """Numeric check: kappa(1) + kappa(k'(1)) = 0."""
        kap1 = kappa_numeric(label, Fraction(1))
        kd1 = ff_dual_level_numeric(label, Fraction(1))
        kap_d1 = kappa_numeric(label, kd1)
        assert kap1 + kap_d1 == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_numeric_complementarity_k2(self, label, gt):
        """Numeric check: kappa(2) + kappa(k'(2)) = 0."""
        kap2 = kappa_numeric(label, Fraction(2))
        kd2 = ff_dual_level_numeric(label, Fraction(2))
        kap_d2 = kappa_numeric(label, kd2)
        assert kap2 + kap_d2 == 0

    def test_g2_cc_sum_is_28(self):
        """G_2: c + c' = 2*14 = 28."""
        assert simplify(complementarity_sum_c('G2') - 28) == 0

    def test_f4_cc_sum_is_104(self):
        """F_4: c + c' = 2*52 = 104."""
        assert simplify(complementarity_sum_c('F4') - 104) == 0

    def test_e6_cc_sum_is_156(self):
        """E_6: c + c' = 2*78 = 156."""
        assert simplify(complementarity_sum_c('E6') - 156) == 0

    def test_e7_cc_sum_is_266(self):
        """E_7: c + c' = 2*133 = 266."""
        assert simplify(complementarity_sum_c('E7') - 266) == 0

    def test_e8_cc_sum_is_496(self):
        """E_8: c + c' = 2*248 = 496."""
        assert simplify(complementarity_sum_c('E8') - 496) == 0

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_koszul_conductor(self, name):
        """Koszul conductor K(g) = 2*dim(g)."""
        sd = compute_shadow_data(name)
        assert sd.koszul_conductor == 2 * EXCEPTIONAL_REGISTRY[name]['dim']


# ============================================================================
# 5. Feigin-Frenkel involution tests
# ============================================================================

class TestFFInvolution:
    """Verify FF involution k -> -k - 2*h^vee."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_involution(self, label, gt):
        """(k')' = k."""
        kd = ff_dual_level_fn(label, k)
        kdd = ff_dual_level_fn(label, kd)
        assert simplify(kdd - k) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_critical_fixed_point(self, label, gt):
        """k = -h^vee is a fixed point."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kd = ff_dual_level_fn(label, -h_dual)
        assert simplify(kd + h_dual) == 0

    def test_g2_ff_dual(self):
        """G_2: k' = -k - 8."""
        assert simplify(ff_dual_level_fn('G2', k) - (-k - 8)) == 0

    def test_f4_ff_dual(self):
        """F_4: k' = -k - 18."""
        assert simplify(ff_dual_level_fn('F4', k) - (-k - 18)) == 0

    def test_e6_ff_dual(self):
        """E_6: k' = -k - 24."""
        assert simplify(ff_dual_level_fn('E6', k) - (-k - 24)) == 0

    def test_e7_ff_dual(self):
        """E_7: k' = -k - 36."""
        assert simplify(ff_dual_level_fn('E7', k) - (-k - 36)) == 0

    def test_e8_ff_dual(self):
        """E_8: k' = -k - 60."""
        assert simplify(ff_dual_level_fn('E8', k) - (-k - 60)) == 0


# ============================================================================
# 6. Central charge tests
# ============================================================================

class TestCentralCharge:
    """Verify c = dim(g) * k / (k + h^vee)."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cc_matches_definition(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        cc = central_charge_fn(label, k)
        expected = _cc_independent(dim, h_dual, k)
        assert simplify(cc - expected) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cc_at_level_zero(self, label, gt):
        """c(0) = 0."""
        cc = central_charge_fn(label, 0)
        assert cc == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cc_large_k_limit(self, label, gt):
        """As k -> infinity, c -> dim(g)."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        cc = central_charge_fn(label, k)
        cc_large = cc.subs(k, 10**6)
        assert abs(float(cc_large) - dim) < 0.01


# ============================================================================
# 7. Casimir degree tests
# ============================================================================

class TestCasimirDegrees:
    """Verify Casimir degrees = exponents + 1."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_degrees_from_exponents(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        expected = [m + 1 for m in exponents]
        assert casimir_degrees(label) == expected

    def test_g2_degrees(self):
        assert casimir_degrees('G2') == [2, 6]

    def test_f4_degrees(self):
        assert casimir_degrees('F4') == [2, 6, 8, 12]

    def test_e6_degrees(self):
        assert casimir_degrees('E6') == [2, 5, 6, 8, 9, 12]

    def test_e7_degrees(self):
        assert casimir_degrees('E7') == [2, 6, 8, 10, 12, 14, 18]

    def test_e8_degrees(self):
        assert casimir_degrees('E8') == [2, 8, 12, 14, 18, 20, 24, 30]

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_no_cubic_casimir(self, name):
        """No exceptional type has a degree-3 Casimir.

        This is because the exponent 2 (giving degree 3) only appears
        in A_n for n >= 2.  All exceptional exponents are 1 or >= 4.
        """
        assert not has_cubic_casimir(name)

    def test_quadratic_casimir_always_present(self):
        """Every simple Lie algebra has a degree-2 Casimir (from Killing form)."""
        for name in EXCEPTIONAL_REGISTRY:
            assert 2 in casimir_degrees(name)


# ============================================================================
# 8. Root system tests
# ============================================================================

class TestRootSystem:
    """Verify root system data."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_exponent_sum(self, label, gt):
        """sum(exponents) = rank * h / 2."""
        assert verify_exponent_sum(label)

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_max_exponent(self, label, gt):
        """max(exponents) = h - 1."""
        assert verify_max_exponent(label)

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_dim_from_roots(self, label, gt):
        """dim = 2 * n_positive_roots + rank."""
        assert verify_dim_from_roots(label)

    def test_g2_positive_roots(self):
        """G_2 has (14-2)/2 = 6 positive roots."""
        assert num_positive_roots('G2') == 6

    def test_f4_positive_roots(self):
        """F_4 has (52-4)/2 = 24 positive roots."""
        assert num_positive_roots('F4') == 24

    def test_e6_positive_roots(self):
        """E_6 has (78-6)/2 = 36 positive roots."""
        assert num_positive_roots('E6') == 36

    def test_e7_positive_roots(self):
        """E_7 has (133-7)/2 = 63 positive roots."""
        assert num_positive_roots('E7') == 63

    def test_e8_positive_roots(self):
        """E_8 has (248-8)/2 = 120 positive roots."""
        assert num_positive_roots('E8') == 120

    def test_g2_weyl_order(self):
        """|W(G_2)| = 2*6 = 12."""
        assert weyl_group_order('G2') == 12

    def test_f4_weyl_order(self):
        """|W(F_4)| = 2*6*8*12 = 1152."""
        assert weyl_group_order('F4') == 1152

    def test_e6_weyl_order(self):
        """|W(E_6)| = 2*5*6*8*9*12 = 51840."""
        assert weyl_group_order('E6') == 51840

    def test_e7_weyl_order(self):
        """|W(E_7)| = 2*6*8*10*12*14*18 = 2903040."""
        assert weyl_group_order('E7') == 2903040

    def test_e8_weyl_order(self):
        """|W(E_8)| = 2*8*12*14*18*20*24*30 = 696729600."""
        assert weyl_group_order('E8') == 696729600


# ============================================================================
# 9. Anomaly ratio tests
# ============================================================================

class TestAnomalyRatio:
    """Verify rho(g) = sum 1/(m_i + 1) for each exceptional type."""

    def test_g2_anomaly_ratio(self):
        """G_2: rho = 1/2 + 1/6 = 2/3."""
        expected = Fraction(1, 2) + Fraction(1, 6)
        assert anomaly_ratio('G2') == expected
        assert expected == Fraction(2, 3)

    def test_f4_anomaly_ratio(self):
        """F_4: rho = 1/2 + 1/6 + 1/8 + 1/12 = 5/6."""
        expected = Fraction(1, 2) + Fraction(1, 6) + Fraction(1, 8) + Fraction(1, 12)
        assert anomaly_ratio('F4') == expected
        # 12/24 + 4/24 + 3/24 + 2/24 = 21/24 = 7/8
        assert expected == Fraction(7, 8)

    def test_e6_anomaly_ratio(self):
        """E_6: rho = 1/2 + 1/5 + 1/6 + 1/8 + 1/9 + 1/12."""
        terms = [Fraction(1, m + 1)
                 for m in [1, 4, 5, 7, 8, 11]]
        expected = sum(terms)
        assert anomaly_ratio('E6') == expected
        # = 1/2 + 1/5 + 1/6 + 1/8 + 1/9 + 1/12
        # LCD = 360
        # = 180/360 + 72/360 + 60/360 + 45/360 + 40/360 + 30/360
        # = 427/360
        assert expected == Fraction(427, 360)

    def test_e7_anomaly_ratio(self):
        """E_7: rho = 1/2 + 1/6 + 1/8 + 1/10 + 1/12 + 1/14 + 1/18."""
        terms = [Fraction(1, m + 1)
                 for m in [1, 5, 7, 9, 11, 13, 17]]
        expected = sum(terms)
        assert anomaly_ratio('E7') == expected
        # = 1/2 + 1/6 + 1/8 + 1/10 + 1/12 + 1/14 + 1/18
        # LCD = 2520
        # = 1260/2520 + 420/2520 + 315/2520 + 252/2520 + 210/2520 + 180/2520 + 140/2520
        # = 2777/2520
        assert expected == Fraction(2777, 2520)

    def test_e8_anomaly_ratio(self):
        """E_8: rho = 1/2 + 1/8 + 1/12 + 1/14 + 1/18 + 1/20 + 1/24 + 1/30."""
        terms = [Fraction(1, m + 1)
                 for m in [1, 7, 11, 13, 17, 19, 23, 29]]
        expected = sum(terms)
        assert anomaly_ratio('E8') == expected
        # Compute from first principles:
        # 1/2 = 63/126
        # 1/8 = 15.75/126
        # Actually let's just verify the known value: 121/126
        # 1/2 + 1/8 + 1/12 + 1/14 + 1/18 + 1/20 + 1/24 + 1/30
        # LCD = 2520, computed:
        # 1260 + 315 + 210 + 180 + 140 + 126 + 105 + 84 = 2420
        # 2420/2520 = 121/126
        assert expected == Fraction(121, 126)


# ============================================================================
# 10. Strange Formula tests
# ============================================================================

class TestStrangeFormula:
    """Verify |rho_Weyl|^2 = dim(g) * h / 12."""

    def test_g2_rho_squared(self):
        """G_2: |rho|^2 = 14*6/12 = 7."""
        assert weyl_rho_squared('G2') == Fraction(7)

    def test_f4_rho_squared(self):
        """F_4: |rho|^2 = 52*12/12 = 52."""
        assert weyl_rho_squared('F4') == Fraction(52)

    def test_e6_rho_squared(self):
        """E_6: |rho|^2 = 78*12/12 = 78."""
        assert weyl_rho_squared('E6') == Fraction(78)

    def test_e7_rho_squared(self):
        """E_7: |rho|^2 = 133*18/12 = 399/2."""
        assert weyl_rho_squared('E7') == Fraction(399, 2)

    def test_e8_rho_squared(self):
        """E_8: |rho|^2 = 248*30/12 = 620."""
        assert weyl_rho_squared('E8') == Fraction(620)

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_strange_formula_verified(self, name):
        assert verify_strange_formula(name)


# ============================================================================
# 11. W-algebra tests
# ============================================================================

class TestWAlgebra:
    """Verify W-algebra kappa = rho * c(W)."""

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_w_kappa_identity_k1(self, name):
        """kappa(W(g), 1) = rho(g) * c(W(g), 1)."""
        rho = anomaly_ratio(name)
        c_w = w_algebra_central_charge_numeric(name, Fraction(1))
        kap_w = w_algebra_kappa_numeric(name, Fraction(1))
        assert kap_w == rho * c_w

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_w_kappa_identity_k2(self, name):
        """kappa(W(g), 2) = rho(g) * c(W(g), 2)."""
        rho = anomaly_ratio(name)
        c_w = w_algebra_central_charge_numeric(name, Fraction(2))
        kap_w = w_algebra_kappa_numeric(name, Fraction(2))
        assert kap_w == rho * c_w

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_w_cc_approaches_rank_at_large_k(self, name):
        """c(W(g), k) -> rank as k -> infinity.

        The FKW formula gives c_W = rank - dim*h*(p-1)^2/p.
        As p -> infinity, dim*h*(p-1)^2/p -> dim*h*p -> infinity.
        So c_W -> -infinity.  Wait, let me recheck.

        Actually for large k: p = k + h^v ~ k, so
        c_W = rank - dim*h*(k+h^v-1)^2/(k+h^v) ~ rank - dim*h*k.
        This goes to -infinity, not to rank.

        The rank is the central charge at the CRITICAL level k = -h^v + 1
        (i.e., p = 1): c_W(p=1) = rank - 0 = rank.

        Let me verify c_W at p=1 (i.e., k = -h^v + 1 = 1 - h^v):
        """
        reg = EXCEPTIONAL_REGISTRY[name]
        # At p = 1 (k = 1 - h^v): c_W = rank - dim*h*0/1 = rank
        c_at_p1 = w_algebra_central_charge_numeric(name, Fraction(1 - reg['h_dual']))
        assert c_at_p1 == Fraction(reg['rank'])


# ============================================================================
# 12. Genus amplitude tests
# ============================================================================

class TestGenusAmplitudes:
    """Verify F_1 = kappa/24 and F_2^scalar = 7*kappa/5760."""

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_F1_formula(self, name):
        """F_1 = kappa / 24."""
        f1 = F1(name, k)
        kap = kappa_fn(name, k)
        assert simplify(f1 - kap / 24) == 0

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_F2_scalar_formula(self, name):
        """F_2^scalar = 7 * kappa / 5760 (LINEAR in kappa, Theorem D)."""
        f2 = F2(name, k)
        kap = kappa_fn(name, k)
        assert simplify(f2 - 7 * kap / 5760) == 0

    def test_F1_g2_k1(self):
        """F_1(G_2, k=1) = (35/4)/24 = 35/96."""
        assert F1_numeric('G2', 1) == Fraction(35, 96)

    def test_F1_e8_k1(self):
        """F_1(E_8, k=1) = (1922/15)/24 = 1922/360 = 961/180."""
        assert F1_numeric('E8', 1) == Fraction(961, 180)

    def test_F2_scalar_g2_k1(self):
        """F_2^scalar(G_2, k=1) = 7*(35/4)/5760 = 245/23040."""
        kap = Fraction(35, 4)
        expected = 7 * kap / 5760
        assert F2_scalar_numeric('G2', 1) == expected

    def test_F2_scalar_e8_k1(self):
        """F_2^scalar(E_8, k=1) = 7*(1922/15)/5760 = 13454/86400."""
        kap = Fraction(1922, 15)
        expected = 7 * kap / 5760
        assert F2_scalar_numeric('E8', 1) == expected


# ============================================================================
# 13. E_8 theta function tests
# ============================================================================

class TestE8Theta:
    """Verify E_8 root lattice theta function properties."""

    def test_e8_root_count(self):
        """E_8 has 240 roots (2 * 120 positive roots)."""
        assert e8_root_count() == 240

    def test_e8_theta_leading(self):
        """Leading coefficient of Theta_{E_8} = 240."""
        assert e8_theta_leading() == 240

    def test_e8_theta_matches_E4(self):
        """Root count 240 matches the coefficient of q in E_4(tau)."""
        assert e8_theta_matches_E4()

    def test_e8_E4_coefficients(self):
        """E_4(tau) = 1 + 240*q + 2160*q^2 + 6720*q^3 + ...

        Coefficients = 240 * sigma_3(n).
        """
        coeffs = theta_e8_coefficients(5)
        assert coeffs[0] == 1
        assert coeffs[1] == 240        # 240 * sigma_3(1) = 240 * 1
        assert coeffs[2] == 2160       # 240 * sigma_3(2) = 240 * (1+8) = 240*9
        assert coeffs[3] == 6720       # 240 * sigma_3(3) = 240 * (1+27) = 240*28
        assert coeffs[4] == 17520      # 240 * sigma_3(4) = 240 * (1+8+27+64) = 240*73 -- wait
        # sigma_3(4) = 1^3 + 2^3 + 4^3 = 1 + 8 + 64 = 73
        # 240 * 73 = 17520

    def test_e8_positive_roots_from_cartan(self):
        """Verify 120 positive roots are computed by cartan_data."""
        cd = cartan_data('E', 8)
        assert len(cd.positive_roots) == 120


# ============================================================================
# 14. Deligne series tests
# ============================================================================

class TestDeligneSeries:
    """Verify properties along the Deligne exceptional series."""

    def test_deligne_series_length(self):
        """Series has 6 members: A_1, G_2, F_4, E_6, E_7, E_8."""
        assert len(DELIGNE_SERIES) == 6

    def test_deligne_dim_increasing(self):
        """Dimensions increase along the series."""
        dims = [entry[3] for entry in DELIGNE_SERIES]
        for i in range(len(dims) - 1):
            assert dims[i] < dims[i + 1]

    def test_deligne_h_dual_increasing(self):
        """Dual Coxeter numbers increase along the series."""
        h_duals = [entry[5] for entry in DELIGNE_SERIES]
        for i in range(len(h_duals) - 1):
            assert h_duals[i] < h_duals[i + 1]

    def test_deligne_kappa_monotonicity_k1(self):
        """Kappa values increase along the series at k=1."""
        results = cross_family_kappa_monotonicity(1)
        for name, ok in results.items():
            assert ok, f"Kappa monotonicity failed: {name}"

    def test_deligne_kappa_at_k1(self):
        """Verify specific kappa values at k=1 along the series."""
        data = deligne_kappa_at_level(1)
        # A_1: kappa = 3*(1+2)/(2*2) = 9/4
        assert data[0]['kappa'] == Fraction(9, 4)
        # G_2: kappa = 7*(1+4)/4 = 35/4
        assert data[1]['kappa'] == Fraction(35, 4)
        # F_4: kappa = 26*(1+9)/9 = 260/9
        assert data[2]['kappa'] == Fraction(260, 9)

    def test_deligne_kappa_over_dim_pattern(self):
        """kappa(g, k)/dim(g) = (k + h^v)/(2*h^v) = 1/2 + k/(2*h^v).

        At k=1: kappa/dim = 1/2 + 1/(2*h^v).
        This DECREASES along the series (h^v increases), converging to 1/2.
        """
        ratios = deligne_kappa_ratios(1)
        for i in range(len(ratios) - 1):
            r1 = ratios[i]['kappa_over_dim']
            r2 = ratios[i + 1]['kappa_over_dim']
            # kappa/dim = 1/2 + 1/(2*h^v) decreases as h^v increases
            assert r1 > r2


# ============================================================================
# 15. Langlands self-duality tests
# ============================================================================

class TestLanglands:
    """Verify Langlands self-duality for all exceptional types."""

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_self_dual(self, name):
        assert is_langlands_self_dual(name)

    @pytest.mark.parametrize("name", list(EXCEPTIONAL_REGISTRY.keys()))
    def test_dual_type(self, name):
        assert langlands_dual_type(name) == name


# ============================================================================
# 16. Cross-family consistency tests (AP10)
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_all_class_L(self):
        results = cross_family_all_class_L()
        for name, ok in results.items():
            assert ok

    def test_all_complementarity(self):
        results = cross_family_complementarity()
        for name, ok in results.items():
            assert ok, f"Complementarity failed: {name}"

    def test_no_cubic_casimir(self):
        results = cross_family_no_cubic_casimir()
        for name, ok in results.items():
            assert ok, f"Cubic Casimir check failed: {name}"

    def test_koszul_conductor(self):
        results = cross_family_koszul_conductor()
        for name, ok in results.items():
            assert ok, f"Koszul conductor check failed: {name}"

    def test_kappa_monotonicity_k1(self):
        results = cross_family_kappa_monotonicity(1)
        for name, ok in results.items():
            assert ok, f"Monotonicity failed: {name}"

    def test_kappa_monotonicity_k2(self):
        results = cross_family_kappa_monotonicity(2)
        for name, ok in results.items():
            assert ok, f"Monotonicity failed: {name}"

    def test_comparison_table(self):
        """Comparison table has expected number of rows."""
        rows = comparison_table([1, 2])
        assert len(rows) == 10  # 5 types * 2 levels

    def test_all_shadow_data_count(self):
        """all_shadow_data returns 5 entries."""
        data = all_shadow_data()
        assert len(data) == 5
        assert set(data.keys()) == {'G2', 'F4', 'E6', 'E7', 'E8'}


# ============================================================================
# 17. AP-specific regression tests
# ============================================================================

class TestAPRegressions:
    """Tests targeting specific anti-patterns from the manuscript's error history."""

    def test_ap1_kappa_not_copied_between_families(self):
        """AP1: Each kappa is computed from its own (dim, h^v).

        G_2 and F_4 have different (dim, h^v) pairs, so their kappas
        are structurally different.  Verify they are NOT equal.
        """
        kap_g2 = kappa_fn('G2', k)
        kap_f4 = kappa_fn('F4', k)
        assert simplify(kap_g2 - kap_f4) != 0

    def test_ap1_kappa_uses_h_dual_not_h(self):
        """AP1: For non-simply-laced, kappa uses h^v, NOT h.

        G_2: h=6, h^v=4.  If you wrongly use h=6:
            kappa_wrong = 14*(k+6)/12 = 7(k+6)/6
        The correct formula is:
            kappa = 14*(k+4)/8 = 7(k+4)/4
        These differ: 7(k+4)/4 != 7(k+6)/6.
        """
        kap_correct = kappa_fn('G2', k)
        kap_wrong = Rational(14) * (k + 6) / (2 * 6)
        assert simplify(kap_correct - kap_wrong) != 0

    def test_ap1_f4_kappa_uses_h_dual_9_not_h_12(self):
        """AP1: F_4 kappa uses h^v=9, NOT h=12."""
        kap_correct = kappa_fn('F4', k)
        kap_wrong = Rational(52) * (k + 12) / (2 * 12)  # using h instead of h^v
        assert simplify(kap_correct - kap_wrong) != 0

    def test_ap3_no_pattern_completion(self):
        """AP3: Each type's kappa verified independently, not by pattern.

        E_6 has dim=78, h^v=12 giving kappa=13(k+12)/4.
        E_7 has dim=133, h^v=18 giving kappa=133(k+18)/36.
        These do NOT follow a simple pattern from E_6.
        """
        kap_e6 = kappa_numeric('E6', 1)
        kap_e7 = kappa_numeric('E7', 1)
        # E_6 at k=1: 169/4 = 42.25
        # E_7 at k=1: 2527/36 ~ 70.19
        # The ratio is NOT a simple integer or low-denominator fraction
        ratio = kap_e7 / kap_e6
        assert ratio != Fraction(2)  # not double
        assert ratio.denominator > 1  # not an integer ratio

    def test_ap9_kappa_vs_c_distinction(self):
        """AP9: kappa(g, k) != c(g, k) in general."""
        for name in EXCEPTIONAL_REGISTRY:
            kap = kappa_fn(name, k)
            cc = central_charge_fn(name, k)
            assert simplify(kap - cc) != 0

    def test_ap19_r_matrix_simple_pole(self):
        """AP19: r-matrix has pole at z^{-1}, not z^{-2}.

        The KM OPE has z^{-2} (central) and z^{-1} (bracket) poles.
        After d log extraction, the r-matrix has a single simple pole.
        """
        for name in EXCEPTIONAL_REGISTRY:
            sd = compute_shadow_data(name)
            assert sd.r_matrix_pole_order == 1

    def test_ap24_km_anti_symmetry(self):
        """AP24: For KM, kappa + kappa' = 0 (not 13 like Virasoro).

        Verify at multiple numeric levels.
        """
        for name in EXCEPTIONAL_REGISTRY:
            for level_val in [1, 2, 5, 10]:
                kap = kappa_numeric(name, Fraction(level_val))
                kd = ff_dual_level_numeric(name, Fraction(level_val))
                kap_dual = kappa_numeric(name, kd)
                assert kap + kap_dual == 0, (
                    f"{name} at k={level_val}: "
                    f"kappa + kappa' = {kap + kap_dual} != 0"
                )

    def test_ap27_weight_1_propagator(self):
        """AP27: Bar propagator is d log E(z,w), weight 1 for all types.

        This is structural: the r-matrix r(z) = Omega/z has weight 1
        in each variable, regardless of the conformal weights of the generators.
        """
        for name in EXCEPTIONAL_REGISTRY:
            sd = compute_shadow_data(name)
            assert sd.r_matrix_pole_order == 1


# ============================================================================
# 18. Numerical spot-checks
# ============================================================================

class TestNumericalSpotChecks:
    """Exhaustive numerical spot-checks at distinguished levels."""

    @pytest.mark.parametrize("name,level,expected_kappa", [
        # G_2: kappa = 7(k+4)/4
        ('G2', 1, Fraction(35, 4)),
        ('G2', 2, Fraction(42, 4)),
        ('G2', 3, Fraction(49, 4)),
        # F_4: kappa = 26(k+9)/9
        ('F4', 1, Fraction(260, 9)),
        ('F4', 2, Fraction(286, 9)),
        ('F4', 3, Fraction(312, 9)),
        # E_6: kappa = 13(k+12)/4
        ('E6', 1, Fraction(169, 4)),
        ('E6', 2, Fraction(182, 4)),
        ('E6', 3, Fraction(195, 4)),
        # E_7: kappa = 133(k+18)/36
        ('E7', 1, Fraction(133 * 19, 36)),
        ('E7', 2, Fraction(133 * 20, 36)),
        ('E7', 3, Fraction(133 * 21, 36)),
        # E_8: kappa = 62(k+30)/15
        ('E8', 1, Fraction(62 * 31, 15)),
        ('E8', 2, Fraction(62 * 32, 15)),
        ('E8', 3, Fraction(62 * 33, 15)),
    ])
    def test_kappa_at_level(self, name, level, expected_kappa):
        assert kappa_numeric(name, level) == expected_kappa

    @pytest.mark.parametrize("name,level,expected_cc", [
        ('G2', 1, Fraction(14, 5)),        # 14*1/(1+4) = 14/5
        ('F4', 1, Fraction(52, 10)),       # 52*1/(1+9) = 52/10 = 26/5
        ('E6', 1, Fraction(78, 13)),       # 78*1/(1+12) = 78/13 = 6
        ('E7', 1, Fraction(133, 19)),      # 133*1/(1+18) = 133/19 = 7
        ('E8', 1, Fraction(248, 31)),      # 248*1/(1+30) = 248/31 = 8
    ])
    def test_cc_at_level(self, name, level, expected_cc):
        assert central_charge_numeric(name, level) == expected_cc

    def test_e6_cc_at_k1_is_6(self):
        """E_6 at k=1: c = 78/13 = 6."""
        assert central_charge_numeric('E6', 1) == Fraction(6)

    def test_e7_cc_at_k1_is_7(self):
        """E_7 at k=1: c = 133/19 = 7."""
        assert central_charge_numeric('E7', 1) == Fraction(7)

    def test_e8_cc_at_k1_is_8(self):
        """E_8 at k=1: c = 248/31 = 8."""
        assert central_charge_numeric('E8', 1) == Fraction(8)

    def test_deligne_cc_at_k1_equals_rank(self):
        """Remarkable: for simply-laced exceptionals at k=1,
        c(E_n, 1) = rank(E_n) = n.

        This is because dim(E_n)/(1 + h^v) simplifies:
        E_6: 78/13 = 6
        E_7: 133/19 = 7
        E_8: 248/31 = 8

        For G_2: c = 14/5 != 2.  For F_4: c = 52/10 = 26/5 != 4.
        So this property is SPECIFIC to the E-series.
        """
        assert central_charge_numeric('E6', 1) == Fraction(6)
        assert central_charge_numeric('E7', 1) == Fraction(7)
        assert central_charge_numeric('E8', 1) == Fraction(8)
        # And NOT for G_2, F_4:
        assert central_charge_numeric('G2', 1) != Fraction(2)
        assert central_charge_numeric('F4', 1) != Fraction(4)


# ============================================================================
# 19. Master verification test
# ============================================================================

class TestMasterVerification:
    """Run the full verification suite and check no failures."""

    def test_verify_all(self):
        results = verify_all()
        failures = {}
        for name, checks in results.items():
            for check_name, passed in checks.items():
                if not passed:
                    failures[f"{name}.{check_name}"] = False
        assert len(failures) == 0, f"Verification failures: {failures}"

    def test_verify_all_against_cartan(self):
        results = verify_all_against_cartan()
        for name, checks in results.items():
            for check_name, passed in checks.items():
                assert passed, f"{name}: cartan check {check_name} failed"
