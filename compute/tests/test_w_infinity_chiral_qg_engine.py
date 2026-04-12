r"""Tests for the W_{1+infinity} chiral quantum group axiom verification engine.

Verifies:
  1. OPE data consistency (lambda-bracket <-> OPE mode conversion)
  2. Chiral coproduct structure (primitivity, quantum corrections)
  3. Counit axiom (A1) for all generators
  4. OPE compatibility axiom (A2) at low spin
  5. Coassociativity axiom (A3) at leading order
  6. R-matrix structure and pole orders (AP19 d-log absorption)
  7. Structure function g(z) and shadow class
  8. CoHA bialgebra comparison (character match, vertex coproduct)
  9. Kappa formulas for W_{1+inf} sectors (AP1 census cross-check)
  10. W_3 axiom constraint analysis

References:
  landscape_census.tex (kappa formulas: C1-C4)
  chapters/theory/yangians.tex (chiral Yangian axioms)
  chapters/theory/en_koszul_duality.tex (E_n bar coproduct)
  Maulik-Okounkov, arXiv:1211.1287 (stable envelopes)
  Schiffmann-Vasserot, arXiv:1202.2756 (SV isomorphism)
  Zamolodchikov 1985 (W_3 OPE)
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify

from compute.lib.w_infinity_chiral_qg_engine import (
    OPEData,
    ChiralCoproduct,
    AxiomVerifier,
    MOStructureFunction,
    MOStructureFunctionOmega,
    WInfinityChiralQG,
    CoHAComparison,
    W3AxiomConstraints,
    full_axiom_check,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_w3,
    kappa_w_n,
    shadow_class,
)


# ======================================================================
#  1. OPE data consistency
# ======================================================================

class TestOPEData:
    """Test OPE structure constants and lambda-bracket/OPE-mode conversion."""

    def setup_method(self):
        self.ope = OPEData(c=Rational(25), k=Rational(1))

    # --- Heisenberg JJ ---

    def test_jj_mode_0_vanishes(self):
        """J_{(0)}J = 0 (no simple pole in JJ OPE for abelian algebra)."""
        coeffs = self.ope.ope_JJ()
        assert coeffs[0] == 0

    def test_jj_mode_1_equals_k(self):
        r"""J_{(1)}J = k (double pole coefficient).

        # VERIFIED: [DC] direct from OPE J(z)J(w) ~ k/(z-w)^2;
        #           [LT] Kac, Vertex Algebras for Beginners, eq. 2.4.
        """
        coeffs = self.ope.ope_JJ()
        assert coeffs[1] == Rational(1)  # k=1

    def test_jj_k_zero_vanishes(self):
        """At k=0 all JJ OPE coefficients vanish (AP126 boundary check)."""
        ope_k0 = OPEData(c=Rational(25), k=Rational(0))
        coeffs = ope_k0.ope_JJ()
        assert coeffs[0] == 0
        assert coeffs[1] == 0

    # --- Virasoro TT ---

    def test_tt_mode_3_central_charge(self):
        r"""T_{(3)}T = c/2 (quartic pole in TT OPE).

        Lambda-bracket coefficient c_3 = c/12.
        OPE mode = 3! * c/12 = c/2.

        # VERIFIED: [DC] 6 * (25/12) = 25/2;
        #           [LT] Zamolodchikov 1985, Virasoro OPE.
        """
        coeffs = self.ope.ope_TT_scalar_coeffs()
        # c_3 = c/12 (lambda-bracket coefficient)
        lambda_coeff = coeffs[3]
        assert lambda_coeff == Rational(25, 12)
        # OPE mode T_{(3)}T = 3! * c/12 = c/2
        ope_mode_3 = 6 * lambda_coeff
        assert ope_mode_3 == Rational(25, 2)

    def test_tt_mode_2_vanishes(self):
        """T_{(2)}T = 0 (no cubic pole in TT OPE)."""
        coeffs = self.ope.ope_TT_scalar_coeffs()
        assert coeffs[2] == 0

    def test_tt_divided_power_consistency(self):
        r"""Verify AP44: lambda^{(n)} = lambda^n / n! convention.

        {T_lambda T} = (c/12) lambda^3 + 2T lambda + dT
        The coefficient of lambda^3 is c/12 (NOT c/2, which is the OPE mode).
        """
        coeffs = self.ope.ope_TT_scalar_coeffs()
        # The lambda^3 coefficient is c/12 (divided power convention)
        assert coeffs[3] == self.ope.c / 12

    # --- W_3 OPE ---

    def test_ww_mode_5_central(self):
        r"""W_{(5)}W = c/3 (sextic pole in WW OPE).

        Lambda-bracket coefficient c_5 = c/3 (in the convention where
        {W_lambda W} = (c/3) lambda^{(5)} + ..., with lambda^{(5)} = lambda^5/5!).

        OPE mode: W_{(5)}W = 5! * c/(3 * 5!) = ... wait.

        Convention check: the engine stores c_5 as the coefficient of
        lambda^{(5)} = lambda^5/120, so the OPE mode is:
          W_{(5)}W = c_5  (if c_5 is already the full coefficient of lambda^5/5!)

        Actually, the lambda-bracket coefficient at lambda^n is c_n
        where {a_lambda b} = sum c_n lambda^n.  Then the divided-power
        lambda-bracket is {a_lambda b} = sum (c_n / n!) lambda^n.

        NO: the standard convention is {a_lambda b} = sum c_n lambda^{(n)}
        where lambda^{(n)} = lambda^n / n!.  So c_n IS the coefficient
        of the divided power.  The OPE mode is a_{(n)}b = c_n (directly).

        For WW: c_5 = c/3.  So W_{(5)}W = c/3.

        # VERIFIED: [DC] Zamolodchikov 1985 OPE: W(z)W(w) ~ (c/3)/(z-w)^6;
        #           [LT] Bouwknegt-Schoutens 1993, eq. 2.12.
        """
        coeffs = self.ope.ope_WW_scalar_coeffs()
        assert coeffs[5] == Rational(25, 3)  # c/3 at c=25

    def test_ww_scalar_lower_modes_vanish(self):
        """Scalar (vacuum) part of WW OPE has only the top pole."""
        coeffs = self.ope.ope_WW_scalar_coeffs()
        for n in range(5):
            assert coeffs[n] == 0, f"Scalar WW coefficient c_{n} should vanish"

    def test_w3_structure_constant(self):
        r"""beta = 32/(22+5c) is the W_3 OPE structure constant.

        The coefficient of Lambda * lambda in {W_lambda W} is 32/(22+5c).
        At c=25: beta = 32/(22+125) = 32/147.
        At c=-22/5: beta diverges (minimal model singularity).

        # VERIFIED: [DC] 32/(22+5*25) = 32/147;
        #           [LT] Zamolodchikov 1985, Bouwknegt-Schoutens 1993 eq. 2.12.
        """
        beta = self.ope.w3_structure_constant()
        assert beta == Rational(32, 147)

    def test_w3_structure_constant_c1(self):
        """At c=1: beta = 32/(22+5) = 32/27."""
        ope_c1 = OPEData(c=Rational(1))
        assert ope_c1.w3_structure_constant() == Rational(32, 27)

    @pytest.mark.parametrize("c_val,expected", [
        (Rational(0), Rational(32, 22)),   # c=0: 32/22 = 16/11
        (Rational(1), Rational(32, 27)),   # c=1
        (Rational(25), Rational(32, 147)), # c=25
    ])
    def test_w3_structure_constant_parametric(self, c_val, expected):
        """W_3 structure constant at various central charges."""
        ope = OPEData(c=c_val)
        assert ope.w3_structure_constant() == expected


# ======================================================================
#  2. Chiral coproduct structure
# ======================================================================

class TestChiralCoproduct:
    """Test chiral coproduct Delta^{ch} at low spin."""

    def setup_method(self):
        self.coprod = ChiralCoproduct(c=Rational(25), k=Rational(1))

    # --- Spin 1: J is primitive ---

    def test_j_is_primitive(self):
        """Delta^{ch}(J) = J tensor 1 + 1 tensor J (primitive)."""
        delta = self.coprod.delta_J()
        assert delta["is_primitive"] is True

    def test_j_has_no_quantum_corrections(self):
        """J coproduct has no quantum corrections."""
        delta = self.coprod.delta_J()
        assert len(delta["quantum_corrections"]) == 0

    def test_j_has_two_terms(self):
        """J coproduct has exactly two terms: J tensor 1 and 1 tensor J."""
        delta = self.coprod.delta_J()
        assert len(delta["terms"]) == 2
        lefts = {t["left"] for t in delta["terms"]}
        rights = {t["right"] for t in delta["terms"]}
        assert lefts == {"J", "1"}
        assert rights == {"J", "1"}

    def test_j_spin_is_1(self):
        delta = self.coprod.delta_J()
        assert delta["spin"] == 1

    # --- Spin 2: T has quantum corrections ---

    def test_t_is_not_primitive(self):
        """Delta^{ch}(T) is NOT primitive (central extension correction)."""
        delta = self.coprod.delta_T()
        assert delta["is_primitive"] is False

    def test_t_has_schwinger_correction(self):
        """T coproduct has the Schwinger term (c/2)/z^2."""
        delta = self.coprod.delta_T()
        assert len(delta["quantum_corrections"]) >= 1
        schwinger = delta["quantum_corrections"][0]
        assert schwinger["coefficient"] == Rational(25, 2)  # c/2 = 25/2
        assert schwinger["z_power"] == -2

    def test_t_schwinger_coefficient_is_half_c(self):
        r"""The Schwinger term coefficient is c/2, not c or c/12.

        c/2 arises from the OPE mode T_{(3)}T = c/2, contributing to
        the cross-factor collision term in the coproduct.

        # VERIFIED: [DC] T_{(3)}T = c/2 from OPE;
        #           [LT] Huang-Lepowsky tensor product theory.
        """
        for c_val in [Rational(1), Rational(13), Rational(25), Rational(26)]:
            coprod = ChiralCoproduct(c=c_val)
            delta = coprod.delta_T()
            schwinger_coeff = delta["quantum_corrections"][0]["coefficient"]
            assert schwinger_coeff == c_val / 2

    def test_t_spin_is_2(self):
        delta = self.coprod.delta_T()
        assert delta["spin"] == 2

    # --- Spin 3: W has parametric corrections ---

    def test_w_is_not_primitive(self):
        """Delta^{ch}(W) is NOT primitive."""
        delta = self.coprod.delta_W()
        assert delta["is_primitive"] is False

    def test_w_has_parametric_constraints(self):
        """W coproduct carries parametric constraints involving beta."""
        delta = self.coprod.delta_W()
        assert "parametric_constraints" in delta
        assert delta["parametric_constraints"]["beta"] == Rational(16, 147)

    def test_w_ww_schwinger_coefficient(self):
        r"""The WW Schwinger term coefficient is c/3.

        From W_{(5)}W = c/3 (sextic pole).

        # VERIFIED: [DC] direct from OPE;
        #           [LT] Zamolodchikov 1985.
        """
        delta = self.coprod.delta_W()
        # Find the WW Schwinger term
        ww_schwinger = [corr for corr in delta["quantum_corrections"]
                        if corr.get("z_power") == -6]
        assert len(ww_schwinger) == 1
        assert ww_schwinger[0]["coefficient"] == Rational(25, 3)  # c/3 at c=25

    def test_w_spin_is_3(self):
        delta = self.coprod.delta_W()
        assert delta["spin"] == 3


# ======================================================================
#  3. Counit axiom (A1)
# ======================================================================

class TestCounitAxiom:
    """Test epsilon(generator) = 0 and counit compatibility."""

    def setup_method(self):
        self.verifier = AxiomVerifier(c=Rational(25), k=Rational(1))

    def test_counit_J(self):
        """epsilon(J) = 0 and (epsilon tensor id) o Delta(J) recovers J."""
        result = self.verifier.verify_counit("J")
        assert result["epsilon_value"] == 0
        assert result["counit_axiom_holds"] is True

    def test_counit_T(self):
        """epsilon(T) = 0 and (epsilon tensor id) o Delta(T) recovers T."""
        result = self.verifier.verify_counit("T")
        assert result["epsilon_value"] == 0
        assert result["counit_axiom_holds"] is True

    def test_counit_W(self):
        """epsilon(W) = 0 and (epsilon tensor id) o Delta(W) recovers W."""
        result = self.verifier.verify_counit("W")
        assert result["epsilon_value"] == 0
        assert result["counit_axiom_holds"] is True

    def test_counit_unknown_raises(self):
        """Unknown generator raises ValueError."""
        with pytest.raises(ValueError):
            self.verifier.verify_counit("X")


# ======================================================================
#  4. OPE compatibility axiom (A2)
# ======================================================================

class TestOPECompatibility:
    """Test OPE compatibility of the chiral coproduct."""

    def setup_method(self):
        self.verifier = AxiomVerifier(c=Rational(25), k=Rational(1))

    def test_jj_mode_0(self):
        """JJ OPE compatibility at mode 0: J_{(0)}J = 0."""
        result = self.verifier.verify_ope_compatibility_JJ()
        assert result["mode_0_compatible"] is True

    def test_jj_mode_1(self):
        """JJ OPE compatibility at mode 1: Delta(k) = k * (1 tensor 1)."""
        result = self.verifier.verify_ope_compatibility_JJ()
        assert result["mode_1_compatible"] is True
        assert result["mode_1_lhs"] == result["mode_1_rhs"]

    def test_jj_all_modes(self):
        """JJ OPE compatibility at all modes."""
        result = self.verifier.verify_ope_compatibility_JJ()
        assert result["all_modes_compatible"] is True

    def test_tt_scalar_mode_3(self):
        """TT OPE scalar compatibility at mode 3: central term c/2."""
        result = self.verifier.verify_ope_compatibility_TT_scalar()
        assert result["mode_3_compatible"] is True

    def test_tt_lambda_bracket_convention(self):
        r"""Verify lambda-bracket <-> OPE mode conversion at mode 3.

        Lambda-bracket c_3 = c/12.  OPE mode = 3! * c/12 = c/2.

        # VERIFIED: [DC] 6 * 25/12 = 25/2;
        #           [CF] matches kappa_Vir = c/2 at arity 2.
        """
        result = self.verifier.verify_ope_compatibility_TT_scalar()
        assert result["ope_mode_3_value"] == Rational(25, 2)
        assert result["mode_3_lambda_bracket_correct"] is True

    @pytest.mark.parametrize("c_val", [
        Rational(0), Rational(1), Rational(13), Rational(25), Rational(26),
    ])
    def test_tt_scalar_parametric(self, c_val):
        """TT scalar OPE compatibility across central charges."""
        v = AxiomVerifier(c=c_val, k=Rational(1))
        result = v.verify_ope_compatibility_TT_scalar()
        assert result["mode_3_compatible"] is True


# ======================================================================
#  5. Coassociativity axiom (A3)
# ======================================================================

class TestCoassociativity:
    """Test coassociativity of the chiral coproduct."""

    def setup_method(self):
        self.verifier = AxiomVerifier(c=Rational(25), k=Rational(1))

    def test_j_coassociative(self):
        """J coassociativity: trivial for primitive elements."""
        result = self.verifier.verify_coassociativity_J()
        assert result["coassociative"] is True
        assert result["lhs_terms"] == result["rhs_terms"]

    def test_t_coassociative_leading(self):
        """T coassociativity at leading order (primitive + first correction)."""
        result = self.verifier.verify_coassociativity_T_leading()
        assert result["coassociative_at_leading_order"] is True

    def test_t_scalar_corrections_match(self):
        """Both sides give 2*(c/2) = c for the scalar correction."""
        result = self.verifier.verify_coassociativity_T_leading()
        assert result["lhs_scalar_correction"] == result["rhs_scalar_correction"]
        assert result["lhs_scalar_correction"] == Rational(25)  # 2 * c/2 = c

    @pytest.mark.parametrize("c_val", [
        Rational(0), Rational(1), Rational(13), Rational(25),
    ])
    def test_t_coassociative_parametric(self, c_val):
        """T coassociativity at leading order across central charges."""
        v = AxiomVerifier(c=c_val)
        result = v.verify_coassociativity_T_leading()
        assert result["coassociative_at_leading_order"] is True


# ======================================================================
#  6. R-matrix structure and pole orders
# ======================================================================

class TestRMatrix:
    """Test R-matrix pole orders and AP19 d-log absorption."""

    def setup_method(self):
        self.mo = MOStructureFunction(c=Rational(25), k=Rational(1))

    def test_spin1_pole_order(self):
        """Heisenberg r-matrix has simple pole (OPE double pole - 1)."""
        r = self.mo.r_matrix_spin1()
        assert r["pole_order"] == 1
        assert r["ope_pole_order"] == 2
        # AP19: r-pole = OPE-pole - 1
        assert r["pole_order"] == r["ope_pole_order"] - 1

    def test_spin2_pole_order(self):
        """Virasoro r-matrix has cubic pole (OPE quartic pole - 1)."""
        r = self.mo.r_matrix_spin2()
        assert r["pole_order"] == 3
        assert r["ope_pole_order"] == 4
        assert r["pole_order"] == r["ope_pole_order"] - 1

    def test_spin3_pole_order(self):
        """W_3 r-matrix has quintic pole (OPE sextic pole - 1)."""
        r = self.mo.r_matrix_spin3()
        assert r["pole_order"] == 5
        assert r["ope_pole_order"] == 6
        assert r["pole_order"] == r["ope_pole_order"] - 1

    def test_ap19_universal(self):
        """AP19 d-log absorption: pole_r = pole_OPE - 1 at all spins."""
        for spin, method in [(1, self.mo.r_matrix_spin1),
                             (2, self.mo.r_matrix_spin2),
                             (3, self.mo.r_matrix_spin3)]:
            r = method()
            assert r["pole_order"] == r["ope_pole_order"] - 1, (
                f"AP19 fails at spin {spin}"
            )

    def test_spin1_k_zero_vanishes(self):
        r"""At k=0, r_1(z) = 0 (AP126 boundary check).

        # VERIFIED: [DC] k/z at k=0 = 0;
        #           [SY] abelian limit symmetry.
        """
        r = self.mo.r_matrix_spin1()
        assert r["k_zero_check"] == 0

    def test_spin1_k_zero_explicit(self):
        """Construct r-matrix at k=0 and verify vanishing."""
        mo_k0 = MOStructureFunction(c=Rational(25), k=Rational(0))
        z = Symbol('z')
        r = mo_k0.r_matrix_spin1(z=z)
        assert simplify(r["r_sympy"]) == 0

    def test_spin2_pole_is_cubic_not_quartic(self):
        r"""Virasoro r-matrix pole order is 3, NOT 4 (AP19, B2, B3).

        The OPE T(z)T(w) has a quartic pole, but d-log absorption
        reduces by one: r^{coll}(z) = (c/2)/z^3 + 2T/z.
        """
        r = self.mo.r_matrix_spin2()
        assert r["pole_order"] == 3  # NOT 4
        assert r["pole_order"] != 4  # Explicit anti-check (B2)
        assert r["pole_order"] != 2  # Explicit anti-check (B3)


# ======================================================================
#  7. Structure function and shadow class
# ======================================================================

class TestStructureFunction:
    """Test structure function g(z) and shadow classification."""

    def setup_method(self):
        self.verifier = AxiomVerifier(c=Rational(25), k=Rational(1))
        self.mo = MOStructureFunction(c=Rational(25), k=Rational(1))

    def test_heisenberg_g_trivial(self):
        """g(z) = 1 for Heisenberg (abelian, class G)."""
        result = self.verifier.structure_function_heisenberg()
        assert result["g_z"] == 1
        assert result["shadow_class"] == "G"

    def test_virasoro_class_M(self):
        """Virasoro is class M (infinite shadow depth)."""
        result = self.verifier.structure_function_virasoro()
        assert result["shadow_class"] == "M"

    def test_rtt_leading_compatible(self):
        """RTT relation is satisfied at leading order for Virasoro."""
        result = self.verifier.structure_function_virasoro()
        assert result["rtt_leading_order_compatible"] is True

    def test_shadow_class_spin1(self):
        """Spin 1 (Heisenberg) is class G."""
        assert shadow_class(1) == "G"

    def test_shadow_class_spin2(self):
        """Spin 2 (Virasoro) is class M."""
        assert shadow_class(2) == "M"

    def test_shadow_class_spin3(self):
        """Spin 3 (W_3) is class M."""
        assert shadow_class(3) == "M"

    def test_shadow_class_invalid(self):
        with pytest.raises(ValueError):
            shadow_class(0)

    def test_mo_structure_function_summary(self):
        """MO structure function summary contains all sectors."""
        result = self.mo.structure_function_from_rtt()
        assert result["g_heisenberg"] == 1
        assert result["shadow_depth_heisenberg"] == 2


# ======================================================================
#  8. CoHA bialgebra comparison
# ======================================================================

class TestCoHAComparison:
    """Test CoHA vs bar complex character identity and coproduct comparison."""

    def setup_method(self):
        self.coha = CoHAComparison(c=Rational(25))

    def test_coha_character_partition_numbers(self):
        r"""CoHA(Jordan) character coefficients are partition numbers.

        p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11.

        # VERIFIED: [DC] recursion p(n) = sum_{k=1}^{n} p(n-k);
        #           [LT] OEIS A000041.
        """
        result = self.coha.coha_character_jordan(max_n=10)
        p = result["character_coefficients"]
        # First 11 partition numbers
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        assert p[:11] == expected

    def test_bar_character_matches_coha(self):
        """B(Heisenberg) character equals CoHA(Jordan) character."""
        result = self.coha.character_comparison(max_n=10)
        assert result["all_match"] is True

    def test_character_coefficients_identical(self):
        """Term-by-term character comparison."""
        result = self.coha.character_comparison(max_n=15)
        coha_c = result["coha_coefficients"]
        bar_c = result["bar_coefficients"]
        for i in range(min(len(coha_c), len(bar_c))):
            assert coha_c[i] == bar_c[i], f"Mismatch at n={i}"

    def test_vertex_coproduct_spin1_match(self):
        """CoHA vertex coproduct matches chiral coproduct at spin 1."""
        result = self.coha.vertex_coproduct_comparison_spin1()
        assert result["match"] is True
        assert result["chiral_coproduct_is_primitive"] is True


# ======================================================================
#  9. Kappa formulas (AP1 census cross-check)
# ======================================================================

class TestKappaFormulas:
    """Test kappa for W_{1+inf} sectors against landscape_census.tex.

    All formulas from C1-C4 (true formula census).
    """

    # --- C1: Heisenberg ---

    def test_kappa_heis_k1(self):
        r"""kappa(H_1) = 1.

        # VERIFIED: [DC] k=1 -> 1; [LT] C1 census.
        """
        assert kappa_heisenberg(Rational(1)) == Rational(1)

    def test_kappa_heis_k0(self):
        """kappa(H_0) = 0 (AP126 boundary)."""
        assert kappa_heisenberg(Rational(0)) == Rational(0)

    def test_kappa_heis_generic(self):
        """kappa(H_k) = k for generic k."""
        for k in [Rational(-1), Rational(1, 2), Rational(3), Rational(7)]:
            assert kappa_heisenberg(k) == k

    # --- C2: Virasoro ---

    def test_kappa_vir_c25(self):
        r"""kappa(Vir_25) = 25/2.

        # VERIFIED: [DC] c/2 = 25/2; [LT] C2 census.
        """
        assert kappa_virasoro(Rational(25)) == Rational(25, 2)

    def test_kappa_vir_c0(self):
        """kappa(Vir_0) = 0."""
        assert kappa_virasoro(Rational(0)) == Rational(0)

    def test_kappa_vir_c13_self_dual(self):
        r"""kappa(Vir_13) = 13/2 (self-dual point, C8).

        # VERIFIED: [DC] 13/2; [SY] self-dual c=13.
        """
        assert kappa_virasoro(Rational(13)) == Rational(13, 2)

    # --- C4: W_N ---

    def test_kappa_w2_equals_vir(self):
        r"""kappa(W_2) = c/2 = kappa(Vir) (W_2 = Virasoro).

        AP136 boundary: H_2 - 1 = 3/2 - 1 = 1/2, so kappa = c * 1/2 = c/2.

        # VERIFIED: [DC] H_2 = 1 + 1/2 = 3/2, H_2 - 1 = 1/2;
        #           [CF] matches kappa_Vir(c).
        """
        c = Rational(25)
        assert kappa_w_n(c, 2) == kappa_virasoro(c)
        assert kappa_w_n(c, 2) == c / 2

    def test_kappa_w3(self):
        r"""kappa(W_3) = 5c/6.

        H_3 = 1 + 1/2 + 1/3 = 11/6.  H_3 - 1 = 5/6.

        # VERIFIED: [DC] 25 * 5/6 = 125/6;
        #           [LT] C4 census.
        """
        c = Rational(25)
        assert kappa_w3(c) == c * Rational(5, 6)
        assert kappa_w3(c) == Rational(125, 6)

    def test_kappa_w3_via_w_n(self):
        """kappa_w3 helper matches kappa_w_n(c, 3)."""
        c = Rational(25)
        assert kappa_w3(c) == kappa_w_n(c, 3)

    def test_kappa_w_n_ap136_not_h_n_minus_1(self):
        r"""AP136: kappa(W_N) = c*(H_N - 1), NOT c*H_{N-1}.

        At N=2: H_2 - 1 = 1/2, but H_1 = 1.
        c*(H_2 - 1) = c/2 (correct, matches Virasoro).
        c*H_1 = c (WRONG, double the correct value).

        # VERIFIED: [DC] H_2 - 1 = 1/2 vs H_1 = 1;
        #           [CF] kappa(W_2) = kappa(Vir) = c/2.
        """
        c = Rational(25)
        # Correct: c * (H_2 - 1) = c * 1/2
        correct = kappa_w_n(c, 2)
        assert correct == c / 2
        # Wrong: c * H_1 = c * 1 = c (this is AP136)
        wrong_h_n_minus_1 = c * Rational(1)  # H_1 = 1
        assert wrong_h_n_minus_1 != correct
        assert wrong_h_n_minus_1 == c  # Double the correct value

    def test_kappa_w_n_raises_for_n_lt_2(self):
        with pytest.raises(ValueError):
            kappa_w_n(Rational(25), 1)

    @pytest.mark.parametrize("N,expected_factor", [
        (2, Rational(1, 2)),     # H_2 - 1 = 1/2
        (3, Rational(5, 6)),     # H_3 - 1 = 5/6
        (4, Rational(13, 12)),   # H_4 - 1 = 13/12
        (5, Rational(77, 60)),   # H_5 - 1 = 77/60
    ])
    def test_kappa_w_n_factors(self, N, expected_factor):
        r"""kappa(W_N) = c * (H_N - 1) at various N.

        H_2 = 3/2,  H_2 - 1 = 1/2
        H_3 = 11/6, H_3 - 1 = 5/6
        H_4 = 25/12, H_4 - 1 = 13/12
        H_5 = 137/60, H_5 - 1 = 77/60

        # VERIFIED: [DC] direct summation H_N = sum 1/j;
        #           [LT] C4/C19 census.
        """
        c = Rational(1)  # Use c=1 to isolate the factor
        assert kappa_w_n(c, N) == expected_factor


# ======================================================================
#  10. W_3 axiom constraint analysis
# ======================================================================

class TestW3Constraints:
    """Test the W_3 coproduct axiom constraint analysis."""

    def setup_method(self):
        self.constraints = W3AxiomConstraints(c=Rational(25))

    def test_weight_decomposition_pole_0(self):
        """At pole order 0: total weight = 3, pairs include (0,3), (1,2), etc."""
        decomp = self.constraints.weight_decomposition(max_pole=0)
        pairs = decomp[0]
        assert (0, 3) in pairs
        assert (1, 2) in pairs
        assert (2, 1) in pairs
        assert (3, 0) in pairs

    def test_weight_decomposition_pole_1(self):
        """At pole order 1: total weight = 4."""
        decomp = self.constraints.weight_decomposition(max_pole=1)
        pairs = decomp[1]
        total = 4
        for h_L, h_R in pairs:
            assert h_L + h_R == total

    def test_tw_constraint_redundant(self):
        """TW OPE constraint is redundant with conformal covariance."""
        result = self.constraints.ope_tw_constraint()
        assert result["independent_content"] is False

    def test_ww_constraint_nontrivial(self):
        """WW OPE constraint is genuinely nontrivial."""
        result = self.constraints.ope_ww_constraint()
        assert result["independent_content"] is True

    def test_ww_constraint_beta(self):
        """WW constraint carries the correct beta parameter."""
        result = self.constraints.ope_ww_constraint()
        assert result["beta_parameter"] == Rational(16, 147)

    def test_ww_constraint_singular_c(self):
        """WW constraint identifies the singular central charge c = -22/5."""
        result = self.constraints.ope_ww_constraint()
        assert result["c_singular"] == Rational(-22, 5)

    def test_conformal_covariance_total_weights(self):
        """Conformal covariance requires total weight 3+n at pole order n."""
        constraints = self.constraints.conformal_covariance_constraints()
        for n in range(1, 5):
            key = f"pole_order_{n}"
            assert constraints[key]["total_weight_required"] == 3 + n


# ======================================================================
#  11. Full axiom check integration
# ======================================================================

class TestFullAxiomCheck:
    """Integration test: run all axiom checks and verify pass rate."""

    def test_full_check_c25(self):
        """All axiom checks pass at c=25, k=1."""
        result = full_axiom_check(c=Rational(25), k=Rational(1))
        assert result["summary"]["all_checks_pass"] is True
        assert result["summary"]["num_passed"] == result["summary"]["num_total"]

    def test_full_check_c1(self):
        """All axiom checks pass at c=1, k=1."""
        result = full_axiom_check(c=Rational(1), k=Rational(1))
        assert result["summary"]["all_checks_pass"] is True

    def test_full_check_c13(self):
        """All axiom checks pass at c=13 (self-dual point), k=1."""
        result = full_axiom_check(c=Rational(13), k=Rational(1))
        assert result["summary"]["all_checks_pass"] is True

    def test_full_check_c0(self):
        """All axiom checks pass at c=0, k=1."""
        result = full_axiom_check(c=Rational(0), k=Rational(1))
        assert result["summary"]["all_checks_pass"] is True

    def test_full_check_k0(self):
        """All axiom checks pass at c=25, k=0 (abelian Heisenberg limit)."""
        result = full_axiom_check(c=Rational(25), k=Rational(0))
        assert result["summary"]["all_checks_pass"] is True

    def test_kappa_parameters(self):
        """Check kappa values in full report."""
        result = full_axiom_check(c=Rational(25), k=Rational(1))
        params = result["parameters"]
        assert params["kappa_heis"] == Rational(1)
        assert params["kappa_vir"] == Rational(25, 2)
        assert params["kappa_w3"] == Rational(125, 6)  # 25 * 5/6

    def test_individual_checks_list(self):
        """Full report contains at least 8 individual checks."""
        result = full_axiom_check(c=Rational(25), k=Rational(1))
        assert result["summary"]["num_total"] >= 8

    @pytest.mark.parametrize("c_val", [
        Rational(-2), Rational(0), Rational(1), Rational(13),
        Rational(25), Rational(26), Rational(100),
    ])
    def test_full_check_parametric(self, c_val):
        """Full axiom check passes across a range of central charges."""
        result = full_axiom_check(c=c_val, k=Rational(1))
        assert result["summary"]["all_checks_pass"] is True

    def test_full_check_negative_k(self):
        """Full axiom check passes at negative Heisenberg level."""
        result = full_axiom_check(c=Rational(25), k=Rational(-1))
        assert result["summary"]["all_checks_pass"] is True


# ======================================================================
#  12. WInfinityChiralQG: unified (Psi, spin_max) interface
# ======================================================================

class TestWInfinityChiralQGConstruction:
    """Basic construction and parameter validation for the unified class."""

    def test_construction_spin1(self):
        qg = WInfinityChiralQG(Psi=Rational(1), spin_max=1)
        assert qg.Psi == Rational(1)
        assert qg.spin_max == 1

    def test_construction_spin2(self):
        qg = WInfinityChiralQG(Psi=Rational(3), spin_max=2)
        assert qg.Psi == Rational(3)
        assert qg.spin_max == 2

    def test_construction_spin3(self):
        qg = WInfinityChiralQG(Psi=Rational(1, 2), spin_max=3)
        assert qg.spin_max == 3

    def test_invalid_spin_max_low(self):
        with pytest.raises(ValueError):
            WInfinityChiralQG(Psi=Rational(1), spin_max=0)

    def test_invalid_spin_max_high(self):
        with pytest.raises(ValueError):
            WInfinityChiralQG(Psi=Rational(1), spin_max=4)

    def test_symbolic_psi(self):
        Psi = Symbol('Psi')
        qg = WInfinityChiralQG(Psi=Psi, spin_max=2)
        assert qg.Psi is Psi


# ======================================================================
#  13. WInfinityChiralQG: Spin-1 Heisenberg axioms
# ======================================================================

class TestWIQGSpin1:
    """Spin-1 axioms via the unified WInfinityChiralQG class."""

    def setup_method(self):
        self.qg = WInfinityChiralQG(Psi=Rational(1), spin_max=1)

    def test_ope_jj_mode0_vanishes(self):
        """J_{(0)}J = 0 (abelian: no simple pole)."""
        ope = self.qg.ope_JJ()
        assert ope["ope_mode_0"] == 0

    def test_ope_jj_mode1_equals_psi(self):
        r"""J_{(1)}J = Psi (double pole coefficient = level).

        # VERIFIED: [DC] direct from OPE; [LT] C10; [LC] Psi=0 -> 0.
        """
        ope = self.qg.ope_JJ()
        assert ope["ope_mode_1"] == Rational(1)
        assert ope["level"] == Rational(1)

    def test_ope_jj_at_psi_zero(self):
        """AP126: at Psi=0, OPE vanishes entirely."""
        qg = WInfinityChiralQG(Psi=Rational(0), spin_max=1)
        ope = qg.ope_JJ()
        assert ope["ope_mode_0"] == 0
        assert ope["ope_mode_1"] == 0

    def test_delta_j_primitive(self):
        """Delta(J) = J.1 + 1.J (primitive)."""
        delta = self.qg.delta_J()
        assert delta["is_primitive"] is True
        assert len(delta["terms"]) == 2
        assert delta["quantum_corrections"] == []

    def test_counit_j(self):
        assert self.qg.verify_counit_J()["holds"] is True

    def test_coassociativity_j(self):
        r = self.qg.verify_coassociativity_J()
        assert r["holds"] is True
        assert r["lhs"] == r["rhs"]

    def test_ope_compat_jj(self):
        r = self.qg.verify_ope_compat_JJ()
        assert r["all_holds"] is True
        assert r["mode_1_lhs"] == r["mode_1_rhs"]

    def test_ope_compat_jj_symbolic_psi(self):
        """OPE compatibility holds for symbolic Psi."""
        Psi = Symbol('Psi')
        qg = WInfinityChiralQG(Psi=Psi, spin_max=1)
        r = qg.verify_ope_compat_JJ()
        assert r["mode_1_lhs"] == Psi
        assert r["mode_1_rhs"] == Psi


# ======================================================================
#  14. WInfinityChiralQG: Spin-2 Sugawara T = (1/(2*Psi)):JJ:
# ======================================================================

class TestWIQGSpin2Sugawara:
    """Spin-2 Sugawara construction and axioms via unified class."""

    def setup_method(self):
        self.qg = WInfinityChiralQG(Psi=Rational(1), spin_max=2)

    def test_sugawara_formula_c1(self):
        r"""T = (1/(2*Psi)):JJ: at Psi=1 gives c^{Sug}=1.

        # VERIFIED: [DC] Sugawara c=1 for rank-1; [LT] Kac VA book ch 3.
        """
        sug = self.qg.sugawara_T()
        assert sug["c_sugawara"] == Rational(1)
        assert sug["ope_TT_quartic_pole"] == Rational(1, 2)  # c/2 = 1/2

    def test_sugawara_undefined_at_psi_zero(self):
        """Sugawara diverges at Psi=0 (critical level analogue)."""
        qg = WInfinityChiralQG(Psi=Rational(0), spin_max=2)
        sug = qg.sugawara_T()
        assert sug["c"] is None

    def test_delta_t_not_primitive(self):
        """Delta(T) has quantum correction from J.J cross-term."""
        delta = self.qg.delta_T_from_delta_J()
        assert delta["is_primitive"] is False
        assert delta["sugawara"] is True
        assert len(delta["quantum_corrections"]) == 2

    def test_delta_t_cross_term_coefficient_psi1(self):
        """Cross-term coefficient is 1/Psi = 1 at Psi=1."""
        delta = self.qg.delta_T_from_delta_J()
        cross = [c for c in delta["quantum_corrections"]
                 if c["type"] == "cross_term"][0]
        assert cross["left"] == "J"
        assert cross["right"] == "J"
        assert cross["coefficient"] == 1  # 1/Psi at Psi=1

    def test_delta_t_cross_term_general_psi(self):
        r"""Cross-term coefficient is 1/Psi for general Psi.

        # VERIFIED: [DC] expanding (1/(2*Psi)):Delta(J)^2:; [LC] Psi->inf -> 0.
        """
        qg = WInfinityChiralQG(Psi=Rational(3), spin_max=2)
        delta = qg.delta_T_from_delta_J()
        cross = [c for c in delta["quantum_corrections"]
                 if c["type"] == "cross_term"][0]
        assert cross["coefficient"] == Rational(1, 3)

    def test_delta_t_schwinger_coefficient(self):
        """Schwinger term is c/2 = 1/2 at Sugawara c=1."""
        delta = self.qg.delta_T_from_delta_J()
        schwinger = [c for c in delta["quantum_corrections"]
                     if c["type"] == "schwinger"][0]
        assert schwinger["coefficient_c_over_2"] == Rational(1, 2)
        assert schwinger["z_power"] == -2

    def test_counit_t(self):
        assert self.qg.verify_counit_T()["holds"] is True

    def test_coassociativity_t_leading(self):
        r = self.qg.verify_coassociativity_T_leading()
        assert r["holds"] is True
        assert r["primitive_match"] is True
        assert r["cross_term_match"] is True

    def test_ope_compat_tt_sugawara_mode3(self):
        r"""OPE compatibility for TT at Sugawara c=1: mode-3 match.

        # VERIFIED: [DC] mode-3 = c/2 = 1/2; [CF] matches Virasoro at c=1.
        """
        r = self.qg.verify_ope_compat_TT_sugawara()
        assert r["all_holds"] is True
        assert r["mode_3_lhs"] == Rational(1, 2)
        assert r["mode_3_rhs"] == Rational(1, 2)

    def test_delta_t_undefined_at_psi_zero(self):
        """Delta(T) returns error at Psi=0."""
        qg = WInfinityChiralQG(Psi=Rational(0), spin_max=2)
        delta = qg.delta_T_from_delta_J()
        assert "error" in delta
        assert delta["terms"] is None


# ======================================================================
#  15. MO structure function g(z) with Omega-background
# ======================================================================

class TestMOStructureFunctionOmega:
    """Maulik-Okounkov structure function g(z)."""

    def test_cy_condition_enforced(self):
        """h3 = -(h1+h2) when not specified."""
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        assert mo.h3 == Rational(-3)
        assert mo.sigma_1 == 0

    def test_sigma_3_equals_psi(self):
        r"""Psi = h1*h2*h3.

        # VERIFIED: [DC] 1*2*(-3) = -6; [LT] Prochazka-Rapcak 1711.11582.
        """
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        assert mo.Psi == Rational(-6)
        assert mo.sigma_3 == Rational(-6)

    def test_sigma_2(self):
        r"""sigma_2 = h1*h2 + h1*h3 + h2*h3.

        # VERIFIED: [DC] 1*2 + 1*(-3) + 2*(-3) = 2 - 3 - 6 = -7.
        """
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        assert mo.sigma_2 == Rational(-7)

    def test_unitarity_rational(self):
        r"""g(z)*g(-z) = 1 for rational h1, h2.

        # VERIFIED: [DC] algebraic identity; [SY] unconditional.
        """
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        r = mo.verify_unitarity()
        assert r["is_one"] is True

    def test_unitarity_symbolic(self):
        """g(z)*g(-z) = 1 for symbolic h (unconditional)."""
        h1, h2 = Symbol('h1'), Symbol('h2')
        mo = MOStructureFunctionOmega(h1, h2)
        r = mo.verify_unitarity()
        assert r["is_one"] is True

    def test_unitarity_non_cy(self):
        """g(z)*g(-z) = 1 even without CY condition."""
        h1, h2, h3 = Symbol('h1'), Symbol('h2'), Symbol('h3')
        mo = MOStructureFunctionOmega(h1, h2, h3)
        r = mo.verify_unitarity()
        assert r["is_one"] is True

    def test_g_at_zero(self):
        r"""g(0) = -1 under CY condition.

        # VERIFIED: [DC] (-h1)(-h2)(-h3)/(h1*h2*h3) = -1; [SY] symmetry.
        """
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        r = mo.evaluate_at_zero()
        assert r["match"] is True
        assert r["g_at_zero"] == Rational(-1)

    def test_g_at_zero_symbolic(self):
        """g(0) = -1 for symbolic h under CY."""
        h1, h2 = Symbol('h1'), Symbol('h2')
        mo = MOStructureFunctionOmega(h1, h2)
        r = mo.evaluate_at_zero()
        assert r["match"] is True

    def test_poles_and_zeros(self):
        """Zeros at h_i, poles at -h_i."""
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        pz = mo.pole_zero_data()
        assert set(pz["zeros"]) == {Rational(1), Rational(2), Rational(-3)}
        assert set(pz["poles"]) == {Rational(-1), Rational(-2), Rational(3)}

    def test_cy_condition_check(self):
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        r = mo.verify_cy_condition()
        assert r["cy_holds"] is True

    def test_cy_condition_fails_when_forced(self):
        """CY condition fails when h3 is independent."""
        mo = MOStructureFunctionOmega(Rational(1), Rational(2), Rational(3))
        r = mo.verify_cy_condition()
        assert r["cy_holds"] is False

    def test_large_z_expansion_leading(self):
        r"""g(z) -> 1 as z -> infinity.

        # VERIFIED: [DC] leading coeff of rational function = 1.
        """
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        exp = mo.large_z_expansion(order=4)
        coeffs = exp["coefficients"]
        assert coeffs.get(0, 0) == 1

    def test_large_z_expansion_1_over_z_vanishes(self):
        """1/z coefficient vanishes under CY (sigma_1 = 0)."""
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        exp = mo.large_z_expansion(order=4)
        coeffs = exp["coefficients"]
        assert coeffs.get(1, 0) == 0

    def test_g_at_zero_of_h1(self):
        r"""g(h1) = 0 (h1 is a zero of g).

        # VERIFIED: [DC] (h1-h1)=0 in numerator.
        """
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        z = Symbol('z')
        g_expr = mo.g(z)
        val = simplify(g_expr.subs(z, Rational(1)))
        assert val == 0

    def test_psi_kappa_identification(self):
        r"""kappa = Psi = h1*h2*h3 for the MO Heisenberg sector.

        # VERIFIED: [DC] kappa(H_Psi) = Psi; [LT] C1; [CF] Heis kappa.
        """
        Psi_val = Rational(-6)
        mo = MOStructureFunctionOmega(Rational(1), Rational(2))
        assert mo.Psi == Psi_val
        assert kappa_heisenberg(Psi_val) == Psi_val


# ======================================================================
#  16. WInfinityChiralQG.verify_all integrated tests
# ======================================================================

class TestWIQGVerifyAll:
    """Full integrated verification via the unified class."""

    def test_verify_all_spin1_only(self):
        """Spin-1 only: all 3 axioms pass."""
        qg = WInfinityChiralQG(Psi=Rational(1), spin_max=1)
        r = qg.verify_all()
        assert r["summary"]["all_pass"] is True
        assert r["summary"]["num_passed"] == 3

    def test_verify_all_spin2(self):
        """Spin 1+2: all 6 axioms pass."""
        qg = WInfinityChiralQG(Psi=Rational(1), spin_max=2)
        r = qg.verify_all()
        assert r["summary"]["all_pass"] is True
        assert r["summary"]["num_passed"] == 6

    def test_verify_all_with_mo(self):
        """Full verification with MO structure function: 9 checks."""
        qg = WInfinityChiralQG(Psi=Rational(-6), spin_max=2)
        r = qg.verify_all(h1=Rational(1), h2=Rational(2))
        assert r["summary"]["all_pass"] is True
        assert r["summary"]["num_passed"] == 9

    @pytest.mark.parametrize("psi_val", [
        Rational(1), Rational(5), Rational(100),
        Rational(1, 7), Rational(-3),
    ])
    def test_verify_all_various_psi(self, psi_val):
        """Verification passes across a range of Psi values."""
        qg = WInfinityChiralQG(Psi=psi_val, spin_max=2)
        r = qg.verify_all()
        assert r["summary"]["all_pass"] is True

    def test_verify_all_symbolic_psi(self):
        """Verification with symbolic Psi (spin-1 only)."""
        Psi = Symbol('Psi')
        qg = WInfinityChiralQG(Psi=Psi, spin_max=1)
        r = qg.verify_all()
        assert r["summary"]["all_pass"] is True

    def test_psi_consistency_check(self):
        """Psi from Omega-background matches WInfinityChiralQG.Psi."""
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        Psi_val = h1 * h2 * h3
        qg = WInfinityChiralQG(Psi=Psi_val, spin_max=2)
        result = qg.mo_structure_function(h1, h2)
        assert result["Psi_consistent"] is True

    def test_psi_inconsistency_detected(self):
        """Psi mismatch is detected."""
        qg = WInfinityChiralQG(Psi=Rational(999), spin_max=2)
        result = qg.mo_structure_function(Rational(1), Rational(2))
        assert result["Psi_consistent"] is False
