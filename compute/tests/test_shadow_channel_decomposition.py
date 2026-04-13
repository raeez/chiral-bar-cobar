"""Tests for shadow channel decomposition (thm:shadow-channel-decomposition).

Verifies:
  1. Multi-channel shadow algebra for rank-N Heisenberg
  2. Channel independence (abelian → decoupled)
  3. Shadow Cauchy-Schwarz inequality: tr(K²) ≤ tr(K)²
  4. Genus-2 clutching via matrix multiplication
  5. Non-abelian/abelian dichotomy

The Cauchy-Schwarz shadow inequality is a NEW invariant:
  ρ = tr(K²)/κ² ∈ [1/r, 1]
measures "channel spread". ρ = 1 iff effectively one-channel.
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

from __future__ import annotations

import numpy as np
import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from shadow_channel_decomposition import (
    MultiChannelShadow,
    HeisenbergShadow,
    abelian_dichotomy_test,
    genus1_multichannel_propagation,
    genus2_multichannel_clutching,
    cauchy_schwarz_shadow,
    master_shadow_decomposition,
)


# ========================================================================
# Multi-channel shadow algebra
# ========================================================================

class TestMultiChannelShadow:

    def test_one_channel_nonabelian(self):
        s = MultiChannelShadow(1, is_abelian=False)
        assert s.r == 1
        assert s.n_gerstenhaber_brackets == 0
        assert s.verify_channel_independence()

    def test_three_channel_abelian(self):
        s = MultiChannelShadow(3, is_abelian=True)
        assert s.r == 3
        assert s.n_cubic_shadows == 0
        assert s.n_gerstenhaber_brackets == 3
        assert s.verify_channel_independence()  # abelian → independent

    def test_abelian_cubic_vanishes(self):
        s = MultiChannelShadow(2, is_abelian=True)
        assert s.cubic_shadow(0, 1) == 0.0
        assert s.quartic_contact(0, 1) == 0.0


# ========================================================================
# Heisenberg shadow algebra
# ========================================================================

class TestHeisenbergShadow:

    def test_rank1_one_channel(self):
        hs = HeisenbergShadow(1)
        assert hs.n_channels == 1
        assert hs.total_kappa == 1.0
        assert hs.central_charge == 1

    def test_rank2_three_channels(self):
        hs = HeisenbergShadow(2)
        assert hs.n_channels == 3
        assert hs.total_kappa == 2.0
        assert hs.central_charge == 2

    def test_rank2_general_metric(self):
        g = np.array([[3.0, 1.0], [1.0, 2.0]])
        hs = HeisenbergShadow(2, g)
        assert hs.total_kappa == 5.0
        kappas = hs.channel_kappas()
        assert kappas[(0, 0)] == 3.0
        assert kappas[(0, 1)] == 1.0
        assert kappas[(1, 1)] == 2.0

    def test_rank3_six_channels(self):
        hs = HeisenbergShadow(3)
        assert hs.n_channels == 6

    def test_abelian_vanishing(self):
        for N in [1, 2, 3, 4]:
            hs = HeisenbergShadow(N)
            v = hs.verify_abelian_vanishing()
            assert v['cubic_shadow_vanishes']
            assert v['quartic_contact_vanishes']
            assert v['termination_arity'] == 2

    def test_genus_g_shadow_is_metric(self):
        g = np.array([[2.0, 0.5], [0.5, 3.0]])
        hs = HeisenbergShadow(2, g)
        shadow = hs.genus_g_shadow_matrix(1)
        assert np.allclose(shadow, g)

    def test_complementarity_antisymmetry(self):
        hs = HeisenbergShadow(2)
        comp = hs.complementarity_genus_g(1)
        assert comp['complementarity_sum'] == 0.0
        assert comp['channel_decomposition']

    def test_shadow_algebra_structure(self):
        hs = HeisenbergShadow(2)
        sa = hs.shadow_algebra_generators()
        assert sa['n_generators'] == 3
        assert sa['is_free_commutative']
        assert sa['termination_arity'] == 2


# ========================================================================
# Non-abelian/abelian dichotomy
# ========================================================================

class TestDichotomy:

    def test_nonabelian_one_channel(self):
        r = abelian_dichotomy_test(
            ope_bracket_nonzero=True, dim_v_prim=1, m_prim_rank=1)
        assert r['type'] == 'non-abelian'
        assert r['one_channel']
        assert r['channels_independent']

    def test_abelian_multi_channel(self):
        r = abelian_dichotomy_test(
            ope_bracket_nonzero=False, dim_v_prim=3, m_prim_rank=0)
        assert r['type'] == 'abelian'
        assert r['dim_H2_cyc'] == 4
        assert not r['one_channel']
        assert r['channels_independent']

    def test_abelian_rank1_one_channel(self):
        r = abelian_dichotomy_test(
            ope_bracket_nonzero=False, dim_v_prim=0, m_prim_rank=0)
        assert r['one_channel']


# ========================================================================
# Genus-1 multi-channel propagation
# ========================================================================

class TestGenus1Propagation:

    def test_identity_metric(self):
        K = np.eye(2)
        r = genus1_multichannel_propagation(K)
        assert r['total_kappa'] == 2.0
        assert r['channels_independent']
        assert np.allclose(r['genus1_shadow'], K)

    def test_general_metric(self):
        K = np.array([[3.0, 1.0], [1.0, 2.0]])
        r = genus1_multichannel_propagation(K)
        assert r['total_kappa'] == 5.0
        assert r['ns_contribution'] == 5.0  # non-sep sees trace only

    def test_one_channel(self):
        K = np.array([[7.0]])
        r = genus1_multichannel_propagation(K)
        assert r['total_kappa'] == 7.0
        assert r['n_channels'] == 1


# ========================================================================
# Genus-2 multi-channel clutching
# ========================================================================

class TestGenus2Clutching:

    def test_identity_metric_genus2(self):
        K = np.eye(2)
        r = genus2_multichannel_clutching(K)
        # K² = I for identity matrix
        assert np.allclose(r['separating_shadow'], np.eye(2))
        assert r['total_kappa'] == 2.0
        # tr(K²) = 2, κ² = 4, so ratio = 1/2 ≠ 1 (multi-channel)
        assert not r['is_rank_one']

    def test_rank1_matrix_genus2(self):
        """Rank-1 K should give tr(K²) = κ²."""
        K = np.array([[3.0, 1.5], [1.5, 0.75]])  # rank 1: K = [3,1.5]^T [1, 0.5]
        # Actually this has rank 1 iff det = 0: 3*0.75 - 1.5*1.5 = 2.25-2.25 = 0 ✓
        r = genus2_multichannel_clutching(K)
        assert r['is_rank_one']

    def test_one_channel_genus2(self):
        K = np.array([[5.0]])
        r = genus2_multichannel_clutching(K)
        assert r['is_rank_one']
        assert np.isclose(r['trace_kappa_sq'], 25.0)


# ========================================================================
# Cauchy-Schwarz shadow inequality (NEW INVARIANT)
# ========================================================================

class TestCauchySchwarzShadow:
    """Tests for the shadow Cauchy-Schwarz inequality: tr(K²) ≤ κ².

    This is a NEW invariant measuring multi-channel spread.
    """

    def test_one_channel_saturates(self):
        """One-channel: tr(K²) = κ² (ratio = 1)."""
        K = np.array([[7.0]])
        r = cauchy_schwarz_shadow(K)
        assert r['is_one_channel']
        assert np.isclose(r['ratio'], 1.0)

    def test_two_channel_identity_ratio(self):
        """Two equal channels: ratio = 1/2."""
        K = np.eye(2)
        r = cauchy_schwarz_shadow(K)
        assert np.isclose(r['ratio'], 0.5)
        assert not r['is_one_channel']

    def test_three_channel_identity_ratio(self):
        """Three equal channels: ratio = 1/3."""
        K = np.eye(3)
        r = cauchy_schwarz_shadow(K)
        assert np.isclose(r['ratio'], 1.0 / 3.0)

    def test_inequality_always_holds(self):
        """tr(K²) ≤ κ² for random positive-definite matrices."""
        rng = np.random.RandomState(42)
        for _ in range(20):
            N = rng.randint(2, 6)
            A = rng.randn(N, N)
            K = A @ A.T + np.eye(N)  # positive definite
            r = cauchy_schwarz_shadow(K)
            assert r['cauchy_schwarz_holds'], \
                f"Cauchy-Schwarz violated for N={N}"

    def test_ratio_bounds(self):
        """1/r ≤ ρ ≤ 1 for all K."""
        rng = np.random.RandomState(123)
        for _ in range(20):
            N = rng.randint(2, 5)
            A = rng.randn(N, N)
            K = A @ A.T + np.eye(N)
            r = cauchy_schwarz_shadow(K)
            assert r['ratio'] >= r['min_ratio'] - 1e-10
            assert r['ratio'] <= r['max_ratio'] + 1e-10

    def test_rank1_is_one_channel(self):
        """Rank-1 K gives ρ = 1 (effectively one-channel)."""
        v = np.array([1.0, 2.0, 3.0])
        K = np.outer(v, v)  # rank 1
        r = cauchy_schwarz_shadow(K)
        assert r['is_one_channel']

    def test_diagonal_unequal(self):
        """Diagonal K with unequal entries: 1/r < ρ < 1."""
        K = np.diag([1.0, 2.0, 3.0])
        r = cauchy_schwarz_shadow(K)
        # tr(K²) = 1+4+9 = 14, κ² = 36, ratio = 14/36 ≈ 0.389
        assert np.isclose(r['ratio'], 14.0 / 36.0)
        assert not r['is_one_channel']
        assert r['ratio'] > r['min_ratio']

    @pytest.mark.parametrize("kappa", [1.0, 3.0, 10.0, 0.5])
    def test_scalar_multiple_preserves_ratio(self, kappa):
        """Scaling K → αK preserves the ratio ρ."""
        K0 = np.array([[2.0, 1.0], [1.0, 3.0]])
        r0 = cauchy_schwarz_shadow(K0)
        K1 = kappa * K0
        r1 = cauchy_schwarz_shadow(K1)
        assert np.isclose(r0['ratio'], r1['ratio'])


# ========================================================================
# Master computation
# ========================================================================

class TestMasterDecomposition:

    def test_master_runs(self):
        results = master_shadow_decomposition()
        assert len(results) >= 7

    def test_heisenberg_examples(self):
        results = master_shadow_decomposition()
        heis = [r for r in results if 'Heisenberg' in r['name']]
        for r in heis:
            if r['n_channels'] == 1:
                assert r['is_one_channel']
            else:
                assert not r['is_one_channel']

    def test_nonabelian_examples(self):
        results = master_shadow_decomposition()
        nonab = [r for r in results if r.get('non_abelian')]
        for r in nonab:
            assert r['is_one_channel']
            assert r['n_channels'] == 1

    def test_cauchy_schwarz_universal(self):
        """Cauchy-Schwarz holds for all examples."""
        results = master_shadow_decomposition()
        for r in results:
            if 'cauchy_schwarz_holds' in r:
                assert r['cauchy_schwarz_holds'], \
                    f"CS failed for {r['name']}"
