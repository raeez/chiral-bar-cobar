r"""Tests for Penner matrix model delta_F_2 engine.

Multi-path verification (AP10, CLAUDE.md mandate):
  Path 1: Power sum formula A_2 = (2*S_1^2 + S_2 - 12)/4
  Path 2: Explicit polynomial A_2 = (N-2)(3N^3+14N^2+22N+33)/24
  Path 3: Graph decomposition A_2 = FE + Th + SR
  Path 4: Shifted moment formula A_2 = T_1*(T_1+4)/2 + T_2/4
  Path 5: Cross-check against a2_polynomial_combinatorics_engine
  Path 6: Discrete model cumulant analysis
  Path 7: Limiting cases (N=2 vanishing, large N asymptotics)
"""

import pytest
from fractions import Fraction

from compute.lib.penner_matrix_model_delta_f2_engine import (
    power_sum,
    S1, S2, S3, S4,
    delta_F2_A2,
    delta_F2_A2_polynomial,
    delta_F2_B2,
    delta_F2_full,
    penner_F2_exact,
    lambda_fp,
    vandermonde_squared,
    discrete_model_moments,
    discrete_model_connected_correlators,
    genus2_from_power_sums,
    penner_multi_matrix_genus2,
    discrete_spectral_curve,
    delta_f2_generating_function,
    penner_deformed_potential,
    a2_as_resolvent_moment,
    theorem_matrix_model_delta_f2,
)

# Import the independent engine for cross-checks (Path 5)
from compute.lib.a2_polynomial_combinatorics_engine import (
    A2_polynomial as A2_poly_independent,
    A2_power_sums as A2_ps_independent,
    A2_symmetric as A2_sym_independent,
    A2_figure_eight,
    A2_theta,
    A2_sunrise,
    B2_polynomial as B2_poly_independent,
    B2_power_sum as B2_ps_independent,
    p1 as p1_independent,
    p2 as p2_independent,
)


# ============================================================================
# I. Power sum consistency (3-path verification)
# ============================================================================

class TestPowerSums:
    """Power sums S_k verified by 3 independent methods."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_S1_two_formulas(self, N):
        """S_1 via summation vs closed form N(N+1)/2 - 1."""
        direct = sum(Fraction(j) for j in range(2, N + 1))
        closed = Fraction(N * (N + 1), 2) - 1
        assert S1(N) == direct == closed

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_S2_two_formulas(self, N):
        """S_2 via summation vs closed form."""
        direct = sum(Fraction(j) ** 2 for j in range(2, N + 1))
        closed = Fraction(N * (N + 1) * (2 * N + 1), 6) - 1
        assert S2(N) == direct == closed

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 8])
    def test_S1_cross_engine(self, N):
        """S_1 matches independent engine."""
        assert S1(N) == p1_independent(N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 8])
    def test_S2_cross_engine(self, N):
        """S_2 matches independent engine."""
        assert S2(N) == p2_independent(N)

    def test_S1_specific_values(self):
        """S_1 at specific N values, computed by hand."""
        assert S1(2) == 2
        assert S1(3) == 5       # 2 + 3
        assert S1(4) == 9       # 2 + 3 + 4
        assert S1(5) == 14      # 2 + 3 + 4 + 5

    def test_S2_specific_values(self):
        """S_2 at specific N values, computed by hand."""
        assert S2(2) == 4
        assert S2(3) == 13      # 4 + 9
        assert S2(4) == 29      # 4 + 9 + 16


# ============================================================================
# II. A_2(N) four-path verification
# ============================================================================

class TestA2FourPath:
    """A_2(N) verified by 4 independent representations."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_power_sum_vs_polynomial(self, N):
        """Path 1 vs Path 2: power sum formula = explicit polynomial."""
        assert delta_F2_A2(N) == delta_F2_A2_polynomial(N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_power_sum_vs_graph_decomposition(self, N):
        """Path 1 vs Path 3: power sum = FE + Th + SR."""
        result = genus2_from_power_sums(N)
        assert result['A2_consistency']
        assert result['A2_total'] == result['A2_direct']

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_power_sum_vs_shifted_moment(self, N):
        """Path 1 vs Path 4: power sum = shifted moment formula."""
        result = a2_as_resolvent_moment(N)
        assert result['consistent']
        assert result['A2_from_shifted_moments'] == result['A2_from_power_sums']

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_cross_engine_polynomial(self, N):
        """Path 5: cross-check against independent a2_polynomial engine."""
        assert delta_F2_A2_polynomial(N) == A2_poly_independent(N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_cross_engine_power_sum(self, N):
        """Path 5b: cross-check power sum representation."""
        assert delta_F2_A2(N) == A2_ps_independent(N)

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_cross_engine_symmetric(self, N):
        """Path 5c: cross-check elementary symmetric representation."""
        assert delta_F2_A2(N) == A2_sym_independent(N)

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_graph_decomposition_cross_engine(self, N):
        """Path 3 vs Path 5: graph pieces match independent engine."""
        result = genus2_from_power_sums(N)
        assert result['A2_FE'] == A2_figure_eight(N)
        assert result['A2_Th'] == A2_theta(N)
        assert result['A2_SR'] == A2_sunrise(N)


# ============================================================================
# III. B_2(N) two-path verification
# ============================================================================

class TestB2TwoPath:
    """B_2(N) verified by 2 independent representations + cross-engine."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_B2_cross_engine_polynomial(self, N):
        """B_2 matches independent polynomial formula."""
        assert delta_F2_B2(N) == B2_ps_independent(N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 8])
    def test_B2_cross_engine_direct(self, N):
        """B_2 matches independent direct formula."""
        assert delta_F2_B2(N) == B2_poly_independent(N)


# ============================================================================
# IV. Limiting cases (Path 7)
# ============================================================================

class TestLimitingCases:
    """Limiting cases for validation."""

    def test_virasoro_vanishes(self):
        """N=2 (Virasoro only): A_2(2) = 0, B_2(2) = 0."""
        assert delta_F2_A2(2) == 0
        assert delta_F2_B2(2) == 0
        assert delta_F2_full(2, Fraction(100)) == 0

    def test_w3_A2_value(self):
        """N=3 (W_3): A_2(3) = 51/4.

        From S_1(3)=5, S_2(3)=13:
        A_2 = (2*25 + 13 - 12)/4 = 51/4.
        """
        assert delta_F2_A2(3) == Fraction(51, 4)

    def test_w3_A2_polynomial_value(self):
        """N=3 polynomial: (3-2)(3*27+14*9+22*3+33)/24 = (81+126+66+33)/24 = 306/24 = 51/4."""
        val = (3 - 2) * (3 * 27 + 14 * 9 + 22 * 3 + 33)
        assert val == 306
        assert Fraction(306, 24) == Fraction(51, 4)
        assert delta_F2_A2_polynomial(3) == Fraction(51, 4)

    def test_w3_B2_value(self):
        """N=3: B_2(3) = (5-2)/48 = 1/16."""
        assert delta_F2_B2(3) == Fraction(1, 16)

    def test_w3_delta_F2_at_c_equals_100(self):
        """delta_F_2(W_3, c=100) = 1/16 + 51/(4*100) = 1/16 + 51/400."""
        c = Fraction(100)
        expected = Fraction(1, 16) + Fraction(51, 400)
        assert delta_F2_full(3, c) == expected

    def test_w4_A2_value(self):
        """N=4: A_2(4) = (2*81 + 29 - 12)/4 = 179/4 from power sums.

        S_1(4)=9, S_2(4)=29.
        """
        assert S1(4) == 9
        assert S2(4) == 29
        expected = (2 * Fraction(81) + 29 - 12) / 4
        assert expected == Fraction(179, 4)
        assert delta_F2_A2(4) == Fraction(179, 4)

    def test_a2_positive_for_N_ge_3(self):
        """A_2(N) > 0 for all N >= 3."""
        for N in range(3, 15):
            assert delta_F2_A2(N) > 0

    def test_a2_growth_rate(self):
        """A_2(N) ~ N^4/8 for large N (leading coefficient is 3/24 = 1/8)."""
        N = 100
        a2 = delta_F2_A2_polynomial(N)
        asymptotic = Fraction(N ** 4, 8)
        ratio = a2 / asymptotic
        # Ratio should approach 1 as N -> inf
        assert Fraction(9, 10) < ratio < Fraction(11, 10)


# ============================================================================
# V. Shifted moment decomposition
# ============================================================================

class TestShiftedMoments:
    """Tests for the shifted moment formula T_k = S_k - 2^k."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_shifted_moment_formula(self, N):
        """A_2 = T_1*(T_1+4)/2 + T_2/4 matches power sum formula."""
        s1 = S1(N)
        s2 = S2(N)
        t1 = s1 - 2
        t2 = s2 - 4
        shifted = t1 * (t1 + 4) / 2 + t2 / 4
        power = (2 * s1 ** 2 + s2 - 12) / 4
        assert shifted == power

    def test_shifted_virasoro_zero(self):
        """At N=2: T_1=0, T_2=0, so shifted formula gives 0."""
        assert S1(2) - 2 == 0
        assert S2(2) - 4 == 0

    def test_shifted_w3(self):
        """At N=3: T_1=3, T_2=9, shifted = 3*7/2 + 9/4 = 51/4."""
        t1, t2 = Fraction(3), Fraction(9)
        assert t1 * (t1 + 4) / 2 + t2 / 4 == Fraction(51, 4)


# ============================================================================
# VI. Discrete model analysis
# ============================================================================

class TestDiscreteModel:
    """Tests for the discrete eigenvalue model."""

    def test_vandermonde_consecutive(self):
        """Vandermonde^2 for {2,3} is (3-2)^2 = 1."""
        assert vandermonde_squared([2, 3]) == 1

    def test_vandermonde_three(self):
        """Vandermonde^2 for {2,3,4} is (1)^2*(2)^2*(1)^2 = 4."""
        assert vandermonde_squared([2, 3, 4]) == 4

    def test_vandermonde_four(self):
        """Vandermonde^2 for {2,3,4,5}: computed from definition."""
        v = vandermonde_squared([2, 3, 4, 5])
        # (3-2)^2*(4-2)^2*(5-2)^2*(4-3)^2*(5-3)^2*(5-4)^2
        # = 1 * 4 * 9 * 1 * 4 * 1 = 144
        assert v == 144

    def test_discrete_moments_match_power_sums(self):
        """Discrete model moments mu_k = S_k/(N-1) match."""
        for N in [3, 4, 5, 6]:
            M = N - 1
            moments = discrete_model_moments(N, 4)
            assert moments[1] == S1(N) / M
            assert moments[2] == S2(N) / M

    def test_discrete_variance_positive(self):
        """Variance of the discrete measure is positive for N >= 3."""
        for N in [3, 4, 5, 6, 7]:
            corr = discrete_model_connected_correlators(N)
            assert corr['variance'] > 0

    def test_spectral_curve_genus_zero(self):
        """Discrete model spectral curve has genus 0."""
        for N in [3, 4, 5, 6]:
            sc = discrete_spectral_curve(N)
            assert sc['genus_spectral_curve'] == 0

    def test_spectral_curve_branch_points(self):
        """Number of branch points = N - 2."""
        for N in [3, 4, 5, 6, 7]:
            sc = discrete_spectral_curve(N)
            assert sc['num_branch_points'] == N - 2


# ============================================================================
# VII. Penner model comparison
# ============================================================================

class TestPennerComparison:
    """Tests comparing Penner model with shadow tower."""

    def test_penner_F2_exact(self):
        """Penner F_2 = -1/240 (Harer-Zagier)."""
        assert penner_F2_exact(0) == Fraction(-1, 240)

    def test_lambda_2_FP(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_1_FP(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_penner_ne_shadow(self):
        """Penner F_2 != lambda_2^FP (different generating functions)."""
        assert penner_F2_exact(0) != lambda_fp(2)

    def test_penner_multi_matrix_data(self):
        """Multi-matrix Penner model returns valid data."""
        result = penner_multi_matrix_genus2(3, Fraction(100))
        assert result['delta_F2'] == delta_F2_full(3, Fraction(100))
        assert result['lambda_2_FP'] == Fraction(7, 5760)

    def test_penner_deformed_potential_poles(self):
        """Deformed Penner potential has poles at generator weights."""
        for N in [3, 4, 5]:
            result = penner_deformed_potential(N)
            assert result['poles'] == list(range(2, N + 1))
            assert result['num_generators'] == N - 1


# ============================================================================
# VIII. Generating function analysis
# ============================================================================

class TestGeneratingFunction:
    """Tests for the generating function of A_2(N)."""

    def test_gf_consistency(self):
        """All A_2 values in the generating function are consistent."""
        result = delta_f2_generating_function(10)
        for N in range(2, 11):
            assert result['values'][N]['A2'] == result['values'][N]['A2_polynomial']

    def test_gf_thooft(self):
        """The 't Hooft parameter is S_1 (sum of weights)."""
        result = delta_f2_generating_function(8)
        assert 'S_1' in result['thooft_parameter']


# ============================================================================
# IX. Full theorem
# ============================================================================

class TestFullTheorem:
    """Tests for the comprehensive theorem statement."""

    def test_theorem_consistent(self):
        """All formulas are internally consistent."""
        result = theorem_matrix_model_delta_f2(8)
        assert result['all_consistent']

    def test_theorem_virasoro(self):
        """Virasoro (N=2) has no cross-channel correction."""
        result = theorem_matrix_model_delta_f2(8)
        assert result['virasoro_vanishes']

    def test_theorem_w3_value(self):
        """W_3 A_2 has the correct value."""
        result = theorem_matrix_model_delta_f2(8)
        assert result['w3_correct']
        assert result['w3_A2'] == Fraction(51, 4)

    def test_negative_result_stated(self):
        """The negative result (no classical spectral curve) is recorded."""
        result = theorem_matrix_model_delta_f2(5)
        assert 'No classical spectral curve' in result['negative_result']

    def test_positive_result_stated(self):
        """The positive result (moment polynomial) is recorded."""
        result = theorem_matrix_model_delta_f2(5)
        assert 'moment polynomial' in result['positive_result']


# ============================================================================
# X. Cross-family consistency (AP10 multi-path)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family tests that A_2(N) is consistent across representations."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8, 9, 10])
    def test_all_four_paths_agree(self, N):
        """All four independent A_2 representations agree at each N.

        Path 1: Power sum (2*S_1^2 + S_2 - 12)/4
        Path 2: Polynomial (N-2)(3N^3+14N^2+22N+33)/24
        Path 3: Graph decomposition FE + Th + SR
        Path 4: Shifted moments T_1*(T_1+4)/2 + T_2/4
        """
        path1 = delta_F2_A2(N)
        path2 = delta_F2_A2_polynomial(N)
        path3_data = genus2_from_power_sums(N)
        path3 = path3_data['A2_total']
        path4_data = a2_as_resolvent_moment(N)
        path4 = path4_data['A2_from_shifted_moments']
        assert path1 == path2 == path3 == path4

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_five_path_with_cross_engine(self, N):
        """Five paths agree: includes independent engine cross-check."""
        path1 = delta_F2_A2(N)
        path5a = A2_poly_independent(N)
        path5b = A2_ps_independent(N)
        path5c = A2_sym_independent(N)
        assert path1 == path5a == path5b == path5c

    def test_additivity_delta_f2(self):
        """delta_F_2 has the correct additive structure.

        A_2(N+1) - A_2(N) should equal the contribution from adding
        the weight-(N+1) generator.

        Adding weight h = N+1:
        New S_1 = old S_1 + (N+1)
        New S_2 = old S_2 + (N+1)^2
        Delta A_2 = [(2*(S1+h)^2 + (S2+h^2) - 12) - (2*S1^2 + S2 - 12)] / 4
                  = [4*S1*h + 2*h^2 + h^2] / 4
                  = [4*S1*h + 3*h^2] / 4
                  = h*(4*S1 + 3*h) / 4
        """
        for N in range(3, 10):
            h = N + 1
            s1 = S1(N)
            expected_increment = Fraction(h) * (4 * s1 + 3 * h) / 4
            actual_increment = delta_F2_A2(N + 1) - delta_F2_A2(N)
            assert actual_increment == expected_increment

    def test_b2_additivity(self):
        """B_2(N+1) - B_2(N) = (N+1)/48."""
        for N in range(2, 10):
            h = N + 1
            increment = delta_F2_B2(N + 1) - delta_F2_B2(N)
            assert increment == Fraction(h, 48)
