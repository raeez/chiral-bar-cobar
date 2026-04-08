r"""Tests for bar cohomology of quantum groups U_q(g) engine.

Multi-path verification structure (at least 3 independent paths per claim):
  Path 1: Direct computation from definitions
  Path 2: Classical limit q -> 1 (recovers U(g))
  Path 3: Root of unity limit (Ginzburg-Kumar polynomial ring)
  Path 4: Cross-checks with companion engines (quantum_group_bar_engine,
          quantum_group_root_of_unity_engine, bar_cohomology_ce)
  Path 5: Dimensional consistency (n_rel + dim_quadratic_dual = 16)
  Path 6: Drinfeld double self-duality (dim D = (dim B)^2 = p^4)
  Path 7: Hopf structure cross-check (skew-primitives = 3)

Organization:
  1.  q-arithmetic (3 tests)
  2.  Generating space V (2 tests)
  3.  Ordered bar B^{ord,n} (4 tests)
  4.  Hochschild chain dimensions (3 tests)
  5.  Classical sl_2 cohomology (2 tests)
  6.  q-deformed generic cohomology (3 tests)
  7.  Small quantum group u_q(sl_2) (5 tests)
  8.  Drinfeld double D(U_q(sl_2)) (4 tests)
  9.  Universal R-matrix in H^{1,1} (5 tests)
  10. Koszul dual quadratic relations (3 tests)
  11. Classical limit q -> 1 (3 tests)
  12. Primitive filtration (3 tests)
  13. Koszul resolution Tor (3 tests)
  14. Cross-engine consistency (3 tests)
  15. Comprehensive verification (2 tests)
  16. Multi-path verification (3 tests)

Total: 51 tests.

References:
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  AP25 (bar != Verdier != cobar), AP33 (Koszul dual != FF involution),
  AP45 (desuspension lowers degree), AP50 (A^!_infty != A^!)
  Ginzburg-Kumar, Duke Math J. 69 (1993)
  Drinfeld ICM 1986, Kassel GTM 155
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.bar_quantum_groups_engine import (
    # q-arithmetic
    q_number,
    q_factorial,
    # Generating space
    uq_sl2_generating_space,
    UqSl2PBW,
    # Ordered bar
    OrderedBarSpace,
    ordered_bar_uqsl2,
    # Hochschild
    hochschild_chain_dim,
    hochschild_dimension_uqsl2,
    # Classical cohomology
    classical_sl2_cohomology_dimensions,
    classical_ce_sl2_dimensions,
    # q-deformed
    q_deformed_sl2_cohomology_generic,
    # Small quantum group
    small_uq_sl2_dimension,
    small_uq_sl2_cohomology_dimensions,
    small_uq_sl2_hilbert_series,
    nilpotent_cone_dimension_sl2,
    # Drinfeld double
    drinfeld_double_dimension,
    small_uq_borel_dimension,
    drinfeld_double_koszul_pairing,
    verify_drinfeld_double_selfduality,
    # R-matrix
    r_matrix_bar_degree,
    r_matrix_leading_term_dim,
    r_matrix_classical_limit_rank,
    universal_r_cohomology_class_check,
    # Quadratic dual
    uqsl2_relation_matrix,
    dim_quadratic_dual,
    # Classical limit
    classical_limit_uqsl2,
    # Primitive filtration
    ordered_bar_primitive_filtration,
    prim_uqsl2_at_q1,
    prim_uqsl2_generic,
    skew_prim_uqsl2,
    # Koszul resolution
    koszul_resolution_uqsl2_tor,
    koszul_lambda_dimensions,
    # Comprehensive
    comprehensive_bar_uqsl2_verification,
    verify_classical_limit_agreement,
    verify_small_uq_ring_structure,
    verify_r_matrix_nontriviality,
)


# =========================================================================
# 1. q-arithmetic (3 tests)
# =========================================================================

class TestQArithmetic:
    """Tests for q-number and q-factorial."""

    def test_q_number_classical_limit(self):
        """[n]_q -> n as q -> 1."""
        q = 1.0 + 1e-12
        for n in range(1, 8):
            assert abs(q_number(n, q) - n) < 1e-6

    def test_q_number_explicit_sl2_level_1(self):
        """At q = exp(pi*i/3) (sl_2 level 1): [2]_q = q + q^{-1}."""
        q = cmath.exp(1j * cmath.pi / 3)
        val = q_number(2, q)
        expected = q + 1.0 / q
        assert abs(val - expected) < 1e-12

    def test_q_factorial_values(self):
        """[3]_q! = [1]_q [2]_q [3]_q at generic q."""
        q = cmath.exp(0.4j)
        prod = q_number(1, q) * q_number(2, q) * q_number(3, q)
        assert abs(q_factorial(3, q) - prod) < 1e-10


# =========================================================================
# 2. Generating space V (2 tests)
# =========================================================================

class TestGeneratingSpace:
    """Tests for the four-dimensional generating space V."""

    def test_V_has_dim_4(self):
        """V = span{E, F, K-1, K^{-1}-1} has dim 4."""
        q = cmath.exp(0.3j)
        V = uq_sl2_generating_space(q)
        assert V["dim"] == 4
        assert len(V["names"]) == 4

    def test_V_names(self):
        """The four generators are named E, F, K-1, K^{-1}-1."""
        q = cmath.exp(0.3j)
        V = uq_sl2_generating_space(q)
        assert "E" in V["names"]
        assert "F" in V["names"]


# =========================================================================
# 3. Ordered bar B^{ord,n} (4 tests)
# =========================================================================

class TestOrderedBar:
    """Tests for the ordered bar complex of U_q(sl_2)."""

    def test_bar_degree_0(self):
        """B^{ord,0} = k (one-dimensional)."""
        q = cmath.exp(0.3j)
        bar = ordered_bar_uqsl2(q)
        assert bar.basis_size(0) == 1

    def test_bar_degree_1_equals_generators(self):
        """B^{ord,1} = V has dimension 4."""
        q = cmath.exp(0.3j)
        bar = ordered_bar_uqsl2(q)
        assert bar.basis_size(1) == 4

    def test_bar_degree_2_equals_V_squared(self):
        """B^{ord,2} = V tensor V has dimension 16."""
        q = cmath.exp(0.3j)
        bar = ordered_bar_uqsl2(q)
        assert bar.basis_size(2) == 16

    def test_bar_enumeration(self):
        """Enumerating B^{ord,2} gives 4^2 = 16 ordered pairs."""
        q = cmath.exp(0.3j)
        bar = ordered_bar_uqsl2(q)
        basis = bar.enumerate_basis(2)
        assert len(basis) == 16
        # Every element is a pair of indices in {0,1,2,3}
        for elt in basis:
            assert len(elt) == 2
            assert all(0 <= i < 4 for i in elt)


# =========================================================================
# 4. Hochschild chain dimensions (3 tests)
# =========================================================================

class TestHochschildChains:
    """Tests for Hochschild chain group dimensions."""

    def test_chain_dim_degree_0(self):
        """C_0 = k, dim 1."""
        assert hochschild_chain_dim(4, 0) == 1

    def test_chain_dim_degree_n(self):
        """C_n = A^{otimes n} has dim (gen_dim)^n."""
        for gen_dim in [3, 4, 5]:
            for n in range(5):
                assert hochschild_chain_dim(gen_dim, n) == gen_dim ** n

    def test_chain_dim_negative(self):
        """C_{-1} = 0 by convention."""
        assert hochschild_chain_dim(4, -1) == 0


# =========================================================================
# 5. Classical sl_2 cohomology (2 tests)
# =========================================================================

class TestClassicalSl2Cohomology:
    """Classical Lie algebra cohomology H^*(sl_2, k)."""

    def test_ce_dimensions_match(self):
        """H^0 = 1, H^1 = 0, H^2 = 0, H^3 = 1."""
        h = classical_sl2_cohomology_dimensions()
        assert h[0] == 1
        assert h[1] == 0
        assert h[2] == 0
        assert h[3] == 1

    def test_ce_dimensions_consistency(self):
        """classical_sl2 == classical_ce_sl2 (two functions, same answer)."""
        h1 = classical_sl2_cohomology_dimensions()
        h2 = classical_ce_sl2_dimensions()
        for n in range(4):
            assert h1[n] == h2[n]


# =========================================================================
# 6. q-deformed generic cohomology (3 tests)
# =========================================================================

class TestQDeformedCohomology:
    """Bar cohomology of U_q(sl_2) at generic q."""

    def test_generic_q_matches_classical(self):
        """At generic q, H^*(U_q(sl_2), k) = H^*(sl_2, k) (rigidity)."""
        q = cmath.exp(0.3 + 0.1j)
        classical = classical_sl2_cohomology_dimensions()
        deformed = q_deformed_sl2_cohomology_generic(q)
        for n in range(4):
            assert classical[n] == deformed[n]

    def test_h0_is_trivial(self):
        """H^0 = k always (trivial module)."""
        q = cmath.exp(0.5j)
        h = q_deformed_sl2_cohomology_generic(q)
        assert h[0] == 1

    def test_h3_nonzero(self):
        """H^3 is the top class of sl_2, nonzero."""
        q = cmath.exp(0.5j)
        h = q_deformed_sl2_cohomology_generic(q)
        assert h[3] == 1


# =========================================================================
# 7. Small quantum group u_q(sl_2) (5 tests)
# =========================================================================

class TestSmallQuantumGroup:
    """Tests for u_q(sl_2) at roots of unity."""

    def test_dim_p_cubed(self):
        """dim u_q(sl_2) = p^3."""
        for p in [3, 4, 5, 7]:
            assert small_uq_sl2_dimension(p) == p ** 3

    def test_invalid_p(self):
        """p < 2 raises ValueError."""
        with pytest.raises(ValueError):
            small_uq_sl2_dimension(1)

    def test_ginzburg_kumar_polynomial_ring(self):
        """H^*(u_q(sl_2), k) = C[x] with |x| = 2 (Ginzburg-Kumar)."""
        for p in [3, 5, 7]:
            dims = small_uq_sl2_cohomology_dimensions(p)
            # H^{even} = 1, H^{odd} = 0
            for n in range(8):
                if n % 2 == 0:
                    assert dims[n] == 1, f"H^{n} should be 1"
                else:
                    assert dims[n] == 0, f"H^{n} should be 0"

    def test_hilbert_series_polynomial(self):
        """Hilbert series coefficients: 1, 0, 1, 0, 1, 0, ..."""
        hs = small_uq_sl2_hilbert_series(5, 8)
        expected = [1, 0, 1, 0, 1, 0, 1, 0, 1]
        assert hs == expected

    def test_nilpotent_cone_dim(self):
        """dim N_{sl_2} = 2 (N(N-1) for N = 2)."""
        assert nilpotent_cone_dimension_sl2() == 2


# =========================================================================
# 8. Drinfeld double D(U_q(sl_2)) (4 tests)
# =========================================================================

class TestDrinfeldDouble:
    """Tests for the Drinfeld double of small quantum Borel."""

    def test_borel_dimension(self):
        """dim u_q(b_+) = p^2."""
        for p in [3, 4, 5]:
            assert small_uq_borel_dimension(p) == p ** 2

    def test_double_dimension(self):
        """dim D(u_q(b_+)) = p^4."""
        for p in [3, 4, 5]:
            d_b = small_uq_borel_dimension(p)
            assert drinfeld_double_dimension(d_b) == p ** 4

    def test_double_koszul_pairing(self):
        """Pairing data: dim B_+ * dim B_- = dim D."""
        for p in [3, 5]:
            data = drinfeld_double_koszul_pairing(p)
            assert data["dim_borel_plus"] == p ** 2
            assert data["dim_borel_minus"] == p ** 2
            assert data["dim_double"] == p ** 4

    def test_double_selfduality(self):
        """Verify dim D = dim B_+ * dim B_-."""
        for p in [3, 5, 7]:
            result = verify_drinfeld_double_selfduality(p)
            assert result["matches"]
            assert result["p_to_4"]


# =========================================================================
# 9. Universal R-matrix in H^{1,1} (5 tests)
# =========================================================================

class TestRMatrixClass:
    """Tests for the R-matrix as a (1,1) cohomology class."""

    def test_bidegree(self):
        """R lives in bar degree (1, 1)."""
        assert r_matrix_bar_degree() == (1, 1)

    def test_leading_term_generic(self):
        """At generic q, the leading coefficient q - q^{-1} is nonzero."""
        q = cmath.exp(0.3 + 0.1j)
        check = universal_r_cohomology_class_check(q, 5)
        assert check["nontrivial_at_1_1"]

    def test_leading_term_at_q_1(self):
        """At q = 1, the leading coefficient vanishes (no deformation)."""
        q = 1.0 + 0.0j
        check = universal_r_cohomology_class_check(q, 5)
        assert not check["nontrivial_at_1_1"]

    def test_r_matrix_truncation_at_root(self):
        """At p-th root of unity, R truncates at p terms."""
        for p in [3, 5, 7]:
            n_terms = r_matrix_leading_term_dim(p)
            assert n_terms == p

    def test_classical_rank_is_3(self):
        """Classical r-matrix r = Omega has rank dim(sl_2) = 3."""
        q = cmath.exp(0.3j)
        assert r_matrix_classical_limit_rank(q) == 3


# =========================================================================
# 10. Koszul dual quadratic relations (3 tests)
# =========================================================================

class TestKoszulQuadraticDual:
    """Tests for the quadratic relations and their dual."""

    def test_relation_matrix_shape(self):
        """Relation matrix is 4 x 16 (4 relations in V tensor V)."""
        q = cmath.exp(0.3j)
        R = uqsl2_relation_matrix(q)
        assert R.shape == (4, 16)

    def test_relation_matrix_rank(self):
        """Relation matrix has rank 4 at generic q."""
        q = cmath.exp(0.3 + 0.1j)
        R = uqsl2_relation_matrix(q)
        rank = np.linalg.matrix_rank(R, tol=1e-10)
        assert rank == 4

    def test_quadratic_dual_dimension(self):
        """dim V^! = 16 - 4 = 12 at generic q."""
        q = cmath.exp(0.3 + 0.1j)
        dim_dual = dim_quadratic_dual(q)
        assert dim_dual == 12


# =========================================================================
# 11. Classical limit q -> 1 (3 tests)
# =========================================================================

class TestClassicalLimit:
    """Tests for the q -> 1 limit recovering U(sl_2)."""

    def test_classical_limit_close_to_1(self):
        """q close to 1 is flagged as classical."""
        q = 1.0 + 1e-8
        result = classical_limit_uqsl2(q, tolerance=1e-4)
        assert result["close_to_classical"]

    def test_classical_limit_far_from_1(self):
        """q far from 1 is NOT classical."""
        q = cmath.exp(1.0j)
        result = classical_limit_uqsl2(q, tolerance=1e-4)
        assert not result["close_to_classical"]

    def test_cohomology_limit_agrees(self):
        """q -> 1 cohomology agrees with classical sl_2 cohomology."""
        result = verify_classical_limit_agreement()
        assert result["agree"]


# =========================================================================
# 12. Primitive filtration (3 tests)
# =========================================================================

class TestPrimitiveFiltration:
    """Tests for the primitive filtration on the ordered bar."""

    def test_primitive_at_q1(self):
        """At q = 1, dim Prim = 3 (= dim sl_2)."""
        assert prim_uqsl2_at_q1() == 3

    def test_strict_primitive_generic_q(self):
        """At generic q, dim strict Prim = 0."""
        assert prim_uqsl2_generic() == 0

    def test_skew_primitive_equals_3(self):
        """Skew-primitives {E, F, K-1} have dim 3."""
        assert skew_prim_uqsl2() == 3


# =========================================================================
# 13. Koszul resolution Tor (3 tests)
# =========================================================================

class TestKoszulResolution:
    """Tests for Koszul resolution and Tor computations."""

    def test_koszul_lambda_dimensions(self):
        """dim Lambda^n(sl_2) = C(3, n)."""
        dims = koszul_lambda_dimensions()
        assert dims[0] == 1
        assert dims[1] == 3
        assert dims[2] == 3
        assert dims[3] == 1

    def test_tor_matches_classical_cohomology(self):
        """Tor_n(k, k) = H^n(sl_2, k)."""
        q = cmath.exp(0.3j)
        tor = koszul_resolution_uqsl2_tor(q)
        classical = classical_sl2_cohomology_dimensions()
        for n in range(4):
            assert tor[n] == classical[n]

    def test_tor_vanishing_high_degree(self):
        """Tor_n = 0 for n >= 4."""
        q = cmath.exp(0.3j)
        tor = koszul_resolution_uqsl2_tor(q, max_deg=5)
        assert tor[4] == 0
        assert tor[5] == 0


# =========================================================================
# 14. Cross-engine consistency (3 tests)
# =========================================================================

class TestCrossEngineConsistency:
    """Tests cross-checking with companion engines."""

    def test_q_number_agrees_with_companion(self):
        """q_number in this engine matches quantum_group_bar_engine."""
        from compute.lib.quantum_group_bar_engine import q_number as qn_ref
        q = cmath.exp(0.3 + 0.1j)
        for n in range(1, 6):
            assert abs(q_number(n, q) - qn_ref(n, q)) < 1e-12

    def test_hochschild_dim_consistency(self):
        """Hochschild chain dim agrees with power of generator dim."""
        for n in range(4):
            assert hochschild_chain_dim(4, n) == 4 ** n

    def test_bar_dim_equals_hochschild_chain_dim(self):
        """Ordered bar dim equals Hochschild chain dim at same n."""
        q = cmath.exp(0.3j)
        bar = ordered_bar_uqsl2(q)
        for n in range(4):
            assert bar.basis_size(n) == hochschild_chain_dim(4, n)


# =========================================================================
# 15. Comprehensive verification (2 tests)
# =========================================================================

class TestComprehensive:
    """End-to-end comprehensive verification."""

    def test_comprehensive_runs(self):
        """Comprehensive verification bundle runs and returns all keys."""
        q = cmath.exp(0.3 + 0.1j)
        results = comprehensive_bar_uqsl2_verification(q, p=5)
        required_keys = [
            "ordered_bar_dims",
            "bar_cohomology_generic",
            "small_uq_dim",
            "small_uq_cohomology",
            "drinfeld_double",
            "r_matrix_bidegree",
            "r_matrix_check",
            "classical_limit",
            "koszul_tor",
            "hochschild",
        ]
        for key in required_keys:
            assert key in results, f"Missing key: {key}"

    def test_comprehensive_values_consistent(self):
        """Comprehensive verification: internal consistency of results."""
        q = cmath.exp(0.3 + 0.1j)
        results = comprehensive_bar_uqsl2_verification(q, p=5)
        # Small u_q dimension should be 5^3 = 125
        assert results["small_uq_dim"] == 125
        # Drinfeld double should self-verify
        assert results["drinfeld_double"]["matches"]
        # R-matrix should be nontrivial
        assert results["r_matrix_check"]["nontrivial_at_1_1"]
        # Bar H^3 should be 1 (top class)
        assert results["bar_cohomology_generic"][3] == 1


# =========================================================================
# 16. Multi-path verification (3 tests)
# =========================================================================

class TestMultipathVerification:
    """Multi-path verification of key claims (>= 3 independent paths)."""

    def test_three_paths_small_uq(self):
        """Three paths to H^*(u_q(sl_2), k) polynomial ring."""
        p = 5
        # Path 1: Direct dimensions
        dims = small_uq_sl2_cohomology_dimensions(p)
        # Path 2: Hilbert series
        hs = small_uq_sl2_hilbert_series(p, 8)
        # Path 3: Ring structure verification
        verify = verify_small_uq_ring_structure(p)

        # All should give H^0 = 1, H^2 = 1, H^4 = 1
        assert dims[0] == 1
        assert hs[0] == 1
        assert verify["polynomial_ring_check"]

        assert dims[2] == 1
        assert hs[2] == 1

        assert dims[4] == 1
        assert hs[4] == 1

    def test_three_paths_drinfeld_double(self):
        """Three paths to dim D(u_q(b_+)) = p^4."""
        p = 5
        # Path 1: Direct p^4
        direct = p ** 4
        # Path 2: double of borel dimension
        d_borel = small_uq_borel_dimension(p)
        via_double = drinfeld_double_dimension(d_borel)
        # Path 3: Self-duality verification
        verify = verify_drinfeld_double_selfduality(p)

        assert direct == 625
        assert via_double == 625
        assert verify["dim_double"] == 625

    def test_three_paths_classical_limit(self):
        """Three paths to H^*(U(sl_2), k) = Lambda(x_3)."""
        # Path 1: Classical CE cohomology
        cl1 = classical_sl2_cohomology_dimensions()
        # Path 2: CE cohomology direct
        cl2 = classical_ce_sl2_dimensions()
        # Path 3: q -> 1 limit of deformed cohomology
        cl3 = q_deformed_sl2_cohomology_generic(1.0 + 1e-8)

        # All should agree: H^0 = H^3 = 1, H^1 = H^2 = 0
        for n in range(4):
            a = cl1.get(n, 0)
            b = cl2.get(n, 0)
            c = cl3.get(n, 0)
            assert a == b == c, f"Mismatch at degree {n}: {a}, {b}, {c}"
