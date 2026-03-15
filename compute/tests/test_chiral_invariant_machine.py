"""Tests for the chiral_invariant_machine module.

Focuses on the InvariantPackage dataclass, pipeline stages, and
mathematical correctness of individual components.

Note: test_invariant_machine.py provides comprehensive integration tests
for the same module. This file tests individual functions and edge cases.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.chiral_invariant_machine import (
    InvariantPackage,
    ChiralInvariantMachine,
    extract_bracket_relations,
    extract_curvature,
    check_pbw_koszulness,
    compute_kappa_from_registry,
    check_bar_gf_algebraicity,
)


# ===================================================================
# InvariantPackage dataclass
# ===================================================================

class TestInvariantPackage:
    def test_creation(self):
        pkg = InvariantPackage(
            name="test",
            n_generators=3,
            generator_weights=[1, 1, 1],
            max_pole_order=2,
            is_curved=True,
        )
        assert pkg.name == "test"
        assert pkg.n_generators == 3

    def test_defaults(self):
        pkg = InvariantPackage(
            name="test",
            n_generators=1,
            generator_weights=[1],
            max_pole_order=1,
            is_curved=False,
        )
        assert pkg.pbw_koszul is None
        assert pkg.bar_dims == {}
        assert pkg.kappa is None

    def test_summary_format(self):
        pkg = InvariantPackage(
            name="test_algebra",
            n_generators=2,
            generator_weights=[1, 2],
            max_pole_order=4,
            is_curved=True,
        )
        s = pkg.summary()
        assert "test_algebra" in s
        assert "Generators: 2" in s
        assert "Curved: True" in s

    def test_summary_with_kappa(self):
        pkg = InvariantPackage(
            name="test",
            n_generators=1,
            generator_weights=[1],
            max_pole_order=2,
            is_curved=True,
            kappa=Rational(1, 2),
        )
        s = pkg.summary()
        assert "1/2" in s


# ===================================================================
# Kappa from registry
# ===================================================================

class TestComputeKappa:
    def test_heisenberg(self):
        kap = compute_kappa_from_registry("Heisenberg")
        assert kap == Symbol("kappa")

    def test_sl2(self):
        """kappa(sl_2) = 3(k+2)/4."""
        kap = compute_kappa_from_registry("sl2")
        k = Symbol("k")
        assert simplify(kap - 3 * (k + 2) / 4) == 0

    def test_virasoro(self):
        """kappa(Vir) = c/2."""
        kap = compute_kappa_from_registry("Virasoro")
        c = Symbol("c")
        assert simplify(kap - c / 2) == 0

    def test_w3(self):
        """kappa(W3) = 5c/6."""
        kap = compute_kappa_from_registry("W3")
        c = Symbol("c")
        assert simplify(kap - 5 * c / 6) == 0

    def test_e8(self):
        """kappa(E8) = 248(k+30)/60."""
        kap = compute_kappa_from_registry("E8")
        k = Symbol("k")
        assert simplify(kap - 248 * (k + 30) / 60) == 0

    def test_nonexistent_returns_none(self):
        kap = compute_kappa_from_registry("nonexistent_algebra")
        assert kap is None


# ===================================================================
# PBW Koszulness via OPE
# ===================================================================

class TestPBWKoszulness:
    def test_sl2_from_ope(self):
        from compute.lib.bar_complex import sl2_algebra
        alg = sl2_algebra()
        result, method = check_pbw_koszulness(alg)
        assert result is True
        assert "Koszul" in method or "KM" in method

    def test_heisenberg_from_ope(self):
        from compute.lib.bar_complex import heisenberg_algebra
        alg = heisenberg_algebra()
        result, method = check_pbw_koszulness(alg)
        assert result is True

    def test_virasoro_from_ope(self):
        from compute.lib.bar_complex import virasoro_algebra
        alg = virasoro_algebra()
        result, method = check_pbw_koszulness(alg)
        assert result is True


# ===================================================================
# Bar GF algebraicity
# ===================================================================

class TestBarGFAlgebraicity:
    def test_empty_data(self):
        result = check_bar_gf_algebraicity({})
        assert result["algebraic"] is None

    def test_insufficient_data(self):
        result = check_bar_gf_algebraicity({1: 3, 2: 6})
        assert result["algebraic"] is None

    def test_sl2_algebraic(self):
        """sl_2: Riordan numbers satisfy algebraic GF of degree 2."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        dims = {n: d for n, d in KNOWN_BAR_DIMS["sl2"].items() if n <= 7}
        result = check_bar_gf_algebraicity(dims)
        assert result["algebraic"] is True
        assert result["degree"] == 2


# ===================================================================
# Bracket extraction
# ===================================================================

class TestBracketExtraction:
    def test_sl2_dim(self):
        from compute.lib.bar_complex import sl2_algebra
        alg = sl2_algebra()
        d, relations = extract_bracket_relations(alg)
        assert d == 3

    def test_sl2_relations_count(self):
        """sl_2 has C(3,2)=3 antisymmetric relations."""
        from compute.lib.bar_complex import sl2_algebra
        alg = sl2_algebra()
        d, relations = extract_bracket_relations(alg)
        assert relations.shape[0] == 3

    def test_heisenberg_no_relations(self):
        """Heisenberg has 1 generator, no antisymmetric pairs."""
        from compute.lib.bar_complex import heisenberg_algebra
        alg = heisenberg_algebra()
        d, relations = extract_bracket_relations(alg)
        assert d == 1
        assert relations.shape[0] == 0


# ===================================================================
# Curvature extraction
# ===================================================================

class TestCurvatureExtraction:
    def test_sl2_has_curvature(self):
        from compute.lib.bar_complex import sl2_algebra
        alg = sl2_algebra(k=Symbol("k"))
        curv = extract_curvature(alg)
        assert curv["has_curvature"] is True

    def test_heisenberg_has_curvature(self):
        from compute.lib.bar_complex import heisenberg_algebra
        alg = heisenberg_algebra()
        curv = extract_curvature(alg)
        assert curv["has_curvature"] is True


# ===================================================================
# Machine pipeline (basic)
# ===================================================================

class TestMachinePipeline:
    def test_heisenberg_pipeline(self):
        machine = ChiralInvariantMachine("Heisenberg")
        pkg = machine.compute()
        assert pkg.name == "Heisenberg"
        assert pkg.pbw_koszul is True
        assert pkg.kappa is not None

    def test_sl2_complementarity(self):
        """kappa(sl_2) + kappa(sl_2') = 0."""
        pkg = ChiralInvariantMachine("sl2").compute()
        assert pkg.kappa_sum is not None
        assert simplify(pkg.kappa_sum) == 0

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        pkg = ChiralInvariantMachine("Virasoro").compute()
        assert pkg.kappa_sum == 13

    def test_w3_complementarity(self):
        """kappa(W3_c) + kappa(W3_{100-c}) = 250/3."""
        pkg = ChiralInvariantMachine("W3").compute()
        assert pkg.kappa_sum == Rational(250, 3)


# ===================================================================
# P_inf vs Coisson (from the module's utility)
# ===================================================================

class TestDiscriminant:
    """Test spectral discriminant computation."""

    def test_sl2_discriminant(self):
        pkg = ChiralInvariantMachine("sl2").compute()
        assert pkg.discriminant is not None
        assert "1-3x" in pkg.discriminant.replace(" ", "").replace("\u2212", "-")

    def test_heisenberg_trivial(self):
        pkg = ChiralInvariantMachine("Heisenberg").compute()
        assert pkg.discriminant is not None
        assert "1" in pkg.discriminant
