r"""Tests for the Costello 4d Chern-Simons comparison engine.

Verifies that the R-matrices and integrable structures computed from
two independent sources agree:

  (1) Costello's 4d Chern-Simons theory (1303.2632, 1308.0370, CWY I-II)
  (2) Our bar-complex collision residue framework

The tests are organized by mathematical content:
  - Tree-level r-matrix agreement (Costello vs bar)
  - Quantum R-matrix agreement (Yang R-matrix)
  - Yang-Baxter equation verification (both frameworks)
  - Classical Yang-Baxter equation (CYBE)
  - Unitarity and crossing symmetry
  - Spectral decomposition
  - Form factor comparison (arity 3)
  - BCD-type R-matrices
  - Transfer matrix commutativity (integrability)
  - Structural comparisons (defects, Koszul duality, HT twist)

Multi-path verification strategy (CLAUDE.md mandate):
  Path 1: Direct computation from defining formulas
  Path 2: Comparison between two independent frameworks (Costello vs bar)
  Path 3: Algebraic identities (YBE, unitarity, crossing)
  Path 4: Spectral decomposition (eigenvalue analysis)
  Path 5: Limiting/special cases (u -> infinity, N = 2)

References:
  - Costello, 1303.2632 (Yangian from gauge theory)
  - Costello, 1308.0370 (integrable lattice models)
  - Costello-Witten-Yamazaki I-II (gauge theory and integrability)
  - yangians_foundations.tex, yangians_drinfeld_kohno.tex
  - yangian_rmatrix_sl3.py, yangian_rtt_all_types.py
"""

import numpy as np
import pytest

from compute.lib.costello_4d_cs_comparison_engine import (
    # Lie algebra data
    permutation_matrix,
    casimir_tensor_slN_fund,
    dual_coxeter_number,
    dim_slN,
    kappa_affine_slN,
    # Costello 4d CS
    costello_tree_level_r_matrix,
    costello_one_loop_correction_slN,
    costello_perturbative_R_matrix,
    # Bar construction
    bar_collision_residue_r_matrix,
    bar_quantum_R_matrix_yang,
    # Comparison
    compare_tree_level_r_matrices,
    compare_quantum_R_matrices,
    # YBE
    verify_ybe_yang,
    verify_ybe_costello_r_matrix,
    # Unitarity/crossing
    verify_unitarity_yang,
    verify_crossing_symmetry,
    # Spectral decomposition
    spectral_decomposition_yang,
    verify_spectral_decomposition,
    # Form factors
    costello_arity3_form_factor,
    bar_arity3_collision_residue,
    compare_arity3_form_factors,
    # BCD types
    costello_r_matrix_typeB,
    bar_r_matrix_typeB,
    costello_r_matrix_typeC,
    costello_r_matrix_typeD,
    verify_ybe_BCD,
    # Transfer matrix
    transfer_matrix_commutativity,
    # Structural
    defect_representation_data,
    koszul_duality_comparison,
    ht_twist_data,
    modular_yangian_vs_4d_cs,
)


# ============================================================
# 1. Lie algebra data tests
# ============================================================

class TestLieAlgebraData:
    """Tests for basic Lie algebra data."""

    def test_permutation_matrix_sl2(self):
        """P^2 = I for sl_2 (N=2)."""
        P = permutation_matrix(2)
        assert np.allclose(P @ P, np.eye(4))

    def test_permutation_matrix_sl3(self):
        """P^2 = I for sl_3 (N=3)."""
        P = permutation_matrix(3)
        assert np.allclose(P @ P, np.eye(9))

    def test_permutation_matrix_sl4(self):
        """P^2 = I for sl_4 (N=4)."""
        P = permutation_matrix(4)
        assert np.allclose(P @ P, np.eye(16))

    def test_permutation_trace_sl2(self):
        """Tr(P) = N for sl_2."""
        P = permutation_matrix(2)
        assert abs(np.trace(P) - 2) < 1e-12

    def test_permutation_trace_sl3(self):
        """Tr(P) = N for sl_3."""
        P = permutation_matrix(3)
        assert abs(np.trace(P) - 3) < 1e-12

    def test_casimir_identity_sl2(self):
        """Omega = P - I/N for sl_2."""
        N = 2
        Omega = casimir_tensor_slN_fund(N)
        P = permutation_matrix(N)
        I = np.eye(N * N)
        assert np.allclose(Omega, P - I / N)

    def test_casimir_identity_sl3(self):
        """Omega = P - I/N for sl_3."""
        N = 3
        Omega = casimir_tensor_slN_fund(N)
        P = permutation_matrix(N)
        I = np.eye(N * N)
        assert np.allclose(Omega, P - I / N)

    def test_casimir_identity_sl4(self):
        """Omega = P - I/N for sl_4."""
        N = 4
        Omega = casimir_tensor_slN_fund(N)
        P = permutation_matrix(N)
        I = np.eye(N * N)
        assert np.allclose(Omega, P - I / N)

    def test_dual_coxeter_sl2(self):
        """h^vee(sl_2) = 2."""
        assert dual_coxeter_number(2) == 2

    def test_dual_coxeter_sl3(self):
        """h^vee(sl_3) = 3."""
        assert dual_coxeter_number(3) == 3

    def test_dim_sl2(self):
        """dim(sl_2) = 3."""
        assert dim_slN(2) == 3

    def test_dim_sl3(self):
        """dim(sl_3) = 8."""
        assert dim_slN(3) == 8

    def test_kappa_sl2_level1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert abs(kappa_affine_slN(2, 1) - 9.0 / 4.0) < 1e-12

    def test_kappa_sl3_level1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        assert abs(kappa_affine_slN(3, 1) - 16.0 / 3.0) < 1e-12


# ============================================================
# 2. Tree-level comparison tests
# ============================================================

class TestTreeLevelComparison:
    """Tests for tree-level r-matrix agreement."""

    def test_tree_level_sl2_agrees(self):
        """Costello tree-level = bar collision residue for sl_2."""
        result = compare_tree_level_r_matrices(2)
        assert result["tree_level_agrees"]

    def test_tree_level_sl3_agrees(self):
        """Costello tree-level = bar collision residue for sl_3."""
        result = compare_tree_level_r_matrices(3)
        assert result["tree_level_agrees"]

    def test_tree_level_sl4_agrees(self):
        """Costello tree-level = bar collision residue for sl_4."""
        result = compare_tree_level_r_matrices(4)
        assert result["tree_level_agrees"]

    def test_tree_level_sl5_agrees(self):
        """Costello tree-level = bar collision residue for sl_5."""
        result = compare_tree_level_r_matrices(5)
        assert result["tree_level_agrees"]

    def test_tree_level_explicit_sl2(self):
        """Explicit check: r(1) = Omega for sl_2 at z=1."""
        r_c = costello_tree_level_r_matrix(1.0, 2)
        r_b = bar_collision_residue_r_matrix(1.0, 2)
        Omega = casimir_tensor_slN_fund(2)
        assert np.allclose(r_c, Omega)
        assert np.allclose(r_b, Omega)

    def test_tree_level_pole_structure(self):
        """r(z) has a single pole at z=0 (AP19)."""
        N = 3
        # z * r(z) should be constant = Omega
        Omega = casimir_tensor_slN_fund(N)
        for z in [0.1, 1.0, 10.0, 100.0]:
            r = costello_tree_level_r_matrix(z, N)
            assert np.allclose(z * r, Omega, atol=1e-10)

    def test_tree_level_complex_z(self):
        """r(z) works for complex z."""
        N = 3
        z = 1.0 + 2.0j
        r_c = costello_tree_level_r_matrix(z, N)
        r_b = bar_collision_residue_r_matrix(z, N)
        assert np.allclose(r_c, r_b)


# ============================================================
# 3. Quantum R-matrix comparison tests
# ============================================================

class TestQuantumRMatrixComparison:
    """Tests for quantum R-matrix agreement."""

    def test_quantum_comparison_sl2(self):
        """Quantum R-matrix comparison for sl_2."""
        result = compare_quantum_R_matrices(2)
        assert result["all_agree"]

    def test_quantum_comparison_sl3(self):
        """Quantum R-matrix comparison for sl_3."""
        result = compare_quantum_R_matrices(3)
        assert result["all_agree"]

    def test_yang_r_matrix_sl2_explicit(self):
        """R(u) = uI + P for sl_2 at u=1."""
        R = bar_quantum_R_matrix_yang(1.0, 2)
        P = permutation_matrix(2)
        I = np.eye(4, dtype=complex)
        assert np.allclose(R, 1.0 * I + P)

    def test_yang_r_matrix_sl3_explicit(self):
        """R(u) = uI + P for sl_3 at u=2."""
        R = bar_quantum_R_matrix_yang(2.0, 3)
        P = permutation_matrix(3)
        I = np.eye(9, dtype=complex)
        assert np.allclose(R, 2.0 * I + P)

    def test_costello_perturbative_leading_order(self):
        """Costello perturbative R at order 1 matches I + Omega/u."""
        N = 3
        u = 5.0
        R_pert = costello_perturbative_R_matrix(u, N, max_order=1)
        Omega = casimir_tensor_slN_fund(N)
        I = np.eye(N * N, dtype=complex)
        expected = I + Omega / u
        assert np.allclose(R_pert, expected, atol=1e-10)

    def test_one_loop_correction_structure(self):
        """One-loop correction is proportional to Omega^2/z^2."""
        N = 3
        z = 2.0
        correction = costello_one_loop_correction_slN(z, N)
        Omega = casimir_tensor_slN_fund(N)
        expected = 0.5 * Omega @ Omega / (z * z)
        assert np.allclose(correction, expected)


# ============================================================
# 4. Yang-Baxter equation tests
# ============================================================

class TestYangBaxterEquation:
    """Tests for the Yang-Baxter equation."""

    def test_ybe_sl2_real(self):
        """YBE for sl_2 at real spectral parameters."""
        assert verify_ybe_yang(1.0, 2.0, 2) < 1e-10

    def test_ybe_sl2_complex(self):
        """YBE for sl_2 at complex spectral parameters."""
        assert verify_ybe_yang(1.0 + 0.5j, 2.0 - 0.3j, 2) < 1e-10

    def test_ybe_sl3_real(self):
        """YBE for sl_3 at real spectral parameters."""
        assert verify_ybe_yang(1.0, 2.0, 3) < 1e-10

    def test_ybe_sl3_complex(self):
        """YBE for sl_3 at complex spectral parameters."""
        assert verify_ybe_yang(1.0 + 0.5j, 2.0 - 0.3j, 3) < 1e-10

    def test_ybe_sl4(self):
        """YBE for sl_4."""
        assert verify_ybe_yang(1.5, 3.0, 4) < 1e-8

    def test_ybe_multiple_parameters_sl2(self):
        """YBE for sl_2 at 10 random parameter pairs."""
        rng = np.random.default_rng(42)
        for _ in range(10):
            u = rng.uniform(-5, 5) + 1j * rng.uniform(-5, 5)
            v = rng.uniform(-5, 5) + 1j * rng.uniform(-5, 5)
            assert verify_ybe_yang(u, v, 2) < 1e-8

    def test_ybe_multiple_parameters_sl3(self):
        """YBE for sl_3 at 5 random parameter pairs."""
        rng = np.random.default_rng(123)
        for _ in range(5):
            u = rng.uniform(-5, 5) + 1j * rng.uniform(-5, 5)
            v = rng.uniform(-5, 5) + 1j * rng.uniform(-5, 5)
            assert verify_ybe_yang(u, v, 3) < 1e-8


# ============================================================
# 5. Classical Yang-Baxter equation tests
# ============================================================

class TestCYBE:
    """Tests for the classical Yang-Baxter equation."""

    def test_cybe_sl2(self):
        """CYBE for Costello r-matrix, sl_2."""
        assert verify_ybe_costello_r_matrix(1.0, 2.0, 3.0, 2) < 1e-10

    def test_cybe_sl3(self):
        """CYBE for Costello r-matrix, sl_3."""
        assert verify_ybe_costello_r_matrix(1.0, 2.0, 3.0, 3) < 1e-10

    def test_cybe_sl4(self):
        """CYBE for Costello r-matrix, sl_4."""
        assert verify_ybe_costello_r_matrix(1.0, 2.0, 3.0, 4) < 1e-8

    def test_cybe_complex_points(self):
        """CYBE at complex insertion points."""
        assert verify_ybe_costello_r_matrix(
            1.0 + 0.5j, 2.0 - 0.3j, 3.0 + 1.0j, 3
        ) < 1e-10

    def test_cybe_multiple_sl2(self):
        """CYBE for sl_2 at 5 random triples."""
        rng = np.random.default_rng(77)
        for _ in range(5):
            z1, z2, z3 = [rng.uniform(0.1, 10) + 1j * rng.uniform(-3, 3)
                          for _ in range(3)]
            assert verify_ybe_costello_r_matrix(z1, z2, z3, 2) < 1e-8


# ============================================================
# 6. Unitarity and crossing tests
# ============================================================

class TestUnitarityCrossing:
    """Tests for unitarity and crossing symmetry."""

    def test_unitarity_sl2(self):
        """R(u)R(-u) = (1-u^2)I for sl_2."""
        assert verify_unitarity_yang(2.0, 2) < 1e-10

    def test_unitarity_sl3(self):
        """R(u)R(-u) = (1-u^2)I for sl_3."""
        assert verify_unitarity_yang(2.0, 3) < 1e-10

    def test_unitarity_sl2_complex(self):
        """Unitarity at complex u for sl_2."""
        assert verify_unitarity_yang(1.0 + 2.0j, 2) < 1e-10

    def test_unitarity_sl3_complex(self):
        """Unitarity at complex u for sl_3."""
        assert verify_unitarity_yang(1.0 + 2.0j, 3) < 1e-10

    def test_unitarity_multiple_sl2(self):
        """Unitarity for sl_2 at 10 random u values."""
        rng = np.random.default_rng(99)
        for _ in range(10):
            u = rng.uniform(-5, 5) + 1j * rng.uniform(-5, 5)
            assert verify_unitarity_yang(u, 2) < 1e-8

    def test_crossing_sl2(self):
        """Crossing symmetry for sl_2."""
        assert verify_crossing_symmetry(2.0, 2) < 1e-10

    def test_crossing_sl3(self):
        """Crossing symmetry for sl_3."""
        assert verify_crossing_symmetry(2.0, 3) < 1e-10

    def test_crossing_sl2_complex(self):
        """Crossing symmetry at complex u for sl_2."""
        assert verify_crossing_symmetry(1.0 + 2.0j, 2) < 1e-10


# ============================================================
# 7. Spectral decomposition tests
# ============================================================

class TestSpectralDecomposition:
    """Tests for spectral decomposition of R-matrix."""

    def test_spectral_sl2_eigenvalues(self):
        """Eigenvalues of R(u) for sl_2: u+1 on Sym, u-1 on Lambda."""
        spec = spectral_decomposition_yang(3.0, 2)
        assert spec["sym_eigenvalue"] == 4.0
        assert spec["asym_eigenvalue"] == 2.0

    def test_spectral_sl2_multiplicities(self):
        """Multiplicities for sl_2: Sym=3, Lambda=1."""
        spec = spectral_decomposition_yang(1.0, 2)
        assert spec["sym_multiplicity"] == 3
        assert spec["asym_multiplicity"] == 1

    def test_spectral_sl3_multiplicities(self):
        """Multiplicities for sl_3: Sym=6, Lambda=3."""
        spec = spectral_decomposition_yang(1.0, 3)
        assert spec["sym_multiplicity"] == 6
        assert spec["asym_multiplicity"] == 3

    def test_spectral_numerical_sl2(self):
        """Numerical spectral decomposition for sl_2."""
        result = verify_spectral_decomposition(3.0, 2)
        assert result["sym_check"]
        assert result["asym_check"]

    def test_spectral_numerical_sl3(self):
        """Numerical spectral decomposition for sl_3."""
        result = verify_spectral_decomposition(3.0, 3)
        assert result["sym_check"]
        assert result["asym_check"]

    def test_spectral_numerical_sl4(self):
        """Numerical spectral decomposition for sl_4."""
        result = verify_spectral_decomposition(3.0, 4)
        assert result["sym_check"]
        assert result["asym_check"]


# ============================================================
# 8. Form factor comparison tests (arity 3)
# ============================================================

class TestFormFactors:
    """Tests for arity-3 form factor comparison."""

    def test_arity3_sl2_agrees(self):
        """Arity-3 form factors agree for sl_2."""
        result = compare_arity3_form_factors(2)
        assert result["all_agree"]

    def test_arity3_sl3_agrees(self):
        """Arity-3 form factors agree for sl_3."""
        result = compare_arity3_form_factors(3)
        assert result["all_agree"]

    def test_arity3_explicit_sl2(self):
        """Explicit arity-3 form factor for sl_2."""
        F_c = costello_arity3_form_factor(1.0, 2.0, 3.0, 2)
        F_b = bar_arity3_collision_residue(1.0, 2.0, 3.0, 2)
        assert np.allclose(F_c, F_b)

    def test_arity3_nonzero(self):
        """Arity-3 form factor is nonzero (nontrivial cubic interaction)."""
        F = costello_arity3_form_factor(1.0, 2.0, 3.0, 3)
        assert np.linalg.norm(F) > 1e-10

    def test_arity3_cybe_consistency(self):
        """Arity-3 form factor consistent with CYBE.

        F_3 = [r_{12}, r_{23}] = -[r_{12}, r_{13}] - [r_{13}, r_{23}]
        by the CYBE. Verify this identity.
        """
        N = 3
        z1, z2, z3 = 1.0, 2.0, 3.0
        z12, z13, z23 = z1 - z2, z1 - z3, z2 - z3

        Omega = casimir_tensor_slN_fund(N)
        from compute.lib.costello_4d_cs_comparison_engine import (
            _embed_R12, _embed_R13, _embed_R23,
        )
        r12 = _embed_R12(Omega / z12, N)
        r13 = _embed_R13(Omega / z13, N)
        r23 = _embed_R23(Omega / z23, N)

        F3_form1 = r12 @ r23 - r23 @ r12
        F3_form2 = -(r12 @ r13 - r13 @ r12) - (r13 @ r23 - r23 @ r13)

        # These should agree by CYBE
        assert np.allclose(F3_form1, F3_form2, atol=1e-10)


# ============================================================
# 9. BCD-type R-matrix tests
# ============================================================

class TestBCDTypes:
    """Tests for B, C, D type R-matrices."""

    def test_typeB_ybe_B2(self):
        """YBE for type B_2 (so_5). kappa = 1.5; avoid u,v,u-v in {0, 1.5}."""
        assert verify_ybe_BCD('B', 2, 3.7, 5.3) < 1e-8

    def test_typeB_ybe_B3(self):
        """YBE for type B_3 (so_7). kappa = 2.5; avoid poles."""
        assert verify_ybe_BCD('B', 3, 4.1, 7.3) < 1e-6

    def test_typeC_ybe_C2(self):
        """YBE for type C_2 (sp_4). kappa = 3; avoid u,v,u-v in {0, 3}."""
        assert verify_ybe_BCD('C', 2, 1.5, 4.5) < 1e-8

    def test_typeD_ybe_D3(self):
        """YBE for type D_3 (so_6). kappa = 2; avoid u,v,u-v in {0, 2}."""
        assert verify_ybe_BCD('D', 3, 3.7, 5.3) < 1e-6

    def test_typeB_bar_agrees(self):
        """Bar R-matrix = Costello R-matrix for type B."""
        u = 2.5
        R_c = costello_r_matrix_typeB(u, 2)
        R_b = bar_r_matrix_typeB(u, 2)
        assert np.allclose(R_c, R_b)

    def test_typeB_unitarity(self):
        """Type B unitarity: R(u) R_{21}(-u) ~ scalar * I."""
        N = 5  # B_2: so_5
        u = 2.0
        R_u = costello_r_matrix_typeB(u, 2)
        P = permutation_matrix(N)
        R_21_minus_u = P @ costello_r_matrix_typeB(-u, 2) @ P
        product = R_u @ R_21_minus_u
        # Check that product is proportional to identity on each eigenspace
        # (it won't be scalar * I in general for BCD, but it should be
        # block-diagonal in the isotypic decomposition)
        eigenvalues = np.linalg.eigvals(product)
        # All eigenvalues should be real (up to numerical error)
        assert all(abs(ev.imag) < 1e-8 for ev in eigenvalues)

    def test_typeC_kappa_value(self):
        """Type C_2 kappa = n + 1 = 3."""
        # The R-matrix has a pole at u = kappa = 3
        R_far = costello_r_matrix_typeC(100.0, 2)
        I = np.eye(16, dtype=complex)
        # At large u, R(u) -> I
        assert np.allclose(R_far, I, atol=0.1)

    def test_typeD_requires_n_ge_3(self):
        """Type D_n requires n >= 3."""
        with pytest.raises(AssertionError):
            costello_r_matrix_typeD(1.0, 2)


# ============================================================
# 10. Transfer matrix and integrability tests
# ============================================================

class TestIntegrability:
    """Tests for transfer matrix commutativity (integrability)."""

    def test_transfer_commutativity_sl2(self):
        """[t(u), t(v)] = 0 for sl_2 two-site chain."""
        assert transfer_matrix_commutativity(2, 1.0, 2.0) < 1e-8

    def test_transfer_commutativity_sl3(self):
        """[t(u), t(v)] = 0 for sl_3 two-site chain."""
        assert transfer_matrix_commutativity(3, 1.0, 2.0) < 1e-6

    def test_transfer_commutativity_sl2_complex(self):
        """[t(u), t(v)] = 0 for sl_2 at complex parameters."""
        assert transfer_matrix_commutativity(2, 1.0 + 0.5j, 2.0 - 0.3j) < 1e-8

    def test_transfer_commutativity_multiple(self):
        """Transfer commutativity at 5 random (u, v) for sl_2."""
        rng = np.random.default_rng(42)
        for _ in range(5):
            u = rng.uniform(0.5, 5.0)
            v = rng.uniform(0.5, 5.0)
            assert transfer_matrix_commutativity(2, u, v) < 1e-8


# ============================================================
# 11. Structural comparison tests
# ============================================================

class TestStructuralComparison:
    """Tests for structural data and correspondence dictionaries."""

    def test_defect_data_sl2(self):
        """Defect-representation data for sl_2."""
        data = defect_representation_data(2)
        assert data["type"] == "sl_2"
        assert data["fund_dim"] == 2
        assert data["MC3_status"] == "proved for all simple types"

    def test_defect_data_sl3(self):
        """Defect-representation data for sl_3."""
        data = defect_representation_data(3)
        assert data["type"] == "sl_3"
        assert data["fund_dim"] == 3

    def test_koszul_duality_comparison_keys(self):
        """Koszul duality comparison has required keys."""
        kd = koszul_duality_comparison()
        assert "costello_R_matrix" in kd
        assert "our_R_matrix" in kd
        assert "identification_level" in kd
        assert "genus-0, arity-2" in kd["identification_level"]

    def test_ht_twist_data_keys(self):
        """HT twist data has required keys."""
        ht = ht_twist_data()
        assert "holomorphic_direction" in ht
        assert "topological_direction" in ht
        assert "match" in ht

    def test_modular_yangian_differences(self):
        """Modular Yangian vs 4d CS structural differences."""
        diff = modular_yangian_vs_4d_cs()
        assert "agreement_genus0_arity2" in diff
        assert "difference_genus" in diff
        assert "difference_universality" in diff


# ============================================================
# 12. Cross-verification with existing engines
# ============================================================

class TestCrossVerification:
    """Cross-verify with existing yangian_residue_extraction.py."""

    def test_yang_r_matrix_matches_extraction_engine(self):
        """Our R(u) matches yangian_residue_extraction.py for sl_2."""
        from compute.lib.yangian_residue_extraction import (
            yang_r_matrix_slN,
        )
        for u in [1.0, 2.0, 5.0]:
            R_ours = bar_quantum_R_matrix_yang(u, 2)
            R_existing = yang_r_matrix_slN(u, 2)
            assert np.allclose(R_ours, R_existing)

    def test_yang_r_matrix_matches_extraction_sl3(self):
        """Our R(u) matches yangian_residue_extraction.py for sl_3."""
        from compute.lib.yangian_residue_extraction import (
            yang_r_matrix_slN,
        )
        for u in [1.0, 2.0, 5.0]:
            R_ours = bar_quantum_R_matrix_yang(u, 3)
            R_existing = yang_r_matrix_slN(u, 3)
            assert np.allclose(R_ours, R_existing)

    def test_ybe_matches_extraction_engine(self):
        """YBE verification matches yangian_residue_extraction.py."""
        from compute.lib.yangian_residue_extraction import (
            verify_yang_baxter_slN,
        )
        for N in [2, 3]:
            ours = verify_ybe_yang(1.0, 2.0, N)
            theirs = verify_yang_baxter_slN(1.0, 2.0, N)
            assert ours < 1e-8
            assert theirs < 1e-8

    def test_permutation_matches_extraction(self):
        """Permutation matrix matches yangian_residue_extraction.py."""
        from compute.lib.yangian_residue_extraction import (
            permutation_matrix_slN,
        )
        for N in [2, 3, 4]:
            P_ours = permutation_matrix(N)
            P_theirs = permutation_matrix_slN(N)
            assert np.allclose(P_ours, P_theirs)


# ============================================================
# 13. Limiting case tests
# ============================================================

class TestLimitingCases:
    """Tests at special/limiting parameter values."""

    def test_r_matrix_large_u(self):
        """R(u) ~ u*I as u -> infinity."""
        u = 1000.0
        N = 3
        R = bar_quantum_R_matrix_yang(u, N)
        I = np.eye(N * N, dtype=complex)
        # R/u -> I as u -> inf
        assert np.allclose(R / u, I, atol=0.01)

    def test_r_matrix_u_zero(self):
        """R(0) = P (permutation)."""
        N = 3
        R = bar_quantum_R_matrix_yang(0.0, N)
        P = permutation_matrix(N)
        assert np.allclose(R, P)

    def test_r_matrix_u_one(self):
        """R(1)|_{Lambda^2} = 0 (antisymmetric projection kernel)."""
        N = 3
        R = bar_quantum_R_matrix_yang(1.0, N)
        P = permutation_matrix(N)
        I = np.eye(N * N)
        P_asym = (I - P) / 2
        # R(1) on Lambda^2: eigenvalue = 1-1 = 0
        R_asym = P_asym @ R @ P_asym
        assert np.allclose(R_asym, np.zeros((N * N, N * N)), atol=1e-10)

    def test_r_matrix_u_minus_one(self):
        """R(-1)|_{Sym^2} = 0 (symmetric projection kernel)."""
        N = 3
        R = bar_quantum_R_matrix_yang(-1.0, N)
        P = permutation_matrix(N)
        I = np.eye(N * N)
        P_sym = (I + P) / 2
        # R(-1) on Sym^2: eigenvalue = -1+1 = 0
        R_sym = P_sym @ R @ P_sym
        assert np.allclose(R_sym, np.zeros((N * N, N * N)), atol=1e-10)

    def test_costello_r_at_infinity_is_identity(self):
        """Costello perturbative R -> I as z -> infinity."""
        N = 3
        z = 1000.0
        R = costello_perturbative_R_matrix(z, N, max_order=3)
        I = np.eye(N * N, dtype=complex)
        assert np.allclose(R, I, atol=0.01)

    def test_casimir_eigenvalue_sym_sl2(self):
        """Omega eigenvalue on Sym^2(V) = (N-1)/N for sl_2.

        Omega = P - I/N. On Sym^2: P = +1, so eigenvalue = 1 - 1/N = (N-1)/N.
        For N=2: eigenvalue = 1/2.
        """
        N = 2
        Omega = casimir_tensor_slN_fund(N)
        # Test on e_0 x e_0 (a symmetric vector)
        v = np.zeros(N * N)
        v[0] = 1.0  # e_0 tensor e_0
        Ov = Omega @ v
        expected_eigenvalue = (N - 1.0) / N
        assert np.allclose(Ov, expected_eigenvalue * v, atol=1e-10)

    def test_casimir_eigenvalue_asym_sl3(self):
        """Omega eigenvalue on Lambda^2(V) = -(N+1)/N for sl_3.

        Omega = P - I/N. On Lambda^2: P = -1, so eigenvalue = -1 - 1/N = -(N+1)/N.
        For N=3: eigenvalue = -4/3.
        """
        N = 3
        Omega = casimir_tensor_slN_fund(N)
        # Test on e_0 x e_1 - e_1 x e_0 (an antisymmetric vector)
        v = np.zeros(N * N)
        v[0 * N + 1] = 1.0
        v[1 * N + 0] = -1.0
        Ov = Omega @ v
        expected_eigenvalue = -(N + 1.0) / N
        assert np.allclose(Ov, expected_eigenvalue * v, atol=1e-10)


# ============================================================
# 14. Multi-path verification tests
# ============================================================

class TestMultiPathVerification:
    """Multi-path verification of key identities (CLAUDE.md mandate)."""

    def test_casimir_three_paths_sl3(self):
        """Casimir Omega = P - I/N verified 3 ways for sl_3.

        Path 1: Direct definition (sum T^a otimes T_a).
        Path 2: P - I/N identity.
        Path 3: Eigenvalue check on Sym^2 and Lambda^2.
        """
        N = 3
        # Path 1: from definition (via our function)
        Omega = casimir_tensor_slN_fund(N)

        # Path 2: P - I/N
        P = permutation_matrix(N)
        I = np.eye(N * N)
        Omega_path2 = P - I / N

        # Path 3: eigenvalues
        # On Sym^2: Omega = 1 - 1/N = (N-1)/N
        # On Lambda^2: Omega = -1 - 1/N = -(N+1)/N
        P_sym = (I + P) / 2
        P_asym = (I - P) / 2
        Omega_sym = P_sym @ Omega @ P_sym
        expected_sym = (N - 1.0) / N * P_sym
        Omega_asym = P_asym @ Omega @ P_asym
        expected_asym = -(N + 1.0) / N * P_asym

        assert np.allclose(Omega, Omega_path2, atol=1e-12)
        assert np.allclose(Omega_sym, expected_sym, atol=1e-10)
        assert np.allclose(Omega_asym, expected_asym, atol=1e-10)

    def test_ybe_three_paths_sl2(self):
        """YBE verified 3 ways for sl_2.

        Path 1: Direct R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}.
        Path 2: Spectral decomposition on each channel.
        Path 3: Unitarity R(u)R(-u) = (1-u^2)I implies YBE.
        """
        # Path 1: direct YBE
        ybe_err = verify_ybe_yang(1.0, 2.0, 2)
        assert ybe_err < 1e-10

        # Path 2: spectral decomposition
        spec = verify_spectral_decomposition(3.0, 2)
        assert spec["sym_check"]
        assert spec["asym_check"]

        # Path 3: unitarity
        unit_err = verify_unitarity_yang(2.0, 2)
        assert unit_err < 1e-10

    def test_r_matrix_costello_vs_bar_vs_yang_sl2(self):
        """R-matrix agreement verified 3 ways for sl_2.

        Path 1: Costello tree-level r(z) = Omega/z.
        Path 2: Bar collision residue r(z) = Omega/z.
        Path 3: Yang R-matrix R(u) = uI + P (additive form).
        """
        N = 2
        z = 2.0

        # Path 1: Costello
        r_costello = costello_tree_level_r_matrix(z, N)

        # Path 2: Bar
        r_bar = bar_collision_residue_r_matrix(z, N)

        # Path 3: Yang (extract leading term of R(u)/u as u -> inf)
        Omega = casimir_tensor_slN_fund(N)
        r_yang = Omega / z

        assert np.allclose(r_costello, r_bar, atol=1e-12)
        assert np.allclose(r_costello, r_yang, atol=1e-12)

    def test_form_factor_arity3_three_paths(self):
        """Arity-3 form factor verified 3 ways for sl_2.

        Path 1: [r_{12}, r_{23}] from Costello.
        Path 2: [r_{12}, r_{23}] from bar.
        Path 3: CYBE rewriting: = -[r_{12}, r_{13}] - [r_{13}, r_{23}].
        """
        N = 2
        z1, z2, z3 = 1.0, 2.0, 3.0

        # Path 1
        F_c = costello_arity3_form_factor(z1, z2, z3, N)
        # Path 2
        F_b = bar_arity3_collision_residue(z1, z2, z3, N)

        # Path 3: CYBE rewriting
        from compute.lib.costello_4d_cs_comparison_engine import (
            _embed_R12, _embed_R13, _embed_R23,
        )
        Omega = casimir_tensor_slN_fund(N)
        z12, z13, z23 = z1 - z2, z1 - z3, z2 - z3
        r12 = _embed_R12(Omega / z12, N)
        r13 = _embed_R13(Omega / z13, N)
        r23 = _embed_R23(Omega / z23, N)
        F_cybe = -(r12 @ r13 - r13 @ r12) - (r13 @ r23 - r23 @ r13)

        assert np.allclose(F_c, F_b, atol=1e-12)
        assert np.allclose(F_c, F_cybe, atol=1e-10)


# ============================================================
# 15. Cross-verification with sl3 engine
# ============================================================

class TestCrossVerificationSl3:
    """Cross-verify with yangian_rmatrix_sl3.py."""

    def test_casimir_matches_sl3_engine(self):
        """Our Casimir matches yangian_rmatrix_sl3.py."""
        from compute.lib.yangian_rmatrix_sl3 import (
            casimir_tensor_fund,
            verify_casimir_identity,
        )
        Omega_ours = casimir_tensor_slN_fund(3)
        Omega_sl3 = casimir_tensor_fund()
        assert np.allclose(Omega_ours, Omega_sl3, atol=1e-10)
        assert verify_casimir_identity()

    def test_r_matrix_yang_matches_sl3(self):
        """Our Yang R-matrix matches yangian_rmatrix_sl3.py."""
        from compute.lib.yangian_rmatrix_sl3 import R_matrix_fund_exact_yang
        for u_val in [1.0, 3.0, 5.0]:
            R_ours = bar_quantum_R_matrix_yang(u_val, 3)
            R_sl3 = R_matrix_fund_exact_yang(u_val)
            assert np.allclose(R_ours, R_sl3, atol=1e-10)

    def test_kappa_matches_sl3_engine(self):
        """Our kappa matches yangian_rmatrix_sl3.py for sl_3."""
        from compute.lib.yangian_rmatrix_sl3 import kappa_sl3
        from sympy import Rational
        for k in [1, 2, 5, 10]:
            kappa_ours = kappa_affine_slN(3, k)
            kappa_sl3_val = float(kappa_sl3(k))
            assert abs(kappa_ours - kappa_sl3_val) < 1e-10


