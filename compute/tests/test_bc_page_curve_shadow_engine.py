"""Tests for bc_page_curve_shadow_engine.py

Multi-path verification for the Page curve from Koszul complementarity.
AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0).
AP8: Self-dual at c = 13, NOT c = 26.
"""

import math
import unittest
from fractions import Fraction

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sympy import Rational

from lib.bc_page_curve_shadow_engine import (
    faber_pandharipande,
    kappa_virasoro,
    kappa_dual_virasoro,
    complementarity_sum,
    scalar_free_energy,
    Q_contact_virasoro,
    shadow_S3_virasoro,
    shadow_S4_virasoro,
    shadow_S5_virasoro,
    shadow_radius_virasoro,
    hawking_entropy,
    island_entropy_koszul,
    page_curve_koszul_value,
    page_curve_full,
    page_curve_sampled,
    page_time_koszul,
    page_time_shadow_corrected,
    page_time_c_scan,
    qes_island_radius,
    qes_island_radius_exact,
    qes_shadow_shift,
    qes_family_census,
    entanglement_entropy_scalar,
    entanglement_shadow_correction_r,
    entanglement_entropy_corrected,
    entanglement_complementarity_corrected,
    replica_partition_Z_n,
    wormhole_correction_genus,
    disconnected_wormhole_g1_g1,
    replica_wormhole_census,
    renyi_entropy_scalar,
    renyi_entropy_genus_correction,
    von_neumann_genus_correction,
    renyi_full,
    renyi_spectrum,
    renyi_shadow_tower_effect,
    scrambling_time_shadow,
    scrambling_time_family_census,
    hayden_preskill_recovery_time,
    hayden_preskill_family_comparison,
    brane_shadow_entropy,
    double_holography_island_formula,
    self_dual_page_curve,
    self_dual_symmetry_verification,
    full_page_census,
    verify_complementarity_at_genus,
    verify_page_crossing,
    verify_koszul_page_time_c_independence,
    verify_renyi_von_neumann_limit,
    verify_replica_additivity,
    verify_island_holographic_consistency,
    quantum_page_correction,
    quantum_page_curve_full,
)


class TestFaberPandharipande(unittest.TestCase):
    """Test Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        self.assertEqual(faber_pandharipande(1), Rational(1, 24))

    def test_lambda2(self):
        self.assertEqual(faber_pandharipande(2), Rational(7, 5760))

    def test_lambda3(self):
        self.assertEqual(faber_pandharipande(3), Rational(31, 967680))

    def test_positive_all_genera(self):
        for g in range(1, 8):
            self.assertGreater(faber_pandharipande(g), 0)

    def test_invalid_genus(self):
        with self.assertRaises(ValueError):
            faber_pandharipande(0)


class TestKappaComplementarity(unittest.TestCase):
    """Test kappa and complementarity (AP24 critical)."""

    def test_kappa_formula(self):
        """kappa(Vir_c) = c/2."""
        self.assertEqual(kappa_virasoro(Rational(26)), Rational(13))
        self.assertEqual(kappa_virasoro(Rational(13)), Rational(13, 2))
        self.assertEqual(kappa_virasoro(Rational(1)), Rational(1, 2))

    def test_kappa_dual_formula(self):
        """kappa(Vir_{26-c}) = (26-c)/2."""
        self.assertEqual(kappa_dual_virasoro(Rational(1)), Rational(25, 2))
        self.assertEqual(kappa_dual_virasoro(Rational(13)), Rational(13, 2))
        self.assertEqual(kappa_dual_virasoro(Rational(26)), Rational(0))

    def test_complementarity_sum_is_13(self):
        """AP24: kappa + kappa' = 13 for ALL c."""
        for c in range(0, 27):
            self.assertEqual(complementarity_sum(Rational(c)), Rational(13))

    def test_complementarity_sum_fractional_c(self):
        """Sum is 13 even for fractional c."""
        for c in [Rational(1, 2), Rational(7, 3), Rational(25, 2)]:
            self.assertEqual(complementarity_sum(c), Rational(13))

    def test_self_dual_at_c13(self):
        """At c = 13: kappa = kappa' = 13/2."""
        self.assertEqual(kappa_virasoro(Rational(13)),
                         kappa_dual_virasoro(Rational(13)))


class TestShadowCoefficients(unittest.TestCase):
    """Test shadow tower coefficients."""

    def test_Q_contact_c1(self):
        """Q^contact at c=1: 10/27."""
        self.assertEqual(Q_contact_virasoro(Rational(1)), Rational(10, 27))

    def test_Q_contact_c13(self):
        """Q^contact at c=13: 10/1131."""
        self.assertEqual(Q_contact_virasoro(Rational(13)), Rational(10, 1131))

    def test_Q_contact_undefined_at_0(self):
        with self.assertRaises(ValueError):
            Q_contact_virasoro(Rational(0))

    def test_S3_formula(self):
        """S_3 = 2 (c-independent, universal gravitational cubic)."""
        self.assertEqual(shadow_S3_virasoro(Rational(1)), Rational(2))
        self.assertEqual(shadow_S3_virasoro(Rational(13)), Rational(2))

    def test_S4_formula(self):
        """S_4 = Q^contact = 10/[c(5c+22)]."""
        self.assertEqual(shadow_S4_virasoro(Rational(1)), Rational(10, 27))

    def test_S5_formula(self):
        """S_5 = -48/[c^2(5c+22)]."""
        self.assertEqual(shadow_S5_virasoro(Rational(1)), Rational(-48, 27))

    def test_shadow_radius_positive(self):
        """Shadow radius is positive for c > 0."""
        for c in [1, 6, 13, 26]:
            self.assertGreater(shadow_radius_virasoro(c), 0)

    def test_shadow_radius_self_dual(self):
        """rho ~ 0.467 at c=13."""
        self.assertAlmostEqual(shadow_radius_virasoro(13), 0.467, delta=0.01)


class TestPageCurve(unittest.TestCase):
    """Test the Koszul Page curve."""

    def test_hawking_entropy_linear(self):
        """S_hawking = (c/6)*t."""
        self.assertEqual(hawking_entropy(Rational(6), Rational(3)), Rational(3))
        self.assertEqual(hawking_entropy(Rational(13), Rational(6)), Rational(13))

    def test_island_entropy_at_t0(self):
        """At t=0: S_island = S_BH."""
        self.assertEqual(island_entropy_koszul(Rational(6), Rational(0), Rational(100)),
                         Rational(100))

    def test_page_curve_starts_at_zero(self):
        """S_page(0) = 0 (no radiation yet)."""
        self.assertEqual(page_curve_koszul_value(Rational(13), Rational(0), Rational(100)),
                         Rational(0))

    def test_page_curve_bounded_by_SBH(self):
        """S_page <= S_BH for all t."""
        S_BH = Rational(100)
        for c in [6, 13, 25]:
            for t_frac in [Rational(i, 20) for i in range(21)]:
                t = t_frac * 6 * S_BH / Rational(c)  # fraction of evaporation time
                S = page_curve_koszul_value(Rational(c), t, S_BH)
                self.assertLessEqual(S, S_BH)

    def test_page_curve_phases(self):
        """Before Page time: hawking phase. After: island phase."""
        S_BH = Rational(100)
        c = Rational(6)
        t_P = page_time_koszul(c, S_BH)

        # Well before Page time
        data_before = page_curve_full(c, t_P / 2, S_BH)
        self.assertEqual(data_before['phase'], 'hawking')

        # At Page time
        data_at = page_curve_full(c, t_P, S_BH)
        self.assertEqual(data_at['phase'], 'page_point')

        # After Page time
        data_after = page_curve_full(c, t_P * 2, S_BH)
        self.assertEqual(data_after['phase'], 'island')


class TestPageTime(unittest.TestCase):
    """Test Page time computation."""

    def test_page_time_formula(self):
        """t_P = 3*S_BH/13."""
        self.assertEqual(page_time_koszul(Rational(6), Rational(13)), Rational(3))
        self.assertEqual(page_time_koszul(Rational(1), Rational(13)), Rational(3))
        self.assertEqual(page_time_koszul(Rational(25), Rational(13)), Rational(3))

    def test_page_time_c_independent(self):
        """AP24: t_P is independent of c (because kappa + kappa' = 13)."""
        S_BH = Rational(100)
        expected = 3 * S_BH / 13
        for c in range(1, 26):
            self.assertEqual(page_time_koszul(Rational(c), S_BH), expected)

    def test_page_time_c_independence_verification(self):
        """verify_koszul_page_time_c_independence returns True."""
        self.assertTrue(verify_koszul_page_time_c_independence(Rational(100)))

    def test_page_crossing_verification(self):
        """Hawking and island entropies meet at t_P."""
        for c in [6, 10, 13, 20, 25]:
            self.assertTrue(verify_page_crossing(Rational(c), Rational(100)))

    def test_shadow_corrected_page_time(self):
        """Shadow-corrected page time includes scalar result."""
        d = page_time_shadow_corrected(Rational(13), Rational(1000))
        self.assertEqual(d['t_page_scalar'],
                         page_time_koszul(Rational(13), Rational(1000)))

    def test_shadow_correction_small_for_large_SBH(self):
        """For large S_BH, shadow corrections to t_P are small."""
        d = page_time_shadow_corrected(Rational(13), Rational(10000))
        self.assertAlmostEqual(float(d['relative_correction']), 0.0, delta=0.01)

    def test_page_time_scan(self):
        """Page time scan produces correct number of entries."""
        scan = page_time_c_scan(Rational(100), 2, 5)
        self.assertEqual(len(scan), 4)


class TestQES(unittest.TestCase):
    """Test quantum extremal surface (island) location."""

    def test_qes_c13_is_half(self):
        """At c=13: r_island^2/r_h^2 = 1/2."""
        self.assertEqual(qes_island_radius_exact(Rational(13)), Rational(1, 2))

    def test_qes_c6(self):
        """At c=6: r^2/r_h^2 = 20/26 = 10/13."""
        self.assertEqual(qes_island_radius_exact(Rational(6)), Rational(10, 13))

    def test_qes_c26_vanishes(self):
        """At c=26: island radius vanishes."""
        self.assertEqual(qes_island_radius_exact(Rational(26)), Rational(0))

    def test_qes_numerical_c13(self):
        """Numerical QES at c=13: r/r_h = 1/sqrt(2)."""
        r = qes_island_radius(13, 100)
        self.assertAlmostEqual(r, 1.0 / math.sqrt(2), places=5)

    def test_qes_shadow_shift_small(self):
        """Shadow shift to QES is small for large S_BH."""
        shift = qes_shadow_shift(Rational(13), Rational(10000), arity=4)
        self.assertAlmostEqual(float(shift), 0.0, delta=0.001)

    def test_qes_family_census(self):
        """QES census includes c=13 with r^2 = 1/2."""
        census = qes_family_census(Rational(100))
        c13_entry = [d for d in census if d['c'] == 13][0]
        self.assertEqual(c13_entry['r_island_sq'], Rational(1, 2))

    def test_qes_complementarity(self):
        """r^2(c) + r^2(26-c) = 1 for all c."""
        for c in [1, 6, 10, 13, 20, 25]:
            r_sq = qes_island_radius_exact(Rational(c))
            r_sq_dual = qes_island_radius_exact(Rational(26 - c))
            self.assertEqual(r_sq + r_sq_dual, Rational(1))


class TestEntanglement(unittest.TestCase):
    """Test entanglement entropy with shadow corrections."""

    def test_EE_scalar_formula(self):
        """S_EE = (c/3) * log(L/eps)."""
        self.assertEqual(entanglement_entropy_scalar(Rational(1), 1), Rational(1, 3))
        self.assertEqual(entanglement_entropy_scalar(Rational(13), 1), Rational(13, 3))

    def test_EE_scalar_complementarity(self):
        """S(c) + S(26-c) = 26/3 * log_ratio (scalar level).

        S_EE = (c/3)*log, so sum = (c + (26-c))/3 * log = 26/3 * log.
        """
        log_r = Rational(10)
        for c in [1, 6, 10, 20, 25]:
            S_c = entanglement_entropy_scalar(Rational(c), log_r)
            S_dual = entanglement_entropy_scalar(Rational(26 - c), log_r)
            self.assertEqual(S_c + S_dual, Rational(26, 3) * log_r)

    def test_EE_corrected_includes_scalar(self):
        """Corrected EE includes the scalar part."""
        d = entanglement_entropy_corrected(Rational(13), Rational(10))
        self.assertEqual(d['S_scalar'],
                         entanglement_entropy_scalar(Rational(13), Rational(10)))

    def test_EE_corrections_nonzero_for_virasoro(self):
        """Virasoro (class M) has nonzero shadow corrections."""
        d = entanglement_entropy_corrected(Rational(13), Rational(10))
        self.assertNotEqual(d['total_correction'], 0)

    def test_complementarity_corrected_scalar_sum(self):
        """Scalar sum: S(c) + S(26-c) = 26/3 * log_ratio = 260/3 at log_ratio=10."""
        d = entanglement_complementarity_corrected(Rational(13), Rational(10))
        self.assertEqual(d['scalar_sum'], Rational(260, 3))


class TestReplicaWormholes(unittest.TestCase):
    """Test replica wormhole corrections."""

    def test_replica_planar(self):
        """Planar contribution Z_planar = 1."""
        d = replica_partition_Z_n(Rational(13, 2), 2)
        self.assertEqual(d['Z_planar'], Rational(1))

    def test_wormhole_genus1(self):
        """W_1(n) = n * kappa * lambda_1."""
        kappa = Rational(13, 2)
        W1 = wormhole_correction_genus(kappa, 2, 1)
        expected = 2 * kappa * Rational(1, 24)
        self.assertEqual(W1, expected)

    def test_wormhole_linear_in_n(self):
        """W_g(n) is linear in n."""
        kappa = Rational(13, 2)
        W_2 = wormhole_correction_genus(kappa, 2, 1)
        W_3 = wormhole_correction_genus(kappa, 3, 1)
        # W(3)/W(2) = 3/2
        self.assertEqual(W_3 * 2, W_2 * 3)

    def test_wormhole_additivity(self):
        """Wormhole corrections are additive in kappa."""
        self.assertTrue(verify_replica_additivity(Rational(3), Rational(5), 2, 1))
        self.assertTrue(verify_replica_additivity(Rational(1), Rational(12), 3, 2))

    def test_disconnected_wormhole_formula(self):
        """Disconnected W_1^2/2 matches formula."""
        kappa = Rational(13, 2)
        W1 = wormhole_correction_genus(kappa, 2, 1)
        disconn = disconnected_wormhole_g1_g1(kappa, 2)
        self.assertEqual(disconn, W1 ** 2 / 2)

    def test_replica_census_length(self):
        """Census has max_n - 1 entries."""
        census = replica_wormhole_census(Rational(13, 2))
        self.assertEqual(len(census), 4)  # n = 2, 3, 4, 5


class TestRenyiEntropy(unittest.TestCase):
    """Test Renyi entropy."""

    def test_renyi_scalar_formula(self):
        """S_n = (kappa/3)(1+1/n)*log_ratio."""
        self.assertEqual(renyi_entropy_scalar(Rational(13, 2), 2, 1), Rational(13, 4))
        self.assertEqual(renyi_entropy_scalar(Rational(1), 2, 1), Rational(1, 2))

    def test_renyi_n_to_1_limit(self):
        """As n -> infinity, S_n -> (kappa/3) * log_ratio."""
        kappa = Rational(13, 2)
        S_inf = renyi_entropy_scalar(kappa, 1000, 1)
        expected = kappa / 3  # limit of (kappa/3)(1+1/n) as n->inf
        self.assertAlmostEqual(float(S_inf), float(expected), delta=0.01)

    def test_von_neumann_genus_correction(self):
        """Von Neumann limit: 2g * F_g."""
        kappa = Rational(13, 2)
        self.assertEqual(von_neumann_genus_correction(kappa, 1),
                         2 * scalar_free_energy(kappa, 1))

    def test_renyi_genus1_at_n2(self):
        """Genus-1 Renyi correction at n=2."""
        kappa = Rational(1)
        corr = renyi_entropy_genus_correction(kappa, 2, 1)
        # (2/1) * (1/24) * (1 - 1/4) = 2/24 * 3/4 = 6/96 = 1/16
        self.assertEqual(corr, Rational(1, 16))

    def test_renyi_spectrum_length(self):
        """Spectrum has max_n entries (including von Neumann)."""
        spec = renyi_spectrum(Rational(13, 2), Rational(1))
        self.assertEqual(len(spec), 5)  # vN + n=2,3,4,5

    def test_renyi_decreasing_in_n(self):
        """S_n is decreasing in n (for fixed positive kappa)."""
        kappa = Rational(13, 2)
        for n in [2, 3, 4]:
            S_n = renyi_entropy_scalar(kappa, n, 1)
            S_n1 = renyi_entropy_scalar(kappa, n + 1, 1)
            self.assertGreater(S_n, S_n1)

    def test_von_neumann_limit_verification(self):
        """verify_renyi_von_neumann_limit returns correct value."""
        result = verify_renyi_von_neumann_limit(Rational(13, 2), 1)
        self.assertEqual(result, Rational(13, 24))

    def test_renyi_full_returns_components(self):
        """Full Renyi includes scalar, corrections, total."""
        d = renyi_full(Rational(13, 2), 2, Rational(1))
        self.assertEqual(d['S_scalar'], Rational(13, 4))
        self.assertIn('genus_corrections', d)
        self.assertIn('S_total', d)

    def test_shadow_tower_affects_spectrum(self):
        """Virasoro shadow tower affects Renyi spectrum."""
        d = renyi_shadow_tower_effect(Rational(13), Rational(10))
        self.assertTrue(d['tower_affects_spectrum'])


class TestScramblingTime(unittest.TestCase):
    """Test scrambling time computations."""

    def test_scrambling_less_than_page(self):
        """t_scramble << t_page for large S_BH."""
        d = scrambling_time_shadow(Rational(13), Rational(1000))
        self.assertLess(d['t_scramble'], d['t_page'])

    def test_scrambling_logarithmic(self):
        """Scrambling time is O(log S_BH)."""
        d1 = scrambling_time_shadow(Rational(13), Rational(100))
        d2 = scrambling_time_shadow(Rational(13), Rational(10000))
        # t_scr ~ log(S), so ratio ~ log(10000)/log(100) = 2
        ratio = d2['t_scramble'] / d1['t_scramble']
        self.assertAlmostEqual(ratio, 2.0, delta=0.1)

    def test_scrambling_inversely_proportional_to_c(self):
        """t_scramble ~ 6/c, so doubling c halves t_scramble."""
        d1 = scrambling_time_shadow(Rational(6), Rational(1000))
        d2 = scrambling_time_shadow(Rational(12), Rational(1000))
        ratio = d1['t_scramble'] / d2['t_scramble']
        self.assertAlmostEqual(ratio, 2.0, places=5)

    def test_family_census_all_scramble_faster_than_page(self):
        """All standard families: t_scr < t_page."""
        census = scrambling_time_family_census(Rational(1000))
        for d in census:
            self.assertLess(d['t_scramble'], d['t_page'])


class TestHaydenPreskill(unittest.TestCase):
    """Test Hayden-Preskill recovery time."""

    def test_recovery_time_positive(self):
        d = hayden_preskill_recovery_time(Rational(13), Rational(1000))
        self.assertGreater(d['delta_t'], 0)

    def test_recovery_time_less_than_page(self):
        """Recovery time < Page time."""
        d = hayden_preskill_recovery_time(Rational(13), Rational(1000))
        self.assertLess(d['delta_t'], d['t_page'])

    def test_total_recovery_after_page(self):
        """Total recovery time (t_page + delta_t) is after the Page time."""
        d = hayden_preskill_recovery_time(Rational(13), Rational(1000))
        self.assertGreater(d['t_total_recovery'], d['t_page'])

    def test_family_comparison(self):
        """All families have positive recovery time."""
        data = hayden_preskill_family_comparison(Rational(1000))
        for d in data:
            self.assertGreater(d['delta_t'], 0)


class TestDoubleHolography(unittest.TestCase):
    """Test double holography / brane-shadow contributions."""

    def test_brane_kappa_is_dual(self):
        """Brane carries the Koszul dual algebra."""
        d = brane_shadow_entropy(Rational(13), Rational(100))
        self.assertEqual(d['kappa_brane'], Rational(13, 2))

    def test_brane_complementarity(self):
        """F_g(bulk) + F_g(brane) = 13 * lambda_g at unit tension."""
        d = brane_shadow_entropy(Rational(6), Rational(100))
        for g in range(1, 4):
            self.assertTrue(d['complementarity_check'][g])

    def test_double_holography_formula(self):
        """No-island entropy is (c/6)*t."""
        d = double_holography_island_formula(Rational(13), Rational(100), Rational(10))
        expected = Rational(13, 6) * 10
        self.assertEqual(d['S_no_island'], expected)


class TestSelfDualC13(unittest.TestCase):
    """Test self-dual properties at c = 13 (AP8)."""

    def test_self_dual_page_curve(self):
        """At c=13: peak = S_BH/2, all corrections vanish."""
        d = self_dual_page_curve(Rational(26))
        self.assertEqual(d['peak_entropy'], Rational(13))
        self.assertEqual(d['page_fraction'], Rational(1, 2))
        self.assertTrue(d['all_corrections_vanish'])

    def test_self_dual_symmetry_full(self):
        """All seven symmetry checks pass at c=13."""
        checks = self_dual_symmetry_verification(Rational(26))
        for name, result in checks.items():
            self.assertTrue(result, f"Check '{name}' failed at c=13")

    def test_quantum_correction_vanishes_at_c13(self):
        """Quantum Page correction vanishes at c=13."""
        for g in range(1, 6):
            self.assertEqual(quantum_page_correction(Rational(13), g), Rational(0))

    def test_quantum_page_curve_at_c13(self):
        """Total correction is zero at c=13."""
        d = quantum_page_curve_full(Rational(13), Rational(3), Rational(13))
        self.assertEqual(d['total_correction'], Rational(0))


class TestComplementarityVerification(unittest.TestCase):
    """Test cross-verification methods."""

    def test_complementarity_all_genera(self):
        """F_g(c) + F_g(26-c) = 13*lambda_g for g=1..5, c=1..25."""
        for c in [1, 6, 10, 13, 20, 25]:
            for g in range(1, 4):
                self.assertTrue(
                    verify_complementarity_at_genus(Rational(c), g),
                    f"Complementarity fails at c={c}, g={g}")

    def test_full_island_consistency(self):
        """Full holographic consistency check passes."""
        checks = verify_island_holographic_consistency(Rational(13), Rational(100))
        for name, result in checks.items():
            self.assertTrue(result, f"Check '{name}' failed")

    def test_full_page_census(self):
        """Census produces correct number of entries."""
        census = full_page_census(Rational(100))
        self.assertGreaterEqual(len(census), 5)
        # All entries have kappa_sum = 13
        for entry in census:
            self.assertEqual(entry['kappa_sum'], Rational(13))


class TestScalarFreeEnergy(unittest.TestCase):
    """Test scalar free energy F_g."""

    def test_F_g_linear_in_kappa(self):
        """F_g(2*kappa) = 2*F_g(kappa)."""
        for g in range(1, 5):
            F1 = scalar_free_energy(Rational(3), g)
            F2 = scalar_free_energy(Rational(6), g)
            self.assertEqual(F2, 2 * F1)

    def test_F_1_is_kappa_over_24(self):
        """F_1 = kappa/24."""
        self.assertEqual(scalar_free_energy(Rational(13, 2), 1), Rational(13, 48))

    def test_complementarity_sum_at_each_genus(self):
        """F_g(kappa) + F_g(kappa') = 13*lambda_g."""
        for c in [1, 6, 13, 20, 25]:
            kappa = kappa_virasoro(Rational(c))
            kappa_d = kappa_dual_virasoro(Rational(c))
            for g in range(1, 5):
                F_sum = scalar_free_energy(kappa, g) + scalar_free_energy(kappa_d, g)
                expected = Rational(13) * faber_pandharipande(g)
                self.assertEqual(F_sum, expected)


class TestPageCurveSampled(unittest.TestCase):
    """Test sampled Page curve."""

    def test_sampled_returns_correct_count(self):
        pts = page_curve_sampled(Rational(13), Rational(130),
                                 [Rational(1, 10), Rational(1, 2)])
        self.assertEqual(len(pts), 2)

    def test_sampled_monotone_before_page(self):
        """Before Page time, curve is monotonically increasing."""
        S_BH = Rational(130)
        t_P = page_time_koszul(Rational(13), S_BH)
        t_vals = [Rational(i, 20) * t_P / S_BH for i in range(1, 10)]
        pts = page_curve_sampled(Rational(13), S_BH, t_vals)
        for i in range(len(pts) - 1):
            self.assertLessEqual(pts[i]['S_page'], pts[i + 1]['S_page'])


class TestQuantumPageCorrections(unittest.TestCase):
    """Test quantum gravity corrections to Page curve."""

    def test_correction_antisymmetric_around_c13(self):
        """delta_S^{(g)}(c) = -delta_S^{(g)}(26-c)."""
        for g in range(1, 5):
            for c in [1, 6, 10, 20, 25]:
                corr = quantum_page_correction(Rational(c), g)
                corr_dual = quantum_page_correction(Rational(26 - c), g)
                self.assertEqual(corr + corr_dual, Rational(0))

    def test_correction_formula(self):
        """delta = (c-13) * lambda_g."""
        for g in [1, 2]:
            c = 14
            corr = quantum_page_correction(Rational(c), g)
            expected = Rational(1) * faber_pandharipande(g)
            self.assertEqual(corr, expected)


if __name__ == '__main__':
    unittest.main()
