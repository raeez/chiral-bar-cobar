r"""Tests for DNP meromorphic tensor product = ordered bar coproduct.

Tests verify Theorem thm:dnp-bar-cobar-identification:
- Path 1: Fusion coefficients from R-twisted coproduct match Verlinde
- Path 2: Collision residue gives r-matrix satisfying CYBE
- Path 3: Koszulness <=> non-renormalization for all standard families

Multi-path verification mandate: every claim verified by >= 3 independent paths.
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from theorem_dnp_meromorphic_tensor_engine import (
    verlinde_coefficients_sl2,
    verify_verlinde_integrality,
    verify_verlinde_level1,
    verify_verlinde_level2,
    verify_cybe_sl2,
    verify_collision_residue_is_r_matrix,
    bar_spectral_sequence_data,
    verify_koszulness_nonrenormalization_equivalence,
    verify_fusion_from_bar_sl2,
    classical_r_matrix_sl2,
)


# ============================================================
# Path 1: Verlinde fusion and R-twisted coproduct
# ============================================================

class TestVerlindeFusion:
    """Test that R-twisted coproduct reproduces Verlinde fusion rules."""

    def test_verlinde_level1_explicit(self):
        """sl_2 level 1: Z/2 fusion ring."""
        result = verify_verlinde_level1()
        assert result['all_match'], f"Mismatches: {result['mismatches']}"

    def test_verlinde_level2_explicit(self):
        """sl_2 level 2: three reps with known fusion rules."""
        result = verify_verlinde_level2()
        assert result['all_match'], f"Mismatches: {result['mismatches']}"

    def test_verlinde_integrality_level1(self):
        """Verlinde coefficients are non-negative integers at level 1."""
        result = verify_verlinde_integrality(1)
        assert result['all_integer']
        assert result['all_nonneg']

    def test_verlinde_integrality_level2(self):
        """Verlinde coefficients are non-negative integers at level 2."""
        result = verify_verlinde_integrality(2)
        assert result['all_integer']
        assert result['all_nonneg']

    def test_verlinde_integrality_level3(self):
        """Verlinde coefficients are non-negative integers at level 3."""
        result = verify_verlinde_integrality(3)
        assert result['all_integer']
        assert result['all_nonneg']

    def test_verlinde_integrality_level5(self):
        """Verlinde coefficients are non-negative integers at level 5."""
        result = verify_verlinde_integrality(5)
        assert result['all_integer']
        assert result['all_nonneg']

    def test_verlinde_integrality_level10(self):
        """Verlinde coefficients are non-negative integers at level 10."""
        result = verify_verlinde_integrality(10)
        assert result['all_integer']
        assert result['all_nonneg']

    def test_s_matrix_unitary(self):
        """Modular S-matrix is unitary."""
        for level in [1, 2, 3, 5]:
            N, S = verlinde_coefficients_sl2(level)
            product = S @ S.T
            np.testing.assert_allclose(product, np.eye(level + 1), atol=1e-10,
                                       err_msg=f"S not unitary at level {level}")

    def test_s_matrix_symmetric(self):
        """Modular S-matrix is symmetric."""
        for level in [1, 2, 3, 5]:
            N, S = verlinde_coefficients_sl2(level)
            np.testing.assert_allclose(S, S.T, atol=1e-14,
                                       err_msg=f"S not symmetric at level {level}")

    def test_fusion_associativity(self):
        """Fusion ring is associative for levels 1-5."""
        for level in [1, 2, 3, 4, 5]:
            result = verify_fusion_from_bar_sl2(level)
            assert result['associativity'], (
                f"Fusion not associative at level {level}"
            )

    def test_fusion_commutativity(self):
        """Fusion coefficients are symmetric: N^c_{ab} = N^c_{ba}."""
        for level in [1, 2, 3]:
            N, S = verlinde_coefficients_sl2(level)
            n = level + 1
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        assert abs(N[a, b, c] - N[b, a, c]) < 1e-10, (
                            f"N^{c}_{{{a},{b}}} != N^{c}_{{{b},{a}}} at level {level}"
                        )

    def test_vacuum_is_unit(self):
        """V_0 is the identity: N^c_{0,b} = delta_{bc}."""
        for level in [1, 2, 3, 5]:
            N, S = verlinde_coefficients_sl2(level)
            n = level + 1
            for b in range(n):
                for c in range(n):
                    expected = 1.0 if b == c else 0.0
                    actual = round(N[0, b, c].real)
                    assert actual == expected, (
                        f"V_0 not unit: N^{c}_{{0,{b}}} = {actual} != {expected}"
                    )


# ============================================================
# Path 2: Classical YBE and collision residue
# ============================================================

class TestClassicalYBE:
    """Test the classical Yang-Baxter equation for the collision residue."""

    def test_cybe_sl2(self):
        """CYBE holds for sl_2 classical r-matrix."""
        result = verify_cybe_sl2()
        assert result['cybe_holds'], (
            f"CYBE violation: norm = {result['cybe_norm']}"
        )

    def test_cybe_multiple_points(self):
        """CYBE holds at multiple (z,w) values."""
        for z, w in [(1.0, 2.0), (0.5+0.3j, 0.7-0.2j),
                     (3.0+1j, -1.0+2j), (0.1, 10.0)]:
            # Recompute at each point
            Id = np.eye(2, dtype=complex)
            sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2
            sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
            sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2
            gens = [sx, sy, sz]

            r12 = np.kron(classical_r_matrix_sl2(z), Id)
            Omega_13 = sum(np.kron(np.kron(g, Id), g) for g in gens)
            r13 = Omega_13 / (z + w)
            r23 = np.kron(Id, classical_r_matrix_sl2(w))

            comm = (r12 @ r13 - r13 @ r12 +
                    r12 @ r23 - r23 @ r12 +
                    r13 @ r23 - r23 @ r13)
            norm = np.linalg.norm(comm)
            assert norm < 1e-10, (
                f"CYBE fails at z={z}, w={w}: norm={norm}"
            )

    def test_r_matrix_antisymmetric(self):
        """Classical r-matrix satisfies r_{12}(z) = -r_{21}(-z) (antisymmetry)."""
        z = 1.0 + 0.5j
        r = classical_r_matrix_sl2(z)
        # r_{21}(-z) = P . r(-z) . P where P is the permutation
        P = np.array([[1, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]], dtype=complex)
        r_neg = classical_r_matrix_sl2(-z)
        r21_neg = P @ r_neg @ P
        np.testing.assert_allclose(r, -r21_neg, atol=1e-14)

    def test_collision_residue_data(self):
        """Collision residue structure is consistent."""
        result = verify_collision_residue_is_r_matrix()
        assert result['consistent_with_kz']


# ============================================================
# Path 3: Koszulness <=> non-renormalization
# ============================================================

class TestKoszulnessNonRenormalization:
    """Test E_2-collapse <=> one-loop exactness for all standard families."""

    def test_all_families_consistent(self):
        """Koszulness = non-renormalization for all standard families."""
        result = verify_koszulness_nonrenormalization_equivalence()
        assert result['all_consistent'], (
            f"Inconsistent families: {[f for f in result['families'] if not f['consistent']]}"
        )

    def test_km_e2_collapse(self):
        """Affine KM: E_2-collapses (class L)."""
        for k in [1, 2, 3, 5]:
            data = bar_spectral_sequence_data('km_sl2', {'level': k})
            assert data['e2_collapse']
            assert data['koszulness_class'] == 'L (Lie/tree)'
            assert data['shadow_depth'] == 3

    def test_virasoro_koszul_but_class_m(self):
        """Virasoro: chirally Koszul (E_2-collapses) but class M."""
        for c in [1, 13, 25, 26]:
            data = bar_spectral_sequence_data('virasoro', {'central_charge': c})
            assert data['e2_collapse']
            assert data['koszulness_class'] == 'M (mixed, infinite)'
            assert data['shadow_depth'] == float('inf')
            assert not data['higher_ainfty_ops_vanish']

    def test_heisenberg_class_g(self):
        """Heisenberg: class G, simplest case."""
        data = bar_spectral_sequence_data('heisenberg', {'level': 1})
        assert data['e2_collapse']
        assert data['koszulness_class'] == 'G (Gaussian)'
        assert data['shadow_depth'] == 2
        assert data['higher_ainfty_ops_vanish']

    def test_betagamma_class_c(self):
        """Beta-gamma: class C (contact/quartic)."""
        data = bar_spectral_sequence_data('betagamma', {})
        assert data['e2_collapse']
        assert data['koszulness_class'] == 'C (contact/quartic)'
        assert data['shadow_depth'] == 4

    def test_shadow_depth_ordering(self):
        """Shadow depth: G(2) < L(3) < C(4) < M(inf)."""
        depths = {
            'G': bar_spectral_sequence_data('heisenberg', {'level': 1})['shadow_depth'],
            'L': bar_spectral_sequence_data('km_sl2', {'level': 1})['shadow_depth'],
            'C': bar_spectral_sequence_data('betagamma', {})['shadow_depth'],
            'M': bar_spectral_sequence_data('virasoro', {'central_charge': 1})['shadow_depth'],
        }
        assert depths['G'] < depths['L'] < depths['C'] < depths['M']

    def test_all_standard_koszul(self):
        """ALL standard families are chirally Koszul (AP14: shadow depth != Koszulness)."""
        families = [
            ('km_sl2', {'level': k}) for k in [1, 2, 3, 5]
        ] + [
            ('virasoro', {'central_charge': c}) for c in [1, 13, 25]
        ] + [
            ('heisenberg', {'level': k}) for k in [1, 2]
        ] + [
            ('betagamma', {}),
        ]
        for fam, params in families:
            data = bar_spectral_sequence_data(fam, params)
            assert data['e2_collapse'], f"{data['family']} should be chirally Koszul"
            assert data['one_loop_exact'], f"{data['family']} should be one-loop exact"


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
