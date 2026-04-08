r"""Tests for the 12-fold Koszulness programme rectification engine.

Verifies ALL 12 items (i)-(xii) of thm:koszul-equivalences-meta plus
K13 (E_3-formality) and K14 (deformation rigidity) candidates, against
the 2024-2026 literature:

  Holstein-Rivera (2410.03604): K11 (P3) redundancy
  Balduf-Gaiotto (2408.03192): non-renormalization = formality bridge
  Gaiotto-Khan (2309.12103): pentagon = PBW Koszul duality
  De Leger (2512.20167): E_3-action on ChirHoch (K13 candidate)
  Linshaw-Qi (2601.12017): deformation rigidity (K14 candidate)
  Heuts (2408.06173): maximal scope of operadic Koszul duality
  Creutzig (2603.04667): KL braided tensor equivalence

Manuscript references:
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  prop:lagrangian-perfectness (bar_cobar_adjunction_inversion.tex)
  cor:lagrangian-unconditional (bar_cobar_adjunction_inversion.tex)
  rem:d-module-purity-content (chiral_koszul_pairs.tex)
  sec:concordance-koszulness-programme (concordance.tex)
"""

import pytest

from compute.lib.theorem_koszul_12fold_rectification_engine import (
    KOSZUL_ITEMS,
    FAMILIES,
    KoszulItem,
    FamilyData,
    verify_item_status,
    count_unconditional,
    count_conditional,
    count_one_directional,
    count_false_candidates,
    verify_item_for_family,
    k11_upgrade_analysis,
    k13_e3_formality_analysis,
    k14_rigidity_analysis,
    dmod_purity_converse_assessment,
    heuts_scope_analysis,
    creutzig_kl_impact,
    full_rectification_summary,
    verify_proof_circuit,
    balduf_gaiotto_bridge,
    landscape_koszulness_table,
)


# =========================================================================
# Section 1: ITEM COUNTS (matches concordance + meta-theorem)
# =========================================================================

class TestItemCounts:
    """Verify the item counts match the meta-theorem statement."""

    def test_total_items_14(self):
        """12 meta-theorem items + 2 candidates = 14 total."""
        assert len(KOSZUL_ITEMS) == 14

    def test_unconditional_10(self):
        """Items (i)-(x) are unconditional equivalences."""
        assert count_unconditional() == 10

    def test_conditional_1(self):
        """Item (xi) is conditional on perfectness."""
        assert count_conditional() == 1

    def test_one_directional_1(self):
        """Item (xii) is one-directional (forward proved, converse open)."""
        assert count_one_directional() == 1

    def test_false_candidates_2(self):
        """K13 and K14 are both false as biconditional equivalences."""
        assert count_false_candidates() == 2

    def test_registry_complete(self):
        """All 12 items plus K13, K14 are in the registry."""
        expected = [
            '(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)',
            '(vii)', '(viii)', '(ix)', '(x)', '(xi)', '(xii)',
            'K13', 'K14',
        ]
        for item_num in expected:
            assert item_num in KOSZUL_ITEMS, f'{item_num} missing'


# =========================================================================
# Section 2: INDIVIDUAL ITEM VERIFICATION
# =========================================================================

class TestUnconditionalItems:
    """Verify each of the 10 unconditional equivalences."""

    @pytest.mark.parametrize("item_num", [
        '(i)', '(ii)', '(iii)', '(iv)', '(v)',
        '(vi)', '(vii)', '(viii)', '(ix)', '(x)',
    ])
    def test_unconditional_status(self, item_num):
        """Each of (i)-(x) has status 'unconditional'."""
        result = verify_item_status(item_num)
        assert result['status'] == 'unconditional'
        assert result['verified']

    @pytest.mark.parametrize("item_num", [
        '(i)', '(ii)', '(iii)', '(iv)', '(v)',
        '(vi)', '(vii)', '(viii)', '(ix)', '(x)',
    ])
    def test_both_directions_proved(self, item_num):
        """Each unconditional item has both directions proved."""
        result = verify_item_status(item_num)
        assert result['proof_direction'] == 'both'

    @pytest.mark.parametrize("item_num", [
        '(i)', '(ii)', '(iii)', '(iv)', '(v)',
        '(vi)', '(vii)', '(viii)', '(ix)', '(x)',
    ])
    def test_not_upgraded(self, item_num):
        """Items (i)-(x) are NOT upgraded by 2024-2026 papers."""
        result = verify_item_status(item_num)
        assert not result['upgraded']

    def test_item_i_name(self):
        """Item (i) is 'Chirally Koszul'."""
        assert KOSZUL_ITEMS['(i)'].name == 'Chirally Koszul'

    def test_item_ii_name(self):
        """Item (ii) is PBW E_2-collapse."""
        assert 'PBW' in KOSZUL_ITEMS['(ii)'].name

    def test_item_iii_name(self):
        """Item (iii) is A_infty formality."""
        assert 'A_infty' in KOSZUL_ITEMS['(iii)'].name

    def test_item_viii_name(self):
        """Item (viii) is ChirHoch polynomial."""
        assert 'ChirHoch' in KOSZUL_ITEMS['(viii)'].name


class TestConditionalItems:
    """Verify conditional / partial items."""

    def test_xi_conditional(self):
        """Item (xi) has status 'conditional'."""
        result = verify_item_status('(xi)')
        assert result['status'] == 'conditional'

    def test_xi_upgraded(self):
        """Item (xi) IS upgraded by Holstein-Rivera."""
        result = verify_item_status('(xi)')
        assert result['upgraded']

    def test_xi_has_condition(self):
        """Item (xi) specifies the perfectness condition."""
        result = verify_item_status('(xi)')
        assert 'P1' in result['condition'] or 'perfectness' in result['condition'].lower()

    def test_xii_one_directional(self):
        """Item (xii) has status 'one-directional'."""
        result = verify_item_status('(xii)')
        assert result['status'] == 'one-directional'

    def test_xii_forward_only(self):
        """Item (xii) has proof_direction 'forward_only'."""
        result = verify_item_status('(xii)')
        assert result['proof_direction'] == 'forward_only'

    def test_xii_not_upgraded(self):
        """Item (xii) is NOT upgraded by 2024-2026 papers."""
        result = verify_item_status('(xii)')
        assert not result['upgraded']


class TestFalseCandidates:
    """Verify K13 and K14 are correctly identified as false."""

    def test_k13_false(self):
        """K13 (E_3-formality) is FALSE as biconditional."""
        result = verify_item_status('K13')
        assert result['status'] == 'false'

    def test_k14_false(self):
        """K14 (deformation rigidity) is FALSE as biconditional."""
        result = verify_item_status('K14')
        assert result['status'] == 'false'


# =========================================================================
# Section 3: K11 UPGRADE (Holstein-Rivera)
# =========================================================================

class TestK11Upgrade:
    """Verify the K11 upgrade from Holstein-Rivera (2410.03604)."""

    def test_heisenberg_p3_redundant(self):
        """(P3) is redundant for Heisenberg on the Koszul locus."""
        result = k11_upgrade_analysis('heisenberg')
        assert result['p3_redundant']

    def test_virasoro_p3_redundant(self):
        """(P3) is redundant for Virasoro on the Koszul locus."""
        result = k11_upgrade_analysis('virasoro')
        assert result['p3_redundant']

    def test_affine_p3_redundant(self):
        """(P3) is redundant for affine sl_2 on the Koszul locus."""
        result = k11_upgrade_analysis('affine_sl2')
        assert result['p3_redundant']

    def test_betagamma_p3_redundant(self):
        """(P3) is redundant for beta-gamma on the Koszul locus."""
        result = k11_upgrade_analysis('betagamma')
        assert result['p3_redundant']

    def test_w3_p3_redundant(self):
        """(P3) is redundant for W_3 on the Koszul locus."""
        result = k11_upgrade_analysis('w3')
        assert result['p3_redundant']

    def test_k11_unconditional_for_standard_landscape(self):
        """K11 is unconditional for all standard families with (P1)+(P2)."""
        for name, fam in FAMILIES.items():
            if fam.has_nondeg_form and fam.finite_weight_spaces and fam.koszul:
                result = k11_upgrade_analysis(name)
                assert result['k11_unconditional'], (
                    f'K11 should be unconditional for {name}'
                )

    def test_ising_not_p3_redundant(self):
        """Ising is NOT Koszul, so P3 redundancy doesn't apply."""
        result = k11_upgrade_analysis('ising')
        # Ising is not Koszul, so P3 redundancy on Koszul locus is vacuous
        assert not result['p3_redundant']

    def test_holstein_rivera_mechanism(self):
        """The mechanism cites Holstein-Rivera explicitly."""
        result = k11_upgrade_analysis('heisenberg')
        assert 'Holstein-Rivera' in result['holstein_rivera']


# =========================================================================
# Section 4: K13 ANALYSIS (De Leger E_3-formality)
# =========================================================================

class TestK13Analysis:
    """Verify K13 (E_3-formality <=> Koszulness) is FALSE."""

    def test_not_biconditional(self):
        """K13 is NOT a biconditional equivalence."""
        result = k13_e3_formality_analysis()
        assert not result['biconditional']

    def test_forward_direction_true(self):
        """E_3-formality => Koszulness is TRUE."""
        result = k13_e3_formality_analysis()
        assert result['forward']

    def test_backward_direction_false(self):
        """Koszulness => E_3-formality is FALSE."""
        result = k13_e3_formality_analysis()
        assert not result['backward']

    def test_counterexample_is_class_m(self):
        """The counterexample to the backward direction is a class-M algebra."""
        result = k13_e3_formality_analysis()
        assert result['counterexample_backward'] is not None
        # The counterexample should be a Koszul + non-e3-formal algebra (class M)
        fam = FAMILIES[result['counterexample_backward']]
        assert fam.koszul and not fam.e3_formal

    def test_ap14_cited(self):
        """The mechanism cites AP14 (Koszulness != SC formality)."""
        result = k13_e3_formality_analysis()
        assert 'AP14' in result['mechanism']

    def test_class_m_is_counterexample(self):
        """Class M algebras are Koszul but not E_3-formal."""
        for name, fam in FAMILIES.items():
            if fam.shadow_class == 'M' and fam.koszul:
                assert not fam.e3_formal, (
                    f'{name} is class M + Koszul but marked e3_formal'
                )

    def test_class_g_is_e3_formal(self):
        """Class G algebras are both Koszul and E_3-formal."""
        for name, fam in FAMILIES.items():
            if fam.shadow_class == 'G' and fam.koszul:
                assert fam.e3_formal, (
                    f'{name} is class G + Koszul but NOT e3_formal'
                )


# =========================================================================
# Section 5: K14 ANALYSIS (Linshaw-Qi rigidity)
# =========================================================================

class TestK14Analysis:
    """Verify K14 (deformation rigidity <=> Koszulness) is FALSE."""

    def test_not_biconditional(self):
        """K14 is NOT a biconditional equivalence."""
        result = k14_rigidity_analysis()
        assert not result['biconditional']

    def test_independent(self):
        """Rigidity and Koszulness are independent properties."""
        result = k14_rigidity_analysis()
        assert result['independent']

    def test_koszul_nonrigid_examples_exist(self):
        """There exist Koszul + non-rigid examples."""
        result = k14_rigidity_analysis()
        assert len(result['koszul_nonrigid']) > 0

    def test_heisenberg_koszul_nonrigid(self):
        """Heisenberg is Koszul and non-rigid."""
        fam = FAMILIES['heisenberg']
        assert fam.koszul
        assert not fam.rigid

    def test_universal_affine_koszul_nonrigid(self):
        """V_k(sl_2) universal is Koszul and non-rigid."""
        fam = FAMILIES['affine_sl2']
        assert fam.koszul
        assert not fam.rigid

    def test_ising_nonkoszul_rigid(self):
        """Ising is non-Koszul and rigid."""
        fam = FAMILIES['ising']
        assert not fam.koszul
        assert fam.rigid


# =========================================================================
# Section 6: D-MODULE PURITY CONVERSE (Gaiotto-Khan)
# =========================================================================

class TestDmodPurityConverse:
    """Verify Gaiotto-Khan does NOT give the D-module purity converse."""

    def test_gk_does_not_give_converse(self):
        """Gaiotto-Khan does NOT give the converse of (xii)."""
        result = dmod_purity_converse_assessment()
        assert not result['gk_gives_converse']

    def test_remaining_gap(self):
        """The remaining gap is PBW = Saito for Virasoro/W-algebras."""
        result = dmod_purity_converse_assessment()
        assert 'Saito' in result['remaining_gap']
        assert 'Virasoro' in result['remaining_gap'] or 'W-algebra' in result['remaining_gap']

    def test_proved_for_affine_km(self):
        """Converse IS proved for affine Kac-Moody."""
        result = dmod_purity_converse_assessment()
        assert 'affine' in result['proved_for'].lower() or 'Kac-Moody' in result['proved_for']

    def test_zero_counterexamples(self):
        """Zero counterexamples to the converse have been found."""
        result = dmod_purity_converse_assessment()
        assert result['zero_counterexamples']


# =========================================================================
# Section 7: HEUTS SCOPE ANALYSIS
# =========================================================================

class TestHeutsScope:
    """Verify the monograph is safe from Heuts' disproof."""

    def test_monograph_safe(self):
        """The monograph is safe from Heuts' result."""
        result = heuts_scope_analysis()
        assert result['monograph_safe']

    def test_no_items_affected(self):
        """No items are affected by Heuts' result."""
        result = heuts_scope_analysis()
        assert len(result['items_affected']) == 0

    def test_three_safety_reasons(self):
        """Three independent safety reasons are documented."""
        result = heuts_scope_analysis()
        assert len(result['safety_reasons']) == 3


# =========================================================================
# Section 8: CREUTZIG KL-EQUIVALENCE
# =========================================================================

class TestCreutzigKL:
    """Verify Creutzig (2603.04667) impact assessment."""

    def test_no_new_equivalences(self):
        """Creutzig gives zero new equivalences."""
        result = creutzig_kl_impact()
        assert result['new_equivalences'] == 0

    def test_landscape_extension(self):
        """Creutzig extends the landscape, not the equivalences."""
        result = creutzig_kl_impact()
        assert result['landscape_extension']


# =========================================================================
# Section 9: PROOF CIRCUIT VERIFICATION
# =========================================================================

class TestProofCircuit:
    """Verify the logical circuit of the meta-theorem proof."""

    def test_core_circuit_complete(self):
        """The core circuit (i)-(ii)-(iii)-(v)-(viii) is complete."""
        result = verify_proof_circuit()
        assert result['core_circuit_complete']

    def test_all_equivalences_proved(self):
        """All 12 items are covered by the proof circuit."""
        result = verify_proof_circuit()
        assert result['all_equivalences_proved']

    def test_no_missing_items(self):
        """No items are missing from the proof circuit."""
        result = verify_proof_circuit()
        assert len(result['missing_items']) == 0


# =========================================================================
# Section 10: BALDUF-GAIOTTO BRIDGE
# =========================================================================

class TestBaldufGaiottoBridge:
    """Verify the Balduf-Gaiotto non-renormalization bridge."""

    def test_no_new_equivalence(self):
        """Balduf-Gaiotto does NOT give a new equivalence."""
        result = balduf_gaiotto_bridge()
        assert not result['new_equivalence']

    def test_compatible_with_iii(self):
        """Balduf-Gaiotto is compatible with item (iii)."""
        result = balduf_gaiotto_bridge()
        assert result['compatible_with_iii']

    def test_distinct_from_iii(self):
        """BG statement is distinct from item (iii) statement."""
        result = balduf_gaiotto_bridge()
        assert result['distinction']['bg_statement'] != result['distinction']['item_iii_statement']

    def test_class_m_not_directly_applicable(self):
        """BG does not directly apply to class M."""
        result = balduf_gaiotto_bridge()
        assert 'NOT' in result['class_compatibility']['M']


# =========================================================================
# Section 11: LANDSCAPE CROSS-CHECKS
# =========================================================================

class TestLandscapeCrossChecks:
    """Cross-family consistency checks across the landscape."""

    def test_landscape_table_consistent(self):
        """All families in the landscape table are consistent."""
        table = landscape_koszulness_table()
        for row in table:
            assert row['consistent'], (
                f"Inconsistency in {row['family']}: {row.get('issue', '')}"
            )

    def test_all_families_present(self):
        """The landscape table covers all registered families."""
        table = landscape_koszulness_table()
        assert len(table) == len(FAMILIES)

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro',
    ])
    def test_archetype_koszul(self, family):
        """Each archetype family is chirally Koszul."""
        assert FAMILIES[family].koszul

    def test_ising_not_koszul(self):
        """Ising minimal model is proved NOT chirally Koszul."""
        assert not FAMILIES['ising'].koszul

    def test_e3_formal_implies_koszul(self):
        """e3-formal => Koszul for all families (forward of K13)."""
        for name, fam in FAMILIES.items():
            if fam.e3_formal:
                assert fam.koszul, (
                    f'{name} is e3-formal but NOT Koszul'
                )

    def test_sc_formal_implies_e3_formal(self):
        """SC-formal => e3-formal for all families."""
        for name, fam in FAMILIES.items():
            if fam.sc_formal:
                assert fam.e3_formal, (
                    f'{name} is SC-formal but NOT e3-formal'
                )

    def test_koszul_not_implies_sc_formal(self):
        """There exist Koszul algebras that are NOT SC-formal."""
        koszul_not_sc = [
            name for name, fam in FAMILIES.items()
            if fam.koszul and not fam.sc_formal
        ]
        assert len(koszul_not_sc) > 0, (
            'Expected at least one Koszul + non-SC-formal example'
        )

    def test_virasoro_koszul_not_sc_formal(self):
        """Virasoro is Koszul but NOT SC-formal (AP14)."""
        fam = FAMILIES['virasoro']
        assert fam.koszul
        assert not fam.sc_formal

    def test_shadow_classes_all_koszul(self):
        """All four shadow classes contain Koszul algebras."""
        classes = {'G', 'L', 'C', 'M'}
        koszul_classes = set()
        for fam in FAMILIES.values():
            if fam.koszul:
                koszul_classes.add(fam.shadow_class)
        assert classes.issubset(koszul_classes), (
            f'Missing Koszul examples for classes: {classes - koszul_classes}'
        )


# =========================================================================
# Section 12: ITEM-FAMILY CROSS-CHECKS
# =========================================================================

class TestItemFamilyCrossChecks:
    """Verify each item against each family for consistency."""

    @pytest.mark.parametrize("item_num", [
        '(i)', '(ii)', '(iii)', '(iv)', '(v)',
        '(vi)', '(vii)', '(viii)', '(ix)', '(x)',
    ])
    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro',
    ])
    def test_unconditional_item_consistent_with_koszul_family(
        self, item_num, family
    ):
        """For Koszul families, all unconditional items hold."""
        result = verify_item_for_family(item_num, family)
        assert result['consistent']
        assert result['item_holds']

    @pytest.mark.parametrize("item_num", [
        '(i)', '(ii)', '(iii)', '(iv)', '(v)',
        '(vi)', '(vii)', '(viii)', '(ix)', '(x)',
    ])
    def test_unconditional_item_fails_for_ising(self, item_num):
        """For non-Koszul Ising, all unconditional items fail."""
        result = verify_item_for_family(item_num, 'ising')
        assert result['consistent']
        assert not result['item_holds']


# =========================================================================
# Section 13: FULL RECTIFICATION SUMMARY
# =========================================================================

class TestFullSummary:
    """Verify the complete rectification summary."""

    def test_total_14(self):
        """Total items is 14."""
        summary = full_rectification_summary()
        assert summary['total_items'] == 14

    def test_unconditional_10(self):
        summary = full_rectification_summary()
        assert summary['unconditional'] == 10

    def test_conditional_1(self):
        summary = full_rectification_summary()
        assert summary['conditional'] == 1

    def test_one_directional_1(self):
        summary = full_rectification_summary()
        assert summary['one_directional'] == 1

    def test_false_candidates_2(self):
        summary = full_rectification_summary()
        assert summary['false_candidates'] == 2

    def test_upgraded_items_xi_only(self):
        """Only item (xi) was upgraded."""
        summary = full_rectification_summary()
        assert summary['upgraded_items'] == ['(xi)']

    def test_dmod_converse_unchanged(self):
        """D-module purity converse is unchanged."""
        summary = full_rectification_summary()
        assert 'UNCHANGED' in summary['dmod_converse_status']

    def test_heuts_safe(self):
        """Heuts assessment says monograph is safe."""
        summary = full_rectification_summary()
        assert 'SAFE' in summary['heuts_status']
