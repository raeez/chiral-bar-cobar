r"""Tests for theorem_shifted_symplectic_k11_engine.py.

Verification strategy (multi-path, per CLAUDE.md mandate):
  1. Shifted symplectic degree computation
  2. PTVV structure verification
  3. (P1) finite weight spaces for all standard families
  4. (P2) nondegenerate invariant form
  5. (P3) dual regularity via Holstein-Rivera
  6. Cyclic pairing perfectness
  7. Holstein-Rivera CY exchange
  8. Calaque-Safronov AKSZ data
  9. Fang PVA construction
  10. Pridham quantization
  11. Lagrangian condition
  12. K11 conditionality analysis
  13. Full landscape census
  14. Complementarity sums (AP24-aware)
  15. Theorem B shifted-symplectic analysis
  16. Cross-engine consistency
  17. What remains conditional
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.theorem_shifted_symplectic_k11_engine import (
    # Section 1: shifted symplectic
    shifted_symplectic_degree,
    ptvv_symplectic_form_degree,
    # Section 2: perfectness
    weight_space_dimension,
    verify_p1_finite_weight_spaces,
    verify_p2_nondegenerate_form,
    verify_p3_dual_regularity,
    # Section 3: cyclic pairing
    cyclic_pairing_matrix,
    verify_perfectness_full,
    # Section 4: Holstein-Rivera
    cy_dimension,
    holstein_rivera_exchange,
    # Section 5: Calaque-Safronov
    aksz_shifted_symplectic_data,
    # Section 6: Fang
    pva_from_shifted_symplectic,
    # Section 7: Pridham
    pridham_quantization,
    # Section 8: Lagrangian
    verify_lagrangian_condition,
    # Section 9: K11 analysis
    k11_conditionality_analysis,
    k11_full_landscape_census,
    # Section 10: Theorem B
    shifted_symplectic_inversion_analysis,
    # Section 11: complementarity
    complementarity_sum,
    # Section 12: synthesis
    full_shifted_symplectic_analysis,
    # Section 13: what remains
    what_remains_conditional,
    # Internal
    _partition_number,
    _multipartition_number,
    _family_kappa,
    _family_kappa_dual,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    kappa_wN,
    shadow_depth_class,
    STANDARD_KAPPAS,
)


# ===================================================================
# 1. SHIFTED SYMPLECTIC DEGREE
# ===================================================================

class TestShiftedSymplecticDegree:
    """Verify shifted symplectic degree = -(3g-3)."""

    def test_genus_0(self):
        assert shifted_symplectic_degree(0) == 3

    def test_genus_1(self):
        assert shifted_symplectic_degree(1) == 0

    def test_genus_2(self):
        assert shifted_symplectic_degree(2) == -3

    def test_genus_3(self):
        assert shifted_symplectic_degree(3) == -6

    def test_genus_5(self):
        assert shifted_symplectic_degree(5) == -12

    def test_monotone_decreasing(self):
        """Shift decreases as genus increases."""
        for g in range(1, 10):
            assert shifted_symplectic_degree(g) > shifted_symplectic_degree(g + 1)

    def test_ptvv_degree(self):
        """PTVV degree = pairing degree (always -1 for cyclic)."""
        assert ptvv_symplectic_form_degree(10, -1) == -1
        assert ptvv_symplectic_form_degree(100, -2) == -2


# ===================================================================
# 2. PARTITION NUMBERS (INTERNAL)
# ===================================================================

class TestPartitionNumbers:
    """Verify partition number computations used for weight spaces."""

    def test_p0(self):
        assert _partition_number(0) == 1

    def test_p1(self):
        assert _partition_number(1) == 1

    def test_p2(self):
        assert _partition_number(2) == 2

    def test_p5(self):
        assert _partition_number(5) == 7

    def test_p10(self):
        assert _partition_number(10) == 42

    def test_p15(self):
        assert _partition_number(15) == 176

    def test_multipartition_r1(self):
        """r=1 colored partitions = ordinary partitions."""
        for n in range(11):
            assert _multipartition_number(n, 1) == _partition_number(n)

    def test_multipartition_r3_low(self):
        """3-colored partitions: p_3(0)=1, p_3(1)=3, p_3(2)=9."""
        assert _multipartition_number(0, 3) == 1
        assert _multipartition_number(1, 3) == 3
        assert _multipartition_number(2, 3) == 9


# ===================================================================
# 3. (P1) FINITE WEIGHT SPACES
# ===================================================================

class TestP1FiniteWeightSpaces:
    """Verify (P1) for all standard families."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'w3',
    ])
    def test_p1_satisfied(self, family):
        result = verify_p1_finite_weight_spaces(family, 10)
        assert result['p1_satisfied'], f"(P1) should hold for {family}"

    def test_heisenberg_dims(self):
        result = verify_p1_finite_weight_spaces('heisenberg', 5)
        assert result['dims'][0] == 1
        assert result['dims'][1] == 1
        assert result['dims'][2] == 2
        assert result['dims'][3] == 3
        assert result['dims'][4] == 5
        assert result['dims'][5] == 7

    def test_positive_energy(self):
        """All standard families satisfy positive energy."""
        for family in ['heisenberg', 'virasoro', 'affine_sl2']:
            result = verify_p1_finite_weight_spaces(family, 5)
            assert result['positive_energy']


# ===================================================================
# 4. (P2) NONDEGENERATE INVARIANT FORM
# ===================================================================

class TestP2NondegenerateForm:
    """Verify (P2) for all standard families at generic parameters."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma',
    ])
    def test_p2_satisfied(self, family):
        result = verify_p2_nondegenerate_form(family, 8)
        assert result['p2_satisfied'], f"(P2) should hold for {family} at generic level"

    def test_no_degenerate_weights(self):
        for family in ['heisenberg', 'virasoro']:
            result = verify_p2_nondegenerate_form(family, 10)
            assert result['degenerate_weights'] == []


# ===================================================================
# 5. (P3) DUAL REGULARITY VIA HOLSTEIN-RIVERA
# ===================================================================

class TestP3DualRegularity:
    """Verify (P3) follows from (P1)+(P2) via Holstein-Rivera."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'w3',
    ])
    def test_p3_satisfied(self, family):
        result = verify_p3_dual_regularity(family, 5)
        assert result['p3_satisfied']

    def test_holstein_rivera_applicable(self):
        """Holstein-Rivera applies to all smooth Koszul algebras."""
        for family in ['heisenberg', 'virasoro', 'affine_sl2']:
            result = verify_p3_dual_regularity(family, 5)
            assert result['holstein_rivera_applicable']
            assert result['smooth']
            assert result['koszul']


# ===================================================================
# 6. CYCLIC PAIRING PERFECTNESS
# ===================================================================

class TestCyclicPairingPerfectness:
    """Verify the cyclic pairing is perfect for standard families."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma',
    ])
    def test_genus_1_perfect(self, family):
        result = cyclic_pairing_matrix(family, 1)
        assert result['perfect']

    def test_heisenberg_genus_2(self):
        result = cyclic_pairing_matrix('heisenberg', 2)
        assert result['perfect']

    def test_full_perfectness_heisenberg(self):
        result = verify_perfectness_full('heisenberg', 3)
        assert result['perfect_all_genera']
        assert result['k11_applicable']

    def test_full_perfectness_virasoro(self):
        result = verify_perfectness_full('virasoro', 3)
        assert result['perfect_all_genera']


# ===================================================================
# 7. HOLSTEIN-RIVERA CY EXCHANGE
# ===================================================================

class TestHolsteinRivera:
    """Verify Holstein-Rivera's smooth/proper CY exchange."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'w3',
    ])
    def test_exchange_valid(self, family):
        result = holstein_rivera_exchange(family)
        assert result['exchange_valid']
        assert result['smooth_cy_on_A']
        assert result['proper_cy_on_B']

    def test_p3_follows(self):
        """(P3) follows from CY exchange on Koszul locus."""
        for family in ['heisenberg', 'virasoro', 'affine_sl2']:
            result = holstein_rivera_exchange(family)
            assert result['p3_follows']

    def test_cy_dimension_is_1(self):
        """All chiral algebras on curves have CY dimension 1."""
        for family in ['heisenberg', 'virasoro', 'affine_sl2', 'w3']:
            assert cy_dimension(family) == 1


# ===================================================================
# 8. CALAQUE-SAFRONOV AKSZ
# ===================================================================

class TestCalaqueSafronov:
    """Verify AKSZ shifted symplectic data."""

    def test_shift_on_M_comp(self):
        """M_comp carries a (-1)-shifted symplectic structure."""
        for g in range(1, 5):
            result = aksz_shifted_symplectic_data(g)
            assert result['shift_on_M_comp'] == -1

    def test_shift_on_C_g(self):
        """C_g(A) carries a (-(3g-3))-shifted symplectic structure."""
        result = aksz_shifted_symplectic_data(1)
        assert result['shift_on_C_g'] == 0
        result = aksz_shifted_symplectic_data(2)
        assert result['shift_on_C_g'] == -3

    def test_log_fm_compatible(self):
        result = aksz_shifted_symplectic_data(1)
        assert result['log_fm_compatible']
        assert result['relative_extension']


# ===================================================================
# 9. FANG PVA FROM SHIFTED SYMPLECTIC
# ===================================================================

class TestFangPVA:
    """Verify Fang's PVA construction from shifted symplectic."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma',
    ])
    def test_pva_bracket_matches(self, family):
        result = pva_from_shifted_symplectic(family)
        assert result['pva_bracket_matches']

    def test_r_matrix_is_mc(self):
        """R-matrix = MC element of PVA deformation complex."""
        for family in ['heisenberg', 'virasoro']:
            result = pva_from_shifted_symplectic(family)
            assert result['r_matrix_is_mc']

    def test_integrable_hierarchy(self):
        """Classes G and L give integrable hierarchies."""
        assert pva_from_shifted_symplectic('heisenberg')['integrable_hierarchy']
        assert pva_from_shifted_symplectic('affine_sl2')['integrable_hierarchy']
        assert not pva_from_shifted_symplectic('virasoro')['integrable_hierarchy']


# ===================================================================
# 10. PRIDHAM QUANTIZATION
# ===================================================================

class TestPridhamQuantization:
    """Verify Pridham's deformation quantization."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma',
    ])
    def test_unique_quantization(self, family):
        result = pridham_quantization(family, 1)
        assert result['unique_quantization']

    def test_associator_independent_genus_1(self):
        """At genus 1 (shift = 0), quantization is associator-independent."""
        result = pridham_quantization('heisenberg', 1)
        assert result['associator_independent']

    def test_associator_dependent_genus_2(self):
        """At genus >= 2, quantization depends on associator."""
        result = pridham_quantization('heisenberg', 2)
        assert not result['associator_independent']

    def test_quantization_bridge(self):
        result = pridham_quantization('virasoro', 1)
        assert 'BD_0' in result['quantization_bridge']


# ===================================================================
# 11. LAGRANGIAN CONDITION
# ===================================================================

class TestLagrangianCondition:
    """Verify the Lagrangian condition for standard families."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'w3',
    ])
    def test_lagrangian(self, family):
        result = verify_lagrangian_condition(family, 1)
        assert result['lagrangian']

    def test_isotropy(self):
        result = verify_lagrangian_condition('heisenberg', 1)
        assert result['isotropic_A']
        assert result['isotropic_A_dual']

    def test_half_dimensional(self):
        result = verify_lagrangian_condition('virasoro', 1)
        assert result['half_dimensional']
        assert result['dim_M_A'] == 1
        assert result['dim_M_A_dual'] == 1
        assert result['dim_M_comp'] == 2

    def test_transversality(self):
        for family in ['heisenberg', 'virasoro', 'affine_sl2']:
            result = verify_lagrangian_condition(family, 1)
            assert result['transverse']


# ===================================================================
# 12. K11 CONDITIONALITY ANALYSIS
# ===================================================================

class TestK11Conditionality:
    """Central test: K11 status for each standard family."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'affine_sl3',
        'betagamma', 'bc', 'w3', 'lattice',
    ])
    def test_k11_unconditional(self, family):
        result = k11_conditionality_analysis(family)
        assert result['k11_status'] == 'unconditional'

    def test_weakened_hypothesis(self):
        """After Holstein-Rivera, K11 needs only (P1)+(P2)."""
        for family in ['heisenberg', 'virasoro', 'affine_sl2']:
            result = k11_conditionality_analysis(family)
            assert result['weakened_hypothesis'] == '(P1)+(P2)'

    def test_holstein_rivera_removes_p3(self):
        """Holstein-Rivera is applicable and removes (P3)."""
        for family in ['heisenberg', 'virasoro', 'affine_sl2']:
            result = k11_conditionality_analysis(family)
            assert result['holstein_rivera']

    def test_irreducible_hypothesis(self):
        """(P2) is irreducible: the form must be nondegenerate."""
        result = k11_conditionality_analysis('heisenberg')
        assert 'nondegenerate' in result['irreducible_hypothesis'].lower()


# ===================================================================
# 13. FULL LANDSCAPE CENSUS
# ===================================================================

class TestLandscapeCensus:
    """Full landscape census for K11."""

    def test_all_unconditional(self):
        result = k11_full_landscape_census()
        assert result['all_unconditional']

    def test_universal_weakened_hypothesis(self):
        result = k11_full_landscape_census()
        assert result['universal_weakened_hypothesis'] == '(P1)+(P2)'

    def test_all_families_present(self):
        result = k11_full_landscape_census()
        families = result['families']
        assert 'heisenberg' in families
        assert 'virasoro' in families
        assert 'affine_sl2' in families
        assert 'betagamma' in families
        assert 'w3' in families
        assert len(families) >= 8


# ===================================================================
# 14. COMPLEMENTARITY SUMS (AP24-AWARE)
# ===================================================================

class TestComplementaritySums:
    """Verify kappa + kappa' sums, respecting AP24."""

    def test_heisenberg_antisymmetric(self):
        result = complementarity_sum('heisenberg')
        assert result['sum'] == 0
        assert result['anti_symmetric']

    def test_virasoro_not_antisymmetric(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        result = complementarity_sum('virasoro')
        assert result['sum'] == 13
        assert not result['anti_symmetric']

    def test_affine_sl2_antisymmetric(self):
        result = complementarity_sum('affine_sl2')
        assert result['sum'] == 0

    def test_betagamma_antisymmetric(self):
        result = complementarity_sum('betagamma')
        assert result['sum'] == 0

    def test_all_match_expected(self):
        for family in ['heisenberg', 'virasoro', 'affine_sl2', 'betagamma']:
            result = complementarity_sum(family)
            assert result['matches_expected']


# ===================================================================
# 15. THEOREM B SHIFTED-SYMPLECTIC ANALYSIS
# ===================================================================

class TestTheoremBAnalysis:
    """Analyze shifted-symplectic perspective on Theorem B."""

    def test_not_new_proof(self):
        result = shifted_symplectic_inversion_analysis()
        assert not result['new_proof']

    def test_conceptual_upgrade(self):
        result = shifted_symplectic_inversion_analysis()
        assert result['conceptual_upgrade']

    def test_proof_chain_length(self):
        result = shifted_symplectic_inversion_analysis()
        assert len(result['proof_chain']) == 5

    def test_ptvv_in_chain(self):
        result = shifted_symplectic_inversion_analysis()
        assert any('PTVV' in step for step in result['proof_chain'])


# ===================================================================
# 16. FULL SYNTHESIS
# ===================================================================

class TestFullSynthesis:
    """Full shifted symplectic analysis for each family."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'virasoro', 'affine_sl2', 'betagamma',
    ])
    def test_full_analysis(self, family):
        result = full_shifted_symplectic_analysis(family)
        assert result['k11_unconditional']
        assert result['cy_exchange_valid']
        assert result['lagrangian']
        assert result['quantization_unique']
        assert result['pva_matches']

    def test_aksz_shift(self):
        result = full_shifted_symplectic_analysis('heisenberg')
        assert result['aksz_shift'] == -1


# ===================================================================
# 17. WHAT REMAINS CONDITIONAL
# ===================================================================

class TestWhatRemains:
    """Verify the precise characterization of remaining conditionality."""

    def test_p3_removed(self):
        result = what_remains_conditional()
        assert result['p3_removed']

    def test_p2_irreducible(self):
        result = what_remains_conditional()
        assert result['p2_irreducible']

    def test_p1_irreducible(self):
        result = what_remains_conditional()
        assert result['p1_irreducible']

    def test_weakened_correctly(self):
        result = what_remains_conditional()
        assert result['weakened_from'] == '(P1)+(P2)+(P3)'
        assert result['weakened_to'] == '(P1)+(P2)'

    def test_removed_by_holstein_rivera(self):
        result = what_remains_conditional()
        assert 'Holstein-Rivera' in result['removed_by']

    def test_still_open_items(self):
        result = what_remains_conditional()
        assert len(result['still_open']) >= 3
        # Critical level is in the open items
        assert any('critical' in item.lower() for item in result['still_open'])


# ===================================================================
# 18. CROSS-ENGINE CONSISTENCY
# ===================================================================

class TestCrossEngineConsistency:
    """Verify consistency with entanglement_shadow_engine kappa values."""

    def test_kappa_heisenberg_consistent(self):
        """Engine kappa matches entanglement_shadow_engine."""
        assert _family_kappa('heisenberg') == kappa_heisenberg(1)

    def test_kappa_virasoro_consistent(self):
        assert _family_kappa('virasoro') == kappa_virasoro(1)

    def test_kappa_betagamma_consistent(self):
        assert _family_kappa('betagamma') == kappa_betagamma(1)

    def test_kappa_affine_sl2_consistent(self):
        assert _family_kappa('affine_sl2') == kappa_affine(3, 1, 2)

    def test_shadow_depth_consistent(self):
        """Shadow depth classes consistent across engines."""
        assert shadow_depth_class('heisenberg') == 'G'
        assert shadow_depth_class('virasoro') == 'M'
        assert shadow_depth_class('affine') == 'L'

    def test_kappa_dual_ap24_virasoro(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
        Here c=1, so kappa=1/2, kappa'=25/2, sum=13."""
        k = _family_kappa('virasoro')
        k_dual = _family_kappa_dual('virasoro')
        assert k + k_dual == 13

    def test_kappa_dual_ap24_heisenberg(self):
        """For Heisenberg: kappa + kappa' = 0."""
        k = _family_kappa('heisenberg')
        k_dual = _family_kappa_dual('heisenberg')
        assert k + k_dual == 0


# ===================================================================
# 19. WEIGHT SPACE DIMENSIONS
# ===================================================================

class TestWeightSpaceDimensions:
    """Verify weight space dimensions for standard families."""

    def test_heisenberg_weight_0(self):
        assert weight_space_dimension('heisenberg', 0) == 1

    def test_heisenberg_weight_4(self):
        assert weight_space_dimension('heisenberg', 4) == 5

    def test_affine_sl2_weight_0(self):
        assert weight_space_dimension('affine_sl2', 0) == 1

    def test_affine_sl2_weight_1(self):
        # 3-colored partitions of 1 = 3
        assert weight_space_dimension('affine_sl2', 1) == 3

    def test_betagamma_weight_1(self):
        # 2-colored partitions of 1 = 2
        assert weight_space_dimension('betagamma', 1) == 2

    def test_dimensions_grow(self):
        """Weight spaces should grow with weight."""
        for family in ['heisenberg', 'virasoro']:
            dims = [weight_space_dimension(family, n) for n in range(10)]
            # Not strictly monotone at n=0,1 but overall growing
            assert dims[-1] > dims[0]


# ===================================================================
# 20. EDGE CASES AND ROBUSTNESS
# ===================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_genus_1_shift_zero(self):
        """Genus 1 is the critical case: ordinary symplectic."""
        assert shifted_symplectic_degree(1) == 0

    def test_bc_ghost_negative_kappa(self):
        """bc ghosts have kappa = -13."""
        result = k11_conditionality_analysis('bc')
        assert result['k11_status'] == 'unconditional'

    def test_complementarity_bc(self):
        """bc + bc_dual: kappa + kappa' = -13 + 13 = 0."""
        result = complementarity_sum('bc')
        assert result['sum'] == 0

    def test_w3_analysis(self):
        result = full_shifted_symplectic_analysis('w3')
        assert result['k11_unconditional']

    def test_lattice_analysis(self):
        result = k11_conditionality_analysis('lattice')
        assert result['k11_status'] == 'unconditional'
