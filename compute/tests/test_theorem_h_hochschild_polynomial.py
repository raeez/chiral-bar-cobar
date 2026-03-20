"""Tests for Theorem H: Hochschild polynomial growth.

Verifies both regimes of Theorem H across all standard families:

REGIME 1 (quadratic Koszul): concentration in [0,2], polynomial P_A(t)
  of degree <= 2, Koszul duality, palindromicity.

REGIME 2 (W-algebra polynomial ring): ChirHoch* = C[Theta_1,...,Theta_r],
  periodicity (rank 1), quasi-periodicity (rank >= 2), polynomial growth.

References:
  thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
  thm:w-algebra-hochschild (hochschild_cohomology.tex)
  thm:virasoro-hochschild (hochschild_cohomology.tex)
  thm:main-koszul-hoch (chiral_hochschild_koszul.tex)
"""

import pytest
from math import comb

from compute.lib.theorem_h_hochschild_polynomial import (
    FAMILY_DATA,
    THEOREM_H_STATUS,
    generator_count,
    hochschild_poincare,
    hochschild_betti,
    hochschild_euler_char,
    hochschild_total_dim,
    quadratic_poincare_polynomial,
    quadratic_hochschild_betti,
    quadratic_euler_char,
    quadratic_total_dim,
    w_algebra_gen_degrees,
    w_algebra_hochschild_dim,
    w_algebra_quasi_period,
    w_algebra_growth_rate,
    w_algebra_poincare_series,
    verify_concentration,
    verify_palindromicity,
    verify_koszul_duality_hochschild,
    verify_theorem_h,
    verify_theorem_h_all_families,
    koszul_dual_polynomial,
    hochschild_spectral_sequence,
    exterior_algebra_verification,
    non_koszul_failure_example,
    affine_slN_data,
    wN_data,
    lattice_data,
    virasoro_hochschild_dims,
    virasoro_periodicity_check,
    w3_hochschild_dims,
    w3_quasi_periodicity_check,
    lcm_list,
)


# ===================================================================
# Regime 1: Quadratic Koszul — Heisenberg
# ===================================================================

class TestHeisenberg:
    """Theorem H for the Heisenberg algebra (1 generator, weight 1)."""

    def test_generator_count(self):
        assert generator_count('heisenberg') == 1

    def test_poincare_polynomial(self):
        """P(t) = 1 + t + t^2."""
        poly = hochschild_poincare('heisenberg')
        assert poly == [1, 1, 1]

    def test_betti_0(self):
        """ChirHoch^0 = C (center)."""
        assert hochschild_betti('heisenberg', 0) == 1

    def test_betti_1(self):
        """ChirHoch^1 = C (the current alpha(z))."""
        assert hochschild_betti('heisenberg', 1) == 1

    def test_betti_2(self):
        """ChirHoch^2 = C (level deformation)."""
        assert hochschild_betti('heisenberg', 2) == 1

    def test_concentration_positive(self):
        """ChirHoch^n = 0 for n > 2."""
        for n in range(3, 10):
            assert hochschild_betti('heisenberg', n) == 0

    def test_concentration_negative(self):
        """ChirHoch^n = 0 for n < 0."""
        for n in range(-5, 0):
            assert hochschild_betti('heisenberg', n) == 0

    def test_euler_char(self):
        """chi = 1 - 1 + 1 = 1."""
        assert hochschild_euler_char('heisenberg') == 1

    def test_total_dim(self):
        """P(1) = 1 + 1 + 1 = 3."""
        assert hochschild_total_dim('heisenberg') == 3

    def test_palindromicity(self):
        """dim H^0 = dim H^2 = 1."""
        result = verify_palindromicity('heisenberg')
        assert result['palindromic_self'] is True


# ===================================================================
# Regime 1: Quadratic Koszul — Affine sl_2
# ===================================================================

class TestAffineSl2:
    """Theorem H for affine sl_2 (3 generators, all weight 1)."""

    def test_generator_count(self):
        assert generator_count('affine_sl2') == 3

    def test_poincare_polynomial(self):
        """P(t) = 1 + 3t + t^2."""
        poly = hochschild_poincare('affine_sl2')
        assert poly == [1, 3, 1]

    def test_betti_0(self):
        """ChirHoch^0 = C (center at generic level)."""
        assert hochschild_betti('affine_sl2', 0) == 1

    def test_betti_1(self):
        """ChirHoch^1 = C^3 = sl_2 (outer derivations)."""
        assert hochschild_betti('affine_sl2', 1) == 3

    def test_betti_2(self):
        """ChirHoch^2 = C (level deformation)."""
        assert hochschild_betti('affine_sl2', 2) == 1

    def test_concentration(self):
        """ChirHoch^n = 0 for n > 2."""
        for n in range(3, 8):
            assert hochschild_betti('affine_sl2', n) == 0

    def test_euler_char(self):
        """chi = 1 - 3 + 1 = -1."""
        assert hochschild_euler_char('affine_sl2') == -1

    def test_total_dim(self):
        """P(1) = 1 + 3 + 1 = 5."""
        assert hochschild_total_dim('affine_sl2') == 5


# ===================================================================
# Regime 1: Quadratic Koszul — Affine sl_3
# ===================================================================

class TestAffineSl3:
    """Theorem H for affine sl_3 (8 generators)."""

    def test_generator_count(self):
        assert generator_count('affine_sl3') == 8

    def test_poincare_polynomial(self):
        """P(t) = 1 + 8t + t^2."""
        poly = hochschild_poincare('affine_sl3')
        assert poly == [1, 8, 1]

    def test_betti_1_equals_dim_g(self):
        """ChirHoch^1 = g = sl_3 has dimension 8."""
        assert hochschild_betti('affine_sl3', 1) == 8

    def test_euler_char(self):
        """chi = 1 - 8 + 1 = -6."""
        assert hochschild_euler_char('affine_sl3') == -6


# ===================================================================
# Regime 1: Quadratic Koszul — betagamma
# ===================================================================

class TestBetagamma:
    """Theorem H for the betagamma system (2 generators)."""

    def test_generator_count(self):
        assert generator_count('betagamma') == 2

    def test_poincare_polynomial(self):
        """P(t) = 1 + 2t + t^2."""
        poly = hochschild_poincare('betagamma')
        assert poly == [1, 2, 1]

    def test_betti_1(self):
        """ChirHoch^1 = C^2 (two generators)."""
        assert hochschild_betti('betagamma', 1) == 2

    def test_concentration(self):
        for n in range(3, 8):
            assert hochschild_betti('betagamma', n) == 0

    def test_palindromic(self):
        """dim H^0 = dim H^2 = 1."""
        result = verify_palindromicity('betagamma')
        assert result['palindromic_self'] is True


# ===================================================================
# Regime 1: Quadratic Koszul — bc ghosts
# ===================================================================

class TestBcGhosts:
    """Theorem H for the bc ghost system (2 generators, Koszul dual of betagamma)."""

    def test_generator_count(self):
        assert generator_count('bc_ghosts') == 2

    def test_poincare_polynomial(self):
        """P(t) = 1 + 2t + t^2 (same as betagamma by Koszul duality)."""
        poly = hochschild_poincare('bc_ghosts')
        assert poly == [1, 2, 1]

    def test_dual_matches_betagamma(self):
        """betagamma and bc have the same Poincare polynomial."""
        poly_bg = hochschild_poincare('betagamma')
        poly_bc = hochschild_poincare('bc_ghosts')
        assert poly_bg == poly_bc


# ===================================================================
# Regime 1: Quadratic Koszul — Free fermion
# ===================================================================

class TestFreeFermion:
    """Theorem H for the free fermion (1 fermionic generator)."""

    def test_generator_count(self):
        assert generator_count('free_fermion') == 1

    def test_poincare_polynomial(self):
        """P(t) = 1 + t + t^2."""
        poly = hochschild_poincare('free_fermion')
        assert poly == [1, 1, 1]


# ===================================================================
# Regime 1: Parametric — Affine sl_N
# ===================================================================

class TestAffineSLN:
    """Theorem H for affine sl_N (N^2 - 1 generators)."""

    @pytest.mark.parametrize("N,expected_gen", [
        (2, 3), (3, 8), (4, 15), (5, 24), (6, 35), (10, 99),
    ])
    def test_generator_count(self, N, expected_gen):
        assert generator_count('affine_slN', N=N) == expected_gen

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_poincare_formula(self, N):
        """P(t) = 1 + (N^2-1)t + t^2."""
        data = affine_slN_data(N)
        assert data['poincare'] == [1, N*N - 1, 1]

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_euler_char(self, N):
        """chi = 2 - (N^2-1) = 3 - N^2."""
        data = affine_slN_data(N)
        assert data['euler_char'] == 3 - N * N

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_total_dim(self, N):
        """P(1) = 2 + (N^2-1) = N^2 + 1."""
        data = affine_slN_data(N)
        assert data['total_dim'] == N * N + 1


# ===================================================================
# Regime 1: Parametric — Lattice VOAs
# ===================================================================

class TestLattice:
    """Theorem H for lattice VOAs of rank r."""

    @pytest.mark.parametrize("r", [1, 2, 3, 4, 8, 24])
    def test_poincare_formula(self, r):
        """P(t) = 1 + r*t + t^2."""
        data = lattice_data(r)
        assert data['poincare'] == [1, r, 1]

    def test_rank_1_matches_heisenberg(self):
        """Rank-1 lattice has same polynomial as Heisenberg."""
        data = lattice_data(1)
        poly_h = hochschild_poincare('heisenberg')
        assert data['poincare'] == poly_h

    @pytest.mark.parametrize("r", [1, 2, 8, 24])
    def test_euler_char(self, r):
        data = lattice_data(r)
        assert data['euler_char'] == 2 - r

    def test_leech_lattice(self):
        """Leech lattice: rank 24, P(t) = 1 + 24t + t^2."""
        data = lattice_data(24)
        assert data['poincare'] == [1, 24, 1]
        assert data['total_dim'] == 26


# ===================================================================
# Regime 2: W-algebra — Virasoro
# ===================================================================

class TestVirasoro:
    """Theorem H for the Virasoro algebra (W-algebra regime)."""

    def test_generator_count(self):
        assert generator_count('virasoro') == 1

    def test_hochschild_dim_even(self):
        """ChirHoch^{2k} = C for all k >= 0."""
        for k in range(15):
            assert hochschild_betti('virasoro', 2*k) == 1

    def test_hochschild_dim_odd(self):
        """ChirHoch^{2k+1} = 0 for all k >= 0."""
        for k in range(15):
            assert hochschild_betti('virasoro', 2*k + 1) == 0

    def test_periodicity(self):
        """2-periodicity: ChirHoch^{n+2} = ChirHoch^n."""
        result = virasoro_periodicity_check(30)
        assert result['passed'] is True
        assert result['period'] == 2

    def test_h0_is_center(self):
        """ChirHoch^0(Vir_c) = C (center)."""
        assert hochschild_betti('virasoro', 0) == 1

    def test_h1_vanishes(self):
        """ChirHoch^1(Vir_c) = 0 (no outer derivations at generic c)."""
        assert hochschild_betti('virasoro', 1) == 0

    def test_h2_is_gelfand_fuchs(self):
        """ChirHoch^2(Vir_c) = C (Gelfand-Fuchs 2-cocycle Theta)."""
        assert hochschild_betti('virasoro', 2) == 1

    def test_virasoro_dims_function(self):
        dims = virasoro_hochschild_dims(10)
        expected = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        assert dims == expected

    def test_total_dim_infinite(self):
        """Total dimension is infinite for W-algebra regime."""
        assert hochschild_total_dim('virasoro') is None


# ===================================================================
# Regime 2: W-algebra — W_3
# ===================================================================

class TestW3:
    """Theorem H for W_3 = W^k(sl_3) (2 generators, weights 2 and 3)."""

    def test_generator_count(self):
        assert generator_count('w3') == 2

    def test_gen_degrees(self):
        """Generators have degrees 2 and 3."""
        assert w_algebra_gen_degrees('A', 2) == [2, 3]

    def test_quasi_period(self):
        """Quasi-period = lcm(2, 3) = 6."""
        assert w_algebra_quasi_period([2, 3]) == 6

    def test_first_13_dims(self):
        """Known dimensions for n = 0..12."""
        dims = w3_hochschild_dims(12)
        # #{(a,b): 2a+3b = n}
        expected = [1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3]
        assert dims == expected

    def test_h0(self):
        assert hochschild_betti('w3', 0) == 1

    def test_h1(self):
        assert hochschild_betti('w3', 1) == 0

    def test_h2(self):
        """ChirHoch^2 = C (the Theta_1 class)."""
        assert hochschild_betti('w3', 2) == 1

    def test_h3(self):
        """ChirHoch^3 = C (the Theta_2 class)."""
        assert hochschild_betti('w3', 3) == 1

    def test_h6(self):
        """ChirHoch^6 = C^2 (Theta_1^3 and Theta_2^2)."""
        assert hochschild_betti('w3', 6) == 2

    def test_quasi_periodicity(self):
        result = w3_quasi_periodicity_check(60)
        assert result['quasi_period'] == 6
        assert result['linear_growth'] is True

    def test_total_dim_infinite(self):
        assert hochschild_total_dim('w3') is None


# ===================================================================
# Regime 2: W-algebra — W_N parametric
# ===================================================================

class TestWN:
    """Theorem H for W_N = W^k(sl_N)."""

    @pytest.mark.parametrize("N,expected_rank", [
        (2, 1), (3, 2), (4, 3), (5, 4), (10, 9),
    ])
    def test_rank(self, N, expected_rank):
        assert generator_count('wN', N=N) == expected_rank

    @pytest.mark.parametrize("N,expected_degrees", [
        (2, [2]), (3, [2, 3]), (4, [2, 3, 4]), (5, [2, 3, 4, 5]),
    ])
    def test_gen_degrees(self, N, expected_degrees):
        assert w_algebra_gen_degrees('A', N - 1) == expected_degrees

    @pytest.mark.parametrize("N,expected_qp", [
        (2, 2), (3, 6), (4, 12), (5, 60), (6, 60),
    ])
    def test_quasi_period(self, N, expected_qp):
        gen_degrees = w_algebra_gen_degrees('A', N - 1)
        assert w_algebra_quasi_period(gen_degrees) == expected_qp

    def test_w4_first_dims(self):
        """W_4: generators of weights 2, 3, 4. Check first dims."""
        dims = w_algebra_poincare_series([2, 3, 4], 12)
        # #{(a,b,c): 2a+3b+4c = n}
        expected = [1, 0, 1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 7]
        assert dims == expected

    def test_w5_first_dims(self):
        """W_5: generators of weights 2, 3, 4, 5."""
        dims = w_algebra_poincare_series([2, 3, 4, 5], 10)
        expected = [1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7]
        assert dims == expected

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro. Check agreement."""
        dims_w2 = w_algebra_poincare_series([2], 20)
        dims_vir = virasoro_hochschild_dims(20)
        assert dims_w2 == dims_vir


# ===================================================================
# W-algebra: detailed weighted partition counts
# ===================================================================

class TestWeightedPartitions:
    """Verify w_algebra_hochschild_dim against hand computations."""

    def test_single_gen_weight_2(self):
        """C[Theta] with |Theta| = 2: 1 if n even, 0 if n odd."""
        for n in range(20):
            expected = 1 if n % 2 == 0 else 0
            assert w_algebra_hochschild_dim([2], n) == expected

    def test_single_gen_weight_3(self):
        """C[Theta] with |Theta| = 3: 1 if 3|n, 0 otherwise."""
        for n in range(21):
            expected = 1 if n % 3 == 0 else 0
            assert w_algebra_hochschild_dim([3], n) == expected

    def test_two_gens_2_3_at_6(self):
        """2a + 3b = 6: (a,b) = (3,0), (0,2) => dim = 2."""
        assert w_algebra_hochschild_dim([2, 3], 6) == 2

    def test_two_gens_2_3_at_12(self):
        """2a + 3b = 12: (a,b) = (6,0), (3,2), (0,4) => dim = 3."""
        assert w_algebra_hochschild_dim([2, 3], 12) == 3

    def test_three_gens_at_0(self):
        """Any number of generators: dim ChirHoch^0 = 1."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5]]:
            assert w_algebra_hochschild_dim(gen_degrees, 0) == 1

    def test_negative_degree(self):
        """dim ChirHoch^n = 0 for n < 0."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4]]:
            for n in range(-5, 0):
                assert w_algebra_hochschild_dim(gen_degrees, n) == 0


# ===================================================================
# Growth rate
# ===================================================================

class TestGrowthRate:
    """Verify polynomial growth rate asymptotics."""

    def test_virasoro_bounded(self):
        """Virasoro: rank 1, bounded dims (0 or 1)."""
        rate = w_algebra_growth_rate([2])
        assert rate == 0.5  # 1/(2 * 0!) = 1/2

    def test_w3_linear(self):
        """W_3: rank 2, linear growth ~ n/(2*3) = n/6."""
        rate = w_algebra_growth_rate([2, 3])
        assert abs(rate - 1.0 / 6) < 1e-12

    def test_w4_quadratic(self):
        """W_4: rank 3, quadratic growth ~ n^2/(2*3*4*2) = n^2/48."""
        rate = w_algebra_growth_rate([2, 3, 4])
        assert abs(rate - 1.0 / 48) < 1e-12

    def test_asymptotic_accuracy_w3(self):
        """Verify that dim ChirHoch^n ~ n/6 for large n."""
        gen_degrees = [2, 3]
        n = 600
        dim_n = w_algebra_hochschild_dim(gen_degrees, n)
        expected = n / 6.0
        assert abs(dim_n / expected - 1.0) < 0.05


# ===================================================================
# Concentration verification
# ===================================================================

class TestConcentration:
    """Verify concentration for all quadratic families."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'affine_sl3',
        'betagamma', 'bc_ghosts', 'free_fermion',
    ])
    def test_quadratic_concentration(self, family):
        result = verify_concentration(family)
        assert result['passed'] is True

    def test_virasoro_no_concentration(self):
        """Virasoro is NOT concentrated in [0,2]: ChirHoch^4 = 1."""
        result = verify_concentration('virasoro')
        assert result['details'].get('unbounded') is True

    def test_w3_no_concentration(self):
        """W_3 is NOT concentrated in [0,2]."""
        result = verify_concentration('w3')
        assert result['details'].get('unbounded') is True


# ===================================================================
# Palindromicity
# ===================================================================

class TestPalindromicity:
    """Verify palindromicity of the quadratic Poincare polynomial."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'affine_sl3',
        'betagamma', 'bc_ghosts', 'free_fermion',
    ])
    def test_palindromic(self, family):
        """All quadratic families have dim Z(A) = dim Z(A^!) = 1."""
        result = verify_palindromicity(family)
        assert result['palindromic_self'] is True

    def test_w_algebra_not_applicable(self):
        """Palindromicity in strict sense does not apply to W-algebras."""
        result = verify_palindromicity('virasoro')
        assert result['passed'] is None


# ===================================================================
# Koszul duality on Hochschild
# ===================================================================

class TestKoszulDuality:
    """Verify Koszul duality relations on ChirHoch."""

    def test_betagamma_bc_duality(self):
        """betagamma and bc are Koszul duals with same polynomial."""
        result = verify_koszul_duality_hochschild('betagamma')
        assert result['passed'] is True

    def test_heisenberg_duality(self):
        result = verify_koszul_duality_hochschild('heisenberg')
        assert result['passed'] is True

    def test_affine_sl2_duality(self):
        result = verify_koszul_duality_hochschild('affine_sl2')
        assert result['passed'] is True


# ===================================================================
# Koszul dual polynomial
# ===================================================================

class TestKoszulDualPolynomial:
    """Verify P_{A^!}(t)."""

    def test_heisenberg_dual_poly(self):
        """P_{H^!}(t) = 1 + t + t^2 (reversed roles of Z(A) and Z(A^!))."""
        dual_poly = koszul_dual_polynomial('heisenberg')
        assert dual_poly == [1, 1, 1]

    def test_betagamma_dual_poly(self):
        """P_{bg^!}(t) = P_{bc}(t) = 1 + 2t + t^2."""
        dual_poly = koszul_dual_polynomial('betagamma')
        assert dual_poly == [1, 2, 1]

    def test_affine_sl2_dual_poly(self):
        """P_{sl2^!}(t) = 1 + 3t + t^2."""
        dual_poly = koszul_dual_polynomial('affine_sl2')
        assert dual_poly == [1, 3, 1]

    def test_w_algebra_returns_none(self):
        """Koszul dual polynomial not defined for W-algebra regime."""
        assert koszul_dual_polynomial('virasoro') is None


# ===================================================================
# Spectral sequence
# ===================================================================

class TestSpectralSequence:
    """Verify the Hochschild spectral sequence collapses at E_2."""

    def test_heisenberg_e2(self):
        E2 = hochschild_spectral_sequence('heisenberg', max_p=4, max_q=3)
        # E_2^{p,0} = ChirHoch^p, all others zero
        assert E2[0][0] == 1
        assert E2[1][0] == 1
        assert E2[2][0] == 1
        assert E2[3][0] == 0
        for p in range(5):
            for q in range(1, 4):
                assert E2[p][q] == 0

    def test_virasoro_e2(self):
        E2 = hochschild_spectral_sequence('virasoro', max_p=6, max_q=3)
        assert E2[0][0] == 1
        assert E2[1][0] == 0
        assert E2[2][0] == 1
        assert E2[3][0] == 0
        assert E2[4][0] == 1
        for p in range(7):
            for q in range(1, 4):
                assert E2[p][q] == 0


# ===================================================================
# Exterior algebra verification
# ===================================================================

class TestExteriorAlgebra:
    """Verify the exterior algebra structure for quadratic Koszul."""

    def test_heisenberg(self):
        result = exterior_algebra_verification('heisenberg')
        assert result['passed'] is True
        assert result['n_generators'] == 1

    def test_affine_sl2(self):
        result = exterior_algebra_verification('affine_sl2')
        assert result['passed'] is True
        assert result['n_generators'] == 3

    def test_betagamma(self):
        result = exterior_algebra_verification('betagamma')
        assert result['passed'] is True

    def test_w_algebra_not_applicable(self):
        result = exterior_algebra_verification('virasoro')
        assert result['passed'] is None


# ===================================================================
# Non-Koszul failure
# ===================================================================

class TestNonKoszul:
    """Verify structural prediction for non-Koszul algebras."""

    def test_failure_example_exists(self):
        result = non_koszul_failure_example()
        assert 'admissible' in result['description']
        assert result['known_data']['ChirHoch^0'] == 1

    def test_l_minus_half_sl2_data(self):
        """L_{-1/2}(sl_2): concentrated in [0,2] despite being admissible."""
        result = non_koszul_failure_example()
        assert result['known_data']['ChirHoch^1'] == 0
        assert result['known_data']['ChirHoch^2'] == 1


# ===================================================================
# Full verification
# ===================================================================

class TestFullVerification:
    """Run verify_theorem_h for all families."""

    def test_heisenberg_passes(self):
        result = verify_theorem_h('heisenberg')
        assert result['passed'] is True

    def test_affine_sl2_passes(self):
        result = verify_theorem_h('affine_sl2')
        assert result['passed'] is True

    def test_betagamma_passes(self):
        result = verify_theorem_h('betagamma')
        assert result['passed'] is True

    def test_virasoro_passes(self):
        result = verify_theorem_h('virasoro')
        assert result['passed'] is True

    def test_w3_passes(self):
        result = verify_theorem_h('w3')
        assert result['passed'] is True

    def test_all_families_pass(self):
        results = verify_theorem_h_all_families()
        for family, result in results.items():
            assert result['passed'] is True, f"{family} failed"

    def test_all_families_count(self):
        """At least 10 families verified."""
        results = verify_theorem_h_all_families()
        assert len(results) >= 10


# ===================================================================
# Status dictionary consistency
# ===================================================================

class TestStatusDictionary:
    """Verify THEOREM_H_STATUS is consistent with computations."""

    def test_all_proved(self):
        """All families in the status dictionary are PROVED."""
        for family, info in THEOREM_H_STATUS.items():
            assert info['status'] == 'PROVED', f"{family} not proved"

    def test_quadratic_polynomials_match(self):
        """Quadratic families: stored polynomial matches computation."""
        for family in ['heisenberg', 'affine_sl2', 'affine_sl3',
                        'betagamma', 'bc_ghosts', 'free_fermion']:
            stored = THEOREM_H_STATUS[family]['poincare']
            computed = hochschild_poincare(family)
            assert stored == computed, f"{family}: stored {stored} != computed {computed}"

    def test_virasoro_period(self):
        assert THEOREM_H_STATUS['virasoro']['periodicity'] == 2

    def test_w3_quasi_period(self):
        assert THEOREM_H_STATUS['w3']['quasi_period'] == 6

    def test_w4_quasi_period(self):
        assert THEOREM_H_STATUS['w4']['quasi_period'] == 12

    def test_w5_quasi_period(self):
        assert THEOREM_H_STATUS['w5']['quasi_period'] == 60


# ===================================================================
# Quadratic polynomial construction
# ===================================================================

class TestQuadraticConstruction:
    """Test the quadratic_poincare_polynomial function directly."""

    def test_basic(self):
        assert quadratic_poincare_polynomial(1, 3, 1) == [1, 3, 1]

    def test_zero_center(self):
        """Hypothetical: center = 0 (never happens for VOAs)."""
        assert quadratic_poincare_polynomial(0, 2, 1) == [0, 2, 1]

    def test_generic_km(self):
        """Generic KM: center = C, H^1 = g, Z(A^!) = C."""
        for d in [3, 8, 15, 24, 35]:
            poly = quadratic_poincare_polynomial(1, d, 1)
            assert poly == [1, d, 1]
            assert sum(poly) == d + 2  # total dim
            assert poly[0] - poly[1] + poly[2] == 2 - d  # euler char


# ===================================================================
# lcm utility
# ===================================================================

class TestLcm:
    """Test the lcm_list utility."""

    def test_lcm_pair(self):
        assert lcm_list([2, 3]) == 6

    def test_lcm_triple(self):
        assert lcm_list([2, 3, 4]) == 12

    def test_lcm_sl5(self):
        assert lcm_list([2, 3, 4, 5]) == 60

    def test_lcm_single(self):
        assert lcm_list([7]) == 7

    def test_lcm_coprime(self):
        assert lcm_list([3, 5, 7]) == 105


# ===================================================================
# Cross-regime comparison
# ===================================================================

class TestCrossRegime:
    """Compare quadratic and W-algebra regimes."""

    def test_km_vs_w_for_sl2(self):
        """Affine sl_2 (quadratic): P(t) = 1+3t+t^2.
        Virasoro = W_2 = DS(sl_2) (W-algebra): ChirHoch = C[Theta].
        Different objects, different regimes."""
        poly_km = hochschild_poincare('affine_sl2')
        dims_w2 = virasoro_hochschild_dims(4)
        # KM: [1, 3, 1]
        # W_2: [1, 0, 1, 0, 1]
        assert poly_km == [1, 3, 1]
        assert dims_w2 == [1, 0, 1, 0, 1]
        # They are DIFFERENT: KM is quadratic, Virasoro is W-algebra

    def test_euler_char_quadratic_finite(self):
        """Euler char is finite and integer for quadratic regime."""
        for family in ['heisenberg', 'affine_sl2', 'affine_sl3',
                        'betagamma', 'bc_ghosts', 'free_fermion']:
            chi = hochschild_euler_char(family)
            assert isinstance(chi, int)

    def test_euler_char_w_algebra_divergent(self):
        """Euler char diverges for W-algebras with even-degree generators."""
        chi = hochschild_euler_char('virasoro')
        assert chi is None  # divergent: Virasoro has Theta of degree 2

    def test_total_dim_quadratic_finite(self):
        for family in ['heisenberg', 'affine_sl2', 'affine_sl3',
                        'betagamma', 'bc_ghosts', 'free_fermion']:
            total = hochschild_total_dim(family)
            assert isinstance(total, int) and total > 0

    def test_total_dim_w_algebra_infinite(self):
        for family in ['virasoro', 'w3']:
            assert hochschild_total_dim(family) is None
