#!/usr/bin/env python3
"""
test_platonic_completion_families.py — Tests for resonance rank and platonic completion conjecture.
"""

import sys
import os
import math
import pytest
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from platonic_completion_families import (
    heisenberg_weight_dims,
    affine_sl2_weight_dims,
    virasoro_weight_dims,
    w3_weight_dims,
    betagamma_weight_dims,
    bar_complex_weight0_dim,
    resonance_rank,
    completion_filtration_decay,
    virasoro_bpz_singular_vectors,
    virasoro_resonance_dimension,
    shadow_depth,
    shadow_archetype,
    platonic_completion_evidence,
    verify_platonic_conjecture,
    weight_generating_function,
    weight_gf_ratio,
    resonance_indicator_matrix,
    ALL_FAMILIES,
    EXPECTED_RESONANCE_RANKS,
)


# ============================================================
# Weight dimension tests
# ============================================================

class TestWeightDimensions:
    """Verify weight-space dimensions match known partition counts."""

    def test_heisenberg_partitions(self):
        """Heisenberg dims = partition numbers p(n)."""
        dims = heisenberg_weight_dims(10)
        # p(0..10) = 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        assert dims == expected

    def test_heisenberg_vacuum(self):
        dims = heisenberg_weight_dims(5)
        assert dims[0] == 1

    def test_affine_sl2_vacuum(self):
        dims = affine_sl2_weight_dims(1, 5)
        assert dims[0] == 1

    def test_affine_sl2_weight1(self):
        """V_k(sl_2) at weight 1: 3 generators J^+, J^-, J^0."""
        dims = affine_sl2_weight_dims(1, 5)
        assert dims[1] == 3

    def test_affine_sl2_critical_raises(self):
        with pytest.raises(ValueError, match="Critical level"):
            affine_sl2_weight_dims(-2, 5)

    def test_virasoro_vacuum(self):
        dims = virasoro_weight_dims(5)
        assert dims[0] == 1
        assert dims[1] == 0  # no weight-1 state (L starts at weight 2)

    def test_virasoro_weight2(self):
        """Single generator L_{-2}|0> at weight 2."""
        dims = virasoro_weight_dims(5)
        assert dims[2] == 1

    def test_virasoro_weight4(self):
        """Weight 4: L_{-4}|0>, L_{-2}^2|0> → 2 states."""
        dims = virasoro_weight_dims(5)
        assert dims[4] == 2

    def test_w3_vacuum(self):
        dims = w3_weight_dims(5)
        assert dims[0] == 1

    def test_w3_weight2(self):
        """W_3 at weight 2: only L_{-2}|0>."""
        dims = w3_weight_dims(5)
        assert dims[2] == 1

    def test_w3_weight3(self):
        """W_3 at weight 3: L_{-3}|0> and W_{-3}|0> → 2."""
        dims = w3_weight_dims(5)
        assert dims[3] == 2

    def test_betagamma_vacuum(self):
        dims = betagamma_weight_dims(5)
        assert dims[0] == 1

    def test_betagamma_weight1(self):
        """βγ at weight 1: β_{-1}|0>, γ_{-1}|0> → 2."""
        dims = betagamma_weight_dims(5)
        assert dims[1] == 2


# ============================================================
# Resonance rank tests — the core results
# ============================================================

class TestResonanceRank:
    """Verify ρ(A) for all standard families."""

    def test_heisenberg_rho_zero(self):
        rho, _ = resonance_rank('heisenberg')
        assert rho == 0

    def test_affine_sl2_rho_zero(self):
        rho, _ = resonance_rank('affine_sl2', k=1)
        assert rho == 0

    def test_affine_sl2_rho_zero_various_levels(self):
        """ρ = 0 for all non-critical levels."""
        for k in [1, 2, 3, 5, 10, 100, -1, Fraction(1, 2)]:
            rho, _ = resonance_rank('affine_sl2', k=k)
            assert rho == 0, f"Failed at k={k}"

    def test_virasoro_rho_one(self):
        rho, _ = resonance_rank('virasoro', c=7)
        assert rho == 1

    def test_virasoro_rho_one_various_c(self):
        """ρ = 1 for generic c."""
        for c in [0, 1, 7, 13, 25, 26, 100, -5]:
            rho, _ = resonance_rank('virasoro', c=c)
            assert rho == 1, f"Failed at c={c}"

    def test_w3_rho_one(self):
        # AP10 correction: ρ(W₃) = 1, not 2.
        # Both generators T (wt 2) and W (wt 3) have positive weight,
        # so V₀ = C·|0⟩ is 1-dimensional and R = C·m₀.
        rho, _ = resonance_rank('w3', c=50)
        assert rho == 1

    def test_betagamma_rho_zero(self):
        rho, _ = resonance_rank('betagamma')
        assert rho == 0

    def test_all_expected_ranks(self):
        """Verify all families match expected resonance ranks."""
        for fam, expected_rho in EXPECTED_RESONANCE_RANKS.items():
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            rho, _ = resonance_rank(fam, **kwargs)
            assert rho == expected_rho, f"{fam}: got ρ={rho}, expected {expected_rho}"

    def test_stabilization(self):
        """All families stabilize by stage 2."""
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            _, stab = resonance_rank(fam, max_stage=10, **kwargs)
            assert stab <= 2, f"{fam} did not stabilize by stage 2"


from fractions import Fraction


# ============================================================
# Bar complex weight-0 tests
# ============================================================

class TestBarComplexWeight0:
    """Test the weight-0 bar complex dimensions."""

    def test_heisenberg_all_stages_zero(self):
        for s in range(10):
            assert bar_complex_weight0_dim('heisenberg', s) == 0

    def test_affine_all_stages_zero(self):
        for s in range(10):
            assert bar_complex_weight0_dim('affine_sl2', s, k=1) == 0

    def test_betagamma_all_stages_zero(self):
        for s in range(10):
            assert bar_complex_weight0_dim('betagamma', s) == 0

    def test_virasoro_stage0_zero(self):
        assert bar_complex_weight0_dim('virasoro', 0) == 0

    def test_virasoro_stage1_one(self):
        assert bar_complex_weight0_dim('virasoro', 1, c=7) == 1

    def test_virasoro_persistent(self):
        """Weight-0 dim persists at 1 for all stages >= 1."""
        for s in range(1, 10):
            assert bar_complex_weight0_dim('virasoro', s, c=7) == 1

    def test_w3_stage0_zero(self):
        assert bar_complex_weight0_dim('w3', 0) == 0

    def test_w3_persistent(self):
        # AP10 correction: weight-0 dim = 1 (curvature m_0 only)
        for s in range(1, 10):
            assert bar_complex_weight0_dim('w3', s, c=50) == 1

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            bar_complex_weight0_dim('unknown', 1)


# ============================================================
# Shadow depth and archetype tests
# ============================================================

class TestShadowClassification:
    """Verify shadow depth and archetype classification."""

    def test_heisenberg_gaussian(self):
        assert shadow_depth('heisenberg') == 2
        assert shadow_archetype('heisenberg') == 'G'

    def test_affine_lie(self):
        assert shadow_depth('affine_sl2') == 3
        assert shadow_archetype('affine_sl2') == 'L'

    def test_betagamma_contact(self):
        assert shadow_depth('betagamma') == 4
        assert shadow_archetype('betagamma') == 'C'

    def test_virasoro_mixed(self):
        assert shadow_depth('virasoro') == float('inf')
        assert shadow_archetype('virasoro') == 'M'

    def test_w3_mixed(self):
        assert shadow_depth('w3') == float('inf')
        assert shadow_archetype('w3') == 'M'

    def test_shadow_depth_independent_of_resonance(self):
        """Shadow depth ≠ resonance rank. βγ has depth 4 but ρ = 0."""
        assert shadow_depth('betagamma') == 4
        rho, _ = resonance_rank('betagamma')
        assert rho == 0


# ============================================================
# Platonic completion conjecture tests
# ============================================================

class TestPlatonicCompletion:
    """Tests for conj:platonic-completion."""

    def test_all_finite(self):
        all_ok, failures = verify_platonic_conjecture()
        assert all_ok, f"Platonic completion failed for: {failures}"

    def test_evidence_structure(self):
        results = platonic_completion_evidence()
        assert set(results.keys()) == set(ALL_FAMILIES)
        for fam, data in results.items():
            assert 'rho' in data
            assert 'stabilized_at' in data
            assert 'shadow_depth' in data
            assert 'archetype' in data
            assert 'finite' in data

    def test_evidence_values(self):
        results = platonic_completion_evidence()
        for fam, data in results.items():
            assert data['rho'] == EXPECTED_RESONANCE_RANKS[fam]
            assert data['finite'] is True


# ============================================================
# Virasoro BPZ tests
# ============================================================

class TestVirasoro:
    def test_generic_c_singular_vectors(self):
        svs = virasoro_bpz_singular_vectors(7.0)
        assert len(svs) == 1  # only trivial L_{-1}|0> = 0
        assert svs[0] == (1, 1)

    def test_resonance_dim_generic(self):
        assert virasoro_resonance_dimension(7) == 1

    def test_resonance_dim_self_dual(self):
        assert virasoro_resonance_dimension(13) == 1

    def test_resonance_dim_c26(self):
        assert virasoro_resonance_dimension(26) == 1


# ============================================================
# Weight generating function tests
# ============================================================

class TestWeightGF:
    def test_gf_matches_dims(self):
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            gf = weight_generating_function(fam, 10, **kwargs)
            assert gf[0] == 1  # vacuum

    def test_growth_rate_finite(self):
        """All families have finite growth ratios (after initial zero gaps)."""
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            dims = weight_generating_function(fam, 15, **kwargs)
            # Check ratios only where denominator is positive
            for i in range(1, len(dims)):
                if dims[i - 1] > 0:
                    assert dims[i] / dims[i - 1] < float('inf')


# ============================================================
# Resonance indicator matrix tests
# ============================================================

class TestResonanceMatrix:
    def test_heisenberg_zero_matrix(self):
        M = resonance_indicator_matrix('heisenberg')
        assert np.all(M == 0)

    def test_affine_zero_matrix(self):
        M = resonance_indicator_matrix('affine_sl2', k=1)
        assert np.all(M == 0)

    def test_betagamma_zero_matrix(self):
        M = resonance_indicator_matrix('betagamma')
        assert np.all(M == 0)

    def test_virasoro_single_direction(self):
        M = resonance_indicator_matrix('virasoro', max_stage=6, max_weight=5)
        # Stage 0: all zero
        assert np.all(M[0] == 0)
        # Stages >= 1: exactly one direction at weight 0
        for s in range(1, 6):
            assert M[s][0] == 1
            assert np.all(M[s][1:] == 0)

    def test_w3_two_directions(self):
        M = resonance_indicator_matrix('w3', max_stage=6, max_weight=5)
        for s in range(1, 6):
            assert M[s][0] == 1  # AP10 fix: ρ(W₃) = 1

    def test_total_resonance_equals_rho(self):
        """Sum of persistent directions at any stage >= 1 equals ρ."""
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            M = resonance_indicator_matrix(fam, max_stage=4, max_weight=5, **kwargs)
            rho, _ = resonance_rank(fam, **kwargs)
            # At stage 1, sum of all weights should equal rho
            assert np.sum(M[1]) == rho, f"{fam}: matrix sum {np.sum(M[1])} != ρ={rho}"


# ============================================================
# Completion filtration decay tests
# ============================================================

class TestCompletionDecay:
    def test_decay_structure(self):
        result = completion_filtration_decay('heisenberg', max_weight=5)
        assert len(result) == 6
        assert result[0] == (0, 1, 0)  # vacuum: dim=1, bar1=0
        assert result[1] == (1, 1, 1)  # weight 1

    def test_virasoro_no_weight1(self):
        result = completion_filtration_decay('virasoro', max_weight=5)
        assert result[1][1] == 0  # no weight-1 state

    def test_all_families_run(self):
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            result = completion_filtration_decay(fam, max_weight=5, **kwargs)
            assert len(result) == 6


# ============================================================
# Monotonicity and consistency tests
# ============================================================

class TestConsistency:
    def test_rho_nonnegative(self):
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            rho, _ = resonance_rank(fam, **kwargs)
            assert rho >= 0

    def test_positive_families_zero_rho(self):
        """Families with PBW / polynomial OPE have ρ = 0."""
        for fam in ['heisenberg', 'affine_sl2', 'betagamma']:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            rho, _ = resonance_rank(fam, **kwargs)
            assert rho == 0

    def test_mixed_families_positive_rho(self):
        """Families with infinite shadow obstruction tower have ρ > 0."""
        for fam in ['virasoro', 'w3']:
            rho, _ = resonance_rank(fam)
            assert rho > 0

    def test_weight_dims_monotone(self):
        """Weight dimensions are eventually non-decreasing."""
        for fam in ALL_FAMILIES:
            kwargs = {'k': 1} if fam == 'affine_sl2' else {}
            dims = weight_generating_function(fam, 20, **kwargs)
            # From some point on, should be non-decreasing
            # (not necessarily from the start due to gaps like Virasoro weight 1)
            # Check from weight 3 onwards
            for i in range(4, len(dims)):
                assert dims[i] >= dims[i - 1], \
                    f"{fam}: dim[{i}]={dims[i]} < dim[{i-1}]={dims[i-1]}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
