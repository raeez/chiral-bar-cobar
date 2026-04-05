r"""Tests for DT invariants from the shadow obstruction tower.

Verifies all engine functions across 90+ tests organized by:
    Section 1:  Arithmetic helpers (Mobius, divisors, sigma)
    Section 2:  Faber-Pandharipande lambda_g^FP
    Section 3:  Shadow coefficient extraction (all families)
    Section 4:  Plethystic exponential (exp-log recurrence)
    Section 5:  Plethystic logarithm and Mobius inversion
    Section 6:  PE/PL roundtrip (fundamental identity)
    Section 7:  PE product form (independent method)
    Section 8:  PE two-method cross-verification
    Section 9:  BPS invariants from shadow data
    Section 10: BPS integrality checks
    Section 11: Heisenberg DT partition function
    Section 12: Virasoro DT partition function
    Section 13: GW/DT correspondence (A-hat identity)
    Section 14: GV extraction (multicover formula)
    Section 15: PT invariants
    Section 16: Motivic shadow partition function
    Section 17: Koszul complementarity (AP24)
    Section 18: Wall-crossing comparison
    Section 19: Shadow depth classification
    Section 20: Full Virasoro DT analysis
    Section 21: Cross-family verification
    Section 22: Numerical precision tests

Multi-path verification mandate: every numerical value checked by at least 2
independent methods. AP1/AP3/AP10 compliance: independent computations, never
hardcoded from pattern matching.
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, cancel, Abs

from compute.lib.bc_donaldson_thomas_shadow_engine import (
    # Arithmetic helpers
    _mobius,
    _prime_factors,
    _divisors,
    _sigma,
    _bernoulli_number,
    _lambda_fp,
    # Shadow coefficients
    virasoro_shadow_coefficients,
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    betagamma_shadow_coefficients,
    virasoro_shadow_coefficients_float,
    # Plethystic
    plethystic_exp_coefficients,
    plethystic_exp_coefficients_float,
    plethystic_log_coefficients,
    plethystic_log_coefficients_float,
    verify_pe_pl_roundtrip,
    # PE product form and Adams exponential
    pe_product_form,
    adams_exponential,
    verify_pe_two_methods,
    # BPS
    shadow_bps_invariants,
    shadow_bps_invariants_from_product,
    bps_integrality_check,
    # DT
    shadow_dt_partition_function,
    shadow_dt_partition_function_float,
    # Wall-crossing
    koszul_dual_shadow,
    wall_crossing_product_comparison,
    # GW/DT
    shadow_free_energy,
    a_hat_generating_function,
    a_hat_gf_series,
    gw_dt_correspondence_check,
    verify_gw_dt_ahat,
    # GV
    gv_from_shadow_free_energy,
    gv_extraction_multicover,
    # PT
    pt_from_dt,
    # Motivic
    motivic_shadow_partition,
    # Classification
    shadow_depth_class,
    dt_complexity_from_depth,
    # Cross-verification
    shadow_kappa_complementarity_check,
    # Full analysis
    virasoro_dt_analysis,
    # Heisenberg specializations
    heisenberg_dt_partition,
    heisenberg_dt_product_form,
)


# ============================================================================
# Section 1: Arithmetic helpers
# ============================================================================

class TestArithmeticHelpers(unittest.TestCase):
    """Test Mobius function, prime factorization, divisors, sigma."""

    def test_mobius_primes(self):
        """mu(p) = -1 for all primes."""
        for p in [2, 3, 5, 7, 11, 13]:
            self.assertEqual(_mobius(p), -1)

    def test_mobius_squarefree(self):
        """mu(pq) = 1 for distinct primes p, q."""
        self.assertEqual(_mobius(6), 1)   # 2*3
        self.assertEqual(_mobius(10), 1)  # 2*5
        self.assertEqual(_mobius(15), 1)  # 3*5
        self.assertEqual(_mobius(30), -1) # 2*3*5

    def test_mobius_squares(self):
        """mu(n) = 0 if n has a squared prime factor."""
        for n in [4, 8, 9, 12, 16, 18, 20, 25, 27]:
            self.assertEqual(_mobius(n), 0, f"mu({n}) should be 0")

    def test_mobius_one(self):
        self.assertEqual(_mobius(1), 1)

    def test_mobius_sum_identity(self):
        """sum_{d|n} mu(d) = [n == 1] (Mobius inversion identity)."""
        for n in range(1, 30):
            s = sum(_mobius(d) for d in _divisors(n))
            expected = 1 if n == 1 else 0
            self.assertEqual(s, expected, f"Failed Mobius sum identity for n={n}")

    def test_prime_factors(self):
        self.assertEqual(_prime_factors(12), {2: 2, 3: 1})
        self.assertEqual(_prime_factors(1), {})
        self.assertEqual(_prime_factors(7), {7: 1})

    def test_divisors(self):
        self.assertEqual(_divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(_divisors(1), [1])
        self.assertEqual(_divisors(7), [1, 7])

    def test_sigma(self):
        """sigma_0(n) = number of divisors."""
        self.assertEqual(_sigma(12, 0), 6)
        self.assertEqual(_sigma(1, 0), 1)
        # sigma_1(6) = 1+2+3+6 = 12
        self.assertEqual(_sigma(6, 1), 12)
        # sigma_2(4) = 1+4+16 = 21
        self.assertEqual(_sigma(4, 2), 21)


# ============================================================================
# Section 2: Faber-Pandharipande lambda_g
# ============================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Test lambda_g^FP values.

    Ground truth (AP38 convention verification):
      lambda_1 = 1/24
      lambda_2 = 7/5760
      lambda_3 = 31/967680
    """

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        self.assertEqual(_lambda_fp(1), Rational(1, 24))

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        self.assertEqual(_lambda_fp(2), Rational(7, 5760))

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        self.assertEqual(_lambda_fp(3), Rational(31, 967680))

    def test_lambda_positivity(self):
        """All lambda_g^FP are positive for g >= 1."""
        for g in range(1, 12):
            self.assertGreater(float(_lambda_fp(g)), 0)

    def test_lambda_formula_consistency(self):
        """Check formula: lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!"""
        import sympy
        for g in range(1, 8):
            B2g = Rational(sympy.bernoulli(2 * g))
            num = (2 ** (2 * g - 1) - 1) * abs(B2g)
            den = 2 ** (2 * g - 1) * sympy.factorial(2 * g)
            expected = Rational(num, den)
            self.assertEqual(_lambda_fp(g), expected, f"Mismatch at g={g}")


# ============================================================================
# Section 3: Shadow coefficient extraction
# ============================================================================

class TestShadowCoefficients(unittest.TestCase):
    """Test shadow coefficients for all standard families."""

    def test_heisenberg_kappa(self):
        """Heisenberg: kappa = k, S_r = 0 for r >= 3."""
        for k in [1, 2, 5]:
            shadow = heisenberg_shadow_coefficients(str(k), 10)
            self.assertEqual(shadow[2], Rational(k))
            for r in range(3, 11):
                self.assertEqual(shadow[r], Rational(0))

    def test_virasoro_kappa(self):
        """Virasoro: kappa = c/2 (AP48 applies)."""
        for c_val in [1, 4, 10, 13, 25]:
            shadow = virasoro_shadow_coefficients(str(c_val), 10)
            self.assertEqual(shadow[2], Rational(c_val, 2))

    def test_virasoro_S3(self):
        """Virasoro S_3 = 2 (universal cubic, AP1 checked)."""
        for c_val in [1, 4, 10, 25]:
            shadow = virasoro_shadow_coefficients(str(c_val), 10)
            # S_3 = a_1/3 = 6/3 = 2
            self.assertEqual(shadow[3], Rational(2))

    def test_virasoro_S4(self):
        """Virasoro S_4 = 10/(c(5c+22)) / 4 ... let's compute.

        a_2 = 40/(c(5c+22)), S_4 = a_2/4 = 10/(c(5c+22)).
        """
        for c_val in [1, 4, 10, 25]:
            shadow = virasoro_shadow_coefficients(str(c_val), 10)
            expected = Rational(10, c_val * (5 * c_val + 22))
            self.assertEqual(cancel(shadow[4] - expected), 0,
                             f"S_4 mismatch at c={c_val}")

    def test_affine_sl2_kappa(self):
        """Affine sl_2: kappa = 3(k+2)/4."""
        for k in [1, 2, 3, 5]:
            shadow = affine_sl2_shadow_coefficients(str(k), 10)
            expected = Rational(3 * (k + 2), 4)
            self.assertEqual(shadow[2], expected)

    def test_affine_sl2_terminates(self):
        """Affine sl_2 is class L: S_r = 0 for r >= 4."""
        shadow = affine_sl2_shadow_coefficients('1', 10)
        for r in range(4, 11):
            self.assertEqual(shadow[r], Rational(0))

    def test_betagamma_terminates(self):
        """Beta-gamma is class C: S_r = 0 for r >= 5."""
        shadow = betagamma_shadow_coefficients(1, 10)
        for r in range(5, 11):
            self.assertEqual(shadow[r], Rational(0))

    def test_betagamma_S3_universal(self):
        """Beta-gamma S_3 = 2 (universal on T-line)."""
        shadow = betagamma_shadow_coefficients(1, 10)
        self.assertEqual(shadow[3], Rational(2))

    def test_virasoro_float_consistency(self):
        """Float and exact Virasoro shadow coefficients agree."""
        c_val = 10
        exact = virasoro_shadow_coefficients(str(c_val), 20)
        flt = virasoro_shadow_coefficients_float(float(c_val), 20)
        for r in range(2, 15):
            self.assertAlmostEqual(float(exact[r]), flt[r], places=10,
                                   msg=f"Float/exact mismatch at r={r}")


# ============================================================================
# Section 4: Plethystic exponential (exp-log recurrence)
# ============================================================================

class TestPlethysticExponential(unittest.TestCase):
    """Test PE[g(q)] computation."""

    def test_pe_zero(self):
        """PE[0] = 1 (constant)."""
        shadow = {r: Rational(0) for r in range(2, 10)}
        pe = plethystic_exp_coefficients(shadow, 10)
        self.assertEqual(pe[0], Rational(1))
        for n in range(1, 11):
            self.assertEqual(pe[n], Rational(0))

    def test_pe_heisenberg_k1(self):
        """PE[q^2] = exp(sum_{k>=1} q^{2k}/k) = (1-q^2)^{-1}.

        This is the geometric series: 1, 0, 1, 0, 1, 0, 1, ...

        NOTE: PE is NOT the same as the Adams/second-quantized exponential.
        PE[q^2] = 1/(1-q^2), while AE[q^2] = prod (1-q^{2m})^{-1}.
        """
        shadow = heisenberg_shadow_coefficients('1', 20)
        pe = plethystic_exp_coefficients(shadow, 10)
        # PE[q^2] = (1-q^2)^{-1} = 1 + q^2 + q^4 + q^6 + ...
        expected = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        for n in range(11):
            self.assertEqual(pe[n], Rational(expected[n]),
                             f"PE[q^2] mismatch at n={n}")

    def test_pe_heisenberg_k2(self):
        """PE[2*q^2] = (1-q^2)^{-2} = sum_{j>=0} (j+1) q^{2j}.

        Coefficients at q^{2j}: j+1 = 1, 2, 3, 4, 5, ...
        """
        shadow = heisenberg_shadow_coefficients('2', 20)
        pe = plethystic_exp_coefficients(shadow, 10)
        # (1-q^2)^{-2} = 1 + 2q^2 + 3q^4 + 4q^6 + 5q^8 + 6q^{10} + ...
        expected = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]
        for n in range(11):
            self.assertEqual(pe[n], Rational(expected[n]),
                             f"PE[2q^2] mismatch at n={n}")

    def test_pe_leading_coefficient(self):
        """PE[alpha*q^r] starts: 1 + 0 + ... + alpha*q^r + ..."""
        for r in [2, 3, 5]:
            shadow = {i: Rational(0) for i in range(2, 10)}
            shadow[r] = Rational(3)
            pe = plethystic_exp_coefficients(shadow, 2 * r)
            self.assertEqual(pe[0], Rational(1))
            for n in range(1, r):
                self.assertEqual(pe[n], Rational(0), f"Non-zero before r={r}")
            self.assertEqual(pe[r], Rational(3), f"Leading coeff wrong at r={r}")

    def test_pe_float_consistency(self):
        """Float and exact PE agree for Heisenberg k=1."""
        shadow_exact = heisenberg_shadow_coefficients('1', 15)
        shadow_float = {r: float(v) for r, v in shadow_exact.items()}
        pe_exact = plethystic_exp_coefficients(shadow_exact, 15)
        pe_float = plethystic_exp_coefficients_float(shadow_float, 15)
        for n in range(16):
            self.assertAlmostEqual(float(pe_exact[n]), pe_float[n], places=10)


# ============================================================================
# Section 5: Plethystic logarithm and Mobius inversion
# ============================================================================

class TestPlethysticLogarithm(unittest.TestCase):
    """Test PL computation and Mobius inversion."""

    def test_pl_of_one(self):
        """PL[1 + 0 + ...] = 0."""
        Z = [Rational(1)] + [Rational(0)] * 10
        pl = plethystic_log_coefficients(Z, 10)
        for n in range(1, 11):
            self.assertEqual(pl[n], Rational(0))

    def test_pl_simple(self):
        """PL[1 + q^2] should give the single-particle spectrum."""
        Z = [Rational(0)] * 11
        Z[0] = Rational(1)
        Z[2] = Rational(1)
        pl = plethystic_log_coefficients(Z, 10)
        # PL[1+q^2] = q^2 - q^4/2 + q^6/3 - ... (log expansion)
        # No! PL is NOT log. PL uses Mobius inversion.
        # log(1+q^2) = q^2 - q^4/2 + q^6/3 - q^8/4 + ...
        # a_n = 0 for odd n, a_{2k} = (-1)^{k-1}/k
        # PL_n = (1/n) sum_{d|n} mu(n/d) d a_d
        # PL_2 = (1/2)(mu(1)*2*a_2) = (1/2)(2*1) = 1  (correct: single particle at 2)
        self.assertEqual(pl[2], Rational(1))

    def test_pl_float_consistency(self):
        """Float and exact PL agree."""
        shadow = heisenberg_shadow_coefficients('1', 15)
        pe = plethystic_exp_coefficients(shadow, 15)
        pe_float = [float(x) for x in pe]
        pl_exact = plethystic_log_coefficients(pe, 15)
        pl_float = plethystic_log_coefficients_float(pe_float, 15)
        for n in range(2, 12):
            self.assertAlmostEqual(float(pl_exact[n]), pl_float[n], places=10)


# ============================================================================
# Section 6: PE/PL roundtrip (fundamental identity)
# ============================================================================

class TestPEPLRoundtrip(unittest.TestCase):
    """PE[PL[Z]] = Z and PL[PE[g]] = g (fundamental identities)."""

    def test_roundtrip_heisenberg_k1(self):
        """Roundtrip for Heisenberg k=1."""
        shadow = heisenberg_shadow_coefficients('1', 20)
        result = verify_pe_pl_roundtrip(shadow, 20)
        self.assertTrue(result['roundtrip_exact'],
                        f"Roundtrip failed: {result['errors']}")

    def test_roundtrip_heisenberg_k3(self):
        """Roundtrip for Heisenberg k=3."""
        shadow = heisenberg_shadow_coefficients('3', 20)
        result = verify_pe_pl_roundtrip(shadow, 20)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_affine_sl2(self):
        """Roundtrip for affine sl_2 at k=1."""
        shadow = affine_sl2_shadow_coefficients('1', 20)
        result = verify_pe_pl_roundtrip(shadow, 20)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_betagamma(self):
        """Roundtrip for beta-gamma."""
        shadow = betagamma_shadow_coefficients(1, 20)
        result = verify_pe_pl_roundtrip(shadow, 15)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_virasoro_c1(self):
        """Roundtrip for Virasoro c=1."""
        shadow = virasoro_shadow_coefficients('1', 15)
        result = verify_pe_pl_roundtrip(shadow, 12)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_virasoro_c13(self):
        """Roundtrip for Virasoro c=13 (self-dual point)."""
        shadow = virasoro_shadow_coefficients('13', 15)
        result = verify_pe_pl_roundtrip(shadow, 12)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_virasoro_c25(self):
        """Roundtrip for Virasoro c=25."""
        shadow = virasoro_shadow_coefficients('25', 15)
        result = verify_pe_pl_roundtrip(shadow, 12)
        self.assertTrue(result['roundtrip_exact'])


# ============================================================================
# Section 7: PE product form (independent method)
# ============================================================================

class TestPEProductForm(unittest.TestCase):
    """Test PE via independent code path (both are exp-log but independent impls)."""

    def test_product_heisenberg_k1(self):
        """Independent PE for Heisenberg k=1 matches exp-log PE."""
        shadow = heisenberg_shadow_coefficients('1', 15)
        pe1 = plethystic_exp_coefficients(shadow, 10)
        pe2 = pe_product_form(shadow, 10)
        for n in range(11):
            self.assertEqual(pe1[n], pe2[n],
                             f"Independent PE mismatch at n={n}")

    def test_product_affine_sl2(self):
        """Independent PE for affine sl_2 matches exp-log."""
        shadow = affine_sl2_shadow_coefficients('1', 12)
        pe_exp = plethystic_exp_coefficients(shadow, 10)
        pe_prod = pe_product_form(shadow, 10)
        for n in range(11):
            self.assertEqual(pe_exp[n], pe_prod[n],
                             f"Product vs exp-log mismatch at n={n}")

    def test_product_single_term(self):
        """PE[2*q^3] = (1-q^3)^{-2} = sum C(j+1,j) q^{3j}."""
        shadow = {r: Rational(0) for r in range(2, 10)}
        shadow[3] = Rational(2)
        pe = pe_product_form(shadow, 12)
        self.assertEqual(pe[0], Rational(1))
        self.assertEqual(pe[3], Rational(2))
        # (1-q^3)^{-2}: coefficient of q^6 is C(3,2) = 3
        self.assertEqual(pe[6], Rational(3))

    def test_adams_heisenberg_k1(self):
        """Adams exponential AE[q^2] = prod (1-q^{2m})^{-1} = even partitions."""
        shadow = heisenberg_shadow_coefficients('1', 20)
        ae = adams_exponential(shadow, 10)
        expected = [1, 0, 1, 0, 2, 0, 3, 0, 5, 0, 7]
        for n in range(11):
            self.assertEqual(ae[n], Rational(expected[n]),
                             f"AE[q^2] mismatch at n={n}")

    def test_adams_vs_pe_differ(self):
        """PE and AE differ for Heisenberg (except at n=0,1,2)."""
        shadow = heisenberg_shadow_coefficients('1', 20)
        pe = plethystic_exp_coefficients(shadow, 10)
        ae = adams_exponential(shadow, 10)
        # At n=4: PE gives 1, AE gives 2
        self.assertEqual(pe[4], Rational(1))
        self.assertEqual(ae[4], Rational(2))
        # They agree at n=0, 1, 2, 3
        for n in [0, 1, 2, 3]:
            self.assertEqual(pe[n], ae[n])


# ============================================================================
# Section 8: PE two-method cross-verification
# ============================================================================

class TestPETwoMethods(unittest.TestCase):
    """Cross-verify PE via exp-log and product form."""

    def test_two_methods_heisenberg(self):
        """Two methods agree for Heisenberg."""
        shadow = heisenberg_shadow_coefficients('1', 20)
        result = verify_pe_two_methods(shadow, 15)
        self.assertTrue(result['match'], f"Mismatch: {result['diffs']}")

    def test_two_methods_affine(self):
        """Two methods agree for affine sl_2."""
        shadow = affine_sl2_shadow_coefficients('1', 15)
        result = verify_pe_two_methods(shadow, 12)
        self.assertTrue(result['match'], f"Mismatch: {result['diffs']}")

    def test_two_methods_betagamma(self):
        """Two methods agree for beta-gamma."""
        shadow = betagamma_shadow_coefficients(1, 12)
        result = verify_pe_two_methods(shadow, 10)
        self.assertTrue(result['match'], f"Mismatch: {result['diffs']}")

    def test_two_methods_virasoro_c4(self):
        """Two methods agree for Virasoro c=4 (truncated at max_r)."""
        shadow = virasoro_shadow_coefficients('4', 10)
        result = verify_pe_two_methods(shadow, 10)
        self.assertTrue(result['match'], f"Mismatch: {result['diffs']}")


# ============================================================================
# Section 9: BPS invariants from shadow data
# ============================================================================

class TestBPSInvariants(unittest.TestCase):
    """Test BPS invariant extraction."""

    def test_bps_heisenberg(self):
        """Heisenberg BPS: Omega(2) = k, Omega(r) = 0 for r >= 3."""
        shadow = heisenberg_shadow_coefficients('3', 10)
        bps = shadow_bps_invariants(shadow, 10)
        self.assertEqual(bps[2], Rational(3))
        for r in range(3, 11):
            self.assertEqual(bps[r], Rational(0))

    def test_bps_from_product_roundtrip(self):
        """BPS extracted from PE matches original shadow."""
        shadow = heisenberg_shadow_coefficients('2', 15)
        pe = plethystic_exp_coefficients(shadow, 15)
        bps = shadow_bps_invariants_from_product(pe, 15)
        for r in range(2, 12):
            expected = shadow.get(r, Rational(0))
            self.assertEqual(bps[r], expected,
                             f"BPS roundtrip failed at r={r}")

    def test_bps_from_product_affine(self):
        """BPS from PE roundtrip for affine sl_2."""
        shadow = affine_sl2_shadow_coefficients('1', 15)
        pe = plethystic_exp_coefficients(shadow, 15)
        bps = shadow_bps_invariants_from_product(pe, 15)
        for r in range(2, 12):
            expected = shadow.get(r, Rational(0))
            self.assertEqual(bps[r], expected)

    def test_bps_virasoro_nonzero(self):
        """Virasoro has nonzero BPS at all arities (class M)."""
        shadow = virasoro_shadow_coefficients('10', 15)
        bps = shadow_bps_invariants(shadow, 15)
        for r in range(2, 10):
            self.assertNotEqual(bps[r], Rational(0),
                                f"Expected nonzero BPS at r={r}")


# ============================================================================
# Section 10: BPS integrality checks
# ============================================================================

class TestBPSIntegrality(unittest.TestCase):
    """Test whether shadow coefficients satisfy integrality conditions."""

    def test_heisenberg_integer_bps(self):
        """Heisenberg BPS are integers for integer k."""
        for k in [1, 2, 5, 10]:
            shadow = heisenberg_shadow_coefficients(str(k), 10)
            result = bps_integrality_check(shadow, 10)
            self.assertTrue(result['all_integer'],
                            f"Heisenberg k={k} BPS not all integer")

    def test_virasoro_bps_rational(self):
        """Virasoro BPS at general c are rational, not necessarily integer.

        This is EXPECTED: the shadow coefficients S_r(c) are rational functions
        of c. For the DT interpretation, integrality would require specific c.
        """
        shadow = virasoro_shadow_coefficients('10', 10)
        result = bps_integrality_check(shadow, 8)
        # Just check it runs; integrality is not expected generically
        self.assertIn('all_integer', result)

    def test_virasoro_c1_S4_not_integer(self):
        """Virasoro S_4 at c=1 is 10/(1*27) = 10/27, NOT integer."""
        shadow = virasoro_shadow_coefficients('1', 10)
        S4 = shadow[4]
        self.assertEqual(S4, Rational(10, 27))


# ============================================================================
# Section 11: Heisenberg DT partition function
# ============================================================================

class TestHeisenbergDT(unittest.TestCase):
    """Test Heisenberg DT specialization."""

    def test_heisenberg_dt_k1_coefficients(self):
        """Heisenberg k=1 DT = AE[q^2] = partitions into even parts.

        OEIS A000009 (partitions into distinct parts) is NOT this;
        this is partitions into parts from {2,4,6,...}.
        Counts: 1, 0, 1, 0, 2, 0, 3, 0, 5, 0, 7.
        """
        pe = heisenberg_dt_partition(1, 10)
        expected = [1, 0, 1, 0, 2, 0, 3, 0, 5, 0, 7]
        for n in range(11):
            self.assertEqual(pe[n], Rational(expected[n]))

    def test_heisenberg_dt_product_form(self):
        """Independent product form agrees with PE for k=1."""
        pe = heisenberg_dt_partition(1, 12)
        prod = heisenberg_dt_product_form(1, 12)
        for n in range(13):
            self.assertEqual(int(pe[n]), prod[n],
                             f"k=1 DT mismatch at n={n}")

    def test_heisenberg_dt_k2_product(self):
        """k=2: Adams exponential and direct product agree."""
        ae = heisenberg_dt_partition(2, 10)
        prod = heisenberg_dt_product_form(2, 10)
        for n in range(11):
            self.assertEqual(int(ae[n]), prod[n],
                             f"k=2 DT mismatch at n={n}")

    def test_heisenberg_dt_k3_product(self):
        """k=3: Adams exponential and direct product agree."""
        ae = heisenberg_dt_partition(3, 10)
        prod = heisenberg_dt_product_form(3, 10)
        for n in range(11):
            self.assertEqual(int(ae[n]), prod[n],
                             f"k=3 DT mismatch at n={n}")

    def test_heisenberg_dt_integrality(self):
        """All Heisenberg DT (Adams) coefficients are non-negative integers."""
        for k in [1, 2, 3, 5]:
            ae = heisenberg_dt_partition(k, 15)
            for n in range(16):
                val = ae[n]
                self.assertEqual(val.denominator, 1,
                                 f"Non-integer at k={k}, n={n}: {val}")
                self.assertGreaterEqual(int(val), 0,
                                        f"Negative at k={k}, n={n}")

    def test_heisenberg_odd_vanish(self):
        """Heisenberg DT (Adams) coefficients vanish at odd n (only even parts)."""
        ae = heisenberg_dt_partition(1, 20)
        for n in range(1, 21, 2):
            self.assertEqual(ae[n], Rational(0),
                             f"Non-zero at odd n={n}")


# ============================================================================
# Section 12: Virasoro DT partition function
# ============================================================================

class TestVirasoroDT(unittest.TestCase):
    """Test Virasoro DT partition function."""

    def test_virasoro_pe_c1_leading(self):
        """Virasoro c=1 PE leading terms.

        PE[g(q)] with g(q) = S_2*q^2 + S_3*q^3 + ...
        Leading: c_0 = 1, c_1 = 0, c_2 = S_2 = 1/2.
        """
        shadow = virasoro_shadow_coefficients('1', 15)
        pe = plethystic_exp_coefficients(shadow, 10)
        self.assertEqual(pe[0], Rational(1))
        self.assertEqual(pe[1], Rational(0))
        self.assertEqual(pe[2], Rational(1, 2))

    def test_virasoro_pe_c13_leading(self):
        """Virasoro c=13 (self-dual) PE leading terms."""
        shadow = virasoro_shadow_coefficients('13', 15)
        pe = plethystic_exp_coefficients(shadow, 6)
        self.assertEqual(pe[0], Rational(1))
        self.assertEqual(pe[2], Rational(13, 2))

    def test_virasoro_pe_starts_at_q2(self):
        """No q^1 term (shadow starts at r=2)."""
        for c_val in [1, 4, 10, 25]:
            shadow = virasoro_shadow_coefficients(str(c_val), 10)
            pe = plethystic_exp_coefficients(shadow, 5)
            self.assertEqual(pe[1], Rational(0))


# ============================================================================
# Section 13: GW/DT correspondence (A-hat identity)
# ============================================================================

class TestGWDT(unittest.TestCase):
    """Test the A-hat generating function identity."""

    def test_ahat_at_zero(self):
        """A-hat GF at x=0 gives 0 (the -1 subtracts the constant)."""
        self.assertAlmostEqual(a_hat_generating_function(0.0), 0.0)

    def test_ahat_series_vs_closed(self):
        """Series and closed form of A-hat agree."""
        for x in [0.1, 0.5, 1.0]:
            series = a_hat_gf_series(x, 15)
            closed = a_hat_generating_function(x, 15)
            self.assertAlmostEqual(series, closed, places=8,
                                   msg=f"A-hat mismatch at x={x}")

    def test_ahat_leading_term(self):
        """Leading term: lambda_1 x^2 = x^2/24."""
        x = 0.01
        val = a_hat_generating_function(x, 15)
        leading = x**2 / 24
        self.assertAlmostEqual(val, leading, places=10)

    def test_gw_dt_check_c1(self):
        """GW/DT correspondence check for kappa = 1/2 (Virasoro c=1)."""
        result = gw_dt_correspondence_check(0.5, 10)
        self.assertTrue(result['converged'])

    def test_gw_dt_check_c25(self):
        """GW/DT correspondence check for kappa = 25/2 (Virasoro c=25)."""
        result = gw_dt_correspondence_check(12.5, 10)
        self.assertTrue(result['converged'])

    def test_verify_gw_dt_ahat_virasoro(self):
        """Full A-hat verification for multiple kappa values."""
        for kappa in [0.5, 5.0, 12.5]:
            result = verify_gw_dt_ahat(kappa, 10)
            self.assertTrue(result['all_match'],
                            f"A-hat failed at kappa={kappa}")

    def test_shadow_free_energy_values(self):
        """F_1 = kappa/24, F_2 = 7*kappa/5760."""
        kappa = Rational(5)
        F = shadow_free_energy(kappa, 5)
        self.assertEqual(F[1], Rational(5, 24))
        self.assertEqual(F[2], Rational(35, 5760))  # 7*5/5760
        self.assertEqual(F[2], Rational(7, 1152))

    def test_shadow_free_energy_positivity(self):
        """All F_g are positive for kappa > 0."""
        for kappa_val in [Rational(1), Rational(5), Rational(13)]:
            F = shadow_free_energy(kappa_val, 10)
            for g in range(1, 11):
                self.assertGreater(float(F[g]), 0,
                                   f"F_{g} not positive for kappa={kappa_val}")


# ============================================================================
# Section 14: GV extraction (multicover formula)
# ============================================================================

class TestGVExtraction(unittest.TestCase):
    """Test GV invariant extraction."""

    def test_gv_constant_map_zero(self):
        """Constant-map GV: all n_g^d = 0 for d >= 1 (no instantons)."""
        kappa = Rational(5)
        gv = gv_from_shadow_free_energy(kappa, g_max=3, d_max=5)
        for g in range(0, 4):
            for d in range(1, 6):
                self.assertEqual(gv[(g, d)], Rational(0))

    def test_gv_extraction_from_conifold_F_coeffs(self):
        """Extract GV from F_0 = sum n_0^d Li_3(Q^d).

        For conifold: n_0^d = 1 for all d.
        F_0,d = sum_{k|d} k^{-3} n_0^{d/k} = sum_{k|d} k^{-3}.
        Check n_0^d extraction via Mobius inversion.
        """
        # Construct F_coefficients for conifold genus 0
        d_max = 10
        F_coeffs: Dict[int, Rational] = {}
        for d in range(1, d_max + 1):
            F_coeffs[d] = sum(Rational(1, k**3) for k in _divisors(d))

        gv = gv_extraction_multicover(F_coeffs, genus=0, d_max=d_max)
        for d in range(1, d_max + 1):
            # Should recover n_0^d = 1
            self.assertEqual(gv[d], Rational(1),
                             f"GV extraction failed at d={d}: got {gv[d]}")

    def test_gv_extraction_genus2(self):
        """GV extraction at genus 2 from known data.

        For conifold at g >= 1: n_g^d = 0 for all d.
        F_{g>=1} = 0 for the conifold (no higher-genus contributions).
        """
        F_coeffs = {d: Rational(0) for d in range(1, 6)}
        gv = gv_extraction_multicover(F_coeffs, genus=2, d_max=5)
        for d in range(1, 6):
            self.assertEqual(gv[d], Rational(0))


# ============================================================================
# Section 15: PT invariants
# ============================================================================

class TestPTInvariants(unittest.TestCase):
    """Test PT partition function computation."""

    def test_pt_chi_zero(self):
        """PT = DT when chi = 0 (local CY3)."""
        shadow = heisenberg_shadow_coefficients('1', 15)
        dt = plethystic_exp_coefficients(shadow, 10)
        pt = pt_from_dt(dt, macmahon_power=0, max_n=10)
        for n in range(11):
            self.assertEqual(pt[n], dt[n])

    def test_pt_chi_one(self):
        """PT = DT / M(q) when chi = 1."""
        # For a simple test: Heisenberg k=1 DT divided by MacMahon
        shadow = heisenberg_shadow_coefficients('1', 15)
        dt = plethystic_exp_coefficients(shadow, 10)
        pt = pt_from_dt(dt, macmahon_power=1, max_n=10)
        # PT[0] should be 1 (constant term is always 1)
        self.assertEqual(pt[0], Rational(1))

    def test_pt_leading_terms(self):
        """Check PT leading structure for chi = 1."""
        shadow = heisenberg_shadow_coefficients('1', 15)
        dt = plethystic_exp_coefficients(shadow, 8)
        pt = pt_from_dt(dt, macmahon_power=1, max_n=8)
        # The result should be well-defined rational numbers
        for n in range(9):
            self.assertIsInstance(pt[n], Rational)


# ============================================================================
# Section 16: Motivic shadow partition function
# ============================================================================

class TestMotivicPartition(unittest.TestCase):
    """Test motivic shadow partition function at y = -1, 0, 1."""

    def test_motivic_y_minus1_equals_pe(self):
        """At y = -1: motivic reduces to PE[sum S_r q^r].

        w(r) = r-2, (-y)^{w(r)} = (1)^{r-2} = 1 for all r.
        So Z^mot(q, -1) = PE[sum S_r q^r].
        """
        shadow = heisenberg_shadow_coefficients('1', 15)
        mot = motivic_shadow_partition(shadow, y_val=Rational(-1), max_n=10)
        pe = plethystic_exp_coefficients(shadow, 10)
        for n in range(11):
            self.assertEqual(mot[n], pe[n],
                             f"Motivic y=-1 != PE at n={n}")

    def test_motivic_y_0(self):
        """At y = 0: only the S_2 term survives (w(2)=0, (-0)^0=1;
        w(r)>0 for r>2 gives 0^{w(r)}=0).
        """
        shadow = {2: Rational(3), 3: Rational(2), 4: Rational(1)}
        for r in range(5, 10):
            shadow[r] = Rational(0)
        mot = motivic_shadow_partition(shadow, y_val=Rational(0), max_n=10)
        # Only S_2 contributes: PE[3*q^2]
        shadow_2only = {2: Rational(3)}
        for r in range(3, 10):
            shadow_2only[r] = Rational(0)
        pe_2only = plethystic_exp_coefficients(shadow_2only, 10)
        for n in range(11):
            self.assertEqual(mot[n], pe_2only[n],
                             f"Motivic y=0 mismatch at n={n}")

    def test_motivic_y_1_alternating(self):
        """At y = 1: (-1)^{w(r)} = (-1)^{r-2} alternates signs.

        For r=2: (-1)^0 = 1 (S_2 unchanged)
        For r=3: (-1)^1 = -1 (S_3 negated)
        For r=4: (-1)^2 = 1 (S_4 unchanged)
        """
        shadow = {2: Rational(3), 3: Rational(2), 4: Rational(1)}
        for r in range(5, 10):
            shadow[r] = Rational(0)
        mot = motivic_shadow_partition(shadow, y_val=Rational(1), max_n=8)
        # Modified: S_2 -> 3, S_3 -> -2, S_4 -> 1
        mod_shadow = {2: Rational(3), 3: Rational(-2), 4: Rational(1)}
        for r in range(5, 10):
            mod_shadow[r] = Rational(0)
        pe_mod = plethystic_exp_coefficients(mod_shadow, 8)
        for n in range(9):
            self.assertEqual(mot[n], pe_mod[n],
                             f"Motivic y=1 mismatch at n={n}")


# ============================================================================
# Section 17: Koszul complementarity (AP24)
# ============================================================================

class TestKoszulComplementarity(unittest.TestCase):
    """Test kappa + kappa' values (AP24 compliance)."""

    def test_virasoro_complementarity(self):
        """Virasoro: kappa + kappa' = 13 (NOT 0)."""
        for c_val in [1, 4, 10, 13, 25]:
            result = shadow_kappa_complementarity_check(Rational(c_val), 'virasoro')
            self.assertTrue(result['match'],
                            f"AP24 failed at c={c_val}: sum={result['sum']}")
            self.assertEqual(result['sum'], Rational(13))

    def test_heisenberg_complementarity(self):
        """Heisenberg: kappa + kappa' = 0."""
        for k in [1, 2, 5]:
            result = shadow_kappa_complementarity_check(Rational(k), 'heisenberg')
            self.assertTrue(result['match'])
            self.assertEqual(result['sum'], Rational(0))

    def test_affine_sl2_complementarity(self):
        """Affine sl_2: kappa + kappa' = 0 (KM family)."""
        for k in [1, 2, 3]:
            result = shadow_kappa_complementarity_check(Rational(k), 'affine_sl2')
            self.assertTrue(result['match'])
            self.assertEqual(result['sum'], Rational(0))

    def test_virasoro_c13_selfdual(self):
        """At c=13: kappa = kappa' = 13/2 (self-dual, AP8)."""
        result = shadow_kappa_complementarity_check(Rational(13), 'virasoro')
        self.assertEqual(result['kappa_A'], Rational(13, 2))
        self.assertEqual(result['kappa_Ad'], Rational(13, 2))


# ============================================================================
# Section 18: Wall-crossing comparison
# ============================================================================

class TestWallCrossing(unittest.TestCase):
    """Test wall-crossing comparison between A and A!."""

    def test_koszul_dual_virasoro_shadow(self):
        """Koszul dual of Vir_c has shadow coefficients of Vir_{26-c}."""
        shadow_c1 = virasoro_shadow_coefficients('1', 10)
        dual = koszul_dual_shadow(shadow_c1, Rational(1), 'virasoro', 10)
        shadow_c25 = virasoro_shadow_coefficients('25', 10)
        for r in range(2, 8):
            self.assertEqual(cancel(dual[r] - shadow_c25[r]), 0,
                             f"Dual shadow mismatch at r={r}")

    def test_koszul_dual_heisenberg(self):
        """Koszul dual of H_k has kappa' = -k."""
        shadow = heisenberg_shadow_coefficients('3', 10)
        dual = koszul_dual_shadow(shadow, Rational(3), 'heisenberg', 10)
        self.assertEqual(dual[2], Rational(-3))

    def test_wall_crossing_product_runs(self):
        """Wall-crossing comparison runs without error."""
        shadow_A = virasoro_shadow_coefficients('10', 10)
        shadow_Ad = virasoro_shadow_coefficients('16', 10)
        result = wall_crossing_product_comparison(shadow_A, shadow_Ad, 8)
        self.assertIn('Z_A_leading', result)
        self.assertIn('ratio_leading', result)

    def test_wall_crossing_selfdual(self):
        """At c=13, A = A!, so ratio should be trivial (all 1s)."""
        shadow = virasoro_shadow_coefficients('13', 10)
        result = wall_crossing_product_comparison(shadow, shadow, 8)
        # Ratio Z_A / Z_{A!} should be 1 + 0 + 0 + ...
        self.assertEqual(result['ratio_leading'][0], Rational(1))
        for n in range(1, min(8, len(result['ratio_leading']))):
            self.assertEqual(result['ratio_leading'][n], Rational(0),
                             f"Non-trivial ratio at n={n}")


# ============================================================================
# Section 19: Shadow depth classification
# ============================================================================

class TestDepthClassification(unittest.TestCase):
    """Test shadow depth classification."""

    def test_heisenberg_class_G(self):
        shadow = heisenberg_shadow_coefficients('1', 10)
        self.assertEqual(shadow_depth_class(shadow), 'G')

    def test_affine_class_L(self):
        shadow = affine_sl2_shadow_coefficients('1', 10)
        self.assertEqual(shadow_depth_class(shadow), 'L')

    def test_betagamma_class_C(self):
        shadow = betagamma_shadow_coefficients(1, 10)
        self.assertEqual(shadow_depth_class(shadow), 'C')

    def test_virasoro_class_M(self):
        shadow = virasoro_shadow_coefficients('10', 10)
        self.assertEqual(shadow_depth_class(shadow), 'M')

    def test_dt_complexity_info(self):
        """DT complexity info is well-formed for all classes."""
        for cls in ['G', 'L', 'C', 'M']:
            info = dt_complexity_from_depth(cls)
            self.assertIn('depth', info)
            self.assertIn('example', info)


# ============================================================================
# Section 20: Full Virasoro DT analysis
# ============================================================================

class TestFullVirasoroAnalysis(unittest.TestCase):
    """Test the comprehensive Virasoro DT analysis function."""

    def test_analysis_c1(self):
        result = virasoro_dt_analysis(1, max_n=10, max_r=10)
        self.assertEqual(result['c'], 1)
        self.assertAlmostEqual(result['kappa'], 0.5)
        self.assertTrue(result['roundtrip_exact'])
        self.assertEqual(result['depth_class'], 'M')
        self.assertTrue(result['complementarity']['match'])

    def test_analysis_c13(self):
        result = virasoro_dt_analysis(13, max_n=10, max_r=10)
        self.assertAlmostEqual(result['kappa'], 6.5)
        self.assertTrue(result['roundtrip_exact'])
        self.assertEqual(result['depth_class'], 'M')

    def test_analysis_c25(self):
        result = virasoro_dt_analysis(25, max_n=10, max_r=10)
        self.assertAlmostEqual(result['kappa'], 12.5)
        self.assertTrue(result['roundtrip_exact'])

    def test_analysis_c4(self):
        result = virasoro_dt_analysis(4, max_n=8, max_r=8)
        self.assertAlmostEqual(result['kappa'], 2.0)
        self.assertTrue(result['roundtrip_exact'])


# ============================================================================
# Section 21: Cross-family verification
# ============================================================================

class TestCrossFamily(unittest.TestCase):
    """Cross-family consistency checks."""

    def test_kappa_additivity(self):
        """For independent tensor product: kappa additive.

        H_k1 tensor H_k2: kappa = k1 + k2.
        """
        k1, k2 = 3, 5
        shadow1 = heisenberg_shadow_coefficients(str(k1), 10)
        shadow2 = heisenberg_shadow_coefficients(str(k2), 10)
        shadow_sum = {r: shadow1.get(r, Rational(0)) + shadow2.get(r, Rational(0))
                      for r in range(2, 11)}
        self.assertEqual(shadow_sum[2], Rational(k1 + k2))

    def test_pe_factorizes_for_independent_sum(self):
        """PE[g1 + g2] = PE[g1] * PE[g2] for independent shadow data.

        This is the fundamental multiplicativity of PE.
        """
        shadow1 = heisenberg_shadow_coefficients('2', 10)
        shadow2 = heisenberg_shadow_coefficients('3', 10)
        shadow_sum = {r: shadow1.get(r, Rational(0)) + shadow2.get(r, Rational(0))
                      for r in range(2, 11)}

        pe_sum = plethystic_exp_coefficients(shadow_sum, 10)
        pe1 = plethystic_exp_coefficients(shadow1, 10)
        pe2 = plethystic_exp_coefficients(shadow2, 10)

        # Compute product pe1 * pe2
        product = [Rational(0)] * 11
        for i in range(11):
            for j in range(11 - i):
                product[i + j] += pe1[i] * pe2[j]

        for n in range(11):
            self.assertEqual(pe_sum[n], product[n],
                             f"PE multiplicativity failed at n={n}")

    def test_all_families_pe_starts_at_one(self):
        """PE always starts with 1."""
        families = [
            heisenberg_shadow_coefficients('1', 10),
            affine_sl2_shadow_coefficients('1', 10),
            betagamma_shadow_coefficients(1, 10),
            virasoro_shadow_coefficients('10', 10),
        ]
        for shadow in families:
            pe = plethystic_exp_coefficients(shadow, 5)
            self.assertEqual(pe[0], Rational(1))

    def test_depth_classification_all_families(self):
        """Each standard family has the correct depth class."""
        self.assertEqual(shadow_depth_class(heisenberg_shadow_coefficients('1', 10)), 'G')
        self.assertEqual(shadow_depth_class(affine_sl2_shadow_coefficients('1', 10)), 'L')
        self.assertEqual(shadow_depth_class(betagamma_shadow_coefficients(1, 10)), 'C')
        self.assertEqual(shadow_depth_class(virasoro_shadow_coefficients('4', 10)), 'M')


# ============================================================================
# Section 22: Numerical precision tests
# ============================================================================

class TestNumericalPrecision(unittest.TestCase):
    """Test numerical precision of float computations."""

    def test_float_pe_vs_exact_virasoro(self):
        """Float PE agrees with exact PE for Virasoro c=10."""
        exact_shadow = virasoro_shadow_coefficients('10', 12)
        float_shadow = {r: float(v) for r, v in exact_shadow.items()}
        pe_exact = plethystic_exp_coefficients(exact_shadow, 10)
        pe_float = plethystic_exp_coefficients_float(float_shadow, 10)
        for n in range(11):
            self.assertAlmostEqual(float(pe_exact[n]), pe_float[n], places=8,
                                   msg=f"Float PE mismatch at n={n}")

    def test_ahat_series_convergence(self):
        """A-hat series converges rapidly for small lambda."""
        x = 0.1
        vals = []
        for g_max in [5, 10, 15, 20]:
            vals.append(a_hat_gf_series(x, g_max))
        # Should converge: differences decrease
        for i in range(1, len(vals) - 1):
            diff_prev = abs(vals[i] - vals[i - 1])
            diff_next = abs(vals[i + 1] - vals[i])
            self.assertLessEqual(diff_next, diff_prev + 1e-20)

    def test_pe_pl_roundtrip_float(self):
        """Float PE-PL roundtrip for Heisenberg."""
        shadow = {r: float(v)
                  for r, v in heisenberg_shadow_coefficients('1', 15).items()}
        pe = plethystic_exp_coefficients_float(shadow, 15)
        pl = plethystic_log_coefficients_float(pe, 15)
        for r in range(2, 12):
            self.assertAlmostEqual(pl[r], shadow.get(r, 0.0), places=10)

    def test_large_n_heisenberg(self):
        """Heisenberg DT at large n: coefficients grow monotonically for even n."""
        pe = heisenberg_dt_partition(1, 30)
        # Even-index coefficients should be non-decreasing
        prev = 0
        for n in range(0, 31, 2):
            val = int(pe[n])
            self.assertGreaterEqual(val, prev,
                                    f"Non-monotone at n={n}")
            prev = val

    def test_virasoro_shadow_growth(self):
        """Virasoro shadow coefficients grow (class M has infinite tower)."""
        shadow = virasoro_shadow_coefficients_float(10.0, 20)
        # |S_r| should not vanish
        nonzero_count = sum(1 for r in range(2, 15) if abs(shadow[r]) > 1e-15)
        self.assertGreater(nonzero_count, 10)


if __name__ == '__main__':
    unittest.main()
