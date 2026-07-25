r"""Tests for holographic_code_engine.py.

Verification strategy:
  1. 12-fold Koszulness-code dictionary structure
  2. Code parameters for all standard families
  3. Knill-Laflamme from Lagrangian orthogonality (algebraic proof)
  4. Shadow depth as redundancy structure (conjecture resolution)
  5. Typed Theorem A / Theorem B / physical-decoder surfaces
  6. Standard landscape code census
  7. Non-Koszul code failure examples
  8. Cross-checks with G11 (entanglement)
  9. Complementarity as code constraint
"""

import pytest
from sympy import Matrix, Rational

from compute.lib.qec_koszul_code_engine import (
    quadratic_comparison_cone,
    theorem_b_certificate_from_cone,
)

from compute.lib.holographic_code_engine import (
    # Section 1: dictionary
    get_koszulness_code_dictionary,
    unconditional_equivalences,
    KOSZULNESS_CODE_DICTIONARY,
    # Section 2: code parameters
    code_parameters,
    redundancy_channels,
    theorem_b_recovery_surface_from_shadow_class,
    independent_reconstruction_surfaces,
    # Section 3: Knill-Laflamme
    verify_lagrangian_isotropy,
    verify_shapovalov_cross_pairing,
    verify_knill_laflamme_scalar_level,
    knill_laflamme_structure,
    # Section 4: redundancy
    shadow_redundancy_resolution,
    # Section 5: main theorem
    koszulness_equals_exact_qec,
    # Section 6: census
    standard_landscape_code_census,
    non_koszul_code_failure,
    # Section 7: cross-checks
    verify_code_entanglement_consistency,
    verify_complementarity_as_code_constraint,
)


def _quadratic_certificate(
    algebra_id: str,
    *,
    comparison_entry: int = 1,
    h_cl_verified: bool = True,
    strong_convergence_verified: bool = True,
):
    """Build an exact one-term certificate through the shared engine."""
    cone = quadratic_comparison_cone(
        source_dimensions={0: 1},
        target_dimensions={0: 1},
        source_differentials={},
        target_differentials={},
        comparison_maps={0: Matrix([[comparison_entry]])},
    )
    return theorem_b_certificate_from_cone(
        cone,
        algebra_id=algebra_id,
        presentation='A = T(V)/(R), one-term finite model',
        h_cl_verified=h_cl_verified,
        strong_convergence_verified=strong_convergence_verified,
    )


# ===================================================================
#  1. KOSZULNESS-CODE DICTIONARY
# ===================================================================

class TestKoszulnessCodeDictionary:
    """The 12-fold dictionary K1-K12 -> code properties."""

    def test_dictionary_has_12_entries(self):
        d = get_koszulness_code_dictionary()
        assert len(d) == 12

    def test_6_unconditional_rows(self):
        """The legacy dictionary retains six formally unconditional rows."""
        assert len(unconditional_equivalences()) == 6

    def test_k4_is_exact_recovery(self):
        """K4 is the certificate-governed quadratic comparison."""
        d = get_koszulness_code_dictionary()
        k4 = [x for x in d if x['id'] == 'K4'][0]
        assert k4['code_property'] == 'Exact quadratic recovery'
        assert 'q_A' in k4['algebraic']
        assert 'p_A' in k4['algebraic']
        assert k4['status'] == 'certificate-required'
        assert 'Cone(q_A)' in k4['condition']
        assert 'H_CL' in k4['condition']

    def test_k11_is_conditional(self):
        """K11 (Lagrangian criterion) is conditional."""
        d = get_koszulness_code_dictionary()
        k11 = [x for x in d if x['id'] == 'K11'][0]
        assert k11['status'] == 'conditional'

    def test_k7_is_theorem_h_conditional(self):
        """K7 carries the full Theorem H hypothesis package."""
        d = get_koszulness_code_dictionary()
        k7 = [x for x in d if x['id'] == 'K7'][0]
        assert k7['status'] == 'conditional'
        assert 'PBW chiral Koszulness' in k7['condition']
        assert 'KD_H^bullet(A)' in k7['condition']

    def test_k12_is_one_directional(self):
        """K12 (bifunctor decomposition) is one-directional."""
        d = get_koszulness_code_dictionary()
        k12 = [x for x in d if x['id'] == 'K12'][0]
        assert k12['status'] == 'one-directional'

    def test_all_entries_have_required_fields(self):
        for entry in KOSZULNESS_CODE_DICTIONARY:
            assert 'id' in entry
            assert 'name' in entry
            assert 'algebraic' in entry
            assert 'code_property' in entry
            assert 'code_meaning' in entry
            assert 'status' in entry

    def test_ids_are_sequential(self):
        """K1 through K12."""
        ids = [e['id'] for e in KOSZULNESS_CODE_DICTIONARY]
        expected = [f'K{i}' for i in range(1, 13)]
        assert ids == expected

    def test_code_properties_are_distinct(self):
        """Each code property is unique."""
        props = [e['code_property'] for e in KOSZULNESS_CODE_DICTIONARY]
        assert len(props) == len(set(props))


# ===================================================================
#  2. CODE PARAMETERS
# ===================================================================

class TestCodeParameters:
    """Code parameters for standard families."""

    def test_heisenberg(self):
        p = code_parameters('heisenberg', k=1)
        assert p['shadow_class'] == 'G'
        assert p['redundancy_channels'] == 0
        assert p['algebra_id'] == 'heisenberg:k=1'
        assert p['universal_reconstruction'] is True
        assert p['exact_recovery'] is None
        assert p['exact_recovery_status'] == 'UNVERIFIED'
        assert p['lagrangian_fraction'] == Rational(1, 2)
        assert p['code_rate'] is None

    def test_affine_sl2(self):
        p = code_parameters('affine', k=1, dim_g=3, h_dual=2)
        assert p['shadow_class'] == 'L'
        assert p['redundancy_channels'] == 1
        assert p['kappa'] == Rational(9, 4)

    def test_betagamma(self):
        p = code_parameters('betagamma', lam=1)
        assert p['shadow_class'] == 'C'
        assert p['redundancy_channels'] == 2

    def test_virasoro(self):
        p = code_parameters('virasoro', c=13)
        assert p['shadow_class'] == 'M'
        assert p['redundancy_channels'] == -1  # infinite
        assert p['kappa'] == Rational(13, 2)
        assert p['algebra_id'] == 'virasoro:c=13'
        assert p['exact_recovery_status'] == 'UNVERIFIED'
        assert p['theorem_a_surface']['theorem'] == 'A'
        assert p['theorem_b_surface']['theorem'] == 'B'

    def test_family_name_gives_no_theorem_b_verdict(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            p = code_parameters(family)
            assert p['is_koszul'] is None
            assert p['exact_quadratic_recovery'] is None
            assert p['exact_recovery_status'] == 'UNVERIFIED'

    def test_lagrangian_fraction_is_separate_from_physical_rate(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            p = code_parameters(family)
            assert p['lagrangian_fraction'] == Rational(1, 2)
            assert p['code_rate'] is None
            assert p['code_rate_status'] == 'REQUIRES_HILBERT_REALIZATION'

    @pytest.mark.parametrize('shadow_class', ['G', 'L', 'C', 'M'])
    def test_shadow_class_gives_no_theorem_b_verdict(self, shadow_class):
        surface = theorem_b_recovery_surface_from_shadow_class(shadow_class)
        assert surface['status'] == 'UNVERIFIED'
        assert surface['koszul'] is None
        assert surface['exact_quadratic_recovery'] is None

    def test_exact_certificate_governs_theorem_b(self):
        algebra_id = 'heisenberg:k=1'
        certificate = _quadratic_certificate(algebra_id)
        p = code_parameters(
            'heisenberg',
            k=1,
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert p['universal_reconstruction'] is True
        assert p['quadratic_koszul'] is True
        assert p['exact_quadratic_recovery'] is True
        assert p['exact_recovery_status'] == 'CERTIFIED'
        assert p['theorem_b_surface']['cone_acyclic'] is True

    def test_obstructed_cone_governs_theorem_b(self):
        algebra_id = 'virasoro:c=13'
        certificate = _quadratic_certificate(algebra_id, comparison_entry=0)
        p = code_parameters(
            'virasoro',
            c=13,
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert p['quadratic_koszul'] is False
        assert p['exact_quadratic_recovery'] is False
        assert p['exact_recovery_status'] == 'OBSTRUCTED_IN_FINITE_MODEL'
        assert p['theorem_b_surface']['cone_homology_support']

    def test_acyclic_cone_with_incomplete_package_stays_pending(self):
        algebra_id = 'betagamma:lambda=1'
        certificate = _quadratic_certificate(
            algebra_id, strong_convergence_verified=False
        )
        p = code_parameters(
            'betagamma',
            lam=1,
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert p['theorem_b_surface']['cone_acyclic'] is True
        assert p['quadratic_koszul'] is None
        assert p['exact_quadratic_recovery'] is None
        assert p['exact_recovery_status'] == 'INCOMPLETE_PACKAGE'

    def test_matching_algebra_id_is_required(self):
        certificate = _quadratic_certificate('heisenberg:k=1')
        with pytest.raises(ValueError, match='algebra_id'):
            code_parameters(
                'heisenberg',
                k=2,
                algebra_id='heisenberg:k=2',
                quadratic_certificate=certificate,
            )

    def test_shadow_wrapper_requires_explicit_id_with_certificate(self):
        certificate = _quadratic_certificate('heisenberg:k=1')
        with pytest.raises(ValueError, match='algebra_id'):
            theorem_b_recovery_surface_from_shadow_class(
                'G', certificate=certificate
            )

    def test_reconstruction_surfaces_are_separate(self):
        p = code_parameters('affine')
        assert p['fixed_coalgebra_surface']['status'] == 'SEPARATE_FIXED_C_SURFACE'
        assert p['verdier_dual_surface']['status'] == 'SEPARATE_CONDITIONAL_SURFACE'
        assert p['derived_center_surface']['status'] == 'SEPARATE_DEFINED_SURFACE'
        assert p['physical_recovery'] is None
        assert 'HILBERT' in p['physical_recovery_status']

        surfaces = independent_reconstruction_surfaces()
        assert set(surfaces) == {
            'fixed_coalgebra',
            'verdier_dual',
            'derived_center',
            'physical_decoder',
        }

    def test_theorem_a_chain_package_is_independent(self):
        p = code_parameters(
            'virasoro',
            c=13,
            completed=True,
            chain_package_verified=True,
        )
        assert p['universal_reconstruction'] is True
        assert p['chain_reconstruction'] is True
        assert p['chain_reconstruction_status'] == 'CERTIFIED'
        assert p['exact_recovery_status'] == 'UNVERIFIED'


class TestRedundancyChannels:
    """Redundancy channel counts."""

    def test_class_G(self):
        assert redundancy_channels('heisenberg') == 0
        assert redundancy_channels('lattice') == 0

    def test_class_L(self):
        assert redundancy_channels('affine') == 1
        assert redundancy_channels('kac_moody') == 1

    def test_class_C(self):
        assert redundancy_channels('betagamma') == 2
        assert redundancy_channels('bc') == 2

    def test_class_M(self):
        assert redundancy_channels('virasoro') == -1
        assert redundancy_channels('w_algebra') == -1

    def test_monotonicity(self):
        """G < L < C < M (in redundancy)."""
        r_g = redundancy_channels('heisenberg')
        r_l = redundancy_channels('affine')
        r_c = redundancy_channels('betagamma')
        assert r_g < r_l < r_c


# ===================================================================
#  3. KNILL-LAFLAMME
# ===================================================================

class TestKnillLaflamme:
    """Knill-Laflamme condition from Lagrangian orthogonality."""

    def test_lagrangian_isotropy(self):
        assert verify_lagrangian_isotropy()

    def test_shapovalov_cross_pairing(self):
        """V+ and V- form the nondegenerate cross-pairing."""
        result = verify_shapovalov_cross_pairing()
        assert result['lagrangian_isotropy'] is True
        assert result['shapovalov_orthogonal'] is False
        assert result['cross_pairing_sign'] == -1
        assert result['decomposition_type'] == 'symplectic'

    def test_scalar_kl(self):
        assert verify_knill_laflamme_scalar_level()

    def test_lagrangian_structure_proved(self):
        kl = knill_laflamme_structure()
        assert kl['isotropy_proved']
        assert kl['orthogonality_proved'] is False
        assert kl['cross_pairing_nondegenerate'] is True
        assert kl['scalar_kl_genus_1']

    def test_physical_kl_requires_decoder_data(self):
        kl = knill_laflamme_structure()
        assert kl['full_kl_higher_genus'] is None
        assert kl['physical_recovery'] is None
        assert kl['physical_kl_status'] == (
            'REQUIRES_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
        )

    def test_kl_overall_status(self):
        kl = knill_laflamme_structure()
        assert kl['overall_status'] == 'PROVED_ALGEBRAIC_LAGRANGIAN_SPLITTING'


# ===================================================================
#  4. SHADOW DEPTH CONJECTURE RESOLUTION
# ===================================================================

class TestShadowRedundancyResolution:
    """Arity-filtration reformulation of the distance conjecture."""

    def test_conjecture_reformulated(self):
        res = shadow_redundancy_resolution()
        assert res['conjecture_status'] == 'REFORMULATED_AS_ARITY_PROXY'

    def test_arity_floor_is_distinct_from_physical_distance(self):
        res = shadow_redundancy_resolution()
        assert res['shadow_arity_floor'] == 2
        assert res['code_distance_all_families'] is None
        assert res['physical_distance_status'] == (
            'REQUIRES_HILBERT_ERROR_ALGEBRA_AND_DECODER'
        )

    def test_redundancy_by_class(self):
        res = shadow_redundancy_resolution()
        rb = res['redundancy_by_class']
        assert rb['G']['channels'] == 0
        assert rb['L']['channels'] == 1
        assert rb['C']['channels'] == 2
        assert rb['M']['channels'] == 'infinite'

    def test_recovery_procedure_exists(self):
        res = shadow_redundancy_resolution()
        assert 'recursive' in res['recovery_procedure'].lower()
        assert 'thm:recursive-existence' in res['recovery_procedure']
        assert res['physical_recovery'] is None


# ===================================================================
#  5. MAIN THEOREM
# ===================================================================

class TestMainTheorem:
    """Typed reconstruction surfaces behind the QEC programme."""

    def test_default_surface_is_typed(self):
        thm = koszulness_equals_exact_qec()
        assert thm['status'] == 'TYPED_SURFACES'
        assert thm['status_map']['theorem_a_enhanced_ran_reconstruction'] == (
            'PROVED_ELSEWHERE'
        )
        assert thm['status_map']['theorem_b_quadratic_comparison'] == 'UNVERIFIED'
        assert 'HILBERT' in thm['status_map']['physical_decoder']

    def test_three_typed_maps(self):
        thm = koszulness_equals_exact_qec()
        assert len(thm['typed_maps']) == 3

    def test_first_map_is_universal_epsilon(self):
        thm = koszulness_equals_exact_qec()
        assert thm['typed_maps'][0]['theorem'] == 'A'
        assert thm['typed_maps'][0]['map'] == 'epsilon_A: Omega_X B_X(A) -> A'

    def test_second_map_is_quadratic_comparison(self):
        thm = koszulness_equals_exact_qec()
        assert thm['typed_maps'][1]['theorem'] == 'B'
        assert thm['typed_maps'][1]['map'] == 'q_A: A^i -> B_X(A)'
        assert thm['typed_maps'][1]['obstruction'] == 'Cone(q_A)'

    def test_physical_decoder_is_conditional(self):
        thm = koszulness_equals_exact_qec()
        assert thm['physical_recovery'] is None
        assert 'OCA' in thm['physical_translation']
        assert 'HILBERT' in thm['physical_recovery_status']

    def test_four_independent_algebraic_surfaces(self):
        thm = koszulness_equals_exact_qec()
        assert thm['theorem_a_surface']['theorem'] == 'A'
        assert thm['theorem_b_surface']['theorem'] == 'B'
        assert thm['fixed_coalgebra_surface']['scope'] == 'one fixed coalgebra C'
        assert 'Hochschild' in thm['derived_center_surface']['scope']

    def test_certificate_transitions_only_theorem_b(self):
        algebra_id = 'A:test'
        certificate = _quadratic_certificate(algebra_id)
        thm = koszulness_equals_exact_qec(
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert thm['theorem_a_surface']['enhanced_ran_status'] == 'PROVED_ELSEWHERE'
        assert thm['theorem_b_surface']['status'] == 'CERTIFIED'
        assert thm['exact_quadratic_recovery'] is True
        assert thm['physical_recovery'] is None


# ===================================================================
#  6. STANDARD LANDSCAPE CODE CENSUS
# ===================================================================

class TestCodeCensus:
    """Standard landscape code census."""

    def test_census_nonempty(self):
        census = standard_landscape_code_census()
        assert len(census) >= 7

    def test_default_census_has_no_quadratic_verdict(self):
        census = standard_landscape_code_census()
        assert all(c['is_koszul'] is None for c in census)
        assert all(c['exact_quadratic_recovery'] is None for c in census)
        assert all(c['exact_recovery_status'] == 'UNVERIFIED' for c in census)

    def test_all_have_universal_theorem_a(self):
        census = standard_landscape_code_census()
        assert all(c['universal_reconstruction'] for c in census)
        assert all(c['theorem_a_surface']['theorem'] == 'A' for c in census)
        assert all('recovery_surface' in c for c in census)

    def test_m_class_preserves_unverified_theorem_b_surface(self):
        census = standard_landscape_code_census()
        for entry in census:
            if entry['class'] == 'M':
                assert entry['theorem_b_surface']['status'] == 'UNVERIFIED'
                assert entry['theorem_b_surface']['certificate_present'] is False

    def test_certificate_is_bound_to_one_census_entry(self):
        algebra_id = 'heisenberg:k=1'
        certificate = _quadratic_certificate(algebra_id)
        census = standard_landscape_code_census(
            {algebra_id: certificate}
        )
        certified = [c for c in census if c['exact_recovery_status'] == 'CERTIFIED']
        assert [c['algebra_id'] for c in certified] == [algebra_id]
        pending = [c for c in census if c['algebra_id'] != algebra_id]
        assert all(c['exact_recovery_status'] == 'UNVERIFIED' for c in pending)

    def test_mismatched_census_certificate_is_rejected(self):
        certificate = _quadratic_certificate('heisenberg:k=2')
        with pytest.raises(ValueError, match='algebra_id'):
            standard_landscape_code_census(
                {'heisenberg:k=1': certificate}
            )

    def test_census_keeps_comparison_surfaces_separate(self):
        for entry in standard_landscape_code_census():
            assert entry['fixed_coalgebra_surface']['status'] == (
                'SEPARATE_FIXED_C_SURFACE'
            )
            assert entry['verdier_dual_surface']['status'] == (
                'SEPARATE_CONDITIONAL_SURFACE'
            )
            assert entry['derived_center_surface']['status'] == (
                'SEPARATE_DEFINED_SURFACE'
            )
            assert entry['physical_recovery'] is None

    def test_class_coverage(self):
        """Census covers all four shadow depth classes."""
        census = standard_landscape_code_census()
        classes = {c['class'] for c in census}
        assert 'G' in classes
        assert 'L' in classes
        assert 'C' in classes
        assert 'M' in classes

    def test_convergent_and_divergent(self):
        """Census includes both convergent and divergent M-class."""
        census = standard_landscape_code_census()
        m_class = [c for c in census if c['class'] == 'M']
        convergent = [c for c in m_class if c.get('convergent')]
        divergent = [c for c in m_class if c.get('convergent') == False]
        assert len(convergent) >= 1
        assert len(divergent) >= 1

    def test_self_dual_present(self):
        """Self-dual point c=13 present."""
        census = standard_landscape_code_census()
        sd = [c for c in census if 'self-dual' in c['family']]
        assert len(sd) == 1
        assert sd[0]['kappa'] == Rational(13, 2)


class TestNonKoszulFailure:
    """Quadratic obstruction criterion and candidate loci."""

    def test_examples_exist(self):
        f = non_koszul_code_failure()
        assert len(f['examples']) >= 2

    def test_candidate_loci_are_unverified(self):
        f = non_koszul_code_failure()
        for ex in f['examples']:
            assert ex['status'] == 'UNVERIFIED'
            assert ex['is_koszul'] is None
            assert ex['exact_recovery'] is None
            assert 'Cone(q_A)' in ex['required_computation']

    def test_research_test_exists(self):
        f = non_koszul_code_failure()
        assert f['status'] == 'OBSTRUCTION_CRITERION'
        assert 'research_test' in f
        assert f['physical_recovery'] is None


# ===================================================================
#  7. CROSS-CHECKS WITH G11
# ===================================================================

class TestCrossChecks:
    """Cross-checks with entanglement programme."""

    def test_code_entanglement_consistency(self):
        data = verify_code_entanglement_consistency(Rational(13))
        assert data['consistent'] is None
        assert data['lagrangian_fraction'] == Rational(1, 2)
        assert data['code_rate'] is None
        assert data['code_entropy_genus_1'] == 0
        assert data['comparison_status'] == 'CONDITIONAL_ON_HILBERT_AND_OCA_PACKAGES'

    def test_complementarity_as_code_constraint(self):
        data = verify_complementarity_as_code_constraint(Rational(13))
        assert data['complementarity_holds']
        assert data['is_self_dual']
        assert data['kappa_sum'] == 13

    def test_complementarity_generic(self):
        """Complementarity constraint for generic c."""
        for c in [Rational(1), Rational(7), Rational(25)]:
            data = verify_complementarity_as_code_constraint(c)
            assert data['complementarity_holds']
            assert not data['is_self_dual']

    def test_code_fraction_self_dual(self):
        """At the self-dual point the two scalar fractions equal 1/2."""
        data = verify_complementarity_as_code_constraint(Rational(13))
        assert data['kappa_fraction'] == Rational(1, 2)
        assert data['kappa_dual_fraction'] == Rational(1, 2)
        assert data['code_fraction'] is None
        assert data['error_fraction'] is None

    def test_code_fraction_asymmetric(self):
        """Away from self-duality the scalar fractions differ."""
        data = verify_complementarity_as_code_constraint(Rational(1))
        assert data['kappa_fraction'] != data['kappa_dual_fraction']
        # kappa(1) = 1/2, kappa(25) = 25/2
        # scalar fraction = (1/2)/13 = 1/26
        assert data['kappa_fraction'] == Rational(1, 26)
        assert data['physical_recovery'] is None
