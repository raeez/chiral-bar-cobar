r"""Tests for CY-18: DT invariants of K3 x E (Oberdieck-Pandharipande).

Verifies:
  Section 1:  Arithmetic helpers (divisors, sigma, partitions, plane partitions)
  Section 2:  K3 elliptic genus phi_{0,1} coefficients
  Section 3:  phi_{0,1} sum constraint and symmetry
  Section 4:  phi_{0,1} numerical verification (theta functions)
  Section 5:  K3 elliptic genus = 2*phi_{0,1}
  Section 6:  Euler characteristics (K3, K3 x E)
  Section 7:  Hilbert scheme chi(Hilb^n(K3)) — recurrence
  Section 8:  Hilbert scheme — direct product expansion (cross-check)
  Section 9:  Hilbert scheme — OEIS A006922 verification
  Section 10: MacMahon function (plane partitions)
  Section 11: DT degree-0 for K3 x E (MNOP: M(-q)^0 = 1)
  Section 12: Yau-Zaslow genus-0 GV invariants
  Section 13: Yau-Zaslow = Hilbert scheme (two independent computations)
  Section 14: DT/PT correspondence (chi = 0)
  Section 15: Motivic DT (degree 0)
  Section 16: Shadow tower: kappa
  Section 17: Shadow tower: F_g and lambda_g^FP
  Section 18: Shadow tower: multi-genus consistency
  Section 19: Topological string free energy F_0
  Section 20: GV integrality
  Section 21: KKV genus-1 invariants
  Section 22: Full analysis pipeline
  Section 23: Cross-check battery (all paths)
  Section 24: Numerical phi_{0,1} evaluation
  Section 25: Bernoulli number verification
  Section 26: Goettsche formula structural tests

Multi-path verification (AP1/AP3/AP10): every value checked by at least
2 independent methods. No hardcoded values from pattern matching.

100+ tests total.
"""

import math
import unittest
from fractions import Fraction

from compute.lib.cy_dt_k3e_engine import (
    # Arithmetic helpers
    _divisors, _sigma, _partition_number, _plane_partition_count,
    _convolve_int, _bernoulli_number_frac,
    # phi_{0,1}
    phi01_fourier, phi01_fourier_safe, phi01_sum_check,
    k3_elliptic_genus_coeff,
    # Euler characteristics
    k3_euler_characteristic, k3xe_euler_characteristic,
    # Hilbert scheme
    hilb_k3_euler_char, hilb_k3_partition_function, hilb_k3_via_product,
    # MacMahon
    macmahon_coeffs,
    # DT degree-0
    dt_degree0_k3xe,
    # Yau-Zaslow / KKV
    yau_zaslow_genus0, kkv_genus1_invariants,
    # DT/PT
    dt_equals_pt_k3xe,
    # Shadow tower
    shadow_kappa_k3xe, shadow_kappa_k3_relative,
    shadow_f1_k3xe, shadow_f1_k3_relative,
    shadow_fg_k3_relative, lambda_fp,
    # GV
    gv_integrality_check_yz,
    # Motivic DT
    motivic_dt_degree0,
    # Topological string
    topological_string_f0,
    # Numerical
    phi01_numerical,
    # Cross-checks
    cross_check_yz_equals_hilb,
    cross_check_hilb_two_methods,
    cross_check_dt_pt,
    cross_check_mnop_degree0,
    cross_check_shadow_f1,
    cross_check_gv_integrality,
    cross_check_phi01_sum,
    cross_check_phi01_symmetry,
    cross_check_k3_eg_at_origin,
    # Full analysis
    full_analysis,
)


# ============================================================================
# Section 1: Arithmetic helpers
# ============================================================================

class TestArithmeticHelpers(unittest.TestCase):
    """Section 1: divisors, sigma, partitions, plane partitions."""

    def test_divisors_1(self):
        self.assertEqual(_divisors(1), [1])

    def test_divisors_6(self):
        self.assertEqual(_divisors(6), [1, 2, 3, 6])

    def test_divisors_12(self):
        self.assertEqual(_divisors(12), [1, 2, 3, 4, 6, 12])

    def test_divisors_prime(self):
        self.assertEqual(_divisors(13), [1, 13])

    def test_sigma_0(self):
        """sigma_0(n) = number of divisors."""
        self.assertEqual(_sigma(6, 0), 4)

    def test_sigma_1(self):
        """sigma_1(6) = 1+2+3+6 = 12."""
        self.assertEqual(_sigma(6, 1), 12)

    def test_sigma_2(self):
        """sigma_2(4) = 1+4+16 = 21."""
        self.assertEqual(_sigma(4, 2), 21)

    def test_partition_small(self):
        """Integer partitions: p(0)=1, p(1)=1, ..., p(5)=7."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
        for n, exp in enumerate(expected):
            self.assertEqual(_partition_number(n), exp, f"p({n})")

    def test_plane_partition_small(self):
        """Plane partitions: OEIS A000219."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282]
        for n, exp in enumerate(expected):
            self.assertEqual(_plane_partition_count(n), exp, f"pp({n})")

    def test_plane_partition_recurrence_vs_oeis(self):
        """Cross-check pp(10) = 500."""
        self.assertEqual(_plane_partition_count(10), 500)

    def test_convolve_identity(self):
        """Convolve with [1] is identity."""
        a = [1, 2, 3]
        b = [1]
        self.assertEqual(_convolve_int(a, b, 3), [1, 2, 3])

    def test_convolve_shift(self):
        """Convolve [1,0,0] * [0,1,0] = [0,1,0]."""
        a = [1, 0, 0]
        b = [0, 1, 0]
        self.assertEqual(_convolve_int(a, b, 4), [0, 1, 0, 0])


# ============================================================================
# Section 2: phi_{0,1} Fourier coefficients
# ============================================================================

class TestPhi01Coefficients(unittest.TestCase):
    """Section 2: phi_{0,1} Fourier expansion."""

    def test_c00(self):
        """c(0, 0) = 10."""
        self.assertEqual(phi01_fourier(0, 0), 10)

    def test_c01(self):
        """c(0, 1) = 1."""
        self.assertEqual(phi01_fourier(0, 1), 1)

    def test_c0m1(self):
        """c(0, -1) = 1."""
        self.assertEqual(phi01_fourier(0, -1), 1)

    def test_c10(self):
        """c(1, 0) = 108."""
        self.assertEqual(phi01_fourier(1, 0), 108)

    def test_c11(self):
        """c(1, 1) = -64."""
        self.assertEqual(phi01_fourier(1, 1), -64)

    def test_c12(self):
        """c(1, 2) = 10."""
        self.assertEqual(phi01_fourier(1, 2), 10)

    def test_c1m2(self):
        """c(1, -2) = 10."""
        self.assertEqual(phi01_fourier(1, -2), 10)

    def test_c20(self):
        """c(2, 0) = 808."""
        self.assertEqual(phi01_fourier(2, 0), 808)

    def test_c21(self):
        """c(2, 1) = -513."""
        self.assertEqual(phi01_fourier(2, 1), -513)

    def test_c22(self):
        """c(2, 2) = 108."""
        self.assertEqual(phi01_fourier(2, 2), 108)

    def test_c23(self):
        """c(2, 3) = 1."""
        self.assertEqual(phi01_fourier(2, 3), 1)

    def test_c_outside_range(self):
        """c(n, l) = 0 for (n,l) outside table with |l| >> n."""
        self.assertEqual(phi01_fourier(0, 5), 0)
        self.assertEqual(phi01_fourier(1, 10), 0)

    def test_c_negative_n(self):
        """c(n, l) = 0 for n < 0."""
        self.assertEqual(phi01_fourier(-1, 0), 0)

    def test_phi01_safe_known(self):
        """phi01_fourier_safe returns int for known entries."""
        self.assertEqual(phi01_fourier_safe(0, 0), 10)

    def test_phi01_safe_provably_zero(self):
        """phi01_fourier_safe returns 0 for provably zero entries."""
        self.assertEqual(phi01_fourier_safe(0, 5), 0)
        self.assertEqual(phi01_fourier_safe(-1, 0), 0)

    def test_phi01_safe_unknown(self):
        """phi01_fourier_safe returns None for unknown entries."""
        # n=3 is not in our verified table
        self.assertIsNone(phi01_fourier_safe(3, 0))


# ============================================================================
# Section 3: phi_{0,1} sum constraint and symmetry
# ============================================================================

class TestPhi01Constraints(unittest.TestCase):
    """Section 3: sum_l c(n,l) = 12*delta_{n,0} and c(n,l)=c(n,-l)."""

    def test_sum_n0(self):
        """sum_l c(0, l) = 12 (= chi(K3)/2)."""
        self.assertEqual(phi01_sum_check(0), 12)

    def test_sum_n1(self):
        """sum_l c(1, l) = 0 (modular constraint)."""
        self.assertEqual(phi01_sum_check(1), 0)

    def test_sum_n2(self):
        """sum_l c(2, l) = 0 (modular constraint)."""
        self.assertEqual(phi01_sum_check(2), 0)

    def test_symmetry_n0(self):
        """c(0, l) = c(0, -l)."""
        for l in range(1, 5):
            self.assertEqual(phi01_fourier(0, l), phi01_fourier(0, -l),
                             f"Symmetry fails at (0, {l})")

    def test_symmetry_n1(self):
        """c(1, l) = c(1, -l)."""
        for l in range(1, 5):
            self.assertEqual(phi01_fourier(1, l), phi01_fourier(1, -l),
                             f"Symmetry fails at (1, {l})")

    def test_symmetry_n2(self):
        """c(2, l) = c(2, -l)."""
        for l in range(1, 5):
            self.assertEqual(phi01_fourier(2, l), phi01_fourier(2, -l),
                             f"Symmetry fails at (2, {l})")

    def test_cross_check_sum_function(self):
        """cross_check_phi01_sum returns True."""
        self.assertTrue(cross_check_phi01_sum())

    def test_cross_check_symmetry_function(self):
        """cross_check_phi01_symmetry returns True."""
        self.assertTrue(cross_check_phi01_symmetry())


# ============================================================================
# Section 4: phi_{0,1} numerical verification
# ============================================================================

class TestPhi01Numerical(unittest.TestCase):
    """Section 4: theta function computation of phi_{0,1}."""

    def test_phi01_at_origin_constant(self):
        """phi_{0,1}(tau, 0) = 12 for various tau (modular invariance)."""
        for T in [1.5, 2.0, 3.0, 5.0]:
            val = phi01_numerical(T, 0.0)
            self.assertAlmostEqual(val.real, 12.0, places=6,
                                   msg=f"phi01(i*{T}, 0) != 12")
            self.assertAlmostEqual(val.imag, 0.0, places=6)

    def test_phi01_q0_term(self):
        """At large T (q~0), phi_{0,1} -> c(0,-1)*y + c(0,0) + c(0,1)/y."""
        T = 10.0
        import cmath
        # y = e^{2*pi*i*z} at z = 0.1
        z = 0.1
        y = cmath.exp(2 * cmath.pi * 1j * z)
        val = phi01_numerical(T, z)
        expected = 1 * y + 10 + 1 / y
        self.assertAlmostEqual(val.real, expected.real, places=4)
        self.assertAlmostEqual(val.imag, expected.imag, places=4)

    def test_phi01_symmetry_numerical(self):
        """phi_{0,1}(tau, -z) = phi_{0,1}(tau, z) numerically."""
        T = 2.0
        z = 0.2
        val_pos = phi01_numerical(T, z)
        val_neg = phi01_numerical(T, -z)
        self.assertAlmostEqual(val_pos.real, val_neg.real, places=6)
        self.assertAlmostEqual(val_pos.imag, val_neg.imag, places=6)


# ============================================================================
# Section 5: K3 elliptic genus
# ============================================================================

class TestK3EllipticGenus(unittest.TestCase):
    """Section 5: K3 EG = 2*phi_{0,1}."""

    def test_k3_eg_is_twice_phi01(self):
        """c_K3(n,l) = 2*c(n,l)."""
        for n in range(3):
            for l in range(-4, 5):
                self.assertEqual(k3_elliptic_genus_coeff(n, l),
                                 2 * phi01_fourier(n, l))

    def test_k3_eg_at_origin(self):
        """2*phi_{0,1}(tau,0)|_{q^0} = chi(K3) = 24."""
        self.assertTrue(cross_check_k3_eg_at_origin())
        self.assertEqual(2 * phi01_sum_check(0), 24)


# ============================================================================
# Section 6: Euler characteristics
# ============================================================================

class TestEulerCharacteristics(unittest.TestCase):
    """Section 6: chi(K3) = 24, chi(K3 x E) = 0."""

    def test_chi_k3(self):
        self.assertEqual(k3_euler_characteristic(), 24)

    def test_chi_k3xe(self):
        self.assertEqual(k3xe_euler_characteristic(), 0)

    def test_chi_product(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        self.assertEqual(k3xe_euler_characteristic(),
                         k3_euler_characteristic() * 0)


# ============================================================================
# Section 7: Hilbert scheme — recurrence
# ============================================================================

class TestHilbertSchemeRecurrence(unittest.TestCase):
    """Section 7: chi(Hilb^n(K3)) via Goettsche recurrence."""

    def test_hilb0(self):
        self.assertEqual(hilb_k3_euler_char(0), 1)

    def test_hilb1(self):
        """Hilb^1(K3) = K3, chi = 24."""
        self.assertEqual(hilb_k3_euler_char(1), 24)

    def test_hilb2(self):
        """chi(Hilb^2(K3)) = 324."""
        self.assertEqual(hilb_k3_euler_char(2), 324)

    def test_hilb3(self):
        """chi(Hilb^3(K3)) = 3200."""
        self.assertEqual(hilb_k3_euler_char(3), 3200)

    def test_hilb4(self):
        """chi(Hilb^4(K3)) = 25650."""
        self.assertEqual(hilb_k3_euler_char(4), 25650)

    def test_hilb5(self):
        """chi(Hilb^5(K3)) = 176256."""
        self.assertEqual(hilb_k3_euler_char(5), 176256)

    def test_hilb_list(self):
        """Partition function as list."""
        expected = [1, 24, 324, 3200, 25650, 176256]
        self.assertEqual(hilb_k3_partition_function(6), expected)

    def test_hilb_negative(self):
        self.assertEqual(hilb_k3_euler_char(-1), 0)


# ============================================================================
# Section 8: Hilbert scheme — direct product (cross-check)
# ============================================================================

class TestHilbertSchemeProduct(unittest.TestCase):
    """Section 8: prod(1-q^k)^{-24} direct expansion."""

    def test_product_matches_recurrence_10(self):
        """Two independent methods agree through q^9."""
        self.assertEqual(hilb_k3_partition_function(10),
                         hilb_k3_via_product(10))

    def test_product_matches_recurrence_15(self):
        """Two independent methods agree through q^14."""
        self.assertTrue(cross_check_hilb_two_methods(15))

    def test_product_first_values(self):
        """Direct product gives known OEIS values."""
        prod = hilb_k3_via_product(6)
        self.assertEqual(prod, [1, 24, 324, 3200, 25650, 176256])


# ============================================================================
# Section 9: OEIS A006922 verification
# ============================================================================

class TestOEIS(unittest.TestCase):
    """Section 9: Hilb^n(K3) matches OEIS A006922."""

    def test_oeis_a006922(self):
        """First 8 values of prod(1-q^n)^{-24}."""
        # OEIS A006922: 1, 24, 324, 3200, 25650, 176256, 1073720, 5930496
        oeis = [1, 24, 324, 3200, 25650, 176256, 1073720, 5930496]
        computed = hilb_k3_partition_function(8)
        self.assertEqual(computed, oeis)


# ============================================================================
# Section 10: MacMahon function
# ============================================================================

class TestMacMahon(unittest.TestCase):
    """Section 10: plane partition numbers M(q) = prod(1-q^n)^{-n}."""

    def test_macmahon_oeis(self):
        """OEIS A000219: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        self.assertEqual(macmahon_coeffs(11), expected)

    def test_macmahon_recurrence_consistency(self):
        """pp(n) satisfies the sigma_2 recurrence."""
        for n in range(1, 15):
            lhs = n * _plane_partition_count(n)
            rhs = sum(_sigma(k, 2) * _plane_partition_count(n - k)
                      for k in range(1, n + 1))
            self.assertEqual(lhs, rhs, f"Recurrence fails at n={n}")


# ============================================================================
# Section 11: DT degree-0 for K3 x E
# ============================================================================

class TestDTDegree0(unittest.TestCase):
    """Section 11: Z_{DT,0}(K3 x E) = M(-q)^0 = 1."""

    def test_dt0_is_delta(self):
        """DT degree-0 is [1, 0, 0, ...]."""
        dt0 = dt_degree0_k3xe(10)
        self.assertEqual(dt0[0], 1)
        for i in range(1, 10):
            self.assertEqual(dt0[i], 0, f"DT_0 coeff at q^{i} != 0")

    def test_mnop_check(self):
        self.assertTrue(cross_check_mnop_degree0(10))


# ============================================================================
# Section 12: Yau-Zaslow genus-0
# ============================================================================

class TestYauZaslow(unittest.TestCase):
    """Section 12: genus-0 GV invariants for K3."""

    def test_yz_n0_0(self):
        """n^0_0 = 1."""
        yz = yau_zaslow_genus0(5)
        self.assertEqual(yz[0], 1)

    def test_yz_n0_1(self):
        """n^0_1 = 24 (24 rational curves on generic K3)."""
        yz = yau_zaslow_genus0(5)
        self.assertEqual(yz[1], 24)

    def test_yz_n0_2(self):
        """n^0_2 = 324."""
        yz = yau_zaslow_genus0(5)
        self.assertEqual(yz[2], 324)

    def test_yz_n0_3(self):
        """n^0_3 = 3200."""
        yz = yau_zaslow_genus0(5)
        self.assertEqual(yz[3], 3200)

    def test_yz_all_positive(self):
        """n^0_d > 0 for d >= 0 (partition counts are positive)."""
        yz = yau_zaslow_genus0(20)
        for d in range(20):
            self.assertGreater(yz[d], 0, f"n^0_{d} not positive")

    def test_yz_all_integer(self):
        """GV integrality: n^0_d in Z."""
        yz = yau_zaslow_genus0(20)
        for d in range(20):
            self.assertIsInstance(yz[d], int, f"n^0_{d} not integer")


# ============================================================================
# Section 13: Yau-Zaslow = Hilbert scheme
# ============================================================================

class TestYZEqualsHilb(unittest.TestCase):
    """Section 13: n^0_d = chi(Hilb^d(K3)) (deep theorem)."""

    def test_yz_equals_hilb_10(self):
        """Two independent computations agree through d=9."""
        self.assertTrue(cross_check_yz_equals_hilb(10))

    def test_yz_equals_hilb_20(self):
        """Agreement through d=19."""
        self.assertTrue(cross_check_yz_equals_hilb(20))

    def test_yz_equals_hilb_termwise(self):
        """Term-by-term comparison."""
        yz = yau_zaslow_genus0(8)
        hilb = hilb_k3_partition_function(8)
        for d in range(8):
            self.assertEqual(yz[d], hilb[d], f"YZ != Hilb at d={d}")


# ============================================================================
# Section 14: DT/PT correspondence
# ============================================================================

class TestDTPT(unittest.TestCase):
    """Section 14: DT = PT for K3 x E."""

    def test_dt_equals_pt(self):
        """chi(K3 x E) = 0 implies Z_DT = Z_PT."""
        self.assertTrue(dt_equals_pt_k3xe())

    def test_chi_zero_is_key(self):
        """The identity holds because chi(K3)*chi(E) = 24*0 = 0."""
        self.assertEqual(k3xe_euler_characteristic(), 0)

    def test_cross_check_dt_pt(self):
        self.assertTrue(cross_check_dt_pt())


# ============================================================================
# Section 15: Motivic DT (degree 0)
# ============================================================================

class TestMotivicDT(unittest.TestCase):
    """Section 15: motivic DT invariants for ideal sheaves."""

    def test_dt0_is_1(self):
        """DT_0 = 1 (empty subscheme)."""
        results = motivic_dt_degree0(5)
        self.assertEqual(results[0].dt_invariant, 1)

    def test_dtn_is_0(self):
        """DT_n = 0 for n >= 1 (MNOP, chi=0)."""
        results = motivic_dt_degree0(5)
        for r in results[1:]:
            self.assertEqual(r.dt_invariant, 0,
                             f"DT_{r.n} should be 0")

    def test_description_nonempty(self):
        """Each result has a nonempty description."""
        results = motivic_dt_degree0(3)
        for r in results:
            self.assertTrue(len(r.description) > 0)


# ============================================================================
# Section 16: Shadow tower kappa
# ============================================================================

class TestShadowKappa(unittest.TestCase):
    """Section 16: modular characteristic kappa."""

    def test_kappa_k3xe_total(self):
        """kappa(K3 x E) = chi/12 = 0/12 = 0."""
        self.assertEqual(shadow_kappa_k3xe(), Fraction(0))

    def test_kappa_k3_relative(self):
        """kappa(K3 relative) = chi(K3)/12 = 24/12 = 2."""
        self.assertEqual(shadow_kappa_k3_relative(), Fraction(2))

    def test_kappa_consistent_with_dt(self):
        """kappa=0 consistent with M(-q)^0 = 1."""
        self.assertEqual(shadow_kappa_k3xe(), Fraction(0))
        self.assertEqual(dt_degree0_k3xe(5)[0], 1)

    def test_kappa_not_c_over_2(self):
        """AP48: kappa != c/2 in general. For K3 relative, kappa=2.
        The chiral de Rham has c = 2*dim = 4, so c/2 = 2 = kappa.
        This coincidence holds for the chiral de Rham complex but
        not for general VOAs (AP48)."""
        self.assertEqual(shadow_kappa_k3_relative(), Fraction(2))


# ============================================================================
# Section 17: Shadow tower F_g and lambda_g^FP
# ============================================================================

class TestShadowFg(unittest.TestCase):
    """Section 17: genus-g shadow amplitudes."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_f1_k3xe(self):
        """F_1(K3 x E) = 0."""
        self.assertEqual(shadow_f1_k3xe(), Fraction(0))

    def test_f1_k3_relative(self):
        """F_1(K3 rel) = kappa/24 = 2/24 = 1/12."""
        self.assertEqual(shadow_f1_k3_relative(), Fraction(1, 12))

    def test_f2_k3_relative(self):
        """F_2 = kappa * lambda_2 = 2 * 7/5760 = 7/2880."""
        self.assertEqual(shadow_fg_k3_relative(2), Fraction(7, 2880))

    def test_f3_k3_relative(self):
        """F_3 = 2 * 31/967680 = 31/483840."""
        self.assertEqual(shadow_fg_k3_relative(3), Fraction(31, 483840))

    def test_fg_formula(self):
        """F_g = kappa * lambda_g for all g."""
        for g in range(1, 6):
            expected = Fraction(2) * lambda_fp(g)
            self.assertEqual(shadow_fg_k3_relative(g), expected,
                             f"F_{g} formula fails")


# ============================================================================
# Section 18: Shadow tower multi-genus consistency
# ============================================================================

class TestShadowMultiGenus(unittest.TestCase):
    """Section 18: F_g values are positive and decreasing."""

    def test_fg_positive(self):
        """F_g > 0 for g >= 1 (since kappa=2 > 0 and lambda_g > 0)."""
        for g in range(1, 8):
            self.assertGreater(shadow_fg_k3_relative(g), 0,
                               f"F_{g} not positive")

    def test_fg_decreasing(self):
        """F_g > F_{g+1} (lambda_g^FP decreases rapidly)."""
        for g in range(1, 6):
            self.assertGreater(shadow_fg_k3_relative(g),
                               shadow_fg_k3_relative(g + 1),
                               f"F_{g} not > F_{g+1}")

    def test_cross_check_shadow_f1(self):
        self.assertTrue(cross_check_shadow_f1())


# ============================================================================
# Section 19: Topological string free energy
# ============================================================================

class TestTopologicalString(unittest.TestCase):
    """Section 19: genus-0 topological string F_0."""

    def test_f0_d1(self):
        """F_0^1 = n^0_1 / 1^3 = 24."""
        f0 = topological_string_f0(5)
        self.assertEqual(f0[1], Fraction(24))

    def test_f0_d2(self):
        """F_0^2 = n^0_2 + n^0_1/8 = 324 + 3 = 327."""
        f0 = topological_string_f0(5)
        # sum_{k|2} n^0_{2/k} / k^3 = n^0_2/1 + n^0_1/8 = 324 + 24/8 = 327
        self.assertEqual(f0[2], Fraction(327))

    def test_f0_d3(self):
        """F_0^3 = n^0_3 + n^0_1/27 = 3200 + 24/27 = 3200 + 8/9."""
        f0 = topological_string_f0(5)
        expected = Fraction(3200) + Fraction(24, 27)
        self.assertEqual(f0[3], expected)


# ============================================================================
# Section 20: GV integrality
# ============================================================================

class TestGVIntegrality(unittest.TestCase):
    """Section 20: Gopakumar-Vafa integrality."""

    def test_gv_all_integer(self):
        """n^0_d in Z for d=0,...,19."""
        self.assertTrue(cross_check_gv_integrality(20))

    def test_gv_check_dict(self):
        """gv_integrality_check_yz returns all True."""
        checks = gv_integrality_check_yz(10)
        for d, ok in checks.items():
            self.assertTrue(ok, f"GV non-integer at d={d}")


# ============================================================================
# Section 21: KKV genus-1
# ============================================================================

class TestKKVGenus1(unittest.TestCase):
    """Section 21: genus-1 BPS invariants."""

    def test_n1_1(self):
        """n^1_1 = -2 (standard K3 result)."""
        g1 = kkv_genus1_invariants(5)
        self.assertEqual(g1[1], -2)

    def test_n1_0(self):
        """n^1_0 = 0."""
        g1 = kkv_genus1_invariants(5)
        self.assertEqual(g1[0], 0)


# ============================================================================
# Section 22: Full analysis pipeline
# ============================================================================

class TestFullAnalysis(unittest.TestCase):
    """Section 22: full_analysis pipeline."""

    def test_full_analysis_runs(self):
        """Pipeline completes without error."""
        result = full_analysis(8)
        self.assertIsNotNone(result)

    def test_full_analysis_chi(self):
        result = full_analysis(8)
        self.assertEqual(result.chi_k3, 24)
        self.assertEqual(result.chi_k3xe, 0)

    def test_full_analysis_dt_pt(self):
        result = full_analysis(8)
        self.assertTrue(result.dt_equals_pt)
        self.assertTrue(result.dt_degree0_trivial)

    def test_full_analysis_hilb(self):
        result = full_analysis(6)
        self.assertEqual(result.hilb_k3, [1, 24, 324, 3200, 25650, 176256])

    def test_full_analysis_yz_match(self):
        result = full_analysis(10)
        self.assertTrue(result.yz_matches_hilb)
        self.assertTrue(result.hilb_two_methods_match)

    def test_full_analysis_shadow(self):
        result = full_analysis(5)
        self.assertEqual(result.kappa_total, Fraction(0))
        self.assertEqual(result.kappa_relative, Fraction(2))
        self.assertEqual(result.f1_total, Fraction(0))
        self.assertEqual(result.f1_relative, Fraction(1, 12))

    def test_full_analysis_phi01(self):
        result = full_analysis(5)
        self.assertTrue(result.phi01_sum_ok)
        self.assertTrue(result.phi01_sym_ok)
        self.assertTrue(result.k3_eg_origin_ok)

    def test_all_cross_checks_pass(self):
        result = full_analysis(10)
        self.assertTrue(result.all_cross_checks_pass)


# ============================================================================
# Section 23: Cross-check battery
# ============================================================================

class TestCrossCheckBattery(unittest.TestCase):
    """Section 23: all cross-check functions return True."""

    def test_yz_hilb(self):
        self.assertTrue(cross_check_yz_equals_hilb(15))

    def test_hilb_two_methods(self):
        self.assertTrue(cross_check_hilb_two_methods(12))

    def test_dt_pt(self):
        self.assertTrue(cross_check_dt_pt())

    def test_mnop(self):
        self.assertTrue(cross_check_mnop_degree0(10))

    def test_shadow_f1(self):
        self.assertTrue(cross_check_shadow_f1())

    def test_gv_int(self):
        self.assertTrue(cross_check_gv_integrality(15))

    def test_phi01_sum(self):
        self.assertTrue(cross_check_phi01_sum())

    def test_phi01_sym(self):
        self.assertTrue(cross_check_phi01_symmetry())

    def test_k3_eg(self):
        self.assertTrue(cross_check_k3_eg_at_origin())


# ============================================================================
# Section 24: Numerical phi_{0,1} evaluation
# ============================================================================

class TestPhi01NumericalEvaluation(unittest.TestCase):
    """Section 24: phi_{0,1} via theta functions."""

    def test_at_origin_T2(self):
        val = phi01_numerical(2.0, 0.0)
        self.assertAlmostEqual(val.real, 12.0, places=8)

    def test_at_origin_T5(self):
        val = phi01_numerical(5.0, 0.0)
        self.assertAlmostEqual(val.real, 12.0, places=10)

    def test_symmetry_z(self):
        """phi(tau, -z) = phi(tau, z)."""
        val1 = phi01_numerical(2.0, 0.3)
        val2 = phi01_numerical(2.0, -0.3)
        self.assertAlmostEqual(val1.real, val2.real, places=8)

    def test_periodicity_z(self):
        """phi(tau, z+1) = phi(tau, z) (period 1 in z)."""
        val1 = phi01_numerical(2.0, 0.2)
        val2 = phi01_numerical(2.0, 1.2)
        self.assertAlmostEqual(val1.real, val2.real, places=6)

    def test_matches_table_at_q0(self):
        """At large T, phi01 -> c(0,-1)*y + c(0,0) + c(0,1)/y."""
        import cmath
        T = 8.0
        z = 0.15
        y = cmath.exp(2 * cmath.pi * 1j * z)
        val = phi01_numerical(T, z)
        expected = 1 * y + 10 + 1 / y  # c(0,+-1)=1, c(0,0)=10
        self.assertAlmostEqual(val.real, expected.real, places=5)
        self.assertAlmostEqual(val.imag, expected.imag, places=5)


# ============================================================================
# Section 25: Bernoulli numbers
# ============================================================================

class TestBernoulliNumbers(unittest.TestCase):
    """Section 25: Bernoulli numbers for lambda_g^FP."""

    def test_b0(self):
        self.assertEqual(_bernoulli_number_frac(0), Fraction(1))

    def test_b1(self):
        self.assertEqual(_bernoulli_number_frac(1), Fraction(-1, 2))

    def test_b2(self):
        self.assertEqual(_bernoulli_number_frac(2), Fraction(1, 6))

    def test_b4(self):
        self.assertEqual(_bernoulli_number_frac(4), Fraction(-1, 30))

    def test_b6(self):
        self.assertEqual(_bernoulli_number_frac(6), Fraction(1, 42))

    def test_b_odd_zero(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(_bernoulli_number_frac(n), Fraction(0))


# ============================================================================
# Section 26: Goettsche formula structural tests
# ============================================================================

class TestGoettscheStructural(unittest.TestCase):
    """Section 26: structural properties of Hilb^n(K3) Euler chars."""

    def test_hilb1_equals_chi_k3(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        self.assertEqual(hilb_k3_euler_char(1), k3_euler_characteristic())

    def test_hilb_growth(self):
        """chi(Hilb^n(K3)) grows monotonically."""
        for n in range(1, 15):
            self.assertGreater(hilb_k3_euler_char(n),
                               hilb_k3_euler_char(n - 1),
                               f"Not monotone at n={n}")

    def test_hilb_divisibility(self):
        """Recurrence gives exact division: n | sum sigma_1(k)*h(n-k)."""
        for n in range(1, 10):
            total = sum(24 * _sigma(k, 1) * hilb_k3_euler_char(n - k)
                        for k in range(1, n + 1))
            self.assertEqual(total % n, 0, f"Division fails at n={n}")

    def test_two_methods_agree_large(self):
        """Recurrence and product agree for n up to 12."""
        rec = hilb_k3_partition_function(12)
        prod = hilb_k3_via_product(12)
        self.assertEqual(rec, prod)


if __name__ == "__main__":
    unittest.main()
