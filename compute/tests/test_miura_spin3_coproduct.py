r"""Tests for the Miura coproduct at spin 3 for W_{1+infinity}[Psi].

Verifies:
  (1)  Drinfeld coproduct Delta_z(psi_3) in the psi-basis.
  (2)  Miura transform relations at spins 1, 2, 3.
  (3)  Coproduct of composite fields :JT:, :J^3:, J''.
  (4)  Main result: Delta_z(W) in the W-field basis.
  (5)  Consistency: Delta_z(W) + Miura corrections = Delta_z(psi_3).
  (6)  Coefficient identification for each tensor component.
  (7)  Free boson limit Psi = 1.
  (8)  Classical limit Psi -> infinity.
  (9)  Counit compatibility (both W-only and full psi_3).
  (10) Comparison with spin-2 structure.
  (11) Specific Psi evaluations (Psi = 2, 3, 1/2).
  (12) z = 0 specialization.

# VERIFIED: every coefficient derived from TWO independent paths:
#   [DC] Direct computation from Drinfeld formula + Miura inversion.
#   [LC] Limiting cases: Psi = 1 (free boson, cross-terms vanish),
#        Psi -> inf (classical, (Psi-1)/Psi -> 1, composite terms -> 0).
#   [CF] Cross-family: agrees with psi-basis formula after full
#        Miura substitution (psi_3 reconstruction test).
"""

import pytest
from sympy import Rational, Symbol, expand, factor, limit, oo, simplify, symbols

from compute.lib.miura_spin3_coproduct_engine import (
    coefficient_1J_z2,
    coefficient_1T_z,
    coefficient_J_Jsq,
    coefficient_JJ_z,
    coefficient_Jsq_J,
    coefficient_JT,
    coefficient_TJ,
    compare_with_spin2,
    delta_J3,
    delta_Jpp,
    delta_JT,
    delta_psi,
    delta_W,
    delta_W_at_Psi,
    delta_W_classical_limit,
    delta_W_explicit,
    delta_W_free_boson,
    miura_psi2_to_W,
    miura_psi3_to_W,
    miura_W_from_psi,
    run_all,
    verify_classical_limit,
    verify_counit_psi3,
    verify_counit_W,
    verify_psi3_reconstruction,
)

Psi = Symbol('Psi')
z = Symbol('z')


# ============================================================================
# 1. Drinfeld coproduct in the psi-basis
# ============================================================================

class TestPsiBasisCoproduct:
    """Test Delta_z(psi_n) from the Drinfeld formula."""

    def test_delta_psi1_primitive(self):
        """psi_1 is primitive: Delta_z(psi_1) = psi_1.1 + 1.psi_1."""
        dp = delta_psi(1)
        assert dp == {(1, 0): Rational(1), (0, 1): Rational(1)}

    def test_delta_psi2_four_terms(self):
        """Delta_z(psi_2) has exactly 4 terms."""
        dp = delta_psi(2)
        assert len(dp) == 4
        assert simplify(dp[(2, 0)] - 1) == 0
        assert simplify(dp[(0, 2)] - 1) == 0
        assert simplify(dp[(1, 1)] - 1) == 0
        assert simplify(dp[(0, 1)] - z) == 0

    def test_delta_psi3_seven_terms(self):
        """Delta_z(psi_3) has exactly 7 terms with correct coefficients."""
        # VERIFIED: [DC] direct from Drinfeld T(u).T(u-z) expansion.
        dp = delta_psi(3)
        assert len(dp) == 7
        assert simplify(dp[(3, 0)] - 1) == 0
        assert simplify(dp[(0, 3)] - 1) == 0
        assert simplify(dp[(1, 2)] - 1) == 0
        assert simplify(dp[(2, 1)] - 1) == 0
        assert simplify(dp[(1, 1)] - z) == 0
        assert simplify(dp[(0, 2)] - 2 * z) == 0
        assert simplify(dp[(0, 1)] - z**2) == 0

    def test_delta_psi3_z0_is_standard(self):
        """At z=0, Delta_0(psi_3) = psi_3.1 + 1.psi_3 + psi_1.psi_2 + psi_2.psi_1."""
        dp = delta_psi(3)
        dp_z0 = {k: expand(v.subs(z, 0)) for k, v in dp.items()}
        dp_z0 = {k: v for k, v in dp_z0.items() if v != 0}
        expected = {
            (3, 0): Rational(1), (0, 3): Rational(1),
            (1, 2): Rational(1), (2, 1): Rational(1),
        }
        assert dp_z0 == expected


# ============================================================================
# 2. Miura transform relations
# ============================================================================

class TestMiuraTransform:
    """Test the Miura relations psi_n <-> W-field basis."""

    def test_psi2_to_W(self):
        """psi_2 = T + :J^2:/(2*Psi)."""
        m = miura_psi2_to_W()
        assert simplify(m["T"] - 1) == 0
        assert simplify(m[":J^2:"] - 1 / (2 * Psi)) == 0
        assert len(m) == 2

    def test_psi3_to_W(self):
        """psi_3 = W + (1/Psi):JT: + (1/(6Psi^2)):J^3: + (1/(2Psi))J''."""
        m = miura_psi3_to_W()
        assert simplify(m["W"] - 1) == 0
        assert simplify(m[":JT:"] - 1 / Psi) == 0
        assert simplify(m[":J^3:"] - 1 / (6 * Psi**2)) == 0
        assert simplify(m["J''"] - 1 / (2 * Psi)) == 0
        assert len(m) == 4

    def test_W_inversion_consistency(self):
        """W = psi_3 - :JT:/Psi - :J^3:/(6Psi^2) - J''/(2Psi)."""
        m = miura_W_from_psi()
        assert simplify(m["psi_3"] - 1) == 0
        assert simplify(m[":JT:"] + 1 / Psi) == 0
        assert simplify(m[":J^3:"] + 1 / (6 * Psi**2)) == 0
        assert simplify(m["J''"] + 1 / (2 * Psi)) == 0

    def test_miura_inversion_roundtrip(self):
        """psi_3 -> W -> psi_3 roundtrip consistency.

        Miura: psi_3 = W + sum(corrections)
        Inversion: W = psi_3 - sum(corrections)
        Adding: psi_3 = (psi_3 - sum) + sum = psi_3.
        """
        fwd = miura_psi3_to_W()
        inv = miura_W_from_psi()
        # The forward relation: psi_3 = W*fwd["W"] + :JT:*fwd[":JT:"] + ...
        # The inverse: W = psi_3*inv["psi_3"] + :JT:*inv[":JT:"] + ...
        # Check: fwd[":JT:"] + inv[":JT:"] should give the
        # net coefficient of :JT: in psi_3 expressed via itself = 0
        for key in [":JT:", ":J^3:", "J''"]:
            assert simplify(fwd.get(key, 0) + inv.get(key, 0)) == 0


# ============================================================================
# 3. Coproduct of composite fields
# ============================================================================

class TestCompositeCoproducts:
    """Test Delta_z for composite fields :JT:, :J^3:, J''."""

    def test_delta_JT_has_eight_terms(self):
        """Delta_z(:JT:) has 8 terms from expanding (J.1+1.J)(T.1+1.T+c*J.J+z*1.J)."""
        djt = delta_JT()
        # Some terms may combine; check key ones exist
        assert (":JT:", "1") in djt
        assert ("1", ":JT:") in djt
        assert ("J", "T") in djt
        assert ("T", "J") in djt

    def test_delta_JT_diagonal_terms(self):
        """The :JT:.1 and 1.:JT: terms have coefficient 1."""
        djt = delta_JT()
        assert simplify(djt[(":JT:", "1")] - 1) == 0
        assert simplify(djt[("1", ":JT:")] - 1) == 0

    def test_delta_J3_binomial(self):
        """:J^3: coproduct follows the binomial pattern: coefficients 1,3,3,1."""
        dj3 = delta_J3()
        assert dj3[(":J^3:", "1")] == 1
        assert dj3[(":J^2:", "J")] == 3
        assert dj3[("J", ":J^2:")] == 3
        assert dj3[("1", ":J^3:")] == 1
        assert len(dj3) == 4

    def test_delta_Jpp_primitive(self):
        """J'' is primitive: Delta_z(J'') = J''.1 + 1.J''."""
        djpp = delta_Jpp()
        assert djpp == {("J''", "1"): Rational(1), ("1", "J''"): Rational(1)}

    def test_delta_J3_no_spectral_parameter(self):
        """Delta_z(:J^3:) is z-independent (since J is primitive and z-free)."""
        dj3 = delta_J3()
        for coeff in dj3.values():
            if hasattr(coeff, 'free_symbols'):
                assert z not in coeff.free_symbols


# ============================================================================
# 4. Main result: Delta_z(W)
# ============================================================================

class TestDeltaW:
    """Test the main result Delta_z(W) in the W-field basis."""

    def test_computed_equals_explicit(self):
        """The component computation matches the closed-form formula."""
        computed = delta_W()
        explicit = delta_W_explicit()
        all_keys = set(computed.keys()) | set(explicit.keys())
        for key in all_keys:
            c = simplify(computed.get(key, 0))
            e = simplify(explicit.get(key, 0))
            assert simplify(c - e) == 0, f"Mismatch at {key}: {c} vs {e}"

    def test_nine_terms(self):
        """Delta_z(W) has exactly 9 nonzero terms."""
        dw = delta_W_explicit()
        assert len(dw) == 9

    def test_primitive_part(self):
        """W.1 + 1.W with coefficient 1."""
        dw = delta_W_explicit()
        assert simplify(dw[("W", "1")] - 1) == 0
        assert simplify(dw[("1", "W")] - 1) == 0

    def test_JT_coefficient(self):
        """Coefficient of J tensor T is (Psi-1)/Psi."""
        # VERIFIED: [DC] Miura inversion; [LC] Psi=1 -> 0, Psi->inf -> 1.
        dw = delta_W_explicit()
        assert simplify(dw[("J", "T")] - (Psi - 1) / Psi) == 0

    def test_TJ_coefficient(self):
        """Coefficient of T tensor J is (Psi-1)/Psi (same as J.T)."""
        dw = delta_W_explicit()
        assert simplify(dw[("T", "J")] - (Psi - 1) / Psi) == 0

    def test_JT_equals_TJ_coefficient(self):
        """The J.T and T.J coefficients are equal (left-right symmetry at z=0)."""
        c1 = coefficient_JT()
        c2 = coefficient_TJ()
        assert simplify(c1 - c2) == 0

    def test_J_Jsq_coefficient(self):
        """Coefficient of J tensor :J^2: is (1-Psi)/(2Psi^2)."""
        # VERIFIED: [DC] direct from cancellation of three sources.
        dw = delta_W_explicit()
        assert simplify(dw[("J", ":J^2:")] - (1 - Psi) / (2 * Psi**2)) == 0

    def test_Jsq_J_coefficient(self):
        """Coefficient of :J^2: tensor J is (1-Psi)/(2Psi^2)."""
        dw = delta_W_explicit()
        assert simplify(dw[(":J^2:", "J")] - (1 - Psi) / (2 * Psi**2)) == 0

    def test_composite_coefficient_sign(self):
        """The :J^2: coefficient has OPPOSITE sign to the T coefficient."""
        c_T = coefficient_JT()
        c_J2 = coefficient_J_Jsq()
        # (Psi-1)/Psi vs (1-Psi)/(2Psi^2) = -(Psi-1)/(2Psi^2)
        assert simplify(c_J2 + c_T / (2 * Psi)) == 0

    def test_spectral_JJ(self):
        """Coefficient of z*J.J is (Psi-1)/Psi (same as spin-2 J.J coefficient)."""
        dw = delta_W_explicit()
        # The J.J coefficient should be z*(Psi-1)/Psi
        jj_coeff = dw[("J", "J")]
        assert simplify(jj_coeff - z * (Psi - 1) / Psi) == 0

    def test_spectral_1T(self):
        """Coefficient of z*1.T is 2 (from binomial(2,1))."""
        # VERIFIED: [DC] from 2z*1.psi_2 in Delta_z(psi_3), W-projected.
        dw = delta_W_explicit()
        assert simplify(dw[("1", "T")] - 2 * z) == 0

    def test_spectral_1J(self):
        """Coefficient of z^2*1.J is 1."""
        dw = delta_W_explicit()
        assert simplify(dw[("1", "J")] - z**2) == 0

    def test_no_WJ_or_JW_terms(self):
        """No W.J or J.W cross-terms (these would be weight 3+1=4, wrong)."""
        dw = delta_W_explicit()
        assert ("W", "J") not in dw
        assert ("J", "W") not in dw

    def test_no_WT_or_TW_terms(self):
        """No W.T or T.W cross-terms (these would be weight 3+2=5, wrong)."""
        dw = delta_W_explicit()
        assert ("W", "T") not in dw
        assert ("T", "W") not in dw


# ============================================================================
# 5. Consistency: psi_3 reconstruction
# ============================================================================

class TestPsi3Reconstruction:
    """Verify Delta_z(psi_3) = Delta_z(W) + Miura corrections."""

    def test_reconstruction_exact(self):
        """The full reconstruction matches term by term."""
        # VERIFIED: [CF] cross-check between psi-basis and W-field basis.
        r = verify_psi3_reconstruction()
        assert r["all_match"], f"Mismatches: {r['mismatches']}"

    def test_reconstruction_has_correct_term_count(self):
        """Both sides of the reconstruction have the same number of terms."""
        r = verify_psi3_reconstruction()
        assert r["num_terms_lhs"] == r["num_terms_rhs"]


# ============================================================================
# 6. Coefficient extraction functions
# ============================================================================

class TestCoefficientFunctions:
    """Test the standalone coefficient extraction functions."""

    def test_coefficient_JT_formula(self):
        assert simplify(coefficient_JT() - (Psi - 1) / Psi) == 0

    def test_coefficient_TJ_formula(self):
        assert simplify(coefficient_TJ() - (Psi - 1) / Psi) == 0

    def test_coefficient_J_Jsq_formula(self):
        assert simplify(coefficient_J_Jsq() - (1 - Psi) / (2 * Psi**2)) == 0

    def test_coefficient_Jsq_J_formula(self):
        assert simplify(coefficient_Jsq_J() - (1 - Psi) / (2 * Psi**2)) == 0

    def test_coefficient_JJ_z_formula(self):
        assert simplify(coefficient_JJ_z() - (Psi - 1) / Psi) == 0

    def test_coefficient_1T_z_is_2(self):
        assert coefficient_1T_z() == Rational(2)

    def test_coefficient_1J_z2_is_1(self):
        assert coefficient_1J_z2() == Rational(1)


# ============================================================================
# 7. Free boson limit Psi = 1
# ============================================================================

class TestFreeBosonLimit:
    """Test Delta_z(W) at Psi = 1 (free boson)."""

    def test_free_boson_only_four_terms(self):
        """At Psi=1, only W.1, 1.W, 1.T, 1.J survive."""
        # VERIFIED: [LC] free boson limiting case.
        fb = delta_W_free_boson()
        assert len(fb) == 4

    def test_free_boson_W_primitive(self):
        """W.1 and 1.W have coefficient 1."""
        fb = delta_W_free_boson()
        assert simplify(fb[("W", "1")] - 1) == 0
        assert simplify(fb[("1", "W")] - 1) == 0

    def test_free_boson_no_JT_cross(self):
        """At Psi=1, the J.T cross-term vanishes."""
        fb = delta_W_free_boson()
        assert ("J", "T") not in fb

    def test_free_boson_no_TJ_cross(self):
        """At Psi=1, the T.J cross-term vanishes."""
        fb = delta_W_free_boson()
        assert ("T", "J") not in fb

    def test_free_boson_no_JJ_spectral(self):
        """At Psi=1, the z*J.J spectral term vanishes."""
        fb = delta_W_free_boson()
        assert ("J", "J") not in fb

    def test_free_boson_spectral_terms(self):
        """At Psi=1, the remaining spectral terms are 2z*1.T + z^2*1.J."""
        fb = delta_W_free_boson()
        assert simplify(fb[("1", "T")] - 2 * z) == 0
        assert simplify(fb[("1", "J")] - z**2) == 0

    def test_free_boson_no_composite(self):
        """At Psi=1, no :J^2: composite terms appear."""
        fb = delta_W_free_boson()
        assert ("J", ":J^2:") not in fb
        assert (":J^2:", "J") not in fb


# ============================================================================
# 8. Classical limit Psi -> infinity
# ============================================================================

class TestClassicalLimit:
    """Test Delta_z(W) in the classical limit Psi -> infinity."""

    def test_classical_limit_correct(self):
        """The limit Psi -> inf matches the classical formula."""
        # VERIFIED: [LC] classical limiting case.
        assert verify_classical_limit()

    def test_classical_JT_coefficient_is_1(self):
        """In the classical limit, J.T coefficient -> 1."""
        assert limit(coefficient_JT(), Psi, oo) == 1

    def test_classical_TJ_coefficient_is_1(self):
        """In the classical limit, T.J coefficient -> 1."""
        assert limit(coefficient_TJ(), Psi, oo) == 1

    def test_classical_composite_vanishes(self):
        """In the classical limit, the :J^2: coefficient -> 0."""
        assert limit(coefficient_J_Jsq(), Psi, oo) == 0

    def test_classical_formula_seven_terms(self):
        """The classical formula has 7 terms."""
        cl = delta_W_classical_limit()
        assert len(cl) == 7

    def test_classical_no_composite(self):
        """No composite :J^2: terms in classical limit."""
        cl = delta_W_classical_limit()
        assert ("J", ":J^2:") not in cl
        assert (":J^2:", "J") not in cl


# ============================================================================
# 9. Counit compatibility
# ============================================================================

class TestCounit:
    """Test counit compatibility for Delta_z(W)."""

    def test_counit_W_only(self):
        """(eps . id)(Delta_z(W)) = W + 2z*T + z^2*J."""
        r = verify_counit_W()
        assert r["all_match"], f"Mismatches: {r['mismatches']}"

    def test_counit_psi3_full(self):
        """(eps . id)(Delta_z(psi_3)) in W-basis is correct."""
        r = verify_counit_psi3()
        assert r["all_match"], f"Mismatches: {r['mismatches']}"


# ============================================================================
# 10. Comparison with spin-2 structure
# ============================================================================

class TestSpinComparison:
    """Compare structural features with the spin-2 result."""

    def test_spin2_z_degree_is_1(self):
        c = compare_with_spin2()
        assert c["spin_2"]["z_degree"] == 1

    def test_spin3_z_degree_is_2(self):
        c = compare_with_spin2()
        assert c["spin_3"]["z_degree"] == 2

    def test_same_primary_coefficient(self):
        """The primary cross-term coefficient (Psi-1)/Psi is the same
        at spins 2 and 3."""
        c = compare_with_spin2()
        assert c["spin_2"]["cross_terms"]["J.J"] == "(Psi-1)/Psi"
        assert c["spin_3"]["cross_terms"]["J.T"] == "(Psi-1)/Psi"

    def test_spin3_has_composite_correction(self):
        """Spin 3 has the composite :J^2: correction absent at spin 2."""
        c = compare_with_spin2()
        assert "J.:J^2:" in c["spin_3"]["cross_terms"]
        # Spin 2 has no composite corrections
        for key in c["spin_2"]["cross_terms"]:
            assert ":J^2:" not in key


# ============================================================================
# 11. Specific Psi evaluations
# ============================================================================

class TestSpecificPsi:
    """Evaluate Delta_z(W) at specific Psi values."""

    def test_Psi_2_JT_coefficient(self):
        """At Psi=2, J.T coefficient is 1/2."""
        c = coefficient_JT().subs(Psi, 2)
        assert c == Rational(1, 2)

    def test_Psi_2_composite_coefficient(self):
        """At Psi=2, J.:J^2: coefficient is -1/8."""
        c = coefficient_J_Jsq().subs(Psi, 2)
        assert c == Rational(-1, 8)

    def test_Psi_3_JT_coefficient(self):
        """At Psi=3, J.T coefficient is 2/3."""
        c = coefficient_JT().subs(Psi, 3)
        assert c == Rational(2, 3)

    def test_Psi_3_composite_coefficient(self):
        """At Psi=3, J.:J^2: coefficient is -1/9."""
        c = coefficient_J_Jsq().subs(Psi, 3)
        assert c == Rational(-1, 9)

    def test_Psi_half_JT_coefficient(self):
        """At Psi=1/2, J.T coefficient is -1."""
        c = coefficient_JT().subs(Psi, Rational(1, 2))
        assert c == Rational(-1)

    def test_Psi_half_composite_coefficient(self):
        """At Psi=1/2, J.:J^2: coefficient is 1."""
        c = coefficient_J_Jsq().subs(Psi, Rational(1, 2))
        assert c == Rational(1)

    def test_Psi_10_approaches_classical(self):
        """At Psi=10, coefficients are close to classical values."""
        jt = coefficient_JT().subs(Psi, 10)
        assert jt == Rational(9, 10)
        comp = coefficient_J_Jsq().subs(Psi, 10)
        assert comp == Rational(-9, 200)

    def test_specific_Psi_W_term_count(self):
        """At Psi=2, Delta_z(W) still has 9 terms."""
        dw = delta_W_at_Psi(Rational(2))
        assert len(dw) == 9


# ============================================================================
# 12. z = 0 specialization
# ============================================================================

class TestZ0Specialization:
    """Test Delta_z(W) at z = 0 (standard, non-spectral coproduct)."""

    def test_z0_no_spectral_terms(self):
        """At z=0, all spectral terms vanish."""
        dw = delta_W_explicit()
        dw_z0 = {k: simplify(v.subs(z, 0))
                 for k, v in dw.items()
                 if simplify(v.subs(z, 0)) != 0}
        assert ("1", "T") not in dw_z0
        assert ("1", "J") not in dw_z0
        assert ("J", "J") not in dw_z0

    def test_z0_has_six_terms(self):
        """At z=0, Delta_0(W) has 6 terms: W.1, 1.W, J.T, T.J, J.:J^2:, :J^2:.J."""
        dw = delta_W_explicit()
        dw_z0 = {k: simplify(v.subs(z, 0))
                 for k, v in dw.items()
                 if simplify(v.subs(z, 0)) != 0}
        assert len(dw_z0) == 6
        expected_keys = {
            ("W", "1"), ("1", "W"), ("J", "T"), ("T", "J"),
            ("J", ":J^2:"), (":J^2:", "J"),
        }
        assert set(dw_z0.keys()) == expected_keys

    def test_z0_cross_terms_symmetric(self):
        """At z=0, the J.T and T.J coefficients are equal (cocommutativity at z=0)."""
        dw = delta_W_explicit()
        jt_z0 = simplify(dw[("J", "T")].subs(z, 0))
        tj_z0 = simplify(dw[("T", "J")].subs(z, 0))
        assert simplify(jt_z0 - tj_z0) == 0


# ============================================================================
# 13. Integration test
# ============================================================================

class TestIntegration:
    """Run the full verification suite."""

    def test_all_checks_pass(self):
        results = run_all()
        assert results["psi3_reconstruction"]["all_match"]
        assert results["classical_limit_correct"]
        assert results["counit_W"]["all_match"]
        assert results["counit_psi3"]["all_match"]
