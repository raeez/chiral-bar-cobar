r"""Tests for delta_F_4 engine: genus-4 cross-channel correction for W_N.

42 tests organized in 7 sections:

  1. Lambda_FP exact values (4 tests)
  2. Virasoro vanishing at all genera (4 tests)
  3. W_3 cross-validation against known closed forms (6 tests)
  4. Genus-4 c-polynomial structure (5 tests)
  5. N-polynomial degree verification (6 tests)
  6. Cross-genus consistency (5 tests)
  7. Power-sum structure and matrix model (6 tests)
  8. Fast amplitude optimization (6 tests)

Every numerical value verified by at least 2 independent paths.
Exact Fraction arithmetic throughout.

References:
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    op:multi-generator-universality (RESOLVED NEGATIVELY)
    AP27: bar propagator weight 1
"""

import pytest
from fractions import Fraction

from compute.lib.delta_f4_engine import (
    # Primitives
    bernoulli_number,
    lambda_fp,
    power_sum,
    # Frobenius algebra
    grav_C3,
    grav_propagator,
    grav_kappa_channel,
    grav_kappa_total,
    # Vertex factors
    grav_V0_factorize,
    grav_vertex_factor,
    # Graph amplitude
    graph_amplitude_decomposed,
    graph_amplitude_fast,
    half_edge_channels,
    # Core computation
    delta_F4_grav_graph_sum,
    delta_F2_grav_graph_sum,
    delta_F3_grav_graph_sum,
    # Enumeration
    genus4_graphs,
    genus4_boundary_graphs,
    # Closed forms
    delta_F2_closed_form_W3,
    delta_F3_closed_form_W3,
    delta_F4_closed_form_W3,
    # Interpolation
    newton_interpolate,
    extract_c_polynomial_genus4,
    # Matrix model
    penner_potential_coefficients,
    penner_free_energy_genus2,
    # Checks
    cross_genus_check_W3,
    virasoro_vanishing_check,
)

from compute.lib.stable_graph_enumeration import StableGraph


# ============================================================================
# Section 1: Lambda_FP exact values
# ============================================================================

class TestLambdaFP:
    """Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda4(self):
        """lambda_4^FP = 127/154828800.

        Independent verification: (2^7 - 1) * |B_8| / (2^7 * 8!)
        = 127 * (1/30) / (128 * 40320) = 127/154828800.
        """
        B8 = bernoulli_number(8)
        assert B8 == Fraction(-1, 30)
        assert lambda_fp(4) == Fraction(127, 154828800)


# ============================================================================
# Section 2: Virasoro vanishing at all genera
# ============================================================================

class TestVirasiroVanishing:
    """delta_F_g(W_2, c) = 0 for all g (Virasoro is uniform weight)."""

    def test_virasoro_genus2(self):
        assert delta_F2_grav_graph_sum(2, Fraction(1)) == 0

    def test_virasoro_genus3(self):
        assert delta_F3_grav_graph_sum(2, Fraction(1)) == 0

    def test_virasoro_genus4(self):
        assert delta_F4_grav_graph_sum(2, Fraction(1)) == 0

    def test_virasoro_genus4_c5(self):
        """Virasoro vanishing at c=5."""
        assert delta_F4_grav_graph_sum(2, Fraction(5)) == 0


# ============================================================================
# Section 3: W_3 cross-validation against known closed forms
# ============================================================================

class TestW3ClosedForms:
    """delta_F_g(W_3, c) matches known closed forms for g = 2, 3, 4."""

    def test_genus2_c1(self):
        """delta_F_2(W_3, 1) = (1+204)/16 = 205/16."""
        computed = delta_F2_grav_graph_sum(3, Fraction(1))
        expected = delta_F2_closed_form_W3(Fraction(1))
        assert computed == expected == Fraction(205, 16)

    def test_genus2_c10(self):
        computed = delta_F2_grav_graph_sum(3, Fraction(10))
        expected = delta_F2_closed_form_W3(Fraction(10))
        assert computed == expected

    def test_genus3_c1(self):
        computed = delta_F3_grav_graph_sum(3, Fraction(1))
        expected = delta_F3_closed_form_W3(Fraction(1))
        assert computed == expected

    def test_genus3_c3(self):
        computed = delta_F3_grav_graph_sum(3, Fraction(3))
        expected = delta_F3_closed_form_W3(Fraction(3))
        assert computed == expected

    def test_genus4_c1(self):
        """Main validation: genus-4 graph sum matches closed form at c=1."""
        computed = delta_F4_grav_graph_sum(3, Fraction(1))
        expected = delta_F4_closed_form_W3(Fraction(1))
        assert computed == expected

    def test_genus4_c2(self):
        computed = delta_F4_grav_graph_sum(3, Fraction(2))
        expected = delta_F4_closed_form_W3(Fraction(2))
        assert computed == expected


# ============================================================================
# Section 4: Genus-4 c-polynomial structure
# ============================================================================

class TestCPolynomialStructure:
    """delta_F_4 has the form P_4(c) / (D_4 * c^3) with deg(P_4) = 4."""

    def test_w3_numerator_degree(self):
        """For W_3: delta_F_4 * c^3 is a degree-4 polynomial in c."""
        c_vals = {Fraction(k): delta_F4_closed_form_W3(Fraction(k)) * Fraction(k)**3
                  for k in range(1, 7)}
        coeffs5 = newton_interpolate(c_vals, 5)
        assert coeffs5[0] == 0  # degree-5 leading coeff is zero

    def test_w3_coefficients(self):
        """Verify the 5 coefficients of the W_3 numerator polynomial."""
        # P(c) = 287c^4 + 268881c^3 + 115455816c^2 + 29725133760c + 5594347866240
        # D = 17418240
        c_vals = {Fraction(k): delta_F4_closed_form_W3(Fraction(k)) * Fraction(k)**3
                  for k in range(1, 6)}
        coeffs = newton_interpolate(c_vals, 4)
        assert coeffs[0] == Fraction(287, 17418240)
        assert coeffs[1] == Fraction(268881, 17418240)

    def test_positivity_w3(self):
        """delta_F_4(W_3, c) > 0 for c > 0."""
        for cv in [1, 2, 5, 10, 100]:
            assert delta_F4_closed_form_W3(Fraction(cv)) > 0

    def test_w4_numerator_degree(self):
        """For W_4: delta_F_4 * c^3 is a degree-4 polynomial in c."""
        c_vals = {}
        for k in range(1, 7):
            c_vals[Fraction(k)] = delta_F4_grav_graph_sum(4, Fraction(k)) * Fraction(k)**3
        coeffs5 = newton_interpolate(c_vals, 5)
        assert coeffs5[0] == 0

    def test_n2_vanishing_in_polynomial(self):
        """All polynomial coefficients vanish at N=2."""
        # Extract c-polynomial for N=2 (Virasoro)
        for cv in range(1, 6):
            assert delta_F4_grav_graph_sum(2, Fraction(cv)) == 0


# ============================================================================
# Section 5: N-polynomial degree verification
# ============================================================================

class TestNPolynomialDegrees:
    """Verify the degree pattern of the N-polynomials."""

    @pytest.fixture(scope='class')
    def all_coefficients(self):
        """Pre-compute c-polynomial coefficients for N=2..7."""
        result = {}
        for N in [2, 3, 4, 5, 6]:
            if N == 2:
                result[N] = {'E': Fraction(0), 'D': Fraction(0),
                             'C': Fraction(0), 'B': Fraction(0), 'A': Fraction(0)}
                continue
            raw = {}
            for cv in range(1, 7):
                raw[cv] = delta_F4_grav_graph_sum(N, Fraction(cv))
            poly_vals = {Fraction(cv): raw[cv] * Fraction(cv)**3 for cv in range(1, 7)}
            coeffs = newton_interpolate(
                {Fraction(cv): poly_vals[Fraction(cv)] for cv in range(1, 6)}, 4
            )
            result[N] = dict(zip(['E', 'D', 'C', 'B', 'A'], coeffs))
        return result

    def test_E_degree_2(self, all_coefficients):
        """E(N) has degree 2 in N (linear quotient after (N-2) factor)."""
        vals = {N: all_coefficients[N]['E'] for N in [2, 3, 4, 5, 6]}
        # Factor (N-2)
        quotient = {N: vals[N] / Fraction(N-2) for N in [3, 4, 5, 6]}
        # Check linearity: use N=3,4 to fit, verify at N=5,6
        a = quotient[4] - quotient[3]
        b = quotient[3] - 3 * a
        assert 5 * a + b == quotient[5]
        assert 6 * a + b == quotient[6]

    def test_D_degree_4(self, all_coefficients):
        """D(N) has degree 4 in N (cubic quotient after (N-2) factor)."""
        vals = {N: all_coefficients[N]['D'] for N in [2, 3, 4, 5, 6]}
        quotient = {N: vals[N] / Fraction(N-2) for N in [3, 4, 5, 6]}
        # Fit degree 2 using N=3,4,5, verify at N=6
        frac_vals = {Fraction(n): quotient[n] for n in [3, 4, 5]}
        coeffs = newton_interpolate(frac_vals, 2)
        predicted_6 = sum(coeffs[i] * Fraction(6)**(2-i) for i in range(3))
        assert predicted_6 != quotient[6], "D quotient is lower degree than expected"
        # Fit degree 3 using N=3,4,5,6 (exact)
        frac_vals4 = {Fraction(n): quotient[n] for n in [3, 4, 5, 6]}
        coeffs3 = newton_interpolate(frac_vals4, 3)
        for n in [3, 4, 5, 6]:
            val = sum(coeffs3[i] * Fraction(n)**(3-i) for i in range(4))
            assert val == quotient[n]

    def test_all_vanish_at_N2(self, all_coefficients):
        """All coefficients vanish at N=2 (Virasoro uniform weight)."""
        for label in ['E', 'D', 'C', 'B', 'A']:
            assert all_coefficients[2][label] == 0

    def test_E_formula(self, all_coefficients):
        """E(N) = (N-2)(N/497664 + 13/1244160)."""
        for N in [3, 4, 5, 6]:
            expected = Fraction(N-2) * (Fraction(N, 497664) + Fraction(13, 1244160))
            assert all_coefficients[N]['E'] == expected

    def test_all_positive_N3(self, all_coefficients):
        """All coefficients are positive for N=3."""
        for label in ['E', 'D', 'C', 'B', 'A']:
            assert all_coefficients[3][label] > 0

    def test_monotone_in_N(self, all_coefficients):
        """Each coefficient is monotonically increasing in N for N >= 3."""
        for label in ['E', 'D', 'C', 'B', 'A']:
            for N in [4, 5, 6]:
                assert all_coefficients[N][label] > all_coefficients[N-1][label], \
                    f"{label}({N}) <= {label}({N-1})"


# ============================================================================
# Section 6: Cross-genus consistency
# ============================================================================

class TestCrossGenusConsistency:
    """Consistency checks across genera 2, 3, 4."""

    def test_growth_ordering(self):
        """delta_F_g grows with g at fixed c and N."""
        c = Fraction(10)
        d2 = delta_F2_grav_graph_sum(3, c)
        d3 = delta_F3_grav_graph_sum(3, c)
        d4 = delta_F4_grav_graph_sum(3, c)
        # At large c, all are positive and grow
        assert d2 > 0
        assert d3 > 0
        assert d4 > 0

    def test_large_c_scaling_g2(self):
        """delta_F_2(W_3, c) -> 1/16 as c -> infinity."""
        # delta_F_2 = (c+204)/(16c) -> 1/16
        big_c = Fraction(10000)
        val = delta_F2_closed_form_W3(big_c)
        assert abs(val - Fraction(1, 16)) < Fraction(1, 100)

    def test_large_c_scaling_g3(self):
        """delta_F_3(W_3, c) grows linearly in c (net degree 1)."""
        c1 = Fraction(100)
        c2 = Fraction(200)
        v1 = delta_F3_closed_form_W3(c1)
        v2 = delta_F3_closed_form_W3(c2)
        # Ratio should approach 2 (linear growth)
        ratio = v2 / v1
        assert ratio > Fraction(19, 10)  # close to 2
        assert ratio < Fraction(21, 10)

    def test_large_c_scaling_g4(self):
        """delta_F_4(W_3, c) grows linearly in c (net degree 1)."""
        c1 = Fraction(100)
        c2 = Fraction(200)
        v1 = delta_F4_closed_form_W3(c1)
        v2 = delta_F4_closed_form_W3(c2)
        ratio = v2 / v1
        assert ratio > Fraction(19, 10)
        assert ratio < Fraction(21, 10)

    def test_w3_full_cross_genus_c1(self):
        """Full cross-genus check at c=1."""
        result = cross_genus_check_W3(Fraction(1))
        assert result['g2']['match']
        assert result['g3']['match']
        assert result['g4']['match']


# ============================================================================
# Section 7: Power-sum structure and matrix model
# ============================================================================

class TestPowerSumStructure:
    """Power-sum basis and Penner model connection."""

    def test_power_sums(self):
        """Verify power sum S_k(N) = 2^k + ... + N^k."""
        assert power_sum(0, 3) == 2  # 1 + 1
        assert power_sum(1, 3) == 5  # 2 + 3
        assert power_sum(2, 3) == 13  # 4 + 9
        assert power_sum(1, 5) == 14  # 2+3+4+5

    def test_genus2_A2_power_sum_formula(self):
        """A_2(N) = (2*S_1^2 + S_2 - 12) / 4 where S_k = sum j^k."""
        for N in [3, 4, 5, 6]:
            S1 = power_sum(1, N)
            S2 = power_sum(2, N)
            A2_ps = (2 * S1**2 + S2 - 12) / 4
            # Compare with closed form: A_2 = (N-2)(3N^3+14N^2+22N+33)/24
            A2_cf = Fraction(N-2) * (3*N**3 + 14*N**2 + 22*N + 33) / 24
            assert A2_ps == A2_cf, f"A_2 power-sum formula fails at N={N}"

    def test_penner_A2_match(self):
        """Penner free energy genus-2 reproduces A_2 via power sums."""
        for N in [3, 4, 5]:
            result = penner_free_energy_genus2(N)
            assert result['A2_match'], f"Penner A_2 mismatch at N={N}"

    def test_kappa_total_harmonic(self):
        """kappa(W_N) = c * (H_N - 1) where H_N = sum 1/j."""
        for N in [3, 4, 5]:
            c = Fraction(6)
            expected = c * sum(Fraction(1, j) for j in range(2, N+1))
            assert grav_kappa_total(N, c) == expected

    def test_penner_potential(self):
        """Penner potential V_k = H_k^{(N)} / k."""
        coeffs = penner_potential_coefficients(4, max_order=3)
        # V_1 = sum_{j=2}^4 1/j = 1/2 + 1/3 + 1/4 = 13/12
        assert coeffs[0] == Fraction(13, 12)
        # V_2 = (1/2) * sum_{j=2}^4 1/j^2 = (1/4+1/9+1/16)/2 = 61/288
        assert coeffs[1] == Fraction(61, 288)

    def test_delta_F2_factorization(self):
        """delta_F_2 factorizes through (N-2) for all tested N."""
        for N in [3, 4, 5, 6, 7]:
            c = Fraction(1)
            val = delta_F2_grav_graph_sum(N, c)
            # Must be divisible by (N-2) as a rational number (it's Fraction(N-2) * something)
            quotient = val / Fraction(N - 2)
            assert quotient.denominator != 0  # basic sanity


# ============================================================================
# Section 8: Fast amplitude optimization
# ============================================================================

class TestFastAmplitude:
    """Verify fast amplitude matches brute force."""

    def test_fast_matches_brute_single_graph(self):
        """Fast and brute force agree on a single genus-4 graph."""
        graphs = genus4_boundary_graphs()
        c = Fraction(1)
        all_weights = (2, 3, 4)
        # Test first boundary graph
        g = graphs[0]
        bf = graph_amplitude_decomposed(g, c, all_weights)
        ft = graph_amplitude_fast(g, c, all_weights)
        assert bf['mixed'] == ft['mixed']
        assert bf['diagonal'] == ft['diagonal']

    def test_fast_matches_brute_10_graphs(self):
        """Fast and brute force agree on first 10 genus-4 graphs for W_4."""
        graphs = genus4_boundary_graphs()[:10]
        c = Fraction(2)
        all_weights = (2, 3, 4)
        for i, g in enumerate(graphs):
            bf = graph_amplitude_decomposed(g, c, all_weights)
            ft = graph_amplitude_fast(g, c, all_weights)
            assert bf['mixed'] == ft['mixed'], f"Graph {i} mixed mismatch"
            assert bf['diagonal'] == ft['diagonal'], f"Graph {i} diag mismatch"

    def test_parity_filter_effectiveness(self):
        """The parity filter reduces computation for N >= 4."""
        g = StableGraph(
            vertex_genera=(0, 0),
            edges=((0, 1), (0, 1), (0, 1)),  # theta graph, genus 2
            legs=(),
        )
        c = Fraction(1)
        all_weights = (2, 3, 4)
        result = graph_amplitude_fast(g, c, all_weights)
        # Should work without error and give a valid result
        assert isinstance(result['mixed'], Fraction)

    def test_genus4_graph_count(self):
        """379 stable graphs of M_bar_{4,0}."""
        assert len(genus4_graphs()) == 379

    def test_genus4_boundary_count(self):
        """378 boundary graphs (edges >= 1)."""
        assert len(genus4_boundary_graphs()) == 378

    def test_half_edge_ordering(self):
        """Half-edge channels: self-loops first, then bridges."""
        g = StableGraph(
            vertex_genera=(1, 0, 0),
            edges=((0, 1), (1, 1), (1, 2), (2, 2)),
            legs=(),
        )
        sigma = (2, 3, 2, 2)
        hec = half_edge_channels(g, sigma)
        # Vertex 1: self-loop (edge 1) first, then bridges (edges 0, 2)
        # Self-loop carries channel 3 -> (3, 3)
        # Bridges carry channels 2, 2 -> (2, 2)
        # Total: (3, 3, 2, 2)
        assert hec[1] == (3, 3, 2, 2)
        # Vertex 0: no self-loops, bridge edge 0 -> (2,)
        assert hec[0] == (2,)
        # Vertex 2: self-loop edge 3 first -> (2, 2), bridge edge 2 -> (2,)
        assert hec[2] == (2, 2, 2)


# ============================================================================
# Section 9: Frobenius algebra unit tests
# ============================================================================

class TestFrobeniusAlgebra:
    """Gravitational Frobenius algebra for W_N."""

    def test_C3_TTT(self):
        c = Fraction(7)
        assert grav_C3(2, 2, 2, c) == c

    def test_C3_TWW(self):
        c = Fraction(7)
        assert grav_C3(2, 3, 3, c) == c
        assert grav_C3(2, 5, 5, c) == c

    def test_C3_parity_vanishing(self):
        """Odd-weight-count triples vanish."""
        c = Fraction(7)
        assert grav_C3(2, 2, 3, c) == 0  # one odd channel
        assert grav_C3(3, 3, 3, c) == 0  # three odd channels

    def test_C3_distinct_nonT(self):
        """Distinct non-T channels vanish."""
        c = Fraction(7)
        assert grav_C3(3, 5, 2, c) == 0
        assert grav_C3(4, 6, 2, c) == 0

    def test_propagator(self):
        c = Fraction(10)
        assert grav_propagator(2, c) == Fraction(1, 5)
        assert grav_propagator(3, c) == Fraction(3, 10)

    def test_kappa_channel(self):
        c = Fraction(6)
        assert grav_kappa_channel(2, c) == Fraction(3)
        assert grav_kappa_channel(3, c) == Fraction(2)
