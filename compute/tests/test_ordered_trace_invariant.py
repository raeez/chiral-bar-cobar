"""Tests for the ordered trace invariant engine.

Multi-path verification of the E_1 ordered trace construction
for sl_2 at various levels on elliptic curves.

VERIFIED values:
  [DC] direct computation from definitions
  [LT] Kac, Infinite-dim Lie algebras; Beauville 1996; Felder 1994
  [LC] limiting case (rational degeneration tau -> i*infty)
  [SY] symmetry (real values on imaginary axis)
  [CF] cross-family (Verlinde numbers across genera)
"""

import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from ordered_trace_invariant_engine import (
    verlinde_number_g, verlinde_number_g1,
    quantum_dimension_sl2, sl2_character,
    theta1, eta_dedekind,
    elliptic_R_eigenvalue_felder, elliptic_R_eigenvalue_diagonal,
    ordered_trace_g1_optionA, ordered_trace_g1_optionB, ordered_trace_g1_optionC,
    ordered_trace_g2,
    conformal_weight_sl2,
)

PI = math.pi


# =========================================================================
# 1. Verlinde numbers
# =========================================================================

def test_verlinde_sl2_k2():
    """Verlinde numbers for sl_2, k=2.

    Z_0 = 1, Z_1 = 3, Z_2 = 10, Z_3 = 36.
    # VERIFIED: [DC] S-matrix sum; [LT] Beauville 1996, Table 1
    """
    assert abs(verlinde_number_g(2, 0) - 1.0) < 1e-10
    assert abs(verlinde_number_g(2, 1) - 3.0) < 1e-10
    assert abs(verlinde_number_g(2, 2) - 10.0) < 0.5
    assert abs(verlinde_number_g(2, 3) - 36.0) < 0.5


def test_verlinde_sl2_k1():
    """Verlinde numbers for sl_2, k=1.

    Z_g = 2^g.
    # VERIFIED: [DC] S-matrix; [LT] Verlinde 1988
    """
    assert abs(verlinde_number_g(1, 0) - 1.0) < 1e-10
    assert abs(verlinde_number_g(1, 1) - 2.0) < 1e-10
    assert abs(verlinde_number_g(1, 2) - 4.0) < 0.5
    assert abs(verlinde_number_g(1, 3) - 8.0) < 0.5


def test_verlinde_sl2_k4():
    """Verlinde numbers for sl_2, k=4.

    Z_1 = 5, Z_2 = 35.
    # VERIFIED: [DC] S-matrix sum; [LT] Beauville normalization
    """
    assert abs(verlinde_number_g(4, 1) - 5.0) < 1e-10
    assert abs(verlinde_number_g(4, 2) - 35.0) < 0.5


# =========================================================================
# 2. Quantum dimensions
# =========================================================================

def test_quantum_dim_k2():
    """Quantum dimensions for sl_2, k=2: 1, sqrt(2), 1.

    # VERIFIED: [DC] sin((j+1)*pi/4)/sin(pi/4); [LT] Kac-Walton
    """
    assert abs(quantum_dimension_sl2(0, 2) - 1.0) < 1e-10
    assert abs(quantum_dimension_sl2(1, 2) - math.sqrt(2)) < 1e-10
    assert abs(quantum_dimension_sl2(2, 2) - 1.0) < 1e-10


def test_quantum_dim_k4():
    """Quantum dimensions for sl_2, k=4: 1, sqrt(3), 2, sqrt(3), 1.

    # VERIFIED: [DC] sin((j+1)*pi/6)/sin(pi/6)
    """
    expected = [1.0, math.sqrt(3), 2.0, math.sqrt(3), 1.0]
    for j in range(5):
        assert abs(quantum_dimension_sl2(j, 4) - expected[j]) < 1e-10, \
            f"j={j}: got {quantum_dimension_sl2(j, 4)}, expected {expected[j]}"


# =========================================================================
# 3. Theta function properties
# =========================================================================

def test_theta1_odd():
    """theta_1(-z|tau) = -theta_1(z|tau) (odd function).

    # VERIFIED: [DC] from series definition; [SY] parity
    """
    z = 0.3 + 0.1j
    tau = 1.0j
    assert abs(theta1(-z, tau) + theta1(z, tau)) < 1e-10


def test_theta1_quasi_period():
    """theta_1(z+1|tau) = -theta_1(z|tau).

    # VERIFIED: [DC] from series; [LT] Mumford, Tata Lectures
    """
    z = 0.3 + 0.1j
    tau = 1.0j
    ratio = theta1(z + 1.0, tau) / theta1(z, tau)
    assert abs(ratio + 1.0) < 1e-8


def test_eta_at_i():
    """eta(i) = Gamma(1/4) / (2*pi^{3/4}) approx 0.768225422326...

    # VERIFIED: [LT] Abramowitz-Stegun; [NE] Mathematica to 30 digits
    """
    eta_i = eta_dedekind(1.0j)
    assert abs(abs(eta_i) - 0.7682254223) < 1e-6


# =========================================================================
# 4. Character leading terms
# =========================================================================

def test_character_leading_term_k2():
    """chi_j(tau) ~ q^{h_j - c/24} * ((j+1) + O(q)).

    At tau = 2i (large Im), the ratio chi_j/q^{h_j-c/24} should be
    close to j+1.
    # VERIFIED: [DC] Weyl-Kac formula; [LC] q -> 0 limit
    """
    tau = 2.0j
    k = 2
    r = k + 2
    c_val = 3.0 * k / r
    for j in range(k + 1):
        chi = sl2_character(j, k, tau)
        h_j = conformal_weight_sl2(j, k)
        leading = cmath.exp(2j * PI * tau * (h_j - c_val / 24.0))
        ratio = chi / leading
        assert abs(ratio.real - (j + 1)) < 0.05, \
            f"j={j}: ratio = {ratio}, expected {j+1}"
        assert abs(ratio.imag) < 0.05, \
            f"j={j}: imaginary part {ratio.imag} too large"


# =========================================================================
# 5. Elliptic R-eigenvalue properties
# =========================================================================

def test_R_eigenvalue_j0_trivial():
    """R-eigenvalue at j=0 (trivial rep) is 1.

    # VERIFIED: [DC] product over empty weight set; [SY]
    """
    R = elliptic_R_eigenvalue_felder(0, 2, 0.3 + 0.1j, 1.0j)
    assert abs(R - 1.0) < 1e-10


def test_R_eigenvalue_doubly_periodic():
    """R-eigenvalue is doubly periodic in u: R(u+1) = R(u), R(u+tau) = R(u).

    This is because it is a ratio of theta functions with the same
    quasi-periodicity factors.
    # VERIFIED: [DC] theta_1 quasi-periodicity cancellation
    """
    k = 2
    tau = 1.0j
    u = 0.3 + 0.1j
    for j in range(k + 1):
        R0 = elliptic_R_eigenvalue_felder(j, k, u, tau)
        R1 = elliptic_R_eigenvalue_felder(j, k, u + 1.0, tau)
        Rtau = elliptic_R_eigenvalue_felder(j, k, u + tau, tau)
        if abs(R0) > 1e-10:
            assert abs(R1 / R0 - 1.0) < 1e-6, \
                f"j={j}: A-period ratio = {R1/R0}"
            assert abs(Rtau / R0 - 1.0) < 1e-6, \
                f"j={j}: B-period ratio = {Rtau/R0}"


def test_R_eigenvalue_rational_limit_k2():
    """In the rational limit (Im tau -> infty), R-eigenvalues approach
    trigonometric values.

    At u = 3/10, k=2:
      w_0^{rat} = 1
      w_2^{rat} = sqrt(5) - 2  [EXACT]

    # VERIFIED: [DC] product of sin ratios; [LC] tau -> i*infty
    """
    k = 2; r = 4
    u = 0.3
    tau_large = 20.0j  # large Im(tau) for rational limit

    # j=0: always 1
    R0 = elliptic_R_eigenvalue_felder(0, k, u, tau_large)
    assert abs(R0 - 1.0) < 1e-8

    # j=2: rational limit is sqrt(5) - 2
    R2 = elliptic_R_eigenvalue_felder(2, k, u, tau_large)
    w2 = R2 / quantum_dimension_sl2(2, k)
    expected = math.sqrt(5) - 2
    assert abs(w2.real - expected) < 1e-6, \
        f"w_2 = {w2}, expected sqrt(5)-2 = {expected}"


# =========================================================================
# 6. Ordered trace properties
# =========================================================================

def test_ordered_trace_real_on_imaginary_axis():
    """Z_1^{ord} is real when tau is purely imaginary and u is real.

    # VERIFIED: [SY] complex conjugation symmetry
    """
    k = 2
    res = ordered_trace_g1_optionB(k, 0.3, 1.0j, n_terms=150)
    assert abs(res["Z_ord"].imag) < 1e-8, \
        f"Imaginary part: {res['Z_ord'].imag}"


def test_ordered_trace_nonzero_delta():
    """Delta_1 = Z_ord - Z_char is nonzero for generic (u, tau).

    This is the core assertion: the ordered trace differs from the
    unweighted character sum.
    # VERIFIED: [DC] explicit numerical evaluation
    """
    k = 2
    res = ordered_trace_g1_optionB(k, 0.3, 1.0j, n_terms=150)
    assert abs(res["Delta"]) > 0.1, \
        f"|Delta| = {abs(res['Delta'])} too small"


def test_ordered_trace_u_dependence():
    """Z_ord(u1) != Z_ord(u2) at different spectral parameters.

    # VERIFIED: [DC] evaluated at u=0.2 and u=0.5
    """
    k = 2
    tau = 1.0j
    r1 = ordered_trace_g1_optionB(k, 0.2, tau, n_terms=150)
    r2 = ordered_trace_g1_optionB(k, 0.5, tau, n_terms=150)
    assert abs(r1["Z_ord"] - r2["Z_ord"]) > 0.01


def test_ordered_trace_not_product():
    """Z_ord / Z_char is NOT constant in u (not a product structure).

    If Z_ord = f(u) * Z_char, the ratio would be u-independent.
    # VERIFIED: [DC] ratio varies with u
    """
    k = 2
    tau = 1.0j
    r1 = ordered_trace_g1_optionB(k, 0.2, tau, n_terms=150)
    r2 = ordered_trace_g1_optionB(k, 0.5, tau, n_terms=150)
    ratio1 = r1["Z_ord"] / r1["Z_char_sum"]
    ratio2 = r2["Z_ord"] / r2["Z_char_sum"]
    assert abs(ratio1 - ratio2) > 0.01, \
        f"Ratio too close: {ratio1} vs {ratio2}"


def test_genus2_ordered_trace():
    """Genus-2 ordered trace differs from Verlinde number.

    Z_2(sl_2, k=2) = 10. The ordered trace at u=0.3 should differ.
    # VERIFIED: [DC]; [CF] Verlinde = 10 from independent S-matrix computation
    """
    k = 2
    res = ordered_trace_g2(k, 0.3, 1.0j, n_terms=150)
    assert abs(res["Z_sym"] - 10.0) < 0.5, \
        f"Verlinde Z_2 = {res['Z_sym']}, expected 10"
    assert abs(res["Delta"]) > 0.1, \
        f"|Delta_2| = {abs(res['Delta'])} too small"


# =========================================================================
# 7. Cross-checks between options
# =========================================================================

def test_all_options_nonzero_delta():
    """All three ordered trace options produce nonzero Delta.

    # VERIFIED: [DC] all three methods give |Delta| > 0
    """
    k = 2
    u = 0.3 + 0.1j
    tau = 0.2 + 1.0j
    for method, func in [
        ("A", ordered_trace_g1_optionA),
        ("B", ordered_trace_g1_optionB),
        ("C", ordered_trace_g1_optionC),
    ]:
        res = func(k, u, tau, n_terms=100)
        assert abs(res["Delta"]) > 0.01, \
            f"Option {method}: |Delta| = {abs(res['Delta'])} too small"


# =========================================================================
# 8. Conformal weight checks
# =========================================================================

def test_conformal_weights_k2():
    """Conformal weights h_j = j(j+2)/(4(k+2)) for k=2.

    h_0 = 0, h_1 = 3/16, h_2 = 1/2.
    # VERIFIED: [DC] direct formula; [LT] Kac table
    """
    assert abs(conformal_weight_sl2(0, 2) - 0.0) < 1e-15
    assert abs(conformal_weight_sl2(1, 2) - 3.0/16.0) < 1e-15
    assert abs(conformal_weight_sl2(2, 2) - 0.5) < 1e-15


# =========================================================================
# Run all tests
# =========================================================================

if __name__ == "__main__":
    test_functions = [v for k, v in sorted(globals().items())
                      if k.startswith("test_") and callable(v)]
    passed = 0
    failed = 0
    for test in test_functions:
        try:
            test()
            print(f"  PASS: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL: {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {test.__name__}: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total")
    if failed > 0:
        sys.exit(1)
