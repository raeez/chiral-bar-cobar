"""Tests for MC5 disk-local packet: BV-BRST = bar at chain level.

Verifies conj:disk-local-perturbative-fm on C₂ and C₃ strata
for abelian CS, su(2) KM, and Virasoro.

The identification: at genus 0, the perturbative BRST differential
extracts the SAME residue operations as the Vol I bar differential.
"""

import pytest
from sympy import Symbol, symbols, S

from compute.lib.mc5_disk_local import (
    verify_C2_identification,
    verify_C3_identification,
    verify_abelian_cs,
    verify_su2_km,
    verify_virasoro,
    verify_all_families,
)


class TestC2Identification:
    """BV-BRST = bar on C₂ (binary operations)."""

    def test_abelian_c2(self):
        k = Symbol('k')
        result = verify_C2_identification({1: k})
        assert result["all_match"]

    def test_structure_constant_c2(self):
        J = Symbol('J')
        result = verify_C2_identification({0: J})
        assert result["all_match"]

    def test_virasoro_c2(self):
        c = Symbol('c')
        T, dT = symbols('T dT')
        result = verify_C2_identification({0: dT, 1: 2*T, 3: c/2})
        assert result["all_match"]

    def test_empty_ope(self):
        result = verify_C2_identification({})
        assert result["all_match"]


class TestC3Identification:
    """BV-BRST = bar on C₃ (ternary, Arnold cancellation)."""

    def test_abelian_c3(self):
        k = Symbol('k')
        result = verify_C3_identification({1: k}, {1: k}, {1: k})
        assert result["all_match"]

    def test_su2_jacobi_c3(self):
        J1, J2, J3 = symbols('J1 J2 J3')
        result = verify_C3_identification({0: J3}, {0: J1}, {0: -J2})
        assert result["all_match"]

    def test_virasoro_c3(self):
        c = Symbol('c')
        T, dT = symbols('T dT')
        ope = {0: dT, 1: 2*T, 3: c/2}
        result = verify_C3_identification(ope, ope, ope)
        assert result["all_match"]


class TestFamilies:
    """Full family-level verification."""

    def test_abelian_cs(self):
        result = verify_abelian_cs()
        assert result["C2"]["all_match"]
        assert result["C3"]["all_match"]

    def test_su2_km(self):
        result = verify_su2_km()
        assert result["C2_structure"]["all_match"]
        assert result["C2_level"]["all_match"]
        assert result["C3_jacobi"]["all_match"]

    def test_virasoro(self):
        result = verify_virasoro()
        assert result["C2"]["all_match"]
        assert result["C3"]["all_match"]

    def test_all_families(self):
        results = verify_all_families()
        assert len(results) == 3
        for family, data in results.items():
            for stratum, checks in data.items():
                if isinstance(checks, dict) and "all_match" in checks:
                    assert checks["all_match"], f"{family}/{stratum} failed"
