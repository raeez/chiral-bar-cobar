"""Independent-oracle tests for the hook-type compatibility engine."""

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
    anomaly_ratio_from_partition,
    bar_cohomology_h0,
    bar_cohomology_h1_generators,
    bar_cohomology_h2_estimate,
    bar_degree_one_generator_count,
    c_complementarity_22,
    c_complementarity_31_211,
    c_sl4_22,
    c_sl4_211,
    c_sl4_31,
    c_sl4_principal,
    complementarity_constant,
    ds_kappa_from_affine,
    ghost_constant,
    ghost_constant_hook,
    hook_dual_level_sl4,
    hook_dual_level_sl_n,
    hook_kappa_anti_symmetry_catalog,
    kappa_anti_symmetry_22,
    kappa_anti_symmetry_31_211,
    kappa_complementarity_sum,
    kappa_sl4_22,
    kappa_sl4_211,
    kappa_sl4_31,
    kappa_sl4_principal,
    krw_central_charge,
    krw_central_charge_data,
    levi_rho_from_partition,
    levi_rho_norm_squared,
    reciprocal_weight_diagnostic_from_partition,
    rho_shift_norm_squared,
    sl4_22_generators,
    sl4_hook_211_generators,
    sl4_hook_31_generators,
    sl4_hook_duality_data,
    sl4_principal_generators,
    transpose_ghost_sum,
    verify_hook_type_w_duality,
    weyl_vector_norm_squared_sl_n,
    weyl_vector_sl_n,
    w_algebra_generator_data,
)
from compute.lib.non_principal_w_bar_engine import type_a_krw_central_charge
from compute.lib.nonprincipal_ds_orbits import (
    homogeneous_f_centralizer_basis_sl_n,
    hook_partition,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


def _matrix_weight_oracle(partition):
    triple = type_a_partition_sl2_triple(partition)
    graded = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return sorted(
        Rational(1) - Rational(grade, 2)
        for grade, basis in graded.items()
        for _ in basis
    )


def _engine_weights(partition):
    return sorted(weight for _, weight, _ in w_algebra_generator_data(partition).strong_generators)


class TestPartitionAndWeylData:
    def test_sl4_transpose_orbits(self):
        assert transpose_partition((3, 1)) == (2, 1, 1)
        assert transpose_partition((2, 1, 1)) == (3, 1)
        assert transpose_partition((2, 2)) == (2, 2)

    def test_weyl_vector_coordinates(self):
        assert weyl_vector_sl_n(4) == (
            Rational(3, 2), Rational(1, 2), Rational(-1, 2), Rational(-3, 2)
        )

    @pytest.mark.parametrize("N", range(2, 9))
    def test_weyl_norm_closed_formula(self, N):
        direct = sum(value * value for value in weyl_vector_sl_n(N))
        expected = Rational(N * (N * N - 1), 12)
        assert direct == expected == weyl_vector_norm_squared_sl_n(N)

    @pytest.mark.parametrize(
        ("partition", "expected"),
        [
            ((4,), Rational(0)),
            ((1, 1, 1, 1), Rational(5)),
            ((3, 1), Rational(1, 2)),
            ((2, 1, 1), Rational(1, 2)),
            ((2, 2), Rational(1)),
        ],
    )
    def test_grade_zero_levi_norms(self, partition, expected):
        coordinates = levi_rho_from_partition(partition)
        assert sum(value * value for value in coordinates) == expected
        assert levi_rho_norm_squared(partition) == expected

    def test_rho_shift_is_norm_difference(self):
        for partition in ((4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)):
            assert rho_shift_norm_squared(partition) == (
                weyl_vector_norm_squared_sl_n(4) - levi_rho_norm_squared(partition)
            )


class TestGeneratorData:
    @pytest.mark.parametrize(
        ("partition", "count"),
        [((4,), 3), ((3, 1), 5), ((2, 2), 7), ((2, 1, 1), 9)],
    )
    def test_centralizer_generator_counts(self, partition, count):
        data = w_algebra_generator_data(partition)
        assert data.f_centralizer_dimension == count
        assert len(data.strong_generators) == count

    @pytest.mark.parametrize(
        "partition",
        [(2, 1), (4,), (3, 1), (2, 2), (2, 1, 1), (3, 2, 1)],
    )
    def test_generator_weights_match_matrix_centralizer(self, partition):
        """The tensor-decomposition implementation matches a matrix kernel."""

        assert _engine_weights(partition) == _matrix_weight_oracle(partition)

    @pytest.mark.parametrize(
        "factory",
        [sl4_hook_211_generators, sl4_hook_31_generators, sl4_22_generators, sl4_principal_generators],
    )
    def test_sl4_generators_are_even(self, factory):
        data = factory()
        assert data.n_even == data.f_centralizer_dimension
        assert data.n_odd == 0
        assert {parity for _, _, parity in data.strong_generators} == {"even"}

    def test_sl4_hook_weight_ledgers(self):
        assert _engine_weights((2, 1, 1)) == [
            Rational(1), Rational(1), Rational(1), Rational(1),
            Rational(3, 2), Rational(3, 2), Rational(3, 2), Rational(3, 2),
            Rational(2),
        ]
        assert _engine_weights((3, 1)) == [
            Rational(1), Rational(2), Rational(2), Rational(2), Rational(3),
        ]


class TestKRWCentralCharge:
    @pytest.mark.parametrize("partition", [(4,), (3, 1), (2, 2), (2, 1, 1)])
    def test_compatibility_engine_matches_canonical_krw(self, partition):
        assert simplify(krw_central_charge(partition, k) - type_a_krw_central_charge(partition, k)) == 0

    def test_sl4_principal_primary_formula(self):
        expected = 3 - 60 * (k + 3) ** 2 / (k + 4)
        assert simplify(c_sl4_principal(k) - expected) == 0

    def test_sl4_rectangular_primary_formula(self):
        expected = 15 * k / (k + 4) - 12 * k - 8
        assert simplify(c_sl4_22(k) - expected) == 0

    def test_sl4_hook_formulas_from_direct_krw_ingredients(self):
        expected_31 = (-24 * k**2 - 115 * k - 136) / (k + 4)
        expected_211 = (-6 * k**2 - 9 * k) / (k + 4)
        assert simplify(c_sl4_31(k) - expected_31) == 0
        assert simplify(c_sl4_211(k) - expected_211) == 0

    @pytest.mark.parametrize("partition", [(4,), (3, 1), (2, 2), (2, 1, 1)])
    def test_krw_packet_exposes_source_and_ingredients(self, partition):
        data = krw_central_charge_data(partition)
        assert "Kac--Roan--Wakimoto" in data.source
        assert data.central_charge == krw_central_charge(partition)
        assert data.x_norm_squared == sum(value * value for value in data.x_diagonal)
        assert data.dim_g_half == sum(grade == Rational(1, 2) for grade in data.positive_root_grades)


class TestExactDiagnostics:
    @pytest.mark.parametrize(
        ("partition", "expected"),
        [
            ((4,), Rational(10)),
            ((3, 1), Rational(6)),
            ((2, 2), Rational(4)),
            ((2, 1, 1), Rational(3)),
            ((1, 1, 1, 1), Rational(0)),
        ],
    )
    def test_ghost_constant(self, partition, expected):
        assert ghost_constant(partition) == expected

    def test_hook_ghost_wrapper(self):
        for N in range(3, 8):
            for r in range(1, N - 1):
                assert ghost_constant_hook(N, r) == ghost_constant(hook_partition(N, r))

    def test_transpose_ghost_sum_is_symmetric(self):
        for partition in ((3, 1), (2, 2), (2, 1, 1)):
            assert transpose_ghost_sum(partition) == transpose_ghost_sum(transpose_partition(partition))
            assert complementarity_constant(partition) == -transpose_ghost_sum(partition)

    @pytest.mark.parametrize(
        ("partition", "expected"),
        [
            ((2, 1), Rational(17, 6)),
            ((4,), Rational(13, 12)),
            ((3, 1), Rational(17, 6)),
            ((2, 2), Rational(5)),
            ((2, 1, 1), Rational(43, 6)),
        ],
    )
    def test_unsigned_reciprocal_weight_diagnostic(self, partition, expected):
        direct = sum(Rational(1) / weight for weight in _engine_weights(partition))
        assert direct == expected == reciprocal_weight_diagnostic_from_partition(partition)

    def test_formal_reflection_is_involutive(self):
        assert hook_dual_level_sl4(k) == -k - 8
        assert simplify(hook_dual_level_sl4(hook_dual_level_sl4(k)) - k) == 0
        for N in range(2, 8):
            assert simplify(hook_dual_level_sl_n(N, hook_dual_level_sl_n(N, k)) - k) == 0

    def test_formal_central_charge_sums_remain_scalar_arithmetic(self):
        assert simplify(c_complementarity_22(k) - 110) == 0
        assert simplify(c_complementarity_31_211(k).diff(k)) != 0


class TestTypedModularAndBarClaims:
    @pytest.mark.parametrize("partition", [(2, 1), (3, 1), (2, 2), (2, 1, 1)])
    def test_rho_packet_is_open(self, partition):
        packet = anomaly_ratio_from_partition(partition)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        with pytest.raises(OpenInvariantError):
            packet.require_value()

    @pytest.mark.parametrize("partition", [(2, 1), (3, 1), (2, 2), (2, 1, 1)])
    def test_ds_kappa_packet_is_conditional(self, partition):
        packet = ds_kappa_from_affine(partition, k)
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None
        assert any("H_hook^{DS/bar}" in item for item in packet.hypotheses)

    @pytest.mark.parametrize(
        "factory",
        [kappa_sl4_211, kappa_sl4_31, kappa_sl4_22, kappa_sl4_principal],
    )
    def test_sl4_kappa_wrappers_keep_open_numeric_surface(self, factory):
        packet = factory(k)
        assert isinstance(packet, ClaimPacket)
        assert packet.value is None

    def test_modular_conductor_apis_are_open(self):
        for packet in (
            kappa_complementarity_sum((3, 1), k),
            kappa_anti_symmetry_31_211(k),
            kappa_anti_symmetry_22(k),
        ):
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None

    def test_hook_modular_catalog_has_typed_packets(self):
        catalog = hook_kappa_anti_symmetry_catalog(6, k)
        assert catalog
        assert all(packet.status is ClaimStatus.OPEN for packet in catalog.values())
        assert all(packet.value is None for packet in catalog.values())

    def test_bar_degree_one_chain_count_is_exact(self):
        assert bar_degree_one_generator_count((2, 1, 1)) == 9
        assert bar_degree_one_generator_count((3, 1)) == 5

    @pytest.mark.parametrize(
        "factory",
        [bar_cohomology_h0, bar_cohomology_h1_generators, bar_cohomology_h2_estimate],
    )
    def test_bar_cohomology_requires_comparison_data(self, factory):
        packet = factory((3, 1))
        assert packet.status in {ClaimStatus.CONDITIONAL, ClaimStatus.OPEN}
        assert packet.value is None


class TestHookComparisonData:
    def test_sl4_hook_data_separates_transpose_and_duality(self):
        data = sl4_hook_duality_data(k)
        assert data.source_partition == (3, 1)
        assert data.target_partition == (2, 1, 1)
        assert data.transpose_relation
        assert data.formal_reflected_level == -k - 8
        assert data.koszul_duality.status is ClaimStatus.CONDITIONAL
        assert data.koszul_duality.value is None
        assert data.ksdual_membership.status is ClaimStatus.OPEN
        assert data.ksdual_membership.value is None

    def test_sl4_hook_data_retains_exact_central_arithmetic(self):
        data = sl4_hook_duality_data(k)
        expected = c_sl4_31(k) + c_sl4_211(-k - 8)
        assert simplify(data.formal_central_charge_sum - expected) == 0

    def test_verification_bundle_distinguishes_booleans_and_packets(self):
        audit = verify_hook_type_w_duality()
        exact_keys = (
            "transpose_relation",
            "transpose_involution",
            "source_generator_count",
            "target_generator_count",
            "all_source_generators_even",
            "all_target_generators_even",
            "central_charge_source_matches_krw",
            "central_charge_target_matches_krw",
            "formal_reflection_is_involutive",
        )
        assert all(audit[key] is True for key in exact_keys)
        assert audit["ds_bar_commutation"].status is ClaimStatus.CONDITIONAL
        assert audit["koszul_duality"].status is ClaimStatus.CONDITIONAL
        assert audit["ksdual_membership"].status is ClaimStatus.OPEN
        assert audit["modular_conductor"].status is ClaimStatus.OPEN


def test_source_excludes_legacy_numeric_promotions():
    source = Path("compute/lib/hook_type_w_duality.py").read_text()
    legacy_fragments = (
        "98" + "/3",
        "kappa = rho" + "_lambda * c",
        "has 4 " + "fermionic generators",
        "bar H^1 = " + "9",
        "transport-to-transpose " + "conjecture holds",
    )
    assert all(source.find(fragment) == -1 for fragment in legacy_fragments)
