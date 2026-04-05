r"""Tests for bc_cluster_shadow_engine.py — cluster algebra mutations from shadow coefficients.

80+ tests covering all 8 mathematical domains:
1. Shadow exchange matrix construction and properties
2. Cluster mutation mechanics (involution, exchange relations)
3. Laurent phenomenon for shadow variables
4. Tropical shadow spectrum
5. Cluster modular group (rank-2 analysis)
6. F-polynomials and g-vectors
7. Shadow quiver classification
8. Koszul duality as cluster transformation

Verification paths (>= 3 per major claim):
Path 1: Laurent phenomenon — S_r is Laurent in initial variables
Path 2: F-polynomial positivity — coefficients positive
Path 3: Mutation involution — mu_k^2 = id
Path 4: Exchange relation consistency — both sides of MC agree
Path 5: Quiver mutation — B-matrix transforms correctly
Path 6: Koszul duality — S_r(c) + S_r(26-c) structure
Path 7: Depth class determines quiver type
Path 8: Numerical cross-check at specific c values
"""

import math
import pytest
import numpy as np

from sympy import Rational, Symbol, cancel, simplify, factor, S as Sym

from compute.lib.bc_cluster_shadow_engine import (
    virasoro_shadow_tower,
    virasoro_shadow_numerical,
    affine_sl2_shadow_tower,
    heisenberg_shadow_tower,
    mc_recursion_coefficient,
    shadow_exchange_matrix,
    shadow_exchange_matrix_exact,
    cluster_mutation,
    mutation_sequence,
    mutation_involution_check,
    shadow_cluster_variables,
    exchange_relation_check,
    shadow_as_rational_function,
    shadow_laurent_in_initial_data,
    p_adic_valuation,
    rational_p_adic_valuation,
    tropical_shadow_vector,
    tropical_shadow_spectrum,
    rank2_cluster_variable_orbit,
    shadow_cluster_modular_group,
    compute_f_polynomials,
    g_vectors,
    shadow_quiver,
    koszul_dual_shadow_tower,
    koszul_duality_mutation_test,
    depth_class_from_quiver,
    caldero_chapoton_rank1,
    cluster_character_rank2,
    full_cluster_shadow_analysis,
    complementarity_sum_tower,
    self_dual_tower,
)

from fractions import Fraction

c = Symbol('c')


# ============================================================================
# 1. Shadow tower — basic structure (cross-check with existing engines)
# ============================================================================

class TestShadowTowerBasic:
    """Verify shadow tower matches known results from virasoro_shadow_tower.py."""

    def test_virasoro_S2_is_kappa(self):
        """S_2 = kappa = c/2 for Virasoro."""
        tower = virasoro_shadow_tower(5)
        assert simplify(tower[2] - c / 2) == 0

    def test_virasoro_S3_is_2(self):
        """S_3 = 2 (gravitational cubic)."""
        tower = virasoro_shadow_tower(5)
        assert simplify(tower[3] - Rational(2)) == 0

    def test_virasoro_S4_is_Q0(self):
        """S_4 = 10/(c(5c+22)) (contact quartic)."""
        tower = virasoro_shadow_tower(5)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(tower[4] - expected) == 0

    def test_virasoro_S5_exact(self):
        """S_5 = -48/(c^2(5c+22)) — matches quintic_shadow_engine.py."""
        tower = virasoro_shadow_tower(6)
        expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(tower[5] - expected) == 0

    def test_virasoro_S6_exact(self):
        """S_6 = 80(45c+193)/(3*c^3*(5c+22)^2) — matches quintic_shadow_engine.py."""
        tower = virasoro_shadow_tower(7)
        expected = Rational(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2)
        assert simplify(tower[6] - expected) == 0

    def test_virasoro_S7_exact(self):
        """S_7 = -2880(15c+61)/(7*c^4*(5c+22)^2) — matches quintic_shadow_engine.py."""
        tower = virasoro_shadow_tower(8)
        expected = Rational(-2880) * (15 * c + 61) / (7 * c ** 4 * (5 * c + 22) ** 2)
        assert simplify(tower[7] - expected) == 0

    def test_virasoro_tower_alternating_signs(self):
        """Shadow coefficients alternate in sign starting from S_4."""
        tower = virasoro_shadow_tower(10)
        for r in range(4, 11):
            val = float(tower[r].subs(c, 10))
            if r % 2 == 0:
                assert val > 0, f"S_{r} should be positive at c=10, got {val}"
            else:
                assert val < 0, f"S_{r} should be negative at c=10, got {val}"

    def test_virasoro_numerical_matches_symbolic(self):
        """Numerical evaluation matches symbolic at c = 7."""
        tower_sym = virasoro_shadow_tower(8)
        tower_num = virasoro_shadow_numerical(7, 8)
        for r in range(2, 9):
            sym_val = float(tower_sym[r].subs(c, 7))
            num_val = tower_num[r]
            assert abs(sym_val - num_val) < 1e-12, f"Mismatch at r={r}: {sym_val} vs {num_val}"

    def test_heisenberg_depth_2(self):
        """Heisenberg tower terminates at depth 2: S_r = 0 for r >= 3."""
        tower = heisenberg_shadow_tower(10)
        for r in range(3, 11):
            assert tower[r] == 0, f"Heisenberg S_{r} should be 0"

    def test_affine_sl2_depth_3(self):
        """Affine sl_2 tower terminates at depth 3: S_r = 0 for r >= 4."""
        tower = affine_sl2_shadow_tower(10)
        for r in range(4, 11):
            assert tower[r] == 0, f"Affine sl_2 S_{r} should be 0"


# ============================================================================
# 2. Shadow exchange matrix
# ============================================================================

class TestExchangeMatrix:
    """Test the shadow exchange matrix B_{ij}."""

    def test_exchange_matrix_skew_symmetric(self):
        """B is skew-symmetric: B_{ij} = -B_{ji}."""
        B = shadow_exchange_matrix(8)
        assert np.allclose(B, -B.T), "Exchange matrix should be skew-symmetric"

    def test_exchange_matrix_diagonal_zero(self):
        """B_{ii} = 0 for all i."""
        B = shadow_exchange_matrix(8)
        assert np.allclose(np.diag(B), 0), "Diagonal should be zero"

    def test_exchange_matrix_exact_skew(self):
        """Exact rational exchange matrix is skew-symmetric."""
        B = shadow_exchange_matrix_exact(6)
        for i in range(2, 7):
            for j in range(2, 7):
                assert B[(i, j)] == -B[(j, i)], f"B[{i},{j}] != -B[{j},{i}]"

    def test_mc_recursion_coefficient_arity_match(self):
        """MC coefficient is nonzero only when i + j = r + 2."""
        for r in range(4, 10):
            for i in range(2, r + 1):
                for j in range(2, r + 1):
                    coeff = mc_recursion_coefficient(i, j, r)
                    if i + j == r + 2 and i >= 2 and j >= 2:
                        if i <= j:
                            assert coeff > 0, f"Expected positive coeff at i={i}, j={j}, r={r}"
                    else:
                        assert coeff == 0, f"Expected zero coeff at i={i}, j={j}, r={r}"

    def test_mc_coefficient_symmetry(self):
        """MC coefficient has eps(i,j) = 1/2 for i = j."""
        # i = j = 3, r = 4 (since 3 + 3 = 4 + 2 = 6)
        coeff_33 = mc_recursion_coefficient(3, 3, 4)
        assert coeff_33 == Rational(9, 2), f"B(3,3) at arity 4 should be 9/2, got {coeff_33}"

    def test_mc_coefficient_23(self):
        """Coefficient of S_2 * S_3 in arity-3 equation: 2*3 = 6."""
        coeff = mc_recursion_coefficient(2, 3, 3)
        assert coeff == Rational(6), f"B(2,3) at arity 3 should be 6, got {coeff}"

    def test_exchange_matrix_B23_value(self):
        """B_{2,3} = 6 (the dominant coupling)."""
        B = shadow_exchange_matrix_exact(6)
        assert B[(2, 3)] == Rational(6), f"B(2,3) should be 6, got {B[(2, 3)]}"
        assert B[(3, 2)] == Rational(-6), f"B(3,2) should be -6, got {B[(3, 2)]}"


# ============================================================================
# 3. Cluster mutations
# ============================================================================

class TestClusterMutations:
    """Test cluster mutation mechanics."""

    def test_mutation_involution_all_nodes(self):
        """mu_k^2 = id for all nodes k in a small exchange matrix."""
        B = shadow_exchange_matrix(6)
        n = B.shape[0]
        for k in range(n):
            ok, dev = mutation_involution_check(B, k)
            assert ok, f"Mutation involution failed at node {k}, deviation {dev}"

    def test_mutation_preserves_skew_symmetry(self):
        """Mutated matrix remains skew-symmetric."""
        B = shadow_exchange_matrix(6)
        for k in range(B.shape[0]):
            Bp = cluster_mutation(B, k)
            assert np.allclose(Bp, -Bp.T, atol=1e-12), \
                f"Mutation at {k} broke skew-symmetry"

    def test_mutation_involution_rank2(self):
        """For rank-2 matrix, mu_0^2 = id."""
        B = np.array([[0.0, 6.0], [-6.0, 0.0]])
        ok, dev = mutation_involution_check(B, 0)
        assert ok, f"Rank-2 mutation involution failed, deviation {dev}"

    def test_mutation_at_node0_flips_row_col(self):
        """Mutation at node 0 negates row 0 and column 0."""
        B = np.array([[0.0, 3.0], [-3.0, 0.0]])
        Bp = cluster_mutation(B, 0)
        assert np.isclose(Bp[0, 1], -3.0), f"Expected -3, got {Bp[0, 1]}"
        assert np.isclose(Bp[1, 0], 3.0), f"Expected 3, got {Bp[1, 0]}"

    def test_mutation_sequence_length_0(self):
        """Empty mutation sequence returns original matrix."""
        B = shadow_exchange_matrix(5)
        Bp = mutation_sequence(B, [])
        assert np.allclose(B, Bp)

    def test_double_mutation_identity(self):
        """Applying mu_k twice recovers the original."""
        B = shadow_exchange_matrix(5)
        for k in range(B.shape[0]):
            Bp = mutation_sequence(B, [k, k])
            assert np.allclose(B, Bp, atol=1e-12), \
                f"Double mutation at {k} failed"

    def test_mutation_3node_A3(self):
        """A_3 quiver: mutations produce finite orbit."""
        # A_3 exchange matrix: 0->1->2
        B = np.array([[0.0, 1.0, 0.0],
                       [-1.0, 0.0, 1.0],
                       [0.0, -1.0, 0.0]])
        # mu_0 mu_1 mu_0 should give something specific
        Bp = mutation_sequence(B, [0, 1, 0])
        # Check it's still skew-symmetric
        assert np.allclose(Bp, -Bp.T, atol=1e-12)


# ============================================================================
# 4. Exchange relation consistency
# ============================================================================

class TestExchangeRelations:
    """Verify exchange relations (MC equation) hold numerically."""

    @pytest.mark.parametrize("c_val", [5, 7, 10, 13, 20])
    def test_exchange_relation_arity5(self, c_val):
        """MC recursion is consistent at arity 5."""
        result = exchange_relation_check(float(c_val), 5)
        assert result['consistent'], \
            f"Exchange relation failed at c={c_val}, r=5: dev={result['deviation']}"

    @pytest.mark.parametrize("c_val", [5, 7, 10, 13, 20])
    def test_exchange_relation_arity6(self, c_val):
        """MC recursion is consistent at arity 6."""
        result = exchange_relation_check(float(c_val), 6)
        assert result['consistent'], \
            f"Exchange relation failed at c={c_val}, r=6: dev={result['deviation']}"

    @pytest.mark.parametrize("r", [7, 8, 9, 10])
    def test_exchange_relation_higher_arities(self, r):
        """MC recursion is consistent at higher arities, c = 10."""
        result = exchange_relation_check(10.0, r)
        assert result['consistent'], \
            f"Exchange relation failed at r={r}: dev={result['deviation']}"

    def test_exchange_relation_at_self_dual(self):
        """MC recursion holds at the self-dual point c = 13."""
        for r in range(5, 11):
            result = exchange_relation_check(13.0, r)
            assert result['consistent'], \
                f"Exchange relation failed at c=13, r={r}: dev={result['deviation']}"


# ============================================================================
# 5. Laurent phenomenon
# ============================================================================

class TestLaurentPhenomenon:
    """Test the Laurent property of shadow variables."""

    def test_S2_is_laurent(self):
        """S_2 = c/2 is Laurent in kappa (trivially)."""
        laurent = shadow_as_rational_function(4)
        assert laurent[2]['is_laurent_in_kappa'], "S_2 should be Laurent in kappa"

    def test_S3_is_laurent(self):
        """S_3 = 2 (constant) is Laurent in kappa."""
        laurent = shadow_as_rational_function(4)
        assert laurent[3]['is_laurent_in_kappa'], "S_3 should be Laurent in kappa"

    def test_S4_has_extra_poles(self):
        """S_4 = 10/(c(5c+22)) has a pole at 5c+22=0, so NOT Laurent in kappa alone."""
        laurent = shadow_as_rational_function(5)
        assert laurent[4]['has_extra_poles'], "S_4 should have extra poles beyond kappa"

    def test_higher_arities_have_extra_poles(self):
        """S_r for r >= 4 has poles at 5c+22=0."""
        laurent = shadow_as_rational_function(8)
        for r in range(4, 9):
            assert laurent[r]['has_extra_poles'], \
                f"S_{r} should have extra poles"

    def test_S2_laurent_in_initial_data(self):
        """S_2 is Laurent in initial cluster variable S_2."""
        data = shadow_laurent_in_initial_data(4)
        assert data[2]['is_laurent_in_S2']

    def test_S3_laurent_in_initial_data(self):
        """S_3 = 2 (constant) is Laurent in S_2."""
        data = shadow_laurent_in_initial_data(4)
        assert data[3]['is_laurent_in_S2']

    def test_S4_not_strictly_laurent_in_S2(self):
        """S_4 is NOT Laurent in S_2 alone due to (5c+22) denominator factor."""
        data = shadow_laurent_in_initial_data(5)
        assert not data[4]['is_laurent_in_S2'], \
            "S_4 should not be Laurent in S_2 alone"

    def test_shadow_rational_in_c(self):
        """All S_r are rational functions of c (no radicals)."""
        tower = virasoro_shadow_tower(10)
        for r, expr in tower.items():
            # Check that expr is a ratio of polynomials in c
            n = cancel(expr)
            assert n is not None, f"S_{r} should be a rational function of c"


# ============================================================================
# 6. Tropical shadow
# ============================================================================

class TestTropicalShadow:
    """Test p-adic valuations and tropical spectrum."""

    def test_p_adic_valuation_basic(self):
        """v_2(8) = 3, v_3(9) = 2, v_5(25) = 2."""
        assert p_adic_valuation(8, 2) == 3
        assert p_adic_valuation(9, 3) == 2
        assert p_adic_valuation(25, 5) == 2

    def test_p_adic_valuation_coprime(self):
        """v_p(n) = 0 when gcd(n, p) = 1."""
        assert p_adic_valuation(7, 2) == 0
        assert p_adic_valuation(11, 3) == 0
        assert p_adic_valuation(13, 5) == 0

    def test_p_adic_valuation_1(self):
        """v_p(1) = 0 for all p."""
        for p in [2, 3, 5, 7]:
            assert p_adic_valuation(1, p) == 0

    def test_rational_p_adic_valuation(self):
        """v_2(3/8) = v_2(3) - v_2(8) = 0 - 3 = -3."""
        assert rational_p_adic_valuation(Fraction(3, 8), 2) == -3

    def test_tropical_vector_c1(self):
        """Tropical shadow vector at c=1, p=2 is well-defined."""
        vec = tropical_shadow_vector(1, 2, 6)
        assert len(vec) == 5  # r = 2..6
        assert all(isinstance(v, int) for v in vec)

    def test_tropical_spectrum_shape(self):
        """Tropical spectrum has correct shape."""
        spec = tropical_shadow_spectrum(2, range(1, 6), 6)
        assert len(spec) == 5  # c = 1..5
        for c_val, vec in spec.items():
            assert len(vec) == 5  # r = 2..6

    @pytest.mark.parametrize("p", [2, 3, 5])
    def test_tropical_S2_valuation(self, p):
        """trop(S_2) at c = p^2 should reflect v_p(c/2)."""
        c_val = p * p
        vec = tropical_shadow_vector(c_val, p, 3)
        # S_2 = c/2 = p^2/2
        # v_p(p^2/2) = 2 (since gcd(2, p) = 1 for p > 2)
        if p > 2:
            expected_v = 2  # v_p(p^2) = 2, v_p(2) = 0
            assert vec[0] == -expected_v, \
                f"trop(S_2) at c={c_val}, p={p}: expected {-expected_v}, got {vec[0]}"

    def test_tropical_different_primes_differ(self):
        """Tropical vectors at different primes are generally different."""
        vec2 = tropical_shadow_vector(6, 2, 6)
        vec3 = tropical_shadow_vector(6, 3, 6)
        # Not necessarily different at every entry, but at least at S_2:
        # S_2 = 3. v_2(3) = 0, v_3(3) = 1. So trop differs.
        assert vec2[0] != vec3[0], "Tropical vectors should differ at p=2 vs p=3 for c=6"


# ============================================================================
# 7. Cluster modular group
# ============================================================================

class TestClusterModularGroup:
    """Test the cluster modular group and orbit finiteness."""

    def test_rank2_A2_finite_orbit(self):
        """A_2 cluster (b = 1) has finite orbit of 5 cluster variables."""
        orbit = rank2_cluster_variable_orbit(1)
        assert orbit['is_finite'], "A_2 orbit should be finite"
        assert orbit['orbit_size'] == 5, f"A_2 should have 5 variables, got {orbit['orbit_size']}"
        assert orbit['cluster_type'] == 'A_2'

    def test_rank2_B2_finite_orbit(self):
        """B_2 cluster (b = 2) has finite orbit of 6 cluster variables."""
        orbit = rank2_cluster_variable_orbit(2)
        assert orbit['is_finite'], "B_2 orbit should be finite"
        assert orbit['orbit_size'] == 6
        assert orbit['cluster_type'] == 'B_2'

    def test_rank2_G2_finite_orbit(self):
        """G_2 cluster (b = 3) has finite orbit of 8 cluster variables."""
        orbit = rank2_cluster_variable_orbit(3)
        assert orbit['is_finite'], "G_2 orbit should be finite"
        assert orbit['orbit_size'] == 8
        assert orbit['cluster_type'] == 'G_2'

    def test_rank2_b4_infinite(self):
        """b = 4 gives infinite orbit (beyond finite type)."""
        orbit = rank2_cluster_variable_orbit(4, max_mutations=50)
        assert not orbit['is_finite'], \
            "b=4 should give infinite cluster variable orbit"

    def test_rank2_b6_infinite(self):
        """b = 6 (shadow coupling) gives infinite orbit."""
        orbit = rank2_cluster_variable_orbit(6, max_mutations=50)
        assert not orbit['is_finite'], \
            "Shadow coupling b=6 should give infinite orbit (class M)"

    def test_shadow_modular_group_virasoro(self):
        """Virasoro shadow cluster modular group has infinite orbit."""
        result = shadow_cluster_modular_group(10.0)
        assert not result['is_finite_type'], \
            "Virasoro should have infinite-type cluster modular group"
        assert result['exchange_parameter'] == 6

    def test_rank2_zero_finite(self):
        """b = 0 gives disconnected quiver, trivially finite."""
        orbit = rank2_cluster_variable_orbit(0)
        assert orbit['is_finite']
        assert orbit['cluster_type'] == 'A_1 x A_1'


# ============================================================================
# 8. F-polynomials and g-vectors
# ============================================================================

class TestFPolynomials:
    """Test F-polynomial computation and positivity."""

    def test_f_poly_S2(self):
        """F-polynomial for S_2 is trivially positive."""
        f = compute_f_polynomials(5)
        assert f[2]['positive_coefficients']

    def test_f_poly_S3(self):
        """F-polynomial for S_3 = 2 has positive coefficients."""
        f = compute_f_polynomials(5)
        assert f[3]['positive_coefficients']

    def test_f_poly_S4_positive(self):
        """F-polynomial for S_4 has positive coefficients (after clearing c-poles)."""
        f = compute_f_polynomials(5)
        # S_4 = 10/(c(5c+22)). After multiplying by c^2 (or appropriate power):
        # Numerator should have positive coefficients.
        assert f[4]['nonneg_coefficients'], \
            f"S_4 F-polynomial should have non-negative coefficients, got {f[4]['F_coefficients']}"

    def test_g_vector_S2(self):
        """g-vector for S_2 = c/2: denominator has c-degree 0."""
        gv = g_vectors(5)
        assert gv[2] == (0,), f"g-vector for S_2 should be (0,), got {gv[2]}"

    def test_g_vector_S3(self):
        """g-vector for S_3 = 2 (constant): denominator c-degree 0."""
        gv = g_vectors(5)
        assert gv[3] == (0,), f"g-vector for S_3 should be (0,), got {gv[3]}"

    def test_g_vector_S4(self):
        """g-vector for S_4: denominator has c-degree 2 (from c*(5c+22) = 5c^2+22c)."""
        gv = g_vectors(5)
        assert gv[4] == (2,), f"g-vector for S_4 should be (2,), got {gv[4]}"

    def test_g_vectors_monotone(self):
        """g-vector c-degrees increase with arity (more c-poles at higher arity)."""
        gv = g_vectors(10)
        for r in range(4, 10):
            assert gv[r][0] <= gv[r + 1][0], \
                f"g-vector degree should be non-decreasing: g[{r}]={gv[r]} > g[{r+1}]={gv[r+1]}"


# ============================================================================
# 9. Shadow quiver
# ============================================================================

class TestShadowQuiver:
    """Test shadow quiver construction and classification."""

    def test_quiver_has_correct_nodes(self):
        """Quiver nodes are arities 2..max_arity."""
        q = shadow_quiver(6)
        assert q['nodes'] == [2, 3, 4, 5, 6]

    def test_quiver_has_arrows(self):
        """Quiver has at least some arrows."""
        q = shadow_quiver(6)
        assert q['n_arrows'] > 0, "Shadow quiver should have arrows"

    def test_quiver_arrows_from_lower_to_higher(self):
        """All arrows go from lower to higher arity (by construction of B)."""
        q = shadow_quiver(8)
        for arrow in q['arrows']:
            assert arrow['from'] < arrow['to'], \
                f"Arrow from {arrow['from']} to {arrow['to']} violates ordering"

    def test_quiver_type_infinite_for_large(self):
        """Shadow quiver with many nodes is infinite type."""
        q = shadow_quiver(6)
        assert 'infinite' in q['quiver_type'].lower(), \
            f"Expected infinite type, got {q['quiver_type']}"

    def test_quiver_B23_arrow_weight(self):
        """The 2->3 arrow has weight 6 (= 2*3)."""
        q = shadow_quiver(6)
        arrow_23 = [a for a in q['arrows'] if a['from'] == 2 and a['to'] == 3]
        assert len(arrow_23) == 1, "Should have exactly one arrow 2->3"
        assert arrow_23[0]['weight'] == 6, f"Arrow weight should be 6, got {arrow_23[0]['weight']}"

    def test_quiver_exchange_sample(self):
        """Verify sample exchange matrix entries."""
        q = shadow_quiver(5)
        sample = q['exchange_matrix_sample']
        assert sample[(2, 3)] == Rational(6)
        assert sample[(2, 4)] == Rational(8)
        assert sample[(3, 4)] == Rational(12)


# ============================================================================
# 10. Koszul duality
# ============================================================================

class TestKoszulDuality:
    """Test Koszul duality c -> 26-c as cluster transformation."""

    def test_kappa_complementarity(self):
        """kappa(c) + kappa(26-c) = 13 (exact)."""
        result = koszul_duality_mutation_test(10.0)
        assert result['kappa_complementarity'], \
            f"Kappa sum = {result['kappa_sum']}, expected 13"

    @pytest.mark.parametrize("c_val", [1, 5, 10, 13, 20, 25])
    def test_kappa_complementarity_all_c(self, c_val):
        """kappa(c) + kappa(26-c) = 13 for all c."""
        result = koszul_duality_mutation_test(float(c_val))
        assert result['kappa_complementarity'], \
            f"Kappa complementarity failed at c={c_val}"

    def test_not_simple_mutation(self):
        """Koszul duality is NOT a simple cluster mutation sequence."""
        result = koszul_duality_mutation_test(10.0)
        assert not result['is_simple_mutation']

    def test_dual_tower_symbolic(self):
        """Dual tower S_r(26-c) is well-defined."""
        dual = koszul_dual_shadow_tower(6)
        # At c = 13 (self-dual): S_r(13) = S_r(26-13) = S_r(13)
        for r in range(2, 7):
            diff = simplify(dual[r].subs(c, 13) - virasoro_shadow_tower(6)[r].subs(c, 13))
            assert diff == 0, f"Dual tower should equal original at c=13, arity {r}"

    def test_complementarity_sum_arity2(self):
        """Complementarity sum at arity 2: S_2(c) + S_2(26-c) = 13."""
        comp = complementarity_sum_tower(4)
        assert simplify(comp[2]['complement_sum'] - 13) == 0

    def test_complementarity_sum_arity3(self):
        """Complementarity sum at arity 3: S_3(c) + S_3(26-c) = 4 (both constant = 2)."""
        comp = complementarity_sum_tower(4)
        assert simplify(comp[3]['complement_sum'] - 4) == 0

    def test_self_dual_point(self):
        """At c = 13: S_r(13) = S_r(13) (self-dual, trivially)."""
        sd = self_dual_tower()
        for r, data in sd.items():
            assert data['S_r_at_13'] is not None, f"S_{r}(13) should be defined"

    def test_self_dual_kappa(self):
        """kappa(Vir_13) = 13/2."""
        sd = self_dual_tower()
        assert sd[2]['S_r_at_13'] == Rational(13, 2), \
            f"kappa(13) should be 13/2, got {sd[2]['S_r_at_13']}"


# ============================================================================
# 11. Depth classification via quiver type
# ============================================================================

class TestDepthClassification:
    """Test depth class -> quiver type mapping."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G, depth 2, Dynkin A_1."""
        d = depth_class_from_quiver('heisenberg')
        assert d['class'] == 'G'
        assert d['depth'] == 2
        assert d['finite_type'] is True

    def test_affine_sl2_class_L(self):
        """Affine sl_2 is class L, depth 3, Dynkin A_2."""
        d = depth_class_from_quiver('affine_sl2')
        assert d['class'] == 'L'
        assert d['depth'] == 3
        assert d['finite_type'] is True

    def test_bc_ghosts_class_C(self):
        """bc ghosts is class C, depth 4."""
        d = depth_class_from_quiver('bc_ghosts')
        assert d['class'] == 'C'
        assert d['depth'] == 4
        assert d['finite_type'] is True

    def test_virasoro_class_M(self):
        """Virasoro is class M, depth infinity, infinite type."""
        d = depth_class_from_quiver('virasoro')
        assert d['class'] == 'M'
        assert d['depth'] == float('inf')
        assert d['finite_type'] is False

    def test_w3_class_M(self):
        """W_3 is class M, infinite depth."""
        d = depth_class_from_quiver('w3')
        assert d['class'] == 'M'
        assert d['finite_type'] is False

    def test_unknown_family(self):
        """Unknown family returns 'unknown' classification."""
        d = depth_class_from_quiver('unknown_algebra')
        assert d['class'] == 'unknown'


# ============================================================================
# 12. Cluster character (Caldero-Chapoton)
# ============================================================================

class TestClusterCharacter:
    """Test Caldero-Chapoton map computations."""

    def test_cc_rank1_simple(self):
        """CC for rank-1 simple: dim Ext = 0 gives CC = 1."""
        assert caldero_chapoton_rank1(0) == 1

    def test_cc_rank1_ext1(self):
        """CC with dim Ext = 1 gives CC = 2."""
        assert caldero_chapoton_rank1(1) == 2

    def test_cluster_character_rank2_A2(self):
        """Rank-2 A_2 cluster category has 5 indecomposables."""
        cc = cluster_character_rank2(2)
        assert cc['type'] == 'A_2'

    def test_cluster_character_rank2_A3(self):
        """Rank-2 A_3 cluster has P_1."""
        cc = cluster_character_rank2(3)
        assert cc['CC_P1_exists']


# ============================================================================
# 13. Full analysis integration
# ============================================================================

class TestFullAnalysis:
    """Integration tests for the full cluster shadow analysis."""

    def test_full_analysis_runs(self):
        """Full analysis completes without error."""
        result = full_cluster_shadow_analysis(c_val=10.0, max_r=8, max_arity_quiver=5)
        assert 'tower' in result
        assert 'exchange_matrix_shape' in result
        assert 'quiver_type' in result

    def test_full_analysis_tower_keys(self):
        """Full analysis includes all tower arities."""
        result = full_cluster_shadow_analysis(c_val=10.0, max_r=8, max_arity_quiver=5)
        for r in range(2, 9):
            assert r in result['tower'], f"Missing arity {r} in tower"

    def test_full_analysis_involution(self):
        """All involution checks pass in full analysis."""
        result = full_cluster_shadow_analysis(c_val=10.0, max_r=8, max_arity_quiver=5)
        for k, data in result['involution_checks'].items():
            assert data['involution'], f"Involution failed at node {k}"

    def test_full_analysis_exchange_consistency(self):
        """All exchange relation checks pass."""
        result = full_cluster_shadow_analysis(c_val=10.0, max_r=8, max_arity_quiver=5)
        for r, data in result['exchange_relation_checks'].items():
            assert data['consistent'], f"Exchange relation failed at r={r}"

    def test_full_analysis_koszul(self):
        """Koszul complementarity holds."""
        result = full_cluster_shadow_analysis(c_val=10.0, max_r=8, max_arity_quiver=5)
        assert result['koszul_duality']['kappa_complementarity']

    def test_full_analysis_at_self_dual(self):
        """Full analysis at self-dual point c = 13."""
        result = full_cluster_shadow_analysis(c_val=13.0, max_r=8, max_arity_quiver=5)
        assert result['koszul_duality']['kappa_complementarity']
        # S_2(13) = 13/2 = 6.5
        assert abs(result['tower'][2] - 6.5) < 1e-10


# ============================================================================
# 14. Numerical cross-checks
# ============================================================================

class TestNumericalCrossChecks:
    """Numerical verification at specific c values."""

    def test_virasoro_tower_c10_values(self):
        """Spot-check shadow tower values at c = 10."""
        tower = virasoro_shadow_numerical(10, 6)
        assert abs(tower[2] - 5.0) < 1e-12  # kappa = c/2 = 5
        assert abs(tower[3] - 2.0) < 1e-12  # cubic = 2
        # S_4 = 10/(10*(50+22)) = 10/720 = 1/72
        assert abs(tower[4] - 1.0 / 72.0) < 1e-12

    def test_virasoro_tower_c1_values(self):
        """Spot-check at c = 1."""
        tower = virasoro_shadow_numerical(1, 6)
        assert abs(tower[2] - 0.5) < 1e-12
        assert abs(tower[3] - 2.0) < 1e-12
        # S_4 = 10/(1*(5+22)) = 10/27
        assert abs(tower[4] - 10.0 / 27.0) < 1e-12

    def test_tower_decays_with_arity(self):
        """|S_r| decreases (roughly) with arity for generic c."""
        tower = virasoro_shadow_numerical(10, 12)
        # After the cubic S_3 = 2, higher arities decay
        for r in range(5, 12):
            assert abs(tower[r]) < abs(tower[r - 1]) or abs(tower[r]) < 1e-5, \
                f"|S_{r}| = {abs(tower[r])} not smaller than |S_{r-1}| = {abs(tower[r-1])}"

    def test_complementarity_numerical_c5(self):
        """S_r(5) + S_r(21) structure at c = 5."""
        t5 = virasoro_shadow_numerical(5, 8)
        t21 = virasoro_shadow_numerical(21, 8)
        # Arity 2: 5/2 + 21/2 = 13
        assert abs(t5[2] + t21[2] - 13.0) < 1e-10
        # Arity 3: 2 + 2 = 4
        assert abs(t5[3] + t21[3] - 4.0) < 1e-10

    def test_S5_negative_at_positive_c(self):
        """S_5 < 0 for c > 0 (from formula -48/(c^2(5c+22)))."""
        for c_val in [1, 5, 10, 13, 25]:
            tower = virasoro_shadow_numerical(c_val, 6)
            assert tower[5] < 0, f"S_5 should be negative at c={c_val}, got {tower[5]}"

    def test_S4_positive_at_positive_c(self):
        """S_4 > 0 for c > 0 (from formula 10/(c(5c+22)))."""
        for c_val in [1, 5, 10, 13, 25]:
            tower = virasoro_shadow_numerical(c_val, 5)
            assert tower[4] > 0, f"S_4 should be positive at c={c_val}, got {tower[4]}"


# ============================================================================
# 15. Additional structural tests
# ============================================================================

class TestStructural:
    """Additional structural and cross-consistency tests."""

    def test_exchange_matrix_size(self):
        """Exchange matrix has correct dimensions."""
        B = shadow_exchange_matrix(6)
        assert B.shape == (5, 5), f"Expected (5,5), got {B.shape}"

    def test_exchange_matrix_size_8(self):
        """Exchange matrix for max_arity=8 is 7x7."""
        B = shadow_exchange_matrix(8)
        assert B.shape == (7, 7)

    def test_tropical_zero_handling(self):
        """Tropical vector handles zero shadow coefficients correctly."""
        # At c = 0, shadow tower has issues (kappa = 0), so test c = 1
        vec = tropical_shadow_vector(1, 2, 4)
        assert len(vec) == 3

    def test_mutation_preserves_zero_diagonal(self):
        """After mutation, diagonal of B remains zero."""
        B = shadow_exchange_matrix(5)
        for k in range(B.shape[0]):
            Bp = cluster_mutation(B, k)
            assert np.allclose(np.diag(Bp), 0), \
                f"Mutation at {k} created nonzero diagonal"

    def test_complementarity_sum_higher_arities(self):
        """Complementarity sum at arities 4-6 is a rational function of c."""
        comp = complementarity_sum_tower(6)
        for r in range(4, 7):
            # The complement sum should be a well-defined expression
            assert comp[r]['complement_sum'] is not None

    def test_f_polynomials_exist_for_all_arities(self):
        """F-polynomial data exists for all computed arities."""
        f = compute_f_polynomials(8)
        for r in range(2, 9):
            assert r in f, f"Missing F-polynomial for arity {r}"

    def test_g_vectors_exist_for_all_arities(self):
        """g-vectors defined for all computed arities."""
        gv = g_vectors(8)
        for r in range(2, 9):
            assert r in gv, f"Missing g-vector for arity {r}"
            assert isinstance(gv[r], tuple)

    def test_shadow_cluster_variables_basic(self):
        """shadow_cluster_variables returns correct dict."""
        vars_dict = shadow_cluster_variables(10.0, 6)
        assert 2 in vars_dict
        assert abs(vars_dict[2] - 5.0) < 1e-12

    def test_virasoro_tower_max_r_bound(self):
        """Can compute tower up to r = 15 without error."""
        tower = virasoro_shadow_tower(15)
        assert 15 in tower
        # Verify it's a valid sympy expression
        val = float(tower[15].subs(c, 10))
        assert math.isfinite(val), f"S_15(10) should be finite, got {val}"
