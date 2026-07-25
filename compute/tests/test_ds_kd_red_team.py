"""Independent oracles for the DS/KD adversarial audit engine."""

from __future__ import annotations

import inspect
from collections import Counter

import pytest
from sympy import Matrix, Rational, Symbol, simplify

import compute.lib.ds_kd_red_team as audit_module
from compute.lib.ds_kd_red_team import (
    AuditSeverity,
    H_BAR_BRST_BICOMPLEX,
    H_BC_DUALITY,
    H_BC_SPECIALNESS,
    H_CRITICAL_PRESENTATION,
    H_DS_KD_COMPARISON,
    H_EXT_OBSTRUCTION,
    H_KAZHDAN_FORMALITY,
    H_MODULAR_GENUS_ONE,
    H_NONPRINCIPAL_LEVEL,
    NON_HOOK_TARGETS,
    analyze_admissible_level,
    analyze_colliding_level,
    analyze_critical_level,
    analyze_type_b2_orbits,
    b_collapse,
    bershadsky_polyakov_control,
    c_collapse,
    complementarity_sum_is_constant,
    complementarity_sum_non_hook,
    enumerate_type_b_orbits,
    enumerate_type_c_orbits,
    formal_central_audit,
    full_red_team_report,
    ghost_obstruction_analysis,
    is_special_type_b_orbit,
    is_valid_type_b_partition,
    is_valid_type_c_partition,
    kappa_sum_is_constant,
    kappa_sum_non_hook,
    probe_all_non_hooks,
    probe_non_hook,
    spectral_sequence_probe,
)
from compute.lib.hook_type_w_duality import ClaimPacket, ClaimStatus, OpenInvariantError
from compute.lib.nonprincipal_ds_orbits import (
    homogeneous_f_centralizer_basis_sl_n,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


EXPECTED = {
    (2, 2): {
        "N": 4,
        "transpose": (2, 2),
        "centralizer": 7,
        "orbit": 8,
        "n_plus": 4,
        "g_half": 0,
        "grades": {Rational(1): 4},
        "bracket_rank": 0,
        "ghost": 4,
        "weights": (1, 1, 1, 2, 2, 2, 2),
        "central_sum": 110,
    },
    (3, 2): {
        "N": 5,
        "transpose": (2, 2, 1),
        "centralizer": 8,
        "orbit": 16,
        "n_plus": 10,
        "g_half": 4,
        "grades": {Rational(1, 2): 4, Rational(1): 3, Rational(3, 2): 2, Rational(2): 1},
        "bracket_rank": 6,
        "ghost": 10,
        "weights": (1, Rational(3, 2), Rational(3, 2), 2, 2, Rational(5, 2), Rational(5, 2), 3),
        "central_sum": 110 - 18 * k,
    },
    (3, 3): {
        "N": 6,
        "transpose": (2, 2, 2),
        "centralizer": 11,
        "orbit": 24,
        "n_plus": 12,
        "g_half": 0,
        "grades": {Rational(1): 8, Rational(2): 4},
        "bracket_rank": 4,
        "ghost": 16,
        "weights": (1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3),
        "central_sum": 148 - 30 * k,
    },
    (2, 2, 2): {
        "N": 6,
        "transpose": (3, 3),
        "centralizer": 17,
        "orbit": 18,
        "n_plus": 9,
        "g_half": 0,
        "grades": {Rational(1): 9},
        "bracket_rank": 0,
        "ghost": 9,
        "weights": (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2),
        "central_sum": 508 + 30 * k,
    },
    (4, 2): {
        "N": 6,
        "transpose": (2, 2, 1, 1),
        "centralizer": 9,
        "orbit": 26,
        "n_plus": 13,
        "g_half": 0,
        "grades": {Rational(1): 8, Rational(2): 4, Rational(3): 1},
        "bracket_rank": 5,
        "ghost": 19,
        "weights": (1, 2, 2, 2, 2, 3, 3, 3, 4),
        "central_sum": 16 - 54 * k,
    },
    (3, 2, 1): {
        "N": 6,
        "transpose": (3, 2, 1),
        "centralizer": 13,
        "orbit": 22,
        "n_plus": 14,
        "g_half": 6,
        "grades": {Rational(1, 2): 6, Rational(1): 5, Rational(3, 2): 2, Rational(2): 1},
        "bracket_rank": 8,
        "ghost": 13,
        "weights": (1, 1, Rational(3, 2), Rational(3, 2), Rational(3, 2), Rational(3, 2), 2, 2, 2, 2, Rational(5, 2), Rational(5, 2), 3),
        "central_sum": 320,
    },
}


def independent_bracket_oracle(partition):
    """Build ``n_+`` and its commutator span directly from matrix units."""

    N = sum(partition)
    h = type_a_partition_sl2_triple(partition).h
    x = tuple(Rational(h[index, index], 2) for index in range(N))
    units = tuple(
        (row, column, x[row] - x[column])
        for row in range(N)
        for column in range(N)
        if row != column and x[row] - x[column] > 0
    )
    brackets = []
    for left_index, (i, j, _left_grade) in enumerate(units):
        for p, q, _right_grade in units[left_index + 1 :]:
            vector = [0] * (N * N)
            if j == p:
                vector[N * i + q] += 1
            if q == i:
                vector[N * p + j] -= 1
            if any(vector):
                brackets.append(Matrix(vector))
    rank = Matrix.hstack(*brackets).rank() if brackets else 0
    grades = Counter(grade for _row, _column, grade in units)
    return len(units), dict(sorted(grades.items())), int(rank)


def independent_generator_weights(partition):
    """Read the homogeneous ``g^f`` basis and convert degree to weight."""

    triple = type_a_partition_sl2_triple(partition)
    basis_by_grade = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return tuple(
        sorted(
            Rational(1) - Rational(grade, 2)
            for grade, basis in basis_by_grade.items()
            for _generator in basis
        )
    )


class TestFiniteTypeAProbe:
    @pytest.mark.parametrize("partition, expected", EXPECTED.items())
    def test_partition_orbit_and_generator_oracles(self, partition, expected):
        probe = probe_non_hook(expected["N"], partition)
        assert probe.transpose == expected["transpose"]
        assert probe.centralizer_dim == expected["centralizer"]
        assert probe.orbit_dim == expected["orbit"]
        assert probe.n_generators == expected["centralizer"]
        assert probe.generator_weights == expected["weights"]
        assert probe.generator_weights == independent_generator_weights(partition)
        assert probe.n_even == probe.n_generators
        assert probe.n_odd == 0

    @pytest.mark.parametrize("partition, expected", EXPECTED.items())
    def test_brst_matrix_oracle(self, partition, expected):
        bracket = ghost_obstruction_analysis(expected["N"], partition)
        oracle_dim, oracle_grades, oracle_rank = independent_bracket_oracle(partition)
        assert bracket.n_plus_dim == expected["n_plus"] == oracle_dim
        assert bracket.grading == expected["grades"] == oracle_grades
        assert bracket.g_half_dim == expected["g_half"]
        assert bracket.bracket_span_dimension == expected["bracket_rank"] == oracle_rank
        assert bracket.n_plus_is_abelian is (oracle_rank == 0)
        assert bracket.quadratic_ghost_term_present is (oracle_rank > 0)
        assert bracket.ghost_constant_value == expected["ghost"]

    @pytest.mark.parametrize("partition, expected", EXPECTED.items())
    def test_every_bracket_witness_has_additive_grade(self, partition, expected):
        bracket = ghost_obstruction_analysis(expected["N"], partition)
        for witness in bracket.bracket_witnesses:
            assert witness.result
            assert witness.result_grade == witness.left.grade + witness.right.grade
            assert witness.result_grade > 0

    def test_catalog_is_genuinely_non_hook(self):
        for N, partition, _description in NON_HOOK_TARGETS:
            assert sum(partition) == N
            assert sum(part > 1 for part in partition) >= 2

    def test_probe_catalog_runs_and_preserves_all_targets(self):
        probes = probe_all_non_hooks()
        assert len(probes) == len(NON_HOOK_TARGETS)
        assert {probe.partition for probe in probes.values()} == set(EXPECTED)

    def test_partition_size_mismatch_fails_loudly(self):
        with pytest.raises(ValueError, match="expected 5"):
            probe_non_hook(5, (2, 2))


class TestBershadskyPolyakovControl:
    def test_standard_generators_weights_and_parity(self):
        control = bershadsky_polyakov_control()
        assert control.generators == (
            ("J", 1, "even"),
            ("G+", Rational(3, 2), "even"),
            ("G-", Rational(3, 2), "even"),
            ("L", 2, "even"),
        )

    def test_standard_central_charge_and_reflection(self):
        control = bershadsky_polyakov_control()
        expected_c = -(2 * k + 3) * (3 * k + 1) / (k + 3)
        assert simplify(control.central_charge - expected_c) == 0
        assert control.formal_reflected_level == -k - 6
        assert simplify(control.formal_central_sum - 50) == 0

    def test_exact_ope_coefficients(self):
        control = bershadsky_polyakov_control()
        assert simplify(control.jj_pole2 - (2 * k + 3) / 3) == 0
        assert control.jg_plus_charge == 1
        assert control.jg_minus_charge == -1
        assert simplify(control.gpgm_pole3 - (k + 1) * (2 * k + 3)) == 0
        assert simplify(control.gpgm_pole2_coefficient - 3 * (k + 1)) == 0
        assert simplify(control.ll_pole4 - control.central_charge / 2) == 0

    def test_exact_pole_ledger(self):
        control = bershadsky_polyakov_control()
        pole_map = {(left, right): poles for left, right, poles in control.pole_orders}
        assert pole_map[("L", "L")] == (4, 2, 1)
        assert pole_map[("J", "J")] == (2,)
        assert pole_map[("G+", "G-")] == (3, 2, 1)
        assert pole_map[("G+", "G+")] == ()

    def test_primary_normalization_source_is_exposed(self):
        control = bershadsky_polyakov_control()
        assert "Fehily--Kawasetsu--Ridout" in control.source
        assert "Definition 2.1" in control.source


class TestFormalCentralArithmetic:
    @pytest.mark.parametrize("partition, expected", EXPECTED.items())
    def test_hardcoded_reflected_scalar_oracle(self, partition, expected):
        scalar = complementarity_sum_non_hook(expected["N"], partition)
        assert simplify(scalar - expected["central_sum"]) == 0
        audit = formal_central_audit(expected["N"], partition)
        assert simplify(audit.formal_sum - expected["central_sum"]) == 0
        assert "Kac--Roan--Wakimoto" in audit.source

    @pytest.mark.parametrize(
        "N, partition, expected_constant, expected_value",
        [
            (4, (2, 2), True, 110),
            (5, (3, 2), False, 110 - 18 * k),
            (6, (3, 3), False, 148 - 30 * k),
            (6, (2, 2, 2), False, 508 + 30 * k),
            (6, (4, 2), False, 16 - 54 * k),
            (6, (3, 2, 1), True, 320),
        ],
    )
    def test_scalar_constancy_is_only_symbolic_arithmetic(
        self, N, partition, expected_constant, expected_value
    ):
        is_constant, value = complementarity_sum_is_constant(N, partition)
        assert is_constant is expected_constant
        assert simplify(value - expected_value) == 0

    def test_scalar_modular_promotion_remains_open(self):
        audit = formal_central_audit(4, (2, 2))
        assert audit.modular_interpretation.status is ClaimStatus.OPEN
        assert audit.modular_interpretation.value is None
        assert H_MODULAR_GENUS_ONE in audit.modular_interpretation.hypotheses
        assert H_NONPRINCIPAL_LEVEL in audit.modular_interpretation.hypotheses

    def test_kappa_sum_is_an_open_packet(self):
        for function in (kappa_sum_non_hook, kappa_sum_is_constant):
            packet = function(4, (2, 2))
            assert isinstance(packet, ClaimPacket)
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None
            assert H_MODULAR_GENUS_ONE in packet.hypotheses
            with pytest.raises(OpenInvariantError):
                packet.require_value()


class TestSpectralSequenceAudit:
    @pytest.mark.parametrize("partition, expected", EXPECTED.items())
    def test_finite_inputs_are_exact(self, partition, expected):
        spectral = spectral_sequence_probe(expected["N"], partition)
        assert spectral.brst.n_plus_dim == expected["n_plus"]
        assert spectral.brst.bracket_span_dimension == expected["bracket_rank"]
        assert spectral.strong_generator_count == expected["centralizer"]

    @pytest.mark.parametrize("partition, expected", EXPECTED.items())
    def test_every_spectral_conclusion_is_typed(self, partition, expected):
        spectral = spectral_sequence_probe(expected["N"], partition)
        packets = (
            spectral.higher_brst_cohomology,
            spectral.kazhdan_degeneration,
            spectral.cross_differential,
            spectral.ds_bar_comparison,
            spectral.obstruction_class,
        )
        assert all(packet.status is ClaimStatus.OPEN for packet in packets)
        assert all(packet.value is None for packet in packets)
        assert H_KAZHDAN_FORMALITY in spectral.kazhdan_degeneration.hypotheses
        assert H_BAR_BRST_BICOMPLEX in spectral.cross_differential.hypotheses
        assert H_EXT_OBSTRUCTION in spectral.obstruction_class.hypotheses

    def test_abelian_bracket_has_no_promoted_collapse(self):
        spectral = spectral_sequence_probe(4, (2, 2))
        assert spectral.brst.n_plus_is_abelian
        assert spectral.kazhdan_degeneration.status is ClaimStatus.OPEN
        assert spectral.obstruction_class.status is ClaimStatus.OPEN

    def test_nonabelian_bracket_has_no_invented_ext_dimension_or_bidegree(self):
        spectral = spectral_sequence_probe(5, (3, 2))
        assert spectral.brst.bracket_span_dimension == 6
        assert not hasattr(spectral, "obstruction_bidegree")
        assert not hasattr(spectral.brst, "ext_group_dimension")
        assert spectral.obstruction_class.value is None


class TestTypeBCFiniteAudit:
    def test_b2_and_c2_partition_enumeration(self):
        assert set(enumerate_type_b_orbits(2)) == {
            (5,),
            (3, 1, 1),
            (2, 2, 1),
            (1, 1, 1, 1, 1),
        }
        assert set(enumerate_type_c_orbits(2)) == {
            (4,),
            (2, 2),
            (2, 1, 1),
            (1, 1, 1, 1),
        }

    @pytest.mark.parametrize(
        "partition, valid_b, valid_c",
        [
            ((3, 1, 1), True, False),
            ((2, 2, 1), True, False),
            ((3, 1), True, False),
            ((2, 1, 1), False, True),
            ((2, 2), True, True),
        ],
    )
    def test_parity_validity(self, partition, valid_b, valid_c):
        assert is_valid_type_b_partition(partition) is valid_b
        assert is_valid_type_c_partition(partition) is valid_c

    @pytest.mark.parametrize(
        "function, partition, expected",
        [
            (b_collapse, (3, 2), (3, 1, 1)),
            (b_collapse, (4, 1), (3, 1, 1)),
            (c_collapse, (3, 1), (2, 2)),
            (c_collapse, (4,), (4,)),
            (c_collapse, (2, 1, 1), (2, 1, 1)),
        ],
    )
    def test_dominance_collapse(self, function, partition, expected):
        assert function(partition) == expected

    def test_specialness_is_typed_instead_of_hardcoded(self):
        for partition in enumerate_type_b_orbits(2):
            packet = is_special_type_b_orbit(partition)
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None
            assert H_BC_SPECIALNESS in packet.hypotheses

    def test_type_changing_duality_is_typed(self):
        analyses = analyze_type_b2_orbits()
        assert len(analyses) == 8
        for orbit in analyses.values():
            assert orbit.is_valid_partition
            assert orbit.specialness.status is ClaimStatus.OPEN
            assert orbit.spaltenstein_image.status is ClaimStatus.OPEN
            assert orbit.bv_dual.status is ClaimStatus.OPEN
            assert H_BC_DUALITY in orbit.bv_dual.hypotheses
            assert orbit.finding.severity is AuditSeverity.SERIOUS

    def test_invalid_type_b_specialness_input_fails_loudly(self):
        with pytest.raises(ValueError, match="type-B parity"):
            is_special_type_b_orbit((4, 1))


class TestLevelAudit:
    @pytest.mark.parametrize("N, partition", [(4, (2, 2)), (5, (3, 2)), (6, (3, 3))])
    def test_critical_denominator_and_formal_fixed_point(self, N, partition):
        result = analyze_critical_level(N, partition)
        assert result.level_value == -N
        assert result.affine_sugawara_denominator == 0
        assert result.affine_sugawara_denominator_vanishes
        assert result.formal_reflected_level == -N
        assert result.formal_reflection_fixed
        assert H_CRITICAL_PRESENTATION in result.conformal_presentation.hypotheses

    def test_critical_behavior_is_presentation_sensitive(self):
        result = analyze_critical_level(4, (2, 2))
        for packet in (
            result.universal_ds_reduction,
            result.conformal_presentation,
            result.simple_quotient_null_ideal,
            result.pbw_koszulness,
            result.ds_bar_comparison,
            result.modular_kappa,
        ):
            assert packet.status in {ClaimStatus.OPEN, ClaimStatus.CONDITIONAL}
            assert packet.value is None
        assert not hasattr(result, "ds_is_defined")
        assert not hasattr(result, "pbw_koszulness_holds")

    def test_admissible_arithmetic(self):
        result = analyze_admissible_level(4, (2, 2), p=5, q=2)
        assert result.level_value == Rational(-3, 2)
        assert result.affine_sugawara_denominator == Rational(5, 2)
        assert result.basic_admissibility_arithmetic
        assert result.simple_quotient_null_ideal.status is ClaimStatus.OPEN

    @pytest.mark.parametrize("p, q", [(4, 2), (3, 1)])
    def test_failed_basic_admissibility_arithmetic_is_recorded(self, p, q):
        result = analyze_admissible_level(4, (2, 2), p=p, q=q)
        assert result.basic_admissibility_arithmetic is False

    def test_nonpositive_admissible_denominator_fails_loudly(self):
        with pytest.raises(ValueError, match="q must be positive"):
            analyze_admissible_level(4, (2, 2), p=5, q=0)

    def test_colliding_level_is_the_same_exact_arithmetic_surface(self):
        collision = analyze_colliding_level(4, (2, 2))
        critical = analyze_critical_level(4, (2, 2))
        assert collision.level_value == critical.level_value == -4
        assert collision.affine_sugawara_denominator_vanishes
        assert collision.formal_reflection_fixed


class TestTypedProbeAndReport:
    def test_nonhook_probe_exposes_every_frontier_claim(self):
        probe = probe_non_hook(5, (3, 2))
        packets = (
            probe.rho_source,
            probe.rho_transpose,
            probe.kappa_w,
            probe.kappa_dual_w,
            probe.modular_conductor,
            probe.ds_bar_commutation,
            probe.pbw_collapse,
            probe.koszul_duality,
            probe.categorical_transport,
            probe.transpose_duality,
            probe.ksdual_membership,
        )
        assert all(isinstance(packet, ClaimPacket) for packet in packets)
        assert all(packet.status in {ClaimStatus.OPEN, ClaimStatus.CONDITIONAL} for packet in packets)
        assert all(packet.value is None for packet in packets)

    def test_finite_graph_reachability_is_not_categorical_transport(self):
        probe = probe_non_hook(5, (3, 2))
        assert probe.finite_graph_reaches_transpose
        assert probe.finite_transport_path == ((3, 2), (3, 1, 1), (2, 2, 1))
        assert probe.categorical_transport.status is ClaimStatus.CONDITIONAL
        assert probe.categorical_transport.value is None
        assert audit_module.H_TRANSPOSE_DUALITY in probe.transpose_duality.hypotheses

    def test_full_report_collects_checkable_findings(self):
        reports = full_red_team_report()
        assert len(reports) == len(NON_HOOK_TARGETS)
        for report in reports:
            assert report.findings
            assert all(finding.exact_evidence for finding in report.findings)
            assert all(finding.obligations for finding in report.findings)
            assert all(finding.claim.value is None for finding in report.findings)
            assert all(
                finding.severity in {
                    AuditSeverity.CRITICAL,
                    AuditSeverity.SERIOUS,
                    AuditSeverity.MODERATE,
                    AuditSeverity.MINOR,
                }
                for finding in report.findings
            )

    def test_report_has_no_promoted_verdict_fields(self):
        report = full_red_team_report()[0]
        for legacy_field in (
            "ds_kd_plausible",
            "obstruction_severity",
            "spectral_sequence_collapses",
            "kappa_constant",
        ):
            assert not hasattr(report, legacy_field)

    def test_findings_name_comparison_and_modular_packages(self):
        probe = probe_non_hook(5, (3, 2))
        obligations = {obligation for finding in probe.findings for obligation in finding.obligations}
        assert H_DS_KD_COMPARISON in obligations
        assert H_MODULAR_GENUS_ONE in obligations


class TestSemanticGuards:
    def test_source_contains_no_unresolved_kappa_arithmetic(self):
        source = inspect.getsource(audit_module)
        forbidden = (
            "kappa_w + kappa_dual_w",
            "kappa_direct + kappa_dual",
            "simplify(kappa_w",
            "simplify(kappa_direct",
        )
        assert all(fragment not in source for fragment in forbidden)

    def test_source_contains_no_invented_spectral_or_ext_verdicts(self):
        source = inspect.getsource(audit_module)
        forbidden = (
            "obstruction_bidegree",
            "ext_group_dimension",
            "spectral_sequence_collapses",
            "h1_ds_survives_at_generic_level",
            "Ext^1 >=",
        )
        assert all(fragment not in source for fragment in forbidden)

    def test_source_contains_no_legacy_critical_or_duality_verdict_fields(self):
        source = inspect.getsource(audit_module)
        forbidden = (
            "ds_is_defined",
            "pbw_koszulness_holds",
            "bv_dual_exists",
            "ds_kd_plausible",
        )
        assert all(fragment not in source for fragment in forbidden)
