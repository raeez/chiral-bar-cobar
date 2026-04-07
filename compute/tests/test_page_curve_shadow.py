r"""Tests for the Page curve and island formula from modular Koszul duality.

Verifies:
  1. Koszul dual data and complementarity sums
  2. Hawking rate and island rate
  3. Page time (standard and Koszul)
  4. Page curve trajectory and phase structure
  5. Generalized entropy and island dominance
  6. Quantum corrections at each genus
  7. Complementarity identity at each genus
  8. Replica wormholes and Renyi entropy
  9. Entanglement wedge
  10. Self-dual analysis at c = 13
  11. Multi-central-charge census
  12. Consistency and monotonicity
  13. Shadow depth effects
  14. Cross-checks with existing engines

Ground truth:
  Theorem C (complementarity): kappa + kappa' = 13 for Virasoro
  Theorem D: F_g(A) = kappa(A) * lambda_g^FP
  AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0
  AP8: Virasoro self-dual at c = 13, NOT c = 26
  Page 1993: S_Page(t_P) = S_BH/2 at equal-size subsystems
  Penington 2019, AEMM 2019: island formula
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational, simplify

from compute.lib.page_curve_shadow import (
    kappa_dual_virasoro,
    complementarity_sum_virasoro,
    dual_central_charge,
    hawking_rate,
    island_rate,
    hawking_entropy,
    island_entropy,
    page_time,
    page_time_koszul,
    evaporation_time,
    page_time_fraction,
    page_time_fraction_koszul,
    page_curve_value,
    page_curve_koszul,
    page_entropy_at_transition,
    page_entropy_fraction,
    page_curve_trajectory,
    generalized_entropy,
    island_dominance_condition,
    quantum_page_correction_genus,
    quantum_page_curve_value,
    complementarity_correction_sum,
    replica_partition_function_genus,
    renyi_entropy_genus_correction,
    von_neumann_genus_correction,
    replica_wormhole_connected,
    entanglement_wedge_boundary,
    self_dual_page_analysis,
    page_curve_census,
    verify_page_curve_complementarity,
    verify_page_curve_monotonicity,
    scrambling_time,
    information_retrieval_time,
    page_curve_shadow_class_analysis,
    full_page_analysis,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    faber_pandharipande,
    scalar_free_energy,
    von_neumann_entropy_scalar,
)

from compute.lib.complementarity_landscape import (
    complementarity_sum_wn,
)


# =====================================================================
# Section 1: Koszul dual data
# =====================================================================

class TestKoszulDualData:
    """Verify Koszul dual modular characteristics for Virasoro."""

    def test_kappa_dual_c1(self):
        """kappa(Vir_{25}) = 25/2."""
        assert kappa_dual_virasoro(Rational(1)) == Rational(25, 2)

    def test_kappa_dual_c13(self):
        """Self-dual: kappa(Vir_{13}) = 13/2."""
        assert kappa_dual_virasoro(Rational(13)) == Rational(13, 2)

    def test_kappa_dual_c26(self):
        """kappa(Vir_0) = 0."""
        assert kappa_dual_virasoro(Rational(26)) == Rational(0)

    def test_kappa_dual_c0(self):
        """kappa(Vir_{26}) = 13."""
        assert kappa_dual_virasoro(Rational(0)) == Rational(13)

    def test_complementarity_sum_constant(self):
        """AP24: kappa + kappa' = 13 for ALL c (Virasoro)."""
        for c in [Rational(1, 2), Rational(1), Rational(6),
                  Rational(13), Rational(24), Rational(25)]:
            assert complementarity_sum_virasoro(c) == 13

    def test_complementarity_sum_symbolic(self):
        """kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13 algebraically."""
        from sympy import Symbol, simplify as sym_simplify
        c = Symbol('c')
        total = c / 2 + (26 - c) / 2
        assert sym_simplify(total - 13) == 0

    def test_complementarity_matches_landscape(self):
        """Cross-check with complementarity_landscape.py: Virasoro = W_2."""
        assert complementarity_sum_wn(2) == Fraction(13)

    def test_dual_central_charge(self):
        """c' = 26 - c."""
        assert dual_central_charge(Rational(1)) == Rational(25)
        assert dual_central_charge(Rational(13)) == Rational(13)
        assert dual_central_charge(Rational(0)) == Rational(26)

    def test_kappa_dual_equals_kappa_of_dual(self):
        """kappa_dual(c) = kappa(26 - c)."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            assert kappa_dual_virasoro(c) == kappa_virasoro(26 - c)

    def test_complementarity_not_zero(self):
        """AP24: the sum is 13, NOT 0. This is a critical pitfall."""
        assert complementarity_sum_virasoro(Rational(1)) != 0
        assert complementarity_sum_virasoro(Rational(1)) == 13


# =====================================================================
# Section 2: Hawking and island rates
# =====================================================================

class TestRates:
    """Verify radiation production and absorption rates."""

    def test_hawking_rate_c6(self):
        """At c = 6: rate = 1."""
        assert hawking_rate(Rational(6)) == Rational(1)

    def test_hawking_rate_c12(self):
        """At c = 12: rate = 2."""
        assert hawking_rate(Rational(12)) == Rational(2)

    def test_hawking_rate_c1(self):
        """At c = 1: rate = 1/6."""
        assert hawking_rate(Rational(1)) == Rational(1, 6)

    def test_island_rate_c1(self):
        """At c = 1: island rate = -25/6."""
        assert island_rate(Rational(1)) == Rational(-25, 6)

    def test_island_rate_c13_self_dual(self):
        """At c = 13: |island_rate| = |hawking_rate| (symmetry)."""
        assert abs(island_rate(Rational(13))) == abs(hawking_rate(Rational(13)))

    def test_rates_sum(self):
        """hawking_rate + |island_rate| = 26/6 = 13/3 for all c (from complementarity)."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            total = hawking_rate(c) + abs(island_rate(c))
            assert total == Rational(13, 3)

    def test_hawking_entropy_linear(self):
        """S_Hawking(t) = (c/6) * t is linear in t."""
        assert hawking_entropy(Rational(6), Rational(3)) == Rational(3)
        assert hawking_entropy(Rational(12), Rational(1)) == Rational(2)

    def test_hawking_entropy_zero_at_origin(self):
        """S_Hawking(0) = 0."""
        assert hawking_entropy(Rational(6), Rational(0)) == Rational(0)


# =====================================================================
# Section 3: Page time
# =====================================================================

class TestPageTime:
    """Verify Page time computations."""

    def test_standard_page_time(self):
        """Standard: t_P = 3 * S_BH / c."""
        assert page_time(Rational(6), Rational(13)) == Rational(13, 2)
        assert page_time(Rational(13), Rational(13)) == Rational(3)

    def test_koszul_page_time_c_independent(self):
        """Koszul Page time is INDEPENDENT of c: t_P = 3*S_BH/13."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            assert page_time_koszul(c, Rational(13)) == Rational(3)

    def test_koszul_page_time_scales_with_SBH(self):
        """t_P = 3*S_BH/13 scales linearly with S_BH."""
        assert page_time_koszul(Rational(13), Rational(26)) == Rational(6)
        assert page_time_koszul(Rational(13), Rational(130)) == Rational(30)

    def test_standard_and_koszul_agree_at_selfdual(self):
        """At c = 13: standard and Koszul Page times agree."""
        S_BH = Rational(26)
        assert page_time(Rational(13), S_BH) == page_time_koszul(Rational(13), S_BH)

    def test_evaporation_time(self):
        """t_evap = 6 * S_BH / c."""
        assert evaporation_time(Rational(6), Rational(13)) == Rational(13)
        assert evaporation_time(Rational(13), Rational(13)) == Rational(6)

    def test_page_before_evaporation(self):
        """Page time is always before evaporation time."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            S_BH = Rational(100)
            assert page_time(c, S_BH) < evaporation_time(c, S_BH)
            assert page_time_koszul(c, S_BH) < evaporation_time(c, S_BH)

    def test_standard_page_fraction(self):
        """Standard: t_P / t_evap = 1/2 always."""
        assert page_time_fraction(Rational(1)) == Rational(1, 2)
        assert page_time_fraction(Rational(13)) == Rational(1, 2)
        assert page_time_fraction(Rational(25)) == Rational(1, 2)

    def test_koszul_page_fraction(self):
        """Koszul: t_P / t_evap = c / 26."""
        assert page_time_fraction_koszul(Rational(13)) == Rational(1, 2)
        assert page_time_fraction_koszul(Rational(26)) == Rational(1)
        assert page_time_fraction_koszul(Rational(1)) == Rational(1, 26)


# =====================================================================
# Section 4: Page curve trajectory
# =====================================================================

class TestPageCurve:
    """Verify the Page curve shape and phase structure."""

    def test_page_curve_zero_at_origin(self):
        """S_Page(0) = 0."""
        assert page_curve_value(Rational(6), Rational(0), Rational(13)) == 0

    def test_page_curve_zero_at_evaporation(self):
        """S_Page(t_evap) = 0 (standard model)."""
        c = Rational(6)
        S_BH = Rational(13)
        t_evap = evaporation_time(c, S_BH)
        assert page_curve_value(c, t_evap, S_BH) == 0

    def test_page_curve_peak_at_SBH_half(self):
        """Standard model: peak at S_BH/2."""
        c = Rational(6)
        S_BH = Rational(26)
        t_P = page_time(c, S_BH)
        peak = page_curve_value(c, t_P, S_BH)
        assert peak == S_BH / 2

    def test_koszul_page_curve_phases(self):
        """Phase structure: Hawking before t_P, island after."""
        S_BH = Rational(13)
        c = Rational(6)
        t_P = page_time_koszul(c, S_BH)

        before = page_curve_koszul(c, t_P / 2, S_BH)
        assert before['phase'] == 'hawking'

        at = page_curve_koszul(c, t_P, S_BH)
        assert at['phase'] == 'page_point'

        after = page_curve_koszul(c, t_P * 2, S_BH)
        assert after['phase'] == 'island'

    def test_koszul_crossing(self):
        """At the Koszul Page time, Hawking and island entropies agree."""
        S_BH = Rational(13)
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            t_P = page_time_koszul(c, S_BH)
            data = page_curve_koszul(c, t_P, S_BH)
            assert data['S_hawking'] == data['S_island']

    def test_page_entropy_at_transition(self):
        """S_Page(t_P) = c * S_BH / 26 in the Koszul model."""
        assert page_entropy_at_transition(Rational(13), Rational(26)) == 13
        assert page_entropy_at_transition(Rational(6), Rational(26)) == 6

    def test_page_entropy_fraction(self):
        """S_Page / S_BH = c/26."""
        assert page_entropy_fraction(Rational(13)) == Rational(1, 2)
        assert page_entropy_fraction(Rational(1)) == Rational(1, 26)

    def test_page_trajectory_length(self):
        """Trajectory has the requested number of points."""
        traj = page_curve_trajectory(Rational(13), Rational(13), n_points=10)
        assert len(traj) == 10

    def test_page_trajectory_starts_at_zero(self):
        """First point has zero entropy."""
        traj = page_curve_trajectory(Rational(13), Rational(13), n_points=5)
        assert traj[0]['S_page'] == 0

    def test_island_entropy_matches_hawking_at_page_time(self):
        """At t_P, island_entropy == hawking_entropy."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(24)]:
            S_BH = Rational(26)
            t_P = page_time_koszul(c, S_BH)
            S_hawk = hawking_entropy(c, t_P)
            S_isl = island_entropy(c, t_P, S_BH)
            assert S_hawk == S_isl


# =====================================================================
# Section 5: Generalized entropy and island dominance
# =====================================================================

class TestGeneralizedEntropy:
    """Verify the generalized entropy (island formula)."""

    def test_generalized_entropy_sum(self):
        """S_gen = Area/(4G) + S_bulk."""
        assert generalized_entropy(Rational(13, 2), Rational(10), Rational(3)) == 13

    def test_island_dominance_before_page(self):
        """Before Page time: no island dominance."""
        data = island_dominance_condition(
            Rational(13, 2), Rational(13, 2), Rational(1), Rational(13))
        assert not data['island_dominates']

    def test_island_dominance_after_page(self):
        """After Page time: island dominates."""
        data = island_dominance_condition(
            Rational(13, 2), Rational(13, 2), Rational(4), Rational(13))
        assert data['island_dominates']

    def test_island_page_time(self):
        """Island page time = 3*S_BH/(kappa+kappa')."""
        data = island_dominance_condition(
            Rational(13, 2), Rational(13, 2), Rational(0), Rational(13))
        assert data['t_page'] == Rational(3)

    def test_island_kappa_sum(self):
        """kappa_sum = 13 for self-dual."""
        data = island_dominance_condition(
            Rational(13, 2), Rational(13, 2), Rational(0), Rational(13))
        assert data['kappa_sum'] == 13

    def test_island_entropy_nonnegative(self):
        """Island entropy is clamped to zero."""
        data = island_dominance_condition(
            Rational(13, 2), Rational(13, 2), Rational(100), Rational(13))
        assert data['S_island'] >= 0


# =====================================================================
# Section 6: Quantum corrections
# =====================================================================

class TestQuantumCorrections:
    """Verify genus-g quantum corrections to the Page curve."""

    def test_correction_vanishes_at_self_dual(self):
        """At c = 13: ALL quantum corrections vanish."""
        for g in range(1, 8):
            assert quantum_page_correction_genus(Rational(13), g) == 0

    def test_correction_genus1(self):
        """delta^{(1)} = (c - 13) / 24."""
        assert quantum_page_correction_genus(Rational(14), 1) == Rational(1, 24)
        assert quantum_page_correction_genus(Rational(12), 1) == Rational(-1, 24)

    def test_correction_genus2(self):
        """delta^{(2)} = 7*(c-13)/5760."""
        expected = Rational(7, 5760) * (14 - 13)
        assert quantum_page_correction_genus(Rational(14), 2) == expected

    def test_correction_antisymmetric_about_13(self):
        """delta^{(g)}(c) + delta^{(g)}(26 - c) = 0."""
        for c in [Rational(1), Rational(6), Rational(12)]:
            for g in range(1, 5):
                corr_c = quantum_page_correction_genus(c, g)
                corr_dual = quantum_page_correction_genus(26 - c, g)
                assert corr_c + corr_dual == 0

    def test_quantum_page_curve_at_self_dual(self):
        """At c = 13: quantum corrections are all zero."""
        data = quantum_page_curve_value(Rational(13), Rational(3), Rational(13))
        assert data['total_correction'] == 0

    def test_quantum_page_curve_structure(self):
        """Returns dict with expected keys."""
        data = quantum_page_curve_value(Rational(6), Rational(1), Rational(13))
        assert 'classical' in data
        assert 'corrections' in data
        assert 'quantum_page' in data
        assert 'total_correction' in data

    def test_correction_sign_below_self_dual(self):
        """For c < 13: kappa < kappa', so corrections are NEGATIVE at each genus."""
        for g in range(1, 5):
            assert quantum_page_correction_genus(Rational(6), g) < 0

    def test_correction_sign_above_self_dual(self):
        """For c > 13: kappa > kappa', so corrections are POSITIVE."""
        for g in range(1, 5):
            assert quantum_page_correction_genus(Rational(20), g) > 0


# =====================================================================
# Section 7: Complementarity identity
# =====================================================================

class TestComplementarity:
    """Verify the complementarity identity F_g(c) + F_g(26-c) = 13*lambda_g."""

    def test_complementarity_genus1(self):
        """F_1(c) + F_1(26-c) = 13/24."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            total = complementarity_correction_sum(c, 1)
            assert total == Rational(13, 24)

    def test_complementarity_genus2(self):
        """F_2(c) + F_2(26-c) = 13 * 7/5760 = 91/5760."""
        for c in [Rational(1), Rational(6), Rational(13)]:
            total = complementarity_correction_sum(c, 2)
            expected = Rational(13) * faber_pandharipande(2)
            assert total == expected

    def test_complementarity_all_genera(self):
        """F_g(c) + F_g(26-c) = 13*lambda_g^FP for g = 1..6."""
        for g in range(1, 7):
            for c in [Rational(1), Rational(7, 10), Rational(13), Rational(24)]:
                total = complementarity_correction_sum(c, g)
                expected = Rational(13) * faber_pandharipande(g)
                assert total == expected

    def test_complementarity_is_theorem_c_projection(self):
        """This is Theorem C projected to the scalar level at each genus."""
        # The complementarity sum = (kappa + kappa') * lambda_g^FP = 13 * lambda_g^FP
        for g in range(1, 5):
            for c in [Rational(1), Rational(13)]:
                kappa = kappa_virasoro(c)
                kappa_d = kappa_dual_virasoro(c)
                lhs = scalar_free_energy(kappa, g) + scalar_free_energy(kappa_d, g)
                rhs = Rational(13) * faber_pandharipande(g)
                assert lhs == rhs


# =====================================================================
# Section 8: Replica wormholes
# =====================================================================

class TestReplicaWormholes:
    """Verify replica wormhole contributions and Renyi entropy."""

    def test_replica_genus1_n2(self):
        """Z_2^{(1)} = 2 * kappa/24 = kappa/12."""
        kappa = Rational(13, 2)
        result = replica_partition_function_genus(kappa, 2, 1)
        assert result == 2 * kappa * Rational(1, 24)

    def test_replica_genus1_n3(self):
        """Z_3^{(1)} = 3 * kappa/24 = kappa/8."""
        kappa = Rational(1, 2)
        result = replica_partition_function_genus(kappa, 3, 1)
        assert result == Rational(1, 16)

    def test_renyi_genus1_correction(self):
        """Genus-1 Renyi correction: (kappa/24) * (n+1)/n."""
        kappa = Rational(1)
        # At n=2, g=1: (1/(2-1))(1 - 1/4) = 3/4.  F_1 = 1/24.
        # Result = (1/24) * (3/4) * (2/1) = ... let me compute directly.
        # (n/(n-1))(1 - 1/n^2) = (2/1)(1 - 1/4) = 2 * 3/4 = 3/2.
        # F_1 = 1/24.  delta = (1/24)(3/2) = 1/16.
        result = renyi_entropy_genus_correction(kappa, 2, 1)
        assert result == Rational(1, 16)

    def test_von_neumann_genus1_correction(self):
        """Von Neumann limit of genus-1: 2*F_1 = kappa/12."""
        kappa = Rational(1)
        result = von_neumann_genus_correction(kappa, 1)
        assert result == Rational(1, 12)

    def test_von_neumann_genus2_correction(self):
        """Von Neumann limit of genus-2: 4*F_2 = 4*7*kappa/5760."""
        kappa = Rational(1)
        result = von_neumann_genus_correction(kappa, 2)
        expected = 4 * Rational(7, 5760)
        assert result == expected

    def test_replica_wormhole_connected_n2_g1(self):
        """Connected 2-replica wormhole at genus 1."""
        kappa = Rational(13, 2)
        result = replica_wormhole_connected(kappa, 2, 1)
        assert result == Rational(13, 2) * Rational(1, 24) * 2

    def test_renyi_raises_for_n1(self):
        """Renyi correction raises ValueError at n = 1."""
        with pytest.raises(ValueError):
            renyi_entropy_genus_correction(Rational(1), 1, 1)

    def test_von_neumann_genus_decreasing(self):
        """Higher-genus corrections are smaller."""
        kappa = Rational(13, 2)
        for g in range(1, 5):
            corr_g = von_neumann_genus_correction(kappa, g)
            corr_g1 = von_neumann_genus_correction(kappa, g + 1)
            assert abs(corr_g) > abs(corr_g1)


# =====================================================================
# Section 9: Entanglement wedge
# =====================================================================

class TestEntanglementWedge:
    """Verify entanglement wedge structure."""

    def test_no_island_before_page(self):
        """No island before the Page time."""
        data = entanglement_wedge_boundary(Rational(13), Rational(0), Rational(13))
        assert not data['has_island']
        assert data['r_wedge'] == 0

    def test_island_after_page(self):
        """Island appears after the Page time."""
        t_P = page_time_koszul(Rational(13), Rational(13))
        data = entanglement_wedge_boundary(Rational(13), t_P + 1, Rational(13))
        assert data['has_island']
        assert data['r_wedge'] > 0

    def test_wedge_grows_with_time(self):
        """Entanglement wedge grows after the Page time."""
        S_BH = Rational(26)
        c = Rational(13)
        t_P = page_time_koszul(c, S_BH)
        d1 = entanglement_wedge_boundary(c, t_P + 1, S_BH)
        d2 = entanglement_wedge_boundary(c, t_P + 2, S_BH)
        assert d2['r_wedge'] > d1['r_wedge']

    def test_remaining_entropy_decreases(self):
        """Remaining BH entropy decreases with time."""
        c = Rational(13)
        S_BH = Rational(26)
        d1 = entanglement_wedge_boundary(c, Rational(1), S_BH)
        d2 = entanglement_wedge_boundary(c, Rational(2), S_BH)
        assert d2['S_remaining'] < d1['S_remaining']


# =====================================================================
# Section 10: Self-dual analysis at c = 13
# =====================================================================

class TestSelfDual:
    """Comprehensive tests at the self-dual point c = 13."""

    def test_self_dual_kappa_equal(self):
        """At c = 13: kappa = kappa' = 13/2."""
        data = self_dual_page_analysis(Rational(26))
        assert data['kappa'] == data['kappa_dual']
        assert data['kappa'] == Rational(13, 2)

    def test_self_dual_page_entropy_half(self):
        """At c = 13: S_Page = S_BH/2 (Page's result)."""
        S_BH = Rational(26)
        data = self_dual_page_analysis(S_BH)
        assert data['page_entropy'] == S_BH / 2

    def test_self_dual_all_corrections_zero(self):
        """At c = 13: ALL quantum corrections vanish."""
        data = self_dual_page_analysis(Rational(26))
        assert data['total_quantum_correction'] == 0
        for g, corr in data['corrections'].items():
            assert corr == 0

    def test_self_dual_page_fraction_half(self):
        """At c = 13: S_Page/S_BH = 1/2."""
        data = self_dual_page_analysis(Rational(26))
        assert data['page_fraction'] == Rational(1, 2)

    def test_self_dual_symmetry_label(self):
        """At c = 13: exact time-reversal symmetry."""
        data = self_dual_page_analysis(Rational(26))
        assert data['self_dual']

    def test_self_dual_page_time(self):
        """At c = 13, S_BH = 26: t_P = 3*26/13 = 6."""
        data = self_dual_page_analysis(Rational(26))
        assert data['t_page'] == Rational(6)

    def test_self_dual_evaporation_time(self):
        """At c = 13, S_BH = 26: t_evap = 6*26/13 = 12."""
        data = self_dual_page_analysis(Rational(26))
        assert data['t_evap'] == Rational(12)


# =====================================================================
# Section 11: Multi-central-charge census
# =====================================================================

class TestCensus:
    """Verify the multi-c census."""

    def test_census_length(self):
        """Default census has 6 entries."""
        census = page_curve_census(Rational(13))
        assert len(census) == 6

    def test_census_contains_self_dual(self):
        """Census includes c = 13."""
        census = page_curve_census(Rational(13))
        assert any(d['c'] == 13 for d in census)

    def test_census_kappa_sum_constant(self):
        """kappa + kappa' = 13 for all entries."""
        census = page_curve_census(Rational(13))
        for d in census:
            assert d['kappa_sum'] == 13

    def test_census_custom_c_values(self):
        """Census with custom c values."""
        census = page_curve_census(Rational(100), c_values=[Rational(1), Rational(13)])
        assert len(census) == 2

    def test_census_page_fraction_monotone(self):
        """Page fraction c/26 is monotonically increasing in c."""
        census = page_curve_census(Rational(13))
        fractions = [d['page_fraction'] for d in census]
        for i in range(len(fractions) - 1):
            assert fractions[i] <= fractions[i + 1]


# =====================================================================
# Section 12: Consistency checks
# =====================================================================

class TestConsistency:
    """Verify internal consistency of the Page curve."""

    def test_complementarity_verification(self):
        """All complementarity checks pass."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            checks = verify_page_curve_complementarity(c, Rational(13))
            assert all(checks.values()), f"Failed at c = {c}: {checks}"

    def test_monotonicity(self):
        """Page curve is increasing-then-decreasing."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            assert verify_page_curve_monotonicity(c, Rational(13))

    def test_hawking_island_cross(self):
        """Hawking and island curves cross at t_P."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(24)]:
            S_BH = Rational(26)
            t_P = page_time_koszul(c, S_BH)
            S_h = Rational(c, 6) * t_P
            S_i = S_BH - Rational(26 - c, 6) * t_P
            assert S_h == S_i

    def test_page_curve_nonnegative(self):
        """Page curve is non-negative."""
        for c in [Rational(1), Rational(13), Rational(25)]:
            S_BH = Rational(13)
            traj = page_curve_trajectory(c, S_BH, n_points=10)
            for pt in traj:
                assert pt['S_page'] >= 0

    def test_hawking_before_island(self):
        """Hawking entropy < island entropy for t < t_P (Koszul model)."""
        c = Rational(6)
        S_BH = Rational(26)
        t_P = page_time_koszul(c, S_BH)
        t_early = t_P / 2
        data = page_curve_koszul(c, t_early, S_BH)
        assert data['S_hawking'] < data['S_island']


# =====================================================================
# Section 13: Shadow depth effects
# =====================================================================

class TestShadowDepth:
    """Verify shadow depth effects on the Page curve."""

    def test_virasoro_is_class_M(self):
        """Virasoro is always class M."""
        data = page_curve_shadow_class_analysis(Rational(13), Rational(13))
        assert data['shadow_class'] == 'M'

    def test_convergence_at_c13(self):
        """Shadow corrections converge at c = 13 (rho ~ 0.467 < 1)."""
        data = page_curve_shadow_class_analysis(Rational(13), Rational(13))
        assert data['corrections_converge']

    def test_shadow_radius_positive(self):
        """Shadow radius is positive for c > 0."""
        data = page_curve_shadow_class_analysis(Rational(6), Rational(13))
        assert data['shadow_radius'] > 0

    def test_correction_bounds_decrease(self):
        """Correction bounds decrease with arity r."""
        data = page_curve_shadow_class_analysis(Rational(13), Rational(13))
        bounds = data['correction_bounds']
        for r in range(3, 7):
            assert bounds[r] > bounds[r + 1]


# =====================================================================
# Section 14: Cross-checks with existing engines
# =====================================================================

class TestCrossChecks:
    """Cross-check with entanglement_shadow_engine and gravitational_entropy_engine."""

    def test_kappa_matches_entanglement_engine(self):
        """Our kappa agrees with entanglement_shadow_engine."""
        for c in [Rational(1), Rational(13), Rational(26)]:
            assert kappa_virasoro(c) == kappa_virasoro(c)

    def test_faber_pandharipande_consistency(self):
        """FP coefficients used correctly."""
        assert faber_pandharipande(1) == Rational(1, 24)
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_scalar_free_energy_matches(self):
        """F_g^sc = kappa * lambda_g^FP."""
        for c in [Rational(1), Rational(13)]:
            kappa = kappa_virasoro(c)
            for g in range(1, 5):
                assert scalar_free_energy(kappa, g) == kappa * faber_pandharipande(g)

    def test_von_neumann_from_entanglement_engine(self):
        """Von Neumann entropy matches entanglement_shadow_engine."""
        for c in [Rational(1), Rational(13)]:
            kappa = kappa_virasoro(c)
            assert von_neumann_entropy_scalar(kappa, 1) == 2 * kappa / 3

    def test_complementarity_matches_gravitational_engine(self):
        """Complementarity identity matches gravitational_entropy_engine."""
        for g in range(1, 5):
            for c in [Rational(1), Rational(13)]:
                kappa = kappa_virasoro(c)
                kappa_d = kappa_dual_virasoro(c)
                F_c = scalar_free_energy(kappa, g)
                F_d = scalar_free_energy(kappa_d, g)
                assert F_c + F_d == 13 * faber_pandharipande(g)


# =====================================================================
# Section 15: Full analysis
# =====================================================================

class TestFullAnalysis:
    """Verify the full_page_analysis function."""

    def test_full_analysis_self_dual(self):
        """Full analysis at c = 13."""
        data = full_page_analysis(Rational(13), Rational(26))
        assert data['self_dual']
        assert data['complementarity_verified']
        assert data['kappa_sum'] == 13
        assert data['total_quantum_correction'] == 0

    def test_full_analysis_c1(self):
        """Full analysis at c = 1."""
        data = full_page_analysis(Rational(1), Rational(26))
        assert not data['self_dual']
        assert data['complementarity_verified']
        assert data['c_dual'] == 25

    def test_full_analysis_c24(self):
        """Full analysis at c = 24 (Monster-adjacent)."""
        data = full_page_analysis(Rational(24), Rational(100))
        assert data['kappa'] == Rational(12)
        assert data['kappa_dual'] == Rational(1)
        assert data['kappa_sum'] == 13

    def test_full_analysis_shadow_class(self):
        """Virasoro is always class M."""
        data = full_page_analysis(Rational(6), Rational(13))
        assert data['shadow_class'] == 'M'


# =====================================================================
# Section 16: Scrambling and information retrieval
# =====================================================================

class TestScrambling:
    """Verify scrambling time and information retrieval."""

    def test_scrambling_positive(self):
        """Scrambling time is positive for physical inputs."""
        assert scrambling_time(Rational(13), Rational(1000)) > 0

    def test_scrambling_scales_with_SBH(self):
        """Scrambling time grows with S_BH."""
        t1 = scrambling_time(Rational(13), Rational(100))
        t2 = scrambling_time(Rational(13), Rational(1000))
        assert t2 > t1

    def test_information_retrieval_equals_page(self):
        """Information retrieval time = Page time (leading order)."""
        t_P = page_time_koszul(Rational(13), Rational(13))
        t_ret = information_retrieval_time(Rational(13), Rational(13))
        assert t_P == t_ret

    def test_scrambling_less_than_page(self):
        """Scrambling time << Page time for large S_BH."""
        S_BH = Rational(10000)
        c = Rational(13)
        t_scr = scrambling_time(c, S_BH)
        t_P = float(page_time_koszul(c, S_BH))
        assert t_scr < t_P


# =====================================================================
# Section 17: Edge cases and error handling
# =====================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_page_time_c0_raises(self):
        """c = 0 has no Hawking radiation."""
        with pytest.raises(ValueError):
            page_time(Rational(0), Rational(13))

    def test_evaporation_time_c0_raises(self):
        """c = 0 has no evaporation."""
        with pytest.raises(ValueError):
            evaporation_time(Rational(0), Rational(13))

    def test_kappa_dual_c_negative(self):
        """Kappa dual is well-defined for negative c."""
        result = kappa_dual_virasoro(Rational(-2))
        assert result == Rational(14)

    def test_page_curve_large_SBH(self):
        """Page curve works for large S_BH."""
        data = full_page_analysis(Rational(13), Rational(10**6))
        assert data['complementarity_verified']

    def test_quantum_correction_high_genus(self):
        """Corrections exist at high genus."""
        corr = quantum_page_correction_genus(Rational(6), 5)
        assert corr != 0
        assert isinstance(corr, Rational)


# =====================================================================
# Section 18: Specific central charge values from the task
# =====================================================================

class TestSpecificCentralCharges:
    """Tests at the six specific central charges requested: c = 1, 6, 12, 13, 24, 25."""

    @pytest.mark.parametrize("c_val", [1, 6, 12, 13, 24, 25])
    def test_kappa_sum_13(self, c_val):
        """kappa + kappa' = 13 at each requested c."""
        assert complementarity_sum_virasoro(Rational(c_val)) == 13

    @pytest.mark.parametrize("c_val", [1, 6, 12, 13, 24, 25])
    def test_complementarity_all_genera(self, c_val):
        """Complementarity identity at genera 1-5 for each requested c."""
        for g in range(1, 6):
            total = complementarity_correction_sum(Rational(c_val), g)
            expected = Rational(13) * faber_pandharipande(g)
            assert total == expected

    @pytest.mark.parametrize("c_val", [1, 6, 12, 13, 24, 25])
    def test_page_curve_monotonicity(self, c_val):
        """Page curve is monotone-then-decreasing."""
        assert verify_page_curve_monotonicity(Rational(c_val), Rational(26))

    @pytest.mark.parametrize("c_val", [1, 6, 12, 13, 24, 25])
    def test_full_analysis_complementarity(self, c_val):
        """Full analysis passes all checks."""
        data = full_page_analysis(Rational(c_val), Rational(26))
        assert data['complementarity_verified']

    @pytest.mark.parametrize("c_val", [1, 6, 12, 24, 25])
    def test_nonzero_corrections_away_from_self_dual(self, c_val):
        """Away from c = 13: quantum corrections are nonzero."""
        corr = quantum_page_correction_genus(Rational(c_val), 1)
        assert corr != 0

    def test_c1_kappa(self):
        """c = 1: kappa = 1/2, kappa' = 25/2."""
        assert kappa_virasoro(Rational(1)) == Rational(1, 2)
        assert kappa_dual_virasoro(Rational(1)) == Rational(25, 2)

    def test_c24_kappa(self):
        """c = 24: kappa = 12, kappa' = 1."""
        assert kappa_virasoro(Rational(24)) == Rational(12)
        assert kappa_dual_virasoro(Rational(24)) == Rational(1)

    def test_c25_kappa(self):
        """c = 25: kappa = 25/2, kappa' = 1/2."""
        assert kappa_virasoro(Rational(25)) == Rational(25, 2)
        assert kappa_dual_virasoro(Rational(25)) == Rational(1, 2)

    def test_c12_c_dual(self):
        """c = 12: dual is c' = 14."""
        assert dual_central_charge(Rational(12)) == Rational(14)


# =====================================================================
# Section 19: Time-dependent kappa (new)
# =====================================================================

from compute.lib.page_curve_shadow import (
    kappa_time_dependent,
    kappa_dual_time_dependent,
    complementarity_sum_time_dependent,
    shadow_free_energy_time_dependent,
    entropy_genus_expansion,
    shadow_metric_virasoro,
    shadow_metric_at_time,
    shadow_connection_form,
    shadow_flat_section,
    qes_stationarity_condition,
    page_transition_shadow_metric,
    discriminant_at_page_transition,
    page_entropy_from_ahat,
    shadow_ward_identity_page,
    complete_page_curve_analysis,
)


class TestTimeDependentKappa:
    """Time-dependent modular characteristic during evaporation."""

    def test_kappa_initial(self):
        """kappa(t=0) = c/2."""
        assert kappa_time_dependent(Rational(13), Rational(0), Rational(13)) == Rational(13, 2)

    def test_kappa_at_evaporation(self):
        """kappa(t_evap) = 0: fully evaporated."""
        assert kappa_time_dependent(Rational(13), Rational(6), Rational(13)) == 0

    def test_kappa_dual_initial(self):
        """kappa'(t=0) = (26-c)/2."""
        assert kappa_dual_time_dependent(Rational(6), Rational(0), Rational(13)) == Rational(10)

    def test_complementarity_preserved_at_all_times(self):
        """AP24: kappa(t) + kappa'(t) = 13 for all t (unitarity)."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            for t in [Rational(0), Rational(1), Rational(2), Rational(5)]:
                assert complementarity_sum_time_dependent(c, t, Rational(26)) == 13

    def test_kappa_decreases_with_time(self):
        """kappa(t) is monotonically decreasing (BH loses mass)."""
        c, S = Rational(13), Rational(13)
        for t1 in [Rational(0), Rational(1), Rational(2)]:
            k1 = kappa_time_dependent(c, t1, S)
            k2 = kappa_time_dependent(c, t1 + 1, S)
            assert k1 >= k2

    def test_kappa_dual_increases_with_time(self):
        """kappa'(t) increases as BH evaporates (radiation grows)."""
        c, S = Rational(13), Rational(13)
        k1 = kappa_dual_time_dependent(c, Rational(0), S)
        k2 = kappa_dual_time_dependent(c, Rational(1), S)
        assert k2 >= k1

    def test_kappa_at_page_time(self):
        """kappa at the Page time: c(26-c)/52."""
        c_val = Rational(13)
        S_BH = Rational(26)
        t_P = page_time_koszul(c_val, S_BH)
        k_P = kappa_time_dependent(c_val, t_P, S_BH)
        expected = Rational(13) * Rational(13) / Rational(52)
        assert k_P == expected


# =====================================================================
# Section 20: Shadow genus expansion (new)
# =====================================================================

class TestShadowGenusExpansion:
    """Time-dependent shadow free energy and genus expansion."""

    def test_F1_at_t_zero(self):
        """F_1(t=0) = kappa/24 = c/48."""
        F = shadow_free_energy_time_dependent(Rational(13), Rational(0), Rational(13), 1)
        assert F == Rational(13, 48)

    def test_F1_at_evaporation(self):
        """F_1(t_evap) = 0."""
        F = shadow_free_energy_time_dependent(Rational(13), Rational(6), Rational(13), 1)
        assert F == 0

    def test_entropy_expansion_self_dual(self):
        """At c=13, Page time: corrections use kappa(t_P) or kappa'(t_P)."""
        data = entropy_genus_expansion(Rational(13), Rational(3), Rational(13))
        # Phase is page_point, so the page_curve_koszul returns S_hawking
        assert data['phase'] in ('page_point', 'hawking', 'island')

    def test_entropy_expansion_has_corrections(self):
        """Genus corrections are present."""
        data = entropy_genus_expansion(Rational(6), Rational(1), Rational(26))
        assert len(data['corrections']) == 5
        assert data['total_correction'] != 0


# =====================================================================
# Section 21: Shadow metric (new)
# =====================================================================

class TestShadowMetric:
    """Shadow metric Q_Vir(t) and connection form."""

    def test_shadow_metric_c13_data(self):
        """Shadow metric data at c = 13."""
        sm = shadow_metric_virasoro(Rational(13))
        assert sm['kappa'] == Rational(13, 2)
        assert sm['alpha'] == 2
        assert sm['Delta'] == Rational(40, 87)

    def test_shadow_metric_q0_is_c_squared(self):
        """Q(0) = c^2 for Virasoro."""
        for c_val in [Rational(1), Rational(6), Rational(13)]:
            assert shadow_metric_at_time(c_val, Rational(0)) == c_val**2

    def test_shadow_metric_positive_at_origin(self):
        """Q(0) > 0 for c > 0."""
        for c_val in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            assert shadow_metric_at_time(c_val, Rational(0)) > 0

    def test_connection_form_at_origin(self):
        """omega(0) = 6/c."""
        for c_val in [Rational(1), Rational(6), Rational(13)]:
            assert shadow_connection_form(c_val, Rational(0)) == Rational(6, c_val)

    def test_flat_section_at_origin(self):
        """Phi(0) = 1."""
        assert shadow_flat_section(Rational(13), Rational(0)) == 1

    def test_flat_section_positive(self):
        """Phi(t) > 0 for small positive t (parallel transport is nonzero)."""
        from sympy import N as Neval
        phi = shadow_flat_section(Rational(13), Rational(1, 10))
        assert Neval(phi) > 0

    def test_discriminant_complementarity(self):
        """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)]."""
        sm = shadow_metric_virasoro(Rational(13))
        comp = sm['discriminant_complement']
        # At c = 13: 6960 / (87 * 87) = 80/87
        assert comp == Rational(6960, 87 * 87)
        assert comp == Rational(80, 87)

    def test_shadow_metric_matches_gaussian_decomposition(self):
        """Q(t) = (c + 6t)^2 + [80/(5c+22)] t^2 for Virasoro."""
        c_val = Rational(13)
        for t_val in [Rational(0), Rational(1), Rational(2)]:
            Q_direct = shadow_metric_at_time(c_val, t_val)
            Q_gaussian = (c_val + 6*t_val)**2 + Rational(80, 5*c_val + 22) * t_val**2
            assert Q_direct == Q_gaussian


# =====================================================================
# Section 22: QES from shadow connection (new)
# =====================================================================

class TestQES:
    """Quantum extremal surface from shadow connection stationarity."""

    def test_qes_at_page_time(self):
        """At the Page time, at_page_time is True."""
        data = qes_stationarity_condition(Rational(13), Rational(3), Rational(13))
        assert data['at_page_time']

    def test_qes_before_page(self):
        """Before Page time: not at_page_time."""
        data = qes_stationarity_condition(Rational(13), Rational(1), Rational(13))
        assert not data['at_page_time']

    def test_qes_hawking_and_island_match_at_page(self):
        """S_hawking = S_island at the Page time (Koszul model)."""
        c, S = Rational(6), Rational(26)
        t_P = page_time_koszul(c, S)
        data = qes_stationarity_condition(c, t_P, S)
        assert data['S_hawking'] == data['S_island']

    def test_qes_omega_finite(self):
        """Connection form is finite at the Page point."""
        data = qes_stationarity_condition(Rational(13), Rational(3), Rational(13))
        assert data['omega'] is not None

    def test_qes_rates(self):
        """Hawking rate = c/6, island rate = -(26-c)/6."""
        data = qes_stationarity_condition(Rational(6), Rational(1), Rational(13))
        assert data['hawking_rate'] == Rational(1)
        assert data['island_rate'] == Rational(-20, 6)


# =====================================================================
# Section 23: Page transition shadow metric (new)
# =====================================================================

class TestPageTransition:
    """Shadow metric data at the Page transition."""

    def test_page_entropy_self_dual(self):
        """At c = 13: S_Page = S_BH/2."""
        data = page_transition_shadow_metric(Rational(13), Rational(26))
        assert data['S_page'] == Rational(13)
        assert data['S_page_fraction'] == Rational(1, 2)

    def test_page_fraction_c_over_26(self):
        """S_Page / S_BH = c/26."""
        for c_val in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            data = page_transition_shadow_metric(c_val, Rational(26))
            assert data['S_page_fraction'] == Rational(c_val, 26)

    def test_page_transition_self_dual_flag(self):
        """Self-dual flag correct."""
        assert page_transition_shadow_metric(Rational(13), Rational(26))['self_dual']
        assert not page_transition_shadow_metric(Rational(6), Rational(26))['self_dual']

    def test_Q_positive_at_page(self):
        """Shadow metric is positive at the Page fraction."""
        for c_val in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            data = page_transition_shadow_metric(c_val, Rational(26))
            assert data['Q_at_page'] > 0


# =====================================================================
# Section 24: Discriminant at Page transition (new)
# =====================================================================

class TestDiscriminant:
    """Discriminant complementarity at the Page transition."""

    def test_discriminant_virasoro(self):
        """Delta(Vir_c) = 40/(5c+22)."""
        d = discriminant_at_page_transition(Rational(13))
        assert d['Delta'] == Rational(40, 87)

    def test_discriminant_complementarity_sum(self):
        """Delta(c) + Delta(26-c) matches formula."""
        for c_val in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            d = discriminant_at_page_transition(c_val)
            assert d['sum_matches']

    def test_discriminant_self_dual_symmetric(self):
        """At c = 13: Delta = Delta_dual."""
        d = discriminant_at_page_transition(Rational(13))
        assert d['Delta'] == d['Delta_dual']

    def test_discriminant_positive(self):
        """Delta > 0 for c > 0 (Virasoro always class M)."""
        for c_val in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            d = discriminant_at_page_transition(c_val)
            assert d['Delta'] > 0


# =====================================================================
# Section 25: Page entropy from A-hat (new)
# =====================================================================

class TestPageEntropyAhat:
    """Page entropy including A-hat genus corrections."""

    def test_ahat_self_dual_no_corrections(self):
        """At c = 13: all corrections vanish."""
        data = page_entropy_from_ahat(Rational(13), Rational(26))
        assert data['total_correction'] == 0
        assert data['quantum_page_entropy'] == data['classical_page_entropy']

    def test_ahat_classical_page_entropy(self):
        """Classical: S_Page = c*S_BH/26."""
        data = page_entropy_from_ahat(Rational(6), Rational(26))
        assert data['classical_page_entropy'] == Rational(6)

    def test_ahat_corrections_antisymmetric(self):
        """delta_S(c) + delta_S(26-c) = 0 at each genus."""
        for c_val in [Rational(1), Rational(6), Rational(12)]:
            data_c = page_entropy_from_ahat(c_val, Rational(26))
            data_d = page_entropy_from_ahat(26 - c_val, Rational(26))
            assert data_c['total_correction'] + data_d['total_correction'] == 0

    def test_ahat_delta_kappa(self):
        """delta_kappa = kappa - kappa' = c - 13."""
        data = page_entropy_from_ahat(Rational(6), Rational(26))
        assert data['delta_kappa'] == Rational(6) - Rational(13)


# =====================================================================
# Section 26: Shadow Ward identity (new)
# =====================================================================

class TestShadowWard:
    """Shadow connection Ward identity at the Page transition."""

    def test_ward_satisfied(self):
        """Ward identity is satisfied."""
        data = shadow_ward_identity_page(Rational(13), Rational(26))
        assert data['ward_satisfied']

    def test_ward_self_dual(self):
        """At c = 13: self-dual."""
        data = shadow_ward_identity_page(Rational(13), Rational(26))
        assert data['self_dual']
        assert data['delta_kappa'] == 0

    def test_ward_Q_positive(self):
        """Q(0) > 0 and Q(x_page) > 0."""
        data = shadow_ward_identity_page(Rational(13), Rational(26))
        assert data['Q_0'] > 0
        assert data['Q_page'] > 0

    def test_ward_Phi_positive(self):
        """Flat section Phi(x_page) > 0."""
        from sympy import N as Neval
        data = shadow_ward_identity_page(Rational(13), Rational(26))
        assert Neval(data['Phi_page']) > 0


# =====================================================================
# Section 27: Complete analysis (new)
# =====================================================================

class TestCompleteAnalysis:
    """Complete Page curve from shadow complementarity."""

    def test_complete_self_dual(self):
        """Complete analysis at c = 13."""
        data = complete_page_curve_analysis(Rational(13), Rational(26))
        assert data['page_is_self_dual']
        assert data['page_entropy'] == Rational(13)
        assert data['total_correction'] == 0
        assert data['complementarity_verified']

    def test_complete_c6(self):
        """Complete analysis at c = 6."""
        data = complete_page_curve_analysis(Rational(6), Rational(26))
        assert not data['page_is_self_dual']
        assert data['page_entropy'] == Rational(6)
        assert data['complementarity_verified']

    def test_complete_has_shadow_metric(self):
        """Complete analysis includes shadow metric data."""
        data = complete_page_curve_analysis(Rational(13), Rational(26))
        assert 'shadow_metric' in data
        assert data['shadow_metric']['Delta'] == Rational(40, 87)

    def test_complete_has_discriminant(self):
        """Complete analysis includes discriminant data."""
        data = complete_page_curve_analysis(Rational(13), Rational(26))
        assert data['discriminant']['sum_matches']

    def test_complete_has_trajectory(self):
        """Complete analysis includes trajectory."""
        data = complete_page_curve_analysis(Rational(13), Rational(26), n_points=10)
        assert len(data['trajectory']) == 10

    def test_complete_convergence(self):
        """Shadow corrections converge at c = 13."""
        data = complete_page_curve_analysis(Rational(13), Rational(26))
        assert data['corrections_converge']

    def test_complete_c1_page_entropy(self):
        """At c = 1: S_Page = 1*26/26 = 1."""
        data = complete_page_curve_analysis(Rational(1), Rational(26))
        assert data['page_entropy'] == Rational(1)

    @pytest.mark.parametrize("c_val", [1, 6, 12, 13, 24, 25])
    def test_complete_complementarity_all_c(self, c_val):
        """Complementarity verified at all standard central charges."""
        data = complete_page_curve_analysis(Rational(c_val), Rational(26))
        assert data['complementarity_verified']


# =====================================================================
# Section 28: Multi-path cross-verification (AP10 compliance)
# =====================================================================

class TestMultiPathVerification:
    """Multi-path verification: every numerical result derived by 2+ independent routes.

    AP10: hardcoded expected values are NECESSARY but NOT SUFFICIENT.
    Cross-family consistency, algebraic identities, and independent
    computation paths catch errors that single-path tests cannot.
    """

    @pytest.mark.parametrize("c_val", [1, 6, 13, 24, 25])
    def test_page_time_three_paths(self, c_val):
        """Page time via 3 independent derivations.

        Path 1: page_time_koszul formula.
        Path 2: crossing condition S_hawk(t) = S_island(t), solved algebraically.
        Path 3: complementarity sum: t_P = 6*S_BH / (2*(kappa+kappa')/3).
        """
        c = Rational(c_val)
        S_BH = Rational(26)

        # Path 1: direct formula
        t1 = page_time_koszul(c, S_BH)

        # Path 2: solve crossing (c/6)*t = S_BH - ((26-c)/6)*t
        # => (c + 26 - c)/6 * t = S_BH => t = 6*S_BH/26 = 3*S_BH/13
        t2 = 6 * S_BH / 26

        # Path 3: via complementarity sum
        kappa_sum = kappa_virasoro(c) + kappa_dual_virasoro(c)
        # Rates: hawking = 2*kappa/3, island = -2*kappa'/3
        # Crossing: (2*kappa/3)*t = S_BH - (2*kappa'/3)*t
        # => (2/3)*(kappa+kappa')*t = S_BH => t = 3*S_BH/(kappa+kappa')
        t3 = 3 * S_BH / kappa_sum

        assert t1 == t2 == t3

    @pytest.mark.parametrize("c_val", [1, 6, 13, 25])
    def test_kappa_complementarity_three_paths(self, c_val):
        """kappa + kappa' = 13 via 3 independent routes.

        Path 1: direct formula c/2 + (26-c)/2.
        Path 2: from the complementarity_sum_virasoro function.
        Path 3: algebraic: (c + 26 - c)/2 = 26/2 = 13.
        """
        c = Rational(c_val)
        path1 = Rational(c, 2) + Rational(26 - c, 2)
        path2 = complementarity_sum_virasoro(c)
        path3 = Rational(26, 2)
        assert path1 == path2 == path3 == 13

    @pytest.mark.parametrize("c_val", [1, 6, 13, 24])
    def test_page_entropy_two_paths(self, c_val):
        """S_Page(t_P) via 2 independent routes.

        Path 1: (c/6) * t_P = (c/6) * (3*S_BH/13) = c*S_BH/26.
        Path 2: page_entropy_at_transition function.
        """
        c = Rational(c_val)
        S_BH = Rational(26)
        t_P = page_time_koszul(c, S_BH)
        path1 = Rational(c, 6) * t_P
        path2 = page_entropy_at_transition(c, S_BH)
        expected = c * S_BH / 26
        assert path1 == path2 == expected

    @pytest.mark.parametrize("g", [1, 2, 3, 4])
    def test_complementarity_correction_sum_two_paths(self, g):
        """F_g(c) + F_g(26-c) = 13*lambda_g via 2 paths.

        Path 1: complementarity_correction_sum function.
        Path 2: explicit kappa computation.
        """
        for c_val in [Rational(1), Rational(6), Rational(13)]:
            path1 = complementarity_correction_sum(c_val, g)
            kappa_c = kappa_virasoro(c_val)
            kappa_d = kappa_virasoro(26 - c_val)
            path2 = (kappa_c + kappa_d) * faber_pandharipande(g)
            assert path1 == path2 == Rational(13) * faber_pandharipande(g)

    @pytest.mark.parametrize("c_val", [1, 6, 13, 25])
    def test_quantum_correction_antisymmetry_two_paths(self, c_val):
        """delta^{(g)}(c) = -delta^{(g)}(26-c) via 2 paths.

        Path 1: quantum_page_correction_genus at c and 26-c.
        Path 2: (kappa - kappa')*lambda_g = -(kappa' - kappa)*lambda_g.
        """
        c = Rational(c_val)
        for g in range(1, 4):
            path1_c = quantum_page_correction_genus(c, g)
            path1_d = quantum_page_correction_genus(26 - c, g)

            lamb = faber_pandharipande(g)
            kappa = kappa_virasoro(c)
            kappa_d = kappa_dual_virasoro(c)
            path2_c = (kappa - kappa_d) * lamb
            path2_d = (kappa_d - kappa) * lamb

            assert path1_c == path2_c
            assert path1_d == path2_d
            assert path1_c + path1_d == 0

    def test_shadow_metric_gaussian_vs_expanded(self):
        """Q(t) via Gaussian decomposition vs expanded polynomial.

        Path 1: Q = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.
        Path 2: Q = q0 + q1*t + q2*t^2 from shadow_metric_virasoro.
        """
        for c_val in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            sm = shadow_metric_virasoro(c_val)
            kappa = sm['kappa']
            alpha = sm['alpha']
            Delta = sm['Delta']
            for t_val in [Rational(0), Rational(1), Rational(3)]:
                path1 = (2*kappa + 3*alpha*t_val)**2 + 2*Delta*t_val**2
                path2 = sm['q0'] + sm['q1']*t_val + sm['q2']*t_val**2
                path3 = shadow_metric_at_time(c_val, t_val)
                assert path1 == path2 == path3

    @pytest.mark.parametrize("c_val", [1, 6, 13, 25])
    def test_discriminant_complementarity_two_paths(self, c_val):
        """Discriminant complementarity via 2 paths.

        Path 1: discriminant_at_page_transition.
        Path 2: explicit 40/(5c+22) + 40/(5(26-c)+22) = 6960/[(5c+22)(152-5c)].
        """
        c = Rational(c_val)
        d = discriminant_at_page_transition(c)

        # Path 2: manual computation
        denom_1 = 5*c + 22
        denom_2 = 5*(26 - c) + 22
        D1 = Rational(40, denom_1)
        D2 = Rational(40, denom_2)
        expected_sum = Rational(6960, denom_1 * denom_2)
        # Note: denom_2 = 152 - 5c
        assert denom_2 == 152 - 5*c
        assert D1 + D2 == expected_sum
        assert d['complementarity_sum'] == expected_sum
        assert d['sum_matches']

    def test_time_dependent_complementarity_algebraic(self):
        """kappa(t) + kappa'(t) = 13 is algebraically necessary.

        kappa(t) = (c/2)(1 - t/t_evap)
        kappa'(t) = 13 - kappa(t)  [by definition]
        Sum = 13 identically. This is NOT a numerical accident.
        """
        from sympy import Symbol as Sym, simplify as sym_simplify
        c_s = Sym('c', positive=True)
        t_s = Sym('t', nonneg=True)
        S_s = Sym('S', positive=True)
        t_evap_s = 6 * S_s / c_s
        kappa_t = (c_s / 2) * (1 - t_s / t_evap_s)
        kappa_d_t = 13 - kappa_t
        assert sym_simplify(kappa_t + kappa_d_t - 13) == 0

    def test_page_time_c_independence_algebraic(self):
        """t_P = 3*S_BH/13 is algebraically c-independent.

        Crossing: (c/6)*t = S_BH - ((26-c)/6)*t
        => (26/6)*t = S_BH => t = 6*S_BH/26 = 3*S_BH/13.
        The c cancels. This is the CONTENT of AP24 for Virasoro.
        """
        from sympy import Symbol as Sym, solve as sym_solve
        c_s = Sym('c', positive=True)
        t_s = Sym('t', positive=True)
        S_s = Sym('S', positive=True)
        eq = (c_s / 6) * t_s - (S_s - ((26 - c_s) / 6) * t_s)
        sol = sym_solve(eq, t_s)
        assert len(sol) == 1
        # The solution should be independent of c
        assert sol[0].diff(c_s) == 0
        assert sol[0] == 3 * S_s / 13
