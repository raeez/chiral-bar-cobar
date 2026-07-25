"""Independent-oracle tests for non-principal line restrictions."""

from pathlib import Path

import pytest
from sympy import I, Rational, Symbol, exp, pi, simplify

from compute.lib.non_principal_w_bar_engine import (
    bershadsky_polyakov_ope_data,
    type_a_krw_central_charge,
)
from compute.lib.theorem_nonprincipal_line_operators_engine import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
    affine_central_charge,
    affine_line_operators,
    bp_anomaly_ratio,
    bp_central_charge,
    bp_dual_level,
    bp_generator_data,
    bp_kappa,
    bp_kappa_complementarity,
    bp_line_operators,
    bp_line_restrictions,
    bp_numerical_at_level,
    bp_ope_channels,
    bp_rmatrix_channels,
    bp_rmatrix_max_pole,
    bp_shadow_depth,
    bp_shadow_tower_on_tline,
    bp_shifted_central_charge,
    bp_shifted_central_reflection_sum,
    bp_standard_central_reflection_sum,
    build_catalog,
    ds_line_reduction_diagram,
    ff_dual_level,
    koszul_conductor_bp,
    koszul_conductor_principal_wn,
    principal_w3_anomaly_ratio,
    principal_w3_central_charge,
    principal_w3_generator_data,
    principal_w3_kappa,
    principal_w3_kappa_complementarity,
    principal_w3_line_operators,
    principal_w3_rmatrix_max_pole,
    principal_wn_central_charge,
    principal_wn_central_reflection_sum,
    quantum_parameter_at_level,
    shadow_depth_classification,
    sl4_hook_211_line_operators,
    sl4_hook_31_line_operators,
    virasoro_anomaly_ratio,
    virasoro_central_charge,
    virasoro_generator_data,
    virasoro_kappa,
    virasoro_shadow_tower,
)
from compute.lib.nonprincipal_ds_orbits import transpose_partition


k = Symbol("k")


class TestExactCentralCharges:
    def test_bp_standard_formula_is_fkr_equation_2_2(self):
        expected = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
        assert simplify(bp_central_charge(k) - expected) == 0

    @pytest.mark.parametrize(
        ("level", "expected"),
        [(0, -1), (1, -5), (-1, 1), (Rational(-3, 2), 0)],
    )
    def test_bp_standard_specializations(self, level, expected):
        assert simplify(bp_central_charge(level) - expected) == 0

    @pytest.mark.parametrize(
        ("level", "expected"),
        [(0, -6), (1, -22), (-1, 2), (Rational(-3, 2), -2)],
    )
    def test_bp_shifted_secondary_specializations(self, level, expected):
        assert simplify(bp_shifted_central_charge(level) - expected) == 0

    def test_standard_and_shifted_bp_surfaces_are_distinct(self):
        assert simplify(bp_central_charge(k) - bp_shifted_central_charge(k)) != 0

    def test_bp_standard_sum_is_50_by_symbolic_and_numeric_oracles(self):
        assert simplify(bp_standard_central_reflection_sum(k) - 50) == 0
        assert simplify(bp_central_charge(0) + bp_central_charge(-6) - 50) == 0
        assert simplify(bp_central_charge(1) + bp_central_charge(-7) - 50) == 0

    def test_bp_shifted_secondary_sum_is_196(self):
        assert simplify(bp_shifted_central_reflection_sum(k) - 196) == 0
        assert simplify(bp_shifted_central_charge(0) + bp_shifted_central_charge(-6) - 196) == 0

    def test_principal_w3_matches_canonical_krw(self):
        expected = 2 - 24 * (k + 2) ** 2 / (k + 3)
        assert simplify(principal_w3_central_charge(k) - expected) == 0
        assert simplify(principal_w3_central_charge(k) - type_a_krw_central_charge((3,), k)) == 0

    def test_principal_wn_formula(self):
        for N in range(2, 7):
            expected = (N - 1) - N * (N * N - 1) * (k + N - 1) ** 2 / (k + N)
            assert simplify(principal_wn_central_charge(N, k) - expected) == 0

    def test_affine_sugawara_formula(self):
        for N in range(2, 7):
            expected = k * (N * N - 1) / (k + N)
            assert simplify(affine_central_charge(N, k) - expected) == 0

    def test_virasoro_formula(self):
        expected = 1 - 6 * (k + 1) ** 2 / (k + 2)
        assert simplify(virasoro_central_charge(k) - expected) == 0

    @pytest.mark.parametrize(
        ("N", "expected"),
        [(2, 26), (3, 100), (4, 246)],
    )
    def test_principal_central_reflection_sums(self, N, expected):
        assert simplify(principal_wn_central_reflection_sum(N, k) - expected) == 0

    def test_formal_reflections_are_involutive(self):
        assert bp_dual_level(k) == -k - 6
        for N in range(2, 8):
            reflected = ff_dual_level(N, k)
            assert simplify(ff_dual_level(N, reflected) - k) == 0


class TestTypedModularSurface:
    @pytest.mark.parametrize(
        "factory",
        [bp_anomaly_ratio, principal_w3_anomaly_ratio, virasoro_anomaly_ratio],
    )
    def test_rho_apis_are_open(self, factory):
        packet = factory()
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None

    @pytest.mark.parametrize(
        "factory",
        [bp_kappa, principal_w3_kappa, virasoro_kappa],
    )
    def test_kappa_apis_are_open(self, factory):
        packet = factory(k)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        with pytest.raises(OpenInvariantError):
            packet.require_value()

    @pytest.mark.parametrize(
        "packet",
        [
            koszul_conductor_bp(),
            koszul_conductor_principal_wn(3),
            bp_kappa_complementarity(),
            principal_w3_kappa_complementarity(),
        ],
    )
    def test_modular_conductor_apis_are_open(self, packet):
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None


class TestGeneratorAndLineRestrictions:
    def test_bp_generator_ledger_is_all_even(self):
        data = bp_generator_data()
        assert [entry[0] for entry in data.generators] == ["J", "G+", "G-", "L"]
        assert [entry[1] for entry in data.generators] == [
            Rational(1), Rational(3, 2), Rational(3, 2), Rational(2)
        ]
        assert {entry[2] for entry in data.generators} == {"even"}
        assert data.num_even == 4
        assert data.num_odd == 0

    def test_bp_reciprocal_weight_diagnostic_is_17_over_6(self):
        data = bp_generator_data()
        direct = Rational(1) + Rational(2, 3) + Rational(2, 3) + Rational(1, 2)
        assert data.reciprocal_weight_diagnostic == direct == Rational(17, 6)
        assert data.rho.status is ClaimStatus.OPEN

    def test_principal_generator_ledgers(self):
        w3 = principal_w3_generator_data()
        vir = virasoro_generator_data()
        assert [entry[1] for entry in w3.generators] == [Rational(2), Rational(3)]
        assert [entry[1] for entry in vir.generators] == [Rational(2)]
        assert w3.num_odd == vir.num_odd == 0

    def test_bp_line_restrictions_are_named_and_exact(self):
        restrictions = {restriction.name: restriction for restriction in bp_line_restrictions()}
        assert set(restrictions) == {
            "Heisenberg J-line",
            "Virasoro L-line",
            "charged self-lines",
            "charged pair",
        }
        assert restrictions["Heisenberg J-line"].exact_ope_channels == (("J", "J", 2),)
        assert restrictions["Virasoro L-line"].exact_ope_channels == (("L", "L", 4),)
        assert restrictions["charged self-lines"].exact_ope_channels == (
            ("G+", "G+", 0), ("G-", "G-", 0)
        )
        assert restrictions["charged pair"].exact_ope_channels == (("G+", "G-", 3),)

    def test_every_line_restriction_keeps_full_depth_open(self):
        for restriction in bp_line_restrictions():
            assert restriction.full_shadow_depth.status is ClaimStatus.OPEN
            assert restriction.full_shadow_depth.value is None

    def test_full_bp_depth_is_separate_from_restrictions(self):
        data = bp_shadow_depth()
        assert data["line_restrictions"] == bp_line_restrictions()
        assert data["full_shadow_depth"].status is ClaimStatus.OPEN
        assert data["full_shadow_depth"].value is None

    @pytest.mark.parametrize(
        "packet",
        [
            shadow_depth_classification(Symbol("c")),
            virasoro_shadow_tower(Symbol("c"), 8),
            bp_shadow_tower_on_tline(8),
        ],
    )
    def test_higher_shadow_apis_are_typed_open(self, packet):
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None


class TestLineCategoryPackets:
    @pytest.mark.parametrize(
        "factory",
        [
            lambda: affine_line_operators(3),
            bp_line_operators,
            principal_w3_line_operators,
            sl4_hook_31_line_operators,
            sl4_hook_211_line_operators,
        ],
    )
    def test_line_categories_are_conditional(self, factory):
        data = factory()
        for packet in (
            data.line_category_equivalence,
            data.ds_line_functor,
            data.ds_bar_commutation,
            data.same_family_duality,
            data.ksdual_membership,
        ):
            assert packet.status is ClaimStatus.CONDITIONAL
            assert packet.value is None

    def test_bp_self_transpose_is_combinatorics(self):
        data = bp_line_operators()
        assert data.partition == (2, 1)
        assert data.transpose == (2, 1)
        assert data.is_self_transpose
        assert data.is_self_dual.status is ClaimStatus.CONDITIONAL
        assert data.same_family_duality.status is ClaimStatus.CONDITIONAL
        assert data.ksdual_membership.status is ClaimStatus.CONDITIONAL

    def test_sl4_hook_transpose_pair_is_combinatorics(self):
        left = sl4_hook_31_line_operators()
        right = sl4_hook_211_line_operators()
        assert left.transpose == right.partition
        assert right.transpose == left.partition
        assert left.same_family_duality.status is ClaimStatus.CONDITIONAL
        assert right.same_family_duality.status is ClaimStatus.CONDITIONAL

    def test_formal_quantum_parameter(self):
        data = bp_line_operators()
        assert simplify(data.formal_quantum_parameter - exp(pi * I / (k + 3))) == 0

    @pytest.mark.parametrize("partition", [(2, 1), (3,), (3, 1), (2, 1, 1), (2, 2)])
    def test_ds_line_diagram_has_exact_indices_and_conditional_square(self, partition):
        diagram = ds_line_reduction_diagram(partition)
        assert diagram.transpose == transpose_partition(partition)
        assert diagram.is_self_transpose == (tuple(partition) == diagram.transpose)
        assert diagram.algebraic_ds_reduction.status is ClaimStatus.PROVED_ELSEWHERE
        assert diagram.algebraic_ds_reduction.value is True
        assert diagram.ds_line_functor.status is ClaimStatus.CONDITIONAL
        assert diagram.ds_bar_commutation.status is ClaimStatus.CONDITIONAL
        assert diagram.diagram_commutes.status is ClaimStatus.CONDITIONAL
        assert diagram.diagram_commutes.value is None

    def test_ds_line_diagram_checks_partition_size(self):
        with pytest.raises(ValueError):
            ds_line_reduction_diagram((2, 1), 4)


class TestPrimaryOPEChannels:
    def test_bp_channel_map_matches_fkr_equation_2_1(self):
        expected = {
            ("L", "L"): 4,
            ("L", "J"): 2,
            ("L", "G+"): 2,
            ("L", "G-"): 2,
            ("J", "J"): 2,
            ("J", "G+"): 1,
            ("J", "G-"): 1,
            ("G+", "G+"): 0,
            ("G-", "G-"): 0,
            ("G+", "G-"): 3,
        }
        actual = {
            (channel.source_generator, channel.target_generator): channel.ope_max_pole
            for channel in bp_ope_channels()
        }
        assert actual == expected

    def test_channel_poles_match_the_primary_ope_packet(self):
        ope = bershadsky_polyakov_ope_data(k)
        for channel in bp_ope_channels():
            terms = ope.terms(channel.source_generator, channel.target_generator)
            oracle = max((term.pole_order for term in terms), default=0)
            assert channel.ope_max_pole == oracle

    def test_every_bp_ope_channel_is_even_even(self):
        assert {channel.channel_type for channel in bp_ope_channels()} == {"even-even"}

    def test_collision_residue_extraction_is_conditional(self):
        for channel in bp_rmatrix_channels():
            assert channel.rmatrix_extraction.status is ClaimStatus.CONDITIONAL
            assert channel.rmatrix_extraction.value is None

    def test_maximum_rmatrix_pole_apis_are_conditional(self):
        for packet in (bp_rmatrix_max_pole(), principal_w3_rmatrix_max_pole()):
            assert packet.status is ClaimStatus.CONDITIONAL
            assert packet.value is None


class TestCatalogAndNumerics:
    def test_catalog_has_expected_entries(self):
        assert set(build_catalog()) == {"Vir", "BP", "W3", "sl4_31", "sl4_211"}

    def test_bp_catalog_keeps_scalar_and_modular_lanes_separate(self):
        entry = build_catalog()["BP"]
        assert entry.partition == (2, 1)
        assert entry.transpose == (2, 1)
        assert simplify(entry.central_charge - bp_central_charge(k)) == 0
        assert entry.central_scalar_reflection_sum == 50
        assert entry.shifted_secondary_sum == 196
        assert entry.reciprocal_weight_diagnostic == Rational(17, 6)
        assert entry.rho.status is ClaimStatus.OPEN
        assert entry.kappa.status is ClaimStatus.OPEN
        assert entry.modular_conductor.status is ClaimStatus.OPEN
        assert entry.full_shadow_depth.status is ClaimStatus.OPEN

    def test_bp_numerical_packet_at_zero(self):
        packet = bp_numerical_at_level(0)
        assert packet["formal_reflected_level"] == -6
        assert packet["standard_central_charge"] == -1
        assert packet["reflected_standard_central_charge"] == 51
        assert packet["standard_sum"] == 50
        assert packet["shifted_central_charge"] == -6
        assert packet["shifted_sum"] == 196
        assert packet["reciprocal_weight_diagnostic"] == Rational(17, 6)
        assert packet["kappa"].status is ClaimStatus.OPEN

    def test_quantum_parameter_numeric_specialization(self):
        actual = quantum_parameter_at_level(3, 0)
        expected = complex(exp(pi * I / 3).evalf())
        assert abs(actual - expected) < 1e-12


def test_source_excludes_legacy_promotions():
    source = Path("compute/lib/theorem_nonprincipal_line_operators_engine.py").read_text()
    legacy_fragments = (
        "98" + "/3",
        "ds_kd_commutes=" + "True",
        "diagram_commutes=" + "is_hook",
        "shadow_class='" + "M'",
        "mixed " + "statistics",
        "K_BP = " + "196",
    )
    assert all(source.find(fragment) == -1 for fragment in legacy_fragments)
