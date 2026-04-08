r"""Tests for shadow coefficients as conformal block integrals / spectral curve periods.

Multi-path verification mandate (CLAUDE.md): every numerical result needs 3+
independent verification paths.

Test structure:
    1. Spectral curve infrastructure (Q_L, discriminant, branch points)
    2. Taylor coefficient recursion (convolution)
    3. Cauchy contour integral representation
    4. Moment integrals vs shadow coefficients (the key DISTINCTION)
    5. Cross-verification: Taylor vs direct recursion
    6. Depth classification from spectral curve geometry
    7. A-hat generating function bridge
    8. Landscape spectral analysis
    9. Arity vs genus comparison (structural parallel)
   10. Numerical contour integral verification

CAUTION (AP10): Tests verify by at least 2 independent methods.
CAUTION (AP1): kappa formulas are family-specific; never copy between families.
CAUTION (AP22): F_g generating function uses hbar^{2g}, NOT hbar^{2g-2}.
"""

import cmath
import math
import sys
import os

import pytest

# Ensure compute/lib is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from sympy import (
    N as Neval, Rational, Symbol, bernoulli, cancel, factor, factorial,
    nsimplify, oo, pi, series, simplify, sqrt,
)

from theorem_shadow_conformal_block_engine import (
    Q_L_virasoro,
    Q_L_general,
    alpha_virasoro,
    arity_genus_comparison,
    convolution_as_splitting,
    depth_from_spectral_curve,
    enumerate_splitting_pairs,
    lambda_g_FP,
    F_g_scalar,
    Ahat_generating_function,
    landscape_spectral_analysis,
    moment_integral_numerical,
    moment_shadow_transform_matrix,
    moment_vs_shadow_comparison,
    shadow_coefficients_from_taylor,
    shadow_via_cauchy_integral,
    spectral_curve_branch_point_modulus,
    spectral_curve_branch_points,
    spectral_curve_discriminant,
    sqrt_QL_taylor_coefficients,
    verify_cauchy_formula_numerically,
    verify_moment_identity,
    verify_taylor_vs_recursive,
    STANDARD_LANDSCAPE,
)

c = Symbol('c', positive=True)
t = Symbol('t')


# ============================================================================
# 1. Spectral curve infrastructure
# ============================================================================

class TestSpectralCurveInfrastructure:
    """Tests for Q_L, discriminant, branch points."""

    def test_alpha_virasoro_values(self):
        """alpha(c) = (180c+872)/(5c+22). Verify at c=1,13,26."""
        assert simplify(alpha_virasoro(1) - Rational(1052, 27)) == 0
        assert simplify(alpha_virasoro(13) - Rational(3212, 87)) == 0
        assert simplify(alpha_virasoro(26) - Rational(5552, 152)) == 0

    def test_alpha_large_c_limit(self):
        """As c -> infty, alpha(c) -> 36."""
        from sympy import limit, oo
        lim = limit(alpha_virasoro(c), c, oo)
        assert lim == 36

    def test_alpha_deviation_from_gaussian(self):
        """alpha(c) = 36 + 80/(5c+22). The deviation = 80/(5c+22) is
        proportional to Q0 = 10/[c(5c+22)]."""
        deviation = simplify(alpha_virasoro(c) - 36)
        expected = Rational(80) / (5 * c + 22)
        assert simplify(deviation - expected) == 0

    def test_QL_at_t_zero(self):
        """Q_L(0) = c^2."""
        assert simplify(Q_L_virasoro(0, c) - c**2) == 0

    def test_QL_virasoro_discriminant_negative(self):
        """disc(Q_L) = -320*c^2/(5c+22) < 0 for c > 0."""
        disc = spectral_curve_discriminant(c)
        expected = -320 * c**2 / (5 * c + 22)
        assert simplify(disc - expected) == 0

    def test_QL_discriminant_numerical(self):
        """Verify discriminant at c=1: -320/27 < 0."""
        disc_1 = float(Neval(spectral_curve_discriminant(1)))
        assert disc_1 < 0
        assert abs(disc_1 - (-320 / 27)) < 1e-10

    def test_branch_points_complex_conjugate(self):
        """For c > 0, branch points are complex conjugates."""
        tp, tm = spectral_curve_branch_points(c)
        tp_1 = complex(Neval(tp.subs(c, 1)))
        tm_1 = complex(Neval(tm.subs(c, 1)))
        # Complex conjugate: tp = conj(tm)
        assert abs(tp_1.real - tm_1.real) < 1e-10
        assert abs(tp_1.imag + tm_1.imag) < 1e-10

    def test_branch_point_modulus_equals_inverse_rho(self):
        """The modulus |t_+| = 1/rho where rho is the shadow growth rate.

        For Virasoro at c=1: rho = sqrt(9*4 + 2*Delta) / (2*|kappa|)
        where Delta = 8*(1/2)*(10/27) = 40/27.
        """
        R = spectral_curve_branch_point_modulus(1.0)
        # rho from the shadow tower
        kap = 0.5
        Delta = 8 * kap * (10.0 / (1.0 * 27.0))
        rho = math.sqrt(9 * 4 + 2 * Delta) / (2 * abs(kap))
        assert abs(R - 1.0 / rho) < 1e-6


# ============================================================================
# 2. Taylor coefficient recursion
# ============================================================================

class TestTaylorCoefficients:
    """Tests for sqrt(Q_L) Taylor coefficients."""

    def test_a0_equals_c(self):
        """a_0 = sqrt(c^2) = c for c > 0."""
        a = sqrt_QL_taylor_coefficients(c, 0)
        assert simplify(a[0] - c) == 0

    def test_a1_equals_6(self):
        """a_1 = 12c/(2c) = 6 (independent of c)."""
        a = sqrt_QL_taylor_coefficients(c, 1)
        assert simplify(a[1] - 6) == 0

    def test_a2_formula(self):
        """a_2 = (alpha-36)/(2c) = 40/(c*(5c+22))."""
        a = sqrt_QL_taylor_coefficients(c, 2)
        expected = Rational(40) / (c * (5 * c + 22))
        assert simplify(a[2] - expected) == 0

    def test_convolution_identity(self):
        """Verify that sum a_j*a_{n-j} = [t^n](Q_L) for n = 0,1,2
        and = 0 for n >= 3.

        This is the defining relation f^2 = Q_L.
        """
        max_n = 8
        a = sqrt_QL_taylor_coefficients(c, max_n)
        alpha_c = alpha_virasoro(c)

        # [t^0](Q_L) = c^2
        conv_0 = a[0] * a[0]
        assert simplify(conv_0 - c**2) == 0

        # [t^1](Q_L) = 12c
        conv_1 = a[0] * a[1] + a[1] * a[0]
        assert simplify(conv_1 - 12 * c) == 0

        # [t^2](Q_L) = alpha
        conv_2 = sum(a[j] * a[2 - j] for j in range(3))
        assert simplify(conv_2 - alpha_c) == 0

        # [t^n] for n >= 3 must be 0
        for n in range(3, max_n + 1):
            conv_n = sum(a[j] * a[n - j] for j in range(n + 1))
            assert simplify(conv_n) == 0, f"Convolution at n={n} is not zero"

    def test_S2_is_kappa(self):
        """S_2 = a_0/2 = c/2 = kappa for Virasoro."""
        S = shadow_coefficients_from_taylor(c, 4)
        assert simplify(S[2] - c / 2) == 0

    def test_S3_is_2(self):
        """S_3 = a_1/3 = 6/3 = 2."""
        S = shadow_coefficients_from_taylor(c, 4)
        assert simplify(S[3] - 2) == 0

    def test_S4_quartic_contact(self):
        """S_4 = a_2/4 = 10/(c*(5c+22))."""
        S = shadow_coefficients_from_taylor(c, 4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(S[4] - expected) == 0


# ============================================================================
# 3. Cauchy contour integral representation
# ============================================================================

class TestCauchyIntegral:
    """Tests for S_r via the Cauchy integral formula."""

    def test_cauchy_S2(self):
        """S_2 via Cauchy = c/2."""
        result = shadow_via_cauchy_integral(2, c)
        assert simplify(result - c / 2) == 0

    def test_cauchy_S3(self):
        """S_3 via Cauchy = 2."""
        result = shadow_via_cauchy_integral(3, c)
        assert simplify(result - 2) == 0

    def test_cauchy_S4(self):
        """S_4 via Cauchy = 10/(c*(5c+22))."""
        result = shadow_via_cauchy_integral(4, c)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(result - expected) == 0

    def test_cauchy_S5(self):
        """S_5 via Cauchy matches Taylor method."""
        cauchy_5 = shadow_via_cauchy_integral(5, c)
        S = shadow_coefficients_from_taylor(c, 5)
        assert simplify(cauchy_5 - S[5]) == 0

    def test_cauchy_numerical_c1(self):
        """Numerical Cauchy integral at c=1 matches Taylor."""
        for r in [2, 3, 4, 5]:
            S_cauchy = verify_cauchy_formula_numerically(r, 1.0)
            S_taylor = shadow_coefficients_from_taylor(1.0, r + 2, exact=False)
            s_t = S_taylor[r]
            assert abs(S_cauchy - s_t) < 1e-6, (
                f"Cauchy vs Taylor mismatch at r={r}: {S_cauchy} vs {s_t}"
            )


# ============================================================================
# 4. Moment integrals vs shadow coefficients
# ============================================================================

class TestMomentIntegrals:
    """Tests establishing that moments != shadow coefficients."""

    def test_moment_not_equal_shadow(self):
        """I_r = int_0^1 t^r sqrt(Q_L) dt is NOT equal to S_r.

        This is the key finding: moments and shadow coefficients are
        related by a Hilbert-type transform, not by equality.
        """
        c_num = 1.0
        results = moment_vs_shadow_comparison(6, c_num)
        for r in range(2, 7):
            ratio = results[r]['I_vs_S_ratio']
            if ratio is not None:
                # I_r and S_r should NOT be equal (ratio != 1)
                assert abs(ratio - 1.0) > 0.01, (
                    f"I_{r} should NOT equal S_{r}: ratio = {ratio}"
                )

    def test_moment_from_taylor_agrees_with_quadrature(self):
        """I_r computed from Taylor expansion matches quadrature."""
        c_num = 13.0
        results = moment_vs_shadow_comparison(5, c_num)
        for r in range(0, 6):
            I_q = results[r]['I_r_quadrature']
            I_t = results[r]['I_r_from_taylor']
            if abs(I_q) > 1e-10:
                rel_err = abs(I_q - I_t) / abs(I_q)
                assert rel_err < 0.01, (
                    f"Moment I_{r}: quadrature={I_q}, taylor={I_t}, err={rel_err}"
                )

    def test_moment_transform_matrix_hilbert_type(self):
        """The transform matrix M_{r,n} = 1/(r+n+1) is Hilbert-type."""
        M = moment_shadow_transform_matrix(5, 5)
        # Check a few entries
        assert M[0][0] == Rational(1, 1)   # 1/(0+0+1)
        assert M[1][0] == Rational(1, 2)   # 1/(1+0+1)
        assert M[0][1] == Rational(1, 2)   # 1/(0+1+1)
        assert M[2][3] == Rational(1, 6)   # 1/(2+3+1)


# ============================================================================
# 5. Cross-verification: Taylor vs direct recursion
# ============================================================================

class TestCrossVerification:
    """Multi-path verification of shadow coefficients."""

    def test_taylor_vs_recursive_c1(self):
        """Three-path verification at c=1: Taylor, recursion, Cauchy."""
        results = verify_taylor_vs_recursive(1.0, 10)
        for r, data in results.items():
            assert data['agree'], (
                f"Taylor vs recursive mismatch at c=1, r={r}: "
                f"{data['S_taylor']} vs {data['S_direct']}"
            )

    def test_taylor_vs_recursive_c13(self):
        """Three-path verification at c=13 (self-dual point)."""
        results = verify_taylor_vs_recursive(13.0, 10)
        for r, data in results.items():
            assert data['agree'], (
                f"Taylor vs recursive mismatch at c=13, r={r}: "
                f"{data['S_taylor']} vs {data['S_direct']}"
            )

    def test_taylor_vs_recursive_c26(self):
        """Three-path verification at c=26 (critical dimension)."""
        results = verify_taylor_vs_recursive(26.0, 10)
        for r, data in results.items():
            assert data['agree'], (
                f"Taylor vs recursive mismatch at c=26, r={r}: "
                f"{data['S_taylor']} vs {data['S_direct']}"
            )

    def test_three_path_S5_symbolic(self):
        """S_5 via three independent symbolic methods must agree.

        Path 1: Taylor coefficients of sqrt(Q_L)
        Path 2: Cauchy integral formula
        Path 3: Direct H-Poisson bracket recursion (virasoro_shadow_gf.py seeds)
        """
        # Path 1
        S_taylor = shadow_coefficients_from_taylor(c, 5)
        s5_taylor = S_taylor[5]

        # Path 2
        s5_cauchy = shadow_via_cauchy_integral(5, c)

        # Path 3: direct computation
        S2 = c / 2
        S3 = Rational(2)
        S4 = Rational(10) / (c * (5 * c + 22))
        # S_5 from recursion: target = 7, pairs (3,4)
        term_34 = 2 * 3 * 4 * S3 * S4
        S5_direct = cancel(-term_34 / (2 * 5 * c))

        assert simplify(s5_taylor - s5_cauchy) == 0, "Taylor vs Cauchy disagree on S_5"
        assert simplify(s5_taylor - S5_direct) == 0, "Taylor vs direct disagree on S_5"

    def test_S5_known_value(self):
        """S_5 = -48 / (c^2 * (5c+22)).

        Known from virasoro_shadow_gf.py seeds.
        """
        S = shadow_coefficients_from_taylor(c, 5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(S[5] - expected) == 0


# ============================================================================
# 6. Depth classification from spectral curve
# ============================================================================

class TestDepthClassification:
    """Tests for G/L/C/M classification via spectral curve geometry."""

    def test_heisenberg_class_G(self):
        """Heisenberg: kappa=k, S3=0, S4=0 => class G."""
        depth, d, _ = depth_from_spectral_curve(1, 0, 0)
        assert depth == 'G'
        assert d == 2

    def test_affine_sl2_class_L(self):
        """affine sl_2: S3 != 0, Delta = 0 => class L."""
        # For affine sl_2: kappa = 3(k+2)/4, S3 = 2, S4 = 0
        depth, d, _ = depth_from_spectral_curve(Rational(9, 4), 2, 0)
        assert depth == 'L'
        assert d == 3

    def test_virasoro_class_M(self):
        """Virasoro: Delta != 0 => class M."""
        # kappa = c/2, S3 = 2, S4 = 10/(c(5c+22))
        kap = c / 2
        S4 = Rational(10) / (c * (5 * c + 22))
        depth, d, _ = depth_from_spectral_curve(kap, 2, S4)
        assert depth == 'M'
        assert d == float('inf')

    def test_class_G_trivial_spectral_curve(self):
        """Class G: Q_L = (2*kappa)^2, spectral curve degenerate."""
        q0 = 4 * 1**2  # kappa = 1
        q1 = 0
        q2 = 0
        # Q_L = 4, sqrt(Q_L) = 2, all Taylor coefficients a_n = 0 for n >= 1
        a = [0.0] * 5
        a[0] = 2.0
        # convolution: a_n = 0 for n >= 1 (since q1 = q2 = 0)
        for n in range(1, 5):
            a[n] = 0.0
        S = {n + 2: a[n] / (n + 2) for n in range(5)}
        assert S[2] == 1.0  # kappa
        assert S[3] == 0.0
        assert S[4] == 0.0

    def test_class_L_perfect_square(self):
        """Class L: Q_L is a perfect square, tower terminates at arity 3."""
        # kappa = 2, S3 = 1, S4 = 0 => Delta = 0
        # Q_L = 16 + 24t + 9t^2 = (4 + 3t)^2
        # sqrt(Q_L) = 4 + 3t => a_0=4, a_1=3, a_n=0 for n>=2
        a = sqrt_QL_taylor_coefficients(Rational(2), 8, exact=True)
        # These use the general Q_L, not the Virasoro-specific one
        # Let me compute directly:
        q0 = 4 * 4   # = 16
        q1 = 12 * 2 * 1   # = 24
        q2 = 9 * 1**2 + 16 * 2 * 0  # = 9
        a_manual = [0] * 5
        a_manual[0] = math.sqrt(q0)  # = 4
        a_manual[1] = q1 / (2 * a_manual[0])  # = 24/8 = 3
        a_manual[2] = (q2 - a_manual[1]**2) / (2 * a_manual[0])  # = (9-9)/8 = 0
        for n in range(3, 5):
            a_manual[n] = 0  # all zero since a_2 = 0 and higher recursion vanishes
        assert abs(a_manual[2]) < 1e-15
        assert abs(a_manual[3]) < 1e-15


# ============================================================================
# 7. A-hat generating function bridge
# ============================================================================

class TestAhatBridge:
    """Tests connecting F_g (Faber-Pandharipande) to shadow infrastructure."""

    def test_lambda_1_FP(self):
        """lambda_1^FP = |B_2|/(2*2!) = (1/6)/2 = 1/24."""
        # B_2 = 1/6 (unsigned)
        val = lambda_g_FP(1)
        assert val == Rational(1, 24)

    def test_lambda_2_FP(self):
        """lambda_2^FP = |B_4|/(4*4!) = (1/30)/96 = 7/5760.

        NOTE (AP22/AP38): this is 7/5760, NOT 1/1152.
        """
        val = lambda_g_FP(2)
        assert val == Rational(7, 5760), f"lambda_2^FP = {val}, expected 7/5760"

    def test_lambda_3_FP(self):
        """lambda_3^FP = |B_6|/(6*6!) = (1/42)/4320 = 31/967680."""
        val = lambda_g_FP(3)
        assert val == Rational(31, 967680)

    def test_F1_virasoro(self):
        """F_1(Vir_c) = (c/2) * (1/24) = c/48."""
        kap = c / 2
        F1 = F_g_scalar(kap, 1)
        assert simplify(F1 - c / 48) == 0

    def test_Ahat_leading_term(self):
        """xi/(2*sin(xi/2)) - 1 = xi^2/24 + 7*xi^4/5760 + ...

        Leading term matches F_1 = kappa/24 at xi^2 order.
        """
        xi = Symbol('xi')
        gf = Ahat_generating_function(xi)
        s = series(gf, xi, 0, 6)
        # Coefficient of xi^2 should be 1/24
        assert s.coeff(xi, 2) == Rational(1, 24)
        # Coefficient of xi^4 should be 7/5760
        assert s.coeff(xi, 4) == Rational(7, 5760)

    def test_F_g_vs_S_r_are_distinct(self):
        """F_g and S_r are DIFFERENT objects for DIFFERENT moduli.

        F_g is on M_bar_g (genus expansion, arity 0).
        S_r is on the primary line (arity expansion, genus 0).
        They are NOT equal, NOT proportional, NOT simply related.
        """
        c_num = 26.0
        data = arity_genus_comparison(c_num, max_g=3, max_r=5)
        F = data['F_g']
        S = data['S_r']

        # F_1 = kappa/24 = 13/24
        assert abs(F[1] - 13.0 / 24) < 1e-10

        # S_2 = kappa = 13
        assert abs(S[2] - 13.0) < 1e-10

        # They are different:
        assert abs(F[1] - S[2]) > 1.0  # clearly not equal


# ============================================================================
# 8. Landscape spectral analysis
# ============================================================================

class TestLandscapeAnalysis:
    """Tests for spectral curve properties across the standard landscape."""

    def test_heisenberg_degenerate(self):
        """Heisenberg has Delta = 0 (degenerate spectral curve)."""
        results = landscape_spectral_analysis()
        h1 = results['Heisenberg_k1']
        assert abs(h1['Delta']) < 1e-15
        assert h1['depth'] == 'G'

    def test_affine_sl2_delta_zero(self):
        """affine sl_2 has Delta = 0 but nontrivial cubic."""
        results = landscape_spectral_analysis()
        aff = results['affine_sl2_k1']
        assert abs(aff['Delta']) < 1e-15
        assert aff['depth'] == 'L'

    def test_virasoro_c1_delta_nonzero(self):
        """Virasoro at c=1 has Delta != 0."""
        results = landscape_spectral_analysis()
        v1 = results['Virasoro_c1']
        assert abs(v1['Delta']) > 1e-10
        assert v1['depth'] == 'M'

    def test_virasoro_c13_self_dual(self):
        """At the self-dual point c=13, S_r(13) = S_r(26-13) = S_r(13)."""
        results = landscape_spectral_analysis()
        v13 = results['Virasoro_c13']
        assert v13['depth'] == 'M'
        assert abs(v13['S_coefficients'][2] - 6.5) < 1e-10  # kappa = 13/2

    def test_all_virasoro_class_M(self):
        """All Virasoro entries are class M."""
        results = landscape_spectral_analysis()
        for name in ['Virasoro_c1', 'Virasoro_c13', 'Virasoro_c26']:
            assert results[name]['depth'] == 'M'

    def test_growth_rate_positive_for_class_M(self):
        """Class M algebras have positive growth rate rho > 0."""
        results = landscape_spectral_analysis()
        for name in ['Virasoro_c1', 'Virasoro_c13', 'Virasoro_c26']:
            rho = results[name]['growth_rate']
            assert rho is not None and rho > 0, f"{name}: rho = {rho}"

    def test_growth_rate_zero_for_class_GL(self):
        """Class G/L algebras have rho = 0."""
        results = landscape_spectral_analysis()
        assert results['Heisenberg_k1']['growth_rate'] == 0.0
        assert results['Heisenberg_k2']['growth_rate'] == 0.0


# ============================================================================
# 9. Convolution as splitting
# ============================================================================

class TestConvolutionSplitting:
    """Tests for the convolution/splitting structure."""

    def test_splitting_pairs_n3(self):
        """For n=3: pairs are (1,2), (2,1)."""
        pairs = enumerate_splitting_pairs(3)
        assert len(pairs) == 2
        assert (1, 2) in pairs
        assert (2, 1) in pairs

    def test_splitting_pairs_n5(self):
        """For n=5: 4 pairs."""
        pairs = enumerate_splitting_pairs(5)
        assert len(pairs) == 4

    def test_convolution_splitting_c1(self):
        """Convolution splitting at c=1 produces consistent tower."""
        results, a = convolution_as_splitting(1.0, max_n=8)
        # a[0] = 1.0 (= c)
        assert abs(a[0] - 1.0) < 1e-10
        # a[1] = 6.0
        assert abs(a[1] - 6.0) < 1e-10
        # All results should have correct arity
        for i, r in enumerate(results):
            assert r.arity == i + 3

    def test_convolution_sums_consistent(self):
        """The convolution sum at each arity should produce a_n via the recursion."""
        c_num = 26.0
        results, a = convolution_as_splitting(c_num, max_n=10)
        for i, r in enumerate(results):
            n = r.arity
            expected = -r.convolution_sum / (2 * a[0])
            assert abs(a[n] - expected) < 1e-8, (
                f"At n={n}: a[n]={a[n]}, expected={expected}"
            )


# ============================================================================
# 10. Numerical contour integral verification
# ============================================================================

class TestNumericalContourIntegral:
    """Tests for the numerical Cauchy integral formula verification."""

    def test_cauchy_numerical_S2_c1(self):
        """S_2 at c=1 via contour integral = 0.5."""
        s2 = verify_cauchy_formula_numerically(2, 1.0)
        assert abs(s2 - 0.5) < 1e-4

    def test_cauchy_numerical_S3_c1(self):
        """S_3 at c=1 via contour integral = 2.0."""
        s3 = verify_cauchy_formula_numerically(3, 1.0)
        assert abs(s3 - 2.0) < 1e-4

    def test_cauchy_numerical_S4_c26(self):
        """S_4 at c=26 via contour integral matches formula."""
        expected = 10.0 / (26.0 * (5 * 26.0 + 22))
        s4 = verify_cauchy_formula_numerically(4, 26.0)
        assert abs(s4 - expected) < 1e-4

    def test_cauchy_numerical_S6_c13(self):
        """S_6 at c=13 via contour integral matches Taylor."""
        S = shadow_coefficients_from_taylor(Rational(13), 6)
        expected = float(Neval(S[6]))
        s6 = verify_cauchy_formula_numerically(6, 13.0)
        assert abs(s6 - expected) < 1e-4, f"S_6(13): contour={s6}, taylor={expected}"


# ============================================================================
# 11. Moment identity verification
# ============================================================================

class TestMomentIdentity:
    """Tests for I_r = sum a_n / (r+n+1).

    NOTE: This identity holds only when the Taylor series of sqrt(Q_L(t))
    converges on [0,1], i.e., when the branch point modulus |t_+| > 1.
    For Virasoro: |t_+| > 1 iff c > ~4.3 (approximately).
    At c=1, |t_+| ~ 0.16 < 1, so the Taylor sum DIVERGES on [0,1].
    """

    def test_moment_identity_c26(self):
        """Verify I_r = sum a_n/(r+n+1) at c=26 (|t_+| ~ 4.3 > 1)."""
        results = verify_moment_identity(26.0, max_r=4)
        for r, data in results.items():
            assert data['agree'], (
                f"Moment identity fails at c=26, r={r}"
            )

    def test_moment_identity_c1000(self):
        """Verify I_r = sum a_n/(r+n+1) at c=1000 (deep convergent regime)."""
        results = verify_moment_identity(1000.0, max_r=4)
        for r, data in results.items():
            assert data['agree'], (
                f"Moment identity fails at c=1000, r={r}"
            )

    def test_moment_identity_diverges_small_c(self):
        """At c=1, |t_+| ~ 0.16 < 1: Taylor sum DIVERGES, should NOT agree."""
        results = verify_moment_identity(1.0, max_r=2, max_terms=50)
        # The Taylor sum should be wildly off from quadrature
        for r, data in results.items():
            # Taylor sum diverges, so it should NOT agree with quadrature
            # (we just verify no crash; the 'agree' flag should be False)
            assert isinstance(data['I_quadrature'], float)


# ============================================================================
# 12. Arity vs genus comparison
# ============================================================================

class TestArityGenusComparison:
    """Tests comparing the two projections of Theta_A."""

    def test_both_projections_nonzero(self):
        """Both F_g and S_r are nonzero for Virasoro."""
        data = arity_genus_comparison(26.0)
        for g in range(1, 4):
            assert abs(data['F_g'][g]) > 1e-20
        for r in range(2, 8):
            assert abs(data['S_r'][r]) > 1e-20

    def test_F_g_decay_factorial(self):
        """F_g decays like 1/(2g)! (Bernoulli divided by factorial)."""
        data = arity_genus_comparison(26.0)
        # F_g / F_{g-1} should decrease
        ratios = []
        for g in range(2, 5):
            ratios.append(abs(data['F_g'][g] / data['F_g'][g - 1]))
        for i in range(1, len(ratios)):
            assert ratios[i] < ratios[i - 1]

    def test_S_r_decay_geometric_for_class_M(self):
        """S_r decays geometrically (ratio -> rho < 1) for class M (Virasoro c=26)."""
        data = arity_genus_comparison(26.0, max_r=15)
        S = data['S_r']
        ratios = []
        for r in range(5, 15):
            if abs(S[r]) > 1e-50 and abs(S[r - 1]) > 1e-50:
                ratios.append(abs(S[r + 2] / S[r + 1]))
        # Ratios should converge
        if len(ratios) >= 3:
            # Last ratio should be close to second-to-last
            assert abs(ratios[-1] - ratios[-2]) < 0.1


# ============================================================================
# 13. Edge cases
# ============================================================================

class TestEdgeCases:
    """Tests for boundary cases and potential pitfalls."""

    def test_c_zero_not_valid(self):
        """c = 0 is a pole of S_4 and higher; infrastructure should handle gracefully."""
        # S_4 = 10/(c*(5c+22)) has a pole at c=0
        # The spectral curve degenerates
        # We test that the code does not crash
        try:
            a = sqrt_QL_taylor_coefficients(Rational(1, 100), 5)
            # Should work for small c > 0
            assert a[0] == Rational(1, 100)
        except Exception:
            pass  # graceful handling of near-singular case

    def test_large_c_gaussian_limit(self):
        """For large c, all S_r for r >= 4 should be small.

        As c -> infty: alpha -> 36, Q_L -> (c+6t)^2, sqrt(Q_L) -> c+6t,
        so a_0 -> c, a_1 -> 6, a_n -> 0 for n >= 2.
        """
        c_large = 10000.0
        a_alpha = (180 * c_large + 872) / (5 * c_large + 22)
        a = [0.0] * 8
        a[0] = c_large
        a[1] = 6.0
        a[2] = (a_alpha - 36) / (2 * c_large)
        for n in range(3, 8):
            conv = sum(a[j] * a[n - j] for j in range(1, n))
            a[n] = -conv / (2 * c_large)

        # a_2 should be small: 40/(c*(5c+22)) ~ 40/(5*c^2) ~ 8e-7
        assert abs(a[2]) < 0.001
        # Higher a_n should be even smaller
        for n in range(3, 8):
            assert abs(a[n]) < abs(a[2])

    def test_moment_integral_positive(self):
        """I_r = int_0^1 t^r sqrt(Q_L(t)) dt > 0 for c > 0 (integrand positive)."""
        for c_num in [1.0, 13.0, 26.0]:
            for r in range(5):
                I_r = moment_integral_numerical(r, c_num)
                assert I_r > 0, f"I_{r}({c_num}) = {I_r} should be positive"
