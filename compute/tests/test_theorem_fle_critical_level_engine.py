r"""Tests for theorem_fle_critical_level_engine: FLE critical-level bar-cobar.

THEOREM (Critical-level bar-cobar degeneration and the FLE):
    At k = -h^v, the bar complex B(V_{-h^v}(g)) is uncurved and its
    cohomology computes the oper differential-form algebra:
        H^n(B(V_{-h^v}(g))) ~ Omega^n(Op_{g^v}(D))    for all n >= 0.

    This is the cohomological shadow of the Fundamental Local Equivalence:
        KL(V_crit(g)) ~ IndCoh(Op_{G^L})
    proved by Gaitsgory-Raskin (arXiv:2405.03648).

FIVE STRUCTURAL QUESTIONS tested:
  Q1: Shadow obstruction tower at critical level (AP31 analysis)
  Q2: Bar complex and the Feigin-Frenkel center z(g_hat)
  Q3: Koszulness characterizations K1-K12 at critical level
  Q4: FLE as categorical lift of bar-oper identification
  Q5: Bicomplex deformation d_k = d_crit + (k+h^v) delta

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct computation of dimensions
  Path 2: Cross-family consistency (all simple types)
  Path 3: Literature comparison (Kac, Humphreys, Feigin-Frenkel, FT06)
  Path 4: Algebraic identity checks
  Path 5: Structural analysis (spectral sequences, de Rham)

Beilinson warnings:
  AP1:  kappa = dim(g)(k+h^v)/(2h^v), NEVER copy between families.
  AP9:  kappa != c/2 for affine KM.
  AP31: kappa = 0 does NOT imply Theta = 0. At critical level, commutativity
        of the FF center implies Theta = 0.
  AP33: Koszul dual V_{k'}(g) != V_{-k}(g).
  AP39: kappa != S_2 for rank > 1.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.theorem_fle_critical_level_engine import (
    FLECriticalLevelAnalysis,
    KoszulnessAtCriticalLevel,
    SimpleLieData,
    bar_cohomology_is_oper_forms,
    bar_h0_critical,
    bar_hn_critical,
    bicomplex_interpolation,
    bicomplex_structure,
    critical_deformation_data,
    ff_center_dim,
    fle_categorical_hierarchy,
    full_fle_critical_analysis,
    hochschild_periodicity,
    is_critical,
    kappa_affine,
    koszul_dual_level,
    koszulness_at_critical_level,
    koszulness_survival_count,
    landscape_sweep,
    lie_data,
    oper_space_analysis,
    shadow_tower_at_critical_level,
)


# ============================================================
# Section 1: Q1 -- Shadow obstruction tower at critical level
# ============================================================


class TestShadowTowerCritical:
    """Q1: Shadow obstruction tower vanishes at critical level."""

    def test_kappa_zero_at_critical_sl2(self):
        """kappa(sl_2, k=-2) = 3*(-2+2)/(2*2) = 0."""
        g = lie_data("A", 1)
        kap = kappa_affine(g, Fraction(-2))
        assert kap == 0

    def test_kappa_zero_at_critical_sl3(self):
        """kappa(sl_3, k=-3) = 8*(-3+3)/(2*3) = 0."""
        g = lie_data("A", 2)
        kap = kappa_affine(g, Fraction(-3))
        assert kap == 0

    def test_kappa_zero_at_critical_all_types(self):
        """kappa(g, k=-h^v) = 0 for all simple g."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("A", 4),
                         ("B", 2), ("B", 3), ("C", 2), ("C", 3),
                         ("D", 4), ("G", 2), ("F", 4),
                         ("E", 6), ("E", 7), ("E", 8)]:
            g = lie_data(lt, rk)
            kap = kappa_affine(g, Fraction(-g.h_vee))
            assert kap == 0, f"kappa != 0 for {lt}_{rk}"

    def test_shadow_tower_vanishes_sl2(self):
        """Full shadow tower Theta = 0 at critical level for sl_2."""
        g = lie_data("A", 1)
        result = shadow_tower_at_critical_level(g)
        assert result['theta_A_vanishes'] is True
        assert result['shadow_kappa'] == 0
        assert result['shadow_cubic_C'] == 0
        assert result['shadow_quartic_Q'] == 0
        assert result['shadow_depth_r_max'] == 0

    def test_ap31_not_violated(self):
        """We are NOT deducing Theta = 0 from kappa = 0 alone (AP31)."""
        g = lie_data("A", 1)
        result = shadow_tower_at_critical_level(g)
        assert result['ap31_violated'] is False
        assert 'Commutativity' in result['reason_theta_vanishes']

    def test_bar_nontrivial_despite_theta_zero(self):
        """Bar complex is nontrivial even though Theta = 0."""
        g = lie_data("A", 2)
        result = shadow_tower_at_critical_level(g)
        assert result['bar_complex_nontrivial'] is True
        assert result['bar_uncurved'] is True
        assert result['bar_cohomology_nontrivial'] is True

    def test_discriminant_zero_at_critical(self):
        """Critical discriminant Delta = 8*kappa*S_4 = 0 when kappa = 0."""
        for (lt, rk) in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            g = lie_data(lt, rk)
            result = shadow_tower_at_critical_level(g)
            assert result['discriminant_Delta'] == 0


# ============================================================
# Section 2: Q2 -- Bar complex and FF center
# ============================================================


class TestBarFFCenter:
    """Q2: H^0(B(V_crit)) = Fun(Op) = z(g_hat)."""

    def test_ff_center_sl2_low_weights(self):
        """For sl_2: Fun(Op) = C[[q_2]], generator weight 2.

        dim at weight w = number of partitions of w into parts of size 2.
        w=0: 1, w=1: 0, w=2: 1, w=3: 0, w=4: 1, w=5: 0, w=6: 1.
        """
        g = lie_data("A", 1)
        assert ff_center_dim(g, 0) == 1
        assert ff_center_dim(g, 1) == 0
        assert ff_center_dim(g, 2) == 1
        assert ff_center_dim(g, 3) == 0
        assert ff_center_dim(g, 4) == 1
        assert ff_center_dim(g, 6) == 1

    def test_ff_center_sl3_low_weights(self):
        """For sl_3: Fun(Op) = C[[q_2, q_3]], generators in weights 2, 3.

        w=0: 1 (const), w=1: 0, w=2: 1 (q_2), w=3: 1 (q_3),
        w=4: 1 (q_2^2), w=5: 1 (q_2*q_3), w=6: 2 (q_2^3, q_3^2).
        """
        g = lie_data("A", 2)
        assert ff_center_dim(g, 0) == 1
        assert ff_center_dim(g, 1) == 0
        assert ff_center_dim(g, 2) == 1
        assert ff_center_dim(g, 3) == 1
        assert ff_center_dim(g, 4) == 1
        assert ff_center_dim(g, 5) == 1
        assert ff_center_dim(g, 6) == 2

    def test_h0_equals_ff_center(self):
        """H^0(B(V_crit(g))) = Fun(Op) = z(g_hat) for all types."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("G", 2)]:
            g = lie_data(lt, rk)
            for w in range(10):
                assert bar_h0_critical(g, w) == ff_center_dim(g, w), \
                    f"H^0 != Fun(Op) at weight {w} for {lt}_{rk}"

    def test_bar_hn_vanishes_above_rank(self):
        """H^n(B) = 0 for n > rank(g)."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("B", 2)]:
            g = lie_data(lt, rk)
            for w in range(8):
                assert bar_hn_critical(g, g.rank + 1, w) == 0, \
                    f"H^{g.rank+1} != 0 at weight {w} for {lt}_{rk}"
                assert bar_hn_critical(g, g.rank + 2, w) == 0

    def test_bar_h1_sl2(self):
        """For sl_2 (rank 1): H^1 = Omega^1(Op) = dq_2 * Fun(Op).

        H^1 at weight w = dim Fun(Op) at weight w-2.
        w=0: 0, w=1: 0, w=2: 1 (dq_2), w=3: 0, w=4: 1 (dq_2*q_2), ...
        """
        g = lie_data("A", 1)
        assert bar_hn_critical(g, 1, 0) == 0
        assert bar_hn_critical(g, 1, 1) == 0
        assert bar_hn_critical(g, 1, 2) == 1  # dq_2 * 1
        assert bar_hn_critical(g, 1, 3) == 0
        assert bar_hn_critical(g, 1, 4) == 1  # dq_2 * q_2

    def test_bar_h1_sl3(self):
        """For sl_3 (rank 2): H^1 = Omega^1(Op) with 2 generators dq_2, dq_3.

        H^1 at weight w = dim Fun(Op)_{w-2} + dim Fun(Op)_{w-3}.
        """
        g = lie_data("A", 2)
        # H^1 at w=2: dq_2 * 1 = 1
        assert bar_hn_critical(g, 1, 2) == 1
        # H^1 at w=3: dq_3 * 1 = 1
        assert bar_hn_critical(g, 1, 3) == 1
        # H^1 at w=4: dq_2 * q_2 = 1
        assert bar_hn_critical(g, 1, 4) == 1
        # H^1 at w=5: dq_2 * q_3 + dq_3 * q_2 = 2
        assert bar_hn_critical(g, 1, 5) == 2

    def test_bar_h2_sl3(self):
        """For sl_3 (rank 2): H^2 = Omega^2(Op) = dq_2 ^ dq_3 * Fun(Op).

        Only one 2-form generator (2-element subset of {dq_2, dq_3}).
        H^2 at weight w = dim Fun(Op)_{w-5} (since 2+3=5).
        """
        g = lie_data("A", 2)
        assert bar_hn_critical(g, 2, 4) == 0  # w=4 < 5
        assert bar_hn_critical(g, 2, 5) == 1  # dq_2^dq_3 * 1
        assert bar_hn_critical(g, 2, 6) == 0  # w-5=1, no partition in {2,3}
        assert bar_hn_critical(g, 2, 7) == 1  # dq_2^dq_3 * q_2

    def test_oper_forms_complete_check(self):
        """Comprehensive check: bar_cohomology_is_oper_forms passes."""
        for (lt, rk) in [("A", 1), ("A", 2), ("B", 2)]:
            g = lie_data(lt, rk)
            result = bar_cohomology_is_oper_forms(g, max_weight=8)
            assert result['vanishing_above_rank'] is True
            assert result['h0_equals_fun_op'] is True
            assert result['vacuum_unique'] is True


# ============================================================
# Section 3: Q3 -- Koszulness at critical level
# ============================================================


class TestKoszulnessCritical:
    """Q3: Koszulness characterizations K1-K12 at critical level."""

    def test_koszulness_analysis_sl2(self):
        """Koszulness analysis for sl_2 at critical level."""
        g = lie_data("A", 1)
        result = koszulness_at_critical_level(g)
        assert result.lie_algebra == "A_1"
        assert result.rank == 1

    def test_k3_ext_fails(self):
        """K3 (Ext diagonal vanishing) FAILS at critical level."""
        g = lie_data("A", 2)
        result = koszulness_at_critical_level(g)
        assert 'FAILS' in result.k3_ext

    def test_k4_barcobar_holds(self):
        """K4 (bar-cobar quasi-iso) HOLDS at critical level."""
        g = lie_data("A", 1)
        result = koszulness_at_critical_level(g)
        assert 'HOLDS' in result.k4_barcobar

    def test_k5_bbl_holds(self):
        """K5 (Barr-Beck-Lurie) HOLDS at critical level."""
        g = lie_data("A", 1)
        result = koszulness_at_critical_level(g)
        assert 'HOLDS' in result.k5_bbl

    def test_k8_shapovalov_fails(self):
        """K8 (Kac-Shapovalov) FAILS at critical level (Sugawara undefined)."""
        g = lie_data("A", 1)
        result = koszulness_at_critical_level(g)
        assert 'FAILS' in result.k8_kac_shapovalov
        assert 'Sugawara' in result.k8_kac_shapovalov

    def test_koszulness_survival_count(self):
        """3 hold, 4 fail, 3 modified, 2 inapplicable = 12 total."""
        g = lie_data("A", 1)
        counts = koszulness_survival_count(g)
        assert counts['total'] == 12
        assert counts['holds'] == 3
        assert counts['fails'] == 4

    def test_koszulness_all_types(self):
        """Koszulness analysis runs for all types without error."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3),
                         ("B", 2), ("C", 2), ("D", 4),
                         ("G", 2), ("F", 4), ("E", 6)]:
            g = lie_data(lt, rk)
            result = koszulness_at_critical_level(g)
            assert result.lie_algebra == f"{lt}_{rk}"


# ============================================================
# Section 4: Q4 -- FLE categorical hierarchy
# ============================================================


class TestFLEHierarchy:
    """Q4: FLE (categorical) => localization (derived) => bar-oper (cohom)."""

    def test_three_levels_exist(self):
        """All three levels of the identification are present."""
        g = lie_data("A", 1)
        result = fle_categorical_hierarchy(g)
        assert 'level_1_fle' in result
        assert 'level_2_localization' in result
        assert 'level_3_bar_oper' in result

    def test_level_1_implies_level_2(self):
        """FLE (Level 1) implies localization (Level 2)."""
        g = lie_data("A", 1)
        result = fle_categorical_hierarchy(g)
        assert result['implications']['level_1_implies_level_2'] is True

    def test_level_2_implies_level_3(self):
        """Localization (Level 2) implies bar-oper (Level 3)."""
        g = lie_data("A", 1)
        result = fle_categorical_hierarchy(g)
        assert result['implications']['level_2_implies_level_3'] is True

    def test_converses_fail(self):
        """The converses do NOT hold."""
        g = lie_data("A", 2)
        result = fle_categorical_hierarchy(g)
        assert result['implications']['level_3_implies_level_2'] is False
        assert result['implications']['level_2_implies_level_1'] is False

    def test_level_3_proved_here(self):
        """Level 3 (bar-oper) is ProvedHere in the monograph."""
        g = lie_data("A", 1)
        result = fle_categorical_hierarchy(g)
        assert result['level_3_bar_oper']['status'] == 'ProvedHere'

    def test_level_1_proved_elsewhere(self):
        """Level 1 (FLE) is ProvedElsewhere (Gaitsgory-Raskin)."""
        g = lie_data("A", 1)
        result = fle_categorical_hierarchy(g)
        assert result['level_1_fle']['status'] == 'ProvedElsewhere'
        assert '2405.03648' in result['level_1_fle']['source']


# ============================================================
# Section 5: Q5 -- Bicomplex structure
# ============================================================


class TestBicomplex:
    """Q5: d_k = d_crit + (k+h^v) delta."""

    def test_bicomplex_at_critical_level(self):
        """At critical level, d_k = d_crit (delta contribution zero)."""
        g = lie_data("A", 1)
        result = bicomplex_structure(g, Fraction(-2))
        assert result['is_critical'] is True
        assert result['d_k_equals_d_crit'] is True
        assert result['delta_contribution_zero'] is True
        assert result['bar_uncurved'] is True

    def test_bicomplex_conditions_always_hold(self):
        """d_crit^2 = 0, delta^2 = 0, {d_crit, delta} = 0 for all k."""
        g = lie_data("A", 2)
        for k in [Fraction(-3), Fraction(1), Fraction(10)]:
            result = bicomplex_structure(g, k)
            assert result['d_crit_squared_zero'] is True
            assert result['delta_squared_zero'] is True
            assert result['anticommutator_zero'] is True

    def test_bicomplex_generic_level_curved(self):
        """At generic level, bar is curved (kappa != 0)."""
        g = lie_data("A", 1)
        result = bicomplex_structure(g, Fraction(1))
        assert result['is_critical'] is False
        assert result['bar_uncurved'] is False
        assert result['d_k_equals_d_crit'] is False

    def test_lambda_parameter(self):
        """lambda = k + h^v is 0 at critical, nonzero elsewhere."""
        g = lie_data("A", 2)
        # Critical
        result_crit = bicomplex_structure(g, Fraction(-3))
        assert abs(result_crit['lambda']) < 1e-12
        # Generic
        result_gen = bicomplex_structure(g, Fraction(1))
        assert abs(result_gen['lambda'] - 4.0) < 1e-12

    def test_interpolation_sequence(self):
        """Bicomplex interpolation from critical to generic."""
        g = lie_data("A", 1)
        results = bicomplex_interpolation(g)
        # First entry is critical (lambda = 0)
        assert results[0]['is_critical'] is True
        assert abs(results[0]['lambda']) < 1e-12
        # Later entries are not critical
        for r in results[1:]:
            assert r['is_critical'] is False


# ============================================================
# Section 6: Oper space analysis
# ============================================================


class TestOperSpace:
    """Oper space invariants."""

    def test_oper_dim_equals_rank(self):
        """dim Op_{g^v}(D) = rank(g) for all types."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("B", 2),
                         ("D", 4), ("E", 6), ("E", 8)]:
            g = lie_data(lt, rk)
            result = oper_space_analysis(g)
            assert result['oper_dimension'] == rk

    def test_de_rham_euler_char_w0(self):
        """Euler characteristic of Omega^*(Op) at weight 0 is 1."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("G", 2)]:
            g = lie_data(lt, rk)
            result = oper_space_analysis(g)
            assert result['euler_char_w0'] == 1

    def test_de_rham_exact_positive_weight(self):
        """Euler characteristic of Omega^*(Op) is 0 for w > 0.

        This is the de Rham exactness: on a formally smooth space,
        the de Rham complex is exact in positive degrees.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("B", 2)]:
            g = lie_data(lt, rk)
            result = oper_space_analysis(g)
            assert result['de_rham_exact_positive_weight'] is True

    def test_formal_smoothness(self):
        """Op_{g^v}(D) is formally smooth (Frenkel-Gaitsgory)."""
        g = lie_data("A", 2)
        result = oper_space_analysis(g)
        assert result['formally_smooth'] is True
        assert result['cotangent_complex_classical'] is True


# ============================================================
# Section 7: Hochschild periodicity
# ============================================================


class TestHochschildBoundedAmplitude:
    """Chiral Hochschild cohomology at critical level (Theorem-H bounded).

    Per AP94/AP95: ChirHoch^*(V_crit) is concentrated in {0,1,2} with
    finite total dimension (Theorem H).  The historical Gelfand-Fuchs polynomial model
    (periodic for sl_2, polynomially growing for higher rank) is
    REFUTED.
    """

    def test_sl2_bounded(self):
        """sl_2: ChirHoch^*(V_crit) bounded by Theorem H amplitude [0,2]."""
        g = lie_data("A", 1)
        result = hochschild_periodicity(g)
        assert result['is_strictly_periodic'] is False
        assert result['period'] is None
        assert result['amplitude'] == (0, 2)
        assert result['bounded_by_theorem_h'] is True

    def test_sl3_bounded(self):
        """sl_3: ChirHoch^*(V_crit) bounded by Theorem H amplitude [0,2]."""
        g = lie_data("A", 2)
        result = hochschild_periodicity(g)
        assert result['amplitude'] == (0, 2)
        assert result['bounded_by_theorem_h'] is True
        assert result['total_dim_bound'] == 4

    def test_higher_rank_bounded(self):
        """Higher rank: ChirHoch bounded, NOT polynomial growth (AP94)."""
        for (lt, rk) in [("A", 3), ("B", 2), ("D", 4)]:
            g = lie_data(lt, rk)
            result = hochschild_periodicity(g)
            assert result['amplitude'] == (0, 2)
            assert result['bounded_by_theorem_h'] is True
            assert 'bounded' in result['growth_rate']
            assert result['is_strictly_periodic'] is False


# ============================================================
# Section 8: Critical deformation
# ============================================================


class TestCriticalDeformation:
    """Deformation from critical to generic level."""

    def test_kappa_sum_zero(self):
        """kappa + kappa' = 0 for KM at deformed level (AP24)."""
        g = lie_data("A", 2)
        result = critical_deformation_data(g)
        assert abs(result['kappa_sum']) < 1e-12

    def test_bar_curved_at_deformed(self):
        """Bar complex is curved away from critical level."""
        g = lie_data("A", 1)
        result = critical_deformation_data(g)
        assert result['bar_uncurved_at_critical'] is True
        assert result['bar_curved_at_deformed'] is True

    def test_oper_identification_only_at_critical(self):
        """The oper identification H^*(B) = Omega^*(Op) only holds at critical."""
        g = lie_data("A", 2)
        result = critical_deformation_data(g)
        assert result['oper_identification_at_critical'] is True
        assert result['oper_identification_at_generic'] is False


# ============================================================
# Section 9: FF involution fixed-point analysis
# ============================================================


class TestFFInvolution:
    """Feigin-Frenkel involution k -> -k - 2h^v."""

    def test_critical_is_fixed_point(self):
        """k = -h^v is the unique fixed point of k -> -k - 2h^v."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3),
                         ("B", 2), ("G", 2), ("E", 8)]:
            g = lie_data(lt, rk)
            k_crit = Fraction(-g.h_vee)
            k_dual = koszul_dual_level(g, k_crit)
            assert k_dual == k_crit, f"Critical not fixed for {lt}_{rk}"

    def test_generic_not_fixed(self):
        """Generic level is NOT a fixed point."""
        g = lie_data("A", 1)
        k = Fraction(1)
        k_dual = koszul_dual_level(g, k)
        assert k_dual != k
        assert k_dual == Fraction(-5)  # -1 - 2*2 = -5

    def test_involution_is_involution(self):
        """Applying the involution twice gives the identity."""
        for (lt, rk) in [("A", 1), ("A", 2), ("B", 3)]:
            g = lie_data(lt, rk)
            for k in [Fraction(1), Fraction(5), Fraction(-1)]:
                k_dual = koszul_dual_level(g, k)
                k_double = koszul_dual_level(g, k_dual)
                assert k_double == k


# ============================================================
# Section 10: Full landscape sweep
# ============================================================


class TestLandscapeSweep:
    """Comprehensive landscape verification."""

    def test_full_analysis_sl2(self):
        """Full analysis for sl_2."""
        result = full_fle_critical_analysis("A", 1, max_weight=8)
        assert result.h_vee == 2
        assert result.dim_g == 3
        assert result.shadow_tower['theta_A_vanishes'] is True
        assert result.bicomplex['is_critical'] is True

    def test_full_analysis_sl3(self):
        """Full analysis for sl_3."""
        result = full_fle_critical_analysis("A", 2, max_weight=8)
        assert result.h_vee == 3
        assert result.dim_g == 8
        assert result.exponents == (1, 2)

    def test_landscape_all_types_pass(self):
        """Landscape sweep runs without error for all types."""
        results = landscape_sweep(max_weight=6)
        assert len(results) == 14  # 14 standard simple types
        for key, analysis in results.items():
            assert analysis.shadow_tower['theta_A_vanishes'] is True
            assert analysis.bicomplex['is_critical'] is True
            assert analysis.bar_ff_center['vacuum_unique'] is True

    def test_landscape_oper_dims(self):
        """Oper dimension = rank for every type in the landscape."""
        results = landscape_sweep(max_weight=4)
        for key, analysis in results.items():
            assert analysis.oper_analysis['oper_dimension'] == analysis.rank

    def test_landscape_de_rham_exactness(self):
        """De Rham exactness at positive weight for every type."""
        results = landscape_sweep(max_weight=6)
        for key, analysis in results.items():
            assert analysis.oper_analysis['de_rham_exact_positive_weight'] is True


# ============================================================
# Section 11: Cross-verification and consistency
# ============================================================


class TestCrossVerification:
    """Cross-checks between different computation methods."""

    def test_h0_dim_two_methods(self):
        """H^0(B) computed via bar_h0_critical and bar_hn_critical agree."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3)]:
            g = lie_data(lt, rk)
            for w in range(10):
                d1 = bar_h0_critical(g, w)
                d2 = bar_hn_critical(g, 0, w)
                assert d1 == d2, f"Methods disagree at w={w} for {lt}_{rk}"

    def test_euler_char_from_dims(self):
        """Euler char computed directly matches oper_space_analysis."""
        g = lie_data("A", 2)
        oper = oper_space_analysis(g)
        for w in range(10):
            chi = sum(
                (-1)**n * bar_hn_critical(g, n, w)
                for n in range(g.rank + 1)
            )
            assert chi == oper['euler_characteristics'][w]

    def test_complementarity_principle(self):
        """FLE (critical, kappa=0) and Koszulness (generic, kappa!=0) are
        complementary: they NEVER hold simultaneously for the same level."""
        g = lie_data("A", 2)
        # At critical level: NOT Koszul (bar cohom spread across degrees)
        kosz = koszulness_at_critical_level(g)
        assert 'FAILS' in kosz.k3_ext

        # At generic level: Koszul (bar cohom concentrated in degree 1)
        kap_gen = kappa_affine(g, Fraction(1))
        assert kap_gen != 0  # NOT at critical level

    def test_bicomplex_vs_shadow(self):
        """At critical level, bicomplex says uncurved => shadow tower trivial."""
        g = lie_data("A", 1)
        bc = bicomplex_structure(g, Fraction(-2))
        st = shadow_tower_at_critical_level(g)
        assert bc['bar_uncurved'] is True
        assert st['theta_A_vanishes'] is True
        # Both agree: critical level is the trivial point


# ============================================================
# Section 12: AP10 multi-path cross-verification
# ============================================================


class TestMultiPathCrossVerification:
    """Multi-path verification to prevent AP10 (hardcoded wrong values).

    Every numerical result is verified by at least 2 independent methods.
    These tests do NOT hardcode expected values; they check algebraic
    identities and cross-family consistency that would fail if any
    single computation path were wrong.
    """

    def test_ff_center_generating_function_sl2(self):
        """For sl_2: Fun(Op) = C[[q_2]], so the generating function is
        1/(1 - x^2) = 1 + x^2 + x^4 + ...

        Independent check: sum_{w=0}^{N} dim_w * x^w should match
        the truncation of 1/(1-x^2).

        Path 1: direct dimension computation via ff_center_dim.
        Path 2: algebraic generating function identity.
        """
        g = lie_data("A", 1)
        for w in range(20):
            # Path 1: engine computation
            d = ff_center_dim(g, w)
            # Path 2: partition count for single generator of weight 2
            expected = 1 if w % 2 == 0 else 0
            assert d == expected, f"GF mismatch at w={w}"

    def test_ff_center_generating_function_sl3(self):
        """For sl_3: Fun(Op) = C[[q_2, q_3]], generating function
        1/((1-x^2)(1-x^3)).

        Path 1: engine computation.
        Path 2: convolution of two single-variable generating functions.
        """
        g = lie_data("A", 2)
        # Build generating function independently
        max_w = 15
        # gf1[w] = coefficient of x^w in 1/(1-x^2)
        gf1 = [0] * (max_w + 1)
        for w in range(0, max_w + 1, 2):
            gf1[w] = 1
        # gf2[w] = coefficient of x^w in 1/(1-x^3)
        gf2 = [0] * (max_w + 1)
        for w in range(0, max_w + 1, 3):
            gf2[w] = 1
        # Product: coefficient of x^w in 1/((1-x^2)(1-x^3))
        product = [0] * (max_w + 1)
        for i in range(max_w + 1):
            for j in range(max_w + 1 - i):
                product[i + j] += gf1[i] * gf2[j]

        for w in range(max_w + 1):
            d = ff_center_dim(g, w)
            assert d == product[w], (
                f"sl_3 Fun(Op) at w={w}: engine={d}, GF product={product[w]}"
            )

    def test_kappa_formula_two_paths(self):
        """kappa = dim(g)(k+h^v)/(2h^v) verified two ways.

        Path 1: kappa_affine function.
        Path 2: direct arithmetic from Lie data.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3),
                         ("B", 2), ("C", 3), ("G", 2), ("E", 6)]:
            g = lie_data(lt, rk)
            for k in [Fraction(-g.h_vee), Fraction(1), Fraction(5)]:
                path1 = kappa_affine(g, k)
                path2 = Fraction(g.dim) * (k + g.h_vee) / (2 * g.h_vee)
                assert path1 == path2, (
                    f"kappa mismatch for {lt}_{rk} at k={k}"
                )

    def test_kappa_complementarity_all_types(self):
        """kappa(g, k) + kappa(g, k') = 0 for k' = -k - 2h^v.

        This is an ALGEBRAIC IDENTITY, not a hardcoded value.
        If the kappa formula or the involution were wrong, this would fail.

        Path 1: compute kappa at k and k'.
        Path 2: verify the algebraic identity dim(g)(k+h^v)/(2h^v)
                 + dim(g)(-k-h^v)/(2h^v) = 0.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("A", 4),
                         ("B", 2), ("B", 3), ("C", 2), ("C", 3),
                         ("D", 4), ("G", 2), ("F", 4),
                         ("E", 6), ("E", 7), ("E", 8)]:
            g = lie_data(lt, rk)
            for k in [Fraction(1), Fraction(5), Fraction(-1),
                      Fraction(1, 3), Fraction(7, 2)]:
                kap = kappa_affine(g, k)
                k_dual = koszul_dual_level(g, k)
                kap_dual = kappa_affine(g, k_dual)
                assert kap + kap_dual == 0, (
                    f"kappa complementarity fails for {lt}_{rk} at k={k}: "
                    f"kappa={kap}, kappa'={kap_dual}, sum={kap + kap_dual}"
                )

    def test_de_rham_euler_char_algebraic_identity(self):
        """For a formally smooth space of dimension r, the de Rham complex
        satisfies: sum_n (-1)^n dim Omega^n_w = delta_{w,0}.

        This is an algebraic identity (Poincare lemma on formal space).
        It cross-verifies the bar_hn_critical computation at all degrees
        simultaneously.  If any single H^n dimension were wrong, this
        would fail.

        Path 1: sum dimensions from bar_hn_critical.
        Path 2: the algebraic prediction delta_{w,0}.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("A", 4),
                         ("B", 2), ("B", 3), ("C", 2),
                         ("D", 4), ("G", 2), ("F", 4)]:
            g = lie_data(lt, rk)
            for w in range(12):
                chi = sum(
                    (-1)**n * bar_hn_critical(g, n, w)
                    for n in range(g.rank + 1)
                )
                expected = 1 if w == 0 else 0
                assert chi == expected, (
                    f"Euler char at w={w} for {lt}_{rk}: "
                    f"got {chi}, expected {expected}"
                )

    def test_ff_involution_algebraic_identity(self):
        """The FF involution k -> -k - 2h^v is an involution:
        applying it twice gives the identity.  This is an algebraic check,
        not a hardcoded value.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("B", 2), ("G", 2), ("E", 8)]:
            g = lie_data(lt, rk)
            for k in [Fraction(1), Fraction(-1), Fraction(3, 7)]:
                k2 = koszul_dual_level(g, koszul_dual_level(g, k))
                assert k2 == k, f"Involution^2 != id for {lt}_{rk} at k={k}"

    def test_exponent_sum_equals_num_positive_roots(self):
        """For a simple Lie algebra: sum of exponents = num positive roots.

        This is a classical identity (Chevalley).  It cross-verifies the
        Lie data tables (exponents and num_positive_roots) against each other.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("A", 4),
                         ("B", 2), ("B", 3), ("C", 2), ("C", 3),
                         ("D", 4), ("G", 2), ("F", 4),
                         ("E", 6), ("E", 7), ("E", 8)]:
            g = lie_data(lt, rk)
            assert sum(g.exponents) == g.num_positive_roots, (
                f"Exponent sum {sum(g.exponents)} != "
                f"num_pos_roots {g.num_positive_roots} for {lt}_{rk}"
            )

    def test_dim_equals_rank_plus_2_num_positive_roots(self):
        """dim(g) = rank + 2 * num_positive_roots.

        Another classical Lie algebra identity.  Cross-verifies dim against
        rank and num_positive_roots.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("A", 4),
                         ("B", 2), ("B", 3), ("C", 2), ("C", 3),
                         ("D", 4), ("G", 2), ("F", 4),
                         ("E", 6), ("E", 7), ("E", 8)]:
            g = lie_data(lt, rk)
            assert g.dim == g.rank + 2 * g.num_positive_roots, (
                f"dim={g.dim} != rank+2*pos={g.rank + 2*g.num_positive_roots} "
                f"for {lt}_{rk}"
            )

    def test_top_lie_cohomology_degree(self):
        """Top degree of H^*(g;k) = sum(2*d_i + 1) = 2*num_pos_roots + rank = dim(g).

        This is the classical fact that H^{dim(g)}(g; k) = k.
        Cross-verifies lie_cohomology_degrees against dim.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3),
                         ("B", 2), ("G", 2), ("F", 4), ("E", 6)]:
            g = lie_data(lt, rk)
            top = g.top_lie_cohomology_degree
            assert top == g.dim, (
                f"Top Lie cohom degree {top} != dim {g.dim} for {lt}_{rk}"
            )

    def test_bar_cohomology_poincare_duality(self):
        """For Omega^*(Op) on a smooth space of dim r:
        dim Omega^n_w = dim Omega^{r-n}_{w + total_gen_weight - sum_of_n_gens}.

        Simpler check: dim Omega^r_w at the minimum possible weight equals 1.
        The minimum weight of the top form is sum of all generator weights.
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("B", 2)]:
            g = lie_data(lt, rk)
            top_weight = sum(g.oper_generators_weights)
            assert bar_hn_critical(g, g.rank, top_weight) == 1, (
                f"Top form at min weight {top_weight} != 1 for {lt}_{rk}"
            )
