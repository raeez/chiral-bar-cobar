r"""
Tests for propagator_weight_universality.py -- verify that the bar propagator
d log E(z,w) is ALWAYS weight 1, so obs_g = kappa * lambda_g uses E_1 for
ALL chiral algebras.

This test suite demonstrates that thm:w3-obstruction (higher_genus_foundations.tex:4423)
is WRONG: it assigns E_h to weight-h generators, producing absurd numerical
discrepancies (13x for Virasoro, 22.6x for W_3).

GRADING: Cohomological, |d| = +1.
"""

import unittest
import re
import os
from fractions import Fraction

from compute.lib.propagator_weight_universality import (
    mumford_exponent,
    virasoro_test,
    w3_discrepancy,
    genus1_curvature_direct,
    genus1_curvature_wrong,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_km,
    kappa_w_n,
    kappa_betagamma,
    kappa_fermion,
    anomaly_ratio_lie,
    anomaly_ratio_w_n,
    harmonic,
    free_energy_universal,
    free_energy_per_channel_correct,
    free_energy_per_channel_wrong,
    field_weight_vs_propagator_weight,
    _lambda_fp_exact,
)


class TestMumfordExponent(unittest.TestCase):
    """Verify the Mumford isomorphism exponent 6j^2 - 6j + 1.

    det(E_j) = lambda^{6j^2 - 6j + 1} (Mumford 1977).
    """

    def test_j1(self):
        """j=1: exponent is 1 (E_1 = standard Hodge bundle)."""
        self.assertEqual(mumford_exponent(1), 1)

    def test_j2(self):
        """j=2: exponent is 13 (quadratic differentials)."""
        self.assertEqual(mumford_exponent(2), 13)

    def test_j3(self):
        """j=3: exponent is 37 (cubic differentials)."""
        self.assertEqual(mumford_exponent(3), 37)

    def test_j4(self):
        """j=4: exponent is 73 (quartic differentials)."""
        self.assertEqual(mumford_exponent(4), 73)

    def test_j5(self):
        """j=5: exponent is 121 (quintic differentials)."""
        self.assertEqual(mumford_exponent(5), 121)

    def test_formula_direct(self):
        """Verify 6j^2 - 6j + 1 against explicit values for j=1..10."""
        expected = [1, 13, 37, 73, 121, 181, 253, 337, 433, 541]
        for j, exp_val in enumerate(expected, start=1):
            self.assertEqual(mumford_exponent(j), exp_val,
                             f"Mumford exponent wrong at j={j}")

    def test_j0_degenerate(self):
        """j=0: exponent is 1 (structure sheaf, trivially)."""
        self.assertEqual(mumford_exponent(0), 1)

    def test_growth_quadratic(self):
        """Mumford exponent grows as 6j^2 for large j.

        6j^2 - 6j + 1 > 4j^2 for j >= 3, and < 7j^2 for all j >= 1.
        """
        for j in range(3, 20):
            e = mumford_exponent(j)
            self.assertGreater(e, 4 * j * j, f"Growth too slow at j={j}")
            self.assertLess(e, 7 * j * j, f"Growth too fast at j={j}")


class TestVirasiroTest(unittest.TestCase):
    """Verify the 13x discrepancy: if Virasoro used E_2, F_1 would be 13x too large.

    This is the decisive falsification of thm:w3-obstruction applied to Virasoro.
    The Virasoro algebra has a single generator T of weight 2, so thm:w3-obstruction
    would assign it to E_2.  But E_2 has Mumford exponent 13, giving F_1 = 13c/48
    instead of the correct c/48.
    """

    def test_ratio_is_13_c1(self):
        """Ratio is exactly 13 at c=1."""
        self.assertEqual(virasoro_test(Fraction(1)), Fraction(13))

    def test_ratio_is_13_c_half(self):
        """Ratio is exactly 13 at c=1/2."""
        self.assertEqual(virasoro_test(Fraction(1, 2)), Fraction(13))

    def test_ratio_is_13_c26(self):
        """Ratio is exactly 13 at c=26 (critical string)."""
        self.assertEqual(virasoro_test(Fraction(26)), Fraction(13))

    def test_ratio_is_13_c_negative(self):
        """Ratio is exactly 13 at c=-22/5 (Yang-Lee)."""
        self.assertEqual(virasoro_test(Fraction(-22, 5)), Fraction(13))

    def test_ratio_is_13_c_generic(self):
        """Ratio is exactly 13 at c=100 (generic)."""
        self.assertEqual(virasoro_test(Fraction(100)), Fraction(13))

    def test_c_independence(self):
        """The ratio 13 is independent of c (structural, not numerical)."""
        test_values = [Fraction(1), Fraction(2), Fraction(-1),
                       Fraction(1, 7), Fraction(100, 3)]
        for c in test_values:
            self.assertEqual(virasoro_test(c), Fraction(13),
                             f"Ratio should be 13 at c={c}")


class TestW3Discrepancy(unittest.TestCase):
    """Verify the 113/5 = 22.6x discrepancy for W_3.

    W_3 has generators T (weight 2, OPE coeff c/2) and W (weight 3, OPE coeff c/3).
    Correct: kappa = c/2 + c/3 = 5c/6.
    Wrong (using E_h): (c/2)*13 + (c/3)*37 = 13c/2 + 37c/3 = (39c+74c)/6 = 113c/6.
    Ratio: (113c/6) / (5c/6) = 113/5.
    """

    def test_ratio_is_113_over_5_c1(self):
        """Ratio is exactly 113/5 at c=1."""
        self.assertEqual(w3_discrepancy(Fraction(1)), Fraction(113, 5))

    def test_ratio_is_113_over_5_c_generic(self):
        """Ratio is exactly 113/5 at c=100."""
        self.assertEqual(w3_discrepancy(Fraction(100)), Fraction(113, 5))

    def test_c_independence(self):
        """The ratio 113/5 is independent of c."""
        for c in [Fraction(1), Fraction(2), Fraction(-1), Fraction(4, 5)]:
            self.assertEqual(w3_discrepancy(c), Fraction(113, 5),
                             f"Ratio should be 113/5 at c={c}")

    def test_wrong_value_explicit(self):
        """Explicit wrong value at c=6: (113*6)/6 = 113."""
        wrong = genus1_curvature_wrong('w3', Fraction(6))
        self.assertEqual(wrong, Fraction(113))

    def test_correct_value_explicit(self):
        """Explicit correct value at c=6: 5*6/6 = 5."""
        correct = genus1_curvature_direct('w3', Fraction(6))
        self.assertEqual(correct, Fraction(5))


class TestW3GenusCurvature(unittest.TestCase):
    """Verify kappa(W_3) = 5c/6 from direct OPE computation.

    T(z)T(w) ~ (c/2)/(z-w)^4 + ...  contributes c/2.
    W(z)W(w) ~ (c/3)/(z-w)^6 + ...  contributes c/3.
    Total: kappa = c/2 + c/3 = 5c/6.
    """

    def test_kappa_w3_c1(self):
        self.assertEqual(kappa_w_n(Fraction(1), 3), Fraction(5, 6))

    def test_kappa_w3_c6(self):
        self.assertEqual(kappa_w_n(Fraction(6), 3), Fraction(5))

    def test_kappa_w3_c12(self):
        self.assertEqual(kappa_w_n(Fraction(12), 3), Fraction(10))

    def test_kappa_w3_matches_formula(self):
        """kappa(W_3, c) = 5c/6 for various c."""
        for c_val in [1, 2, 3, 6, 12, 100]:
            c = Fraction(c_val)
            self.assertEqual(kappa_w_n(c, 3), 5 * c / 6,
                             f"kappa(W_3) wrong at c={c}")

    def test_kappa_w3_additive_decomposition(self):
        """kappa(W_3) = kappa_T + kappa_W = c/2 + c/3."""
        for c_val in [1, 6, 26]:
            c = Fraction(c_val)
            kappa_T = c / 2   # T channel
            kappa_W = c / 3   # W channel
            self.assertEqual(kappa_T + kappa_W, kappa_w_n(c, 3))


class TestWNGenusOneCurvature(unittest.TestCase):
    """Verify kappa(W_N) = c * (H_N - 1) for N=2..6.

    H_N = 1 + 1/2 + ... + 1/N (harmonic number).
    H_N - 1 = 1/2 + 1/3 + ... + 1/N (anomaly ratio).
    """

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: kappa = c/2 = c*(H_2 - 1)."""
        c = Fraction(10)
        self.assertEqual(kappa_w_n(c, 2), kappa_virasoro(c))
        self.assertEqual(kappa_w_n(c, 2), c / 2)

    def test_w3(self):
        """W_3: kappa = c*(1/2 + 1/3) = 5c/6."""
        c = Fraction(6)
        self.assertEqual(kappa_w_n(c, 3), c * (harmonic(3) - 1))
        self.assertEqual(kappa_w_n(c, 3), Fraction(5))

    def test_w4(self):
        """W_4: kappa = c*(1/2 + 1/3 + 1/4) = 13c/12."""
        c = Fraction(12)
        self.assertEqual(kappa_w_n(c, 4), c * (harmonic(4) - 1))
        self.assertEqual(kappa_w_n(c, 4), Fraction(13))

    def test_w5(self):
        """W_5: kappa = c*(1/2 + 1/3 + 1/4 + 1/5) = 77c/60."""
        c = Fraction(60)
        self.assertEqual(kappa_w_n(c, 5), c * (harmonic(5) - 1))
        self.assertEqual(kappa_w_n(c, 5), Fraction(77))

    def test_w6(self):
        """W_6: kappa = c*(1/2 + 1/3 + 1/4 + 1/5 + 1/6) = 87c/60 = 29c/20."""
        c = Fraction(20)
        self.assertEqual(kappa_w_n(c, 6), c * (harmonic(6) - 1))
        self.assertEqual(kappa_w_n(c, 6), Fraction(29))

    def test_anomaly_ratio_matches(self):
        """anomaly_ratio_w_n(N) = H_N - 1 for N=2..6."""
        for N in range(2, 7):
            self.assertEqual(anomaly_ratio_w_n(N), harmonic(N) - 1,
                             f"Anomaly ratio mismatch at N={N}")

    def test_anomaly_ratio_sl_n(self):
        """anomaly_ratio_lie('sl{N}') = H_N - 1 for N=2..6."""
        for N in range(2, 7):
            g_name = f"sl{N}"
            if g_name in ['sl2', 'sl3', 'sl4', 'sl5', 'sl6']:
                self.assertEqual(anomaly_ratio_lie(g_name),
                                 anomaly_ratio_w_n(N),
                                 f"Lie vs W_N anomaly ratio mismatch at N={N}")


class TestKMCurvature(unittest.TestCase):
    """Verify kappa(sl_2, k) = 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2h^v).

    dim(sl_2) = 3, h^v(sl_2) = 2.
    kappa = 3*(k+2)/(2*2) = 3(k+2)/4.
    """

    def test_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        self.assertEqual(kappa_km('sl2', Fraction(1)), Fraction(9, 4))

    def test_sl2_k2(self):
        """kappa(sl_2, k=2) = 3*4/4 = 3."""
        self.assertEqual(kappa_km('sl2', Fraction(2)), Fraction(3))

    def test_sl2_k_generic(self):
        """kappa(sl_2, k) = 3(k+2)/4 for k = 1..10."""
        for k in range(1, 11):
            expected = Fraction(3 * (k + 2), 4)
            self.assertEqual(kappa_km('sl2', Fraction(k)), expected,
                             f"kappa(sl_2, k={k}) wrong")

    def test_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*4/6 = 16/3."""
        # dim(sl_3) = 8, h^v = 3; kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        self.assertEqual(kappa_km('sl3', Fraction(1)), Fraction(16, 3))

    def test_sl3_k_generic(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        for k in range(1, 6):
            expected = Fraction(4 * (k + 3), 3)
            self.assertEqual(kappa_km('sl3', Fraction(k)), expected)

    def test_general_formula(self):
        """kappa = dim(g)*(k+h^v)/(2*h^v) for all available Lie algebras."""
        test_cases = {
            'sl2': (3, 2),
            'sl3': (8, 3),
            'g2': (14, 4),
            'so5': (10, 3),
        }
        k = Fraction(1)
        for name, (dim_g, h_dual) in test_cases.items():
            expected = Fraction(dim_g * (k + h_dual), 2 * h_dual)
            self.assertEqual(kappa_km(name, k), expected,
                             f"kappa({name}, k={k}) wrong")


class TestUniversalFreeEnergy(unittest.TestCase):
    """Verify F_g = kappa * lambda_g^FP for g=1..5.

    lambda_1^FP = 1/24
    lambda_2^FP = 7/5760
    lambda_3^FP = 31/967680
    """

    def test_f1(self):
        """F_1 = kappa/24."""
        kappa = Fraction(1)
        self.assertEqual(free_energy_universal(kappa, 1), Fraction(1, 24))

    def test_f2(self):
        """F_2 = 7*kappa/5760."""
        kappa = Fraction(1)
        self.assertEqual(free_energy_universal(kappa, 2), Fraction(7, 5760))

    def test_f3(self):
        """F_3 = 31*kappa/967680."""
        kappa = Fraction(1)
        self.assertEqual(free_energy_universal(kappa, 3), Fraction(31, 967680))

    def test_lambda_fp_values(self):
        """Verify lambda_g^FP for g=1..5 against known values."""
        known = {
            1: Fraction(1, 24),
            2: Fraction(7, 5760),
            3: Fraction(31, 967680),
        }
        for g, expected in known.items():
            self.assertEqual(_lambda_fp_exact(g), expected,
                             f"lambda_{g}^FP wrong")

    def test_linearity_in_kappa(self):
        """F_g(a*kappa) = a * F_g(kappa)."""
        for g in range(1, 6):
            for a in [2, 3, Fraction(1, 2), Fraction(5, 7)]:
                kappa = Fraction(3)
                self.assertEqual(
                    free_energy_universal(a * kappa, g),
                    a * free_energy_universal(kappa, g),
                    f"Linearity fails at g={g}, a={a}")

    def test_f1_virasoro(self):
        """F_1(Vir_c) = c/48 (the canonical test value)."""
        for c_val in [1, 2, 26]:
            c = Fraction(c_val)
            kappa = kappa_virasoro(c)
            self.assertEqual(free_energy_universal(kappa, 1),
                             c / 48,
                             f"F_1(Vir_{c}) wrong")

    def test_f1_w3(self):
        """F_1(W_3, c) = 5c/144."""
        for c_val in [1, 6, 12]:
            c = Fraction(c_val)
            kappa = kappa_w_n(c, 3)
            self.assertEqual(free_energy_universal(kappa, 1),
                             5 * c / 144,
                             f"F_1(W_3, c={c}) wrong")

    def test_f1_heisenberg(self):
        """F_1(H_k) = k/24."""
        for k in [1, 2, 3]:
            kappa = kappa_heisenberg(Fraction(k))
            self.assertEqual(free_energy_universal(kappa, 1),
                             Fraction(k, 24))

    def test_positivity(self):
        """F_g > 0 for kappa > 0 and all g >= 1."""
        kappa = Fraction(1)
        for g in range(1, 6):
            self.assertGreater(free_energy_universal(kappa, g), 0)


class TestPerChannelCorrect(unittest.TestCase):
    """Verify that the correct per-channel formula sums to kappa * lambda_g^FP.

    This is an algebraic identity: since every channel uses E_1,
    F_g = (sum kappa_i) * lambda_g^FP = kappa * lambda_g^FP.
    """

    def test_w3_channels_sum(self):
        """W_3 channels [c/2, c/3] sum to 5c/6 * lambda_g^FP."""
        c = Fraction(6)
        kappa_list = [c / 2, c / 3]
        total_kappa = kappa_w_n(c, 3)
        for g in range(1, 4):
            self.assertEqual(
                free_energy_per_channel_correct(kappa_list, g),
                free_energy_universal(total_kappa, g),
                f"Per-channel sum disagrees at g={g}")

    def test_w4_channels_sum(self):
        """W_4 channels [c/2, c/3, c/4] sum correctly."""
        c = Fraction(12)
        kappa_list = [c / 2, c / 3, c / 4]
        total_kappa = kappa_w_n(c, 4)
        for g in range(1, 4):
            self.assertEqual(
                free_energy_per_channel_correct(kappa_list, g),
                free_energy_universal(total_kappa, g))

    def test_single_channel_agrees(self):
        """Single channel [kappa] = kappa * lambda_g^FP."""
        kappa = Fraction(7, 3)
        for g in range(1, 4):
            self.assertEqual(
                free_energy_per_channel_correct([kappa], g),
                free_energy_universal(kappa, g))


class TestPerChannelWrongDisagreesAtGenus2(unittest.TestCase):
    """Verify the wrong E_h formula gives different F_2 for W_3.

    At genus 1, the wrong formula gives 113/5 times the correct value.
    The wrong formula also disagrees at genus 2 (and all higher genera).
    """

    def test_wrong_disagrees_genus1_w3(self):
        """Wrong E_h formula disagrees with correct at genus 1 for W_3."""
        c = Fraction(6)
        kappa_list = [c / 2, c / 3]
        weight_list = [2, 3]
        correct = free_energy_per_channel_correct(kappa_list, 1)
        wrong = free_energy_per_channel_wrong(kappa_list, weight_list, 1)
        self.assertNotEqual(correct, wrong)
        self.assertEqual(wrong / correct, Fraction(113, 5))

    def test_wrong_disagrees_genus2_w3(self):
        """Wrong E_h formula disagrees with correct at genus 2 for W_3."""
        c = Fraction(6)
        kappa_list = [c / 2, c / 3]
        weight_list = [2, 3]
        correct = free_energy_per_channel_correct(kappa_list, 2)
        wrong = free_energy_per_channel_wrong(kappa_list, weight_list, 2)
        self.assertNotEqual(correct, wrong)

    def test_wrong_agrees_for_heisenberg(self):
        """Wrong E_h formula AGREES with correct for Heisenberg (weight 1 -> E_1).

        Since the Heisenberg generator has weight 1 and E_1 has Mumford exponent 1,
        the wrong formula coincidentally gives the correct answer.
        """
        kappa = Fraction(1)
        for g in range(1, 4):
            correct = free_energy_per_channel_correct([kappa], g)
            wrong = free_energy_per_channel_wrong([kappa], [1], g)
            self.assertEqual(correct, wrong,
                             f"Should agree for weight-1 at g={g}")

    def test_wrong_disagrees_for_virasoro(self):
        """Wrong E_h formula disagrees for Virasoro (weight 2 != weight 1)."""
        c = Fraction(26)
        kappa = kappa_virasoro(c)
        correct = free_energy_per_channel_correct([kappa], 1)
        wrong = free_energy_per_channel_wrong([kappa], [2], 1)
        self.assertNotEqual(correct, wrong)
        self.assertEqual(wrong / correct, Fraction(13))


class TestLandscapeCensusConsistency(unittest.TestCase):
    """Cross-check kappa values against the landscape census table.

    The canonical values from landscape_census.tex:
        Heisenberg (d bosons): kappa = d
        sl_2 at level k:       kappa = 3(k+2)/4
        beta-gamma (lambda=1): kappa = 1
        Virasoro:              kappa = c/2
        W_3:                   kappa = 5c/6
    """

    def test_heisenberg_census(self):
        """Heisenberg: kappa = d (rank d at level 1)."""
        for d in range(1, 5):
            self.assertEqual(kappa_heisenberg(Fraction(1), d), Fraction(d))

    def test_sl2_census(self):
        """sl_2 at level k: kappa = 3(k+2)/4."""
        for k in range(1, 6):
            expected = Fraction(3 * (k + 2), 4)
            self.assertEqual(kappa_km('sl2', Fraction(k)), expected)

    def test_betagamma_census(self):
        """beta-gamma: kappa = 1, c = 2, rho = 1/2."""
        self.assertEqual(kappa_betagamma(), Fraction(1))

    def test_virasoro_census(self):
        """Virasoro: kappa = c/2, rho = 1/2."""
        for c_val in [1, Fraction(1, 2), 26, Fraction(-22, 5)]:
            c = Fraction(c_val)
            self.assertEqual(kappa_virasoro(c), c / 2)

    def test_w3_census(self):
        """W_3: kappa = 5c/6, rho = 5/6."""
        for c_val in [1, 6, Fraction(4, 5)]:
            c = Fraction(c_val)
            self.assertEqual(kappa_w_n(c, 3), 5 * c / 6)

    def test_anomaly_ratio_virasoro_census(self):
        """Virasoro anomaly ratio rho = 1/2."""
        self.assertEqual(anomaly_ratio_w_n(2), Fraction(1, 2))

    def test_anomaly_ratio_w3_census(self):
        """W_3 anomaly ratio rho = 5/6."""
        self.assertEqual(anomaly_ratio_w_n(3), Fraction(5, 6))

    def test_anomaly_ratio_w4_census(self):
        """W_4 anomaly ratio rho = 13/12."""
        self.assertEqual(anomaly_ratio_w_n(4), Fraction(13, 12))

    def test_f1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all standard families (landscape census identity)."""
        families = [
            ('heisenberg', {'k': 1, 'd': 1}),
            ('virasoro', {}),
            ('w3', {}),
            ('km', {'g_name': 'sl2', 'k': 1}),
        ]
        for algebra, kwargs in families:
            c = Fraction(6) if algebra in ('virasoro', 'w3') else Fraction(1)
            kappa = genus1_curvature_direct(algebra, c, **kwargs)
            f1 = free_energy_universal(kappa, 1)
            self.assertEqual(f1, kappa / 24,
                             f"F_1 != kappa/24 for {algebra}")

    def test_landscape_census_tex_kappa_values(self):
        """Cross-check against the landscape_census.tex table entries.

        From the table at line ~557:
            H_1^{d bosons}: c=d, kappa=d, rho=1
            sl_{2,k}: c=3k/(k+2), kappa=3(k+2)/4, rho=(k+2)^2/(4k)
            betagamma_{lambda=1}: c=2, kappa=1, rho=1/2
            Vir_c: c=c, kappa=c/2, rho=1/2
            W_{3,c}: c=c, kappa=5c/6, rho=5/6
        """
        # Heisenberg d=1
        self.assertEqual(kappa_heisenberg(Fraction(1), 1), Fraction(1))

        # sl_2 at k=1: c = 3*1/(1+2) = 1, kappa = 3*3/4 = 9/4
        c_sl2 = Fraction(3, 3)  # = 1
        kappa_sl2 = kappa_km('sl2', Fraction(1))
        self.assertEqual(kappa_sl2, Fraction(9, 4))
        rho_sl2 = kappa_sl2 / c_sl2
        self.assertEqual(rho_sl2, Fraction(9, 4))

        # betagamma
        self.assertEqual(kappa_betagamma(), Fraction(1))

        # Virasoro at c=26
        self.assertEqual(kappa_virasoro(Fraction(26)), Fraction(13))

        # W_3 at c=6
        self.assertEqual(kappa_w_n(Fraction(6), 3), Fraction(5))


class TestAntiPattern27(unittest.TestCase):
    """AP27: field weight != propagator weight for all non-weight-1 families.

    The bar propagator d log E(z,w) is ALWAYS weight 1.  The conformal weight
    of the field is a property of the FIELD, not the PROPAGATOR.

    thm:w3-obstruction confuses these: it assigns weight-h fields to E_h,
    as if the propagator had weight h.  This is wrong.
    """

    def test_heisenberg_weight_equals_propagator(self):
        """Heisenberg: weight 1 = propagator weight 1 (coincidence)."""
        data = field_weight_vs_propagator_weight('heisenberg')
        self.assertEqual(data['propagator_weight'], 1)
        self.assertEqual(data['generator_weights'], [1])
        self.assertTrue(data['weight_equals_propagator'])

    def test_virasoro_weight_differs(self):
        """Virasoro: field weight 2 != propagator weight 1."""
        data = field_weight_vs_propagator_weight('virasoro')
        self.assertEqual(data['propagator_weight'], 1)
        self.assertEqual(data['generator_weights'], [2])
        self.assertFalse(data['weight_equals_propagator'])

    def test_w3_weight_differs(self):
        """W_3: field weights [2, 3] != propagator weight 1."""
        data = field_weight_vs_propagator_weight('w3')
        self.assertEqual(data['propagator_weight'], 1)
        self.assertEqual(data['generator_weights'], [2, 3])
        self.assertFalse(data['weight_equals_propagator'])

    def test_w4_weight_differs(self):
        """W_4: field weights [2, 3, 4] != propagator weight 1."""
        data = field_weight_vs_propagator_weight('w_n', N=4)
        self.assertEqual(data['propagator_weight'], 1)
        self.assertEqual(data['generator_weights'], [2, 3, 4])
        self.assertFalse(data['weight_equals_propagator'])

    def test_km_weight_equals_propagator(self):
        """KM: weight 1 = propagator weight 1 (coincidence)."""
        data = field_weight_vs_propagator_weight('km')
        self.assertEqual(data['propagator_weight'], 1)
        self.assertEqual(data['generator_weights'], [1])
        self.assertTrue(data['weight_equals_propagator'])

    def test_betagamma_weight_differs(self):
        """beta-gamma: generator weights [1, 0] include weight 0 != 1."""
        data = field_weight_vs_propagator_weight('betagamma')
        self.assertEqual(data['propagator_weight'], 1)
        self.assertFalse(data['weight_equals_propagator'])

    def test_fermion_weight_differs(self):
        """Fermion: weight 1/2 != propagator weight 1."""
        data = field_weight_vs_propagator_weight('fermion')
        self.assertEqual(data['propagator_weight'], 1)
        self.assertEqual(data['generator_weights'], [Fraction(1, 2)])
        self.assertFalse(data['weight_equals_propagator'])

    def test_propagator_always_weight_1(self):
        """Propagator weight is 1 for ALL algebras."""
        algebras = [
            ('heisenberg', {}),
            ('virasoro', {}),
            ('w3', {}),
            ('w_n', {'N': 5}),
            ('km', {}),
            ('betagamma', {}),
            ('fermion', {}),
        ]
        for algebra, kwargs in algebras:
            data = field_weight_vs_propagator_weight(algebra, **kwargs)
            self.assertEqual(data['propagator_weight'], 1,
                             f"Propagator weight != 1 for {algebra}")

    def test_wrong_formula_amplifies_for_high_weight(self):
        """Wrong E_h formula gives increasingly absurd ratios at higher weight.

        Weight-h with E_h has Mumford exponent 6h^2-6h+1, so the discrepancy
        grows quadratically.
        """
        for h in range(2, 8):
            ratio = mumford_exponent(h)
            self.assertGreater(ratio, 1,
                               f"Mumford exponent should be > 1 for h={h}")
            # The discrepancy grows as ~6h^2
            self.assertGreater(ratio, h,
                               f"Mumford exponent should exceed h for h={h}")


class TestE8AnomalyRatio(unittest.TestCase):
    """Verify the E_8 anomaly ratio from the landscape census.

    From landscape_census.tex (rem:e8-complementarity):
        rho(E_8) = 1/2 + 1/8 + 1/12 + 1/14 + 1/18 + 1/20 + 1/24 + 1/30 = 121/126.

    E_8 exponents: 1, 7, 11, 13, 17, 19, 23, 29.
    """

    def test_e8_anomaly_ratio(self):
        """rho(E_8) = 121/126."""
        rho = anomaly_ratio_lie('e8')
        self.assertEqual(rho, Fraction(121, 126))

    def test_e8_from_exponents(self):
        """Verify from E_8 exponents: m_i = 1,7,11,13,17,19,23,29."""
        exponents = [1, 7, 11, 13, 17, 19, 23, 29]
        rho = sum(Fraction(1, m + 1) for m in exponents)
        self.assertEqual(rho, Fraction(121, 126))

    def test_e8_kappa(self):
        """kappa(E_8, k) = c * 121/126 where c = 248*k/(k+30)."""
        k = Fraction(1)
        kappa = kappa_km('e8', k)
        # dim(E_8) = 248, h^v = 30
        # kappa = 248*(k+30)/(2*30) = 248*31/60
        expected = Fraction(248 * 31, 60)
        self.assertEqual(kappa, expected)


class TestHarmonicNumbers(unittest.TestCase):
    """Verify harmonic numbers H_N = 1 + 1/2 + ... + 1/N."""

    def test_h1(self):
        self.assertEqual(harmonic(1), Fraction(1))

    def test_h2(self):
        self.assertEqual(harmonic(2), Fraction(3, 2))

    def test_h3(self):
        self.assertEqual(harmonic(3), Fraction(11, 6))

    def test_h4(self):
        self.assertEqual(harmonic(4), Fraction(25, 12))

    def test_h5(self):
        self.assertEqual(harmonic(5), Fraction(137, 60))

    def test_h6(self):
        self.assertEqual(harmonic(6), Fraction(49, 20))


class TestWrongFormulaHeisenbergCoincidence(unittest.TestCase):
    """The wrong E_h formula coincidentally agrees for weight-1 algebras.

    For Heisenberg and KM (weight-1 generators), the Mumford exponent of E_1
    is 1, so the wrong formula gives the same answer.  This is the root cause
    of the error: thm:w3-obstruction was likely tested only against weight-1
    families where the bug is invisible.
    """

    def test_heisenberg_coincidence(self):
        """Wrong = correct for Heisenberg (weight 1)."""
        k = Fraction(3)
        correct = genus1_curvature_direct('heisenberg', k=k)
        wrong = genus1_curvature_wrong('heisenberg', k=k)
        self.assertEqual(correct, wrong)

    def test_km_would_coincide(self):
        """Wrong = correct for KM (weight 1) at genus 1.

        KM generators J^a have weight 1; mumford_exponent(1) = 1.
        """
        self.assertEqual(mumford_exponent(1), 1)

    def test_virasoro_does_not_coincide(self):
        """Wrong != correct for Virasoro (weight 2)."""
        c = Fraction(26)
        correct = genus1_curvature_direct('virasoro', c)
        wrong = genus1_curvature_wrong('virasoro', c)
        self.assertNotEqual(correct, wrong)
        self.assertEqual(wrong / correct, Fraction(13))


if __name__ == '__main__':
    unittest.main()
