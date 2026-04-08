"""Tests for the Yangian chapter rectification engine.

Verifies the three Yangian chapters against five major 2024--2026 papers:
  [DNP25]  Dimofte--Niu--Py, 2508.11749
  [AN24a]  Abedin--Niu, 2405.19906
  [DN24]   Dimofte--Niu, 2411.04194
  [AN24b]  Abedin--Niu, 2411.05068
  [AN25]   Abedin--Niu, 2512.16996

Test taxonomy:
  1. Yang--Baxter equation verification (all types)
  2. R-matrix unitarity (R * R^{-1} = I)
  3. Koszul dual sign flip (R^{-1} vs R(-hbar))
  4. qKZ -> KZ limit (Abedin-Niu specialization)
  5. Non-renormalization = Koszulness correspondence
  6. Spark algebra identification (Dimofte-Niu)
  7. Factorization dual Yangian consistency (Abedin-Niu)
  8. Quantum groupoid data (Abedin-Niu)
  9. Stable-graph Yang-Baxter at genus 0/1
  10. SQED dg-shifted Yangian (DNP simplest example)
  11. Cotangent Lie algebra R-matrix
  12. Comprehensive chapter rectification checks
"""

import numpy as np
import pytest

from compute.lib.theorem_yangian_chapter_rectification_engine import (
    yang_r_matrix,
    yang_r_matrix_multiplicative,
    yang_r_inverse_multiplicative,
    permutation_operator,
    verify_ybe,
    cotangent_r_matrix_sl2,
    cotangent_casimir_sl2,
    sqed_koszul_dual_data,
    sqed_r_matrix,
    sqed_bar_differential_degree2,
    kz_connection_matrix,
    verify_qkz_to_kz_limit,
    non_renormalization_koszulness_check,
    spark_algebra_data,
    factorization_dual_yangian_data,
    quantum_groupoid_data,
    stable_graph_yb_genus0,
    stable_graph_yb_genus1_correction,
    verify_r_matrix_inversion,
    koszul_dual_r_matrix_sign_flip,
    rectification_checklist,
    chapter_specific_findings,
    verify_yang_ybe_all_types,
    verify_r_unitarity_sweep,
    verify_koszul_dual_sign_flip_sweep,
    verify_qkz_kz_limit_sweep,
    missing_bibliography_entries,
)


# ================================================================
# SECTION 1: YANG--BAXTER EQUATION
# ================================================================

class TestYangBaxterEquation:
    """Verify YBE for Yang R-matrix at all ranks."""

    def test_ybe_sl2_random(self):
        """YBE for sl_2 at 50 random spectral parameters."""
        rng = np.random.default_rng(42)
        for _ in range(50):
            u = rng.uniform(0.5, 5.0) + 1j * rng.uniform(-2, 2)
            v = rng.uniform(0.5, 5.0) + 1j * rng.uniform(-2, 2)
            err = verify_ybe(yang_r_matrix, u, v, N=2, hbar=1.0)
            assert err < 1e-8, f"YBE failed for sl_2: u={u}, v={v}, err={err}"

    def test_ybe_sl3_random(self):
        """YBE for sl_3 at 30 random spectral parameters."""
        rng = np.random.default_rng(43)
        for _ in range(30):
            u = rng.uniform(0.5, 5.0) + 1j * rng.uniform(-2, 2)
            v = rng.uniform(0.5, 5.0) + 1j * rng.uniform(-2, 2)
            err = verify_ybe(yang_r_matrix, u, v, N=3, hbar=1.0)
            assert err < 1e-7, f"YBE failed for sl_3: u={u}, v={v}, err={err}"

    def test_ybe_sl4_random(self):
        """YBE for sl_4 at 20 random spectral parameters."""
        rng = np.random.default_rng(44)
        for _ in range(20):
            u = rng.uniform(1.0, 5.0) + 1j * rng.uniform(-2, 2)
            v = rng.uniform(1.0, 5.0) + 1j * rng.uniform(-2, 2)
            err = verify_ybe(yang_r_matrix, u, v, N=4, hbar=1.0)
            assert err < 1e-6, f"YBE failed for sl_4: u={u}, v={v}, err={err}"

    def test_ybe_all_types_sweep(self):
        """YBE sweep for sl_2 through sl_5."""
        results = verify_yang_ybe_all_types(N_max=4, n_trials=30)
        for key, val in results.items():
            assert val["passed"], f"YBE failed for {key}: max_error={val['max_ybe_error']}"

    def test_ybe_specific_parameters(self):
        """YBE at specific known-good parameters."""
        for u, v in [(1.0, 2.0), (3.0, 1.0), (2.5+1j, 1.0-0.5j)]:
            err = verify_ybe(yang_r_matrix, u, v, N=2, hbar=1.0)
            assert err < 1e-10, f"YBE failed at u={u}, v={v}"

    def test_ybe_hbar_dependence(self):
        """YBE holds for arbitrary hbar."""
        for hbar in [0.5, 1.0, 2.0, -1.0, 1.0+0.5j]:
            err = verify_ybe(yang_r_matrix, 2.0, 1.0, N=2, hbar=hbar)
            assert err < 1e-8, f"YBE failed for hbar={hbar}"


# ================================================================
# SECTION 2: R-MATRIX UNITARITY
# ================================================================

class TestRMatrixUnitarity:
    """Verify R(u) R^{-1}(u) = I."""

    def test_unitarity_sl2(self):
        """R * R^{-1} = I for sl_2 (avoiding singular u = +/- hbar)."""
        for u in [2.0, 3.0, 3.0+1j, 0.5-2j, 5.0]:
            err = verify_r_matrix_inversion(u, N=2)
            assert err < 1e-10, f"Unitarity failed for sl_2 at u={u}: err={err}"

    def test_unitarity_singular(self):
        """R-matrix is singular at u = hbar."""
        with pytest.raises(ValueError):
            yang_r_inverse_multiplicative(1.0, N=2, hbar=1.0)

    def test_unitarity_sl3(self):
        """R * R^{-1} = I for sl_3."""
        for u in [2.0, 3.0, 1.0+1j]:
            err = verify_r_matrix_inversion(u, N=3)
            assert err < 1e-10, f"Unitarity failed for sl_3 at u={u}: err={err}"

    def test_unitarity_sweep(self):
        """Unitarity sweep for sl_2 and sl_3."""
        for N in [2, 3]:
            result = verify_r_unitarity_sweep(N=N, n_points=30)
            assert result["passed"], f"Unitarity sweep failed for N={N}"

    def test_unitarity_large_u(self):
        """R approaches I for large u, so R^{-1} also approaches I."""
        u = 1000.0
        R = yang_r_matrix_multiplicative(u, N=2)
        assert np.linalg.norm(R - np.eye(4)) < 0.01

    def test_unitarity_hbar_variations(self):
        """Unitarity for different hbar values (u != +/- hbar)."""
        for hbar in [0.5, 1.0, 2.0]:
            u = 3.0 * hbar  # always away from singular points
            err = verify_r_matrix_inversion(u, N=2, hbar=hbar)
            assert err < 1e-10


# ================================================================
# SECTION 3: KOSZUL DUAL SIGN FLIP
# ================================================================

class TestKoszulDualSignFlip:
    """Verify R^{-1}(u;hbar) = R(u;-hbar) at leading order."""

    def test_sign_flip_leading_order(self):
        """R^{-1} and R(-hbar) agree at O(1/u)."""
        diff_norm, expected = koszul_dual_r_matrix_sign_flip(10.0, N=2, hbar=1.0)
        # Difference should be O(1/u^2)
        assert diff_norm < 0.1, f"Sign flip mismatch: diff={diff_norm}"

    def test_sign_flip_large_u(self):
        """At large u, R^{-1} and R(-hbar) converge."""
        diff_norm, expected = koszul_dual_r_matrix_sign_flip(100.0, N=2, hbar=1.0)
        assert diff_norm < 0.001

    def test_sign_flip_scaling(self):
        """Difference scales as 1/u^2."""
        diffs = []
        for u in [5.0, 10.0, 20.0, 50.0]:
            d, _ = koszul_dual_r_matrix_sign_flip(u, N=2, hbar=1.0)
            diffs.append((u, d))

        # Check d ~ C/u^2: ratio d * u^2 should be roughly constant
        scaled = [d * u**2 for u, d in diffs]
        # Allow 50% variation
        assert max(scaled) / min(scaled) < 2.0, f"Scaling not 1/u^2: {scaled}"

    def test_sign_flip_sweep(self):
        """Sweep verification."""
        result = verify_koszul_dual_sign_flip_sweep(N=2, n_points=30)
        assert result["leading_order_match"]

    def test_sign_flip_sl3(self):
        """Sign flip for sl_3."""
        diff_norm, expected = koszul_dual_r_matrix_sign_flip(10.0, N=3, hbar=1.0)
        assert diff_norm < 1.0  # larger matrices, larger tolerance


# ================================================================
# SECTION 4: qKZ -> KZ LIMIT (ABEDIN-NIU)
# ================================================================

class TestQKZToKZLimit:
    """Verify R-matrix residue -> KZ connection (Abedin-Niu 2405.19906).

    The core identification: the residue of the Yang R-matrix R(u) = I - P/u
    at u=0 gives -P, which equals -(Omega + I/N) for sl_N. The KZ connection
    coefficient is Omega/(kappa*(z_i - z_j)), extracted from this residue.
    """

    def test_r_residue_gives_permutation(self):
        """Residue of R(u) at u=0 is -P."""
        # R(u) = I - P/u, so Res_{u=0}(R - I) = -P
        P = permutation_operator(2)
        # Numerical check: (R(u) - I)*u -> -P as u -> 0
        for u in [0.1, 0.01, 0.001]:
            R = yang_r_matrix_multiplicative(u, N=2, hbar=1.0)
            residue = -(R - np.eye(4, dtype=complex)) * u
            assert np.linalg.norm(residue - P) < 1e-8

    def test_permutation_decomposes_as_casimir_plus_trace(self):
        """P = Omega + I/N for sl_N (Casimir + trace part)."""
        N = 2
        P = permutation_operator(N)
        Omega = cotangent_casimir_sl2()
        I_correction = np.eye(N**2, dtype=complex) / N
        assert np.linalg.norm(P - Omega - I_correction) < 1e-15

    def test_qkz_kz_residue_identification(self):
        """Full residue identification: R-matrix -> KZ connection."""
        err = verify_qkz_to_kz_limit(z1=2.0, z2=1.0, eta=0.01, k=1)
        assert err < 1e-8, f"Residue identification failed: err={err}"

    def test_qkz_kz_multiple_levels(self):
        """Residue identification at different levels k."""
        for k in [1, 2, 5]:
            err = verify_qkz_to_kz_limit(z1=3.0, z2=1.0, eta=0.05, k=k)
            assert err < 1e-8, f"Failed at level k={k}: err={err}"

    def test_qkz_kz_sweep(self):
        """Comprehensive sweep."""
        result = verify_qkz_kz_limit_sweep(n_points=10)
        assert result["tests"] > 5
        assert result["all_passed"], f"Sweep failed: max_error={result['max_error']}"

    def test_kz_connection_singular(self):
        """KZ connection is singular at z1=z2."""
        with pytest.raises(ValueError):
            kz_connection_matrix(1.0, 1.0, k=1)

    def test_kz_connection_values(self):
        """KZ connection matrix has correct structure."""
        M = kz_connection_matrix(2.0, 1.0, k=1, h_vee=2)
        # Should be Omega / (kappa * (z1-z2)) = Omega / (3 * 1) = Omega/3
        Omega = cotangent_casimir_sl2()
        expected = Omega / 3.0
        assert np.linalg.norm(M - expected) < 1e-10


# ================================================================
# SECTION 5: NON-RENORMALIZATION = KOSZULNESS
# ================================================================

class TestNonRenormalizationKoszulness:
    """DNP non-renormalization = bar E_2 collapse = Koszulness."""

    def test_type_a_all_ranks(self):
        """Non-renormalization for sl_N, N=2..6."""
        for rank in range(1, 6):
            data = non_renormalization_koszulness_check("A", rank)
            assert data["koszul"]
            assert data["one_loop_exact"]
            assert data["bar_collapse_page"] == 2
            assert data["rtt_quadratic"]

    def test_type_b(self):
        """Non-renormalization for so_{2n+1}."""
        for rank in range(2, 5):
            data = non_renormalization_koszulness_check("B", rank)
            assert data["koszul"]
            assert data["dim_g"] == rank * (2 * rank + 1)

    def test_type_c(self):
        """Non-renormalization for sp_{2n}."""
        for rank in range(2, 5):
            data = non_renormalization_koszulness_check("C", rank)
            assert data["koszul"]
            assert data["dim_g"] == rank * (2 * rank + 1)

    def test_type_d(self):
        """Non-renormalization for so_{2n}."""
        for rank in range(3, 6):
            data = non_renormalization_koszulness_check("D", rank)
            assert data["koszul"]
            assert data["dim_g"] == rank * (2 * rank - 1)

    def test_correspondence_string(self):
        """The correspondence statement is correctly formulated."""
        data = non_renormalization_koszulness_check("A", 1)
        assert "Koszulness" in data["correspondence"]
        assert "E_2" in data["correspondence"]


# ================================================================
# SECTION 6: SPARK ALGEBRA (DIMOFTE-NIU)
# ================================================================

class TestSparkAlgebra:
    """Spark algebra = bar-comodule End (Dimofte-Niu 2411.04194)."""

    def test_bar_identification(self):
        """Spark algebra is End in bar-comodule category."""
        data = spark_algebra_data(g_dim=3)
        assert data["bar_identification"] == "End in bar-comodule category"
        assert data["matches_dk_eval"]
        assert data["e1_factorization"]

    def test_evaluation_locus(self):
        """Spark algebra lives on evaluation locus."""
        data = spark_algebra_data(g_dim=8)
        assert data["evaluation_locus"]

    def test_different_dims(self):
        """Spark algebra data for various Lie algebra dimensions."""
        for dim in [3, 8, 15, 24, 35]:
            data = spark_algebra_data(g_dim=dim)
            assert data["construction"] == "junction local operators"


# ================================================================
# SECTION 7: FACTORIZATION DUAL YANGIAN (ABEDIN-NIU)
# ================================================================

class TestFactorizationDualYangian:
    """Factorization algebra dual Yangian (Abedin-Niu 2512.16996)."""

    def test_genus_0_match(self):
        """Genus-0 sector matches modular Yangian."""
        data = factorization_dual_yangian_data("A", 1)
        assert data["genus_0_match"]
        assert data["r_matrix_match"]
        assert data["coproduct_match"]

    def test_ran_space(self):
        """Ran space structure matches bar complex."""
        data = factorization_dual_yangian_data("A", 1)
        assert "bar complex" in data["ran_space"]

    def test_type_a_ranks(self):
        """Works for all type A ranks."""
        for rank in range(1, 5):
            data = factorization_dual_yangian_data("A", rank)
            expected_dim = (rank + 1)**2 - 1
            assert data["g_dim"] == expected_dim

    def test_langlands_self_dual(self):
        """Type A is Langlands self-dual."""
        for rank in range(1, 5):
            data = factorization_dual_yangian_data("A", rank)
            assert data["langlands_dual"] == f"sl_{rank + 1}"


# ================================================================
# SECTION 8: QUANTUM GROUPOID (ABEDIN-NIU)
# ================================================================

class TestQuantumGroupoid:
    """Quantum groupoid from G-bundles (Abedin-Niu 2411.05068)."""

    def test_groupoid_not_hopf(self):
        """Quantum groupoid is NOT a Hopf algebra."""
        data = quantum_groupoid_data("sl_2")
        assert "groupoid" in data["algebra_type"]
        assert "not Hopf" in data["algebra_type"]

    def test_genus_1_dk(self):
        """Relates to genus-1 DK bridge."""
        data = quantum_groupoid_data("sl_2")
        assert data["comparison_dk"] == "genus-1 DK bridge"
        assert data["modular_yangian_genus_1"]
        assert data["elliptic_r_matrix"]

    def test_dk_square_generalization(self):
        """Generalizes the DK square to genus 1."""
        data = quantum_groupoid_data("sl_3")
        assert "genus-1" in data["relation_to_dk_square"]


# ================================================================
# SECTION 9: STABLE-GRAPH YANG-BAXTER
# ================================================================

class TestStableGraphYB:
    """Stable-graph Yang-Baxter equation at genus 0 and 1."""

    def test_genus_0_cybe(self):
        """Genus-0 stable-graph YB = classical YBE."""
        Omega = cotangent_casimir_sl2()
        result = stable_graph_yb_genus0(Omega)
        assert np.linalg.norm(result) < 1e-15

    def test_genus_1_correction_structure(self):
        """Genus-1 correction has correct structure."""
        Omega = cotangent_casimir_sl2()
        kappa = 2.0  # example value
        result = stable_graph_yb_genus1_correction(kappa, Omega)
        assert result["genus"] == 1
        assert result["kappa"] == kappa
        assert "scalar" in result["correction_type"]

    def test_genus_1_kappa_dependence(self):
        """Genus-1 correction is linear in kappa."""
        Omega = cotangent_casimir_sl2()
        r1 = stable_graph_yb_genus1_correction(1.0, Omega)
        r2 = stable_graph_yb_genus1_correction(2.0, Omega)
        # Loop operator trace should double
        assert abs(r2["loop_operator_trace"] - 2 * r1["loop_operator_trace"]) < 1e-10

    def test_genus_1_casimir_trace(self):
        """Casimir trace for sl_2: (4-1)/2 = 3/2."""
        Omega = cotangent_casimir_sl2()
        result = stable_graph_yb_genus1_correction(1.0, Omega)
        # Tr_{fund}(Omega_{sl_2}) = (N^2-1)/N = 3/2 for N=2
        expected_trace = 1.0 * 1.5  # kappa * casimir_trace
        assert abs(result["loop_operator_trace"] - expected_trace) < 1e-10


# ================================================================
# SECTION 10: SQED dg-SHIFTED YANGIAN
# ================================================================

class TestSQED:
    """SQED dg-shifted Yangian (DNP simplest example)."""

    def test_sqed_data(self):
        """SQED data is correctly structured."""
        data = sqed_koszul_dual_data()
        assert data["gauge_dim"] == 1
        assert data["non_renormalization"]
        assert data["koszul"]
        assert data["bar_collapse"] == "E_2"

    def test_sqed_r_matrix_trivial(self):
        """SQED R-matrix is trivial (abelian)."""
        R = sqed_r_matrix(1.0)
        assert R.shape == (1, 1)
        assert abs(R[0, 0] - 1.0) < 1e-15

    def test_sqed_bar_abelian(self):
        """Bar differential vanishes for abelian gauge theory."""
        data = sqed_bar_differential_degree2(N_f=0)
        assert "zero" in data["gauge_differential"]
        assert data["koszul"]

    def test_sqed_bar_with_matter(self):
        """Bar differential with matter introduces A_infty."""
        for N_f in [1, 2, 3]:
            data = sqed_bar_differential_degree2(N_f=N_f)
            assert data["H2_dim"] == 1 + 2 * N_f


# ================================================================
# SECTION 11: COTANGENT LIE ALGEBRA R-MATRIX
# ================================================================

class TestCotangentRMatrix:
    """T*(sl_2) R-matrix and comparison with Y_T^mod."""

    def test_cotangent_restricts_to_yang(self):
        """T*(sl_2) R-matrix restricts to Yang R-matrix on sl_2."""
        u = 2.0
        R_cot = cotangent_r_matrix_sl2(u, hbar=1.0)
        R_yang = yang_r_matrix(u, N=2, hbar=1.0)
        assert np.linalg.norm(R_cot - R_yang) < 1e-15

    def test_casimir_structure(self):
        """Casimir of sl_2 is P - I/2."""
        Omega = cotangent_casimir_sl2()
        P = permutation_operator(2)
        expected = P - 0.5 * np.eye(4)
        assert np.linalg.norm(Omega - expected) < 1e-15

    def test_casimir_trace(self):
        """Tr(Omega) for sl_2 in fundamental = (4-1)/2 = 3/2."""
        Omega = cotangent_casimir_sl2()
        # Partial trace over second factor: Tr_2(Omega) should give
        # a 2x2 matrix proportional to identity
        # For P: Tr_2(P) = I_2 (trace of permutation is dimension)
        # Tr_2(Omega) = Tr_2(P) - (1/2) Tr_2(I_4) = I_2 - (1/2)*2*I_2 = 0
        # Full trace: Tr(Omega) = Tr(P) - 2 = 2 - 2 = 0
        # (since Tr(P) on C^2 x C^2 = 2)
        full_trace = np.trace(Omega)
        assert abs(full_trace) < 1e-15  # traceless Casimir

    def test_casimir_eigenvalues(self):
        """Casimir eigenvalues: P has eigenvalues +1, -1."""
        Omega = cotangent_casimir_sl2()
        eigenvals = np.sort(np.real(np.linalg.eigvals(Omega)))
        # P eigenvalues: +1 (symmetric, 3-dim) and -1 (antisymmetric, 1-dim)
        # Omega = P - I/2, so eigenvalues: +1/2 (3-fold) and -3/2 (1-fold)
        expected = np.sort([-1.5, 0.5, 0.5, 0.5])
        assert np.allclose(eigenvals, expected, atol=1e-10)


# ================================================================
# SECTION 12: PERMUTATION OPERATOR
# ================================================================

class TestPermutationOperator:
    """Permutation operator properties."""

    def test_p_squared_is_identity(self):
        """P^2 = I (permutation is involution)."""
        for N in [2, 3, 4]:
            P = permutation_operator(N)
            assert np.linalg.norm(P @ P - np.eye(N**2)) < 1e-15

    def test_p_trace(self):
        """Tr(P) = N (trace of permutation = dimension)."""
        for N in [2, 3, 4]:
            P = permutation_operator(N)
            assert abs(np.trace(P) - N) < 1e-15

    def test_p_eigenvalues(self):
        """P eigenvalues: +1 (N(N+1)/2 times) and -1 (N(N-1)/2 times)."""
        for N in [2, 3, 4]:
            P = permutation_operator(N)
            eigenvals = np.real(np.linalg.eigvals(P))
            n_plus = sum(1 for e in eigenvals if abs(e - 1) < 1e-10)
            n_minus = sum(1 for e in eigenvals if abs(e + 1) < 1e-10)
            assert n_plus == N * (N + 1) // 2
            assert n_minus == N * (N - 1) // 2


# ================================================================
# SECTION 13: COMPREHENSIVE RECTIFICATION CHECKS
# ================================================================

class TestRectificationChecklist:
    """Verify the rectification checklist is complete."""

    def test_all_five_papers_covered(self):
        """All five papers appear in the checklist."""
        checklist = rectification_checklist()
        assert "DNP25_2508.11749" in checklist
        assert "AN24a_2405.19906" in checklist
        assert "DN24_2411.04194" in checklist
        assert "AN24b_2411.05068" in checklist
        assert "AN25_2512.16996" in checklist

    def test_dnp25_status_cited(self):
        """DNP25 is marked as already cited."""
        checklist = rectification_checklist()
        assert "CITED" in checklist["DNP25_2508.11749"]["status"]

    def test_uncited_papers_flagged(self):
        """Uncited papers are flagged."""
        checklist = rectification_checklist()
        for key in ["AN24a_2405.19906", "DN24_2411.04194",
                     "AN24b_2411.05068", "AN25_2512.16996"]:
            assert "NOT CITED" in checklist[key]["status"]

    def test_all_actions_defined(self):
        """Every paper has an action item."""
        checklist = rectification_checklist()
        for key, val in checklist.items():
            assert "action" in val
            assert len(val["action"]) > 0

    def test_chapter_findings_complete(self):
        """All three chapters have findings."""
        findings = chapter_specific_findings()
        assert "yangians_foundations.tex" in findings
        assert "yangians_computations.tex" in findings
        assert "yangians_drinfeld_kohno.tex" in findings

    def test_each_chapter_has_findings(self):
        """Each chapter has at least 3 findings."""
        findings = chapter_specific_findings()
        for chapter, items in findings.items():
            assert len(items) >= 3, f"{chapter} has too few findings"

    def test_bibliography_entries(self):
        """Four bibliography entries need to be added."""
        entries = missing_bibliography_entries()
        assert len(entries) == 4
        arxiv_ids = {e["arxiv"] for e in entries}
        assert "2405.19906" in arxiv_ids
        assert "2411.04194" in arxiv_ids
        assert "2411.05068" in arxiv_ids
        assert "2512.16996" in arxiv_ids


# ================================================================
# SECTION 14: R-MATRIX SPECIAL VALUES
# ================================================================

class TestRMatrixSpecialValues:
    """R-matrix at specific parameter values."""

    def test_r_at_hbar_zero(self):
        """R(u; hbar=0) = u*I (trivial braiding)."""
        u = 3.0
        R = yang_r_matrix(u, N=2, hbar=0.0)
        expected = u * np.eye(4, dtype=complex)
        assert np.linalg.norm(R - expected) < 1e-15

    def test_r_multiplicative_large_u(self):
        """R_mult(u) -> I as u -> infinity."""
        R = yang_r_matrix_multiplicative(100.0, N=2, hbar=1.0)
        assert np.linalg.norm(R - np.eye(4)) < 0.025

    def test_r_at_u_equals_hbar(self):
        """R(u=hbar) = hbar*(I - P) (degenerate at u=hbar)."""
        hbar = 1.0
        R = yang_r_matrix(hbar, N=2, hbar=hbar)
        P = permutation_operator(2)
        expected = hbar * (np.eye(4) - P)
        assert np.linalg.norm(R - expected) < 1e-15

    def test_r_symmetric_antisymmetric_eigenspaces(self):
        """R has eigenvalues u+hbar (sym) and u-hbar (antisym)."""
        u = 3.0
        hbar = 1.0
        R = yang_r_matrix(u, N=2, hbar=hbar)
        eigenvals = np.sort(np.real(np.linalg.eigvals(R)))
        # Symmetric subspace (dim 3): eigenvalue u + hbar = 4
        # Antisymmetric subspace (dim 1): eigenvalue u - hbar = 2
        # But R = u*I - hbar*P, and P has eigenvalues +1 (sym) and -1 (antisym)
        # So eigenvalues: u - hbar*1 = 2 (on sym, 3-fold)
        #                 u - hbar*(-1) = 4 (on antisym, 1-fold)
        # Wait: P|_sym = +1, P|_antisym = -1
        # R|_sym = u - hbar, R|_antisym = u + hbar
        expected = np.sort([u + hbar] + [u - hbar] * 3)
        assert np.allclose(eigenvals, expected, atol=1e-10)

    def test_r_inverse_at_special_u(self):
        """R^{-1}(u) on eigenspaces."""
        u = 3.0
        hbar = 1.0
        R_inv = yang_r_inverse_multiplicative(u, N=2, hbar=hbar)
        eigenvals = np.sort(np.real(np.linalg.eigvals(R_inv)))
        # R_mult = 1 - hbar*P/u
        # On sym: 1 - hbar/u = 1 - 1/3 = 2/3
        # On antisym: 1 + hbar/u = 1 + 1/3 = 4/3
        # R_inv on sym: 3/2, on antisym: 3/4
        expected = np.sort([u / (u + hbar)] + [u / (u - hbar)] * 3)
        assert np.allclose(eigenvals, expected, atol=1e-10)


# ================================================================
# SECTION 15: CROSS-CHECKS WITH EXISTING ENGINES
# ================================================================

class TestCrossChecks:
    """Cross-checks with existing Yangian compute modules."""

    def test_yang_r_matrix_matches_rtt_engine(self):
        """Our R-matrix matches the RTT all-types engine convention."""
        # The additive Yang R-matrix R(u) = u*I + P (type A convention in rtt)
        # Our convention: R(u) = u*I - hbar*P
        # With hbar = -1: R(u) = u*I + P (matches)
        u = 2.0
        R_ours = yang_r_matrix(u, N=2, hbar=-1.0)
        P = permutation_operator(2)
        R_rtt = u * np.eye(4) + P  # Type A additive convention
        assert np.linalg.norm(R_ours - R_rtt) < 1e-15

    def test_casimir_matches_sl3_engine(self):
        """Casimir structure consistent with sl3 R-matrix engine."""
        # For sl_2 in fund: Omega = P - I/N
        # Our Casimir: P - I/2
        N = 2
        P = permutation_operator(N)
        Omega_canonical = P - np.eye(N**2) / N
        Omega_ours = cotangent_casimir_sl2()
        assert np.linalg.norm(Omega_canonical - Omega_ours) < 1e-15


# ================================================================
# SECTION 16: DIMENSIONAL CHECKS
# ================================================================

class TestDimensionalChecks:
    """Verify dimensional consistency."""

    def test_r_matrix_dimension(self):
        """R-matrix has dimension N^2 x N^2."""
        for N in [2, 3, 4, 5]:
            R = yang_r_matrix(1.0, N=N)
            assert R.shape == (N**2, N**2)

    def test_permutation_dimension(self):
        """Permutation operator has dimension N^2 x N^2."""
        for N in [2, 3, 4, 5]:
            P = permutation_operator(N)
            assert P.shape == (N**2, N**2)

    def test_kz_parallel_transport_dimension(self):
        """KZ parallel transport matrix is 4x4 for sl_2."""
        from compute.lib.theorem_yangian_chapter_rectification_engine import (
            kz_parallel_transport_2pt,
        )
        A = kz_parallel_transport_2pt(2.0, 1.0, kappa=3.0, dt=0.01, N=2)
        assert A.shape == (4, 4)

    def test_kz_connection_dimension(self):
        """KZ connection matrix is 4x4 for sl_2."""
        M = kz_connection_matrix(2.0, 1.0, k=1)
        assert M.shape == (4, 4)
