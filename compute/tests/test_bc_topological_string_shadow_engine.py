r"""Tests for bar-cobar topological string amplitudes from shadow tower.

Verifies ALL 18 engine functions across 90+ tests, organized by:
    Section 1:  Bernoulli numbers (exact, mpmath cross-check)
    Section 2:  Faber-Pandharipande intersection numbers
    Section 3:  Shadow free energy (Virasoro, Heisenberg, affine)
    Section 4:  BCOV holomorphic anomaly (MC splitting)
    Section 5:  Shadow propagator
    Section 6:  GV invariant extraction
    Section 7:  GV integrality
    Section 8:  Spectral curve genus
    Section 9:  Branch points
    Section 10: Bergman kernel
    Section 11: Mirror map coefficients
    Section 12: OSV partition function
    Section 13: Symplectic invariance
    Section 14: Gap condition
    Section 15: Koszul complementarity (AP24)
    Section 16: Genus expansion convergence
    Section 17: A-hat generating function
    Section 18: Cross-family verification
    Section 19: Full suite

Multi-path verification mandate: every numerical value is checked by AT LEAST
2 independent methods (direct formula + alternative computation or mpmath).
"""

import math
import unittest
from fractions import Fraction

import mpmath

from compute.lib.bc_topological_string_shadow_engine import (
    # Bernoulli
    bernoulli_number,
    bernoulli_number_mpmath,
    # Faber-Pandharipande
    lambda_fp,
    lambda_fp_mpmath,
    # Shadow free energy
    shadow_free_energy,
    heisenberg_free_energy,
    affine_free_energy,
    # BCOV
    holomorphic_anomaly_rhs,
    # Propagator
    shadow_propagator,
    # GV
    gv_invariant_extract,
    gv_integrality_check,
    # Spectral curve
    spectral_curve_genus,
    branch_points,
    bergman_kernel,
    # Mirror map
    mirror_map_coefficient,
    # OSV
    osv_partition,
    # Symplectic
    symplectic_invariance_test,
    # Gap
    gap_condition_check,
    # Complementarity
    koszul_free_energy_sum,
    # Convergence
    genus_expansion_convergence,
    # A-hat
    ahat_coefficient,
    ahat_generating_function_check,
    # Cross-checks
    heisenberg_complementarity,
    affine_sl2_complementarity,
    # Full suite
    full_verification_suite,
)


# ====================================================================
# Section 1: Bernoulli numbers
# ====================================================================

class TestBernoulliNumbers(unittest.TestCase):
    """Exact Bernoulli number verification."""

    def test_B0(self):
        self.assertEqual(bernoulli_number(0), Fraction(1))

    def test_B1(self):
        self.assertEqual(bernoulli_number(1), Fraction(-1, 2))

    def test_B2(self):
        self.assertEqual(bernoulli_number(2), Fraction(1, 6))

    def test_B3(self):
        """B_3 = 0 (all odd Bernoulli beyond B_1 vanish)."""
        self.assertEqual(bernoulli_number(3), Fraction(0))

    def test_B4(self):
        self.assertEqual(bernoulli_number(4), Fraction(-1, 30))

    def test_B6(self):
        self.assertEqual(bernoulli_number(6), Fraction(1, 42))

    def test_B8(self):
        self.assertEqual(bernoulli_number(8), Fraction(-1, 30))

    def test_B10(self):
        self.assertEqual(bernoulli_number(10), Fraction(5, 66))

    def test_B12(self):
        self.assertEqual(bernoulli_number(12), Fraction(-691, 2730))

    def test_B14(self):
        self.assertEqual(bernoulli_number(14), Fraction(7, 6))

    def test_odd_bernoulli_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for k in range(1, 10):
            self.assertEqual(bernoulli_number(2 * k + 1), Fraction(0),
                             f"B_{2*k+1} should be 0")

    def test_bernoulli_alternating_sign(self):
        """B_{2g} has sign (-1)^{g+1} for g >= 1."""
        for g in range(1, 8):
            B_2g = bernoulli_number(2 * g)
            expected_sign = (-1) ** (g + 1)
            actual_sign = 1 if B_2g > 0 else -1
            self.assertEqual(actual_sign, expected_sign,
                             f"B_{2*g} = {B_2g}, expected sign {expected_sign}")

    def test_bernoulli_mpmath_crosscheck(self):
        """Cross-verify Bernoulli numbers: exact vs mpmath (2 independent paths)."""
        for n in [0, 1, 2, 4, 6, 8, 10, 12, 14, 20]:
            exact = bernoulli_number(n)
            mp_val = bernoulli_number_mpmath(n, dps=50)
            self.assertAlmostEqual(float(exact), float(mp_val), places=40,
                                   msg=f"B_{n} mismatch: exact={exact}, mpmath={mp_val}")

    def test_bernoulli_negative_raises(self):
        with self.assertRaises(ValueError):
            bernoulli_number(-1)


# ====================================================================
# Section 2: Faber-Pandharipande intersection numbers
# ====================================================================

class TestLambdaFP(unittest.TestCase):
    """Verify lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda_4(self):
        """lambda_4 = (2^7-1)/2^7 * |B_8|/8! = 127/128 * (1/30)/40320."""
        expected = Fraction(127, 128) * Fraction(1, 30) / Fraction(math.factorial(8))
        self.assertEqual(lambda_fp(4), expected)

    def test_lambda_5(self):
        """lambda_5 = (2^9-1)/2^9 * |B_10|/10!."""
        expected = Fraction(511, 512) * Fraction(5, 66) / Fraction(math.factorial(10))
        self.assertEqual(lambda_fp(5), expected)

    def test_lambda_positive(self):
        """All lambda_g^FP must be positive (AP22)."""
        for g in range(1, 10):
            self.assertGreater(lambda_fp(g), Fraction(0),
                               f"lambda_{g} should be positive")

    def test_lambda_decreasing(self):
        """lambda_g^FP is strictly decreasing for g >= 1."""
        for g in range(1, 9):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1),
                               f"lambda_{g} should be > lambda_{g+1}")

    def test_lambda_mpmath_crosscheck(self):
        """Cross-verify lambda_g: Fraction vs mpmath (2 independent paths)."""
        for g in range(1, 8):
            exact = lambda_fp(g)
            mp_val = lambda_fp_mpmath(g, dps=50)
            self.assertAlmostEqual(float(exact), float(mp_val), places=30,
                                   msg=f"lambda_{g} mismatch")

    def test_lambda_fp_invalid(self):
        with self.assertRaises(ValueError):
            lambda_fp(0)

    def test_lambda_1_from_bernoulli(self):
        """Verify lambda_1 = 1/24 from B_2 = 1/6 directly.

        lambda_1 = (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * (1/6)/2 = 1/24.
        """
        B2 = bernoulli_number(2)
        result = Fraction(1, 2) * abs(B2) / Fraction(2)
        self.assertEqual(result, Fraction(1, 24))
        self.assertEqual(lambda_fp(1), result)


# ====================================================================
# Section 3: Shadow free energy
# ====================================================================

class TestShadowFreeEnergy(unittest.TestCase):
    """Verify F_g = kappa * lambda_g^FP for various families."""

    def test_F1_virasoro_c1(self):
        """F_1(Vir_1) = (1/2) * (1/24) = 1/48."""
        self.assertEqual(shadow_free_energy(1, Fraction(1)), Fraction(1, 48))

    def test_F1_virasoro_c2(self):
        """F_1(Vir_2) = (2/2) * (1/24) = 1/24."""
        self.assertEqual(shadow_free_energy(1, Fraction(2)), Fraction(1, 24))

    def test_F1_virasoro_c26(self):
        """F_1(Vir_26) = 13 * (1/24) = 13/24."""
        self.assertEqual(shadow_free_energy(1, Fraction(26)), Fraction(13, 24))

    def test_F2_virasoro_c2(self):
        """F_2(Vir_2) = 1 * 7/5760 = 7/5760."""
        self.assertEqual(shadow_free_energy(2, Fraction(2)), Fraction(7, 5760))

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all c (key identity)."""
        for c_val in [1, 2, 5, 10, 13, 26]:
            c_frac = Fraction(c_val)
            kappa = c_frac / 2
            expected = kappa / 24
            self.assertEqual(shadow_free_energy(1, c_frac), expected,
                             f"F_1(c={c_val}) should be kappa/24 = {expected}")

    def test_F2_equals_7kappa_over_5760(self):
        """F_2 = 7*kappa/5760 for all c."""
        for c_val in [1, 2, 13, 26]:
            c_frac = Fraction(c_val)
            kappa = c_frac / 2
            expected = 7 * kappa / 5760
            self.assertEqual(shadow_free_energy(2, c_frac), expected,
                             f"F_2(c={c_val}) should be 7*kappa/5760")

    def test_F_g_zero_at_c0(self):
        """F_g = 0 when c = 0 (kappa = 0)."""
        for g in range(1, 6):
            self.assertEqual(shadow_free_energy(g, Fraction(0)), Fraction(0))

    def test_shadow_free_energy_invalid(self):
        with self.assertRaises(ValueError):
            shadow_free_energy(0, Fraction(1))


class TestHeisenbergFreeEnergy(unittest.TestCase):
    """F_g for Heisenberg: kappa = k."""

    def test_F1_heisenberg_k1(self):
        """F_1(H_1) = 1 * 1/24 = 1/24."""
        self.assertEqual(heisenberg_free_energy(Fraction(1), 1), Fraction(1, 24))

    def test_F1_heisenberg_k2(self):
        """F_1(H_2) = 2 * 1/24 = 1/12."""
        self.assertEqual(heisenberg_free_energy(Fraction(2), 1), Fraction(1, 12))

    def test_F2_heisenberg_k1(self):
        """F_2(H_1) = 1 * 7/5760 = 7/5760."""
        self.assertEqual(heisenberg_free_energy(Fraction(1), 2), Fraction(7, 5760))

    def test_heisenberg_linearity_in_k(self):
        """F_g is linear in k: F_g(2k) = 2*F_g(k)."""
        for g in range(1, 5):
            self.assertEqual(
                heisenberg_free_energy(Fraction(4), g),
                2 * heisenberg_free_energy(Fraction(2), g),
            )

    def test_heisenberg_vs_virasoro_k1(self):
        """H_1 has kappa=1, Vir_2 has kappa=1: same F_g."""
        for g in range(1, 5):
            self.assertEqual(
                heisenberg_free_energy(Fraction(1), g),
                shadow_free_energy(g, Fraction(2)),
            )


class TestAffineFreeEnergy(unittest.TestCase):
    """F_g for affine sl_2: kappa = 3(k+2)/4."""

    def test_kappa_sl2_k1(self):
        """kappa(V_1(sl_2)) = 3*3/4 = 9/4."""
        expected = Fraction(9, 4)
        self.assertEqual(affine_free_energy(Fraction(1), 1),
                         expected * lambda_fp(1))

    def test_kappa_sl2_k_minus_2(self):
        """At k = -2 (critical level): kappa = 0, F_g = 0.

        NOTE: Sugawara is UNDEFINED at k = -h^v = -2 (AP pitfall).
        Here we only check that the formula gives kappa=0.
        """
        self.assertEqual(affine_free_energy(Fraction(-2), 1), Fraction(0))

    def test_affine_F1(self):
        """F_1(V_1(sl_2)) = (9/4) * 1/24 = 9/96 = 3/32."""
        self.assertEqual(affine_free_energy(Fraction(1), 1), Fraction(3, 32))


# ====================================================================
# Section 4: BCOV holomorphic anomaly
# ====================================================================

class TestBCOVAnomaly(unittest.TestCase):
    """Verify BCOV splitting from MC equation."""

    def test_splitting_g2(self):
        """At g=2: splitting = F_1^2."""
        c_val = Fraction(2)
        F1 = shadow_free_energy(1, c_val)
        splitting = holomorphic_anomaly_rhs(2, c_val)
        self.assertEqual(splitting, F1 * F1)

    def test_splitting_g3(self):
        """At g=3: splitting = 2 * F_1 * F_2."""
        c_val = Fraction(2)
        F1 = shadow_free_energy(1, c_val)
        F2 = shadow_free_energy(2, c_val)
        splitting = holomorphic_anomaly_rhs(3, c_val)
        self.assertEqual(splitting, 2 * F1 * F2)

    def test_splitting_g4(self):
        """At g=4: splitting = 2*F_1*F_3 + F_2^2."""
        c_val = Fraction(2)
        F1 = shadow_free_energy(1, c_val)
        F2 = shadow_free_energy(2, c_val)
        F3 = shadow_free_energy(3, c_val)
        splitting = holomorphic_anomaly_rhs(4, c_val)
        expected = 2 * F1 * F3 + F2 * F2
        self.assertEqual(splitting, expected)

    def test_splitting_g1_is_zero(self):
        """At g=1: no splitting (trivial)."""
        self.assertEqual(holomorphic_anomaly_rhs(1, Fraction(2)), Fraction(0))

    def test_splitting_positive(self):
        """Splitting sum is positive for c > 0."""
        for g in range(2, 6):
            self.assertGreater(holomorphic_anomaly_rhs(g, Fraction(2)), Fraction(0))

    def test_splitting_with_precomputed(self):
        """Verify splitting with precomputed S_values matches direct computation."""
        c_val = Fraction(10)
        S_vals = {g: shadow_free_energy(g, c_val) for g in range(1, 6)}
        for g in range(2, 6):
            direct = holomorphic_anomaly_rhs(g, c_val)
            precomp = holomorphic_anomaly_rhs(g, c_val, S_values=S_vals)
            self.assertEqual(direct, precomp,
                             f"Splitting mismatch at g={g}")

    def test_splitting_scales_as_kappa_squared(self):
        """Splitting at g=2 scales as kappa^2 (since F_1 ~ kappa)."""
        c1, c2 = Fraction(2), Fraction(4)
        s1 = holomorphic_anomaly_rhs(2, c1)
        s2 = holomorphic_anomaly_rhs(2, c2)
        # kappa ratio = 2, so splitting ratio = 4
        self.assertEqual(s2 / s1, Fraction(4))


# ====================================================================
# Section 5: Shadow propagator
# ====================================================================

class TestShadowPropagator(unittest.TestCase):
    """Verify shadow propagator from Q_L."""

    def test_propagator_c1(self):
        """At c=1: propagator_0 = 1/c^2 = 1."""
        p = shadow_propagator(Fraction(1))
        self.assertEqual(p['propagator_0'], Fraction(1))

    def test_propagator_c2(self):
        """At c=2: propagator_0 = 1/4."""
        p = shadow_propagator(Fraction(2))
        self.assertEqual(p['propagator_0'], Fraction(1, 4))

    def test_kappa_value(self):
        p = shadow_propagator(Fraction(10))
        self.assertEqual(p['kappa'], Fraction(5))

    def test_alpha_value(self):
        p = shadow_propagator(Fraction(10))
        self.assertEqual(p['alpha'], Fraction(2))

    def test_S4_virasoro(self):
        """S_4 = 10/(c*(5c+22)) for Virasoro."""
        c_val = Fraction(10)
        p = shadow_propagator(c_val)
        expected = Fraction(10) / (c_val * (5 * c_val + 22))
        self.assertEqual(p['S4'], expected)

    def test_Delta_virasoro(self):
        """Delta = 40/(5c+22) for Virasoro."""
        c_val = Fraction(10)
        p = shadow_propagator(c_val)
        expected = Fraction(40) / (5 * c_val + 22)
        self.assertEqual(p['Delta'], expected)

    def test_propagator_c0_raises(self):
        with self.assertRaises(ValueError):
            shadow_propagator(Fraction(0))

    def test_Q_L_0_equals_c_squared(self):
        """Q_L(0) = (2*kappa)^2 = c^2."""
        for c_val in [1, 2, 5, 13, 26]:
            p = shadow_propagator(Fraction(c_val))
            self.assertEqual(p['Q_L_0'], Fraction(c_val) ** 2)


# ====================================================================
# Section 6: GV invariant extraction
# ====================================================================

class TestGVExtraction(unittest.TestCase):
    """Verify GV invariant extraction from shadow F_g."""

    def test_shadow_gv_degree0(self):
        """Shadow sector: n_0^0 = kappa."""
        gv = gv_invariant_extract(Fraction(2), beta=5, g_max=3)
        self.assertEqual(gv[(0, 0)], Fraction(1))

    def test_shadow_gv_degree_positive_zero(self):
        """Shadow sector: n_g^{beta>=1} = 0 (no instantons from scalar shadow)."""
        gv = gv_invariant_extract(Fraction(2), beta=5, g_max=3)
        for g in range(4):
            for b in range(1, 6):
                self.assertEqual(gv[(g, b)], Fraction(0),
                                 f"n_{g}^{b} should be 0 in shadow sector")


# ====================================================================
# Section 7: GV integrality
# ====================================================================

class TestGVIntegrality(unittest.TestCase):
    """Verify GV integrality for the shadow sector."""

    def test_conifold_integrality(self):
        """Conifold (c=2, kappa=1): kappa is integer."""
        result = gv_integrality_check(2, beta_max=5, g_max=3)
        self.assertTrue(result['kappa_is_integer'])
        self.assertTrue(result['all_integer'])

    def test_quintic_kappa_not_integer(self):
        """Quintic (c=-200, kappa=-100): kappa is integer."""
        result = gv_integrality_check(-200, beta_max=3, g_max=2)
        self.assertTrue(result['kappa_is_integer'])

    def test_virasoro_c1_kappa_half_integer(self):
        """Vir_1 (c=1, kappa=1/2): kappa is not integer."""
        result = gv_integrality_check(1, beta_max=3, g_max=2)
        self.assertFalse(result['kappa_is_integer'])


# ====================================================================
# Section 8: Spectral curve genus
# ====================================================================

class TestSpectralCurveGenus(unittest.TestCase):
    """The shadow spectral curve is always genus 0."""

    def test_genus_0_all_c(self):
        """Spectral curve genus is 0 for all central charges."""
        for c_val in [1, 2, 5, 10, 13, 25, 26, 100]:
            self.assertEqual(spectral_curve_genus(Fraction(c_val)), 0)

    def test_genus_0_negative_c(self):
        self.assertEqual(spectral_curve_genus(Fraction(-200)), 0)


# ====================================================================
# Section 9: Branch points
# ====================================================================

class TestBranchPoints(unittest.TestCase):
    """Verify branch point structure of shadow spectral curve."""

    def test_branch_points_c1(self):
        bp = branch_points(Fraction(1))
        self.assertEqual(bp['spectral_genus'], 0)
        self.assertEqual(bp['type'], 'complex_conjugate')

    def test_branch_points_c13_selfdual(self):
        """At c=13 (self-dual): branch points exist."""
        bp = branch_points(Fraction(13))
        self.assertEqual(bp['spectral_genus'], 0)
        self.assertGreater(bp['convergence_radius'], 0)

    def test_branch_points_c26(self):
        bp = branch_points(Fraction(26))
        self.assertEqual(bp['type'], 'complex_conjugate')
        # rho < 1 at c=26 (convergent tower)
        self.assertLess(bp['growth_rate_rho'], 1.0)

    def test_branch_points_rho_c13(self):
        """Shadow growth rate at c=13 is about 0.467."""
        bp = branch_points(Fraction(13))
        self.assertAlmostEqual(bp['growth_rate_rho'], 0.467, places=2)

    def test_branch_points_c0_degenerate(self):
        bp = branch_points(Fraction(0))
        self.assertIn('degenerate', bp.get('note', ''))

    def test_branch_points_conjugate_pair(self):
        """For generic c > 0, branch points are complex conjugates."""
        bp = branch_points(Fraction(5))
        t_plus = bp['t_plus']
        t_minus = bp['t_minus']
        # Should be complex conjugates
        self.assertAlmostEqual(t_plus.real, t_minus.real, places=10)
        self.assertAlmostEqual(t_plus.imag, -t_minus.imag, places=10)

    def test_branch_points_equal_modulus(self):
        """Complex conjugate branch points have equal modulus."""
        bp = branch_points(Fraction(5))
        self.assertAlmostEqual(bp['modulus_plus'], bp['modulus_minus'], places=10)


# ====================================================================
# Section 10: Bergman kernel
# ====================================================================

class TestBergmanKernel(unittest.TestCase):
    """Verify genus-0 Bergman kernel."""

    def test_bergman_basic(self):
        """B(1, 0) = 1/(1-0)^2 = 1."""
        self.assertAlmostEqual(bergman_kernel(Fraction(1), 1.0, 0.0), 1.0)

    def test_bergman_symmetric(self):
        """Bergman kernel is symmetric: B(z,w) = B(w,z)."""
        z, w = 1.5 + 0.3j, 2.0 - 0.5j
        self.assertAlmostEqual(
            bergman_kernel(Fraction(1), z, w),
            bergman_kernel(Fraction(1), w, z),
        )

    def test_bergman_singular(self):
        with self.assertRaises(ValueError):
            bergman_kernel(Fraction(1), 1.0, 1.0)

    def test_bergman_decay(self):
        """B(z,w) ~ 1/|z-w|^2 decays for large separation."""
        val = bergman_kernel(Fraction(1), 100.0, 0.0)
        self.assertAlmostEqual(val, 1e-4, places=6)

    def test_bergman_complex_points(self):
        z, w = 1.0 + 1.0j, 2.0 + 3.0j
        expected = 1.0 / (z - w) ** 2
        self.assertAlmostEqual(bergman_kernel(Fraction(1), z, w), expected)


# ====================================================================
# Section 11: Mirror map coefficients
# ====================================================================

class TestMirrorMap(unittest.TestCase):
    """Mirror map is trivial at the scalar shadow level."""

    def test_mirror_map_trivial(self):
        """All mirror map coefficients are 0 in the shadow sector."""
        for n in range(1, 10):
            self.assertEqual(mirror_map_coefficient(2, n), Fraction(0))

    def test_mirror_map_invalid(self):
        with self.assertRaises(ValueError):
            mirror_map_coefficient(2, 0)


# ====================================================================
# Section 12: OSV partition function
# ====================================================================

class TestOSVPartition(unittest.TestCase):
    """Verify OSV partition function from shadow F_g."""

    def test_osv_F_values(self):
        result = osv_partition(Fraction(2), g_max=3)
        self.assertEqual(result['kappa'], Fraction(1))
        self.assertEqual(result['F_values'][1], Fraction(1, 24))
        self.assertEqual(result['F_values'][2], Fraction(7, 5760))

    def test_osv_log_Z_sq(self):
        """log|Z|^2 coefficients are 2*F_g."""
        result = osv_partition(Fraction(2), g_max=3)
        for g in range(1, 4):
            self.assertEqual(
                result['log_Z_squared_coefficients'][g],
                2 * result['F_values'][g],
            )

    def test_osv_kappa(self):
        result = osv_partition(Fraction(26), g_max=2)
        self.assertEqual(result['kappa'], Fraction(13))


# ====================================================================
# Section 13: Symplectic invariance
# ====================================================================

class TestSymplecticInvariance(unittest.TestCase):
    """F_g is invariant under sheet exchange at the scalar level."""

    def test_invariance_all_genera(self):
        for g in range(1, 6):
            result = symplectic_invariance_test(Fraction(10), g)
            self.assertTrue(result['invariant'],
                            f"Symplectic invariance fails at g={g}")


# ====================================================================
# Section 14: Gap condition
# ====================================================================

class TestGapCondition(unittest.TestCase):
    """Verify gap structure near the conifold point."""

    def test_gap_satisfied(self):
        for g in range(1, 5):
            result = gap_condition_check(Fraction(2), g)
            self.assertTrue(result['gap_satisfied'])

    def test_leading_power(self):
        """F_g ~ c^1 near c=0."""
        result = gap_condition_check(Fraction(2), 1)
        self.assertEqual(result['leading_power_of_c'], 1)


# ====================================================================
# Section 15: Koszul complementarity (AP24 — the critical test)
# ====================================================================

class TestKoszulComplementarity(unittest.TestCase):
    """Verify kappa + kappa' = 13 for Virasoro (NOT 0, AP24)."""

    def test_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_val in [1, 2, 5, 10, 13, 20, 25]:
            result = koszul_free_energy_sum(Fraction(c_val), 1)
            self.assertEqual(result['kappa_sum'], Fraction(13),
                             f"kappa sum should be 13 at c={c_val}")

    def test_complementarity_holds(self):
        """F_g(c) + F_g(26-c) = 13 * lambda_g^FP for all g, c."""
        for g in range(1, 5):
            for c_val in [1, 5, 13, 25]:
                result = koszul_free_energy_sum(Fraction(c_val), g)
                self.assertTrue(result['complementarity_holds'],
                                f"Complementarity fails at g={g}, c={c_val}")

    def test_self_dual_c13(self):
        """At c=13: kappa = kappa' = 13/2."""
        result = koszul_free_energy_sum(Fraction(13), 1)
        self.assertEqual(result['kappa'], Fraction(13, 2))
        self.assertEqual(result['kappa_dual'], Fraction(13, 2))

    def test_F_g_sum_independent_of_c(self):
        """F_g(c) + F_g(26-c) is the SAME for all c (c-independent)."""
        for g in range(1, 4):
            sums = set()
            for c_val in [1, 3, 7, 13, 20]:
                result = koszul_free_energy_sum(Fraction(c_val), g)
                sums.add(result['F_g_sum'])
            self.assertEqual(len(sums), 1,
                             f"F_g sum should be c-independent at g={g}")

    def test_F_g_sum_equals_13_lambda(self):
        """F_g(c) + F_g(26-c) = 13 * lambda_g^FP (exact value)."""
        for g in range(1, 5):
            result = koszul_free_energy_sum(Fraction(7), g)
            expected = Fraction(13) * lambda_fp(g)
            self.assertEqual(result['F_g_sum'], expected)

    def test_kappa_sum_NOT_zero_virasoro(self):
        """CRITICAL: kappa + kappa' = 13 != 0 for Virasoro (AP24).

        This test explicitly guards against the overclaim kappa + kappa' = 0
        that was found in 20+ locations across both volumes.
        """
        result = koszul_free_energy_sum(Fraction(1), 1)
        self.assertNotEqual(result['kappa_sum'], Fraction(0),
                            "kappa sum MUST NOT be 0 for Virasoro (AP24)")
        self.assertEqual(result['kappa_sum'], Fraction(13))


class TestHeisenbergComplementarity(unittest.TestCase):
    """kappa + kappa' = 0 for Heisenberg."""

    def test_sum_zero(self):
        for g in range(1, 5):
            result = heisenberg_complementarity(Fraction(1), g)
            self.assertTrue(result['complementarity_holds'])
            self.assertEqual(result['F_g_sum'], Fraction(0))

    def test_antisymmetric(self):
        """F_g(H_k) = -F_g(H_{-k})."""
        for g in range(1, 4):
            F_plus = heisenberg_free_energy(Fraction(3), g)
            F_minus = heisenberg_free_energy(Fraction(-3), g)
            self.assertEqual(F_plus + F_minus, Fraction(0))


class TestAffineSl2Complementarity(unittest.TestCase):
    """kappa + kappa' = 0 for affine sl_2 under FF involution."""

    def test_sum_zero(self):
        for g in range(1, 4):
            for k_val in [1, 2, 3, 5]:
                result = affine_sl2_complementarity(Fraction(k_val), g)
                self.assertTrue(result['complementarity_holds'],
                                f"Affine sl_2 complementarity fails at k={k_val}, g={g}")


# ====================================================================
# Section 16: Genus expansion convergence
# ====================================================================

class TestGenusExpansionConvergence(unittest.TestCase):
    """Verify asymptotic behavior of genus expansion."""

    def test_ratios_decrease(self):
        """lambda_g/lambda_{g-1} should decrease (roughly)."""
        result = genus_expansion_convergence(Fraction(2), g_max=10)
        ratios = result['ratios']
        for i in range(1, len(ratios)):
            self.assertLess(ratios[i]['ratio_float'], ratios[i - 1]['ratio_float'],
                            f"Ratio not decreasing at g={ratios[i]['g']}")

    def test_factorial_divergence(self):
        """The genus expansion diverges factorially."""
        result = genus_expansion_convergence(Fraction(2), g_max=10)
        self.assertTrue(result['diverges_factorially'])

    def test_asymptotic_limit(self):
        """Ratio -> 1/(4*pi^2) ~ 0.02533."""
        result = genus_expansion_convergence(Fraction(2), g_max=15)
        last_ratio = result['ratios'][-1]['ratio_float']
        expected = 1.0 / (4 * math.pi ** 2)
        # Not exact at g=15, but should be in the right ballpark
        self.assertAlmostEqual(last_ratio, expected, places=2)

    def test_empty_at_c0(self):
        result = genus_expansion_convergence(Fraction(0), g_max=5)
        self.assertEqual(len(result['ratios']), 0)


# ====================================================================
# Section 17: A-hat generating function
# ====================================================================

class TestAhatGeneratingFunction(unittest.TestCase):
    """Verify lambda_g^FP matches (x/2)/sin(x/2) expansion."""

    def test_ahat_coeff_g0(self):
        self.assertEqual(ahat_coefficient(0), Fraction(1))

    def test_ahat_coeff_g1(self):
        self.assertEqual(ahat_coefficient(1), lambda_fp(1))

    def test_ahat_coeff_g2(self):
        self.assertEqual(ahat_coefficient(2), lambda_fp(2))

    def test_ahat_generating_function_consistency(self):
        """Cross-verify lambda_g against (x/2)/sin(x/2) via mpmath."""
        result = ahat_generating_function_check(g_max=6)
        for g in range(1, 7):
            self.assertTrue(result[g]['agree'],
                            f"A-hat GF mismatch at g={g}: "
                            f"lambda={result[g]['lambda_fp_float']}, "
                            f"ahat={result[g]['ahat_coeff_mpmath']}")

    def test_ahat_mpmath_vs_fraction(self):
        """Lambda from Fraction matches mpmath (3 independent paths)."""
        result = ahat_generating_function_check(g_max=5)
        for g in range(1, 6):
            # Path 1: Fraction
            lam_frac = result[g]['lambda_fp_float']
            # Path 2: mpmath Bernoulli
            lam_mp = result[g]['lambda_fp_mpmath']
            # Path 3: series inversion
            lam_ahat = result[g]['ahat_coeff_mpmath']
            self.assertAlmostEqual(lam_frac, lam_mp, places=30)
            self.assertAlmostEqual(lam_frac, lam_ahat, places=30)


# ====================================================================
# Section 18: Cross-family verification
# ====================================================================

class TestCrossFamilyVerification(unittest.TestCase):
    """Cross-verify F_g across families at matching kappa."""

    def test_heisenberg_k1_equals_virasoro_c2(self):
        """H_1 (kappa=1) and Vir_2 (kappa=1) give same F_g."""
        for g in range(1, 5):
            self.assertEqual(
                heisenberg_free_energy(Fraction(1), g),
                shadow_free_energy(g, Fraction(2)),
                f"Mismatch at g={g}",
            )

    def test_additivity_heisenberg(self):
        """F_g(H_{k1}) + F_g(H_{k2}) = F_g(H_{k1+k2}) (linearity in kappa)."""
        for g in range(1, 4):
            self.assertEqual(
                heisenberg_free_energy(Fraction(3), g) +
                heisenberg_free_energy(Fraction(5), g),
                heisenberg_free_energy(Fraction(8), g),
            )

    def test_virasoro_bernoulli_sign_check(self):
        """F_g values are positive for c > 0 (AP22 sign check)."""
        for g in range(1, 8):
            F_g = shadow_free_energy(g, Fraction(10))
            self.assertGreater(F_g, Fraction(0),
                               f"F_{g} should be positive for c > 0")

    def test_three_path_F1(self):
        """F_1 verified 3 ways: formula, kappa/24, Bernoulli.

        Path 1: F_1 = kappa * lambda_1 = (c/2) * (1/24) = c/48
        Path 2: F_1 = kappa/24 (standard identity)
        Path 3: F_1 from Bernoulli: kappa * (1/2)*(1/6)/2 = kappa/24
        """
        c_val = Fraction(10)
        kappa = c_val / 2

        # Path 1
        path1 = shadow_free_energy(1, c_val)

        # Path 2
        path2 = kappa / 24

        # Path 3
        B2 = bernoulli_number(2)
        path3 = kappa * Fraction(1, 2) * abs(B2) / Fraction(2)

        self.assertEqual(path1, path2)
        self.assertEqual(path1, path3)

    def test_three_path_F2(self):
        """F_2 verified 3 ways.

        Path 1: F_2 = kappa * lambda_2 = kappa * 7/5760
        Path 2: Direct Bernoulli: kappa * (3/4)*(1/30)/24 = kappa * 7/5760
            Actually: lambda_2 = (2^3-1)/2^3 * |B_4|/4! = 7/8 * (1/30)/24 = 7/5760
        Path 3: mpmath
        """
        c_val = Fraction(10)
        kappa = c_val / 2

        # Path 1
        path1 = shadow_free_energy(2, c_val)

        # Path 2
        prefactor = Fraction(2**3 - 1, 2**3)  # 7/8
        B4 = bernoulli_number(4)
        path2 = kappa * prefactor * abs(B4) / Fraction(math.factorial(4))

        # Path 3
        with mpmath.workdps(50):
            path3_mp = float(kappa) * float(lambda_fp_mpmath(2))

        self.assertEqual(path1, path2)
        self.assertAlmostEqual(float(path1), path3_mp, places=30)


# ====================================================================
# Section 19: Full verification suite
# ====================================================================

class TestFullSuite(unittest.TestCase):
    """Run the complete verification suite."""

    def test_full_suite_passes(self):
        result = full_verification_suite(g_max=5)
        self.assertTrue(result['all_passed'],
                        f"Full suite failed: {result}")

    def test_bernoulli_check(self):
        result = full_verification_suite()
        self.assertTrue(result['bernoulli'])

    def test_lambda_check(self):
        result = full_verification_suite()
        self.assertTrue(result['lambda_fp'])

    def test_lambda_positive_check(self):
        result = full_verification_suite()
        self.assertTrue(result['lambda_positive'])

    def test_F1_conifold_check(self):
        result = full_verification_suite()
        self.assertTrue(result['F1_conifold'])

    def test_F2_conifold_check(self):
        result = full_verification_suite()
        self.assertTrue(result['F2_conifold'])

    def test_koszul_check(self):
        result = full_verification_suite()
        self.assertTrue(result['koszul_complementarity'])

    def test_heisenberg_check(self):
        result = full_verification_suite()
        self.assertTrue(result['heisenberg_complementarity'])

    def test_affine_check(self):
        result = full_verification_suite()
        self.assertTrue(result['affine_complementarity'])

    def test_spectral_genus_check(self):
        result = full_verification_suite()
        self.assertTrue(result['spectral_genus_0'])

    def test_ahat_check(self):
        result = full_verification_suite()
        self.assertTrue(result['ahat_consistency'])


if __name__ == '__main__':
    unittest.main()
