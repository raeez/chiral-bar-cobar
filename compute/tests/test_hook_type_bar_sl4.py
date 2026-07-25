"""Oracle tests for the typed ``sl_4`` hook bar compatibility surface."""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.hook_type_bar_sl4 import (
    ClaimPacket,
    ClaimStatus,
    GENERATORS_211,
    GENERATORS_31,
    GENERATOR_NAMES_211,
    GENERATOR_NAMES_31,
    OpenInvariantError,
    PARTITION_211,
    PARTITION_31,
    bar_deg1_dim_211,
    bar_deg1_dim_31,
    bar_deg2_chain_dim_211,
    c_211,
    c_31,
    c_complementarity_sum,
    complementarity_constant_value,
    curvature_211,
    curvature_31,
    ds_bar_commutation_211,
    ds_bar_commutation_31,
    dual_level,
    is_chirally_koszul_211,
    kappa_211,
    kappa_31,
    kappa_anti_symmetry_sum,
    ope_fermionic_leading,
    ope_virasoro,
    ope_weight1_fermionic,
    ope_weight1_weight1,
    residual_sl2_level,
    residual_u1_level,
    vacuum_character_211,
    vacuum_character_31,
    vacuum_dim_211,
    verify_all,
    verify_ghost_constants,
    verify_partition_duality,
    verify_transport_to_transpose,
)
from compute.lib.hook_type_w_duality import krw_central_charge, w_algebra_generator_data
from compute.lib.nonprincipal_ds_orbits import transpose_partition


k = Symbol("k")


class TestExactHookArithmetic:
    def test_partition_transpose_orbit(self):
        assert transpose_partition(PARTITION_211) == PARTITION_31
        assert transpose_partition(PARTITION_31) == PARTITION_211

    def test_generator_names_and_counts(self):
        assert len(GENERATOR_NAMES_211) == len(GENERATORS_211) == 9
        assert len(GENERATOR_NAMES_31) == len(GENERATORS_31) == 5
        assert bar_deg1_dim_211() == 9
        assert bar_deg1_dim_31() == 5

    def test_generator_ledgers_are_even(self):
        assert {entry["parity"] for entry in GENERATORS_211.values()} == {"even"}
        assert {entry["parity"] for entry in GENERATORS_31.values()} == {"even"}
        assert w_algebra_generator_data(PARTITION_211).n_odd == 0
        assert w_algebra_generator_data(PARTITION_31).n_odd == 0

    def test_generator_weight_multisets(self):
        assert sorted(entry["weight"] for entry in GENERATORS_211.values()) == [
            Rational(1), Rational(1), Rational(1), Rational(1),
            Rational(3, 2), Rational(3, 2), Rational(3, 2), Rational(3, 2),
            Rational(2),
        ]
        assert sorted(entry["weight"] for entry in GENERATORS_31.values()) == [
            Rational(1), Rational(2), Rational(2), Rational(2), Rational(3),
        ]

    def test_central_charges_match_canonical_krw(self):
        assert simplify(c_211(k) - krw_central_charge(PARTITION_211, k)) == 0
        assert simplify(c_31(k) - krw_central_charge(PARTITION_31, k)) == 0

    def test_explicit_central_charge_formulas(self):
        expected_211 = (-6 * k**2 - 9 * k) / (k + 4)
        expected_31 = (-24 * k**2 - 115 * k - 136) / (k + 4)
        assert simplify(c_211(k) - expected_211) == 0
        assert simplify(c_31(k) - expected_31) == 0

    def test_formal_reflection_is_involutive(self):
        assert dual_level(k) == -k - 8
        assert simplify(dual_level(dual_level(k)) - k) == 0

    def test_formal_central_sum_is_exact_and_k_dependent(self):
        expected = simplify(c_31(k) + c_211(-k - 8))
        actual = c_complementarity_sum(k)
        assert simplify(actual - expected) == 0
        assert simplify(actual.diff(k)) != 0

    def test_signed_transpose_ghost_sum(self):
        assert complementarity_constant_value() == -9
        assert all(verify_ghost_constants().values())
        assert all(verify_partition_duality().values())


class TestTypedFrontierSurface:
    @pytest.mark.parametrize("factory", [kappa_211, kappa_31])
    def test_kappa_requires_genus_one_and_ds_comparison(self, factory):
        packet = factory(k)
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None
        with pytest.raises(OpenInvariantError):
            packet.require_value()

    def test_modular_conductor_is_open(self):
        packet = kappa_anti_symmetry_sum(k)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None

    @pytest.mark.parametrize("factory", [residual_sl2_level, residual_u1_level])
    def test_residual_levels_require_brst_normalization(self, factory):
        packet = factory(k)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None

    @pytest.mark.parametrize(
        "factory",
        [ope_weight1_weight1, ope_virasoro, ope_weight1_fermionic, ope_fermionic_leading],
    )
    def test_ope_coefficients_require_direct_calculation(self, factory):
        packet = factory()
        assert packet.status in {ClaimStatus.OPEN, ClaimStatus.CONDITIONAL}
        assert packet.value is None

    @pytest.mark.parametrize(
        "packet",
        [vacuum_character_211(6), vacuum_character_31(6), vacuum_dim_211(2)],
    )
    def test_vacuum_characters_require_pbw_and_null_control(self, packet):
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None

    def test_bar_degree_two_requires_a_completed_model(self):
        packet = bar_deg2_chain_dim_211(3)
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None

    @pytest.mark.parametrize("factory", [curvature_211, curvature_31])
    def test_curvature_requires_normalized_ope_pairings(self, factory):
        packet = factory()
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None

    @pytest.mark.parametrize("factory", [ds_bar_commutation_211, ds_bar_commutation_31])
    def test_ds_bar_commutation_is_conditional(self, factory):
        packet = factory()
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None
        assert any("H_hook^{DS/bar}" in item for item in packet.hypotheses)

    def test_koszulness_is_conditional(self):
        packet = is_chirally_koszul_211()
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None
        assert any("H_PBW^bar" in item for item in packet.hypotheses)


class TestAuditBundles:
    def test_transport_bundle_separates_exact_and_conditional_fields(self):
        audit = verify_transport_to_transpose()
        assert audit["transpose_relation"]
        assert audit["transpose_involution"]
        assert audit["source_generator_count"] == 9
        assert audit["target_generator_count"] == 5
        assert audit["formal_reflected_level"] == -k - 8
        assert audit["modular_conductor"].status is ClaimStatus.OPEN
        assert audit["ds_bar_commutation"].status is ClaimStatus.CONDITIONAL
        assert audit["koszul_duality"].status is ClaimStatus.CONDITIONAL

    def test_full_audit_exact_booleans_and_typed_claims(self):
        audit = verify_all()
        bool_values = [value for value in audit.values() if isinstance(value, bool)]
        assert bool_values
        assert all(bool_values)
        assert audit["source_all_even"]
        assert audit["target_all_even"]
        assert audit["modular_conductor"].status is ClaimStatus.OPEN
        assert audit["ds_bar_source"].status is ClaimStatus.CONDITIONAL
        assert audit["ds_bar_target"].status is ClaimStatus.CONDITIONAL
        assert audit["koszulness"].status is ClaimStatus.CONDITIONAL
