"""Tests for MC3 categorical lift: Baxter SES for prefundamental modules.

KEY THEOREM: The singular vector w₀ = -v₊⊗f·v₀ in V₁(a)⊗L⁻(b) is
Yangian highest-weight UNCONDITIONALLY (Δ(E)·w₀ = 0 at λ=0).
This gives the Baxter SES:
  0 → L⁻(b-1) → V₁(a)⊗L⁻(b) → L⁻(b+1) → 0
for all spectral parameters a, b.
"""

import pytest

from compute.lib.mc3_categorical_lift import (
    baxter_ses_higher_spin,
    baxter_ses_prefundamental,
    mc3_thick_generation_status,
    yangian_singular_vector_lambda0,
)


class TestBaxterSESPrefundamental:
    """The Baxter SES for V₁ ⊗ L⁻."""

    def test_ses_holds(self):
        r = baxter_ses_prefundamental()
        assert r["ses_holds"]

    def test_singular_vector_sl2(self):
        r = baxter_ses_prefundamental()
        assert r["singular_vector"]["sl2_highest_weight"]

    def test_singular_vector_yangian(self):
        r = baxter_ses_prefundamental()
        assert r["singular_vector"]["yangian_highest_weight"]

    def test_unconditional(self):
        """The λ=0 case needs NO spectral constraint."""
        r = baxter_ses_prefundamental()
        assert "NONE" in r["singular_vector"]["spectral_constraint"]


class TestYangianSingularVector:
    """The Yangian singular vector at λ=0."""

    def test_formula(self):
        r = yangian_singular_vector_lambda0()
        assert r["lambda"] == 0
        assert "unconditional" in r["result"]

    def test_unconditional(self):
        r = yangian_singular_vector_lambda0()
        assert "no constraint" in r["comparison_with_verma"].lower()


class TestHigherSpinBaxter:
    """V_n ⊗ L⁻ = ⊕ L⁻(shifted) for n ≥ 2."""

    def test_n2(self):
        r = baxter_ses_higher_spin(2)
        assert r["match"]

    def test_n3(self):
        r = baxter_ses_higher_spin(3)
        assert r["match"]

    def test_n4(self):
        r = baxter_ses_higher_spin(4)
        assert r["match"]

    def test_n6(self):
        r = baxter_ses_higher_spin(6)
        assert r["match"]

    def test_n8(self):
        r = baxter_ses_higher_spin(8)
        assert r["match"]


class TestMC3ThickGeneration:
    """Comprehensive thick generation status."""

    def test_all_components(self):
        status = mc3_thick_generation_status()
        assert status["prefundamental_cg"]["all_match"]
        assert status["baxter_ses_prefundamental"]["ses_holds"]
        assert status["yangian_sv_lambda0"]["unconditional"]
        assert status["k0_generation"]["all_contained"]

    def test_overall_status(self):
        status = mc3_thick_generation_status()
        assert "PROVED" in status["overall"]
