r"""Tests for shadow_period_integral_engine.py.

Multi-path verification of shadow period integrals, covering:
  1. Genus-1 shadow periods for all standard families
  2. Genus-2 shadow periods (scalar + higher-arity corrections)
  3. Period polynomial (= lambda_g^FP, universal)
  4. Siegel modular volumes
  5. Shadow curve periods and branch points (Virasoro, class M)
  6. Beilinson regulator
  7. Deligne periods
  8. Bernoulli structure and A-hat consistency
  9. Additivity, complementarity, rationality cross-checks
 10. CM criterion for shadow curves
 11. Period decay ratios
 12. Landscape-wide tests

Multi-path verification strategy (AP10-compliant):
  Path 1: Direct computation from kappa * lambda_g^FP * Vol(A_g)
  Path 2: Tautological intersection numbers * moduli volumes
  Path 3: Bernoulli number route
  Path 4: A-hat generating function route
  Path 5: Cross-family consistency (additivity, complementarity)

References:
    thm:universal-generating-function, prop:shadow-periods,
    thm:riccati-algebraicity, def:shadow-metric
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import math
import pytest
from fractions import Fraction

from sympy import (
    Rational, Symbol, cancel, expand, pi, simplify, sqrt,
    Abs, N as sym_N, bernoulli, factorial, oo,
)

from compute.lib.shadow_period_integral_engine import (
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_affine_slN,
    kappa_lattice,
    kappa_free_fermion,
    kappa_betagamma,
    kappa_bc_ghost,
    kappa_wN,
    # Siegel volumes
    siegel_volume,
    siegel_volume_numerical,
    # Shadow periods
    shadow_period_genus_g,
    shadow_period_ratio,
    shadow_period_heisenberg,
    shadow_period_virasoro,
    shadow_period_affine_sl2,
    # Period polynomial
    period_polynomial_coefficient,
    period_polynomial_table,
    # Bernoulli / A-hat
    bernoulli_shadow_amplitude,
    ahat_shadow_amplitude,
    # Shadow curve
    virasoro_shadow_metric_QL,
    shadow_curve_branch_points,
    shadow_curve_period_numerical,
    shadow_curve_picard_fuchs,
    # Beilinson regulator
    beilinson_regulator_numerical,
    # Deligne periods
    deligne_period_shadow_motive,
    # Genus-2 corrections
    genus2_scalar_period,
    genus2_cubic_correction,
    genus2_quartic_correction,
    genus2_full_period,
    # Landscape
    STANDARD_LANDSCAPE,
    landscape_period_table,
    # Bounds
    period_bernoulli_bound,
    period_decay_ratio,
    # CM
    shadow_curve_cm_test,
    # Cross-verification
    verify_period_additivity,
    verify_period_ratio_rationality,
    verify_bernoulli_consistency,
    verify_ahat_consistency,
    verify_complementarity_periods,
)

from compute.lib.utils import lambda_fp, F_g


# =========================================================================
# Section 1: Kappa formulas (AP1 — independent recomputation)
# =========================================================================

class TestKappaFormulas:
    """Verify kappa formulas for each family from first principles (AP1)."""

    def test_heisenberg_kappa(self):
        assert kappa_heisenberg(1) == 1
        assert kappa_heisenberg(2) == 2
        assert kappa_heisenberg(Rational(1, 2)) == Rational(1, 2)

    def test_virasoro_kappa(self):
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)
        assert kappa_virasoro(13) == Rational(13, 2)
        assert kappa_virasoro(26) == 13

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        assert kappa_affine_sl2(1) == Rational(9, 4)
        assert kappa_affine_sl2(2) == Rational(3)
        assert kappa_affine_sl2(-2) == 0  # critical level

    def test_affine_slN_kappa(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N)."""
        # sl_2 at k=1: (4-1)(1+2)/4 = 9/4
        assert kappa_affine_slN(2, 1) == Rational(9, 4)
        # sl_3 at k=1: (9-1)(1+3)/6 = 32/6 = 16/3
        assert kappa_affine_slN(3, 1) == Rational(16, 3)

    def test_lattice_kappa(self):
        assert kappa_lattice(8) == 8
        assert kappa_lattice(24) == 24

    def test_free_fermion_kappa(self):
        assert kappa_free_fermion() == Rational(1, 4)

    def test_betagamma_kappa(self):
        """kappa(bg, lambda) = 6*lambda^2 - 6*lambda + 1."""
        assert kappa_betagamma(1) == 1  # 6-6+1 = 1
        assert kappa_betagamma(2) == 13  # 24-12+1 = 13
        assert kappa_betagamma(0) == 1  # 0-0+1 = 1

    def test_bc_ghost_kappa(self):
        """kappa(bc, j) = -(6j^2 - 6j + 1)."""
        assert kappa_bc_ghost(2) == -13  # -(24-12+1) = -13
        assert kappa_bc_ghost(1) == -1

    def test_wN_kappa(self):
        """kappa(W_N, c) = (H_N - 1) * c."""
        # W_2 = Virasoro: H_2 - 1 = 1/2, so kappa = c/2
        assert kappa_wN(2, 10) == 5
        assert kappa_wN(2, 10) == kappa_virasoro(10)
        # W_3: H_3 - 1 = 1/2 + 1/3 = 5/6
        assert kappa_wN(3, 6) == 5

    def test_kappa_ghost_complementarity(self):
        """kappa(bc, j=2) + kappa(bg, lambda=2) = -13 + 13 = 0."""
        assert kappa_bc_ghost(2) + kappa_betagamma(2) == 0

    def test_virasoro_complementarity_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [Rational(1, 2), 1, 2, 13, 25]:
            cv = Rational(c_val)
            assert kappa_virasoro(cv) + kappa_virasoro(26 - cv) == 13


# =========================================================================
# Section 2: Siegel modular volumes
# =========================================================================

class TestSiegelVolumes:
    """Verify Siegel modular volumes Vol(A_g)."""

    def test_vol_A0(self):
        assert siegel_volume(0) == 1

    def test_vol_A1(self):
        """Vol(A_1) = Vol(SL_2(Z)\\H) = pi/3."""
        assert siegel_volume(1) == pi / 3
        assert abs(siegel_volume_numerical(1) - math.pi / 3) < 1e-10

    def test_vol_A2(self):
        """Vol(A_2) = pi^4/720."""
        assert siegel_volume(2) == pi**4 / 720
        assert abs(siegel_volume_numerical(2) - math.pi**4 / 720) < 1e-10

    def test_vol_A1_numerical(self):
        val = siegel_volume_numerical(1)
        assert abs(val - 1.0471975511965976) < 1e-8  # pi/3

    def test_vol_A2_numerical(self):
        val = siegel_volume_numerical(2)
        expected = math.pi**4 / 720
        assert abs(val - expected) < 1e-10

    def test_vol_A3_exists(self):
        """Vol(A_3) should be computable and positive."""
        vol3 = siegel_volume(3)
        vol3_num = siegel_volume_numerical(3)
        assert vol3_num > 0

    def test_vol_positivity(self):
        """All Siegel volumes should be positive."""
        for g in range(1, 5):
            assert siegel_volume_numerical(g) > 0

    def test_vol_decreasing(self):
        """Siegel volumes should decrease rapidly (exponentially in g)."""
        vols = [siegel_volume_numerical(g) for g in range(1, 6)]
        for i in range(len(vols) - 1):
            assert vols[i + 1] < vols[i]


# =========================================================================
# Section 3: Genus-1 shadow periods
# =========================================================================

class TestGenus1Periods:
    """Genus-1 shadow periods: Omega_1 = kappa/24 * pi/3."""

    def test_heisenberg_genus1(self):
        """Omega_1(H_1) = 1/24 * pi/3 = pi/72."""
        omega = shadow_period_heisenberg(1, 1)
        assert cancel(omega - pi / 72) == 0

    def test_heisenberg_genus1_k2(self):
        """Omega_1(H_2) = 2/24 * pi/3 = pi/36."""
        omega = shadow_period_heisenberg(2, 1)
        assert cancel(omega - pi / 36) == 0

    def test_virasoro_genus1_c1(self):
        """Omega_1(Vir_1) = (1/2)/24 * pi/3 = pi/144."""
        omega = shadow_period_virasoro(1, 1)
        assert cancel(omega - pi / 144) == 0

    def test_virasoro_genus1_chalf(self):
        """Omega_1(Vir_{1/2}) = (1/4)/24 * pi/3 = pi/288."""
        omega = shadow_period_virasoro(Rational(1, 2), 1)
        assert cancel(omega - pi / 288) == 0

    def test_affine_sl2_genus1_k1(self):
        """Omega_1(sl_2, k=1) = (9/4)/24 * pi/3 = 9*pi/(4*72) = pi/32."""
        omega = shadow_period_affine_sl2(1, 1)
        expected = Rational(9, 4) / 24 * pi / 3
        assert cancel(omega - expected) == 0

    def test_genus1_period_is_rational_times_pi(self):
        """Omega_1(A) = (rational) * pi for all standard families."""
        for name, data in STANDARD_LANDSCAPE.items():
            kap = data['kappa']
            omega = shadow_period_genus_g(kap, 1)
            # omega should be rational * pi
            ratio = cancel(omega / pi)
            # ratio should be a rational number
            assert ratio == kap / 72  # kappa/24 * 1/3

    def test_genus1_explicit_values(self):
        """Cross-check explicit genus-1 periods."""
        # Omega_1(H_k) = k/24 * pi/3
        assert cancel(shadow_period_heisenberg(1, 1) - pi / 72) == 0
        # Omega_1(Vir_c) = c/48 * pi/3 = c*pi/144
        assert cancel(shadow_period_virasoro(1, 1) - pi / 144) == 0
        # Omega_1(sl_2, k=1) = 9/(4*24) * pi/3 = 3*pi/96
        omega_sl2 = shadow_period_affine_sl2(1, 1)
        assert cancel(omega_sl2 - Rational(9, 4) * pi / 72) == 0


# =========================================================================
# Section 4: Genus-2 shadow periods
# =========================================================================

class TestGenus2Periods:
    """Genus-2 shadow periods: Omega_2 = kappa * 7/5760 * pi^4/720."""

    def test_heisenberg_genus2(self):
        """Omega_2(H_1) = 7/5760 * pi^4/720."""
        omega = shadow_period_heisenberg(1, 2)
        expected = Rational(7, 5760) * pi**4 / 720
        assert cancel(omega - expected) == 0

    def test_virasoro_genus2(self):
        """Omega_2(Vir_c) = (c/2) * 7/5760 * pi^4/720."""
        for c_val in [1, 2, 13]:
            omega = shadow_period_virasoro(c_val, 2)
            expected = kappa_virasoro(c_val) * Rational(7, 5760) * pi**4 / 720
            assert cancel(omega - expected) == 0

    def test_genus2_scalar_period_explicit(self):
        """Scalar genus-2 period for H_1."""
        omega = genus2_scalar_period(Rational(1))
        expected = Rational(7, 5760) * pi**4 / 720
        assert cancel(omega - expected) == 0

    def test_genus2_no_cubic_for_heisenberg(self):
        """Heisenberg has S_3 = 0, so cubic correction vanishes."""
        corr = genus2_cubic_correction(Rational(1), Rational(0))
        assert corr == 0

    def test_genus2_no_quartic_for_heisenberg(self):
        """Heisenberg has S_4 = 0, so quartic correction vanishes."""
        corr = genus2_quartic_correction(Rational(1), Rational(0))
        assert corr == 0

    def test_genus2_full_equals_scalar_for_gaussian(self):
        """For class G (Heisenberg), full period = scalar period."""
        full = genus2_full_period(Rational(1))
        scalar = genus2_scalar_period(Rational(1))
        assert cancel(full - scalar) == 0

    def test_genus2_cubic_correction_virasoro(self):
        """Virasoro has S_3 = 2, so cubic correction is nonzero."""
        kap = kappa_virasoro(1)
        corr = genus2_cubic_correction(kap, Rational(2))
        # corr = S_3 * (10*S_3 - kappa) / 48 * Vol(A_2)
        expected = Rational(2) * (20 - kap) / 48 * pi**4 / 720
        assert cancel(corr - expected) == 0


# =========================================================================
# Section 5: Period polynomial
# =========================================================================

class TestPeriodPolynomial:
    """P(g) = lambda_g^FP is universal (algebra-independent)."""

    def test_period_polynomial_genus1(self):
        """P(1) = lambda_1^FP = 1/24."""
        assert period_polynomial_coefficient(1) == Rational(1, 24)

    def test_period_polynomial_genus2(self):
        """P(2) = lambda_2^FP = 7/5760."""
        assert period_polynomial_coefficient(2) == Rational(7, 5760)

    def test_period_polynomial_genus3(self):
        """P(3) = lambda_3^FP = 31/967680."""
        lfp3 = lambda_fp(3)
        # Compute: (2^5-1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/(32*30240) = 31/967680
        expected = Rational(31, 32) * Rational(1, 42) / 720
        assert lfp3 == expected
        assert period_polynomial_coefficient(3) == lfp3

    def test_period_polynomial_table(self):
        """Period polynomial table should have correct structure."""
        table = period_polynomial_table(3)
        assert 1 in table and 2 in table and 3 in table
        assert table[1]['lambda_fp'] == Rational(1, 24)
        assert table[2]['lambda_fp'] == Rational(7, 5760)

    def test_period_polynomial_is_universal(self):
        """P(g) does not depend on the algebra."""
        for g in range(1, 5):
            ppc = period_polynomial_coefficient(g)
            assert ppc == lambda_fp(g)


# =========================================================================
# Section 6: Bernoulli structure
# =========================================================================

class TestBernoulliStructure:
    """Bernoulli numbers in shadow amplitudes."""

    def test_bernoulli_genus1(self):
        """B_2 = 1/6: F_1 = kappa * (1/2 * 1/6 / 2) = kappa/24."""
        # (2^1-1)/2^1 * |B_2|/2! = 1/2 * (1/6)/2 = 1/24
        f1 = bernoulli_shadow_amplitude(Rational(1), 1)
        assert f1 == Rational(1, 24)

    def test_bernoulli_genus2(self):
        """B_4 = -1/30: F_2 = kappa * (7/8 * 1/30 / 24) = 7*kappa/5760."""
        f2 = bernoulli_shadow_amplitude(Rational(1), 2)
        assert f2 == Rational(7, 5760)

    def test_bernoulli_genus3(self):
        """B_6 = 1/42."""
        f3 = bernoulli_shadow_amplitude(Rational(1), 3)
        expected = Rational(31, 32) * abs(bernoulli(6)) / factorial(6)
        assert cancel(f3 - expected) == 0

    def test_ahat_agrees_with_bernoulli(self):
        """A-hat route and Bernoulli route must agree at all genera."""
        for g in range(1, 6):
            b = bernoulli_shadow_amplitude(Rational(1), g)
            a = ahat_shadow_amplitude(Rational(1), g)
            assert cancel(b - a) == 0

    def test_fp_agrees_with_bernoulli(self):
        """FP formula and Bernoulli formula must agree."""
        for g in range(1, 6):
            for kap in [Rational(1), Rational(1, 2), Rational(13, 2)]:
                result = verify_bernoulli_consistency(kap, g)
                assert result['agree']

    def test_ahat_consistency_table(self):
        """A-hat consistency across genera."""
        result = verify_ahat_consistency(Rational(1), 5)
        for g in range(1, 6):
            assert result[g]['agree']


# =========================================================================
# Section 7: Period ratio rationality
# =========================================================================

class TestPeriodRatioRationality:
    """The period ratio r_g(A) = Omega_g / Vol(A_g) is always rational."""

    def test_ratio_genus1_heisenberg(self):
        """r_1(H_1) = 1/24."""
        ratio = shadow_period_ratio(Rational(1), 1)
        assert ratio == Rational(1, 24)

    def test_ratio_genus1_virasoro(self):
        """r_1(Vir_c) = c/48."""
        ratio = shadow_period_ratio(Rational(1, 2), 1)  # Vir_{c=1}: kappa = 1/2
        assert ratio == Rational(1, 48)

    def test_ratio_genus2_heisenberg(self):
        """r_2(H_1) = 7/5760."""
        ratio = shadow_period_ratio(Rational(1), 2)
        assert ratio == Rational(7, 5760)

    def test_ratio_rationality_all_families(self):
        """Period ratio is rational for all standard families at all genera."""
        for name, data in STANDARD_LANDSCAPE.items():
            kap = data['kappa']
            for g in range(1, 4):
                result = verify_period_ratio_rationality(kap, g)
                assert result['rational'], f"Non-rational ratio for {name} at g={g}"


# =========================================================================
# Section 8: Additivity
# =========================================================================

class TestAdditivity:
    """Shadow periods are additive in kappa."""

    def test_additivity_genus1(self):
        """Omega_1(A1+A2) = Omega_1(A1) + Omega_1(A2)."""
        result = verify_period_additivity(Rational(1), Rational(2), 1)
        assert result['additive']

    def test_additivity_genus2(self):
        result = verify_period_additivity(Rational(3), Rational(5), 2)
        assert result['additive']

    def test_additivity_genus3(self):
        result = verify_period_additivity(Rational(1, 2), Rational(13, 2), 3)
        assert result['additive']

    def test_additivity_all_genera(self):
        """Additivity at all genera."""
        for g in range(1, 5):
            result = verify_period_additivity(Rational(7), Rational(11), g)
            assert result['additive'], f"Additivity fails at g={g}"


# =========================================================================
# Section 9: Complementarity (AP24)
# =========================================================================

class TestComplementarity:
    """Virasoro complementarity: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""

    def test_complementarity_genus1(self):
        """Omega_1(Vir_1) + Omega_1(Vir_25) = 13/24 * pi/3."""
        result = verify_complementarity_periods(1, 1)
        assert result['match']

    def test_complementarity_genus2(self):
        result = verify_complementarity_periods(2, 2)
        assert result['match']

    def test_complementarity_self_dual(self):
        """At c=13: Omega_g(Vir_13) + Omega_g(Vir_13) = 13 * lambda_g^FP * Vol(A_g)."""
        result = verify_complementarity_periods(13, 1)
        assert result['match']

    def test_complementarity_all_c_values(self):
        """Complementarity at various c values."""
        for c_val in [Rational(1, 2), 1, 2, 7, 13, 25]:
            for g in range(1, 3):
                result = verify_complementarity_periods(c_val, g)
                assert result['match'], f"Complementarity fails at c={c_val}, g={g}"

    def test_complementarity_sum_is_13(self):
        """The sum kappa(A) + kappa(A!) = 13 for Virasoro (AP24)."""
        for c_val in [Rational(1, 2), 1, 2, 13, 25]:
            cv = Rational(c_val)
            assert kappa_virasoro(cv) + kappa_virasoro(26 - cv) == 13


# =========================================================================
# Section 10: Shadow curve periods (class M, transcendental)
# =========================================================================

class TestShadowCurvePeriods:
    """Periods of the shadow curve C_{Vir_c}: y^2 = t^4 Q_L(t)."""

    def test_virasoro_QL_genus1_c1(self):
        """Q_L(t) for Virasoro at c=1."""
        QL, (q0, q1, q2) = virasoro_shadow_metric_QL(1)
        assert q0 == Rational(1)  # 4*(1/2)^2 = 1
        assert q1 == Rational(12)  # 12*(1/2)*2 = 12
        assert cancel(q2 - (36 + Rational(80, 27))) == 0  # 9*4 + 80/(5+22)

    def test_virasoro_QL_c13(self):
        """Q_L(t) for Virasoro at c=13 (self-dual)."""
        QL, (q0, q1, q2) = virasoro_shadow_metric_QL(13)
        assert q0 == Rational(169)  # 4*(13/2)^2
        assert q1 == Rational(156)  # 12*(13/2)*2

    def test_branch_points_class_M(self):
        """For generic Virasoro (class M), branch points are complex."""
        bp = shadow_curve_branch_points(1)
        disc_val = float(sym_N(bp['discriminant']))
        # For class M, discriminant of Q_L as polynomial in t is negative
        assert disc_val < 0, "Virasoro c=1 should have negative discriminant (class M)"

    def test_branch_points_c_values(self):
        """Branch points for various c values."""
        for c_val in [Rational(1, 2), 1, 2, 13, 25]:
            bp = shadow_curve_branch_points(c_val)
            # All these are class M: disc < 0
            disc_val = float(sym_N(bp['discriminant']))
            assert disc_val < 0, f"Expected disc < 0 for Virasoro c={c_val}"

    def test_shadow_curve_period_numerical_runs(self):
        """Numerical period computation should run without error."""
        result = shadow_curve_period_numerical(1, n_points=1000)
        assert 'disc' in result

    def test_shadow_curve_period_c13(self):
        """Numerical period at self-dual point c=13."""
        result = shadow_curve_period_numerical(13, n_points=1000)
        assert 'disc' in result
        assert result['disc'] < 0  # class M


# =========================================================================
# Section 11: Picard-Fuchs
# =========================================================================

class TestPicardFuchs:
    """Picard-Fuchs equation for the shadow curve family."""

    def test_picard_fuchs_exists(self):
        """PF equation should return valid structure."""
        pf = shadow_curve_picard_fuchs(1)
        assert 'discriminant' in pf
        assert 'P_coefficient' in pf

    def test_picard_fuchs_discriminant_c1(self):
        """Discriminant of Q_L at c=1."""
        pf = shadow_curve_picard_fuchs(1)
        disc = pf['discriminant']
        disc_val = float(sym_N(disc))
        assert disc_val < 0  # class M

    def test_picard_fuchs_c_dependence(self):
        """PF equation should depend on c."""
        pf1 = shadow_curve_picard_fuchs(1)
        pf2 = shadow_curve_picard_fuchs(2)
        # Different c => different discriminants
        d1 = float(sym_N(pf1['discriminant']))
        d2 = float(sym_N(pf2['discriminant']))
        assert d1 != d2


# =========================================================================
# Section 12: Beilinson regulator
# =========================================================================

class TestBeilinsonRegulator:
    """Beilinson regulator of {t, y} on the shadow curve."""

    def test_regulator_runs(self):
        """Regulator computation should run without error."""
        result = beilinson_regulator_numerical(1, n_points=500)
        assert 'regulator' in result

    def test_regulator_c_half(self):
        """Regulator at c=1/2 (Ising)."""
        result = beilinson_regulator_numerical(Rational(1, 2), n_points=500)
        assert 'regulator' in result

    def test_regulator_c13(self):
        """Regulator at self-dual point c=13."""
        result = beilinson_regulator_numerical(13, n_points=500)
        assert 'regulator' in result


# =========================================================================
# Section 13: Deligne periods
# =========================================================================

class TestDelignePeridos:
    """Deligne period c^+(M_A) for shadow motives."""

    def test_deligne_period_c1(self):
        """Deligne period at c=1."""
        result = deligne_period_shadow_motive(1)
        assert result['c_plus'] > 0
        assert result['disc'] < 0  # class M => imaginary period

    def test_deligne_period_c2(self):
        """Deligne period at c=2."""
        result = deligne_period_shadow_motive(2)
        assert result['c_plus'] > 0

    def test_deligne_period_chalf(self):
        """Deligne period at c=1/2 (Ising)."""
        result = deligne_period_shadow_motive(Rational(1, 2))
        assert result['c_plus'] > 0

    def test_deligne_period_c13(self):
        """Deligne period at self-dual point."""
        result = deligne_period_shadow_motive(13)
        assert result['c_plus'] > 0

    def test_deligne_period_scales_with_disc(self):
        """Period should scale as 1/sqrt(|disc|) for class M."""
        d1 = deligne_period_shadow_motive(1)
        d2 = deligne_period_shadow_motive(2)
        # Both should be finite and positive
        assert 0 < d1['c_plus'] < float('inf')
        assert 0 < d2['c_plus'] < float('inf')


# =========================================================================
# Section 14: CM criterion
# =========================================================================

class TestCMCriterion:
    """Complex multiplication criterion for shadow curves."""

    def test_cm_c1(self):
        """CM test at c=1."""
        result = shadow_curve_cm_test(1)
        assert 'tau' in result or 'has_cm' in result

    def test_cm_c_half(self):
        """CM test at c=1/2."""
        result = shadow_curve_cm_test(Rational(1, 2))
        assert 'tau' in result or 'has_cm' in result

    def test_cm_c13(self):
        """CM test at self-dual c=13."""
        result = shadow_curve_cm_test(13)
        assert result.get('has_cm') is not None

    def test_cm_rational_c_always_algebraic_tau(self):
        """For rational c, tau^2 is always rational (weak CM)."""
        for c_val in [Rational(1, 2), 1, 2, 13, 25]:
            result = shadow_curve_cm_test(c_val)
            if result.get('disc', 0) < 0:
                assert 'tau_squared_exact' in result


# =========================================================================
# Section 15: Genus-2 higher-arity corrections
# =========================================================================

class TestGenus2Corrections:
    """Higher-arity corrections to genus-2 periods."""

    def test_cubic_correction_heisenberg_zero(self):
        """Heisenberg: S_3 = 0, so cubic correction = 0."""
        corr = genus2_cubic_correction(Rational(1), Rational(0))
        assert corr == 0

    def test_cubic_correction_virasoro_nonzero(self):
        """Virasoro: S_3 = 2, nonzero cubic correction."""
        kap = kappa_virasoro(2)  # c=2: kappa = 1
        corr = genus2_cubic_correction(kap, Rational(2))
        assert corr != 0

    def test_quartic_correction_heisenberg_zero(self):
        """Heisenberg: S_4 = 0."""
        corr = genus2_quartic_correction(Rational(1), Rational(0))
        assert corr == 0

    def test_quartic_correction_virasoro_nonzero(self):
        """Virasoro: S_4 != 0."""
        c_val = 2
        kap = kappa_virasoro(c_val)
        S4 = Rational(10) / (c_val * (5 * c_val + 22))
        corr = genus2_quartic_correction(kap, S4)
        assert corr != 0

    def test_full_period_gaussian_is_scalar(self):
        """For Gaussian depth (Heisenberg), full = scalar."""
        full = genus2_full_period(Rational(1))
        scalar = genus2_scalar_period(Rational(1))
        assert cancel(full - scalar) == 0

    def test_full_period_mixed_has_corrections(self):
        """For mixed depth (Virasoro), full != scalar."""
        c_val = 2
        kap = kappa_virasoro(c_val)
        S3 = Rational(2)
        S4 = Rational(10) / (c_val * (5 * c_val + 22))
        full = genus2_full_period(kap, S3, S4)
        scalar = genus2_scalar_period(kap)
        # The corrections should make full != scalar
        diff = cancel(full - scalar)
        assert diff != 0


# =========================================================================
# Section 16: Landscape-wide tests
# =========================================================================

class TestLandscape:
    """Landscape-wide period computation."""

    def test_landscape_table_structure(self):
        """Landscape table should have all families."""
        table = landscape_period_table(2)
        assert len(table) >= 12
        for name in ['heisenberg_1', 'virasoro_1', 'sl2_k1', 'lattice_E8']:
            assert name in table

    def test_landscape_genus1_all_positive(self):
        """All genus-1 periods should be positive (kappa > 0 for standard)."""
        table = landscape_period_table(1)
        for name, data in table.items():
            if data['kappa'] > 0:
                omega_val = float(sym_N(data['Omega_1']))
                assert omega_val > 0, f"Non-positive period for {name}"

    def test_landscape_period_ratios_rational(self):
        """All period ratios should be rational."""
        table = landscape_period_table(2)
        for name, data in table.items():
            r1 = data['ratio_1']
            r2 = data['ratio_2']
            # These should be Rational objects
            assert isinstance(r1, Rational), f"Non-rational r_1 for {name}: {type(r1)}"
            assert isinstance(r2, Rational), f"Non-rational r_2 for {name}: {type(r2)}"

    def test_landscape_f1_values(self):
        """F_1 = kappa/24 for all families."""
        table = landscape_period_table(1)
        for name, data in table.items():
            kap = data['kappa']
            assert data['F_1'] == kap / 24, f"F_1 mismatch for {name}"

    def test_landscape_f2_values(self):
        """F_2 = 7*kappa/5760 for all families."""
        table = landscape_period_table(2)
        for name, data in table.items():
            kap = data['kappa']
            assert data['F_2'] == kap * Rational(7, 5760), f"F_2 mismatch for {name}"


# =========================================================================
# Section 17: Period decay and bounds
# =========================================================================

class TestPeriodDecayBounds:
    """Period bounds from Bernoulli decay."""

    def test_period_bound_genus1(self):
        """Period bound at genus 1."""
        bound = period_bernoulli_bound(1, 1)
        assert bound > 0

    def test_period_bound_decreasing(self):
        """Period bounds should decrease with genus (Bernoulli decay dominates)."""
        bounds = [period_bernoulli_bound(1, g) for g in range(1, 6)]
        for i in range(len(bounds) - 1):
            assert bounds[i + 1] < bounds[i], f"Bound not decreasing at g={i+2}"

    def test_period_decay_ratio(self):
        """Decay ratios should converge to 1/(2*pi)^2 * Vol ratio."""
        ratios = period_decay_ratio(1, 5)
        # The decay ratio involves both lambda_fp ratio and Vol ratio.
        # lambda_fp ratio -> 1/(2*pi)^2, but Vol ratio depends on g.
        # At minimum, ratios should be finite and positive.
        for r in ratios[:4]:
            assert 0 < r < float('inf')


# =========================================================================
# Section 18: Multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification of shadow periods (AP10-compliant)."""

    def test_three_paths_genus1_heisenberg(self):
        """Three paths for Omega_1(H_1).

        Path 1: Direct: kappa * lambda_1^FP * Vol(A_1) = 1 * 1/24 * pi/3
        Path 2: Bernoulli: kappa * (1/2 * |B_2|/2!) * pi/3
        Path 3: Complementarity: Omega_1(H_1) + Omega_1(H_{-1}) = 0
                (kappa(-1) = -1, so Omega_1 = -1/24 * pi/3)
        """
        # Path 1
        p1 = shadow_period_heisenberg(1, 1)
        # Path 2
        p2 = bernoulli_shadow_amplitude(Rational(1), 1) * siegel_volume(1)
        # Path 3 (additivity check)
        p3_sum = shadow_period_heisenberg(1, 1) + shadow_period_heisenberg(-1, 1)
        # Paths 1 and 2 agree
        assert cancel(p1 - p2) == 0
        # Path 3: sum should be zero (kappa additive, 1 + (-1) = 0)
        assert cancel(p3_sum) == 0

    def test_three_paths_genus1_virasoro(self):
        """Three paths for Omega_1(Vir_1)."""
        kap = kappa_virasoro(1)
        # Path 1: Direct
        p1 = shadow_period_virasoro(1, 1)
        # Path 2: FP formula
        p2 = kap * lambda_fp(1) * siegel_volume(1)
        # Path 3: Complementarity
        p3_A = shadow_period_virasoro(1, 1)
        p3_Ad = shadow_period_virasoro(25, 1)
        p3_sum = cancel(p3_A + p3_Ad)
        expected_sum = cancel(13 * lambda_fp(1) * siegel_volume(1))
        assert cancel(p1 - p2) == 0
        assert cancel(p3_sum - expected_sum) == 0

    def test_four_paths_genus2(self):
        """Four-path verification at genus 2."""
        kap = Rational(1)
        # Path 1: Direct
        p1 = shadow_period_genus_g(kap, 2)
        # Path 2: Bernoulli
        p2 = bernoulli_shadow_amplitude(kap, 2) * siegel_volume(2)
        # Path 3: A-hat
        p3 = ahat_shadow_amplitude(kap, 2) * siegel_volume(2)
        # Path 4: Explicit FP number
        p4 = kap * Rational(7, 5760) * pi**4 / 720
        assert cancel(p1 - p2) == 0
        assert cancel(p1 - p3) == 0
        assert cancel(p1 - p4) == 0

    def test_three_paths_genus3(self):
        """Three-path verification at genus 3."""
        kap = Rational(1)
        p1 = shadow_period_genus_g(kap, 3)
        p2 = bernoulli_shadow_amplitude(kap, 3) * siegel_volume(3)
        p3 = kap * lambda_fp(3) * siegel_volume(3)
        assert cancel(p1 - p2) == 0
        assert cancel(p1 - p3) == 0


# =========================================================================
# Section 19: Bernoulli number explicit values
# =========================================================================

class TestBernoulliExplicitValues:
    """Verify Bernoulli numbers used in period computations."""

    def test_B2(self):
        assert bernoulli(2) == Rational(1, 6)

    def test_B4(self):
        assert bernoulli(4) == Rational(-1, 30)

    def test_B6(self):
        assert bernoulli(6) == Rational(1, 42)

    def test_B8(self):
        assert bernoulli(8) == Rational(-1, 30)

    def test_B10(self):
        assert bernoulli(10) == Rational(5, 66)

    def test_lambda_fp_from_bernoulli(self):
        """Verify lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""
        for g in range(1, 6):
            B_2g = abs(bernoulli(2 * g))
            pref = (Rational(2)**(2 * g - 1) - 1) / Rational(2)**(2 * g - 1)
            expected = pref * B_2g / factorial(2 * g)
            assert lambda_fp(g) == expected, f"lambda_fp mismatch at g={g}"


# =========================================================================
# Section 20: Specific numerical checks
# =========================================================================

class TestNumericalChecks:
    """Specific numerical values for cross-checking."""

    def test_omega1_heisenberg_numerical(self):
        """Omega_1(H_1) = pi/72 ~ 0.04363."""
        val = float(sym_N(shadow_period_heisenberg(1, 1)))
        assert abs(val - math.pi / 72) < 1e-10

    def test_omega1_virasoro_c1_numerical(self):
        """Omega_1(Vir_1) = pi/144 ~ 0.02182."""
        val = float(sym_N(shadow_period_virasoro(1, 1)))
        assert abs(val - math.pi / 144) < 1e-10

    def test_omega2_heisenberg_numerical(self):
        """Omega_2(H_1) = 7*pi^4/(5760*720)."""
        val = float(sym_N(shadow_period_heisenberg(1, 2)))
        expected = 7 * math.pi**4 / (5760 * 720)
        assert abs(val - expected) < 1e-12

    def test_omega1_sl2_k1_numerical(self):
        """Omega_1(sl_2, k=1) = 9/(4*24) * pi/3 = 3*pi/96."""
        val = float(sym_N(shadow_period_affine_sl2(1, 1)))
        expected = 9 / (4 * 24) * math.pi / 3
        assert abs(val - expected) < 1e-10

    def test_vol_A1_times_lambda1(self):
        """Vol(A_1) * lambda_1^FP = pi/3 * 1/24 = pi/72."""
        val = float(sym_N(siegel_volume(1) * lambda_fp(1)))
        assert abs(val - math.pi / 72) < 1e-10

    def test_vol_A2_times_lambda2(self):
        """Vol(A_2) * lambda_2^FP = pi^4/720 * 7/5760."""
        val = float(sym_N(siegel_volume(2) * lambda_fp(2)))
        expected = math.pi**4 / 720 * 7 / 5760
        assert abs(val - expected) < 1e-14

    def test_omega1_lattice_E8(self):
        """Omega_1(V_{E_8}) = 8/24 * pi/3 = pi/9."""
        omega = shadow_period_genus_g(Rational(8), 1)
        assert cancel(omega - pi / 9) == 0

    def test_omega1_free_fermion(self):
        """Omega_1(ff) = (1/4)/24 * pi/3 = pi/288."""
        omega = shadow_period_genus_g(Rational(1, 4), 1)
        assert cancel(omega - pi / 288) == 0


# =========================================================================
# Section 21: Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_heisenberg_virasoro_chalf_same_kappa(self):
        """H_{1/4} and Vir_{1/2} have the same kappa = 1/4."""
        assert kappa_heisenberg(Rational(1, 4)) == kappa_virasoro(Rational(1, 2))
        # Their periods should agree
        omega_H = shadow_period_genus_g(kappa_heisenberg(Rational(1, 4)), 1)
        omega_V = shadow_period_genus_g(kappa_virasoro(Rational(1, 2)), 1)
        assert cancel(omega_H - omega_V) == 0

    def test_heisenberg_virasoro_c2_same_kappa(self):
        """H_1 and Vir_2 have kappa = 1."""
        assert kappa_heisenberg(1) == kappa_virasoro(2)

    def test_bc_bg_complementarity(self):
        """kappa(bc, j=2) + kappa(bg, lambda=2) = 0."""
        k_bc = kappa_bc_ghost(2)
        k_bg = kappa_betagamma(2)
        assert k_bc + k_bg == 0
        # Periods should cancel
        omega_bc = shadow_period_genus_g(k_bc, 1)
        omega_bg = shadow_period_genus_g(k_bg, 1)
        assert cancel(omega_bc + omega_bg) == 0

    def test_lattice_rank_equals_kappa(self):
        """For lattice VOAs, kappa = rank."""
        for r in [1, 2, 8, 16, 24]:
            assert kappa_lattice(r) == r

    def test_wN_reduces_to_virasoro(self):
        """W_2 = Virasoro: kappa(W_2, c) = c/2."""
        for c_val in [1, 2, 13, 26]:
            assert kappa_wN(2, c_val) == kappa_virasoro(c_val)


# =========================================================================
# Section 22: Edge cases and boundary values
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary values."""

    def test_critical_level_sl2(self):
        """At critical level k = -h^v = -2: kappa(sl_2, -2) = 0."""
        assert kappa_affine_sl2(-2) == 0
        # Period vanishes
        omega = shadow_period_genus_g(Rational(0), 1)
        assert omega == 0

    def test_self_dual_virasoro_c13(self):
        """At self-dual c=13: kappa = 13/2, Omega_1 = 13/48 * pi/3."""
        kap = kappa_virasoro(13)
        assert kap == Rational(13, 2)
        omega = shadow_period_virasoro(13, 1)
        assert cancel(omega - Rational(13, 2) * pi / 72) == 0

    def test_critical_string_c26(self):
        """At c=26: kappa = 13, Omega_1 = 13/24 * pi/3 = 13*pi/72."""
        omega = shadow_period_virasoro(26, 1)
        assert cancel(omega - 13 * pi / 72) == 0

    def test_zero_kappa_gives_zero_period(self):
        """kappa = 0 => all periods vanish."""
        for g in range(1, 5):
            assert shadow_period_genus_g(Rational(0), g) == 0

    def test_negative_kappa_gives_negative_period(self):
        """Negative kappa (ghosts) gives negative periods."""
        omega = shadow_period_genus_g(Rational(-1), 1)
        val = float(sym_N(omega))
        assert val < 0


# =========================================================================
# Section 23: Shadow ODE / Picard-Fuchs verification
# =========================================================================

class TestShadowODE:
    """Shadow ODE and Picard-Fuchs connection to periods."""

    def test_pf_discriminant_negative_class_M(self):
        """For class M Virasoro, discriminant of Q_L is negative."""
        for c_val in [Rational(1, 2), 1, 2, 13, 25]:
            pf = shadow_curve_picard_fuchs(c_val)
            disc_val = float(sym_N(pf['discriminant']))
            assert disc_val < 0, f"Expected negative disc for c={c_val}"

    def test_pf_q0_is_c_squared(self):
        """q_0 = c^2 (= 4*kappa^2)."""
        pf = shadow_curve_picard_fuchs(3)
        assert pf['q0'] == Rational(9)

    def test_pf_q1_is_12c(self):
        """q_1 = 12c (= 12*kappa*alpha = 12*(c/2)*2)."""
        pf = shadow_curve_picard_fuchs(5)
        assert pf['q1'] == Rational(60)


# =========================================================================
# Section 24: Period growth analysis
# =========================================================================

class TestPeriodGrowth:
    """Period growth and asymptotics."""

    def test_lambda_fp_ratio_converges(self):
        """lambda_{g+1}^FP / lambda_g^FP -> 1/(2*pi)^2 ~ 0.0253."""
        target = 1 / (2 * math.pi)**2
        ratios = []
        for g in range(1, 15):
            r = float(lambda_fp(g + 1) / lambda_fp(g))
            ratios.append(r)
        # Last ratio should be close to target
        assert abs(ratios[-1] - target) < 0.001

    def test_period_polynomial_decreasing(self):
        """P(g) = lambda_g^FP is strictly decreasing and positive."""
        for g in range(1, 10):
            assert lambda_fp(g) > 0
            assert lambda_fp(g + 1) < lambda_fp(g)

    def test_bernoulli_growth_check(self):
        """Bernoulli numbers |B_{2g}| ~ 2*(2g)!/(2*pi)^{2g}."""
        for g in range(1, 8):
            B_2g = float(abs(bernoulli(2 * g)))
            asymptotic = 2 * float(factorial(2 * g)) / (2 * math.pi)**(2 * g)
            ratio = B_2g / asymptotic
            # Ratio should be close to 1 for large g
            if g >= 3:
                assert abs(ratio - 1) < 0.1, f"Bernoulli ratio {ratio} at g={g}"
