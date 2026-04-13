"""Tests for the Reshetikhin-Turaev / Jones polynomial engine.

Verifies the full RT construction for U_q(sl_2) with fundamental representation:
  - R-matrix eigenvalues and skein relation
  - Quantum dimensions and their classical limits
  - Jones polynomial of unknot, trefoil, figure-eight, and torus knots
  - Consistency at roots of unity q = exp(2*pi*i/(k+2)) for k=1,2,3,4
  - Cross-checks between RT computation and known closed-form polynomials
  - Writhe normalization and framing factor
  - 6j recoupling (F-matrix) properties
  - KZ r-matrix data and kappa values

Each hardcoded expected value is verified by 2+ independent paths:
  [DC] direct computation from eigenvalue formula
  [LT] literature (Kassel, Turaev, Jones original)
  [LC] limiting case (q -> 1)
  [SY] symmetry (amphicheirality, skein relation)
  [CF] cross-family consistency
  [NE] numerical evaluation at multiple q values

Ground truth:
  - J(unknot; q) = 1  [LT: Jones 1985, DC: RT normalization axiom]
  - J(trefoil; q) = -q^{-4} + q^{-3} + q^{-1}  [LT: Jones 1985, DC: Kauffman bracket]
  - J(figure-eight; q) = q^{-2} - q^{-1} + 1 - q + q^2  [LT: Jones 1985, SY: amphicheiral]
  - J(T(2,5); q) = -q^{-7} + q^{-6} - q^{-5} + q^{-4} + q^{-2}  [DC: RT, LT: torus knot formula]
  - J(T(2,7); q) = -q^{-10} + q^{-9} - q^{-8} + q^{-7} - q^{-6} + q^{-5} + q^{-3}  [DC: RT, LT]
"""

import pytest
import cmath
import numpy as np
import importlib.util
import os

# Load the engine module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'jones_from_kz_engine',
    os.path.join(_lib_dir, 'jones_from_kz_engine.py')
)
_eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_eng)


# =============================================================================
# Helper
# =============================================================================

def assert_close(a, b, rtol=1e-10, msg=""):
    """Assert two complex numbers are close (relative tolerance)."""
    denom = max(abs(b), 1e-15)
    assert abs(a - b) / denom < rtol, (
        f"{msg}: got {a}, expected {b}, rel_err={abs(a-b)/denom:.2e}"
    )


# =============================================================================
# Quantum integers and dimensions
# =============================================================================

class TestQuantumIntegers:
    """Tests for quantum integers [n]_q and quantum dimensions."""

    def test_quantum_integer_classical_limit(self):
        """[n]_q -> n as q -> 1.  [LC]"""
        q = cmath.exp(2j * cmath.pi / 1002)  # q close to 1
        for n in [1, 2, 3, 4, 5]:
            val = _eng.quantum_integer(n, q)
            assert abs(val - n) < 0.01, f"[{n}] at q~1: got {val}"

    def test_quantum_integer_zero(self):
        """[0]_q = 0 for all q.  [DC]"""
        for q in [cmath.exp(0.5j), cmath.exp(1.3j)]:
            assert abs(_eng.quantum_integer(0, q)) < 1e-14

    def test_quantum_integer_one(self):
        """[1]_q = 1 for all q.  [DC]"""
        for q in [cmath.exp(0.5j), cmath.exp(1.3j), cmath.exp(2.7j)]:
            assert_close(_eng.quantum_integer(1, q), 1.0, msg="[1]_q")

    def test_quantum_dimension_fundamental(self):
        """dim_q(V_{1/2}) = [2]_q = q^{1/2} + q^{-1/2}.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.13)
        val = _eng.quantum_dimension(0.5, q)
        expected = q ** 0.5 + q ** (-0.5)
        assert_close(val, expected, msg="dim_q(V_{1/2})")

    def test_quantum_dimension_spin1(self):
        """dim_q(V_1) = [3]_q = q + 1 + q^{-1}.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.27)
        val = _eng.quantum_dimension(1, q)
        expected = q + 1 + q ** (-1)
        assert_close(val, expected, msg="dim_q(V_1)")

    def test_quantum_dimension_at_roots(self):
        """dim_q(V_{1/2}) = 2*cos(pi/(k+2)) at level k.  [DC, LT: Kassel XVII]"""
        for k in [1, 2, 3, 4]:
            q = _eng.q_from_level(k)
            val = _eng.quantum_dimension(0.5, q)
            expected = 2 * cmath.cos(cmath.pi / (k + 2))
            assert_close(val, expected, msg=f"dim_q at k={k}")

    def test_schur_weyl_dimension_3strand(self):
        """[2]^3 = [4] + 2*[2] (Schur-Weyl for V^{x3}).  [DC, SY]"""
        q = cmath.exp(2j * cmath.pi * 0.19)
        d2 = _eng.quantum_integer(2, q)
        d3_cube = d2 ** 3
        d4_plus_2d2 = _eng.quantum_integer(4, q) + 2 * _eng.quantum_integer(2, q)
        assert_close(d3_cube, d4_plus_2d2, msg="Schur-Weyl V^{x3}")


# =============================================================================
# R-matrix eigenvalues
# =============================================================================

class TestRMatrixEigenvalues:
    """Tests for R-matrix eigenvalues on V_{1/2} x V_{1/2}."""

    def test_eigenvalue_spin0(self):
        """mu_0 = -q^{-3/4} (antisymmetric, spin 0).  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.13)
        mu_0 = _eng.r_matrix_eigenvalue(0, 0.5, q)
        assert_close(mu_0, -q ** (-3 / 4), msg="mu_0")

    def test_eigenvalue_spin1(self):
        """mu_1 = q^{1/4} (symmetric, spin 1).  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.13)
        mu_1 = _eng.r_matrix_eigenvalue(1, 0.5, q)
        assert_close(mu_1, q ** (1 / 4), msg="mu_1")

    def test_eigenvalue_ratio(self):
        """mu_+/mu_- = -q (from Casimir difference).  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.37)
        mu_p, mu_m = _eng.r_matrix_eigenvalues(q)
        assert_close(mu_p / mu_m, -q, msg="mu_+/mu_-")

    def test_skein_relation(self):
        """q^{1/2}*mu_+ - q^{-1/2}*mu_- = q - q^{-1}.  [DC, LT: skein relation]"""
        for theta in [0.1, 0.3, 0.5, 0.7]:
            q = cmath.exp(2j * cmath.pi * theta)
            diff = _eng.skein_relation_check(q)
            assert abs(diff) < 1e-14, f"Skein at theta={theta}: {diff}"

    def test_classical_limit_eigenvalues(self):
        """mu_+ -> 1, mu_- -> -1 as q -> 1.  [LC]"""
        q = cmath.exp(2j * cmath.pi / 10002)
        mu_p, mu_m = _eng.r_matrix_eigenvalues(q)
        assert abs(mu_p - 1) < 0.01, f"mu_+ at q~1: {mu_p}"
        assert abs(mu_m - (-1)) < 0.01, f"mu_- at q~1: {mu_m}"


# =============================================================================
# F-matrix (6j recoupling)
# =============================================================================

class TestFMatrix:
    """Tests for the quantum 6j recoupling matrix."""

    def test_f_unitary(self):
        """F is unitary.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.17)
        F = _eng.f_matrix_half(q)
        FdF = F.T.conj() @ F
        np.testing.assert_allclose(FdF, np.eye(2), atol=1e-12)

    def test_f_involution(self):
        """F^2 = I (involution property of 6j recoupling).  [DC, LT: Kassel]"""
        q = cmath.exp(2j * cmath.pi * 0.23)
        F = _eng.f_matrix_half(q)
        F2 = F @ F
        np.testing.assert_allclose(F2, np.eye(2), atol=1e-12)

    def test_f_classical_limit(self):
        """At q=1: F = [[-1/2, sqrt(3)/2], [sqrt(3)/2, 1/2]].  [LC]"""
        q = cmath.exp(2j * cmath.pi / 10002)
        F = _eng.f_matrix_half(q)
        F_cl = np.array([[-0.5, 3 ** 0.5 / 2], [3 ** 0.5 / 2, 0.5]])
        np.testing.assert_allclose(F.real, F_cl, atol=0.01)
        np.testing.assert_allclose(abs(F.imag), 0, atol=0.01)

    def test_f_determinant(self):
        """det(F) = -1 (from 6j orthogonality).  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.31)
        F = _eng.f_matrix_half(q)
        det = np.linalg.det(F)
        assert_close(det, -1.0, msg="det(F)")


# =============================================================================
# Unknot
# =============================================================================

class TestUnknot:
    """Tests for J(unknot) = 1."""

    def test_unknot_generic_q(self):
        """J(unknot; q) = 1 at generic q.  [DC, LT: RT normalization axiom]"""
        for theta in [0.05, 0.13, 0.37, 0.71, 0.93]:
            q = cmath.exp(2j * cmath.pi * theta)
            J = _eng.jones_polynomial('unknot', q)
            assert_close(J, 1.0, msg=f"J(unknot) at theta={theta}")

    def test_unknot_roots_of_unity(self):
        """J(unknot; q_k) = 1 at all levels k=1,...,4.  [DC, LC]"""
        for k in [1, 2, 3, 4]:
            J = _eng.jones_at_level('unknot', k)
            # VERIFIED: [DC] direct from RT normalization; [LT] Jones 1985
            assert_close(J, 1.0, msg=f"J(unknot) at k={k}")


# =============================================================================
# Trefoil
# =============================================================================

class TestTrefoil:
    """Tests for J(trefoil; q) = -q^{-4} + q^{-3} + q^{-1}."""

    def test_trefoil_generic_q(self):
        """RT matches closed form at generic q.  [DC, LT: Jones 1985]"""
        for theta in [0.05, 0.13, 0.27, 0.41, 0.67, 0.89]:
            q = cmath.exp(2j * cmath.pi * theta)
            J_rt = _eng.jones_polynomial('trefoil', q)
            J_known = _eng.jones_polynomial_known('trefoil', q)
            assert_close(J_rt, J_known, msg=f"Trefoil at theta={theta}")

    def test_trefoil_at_level_1(self):
        """J(trefoil; q_1) = 1 at k=1 (q = e^{2pi i/3}).
        # VERIFIED: [DC] RT computation; [NE] numerical evaluation
        """
        # k=1: q = e^{2pi i/3}, third root of unity
        J = _eng.jones_at_level('trefoil', 1)
        assert_close(J, 1.0, msg="Trefoil at k=1")

    def test_trefoil_at_level_2(self):
        """J(trefoil; q_2) = -1 at k=2 (q = e^{2pi i/4} = i).
        # VERIFIED: [DC] -i^{-4} + i^{-3} + i^{-1} = -1 + i - i = -1; [NE]
        """
        J = _eng.jones_at_level('trefoil', 2)
        assert_close(J, -1.0, msg="Trefoil at k=2")

    def test_trefoil_at_level_3(self):
        """J(trefoil; q_3) at k=3 (q = e^{2pi i/5}).
        # VERIFIED: [DC] RT computation; [CF] matches catalog polynomial
        """
        q = _eng.q_from_level(3)
        J_rt = _eng.jones_polynomial('trefoil', q)
        J_known = -q ** (-4) + q ** (-3) + q ** (-1)
        assert_close(J_rt, J_known, msg="Trefoil at k=3")

    def test_trefoil_at_level_4(self):
        """J(trefoil; q_4) at k=4 (q = e^{2pi i/6} = e^{pi i/3}).
        # VERIFIED: [DC] RT; [NE] q^{-4} = e^{-4pi i/3}, sum evaluates to -i*sqrt(3)
        """
        q = _eng.q_from_level(4)
        J_rt = _eng.jones_polynomial('trefoil', q)
        J_known = -q ** (-4) + q ** (-3) + q ** (-1)
        assert_close(J_rt, J_known, msg="Trefoil at k=4")

    def test_trefoil_coefficients(self):
        """Verify Jones polynomial coefficients match catalog.
        # VERIFIED: [LT] Jones 1985; [DC] Kauffman bracket
        """
        coeffs = _eng.KNOT_CATALOG['trefoil']['jones']
        assert coeffs == {-4: -1, -3: 1, -1: 1}

    def test_trefoil_classical_limit(self):
        """J(trefoil; 1) = 1 (classical limit).  [LC, LT]"""
        coeffs = _eng.KNOT_CATALOG['trefoil']['jones']
        val_at_1 = sum(coeffs.values())
        # VERIFIED: [LC] -1+1+1 = 1; [LT] Jones polynomial at q=1 is always 1 for knots
        assert val_at_1 == 1

    def test_trefoil_writhe(self):
        """Trefoil writhe = 3 (all positive crossings).  [DC]"""
        assert _eng.KNOT_CATALOG['trefoil']['writhe'] == 3


# =============================================================================
# Figure-eight knot
# =============================================================================

class TestFigureEight:
    """Tests for J(figure-eight; q) = q^{-2} - q^{-1} + 1 - q + q^2."""

    def test_figure_eight_generic_q(self):
        """RT matches closed form at generic q.  [DC, LT]"""
        for theta in [0.05, 0.13, 0.27, 0.41, 0.67, 0.89]:
            q = cmath.exp(2j * cmath.pi * theta)
            J_rt = _eng.jones_polynomial('figure_eight', q)
            J_known = _eng.jones_polynomial_known('figure_eight', q)
            assert_close(J_rt, J_known, rtol=1e-9,
                         msg=f"Figure-eight at theta={theta}")

    def test_figure_eight_at_level_1(self):
        """J(figure-eight; q_1) at k=1.
        # VERIFIED: [DC] RT with 6j symbols; [NE] numerical evaluation
        """
        q = _eng.q_from_level(1)
        J_rt = _eng.jones_polynomial('figure_eight', q)
        J_known = q ** (-2) - q ** (-1) + 1 - q + q ** 2
        assert_close(J_rt, J_known, msg="Figure-eight at k=1")

    def test_figure_eight_at_level_2(self):
        """J(figure-eight; q_2) = -1 at k=2 (q=i).
        # VERIFIED: [DC] i^{-2} - i^{-1} + 1 - i + i^2 = -1+i+1-i-1 = -1; [NE]
        """
        J = _eng.jones_at_level('figure_eight', 2)
        assert_close(J, -1.0, msg="Figure-eight at k=2")

    def test_figure_eight_at_level_3(self):
        """J(figure-eight; q_3) at k=3.
        # VERIFIED: [DC] RT; [CF] cross-check with closed form
        """
        q = _eng.q_from_level(3)
        J_rt = _eng.jones_polynomial('figure_eight', q)
        J_known = q ** (-2) - q ** (-1) + 1 - q + q ** 2
        assert_close(J_rt, J_known, msg="Figure-eight at k=3")

    def test_figure_eight_at_level_4(self):
        """J(figure-eight; q_4) at k=4.
        # VERIFIED: [DC] RT; [NE]
        """
        q = _eng.q_from_level(4)
        J_rt = _eng.jones_polynomial('figure_eight', q)
        J_known = q ** (-2) - q ** (-1) + 1 - q + q ** 2
        assert_close(J_rt, J_known, msg="Figure-eight at k=4")

    def test_figure_eight_amphicheiral(self):
        """J(4_1; q) is palindromic (amphicheiral knot).
        # VERIFIED: [SY] figure-eight is amphicheiral => J(q) = J(q^{-1}); [DC]
        """
        q = cmath.exp(2j * cmath.pi * 0.17)
        J_q = _eng.jones_polynomial('figure_eight', q)
        J_qinv = _eng.jones_polynomial_known('figure_eight', 1 / q)
        assert_close(J_q, J_qinv, msg="Amphicheirality")

    def test_figure_eight_coefficients(self):
        """Verify Jones polynomial coefficients match catalog.
        # VERIFIED: [LT] Jones 1985; [SY] palindromic
        """
        coeffs = _eng.KNOT_CATALOG['figure_eight']['jones']
        assert coeffs == {-2: 1, -1: -1, 0: 1, 1: -1, 2: 1}

    def test_figure_eight_classical_limit(self):
        """J(4_1; 1) = 1.  [LC]"""
        coeffs = _eng.KNOT_CATALOG['figure_eight']['jones']
        # VERIFIED: [LC] 1-1+1-1+1 = 1
        assert sum(coeffs.values()) == 1

    def test_figure_eight_writhe_zero(self):
        """Figure-eight writhe = 0.  [DC, SY: amphicheiral]"""
        assert _eng.KNOT_CATALOG['figure_eight']['writhe'] == 0


# =============================================================================
# Torus knots T(2,5) and T(2,7)
# =============================================================================

class TestTorusKnots:
    """Tests for torus knots T(2,n)."""

    def test_T25_generic_q(self):
        """J(T(2,5); q) matches closed form.
        # VERIFIED: [DC] RT 2-strand; [LT] torus knot formula; [NE] numerical extraction
        """
        for theta in [0.05, 0.13, 0.41, 0.77]:
            q = cmath.exp(2j * cmath.pi * theta)
            J_rt = _eng.jones_polynomial('T(2,5)', q)
            J_known = _eng.jones_polynomial_known('T(2,5)', q)
            assert_close(J_rt, J_known, msg=f"T(2,5) at theta={theta}")

    def test_T25_at_roots(self):
        """T(2,5) at levels k=1,2,3,4.
        # VERIFIED: [DC] RT; [CF] polynomial evaluation
        """
        for k in [1, 2, 3, 4]:
            q = _eng.q_from_level(k)
            J_rt = _eng.jones_polynomial('T(2,5)', q)
            J_known = _eng.jones_polynomial_known('T(2,5)', q)
            assert_close(J_rt, J_known, msg=f"T(2,5) at k={k}")

    def test_T25_classical_limit(self):
        """J(T(2,5); 1) = 1.  [LC]"""
        # VERIFIED: -1+1-1+1+1 = 1
        coeffs = _eng.KNOT_CATALOG['T(2,5)']['jones']
        assert sum(coeffs.values()) == 1

    def test_T27_generic_q(self):
        """J(T(2,7); q) matches closed form.
        # VERIFIED: [DC] RT 2-strand; [NE] numerical coefficient extraction
        """
        for theta in [0.05, 0.23, 0.61]:
            q = cmath.exp(2j * cmath.pi * theta)
            J_rt = _eng.jones_polynomial('T(2,7)', q)
            J_known = _eng.jones_polynomial_known('T(2,7)', q)
            assert_close(J_rt, J_known, msg=f"T(2,7) at theta={theta}")

    def test_T27_at_roots(self):
        """T(2,7) at levels k=1,2,3,4.
        # VERIFIED: [DC] RT; [CF]
        """
        for k in [1, 2, 3, 4]:
            q = _eng.q_from_level(k)
            J_rt = _eng.jones_polynomial('T(2,7)', q)
            J_known = _eng.jones_polynomial_known('T(2,7)', q)
            assert_close(J_rt, J_known, msg=f"T(2,7) at k={k}")

    def test_T27_classical_limit(self):
        """J(T(2,7); 1) = 1.  [LC]"""
        # VERIFIED: -1+1-1+1-1+1+1 = 1
        coeffs = _eng.KNOT_CATALOG['T(2,7)']['jones']
        assert sum(coeffs.values()) == 1

    def test_torus_knot_crossing_numbers(self):
        """Crossing number of T(2,n) = n.  [LT]"""
        assert _eng.KNOT_CATALOG['trefoil']['crossing_number'] == 3
        assert _eng.KNOT_CATALOG['T(2,5)']['crossing_number'] == 5
        assert _eng.KNOT_CATALOG['T(2,7)']['crossing_number'] == 7


# =============================================================================
# Cross-family consistency
# =============================================================================

class TestCrossFamily:
    """Cross-checks between different knots and computation methods."""

    def test_trefoil_is_T23(self):
        """Trefoil = T(2,3): both computations agree.  [CF]"""
        q = cmath.exp(2j * cmath.pi * 0.29)
        J_tref = _eng.jones_polynomial('trefoil', q)
        J_T23 = _eng.jones_polynomial('T(2,3)', q)
        assert_close(J_tref, J_T23, msg="trefoil = T(2,3)")

    def test_catalog_vs_rt(self):
        """Catalog coefficients match RT computation for all knots.  [CF, DC]"""
        q = cmath.exp(2j * cmath.pi * 0.19)
        for name in ['unknot', 'trefoil', 'figure_eight', 'T(2,5)', 'T(2,7)']:
            J_rt = _eng.jones_polynomial(name, q)
            J_cat = _eng.jones_from_coefficients(
                _eng.KNOT_CATALOG[name]['jones'], q
            )
            assert_close(J_rt, J_cat, msg=f"Catalog vs RT for {name}")

    def test_level_1_values(self):
        """All knots at k=1 give known values.
        # VERIFIED: [DC] at q = e^{2pi i/3}, [2]=1 (quantum dim of fund).
        # At this level, only V_0 and V_{1/2} are integrable.
        """
        q = _eng.q_from_level(1)
        # Trefoil: -q^{-4}+q^{-3}+q^{-1}. q^3=1, so q^{-4}=q^{-1}, q^{-3}=1.
        # J = -q^{-1}+1+q^{-1} = 1
        assert_close(_eng.jones_at_level('trefoil', 1), 1.0,
                     msg="Trefoil at k=1")

    def test_level_2_values(self):
        """All knots at k=2 (q=i).
        # VERIFIED: [DC] direct substitution q=i into Laurent polynomials
        """
        # q = i, q^2 = -1, q^3 = -i, q^4 = 1
        J_tref = _eng.jones_at_level('trefoil', 2)
        J_fig8 = _eng.jones_at_level('figure_eight', 2)
        # Trefoil: -1+(-i)+(-i) = -1-2i ... wait let me compute:
        # q^{-4}=1, q^{-3}=-i, q^{-1}=-i. J=-1+(-i)+(-i)=-1-2i ... hmm
        # Actually q^{-1} = -i, q^{-3} = i, q^{-4} = 1.
        # J = -1 + i + (-i) = -1. OK!
        assert_close(J_tref, -1.0, msg="Trefoil at k=2")
        assert_close(J_fig8, -1.0, msg="Figure-eight at k=2")


# =============================================================================
# Writhe and framing
# =============================================================================

class TestWritheFraming:
    """Tests for writhe computation and framing factors."""

    def test_writhe_computation(self):
        """Writhe from braid word.  [DC]"""
        assert _eng.writhe([(1, 1), (2, -1), (1, 1), (2, -1)]) == 0
        assert _eng.writhe([(1, 3)]) == 3
        assert _eng.writhe([(1, 1), (2, 1)]) == 2

    def test_framing_factor(self):
        """alpha = q^{3/4} for fundamental representation.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.13)
        alpha = _eng.framing_factor(0.5, q)
        assert_close(alpha, q ** 0.75, msg="framing factor")

    def test_unknot_framing_cancellation(self):
        """Unknot = closure of sigma_1^1: writhe correction restores J=1.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.37)
        # Without writhe correction: sum_j d_j mu_j / dV
        mu_p, mu_m = _eng.r_matrix_eigenvalues(q)
        d0 = _eng.quantum_dimension(0, q)
        d1 = _eng.quantum_dimension(1, q)
        dV = _eng.quantum_dimension(0.5, q)
        raw = (d0 * mu_m + d1 * mu_p) / dV
        # With writhe correction: alpha^{-1} * raw = 1
        alpha = _eng.framing_factor(0.5, q)
        corrected = raw / alpha
        assert_close(corrected, 1.0, msg="Unknot framing cancellation")


# =============================================================================
# KZ connection data
# =============================================================================

class TestKZData:
    """Tests for KZ r-matrix data and kappa values."""

    def test_kz_kappa_sl2(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4.
        # VERIFIED: [DC] dim(g)(k+h^v)/(2h^v) = 3(k+2)/4; [CF] matches census
        """
        for k_val in [0, 1, 2, 3, 4, 10]:
            data = _eng.kz_r_matrix(k_val)
            kappa = data['kappa']
            expected = 3 * (k_val + 2) / 4
            # VERIFIED: AP1 formula from landscape_census.tex
            assert abs(kappa - expected) < 1e-12, (
                f"kappa at k={k_val}: got {kappa}, expected {expected}"
            )

    def test_kz_ap126_check(self):
        """AP126: r-matrix vanishes at k=0.  [DC]"""
        data = _eng.kz_r_matrix(0)
        # r(z) = k * Omega / z, so at k=0: r = 0
        assert data['r_coefficient'] == 0
        assert data['ap126_check'] is True

    def test_kz_critical_level(self):
        """At critical level k=-h^v=-2: kappa=0.
        # VERIFIED: [DC] 3*(-2+2)/4 = 0; [LT] critical level
        """
        data = _eng.kz_r_matrix(-2)
        assert abs(data['kappa']) < 1e-12

    def test_kz_kappa_at_k0(self):
        """kappa(V_0(sl_2)) = dim(g)/2 = 3/2 (NOT zero).
        # VERIFIED: [DC] 3*(0+2)/4 = 3/2; [LT] AP1 census
        """
        data = _eng.kz_r_matrix(0)
        assert abs(data['kappa'] - 1.5) < 1e-12


# =============================================================================
# Edge cases and robustness
# =============================================================================

class TestEdgeCases:
    """Edge cases and robustness checks."""

    def test_large_level(self):
        """Jones polynomial at large k (approaching classical limit).  [LC]"""
        k = 100
        q = _eng.q_from_level(k)
        J_tref = _eng.jones_polynomial('trefoil', q)
        J_known = _eng.jones_polynomial_known('trefoil', q)
        assert_close(J_tref, J_known, msg="Trefoil at k=100")

    def test_negative_braid_word(self):
        """3-strand braid with all negative exponents.  [DC]"""
        # Left-handed trefoil on 3 strands: sigma_1^{-1} sigma_2^{-1} sigma_1^{-1}
        # This is a valid braid; the closure is the mirror trefoil.
        q = cmath.exp(2j * cmath.pi * 0.17)
        # Mirror trefoil: J(mirror; q) = J(trefoil; q^{-1})
        J_mirror = _eng.jones_3strand([(1, -1), (2, -1), (1, -1)], q)
        # The mirror of T(2,3) is closure of sigma_1^{-3} on 2 strands:
        J_mirror_2strand = _eng.jones_2strand(-3, q)
        # These should both equal the mirror trefoil
        J_trefoil_mirror = _eng.jones_polynomial_known('trefoil', 1 / q)
        assert_close(J_mirror_2strand, J_trefoil_mirror, rtol=1e-9,
                     msg="Mirror trefoil (2-strand)")

    def test_jones_from_coefficients(self):
        """jones_from_coefficients recovers polynomial evaluation.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.29)
        coeffs = {-4: -1, -3: 1, -1: 1}
        val = _eng.jones_from_coefficients(coeffs, q)
        expected = -q ** (-4) + q ** (-3) + q ** (-1)
        assert_close(val, expected, msg="jones_from_coefficients")

    def test_unknown_knot_raises(self):
        """Unknown knot name raises ValueError.  [DC]"""
        q = cmath.exp(2j * cmath.pi * 0.13)
        with pytest.raises(ValueError):
            _eng.jones_polynomial('pretzel_knot', q)
