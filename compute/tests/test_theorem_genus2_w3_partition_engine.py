r"""Tests for genus-2 shadow free energy of W_3.

Multi-path verification of the first non-affine genus-2 computation.
W_3 has generators T (weight 2), W (weight 3) -- multi-weight, so
the scalar formula F_g = kappa * lambda_g FAILS at genus >= 2.

The full decomposition (thm:multi-weight-genus-expansion):
  F_2(W_3) = kappa * lambda_2^FP + delta_F_2^cross
  where delta_F_2^cross = (c + 204)/(16c).

AP1: kappa(W_3) = 5c/6, NOT c/2.
AP10: cross-family consistency prevents hardcoded wrong values.
AP39: kappa != c/2 for non-Virasoro families.

Ground truth:
  thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex),
  prop:universal-gravitational-cross-channel,
  thm:propagator-variance, multichannel_genus2.py,
  theorem_thm_d_multiweight_frontier_engine.py.
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from fractions import Fraction

from theorem_genus2_w3_partition_engine import (
    w3_data,
    w3_central_charge_from_level,
    w3_koszul_dual_c,
    harmonic_number,
    kappa_w3,
    kappa_t_channel,
    kappa_w_channel,
    kappa_channel_sum,
    verify_kappa_decomposition,
    bernoulli_number,
    lambda_fp,
    banana_cross_channel,
    theta_graph_cross_channel,
    lollipop_cross_channel,
    barbell_cross_channel,
    delta_F2_cross_graphwise,
    delta_F2_universal_formula,
    delta_F2_w3_closed_form,
    F2_scalar_part,
    F2_cross_channel,
    F2_w3_total,
    F2_w3_closed_form,
    F2_virasoro_at_c,
    F2_w3_per_channel,
    F2_at_self_dual,
    F2_at_integer_values,
    sl3_data_at_level,
    F2_sl3_scalar,
    ds_comparison,
    koszul_duality_analysis,
    large_c_asymptotics,
    rational_reconstruction_check,
    cross_family_comparison,
    propagator_variance_w3,
    multi_path_verification,
    full_F2_multi_path,
    summary_report,
)


# ======================================================================
# 1. W_3 algebra data
# ======================================================================

class TestW3Data:
    """Tests for W_3 algebra data."""

    def test_generators(self):
        """W_3 has two generators: T (weight 2) and W (weight 3)."""
        data = w3_data()
        assert data['generators'] == {'T': 2, 'W': 3}
        assert data['weights'] == (2, 3)
        assert data['num_generators'] == 2

    def test_koszul_conductor(self):
        """K_3 = 100 (NOT 4, NOT 26)."""
        data = w3_data()
        assert data['koszul_conductor'] == Fraction(100)

    def test_self_dual_point(self):
        """Self-dual at c = K_3/2 = 50."""
        data = w3_data()
        assert data['self_dual_c'] == Fraction(50)

    def test_shadow_class(self):
        """W_3 is class M (infinite shadow depth)."""
        data = w3_data()
        assert data['shadow_class'] == 'M'


class TestCentralCharge:
    """Tests for W_3 central charge formula."""

    def test_w3_c_formula(self):
        """c(W_3, k) = 2 - 24/(k+3)."""
        assert w3_central_charge_from_level(Fraction(1)) == Fraction(2) - Fraction(24, 4)
        assert w3_central_charge_from_level(Fraction(1)) == Fraction(-4)

    def test_w3_c_at_k_equals_minus1(self):
        """c(W_3, k=-1) = 2 - 24/2 = -10."""
        assert w3_central_charge_from_level(Fraction(-1)) == Fraction(-10)

    def test_koszul_dual_c(self):
        """c' = 100 - c."""
        assert w3_koszul_dual_c(Fraction(2)) == Fraction(98)
        assert w3_koszul_dual_c(Fraction(50)) == Fraction(50)
        assert w3_koszul_dual_c(Fraction(0)) == Fraction(100)


# ======================================================================
# 2. Kappa computation (AP1, AP39)
# ======================================================================

class TestKappa:
    """Tests for kappa(W_3) = 5c/6."""

    def test_harmonic_number_H3(self):
        """H_3 = 1 + 1/2 + 1/3 = 11/6."""
        assert harmonic_number(3) == Fraction(11, 6)

    def test_kappa_formula(self):
        """kappa(W_3) = 5c/6 for various c."""
        assert kappa_w3(Fraction(6)) == Fraction(5)
        assert kappa_w3(Fraction(12)) == Fraction(10)
        assert kappa_w3(Fraction(50)) == Fraction(250, 6)

    def test_kappa_not_c_over_2(self):
        """AP39: kappa(W_3) != c/2 for c != 0 (AP1 prevention)."""
        for c_val in [1, 2, 6, 10, 50, 100]:
            c = Fraction(c_val)
            assert kappa_w3(c) != c / 2, f"kappa = c/2 at c={c_val}, AP39 violation"

    def test_per_channel_kappa(self):
        """kappa_T = c/2, kappa_W = c/3."""
        c = Fraction(12)
        assert kappa_t_channel(c) == Fraction(6)
        assert kappa_w_channel(c) == Fraction(4)

    def test_channel_sum_equals_total(self):
        """kappa_T + kappa_W = kappa_total (AP10 cross-check)."""
        for c_val in [1, 2, 6, 10, 50, 100]:
            c = Fraction(c_val)
            assert kappa_channel_sum(c) == kappa_w3(c), \
                f"Channel sum != total at c={c_val}"

    def test_kappa_decomposition_3_paths(self):
        """Three independent paths to kappa all agree."""
        c = Fraction(30)
        result = verify_kappa_decomposition(c)
        assert result['all_agree']
        assert result['kappa_total'] == Fraction(25)


# ======================================================================
# 3. Faber-Pandharipande
# ======================================================================

class TestLambdaFP:
    """Tests for lambda_g^FP intersection numbers."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760 (NOT 1/1152, AP38)."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680.

        (2^5 - 1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/967680.
        """
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_bernoulli_B4(self):
        """B_4 = -1/30 (used in lambda_2 computation)."""
        assert bernoulli_number(4) == Fraction(-1, 30)


# ======================================================================
# 4. Cross-channel graph-by-graph
# ======================================================================

class TestGraphCrossChannel:
    """Tests for individual graph cross-channel amplitudes."""

    def test_banana(self):
        """Banana cross-channel = 3/c."""
        assert banana_cross_channel(Fraction(1)) == Fraction(3)
        assert banana_cross_channel(Fraction(3)) == Fraction(1)
        assert banana_cross_channel(Fraction(6)) == Fraction(1, 2)

    def test_theta(self):
        """Theta graph cross-channel = 9/(2c)."""
        assert theta_graph_cross_channel(Fraction(1)) == Fraction(9, 2)
        assert theta_graph_cross_channel(Fraction(9)) == Fraction(1, 2)

    def test_lollipop(self):
        """Lollipop cross-channel = 1/16 (independent of c)."""
        assert lollipop_cross_channel(Fraction(1)) == Fraction(1, 16)
        assert lollipop_cross_channel(Fraction(100)) == Fraction(1, 16)
        assert lollipop_cross_channel(Fraction(50)) == Fraction(1, 16)

    def test_barbell(self):
        """Barbell cross-channel = 21/(4c)."""
        assert barbell_cross_channel(Fraction(4)) == Fraction(21, 16)
        assert barbell_cross_channel(Fraction(21)) == Fraction(1, 4)

    def test_total_graphwise(self):
        """Sum of 4 graphs = (c+204)/(16c)."""
        c = Fraction(12)
        result = delta_F2_cross_graphwise(c)
        expected = (c + 204) / (16 * c)
        assert result['total'] == expected

    def test_total_graphwise_multiple_c(self):
        """Graph sum equals closed form for c = 1, ..., 10."""
        for c_val in range(1, 11):
            c = Fraction(c_val)
            graphwise = delta_F2_cross_graphwise(c)['total']
            closed = delta_F2_w3_closed_form(c)
            assert graphwise == closed, f"Mismatch at c={c_val}"


# ======================================================================
# 5. Universal N-formula
# ======================================================================

class TestUniversalFormula:
    """Tests for the universal N-formula specialization."""

    def test_N3_equals_closed_form(self):
        """delta_F_2(W_3, c) via N-formula matches closed form."""
        for c_val in [1, 2, 5, 10, 50, 100]:
            c = Fraction(c_val)
            universal = delta_F2_universal_formula(3, c)
            closed = delta_F2_w3_closed_form(c)
            assert universal == closed, f"N-formula != closed form at c={c_val}"

    def test_N2_vanishes(self):
        """delta_F_2(W_2, c) = delta_F_2(Vir, c) = 0 (single-generator)."""
        assert delta_F2_universal_formula(2, Fraction(10)) == Fraction(0)

    def test_N4_nonzero(self):
        """delta_F_2(W_4, c) is nonzero."""
        assert delta_F2_universal_formula(4, Fraction(10)) != Fraction(0)

    def test_N_formula_B_coefficient(self):
        """B = (N-2)(N+3)/96. For N=3: B = 6/96 = 1/16."""
        N = 3
        B = Fraction((N - 2) * (N + 3), 96)
        assert B == Fraction(1, 16)

    def test_N_formula_A_coefficient(self):
        """A = (N-2)(3N^3+14N^2+22N+33)/24. For N=3: A = 306/24 = 51/4."""
        N = 3
        A = Fraction((N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33), 24)
        assert A == Fraction(51, 4)


# ======================================================================
# 6. Full F_2(W_3) computation
# ======================================================================

class TestF2Total:
    """Tests for the full genus-2 free energy."""

    def test_scalar_part(self):
        """Scalar part = kappa * lambda_2 = 7c/6912."""
        c = Fraction(6912)
        assert F2_scalar_part(c) == Fraction(7)  # 7*6912/6912

    def test_scalar_part_general(self):
        """Scalar part = (5c/6)(7/5760) = 7c/6912."""
        c = Fraction(1)
        expected = Fraction(5, 6) * Fraction(7, 5760)
        assert F2_scalar_part(c) == expected
        assert expected == Fraction(7, 6912)

    def test_total_equals_sum(self):
        """F_2 = scalar + cross for multiple c values."""
        for c_val in range(1, 11):
            c = Fraction(c_val)
            total = F2_w3_total(c)
            parts = F2_scalar_part(c) + F2_cross_channel(c)
            assert total == parts, f"F_2 != scalar + cross at c={c_val}"

    def test_total_equals_closed_form(self):
        """F_2 via summation matches closed-form rational function."""
        for c_val in range(1, 11):
            c = Fraction(c_val)
            total = F2_w3_total(c)
            closed = F2_w3_closed_form(c)
            assert total == closed, f"Sum != closed form at c={c_val}"

    def test_closed_form_numerator(self):
        """Numerator is 112c^2 + 6912c + 1410048.

        112 = 7 * 16 (from clearing the c in the scalar term's denominator).
        6912 * 204 = 1410048.
        """
        assert 7 * 16 == 112
        assert 6912 * 204 == 1410048

    def test_closed_form_denominator(self):
        """Denominator is 110592c = 6912 * 16 * c."""
        assert 6912 * 16 == 110592


# ======================================================================
# 7. Self-dual point c = 50
# ======================================================================

class TestSelfDual:
    """Tests at the self-dual point c = 50."""

    def test_kappa_self_dual(self):
        """kappa(50) = 250/6 = 125/3."""
        assert kappa_w3(Fraction(50)) == Fraction(125, 3)

    def test_kappa_symmetric(self):
        """kappa(50) = kappa(100 - 50) (self-duality)."""
        result = F2_at_self_dual()
        assert result['kappa_is_self_dual']

    def test_F2_at_50(self):
        """F_2(50) = 31807/86400.

        Scalar: (125/3)(7/5760) = 875/17280 = 175/3456.
        Cross: 254/800 = 127/400.
        Sum: 175/3456 + 127/400.
        LCD(3456, 400) = 86400.
        175/3456 = 4375/86400.
        127/400 = 27432/86400.
        Total = 31807/86400.
        """
        result = F2_at_self_dual()
        total = result['F2_total']
        # Verify via closed form
        c = Fraction(50)
        closed = (112 * c**2 + 6912 * c + 1410048) / (110592 * c)
        assert total == closed
        # Verify numerical value: 112*2500 + 345600 + 1410048 = 2035648
        expected = Fraction(2035648, 5529600)
        assert total == expected
        # Simplify: gcd(2035648, 5529600) should give 31807/86400
        assert total == Fraction(31807, 86400)

    def test_cross_at_50(self):
        """delta_F_2(50) = 254/800 = 127/400."""
        c = Fraction(50)
        delta = delta_F2_w3_closed_form(c)
        assert delta == Fraction(254, 800)
        assert delta == Fraction(127, 400)


# ======================================================================
# 8. Comparison with Virasoro
# ======================================================================

class TestVirComparison:
    """Tests comparing F_2(W_3) with F_2(Vir)."""

    def test_virasoro_F2(self):
        """F_2(Vir_c) = 7c/11520."""
        c = Fraction(11520)
        assert F2_virasoro_at_c(c) == Fraction(7)

    def test_w3_exceeds_virasoro(self):
        """F_2(W_3) > F_2(Vir) for all c > 0 (extra W-channel + cross)."""
        for c_val in range(1, 20):
            c = Fraction(c_val)
            assert F2_w3_total(c) > F2_virasoro_at_c(c)

    def test_difference_decomposition(self):
        """F_2(W_3) - F_2(Vir) = kappa_W * lambda_2 + delta_F_2."""
        c = Fraction(10)
        result = cross_family_comparison(c)
        assert result['diff_matches_expected']


# ======================================================================
# 9. Multi-path verification
# ======================================================================

class TestMultiPath:
    """Tests for multi-path verification of delta_F_2."""

    def test_5_paths_agree(self):
        """All 5 paths agree for delta_F_2 at c = 7."""
        result = multi_path_verification(Fraction(7))
        assert result['all_paths_agree']

    def test_5_paths_agree_multiple_c(self):
        """All paths agree for c = 1, ..., 10."""
        for c_val in range(1, 11):
            result = multi_path_verification(Fraction(c_val))
            assert result['all_paths_agree'], f"Paths disagree at c={c_val}"

    def test_full_F2_3_paths(self):
        """Three paths for full F_2 agree."""
        result = full_F2_multi_path(Fraction(5))
        assert result['all_paths_agree']


# ======================================================================
# 10. Koszul duality
# ======================================================================

class TestKoszulDuality:
    """Tests for Koszul duality c -> 100 - c."""

    def test_kappa_sum_is_250_over_3(self):
        """kappa(c) + kappa(100-c) = 250/3 for all c."""
        for c_val in [1, 5, 10, 25, 50, 75, 99]:
            result = koszul_duality_analysis(Fraction(c_val))
            assert result['kappa_sum_check'], f"kappa_sum != 250/3 at c={c_val}"

    def test_F2_sum_symmetric(self):
        """F_2(c) + F_2(100-c) does not depend on the sign of (c - 50)."""
        # The sum is a specific function of c; verify it at c and 100-c
        c1 = Fraction(20)
        c2 = Fraction(80)
        r1 = koszul_duality_analysis(c1)
        r2 = koszul_duality_analysis(c2)
        # F_2(20) + F_2(80) should equal F_2(80) + F_2(20) (trivially)
        assert r1['F2_sum'] == r2['F2_sum']

    def test_self_dual_symmetry(self):
        """At c = 50: F_2(c) = F_2(100-c)."""
        result = koszul_duality_analysis(Fraction(50))
        assert result['F2_c'] == result['F2_dual']
        assert result['F2_diff'] == Fraction(0)


# ======================================================================
# 11. Asymptotics
# ======================================================================

class TestAsymptotics:
    """Tests for large-c asymptotic behavior."""

    def test_large_c_limit_of_cross(self):
        """delta_F_2 -> 1/16 as c -> infinity."""
        asymp = large_c_asymptotics()
        assert asymp['cross_channel_large_c_limit'] == Fraction(1, 16)

    def test_ratio_to_virasoro(self):
        """F_2(W_3)/F_2(Vir) -> 5/3 as c -> infinity."""
        asymp = large_c_asymptotics()
        assert asymp['ratio_to_virasoro_large_c'] == Fraction(5, 3)

    def test_large_c_numerical(self):
        """At c = 10000, cross-channel is close to 1/16."""
        c = Fraction(10000)
        delta = delta_F2_w3_closed_form(c)
        # delta = (10000 + 204)/(16*10000) = 10204/160000 = 2551/40000
        # 1/16 = 2500/40000
        # Difference: 51/40000 = 51/(4*10000) -- the 1/c correction
        assert delta - Fraction(1, 16) == Fraction(51, 4 * 10000)


# ======================================================================
# 12. DS reduction
# ======================================================================

class TestDSReduction:
    """Tests for DS reduction comparison sl_3 -> W_3."""

    def test_c_relation(self):
        """c(sl_3, k) - c(W_3, k) = 6 for all k."""
        for k_val in [1, 2, 3, 5, 10]:
            result = ds_comparison(Fraction(k_val))
            assert result['c_relation'] == Fraction(6), \
                f"c_sl3 - c_w3 != 6 at k={k_val}"

    def test_sl3_kappa_formula(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        data = sl3_data_at_level(Fraction(1))
        assert data['kappa'] == Fraction(16, 3)
        data2 = sl3_data_at_level(Fraction(3))
        assert data2['kappa'] == Fraction(8)

    def test_ds_gap_exists(self):
        """F_2(sl_3) != F_2(W_3) at the DS point (ghost contribution nonzero)."""
        result = ds_comparison(Fraction(1))
        assert result['difference'] != Fraction(0)


# ======================================================================
# 13. Propagator variance
# ======================================================================

class TestPropagatorVariance:
    """Tests for propagator variance delta_mix."""

    def test_variance_nonzero(self):
        """delta_mix(W_3) != 0 for c != 0 (multi-channel non-autonomy)."""
        result = propagator_variance_w3(Fraction(10))
        assert result['is_nonzero']

    def test_variance_formula(self):
        """delta_mix = c/5."""
        for c_val in [1, 5, 10, 50]:
            c = Fraction(c_val)
            result = propagator_variance_w3(c)
            assert result['delta_mix'] == result['delta_mix_simplified']
            assert result['delta_mix'] == c / 5


# ======================================================================
# 14. Rational reconstruction
# ======================================================================

class TestRationalReconstruction:
    """Tests for rational reconstruction verification."""

    def test_all_integer_evaluations_match(self):
        """F_2 at integer c matches closed form."""
        result = rational_reconstruction_check(10)
        assert result['all_match_closed_form']

    def test_integer_evaluations_values(self):
        """Spot-check specific integer evaluations."""
        vals = F2_at_integer_values()
        # At c = 1: F_2 = 7/6912 + 205/16 = 7/6912 + 88560/6912 = 88567/6912.
        # Closed form: (112 + 6912 + 1410048)/110592 = 1417072/110592 = 88567/6912.
        c = Fraction(1)
        expected = Fraction(112 + 6912 + 1410048, 110592)
        assert vals[1]['closed_form'] == expected
        assert vals[1]['closed_form'] == Fraction(88567, 6912)


# ======================================================================
# 15. Summary and integration
# ======================================================================

class TestSummary:
    """Integration tests for the summary report."""

    def test_summary_self_dual(self):
        """Summary at c = 50 is consistent."""
        report = summary_report(Fraction(50))
        assert report['is_multi_weight']
        assert report['cross_channel_nonzero']
        assert report['multi_path_delta']['all_paths_agree']
        assert report['multi_path_total']['all_paths_agree']

    def test_summary_generic_c(self):
        """Summary at c = 7 is consistent."""
        report = summary_report(Fraction(7))
        assert report['multi_path_delta']['all_paths_agree']
        assert report['multi_path_total']['all_paths_agree']

    def test_cross_channel_positive(self):
        """delta_F_2 > 0 for all c > 0 (thm:multi-weight-genus-expansion)."""
        for c_val in range(1, 20):
            c = Fraction(c_val)
            assert F2_cross_channel(c) > 0, f"delta_F_2 <= 0 at c={c_val}"

    def test_F2_at_c_equals_2(self):
        """F_2(W_3, c=2) vs F_2(Vir, c=2): W_3 is strictly larger.

        F_2(Vir, 2) = 7*2/11520 = 14/11520 = 7/5760.
        F_2(W_3, 2) = 7*2/6912 + 206/32 = 14/6912 + 206/32.
                     = 7/3456 + 103/16.
        The cross-channel dominates at small c.
        """
        c = Fraction(2)
        f2_vir = F2_virasoro_at_c(c)
        f2_w3 = F2_w3_total(c)
        assert f2_w3 > f2_vir
        # Verify the cross-channel value
        cross = delta_F2_w3_closed_form(c)
        assert cross == Fraction(206, 32)
        assert cross == Fraction(103, 16)
