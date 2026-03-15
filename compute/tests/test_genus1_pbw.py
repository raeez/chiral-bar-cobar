"""Tests for genus-1 PBW spectral sequence verification (MC1).

Verifies the computational claims in Theorem thm:pbw-genus1-km
(higher_genus.tex:8517), Step 4: explicit verification at low weights
for sl2-hat at genus 1.
"""

import pytest
from sympy import Rational

from compute.lib.genus1_pbw_sl2 import (
    bracket_on_tensor_square,
    killing_form_element,
    adjoint_casimir_on_tensor_square,
    ce_differential_1_to_2,
    ce_differential_2_to_3,
    verify_enrichment_claims,
    verify_ce_complex,
)


# ===========================================================================
# CE complex of sl2
# ===========================================================================

class TestCEComplex:
    """Chevalley-Eilenberg complex of sl2."""

    def test_d1_rank(self):
        """d_CE: Lambda^1 -> Lambda^2 has rank 3 (injective)."""
        d1 = ce_differential_1_to_2()
        assert d1.shape == (3, 3)
        assert d1.rank() == 3

    def test_d2_zero(self):
        """d_CE: Lambda^2 -> Lambda^3 is the zero map."""
        d2 = ce_differential_2_to_3()
        assert d2.shape == (1, 3)
        assert d2.rank() == 0

    def test_d_squared_zero(self):
        """d^2 = 0 in the CE complex."""
        d1 = ce_differential_1_to_2()
        d2 = ce_differential_2_to_3()
        assert (d2 * d1).is_zero_matrix

    def test_cohomology(self):
        """H*(sl2) = (1, 0, 0, 1), Poincare polynomial 1 + t^3."""
        ce = verify_ce_complex()
        assert ce["H0"] == 1
        assert ce["H1"] == 0
        assert ce["H2"] == 0
        assert ce["H3"] == 1
        assert ce["total_betti"] == 2


# ===========================================================================
# Enrichment d_1 at weight h=2 (Step 4 of thm:pbw-genus1-km)
# ===========================================================================

class TestEnrichmentD1:
    """PBW d_1 differential on genus-1 enrichment at weight 2."""

    def test_d1_surjective(self):
        """d_1: g^{otimes 2} -> g has rank 3 (surjective)."""
        D = bracket_on_tensor_square()
        assert D.shape == (3, 9)
        assert D.rank() == 3

    def test_kernel_dim_6(self):
        """ker(d_1) has dimension 6 = dim(V_5) + dim(V_1)."""
        D = bracket_on_tensor_square()
        assert 9 - D.rank() == 6

    def test_v3_isomorphism(self):
        """V_3 = Lambda^2(g) maps isomorphically under d_1."""
        enr = verify_enrichment_claims()
        assert enr["claim_3_V3_isomorphism"]

    def test_killing_in_kernel(self):
        """The Killing form element kappa lies in ker(d_1)."""
        D = bracket_on_tensor_square()
        kappa = killing_form_element()
        result = D * kappa
        assert all(result[i] == 0 for i in range(3))

    def test_killing_is_invariant(self):
        """kappa is g-invariant (Casimir eigenvalue 0)."""
        C2 = adjoint_casimir_on_tensor_square()
        kappa = killing_form_element()
        result = C2 * kappa
        assert all(result[i] == 0 for i in range(9))


# ===========================================================================
# Casimir decomposition
# ===========================================================================

class TestCasimirDecomposition:
    """Adjoint decomposition g^{otimes 2} = V_5 + V_3 + V_1."""

    def test_eigenvalues(self):
        """Casimir eigenvalues: {12:5, 4:3, 0:1} (normalization 2j(j+1))."""
        C2 = adjoint_casimir_on_tensor_square()
        eigenvals = C2.eigenvals()
        expected = {Rational(12): 5, Rational(4): 3, Rational(0): 1}
        assert eigenvals == expected

    def test_total_dimension(self):
        """5 + 3 + 1 = 9 = dim(g^{otimes 2})."""
        C2 = adjoint_casimir_on_tensor_square()
        eigenvals = C2.eigenvals()
        assert sum(eigenvals.values()) == 9


# ===========================================================================
# d_2 (Killing contraction)
# ===========================================================================

class TestKillingContraction:
    """d_2 at E_3: Killing form contraction kills the invariant V_1."""

    def test_contraction_nonzero(self):
        """kappa^{ab} kappa_{ab} = dim(sl2) = 3, nonzero at generic k."""
        enr = verify_enrichment_claims()
        assert enr["killing_contraction_scalar"] == 3

    def test_d2_kills_invariant(self):
        """d_2(kappa tensor H^1) = k * 3 is nonzero for k != 0."""
        enr = verify_enrichment_claims()
        assert enr["claim_5_d2_nonzero"]


# ===========================================================================
# Integration: all claims together
# ===========================================================================

class TestMC1Integration:
    """Full MC1 verification: all 11 claims pass."""

    def test_all_pass(self):
        ce = verify_ce_complex()
        enr = verify_enrichment_claims()
        assert ce["claim_6_d1_rank_3"]
        assert ce["claim_7_d2_is_zero"]
        assert ce["claim_8_cohomology"]
        assert ce["d_squared_zero"]
        assert enr["claim_1_surjective"]
        assert enr["claim_2_ker_dim_6"]
        assert enr["claim_3_V3_isomorphism"]
        assert enr["claim_4_kappa_in_ker"]
        assert enr["claim_5_d2_nonzero"]
        assert enr["claim_adjoint_decomposition"]
        assert enr["claim_kappa_is_invariant"]
