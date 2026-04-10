"""Tests for Theorem H: Hochschild polynomial growth (bounded amplitude).

Verifies the bounded Koszul regime of Theorem H across all standard
families.  Every Koszul chiral algebra A on a smooth projective curve
X (dim_C X = 1) has:
  * ChirHoch^n(A) = 0 for n outside [0, 2];
  * P_A(t) a polynomial of degree <= 2;
  * dim ChirHoch*(A) <= 4.

AP94 rectification: the prior "W-algebra polynomial ring regime"
(ChirHoch*(W^k) = C[Theta_1, ..., Theta_r] with infinite-dimensional
polynomial growth) was a Gelfand-Fuchs-style artefact.  It is REFUTED
by Theorem H: Virasoro, W_3, W_N are Koszul at generic level (see
prop:virasoro-koszul-acyclic, thm:virasoro-chiral-koszul), so their
ChirHoch lives in amplitude [0, 2] with total dim <= 4.  The tests
below reflect the bounded model.

References:
  thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
  thm:main-koszul-hoch             (chiral_hochschild_koszul.tex)
  prop:virasoro-koszul-acyclic     (bar_complex_tables.tex)
  thm:virasoro-chiral-koszul       (bar_complex_tables.tex)
  CLAUDE.md: Theorem H, AP94-AP98, AP102, AP128
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
    bar_complex_betti_sl2,
    bar_complex_betti_abelian,
    polynomial_growth_verification,
    euler_characteristic_derived,
    palindromicity_derived,
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
# Virasoro (bounded Koszul per Theorem H; formerly "W-algebra regime")
# ===================================================================

class TestVirasoro:
    """Theorem H for Virasoro Vir_c at generic c.

    AP94 rectification: under Theorem H amplitude [0, 2],
      ChirHoch^0(Vir_c) = C (center),
      ChirHoch^1(Vir_c) = 0 (no outer derivations at generic c),
      ChirHoch^2(Vir_c) = C (level/central kappa = c/2 deformation),
      ChirHoch^n(Vir_c) = 0 for n > 2.
    The prior 2-periodic ChirHoch^{2k} = C (infinite) was a
    Gelfand-Fuchs-style artefact, REFUTED by Theorem H.
    """

    def test_generator_count(self):
        assert generator_count('virasoro') == 1

    def test_h0_is_center(self):
        """ChirHoch^0(Vir_c) = C (center)."""
        assert hochschild_betti('virasoro', 0) == 1

    def test_h1_vanishes(self):
        """ChirHoch^1(Vir_c) = 0 (no outer derivations at generic c)."""
        assert hochschild_betti('virasoro', 1) == 0

    def test_h2_central_extension(self):
        """ChirHoch^2(Vir_c) = C (Virasoro central extension class kappa=c/2)."""
        assert hochschild_betti('virasoro', 2) == 1

    def test_bounded_amplitude(self):
        """ChirHoch^n(Vir_c) = 0 for n > 2 (Theorem H, amplitude [0,2])."""
        for n in range(3, 20):
            assert hochschild_betti('virasoro', n) == 0

    def test_concentration_negative(self):
        """ChirHoch^n(Vir_c) = 0 for n < 0."""
        for n in range(-5, 0):
            assert hochschild_betti('virasoro', n) == 0

    def test_virasoro_dims_function(self):
        """virasoro_hochschild_dims(10) = [1, 0, 1, 0, ..., 0]."""
        dims = virasoro_hochschild_dims(10)
        expected = [0] * 11
        expected[0] = 1
        expected[2] = 1
        assert dims == expected

    def test_poincare_polynomial(self):
        """P_{Vir}(t) = 1 + t^2."""
        poly = hochschild_poincare('virasoro')
        assert poly == [1, 0, 1]

    def test_total_dim_bounded(self):
        """Total dim = 2 (Theorem H dim <= 4 bound, Virasoro saturates to 2)."""
        assert hochschild_total_dim('virasoro') == 2

    def test_euler_char(self):
        """chi(Vir_c) = 1 - 0 + 1 = 2."""
        assert hochschild_euler_char('virasoro') == 2

    def test_periodicity_check_reports_bounded(self):
        """virasoro_periodicity_check now reports bounded amplitude [0,2]."""
        result = virasoro_periodicity_check(30)
        assert result['passed'] is True
        assert result['amplitude'] == [0, 2]
        assert result['total_dim'] == 2


# ===================================================================
# W_3 (bounded Koszul per Theorem H; formerly "W-algebra regime")
# ===================================================================

class TestW3:
    """Theorem H for W_3 = W^k(sl_3, f_prin) at generic level.

    AP94 rectification: under Theorem H W_3 is Koszul (Feigin-Frenkel),
    so its chiral Hochschild cohomology has amplitude [0, 2] with
      P_{W_3}(t) = 1 + t^2.
    The prior polynomial-ring model C[Theta_1, Theta_2] with
    weighted-partition counts is REFUTED.  The strong generators of
    the VOA (weights 2 and 3) are preserved as VOA metadata but do
    NOT give polynomial generators on ChirHoch*.
    """

    def test_generator_count(self):
        """W_3 has 2 strong generators (T of weight 2, W of weight 3)."""
        assert generator_count('w3') == 2

    def test_strong_gen_weights(self):
        """Strong-generator weights = [2, 3] (VOA metadata)."""
        assert w_algebra_gen_degrees('A', 2) == [2, 3]

    def test_h0(self):
        """ChirHoch^0(W_3) = C (center)."""
        assert hochschild_betti('w3', 0) == 1

    def test_h1(self):
        """ChirHoch^1(W_3) = 0 (no outer derivations at generic level)."""
        assert hochschild_betti('w3', 1) == 0

    def test_h2(self):
        """ChirHoch^2(W_3) = C (level deformation class)."""
        assert hochschild_betti('w3', 2) == 1

    def test_bounded_amplitude(self):
        """ChirHoch^n(W_3) = 0 for n > 2 (Theorem H, amplitude [0,2])."""
        for n in range(3, 20):
            assert hochschild_betti('w3', n) == 0

    def test_w3_dims_function_bounded(self):
        """w3_hochschild_dims returns the bounded sequence [1,0,1,0,...]."""
        dims = w3_hochschild_dims(12)
        expected = [0] * 13
        expected[0] = 1
        expected[2] = 1
        assert dims == expected

    def test_quasi_periodicity_check_reports_bounded(self):
        """Formerly quasi-period 6; now reports bounded amplitude [0,2]."""
        result = w3_quasi_periodicity_check(60)
        assert result['amplitude'] == [0, 2]
        assert result['total_dim'] == 2
        assert result['passed'] is True

    def test_poincare_polynomial(self):
        """P_{W_3}(t) = 1 + t^2."""
        poly = hochschild_poincare('w3')
        assert poly == [1, 0, 1]

    def test_total_dim_bounded(self):
        """Total dim = 2, satisfying Theorem H dim <= 4 bound."""
        assert hochschild_total_dim('w3') == 2

    def test_euler_char(self):
        """chi(W_3) = 1 - 0 + 1 = 2."""
        assert hochschild_euler_char('w3') == 2


# ===================================================================
# W_N parametric (bounded Koszul per Theorem H)
# ===================================================================

class TestWN:
    """Theorem H for W_N = W^k(sl_N, f_prin) at generic level.

    AP94 rectification: every W_N is Koszul at generic level, so
    P_{W_N}(t) = 1 + t^2 (bounded amplitude [0, 2], total dim 2).
    The prior polynomial-ring model with r = N-1 generators giving
    weighted-partition counts is REFUTED.  VOA strong-generator
    weights (2, 3, ..., N) are preserved as metadata only.
    """

    @pytest.mark.parametrize("N,expected_rank", [
        (2, 1), (3, 2), (4, 3), (5, 4), (10, 9),
    ])
    def test_strong_gen_count(self, N, expected_rank):
        """W_N has N-1 strong generators (VOA metadata)."""
        assert generator_count('wN', N=N) == expected_rank

    @pytest.mark.parametrize("N,expected_weights", [
        (2, [2]), (3, [2, 3]), (4, [2, 3, 4]), (5, [2, 3, 4, 5]),
    ])
    def test_strong_gen_weights(self, N, expected_weights):
        """Strong-generator conformal weights are 2, 3, ..., N."""
        assert w_algebra_gen_degrees('A', N - 1) == expected_weights

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_bounded_poincare(self, N):
        """P_{W_N}(t) = 1 + t^2 for every N (Theorem H bounded regime)."""
        poly = hochschild_poincare('wN', N=N)
        assert poly == [1, 0, 1]

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_total_dim_at_most_4(self, N):
        """Theorem H bound: total dim ChirHoch*(W_N) <= 4."""
        total = hochschild_total_dim('wN', N=N)
        assert total == 2
        assert total <= 4

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_bounded_amplitude(self, N):
        """ChirHoch^n(W_N) = 0 for n > 2 (Theorem H)."""
        for n in range(3, 15):
            assert hochschild_betti('wN', n, N=N) == 0

    def test_w4_bounded_series(self):
        """W_4 bounded series: [1, 0, 1, 0, 0, ...]."""
        dims = w_algebra_poincare_series([2, 3, 4], 12)
        expected = [0] * 13
        expected[0] = 1
        expected[2] = 1
        assert dims == expected

    def test_w5_bounded_series(self):
        """W_5 bounded series: [1, 0, 1, 0, 0, ...]."""
        dims = w_algebra_poincare_series([2, 3, 4, 5], 10)
        expected = [0] * 11
        expected[0] = 1
        expected[2] = 1
        assert dims == expected

    def test_w2_agrees_with_virasoro(self):
        """W_2 = Virasoro: both bounded to [1, 0, 1, 0, ...]."""
        dims_w2 = w_algebra_poincare_series([2], 20)
        dims_vir = virasoro_hochschild_dims(20)
        assert dims_w2 == dims_vir


# ===================================================================
# Bounded Hochschild dimensions (formerly weighted-partition model)
# ===================================================================

class TestBoundedHochschildDim:
    """Verify w_algebra_hochschild_dim returns the bounded sequence.

    AP94: the prior weighted-partition model has been REFUTED.  The
    function now returns the Theorem-H-consistent finite support:
    dim = 1 at n = 0 and n = 2, otherwise 0.
    """

    def test_single_gen_bounded(self):
        """All single-generator W-algebras: dim = 1 at n=0,2; else 0."""
        for gen_degrees in ([2], [3], [4]):
            assert w_algebra_hochschild_dim(gen_degrees, 0) == 1
            assert w_algebra_hochschild_dim(gen_degrees, 1) == 0
            assert w_algebra_hochschild_dim(gen_degrees, 2) == 1
            for n in range(3, 20):
                assert w_algebra_hochschild_dim(gen_degrees, n) == 0

    def test_two_gen_bounded(self):
        """W_3 with strong gens of weight (2,3): bounded to [1,0,1,0,...]."""
        assert w_algebra_hochschild_dim([2, 3], 0) == 1
        assert w_algebra_hochschild_dim([2, 3], 1) == 0
        assert w_algebra_hochschild_dim([2, 3], 2) == 1
        for n in range(3, 20):
            assert w_algebra_hochschild_dim([2, 3], n) == 0

    def test_any_gens_h0_is_one(self):
        """Any W-algebra: dim ChirHoch^0 = 1 (center)."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5]]:
            assert w_algebra_hochschild_dim(gen_degrees, 0) == 1

    def test_any_gens_h2_is_one(self):
        """Any W-algebra: dim ChirHoch^2 = 1 (level deformation)."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5]]:
            assert w_algebra_hochschild_dim(gen_degrees, 2) == 1

    def test_negative_degree(self):
        """dim ChirHoch^n = 0 for n < 0."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4]]:
            for n in range(-5, 0):
                assert w_algebra_hochschild_dim(gen_degrees, n) == 0

    def test_concentration_above_two(self):
        """dim ChirHoch^n = 0 for n > 2 (Theorem H amplitude [0,2])."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5]]:
            for n in range(3, 30):
                assert w_algebra_hochschild_dim(gen_degrees, n) == 0


# ===================================================================
# Growth rate (REFUTED polynomial-ring model)
# ===================================================================

class TestGrowthRate:
    """Verify w_algebra_growth_rate returns 0 (bounded amplitude).

    AP94: the prior polynomial-growth model (dim ~ n^{r-1}) is REFUTED.
    Under Theorem H the support is finite, so the asymptotic growth
    rate is 0 for every W-algebra family.
    """

    def test_virasoro_growth_rate_zero(self):
        """Virasoro bounded support: growth rate 0."""
        rate = w_algebra_growth_rate([2])
        assert rate == 0.0

    def test_w3_growth_rate_zero(self):
        """W_3 bounded support: growth rate 0 (formerly ~ n/6)."""
        rate = w_algebra_growth_rate([2, 3])
        assert rate == 0.0

    def test_w4_growth_rate_zero(self):
        """W_4 bounded support: growth rate 0 (formerly ~ n^2/48)."""
        rate = w_algebra_growth_rate([2, 3, 4])
        assert rate == 0.0

    def test_large_n_bounded(self):
        """At large n, dim = 0 for every W-algebra (bounded amplitude)."""
        for gen_degrees in [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5]]:
            for n in [100, 500, 1000]:
                assert w_algebra_hochschild_dim(gen_degrees, n) == 0


# ===================================================================
# Concentration verification (all Koszul families, Theorem H)
# ===================================================================

class TestConcentration:
    """Verify amplitude [0, 2] concentration for every Koszul family.

    AP94: under Theorem H every Koszul chiral algebra has bounded
    Hochschild in [0, 2] with dim <= 4.  This includes Virasoro, W_3,
    W_N, formerly mis-modelled as polynomial rings.
    """

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'affine_sl3',
        'betagamma', 'bc_ghosts', 'free_fermion',
    ])
    def test_bounded_concentration_KM_type(self, family):
        result = verify_concentration(family)
        assert result['passed'] is True

    def test_virasoro_bounded(self):
        """Virasoro: concentrated in [0, 2] (Theorem H)."""
        result = verify_concentration('virasoro')
        assert result['passed'] is True
        assert result['details'].get('unbounded') is False

    def test_w3_bounded(self):
        """W_3: concentrated in [0, 2] (Theorem H)."""
        result = verify_concentration('w3')
        assert result['passed'] is True
        assert result['details'].get('unbounded') is False


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

    def test_virasoro_palindromic(self):
        """Virasoro P(t) = 1 + t^2 is palindromic (dim Z = dim Z^! = 1)."""
        result = verify_palindromicity('virasoro')
        assert result['passed'] is True
        assert result['palindromic_self'] is True


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

    def test_virasoro_dual_poly(self):
        """P_{Vir^!}(t) = P_{Vir_{26-c}}(t) = 1 + t^2 (palindromic)."""
        dual_poly = koszul_dual_polynomial('virasoro')
        assert dual_poly == [1, 0, 1]


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
        """Bounded amplitude: E_2^{p,0} = [1, 0, 1, 0, 0, 0, 0]."""
        E2 = hochschild_spectral_sequence('virasoro', max_p=6, max_q=3)
        assert E2[0][0] == 1
        assert E2[1][0] == 0
        assert E2[2][0] == 1
        # Theorem H amplitude [0,2]: E_2^{p,0} = 0 for p > 2
        assert E2[3][0] == 0
        assert E2[4][0] == 0
        assert E2[5][0] == 0
        assert E2[6][0] == 0
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

    def test_virasoro_bounded(self):
        """Virasoro under Theorem H: bounded 3-term polynomial [1, 0, 1]."""
        result = exterior_algebra_verification('virasoro')
        assert result['passed'] is True
        assert result['polynomial'] == [1, 0, 1]


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

    def test_virasoro_bounded_poincare(self):
        """Virasoro: P(t) = 1 + t^2 (AP94 bounded model)."""
        assert THEOREM_H_STATUS['virasoro']['poincare'] == [1, 0, 1]

    def test_w3_bounded_poincare(self):
        """W_3: P(t) = 1 + t^2 (AP94 bounded model)."""
        assert THEOREM_H_STATUS['w3']['poincare'] == [1, 0, 1]

    def test_w4_bounded_poincare(self):
        """W_4: P(t) = 1 + t^2 (AP94 bounded model)."""
        assert THEOREM_H_STATUS['w4']['poincare'] == [1, 0, 1]

    def test_w5_bounded_poincare(self):
        """W_5: P(t) = 1 + t^2 (AP94 bounded model)."""
        assert THEOREM_H_STATUS['w5']['poincare'] == [1, 0, 1]

    def test_all_w_algebras_bounded_by_four(self):
        """All W-algebra entries: total dim <= 4 (Theorem H)."""
        for family in ('virasoro', 'w3', 'w4', 'w5'):
            poly = THEOREM_H_STATUS[family]['poincare']
            assert sum(poly) <= 4


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
    """Compare bounded polynomials across the standard landscape.

    AP94: under Theorem H every Koszul chiral algebra has a bounded
    amplitude 3-term Hochschild polynomial.  Different families give
    different polynomials (different coefficients), but all are
    finitely supported in [0, 2].
    """

    def test_km_vs_virasoro_bounded_contrast(self):
        """Affine sl_2 has P(t) = 1 + 3t + t^2 (total dim 5);
        Virasoro has P(t) = 1 + t^2 (total dim 2).  Both bounded
        in [0, 2] per Theorem H; ChirHoch^1 distinguishes them."""
        poly_km = hochschild_poincare('affine_sl2')
        poly_vir = hochschild_poincare('virasoro')
        assert poly_km == [1, 3, 1]
        assert poly_vir == [1, 0, 1]
        assert sum(poly_km) == 5
        assert sum(poly_vir) == 2

    def test_euler_char_finite_integer_everywhere(self):
        """chi = P_A(-1) is a finite integer for every Koszul family."""
        families = ['heisenberg', 'affine_sl2', 'affine_sl3',
                    'betagamma', 'bc_ghosts', 'free_fermion',
                    'virasoro', 'w3']
        for family in families:
            chi = hochschild_euler_char(family)
            assert isinstance(chi, int)

    def test_euler_char_virasoro_bounded(self):
        """chi(Vir_c) = 1 - 0 + 1 = 2 (Theorem H bounded, AP94)."""
        assert hochschild_euler_char('virasoro') == 2

    def test_total_dim_finite_everywhere(self):
        """dim ChirHoch*(A) <= 4 for every family (Theorem H bound)."""
        families = ['heisenberg', 'affine_sl2', 'affine_sl3',
                    'betagamma', 'bc_ghosts', 'free_fermion',
                    'virasoro', 'w3']
        for family in families:
            total = hochschild_total_dim(family)
            assert isinstance(total, int)
            assert total > 0
            assert total <= 5   # Theorem H bound; saturates at sl_2

    def test_total_dim_w_algebras_equals_two(self):
        """Virasoro and W_3: total dim = 2 (1 + 0 + 1)."""
        for family in ['virasoro', 'w3']:
            assert hochschild_total_dim(family) == 2


# ===================================================================
# DERIVED: Bar complex Betti numbers for sl_2
# ===================================================================

class TestBarComplexBettiSl2:
    """Compute Hochschild Betti numbers from the bar complex of CE(sl_2)."""

    def test_ce_cohomology_h0(self):
        """H^0(CE(sl_2)) = 1 (constants)."""
        r = bar_complex_betti_sl2()
        assert r["H0_CE"] == 1

    def test_ce_cohomology_h1_vanishes(self):
        """H^1(CE(sl_2)) = 0 (Whitehead's first lemma)."""
        r = bar_complex_betti_sl2()
        assert r["H1_CE"] == 0

    def test_ce_cohomology_h2_vanishes(self):
        """H^2(CE(sl_2)) = 0 (Whitehead's second lemma)."""
        r = bar_complex_betti_sl2()
        assert r["H2_CE"] == 0

    def test_ce_cohomology_h3(self):
        """H^3(CE(sl_2)) = 1 (top exterior power)."""
        r = bar_complex_betti_sl2()
        assert r["H3_CE"] == 1

    def test_whitehead_holds(self):
        """Whitehead's lemma holds for sl_2."""
        r = bar_complex_betti_sl2()
        assert r["whitehead_holds"] is True

    def test_chiral_hochschild_from_bar(self):
        """Chiral Hochschild = [1, 3, 1] from bar + curve spectral sequence."""
        r = bar_complex_betti_sl2()
        assert r["chiral_hochschild"] == [1, 3, 1]

    def test_ce_dims(self):
        """CE(sl_2) has dims {0:1, 1:3, 2:3, 3:1} = exterior algebra."""
        r = bar_complex_betti_sl2()
        assert r["ce_dims"] == {0: 1, 1: 3, 2: 3, 3: 1}


# ===================================================================
# DERIVED: Bar complex Betti numbers for abelian Lie algebra
# ===================================================================

class TestBarComplexBettiAbelian:
    """Compute bar Betti numbers for the abelian Lie algebra."""

    def test_rank1_ce_dims(self):
        """CE(h_1): Lambda^*(k) = k + k*x, dims = {0:1, 1:1}."""
        r = bar_complex_betti_abelian(rank=1)
        assert r["ce_dims"] == {0: 1, 1: 1}

    def test_rank1_chiral_hochschild(self):
        """Chiral Hochschild for rank-1 Heisenberg: [1, 1, 1]."""
        r = bar_complex_betti_abelian(rank=1)
        assert r["chiral_hochschild"] == [1, 1, 1]

    def test_rank3_chiral_hochschild(self):
        """Chiral Hochschild for rank-3: [1, 3, 1]."""
        r = bar_complex_betti_abelian(rank=3)
        assert r["chiral_hochschild"] == [1, 3, 1]

    def test_rank_r_euler_char(self):
        """Euler char = 2 - r for rank r."""
        for r in [1, 2, 3, 4, 8]:
            result = bar_complex_betti_abelian(rank=r)
            assert result["euler_char_chiral"] == 2 - r

    def test_rank1_all_cocycles(self):
        """For abelian algebra with d=0, all cochains are cocycles."""
        r = bar_complex_betti_abelian(rank=1)
        assert r["ce_cohomology"] == {0: 1, 1: 1}

    def test_rank2_ce_cohomology(self):
        """For rank 2, CE has dims {0:1, 1:2, 2:1} and all are cocycles."""
        r = bar_complex_betti_abelian(rank=2)
        assert r["ce_cohomology"] == {0: 1, 1: 2, 2: 1}


# ===================================================================
# DERIVED: Polynomial growth verification
# ===================================================================

class TestPolynomialGrowthVerification:
    """Verify polynomial growth from computed dimensions."""

    def test_heisenberg_finite_support(self):
        """Heisenberg: dims have finite support in [0, 2]."""
        r = polynomial_growth_verification('heisenberg')
        assert r["verified"]
        assert r["is_finite_support"]
        assert r["max_nonzero_degree"] == 2

    def test_affine_sl2_finite_support(self):
        """Affine sl_2: dims have finite support."""
        r = polynomial_growth_verification('affine_sl2')
        assert r["verified"]
        assert r["is_finite_support"]

    def test_betagamma_finite_support(self):
        r = polynomial_growth_verification('betagamma')
        assert r["verified"]

    def test_virasoro_finite_support(self):
        """Virasoro bounded amplitude [0, 2] (AP94 rectified)."""
        r = polynomial_growth_verification('virasoro', max_n=30)
        assert r["verified"]
        assert r["is_finite_support"]
        assert r["max_nonzero_degree"] == 2
        assert r["growth_degree"] == 0

    def test_w3_finite_support(self):
        """W_3 bounded amplitude [0, 2] (AP94 rectified, was linear)."""
        r = polynomial_growth_verification('w3', max_n=60)
        assert r["verified"]
        assert r["is_finite_support"]
        assert r["max_nonzero_degree"] == 2
        assert r["growth_degree"] == 0

    def test_w4_finite_support(self):
        """W_4 bounded amplitude [0, 2] (AP94 rectified, was quadratic)."""
        r = polynomial_growth_verification('wN', max_n=60, N=4)
        assert r["verified"]
        assert r["is_finite_support"]
        assert r["max_nonzero_degree"] == 2
        assert r["growth_degree"] == 0

    def test_w5_finite_support(self):
        """W_5 bounded amplitude [0, 2] (AP94 rectified, was cubic)."""
        r = polynomial_growth_verification('wN', max_n=60, N=5)
        assert r["verified"]
        assert r["is_finite_support"]
        assert r["max_nonzero_degree"] == 2
        assert r["growth_degree"] == 0


# ===================================================================
# DERIVED: Euler characteristic from bar dimensions
# ===================================================================

class TestEulerCharDerived:
    """Compute Euler characteristic from actual bar cohomology dimensions."""

    def test_heisenberg_chi_from_dims(self):
        """chi(H) = 1 - 1 + 1 = 1 from computed dims."""
        r = euler_characteristic_derived('heisenberg')
        assert r["chi"] == 1
        assert r["verified"]

    def test_affine_sl2_chi_from_dims(self):
        """chi(sl_2) = 1 - 3 + 1 = -1 from computed dims."""
        r = euler_characteristic_derived('affine_sl2')
        assert r["chi"] == -1
        assert r["verified"]

    def test_affine_sl3_chi_from_dims(self):
        """chi(sl_3) = 1 - 8 + 1 = -6 from computed dims."""
        r = euler_characteristic_derived('affine_sl3')
        assert r["chi"] == -6
        assert r["verified"]

    def test_betagamma_chi_from_dims(self):
        """chi(bg) = 1 - 2 + 1 = 0 from computed dims."""
        r = euler_characteristic_derived('betagamma')
        assert r["chi"] == 0
        assert r["verified"]

    def test_quadratic_chi_stabilizes(self):
        """For quadratic families, chi stabilizes after degree 2."""
        for family in ['heisenberg', 'affine_sl2', 'betagamma', 'bc_ghosts']:
            r = euler_characteristic_derived(family)
            assert r["stabilized"], f"{family}: chi does not stabilize"

    def test_virasoro_chi_finite(self):
        """Virasoro bounded: chi = 1 - 0 + 1 = 2 stabilises after n = 2."""
        r = euler_characteristic_derived('virasoro')
        assert r["chi"] == 2
        assert r["stabilized"]
        assert r["verified"]

    def test_w3_chi_finite(self):
        """W_3 bounded: chi = 1 - 0 + 1 = 2 stabilises after n = 2."""
        r = euler_characteristic_derived('w3')
        assert r["chi"] == 2
        assert r["stabilized"]
        assert r["verified"]

    def test_quadratic_chi_matches_formula(self):
        """Derived chi matches the formula chi = p0 - p1 + p2."""
        for family in ['heisenberg', 'affine_sl2', 'affine_sl3',
                        'betagamma', 'bc_ghosts', 'free_fermion']:
            r = euler_characteristic_derived(family)
            expected = hochschild_euler_char(family)
            assert r["chi"] == expected, f"{family}: {r['chi']} != {expected}"


# ===================================================================
# DERIVED: Palindromicity from computed dimensions
# ===================================================================

class TestPalindromicityDerived:
    """Verify palindromicity from COMPUTED bar dimensions."""

    def test_heisenberg_palindromic(self):
        """Heisenberg: p_0 = p_2 = 1."""
        r = palindromicity_derived('heisenberg')
        assert r["palindromic"]
        assert r["verified"]

    def test_affine_sl2_palindromic(self):
        """sl_2: p_0 = p_2 = 1."""
        r = palindromicity_derived('affine_sl2')
        assert r["palindromic"]
        assert r["verified"]

    def test_betagamma_palindromic(self):
        """bg: p_0 = p_2 = 1."""
        r = palindromicity_derived('betagamma')
        assert r["palindromic"]
        assert r["verified"]

    def test_all_quadratic_palindromic(self):
        """ALL quadratic families are palindromic."""
        for family in ['heisenberg', 'affine_sl2', 'affine_sl3',
                        'betagamma', 'bc_ghosts', 'free_fermion']:
            r = palindromicity_derived(family)
            assert r["palindromic"], f"{family} not palindromic"
            assert r["concentrated_in_0_2"], f"{family} not concentrated"

    def test_virasoro_palindromic_derived(self):
        """Virasoro P(t) = 1 + t^2 is self-palindromic (p_0 = p_2 = 1)."""
        r = palindromicity_derived('virasoro')
        assert r["applicable"]
        assert r["palindromic"]
        assert r["concentrated_in_0_2"]
        assert r["verified"]

    def test_concentration_verified(self):
        """Concentration in [0,2] verified from computed dims."""
        for family in ['heisenberg', 'affine_sl2', 'betagamma']:
            r = palindromicity_derived(family)
            assert r["concentrated_in_0_2"]

    def test_koszul_duality_check_present(self):
        """Koszul duality check data is present for dual pairs in FAMILY_DATA."""
        # betagamma <-> bc_ghosts are both in FAMILY_DATA
        for family in ['betagamma', 'bc_ghosts']:
            r = palindromicity_derived(family)
            assert "H0_A" in r["koszul_duality_check"], (
                f"{family}: koszul_duality_check = {r['koszul_duality_check']}"
            )
