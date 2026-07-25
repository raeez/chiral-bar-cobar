r"""Independent-oracle tests for exact DS data and typed DS--bar claims."""

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.ds_bar_commutation import (
    BarComplexData,
    BershadskyPolyakovData,
    ClaimPacket,
    ClaimStatus,
    DSBarAudit,
    DSBarCommutationData,
    KoszulDualIdentification,
    N2SCAData,
    OpenInvariantError,
    affine_central_charge_sl_n,
    affine_kappa_sl_n,
    bar_complex_n2_sca,
    bershadsky_polyakov_data,
    dim_sl_n,
    ds_bar_commutation_check,
    ds_good_grading_data,
    ds_nilpotent_half_dim,
    ds_nilpotent_plus_dim,
    koszul_dual_identification,
    n2_sca_data,
    sl3_minimal_data,
    sl4_hook_ds_bar_data,
    verify_ds_bar_commutation,
)
from compute.lib.hook_type_w_duality import krw_central_charge
from compute.lib.non_principal_w_bar_engine import bershadsky_polyakov_ope_data
from compute.lib.nonprincipal_ds_orbits import (
    homogeneous_f_centralizer_basis_sl_n,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


def _matrix_weight_oracle(partition):
    triple = type_a_partition_sl2_triple(partition)
    centralizer = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return tuple(sorted(
        Rational(1) - Rational(grade, 2)
        for grade, basis in centralizer.items()
        for _ in basis
    ))


def _good_grading_oracle(partition):
    triple = type_a_partition_sl2_triple(partition)
    n = sum(partition)
    x_diagonal = [Rational(triple.h[index, index], 2) for index in range(n)]
    positive_pairs = []
    grades = {}
    for left in range(n):
        for right in range(n):
            if left == right:
                continue
            grade = x_diagonal[left] - x_diagonal[right]
            if grade > 0:
                positive_pairs.append((left, right))
                grades[grade] = grades.get(grade, 0) + 1
    bracket_exists = any(
        middle == next_left and left != right
        for left, middle in positive_pairs
        for next_left, right in positive_pairs
    )
    return {
        "dimension": len(positive_pairs),
        "grades": dict(sorted(grades.items())),
        "half_dimension": grades.get(Rational(1, 2), 0),
        "abelian": not bracket_exists,
    }


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus):
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses
    with pytest.raises(OpenInvariantError):
        packet.require_value()


class TestStandardBershadskyPolyakovData:
    def test_compatibility_entry_point_has_the_correct_object(self):
        data = n2_sca_data(k)
        assert isinstance(data, N2SCAData)
        assert isinstance(data, BershadskyPolyakovData)
        assert data == bershadsky_polyakov_data(k)
        assert "Bershadsky" in data.source or "Fehily" in data.source

    def test_generators_are_even_with_matrix_weights(self):
        data = bershadsky_polyakov_data(k)
        assert data.generators == (
            ("J", 1, "even"),
            ("G+", Rational(3, 2), "even"),
            ("G-", Rational(3, 2), "even"),
            ("L", 2, "even"),
        )
        assert tuple(weight for _, weight, _ in data.generators) == _matrix_weight_oracle((2, 1))

    def test_standard_central_charge(self):
        data = bershadsky_polyakov_data(k)
        expected = -(2 * k + 3) * (3 * k + 1) / (k + 3)
        assert simplify(data.central_charge - expected) == 0
        assert simplify(data.central_charge - krw_central_charge((2, 1), k)) == 0
        assert data.central_charge.subs(k, 0) == -1
        assert data.central_charge.subs(k, 1) == -5

    def test_formal_reflection_and_standard_sum(self):
        data = bershadsky_polyakov_data(k)
        assert simplify(data.formal_reflected_level + k + 6) == 0
        assert simplify(data.formal_central_sum - 50) == 0

    def test_primary_ope_coefficients(self):
        data = bershadsky_polyakov_data(k)
        assert simplify(data.jj_pole2 - (2 * k + 3) / 3) == 0
        assert data.jg_charge == 1
        assert data.jg_minus_charge == -1
        assert simplify(data.gg_pole3 - (k + 1) * (2 * k + 3)) == 0
        assert simplify(data.gg_pole2_coeff - 3 * (k + 1)) == 0
        assert simplify(data.tt_pole4 - data.central_charge / 2) == 0

    def test_primary_ope_pole_orders(self):
        data = bershadsky_polyakov_data(k)
        assert dict(((left, right), pole) for left, right, pole in data.exact_pole_orders) == {
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

    def test_ope_packet_is_imported_canonically(self):
        data = bershadsky_polyakov_data(k)
        assert data.ope_data == bershadsky_polyakov_ope_data(k)


class TestBPBarInput:
    def test_exact_chain_input(self):
        bar = bar_complex_n2_sca(k)
        assert isinstance(bar, BarComplexData)
        assert bar.partition == (2, 1)
        assert bar.h0_dim == 1
        assert bar.h1_dim == 4
        assert bar.h1_generators == bershadsky_polyakov_data(k).generators
        assert bar.singular_ope_channels == bershadsky_polyakov_data(k).exact_pole_orders

    def test_ope_channels_do_not_create_higher_cohomology_dimensions(self):
        bar = bar_complex_n2_sca(k)
        assert not hasattr(bar, "h2_dim")
        assert not hasattr(bar, "h3_dim")
        assert not hasattr(bar, "euler_char")

    def test_higher_bar_claims_are_typed(self):
        bar = bar_complex_n2_sca(k)
        _assert_unresolved(bar.higher_bar_cohomology, ClaimStatus.OPEN)
        _assert_unresolved(bar.pbw_collapse, ClaimStatus.CONDITIONAL)
        _assert_unresolved(bar.koszulness, ClaimStatus.CONDITIONAL)
        assert bar.is_koszul is bar.koszulness


class TestAffineArithmetic:
    @pytest.mark.parametrize(("N", "dimension"), [(2, 3), (3, 8), (4, 15), (5, 24)])
    def test_dimension(self, N, dimension):
        assert dim_sl_n(N) == dimension

    def test_dimension_domain(self):
        with pytest.raises(ValueError):
            dim_sl_n(1)

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_affine_formulas(self, N):
        assert simplify(
            affine_kappa_sl_n(N, k)
            - Rational(N * N - 1, 2 * N) * (k + N)
        ) == 0
        assert simplify(
            affine_central_charge_sl_n(N, k)
            - k * (N * N - 1) / (k + N)
        ) == 0

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_affine_characteristic_formal_reflection(self, N):
        reflected = -k - 2 * N
        assert simplify(
            affine_kappa_sl_n(N, k) + affine_kappa_sl_n(N, reflected)
        ) == 0


class TestGoodGradingBRSTData:
    @pytest.mark.parametrize(
        ("partition", "dimension", "grades", "abelian", "half_dimension"),
        [
            ((2, 1), 3, {Rational(1, 2): 2, Rational(1): 1}, False, 2),
            ((3,), 3, {Rational(1): 2, Rational(2): 1}, False, 0),
            ((3, 1), 5, {Rational(1): 4, Rational(2): 1}, False, 0),
            ((2, 1, 1), 5, {Rational(1, 2): 4, Rational(1): 1}, False, 4),
            ((2, 2), 4, {Rational(1): 4}, True, 0),
        ],
    )
    def test_hardcoded_good_grading_cases(
        self,
        partition,
        dimension,
        grades,
        abelian,
        half_dimension,
    ):
        data = ds_good_grading_data(partition)
        assert data.n_plus_dim == dimension
        assert data.n_plus_grades == grades
        assert data.n_plus_is_abelian is abelian
        assert data.g_half_dim == half_dimension
        assert ds_nilpotent_plus_dim(partition) == dimension
        assert ds_nilpotent_half_dim(partition) == half_dimension

    @pytest.mark.parametrize("partition", [(2, 1), (3,), (3, 1), (2, 1, 1), (2, 2), (3, 2)])
    def test_matrix_grading_oracle(self, partition):
        expected = _good_grading_oracle(partition)
        data = ds_good_grading_data(partition)
        assert data.n_plus_dim == expected["dimension"]
        assert data.n_plus_grades == expected["grades"]
        assert data.g_half_dim == expected["half_dimension"]
        assert data.n_plus_is_abelian is expected["abelian"]


class TestTypedDSBarProfiles:
    @pytest.mark.parametrize("partition", [(2, 1), (3,), (3, 1), (2, 1, 1), (2, 2), (3, 2)])
    def test_exact_profile_data(self, partition):
        data = ds_bar_commutation_check(partition, k)
        assert isinstance(data, DSBarCommutationData)
        N = sum(partition)
        assert data.affine_generators == N * N - 1
        assert simplify(data.affine_central_charge - affine_central_charge_sl_n(N, k)) == 0
        assert simplify(data.affine_kappa - affine_kappa_sl_n(N, k)) == 0
        assert data.w_generator_weights == _matrix_weight_oracle(partition)
        assert data.w_generators == len(data.w_generator_weights)
        assert data.w_num_even == data.w_generators
        assert data.w_num_odd == 0
        assert simplify(data.w_central_charge - krw_central_charge(partition, k)) == 0

    @pytest.mark.parametrize("partition", [(2, 1), (3,), (3, 1), (2, 1, 1), (2, 2), (3, 2)])
    def test_good_grading_fields_match_independent_oracle(self, partition):
        data = ds_bar_commutation_check(partition, k)
        expected = _good_grading_oracle(partition)
        assert data.positive_grade_multiplicities == expected["grades"]
        assert data.positive_subalgebra_is_abelian is expected["abelian"]
        assert data.ghost_dim == expected["dimension"]
        assert data.neutral_half_dimension == expected["half_dimension"]
        assert data.ghost_constant_value == sum(
            grade * multiplicity for grade, multiplicity in expected["grades"].items()
        )

    @pytest.mark.parametrize("partition", [(2, 1), (3,), (3, 1), (2, 1, 1), (2, 2), (3, 2)])
    def test_modular_and_homological_fields_are_typed(self, partition):
        data = ds_bar_commutation_check(partition, k)
        _assert_unresolved(data.rho, ClaimStatus.OPEN)
        _assert_unresolved(data.w_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.pbw_collapse, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.ds_bar_commutation, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.koszulness, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.categorical_transport, ClaimStatus.CONDITIONAL)
        assert data.kappa_commutes is data.ds_bar_commutation


class TestSl3SeedPacket:
    def test_exact_seed_data(self):
        data = sl3_minimal_data(k)
        assert data["partition"] == (2, 1)
        assert data["transpose"] == (2, 1)
        assert data["is_self_transpose"]
        assert data["n_generators"] == 4
        assert data["n_even"] == 4
        assert data["n_odd"] == 0
        assert data["n_bosonic"] == 4
        assert data["n_fermionic"] == 0
        assert data["reciprocal_weight_diagnostic"] == Rational(17, 6)
        assert data["ghost_constant"] == 2

    def test_standard_central_and_formal_fixed_level(self):
        data = sl3_minimal_data(k)
        expected = -(2 * k + 3) * (3 * k + 1) / (k + 3)
        assert simplify(data["central_charge"] - expected) == 0
        assert simplify(data["formal_reflected_level"] + k + 6) == 0
        assert simplify(data["formal_central_sum"] - 50) == 0
        assert data["formal_fixed_level"] == -3
        assert data["central_charge_has_pole_at_fixed_level"]

    def test_seed_frontier_fields_are_typed(self):
        data = sl3_minimal_data(k)
        _assert_unresolved(data["rho"], ClaimStatus.OPEN)
        _assert_unresolved(data["kappa"], ClaimStatus.CONDITIONAL)
        _assert_unresolved(data["reflected_kappa"], ClaimStatus.CONDITIONAL)
        _assert_unresolved(data["modular_conductor"], ClaimStatus.OPEN)
        _assert_unresolved(data["bar_complex"].koszulness, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data["ds_bar_check"].ds_bar_commutation, ClaimStatus.CONDITIONAL)


class TestSl4HookPair:
    def test_exact_pair_data(self):
        data = sl4_hook_ds_bar_data(k)
        assert data["source_partition"] == (2, 1, 1)
        assert data["transpose_partition"] == (3, 1)
        assert simplify(data["formal_reflected_level"] + k + 8) == 0
        assert simplify(data["formal_central_sum"] - (188 + 18 * k)) == 0
        assert data["minimal_check"].w_generators == 9
        assert data["minimal_check"].w_num_even == 9
        assert data["subregular_check"].w_generators == 5
        assert data["subregular_check"].w_num_even == 5

    def test_pair_claims_are_typed(self):
        data = sl4_hook_ds_bar_data(k)
        _assert_unresolved(data["source_kappa"], ClaimStatus.CONDITIONAL)
        _assert_unresolved(data["transpose_kappa"], ClaimStatus.CONDITIONAL)
        _assert_unresolved(data["modular_conductor"], ClaimStatus.OPEN)
        _assert_unresolved(data["duality"].koszul_duality, ClaimStatus.CONDITIONAL)


class TestFormalTransposeAndDuality:
    @pytest.mark.parametrize(
        ("partition", "transpose", "reflected_shift"),
        [
            ((2, 1), (2, 1), 6),
            ((2, 1, 1), (3, 1), 8),
            ((3, 1), (2, 1, 1), 8),
            ((3, 2), (2, 2, 1), 10),
        ],
    )
    def test_exact_formal_data(self, partition, transpose, reflected_shift):
        data = koszul_dual_identification(partition, k)
        assert isinstance(data, KoszulDualIdentification)
        assert data.dual_partition == transpose
        assert simplify(data.dual_level + k + reflected_shift) == 0
        assert data.formal_fixed_level == -sum(partition)
        assert data.self_dual_level == (
            -sum(partition) if partition == transpose else None
        )
        assert data.hasse_path_to_transpose[0] == partition
        assert data.hasse_path_to_transpose[-1] == transpose

    @pytest.mark.parametrize(
        ("partition", "expected", "constant"),
        [
            ((2, 1), 50, True),
            ((2, 1, 1), 188 + 18 * k, False),
            ((3, 1), 44 - 18 * k, False),
            ((3, 2), 110 - 18 * k, False),
        ],
    )
    def test_formal_central_sums(self, partition, expected, constant):
        data = koszul_dual_identification(partition, k)
        assert simplify(data.formal_central_sum - expected) == 0
        assert data.formal_central_sum_k_independent is constant

    @pytest.mark.parametrize("partition", [(2, 1), (2, 1, 1), (3, 1), (3, 2)])
    def test_modular_and_object_claims_are_typed(self, partition):
        data = koszul_dual_identification(partition, k)
        _assert_unresolved(data.source_rho, ClaimStatus.OPEN)
        _assert_unresolved(data.dual_rho, ClaimStatus.OPEN)
        _assert_unresolved(data.source_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.dual_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.modular_conductor, ClaimStatus.OPEN)
        _assert_unresolved(data.categorical_transport, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.bar_compatibility, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.koszul_duality, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.ksdual_membership, ClaimStatus.CONDITIONAL)
        assert not hasattr(data, "kappa_sum")


class TestAuditSurface:
    def test_exact_audit_checks_pass(self):
        audit = verify_ds_bar_commutation()
        assert isinstance(audit, DSBarAudit)
        assert audit.exact_check_count == 15
        assert audit.all_exact_checks_pass
        assert all(value for _, value in audit.exact_checks)

    def test_theorem_level_audit_claims_remain_unresolved(self):
        audit = verify_ds_bar_commutation()
        assert len(audit.claims) == 10
        assert all(
            packet.status in (ClaimStatus.OPEN, ClaimStatus.CONDITIONAL)
            for packet in audit.claims
        )
        assert all(packet.value is None for packet in audit.claims)


def test_source_excludes_legacy_promotions():
    source = Path("compute/lib/ds_bar_commutation.py").read_text()
    fragments = (
        "is_koszul=" + "True",
        "kappa_expected = rho * w_c",
        "simplify(source_kappa + dual_kappa)",
        "2 - 24 * (k + 1)",
        '"fermionic"',
        "h2_dim=4",
        "h3_dim=1",
        "kappa_sum_equals_comp",
        "N=2 superconformal algebra",
    )
    assert all(source.find(fragment) == -1 for fragment in fragments)
