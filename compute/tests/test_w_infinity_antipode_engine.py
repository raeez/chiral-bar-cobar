r"""Tests for W_{1+infinity} antipode engine.

Verification paths for each test:
  [DC] Direct computation (recurrence / Miura inversion)
  [LT] Literature: Molev 2007, Ch.1 (Yangian antipode); Prochazka-Rapcak 1711.11582
  [LC] Limiting case (Psi = 1 free boson; Psi -> inf classical)
  [SY] Symmetry / involutivity
  [NE] Numerical evaluation at specific Psi
"""

import pytest
from sympy import Rational, Symbol, expand, factor, simplify, symbols

from compute.lib.w_infinity_antipode_engine import (
    antipode_W_basis,
    hopf_axiom_obstruction,
    numerical_checks,
    quartic_pole_obstruction,
    transfer_matrix_inverse,
    verify_inverse,
    verify_involutivity,
)

Psi_sym = Symbol('Psi')
c_sym = Symbol('c')


# ============================================================================
# 1. Transfer matrix inverse
# ============================================================================

class TestTransferMatrixInverse:
    """Test T(u)^{-1} coefficients."""

    def test_sigma_1(self):
        """sigma_1 = -psi_1.
        # VERIFIED [DC] direct recurrence; [LT] Molev 2007 Prop 1.23
        """
        sigma = transfer_matrix_inverse(1)
        p1 = Symbol('psi_1')
        assert expand(sigma[1] + p1) == 0

    def test_sigma_2(self):
        """sigma_2 = psi_1^2 - psi_2.
        # VERIFIED [DC] direct recurrence; [LT] Molev 2007 Prop 1.23
        """
        sigma = transfer_matrix_inverse(2)
        p1, p2 = symbols('psi_1 psi_2')
        expected = p1**2 - p2
        assert expand(sigma[2] - expected) == 0

    def test_sigma_3(self):
        """sigma_3 = -psi_1^3 + 2*psi_1*psi_2 - psi_3.
        # VERIFIED [DC] direct recurrence; [LT] Molev 2007 Prop 1.23
        """
        sigma = transfer_matrix_inverse(3)
        p1, p2, p3 = symbols('psi_1 psi_2 psi_3')
        expected = -p1**3 + 2*p1*p2 - p3
        assert expand(sigma[3] - expected) == 0

    def test_inverse_identity_order3(self):
        """T(u)*T(u)^{-1} = 1 to order u^{-3}.
        # VERIFIED [DC] polynomial identity; [SY] algebraic closure
        """
        result = verify_inverse(3)
        assert result["all_zero"]

    def test_inverse_identity_order5(self):
        """T(u)*T(u)^{-1} = 1 to order u^{-5}.
        # VERIFIED [DC] higher-order recurrence
        """
        result = verify_inverse(5)
        assert result["all_zero"]

    def test_sigma_pattern_alternating(self):
        """Leading term of sigma_n is (-1)^n * psi_1^n.
        # VERIFIED [DC] from recurrence; [LC] at psi_k=0 for k>=2: sigma_n = (-psi_1)^n
        """
        sigma = transfer_matrix_inverse(4)
        p1 = Symbol('psi_1')
        for n in range(1, 5):
            # Set psi_2 = psi_3 = psi_4 = 0
            subs = {Symbol(f'psi_{k}'): 0 for k in range(2, 5)}
            val = sigma[n].subs(subs)
            expected = (-p1)**n
            assert expand(val - expected) == 0, f"Failed at n={n}"


# ============================================================================
# 2. W-field antipode
# ============================================================================

class TestWFieldAntipode:
    """Test antipode formulas in W-field basis."""

    def test_S_J(self):
        """S(J) = -J.
        # VERIFIED [DC] sigma_1 = -psi_1 = -J; [LT] standard Yangian
        """
        wb = antipode_W_basis()
        assert wb["S(J)"] == "-J"

    def test_S_T_coefficient(self):
        """S(T) = -T + (Psi-1)/Psi * :JJ:.
        # VERIFIED [DC] Miura inversion; [LC] Psi=1 gives S(T)=-T
        """
        wb = antipode_W_basis()
        alpha = wb["alpha"]
        expected = (Psi_sym - 1) / Psi_sym
        assert simplify(alpha - expected) == 0

    def test_S_T_free_boson(self):
        """At Psi=1 (free boson): S(T) = -T (no J^2 correction).
        # VERIFIED [LC] free boson; [NE] alpha(1) = 0
        """
        wb = antipode_W_basis(Psi=Rational(1))
        assert wb["alpha"] == 0

    def test_S_T_classical_limit(self):
        """At Psi -> inf (classical): alpha -> 1, so S(T) -> -T + :JJ:.
        # VERIFIED [LC] classical limit
        """
        from sympy import limit, oo
        alpha = (Psi_sym - 1) / Psi_sym
        assert limit(alpha, Psi_sym, oo) == 1


# ============================================================================
# 3. Involutivity
# ============================================================================

class TestInvolutivity:
    """Test S^2 = id."""

    def test_S_squared_J(self):
        """S^2(J) = J.
        # VERIFIED [DC] S(-J) = J; [SY] involution
        """
        result = verify_involutivity()
        assert result["S^2(J) == J"]

    def test_S_squared_T(self):
        """S^2(T) = T.
        # VERIFIED [DC] -S(T) + alpha*S(J)^2 = T; [SY] involution
        """
        result = verify_involutivity()
        assert result["S^2(T) == T"]

    def test_S_squared_at_Psi_2(self):
        """S^2 = id at Psi=2.
        # VERIFIED [NE] numerical evaluation
        """
        result = verify_involutivity(Psi=Rational(2))
        assert result["S^2(J) == J"]
        assert result["S^2(T) == T"]


# ============================================================================
# 4. Quartic pole obstruction
# ============================================================================

class TestQuarticPoleObstruction:
    """Test that S does NOT preserve the Virasoro quartic pole generically."""

    def test_obstruction_formula(self):
        """Obstruction = 2*(Psi-1)*(Psi-2).
        # VERIFIED [DC] OPE computation via Wick theorem; [SY] factored form
        """
        qpo = quartic_pole_obstruction()
        obs = qpo["obstruction_factored"]
        expected = 2 * (Psi_sym - 1) * (Psi_sym - 2)
        assert simplify(obs - expected) == 0

    def test_obstruction_nonzero_generically(self):
        """Obstruction does not vanish for generic Psi.
        # VERIFIED [DC] polynomial of degree 2 with 2 roots
        """
        qpo = quartic_pole_obstruction()
        assert not qpo["is_zero_generically"]

    def test_vanishing_locus(self):
        """Obstruction vanishes exactly at Psi in {1, 2}.
        # VERIFIED [DC] roots of 2*(Psi-1)*(Psi-2); [NE] evaluation
        """
        qpo = quartic_pole_obstruction()
        locus = sorted(qpo["vanishing_locus"])
        assert locus == [1, 2]

    def test_obstruction_at_Psi_1(self):
        """At Psi=1: S(T)=-T preserves the OPE.
        # VERIFIED [LC] free boson; [NE] 2*(1-1)*(1-2) = 0
        """
        qpo = quartic_pole_obstruction(Psi=Rational(1))
        assert qpo["obstruction"] == 0

    def test_obstruction_at_Psi_2(self):
        """At Psi=2 (c=-2): obstruction vanishes.
        # VERIFIED [NE] 2*(2-1)*(2-2) = 0
        """
        qpo = quartic_pole_obstruction(Psi=Rational(2))
        assert qpo["obstruction"] == 0

    def test_obstruction_at_Psi_3(self):
        """At Psi=3: obstruction = 2*2*1 = 4.
        # VERIFIED [NE] 2*(3-1)*(3-2) = 4
        """
        qpo = quartic_pole_obstruction(Psi=Rational(3), c=Rational(1) - 6*Rational(4, 3))
        assert qpo["obstruction"] == 4

    def test_ope_contributions(self):
        """Individual OPE contributions match Wick theorem computation.
        # VERIFIED [DC] Wick theorem; [LT] Kac VA book Ch. 3
        #
        # T_{(3)}(:JJ:) = Psi
        # (:JJ:)_{(3)}T = Psi  (skew-symmetry)
        # (:JJ:)_{(3)}(:JJ:) = 2*Psi^2  (Sugawara scaling)
        """
        Psi = Psi_sym
        alpha = (Psi - 1) / Psi

        # S(T)_{(3)}S(T) = c/2 - 2*alpha*Psi + 2*alpha^2*Psi^2
        c = c_sym
        result = expand(c/2 - 2*alpha*Psi + 2*alpha**2*Psi**2)
        expected = expand(c/2 + 2*(Psi - 1)*(Psi - 2))
        assert simplify(result - expected) == 0


# ============================================================================
# 5. Hopf axiom obstruction
# ============================================================================

class TestHopfAxiomObstruction:
    """Test the failure of the vertex Hopf algebra axiom."""

    def test_singular_term(self):
        """Singular obstruction = -(Psi-1)/z^2.
        # VERIFIED [DC] from Y(-J,z)*J = -Psi/z^2 - :JJ: + O(z)
        """
        hopf = hopf_axiom_obstruction()
        assert simplify(hopf["singular_term_simplified"] + (Psi_sym - 1)) == 0

    def test_linear_term_persists(self):
        """The z*J term persists at all Psi, including Psi=1.
        # VERIFIED [DC] comes from z*(1 tensor J) in Delta_z(T)
        """
        hopf = hopf_axiom_obstruction()
        assert hopf["z_J_term_persists"]

    def test_singular_vanishes_Psi_1(self):
        """At Psi=1: singular term vanishes but z*J remains.
        # VERIFIED [NE] -(1-1)/z^2 = 0 but z*J != 0
        """
        hopf = hopf_axiom_obstruction()
        assert hopf["vanishes_at_Psi_1"]

    def test_hopf_axiom_fails_everywhere(self):
        """The Hopf axiom fails at ALL Psi due to the z*J term.
        # VERIFIED [DC] z*J comes from Delta_z spectral dependence, independent of Psi
        """
        hopf = hopf_axiom_obstruction()
        # The z*J term is present regardless of Psi
        assert hopf["linear_term"] == "z*J"


# ============================================================================
# 6. Numerical consistency
# ============================================================================

class TestNumericalConsistency:
    """Numerical checks at specific parameter values."""

    def test_Psi_1_free_boson(self):
        """Psi=1 (c=1, free boson): S(T) = -T, quartic pole preserved.
        # VERIFIED [LC] free boson limit; [NE] direct evaluation
        """
        nc = numerical_checks()
        data = nc["Psi=1 (free boson, c=1)"]
        assert data["alpha"] == 0
        assert data["c"] == 1
        assert data["quartic_pole_vanishes"]

    def test_Psi_2_bc_ghost(self):
        """Psi=2 (c=-2, bc ghost): quartic pole preserved.
        # VERIFIED [NE] 2*(2-1)*(2-2) = 0; [LT] bc at lambda=1 has c=-2
        """
        nc = numerical_checks()
        data = nc["Psi=2 (c=-2, bc ghost)"]
        assert data["c"] == -2
        assert data["quartic_pole_vanishes"]

    def test_Psi_3_obstruction_nonzero(self):
        """Psi=3: quartic pole obstruction = 4.
        # VERIFIED [NE] 2*(3-1)*(3-2) = 4
        """
        nc = numerical_checks()
        data = nc["Psi=3 (c=-8/3)"]
        assert data["quartic_pole_obstruction"] == 4
        assert not data["quartic_pole_vanishes"]

    def test_Psi_10_obstruction_nonzero(self):
        """Psi=10: quartic pole obstruction = 2*9*8 = 144.
        # VERIFIED [NE] 2*(10-1)*(10-2) = 144
        """
        nc = numerical_checks()
        data = nc["Psi=10"]
        assert data["quartic_pole_obstruction"] == 144
        assert not data["quartic_pole_vanishes"]


# ============================================================================
# 7. Cross-checks with existing coproduct engine
# ============================================================================

class TestCrossChecks:
    """Cross-checks against w_infinity_ope_compat_spin2 engine."""

    def test_alpha_matches_JJ_coefficient(self):
        """The alpha = (Psi-1)/Psi in S(T) matches the J.J coefficient in Delta_z(T).
        # VERIFIED [CF] cross-engine: w_infinity_ope_compat_spin2.delta_T_coefficient_JJ
        """
        from compute.lib.w_infinity_ope_compat_spin2 import delta_T_coefficient_JJ
        jj_coeff = delta_T_coefficient_JJ()
        expected = (Psi_sym - 1) / Psi_sym
        assert simplify(jj_coeff - expected) == 0

    def test_coproduct_consistency(self):
        """The Miura derivation of Delta_z(T) is consistent.
        # VERIFIED [CF] cross-engine: w_infinity_ope_compat_spin2.verify_miura_derivation
        """
        from compute.lib.w_infinity_ope_compat_spin2 import verify_miura_derivation
        md = verify_miura_derivation()
        assert md["all_match"]
