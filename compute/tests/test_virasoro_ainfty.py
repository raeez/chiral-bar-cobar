"""Tests for Virasoro A-infinity structure.

Ground truth from comp:virasoro-degree3, comp:virasoro-curvature,
CLAUDE.md curved A-infinity section.
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.virasoro_ainfty import (
    virasoro_m0,
    virasoro_m1_squared,
    virasoro_m2,
    virasoro_m3_from_bar,
    virasoro_m3_weight,
    curved_ainfty_relation,
    virasoro_curved_regimes,
    arnold_as_ainfty,
    verify_virasoro_ainfty,
)

c = Symbol('c')


class TestM0:
    def test_value(self):
        assert virasoro_m0() == c / 2

    def test_uncurved_at_c0(self):
        assert virasoro_m0().subs(c, 0) == 0


class TestM1Squared:
    def test_on_generator(self):
        """m_1^2(T) = [m_0, T] = 0 since m_0 is scalar."""
        result = virasoro_m1_squared()
        assert result["m1_squared_on_T"] == 0


class TestM2:
    def test_TT(self):
        result = virasoro_m2("T", "T")
        assert result["T"] == 2
        assert result["dT"] == 1

    def test_T_dT(self):
        result = virasoro_m2("T", "dT")
        assert result["dT"] == 3
        assert result["d2T"] == 1

    def test_dT_T(self):
        result = virasoro_m2("dT", "T")
        assert result["dT"] == 3
        assert result["d2T"] == 2

    def test_asymmetry(self):
        """m_2 is not symmetric: m_2(T,dT) != m_2(dT,T)."""
        r1 = virasoro_m2("T", "dT")
        r2 = virasoro_m2("dT", "T")
        assert r1["d2T"] != r2["d2T"]


class TestM3:
    def test_vacuum_killed(self):
        result = virasoro_m3_from_bar()
        assert result["vacuum_contribution"] == 0

    def test_surviving_terms(self):
        result = virasoro_m3_from_bar()
        assert len(result["surviving_bar2"]) == 2

    def test_weight(self):
        assert virasoro_m3_weight() == 6


class TestCurvedRelations:
    def test_n0(self):
        assert "m_1(m_0)" in curved_ainfty_relation(0)

    def test_n1(self):
        rel = curved_ainfty_relation(1)
        assert "m_1^2" in rel
        assert "[m_0, a]" in rel

    def test_n2(self):
        rel = curved_ainfty_relation(2)
        assert "m_3" in rel


class TestCurvatureRegimes:
    def test_three_regimes(self):
        regimes = virasoro_curved_regimes()
        assert len(regimes) == 3

    def test_c0_uncurved(self):
        regimes = virasoro_curved_regimes()
        assert regimes["c=0"]["curved"] is False

    def test_generic_curved(self):
        regimes = virasoro_curved_regimes()
        assert regimes["c_generic"]["curved"] is True

    def test_c26_dual_uncurved(self):
        regimes = virasoro_curved_regimes()
        assert regimes["c=26"]["dual_m0"] == 0


class TestArnoldAinfty:
    def test_deg3(self):
        result = arnold_as_ainfty(3)
        assert result["n_collisions"] == 3
        assert result["vacuum_leakage_cancels"]

    def test_deg4(self):
        result = arnold_as_ainfty(4)
        assert result["n_collisions"] == 6

    def test_deg5(self):
        result = arnold_as_ainfty(5)
        assert result["n_collisions"] == 10


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_virasoro_ainfty().items():
            assert ok, f"Failed: {name}"
