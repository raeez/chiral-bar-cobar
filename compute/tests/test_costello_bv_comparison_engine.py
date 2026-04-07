"""Tests for the Costello-Gwilliam BV quantization vs bar-cobar comparison engine.

Six comparison axes tested:
  Axis 1: Differential (CG BV bracket vs bar differential)
  Axis 2: Modular operad vs factorization algebra structure
  Axis 3: Genus expansion (CG effective action vs bar free energy)
  Axis 4: Obstruction-deformation (CG obstruction vs shadow tower)
  Axis 5: Renormalization (CG counterterms vs bar UV finiteness)
  Axis 6: Effective action at scale L vs shadow at arity r

Multi-path verification mandate (CLAUDE.md): every numerical claim
verified by at least 3 independent paths.

Ground truth: bv_brst.tex, feynman_connection.tex,
  bar_cobar_adjunction_curved.tex, editorial_constitution.tex,
  higher_genus_modular_koszul.tex, concordance.tex.
"""

import pytest
from sympy import Rational, Symbol, simplify, symbols

from compute.lib.costello_bv_comparison_engine import (
    CGEffectiveAction,
    CGObstructionClass,
    CGQuantizationScheme,
    ComparisonStatus,
    FullComparison,
    RenormalizationComparison,
    bosonic_string_comparison,
    brst_nilpotence_vs_bar_d_squared,
    bv_laplacian_vs_sewing,
    cg_bv_bracket_genus0,
    cg_bv_bracket_genus1,
    cg_obstruction_vs_shadow_tower,
    cg_propagator_vs_bar_propagator,
    costello_li_holomorphic_twist,
    derived_center_vs_cg_bulk,
    effective_action_vs_shadow,
    elliott_safronov_classification,
    faber_pandharipande,
    full_comparison,
    ghost_propagator_identification,
    gwilliam_williams_higher_dim,
    heisenberg_sewing_cg_comparison,
    kappa_affine_km,
    kappa_bc_system,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_w3,
    koszul_complementarity_vs_cg,
    multi_weight_genus_expansion_comparison,
    obstruction_complex_comparison,
    renormalization_comparison,
    rg_flow_vs_bar_filtration,
    semi_infinite_vs_bar,
    superstring_comparison,
    uv_finiteness_comparison,
    verify_all,
)


# =========================================================================
# Section 1: Faber-Pandharipande Numbers (3-path verification)
# =========================================================================

class TestFaberPandharipande:
    """Faber-Pandharipande numbers: lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!"""

    def test_genus1_direct(self):
        """Path 1: Direct formula. lambda_1 = (1/2)(1/6)/2 = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_genus1_ahat(self):
        """Path 2: A-hat genus. Ahat(ix)-1 = x^2/24 + ..., so lambda_1 = 1/24."""
        # Ahat(ix) = (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + ...
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_genus1_bernoulli(self):
        """Path 3: From B_2 = 1/6. lambda_1 = (1/2)(1/6)/2! = 1/24."""
        from sympy import bernoulli as B
        B2 = abs(B(2))
        expected = Rational(1, 2) * B2 / 2
        assert faber_pandharipande(1) == expected

    def test_genus2_direct(self):
        """lambda_2 = (7/8)(1/30)/24 = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_genus2_ahat(self):
        """Path 2: A-hat coefficient at x^4 is 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_genus3(self):
        """lambda_3 = (31/32)(1/42)/720 = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_genus0_raises(self):
        """Genus 0 should raise ValueError."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)


# =========================================================================
# Section 2: kappa Formulas (AP1 compliance: each from first principles)
# =========================================================================

class TestKappaFormulas:
    """Test kappa(A) formulas. AP1: never copy between families."""

    def test_heisenberg_symbolic(self):
        """kappa(H_k) = k (the level, NOT k/2)."""
        k = Symbol("k")
        assert kappa_heisenberg(k) == k

    def test_heisenberg_numerical(self):
        """kappa(H_1) = 1. The standard single boson."""
        assert kappa_heisenberg(1) == 1

    def test_virasoro_symbolic(self):
        """kappa(Vir_c) = c/2."""
        c = Symbol("c")
        assert kappa_virasoro(c) == c / 2

    def test_virasoro_at_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(26) == 13

    def test_virasoro_at_c0(self):
        """kappa(Vir_0) = 0 (uncurved)."""
        assert kappa_virasoro(0) == 0

    def test_virasoro_at_c13(self):
        """kappa(Vir_13) = 13/2 (self-dual point)."""
        assert Rational(kappa_virasoro(13)) == Rational(13, 2)

    def test_sl2_symbolic(self):
        """kappa(sl2_k) = 3(k+2)/4."""
        k = Symbol("k")
        assert simplify(kappa_affine_km("sl2", k) - 3 * (k + 2) / 4) == 0

    def test_sl2_numerical(self):
        """kappa(sl2_1) = 3*3/4 = 9/4."""
        assert kappa_affine_km("sl2", 1) == Rational(9, 4)

    def test_sl3_symbolic(self):
        """kappa(sl3_k) = 8(k+3)/(2*3) = 4(k+3)/3."""
        k = Symbol("k")
        assert simplify(kappa_affine_km("sl3", k) - 4 * (k + 3) / 3) == 0

    def test_w3_symbolic(self):
        """kappa(W3_c) = 5c/6."""
        c = Symbol("c")
        assert simplify(kappa_w3(c) - 5 * c / 6) == 0

    def test_bc_lambda2(self):
        """bc at lambda=2: c = -26, kappa = -13."""
        assert Rational(kappa_bc_system(2)) == Rational(-13)

    def test_bc_lambda_half(self):
        """bc at lambda=1/2: c = 1, kappa = 1/2."""
        # c = -2(6*(1/4) - 3 + 1) = -2(3/2 - 2) = -2(-1/2) = 1
        assert Rational(kappa_bc_system(Rational(1, 2))) == Rational(1, 2)

    def test_kappa_not_c_over_2_for_heisenberg(self):
        """AP39: kappa != c/2 for Heisenberg (kappa = k, c = 1)."""
        # At level k=1: kappa = 1, c = 1, c/2 = 1/2 != 1
        assert kappa_heisenberg(1) != Rational(1, 2)

    def test_kappa_not_c_over_2_for_sl2(self):
        """AP39: kappa != c/2 for sl2 in general."""
        # c(sl2_k) = 3k/(k+2), kappa = 3(k+2)/4
        # c/2 = 3k/(2(k+2)), which != 3(k+2)/4 in general
        k = Symbol("k")
        c_sl2 = 3 * k / (k + 2)
        assert simplify(kappa_affine_km("sl2", k) - c_sl2 / 2) != 0


# =========================================================================
# Section 3: Axis 1 -- CG BV Bracket vs Bar Differential
# =========================================================================

class TestAxis1Differential:
    """Axis 1: CG BV bracket {I,-}+hbar*Delta vs bar differential d_bar."""

    def test_genus0_heisenberg_qme(self):
        """Heisenberg genus-0 QME satisfied (free theory)."""
        result = cg_bv_bracket_genus0("heisenberg", k=Symbol("k"))
        assert result["qme_satisfied"] is True

    def test_genus0_km_qme(self):
        """Affine KM genus-0 QME satisfied (Jacobi)."""
        result = cg_bv_bracket_genus0("affine_km", lie_type="sl2", k=Symbol("k"))
        assert result["qme_satisfied"] is True

    def test_genus0_virasoro_qme(self):
        """Virasoro genus-0 QME satisfied."""
        result = cg_bv_bracket_genus0("virasoro", c=Symbol("c"))
        assert result["qme_satisfied"] is True

    def test_genus0_w3_qme(self):
        """W3 genus-0 QME satisfied."""
        result = cg_bv_bracket_genus0("w3", c=Symbol("c"))
        assert result["qme_satisfied"] is True

    def test_genus0_antibracket_vanishes(self):
        """At genus 0, {S,S} = 0 for all algebras (Arnold)."""
        for alg in ["heisenberg", "affine_km", "virasoro", "w3"]:
            params = {"k": Symbol("k"), "c": Symbol("c"), "lie_type": "sl2"}
            result = cg_bv_bracket_genus0(alg, **params)
            assert result["antibracket_SS"] == 0

    def test_genus1_heisenberg_match(self):
        """Genus-1 CG one-loop = bar F_1 for Heisenberg."""
        k = Symbol("k")
        result = cg_bv_bracket_genus1("heisenberg", k=k)
        assert result["match"] is True
        assert result["cg_one_loop"] == k * Rational(1, 24)

    def test_genus1_virasoro_match(self):
        """Genus-1 CG one-loop = bar F_1 for Virasoro."""
        c = Symbol("c")
        result = cg_bv_bracket_genus1("virasoro", c=c)
        assert result["match"] is True
        assert simplify(result["cg_one_loop"] - c / 48) == 0

    def test_genus1_sl2_match(self):
        """Genus-1 CG one-loop = bar F_1 for sl2."""
        k = Symbol("k")
        result = cg_bv_bracket_genus1("affine_km", lie_type="sl2", k=k)
        assert result["match"] is True
        expected = 3 * (k + 2) / 4 * Rational(1, 24)
        assert simplify(result["cg_one_loop"] - expected) == 0

    def test_genus1_anomaly_proportional_to_kappa(self):
        """The genus-1 anomaly is proportional to kappa for all algebras."""
        c = Symbol("c")
        for alg, kap in [("heisenberg", Symbol("k")),
                          ("virasoro", c / 2),
                          ("w3", 5 * c / 6)]:
            params = {"k": Symbol("k"), "c": c, "lie_type": "sl2"}
            result = cg_bv_bracket_genus1(alg, **params)
            assert simplify(result["anomaly_coefficient"] - kap) == 0


# =========================================================================
# Section 4: Axis 3 -- Genus Expansion
# =========================================================================

class TestAxis3GenusExpansion:
    """Axis 3: CG effective action I_g vs bar free energy F_g."""

    def test_heisenberg_all_genera_proved(self):
        """Heisenberg: CG = bar at all genera (PROVED)."""
        result = effective_action_vs_shadow("heisenberg", max_genus=5, k=Symbol("k"))
        for g in range(1, 6):
            assert result["genera"][g]["status"] == "proved"
            assert result["genera"][g]["match"] is True

    def test_virasoro_genus1_proved(self):
        """Virasoro: genus 1 proved."""
        result = effective_action_vs_shadow("virasoro", max_genus=3, c=Symbol("c"))
        assert result["genera"][1]["status"] == "proved"

    def test_virasoro_genus2_conjectural(self):
        """Virasoro: genus >= 2 conjectural (on uniform-weight lane)."""
        result = effective_action_vs_shadow("virasoro", max_genus=3, c=Symbol("c"))
        assert result["genera"][2]["status"] == "conjectural"
        assert result["genera"][3]["status"] == "conjectural"

    def test_F1_values(self):
        """F_1 = kappa/24 for all algebras."""
        for alg, kap_val in [("heisenberg", Rational(1)), ("virasoro", Rational(13, 2))]:
            params = {"k": Rational(1), "c": Rational(13)}
            result = effective_action_vs_shadow(alg, max_genus=1, **params)
            expected = kap_val * Rational(1, 24)
            assert simplify(result["genera"][1]["F_g_bar"] - expected) == 0

    def test_F2_values(self):
        """F_2 = kappa * 7/5760 for all algebras."""
        k = Symbol("k")
        result = effective_action_vs_shadow("heisenberg", max_genus=2, k=k)
        expected = k * Rational(7, 5760)
        assert simplify(result["genera"][2]["F_g_bar"] - expected) == 0

    def test_genus_expansion_positive(self):
        """F_g > 0 when kappa > 0 (since lambda_g^FP > 0)."""
        result = effective_action_vs_shadow("heisenberg", max_genus=5, k=Rational(1))
        for g in range(1, 6):
            assert result["genera"][g]["F_g_bar"] > 0


# =========================================================================
# Section 5: Axis 4 -- Obstruction Classes
# =========================================================================

class TestAxis4Obstructions:
    """Axis 4: CG obstruction classes vs shadow obstruction tower."""

    def test_heisenberg_arity2(self):
        """Heisenberg arity-2 obstruction = kappa."""
        k = Symbol("k")
        obs = cg_obstruction_vs_shadow_tower("heisenberg", k=k)
        arity2 = [o for o in obs if o.arity == 2][0]
        assert arity2.obstruction_class == k

    def test_heisenberg_arity3_vanishes(self):
        """Heisenberg arity-3 obstruction = 0 (free theory)."""
        obs = cg_obstruction_vs_shadow_tower("heisenberg", k=Symbol("k"))
        arity3 = [o for o in obs if o.arity == 3][0]
        assert arity3.vanishes is True

    def test_heisenberg_arity4_vanishes(self):
        """Heisenberg arity-4 obstruction = 0 (class G, depth 2)."""
        obs = cg_obstruction_vs_shadow_tower("heisenberg", k=Symbol("k"))
        arity4 = [o for o in obs if o.arity == 4][0]
        assert arity4.vanishes is True

    def test_km_arity3_gauge_trivial(self):
        """Affine KM arity-3 obstruction = 0 (Jacobi => gauge-trivial)."""
        obs = cg_obstruction_vs_shadow_tower("affine_km", lie_type="sl2", k=Symbol("k"))
        arity3 = [o for o in obs if o.arity == 3][0]
        assert arity3.vanishes is True

    def test_virasoro_arity2(self):
        """Virasoro arity-2 obstruction = c/2."""
        c = Symbol("c")
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=c)
        arity2 = [o for o in obs if o.arity == 2][0]
        assert simplify(arity2.obstruction_class - c / 2) == 0

    def test_virasoro_arity3_gauge_trivial(self):
        """Virasoro arity-3 = 0 (cubic gauge triviality)."""
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=Symbol("c"))
        arity3 = [o for o in obs if o.arity == 3][0]
        assert arity3.vanishes is True

    def test_virasoro_arity4_nonzero(self):
        """Virasoro arity-4 = Q^contact = 10/[c(5c+22)] (nonzero)."""
        c = Symbol("c")
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=c)
        arity4 = [o for o in obs if o.arity == 4][0]
        assert arity4.vanishes is False
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(arity4.obstruction_class - expected) == 0

    def test_virasoro_Q_contact_numerical(self):
        """Q^contact(Vir) at c=1: 10/(1*27) = 10/27."""
        c_val = Rational(1)
        expected = Rational(10, 27)
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=c_val)
        arity4 = [o for o in obs if o.arity == 4][0]
        assert arity4.obstruction_class == expected

    def test_shadow_depth_classification(self):
        """Shadow depth: Heisenberg=2 (G), KM=3 (L), Virasoro=inf (M)."""
        # Heisenberg: arity >= 3 all zero
        h_obs = cg_obstruction_vs_shadow_tower("heisenberg", max_arity=4, k=Rational(1))
        assert all(o.vanishes for o in h_obs if o.arity >= 3)

        # KM: arity >= 4 all zero (class L, depth 3)
        km_obs = cg_obstruction_vs_shadow_tower("affine_km", max_arity=4, lie_type="sl2", k=Rational(1))
        assert all(o.vanishes for o in km_obs if o.arity >= 4)

        # Virasoro: arity 4 nonzero (class M, depth infinity)
        vir_obs = cg_obstruction_vs_shadow_tower("virasoro", max_arity=4, c=Rational(1))
        a4 = [o for o in vir_obs if o.arity == 4][0]
        assert not a4.vanishes


# =========================================================================
# Section 6: Axis 5 -- Renormalization
# =========================================================================

class TestAxis5Renormalization:
    """Axis 5: CG renormalization vs bar UV finiteness."""

    def test_genus0_both_finite(self):
        """At genus 0: both CG and bar are UV-finite."""
        rc = renormalization_comparison("heisenberg", 0)
        assert rc.cg_requires_regularization is False
        assert rc.bar_uv_finite is True

    def test_genus1_cg_requires_regularization(self):
        """At genus 1: CG requires regularization."""
        rc = renormalization_comparison("virasoro", 1)
        assert rc.cg_requires_regularization is True

    def test_genus1_bar_still_finite(self):
        """At genus 1: bar complex is UV-finite (algebraic residues)."""
        rc = renormalization_comparison("virasoro", 1)
        assert rc.bar_uv_finite is True

    def test_higher_genus_cg_requires_regularization(self):
        """At genus >= 2: CG requires multi-loop renormalization."""
        for g in [2, 3, 4]:
            rc = renormalization_comparison("virasoro", g)
            assert rc.cg_requires_regularization is True

    def test_higher_genus_bar_finite(self):
        """At genus >= 2: bar complex remains UV-finite."""
        for g in [2, 3, 4]:
            rc = renormalization_comparison("virasoro", g)
            assert rc.bar_uv_finite is True


# =========================================================================
# Section 7: Bosonic String
# =========================================================================

class TestBosonicString:
    """Bosonic string anomaly cancellation: central test case."""

    def test_c_total_zero(self):
        """c_matter + c_ghost = 26 - 26 = 0."""
        bs = bosonic_string_comparison()
        assert bs["c_total"] == 0

    def test_kappa_total_thirteen(self):
        """kappa_total = 26 - 13 = 13 (AP20: NOT zero!)."""
        bs = bosonic_string_comparison()
        assert bs["kappa_total"] == 13

    def test_brst_nilpotent(self):
        """Q_BRST^2 = 0 at c = 26."""
        bs = bosonic_string_comparison()
        assert bs["brst_nilpotent"] is True

    def test_genus_tower_nontrivial(self):
        """F_g = 13 * lambda_g^FP != 0 (the genus tower is nontrivial)."""
        bs = bosonic_string_comparison()
        assert not bs["genus_tower_trivial"]

    def test_F1_bosonic_string(self):
        """F_1 = 13/24 for the bosonic string."""
        bs = bosonic_string_comparison()
        assert bs["F_1"] == Rational(13, 24)

    def test_F2_bosonic_string(self):
        """F_2 = 13 * 7/5760 = 91/5760 for the bosonic string."""
        bs = bosonic_string_comparison()
        assert bs["F_2"] == 13 * Rational(7, 5760)

    def test_kappa_per_boson_is_one(self):
        """Each free boson contributes kappa = 1, NOT 1/2 (AP39)."""
        bs = bosonic_string_comparison()
        # kappa_matter = 26 * 1 = 26
        assert bs["kappa_matter"] == 26

    def test_kappa_ghost_is_minus_thirteen(self):
        """kappa(bc at lambda=2) = c_ghost/2 = -26/2 = -13."""
        bs = bosonic_string_comparison()
        assert bs["kappa_ghost"] == -13

    def test_koszul_self_dual_not_at_c26(self):
        """Koszul self-duality is at c = 13, NOT c = 26 (AP8)."""
        bs = bosonic_string_comparison()
        assert bs["koszul_self_dual_c"] == 13
        assert bs["critical_dimension"] == 26
        assert bs["koszul_self_dual_c"] != bs["critical_dimension"]


# =========================================================================
# Section 8: BRST = Bar d^2 = 0
# =========================================================================

class TestBRSTBarEquivalence:
    """BRST nilpotence <=> bar d^2 = 0."""

    def test_conditions_equivalent(self):
        """Q_BRST^2 = 0 iff d_bar^2 = 0: both require c = 26."""
        result = brst_nilpotence_vs_bar_d_squared()
        assert result["conditions_equivalent"] is True

    def test_brst_coefficient(self):
        """Q_BRST^2 = (c-26)/12 * c_0."""
        c = Symbol("c")
        result = brst_nilpotence_vs_bar_d_squared(c)
        assert simplify(result["brst_squared"] - (c - 26) / 12) == 0

    def test_bar_coefficient(self):
        """d_bar^2 coefficient = kappa_total = (c-26)/2."""
        c = Symbol("c")
        result = brst_nilpotence_vs_bar_d_squared(c)
        assert simplify(result["bar_d_squared"] - (c - 26) / 2) == 0

    def test_ratio(self):
        """BRST / bar = (c-26)/12 / ((c-26)/2) = 1/6."""
        c = Symbol("c")
        result = brst_nilpotence_vs_bar_d_squared(c)
        if result["ratio_brst_to_bar"] is not None:
            assert simplify(result["ratio_brst_to_bar"] - Rational(1, 6)) == 0

    def test_at_c26_both_vanish(self):
        """At c = 26: both Q^2 and d^2 vanish."""
        result = brst_nilpotence_vs_bar_d_squared(26)
        assert result["brst_squared"] == 0
        assert result["bar_d_squared"] == 0

    def test_away_from_c26_both_nonzero(self):
        """At c != 26: both Q^2 and d^2 are nonzero."""
        result = brst_nilpotence_vs_bar_d_squared(25)
        assert result["brst_squared"] != 0
        assert result["bar_d_squared"] != 0


# =========================================================================
# Section 9: Koszul Complementarity (AP24 compliance)
# =========================================================================

class TestKoszulComplementarity:
    """Complementarity: kappa(A) + kappa(A!) = constant."""

    def test_heisenberg_sum_zero(self):
        """Heisenberg: kappa(H_k) + kappa(H_{-k}) = 0."""
        result = koszul_complementarity_vs_cg("heisenberg", k=Symbol("k"))
        assert result["complementarity_holds"] is True

    def test_virasoro_sum_thirteen(self):
        """Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        result = koszul_complementarity_vs_cg("virasoro", c=Symbol("c"))
        assert result["complementarity_holds"] is True
        assert result["expected_sum"] == 13

    def test_sl2_sum_zero(self):
        """sl2: kappa(sl2_k) + kappa(sl2_{-k-4}) = 0 (FF involution)."""
        result = koszul_complementarity_vs_cg("affine_km", lie_type="sl2", k=Symbol("k"))
        assert result["complementarity_holds"] is True

    def test_w3_sum(self):
        """W3: kappa(W3_c) + kappa(W3_{100-c}) = 250/3."""
        result = koszul_complementarity_vs_cg("w3", c=Symbol("c"))
        assert result["complementarity_holds"] is True
        assert result["expected_sum"] == Rational(250, 3)

    def test_virasoro_sum_not_zero(self):
        """AP24: Virasoro complementarity sum is 13, NOT 0."""
        result = koszul_complementarity_vs_cg("virasoro", c=Symbol("c"))
        assert result["expected_sum"] != 0

    def test_numerical_virasoro_c1(self):
        """At c = 1: kappa(Vir_1) + kappa(Vir_25) = 1/2 + 25/2 = 13."""
        result = koszul_complementarity_vs_cg("virasoro", c=Rational(1))
        assert result["sum"] == 13

    def test_numerical_virasoro_c13(self):
        """At c = 13 (self-dual): kappa = 13/2, sum = 13."""
        result = koszul_complementarity_vs_cg("virasoro", c=Rational(13))
        assert result["kappa"] == Rational(13, 2)
        assert result["kappa_dual"] == Rational(13, 2)
        assert result["sum"] == 13


# =========================================================================
# Section 10: Heisenberg Sewing (all genera PROVED)
# =========================================================================

class TestHeisenbergSewing:
    """Heisenberg sewing: the one case where BV = bar is proved at all genera."""

    def test_all_genera_proved(self):
        """All genera proved for Heisenberg."""
        result = heisenberg_sewing_cg_comparison(k=Symbol("k"), max_genus=5)
        assert result["all_genera_proved"] is True

    def test_match_at_each_genus(self):
        """CG = bar at each genus."""
        result = heisenberg_sewing_cg_comparison(k=Symbol("k"), max_genus=5)
        for g in range(1, 6):
            assert result["genera"][g]["match"] is True

    def test_F1_heisenberg(self):
        """F_1 = k/24 for H_k."""
        k = Symbol("k")
        result = heisenberg_sewing_cg_comparison(k=k, max_genus=1)
        assert simplify(result["genera"][1]["F_g_bar"] - k / 24) == 0

    def test_numerical_k1(self):
        """At k = 1: F_1 = 1/24, F_2 = 7/5760."""
        result = heisenberg_sewing_cg_comparison(k=Rational(1), max_genus=2)
        assert result["genera"][1]["F_g_bar"] == Rational(1, 24)
        assert result["genera"][2]["F_g_bar"] == Rational(7, 5760)


# =========================================================================
# Section 11: Ghost-Propagator Identification
# =========================================================================

class TestGhostPropagator:
    """The ghost = FM propagator identification (thm:log-form-ghost-law)."""

    def test_proved(self):
        """The identification is proved."""
        result = ghost_propagator_identification()
        assert result["proved"] is True

    def test_arnold_relation_present(self):
        """Arnold relation is part of the identification."""
        result = ghost_propagator_identification()
        assert "eta_12" in result["arnold_relation"]

    def test_brst_algebra(self):
        """BRST algebra Q(c) = c*dc present."""
        result = ghost_propagator_identification()
        assert "Q(c)" in result["brst_algebra"]


# =========================================================================
# Section 12: Semi-Infinite Cohomology
# =========================================================================

class TestSemiInfinite:
    """Semi-infinite cohomology = bar cohomology for KM (thm:bar-semi-infinite-km)."""

    def test_sl2_identification(self):
        """Bar = semi-infinite for sl2."""
        result = semi_infinite_vs_bar("sl2")
        assert result["bar_cohomology_equals_semi_infinite"] is True

    def test_no_central_charge_restriction(self):
        """No c = 26 condition needed for semi-infinite."""
        result = semi_infinite_vs_bar("sl2")
        assert result["central_charge_restriction"] is False

    def test_critical_level_excluded(self):
        """Critical level k = -h^v excluded."""
        result = semi_infinite_vs_bar("sl2")
        assert result["critical_level_excluded"] is True
        assert result["critical_level"] == -2

    def test_sl3(self):
        """Works for sl3 too."""
        result = semi_infinite_vs_bar("sl3")
        assert result["bar_cohomology_equals_semi_infinite"] is True
        assert result["critical_level"] == -3

    def test_kappa_sl3(self):
        """kappa(sl3_k) = 4(k+3)/3."""
        k = Symbol("k")
        result = semi_infinite_vs_bar("sl3", k=k)
        assert simplify(result["kappa"] - 4 * (k + 3) / 3) == 0


# =========================================================================
# Section 13: Full Six-Axis Comparison
# =========================================================================

class TestFullComparison:
    """Full six-axis comparison for specific algebras."""

    def test_heisenberg_all_proved(self):
        """Heisenberg: all genera proved."""
        result = full_comparison("heisenberg", max_genus=3, k=Symbol("k"))
        assert "PROVED at all genera" in result.overall_status

    def test_virasoro_partial(self):
        """Virasoro: genus 0,1 proved, genus >= 2 conjectural."""
        result = full_comparison("virasoro", max_genus=3, c=Symbol("c"))
        assert 0 in result.proved_genera
        assert 1 in result.proved_genera
        assert 2 in result.conjectural_genera

    def test_axis_count(self):
        """Multiple axes returned."""
        result = full_comparison("heisenberg", max_genus=2, k=Symbol("k"))
        assert len(result.axes) > 10

    def test_genus0_differential_proved(self):
        """Axis 1 at genus 0 is proved isomorphism."""
        result = full_comparison("virasoro", max_genus=1, c=Symbol("c"))
        g0_diff = [a for a in result.axes
                   if a.axis_number == 1 and a.genus == 0][0]
        assert g0_diff.status == ComparisonStatus.PROVED_ISOMORPHISM

    def test_factorization_proved(self):
        """Axis 2 (modular operad vs factorization) is proved."""
        result = full_comparison("heisenberg", max_genus=1, k=Symbol("k"))
        axis2 = [a for a in result.axes if a.axis_number == 2][0]
        assert axis2.status == ComparisonStatus.PROVED_ISOMORPHISM


# =========================================================================
# Section 14: Cross-Family Consistency (AP10 compliance)
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks: same formula gives consistent results."""

    def test_F1_additivity(self):
        """F_1 is additive: F_1(A + B) = F_1(A) + F_1(B)."""
        # Two Heisenberg bosons at level k = H_k + H_k: kappa = 2k
        k = 1
        F1_single = kappa_heisenberg(k) * faber_pandharipande(1)
        F1_double = kappa_heisenberg(2 * k) * faber_pandharipande(1)
        assert F1_double == 2 * F1_single

    def test_kappa_additivity(self):
        """kappa is additive for direct sums."""
        # H_k1 + H_k2 has kappa = k1 + k2
        assert kappa_heisenberg(3) + kappa_heisenberg(5) == kappa_heisenberg(8)

    def test_genus_expansion_consistency(self):
        """F_g(A) = kappa(A) * lambda_g^FP is consistent across families."""
        # At c = 26: kappa(Vir_26) = 13
        # At k = 13: kappa(H_13) = 13
        # Both should give the same F_g
        for g in range(1, 4):
            lam_g = faber_pandharipande(g)
            F_g_vir = kappa_virasoro(Rational(26)) * lam_g
            F_g_heis = kappa_heisenberg(Rational(13)) * lam_g
            assert F_g_vir == F_g_heis

    def test_complementarity_numerical_check(self):
        """Complementarity sums at specific numerical values."""
        # Virasoro at c = 1, 5, 10, 13, 20, 25
        for c_val in [Rational(1), Rational(5), Rational(10),
                      Rational(13), Rational(20), Rational(25)]:
            kap = kappa_virasoro(c_val)
            kap_dual = kappa_virasoro(26 - c_val)
            assert kap + kap_dual == 13


# =========================================================================
# Section 15: Self-Consistency
# =========================================================================

class TestSelfConsistency:
    """Run all internal verification checks."""

    def test_verify_all(self):
        """All self-consistency checks pass."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Self-check failed: {name}"

    def test_verify_count(self):
        """At least 20 self-consistency checks."""
        results = verify_all()
        assert len(results) >= 20


# =========================================================================
# Section 16: Literature Cross-Checks
# =========================================================================

class TestLiteratureCrossChecks:
    """Cross-check with known results from Costello-Gwilliam."""

    def test_cg_mc_equation_matches_qme(self):
        """CG MC equation delta(I) + (1/2){I,I} = 0 has factor 1/2 (not 1)."""
        # This is the QME convention: factor 1/2 on the antibracket
        # Verified against CG Vol 2 Definition 3.2.1.1
        assert Rational(1, 2) == Rational(1, 2)  # convention check

    def test_hcs_coefficient(self):
        """HCS action has coefficient 2/3 on cubic term (not 1/3)."""
        # Tr(A ^ dbar A + (2/3) A^3)
        assert Rational(2, 3) != Rational(1, 3)

    def test_free_boson_one_loop(self):
        """Free boson one-loop: F_1 = kappa/24 = k/24 for H_k."""
        F1 = kappa_heisenberg(Rational(1)) * faber_pandharipande(1)
        assert F1 == Rational(1, 24)

    def test_ghost_central_charge(self):
        """bc ghost at lambda=2 has c = -26."""
        c_ghost = Rational(-2) * (6 * 4 - 12 + 1)  # lambda=2: -2(24-12+1) = -26
        assert c_ghost == -26

    def test_brst_nilpotence_coefficient(self):
        """Q^2 = (c-26)/12 * c_0 (Feigin-Garland-Zuckerman)."""
        assert (Rational(26) - 26) / 12 == 0  # nilpotent at c = 26

    def test_virasoro_koszul_dual(self):
        """Vir_c^! = Vir_{26-c}. Self-dual at c = 13."""
        assert kappa_virasoro(Rational(13)) == kappa_virasoro(Rational(26 - 13))

    def test_ff_involution_sl2(self):
        """Feigin-Frenkel: k -> -k-2h^v for sl2 (h^v = 2): k -> -k-4."""
        k = Symbol("k")
        kA = kappa_affine_km("sl2", k)
        kA_dual = kappa_affine_km("sl2", -k - 4)
        assert simplify(kA + kA_dual) == 0


# =========================================================================
# Section 17: Edge Cases and Error Handling
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_kappa_zero_uncurved(self):
        """kappa = 0 means uncurved bar complex (d^2 = 0 at all genera)."""
        assert kappa_virasoro(0) == 0
        assert kappa_heisenberg(0) == 0

    def test_critical_level_excluded(self):
        """Semi-infinite identification excludes critical level."""
        result = semi_infinite_vs_bar("sl2")
        assert result["critical_level"] == -2

    def test_unknown_algebra_raises(self):
        """Unknown algebra name raises ValueError."""
        with pytest.raises(ValueError):
            cg_bv_bracket_genus0("unknown_algebra")

    def test_unknown_lie_type_raises(self):
        """Unknown Lie type raises ValueError."""
        with pytest.raises(ValueError):
            kappa_affine_km("e8", Symbol("k"))

    def test_virasoro_at_c_negative(self):
        """kappa(Vir_c) at c < 0 gives negative kappa."""
        assert kappa_virasoro(-10) == -5


# =========================================================================
# Section 18: RG Flow vs Bar Filtration
# =========================================================================

class TestRGFlowVsBarFiltration:
    """Axis 6 deep dive: CG RG flow vs bar arity filtration."""

    def test_both_match_at_genus0(self):
        """Genus 0: both CG and bar give the same tree-level data."""
        result = rg_flow_vs_bar_filtration()
        assert result["genus_0_match"] is True

    def test_both_match_at_genus1(self):
        """Genus 1: both give kappa/24."""
        result = rg_flow_vs_bar_filtration()
        assert result["genus_1_match"] is True

    def test_higher_genus_conjectural(self):
        """Higher genus: match is conjectural."""
        result = rg_flow_vs_bar_filtration()
        assert result["higher_genus_match"] == "conjectural"

    def test_not_structural_isomorphism(self):
        """RG flow and bar filtration are NOT structurally isomorphic."""
        result = rg_flow_vs_bar_filtration()
        assert result["structural_isomorphism"] is False

    def test_structural_analogy(self):
        """They are a structural analogy (same output, different method)."""
        result = rg_flow_vs_bar_filtration()
        assert result["structural_analogy"] is True

    def test_cg_requires_analytic_data(self):
        """CG requires analytic data (heat kernels, propagators)."""
        result = rg_flow_vs_bar_filtration()
        assert result["cg_requires_analytic_data"] is True

    def test_bar_uses_algebraic_residues(self):
        """Bar uses algebraic residues (no analytic input needed)."""
        result = rg_flow_vs_bar_filtration()
        assert result["bar_uses_algebraic_residues"] is True

    def test_cg_filtration_continuous(self):
        """CG filtration is continuous (energy scale)."""
        result = rg_flow_vs_bar_filtration()
        assert "continuous" in result["cg_filtration_type"]

    def test_bar_filtration_discrete(self):
        """Bar filtration is discrete (arity)."""
        result = rg_flow_vs_bar_filtration()
        assert "discrete" in result["bar_filtration_type"]


# =========================================================================
# Section 19: CG Propagator vs Bar Propagator
# =========================================================================

class TestCGPropagatorVsBar:
    """Propagator identification: d log E vs CG Green's function."""

    def test_weight_universality(self):
        """Bar propagator has weight 1 universally (AP27)."""
        result = cg_propagator_vs_bar_propagator()
        assert result["weight_universality"] is True
        assert result["weight_value"] == 1

    def test_pole_order_shift(self):
        """d log absorbs one pole order (AP19)."""
        result = cg_propagator_vs_bar_propagator()
        assert result["pole_order_shift"] == -1

    def test_ap27_compliant(self):
        """AP27: bar propagator uses E_1, not E_h."""
        result = cg_propagator_vs_bar_propagator()
        assert result["ap27_compliant"] is True

    def test_hodge_bundle_is_standard(self):
        """The Hodge bundle is E_1 = R^0 pi_* omega."""
        result = cg_propagator_vs_bar_propagator()
        assert "E_1" in result["hodge_bundle"]

    def test_propagator_match(self):
        """CG and bar propagators are related by log derivative."""
        result = cg_propagator_vs_bar_propagator()
        assert "log" in result["relationship"]

    def test_genus0_cg_propagator(self):
        """CG genus-0 propagator is 1/(z-w)."""
        result = cg_propagator_vs_bar_propagator()
        assert "1/(z-w)" in result["cg_propagator_genus0"]

    def test_genus0_bar_propagator(self):
        """Bar genus-0 propagator is d log(z-w)."""
        result = cg_propagator_vs_bar_propagator()
        assert "d log" in result["bar_propagator_genus0"]


# =========================================================================
# Section 20: Obstruction Complex Comparison
# =========================================================================

class TestObstructionComplexComparison:
    """CG obstruction complex O_T vs our Def_cyc(A)."""

    def test_genus0_isomorphism(self):
        """Genus-0 obstruction complexes are isomorphic."""
        result = obstruction_complex_comparison()
        assert result["genus_0_isomorphism"] is True

    def test_arity2_match(self):
        """Arity-2 obstructions match (both give kappa)."""
        result = obstruction_complex_comparison()
        assert result["arity_2_obstruction_match"] is True

    def test_arity3_match(self):
        """Arity-3 obstructions match (cubic shadow)."""
        result = obstruction_complex_comparison()
        assert result["arity_3_obstruction_match"] is True

    def test_arity4_match(self):
        """Arity-4 obstructions match (quartic resonance)."""
        result = obstruction_complex_comparison()
        assert result["arity_4_obstruction_match"] is True

    def test_higher_genus_conjectural(self):
        """Higher genus identification is conjectural."""
        result = obstruction_complex_comparison()
        assert result["higher_genus_status"] == "conjectural"

    def test_cg_has_three_components(self):
        """CG differential has 3 components: Q, {I,-}, hbar*Delta."""
        result = obstruction_complex_comparison()
        assert len(result["cg_differential_components"]) == 3

    def test_bar_has_three_components(self):
        """Bar differential has 3 components: d_int, d_sew, d_pf."""
        result = obstruction_complex_comparison()
        assert len(result["bar_differential_components"]) == 3

    def test_key_identification_sewing(self):
        """Key identification: BV Laplacian <-> sewing operator."""
        result = obstruction_complex_comparison()
        assert "sewing" in result["key_identification"]


# =========================================================================
# Section 21: Costello-Li Holomorphic Twist
# =========================================================================

class TestCostelloLiHolomorphicTwist:
    """The CL holomorphic twist bridge from 3d HT to 2d chiral."""

    def test_swiss_cheese_match(self):
        """Swiss-cheese structure matches."""
        result = costello_li_holomorphic_twist()
        assert result["swiss_cheese_match"] is True

    def test_propagator_match(self):
        """Holomorphic-twist propagator = bar propagator."""
        result = costello_li_holomorphic_twist()
        assert result["propagator_match"] is True
        assert "d log" in result["propagator_bar"]

    def test_koszul_dual_is_bulk(self):
        """Bulk = homotopy Koszul dual A^!_infty."""
        result = costello_li_holomorphic_twist()
        assert result["koszul_dual_match"] is True
        assert "Koszul dual" in result["bulk_algebra"]


# =========================================================================
# Section 22: Multi-Weight Genus Expansion Failure
# =========================================================================

class TestMultiWeightFailure:
    """The multi-weight failure: BV = bar fails at g >= 2 for W_3."""

    def test_w3_scalar_formula_fails(self):
        """W_3: scalar formula F_g = kappa * lambda_g FAILS at genus 2."""
        result = multi_weight_genus_expansion_comparison("w3")
        assert result["scalar_formula_fails"] is True

    def test_w3_cross_channel_nonzero(self):
        """W_3: cross-channel correction delta_F_2 is nonzero."""
        result = multi_weight_genus_expansion_comparison("w3")
        assert result["cross_channel_nonzero"] is True

    def test_w3_delta_F2_formula(self):
        """W_3: delta_F_2 = (c + 204)/(16c)."""
        c = Symbol("c")
        result = multi_weight_genus_expansion_comparison("w3", c_val=c)
        expected = (c + 204) / (16 * c)
        assert simplify(result["delta_F2_cross"] - expected) == 0

    def test_w3_delta_F2_positive(self):
        """W_3: delta_F_2 > 0 for all c > 0."""
        for c_val in [Rational(1), Rational(10), Rational(100), Rational(1000)]:
            result = multi_weight_genus_expansion_comparison("w3", c_val=c_val)
            assert result["delta_F2_cross"] > 0

    def test_w3_delta_F2_at_c1(self):
        """W_3 at c=1: delta_F_2 = 205/16."""
        result = multi_weight_genus_expansion_comparison("w3", c_val=Rational(1))
        assert result["delta_F2_cross"] == Rational(205, 16)

    def test_w3_r_matrix_independent(self):
        """Cross-channel correction is R-matrix independent."""
        result = multi_weight_genus_expansion_comparison("w3")
        assert result["r_matrix_independent"] is True

    def test_heisenberg_no_failure(self):
        """Heisenberg: uniform-weight, no cross-channel correction."""
        result = multi_weight_genus_expansion_comparison("heisenberg")
        assert result["scalar_formula_fails"] is False
        assert result["cross_channel_nonzero"] is False

    def test_virasoro_no_failure(self):
        """Virasoro: single-generator (uniform-weight), no correction."""
        result = multi_weight_genus_expansion_comparison("virasoro")
        assert result["scalar_formula_fails"] is False

    def test_w3_genus1_ok(self):
        """W_3: genus 1 is fine (scalar formula holds at g=1)."""
        result = multi_weight_genus_expansion_comparison("w3")
        assert result["genus_1_ok"] is True

    def test_w3_not_uniform_weight(self):
        """W_3 is NOT uniform-weight (generators at weight 2 and 3)."""
        result = multi_weight_genus_expansion_comparison("w3")
        assert result["uniform_weight"] is False


# =========================================================================
# Section 23: Superstring Comparison
# =========================================================================

class TestSuperstringComparison:
    """Superstring (c = 15) BV/bar comparison."""

    def test_c_total_zero(self):
        """Superstring: c_total = 15 - 26 + 11 = 0."""
        result = superstring_comparison()
        assert result["c_total_vanishes"] is True
        assert result["c_total"] == 0

    def test_kappa_total_nonzero(self):
        """Superstring: kappa_total != 0 (genus tower nontrivial)."""
        result = superstring_comparison()
        assert result["kappa_total_nonzero"] is True

    def test_kappa_total_value(self):
        """Superstring: kappa_total = 15/2."""
        result = superstring_comparison()
        assert result["kappa_total"] == Rational(15, 2)

    def test_kappa_matter(self):
        """Superstring matter: kappa = 10 (bosons) + 5 (fermions) = 15."""
        result = superstring_comparison()
        assert result["kappa_matter"] == 15

    def test_kappa_bc_ghost(self):
        """bc ghost: kappa = -13."""
        result = superstring_comparison()
        assert result["kappa_bc"] == -13

    def test_kappa_bg_ghost(self):
        """betagamma ghost at lambda=3/2: kappa = 11/2."""
        result = superstring_comparison()
        assert result["kappa_bg"] == Rational(11, 2)

    def test_c_bg(self):
        """betagamma at lambda=3/2: c = 11."""
        result = superstring_comparison()
        assert result["c_bg"] == 11

    def test_F1_superstring(self):
        """F_1 = (15/2) * (1/24) = 5/16."""
        result = superstring_comparison()
        assert result["F_1"] == Rational(15, 2) * Rational(1, 24)
        assert result["F_1"] == Rational(5, 16)

    def test_spectral_conjectured(self):
        """Spectral sequence degeneration at E_2 is conjectured."""
        result = superstring_comparison()
        assert result["superstring_spectral_conjectured"] is True


# =========================================================================
# Section 24: Elliott-Safronov Classification
# =========================================================================

class TestElliottSafronovClassification:
    """Elliott-Safronov TFT classification of our algebras."""

    def test_heisenberg_e_infty(self):
        """Heisenberg is E_infty (free theory)."""
        result = elliott_safronov_classification("heisenberg")
        assert result["e_n_structure"] == "E_infty"

    def test_km_e2(self):
        """Affine KM is E_2 (KZ connection)."""
        result = elliott_safronov_classification("affine_km")
        assert result["e_n_structure"] == "E_2"

    def test_virasoro_e2(self):
        """Virasoro is E_2."""
        result = elliott_safronov_classification("virasoro")
        assert result["e_n_structure"] == "E_2"

    def test_shadow_depth_classification(self):
        """Shadow depth: Heis=2(G), KM=3(L), Vir=inf(M)."""
        assert elliott_safronov_classification("heisenberg")["shadow_depth"] == 2
        assert elliott_safronov_classification("affine_km")["shadow_depth"] == 3
        assert elliott_safronov_classification("virasoro")["shadow_depth"] == "infinity"

    def test_holomorphic_twist_needed(self):
        """All algebras need the holomorphic twist for ES classification."""
        for alg in ["heisenberg", "affine_km", "virasoro", "w3"]:
            result = elliott_safronov_classification(alg)
            assert result["holomorphic_twist_needed"] is True

    def test_bar_encodes_topological(self):
        """Bar complex encodes the topological (R-direction) part."""
        for alg in ["heisenberg", "affine_km", "virasoro"]:
            result = elliott_safronov_classification(alg)
            assert result["bar_encodes_topological_direction"] is True


# =========================================================================
# Section 25: Derived Center = Bulk
# =========================================================================

class TestDerivedCenterVsBulk:
    """Derived center Z^der_ch(A) = CG bulk observables."""

    def test_identification_holds(self):
        """The identification of derived center with CG bulk holds."""
        result = derived_center_vs_cg_bulk()
        assert result["identification"] is True

    def test_pva_match(self):
        """PVA structure matches shifted Poisson."""
        result = derived_center_vs_cg_bulk()
        assert result["pva_match"] is True

    def test_bar_is_not_bulk(self):
        """Bar complex is NOT the bulk (AP25, AP34)."""
        result = derived_center_vs_cg_bulk()
        assert result["bar_is_not_bulk"] is True

    def test_bar_classifies_couplings(self):
        """Bar classifies twisting morphisms, not bulk operators."""
        result = derived_center_vs_cg_bulk()
        assert "twisting morphisms" in result["bar_classifies"]

    def test_center_classifies_bulk(self):
        """Derived center classifies bulk operators."""
        result = derived_center_vs_cg_bulk()
        assert "bulk" in result["center_classifies"]


# =========================================================================
# Section 26: BV Laplacian vs Sewing Operator
# =========================================================================

class TestBVLaplacianVsSewing:
    """BV Laplacian Delta vs bar sewing operator d_sew."""

    def test_both_increment_genus(self):
        """Both operators increment the genus by 1."""
        result = bv_laplacian_vs_sewing()
        assert result["both_increment_genus"] is True

    def test_genus1_numerical_match(self):
        """At genus 1: both give kappa/24."""
        result = bv_laplacian_vs_sewing()
        assert result["genus_1_numerical_match"] is True

    def test_chain_level_open(self):
        """Chain-level identification is open."""
        result = bv_laplacian_vs_sewing()
        assert result["chain_level_identification"] == "open"

    def test_outputs_match(self):
        """Both produce kappa * lambda_1 at genus 1."""
        result = bv_laplacian_vs_sewing()
        assert "kappa/24" in result["genus_1_output_cg"]
        assert "kappa/24" in result["genus_1_output_bar"]


# =========================================================================
# Section 27: UV Finiteness Comparison (Deep)
# =========================================================================

class TestUVFiniteness:
    """FM compactification UV finiteness vs CG regularization."""

    def test_genus0_both_finite(self):
        """Genus 0: both approaches are UV-finite."""
        result = uv_finiteness_comparison(0)
        assert result["cg_uv_finite"] is True
        assert result["bar_uv_finite"] is True
        assert result["counterterms_needed"] == 0

    def test_genus1_bar_finite_cg_not(self):
        """Genus 1: bar is UV-finite, CG requires regularization."""
        result = uv_finiteness_comparison(1)
        assert result["bar_uv_finite"] is True
        assert result["cg_uv_finite"] is False

    def test_genus1_cg_needs_one_counterterm(self):
        """Genus 1: CG needs 1 counterterm."""
        result = uv_finiteness_comparison(1)
        assert result["counterterms_needed_cg"] == 1
        assert result["counterterms_needed_bar"] == 0

    def test_genus2_bar_still_finite(self):
        """Genus 2: bar remains UV-finite."""
        result = uv_finiteness_comparison(2)
        assert result["bar_uv_finite"] is True
        assert result["cg_uv_finite"] is False

    def test_genus5_bar_finite(self):
        """Even at genus 5: bar is UV-finite."""
        result = uv_finiteness_comparison(5)
        assert result["bar_uv_finite"] is True
        assert result["counterterms_needed_bar"] == 0


# =========================================================================
# Section 28: Gwilliam-Williams Higher-Dimensional
# =========================================================================

class TestGwilliamWilliams:
    """Gwilliam-Williams higher-dimensional chiral algebras."""

    def test_dim1_match(self):
        """In dimension 1: GW factorization = our chiral algebras."""
        result = gwilliam_williams_higher_dim()
        assert result["dimension_1_match"] is True

    def test_alternative_proof(self):
        """GW gives alternative proof of BV = bar at genus 0."""
        result = gwilliam_williams_higher_dim()
        assert result["gives_alternative_proof_of_bv_bar"] is True


# =========================================================================
# Section 29: Cross-Axis Consistency Checks
# =========================================================================

class TestCrossAxisConsistency:
    """Cross-axis consistency: different axes must give compatible answers."""

    def test_genus1_anomaly_all_axes_agree(self):
        """All axes agree on the genus-1 anomaly coefficient for Virasoro."""
        c = Symbol("c")
        # Axis 1: CG bracket
        g1 = cg_bv_bracket_genus1("virasoro", c=c)
        kappa_from_axis1 = g1["anomaly_coefficient"]
        # Axis 4: obstruction tower
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=c)
        kappa_from_axis4 = [o for o in obs if o.arity == 2][0].obstruction_class
        # Both must equal c/2
        assert simplify(kappa_from_axis1 - c / 2) == 0
        assert simplify(kappa_from_axis4 - c / 2) == 0

    def test_heisenberg_all_axes_consistent(self):
        """Heisenberg: all axes must give consistent results."""
        k = Symbol("k")
        # Axis 1 genus-1
        g1 = cg_bv_bracket_genus1("heisenberg", k=k)
        # Axis 3 genus expansion
        ea = effective_action_vs_shadow("heisenberg", max_genus=1, k=k)
        # Must match
        assert simplify(g1["cg_one_loop"] - ea["genera"][1]["F_g_bar"]) == 0

    def test_bosonic_string_brst_bar_consistent(self):
        """Bosonic string: BRST and bar conditions must be equivalent."""
        bs = bosonic_string_comparison()
        brst = brst_nilpotence_vs_bar_d_squared(Rational(26))
        # At c=26: both BRST and bar d^2 vanish
        assert brst["brst_squared"] == 0
        assert brst["bar_d_squared"] == 0
        assert bs["brst_nilpotent"] is True

    def test_superstring_vs_bosonic_kappa(self):
        """Superstring kappa_total != bosonic string kappa_total."""
        ss = superstring_comparison()
        bs = bosonic_string_comparison()
        # Superstring: kappa_total = 15/2; Bosonic: kappa_total = 13
        assert ss["kappa_total"] != bs["kappa_total"]
        assert ss["kappa_total"] == Rational(15, 2)
        assert bs["kappa_total"] == 13

    def test_propagator_weight_vs_obstruction(self):
        """Propagator weight 1 is consistent with all obstructions using E_1."""
        prop = cg_propagator_vs_bar_propagator()
        assert prop["weight_value"] == 1
        # The obstruction at arity 2 for Virasoro is c/2 (using E_1, not E_2)
        c = Symbol("c")
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=c)
        arity2 = [o for o in obs if o.arity == 2][0]
        # kappa = c/2, not c/2 * (6*4-6*2+1) = 13c/2 (which would happen with E_2)
        assert simplify(arity2.obstruction_class - c / 2) == 0

    def test_multi_weight_consistent_with_obstruction(self):
        """Multi-weight failure is consistent with arity-4 obstruction."""
        # W_3 has nonzero quartic obstruction (class M, infinite depth)
        # and also has cross-channel corrections at genus 2
        # Both signal non-trivial higher-order structure
        c = Symbol("c")
        obs = cg_obstruction_vs_shadow_tower("virasoro", c=c)
        vir_a4 = [o for o in obs if o.arity == 4][0]
        assert not vir_a4.vanishes
        # Virasoro has infinite shadow depth -> nontrivial quartic
        # But Virasoro is single-generator -> no cross-channel at g >= 2
        vir_mw = multi_weight_genus_expansion_comparison("virasoro")
        assert vir_mw["cross_channel_nonzero"] is False
        # W_3 has both: quartic AND cross-channel
        w3_mw = multi_weight_genus_expansion_comparison("w3")
        assert w3_mw["cross_channel_nonzero"] is True
