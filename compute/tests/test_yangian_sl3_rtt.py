r"""Tests for RTT presentation of Y(sl_3) from the bar-cobar construction.

Verifies:
    1. RTT relation via Yang-Baxter equation (evaluation L-operators)
    2. RTT relation order-by-order extraction
    3. Quantum determinant: scalar property, explicit value, centrality
    4. Drinfeld generators: level-0 bracket, Serre relations, level-1/2 map
    5. Adjoint representation: 64x64 R-matrix, permutation eigenvalues
    6. Fusion rules: 3 x 3 = 6 + bar{3}, dimension checks
    7. KZ monodromy: large-kappa limit, eigenvalue ratios, q extraction
    8. Tensor product reducibility: rank drop at a1 - a2 = +-1
    9. Casimir formula: C_2 and dimension for all standard representations
    10. Bar-to-RTT connection: structural verification
    11. Level-k deformation: R-matrix independence, trigonometric limit
    12. Evaluation modules: Drinfeld polynomials, qdet values

Ground truth references:
    - yangian_rmatrix_sl3.py: fundamental R-matrix, Casimir, YBE
    - yangian_bar.py: bar complex structure
    - yangians.tex: RTT presentation, DK bridge
    - Chari-Pressley: quantum groups
    - Molev: Yangians and classical Lie algebras
"""

import pytest
import numpy as np
from sympy import Rational, Symbol

from compute.lib.yangian_sl3_rtt import (
    # Constants
    N, DIM_SL3, H_VEE_SL3,
    # RTT generators
    rtt_generators_symbolic,
    T_matrix_formal,
    rtt_relation_order,
    # RTT verification
    rtt_evaluation_L_operator,
    verify_rtt_from_ybe,
    extract_rtt_relation_11,
    verify_rtt_order_by_order,
    # Quantum determinant
    quantum_determinant_matrix,
    quantum_determinant_scalar,
    verify_qdet_centrality,
    verify_qdet_antisymmetrizer,
    quantum_determinant_explicit,
    verify_qdet_is_scalar,
    verify_qdet_value,
    # Drinfeld generators
    gauss_decomposition_level0,
    drinfeld_generators_level0,
    drinfeld_generators_level1,
    drinfeld_generators_level2,
    rtt_to_drinfeld_map_level1,
    rtt_to_drinfeld_map_level2,
    verify_drinfeld_level0_bracket,
    verify_drinfeld_serre_relations,
    # Adjoint
    adjoint_rep_matrices,
    adjoint_killing_form,
    adjoint_casimir_tensor,
    adjoint_R_matrix,
    adjoint_casimir_eigenvalues,
    verify_adjoint_permutation_eigenvalues,
    adjoint_permutation_matrix,
    adjoint_R_eigenvalues,
    # Fusion
    fusion_rules_fundamental,
    fusion_rules_fund_x_antifund,
    verify_fusion_dimensions,
    verify_R_eigenvalue_on_fusion,
    # KZ
    kz_monodromy_matrix,
    verify_kz_monodromy_yang_limit,
    kz_monodromy_to_q,
    verify_monodromy_eigenvalue_ratio,
    # Evaluation modules
    evaluation_module_drinfeld_polynomial,
    tensor_product_evaluation,
    verify_tensor_product_reducibility,
    # Casimir formula
    casimir_eigenvalue_sl3,
    dimension_sl3,
    # Bar connection
    bar_to_rtt_connection,
    # Level-k
    R_matrix_level_k,
    kz_R_matrix_from_monodromy,
    # Full verification
    full_rtt_verification,
)

from compute.lib.yangian_rmatrix_sl3 import (
    kappa_sl3,
    R_matrix_fund_exact_yang,
    permutation_matrix_3,
    casimir_tensor_fund,
    fund_rep_matrices,
    casimir_scalar_fund,
)

from compute.lib.sl3_bar import sl3_structure_constants


# ============================================================
# 1. RTT relation from Yang-Baxter equation
# ============================================================

class TestRTTFromYBE:
    """RTT relation = YBE with relabeled spaces."""

    def test_rtt_real_parameters(self):
        """RTT at real spectral parameters (10, 7)."""
        assert verify_rtt_from_ybe(10.0, 7.0) < 1e-10

    def test_rtt_real_parameters_2(self):
        """RTT at real spectral parameters (3.5, 1.2)."""
        assert verify_rtt_from_ybe(3.5, 1.2) < 1e-10

    def test_rtt_complex_parameters(self):
        """RTT at complex spectral parameters."""
        assert verify_rtt_from_ybe(2.0 + 1.0j, 5.0 - 0.5j) < 1e-10

    def test_rtt_close_parameters(self):
        """RTT when u and v are close (but not equal)."""
        assert verify_rtt_from_ybe(1.0, 1.1) < 1e-10

    def test_rtt_large_parameters(self):
        """RTT at large spectral parameters."""
        assert verify_rtt_from_ybe(100.0, 200.0) < 1e-8

    def test_rtt_negative_parameters(self):
        """RTT with negative spectral parameters."""
        assert verify_rtt_from_ybe(-3.0, -7.0) < 1e-10

    def test_rtt_with_evaluation_point(self):
        """RTT at nonzero evaluation point a = 2."""
        assert verify_rtt_from_ybe(10.0, 7.0, a=2.0) < 1e-10

    def test_rtt_evaluation_point_complex(self):
        """RTT at complex evaluation point."""
        assert verify_rtt_from_ybe(5.0, 3.0, a=1.0 + 0.5j) < 1e-10

    def test_rtt_is_27x27_matrix_equation(self):
        """RTT acts on V^{otimes 3} = C^27 (729 scalar equations)."""
        N_val = 3
        assert N_val ** 3 == 27
        assert verify_rtt_from_ybe(4.0, 2.0) < 1e-10


# ============================================================
# 2. RTT relation order-by-order
# ============================================================

class TestRTTOrderByOrder:
    """RTT relation expanded in powers of 1/u and 1/v."""

    def test_order_00_description(self):
        """Order (0,0) is trivial."""
        desc = rtt_relation_order(0, 0)
        assert "Trivial" in desc

    def test_order_10_description(self):
        """Order (1,0): T^(1) commutes with R in first factor."""
        desc = rtt_relation_order(1, 0)
        assert "commutes" in desc.lower()

    def test_order_11_description(self):
        """Order (1,1): key quadratic relation."""
        desc = rtt_relation_order(1, 1)
        assert "quadratic" in desc.lower() or "defining" in desc.lower()

    def test_order_11_trivial_at_a0(self):
        """At evaluation a=0, the (1,1) relation is trivially satisfied."""
        result = extract_rtt_relation_11(a=0.0)
        assert np.max(np.abs(result)) < 1e-14

    def test_order_11_trivial_at_a_nonzero(self):
        """At evaluation a!=0, T^(1) = aI so [T_1,T_2] = 0 = RHS."""
        result = extract_rtt_relation_11(a=3.0)
        assert np.max(np.abs(result)) < 1e-14

    def test_verify_order_by_order_all_pass(self):
        """All order-by-order checks pass at generic parameters."""
        results = verify_rtt_order_by_order(u_val=10.0, v_val=7.0)
        for key, norm in results.items():
            assert norm < 1e-10, f"Failed at {key}: norm = {norm}"


# ============================================================
# 3. Quantum determinant
# ============================================================

class TestQuantumDeterminant:
    """Quantum determinant for Y(sl_3)."""

    def test_qdet_is_scalar_u5(self):
        """qdet T(5) is proportional to I_3."""
        assert verify_qdet_is_scalar(5.0) < 1e-10

    def test_qdet_is_scalar_u10(self):
        """qdet T(10) is proportional to I_3."""
        assert verify_qdet_is_scalar(10.0) < 1e-10

    def test_qdet_is_scalar_complex(self):
        """qdet at complex u is still scalar."""
        assert verify_qdet_is_scalar(3.0 + 2.0j) < 1e-10

    def test_qdet_value_u5_a0(self):
        """qdet T(5)|_{V(0)} = (5+1)(5-1)(5-2) = 6*4*3 = 72."""
        expected = 6 * 4 * 3
        qdet = quantum_determinant_explicit(5.0, 0.0)
        assert abs(qdet[0, 0].real - expected) < 1e-10

    def test_qdet_value_u3_a1(self):
        """qdet T(3)|_{V(1)} = (3-1+1)(3-1-1)(3-1-2) = 3*1*0 = 0."""
        expected = 3 * 1 * 0
        qdet = quantum_determinant_explicit(3.0, 1.0)
        assert abs(qdet[0, 0].real - expected) < 1e-10

    def test_qdet_value_formula(self):
        """Verify qdet matches (u-a+1)(u-a-1)(u-a-2) for several (u, a)."""
        test_cases = [
            (5.0, 0.0),
            (10.0, 0.0),
            (4.0, 1.0),
            (7.0, 2.0),
            (3.0 + 1.0j, 0.0),
        ]
        for u, a in test_cases:
            assert verify_qdet_value(u, a) < 1e-10, f"Failed at u={u}, a={a}"

    def test_qdet_zero_at_u_a_minus_1(self):
        """qdet vanishes at u = a - 1 (first root)."""
        a = 2.0
        u = a - 1  # = 1
        val = quantum_determinant_scalar(u, a)
        assert abs(val) < 1e-14

    def test_qdet_zero_at_u_a_plus_1(self):
        """qdet vanishes at u = a + 1 (second root)."""
        a = 2.0
        u = a + 1  # = 3
        val = quantum_determinant_scalar(u, a)
        assert abs(val) < 1e-14

    def test_qdet_zero_at_u_a_plus_2(self):
        """qdet vanishes at u = a + 2 (third root)."""
        a = 2.0
        u = a + 2  # = 4
        val = quantum_determinant_scalar(u, a)
        assert abs(val) < 1e-14

    def test_qdet_antisymmetrizer(self):
        """qdet via antisymmetrizer check is consistent."""
        assert verify_qdet_antisymmetrizer(5.0) < 1e-10

    def test_qdet_centrality(self):
        """[qdet(u), L(v)] = 0 (centrality in evaluation representation)."""
        assert verify_qdet_centrality(5.0, 3.0) < 1e-10

    def test_qdet_centrality_complex(self):
        """Centrality at complex spectral parameters."""
        assert verify_qdet_centrality(5.0 + 1.0j, 3.0 - 0.5j) < 1e-10

    def test_qdet_matrix_matches_explicit(self):
        """quantum_determinant_matrix matches quantum_determinant_explicit."""
        u = 7.0
        mat = quantum_determinant_matrix(u)
        explicit = quantum_determinant_explicit(u, 0.0)
        assert np.allclose(mat, explicit, atol=1e-10)


# ============================================================
# 4. Drinfeld generators
# ============================================================

class TestDrinfeldGenerators:
    """Drinfeld presentation of Y(sl_3)."""

    def test_level0_bracket_sl3(self):
        """Level-0 Drinfeld generators satisfy [h_i, e_j] = A_{ij} e_j."""
        assert verify_drinfeld_level0_bracket() < 1e-14

    def test_serre_relations(self):
        """Serre relations [e_i, [e_i, e_j]] = 0 for i != j."""
        assert verify_drinfeld_serre_relations() < 1e-14

    def test_level0_traceless(self):
        """All level-0 generators are traceless."""
        gens = drinfeld_generators_level0()
        for name, M in gens.items():
            assert abs(np.trace(M)) < 1e-14, f"{name} not traceless"

    def test_level0_h_diagonal(self):
        """h_1, h_2 are diagonal matrices."""
        gens = drinfeld_generators_level0()
        for name in ["h1", "h2"]:
            M = gens[name]
            off_diag = M - np.diag(np.diag(M))
            assert np.max(np.abs(off_diag)) < 1e-14, f"{name} not diagonal"

    def test_level0_e_strictly_upper(self):
        """e_1, e_2 are strictly upper triangular."""
        gens = drinfeld_generators_level0()
        for name in ["e1", "e2"]:
            M = gens[name]
            # Check lower triangle is zero
            for i in range(N):
                for j in range(i + 1):
                    assert abs(M[i, j]) < 1e-14, f"{name}[{i},{j}] nonzero"

    def test_level0_f_strictly_lower(self):
        """f_1, f_2 are strictly lower triangular."""
        gens = drinfeld_generators_level0()
        for name in ["f1", "f2"]:
            M = gens[name]
            for i in range(N):
                for j in range(i, N):
                    assert abs(M[i, j]) < 1e-14, f"{name}[{i},{j}] nonzero"

    def test_level1_proportional(self):
        """Level-1 generators at evaluation a are a * level-0."""
        a = 3.0
        level0 = drinfeld_generators_level0()
        level1 = drinfeld_generators_level1(a)
        for name in level0:
            assert np.allclose(level1[name], a * level0[name], atol=1e-14)

    def test_level2_proportional(self):
        """Level-2 generators at evaluation a are a^2 * level-0."""
        a = 2.5
        level0 = drinfeld_generators_level0()
        level2 = drinfeld_generators_level2(a)
        for name in level0:
            assert np.allclose(level2[name], a ** 2 * level0[name], atol=1e-14)

    def test_gauss_level0_trivial(self):
        """Gauss decomposition at level 0: F = H = E = I."""
        gauss = gauss_decomposition_level0()
        I3 = np.eye(N, dtype=complex)
        for key in ["F", "H", "E"]:
            assert np.allclose(gauss[key], I3, atol=1e-14)

    def test_rtt_to_drinfeld_map_exists_level1(self):
        """RTT-to-Drinfeld map at level 1 has correct structure."""
        mapping = rtt_to_drinfeld_map_level1()
        assert "e1^(1)" in mapping
        assert "f2^(1)" in mapping
        assert "h1^(1)" in mapping

    def test_rtt_to_drinfeld_map_exists_level2(self):
        """RTT-to-Drinfeld map at level 2 has correct structure."""
        mapping = rtt_to_drinfeld_map_level2()
        assert "e1^(2)" in mapping
        assert "h1^(2)" in mapping

    def test_h1_eigenvalues(self):
        """h_1 has eigenvalues 1, -1, 0 (Cartan weights of fundamental)."""
        gens = drinfeld_generators_level0()
        evals = sorted(np.linalg.eigvalsh(gens["h1"].real))
        assert np.allclose(evals, [-1, 0, 1], atol=1e-14)

    def test_h2_eigenvalues(self):
        """h_2 has eigenvalues 0, 1, -1 (Cartan weights of fundamental)."""
        gens = drinfeld_generators_level0()
        evals = sorted(np.linalg.eigvalsh(gens["h2"].real))
        assert np.allclose(evals, [-1, 0, 1], atol=1e-14)


# ============================================================
# 5. Adjoint representation
# ============================================================

class TestAdjointRepresentation:
    """Adjoint representation and 64x64 R-matrix."""

    def test_adjoint_matrices_8x8(self):
        """8 adjoint matrices, each 8x8."""
        mats = adjoint_rep_matrices()
        assert len(mats) == DIM_SL3
        for M in mats:
            assert M.shape == (DIM_SL3, DIM_SL3)

    def test_adjoint_traceless(self):
        """All ad(T_a) are traceless (sl_3 is unimodular)."""
        mats = adjoint_rep_matrices()
        for a in range(DIM_SL3):
            assert abs(np.trace(mats[a])) < 1e-12

    def test_adjoint_bracket(self):
        """[ad(T_a), ad(T_b)] = ad([T_a, T_b]) (Jacobi identity)."""
        mats = adjoint_rep_matrices()
        f = sl3_structure_constants()
        max_err = 0.0
        for a in range(DIM_SL3):
            for b in range(DIM_SL3):
                comm = mats[a] @ mats[b] - mats[b] @ mats[a]
                expected = np.zeros((DIM_SL3, DIM_SL3), dtype=complex)
                if (a, b) in f:
                    for c, coeff in f[(a, b)].items():
                        expected += float(coeff) * mats[c]
                max_err = max(max_err, float(np.linalg.norm(comm - expected)))
        assert max_err < 1e-12

    def test_adjoint_killing_form_symmetric(self):
        """Adjoint Killing form is symmetric."""
        K = adjoint_killing_form()
        assert np.allclose(K, K.T, atol=1e-12)

    def test_adjoint_killing_proportional_to_fund(self):
        """K^{adj}_{ab} = 2h^vee * g^{fund}_{ab} = 6 * tr_{fund}(T_a T_b).

        For sl_3 with h^vee = 3: K = 6 * g_fund.
        """
        from compute.lib.yangian_rmatrix_sl3 import killing_form_matrix as kf_fund
        K_adj = adjoint_killing_form()
        K_fund = kf_fund()
        ratio = 2 * H_VEE_SL3  # = 6
        assert np.allclose(K_adj, ratio * K_fund, atol=1e-10)

    def test_adjoint_permutation_eigenvalues(self):
        """P^{adj} has eigenvalues +1 (x36) and -1 (x28)."""
        assert verify_adjoint_permutation_eigenvalues() < 1e-10

    def test_adjoint_permutation_squared_identity(self):
        """(P^{adj})^2 = I_{64}."""
        P = adjoint_permutation_matrix()
        assert np.allclose(P @ P, np.eye(64), atol=1e-14)

    def test_adjoint_R_matrix_shape(self):
        """R^{adj}(u) is 64x64."""
        R = adjoint_R_matrix(3.0)
        assert R.shape == (64, 64)

    def test_adjoint_decomposition_dimensions(self):
        """adj x adj = 1 + 8 + 8 + 10 + 10 + 27 (total 64)."""
        info = adjoint_casimir_eigenvalues()
        total = sum(v["dim"] for v in info.values())
        assert total == 64

    def test_adjoint_R_eigenvalues_structure(self):
        """R^{adj}(u) = u I + P^{adj} has two eigenvalue families."""
        info = adjoint_R_eigenvalues(3.0)
        assert info["Sym^2(adj)"]["dim"] == 36
        assert info["Lambda^2(adj)"]["dim"] == 28


# ============================================================
# 6. Fusion rules
# ============================================================

class TestFusionRules:
    """Fusion rules and MC3 verification."""

    def test_fund_x_fund_dimensions(self):
        """3 x 3 = 6 + bar{3} (9 = 6 + 3)."""
        assert verify_fusion_dimensions()

    def test_R_eigenvalue_decomposition_u2(self):
        """R(u) = (u+1) P_sym + (u-1) P_asym at u=2."""
        assert verify_R_eigenvalue_on_fusion(2.0) < 1e-10

    def test_R_eigenvalue_decomposition_u5(self):
        """R(u) decomposition at u=5."""
        assert verify_R_eigenvalue_on_fusion(5.0) < 1e-10

    def test_R_eigenvalue_decomposition_complex(self):
        """R(u) decomposition at complex u."""
        assert verify_R_eigenvalue_on_fusion(3.0 + 1.0j) < 1e-10

    def test_fusion_mc3_status(self):
        """MC3 status is proved."""
        info = fusion_rules_fundamental()
        assert "PROVED" in info["MC3_status"]

    def test_fund_x_antifund_dimensions(self):
        """3 x bar{3} = 1 + 8 (9 = 1 + 8)."""
        info = fusion_rules_fund_x_antifund()
        total = sum(v["dim"] for v in info["3 x bar{3}"].values())
        assert total == 9

    def test_sym_eigenvalue_positive(self):
        """R(u) eigenvalue on Sym^2 is u+1 (positive for u > 0)."""
        P = permutation_matrix_3().astype(complex)
        I9 = np.eye(9, dtype=complex)
        P_sym = (I9 + P) / 2
        u = 3.0
        R = R_matrix_fund_exact_yang(u)
        assert np.allclose(R @ P_sym, (u + 1) * P_sym, atol=1e-10)

    def test_asym_eigenvalue(self):
        """R(u) eigenvalue on Lambda^2 is u-1."""
        P = permutation_matrix_3().astype(complex)
        I9 = np.eye(9, dtype=complex)
        P_asym = (I9 - P) / 2
        u = 3.0
        R = R_matrix_fund_exact_yang(u)
        assert np.allclose(R @ P_asym, (u - 1) * P_asym, atol=1e-10)


# ============================================================
# 7. KZ monodromy
# ============================================================

class TestKZMonodromy:
    """Drinfeld-Kohno correspondence: KZ monodromy -> quantum group."""

    def test_monodromy_large_kappa(self):
        """Monodromy -> I as kappa -> infinity."""
        assert verify_kz_monodromy_yang_limit(1000.0) < 0.05

    def test_monodromy_eigenvalue_ratio_k1(self):
        """Monodromy eigenvalue ratio matches q^3 at k=1."""
        assert verify_monodromy_eigenvalue_ratio(1) < 1e-10

    def test_monodromy_eigenvalue_ratio_k2(self):
        """Monodromy eigenvalue ratio matches q^3 at k=2."""
        assert verify_monodromy_eigenvalue_ratio(2) < 1e-10

    def test_monodromy_eigenvalue_ratio_k5(self):
        """Monodromy eigenvalue ratio matches q^3 at k=5."""
        assert verify_monodromy_eigenvalue_ratio(5) < 1e-10

    def test_monodromy_eigenvalue_ratio_k10(self):
        """Monodromy eigenvalue ratio matches q^3 at k=10."""
        assert verify_monodromy_eigenvalue_ratio(10) < 1e-10

    def test_monodromy_matrix_shape(self):
        """KZ monodromy is 9x9."""
        M = kz_monodromy_matrix(float(kappa_sl3(1)))
        assert M.shape == (9, 9)

    def test_monodromy_unitary(self):
        """KZ monodromy is unitary (preserves inner product)."""
        M = kz_monodromy_matrix(float(kappa_sl3(1)))
        assert np.allclose(M @ M.conj().T, np.eye(9, dtype=complex), atol=1e-10)

    def test_q_at_k1(self):
        """q = exp(pi i / 4) at k = 1 (since k + h^vee = 4)."""
        kappa_val = float(kappa_sl3(1))
        q = kz_monodromy_to_q(kappa_val)
        expected = np.exp(1j * np.pi / 4)
        assert abs(q - expected) < 1e-10

    def test_q_at_k3(self):
        """q = exp(pi i / 6) at k = 3 (since k + h^vee = 6)."""
        kappa_val = float(kappa_sl3(3))
        q = kz_monodromy_to_q(kappa_val)
        expected = np.exp(1j * np.pi / 6)
        assert abs(q - expected) < 1e-10

    def test_trigonometric_R_matrix_unitary(self):
        """Trigonometric R-matrix from KZ is unitary."""
        R_trig = kz_R_matrix_from_monodromy(k=2)
        assert np.allclose(R_trig @ R_trig.conj().T, np.eye(9, dtype=complex), atol=1e-10)


# ============================================================
# 8. Tensor product and evaluation modules
# ============================================================

class TestTensorProducts:
    """Tensor product structure and evaluation modules."""

    def test_reducible_at_diff_1(self):
        """V(1) x V(0): R(1) has rank 6 (Lambda^2 eigenvalue = 0)."""
        result = verify_tensor_product_reducibility(1.0, 0.0)
        assert result["R_rank"] == 6
        assert result["reducible"] == True

    def test_reducible_at_diff_minus_1(self):
        """V(0) x V(1): R(-1) has rank 3 (Sym^2 eigenvalue = 0)."""
        result = verify_tensor_product_reducibility(0.0, 1.0)
        # R(-1) = -I + P, which has eigenvalue 0 on Sym^2 (dim 6) and -2 on Lambda^2 (dim 3)
        # Rank = 3 (only Lambda^2 survives)
        assert result["R_rank"] == 3
        assert result["reducible"] == True

    def test_irreducible_generic(self):
        """V(3) x V(0) is irreducible (a1 - a2 = 3, generic)."""
        result = verify_tensor_product_reducibility(3.0, 0.0)
        assert result["R_rank"] == 9
        assert result["reducible"] == False

    def test_irreducible_irrational(self):
        """V(pi) x V(0) is irreducible (irrational difference)."""
        result = verify_tensor_product_reducibility(np.pi, 0.0)
        assert result["R_rank"] == 9
        assert result["reducible"] == False

    def test_drinfeld_polynomial_fundamental(self):
        """Drinfeld polynomial for V(a) has single root at a."""
        roots = evaluation_module_drinfeld_polynomial(3.5)
        assert len(roots) == 1
        assert abs(roots[0] - 3.5) < 1e-14

    def test_tensor_product_description(self):
        """Tensor product description is consistent."""
        tp = tensor_product_evaluation(1.0, 0.0)
        assert tp["type"] == "reducible (a1 - a2 = 1)"
        assert len(tp["components"]) == 2


# ============================================================
# 9. Casimir formula and dimensions
# ============================================================

class TestCasimirFormula:
    """Casimir eigenvalue formula for sl_3 representations."""

    def test_C2_fundamental(self):
        """C_2(1,0) = 8/3 (trace normalization)."""
        assert casimir_eigenvalue_sl3(1, 0) == Rational(8, 3)

    def test_C2_antifundamental(self):
        """C_2(0,1) = 8/3."""
        assert casimir_eigenvalue_sl3(0, 1) == Rational(8, 3)

    def test_C2_adjoint(self):
        """C_2(1,1) = 6."""
        assert casimir_eigenvalue_sl3(1, 1) == Rational(6)

    def test_C2_symmetric_square(self):
        """C_2(2,0) = 20/3."""
        assert casimir_eigenvalue_sl3(2, 0) == Rational(20, 3)

    def test_C2_30(self):
        """C_2(3,0) = 12."""
        assert casimir_eigenvalue_sl3(3, 0) == Rational(12)

    def test_C2_03(self):
        """C_2(0,3) = 12."""
        assert casimir_eigenvalue_sl3(0, 3) == Rational(12)

    def test_C2_22(self):
        """C_2(2,2) = 16."""
        assert casimir_eigenvalue_sl3(2, 2) == Rational(16)

    def test_C2_trivial(self):
        """C_2(0,0) = 0."""
        assert casimir_eigenvalue_sl3(0, 0) == Rational(0)

    def test_dim_fundamental(self):
        """dim(1,0) = 3."""
        assert dimension_sl3(1, 0) == 3

    def test_dim_antifundamental(self):
        """dim(0,1) = 3."""
        assert dimension_sl3(0, 1) == 3

    def test_dim_adjoint(self):
        """dim(1,1) = 8."""
        assert dimension_sl3(1, 1) == 8

    def test_dim_symmetric_square(self):
        """dim(2,0) = 6."""
        assert dimension_sl3(2, 0) == 6

    def test_dim_10(self):
        """dim(3,0) = 10."""
        assert dimension_sl3(3, 0) == 10

    def test_dim_27(self):
        """dim(2,2) = 27."""
        assert dimension_sl3(2, 2) == 27

    def test_dim_trivial(self):
        """dim(0,0) = 1."""
        assert dimension_sl3(0, 0) == 1


# ============================================================
# 10. Bar-to-RTT structural connection
# ============================================================

class TestBarToRTT:
    """Structural connection from bar complex to RTT presentation."""

    def test_connection_has_all_steps(self):
        """Bar-to-RTT connection has 6 steps."""
        conn = bar_to_rtt_connection()
        assert len(conn) == 6

    def test_step1_collision_residue(self):
        """Step 1: collision residue gives r-matrix."""
        conn = bar_to_rtt_connection()
        assert "collision" in conn["step_1"].lower() or "residue" in conn["step_1"].lower()

    def test_step4_d_squared(self):
        """Step 4: YBE comes from d^2 = 0."""
        conn = bar_to_rtt_connection()
        assert "d^2" in conn["step_4"] or "YBE" in conn["step_4"]

    def test_step6_mc3(self):
        """Step 6: MC3 gives categorical equivalence."""
        conn = bar_to_rtt_connection()
        assert "MC3" in conn["step_6"]


# ============================================================
# 11. Level-k deformation
# ============================================================

class TestLevelKDeformation:
    """Level dependence and trigonometric limit."""

    def test_rational_R_independent_of_k(self):
        """R(u) = uI + P does not depend on level k."""
        R_k1 = R_matrix_level_k(3.0, 1)
        R_k5 = R_matrix_level_k(3.0, 5)
        R_k100 = R_matrix_level_k(3.0, 100)
        assert np.allclose(R_k1, R_k5, atol=1e-14)
        assert np.allclose(R_k1, R_k100, atol=1e-14)

    def test_trigonometric_R_at_k1(self):
        """Trigonometric R-matrix at k=1 is well-defined."""
        R_trig = kz_R_matrix_from_monodromy(k=1)
        assert R_trig.shape == (9, 9)
        # Should not be proportional to identity (nontrivial q)
        assert not np.allclose(R_trig, R_trig[0, 0] * np.eye(9, dtype=complex), atol=0.1)

    def test_trigonometric_R_eigenvalues(self):
        """Trigonometric R-matrix has eigenvalues q (x6) and -q^{-1} (x3)."""
        k = 2
        kappa_val = float(kappa_sl3(k))
        q = kz_monodromy_to_q(kappa_val)
        R_trig = kz_R_matrix_from_monodromy(k)
        evals = np.sort(np.linalg.eigvals(R_trig))

        # 6 eigenvalues at q, 3 at -1/q
        expected = sorted(list([q] * 6 + [-1.0 / q] * 3), key=lambda x: x.real)
        evals_sorted = sorted(evals, key=lambda x: x.real)
        for e, exp in zip(evals_sorted, expected):
            assert abs(e - exp) < 1e-10

    def test_kappa_at_critical_level(self):
        """kappa = 0 at the critical level k = -h^vee = -3."""
        assert kappa_sl3(-3) == 0


# ============================================================
# 12. RTT generators symbolic
# ============================================================

class TestRTTGeneratorsSymbolic:
    """Symbolic RTT generating matrices."""

    def test_T0_is_identity(self):
        """T^{(0)} = I_3."""
        from sympy import eye as sym_eye
        gens = rtt_generators_symbolic(2)
        assert gens[0] == sym_eye(N)

    def test_T1_has_9_symbols(self):
        """T^{(1)} has 9 independent symbolic entries."""
        gens = rtt_generators_symbolic(2)
        T1 = gens[1]
        # Count distinct symbols
        symbols_set = set()
        for i in range(N):
            for j in range(N):
                symbols_set.add(T1[i, j])
        assert len(symbols_set) == 9

    def test_T2_has_9_symbols(self):
        """T^{(2)} has 9 independent symbolic entries."""
        gens = rtt_generators_symbolic(2)
        T2 = gens[2]
        symbols_set = set()
        for i in range(N):
            for j in range(N):
                symbols_set.add(T2[i, j])
        assert len(symbols_set) == 9

    def test_T_formal_matrix_shape(self):
        """T(u) is a 3x3 matrix."""
        u = Symbol('u')
        T = T_matrix_formal(u, max_level=2)
        assert T.shape == (N, N)


# ============================================================
# 13. Cross-checks with existing module
# ============================================================

class TestCrossChecks:
    """Cross-checks with yangian_rmatrix_sl3.py."""

    def test_R_matrix_consistency(self):
        """R(u) from RTT module matches yangian_rmatrix_sl3."""
        u = 4.5
        R_rtt = R_matrix_level_k(u, k=1)
        R_existing = R_matrix_fund_exact_yang(u)
        assert np.allclose(R_rtt, R_existing, atol=1e-14)

    def test_casimir_consistency(self):
        """C_2(fund) from formula matches numerical computation.

        casimir_scalar_fund() computes sum_a T^a T_a on V = C^3,
        which is the Casimir C_2(fund) = 8/3 in trace normalization.
        """
        c2_formula = float(casimir_eigenvalue_sl3(1, 0))
        c2_numeric = casimir_scalar_fund()
        assert abs(c2_formula - c2_numeric) < 1e-10

    def test_spectral_decomposition_consistency(self):
        """Spectral decomposition from both modules agree."""
        from compute.lib.yangian_rmatrix_sl3 import spectral_decomposition
        sd = spectral_decomposition()
        assert sd["sym_dim"] == 6
        assert sd["asym_dim"] == 3

    def test_omega_eigenvalue_consistency(self):
        """Omega eigenvalue on Sym from Casimir formula.

        Omega|_{V_lam in V_mu x V_nu} = (C_2(lam) - C_2(mu) - C_2(nu)) / 2
        where the factor 2 comes from C_2^{12} = C_2^1 + C_2^2 + 2 Omega.

        Omega|_{Sym^2} = (C_2(2,0) - 2*C_2(1,0)) / 2
        = (20/3 - 16/3) / 2 = (4/3)/2 = 2/3.
        """
        c2_sym = float(casimir_eigenvalue_sl3(2, 0))
        c2_fund = float(casimir_eigenvalue_sl3(1, 0))
        omega_sym = (c2_sym - 2 * c2_fund) / 2
        assert abs(omega_sym - 2.0 / 3.0) < 1e-10

    def test_omega_eigenvalue_asym_consistency(self):
        """Omega|_{Lambda^2} = (C_2(0,1) - 2*C_2(1,0)) / 2
        = (8/3 - 16/3) / 2 = (-8/3)/2 = -4/3.
        """
        c2_asym = float(casimir_eigenvalue_sl3(0, 1))
        c2_fund = float(casimir_eigenvalue_sl3(1, 0))
        omega_asym = (c2_asym - 2 * c2_fund) / 2
        assert abs(omega_asym - (-4.0 / 3.0)) < 1e-10


# ============================================================
# 14. Full integration test
# ============================================================

class TestFullIntegration:
    """Full RTT verification (all checks)."""

    def test_full_verification_all_pass(self):
        """All 23+ checks in full_rtt_verification pass."""
        results = full_rtt_verification()
        for name, ok in results.items():
            assert ok, f"Full verification failed: {name}"

    def test_full_verification_count(self):
        """Full verification includes at least 20 checks."""
        results = full_rtt_verification()
        assert len(results) >= 20


# ============================================================
# 15. L-operator and evaluation representation
# ============================================================

class TestLOperator:
    """L-operator for evaluation representations."""

    def test_L_operator_is_R_matrix(self):
        """L_a(u) = R(u - a)."""
        u, a = 5.0, 2.0
        L = rtt_evaluation_L_operator(u, a)
        R = R_matrix_fund_exact_yang(u - a)
        assert np.allclose(L, R, atol=1e-14)

    def test_L_operator_at_collision(self):
        """L_a(a) = R(0) = P (permutation at collision)."""
        a = 3.0
        L = rtt_evaluation_L_operator(a, a)
        P = permutation_matrix_3()
        assert np.allclose(L, P, atol=1e-14)

    def test_L_operator_shape(self):
        """L-operator is 9x9."""
        L = rtt_evaluation_L_operator(5.0, 0.0)
        assert L.shape == (9, 9)


# ============================================================
# Collection marker
# ============================================================

def test_import():
    """Module imports successfully."""
    from compute.lib.yangian_sl3_rtt import full_rtt_verification
    assert callable(full_rtt_verification)


def test_constants():
    """Module constants are correct."""
    assert N == 3
    assert DIM_SL3 == 8
    assert H_VEE_SL3 == 3
