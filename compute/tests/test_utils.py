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
        """lambda_1 = |B_2| / (2 * 0!) = (1/6) / 2 = 1/12."""
        assert lambda_fp(1) == Rational(1, 12)

    def test_lambda_fp_genus2(self):
        """lambda_2 = |B_4| / (4 * 2!) = (1/30) / 8 = 1/240."""
        assert lambda_fp(2) == Rational(1, 240)

    def test_lambda_fp_genus3(self):
        """lambda_3 = |B_6| / (6 * 4!) = (1/42) / 144 = 1/6048."""
        assert lambda_fp(3) == Rational(1, 6048)

    def test_F_g_heisenberg(self):
        """F_1(H_kappa) = kappa/12."""
        from sympy import Symbol
        kappa = Symbol("kappa")
        assert F_g(kappa, 1) == kappa / 12


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
