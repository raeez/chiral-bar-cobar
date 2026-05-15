"""Tests for beta-gamma and bc ghost bar complex chain-level computations.

Ground truth from manuscript (beta_gamma.tex):
  OPE: beta_{(0)}gamma = 1 (simple pole only)
  Closed collision: r_coll(beta gamma) = 0, r_coll(bc) = 0, m_0 = 0
  Bar diff: D(beta⊗gamma) = 1 (vacuum), D(gamma⊗beta) = -1
  D(beta⊗beta) = 0, D(gamma⊗gamma) = 0
  Chain type count: 2·3^{n-1}
  Bare bar cohomology: Koszul-dual coalgebra, not acyclic
  Twisted Koszul resolution: H^0 = C, H^n = 0 for n >= 1
  Koszul dual: (betagamma)^! = bc ghosts, (bc)^! = betagamma
  Class C: r_max = 4, S_3 = 0, S_4 = -5/12, S_r = 0 for r >= 5
"""

import pytest
from sympy import Rational

from compute.lib.betagamma_bar import (
    betagamma_nth_product,
    betagamma_all_products,
    betagamma_bar_diff_deg2,
    betagamma_bar_diff_deg3_example,
    betagamma_chain_type_count,
    betagamma_bar_cohomology_dim,
    betagamma_koszul_dual,
    betagamma_is_koszul_acyclic,
    betagamma_bare_bar_is_acyclic,
    betagamma_twisted_koszul_resolution_is_acyclic,
    betagamma_curvature,
    betagamma_closed_collision_residue,
    bc_closed_collision_residue,
    betagamma_class_c_shadow_data,
    bc_bar_diff_deg2,
    bc_coalgebra_type,
    bc_koszul_dual,
    bc_bar_cohomology_dim,
    verify_betagamma_bar_diff,
    verify_bc_bar_diff,
    verify_chain_type_counts,
    verify_koszul_duality,
    verify_closed_collision_vs_contact,
)


class TestNthProducts:
    def test_simple_pole(self):
        """beta_{(0)}gamma = 1."""
        assert betagamma_nth_product("beta", "gamma", 0)["vac"] == Rational(1)

    def test_no_beta_beta(self):
        assert len(betagamma_nth_product("beta", "beta", 0)) == 0

    def test_no_gamma_gamma(self):
        assert len(betagamma_nth_product("gamma", "gamma", 0)) == 0

    def test_no_higher_poles(self):
        for n in [1, 2, 3]:
            assert len(betagamma_nth_product("beta", "gamma", n)) == 0

    def test_all_products_structure(self):
        prods = betagamma_all_products()
        assert ("beta", "gamma") in prods
        assert ("beta", "beta") in prods
        assert len(prods[("beta", "gamma")]) == 1  # just n=0


class TestBarDifferential:
    def test_bg_vacuum(self):
        """D(beta⊗gamma) = 1."""
        vac, bar1 = betagamma_bar_diff_deg2("beta", "gamma")
        assert vac["vac"] == Rational(1)
        assert len(bar1) == 0

    def test_gb_vacuum(self):
        """D(gamma⊗beta) = -1."""
        vac, bar1 = betagamma_bar_diff_deg2("gamma", "beta")
        assert vac["vac"] == Rational(-1)

    def test_bb_zero(self):
        """D(beta⊗beta) = 0."""
        vac, bar1 = betagamma_bar_diff_deg2("beta", "beta")
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_gg_zero(self):
        """D(gamma⊗gamma) = 0."""
        vac, bar1 = betagamma_bar_diff_deg2("gamma", "gamma")
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_bg_gb_opposite_signs(self):
        """D(bg) and D(gb) have opposite vacuum terms."""
        vac_bg, _ = betagamma_bar_diff_deg2("beta", "gamma")
        vac_gb, _ = betagamma_bar_diff_deg2("gamma", "beta")
        assert vac_bg["vac"] + vac_gb["vac"] == 0


class TestBarDiffDeg3:
    def test_structure(self):
        """D(beta1⊗beta2⊗gamma3): three collisions."""
        result = betagamma_bar_diff_deg3_example()
        assert result["D_12"]["coeff"] == Rational(0)
        assert result["D_13"]["coeff"] == Rational(1)
        assert result["D_23"]["coeff"] == Rational(-1)

    def test_d12_zero(self):
        """D_{12}: beta_{(0)}beta = 0."""
        result = betagamma_bar_diff_deg3_example()
        assert result["D_12"]["result"] == "0"


class TestChainTypeCounts:
    @pytest.mark.parametrize("n,expected", [
        (1, 2), (2, 6), (3, 18), (4, 54), (5, 162),
    ])
    def test_formula(self, n, expected):
        """rank(B-bar^n) = 2·3^{n-1}."""
        assert betagamma_chain_type_count(n) == expected

    def test_deg0(self):
        assert betagamma_chain_type_count(0) == 0


class TestBarCohomology:
    @pytest.mark.parametrize("h,expected", [
        (1, 2), (2, 4), (3, 10), (4, 26), (5, 70), (6, 192), (7, 534), (8, 1500),
    ])
    def test_bg_dims(self, h, expected):
        assert betagamma_bar_cohomology_dim(h) == expected

    @pytest.mark.parametrize("h,expected", [
        (1, 2), (2, 3), (3, 6), (4, 13), (5, 28), (6, 59), (7, 122), (8, 249),
    ])
    def test_bc_dims(self, h, expected):
        assert bc_bar_cohomology_dim(h) == expected


class TestKoszulDuality:
    def test_bg_dual_is_bc(self):
        assert betagamma_koszul_dual() == "bc_ghosts"

    def test_bc_dual_is_bg(self):
        assert bc_koszul_dual() == "beta_gamma"

    def test_involution(self):
        """(A^!)^! = A."""
        assert bc_koszul_dual() == "beta_gamma"
        assert betagamma_koszul_dual() == "bc_ghosts"

    def test_bare_bar_not_acyclic(self):
        """The bare bar cohomology is the Koszul-dual coalgebra."""
        assert betagamma_bare_bar_is_acyclic() is False
        assert betagamma_bar_cohomology_dim(1) == 2
        assert betagamma_bar_cohomology_dim(2) == 4

    def test_twisted_resolution_acyclic(self):
        """Acyclicity belongs to the twisted Koszul resolution."""
        assert betagamma_is_koszul_acyclic() is True
        assert betagamma_twisted_koszul_resolution_is_acyclic() is True


class TestCurvature:
    def test_closed_genus0_curvature_zero(self):
        curv = betagamma_curvature()
        assert curv["m0"] == Rational(0)
        assert curv["closed_collision_residue"] == Rational(0)

    def test_closed_collision_residues_zero(self):
        bg_closed = betagamma_closed_collision_residue()
        bc_closed = bc_closed_collision_residue()
        assert bg_closed["r_coll"] == Rational(0)
        assert bg_closed["m0"] == Rational(0)
        assert bc_closed["r_coll"] == Rational(0)
        assert bc_closed["m0"] == Rational(0)

    def test_simple_ope_residue_is_contact_data(self):
        """beta_{(0)}gamma = 1 remains bar-contact data."""
        curv = betagamma_curvature()
        simple_ope = betagamma_nth_product("beta", "gamma", 0)["vac"]
        assert simple_ope == Rational(1)
        assert curv["simple_ope_residue"] == simple_ope
        assert curv["bar_contact_residue"] == simple_ope
        assert curv["simple_ope_residue"] != curv["m0"]

    def test_legacy_beta_gamma_key_is_contact_data(self):
        """The legacy beta_gamma key records beta_{(0)}gamma, not m_0."""
        curv = betagamma_curvature()
        assert curv["beta_gamma"] == Rational(1)
        assert curv["beta_gamma"] == curv["bar_contact_residue"]
        assert curv["beta_gamma"] != curv["m0"]


class TestClassCShadowData:
    def test_standard_family_conventions(self):
        class_c = betagamma_class_c_shadow_data()
        assert class_c["shadow_class"] == "C"
        assert class_c["depth"] == 4
        assert class_c["S3"] == Rational(0)
        assert class_c["S4"] == Rational(-5, 12)
        assert class_c["tail_from_5"] == Rational(0)
        assert class_c["closed_collision_residue"] == Rational(0)


class TestBCGhosts:
    def test_bc_vacuum(self):
        vac, _ = bc_bar_diff_deg2("b", "c")
        assert vac["vac"] == Rational(1)

    def test_cb_vacuum(self):
        vac, _ = bc_bar_diff_deg2("c", "b")
        assert vac["vac"] == Rational(-1)

    def test_bb_zero(self):
        vac, bar1 = bc_bar_diff_deg2("b", "b")
        assert len(vac) == 0

    def test_cc_zero(self):
        vac, bar1 = bc_bar_diff_deg2("c", "c")
        assert len(vac) == 0

    def test_coalgebra_type(self):
        """Fermionic generators -> even after desuspension -> Sym^c."""
        assert bc_coalgebra_type() == "symmetric"


class TestSelfConsistency:
    def test_bg_bar_diff(self):
        for name, ok in verify_betagamma_bar_diff().items():
            assert ok, f"Failed: {name}"

    def test_bc_bar_diff(self):
        for name, ok in verify_bc_bar_diff().items():
            assert ok, f"Failed: {name}"

    def test_chain_counts(self):
        for name, ok in verify_chain_type_counts().items():
            assert ok, f"Failed: {name}"

    def test_koszul(self):
        for name, ok in verify_koszul_duality().items():
            assert ok, f"Failed: {name}"

    def test_closed_collision_vs_contact(self):
        for name, ok in verify_closed_collision_vs_contact().items():
            assert ok, f"Failed: {name}"
