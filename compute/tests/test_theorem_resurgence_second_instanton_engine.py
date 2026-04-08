r"""Tests for the higher-instanton resurgence engine.

Multi-path verification of:
    (1) Residues at all poles of G[F](xi) = kappa*(xi/(2 sin(xi/2)) - 1)
    (2) Stokes constants S_n = (-1)^n * 4*pi^2*n*kappa*i
    (3) Universal ratio S_n/S_1 = (-1)^{n+1}*n
    (4) Alien derivatives at all instantons
    (5) Ecalle bridge equation consistency
    (6) Multi-instanton sector decomposition
    (7) Partial-fraction reconstruction of G[F]
    (8) Anomaly cancellation at c=26 for all instantons
    (9) Instanton hierarchy and exponential suppression
    (10) Large-order / instanton reconstruction of F_g

Each result is verified by at least 2 independent paths (AP10 compliance).
"""

import cmath
import math
import sys

import pytest

sys.path.insert(0, "/Users/raeez/chiral-bar-cobar/compute/lib")

from theorem_resurgence_second_instanton_engine import (
    STANDARD_FAMILIES,
    UNIVERSAL_INSTANTON_ACTION,
    F_g_exact_value,
    F_g_from_all_instantons,
    alien_derivative_at_instanton,
    alien_derivative_leibniz_check,
    anomaly_cancellation_all_instantons,
    bridge_equation_discontinuity,
    instanton_action,
    instanton_action_ratio,
    instanton_decomposition_of_F_g,
    instanton_hierarchy,
    kappa_heisenberg,
    kappa_kac_moody,
    kappa_virasoro,
    large_order_from_n_th_instanton,
    multi_instanton_sector,
    partial_fraction_reconstruction,
    partial_fraction_vs_closed_form,
    residue_at_pole,
    residue_at_pole_numerical,
    second_instanton_full_analysis,
    stokes_constant,
    stokes_constant_from_mc,
    stokes_ratio,
    stokes_ratio_analytic,
    trans_series,
    verify_ratio_universality,
)

PI = math.pi


# ============================================================================
# Section 1: Residue tests (analytic + numerical cross-check)
# ============================================================================

class TestResidues:
    """Residues of G[F] at xi = 2*pi*n."""

    def test_residue_n1_analytic(self):
        """Res_{xi=2pi} G[F] = -2*pi*kappa for Virasoro c=1."""
        kappa = 0.5
        res = residue_at_pole(1, kappa)
        expected = -2.0 * PI * kappa  # (-1)^1 * 2*pi*1 * kappa
        assert abs(res - expected) < 1e-12

    def test_residue_n2_analytic(self):
        """Res_{xi=4pi} G[F] = +4*pi*kappa."""
        kappa = 0.5
        res = residue_at_pole(2, kappa)
        expected = 4.0 * PI * kappa  # (-1)^2 * 2*pi*2 * kappa
        assert abs(res - expected) < 1e-12

    def test_residue_n3_analytic(self):
        """Res_{xi=6pi} G[F] = -6*pi*kappa."""
        kappa = 0.5
        res = residue_at_pole(3, kappa)
        expected = -6.0 * PI * kappa  # (-1)^3 * 2*pi*3 * kappa
        assert abs(res - expected) < 1e-12

    def test_residue_n4_analytic(self):
        kappa = 0.5
        res = residue_at_pole(4, kappa)
        expected = 8.0 * PI * kappa  # (-1)^4 * 2*pi*4 * kappa
        assert abs(res - expected) < 1e-12

    def test_residue_n5_analytic(self):
        kappa = 0.5
        res = residue_at_pole(5, kappa)
        expected = -10.0 * PI * kappa
        assert abs(res - expected) < 1e-12

    def test_residue_general_formula(self):
        """Verify Res = (-1)^n * 2*pi*n*kappa for n=1,...,10."""
        kappa = 3.7
        for n in range(1, 11):
            res = residue_at_pole(n, kappa)
            expected = ((-1) ** n) * 2.0 * PI * n * kappa
            assert abs(res - expected) < 1e-10, f"Failed at n={n}"

    def test_residue_numerical_vs_analytic_n1(self):
        """Cross-check: numerical contour integral vs analytic at n=1."""
        kappa = 2.5
        analytic = residue_at_pole(1, kappa)
        numerical = residue_at_pole_numerical(1, kappa)
        assert abs(analytic - numerical.real) / abs(analytic) < 1e-4

    def test_residue_numerical_vs_analytic_n2(self):
        """Cross-check: numerical contour integral vs analytic at n=2."""
        kappa = 2.5
        analytic = residue_at_pole(2, kappa)
        numerical = residue_at_pole_numerical(2, kappa)
        assert abs(analytic - numerical.real) / abs(analytic) < 1e-4

    def test_residue_numerical_vs_analytic_n3(self):
        """Cross-check: numerical contour integral vs analytic at n=3."""
        kappa = 2.5
        analytic = residue_at_pole(3, kappa)
        numerical = residue_at_pole_numerical(3, kappa)
        assert abs(analytic - numerical.real) / abs(analytic) < 1e-4

    def test_residue_zero_at_n0(self):
        """No pole at xi=0: residue is 0."""
        assert residue_at_pole(0, 1.0) == 0.0

    def test_residue_linearity_in_kappa(self):
        """Residue is linear in kappa."""
        for n in range(1, 6):
            r1 = residue_at_pole(n, 1.0)
            r3 = residue_at_pole(n, 3.0)
            assert abs(r3 - 3.0 * r1) < 1e-12


# ============================================================================
# Section 2: Stokes constant tests
# ============================================================================

class TestStokesConstants:
    """S_n = (-1)^n * 4*pi^2*n*kappa*i."""

    def test_S1_explicit(self):
        """S_1 = -4*pi^2*kappa*i."""
        kappa = 1.0
        S1 = stokes_constant(1, kappa)
        expected = -4.0 * PI ** 2 * kappa * 1j
        assert abs(S1 - expected) < 1e-10

    def test_S2_explicit(self):
        """S_2 = +8*pi^2*kappa*i."""
        kappa = 1.0
        S2 = stokes_constant(2, kappa)
        expected = 8.0 * PI ** 2 * kappa * 1j
        assert abs(S2 - expected) < 1e-10

    def test_S3_explicit(self):
        """S_3 = -12*pi^2*kappa*i."""
        kappa = 1.0
        S3 = stokes_constant(3, kappa)
        expected = -12.0 * PI ** 2 * kappa * 1j
        assert abs(S3 - expected) < 1e-10

    def test_S4_explicit(self):
        """S_4 = +16*pi^2*kappa*i."""
        kappa = 1.0
        S4 = stokes_constant(4, kappa)
        expected = 16.0 * PI ** 2 * kappa * 1j
        assert abs(S4 - expected) < 1e-10

    def test_S5_explicit(self):
        """S_5 = -20*pi^2*kappa*i."""
        kappa = 1.0
        S5 = stokes_constant(5, kappa)
        expected = -20.0 * PI ** 2 * kappa * 1j
        assert abs(S5 - expected) < 1e-10

    def test_stokes_from_residue_vs_direct(self):
        """S_n = 2*pi*i * Res_n (definition) matches direct formula."""
        kappa = 4.2
        for n in range(1, 8):
            from_residue = 2.0j * PI * residue_at_pole(n, kappa)
            direct = stokes_constant(n, kappa)
            assert abs(from_residue - direct) < 1e-10, f"Failed at n={n}"

    def test_stokes_from_mc_matches(self):
        """MC-derived Stokes constant matches Borel-derived for n=1,...,5."""
        kappa = 6.5
        for n in range(1, 6):
            s_borel = stokes_constant(n, kappa)
            s_mc = stokes_constant_from_mc(n, kappa)
            assert abs(s_borel - s_mc) < 1e-10

    def test_stokes_purely_imaginary(self):
        """All S_n are purely imaginary."""
        kappa = 2.0
        for n in range(1, 10):
            S_n = stokes_constant(n, kappa)
            assert abs(S_n.real) < 1e-12

    def test_stokes_magnitude_grows_linearly(self):
        """|S_n| = 4*pi^2*n*kappa grows linearly in n."""
        kappa = 1.0
        for n in range(1, 10):
            mag = abs(stokes_constant(n, kappa))
            expected = 4.0 * PI ** 2 * n * kappa
            assert abs(mag - expected) < 1e-10

    def test_stokes_alternating_sign(self):
        """Im(S_n) alternates sign: negative for odd n, positive for even n."""
        kappa = 1.0
        for n in range(1, 10):
            S_n = stokes_constant(n, kappa)
            if n % 2 == 1:
                assert S_n.imag < 0
            else:
                assert S_n.imag > 0


# ============================================================================
# Section 3: Universal ratio S_n/S_1 = (-1)^{n+1}*n
# ============================================================================

class TestUniversalRatio:
    """S_n/S_1 = (-1)^{n+1}*n, independent of kappa."""

    def test_ratio_n1(self):
        """S_1/S_1 = 1."""
        assert abs(stokes_ratio_analytic(1) - 1.0) < 1e-15

    def test_ratio_n2(self):
        """S_2/S_1 = -2."""
        assert abs(stokes_ratio_analytic(2) - (-2.0)) < 1e-15

    def test_ratio_n3(self):
        """S_3/S_1 = 3."""
        assert abs(stokes_ratio_analytic(3) - 3.0) < 1e-15

    def test_ratio_n4(self):
        """S_4/S_1 = -4."""
        assert abs(stokes_ratio_analytic(4) - (-4.0)) < 1e-15

    def test_ratio_n5(self):
        """S_5/S_1 = 5."""
        assert abs(stokes_ratio_analytic(5) - 5.0) < 1e-15

    def test_ratio_computed_matches_analytic_n1_to_5(self):
        """Computed ratio from Stokes constants matches analytic formula."""
        kappa = 7.3
        for n in range(1, 6):
            computed = stokes_ratio(n, kappa)
            analytic = stokes_ratio_analytic(n)
            assert abs(computed - analytic) < 1e-10

    def test_ratio_independent_of_kappa(self):
        """Ratio is the same for all kappa values."""
        kappas = [0.1, 0.5, 1.0, 5.0, 13.0, 100.0]
        for n in range(1, 6):
            ratios = [stokes_ratio(n, k) for k in kappas]
            for r in ratios:
                assert abs(r - ratios[0]) < 1e-10

    def test_ratio_universal_across_families(self):
        """Verify universality across all standard families."""
        results = verify_ratio_universality(n_max=5)
        for name, family_results in results.items():
            for entry in family_results:
                assert entry['match'], (
                    f"Family {name}, n={entry['n']}: "
                    f"computed={entry['computed_ratio']}, "
                    f"expected={entry['expected_ratio']}"
                )

    def test_ratio_formula_derivation(self):
        """Direct derivation: S_n/S_1 = [(-1)^n*n] / [(-1)^1*1] = (-1)^{n+1}*n."""
        for n in range(1, 20):
            ratio = ((-1) ** n * n) / ((-1) ** 1 * 1)
            expected = ((-1) ** (n + 1)) * n
            assert abs(ratio - expected) < 1e-15


# ============================================================================
# Section 4: Second instanton detailed analysis
# ============================================================================

class TestSecondInstanton:
    """Detailed tests for the second instanton at xi = 4*pi."""

    def test_second_instanton_residue(self):
        """Res_{xi=4pi} = 4*pi*kappa."""
        kappa = 6.5
        analysis = second_instanton_full_analysis(kappa)
        expected = 4.0 * PI * kappa
        assert abs(analysis['residue_analytic'] - expected) < 1e-10

    def test_second_instanton_stokes(self):
        """S_2 = 8*pi^2*kappa*i."""
        kappa = 6.5
        analysis = second_instanton_full_analysis(kappa)
        expected = 8.0 * PI ** 2 * kappa * 1j
        assert abs(analysis['S_2'] - expected) < 1e-10

    def test_second_instanton_ratio(self):
        """S_2/S_1 = -2."""
        kappa = 6.5
        analysis = second_instanton_full_analysis(kappa)
        assert analysis['ratio_match']

    def test_second_instanton_action(self):
        """A_2 = 2*A = 8*pi^2."""
        kappa = 1.0
        analysis = second_instanton_full_analysis(kappa)
        assert abs(analysis['A_2'] - 2.0 * UNIVERSAL_INSTANTON_ACTION) < 1e-10

    def test_second_instanton_numerical_residue(self):
        """Numerical contour integral agrees with analytic residue at n=2."""
        kappa = 6.5
        analysis = second_instanton_full_analysis(kappa)
        assert analysis['residue_agreement'] < 1e-3


# ============================================================================
# Section 5: Alien derivative tests
# ============================================================================

class TestAlienDerivatives:
    """Alien derivatives Delta_{omega_n} at all instantons."""

    def test_alien_equals_stokes(self):
        """For simple poles, alien derivative = Stokes constant."""
        kappa = 3.0
        for n in range(1, 6):
            alien = alien_derivative_at_instanton(n, kappa)
            S_n = stokes_constant(n, kappa)
            assert abs(alien - S_n) < 1e-10

    def test_alien_leibniz_additivity(self):
        """Leibniz rule: Delta(F_1 + F_2) = Delta(F_1) + Delta(F_2)."""
        for n in range(1, 6):
            result = alien_derivative_leibniz_check(n, 2.0, 3.0)
            assert result['difference'] < 1e-10

    def test_alien_leibniz_multiple_pairs(self):
        """Leibniz rule for various (kappa_1, kappa_2) pairs."""
        pairs = [(1.0, 1.0), (0.5, 6.5), (13.0, -13.0), (0.1, 99.9)]
        for k1, k2 in pairs:
            for n in range(1, 4):
                result = alien_derivative_leibniz_check(n, k1, k2)
                assert result['difference'] < 1e-10

    def test_alien_c26_cancellation(self):
        """At c=26: matter + ghost alien derivatives cancel."""
        kappa_m = 13.0  # c/2
        kappa_g = -13.0
        for n in range(1, 6):
            delta_m = alien_derivative_at_instanton(n, kappa_m)
            delta_g = alien_derivative_at_instanton(n, kappa_g)
            assert abs(delta_m + delta_g) < 1e-10


# ============================================================================
# Section 6: Ecalle bridge equation tests
# ============================================================================

class TestBridgeEquation:
    """Ecalle bridge equation: discontinuity = instanton sum."""

    def test_bridge_leading_term_sign(self):
        """Leading term has Im < 0 for kappa > 0 (from S_1 = -4*pi^2*kappa*i)."""
        kappa = 1.0
        x_sq = 100.0  # large x^2 so exponential is not tiny
        bridge = bridge_equation_discontinuity(x_sq, kappa, n_max=1)
        leading = bridge['leading_term']
        assert leading.imag < 0

    def test_bridge_exponential_suppression(self):
        """Higher instantons are exponentially suppressed at small x."""
        kappa = 1.0
        x_sq = 5.0  # moderate x^2
        bridge = bridge_equation_discontinuity(x_sq, kappa, n_max=5)
        ps = bridge['partial_sums']
        # Each successive instanton should be smaller in magnitude
        for i in range(1, len(ps)):
            assert abs(ps[i]['contribution']) < abs(ps[i - 1]['contribution'])

    def test_bridge_sum_convergence(self):
        """Bridge equation sum converges as n_max increases."""
        kappa = 1.0
        x_sq = 10.0
        sums = []
        for n_max in [3, 5, 10, 20]:
            bridge = bridge_equation_discontinuity(x_sq, kappa, n_max=n_max)
            sums.append(bridge['total_discontinuity'])
        # Successive differences should decrease
        for i in range(1, len(sums) - 1):
            diff_prev = abs(sums[i] - sums[i - 1])
            diff_next = abs(sums[i + 1] - sums[i])
            # Allow for convergence: later differences should be smaller
            assert diff_next <= diff_prev * 1.1  # tolerance for numerical noise

    def test_bridge_cancellation_c26(self):
        """At c=26, the bridge equation discontinuity vanishes for all n."""
        kappa = 0.0  # kappa_matter + kappa_ghost = 0
        x_sq = 10.0
        bridge = bridge_equation_discontinuity(x_sq, kappa, n_max=5)
        assert abs(bridge['total_discontinuity']) < 1e-15


# ============================================================================
# Section 7: Partial-fraction reconstruction tests
# ============================================================================

class TestPartialFraction:
    """Partial-fraction reconstruction of G[F]."""

    def test_pf_at_xi_1(self):
        """Partial fraction agrees with closed form at xi=1.

        The Euler expansion 1/sin(z) = sum (-1)^n/(z - n*pi) converges
        conditionally (like an alternating harmonic series).  With n_max=500,
        relative error ~ 1e-5 at xi=1.
        """
        kappa = 1.0
        result = partial_fraction_vs_closed_form(1.0, kappa, n_max=500)
        assert result['relative_error'] < 1e-3

    def test_pf_at_xi_3(self):
        """Partial fraction at xi=3 (between first and second poles)."""
        kappa = 1.0
        result = partial_fraction_vs_closed_form(3.0, kappa, n_max=500)
        assert result['relative_error'] < 1e-2

    def test_pf_at_complex_xi(self):
        """Partial fraction at complex xi (exponentially better convergence)."""
        kappa = 2.0
        result = partial_fraction_vs_closed_form(1.0 + 0.5j, kappa, n_max=500)
        assert result['relative_error'] < 1e-3

    def test_pf_near_origin(self):
        """Partial fraction at small xi matches Taylor expansion."""
        kappa = 1.0
        result = partial_fraction_vs_closed_form(0.1, kappa, n_max=500)
        assert result['relative_error'] < 1e-5

    def test_pf_convergence_with_n_max(self):
        """Partial fraction improves with more terms."""
        kappa = 1.0
        xi = 2.0
        errors = []
        for n_max in [10, 50, 100, 200]:
            result = partial_fraction_vs_closed_form(xi, kappa, n_max=n_max)
            errors.append(result['relative_error'])
        # Errors should decrease
        for i in range(len(errors) - 1):
            assert errors[i + 1] < errors[i]


# ============================================================================
# Section 8: Multi-instanton expansion tests
# ============================================================================

class TestMultiInstanton:
    """Multi-instanton sectors and trans-series."""

    def test_instanton_action_n1(self):
        """A_1 = (2*pi)^2."""
        assert abs(instanton_action(1) - UNIVERSAL_INSTANTON_ACTION) < 1e-10

    def test_instanton_action_n2(self):
        """A_2 = 2*(2*pi)^2."""
        assert abs(instanton_action(2) - 2.0 * UNIVERSAL_INSTANTON_ACTION) < 1e-10

    def test_instanton_action_ratio_universal(self):
        """A_n/A_1 = n for n=1,...,10."""
        for n in range(1, 11):
            assert abs(instanton_action_ratio(n) - float(n)) < 1e-15

    def test_trans_series_perturbative_matches_F_g(self):
        """Perturbative sector matches sum of F_g."""
        kappa = 6.5
        x_sq = 0.01  # small x^2 for convergence
        ts = trans_series(x_sq, kappa, k_max=0)
        pert = ts['perturbative']
        # Compare with direct sum of F_g
        direct = sum(F_g_exact_value(g, kappa) * x_sq ** g for g in range(1, 30))
        assert abs(pert - direct) / max(abs(direct), 1e-100) < 1e-8

    def test_instanton_hierarchy_suppression(self):
        """Higher instantons are exponentially suppressed."""
        kappa = 1.0
        x_sq = 5.0
        hierarchy = instanton_hierarchy(x_sq, kappa, n_max=5)
        for i in range(1, len(hierarchy)):
            assert hierarchy[i]['magnitude'] < hierarchy[i - 1]['magnitude']


# ============================================================================
# Section 9: Large-order / instanton reconstruction of F_g
# ============================================================================

class TestLargeOrder:
    """Reconstruct F_g from instanton contributions."""

    def test_F1_reconstruction(self):
        """F_1 = kappa/24 reconstructed from instantons."""
        kappa = 1.0
        reconstructed = F_g_from_all_instantons(1, kappa, n_max=500)
        exact = F_g_exact_value(1, kappa)
        assert abs(reconstructed - exact) / abs(exact) < 1e-3

    def test_F2_reconstruction(self):
        """F_2 = 7*kappa/5760 reconstructed from instantons."""
        kappa = 1.0
        reconstructed = F_g_from_all_instantons(2, kappa, n_max=500)
        exact = F_g_exact_value(2, kappa)
        assert abs(reconstructed - exact) / abs(exact) < 1e-3

    def test_F3_reconstruction(self):
        """F_3 = 31*kappa/967680 reconstructed from instantons."""
        kappa = 1.0
        reconstructed = F_g_from_all_instantons(3, kappa, n_max=500)
        exact = F_g_exact_value(3, kappa)
        assert abs(reconstructed - exact) / abs(exact) < 1e-3

    def test_instanton_decomposition_dominant_term(self):
        """The n=1 instanton dominates the sum for large g."""
        kappa = 1.0
        for g in [3, 5, 8]:
            decomp = instanton_decomposition_of_F_g(g, kappa, n_max=10)
            # n=1 contribution should be largest in magnitude
            c1 = abs(decomp['contributions'][0]['contribution'])
            for entry in decomp['contributions'][1:]:
                assert abs(entry['contribution']) < c1

    def test_reconstruction_improves_with_n_max(self):
        """Instanton reconstruction improves as more terms are added."""
        kappa = 1.0
        g = 2
        errors = []
        for n_max in [10, 50, 200, 500]:
            reconstructed = F_g_from_all_instantons(g, kappa, n_max=n_max)
            exact = F_g_exact_value(g, kappa)
            errors.append(abs(reconstructed - exact) / abs(exact))
        for i in range(len(errors) - 1):
            assert errors[i + 1] < errors[i]


# ============================================================================
# Section 10: Anomaly cancellation at all instantons
# ============================================================================

class TestAnomalyCancellation:
    """All-instanton anomaly cancellation at c=26."""

    def test_c26_kappa_cancels(self):
        """kappa(matter) + kappa(ghost) = 0 at c=26."""
        result = anomaly_cancellation_all_instantons(c=26.0)
        assert result['kappa_cancels']

    def test_c26_all_stokes_cancel(self):
        """S_n(matter) + S_n(ghost) = 0 for n=1,...,5 at c=26."""
        result = anomaly_cancellation_all_instantons(c=26.0, n_max=5)
        assert result['all_cancel']

    def test_c26_stokes_cancel_n1(self):
        result = anomaly_cancellation_all_instantons(c=26.0)
        assert result['stokes_data'][0]['cancellation']

    def test_c26_stokes_cancel_n2(self):
        result = anomaly_cancellation_all_instantons(c=26.0)
        assert result['stokes_data'][1]['cancellation']

    def test_c_not_26_no_cancellation(self):
        """At c != 26, Stokes constants do NOT cancel."""
        result = anomaly_cancellation_all_instantons(c=25.0)
        assert not result['kappa_cancels']
        assert not result['all_cancel']


# ============================================================================
# Section 11: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Tests across multiple algebra families."""

    def test_heisenberg_stokes_constants(self):
        """Heisenberg k=1: kappa=1, S_1=-4*pi^2*i."""
        kappa = kappa_heisenberg(1.0)
        S1 = stokes_constant(1, kappa)
        expected = -4.0 * PI ** 2 * 1j
        assert abs(S1 - expected) < 1e-10

    def test_sl2_k1_stokes(self):
        """sl2 at k=1: kappa = 3*(1+2)/(2*2) = 9/4."""
        kappa = kappa_kac_moody(3, 1.0, 2.0)
        assert abs(kappa - 2.25) < 1e-10
        S1 = stokes_constant(1, kappa)
        expected = -4.0 * PI ** 2 * 2.25 * 1j
        assert abs(S1 - expected) < 1e-10

    def test_virasoro_self_dual_c13(self):
        """At c=13 (self-dual): kappa=13/2, S_n still obey universal ratio."""
        kappa = kappa_virasoro(13.0)
        for n in range(1, 6):
            ratio = stokes_ratio(n, kappa)
            expected = stokes_ratio_analytic(n)
            assert abs(ratio - expected) < 1e-10

    def test_additivity_independent_systems(self):
        """kappa(A+B) = kappa(A) + kappa(B) implies S_n(A+B) = S_n(A) + S_n(B)."""
        k1 = 2.5
        k2 = 4.3
        for n in range(1, 6):
            s1 = stokes_constant(n, k1)
            s2 = stokes_constant(n, k2)
            s_sum = stokes_constant(n, k1 + k2)
            assert abs(s_sum - (s1 + s2)) < 1e-10

    def test_stokes_scales_with_kappa(self):
        """S_n(lambda*kappa) = lambda * S_n(kappa)."""
        kappa = 3.0
        lam = 7.0
        for n in range(1, 6):
            scaled = stokes_constant(n, lam * kappa)
            direct = lam * stokes_constant(n, kappa)
            assert abs(scaled - direct) < 1e-10


# ============================================================================
# Section 12: Instanton action universality
# ============================================================================

class TestInstantonAction:
    """A = (2*pi)^2 is universal."""

    def test_instanton_action_value(self):
        """A = (2*pi)^2 = 4*pi^2."""
        assert abs(UNIVERSAL_INSTANTON_ACTION - 4.0 * PI ** 2) < 1e-10

    def test_instanton_action_numerical(self):
        """A ~ 39.4784."""
        assert abs(UNIVERSAL_INSTANTON_ACTION - 39.478417604357434) < 1e-8

    def test_higher_instanton_actions(self):
        """A_n = n * A for n=1,...,10."""
        for n in range(1, 11):
            assert abs(instanton_action(n) - n * UNIVERSAL_INSTANTON_ACTION) < 1e-10


# ============================================================================
# Section 13: Exact F_g values (ground truth from FP formula)
# ============================================================================

class TestExactValues:
    """Ground-truth F_g values from the Faber-Pandharipande formula."""

    def test_F1_value(self):
        """F_1 = kappa/24."""
        kappa = 1.0
        assert abs(F_g_exact_value(1, kappa) - 1.0 / 24.0) < 1e-15

    def test_F2_value(self):
        """F_2 = 7*kappa/5760."""
        kappa = 1.0
        assert abs(F_g_exact_value(2, kappa) - 7.0 / 5760.0) < 1e-15

    def test_F3_value(self):
        """F_3 = 31*kappa/967680."""
        kappa = 1.0
        assert abs(F_g_exact_value(3, kappa) - 31.0 / 967680.0) < 1e-15

    def test_F_g_positive(self):
        """F_g > 0 for all g >= 1 and kappa > 0."""
        kappa = 1.0
        for g in range(1, 20):
            assert F_g_exact_value(g, kappa) > 0
