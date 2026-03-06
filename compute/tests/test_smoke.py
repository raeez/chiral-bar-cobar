"""Cross-module smoke tests.

Verify that every public function in compute.lib can be called
with minimal valid inputs and produces non-trivial results.
"""

import pytest


class TestCoreTypes:
    def test_graded_vector_space(self):
        from compute.lib import GradedVectorSpace
        V = GradedVectorSpace({0: 1, 1: 3, 2: 5})
        assert V.dim(0) == 1
        assert V.dim(1) == 3

    def test_chain_complex(self):
        from compute.lib import GradedVectorSpace, ChainComplex
        spaces = GradedVectorSpace({0: 1, 1: 3, 2: 5})
        cc = ChainComplex(spaces)
        assert cc.spaces.dim(1) == 3

    def test_ope_algebra(self):
        from compute.lib import OPEAlgebra, Generator
        T = Generator("T", 2, 0)
        alg = OPEAlgebra([T], {}, name="test")
        assert len(alg.generators) == 1


class TestAlgebraConstructors:
    def test_heisenberg(self):
        from compute.lib import heisenberg_algebra
        H = heisenberg_algebra()
        assert len(H.generators) == 1

    def test_sl2(self):
        from compute.lib import sl2_algebra
        g = sl2_algebra()
        assert len(g.generators) == 3

    def test_virasoro(self):
        from compute.lib import virasoro_algebra
        V = virasoro_algebra()
        assert len(V.generators) == 1

    def test_free_fermion(self):
        from compute.lib import free_fermion_algebra
        F = free_fermion_algebra()
        assert len(F.generators) >= 1


class TestLieAlgebra:
    def test_cartan_data(self):
        from compute.lib import cartan_data
        cd = cartan_data("A", 1)
        assert cd.dim == 3
        assert cd.h_dual == 2

    def test_sugawara_c(self):
        from compute.lib import sugawara_c
        from sympy import Symbol
        k = Symbol('k')
        c = sugawara_c("A", 1, k)
        assert c.subs(k, 1) == 1

    def test_ff_dual_level(self):
        from compute.lib import ff_dual_level
        from sympy import Symbol, simplify
        k = Symbol('k')
        kp = ff_dual_level("A", 1, k)
        assert simplify(kp - (-k - 4)) == 0

    def test_kappa_km(self):
        from compute.lib import kappa_km
        from sympy import Symbol
        k = Symbol('k')
        kap = kappa_km("A", 1, k)
        assert kap is not None


class TestRegistries:
    def test_algebra_registry(self):
        from compute.lib import ALGEBRA_REGISTRY
        assert len(ALGEBRA_REGISTRY) == 11

    def test_known_bar_dims(self):
        from compute.lib import KNOWN_BAR_DIMS
        assert "sl2" in KNOWN_BAR_DIMS
        assert KNOWN_BAR_DIMS["sl2"][1] == 3

    def test_verify_bar_dim(self):
        from compute.lib import verify_bar_dim
        ok, msg = verify_bar_dim("sl2", 1, 3)
        assert ok


class TestKoszulHilbert:
    def test_riordan(self):
        from compute.lib import riordan
        # R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6
        assert riordan(4) == 3
        assert riordan(5) == 6
        assert riordan(6) == 15

    def test_motzkin(self):
        from compute.lib import motzkin
        assert motzkin(0) == 1
        assert motzkin(3) == 4
        assert motzkin(4) == 9

    def test_verify_koszul_sym_ext(self):
        from compute.lib import verify_koszul
        from math import comb
        h_sym = [comb(k + 2, k) for k in range(5)]
        h_ext = [comb(3, k) for k in range(4)] + [0]
        assert verify_koszul(h_sym, h_ext)


class TestOrlikSolomon:
    def test_os_dimension(self):
        from compute.lib import os_dimension
        assert os_dimension(2, 1) == 1
        assert os_dimension(3, 2) == 2

    def test_os_basis(self):
        from compute.lib import os_basis
        b = os_basis(3, 2)
        assert len(b) == 2

    def test_residue_map(self):
        from compute.lib import residue_map
        r = residue_map(3, 2, 0, 1)
        assert r is not None


class TestUtilities:
    def test_partition_number(self):
        from compute.lib import partition_number
        assert partition_number(0) == 1
        assert partition_number(5) == 7

    def test_lambda_fp(self):
        from compute.lib import lambda_fp
        from fractions import Fraction
        lam1 = lambda_fp(1)
        assert lam1 == Fraction(1, 24)

    def test_F_g(self):
        from compute.lib import F_g
        from fractions import Fraction
        f1 = F_g(1, 1)
        assert f1 == Fraction(1, 24)
