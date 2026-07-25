"""Exact OPE and open-invariant tests for the N=2 engine."""

import pytest
import sympy as sp

from compute.lib.n2_superconformal_shadow import (
    OpenN2ShadowError,
    kappa_n2,
    n2_F_g,
    n2_bar_diff_deg2,
    n2_central_charge,
    n2_complementarity_sum,
    n2_cross_channel_curvatures,
    n2_curvature,
    n2_curvature_ratios,
    n2_ff_dual_central_charge,
    n2_full_shadow_coefficients,
    n2_genus_table,
    n2_modular_status_packet,
    n2_nth_product,
    n2_nth_products,
    n2_ope_status_packet,
    n2_propagator_variance,
    n2_self_dual_point,
    n2_shadow_class,
    n2_shadow_data_G_line,
    n2_shadow_data_J_line,
    n2_shadow_data_T_line,
    n2_shadow_growth_rate_G_line,
    n2_shadow_growth_rate_J_line,
    n2_shadow_growth_rate_T_line,
    n2_shadow_tower_G_line,
    n2_shadow_tower_J_line,
    n2_shadow_tower_T_line,
    n2_special_values,
    sigma_n2,
    verify_all,
    verify_n2_jacobi_GGT,
    verify_n2_jacobi_JGG,
    verify_n2_jacobi_TJG,
)


c = sp.Symbol("c")
k = sp.Symbol("k")


class TestCentralParameter:
    @pytest.mark.parametrize(
        ("level", "central_charge"),
        [(1, 1), (2, sp.Rational(3, 2)), (10, sp.Rational(5, 2))],
    )
    def test_values(self, level, central_charge):
        assert n2_central_charge(level) == central_charge

    def test_reflection_sum(self):
        assert sp.simplify(n2_central_charge(k) + n2_central_charge(-k - 4)) == 6
        assert n2_ff_dual_central_charge(c) == 6 - c

    def test_pole(self):
        with pytest.raises(ValueError):
            n2_central_charge(-2)

    def test_fixed_point_packet(self):
        packet = n2_self_dual_point()
        assert packet["central_reflection_fixed_point"] == 3
        assert packet["level_reflection_fixed_point"] == -2
        assert packet["object_level_duality"] is None


class TestStandardOPEPacket:
    def test_parities(self):
        generators = n2_ope_status_packet()["generators"]
        assert generators["T"]["parity"] == "even"
        assert generators["J"]["parity"] == "even"
        assert generators["G+"]["parity"] == "odd"
        assert generators["G-"]["parity"] == "odd"

    def test_virasoro_products(self):
        assert n2_nth_product("T", "T", 3) == {"vac": c / 2}
        assert n2_nth_product("T", "T", 1) == {"T": 2}
        assert n2_nth_product("T", "T", 0) == {"dT": 1}

    def test_current_products(self):
        assert n2_nth_product("J", "J", 1) == {"vac": c / 3}
        assert n2_nth_product("J", "G+", 0) == {"G+": 1}
        assert n2_nth_product("J", "G-", 0) == {"G-": -1}

    def test_mixed_supercurrent_normalization(self):
        products = n2_nth_products()[("G+", "G-")]
        assert products[2] == {"vac": 2 * c / 3}
        assert products[1] == {"J": 2}
        assert products[0] == {"T": 2, "dJ": 1}

    def test_opposite_mixed_product(self):
        products = n2_nth_products()[("G-", "G+")]
        assert products[2] == {"vac": 2 * c / 3}
        assert products[1] == {"J": -2}
        assert products[0] == {"T": 2, "dJ": -1}

    def test_self_products_are_regular(self):
        assert n2_nth_products()[("G+", "G+")] == {}
        assert n2_nth_products()[("G-", "G-")] == {}

    def test_exact_jacobi_packets(self):
        assert all(verify_n2_jacobi_TJG().values())
        assert all(verify_n2_jacobi_JGG().values())
        assert all(verify_n2_jacobi_GGT().values())


class TestTypedLineRestrictions:
    def test_leading_ope_norms(self):
        packet = n2_curvature()
        assert packet["status"] == "leading OPE norms"
        assert packet["TT"] == c / 2
        assert packet["JJ"] == c / 3
        assert packet["G+G-"] == 2 * c / 3
        assert packet["bar_curvature"] is None

    def test_norm_ratios(self):
        assert n2_curvature_ratios()["JJ/TT"] == sp.Rational(2, 3)
        assert n2_curvature_ratios()["G+G-/TT"] == sp.Rational(4, 3)

    def test_t_line_packet(self):
        packet = n2_shadow_data_T_line(6)
        assert packet["leading_norm"] == 3
        assert packet["full_shadow"] is None

    def test_j_line_packet(self):
        packet = n2_shadow_data_J_line()
        assert packet["leading_norm"] == c / 3
        assert packet["full_shadow"] is None

    def test_g_line_packet(self):
        packet = n2_shadow_data_G_line(6)
        assert packet["leading_norm"] == 4
        assert packet["singular_products"][2]["vac"] == 4
        assert packet["full_shadow"] is None

    def test_cross_channel_packet(self):
        packet = n2_cross_channel_curvatures()
        assert packet["mixed_shadow_tensor"] is None
        assert packet["G+G-"] == 2 * c / 3


class TestOpenInvariantAPIs:
    @pytest.mark.parametrize(
        ("function", "args"),
        [
            (n2_bar_diff_deg2, ("T", "T")),
            (kappa_n2, (1,)),
            (sigma_n2, (1,)),
            (n2_complementarity_sum, (1,)),
            (n2_shadow_tower_T_line, (1,)),
            (n2_shadow_tower_J_line, (1,)),
            (n2_shadow_tower_G_line, (1,)),
            (n2_shadow_growth_rate_T_line, (1,)),
            (n2_shadow_growth_rate_J_line, ()),
            (n2_shadow_growth_rate_G_line, ()),
            (n2_F_g, (1, 1)),
            (n2_genus_table, (1,)),
            (n2_propagator_variance, (1,)),
            (n2_full_shadow_coefficients, (1,)),
        ],
    )
    def test_open_calls_fail_loudly(self, function, args):
        with pytest.raises(OpenN2ShadowError):
            function(*args)

    def test_open_status_packets(self):
        assert n2_modular_status_packet()["kappa"] is None
        assert n2_modular_status_packet()["K_kappa"] is None
        assert n2_shadow_class()["class"] is None

    def test_special_values_stop_at_central_charge(self):
        packet = n2_special_values()
        assert packet[1]["central_charge"] == 1
        assert packet[2]["central_charge"] == sp.Rational(3, 2)
        assert all(item["kappa"] is None for item in packet.values())


def test_master_report() -> None:
    report = verify_all()
    assert report["all_exact_checks_pass"] is True
    assert all(report["exact_checks"].values())
    assert report["bar_status"]["status"] == "open"
    assert report["modular_status"]["status"] == "open"
    assert report["shadow_status"]["status"] == "open"
