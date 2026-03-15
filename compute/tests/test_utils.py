"""Tests for compute/lib/utils.py — graded spaces, signs, Bernoulli numbers."""

import pytest
from sympy import Rational, bernoulli

from compute.lib.utils import (
    GradedVectorSpace,
    ChainComplex,
    koszul_sign,
    lambda_fp,
    F_g,
    partition_number,
)
from sympy import Matrix


class TestGradedVectorSpace:
    def test_basic(self):
        V = GradedVectorSpace(dims={0: 3, 1: 2}, name="V")
        assert V.dim(0) == 3
        assert V.dim(1) == 2
        assert V.dim(5) == 0
        assert V.total_dim() == 5

    def test_euler_char(self):
        V = GradedVectorSpace(dims={0: 3, 1: 2, 2: 1})
        # 3 - 2 + 1 = 2
        assert V.euler_char() == 2

    def test_desuspension(self):
        """s^{-1}V = V[1]: degree k of s^{-1}V = degree k+1 of V."""
        V = GradedVectorSpace(dims={0: 1, 1: 3})
        sV = V.desuspend()
        # V[1]^k = V^{k+1}, so V[1]^{-1} = V^0 = 1, V[1]^0 = V^1 = 3
        assert sV.dim(-1) == 1
        assert sV.dim(0) == 3

    def test_suspension(self):
        """sV = V[-1]: degree k of sV = degree k-1 of V."""
        V = GradedVectorSpace(dims={0: 1, 1: 3})
        sV = V.suspend()
        assert sV.dim(1) == 1
        assert sV.dim(2) == 3


class TestChainComplex:
    def test_d_squared_zero(self):
        """Simple 2-term complex with d^2 = 0."""
        spaces = GradedVectorSpace(dims={0: 2, 1: 2, 2: 1})
        d0 = Matrix([[1, 0], [0, 1]])  # 2x2
        d1 = Matrix([[0, 0]])          # 1x2, composed d1*d0 should be zero
        # Actually d1*d0 = [[0,0]] * [[1,0],[0,1]] ... dimensions wrong
        # Let me fix: d0: C^0(2-dim) -> C^1(2-dim), d1: C^1(2-dim) -> C^2(1-dim)
        d0 = Matrix([[1, 0], [0, 1]])  # 2x2: C^0 -> C^1
        d1 = Matrix([[1, -1]])          # 1x2: C^1 -> C^2
        # d1 * d0 = [[1,-1]] * [[1,0],[0,1]] = [[1,-1]] != 0
        # Fix: make d^2 = 0
        d0 = Matrix([[1, 1], [-1, -1]])  # rank 1
        d1 = Matrix([[1, 1]])            # rank 1
        # d1 * d0 = [[1,1]] * [[1,1],[-1,-1]] = [[0,0]] ✓

        cx = ChainComplex(
            spaces=spaces,
            differentials={0: d0, 1: d1},
        )
        results = cx.check_d_squared()
        assert all(passes for _, passes in results)

    def test_cohomology(self):
        """Compute cohomology of a simple complex."""
        # 0 -> C^1 -d-> C^1 -> 0 with d = identity
        spaces = GradedVectorSpace(dims={0: 1, 1: 1})
        d0 = Matrix([[1]])  # isomorphism
        cx = ChainComplex(spaces=spaces, differentials={0: d0})
        # H^0 = ker(d0) = 0, H^1 = C^1 / im(d0) = 0
        assert cx.cohomology_dim(0) == 0
        assert cx.cohomology_dim(1) == 0


class TestKoszulSign:
    def test_identity(self):
        """Identity permutation has sign +1."""
        assert koszul_sign([1, 2], [0, 1]) == 1

    def test_swap_odd(self):
        """Swapping two odd-degree elements: (-1)^{1*1} = -1."""
        assert koszul_sign([1, 1], [1, 0]) == -1

    def test_swap_even(self):
        """Swapping two even-degree elements: (-1)^{0*0} = +1."""
        assert koszul_sign([2, 2], [1, 0]) == 1

    def test_mixed(self):
        """Swapping even and odd: (-1)^{1*2} = +1."""
        assert koszul_sign([1, 2], [1, 0]) == 1


class TestBernoulli:
    def test_lambda_fp_genus1(self):
        """lambda_1 = (2^1-1)/2^1 * |B_2|/2! = (1/2)*(1/6)/2 = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2 = (2^3-1)/2^3 * |B_4|/4! = (7/8)*(1/30)/24 = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3 = (2^5-1)/2^5 * |B_6|/6! = (31/32)*(1/42)/720 = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_F_g_heisenberg(self):
        """F_1(H_kappa) = kappa/24."""
        from sympy import Symbol
        kappa = Symbol("kappa")
        assert F_g(kappa, 1) == kappa / 24


class TestLambdaFPExtended:
    """Verify lambda_fp(g) for g=1..10 against Bernoulli number formula.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """

    def test_lambda_fp_through_10(self):
        """Compute lambda_fp(g) for g=1..10 and verify via generating function."""
        from sympy import bernoulli as bern, factorial as fac, Abs
        for g in range(1, 11):
            B_2g = bern(2 * g)
            expected = (2**(2*g - 1) - 1) * abs(B_2g) / (2**(2*g - 1) * fac(2*g))
            computed = lambda_fp(g)
            assert computed == expected, f"lambda_fp({g}) = {computed} != {expected}"

    def test_lambda_fp_known_exact(self):
        """Check exact rational values for lambda_1 through lambda_5."""
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        assert lambda_fp(3) == Rational(31, 967680)
        # lambda_4 = (2^7 - 1)/2^7 * |B_8|/8! = 127/128 * (1/30) / 40320
        assert lambda_fp(4) == Rational(127, 154828800)
        # lambda_5
        assert lambda_fp(5) == Rational(73, 3503554560)

    def test_all_positive(self):
        for g in range(1, 11):
            assert lambda_fp(g) > 0

    def test_decreasing(self):
        """lambda_fp values are strictly decreasing."""
        for g in range(1, 10):
            assert lambda_fp(g) > lambda_fp(g + 1)


class TestPartition:
    def test_small_values(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11."""
        assert partition_number(0) == 1
        assert partition_number(1) == 1
        assert partition_number(2) == 2
        assert partition_number(3) == 3
        assert partition_number(4) == 5
        assert partition_number(5) == 7
        assert partition_number(6) == 11

    def test_negative(self):
        assert partition_number(-1) == 0
