r"""Tests for genus-3 free energy across the standard landscape.

Tests:
1. lambda_3^FP = 31/967680 from Bernoulli numbers
2. F_3 for all 10 families (exact rational arithmetic)
3. Manuscript cross-checks (eq:genus3-k1, comp:w3-genus-expansion)
4. Universal ratios F_3/F_1, F_3/F_2
5. Complementarity: F_3 + F_3' = 0 for KM/free fields
6. Complementarity: F_3 + F_3' = (kappa+kappa') * lambda_3^FP for W-algebras
7. Planted-forest correction: Heisenberg vanishing (class G)
8. Planted-forest correction: affine sl_2 (class L, S_4=S_5=0)
9. Planted-forest correction: Virasoro at multiple c values
10. Planted-forest correction: W_3 T-line
11. Generating function consistency
12. Kappa additivity for lattice VOAs
13. Bernoulli number verification
14. Genus-3 planted-forest: 11-term polynomial structure
"""

import unittest
from fractions import Fraction
from math import factorial

from compute.lib.genus3_landscape import (
    LAMBDA3_FP,
    F3,
    _bernoulli_exact,
    c_affine_sl2,
    c_affine_sl3,
    c_betagamma,
    c_w3,
    complementarity_check_F3,
    delta_pf_genus3_affine_sl2,
    delta_pf_genus3_formula,
    delta_pf_genus3_heisenberg,
    delta_pf_genus3_symbolic,
    delta_pf_genus3_virasoro,
    delta_pf_genus3_virasoro_symbolic,
    delta_pf_genus3_w3_Tline,
    genus3_landscape_table,
    genus3_ratio_table,
    kappa_affine_sl2,
    kappa_affine_sl3,
    kappa_betagamma,
    kappa_heisenberg,
    kappa_lattice,
    kappa_virasoro,
    kappa_w3,
    lambda_fp,
    verify_generating_function_consistency,
    verify_manuscript_sl2_genus3,
    verify_manuscript_w3_genus3,
    virasoro_shadow_values,
    w3_shadow_values,
)


# ====================================================================
# Section 1: Faber-Pandharipande numbers
# ====================================================================

class TestLambdaFP(unittest.TestCase):
    """Test lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda3_equals_constant(self):
        self.assertEqual(lambda_fp(3), LAMBDA3_FP)

    def test_lambda4(self):
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))

    def test_lambda5(self):
        """lambda_5^FP = 511 * |B_{10}| / (2^9 * 10!) = 511/24524881920."""
        # B_10 = 5/66
        # |B_10| = 5/66
        # (2^9-1)/2^9 = 511/512
        # 511/512 * (5/66) / 3628800 = 511*5 / (512*66*3628800)
        # = 2555 / 122268860160 -- let's just check the computation
        l5 = lambda_fp(5)
        self.assertEqual(l5.numerator, 73)
        self.assertEqual(l5.denominator, 3503554560)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive (Hodge index theorem)."""
        for g in range(1, 10):
            self.assertGreater(lambda_fp(g), 0)

    def test_lambda_decreasing(self):
        """lambda_{g+1}^FP < lambda_g^FP (geometric decay)."""
        for g in range(1, 8):
            self.assertLess(lambda_fp(g + 1), lambda_fp(g))


# ====================================================================
# Section 2: Bernoulli numbers
# ====================================================================

class TestBernoulli(unittest.TestCase):
    """Test exact Bernoulli numbers."""

    def test_B0(self):
        self.assertEqual(_bernoulli_exact(0), Fraction(1))

    def test_B1(self):
        self.assertEqual(_bernoulli_exact(1), Fraction(-1, 2))

    def test_B2(self):
        self.assertEqual(_bernoulli_exact(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(_bernoulli_exact(4), Fraction(-1, 30))

    def test_B6(self):
        self.assertEqual(_bernoulli_exact(6), Fraction(1, 42))

    def test_B8(self):
        self.assertEqual(_bernoulli_exact(8), Fraction(-1, 30))

    def test_B10(self):
        self.assertEqual(_bernoulli_exact(10), Fraction(5, 66))

    def test_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for k in range(1, 10):
            self.assertEqual(_bernoulli_exact(2 * k + 1), Fraction(0))


# ====================================================================
# Section 3: Kappa values
# ====================================================================

class TestKappaValues(unittest.TestCase):
    """Test kappa formulas for all families."""

    def test_heisenberg(self):
        self.assertEqual(kappa_heisenberg(1), Fraction(1))
        self.assertEqual(kappa_heisenberg(2), Fraction(2))

    def test_virasoro(self):
        self.assertEqual(kappa_virasoro(Fraction(25)), Fraction(25, 2))
        self.assertEqual(kappa_virasoro(Fraction(26)), Fraction(13))
        self.assertEqual(kappa_virasoro(Fraction(0)), Fraction(0))

    def test_affine_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        self.assertEqual(kappa_affine_sl2(1), Fraction(9, 4))
        self.assertEqual(kappa_affine_sl2(2), Fraction(3))
        # At critical k=-2: kappa = 0
        self.assertEqual(kappa_affine_sl2(-2), Fraction(0))

    def test_affine_sl3(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        self.assertEqual(kappa_affine_sl3(1), Fraction(16, 3))
        # At critical k=-3: kappa = 0
        self.assertEqual(kappa_affine_sl3(-3), Fraction(0))

    def test_w3(self):
        """kappa(W_3, c) = 5c/6."""
        self.assertEqual(kappa_w3(Fraction(2)), Fraction(5, 3))
        self.assertEqual(kappa_w3(Fraction(50)), Fraction(125, 3))
        self.assertEqual(kappa_w3(Fraction(100)), Fraction(250, 3))

    def test_betagamma(self):
        """kappa(beta-gamma, lambda) = 6*lambda^2 - 6*lambda + 1."""
        self.assertEqual(kappa_betagamma(1), Fraction(1))
        self.assertEqual(kappa_betagamma(0), Fraction(1))
        # At lambda=1/2: kappa = 6/4 - 3 + 1 = -1/2 (using Fraction)
        # But we take integer lambda here

    def test_lattice(self):
        """kappa(V_Lambda) = rank."""
        self.assertEqual(kappa_lattice(4), Fraction(4))
        self.assertEqual(kappa_lattice(8), Fraction(8))
        self.assertEqual(kappa_lattice(24), Fraction(24))

    def test_betagamma_c_relation(self):
        """kappa = c/2 for beta-gamma."""
        for lam in [0, 1, 2, 3]:
            c = c_betagamma(lam)
            self.assertEqual(kappa_betagamma(lam), c / 2)


# ====================================================================
# Section 4: F_3 values for 10 families
# ====================================================================

class TestF3Values(unittest.TestCase):
    """Test F_3 = kappa * 31/967680 for all 10 families."""

    def test_heisenberg_k1(self):
        """F_3(H_1) = 31/967680."""
        self.assertEqual(F3(kappa_heisenberg(1)), Fraction(31, 967680))

    def test_virasoro_c25(self):
        """F_3(Vir_25) = (25/2) * 31/967680 = 155/387072."""
        self.assertEqual(F3(kappa_virasoro(Fraction(25))), Fraction(155, 387072))

    def test_affine_sl2_k1(self):
        """F_3(sl_2, k=1) = 31/430080 (eq:genus3-k1)."""
        self.assertEqual(F3(kappa_affine_sl2(1)), Fraction(31, 430080))

    def test_affine_sl3_k1(self):
        """F_3(sl_3, k=1) = (16/3) * 31/967680."""
        expected = Fraction(16, 3) * Fraction(31, 967680)
        self.assertEqual(F3(kappa_affine_sl3(1)), expected)
        # Simplify: 16*31 / (3*967680) = 496/2903040 = 31/181440
        self.assertEqual(expected, Fraction(31, 181440))

    def test_w3_c2(self):
        """F_3(W_3, c=2) = (5/3) * 31/967680 = 155/2903040 = 31/580608."""
        expected = Fraction(5, 3) * Fraction(31, 967680)
        self.assertEqual(F3(kappa_w3(Fraction(2))), expected)
        self.assertEqual(expected, Fraction(31, 580608))

    def test_w3_c50_selfdual(self):
        """F_3(W_3, c=50) = (125/3) * 31/967680 = 775/580608."""
        expected = Fraction(125, 3) * Fraction(31, 967680)
        self.assertEqual(F3(kappa_w3(Fraction(50))), expected)
        # 125*31 / (3*967680) = 3875/2903040 = 775/580608
        self.assertEqual(expected, Fraction(775, 580608))

    def test_betagamma_lam1(self):
        """F_3(beta-gamma, lambda=1) = 1 * 31/967680 = 31/967680."""
        self.assertEqual(F3(kappa_betagamma(1)), Fraction(31, 967680))

    def test_D4_lattice(self):
        """F_3(D_4 lattice) = 4 * 31/967680 = 31/241920."""
        self.assertEqual(F3(kappa_lattice(4)), Fraction(31, 241920))

    def test_E8_lattice(self):
        """F_3(E_8 lattice) = 8 * 31/967680 = 31/120960."""
        self.assertEqual(F3(kappa_lattice(8)), Fraction(31, 120960))

    def test_Leech_lattice(self):
        """F_3(Leech lattice) = 24 * 31/967680 = 31/40320."""
        self.assertEqual(F3(kappa_lattice(24)), Fraction(31, 40320))

    def test_heisenberg_betagamma_coincidence(self):
        """H_1 and beta-gamma at lambda=1 have the same kappa (both = 1)."""
        self.assertEqual(F3(kappa_heisenberg(1)), F3(kappa_betagamma(1)))

    def test_Leech_F3_equals_31_over_40320(self):
        """F_3(Leech) = 31/40320. Note 40320 = 8!."""
        self.assertEqual(Fraction(31, 40320), F3(kappa_lattice(24)))
        self.assertEqual(40320, factorial(8))


# ====================================================================
# Section 5: Manuscript cross-checks
# ====================================================================

class TestManuscriptCrossChecks(unittest.TestCase):
    """Verify against explicit values stated in the manuscript."""

    def test_sl2_k1_genus3(self):
        """eq:genus3-k1: F_3(sl_2, k=1) = 31/430080."""
        self.assertTrue(verify_manuscript_sl2_genus3())

    def test_w3_k1_genus3(self):
        """comp:w3-genus-expansion: F_3(W_3, k=1) = -403/290304."""
        self.assertTrue(verify_manuscript_w3_genus3())

    def test_sl2_k1_genus3_direct(self):
        """Direct computation: 3(1+2)/4 * 31/967680 = 9/4 * 31/967680."""
        kappa = Fraction(9, 4)
        f3 = kappa * LAMBDA3_FP
        self.assertEqual(f3, Fraction(31, 430080))
        # Verify: 9*31/(4*967680) = 279/3870720
        # GCD(279,3870720): 279 = 9*31, 3870720 = 4*967680
        # 279/3870720 = 31/430080 (dividing by 9: 3870720/9 = 430080)
        self.assertEqual(Fraction(279, 3870720), Fraction(31, 430080))

    def test_w3_k1_c_value(self):
        """Verify c(W_3, k=1) = -52."""
        c = c_w3(1)
        self.assertEqual(c, Fraction(-52))

    def test_w3_k1_kappa_value(self):
        """Verify kappa(W_3, k=1) = 5*(-52)/6 = -130/3."""
        kappa = kappa_w3(c_w3(1))
        self.assertEqual(kappa, Fraction(-130, 3))

    def test_w3_k1_F3_chain(self):
        """Verify the full chain: c=-52, kappa=-130/3, F_3=-403/290304."""
        c = c_w3(1)
        self.assertEqual(c, Fraction(-52))
        kappa = kappa_w3(c)
        self.assertEqual(kappa, Fraction(-130, 3))
        f3 = F3(kappa)
        # -130/3 * 31/967680 = -130*31/(3*967680) = -4030/2903040
        # = -403/290304 (dividing by 10)
        self.assertEqual(f3, Fraction(-403, 290304))

    def test_sl2_genus3_formula(self):
        """Verify F_3(sl_2, k) = 3(k+2)/4 * 31/967680 = 31(k+2)/1290240."""
        for k in [1, 2, 3, 5, 10]:
            kappa = kappa_affine_sl2(k)
            f3 = F3(kappa)
            expected = Fraction(31 * (k + 2), 1290240)
            self.assertEqual(f3, expected,
                             f"Failed at k={k}: {f3} != {expected}")


# ====================================================================
# Section 6: Complementarity
# ====================================================================

class TestComplementarity(unittest.TestCase):
    """Test F_3 complementarity: F_3(A) + F_3(A^!) relations."""

    def test_heisenberg_antisymmetry(self):
        """For Heisenberg: kappa' = -kappa, so F_3 + F_3' = 0."""
        for k in [1, 2, 5]:
            kA = kappa_heisenberg(k)
            kA_dual = -kA
            result = complementarity_check_F3('Heisenberg', kA, kA_dual)
            self.assertEqual(result['sum'], Fraction(0))
            self.assertEqual(result['kappa_sum'], Fraction(0))

    def test_affine_sl2_antisymmetry(self):
        """For affine sl_2: kappa + kappa' = 0 (Feigin-Frenkel: k -> -k-2h^v)."""
        for k in [1, 2, 3]:
            kA = kappa_affine_sl2(k)
            # Dual: k' = -k - 2*2 = -k - 4
            k_dual = -k - 4
            kA_dual = kappa_affine_sl2(k_dual)
            result = complementarity_check_F3('Affine_sl2', kA, kA_dual)
            self.assertEqual(result['kappa_sum'], Fraction(0),
                             f"Failed at k={k}: kappa+kappa'={result['kappa_sum']}")
            self.assertEqual(result['sum'], Fraction(0))

    def test_virasoro_nonzero_sum(self):
        """For Virasoro: kappa + kappa' = 13 (not 0). AP24."""
        kA = kappa_virasoro(Fraction(25))
        kA_dual = kappa_virasoro(Fraction(1))  # c' = 26 - 25 = 1
        result = complementarity_check_F3('Virasoro', kA, kA_dual)
        self.assertEqual(result['kappa_sum'], Fraction(13))
        self.assertEqual(result['sum'], Fraction(13) * LAMBDA3_FP)

    def test_virasoro_selfdual(self):
        """At c=13 (self-dual): kappa = kappa' = 13/2, sum = 13."""
        kA = kappa_virasoro(Fraction(13))
        result = complementarity_check_F3('Virasoro_sd', kA, kA)
        self.assertEqual(result['kappa_sum'], Fraction(13))

    def test_w3_nonzero_sum(self):
        """For W_3: kappa + kappa' = 250/3 (c+c'=100, kappa=5c/6)."""
        c_val = Fraction(2)
        c_dual = Fraction(98)  # c' = 100 - c
        kA = kappa_w3(c_val)
        kA_dual = kappa_w3(c_dual)
        result = complementarity_check_F3('W3', kA, kA_dual)
        self.assertEqual(result['kappa_sum'], Fraction(250, 3))

    def test_betagamma_antisymmetry(self):
        """For beta-gamma: kappa + kappa(bc) = 0."""
        kA = kappa_betagamma(1)
        kA_dual = -kA  # bc has kappa = -kappa(beta-gamma)
        result = complementarity_check_F3('BetaGamma', kA, kA_dual)
        self.assertEqual(result['sum'], Fraction(0))

    def test_lattice_antisymmetry(self):
        """For lattice VOA: kappa + kappa' = 0."""
        for d in [4, 8, 24]:
            kA = kappa_lattice(d)
            kA_dual = -kA
            result = complementarity_check_F3(f'Lattice_d{d}', kA, kA_dual)
            self.assertEqual(result['sum'], Fraction(0))


# ====================================================================
# Section 7: Universal ratios
# ====================================================================

class TestUniversalRatios(unittest.TestCase):
    """Test that F_g/F_h ratios are algebra-independent on the scalar lane."""

    def test_F3_over_F1(self):
        """F_3/F_1 = lambda_3/lambda_1 = (31/967680)/(1/24) = 31/40320."""
        ratios = genus3_ratio_table()
        self.assertEqual(ratios['F3_over_F1'], Fraction(31, 40320))

    def test_F3_over_F2(self):
        """F_3/F_2 = (31/967680)/(7/5760) = 31*5760/(7*967680) = 31/1176."""
        ratios = genus3_ratio_table()
        self.assertEqual(ratios['F3_over_F2'], Fraction(31, 1176))

    def test_F2_over_F1(self):
        """F_2/F_1 = 7/240 (universal)."""
        ratios = genus3_ratio_table()
        self.assertEqual(ratios['F2_over_F1'], Fraction(7, 240))

    def test_ratio_universality(self):
        """Verify ratios are the same for different algebras."""
        table = genus3_landscape_table()
        r = Fraction(31, 40320)
        for name, data in table.items():
            kappa = data['kappa']
            if kappa == 0:
                continue
            f3 = data['F3']
            f1 = kappa * lambda_fp(1)
            self.assertEqual(f3 / f1, r,
                             f"Ratio F_3/F_1 not universal for {name}")

    def test_40320_is_8_factorial(self):
        """Verify 40320 = 8!."""
        self.assertEqual(factorial(8), 40320)


# ====================================================================
# Section 8: Planted-forest correction: class G (Heisenberg)
# ====================================================================

class TestPlantedForestHeisenberg(unittest.TestCase):
    """Test delta_pf^{(3,0)} = 0 for class G (Heisenberg)."""

    def test_vanishes(self):
        """Heisenberg has S_3 = S_4 = S_5 = 0, so delta_pf = 0."""
        self.assertEqual(delta_pf_genus3_heisenberg(), Fraction(0))

    def test_all_terms_vanish_individually(self):
        """Each of the 11 terms has at least one factor S_3, S_4, or S_5."""
        # With S_3 = S_4 = S_5 = 0, every term vanishes
        k = Fraction(1)
        self.assertEqual(
            delta_pf_genus3_formula(k, Fraction(0), Fraction(0), Fraction(0)),
            Fraction(0)
        )

    def test_any_kappa(self):
        """Vanishing holds for any kappa value (class G property)."""
        for k in [Fraction(1), Fraction(5), Fraction(-3), Fraction(100)]:
            self.assertEqual(
                delta_pf_genus3_formula(k, Fraction(0), Fraction(0), Fraction(0)),
                Fraction(0)
            )


# ====================================================================
# Section 9: Planted-forest correction: class L (affine sl_2)
# ====================================================================

class TestPlantedForestAffine(unittest.TestCase):
    """Test delta_pf^{(3,0)} for class L (S_3 != 0, S_4 = S_5 = 0)."""

    def test_nonzero(self):
        """Affine sl_2 (class L) has nonzero planted-forest correction."""
        dpf = delta_pf_genus3_affine_sl2(1)
        self.assertNotEqual(dpf, Fraction(0))

    def test_S4_S5_zero_terms_vanish(self):
        """With S_4 = S_5 = 0, only S_3-dependent terms survive."""
        kappa = Fraction(9, 4)
        S3 = Fraction(2)
        # All S_4 and S_5 terms should vanish
        dpf = delta_pf_genus3_formula(kappa, S3, Fraction(0), Fraction(0))
        # The surviving terms are:
        # 3/512 S_3^3 kappa - 5/128 S_3^4 - 343/2304 S_3 kappa
        # - 1/4608 S_3^2 kappa^2 - 1/82944 S_3 kappa^3
        t1 = Fraction(3, 512) * S3**3 * kappa
        t2 = -Fraction(5, 128) * S3**4
        t3 = -Fraction(343, 2304) * S3 * kappa
        t4 = -Fraction(1, 4608) * S3**2 * kappa**2
        t5 = -Fraction(1, 82944) * S3 * kappa**3
        expected = t1 + t2 + t3 + t4 + t5
        self.assertEqual(dpf, expected)

    def test_affine_sl2_k1_exact(self):
        """Compute delta_pf for affine sl_2 at k=1 exactly."""
        dpf = delta_pf_genus3_affine_sl2(1)
        # kappa = 9/4, S_3 = 2
        k = Fraction(9, 4)
        S3 = Fraction(2)
        # 3/512 * 8 * 9/4 = 3*8*9/(512*4) = 216/2048 = 27/256
        t1 = Fraction(3, 512) * 8 * k
        self.assertEqual(t1, Fraction(27, 256))
        # -5/128 * 16 = -80/128 = -5/8
        t2 = -Fraction(5, 128) * 16
        self.assertEqual(t2, Fraction(-5, 8))
        # -343/2304 * 2 * 9/4 = -343*18/(2304*4) = -6174/9216 = -343/512
        t3 = -Fraction(343, 2304) * 2 * k
        self.assertEqual(t3, Fraction(-343, 512))
        # -1/4608 * 4 * 81/16 = -324/(4608*16) = -324/73728 = -9/2048
        t4 = -Fraction(1, 4608) * 4 * k**2
        self.assertEqual(t4, Fraction(-9, 2048))
        # -1/82944 * 2 * 729/64 = -1458/(82944*64) = -1458/5308416
        t5 = -Fraction(1, 82944) * 2 * k**3
        expected = t1 + t2 + t3 + t4 + t5
        self.assertEqual(dpf, expected)


# ====================================================================
# Section 10: Planted-forest correction: class M (Virasoro)
# ====================================================================

class TestPlantedForestVirasoro(unittest.TestCase):
    """Test delta_pf^{(3,0)} for Virasoro (class M, infinite tower)."""

    def test_shadow_values_c25(self):
        """Verify Virasoro shadow data at c=25."""
        sd = virasoro_shadow_values(Fraction(25))
        self.assertEqual(sd['kappa'], Fraction(25, 2))
        self.assertEqual(sd['S3'], Fraction(2))
        # S_4 = 10/(25*(5*25+22)) = 10/(25*147) = 10/3675 = 2/735
        self.assertEqual(sd['S4'], Fraction(2, 735))
        # S_5 = -48/(25^2*(5*25+22)) = -48/(625*147) = -48/91875
        self.assertEqual(sd['S5'], Fraction(-48, 91875))

    def test_shadow_values_c1(self):
        """Verify Virasoro shadow data at c=1."""
        sd = virasoro_shadow_values(Fraction(1))
        self.assertEqual(sd['kappa'], Fraction(1, 2))
        self.assertEqual(sd['S3'], Fraction(2))
        # S_4 = 10/(1*(5+22)) = 10/27
        self.assertEqual(sd['S4'], Fraction(10, 27))
        # S_5 = -48/(1*(5+22)) = -48/27 = -16/9
        self.assertEqual(sd['S5'], Fraction(-16, 9))

    def test_nonzero_at_generic_c(self):
        """Virasoro has nonzero planted-forest correction."""
        for c in [1, 2, 10, 25]:
            dpf = delta_pf_genus3_virasoro(Fraction(c))
            self.assertNotEqual(dpf, Fraction(0), f"Unexpected zero at c={c}")

    def test_c13_self_dual(self):
        """At c=13 (self-dual): planted-forest correction is finite and nonzero."""
        dpf = delta_pf_genus3_virasoro(Fraction(13))
        self.assertNotEqual(dpf, Fraction(0))

    def test_virasoro_symbolic_matches_numerical(self):
        """Symbolic and numerical evaluations should agree."""
        from sympy import Symbol, Rational as R
        expr = delta_pf_genus3_virasoro_symbolic()
        c = Symbol('c')
        for c_val in [1, 2, 5, 13, 25]:
            symbolic = float(expr.subs(c, c_val))
            numerical = float(delta_pf_genus3_virasoro(Fraction(c_val)))
            self.assertAlmostEqual(symbolic, numerical, places=10,
                                   msg=f"Mismatch at c={c_val}")


# ====================================================================
# Section 11: Planted-forest correction: W_3 T-line
# ====================================================================

class TestPlantedForestW3(unittest.TestCase):
    """Test delta_pf^{(3,0)} for W_3 on the T-line."""

    def test_w3_Tline_equals_virasoro(self):
        """On the T-line, W_3 planted-forest = Virasoro planted-forest."""
        for c_val in [2, 50, 98]:
            dpf_w3 = delta_pf_genus3_w3_Tline(Fraction(c_val))
            dpf_vir = delta_pf_genus3_virasoro(Fraction(c_val))
            self.assertEqual(dpf_w3, dpf_vir,
                             f"Mismatch at c={c_val}")

    def test_w3_shadow_equals_virasoro_shadow(self):
        """W_3 T-line shadow data = Virasoro shadow data."""
        for c_val in [2, 50]:
            w3sd = w3_shadow_values(Fraction(c_val))
            virsd = virasoro_shadow_values(Fraction(c_val))
            self.assertEqual(w3sd, virsd)


# ====================================================================
# Section 12: Genus-3 planted-forest symbolic structure
# ====================================================================

class TestPlantedForestSymbolic(unittest.TestCase):
    """Test the symbolic 11-term polynomial structure."""

    def test_symbolic_returns_polynomial(self):
        """The symbolic formula returns a polynomial in 4 variables."""
        expr, (kappa, S3, S4, S5) = delta_pf_genus3_symbolic()
        self.assertIn(kappa, expr.free_symbols)
        self.assertIn(S3, expr.free_symbols)
        self.assertIn(S4, expr.free_symbols)
        self.assertIn(S5, expr.free_symbols)

    def test_class_G_vanishing_symbolic(self):
        """Setting S_3=S_4=S_5=0 gives 0."""
        from sympy import Symbol
        expr, (kappa, S3, S4, S5) = delta_pf_genus3_symbolic()
        result = expr.subs([(S3, 0), (S4, 0), (S5, 0)])
        self.assertEqual(result, 0)

    def test_class_L_S4_S5_zero(self):
        """Setting S_4=S_5=0 retains S_3-dependent terms only."""
        from sympy import Symbol, cancel as sym_cancel
        expr, (kappa, S3, S4, S5) = delta_pf_genus3_symbolic()
        result = sym_cancel(expr.subs([(S4, 0), (S5, 0)]))
        # Should contain S_3 but not S_4 or S_5
        self.assertIn(S3, result.free_symbols)
        self.assertNotIn(S4, result.free_symbols)
        self.assertNotIn(S5, result.free_symbols)


# ====================================================================
# Section 13: Generating function consistency
# ====================================================================

class TestGeneratingFunction(unittest.TestCase):
    """Test GF consistency: sum lambda_g x^{2g} = (x/2)/sin(x/2) - 1."""

    def test_consistency_through_g5(self):
        self.assertTrue(verify_generating_function_consistency(Fraction(1), 5))

    def test_consistency_through_g8(self):
        self.assertTrue(verify_generating_function_consistency(Fraction(1), 8))


# ====================================================================
# Section 14: Kappa additivity
# ====================================================================

class TestKappaAdditivity(unittest.TestCase):
    """Test kappa additivity for tensor products (lattice VOAs)."""

    def test_lattice_is_rank_copies(self):
        """kappa(H_1^{tensor d}) = d * kappa(H_1) = d."""
        for d in [1, 4, 8, 16, 24]:
            self.assertEqual(kappa_lattice(d), d * kappa_heisenberg(1))

    def test_E8xE8_equals_16(self):
        """kappa(E_8 x E_8) = 16 (rank 16)."""
        self.assertEqual(kappa_lattice(16), Fraction(16))

    def test_F3_additivity(self):
        """F_3(A tensor B) = F_3(A) + F_3(B) for free-field tensor products."""
        # Leech = H_1^{24}: F_3(Leech) = 24 * F_3(H_1)
        self.assertEqual(
            F3(kappa_lattice(24)),
            24 * F3(kappa_heisenberg(1))
        )

    def test_D4_is_four_copies(self):
        """F_3(D_4) = 4 * F_3(H_1)."""
        self.assertEqual(F3(kappa_lattice(4)), 4 * F3(kappa_heisenberg(1)))


# ====================================================================
# Section 15: Central charge formulas
# ====================================================================

class TestCentralCharge(unittest.TestCase):
    """Test central charge formulas."""

    def test_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/3 = 1."""
        self.assertEqual(c_affine_sl2(1), Fraction(1))

    def test_sl2_k2(self):
        """c(sl_2, k=2) = 6/4 = 3/2."""
        self.assertEqual(c_affine_sl2(2), Fraction(3, 2))

    def test_sl3_k1(self):
        """c(sl_3, k=1) = 8/4 = 2."""
        self.assertEqual(c_affine_sl3(1), Fraction(2))

    def test_w3_k1(self):
        """c(W_3, k=1) = 2 - 24*9/4 = 2 - 54 = -52."""
        self.assertEqual(c_w3(1), Fraction(-52))

    def test_betagamma_lam1(self):
        """c(beta-gamma, lambda=1) = 12 - 12 + 2 = 2."""
        self.assertEqual(c_betagamma(1), Fraction(2))

    def test_betagamma_lam0(self):
        """c(beta-gamma, lambda=0) = 0 - 0 + 2 = 2."""
        self.assertEqual(c_betagamma(0), Fraction(2))


# ====================================================================
# Section 16: Edge cases and sign checks
# ====================================================================

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and sign behavior."""

    def test_F3_positive_for_positive_kappa(self):
        """F_3 > 0 when kappa > 0 (all lambda_g^FP > 0)."""
        for k in [Fraction(1), Fraction(1, 2), Fraction(100)]:
            self.assertGreater(F3(k), Fraction(0))

    def test_F3_negative_for_negative_kappa(self):
        """F_3 < 0 when kappa < 0."""
        for k in [Fraction(-1), Fraction(-10)]:
            self.assertLess(F3(k), Fraction(0))

    def test_F3_zero_for_zero_kappa(self):
        """F_3 = 0 when kappa = 0 (uncurved)."""
        self.assertEqual(F3(Fraction(0)), Fraction(0))

    def test_critical_level_sl2(self):
        """At critical level k=-h^v=-2: kappa=0, F_3=0."""
        kappa = kappa_affine_sl2(-2)
        self.assertEqual(kappa, Fraction(0))
        self.assertEqual(F3(kappa), Fraction(0))

    def test_critical_level_sl3(self):
        """At critical level k=-h^v=-3: kappa=0, F_3=0."""
        kappa = kappa_affine_sl3(-3)
        self.assertEqual(kappa, Fraction(0))
        self.assertEqual(F3(kappa), Fraction(0))

    def test_virasoro_c0(self):
        """At c=0: kappa=0, F_3=0 (uncurved bar complex)."""
        self.assertEqual(F3(kappa_virasoro(Fraction(0))), Fraction(0))


# ====================================================================
# Section 17: Planted-forest genus-2 cross-check
# ====================================================================

class TestPlantedForestGenus2CrossCheck(unittest.TestCase):
    """Cross-check genus-2 planted-forest formula delta_pf^{(2,0)}."""

    def test_genus2_virasoro(self):
        """delta_pf^{(2,0)}(Vir_c) = -(c-40)/48 (from manuscript)."""
        # delta_pf^{(2,0)} = S_3(10*S_3 - kappa) / 48
        # For Virasoro: S_3 = 2, kappa = c/2
        # = 2*(20 - c/2) / 48 = (40 - c) / 48 = -(c-40)/48
        for c_val in [1, 10, 13, 25, 40]:
            S3 = Fraction(2)
            kappa = Fraction(c_val, 2)
            dpf2 = S3 * (10 * S3 - kappa) / 48
            expected = -(Fraction(c_val) - 40) / 48
            self.assertEqual(dpf2, expected,
                             f"Failed at c={c_val}: {dpf2} != {expected}")

    def test_genus2_heisenberg(self):
        """delta_pf^{(2,0)}(Heisenberg) = 0 (S_3 = 0)."""
        S3 = Fraction(0)
        dpf2 = S3 * (10 * S3 - Fraction(1)) / 48
        self.assertEqual(dpf2, Fraction(0))


# ====================================================================
# Section 18: Full landscape table
# ====================================================================

class TestLandscapeTable(unittest.TestCase):
    """Test the full landscape table."""

    def test_table_has_10_entries(self):
        table = genus3_landscape_table()
        self.assertEqual(len(table), 10)

    def test_all_entries_have_required_keys(self):
        table = genus3_landscape_table()
        for name, data in table.items():
            self.assertIn('kappa', data)
            self.assertIn('F3', data)
            self.assertIn('c', data)
            self.assertIn('description', data)

    def test_F3_consistency(self):
        """Every F_3 in the table equals kappa * lambda_3^FP."""
        table = genus3_landscape_table()
        for name, data in table.items():
            expected = data['kappa'] * LAMBDA3_FP
            self.assertEqual(data['F3'], expected,
                             f"Inconsistency for {name}")


if __name__ == '__main__':
    unittest.main()
