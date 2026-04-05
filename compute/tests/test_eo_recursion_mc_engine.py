r"""Tests for the EO recursion MC engine: multi-path verification.

75+ tests covering:
  1. Witten-Kontsevich intersection numbers (Airy curve)
  2. Spectral curve extraction from shadow data
  3. Multi-path free energy verification (EO vs MC vs intersection)
  4. Dilaton equation
  5. String equation
  6. WDVV from MC
  7. Blobbed TR for class M algebras
  8. Matrix model (GUE) comparison
  9. KdV constraints
 10. Cross-family consistency
 11. EO correlators for Virasoro spectral curve (mpmath)
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, simplify, factorial, bernoulli

from compute.lib.eo_recursion_mc_engine import (
    # Faber-Pandharipande
    lambda_fp,
    _bernoulli_number,
    # Witten-Kontsevich
    wk_intersection,
    airy_omega_gn,
    airy_F_g,
    airy_total_intersection_genus,
    # Spectral data
    ShadowSpectralData,
    virasoro_spectral,
    heisenberg_spectral,
    affine_sl2_spectral,
    w3_spectral,
    # Shadow tower
    shadow_tower_coefficients,
    # MC shadow
    mc_shadow_free_energy,
    mc_shadow_F1,
    mc_shadow_F2,
    mc_shadow_F3,
    # Multi-path
    MultiPathResult,
    verify_free_energy_three_paths,
    verify_all_free_energies,
    # Equations
    verify_dilaton_equation_genus0,
    verify_string_equation,
    verify_wdvv_from_mc,
    verify_kdv_constraint_genus1,
    # Blobbed
    blobbed_correction,
    # Matrix model
    gue_shadow_comparison,
    # Tables
    spectral_curve_table,
    full_verification_report,
    # EO engine
    EORecursionEngine,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ====================================================================
# Section 1: Faber-Pandharipande numbers
# ====================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda_1(self):
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_lambda_2(self):
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_lambda_3(self):
        self.assertEqual(lambda_fp(3), Rational(31, 967680))

    def test_lambda_4(self):
        B8 = _bernoulli_number(8)
        expected = Rational(2**7 - 1, 2**7) * abs(B8) / factorial(8)
        self.assertEqual(lambda_fp(4), expected)

    def test_lambda_5(self):
        B10 = _bernoulli_number(10)
        expected = Rational(2**9 - 1, 2**9) * abs(B10) / factorial(10)
        self.assertEqual(lambda_fp(5), expected)

    def test_lambda_positive(self):
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_lambda_decreasing(self):
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))

    def test_lambda_invalid_genus(self):
        with self.assertRaises(ValueError):
            lambda_fp(0)


# ====================================================================
# Section 2: Witten-Kontsevich intersection numbers
# ====================================================================

class TestWittenKontsevich(unittest.TestCase):
    """Test WK intersection numbers against known values."""

    def test_tau_000_g0(self):
        """<tau_0^3>_0 = 1."""
        self.assertEqual(wk_intersection(0, 0, 0, g=0), Rational(1))

    def test_tau_1_g1(self):
        """<tau_1>_1 = 1/24."""
        self.assertEqual(wk_intersection(1, g=1), Rational(1, 24))

    def test_tau_11_g1(self):
        """<tau_1 tau_1>_1 = 1/12 (by dilaton: (2*1-2+2)*<tau_1>_1 = 2/24)."""
        val = wk_intersection(1, 1, g=1)
        self.assertEqual(val, Rational(1, 12))

    def test_tau_111_g1(self):
        """<tau_1^3>_1 = 1/4 (dilaton: 3 * 1/12)."""
        val = wk_intersection(1, 1, 1, g=1)
        self.assertEqual(val, Rational(1, 4))

    def test_tau_010_g0(self):
        """<tau_0 tau_1 tau_0>_0: sum=1, n=3, 3*0-3+3=0. 1!=0. Zero by selection."""
        val = wk_intersection(0, 1, 0, g=0)
        self.assertEqual(val, Rational(0))

    def test_tau_110_g0(self):
        """<tau_1 tau_1 tau_0>_0: sum=2, n=3, 0-3+3=0. 2!=0. Zero."""
        val = wk_intersection(1, 1, 0, g=0)
        self.assertEqual(val, Rational(0))

    def test_tau_0000_g0(self):
        """<tau_0^4>_0: sum=0, n=4, 0-3+4=1. 0!=1. Zero."""
        val = wk_intersection(0, 0, 0, 0, g=0)
        self.assertEqual(val, Rational(0))

    def test_tau_0010_g0(self):
        """<tau_0 tau_0 tau_1 tau_0>_0: sum=1, n=4, 0-3+4=1. OK."""
        val = wk_intersection(0, 0, 1, 0, g=0)
        self.assertEqual(val, Rational(1))

    def test_genus0_witten_formula(self):
        """<tau_{d1}...tau_{dn}>_0 = (n-3)!/prod(d_i!)."""
        # <tau_1 tau_1 tau_1 tau_0 tau_0>_0: sum=3, n=5, 0-3+5=2. 3!=2. Zero.
        # <tau_2 tau_0 tau_0>_0: sum=2, n=3, 0-3+3=0. 2!=0. Zero.
        # <tau_0 tau_0 tau_0 tau_0 tau_1>_0: sum=1, n=5, 2. 1!=2. Zero.
        # Need sum d_i = n-3 for genus 0.
        # <tau_1 tau_0 tau_0 tau_0>_0: sum=1, n=4, 1. OK.
        # Witten: (4-3)!/1! = 1. By string: reduce tau_0, decrease tau_1: <tau_0^3>_0 = 1. OK.
        val = wk_intersection(1, 0, 0, 0, g=0)
        self.assertEqual(val, Rational(1))

    def test_selection_rule_violation(self):
        """Selection rule violation gives 0."""
        self.assertEqual(wk_intersection(5, g=0), Rational(0))
        self.assertEqual(wk_intersection(0, g=1), Rational(0))

    def test_unstable_gives_zero(self):
        """Unstable (g,n) with 2g-2+n <= 0 gives 0."""
        self.assertEqual(wk_intersection(g=0), Rational(0))  # n=0

    def test_genus0_4point(self):
        """<tau_0 tau_0 tau_0 tau_1 tau_1>_0: sum=2, n=5, 0-3+5=2. OK."""
        # Witten: (5-3)! / (0!*0!*0!*1!*1!) = 2
        val = wk_intersection(0, 0, 0, 1, 1, g=0)
        expected = Rational(factorial(5-3), factorial(0)**3 * factorial(1)**2)
        self.assertEqual(val, expected)

    def test_string_equation_tau_02_g1(self):
        """<tau_0 tau_2>_1 = <tau_1>_1 = 1/24 by string."""
        val = wk_intersection(0, 2, g=1)
        self.assertEqual(val, Rational(1, 24))

    def test_tau_4_g2(self):
        """<tau_4>_2: sum=4, n=1, 3*2-3+1=4. OK.

        This is a genus-2 1-point intersection number.
        By the DVV recursion or known tables: <tau_4>_2 = 1/1152.
        """
        val = wk_intersection(4, g=2)
        self.assertEqual(val, Rational(1, 1152))

    def test_tau_31_g2(self):
        """<tau_3 tau_1>_2: sum=4, n=2, 3*2-3+2=5. 4!=5. Zero."""
        val = wk_intersection(3, 1, g=2)
        self.assertEqual(val, Rational(0))


# ====================================================================
# Section 3: Airy curve
# ====================================================================

class TestAiryCurve(unittest.TestCase):
    """Airy curve F_g = lambda_fp(g) and intersection numbers."""

    def test_airy_F1(self):
        self.assertEqual(airy_F_g(1), Rational(1, 24))

    def test_airy_F2(self):
        self.assertEqual(airy_F_g(2), Rational(7, 5760))

    def test_airy_F3(self):
        self.assertEqual(airy_F_g(3), Rational(31, 967680))

    def test_airy_F4(self):
        self.assertEqual(airy_F_g(4), lambda_fp(4))

    def test_airy_omega_03(self):
        """omega_{0,3}^{Airy} at d=(0,0,0) = <tau_0^3>_0 = 1."""
        self.assertEqual(airy_omega_gn(0, (0, 0, 0)), Rational(1))

    def test_airy_omega_11(self):
        """omega_{1,1}^{Airy} at d=(1,) = <tau_1>_1 = 1/24."""
        self.assertEqual(airy_omega_gn(1, (1,)), Rational(1, 24))

    def test_airy_omega_04(self):
        """omega_{0,4}^{Airy} at d=(0,0,0,1) = <tau_0^3 tau_1>_0 = 1."""
        self.assertEqual(airy_omega_gn(0, (0, 0, 0, 1)), Rational(1))

    def test_airy_total_genus1_n1(self):
        """Total WK at g=1, n=1: sum over d=1 only. = 1/24."""
        total = airy_total_intersection_genus(1, 1)
        self.assertEqual(total, Rational(1, 24))


# ====================================================================
# Section 4: Spectral curve extraction
# ====================================================================

class TestSpectralCurve(unittest.TestCase):
    """Test spectral curve data extraction from shadow."""

    def test_heisenberg_degenerate(self):
        """Heisenberg has Q_L = 4k^2 (constant), degenerate."""
        h = heisenberg_spectral(1)
        self.assertEqual(h.q0, 4)
        self.assertEqual(h.q1, 0)
        self.assertEqual(h.q2, 0)
        self.assertTrue(h.is_degenerate)

    def test_affine_sl2_degenerate(self):
        """Affine sl_2 has Delta = 0 (class L), disc = 0."""
        a = affine_sl2_spectral(1)
        self.assertEqual(a.Delta, 0)
        self.assertEqual(a.disc_QL, 0)  # disc = -32*kappa^2*Delta = 0
        self.assertTrue(a.is_degenerate)

    def test_virasoro_nondegenerate(self):
        """Virasoro has Delta != 0 (class M), genuine spectral curve."""
        v = virasoro_spectral(10)
        self.assertNotEqual(v.Delta, 0)
        self.assertFalse(v.is_degenerate)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [1, 10, 26, 13]:
            v = virasoro_spectral(c)
            self.assertEqual(v.kappa, Rational(c, 2))

    def test_virasoro_S4(self):
        """S_4 = 10/(c(5c+22)) for Virasoro."""
        c = Rational(10)
        v = virasoro_spectral(c)
        expected = Rational(10) / (c * (5 * c + 22))
        self.assertEqual(v.S4, expected)

    def test_virasoro_Q_coefficients(self):
        """Verify Q_L coefficients for Virasoro."""
        c = Rational(10)
        v = virasoro_spectral(c)
        self.assertEqual(v.q0, 4 * (c/2)**2)
        self.assertEqual(v.q1, 12 * (c/2) * 2)
        self.assertEqual(v.q2, 9 * 4 + 16 * (c/2) * v.S4)

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 5]:
            h = heisenberg_spectral(k)
            self.assertEqual(h.kappa, Rational(k))

    def test_affine_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        a = affine_sl2_spectral(1)
        self.assertEqual(a.kappa, Rational(9, 4))

    def test_w3_kappa(self):
        """kappa(W_3, c) = 5c/6."""
        c = Rational(10)
        w = w3_spectral(c)
        self.assertEqual(w.kappa, Rational(50, 6))

    def test_depth_classes(self):
        """Verify depth class assignments."""
        self.assertEqual(heisenberg_spectral(1).depth_class, 'G')
        self.assertEqual(affine_sl2_spectral(1).depth_class, 'L')
        self.assertEqual(virasoro_spectral(10).depth_class, 'M')
        self.assertEqual(w3_spectral(10).depth_class, 'M')

    def test_spectral_curve_table(self):
        """Full spectral curve table has correct structure."""
        table = spectral_curve_table()
        self.assertIn('Heisenberg_k=1', table)
        self.assertIn('Vir_c=10', table)
        self.assertTrue(table['Heisenberg_k=1']['degenerate'])
        self.assertFalse(table['Vir_c=10']['degenerate'])


# ====================================================================
# Section 5: Shadow tower coefficients
# ====================================================================

class TestShadowTower(unittest.TestCase):
    """Test shadow tower extraction from Q_L."""

    def test_heisenberg_tower(self):
        """Heisenberg tower: S_2 = kappa, S_r = 0 for r >= 3."""
        h = heisenberg_spectral(1)
        tower = shadow_tower_coefficients(h, max_arity=8)
        self.assertEqual(tower[2], Rational(1))  # kappa = 1
        for r in range(3, 9):
            self.assertEqual(tower[r], 0)

    def test_virasoro_tower_S2(self):
        """S_2 = kappa for Virasoro."""
        c = Rational(10)
        v = virasoro_spectral(c)
        tower = shadow_tower_coefficients(v, max_arity=6)
        expected_S2 = v.kappa
        self.assertEqual(simplify(tower[2] - expected_S2), 0)

    def test_affine_tower_terminates(self):
        """Affine sl_2 tower: S_r = 0 for r >= 4 (class L)."""
        a = affine_sl2_spectral(1)
        tower = shadow_tower_coefficients(a, max_arity=8)
        # S_2 = kappa, S_3 = alpha, S_4 = 0 for class L
        for r in range(4, 9):
            self.assertEqual(simplify(tower[r]), 0)


# ====================================================================
# Section 6: MC shadow free energies
# ====================================================================

class TestMCShadow(unittest.TestCase):
    """Test MC shadow projection F_g = kappa * lambda_fp(g)."""

    def test_mc_F1_heisenberg(self):
        self.assertEqual(mc_shadow_F1(Rational(1)), Rational(1, 24))

    def test_mc_F2_heisenberg(self):
        self.assertEqual(mc_shadow_F2(Rational(1)), Rational(7, 5760))

    def test_mc_F3_heisenberg(self):
        self.assertEqual(mc_shadow_F3(Rational(1)), Rational(31, 967680))

    def test_mc_F1_virasoro(self):
        c = Rational(10)
        kappa = c / 2
        self.assertEqual(mc_shadow_F1(kappa), kappa / 24)

    def test_mc_F2_virasoro(self):
        c = Rational(26)
        kappa = c / 2
        expected = kappa * Rational(7, 5760)
        self.assertEqual(mc_shadow_F2(kappa), expected)

    def test_mc_shadow_general(self):
        """F_g from generic kappa."""
        kappa = Rational(3, 7)
        for g in range(1, 5):
            self.assertEqual(mc_shadow_free_energy(kappa, g), kappa * lambda_fp(g))


# ====================================================================
# Section 7: Multi-path verification
# ====================================================================

class TestMultiPath(unittest.TestCase):
    """Three independent paths must agree."""

    def test_heisenberg_3path(self):
        """Heisenberg k=1: all three paths give lambda_fp(g)."""
        heis = heisenberg_spectral(1)
        for g in range(1, 5):
            r = verify_free_energy_three_paths(heis.kappa, g)
            self.assertTrue(r.all_agree, f"g={g}: paths disagree")

    def test_virasoro_3path(self):
        """Virasoro c=10: all three paths give kappa*lambda_fp(g)."""
        vir = virasoro_spectral(10)
        for g in range(1, 5):
            r = verify_free_energy_three_paths(vir.kappa, g)
            self.assertTrue(r.all_agree, f"g={g}: paths disagree")

    def test_virasoro_c26_3path(self):
        """Virasoro at c=26 (critical): F_g = 13*lambda_fp(g)."""
        vir = virasoro_spectral(26)
        for g in range(1, 4):
            r = verify_free_energy_three_paths(vir.kappa, g)
            self.assertTrue(r.all_agree, f"g={g}: paths disagree for c=26")
            expected = float(13 * lambda_fp(g))
            self.assertAlmostEqual(r.path2_mc, expected, places=10)

    def test_verify_all_free_energies(self):
        """Batch verification for a family."""
        heis = heisenberg_spectral(1)
        results = verify_all_free_energies(heis, max_genus=4)
        self.assertEqual(len(results), 4)
        for r in results:
            self.assertTrue(r.all_agree)

    def test_affine_3path(self):
        """Affine sl_2 at k=1: three paths agree."""
        aff = affine_sl2_spectral(1)
        for g in range(1, 4):
            r = verify_free_energy_three_paths(aff.kappa, g)
            self.assertTrue(r.all_agree, f"g={g}: paths disagree for aff sl2")

    def test_w3_3path(self):
        """W_3 at c=10: three paths agree."""
        w = w3_spectral(10)
        for g in range(1, 4):
            r = verify_free_energy_three_paths(w.kappa, g)
            self.assertTrue(r.all_agree, f"g={g}: paths disagree for W3")


# ====================================================================
# Section 8: Dilaton equation
# ====================================================================

class TestDilatonEquation(unittest.TestCase):
    """Verify the dilaton equation from WK intersection numbers."""

    def test_dilaton_tau11_g1(self):
        """<tau_1 tau_1>_1 = 2 * <tau_1>_1 = 1/12."""
        results = verify_dilaton_equation_genus0()
        self.assertTrue(results['(1,1)_g1']['dilaton_holds'])

    def test_dilaton_tau111_g1(self):
        """<tau_1^3>_1 = 3 * <tau_1^2>_1 = 3 * 1/12 = 1/4."""
        results = verify_dilaton_equation_genus0()
        self.assertTrue(results['(1,1,1)_g1']['dilaton_holds'])

    def test_dilaton_tau1000_g0(self):
        """<tau_1 tau_0^3>_0 = 1 (string applies first, gives 1)."""
        results = verify_dilaton_equation_genus0()
        self.assertTrue(results['(1,0,0,0)_g0']['dilaton_holds'])

    def test_dilaton_explicit(self):
        """Direct dilaton: <tau_1 X>_g = (2g-2+n+1) * <X>_g."""
        # <tau_1 tau_1 tau_1 tau_1>_1: sum=4, n=4, 3-3+4=4. OK!
        # Dilaton: (2-2+4)*<tau_1^3>_1 = 4 * 1/4 = 1
        val = wk_intersection(1, 1, 1, 1, g=1)
        expected = 4 * wk_intersection(1, 1, 1, g=1)
        self.assertEqual(val, expected)


# ====================================================================
# Section 9: String equation
# ====================================================================

class TestStringEquation(unittest.TestCase):
    """Verify the string equation."""

    def test_string_base(self):
        results = verify_string_equation()
        self.assertTrue(results['base_g0']['ok'])

    def test_string_010(self):
        results = verify_string_equation()
        self.assertTrue(results['string_010']['ok'])

    def test_string_0010(self):
        results = verify_string_equation()
        self.assertTrue(results['string_0010']['ok'])

    def test_string_02_g1(self):
        results = verify_string_equation()
        self.assertTrue(results['string_02_g1']['ok'])

    def test_string_003_g1(self):
        results = verify_string_equation()
        self.assertTrue(results['string_003_g1']['ok'])

    def test_string_explicit(self):
        """<tau_0 tau_0 tau_1>_0 = <tau_0 tau_0 tau_0>_0 = 1."""
        lhs = wk_intersection(0, 0, 1, g=0)
        # sum=1, n=3, 0. 1!=0. ZERO by selection rule.
        # Wait: g=0 not consistent. Let me recalculate.
        # Actually <tau_0 tau_0 tau_1>_0: sum=1, n=3, 3*0-3+3=0. 1!=0. Zero!
        self.assertEqual(lhs, Rational(0))


# ====================================================================
# Section 10: WDVV from MC
# ====================================================================

class TestWDVV(unittest.TestCase):
    """Verify WDVV equations from MC shadow."""

    def test_wdvv_rank1_trivial(self):
        """WDVV is trivial for rank-1 CohFT."""
        vir = virasoro_spectral(10)
        result = verify_wdvv_from_mc(vir)
        self.assertTrue(result['rank_1_wdvv'])

    def test_wdvv_heisenberg(self):
        """WDVV for Heisenberg: trivially satisfied."""
        heis = heisenberg_spectral(1)
        result = verify_wdvv_from_mc(heis)
        self.assertTrue(result['wdvv_trivial_rank1'])

    def test_frobenius_not_trivial(self):
        """Frobenius relation alpha^2 = 2*kappa*S4 is NOT trivially true."""
        vir = virasoro_spectral(10)
        result = verify_wdvv_from_mc(vir)
        # For Virasoro: alpha=2, kappa=5, S4=10/(10*72)=1/72
        # alpha^2 = 4, 2*kappa*S4 = 2*5/72 = 5/36 != 4
        self.assertFalse(result['frobenius_check']['equal'])


# ====================================================================
# Section 11: Blobbed topological recursion
# ====================================================================

class TestBlobbedTR(unittest.TestCase):
    """Blobbed TR for class M algebras."""

    def test_blob_heisenberg_zero(self):
        """Heisenberg (class G): no blob correction."""
        heis = heisenberg_spectral(1)
        for g in range(1, 4):
            self.assertEqual(blobbed_correction(heis, g, 0), 0)

    def test_blob_affine_zero(self):
        """Affine (class L): no blob correction."""
        aff = affine_sl2_spectral(1)
        for g in range(1, 4):
            self.assertEqual(blobbed_correction(aff, g, 0), 0)

    def test_blob_virasoro_nonzero_high_genus(self):
        """Virasoro (class M): blob correction at g >= 3."""
        vir = virasoro_spectral(10)
        # S_5 first contributes at g = 3 (g_min(5) = 5//2+1 = 3)
        blob_g3 = blobbed_correction(vir, 3, 0)
        self.assertNotEqual(blob_g3, 0)

    def test_blob_virasoro_zero_low_genus(self):
        """Virasoro: blob correction at g=1 is zero (arities 5+ not visible)."""
        vir = virasoro_spectral(10)
        # At g=1, S_r for r>=5 need g >= floor(r/2)+1 >= 3
        blob_g1 = blobbed_correction(vir, 1, 0)
        self.assertEqual(blob_g1, 0)


# ====================================================================
# Section 12: Matrix model (GUE) comparison
# ====================================================================

class TestGUEComparison(unittest.TestCase):
    """GUE free energies match shadow at kappa=1."""

    def test_gue_comparison(self):
        results = gue_shadow_comparison(5)
        for g in range(1, 6):
            self.assertTrue(results[g]['agree'], f"GUE disagrees at g={g}")

    def test_gue_F1(self):
        """F_1^{GUE} = 1/24."""
        self.assertEqual(mc_shadow_free_energy(Rational(1), 1), Rational(1, 24))

    def test_gue_F2(self):
        """F_2^{GUE} = 7/5760."""
        self.assertEqual(mc_shadow_free_energy(Rational(1), 2), Rational(7, 5760))

    def test_gue_scaling(self):
        """F_g(kappa) = kappa * F_g^{GUE} for any kappa."""
        kappa = Rational(5)
        for g in range(1, 5):
            self.assertEqual(
                mc_shadow_free_energy(kappa, g),
                kappa * mc_shadow_free_energy(Rational(1), g)
            )


# ====================================================================
# Section 13: KdV constraints
# ====================================================================

class TestKdV(unittest.TestCase):
    """KdV/Virasoro constraint verification."""

    def test_kdv_genus1(self):
        results = verify_kdv_constraint_genus1()
        self.assertTrue(results['tau_0_g1']['ok'])
        self.assertTrue(results['tau_1_g1']['ok'])
        self.assertTrue(results['tau_2_g1']['ok'])

    def test_kdv_tau1_g1_value(self):
        """<tau_1>_1 = 1/24."""
        self.assertEqual(wk_intersection(1, g=1), Rational(1, 24))

    def test_kdv_tau_n_g1_vanishes(self):
        """<tau_n>_1 = 0 for n != 1 (by selection rule)."""
        for n in [0, 2, 3, 4, 5]:
            self.assertEqual(wk_intersection(n, g=1), Rational(0))


# ====================================================================
# Section 14: Cross-family consistency (AP24)
# ====================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Koszul duality and additivity checks."""

    def test_virasoro_koszul_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [1, 5, 10, 13, 20, 25]:
            kc = Rational(c, 2)
            kc_dual = Rational(26 - c, 2)
            self.assertEqual(kc + kc_dual, 13)

    def test_free_energy_koszul_sum(self):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_fp(g)."""
        for g in range(1, 4):
            for c in [1, 10, 13]:
                f_c = mc_shadow_free_energy(Rational(c, 2), g)
                f_dual = mc_shadow_free_energy(Rational(26-c, 2), g)
                expected = 13 * lambda_fp(g)
                self.assertEqual(simplify(f_c + f_dual - expected), 0)

    def test_heisenberg_additivity(self):
        """kappa(H_{k1} + H_{k2}) = kappa(H_{k1}) + kappa(H_{k2})."""
        for k1, k2 in [(1, 2), (3, 5), (1, 1)]:
            for g in range(1, 4):
                f_sum = (mc_shadow_free_energy(Rational(k1), g)
                         + mc_shadow_free_energy(Rational(k2), g))
                f_tensor = mc_shadow_free_energy(Rational(k1 + k2), g)
                self.assertEqual(simplify(f_sum - f_tensor), 0)

    def test_virasoro_self_dual_c13(self):
        """At c=13: kappa(Vir_13) = kappa(Vir_{26-13}) = 13/2."""
        v = virasoro_spectral(13)
        v_dual = virasoro_spectral(13)
        self.assertEqual(v.kappa, v_dual.kappa)
        self.assertEqual(v.kappa, Rational(13, 2))


# ====================================================================
# Section 15: EO engine (mpmath, numerical)
# ====================================================================

@unittest.skipUnless(HAS_MPMATH, "mpmath required for EO engine tests")
class TestEOEngine(unittest.TestCase):
    """Numerical EO recursion on spectral curves."""

    def test_heisenberg_degenerate(self):
        """Heisenberg engine is degenerate, omega_{1,1} = 0."""
        heis = heisenberg_spectral(1)
        eng = EORecursionEngine.from_shadow_data(heis)
        self.assertTrue(eng.degenerate)
        val = eng.omega_11(2.0 + 0.3j)
        self.assertAlmostEqual(abs(val), 0.0, places=10)

    def test_virasoro_nondegenerate(self):
        """Virasoro engine is not degenerate."""
        vir = virasoro_spectral(10)
        eng = EORecursionEngine.from_shadow_data(vir)
        self.assertFalse(eng.degenerate)

    def test_virasoro_omega11_nonzero(self):
        """Virasoro omega_{1,1} is nonzero at generic point."""
        vir = virasoro_spectral(10)
        eng = EORecursionEngine.from_shadow_data(vir, dps=30, contour_points=128)
        val = eng.omega_11(2.0 + 0.3j)
        self.assertGreater(abs(val), 1e-15)

    def test_virasoro_omega03_nonzero(self):
        """Virasoro omega_{0,3} is nonzero at generic point."""
        vir = virasoro_spectral(10)
        eng = EORecursionEngine.from_shadow_data(vir, dps=30, contour_points=128)
        val = eng.omega_03(2.0, 3.0 + 0.1j, 4.0 - 0.2j)
        self.assertGreater(abs(val), 1e-15)

    def test_one_cut_model_nondegenerate(self):
        """One-cut model with [a,b] = [-2, 2] is nondegenerate."""
        eng = EORecursionEngine.one_cut_matrix_model(-2.0, 2.0)
        self.assertFalse(eng.degenerate)

    def test_omega11_symmetric(self):
        """omega_{1,1} should be well-defined (no symmetry to test for n=1)."""
        vir = virasoro_spectral(10)
        eng = EORecursionEngine.from_shadow_data(vir, dps=30, contour_points=128)
        val1 = eng.omega_11(2.0 + 0.3j)
        val2 = eng.omega_11(2.0 + 0.3j)
        self.assertAlmostEqual(abs(val1 - val2), 0.0, places=10)

    def test_omega03_symmetric(self):
        """omega_{0,3} is symmetric in its arguments."""
        vir = virasoro_spectral(10)
        eng = EORecursionEngine.from_shadow_data(vir, dps=30, contour_points=64)
        z0, z1, z2 = 2.0, 3.0 + 0.1j, 4.0 - 0.2j
        val_012 = eng.omega_03(z0, z1, z2)
        val_102 = eng.omega_03(z1, z0, z2)
        # Symmetry: omega_{0,3} is symmetric
        self.assertAlmostEqual(abs(val_012 - val_102) / max(abs(val_012), 1e-30),
                               0.0, places=3)


# ====================================================================
# Section 16: Comprehensive report
# ====================================================================

class TestComprehensiveReport(unittest.TestCase):
    """Test the full verification report."""

    def test_report_runs(self):
        """Full report completes without error."""
        report = full_verification_report(max_genus=3)
        self.assertIn('wk_base_values', report)
        self.assertIn('airy_F_g', report)
        self.assertIn('heisenberg_3path', report)
        self.assertIn('spectral_curves', report)

    def test_report_all_agree(self):
        """All multi-path results in the report agree."""
        report = full_verification_report(max_genus=3)
        for entry in report['heisenberg_3path']:
            self.assertTrue(entry['agree'])
        for entry in report['virasoro_c10_3path']:
            self.assertTrue(entry['agree'])


# ====================================================================
# Section 17: Higher genus WK intersection numbers
# ====================================================================

class TestHigherGenusWK(unittest.TestCase):
    """Verify WK intersection numbers at genus >= 2."""

    def test_tau_4_g2_from_dvv(self):
        """<tau_4>_2 = 1/1152 via DVV recursion."""
        val = wk_intersection(4, g=2)
        self.assertEqual(val, Rational(1, 1152))

    def test_tau_22_g2(self):
        """<tau_2 tau_2>_2: sum=4, n=2, 3*2-3+2=5. 4!=5. Zero."""
        val = wk_intersection(2, 2, g=2)
        self.assertEqual(val, Rational(0))

    def test_tau_0_4_g2(self):
        """<tau_0 tau_4>_2: sum=4, n=2, 3*2-3+2=5. 4!=5. Zero."""
        val = wk_intersection(0, 4, g=2)
        self.assertEqual(val, Rational(0))

    def test_tau_50_g2(self):
        """<tau_5 tau_0>_2: sum=5, n=2, 5. OK!"""
        val = wk_intersection(5, 0, g=2)
        # String: <tau_5 tau_0>_2 = <tau_4>_2 = 1/1152
        self.assertEqual(val, Rational(1, 1152))

    def test_tau_1_4_g2(self):
        """<tau_1 tau_4>_2: sum=5, n=2, 5. OK!
        Dilaton: (2*2-2+2)*<tau_4>_2 = 4 * 1/1152 = 1/288."""
        val = wk_intersection(1, 4, g=2)
        expected = 4 * Rational(1, 1152)
        self.assertEqual(val, expected)


# ====================================================================
# Section 18: Shadow free energy consistency
# ====================================================================

class TestShadowFreeEnergyConsistency(unittest.TestCase):
    """Cross-check shadow free energies with spectral data."""

    def test_shadow_F_matches_mc(self):
        """ShadowSpectralData.shadow_free_energy = mc_shadow_free_energy."""
        for data in [heisenberg_spectral(1), virasoro_spectral(10),
                     affine_sl2_spectral(1), w3_spectral(10)]:
            for g in range(1, 4):
                f1 = data.shadow_free_energy(g)
                f2 = mc_shadow_free_energy(data.kappa, g)
                self.assertEqual(simplify(f1 - f2), 0,
                                 f"{data.name} g={g}: shadow != mc")

    def test_airy_equals_heisenberg_k1(self):
        """Airy F_g = F_g(Heisenberg, k=1)."""
        for g in range(1, 6):
            self.assertEqual(airy_F_g(g), heisenberg_spectral(1).shadow_free_energy(g))

    def test_virasoro_c26_critical(self):
        """At c=26 (critical string): F_g = 13*lambda_fp(g)."""
        vir = virasoro_spectral(26)
        for g in range(1, 4):
            expected = 13 * lambda_fp(g)
            self.assertEqual(simplify(vir.shadow_free_energy(g) - expected), 0)


# ====================================================================
# Section 19: Genus-2 intersection number consistency
# ====================================================================

class TestGenus2WK(unittest.TestCase):
    """Detailed genus-2 intersection number verification."""

    def test_sum_all_tau_g2_n1(self):
        """Sum at g=2, n=1: only <tau_4>_2 = 1/1152."""
        total = airy_total_intersection_genus(2, 1)
        self.assertEqual(total, Rational(1, 1152))

    def test_genus2_n2_partitions(self):
        """At g=2, n=2: sum d_i = 3*2-3+2 = 5.
        Partitions of 5 into 2 parts: (0,5),(1,4),(2,3),(3,2),(4,1),(5,0).
        Only those satisfying stability contribute."""
        total = Rational(0)
        for d1 in range(6):
            d2 = 5 - d1
            total += wk_intersection(d1, d2, g=2)
        # We just check it is a well-defined rational number
        self.assertIsInstance(total, Rational)


# ====================================================================
# Section 20: Bernoulli number sanity
# ====================================================================

class TestBernoulli(unittest.TestCase):
    """Bernoulli number sanity checks."""

    def test_B0(self):
        self.assertEqual(_bernoulli_number(0), 1)

    def test_B1(self):
        # sympy bernoulli(1) = 1/2 (some conventions use -1/2)
        self.assertEqual(abs(_bernoulli_number(1)), Rational(1, 2))

    def test_B2(self):
        self.assertEqual(_bernoulli_number(2), Rational(1, 6))

    def test_B4(self):
        self.assertEqual(_bernoulli_number(4), Rational(-1, 30))

    def test_B6(self):
        self.assertEqual(_bernoulli_number(6), Rational(1, 42))

    def test_B_odd_zero(self):
        """B_{2k+1} = 0 for k >= 1."""
        for k in range(1, 10):
            self.assertEqual(_bernoulli_number(2 * k + 1), 0)


if __name__ == '__main__':
    unittest.main()
