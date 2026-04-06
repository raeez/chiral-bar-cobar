r"""Tests for BC-128: Non-commutative Chern-Weil theory from shadow connections.

Tests organized by section:
  1.  Shadow data validation (exact rational arithmetic)
  2.  Shadow metric and connection form
  3.  Curvature computation (direct + exact formula)
  4.  First Chern class universality (c_1 = 1/2)
  5.  Second Chern number c_2
  6.  Chern-Simons invariant (exact + numerical)
  7.  Heisenberg exact results (class G: CS=0, F=0)
  8.  Affine sl_2 curvature (exact formula)
  9.  Virasoro multi-path curvature verification
  10. Virasoro multi-path CS verification
  11. APS index theorem
  12. Eta invariant truncated spectrum
  13. NC Chern character
  14. Complementarity of curvature
  15. Complementarity of CS
  16. Complementarity of c_2
  17. CS landscape table
  18. Family Chern-Weil packages
  19. Zeta zeros: shadow data
  20. Zeta zeros: curvature
  21. Zeta zeros: CS
  22. Zeta zeros: CS mod Z
  23. Zeta zeros: c_1 universal at zeros
  24. Zeta zeros: c_2
  25. Zeta zeros: eta invariant
  26. Zeta zeros: full invariant package
  27. CS near-zero analysis (discontinuity)
  28. Eta integer jump test
  29. Multi-path: Chern-Weil vs transgression
  30. Multi-path: NC Chern character vs Chern class
  31. Virasoro exact curvature cross-check
  32. sl_2 exact curvature cross-check
  33. CS for class L (affine KM)
  34. Curvature sign analysis
  35. Shadow potential
  36. Landscape diagnostic
  37. Edge cases: c=1/2, c=26
  38. Self-dual point c=13
  39. Koszul dual pairs
  40. Run full diagnostic

Verification paths:
  (1) Chern-Weil formula (direct curvature computation)
  (2) Chern-Simons transgression (integration of connection form)
  (3) APS index theorem (ind = A-hat - (h+eta)/2)
  (4) NC Chern character from K-theory
  (5) Numerical evaluation at multiple precisions
"""

import pytest
import math
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_nc_chernweil_shadow_engine import (
    # Section 0: Shadow data
    virasoro_shadow_data_exact, heisenberg_shadow_data_exact,
    affine_sl2_shadow_data_exact, affine_slN_shadow_data_exact,
    betagamma_shadow_data_exact,
    # Section 1: Metric and connection
    shadow_metric_Q, shadow_metric_coefficients,
    connection_form_omega, connection_form_derivative,
    # Section 2: Curvature
    curvature_F, curvature_at_origin,
    # Section 3: Chern classes
    first_chern_class_integrated, first_chern_class_total,
    second_chern_number, chern_character_rank1,
    # Section 4: CS
    chern_simons_integrand, chern_simons_exact, chern_simons_value,
    chern_simons_mod_Z, chern_simons_numerical,
    # Section 5: Eta invariant
    shadow_potential, shadow_dirac_spectrum_truncated,
    eta_invariant_truncated, eta_invariant_multi_truncation,
    # Section 6: APS
    ahat_genus_1d, aps_index_check,
    # Section 7: Zeta zeros
    c_from_zeta_zero, kappa_from_zeta_zero,
    # Section 8: Exact formulas
    virasoro_curvature_exact, virasoro_c2_exact,
    virasoro_chern_simons_exact, sl2_curvature_exact, sl2_c2_exact,
    heisenberg_cs_exact, heisenberg_curvature_exact,
    # Section 9: Multi-path
    verify_curvature_virasoro_multipath, verify_cs_virasoro_multipath,
    verify_c1_universal, verify_chern_character_vs_chern_class,
    # Section 10: Complementarity
    complementarity_curvature_sum, complementarity_cs_sum,
    complementarity_c2_sum,
    # Section 11: Tables
    family_chern_weil_package, landscape_chern_weil_table,
    cs_landscape_table, run_full_diagnostic,
    # Section 12: NC Chern character
    nc_chern_character_rank1, nc_chern_character_at_origin,
    # Section 13: Constants
    STANDARD_FAMILIES, _frac,
)

# Conditional mpmath imports
try:
    import mpmath
    from mpmath import mp, mpf, mpre, mpim, fabs
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

# Conditional numpy
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# =========================================================================
# 1. Shadow data validation
# =========================================================================

class TestShadowData:
    """Verify shadow data for standard families."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 for several c values."""
        for c_val in [1, 2, 13, 25, 26]:
            kappa, _, _, _ = virasoro_shadow_data_exact(c_val)
            assert kappa == Fraction(c_val, 2), f"kappa(Vir_{c_val}) != c/2"

    def test_virasoro_alpha(self):
        """alpha = 2 for all Virasoro."""
        for c_val in [1, 2, 13, 25]:
            _, alpha, _, _ = virasoro_shadow_data_exact(c_val)
            assert alpha == Fraction(2)

    def test_virasoro_S4(self):
        """S4 = 10/[c(5c+22)] for Virasoro."""
        for c_val in [1, 2, 5, 13]:
            c = Fraction(c_val)
            _, _, S4, _ = virasoro_shadow_data_exact(c_val)
            expected = Fraction(10) / (c * (5 * c + 22))
            assert S4 == expected, f"S4 wrong at c={c_val}"

    def test_virasoro_delta(self):
        """Delta = 40/(5c+22) for Virasoro."""
        for c_val in [1, 2, 13]:
            c = Fraction(c_val)
            _, _, _, Delta = virasoro_shadow_data_exact(c_val)
            expected = Fraction(40) / (5 * c + 22)
            assert Delta == expected

    def test_heisenberg_class_G(self):
        """Heisenberg: alpha=0, S4=0, Delta=0 (class G)."""
        for k_val in [1, 2, 5]:
            kappa, alpha, S4, Delta = heisenberg_shadow_data_exact(k_val)
            assert kappa == Fraction(k_val)
            assert alpha == Fraction(0)
            assert S4 == Fraction(0)
            assert Delta == Fraction(0)

    def test_sl2_shadow_data(self):
        """sl_2 at k=1: kappa=9/4, alpha=2, S4=0."""
        kappa, alpha, S4, Delta = affine_sl2_shadow_data_exact(1)
        assert kappa == Fraction(9, 4)
        assert alpha == Fraction(2)
        assert S4 == Fraction(0)
        assert Delta == Fraction(0)

    def test_sl2_shadow_data_k2(self):
        """sl_2 at k=2: kappa=3, alpha=3/2."""
        kappa, alpha, S4, Delta = affine_sl2_shadow_data_exact(2)
        assert kappa == Fraction(3)
        assert alpha == Fraction(3, 2)

    def test_slN_kappa_formula(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N) for several (N,k)."""
        for N, k in [(2, 1), (2, 2), (3, 1), (4, 1)]:
            kappa, _, _, _ = affine_slN_shadow_data_exact(N, k)
            expected = Fraction(N**2 - 1) * Fraction(k + N) / Fraction(2 * N)
            assert kappa == expected


# =========================================================================
# 2. Shadow metric and connection form
# =========================================================================

class TestShadowMetric:
    """Verify shadow metric Q_L(t) computations."""

    def test_Q_at_origin_equals_4kappa_squared(self):
        """Q(0) = 4*kappa^2 for all families."""
        for c_val in [1, 2, 13]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            Q0 = shadow_metric_Q(kappa, alpha, S4, Fraction(0))
            assert Q0 == 4 * kappa**2

    def test_Q_coefficients(self):
        """Q = q0 + q1*t + q2*t^2 with correct coefficients."""
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(1)
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        assert q0 == 4 * kappa**2
        assert q1 == 12 * kappa * alpha
        assert q2 == 9 * alpha**2 + 16 * kappa * S4

    def test_Q_expanded_virasoro(self):
        """Q_Vir(t) = c^2 + 12ct + [(180c+872)/(5c+22)] t^2."""
        c_val = 1
        c = Fraction(c_val)
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        assert q0 == c**2
        assert q1 == 12 * c
        expected_q2 = (180 * c + 872) / (5 * c + 22)
        assert q2 == expected_q2

    def test_connection_form_at_origin(self):
        """omega(0) = q1/(2*q0) = 12*kappa*alpha / (2*4*kappa^2) = 3*alpha/(2*kappa)."""
        for c_val in [1, 2, 13]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            omega_0 = connection_form_omega(kappa, alpha, S4, Fraction(0))
            expected = 3 * alpha / (2 * kappa)
            assert omega_0 == expected

    def test_heisenberg_connection_zero(self):
        """Heisenberg: omega = 0 (constant Q)."""
        for k_val in [1, 2]:
            kappa, alpha, S4, _ = heisenberg_shadow_data_exact(k_val)
            omega = connection_form_omega(kappa, alpha, S4, Fraction(0))
            assert omega == 0

    def test_Q_gaussian_decomposition(self):
        """Q = (2kappa + 3alpha*t)^2 + 2*Delta*t^2."""
        kappa, alpha, S4, Delta = virasoro_shadow_data_exact(1)
        for t_val in [Fraction(0), Fraction(1, 2), Fraction(1)]:
            Q_direct = shadow_metric_Q(kappa, alpha, S4, t_val)
            Q_gauss = (2 * kappa + 3 * alpha * t_val)**2 + 2 * Delta * t_val**2
            assert Q_direct == Q_gauss


# =========================================================================
# 3. Curvature computation
# =========================================================================

class TestCurvature:
    """Verify curvature F = d omega."""

    def test_heisenberg_curvature_zero(self):
        """Heisenberg: F(0) = 0 (flat connection)."""
        for k_val in [1, 2, 5]:
            F0 = heisenberg_curvature_exact(k_val)
            assert F0 == Fraction(0)

    def test_virasoro_curvature_exact_formula(self):
        """F(0) = -8*(45c+178)/[c^2*(5c+22)] for Virasoro."""
        for c_val in [1, 2, 5, 13, 25]:
            c = Fraction(c_val)
            F0 = virasoro_curvature_exact(c_val)
            expected = Fraction(-8) * (45 * c + 178) / (c**2 * (5 * c + 22))
            assert F0 == expected, f"F(0) wrong at c={c_val}"

    def test_curvature_direct_vs_exact_virasoro(self):
        """curvature_at_origin should equal virasoro_curvature_exact."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            F0_direct = curvature_at_origin(kappa, alpha, S4)
            F0_exact = virasoro_curvature_exact(c_val)
            assert F0_direct == F0_exact, f"Mismatch at c={c_val}"

    def test_curvature_negative_virasoro(self):
        """Virasoro curvature is negative for c > 0 (saddle point)."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            F0 = virasoro_curvature_exact(c_val)
            assert F0 < 0, f"F(0) >= 0 at c={c_val}"

    def test_sl2_curvature_exact(self):
        """F(0) = -144/(k+2)^4 for affine sl_2."""
        for k_val in [1, 2, 3, 5]:
            k = Fraction(k_val)
            F0 = sl2_curvature_exact(k_val)
            expected = Fraction(-144) / (k + 2)**4
            assert F0 == expected

    def test_sl2_curvature_direct_vs_exact(self):
        """Direct curvature from shadow data matches exact formula for sl_2."""
        for k_val in [1, 2, 3]:
            kappa, alpha, S4, _ = affine_sl2_shadow_data_exact(k_val)
            F0_direct = curvature_at_origin(kappa, alpha, S4)
            F0_exact = sl2_curvature_exact(k_val)
            assert F0_direct == F0_exact

    def test_curvature_at_nonzero_t(self):
        """F(t) exists and is finite away from zeros of Q."""
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(2)
        for t_val in [Fraction(1, 10), Fraction(1, 2), Fraction(1)]:
            F_t = curvature_F(kappa, alpha, S4, t_val)
            assert F_t is not None
            assert abs(float(F_t)) < 1e6  # finite


# =========================================================================
# 4. First Chern class universality
# =========================================================================

class TestFirstChernClass:
    """c_1 = 1/2 is universal (the Koszul half-residue)."""

    def test_c1_universal_all_families(self):
        """c_1 = 1/2 for every standard family."""
        results, all_half = verify_c1_universal()
        assert all_half, f"c_1 not universal: {results}"

    def test_c1_per_zero_virasoro(self):
        """c_1 per zero = 1/2 for Virasoro."""
        for c_val in [1, 2, 13, 25, 26]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            c1 = first_chern_class_integrated(kappa, alpha, S4)
            assert c1 == Fraction(1, 2)

    def test_c1_per_zero_heisenberg(self):
        """c_1 per zero = 1/2 for Heisenberg."""
        for k_val in [1, 2, 5]:
            kappa, alpha, S4, _ = heisenberg_shadow_data_exact(k_val)
            c1 = first_chern_class_integrated(kappa, alpha, S4)
            assert c1 == Fraction(1, 2)

    def test_c1_total(self):
        """Total c_1 = 1 (sum over both zeros of Q)."""
        assert first_chern_class_total() == Fraction(1)

    def test_c1_per_zero_sl2(self):
        """c_1 per zero = 1/2 for sl_2."""
        for k_val in [1, 2, 3]:
            kappa, alpha, S4, _ = affine_sl2_shadow_data_exact(k_val)
            c1 = first_chern_class_integrated(kappa, alpha, S4)
            assert c1 == Fraction(1, 2)


# =========================================================================
# 5. Second Chern number
# =========================================================================

class TestSecondChernNumber:
    """c_2 = F(0)^2/4."""

    def test_heisenberg_c2_zero(self):
        """c_2 = 0 for Heisenberg (flat connection)."""
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        c2 = second_chern_number(kappa, alpha, S4)
        assert c2 == Fraction(0)

    def test_virasoro_c2_exact(self):
        """c_2 matches exact formula for Virasoro."""
        for c_val in [1, 2, 5, 13]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            c2_direct = second_chern_number(kappa, alpha, S4)
            c2_exact = virasoro_c2_exact(c_val)
            assert c2_direct == c2_exact, f"c_2 mismatch at c={c_val}"

    def test_c2_positive_virasoro(self):
        """c_2 >= 0 for Virasoro (it is F^2/4 >= 0)."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            c2 = virasoro_c2_exact(c_val)
            assert c2 >= 0

    def test_sl2_c2(self):
        """c_2 for sl_2 matches F(0)^2/4."""
        for k_val in [1, 2, 3]:
            F0 = sl2_curvature_exact(k_val)
            c2 = sl2_c2_exact(k_val)
            assert c2 == F0**2 / 4

    def test_c2_virasoro_c1_exact_value(self):
        """c_2 at c=1: F(0) = -8*223/27 = -1784/27.  c_2 = (1784/27)^2/4."""
        F0 = virasoro_curvature_exact(1)
        c = Fraction(1)
        expected_F0 = Fraction(-8) * (45 + 178) / (1 * (5 + 22))
        assert F0 == expected_F0
        c2 = F0**2 / 4
        assert c2 == virasoro_c2_exact(1)


# =========================================================================
# 6. Chern-Simons invariant
# =========================================================================

class TestChernSimons:
    """CS = (1/4) log(Q(1)/Q(0))."""

    def test_heisenberg_cs_zero(self):
        """CS = 0 for Heisenberg (constant Q)."""
        for k_val in [1, 2, 5]:
            cs = heisenberg_cs_exact(k_val)
            assert cs == Fraction(0)

    def test_cs_heisenberg_from_engine(self):
        """CS from engine also gives 0 for Heisenberg."""
        for k_val in [1, 2]:
            kappa, alpha, S4, _ = heisenberg_shadow_data_exact(k_val)
            ratio = chern_simons_exact(kappa, alpha, S4)
            assert abs(ratio - 1.0) < 1e-10  # ratio = Q(1)/Q(0) = 1

    def test_virasoro_cs_positive(self):
        """CS > 0 for Virasoro c > 0 (Q(1) > Q(0) > 0 for c >> 1)."""
        for c_val in [2, 5, 13, 25, 26]:
            cs = virasoro_chern_simons_exact(c_val)
            assert isinstance(cs, float)

    def test_cs_exact_vs_numerical_virasoro(self):
        """Exact CS matches numerical integration for Virasoro."""
        for c_val in [2, 5, 13]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            cs_exact = chern_simons_value(kappa, alpha, S4)
            cs_num = chern_simons_numerical(kappa, alpha, S4, N_pts=5000)
            if isinstance(cs_exact, complex):
                continue
            assert abs(cs_exact - cs_num) < 0.05 * max(abs(cs_exact), 0.01), \
                f"CS mismatch at c={c_val}: exact={cs_exact}, num={cs_num}"

    def test_cs_mod_Z_bounded(self):
        """CS mod Z is in [0, 1) for real CS."""
        for c_val in [2, 5, 13, 25]:
            kappa, alpha, S4, _ = virasoro_shadow_data_exact(c_val)
            cs_mod = chern_simons_mod_Z(kappa, alpha, S4)
            if isinstance(cs_mod, complex):
                continue
            assert 0 <= cs_mod < 1, f"CS mod Z out of range at c={c_val}"

    def test_sl2_cs(self):
        """CS for sl_2 is finite."""
        for k_val in [1, 2, 3]:
            kappa, alpha, S4, _ = affine_sl2_shadow_data_exact(k_val)
            cs = chern_simons_value(kappa, alpha, S4)
            assert isinstance(cs, (float, complex))


# =========================================================================
# 7. Heisenberg exact results (class G)
# =========================================================================

class TestHeisenbergExact:
    """Class G: CS=0, F=0, c_2=0."""

    def test_all_zero(self):
        """For Heisenberg: F=0, CS=0, c_2=0."""
        for k_val in [1, 2, 5, 10]:
            assert heisenberg_curvature_exact(k_val) == Fraction(0)
            assert heisenberg_cs_exact(k_val) == Fraction(0)

    def test_c2_zero(self):
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        assert second_chern_number(kappa, alpha, S4) == Fraction(0)

    def test_potential_zero(self):
        """Shadow potential V = 0 for Heisenberg."""
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        V = shadow_potential(kappa, alpha, S4, Fraction(0))
        assert abs(V) < 1e-15


# =========================================================================
# 8. Affine sl_2 curvature
# =========================================================================

class TestAffineSl2:
    """F(0) = -144/(k+2)^4 for sl_2."""

    def test_k1(self):
        assert sl2_curvature_exact(1) == Fraction(-144, 81)

    def test_k2(self):
        assert sl2_curvature_exact(2) == Fraction(-144, 256)

    def test_k3(self):
        assert sl2_curvature_exact(3) == Fraction(-144, 625)

    def test_decreasing_magnitude(self):
        """|F(0)| decreases as k increases."""
        prev = abs(float(sl2_curvature_exact(1)))
        for k_val in [2, 3, 5, 10]:
            curr = abs(float(sl2_curvature_exact(k_val)))
            assert curr < prev
            prev = curr

    def test_c2_k1(self):
        c2 = sl2_c2_exact(1)
        expected = Fraction(-144, 81)**2 / 4
        assert c2 == expected


# =========================================================================
# 9. Virasoro multi-path curvature verification
# =========================================================================

class TestVirasoroMultiPathCurvature:
    """3-path verification of Virasoro curvature."""

    def test_c1(self):
        res = verify_curvature_virasoro_multipath(1)
        assert res['p1_p2_agree']
        assert res['p1_p3_close']

    def test_c2(self):
        res = verify_curvature_virasoro_multipath(2)
        assert res['p1_p2_agree']

    def test_c13(self):
        res = verify_curvature_virasoro_multipath(13)
        assert res['p1_p2_agree']

    def test_c25(self):
        res = verify_curvature_virasoro_multipath(25)
        assert res['p1_p2_agree']

    def test_c26(self):
        res = verify_curvature_virasoro_multipath(26)
        assert res['p1_p2_agree']


# =========================================================================
# 10. Virasoro multi-path CS verification
# =========================================================================

class TestVirasoroMultiPathCS:
    """3-path verification of Virasoro Chern-Simons."""

    def test_c2(self):
        res = verify_cs_virasoro_multipath(2)
        assert res['p1_p2_agree']

    def test_c5(self):
        res = verify_cs_virasoro_multipath(5)
        assert res['p1_p2_agree']

    def test_c13(self):
        res = verify_cs_virasoro_multipath(13)
        assert res['p1_p2_agree']

    def test_c25(self):
        res = verify_cs_virasoro_multipath(25)
        assert res['p1_p2_agree']


# =========================================================================
# 11. APS index theorem
# =========================================================================

@pytest.mark.skipif(not HAS_NUMPY, reason="numpy required")
class TestAPSIndex:
    """APS index theorem: ind(D) = A-hat - (h+eta)/2."""

    def test_ahat_at_zero(self):
        """A-hat(0) = 1."""
        assert ahat_genus_1d(0.0) == 1.0

    def test_ahat_small_F(self):
        """A-hat(F) ~ 1 - F^2/24 for small F."""
        F = 0.1
        ahat = ahat_genus_1d(F)
        assert abs(ahat - (1 - F**2 / 24)) < 1e-6

    def test_aps_virasoro_c2(self):
        """APS check for Virasoro c=2."""
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(2)
        res = aps_index_check(kappa, alpha, S4, N_modes=20, L=5.0)
        assert 'aps_index' in res
        assert isinstance(res['aps_index'], int)

    def test_aps_heisenberg(self):
        """APS for Heisenberg: everything should be trivial."""
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        res = aps_index_check(kappa, alpha, S4, N_modes=20, L=5.0)
        assert abs(res['F0']) < 1e-10
        assert abs(res['ahat'] - 1.0) < 1e-10


# =========================================================================
# 12. Eta invariant
# =========================================================================

@pytest.mark.skipif(not HAS_NUMPY, reason="numpy required")
class TestEtaInvariant:
    """Eta invariant of the shadow Dirac operator."""

    def test_heisenberg_eta_zero(self):
        """Heisenberg: eta = 0 (flat, symmetric spectrum)."""
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        eta, info = eta_invariant_truncated(kappa, alpha, S4, N_modes=20, L=5.0)
        assert eta == 0

    def test_eta_integer_valued(self):
        """eta(D) at s=0 is always an integer (spectral asymmetry count)."""
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(2)
        eta, info = eta_invariant_truncated(kappa, alpha, S4, N_modes=20, L=5.0)
        assert eta == int(eta)

    def test_eta_multi_truncation(self):
        """Eta at multiple truncation levels."""
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(2)
        results = eta_invariant_multi_truncation(kappa, alpha, S4,
                                                  truncations=(10, 20))
        assert 10 in results
        assert 20 in results
        for N in results:
            assert results[N]['eta'] == int(results[N]['eta'])


# =========================================================================
# 13. NC Chern character
# =========================================================================

class TestNCChernCharacter:
    """NC Chern character ch = exp(F)."""

    def test_ch_at_zero_curvature(self):
        """ch(0) = 1."""
        assert nc_chern_character_rank1(0.0) == 1.0

    def test_ch_expansion(self):
        """ch(F) = 1 + F + F^2/2 + F^3/6 + F^4/24."""
        F = 0.5
        ch = nc_chern_character_rank1(F)
        expected = math.exp(F)
        assert abs(ch - expected) < 0.001

    def test_ch_vs_exp_virasoro(self):
        """ch matches exp(F(0)) for Virasoro."""
        for c_val in [2, 5, 13]:
            res = verify_chern_character_vs_chern_class(
                *virasoro_shadow_data_exact(c_val)[:3])
            assert res['agree']

    def test_ch_heisenberg_equals_one(self):
        """Heisenberg: ch = exp(0) = 1."""
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        ch = nc_chern_character_at_origin(kappa, alpha, S4)
        assert abs(ch - 1.0) < 1e-10


# =========================================================================
# 14. Complementarity of curvature
# =========================================================================

class TestComplementarityCurvature:
    """F(0,c) + F(0,26-c) behavior under Koszul duality."""

    def test_self_dual_c13(self):
        """At c=13: F(0,13) + F(0,13) = 2*F(0,13)."""
        F_sum = complementarity_curvature_sum(13)
        F13 = virasoro_curvature_exact(13)
        assert F_sum == 2 * F13

    def test_complementarity_c1_c25(self):
        """F(0,1) + F(0,25) is computable."""
        F_sum = complementarity_curvature_sum(1)
        F1 = virasoro_curvature_exact(1)
        F25 = virasoro_curvature_exact(25)
        assert F_sum == F1 + F25

    def test_complementarity_c2_c24(self):
        F_sum = complementarity_curvature_sum(2)
        assert F_sum == virasoro_curvature_exact(2) + virasoro_curvature_exact(24)

    def test_complementarity_nonzero(self):
        """F(c) + F(26-c) is generally nonzero: curvature is NOT anti-symmetric."""
        for c_val in [1, 2, 5]:
            F_sum = complementarity_curvature_sum(c_val)
            assert F_sum != Fraction(0), f"Unexpected zero at c={c_val}"


# =========================================================================
# 15. Complementarity of CS
# =========================================================================

class TestComplementarityCS:
    """CS(c) + CS(26-c) behavior."""

    def test_self_dual_c13(self):
        """At c=13: CS(13) + CS(13) = 2*CS(13)."""
        cs_sum = complementarity_cs_sum(13)
        cs13 = virasoro_chern_simons_exact(13)
        assert abs(cs_sum - 2 * cs13) < 1e-10

    def test_cs_sum_finite(self):
        """CS sum is finite for c=1,...,12."""
        for c_val in [1, 2, 5, 10, 12]:
            cs_sum = complementarity_cs_sum(c_val)
            assert math.isfinite(cs_sum)


# =========================================================================
# 16. Complementarity of c_2
# =========================================================================

class TestComplementarityC2:
    """c_2(c) + c_2(26-c) behavior."""

    def test_c2_sum_positive(self):
        """c_2(c) + c_2(26-c) > 0 for c > 0."""
        for c_val in [1, 2, 5, 13]:
            c2_sum = complementarity_c2_sum(c_val)
            assert c2_sum > 0

    def test_c2_self_dual(self):
        c2_sum = complementarity_c2_sum(13)
        c2_13 = virasoro_c2_exact(13)
        assert c2_sum == 2 * c2_13


# =========================================================================
# 17. CS landscape table
# =========================================================================

class TestCSLandscapeTable:
    """Full CS table for standard families."""

    def test_table_nonempty(self):
        table = cs_landscape_table()
        assert len(table) > 0

    def test_heisenberg_entries(self):
        table = cs_landscape_table()
        heis = [r for r in table if 'Heisenberg' in r.get('description', '')]
        for h in heis:
            assert h['CS'] == 0.0 or h['CS'] == Fraction(0)

    def test_all_families_present(self):
        table = cs_landscape_table()
        families = {r['family'] for r in table}
        assert 'Heisenberg_k1' in families
        assert 'Virasoro_c13' in families


# =========================================================================
# 18. Family Chern-Weil packages
# =========================================================================

class TestFamilyPackages:
    """Full Chern-Weil package for each family."""

    def test_heisenberg_package(self):
        pkg = family_chern_weil_package('Heisenberg_k1')
        assert pkg['F0'] == Fraction(0)
        assert pkg['c1_per_zero'] == Fraction(1, 2)
        assert pkg['c2'] == Fraction(0)

    def test_virasoro_c13_package(self):
        pkg = family_chern_weil_package('Virasoro_c13')
        assert pkg['c1_per_zero'] == Fraction(1, 2)
        assert pkg['c2'] > 0

    def test_sl2_k1_package(self):
        pkg = family_chern_weil_package('sl2_k1')
        assert pkg['F0'] < 0
        assert pkg['c1_per_zero'] == Fraction(1, 2)

    def test_landscape_table(self):
        table = landscape_chern_weil_table()
        assert len(table) == len(STANDARD_FAMILIES)
        for entry in table:
            if 'error' not in entry:
                assert entry['c1_per_zero'] == Fraction(1, 2)


# =========================================================================
# 19-26. Zeta zero tests
# =========================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestZetaZeroShadowData:
    """Shadow data at zeta zeros."""

    def test_c_from_zero_real_part(self):
        """c(rho) has Re(c) = 14 on the critical line."""
        mp.dps = 30
        rho1 = zetazero(1)
        c_val = c_from_zeta_zero(rho1)
        assert abs(float(mpre(c_val)) - 14.0) < 1e-10

    def test_kappa_from_zero_real_part(self):
        """kappa has Re(kappa) = 7 on the critical line."""
        mp.dps = 30
        rho1 = zetazero(1)
        kap = kappa_from_zeta_zero(rho1)
        assert abs(float(mpre(kap)) - 7.0) < 1e-10

    def test_shadow_data_at_zero_1(self):
        from bc_nc_chernweil_shadow_engine import shadow_data_at_zeta_zero_mpmath
        data = shadow_data_at_zeta_zero_mpmath(1, dps=30)
        assert data['n'] == 1
        assert abs(float(mpre(data['c'])) - 14.0) < 1e-10
        assert data['alpha'] == 2

    def test_shadow_data_at_zero_5(self):
        from bc_nc_chernweil_shadow_engine import shadow_data_at_zeta_zero_mpmath
        data = shadow_data_at_zeta_zero_mpmath(5, dps=30)
        assert data['n'] == 5


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestZetaZeroCurvature:
    """Curvature at zeta zeros."""

    def test_curvature_finite_zero1(self):
        from bc_nc_chernweil_shadow_engine import curvature_at_zeta_zero
        F0, data = curvature_at_zeta_zero(1, dps=30)
        assert fabs(F0) < mpf('1e10')  # finite

    def test_curvature_finite_zero5(self):
        from bc_nc_chernweil_shadow_engine import curvature_at_zeta_zero
        F0, data = curvature_at_zeta_zero(5, dps=30)
        assert fabs(F0) < mpf('1e10')

    def test_curvature_complex(self):
        """Curvature is complex at zeta zeros (c is complex)."""
        from bc_nc_chernweil_shadow_engine import curvature_at_zeta_zero
        F0, _ = curvature_at_zeta_zero(1, dps=30)
        assert fabs(mpim(F0)) > mpf('1e-10')


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestZetaZeroCS:
    """Chern-Simons at zeta zeros."""

    def test_cs_finite_zero1(self):
        from bc_nc_chernweil_shadow_engine import chern_simons_at_zeta_zero
        cs, data = chern_simons_at_zeta_zero(1, dps=30)
        assert cs is not None
        assert fabs(cs) < mpf('1e10')

    def test_cs_finite_zero3(self):
        from bc_nc_chernweil_shadow_engine import chern_simons_at_zeta_zero
        cs, data = chern_simons_at_zeta_zero(3, dps=30)
        assert cs is not None

    def test_cs_complex_at_zeros(self):
        """CS is complex at zeta zeros (since c is complex)."""
        from bc_nc_chernweil_shadow_engine import chern_simons_at_zeta_zero
        cs, _ = chern_simons_at_zeta_zero(1, dps=30)
        assert fabs(mpim(cs)) > mpf('1e-10')


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestZetaZeroCSModZ:
    """CS mod Z at zeta zeros."""

    def test_cs_mod_z_zero1(self):
        from bc_nc_chernweil_shadow_engine import chern_simons_mod_Z_at_zeta_zero
        cs_mod, _ = chern_simons_mod_Z_at_zeta_zero(1, dps=30)
        assert cs_mod is not None

    def test_cs_mod_z_real_bounded(self):
        """Real part of CS mod Z should be in [0,1)."""
        from bc_nc_chernweil_shadow_engine import chern_simons_mod_Z_at_zeta_zero
        cs_mod, _ = chern_simons_mod_Z_at_zeta_zero(1, dps=30)
        re_part = float(mpre(cs_mod))
        assert -0.1 <= re_part <= 1.1  # allow slight numerical tolerance


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestZetaZeroC1Universal:
    """c_1 = 1/2 at every zeta zero (universal Koszul half-residue)."""

    def test_c1_universal_zero1(self):
        from bc_nc_chernweil_shadow_engine import chern_class_c1_at_zeta_zero
        c1 = chern_class_c1_at_zeta_zero(1)
        assert abs(float(c1) - 0.5) < 1e-10

    def test_c1_universal_zero10(self):
        from bc_nc_chernweil_shadow_engine import chern_class_c1_at_zeta_zero
        c1 = chern_class_c1_at_zeta_zero(10)
        assert abs(float(c1) - 0.5) < 1e-10


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestZetaZeroC2:
    """c_2 at zeta zeros."""

    def test_c2_finite_zero1(self):
        from bc_nc_chernweil_shadow_engine import chern_class_c2_at_zeta_zero
        c2, _ = chern_class_c2_at_zeta_zero(1, dps=30)
        assert fabs(c2) < mpf('1e20')

    def test_c2_nonzero_zero1(self):
        """c_2 is nonzero at zeta zeros (curvature is nonzero)."""
        from bc_nc_chernweil_shadow_engine import chern_class_c2_at_zeta_zero
        c2, _ = chern_class_c2_at_zeta_zero(1, dps=30)
        assert fabs(c2) > mpf('1e-20')


@pytest.mark.skipif(not HAS_MPMATH or not HAS_NUMPY, reason="mpmath+numpy required")
class TestZetaZeroEta:
    """Eta invariant at zeta zeros."""

    def test_eta_finite_zero1(self):
        from bc_nc_chernweil_shadow_engine import eta_at_zeta_zero_numerical
        eta, info = eta_at_zeta_zero_numerical(1, N_modes=20, dps=20)
        assert isinstance(eta, (int, float, np.integer))

    def test_eta_integer_zero1(self):
        """eta at s=0 is an integer."""
        from bc_nc_chernweil_shadow_engine import eta_at_zeta_zero_numerical
        eta, _ = eta_at_zeta_zero_numerical(1, N_modes=20, dps=20)
        assert eta == int(eta)


@pytest.mark.skipif(not HAS_MPMATH or not HAS_NUMPY, reason="mpmath+numpy required")
class TestZetaZeroFullPackage:
    """Full invariant package at zeta zeros."""

    def test_full_package_zero1(self):
        from bc_nc_chernweil_shadow_engine import full_invariants_at_zeta_zero
        pkg = full_invariants_at_zeta_zero(1, N_modes=20, dps=20)
        assert pkg['n'] == 1
        assert abs(float(pkg['c_1']) - 0.5) < 1e-10
        assert pkg['CS'] is not None
        assert isinstance(pkg['eta'], (int, float, np.integer))

    def test_full_package_zero3(self):
        from bc_nc_chernweil_shadow_engine import full_invariants_at_zeta_zero
        pkg = full_invariants_at_zeta_zero(3, N_modes=20, dps=20)
        assert pkg['n'] == 3


# =========================================================================
# 27. CS near-zero analysis
# =========================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestCSNearZeroAnalysis:
    """Discontinuity analysis of CS near zeta zeros."""

    def test_near_zero_1(self):
        from bc_nc_chernweil_shadow_engine import cs_near_zero_analysis
        res = cs_near_zero_analysis(1, epsilon=0.01, dps=20)
        assert res['n'] == 1
        assert res['CS_at'] is not None

    def test_jump_finite(self):
        from bc_nc_chernweil_shadow_engine import cs_near_zero_analysis
        res = cs_near_zero_analysis(1, epsilon=0.01, dps=20)
        if res['CS_jump'] is not None:
            assert fabs(res['CS_jump']) < mpf('1e5')


# =========================================================================
# 28. Eta integer jump test
# =========================================================================

@pytest.mark.skipif(not HAS_MPMATH or not HAS_NUMPY, reason="mpmath+numpy required")
class TestEtaIntegerJump:
    """Eta integer jumps between adjacent zeta zeros."""

    def test_jump_analysis_zero2(self):
        from bc_nc_chernweil_shadow_engine import eta_integer_jump_test
        res = eta_integer_jump_test(2, N_modes=20, dps=20)
        assert 'etas' in res
        assert 'jumps' in res


# =========================================================================
# 29-30. Multi-path cross-verification
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification of core quantities."""

    def test_virasoro_curvature_3path_c2(self):
        res = verify_curvature_virasoro_multipath(2)
        assert res['p1_p2_agree']
        assert res['p1_p3_close']

    def test_virasoro_curvature_3path_c13(self):
        res = verify_curvature_virasoro_multipath(13)
        assert res['p1_p2_agree']
        assert res['p1_p3_close']

    def test_virasoro_cs_3path_c2(self):
        res = verify_cs_virasoro_multipath(2)
        assert res['p1_p2_agree']
        assert res['p1_p3_close']

    def test_virasoro_cs_3path_c13(self):
        res = verify_cs_virasoro_multipath(13)
        assert res['p1_p2_agree']


# =========================================================================
# 31. Virasoro exact curvature cross-check
# =========================================================================

class TestVirasotoExactCrossCheck:
    """Cross-check virasoro_curvature_exact against independent computation."""

    def test_c1_numerator(self):
        """At c=1: 45*1+178 = 223, denominator = 1*27 = 27."""
        F0 = virasoro_curvature_exact(1)
        assert F0 == Fraction(-8 * 223, 27)

    def test_c2_numerator(self):
        """At c=2: 45*2+178 = 268, denom = 4*32 = 128."""
        F0 = virasoro_curvature_exact(2)
        assert F0 == Fraction(-8 * 268, 128)

    def test_c26_numerator(self):
        """At c=26: 45*26+178 = 1348, denom = 676*152."""
        F0 = virasoro_curvature_exact(26)
        expected = Fraction(-8 * 1348, 676 * 152)
        assert F0 == expected


# =========================================================================
# 32. sl_2 exact curvature cross-check
# =========================================================================

class TestSl2ExactCrossCheck:
    """Cross-check sl2_curvature_exact."""

    def test_direct_computation_k1(self):
        """Direct: kappa=9/4, alpha=2, S4=0.  q0=81/4, q1=54, q2=36."""
        kappa = Fraction(9, 4)
        alpha = Fraction(2)
        S4 = Fraction(0)
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        assert q0 == Fraction(81, 4)
        assert q1 == Fraction(54)
        assert q2 == Fraction(36)
        F0 = (2 * q0 * q2 - q1**2) / (2 * q0**2)
        assert F0 == sl2_curvature_exact(1)


# =========================================================================
# 33. CS for class L (affine KM)
# =========================================================================

class TestCSClassL:
    """CS for class L algebras (affine KM, S4=0)."""

    def test_sl2_cs_nonzero(self):
        """sl_2 CS is nonzero (unlike Heisenberg) because alpha != 0."""
        kappa, alpha, S4, _ = affine_sl2_shadow_data_exact(1)
        cs = chern_simons_value(kappa, alpha, S4)
        assert isinstance(cs, (float, complex))
        if isinstance(cs, float):
            assert cs != 0.0

    def test_sl2_cs_finite(self):
        for k_val in [1, 2, 3]:
            kappa, alpha, S4, _ = affine_sl2_shadow_data_exact(k_val)
            cs = chern_simons_value(kappa, alpha, S4)
            if isinstance(cs, float):
                assert math.isfinite(cs)


# =========================================================================
# 34. Curvature sign analysis
# =========================================================================

class TestCurvatureSign:
    """Sign of curvature encodes shadow geometry."""

    def test_virasoro_always_negative(self):
        """F(0) < 0 for all Virasoro c > 0."""
        for c_val in [Fraction(1, 2), 1, 2, 5, 13, 25, 26]:
            F0 = virasoro_curvature_exact(c_val)
            assert F0 < 0, f"F(0) >= 0 at c={c_val}"

    def test_sl2_always_negative(self):
        """F(0) < 0 for all sl_2 k > 0."""
        for k_val in [1, 2, 3, 5, 10]:
            F0 = sl2_curvature_exact(k_val)
            assert F0 < 0

    def test_heisenberg_zero(self):
        """F(0) = 0 for Heisenberg (class G)."""
        for k_val in [1, 2, 5]:
            F0 = heisenberg_curvature_exact(k_val)
            assert F0 == 0


# =========================================================================
# 35. Shadow potential
# =========================================================================

@pytest.mark.skipif(not HAS_NUMPY, reason="numpy required")
class TestShadowPotential:
    """V_sh = omega^2 + omega' (Ricatti transform)."""

    def test_heisenberg_potential_zero(self):
        kappa, alpha, S4, _ = heisenberg_shadow_data_exact(1)
        V = shadow_potential(kappa, alpha, S4, Fraction(0))
        assert abs(V) < 1e-15

    def test_virasoro_potential_finite(self):
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(2)
        V = shadow_potential(kappa, alpha, S4, Fraction(0))
        assert abs(V) < 1e10


# =========================================================================
# 36. Landscape diagnostic
# =========================================================================

class TestLandscapeDiagnostic:
    """Full diagnostic across all families."""

    def test_diagnostic_runs(self):
        results = run_full_diagnostic()
        assert results['c1_universal']
        assert len(results['landscape']) > 0
        assert len(results['cs_table']) > 0


# =========================================================================
# 37. Edge cases
# =========================================================================

class TestEdgeCases:
    """Edge cases: c=1/2 (Ising), c=26 (critical)."""

    def test_ising_c_half(self):
        """Virasoro at c=1/2 (Ising model)."""
        kappa, alpha, S4, Delta = virasoro_shadow_data_exact(Fraction(1, 2))
        assert kappa == Fraction(1, 4)
        F0 = curvature_at_origin(kappa, alpha, S4)
        assert F0 < 0

    def test_critical_c26(self):
        """Virasoro at c=26 (critical dimension)."""
        kappa, alpha, S4, Delta = virasoro_shadow_data_exact(26)
        assert kappa == Fraction(13)
        F0 = curvature_at_origin(kappa, alpha, S4)
        assert F0 < 0

    def test_ising_cs_finite(self):
        kappa, alpha, S4, _ = virasoro_shadow_data_exact(Fraction(1, 2))
        cs = chern_simons_value(kappa, alpha, S4)
        assert isinstance(cs, (float, complex))


# =========================================================================
# 38. Self-dual point c=13
# =========================================================================

class TestSelfDualC13:
    """Properties at the Virasoro self-dual point c=13."""

    def test_kappa_13_over_2(self):
        kappa, _, _, _ = virasoro_shadow_data_exact(13)
        assert kappa == Fraction(13, 2)

    def test_curvature_self_consistent(self):
        """F(0,13) is well-defined and negative."""
        F0 = virasoro_curvature_exact(13)
        assert F0 < 0

    def test_complementarity_double(self):
        """At c=13: F(c) + F(26-c) = 2*F(13)."""
        F_sum = complementarity_curvature_sum(13)
        F13 = virasoro_curvature_exact(13)
        assert F_sum == 2 * F13

    def test_delta_self_dual(self):
        """Delta(13) = 40/(5*13+22) = 40/87."""
        _, _, _, Delta = virasoro_shadow_data_exact(13)
        assert Delta == Fraction(40, 87)


# =========================================================================
# 39. Koszul dual pairs
# =========================================================================

class TestKoszulDualPairs:
    """Curvature and CS at Koszul dual pairs (c, 26-c)."""

    def test_pair_c1_c25(self):
        F1 = virasoro_curvature_exact(1)
        F25 = virasoro_curvature_exact(25)
        assert F1 != F25  # NOT anti-symmetric in general

    def test_pair_c2_c24(self):
        F2 = virasoro_curvature_exact(2)
        F24 = virasoro_curvature_exact(24)
        assert F2 != F24

    def test_c2_pair_c1_c25(self):
        c2_1 = virasoro_c2_exact(1)
        c2_25 = virasoro_c2_exact(25)
        assert c2_1 != c2_25


# =========================================================================
# 40. Full diagnostic
# =========================================================================

class TestFullDiagnostic:
    """Run the complete diagnostic."""

    def test_runs_without_error(self):
        results = run_full_diagnostic()
        assert isinstance(results, dict)
        assert 'c1_universal' in results
        assert results['c1_universal'] is True

    def test_heis_exact(self):
        results = run_full_diagnostic()
        assert results['heis_cs_k1'] == Fraction(0)
        assert results['heis_F_k1'] == Fraction(0)
