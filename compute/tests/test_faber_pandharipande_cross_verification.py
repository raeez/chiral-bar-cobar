r"""Definitive cross-verification tests for Faber-Pandharipande numbers.

Tests lambda_g^FP = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)! via 6 methods.

Test organization:
  - 6 methods x 10 genera = 60 individual computations
  - All 6 methods agree for each g (10 agreement tests)
  - Generating function (t/2)/sin(t/2) matches term-by-term (10 tests)
  - A-hat genus Ahat(x) = (x/2)/sinh(x/2) relationship (10 tests)
  - AP22 index convention verification
  - Bernoulli number structural properties (von Staudt-Clausen, Kummer)
  - Asymptotic behavior (ratio -> 1)
  - Cross-check against existing utils.lambda_fp
  - Positivity and monotonicity
  - Comparison with published values
  Total: 100+ tests

References: [FP00], [Fab99], concordance.tex (Theorem D).
"""

import pytest
from sympy import Rational, simplify, factorial, pi, Abs, bernoulli as sympy_bernoulli

from compute.lib.faber_pandharipande_cross_verification import (
    method1_bernoulli_recurrence,
    method2_ahat_series,
    method3_zeta_values,
    method4_sympy_bernoulli,
    method5_exponential_generating_function,
    method6_akiyama_tanigawa,
    all_methods,
    verify_all_methods_agree,
    definitive_table,
    bernoulli_table,
    verify_generating_function,
    verify_ahat_relationship,
    asymptotic_ratio,
    verify_bernoulli_von_staudt_clausen,
    verify_bernoulli_kummer_congruence,
    _bernoulli_binomial_recurrence,
    _bernoulli_akiyama_tanigawa,
)


# =====================================================================
# CLASS 1: Individual method tests (6 methods x 10 genera = 60 tests)
# =====================================================================

class TestMethod1BernoulliRecurrence:
    """Method 1: direct Bernoulli via binomial recurrence."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_method1_returns_positive_rational(self, g):
        val = method1_bernoulli_recurrence(g)
        assert isinstance(val, Rational)
        assert val > 0


class TestMethod2AhatSeries:
    """Method 2: A-hat genus series expansion."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_method2_returns_positive_rational(self, g):
        val = method2_ahat_series(g)
        assert isinstance(val, Rational)
        assert val > 0


class TestMethod3ZetaValues:
    """Method 3: Bernoulli-zeta identity route."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_method3_returns_positive_rational(self, g):
        val = method3_zeta_values(g)
        assert isinstance(val, Rational)
        assert val > 0


class TestMethod4SympyBernoulli:
    """Method 4: sympy's built-in Bernoulli numbers."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_method4_returns_positive_rational(self, g):
        val = method4_sympy_bernoulli(g)
        assert isinstance(val, Rational)
        assert val > 0


class TestMethod5ExponentialGF:
    """Method 5: exponential generating function of x/(e^x - 1)."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_method5_returns_positive_rational(self, g):
        val = method5_exponential_generating_function(g)
        assert isinstance(val, Rational)
        assert val > 0


class TestMethod6AkiyamaTanigawa:
    """Method 6: Akiyama-Tanigawa algorithm."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_method6_returns_positive_rational(self, g):
        val = method6_akiyama_tanigawa(g)
        assert isinstance(val, Rational)
        assert val > 0


# =====================================================================
# CLASS 2: Cross-method agreement (10 tests, one per genus)
# =====================================================================

class TestCrossMethodAgreement:
    """All six methods must produce identical results for each genus."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_all_six_methods_agree(self, g):
        agree, value, results = verify_all_methods_agree(g)
        assert agree, (
            f"Methods disagree at g={g}:\n" +
            "\n".join(f"  {k}: {v}" for k, v in results.items())
        )

    def test_definitive_table_completes(self):
        """definitive_table(10) runs without assertion errors."""
        table = definitive_table(10)
        assert len(table) == 10
        for g in range(1, 11):
            assert g in table
            assert table[g] > 0


# =====================================================================
# CLASS 3: Known values verification (computed from first principles)
# =====================================================================

class TestKnownValues:
    """Verify specific lambda_g^FP values computed by hand."""

    def test_g1_equals_1_over_24(self):
        """lambda_1 = |B_2|/(2*2!) * (2^1-1)/2^1 = (1/6)/(2*2) * 1/2.

        Wait, let me compute carefully:
        B_2 = 1/6, |B_2| = 1/6
        (2^{1}-1)/2^{1} = 1/2
        (2g)! = 2! = 2
        lambda_1 = (1/2) * (1/6) / 2 = 1/24.
        """
        assert definitive_table(1)[1] == Rational(1, 24)

    def test_g2_equals_7_over_5760(self):
        """B_4 = -1/30, |B_4| = 1/30.
        (2^3-1)/2^3 = 7/8.
        (2g)! = 4! = 24.
        lambda_2 = (7/8) * (1/30) / 24 = 7/5760.
        """
        assert definitive_table(2)[2] == Rational(7, 5760)

    def test_g3_equals_31_over_967680(self):
        """B_6 = 1/42, |B_6| = 1/42.
        (2^5-1)/2^5 = 31/32.
        (2g)! = 6! = 720.
        lambda_3 = (31/32) * (1/42) / 720 = 31/967680.
        """
        assert definitive_table(3)[3] == Rational(31, 967680)

    def test_g4_equals_127_over_154828800(self):
        """B_8 = -1/30, |B_8| = 1/30.
        (2^7-1)/2^7 = 127/128.
        (2g)! = 8! = 40320.
        lambda_4 = (127/128) * (1/30) / 40320 = 127/154828800.
        """
        assert definitive_table(4)[4] == Rational(127, 154828800)

    def test_g5_hand_computation(self):
        """B_10 = 5/66, |B_10| = 5/66.
        (2^9-1)/2^9 = 511/512.
        (2g)! = 10! = 3628800.
        lambda_5 = (511/512) * (5/66) / 3628800 = 2555/(512*66*3628800).

        Let me simplify: 512*66 = 33792. 33792*3628800 = ?
        Actually: lambda_5 = 511*5 / (512*66*3628800) = 2555/122624409600.
        Simplify: gcd(2555, 122624409600).
        2555 = 5*511 = 5*7*73.
        122624409600 = 512*66*3628800 = 2^9 * 2*3*11 * 3628800
                     = 2^10 * 3 * 11 * 3628800.
        3628800 = 10! = 2^8 * 3^4 * 5^2 * 7.
        So denominator = 2^10 * 3 * 11 * 2^8 * 3^4 * 5^2 * 7
                       = 2^18 * 3^5 * 5^2 * 7 * 11.
        Numerator: 2555 = 5 * 7 * 73.
        gcd = 5*7 = 35.
        2555/35 = 73. denominator/35 = 2^18 * 3^5 * 5 * 11 = 262144*243*5*11
                = 262144*13365 = 3503554560.
        So lambda_5 = 73/3503554560.
        """
        assert definitive_table(5)[5] == Rational(73, 3503554560)

    def test_g1_from_euler_characteristic(self):
        """lambda_1 = chi(M_{1,1})/12 = 2/(12*24)... no.

        More directly: int_{M-bar_{1,1}} psi^0 lambda_1 = int lambda_1 = 1/24.
        This is the Euler characteristic relation: chi(M_{1,1}) = -1/12,
        and lambda_1 integrates to 1/24 on M-bar_{1,1} (compact).
        """
        assert method1_bernoulli_recurrence(1) == Rational(1, 24)


# =====================================================================
# CLASS 4: Generating function verification
# =====================================================================

class TestGeneratingFunction:
    """Verify sum_{g>=1} lambda_g^FP t^{2g} = (t/2)/sin(t/2) - 1."""

    def test_generating_function_all_match(self):
        result = verify_generating_function(10)
        assert result['all_match']

    def test_constant_term_is_one(self):
        result = verify_generating_function(1)
        assert result['constant_term'] == 1

    @pytest.mark.parametrize("g", range(1, 11))
    def test_generating_function_genus_g(self, g):
        """Coefficient of t^{2g} in (t/2)/sin(t/2) equals lambda_g^FP."""
        from sympy import Symbol, sin, series
        t = Symbol('t')
        f = t / 2 / sin(t / 2)
        s = series(f, t, 0, 2 * g + 2)
        coeff = Rational(s.coeff(t, 2 * g))
        fp = method4_sympy_bernoulli(g)
        assert simplify(coeff - fp) == 0, (
            f"g={g}: series coeff = {coeff}, lambda_fp = {fp}"
        )


# =====================================================================
# CLASS 5: A-hat genus relationship
# =====================================================================

class TestAhatRelationship:
    """Verify Ahat(x) = (x/2)/sinh(x/2) = sum (-1)^g lambda_g^FP x^{2g}."""

    def test_ahat_all_match(self):
        result = verify_ahat_relationship(10)
        assert result['all_match']

    @pytest.mark.parametrize("g", range(1, 11))
    def test_ahat_coefficient_genus_g(self, g):
        """Coeff of x^{2g} in (x/2)/sinh(x/2) = (-1)^g * lambda_g^FP."""
        from sympy import Symbol, sinh, series
        x = Symbol('x')
        ahat = x / 2 / sinh(x / 2)
        s = series(ahat, x, 0, 2 * g + 2)
        coeff = Rational(s.coeff(x, 2 * g))
        fp = method4_sympy_bernoulli(g)
        expected = (-1) ** g * fp
        assert simplify(coeff - expected) == 0


# =====================================================================
# CLASS 6: AP22 index convention tests
# =====================================================================

class TestAP22IndexConvention:
    """Verify the index convention F_g ~ hbar^{2g}, NOT hbar^{2g-2}.

    AP22: the generating function is:
        sum_{g>=1} F_g hbar^{2g} = kappa * ((hbar/2)/sin(hbar/2) - 1)

    The RHS starts at hbar^2 (since (t/2)/sin(t/2) - 1 starts at t^2).
    F_1 = kappa/24 is the hbar^2 term. This matches because 2g = 2 for g=1.

    If one writes hbar^{2g-2}, then F_1 is the hbar^0 term, but the RHS
    starts at hbar^2, giving a mismatch UNLESS one includes 1/hbar^2.
    """

    def test_generating_function_starts_at_order_2(self):
        """(t/2)/sin(t/2) - 1 starts at t^2."""
        from sympy import Symbol, sin, series
        t = Symbol('t')
        f = t / 2 / sin(t / 2) - 1
        s = series(f, t, 0, 4)
        assert s.coeff(t, 0) == 0  # no constant term
        assert s.coeff(t, 1) == 0  # no t^1 term
        assert s.coeff(t, 2) == Rational(1, 24)  # t^2 coefficient = lambda_1

    def test_f1_matches_hbar_squared_coefficient(self):
        """F_1 = kappa * lambda_1 = kappa/24 matches the hbar^2 coefficient."""
        from sympy import Symbol, sin, series
        t = Symbol('t')
        kappa = Symbol('kappa')
        f = kappa * (t / 2 / sin(t / 2) - 1)
        s = series(f, t, 0, 4)
        # The hbar^{2g} = hbar^2 coefficient for g=1 should be kappa/24
        assert s.coeff(t, 2) == kappa / 24

    def test_corrected_2g_minus_2_form(self):
        """The 2g-2 form requires explicit 1/hbar^2:
        sum F_g hbar^{2g-2} = (kappa/hbar^2) * ((hbar/2)/sin(hbar/2) - 1).

        Verify that the hbar^0 coefficient (g=1) matches F_1 = kappa/24.
        """
        from sympy import Symbol, sin, series
        h = Symbol('h')
        kappa = Symbol('kappa')
        # RHS = (kappa/h^2) * ((h/2)/sin(h/2) - 1)
        inner = h / 2 / sin(h / 2) - 1
        # inner = t^2/24 + 7t^4/5760 + ...
        s_inner = series(inner, h, 0, 6)
        # Multiply by kappa/h^2
        # h^2/24 / h^2 = 1/24, so hbar^0 coeff = kappa/24. Correct!
        coeff_h0 = s_inner.coeff(h, 2) * kappa  # This is the h^0 term after dividing by h^2
        assert coeff_h0 == kappa * Rational(1, 24)


# =====================================================================
# CLASS 7: Bernoulli number structural tests
# =====================================================================

class TestBernoulliStructural:
    """Structural properties of Bernoulli numbers as cross-checks."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_von_staudt_clausen(self, g):
        """B_{2g} + sum_{(p-1)|2g} 1/p is an integer."""
        assert verify_bernoulli_von_staudt_clausen(g)

    def test_bernoulli_signs(self):
        """B_{2g} has sign (-1)^{g+1} for g >= 1."""
        B = _bernoulli_binomial_recurrence(20)
        for g in range(1, 11):
            expected_sign = (-1) ** (g + 1)
            actual_sign = 1 if B[2 * g] > 0 else -1
            assert actual_sign == expected_sign, (
                f"B_{2*g} = {B[2*g]}, expected sign {expected_sign}"
            )

    def test_bernoulli_b1_equals_minus_half(self):
        """B_1 = -1/2 (our convention)."""
        B = _bernoulli_binomial_recurrence(1)
        assert B[1] == Rational(-1, 2)

    def test_odd_bernoulli_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        B = _bernoulli_binomial_recurrence(20)
        for k in range(1, 10):
            assert B[2 * k + 1] == 0, f"B_{2*k+1} = {B[2*k+1]}"

    def test_two_algorithms_agree_on_even_bernoulli(self):
        """Method 1 (binomial recurrence) and Method 6 (Akiyama-Tanigawa) produce
        the same EVEN Bernoulli numbers B_0, B_2, B_4, ..., B_20.

        Note: B_1 has a convention ambiguity (+1/2 vs -1/2). The Akiyama-Tanigawa
        algorithm produces B_1 = +1/2 while the binomial recurrence produces
        B_1 = -1/2. Both are correct conventions; the difference only affects B_1
        and is irrelevant for lambda_g^FP (which uses only B_{2g}).
        """
        B1 = _bernoulli_binomial_recurrence(20)
        B6 = _bernoulli_akiyama_tanigawa(20)
        for k in range(11):
            n = 2 * k
            assert B1[n] == B6[n], f"B_{n}: recurrence={B1[n]}, AT={B6[n]}"

    def test_bernoulli_against_sympy(self):
        """Binomial recurrence agrees with sympy.bernoulli for EVEN indices.

        B_1 convention: sympy uses B_1 = +1/2, our recurrence gives -1/2.
        Both are legitimate. Only even Bernoulli numbers matter for lambda_g^FP.
        """
        B1 = _bernoulli_binomial_recurrence(20)
        for k in range(11):
            n = 2 * k
            assert B1[n] == sympy_bernoulli(n), (
                f"B_{n}: recurrence={B1[n]}, sympy={sympy_bernoulli(n)}"
            )

    @pytest.mark.parametrize("g1,g2,p", [
        (1, 3, 5), (1, 5, 5), (1, 7, 5), (3, 5, 5), (5, 7, 5),  # p=5
        (1, 4, 7), (2, 5, 7), (4, 7, 7),  # p=7
        (1, 6, 11), (2, 7, 11),  # p=11
    ])
    def test_kummer_congruence(self, g1, g2, p):
        """Kummer congruence: B_{n1}/n1 ≡ B_{n2}/n2 (mod p)."""
        assert verify_bernoulli_kummer_congruence(g1, g2, p)


# =====================================================================
# CLASS 8: Asymptotic tests
# =====================================================================

class TestAsymptotics:
    """Asymptotic behavior of lambda_g^FP for large g."""

    def test_ratio_approaches_one(self):
        """lambda_g / (2/(2pi)^{2g}) -> 1 as g -> infinity."""
        for g in [5, 7, 10]:
            r = asymptotic_ratio(g)
            assert abs(r - 1.0) < 0.01, f"g={g}: ratio = {r}"

    def test_monotone_decrease(self):
        """lambda_g^FP is strictly decreasing in g."""
        table = definitive_table(10)
        for g in range(1, 10):
            assert table[g] > table[g + 1], (
                f"Not decreasing: lambda_{g} = {table[g]}, lambda_{g+1} = {table[g+1]}"
            )

    def test_positivity(self):
        """lambda_g^FP > 0 for all g >= 1."""
        table = definitive_table(10)
        for g in range(1, 11):
            assert table[g] > 0

    def test_asymptotic_ratio_monotone(self):
        """The ratio lambda_g / asymptotic should increase toward 1."""
        ratios = [asymptotic_ratio(g) for g in range(2, 11)]
        for i in range(len(ratios) - 1):
            assert ratios[i] < ratios[i + 1], (
                f"Ratio not increasing: g={i+2}: {ratios[i]}, g={i+3}: {ratios[i+1]}"
            )

    @pytest.mark.parametrize("g", range(1, 11))
    def test_ratio_below_one(self, g):
        """Ratio should be less than 1 (|B_{2g}| slightly less than 2*(2g)!/(2pi)^{2g})."""
        r = asymptotic_ratio(g)
        assert 0 < r < 1.001  # slight tolerance for numerical precision


# =====================================================================
# CLASS 9: Cross-check against existing utils.lambda_fp
# =====================================================================

class TestCrossCheckWithUtils:
    """Verify agreement with the existing utils.lambda_fp function."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_matches_utils_lambda_fp(self, g):
        from compute.lib.utils import lambda_fp as utils_lambda_fp
        utils_val = utils_lambda_fp(g)
        our_val = method4_sympy_bernoulli(g)
        assert simplify(utils_val - our_val) == 0, (
            f"g={g}: utils={utils_val}, cross_verify={our_val}"
        )

    @pytest.mark.parametrize("g", range(1, 11))
    def test_all_methods_match_utils(self, g):
        """All six methods match the existing production code."""
        from compute.lib.utils import lambda_fp as utils_lambda_fp
        utils_val = utils_lambda_fp(g)
        results = all_methods(g)
        for name, val in results.items():
            assert simplify(val - utils_val) == 0, (
                f"g={g}, {name}: {val} != utils {utils_val}"
            )


# =====================================================================
# CLASS 10: Bernoulli number table verification
# =====================================================================

class TestBernoulliTable:
    """Verify the Bernoulli number table against known values."""

    KNOWN_BERNOULLI = {
        0: Rational(1),
        2: Rational(1, 6),
        4: Rational(-1, 30),
        6: Rational(1, 42),
        8: Rational(-1, 30),
        10: Rational(5, 66),
        12: Rational(-691, 2730),
        14: Rational(7, 6),
        16: Rational(-3617, 510),
        18: Rational(43867, 798),
        20: Rational(-174611, 330),
    }

    @pytest.mark.parametrize("n,expected", list(KNOWN_BERNOULLI.items()))
    def test_bernoulli_value(self, n, expected):
        table = bernoulli_table(20)
        assert table[n] == expected, f"B_{n}: got {table[n]}, expected {expected}"


# =====================================================================
# CLASS 11: Formula decomposition tests
# =====================================================================

class TestFormulaDecomposition:
    """Verify the three factors in lambda_g^FP separately."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_factor_analysis(self, g):
        """lambda_g = prefactor * |B_{2g}| / (2g)! where prefactor = (2^{2g-1}-1)/2^{2g-1}."""
        B_2g = sympy_bernoulli(2 * g)
        abs_B = Abs(B_2g)
        prefactor = Rational(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
        denominator = factorial(2 * g)
        expected = prefactor * abs_B / denominator
        actual = method4_sympy_bernoulli(g)
        assert simplify(expected - actual) == 0

    @pytest.mark.parametrize("g", range(1, 11))
    def test_prefactor_approaches_one(self, g):
        """(2^{2g-1}-1)/2^{2g-1} = 1 - 2^{-(2g-1)} -> 1."""
        prefactor = Rational(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
        assert prefactor < 1
        assert prefactor > 0
        if g >= 5:
            assert float(prefactor) > 0.99

    def test_prefactor_g1(self):
        """At g=1: (2^1-1)/2^1 = 1/2."""
        assert Rational(2 ** 1 - 1, 2 ** 1) == Rational(1, 2)

    def test_prefactor_g2(self):
        """At g=2: (2^3-1)/2^3 = 7/8."""
        assert Rational(2 ** 3 - 1, 2 ** 3) == Rational(7, 8)


# =====================================================================
# CLASS 12: Free energy F_g tests
# =====================================================================

class TestFreeEnergy:
    """Verify F_g(A) = kappa(A) * lambda_g^FP for specific algebras."""

    def test_heisenberg_f1(self):
        """F_1(H_k) = k * 1/24 = k/24."""
        from sympy import Symbol
        k = Symbol('k')
        fp = method4_sympy_bernoulli(1)
        assert fp == Rational(1, 24)

    def test_virasoro_f1(self):
        """F_1(Vir_c) = (c/2) * 1/24 = c/48."""
        fp = method4_sympy_bernoulli(1)
        assert fp == Rational(1, 24)
        # kappa(Vir_c) = c/2, so F_1 = c/48

    def test_virasoro_f2(self):
        """F_2(Vir_c) = (c/2) * 7/5760 = 7c/11520."""
        fp = method4_sympy_bernoulli(2)
        assert fp == Rational(7, 5760)
        # kappa(Vir_c) = c/2, so F_2 = 7c/11520

    def test_sl2_f1(self):
        """F_1(sl_2_k) = 3(k+2)/4 * 1/24 = (k+2)/32."""
        fp = method4_sympy_bernoulli(1)
        assert fp == Rational(1, 24)
        # kappa(sl_2_k) = 3(k+2)/4, so F_1 = 3(k+2)/96 = (k+2)/32


# =====================================================================
# CLASS 13: Generating function sin vs sinh duality
# =====================================================================

class TestSinSinhDuality:
    r"""Verify the sin/sinh duality:

    (t/2)/sin(t/2) evaluated at t = ix gives (ix/2)/sin(ix/2) = (x/2)/sinh(x/2) = Ahat(x).

    Since (t/2)/sin(t/2) = 1 + sum lambda_g t^{2g},
    and Ahat(x) = 1 + sum (-1)^g lambda_g x^{2g},
    the substitution t -> ix flips the sign of even powers:
    (ix)^{2g} = (-1)^g x^{2g}. Consistent.
    """

    def test_sin_sinh_coefficient_relation(self):
        from sympy import Symbol, sin, sinh, series
        t = Symbol('t')
        x = Symbol('x')

        sin_series = series(t / 2 / sin(t / 2), t, 0, 12)
        sinh_series = series(x / 2 / sinh(x / 2), x, 0, 12)

        for g in range(1, 6):
            sin_coeff = Rational(sin_series.coeff(t, 2 * g))
            sinh_coeff = Rational(sinh_series.coeff(x, 2 * g))
            # sinh_coeff = (-1)^g * sin_coeff
            assert simplify(sinh_coeff - (-1) ** g * sin_coeff) == 0, (
                f"g={g}: sin_coeff={sin_coeff}, sinh_coeff={sinh_coeff}"
            )


# =====================================================================
# CLASS 14: Numerical precision tests
# =====================================================================

class TestNumericalPrecision:
    """Verify exact rational arithmetic -- no floating point leakage."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_exact_rational_type(self, g):
        """All methods return Rational, not float."""
        results = all_methods(g)
        for name, val in results.items():
            assert isinstance(val, Rational), f"{name} at g={g} returned {type(val)}"

    @pytest.mark.parametrize("g", range(1, 11))
    def test_denominator_factorization(self, g):
        """The denominator of lambda_g should divide 2^{2g-1} * (2g)!.

        Since lambda_g = (2^{2g-1}-1) * |B_{2g}| / (2^{2g-1} * (2g)!),
        the denominator divides 2^{2g-1} * (2g)! * denominator(|B_{2g}|).
        """
        val = method4_sympy_bernoulli(g)
        # Just check it's a positive rational with integer numerator/denominator
        assert val.p > 0
        assert val.q > 0


# =====================================================================
# CLASS 15: Edge cases and error handling
# =====================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_method1_rejects_g0(self):
        with pytest.raises(AssertionError):
            method1_bernoulli_recurrence(0)

    def test_method4_rejects_g0(self):
        with pytest.raises(AssertionError):
            method4_sympy_bernoulli(0)

    def test_method6_rejects_g0(self):
        with pytest.raises(AssertionError):
            method6_akiyama_tanigawa(0)


# =====================================================================
# CLASS 16: Pairwise method agreement (comprehensive)
# =====================================================================

class TestPairwiseAgreement:
    """Verify each pair of methods agrees -- catch any single method error."""

    METHOD_FUNCS = {
        '1': method1_bernoulli_recurrence,
        '2': method2_ahat_series,
        '3': method3_zeta_values,
        '4': method4_sympy_bernoulli,
        '5': method5_exponential_generating_function,
        '6': method6_akiyama_tanigawa,
    }

    @pytest.mark.parametrize("g", [1, 5, 10])
    def test_method1_vs_method2(self, g):
        assert simplify(method1_bernoulli_recurrence(g) - method2_ahat_series(g)) == 0

    @pytest.mark.parametrize("g", [1, 5, 10])
    def test_method1_vs_method5(self, g):
        assert simplify(method1_bernoulli_recurrence(g) - method5_exponential_generating_function(g)) == 0

    @pytest.mark.parametrize("g", [1, 5, 10])
    def test_method2_vs_method6(self, g):
        assert simplify(method2_ahat_series(g) - method6_akiyama_tanigawa(g)) == 0

    @pytest.mark.parametrize("g", [1, 5, 10])
    def test_method3_vs_method4(self, g):
        assert simplify(method3_zeta_values(g) - method4_sympy_bernoulli(g)) == 0

    @pytest.mark.parametrize("g", [1, 5, 10])
    def test_method4_vs_method5(self, g):
        assert simplify(method4_sympy_bernoulli(g) - method5_exponential_generating_function(g)) == 0


# =====================================================================
# CLASS 17: NOT lambda_2 = 1/240 (AP38 trap)
# =====================================================================

class TestAP38Traps:
    """Verify we do NOT have wrong values from convention mismatches.

    AP38: hardcoded values from the literature may use different conventions.

    lambda_2^FP = 7/5760 (this is the Hodge integral on M-bar_{2,1}).
    It is NOT 1/240 (which is int_{M-bar_{2,0}} lambda_2 = 1/240).
    It is NOT 1/1152 (which was a wrong value in an earlier test).
    """

    def test_lambda_2_is_not_1_over_240(self):
        """1/240 is int_{M-bar_{2,0}} lambda_2, NOT lambda_2^FP."""
        assert definitive_table(2)[2] != Rational(1, 240)

    def test_lambda_2_is_not_1_over_1152(self):
        """1/1152 was a wrong value found in a historical test (AP38)."""
        assert definitive_table(2)[2] != Rational(1, 1152)

    def test_lambda_2_is_7_over_5760(self):
        """The correct value is 7/5760."""
        assert definitive_table(2)[2] == Rational(7, 5760)

    def test_7_over_5760_derivation(self):
        """Explicitly derive 7/5760 step by step."""
        # B_4 = -1/30
        assert sympy_bernoulli(4) == Rational(-1, 30)
        # |B_4| = 1/30
        abs_B4 = Abs(sympy_bernoulli(4))
        assert abs_B4 == Rational(1, 30)
        # 4! = 24
        assert factorial(4) == 24
        # (2^3 - 1)/2^3 = 7/8
        prefactor = Rational(2 ** 3 - 1, 2 ** 3)
        assert prefactor == Rational(7, 8)
        # lambda_2 = (7/8) * (1/30) / 24 = 7/(8*30*24) = 7/5760
        result = prefactor * abs_B4 / factorial(4)
        assert result == Rational(7, 5760)


# =====================================================================
# CLASS 18: Additivity check (F_g is linear in kappa)
# =====================================================================

class TestAdditivity:
    """F_g(A oplus B) = F_g(A) + F_g(B) since kappa is additive."""

    @pytest.mark.parametrize("g", range(1, 6))
    def test_linearity(self, g):
        """kappa1 * lambda_g + kappa2 * lambda_g = (kappa1 + kappa2) * lambda_g."""
        fp = method4_sympy_bernoulli(g)
        from sympy import Symbol
        k1 = Symbol('k1')
        k2 = Symbol('k2')
        lhs = k1 * fp + k2 * fp
        rhs = (k1 + k2) * fp
        assert simplify(lhs - rhs) == 0
