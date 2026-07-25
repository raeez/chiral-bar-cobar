r"""Exact arithmetic and epistemic-boundary tests for DS--ChirHoch data."""

from fractions import Fraction

import pytest

from compute.lib.ds_chirhoch_compatibility_engine import (
    DIM_SL2,
    NUM_NEG_ROOTS_SL2,
    NUM_POS_ROOTS_SL2,
    RANK_SL2,
    c_ds_sl2,
    ds_scalar_data_sl2,
    ft4_scope_report,
    kappa_km_sl2,
    kappa_vir,
    nilpotent_orbit_arithmetic_sl_n,
    nonprincipal_ds_scope_report,
    principal_ds_obligations_sl2,
    principal_ds_obligations_sl_n,
    principal_ds_scope_report,
    sl_n_data,
    transpose_partition,
    virasoro_mode_convention,
)


class TestRootArithmetic:
    """The tests in this class use matrix and root counts directly."""

    @pytest.mark.parametrize(
        ("N", "expected"),
        [
            (2, {"dim": 3, "rank": 1, "pos_roots": 1, "neg_roots": 1}),
            (3, {"dim": 8, "rank": 2, "pos_roots": 3, "neg_roots": 3}),
            (4, {"dim": 15, "rank": 3, "pos_roots": 6, "neg_roots": 6}),
            (5, {"dim": 24, "rank": 4, "pos_roots": 10, "neg_roots": 10}),
        ],
    )
    def test_small_rank_table(self, N, expected):
        data = sl_n_data(N)
        assert {key: data[key] for key in expected} == expected

    def test_sl2_constants(self):
        assert (DIM_SL2, RANK_SL2) == (3, 1)
        assert (NUM_POS_ROOTS_SL2, NUM_NEG_ROOTS_SL2) == (1, 1)

    def test_traceless_matrix_count_and_root_symmetry(self):
        for N in range(2, 12):
            data = sl_n_data(N)
            assert data["dim"] == N * N - 1
            assert data["pos_roots"] == data["neg_roots"]
            assert data["pos_roots"] == sum(range(1, N))
            assert data["dim"] == (
                data["pos_roots"] + data["rank"] + data["neg_roots"]
            )

    @pytest.mark.parametrize("value", [1, 0, -2, 2.0, True])
    def test_rank_domain(self, value):
        with pytest.raises(ValueError):
            sl_n_data(value)


class TestScalarFormulas:
    """Expected values come from direct substitution and a second form of c(k)."""

    @pytest.mark.parametrize(
        ("k", "expected_c", "expected_kappa_km", "expected_kappa_vir"),
        [
            (Fraction(-3), Fraction(25), Fraction(-3, 4), Fraction(25, 2)),
            (Fraction(-1), Fraction(1), Fraction(3, 4), Fraction(1, 2)),
            (Fraction(0), Fraction(-2), Fraction(3, 2), Fraction(-1)),
            (Fraction(1), Fraction(-7), Fraction(9, 4), Fraction(-7, 2)),
            (Fraction(2), Fraction(-25, 2), Fraction(3), Fraction(-25, 4)),
        ],
    )
    def test_direct_values(self, k, expected_c, expected_kappa_km, expected_kappa_vir):
        data = ds_scalar_data_sl2(k)
        assert data["c"] == expected_c
        assert data["kappa_km"] == expected_kappa_km
        assert data["kappa_vir"] == expected_kappa_vir

    def test_alternative_central_charge_formula(self):
        levels = (
            Fraction(-3),
            Fraction(-3, 2),
            Fraction(-1),
            Fraction(0),
            Fraction(4, 3),
            Fraction(5),
        )
        for k in levels:
            t = k + 2
            expected = Fraction(13) - 6 * (t + 1 / t)
            assert c_ds_sl2(k) == expected

    def test_feigin_fuchs_level_involution(self):
        for t in (Fraction(-3), Fraction(-1, 2), Fraction(2, 3), Fraction(3), Fraction(7, 2)):
            k = t - 2
            dual_k = 1 / t - 2
            assert c_ds_sl2(k) == c_ds_sl2(dual_k)

    def test_critical_pole(self):
        with pytest.raises(ValueError):
            c_ds_sl2(Fraction(-2))

    def test_kappa_formulas_are_exact_linear_maps(self):
        assert kappa_km_sl2(Fraction(-2)) == 0
        assert kappa_km_sl2(Fraction(2, 3)) == 2
        assert kappa_vir(Fraction(0)) == 0
        assert kappa_vir(Fraction(13)) == Fraction(13, 2)


class TestOpenChainMapObligations:
    """Root sectors are exact; the cohomological images remain explicit data."""

    def test_sl2_sectors_and_weights(self):
        obligations = principal_ds_obligations_sl2()
        assert tuple(item.sector for item in obligations) == (
            "positive_root_h_weight_2",
            "cartan_h_weight_0",
            "negative_root_h_weight_minus_2",
        )
        assert tuple(item.multiplicity for item in obligations) == (1, 1, 1)

    def test_every_sl2_image_requires_a_chain_map(self):
        for obligation in principal_ds_obligations_sl2():
            assert obligation.epistemic_status == "open_chain_map_obligation"
            assert obligation.induced_chain_map is None
            assert obligation.target_cocycle is None
            assert obligation.null_homotopy is None
            assert obligation.inner_witness is None
            assert obligation.required_data

    def test_general_sector_counts_are_root_arithmetic_only(self):
        obligations = principal_ds_obligations_sl_n(6)
        assert tuple(item.multiplicity for item in obligations) == (15, 5, 15)
        assert all(item.induced_chain_map is None for item in obligations)

    def test_conformal_mode_convention(self):
        convention = virasoro_mode_convention()
        assert convention["conformal_vector_zero_mode"] == "omega_(0) = L_(-1)"
        assert convention["conformal_vector_grading_mode"] == "omega_(1) = L_0"
        assert "z d_z" in convention["grading_commutator"]
        assert convention["cartan_to_target_chain_map"] is None
        assert convention["inner_witness_for_l0"] is None

    def test_screening_ambient_is_explicit(self):
        screening = principal_ds_obligations_sl2()[2]
        assert "free-field extension" in screening.natural_ambient
        assert screening.inner_witness is None

    def test_principal_scope_report_keeps_derived_dimensions_open(self):
        report = principal_ds_scope_report(4)
        assert report["epistemic_status"] == "root_arithmetic_proved_chain_map_open"
        assert report["root_decomposition_identity"] is True
        assert report["root_decomposition_total"] == 15
        assert report["source_chirhoch1_dimension"] is None
        assert report["target_chirhoch1_dimension"] is None
        assert report["induced_chirhoch1_map"] is None
        assert report["brst_image"] is None
        assert report["cartan_image"] is None
        assert report["screening_image"] is None

    def test_ft4_is_a_scope_report(self):
        report = ft4_scope_report()
        assert report["epistemic_status"] == "arithmetic_proved_chain_map_open"
        assert report["root_arithmetic"]["dim"] == 3
        assert report["ft4_outcome"] is None
        assert report["chirhoch_source"] is None
        assert report["chirhoch_target"] is None
        assert report["induced_map"] is None
        assert set(report["scalar_data"]) == {
            Fraction(1),
            Fraction(2),
            Fraction(3),
            Fraction(5),
            Fraction(10),
            Fraction(-3),
        }


class TestNilpotentOrbitArithmetic:
    """Partition tests use Young-diagram column counts as the oracle."""

    @pytest.mark.parametrize(
        ("partition", "transpose"),
        [
            ((4,), (1, 1, 1, 1)),
            ((3, 1), (2, 1, 1)),
            ((2, 2), (2, 2)),
            ((2, 1, 1), (3, 1)),
            ((1, 1, 1, 1), (4,)),
        ],
    )
    def test_transpose_partition(self, partition, transpose):
        assert transpose_partition(partition) == transpose

    def test_principal_orbit_sl3(self):
        data = nilpotent_orbit_arithmetic_sl_n(3, (3,))
        assert data.transpose_partition == (1, 1, 1)
        assert data.dim_nilpotent_centralizer_sl_n == 2
        assert data.dim_orbit == 6
        assert data.half_orbit_dimension == 3
        assert data.dim_reductive_triple_centralizer_sl_n == 0
        assert data.dim_center_reductive_triple_centralizer == 0

    def test_subregular_orbit_sl3(self):
        data = nilpotent_orbit_arithmetic_sl_n(3, (2, 1))
        assert data.transpose_partition == (2, 1)
        assert data.block_multiplicities == ((2, 1), (1, 1))
        assert data.dim_nilpotent_centralizer_sl_n == 4
        assert data.dim_orbit == 4
        assert data.half_orbit_dimension == 2
        assert data.dim_reductive_triple_centralizer_sl_n == 1
        assert data.dim_center_reductive_triple_centralizer == 1

    def test_zero_orbit_sl3(self):
        data = nilpotent_orbit_arithmetic_sl_n(3, (1, 1, 1))
        assert data.transpose_partition == (3,)
        assert data.block_multiplicities == ((1, 3),)
        assert data.dim_nilpotent_centralizer_sl_n == 8
        assert data.dim_orbit == 0
        assert data.dim_reductive_triple_centralizer_sl_n == 8
        assert data.dim_center_reductive_triple_centralizer == 0

    def test_minimal_orbit_sl4(self):
        data = nilpotent_orbit_arithmetic_sl_n(4, (2, 1, 1))
        assert data.transpose_partition == (3, 1)
        assert data.dim_nilpotent_centralizer_sl_n == 9
        assert data.dim_orbit == 6
        assert data.half_orbit_dimension == 3
        assert data.dim_reductive_triple_centralizer_sl_n == 4
        assert data.dim_center_reductive_triple_centralizer == 1

    def test_partition_validation(self):
        with pytest.raises(ValueError):
            nilpotent_orbit_arithmetic_sl_n(4, (3,))
        with pytest.raises(ValueError):
            nilpotent_orbit_arithmetic_sl_n(4, (1, 3))
        with pytest.raises(ValueError):
            nilpotent_orbit_arithmetic_sl_n(4, (2, 0, 2))

    def test_nonprincipal_report_keeps_chirhoch_formula_open(self):
        report = nonprincipal_ds_scope_report(4, (3, 1))
        assert report["epistemic_status"] == "orbit_arithmetic_proved_chain_map_open"
        # lambda'=(2,1,1), hence dim O_lambda=4^2-(2^2+1^2+1^2)=10.
        assert report["arithmetic"].dim_orbit == 10
        assert report["source_chirhoch1_dimension"] is None
        assert report["target_chirhoch1_dimension"] is None
        assert report["induced_chirhoch1_map"] is None
        assert report["conditional_target_formula"] is None
        assert len(report["required_data"]) == 4
