"""Tests for the cross-volume bridge: Vol I ↔ Vol II verification.

The first test suite that computationally crosses the Vol I / Vol II boundary.

Five bridges tested:
  1. DK-0 (Laplace): r(z) = Laplace transform of λ-bracket
  2. Theorem D (κ): curvature from bar complex = m_0 from curved A∞
  3. Theorem C (complementarity): κ(A) + κ(A!) is constant
  4. Theorem B (Feigin–Frenkel): k ↔ −k−2h∨, Vir self-dual at c=13
  5. Theorem H (Hochschild): ChirHoch*(A) polynomial on Koszul locus

Families: Heisenberg, sl₂, Virasoro, bc/βγ, W₃.
"""

import pytest
from sympy import Symbol, Rational, simplify, expand, S

from compute.lib.cross_volume_bridge import (
    heisenberg_family, sl2_family, virasoro_family,
    bc_betagamma_family, w3_family,
    verify_bridge_1, verify_bridge_2, verify_bridge_3,
    verify_bridge_4_virasoro, verify_bridge_4_sl2,
    verify_bridge_5_heisenberg, verify_bridge_5_sl2, verify_bridge_5_sl3,
    laplace_transform, ope_from_bracket, extract_kappa_from_ope,
    run_all_bridges, count_results,
)


# ═══════════════════════════════════════════════════════════════
# Bridge 1: Laplace / DK-0
# ═══════════════════════════════════════════════════════════════

class TestBridge1_Laplace:
    """Verify r(z) = Laplace transform of λ-bracket for all families."""

    def test_heisenberg_laplace(self):
        """Heisenberg: {a_λ a} = kλ → r(z) = k/z²."""
        results = verify_bridge_1(heisenberg_family())
        for key, data in results.items():
            assert data["match"], f"{key}: diff = {data['diff']}"

    def test_sl2_laplace_all_pairs(self):
        """sl₂: 9 generator pairs, all must match."""
        results = verify_bridge_1(sl2_family())
        for key, data in results.items():
            assert data["match"], f"{key}: diff = {data['diff']}"

    def test_sl2_laplace_count(self):
        """sl₂ has 6 non-trivial bracket pairs."""
        results = verify_bridge_1(sl2_family())
        assert len(results) == 6

    def test_virasoro_laplace(self):
        """{T_λ T} = ∂T + 2Tλ + (c/12)λ³ → OPE with poles 1,2,4."""
        results = verify_bridge_1(virasoro_family())
        for key, data in results.items():
            assert data["match"], f"{key}: diff = {data['diff']}"

    def test_bc_laplace(self):
        """bc ghosts: {b_λ c} = 1 → r(z) = 1/z."""
        results = verify_bridge_1(bc_betagamma_family())
        for key, data in results.items():
            assert data["match"], f"{key}: diff = {data['diff']}"

    def test_w3_laplace(self):
        """W₃: T-T, T-W, W-W brackets all match."""
        results = verify_bridge_1(w3_family())
        assert len(results) == 3
        for key, data in results.items():
            assert data["match"], f"{key}: diff = {data['diff']}"

    def test_laplace_basic_formula(self):
        """Verify: Σ c_n λ^n → Σ c_n n! / z^{n+1}."""
        z = Symbol('z')
        coeffs = {0: 1, 1: 2, 3: 3}
        r = laplace_transform(coeffs, z)
        expected = 1 / z + 2 / z**2 + 18 / z**4  # 3·3! = 18
        assert simplify(r - expected) == 0


# ═══════════════════════════════════════════════════════════════
# Bridge 2: Curvature / κ extraction
# ═══════════════════════════════════════════════════════════════

class TestBridge2_Kappa:
    """Verify κ(A) extraction matches stated values."""

    def test_heisenberg_kappa(self):
        """Heisenberg: κ = k (the level IS the curvature)."""
        results = verify_bridge_2(heisenberg_family())
        assert results["κ extraction"]["match"]

    def test_virasoro_kappa(self):
        """Virasoro: κ = c/2 (from the quartic pole c/2 in T(z)T(w))."""
        results = verify_bridge_2(virasoro_family())
        assert results["κ extraction"]["match"]

    def test_w3_kappa(self):
        """W₃: κ = 5c/6 = c/2 (from T) + c/3 (from W)."""
        results = verify_bridge_2(w3_family())
        assert results["κ extraction"]["match"]

    def test_w3_kappa_decomposition(self):
        """W₃ kappa decomposes: c/2 + c/3 = 5c/6."""
        c = Symbol('c')
        assert simplify(c / 2 + c / 3 - 5 * c / 6) == 0


# ═══════════════════════════════════════════════════════════════
# Bridge 3: Complementarity
# ═══════════════════════════════════════════════════════════════

class TestBridge3_Complementarity:
    """Verify κ(A) + κ(A!) is constant (parameter-independent)."""

    def test_heisenberg_complementarity(self):
        """Heisenberg: κ(H_k) + κ(H_{-k}) = k + (-k) = 0."""
        results = verify_bridge_3(heisenberg_family())
        assert results["κ-complementarity"]["match"]

    def test_sl2_complementarity(self):
        """sl₂: κ(ĝ_k) + κ(ĝ_{-k-4}) = 0 (anti-symmetric)."""
        results = verify_bridge_3(sl2_family())
        assert results["κ-complementarity"]["match"]

    def test_virasoro_complementarity(self):
        """Vir: κ(c) + κ(26-c) = 13 (constant, NOT 0)."""
        results = verify_bridge_3(virasoro_family())
        assert results["κ-complementarity"]["match"]
        assert results["κ-complementarity"]["sum"] == 13

    def test_w3_complementarity(self):
        """W₃: κ(c) + κ(100-c) = 250/3 (constant)."""
        results = verify_bridge_3(w3_family())
        assert results["κ-complementarity"]["match"]
        assert results["κ-complementarity"]["sum"] == Rational(250, 3)

    def test_bc_complementarity(self):
        """bc: κ + κ' = -13 + 13 = 0."""
        results = verify_bridge_3(bc_betagamma_family())
        assert results["κ-complementarity"]["match"]


# ═══════════════════════════════════════════════════════════════
# Bridge 4: Feigin–Frenkel / duality
# ═══════════════════════════════════════════════════════════════

class TestBridge4_FeiginFrenkel:
    """Verify duality involutions."""

    def test_virasoro_self_dual_at_13(self):
        """CRITICAL PITFALL: Vir self-dual at c=13, NOT c=26."""
        results = verify_bridge_4_virasoro()
        assert results["Vir self-duality"]["self_dual_at"] == 13
        assert results["Vir self-duality"]["NOT_26"]

    def test_sl2_feigin_frenkel(self):
        """sl₂: dual level = -k-4 (= -k-2h∨ with h∨=2)."""
        results = verify_bridge_4_sl2()
        assert results["FF involution"]["dual_level"] == "-k - 4"
        assert results["FF involution"]["critical_level_k"] == -2
        assert results["FF involution"]["sugawara_undefined"]


# ═══════════════════════════════════════════════════════════════
# Bridge 5: Hochschild polynomiality
# ═══════════════════════════════════════════════════════════════

class TestBridge5_Hochschild:
    """Verify ChirHoch*(A) is polynomial with correct generators."""

    def test_heisenberg_polynomial(self):
        """H_k: ChirHoch = C[T], one generator degree 2."""
        results = verify_bridge_5_heisenberg()
        data = results["Heisenberg ChirHoch"]
        assert data["num_generators"] == 1
        assert data["generator_degree"] == 2
        assert data["poincare_series"] == "1/(1-t²)"

    def test_sl2_polynomial(self):
        """sl₂: ChirHoch = C[C₂], one generator degree 2."""
        results = verify_bridge_5_sl2()
        data = results["sl₂ ChirHoch"]
        assert data["num_generators"] == 1
        assert data["generator_degree"] == 2

    def test_sl3_polynomial(self):
        """sl₃: ChirHoch = C[C₂, C₃], two generators degrees 2,3."""
        results = verify_bridge_5_sl3()
        data = results["sl₃ ChirHoch"]
        assert data["num_generators"] == 2
        assert data["generator_degrees"] == [2, 3]
        assert data["exponents"] == [1, 2]

    def test_hochschild_heisenberg_dims(self):
        """Heisenberg: dim ChirHoch^n = 1 if n even, 0 if n odd."""
        results = verify_bridge_5_heisenberg()
        dims = results["Heisenberg ChirHoch"]["dims_0_through_7"]
        for n in range(8):
            expected = 1 if n % 2 == 0 else 0
            assert dims[n] == expected, f"dim ChirHoch^{n} = {dims[n]}, expected {expected}"


# ═══════════════════════════════════════════════════════════════
# Master test: all bridges, all families
# ═══════════════════════════════════════════════════════════════

class TestMasterBridge:
    """Run the complete cross-volume verification."""

    def test_all_bridges_pass(self):
        """Every bridge on every family must pass."""
        results = run_all_bridges()
        passes, failures = count_results(results)
        assert failures == 0, f"{failures} bridge checks failed"
        assert passes >= 25, f"Expected ≥25 checks, got {passes}"

    def test_five_families_tested(self):
        """All five families must be tested."""
        results = run_all_bridges()
        family_names = set(results.keys())
        for expected in ["Heisenberg H_k", "sl₂ level k", "Virasoro Vir_c",
                         "bc ghosts", "W₃ at central charge c"]:
            assert expected in family_names, f"Missing family: {expected}"
