r"""Tests for theorem_delta_f2_intersection_engine.

Tests the intersection-theoretic decomposition of delta_F_2(W_N, c) = B(N) + A(N)/c
on M-bar_{2,0}, verified against the established multi_weight_genus_tower engine.

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct formula evaluation
  Path 2: W_3 established engine cross-check
  Path 3: Per-graph A/B decomposition
  Path 4: Structural properties (vanishing, factorization, irreducibility)
  Path 5: Faber intersection number consistency
  Path 6: Asymptotic analysis
"""

from fractions import Fraction
import pytest

from compute.lib.theorem_delta_f2_intersection_engine import (
    # Formulas
    A_of_N,
    B_of_N,
    delta_F2_closed,
    cubic_residual,
    linear_residual,
    # Faber numbers
    lambda_fp,
    INT_MBAR2_LAMBDA2,
    INT_MBAR2_LAMBDA1_CUBED,
    INT_MBAR2_LAMBDA1_LAMBDA2,
    INT_MBAR2_KAPPA1_CUBED,
    INT_MBAR2_KAPPA1_KAPPA2,
    INT_MBAR2_KAPPA1_LAMBDA2,
    FABER_TABLE,
    # W_3
    w3_delta_F2,
    w3_per_graph_AB,
    # Proofs
    B_stratum_analysis,
    A_stratum_analysis,
    vanishing_at_N2,
    cubic_irreducibility,
    faber_connection,
    # Verification
    verify_W3_formula,
    verify_W3_per_graph,
    verify_AB_values,
    verify_faber_numbers,
    verify_asymptotic,
    verify_all,
    summary_table,
)


# ============================================================================
# PATH 1: Direct formula evaluation
# ============================================================================

class TestABFormulas:
    """Direct verification of the A(N) and B(N) formulas."""

    def test_A_at_N2(self):
        """A(2) = 0 (uniform weight vanishing)."""
        assert A_of_N(2) == Fraction(0)

    def test_B_at_N2(self):
        """B(2) = 0 (uniform weight vanishing)."""
        assert B_of_N(2) == Fraction(0)

    def test_A_at_N3(self):
        """A(3) = 51/4 (W_3 coefficient)."""
        assert A_of_N(3) == Fraction(51, 4)

    def test_B_at_N3(self):
        """B(3) = 1/16 (W_3 coefficient)."""
        assert B_of_N(3) == Fraction(1, 16)

    def test_A_at_N4(self):
        """A(4) = (2)(3*64+14*16+22*4+33)/24 = 2*537/24 = 179/4."""
        expected = Fraction(2) * Fraction(3*64 + 14*16 + 22*4 + 33, 24)
        assert A_of_N(4) == expected
        assert A_of_N(4) == Fraction(179, 4)

    def test_B_at_N4(self):
        """B(4) = (2)(7)/96 = 7/48."""
        assert B_of_N(4) == Fraction(7, 48)

    def test_A_at_N5(self):
        """A(5) = (3)(868)/24 = 217/2."""
        assert A_of_N(5) == Fraction(217, 2)

    def test_B_at_N5(self):
        """B(5) = (3)(8)/96 = 1/4."""
        assert B_of_N(5) == Fraction(1, 4)

    def test_A_at_N6(self):
        """A(6) = (4)(1317)/24 = 439/2."""
        expected = Fraction(4) * Fraction(3*216 + 14*36 + 22*6 + 33, 24)
        assert A_of_N(6) == expected

    def test_B_at_N6(self):
        """B(6) = (4)(9)/96 = 3/8."""
        assert B_of_N(6) == Fraction(3, 8)

    def test_delta_F2_at_N2_is_zero(self):
        """delta_F_2(W_2, c) = 0 for any c."""
        for cv in [1, 2, 5, 10, 26, 100]:
            assert delta_F2_closed(2, Fraction(cv)) == Fraction(0)

    def test_delta_F2_W3_formula(self):
        """delta_F_2(W_3, c) = (c+204)/(16c) for multiple c values."""
        for cv in [1, 2, 3, 5, 7, 10, 13, 26, 50, 100]:
            c = Fraction(cv)
            our = delta_F2_closed(3, c)
            expected = (c + 204) / (16 * c)
            assert our == expected, f"Mismatch at c={cv}: {our} != {expected}"

    def test_A_positive_for_N_geq_3(self):
        """A(N) > 0 for N >= 3."""
        for N in range(3, 20):
            assert A_of_N(N) > 0

    def test_B_positive_for_N_geq_3(self):
        """B(N) > 0 for N >= 3."""
        for N in range(3, 20):
            assert B_of_N(N) > 0

    def test_A_less_than_2_implies_zero(self):
        """A(N) = 0 for N < 2."""
        assert A_of_N(0) == Fraction(0)
        assert A_of_N(1) == Fraction(0)

    def test_B_less_than_2_implies_zero(self):
        """B(N) = 0 for N < 2."""
        assert B_of_N(0) == Fraction(0)
        assert B_of_N(1) == Fraction(0)


# ============================================================================
# PATH 2: W_3 established engine cross-check
# ============================================================================

class TestW3CrossCheck:
    """Cross-check against the established multi_weight_genus_tower engine."""

    def test_W3_closed_form_all_c(self):
        """Our formula matches (c+204)/(16c) at 9 c-values."""
        r = verify_W3_formula()
        assert r['all_match_closed']

    def test_W3_engine_match_all_c(self):
        """Our formula matches the established graph-sum engine at 9 c-values."""
        r = verify_W3_formula()
        assert r['all_match_engine']

    def test_W3_A3_value(self):
        """A(3) = 51/4 matches 204/16."""
        r = verify_W3_formula()
        assert r['A3_check']

    def test_W3_B3_value(self):
        """B(3) = 1/16."""
        r = verify_W3_formula()
        assert r['B3_check']

    def test_W3_at_c1(self):
        """delta_F_2(W_3, 1) via engine."""
        w3_val = w3_delta_F2(Fraction(1))
        our_val = delta_F2_closed(3, Fraction(1))
        assert w3_val is not None
        assert w3_val == our_val

    def test_W3_at_c26(self):
        """delta_F_2(W_3, 26) = 115/208 via engine."""
        w3_val = w3_delta_F2(Fraction(26))
        expected = (Fraction(26) + 204) / (16 * 26)
        assert w3_val is not None
        assert w3_val == expected

    def test_W3_at_c13_self_dual(self):
        """delta_F_2(W_3, 13) at the self-dual point."""
        w3_val = w3_delta_F2(Fraction(13))
        our_val = delta_F2_closed(3, Fraction(13))
        assert w3_val is not None
        assert w3_val == our_val


# ============================================================================
# PATH 3: Per-graph A/B decomposition
# ============================================================================

class TestPerGraphDecomposition:
    """Per-graph decomposition for W_3 from established engine."""

    @pytest.fixture
    def w3_data(self):
        data = w3_per_graph_AB()
        if data is None:
            pytest.skip("multi_weight_genus_tower not available")
        return data

    def test_lollipop_zero_mixed(self, w3_data):
        """Lollipop (1 edge): A=0, B=0."""
        assert w3_data['lollipop']['A'] == 0
        assert w3_data['lollipop']['B'] == 0

    def test_dumbbell_zero_mixed(self, w3_data):
        """Dumbbell (1 edge): A=0, B=0."""
        assert w3_data['dumbbell']['A'] == 0
        assert w3_data['dumbbell']['B'] == 0

    def test_banana_A(self, w3_data):
        """Banana: A=3, B=0."""
        assert w3_data['banana']['A'] == Fraction(3)
        assert w3_data['banana']['B'] == 0

    def test_theta_A(self, w3_data):
        """Theta: A=9/2, B=0."""
        assert w3_data['theta']['A'] == Fraction(9, 2)
        assert w3_data['theta']['B'] == 0

    def test_barbell_A(self, w3_data):
        """Barbell: A=21/4, B=0."""
        assert w3_data['barbell']['A'] == Fraction(21, 4)
        assert w3_data['barbell']['B'] == 0

    def test_lollipop_bridge_B(self, w3_data):
        """Lollipop-bridge: A=0, B=1/16."""
        assert w3_data['lollipop_bridge']['A'] == 0
        assert w3_data['lollipop_bridge']['B'] == Fraction(1, 16)

    def test_A_sum_matches(self, w3_data):
        """Sum of per-graph A = A(3) = 51/4."""
        A_sum = sum(d['A'] for d in w3_data.values())
        assert A_sum == A_of_N(3)

    def test_B_sum_matches(self, w3_data):
        """Sum of per-graph B = B(3) = 1/16."""
        B_sum = sum(d['B'] for d in w3_data.values())
        assert B_sum == B_of_N(3)

    def test_single_edge_graphs_zero_mixed(self, w3_data):
        """Graphs with 1 edge (lollipop, dumbbell) have zero mixed."""
        r = verify_W3_per_graph()
        assert r['single_edge_zero']

    def test_B_entirely_from_lollipop_bridge(self, w3_data):
        """B(3) comes entirely from the lollipop-bridge graph."""
        r = verify_W3_per_graph()
        assert r['B_from_lp_bridge_only']

    def test_A_entirely_from_genus0_vertices(self, w3_data):
        """A(3) comes entirely from genus-0-vertex graphs."""
        r = verify_W3_per_graph()
        assert r['A_from_genus0_only']

    def test_banana_plus_theta_plus_barbell(self, w3_data):
        """A(3) = A_banana + A_theta + A_barbell = 3 + 9/2 + 21/4 = 51/4."""
        total = Fraction(3) + Fraction(9, 2) + Fraction(21, 4)
        assert total == Fraction(51, 4)
        assert total == A_of_N(3)


# ============================================================================
# PATH 4: Structural properties
# ============================================================================

class TestStructuralProperties:
    """Vanishing, factorization, irreducibility."""

    def test_vanishing_at_N2(self):
        """delta_F_2 vanishes at N=2 (single-generator / uniform weight)."""
        v = vanishing_at_N2()
        assert v['A2_vanishes']
        assert v['B2_vanishes']

    def test_N_minus_2_divides_A(self):
        """(N-2) | A(N) for N = 2, ..., 20."""
        for N in range(2, 21):
            A = A_of_N(N)
            if N == 2:
                assert A == 0
            else:
                quotient = A / Fraction(N - 2)
                # Check quotient is a fraction with denominator dividing 24
                assert quotient * 24 == (quotient * 24).limit_denominator(1)

    def test_N_minus_2_divides_B(self):
        """(N-2) | B(N) for N = 2, ..., 20."""
        for N in range(2, 21):
            B = B_of_N(N)
            if N == 2:
                assert B == 0
            else:
                quotient = B / Fraction(N - 2)
                # Check quotient equals (N+3)/96
                assert quotient == Fraction(N + 3, 96)

    def test_cubic_irreducibility(self):
        """3N^3 + 14N^2 + 22N + 33 is irreducible over Q."""
        r = cubic_irreducibility()
        assert r['irreducible']

    def test_cubic_no_integer_roots(self):
        """No integer root of 3N^3 + 14N^2 + 22N + 33."""
        p = lambda n: 3*n**3 + 14*n**2 + 22*n + 33
        for n in [1, -1, 3, -3, 11, -11, 33, -33]:
            assert p(n) != 0

    def test_cubic_positive_for_N_geq_0(self):
        """3N^3 + 14N^2 + 22N + 33 > 0 for N >= 0."""
        for N in range(0, 100):
            assert cubic_residual(N) > 0

    def test_linear_residual(self):
        """B(N)/(N-2) = (N+3)/96."""
        for N in range(3, 20):
            assert B_of_N(N) / Fraction(N - 2) == Fraction(N + 3, 96)

    def test_cubic_residual_values(self):
        """Explicit cubic values: p(3)=306, p(4)=537, p(5)=868."""
        assert cubic_residual(3) == 306
        assert cubic_residual(4) == 537
        assert cubic_residual(5) == 868

    def test_A_residual_equals_cubic_over_24(self):
        """A(N)/(N-2) = p(N)/24 for N >= 3."""
        for N in range(3, 15):
            assert A_of_N(N) / Fraction(N - 2) == cubic_residual(N) / 24


# ============================================================================
# PATH 5: Faber intersection number consistency
# ============================================================================

class TestFaberNumbers:
    """Consistency of Faber intersection numbers."""

    def test_lambda_1_FP(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2_FP(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3_FP(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_int_lambda2_mbar2(self):
        """int_{M-bar_2} lambda_2 = 1/240."""
        assert INT_MBAR2_LAMBDA2 == Fraction(1, 240)

    def test_int_lambda1_cubed(self):
        """int_{M-bar_2} lambda_1^3 = 1/240."""
        assert INT_MBAR2_LAMBDA1_CUBED == Fraction(1, 240)

    def test_int_kappa1_lambda2(self):
        """int_{M-bar_2} kappa_1 lambda_2 = 7/5760 = lambda_2^FP."""
        assert INT_MBAR2_KAPPA1_LAMBDA2 == Fraction(7, 5760)
        assert INT_MBAR2_KAPPA1_LAMBDA2 == lambda_fp(2)

    def test_int_kappa1_cubed(self):
        """int_{M-bar_2} kappa_1^3 = 7/240."""
        assert INT_MBAR2_KAPPA1_CUBED == Fraction(7, 240)

    def test_int_lambda1_lambda2(self):
        """int_{M-bar_2} lambda_1 lambda_2 = 1/1152."""
        assert INT_MBAR2_LAMBDA1_LAMBDA2 == Fraction(1, 1152)

    def test_faber_table_lambda1_cubed(self):
        """Faber table: int lambda_1^3 = 1/240."""
        assert FABER_TABLE[(3, 0, 0)] == Fraction(1, 240)

    def test_faber_table_lambda1_sq_delta_irr(self):
        """Faber table: int lambda_1^2 delta_irr = 1/120."""
        assert FABER_TABLE[(2, 1, 0)] == Fraction(1, 120)

    def test_faber_table_lambda1_sq_delta_1(self):
        """Faber table: int lambda_1^2 delta_1 = 0."""
        assert FABER_TABLE[(2, 0, 1)] == Fraction(0)


# ============================================================================
# PATH 6: Asymptotic and ratio analysis
# ============================================================================

class TestAsymptoticProperties:
    """Asymptotic behavior of A(N) and B(N)."""

    def test_A_over_B_grows(self):
        """A(N)/B(N) is increasing for N >= 3."""
        ratios = []
        for N in range(3, 15):
            ratio = A_of_N(N) / B_of_N(N)
            ratios.append(ratio)
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i]

    def test_A_over_B_quadratic_growth(self):
        """A(N)/B(N) ~ 12N^2 at leading order: ratio / (12N^2) -> 1."""
        for N in [10, 15, 20, 50]:
            ratio = A_of_N(N) / B_of_N(N)
            normalized = ratio / Fraction(12 * N * N)
            # Should approach 1 (subleading corrections decrease with N)
            assert Fraction(7, 10) < normalized < Fraction(15, 10)

    def test_A_quartic_growth(self):
        """A(N) ~ N^4/8 at leading order."""
        for N in [10, 20, 50]:
            A = A_of_N(N)
            leading = Fraction(N**4, 8)
            ratio = A / leading
            assert Fraction(1, 2) < ratio < Fraction(3, 2)

    def test_B_quadratic_growth(self):
        """B(N) ~ N^2/96 at leading order."""
        for N in [10, 20, 50]:
            B = B_of_N(N)
            leading = Fraction(N**2, 96)
            ratio = B / leading
            assert Fraction(1, 2) < ratio < Fraction(3, 2)

    def test_delta_F2_dominated_by_A_at_small_c(self):
        """For small c, A(N)/c >> B(N)."""
        c = Fraction(1, 10)
        for N in range(3, 10):
            A_part = A_of_N(N) / c
            B_part = B_of_N(N)
            assert A_part > 10 * B_part

    def test_delta_F2_dominated_by_B_at_large_c(self):
        """For large c, B(N) >> A(N)/c."""
        c = Fraction(10**6)
        for N in range(5, 15):  # Use larger N where B is non-negligible
            A_part = A_of_N(N) / c
            B_part = B_of_N(N)
            assert B_part > 100 * A_part


# ============================================================================
# Stratum analysis tests
# ============================================================================

class TestStratumAnalysis:
    """Tests for the intersection-theoretic stratum decomposition."""

    def test_B_stratum_is_lollipop_bridge(self):
        """B(N) arises from the lollipop-bridge stratum."""
        r = B_stratum_analysis()
        assert r['stratum'] == 'lollipop-bridge [xi_5]'
        assert r['codimension'] == 2
        assert r['automorphism'] == 2

    def test_B_stratum_W3_match(self):
        """B(3) from stratum analysis matches formula."""
        r = B_stratum_analysis()
        if r['W3_match'] is not None:
            assert r['W3_match']

    def test_A_strata_are_genus0(self):
        """A(N) arises from genus-0-vertex strata."""
        r = A_stratum_analysis()
        assert 'banana [xi_2]' in r['strata']
        assert 'theta [xi_4]' in r['strata']
        assert 'barbell [xi_6]' in r['strata']

    def test_A_strata_codimensions(self):
        """Banana is codim 2; theta and barbell are codim 3."""
        r = A_stratum_analysis()
        assert r['codimensions'] == [2, 3, 3]

    def test_A_W3_decomposition_match(self):
        """Per-graph A decomposition for W_3 matches A(3)."""
        r = A_stratum_analysis()
        if 'W3_per_graph' in r:
            assert r['W3_per_graph']['match']

    def test_faber_connection_gorenstein(self):
        """M-bar_{2,0} has Gorenstein duality."""
        r = faber_connection()
        assert r['gorenstein']
        assert r['socle_degree'] == 3

    def test_faber_connection_mumford(self):
        """Mumford relation: 10 lambda_1 = delta_irr + 2 delta_1."""
        r = faber_connection()
        assert r['mumford_relation'] == '10 lambda_1 = delta_irr + 2 delta_1'


# ============================================================================
# Master verification
# ============================================================================

class TestMasterVerification:
    """Run the complete verification suite."""

    def test_verify_all_passes(self):
        """All 15 verification checks pass."""
        results = verify_all()
        for key, val in results.items():
            assert val, f"Verification failed: {key}"

    def test_summary_table_N2_zero(self):
        """Summary table at N=2 shows zero correction."""
        table = summary_table(3)
        row2 = [r for r in table if r['N'] == 2][0]
        assert row2['A'] == 0
        assert row2['B'] == 0

    def test_summary_table_N3_correct(self):
        """Summary table at N=3 shows correct values."""
        table = summary_table(4)
        row3 = [r for r in table if r['N'] == 3][0]
        assert row3['A'] == Fraction(51, 4)
        assert row3['B'] == Fraction(1, 16)
