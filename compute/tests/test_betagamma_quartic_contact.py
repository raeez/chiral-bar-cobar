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
    betagamma_ope_residue,
    weight_changing_class_bracket,
    transferred_m3_on_weight_line,
    quartic_contact_invariant,
    verify_rank_one_rigidity,
    betagamma_kappa,
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
