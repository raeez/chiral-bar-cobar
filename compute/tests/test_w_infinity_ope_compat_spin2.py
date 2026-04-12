r"""Tests for OPE compatibility of the spectral coproduct at spin 2.

Verifies:
  (1) Psi-basis coproduct formulas Delta_z(psi_n) for n = 1, 2, 3.
  (2) Miura derivation of Delta_z(T) with CORRECT coefficient (Psi-1)/Psi on J tensor J.
  (3) Paper formula discrepancy: 1/Psi is WRONG, (Psi-1)/Psi is correct.
  (4) z=0 specialization to standard coproduct.
  (5) Counit compatibility.
  (6) OPE compatibility via RTT argument (trivial for gl_1).
  (7) Limiting behavior at special Psi values.

# VERIFIED: coefficient (Psi-1)/Psi derived from TWO independent paths:
#   [DC] Direct computation: Delta_z(T(u)) = T(u).T(u-z) expanded at u^{-2},
#        then Miura transform psi_2 = T + J^2/(2*Psi) inverted.
#   [LC] Limiting case: Psi -> inf gives coefficient 1 (classical);
#        Psi = 1 gives coefficient 0 (free boson, J.J vanishes).
#   [CF] Cross-family: agrees with psi-basis formula (coefficient 1 on
#        psi_1.psi_1 in Delta_z(psi_2)) after Miura substitution.
"""

import pytest
from sympy import Rational, Symbol, expand, limit, oo, simplify, symbols

from compute.lib.w_infinity_ope_compat_spin2 import (
    delta_T_coefficient_JJ,
    delta_T_from_miura,
    delta_psi,
    run_all,
    verify_counit,
    verify_miura_derivation,
    verify_ope_compatibility_rtt,
    verify_paper_formula_is_wrong,
    verify_psi_basis_coproduct,
    verify_z0_specialization,
)

Psi = Symbol('Psi')
z = Symbol('z')


# ============================================================================
# 1. Psi-basis coproduct formulas
# ============================================================================

class TestPsiBasisCoproduct:
    """Test Delta_z(psi_n) from the Drinfeld formula."""

    def test_delta_psi1(self):
        """Delta_z(psi_1) = psi_1.1 + 1.psi_1 (primitive)."""
        dp = delta_psi(1)
        assert dp == {(1, 0): Rational(1), (0, 1): Rational(1)}

    def test_delta_psi2(self):
        """Delta_z(psi_2) = psi_2.1 + 1.psi_2 + psi_1.psi_1 + z*(1.psi_1)."""
        dp = delta_psi(2)
        assert simplify(dp[(2, 0)] - 1) == 0
        assert simplify(dp[(0, 2)] - 1) == 0
        assert simplify(dp[(1, 1)] - 1) == 0
        assert simplify(dp[(0, 1)] - z) == 0
        assert len(dp) == 4

    def test_delta_psi3(self):
        """Delta_z(psi_3) matches eq:coprod-psi3."""
        dp = delta_psi(3)
        assert simplify(dp[(3, 0)] - 1) == 0
        assert simplify(dp[(0, 3)] - 1) == 0
        assert simplify(dp[(1, 2)] - 1) == 0
        assert simplify(dp[(2, 1)] - 1) == 0
        assert simplify(dp[(1, 1)] - z) == 0
        assert simplify(dp[(0, 2)] - 2 * z) == 0
        assert simplify(dp[(0, 1)] - z**2) == 0
        assert len(dp) == 7

    def test_psi1_is_primitive(self):
        """psi_1 has no z-dependence (truly primitive)."""
        dp = delta_psi(1)
        for coeff in dp.values():
            assert simplify(coeff.diff(z)) == 0

    def test_full_suite(self):
        """Run the full psi-basis verification."""
        results = verify_psi_basis_coproduct()
        assert results["delta_psi1_correct"]
        assert results["delta_psi2_correct"]
        assert results["delta_psi3_correct"]


# ============================================================================
# 2. Miura derivation and the CORRECTED coefficient
# ============================================================================

class TestMiuraDerivation:
    """Test Delta_z(T) derived from psi-basis via Miura transform."""

    def test_JJ_coefficient_is_1_minus_1_over_Psi(self):
        """The coefficient of J tensor J in Delta_z(T) is (Psi-1)/Psi."""
        # VERIFIED: [DC] direct computation from Drinfeld + Miura.
        # VERIFIED: [LC] Psi=1 -> 0 (free boson cross-term vanishes).
        coeff = delta_T_coefficient_JJ()
        assert simplify(coeff - (1 - 1 / Psi)) == 0

    def test_JJ_coefficient_NOT_1_over_Psi(self):
        """The paper's 1/Psi is WRONG for general Psi."""
        coeff = delta_T_coefficient_JJ()
        diff = simplify(coeff - 1 / Psi)
        assert diff != 0, "Coefficient should NOT be 1/Psi"

    def test_delta_T_full_formula(self):
        """Delta_z(T) = T.1 + 1.T + (1 - 1/Psi)*J.J + z*(1.J)."""
        dt = delta_T_from_miura()
        assert simplify(dt[("T", "1")] - 1) == 0
        assert simplify(dt[("1", "T")] - 1) == 0
        assert simplify(dt[("J", "J")] - (1 - 1 / Psi)) == 0
        assert simplify(dt[("1", "J")] - z) == 0
        # No other terms
        assert len(dt) == 4

    def test_miura_derivation_suite(self):
        """Run the full Miura derivation suite."""
        results = verify_miura_derivation()
        assert results["all_match"]

    def test_at_Psi_1(self):
        """At Psi=1 (free boson), the J.J cross-term vanishes."""
        # VERIFIED: [LC] free boson limiting case.
        coeff = delta_T_coefficient_JJ().subs(Psi, 1)
        assert coeff == 0

    def test_at_Psi_2(self):
        """At Psi=2, the coefficient is 1/2 (agrees with paper accidentally)."""
        coeff = delta_T_coefficient_JJ().subs(Psi, 2)
        assert coeff == Rational(1, 2)

    def test_at_Psi_3(self):
        """At Psi=3, the coefficient is 2/3 (paper would give 1/3)."""
        coeff = delta_T_coefficient_JJ().subs(Psi, 3)
        assert coeff == Rational(2, 3)

    def test_classical_limit(self):
        """Psi -> infinity: coefficient -> 1 (full classical cross-term)."""
        # VERIFIED: [LC] classical limit.
        coeff = delta_T_coefficient_JJ()
        assert limit(coeff, Psi, oo) == 1


# ============================================================================
# 3. Paper formula discrepancy
# ============================================================================

class TestPaperDiscrepancy:
    """Verify the discrepancy with the paper's formula."""

    def test_discrepancy_exists(self):
        """The paper's 1/Psi differs from the correct (Psi-1)/Psi."""
        results = verify_paper_formula_is_wrong()
        assert results["Psi=1"]["match"] is False
        assert results["Psi=3"]["match"] is False

    def test_accidental_agreement_at_Psi_2(self):
        """The formulas agree only at Psi=2."""
        results = verify_paper_formula_is_wrong()
        assert results["Psi=2"]["match"] is True


# ============================================================================
# 4. z=0 specialization
# ============================================================================

class TestZ0Specialization:
    """Test that z=0 gives the standard (non-spectral) coproduct."""

    def test_z0_psi1(self):
        results = verify_z0_specialization()
        assert results["psi1_z0_correct"]

    def test_z0_psi2(self):
        results = verify_z0_specialization()
        assert results["psi2_z0_correct"]

    def test_z0_psi3(self):
        results = verify_z0_specialization()
        assert results["psi3_z0_correct"]


# ============================================================================
# 5. Counit
# ============================================================================

class TestCounit:
    """Test counit compatibility: (eps . id)(Delta_z(psi_n)) = T(u-z) coefficients."""

    def test_counit_psi1(self):
        results = verify_counit()
        assert results["counit_psi1_correct"]

    def test_counit_psi2(self):
        results = verify_counit()
        assert results["counit_psi2_correct"]

    def test_counit_psi3(self):
        results = verify_counit()
        assert results["counit_psi3_correct"]


# ============================================================================
# 6. OPE compatibility via RTT
# ============================================================================

class TestOPECompatibility:
    """Test that OPE compatibility holds at all spins via RTT."""

    def test_rtt_holds(self):
        results = verify_ope_compatibility_rtt()
        assert results["holds_at_all_spins"]

    def test_no_spin_by_spin_needed(self):
        results = verify_ope_compatibility_rtt()
        assert results["no_spin_by_spin_check_needed"]


# ============================================================================
# 7. Integration test
# ============================================================================

class TestIntegration:
    """Run the full verification suite."""

    def test_all_checks_pass(self):
        results = run_all()
        # Psi-basis
        pb = results["psi_basis_coproduct"]
        assert all(pb[f"delta_psi{n}_correct"] for n in range(1, 4))
        # Miura
        assert results["miura_derivation"]["all_match"]
        # z=0
        z0 = results["z0_specialization"]
        assert all(z0[f"psi{n}_z0_correct"] for n in range(1, 4))
        # Counit
        cu = results["counit"]
        assert all(cu[f"counit_psi{n}_correct"] for n in range(1, 4))
        # RTT
        assert results["ope_compatibility_rtt"]["holds_at_all_spins"]
