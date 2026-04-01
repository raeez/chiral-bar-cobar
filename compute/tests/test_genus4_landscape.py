r"""Tests for genus-4 free energy across the standard landscape.

Tests:
1. lambda_4^FP = 127/154828800 from Bernoulli numbers (3 tests)
2. Bernoulli B_8 = -1/30 verification (3 tests)
3. Kappa values for all families (8 tests)
4. F_4 for all 10 families (exact rational arithmetic) (11 tests)
5. Universal ratios F_4/F_1, F_4/F_2, F_4/F_3 (5 tests)
6. Complementarity: F_4 + F_4' = 0 for KM/free fields (4 tests)
7. Complementarity: F_4 + F_4' = 13*lambda_4 for Virasoro (AP24) (3 tests)
8. Generating function consistency (2 tests)
9. Kappa additivity for lattice VOAs (3 tests)
10. Cross-genus ratio universality (3 tests)
11. Sign and edge case checks (5 tests)
12. Manuscript cross-checks (3 tests)
13. Full landscape table structure (3 tests)
"""

import unittest
from fractions import Fraction
from math import factorial

from compute.lib.genus4_landscape import (
    LAMBDA4_FP,
    F4,
    _bernoulli_exact,
    c_affine_sl2,
    c_affine_sl3,
    c_betagamma,
    c_w3,
    complementarity_check_F4,
    genus4_landscape_table,
    genus4_ratio_table,
    kappa_affine_sl2,
    kappa_affine_sl3,
    kappa_betagamma,
    kappa_heisenberg,
    kappa_lattice,
    kappa_virasoro,
    kappa_w3,
    lambda_fp,
    verify_generating_function_consistency,
    verify_manuscript_sl2_genus4,
    verify_manuscript_w3_genus4,
)


# ====================================================================
# Section 1: Faber-Pandharipande numbers
# ====================================================================

class TestLambdaFP(unittest.TestCase):
    """Test lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda4_exact(self):
        """lambda_4^FP = 127/154828800.

        Derivation:
          B_8 = -1/30,  |B_8| = 1/30.
          (2^7 - 1)/2^7 = 127/128.
          8! = 40320.
          lambda_4 = (127/128) * (1/30) / 40320
                   = 127 / (128 * 30 * 40320)
                   = 127 / 154828800.
        """
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))

    def test_lambda4_equals_constant(self):
        """lambda_fp(4) should match the precomputed constant LAMBDA4_FP."""
        self.assertEqual(lambda_fp(4), LAMBDA4_FP)

    def test_lambda4_from_components(self):
        """Verify from components: prefactor * |B_8| / 8!."""
        prefactor = Fraction(127, 128)
        abs_B8 = Fraction(1, 30)
        fact8 = Fraction(40320)
        self.assertEqual(prefactor * abs_B8 / fact8, LAMBDA4_FP)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive (Hodge index theorem)."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_lambda_decreasing(self):
        """lambda_{g+1}^FP < lambda_g^FP (geometric decay)."""
        for g in range(1, 6):
            self.assertLess(lambda_fp(g + 1), lambda_fp(g))

    def test_lambda4_denominator_factorization(self):
        """Verify 154828800 = 128 * 30 * 40320 = 2^7 * 30 * 8!."""
        self.assertEqual(128 * 30 * 40320, 154828800)
        self.assertEqual(40320, factorial(8))


# ====================================================================
# Section 2: Bernoulli numbers
# ====================================================================

class TestBernoulli(unittest.TestCase):
    """Test exact Bernoulli numbers relevant to genus 4."""

    def test_B8(self):
        """B_8 = -1/30."""
        self.assertEqual(_bernoulli_exact(8), Fraction(-1, 30))

    def test_B6(self):
        """B_6 = 1/42 (genus-3 cross-check)."""
        self.assertEqual(_bernoulli_exact(6), Fraction(1, 42))

    def test_B10(self):
        """B_10 = 5/66 (genus-5 look-ahead)."""
        self.assertEqual(_bernoulli_exact(10), Fraction(5, 66))


# ====================================================================
# Section 3: Kappa values
# ====================================================================

class TestKappaValues(unittest.TestCase):
    """Test kappa formulas for all families (AP1: never copy between families)."""

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
        self.assertEqual(kappa_affine_sl2(-2), Fraction(0))

    def test_affine_sl3(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        self.assertEqual(kappa_affine_sl3(1), Fraction(16, 3))
        self.assertEqual(kappa_affine_sl3(-3), Fraction(0))

    def test_w3(self):
        """kappa(W_3, c) = 5c/6."""
        self.assertEqual(kappa_w3(Fraction(2)), Fraction(5, 3))
        self.assertEqual(kappa_w3(Fraction(50)), Fraction(125, 3))

    def test_betagamma(self):
        """kappa(beta-gamma, lambda) = 6*lambda^2 - 6*lambda + 1."""
        self.assertEqual(kappa_betagamma(1), Fraction(1))
        self.assertEqual(kappa_betagamma(0), Fraction(1))

    def test_lattice(self):
        """kappa(V_Lambda) = rank."""
        self.assertEqual(kappa_lattice(4), Fraction(4))
        self.assertEqual(kappa_lattice(8), Fraction(8))
        self.assertEqual(kappa_lattice(24), Fraction(24))

    def test_betagamma_c_relation(self):
        """kappa = c/2 for beta-gamma (all lambda values)."""
        for lam in [0, 1, 2, 3]:
            c = c_betagamma(lam)
            self.assertEqual(kappa_betagamma(lam), c / 2)


# ====================================================================
# Section 4: F_4 values for 10 families
# ====================================================================

class TestF4Values(unittest.TestCase):
    """Test F_4 = kappa * 127/154828800 for all 10 families."""

    def test_heisenberg_k1(self):
        """F_4(H_1) = 127/154828800."""
        self.assertEqual(F4(kappa_heisenberg(1)), Fraction(127, 154828800))

    def test_virasoro_c25(self):
        """F_4(Vir_25) = (25/2) * 127/154828800 = 127/12386304."""
        f4 = F4(kappa_virasoro(Fraction(25)))
        self.assertEqual(f4, Fraction(127, 12386304))

    def test_affine_sl2_k1(self):
        """F_4(sl_2, k=1) = (9/4) * 127/154828800 = 127/68812800."""
        f4 = F4(kappa_affine_sl2(1))
        self.assertEqual(f4, Fraction(127, 68812800))

    def test_affine_sl3_k1(self):
        """F_4(sl_3, k=1) = (16/3) * 127/154828800 = 127/29030400."""
        expected = Fraction(16, 3) * Fraction(127, 154828800)
        self.assertEqual(F4(kappa_affine_sl3(1)), expected)
        self.assertEqual(expected, Fraction(127, 29030400))

    def test_w3_c2(self):
        """F_4(W_3, c=2) = (5/3) * 127/154828800 = 127/92897280."""
        expected = Fraction(5, 3) * Fraction(127, 154828800)
        self.assertEqual(F4(kappa_w3(Fraction(2))), expected)
        self.assertEqual(expected, Fraction(127, 92897280))

    def test_w3_c50_selfdual(self):
        """F_4(W_3, c=50) = (125/3) * 127/154828800 = 635/18579456."""
        expected = Fraction(125, 3) * Fraction(127, 154828800)
        self.assertEqual(F4(kappa_w3(Fraction(50))), expected)
        # 125*127 / (3*154828800) = 15875/464486400 = 635/18579456
        self.assertEqual(expected, Fraction(635, 18579456))

    def test_betagamma_lam1(self):
        """F_4(beta-gamma, lambda=1) = 127/154828800."""
        self.assertEqual(F4(kappa_betagamma(1)), Fraction(127, 154828800))

    def test_D4_lattice(self):
        """F_4(D_4 lattice) = 4 * 127/154828800 = 127/38707200."""
        self.assertEqual(F4(kappa_lattice(4)), Fraction(127, 38707200))

    def test_E8_lattice(self):
        """F_4(E_8 lattice) = 8 * 127/154828800 = 127/19353600."""
        self.assertEqual(F4(kappa_lattice(8)), Fraction(127, 19353600))

    def test_Leech_lattice(self):
        """F_4(Leech lattice) = 24 * 127/154828800 = 127/6451200."""
        self.assertEqual(F4(kappa_lattice(24)), Fraction(127, 6451200))

    def test_heisenberg_betagamma_coincidence(self):
        """H_1 and beta-gamma at lambda=1 have same kappa (both = 1)."""
        self.assertEqual(F4(kappa_heisenberg(1)), F4(kappa_betagamma(1)))


# ====================================================================
# Section 5: Universal ratios
# ====================================================================

class TestUniversalRatios(unittest.TestCase):
    """Test that F_g/F_h ratios are algebra-independent on the scalar lane."""

    def test_F4_over_F1(self):
        """F_4/F_1 = lambda_4/lambda_1 = (127/154828800)/(1/24) = 127/6451200."""
        ratios = genus4_ratio_table()
        self.assertEqual(ratios['F4_over_F1'], Fraction(127, 6451200))

    def test_F4_over_F2(self):
        """F_4/F_2 = (127/154828800)/(7/5760) = 127/188160."""
        ratios = genus4_ratio_table()
        self.assertEqual(ratios['F4_over_F2'], Fraction(127, 188160))

    def test_F4_over_F3(self):
        """F_4/F_3 = (127/154828800)/(31/967680) = 127/4960."""
        ratios = genus4_ratio_table()
        self.assertEqual(ratios['F4_over_F3'], Fraction(127, 4960))

    def test_ratio_universality_across_families(self):
        """Verify F_4/F_1 is the same for all algebras with nonzero kappa."""
        table = genus4_landscape_table()
        r41 = Fraction(127, 6451200)
        for name, data in table.items():
            kappa = data['kappa']
            if kappa == 0:
                continue
            f4 = data['F4']
            f1 = kappa * lambda_fp(1)
            self.assertEqual(f4 / f1, r41,
                             f"Ratio F_4/F_1 not universal for {name}")

    def test_127_is_prime(self):
        """Verify 127 = 2^7 - 1 is a Mersenne prime.

        This explains why the lambda_4^FP numerator does not simplify
        further: 127 is prime, so Fraction(127, 154828800) is already reduced.
        """
        self.assertEqual(2**7 - 1, 127)
        # Check 127 is prime by trial division
        for p in [2, 3, 5, 7, 11]:
            self.assertNotEqual(127 % p, 0)


# ====================================================================
# Section 6: Complementarity (AP24)
# ====================================================================

class TestComplementarity(unittest.TestCase):
    """Test F_4 complementarity: F_4(A) + F_4(A^!) relations."""

    def test_heisenberg_antisymmetry(self):
        """For Heisenberg: kappa' = -kappa, so F_4 + F_4' = 0."""
        for k in [1, 2, 5]:
            kA = kappa_heisenberg(k)
            kA_dual = -kA
            result = complementarity_check_F4('Heisenberg', kA, kA_dual)
            self.assertEqual(result['sum'], Fraction(0))
            self.assertEqual(result['kappa_sum'], Fraction(0))

    def test_affine_sl2_antisymmetry(self):
        """For affine sl_2: kappa + kappa' = 0 (Feigin-Frenkel: k -> -k-2h^v)."""
        for k in [1, 2, 3]:
            kA = kappa_affine_sl2(k)
            k_dual = -k - 4  # h^v = 2 for sl_2
            kA_dual = kappa_affine_sl2(k_dual)
            result = complementarity_check_F4('Affine_sl2', kA, kA_dual)
            self.assertEqual(result['kappa_sum'], Fraction(0),
                             f"Failed at k={k}: kappa+kappa'={result['kappa_sum']}")
            self.assertEqual(result['sum'], Fraction(0))

    def test_lattice_antisymmetry(self):
        """For lattice VOA: kappa + kappa' = 0."""
        for d in [4, 8, 24]:
            kA = kappa_lattice(d)
            kA_dual = -kA
            result = complementarity_check_F4(f'Lattice_d{d}', kA, kA_dual)
            self.assertEqual(result['sum'], Fraction(0))

    def test_virasoro_nonzero_sum(self):
        """For Virasoro: kappa + kappa' = 13 (not 0). AP24.

        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
        F_4 + F_4' = 13 * lambda_4^FP = 1651/154828800.
        """
        for c_val in [1, 13, 25]:
            kA = kappa_virasoro(Fraction(c_val))
            kA_dual = kappa_virasoro(Fraction(26 - c_val))
            result = complementarity_check_F4('Virasoro', kA, kA_dual)
            self.assertEqual(result['kappa_sum'], Fraction(13))
            expected_sum = Fraction(13) * LAMBDA4_FP
            self.assertEqual(result['sum'], expected_sum,
                             f"Failed at c={c_val}")
            # Verify explicit value: 13 * 127 / 154828800 = 1651/154828800
            self.assertEqual(expected_sum, Fraction(1651, 154828800))


# ====================================================================
# Section 7: Generating function consistency
# ====================================================================

class TestGeneratingFunction(unittest.TestCase):
    """Test GF consistency: sum lambda_g x^{2g} = (x/2)/sin(x/2) - 1."""

    def test_consistency_through_g5(self):
        self.assertTrue(verify_generating_function_consistency(5))

    def test_consistency_through_g8(self):
        self.assertTrue(verify_generating_function_consistency(8))


# ====================================================================
# Section 8: Kappa additivity
# ====================================================================

class TestKappaAdditivity(unittest.TestCase):
    """Test kappa additivity for tensor products (lattice VOAs)."""

    def test_lattice_is_rank_copies(self):
        """kappa(H_1^{tensor d}) = d * kappa(H_1) = d."""
        for d in [1, 4, 8, 16, 24]:
            self.assertEqual(kappa_lattice(d), d * kappa_heisenberg(1))

    def test_F4_additivity(self):
        """F_4(A tensor B) = F_4(A) + F_4(B) for free-field tensor products."""
        self.assertEqual(
            F4(kappa_lattice(24)),
            24 * F4(kappa_heisenberg(1))
        )

    def test_D4_is_four_copies(self):
        """F_4(D_4) = 4 * F_4(H_1)."""
        self.assertEqual(F4(kappa_lattice(4)), 4 * F4(kappa_heisenberg(1)))


# ====================================================================
# Section 9: Cross-genus ratio universality
# ====================================================================

class TestCrossGenusRatios(unittest.TestCase):
    """Verify cross-genus ratio chain is consistent."""

    def test_F4_F1_ratio_chain(self):
        """F_4/F_1 = (F_4/F_3) * (F_3/F_2) * (F_2/F_1).

        Verify the chain of ratios multiplies correctly.
        """
        ratios = genus4_ratio_table()
        chain = ratios['F4_over_F3'] * ratios['F3_over_F1']
        direct = ratios['F4_over_F1']
        self.assertEqual(chain, direct)

    def test_F4_F2_via_F3(self):
        """F_4/F_2 = (F_4/F_3) * (F_3/F_2)."""
        ratios = genus4_ratio_table()
        l2 = ratios['lambda_2']
        l3 = ratios['lambda_3']
        l4 = ratios['lambda_4']
        self.assertEqual(l4 / l2, (l4 / l3) * (l3 / l2))

    def test_numerators_are_mersenne(self):
        """The numerators 1, 7, 31, 127 are 2^{2g-1} - 1.

        g=1: 2^1-1=1, g=2: 2^3-1=7, g=3: 2^5-1=31, g=4: 2^7-1=127.
        """
        for g, expected_num in [(1, 1), (2, 7), (3, 31), (4, 127)]:
            self.assertEqual(2**(2*g - 1) - 1, expected_num)
            lfp = lambda_fp(g)
            # The numerator of the reduced fraction should divide 2^{2g-1}-1
            self.assertEqual(lfp.numerator % expected_num, 0,
                             f"At g={g}: numerator {lfp.numerator} "
                             f"not divisible by {expected_num}")


# ====================================================================
# Section 10: Sign and edge case checks
# ====================================================================

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and sign behavior."""

    def test_F4_positive_for_positive_kappa(self):
        """F_4 > 0 when kappa > 0."""
        for k in [Fraction(1), Fraction(1, 2), Fraction(100)]:
            self.assertGreater(F4(k), Fraction(0))

    def test_F4_negative_for_negative_kappa(self):
        """F_4 < 0 when kappa < 0."""
        for k in [Fraction(-1), Fraction(-10)]:
            self.assertLess(F4(k), Fraction(0))

    def test_F4_zero_for_zero_kappa(self):
        """F_4 = 0 when kappa = 0 (uncurved)."""
        self.assertEqual(F4(Fraction(0)), Fraction(0))

    def test_critical_level_sl2(self):
        """At critical level k=-h^v=-2: kappa=0, F_4=0."""
        kappa = kappa_affine_sl2(-2)
        self.assertEqual(kappa, Fraction(0))
        self.assertEqual(F4(kappa), Fraction(0))

    def test_critical_level_sl3(self):
        """At critical level k=-h^v=-3: kappa=0, F_4=0."""
        kappa = kappa_affine_sl3(-3)
        self.assertEqual(kappa, Fraction(0))
        self.assertEqual(F4(kappa), Fraction(0))


# ====================================================================
# Section 11: Manuscript cross-checks
# ====================================================================

class TestManuscriptCrossChecks(unittest.TestCase):
    """Verify against explicit values and computation chains."""

    def test_sl2_k1_genus4(self):
        """F_4(sl_2, k=1) = 127/68812800."""
        self.assertTrue(verify_manuscript_sl2_genus4())
        # Direct: 9/4 * 127/154828800 = 9*127/(4*154828800) = 1143/619315200
        # Simplify: GCD(1143, 619315200) = 9 → 127/68812800
        f4 = F4(kappa_affine_sl2(1))
        self.assertEqual(f4, Fraction(127, 68812800))

    def test_w3_k1_genus4(self):
        """F_4(W_3, k=1): c=-52, kappa=-130/3, F_4=-1651/46448640."""
        self.assertTrue(verify_manuscript_w3_genus4())
        c_val = c_w3(1)
        self.assertEqual(c_val, Fraction(-52))
        kappa = kappa_w3(c_val)
        self.assertEqual(kappa, Fraction(-130, 3))
        f4 = F4(kappa)
        # -130/3 * 127/154828800 = -130*127/(3*154828800) = -16510/464486400
        # = -1651/46448640
        self.assertEqual(f4, Fraction(-1651, 46448640))

    def test_sl2_genus4_parametric(self):
        """Verify F_4(sl_2, k) = 127(k+2)/206438400 for several k."""
        for k in [1, 2, 3, 5, 10]:
            kappa = kappa_affine_sl2(k)
            f4 = F4(kappa)
            # kappa = 3(k+2)/4,  F_4 = 3(k+2)/4 * 127/154828800
            # = 3*127*(k+2)/(4*154828800) = 381*(k+2)/619315200
            # = 127*(k+2)/206438400
            expected = Fraction(127 * (k + 2), 206438400)
            self.assertEqual(f4, expected,
                             f"Failed at k={k}: {f4} != {expected}")


# ====================================================================
# Section 12: Full landscape table
# ====================================================================

class TestLandscapeTable(unittest.TestCase):
    """Test the full landscape table."""

    def test_table_has_10_entries(self):
        table = genus4_landscape_table()
        self.assertEqual(len(table), 10)

    def test_all_entries_have_required_keys(self):
        table = genus4_landscape_table()
        for name, data in table.items():
            self.assertIn('kappa', data)
            self.assertIn('F4', data)
            self.assertIn('c', data)
            self.assertIn('description', data)

    def test_F4_consistency(self):
        """Every F_4 in the table equals kappa * lambda_4^FP."""
        table = genus4_landscape_table()
        for name, data in table.items():
            expected = data['kappa'] * LAMBDA4_FP
            self.assertEqual(data['F4'], expected,
                             f"Inconsistency for {name}")


# ====================================================================
# Section 13: Cross-check against genus-3 module
# ====================================================================

class TestCrossGenusConsistency(unittest.TestCase):
    """Cross-check genus-4 values against genus-3 module for consistency."""

    def test_lambda_consistency_g1_to_g4(self):
        """lambda_g^FP matches known values for g = 1, 2, 3, 4."""
        self.assertEqual(lambda_fp(1), Fraction(1, 24))
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))

    def test_F4_over_F1_equals_lambda4_over_lambda1(self):
        """The ratio F_4/F_1 = lambda_4/lambda_1 for any nonzero kappa."""
        kappa = Fraction(7, 3)
        f4 = F4(kappa)
        f1 = kappa * lambda_fp(1)
        self.assertEqual(f4 / f1, lambda_fp(4) / lambda_fp(1))
        self.assertEqual(f4 / f1, Fraction(127, 6451200))


# ====================================================================
# Section 14: Asymptotic ratio check
# ====================================================================

class TestAsymptoticRatio(unittest.TestCase):
    """Verify F_{g+1}/F_g ratio approaches 1/(2*pi)^2."""

    def test_ratio_at_genus_4(self):
        """lambda_4/lambda_3 should be closer to 1/(4*pi^2) than lambda_3/lambda_2."""
        import math
        target = 1.0 / (4 * math.pi**2)  # ~ 0.02533
        r43 = float(lambda_fp(4) / lambda_fp(3))  # 127/4960
        r32 = float(lambda_fp(3) / lambda_fp(2))  # 31/1176
        # Both should be in the right ballpark
        self.assertAlmostEqual(r43, target, places=2)
        # r43 should be closer to the asymptotic value than r32
        self.assertLess(abs(r43 - target), abs(r32 - target))


if __name__ == '__main__':
    unittest.main()
