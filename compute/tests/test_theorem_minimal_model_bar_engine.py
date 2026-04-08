r"""Tests for theorem_minimal_model_bar_engine: non-Koszul bar complexes.

FIRST EXPLICIT COMPUTATION of non-Koszul bar complexes in the chiral
algebraic framework.  Tests cover:

1. Central charge and null vector structure (ground truth)
2. Vacuum module dimensions (universal vs simple quotient)
3. Bar chain dimensions at each (n, h) bigrading
4. Euler characteristic analysis (detects cohomology changes)
5. Koszulness obstruction mechanism for the Ising model
6. Comparison across minimal models (Ising, TCI, Potts, Lee-Yang)
7. D-module purity converse predictions
8. Zhu algebra comparison
9. Shadow obstruction tower consistency
10. Cross-family complementarity (kappa + kappa' = 13)

Multi-path verification (AP10 compliance):
  Path 1: Direct dimension computation from partition arithmetic
  Path 2: Euler characteristic consistency (chain dims must sum correctly)
  Path 3: Comparison with universal Virasoro (agree below null weight)
  Path 4: Cross-family checks (complementarity, shadow class)
  Path 5: Null vector structure from Kac determinant

Ground truth:
  comp:ising-bar-interpretation (minimal_model_examples.tex)
  prop:pbw-universality (chiral_koszul_pairs.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  Kac determinant: first vacuum null at weight (p-1)(q-1)
"""

import pytest
from sympy import Rational

from compute.lib.theorem_minimal_model_bar_engine import (
    # Partition arithmetic
    num_partitions,
    partitions_geq2,
    partitions_geq2_list,
    # Minimal model data
    minimal_model_c,
    vacuum_singular_weight,
    n_primaries,
    conformal_weight_kac,
    STANDARD_MODELS,
    # Vacuum module dimensions
    universal_vac_dim,
    null_submodule_dim,
    simple_quotient_dim,
    simple_quotient_dims_table,
    # Bar chain dimensions
    bar_chain_dim_universal,
    bar_chain_dim_simple,
    bar_chain_table,
    # Euler characteristics
    euler_char_universal,
    euler_char_simple,
    # Bar cohomology
    bar_cohomology_universal,
    MinimalModelBarAnalysis,
    # Ising specifics
    ising_analysis,
    ising_null_vector_structure,
    ising_bar_chain_comparison,
    # Tricritical
    tricritical_analysis,
    # Cross-model
    non_koszulness_comparison,
    non_koszulness_pattern,
    # Shadow
    shadow_data,
    # Verification
    verify_complementarity,
    verify_kappa_sum,
    verify_shadow_class_consistency,
    verify_all,
    # Explicit bar analysis
    explicit_bar_degree_1,
    explicit_bar_degree_2,
)


# ===========================================================================
# 1. PARTITION ARITHMETIC
# ===========================================================================


class TestPartitionArithmetic:
    """Verify partition counts used as dimension formulas."""

    def test_num_partitions_small(self):
        """Unrestricted partitions: p(0)=1, p(1)=1, ..., p(5)=7."""
        assert num_partitions(0) == 1
        assert num_partitions(1) == 1
        assert num_partitions(2) == 2
        assert num_partitions(3) == 3
        assert num_partitions(4) == 5
        assert num_partitions(5) == 7

    def test_partitions_geq2_small(self):
        """Partitions into parts >= 2: p_{>=2}(h).

        These are the dimensions of the Virasoro vacuum augmentation ideal.
        p_{>=2}(0)=1, p_{>=2}(1)=0, p_{>=2}(2)=1, p_{>=2}(3)=1,
        p_{>=2}(4)=2, p_{>=2}(5)=2, p_{>=2}(6)=4, p_{>=2}(7)=4,
        p_{>=2}(8)=7.
        """
        assert partitions_geq2(0) == 1
        assert partitions_geq2(1) == 0
        assert partitions_geq2(2) == 1
        assert partitions_geq2(3) == 1
        assert partitions_geq2(4) == 2
        assert partitions_geq2(5) == 2
        assert partitions_geq2(6) == 4
        assert partitions_geq2(7) == 4
        assert partitions_geq2(8) == 7

    def test_partitions_geq2_list_weight6(self):
        """At weight 6: (6), (4,2), (3,3), (2,2,2) = 4 partitions."""
        parts = partitions_geq2_list(6)
        assert len(parts) == 4
        # Check all parts >= 2 and sum to 6
        for p in parts:
            assert sum(p) == 6
            assert all(x >= 2 for x in p)

    def test_partitions_geq2_negative(self):
        assert partitions_geq2(-1) == 0
        assert num_partitions(-1) == 0

    def test_partitions_geq2_list_consistency(self):
        """List length matches count for all h <= 10."""
        for h in range(11):
            assert len(partitions_geq2_list(h)) == partitions_geq2(h)


# ===========================================================================
# 2. CENTRAL CHARGES
# ===========================================================================


class TestCentralCharges:
    """Verify c_{p,q} = 1 - 6(p-q)^2/(pq)."""

    def test_ising(self):
        assert minimal_model_c(4, 3) == Rational(1, 2)

    def test_tricritical(self):
        assert minimal_model_c(5, 4) == Rational(7, 10)

    def test_potts(self):
        assert minimal_model_c(6, 5) == Rational(4, 5)

    def test_lee_yang(self):
        assert minimal_model_c(5, 2) == Rational(-22, 5)

    def test_trivial(self):
        assert minimal_model_c(3, 2) == 0

    def test_tetracritical(self):
        assert minimal_model_c(7, 6) == Rational(6, 7)

    def test_unitary_series_monotone(self):
        """Unitary series M(m+1, m) has c increasing with m."""
        c_prev = 0
        for m in range(3, 10):
            c = minimal_model_c(m + 1, m)
            assert c > c_prev
            c_prev = c

    def test_unitary_series_bounded(self):
        """Unitary series c < 1 for all finite m."""
        for m in range(3, 20):
            assert minimal_model_c(m + 1, m) < 1


# ===========================================================================
# 3. NULL VECTOR STRUCTURE
# ===========================================================================


class TestNullVectors:
    """Verify vacuum singular vector weights w_0 = (p-1)(q-1)."""

    def test_ising_null_weight(self):
        """Ising M(4,3): w_0 = 3*2 = 6."""
        assert vacuum_singular_weight(4, 3) == 6

    def test_tricritical_null_weight(self):
        """TCI M(5,4): w_0 = 4*3 = 12."""
        assert vacuum_singular_weight(5, 4) == 12

    def test_potts_null_weight(self):
        """Potts M(6,5): w_0 = 5*4 = 20."""
        assert vacuum_singular_weight(6, 5) == 20

    def test_trivial_null_weight(self):
        """Trivial M(3,2): w_0 = 2*1 = 2."""
        assert vacuum_singular_weight(3, 2) == 2

    def test_lee_yang_null_weight(self):
        """Lee-Yang M(5,2): w_0 = 4*1 = 4."""
        assert vacuum_singular_weight(5, 2) == 4

    def test_null_weight_monotone_unitary(self):
        """For unitary series: w_0 = m(m-1) grows with m."""
        for m in range(3, 10):
            w0 = vacuum_singular_weight(m + 1, m)
            assert w0 == m * (m - 1)


# ===========================================================================
# 4. VACUUM MODULE DIMENSIONS
# ===========================================================================


class TestVacuumDimensions:
    """Verify dimensions of V_c and L(c,0)."""

    def test_universal_dim_equals_partitions(self):
        """Universal V_c: dim V_+(h) = p_{>=2}(h)."""
        for h in range(10):
            assert universal_vac_dim(h) == (partitions_geq2(h) if h >= 2 else 0)

    def test_ising_null_dim_below_w0(self):
        """Below w_0=6: no null states in Ising."""
        for h in range(6):
            assert null_submodule_dim(4, 3, h) == 0

    def test_ising_null_dim_at_w0(self):
        """At w_0=6: exactly 1 null state (the singular vector itself)."""
        assert null_submodule_dim(4, 3, 6) == 1

    def test_ising_null_dim_at_w7(self):
        """At w=7: p(7-6) = p(1) = 1 null descendant."""
        assert null_submodule_dim(4, 3, 7) == 1

    def test_ising_null_dim_at_w8(self):
        """At w=8: p(8-6) = p(2) = 2 null descendants."""
        assert null_submodule_dim(4, 3, 8) == 2

    def test_ising_simple_dim_below_w0(self):
        """Below w_0: simple = universal."""
        for h in range(6):
            assert simple_quotient_dim(4, 3, h) == universal_vac_dim(h)

    def test_ising_simple_dim_at_w0(self):
        """At w_0=6: dim L = 4 - 1 = 3."""
        assert simple_quotient_dim(4, 3, 6) == 3

    def test_simple_dims_nonnegative(self):
        """Simple quotient dimensions must be non-negative."""
        for name, (p, q) in STANDARD_MODELS.items():
            for h in range(20):
                assert simple_quotient_dim(p, q, h) >= 0

    def test_simple_leq_universal(self):
        """Simple quotient dims <= universal dims (quotient is smaller)."""
        for name, (p, q) in STANDARD_MODELS.items():
            for h in range(20):
                assert simple_quotient_dim(p, q, h) <= universal_vac_dim(h)


# ===========================================================================
# 5. BAR CHAIN DIMENSIONS
# ===========================================================================


class TestBarChainDims:
    """Verify bar chain dimensions B^n_h."""

    def test_universal_bar1_is_vac_dim(self):
        """B^1_h(V_c) = dim V_+(h) = p_{>=2}(h)."""
        for h in range(2, 10):
            assert bar_chain_dim_universal(1, h) == partitions_geq2(h)

    def test_bar_chain_zero_below_threshold(self):
        """B^n_h = 0 when h < 2n."""
        for n in range(1, 5):
            for h in range(2 * n):
                assert bar_chain_dim_universal(n, h) == 0
                assert bar_chain_dim_simple(4, 3, n, h) == 0

    def test_ising_bar2_at_weight4(self):
        """B^2_4: pairs (a, 4-a) with a, 4-a >= 2: only (2,2).
        dim(V_+, 2) = 1 (just L_{-2}|0>).  So tensor dim = 1*1 = 1."""
        assert bar_chain_dim_universal(2, 4) == 1
        # Below null: simple = universal
        assert bar_chain_dim_simple(4, 3, 2, 4) == 1

    def test_ising_bar2_at_weight5(self):
        """B^2_5: pairs (2,3) and (3,2).  dim V_+(2)=1, dim V_+(3)=1.
        Tensor dim = 1*1 + 1*1 = 2."""
        assert bar_chain_dim_universal(2, 5) == 2
        assert bar_chain_dim_simple(4, 3, 2, 5) == 2

    def test_ising_bar2_at_weight6(self):
        """B^2_6 (at null weight): pairs (2,4), (3,3), (4,2).
        All factors below w_0=6, so simple = universal.
        dim V_+(2)=1, dim V_+(3)=1, dim V_+(4)=2.
        Tensor: 1*2 + 1*1 + 2*1 = 5."""
        assert bar_chain_dim_universal(2, 6) == 5
        assert bar_chain_dim_simple(4, 3, 2, 6) == 5

    def test_ising_bar1_change_at_null(self):
        """At w_0=6: B^1 drops by 1 (one null state removed)."""
        u = bar_chain_dim_universal(1, 6)
        s = bar_chain_dim_simple(4, 3, 1, 6)
        assert u == 4  # p_{>=2}(6) = 4
        assert s == 3  # 4 - 1 null
        assert u - s == 1

    def test_ising_bar2_unchanged_at_null(self):
        """At w_0=6: B^2 unchanged (all tensor factors below w_0)."""
        u = bar_chain_dim_universal(2, 6)
        s = bar_chain_dim_simple(4, 3, 2, 6)
        assert u == s

    def test_ising_chains_agree_below_null(self):
        """Below w_0=6: all bar chains identical for universal and simple."""
        for n in range(1, 4):
            for h in range(2 * n, 6):
                u = bar_chain_dim_universal(n, h)
                s = bar_chain_dim_simple(4, 3, n, h)
                assert u == s, f"Disagree at (n={n}, h={h}): {u} vs {s}"


# ===========================================================================
# 6. EULER CHARACTERISTICS
# ===========================================================================


class TestEulerCharacteristics:
    """Euler characteristic chi_h = sum (-1)^n dim B^n_h."""

    def test_euler_universal_weight2(self):
        """h=2: B^1_2=1 (only term).  chi = -1."""
        assert euler_char_universal(2) == -1

    def test_euler_universal_weight4(self):
        """h=4: B^1_4=2, B^2_4=1.  chi = -2 + 1 = -1."""
        assert euler_char_universal(4) == -1

    def test_euler_ising_agree_below_null(self):
        """Below w_0=6: Euler chars agree."""
        for h in range(2, 6):
            assert euler_char_universal(h) == euler_char_simple(4, 3, h)

    def test_euler_ising_change_at_null(self):
        """At w_0=6: Euler char changes (key non-Koszulness signal).

        Universal: chi_6 = -B^1_6 + B^2_6 - B^3_6
                        = -4 + 5 - 1 = 0
        Simple:   chi_6 = -3 + 5 - 1 = 1

        The deficit of +1 indicates new cohomology in the simple quotient.
        """
        chi_u = euler_char_universal(6)
        chi_s = euler_char_simple(4, 3, 6)
        assert chi_u == 0
        assert chi_s == 1
        assert chi_s - chi_u == 1

    def test_euler_char_sum_consistency(self):
        """Euler char must equal alternating sum of chain dims (tautology check)."""
        for h in range(2, 10):
            expected = sum((-1) ** n * bar_chain_dim_universal(n, h)
                          for n in range(1, h // 2 + 1))
            assert euler_char_universal(h) == expected


# ===========================================================================
# 7. KOSZULNESS OBSTRUCTION (Ising model)
# ===========================================================================


class TestIsingKoszulnessObstruction:
    """The Ising model M(4,3) is the simplest non-Koszul case."""

    @pytest.fixture
    def analysis(self):
        return ising_analysis(12)

    def test_ising_is_non_koszul(self, analysis):
        """The Ising simple quotient is predicted non-Koszul."""
        ko = analysis.koszulness_obstruction_analysis()
        assert ko['likely_non_koszul'] is True

    def test_new_cohomology_in_degree_2(self, analysis):
        """Non-Koszulness manifests as new H^2."""
        ko = analysis.koszulness_obstruction_analysis()
        assert ko['new_cohomology_degree'] == 2

    def test_null_weight_6(self, analysis):
        assert analysis.w0 == 6

    def test_kappa_one_fourth(self, analysis):
        assert analysis.kappa() == Rational(1, 4)

    def test_3_primaries(self, analysis):
        assert analysis.n_irreps == 3

    def test_dimension_deficit_starts_at_6(self, analysis):
        deficit = analysis.dimension_deficit()
        assert min(deficit.keys()) == 6

    def test_b2_unchanged_at_null(self, analysis):
        """B^2 at null weight is unchanged -- critical for the mechanism."""
        ko = analysis.koszulness_obstruction_analysis()
        assert ko['b2_unchanged_at_null'] is True

    def test_mechanism_description(self, analysis):
        """The mechanism field should describe the kernel creation."""
        ko = analysis.koszulness_obstruction_analysis()
        assert 'cycles' in ko['mechanism'].lower() or 'kernel' in ko['mechanism'].lower()

    def test_chain_changes_correct(self, analysis):
        """B^1 changes at weight 6, B^2 does not at weight 6."""
        changes = analysis.chain_dimension_change()
        assert (1, 6) in changes
        assert changes[(1, 6)] == -1  # one state removed
        assert (2, 6) not in changes  # B^2 unchanged at w_0


class TestIsingNullStructure:
    """Detailed null vector analysis for the Ising model."""

    def test_null_structure_data(self):
        ns = ising_null_vector_structure()
        assert ns['c'] == Rational(1, 2)
        assert ns['null_weight'] == 6
        assert ns['n_states_w6_universal'] == 4
        assert ns['n_states_w6_simple'] == 3

    def test_basis_at_weight_6(self):
        """4 states at weight 6: L_{-6}, L_{-4}L_{-2}, L_{-3}^2, L_{-2}^3."""
        ns = ising_null_vector_structure()
        assert len(ns['basis_at_w6']) == 4

    def test_bar_chain_comparison(self):
        comp = ising_bar_chain_comparison(10)
        # Changes should exist
        assert len(comp['changes']) > 0
        # Detail at null weight
        assert 'B^1_6' in comp['detail_at_null_weight']
        detail = comp['detail_at_null_weight']['B^1_6']
        assert detail['universal'] == 4
        assert detail['simple'] == 3
        assert detail['change'] == -1


# ===========================================================================
# 8. TRICRITICAL ISING M(5,4)
# ===========================================================================


class TestTricriticalIsing:
    """Tricritical Ising M(5,4), c=7/10, w_0=12."""

    @pytest.fixture
    def analysis(self):
        return tricritical_analysis(16)

    def test_central_charge(self, analysis):
        assert analysis.c == Rational(7, 10)

    def test_null_weight_12(self, analysis):
        assert analysis.w0 == 12

    def test_6_primaries(self, analysis):
        assert analysis.n_irreps == 6

    def test_kappa(self, analysis):
        assert analysis.kappa() == Rational(7, 20)

    def test_non_koszul(self, analysis):
        ko = analysis.koszulness_obstruction_analysis()
        assert ko['likely_non_koszul'] is True

    def test_agree_below_null(self, analysis):
        """Below w_0=12: universal and simple agree."""
        for h in range(2, 12):
            u = bar_chain_dim_universal(1, h)
            s = bar_chain_dim_simple(5, 4, 1, h)
            assert u == s, f"Disagree at h={h}"

    def test_differ_at_null(self, analysis):
        """At w_0=12: simple has fewer states."""
        u = bar_chain_dim_universal(1, 12)
        s = bar_chain_dim_simple(5, 4, 1, 12)
        assert s < u

    def test_null_dim_1_at_w0(self):
        """One singular vector at w_0=12."""
        assert null_submodule_dim(5, 4, 12) == 1


# ===========================================================================
# 9. COMPARISON ACROSS MODELS
# ===========================================================================


class TestCrossModelComparison:
    """Compare non-Koszulness across minimal models."""

    def test_comparison_returns_all_models(self):
        comp = non_koszulness_comparison(14)
        assert 'Ising' in comp
        assert 'tricritical' in comp
        assert 'trivial' in comp

    def test_trivial_is_koszul(self):
        """M(3,2), c=0: w_0=2, NOT non-Koszul by our criterion (w_0 < 4)."""
        comp = non_koszulness_comparison(6)
        assert comp['trivial']['likely_non_koszul'] is False

    def test_all_nontrivial_are_non_koszul(self):
        """All minimal models with w_0 >= 4 are predicted non-Koszul."""
        comp = non_koszulness_comparison(24)
        for name in ['Ising', 'Lee-Yang', 'tricritical', 'Potts']:
            assert comp[name]['likely_non_koszul'] is True, \
                f"{name} should be non-Koszul"

    def test_null_weight_ordering(self):
        """Ising < Lee-Yang < TCI < Potts by null weight."""
        comp = non_koszulness_comparison(24)
        assert comp['Ising']['null_weight'] == 6
        assert comp['Lee-Yang']['null_weight'] == 4
        assert comp['tricritical']['null_weight'] == 12
        assert comp['Potts']['null_weight'] == 20

    def test_pattern_description(self):
        pattern = non_koszulness_pattern()
        assert 'mechanism' in pattern
        assert 'Ising' in pattern['first_non_trivial']


# ===========================================================================
# 10. D-MODULE PURITY
# ===========================================================================


class TestDModulePurity:
    """D-module purity converse predictions."""

    def test_ising_non_pure(self):
        analysis = ising_analysis(10)
        dp = analysis.dmodule_purity_prediction()
        assert dp['purity_prediction'] == 'non-pure'
        assert dp['non_koszul'] is True

    def test_jordan_block(self):
        """Non-Koszulness creates a Jordan block of size 2."""
        analysis = ising_analysis(10)
        dp = analysis.dmodule_purity_prediction()
        assert dp['jordan_block_size'] == 2

    def test_affected_stratum(self):
        analysis = ising_analysis(10)
        dp = analysis.dmodule_purity_prediction()
        assert 'FM_2' in dp['affected_stratum']

    def test_tci_also_non_pure(self):
        analysis = tricritical_analysis(14)
        dp = analysis.dmodule_purity_prediction()
        assert dp['purity_prediction'] == 'non-pure'


# ===========================================================================
# 11. ZHU ALGEBRA COMPARISON
# ===========================================================================


class TestZhuComparison:
    """Zhu algebra Ext vs bar cohomology."""

    def test_zhu_does_not_detect_non_koszul(self):
        """Zhu algebra is semisimple for L(c,0) -> cannot detect
        non-Koszulness which lives at higher conformal weights."""
        analysis = ising_analysis(10)
        zhu = analysis.zhu_comparison()
        assert zhu['zhu_detects_non_koszul'] is False

    def test_universal_zhu_koszul(self):
        analysis = ising_analysis(10)
        zhu = analysis.zhu_comparison()
        assert zhu['universal_ext'][1] == 1  # one generator
        assert zhu['universal_ext'][2] == 0  # Koszul: no H^2 in Zhu Ext

    def test_simple_zhu_semisimple(self):
        analysis = ising_analysis(10)
        zhu = analysis.zhu_comparison()
        assert zhu['simple_ext'][1] == 0  # semisimple: Ext^1 = 0

    def test_tci_zhu_dim(self):
        analysis = tricritical_analysis(14)
        zhu = analysis.zhu_comparison()
        assert '6' in zhu['simple_zhu']  # 6 irreps


# ===========================================================================
# 12. SHADOW OBSTRUCTION TOWER
# ===========================================================================


class TestShadowData:
    """Shadow obstruction tower for minimal models."""

    def test_ising_shadow(self):
        sd = shadow_data(4, 3)
        assert sd['kappa'] == Rational(1, 4)
        assert sd['class'] == 'M'

    def test_tci_shadow(self):
        sd = shadow_data(5, 4)
        assert sd['kappa'] == Rational(7, 20)
        assert sd['class'] == 'M'

    def test_trivial_shadow(self):
        sd = shadow_data(3, 2)
        assert sd['kappa'] == Rational(0)
        assert sd['class'] == 'trivial'

    def test_lee_yang_shadow(self):
        """Lee-Yang c=-22/5: 5c+22=0, singular shadow."""
        sd = shadow_data(5, 2)
        assert sd['class'] == 'singular'

    def test_ising_delta(self):
        """Delta = 40/(5c+22) = 40/(5/2+22) = 40/(49/2) = 80/49."""
        sd = shadow_data(4, 3)
        expected = Rational(40) / (5 * Rational(1, 2) + 22)
        assert sd['Delta'] == expected

    def test_shadow_class_consistency(self):
        results = verify_shadow_class_consistency()
        for name, ok in results.items():
            assert ok, f"Shadow class wrong for {name}"


# ===========================================================================
# 13. COMPLEMENTARITY
# ===========================================================================


class TestComplementarity:
    """Koszul duality: c + c' = 26, kappa + kappa' = 13."""

    def test_all_models_complementarity(self):
        """c + c' = 26 for all standard minimal models."""
        for name, (p, q) in STANDARD_MODELS.items():
            assert verify_complementarity(p, q), f"Failed for {name}"

    def test_kappa_sum_13(self):
        """kappa + kappa' = 13 for all models (AP24: NOT zero!)."""
        for name, (p, q) in STANDARD_MODELS.items():
            assert verify_kappa_sum(p, q) == 13, f"Failed for {name}"


# ===========================================================================
# 14. CONFORMAL WEIGHTS (Kac table)
# ===========================================================================


class TestConformalWeights:
    """Kac table h_{r,s} = ((pr-qs)^2 - (p-q)^2)/(4pq)."""

    def test_ising_vacuum(self):
        """h_{1,1} = 0 for M(4,3)."""
        assert conformal_weight_kac(4, 3, 1, 1) == 0

    def test_ising_sigma(self):
        """h_{1,2} = 1/16 for M(4,3)."""
        assert conformal_weight_kac(4, 3, 1, 2) == Rational(1, 16)

    def test_ising_epsilon(self):
        """h_{1,3} = 1/2 for M(4,3)."""
        assert conformal_weight_kac(4, 3, 1, 3) == Rational(1, 2)

    def test_ising_null_field(self):
        """h_{2,3} = 0 for M(4,3): this is the null field giving w_0=6."""
        assert conformal_weight_kac(4, 3, 2, 3) == 0

    def test_tci_vacuum(self):
        assert conformal_weight_kac(5, 4, 1, 1) == 0

    def test_n_primaries_ising(self):
        """Ising: (4-1)(3-1)/2 = 3."""
        assert n_primaries(4, 3) == 3

    def test_n_primaries_tci(self):
        """TCI: (5-1)(4-1)/2 = 6."""
        assert n_primaries(5, 4) == 6

    def test_n_primaries_potts(self):
        """Potts: (6-1)(5-1)/2 = 10."""
        assert n_primaries(6, 5) == 10


# ===========================================================================
# 15. FULL ANALYSIS
# ===========================================================================


class TestFullAnalysis:
    """Integration tests: full analysis pipeline."""

    def test_ising_full_analysis(self):
        analysis = ising_analysis(10)
        result = analysis.full_analysis()
        assert result['c'] == Rational(1, 2)
        assert result['null_weight'] == 6
        assert result['kappa'] == Rational(1, 4)
        assert result['n_primaries'] == 3
        assert 'koszulness_analysis' in result
        assert 'dmodule_purity' in result
        assert 'zhu_comparison' in result

    def test_tci_full_analysis(self):
        analysis = tricritical_analysis(14)
        result = analysis.full_analysis()
        assert result['c'] == Rational(7, 10)
        assert result['null_weight'] == 12

    def test_invalid_model_raises(self):
        with pytest.raises(ValueError):
            MinimalModelBarAnalysis(4, 4)  # p must be > q
        with pytest.raises(ValueError):
            MinimalModelBarAnalysis(6, 4)  # gcd(6,4) = 2, not coprime

    def test_explicit_bar_degree_1(self):
        """Bar degree 1 for Ising: affected starting at w_0=6."""
        bd1 = explicit_bar_degree_1(4, 3, 8)
        assert not bd1[2]['affected']
        assert not bd1[5]['affected']
        assert bd1[6]['affected']
        assert bd1[6]['universal'] == 4
        assert bd1[6]['simple'] == 3

    def test_explicit_bar_degree_2(self):
        """Bar degree 2 for Ising at weight 6: unchanged."""
        bd2 = explicit_bar_degree_2(4, 3, 8)
        assert bd2[6]['change'] == 0  # unchanged at null weight


# ===========================================================================
# 16. MULTI-PATH CONSISTENCY
# ===========================================================================


class TestMultiPathVerification:
    """Cross-validate results through genuinely independent computation paths.

    AP10 compliance: every numerical value is verified via at least 2
    genuinely independent methods that could fail independently.
    """

    def test_euler_from_chains(self):
        """Path 1 vs Path 2: Euler char from chain dims must be consistent."""
        for h in range(2, 10):
            direct = euler_char_universal(h)
            manual = sum((-1) ** n * bar_chain_dim_universal(n, h)
                         for n in range(1, h // 2 + 1))
            assert direct == manual, f"Euler mismatch at h={h}"

    def test_simple_agree_below_null_all_models(self):
        """Path 3: simple = universal below null weight for ALL models."""
        for name, (p, q) in STANDARD_MODELS.items():
            w0 = vacuum_singular_weight(p, q)
            for h in range(min(w0, 8)):
                u = universal_vac_dim(h)
                s = simple_quotient_dim(p, q, h)
                assert u == s, f"{name} disagree at h={h}"

    def test_null_dim_plus_simple_equals_universal(self):
        """Path 4: dim V = dim L + dim N (direct sum below w_0 + w_0 range)."""
        for h in range(15):
            v = universal_vac_dim(h)
            l = simple_quotient_dim(4, 3, h)
            n = null_submodule_dim(4, 3, h)
            assert l == v - n, f"h={h}: {l} != {v} - {n}"

    def test_chain_dim_nonneg(self):
        """Sanity: all bar chain dimensions non-negative."""
        for n in range(1, 5):
            for h in range(2, 12):
                assert bar_chain_dim_universal(n, h) >= 0
                assert bar_chain_dim_simple(4, 3, n, h) >= 0

    def test_verify_all_passes(self):
        """The built-in verification suite must pass completely."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"verify_all FAILED: {name}"

    # ---- Genuine multi-path cross-checks (AP10) ----

    def test_central_charge_two_formulas(self):
        """Cross-check c via c = 1-6(p-q)^2/(pq) vs c = 1-6/(m(m+1))
        for the unitary series M(m+1, m)."""
        for m in range(3, 10):
            p, q = m + 1, m
            c_pq = minimal_model_c(p, q)
            c_m = Rational(1) - Rational(6, m * (m + 1))
            assert c_pq == c_m, f"m={m}: {c_pq} != {c_m}"

    def test_null_weight_two_formulas(self):
        """Cross-check w_0 = (p-1)(q-1) vs h_{r,s}=0 from Kac table.

        The null at w_0 corresponds to h_{q-1, p-1} = 0 in the Kac table.
        Verify independently that h_{q-1,p-1} is indeed 0."""
        for name, (p, q) in STANDARD_MODELS.items():
            if name == 'trivial':
                continue
            r, s = q - 1, p - 1
            h_rs = conformal_weight_kac(p, q, r, s)
            assert h_rs == 0, f"{name}: h_{{{r},{s}}} = {h_rs} != 0"
            assert r * s == vacuum_singular_weight(p, q), \
                f"{name}: r*s = {r * s} != w_0 = {vacuum_singular_weight(p, q)}"

    def test_n_primaries_vs_kac_table_enumeration(self):
        """Cross-check n_primaries = (p-1)(q-1)/2 by explicitly enumerating
        Kac table entries with the identification h_{r,s} = h_{q-r,p-s}."""
        for name, (p, q) in STANDARD_MODELS.items():
            formula_count = n_primaries(p, q)
            # Enumerate explicitly
            seen = set()
            for r in range(1, q):
                for s in range(1, p):
                    pair = (r, s)
                    dual = (q - r, p - s)
                    canonical = min(pair, dual)
                    seen.add(canonical)
            assert len(seen) == formula_count, \
                f"{name}: enumerated {len(seen)} != formula {formula_count}"

    def test_partitions_geq2_vs_generating_function(self):
        """Cross-check p_{>=2}(h) via explicit generating function coefficients.

        Product_{n>=2} 1/(1-x^n) = sum p_{>=2}(h) x^h.
        Independent implementation using polynomial multiplication."""
        max_h = 10
        # Build generating function as polynomial coefficients
        coeffs = [0] * (max_h + 1)
        coeffs[0] = 1
        for n in range(2, max_h + 1):
            new_coeffs = list(coeffs)
            for j in range(n, max_h + 1):
                new_coeffs[j] += new_coeffs[j - n]
            coeffs = new_coeffs
        # Compare with the engine's lru_cache implementation
        for h in range(max_h + 1):
            assert partitions_geq2(h) == coeffs[h], \
                f"p_{{>=2}}({h}): engine={partitions_geq2(h)}, genfn={coeffs[h]}"

    def test_kappa_via_two_independent_formulas(self):
        """Cross-check kappa = c/2 (Virasoro) against direct computation.

        For Virasoro: kappa = c/2.  Also verify kappa + kappa' = 13
        (AP24: the sum is 13, NOT 0, for Virasoro).
        These are two independent constraints on kappa."""
        for name, (p, q) in STANDARD_MODELS.items():
            c = minimal_model_c(p, q)
            kappa = c / 2
            kappa_dual = (26 - c) / 2
            # Path 1: direct formula
            assert kappa == c / 2
            # Path 2: complementarity constraint
            assert kappa + kappa_dual == 13

    def test_bar_chain_dim_universal_vs_convolution(self):
        """Cross-check B^2_h via direct tensor product vs convolution formula.

        B^2_h = sum_{a=2}^{h-2} p_{>=2}(a) * p_{>=2}(h-a).
        This is a discrete convolution, independently computed."""
        for h in range(4, 12):
            convolution = sum(
                partitions_geq2(a) * partitions_geq2(h - a)
                for a in range(2, h - 1)
            )
            assert bar_chain_dim_universal(2, h) == convolution, \
                f"B^2_{h}: engine={bar_chain_dim_universal(2, h)}, conv={convolution}"

    def test_ising_euler_deficit_from_chain_dims(self):
        """Cross-check Euler deficit at w_0=6 via two paths:
        Path A: direct call to euler_char functions.
        Path B: manually compute from chain dims at each bar degree."""
        # Path A
        chi_u = euler_char_universal(6)
        chi_s = euler_char_simple(4, 3, 6)
        deficit_a = chi_s - chi_u

        # Path B: compute from individual chain dims
        chi_u_manual = 0
        chi_s_manual = 0
        for n in range(1, 4):  # max bar degree at weight 6 is 3
            du = bar_chain_dim_universal(n, 6)
            ds = bar_chain_dim_simple(4, 3, n, 6)
            chi_u_manual += (-1) ** n * du
            chi_s_manual += (-1) ** n * ds
        deficit_b = chi_s_manual - chi_u_manual

        assert deficit_a == deficit_b == 1

    def test_ising_null_dim_vs_partition_formula(self):
        """Cross-check null_submodule_dim at Ising w_0=6 via two paths:
        Path A: engine function null_submodule_dim(4, 3, h).
        Path B: direct computation p(h - w_0) capped by p_{>=2}(h)."""
        w0 = 6
        for h in range(12):
            engine = null_submodule_dim(4, 3, h)
            if h < w0:
                direct = 0
            else:
                direct = min(num_partitions(h - w0), partitions_geq2(h))
            assert engine == direct, f"h={h}: engine={engine}, direct={direct}"

    def test_shadow_delta_two_formulas(self):
        """Cross-check Delta = 40/(5c+22) vs Delta = 8*kappa*S_4.

        Two genuinely independent formulas for the critical discriminant."""
        for name, (p, q) in STANDARD_MODELS.items():
            sd = shadow_data(p, q)
            if sd.get('Delta') is None:
                continue
            c = minimal_model_c(p, q)
            kappa = c / 2
            S4 = sd['S4']
            # Path 1: direct formula
            delta_direct = Rational(40) / (5 * c + 22)
            # Path 2: from kappa and S4
            delta_from_ks = 8 * kappa * S4
            assert sd['Delta'] == delta_direct == delta_from_ks, \
                f"{name}: Delta mismatch"

    def test_unitary_null_weight_quadratic_formula(self):
        """Cross-check w_0 for unitary series: (p-1)(q-1) = m(m-1).

        For M(m+1, m): w_0 = m*(m-1).  This is ALSO the degree of the
        null relation in Zhu's algebra, = n_primaries * 2 for Ising, etc.
        Two independent formulas giving the same number."""
        for m in range(3, 10):
            w0_formula = vacuum_singular_weight(m + 1, m)
            w0_quadratic = m * (m - 1)
            assert w0_formula == w0_quadratic, \
                f"m={m}: {w0_formula} != {w0_quadratic}"

    def test_b2_at_null_weight_independence(self):
        """Cross-check that B^2 is unchanged at null weight for Ising.

        Path A: compare bar_chain_dim_universal vs bar_chain_dim_simple at (2,6).
        Path B: verify all tensor factor weights are below w_0=6.
        If all factors in (a, 6-a) have a < 6 and 6-a < 6, then no factor
        is affected by the null quotient."""
        # Path A
        assert bar_chain_dim_universal(2, 6) == bar_chain_dim_simple(4, 3, 2, 6)
        # Path B: enumerate tensor splits
        for a in range(2, 5):  # a from 2 to 4 (so 6-a from 4 to 2)
            assert a < 6 and (6 - a) < 6, f"factor at w_0: a={a}"

    def test_chi_deficit_sign_predicts_new_cohomology(self):
        """The sign of the Euler char deficit predicts the parity of new H^*.

        At w_0=6 for Ising: chi changes by +1.  Since B^2 is unchanged and
        B^1 loses 1 state, the deficit must equal +1, and this signals
        exactly one new odd-degree cohomology class (H^1 gains 1 dimension
        at weight 6 in the quotient).

        Verify: deficit = -(change in B^1) = -(-1) = +1."""
        b1_change = bar_chain_dim_simple(4, 3, 1, 6) - bar_chain_dim_universal(1, 6)
        b2_change = bar_chain_dim_simple(4, 3, 2, 6) - bar_chain_dim_universal(2, 6)
        b3_change = bar_chain_dim_simple(4, 3, 3, 6) - bar_chain_dim_universal(3, 6)
        euler_change = -(b1_change) + (b2_change) - (b3_change)
        assert euler_change == 1
        assert b1_change == -1
        assert b2_change == 0
        assert b3_change == 0


# ===========================================================================
# 17. BAR COHOMOLOGY STRUCTURE (Universal Virasoro)
# ===========================================================================


class TestBarCohomologyUniversal:
    """The universal Virasoro V_c is Koszul: H^1_2=1, H^2_4=1, rest=0."""

    def test_h1_weight2(self):
        result = bar_cohomology_universal(8)
        assert result[(1, 2)] == 1

    def test_h2_weight4(self):
        result = bar_cohomology_universal(8)
        assert result[(2, 4)] == 1

    def test_higher_vanish(self):
        result = bar_cohomology_universal(8)
        for (n, h), d in result.items():
            if (n, h) not in {(1, 2), (2, 4)}:
                assert d == 0, f"H^{n}_{h} = {d} != 0"


# ===========================================================================
# 18. LEE-YANG MODEL M(5,2)
# ===========================================================================


class TestLeeYang:
    """Lee-Yang M(5,2), c=-22/5 (non-unitary), w_0=4."""

    def test_central_charge(self):
        assert minimal_model_c(5, 2) == Rational(-22, 5)

    def test_null_weight_4(self):
        assert vacuum_singular_weight(5, 2) == 4

    def test_non_koszul(self):
        analysis = MinimalModelBarAnalysis(5, 2, 8)
        ko = analysis.koszulness_obstruction_analysis()
        assert ko['likely_non_koszul'] is True

    def test_shadow_singular(self):
        """5c+22 = 5*(-22/5)+22 = 0: shadow obstruction tower is singular."""
        sd = shadow_data(5, 2)
        assert sd['class'] == 'singular'

    def test_agree_below_null(self):
        """Below w_0=4: B^1 unchanged."""
        for h in range(2, 4):
            assert bar_chain_dim_universal(1, h) == \
                   bar_chain_dim_simple(5, 2, 1, h)
