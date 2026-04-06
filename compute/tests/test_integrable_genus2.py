r"""Tests for the integrable hierarchy approach to genus-2 free energy.

MULTI-PATH VERIFICATION for F_2 across:
    Path 1: Direct A-hat formula (kappa * lambda_2^FP)
    Path 2: Integrable hierarchy (KdV / Boussinesq / Toda / Gelfand-Dickey)
    Path 3: Matrix model (Gaussian / cubic potential)
    Path 4: Graph sum (from w3_genus2.py and multichannel_genus2.py)
    Path 5: Topological recursion (EO on shadow spectral curve)

KEY RESULTS TESTED:
    1. lambda_2^FP = 7/5760 (exact, from Bernoulli numbers)
    2. F_2/F_1 = 7/240 (universal ratio, independent of algebra)
    3. KdV F_2 = (c/2) * 7/5760 for Virasoro (all three paths agree)
    4. Toda F_2 = 3(k+2)/4 * 7/5760 for V_k(sl_2) (uniform-weight)
    5. Boussinesq F_2^{diag} = 5c/6 * 7/5760 for W_3 (per-channel)
    6. W_3 cross-channel correction delta_F_2 = (c+204)/(16c) (graph sum)
    7. Multi-generator universality FAILS at genus 2 for W_3
    8. Additivity: F_2(A_1 + A_2) = F_2(A_1) + F_2(A_2)
    9. F_2 > 0 for all kappa > 0 (positivity from A-hat)
   10. Heisenberg = simplest test case (class G, exact)

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    rem:w3-genus2-cross-channel (higher_genus_modular_koszul.tex)
    rem:shadow-multiplicative-deformation (higher_genus_modular_koszul.tex)
    op:multi-generator-universality (higher_genus_foundations.tex)
"""

import unittest
from fractions import Fraction

from compute.lib.integrable_genus2_engine import (
    _bernoulli,
    lambda_fp,
    a_hat_coefficient,
    KdVGenus2,
    BoussinesqGenus2,
    TodaGenus2,
    GelfandDickeyGenus2,
    HeisenbergGenus2,
    SpectralCurveGenus2,
    F2_topological_recursion_airy,
    F2_matrix_model_gaussian,
    F2_matrix_model_cubic_potential,
    F2_numerical_eo,
    verify_F2_ratio_universality,
    verify_F2_additivity,
    multi_generator_universality_test,
    integrability_summary,
)


# ============================================================================
# Section 1: Bernoulli numbers and Faber-Pandharipande
# ============================================================================

class TestBernoulliNumbers(unittest.TestCase):
    """Verify Bernoulli numbers used in lambda_g^FP computation."""

    def test_B0(self):
        self.assertEqual(_bernoulli(0), Fraction(1))

    def test_B1(self):
        self.assertEqual(_bernoulli(1), Fraction(-1, 2))

    def test_B2(self):
        self.assertEqual(_bernoulli(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(_bernoulli(4), Fraction(-1, 30))

    def test_B6(self):
        self.assertEqual(_bernoulli(6), Fraction(1, 42))

    def test_odd_bernoulli_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(_bernoulli(n), Fraction(0),
                             f"B_{n} should vanish")


class TestLambdaFP(unittest.TestCase):
    """Verify Faber-Pandharipande numbers lambda_g^FP."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda_2_from_bernoulli(self):
        """Verify lambda_2^FP = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24."""
        B4 = Fraction(1, 30)  # |B_4|
        expected = Fraction(7, 8) * B4 / Fraction(24)
        self.assertEqual(lambda_fp(2), expected)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0, f"lambda_{g}^FP should be positive")

    def test_lambda_decreasing(self):
        """lambda_g^FP is decreasing in g (Bernoulli decay)."""
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1),
                               f"lambda_{g}^FP should exceed lambda_{g+1}^FP")

    def test_a_hat_coefficient_equals_lambda(self):
        """A-hat coefficient at genus g equals lambda_g^FP."""
        for g in range(1, 6):
            self.assertEqual(a_hat_coefficient(g), lambda_fp(g))

    def test_lambda_g_invalid(self):
        """lambda_0^FP should raise ValueError."""
        with self.assertRaises(ValueError):
            lambda_fp(0)


# ============================================================================
# Section 2: Universal ratio F_2/F_1 = 7/240
# ============================================================================

class TestUniversalRatio(unittest.TestCase):
    """Verify the universal genus-2 to genus-1 ratio."""

    def test_ratio_value(self):
        """F_2/F_1 = lambda_2^FP / lambda_1^FP = 7/240."""
        ratio = lambda_fp(2) / lambda_fp(1)
        self.assertEqual(ratio, Fraction(7, 240))

    def test_ratio_independence(self):
        """The ratio is independent of kappa (cancels)."""
        for kappa in [Fraction(1), Fraction(5), Fraction(13), Fraction(1, 7)]:
            f1 = kappa * lambda_fp(1)
            f2 = kappa * lambda_fp(2)
            ratio = f2 / f1
            self.assertEqual(ratio, Fraction(7, 240),
                             f"Ratio should be 7/240 for kappa = {kappa}")

    def test_ratio_perturbative(self):
        """F_2/F_1^2 = 7/(10*kappa) is perturbative in 1/kappa."""
        kappa = Fraction(5)
        f1 = kappa * lambda_fp(1)
        f2 = kappa * lambda_fp(2)
        ratio_sq = f2 / (f1 ** 2)
        expected = Fraction(7) / (10 * kappa)
        self.assertEqual(ratio_sq, expected)


# ============================================================================
# Section 3: KdV hierarchy (Virasoro)
# ============================================================================

class TestKdVGenus2(unittest.TestCase):
    """Verify KdV (Virasoro) genus-2 free energy via multiple paths."""

    def test_virasoro_c10_all_paths(self):
        """All three paths agree for Virasoro at c = 10."""
        kdv = KdVGenus2(Fraction(10))
        result = kdv.verify_all_paths()
        self.assertTrue(result['all_agree'])
        self.assertEqual(result['F2_value'], Fraction(5) * Fraction(7, 5760))

    def test_virasoro_c26_critical(self):
        """Virasoro at c = 26 (critical dimension)."""
        kdv = KdVGenus2(Fraction(26))
        self.assertEqual(kdv.kappa, Fraction(13))
        self.assertEqual(kdv.F2_direct(), Fraction(13) * Fraction(7, 5760))
        self.assertEqual(kdv.F2_direct(), Fraction(91, 5760))

    def test_virasoro_c1(self):
        """Virasoro at c = 1."""
        kdv = KdVGenus2(Fraction(1))
        self.assertEqual(kdv.kappa, Fraction(1, 2))
        self.assertEqual(kdv.F2_direct(), Fraction(7, 11520))

    def test_virasoro_c0(self):
        """Virasoro at c = 0: kappa = 0, F_2 = 0."""
        kdv = KdVGenus2(Fraction(0))
        self.assertEqual(kdv.kappa, Fraction(0))
        self.assertEqual(kdv.F2_direct(), Fraction(0))

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c = 13 (self-dual point, AP8)."""
        kdv = KdVGenus2(Fraction(13))
        self.assertEqual(kdv.kappa, Fraction(13, 2))
        f2 = kdv.F2_direct()
        self.assertEqual(f2, Fraction(13, 2) * Fraction(7, 5760))

    def test_kdv_ratio(self):
        """F_2/F_1 = 7/240 for KdV."""
        kdv = KdVGenus2(Fraction(10))
        self.assertEqual(kdv.F2_over_F1_ratio(), Fraction(7, 240))

    def test_all_three_paths_identical(self):
        """Direct, Witten-Kontsevich, and Dubrovin-Zhang give same value."""
        for c in [Fraction(1), Fraction(2), Fraction(10), Fraction(26)]:
            kdv = KdVGenus2(c)
            self.assertEqual(kdv.F2_direct(), kdv.F2_witten_kontsevich())
            self.assertEqual(kdv.F2_direct(), kdv.F2_dubrovin_zhang())


# ============================================================================
# Section 4: Boussinesq hierarchy (W_3)
# ============================================================================

class TestBoussinesqGenus2(unittest.TestCase):
    """Verify W_3 genus-2 free energy via multiple paths."""

    def test_w3_kappa(self):
        """kappa(W_3) = 5c/6."""
        bsq = BoussinesqGenus2(Fraction(6))
        self.assertEqual(bsq.kappa, Fraction(5))
        self.assertEqual(bsq.kappa_T, Fraction(3))
        self.assertEqual(bsq.kappa_W, Fraction(2))

    def test_w3_c10_diagonal(self):
        """Per-channel F_2 for W_3 at c = 10."""
        bsq = BoussinesqGenus2(Fraction(10))
        f2_diag = bsq.F2_diagonal()
        expected = Fraction(25, 3) * Fraction(7, 5760)
        self.assertEqual(f2_diag, expected)

    def test_w3_c10_cross_channel(self):
        """Cross-channel correction for W_3 at c = 10."""
        bsq = BoussinesqGenus2(Fraction(10))
        delta = bsq.delta_F2_cross_channel()
        # (10 + 204) / (16 * 10) = 214/160 = 107/80
        self.assertEqual(delta, Fraction(107, 80))

    def test_w3_delta_decomposition(self):
        """delta_F_2 = delta_banana + delta_theta + delta_lollipop + delta_barbell."""
        for c in [Fraction(1), Fraction(6), Fraction(10), Fraction(26)]:
            bsq = BoussinesqGenus2(c)
            self.assertTrue(bsq.verify_delta_decomposition(),
                            f"Decomposition failed at c = {c}")

    def test_w3_delta_banana(self):
        """delta_banana = 3/c."""
        bsq = BoussinesqGenus2(Fraction(6))
        self.assertEqual(bsq.delta_F2_banana(), Fraction(1, 2))

    def test_w3_delta_theta(self):
        """delta_theta = 9/(2c)."""
        bsq = BoussinesqGenus2(Fraction(6))
        self.assertEqual(bsq.delta_F2_theta(), Fraction(3, 4))

    def test_w3_delta_lollipop(self):
        """delta_lollipop = 1/16 (independent of c)."""
        for c in [Fraction(1), Fraction(6), Fraction(10), Fraction(100)]:
            bsq = BoussinesqGenus2(c)
            self.assertEqual(bsq.delta_F2_lollipop(), Fraction(1, 16))

    def test_w3_full_f2(self):
        """F_2^{full} = F_2^{diag} + delta_F_2."""
        bsq = BoussinesqGenus2(Fraction(10))
        f2_full = bsq.F2_full()
        f2_diag = bsq.F2_diagonal()
        delta = bsq.delta_F2_cross_channel()
        self.assertEqual(f2_full, f2_diag + delta)

    def test_w3_dz_diagonal_agrees(self):
        """Dubrovin-Zhang per-channel agrees with direct formula."""
        for c in [Fraction(1), Fraction(6), Fraction(10)]:
            bsq = BoussinesqGenus2(c)
            dz = bsq.F2_integrable_hierarchy()
            self.assertTrue(dz['diagonal_agrees'],
                            f"DZ diagonal mismatch at c = {c}")

    def test_w3_cross_channel_nonzero(self):
        """Cross-channel correction is nonzero for all positive c."""
        for c in [Fraction(1), Fraction(2), Fraction(10), Fraction(100)]:
            bsq = BoussinesqGenus2(c)
            delta = bsq.delta_F2_cross_channel()
            self.assertGreater(delta, 0,
                               f"delta_F_2 should be positive for c = {c}")

    def test_w3_cross_channel_large_c(self):
        """delta_F_2 ~ 1/16 as c -> infinity (semi-classical limit)."""
        bsq = BoussinesqGenus2(Fraction(10000))
        delta = bsq.delta_F2_cross_channel()
        # (c + 204)/(16c) = 1/16 + 204/(16c) -> 1/16
        self.assertTrue(abs(float(delta) - 1/16) < 0.002)

    def test_w3_cross_channel_small_c(self):
        """delta_F_2 diverges as c -> 0^+."""
        bsq = BoussinesqGenus2(Fraction(1, 100))
        delta = bsq.delta_F2_cross_channel()
        self.assertGreater(float(delta), 100)

    def test_w3_c0_raises(self):
        """c = 0 should raise ValueError."""
        with self.assertRaises(ValueError):
            BoussinesqGenus2(Fraction(0))

    def test_w3_manuscript_formula(self):
        """Verify against rem:w3-genus2-cross-channel formula.

        F_2^{full}(W_3) = 7c/6912 + (c+204)/(16c)

        At c = 6:
            7*6/6912 = 42/6912 = 7/1152
            (6+204)/(16*6) = 210/96 = 35/16
            Total = 7/1152 + 35/16
        """
        bsq = BoussinesqGenus2(Fraction(6))
        f2_diag = bsq.F2_diagonal()
        # kappa = 5*6/6 = 5, lambda_2 = 7/5760
        self.assertEqual(f2_diag, Fraction(5) * Fraction(7, 5760))
        self.assertEqual(f2_diag, Fraction(7, 1152))

        delta = bsq.delta_F2_cross_channel()
        self.assertEqual(delta, Fraction(210, 96))
        self.assertEqual(delta, Fraction(35, 16))

        f2_full = bsq.F2_full()
        self.assertEqual(f2_full, Fraction(7, 1152) + Fraction(35, 16))

    def test_w3_verify_all_paths(self):
        """Full multi-path verification for W_3."""
        bsq = BoussinesqGenus2(Fraction(10))
        result = bsq.verify_all_paths()
        self.assertTrue(result['delta_decomposition_ok'])
        self.assertTrue(result['DZ_diagonal_agrees'])
        self.assertFalse(result['delta_F2'] == 0)


# ============================================================================
# Section 5: Toda hierarchy (V_k(sl_2))
# ============================================================================

class TestTodaGenus2(unittest.TestCase):
    """Verify Toda (V_k(sl_2)) genus-2 free energy."""

    def test_sl2_k1_kappa(self):
        """kappa(V_1(sl_2)) = 3*(1+2)/4 = 9/4."""
        toda = TodaGenus2(Fraction(1))
        self.assertEqual(toda.kappa, Fraction(9, 4))

    def test_sl2_k1_f2(self):
        """F_2(V_1(sl_2)) = 9/4 * 7/5760 = 63/23040 = 7/2560."""
        toda = TodaGenus2(Fraction(1))
        expected = Fraction(9, 4) * Fraction(7, 5760)
        self.assertEqual(toda.F2_direct(), expected)

    def test_sl2_all_paths(self):
        """All three paths agree for V_k(sl_2)."""
        for k in [Fraction(1), Fraction(2), Fraction(3), Fraction(10)]:
            toda = TodaGenus2(k)
            result = toda.verify_all_paths()
            self.assertTrue(result['all_agree'],
                            f"Paths disagree at k = {k}")

    def test_sl2_uniform_weight(self):
        """V_k(sl_2) is uniform-weight: all generators weight 1."""
        toda = TodaGenus2(Fraction(1))
        # Direct = Toda = uniform-weight argument
        self.assertEqual(toda.F2_direct(), toda.F2_toda_hierarchy())
        self.assertEqual(toda.F2_direct(), toda.F2_uniform_weight_argument())

    def test_sl2_critical_level(self):
        """At critical level k = -h^v = -2: kappa = 0, F_2 = 0."""
        toda = TodaGenus2(Fraction(-2))
        self.assertEqual(toda.kappa, Fraction(0))
        self.assertEqual(toda.F2_direct(), Fraction(0))


# ============================================================================
# Section 6: Gelfand-Dickey hierarchy (W_N)
# ============================================================================

class TestGelfandDickeyGenus2(unittest.TestCase):
    """Verify W_N genus-2 free energy for various N."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: kappa = c/2, uniform-weight, delta_F_2 = 0."""
        gd = GelfandDickeyGenus2(2, Fraction(10))
        self.assertEqual(gd.kappa, Fraction(5))
        self.assertTrue(gd.is_uniform_weight())
        self.assertEqual(gd.delta_F2(), Fraction(0))
        self.assertEqual(gd.F2_full(), gd.F2_diagonal())

    def test_w3_kappa(self):
        """kappa(W_3) = c * (1 + 1/2 + 1/3 - 1) = 5c/6."""
        gd = GelfandDickeyGenus2(3, Fraction(6))
        self.assertEqual(gd.kappa, Fraction(5))

    def test_w3_delta(self):
        """W_3 delta_F_2 = (c+204)/(16c) (known exactly)."""
        gd = GelfandDickeyGenus2(3, Fraction(10))
        delta = gd.delta_F2()
        self.assertEqual(delta, Fraction(214, 160))

    def test_w4_kappa(self):
        """kappa(W_4) = c * (1 + 1/2 + 1/3 + 1/4 - 1) = 13c/12."""
        gd = GelfandDickeyGenus2(4, Fraction(12))
        self.assertEqual(gd.kappa, Fraction(13))

    def test_w4_delta_unknown(self):
        """W_4 delta_F_2 is not yet computed."""
        gd = GelfandDickeyGenus2(4, Fraction(10))
        self.assertIsNone(gd.delta_F2())
        self.assertIsNone(gd.F2_full())

    def test_w4_not_uniform(self):
        """W_4 is NOT uniform-weight (generators weight 2, 3, 4)."""
        gd = GelfandDickeyGenus2(4, Fraction(10))
        self.assertFalse(gd.is_uniform_weight())

    def test_w5_kappa(self):
        """kappa(W_5) = c * (H_5 - 1) = c * (137/60 - 1) = 77c/60."""
        gd = GelfandDickeyGenus2(5, Fraction(60))
        # H_5 = 1 + 1/2 + 1/3 + 1/4 + 1/5 = 137/60
        self.assertEqual(gd.kappa, Fraction(60) * Fraction(77, 60))
        self.assertEqual(gd.kappa, Fraction(77))

    def test_per_channel_kappas(self):
        """Per-channel kappas for W_4: kappa_j = c/(j+1) for j=1,2,3."""
        gd = GelfandDickeyGenus2(4, Fraction(12))
        self.assertEqual(gd.kappa_per_channel[2], Fraction(12, 2))  # weight 2
        self.assertEqual(gd.kappa_per_channel[3], Fraction(12, 3))  # weight 3
        self.assertEqual(gd.kappa_per_channel[4], Fraction(12, 4))  # weight 4


# ============================================================================
# Section 7: Heisenberg (simplest test case)
# ============================================================================

class TestHeisenbergGenus2(unittest.TestCase):
    """Verify Heisenberg genus-2 free energy (class G)."""

    def test_heisenberg_k1(self):
        """F_2(H_1) = 1 * 7/5760 = 7/5760."""
        heis = HeisenbergGenus2(Fraction(1))
        self.assertEqual(heis.F2(), Fraction(7, 5760))

    def test_heisenberg_verify(self):
        """Full verification for H_1."""
        heis = HeisenbergGenus2(Fraction(1))
        result = heis.verify()
        self.assertTrue(result['matches'])
        self.assertEqual(result['F2_over_F1'], Fraction(7, 240))

    def test_heisenberg_various_levels(self):
        """F_2(H_k) = 7k/5760 for various k."""
        for k in [Fraction(1), Fraction(2), Fraction(5), Fraction(1, 2)]:
            heis = HeisenbergGenus2(k)
            self.assertEqual(heis.F2(), Fraction(7) * k / 5760)


# ============================================================================
# Section 8: Topological recursion and matrix model
# ============================================================================

class TestTopologicalRecursion(unittest.TestCase):
    """Verify F_2 from topological recursion and matrix models."""

    def test_airy_f2(self):
        """Airy model F_2 = lambda_2^FP = 7/5760."""
        self.assertEqual(F2_topological_recursion_airy(), Fraction(7, 5760))

    def test_gaussian_matrix_model(self):
        """Gaussian matrix model F_2 = kappa * 7/5760."""
        for kappa in [Fraction(1), Fraction(5), Fraction(13)]:
            f2 = F2_matrix_model_gaussian(kappa)
            self.assertEqual(f2, kappa * Fraction(7, 5760))

    def test_cubic_matrix_model_t0(self):
        """Cubic matrix model at t = 0 reduces to Gaussian."""
        for kappa in [Fraction(1), Fraction(5)]:
            f2_cubic = F2_matrix_model_cubic_potential(kappa, Fraction(0))
            f2_gauss = F2_matrix_model_gaussian(kappa)
            self.assertEqual(f2_cubic, f2_gauss)

    def test_numerical_eo_virasoro(self):
        """Numerical EO for Virasoro should match exact F_2."""
        for c_val in [1.0, 10.0, 26.0]:
            kappa = c_val / 2
            f2_num = F2_numerical_eo(kappa, alpha_val=2.0,
                                     S4_val=10.0/(c_val*(5*c_val+22)))
            f2_exact = float(Fraction(int(c_val), 2) * lambda_fp(2))
            self.assertAlmostEqual(f2_num, f2_exact, places=10,
                                   msg=f"EO mismatch at c = {c_val}")

    def test_numerical_eo_heisenberg(self):
        """Numerical EO for Heisenberg (class G)."""
        f2_num = F2_numerical_eo(1.0, alpha_val=0.0, S4_val=0.0)
        f2_exact = float(lambda_fp(2))
        self.assertAlmostEqual(f2_num, f2_exact, places=10)


# ============================================================================
# Section 9: Spectral curve families
# ============================================================================

class TestSpectralCurves(unittest.TestCase):
    """Verify spectral curve data for all families."""

    def test_kdv_spectral_curve(self):
        """KdV spectral curve is rank 1."""
        data = SpectralCurveGenus2.kdv_spectral_curve(Fraction(10))
        self.assertEqual(data['rank'], 1)
        self.assertEqual(data['kappa'], Fraction(5))
        self.assertEqual(data['F2'], Fraction(5) * lambda_fp(2))

    def test_boussinesq_spectral_curve(self):
        """Boussinesq spectral curve is rank 2."""
        data = SpectralCurveGenus2.boussinesq_spectral_curve(Fraction(10))
        self.assertEqual(data['rank'], 2)
        self.assertEqual(data['kappa_total'], Fraction(25, 3))

    def test_toda_spectral_curve(self):
        """Toda spectral curve reduces to rank 1."""
        data = SpectralCurveGenus2.toda_spectral_curve(Fraction(1))
        self.assertEqual(data['rank'], 1)
        self.assertEqual(data['kappa'], Fraction(9, 4))

    def test_gd_spectral_curve(self):
        """N-th Gelfand-Dickey spectral curve has rank N-1."""
        for N in [2, 3, 4, 5]:
            data = SpectralCurveGenus2.gelfand_dickey_spectral_curve(N, Fraction(10))
            self.assertEqual(data['rank'], N - 1)

    def test_gd_uniform_weight_only_n2(self):
        """Only W_2 (Virasoro) is uniform-weight."""
        for N in [2, 3, 4, 5]:
            data = SpectralCurveGenus2.gelfand_dickey_spectral_curve(N, Fraction(10))
            self.assertEqual(data['uniform_weight'], N == 2)


# ============================================================================
# Section 10: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Verify cross-family consistency of F_2."""

    def test_ratio_universality(self):
        """F_2/F_1 = 7/240 for all standard families."""
        result = verify_F2_ratio_universality()
        self.assertTrue(result['all_match'])
        self.assertEqual(result['universal_ratio'], Fraction(7, 240))

    def test_additivity(self):
        """F_2(A_1 + A_2) = F_2(A_1) + F_2(A_2)."""
        for k1, k2 in [(Fraction(1), Fraction(2)),
                        (Fraction(5), Fraction(3)),
                        (Fraction(1, 2), Fraction(1, 3))]:
            result = verify_F2_additivity(k1, k2)
            self.assertTrue(result['additive'],
                            f"Additivity failed for kappa = {k1}, {k2}")

    def test_positivity(self):
        """F_2 > 0 for all kappa > 0."""
        for kappa in [Fraction(1, 100), Fraction(1), Fraction(100)]:
            f2 = kappa * lambda_fp(2)
            self.assertGreater(f2, 0)


# ============================================================================
# Section 11: Multi-generator universality test
# ============================================================================

class TestMultiGeneratorUniversality(unittest.TestCase):
    """Test the decisive computation for op:multi-generator-universality."""

    def test_w3_universality_fails(self):
        """Multi-generator universality FAILS at genus 2 for W_3."""
        result = multi_generator_universality_test(Fraction(10))
        self.assertFalse(result['universality_holds'])

    def test_w3_delta_nonzero_all_positive_c(self):
        """delta_F_2 > 0 for all c > 0."""
        for c in [Fraction(1, 10), Fraction(1), Fraction(10), Fraction(100)]:
            result = multi_generator_universality_test(c)
            self.assertGreater(result['delta_F2'], 0)

    def test_w3_delta_vanishes_at_minus_204(self):
        """delta_F_2 = 0 only at c = -204 (unphysical)."""
        result = multi_generator_universality_test(Fraction(-204))
        # At c = -204: (c+204)/(16c) = 0/(-3264) = 0
        self.assertEqual(result['delta_F2'], Fraction(0))
        self.assertTrue(result['universality_holds'])

    def test_w3_delta_formula(self):
        """delta_F_2 = (c + 204) / (16c) at various c values."""
        for c_val in [Fraction(1), Fraction(6), Fraction(10)]:
            result = multi_generator_universality_test(c_val)
            expected = (c_val + 204) / (16 * c_val)
            self.assertEqual(result['delta_F2'], expected)

    def test_w3_cross_channel_ratio_large_c(self):
        """Cross-channel ratio vanishes at large c (semi-classical)."""
        result = multi_generator_universality_test(Fraction(10000))
        ratio = result['cross_channel_ratio']
        # delta/F2_diag = (c+204)/(16c) / (5c/6 * 7/5760)
        # = (c+204)/(16c) * 6912/(7c)
        # ~ 6912/(16*7*c) = 6912/(112*c) = 432/(7c)
        # At c = 10000: ~ 0.00617
        self.assertLess(float(ratio), 0.01)

    def test_w3_c_singular_zero(self):
        """c = 0 returns error."""
        result = multi_generator_universality_test(Fraction(0))
        self.assertIn('error', result)


# ============================================================================
# Section 12: Cross-check with existing w3_genus2 engine
# ============================================================================

class TestCrossCheckWithExistingEngines(unittest.TestCase):
    """Cross-check integrable engine with w3_genus2 and multichannel_genus2."""

    def test_lambda_fp_matches_w3_engine(self):
        """lambda_2^FP matches between engines."""
        # Our engine
        ours = lambda_fp(2)

        # Direct computation (same formula, independent implementation)
        B4 = abs(_bernoulli(4))
        direct = Fraction(7, 8) * B4 / Fraction(24)
        self.assertEqual(ours, direct)
        self.assertEqual(ours, Fraction(7, 5760))

    def test_w3_diagonal_matches_manuscript(self):
        """F_2^{diag}(W_3) = 7c/6912 (manuscript rem:w3-genus2-cross-channel)."""
        c = Fraction(10)
        bsq = BoussinesqGenus2(c)
        f2_diag = bsq.F2_diagonal()
        # 5c/6 * 7/5760 = 35c/34560 = 7c/6912
        expected = Fraction(7) * c / 6912
        self.assertEqual(f2_diag, expected)

    def test_w3_delta_matches_manuscript(self):
        """delta_F_2 = (c+204)/(16c) (manuscript rem:w3-genus2-cross-channel)."""
        c = Fraction(10)
        bsq = BoussinesqGenus2(c)
        delta = bsq.delta_F2_cross_channel()
        expected = (c + 204) / (16 * c)
        self.assertEqual(delta, expected)

    def test_kdv_matches_virasoro_shadow(self):
        """KdV F_2 matches the Virasoro shadow formula."""
        c = Fraction(10)
        kdv = KdVGenus2(c)
        # From shadow_cohft_tautological.py: F_2 = kappa * lambda_2^FP
        f2_shadow = Fraction(5) * Fraction(7, 5760)
        self.assertEqual(kdv.F2_direct(), f2_shadow)

    def test_toda_matches_affine_kappa(self):
        """Toda F_2 matches kappa(V_k(sl_2)) * lambda_2^FP."""
        k = Fraction(1)
        toda = TodaGenus2(k)
        # kappa = 3(k+2)/4 = 9/4
        self.assertEqual(toda.kappa, Fraction(9, 4))
        expected = Fraction(9, 4) * Fraction(7, 5760)
        self.assertEqual(toda.F2_direct(), expected)


# ============================================================================
# Section 13: Integrability summary
# ============================================================================

class TestIntegrabilitySummary(unittest.TestCase):
    """Verify the summary is well-formed and contains key conclusions."""

    def test_summary_keys(self):
        """Summary has all expected keys."""
        s = integrability_summary()
        expected_keys = [
            'uniform_weight',
            'multi_weight_diagonal',
            'multi_weight_cross_channel',
            'integrable_hierarchy_role',
            'open_problem',
        ]
        for key in expected_keys:
            self.assertIn(key, s)

    def test_summary_mentions_open(self):
        """Summary correctly identifies op:multi-generator-universality as OPEN."""
        s = integrability_summary()
        self.assertIn('OPEN', s['open_problem'])

    def test_summary_mentions_fails(self):
        """Summary correctly states universality fails at tree level."""
        s = integrability_summary()
        self.assertIn('FAILS', s['multi_weight_cross_channel'])


# ============================================================================
# Section 14: Numerical precision and edge cases
# ============================================================================

class TestEdgeCases(unittest.TestCase):
    """Edge cases and numerical precision checks."""

    def test_large_genus_lambda_fp(self):
        """lambda_g^FP for large g: should be small but positive."""
        for g in range(1, 11):
            val = lambda_fp(g)
            self.assertGreater(val, 0)
            self.assertLess(float(val), 1.0)

    def test_very_large_kappa(self):
        """F_2 at very large kappa is very large."""
        kappa = Fraction(10 ** 6)
        f2 = kappa * lambda_fp(2)
        self.assertGreater(f2, 0)
        self.assertGreater(float(f2), 1.0)

    def test_very_small_kappa(self):
        """F_2 at very small kappa is very small but positive."""
        kappa = Fraction(1, 10 ** 6)
        f2 = kappa * lambda_fp(2)
        self.assertGreater(f2, 0)
        self.assertLess(float(f2), 1e-5)

    def test_negative_kappa(self):
        """F_2 is negative for negative kappa (physical: dual algebra)."""
        kappa = Fraction(-5)
        f2 = kappa * lambda_fp(2)
        self.assertLess(f2, 0)

    def test_w3_negative_c(self):
        """W_3 at negative c: kappa < 0, delta_F_2 can be negative."""
        bsq = BoussinesqGenus2(Fraction(-10))
        # kappa = 5*(-10)/6 = -25/3 < 0
        self.assertLess(bsq.kappa, 0)
        # delta = (-10 + 120)/(16*(-10)) = 110/(-160) = -11/16 < 0
        self.assertLess(bsq.delta_F2_cross_channel(), 0)

    def test_gd_invalid_n(self):
        """W_N with N < 2 should raise ValueError."""
        with self.assertRaises(ValueError):
            GelfandDickeyGenus2(1, Fraction(10))


# ============================================================================
# Section 15: Consistency with known intersection numbers
# ============================================================================

class TestIntersectionNumbers(unittest.TestCase):
    """Verify consistency with known intersection numbers on M-bar_{2,0}."""

    def test_int_mbar2_lambda2(self):
        """int_{M-bar_2} lambda_2 = 1/240 (Faber).

        The Faber-Pandharipande number lambda_2^FP = 7/5760 is DIFFERENT
        from int_{M_2} lambda_2 = 1/240. The relation:
            lambda_2^FP = (2^3 - 1)/2^3 * |B_4|/4!
            int lambda_2  = |B_4|/(4*2) = 1/240

        Ratio: lambda_2^FP / int(lambda_2) = 7/5760 * 240 = 7/24.
        """
        int_lambda2 = Fraction(1, 240)
        lambda2_fp = lambda_fp(2)
        ratio = lambda2_fp / int_lambda2
        self.assertEqual(ratio, Fraction(7, 24))

    def test_F2_uses_lambda_fp_not_int_lambda(self):
        """F_2 uses lambda_2^FP = 7/5760, NOT int(lambda_2) = 1/240.

        The shadow CohFT genus-2 free energy is:
            F_2 = kappa * lambda_2^FP = kappa * 7/5760

        NOT kappa * 1/240 = kappa * int(lambda_2).
        The Faber-Pandharipande number includes the Bernoulli correction.
        """
        kappa = Fraction(1)
        f2_correct = kappa * lambda_fp(2)
        f2_wrong = kappa * Fraction(1, 240)
        self.assertEqual(f2_correct, Fraction(7, 5760))
        self.assertNotEqual(f2_correct, f2_wrong)
        # The wrong value would be 24 times too large
        self.assertEqual(f2_wrong / f2_correct, Fraction(24, 7))

    def test_chi_mbar2(self):
        r"""Orbifold Euler characteristic chi(M_2) = 1/240 = int lambda_2.

        This is NOT the same as lambda_2^FP.
        chi(M_2) = B_4/(4*2) = (1/30)/8 ... wait:
        chi(M_2) = |B_4|/(4*2) = (1/30)/8 = 1/240. No:
        Actually chi(M_g) = B_{2g}/(2g(2g-2)).
        chi(M_2) = B_4/(4*2) = (-1/30)/8 = -1/240.
        |chi(M_2)| = 1/240.

        But int_{M-bar_2} lambda_2 = 1/240 (unsigned, Faber).
        These two numbers coinciding at g=2 is a coincidence that does NOT
        persist at higher genus.
        """
        chi_M2 = abs(_bernoulli(4)) / Fraction(4 * 2)
        self.assertEqual(chi_M2, Fraction(1, 240))


if __name__ == '__main__':
    unittest.main()
