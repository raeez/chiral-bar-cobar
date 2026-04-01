r"""Tests for bar cohomology Koszul criterion and generating function analysis.

Tests the three-pronged approach:
1. FALSIFICATION: P(t)*P(-t) = 1 is FALSE for bar cohomology series
2. ALGEBRAIC GF: Degree-2 equations with shared discriminant (1-3x)(1+x)
3. HOLONOMIC RECURRENCE: Proved recurrences extend to arbitrary bar degree

50+ tests covering:
- Known values verification against ground truth
- Recurrence verification for all rank-1 families
- Algebraic equation verification
- Cross-family discriminant consistency
- Near-rationality analysis (Virasoro spurious fit)
- Asymptotic growth analysis
- Per-weight Koszul criterion
- Rank-2 conjectured extensions (sl3, W3)
"""

import math
import unittest


class TestKnownValues(unittest.TestCase):
    """Verify known bar cohomology dimensions against ground truth."""

    def test_virasoro_known_values(self):
        """Virasoro: h_n = M(n+1) - M(n), verified through n=10."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(10)
        expected = [1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610]
        self.assertEqual(h, expected)

    def test_sl2_known_values(self):
        """sl2: h_n = R(n+3), verified through n=8."""
        from compute.lib.bar_cohomology_koszul_criterion import sl2_bar_dims
        h = sl2_bar_dims(8)
        expected = [3, 6, 15, 36, 91, 232, 603, 1585]
        self.assertEqual(h, expected)

    def test_betagamma_known_values(self):
        """betagamma: sqrt((1+x)/(1-3x)) coefficients, verified through n=8."""
        from compute.lib.bar_cohomology_koszul_criterion import betagamma_bar_dims
        h = betagamma_bar_dims(8)
        expected = [2, 4, 10, 26, 70, 192, 534, 1500]
        self.assertEqual(h, expected)

    def test_sl3_known_values(self):
        """sl3: verified through n=3 (direct computation)."""
        from compute.lib.bar_cohomology_koszul_criterion import sl3_bar_dims
        h = sl3_bar_dims(3)
        expected = [8, 36, 204]
        self.assertEqual(h, expected)

    def test_w3_known_values(self):
        """W3: verified through n=5."""
        from compute.lib.bar_cohomology_koszul_criterion import w3_bar_dims
        h = w3_bar_dims(5)
        expected = [2, 5, 16, 52, 171]
        self.assertEqual(h, expected)

    def test_heisenberg_known_values(self):
        """Heisenberg: h_1=1, h_n=p(n-2) for n >= 2."""
        from compute.lib.bar_cohomology_koszul_criterion import heisenberg_bar_dims
        h = heisenberg_bar_dims(7)
        expected = [1, 1, 1, 2, 3, 5, 7]
        self.assertEqual(h, expected)

    def test_motzkin_numbers(self):
        """Motzkin numbers M(0)..M(10) against OEIS A001006."""
        from compute.lib.bar_cohomology_koszul_criterion import motzkin_numbers
        M = motzkin_numbers(11)
        expected = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188]
        self.assertEqual(M, expected)

    def test_riordan_numbers(self):
        """Riordan numbers R(0)..R(10) against OEIS A005043."""
        from compute.lib.bar_cohomology_koszul_criterion import riordan_numbers
        R = riordan_numbers(11)
        expected = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603]
        self.assertEqual(R, expected)

    def test_virasoro_is_motzkin_diff(self):
        """h_n(Vir) = M(n+1) - M(n) verified through n=15."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, motzkin_numbers,
        )
        h = virasoro_bar_dims(15)
        M = motzkin_numbers(17)
        for n in range(1, 16):
            self.assertEqual(h[n - 1], M[n + 1] - M[n],
                             f"h_{n} = {h[n-1]} != M({n+1})-M({n}) = {M[n+1]-M[n]}")

    def test_sl2_is_shifted_riordan(self):
        """h_n(sl2) = R(n+3) verified through n=12."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            sl2_bar_dims, riordan_numbers,
        )
        h = sl2_bar_dims(12)
        R = riordan_numbers(16)
        for n in range(1, 13):
            self.assertEqual(h[n - 1], R[n + 3],
                             f"h_{n} = {h[n-1]} != R({n+3}) = {R[n+3]}")


class TestFalsification(unittest.TestCase):
    """PROVE that P(t)*P(-t) = 1 is FALSE."""

    def test_virasoro_self_product_not_one(self):
        """P_Vir(t)*P_Vir(-t) != 1: first failure at t^2."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            falsify_self_product_criterion,
        )
        result = falsify_self_product_criterion()
        self.assertFalse(result['virasoro']['is_identity'])
        self.assertEqual(result['virasoro']['first_nonzero_above_0'], 2)

    def test_sl2_self_product_not_one(self):
        """P_sl2(t)*P_sl2(-t) != 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            falsify_self_product_criterion,
        )
        result = falsify_self_product_criterion()
        self.assertFalse(result['sl2']['is_identity'])

    def test_betagamma_self_product_not_one(self):
        """P_bg(t)*P_bg(-t) != 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            falsify_self_product_criterion,
        )
        result = falsify_self_product_criterion()
        self.assertFalse(result['betagamma']['is_identity'])

    def test_all_families_fail(self):
        """All three rank-1 families fail P(t)*P(-t)=1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            falsify_self_product_criterion,
        )
        result = falsify_self_product_criterion()
        self.assertTrue(result['all_false'])

    def test_self_product_odd_coefficients_vanish(self):
        """Odd-degree coefficients of P(t)*P(-t) always vanish (by symmetry)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            compute_self_product, virasoro_bar_dims,
        )
        h = [1] + virasoro_bar_dims(10)
        prod = compute_self_product(h)
        for i in range(1, len(prod), 2):
            self.assertEqual(prod[i], 0,
                             f"Odd coefficient t^{i} = {prod[i]} should be 0")

    def test_self_product_even_coefficients_nonzero(self):
        """Even-degree coefficients of P(t)*P(-t) are generically nonzero."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            compute_self_product, virasoro_bar_dims,
        )
        h = [1] + virasoro_bar_dims(10)
        prod = compute_self_product(h)
        # t^2 coefficient should be nonzero
        self.assertNotEqual(prod[2], 0)
        # t^4 coefficient should be nonzero
        self.assertNotEqual(prod[4], 0)

    def test_virasoro_self_product_t2_coefficient(self):
        """P(t)*P(-t) at t^2 = h_0^2*(h_0-2h_1) + ... = 1-2+4 = 3."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            compute_self_product, virasoro_bar_dims,
        )
        h = [1] + virasoro_bar_dims(10)
        prod = compute_self_product(h)
        # t^2 coefficient: h_0*(-h_2) + h_1*h_1 + h_2*h_0*(-1)^0...
        # Let's just check it's 3 (computed earlier)
        # Actually: sum_{i+j=2} h_i * (-1)^j * h_j
        # = h_0*(-1)^2*h_2 + h_1*(-1)^1*h_1 + h_2*(-1)^0*h_0
        # = h_2 - h_1^2 + h_2 = 2*h_2 - h_1^2 = 2*2 - 1 = 3
        self.assertEqual(prod[2], 3)


class TestClassicalKoszulHilbert(unittest.TestCase):
    """Verify the CORRECT Koszul-Hilbert relation H_A(t)*H_{A!}(-t)=1."""

    def test_dim_1(self):
        """Polynomial ring in 1 variable: 1/(1-t) * (1-t) = 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_classical_koszul_hilbert,
        )
        result = verify_classical_koszul_hilbert(1, 10)
        self.assertTrue(result['verified'])

    def test_dim_3_sl2(self):
        """Sym(sl2): 1/(1-t)^3 * (1-t)^3 = 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_classical_koszul_hilbert,
        )
        result = verify_classical_koszul_hilbert(3, 10)
        self.assertTrue(result['verified'])

    def test_dim_8_sl3(self):
        """Sym(sl3): 1/(1-t)^8 * (1-t)^8 = 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_classical_koszul_hilbert,
        )
        result = verify_classical_koszul_hilbert(8, 10)
        self.assertTrue(result['verified'])

    def test_dim_14_g2(self):
        """Sym(G2): 1/(1-t)^14 * (1-t)^14 = 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_classical_koszul_hilbert,
        )
        result = verify_classical_koszul_hilbert(14, 8)
        self.assertTrue(result['verified'])

    def test_lie_algebra_koszul(self):
        """Classical sl2 Koszul relation."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_lie_algebra_koszul,
        )
        result = verify_lie_algebra_koszul(3, 10)
        self.assertTrue(result['verified'])

    def test_per_weight_sl2(self):
        """Per-weight Koszul criterion for classical sl2."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            bigraded_koszul_criterion_sl2,
        )
        result = bigraded_koszul_criterion_sl2(10)
        self.assertTrue(result['all_verified'])


class TestRecurrenceVerification(unittest.TestCase):
    """Verify holonomic recurrences for all families."""

    def test_virasoro_recurrence(self):
        """(n+3)h(n) = (3n+4)h(n-1) + (n+1)h(n-2) - 3(n-2)h(n-3)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro(20)
        self.assertTrue(result['recurrence_verified'])

    def test_sl2_recurrence(self):
        """(n+4)h(n) = (n+2)(2h(n-1) + 3h(n-2))."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_sl2,
        )
        result = verify_algebraic_equation_sl2(20)
        self.assertTrue(result['recurrence_verified'])

    def test_betagamma_recurrence(self):
        """n*h(n) = 2n*h(n-1) + 3(n-2)*h(n-2)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_betagamma,
        )
        result = verify_algebraic_equation_betagamma(20)
        self.assertTrue(result['recurrence_verified'])

    def test_virasoro_algebraic_eq(self):
        """Algebraic equation x^4 B^2 + ... = 0 verified."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro(12)
        self.assertTrue(result['algebraic_eq_vanishes'])

    def test_virasoro_degree_2(self):
        """Virasoro GF is algebraic of degree 2."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro()
        self.assertEqual(result['algebraic_degree'], 2)

    def test_sl2_degree_2(self):
        """sl2 GF is algebraic of degree 2."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_sl2,
        )
        result = verify_algebraic_equation_sl2()
        self.assertEqual(result['algebraic_degree'], 2)

    def test_virasoro_discriminant(self):
        """Virasoro discriminant is (1-3x)(1+x)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro()
        self.assertEqual(result['discriminant'], '(1 - 3x)(1 + x)')


class TestExtension(unittest.TestCase):
    """Test extension of bar cohomology to high bar degree."""

    def test_virasoro_extension_20(self):
        """Extend Virasoro to n=20, verify monotone increasing."""
        from compute.lib.bar_cohomology_koszul_criterion import extend_virasoro
        h = extend_virasoro(20)
        self.assertEqual(len(h), 20)
        for i in range(1, len(h)):
            self.assertGreater(h[i], h[i - 1])

    def test_sl2_extension_20(self):
        """Extend sl2 to n=20, verify monotone increasing."""
        from compute.lib.bar_cohomology_koszul_criterion import extend_sl2
        h = extend_sl2(20)
        self.assertEqual(len(h), 20)
        for i in range(1, len(h)):
            self.assertGreater(h[i], h[i - 1])

    def test_betagamma_extension_20(self):
        """Extend betagamma to n=20, verify monotone increasing."""
        from compute.lib.bar_cohomology_koszul_criterion import extend_betagamma
        h = extend_betagamma(20)
        self.assertEqual(len(h), 20)
        for i in range(1, len(h)):
            self.assertGreater(h[i], h[i - 1])

    def test_virasoro_h7_to_h9(self):
        """Virasoro: h_7=196, h_8=512, h_9=1353 (from PROVED recurrence)."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(9)
        self.assertEqual(h[6], 196)
        self.assertEqual(h[7], 512)
        self.assertEqual(h[8], 1353)

    def test_virasoro_h10_to_h15(self):
        """Virasoro: verified extension to h_15."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(15)
        expected = [1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610,
                    9713, 26324, 71799, 196938, 542895]
        self.assertEqual(h, expected)

    def test_sl3_extension_positive(self):
        """sl3 conjectured extension gives positive integers."""
        from compute.lib.bar_cohomology_koszul_criterion import extend_sl3
        h = extend_sl3(10)
        for i, v in enumerate(h):
            self.assertGreater(v, 0, f"h_{i+1} = {v} should be positive")
            self.assertEqual(v, int(v), f"h_{i+1} should be an integer")

    def test_w3_extension_positive(self):
        """W3 conjectured extension gives positive integers."""
        from compute.lib.bar_cohomology_koszul_criterion import extend_w3
        h = extend_w3(10)
        for i, v in enumerate(h):
            self.assertGreater(v, 0, f"h_{i+1} = {v} should be positive")
            self.assertEqual(v, int(v), f"h_{i+1} should be an integer")

    def test_w3_h6(self):
        """W3: h_6 = 564 (conjectured from rational GF)."""
        from compute.lib.bar_cohomology_koszul_criterion import w3_bar_dims
        h = w3_bar_dims(6)
        # 4*171 - 2*52 - 16 = 684 - 104 - 16 = 564
        self.assertEqual(h[5], 564)

    def test_w3_h7(self):
        """W3: h_7 = 1862 (conjectured from rational GF recurrence)."""
        from compute.lib.bar_cohomology_koszul_criterion import w3_bar_dims
        h = w3_bar_dims(7)
        # 4*564 - 2*171 - 52 = 2256 - 342 - 52 = 1862
        self.assertEqual(h[6], 1862)

    def test_w3_h8(self):
        """W3: h_8 from recurrence."""
        from compute.lib.bar_cohomology_koszul_criterion import w3_bar_dims
        h = w3_bar_dims(8)
        val = 4 * h[6] - 2 * h[5] - h[4]
        self.assertEqual(h[7], val)


class TestCrossFamilyConsistency(unittest.TestCase):
    """Cross-family consistency checks."""

    def test_shared_discriminant(self):
        """All rank-1 families share discriminant (1-3x)(1+x)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            discriminant_universality_check,
        )
        result = discriminant_universality_check()
        self.assertTrue(result['all_converge'])

    def test_growth_rate_3(self):
        """All rank-1 families converge to growth rate 3."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            cross_family_growth_analysis,
        )
        result = cross_family_growth_analysis(20)
        for name in ['sl2', 'virasoro', 'betagamma']:
            ratios = result[name]['ratios']
            self.assertAlmostEqual(ratios[-1], 3.0, delta=0.5,
                                   msg=f"{name} growth rate not approaching 3")

    def test_shared_discriminant_structure(self):
        """Discriminant analysis returns correct structure."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            shared_discriminant_coefficients,
        )
        result = shared_discriminant_coefficients()
        from sympy import Rational
        self.assertEqual(result['radius_of_convergence'], Rational(1, 3))
        self.assertEqual(result['growth_rate'], 3)

    def test_virasoro_sl2_ratio_ordering(self):
        """sl2 bar dims are always larger than Virasoro bar dims."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, sl2_bar_dims,
        )
        h_vir = virasoro_bar_dims(15)
        h_sl2 = sl2_bar_dims(15)
        for n in range(15):
            self.assertGreater(h_sl2[n], h_vir[n],
                               f"sl2 h_{n+1} should exceed Virasoro h_{n+1}")

    def test_consistency_with_bar_gf_solver(self):
        """Check consistency with existing bar_gf_solver module."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, sl2_bar_dims,
        )
        from compute.lib.bar_gf_solver import (
            bar_dims_virasoro, bar_dims_sl2,
        )
        for n in range(1, 13):
            self.assertEqual(virasoro_bar_dims(n), bar_dims_virasoro(n))
            self.assertEqual(sl2_bar_dims(n), bar_dims_sl2(n))

    def test_consistency_with_bar_gf_algebraicity(self):
        """Check consistency with existing bar_gf_algebraicity module."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims as vir_kc,
            sl2_bar_dims as sl2_kc,
            w3_bar_dims as w3_kc,
            sl3_bar_dims as sl3_kc,
        )
        from compute.lib.bar_gf_algebraicity import (
            virasoro_bar_dims as vir_gfa,
            sl2_bar_dims as sl2_gfa,
            w3_bar_dims as w3_gfa,
            sl3_bar_dims as sl3_gfa,
        )
        for n in [5, 10, 15]:
            self.assertEqual(vir_kc(n), vir_gfa(n), f"Virasoro mismatch at n={n}")
            self.assertEqual(sl2_kc(n), sl2_gfa(n), f"sl2 mismatch at n={n}")
        for n in [5, 8]:
            self.assertEqual(w3_kc(n), w3_gfa(n), f"W3 mismatch at n={n}")
            self.assertEqual(sl3_kc(n), sl3_gfa(n), f"sl3 mismatch at n={n}")


class TestNearRationality(unittest.TestCase):
    """Test near-rationality of Virasoro GF."""

    def test_spurious_rational_fit_works_through_8(self):
        """Spurious rational recurrence works through n=8."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_near_rationality,
        )
        result = virasoro_near_rationality(12)
        errors = result['errors']
        for e in errors:
            if e['n'] <= 8:
                self.assertEqual(e['error'], 0,
                                 f"Spurious recurrence should match at n={e['n']}")

    def test_spurious_rational_fit_fails_at_9(self):
        """Spurious rational recurrence fails at n=9 by exactly 1."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_near_rationality,
        )
        result = virasoro_near_rationality(12)
        first_fail = result['first_failure']
        self.assertIsNotNone(first_fail)
        self.assertEqual(first_fail['n'], 9)
        # The error is predicted=1352, actual=1353, error=-1
        self.assertEqual(abs(first_fail['error']), 1)

    def test_true_recurrence_always_works(self):
        """True holonomic recurrence works at all degrees (contrast with spurious)."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(25)
        for n in range(4, 26):
            lhs = (n + 3) * h[n - 1]
            rhs = (3 * n + 4) * h[n - 2] + (n + 1) * h[n - 3] - 3 * (n - 2) * h[n - 4]
            self.assertEqual(lhs, rhs,
                             f"Holonomic recurrence fails at n={n}")


class TestAsymptotics(unittest.TestCase):
    """Asymptotic growth analysis."""

    def test_virasoro_growth_rate(self):
        """Virasoro growth rate converges to 3."""
        from compute.lib.bar_cohomology_koszul_criterion import asymptotic_analysis
        result = asymptotic_analysis('virasoro', 30)
        self.assertEqual(result['growth_rate'], 3)

    def test_sl2_growth_rate(self):
        """sl2 growth rate converges to 3."""
        from compute.lib.bar_cohomology_koszul_criterion import asymptotic_analysis
        result = asymptotic_analysis('sl2', 30)
        self.assertEqual(result['growth_rate'], 3)

    def test_virasoro_alpha(self):
        """Virasoro subleading exponent alpha ~ 3/2."""
        from compute.lib.bar_cohomology_koszul_criterion import asymptotic_analysis
        result = asymptotic_analysis('virasoro', 50)
        if result.get('alpha_final'):
            self.assertAlmostEqual(result['alpha_final'], 1.5, delta=0.2,
                                   msg="Virasoro alpha should be ~3/2")

    def test_betagamma_alpha(self):
        """betagamma subleading exponent alpha ~ 1/2."""
        from compute.lib.bar_cohomology_koszul_criterion import asymptotic_analysis
        result = asymptotic_analysis('betagamma', 50)
        if result.get('alpha_final'):
            self.assertAlmostEqual(result['alpha_final'], 0.5, delta=0.2,
                                   msg="betagamma alpha should be ~1/2")


class TestW3Extension(unittest.TestCase):
    """W3 Koszul duality extension tests."""

    def test_w3_recurrence_against_known(self):
        """W3 recurrence h(n) = 4h(n-1) - 2h(n-2) - h(n-3) matches known values."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            w3_koszul_duality_extension,
        )
        result = w3_koszul_duality_extension(10)
        for check in result['recurrence_checks']:
            self.assertTrue(check['match'],
                            f"W3 recurrence fails at n={check['n']}")

    def test_w3_growth_rate(self):
        """W3 growth rate ~ 3.303 (golden-ratio related)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            w3_koszul_duality_extension,
        )
        result = w3_koszul_duality_extension(10)
        self.assertAlmostEqual(result['growth_rate'], 3.302776, delta=0.01)

    def test_w3_extended_monotone(self):
        """W3 extended sequence is monotone increasing."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            w3_koszul_duality_extension,
        )
        result = w3_koszul_duality_extension(15)
        h = result['extended']
        for i in range(1, len(h)):
            self.assertGreater(h[i], h[i - 1])


class TestPredictAllFamilies(unittest.TestCase):
    """Comprehensive prediction tests."""

    def test_all_families_present(self):
        """All 6 standard families are predicted."""
        from compute.lib.bar_cohomology_koszul_criterion import predict_all_families
        result = predict_all_families(10)
        expected_families = ['virasoro', 'sl2', 'betagamma', 'sl3', 'w3', 'heisenberg']
        for name in expected_families:
            self.assertIn(name, result, f"Missing family: {name}")

    def test_all_proved_families_have_proved_status(self):
        """Rank-1 families have PROVED status."""
        from compute.lib.bar_cohomology_koszul_criterion import predict_all_families
        result = predict_all_families(10)
        for name in ['virasoro', 'sl2', 'betagamma', 'heisenberg']:
            self.assertIn('PROVED', result[name]['status'],
                          f"{name} should have PROVED status")

    def test_conjectured_families_flagged(self):
        """Rank-2 families have CONJECTURED status."""
        from compute.lib.bar_cohomology_koszul_criterion import predict_all_families
        result = predict_all_families(10)
        for name in ['sl3', 'w3']:
            self.assertIn('CONJECTURED', result[name]['status'],
                          f"{name} should have CONJECTURED status")

    def test_predictions_are_positive_integers(self):
        """All predicted dimensions are positive integers."""
        from compute.lib.bar_cohomology_koszul_criterion import predict_all_families
        result = predict_all_families(15)
        for name, data in result.items():
            for n, v in enumerate(data['dims']):
                self.assertGreater(v, 0, f"{name} h_{n+1} = {v} not positive")
                self.assertEqual(v, int(v), f"{name} h_{n+1} = {v} not integer")


class TestBigraded(unittest.TestCase):
    """Bigraded Koszul criterion tests."""

    def test_bigraded_virasoro(self):
        """Bigraded criterion for Virasoro PBW-graded."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            bigraded_koszul_criterion_virasoro,
        )
        result = bigraded_koszul_criterion_virasoro(12)
        self.assertIn('bigraded_criterion', result)

    def test_partitions_geq2(self):
        """Partitions into parts >= 2: p_{>=2}(0..8) = 1,0,1,1,2,2,4,4,7."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            bigraded_koszul_criterion_virasoro,
        )
        result = bigraded_koszul_criterion_virasoro(8)
        p = result['dimensions_p_geq2']
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7]
        self.assertEqual(p, expected)


class TestMasterSummary(unittest.TestCase):
    """Master summary integration test."""

    def test_master_summary_runs(self):
        """Master summary completes without error."""
        from compute.lib.bar_cohomology_koszul_criterion import master_summary
        result = master_summary(10)
        self.assertIn('falsification', result)
        self.assertIn('virasoro_algebraic', result)
        self.assertIn('sl2_algebraic', result)
        self.assertIn('discriminant', result)

    def test_falsification_in_summary(self):
        """Falsification result present and correct in summary."""
        from compute.lib.bar_cohomology_koszul_criterion import master_summary
        result = master_summary(10)
        self.assertTrue(result['falsification']['all_false'])


class TestAdversarial(unittest.TestCase):
    """Adversarial tests: edge cases, potential confusions, AP violations."""

    def test_h0_convention(self):
        """h_0 is NOT included in bar_dims (starts at h_1)."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(3)
        # h_1 = 1 (not h_0)
        self.assertEqual(h[0], 1)
        self.assertEqual(len(h), 3)

    def test_sl2_h2_is_5_not_6(self):
        """sl2: h_2 = 6 (from R(5) = 6). Not 5 (CLAUDE.md says 5 was wrong)."""
        from compute.lib.bar_cohomology_koszul_criterion import sl2_bar_dims
        h = sl2_bar_dims(2)
        self.assertEqual(h[1], 6)

    def test_no_negative_dims(self):
        """No family produces negative dimensions at any degree."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, sl2_bar_dims, betagamma_bar_dims,
            sl3_bar_dims, w3_bar_dims, heisenberg_bar_dims,
        )
        for name, func in [
            ('virasoro', virasoro_bar_dims),
            ('sl2', sl2_bar_dims),
            ('betagamma', betagamma_bar_dims),
            ('sl3', sl3_bar_dims),
            ('w3', w3_bar_dims),
            ('heisenberg', heisenberg_bar_dims),
        ]:
            h = func(20)
            for n, v in enumerate(h):
                self.assertGreaterEqual(v, 0,
                                        f"{name} h_{n+1} = {v} is negative")

    def test_virasoro_not_self_dual_in_bar_series(self):
        """Even though Vir_c! = Vir_{26-c}, P(t)*P(-t) != 1.

        This tests AP9: same name ('self-dual'), different object.
        Koszul self-duality means the ALGEBRA is self-dual (at c=13),
        NOT that the bar cohomology series satisfies P*P(-) = 1.
        """
        from compute.lib.bar_cohomology_koszul_criterion import (
            compute_self_product, virasoro_bar_dims,
        )
        h = [1] + virasoro_bar_dims(8)
        prod = compute_self_product(h)
        self.assertEqual(prod[0], 1)  # constant term always 1
        self.assertNotEqual(prod[2], 0)  # but t^2 is nonzero

    def test_different_recurrence_types(self):
        """Virasoro has holonomic (n-dependent) recurrence, W3 has constant-coefficient.

        This is the key structural difference: algebraic vs rational GF.
        """
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, w3_bar_dims,
        )
        # Virasoro: holonomic (polynomial-in-n coefficients)
        h_vir = virasoro_bar_dims(15)
        # Test that constant-coefficient recurrence FAILS for Virasoro beyond n=8
        vir_cc_error = (4 * h_vir[7] - 2 * h_vir[6] - 4 * h_vir[5]) - h_vir[8]
        self.assertNotEqual(vir_cc_error, 0,
                            "Virasoro should NOT satisfy a constant-coefficient recurrence")

        # W3: constant-coefficient (rational GF)
        h_w3 = w3_bar_dims(10)
        for n in range(4, 11):
            cc_val = 4 * h_w3[n - 2] - 2 * h_w3[n - 3] - h_w3[n - 4]
            self.assertEqual(cc_val, h_w3[n - 1],
                             f"W3 constant-coefficient recurrence fails at n={n}")


class TestMotzkinConvolution(unittest.TestCase):
    """Test the B(x) = x*M(x)^2 identity for Virasoro."""

    def test_b_equals_x_m_squared_through_20(self):
        """h_n = sum_{k=0}^{n-1} M(k)*M(n-1-k) verified through n=20."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, motzkin_numbers,
        )
        h = virasoro_bar_dims(20)
        M = motzkin_numbers(21)
        for n in range(1, 21):
            conv = sum(M[k] * M[n - 1 - k] for k in range(n))
            self.assertEqual(h[n - 1], conv,
                             f"B=xM^2 fails at n={n}: h_n={h[n-1]}, conv={conv}")

    def test_motzkin_convolution_formula(self):
        """The convolution M*M gives the Motzkin difference sequence."""
        from compute.lib.bar_cohomology_koszul_criterion import motzkin_numbers
        M = motzkin_numbers(15)
        # h_n = M(n+1) - M(n) = sum_{k=0}^{n-1} M(k)M(n-1-k)
        for n in range(1, 14):
            diff = M[n + 1] - M[n]
            conv = sum(M[k] * M[n - 1 - k] for k in range(n))
            self.assertEqual(diff, conv,
                             f"At n={n}: M({n+1})-M({n})={diff}, conv={conv}")

    def test_b_x_m_squared_implies_algebraic_degree_2(self):
        """B(x) = xM(x)^2 and M algebraic of degree 2 implies B algebraic of degree 2."""
        # If M satisfies c2*M^2 + c1*M + c0 = 0, then M^2 = -(c1*M+c0)/c2.
        # B = xM^2 = -x(c1*M+c0)/c2.
        # M = (B/x - c0*x/c2*...) -- this gives a degree-2 relation for B.
        # We just verify the known algebraic equation.
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro(15)
        self.assertEqual(result['algebraic_degree'], 2)


class TestAlgebraicEquation(unittest.TestCase):
    """Verify the algebraic equation x^3 B^2 + (x^2+2x-1)B + x = 0."""

    def test_virasoro_algebraic_equation_degree_12(self):
        """Algebraic equation vanishes through degree 12."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro(12)
        self.assertTrue(result['algebraic_eq_vanishes'])

    def test_virasoro_algebraic_equation_degree_20(self):
        """Algebraic equation vanishes through degree 20."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            verify_algebraic_equation_virasoro,
        )
        result = verify_algebraic_equation_virasoro(20)
        self.assertTrue(result['algebraic_eq_vanishes'])

    def test_virasoro_discriminant_factorization(self):
        """Discriminant of x^3 B^2 + (x^2+2x-1)B + x = 0 contains (1-3x)(1+x)."""
        from sympy import Symbol, factor, expand
        x = Symbol('x')
        # disc = (x^2+2x-1)^2 - 4*x^3*x = (x^2+2x-1)^2 - 4x^4
        disc = expand((x ** 2 + 2 * x - 1) ** 2 - 4 * x ** 4)
        disc_f = factor(disc)
        # Should factor as -(x-1)^2 * (x+1) * (3x-1)
        # which contains the standard discriminant factors (1+x) and (1-3x)
        self.assertIn('3*x - 1', str(disc_f))
        self.assertIn('x + 1', str(disc_f))


class TestLargeExtension(unittest.TestCase):
    """Test extensions to very high bar degree."""

    def test_virasoro_to_30(self):
        """Virasoro extends to n=30 with correct recurrence."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(30)
        self.assertEqual(len(h), 30)
        # Verify recurrence at n=30
        n = 30
        lhs = (n + 3) * h[n - 1]
        rhs = (3 * n + 4) * h[n - 2] + (n + 1) * h[n - 3] - 3 * (n - 2) * h[n - 4]
        self.assertEqual(lhs, rhs)

    def test_sl2_to_30(self):
        """sl2 extends to n=30 with correct recurrence."""
        from compute.lib.bar_cohomology_koszul_criterion import sl2_bar_dims
        h = sl2_bar_dims(30)
        self.assertEqual(len(h), 30)
        # Verify recurrence at n=30
        n = 30
        lhs = (n + 4) * h[n - 1]
        rhs = (n + 2) * (2 * h[n - 2] + 3 * h[n - 3])
        self.assertEqual(lhs, rhs)

    def test_betagamma_to_30(self):
        """betagamma extends to n=30 with correct recurrence."""
        from compute.lib.bar_cohomology_koszul_criterion import betagamma_bar_dims
        h = betagamma_bar_dims(30)
        self.assertEqual(len(h), 30)
        # Verify recurrence at n=30
        n = 30
        lhs = n * h[n - 1]
        rhs = 2 * n * h[n - 2] + 3 * (n - 2) * h[n - 3]
        self.assertEqual(lhs, rhs)


class TestRatioConvergence(unittest.TestCase):
    """Test that h_{n+1}/h_n converges to the correct growth rate."""

    def test_virasoro_ratio_monotone_after_initial(self):
        """Virasoro ratios are monotonically increasing after n=3."""
        from compute.lib.bar_cohomology_koszul_criterion import virasoro_bar_dims
        h = virasoro_bar_dims(25)
        ratios = [h[n] / h[n - 1] for n in range(1, 25)]
        # After initial oscillation, should be monotone increasing
        for i in range(4, len(ratios) - 1):
            self.assertGreater(ratios[i + 1], ratios[i],
                               f"Virasoro ratio not increasing at n={i+2}")

    def test_betagamma_ratio_monotone_after_initial(self):
        """betagamma ratios are monotonically increasing after n=2."""
        from compute.lib.bar_cohomology_koszul_criterion import betagamma_bar_dims
        h = betagamma_bar_dims(25)
        ratios = [h[n] / h[n - 1] for n in range(1, 25)]
        for i in range(3, len(ratios) - 1):
            self.assertGreater(ratios[i + 1], ratios[i],
                               f"betagamma ratio not increasing at n={i+2}")

    def test_all_ratios_below_3(self):
        """All rank-1 family ratios are strictly below 3 (convergence from below)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            virasoro_bar_dims, sl2_bar_dims, betagamma_bar_dims,
        )
        for name, func in [
            ('virasoro', virasoro_bar_dims),
            ('sl2', sl2_bar_dims),
            ('betagamma', betagamma_bar_dims),
        ]:
            h = func(25)
            ratios = [h[n] / h[n - 1] for n in range(1, 25)]
            for r in ratios:
                self.assertLess(r, 3.0,
                                f"{name}: ratio {r} exceeds 3")


class TestSl3Sl2Comparison(unittest.TestCase):
    """Compare rank-1 (sl2) and rank-2 (sl3) families."""

    def test_sl3_exceeds_sl2(self):
        """sl3 bar dims strictly exceed sl2 bar dims (rank-2 > rank-1)."""
        from compute.lib.bar_cohomology_koszul_criterion import (
            sl2_bar_dims, sl3_bar_dims,
        )
        h_sl2 = sl2_bar_dims(10)
        h_sl3 = sl3_bar_dims(10)
        for n in range(10):
            self.assertGreater(h_sl3[n], h_sl2[n],
                               f"sl3 h_{n+1} should exceed sl2 h_{n+1}")

    def test_sl3_growth_rate_exceeds_3(self):
        """sl3 conjectured growth rate exceeds 3 (different from rank-1 families)."""
        from compute.lib.bar_cohomology_koszul_criterion import sl3_bar_dims
        h = sl3_bar_dims(15)
        ratio = h[-1] / h[-2]
        self.assertGreater(ratio, 3.0,
                           "sl3 growth rate should exceed 3")

    def test_w3_growth_rate_exceeds_3(self):
        """W3 conjectured growth rate exceeds 3."""
        from compute.lib.bar_cohomology_koszul_criterion import w3_bar_dims
        h = w3_bar_dims(15)
        ratio = h[-1] / h[-2]
        self.assertGreater(ratio, 3.0,
                           "W3 growth rate should exceed 3")

    def test_w3_growth_rate_near_golden(self):
        """W3 growth rate approaches (3+sqrt(13))/2 ~ 3.303."""
        from compute.lib.bar_cohomology_koszul_criterion import w3_bar_dims
        h = w3_bar_dims(20)
        ratio = h[-1] / h[-2]
        golden_w3 = (3 + math.sqrt(13)) / 2
        self.assertAlmostEqual(ratio, golden_w3, delta=0.1,
                               msg="W3 growth rate should approach (3+sqrt(13))/2")


if __name__ == '__main__':
    unittest.main()
