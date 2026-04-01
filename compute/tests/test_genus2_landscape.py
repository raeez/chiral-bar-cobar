r"""Tests for compute/lib/genus2_landscape.py.

Verifies genus-2 free energy F_2 across the standard landscape:
    1. Heisenberg at k=1 (scalar lane, class G)
    2. Virasoro at c=25 (scalar lane, class M)
    3. Affine sl_2 at k=1 (scalar lane, class L)
    4. W_3 at generic c (multi-weight, class M)
    5. betagamma at lambda=1 (multi-weight, class C)
    6. E_8 lattice (scalar lane, class G)

Test categories:
    - Exact kappa values (AP1: never copy between families without recomputing)
    - F_2 values on scalar lane (AP10: cross-family structural checks)
    - Planted-forest corrections (formula verification)
    - Complementarity (AP24: kappa + kappa' != 0 for Virasoro)
    - Linearity / additivity (structural consistency)
    - Multi-weight status flags (AP14, AP28: precise qualification)
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.genus2_landscape import (
    lambda_fp_2,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_w3,
    kappa_w3_T,
    kappa_w3_W,
    kappa_betagamma,
    kappa_E8_lattice,
    F2_scalar,
    planted_forest_g2,
    planted_forest_g2_w3_T,
    planted_forest_g2_w3_W,
    planted_forest_g2_w3_total,
    F2_heisenberg,
    F2_virasoro,
    F2_affine_sl2,
    F2_w3,
    F2_betagamma,
    F2_E8_lattice,
    genus2_landscape_table,
    verify_kappa_additivity,
    verify_F2_linearity,
    verify_complementarity_F2,
    verify_planted_forest_consistency,
)


# ============================================================================
# lambda_2^FP
# ============================================================================

class TestLambdaFP2:
    """Verify the Faber-Pandharipande number at genus 2."""

    def test_exact_value(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp_2() == Rational(7, 5760)

    def test_from_bernoulli(self):
        """Independent computation: (2^3 - 1)/2^3 * |B_4| / 4!"""
        from sympy import bernoulli, factorial
        B4 = bernoulli(4)  # B_4 = -1/30
        assert B4 == Rational(-1, 30)
        lam2 = Rational(7, 8) * abs(B4) / factorial(4)
        assert lam2 == Rational(7, 5760)


# ============================================================================
# Kappa formulas (AP1: verify each independently, never copy between families)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa for each family from first principles."""

    def test_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(1) == Rational(1)

    def test_heisenberg_k_general(self):
        """kappa(H_k) = k for several values."""
        for k in [1, 2, 5, 10]:
            assert kappa_heisenberg(k) == Rational(k)

    def test_virasoro_c25(self):
        """kappa(Vir_25) = 25/2."""
        assert kappa_virasoro(25) == Rational(25, 2)

    def test_virasoro_c26(self):
        """kappa(Vir_26) = 13. Self-dual point: kappa = c/2 = 13."""
        assert kappa_virasoro(26) == Rational(13)

    def test_virasoro_c0(self):
        """kappa(Vir_0) = 0. Uncurved bar complex."""
        assert kappa_virasoro(0) == Rational(0)

    def test_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4.

        dim(sl_2) = 3, h^v = 2, k+h^v = 3.
        kappa = dim*(k+h^v)/(2*h^v) = 3*3/4 = 9/4.

        NOTE: The user's prompt incorrectly computed this as 9/8.
        The correct formula: 3*3/(2*2) = 9/4, NOT 3*3/(4*2) = 9/8.
        """
        assert kappa_affine_sl2(1) == Rational(9, 4)

    def test_sl2_k1_from_first_principles(self):
        """Independent recomputation: dim=3, h^v=2, k=1."""
        dim_g = 3
        h_dual = 2
        k = 1
        kappa = Rational(dim_g) * (k + h_dual) / (2 * h_dual)
        assert kappa == Rational(9, 4)
        assert kappa == kappa_affine_sl2(1)

    def test_w3_generic(self):
        """kappa(W_3) = 5c/6 for several c values."""
        for c_val in [6, 25, 50, 100]:
            assert kappa_w3(c_val) == Rational(5) * Rational(c_val) / 6

    def test_w3_channel_decomposition(self):
        """kappa(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
        for c_val in [6, 25, 50]:
            assert kappa_w3(c_val) == kappa_w3_T(c_val) + kappa_w3_W(c_val)

    def test_betagamma_lam1(self):
        """kappa(bg, lambda=1) = 6*1 - 6 + 1 = 1."""
        assert kappa_betagamma(1) == Rational(1)

    def test_betagamma_lam0(self):
        """kappa(bg, lambda=0) = 0 - 0 + 1 = 1."""
        assert kappa_betagamma(0) == Rational(1)

    def test_betagamma_lam_half(self):
        """kappa(bg, lambda=1/2) = 6/4 - 3 + 1 = 3/2 - 3 + 1 = -1/2."""
        assert kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)

    def test_betagamma_lam1_lam0_agree(self):
        """kappa(bg, 0) = kappa(bg, 1) = 1 (invariant under lambda -> 1-lambda)."""
        assert kappa_betagamma(0) == kappa_betagamma(1)

    def test_E8_lattice(self):
        """kappa(V_{E_8}) = rank = 8."""
        assert kappa_E8_lattice() == Rational(8)


# ============================================================================
# F_2 scalar-lane values
# ============================================================================

class TestF2ScalarLane:
    """Verify F_2 = kappa * 7/5760 on the scalar lane."""

    def test_F2_heisenberg_k1(self):
        """F_2(H_1) = 7/5760."""
        result = F2_heisenberg(1)
        assert result['F2'] == Rational(7, 5760)

    def test_F2_virasoro_c25(self):
        """F_2(Vir_25) = (25/2) * 7/5760 = 175/11520 = 35/2304.

        NOTE: The user's prompt stated 175/5760 which is WRONG.
        The correct value is 7*(25/2)/5760 = 175/11520 = 35/2304.
        """
        result = F2_virasoro(25)
        expected = Rational(25, 2) * Rational(7, 5760)
        assert expected == Rational(35, 2304)  # reduced form
        assert result['F2'] == expected

    def test_F2_virasoro_c25_not_175_over_5760(self):
        """The user's prompt claimed F_2 = 175/5760. This is WRONG by factor 2.

        Correct: 7*(25/2)/5760 = 175/11520 = 35/2304, NOT 175/5760.
        """
        correct = Rational(25, 2) * Rational(7, 5760)
        wrong = Rational(175, 5760)
        assert correct != wrong
        assert correct == wrong / 2  # user's value is exactly 2x too large

    def test_F2_sl2_k1(self):
        """F_2(sl_2, k=1) = (9/4) * 7/5760 = 63/23040 = 7/2560.

        NOTE: The user's prompt computed kappa = 9/8 (wrong).
        The correct kappa = 3*(1+2)/4 = 9/4.
        """
        result = F2_affine_sl2(1)
        expected = Rational(9, 4) * Rational(7, 5760)
        assert expected == Rational(7, 2560)  # reduced form
        assert result['F2'] == expected

    def test_F2_sl2_k1_not_user_value(self):
        """The user's prompt used kappa = 9/8. This is WRONG.

        kappa = dim*(k+h^v)/(2*h^v) = 3*(1+2)/(2*2) = 9/4, NOT 9/8.
        The user wrote 3*3/(4*2) = 9/8, confusing the denominator.
        """
        wrong_kappa = Rational(9, 8)
        correct_kappa = Rational(9, 4)
        assert correct_kappa == 2 * wrong_kappa
        assert kappa_affine_sl2(1) == correct_kappa

    def test_F2_betagamma_lam1_scalar_value(self):
        """F_2^{scal}(bg, lambda=1) = 1 * 7/5760 = 7/5760.

        The scalar-lane VALUE is 7/5760. But betagamma at lambda=1 is
        multi-weight (beta weight 1, gamma weight 0), so whether this
        is the ACTUAL F_2 depends on op:multi-generator-universality.
        """
        result = F2_betagamma(1)
        assert result['F2_scalar'] == Rational(7, 5760)

    def test_F2_E8(self):
        """F_2(V_{E_8}) = 8 * 7/5760 = 56/5760 = 7/720."""
        result = F2_E8_lattice()
        expected = Rational(8) * Rational(7, 5760)
        assert expected == Rational(7, 720)
        assert result['F2'] == expected


# ============================================================================
# Scalar-lane status flags (AP14, AP28: precise qualification)
# ============================================================================

class TestScalarLaneFlags:
    """Verify which families are on the scalar lane and which are not."""

    def test_heisenberg_is_scalar(self):
        """Heisenberg: single generator, weight 1. Scalar lane."""
        assert F2_heisenberg(1)['scalar_lane'] is True

    def test_virasoro_is_scalar(self):
        """Virasoro: single generator, weight 2. Scalar lane."""
        assert F2_virasoro(25)['scalar_lane'] is True

    def test_sl2_is_scalar(self):
        """Affine sl_2: 3 generators, ALL weight 1. Uniform weight, scalar lane."""
        assert F2_affine_sl2(1)['scalar_lane'] is True

    def test_w3_not_scalar(self):
        """W_3: generators T (weight 2) and W (weight 3). Multi-weight."""
        assert F2_w3(50)['scalar_lane'] is False

    def test_betagamma_lam1_not_scalar(self):
        """betagamma at lambda=1: weights 1 and 0. Multi-weight."""
        assert F2_betagamma(1)['scalar_lane'] is False

    def test_betagamma_lam_half_is_scalar(self):
        """betagamma at lambda=1/2: weights 1/2 and 1/2. Uniform weight."""
        result = F2_betagamma(Rational(1, 2))
        assert result['scalar_lane'] is True

    def test_E8_is_scalar(self):
        """E_8 lattice: 8 generators, all weight 1. Uniform weight, scalar lane."""
        assert F2_E8_lattice()['scalar_lane'] is True


# ============================================================================
# Shadow classification
# ============================================================================

class TestShadowClass:
    """Verify shadow depth classification for each family."""

    def test_heisenberg_class_G(self):
        assert F2_heisenberg(1)['shadow_class'] == 'G'
        assert F2_heisenberg(1)['shadow_depth'] == 2

    def test_virasoro_class_M(self):
        assert F2_virasoro(25)['shadow_class'] == 'M'

    def test_sl2_class_L(self):
        assert F2_affine_sl2(1)['shadow_class'] == 'L'
        assert F2_affine_sl2(1)['shadow_depth'] == 3

    def test_w3_class_M(self):
        assert F2_w3(50)['shadow_class'] == 'M'

    def test_betagamma_class_C(self):
        assert F2_betagamma(1)['shadow_class'] == 'C'
        assert F2_betagamma(1)['shadow_depth'] == 4

    def test_E8_class_G(self):
        assert F2_E8_lattice()['shadow_class'] == 'G'
        assert F2_E8_lattice()['shadow_depth'] == 2


# ============================================================================
# Planted-forest correction
# ============================================================================

class TestPlantedForest:
    """Verify planted-forest corrections at genus 2."""

    def test_formula_general(self):
        """delta_pf = S_3 * (10*S_3 - kappa) / 48."""
        # S_3 = 3, kappa = 10: delta = 3*(30 - 10)/48 = 60/48 = 5/4
        assert planted_forest_g2(Rational(3), Rational(10)) == Rational(5, 4)

    def test_heisenberg_zero(self):
        """Heisenberg (class G): S_3 = 0, delta_pf = 0."""
        assert planted_forest_g2(Rational(0), Rational(1)) == Rational(0)

    def test_virasoro_c26(self):
        """Virasoro c=26: S_3 = 2, kappa = 13.
        delta_pf = 2*(20 - 13)/48 = 14/48 = 7/24.
        """
        assert planted_forest_g2(Rational(2), Rational(13)) == Rational(7, 24)

    def test_virasoro_c40_vanishes(self):
        """Virasoro c=40: S_3 = 2, kappa = 20.
        delta_pf = 2*(20 - 20)/48 = 0.
        Special value where the correction vanishes.
        """
        assert planted_forest_g2(Rational(2), Rational(20)) == Rational(0)

    def test_w3_T_line(self):
        """W_3 T-line: S_3 = 2, kappa_T = c/2.
        At c=50: delta_pf_T = 2*(20 - 25)/48 = -10/48 = -5/24.
        """
        dpf = planted_forest_g2_w3_T(50)
        expected = Rational(2) * (20 - 25) / 48
        assert dpf == expected
        assert dpf == Rational(-5, 24)

    def test_w3_W_line_zero(self):
        """W_3 W-line: S_3 = 0 by Z_2 parity. delta_pf_W = 0."""
        assert planted_forest_g2_w3_W(50) == Rational(0)
        assert planted_forest_g2_w3_W(100) == Rational(0)

    def test_w3_total_equals_T_line(self):
        """W_3 total delta_pf = delta_pf_T + 0 = delta_pf_T."""
        for c_val in [25, 50, 100]:
            assert planted_forest_g2_w3_total(c_val) == planted_forest_g2_w3_T(c_val)

    def test_w3_total_formula(self):
        """W_3 total delta_pf = (40 - c) / 48."""
        for c_val in [25, 50, 100]:
            dpf = planted_forest_g2_w3_total(c_val)
            expected = (Rational(40) - Rational(c_val)) / 48
            assert dpf == expected

    def test_w3_symbolic(self):
        """W_3 planted-forest in symbolic c."""
        dpf = planted_forest_g2_w3_total()
        c_sym = Symbol('c')
        expected = (40 - c_sym) / 48
        assert simplify(dpf - expected) == 0


# ============================================================================
# F_2 linearity and additivity (structural cross-checks, AP10)
# ============================================================================

class TestStructuralChecks:
    """Cross-family structural consistency checks."""

    def test_kappa_additivity(self):
        """All kappa additivity checks pass."""
        results = verify_kappa_additivity()
        for name, ok in results.items():
            assert ok, f"Kappa additivity failed: {name}"

    def test_F2_linearity(self):
        """All F_2 linearity checks pass."""
        results = verify_F2_linearity()
        for name, ok in results.items():
            assert ok, f"F_2 linearity failed: {name}"

    def test_planted_forest_consistency(self):
        """All planted-forest consistency checks pass."""
        results = verify_planted_forest_consistency()
        for name, ok in results.items():
            assert ok, f"Planted-forest consistency failed: {name}"


# ============================================================================
# Complementarity (AP24: kappa + kappa' != 0 for Virasoro)
# ============================================================================

class TestComplementarity:
    """Verify Koszul duality complementarity for F_2."""

    def test_virasoro_complementarity(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * lambda_2^FP = 91/5760.

        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
        AP24: this is 13, NOT 0.
        """
        comp = verify_complementarity_F2()
        vir_data = comp['Vir F2 + F2_dual']
        assert vir_data['match']
        assert vir_data['sum'] == Rational(91, 5760)

    def test_sl2_complementarity(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0.

        Feigin-Frenkel: k' = -k - 2h^v = -k - 4.
        For KM: anti-symmetry holds (AP24: kappa + kappa' = 0).
        """
        comp = verify_complementarity_F2()
        sl2_data = comp['sl2 kappa + kappa_dual = 0']
        assert sl2_data['match']
        assert sl2_data['sum'] == Rational(0)

    def test_virasoro_complementarity_varies_c(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 91/5760 for several c values."""
        for c_val in [1, 10, 13, 25]:
            F2_c = F2_virasoro(c_val)['F2']
            F2_dual = F2_virasoro(26 - c_val)['F2']
            assert F2_c + F2_dual == Rational(91, 5760), f"Failed at c={c_val}"

    def test_virasoro_self_dual_point(self):
        """At c=13: Vir_13^! = Vir_13. F_2 = (13/2) * 7/5760 = 91/11520."""
        F2_13 = F2_virasoro(13)['F2']
        assert F2_13 == Rational(13, 2) * Rational(7, 5760)
        assert F2_13 == Rational(91, 11520)
        # Self-dual: F_2 + F_2' = 2 * F_2 = 91/5760
        assert 2 * F2_13 == Rational(91, 5760)


# ============================================================================
# W_3 multi-channel detail
# ============================================================================

class TestW3Detail:
    """Detailed tests for the W_3 multi-weight computation."""

    def test_channel_decomposition(self):
        """kappa_T + kappa_W = 5c/6 for c=60."""
        assert kappa_w3_T(60) + kappa_w3_W(60) == kappa_w3(60)
        assert kappa_w3_T(60) == Rational(30)
        assert kappa_w3_W(60) == Rational(20)
        assert kappa_w3(60) == Rational(50)

    def test_F2_scalar_w3(self):
        """F_2^{scal}(W_3, c=60) = (50) * 7/5760 = 350/5760 = 35/576."""
        result = F2_w3(60)
        assert result['F2_scalar'] == Rational(50) * Rational(7, 5760)
        assert result['F2_scalar'] == Rational(35, 576)

    def test_planted_forest_w3_c60(self):
        """At c=60: delta_pf = (40-60)/48 = -20/48 = -5/12."""
        result = F2_w3(60)
        assert result['delta_pf_total'] == Rational(-5, 12)

    def test_planted_forest_w3_c40_vanishes(self):
        """At c=40: delta_pf = (40-40)/48 = 0. Special vanishing point."""
        result = F2_w3(40)
        assert result['delta_pf_total'] == Rational(0)

    def test_w3_status_conditional(self):
        """W_3 F_2 is CONDITIONAL because it is multi-weight."""
        result = F2_w3(50)
        assert 'CONDITIONAL' in result['status']

    def test_w3_T_line_data(self):
        """T-line shadow data: S_3 = 2 (identical to Virasoro)."""
        result = F2_w3(50)
        assert result['T_line']['S_3'] == Rational(2)

    def test_w3_W_line_data(self):
        """W-line shadow data: S_3 = 0 (Z_2 parity kills odd arities)."""
        result = F2_w3(50)
        assert result['W_line']['S_3'] == Rational(0)


# ============================================================================
# betagamma multi-weight detail
# ============================================================================

class TestBetagammaDetail:
    """Detailed tests for betagamma multi-weight status."""

    def test_lam1_multi_weight(self):
        """At lambda=1: beta weight 1, gamma weight 0. Multi-weight."""
        result = F2_betagamma(1)
        assert result['weight_beta'] == Rational(1)
        assert result['weight_gamma'] == Rational(0)
        assert not result['scalar_lane']

    def test_lam_half_uniform_weight(self):
        """At lambda=1/2: beta weight 1/2, gamma weight 1/2. Uniform weight."""
        result = F2_betagamma(Rational(1, 2))
        assert result['weight_beta'] == Rational(1, 2)
        assert result['weight_gamma'] == Rational(1, 2)
        assert result['scalar_lane']

    def test_lam_half_status_proved(self):
        """At lambda=1/2: uniform weight, so status is PROVED."""
        result = F2_betagamma(Rational(1, 2))
        assert result['status'] == 'PROVED'

    def test_lam1_status_conditional(self):
        """At lambda=1: multi-weight, so status is CONDITIONAL."""
        result = F2_betagamma(1)
        assert 'CONDITIONAL' in result['status']

    def test_lam_symmetry(self):
        """kappa(bg, lambda) = kappa(bg, 1-lambda)."""
        for lam_val in [0, Rational(1, 3), Rational(1, 2), 1]:
            lam_r = Rational(lam_val)
            assert kappa_betagamma(lam_r) == kappa_betagamma(1 - lam_r)


# ============================================================================
# Landscape table completeness
# ============================================================================

class TestLandscapeTable:
    """Verify the full landscape table is complete and consistent."""

    def test_six_families(self):
        """Table has exactly 6 entries."""
        table = genus2_landscape_table()
        assert len(table) == 6

    def test_all_families_present(self):
        """All six families appear in the table."""
        table = genus2_landscape_table()
        families = {v['family'] for v in table.values()}
        assert families == {'Heisenberg', 'Virasoro', 'Affine sl_2',
                            'W_3', 'betagamma', 'E_8 lattice'}

    def test_all_have_status(self):
        """Every entry has a status field."""
        table = genus2_landscape_table()
        for key, data in table.items():
            assert 'status' in data, f"Missing status for {key}"

    def test_all_have_shadow_class(self):
        """Every entry has a shadow class."""
        table = genus2_landscape_table()
        for key, data in table.items():
            assert 'shadow_class' in data, f"Missing shadow_class for {key}"

    def test_four_shadow_classes(self):
        """All four shadow classes G, L, C, M are represented."""
        table = genus2_landscape_table()
        classes = {v['shadow_class'] for v in table.values()}
        assert classes == {'G', 'L', 'C', 'M'}

    def test_scalar_lane_count(self):
        """Exactly 4 families are on the scalar lane, 2 are not."""
        table = genus2_landscape_table()
        scalar_count = sum(1 for v in table.values() if v['scalar_lane'])
        assert scalar_count == 4
        multi_count = sum(1 for v in table.values() if not v['scalar_lane'])
        assert multi_count == 2


# ============================================================================
# Cross-check with existing modules (AP10)
# ============================================================================

class TestCrossModuleConsistency:
    """Verify consistency with existing compute modules."""

    def test_kappa_heisenberg_matches(self):
        """Cross-check kappa_heisenberg with genus_expansion module."""
        from compute.lib.genus_expansion import kappa_heisenberg as kH_old
        assert kappa_heisenberg(1) == kH_old(1)

    def test_kappa_virasoro_matches(self):
        """Cross-check kappa_virasoro with genus_expansion module."""
        from compute.lib.genus_expansion import kappa_virasoro as kV_old
        assert kappa_virasoro(25) == kV_old(25)

    def test_kappa_sl2_matches(self):
        """Cross-check kappa_sl2 with genus_expansion module."""
        from compute.lib.genus_expansion import kappa_sl2 as kS_old
        assert kappa_affine_sl2(1) == kS_old(1)

    def test_kappa_w3_matches(self):
        """Cross-check kappa_w3 with genus_expansion module."""
        from compute.lib.genus_expansion import kappa_w3 as kW_old
        assert kappa_w3(50) == kW_old(50)

    def test_kappa_betagamma_matches(self):
        """Cross-check with betagamma_determinant module."""
        from compute.lib.betagamma_determinant import kappa_betagamma as kBG_old
        assert kappa_betagamma(1) == kBG_old(1)
        assert kappa_betagamma(0) == kBG_old(0)

    def test_lambda_fp_2_matches(self):
        """Cross-check lambda_2^FP with utils module."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp_2() == lambda_fp(2)

    def test_F2_matches_genus_expansion(self):
        """Cross-check F_2 with genus_expansion.F_g."""
        from compute.lib.utils import F_g
        for kappa_val in [1, Rational(25, 2), Rational(9, 4), 8]:
            assert F2_scalar(kappa_val) == F_g(kappa_val, 2)

    def test_planted_forest_matches_graph_engine(self):
        """Cross-check planted-forest formula with higher_genus_graph_sum_engine."""
        from fractions import Fraction as F
        from compute.lib.higher_genus_graph_sum_engine import planted_forest_correction_g2
        # Virasoro: alpha=2, kappa=c/2
        for c_val in [10, 25, 26, 40]:
            kappa_val = F(c_val, 2)
            alpha_val = F(2)
            engine_val = planted_forest_correction_g2(alpha_val, kappa_val)
            my_val = planted_forest_g2(Rational(2), Rational(c_val, 2))
            assert Rational(engine_val.numerator, engine_val.denominator) == my_val, \
                f"Mismatch at c={c_val}"
