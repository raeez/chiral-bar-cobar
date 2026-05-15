"""Tests for compute/lib/betagamma_quartic_contact.py.

Key mathematical result: mu_{bg} = 0 (quartic contact invariant vanishes
on the weight-changing line of the beta-gamma system).

Two independent arguments:
  (1) Homotopy transfer: m_2(eta,eta)=0 => m_3(eta,eta,eta)=0
  (2) Rank-one abelian rigidity (Thm thm:nms-rank-one-rigidity)
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.betagamma_quartic_contact import (
    bc_closed_collision_residue,
    bc_contact_transport_data,
    bc_simple_ope_residue,
    betagamma_class_c_shadow_data,
    betagamma_closed_collision_residue,
    betagamma_contact_transport_data,
    betagamma_ope_residue,
    betagamma_simple_ope_residue,
    weight_changing_class_bracket,
    transferred_m3_on_weight_line,
    quartic_contact_invariant,
    verify_rank_one_rigidity,
    betagamma_kappa,
    class_c_shadow_coefficient,
    verify_all,
)


class TestOPEResidues:
    """OPE residues of the beta-gamma system."""

    def test_beta_gamma_residue(self):
        assert betagamma_ope_residue("beta", "gamma") == Rational(1)

    def test_gamma_beta_residue(self):
        assert betagamma_ope_residue("gamma", "beta") == Rational(-1)

    def test_beta_beta_regular(self):
        assert betagamma_ope_residue("beta", "beta") == Rational(0)

    def test_gamma_gamma_regular(self):
        assert betagamma_ope_residue("gamma", "gamma") == Rational(0)

    def test_antisymmetry(self):
        """OPE residue is antisymmetric: Res(a,b) = -Res(b,a)."""
        for a, b in [("beta", "gamma"), ("gamma", "beta")]:
            assert betagamma_ope_residue(a, b) == -betagamma_ope_residue(b, a)

    def test_legacy_wrapper_matches_simple_ope_contact_residue(self):
        """Legacy betagamma_ope_residue remains the simple OPE/contact lane."""
        for a in ["beta", "gamma"]:
            for b in ["beta", "gamma"]:
                assert betagamma_ope_residue(a, b) == betagamma_simple_ope_residue(a, b)


class TestClosedCollisionResidues:
    """Closed collision curvature residues vanish separately from OPE residues."""

    def test_betagamma_closed_collision_and_m0_vanish(self):
        assert betagamma_closed_collision_residue() == {
            "r_coll": Rational(0),
            "m0": Rational(0),
        }

    def test_bc_closed_collision_and_m0_vanish(self):
        assert bc_closed_collision_residue() == {
            "r_coll": Rational(0),
            "m0": Rational(0),
        }

    def test_betagamma_contact_residue_survives_closed_collision_zero(self):
        contact = betagamma_contact_transport_data()
        closed = betagamma_closed_collision_residue()

        assert contact["simple_ope_residue"] == Rational(1)
        assert contact["bar_contact_residue"] == Rational(1)
        assert contact["beta_gamma"] == betagamma_ope_residue("beta", "gamma")
        assert contact["closed_collision_residue"] == closed["r_coll"] == Rational(0)
        assert contact["m0"] == closed["m0"] == Rational(0)
        assert contact["simple_ope_residue"] != contact["closed_collision_residue"]
        assert contact["bar_contact_residue"] != contact["m0"]

    def test_bc_contact_residue_survives_closed_collision_zero(self):
        contact = bc_contact_transport_data()
        closed = bc_closed_collision_residue()

        assert bc_simple_ope_residue("b", "c") == Rational(1)
        assert bc_simple_ope_residue("c", "b") == Rational(-1)
        assert contact["simple_ope_residue"] == Rational(1)
        assert contact["bar_contact_residue"] == Rational(1)
        assert contact["b_c"] == bc_simple_ope_residue("b", "c")
        assert contact["closed_collision_residue"] == closed["r_coll"] == Rational(0)
        assert contact["m0"] == closed["m0"] == Rational(0)
        assert contact["simple_ope_residue"] != contact["closed_collision_residue"]
        assert contact["bar_contact_residue"] != contact["m0"]


class TestClassCConventionData:
    """Class-C shadow constants are finite-depth contact data."""

    def test_class_c_shadow_record_has_standard_constants(self):
        data = betagamma_class_c_shadow_data()

        assert data["shadow_class"] == "C"
        assert data["r_max"] == 4
        assert data["depth"] == 4
        assert data["S3"] == data["S_3"] == Rational(0)
        assert data["S4"] == data["S_4"] == Rational(-5, 12)
        assert data["tail_from_5"] == data["S_r_ge_5"] == Rational(0)

    def test_class_c_shadow_coefficients_by_arity(self):
        assert class_c_shadow_coefficient(3) == Rational(0)
        assert class_c_shadow_coefficient(4) == Rational(-5, 12)
        for arity in range(5, 11):
            assert class_c_shadow_coefficient(arity) == Rational(0)

    def test_class_c_shadow_undefined_below_arity_three(self):
        with pytest.raises(ValueError, match="defined for r >= 3"):
            class_c_shadow_coefficient(2)

    def test_class_c_shadow_not_closed_collision_curvature(self):
        data = betagamma_class_c_shadow_data()
        closed = betagamma_closed_collision_residue()

        assert data["closed_collision_residue"] == closed["r_coll"] == Rational(0)
        assert closed["m0"] == Rational(0)
        assert data["S_4"] == Rational(-5, 12)
        assert data["S_4"] != data["closed_collision_residue"]
        assert data["S_4"] != closed["m0"]


class TestWeightChangingBracket:
    """[eta, eta] = m_2(eta, eta) = 0 on the weight-changing subspace."""

    def test_bracket_vanishes(self):
        assert weight_changing_class_bracket() == Rational(0)


class TestHomotopyTransferM3:
    """m_3(eta, eta, eta) = 0 via the homotopy transfer formula."""

    def test_m3_vanishes(self):
        assert transferred_m3_on_weight_line() == Rational(0)


class TestQuarticContactInvariant:
    """The main result: mu_{bg} = <eta, m_3(eta,eta,eta)> = 0."""

    def test_mu_bg_vanishes(self):
        """KEY RESULT: quartic contact invariant mu_{bg} = 0."""
        assert quartic_contact_invariant() == Rational(0)

    def test_mu_bg_is_rational(self):
        mu = quartic_contact_invariant()
        assert isinstance(mu, Rational)


class TestRankOneRigidity:
    """Rank-one abelian rigidity verification for beta-gamma."""

    def test_all_rigidity_checks_pass(self):
        results = verify_rank_one_rigidity()
        for name, ok in results.items():
            assert ok, f"Rigidity check failed: {name}"

    def test_ell2_vanishes(self):
        results = verify_rank_one_rigidity()
        assert results["ell_2(eta,eta) = 0"]

    def test_ell3_vanishes(self):
        results = verify_rank_one_rigidity()
        assert results["ell_3(eta,eta,eta) = 0"]

    def test_quartic_shadow_vanishes(self):
        results = verify_rank_one_rigidity()
        assert results["Sh_4 = Q_{bg}(eta,eta,eta,eta) = mu_bg = 0"]

    def test_weight_shift_line_formally_linear(self):
        results = verify_rank_one_rigidity()
        assert results["Weight-shift line is formally linear"]

    def test_rigidity_report_includes_closed_collision_contact_separation(self):
        results = verify_rank_one_rigidity()
        required = [
            "beta-gamma closed collision residue = 0",
            "bc closed collision residue = 0",
            "simple OPE residue remains contact data",
            "bc simple OPE residue remains contact data",
            "class C: r_max=4, S3=0, S4=-5/12, tail=0",
        ]

        for name in required:
            assert results[name], f"Rigidity separation check failed: {name}"


class TestBetagammaKappa:
    """Obstruction coefficient kappa(bg, lambda) = 6*lambda^2 - 6*lambda + 1."""

    def test_kappa_symbolic(self):
        lam = Symbol('lambda')
        k = betagamma_kappa(lam)
        assert k == 6 * lam**2 - 6 * lam + 1

    def test_kappa_lambda_0(self):
        """lambda=0: c = 2*kappa = 2."""
        assert betagamma_kappa(0) == 1

    def test_kappa_lambda_half(self):
        """lambda=1/2 (symplectic): kappa = 6/4 - 3 + 1 = -1/2."""
        assert betagamma_kappa(Rational(1, 2)) == Rational(-1, 2)

    def test_kappa_lambda_1(self):
        """lambda=1: kappa = 6 - 6 + 1 = 1."""
        assert betagamma_kappa(1) == 1

    def test_kappa_quadratic(self):
        """kappa is a degree-2 polynomial in lambda."""
        lam = Symbol('lambda')
        k = betagamma_kappa(lam)
        assert k.as_poly(lam).degree() == 2


class TestVerifyAll:
    """Integration test: verify_all runs without error and all checks pass."""

    def test_verify_all_passes(self):
        results = verify_all()
        assert all(results.values()), "Some verify_all checks failed"

    def test_verify_all_reports_contact_curvature_separation(self):
        results = verify_all()
        required = [
            "beta-gamma r_coll = 0",
            "beta-gamma m0 = 0",
            "bc r_coll = 0",
            "simple OPE residue = 1",
            "simple OPE residue is not m0",
            "bc simple OPE residue = 1",
            "bc simple OPE residue is not m0",
            "class C S4 = -5/12",
            "class C tail vanishes from arity 5",
        ]

        for name in required:
            assert results[name], f"verify_all separation check failed: {name}"
