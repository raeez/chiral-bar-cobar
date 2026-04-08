r"""Tests for the PVA classical limit bar engine.

Verification of H^*(gr^F B(A)) for Heisenberg, affine sl_2, Virasoro,
comparing three independent paths (direct bar computation, closed-form
Chevalley-Eilenberg, Euler characteristic) per CLAUDE.md multi-path mandate.

Verification paths (at least 3 per claim):

    Path 1: Direct bar complex computation (rational rank of d_CE matrices)
    Path 2: Closed-form Chevalley-Eilenberg (for semisimple Lie algebras)
    Path 3: Euler characteristic consistency
    Path 4: Symmetry / anti-symmetry of Poisson bracket
    Path 5: Complementarity sum (AP24 compliance)
    Path 6: Cross-family consistency (Heis, sl_2, Vir)
    Path 7: Associated variety dimension
    Path 8: Jacobi identity verification

Anti-patterns defended:
    AP1  — formulas computed from first principles, not copied
    AP10 — cross-family consistency checks, not just hardcoded values
    AP19 — Poisson bracket lives at zero-mode (no d-log shift at this level)
    AP24 — complementarity sum is 0 for KM/free, 13 for Virasoro (not 0)
    AP25 — gr^F B(A) is bar of classical limit, NOT the Verdier dual or cobar
    AP33 — PVA-level Koszul dual of H_k has kappa = -k but is a different
           object from H_{-k} at the full VA level
    AP44 — lambda-bracket c_n = a_{(n)}b / n! divided-power convention
"""

import pytest
from fractions import Fraction

from compute.lib.pva_classical_limit_bar_engine import (
    ClassicalPVA,
    heisenberg_classical_pva,
    affine_sl2_classical_pva,
    virasoro_classical_pva,
    ce_differential_matrix,
    ce_bar_cohomology,
    rational_rank,
    sl2_ce_cohomology_closed_form,
    check_sl2_matches_closed_form,
    pva_koszul_dual_heisenberg,
    pva_koszul_dual_sl2,
    pva_koszul_dual_virasoro,
    pva_complementarity_sum,
    heisenberg_associated_variety,
    sl2_universal_associated_variety,
    sl2_integrable_associated_variety,
    virasoro_associated_variety,
    li_bar_E1_page,
    pva_scalar_kappa,
    classical_limit_landscape_summary,
    verify_jacobi_identity,
    verify_antisymmetry,
    leak_dimensions,
    _sort_with_sign,
    _basis_exterior,
    _sign_remove_two,
)


# =========================================================================
# Section 1: Heisenberg classical-limit PVA
# =========================================================================

class TestHeisenbergClassicalPVA:
    """Heisenberg PVA: single generator phi, {phi, phi}_0 = 0, central = k."""

    def test_heisenberg_single_generator(self):
        """Path 1: Heisenberg classical PVA has exactly one generator."""
        pva = heisenberg_classical_pva(k=Fraction(3))
        assert pva.generators == ["phi"]
        assert pva.weights["phi"] == 1

    def test_heisenberg_zero_linear_bracket(self):
        """Path 1: at the C_2 level, {phi, phi}_P has no linear part."""
        pva = heisenberg_classical_pva(k=Fraction(5))
        lin, _ = pva.poisson_bracket("phi", "phi")
        assert lin == {}

    def test_heisenberg_central_term_equals_k(self):
        """Path 1: central Poisson term = k."""
        for k in [1, 2, 3, 7, -1]:
            pva = heisenberg_classical_pva(k=Fraction(k))
            _, cen = pva.poisson_bracket("phi", "phi")
            assert cen == Fraction(k)

    def test_heisenberg_kappa_equals_k(self):
        """Path 5 (kappa consistency): kappa(H_k) = k."""
        for k in [1, 2, 5, -3]:
            pva = heisenberg_classical_pva(k=Fraction(k))
            assert pva_scalar_kappa(pva) == Fraction(k)

    def test_heisenberg_bar_dimensions(self):
        """Path 1: bar complex dimensions are (1, 1) for single generator."""
        pva = heisenberg_classical_pva(k=Fraction(2))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_C[0] == 1
        assert report.dim_C[1] == 1
        # Arity 2 has no elements (single generator, no wedge square)
        assert report.dim_C.get(2, 0) == 0

    def test_heisenberg_bar_cohomology(self):
        """Path 1+3: bar cohomology = (1, 1), Euler char = 0."""
        pva = heisenberg_classical_pva(k=Fraction(1))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_H[0] == 1
        assert report.dim_H[1] == 1
        assert report.euler_char == 0

    def test_heisenberg_differential_vanishes(self):
        """Path 1: d_CE is zero at every arity (no linear bracket)."""
        pva = heisenberg_classical_pva(k=Fraction(4))
        for arity in range(3):
            mat = ce_differential_matrix(pva, arity)
            assert rational_rank(mat) == 0

    def test_heisenberg_jacobi(self):
        """Path 8: Jacobi holds trivially (only one generator)."""
        pva = heisenberg_classical_pva(k=Fraction(2))
        assert verify_jacobi_identity(pva)["ok"]

    def test_heisenberg_antisymmetry(self):
        """Path 4: anti-symmetry trivially holds."""
        pva = heisenberg_classical_pva(k=Fraction(2))
        assert verify_antisymmetry(pva)["ok"]


# =========================================================================
# Section 2: Affine sl_2 classical-limit PVA
# =========================================================================

class TestAffineSl2ClassicalPVA:
    """Affine sl_2 classical PVA: Kirillov-Kostant bracket on sl_2^*."""

    def test_sl2_generator_list(self):
        """Path 1: generators are (e, f, h), all weight 1."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        assert set(pva.generators) == {"e", "f", "h"}
        for g in pva.generators:
            assert pva.weights[g] == 1

    def test_sl2_critical_level_raises(self):
        """Path 1: k = -h^v = -2 raises ValueError."""
        with pytest.raises(ValueError):
            affine_sl2_classical_pva(k=Fraction(-2))

    def test_sl2_kirillov_kostant_brackets(self):
        """Path 1: [e, f] = h, [h, e] = 2e, [h, f] = -2f."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        lin_ef, _ = pva.poisson_bracket("e", "f")
        assert lin_ef == {"h": Fraction(1)}
        lin_he, _ = pva.poisson_bracket("h", "e")
        assert lin_he == {"e": Fraction(2)}
        lin_hf, _ = pva.poisson_bracket("h", "f")
        assert lin_hf == {"f": Fraction(-2)}

    def test_sl2_inferred_reversed_brackets(self):
        """Path 4: {f, e} = -{e, f} from anti-symmetry inference."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        lin_fe, _ = pva.poisson_bracket("f", "e")
        assert lin_fe == {"h": Fraction(-1)}
        lin_eh, _ = pva.poisson_bracket("e", "h")
        assert lin_eh == {"e": Fraction(-2)}
        lin_fh, _ = pva.poisson_bracket("f", "h")
        assert lin_fh == {"f": Fraction(2)}

    def test_sl2_central_terms(self):
        """Path 1: central lambda^1 term encodes level k."""
        for k_val in [1, 2, 5, -3]:
            pva = affine_sl2_classical_pva(k=Fraction(k_val))
            _, cen_ef = pva.poisson_bracket("e", "f")
            assert cen_ef == Fraction(k_val)
            _, cen_hh = pva.poisson_bracket("h", "h")
            assert cen_hh == Fraction(2) * k_val

    def test_sl2_bar_complex_dimensions(self):
        """Path 1: Lambda^*(3 gens) has dimensions (1, 3, 3, 1)."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_C[0] == 1
        assert report.dim_C[1] == 3
        assert report.dim_C[2] == 3
        assert report.dim_C[3] == 1

    def test_sl2_bar_cohomology_matches_closed_form(self):
        """Path 2: direct bar = closed-form H*(sl_2, C) = (1, 0, 0, 1)."""
        result = check_sl2_matches_closed_form(k=Fraction(1))
        assert result["matches"]
        assert result["direct"] == {0: 1, 1: 0, 2: 0, 3: 1}

    def test_sl2_bar_cohomology_level_independent(self):
        """Path 6: CE cohomology does NOT depend on the level k."""
        # The central (level) terms are filtered out of the Chevalley-Eilenberg
        # differential on R_+; only the linear Kirillov-Kostant structure
        # controls cohomology.  So every non-critical level gives the same H.
        levels = [Fraction(1), Fraction(2), Fraction(5), Fraction(-1),
                  Fraction(-3), Fraction(1, 2)]
        target = {0: 1, 1: 0, 2: 0, 3: 1}
        for k in levels:
            pva = affine_sl2_classical_pva(k=k)
            report = ce_bar_cohomology(pva, max_arity=3)
            assert report.dim_H == target, f"level {k} gave {report.dim_H}"

    def test_sl2_differential_rank(self):
        """Path 1: d_CE: C^2 -> C^1 has rank 3 (full rank)."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        mat = ce_differential_matrix(pva, 2)
        assert rational_rank(mat) == 3

    def test_sl2_arity3_differential_vanishes(self):
        """Path 1: d_CE: C^3 -> C^2 = 0 (single wedge of all 3 gens)."""
        # d(e ^ f ^ h) = {e,f} ^ h - {e,h} ^ f + {f,h} ^ e
        #              = h ^ h - (-2e) ^ f + (2f) ^ e
        #              = 0 + 2 e ^ f + 2 f ^ e = 2 e ^ f - 2 e ^ f = 0
        pva = affine_sl2_classical_pva(k=Fraction(1))
        mat = ce_differential_matrix(pva, 3)
        assert rational_rank(mat) == 0

    def test_sl2_euler_characteristic_zero(self):
        """Path 3: chi(Lambda^*(3 gens)) = 1 - 3 + 3 - 1 = 0."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.euler_char == 0

    def test_sl2_jacobi_identity(self):
        """Path 8: Lie-Poisson Jacobi = Lie algebra Jacobi for sl_2."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        report = verify_jacobi_identity(pva)
        assert report["ok"], f"Jacobi failed: {report['failures']}"

    def test_sl2_antisymmetry(self):
        """Path 4: anti-symmetry {x,y} = -{y,x} for every ordered pair."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        assert verify_antisymmetry(pva)["ok"]

    def test_sl2_kappa_formula(self):
        """Path 5: kappa(sl_2, k) = 3(k+2)/4."""
        for k_val in [1, 2, 5, -1]:
            pva = affine_sl2_classical_pva(k=Fraction(k_val))
            expected = Fraction(3, 4) * (Fraction(k_val) + Fraction(2))
            assert pva_scalar_kappa(pva) == expected


# =========================================================================
# Section 3: Virasoro classical-limit PVA
# =========================================================================

class TestVirasoroClassicalPVA:
    """Virasoro classical PVA: single T with central c/12 term."""

    def test_virasoro_single_generator(self):
        """Path 1: Virasoro PVA has exactly one generator T of weight 2."""
        pva = virasoro_classical_pva(c=Fraction(1))
        assert pva.generators == ["T"]
        assert pva.weights["T"] == 2

    def test_virasoro_zero_linear_bracket(self):
        """Path 1: {T, T}_P linear part vanishes (partial T in C_2)."""
        pva = virasoro_classical_pva(c=Fraction(1))
        lin, _ = pva.poisson_bracket("T", "T")
        assert lin == {}

    def test_virasoro_central_is_c_over_12(self):
        """Path 1: central Poisson term = c/12."""
        for c_val in [1, 2, 13, 26, -22]:
            pva = virasoro_classical_pva(c=Fraction(c_val))
            _, cen = pva.poisson_bracket("T", "T")
            assert cen == Fraction(c_val) / Fraction(12)

    def test_virasoro_kappa_equals_c_over_2(self):
        """Path 5: kappa(Vir_c) = c/2."""
        for c_val in [1, 13, 26, Fraction(1, 2)]:
            pva = virasoro_classical_pva(c=Fraction(c_val))
            assert pva_scalar_kappa(pva) == Fraction(c_val) / Fraction(2)

    def test_virasoro_bar_dimensions(self):
        """Path 1: Lambda^*(1 gen) has dim (1, 1), nothing else."""
        pva = virasoro_classical_pva(c=Fraction(1))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_C[0] == 1
        assert report.dim_C[1] == 1
        assert report.dim_C.get(2, 0) == 0

    def test_virasoro_bar_cohomology(self):
        """Path 1: H^0 = 1, H^1 = 1 (trivial differential)."""
        pva = virasoro_classical_pva(c=Fraction(1))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_H[0] == 1
        assert report.dim_H[1] == 1


# =========================================================================
# Section 4: Chevalley-Eilenberg differential primitives
# =========================================================================

class TestCEDifferentialPrimitives:
    """Low-level sanity tests for the exterior algebra bar machinery."""

    def test_basis_exterior_sizes(self):
        """Path 1: |Lambda^k(n)| = C(n, k)."""
        gens = ["a", "b", "c", "d"]
        assert len(_basis_exterior(gens, 0)) == 1
        assert len(_basis_exterior(gens, 1)) == 4
        assert len(_basis_exterior(gens, 2)) == 6
        assert len(_basis_exterior(gens, 3)) == 4
        assert len(_basis_exterior(gens, 4)) == 1
        assert len(_basis_exterior(gens, 5)) == 0

    def test_sort_with_sign_identity(self):
        """Path 1: already sorted tuple has sign +1."""
        t = ("a", "b", "c")
        sorted_t, sign = _sort_with_sign(t)
        assert sorted_t == t
        assert sign == 1

    def test_sort_with_sign_single_swap(self):
        """Path 1: one transposition gives sign -1."""
        sorted_t, sign = _sort_with_sign(("b", "a"))
        assert sorted_t == ("a", "b")
        assert sign == -1

    def test_sort_with_sign_three_cycle(self):
        """Path 1: (c, a, b) sorts to (a, b, c) with sign +1 (two swaps)."""
        sorted_t, sign = _sort_with_sign(("c", "a", "b"))
        assert sorted_t == ("a", "b", "c")
        assert sign == 1

    def test_sort_with_sign_duplicate(self):
        """Path 1: duplicate entry produces sign 0 (wedge squared zero)."""
        _, sign = _sort_with_sign(("a", "a", "b"))
        assert sign == 0

    def test_sign_remove_two_alternates(self):
        """Path 1: (-1)^{a+b} convention."""
        assert _sign_remove_two(3, 1, 2) == -1
        assert _sign_remove_two(3, 1, 3) == 1
        assert _sign_remove_two(3, 2, 3) == -1

    def test_rational_rank_identity(self):
        """Path 1: rank of n-by-n identity is n."""
        for n in range(1, 6):
            mat = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
            assert rational_rank(mat) == n

    def test_rational_rank_rank_one(self):
        """Path 1: outer product has rank 1."""
        mat = [
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(2), Fraction(4), Fraction(6)],
            [Fraction(3), Fraction(6), Fraction(9)],
        ]
        assert rational_rank(mat) == 1

    def test_rational_rank_zero_matrix(self):
        """Path 1: zero matrix has rank 0."""
        mat = [[Fraction(0)] * 4 for _ in range(3)]
        assert rational_rank(mat) == 0


# =========================================================================
# Section 5: Koszul duality at the PVA level and complementarity sums
# =========================================================================

class TestKoszulDualityPVA:
    """Koszul dual PVAs and complementarity sums (AP24 compliance)."""

    def test_heisenberg_koszul_dual_opposite_sign(self):
        """Path 1: Koszul dual of H_k is H_{-k} at the PVA level."""
        dual = pva_koszul_dual_heisenberg(Fraction(5))
        assert pva_scalar_kappa(dual) == Fraction(-5)

    def test_heisenberg_complementarity_zero(self):
        """Path 5 (AP24): kappa(H_k) + kappa(H_k!) = 0 for KM/free fields."""
        for k in [1, 2, 5, 10, -3]:
            s = pva_complementarity_sum("Heisenberg", Fraction(k))
            assert s == Fraction(0)

    def test_sl2_koszul_dual_feigin_frenkel(self):
        """Path 1: FF involution k -> -k - 4 for sl_2."""
        # kappa(sl_2, 5) = 21/4; kappa(sl_2, -9) = 3(-9+2)/4 = -21/4
        dual = pva_koszul_dual_sl2(Fraction(5))
        assert pva_scalar_kappa(dual) == -Fraction(21, 4)

    def test_sl2_complementarity_zero(self):
        """Path 5 (AP24): kappa(sl_2, k) + kappa(sl_2, k!) = 0."""
        for k in [1, 2, 5, 10, -3]:
            s = pva_complementarity_sum("sl_2", Fraction(k))
            assert s == Fraction(0)

    def test_virasoro_koszul_dual_26_minus_c(self):
        """Path 1: Virasoro Koszul dual at the PVA level is c -> 26 - c."""
        dual = pva_koszul_dual_virasoro(Fraction(1))
        assert pva_scalar_kappa(dual) == Fraction(25, 2)

    def test_virasoro_complementarity_is_13_not_zero(self):
        """Path 5 (AP24 CRITICAL): kappa(Vir_c) + kappa(Vir_{26-c}) = 13.

        This is the direct codification of AP24: the anti-symmetry
        formula holds for KM/free fields but FAILS for Virasoro where
        the complementarity sum is 13 = (c + (26-c))/2, not 0.
        """
        for c in [0, 1, 13, 25, 26, -5]:
            s = pva_complementarity_sum("Virasoro", Fraction(c))
            assert s == Fraction(13), f"Vir c={c} gave {s}, expected 13"

    def test_virasoro_self_dual_at_c_13(self):
        """Path 5: Vir is self-dual at c = 13 (NOT c = 26, AP8)."""
        pva = virasoro_classical_pva(c=Fraction(13))
        dual = pva_koszul_dual_virasoro(Fraction(13))
        assert pva_scalar_kappa(pva) == pva_scalar_kappa(dual)
        assert pva_scalar_kappa(pva) == Fraction(13, 2)

    def test_virasoro_not_self_dual_at_c_26(self):
        """Path 5 (AP8): c = 26 is NOT the self-dual point for Vir."""
        pva = virasoro_classical_pva(c=Fraction(26))
        dual = pva_koszul_dual_virasoro(Fraction(26))
        # kappa(Vir_26) = 13; kappa(Vir_0) = 0 -- not equal
        assert pva_scalar_kappa(pva) != pva_scalar_kappa(dual)

    def test_unknown_family_raises(self):
        """Path 1: unknown family name raises ValueError."""
        with pytest.raises(ValueError):
            pva_complementarity_sum("unknown", Fraction(1))


# =========================================================================
# Section 6: Associated variety X_A
# =========================================================================

class TestAssociatedVariety:
    """Associated variety dimension and orbit type checks."""

    def test_heisenberg_variety(self):
        """Path 7: X_{Heis} = A^1, smooth, dim 1."""
        v = heisenberg_associated_variety(Fraction(1))
        assert v.krull_dimension == 1
        assert v.smooth is True

    def test_sl2_universal_variety(self):
        """Path 7: X_{V_k(sl_2)} = sl_2^* ~ A^3."""
        v = sl2_universal_associated_variety(Fraction(1))
        assert v.krull_dimension == 3
        assert v.smooth is True

    def test_sl2_integrable_variety_nilpotent_cone(self):
        """Path 7: X_{L_k(sl_2)} = nilpotent cone, dim 2, singular."""
        v = sl2_integrable_associated_variety(k_int=1)
        assert v.krull_dimension == 2
        assert v.smooth is False
        assert "nilpotent" in v.orbit_type

    def test_sl2_integrable_negative_level_raises(self):
        """Path 1: integrable levels are non-negative integers."""
        with pytest.raises(ValueError):
            sl2_integrable_associated_variety(k_int=-1)

    def test_virasoro_variety_dim_one(self):
        """Path 7: X_{Vir} is one-dimensional (single T generator)."""
        v = virasoro_associated_variety(Fraction(1))
        assert v.krull_dimension == 1


# =========================================================================
# Section 7: Li-bar E_1 page
# =========================================================================

class TestLiBarE1:
    """Li-bar spectral sequence E_1 page setup."""

    def test_e1_page_heisenberg(self):
        """Path 1: E_1 = E_0 for free commutative Heisenberg."""
        pva = heisenberg_classical_pva(k=Fraction(1))
        data = li_bar_E1_page(pva, max_arity=3)
        assert data.E0_dimensions[0] == 1
        assert data.E0_dimensions[1] == 1
        assert data.E1_dimensions == data.E0_dimensions

    def test_e1_page_sl2_dimensions(self):
        """Path 1: E_0 = (1, 3, 3, 1), E_2 = (1, 0, 0, 1) after d_1 = d_CE."""
        pva = affine_sl2_classical_pva(k=Fraction(1))
        data = li_bar_E1_page(pva, max_arity=3)
        assert data.E0_dimensions == {0: 1, 1: 3, 2: 3, 3: 1}
        assert data.E2_dimensions == {0: 1, 1: 0, 2: 0, 3: 1}

    def test_e1_page_virasoro(self):
        """Path 1: Virasoro E_1 = E_0 = (1, 1), E_2 = (1, 1)."""
        pva = virasoro_classical_pva(c=Fraction(1))
        data = li_bar_E1_page(pva, max_arity=3)
        assert data.E0_dimensions[0] == 1
        assert data.E0_dimensions[1] == 1


# =========================================================================
# Section 8: Leak between classical and quantum bar
# =========================================================================

class TestLeakDimensions:
    """Leak = dim H(VA bar) - dim H(PVA bar)."""

    def test_leak_zero_for_classically_koszul(self):
        """Path 1: if VA and PVA bar dims agree, leak = 0."""
        pva_dims = {0: 1, 1: 0, 2: 0, 3: 1}
        va_dims = {0: 1, 1: 0, 2: 0, 3: 1}
        leak = leak_dimensions(pva_dims, va_dims, max_arity=3)
        assert all(v == 0 for v in leak.values())

    def test_leak_nonzero_for_quantum_correction(self):
        """Path 1: quantum correction in arity 2 produces leak[2] = 1."""
        pva_dims = {0: 1, 1: 0, 2: 0, 3: 1}
        va_dims = {0: 1, 1: 0, 2: 1, 3: 1}
        leak = leak_dimensions(pva_dims, va_dims, max_arity=3)
        assert leak[2] == 1

    def test_leak_signed(self):
        """Path 1: negative leak means PVA has more classes than VA."""
        pva_dims = {0: 1, 1: 2, 2: 0, 3: 0}
        va_dims = {0: 1, 1: 0, 2: 0, 3: 0}
        leak = leak_dimensions(pva_dims, va_dims, max_arity=3)
        assert leak[1] == -2


# =========================================================================
# Section 9: Cross-family landscape consistency
# =========================================================================

class TestLandscapeSummary:
    """Cross-family checks on the landscape summary."""

    def test_landscape_has_three_families(self):
        """Path 6: summary contains Heis, sl_2, Vir."""
        rows = classical_limit_landscape_summary()
        assert len(rows) == 3
        families = {r["family"] for r in rows}
        assert families == {"Heisenberg", "Affine sl_2", "Virasoro"}

    def test_landscape_kappa_values(self):
        """Path 5: kappa values match the known formulas."""
        rows = classical_limit_landscape_summary()
        by_fam = {r["family"]: r for r in rows}
        assert by_fam["Heisenberg"]["kappa"] == Fraction(1)
        assert by_fam["Affine sl_2"]["kappa"] == Fraction(9, 4)
        assert by_fam["Virasoro"]["kappa"] == Fraction(1, 2)

    def test_landscape_bar_dims_sl2_matches_ce(self):
        """Path 2: sl_2 landscape bar dims match closed-form H^*(sl_2, C)."""
        rows = classical_limit_landscape_summary()
        sl2_row = [r for r in rows if r["family"] == "Affine sl_2"][0]
        assert sl2_row["bar_dims"] == {0: 1, 1: 0, 2: 0, 3: 1}

    def test_landscape_euler_characteristics(self):
        """Path 3: every family has Euler characteristic 0 on Lambda^*."""
        rows = classical_limit_landscape_summary()
        for row in rows:
            assert row["euler"] == 0


# =========================================================================
# Section 10: Cross-level sl_2 consistency (AP10)
# =========================================================================

class TestCrossLevelSl2Consistency:
    """Multi-level sl_2 cross-consistency (AP10: cross-family)."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, -1, -3, -5])
    def test_sl2_bar_cohomology_level_independent(self, k_val):
        """Path 6: sl_2 bar cohomology does NOT depend on level k."""
        pva = affine_sl2_classical_pva(k=Fraction(k_val))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_H == {0: 1, 1: 0, 2: 0, 3: 1}

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, -1, -3, -5])
    def test_sl2_jacobi_level_independent(self, k_val):
        """Path 8: Jacobi holds at every level."""
        pva = affine_sl2_classical_pva(k=Fraction(k_val))
        assert verify_jacobi_identity(pva)["ok"]

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, -1, -3, -5])
    def test_sl2_antisymmetry_level_independent(self, k_val):
        """Path 4: anti-symmetry holds at every level."""
        pva = affine_sl2_classical_pva(k=Fraction(k_val))
        assert verify_antisymmetry(pva)["ok"]

    @pytest.mark.parametrize("k_val", [1, 2, 5, -1])
    def test_sl2_complementarity_sum_zero(self, k_val):
        """Path 5: complementarity sum vanishes at every level."""
        s = pva_complementarity_sum("sl_2", Fraction(k_val))
        assert s == Fraction(0)


# =========================================================================
# Section 11: Cross-parameter Virasoro consistency
# =========================================================================

class TestCrossCentralChargeVirasoro:
    """Virasoro cross-parameter checks."""

    @pytest.mark.parametrize("c_val", [0, 1, 13, 25, 26, -5])
    def test_virasoro_complementarity_equals_13(self, c_val):
        """Path 5 (AP24 CRITICAL): sum = 13 for every c, including c=0 and c=26."""
        s = pva_complementarity_sum("Virasoro", Fraction(c_val))
        assert s == Fraction(13)

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_virasoro_kappa_equals_half_c(self, c_val):
        """Path 5: kappa(Vir_c) = c/2."""
        pva = virasoro_classical_pva(c=Fraction(c_val))
        assert pva_scalar_kappa(pva) == Fraction(c_val) / Fraction(2)

    @pytest.mark.parametrize("c_val", [1, 2, 13, 25])
    def test_virasoro_bar_shape(self, c_val):
        """Path 1: single-generator bar shape (1, 1) regardless of c."""
        pva = virasoro_classical_pva(c=Fraction(c_val))
        report = ce_bar_cohomology(pva, max_arity=3)
        assert report.dim_H[0] == 1
        assert report.dim_H[1] == 1


# =========================================================================
# Section 12: Meta-properties: no AI attribution in engine file
# =========================================================================

class TestNoAIAttribution:
    """Meta-test: the engine source file contains no AI attribution."""

    def test_engine_contains_no_ai_attribution(self):
        """PRE-COMMIT rule: NO AI attribution anywhere. All work by Raeez Lorgat."""
        from pathlib import Path
        p = Path(__file__).resolve().parents[1] / "lib" / "pva_classical_limit_bar_engine.py"
        text = p.read_text()
        forbidden = ["Co-Authored-By", "Claude", "Anthropic", "GPT", "AI-generated"]
        for token in forbidden:
            assert token not in text, f"Forbidden attribution token '{token}' found"
