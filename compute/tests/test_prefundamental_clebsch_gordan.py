"""Tests for the prefundamental Clebsch-Gordan decomposition.

THEOREM: V_n(a) ⊗ L⁻(b) = ⊕_{j=0}^n L⁻(b + n - 2j) at character level.

This is the key structural result for MC3 thick generation:
it shows L⁻ is evaluation-stable (tensoring with V_n just shifts).
"""

import pytest

from compute.lib.prefundamental_clebsch_gordan import (
    k0_generation_chain,
    prefundamental_clebsch_gordan,
    verma_in_k0_span_of_prefundamental,
    verify_prefundamental_cg,
)


class TestPrefundamentalClebschGordan:
    """V_n ⊗ L⁻ = ⊕ L⁻(shifted) — the core decomposition."""

    def test_n1(self):
        """V_1 ⊗ L⁻ = L⁻(1) ⊕ L⁻(-1)."""
        r = prefundamental_clebsch_gordan(1)
        assert r["match"]
        assert r["n_components"] == 2
        assert r["highest_weights"] == [1, -1]

    def test_n2(self):
        """V_2 ⊗ L⁻ = L⁻(2) ⊕ L⁻(0) ⊕ L⁻(-2)."""
        r = prefundamental_clebsch_gordan(2)
        assert r["match"]
        assert r["n_components"] == 3

    def test_n3(self):
        r = prefundamental_clebsch_gordan(3)
        assert r["match"]

    def test_n4(self):
        r = prefundamental_clebsch_gordan(4)
        assert r["match"]

    def test_n5(self):
        r = prefundamental_clebsch_gordan(5)
        assert r["match"]

    def test_n6(self):
        r = prefundamental_clebsch_gordan(6)
        assert r["match"]

    def test_n7(self):
        r = prefundamental_clebsch_gordan(7)
        assert r["match"]

    def test_n8(self):
        r = prefundamental_clebsch_gordan(8)
        assert r["match"]

    def test_all_n_1_through_8(self):
        """Batch verification for n = 1, ..., 8."""
        results = verify_prefundamental_cg(max_n=8)
        for n, ok in results.items():
            assert ok, f"Prefundamental CG failed at n={n}"


class TestVermaInK0Span:
    """[M(λ)] is in the character-level span of {[L⁻(shifted)]}."""

    def test_m0_containment(self):
        r = verma_in_k0_span_of_prefundamental(0)
        assert r["k1_pattern"]
        assert r["containment"]

    def test_m1_containment(self):
        r = verma_in_k0_span_of_prefundamental(1)
        assert r["containment"]

    def test_m2_containment(self):
        r = verma_in_k0_span_of_prefundamental(2)
        assert r["containment"]

    def test_m3_containment(self):
        r = verma_in_k0_span_of_prefundamental(3)
        assert r["containment"]

    def test_m5_containment(self):
        r = verma_in_k0_span_of_prefundamental(5)
        assert r["containment"]


class TestK0GenerationChain:
    """K_0 generation: all Verma modules in the span of {V_n, L⁻}."""

    def test_chain_through_10(self):
        results = k0_generation_chain(max_lam=10)
        for lam, ok in results.items():
            assert ok, f"K_0 generation failed at λ={lam}"
