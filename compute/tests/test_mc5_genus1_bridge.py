"""Tests for MC5 genus-1 bridge: curved bar d² = κ(A)·ω₁.

Verifies the extension of MC5 from genus 0 (d²=0) to genus 1 (d²=κ·ω₁)
for Heisenberg, sl₂, Virasoro, W₃, and bc/βγ.

Three independent verification axes:
  I.   Curvature: d²_fib = κ(A)·E₂(τ)·ω₁ with correct κ values
  II.  Complementarity: κ(A) + κ(A!) = const at genus 1
  III. Quantum correction: F₁(A) = κ/24 absorbs curvature, restoring D₁²=0

Ground truth:
  Vol I: higher_genus_foundations.tex, quantum_corrections.tex, genus_expansion.py
  Vol II: bv_construction.tex (A∞ curvature = m₀ at genus 1)
  Cross: cross_volume_bridge.py Bridge 2 (κ identification)
"""

import pytest
from sympy import (
    Symbol, Rational, simplify, expand, S, symbols, bernoulli,
    factorial, Abs,
)

from compute.lib.mc5_genus1_bridge import (
    eisenstein_E2_q_expansion,
    arnold_defect_genus1,
    curved_bar_d_squared,
    verify_curvature_formula,
    lambda_fp_genus1,
    genus1_free_energy,
    verify_total_differential_nilpotence,
    verify_heisenberg_genus1,
    verify_sl2_genus1,
    verify_virasoro_genus1,
    verify_w3_genus1,
    verify_bc_genus1,
    verify_E2_modularity_defect,
    verify_genus1_bridge_all_families,
    genus_comparison,
)


# ═══════════════════════════════════════════════════════════════════════
# I. Eisenstein series E₂
# ═══════════════════════════════════════════════════════════════════════

class TestEisensteinE2:
    """q-expansion and divisor sum verification for E₂(τ)."""

    def test_constant_term(self):
        """E₂ starts with 1."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[0] == 1

    def test_q1_coefficient(self):
        """Coefficient of q¹ is -24·σ₁(1) = -24."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[1] == -24

    def test_q2_coefficient(self):
        """σ₁(2) = 1+2 = 3, so coeff = -72."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[2] == -72

    def test_q3_coefficient(self):
        """σ₁(3) = 1+3 = 4, so coeff = -96."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[3] == -96

    def test_q4_coefficient(self):
        """σ₁(4) = 1+2+4 = 7, so coeff = -168."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[4] == -168

    def test_q5_coefficient(self):
        """σ₁(5) = 1+5 = 6, so coeff = -144."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[5] == -144

    def test_q6_coefficient(self):
        """σ₁(6) = 1+2+3+6 = 12, so coeff = -288."""
        coeffs = eisenstein_E2_q_expansion(10)
        assert coeffs[6] == -288

    def test_modularity_defect_all_match(self):
        result = verify_E2_modularity_defect()
        assert result["all_match"]


# ═══════════════════════════════════════════════════════════════════════
# II. Faber-Pandharipande number λ₁^FP
# ═══════════════════════════════════════════════════════════════════════

class TestLambdaFP:
    """λ₁^FP = 1/24."""

    def test_value(self):
        assert lambda_fp_genus1() == Rational(1, 24)

    def test_from_bernoulli(self):
        """Direct computation: (2¹-1)/2¹ · |B₂|/(2!) = 1/2 · 1/12 = 1/24."""
        B2 = bernoulli(2)  # 1/6
        result = Rational(1, 2) * Abs(B2) / factorial(2)
        assert result == Rational(1, 24)


# ═══════════════════════════════════════════════════════════════════════
# III. Genus-1 curvature: d²_fib = κ · ω₁
# ═══════════════════════════════════════════════════════════════════════

class TestCurvatureFormula:
    """d²_fib = κ(A)·E₂(τ)·ω₁."""

    def test_zero_kappa_gives_flat(self):
        """κ = 0 ⟹ d² = 0 (uncurved, genus-0 behavior persists)."""
        result = curved_bar_d_squared(S.Zero)
        assert result["is_zero"]
        assert result["d_squared"] == 0

    def test_nonzero_kappa_gives_curvature(self):
        """κ ≠ 0 ⟹ d² ≠ 0 (curved)."""
        k = Symbol('k', positive=True)
        result = curved_bar_d_squared(k)
        assert not result["is_zero"]

    def test_curvature_linear_in_kappa(self):
        """d² is linear in κ: d²(2κ) = 2·d²(κ)."""
        k = Symbol('k')
        r1 = curved_bar_d_squared(k)
        r2 = curved_bar_d_squared(2 * k)
        assert simplify(r2["d_squared"] - 2 * r1["d_squared"]) == 0

    def test_curvature_additive(self):
        """d²(κ₁ + κ₂) = d²(κ₁) + d²(κ₂) (additivity of κ)."""
        k1, k2 = symbols('k1 k2')
        r_sum = curved_bar_d_squared(k1 + k2)
        r1 = curved_bar_d_squared(k1)
        r2 = curved_bar_d_squared(k2)
        assert simplify(r_sum["d_squared"] - r1["d_squared"] - r2["d_squared"]) == 0


# ═══════════════════════════════════════════════════════════════════════
# IV. Quantum correction: F₁ = κ/24 and D₁² = 0
# ═══════════════════════════════════════════════════════════════════════

class TestQuantumCorrection:
    """Period-corrected total differential D₁ = d₀ + (κ/24)·d₁, D₁²=0."""

    def test_free_energy_formula(self):
        """F₁(A) = κ(A)/24."""
        k = Symbol('k')
        assert simplify(genus1_free_energy(k) - k / 24) == 0

    def test_free_energy_heisenberg(self):
        """F₁(H_κ) = κ/24."""
        assert genus1_free_energy(Rational(1)) == Rational(1, 24)

    def test_free_energy_virasoro(self):
        """F₁(Vir_c) = (c/2)/24 = c/48."""
        c = Symbol('c')
        kappa_vir = c / 2
        assert simplify(genus1_free_energy(kappa_vir) - c / 48) == 0

    def test_nilpotence_restoration(self):
        """D₁² = 0: the correction absorbs the curvature."""
        k = Symbol('k')
        result = verify_total_differential_nilpotence(k)
        assert result["correction = curvature × integral"]
        assert result["D₁² = 0"]


# ═══════════════════════════════════════════════════════════════════════
# V. Heisenberg at genus 1
# ═══════════════════════════════════════════════════════════════════════

class TestHeisenbergGenus1:
    """H_κ: κ(A) = κ, κ(A!) = -κ, complementarity sum = 0."""

    def test_curvature_is_level(self):
        result = verify_heisenberg_genus1()
        kappa = Symbol('kappa')
        assert result["curvature"]["κ"] == kappa

    def test_complementarity(self):
        result = verify_heisenberg_genus1()
        assert result["complementarity"]["match"]

    def test_complementarity_sum_is_zero(self):
        result = verify_heisenberg_genus1()
        assert simplify(result["complementarity"]["sum"]) == 0

    def test_free_energy(self):
        result = verify_heisenberg_genus1()
        assert result["F₁_match"]

    def test_correction(self):
        result = verify_heisenberg_genus1()
        assert result["correction"]["D₁² = 0"]


# ═══════════════════════════════════════════════════════════════════════
# VI. sl₂ at genus 1
# ═══════════════════════════════════════════════════════════════════════

class TestSl2Genus1:
    """sl₂_k: κ = 3(k+2)/4, anti-symmetric under k ↦ -k-4."""

    def test_kappa_formula(self):
        result = verify_sl2_genus1()
        k = Symbol('k')
        expected = Rational(3) * (k + 2) / 4
        assert simplify(result["curvature"]["κ"] - expected) == 0

    def test_complementarity(self):
        result = verify_sl2_genus1()
        assert result["complementarity"]["match"]

    def test_complementarity_sum_is_zero(self):
        """κ(sl₂_k) + κ(sl₂_{-k-4}) = 0 (anti-symmetric)."""
        result = verify_sl2_genus1()
        assert simplify(result["complementarity"]["sum"]) == 0

    def test_free_energy(self):
        result = verify_sl2_genus1()
        assert result["F₁_match"]

    def test_free_energy_at_k1(self):
        """F₁(sl₂_1) = 3·3/4 · 1/24 = 9/96 = 3/32."""
        k = Symbol('k')
        F1 = genus1_free_energy(Rational(3) * (1 + 2) / 4)
        assert F1 == Rational(3, 32)

    def test_correction(self):
        result = verify_sl2_genus1()
        assert result["correction"]["D₁² = 0"]


# ═══════════════════════════════════════════════════════════════════════
# VII. Virasoro at genus 1
# ═══════════════════════════════════════════════════════════════════════

class TestVirasoroGenus1:
    """Vir_c: κ = c/2, dual = (26-c)/2, sum = 13. Self-dual at c=13."""

    def test_kappa_formula(self):
        result = verify_virasoro_genus1()
        c = Symbol('c')
        assert simplify(result["curvature"]["κ"] - c / 2) == 0

    def test_complementarity(self):
        result = verify_virasoro_genus1()
        assert result["complementarity"]["match"]

    def test_complementarity_sum_is_13(self):
        """κ(Vir_c) + κ(Vir_{26-c}) = 13."""
        result = verify_virasoro_genus1()
        assert result["complementarity"]["sum"] == 13

    def test_self_duality_at_c13(self):
        """Self-dual at c=13, NOT c=26 (Critical Pitfall)."""
        result = verify_virasoro_genus1()
        assert result["self_dual_c"] == 13
        assert result["self_duality_verified"]

    def test_not_self_dual_at_c26(self):
        """Explicitly verify c=26 is NOT the self-dual point."""
        c = S(26)
        kappa = c / 2  # = 13
        kappa_dual = (26 - c) / 2  # = 0
        assert kappa != kappa_dual

    def test_free_energy(self):
        result = verify_virasoro_genus1()
        assert result["F₁_match"]

    def test_free_energy_at_c26(self):
        """F₁(Vir_26) = 26/48 = 13/24."""
        F1 = genus1_free_energy(Rational(26) / 2)
        assert F1 == Rational(13, 24)

    def test_correction(self):
        result = verify_virasoro_genus1()
        assert result["correction"]["D₁² = 0"]


# ═══════════════════════════════════════════════════════════════════════
# VIII. W₃ at genus 1
# ═══════════════════════════════════════════════════════════════════════

class TestW3Genus1:
    """W₃_c: κ = 5c/6, sum = 250/3."""

    def test_kappa_formula(self):
        result = verify_w3_genus1()
        c = Symbol('c')
        assert simplify(result["curvature"]["κ"] - 5 * c / 6) == 0

    def test_complementarity(self):
        result = verify_w3_genus1()
        assert result["complementarity"]["match"]

    def test_complementarity_sum(self):
        """κ(W₃_c) + κ(W₃_{100-c}) = 250/3."""
        result = verify_w3_genus1()
        assert result["complementarity"]["sum"] == Rational(250, 3)

    def test_free_energy(self):
        result = verify_w3_genus1()
        assert result["F₁_match"]

    def test_correction(self):
        result = verify_w3_genus1()
        assert result["correction"]["D₁² = 0"]


# ═══════════════════════════════════════════════════════════════════════
# IX. bc/βγ at genus 1
# ═══════════════════════════════════════════════════════════════════════

class TestBcGenus1:
    """bc system: κ = c/2 = -(6λ²-6λ+1)."""

    def test_c_at_half(self):
        """At λ=1/2: c = 1."""
        result = verify_bc_genus1()
        assert result["c_at_λ=1/2"] == 1

    def test_kappa_at_half(self):
        """At λ=1/2: κ = 1/2."""
        result = verify_bc_genus1()
        assert result["κ_at_λ=1/2"] == Rational(1, 2)

    def test_F1_at_half(self):
        """At λ=1/2: F₁ = (1/2)/24 = 1/48."""
        result = verify_bc_genus1()
        assert result["F₁_at_λ=1/2"] == Rational(1, 48)

    def test_correction(self):
        result = verify_bc_genus1()
        assert result["correction"]["D₁² = 0"]


# ═══════════════════════════════════════════════════════════════════════
# X. Cross-family structural tests
# ═══════════════════════════════════════════════════════════════════════

class TestCrossFamilyStructure:
    """Structural properties that hold across all families."""

    def test_all_families_have_curvature(self):
        """Every family has a well-defined d²_fib coefficient."""
        results = verify_genus1_bridge_all_families()
        for name in ["Heisenberg", "sl₂", "Virasoro", "W₃", "bc/βγ"]:
            assert "curvature" in results[name]

    def test_all_families_have_correction(self):
        """Every family has D₁² = 0."""
        results = verify_genus1_bridge_all_families()
        for name in ["Heisenberg", "sl₂", "Virasoro", "W₃", "bc/βγ"]:
            assert results[name]["correction"]["D₁² = 0"]

    def test_all_families_free_energy_match(self):
        """F₁ = κ/24 for all families."""
        results = verify_genus1_bridge_all_families()
        for name in ["Heisenberg", "sl₂", "Virasoro", "W₃"]:
            assert results[name]["F₁_match"]

    def test_complementarity_holds_for_paired_families(self):
        """κ + κ' = const for all families with Koszul duals."""
        results = verify_genus1_bridge_all_families()
        for name in ["Heisenberg", "sl₂", "Virasoro", "W₃"]:
            assert results[name]["complementarity"]["match"]


class TestGenusComparison:
    """Genus 0 vs genus 1 comparison."""

    def test_genus0_is_flat(self):
        k = Symbol('k')
        result = genus_comparison(k)
        assert result["genus_0"]["d²"] == 0

    def test_genus1_is_curved(self):
        k = Symbol('k')
        result = genus_comparison(k)
        assert result["genus_1"]["d²_fib"] == k

    def test_genus1_correction_restores_nilpotence(self):
        k = Symbol('k')
        result = genus_comparison(k)
        assert result["genus_1"]["D₁²"] == 0

    def test_correction_mechanism(self):
        k = Symbol('k')
        result = genus_comparison(k)
        assert result["transition"]["mechanism"] == \
            "period integral ∫_{M₁} ω₁ = λ₁^FP = 1/24"


# ═══════════════════════════════════════════════════════════════════════
# XI. Numerical spot checks
# ═══════════════════════════════════════════════════════════════════════

class TestNumericalSpotChecks:
    """Exact rational arithmetic checks at specific parameter values."""

    def test_heisenberg_k1_F1(self):
        """F₁(H_1) = 1/24."""
        assert genus1_free_energy(1) == Rational(1, 24)

    def test_sl2_k1_kappa(self):
        """κ(sl₂_1) = 3·3/4 = 9/4."""
        assert Rational(3) * (1 + 2) / 4 == Rational(9, 4)

    def test_sl2_k1_F1(self):
        """F₁(sl₂_1) = (9/4)/24 = 9/96 = 3/32."""
        assert genus1_free_energy(Rational(9, 4)) == Rational(3, 32)

    def test_virasoro_c1_F1(self):
        """F₁(Vir_1) = (1/2)/24 = 1/48."""
        assert genus1_free_energy(Rational(1, 2)) == Rational(1, 48)

    def test_virasoro_c26_F1(self):
        """F₁(Vir_26) = 13/24."""
        assert genus1_free_energy(Rational(13)) == Rational(13, 24)

    def test_virasoro_c13_selfdual_F1(self):
        """F₁(Vir_13) = (13/2)/24 = 13/48."""
        assert genus1_free_energy(Rational(13, 2)) == Rational(13, 48)

    def test_w3_c100_F1(self):
        """F₁(W₃_{c=100}) = (5·100/6)/24 = 500/144 = 125/36."""
        kappa = Rational(5) * 100 / 6
        assert genus1_free_energy(kappa) == Rational(125, 36)

    def test_complementarity_sl2_k1(self):
        """κ(sl₂_1) + κ(sl₂_{-5}) = 9/4 + 3(-3)/4 = 9/4 - 9/4 = 0."""
        kappa = Rational(3) * (1 + 2) / 4  # = 9/4
        kappa_dual = Rational(3) * (-5 + 2) / 4  # = -9/4
        assert kappa + kappa_dual == 0

    def test_complementarity_virasoro_c1(self):
        """κ(Vir_1) + κ(Vir_25) = 1/2 + 25/2 = 13."""
        assert Rational(1, 2) + Rational(25, 2) == 13
