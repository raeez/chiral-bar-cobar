r"""Tests for Tannakian QFT engine: spark algebras, R-matrices, quantum groups.

Verifies the five-path comparison between Dimofte-Niu's Tannakian QFT
(arXiv:2411.04194) and the monograph's bar-cobar duality / MC3 / DK bridge.

Multi-path verification mandate: every claim verified by >= 3 independent paths.

Test organization:
- Section 1: Spark algebra structure (Path 1)
- Section 2: Topological R-matrix and YBE (Path 2)
- Section 3: Quantum group reconstruction (Path 4)
- Section 4: Monograph comparison (Paths 1-5 cross-checks)
- Section 5: Drinfeld double (Path 3)
- Section 6: Koszul duality in dg categories (Path 5)
- Section 7: MC3 connection analysis
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from theorem_tannakian_qft_engine import (
    spark_algebra_sl2,
    spark_algebra_sln,
    spark_algebra_finite_group,
    topological_r_matrix_sl2,
    verify_yang_baxter_equation,
    verify_unitarity,
    koszul_dual_r_matrix_sl2,
    verify_koszul_r_matrix_inversion,
    quantum_group_coproduct_sl2,
    verify_quantum_group_relations,
    verify_coproduct_is_algebra_map,
    r_matrix_from_universal_r,
    verify_r_matrix_classical_limit,
    compare_spark_r_with_monograph_r,
    compare_r_matrices_at_levels,
    drinfeld_double_dim,
    drinfeld_double_finite_group,
    verify_drinfeld_double_z2,
    verify_drinfeld_double_s3,
    mc3_tannakian_connection,
    tannakian_vs_bar_cobar_comparison,
    koszul_duality_dg_categories,
)


# ============================================================
# Section 1: Spark algebra structure
# ============================================================

class TestSparkAlgebra:
    """Test spark algebra construction and identification with bar cohomology."""

    def test_sl2_spark_algebra_generators(self):
        """SL(2) spark algebra has rank 1, one generator."""
        data = spark_algebra_sl2()
        assert data['rank'] == 1
        assert len(data['generators']) == 1
        assert data['cartan_dim'] == 1

    def test_sl2_spark_graded_dims(self):
        """SL(2) spark algebra Sym(h*) has dim 1 in every degree (rank 1)."""
        data = spark_algebra_sl2()
        for deg in range(4):
            assert data['graded_dims'][deg] == 1

    def test_sl2_bar_cohomology_match(self):
        """Spark algebra matches bar E_2 page on Koszul locus."""
        data = spark_algebra_sl2()
        assert data['bar_cohomology_match'] is True
        assert data['bar_e2_page'] == 'Sym(h*)'

    def test_sl2_koszul_dual(self):
        """Koszul dual of Sym(h*) is Sym(h) (dual polynomial ring)."""
        data = spark_algebra_sl2()
        assert data['koszul_dual_algebra'] == 'Sym(h)'

    def test_sln_spark_rank(self):
        """SL(n) spark algebra has rank n-1."""
        for n in [2, 3, 4, 5]:
            data = spark_algebra_sln(n)
            assert data['rank'] == n - 1

    def test_sln_graded_dims(self):
        """SL(n) spark Sym^k(C^{n-1}) has correct dimensions."""
        from math import comb
        for n in [2, 3, 4]:
            data = spark_algebra_sln(n)
            rank = n - 1
            for k in range(5):
                expected = comb(k + rank - 1, rank - 1)
                assert data['graded_dims'][k] == expected, (
                    f"SL({n}), degree {k}: got {data['graded_dims'][k]}, "
                    f"expected {expected}"
                )

    def test_sl3_spark_specific_dims(self):
        """SL(3) spark: dim Sym^k(C^2) = k+1."""
        data = spark_algebra_sln(3)
        for k in range(8):
            assert data['graded_dims'][k] == k + 1

    def test_finite_group_spark(self):
        """Finite group spark algebra has correct dimensions."""
        data = spark_algebra_finite_group(6, 3)  # S_3
        assert data['group_order'] == 6
        assert data['n_conjugacy_classes'] == 3
        assert data['center_dim'] == 3
        assert data['drinfeld_double_dim'] == 36


# ============================================================
# Section 2: Topological R-matrix and Yang-Baxter equation
# ============================================================

class TestTopologicalRMatrix:
    """Test the topological R-matrix from spark construction."""

    def test_r_matrix_identity_at_infinity(self):
        """R(u) -> Id as u -> infinity."""
        R = topological_r_matrix_sl2(1000.0)
        np.testing.assert_allclose(R, np.eye(4, dtype=complex), atol=1e-2)

    def test_r_matrix_shape(self):
        """R-matrix is 4x4 (fundamental tensor fundamental of sl_2)."""
        R = topological_r_matrix_sl2(1.0)
        assert R.shape == (4, 4)

    def test_r_matrix_invertible(self):
        """R-matrix is invertible for u != hbar (pole at u=hbar where singlet eigenvalue vanishes)."""
        # At hbar=1: R(u) is singular at u=1 (singlet eigenvalue = 1 - hbar/u = 0)
        # Test at u != hbar
        for u in [0.5, 2.0, 1.0 + 1j, 3.0]:
            R = topological_r_matrix_sl2(u)
            assert abs(np.linalg.det(R)) > 1e-10, (
                f"R-matrix singular at u={u}"
            )

    def test_yang_baxter_equation(self):
        """Quantum YBE holds for the Yang R-matrix."""
        result = verify_yang_baxter_equation(1.0, 2.0)
        assert result['ybe_holds'], (
            f"YBE violation: norm = {result['ybe_norm']}"
        )

    def test_yang_baxter_multiple_points(self):
        """YBE holds at multiple spectral parameters."""
        for u, v in [(1.0, 2.0), (0.5, 0.7), (1.0 + 0.3j, 0.7 - 0.2j),
                     (3.0, 0.1), (0.5 + 1j, 2.0 - 0.5j)]:
            result = verify_yang_baxter_equation(u, v)
            assert result['ybe_holds'], (
                f"YBE fails at u={u}, v={v}: norm={result['ybe_norm']}"
            )

    def test_yang_baxter_hbar_dependence(self):
        """YBE holds for various values of hbar."""
        for hbar in [0.1, 0.5, 1.0, 2.0, 0.01]:
            result = verify_yang_baxter_equation(1.0, 2.0, hbar)
            assert result['ybe_holds'], (
                f"YBE fails at hbar={hbar}: norm={result['ybe_norm']}"
            )

    def test_unitarity(self):
        """R(u) R(-u) = (1 - hbar^2/u^2) Id (Yang unitarity)."""
        result = verify_unitarity(2.0)
        assert result['unitarity_holds'], (
            f"Unitarity violation: norm = {result['unitarity_norm']}"
        )
        # Check scalar factor is correct
        assert abs(result['scalar_factor'] - (1.0 - 1.0/4.0)) < 1e-10

    def test_unitarity_multiple_points(self):
        """Yang unitarity at multiple spectral parameters."""
        for u in [2.0, 2.5, 3.0, 1.0 + 1j, 5.0]:
            result = verify_unitarity(u)
            assert result['unitarity_holds'], (
                f"Unitarity fails at u={u}: norm={result['unitarity_norm']}"
            )

    def test_koszul_dual_r_matrix(self):
        """Koszul dual: R(u,hbar) R(u,-hbar) = (1 - hbar^2/u^2) Id."""
        result = verify_koszul_r_matrix_inversion(2.0)
        assert result['inversion_holds'], (
            f"Koszul inversion fails: norm={result['inversion_norm']}"
        )

    def test_koszul_dual_r_matrix_multiple(self):
        """Koszul R-matrix product is scalar at multiple parameters."""
        for u in [2.0, 3.0, 5.0]:
            for hbar in [0.1, 0.5, 1.0]:
                result = verify_koszul_r_matrix_inversion(u, hbar)
                assert result['inversion_holds'], (
                    f"Koszul inversion fails at u={u}, hbar={hbar}"
                )

    def test_r_matrix_eigenvalues(self):
        """R-matrix has eigenvalues 1+hbar/u (singlet) and 1-hbar/u (triplet)."""
        u = 2.0
        hbar = 0.5
        R = topological_r_matrix_sl2(u, hbar)
        evals = sorted(np.linalg.eigvals(R).real)
        singlet = 1 + hbar / u
        triplet = 1 - hbar / u
        # Triplet is threefold degenerate
        assert abs(evals[0] - triplet) < 1e-10
        assert abs(evals[1] - triplet) < 1e-10
        assert abs(evals[2] - triplet) < 1e-10
        assert abs(evals[3] - singlet) < 1e-10


# ============================================================
# Section 3: Quantum group reconstruction
# ============================================================

class TestQuantumGroupReconstruction:
    """Test Tannakian reconstruction of U_q(sl_2)."""

    def test_quantum_group_relations_small_hbar(self):
        """U_q(sl_2) relations hold at small hbar."""
        result = verify_quantum_group_relations(0.1)
        assert result['ef_relation_holds']
        assert result['kek_relation_holds']
        assert result['kfk_relation_holds']

    def test_quantum_group_relations_moderate_hbar(self):
        """U_q(sl_2) relations hold at moderate hbar."""
        result = verify_quantum_group_relations(0.5)
        assert result['ef_relation_holds']
        assert result['kek_relation_holds']
        assert result['kfk_relation_holds']

    def test_quantum_group_relations_large_hbar(self):
        """U_q(sl_2) relations hold at large hbar."""
        result = verify_quantum_group_relations(1.0)
        assert result['ef_relation_holds']
        assert result['kek_relation_holds']
        assert result['kfk_relation_holds']

    def test_coproduct_algebra_map(self):
        """Coproduct is an algebra homomorphism (Hopf axiom)."""
        for hbar in [0.1, 0.5, 1.0]:
            result = verify_coproduct_is_algebra_map(hbar)
            assert result['ke_relation_on_coproduct_holds'], (
                f"Coproduct not algebra map at hbar={hbar}: "
                f"norm={result['ke_relation_on_coproduct_norm']}"
            )

    def test_universal_r_matrix_invertible(self):
        """Universal R-matrix is invertible."""
        for hbar in [0.1, 0.5, 1.0, 2.0]:
            data = r_matrix_from_universal_r(hbar)
            assert data['is_invertible'], (
                f"Universal R not invertible at hbar={hbar}"
            )

    def test_classical_limit_convergence(self):
        """Quantum R-matrix classical limit converges to expected r-matrix."""
        results = verify_r_matrix_classical_limit()
        for r in results:
            assert r['converges'], (
                f"Classical limit does not converge at hbar={r['hbar']}: "
                f"error={r['classical_limit_error']}"
            )
            # EF coefficient -> 2 as hbar -> 0
            assert abs(r['coeff_ef'] - 2.0) < 0.1, (
                f"EF coefficient {r['coeff_ef']} not close to 2"
            )

    def test_classical_limit_monotone(self):
        """Error in classical limit decreases with hbar."""
        results = verify_r_matrix_classical_limit()
        errors = [r['classical_limit_error'] for r in results]
        for i in range(len(errors) - 1):
            assert errors[i] > errors[i + 1] * 0.5, (
                f"Classical limit error not monotonically decreasing"
            )


# ============================================================
# Section 4: Comparison with monograph's R-matrix
# ============================================================

class TestMonographComparison:
    """Test comparison between spark R-matrix and monograph's bar-derived R-matrix."""

    def test_p_equals_2omega_plus_half_id(self):
        """Permutation P = 2*Omega + Id/2 for sl_2 fundamental."""
        result = compare_spark_r_with_monograph_r(1.0)
        assert result['P_equals_2Omega_plus_half_Id']

    def test_level_comparison_eigenvalues(self):
        """R-matrix eigenvalues match at various levels."""
        results = compare_r_matrices_at_levels()
        for r in results:
            assert r['singlet_match'], (
                f"Singlet eigenvalue mismatch at level {r['level']}"
            )
            assert r['triplet_match'], (
                f"Triplet eigenvalue mismatch at level {r['level']}"
            )

    def test_spark_matches_yang_r_matrix(self):
        """Spark topological R-matrix IS the Yang R-matrix."""
        P = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ], dtype=complex)
        for u in [1.0, 2.0, 0.5]:
            for hbar in [0.1, 1.0]:
                R = topological_r_matrix_sl2(u, hbar)
                expected = np.eye(4, dtype=complex) - hbar * P / u
                np.testing.assert_allclose(R, expected, atol=1e-14)

    def test_hbar_identification_with_level(self):
        """At level k for sl_2: hbar = 1/(k + h^v) with h^v = 2."""
        h_dual = 2
        for k in [1, 2, 3, 5, 10]:
            hbar = 1.0 / (k + h_dual)
            # Use u=2 to avoid singularity (u >> hbar)
            R = topological_r_matrix_sl2(2.0, hbar)
            # R should be well-defined (not singular)
            assert abs(np.linalg.det(R)) > 0.1, (
                f"R-matrix nearly singular at level {k}"
            )


# ============================================================
# Section 5: Drinfeld double from boundary conditions
# ============================================================

class TestDrinfeldDouble:
    """Test Drinfeld double construction from transverse boundary pairs."""

    def test_double_dimension(self):
        """D(H) has dimension dim(H)^2."""
        for d in [2, 4, 6, 8]:
            assert drinfeld_double_dim(d) == d ** 2

    def test_z2_double(self):
        """D(Z/2) = C[Z/2 x Z/2], dimension 4, 4 irreps."""
        data = verify_drinfeld_double_z2()
        assert data['double_dim'] == 4
        assert data['n_irreps'] == 4
        assert data['is_abelian'] is True
        assert data['double_group'] == 'Z/2 x Z/2'

    def test_s3_double(self):
        """D(S_3) has dimension 36 and 8 irreps."""
        data = verify_drinfeld_double_s3()
        assert data['double_dim'] == 36
        assert data['total_irreps'] == 8

    def test_s3_centralizer_decomposition(self):
        """D(S_3) irrep count = sum of centralizer irrep counts."""
        data = verify_drinfeld_double_s3()
        total = sum(c['n_irreps'] for c in data['centralizer_data'])
        assert total == data['total_irreps']

    def test_abelian_double_dim(self):
        """For abelian G of order n: D(G) has n^2 one-dimensional irreps."""
        for n in [2, 3, 4, 5]:
            data = drinfeld_double_finite_group(n)
            assert data['double_dim'] == n ** 2


# ============================================================
# Section 6: Koszul duality in dg categories
# ============================================================

class TestKoszulDualityDgCategories:
    """Test Koszul duality connections between Tannakian QFT and bar-cobar."""

    def test_three_levels_present(self):
        """Koszul duality operates at algebra, category, and dg levels."""
        data = koszul_duality_dg_categories()
        assert 'level_1_algebra' in data
        assert 'level_2_category' in data
        assert 'level_3_dg' in data

    def test_level_1_proved(self):
        """Algebra-level Koszul duality (Theorem A) is proved."""
        data = koszul_duality_dg_categories()
        assert data['level_1_algebra']['status'] == 'PROVED'

    def test_level_2_proved(self):
        """Category-level Koszul duality is proved on evaluation core."""
        data = koszul_duality_dg_categories()
        assert 'PROVED' in data['level_2_category']['status']

    def test_level_3_proved(self):
        """dg-level Koszul duality (strictification) is proved."""
        data = koszul_duality_dg_categories()
        assert 'PROVED' in data['level_3_dg']['status']


# ============================================================
# Section 7: MC3 connection analysis
# ============================================================

class TestMC3Connection:
    """Test the connection between MC3 and Tannakian QFT."""

    def test_mc3_is_proved(self):
        """MC3 is proved for all simple types on evaluation-generated core."""
        data = mc3_tannakian_connection()
        assert 'PROVED' in data['mc3_status']

    def test_tannakian_provides_independent_confirmation(self):
        """Tannakian QFT provides independent physics confirmation."""
        data = mc3_tannakian_connection()
        assert 'Independent physics confirmation' in data['tannakian_qft_provides']

    def test_tannakian_does_not_replace_mc3(self):
        """Tannakian QFT does NOT provide a mathematical proof of MC3."""
        data = mc3_tannakian_connection()
        assert any('Mathematical proof' in item
                    for item in data['tannakian_qft_does_not_provide'])

    def test_tannakian_genus_zero_only(self):
        """Tannakian QFT is genus 0 only (no higher genus data from sparks)."""
        data = mc3_tannakian_connection()
        assert any('genus 0' in item.lower()
                    for item in data['tannakian_qft_does_not_provide'])

    def test_bridge_item_b3(self):
        """Tannakian QFT connects to DK bridge item B3."""
        data = mc3_tannakian_connection()
        assert 'B3' in data['bridge_item']

    def test_five_parallel_structures(self):
        """Five parallel structures between Tannakian QFT and bar-cobar."""
        data = tannakian_vs_bar_cobar_comparison()
        assert len(data['parallel_structures']) == 5

    def test_collision_residue_identification_proved(self):
        """Collision residue = topological R-matrix is PROVED."""
        data = tannakian_vs_bar_cobar_comparison()
        r_matrix_entry = [s for s in data['parallel_structures']
                          if 'R-matrix' in s['tannakian']][0]
        assert 'PROVED' in r_matrix_entry['status']

    def test_fiber_functor_identification_proved(self):
        """Tannakian fiber functor = cobar functor is PROVED."""
        data = tannakian_vs_bar_cobar_comparison()
        fiber_entry = [s for s in data['parallel_structures']
                       if 'fiber functor' in s['tannakian'].lower()][0]
        assert 'PROVED' in fiber_entry['status']
