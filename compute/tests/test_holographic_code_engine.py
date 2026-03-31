r"""Tests for holographic_code_engine.py.

Verification strategy:
  1. 12-fold Koszulness-code dictionary structure
  2. Code parameters for all standard families
  3. Knill-Laflamme from Lagrangian orthogonality (algebraic proof)
  4. Shadow depth as redundancy structure (conjecture resolution)
  5. Main theorem: Koszulness = exact QEC
  6. Standard landscape code census
  7. Non-Koszul code failure examples
  8. Cross-checks with G11 (entanglement)
  9. Complementarity as code constraint
"""

import pytest
from sympy import Rational

from compute.lib.holographic_code_engine import (
    # Section 1: dictionary
    get_koszulness_code_dictionary,
    unconditional_equivalences,
    KOSZULNESS_CODE_DICTIONARY,
    # Section 2: code parameters
    code_parameters,
    redundancy_channels,
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


# ===================================================================
#  1. KOSZULNESS-CODE DICTIONARY
# ===================================================================

class TestKoszulnessCodeDictionary:
    """The 12-fold dictionary K1-K12 -> code properties."""

    def test_dictionary_has_12_entries(self):
        d = get_koszulness_code_dictionary()
        assert len(d) == 12

    def test_10_unconditional(self):
        """10 unconditional equivalences (K1-K10)."""
        assert len(unconditional_equivalences()) == 10

    def test_k4_is_exact_recovery(self):
        """K4 (bar-cobar quasi-iso) = exact recovery."""
        d = get_koszulness_code_dictionary()
        k4 = [x for x in d if x['id'] == 'K4'][0]
        assert k4['code_property'] == 'Exact recovery'
        assert 'Theorem B' in k4['algebraic']

    def test_k11_is_conditional(self):
        """K11 (Lagrangian criterion) is conditional."""
        d = get_koszulness_code_dictionary()
        k11 = [x for x in d if x['id'] == 'K11'][0]
        assert k11['status'] == 'conditional'

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
        assert p['exact_recovery']
        assert p['code_rate'] == Rational(1, 2)

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

    def test_all_standard_are_koszul(self):
        """All standard families are Koszul."""
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            p = code_parameters(family)
            assert p['is_koszul']
            assert p['exact_recovery']

    def test_code_rate_is_half(self):
        """Lagrangian = half-dimensional => code rate 1/2."""
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            p = code_parameters(family)
            assert p['code_rate'] == Rational(1, 2)


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
        """V+ and V- are NOT Shapovalov-orthogonal; the decomposition is symplectic."""
        result = verify_shapovalov_cross_pairing()
        assert result['lagrangian_isotropy'] is True
        assert result['shapovalov_orthogonal'] is False
        assert result['cross_pairing_sign'] == -1
        assert result['decomposition_type'] == 'symplectic'

    def test_scalar_kl(self):
        assert verify_knill_laflamme_scalar_level()

    def test_kl_structure_prerequisites_proved(self):
        kl = knill_laflamme_structure()
        assert kl['isotropy_proved']
        assert kl['orthogonality_proved']
        assert kl['scalar_kl_genus_1']

    def test_kl_higher_genus_honest(self):
        """Full KL at genus >= 2 is open (honest scope)."""
        kl = knill_laflamme_structure()
        assert kl['full_kl_higher_genus'] == 'open'

    def test_kl_overall_status(self):
        kl = knill_laflamme_structure()
        assert 'PROVED' in kl['overall_status']
        assert 'prerequisites' in kl['overall_status'].lower()


# ===================================================================
#  4. SHADOW DEPTH CONJECTURE RESOLUTION
# ===================================================================

class TestShadowRedundancyResolution:
    """Resolution of conj:thqg-shadow-depth-code-distance."""

    def test_conjecture_resolved(self):
        res = shadow_redundancy_resolution()
        assert res['conjecture_status'] == 'RESOLVED'

    def test_code_distance_is_2(self):
        """Code distance in arity filtration is always 2."""
        res = shadow_redundancy_resolution()
        assert res['code_distance_all_families'] == 2

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


# ===================================================================
#  5. MAIN THEOREM
# ===================================================================

class TestMainTheorem:
    """Koszulness = Exact Quantum Error Correction."""

    def test_theorem_proved(self):
        thm = koszulness_equals_exact_qec()
        assert thm['status'] == 'PROVED'

    def test_three_equivalences(self):
        thm = koszulness_equals_exact_qec()
        assert len(thm['equivalences']) == 3

    def test_equivalence_i_is_koszulness(self):
        thm = koszulness_equals_exact_qec()
        assert 'Koszul' in thm['equivalences'][0]['statement']

    def test_equivalence_ii_is_exact_recovery(self):
        thm = koszulness_equals_exact_qec()
        assert 'exact recovery' in thm['equivalences'][1]['statement']

    def test_equivalence_iii_is_bulk_reconstruction(self):
        thm = koszulness_equals_exact_qec()
        assert 'bulk reconstruction' in thm['equivalences'][2]['statement']

    def test_four_consequences(self):
        thm = koszulness_equals_exact_qec()
        assert len(thm['consequences']) == 4

    def test_proof_references_theorem_b(self):
        thm = koszulness_equals_exact_qec()
        assert 'Theorem B' in thm['proof_sketch']


# ===================================================================
#  6. STANDARD LANDSCAPE CODE CENSUS
# ===================================================================

class TestCodeCensus:
    """Standard landscape code census."""

    def test_census_nonempty(self):
        census = standard_landscape_code_census()
        assert len(census) >= 7

    def test_all_koszul(self):
        census = standard_landscape_code_census()
        assert all(c['is_koszul'] for c in census)

    def test_all_exact_recovery(self):
        census = standard_landscape_code_census()
        assert all(c['exact_recovery'] for c in census)

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
    """Non-Koszul code failure."""

    def test_examples_exist(self):
        f = non_koszul_code_failure()
        assert len(f['examples']) >= 2

    def test_not_koszul(self):
        f = non_koszul_code_failure()
        for ex in f['examples']:
            assert not ex['is_koszul']
            assert not ex['exact_recovery']

    def test_prediction_exists(self):
        f = non_koszul_code_failure()
        assert 'prediction' in f
        assert 'testable' in f['prediction'].lower()


# ===================================================================
#  7. CROSS-CHECKS WITH G11
# ===================================================================

class TestCrossChecks:
    """Cross-checks with entanglement programme."""

    def test_code_entanglement_consistency(self):
        data = verify_code_entanglement_consistency(Rational(13))
        assert data['consistent']
        assert data['code_rate'] == Rational(1, 2)
        assert data['code_entropy_genus_1'] == 0

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
        """At self-dual point: code fraction = error fraction = 1/2."""
        data = verify_complementarity_as_code_constraint(Rational(13))
        assert data['code_fraction'] == Rational(1, 2)
        assert data['error_fraction'] == Rational(1, 2)

    def test_code_fraction_asymmetric(self):
        """Off self-dual: code and error fractions differ."""
        data = verify_complementarity_as_code_constraint(Rational(1))
        assert data['code_fraction'] != data['error_fraction']
        # kappa(1) = 1/2, kappa(25) = 25/2
        # code fraction = (1/2)/13 = 1/26
        assert data['code_fraction'] == Rational(1, 26)
