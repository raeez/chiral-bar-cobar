r"""Tests for GZ26 commuting Hamiltonians from the MC element.

Tests verify Theorem thm:gz26-commuting-differentials:
- Path 1: Shadow connection flatness -> [H_i, H_j] = 0
- Path 2: Collision-depth expansion matches family structure
- Path 3: Direct algebraic verification (IBR for KM, Ward for Virasoro)
- Cross-path consistency

Multi-path verification mandate: every claim verified by >= 3 independent paths.
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from theorem_gz26_commuting_hamiltonians_engine import (
    sl2_casimir,
    kz_hamiltonians,
    verify_kz_commutativity,
    verify_ibr,
    collision_depth_expansion,
    verify_shadow_connection_flatness_km,
    three_path_verification,
    koszulness_implies_one_loop_exactness,
    verify_bpz_commutativity_4pt,
    _embed_casimir_direct,
)


# ============================================================
# sl_2 Casimir basic tests
# ============================================================

class TestSl2Casimir:
    """Test the sl_2 Casimir operator construction."""

    def test_casimir_spin_half(self):
        """C_2 for spin-1/2 x spin-1/2: eigenvalues 3/4 (triplet), -1/4 (singlet)."""
        Omega = sl2_casimir(2)
        eigs = sorted(np.linalg.eigvalsh(Omega))
        # singlet eigenvalue: j(j+1)/2 for j=0: C_2 = -3/4 ... wait
        # Actually Omega = J_1 . J_2 = (J_total^2 - J_1^2 - J_2^2)/2
        # For singlet (j=0): (0 - 3/4 - 3/4)/2 = -3/4
        # For triplet (j=1): (2 - 3/4 - 3/4)/2 = 1/4
        expected = sorted([-3/4] + [1/4]*3)
        np.testing.assert_allclose(eigs, expected, atol=1e-12)

    def test_casimir_spin_1(self):
        """C_2 for spin-1 x spin-1: eigenvalues for j=0,1,2."""
        Omega = sl2_casimir(3)
        eigs = sorted(np.linalg.eigvalsh(Omega))
        # j=0: (0 - 2 - 2)/2 = -2 (multiplicity 1)
        # j=1: (2 - 2 - 2)/2 = -1 (multiplicity 3)
        # j=2: (6 - 2 - 2)/2 = 1  (multiplicity 5)
        expected = sorted([-2]*1 + [-1]*3 + [1]*5)
        np.testing.assert_allclose(eigs, expected, atol=1e-12)

    def test_casimir_symmetric(self):
        """Casimir should be symmetric (Hermitian)."""
        for d in [2, 3, 4]:
            Omega = sl2_casimir(d)
            np.testing.assert_allclose(Omega, Omega.T, atol=1e-14)


# ============================================================
# Path 1: KZ Hamiltonians and commutativity
# ============================================================

class TestKZHamiltonians:
    """Test KZ Hamiltonians [H_i, H_j] = 0 (Path 1: shadow connection flatness)."""

    def test_kz_3pt_spin_half_commute(self):
        """[H_i, H_j] = 0 for 3 spin-1/2 reps of sl_2 at level 1."""
        positions = [0.0 + 0j, 1.0 + 0j, 0.5 + 0.5j]
        result = verify_kz_commutativity(3, [2, 2, 2], positions, level=1)
        assert result['all_commute']

    def test_kz_4pt_spin_half_commute(self):
        """[H_i, H_j] = 0 for 4 spin-1/2 reps."""
        positions = [0.0, 1.0, 2.0 + 1j, -1.0 + 0.5j]
        result = verify_kz_commutativity(4, [2, 2, 2, 2], positions, level=1)
        assert result['all_commute']

    def test_kz_3pt_mixed_reps_commute(self):
        """[H_i, H_j] = 0 for mixed representations (spin-1/2, spin-1, spin-1/2)."""
        positions = [0.0, 1.0 + 0.3j, 2.0]
        result = verify_kz_commutativity(3, [2, 3, 2], positions, level=2)
        assert result['all_commute']

    def test_kz_4pt_spin_1_commute(self):
        """[H_i, H_j] = 0 for 4 spin-1 reps at level 2."""
        positions = [0.0, 1.0, 0.5 + 1j, -0.5 + 0.5j]
        result = verify_kz_commutativity(4, [3, 3, 3, 3], positions, level=2)
        assert result['all_commute']

    def test_kz_5pt_commute(self):
        """[H_i, H_j] = 0 for 5 points (2D moduli space, nontrivial check)."""
        np.random.seed(123)
        positions = np.random.randn(5) + 1j * np.random.randn(5)
        result = verify_kz_commutativity(5, [2, 2, 2, 2, 2], positions, level=1)
        assert result['all_commute']

    def test_kz_position_independence(self):
        """Commutativity holds for multiple random position configurations."""
        result = verify_shadow_connection_flatness_km(
            n_points=3, dims=[2, 2, 2], level=1, n_random_positions=10
        )
        assert result['all_pass']

    def test_kz_level_independence(self):
        """Commutativity holds at various levels."""
        positions = [0.0, 1.0, 0.5 + 0.7j]
        for k in [1, 2, 3, 5, 10]:
            result = verify_kz_commutativity(3, [2, 2, 2], positions, level=k)
            assert result['all_commute'], f"Failed at level {k}"


# ============================================================
# Path 3: Infinitesimal Braid Relation
# ============================================================

class TestIBR:
    """Test the infinitesimal braid relation (Path 3: algebraic verification)."""

    def test_ibr_spin_half(self):
        """IBR for three spin-1/2 representations."""
        result = verify_ibr([2, 2, 2])
        assert result['ibr_holds']

    def test_ibr_spin_1(self):
        """IBR for three spin-1 representations."""
        result = verify_ibr([3, 3, 3])
        assert result['ibr_holds']

    def test_ibr_mixed_reps(self):
        """IBR for mixed representations."""
        result = verify_ibr([2, 3, 2])
        assert result['ibr_holds']

    def test_ibr_spin_3half(self):
        """IBR for three spin-3/2 representations."""
        result = verify_ibr([4, 4, 4])
        assert result['ibr_holds']

    def test_ibr_all_mixed(self):
        """IBR for three different representations."""
        result = verify_ibr([2, 3, 4])
        assert result['ibr_holds']

    def test_ibr_higher_spin(self):
        """IBR for spin-2 representations."""
        result = verify_ibr([5, 5, 5])
        assert result['ibr_holds']


# ============================================================
# Path 2: Collision-depth expansion
# ============================================================

class TestCollisionDepthExpansion:
    """Test collision-depth structure matches family classification."""

    def test_km_sl2_depth(self):
        """KM sl_2: OPE pole 2, k_max = 1 (d log absorption)."""
        result = collision_depth_expansion('km_sl2', {'level': 1}, 3)
        assert result['ope_max_pole'] == 2
        assert result['k_max'] == 1
        assert result['differential_order'] == 0

    def test_virasoro_depth(self):
        """Virasoro: OPE pole 4, k_max = 3."""
        result = collision_depth_expansion('virasoro', {'central_charge': 25}, 3)
        assert result['ope_max_pole'] == 4
        assert result['k_max'] == 3
        assert result['differential_order'] == 1  # First-order on primaries

    def test_w3_depth(self):
        """W_3: OPE pole 6, k_max = 5."""
        result = collision_depth_expansion('w3', {'central_charge': 2}, 3)
        assert result['ope_max_pole'] == 6
        assert result['k_max'] == 5
        assert result['differential_order'] == 4  # Order 2N-2 = 4

    def test_wn_depth_formula(self):
        """W_N: k_max = 2N-1 for all N."""
        for N in range(2, 8):
            result = collision_depth_expansion('wN', {'N': N}, 3)
            assert result['k_max'] == 2 * N - 1
            assert result['ope_max_pole'] == 2 * N
            assert result['differential_order'] == 2 * N - 2

    def test_dlog_absorption_consistent(self):
        """k_max = ope_max_pole - 1 for all families (AP19 d log absorption)."""
        families = [
            ('km_sl2', {'level': 1}),
            ('virasoro', {'central_charge': 1}),
            ('w3', {'central_charge': 2}),
        ]
        for fam, params in families:
            result = collision_depth_expansion(fam, params, 3)
            assert result['k_max'] == result['ope_max_pole'] - 1, (
                f"d log absorption violated for {fam}: "
                f"k_max={result['k_max']} != ope_pole-1={result['ope_max_pole']-1}"
            )


# ============================================================
# Three-path cross-verification
# ============================================================

class TestThreePathVerification:
    """Cross-verify all three paths for consistency."""

    def test_km_sl2_three_paths(self):
        """Three-path verification for sl_2 at level 1."""
        result = three_path_verification(
            'km_sl2', {'level': 1, 'dims': [2, 2, 2]}, n_points=3
        )
        assert result['path1_flatness']['all_pass']
        assert result['path2_collision_depth']['k_max'] == 1
        assert result['path3_ibr']['ibr_holds']
        assert result['paths_consistent']

    def test_km_sl2_level2_three_paths(self):
        """Three-path verification for sl_2 at level 2."""
        result = three_path_verification(
            'km_sl2', {'level': 2, 'dims': [3, 3, 3]}, n_points=3
        )
        assert result['path1_flatness']['all_pass']
        assert result['path3_ibr']['ibr_holds']

    def test_virasoro_three_paths(self):
        """Three-path verification for Virasoro."""
        result = three_path_verification(
            'virasoro', {'central_charge': 25, 'weights': [0.5, 0.5, 1.0, 0.25]},
            n_points=4
        )
        assert result['path2_collision_depth']['k_max'] == 3
        assert result['path3_ward']['commutativity_automatic']


# ============================================================
# Koszulness / non-renormalization correspondence
# ============================================================

class TestKoszulnessNonRenormalization:
    """Test Koszulness <-> non-renormalization (thm:dnp-bar-cobar-identification(iii))."""

    def test_km_koszul_and_one_loop(self):
        """Affine KM: chirally Koszul AND one-loop exact."""
        result = koszulness_implies_one_loop_exactness('km_sl2', {'level': 1})
        assert result['chirally_koszul']
        assert result['one_loop_exact']
        assert result['e2_collapse']
        assert result['higher_m_k_vanish']

    def test_virasoro_koszul_but_nonformality(self):
        """Virasoro: chirally Koszul but SC non-formal (AP14)."""
        result = koszulness_implies_one_loop_exactness('virasoro', {'central_charge': 25})
        assert result['chirally_koszul']
        assert result['one_loop_exact']
        assert result['e2_collapse']
        # Key: m_k^SC != 0 even though chirally Koszul
        assert not result['higher_m_k_vanish']
        assert result['shadow_depth'] == float('inf')

    def test_heisenberg_class_g(self):
        """Heisenberg: class G, maximally simple."""
        result = koszulness_implies_one_loop_exactness('heisenberg', {'level': 1})
        assert result['chirally_koszul']
        assert result['one_loop_exact']
        assert result['higher_m_k_vanish']
        assert result['shadow_depth'] == 2

    def test_shadow_depth_classification(self):
        """Shadow depth: G=2 < L=3 < C=4 < M=infinity."""
        depths = {
            'heisenberg': koszulness_implies_one_loop_exactness('heisenberg', {'level': 1})['shadow_depth'],
            'km_sl2': koszulness_implies_one_loop_exactness('km_sl2', {'level': 1})['shadow_depth'],
            'virasoro': koszulness_implies_one_loop_exactness('virasoro', {'central_charge': 25})['shadow_depth'],
        }
        assert depths['heisenberg'] == 2  # Class G
        assert depths['km_sl2'] == 3      # Class L
        assert depths['virasoro'] == float('inf')  # Class M


# ============================================================
# BPZ structure tests
# ============================================================

class TestBPZStructure:
    """Test Virasoro BPZ Hamiltonian structure."""

    def test_bpz_4pt_ward(self):
        """4-point BPZ Ward identities satisfied."""
        result = verify_bpz_commutativity_4pt([0.5, 0.5, 0.5, 0.5], c=25)
        assert result['ward_translation']
        assert result['ward_dilation']

    def test_bpz_4pt_automatic_commutativity(self):
        """4-point commutativity is automatic (1D moduli space)."""
        result = verify_bpz_commutativity_4pt([1, 1, 1, 1], c=1)
        assert result['commutativity_automatic']


# ============================================================
# Consistency: KZ is genus-0 shadow of Theta for KM
# ============================================================

class TestKZFromMCElement:
    """Verify KZ connection = Sh_{0,n}(Theta_A) for affine KM.

    This is Theorem thm:shadow-connection-kz:
    nabla^hol_{0,n} = nabla^KZ for A = hat{g}_k.
    """

    def test_kz_prefactor(self):
        """KZ prefactor is 1/(k+h^v), not 1/k."""
        for k in [1, 2, 3, 5]:
            h_dual = 2  # sl_2
            expected_prefactor = 1.0 / (k + h_dual)
            # Check by computing H_1 for 2 points and comparing
            positions = [0.0, 1.0]
            Hs = kz_hamiltonians(2, [2, 2], positions, level=k, h_dual=h_dual)
            # H_1 = (1/(k+h^v)) * Omega_{12} / (z_1 - z_2) = -(1/(k+h^v)) * Omega
            Omega = _embed_casimir_direct([2, 2], 0, 1)
            expected_H1 = expected_prefactor * Omega / (0.0 - 1.0)
            np.testing.assert_allclose(Hs[0], expected_H1, atol=1e-14)

    def test_kz_sum_zero(self):
        """Translation invariance: sum_i H_i = 0 (after removing center of mass)."""
        positions = [0.0, 1.0, 0.5 + 0.5j]
        Hs = kz_hamiltonians(3, [2, 2, 2], positions, level=1)
        total = sum(Hs)
        # sum H_i = 0 because sum_i sum_{j!=i} Omega_{ij}/z_{ij} = 0
        # (each pair (i,j) contributes Omega_{ij}/z_{ij} + Omega_{ji}/z_{ji} = 0)
        np.testing.assert_allclose(total, 0, atol=1e-12)


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
