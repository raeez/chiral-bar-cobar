"""Tests for compute/lib/resonance_rank_classification.py.

Key results:
  - rho(H_k) = 0 (Heisenberg: positive tower)
  - rho(V_k(g)) = 0 (affine KM: positive tower)
  - rho(Vir_c) is structurally trivial (finite-type, MC4 not needed)
  - MC4+ / MC4^0 splitting for infinite-type algebras
  - Weight stabilization for positive towers
"""

import pytest
from fractions import Fraction

from compute.lib.resonance_rank_classification import (
    GeneratorData,
    ChiralAlgebraData,
    ResonanceRankEngine,
    heisenberg,
    affine_sl2,
    affine_slN,
    betagamma,
    virasoro,
    w_algebra,
    w_infinity,
    affine_yangian_sl2,
    rtt_algebra,
)


class TestStandardFamilyConstructors:
    """Verify constructor data for standard families."""

    def test_heisenberg_generators(self):
        H = heisenberg(1)
        assert H.n_generators == 1
        assert H.is_finite_type
        assert H.shadow_class == 'G'
        assert H.shadow_depth == 2

    def test_affine_sl2_generators(self):
        A = affine_sl2(Fraction(1))
        assert A.n_generators == 3
        assert A.is_finite_type
        assert A.shadow_class == 'L'

    def test_affine_sl3_dim(self):
        A = affine_slN(3, Fraction(1))
        assert A.n_generators == 8  # dim(sl_3) = 8

    def test_betagamma_data(self):
        bg = betagamma()
        assert bg.n_generators == 2
        assert bg.shadow_class == 'C'
        assert bg.shadow_depth == 4

    def test_virasoro_single_generator(self):
        V = virasoro(Fraction(26))
        assert V.n_generators == 1
        assert V.shadow_class == 'M'
        assert V.shadow_depth is None  # infinite

    def test_w_algebra_generators(self):
        W = w_algebra(3, Fraction(1))
        assert W.n_generators == 2  # W_2=T, W_3

    def test_w_infinity_infinite_type(self):
        W = w_infinity(Fraction(1))
        assert not W.is_finite_type

    def test_critical_level_raises(self):
        with pytest.raises(ValueError):
            affine_sl2(Fraction(-2))  # k = -h^vee


class TestResonanceRankPositiveTowers:
    """Positive towers: rho = 0, all generators at positive weight."""

    def test_heisenberg_rho_zero(self):
        """KEY RESULT: rho(Heisenberg) = 0."""
        engine = ResonanceRankEngine(heisenberg(1))
        assert engine.resonance_rank() == 0

    def test_affine_sl2_rho_zero(self):
        """KEY RESULT: rho(aff sl_2) = 0."""
        engine = ResonanceRankEngine(affine_sl2(Fraction(1)))
        assert engine.resonance_rank() == 0

    def test_affine_slN_rho_zero(self):
        for N in [2, 3, 4, 5]:
            engine = ResonanceRankEngine(affine_slN(N, Fraction(1)))
            assert engine.resonance_rank() == 0

    def test_positive_grading_implies_rho_zero(self):
        """Any algebra with all generators at positive weight has rho=0."""
        for fam in [heisenberg(1), affine_sl2(Fraction(1)),
                    virasoro(Fraction(26)), w_algebra(4, Fraction(1))]:
            engine = ResonanceRankEngine(fam)
            assert engine.has_positive_grading()
            assert engine.resonance_rank() == 0


class TestResonanceRankBetagamma:
    """Beta-gamma has a weight-0 generator but is finite-type."""

    def test_betagamma_has_weight_zero_generator(self):
        engine = ResonanceRankEngine(betagamma())
        assert engine.weight_zero_dim() == 1  # gamma at weight 0

    def test_betagamma_not_positive_grading(self):
        engine = ResonanceRankEngine(betagamma())
        assert not engine.has_positive_grading()

    def test_betagamma_finite_type_classification(self):
        """Finite-type algebras are classified as 'finite-type', not MC4+/MC4^0."""
        engine = ResonanceRankEngine(betagamma())
        assert engine.mc4_class() == 'finite-type'


class TestMC4Splitting:
    """MC4+ / MC4^0 splitting for infinite-type algebras."""

    def test_w_infinity_mc4_plus(self):
        """W_{1+infty} is MC4+ (positive tower, rho=0)."""
        engine = ResonanceRankEngine(w_infinity(Fraction(1)))
        assert engine.resonance_rank() == 0
        assert engine.mc4_class() == 'MC4+'

    def test_affine_yangian_mc4_plus(self):
        """Affine Yangian Y(sl_2) is MC4+ (positive tower)."""
        engine = ResonanceRankEngine(affine_yangian_sl2())
        assert engine.resonance_rank() == 0
        assert engine.mc4_class() == 'MC4+'

    def test_rtt_mc4_plus(self):
        """RTT algebra is MC4+ (positive tower)."""
        engine = ResonanceRankEngine(rtt_algebra())
        assert engine.resonance_rank() == 0
        assert engine.mc4_class() == 'MC4+'

    def test_finite_type_not_mc4(self):
        """Finite-type algebras don't need MC4."""
        for fam in [heisenberg(1), virasoro(Fraction(1)), w_algebra(3, Fraction(1))]:
            engine = ResonanceRankEngine(fam)
            assert engine.mc4_class() == 'finite-type'


class TestMC4Details:
    """Detailed MC4 classification reports."""

    def test_details_positive_tower(self):
        details = ResonanceRankEngine(w_infinity(Fraction(1))).mc4_details()
        assert details['mc4_class'] == 'MC4+'
        assert details['resonance_rank'] == 0
        assert details['is_finite_type'] is False

    def test_details_finite_type(self):
        details = ResonanceRankEngine(heisenberg(1)).mc4_details()
        assert details['mc4_class'] == 'finite-type'
        assert details['is_finite_type'] is True


class TestWeightStabilization:
    """Weight stabilization for positive towers (thm:stabilized-completion-positive)."""

    def test_heisenberg_stabilization(self):
        engine = ResonanceRankEngine(heisenberg(1))
        result = engine.verify_weight_stabilization(max_weight=5)
        assert result['applies']
        assert result['all_stabilized']

    def test_w_infinity_stabilization(self):
        engine = ResonanceRankEngine(w_infinity(Fraction(1)))
        result = engine.verify_weight_stabilization(max_weight=4)
        assert result['applies']
        assert result['all_stabilized']

    def test_stabilization_stage_equals_weight(self):
        engine = ResonanceRankEngine(w_infinity(Fraction(1)))
        for w in range(1, 5):
            assert engine.weight_stabilization_stage(w) == w


class TestShadowVsResonance:
    """Shadow depth and resonance rank are independent classifications."""

    def test_gaussian_positive(self):
        """Heisenberg: shadow G (depth 2), rho = 0."""
        engine = ResonanceRankEngine(heisenberg(1))
        info = engine.shadow_vs_resonance()
        assert info['shadow_class'] == 'G'
        assert info['resonance_rank'] == 0

    def test_mixed_positive(self):
        """W_{1+infty}: shadow M (depth inf), but rho = 0 (MC4+)."""
        engine = ResonanceRankEngine(w_infinity(Fraction(1)))
        info = engine.shadow_vs_resonance()
        assert info['shadow_class'] == 'M'
        assert info['resonance_rank'] == 0
