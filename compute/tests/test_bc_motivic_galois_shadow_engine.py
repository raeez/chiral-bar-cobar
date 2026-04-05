"""Tests for bc_motivic_galois_shadow_engine.py.

Comprehensive test suite covering:
- Arithmetic primitives (primes, divisor sums, Ramanujan tau)
- Kappa formulas (AP1/AP39)
- Shadow coefficients for all families
- Shadow motives and fiber functors
- Motivic Galois groups
- Weight decomposition
- Frobenius eigenvalues and Ramanujan test
- Motivic Euler product and shadow zeta
- Periods
- Motivic cohomology
- Mixed Tate structure
- Grothendieck ring classes
- Standard conjectures
- Tannakian structure verification
- Cross-verification (AP10)
"""

import math
import unittest

from sympy import Rational, N as Neval

from compute.lib.bc_motivic_galois_shadow_engine import (
    primes_up_to,
    first_n_primes,
    divisor_sum,
    ramanujan_tau,
    virasoro_kappa,
    heisenberg_kappa,
    affine_sl2_kappa,
    virasoro_shadow_coefficients,
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    ShadowMotive,
    fiber_functor_dimension,
    build_shadow_motive,
    heisenberg_motive,
    virasoro_motive,
    sl2_motive,
    MotivicGaloisGroup,
    motivic_galois_group,
    weight_decomposition,
    weight_decomposition_comparison,
    shadow_frobenius_eigenvalue,
    local_euler_factor,
    motivic_euler_product,
    shadow_zeta_from_coefficients,
    compare_euler_product_and_shadow_zeta,
    shadow_periods,
    frobenius_data_at_prime,
    frobenius_landscape,
    ramanujan_test_landscape,
    motivic_cohomology,
    motivic_cohomology_table,
    is_mixed_tate,
    GrothendieckClass,
    motivic_measure_shadow_curve,
    motivic_measure_bar_complex,
    test_conjecture_B as check_conjecture_B,
    test_conjecture_C as check_conjecture_C,
    test_conjecture_D as check_conjecture_D,
    test_all_standard_conjectures as check_all_standard_conjectures,
    shadow_motivic_landscape,
    verify_fiber_functor_additivity,
    verify_weight_filtration_compatibility,
    verify_galois_weight_purity,
    verify_tannakian_structure,
    complete_motivic_analysis,
)


class TestPrimes(unittest.TestCase):
    """Test prime-related arithmetic primitives."""

    def test_primes_up_to_10(self):
        self.assertEqual(primes_up_to(10), [2, 3, 5, 7])

    def test_primes_up_to_1(self):
        self.assertEqual(primes_up_to(1), [])

    def test_first_5_primes(self):
        self.assertEqual(first_n_primes(5), [2, 3, 5, 7, 11])

    def test_first_0_primes(self):
        self.assertEqual(first_n_primes(0), [])

    def test_prime_count(self):
        """pi(100) = 25."""
        self.assertEqual(len(primes_up_to(100)), 25)


class TestDivisorSum(unittest.TestCase):
    """Test divisor sum sigma_k(n)."""

    def test_sigma0(self):
        """sigma_0(n) = number of divisors."""
        self.assertEqual(divisor_sum(6, 0), 4)  # 1,2,3,6
        self.assertEqual(divisor_sum(12, 0), 6)

    def test_sigma1(self):
        """sigma_1(n) = sum of divisors."""
        self.assertEqual(divisor_sum(6, 1), 12)  # 1+2+3+6
        self.assertEqual(divisor_sum(1, 1), 1)

    def test_sigma_zero_input(self):
        self.assertEqual(divisor_sum(0, 1), 0)

    def test_sigma_prime(self):
        """sigma_1(p) = p+1 for prime p."""
        self.assertEqual(divisor_sum(7, 1), 8)
        self.assertEqual(divisor_sum(11, 1), 12)


class TestRamanujanTau(unittest.TestCase):
    """Test Ramanujan tau function."""

    def test_tau_1(self):
        self.assertEqual(ramanujan_tau(1), 1)

    def test_tau_2(self):
        self.assertEqual(ramanujan_tau(2), -24)

    def test_tau_3(self):
        self.assertEqual(ramanujan_tau(3), 252)

    def test_tau_4(self):
        self.assertEqual(ramanujan_tau(4), -1472)

    def test_tau_0(self):
        self.assertEqual(ramanujan_tau(0), 0)

    def test_tau_negative(self):
        self.assertEqual(ramanujan_tau(-1), 0)


class TestKappaFormulas(unittest.TestCase):
    """Test kappa formulas (AP1/AP39)."""

    def test_virasoro(self):
        self.assertEqual(virasoro_kappa(2), Rational(1))
        self.assertEqual(virasoro_kappa(26), Rational(13))

    def test_heisenberg(self):
        self.assertEqual(heisenberg_kappa(3), Rational(3))

    def test_affine_sl2(self):
        self.assertEqual(affine_sl2_kappa(1), Rational(9, 4))

    def test_kappa_not_c(self):
        """kappa != c for Virasoro (AP39)."""
        self.assertNotEqual(virasoro_kappa(4), 4)


class TestShadowCoefficients(unittest.TestCase):
    """Test shadow coefficient computation."""

    def test_virasoro_S2(self):
        S = virasoro_shadow_coefficients(10, max_r=4)
        self.assertEqual(S[2], Rational(5))  # kappa = c/2 = 5

    def test_virasoro_S3(self):
        S = virasoro_shadow_coefficients(10, max_r=4)
        self.assertEqual(S[3], Rational(2))  # alpha = 2

    def test_virasoro_S4(self):
        S = virasoro_shadow_coefficients(10, max_r=5)
        expected = Rational(10) / (10 * (50 + 22))
        self.assertEqual(S[4], expected)

    def test_heisenberg_only_S2(self):
        S = heisenberg_shadow_coefficients(5, max_r=6)
        self.assertEqual(S[2], Rational(5))
        for r in range(3, 7):
            self.assertEqual(S[r], 0)

    def test_affine_sl2_only_S2(self):
        """sl_2 has no cubic Casimir, so S_3=0."""
        S = affine_sl2_shadow_coefficients(1, max_r=5)
        self.assertEqual(S[2], Rational(9, 4))
        self.assertEqual(S[3], 0)

    def test_virasoro_c0_raises(self):
        with self.assertRaises(ValueError):
            virasoro_shadow_coefficients(0)


class TestFiberFunctorDimension(unittest.TestCase):
    """Test fiber functor dimension."""

    def test_class_G(self):
        self.assertEqual(fiber_functor_dimension('G', 2), 1)

    def test_class_L(self):
        self.assertEqual(fiber_functor_dimension('L', 3), 2)

    def test_class_C(self):
        self.assertEqual(fiber_functor_dimension('C', 4), 3)

    def test_class_M_truncated(self):
        self.assertEqual(fiber_functor_dimension('M', float('inf'), 10), 9)


class TestMotiveConstruction(unittest.TestCase):
    """Test shadow motive construction."""

    def test_heisenberg_motive(self):
        m = heisenberg_motive(3)
        self.assertEqual(m.family, 'G')
        self.assertEqual(m.dim_fiber, 1)
        self.assertEqual(m.r_max, 2)

    def test_virasoro_motive(self):
        m = virasoro_motive(10, truncation=8)
        self.assertEqual(m.family, 'M')
        self.assertEqual(m.r_max, float('inf'))

    def test_sl2_motive(self):
        m = sl2_motive(1)
        self.assertEqual(m.family, 'L')
        self.assertEqual(m.r_max, 3)


class TestMotivicGaloisGroup(unittest.TestCase):
    """Test motivic Galois group computation."""

    def test_class_G(self):
        m = heisenberg_motive(1)
        g = motivic_galois_group(m)
        self.assertEqual(g.name, 'GL_1')
        self.assertEqual(g.dimension, 1)
        self.assertTrue(g.is_solvable)
        self.assertTrue(g.is_reductive)

    def test_class_L_sl2(self):
        m = sl2_motive(1)
        g = motivic_galois_group(m)
        # sl_2 has only S_2 nonzero (no cubic), so effectively GL_1
        self.assertEqual(g.name, 'GL_1')

    def test_class_M(self):
        m = virasoro_motive(10, truncation=6)
        g = motivic_galois_group(m)
        self.assertFalse(g.is_solvable)
        self.assertTrue(g.is_reductive)


class TestWeightDecomposition(unittest.TestCase):
    """Test weight decomposition."""

    def test_heisenberg_single_weight(self):
        m = heisenberg_motive(1)
        w = weight_decomposition(m)
        self.assertEqual(w, {2: 1})

    def test_virasoro_multiple_weights(self):
        m = virasoro_motive(10, truncation=6)
        w = weight_decomposition(m)
        self.assertIn(2, w)
        self.assertIn(3, w)
        self.assertIn(4, w)

    def test_comparison(self):
        m = virasoro_motive(10, truncation=6)
        comp = weight_decomposition_comparison(m)
        self.assertIn('weight_grading', comp)
        self.assertIn('depth_filtration', comp)


class TestFrobeniusEigenvalues(unittest.TestCase):
    """Test Frobenius eigenvalue computation."""

    def test_heisenberg_eigenvalue(self):
        m = heisenberg_motive(1)
        eigs = shadow_frobenius_eigenvalue(m, 2)
        # Weight 2: eigenvalue = 2^{2/2} = 2
        self.assertEqual(len(eigs), 1)
        self.assertAlmostEqual(eigs[0], 2.0)

    def test_virasoro_eigenvalues(self):
        m = virasoro_motive(10, truncation=5)
        eigs = shadow_frobenius_eigenvalue(m, 3)
        self.assertGreater(len(eigs), 1)

    def test_ramanujan_heisenberg(self):
        m = heisenberg_motive(1)
        fd = frobenius_data_at_prime(m, 5)
        self.assertTrue(fd.satisfies_ramanujan)

    def test_ramanujan_landscape(self):
        m = heisenberg_motive(1)
        result = ramanujan_test_landscape(m, num_primes=20)
        self.assertTrue(result['satisfies_ramanujan'])


class TestLocalEulerFactor(unittest.TestCase):
    """Test local Euler factor computation."""

    def test_heisenberg_factor(self):
        m = heisenberg_motive(1)
        L2 = local_euler_factor(m, 2, 3.0)
        # 1/(1 - 2 * 2^{-3}) = 1/(1 - 1/4) = 4/3
        self.assertAlmostEqual(L2.real, 4.0 / 3.0, places=8)

    def test_euler_product_converges(self):
        m = heisenberg_motive(1)
        L = motivic_euler_product(m, 4.0, num_primes=50)
        self.assertTrue(math.isfinite(L.real))


class TestShadowZeta(unittest.TestCase):
    """Test shadow zeta function."""

    def test_heisenberg_zeta(self):
        m = heisenberg_motive(3)
        z = shadow_zeta_from_coefficients(m, 3.0)
        # Only S_2 = 3, so z = 3 * 2^{-3} = 3/8
        self.assertAlmostEqual(z.real, 3.0 / 8.0, places=8)

    def test_virasoro_zeta_finite(self):
        m = virasoro_motive(10, truncation=6)
        z = shadow_zeta_from_coefficients(m, 3.0)
        self.assertTrue(math.isfinite(z.real))

    def test_comparison(self):
        m = heisenberg_motive(1)
        result = compare_euler_product_and_shadow_zeta(m, [3.0, 4.0], num_primes=10)
        self.assertEqual(len(result), 2)


class TestPeriods(unittest.TestCase):
    """Test period computation."""

    def test_heisenberg_rational(self):
        m = heisenberg_motive(3)
        periods = shadow_periods(m)
        self.assertGreater(len(periods), 0)
        self.assertEqual(periods[0].generators_used, ['1'])

    def test_virasoro_transcendental(self):
        m = virasoro_motive(10, truncation=6)
        periods = shadow_periods(m)
        self.assertGreater(len(periods), 0)
        # Should include pi-based periods for class M
        has_pi = any('pi' in p.generators_used for p in periods)
        self.assertTrue(has_pi)


class TestMotivicCohomology(unittest.TestCase):
    """Test motivic cohomology."""

    def test_H00_invariants(self):
        m = heisenberg_motive(1)
        mc = motivic_cohomology(m, 0, 0)
        self.assertEqual(mc.dimension, 1)

    def test_H10_no_ext_tate(self):
        m = heisenberg_motive(1)
        mc = motivic_cohomology(m, 1, 0)
        self.assertEqual(mc.dimension, 0)

    def test_cohomology_table(self):
        m = virasoro_motive(10, truncation=5)
        table = motivic_cohomology_table(m)
        self.assertEqual(len(table), 6)  # 3 * 2

    def test_H20_vanishes(self):
        m = virasoro_motive(10, truncation=5)
        mc = motivic_cohomology(m, 2, 0)
        self.assertEqual(mc.dimension, 0)


class TestMixedTate(unittest.TestCase):
    """Test mixed Tate structure classification."""

    def test_heisenberg_tate(self):
        m = heisenberg_motive(1)
        result = is_mixed_tate(m)
        self.assertTrue(result['is_mixed_tate'])

    def test_sl2_tate(self):
        m = sl2_motive(1)
        result = is_mixed_tate(m)
        self.assertTrue(result['is_mixed_tate'])

    def test_virasoro_not_tate(self):
        m = virasoro_motive(10, truncation=6)
        result = is_mixed_tate(m)
        self.assertFalse(result['is_mixed_tate'])


class TestGrothendieckClass(unittest.TestCase):
    """Test Grothendieck ring computations."""

    def test_euler_char(self):
        gc = GrothendieckClass(name='test', coefficients={0: 1, 1: 1})
        self.assertEqual(gc.euler_characteristic, 2)

    def test_degree(self):
        gc = GrothendieckClass(name='test', coefficients={0: 1, 1: 1})
        self.assertEqual(gc.degree, 1)

    def test_evaluate(self):
        gc = GrothendieckClass(name='test', coefficients={0: 1, 1: 1})
        self.assertAlmostEqual(gc.evaluate_at_L(2.0), 3.0)

    def test_shadow_curve_class(self):
        m = heisenberg_motive(1)
        gc = motivic_measure_shadow_curve(m)
        self.assertEqual(gc.euler_characteristic, 2)  # [P^1]

    def test_bar_complex_class(self):
        m = heisenberg_motive(1)
        gc = motivic_measure_bar_complex(m)
        self.assertEqual(gc.degree, 1)  # L^1


class TestStandardConjectures(unittest.TestCase):
    """Test Grothendieck standard conjectures."""

    def test_all_hold(self):
        m = virasoro_motive(10, truncation=5)
        results = check_all_standard_conjectures(m)
        self.assertTrue(results['B'].holds)
        self.assertTrue(results['C'].holds)
        self.assertTrue(results['D'].holds)


class TestTannakian(unittest.TestCase):
    """Test Tannakian structure verification."""

    def test_heisenberg(self):
        m = heisenberg_motive(1)
        checks = verify_tannakian_structure(m)
        self.assertTrue(checks['fiber_functor_exact'])
        self.assertTrue(checks['galois_group_affine'])
        self.assertTrue(checks['weight_filtration_functorial'])

    def test_virasoro(self):
        m = virasoro_motive(10, truncation=5)
        checks = verify_tannakian_structure(m)
        self.assertTrue(checks['fiber_functor_exact'])

    def test_weight_purity(self):
        m = heisenberg_motive(1)
        result = verify_galois_weight_purity(m, num_primes=5)
        self.assertTrue(result['all_pure'])


class TestCompletePipeline(unittest.TestCase):
    """Test the complete motivic analysis pipeline."""

    def test_heisenberg(self):
        m = heisenberg_motive(1)
        result = complete_motivic_analysis(m)
        self.assertEqual(result['motive']['family'], 'G')
        self.assertTrue(result['standard_conjectures']['B'])
        self.assertTrue(result['weight_purity'])

    def test_virasoro(self):
        m = virasoro_motive(10, truncation=5)
        result = complete_motivic_analysis(m)
        self.assertEqual(result['motive']['family'], 'M')


class TestLandscape(unittest.TestCase):
    """Test landscape-wide computations."""

    def test_motivic_landscape(self):
        result = shadow_motivic_landscape(truncation=5)
        self.assertIn('H_1', result)
        self.assertIn('Vir_2', result)
        self.assertIn('sl2_1', result)

    def test_landscape_families(self):
        result = shadow_motivic_landscape(truncation=5)
        self.assertEqual(result['H_1']['family'], 'G')
        self.assertEqual(result['Vir_2']['family'], 'M')


class TestCrossVerification(unittest.TestCase):
    """Multi-path cross-verification tests (AP10)."""

    def test_kappa_consistency(self):
        """kappa from formula equals S_2 from tower."""
        for c_val in [2, 6, 13]:
            kappa = virasoro_kappa(c_val)
            S = virasoro_shadow_coefficients(c_val, max_r=4)
            self.assertEqual(kappa, S[2], f"kappa != S_2 at c={c_val}")

    def test_fiber_dim_matches_nonzero_coeffs(self):
        """Fiber functor dimension equals number of nonzero S_r."""
        m = heisenberg_motive(1)
        w = weight_decomposition(m)
        self.assertEqual(m.dim_fiber, len(w))

    def test_galois_solvable_iff_tate(self):
        """is_mixed_tate == galois_group.is_solvable for all families."""
        for m in [heisenberg_motive(1), sl2_motive(1), virasoro_motive(10, 5)]:
            g = motivic_galois_group(m)
            tate = is_mixed_tate(m)
            self.assertEqual(tate['is_mixed_tate'], g.is_solvable)

    def test_frobenius_product_formula(self):
        """Local factor at p=2 for Heisenberg: 1/(1 - alpha * 2^{-s}).

        At s=2, alpha=2: 1/(1 - 2*2^{-2}) = 1/(1-1/2) = 2.
        """
        m = heisenberg_motive(1)
        L = local_euler_factor(m, 2, 2.0)
        self.assertAlmostEqual(L.real, 2.0, places=8)

    def test_additivity(self):
        m1 = heisenberg_motive(1)
        m2 = heisenberg_motive(2)
        self.assertTrue(verify_fiber_functor_additivity(m1, m2))


class TestAdditionalArithmetic(unittest.TestCase):
    """Additional arithmetic primitive tests."""

    def test_primes_up_to_30(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(primes_up_to(30), expected)

    def test_first_10_primes(self):
        p = first_n_primes(10)
        self.assertEqual(len(p), 10)
        self.assertEqual(p[-1], 29)

    def test_divisor_sum_k2(self):
        """sigma_2(6) = 1 + 4 + 9 + 36 = 50."""
        self.assertEqual(divisor_sum(6, 2), 50)

    def test_ramanujan_tau_5(self):
        self.assertEqual(ramanujan_tau(5), 4830)

    def test_ramanujan_multiplicative(self):
        """tau(mn) = tau(m)*tau(n) for coprime m,n."""
        self.assertEqual(ramanujan_tau(6), ramanujan_tau(2) * ramanujan_tau(3))


class TestAdditionalMotives(unittest.TestCase):
    """Additional motive construction and analysis tests."""

    def test_heisenberg_kappa_values(self):
        for k in range(1, 6):
            m = heisenberg_motive(k)
            self.assertEqual(float(Neval(m.kappa)), float(k))

    def test_virasoro_kappa_values(self):
        for c in [2, 10, 13]:
            m = virasoro_motive(c, truncation=5)
            self.assertAlmostEqual(float(Neval(m.kappa)), c / 2.0)

    def test_motive_name(self):
        m = heisenberg_motive(3)
        self.assertEqual(m.name, 'H_3')

    def test_sl2_kappa_linear(self):
        """kappa(sl_2, k) is linear in k."""
        k1 = float(Neval(sl2_motive(1).kappa))
        k2 = float(Neval(sl2_motive(2).kappa))
        k3 = float(Neval(sl2_motive(3).kappa))
        self.assertAlmostEqual(k3 - k2, k2 - k1, places=10)

    def test_grothendieck_repr(self):
        gc = GrothendieckClass(name='test', coefficients={0: 1, 1: 1})
        s = repr(gc)
        self.assertIn('L', s)

    def test_bar_complex_class_dim(self):
        """Bar complex class [A^d] = L^d."""
        m = virasoro_motive(10, truncation=5)
        gc = motivic_measure_bar_complex(m)
        self.assertEqual(gc.degree, m.dim_fiber)


class TestAdditionalGalois(unittest.TestCase):
    """Additional Galois group tests."""

    def test_class_C_not_reductive(self):
        """Class C has non-reductive Galois group."""
        S = {2: Rational(1), 3: Rational(2), 4: Rational(1, 10)}
        m = build_shadow_motive('bg', 'C', 4, S, Rational(1))
        g = motivic_galois_group(m)
        self.assertFalse(g.is_reductive)
        self.assertTrue(g.is_solvable)

    def test_frobenius_landscape_length(self):
        m = heisenberg_motive(1)
        fl = frobenius_landscape(m, primes=[2, 3, 5])
        self.assertEqual(len(fl), 3)


if __name__ == '__main__':
    unittest.main()
