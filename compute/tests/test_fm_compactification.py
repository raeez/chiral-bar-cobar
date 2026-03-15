"""Tests for FM compactification and configuration space forms."""

import pytest
from compute.lib.fm_compactification import (
    poincare_polynomial,
    os_dim,
    os_top_dim,
    euler_char,
    arnold_relation_count,
    fm_boundary_strata_count,
    fm_codim1_strata,
    mbar_05_data,
    normal_bundle_diagonal,
    verify_fm,
)


class TestPoincare:
    def test_conf2(self):
        assert poincare_polynomial(2) == [1, 1]

    def test_conf3(self):
        assert poincare_polynomial(3) == [1, 3, 2]

    def test_conf4(self):
        assert poincare_polynomial(4) == [1, 6, 11, 6]

    def test_conf5(self):
        assert poincare_polynomial(5) == [1, 10, 35, 50, 24]


class TestOSDim:
    def test_top_degrees(self):
        for n in range(2, 7):
            from math import factorial
            assert os_top_dim(n) == factorial(n - 1)

    def test_h0_always_1(self):
        for n in range(1, 6):
            assert os_dim(n, 0) == 1

    def test_specific_values(self):
        assert os_dim(4, 2) == 11
        assert os_dim(5, 3) == 50


class TestArnold:
    def test_triple_count(self):
        from math import comb
        for n in range(3, 8):
            assert arnold_relation_count(n) == comb(n, 3)


class TestFMStrata:
    def test_fm3(self):
        assert fm_boundary_strata_count(3) == 4

    def test_fm4(self):
        assert fm_boundary_strata_count(4) == 11

    def test_strata_list(self):
        strata = fm_codim1_strata(3)
        assert len(strata) == 4  # {12}, {13}, {23}, {123}


class TestEuler:
    def test_conf1(self):
        assert euler_char(1) == 1

    def test_conf_ge2(self):
        for n in range(2, 6):
            assert euler_char(n) == 0


class TestSpecialCases:
    def test_mbar05(self):
        data = mbar_05_data()
        assert data["del_pezzo_degree"] == 5
        assert data["dim_H2"] == 5

    def test_normal_bundle(self):
        nb = normal_bundle_diagonal()
        assert "tangent" in nb.lower()


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_fm().items():
            assert ok, f"Failed: {name}"
