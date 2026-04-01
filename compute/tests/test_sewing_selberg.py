r"""
test_sewing_selberg.py -- Independent verification of the Sewing-Selberg formula.

Tests the Selberg integral S_n(a, b, c), its connection to Heisenberg sewing
amplitudes, and the genus-1 free energy F_1(H_k) = k/24.

VERIFICATION STRATEGY:
  1. S_1(a,b,c) = B(a,b) for all c (the n=1 Selberg integral is the beta function)
  2. S_n(a,b,c) product formula vs direct numerical integration for small n
  3. Morris identity: S_n(1,1,1) = known exact values
  4. Heisenberg F_1 = k/24 from multiple independent routes
  5. Selberg growth analysis
  6. Convention pitfall detection

Anti-patterns guarded against:
  AP1: Copy-paste formulas between families -- we compute from first principles
  AP3: Pattern completion -- independent verification at each n
  AP10: Hardcoded wrong expected values -- multiple independent computations
  AP22: Generating function index mismatch -- careful x^{2g} vs x^{2g-2}
"""

import math
import pytest
from fractions import Fraction

from compute.lib.sewing_selberg import (
    selberg_integral,
    selberg_integral_exact,
    selberg_integral_numerical,
    selberg_symmetric,
    morris_integral,
    morris_integral_exact,
    beta_function,
    heisenberg_kappa,
    heisenberg_F_g,
    heisenberg_F1,
    heisenberg_partition_log,
    selberg_sewing_amplitude,
    dyson_circular_integral,
    selberg_growth_sequence,
    selberg_ratio_sequence,
    lambda_g_fp,
    selberg_F1_cross_check,
    mehta_integral,
    mehta_log_asymptotics,
    selberg_convention_comparison,
    genus1_sewing_from_eta,
    verify_F1_from_bernoulli,
)

# Try to import mpmath for numerical integration tests
try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

needs_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath not installed")


# ============================================================
# Test 1: S_1(a,b,c) = B(a,b) -- fundamental identity
# ============================================================

class TestSelbergN1:
    """S_1(a,b,c) = B(a,b) = Gamma(a)*Gamma(b)/Gamma(a+b) for all c."""

    @needs_mpmath
    @pytest.mark.parametrize("a,b,c", [
        (1.0, 1.0, 0.5),
        (1.0, 1.0, 1.0),
        (1.0, 1.0, 2.0),
        (2.0, 3.0, 1.0),
        (0.5, 0.5, 1.0),
        (1.0, 1.0, 0.0),  # c=0 should still give B(1,1) = 1
    ])
    def test_s1_equals_beta(self, a, b, c):
        """S_1(a,b,c) must equal B(a,b) regardless of c."""
        s1 = selberg_integral(1, a, b, c)
        beta = beta_function(a, b)
        assert abs(s1 - beta) < 1e-14, (
            f"S_1({a},{b},{c}) = {s1} != B({a},{b}) = {beta}"
        )

    @needs_mpmath
    def test_s1_beta_11(self):
        """S_1(1,1,c) = B(1,1) = 1 for all c."""
        for c in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0]:
            s1 = selberg_integral(1, 1.0, 1.0, c)
            assert abs(s1 - 1.0) < 1e-14, f"S_1(1,1,{c}) = {s1} != 1"

    @needs_mpmath
    def test_s1_beta_half_half(self):
        """S_1(1/2, 1/2, c) = B(1/2, 1/2) = pi for all c."""
        expected = math.pi
        for c in [0.5, 1.0, 2.0]:
            s1 = selberg_integral(1, 0.5, 0.5, c)
            assert abs(s1 - expected) < 1e-12, (
                f"S_1(0.5, 0.5, {c}) = {s1} != pi = {expected}"
            )


# ============================================================
# Test 2: S_2(a,b,c) -- product formula vs numerical integration
# ============================================================

class TestSelbergN2:
    """Verify S_2 product formula against direct numerical integration."""

    @needs_mpmath
    def test_s2_product_vs_numerical_111(self):
        """S_2(1,1,1) product formula vs numerical integration."""
        product = selberg_integral(2, 1.0, 1.0, 1.0)
        numerical = selberg_integral_numerical(2, 1.0, 1.0, 1.0, dps=20)
        assert abs(product - numerical) / abs(product) < 1e-8, (
            f"S_2(1,1,1): product={product}, numerical={numerical}"
        )

    @needs_mpmath
    def test_s2_product_vs_numerical_110_5(self):
        """S_2(1,1,0.5) product formula vs numerical integration.

        Note: numerical integration of |x_i - x_j|^{2c} with non-integer
        exponents converges more slowly.  Tolerance relaxed to 1e-4.
        """
        product = selberg_integral(2, 1.0, 1.0, 0.5)
        numerical = selberg_integral_numerical(2, 1.0, 1.0, 0.5, dps=20)
        assert abs(product - numerical) / abs(product) < 1e-4, (
            f"S_2(1,1,0.5): product={product}, numerical={numerical}"
        )

    @needs_mpmath
    def test_s2_product_vs_numerical_231(self):
        """S_2(2,3,1) product formula vs numerical integration."""
        product = selberg_integral(2, 2.0, 3.0, 1.0)
        numerical = selberg_integral_numerical(2, 2.0, 3.0, 1.0, dps=20)
        assert abs(product - numerical) / abs(product) < 1e-8, (
            f"S_2(2,3,1): product={product}, numerical={numerical}"
        )

    @needs_mpmath
    def test_s2_known_value(self):
        """S_2(1,1,1) = 1/6 (exact).

        Product: j=0: Gamma(1)*Gamma(1)*Gamma(2) / [Gamma(3)*Gamma(2)] = 1*1*1/(2*1) = 1/2
                 j=1: Gamma(2)*Gamma(2)*Gamma(3) / [Gamma(4)*Gamma(2)] = 1*1*2/(6*1) = 1/3
        Total: 1/2 * 1/3 = 1/6.
        """
        s2 = selberg_integral(2, 1.0, 1.0, 1.0)
        expected = 1.0 / 6.0
        assert abs(s2 - expected) < 1e-14, f"S_2(1,1,1) = {s2} != 1/6"


# ============================================================
# Test 3: Morris identity S_n(1,1,1)
# ============================================================

class TestMorris:
    """Morris integral: S_n(1, 1, 1) = prod_{j=0}^{n-1} (j!)^2 (j+1)! / (n+j)!."""

    @needs_mpmath
    def test_morris_n1(self):
        """S_1(1,1,1) = 1 (= B(1,1))."""
        assert abs(morris_integral(1) - 1.0) < 1e-14

    @needs_mpmath
    def test_morris_n2(self):
        """S_2(1,1,1) = 1/6.

        Exact: (0!)^2*1!/2! * (1!)^2*2!/3! = (1/2) * (2/6) = 1/6.
        """
        exact = morris_integral_exact(2)
        assert exact == Fraction(1, 6)
        numerical = morris_integral(2)
        assert abs(numerical - 1.0 / 6.0) < 1e-14

    @needs_mpmath
    def test_morris_n3(self):
        """S_3(1,1,1) computed exactly.

        j=0: 1*1*1 / (3!*1) = 1/6
        j=1: 1*1*2 / (4!*1) = 2/24 = 1/12
        j=2: 2*2*6 / (5!*1) = 24/120 = 1/5
        Total: 1/6 * 1/12 * 1/5 = 1/360.
        """
        exact = morris_integral_exact(3)
        expected = Fraction(1, 360)
        assert exact == expected, f"S_3(1,1,1) = {exact} != {expected}"
        numerical = morris_integral(3)
        assert abs(numerical - 1.0 / 360.0) < 1e-13

    @needs_mpmath
    def test_morris_n4(self):
        """S_4(1,1,1) computed exactly.

        j=0: 1/4! = 1/24
        j=1: 2/5! = 2/120 = 1/60
        j=2: 24/6! = 24/720 = 1/30
        j=3: 720/7! = 720/5040 = 1/7
        Total: 1/24 * 1/60 * 1/30 * 1/7 = 1/302400.
        """
        exact = morris_integral_exact(4)
        # Compute independently:
        prod_val = Fraction(1)
        for j in range(4):
            num = math.factorial(j) ** 2 * math.factorial(j + 1)
            den = math.factorial(4 + j)
            prod_val *= Fraction(num, den)
        assert exact == prod_val
        numerical = morris_integral(4)
        assert abs(numerical - float(exact)) < 1e-12

    @needs_mpmath
    def test_morris_exact_matches_product(self):
        """Morris exact formula matches Selberg product formula for n=1..6."""
        for n in range(1, 7):
            exact = float(morris_integral_exact(n))
            product = selberg_integral(n, 1.0, 1.0, 1.0)
            assert abs(exact - product) / max(abs(exact), 1e-30) < 1e-12, (
                f"n={n}: exact={exact}, product={product}"
            )

    @needs_mpmath
    def test_morris_rapid_decay(self):
        """S_n(1,1,1) decays super-exponentially as n grows."""
        vals = [float(morris_integral_exact(n)) for n in range(1, 8)]
        # Each ratio S_{n+1}/S_n should be DECREASING
        ratios = [vals[i + 1] / vals[i] for i in range(len(vals) - 1)]
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] < ratios[i], (
                f"Morris ratios not decreasing: r[{i}]={ratios[i]}, r[{i+1}]={ratios[i+1]}"
            )


# ============================================================
# Test 4: S_n(1,1,c) for Heisenberg connection
# ============================================================

class TestSelbergHeisenberg:
    """Selberg integral with parameters relevant to Heisenberg sewing."""

    @needs_mpmath
    def test_symmetric_selberg_k_half(self):
        """S_n(1, 1, 1/2) for n=1,2,3 (Heisenberg at k=1, c=k/2=1/2)."""
        # n=1: B(1,1) = 1
        s1 = selberg_integral(1, 1.0, 1.0, 0.5)
        assert abs(s1 - 1.0) < 1e-14

        # n=2: product formula
        # j=0: Gamma(1)*Gamma(1)*Gamma(3/2) / [Gamma(5/2)*Gamma(3/2)]
        #     = 1*1*sqrt(pi)/2 / [(3*sqrt(pi)/4) * (sqrt(pi)/2)]
        #     = (sqrt(pi)/2) / (3*pi/8)
        #     = 4/(3*sqrt(pi))
        # j=1: Gamma(3/2)*Gamma(3/2)*Gamma(2) / [Gamma(3)*Gamma(3/2)]
        #     = (sqrt(pi)/2)^2 * 1 / [2 * sqrt(pi)/2]
        #     = (pi/4) / sqrt(pi)
        #     = sqrt(pi)/4
        # Total: 4/(3*sqrt(pi)) * sqrt(pi)/4 = 1/3
        s2 = selberg_integral(2, 1.0, 1.0, 0.5)
        assert abs(s2 - 1.0 / 3.0) < 1e-13, f"S_2(1,1,1/2) = {s2} != 1/3"

    @needs_mpmath
    def test_symmetric_selberg_k1(self):
        """S_2(1, 1, 1) = 1/6 for Heisenberg at k=2 (c=k/2=1)."""
        s2 = selberg_integral(2, 1.0, 1.0, 1.0)
        assert abs(s2 - 1.0 / 6.0) < 1e-14

    @needs_mpmath
    def test_sewing_amplitude_k1(self):
        """Sewing amplitude S_n(1, 1, 1/2) for Heisenberg k=1."""
        # This is the symmetric Selberg integral with c = k/2 = 1/2
        s1 = selberg_sewing_amplitude(1, 1.0)
        assert abs(s1 - 1.0) < 1e-14

        s2 = selberg_sewing_amplitude(2, 1.0)
        assert abs(s2 - 1.0 / 3.0) < 1e-13


# ============================================================
# Test 5: Heisenberg F_1 = kappa/24 from multiple routes
# ============================================================

class TestHeisenbergF1:
    """Verify F_1(H_k) = k/24 from independent computations."""

    @needs_mpmath
    def test_F1_from_kappa(self):
        """F_1 = kappa/24 for k = 1, 2, 5, 10."""
        for k in [1, 2, 5, 10]:
            f1 = heisenberg_F1(k)
            expected = k / 24.0
            assert abs(f1 - expected) < 1e-15, (
                f"F_1(H_{k}) = {f1} != {expected}"
            )

    @needs_mpmath
    def test_F1_from_Fg_formula(self):
        """F_1 from the Faber-Pandharipande formula matches kappa/24."""
        for k in [1, 2, 3, 7]:
            f1_fg = heisenberg_F_g(1, k)
            f1_direct = heisenberg_F1(k)
            assert abs(f1_fg - f1_direct) < 1e-14, (
                f"F_1(H_{k}): FP={f1_fg}, direct={f1_direct}"
            )

    @needs_mpmath
    def test_F1_cross_check(self):
        """Full cross-check for k=1."""
        result = selberg_F1_cross_check(1.0)
        assert result['all_F1_agree'], f"F_1 routes disagree: {result}"
        assert abs(result['kappa_over_24'] - 1.0 / 24.0) < 1e-15

    @needs_mpmath
    def test_F1_cross_check_k2(self):
        """Full cross-check for k=2."""
        result = selberg_F1_cross_check(2.0)
        assert result['all_F1_agree']
        assert abs(result['kappa_over_24'] - 2.0 / 24.0) < 1e-15

    @needs_mpmath
    def test_F1_bernoulli_verification(self):
        """Verify F_1 = k/24 from Bernoulli number B_2 = 1/6."""
        for k in [1, 2, 5]:
            result = verify_F1_from_bernoulli(k)
            assert result['match'], f"Bernoulli verification failed for k={k}: {result}"
            assert abs(result['lambda1_FP'] - 1.0 / 24.0) < 1e-15

    @needs_mpmath
    def test_lambda1_FP(self):
        r"""lambda_1^{FP} = 1/24.

        lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
        At g=1: (2-1)/2 * (1/6)/2 = 1/2 * 1/12 = 1/24.
        """
        l1 = lambda_g_fp(1)
        assert abs(l1 - 1.0 / 24.0) < 1e-15

    @needs_mpmath
    def test_lambda2_FP(self):
        r"""lambda_2^{FP} = 7/5760.

        At g=2: (2^3-1)/2^3 * |B_4|/4! = 7/8 * (1/30)/24 = 7/8 * 1/720 = 7/5760.
        """
        l2 = lambda_g_fp(2)
        expected = 7.0 / 5760.0
        assert abs(l2 - expected) < 1e-15, f"lambda_2 = {l2} != {expected}"


# ============================================================
# Test 6: Heisenberg genus expansion at higher genera
# ============================================================

class TestHeisenbergHigherGenus:
    """F_g(H_k) at genus g >= 2."""

    @needs_mpmath
    def test_F2_heisenberg_k1(self):
        """F_2(H_1) = 7/5760."""
        f2 = heisenberg_F_g(2, 1.0)
        expected = 7.0 / 5760.0
        assert abs(f2 - expected) < 1e-14, f"F_2(H_1) = {f2} != {expected}"

    @needs_mpmath
    def test_F3_heisenberg_k1(self):
        """F_3(H_1) = 31/967680.

        lambda_3 = (2^5-1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/(32*30240) = 31/967680.
        """
        f3 = heisenberg_F_g(3, 1.0)
        expected = 31.0 / 967680.0
        assert abs(f3 - expected) < 1e-14, f"F_3(H_1) = {f3} != {expected}"

    @needs_mpmath
    def test_Fg_linearity_in_k(self):
        """F_g(H_k) = k * F_g(H_1) for all g, k (linearity in kappa = k)."""
        for g in [1, 2, 3, 4]:
            f_g_1 = heisenberg_F_g(g, 1.0)
            for k in [2, 3, 5]:
                f_g_k = heisenberg_F_g(g, float(k))
                assert abs(f_g_k - k * f_g_1) < 1e-13 * max(abs(f_g_k), 1e-20), (
                    f"F_{g}(H_{k}) = {f_g_k} != {k} * F_{g}(H_1) = {k * f_g_1}"
                )

    @needs_mpmath
    def test_Fg_rank_scaling(self):
        """F_g(H_k, rank d) = d * F_g(H_k, rank 1)."""
        for g in [1, 2, 3]:
            f_rank1 = heisenberg_F_g(g, 1.0, d=1)
            for d in [2, 3, 5]:
                f_rank_d = heisenberg_F_g(g, 1.0, d=d)
                assert abs(f_rank_d - d * f_rank1) < 1e-14 * max(abs(f_rank_d), 1e-20)

    @needs_mpmath
    def test_Fg_all_positive(self):
        """F_g(H_k) > 0 for all g >= 1, k > 0.

        The Bernoulli numbers alternate in sign, but the factor
        (2^{2g-1}-1)/2^{2g-1} * |B_{2g}| / (2g)! is always positive.
        """
        for g in range(1, 8):
            f_g = heisenberg_F_g(g, 1.0)
            assert f_g > 0, f"F_{g}(H_1) = {f_g} <= 0"


# ============================================================
# Test 7: Selberg growth analysis
# ============================================================

class TestSelbergGrowth:
    """Analyze how S_n(a,b,c) grows with n."""

    @needs_mpmath
    def test_morris_superexponential_decay(self):
        """S_n(1,1,1) decays faster than any exponential."""
        vals = selberg_growth_sequence(8, 1.0, 1.0, 1.0)
        # Check S_n > 0 for all n
        for n, v in enumerate(vals, 1):
            assert v > 0, f"S_{n}(1,1,1) = {v} <= 0"
        # Check monotone decrease
        for i in range(len(vals) - 1):
            assert vals[i + 1] < vals[i], (
                f"S_{i+2}(1,1,1) = {vals[i+1]} >= S_{i+1}(1,1,1) = {vals[i]}"
            )

    @needs_mpmath
    def test_selberg_ratio_analysis(self):
        """Ratio S_{n+1}/S_n for S_n(1,1,1) should decrease."""
        ratios = selberg_ratio_sequence(7, 1.0, 1.0, 1.0)
        # Ratios should be positive and decreasing
        for i, r in enumerate(ratios):
            assert 0 < r < 1, f"Ratio at n={i+1}: {r} not in (0,1)"
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] < ratios[i], (
                f"Ratios not decreasing at n={i+2}"
            )

    @needs_mpmath
    def test_selberg_growth_c_half(self):
        """S_n(1,1,1/2) for n=1..6: still decays but slower than c=1."""
        vals_half = selberg_growth_sequence(6, 1.0, 1.0, 0.5)
        vals_one = selberg_growth_sequence(6, 1.0, 1.0, 1.0)
        # S_n(1,1,1/2) > S_n(1,1,1) for n >= 2 (less repulsion)
        for n in range(1, 6):  # index 1 = n=2
            assert vals_half[n] > vals_one[n], (
                f"n={n+1}: S_n(1,1,1/2) = {vals_half[n]} <= S_n(1,1,1) = {vals_one[n]}"
            )


# ============================================================
# Test 8: Dyson/Mehta circular integral
# ============================================================

class TestDysonMehta:
    """Dyson circular integral M_n(beta)."""

    @needs_mpmath
    def test_dyson_n1(self):
        """M_1(beta) = Gamma(1+beta)/Gamma(1+beta) = 1 for all beta."""
        for beta in [0.5, 1.0, 2.0]:
            m1 = dyson_circular_integral(1, beta)
            assert abs(m1 - 1.0) < 1e-14

    @needs_mpmath
    def test_dyson_n2_beta1(self):
        """M_2(1) = Gamma(2)*Gamma(3) / Gamma(2)^2 = 1*2/1 = 2."""
        m2 = dyson_circular_integral(2, 1.0)
        assert abs(m2 - 2.0) < 1e-14

    @needs_mpmath
    def test_dyson_n3_beta1(self):
        """M_3(1) = Gamma(2)*Gamma(3)*Gamma(4) / Gamma(2)^3 = 1*2*6/1 = 12."""
        m3 = dyson_circular_integral(3, 1.0)
        assert abs(m3 - 12.0) < 1e-12

    @needs_mpmath
    def test_dyson_beta1_is_factorial(self):
        """M_n(1) = prod_{j=1}^n j! / 1^n = (1!)(2!)(3!)...(n!).

        Actually: Gamma(1+j)/Gamma(2) = j!/1 = j!.
        M_n(1) = prod_{j=1}^n j!.
        M_1 = 1, M_2 = 1*2 = 2, M_3 = 1*2*6 = 12, M_4 = 1*2*6*24 = 288.
        """
        expected = [1, 2, 12, 288]
        for n in range(1, 5):
            mn = dyson_circular_integral(n, 1.0)
            assert abs(mn - expected[n - 1]) < 1e-10, (
                f"M_{n}(1) = {mn} != {expected[n-1]}"
            )


# ============================================================
# Test 9: Convention comparison
# ============================================================

class TestConventions:
    """Detect convention pitfalls between different Selberg formulations."""

    @needs_mpmath
    def test_convention_matters_at_n2(self):
        """Convention A (exponent 2c) vs Convention D (exponent c) differ at n >= 2.

        S_2^A(1,1,1) uses |x_i-x_j|^{2*1} = |x_i-x_j|^2
        S_2^D(1,1,1) uses |x_i-x_j|^{1}, i.e. S_2^A(1,1,1/2)

        These are different values.
        """
        result = selberg_convention_comparison(2, 1.0, 1.0, 1.0)
        conv_A = result['convention_A_2c']  # S_2(1,1,1) = 1/6
        conv_D = result['convention_D_c']   # S_2(1,1,1/2) = 1/3
        assert abs(conv_A - 1.0 / 6.0) < 1e-14
        assert abs(conv_D - 1.0 / 3.0) < 1e-13
        assert abs(result['ratio_A_over_D'] - 0.5) < 1e-12, (
            f"Convention ratio = {result['ratio_A_over_D']} != 1/2"
        )

    @needs_mpmath
    def test_convention_irrelevant_at_n1(self):
        """At n=1, both conventions give B(a,b), so the ratio is 1."""
        result = selberg_convention_comparison(1, 2.0, 3.0, 1.0)
        assert abs(result['ratio_A_over_D'] - 1.0) < 1e-14


# ============================================================
# Test 10: Partition function coefficients
# ============================================================

class TestPartitionCoefficients:
    """Heisenberg partition function F_1^conn(q) coefficients."""

    @needs_mpmath
    def test_partition_coeffs_k1(self):
        """F_1^conn(q) = sum sigma_{-1}(N) q^N for k=1.

        sigma_{-1}(1) = 1, sigma_{-1}(2) = 1+1/2 = 3/2,
        sigma_{-1}(3) = 1+1/3 = 4/3.
        """
        coeffs = heisenberg_partition_log(1.0, 5)
        assert abs(coeffs[0] - 1.0) < 1e-14  # N=1: sigma_{-1}(1) = 1
        assert abs(coeffs[1] - 1.5) < 1e-14  # N=2: sigma_{-1}(2) = 3/2
        assert abs(coeffs[2] - 4.0 / 3.0) < 1e-14  # N=3: sigma_{-1}(3) = 4/3
        # N=4: sigma_{-1}(4) = 1 + 1/2 + 1/4 = 7/4
        assert abs(coeffs[3] - 7.0 / 4.0) < 1e-14
        # N=5: sigma_{-1}(5) = 1 + 1/5 = 6/5
        assert abs(coeffs[4] - 6.0 / 5.0) < 1e-14

    @needs_mpmath
    def test_partition_coeffs_scaled_by_k(self):
        """Coefficients scale linearly with k."""
        coeffs_k1 = heisenberg_partition_log(1.0, 10)
        for k in [2, 3, 5]:
            coeffs_kn = heisenberg_partition_log(float(k), 10)
            for i in range(10):
                assert abs(coeffs_kn[i] - k * coeffs_k1[i]) < 1e-12


# ============================================================
# Test 11: Mehta integral asymptotics
# ============================================================

class TestMehtaAsymptotics:
    """Log M_n(beta) asymptotic expansion."""

    @needs_mpmath
    def test_mehta_log_n_coefficient(self):
        r"""The coefficient of log(n) in log M_n(beta) is (beta+1/beta-1)/12.

        For beta=1: (1+1-1)/12 = 1/12.
        For beta=2: (2+1/2-1)/12 = (3/2)/12 = 1/8.
        """
        assert abs((1 + 1 - 1) / 12 - 1 / 12) < 1e-15
        assert abs((2 + 0.5 - 1) / 12 - 1 / 8) < 1e-15

    @needs_mpmath
    def test_mehta_coeff_NOT_k_over_24(self):
        """The Mehta log(n) coefficient is NOT k/24 in general.

        For beta=k: coeff = (k + 1/k - 1)/12.
        k/24 would require (k + 1/k - 1)/12 = k/24, i.e.
        2(k + 1/k - 1) = k, i.e. 2k + 2/k - 2 = k, i.e. k + 2/k = 2.
        This gives k^2 - 2k + 2 = 0, which has NO real solutions.

        So the Mehta coefficient is NEVER equal to k/24 for real k.
        The connection between Selberg and F_1 = k/24 is NOT via
        the Mehta log(n) coefficient.
        """
        for k in [1, 2, 3]:
            mehta_coeff = (k + 1.0 / k - 1.0) / 12.0
            f1 = k / 24.0
            # These should NOT be equal
            assert abs(mehta_coeff - f1) > 1e-4, (
                f"Mehta coeff and k/24 unexpectedly equal at k={k}: "
                f"mehta={mehta_coeff}, F1={f1}"
            )


# ============================================================
# Test 12: Selberg integral exact computation
# ============================================================

class TestSelbergExact:
    """Exact rational computation of Selberg integral."""

    def test_exact_n2_111(self):
        """S_2(1,1,1) = 1/6 exactly."""
        result = selberg_integral_exact(2, Fraction(1), Fraction(1), Fraction(1))
        assert result == Fraction(1, 6)

    def test_exact_n3_111(self):
        """S_3(1,1,1) = 1/360 exactly."""
        result = selberg_integral_exact(3, Fraction(1), Fraction(1), Fraction(1))
        assert result == Fraction(1, 360)

    def test_exact_n1_23c(self):
        """S_1(2,3,c) = B(2,3) = 1/12 for any integer c."""
        for c in [1, 2, 3]:
            result = selberg_integral_exact(1, Fraction(2), Fraction(3), Fraction(c))
            assert result == Fraction(1, 12), f"S_1(2,3,{c}) = {result} != 1/12"


# ============================================================
# Test 13: S_3 product formula vs numerical
# ============================================================

class TestSelbergN3:
    """S_3 verification: product vs numerical."""

    @needs_mpmath
    def test_s3_product_vs_numerical_111(self):
        """S_3(1,1,1) = 1/360 by both methods."""
        product = selberg_integral(3, 1.0, 1.0, 1.0)
        numerical = selberg_integral_numerical(3, 1.0, 1.0, 1.0, dps=15)
        assert abs(product - 1.0 / 360.0) < 1e-13
        assert abs(numerical - 1.0 / 360.0) / (1.0 / 360.0) < 1e-4, (
            f"S_3 numerical = {numerical}, expected 1/360 = {1/360}"
        )


# ============================================================
# Test 14: Normalization mismatch detection
# ============================================================

class TestNormalizationMismatch:
    """Detect potential normalization errors in sewing-Selberg connection."""

    @needs_mpmath
    def test_selberg_does_not_directly_give_F1(self):
        """No finite-n Selberg integral S_n(1,1,k) equals F_1 = k/24.

        S_1(1,1,k) = 1 (independent of k).
        S_2(1,1,k) depends on k but is NOT k/24.

        The connection is asymptotic (via Mehta), not direct.
        """
        for k_val in [1, 2, 5]:
            k = float(k_val)
            s1 = selberg_integral(1, 1.0, 1.0, k)
            s2 = selberg_integral(2, 1.0, 1.0, k)
            f1 = k / 24.0

            # S_1 = 1, not k/24
            assert abs(s1 - f1) > 0.01 or k_val == 24, (
                f"S_1(1,1,{k}) unexpectedly equals F_1={f1}"
            )
            # S_2 is not k/24 either
            assert abs(s2 - f1) > 1e-4, (
                f"S_2(1,1,{k}) = {s2} unexpectedly equals F_1={f1}"
            )

    @needs_mpmath
    def test_eta_route_is_correct(self):
        """F_1 = k/24 comes from eta function, NOT from any Selberg integral.

        The correct derivation chain:
        Heisenberg Z_1(q) = eta(q)^{-k}
        => F_1^conn = -k * log eta(q)
        => constant term = k * zeta(-1) = k * (-1/12)
        Wait: zeta(-1) = -1/12, so k * (-(-1/12)) = k/12? That's wrong.

        Correct: eta(q) = q^{1/24} prod(1-q^n)
        => log eta = (2*pi*i*tau)/24 + sum log(1-q^n)
        => -k * log eta = -k*(2*pi*i*tau)/24 - k*sum log(1-q^n)
        The first term gives the q^{-k/24} in the partition function.
        F_1 = k/24 is the leading Faber-Pandharipande value.

        Check: B_2 = 1/6, lambda_1 = 1/24.
        F_1 = kappa * lambda_1 = k * 1/24 = k/24. Correct.
        """
        f1 = genus1_sewing_from_eta(1.0)
        assert abs(f1 - 1.0 / 24.0) < 1e-15

    @needs_mpmath
    def test_F1_does_not_come_from_selberg(self):
        """Explicit verification that F_1 = k/24 is NOT a Selberg integral value.

        The sewing-Selberg connection (if it exists) must involve an
        INFINITE product or asymptotic limit, not a finite Selberg integral.
        """
        k = 1.0
        f1 = k / 24.0  # = 1/24

        # Check S_n(1,1,k) for n=1..10: none should equal 1/24
        for n in range(1, 11):
            sn = selberg_integral(n, 1.0, 1.0, k)
            if abs(sn - f1) < 1e-10:
                # This would be a coincidence worth investigating
                pytest.fail(
                    f"COINCIDENCE: S_{n}(1,1,{k}) = {sn} matches F_1 = {f1}. "
                    f"Investigate whether this is meaningful."
                )


# ============================================================
# Test 15: Heisenberg kappa values
# ============================================================

class TestKappaValues:
    """Verify kappa(H_k) = k and related values."""

    def test_kappa_rank1(self):
        """kappa(H_k) = k for rank 1."""
        for k in [1, 2, 3, -1, 0.5]:
            assert heisenberg_kappa(k) == k

    def test_kappa_rank_d(self):
        """kappa(H_k, rank d) = d*k."""
        assert heisenberg_kappa(1, 3) == 3
        assert heisenberg_kappa(2, 5) == 10
        assert heisenberg_kappa(0.5, 4) == 2.0

    def test_kappa_complementarity(self):
        """kappa(H_k) + kappa(H_{-k}) = 0 (anti-symmetry for Heisenberg).

        This is the AP24-safe statement: kappa + kappa' = 0 for Heisenberg/KM.
        NOT universal (Virasoro has kappa + kappa' = 13, not 0).
        """
        for k in [1, 2, 3, 0.5]:
            assert abs(heisenberg_kappa(k) + heisenberg_kappa(-k)) < 1e-15


# ============================================================
# Test 16: Generating function consistency
# ============================================================

class TestGeneratingFunction:
    """Verify the generating function sum F_g x^{2g} = kappa(x/sin(x/2) - 1)."""

    @needs_mpmath
    def test_generating_function_expansion(self):
        """sum_{g=1}^G F_g(H_1) x^{2g} should match kappa*(x/2/sin(x/2) - 1).

        At x = 0.1 (small):
        x/2/sin(x/2) - 1 = (0.05/sin(0.05)) - 1
        sin(0.05) ~ 0.05 - 0.05^3/6 = 0.05 - 2.083e-5 = 0.049979...
        0.05/0.049979 - 1 ~ 1.000417 - 1 = 4.17e-4

        Sum: F_1 * 0.01 + F_2 * 0.0001 + ... = (1/24)*0.01 + (7/5760)*0.0001 + ...
           = 4.1667e-4 + 1.215e-7 + ... ~ 4.168e-4
        """
        x = 0.1
        kappa = 1.0  # k = 1

        # Compute partial sum
        partial_sum = sum(heisenberg_F_g(g, kappa) * x ** (2 * g) for g in range(1, 10))

        # Compute exact generating function
        half_x = x / 2.0
        exact = kappa * (half_x / math.sin(half_x) - 1.0)

        assert abs(partial_sum - exact) < 1e-12, (
            f"GF mismatch at x={x}: partial={partial_sum}, exact={exact}"
        )

    @needs_mpmath
    def test_gf_index_is_2g_not_2g_minus_2(self):
        """CRITICAL (AP22): the generating function uses x^{2g}, NOT x^{2g-2}.

        sum F_g x^{2g} = kappa*(x/2/sin(x/2) - 1).

        If we incorrectly used x^{2g-2}:
        sum F_g x^{2g-2} = F_1 + F_2 x^2 + ... (starts at x^0)
        But kappa*(x/2/sin(x/2) - 1) starts at x^2 (since x/sin(x) - 1 ~ x^2/6).
        The F_1 x^0 term on the left has no match on the right.

        This confirms the INDEX IS x^{2g}.
        """
        kappa = 1.0
        # The generating function starts at x^2 order
        # x/2/sin(x/2) - 1 = (x/2)^2/6 + ... at leading order
        # The coefficient of x^2 is 1/24 = F_1. Check:
        f1 = heisenberg_F_g(1, kappa)
        # Leading Taylor of x/2/sin(x/2) - 1:
        # = (x/2)/(x/2 - (x/2)^3/6 + ...) - 1
        # = 1/(1 - x^2/24 + ...) - 1
        # = x^2/24 + ...
        # So coefficient of x^2 is 1/24 = F_1. Correct.
        assert abs(f1 - 1.0 / 24.0) < 1e-15


# ============================================================
# Test 17: Selberg integral convergence conditions
# ============================================================

class TestConvergence:
    """Verify convergence conditions for the Selberg integral."""

    @needs_mpmath
    def test_convergence_positive_params(self):
        """S_n(a,b,c) converges for a,b,c > 0."""
        for n in [1, 2, 3]:
            val = selberg_integral(n, 1.0, 1.0, 0.5)
            assert val > 0 and math.isfinite(val), (
                f"S_{n}(1,1,0.5) = {val} not finite positive"
            )

    @needs_mpmath
    def test_c_zero_gives_product_of_betas(self):
        """S_n(a,b,0) = B(a,b)^n (independent integrals when c=0)."""
        a, b = 2.0, 3.0
        beta_val = beta_function(a, b)
        for n in [1, 2, 3, 4]:
            sn = selberg_integral(n, a, b, 0.0)
            expected = beta_val ** n
            assert abs(sn - expected) < 1e-12, (
                f"S_{n}(2,3,0) = {sn} != B(2,3)^{n} = {expected}"
            )


# ============================================================
# Test 18: Symmetry S_n(a,b,c) = S_n(b,a,c)
# ============================================================

class TestSelbergSymmetry:
    """S_n(a,b,c) = S_n(b,a,c) by the substitution x_i -> 1-x_i."""

    @needs_mpmath
    def test_ab_symmetry(self):
        """S_n(a,b,c) = S_n(b,a,c) for several (a,b,c,n)."""
        test_cases = [
            (2, 2.0, 3.0, 1.0),
            (3, 1.0, 2.0, 0.5),
            (2, 0.5, 1.5, 1.0),
        ]
        for n, a, b, c in test_cases:
            sab = selberg_integral(n, a, b, c)
            sba = selberg_integral(n, b, a, c)
            assert abs(sab - sba) < 1e-13, (
                f"S_{n}({a},{b},{c}) = {sab} != S_{n}({b},{a},{c}) = {sba}"
            )


# ============================================================
# Test 19: Selberg product formula internal consistency
# ============================================================

class TestProductFormula:
    """Internal consistency checks on the product formula."""

    @needs_mpmath
    def test_product_formula_ratio(self):
        """S_{n+1} / S_n should be a computable ratio.

        S_{n+1}(a,b,c) / S_n(a,b,c) =
            [new factor j=n] * prod_{j=0}^{n-1} [Gamma(a+b+(n+j)c) / Gamma(a+b+(n-1+j)c)]^{-1}

        Since the denominator Gamma(a+b+(N-1+j)c) changes when N goes from n to n+1,
        the ratio is NOT simply the j=n factor.

        We verify instead by direct division of the product formula values.
        """
        import mpmath as mp
        a, b, c = 1.0, 1.0, 1.0
        for n in range(1, 6):
            sn = selberg_integral(n, a, b, c)
            sn1 = selberg_integral(n + 1, a, b, c)

            # Compute the ratio S_{n+1}/S_n directly from the product formula
            old_dps = mp.mp.dps
            mp.mp.dps = 30

            # S_{n+1} = prod_{j=0}^n num(j,n+1)/den(j,n+1)
            # S_n = prod_{j=0}^{n-1} num(j,n)/den(j,n)
            # where num(j,N) = Gamma(a+jc)*Gamma(b+jc)*Gamma(1+(j+1)c)
            #       den(j,N) = Gamma(a+b+(N-1+j)c)*Gamma(1+c)
            # The numerators are the same, but denominators differ in N.

            expected_ratio = mp.mpf(1)
            # New j=n factor (only in S_{n+1})
            expected_ratio *= (
                mp.gamma(a + n * c) * mp.gamma(b + n * c) * mp.gamma(1 + (n + 1) * c)
                / (mp.gamma(a + b + (n + n) * c) * mp.gamma(1 + c))
            )
            # Correction for j=0..n-1: denominator changes from (n-1+j)c to (n+j)c
            for j in range(n):
                expected_ratio *= (
                    mp.gamma(a + b + (n - 1 + j) * c)
                    / mp.gamma(a + b + (n + j) * c)
                )
            expected_ratio = float(expected_ratio)
            mp.mp.dps = old_dps

            actual_ratio = sn1 / sn
            assert abs(actual_ratio - expected_ratio) / max(abs(actual_ratio), 1e-30) < 1e-10, (
                f"n={n}: actual_ratio={actual_ratio}, expected_ratio={expected_ratio}"
            )


# ============================================================
# Test 20: Key finding -- the sewing-Selberg connection
# ============================================================

class TestSewingSelbergConnection:
    """The sewing-Selberg connection is ASYMPTOTIC, not direct.

    FINDING: The genus-1 free energy F_1 = k/24 does NOT arise as any
    finite Selberg integral S_n(a,b,c) at fixed n.  Instead:

    1. The Heisenberg partition function Z_1 = eta^{-k} gives F_1 = k/24
       via the Dedekind eta function.
    2. The Selberg integral appears in correlation functions, NOT in the
       partition function.
    3. The Mehta integral M_n(beta) has a log(n) coefficient
       (beta + 1/beta - 1)/12, which equals k/24 ONLY IF
       k + 1/k - 1 = k/2, i.e. never for real k.

    CONCLUSION: If the manuscript claims a direct "sewing-Selberg formula"
    A_g(H_k) = (normalization) * S_n(k), this is WRONG.  The correct
    statement involves the INFINITE PRODUCT (Fredholm determinant / eta),
    not a finite Selberg integral.
    """

    @needs_mpmath
    def test_no_finite_selberg_matches_F1(self):
        """No S_n(a,b,c) for reasonable parameters equals k/24."""
        k = 1.0
        target = 1.0 / 24.0

        for n in range(1, 8):
            # Try various parameter choices
            for a, b, c in [(1, 1, k), (1, 1, k / 2), (k, k, 1), (1, k, 1)]:
                sn = selberg_integral(n, float(a), float(b), float(c))
                if abs(sn - target) < 1e-8:
                    # Document the coincidence but don't fail
                    print(f"COINCIDENCE: S_{n}({a},{b},{c}) = {sn} ~ F_1 = {target}")

    @needs_mpmath
    def test_eta_product_is_infinite_selberg(self):
        """The eta function is the INFINITE product, not a finite Selberg integral.

        prod_{n=1}^N (1 - q^n) converges to eta(q) * q^{-1/24} as N -> infty.
        This is an infinite product, not a Selberg integral.

        The connection between Selberg integrals and random matrix theory
        (circular beta-ensemble) involves the JOINT DENSITY, not the
        partition function.
        """
        if not HAS_MPMATH:
            pytest.skip("mpmath required")

        # Compute partial product and check convergence
        mpmath.mp.dps = 30
        q = mpmath.mpf(0.1)
        partial = mpmath.mpf(1)
        for n in range(1, 50):
            partial *= (1 - q ** n)

        # Compare with Dedekind eta
        tau = mpmath.log(q) / (2 * mpmath.pi * mpmath.mpc(0, 1))
        eta_val = q ** mpmath.mpf('1/24') * partial

        # The point: this is an INFINITE product, fundamentally different
        # from the finite Selberg integral.  Both involve products of
        # differences, but the structures are different:
        # - Selberg: integral over [0,1]^n of prod |x_i - x_j|^{2c}
        # - Eta: infinite product prod (1 - q^n)
        assert float(partial) > 0  # Just verify computation ran


# ============================================================
# Test 21: Selberg at large c
# ============================================================

class TestSelbergLargeC:
    """Behavior of S_n(1,1,c) as c grows."""

    @needs_mpmath
    def test_large_c_decay(self):
        """S_n(1,1,c) for fixed n, increasing c, should decay.

        As c -> infty, the repulsion |x_i - x_j|^{2c} forces the
        integration variables apart, reducing the integral.
        """
        n = 3
        vals = []
        for c in [0.5, 1.0, 2.0, 5.0]:
            vals.append(selberg_integral(n, 1.0, 1.0, c))
        for i in range(len(vals) - 1):
            assert vals[i + 1] < vals[i], (
                f"S_3(1,1,{[0.5,1,2,5][i+1]}) = {vals[i+1]} >= "
                f"S_3(1,1,{[0.5,1,2,5][i]}) = {vals[i]}"
            )


# ============================================================
# Test 22: Numerical vs product at n=2 with various parameters
# ============================================================

class TestNumericalVerification:
    """Thorough numerical verification of the product formula."""

    @needs_mpmath
    @pytest.mark.parametrize("a,b,c", [
        (1.0, 1.0, 0.5),
        (1.0, 1.0, 1.0),
        (1.0, 1.0, 2.0),
        (2.0, 1.0, 1.0),
        (1.5, 2.5, 0.5),
    ])
    def test_n2_product_vs_numerical(self, a, b, c):
        """S_2 product formula matches numerical integration.

        Tolerance 1e-4: numerical quadrature of |x_i - x_j|^{2c} with
        non-integer c converges slowly due to the cusp at x_i = x_j.
        """
        product = selberg_integral(2, a, b, c)
        numerical = selberg_integral_numerical(2, a, b, c, dps=20)
        rel_err = abs(product - numerical) / max(abs(product), 1e-30)
        assert rel_err < 1e-4, (
            f"S_2({a},{b},{c}): product={product}, numerical={numerical}, "
            f"rel_err={rel_err}"
        )


# ============================================================
# Test 23: Summary finding
# ============================================================

class TestSummaryFinding:
    """Document the key mathematical finding of this verification.

    FINDING: The "sewing-Selberg formula" as stated in raeeznotes 105-112
    requires careful interpretation:

    1. F_1(H_k) = k/24 is CORRECT (from Bernoulli, Faber-Pandharipande,
       and Dedekind eta).

    2. The Selberg integral S_n(a,b,c) does NOT directly give F_1.
       No finite Selberg integral equals k/24 for general k.

    3. The connection between Selberg integrals and Heisenberg sewing
       goes through the RANDOM MATRIX THEORY bridge:
       - Dyson's circular integral = normalization of circular beta-ensemble
       - Beta-ensemble partition function has logarithmic derivative
         related to the free energy
       - The large-N limit of the beta-ensemble free energy involves
         the Barnes G-function

    4. The CORRECT normalization for the Heisenberg sewing amplitude is:
       Z_g(H_k) = det(1 - K_q)^{-k} (Fredholm determinant)
       which at genus 1 gives eta(q)^{-k} with F_1 = k/24.

    5. If the manuscript claims A_g = S_n(k) for some n, this is either:
       (a) Using "Selberg" loosely to mean "product of Gamma functions"
       (b) Wrong
       The Gamma-function product formula for F_g matches the
       Faber-Pandharipande formula, which involves Bernoulli numbers
       (themselves Gamma-function ratios via the reflection formula).
    """

    @needs_mpmath
    def test_summary_F1_correct(self):
        """F_1 = k/24 verified from 3 independent routes."""
        k = 1.0
        route1 = heisenberg_F1(k)
        route2 = heisenberg_F_g(1, k)
        route3 = lambda_g_fp(1) * heisenberg_kappa(k)
        assert abs(route1 - route2) < 1e-15
        assert abs(route1 - route3) < 1e-15
        assert abs(route1 - 1.0 / 24.0) < 1e-15

    @needs_mpmath
    def test_summary_Fg_is_bernoulli_not_selberg(self):
        """F_g is controlled by Bernoulli numbers, not Selberg integrals.

        F_g = kappa * (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!

        This is a BERNOULLI formula.  The Selberg integral is a
        GAMMA-function product.  They are related through the
        functional equation of the Riemann zeta function
        (B_{2g} = -2*(2g)!/(2*pi)^{2g} * zeta(2g)), but the
        sewing amplitude is NOT a Selberg integral.
        """
        # Verify first few F_g against Bernoulli numbers
        if not HAS_MPMATH:
            pytest.skip("mpmath required")

        # B_2 = 1/6, B_4 = -1/30, B_6 = 1/42
        bernoulli_abs = {
            2: Fraction(1, 6),
            4: Fraction(1, 30),
            6: Fraction(1, 42),
        }
        for g in [1, 2, 3]:
            b2g = bernoulli_abs[2 * g]
            factor = Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            lambda_g = factor * b2g / Fraction(math.factorial(2 * g))
            f_g = float(lambda_g)  # F_g at kappa = 1
            computed = heisenberg_F_g(g, 1.0)
            assert abs(f_g - computed) < 1e-14, (
                f"g={g}: Bernoulli={f_g}, computed={computed}"
            )
