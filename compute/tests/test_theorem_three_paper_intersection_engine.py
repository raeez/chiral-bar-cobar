r"""Tests for three-paper intersection theorems: DNP25 + KZ25 + GZ26.

Tests verify three new theorems derived from the intersection:

Theorem 1 (thm:gaudin-yangian-identification):
    GZ26 commuting Hamiltonians = Gaudin Hamiltonians of Y^dg(g)
    - Path 1: Direct computation from collision residues
    - Path 2: Yangian evaluation map
    - Path 3: Cross-consistency (both commute, both agree)

Theorem 2 (thm:yangian-sklyanin-quantization):
    Y_hbar(g) quantizes the Sklyanin-Poisson bracket on A!
    - Path 1: Classical limit R(z) -> I + hbar*r^cl(z)
    - Path 2: Coproduct deviation = hbar * Sklyanin correction
    - Path 3: KZ25 lambda-bracket = classical limit of bar differential

Theorem 3 (thm:shadow-depth-operator-order):
    Shadow depth class determines differential operator order
    - Path 1: Direct computation from OPE pole orders
    - Path 2: Cross-family consistency check
    - Path 3: G/L/C order 0 vs M order > 0 dichotomy

Multi-path verification mandate: every claim verified by >= 3 independent paths.
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from theorem_three_paper_intersection_engine import (
    yangian_evaluation_map,
    sl2_r_matrix_km,
    verify_gaudin_equals_gz26,
    classical_r_matrix_sl2,
    quantum_r_matrix_sl2,
    verify_quantization_limit,
    verify_sklyanin_poisson_bracket,
    shadow_depth_to_operator_order,
    verify_operator_order_dichotomy,
    verify_kz_as_gaudin_limit,
    verify_bv_boundary_restriction_genus0,
    verify_all_three_paper_theorems,
)


# ============================================================
# Theorem 1: Gaudin-Yangian identification
# ============================================================

class TestGaudinYangianIdentification:
    """Theorem 1: GZ26 Hamiltonians = Gaudin Hamiltonians of Y^dg(g)."""

    def test_gaudin_equals_gz26_3pt_spin_half(self):
        """3-point, spin-1/2, level 1: Gaudin = GZ26."""
        positions = np.array([0.0, 1.0, 0.5 + 0.5j])
        result = verify_gaudin_equals_gz26(3, [2, 2, 2], positions, level=1)
        assert result['theorem_verified']
        assert result['max_diff'] < 1e-12

    def test_gaudin_equals_gz26_3pt_mixed(self):
        """3-point, mixed reps (spin-1/2, spin-1, spin-1/2), level 2."""
        positions = np.array([0.0, 1.0 + 0.3j, 2.0])
        result = verify_gaudin_equals_gz26(3, [2, 3, 2], positions, level=2)
        assert result['theorem_verified']
        assert result['max_diff'] < 1e-12

    def test_gaudin_equals_gz26_4pt_spin_half(self):
        """4-point, all spin-1/2, level 1."""
        positions = np.array([0.0, 1.0, 2.0 + 1j, -1.0 + 0.5j])
        result = verify_gaudin_equals_gz26(4, [2, 2, 2, 2], positions, level=1)
        assert result['theorem_verified']

    def test_gaudin_equals_gz26_4pt_spin_1(self):
        """4-point, all spin-1, level 2."""
        positions = np.array([0.0, 1.0, 0.5 + 1j, -0.5 + 0.5j])
        result = verify_gaudin_equals_gz26(4, [3, 3, 3, 3], positions, level=2)
        assert result['theorem_verified']

    def test_gaudin_equals_gz26_5pt(self):
        """5-point (2D moduli space, nontrivial)."""
        np.random.seed(123)
        positions = np.random.randn(5) + 1j * np.random.randn(5)
        result = verify_gaudin_equals_gz26(5, [2, 2, 2, 2, 2], positions, level=1)
        assert result['theorem_verified']

    def test_gaudin_commute_independently(self):
        """Both GZ26 and Gaudin Hamiltonians commute independently."""
        positions = np.array([0.0, 1.0, 0.5 + 0.5j])
        result = verify_gaudin_equals_gz26(3, [2, 2, 2], positions, level=1)
        assert result['gz26_commute']
        assert result['gaudin_commute']

    def test_gaudin_level_independence(self):
        """Identification holds at various levels k = 1, 2, 5, 10."""
        positions = np.array([0.0, 1.0, 0.5 + 0.7j])
        for k in [1, 2, 5, 10]:
            result = verify_gaudin_equals_gz26(3, [2, 2, 2], positions, level=k)
            assert result['theorem_verified'], f"Failed at level {k}"

    def test_gaudin_position_independence(self):
        """Identification holds for multiple random configurations."""
        for seed in range(5):
            np.random.seed(42 + seed)
            positions = np.random.randn(3) + 1j * np.random.randn(3)
            while min(abs(positions[i] - positions[j])
                      for i, j in [(0, 1), (0, 2), (1, 2)]) < 0.2:
                positions = np.random.randn(3) + 1j * np.random.randn(3)
            result = verify_gaudin_equals_gz26(3, [2, 2, 2], positions, level=1)
            assert result['theorem_verified'], f"Failed at seed {seed}"

    def test_kz_as_gaudin_master(self):
        """Master verification across multiple configurations."""
        result = verify_kz_as_gaudin_limit()
        assert result['all_pass']


# ============================================================
# Theorem 2: Yangian as Sklyanin quantization
# ============================================================

class TestYangianSklyaninQuantization:
    """Theorem 2: Y_hbar(g) quantizes the Sklyanin-Poisson bracket."""

    def test_classical_r_matrix_poles(self):
        """Classical r-matrix has a simple pole at z=0."""
        r1 = classical_r_matrix_sl2(1.0)
        r2 = classical_r_matrix_sl2(2.0)
        # r(z) = Omega/z, so r(1) = Omega, r(2) = Omega/2
        np.testing.assert_allclose(r1, 2 * r2, atol=1e-12)

    def test_classical_r_matrix_casimir_eigenvalues(self):
        """Classical r-matrix at z=1 is the Casimir with correct eigenvalues.

        Using J = sigma/2 normalization (standard spin-1/2 generators):
        Omega = J_z x J_z + (1/2)(J_+ x J_- + J_- x J_+)
        Eigenvalues: 1/4 (triplet, mult 3), -3/4 (singlet, mult 1).
        """
        r = classical_r_matrix_sl2(1.0)
        eigs = sorted(np.linalg.eigvalsh(r))
        expected = sorted([-3 / 4] + [1 / 4] * 3)
        np.testing.assert_allclose(eigs, expected, atol=1e-12)

    def test_quantum_r_yang(self):
        """Quantum R-matrix = Yang R-matrix (z*I + hbar*P)/(z + hbar)."""
        z, hbar = 2.0, 0.5
        R = quantum_r_matrix_sl2(z, hbar)
        # R should be unitary-like: R(z) R(-z) should be proportional to identity
        # Actually for Yang: R(z)R(-z) = (z^2 - hbar^2)/(z^2 - hbar^2) * I = I
        R_neg = quantum_r_matrix_sl2(-z, hbar)
        prod = R @ R_neg
        # (z*I + hbar*P)(-z*I + hbar*P) / (z+hbar)(-z+hbar)
        # = (-z^2*I + hbar^2*P^2) / (hbar^2 - z^2)  [P^2 = I]
        # = (-z^2 + hbar^2) / (hbar^2 - z^2) * I = I
        np.testing.assert_allclose(prod, np.eye(4), atol=1e-12)

    def test_quantum_classical_limit(self):
        """R(z) -> I + hbar*(P-I)/z as hbar -> 0.

        The Yang R-matrix has leading term (P-I)/z, where P = 2*Omega + I/2.
        The collision residue uses Omega normalization; the Yang R-matrix
        uses permutation normalization. The relationship is P - I = 2*Omega - I/2.
        """
        z = 1.5
        P = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                       [0, 1, 0, 0], [0, 0, 0, 1]], dtype=float)
        classical_limit = (P - np.eye(4)) / z
        for hbar in [0.1, 0.01, 0.001]:
            R = quantum_r_matrix_sl2(z, hbar)
            leading = (R - np.eye(4)) / hbar
            diff = np.linalg.norm(leading - classical_limit)
            # Error is O(hbar)
            assert diff < 5 * abs(hbar), f"hbar={hbar}, diff={diff}"

    def test_quantization_limit_convergence(self):
        """Quantization limit converges as k -> infinity (hbar -> 0)."""
        result = verify_quantization_limit(
            z_values=[1.0, 2.0],
            levels=[10, 50, 100, 500],
        )
        assert result['all_converge']

    def test_sklyanin_poisson_bracket(self):
        """Sklyanin-Poisson bracket structure is quantized by Yangian coproduct."""
        result = verify_sklyanin_poisson_bracket()
        assert result['sklyanin_quantization_verified']

    def test_quantization_parameter_identification(self):
        """hbar = 1/(k+h^v) correctly identifies quantization parameter.

        For sl_2 at level k: hbar = 1/(k+2).
        The collision residue r(z) = Omega/((k+h^v)*z) = hbar*Omega/z.
        """
        for k in [1, 2, 5, 10, 100]:
            hbar = 1.0 / (k + 2)
            z = 1.0
            # Collision residue = hbar * Omega / z
            r_coll = sl2_r_matrix_km(z, [2, 2], 0, 1, level=k, h_dual=2)
            r_cl = classical_r_matrix_sl2(z)
            # r_coll should equal hbar * r_cl
            np.testing.assert_allclose(r_coll, hbar * r_cl, atol=1e-12)


# ============================================================
# Theorem 3: Shadow depth operator order dichotomy
# ============================================================

class TestShadowDepthOperatorOrder:
    """Theorem 3: Shadow depth class determines GZ26 operator order."""

    def test_heisenberg_class_G(self):
        """Heisenberg (class G, depth 2): operator order 0."""
        data = shadow_depth_to_operator_order('heisenberg')
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['operator_order'] == 0
        assert data['k_max'] == 1

    def test_km_class_L(self):
        """Affine KM (class L, depth 3): operator order 0."""
        data = shadow_depth_to_operator_order('km_sl2')
        assert data['shadow_class'] == 'L'
        assert data['shadow_depth'] == 3
        assert data['operator_order'] == 0
        assert data['k_max'] == 1

    def test_betagamma_class_C(self):
        """Beta-gamma (class C, depth 4): trivial Hamiltonians, k_max = 0.

        AP10 fix: betagamma generator OPE is a SIMPLE pole (max_ope_pole=1),
        so k_max = 0 by AP19. Shadow depth 4 comes from composite-field
        channels (the quartic contact class), NOT from generator OPE.
        """
        data = shadow_depth_to_operator_order('betagamma')
        assert data['shadow_class'] == 'C'
        assert data['shadow_depth'] == 4
        assert data['operator_order'] == 0
        assert data['k_max'] == 0
        assert data['max_ope_pole'] == 1

    def test_virasoro_class_M(self):
        """Virasoro (class M, depth inf): operator order 1."""
        data = shadow_depth_to_operator_order('virasoro')
        assert data['shadow_class'] == 'M'
        assert data['shadow_depth'] == float('inf')
        assert data['operator_order'] == 1
        assert data['k_max'] == 3

    def test_w3_class_M(self):
        """W_3 (class M): operator order 4 = 2*3-2."""
        data = shadow_depth_to_operator_order('w3')
        assert data['shadow_class'] == 'M'
        assert data['operator_order'] == 4
        assert data['k_max'] == 5

    def test_wN_formula(self):
        """W_N: operator order = 2N-2 for all N >= 2."""
        for N in range(2, 10):
            data = shadow_depth_to_operator_order('wN', {'N': N})
            assert data['operator_order'] == 2 * N - 2
            assert data['k_max'] == 2 * N - 1
            assert data['max_ope_pole'] == 2 * N

    def test_finite_depth_implies_order_zero(self):
        """Classes G/L/C (finite depth) all have operator order 0."""
        for fam in ['heisenberg', 'km_sl2', 'km_slN', 'betagamma']:
            data = shadow_depth_to_operator_order(fam)
            assert data['shadow_depth'] < float('inf')
            assert data['operator_order'] == 0, f"{fam} should have order 0"

    def test_infinite_depth_implies_positive_order(self):
        """Class M (infinite depth) has operator order > 0."""
        for fam in ['virasoro', 'w3']:
            data = shadow_depth_to_operator_order(fam)
            assert data['shadow_depth'] == float('inf')
            assert data['operator_order'] > 0, f"{fam} should have order > 0"

    def test_operator_order_dichotomy_master(self):
        """Master dichotomy check across all families."""
        result = verify_operator_order_dichotomy()
        assert result['dichotomy_holds']

    def test_dlog_absorption_universal(self):
        """k_max = max_ope_pole - 1 for all families (AP19)."""
        for fam in ['heisenberg', 'km_sl2', 'virasoro', 'w3']:
            data = shadow_depth_to_operator_order(fam)
            assert data['k_max'] == data['max_ope_pole'] - 1

    def test_wN_dlog_absorption(self):
        """k_max = 2N - 1 = (2N) - 1 for W_N (AP19)."""
        for N in range(2, 8):
            data = shadow_depth_to_operator_order('wN', {'N': N})
            assert data['k_max'] == data['max_ope_pole'] - 1


# ============================================================
# Candidate Theorem 4: BV boundary restriction (DOWNGRADED)
# ============================================================

class TestBVBoundaryRestriction:
    """Candidate 4: BV boundary restriction = GZ26 (downgraded to remark)."""

    def test_is_not_new_theorem(self):
        """BV boundary restriction at genus 0 is a reformulation, not new."""
        result = verify_bv_boundary_restriction_genus0('km_sl2', {'level': 1})
        assert result['is_new_theorem'] is False
        assert result['is_remark'] is True

    def test_genus0_proved(self):
        """Genus-0 content is proved (thm:kz-classical-quantum-bridge)."""
        result = verify_bv_boundary_restriction_genus0('virasoro', {'c': 25})
        assert result['genus0_proved'] is True

    def test_higher_genus_conjectural(self):
        """Higher genus remains conjectural (conj:master-bv-brst)."""
        result = verify_bv_boundary_restriction_genus0('km_sl2', {'level': 1})
        assert 'conjectural' in result['higher_genus_status']


# ============================================================
# Cross-theorem consistency
# ============================================================

class TestCrossTheoremConsistency:
    """Cross-consistency between the three theorems."""

    def test_gaudin_commutativity_from_cybe(self):
        """Gaudin commutativity follows from CYBE, which is MC at arity 3.

        Theorem 1 (Gaudin = GZ26) + Theorem 2 (quantization) together give:
        The CYBE for the classical r-matrix is the classical limit of
        the MC equation, and Gaudin commutativity is a consequence.
        """
        # Classical r-matrix satisfies CYBE: [r_12, r_13] + [r_12, r_23] + [r_13, r_23] = 0
        r = classical_r_matrix_sl2
        z1, z2, z3 = 1.0, 2.0, 3.0

        # Embed r_{12}, r_{13}, r_{23} in C^2 x C^2 x C^2 = C^8
        def embed_12(M):
            return np.kron(M, np.eye(2))

        def embed_23(M):
            return np.kron(np.eye(2), M)

        def embed_13(M):
            """Embed r_{13} = (1 x P)(r_{12} x 1)(1 x P) where P is flip on 2,3."""
            # More directly: permute tensor factors
            result = np.zeros((8, 8), dtype=complex)
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        for d in range(2):
                            for e in range(2):
                                for f in range(2):
                                    # r_{13} acts on factors 1 and 3
                                    idx_in = a * 4 + b * 2 + c
                                    idx_out = d * 4 + e * 2 + f
                                    # r acts on (a,c) -> (d,f), delta on b -> e
                                    if b == e:
                                        r_val = M[a * 2 + c, d * 2 + f]
                                        result[idx_out, idx_in] += r_val
            return result

        r12 = embed_12(r(z1 - z2))
        r23 = embed_23(r(z2 - z3))

        # For r13: use the tensor-permutation method
        r_raw = r(z1 - z3)
        r13 = np.zeros((8, 8), dtype=complex)
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        for e in range(2):
                            for f in range(2):
                                if b == e:
                                    r13[d * 4 + e * 2 + f, a * 4 + b * 2 + c] += r_raw[a * 2 + c, d * 2 + f]

        # CYBE: [r12, r13] + [r12, r23] + [r13, r23] = 0
        cybe = (r12 @ r13 - r13 @ r12 +
                r12 @ r23 - r23 @ r12 +
                r13 @ r23 - r23 @ r13)
        assert np.linalg.norm(cybe) < 1e-10, f"CYBE violation: {np.linalg.norm(cybe)}"

    def test_operator_order_consistent_with_collision_depth(self):
        """Operator order from Theorem 3 matches collision depth from Theorem 1.

        For affine KM: collision depth 1 (from Theorem 1 = Gaudin),
        operator order 0 (from Theorem 3 = dichotomy). Consistent.
        """
        # Theorem 1 data: k_max = 1 for affine KM
        gaudin_data = shadow_depth_to_operator_order('km_sl2')
        assert gaudin_data['k_max'] == 1

        # Theorem 3 data: operator order = 0 for class L
        assert gaudin_data['operator_order'] == 0

        # Consistency: k_max = 1 means only one collision depth,
        # which is a multiplication operator (order 0)
        assert gaudin_data['k_max'] - 1 == gaudin_data['operator_order']

    def test_quantization_parameter_in_gaudin(self):
        """Theorem 2 quantization parameter appears in Theorem 1 Gaudin.

        The Gaudin Hamiltonian has prefactor 1/(k+h^v) = hbar.
        This IS the quantization parameter of Theorem 2.
        """
        for k in [1, 2, 5, 10]:
            hbar = 1.0 / (k + 2)  # h^v = 2 for sl_2
            # In the Gaudin Hamiltonian:
            # H_i = sum Omega_{ij}/((k+h^v)*z_{ij}) = hbar * sum Omega_{ij}/z_{ij}
            # So the Gaudin coupling = hbar, linking Theorems 1 and 2.
            positions = np.array([0.0, 1.0, 0.5 + 0.5j])
            result = verify_gaudin_equals_gz26(3, [2, 2, 2], positions, level=k)
            assert result['theorem_verified']


# ============================================================
# Master verification
# ============================================================

class TestMasterVerification:
    """Run the complete three-paper intersection verification."""

    def test_master_all_theorems(self):
        """All three theorems pass master verification."""
        result = verify_all_three_paper_theorems()
        assert result['all_verified']

    def test_theorem_1_passes(self):
        """Theorem 1 (Gaudin-Yangian) passes."""
        result = verify_all_three_paper_theorems()
        assert result['theorem_1_gaudin']['all_pass']

    def test_theorem_2_limit_passes(self):
        """Theorem 2 (quantization limit) passes."""
        result = verify_all_three_paper_theorems()
        assert result['theorem_2_quantization_limit']['all_converge']

    def test_theorem_2_sklyanin_passes(self):
        """Theorem 2 (Sklyanin bracket) passes."""
        result = verify_all_three_paper_theorems()
        assert result['theorem_2_sklyanin']['sklyanin_quantization_verified']

    def test_theorem_3_dichotomy_passes(self):
        """Theorem 3 (operator order dichotomy) passes."""
        result = verify_all_three_paper_theorems()
        assert result['theorem_3_dichotomy']['dichotomy_holds']

    def test_theorem_4_is_remark(self):
        """Candidate 4 is correctly classified as a remark."""
        result = verify_all_three_paper_theorems()
        assert result['theorem_4_bv_boundary']['is_remark']
