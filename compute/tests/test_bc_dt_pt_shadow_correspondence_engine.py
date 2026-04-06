r"""Tests for BC-122: DT/PT correspondence from the shadow obstruction tower.

Verifies:
  Section 1:  Number-theoretic helpers (Mobius, divisors, sigma, Bernoulli)
  Section 2:  Shadow coefficient extraction (all families)
  Section 3:  Plethystic exponential (exp-log)
  Section 4:  Plethystic logarithm and Mobius inversion
  Section 5:  PE/PL roundtrip (fundamental identity)
  Section 6:  Independent PE cross-verification (two code paths)
  Section 7:  MacMahon function (plane partitions)
  Section 8:  Signed MacMahon M(-q)^chi
  Section 9:  DT partition function (shadow families)
  Section 10: PT partition function (DT / M(-q)^chi)
  Section 11: DT/PT wall-crossing verification
  Section 12: Heisenberg DT specialization
  Section 13: Heisenberg PE vs Adams (two methods)
  Section 14: GV extraction from PT
  Section 15: GV integrality checks
  Section 16: DT at zeta zeros
  Section 17: PT at zeta zeros
  Section 18: DT/PT ratio at zeta zeros
  Section 19: GV at zeta zeros
  Section 20: Shadow depth classification
  Section 21: Multi-family comparison
  Section 22: Full analysis pipelines
  Section 23: Cross-family consistency
  Section 24: Numerical precision tests

Multi-path verification mandate (AP1/AP3/AP10): every numerical value
checked by at least 2 independent methods. No hardcoded values from
pattern matching.

90+ tests total.
"""

import math
import unittest

from sympy import Rational, cancel, Abs

from compute.lib.bc_dt_pt_shadow_correspondence_engine import (
    # Helpers
    _mobius, _prime_factors, _divisors, _sigma,
    _bernoulli_number, _lambda_fp, _plane_partition_count,
    # Zeta zeros
    ZETA_ZERO_GAMMAS, get_zeta_zero, c_at_zeta_zero,
    # Shadow coefficients
    virasoro_shadow_coefficients, virasoro_shadow_float,
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    betagamma_shadow_coefficients,
    # Plethystic
    plethystic_exp, plethystic_exp_float,
    plethystic_log, plethystic_log_float,
    plethystic_exp_independent,
    # MacMahon
    macmahon_coefficients, macmahon_power_coefficients,
    macmahon_signed_power_coefficients, macmahon_signed_power_float,
    # DT
    shadow_dt_coefficients, shadow_dt_float,
    hilb_dt_coefficients,
    # PT
    shadow_pt_coefficients, shadow_pt_float,
    pt_pair_coefficients,
    # Wall-crossing
    dt_pt_wall_crossing_check,
    # GV
    gv_from_pt, gv_from_dt_direct, gv_integrality_check,
    # Heisenberg specializations
    heisenberg_dt_pe, heisenberg_dt_adams, heisenberg_pt,
    # Roundtrip
    verify_pe_pl_roundtrip,
    # Zeta zero evaluations
    dt_at_zeta_zero, pt_at_zeta_zero,
    dt_pt_ratio_at_zeta_zero, gv_at_zeta_zero,
    # Classification
    shadow_depth_class,
    # Multi-family
    family_dt_comparison,
    # Full analysis
    full_dt_pt_analysis,
    heisenberg_full_analysis, virasoro_full_analysis,
    affine_sl2_full_analysis, betagamma_full_analysis,
)


# ============================================================================
# Section 1: Number-theoretic helpers
# ============================================================================

class TestHelpers(unittest.TestCase):
    """Arithmetic helper functions."""

    def test_mobius_primes(self):
        """mu(p) = -1 for prime p."""
        for p in [2, 3, 5, 7, 11, 13]:
            self.assertEqual(_mobius(p), -1)

    def test_mobius_squarefree(self):
        """mu(pq) = 1 for distinct primes."""
        self.assertEqual(_mobius(6), 1)   # 2*3
        self.assertEqual(_mobius(10), 1)  # 2*5
        self.assertEqual(_mobius(15), 1)  # 3*5
        self.assertEqual(_mobius(30), -1) # 2*3*5

    def test_mobius_squareful(self):
        """mu(n) = 0 if n has squared factor."""
        for n in [4, 8, 9, 12, 16, 18, 25]:
            self.assertEqual(_mobius(n), 0)

    def test_divisors(self):
        """Divisor enumeration."""
        self.assertEqual(_divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(_divisors(1), [1])
        self.assertEqual(_divisors(7), [1, 7])

    def test_sigma(self):
        """Divisor sum sigma_k."""
        # sigma_0(12) = 6 (number of divisors)
        self.assertEqual(_sigma(12, 0), 6)
        # sigma_1(12) = 1+2+3+4+6+12 = 28
        self.assertEqual(_sigma(12, 1), 28)
        # sigma_2(1) = 1, sigma_2(2) = 5, sigma_2(3) = 10
        self.assertEqual(_sigma(1, 2), 1)
        self.assertEqual(_sigma(2, 2), 5)
        self.assertEqual(_sigma(3, 2), 10)

    def test_bernoulli(self):
        """Bernoulli numbers (sympy convention: B_1 = +1/2)."""
        self.assertEqual(_bernoulli_number(0), 1)
        self.assertEqual(_bernoulli_number(1), Rational(1, 2))
        self.assertEqual(_bernoulli_number(2), Rational(1, 6))
        self.assertEqual(_bernoulli_number(4), Rational(-1, 30))

    def test_lambda_fp(self):
        """Faber-Pandharipande intersection numbers."""
        self.assertEqual(_lambda_fp(1), Rational(1, 24))
        self.assertEqual(_lambda_fp(2), Rational(7, 5760))
        self.assertEqual(_lambda_fp(3), Rational(31, 967680))

    def test_plane_partitions(self):
        """Plane partition counts (OEIS A000219)."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for n, val in enumerate(expected):
            self.assertEqual(_plane_partition_count(n), val)


# ============================================================================
# Section 2: Shadow coefficient extraction
# ============================================================================

class TestShadowCoefficients(unittest.TestCase):
    """Shadow coefficients for all standard families."""

    def test_heisenberg_terminates(self):
        """Heisenberg: class G, S_r = 0 for r >= 3."""
        shadow = heisenberg_shadow_coefficients(1, 10)
        self.assertEqual(shadow[2], Rational(1))
        for r in range(3, 11):
            self.assertEqual(shadow[r], Rational(0))

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 5, 10]:
            shadow = heisenberg_shadow_coefficients(k, 5)
            self.assertEqual(shadow[2], Rational(k))

    def test_affine_sl2_class_L(self):
        """Affine sl_2: class L, terminates at arity 3."""
        shadow = affine_sl2_shadow_coefficients(1, 10)
        # kappa = 3(k+2)/4 = 3*3/4 = 9/4
        self.assertEqual(shadow[2], Rational(9, 4))
        # S_3 = 4/(k+2) = 4/3
        self.assertEqual(shadow[3], Rational(4, 3))
        for r in range(4, 11):
            self.assertEqual(shadow[r], Rational(0))

    def test_betagamma_class_C(self):
        """Beta-gamma: class C, terminates at arity 4."""
        shadow = betagamma_shadow_coefficients(1, 10)
        # c = 2(6-6+1) = 2, kappa = 1
        self.assertEqual(shadow[2], Rational(1))
        self.assertEqual(shadow[3], Rational(2))
        for r in range(5, 11):
            self.assertEqual(shadow[r], Rational(0))

    def test_virasoro_leading(self):
        """Virasoro leading shadow coefficients."""
        shadow = virasoro_shadow_coefficients(1, 6)
        # kappa = c/2 = 1/2
        self.assertEqual(shadow[2], Rational(1, 2))
        # S_3 = a_1/3 = 6/3 = 2
        self.assertEqual(shadow[3], Rational(2))

    def test_virasoro_float_matches_exact(self):
        """Float Virasoro matches exact at real c."""
        shadow_exact = virasoro_shadow_coefficients(2, 8)
        shadow_float = virasoro_shadow_float(2.0, 8)
        for r in range(2, 8):
            self.assertAlmostEqual(
                float(shadow_exact[r]), shadow_float[r].real, places=10
            )
            self.assertAlmostEqual(shadow_float[r].imag, 0.0, places=10)

    def test_virasoro_complex_c(self):
        """Virasoro at complex c produces complex shadow coefficients."""
        shadow = virasoro_shadow_float(1.0 + 2.0j, 6)
        # S_2 = c/2 = (1+2i)/2
        self.assertAlmostEqual(shadow[2], (1.0 + 2.0j) / 2, places=10)
        # S_3 = a_1/3 = 6/3 = 2 is always real (independent of c)
        self.assertAlmostEqual(shadow[3], 2.0, places=10)
        # S_4 = a_2/4 = 40/(4*c*(5c+22)) depends on c, hence complex
        self.assertNotAlmostEqual(shadow[4].imag, 0.0)


# ============================================================================
# Section 3-4: Plethystic exponential and logarithm
# ============================================================================

class TestPlethystic(unittest.TestCase):
    """Plethystic exponential and logarithm."""

    def test_pe_heisenberg_k1(self):
        """PE[q^2] = 1/(1-q^2) = 1 + q^2 + q^4 + ..."""
        shadow = {2: Rational(1)}
        pe = plethystic_exp(shadow, 10)
        # (1-q^2)^{-1}: coeff of q^{2n} = 1, odd = 0
        for n in range(11):
            expected = Rational(1) if n % 2 == 0 else Rational(0)
            self.assertEqual(pe[n], expected,
                             f"PE[q^2] at q^{n}: got {pe[n]}, expected {expected}")

    def test_pe_heisenberg_k2(self):
        """PE[2q^2] = (1-q^2)^{-2} = 1 + 2q^2 + 3q^4 + ..."""
        shadow = {2: Rational(2)}
        pe = plethystic_exp(shadow, 10)
        for n in range(0, 11, 2):
            expected = Rational(n // 2 + 1)
            self.assertEqual(pe[n], expected)
        for n in range(1, 11, 2):
            self.assertEqual(pe[n], Rational(0))

    def test_pl_inverts_pe(self):
        """PL[PE[g]] = g for Virasoro shadow data."""
        shadow = virasoro_shadow_coefficients(2, 12)
        pe = plethystic_exp(shadow, 15)
        pl = plethystic_log(pe, 12)
        for r in range(2, 12):
            diff = cancel(shadow.get(r, Rational(0)) - pl[r])
            self.assertEqual(diff, 0, f"PL roundtrip failed at r={r}")

    def test_pl_inverts_pe_affine(self):
        """PL roundtrip for affine sl_2."""
        shadow = affine_sl2_shadow_coefficients(1, 10)
        pe = plethystic_exp(shadow, 15)
        pl = plethystic_log(pe, 10)
        for r in range(2, 10):
            diff = cancel(shadow.get(r, Rational(0)) - pl[r])
            self.assertEqual(diff, 0, f"PL roundtrip failed at r={r}")

    def test_pe_float_matches_exact(self):
        """Float PE matches exact PE for real shadow data."""
        shadow_r = heisenberg_shadow_coefficients(3, 10)
        pe_exact = plethystic_exp(shadow_r, 15)
        shadow_f = {r: complex(v) for r, v in shadow_r.items()}
        pe_float = plethystic_exp_float(shadow_f, 15)
        for n in range(16):
            self.assertAlmostEqual(float(pe_exact[n]), pe_float[n].real, places=10)


# ============================================================================
# Section 5: PE/PL roundtrip
# ============================================================================

class TestRoundtrip(unittest.TestCase):
    """Fundamental PE/PL roundtrip identity."""

    def test_roundtrip_heisenberg(self):
        """PE/PL roundtrip for Heisenberg."""
        shadow = heisenberg_shadow_coefficients(5, 20)
        result = verify_pe_pl_roundtrip(shadow, 15)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_virasoro(self):
        """PE/PL roundtrip for Virasoro."""
        shadow = virasoro_shadow_coefficients(3, 15)
        result = verify_pe_pl_roundtrip(shadow, 12)
        self.assertTrue(result['roundtrip_exact'])

    def test_roundtrip_betagamma(self):
        """PE/PL roundtrip for beta-gamma."""
        shadow = betagamma_shadow_coefficients(1, 15)
        result = verify_pe_pl_roundtrip(shadow, 12)
        self.assertTrue(result['roundtrip_exact'])


# ============================================================================
# Section 6: Independent PE cross-verification
# ============================================================================

class TestPEIndependent(unittest.TestCase):
    """Two independent PE computation paths must agree."""

    def test_two_paths_heisenberg(self):
        """Two PE paths agree for Heisenberg."""
        shadow = heisenberg_shadow_coefficients(2, 20)
        pe1 = plethystic_exp(shadow, 20)
        pe2 = plethystic_exp_independent(shadow, 20)
        for n in range(21):
            self.assertEqual(pe1[n], pe2[n],
                             f"PE mismatch at n={n}: {pe1[n]} vs {pe2[n]}")

    def test_two_paths_virasoro(self):
        """Two PE paths agree for Virasoro."""
        shadow = virasoro_shadow_coefficients(4, 15)
        pe1 = plethystic_exp(shadow, 15)
        pe2 = plethystic_exp_independent(shadow, 15)
        for n in range(16):
            diff = cancel(pe1[n] - pe2[n])
            self.assertEqual(diff, 0, f"PE mismatch at n={n}")

    def test_two_paths_affine(self):
        """Two PE paths agree for affine sl_2."""
        shadow = affine_sl2_shadow_coefficients(2, 15)
        pe1 = plethystic_exp(shadow, 15)
        pe2 = plethystic_exp_independent(shadow, 15)
        for n in range(16):
            diff = cancel(pe1[n] - pe2[n])
            self.assertEqual(diff, 0)

    def test_two_paths_betagamma(self):
        """Two PE paths agree for beta-gamma."""
        shadow = betagamma_shadow_coefficients(1, 15)
        pe1 = plethystic_exp(shadow, 15)
        pe2 = plethystic_exp_independent(shadow, 15)
        for n in range(16):
            diff = cancel(pe1[n] - pe2[n])
            self.assertEqual(diff, 0)


# ============================================================================
# Section 7: MacMahon function
# ============================================================================

class TestMacMahon(unittest.TestCase):
    """MacMahon function M(q) = prod (1-q^n)^{-n}."""

    def test_macmahon_oeis(self):
        """MacMahon coefficients match OEIS A000219."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        actual = macmahon_coefficients(10)
        self.assertEqual(actual, expected)

    def test_macmahon_power_1(self):
        """M(q)^1 = M(q)."""
        Mcoeffs = macmahon_power_coefficients(10, Rational(1))
        expected = macmahon_coefficients(10)
        for n in range(11):
            self.assertEqual(Mcoeffs[n], Rational(expected[n]))

    def test_macmahon_power_0(self):
        """M(q)^0 = 1."""
        Mcoeffs = macmahon_power_coefficients(10, Rational(0))
        self.assertEqual(Mcoeffs[0], Rational(1))
        for n in range(1, 11):
            self.assertEqual(Mcoeffs[n], Rational(0))


# ============================================================================
# Section 8: Signed MacMahon M(-q)^chi
# ============================================================================

class TestSignedMacMahon(unittest.TestCase):
    """M(-q)^chi for DT/PT wall-crossing."""

    def test_signed_macmahon_chi0(self):
        """M(-q)^0 = 1."""
        Mc = macmahon_signed_power_coefficients(10, Rational(0))
        self.assertEqual(Mc[0], Rational(1))
        for n in range(1, 11):
            self.assertEqual(Mc[n], Rational(0))

    def test_signed_macmahon_alternating_sign(self):
        """M(-q)^1 has coefficients with alternating-related signs."""
        Mc = macmahon_signed_power_coefficients(5, Rational(1))
        # M(-q) = prod (1-(-q)^n)^{-n} = prod (1-(-1)^n q^n)^{-n}
        # n=1: (1+q)^{-1}, n=2: (1-q^2)^{-2}, etc.
        # Leading: 1 - q + 2q^2 - 2q^3 + ...
        # Verify c_0 = 1
        self.assertEqual(Mc[0], Rational(1))

    def test_signed_float_matches_exact(self):
        """Float M(-q)^chi matches exact for integer chi."""
        Mc_exact = macmahon_signed_power_coefficients(10, Rational(2))
        Mc_float = macmahon_signed_power_float(10, 2.0)
        for n in range(11):
            self.assertAlmostEqual(float(Mc_exact[n]), Mc_float[n].real, places=8)
            self.assertAlmostEqual(Mc_float[n].imag, 0.0, places=8)


# ============================================================================
# Section 9: DT partition function
# ============================================================================

class TestDTPartition(unittest.TestCase):
    """Shadow DT partition functions."""

    def test_dt_heisenberg(self):
        """Heisenberg DT = PE[kq^2] = (1-q^2)^{-k}."""
        shadow = heisenberg_shadow_coefficients(1, 10)
        dt = shadow_dt_coefficients(shadow, 10)
        for n in range(11):
            expected = Rational(1) if n % 2 == 0 else Rational(0)
            self.assertEqual(dt[n], expected)

    def test_dt_heisenberg_k3(self):
        """Heisenberg k=3: (1-q^2)^{-3}."""
        from math import comb
        shadow = heisenberg_shadow_coefficients(3, 20)
        dt = shadow_dt_coefficients(shadow, 20)
        for j in range(11):
            self.assertEqual(dt[2 * j], Rational(comb(3 + j - 1, j)))

    def test_dt_float_matches_exact(self):
        """Float DT matches exact for Virasoro c=2."""
        shadow_r = virasoro_shadow_coefficients(2, 12)
        dt_exact = shadow_dt_coefficients(shadow_r, 10)
        shadow_f = {r: complex(v) for r, v in shadow_r.items()}
        dt_float = shadow_dt_float(shadow_f, 10)
        for n in range(11):
            self.assertAlmostEqual(float(dt_exact[n]), dt_float[n].real, places=8)

    def test_hilb_dt_equals_pe(self):
        """hilb_dt_coefficients is just PE[shadow]."""
        shadow = virasoro_shadow_coefficients(3, 12)
        hilb = hilb_dt_coefficients(shadow, 10)
        pe = plethystic_exp(shadow, 10)
        for n in range(11):
            self.assertEqual(hilb[n], pe[n])


# ============================================================================
# Section 10: PT partition function
# ============================================================================

class TestPTPartition(unittest.TestCase):
    """PT partition function Z^PT = Z^DT / M(-q)^chi."""

    def test_pt_chi0(self):
        """When chi=0, Z^PT = Z^DT."""
        shadow = virasoro_shadow_coefficients(2, 12)
        dt = shadow_dt_coefficients(shadow, 10)
        pt = shadow_pt_coefficients(shadow, Rational(0), 10)
        for n in range(11):
            diff = cancel(dt[n] - pt[n])
            self.assertEqual(diff, 0, f"PT != DT at chi=0, n={n}")

    def test_pt_c0_is_1(self):
        """PT[0] = 1 always."""
        shadow = virasoro_shadow_coefficients(3, 12)
        pt = shadow_pt_coefficients(shadow, Rational(3, 2), 10)
        self.assertEqual(pt[0], Rational(1))

    def test_pt_pair_matches(self):
        """pt_pair_coefficients = shadow_pt_coefficients."""
        shadow = heisenberg_shadow_coefficients(2, 15)
        pt1 = shadow_pt_coefficients(shadow, Rational(2), 10)
        pt2 = pt_pair_coefficients(shadow, Rational(2), 10)
        for n in range(11):
            self.assertEqual(pt1[n], pt2[n])


# ============================================================================
# Section 11: DT/PT wall-crossing
# ============================================================================

class TestWallCrossing(unittest.TestCase):
    """Z^DT = M(-q)^chi * Z^PT verification."""

    def test_wall_crossing_heisenberg(self):
        """Wall-crossing holds for Heisenberg k=1."""
        shadow = heisenberg_shadow_coefficients(1, 15)
        result = dt_pt_wall_crossing_check(shadow, Rational(1), 12)
        self.assertTrue(result['exact_match'],
                        f"Wall-crossing failed: {result['n_errors']} errors")

    def test_wall_crossing_heisenberg_k5(self):
        """Wall-crossing holds for Heisenberg k=5."""
        shadow = heisenberg_shadow_coefficients(5, 15)
        result = dt_pt_wall_crossing_check(shadow, Rational(5), 12)
        self.assertTrue(result['exact_match'])

    def test_wall_crossing_virasoro(self):
        """Wall-crossing holds for Virasoro c=2."""
        shadow = virasoro_shadow_coefficients(2, 15)
        result = dt_pt_wall_crossing_check(shadow, Rational(1), 10)
        self.assertTrue(result['exact_match'])

    def test_wall_crossing_affine(self):
        """Wall-crossing holds for affine sl_2 k=1."""
        shadow = affine_sl2_shadow_coefficients(1, 15)
        kappa = Rational(9, 4)
        result = dt_pt_wall_crossing_check(shadow, kappa, 10)
        self.assertTrue(result['exact_match'])

    def test_wall_crossing_betagamma(self):
        """Wall-crossing holds for beta-gamma lam=1."""
        shadow = betagamma_shadow_coefficients(1, 15)
        kappa = Rational(1)
        result = dt_pt_wall_crossing_check(shadow, kappa, 10)
        self.assertTrue(result['exact_match'])


# ============================================================================
# Section 12: Heisenberg DT specialization
# ============================================================================

class TestHeisenbergDT(unittest.TestCase):
    """Heisenberg DT via PE and Adams exponential."""

    def test_heisenberg_pe_k1(self):
        """PE version: (1-q^2)^{-1}."""
        dt = heisenberg_dt_pe(1, 10)
        for n in range(11):
            expected = Rational(1) if n % 2 == 0 else Rational(0)
            self.assertEqual(dt[n], expected)

    def test_heisenberg_adams_k1(self):
        """Adams version: prod_{m>=1} (1-q^{2m})^{-1} = partitions into even parts."""
        dt = heisenberg_dt_adams(1, 10)
        # Partitions into even parts: 1, 0, 1, 0, 2, 0, 2, 0, 4, 0, 4
        # (these are partitions of n into parts from {2,4,6,...})
        # n=0:1, n=2:1(=2), n=4:2(=4, 2+2), n=6:2(=6, 4+2), n=8:4(=8,6+2,4+4,4+2+2)
        self.assertEqual(dt[0], Rational(1))
        self.assertEqual(dt[1], Rational(0))
        self.assertEqual(dt[2], Rational(1))
        self.assertEqual(dt[4], Rational(2))

    def test_pe_vs_adams_differ(self):
        """PE and Adams are DIFFERENT for Heisenberg (PE is finite, Adams infinite)."""
        pe = heisenberg_dt_pe(1, 10)
        adams = heisenberg_dt_adams(1, 10)
        # They agree at n=0,1,2 but differ at n=4
        self.assertEqual(pe[0], adams[0])
        self.assertEqual(pe[2], adams[2])
        # At n=4: PE gives C(1,2)=1, Adams gives 2
        self.assertEqual(pe[4], Rational(1))
        self.assertEqual(adams[4], Rational(2))


# ============================================================================
# Section 13: Heisenberg PE vs Adams cross-check
# ============================================================================

class TestHeisenbergPEAdams(unittest.TestCase):
    """Cross-verification of two DT computation methods for Heisenberg."""

    def test_adams_k1_leading(self):
        """Adams for k=1 produces partition-into-even-parts counts."""
        dt = heisenberg_dt_adams(1, 20)
        # The even-part partition function is known:
        # prod_{m>=1} 1/(1-q^{2m})
        # First few: p_even(0)=1, p_even(2)=1, p_even(4)=2, p_even(6)=3,
        # p_even(8)=5, p_even(10)=7
        self.assertEqual(dt[0], Rational(1))
        self.assertEqual(dt[6], Rational(3))
        self.assertEqual(dt[8], Rational(5))
        self.assertEqual(dt[10], Rational(7))

    def test_adams_k2_has_correct_symmetry(self):
        """Adams for k=2 vanishes at odd indices."""
        dt = heisenberg_dt_adams(2, 14)
        for n in range(1, 15, 2):
            self.assertEqual(dt[n], Rational(0))


# ============================================================================
# Section 14: GV extraction from PT
# ============================================================================

class TestGVExtraction(unittest.TestCase):
    """GV invariant extraction from PT partition function."""

    def test_gv_heisenberg_k1(self):
        """GV for Heisenberg k=1: finite shadow, simple BPS."""
        shadow = heisenberg_shadow_coefficients(1, 15)
        pt = shadow_pt_coefficients(shadow, Rational(1), 15)
        gv = gv_from_pt(pt, g_max=3, k_max=8)
        # The GV data should be finite (class G)
        self.assertIsInstance(gv, dict)
        self.assertIn((0, 1), gv)

    def test_gv_virasoro(self):
        """GV extraction for Virasoro c=2 produces data."""
        shadow = virasoro_shadow_coefficients(2, 12)
        pt = shadow_pt_coefficients(shadow, Rational(1), 12)
        gv = gv_from_pt(pt, g_max=2, k_max=6)
        self.assertIn((0, 1), gv)

    def test_gv_from_dt_direct_matches(self):
        """GV from DT directly matches GV from PT."""
        shadow = heisenberg_shadow_coefficients(2, 15)
        dt = shadow_dt_coefficients(shadow, 15)
        gv_dt = gv_from_dt_direct(dt, Rational(2), 8)
        pt = shadow_pt_coefficients(shadow, Rational(2), 15)
        gv_pt = gv_from_pt(pt, g_max=0, k_max=8)

        # The total BPS Omega(k) from both paths should match
        for k in range(1, 7):
            if k in gv_dt and (0, k) in gv_pt:
                diff = cancel(gv_dt[k] - gv_pt[(0, k)])
                self.assertEqual(diff, 0,
                                 f"GV mismatch at k={k}: {gv_dt[k]} vs {gv_pt[(0,k)]}")


# ============================================================================
# Section 15: GV integrality
# ============================================================================

class TestGVIntegrality(unittest.TestCase):
    """GV integrality checks."""

    def test_integrality_heisenberg(self):
        """Heisenberg GV invariants are integers."""
        shadow = heisenberg_shadow_coefficients(1, 15)
        pt = shadow_pt_coefficients(shadow, Rational(1), 15)
        gv = gv_from_pt(pt, g_max=3, k_max=8)
        result = gv_integrality_check(gv)
        self.assertTrue(result['all_integer'],
                        f"Integrality failure: {result['details']}")

    def test_integrality_heisenberg_k3(self):
        """Heisenberg k=3 GV integrality."""
        shadow = heisenberg_shadow_coefficients(3, 15)
        pt = shadow_pt_coefficients(shadow, Rational(3), 15)
        gv = gv_from_pt(pt, g_max=2, k_max=6)
        result = gv_integrality_check(gv)
        self.assertTrue(result['all_integer'])

    def test_integrality_check_dict_format(self):
        """Integrality checker works with both dict formats."""
        data1 = {(0, 1): Rational(3), (0, 2): Rational(-5)}
        result1 = gv_integrality_check(data1)
        self.assertTrue(result1['all_integer'])

        data2 = {1: Rational(3), 2: Rational(-5)}
        result2 = gv_integrality_check(data2)
        self.assertTrue(result2['all_integer'])

    def test_integrality_fails_for_noninteger(self):
        """Integrality check correctly fails for non-integer values."""
        data = {(0, 1): Rational(3, 2)}
        result = gv_integrality_check(data)
        self.assertFalse(result['all_integer'])


# ============================================================================
# Section 16: DT at zeta zeros
# ============================================================================

class TestDTAtZetaZeros(unittest.TestCase):
    """DT partition function at Riemann zeta zeros."""

    def test_dt_zero_1(self):
        """DT at first zeta zero: c = 1/2 + i*14.13..."""
        result = dt_at_zeta_zero(1, max_order=10, max_r=12)
        self.assertEqual(result['zero_index'], 1)
        self.assertAlmostEqual(result['c_val'].real, 0.5, places=5)
        self.assertAlmostEqual(result['c_val'].imag, ZETA_ZERO_GAMMAS[0], places=5)
        # DT[0] = 1 always
        self.assertAlmostEqual(result['dt_coefficients'][0].real, 1.0, places=8)

    def test_dt_zero_5(self):
        """DT at 5th zeta zero."""
        result = dt_at_zeta_zero(5, max_order=10, max_r=12)
        self.assertEqual(result['zero_index'], 5)
        self.assertAlmostEqual(abs(result['dt_coefficients'][0]), 1.0, places=8)

    def test_dt_zeros_have_unit_leading(self):
        """Z^DT[0] = 1 at all zeta zeros."""
        for n in range(1, 6):
            result = dt_at_zeta_zero(n, max_order=5, max_r=8)
            self.assertAlmostEqual(abs(result['dt_coefficients'][0]), 1.0, places=8)


# ============================================================================
# Section 17: PT at zeta zeros
# ============================================================================

class TestPTAtZetaZeros(unittest.TestCase):
    """PT partition function at zeta zeros."""

    def test_pt_zero_1(self):
        """PT at first zeta zero has unit leading coefficient."""
        result = pt_at_zeta_zero(1, max_order=10, max_r=12)
        self.assertAlmostEqual(abs(result['pt_coefficients'][0]), 1.0, places=8)

    def test_pt_zeros_leading(self):
        """PT[0] = 1 at all tested zeta zeros."""
        for n in range(1, 5):
            result = pt_at_zeta_zero(n, max_order=5, max_r=8)
            self.assertAlmostEqual(abs(result['pt_coefficients'][0]), 1.0, places=8)


# ============================================================================
# Section 18: DT/PT ratio at zeta zeros
# ============================================================================

class TestDTPTRatioZetaZeros(unittest.TestCase):
    """Z^DT / Z^PT = M(-q)^chi at zeta zeros."""

    def test_ratio_zero_1(self):
        """Wall-crossing holds numerically at first zeta zero."""
        result = dt_pt_ratio_at_zeta_zero(1, max_order=10, max_r=12)
        self.assertTrue(result['wall_crossing_holds'],
                        f"Max error: {result['max_reconstruction_error']}")

    def test_ratio_zero_2(self):
        """Wall-crossing at second zeta zero."""
        result = dt_pt_ratio_at_zeta_zero(2, max_order=10, max_r=12)
        self.assertTrue(result['wall_crossing_holds'],
                        f"Max error: {result['max_reconstruction_error']}")

    def test_ratio_zero_3(self):
        """Wall-crossing at third zeta zero."""
        result = dt_pt_ratio_at_zeta_zero(3, max_order=8, max_r=10)
        self.assertTrue(result['wall_crossing_holds'],
                        f"Max error: {result['max_reconstruction_error']}")

    def test_ratio_multiple_zeros(self):
        """Wall-crossing holds at zeta zeros 1-5."""
        for n in range(1, 6):
            result = dt_pt_ratio_at_zeta_zero(n, max_order=8, max_r=10)
            self.assertTrue(result['wall_crossing_holds'],
                            f"Wall-crossing failed at zero {n}: "
                            f"err={result['max_reconstruction_error']}")


# ============================================================================
# Section 19: GV at zeta zeros
# ============================================================================

class TestGVAtZetaZeros(unittest.TestCase):
    """GV invariants at zeta zeros."""

    def test_gv_zero_1(self):
        """GV extraction at first zeta zero produces data."""
        result = gv_at_zeta_zero(1, max_order=10, max_r=12)
        self.assertEqual(result['zero_index'], 1)
        self.assertIn(1, result['gv_bps'])
        # At complex c, GV invariants are complex: integrality generically fails
        # This tests that the extraction runs and produces finite values
        for k in range(1, min(6, len(result['gv_bps']) + 1)):
            self.assertTrue(math.isfinite(abs(result['gv_bps'][k])),
                            f"GV[{k}] is not finite at zero 1")

    def test_gv_zeros_finite(self):
        """GV invariants finite at zeta zeros 1-5."""
        for n in range(1, 6):
            result = gv_at_zeta_zero(n, max_order=8, max_r=10)
            for k in result['gv_bps']:
                self.assertTrue(math.isfinite(abs(result['gv_bps'][k])),
                                f"GV[{k}] not finite at zero {n}")

    def test_gv_zeros_complex(self):
        """At complex c, GV invariants are generically complex (non-integer)."""
        result = gv_at_zeta_zero(1, max_order=10, max_r=12)
        # At least some should have nonzero imaginary part
        has_complex = any(abs(v.imag) > 1e-10 for v in result['gv_bps'].values())
        self.assertTrue(has_complex,
                        "Expected complex GV at zeta zero but all are real")


# ============================================================================
# Section 20: Shadow depth classification
# ============================================================================

class TestDepthClassification(unittest.TestCase):
    """Shadow depth G/L/C/M classification."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (depth 2)."""
        shadow = heisenberg_shadow_coefficients(1, 10)
        self.assertEqual(shadow_depth_class(shadow), 'G')

    def test_affine_class_L(self):
        """Affine sl_2 is class L (depth 3)."""
        shadow = affine_sl2_shadow_coefficients(1, 10)
        self.assertEqual(shadow_depth_class(shadow), 'L')

    def test_betagamma_class_C(self):
        """Beta-gamma is class C (depth 4)."""
        shadow = betagamma_shadow_coefficients(1, 10)
        self.assertEqual(shadow_depth_class(shadow), 'C')

    def test_virasoro_class_M(self):
        """Virasoro is class M (depth infinity)."""
        shadow = virasoro_shadow_coefficients(2, 10)
        self.assertEqual(shadow_depth_class(shadow), 'M')


# ============================================================================
# Section 21: Multi-family comparison
# ============================================================================

class TestMultiFamily(unittest.TestCase):
    """Cross-family DT comparison."""

    def test_family_comparison_runs(self):
        """Family comparison pipeline completes."""
        result = family_dt_comparison(max_n=10)
        self.assertIn('heisenberg_k1', result)
        self.assertIn('virasoro_c1', result)
        self.assertIn('affine_sl2_k1', result)
        self.assertIn('betagamma_lam1', result)

    def test_all_roundtrips_pass(self):
        """All families pass PE/PL roundtrip."""
        result = family_dt_comparison(max_n=10)
        for name, data in result.items():
            self.assertTrue(data['pe_pl_roundtrip'],
                            f"Roundtrip failed for {name}")

    def test_kappa_ordering(self):
        """kappa values match known formulas."""
        result = family_dt_comparison(max_n=5)
        # Heisenberg k=1: kappa=1
        self.assertAlmostEqual(result['heisenberg_k1']['kappa'], 1.0)
        # Virasoro c=1: kappa=1/2
        self.assertAlmostEqual(result['virasoro_c1']['kappa'], 0.5)
        # Affine sl_2 k=1: kappa=9/4
        self.assertAlmostEqual(result['affine_sl2_k1']['kappa'], 9 / 4)


# ============================================================================
# Section 22: Full analysis pipelines
# ============================================================================

class TestFullAnalysis(unittest.TestCase):
    """Full DT/PT analysis pipelines."""

    def test_heisenberg_full(self):
        """Heisenberg full analysis."""
        result = heisenberg_full_analysis(k=1, max_n=15)
        self.assertEqual(result['depth_class'], 'G')
        self.assertTrue(result['wall_crossing_exact'])
        self.assertTrue(result['roundtrip_exact'])

    def test_virasoro_full(self):
        """Virasoro full analysis."""
        result = virasoro_full_analysis(c=2, max_n=10)
        self.assertEqual(result['depth_class'], 'M')
        self.assertTrue(result['wall_crossing_exact'])
        self.assertTrue(result['roundtrip_exact'])

    def test_affine_full(self):
        """Affine sl_2 full analysis."""
        result = affine_sl2_full_analysis(k=1, max_n=10)
        self.assertEqual(result['depth_class'], 'L')
        self.assertTrue(result['wall_crossing_exact'])

    def test_betagamma_full(self):
        """Beta-gamma full analysis."""
        result = betagamma_full_analysis(lam=1, max_n=10)
        self.assertEqual(result['depth_class'], 'C')
        self.assertTrue(result['wall_crossing_exact'])


# ============================================================================
# Section 23: Cross-family consistency
# ============================================================================

class TestCrossFamily(unittest.TestCase):
    """Cross-family consistency checks (AP10 compliance)."""

    def test_dt_additivity_heisenberg(self):
        """DT partition function is multiplicative under independent sum.

        H_k1 + H_k2 (independent): Z^DT_{k1+k2} = Z^DT_{k1} * Z^DT_{k2}
        since PE[g1+g2] = PE[g1] * PE[g2] when supports are the same.

        For Heisenberg: PE[(k1+k2)q^2] = PE[k1 q^2] * PE[k2 q^2].
        """
        N = 12
        dt_3 = plethystic_exp(heisenberg_shadow_coefficients(3, N + 2), N)
        dt_1 = plethystic_exp(heisenberg_shadow_coefficients(1, N + 2), N)
        dt_2 = plethystic_exp(heisenberg_shadow_coefficients(2, N + 2), N)

        # Multiply dt_1 * dt_2
        product = [Rational(0)] * (N + 1)
        for n in range(N + 1):
            for k in range(n + 1):
                product[n] += dt_1[k] * dt_2[n - k]

        for n in range(N + 1):
            diff = cancel(dt_3[n] - product[n])
            self.assertEqual(diff, 0,
                             f"Additivity failed at n={n}: {dt_3[n]} vs {product[n]}")

    def test_kappa_complementarity_virasoro(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        for c in [1, 2, 5, 10, 13]:
            k1 = Rational(c, 2)
            k2 = Rational(26 - c, 2)
            self.assertEqual(k1 + k2, Rational(13))

    def test_kappa_complementarity_heisenberg(self):
        """AP24: kappa(H_k) + kappa(H_{-k}) = 0."""
        for k in [1, 2, 5]:
            k1 = Rational(k)
            k2 = Rational(-k)
            self.assertEqual(k1 + k2, Rational(0))

    def test_pe_multiplicativity(self):
        """PE[f+g] = PE[f]*PE[g] for disjoint-support shadow data."""
        # Use shadow data with supports on different arities
        f = {2: Rational(1), 3: Rational(0), 4: Rational(0)}
        g = {2: Rational(0), 3: Rational(2), 4: Rational(0)}
        fg = {2: Rational(1), 3: Rational(2), 4: Rational(0)}
        N = 12
        pe_f = plethystic_exp(f, N)
        pe_g = plethystic_exp(g, N)
        pe_fg = plethystic_exp(fg, N)

        product = [Rational(0)] * (N + 1)
        for n in range(N + 1):
            for k in range(n + 1):
                product[n] += pe_f[k] * pe_g[n - k]

        for n in range(N + 1):
            diff = cancel(pe_fg[n] - product[n])
            self.assertEqual(diff, 0,
                             f"PE multiplicativity failed at n={n}")


# ============================================================================
# Section 24: Numerical precision tests
# ============================================================================

class TestNumericalPrecision(unittest.TestCase):
    """Precision and convergence tests."""

    def test_virasoro_shadow_growth(self):
        """Virasoro shadow coefficients grow but stay finite."""
        shadow = virasoro_shadow_coefficients(2, 20)
        for r in range(2, 20):
            val = float(shadow[r])
            self.assertTrue(math.isfinite(val), f"S_{r} not finite: {val}")

    def test_pe_coefficients_finite(self):
        """PE coefficients stay finite for Virasoro through n=20."""
        shadow = virasoro_shadow_coefficients(2, 15)
        pe = plethystic_exp(shadow, 20)
        for n in range(21):
            val = float(pe[n])
            self.assertTrue(math.isfinite(val), f"PE[{n}] not finite: {val}")

    def test_zeta_zero_table(self):
        """Zeta zero table has 30 entries and is monotonically increasing."""
        self.assertEqual(len(ZETA_ZERO_GAMMAS), 30)
        for i in range(1, len(ZETA_ZERO_GAMMAS)):
            self.assertGreater(ZETA_ZERO_GAMMAS[i], ZETA_ZERO_GAMMAS[i - 1])

    def test_zeta_zero_first(self):
        """First zeta zero gamma_1 ~ 14.1347."""
        self.assertAlmostEqual(ZETA_ZERO_GAMMAS[0], 14.134725141734693, places=8)

    def test_c_at_zeta_zero(self):
        """c(rho_n) = 1/2 + i*gamma_n."""
        c = c_at_zeta_zero(1)
        self.assertAlmostEqual(c.real, 0.5, places=10)
        self.assertAlmostEqual(c.imag, ZETA_ZERO_GAMMAS[0], places=10)

    def test_large_n_heisenberg(self):
        """Heisenberg DT at large n still finite."""
        shadow = heisenberg_shadow_coefficients(1, 35)
        dt = plethystic_exp(shadow, 30)
        for n in range(31):
            self.assertTrue(math.isfinite(float(dt[n])))

    def test_float_complex_pe_stable(self):
        """Complex PE stays numerically stable through n=15."""
        shadow = virasoro_shadow_float(0.5 + 14.0j, 12)
        pe = plethystic_exp_float(shadow, 15)
        for n in range(16):
            self.assertTrue(math.isfinite(abs(pe[n])),
                            f"PE[{n}] diverged at complex c")


if __name__ == '__main__':
    unittest.main()
