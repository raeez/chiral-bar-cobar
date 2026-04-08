r"""Tests for the universal chiral genus extension engine.

Verifies the three-tier architecture (thm:three-tier-architecture):
  Tier 0: MC existence is unconditional for ALL chiral algebras.
  Tier 1: Koszul algebras have computable shadows and full engine.
  Tier 2: Finitely generated Koszul algebras have analytic convergence.

Multi-path verification on kappa values cross-checks against
known formulas from landscape_census.tex (AP1, AP10, AP39).
"""

from fractions import Fraction

import pytest

from compute.lib.theorem_universal_chiral_genus_extension_engine import (
    ChiralAlgebraData,
    GenusExtensionResult,
    admissible_level_simple_quotient,
    affine_km,
    analyze_all_standard_families,
    beta_gamma,
    classify_genus_extension,
    compare_genus_extension_methods,
    curve_independence_check,
    four_regime_hierarchy,
    genus_zero_determines,
    heisenberg,
    lattice_voa,
    non_koszul_hypothetical,
    non_lie_conformal_example,
    verify_tier_chain,
    virasoro,
    w_algebra,
    w_infinity,
)


# =================================================================
# 1. Constructor smoke tests: every family builds without error
# =================================================================

class TestFamilyConstructors:
    """Each standard family constructor returns valid ChiralAlgebraData."""

    def test_heisenberg_basic(self):
        A = heisenberg(1)
        assert A.family == "Heisenberg"
        assert A.num_generators == 1
        assert A.generator_weights == (1,)

    def test_heisenberg_level(self):
        A = heisenberg(5)
        assert A.kappa == 5
        assert A.central_charge == 5

    def test_affine_km_sl2(self):
        A = affine_km("A", 1, 1)
        assert A.family == "affine_KM"
        # dim(sl_2) = 3, h^v = 2, k=1 => kappa = 3*(1+2)/(2*2) = 9/4
        assert A.kappa == Fraction(9, 4)

    def test_affine_km_sl3(self):
        A = affine_km("A", 2, 1)
        # dim(sl_3) = 8, h^v = 3, k=1 => kappa = 8*(1+3)/(2*3) = 16/3
        assert A.kappa == Fraction(16, 3)

    def test_affine_km_critical_level_raises(self):
        """Critical level k = -h^v must raise an error."""
        with pytest.raises(ValueError, match="Critical level"):
            affine_km("A", 1, -2)  # h^v(sl_2) = 2

    def test_virasoro_basic(self):
        A = virasoro(1)
        assert A.kappa == Fraction(1, 2)
        assert A.generator_weights == (2,)
        assert A.max_pole_order == 4
        assert A.shadow_depth == -1  # class M

    def test_virasoro_c26_critical(self):
        A = virasoro(26)
        assert A.kappa == 13

    def test_virasoro_c0(self):
        A = virasoro(0)
        assert A.kappa == 0

    def test_w_algebra_w3(self):
        A = w_algebra(3, 1)
        assert A.family == "W_algebra"
        assert A.num_generators == 2
        assert A.generator_weights == (2, 3)
        assert A.max_pole_order == 6

    def test_w_algebra_w4(self):
        A = w_algebra(4, 1)
        assert A.num_generators == 3
        assert A.generator_weights == (2, 3, 4)
        assert A.max_pole_order == 8

    def test_beta_gamma_lam1(self):
        A = beta_gamma(1)
        assert A.num_generators == 2
        assert A.generator_weights == (1, 0)
        assert A.shadow_depth == 4  # class C
        assert A.is_positive_energy is True

    def test_beta_gamma_lam0_nonpositive_energy(self):
        """beta-gamma at lambda=0 has a weight-0 generator (AP18)."""
        A = beta_gamma(0)
        assert A.is_positive_energy is False

    def test_lattice_voa(self):
        A = lattice_voa(24)
        assert A.kappa == 24
        assert A.central_charge == 24
        assert A.shadow_depth == 2  # class G

    def test_w_infinity(self):
        A = w_infinity()
        assert A.num_generators == -1
        assert A.has_hs_sewing is False
        assert A.regime == "programmatic"

    def test_non_lie_conformal(self):
        A = non_lie_conformal_example()
        assert A.is_koszul is True
        assert A.has_hs_sewing is True

    def test_non_koszul_hypothetical(self):
        A = non_koszul_hypothetical()
        assert A.is_koszul is False


# =================================================================
# 2. Tier 0: MC existence is unconditional for ALL chiral algebras
# =================================================================

class TestTier0Unconditional:
    """D^2 = 0 holds for ALL chiral algebras, including non-Koszul."""

    @pytest.mark.parametrize("factory", [
        lambda: heisenberg(1),
        lambda: affine_km("A", 1, 1),
        lambda: virasoro(1),
        lambda: w_algebra(3, 1),
        lambda: beta_gamma(0),
        lambda: w_infinity(),
        lambda: non_koszul_hypothetical(),
        lambda: non_lie_conformal_example(),
        lambda: lattice_voa(8),
        lambda: admissible_level_simple_quotient("A", 2, 2, 3),
    ])
    def test_mc_exists_unconditional(self, factory):
        """Theta_A exists for every chiral algebra (thm:mc2-bar-intrinsic)."""
        A = factory()
        result = classify_genus_extension(A)
        assert result.mc_exists is True

    def test_non_koszul_still_has_mc(self):
        """Non-Koszul algebras have MC at Tier 0 but not full engine."""
        A = non_koszul_hypothetical()
        result = classify_genus_extension(A)
        assert result.mc_exists is True
        assert result.tier == 0
        assert result.full_engine is False

    def test_genus_zero_always_gives_mc(self):
        """genus_zero_determines always reports MC existence."""
        A = non_koszul_hypothetical()
        analysis = genus_zero_determines(A)
        assert analysis["genus_0_gives_mc"] is True
        assert analysis["tier_0_unconditional"]["mc_element_exists"] is True
        assert analysis["tier_0_unconditional"]["shadow_tower_converges"] is True


# =================================================================
# 3. Tier classification: Koszul => Tier 1+, finitely gen => Tier 2
# =================================================================

class TestTierClassification:
    """Correct tier assignment for each family."""

    def test_heisenberg_tier2(self):
        result = classify_genus_extension(heisenberg(1))
        assert result.tier == 2
        assert result.full_engine is True
        assert result.analytic_convergence is True

    def test_virasoro_tier2(self):
        result = classify_genus_extension(virasoro(1))
        assert result.tier == 2

    def test_affine_km_tier2(self):
        result = classify_genus_extension(affine_km("A", 1, 1))
        assert result.tier == 2

    def test_w_algebra_tier2(self):
        result = classify_genus_extension(w_algebra(3, 1))
        assert result.tier == 2

    def test_lattice_tier2(self):
        result = classify_genus_extension(lattice_voa(24))
        assert result.tier == 2

    def test_w_infinity_not_tier2(self):
        """W_infinity: Koszul but infinitely generated, HS-sewing unverified."""
        result = classify_genus_extension(w_infinity())
        # MC4 proved, so Koszul and PBW hold, but HS-sewing is False
        assert result.mc_exists is True
        assert result.full_engine is True
        assert result.analytic_convergence is False
        assert result.tier == 1

    def test_non_koszul_tier0(self):
        result = classify_genus_extension(non_koszul_hypothetical())
        assert result.tier == 0

    def test_beta_gamma_lam0_tier0(self):
        """beta-gamma at lambda=0: positive energy fails (AP18)."""
        result = classify_genus_extension(beta_gamma(0))
        # has_pbw is True but is_positive_energy is False
        # shadow_computable requires BOTH
        assert result.shadow_computable is False
        assert result.tier == 0

    def test_beta_gamma_lam1_tier2(self):
        result = classify_genus_extension(beta_gamma(1))
        assert result.tier == 2

    def test_admissible_sl2_koszul(self):
        """L_k(sl_2) at admissible level: Koszul is PROVED."""
        A = admissible_level_simple_quotient("A", 1, 2, 3)
        assert A.is_koszul is True
        result = classify_genus_extension(A)
        assert result.tier == 2

    def test_admissible_sl3_koszul_open(self):
        """L_k(sl_3) at admissible level: Koszulness is OPEN for rank >= 2."""
        A = admissible_level_simple_quotient("A", 2, 2, 3)
        assert A.is_koszul is False
        result = classify_genus_extension(A)
        assert result.tier == 0


# =================================================================
# 4. Tier chain: P4 => P3 => P2 => P1
# =================================================================

class TestTierChain:
    """The implication chain must be consistent for all families."""

    @pytest.mark.parametrize("factory", [
        lambda: heisenberg(1),
        lambda: affine_km("A", 1, 1),
        lambda: virasoro(26),
        lambda: w_algebra(3, 1),
        lambda: beta_gamma(1),
        lambda: lattice_voa(8),
        lambda: w_infinity(),
        lambda: non_koszul_hypothetical(),
    ])
    def test_chain_valid(self, factory):
        """P4 => P3 => P2 => P1 must never be violated."""
        chain = verify_tier_chain(factory())
        assert chain["chain_valid"] is True
        # P1 always holds
        assert chain["P1_d_squared"] is True

    def test_chain_p4_implies_p3(self):
        """If HS-sewing holds, the algebra must be Koszul."""
        for A_factory in [heisenberg, lambda: affine_km("A", 1, 1), virasoro]:
            A = A_factory() if callable(A_factory) else A_factory
            chain = verify_tier_chain(A)
            if chain["P4_hs_sewing"]:
                assert chain["P3_koszul"] is True

    def test_chain_p3_implies_p2(self):
        """Koszul implies PBW (bar SS collapse implies PBW filtration)."""
        A = virasoro(1)
        chain = verify_tier_chain(A)
        if chain["P3_koszul"]:
            assert chain["P2_pbw"] is True


# =================================================================
# 5. Curve independence
# =================================================================

class TestCurveIndependence:
    """prop:genus0-curve-independence: bar complex at genus 0 is
    curve-independent for all algebras."""

    @pytest.mark.parametrize("factory", [
        lambda: heisenberg(1),
        lambda: virasoro(1),
        lambda: non_koszul_hypothetical(),
        lambda: w_infinity(),
    ])
    def test_genus0_always_curve_independent(self, factory):
        check = curve_independence_check(factory())
        assert check["genus_0_curve_independent"] is True

    def test_koszul_has_pbw_propagation(self):
        check = curve_independence_check(virasoro(1))
        assert check["pbw_propagation"] is True
        assert "kappa(A)" in check["algebraic_invariants_determined"]

    def test_non_koszul_no_pbw_propagation(self):
        check = curve_independence_check(non_koszul_hypothetical())
        assert "pbw_propagation" not in check

    def test_boundary_curve_independence_conjectured(self):
        """Higher-genus boundary curve independence is still conjectured."""
        check = curve_independence_check(heisenberg(1))
        assert check["higher_genus_boundary"] == "conjectured"
        assert check["all_genera_unconditional"] is False


# =================================================================
# 6. Genus-0 determines analysis
# =================================================================

class TestGenusZeroDetermines:
    """genus_zero_determines returns correct tier-specific data."""

    def test_tier2_has_all_tiers(self):
        analysis = genus_zero_determines(heisenberg(1))
        assert "tier_0_unconditional" in analysis
        assert "tier_0_plus" in analysis
        assert "tier_1" in analysis
        assert "tier_2" in analysis
        assert analysis["genus_0_is_sufficient"] is True

    def test_tier1_missing_tier2(self):
        analysis = genus_zero_determines(w_infinity())
        assert "tier_1" in analysis
        assert "tier_2" not in analysis

    def test_tier0_minimal(self):
        analysis = genus_zero_determines(non_koszul_hypothetical())
        assert "tier_0_unconditional" in analysis
        assert "tier_1" not in analysis
        assert "tier_2" not in analysis
        assert analysis["genus_0_is_sufficient"] is False

    def test_lie_conformal_not_required(self):
        """Lie conformal generation is NOT necessary for genus extension."""
        analysis = genus_zero_determines(non_lie_conformal_example())
        assert analysis["lie_conformal_required"] is False
        assert analysis["tier"] == 2  # non-Lie-conformal but still tier 2


# =================================================================
# 7. Four-regime hierarchy
# =================================================================

class TestFourRegimeHierarchy:
    """The four bar-cobar regimes: quadratic, curved-central,
    filtered-complete, programmatic."""

    def test_hierarchy_has_four_regimes(self):
        h = four_regime_hierarchy()
        assert set(h.keys()) == {
            "quadratic", "curved_central",
            "filtered_complete", "programmatic",
        }

    def test_all_regimes_have_mc(self):
        """D^2 = 0 in every regime."""
        for regime, data in four_regime_hierarchy().items():
            assert data["mc_exists"] is True, f"{regime} must have MC"

    def test_all_regimes_have_inversion(self):
        """Bar-cobar inversion works in every regime (MC4 proved)."""
        for regime, data in four_regime_hierarchy().items():
            assert data["bar_cobar_inversion"] is True

    def test_heisenberg_is_quadratic(self):
        A = heisenberg(1)
        assert A.regime == "quadratic"

    def test_virasoro_is_curved_central(self):
        A = virasoro(1)
        assert A.regime == "curved-central"

    def test_w_algebra_is_filtered_complete(self):
        A = w_algebra(3, 1)
        assert A.regime == "filtered-complete"

    def test_w_infinity_is_programmatic(self):
        A = w_infinity()
        assert A.regime == "programmatic"


# =================================================================
# 8. Multi-path kappa verification (AP1, AP10, AP39)
# =================================================================

class TestKappaMultiPath:
    """Cross-check kappa values against independent formulas.

    Path 1: direct from constructor (engine formula).
    Path 2: recompute from defining formula dim(g)*(k+h^v)/(2*h^v).
    Path 3: limiting/special cases.
    """

    def test_heisenberg_kappa_direct(self):
        """kappa(H_k) = k.  Path 1: constructor."""
        for k in [1, 2, 5, 10]:
            assert heisenberg(k).kappa == k

    def test_heisenberg_kappa_equals_c(self):
        """For Heisenberg: kappa = c (both equal k). Path 3: identity."""
        for k in [1, 3, 7]:
            A = heisenberg(k)
            assert A.kappa == A.central_charge

    def test_virasoro_kappa_is_c_over_2(self):
        """kappa(Vir_c) = c/2.  Path 1 vs Path 2."""
        for c in [1, 2, 26, 0, -2]:
            A = virasoro(c)
            assert A.kappa == Fraction(c, 2)

    def test_affine_sl2_kappa_formula(self):
        """kappa(V^k(sl_2)) = dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4.
        Path 2: independent recomputation."""
        for k in [1, 2, 3, 5]:
            A = affine_km("A", 1, k)
            expected = Fraction(3 * (k + 2), 4)
            assert A.kappa == expected, (
                f"kappa(sl_2, k={k}): got {A.kappa}, expected {expected}"
            )

    def test_affine_sl3_kappa_formula(self):
        """kappa(V^k(sl_3)) = 8*(k+3)/6 = 4*(k+3)/3.
        dim(sl_3)=8, h^v=3."""
        for k in [1, 2, 4]:
            A = affine_km("A", 2, k)
            expected = Fraction(4 * (k + 3), 3)
            assert A.kappa == expected

    def test_affine_e8_kappa_formula(self):
        """kappa(V^1(E_8)) = 248*(1+30)/(2*30) = 248*31/60.
        dim(E_8)=248, h^v=30."""
        A = affine_km("E", 8, 1)
        expected = Fraction(248 * 31, 60)
        assert A.kappa == expected

    def test_lattice_kappa_equals_rank(self):
        """kappa(V_Lambda) = rank.  Path 1 vs Path 3."""
        for r in [1, 8, 16, 24]:
            assert lattice_voa(r).kappa == r

    def test_kappa_not_equal_c_over_2_for_affine(self):
        """AP39: kappa != c/2 for affine KM at rank > 1 generically."""
        A = affine_km("A", 2, 1)
        c_over_2 = A.central_charge / 2
        # kappa = 16/3, c = 8*1/(1+3) = 2, c/2 = 1
        assert A.kappa != c_over_2

    def test_heisenberg_kappa_additivity(self):
        """kappa is additive: kappa(H_k1 + H_k2) = k1 + k2.
        Path 5: cross-family consistency."""
        k1, k2 = 3, 7
        assert heisenberg(k1).kappa + heisenberg(k2).kappa == k1 + k2


# =================================================================
# 9. Compare genus extension methods
# =================================================================

class TestCompareGenusExtensionMethods:

    def test_three_methods_returned(self):
        comp = compare_genus_extension_methods()
        assert "bar_intrinsic" in comp
        assert "factorization_envelope" in comp
        assert "chiral_homology_gluing" in comp

    def test_bar_intrinsic_is_most_general(self):
        comp = compare_genus_extension_methods()
        assert comp["bar_intrinsic"]["scope"] == "all chiral algebras"
        assert comp["bar_intrinsic"]["hypothesis"] == "none (D^2 = 0 unconditional)"

    def test_factorization_envelope_restricted(self):
        comp = compare_genus_extension_methods()
        assert "Lie conformal" in comp["factorization_envelope"]["scope"]


# =================================================================
# 10. Analyze all standard families (integration test)
# =================================================================

class TestAnalyzeAllStandardFamilies:

    def test_runs_without_error(self):
        results = analyze_all_standard_families()
        assert len(results) >= 20

    def test_all_have_mc(self):
        """Every family in the standard landscape has MC existence."""
        for r in analyze_all_standard_families():
            assert r["mc_exists"] is True, f"{r['name']} must have MC"

    def test_koszul_positive_energy_families_tier_at_least_1(self):
        """Koszul + positive energy => tier >= 1.
        beta_gamma(0) is Koszul but NOT positive-energy (AP18:
        weight-0 generator), so it remains at tier 0."""
        for r in analyze_all_standard_families():
            if r["koszul"] and r["name"] != "betagamma_0":
                assert r["tier"] >= 1, (
                    f"{r['name']}: Koszul but tier {r['tier']}"
                )

    def test_non_koszul_tier_0(self):
        for r in analyze_all_standard_families():
            if not r["koszul"]:
                assert r["tier"] == 0, (
                    f"{r['name']}: non-Koszul but tier {r['tier']}"
                )


# =================================================================
# 11. Shadow depth consistency
# =================================================================

class TestShadowDepthConsistency:
    """Shadow depth class assignment matches CLAUDE.md taxonomy:
    G=2, L=3, C=4, M=infinite(-1)."""

    def test_heisenberg_class_g(self):
        assert heisenberg(1).shadow_depth == 2

    def test_affine_km_class_l(self):
        assert affine_km("A", 1, 1).shadow_depth == 3

    def test_beta_gamma_class_c(self):
        assert beta_gamma(1).shadow_depth == 4

    def test_virasoro_class_m(self):
        assert virasoro(1).shadow_depth == -1

    def test_w_algebra_class_m(self):
        assert w_algebra(3, 1).shadow_depth == -1

    def test_lattice_class_g(self):
        assert lattice_voa(24).shadow_depth == 2


# =================================================================
# 12. Obstructions are correctly reported
# =================================================================

class TestObstructions:

    def test_non_koszul_obstruction_message(self):
        result = classify_genus_extension(non_koszul_hypothetical())
        obs = " ".join(result.obstructions)
        assert "spectral sequence" in obs.lower() or "Koszul" in obs

    def test_w_infinity_hs_obstruction(self):
        result = classify_genus_extension(w_infinity())
        obs = " ".join(result.obstructions)
        assert "sewing" in obs.lower() or "analytic" in obs.lower()

    def test_tier2_no_obstructions(self):
        result = classify_genus_extension(heisenberg(1))
        assert len(result.obstructions) == 0

    def test_beta_gamma_lam0_energy_obstruction(self):
        result = classify_genus_extension(beta_gamma(0))
        obs = " ".join(result.obstructions)
        assert "L_0" in obs or "bounded" in obs.lower()


# =================================================================
# 13. Verification paths populated correctly
# =================================================================

class TestVerificationPaths:

    def test_verification_dict_keys(self):
        result = classify_genus_extension(virasoro(1))
        vp = result.verification_paths
        assert "P1_d_squared_zero" in vp
        assert "P2_pbw" in vp
        assert "P3_koszul" in vp
        assert "P4_analytic" in vp
        assert "regime" in vp

    def test_p1_always_true(self):
        for factory in [heisenberg, virasoro, non_koszul_hypothetical]:
            A = factory() if callable(factory) else factory
            vp = classify_genus_extension(A).verification_paths
            assert vp["P1_d_squared_zero"] is True


# =================================================================
# 14. Edge cases and boundary conditions
# =================================================================

class TestEdgeCases:

    def test_virasoro_half_integer_c(self):
        A = virasoro(Fraction(1, 2))
        assert A.kappa == Fraction(1, 4)
        result = classify_genus_extension(A)
        assert result.tier == 2

    def test_virasoro_negative_c(self):
        A = virasoro(-2)
        assert A.kappa == -1
        result = classify_genus_extension(A)
        assert result.tier == 2

    def test_affine_km_exceptional_types(self):
        """All exceptional Lie types should work."""
        for (t, r) in [("G", 2), ("F", 4), ("E", 6), ("E", 7), ("E", 8)]:
            A = affine_km(t, r, 1)
            result = classify_genus_extension(A)
            assert result.tier == 2, f"{t}_{r} should be tier 2"

    def test_w_algebra_critical_level_raises(self):
        with pytest.raises(ValueError):
            w_algebra(3, -3)  # k + N = 0 for sl_3
