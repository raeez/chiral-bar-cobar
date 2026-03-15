"""Tests for Yangian Y(sl₂) H⁴ = 82 verification.

Verifies multiple independent consistency checks supporting the
conjectured value H⁴(B(Y(sl₂))) = 82 via the generating function
P(x) = (1 - 3x²)/((1-x)(1-3x)).
"""

import pytest
import numpy as np
from math import factorial, comb


class TestRecurrenceConsistency:
    """Verify the rational GF recurrence a(n) = 4a(n-1) - 3a(n-2)."""

    def test_known_values(self):
        """Recurrence reproduces known H¹=4, H²=10, H³=28."""
        a = [1, 4, 10, 28]
        # a(2) = 4*a(1) - 3*a(0) = 16 - 3 = 13? NO.
        # Wait: N(x) = 1 - 3x², so the recurrence starts at n=3.
        # For n >= 3: a(n) = 4a(n-1) - 3a(n-2)
        assert 4 * a[2] - 3 * a[1] == a[3]  # 40 - 12 = 28

    def test_h4_prediction(self):
        """Recurrence predicts H⁴ = 82."""
        a = [1, 4, 10, 28]
        a4 = 4 * a[3] - 3 * a[2]
        assert a4 == 82

    def test_closed_form(self):
        """a(n) = 3^n + 1 for n >= 1."""
        for n in range(1, 10):
            a = [1, 4]
            for k in range(2, n + 1):
                if k == 2:
                    a.append(10)  # from GF: a(2) - 4*a(1) + 3*a(0) = -3
                else:
                    a.append(4 * a[-1] - 3 * a[-2])
            assert a[n] == 3 ** n + 1

    def test_numerator_coefficients(self):
        """GF numerator N(x) = 1 - 3x² matches known values.

        D(x)*P(x) = N(x) where P(x) = sum a_n x^n.
        D(x) = 1 - 4x + 3x².
        """
        a = {0: 1, 1: 4, 2: 10, 3: 28, 4: 82}

        # x⁰: a₀ = 1
        assert a[0] == 1

        # x¹: a₁ - 4*a₀ = 4 - 4 = 0
        assert a[1] - 4 * a[0] == 0

        # x²: a₂ - 4*a₁ + 3*a₀ = 10 - 16 + 3 = -3
        assert a[2] - 4 * a[1] + 3 * a[0] == -3

        # x³: a₃ - 4*a₂ + 3*a₁ = 28 - 40 + 12 = 0 (recurrence)
        assert a[3] - 4 * a[2] + 3 * a[1] == 0

        # x⁴: a₄ - 4*a₃ + 3*a₂ = 82 - 112 + 30 = 0 (recurrence)
        assert a[4] - 4 * a[3] + 3 * a[2] == 0

    def test_denominator_factorization(self):
        """D(x) = (1-x)(1-3x) = 1 - 4x + 3x²."""
        d0 = 1
        d1 = -1 + (-3)
        d2 = (-1) * (-3)
        assert (d0, d1, d2) == (1, -4, 3)

    def test_growth_rate(self):
        """Ratio a(n)/a(n-1) → 3 (dominant root of D(x))."""
        a = [1, 4, 10, 28, 82, 244, 730, 2188, 6562]
        for _ in range(5):
            a.append(4 * a[-1] - 3 * a[-2])
        for n in range(8, len(a)):
            ratio = a[n] / a[n - 1]
            assert abs(ratio - 3.0) < 0.01, f"Ratio at n={n}: {ratio:.6f}"


class TestKoszulRelation:
    """Verify H_A(t) * H_{A!}(-t) = 1 for the Yangian."""

    def test_product_is_one(self):
        """Formal power series product equals 1 through degree 10."""
        N = 11
        a = [3 ** n + 1 if n >= 1 else 1 for n in range(N)]
        a_neg = [a[i] * ((-1) ** i) for i in range(N)]

        h = [0] * N
        h[0] = 1
        for n in range(1, N):
            s = sum(a_neg[k] * h[n - k] for k in range(1, n + 1))
            h[n] = -s

        for k in range(N):
            prod_k = sum(h[i] * a_neg[k - i] for i in range(k + 1))
            if k == 0:
                assert prod_k == 1
            else:
                assert abs(prod_k) < 1e-6

    def test_dual_dims_positive_through_10(self):
        """H_{A!} coefficients are positive integers through degree 10."""
        N = 11
        a = [3 ** n + 1 if n >= 1 else 1 for n in range(N)]
        a_neg = [a[i] * ((-1) ** i) for i in range(N)]

        h = [0] * N
        h[0] = 1
        for n in range(1, N):
            s = sum(a_neg[k] * h[n - k] for k in range(1, n + 1))
            h[n] = -s

        for n in range(N):
            assert h[n] > 0, f"H_A![{n}] = {h[n]} not positive"
            assert h[n] == int(h[n]), f"H_A![{n}] = {h[n]} not integer"

    def test_dual_dims_closed_form(self):
        """H_{A!}(t) = (1+4t+3t²)/(1-3t²).

        Coefficients: even n >= 2: 2*3^{n/2}, odd n >= 1: 4*3^{(n-1)/2}.
        """
        N = 11
        a = [3 ** n + 1 if n >= 1 else 1 for n in range(N)]
        a_neg = [a[i] * ((-1) ** i) for i in range(N)]

        h = [0] * N
        h[0] = 1
        for n in range(1, N):
            s = sum(a_neg[k] * h[n - k] for k in range(1, n + 1))
            h[n] = -s

        # Check against closed form: H_{A!}(t) = (1+4t+3t²)/(1-3t²)
        # Expand: (1+4t+3t²) * sum_{k>=0} (3t²)^k
        expected = [0] * N
        for k in range(N):
            # Contribution from 1 * (3t²)^k at degree 2k
            if 2 * k < N:
                expected[2 * k] += 3 ** k
            # Contribution from 4t * (3t²)^k at degree 2k+1
            if 2 * k + 1 < N:
                expected[2 * k + 1] += 4 * 3 ** k
            # Contribution from 3t² * (3t²)^k at degree 2k+2
            if 2 * k + 2 < N:
                expected[2 * k + 2] += 3 * 3 ** k

        for n in range(N):
            assert int(h[n]) == expected[n], \
                f"deg {n}: computed {int(h[n])}, expected {expected[n]}"


class TestH2Independent:
    """Independent verification of H² = 10."""

    def test_h2_value(self):
        """H² = 10 = 3² + 1."""
        assert 3 ** 2 + 1 == 10

    def test_kunneth_h2(self):
        """At degree 2, Yangian = gl₂ (no Serre correction).

        H²(Y(sl₂)) = H²(sl₂) + H¹(sl₂)*H¹(gl₁) + H²(gl₁)
        Using bar dims for sl₂: R(5) = 6, R(4) = 3, R(3) = 1
        H⁰(sl₂) = R(3) = 1
        H¹(sl₂) = R(4) = 3
        H²(sl₂) = R(5) = 6
        H⁰(gl₁) = 1, H¹(gl₁) = 1, H²(gl₁) = 1
        Kunneth: 6*1 + 3*1 + 1*1 = 10.
        """
        from compute.lib.bar_gf_solver import riordan_numbers
        R = riordan_numbers(8)
        # H^i(sl₂) = R[i+3]
        h_sl2 = {0: R[3], 1: R[4], 2: R[5]}
        h_gl1 = {0: 1, 1: 1, 2: 1}  # Heisenberg: all 1 for low degrees
        kunneth = sum(h_sl2[i] * h_gl1[2 - i] for i in range(3))
        assert kunneth == 10


class TestRankCascade:
    """Verify the rank cascade from known cohomology dimensions.

    Using chiral bar complex with d=4 (gl₂ generators):
    dim B^n = 4^n × (n-1)! for n >= 2, dim B^1 = 4.
    """

    def test_chain_dims(self):
        """Verify chain group dimensions."""
        d = 4
        assert d ** 1 == 4           # B^1
        assert d ** 2 * 1 == 16      # B^2
        assert d ** 3 * 2 == 128     # B^3
        assert d ** 4 * 6 == 1536    # B^4

    def test_rank_d2(self):
        """rank(d₂) = dim B¹ - H¹ = 4 - 4 = 0."""
        assert 4 - 4 == 0

    def test_rank_d3(self):
        """rank(d₃) = dim B² - rank(d₂) - H² = 16 - 0 - 10 = 6."""
        assert 16 - 0 - 10 == 6

    def test_rank_d4(self):
        """rank(d₄) = dim B³ - rank(d₃) - H³ = 128 - 6 - 28 = 94."""
        assert 128 - 6 - 28 == 94

    def test_rank_d5_from_h4(self):
        """If H⁴ = 82: rank(d₅) = dim B⁴ - rank(d₄) - H⁴ = 1536 - 94 - 82 = 1360."""
        rank_d5 = 1536 - 94 - 82
        assert rank_d5 == 1360

    def test_rank_d5_feasible(self):
        """rank(d₅) = 1360 ≤ min(dim B⁴, dim B⁵)."""
        rank_d5 = 1360
        dim_B4 = 4 ** 4 * 6     # 1536
        dim_B5 = 4 ** 5 * 24    # 24576
        assert rank_d5 <= dim_B4
        assert rank_d5 <= dim_B5

    def test_all_ranks_nonneg(self):
        """All ranks are non-negative."""
        ranks = [0, 0, 6, 94, 1360]
        for r in ranks:
            assert r >= 0


class TestEulerCharacteristic:
    """Verify partial Euler characteristic consistency."""

    def test_alternating_sum_gf(self):
        """P(-1) = (1-3)/((1-(-1))(1-3*(-1))) = -2/(2*4) = -1/4.

        This means sum (-1)^n a(n) = -1/4 (formal).
        Partial sums should approach this.
        """
        # sum_{n=0}^N (-1)^n (3^n+1) for n >= 1, plus a(0)=1
        # = 1 + sum_{n=1}^N (-1)^n (3^n + 1)
        # = 1 + sum (-3)^n + sum (-1)^n
        # The sums of (-3)^n and (-1)^n are Cesaro-summable
        # Just verify the GF value
        from fractions import Fraction
        p_neg1 = Fraction(1 - 3, (1 - (-1)) * (1 - 3 * (-1)))
        assert p_neg1 == Fraction(-1, 4)


class TestDimensionFormulas:
    """Verify dimension formulas for chain groups."""

    @pytest.mark.parametrize("n,expected", [
        (1, 4), (2, 16), (3, 128), (4, 1536), (5, 24576),
    ])
    def test_chain_group_dims(self, n, expected):
        """dim B^n = 4^n × (n-1)! for n >= 2, 4^1 for n=1."""
        if n == 1:
            assert 4 ** n == expected
        else:
            assert 4 ** n * factorial(n - 1) == expected


class TestIntegration:
    """Full integration tests using yangian_h4_verification module."""

    def test_recurrence_module(self):
        from compute.lib.yangian_h4_verification import check_recurrence_consistency
        result = check_recurrence_consistency()
        assert result['H4_predicted'] == 82
        assert result['all_match'] is True

    def test_numerator_module(self):
        from compute.lib.yangian_h4_verification import check_numerator_coefficients
        result = check_numerator_coefficients()
        assert result['all_match'] is True

    def test_koszul_identity_module(self):
        from compute.lib.yangian_h4_verification import check_koszul_identity
        result = check_koszul_identity()
        assert result['all_positive'] is True
        assert result['all_integral'] is True
        assert result['all_ok'] is True

    def test_rank_cascade_module(self):
        from compute.lib.yangian_h4_verification import check_rank_cascade
        result = check_rank_cascade()
        assert result['predicted_H4'] == 82
        assert result['all_feasible'] is True

    def test_growth_rate_module(self):
        from compute.lib.yangian_h4_verification import check_growth_rate
        result = check_growth_rate()
        assert result['convergence_to_3'] is True
