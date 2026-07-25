"""Guards for the typed superconformal comparison ledger."""

from fractions import Fraction

import pytest

from compute.lib.theorem_ap49_superconformal_engine import (
    OpenSuperconformalInvariantError,
    ap48_kappa_not_c_over_2,
    bp_central_charge,
    bp_comp_sum,
    bp_comp_sum_t_line,
    bp_ff_dual_level,
    bp_generator_parities,
    bp_koszul_conductor,
    bp_reciprocal_weight_diagnostic,
    bp_shifted_secondary_central_charge,
    bp_shifted_secondary_sum,
    bp_varrho,
    check_bp_anomaly_ratio,
    check_bp_collapsing_level,
    check_bp_intra_file_contradiction,
    check_n2_cross_volume,
    check_n4_cross_volume,
    hierarchy_comp_sums_decreasing,
    kappa_bp,
    kappa_bp_t_line,
    kappa_n2_from_c,
    kappa_n2_from_level,
    kappa_n4_from_c,
    kappa_n4_from_level,
    kappa_svir,
    kappa_vir,
    multipath_bp,
    n2_central_charge,
    n2_comp_sum,
    n2_coset_decomposition,
    n2_koszul_dual_c,
    n2_level_from_c,
    n4_central_charge,
    n4_comp_sum_cy,
    n4_comp_sum_ff,
    n4_koszul_dual_c,
    svir_comp_sum,
    svir_koszul_dual_c,
    superconformal_hierarchy,
    superconformal_status_packet,
    vir_comp_sum,
    vir_koszul_dual_c,
)


F = Fraction


class TestVirasoroCertifiedLane:
    @pytest.mark.parametrize("c", [F(0), F(1), F(13), F(26), F(7, 3)])
    def test_complementarity(self, c):
        assert kappa_vir(c) == c / 2
        assert vir_koszul_dual_c(vir_koszul_dual_c(c)) == c
        assert vir_comp_sum(c) == 13

    def test_status(self):
        packet = superconformal_status_packet("Virasoro")
        assert packet["status"] == "proved"
        assert packet["K_kappa"] == 13


class TestExactParameterMaps:
    @pytest.mark.parametrize("c", [F(0), F(1), F(15, 2), F(15)])
    def test_n1_reflection_is_involutive(self, c):
        assert svir_koszul_dual_c(svir_koszul_dual_c(c)) == c

    @pytest.mark.parametrize("k", [F(0), F(1), F(2), F(7, 3)])
    def test_n2_parameter_relation_is_invertible(self, k):
        c = n2_central_charge(k)
        assert n2_level_from_c(c) == k

    def test_n2_poles_are_explicit(self):
        with pytest.raises(ValueError):
            n2_central_charge(F(-2))
        with pytest.raises(ValueError):
            n2_level_from_c(F(3))

    @pytest.mark.parametrize("c", [F(0), F(1), F(3), F(6)])
    def test_n2_reflection_is_involutive(self, c):
        assert n2_koszul_dual_c(n2_koszul_dual_c(c)) == c

    @pytest.mark.parametrize("k", [F(-2), F(0), F(1), F(5, 2)])
    def test_small_n4_parameter_relation(self, k):
        assert n4_central_charge(k) == 6 * k

    @pytest.mark.parametrize("c", [F(-24), F(-12), F(0), F(6)])
    def test_small_n4_reflection_is_involutive(self, c):
        assert n4_koszul_dual_c(n4_koszul_dual_c(c)) == c

    def test_coset_packet_stops_at_central_charge(self):
        packet = n2_coset_decomposition(F(2))
        assert packet["central_charge"] == F(3, 2)
        assert packet["kappa"] is None


class TestOpenModularLanes:
    @pytest.mark.parametrize(
        ("function", "args"),
        [
            (kappa_svir, (F(1),)),
            (svir_comp_sum, (F(1),)),
            (kappa_n2_from_c, (F(1),)),
            (kappa_n2_from_level, (F(1),)),
            (n2_comp_sum, (F(1),)),
            (kappa_n4_from_c, (F(6),)),
            (kappa_n4_from_level, (F(1),)),
            (n4_comp_sum_ff, (F(6),)),
            (n4_comp_sum_cy, (F(1),)),
            (bp_varrho, ()),
            (kappa_bp, (F(1),)),
            (bp_comp_sum, (F(1),)),
            (hierarchy_comp_sums_decreasing, ()),
            (ap48_kappa_not_c_over_2, ()),
        ],
    )
    def test_numeric_promotion_fails_loudly(self, function, args):
        with pytest.raises(OpenSuperconformalInvariantError):
            function(*args)

    def test_hierarchy_has_one_certified_modular_lane(self):
        hierarchy = superconformal_hierarchy()
        assert hierarchy["Virasoro"]["status"] == "proved"
        for family in ("N=1", "N=2", "small N=4", "BP"):
            assert hierarchy[family]["status"] == "open"

    def test_cross_volume_packets_keep_kappa_open(self):
        assert check_n2_cross_volume()["kappa"] is None
        assert check_n4_cross_volume()["kappa"] is None


class TestBershadskyPolyakovExactLane:
    @pytest.mark.parametrize(
        ("k", "c"),
        [
            (F(-3, 2), F(0)),
            (F(-1, 3), F(0)),
            (F(-1), F(1)),
            (F(-1, 2), F(2, 5)),
            (F(0), F(-1)),
            (F(1), F(-5)),
        ],
    )
    def test_standard_central_charge(self, k, c):
        assert bp_central_charge(k) == c

    def test_critical_pole(self):
        with pytest.raises(ValueError):
            bp_central_charge(F(-3))

    @pytest.mark.parametrize("k", [F(-2), F(-1), F(0), F(1), F(5)])
    def test_standard_and_shifted_sums(self, k):
        assert bp_koszul_conductor(k) == 50
        assert bp_shifted_secondary_sum(k) == 196

    def test_conformal_vector_conventions_are_distinct(self):
        assert bp_central_charge(F(-1)) == 1
        assert bp_shifted_secondary_central_charge(F(-1)) == 2

    def test_all_generators_even(self):
        assert set(bp_generator_parities().values()) == {"even"}
        assert bp_reciprocal_weight_diagnostic() == F(17, 6)

    def test_level_reflection_is_involutive(self):
        for k in (F(-2), F(0), F(1), F(5, 3)):
            assert bp_ff_dual_level(bp_ff_dual_level(k)) == k

    def test_t_line_projection_is_separate(self):
        k = F(1)
        assert kappa_bp_t_line(k) == bp_central_charge(k) / 2
        assert bp_comp_sum_t_line(k) == 25

    def test_status_reports(self):
        ratio = check_bp_anomaly_ratio()
        assert ratio["rho"] is None
        assert ratio["reciprocal_weight_diagnostic"] == F(17, 6)
        collapsing = check_bp_collapsing_level()
        assert collapsing == {"level": F(-1), "standard_c": F(1), "shifted_secondary": F(2)}
        contradiction = check_bp_intra_file_contradiction()
        assert contradiction["standard_reflection_sum"] == 50
        assert contradiction["shifted_secondary_sum"] == 196

    def test_two_exact_paths_and_open_modular_output(self):
        packet = multipath_bp(F(1))
        assert packet["central_paths_agree"] is True
        assert packet["standard_central_sum_direct"] == 50
        assert packet["shifted_secondary_sum"] == 196
        assert packet["kappa"] is None
        assert packet["K_kappa"] is None
