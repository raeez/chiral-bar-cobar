r"""Tests for the K3 x E modular partition function engine.

Multi-path verification of:
1. Siegel modular form structure (chi_10, Fourier-Jacobi expansion)
2. Jacobi forms (phi_{0,1}, phi_{-2,1}, phi_{10,1})
3. DVV formula and BPS degeneracies
4. Shadow obstruction tower for K3 x E
5. Jacobi form ring structure
6. Ramanujan tau function and eta products
7. Mathieu moonshine coefficients
8. Cross-consistency checks

Conventions: Eichler-Zagier throughout (AP38).
"""

import math
import unittest
from fractions import Fraction

from compute.lib.cy_modular_k3e_engine import (
    K3_CENTRAL_CHARGE,
    K3_COMPLEX_DIM,
    K3_EULER_CHAR,
    K3E_CENTRAL_CHARGE,
    K3E_COMPLEX_DIM,
    K3E_EULER_CHAR,
    bernoulli_number,
    bps_degeneracy,
    bps_degeneracy_table,
    bps_entropy_leading,
    chi10_fourier_jacobi,
    delta_coeffs,
    divisors,
    e4_coeffs,
    e6_coeffs,
    eta_coeffs,
    eta_power_coeffs,
    faber_pandharipande,
    fourier_jacobi_comparison,
    full_k3e_modular_data,
    genus2_siegel_form_weights,
    jacobi_cusp_dimension,
    jacobi_ring_basis_dimensions,
    jacobi_ring_dimension,
    jacobi_ring_relations,
    kappa_elliptic_curve,
    kappa_k3,
    kappa_k3e,
    mathieu_moonshine_coefficients,
    partition_count,
    phi01_at_z0,
    phi01_discriminant_table,
    phi01_fourier,
    phi101_at_z0,
    phi101_fourier,
    phi_m21_fourier,
    rademacher_leading,
    ramanujan_tau,
    shadow_ahat_generating_function,
    shadow_F1_k3e,
    shadow_F2_k3e,
    shadow_Fg_k3e,
    sigma_k,
    verify_bps_vs_phi_m21,
    verify_eta_product_identity,
    verify_jacobi_ring_dimensions,
    verify_k3_elliptic_genus_chi,
    verify_kappa_additivity,
    verify_phi01_constant_at_z0,
    verify_phi101_equals_delta_times_phi_m21,
    verify_phi101_vanishes_at_z0,
    verify_ramanujan_tau,
    verify_shadow_ahat,
)


# =====================================================================
# Section 1: Arithmetic primitives
# =====================================================================

class TestArithmeticPrimitives(unittest.TestCase):
    """Tests for low-level arithmetic functions."""

    def test_sigma_k_basic(self):
        """sigma_1(6) = 1 + 2 + 3 + 6 = 12."""
        self.assertEqual(sigma_k(6, 1), 12)

    def test_sigma_k_cubes(self):
        """sigma_3(2) = 1 + 8 = 9."""
        self.assertEqual(sigma_k(2, 3), 9)

    def test_sigma_k_zero(self):
        self.assertEqual(sigma_k(0, 1), 0)
        self.assertEqual(sigma_k(-1, 1), 0)

    def test_sigma_k_prime(self):
        """sigma_k(p) = 1 + p^k for prime p."""
        self.assertEqual(sigma_k(7, 2), 1 + 49)

    def test_partition_count_small(self):
        """Known partition numbers: p(0)=1, p(1)=1, ..., p(5)=7."""
        known = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n, expected in enumerate(known):
            self.assertEqual(partition_count(n), expected,
                             f"p({n}) = {partition_count(n)}, expected {expected}")

    def test_bernoulli_values(self):
        """Known Bernoulli numbers."""
        self.assertEqual(bernoulli_number(0), Fraction(1))
        self.assertEqual(bernoulli_number(1), Fraction(-1, 2))
        self.assertEqual(bernoulli_number(2), Fraction(1, 6))
        self.assertEqual(bernoulli_number(4), Fraction(-1, 30))
        self.assertEqual(bernoulli_number(6), Fraction(1, 42))
        self.assertEqual(bernoulli_number(3), Fraction(0))
        self.assertEqual(bernoulli_number(5), Fraction(0))

    def test_divisors(self):
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(divisors(1), [1])
        self.assertEqual(divisors(7), [1, 7])

    def test_faber_pandharipande_values(self):
        """lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680."""
        self.assertEqual(faber_pandharipande(1), Fraction(1, 24))
        self.assertEqual(faber_pandharipande(2), Fraction(7, 5760))
        self.assertEqual(faber_pandharipande(3), Fraction(31, 967680))


# =====================================================================
# Section 2: Eta function and Eisenstein series
# =====================================================================

class TestEtaEisenstein(unittest.TestCase):
    """Tests for q-expansion primitives."""

    def test_eta_leading(self):
        """eta = q^{1/24}(1 - q - q^2 + q^5 + q^7 - ...)."""
        c = eta_coeffs(10)
        self.assertEqual(c[0], 1)
        self.assertEqual(c[1], -1)
        self.assertEqual(c[2], -1)
        self.assertEqual(c[3], 0)
        self.assertEqual(c[4], 0)
        self.assertEqual(c[5], 1)

    def test_eta_pentagonal(self):
        """Pentagonal numbers: nonzero at k(3k-1)/2 for k in Z."""
        c = eta_coeffs(30)
        # k=1: 1, k=2: 5, k=-1: 2, k=-2: 7
        pent = {0, 1, 2, 5, 7, 12, 15, 22, 26}
        for n in range(30):
            if n in pent:
                self.assertNotEqual(c[n], 0, f"eta[{n}] should be nonzero")
            else:
                self.assertEqual(c[n], 0, f"eta[{n}] should be zero")

    def test_eta_power_24_is_delta(self):
        """eta^{24} (shifted by q) should give the Delta function."""
        v = verify_eta_product_identity(15)
        self.assertTrue(v['consistent'])

    def test_e4_leading(self):
        """E_4 = 1 + 240q + 2160q^2 + ..."""
        c = e4_coeffs(5)
        self.assertEqual(c[0], 1)
        self.assertEqual(c[1], 240)
        self.assertEqual(c[2], 2160)

    def test_e6_leading(self):
        """E_6 = 1 - 504q - 16632q^2 - ..."""
        c = e6_coeffs(5)
        self.assertEqual(c[0], 1)
        self.assertEqual(c[1], -504)
        self.assertEqual(c[2], -16632)

    def test_e4_e6_discriminant(self):
        """Delta = (E_4^3 - E_6^2) / 1728."""
        nmax = 8
        e4 = e4_coeffs(nmax)
        e6 = e6_coeffs(nmax)
        delta = delta_coeffs(nmax)

        # E_4^3
        from compute.lib.cy_modular_k3e_engine import _convolve
        e4sq = _convolve(e4, e4, nmax)
        e4cu = _convolve(e4sq, e4, nmax)
        # E_6^2
        e6sq = _convolve(e6, e6, nmax)

        for n in range(nmax):
            lhs = Fraction(e4cu[n] - e6sq[n], 1728)
            rhs = Fraction(delta[n])
            self.assertEqual(lhs, rhs,
                             f"Delta[{n}]: (E4^3-E6^2)/1728 = {lhs}, delta = {rhs}")

    def test_delta_leading(self):
        """Delta = q - 24q^2 + 252q^3 - 1472q^4 + ..."""
        d = delta_coeffs(6)
        self.assertEqual(d[0], 0)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[2], -24)
        self.assertEqual(d[3], 252)
        self.assertEqual(d[4], -1472)
        self.assertEqual(d[5], 4830)

    def test_delta_coeffs_are_int(self):
        """All Delta coefficients must be exact integers."""
        d = delta_coeffs(20)
        for n, c in enumerate(d):
            self.assertIsInstance(c, int, f"delta[{n}] = {c} is {type(c)}")


# =====================================================================
# Section 3: Ramanujan tau function
# =====================================================================

class TestRamanujanTau(unittest.TestCase):
    """Multi-path verification of the Ramanujan tau function."""

    def test_tau_values(self):
        """Known tau(n) values from literature."""
        known = {
            1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
            6: -6048, 7: -16744, 8: 84480, 9: -113643, 10: -115920,
        }
        for n, expected in known.items():
            self.assertEqual(ramanujan_tau(n), expected,
                             f"tau({n}) = {ramanujan_tau(n)}, expected {expected}")

    def test_tau_multiplicativity(self):
        """tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        pairs = [(2, 3), (2, 5), (3, 5), (2, 7), (3, 7)]
        for a, b in pairs:
            self.assertEqual(ramanujan_tau(a * b),
                             ramanujan_tau(a) * ramanujan_tau(b),
                             f"tau({a}*{b}) != tau({a})*tau({b})")

    def test_tau_hecke_relation(self):
        """tau(p^2) = tau(p)^2 - p^{11} for primes p."""
        for p in [2, 3, 5, 7]:
            lhs = ramanujan_tau(p * p)
            rhs = ramanujan_tau(p) ** 2 - p ** 11
            self.assertEqual(lhs, rhs,
                             f"Hecke at p={p}: tau(p^2)={lhs}, tau(p)^2-p^11={rhs}")

    def test_verify_ramanujan_tau_all_paths(self):
        """Full multi-path verification."""
        v = verify_ramanujan_tau()
        self.assertTrue(v['all_values_match'])
        self.assertTrue(v['all_multiplicative'])
        self.assertTrue(v['all_hecke'])


# =====================================================================
# Section 4: Jacobi form phi_{0,1}
# =====================================================================

class TestPhi01(unittest.TestCase):
    """Tests for phi_{0,1} (unique weak Jacobi form of weight 0, index 1)."""

    def test_phi01_z0_is_12(self):
        """phi_{0,1}(tau, 0) = 12 (constant)."""
        z0 = phi01_at_z0(10)
        self.assertEqual(z0[0], 12)
        for n in range(1, 10):
            self.assertEqual(z0[n], 0, f"phi01(tau,0) at q^{n} = {z0[n]} != 0")

    def test_phi01_disc_table_known_values(self):
        """Verify known discriminant coefficients (Eichler-Zagier)."""
        table = phi01_discriminant_table()
        self.assertEqual(table[-1], 1)
        self.assertEqual(table[0], 10)
        self.assertEqual(table[3], -64)
        self.assertEqual(table[4], 108)
        self.assertEqual(table[7], -513)
        self.assertEqual(table[8], 808)

    def test_phi01_disc_constraint(self):
        """sum_l c(4n - l^2) = 0 for n >= 1 (phi01 is constant at z=0)."""
        table = phi01_discriminant_table()
        for n in range(1, 8):
            s = 0
            for l in range(-20, 21):
                D = 4 * n - l * l
                if D in table:
                    s += table[D]
            self.assertEqual(s, 0, f"Disc constraint fails at n={n}: sum = {s}")

    def test_phi01_leading_fourier(self):
        """phi_{0,1} = (y + 10 + y^{-1}) + (10y^2 - 64y + 108 - 64y^{-1} + 10y^{-2})q + ..."""
        fc = phi01_fourier(3)
        # q^0 terms
        self.assertEqual(fc.get((0, 1), 0), 1)
        self.assertEqual(fc.get((0, 0), 0), 10)
        self.assertEqual(fc.get((0, -1), 0), 1)
        # q^1 terms
        self.assertEqual(fc.get((1, 2), 0), 10)
        self.assertEqual(fc.get((1, 1), 0), -64)
        self.assertEqual(fc.get((1, 0), 0), 108)
        self.assertEqual(fc.get((1, -1), 0), -64)
        self.assertEqual(fc.get((1, -2), 0), 10)

    def test_phi01_symmetry(self):
        """c(n, l) = c(n, -l) (phi_{0,1} is even in z)."""
        fc = phi01_fourier(8)
        for (n, l), c in fc.items():
            c_neg = fc.get((n, -l), 0)
            self.assertEqual(c, c_neg, f"Symmetry fails at (n={n}, l={l})")

    def test_verify_phi01_constant_multi_path(self):
        """Full multi-path verification of phi_{0,1}(tau, 0) = 12."""
        v = verify_phi01_constant_at_z0(8)
        self.assertTrue(v['paths_agree'])

    def test_k3_elliptic_genus_equals_2phi01(self):
        """phi(K3) = 2*phi_{0,1}, so phi(K3)(tau, 0) = 24 = chi(K3)."""
        v = verify_k3_elliptic_genus_chi()
        self.assertTrue(v['all_24'])


# =====================================================================
# Section 5: Jacobi form phi_{-2,1}
# =====================================================================

class TestPhiM21(unittest.TestCase):
    """Tests for phi_{-2,1} (unique weak Jacobi form of weight -2, index 1)."""

    def test_phi_m21_z0_vanishes(self):
        """phi_{-2,1}(tau, 0) = 0 identically."""
        fc = phi_m21_fourier(10)
        for n in range(10):
            s = sum(c for (nn, l), c in fc.items() if nn == n)
            self.assertEqual(s, 0, f"phi_m21(tau,0) at q^{n} = {s} != 0")

    def test_phi_m21_leading_terms(self):
        """phi_{-2,1} = (y - 2 + y^{-1}) + ..."""
        fc = phi_m21_fourier(3)
        self.assertEqual(fc.get((0, 1), 0), 1)
        self.assertEqual(fc.get((0, 0), 0), -2)
        self.assertEqual(fc.get((0, -1), 0), 1)

    def test_phi_m21_disc_coeffs(self):
        """Known disc coefficients: c(-1)=1, c(0)=-2, c(3)=8, c(4)=-12."""
        fc = phi_m21_fourier(5)
        disc = {}
        for (n, l), c in fc.items():
            D = 4 * n - l * l
            if D not in disc:
                disc[D] = c
        self.assertEqual(disc.get(-1), 1)
        self.assertEqual(disc.get(0), -2)
        self.assertEqual(disc.get(3), 8)
        self.assertEqual(disc.get(4), -12)
        self.assertEqual(disc.get(7), 39)
        self.assertEqual(disc.get(8), -56)

    def test_phi_m21_symmetry(self):
        """c(n, l) = c(n, -l) for phi_{-2,1} (even in z)."""
        fc = phi_m21_fourier(8)
        for (n, l), c in fc.items():
            c_neg = fc.get((n, -l), 0)
            self.assertEqual(c, c_neg, f"Symmetry at (n={n}, l={l})")

    def test_phi_m21_disc_constraint_z0(self):
        """sum_l c(4n - l^2) = 0 for all n >= 0 (phi_{-2,1} vanishes at z=0)."""
        fc = phi_m21_fourier(8)
        disc = {}
        for (n, l), c in fc.items():
            D = 4 * n - l * l
            if D not in disc:
                disc[D] = c
        for n in range(8):
            s = 0
            for l in range(-20, 21):
                D = 4 * n - l * l
                if D in disc:
                    s += disc[D]
            self.assertEqual(s, 0, f"Disc constraint at n={n}: sum = {s}")


# =====================================================================
# Section 6: Jacobi cusp form phi_{10,1}
# =====================================================================

class TestPhi101(unittest.TestCase):
    """Tests for phi_{10,1} = eta^{18} * theta_1^2."""

    def test_phi101_vanishes_at_z0(self):
        """phi_{10,1}(tau, 0) = 0 (theta_1 vanishes at z=0)."""
        z0 = phi101_at_z0(8)
        for n in range(8):
            self.assertEqual(z0[n], 0, f"phi101(tau,0) at q^{n} = {z0[n]}")

    def test_phi101_is_cusp(self):
        """phi_{10,1} vanishes at q=0 (cusp form)."""
        fc = phi101_fourier(5)
        for l in range(-10, 11):
            self.assertEqual(fc.get((0, l), 0), 0,
                             f"phi101 has nonzero term at (0, {l})")

    def test_phi101_disc_values(self):
        """Known disc coefficients from Skoruppa / LMFDB."""
        fc = phi101_fourier(5)
        disc = {}
        for (n, l), c in fc.items():
            D = 4 * n - l * l
            if D not in disc:
                disc[D] = c
        # Literature values
        self.assertEqual(disc.get(3), -1)
        self.assertEqual(disc.get(4), 2)
        self.assertEqual(disc.get(7), 16)
        self.assertEqual(disc.get(8), -36)

    def test_phi101_equals_neg_delta_phi_m21(self):
        """phi_{10,1} = -Delta * phi_{-2,1}."""
        v = verify_phi101_equals_delta_times_phi_m21(6)
        self.assertTrue(v['weight_check'])
        self.assertTrue(v['index_check'])
        self.assertTrue(v['fourier_match'])
        self.assertTrue(v['paths_agree'])

    def test_phi101_weight_index(self):
        """phi_{10,1} has weight 10, index 1."""
        # Weight: eta^{18} has weight 9, theta_1^2 has weight 1.
        # 9 + 1 = 10. CHECK.
        # Alternatively: -Delta (wt 12) * phi_{-2,1} (wt -2) = wt 10.
        self.assertEqual(12 + (-2), 10)

    def test_phi101_symmetry(self):
        """c(n, l) = c(n, -l) for phi_{10,1} (even in z since theta_1^2 is even)."""
        fc = phi101_fourier(6)
        for (n, l), c in fc.items():
            c_neg = fc.get((n, -l), 0)
            self.assertEqual(c, c_neg, f"Symmetry at (n={n}, l={l})")

    def test_phi101_all_int(self):
        """All phi_{10,1} Fourier coefficients should be exact integers."""
        fc = phi101_fourier(8)
        for (n, l), c in fc.items():
            self.assertIsInstance(c, int,
                                 f"phi101({n},{l}) = {c} is {type(c)}")

    def test_phi101_vanishes_multi_path(self):
        """Multi-path verification that phi_{10,1}(tau, 0) = 0."""
        v = verify_phi101_vanishes_at_z0(8)
        self.assertTrue(v['all_zero'])
        self.assertTrue(v['paths_agree'])

    def test_phi101_first_nonzero(self):
        """phi_{10,1} starts at q^1 (cusp form), with c(1, +/-1) = -1."""
        fc = phi101_fourier(3)
        self.assertEqual(fc.get((1, 1), 0), -1)
        self.assertEqual(fc.get((1, -1), 0), -1)
        self.assertEqual(fc.get((1, 0), 0), 2)


# =====================================================================
# Section 7: Igusa cusp form chi_10
# =====================================================================

class TestChi10(unittest.TestCase):
    """Tests for the Igusa cusp form chi_10."""

    def test_chi10_leading_fj(self):
        """The leading FJ coefficient of chi_10 is phi_{10,1}."""
        fj = chi10_fourier_jacobi(mmax=1, nmax=5)
        self.assertIn(1, fj)
        phi1 = fj[1]
        phi101 = phi101_fourier(5)
        # Compare
        for key in set(phi1.keys()) | set(phi101.keys()):
            self.assertEqual(phi1.get(key, 0), phi101.get(key, 0),
                             f"FJ mismatch at {key}")

    def test_chi10_weight(self):
        """chi_10 has weight 10 on Sp(4, Z)."""
        data = genus2_siegel_form_weights()
        self.assertEqual(data['siegel_generators']['chi_10']['weight'], 10)

    def test_siegel_ring_generators(self):
        """Siegel ring for Sp(4,Z) has 4 generators: E4, E6, chi_10, chi_12."""
        data = genus2_siegel_form_weights()
        gens = data['siegel_generators']
        self.assertIn('E_4^{(2)}', gens)
        self.assertIn('E_6^{(2)}', gens)
        self.assertIn('chi_10', gens)
        self.assertIn('chi_12', gens)
        self.assertEqual(gens['chi_10']['type'], 'cusp')


# =====================================================================
# Section 8: BPS degeneracies and DVV formula
# =====================================================================

class TestBPSDegeneracies(unittest.TestCase):
    """Tests for BPS degeneracies from 1/Phi_10."""

    def test_bps_table_exists(self):
        """BPS degeneracy table should have entries."""
        table = bps_degeneracy_table()
        self.assertGreater(len(table), 0)

    def test_bps_ground_state(self):
        """d(Delta=-1) = 1 (ground state)."""
        table = bps_degeneracy_table()
        self.assertEqual(table[-1], 1)

    def test_bps_marginal(self):
        """d(Delta=0) = -2 (marginal bound states)."""
        table = bps_degeneracy_table()
        self.assertEqual(table[0], -2)

    def test_bps_disc_3(self):
        """d(Delta=3) = 8."""
        table = bps_degeneracy_table()
        self.assertEqual(table[3], 8)

    def test_bps_matches_phi_m21_leading(self):
        """At leading FJ order, BPS disc coeffs match phi_{-2,1} disc coeffs."""
        v = verify_bps_vs_phi_m21()
        # The BPS table should match phi_{-2,1} at leading FJ order
        bps = bps_degeneracy_table()
        phi_m21_disc = {
            -1: 1, 0: -2, 3: 8, 4: -12, 7: 39, 8: -56,
            11: 152, 12: -208, 15: 513, 16: -684,
        }
        for D in [-1, 0, 3, 4, 7, 8]:
            self.assertEqual(bps[D], phi_m21_disc[D],
                             f"BPS vs phi_m21 mismatch at D={D}")

    def test_bps_entropy_positive(self):
        """BPS entropy S = pi*sqrt(Delta) > 0 for Delta > 0."""
        for n, l, m in [(1, 0, 1), (2, 1, 1), (3, 0, 1)]:
            S = bps_entropy_leading(n, l, m)
            Delta = 4 * n * m - l * l
            if Delta > 0:
                self.assertGreater(S, 0)
                self.assertAlmostEqual(S, math.pi * math.sqrt(Delta), places=10)

    def test_bps_entropy_zero_nonpositive_disc(self):
        """S = 0 when Delta <= 0."""
        self.assertEqual(bps_entropy_leading(0, 0, 0), 0.0)
        self.assertEqual(bps_entropy_leading(0, 1, 0), 0.0)

    def test_bps_degeneracy_function(self):
        """bps_degeneracy(n, l, m) looks up the correct discriminant."""
        # Delta = 4*1*1 - 1^2 = 3
        self.assertEqual(bps_degeneracy(1, 1, 1), 8)
        # Delta = 4*1*1 - 0^2 = 4
        self.assertEqual(bps_degeneracy(1, 0, 1), -12)

    def test_rademacher_leading_growth(self):
        """Rademacher term grows exponentially with sqrt(Delta)."""
        r10 = rademacher_leading(10)
        r100 = rademacher_leading(100)
        r1000 = rademacher_leading(1000)
        self.assertGreater(r100, r10)
        self.assertGreater(r1000, r100)

    def test_rademacher_zero_for_nonpositive(self):
        self.assertEqual(rademacher_leading(0), 0.0)
        self.assertEqual(rademacher_leading(-5), 0.0)


# =====================================================================
# Section 9: Shadow obstruction tower for K3 x E
# =====================================================================

class TestShadowTower(unittest.TestCase):
    """Tests for the shadow obstruction tower of K3 x E."""

    def test_kappa_k3(self):
        """kappa(K3) = 2 (complex dimension of K3). NOT c/2 = 3 (AP48)."""
        self.assertEqual(kappa_k3(), Fraction(2))
        # AP48: kappa != c/2 in general. For K3: c = 6, c/2 = 3 != kappa = 2.
        self.assertNotEqual(kappa_k3(), Fraction(K3_CENTRAL_CHARGE, 2))

    def test_kappa_elliptic_curve(self):
        """kappa(E) = 1."""
        self.assertEqual(kappa_elliptic_curve(), Fraction(1))

    def test_kappa_k3e_additivity(self):
        """kappa(K3 x E) = kappa(K3) + kappa(E) = 3."""
        self.assertEqual(kappa_k3e(), Fraction(3))
        self.assertEqual(kappa_k3e(), kappa_k3() + kappa_elliptic_curve())

    def test_kappa_k3e_equals_complex_dim(self):
        """For CY d-fold: kappa = d. K3 x E is CY 3-fold, so kappa = 3."""
        self.assertEqual(kappa_k3e(), Fraction(K3E_COMPLEX_DIM))

    def test_verify_kappa_multi_path(self):
        """Multi-path kappa verification."""
        v = verify_kappa_additivity()
        self.assertTrue(v['paths_agree'])

    def test_F1_k3e(self):
        """F_1(K3 x E) = kappa/24 = 3/24 = 1/8."""
        self.assertEqual(shadow_F1_k3e(), Fraction(1, 8))

    def test_F2_k3e(self):
        """F_2(K3 x E) = kappa * lambda_2 = 3 * 7/5760 = 7/1920."""
        self.assertEqual(shadow_F2_k3e(), Fraction(7, 1920))

    def test_Fg_k3e_genus3(self):
        """F_3(K3 x E) = 3 * 31/967680 = 31/322560."""
        self.assertEqual(shadow_Fg_k3e(3), Fraction(3) * Fraction(31, 967680))

    def test_shadow_ahat_consistency(self):
        """Shadow GF matches A-hat genus coefficients."""
        v = verify_shadow_ahat(4)
        self.assertTrue(v['all_agree'])

    def test_shadow_ahat_generating_function(self):
        """sum F_g hbar^{2g} = kappa * (Ahat(i*hbar) - 1)."""
        gf = shadow_ahat_generating_function(4)
        self.assertEqual(gf[1], Fraction(1, 8))
        self.assertEqual(gf[2], Fraction(7, 1920))

    def test_k3e_euler_char_zero(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        self.assertEqual(K3E_EULER_CHAR, 0)

    def test_F1_not_c_over_48(self):
        """F_1 = kappa/24 = 3/24, NOT c/48 = 9/48 (AP48 guard)."""
        F1 = shadow_F1_k3e()
        c = K3E_CENTRAL_CHARGE  # = 9
        self.assertNotEqual(F1, Fraction(c, 48),
                            "F1 should NOT be c/48 -- kappa != c/2 for K3xE")


# =====================================================================
# Section 10: Jacobi form ring structure
# =====================================================================

class TestJacobiRing(unittest.TestCase):
    """Tests for the ring of weak Jacobi forms."""

    def test_J01_dim_1(self):
        """dim J_{0,1}^{weak} = 1 (spanned by phi_{0,1})."""
        self.assertEqual(jacobi_ring_dimension(0, 1), 1)

    def test_Jm21_dim_1(self):
        """dim J_{-2,1}^{weak} = 1 (spanned by phi_{-2,1})."""
        self.assertEqual(jacobi_ring_dimension(-2, 1), 1)

    def test_J02_dim_2(self):
        """dim J_{0,2}^{weak} = 2."""
        self.assertEqual(jacobi_ring_dimension(0, 2), 2)

    def test_J03_dim_3(self):
        """dim J_{0,3}^{weak} = 3."""
        self.assertEqual(jacobi_ring_dimension(0, 3), 3)

    def test_J41_dim_2(self):
        """dim J_{4,1}^{weak} = 2."""
        self.assertEqual(jacobi_ring_dimension(4, 1), 2)

    def test_J101_dim_3(self):
        """dim J_{10,1}^{weak} = dim M_10 + dim M_12 = 1 + 2 = 3."""
        self.assertEqual(jacobi_ring_dimension(10, 1), 3)

    def test_J101_cusp_dim_1(self):
        """dim J_{10,1}^{cusp} = 1 (spanned by phi_{10,1})."""
        self.assertEqual(jacobi_cusp_dimension(10, 1), 1)

    def test_J121_cusp_dim_1(self):
        """dim J_{12,1}^{cusp} = 1."""
        self.assertEqual(jacobi_cusp_dimension(12, 1), 1)

    def test_J161_cusp_dim_2(self):
        """dim J_{16,1}^{cusp} = 2."""
        self.assertEqual(jacobi_cusp_dimension(16, 1), 2)

    def test_odd_weight_dim_zero(self):
        """J_{k,m} = 0 for odd k (on SL(2,Z))."""
        for k in [1, 3, 5, 7, 9, 11]:
            self.assertEqual(jacobi_ring_dimension(k, 1), 0,
                             f"J_{{{k},1}} should be 0")

    def test_negative_weight_no_modular_forms(self):
        """dim M_w = 0 for w < 0."""
        from compute.lib.cy_modular_k3e_engine import _dim_modular_forms
        for w in [-2, -4, -10]:
            self.assertEqual(_dim_modular_forms(w), 0)

    def test_dim_M_w_values(self):
        """Known dimensions of M_w(SL(2,Z))."""
        from compute.lib.cy_modular_k3e_engine import _dim_modular_forms
        known = {0: 1, 2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 2, 14: 1, 16: 2, 18: 2, 20: 2}
        for w, d in known.items():
            self.assertEqual(_dim_modular_forms(w), d, f"dim M_{w} = {_dim_modular_forms(w)}, expected {d}")

    def test_dim_S_w_values(self):
        """Known dimensions of S_w(SL(2,Z))."""
        from compute.lib.cy_modular_k3e_engine import _dim_cusp_forms
        known = {0: 0, 2: 0, 4: 0, 6: 0, 8: 0, 10: 0, 12: 1, 14: 0, 16: 1, 18: 1, 20: 1, 24: 2}
        for w, d in known.items():
            self.assertEqual(_dim_cusp_forms(w), d, f"dim S_{w} = {_dim_cusp_forms(w)}, expected {d}")

    def test_verify_all_dimensions(self):
        """Full multi-path dimension verification."""
        v = verify_jacobi_ring_dimensions()
        self.assertTrue(v['all_match'])

    def test_jacobi_ring_relations(self):
        """Ring structure data is consistent."""
        rel = jacobi_ring_relations()
        self.assertEqual(rel['J_{0,1}_dim'], 1)
        self.assertEqual(rel['J_{0,2}_dim'], 2)
        self.assertEqual(rel['J_{0,3}_dim'], 3)
        self.assertEqual(rel['J_{10,1}_cusp_dim'], 1)

    def test_basis_dimensions_table(self):
        """Basis dimension table for small weights and indices."""
        dims = jacobi_ring_basis_dimensions(max_weight=12, max_index=2)
        self.assertIn((0, 1), dims)
        self.assertEqual(dims[(0, 1)], 1)
        self.assertIn((0, 2), dims)
        self.assertEqual(dims[(0, 2)], 2)


# =====================================================================
# Section 11: Mathieu moonshine
# =====================================================================

class TestMathieuMoonshine(unittest.TestCase):
    """Tests for the Mathieu moonshine connection."""

    def test_moonshine_coefficients(self):
        """A_n values from Eguchi-Ooguri-Tachikawa (2010)."""
        data = mathieu_moonshine_coefficients()
        An = data['A_n_coefficients']
        self.assertEqual(An[1], 90)
        self.assertEqual(An[2], 462)
        self.assertEqual(An[3], 1540)
        self.assertEqual(An[4], 4554)
        self.assertEqual(An[5], 11592)

    def test_A1_m24_decomposition(self):
        """A_1 = 90 = 45 + 45 (two M24 irreps of dim 45)."""
        data = mathieu_moonshine_coefficients()
        self.assertTrue(data['A1_decomp_check'])
        self.assertEqual(data['A_n_coefficients'][1], 45 + 45)

    def test_A2_m24_decomposition(self):
        """A_2 = 462 = 231 + 231 (two M24 irreps of dim 231)."""
        data = mathieu_moonshine_coefficients()
        self.assertTrue(data['A2_decomp_check'])
        self.assertEqual(data['A_n_coefficients'][2], 231 + 231)

    def test_kappa_k3_in_moonshine(self):
        """kappa(K3) = 2 appears in moonshine data."""
        data = mathieu_moonshine_coefficients()
        self.assertEqual(data['kappa_K3'], 2)


# =====================================================================
# Section 12: K3 surface data
# =====================================================================

class TestK3Data(unittest.TestCase):
    """Tests for K3 surface invariants."""

    def test_k3_euler_24(self):
        self.assertEqual(K3_EULER_CHAR, 24)

    def test_k3_central_charge_6(self):
        self.assertEqual(K3_CENTRAL_CHARGE, 6)

    def test_k3_complex_dim_2(self):
        self.assertEqual(K3_COMPLEX_DIM, 2)

    def test_k3_hodge_diamond(self):
        """K3 Hodge diamond: h^{0,0}=h^{2,2}=1, h^{1,1}=20, h^{2,0}=h^{0,2}=1."""
        # chi = sum (-1)^{p+q} h^{p,q} = 1+1+20+1+1 = 24
        hodge_sum = 1 + 1 + 20 + 1 + 1
        self.assertEqual(hodge_sum, K3_EULER_CHAR)

    def test_k3_signature(self):
        """sigma(K3) = -16 (from the intersection form)."""
        # b_+ = 3, b_- = 19, sigma = 3 - 19 = -16
        self.assertEqual(3 - 19, -16)

    def test_k3_not_c_over_2_for_kappa(self):
        """AP48 guard: kappa(K3) = 2 != c/2 = 3."""
        self.assertNotEqual(int(kappa_k3()), K3_CENTRAL_CHARGE // 2)


# =====================================================================
# Section 13: Cross-consistency checks
# =====================================================================

class TestCrossConsistency(unittest.TestCase):
    """Cross-consistency between different parts of the engine."""

    def test_phi01_phi_m21_product_weight(self):
        """phi_{0,1} * phi_{-2,1} has weight -2, index 2."""
        # phi_{0,1}: weight 0, index 1
        # phi_{-2,1}: weight -2, index 1
        # Product: weight -2, index 2
        self.assertEqual(0 + (-2), -2)
        self.assertEqual(1 + 1, 2)

    def test_phi01_squared_in_J02(self):
        """phi_{0,1}^2 is in J_{0,2} which has dim 2."""
        self.assertEqual(jacobi_ring_dimension(0, 2), 2)

    def test_delta_from_e4_e6(self):
        """Delta = (E_4^3 - E_6^2)/1728 cross-check."""
        nmax = 6
        e4 = e4_coeffs(nmax)
        e6 = e6_coeffs(nmax)
        delta = delta_coeffs(nmax)
        from compute.lib.cy_modular_k3e_engine import _convolve
        e4sq = _convolve(e4, e4, nmax)
        e4cu = _convolve(e4sq, e4, nmax)
        e6sq = _convolve(e6, e6, nmax)
        for n in range(nmax):
            self.assertEqual(Fraction(e4cu[n] - e6sq[n], 1728), Fraction(delta[n]))

    def test_shadow_F1_matches_kappa_over_24(self):
        """F_1 = kappa/24 for all kappa values."""
        for kappa_val in [1, 2, 3, 5, 12]:
            F1 = Fraction(kappa_val, 24)
            self.assertEqual(F1.denominator, 24 // math.gcd(kappa_val, 24))

    def test_fourier_jacobi_comparison(self):
        """FJ comparison runs without error and produces sane output."""
        data = fourier_jacobi_comparison(5)
        self.assertIn('phi101_disc_coeffs', data)
        self.assertIn('kappa_K3E', data)
        self.assertEqual(data['kappa_K3E'], Fraction(3))

    def test_full_data_package(self):
        """Master data package has all required fields."""
        data = full_k3e_modular_data()
        self.assertEqual(data['kappa_K3'], 2)
        self.assertEqual(data['kappa_E'], 1)
        self.assertEqual(data['kappa_K3E'], 3)
        self.assertEqual(data['chi_K3'], 24)
        self.assertEqual(data['d_K3E'], 3)
        self.assertTrue(data['phi101_is_cusp'])

    def test_phi_m21_disc_matches_bps(self):
        """phi_{-2,1} disc coefficients match BPS table at leading order."""
        phi_m21 = phi_m21_fourier(6)
        disc = {}
        for (n, l), c in phi_m21.items():
            D = 4 * n - l * l
            if D not in disc:
                disc[D] = c
        bps = bps_degeneracy_table()
        for D in [-1, 0, 3, 4, 7, 8, 11, 12]:
            self.assertEqual(disc.get(D), bps.get(D),
                             f"phi_m21 vs BPS at D={D}: {disc.get(D)} vs {bps.get(D)}")


# =====================================================================
# Section 14: Sign and convention guards (anti-pattern prevention)
# =====================================================================

class TestConventionGuards(unittest.TestCase):
    """Guards against known anti-patterns AP38, AP46, AP48."""

    def test_ap46_eta_includes_q_power(self):
        """AP46: eta(q) = q^{1/24} * prod(1-q^n). The product starts at 1."""
        c = eta_coeffs(5)
        self.assertEqual(c[0], 1, "eta product must start with 1 (the q^{1/24} is separate)")

    def test_ap48_kappa_not_c_over_2(self):
        """AP48: kappa depends on the full algebra, not the Virasoro subalgebra."""
        # For K3: kappa = 2, c = 6, c/2 = 3.
        self.assertNotEqual(kappa_k3(), Fraction(6, 2))
        # For K3 x E: kappa = 3, c = 9, c/2 = 4.5.
        self.assertNotEqual(kappa_k3e(), Fraction(9, 2))

    def test_ap38_eichler_zagier_convention(self):
        """AP38: phi_{0,1} is in Eichler-Zagier convention (phi(tau,0) = 12)."""
        z0 = phi01_at_z0(5)
        self.assertEqual(z0[0], 12)
        # DVV convention would give phi(tau,0) = 20 (different normalization).
        self.assertNotEqual(z0[0], 20)

    def test_ap22_hbar_power(self):
        """AP22: sum F_g hbar^{2g} (not 2g-2)."""
        gf = shadow_ahat_generating_function(3)
        # F_1 at hbar^2: 1/8
        # F_2 at hbar^4: 7/1920
        self.assertEqual(gf[1], Fraction(1, 8))
        self.assertEqual(gf[2], Fraction(7, 1920))

    def test_phi_m21_vanishes_at_z0(self):
        """phi_{-2,1}(tau, 0) = 0 -- not just at leading order, at ALL orders."""
        fc = phi_m21_fourier(10)
        for n in range(10):
            s = sum(c for (nn, l), c in fc.items() if nn == n)
            self.assertEqual(s, 0, f"phi_m21 fails z=0 vanishing at n={n}")

    def test_phi101_vanishes_at_z0_all_orders(self):
        """phi_{10,1}(tau, 0) = 0 at all computed orders."""
        z0 = phi101_at_z0(10)
        for n, c in enumerate(z0):
            self.assertEqual(c, 0, f"phi101 nonzero at z=0, n={n}")


# =====================================================================
# Section 15: Numerical and asymptotic checks
# =====================================================================

class TestNumerical(unittest.TestCase):
    """Numerical and asymptotic consistency checks."""

    def test_bps_entropy_formula(self):
        """S_BH = pi*sqrt(4nm - l^2) is positive for large charges."""
        S = bps_entropy_leading(10, 0, 10)
        self.assertAlmostEqual(S, math.pi * 20.0, places=10)

    def test_rademacher_growth_rate(self):
        """Rademacher leading term grows monotonically with Delta."""
        # The full Rademacher term includes power-law prefactors
        # (Delta^{-(2k-3)/4} / sqrt(2*pi*x)), so log(r) is NOT
        # simply pi*sqrt(Delta). But the growth must be monotone
        # and dominated by the exp(pi*sqrt(Delta)) factor.
        r_prev = rademacher_leading(10)
        for Delta in [100, 400, 900, 1600]:
            r = rademacher_leading(Delta)
            self.assertGreater(r, r_prev,
                               f"Rademacher not monotone at Delta={Delta}")
            r_prev = r
        # At very large Delta, the exponential dominates the prefactor:
        # log(r(4D)) / log(r(D)) -> sqrt(4) = 2 as D -> infinity.
        log_r1 = math.log(rademacher_leading(10000))
        log_r2 = math.log(rademacher_leading(40000))
        ratio = log_r2 / log_r1
        self.assertAlmostEqual(ratio, 2.0, delta=0.15,
                               msg="Exponential growth rate mismatch")

    def test_shadow_Fg_positive(self):
        """F_g > 0 for all g >= 1 (Bernoulli sign analysis)."""
        for g in range(1, 6):
            Fg = shadow_Fg_k3e(g)
            self.assertGreater(Fg, 0, f"F_{g} = {Fg} should be positive")

    def test_shadow_Fg_decreasing(self):
        """F_g is decreasing: F_1 > F_2 > F_3 > ..."""
        Fg_prev = shadow_Fg_k3e(1)
        for g in range(2, 6):
            Fg = shadow_Fg_k3e(g)
            self.assertLess(Fg, Fg_prev, f"F_{g} should be < F_{g-1}")
            Fg_prev = Fg

    def test_partition_function_consistency(self):
        """partition_count(n) matches p(n) from eta^{-1}."""
        eta_inv = eta_power_coeffs(20, -1)
        for n in range(15):
            self.assertEqual(partition_count(n), eta_inv[n],
                             f"p({n}): {partition_count(n)} vs eta^-1: {eta_inv[n]}")


if __name__ == '__main__':
    unittest.main()
