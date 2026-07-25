"""Guards for the superconformal compatibility surface."""

from fractions import Fraction

import pytest

from compute.lib.theorem_ap49_superconformal_engine import (
    OpenSuperconformalInvariantError,
)
from compute.lib.theorem_sca_kappa_fix_engine import (
    kappa_n2_coset_decomposition,
    kappa_n2_from_c,
    kappa_n2_from_level,
    kappa_n4_from_c,
    kappa_n4_from_level,
    kappa_svir,
    n2_central_charge,
    n2_complementarity_sum,
    n2_kappa_multipath,
    n2_koszul_dual_c,
    n2_level_from_c,
    n4_central_charge,
    n4_complementarity_sum_cy,
    n4_complementarity_sum_ff,
    n4_kappa_multipath,
    n4_koszul_dual_c,
    superconformal_hierarchy,
    verify_n2_ap49_discrepancy,
    verify_n4_ap49_discrepancy,
)


F = Fraction


class TestExactParameterArithmetic:
    @pytest.mark.parametrize("k", [F(0), F(1), F(2), F(5, 2)])
    def test_n2_relation_and_inverse(self, k):
        c = n2_central_charge(k)
        assert n2_level_from_c(c) == k

    def test_n2_poles(self):
        with pytest.raises(ValueError):
            n2_central_charge(F(-2))
        with pytest.raises(ValueError):
            n2_level_from_c(F(3))

    @pytest.mark.parametrize("c", [F(0), F(1), F(3), F(6)])
    def test_n2_reflection(self, c):
        assert n2_koszul_dual_c(n2_koszul_dual_c(c)) == c

    @pytest.mark.parametrize("k", [F(-2), F(0), F(1), F(7, 3)])
    def test_n4_relation(self, k):
        assert n4_central_charge(k) == 6 * k

    @pytest.mark.parametrize("c", [F(-24), F(-12), F(0), F(6)])
    def test_n4_reflection(self, c):
        assert n4_koszul_dual_c(n4_koszul_dual_c(c)) == c


class TestOpenModularAPIs:
    @pytest.mark.parametrize(
        ("function", "argument"),
        [
            (kappa_n2_from_level, F(1)),
            (kappa_n2_from_c, F(1)),
            (n2_complementarity_sum, F(1)),
            (kappa_n4_from_level, F(1)),
            (kappa_n4_from_c, F(6)),
            (n4_complementarity_sum_ff, F(6)),
            (n4_complementarity_sum_cy, F(1)),
            (kappa_svir, F(1)),
        ],
    )
    def test_open_numeric_calls_fail_loudly(self, function, argument):
        with pytest.raises(OpenSuperconformalInvariantError):
            function(argument)

    def test_coset_packet_stops_before_kappa(self):
        packet = kappa_n2_coset_decomposition(F(2))
        assert packet["central_charge"] == F(3, 2)
        assert packet["kappa_total"] is None

    def test_hierarchy_statuses(self):
        hierarchy = superconformal_hierarchy()
        assert hierarchy["Virasoro"]["status"] == "proved"
        for family in ("N=1", "N=2", "small N=4", "BP"):
            assert hierarchy[family]["status"] == "open"


class TestTypedAuditReports:
    def test_n2_report(self):
        packet = verify_n2_ap49_discrepancy()
        assert packet["central_charge"] == 1
        assert packet["inverse_level"] == 1
        assert packet["kappa"] is None

    def test_n4_report(self):
        packet = verify_n4_ap49_discrepancy()
        assert packet["central_charge"] == 6
        assert packet["parameter_reflection"] == -30
        assert packet["kappa"] is None

    def test_multipath_names_open_obligation(self):
        n2 = n2_kappa_multipath(F(1))
        n4 = n4_kappa_multipath(F(1))
        assert n2["kappa"] is None and n2["paths_agree"] is None
        assert n4["kappa"] is None and n4["paths_agree"] is None
        assert n2["status"] == n4["status"] == "open modular lane"
