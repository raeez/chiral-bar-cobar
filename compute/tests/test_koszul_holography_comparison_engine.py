r"""Tests for koszul_holography_comparison_engine.

Unified synthesis of four research agents' findings:
  Agent 1 (Costello form factors): 4-layer Koszul duality
  Agent 2 (Twisted holography):    Genus-0 agreement, our extensions
  Agent 3 (Boundary VOA):          S-duality != Koszul duality
  Agent 4 (3d mirror):             Four distinct dualities

VERIFICATION STRUCTURE (multi-path per CLAUDE.md):
  Path 1: Direct formula computation
  Path 2: Cross-family consistency (additivity, complementarity)
  Path 3: Duality comparison (KD vs S vs mirror vs categorical)
  Path 4: Limiting cases
  Path 5: AP compliance (AP19, AP24, AP25, AP33, AP39, AP50)
  Path 6: Literature values with convention check (AP38)

Test count: 65+ tests covering:
  1. Costello's four layers                                [12 tests]
  2. Four distinct dualities                               [10 tests]
  3. Koszul vs S-duality quantitative                      [8 tests]
  4. Holography = KD status (proved vs conjectural)        [8 tests]
  5. Genus tower (our extension)                           [8 tests]
  6. Kappa cross-checks                                    [8 tests]
  7. Collision residue AP19                                [5 tests]
  8. Master synthesis consistency                          [6 tests]
  9. Uncited papers                                        [3 tests]
"""

from __future__ import annotations

from fractions import Fraction

import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from koszul_holography_comparison_engine import (
    # Kappa formulas
    kappa_km, kappa_slN, kappa_glN, kappa_virasoro,
    kappa_heisenberg, kappa_betagamma, kappa_bc,
    kappa_symplectic_boson,
    # Layer comparisons
    CostelloLayer, layer1_cg_bv, layer2_cwy,
    layer3_m2_holography, layer4_celestial_twisted,
    # Duality comparisons
    DualityType, chiral_koszul_comparison, s_duality_comparison,
    mirror_3d_comparison, categorical_koszul_comparison,
    # Holography status
    holography_status_m2, holography_status_d3,
    holography_status_ads3, holography_status_celestial,
    # Quantitative
    genus_tower_extension, koszul_vs_s_duality_sl2,
    koszul_vs_s_duality_coincidence_locus,
    collision_residue_pole_check,
    # Synthesis
    full_synthesis, uncited_costello_papers,
    # Internal
    _lambda_fp, _frac,
)


# ===========================================================================
# 1. Costello's four layers — structural tests
# ===========================================================================

class TestCostelloFourLayers:
    """Verify the four-layer structure of Costello's Koszul duality."""

    def test_layer1_cg_bv_proved(self):
        """Layer 1 (CG BV): PROVED at genus 0."""
        layer = layer1_cg_bv()
        assert layer.layer == CostelloLayer.CG_BV
        assert "PROVED" in layer.proved_vs_conjectural

    def test_layer1_our_extensions_nonempty(self):
        """We have genuine extensions beyond CG BV."""
        layer = layer1_cg_bv()
        assert len(layer.our_extensions) >= 5
        # Must include genus tower
        assert any("genus" in ext.lower() for ext in layer.our_extensions)

    def test_layer2_cwy_r_matrix_match(self):
        """Layer 2 (CWY): R-matrix matches our collision residue."""
        layer = layer2_cwy()
        assert "collision residue" in layer.our_identification.lower() or \
               "r(z)" in layer.our_identification

    def test_layer2_dk_bridge(self):
        """Layer 2 references the DK bridge (DK-0 through DK-3)."""
        layer = layer2_cwy()
        assert "DK" in layer.our_identification

    def test_layer3_m2_genus_0_only(self):
        """Layer 3 (M2): Costello's proof is genus 0 only."""
        layer = layer3_m2_holography()
        assert "genus 0" in layer.costello_content.lower() or \
               "GENUS 0" in layer.costello_content

    def test_layer3_m2_mixed_status(self):
        """Layer 3 status is MIXED (Costello proved at g=0, we extend)."""
        layer = layer3_m2_holography()
        assert "MIXED" in layer.proved_vs_conjectural

    def test_layer3_our_genus_tower_extension(self):
        """Layer 3: our genus tower is a genuine extension."""
        layer = layer3_m2_holography()
        assert any("genus tower" in ext.lower() for ext in layer.our_extensions)

    def test_layer4_mostly_conjectural(self):
        """Layer 4 (Celestial/Twisted): mostly CONJECTURAL."""
        layer = layer4_celestial_twisted()
        assert "CONJECTURAL" in layer.proved_vs_conjectural

    def test_layer4_boundary_voa_proved(self):
        """Layer 4: boundary VOA identification IS proved."""
        layer = layer4_celestial_twisted()
        assert "boundary VOA" in layer.proved_vs_conjectural.lower() or \
               "boundary" in layer.proved_vs_conjectural.lower()

    def test_all_layers_have_costello_advantages(self):
        """Each layer has genuine Costello advantages we lack."""
        for layer_fn in [layer1_cg_bv, layer2_cwy,
                         layer3_m2_holography, layer4_celestial_twisted]:
            layer = layer_fn()
            assert len(layer.costello_advantages) >= 3

    def test_all_layers_have_our_extensions(self):
        """Each layer has genuine extensions from our framework."""
        for layer_fn in [layer1_cg_bv, layer2_cwy,
                         layer3_m2_holography, layer4_celestial_twisted]:
            layer = layer_fn()
            assert len(layer.our_extensions) >= 5

    def test_four_layers_cover_four_distinct_operations(self):
        """The four layers are distinct operations, not overlapping."""
        layers = [layer1_cg_bv(), layer2_cwy(),
                  layer3_m2_holography(), layer4_celestial_twisted()]
        layer_types = {l.layer for l in layers}
        assert len(layer_types) == 4


# ===========================================================================
# 2. Four distinct dualities (Agent 3 + Agent 4 findings)
# ===========================================================================

class TestFourDualities:
    """The four dualities (KD, S, mirror, categorical) are DISTINCT."""

    def test_chiral_kd_is_theorem_a(self):
        """Chiral Koszul duality IS our Theorem A."""
        comp = chiral_koszul_comparison()
        assert comp.duality == DualityType.CHIRAL_KOSZUL
        assert "Theorem A" in comp.relation_to_our_theorem_a

    def test_s_duality_generically_different(self):
        """S-duality is generically DIFFERENT from Koszul duality."""
        comp = s_duality_comparison()
        assert "DIFFERENT" in comp.relation_to_our_theorem_a.upper() or \
               "GENERICALLY DIFFERENT" in comp.relation_to_our_theorem_a.upper()

    def test_s_duality_coincidence_locus(self):
        """S-duality = KD only at Psi^2 = -1 (Agent 3 finding)."""
        comp = s_duality_comparison()
        assert "Psi" in comp.when_they_coincide or "self-dual" in comp.when_they_coincide

    def test_mirror_no_direct_relation(self):
        """3d mirror symmetry has NO direct relation to our Theorem A."""
        comp = mirror_3d_comparison()
        assert "NO DIRECT" in comp.relation_to_our_theorem_a.upper()

    def test_mirror_exchanges_branches(self):
        """3d mirror exchanges Coulomb/Higgs branches, not bar complexes."""
        comp = mirror_3d_comparison()
        assert "Coulomb" in comp.definition or "Higgs" in comp.definition

    def test_categorical_kd_is_categorical_lift(self):
        """Categorical KD is the categorical LIFT of our Theorem A."""
        comp = categorical_koszul_comparison()
        assert "LIFT" in comp.relation_to_our_theorem_a.upper() or \
               "DK" in comp.relation_to_our_theorem_a

    def test_categorical_kd_mc3_proved(self):
        """Categorical KD on evaluation core: MC3 Layers 1+2 proved for all types; Layer 3 type A only."""
        comp = categorical_koszul_comparison()
        assert "MC3" in comp.when_they_coincide or \
               "evaluation" in comp.when_they_coincide.lower()

    def test_four_dualities_all_have_discrepancy_info(self):
        """Each duality comparison explains when they differ."""
        for comp_fn in [chiral_koszul_comparison, s_duality_comparison,
                        mirror_3d_comparison, categorical_koszul_comparison]:
            comp = comp_fn()
            assert comp.when_they_differ  # nonempty string

    def test_s_duality_has_quantitative_discrepancy(self):
        """S-duality comparison includes a quantitative formula."""
        comp = s_duality_comparison()
        assert comp.discrepancy_formula is not None
        assert "sl_2" in comp.discrepancy_formula

    def test_chiral_kd_no_discrepancy(self):
        """Chiral KD has no discrepancy (it IS our theorem)."""
        comp = chiral_koszul_comparison()
        assert comp.discrepancy_formula is None


# ===========================================================================
# 3. Koszul vs S-duality — quantitative (Agent 3 key finding)
# ===========================================================================

class TestKoszulVsSDuality:
    """Quantitative comparison: KD level vs S-dual level for sl_2."""

    def test_sl2_kd_level(self):
        """Koszul dual of sl_2 at k sends k -> -k-4."""
        for k in [1, 2, 3, 5]:
            result = koszul_vs_s_duality_sl2(Fraction(k))
            assert result["koszul_dual_level"] == Fraction(-k - 4)

    def test_sl2_s_dual_level(self):
        """S-dual of sl_2 at k: Psi = k+2, Psi' = -1/Psi, k' = Psi'-2.

        At k=1: Psi=3, Psi'=-1/3, k'=-1/3-2=-7/3.
        """
        result = koszul_vs_s_duality_sl2(Fraction(1))
        assert result["s_dual_level"] == Fraction(-7, 3)

    def test_sl2_levels_differ_at_generic_k(self):
        """At generic k, Koszul dual level != S-dual level."""
        for k in [1, 2, 3, 5, 10]:
            result = koszul_vs_s_duality_sl2(Fraction(k))
            assert result["levels_match"] is False

    def test_sl2_levels_match_at_k_minus1(self):
        """At k=-1: both dualities give dual level -3.

        KD: -(-1)-4 = -3. S-dual: Psi=-1+2=1, Psi'=-1, k'=-1-2=-3. Match.
        """
        result = koszul_vs_s_duality_sl2(Fraction(-1))
        assert result["levels_match"] is True
        assert result["koszul_dual_level"] == Fraction(-3)
        assert result["s_dual_level"] == Fraction(-3)

    def test_sl2_levels_match_at_k_minus3(self):
        """At k=-3: both dualities give dual level -1.

        KD: -(-3)-4 = -1. S-dual: Psi=-3+2=-1, Psi'=-1/(-1)=1, k'=1-2=-1. Match.
        """
        result = koszul_vs_s_duality_sl2(Fraction(-3))
        assert result["levels_match"] is True
        assert result["koszul_dual_level"] == Fraction(-1)
        assert result["s_dual_level"] == Fraction(-1)

    def test_coincidence_locus(self):
        """The coincidence locus is exactly k=-1 and k=-3."""
        locus = koszul_vs_s_duality_coincidence_locus()
        assert sorted(locus["coincidence_levels"]) == [-3, -1]
        assert sorted(locus["expected"]) == [-3, -1]

    def test_kappa_complementarity_always_holds(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0 (AP24 for KM)."""
        for k in [1, 2, 3, -1, -3, 5, 10]:
            if k == -2:
                continue  # critical
            result = koszul_vs_s_duality_sl2(Fraction(k))
            assert result["kappa_sum_koszul"] == 0

    def test_critical_level_excluded(self):
        """Critical level k=-2 excluded (Sugawara undefined)."""
        with pytest.raises(ValueError, match="Critical"):
            kappa_slN(2, Fraction(-2))


# ===========================================================================
# 4. Holography = KD status (proved vs conjectural)
# ===========================================================================

class TestHolographyStatus:
    """Status of the "Holography = Koszul duality" thesis."""

    def test_m2_kd_proved_perturbatively(self):
        """M2 brane: Koszul duality PROVED perturbatively."""
        status = holography_status_m2()
        assert status.koszul_duality_proved is True
        assert "genus 0" in status.koszul_duality_scope.lower()

    def test_m2_bulk_id_not_proved(self):
        """M2 brane: bulk identification NOT proved."""
        status = holography_status_m2()
        assert status.bulk_identification_proved is False

    def test_d3_kd_not_proved(self):
        """D3 brane: full Koszul duality NOT proved."""
        status = holography_status_d3()
        assert status.koszul_duality_proved is False

    def test_ads3_kd_not_proved(self):
        """AdS_3: full Koszul duality NOT proved."""
        status = holography_status_ads3()
        assert status.koszul_duality_proved is False

    def test_celestial_kd_not_proved(self):
        """Celestial: full Koszul duality NOT proved."""
        status = holography_status_celestial()
        assert status.koszul_duality_proved is False

    def test_all_systems_boundary_voa_proved(self):
        """Boundary VOA identification PROVED for all systems."""
        for status_fn in [holography_status_m2, holography_status_d3,
                          holography_status_ads3, holography_status_celestial]:
            status = status_fn()
            assert status.boundary_voa_proved is True

    def test_all_systems_our_theorem_a_applies(self):
        """Our Theorem A applies to ALL systems (it is algebraic, not physical)."""
        for status_fn in [holography_status_m2, holography_status_d3,
                          holography_status_ads3, holography_status_celestial]:
            status = status_fn()
            assert status.our_theorem_a_applies is True

    def test_all_systems_our_genus_tower_computed(self):
        """Our genus tower is computed for ALL systems."""
        for status_fn in [holography_status_m2, holography_status_d3,
                          holography_status_ads3, holography_status_celestial]:
            status = status_fn()
            assert status.our_genus_tower_computed is True


# ===========================================================================
# 5. Genus tower — our key extension
# ===========================================================================

class TestGenusTower:
    """The genus tower F_g = kappa * lambda_g is our central extension."""

    def test_lambda_fp_values(self):
        """Standard Faber-Pandharipande values."""
        assert _lambda_fp(1) == Fraction(1, 24)
        assert _lambda_fp(2) == Fraction(7, 5760)
        assert _lambda_fp(3) == Fraction(31, 967680)

    def test_m2_genus_tower(self):
        """M2 brane (N=1): kappa = -2, F_1 = -1/12."""
        kap = Fraction(-2)  # kappa_abjm(1,1) = -(1+1)
        tower = genus_tower_extension("M2_N1", kap)
        assert tower["kappa"] == Fraction(-2)
        assert tower["genus_tower"][1] == Fraction(-1, 12)
        assert tower["costello_computes_this"] is False

    def test_d3_genus_tower(self):
        """D3 brane (gl_2, k=1): kappa = 13/4, F_1 = 13/96."""
        kap = kappa_glN(2, Fraction(1))
        assert kap == Fraction(13, 4)
        tower = genus_tower_extension("D3_gl2", kap)
        assert tower["genus_tower"][1] == Fraction(13, 96)

    def test_virasoro_genus_tower(self):
        """Virasoro c=26: kappa = 13, F_1 = 13/24."""
        kap = kappa_virasoro(Fraction(26))
        tower = genus_tower_extension("Vir_26", kap)
        assert tower["genus_tower"][1] == Fraction(13, 24)

    def test_heisenberg_genus_tower(self):
        """Heisenberg k=1: kappa = 1, F_1 = 1/24."""
        kap = kappa_heisenberg(Fraction(1))
        tower = genus_tower_extension("H_1", kap)
        assert tower["genus_tower"][1] == Fraction(1, 24)

    def test_genus_tower_costello_flag(self):
        """All genus towers are flagged as NOT computed by Costello."""
        for name, kap in [("test1", Fraction(1)), ("test2", Fraction(-5))]:
            tower = genus_tower_extension(name, kap)
            assert tower["costello_computes_this"] is False

    def test_genus_tower_f_g_nonzero_when_kappa_nonzero(self):
        """F_g != 0 for all g when kappa != 0."""
        kap = Fraction(3)
        tower = genus_tower_extension("test", kap, g_max=8)
        for g in range(1, 9):
            assert tower["genus_tower"][g] != 0

    def test_genus_tower_f_g_zero_when_kappa_zero(self):
        """F_g = 0 for all g when kappa = 0 (uncurved bar complex)."""
        kap = Fraction(0)
        tower = genus_tower_extension("test", kap, g_max=5)
        for g in range(1, 6):
            assert tower["genus_tower"][g] == 0


# ===========================================================================
# 6. Kappa cross-checks
# ===========================================================================

class TestKappaCrossChecks:
    """Multi-path kappa verification (AP1, AP10, AP39, AP48)."""

    def test_kappa_km_formula(self):
        """kappa(g, k) = dim(g)(k+h^v)/(2h^v)."""
        # sl_2: dim=3, h^v=2
        assert kappa_km(3, 2, Fraction(1)) == Fraction(9, 4)
        # sl_3: dim=8, h^v=3
        assert kappa_km(8, 3, Fraction(1)) == Fraction(32, 6)

    def test_kappa_sl2_three_paths(self):
        """kappa(sl_2, k=1) by three methods.

        Path 1: dim(g)(k+h^v)/(2h^v) = 3*3/4 = 9/4.
        Path 2: gl_2 minus u(1): 13/4 - 1 = 9/4.
        Path 3: FF: -kappa(sl_2, -5) = -(-9/4) = 9/4.
        """
        p1 = Fraction(3) * Fraction(3) / Fraction(4)
        p2 = kappa_glN(2, Fraction(1)) - kappa_heisenberg(Fraction(1))
        p3 = -kappa_slN(2, Fraction(-5))
        assert p1 == p2 == p3 == Fraction(9, 4)

    def test_kappa_not_c_over_2_for_km(self):
        """AP39: kappa != c/2 for affine KM at rank > 1.

        sl_2, k=1: c = k*dim/(k+h^v) = 3/3 = 1. c/2 = 1/2. kappa = 9/4.
        """
        c_sl2 = Fraction(1) * Fraction(3) / (Fraction(1) + Fraction(2))
        assert c_sl2 == Fraction(1)
        assert kappa_slN(2, Fraction(1)) != c_sl2 / 2

    def test_kappa_equals_c_over_2_for_virasoro(self):
        """AP39 safe case: kappa = c/2 for Virasoro."""
        for c in [0, 1, 13, 25, 26]:
            assert kappa_virasoro(Fraction(c)) == Fraction(c, 2)

    def test_betagamma_kappa_weight_symmetry(self):
        """kappa(bg_lambda) = kappa(bg_{1-lambda})."""
        for n in range(20):
            lam = Fraction(n, 4)
            assert kappa_betagamma(lam) == kappa_betagamma(1 - lam)

    def test_betagamma_bc_complementarity(self):
        """AP24: kappa(bg) + kappa(bc) = 0 (free field)."""
        for n in range(20):
            lam = Fraction(n, 8)
            assert kappa_betagamma(lam) + kappa_bc(lam) == 0

    def test_slN_feigin_frenkel_complementarity(self):
        """AP24: kappa(sl_N, k) + kappa(sl_N, -k-2N) = 0."""
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3]:
                kf = Fraction(k)
                kap = kappa_slN(N, kf)
                kap_dual = kappa_slN(N, -kf - 2 * N)
                assert kap + kap_dual == 0

    def test_virasoro_complementarity_nonzero(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT zero)."""
        for c in [0, 1, 13, 25, 26]:
            s = kappa_virasoro(Fraction(c)) + kappa_virasoro(Fraction(26 - c))
            assert s == 13


# ===========================================================================
# 7. Collision residue AP19
# ===========================================================================

class TestCollisionResidue:
    """AP19: d log absorption reduces pole order by 1."""

    def test_heisenberg_r_matrix_pole(self):
        """Heisenberg: OPE double pole -> r(z) simple pole."""
        result = collision_residue_pole_check(2)
        assert result["r_matrix_pole"] == 1

    def test_virasoro_r_matrix_pole(self):
        """Virasoro: OPE quartic pole -> r(z) cubic pole."""
        result = collision_residue_pole_check(4)
        assert result["r_matrix_pole"] == 3

    def test_betagamma_r_matrix_regular(self):
        """bg: OPE simple pole -> r(z) regular (pole 0)."""
        result = collision_residue_pole_check(1)
        assert result["r_matrix_pole"] == 0

    def test_w3_r_matrix_pole(self):
        """W_3: OPE sextic pole -> r(z) quintic pole."""
        result = collision_residue_pole_check(6)
        assert result["r_matrix_pole"] == 5

    def test_no_negative_poles(self):
        """OPE pole 0 (no singularity) -> r(z) pole 0."""
        result = collision_residue_pole_check(0)
        assert result["r_matrix_pole"] == 0


# ===========================================================================
# 8. Master synthesis consistency
# ===========================================================================

class TestMasterSynthesis:
    """Test the unified synthesis for internal consistency."""

    def test_synthesis_has_three_questions(self):
        """Synthesis answers all three main questions."""
        s = full_synthesis()
        assert "Q1_theorem_a_vs_costello" in s
        assert "Q2_four_layers" in s
        assert "Q3_holography_equals_koszul" in s

    def test_q1_has_agreement_and_divergence(self):
        """Q1 identifies where they agree AND where they diverge."""
        q1 = full_synthesis()["Q1_theorem_a_vs_costello"]
        # The agreement text describes matching output at genus 0
        assert "same" in q1["where_they_agree"].lower()
        assert len(q1["where_they_diverge"]) > 100  # substantive

    def test_q2_has_all_four_layers(self):
        """Q2 covers all four Costello layers."""
        q2 = full_synthesis()["Q2_four_layers"]
        assert len(q2) == 4

    def test_q3_has_proved_and_conjectural(self):
        """Q3 separates proved from conjectural components."""
        q3 = full_synthesis()["Q3_holography_equals_koszul"]
        assert len(q3["proved_components"]) >= 5
        assert len(q3["conjectural_components"]) >= 4

    def test_synthesis_complementary(self):
        """Synthesis concludes programmes are COMPLEMENTARY."""
        s = full_synthesis()
        assert "COMPLEMENTARY" in s["agent_synthesis"]["complementary_not_competing"]

    def test_synthesis_four_dualities_distinct(self):
        """Synthesis states four dualities are DISTINCT."""
        s = full_synthesis()
        assert "DISTINCT" in s["agent_synthesis"]["four_dualities_are_distinct"].upper()


# ===========================================================================
# 9. Uncited papers
# ===========================================================================

class TestUncitedPapers:
    """Papers from Costello's programme we should cite."""

    def test_uncited_papers_nonempty(self):
        """There are uncited papers to address."""
        papers = uncited_costello_papers()
        assert len(papers) >= 4

    def test_uncited_papers_have_arxiv_ids(self):
        """Each uncited paper has an arXiv identifier."""
        for paper in uncited_costello_papers():
            assert paper["arxiv"]
            assert len(paper["arxiv"]) >= 7  # e.g., "1705.02500"

    def test_uncited_papers_have_relevance(self):
        """Each uncited paper explains its relevance."""
        for paper in uncited_costello_papers():
            assert len(paper["relevance"]) >= 20


# ===========================================================================
# 10. AP50 compliance: A^!_infty != A^!
# ===========================================================================

class TestAP50Compliance:
    """AP50: A^!_infty (homotopy) != A^! (strict); compatibility is Theorem A."""

    def test_layer3_mentions_ap50(self):
        """Layer 3 (M2 holography) properly distinguishes A^!_infty from A^!."""
        layer = layer3_m2_holography()
        assert "AP50" in layer.theorem_a_covers

    def test_chiral_kd_mentions_verdier(self):
        """Chiral KD comparison mentions Verdier intertwining."""
        comp = chiral_koszul_comparison()
        assert "Verdier" in comp.definition

    def test_layer1_bar_coalgebra_not_algebra(self):
        """Layer 1 correctly states bar complex is COALGEBRA (AP25)."""
        layer = layer1_cg_bv()
        assert "coalgebra" in layer.our_identification.lower() or \
               "bar complex" in layer.our_identification.lower()


# ===========================================================================
# 11. Cross-layer consistency
# ===========================================================================

class TestCrossLayerConsistency:
    """Verify consistency across layers and dualities."""

    def test_genus_0_agreement_across_all_layers(self):
        """At genus 0, all layers agree (Agent 2 finding)."""
        # Layer 1: BV = bar at genus 0
        l1 = layer1_cg_bv()
        assert "genus 0" in l1.proved_vs_conjectural.lower()
        # Layer 2: R-matrix match at genus 0
        l2 = layer2_cwy()
        assert "r(z)" in l2.our_identification.lower() or \
               "collision" in l2.our_identification.lower()

    def test_our_theorem_a_universal(self):
        """Our Theorem A is ALGEBRAIC: applies to all systems."""
        for status_fn in [holography_status_m2, holography_status_d3,
                          holography_status_ads3, holography_status_celestial]:
            assert status_fn().our_theorem_a_applies is True

    def test_costello_kd_only_proved_for_m2(self):
        """Among brane systems, only M2 has proved KD (Costello side)."""
        assert holography_status_m2().koszul_duality_proved is True
        assert holography_status_d3().koszul_duality_proved is False
        assert holography_status_ads3().koszul_duality_proved is False
        assert holography_status_celestial().koszul_duality_proved is False

    def test_s_duality_not_in_costello_layers(self):
        """S-duality is NOT one of Costello's four KD layers."""
        layer_names = [l.value for l in CostelloLayer]
        assert not any("S-duality" in name for name in layer_names)

    def test_mirror_not_in_costello_layers(self):
        """3d mirror symmetry is NOT one of Costello's four KD layers."""
        layer_names = [l.value for l in CostelloLayer]
        assert not any("mirror" in name.lower() for name in layer_names)


# ===========================================================================
# 12. Multi-path cross-checks (AP10 compliance)
# ===========================================================================

class TestMultiPathCrossChecks:
    """Cross-checks verifying key claims by structurally independent paths.

    AP10: hardcoded single-family tests are necessary but NOT sufficient.
    These tests verify the SAME quantity via genuinely different methods.
    """

    def test_kd_s_duality_coincidence_three_paths(self):
        """KD = S-duality at k=-1 for sl_2, verified three ways.

        Path 1: KD level = -(-1)-4 = -3; S-level = -(2(-1)+5)/(-1+2) = -3.
        Path 2: kappa_slN(2, -1) + kappa_slN(2, -3) = 0 (FF complementarity).
        Path 3: The coincidence locus function returns -1 as a coincidence.
        """
        # Path 1: direct level computation
        result = koszul_vs_s_duality_sl2(Fraction(-1))
        assert result["koszul_dual_level"] == Fraction(-3)
        assert result["s_dual_level"] == Fraction(-3)
        # Path 2: FF complementarity holds at both matched levels
        assert kappa_slN(2, Fraction(-1)) + kappa_slN(2, Fraction(-3)) == 0
        # Path 3: coincidence locus function
        locus = koszul_vs_s_duality_coincidence_locus()
        assert -1 in locus["coincidence_levels"]

    def test_genus_tower_additivity_cross_check(self):
        """F_g for gl_N = F_g for sl_N + F_g for u(1) (additivity).

        This cross-checks the genus tower against the additivity of kappa
        (prop:independent-sum-factorization) by an independent path.
        """
        for N in [2, 3, 4]:
            k = Fraction(1)
            kap_gl = kappa_glN(N, k)
            kap_sl = kappa_slN(N, k)
            kap_u1 = kappa_heisenberg(k)
            for g in range(1, 5):
                F_gl = kap_gl * _lambda_fp(g)
                F_sl = kap_sl * _lambda_fp(g)
                F_u1 = kap_u1 * _lambda_fp(g)
                assert F_gl == F_sl + F_u1, (
                    f"Genus tower additivity fails for gl_{N}, g={g}: "
                    f"{F_gl} != {F_sl} + {F_u1}"
                )

    def test_complementarity_vs_genus_tower_cross_check(self):
        """F_g(A) + F_g(A!) = 0 for KM (complementarity + genus tower).

        Path 1: kappa + kappa' = 0 => F_g + F_g' = 0.
        Path 2: compute F_g and F_g' independently and add.
        """
        for N in [2, 3]:
            k = Fraction(1)
            kap = kappa_slN(N, k)
            kap_dual = kappa_slN(N, -k - 2 * N)
            for g in range(1, 5):
                F_g = kap * _lambda_fp(g)
                F_g_dual = kap_dual * _lambda_fp(g)
                assert F_g + F_g_dual == 0, (
                    f"Complementarity genus tower fails for sl_{N}, g={g}"
                )

    def test_collision_residue_cross_check_virasoro(self):
        """Virasoro r-matrix pole order by two paths.

        Path 1: AP19 formula: max_ope_pole - 1 = 4 - 1 = 3.
        Path 2: The d log kernel d log(z-w) has weight 1; the OPE
                T(z)T(w) ~ c/2 (z-w)^{-4} + ... has max pole 4.
                After d log absorption: (z-w)^{-4} * (z-w) = (z-w)^{-3}.
                So the leading r-matrix pole is z^{-3}. Pole order = 3.
        """
        # Path 1
        result = collision_residue_pole_check(4)
        assert result["r_matrix_pole"] == 3
        # Path 2: direct pole arithmetic
        ope_leading_pole = 4
        dlog_absorption = 1
        r_matrix_leading_pole = ope_leading_pole - dlog_absorption
        assert r_matrix_leading_pole == 3
        # Cross-check
        assert result["r_matrix_pole"] == r_matrix_leading_pole

    def test_kappa_glN_three_independent_paths(self):
        """kappa(gl_N, k) by three independent formulae for N=3, k=2.

        Path 1: kappa(sl_3, 2) + kappa(u(1), 2) = 8*(2+3)/6 + 2 = 40/6+2 = 52/6.
        Path 2: kappa_glN direct = kappa_km(8, 3, 2) + 2.
        Path 3: Complementarity: -kappa_dual, where dual = sl_3 at -8 + u(1) at -2.
        """
        N, k = 3, Fraction(2)
        # Path 1
        p1 = kappa_slN(N, k) + kappa_heisenberg(k)
        # Path 2
        p2 = kappa_glN(N, k)
        # Path 3
        kap_sl_dual = kappa_slN(N, -k - 2 * N)
        kap_u1_dual = kappa_heisenberg(-k)
        p3 = -(kap_sl_dual + kap_u1_dual)
        assert p1 == p2 == p3

    def test_s_duality_self_consistency(self):
        """S-duality is an involution: applying it twice returns to k.

        For sl_2: S sends k to k' = -(2k+5)/(k+2).
        Applying again: k'' = -(2k'+5)/(k'+2) = k.
        Verify numerically.
        """
        for k_num in [1, 3, 5, 7]:
            k = Fraction(k_num)
            h_v = 2
            psi = k + h_v
            # First application
            psi_s = -Fraction(1) / psi
            k_s = psi_s - h_v
            # Second application
            psi_ss = -Fraction(1) / (k_s + h_v)
            k_ss = psi_ss - h_v
            assert k_ss == k, f"S-duality is not involutive at k={k}: k'' = {k_ss}"

    def test_kd_involution_cross_check(self):
        """Koszul duality (FF) is an involution: (A!)! = A.

        For sl_N: k -> -k-2N -> -(-k-2N)-2N = k. Verify via kappa.
        """
        for N in [2, 3, 4]:
            for k_num in [1, 2, 3]:
                k = Fraction(k_num)
                kap = kappa_slN(N, k)
                k_dual = -k - 2 * N
                kap_dual = kappa_slN(N, k_dual)
                k_double_dual = -k_dual - 2 * N
                kap_double_dual = kappa_slN(N, k_double_dual)
                assert k_double_dual == k
                assert kap_double_dual == kap

    def test_virasoro_kd_not_involutive_at_c_neq_13(self):
        """Virasoro KD: c -> 26-c. Not involutive (except c=13).

        (26-c) -> 26-(26-c) = c. Actually it IS involutive for Virasoro!
        But kappa + kappa' = 13 != 0 (AP24). Verify both facts.
        """
        for c_num in [0, 1, 10, 25, 26]:
            c = Fraction(c_num)
            c_dual = 26 - c
            c_double_dual = 26 - c_dual
            assert c_double_dual == c  # involutive
            kap = kappa_virasoro(c)
            kap_dual = kappa_virasoro(c_dual)
            assert kap + kap_dual == 13  # but sum != 0 (AP24)
