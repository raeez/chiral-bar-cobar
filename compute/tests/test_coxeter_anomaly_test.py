"""Finite-window tests for compute/lib/coxeter_anomaly_test.

The test surface is deliberately modest: exact S_n sign checks, type-A
Vandermonde divisibility oracles, the A2 Chevalley discriminant identity,
and the Virasoro level-4 Lambda packet.  None of these tests is allowed to
promote a finite reflection-group diagnostic to a full anomaly class.
"""

from itertools import permutations

import sympy as sp

from compute.lib.coxeter_anomaly_test import (
    antisymmetrize,
    chevalley_A2_discriminant_packet,
    identify_genuine_insight,
    is_anti_invariant,
    polynomial_divides,
    permutation_sign,
    shadow_arity2,
    shadow_arity3,
    test_claim_A_arity2 as claim_A_arity2,
    test_claim_A_arity3 as claim_A_arity3,
    test_claim_A_arity4 as claim_A_arity4,
    test_claim_A_arity4_on_constraint as claim_A_arity4_on_constraint,
    test_claim_A_arity5 as claim_A_arity5,
    test_claim_B as claim_B,
    total_mode_degree,
    vandermonde,
    virasoro_level4_finite_window_packet,
)


def inversion_count_sign(perm):
    inversions = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


def test_permutation_sign_matches_inversion_count():
    """Cycle-decomposition sign agrees with the independent inversion count."""
    for perm in permutations(range(4)):
        perm = list(perm)
        assert permutation_sign(perm) == inversion_count_sign(perm)


def test_vandermonde_is_the_sign_oracle():
    """Delta_n is anti-invariant, and Delta_n times a symmetric factor divides."""
    m1, m2, m3 = sp.symbols('m1 m2 m3')
    modes = [m1, m2, m3]
    delta = vandermonde(modes)
    symmetric_factor = m1**2 + m2**2 + m3**2

    assert is_anti_invariant(delta, modes)
    assert polynomial_divides(sp.expand(delta * symmetric_factor), delta, modes)
    assert not polynomial_divides(symmetric_factor, delta, modes)


def test_rank_one_arity2_and_arity3_are_not_sign_representations():
    """The tested rank-one shadow tensors are symmetric and have zero sign part."""
    m1, m2, m3 = sp.symbols('m1 m2 m3')
    c = sp.Symbol('c')
    sh2 = shadow_arity2(m1, m2, c / 2)
    sh3 = shadow_arity3(m1, m2, m3)

    assert claim_A_arity2()['is_symmetric']
    assert not claim_A_arity2()['is_anti_invariant']
    assert sp.simplify(antisymmetrize(sh2, [m1, m2])) == 0

    assert claim_A_arity3()['is_symmetric']
    assert not claim_A_arity3()['is_anti_invariant']
    assert sp.simplify(antisymmetrize(sh3, [m1, m2, m3])) == 0


def test_raw_arity4_lift_has_no_sign_or_vandermonde_certificate():
    """The raw arity-4 lift is degree 6, non-physical, and not alternating."""
    result = claim_A_arity4()

    assert result['amplitude_degree'] == 6
    assert result['physical_quartic_degree'] == 4
    assert not result['is_fully_symmetric']
    assert not result['is_anti_invariant']
    assert result['anti_part_vanishes']
    assert result['vandermonde_degree'] == 6
    assert not result['is_vandermonde_divisible']
    assert result['full_anomaly_class_inferred'] is False


def test_constraint_restriction_does_not_recover_physical_quartic():
    """Imposing sum m_i=0 on the raw lift still leaves a degree-6 diagnostic."""
    result = claim_A_arity4_on_constraint()

    assert result['constrained_degree'] == 6
    assert result['line_degree'] == 6
    assert result['physical_quartic_degree'] == 4
    assert result['matches_physical_quartic_degree'] is False
    assert result['full_anomaly_class_inferred'] is False


def test_toy_arity5_is_symmetric_but_not_a_vandermonde_anomaly():
    """The cubic-quartic toy lift has zero sign projection and degree below Delta_5."""
    result = claim_A_arity5()

    assert result['amplitude_degree'] == 7
    assert result['physical_quintic_degree'] == 5
    assert result['is_symmetric']
    assert result['anti_part_vanishes']
    assert result['vandermonde_degree'] == 10
    assert not result['is_vandermonde_divisible']
    assert result['full_anomaly_class_inferred'] is False


def test_A2_chevalley_discriminant_identity_exact():
    """On H_3, Delta_3^2 = p2^3/2 - 3 p3^2."""
    packet = chevalley_A2_discriminant_packet()

    assert packet['identity_holds']
    assert packet['scope'] == 'finite_A2_Chevalley_discriminant_only'
    assert packet['full_anomaly_class_inferred'] is False


def test_claim_B_is_only_a_finite_reflection_group_diagnostic():
    """Claim B records type-A dimensions, not a proof of shadow-depth cause."""
    result = claim_B()

    assert result['A2_identity_holds']
    assert result['chevalley_degrees_by_arity'][5] == (2, 3, 4, 5)
    assert result['correlation_tautological']
    assert 'not Chevalley geometry' in result['genuine_content']
    assert result['full_anomaly_class_inferred'] is False


def test_virasoro_level4_lambda_packet_matches_local_source_formula():
    """Level-4 Gram determinant, Lambda norm, and S4 share c(5c+22)."""
    c = sp.Symbol('c')
    packet = virasoro_level4_finite_window_packet()

    assert sp.simplify(packet['vacuum_level4_gram_det'] - c**2 * (5 * c + 22) / 2) == 0
    assert sp.simplify(packet['lambda_norm'] - c * (5 * c + 22) / 10) == 0
    assert sp.simplify(packet['S4'] - sp.Rational(10, 1) / (c * (5 * c + 22))) == 0
    assert packet['S4_times_lambda_norm'] == 1
    assert sp.simplify(packet['shared_factor'] - (5 * c + 22)) == 0
    assert sp.simplify(packet['shared_denominator'] - c * (5 * c + 22)) == 0
    assert sp.simplify(packet['det_over_shared_factor'] - c**2 / 2) == 0
    assert sp.simplify(packet['det_over_S4_denominator'] - c / 2) == 0
    assert packet['full_anomaly_class_inferred'] is False


def test_identify_genuine_insight_stays_finite_window():
    """Summary rejects sign/Chevalley overclaims and names the open obligation."""
    c = sp.Symbol('c')
    result = identify_genuine_insight()

    assert 'no sign-representation component' in result['claim_A']
    assert 'not structural cause' in result['claim_B']
    assert 'not Chevalley geometry' in result['genuine_connection']
    assert 'remains open' in result['open_question']
    assert sp.simplify(result['kac_level4'] - c**2 * (5 * c + 22) / 2) == 0
    assert sp.simplify(result['shared_factor'] - (5 * c + 22)) == 0
    assert sp.simplify(result['shared_denominator'] - c * (5 * c + 22)) == 0
    assert result['S4_times_lambda_norm'] == 1
    assert result['A2_discriminant_identity_holds']
    assert result['kac_shadow_connection_status'] == 'finite-window shared-factor check'
    assert result['scope'] == 'finite_window_diagnostics_only'
    assert result['full_anomaly_class_inferred'] is False


def test_total_mode_degree_clears_only_scalar_denominators():
    """Degree oracle is independent of scalar c-denominators in rational shadows."""
    m1, m2 = sp.symbols('m1 m2')
    c = sp.Symbol('c')
    assert total_mode_degree((m1 - m2) ** 2 / (c * (5 * c + 22)), [m1, m2]) == 2
