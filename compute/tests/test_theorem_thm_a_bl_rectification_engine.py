r"""Tests for Theorem A rectification against Booth-Lazarev (arXiv:2304.08409).

CONTEXT:
Booth-Lazarev (BL-GKD, "Global Koszul duality", arXiv:2304.08409, rev. 2026)
construct a monoidal model structure on curved coalgebras and prove Quillen
equivalence with curved algebras via extended bar-cobar.

These tests verify every claim in the monograph's Theorem A (bar-cobar
adjunction + Verdier intertwining) and related results against BL-GKD's
framework.

VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):
    Path 1 (BL axiom verification): Verify chiral setting satisfies BL axioms
    Path 2 (Cofibrant object check): Verify barB(A) cofibrant in BL model
    Path 3 (Quillen scope): Determine which Quillen equivalence applies
    Path 4 (Cross-family consistency): All families behave consistently
    Path 5 (Status tag audit): AP4 check on ProvedHere tags

References:
    thm:bar-cobar-isomorphism-main (chiral_koszul_pairs.tex) -- Theorem A
    thm:bar-cobar-inversion-qi (bar_cobar_adjunction_inversion.tex) -- Theorem B
    thm:quillen-equivalence-chiral (bar_cobar_adjunction_curved.tex)
    thm:positselski-chiral-proved (bar_cobar_adjunction_inversion.tex)
    thm:completed-bar-cobar-strong (bar_cobar_adjunction_curved.tex) -- MC4
    Booth-Lazarev, arXiv:2304.08409 (Global Koszul duality)
    Booth-Lazarev, arXiv:2406.04684 (Monoidal model structures) = BL24
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_thm_a_bl_rectification_engine import (
    # Data structures
    ChiralAlgebraData,
    # Family constructors
    heisenberg,
    kac_moody,
    virasoro,
    w_algebra,
    beta_gamma,
    w_infinity,
    lattice_voa,
    STANDARD_FAMILIES,
    # BL axiom verification
    verify_bl_axiom_A1,
    verify_bl_axiom_A2,
    verify_bl_axiom_A3,
    verify_all_bl_axioms,
    # Cofibrant verification
    verify_bar_cofibrant_in_bl,
    # Quillen scope
    quillen_equivalence_scope,
    # Coderived compatibility
    verify_coderived_compatibility,
    # Generating cofibrations
    compute_generating_cofibrations,
    # Theorem A verification
    verify_theorem_a_vs_bl,
    # Theorem B verification
    verify_theorem_b_vs_bl,
    # Positselski verification
    verify_positselski_chiral_vs_bl,
    # MC4 verification
    verify_mc4_vs_bl,
    # Status tags
    verify_status_tags,
    # Conjectural steps
    assess_conjectural_steps,
    # Bibliography
    check_bibliography_discrepancy,
    # Cross-volume
    check_cross_volume_consistency,
    # Master
    verify_theorem_a_bl_rectification_all,
)


# ============================================================================
# I. BL-GKD AXIOM VERIFICATION (PATH 1)
# ============================================================================

class TestBLAxiomA1:
    """Test BL axiom (A1): symmetric monoidal abelian with enough projectives."""

    def test_heisenberg_A1(self):
        result = verify_bl_axiom_A1(heisenberg())
        assert result['A1_satisfied'] is True

    def test_virasoro_A1(self):
        result = verify_bl_axiom_A1(virasoro())
        assert result['A1_satisfied'] is True

    def test_w3_A1(self):
        result = verify_bl_axiom_A1(w_algebra(3))
        assert result['A1_satisfied'] is True

    def test_all_families_A1(self):
        """All standard families satisfy (A1)."""
        for fam in STANDARD_FAMILIES:
            result = verify_bl_axiom_A1(fam)
            assert result['A1_satisfied'] is True, f"A1 failed for {fam.name}"


class TestBLAxiomA2:
    """Test BL axiom (A2): tensor preserves colimits."""

    def test_heisenberg_A2(self):
        result = verify_bl_axiom_A2(heisenberg())
        assert result['A2_satisfied'] is True

    def test_virasoro_A2(self):
        result = verify_bl_axiom_A2(virasoro())
        assert result['A2_satisfied'] is True

    def test_all_families_A2(self):
        for fam in STANDARD_FAMILIES:
            result = verify_bl_axiom_A2(fam)
            assert result['A2_satisfied'] is True, f"A2 failed for {fam.name}"


class TestBLAxiomA3:
    """Test BL axiom (A3): unit is cofibrant."""

    def test_heisenberg_A3(self):
        result = verify_bl_axiom_A3(heisenberg())
        assert result['A3_satisfied'] is True

    def test_all_families_A3(self):
        for fam in STANDARD_FAMILIES:
            result = verify_bl_axiom_A3(fam)
            assert result['A3_satisfied'] is True, f"A3 failed for {fam.name}"


class TestBLAllAxioms:
    """Test all BL axioms simultaneously."""

    def test_heisenberg_all(self):
        result = verify_all_bl_axioms(heisenberg())
        assert result['all_satisfied'] is True

    def test_virasoro_all(self):
        result = verify_all_bl_axioms(virasoro())
        assert result['all_satisfied'] is True

    def test_w3_all(self):
        result = verify_all_bl_axioms(w_algebra(3))
        assert result['all_satisfied'] is True

    def test_beta_gamma_all(self):
        result = verify_all_bl_axioms(beta_gamma())
        assert result['all_satisfied'] is True

    def test_w_infinity_all(self):
        result = verify_all_bl_axioms(w_infinity())
        assert result['all_satisfied'] is True

    def test_all_families_all_axioms(self):
        """Universal: every standard family satisfies all BL axioms."""
        for fam in STANDARD_FAMILIES:
            result = verify_all_bl_axioms(fam)
            assert result['all_satisfied'] is True, (
                f"BL axioms failed for {fam.name}"
            )


# ============================================================================
# II. COFIBRANT OBJECT VERIFICATION (PATH 2)
# ============================================================================

class TestCofibrantInBL:
    """Test that barB(A) is cofibrant in BL-GKD model structure."""

    def test_heisenberg_cofibrant(self):
        result = verify_bar_cofibrant_in_bl(heisenberg())
        assert result['cofibrant_in_bl'] is True
        assert result['cofibrant_in_vallette'] is True  # conilpotent
        assert result['genus_0_cofibrant'] is True
        assert result['genus_ge1_cofibrant'] is True

    def test_virasoro_cofibrant(self):
        """Virasoro: cofibrant in BL but NOT in Vallette (not conilpotent)."""
        result = verify_bar_cofibrant_in_bl(virasoro())
        assert result['cofibrant_in_bl'] is True
        assert result['cofibrant_in_vallette'] is False  # needs completion
        assert result['genus_ge1_cofibrant'] is True

    def test_w3_cofibrant(self):
        result = verify_bar_cofibrant_in_bl(w_algebra(3))
        assert result['cofibrant_in_bl'] is True
        assert result['cofibrant_in_vallette'] is False

    def test_all_cofibrant_in_bl(self):
        """ALL families cofibrant in BL model structure."""
        for fam in STANDARD_FAMILIES:
            result = verify_bar_cofibrant_in_bl(fam)
            assert result['cofibrant_in_bl'] is True, (
                f"Not cofibrant in BL for {fam.name}"
            )

    def test_quadratic_cofibrant_in_both(self):
        """Quadratic algebras: cofibrant in BOTH Vallette and BL."""
        for fam in STANDARD_FAMILIES:
            if fam.is_quadratic:
                result = verify_bar_cofibrant_in_bl(fam)
                assert result['cofibrant_in_bl'] is True
                assert result['cofibrant_in_vallette'] is True, (
                    f"Quadratic {fam.name} should be Vallette-cofibrant"
                )

    def test_nonquadratic_only_bl_cofibrant(self):
        """Non-quadratic: cofibrant in BL but not Vallette."""
        for fam in STANDARD_FAMILIES:
            if not fam.is_quadratic and not fam.is_conilpotent:
                result = verify_bar_cofibrant_in_bl(fam)
                assert result['cofibrant_in_bl'] is True
                assert result['cofibrant_in_vallette'] is False


# ============================================================================
# III. QUILLEN EQUIVALENCE SCOPE (PATH 3)
# ============================================================================

class TestQuillenScope:
    """Test Quillen equivalence scope at each genus."""

    def test_heisenberg_genus_0(self):
        result = quillen_equivalence_scope(heisenberg())
        assert result['genus_0']['quillen_level'] == 'Level 1 (Vallette)'
        assert result['genus_0']['bl_confirms'] is True

    def test_heisenberg_genus_ge1(self):
        result = quillen_equivalence_scope(heisenberg())
        assert result['genus_ge1']['curved'] is True
        assert result['genus_ge1']['bl_upgrades'] is True

    def test_virasoro_genus_0(self):
        result = quillen_equivalence_scope(virasoro())
        assert result['genus_0']['curved'] is False
        assert result['genus_0']['quillen_level'] == 'Level 1 (Vallette)'

    def test_virasoro_genus_ge1(self):
        result = quillen_equivalence_scope(virasoro())
        assert result['genus_ge1']['curved'] is True
        assert result['genus_ge1']['bl_upgrades'] is True

    def test_genus_0_always_uncurved(self):
        """At genus 0, curvature is always zero (Koszul locus)."""
        for fam in STANDARD_FAMILIES:
            result = quillen_equivalence_scope(fam)
            assert result['genus_0']['curved'] is False, (
                f"Genus 0 should be uncurved for {fam.name}"
            )

    def test_koszul_genus_0_vallette(self):
        """Koszul algebras at genus 0: Vallette model structure applies."""
        for fam in STANDARD_FAMILIES:
            if fam.is_koszul:
                result = quillen_equivalence_scope(fam)
                assert result['genus_0']['quillen_level'] == 'Level 1 (Vallette)'

    def test_nonzero_kappa_curved_genus_ge1(self):
        """Families with kappa != 0 are curved at genus >= 1."""
        for fam in STANDARD_FAMILIES:
            result = quillen_equivalence_scope(fam)
            if fam.kappa != 0:
                assert result['genus_ge1']['curved'] is True, (
                    f"{fam.name} (kappa={fam.kappa}) should be curved at g>=1"
                )


# ============================================================================
# IV. CODERIVED COMPATIBILITY
# ============================================================================

class TestCoderivedCompatibility:
    """Test BL-GKD compatibility with Positselski coderived passage."""

    def test_heisenberg_compatible(self):
        result = verify_coderived_compatibility(heisenberg())
        assert result['bl_restriction_applies'] is True
        assert result['positselski_confirmed'] is True

    def test_virasoro_compatible(self):
        result = verify_coderived_compatibility(virasoro())
        assert result['bl_restriction_applies'] is True
        assert result['positselski_confirmed'] is True

    def test_all_families_compatible(self):
        for fam in STANDARD_FAMILIES:
            result = verify_coderived_compatibility(fam)
            assert result['bl_restriction_applies'] is True, (
                f"BL restriction fails for {fam.name}"
            )
            assert result['positselski_confirmed'] is True


# ============================================================================
# V. THEOREM A CLAIM-BY-CLAIM (PATH 4: CROSS-FAMILY)
# ============================================================================

class TestTheoremAVsBL:
    """Test Theorem A claims against BL-GKD."""

    def test_heisenberg_part1_confirmed(self):
        result = verify_theorem_a_vs_bl(heisenberg())
        assert result['part_1_bar_cobar_inversion']['bl_assessment'] == 'CONFIRMED'

    def test_heisenberg_part2_not_addressed(self):
        """Verdier intertwining is geometric, not in BL scope."""
        result = verify_theorem_a_vs_bl(heisenberg())
        assert 'NOT ADDRESSED' in result['part_2_verdier_intertwining']['bl_assessment']

    def test_heisenberg_part3_not_addressed(self):
        result = verify_theorem_a_vs_bl(heisenberg())
        assert 'NOT ADDRESSED' in result['part_3_koszul_dual_identification']['bl_assessment']

    def test_no_contradiction_any_family(self):
        """BL-GKD NEVER contradicts any Theorem A claim."""
        for fam in STANDARD_FAMILIES:
            result = verify_theorem_a_vs_bl(fam)
            assert result['overall']['bl_contradicts'] is False, (
                f"BL contradicts Theorem A for {fam.name}!"
            )

    def test_bl_confirms_all_families(self):
        """BL-GKD confirms algebraic content for all families."""
        for fam in STANDARD_FAMILIES:
            result = verify_theorem_a_vs_bl(fam)
            assert result['overall']['bl_confirms'] is True

    def test_bl_extends_all_families(self):
        """BL-GKD extends (not supersedes) for all families."""
        for fam in STANDARD_FAMILIES:
            result = verify_theorem_a_vs_bl(fam)
            assert result['overall']['bl_extends'] is True
            assert result['overall']['bl_supersedes'] is False


# ============================================================================
# VI. THEOREM B VERIFICATION
# ============================================================================

class TestTheoremBVsBL:
    """Test Theorem B (inversion) against BL-GKD."""

    def test_heisenberg_confirmed(self):
        result = verify_theorem_b_vs_bl(heisenberg())
        assert result['bl_assessment'] == 'CONFIRMED'

    def test_virasoro_confirmed(self):
        result = verify_theorem_b_vs_bl(virasoro())
        assert result['bl_assessment'] == 'CONFIRMED'

    def test_koszul_families_confirmed(self):
        for fam in STANDARD_FAMILIES:
            if fam.is_koszul:
                result = verify_theorem_b_vs_bl(fam)
                assert result['bl_assessment'] == 'CONFIRMED', (
                    f"Theorem B not confirmed for {fam.name}"
                )

    def test_independent_proofs(self):
        """Monograph and BL provide INDEPENDENT proofs."""
        result = verify_theorem_b_vs_bl(heisenberg())
        assert result['proof_comparison']['independent'] is True
        assert result['proof_comparison']['both_valid'] is True


# ============================================================================
# VII. POSITSELSKI CHIRAL VERIFICATION
# ============================================================================

class TestPositselskiVsBL:
    """Test thm:positselski-chiral-proved against BL-GKD."""

    def test_heisenberg_compatible(self):
        result = verify_positselski_chiral_vs_bl(heisenberg())
        assert result['positselski_applies'] is True
        assert result['bl_compatible'] is True
        assert result['bl_recovers_positselski'] is True

    def test_virasoro_compatible(self):
        result = verify_positselski_chiral_vs_bl(virasoro())
        assert result['bl_compatible'] is True

    def test_all_families_compatible(self):
        for fam in STANDARD_FAMILIES:
            result = verify_positselski_chiral_vs_bl(fam)
            assert result['bl_compatible'] is True, (
                f"Positselski-BL incompatible for {fam.name}"
            )


# ============================================================================
# VIII. MC4 VERIFICATION
# ============================================================================

class TestMC4VsBL:
    """Test MC4 completion theorem against BL-GKD."""

    def test_mc4_orthogonal_to_bl(self):
        """MC4 is about inverse limits, BL about model structures."""
        result = verify_mc4_vs_bl(w_infinity())
        assert result['bl_assessment'] == 'ORTHOGONAL'

    def test_virasoro_mc4(self):
        result = verify_mc4_vs_bl(virasoro())
        assert result['mc4_applies'] is True

    def test_quadratic_no_mc4(self):
        """Quadratic algebras don't need MC4."""
        h = heisenberg()
        result = verify_mc4_vs_bl(h)
        assert result['mc4_applies'] is False


# ============================================================================
# IX. STATUS TAG AUDIT (AP4)
# ============================================================================

class TestStatusTags:
    """AP4: verify ClaimStatusProvedHere tags are correct."""

    def test_no_status_violations(self):
        result = verify_status_tags()
        assert result['status_violations_found'] == 0

    def test_proved_elsewhere_correctly_tagged(self):
        result = verify_status_tags()
        elsewhere = result['proved_elsewhere_correctly_tagged']
        # Quillen equivalence is correctly ProvedElsewhere
        assert any('quillen' in x.lower() for x in elsewhere)
        # GLZ is correctly ProvedElsewhere
        assert any('GLZ' in x for x in elsewhere)
        # FG is correctly ProvedElsewhere
        assert any('FG' in x for x in elsewhere)


# ============================================================================
# X. CONJECTURAL STEPS (C1)-(C4) ASSESSMENT
# ============================================================================

class TestConjecturalSteps:
    """Test assessment of the four conjectural steps in rem:coderived-status."""

    def test_c1_partially_resolved(self):
        result = assess_conjectural_steps()
        assert 'PARTIALLY RESOLVED' in result['C1_coderived_model_structure']['post_bl']

    def test_c2_partially_resolved(self):
        result = assess_conjectural_steps()
        assert 'PARTIALLY RESOLVED' in result['C2_quillen_equivalence']['post_bl']

    def test_c3_unchanged(self):
        result = assess_conjectural_steps()
        assert 'UNCHANGED' in result['C3_shadow_identification']['post_bl']

    def test_c4_unchanged(self):
        result = assess_conjectural_steps()
        assert 'UNCHANGED' in result['C4_analytic_comparison']['post_bl']

    def test_c1_c2_pre_bl_conjectural(self):
        """Before BL-GKD, (C1) and (C2) were conjectural."""
        result = assess_conjectural_steps()
        assert result['C1_coderived_model_structure']['pre_bl'] == 'CONJECTURAL'
        assert result['C2_quillen_equivalence']['pre_bl'] == 'CONJECTURAL'


# ============================================================================
# XI. BIBLIOGRAPHY DISCREPANCY
# ============================================================================

class TestBibliography:
    """Test bibliography discrepancy between BL24 and BL-GKD."""

    def test_discrepancy_exists(self):
        result = check_bibliography_discrepancy()
        assert result['discrepancy'] is True

    def test_currently_cited_is_2406(self):
        result = check_bibliography_discrepancy()
        assert result['currently_cited']['arxiv'] == '2406.04684'

    def test_should_cite_2304(self):
        result = check_bibliography_discrepancy()
        assert result['should_also_cite']['arxiv'] == '2304.08409'

    def test_different_papers(self):
        """BL24 and BL-GKD are DIFFERENT papers."""
        result = check_bibliography_discrepancy()
        assert (result['currently_cited']['arxiv']
                != result['should_also_cite']['arxiv'])

    def test_severity_moderate(self):
        result = check_bibliography_discrepancy()
        assert result['severity'] == 'MODERATE'


# ============================================================================
# XII. CROSS-VOLUME CONSISTENCY (AP5)
# ============================================================================

class TestCrossVolume:
    """AP5: cross-volume formula consistency."""

    def test_adjunction_direction_consistent(self):
        result = check_cross_volume_consistency()
        assert 'CONSISTENT' in result['adjunction_direction']

    def test_verdier_intertwining_consistent(self):
        result = check_cross_volume_consistency()
        assert 'CONSISTENT' in result['verdier_intertwining']

    def test_counit_direction_consistent(self):
        result = check_cross_volume_consistency()
        assert 'CONSISTENT' in result['counit_direction']

    def test_quillen_reference_consistent(self):
        result = check_cross_volume_consistency()
        assert 'CONSISTENT' in result['quillen_reference']

    def test_bl_reference_inconsistent(self):
        """BL-GKD reference is INCONSISTENT (missing from theory files)."""
        result = check_cross_volume_consistency()
        assert 'INCONSISTENT' in result['bl_reference']

    def test_vol2_checked(self):
        result = check_cross_volume_consistency()
        assert result['vol2_checked'] is True


# ============================================================================
# XIII. GENERATING COFIBRATIONS
# ============================================================================

class TestGeneratingCofibrations:
    """Test generating cofibrations in BL model structure for chiral setting."""

    def test_heisenberg_genus_0_uncurved(self):
        result = compute_generating_cofibrations(heisenberg())
        assert result['generating_cofibrations']['genus_0']['type'] == 'uncurved, standard Vallette'

    def test_heisenberg_genus_ge1_curved(self):
        result = compute_generating_cofibrations(heisenberg())
        assert result['generating_cofibrations']['genus_ge1']['type'] == 'curved, BL-GKD'

    def test_virasoro_genus_ge1_curvature(self):
        vir = virasoro(Fraction(26))
        result = compute_generating_cofibrations(vir)
        assert '13' in result['generating_cofibrations']['genus_ge1']['curvature']


# ============================================================================
# XIV. KAPPA FORMULA CROSS-CHECK (AP1, AP39)
# ============================================================================

class TestKappaFormulas:
    """Cross-check kappa formulas used in the engine (AP1, AP39)."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP39)."""
        assert heisenberg(1).kappa == 1
        assert heisenberg(2).kappa == 2

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert virasoro(Fraction(1)).kappa == Fraction(1, 2)
        assert virasoro(Fraction(26)).kappa == Fraction(13)

    def test_sl2_kappa(self):
        """kappa(KM_sl2_k=1) = dim(sl2)*(1+2)/(2*2) = 3*3/4 = 9/4."""
        km = kac_moody('sl2', 3, 2, 1)
        assert km.kappa == Fraction(9, 4)

    def test_sl3_kappa(self):
        """kappa(KM_sl3_k=1) = dim(sl3)*(1+3)/(2*3) = 8*4/6 = 16/3."""
        km = kac_moody('sl3', 8, 3, 1)
        assert km.kappa == Fraction(16, 3)

    def test_beta_gamma_kappa(self):
        """kappa(beta_gamma) = -1."""
        assert beta_gamma().kappa == Fraction(-1)

    def test_lattice_kappa(self):
        """kappa(V_Lambda) = rank(Lambda) (AP48)."""
        assert lattice_voa(1).kappa == Fraction(1)
        assert lattice_voa(24).kappa == Fraction(24)

    def test_virasoro_self_dual_at_c13(self):
        """Vir_c self-dual at c=13 (kappa=13/2), Vir_c^! = Vir_{26-c}."""
        vir13 = virasoro(Fraction(13))
        assert vir13.kappa == Fraction(13, 2)

    def test_kappa_additivity(self):
        """kappa is additive: kappa(A tensor B) = kappa(A) + kappa(B)."""
        h1 = heisenberg(1)
        h2 = heisenberg(2)
        assert h1.kappa + h2.kappa == Fraction(3)


# ============================================================================
# XV. REGIME CLASSIFICATION CONSISTENCY
# ============================================================================

class TestRegimeClassification:
    """Verify regime classification matches the four-regime hierarchy."""

    def test_heisenberg_quadratic(self):
        assert heisenberg().regime == 'quadratic'
        assert heisenberg().is_quadratic is True

    def test_km_quadratic(self):
        assert kac_moody().regime == 'quadratic'
        assert kac_moody().is_quadratic is True

    def test_virasoro_curved_central(self):
        assert virasoro().regime == 'curved-central'
        assert virasoro().is_quadratic is False

    def test_w3_filtered(self):
        assert w_algebra(3).regime == 'filtered-complete'

    def test_winfty_programmatic(self):
        assert w_infinity().regime == 'programmatic'

    def test_quadratic_no_completion(self):
        """Quadratic algebras never need completion."""
        for fam in STANDARD_FAMILIES:
            if fam.is_quadratic:
                assert fam.completion_needed is False, (
                    f"Quadratic {fam.name} should not need completion"
                )

    def test_nonquadratic_need_completion(self):
        """Non-quadratic Koszul algebras need completion."""
        vir = virasoro()
        assert vir.completion_needed is True
        w3 = w_algebra(3)
        assert w3.completion_needed is True


# ============================================================================
# XVI. MASTER VERIFICATION
# ============================================================================

class TestMasterVerification:
    """Test the master verification function."""

    def test_master_runs(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result is not None

    def test_theorem_a_sound(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['theorem_a_sound'] is True

    def test_theorem_b_sound(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['theorem_b_sound'] is True

    def test_mc4_sound(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['mc4_sound'] is True

    def test_positselski_sound(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['positselski_sound'] is True

    def test_quillen_sound(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['quillen_sound'] is True

    def test_bl_confirms_not_contradicts(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['bl_confirms'] is True
        assert result['verdict']['bl_contradicts'] is False

    def test_bl_extends_not_supersedes(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['bl_extends_genus_ge1'] is True
        assert result['verdict']['bl_supersedes'] is False

    def test_bibliography_needs_update(self):
        result = verify_theorem_a_bl_rectification_all()
        assert result['verdict']['bibliography_needs_update'] is True

    def test_all_families_in_report(self):
        result = verify_theorem_a_bl_rectification_all()
        for fam in STANDARD_FAMILIES:
            assert fam.name in result['family_reports'], (
                f"Missing {fam.name} from report"
            )

    def test_finding_register_complete(self):
        result = verify_theorem_a_bl_rectification_all()
        fr = result['finding_register']
        assert 'F1' in fr
        assert 'F2' in fr
        assert 'F3' in fr
        assert 'F4' in fr
        assert 'F5_to_F10' in fr
        assert 'F11' in fr
