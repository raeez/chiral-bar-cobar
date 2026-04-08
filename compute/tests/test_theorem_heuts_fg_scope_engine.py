r"""Tests for Heuts-FG scope analysis: nilcompleteness, conilcompleteness,
and bar-cobar equivalence scope for chiral algebras.

THEOREM (Heuts, arXiv:2408.06173):
Koszul duality gives an equivalence between nilcomplete O-algebras and
conilcomplete BO-coalgebras, for any operad O.  This is the LARGEST
scope for which bar-cobar is an equivalence, disproving the Francis-
Gaitsgory prediction that the equivalence holds in full generality.

THEOREM (Booth-Lazarev, arXiv:2304.08409):
The curved bar-cobar adjunction is a Quillen equivalence between
curved coalgebras and curved algebras.

MONOGRAPH VERDICT: SAFE.  Three independent reasons (R1-R3).

VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):

    Path 1 (Pro-nilpotence): Chiral tensor on Ran(X) is pro-nilpotent
        => all chiral algebras nilcomplete automatically.
    Path 2 (Weight grading): Conformal weight + finite-dim => conilpotent.
    Path 3 (Koszul locus): PBW spectral sequence collapse => qi without
        needing nilcompleteness at all.

Cross-checks:
    (a) All standard families conilpotent (structural + explicit)
    (b) All standard families nilcomplete (3 independent paths)
    (c) Bar-cobar qi on Koszul locus verified family by family
    (d) Off-Koszul failure modes identified (minimal models)
    (e) Heuts scope boundary correctly identifies chiral as safe
    (f) Cross-family consistency (additivity, duality, DS)

All formulas computed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
Multi-path verification per CLAUDE.md mandate.

References:
    thm:quillen-equivalence-chiral (bar_cobar_adjunction_curved.tex)
    thm:conilpotency-convergence (bar_cobar_adjunction_curved.tex)
    thm:bar-cobar-inversion-qi (bar_cobar_adjunction_inversion.tex)
    thm:abstract-bar-cobar (dual_methodology.tex)
    Heuts, arXiv:2408.06173 (Koszul duality and FG conjecture)
    Booth-Lazarev, arXiv:2304.08409 (Global Koszul duality)
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_heuts_fg_scope_engine import (
    # Family constructors
    ChiralFamilyData,
    heisenberg_family,
    kac_moody_family,
    sl2_km,
    virasoro_family,
    w3_family,
    beta_gamma_family,
    w_infinity_family,
    minimal_model_family,
    STANDARD_FAMILIES,
    ALL_FAMILIES,
    # Conilpotency
    verify_conilpotency_weight_grading,
    verify_conilpotency_explicit,
    # Nilcompleteness
    verify_nilcompleteness,
    # Bar-cobar scope
    verify_bar_cobar_qi_scope,
    # Heuts scope boundary
    analyze_heuts_scope_boundary,
    # Booth-Lazarev
    analyze_booth_lazarev_upgrade,
    # Bar complex dimensions
    bar_complex_dimensions,
    # Koszul locus
    koszul_locus_diagnostic,
    # Cross-family
    cross_family_consistency_check,
    # Chiral pro-nilpotence
    verify_chiral_pronilpotence,
    # Quillen scope
    quillen_equivalence_scope,
    # Master
    verify_heuts_fg_scope_all,
)


# ============================================================================
# I. CONILPOTENCY: STRUCTURAL ARGUMENT (PATH 1)
# ============================================================================

class TestConilpotencyStructural:
    """Test conilpotency via weight-grading argument for all families."""

    def test_heisenberg_conilpotent(self):
        """Heisenberg: weight 1 generator, h_min = 1, manifestly conilpotent."""
        result = verify_conilpotency_weight_grading(heisenberg_family())
        assert result['conilpotent'] is True
        assert result['h_min'] == 1

    def test_sl2_km_conilpotent(self):
        """sl_2 KM: weight 1 generators, conilpotent."""
        result = verify_conilpotency_weight_grading(sl2_km())
        assert result['conilpotent'] is True
        assert result['h_min'] == 1

    def test_virasoro_conilpotent(self):
        """Virasoro: weight 2 generator, conilpotent."""
        result = verify_conilpotency_weight_grading(virasoro_family())
        assert result['conilpotent'] is True
        assert result['h_min'] == 2

    def test_w3_conilpotent(self):
        """W_3: generators at weights 2, 3; h_min = 2, conilpotent."""
        result = verify_conilpotency_weight_grading(w3_family())
        assert result['conilpotent'] is True
        assert result['h_min'] == 2

    def test_beta_gamma_conilpotent(self):
        """beta-gamma: gamma has weight 0, but still conilpotent
        (finite-dim weight spaces suffice)."""
        result = verify_conilpotency_weight_grading(beta_gamma_family())
        assert result['conilpotent'] is True
        assert result['h_min'] == 0

    def test_w_infinity_conilpotent(self):
        """W_{1+inf}: infinitely many generators but finite-dim weight spaces."""
        result = verify_conilpotency_weight_grading(w_infinity_family())
        assert result['conilpotent'] is True

    def test_minimal_model_conilpotent(self):
        """Minimal model: not Koszul but still conilpotent (weight grading)."""
        result = verify_conilpotency_weight_grading(minimal_model_family())
        assert result['conilpotent'] is True

    def test_all_standard_families_conilpotent(self):
        """Every standard family has conilpotent bar coalgebra."""
        for family in STANDARD_FAMILIES:
            result = verify_conilpotency_weight_grading(family)
            assert result['conilpotent'] is True, f"Failed for {family.name}"


# ============================================================================
# II. CONILPOTENCY: EXPLICIT BAR-DEGREE COMPUTATION (PATH 2)
# ============================================================================

class TestConilpotencyExplicit:
    """Test conilpotency by explicit bar complex dimension computation."""

    def test_heisenberg_bar_degrees(self):
        """Heisenberg: at weight w, max bar degree = w (h_min=1)."""
        result = verify_conilpotency_explicit(heisenberg_family())
        assert result['conilpotent'] is True
        # weight 1: bar deg 1 only; weight 2: bar deg 1,2; etc.
        for w, max_n in result['max_bar_deg_by_weight'].items():
            assert max_n <= w + 1, f"weight {w}: max bar deg {max_n} > {w+1}"

    def test_virasoro_bar_degrees(self):
        """Virasoro: at weight w, max bar degree = w//2 (h_min=2)."""
        result = verify_conilpotency_explicit(virasoro_family())
        assert result['conilpotent'] is True
        for w, max_n in result['max_bar_deg_by_weight'].items():
            if w > 0:
                assert max_n <= w // 2 + 1, f"weight {w}: bar deg {max_n}"

    def test_sl2_bar_degrees(self):
        """sl_2 KM: 3 generators at weight 1."""
        result = verify_conilpotency_explicit(sl2_km())
        assert result['conilpotent'] is True

    def test_w3_bar_degrees(self):
        """W_3: generators at weights 2,3; max bar degree at weight w is w//2."""
        result = verify_conilpotency_explicit(w3_family())
        assert result['conilpotent'] is True

    def test_beta_gamma_bar_degrees(self):
        """beta-gamma: weight 0 generator makes bar degree potentially large."""
        result = verify_conilpotency_explicit(beta_gamma_family(), max_weight=4)
        assert result['conilpotent'] is True

    def test_all_families_explicit(self):
        """All families pass explicit bar-degree conilpotency check."""
        for family in STANDARD_FAMILIES:
            result = verify_conilpotency_explicit(family, max_weight=4)
            assert result['conilpotent'] is True, f"Failed for {family.name}"


# ============================================================================
# III. NILCOMPLETENESS (PATH 1: GEOMETRIC PRO-NILPOTENCE)
# ============================================================================

class TestNilcompleteness:
    """Test nilcompleteness of chiral algebras."""

    def test_heisenberg_nilcomplete(self):
        """Heisenberg: nilcomplete via all three paths."""
        result = verify_nilcompleteness(heisenberg_family())
        assert result['nilcomplete'] is True
        assert result['path1_geometric_pronilpotence'] is True
        assert result['path2_weight_grading'] is True
        assert result['path3_koszul_pbw'] is True
        assert result['num_independent_paths'] == 3

    def test_virasoro_nilcomplete(self):
        """Virasoro: nilcomplete (geometric + weight + Koszul)."""
        result = verify_nilcompleteness(virasoro_family())
        assert result['nilcomplete'] is True
        assert result['num_independent_paths'] == 3

    def test_w3_nilcomplete(self):
        """W_3: nilcomplete."""
        result = verify_nilcompleteness(w3_family())
        assert result['nilcomplete'] is True

    def test_beta_gamma_nilcomplete_geometric(self):
        """beta-gamma: path 1 (geometric) always works; path 2 fails (h_min=0)."""
        result = verify_nilcompleteness(beta_gamma_family())
        assert result['nilcomplete'] is True
        assert result['path1_geometric_pronilpotence'] is True
        assert result['path2_weight_grading'] is False  # h_min = 0

    def test_minimal_model_nilcomplete(self):
        """Minimal model: nilcomplete (geometric) but NOT Koszul."""
        result = verify_nilcompleteness(minimal_model_family())
        assert result['nilcomplete'] is True
        assert result['path1_geometric_pronilpotence'] is True
        assert result['path3_koszul_pbw'] is False

    def test_all_families_nilcomplete(self):
        """ALL chiral algebra families are nilcomplete
        (by pro-nilpotence of chiral tensor on Ran(X))."""
        for family in ALL_FAMILIES:
            result = verify_nilcompleteness(family)
            assert result['nilcomplete'] is True, f"Failed for {family.name}"

    def test_geometric_pronilpotence_universal(self):
        """Geometric pro-nilpotence is universal: it does not depend
        on the specific family, only on the chiral tensor structure."""
        for family in ALL_FAMILIES:
            result = verify_nilcompleteness(family)
            assert result['path1_geometric_pronilpotence'] is True


# ============================================================================
# IV. BAR-COBAR QUASI-ISOMORPHISM SCOPE
# ============================================================================

class TestBarCobarScope:
    """Test the scope of bar-cobar inversion as quasi-isomorphism."""

    def test_heisenberg_qi(self):
        """Heisenberg: qi at all genera (quadratic, conilpotent, Koszul)."""
        result = verify_bar_cobar_qi_scope(heisenberg_family())
        assert result['bar_cobar_qi_genus_0'] is True
        assert result['bar_cobar_qi_all_genera'] is True
        assert result['within_heuts_scope'] is True

    def test_sl2_qi(self):
        """sl_2 KM: qi at all genera."""
        result = verify_bar_cobar_qi_scope(sl2_km())
        assert result['bar_cobar_qi_all_genera'] is True

    def test_virasoro_qi(self):
        """Virasoro: qi at all genera (needs completion but has it)."""
        result = verify_bar_cobar_qi_scope(virasoro_family())
        assert result['bar_cobar_qi_all_genera'] is True
        assert result['needs_completion'] is True

    def test_w3_qi(self):
        """W_3: qi at all genera."""
        result = verify_bar_cobar_qi_scope(w3_family())
        assert result['bar_cobar_qi_all_genera'] is True

    def test_minimal_model_NOT_qi(self):
        """Minimal model: NOT Koszul, bar-cobar NOT a qi."""
        result = verify_bar_cobar_qi_scope(minimal_model_family())
        assert result['bar_cobar_qi_genus_0'] is False
        assert result['bar_cobar_qi_all_genera'] is False
        assert result['koszul'] is False
        # But still within Heuts' scope (nilcomplete)!
        assert result['within_heuts_scope'] is True

    def test_all_standard_qi(self):
        """All standard (Koszul) families: bar-cobar qi at all genera."""
        for family in STANDARD_FAMILIES:
            result = verify_bar_cobar_qi_scope(family)
            assert result['bar_cobar_qi_all_genera'] is True, (
                f"Failed for {family.name}"
            )

    def test_heuts_scope_universal(self):
        """ALL families (including non-Koszul) are within Heuts' scope."""
        for family in ALL_FAMILIES:
            result = verify_bar_cobar_qi_scope(family)
            assert result['within_heuts_scope'] is True, (
                f"Failed for {family.name}"
            )


# ============================================================================
# V. HEUTS SCOPE BOUNDARY ANALYSIS
# ============================================================================

class TestHeutsScopeBoundary:
    """Test the scope boundary of Heuts' theorem across different settings."""

    def test_chiral_setting_safe(self):
        """Case 1: chiral on Ran(X) is pro-nilpotent, FG prediction TRUE."""
        result = analyze_heuts_scope_boundary()
        case1 = result['case_1_chiral']
        assert case1['pro_nilpotent'] is True
        assert case1['heuts_automatic'] is True
        assert case1['monograph_safe'] is True

    def test_chain_complexes_not_pronilpotent(self):
        """Case 2: chain complexes are NOT pro-nilpotent, FG prediction FALSE."""
        result = analyze_heuts_scope_boundary()
        case2 = result['case_2_chain']
        assert case2['pro_nilpotent'] is False
        assert case2['heuts_automatic'] is False

    def test_spectra_not_pronilpotent(self):
        """Case 3: spectra are NOT pro-nilpotent, FG prediction FALSE."""
        result = analyze_heuts_scope_boundary()
        case3 = result['case_3_spectra']
        assert case3['pro_nilpotent'] is False
        assert case3['heuts_automatic'] is False

    def test_heuts_disproof_does_not_affect_monograph(self):
        """The Heuts disproof is in Cases 2-3; Case 1 (our setting) is safe."""
        result = analyze_heuts_scope_boundary()
        assert result['case_1_chiral']['monograph_safe'] is True
        assert 'No adjustment' in result['conclusion']


# ============================================================================
# VI. CHIRAL PRO-NILPOTENCE OF RAN(X)
# ============================================================================

class TestChiralPronilpotence:
    """Test the pro-nilpotence of the chiral tensor structure on Ran(X)."""

    def test_pronilpotent(self):
        """Chiral tensor on DMod(Ran(X)) is pro-nilpotent."""
        result = verify_chiral_pronilpotence()
        assert result['pro_nilpotent'] is True

    def test_three_paths(self):
        """Pro-nilpotence verified by three independent paths."""
        result = verify_chiral_pronilpotence()
        assert result['path1_stratification'] is True
        assert result['path2_configuration'] is True
        assert result['path3_vanishing'] is True

    def test_implication_for_heuts(self):
        """Pro-nilpotence implies Heuts' equivalence holds for ALL chiral algebras."""
        result = verify_chiral_pronilpotence()
        assert 'all chiral algebras' in result['implication_for_heuts']


# ============================================================================
# VII. KOSZUL LOCUS DIAGNOSTICS
# ============================================================================

class TestKoszulLocus:
    """Test Koszul locus membership for all families."""

    def test_heisenberg_on_koszul(self):
        """Heisenberg: on Koszul locus (quadratic)."""
        result = koszul_locus_diagnostic(heisenberg_family())
        assert result['on_koszul_locus'] is True
        assert result['is_quadratic'] is True
        assert result['bar_cobar_qi'] is True

    def test_sl2_on_koszul(self):
        """sl_2 KM: on Koszul locus (quadratic)."""
        result = koszul_locus_diagnostic(sl2_km())
        assert result['on_koszul_locus'] is True

    def test_virasoro_on_koszul(self):
        """Virasoro: on Koszul locus (non-quadratic but Koszul via Feigin-Frenkel)."""
        result = koszul_locus_diagnostic(virasoro_family())
        assert result['on_koszul_locus'] is True
        assert result['is_quadratic'] is False

    def test_minimal_model_off_koszul(self):
        """Minimal model: OFF the Koszul locus (simple quotient)."""
        result = koszul_locus_diagnostic(minimal_model_family())
        assert result['on_koszul_locus'] is False
        assert result['bar_cobar_qi'] is False
        assert result['heuts_relevant'] is True

    def test_heuts_irrelevant_on_koszul(self):
        """On the Koszul locus, Heuts' theorem is redundant."""
        for family in STANDARD_FAMILIES:
            result = koszul_locus_diagnostic(family)
            assert result['on_koszul_locus'] is True
            assert result['heuts_relevant'] is False


# ============================================================================
# VIII. BOOTH-LAZAREV CURVED UPGRADE
# ============================================================================

class TestBoothLazarevUpgrade:
    """Test the Booth-Lazarev curved Quillen equivalence analysis."""

    def test_genus_0_no_upgrade_needed(self):
        """At genus 0, no curvature: BL not needed (Vallette suffices)."""
        result = analyze_booth_lazarev_upgrade(heisenberg_family())
        assert result['genus_0']['curved'] is False

    def test_genus_ge_1_curved(self):
        """At genus >= 1, curvature is nonzero: BL applies."""
        result = analyze_booth_lazarev_upgrade(virasoro_family())
        assert result['genus_ge_1']['curved'] is True

    def test_unification_possible(self):
        """BL could unify genus 0 and genus >= 1 frameworks."""
        result = analyze_booth_lazarev_upgrade(virasoro_family())
        assert result['unification_possible'] is True

    def test_heisenberg_curvature(self):
        """Heisenberg curvature at genus >= 1 is kappa * omega_g = k * omega_g."""
        h = heisenberg_family(k=Fraction(2))
        result = analyze_booth_lazarev_upgrade(h)
        assert '2 * omega_g' in result['genus_ge_1']['curvature']

    def test_virasoro_curvature(self):
        """Virasoro curvature at genus >= 1 is c/2 * omega_g."""
        v = virasoro_family(c=Fraction(26))
        result = analyze_booth_lazarev_upgrade(v)
        assert '13 * omega_g' in result['genus_ge_1']['curvature']


# ============================================================================
# IX. BAR COMPLEX DIMENSION TABLES
# ============================================================================

class TestBarComplexDimensions:
    """Test explicit bar complex dimension computations."""

    def test_heisenberg_bar_dims(self):
        """Heisenberg: bar degree n at weight w has known dimensions."""
        result = bar_complex_dimensions(heisenberg_family(), max_weight=5, max_bar_deg=5)
        dims = result['dims']
        # Bar degree 1, weight 1: one generator alpha
        assert dims.get((1, 1), 0) == 1
        # Bar degree 2, weight 2: alpha tensor alpha
        assert dims.get((2, 2), 0) == 1
        # Bar degree 3, weight 3: alpha^{otimes 3}
        assert dims.get((3, 3), 0) == 1

    def test_sl2_bar_dims(self):
        """sl_2 KM: 3 generators at weight 1."""
        result = bar_complex_dimensions(sl2_km(), max_weight=3, max_bar_deg=3)
        dims = result['dims']
        # Bar degree 1, weight 1: 3 generators
        assert dims.get((1, 1), 0) == 3
        # Bar degree 2, weight 2: 3^2 = 9 tensor products
        assert dims.get((2, 2), 0) == 9

    def test_virasoro_bar_dims(self):
        """Virasoro: one generator at weight 2."""
        result = bar_complex_dimensions(virasoro_family(), max_weight=6, max_bar_deg=3)
        dims = result['dims']
        # Bar degree 1, weight 2: one generator T
        assert dims.get((1, 2), 0) == 1
        # Bar degree 2, weight 4: T tensor T
        assert dims.get((2, 4), 0) == 1
        # Bar degree 3, weight 6: T^{otimes 3}
        assert dims.get((3, 6), 0) == 1
        # Bar degree 1 at weight 1: nothing
        assert dims.get((1, 1), 0) == 0

    def test_w3_bar_dims(self):
        """W_3: generators T (weight 2) and W (weight 3)."""
        result = bar_complex_dimensions(w3_family(), max_weight=6, max_bar_deg=3)
        dims = result['dims']
        # Bar degree 1, weight 2: T only
        assert dims.get((1, 2), 0) == 1
        # Bar degree 1, weight 3: W only
        assert dims.get((1, 3), 0) == 1
        # Bar degree 2, weight 4: TT only
        assert dims.get((2, 4), 0) == 1
        # Bar degree 2, weight 5: TW and WT = 2
        assert dims.get((2, 5), 0) == 2

    def test_conilpotent_from_dims(self):
        """Bar complex dimensions confirm conilpotency for all families."""
        for family in STANDARD_FAMILIES:
            result = bar_complex_dimensions(family, max_weight=4, max_bar_deg=4)
            assert result['conilpotent'] is True, f"Failed for {family.name}"


# ============================================================================
# X. QUILLEN EQUIVALENCE SCOPE
# ============================================================================

class TestQuillenScope:
    """Test which Quillen equivalence theorem applies to each family."""

    def test_heisenberg_all_levels(self):
        """Heisenberg: all three levels of Quillen equivalence apply."""
        result = quillen_equivalence_scope(heisenberg_family())
        assert result['level_1_vallette']['applies'] is True
        assert result['level_2_booth_lazarev']['applies'] is True
        assert result['level_3_heuts']['applies'] is True

    def test_minimal_model_only_heuts(self):
        """Minimal model: not Koszul, so only Heuts level-3 applies."""
        result = quillen_equivalence_scope(minimal_model_family())
        assert result['level_1_vallette']['applies'] is False
        assert result['level_2_booth_lazarev']['applies'] is False
        assert result['level_3_heuts']['applies'] is True

    def test_all_families_heuts_level(self):
        """All families are within Heuts' level-3 scope."""
        for family in ALL_FAMILIES:
            result = quillen_equivalence_scope(family)
            assert result['level_3_heuts']['applies'] is True


# ============================================================================
# XI. CROSS-FAMILY CONSISTENCY
# ============================================================================

class TestCrossFamilyConsistency:
    """Test cross-family consistency of nilcompleteness/conilcompleteness."""

    def test_all_nilcomplete(self):
        """Cross-family: all standard families nilcomplete."""
        result = cross_family_consistency_check()
        assert result['all_nilcomplete'] is True

    def test_all_conilpotent(self):
        """Cross-family: all standard families have conilpotent bar."""
        result = cross_family_consistency_check()
        assert result['all_conilpotent'] is True

    def test_all_within_heuts(self):
        """Cross-family: all within Heuts' scope."""
        result = cross_family_consistency_check()
        assert result['all_within_heuts'] is True

    def test_koszul_families_qi(self):
        """Cross-family: all Koszul families have bar-cobar qi."""
        result = cross_family_consistency_check()
        for name, data in result['families'].items():
            assert data['bar_cobar_qi'] is True, f"Failed for {name}"


# ============================================================================
# XII. MULTI-PATH AGREEMENT
# ============================================================================

class TestMultiPathAgreement:
    """Verify that different verification paths agree for each family.

    Per CLAUDE.md multi-path verification mandate: every claim needs
    3+ independent paths that converge to the same result.
    """

    def test_conilpotency_two_paths_agree(self):
        """Structural and explicit conilpotency agree for all families."""
        for family in STANDARD_FAMILIES:
            r1 = verify_conilpotency_weight_grading(family)
            r2 = verify_conilpotency_explicit(family, max_weight=4)
            assert r1['conilpotent'] == r2['conilpotent'], (
                f"Paths disagree for {family.name}: "
                f"structural={r1['conilpotent']}, explicit={r2['conilpotent']}"
            )

    def test_nilcompleteness_multiple_paths(self):
        """Nilcompleteness verified by 2+ independent paths for each family."""
        for family in STANDARD_FAMILIES:
            result = verify_nilcompleteness(family)
            assert result['num_independent_paths'] >= 2, (
                f"Only {result['num_independent_paths']} paths for {family.name}"
            )

    def test_koszul_heisenberg_three_paths(self):
        """Heisenberg: nilcompleteness verified by all three paths."""
        result = verify_nilcompleteness(heisenberg_family())
        assert result['num_independent_paths'] == 3

    def test_beta_gamma_two_paths(self):
        """beta-gamma: two paths (geometric + Koszul, not weight due to h_min=0)."""
        result = verify_nilcompleteness(beta_gamma_family())
        assert result['path1_geometric_pronilpotence'] is True
        assert result['path3_koszul_pbw'] is True
        # path2 fails because h_min = 0
        assert result['path2_weight_grading'] is False


# ============================================================================
# XIII. SPECIFIC KAPPA VALUES (CROSS-CHECK WITH AP1/AP39)
# ============================================================================

class TestKappaValues:
    """Verify kappa values are consistent with AP1/AP39 formulas."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP39)."""
        h = heisenberg_family(k=Fraction(3))
        assert h.kappa == 3

    def test_sl2_kappa(self):
        """kappa(sl_2, k=1) = dim(g)*(k+h^v)/(2*h^v) = 3*3/4 (AP1)."""
        km = sl2_km(k=Fraction(1))
        assert km.kappa == Fraction(9, 4)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP39)."""
        v = virasoro_family(c=Fraction(26))
        assert v.kappa == 13

    def test_virasoro_self_dual_kappa(self):
        """At c=13, kappa = 13/2 (AP8: self-dual point)."""
        v = virasoro_family(c=Fraction(13))
        assert v.kappa == Fraction(13, 2)

    def test_w3_kappa(self):
        """kappa(W_3) = c/2 (AP39: for Virasoro subalgebra; AP48 caveat)."""
        w = w3_family(c=Fraction(100))
        assert w.kappa == 50


# ============================================================================
# XIV. FAILURE MODES OFF THE KOSZUL LOCUS
# ============================================================================

class TestFailureModes:
    """Test that failure modes are correctly identified."""

    def test_minimal_model_ising_not_koszul(self):
        """Ising model M(3,4): not Koszul, bar-cobar NOT qi."""
        mm = minimal_model_family(3, 4)
        assert mm.is_koszul is False
        result = verify_bar_cobar_qi_scope(mm)
        assert result['bar_cobar_qi_genus_0'] is False

    def test_yang_lee_not_koszul(self):
        """Yang-Lee M(2,5): not Koszul."""
        yl = minimal_model_family(2, 5)
        assert yl.is_koszul is False
        result = koszul_locus_diagnostic(yl)
        assert result['on_koszul_locus'] is False

    def test_non_koszul_still_nilcomplete(self):
        """Non-Koszul algebras are STILL nilcomplete (geometric pro-nilpotence)."""
        for p, q in [(3, 4), (2, 5), (3, 5)]:
            mm = minimal_model_family(p, q)
            result = verify_nilcompleteness(mm)
            assert result['nilcomplete'] is True

    def test_non_koszul_still_conilpotent(self):
        """Non-Koszul algebras still have conilpotent bar coalgebras."""
        mm = minimal_model_family(3, 4)
        result = verify_conilpotency_weight_grading(mm)
        assert result['conilpotent'] is True


# ============================================================================
# XV. MASTER VERIFICATION
# ============================================================================

class TestMasterVerification:
    """Test the master verification function."""

    def test_master_verdict_safe(self):
        """Master verification: monograph is safe."""
        result = verify_heuts_fg_scope_all()
        assert result['verdict']['monograph_safe'] is True

    def test_master_all_families_covered(self):
        """Master verification covers all families."""
        result = verify_heuts_fg_scope_all()
        assert len(result['family_reports']) == len(ALL_FAMILIES)

    def test_master_heuts_boundary(self):
        """Master verification includes Heuts scope boundary."""
        result = verify_heuts_fg_scope_all()
        assert result['heuts_boundary']['case_1_chiral']['monograph_safe'] is True

    def test_master_pronilpotence(self):
        """Master verification confirms chiral pro-nilpotence."""
        result = verify_heuts_fg_scope_all()
        assert result['chiral_pronilpotence']['pro_nilpotent'] is True

    def test_master_cross_family(self):
        """Master verification: cross-family consistency passes."""
        result = verify_heuts_fg_scope_all()
        assert result['cross_family']['all_nilcomplete'] is True
        assert result['cross_family']['all_conilpotent'] is True


# ============================================================================
# XVI. SPECIFIC MONOGRAPH THEOREMS
# ============================================================================

class TestMonographTheorems:
    """Test that specific monograph theorems are within scope of Heuts/BL."""

    def test_theorem_a_verdier_intertwining(self):
        """Theorem A (Verdier intertwining) uses FG12's pro-nilpotent result.
        This is Case 1 of Heuts' boundary: automatic."""
        result = analyze_heuts_scope_boundary()
        assert result['case_1_chiral']['fg_prediction_status'].startswith('TRUE')

    def test_theorem_b_inversion_koszul_locus(self):
        """Theorem B (inversion) is on the Koszul locus: spectral sequence
        collapse gives qi independently of Heuts."""
        for family in STANDARD_FAMILIES:
            result = verify_bar_cobar_qi_scope(family)
            assert result['bar_cobar_qi_all_genera'] is True
            kd = koszul_locus_diagnostic(family)
            assert kd['on_koszul_locus'] is True

    def test_quillen_equivalence_conilpotent_coalgebras(self):
        """thm:quillen-equivalence-chiral operates on CONILPOTENT coalgebras,
        which is within Heuts' safe zone."""
        for family in STANDARD_FAMILIES:
            cn = verify_conilpotency_weight_grading(family)
            assert cn['conilpotent'] is True

    def test_thm_abstract_bar_cobar_fg12(self):
        """thm:abstract-bar-cobar (FG12 Thm 7.2.1) uses pro-nilpotence.
        Heuts confirms this is exactly the right condition."""
        result = verify_chiral_pronilpotence()
        assert result['pro_nilpotent'] is True

    def test_completion_necessity_off_koszul(self):
        """thm:completion-necessity correctly identifies when completion
        is needed -- this is precisely the nilcompleteness condition
        that Heuts identifies."""
        # Non-quadratic algebras need completion
        v = virasoro_family()
        assert v.needs_completion is True
        # Quadratic algebras do not
        h = heisenberg_family()
        assert h.needs_completion is False

    def test_conilpotency_convergence_theorem(self):
        """thm:conilpotency-convergence is confirmed by Heuts:
        conilpotent coalgebras are within the equivalence scope."""
        for family in STANDARD_FAMILIES:
            cn = verify_conilpotency_weight_grading(family)
            assert cn['conilpotent'] is True
            qs = verify_bar_cobar_qi_scope(family)
            assert qs['within_heuts_scope'] is True
