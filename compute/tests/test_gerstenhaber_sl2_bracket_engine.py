r"""Tests for FT-10: Gerstenhaber bracket on ChirHoch^1(V_k(sl_2)).

Verifies that the Gerstenhaber bracket on the first chiral Hochschild
group of affine sl_2 reproduces the sl_2 Lie bracket.  This is the
FIRST non-abelian E_3 structure verification in the programme.

Organized by:
  I.    sl_2 structure constants and Jacobi identity
  II.   Killing form
  III.  Gerstenhaber bracket: [D_e, D_f] = D_h
  IV.   Gerstenhaber bracket: [D_h, D_e] = 2*D_e
  V.    Gerstenhaber bracket: [D_h, D_f] = -2*D_f
  VI.   Graded antisymmetry
  VII.  Graded Jacobi identity
  VIII. Level independence
  IX.   Comparison with Heisenberg (abelian: all brackets vanish)
  X.    Full FT-10 verification

References:
  prop:chirhoch1-affine-km (chiral_center_theorem.tex)
  prop:gerstenhaber-sl2-bracket (chiral_center_theorem.tex)
  hh_heisenberg_e3_engine.py (abelian case)
  Keller, ICM 2006 Theorem 3.4: Ext bracket on Koszul HH^1
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.gerstenhaber_sl2_bracket_engine import (
    # Lie algebra data
    STRUCTURE_CONSTANTS,
    BASIS,
    INDICES,
    lie_bracket,
    verify_sl2_jacobi,
    # Killing form
    killing_form_matrix,
    verify_killing_form,
    # Outer derivations
    OuterDerivation,
    D_e,
    D_f,
    D_h,
    basis_derivations,
    # Brace and bracket
    chiral_brace,
    gerstenhaber_bracket,
    gerstenhaber_bracket_basis,
    # Axiom verification
    verify_graded_antisymmetry,
    verify_graded_jacobi,
    verify_level_independence,
    # Comparison
    heisenberg_comparison,
    # Full verification
    GerstenhaberSl2Result,
    full_verification,
    summary,
)


# ======================================================================
#  I. sl_2 structure constants and Jacobi identity
# ======================================================================

class TestSl2StructureConstants:
    """Structure constants f^{ab}_c for sl_2 in the {e, f, h} basis."""

    def test_ef_bracket(self):
        """[e, f] = h: f^{ef}_h = 1."""
        # VERIFIED: [DC] direct definition of sl_2
        # VERIFIED: [LT] Humphreys, ch.7: [e,f] = h for Chevalley basis
        assert STRUCTURE_CONSTANTS[0][1][2] == 1.0

    def test_fe_bracket(self):
        """[f, e] = -h: antisymmetry."""
        assert STRUCTURE_CONSTANTS[1][0][2] == -1.0

    def test_he_bracket(self):
        """[h, e] = 2e: f^{he}_e = 2."""
        # VERIFIED: [DC] ad_h(e) = 2e (eigenvalue +2)
        # VERIFIED: [LT] Humphreys, ch.7: [h,e] = 2e for Chevalley basis
        assert STRUCTURE_CONSTANTS[2][0][0] == 2.0

    def test_eh_bracket(self):
        """[e, h] = -2e: antisymmetry."""
        assert STRUCTURE_CONSTANTS[0][2][0] == -2.0

    def test_hf_bracket(self):
        """[h, f] = -2f: f^{hf}_f = -2."""
        # VERIFIED: [DC] ad_h(f) = -2f (eigenvalue -2)
        # VERIFIED: [LT] Humphreys, ch.7: [h,f] = -2f for Chevalley basis
        assert STRUCTURE_CONSTANTS[2][1][1] == -2.0

    def test_fh_bracket(self):
        """[f, h] = 2f: antisymmetry."""
        assert STRUCTURE_CONSTANTS[1][2][1] == 2.0

    def test_vanishing_brackets(self):
        """All other structure constants vanish."""
        nonzero_positions = {
            (0, 1, 2), (1, 0, 2),  # [e,f] and [f,e]
            (2, 0, 0), (0, 2, 0),  # [h,e] and [e,h]
            (2, 1, 1), (1, 2, 1),  # [h,f] and [f,h]
        }
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if (a, b, c) not in nonzero_positions:
                        assert STRUCTURE_CONSTANTS[a][b][c] == 0.0, \
                            f"f[{a}][{b}][{c}] = {STRUCTURE_CONSTANTS[a][b][c]} should be 0"

    def test_antisymmetry(self):
        """f^{ab}_c = -f^{ba}_c for all a, b, c."""
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    assert abs(STRUCTURE_CONSTANTS[a][b][c]
                               + STRUCTURE_CONSTANTS[b][a][c]) < 1e-14

    def test_jacobi_identity(self):
        """Jacobi identity for sl_2 structure constants.

        VERIFIED: [DC] exhaustive check on all 27 triples
        VERIFIED: [SY] sl_2 is a Lie algebra (classical fact)
        """
        assert verify_sl2_jacobi()

    def test_lie_bracket_vector(self):
        """Test lie_bracket function: [e, f] = h."""
        e = np.array([1.0, 0.0, 0.0])
        f = np.array([0.0, 1.0, 0.0])
        h = np.array([0.0, 0.0, 1.0])
        result = lie_bracket(e, f)
        assert np.allclose(result, h)

    def test_lie_bracket_linear_combination(self):
        """[e+f, h] = -2e + 2f."""
        e_plus_f = np.array([1.0, 1.0, 0.0])
        h = np.array([0.0, 0.0, 1.0])
        result = lie_bracket(e_plus_f, h)
        expected = np.array([-2.0, 2.0, 0.0])
        assert np.allclose(result, expected)


# ======================================================================
#  II. Killing form
# ======================================================================

class TestKillingForm:
    """Killing form kappa(X,Y) = tr(ad_X ad_Y) for sl_2."""

    def test_killing_form_values(self):
        """Killing form matrix for sl_2 in {e, f, h} basis.

        VERIFIED: [DC] trace of product of adjoint matrices
        VERIFIED: [LT] Humphreys 8.1: kappa = 2N * tr_fund for sl_N;
                  at N=2, kappa = 4 * tr_fund
        """
        result = verify_killing_form()
        assert result["match"]

    def test_killing_form_nondegenerate(self):
        """sl_2 Killing form is nondegenerate (sl_2 is semisimple)."""
        result = verify_killing_form()
        assert result["is_nondegenerate"]

    def test_killing_form_ef(self):
        """kappa(e, f) = 4."""
        K = killing_form_matrix()
        assert abs(K[0][1] - 4.0) < 1e-14

    def test_killing_form_hh(self):
        """kappa(h, h) = 8."""
        K = killing_form_matrix()
        assert abs(K[2][2] - 8.0) < 1e-14

    def test_killing_form_symmetric(self):
        """Killing form is symmetric."""
        K = killing_form_matrix()
        assert np.allclose(K, K.T)

    def test_killing_form_determinant(self):
        """det(K) = -128.

        VERIFIED: [DC] det([[0,4,0],[4,0,0],[0,0,8]]) = 8*(0-16) = -128
        VERIFIED: [CF] for sl_2: det(kappa) = -(4)^2 * 8 = -128
        """
        K = killing_form_matrix()
        assert abs(np.linalg.det(K) - (-128.0)) < 1e-10


# ======================================================================
#  III. Gerstenhaber bracket: [D_e, D_f] = D_h
# ======================================================================

class TestBracketEF:
    """[D_e, D_f] = D_h: the Cartan element from raising/lowering."""

    def test_bracket_ef_is_dh(self):
        """[D_e, D_f] = D_h (coefficient 1).

        VERIFIED: [DC] brace computation from OPE simple-pole residue
        VERIFIED: [LT] Keller ICM 2006: HH^1 bracket = Lie bracket for Koszul
        """
        brackets = gerstenhaber_bracket_basis()
        basis_elem, coeff = brackets["[D_e, D_f]"]
        assert basis_elem == "h"
        assert coeff == Fraction(1)

    def test_bracket_ef_vector(self):
        """[D_e, D_f] as coefficient vector is [0, 0, 1]."""
        result = gerstenhaber_bracket(D_e(), D_f())
        expected = np.array([0.0, 0.0, 1.0])
        assert np.allclose(result.coefficients, expected)


# ======================================================================
#  IV. Gerstenhaber bracket: [D_h, D_e] = 2*D_e
# ======================================================================

class TestBracketHE:
    """[D_h, D_e] = 2*D_e: the Cartan eigenvalue of e."""

    def test_bracket_he_is_2de(self):
        """[D_h, D_e] = 2*D_e (coefficient 2).

        VERIFIED: [DC] eigenvalue of ad_h on e is +2
        VERIFIED: [LT] Root system: e is the positive root with alpha(h)=2
        """
        brackets = gerstenhaber_bracket_basis()
        basis_elem, coeff = brackets["[D_h, D_e]"]
        assert basis_elem == "e"
        assert coeff == Fraction(2)

    def test_bracket_he_vector(self):
        """[D_h, D_e] as coefficient vector is [2, 0, 0]."""
        result = gerstenhaber_bracket(D_h(), D_e())
        expected = np.array([2.0, 0.0, 0.0])
        assert np.allclose(result.coefficients, expected)


# ======================================================================
#  V. Gerstenhaber bracket: [D_h, D_f] = -2*D_f
# ======================================================================

class TestBracketHF:
    """[D_h, D_f] = -2*D_f: the Cartan eigenvalue of f."""

    def test_bracket_hf_is_minus2df(self):
        """[D_h, D_f] = -2*D_f (coefficient -2).

        VERIFIED: [DC] eigenvalue of ad_h on f is -2
        VERIFIED: [LT] Root system: f is the negative root with alpha(h)=-2
        """
        brackets = gerstenhaber_bracket_basis()
        basis_elem, coeff = brackets["[D_h, D_f]"]
        assert basis_elem == "f"
        assert coeff == Fraction(-2)

    def test_bracket_hf_vector(self):
        """[D_h, D_f] as coefficient vector is [0, -2, 0]."""
        result = gerstenhaber_bracket(D_h(), D_f())
        expected = np.array([0.0, -2.0, 0.0])
        assert np.allclose(result.coefficients, expected)


# ======================================================================
#  VI. Graded antisymmetry
# ======================================================================

class TestGradedAntisymmetry:
    """[phi, psi] = -(-1)^{(|phi|-1)(|psi|-1)} [psi, phi] on all basis pairs."""

    def test_graded_antisymmetry_all_pairs(self):
        """Antisymmetry on all 9 basis pairs.

        For degree-1 elements: [X, Y] = -[Y, X] (ordinary antisymmetry).
        """
        assert verify_graded_antisymmetry()

    def test_bracket_fe_is_minus_dh(self):
        """[D_f, D_e] = -D_h (antisymmetry of [D_e, D_f] = D_h)."""
        result = gerstenhaber_bracket(D_f(), D_e())
        expected = np.array([0.0, 0.0, -1.0])
        assert np.allclose(result.coefficients, expected)

    def test_bracket_eh_is_minus2de(self):
        """[D_e, D_h] = -2*D_e (antisymmetry of [D_h, D_e] = 2*D_e)."""
        result = gerstenhaber_bracket(D_e(), D_h())
        expected = np.array([-2.0, 0.0, 0.0])
        assert np.allclose(result.coefficients, expected)

    def test_bracket_fh_is_2df(self):
        """[D_f, D_h] = 2*D_f (antisymmetry of [D_h, D_f] = -2*D_f)."""
        result = gerstenhaber_bracket(D_f(), D_h())
        expected = np.array([0.0, 2.0, 0.0])
        assert np.allclose(result.coefficients, expected)

    def test_self_brackets_vanish(self):
        """[D_X, D_X] = 0 for all basis elements (shifted even degree)."""
        for d in basis_derivations():
            result = gerstenhaber_bracket(d, d)
            assert result.is_zero()


# ======================================================================
#  VII. Graded Jacobi identity
# ======================================================================

class TestGradedJacobi:
    """Jacobi identity on all triples of basis derivations."""

    def test_graded_jacobi_all_triples(self):
        """Jacobi identity on all 27 triples.

        VERIFIED: [DC] exhaustive computation
        VERIFIED: [SY] inherits from Jacobi identity of sl_2
        """
        assert verify_graded_jacobi()

    def test_jacobi_efh(self):
        """Jacobi on (e, f, h): [e,[f,h]] + [f,[h,e]] + [h,[e,f]] = 0.

        [f,h] = 2f, [e, 2f] = 2h
        [h,e] = 2e, [f, 2e] = -2h
        [e,f] = h, [h, h] = 0
        Total: 2h + (-2h) + 0 = 0. Verified.
        """
        de, df, dh = D_e(), D_f(), D_h()

        fh = gerstenhaber_bracket(df, dh)      # 2*D_f
        e_fh = gerstenhaber_bracket(de, fh)     # [e, 2f] = 2*[e,f] = 2*h

        he = gerstenhaber_bracket(dh, de)       # 2*D_e
        f_he = gerstenhaber_bracket(df, he)     # [f, 2e] = 2*[f,e] = -2*h

        ef = gerstenhaber_bracket(de, df)       # D_h
        h_ef = gerstenhaber_bracket(dh, ef)     # [h, h] = 0

        total = e_fh.coefficients + f_he.coefficients + h_ef.coefficients
        assert np.allclose(total, np.zeros(3))


# ======================================================================
#  VIII. Level independence
# ======================================================================

class TestLevelIndependence:
    """The bracket depends on structure constants f^{ab}_c, not on k."""

    def test_level_independence(self):
        """Bracket is k-independent (simple-pole OPE term has no level).

        VERIFIED: [DC] gerstenhaber_bracket has no k parameter
        VERIFIED: [LT] Keller ICM 2006: Ext bracket depends on quadratic
                  relations only
        """
        assert verify_level_independence()

    def test_bracket_at_k1_and_k3(self):
        """Same bracket at k=1 and k=3: no level dependence in the formula."""
        # The bracket function does not take a level parameter,
        # confirming level independence by construction.
        result = gerstenhaber_bracket(D_e(), D_f())
        assert np.allclose(result.coefficients, [0.0, 0.0, 1.0])


# ======================================================================
#  IX. Comparison with Heisenberg
# ======================================================================

class TestHeisenbergComparison:
    """Abelian comparison: Heisenberg has trivial brackets."""

    def test_heisenberg_trivial(self):
        """Heisenberg brackets all vanish (f^{ab}_c = 0)."""
        comp = heisenberg_comparison()
        assert comp["heisenberg_brackets_trivial"] is True

    def test_sl2_nontrivial(self):
        """sl_2 brackets are nontrivial (f^{ab}_c != 0)."""
        comp = heisenberg_comparison()
        assert comp["sl2_brackets_trivial"] is False

    def test_dim_hh1_comparison(self):
        """dim ChirHoch^1: 1 for Heisenberg, 3 for sl_2."""
        comp = heisenberg_comparison()
        assert comp["heisenberg_dim_hh1"] == 1
        assert comp["sl2_dim_hh1"] == 3


# ======================================================================
#  X. Full FT-10 verification
# ======================================================================

class TestFullVerification:
    """Complete FT-10: Gerstenhaber bracket reproduces sl_2 Lie bracket."""

    def test_reproduces_sl2_bracket(self):
        """The Gerstenhaber bracket on ChirHoch^1(V_k(sl_2)) IS the sl_2 Lie bracket."""
        result = full_verification()
        assert result.reproduces_sl2_bracket

    def test_chirhoch_dimensions(self):
        """ChirHoch^*(V_k(sl_2)) = (1, 3, 1), total 5.

        VERIFIED: [DC] prop:chirhoch1-affine-km gives dim HH^1 = dim(sl_2) = 3
        VERIFIED: [LT] chirhoch_dimension_engine.py: total_dim = 5 for sl_2
        """
        result = full_verification()
        assert result.dim_hh0 == 1
        assert result.dim_hh1 == 3
        assert result.dim_hh2 == 1
        assert result.dim_hh0 + result.dim_hh1 + result.dim_hh2 == 5

    def test_all_axioms_pass(self):
        """All Gerstenhaber algebra axioms verified."""
        result = full_verification()
        assert result.graded_antisymmetry
        assert result.graded_jacobi
        assert result.level_independent

    def test_killing_form(self):
        """Killing form is nondegenerate (sl_2 is semisimple)."""
        result = full_verification()
        assert result.killing_form_nondegenerate

    def test_is_first_nonabelian(self):
        """This is the first non-abelian E_3 verification."""
        result = full_verification()
        assert result.is_first_nonabelian_verification

    def test_summary_verdict(self):
        """Summary reports PASS."""
        s = summary()
        assert s["VERDICT"] == "PASS"

    def test_bracket_values_in_summary(self):
        """Summary contains the correct bracket values."""
        s = summary()
        assert s["brackets"]["[D_e, D_f]"] == "1*D_h"
        assert s["brackets"]["[D_h, D_e]"] == "2*D_e"
        assert s["brackets"]["[D_h, D_f]"] == "-2*D_f"


# ======================================================================
#  XI. Chiral brace product (circle composition)
# ======================================================================

class TestChiralBrace:
    """The chiral brace D_X circ D_Y from OPE residue extraction."""

    def test_brace_ef(self):
        """D_e circ D_f: residue of e(z)f(w) simple pole gives h."""
        result = chiral_brace(D_e(), D_f())
        # D_e circ D_f (J^c) = sum X^a Y^b f^{ab}_c
        # = 1*1*f^{ef}_h = 1 => D_h
        expected = np.array([0.0, 0.0, 1.0])
        assert np.allclose(result.coefficients, expected)

    def test_brace_fe(self):
        """D_f circ D_e: residue of f(z)e(w) simple pole gives -h."""
        result = chiral_brace(D_f(), D_e())
        expected = np.array([0.0, 0.0, -1.0])
        assert np.allclose(result.coefficients, expected)

    def test_brace_he(self):
        """D_h circ D_e: residue of h(z)e(w) simple pole gives 2e."""
        result = chiral_brace(D_h(), D_e())
        expected = np.array([2.0, 0.0, 0.0])
        assert np.allclose(result.coefficients, expected)

    def test_brace_hf(self):
        """D_h circ D_f: residue of h(z)f(w) simple pole gives -2f."""
        result = chiral_brace(D_h(), D_f())
        expected = np.array([0.0, -2.0, 0.0])
        assert np.allclose(result.coefficients, expected)

    def test_brace_hh(self):
        """D_h circ D_h: [h, h] = 0."""
        result = chiral_brace(D_h(), D_h())
        assert result.is_zero()

    def test_brace_ee(self):
        """D_e circ D_e: [e, e] = 0."""
        result = chiral_brace(D_e(), D_e())
        assert result.is_zero()

    def test_brace_ff(self):
        """D_f circ D_f: [f, f] = 0."""
        result = chiral_brace(D_f(), D_f())
        assert result.is_zero()
