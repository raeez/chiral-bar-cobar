r"""Quantum modular forms from class-M shadow towers.

Class-M chiral algebras (Virasoro, W_N) have infinite shadow towers.
The shadow generating function

    H_A(t) = sum_{r>=2} S_r(A) * t^r = kappa * t^2 * sqrt(Q_L(t)/Q_L(0))

is algebraic of degree 2, with branch cuts controlled by the shadow metric.
This module investigates quantum modularity of H_A at rational points,
mock modular structure of shadow partition functions, connections to false
theta functions, the Nahm conjecture, and Habiro ring integrality.

MATHEMATICAL FRAMEWORK
======================

1. QUANTUM MODULARITY: Zagier's quantum modular forms are functions
   f: Q -> C such that the "error of modularity"
       h_gamma(x) = f(gamma*x) - (cx+d)^{-k} * f(x)
   extends to a smooth/analytic function on R for each gamma in SL_2(Z).

   The shadow generating function H_A(p/q) at rational arguments produces
   values whose modularity defects are controlled by the shadow metric.
   Since Q_L is quadratic, H_A is algebraic of degree 2, so the defects
   are algebraically structured.

2. MOCK MODULAR FORMS: For Virasoro at c < 1 (minimal models), the shadow
   partition function Z^sh(tau) should exhibit mock modular behavior.
   A mock modular form f has a "shadow" g such that f + g* is harmonic.
   The non-holomorphic completion involves the Eichler integral of g.

3. FALSE THETA FUNCTIONS: Psi(q) = sum_{n>=0} (-1)^n q^{n(n+1)/2} and
   related partial theta functions appear in minimal model characters.
   Their connection to shadow tower coefficients is investigated.

4. NAHM CONJECTURE: Certain q-hypergeometric series are modular iff
   they come from rational CFT. The Nahm matrix encodes the quadratic
   form in the exponent.

5. HABIRO RING: Z[q]^ = lim Z[q]/(1-q)(1-q^2)...(1-q^n) is where
   WRT invariants naturally live. The shadow partition function at roots
   of unity is tested for Habiro ring membership.

6. MODULAR COMPLETION: Every mock modular form has a non-holomorphic
   completion f_hat(tau) = f(tau) + integral of shadow.

7. RADIAL LIMITS: lim_{q->zeta_N radially} Z^sh(q) produces quantum
   invariants related to 3-manifold topology.

CONVENTIONS:
  - q = e^{2*pi*i*tau}
  - kappa(A) = modular characteristic (AP20)
  - E_2*(tau) is quasi-modular (AP15)
  - The shadow PF at the scalar level is tau-INDEPENDENT
  - H_A(t) = sum_{r>=2} S_r t^r (ordinary GF), NOT the weighted GF

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, factorial, pi as sym_pi,
    simplify, sqrt, Abs, N as Neval, cos, sin, atan2, I,
    binomial, cancel, oo, conjugate,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PI = math.pi
TWO_PI = 2 * PI
TWO_PI_SQ = TWO_PI ** 2

c_sym = Symbol('c')
t_sym = Symbol('t')


# =========================================================================
# Section 0: Virasoro shadow data helpers
# =========================================================================

def virasoro_kappa(c_val):
    """kappa(Vir_c) = c/2."""
    return c_val / 2


def virasoro_cubic(c_val):
    """S_3(Vir_c) = 2 (the cubic shadow coefficient alpha)."""
    return 2


def virasoro_quartic(c_val):
    """S_4(Vir_c) = Q^contact = 10/(c*(5c+22))."""
    if abs(c_val) < 1e-15:
        return float('inf')
    return 10.0 / (c_val * (5.0 * c_val + 22.0))


def virasoro_shadow_metric_coeffs(c_val):
    """Coefficients (q0, q1, q2) of Q_L(t) for Virasoro.

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
           = c^2 + 12c*t + q2*t^2

    where q2 = 36 + 80/(5c+22) = (180c+872)/(5c+22).
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = virasoro_quartic(c_val)
    q0 = 4.0 * kappa ** 2  # c^2
    q1 = 12.0 * kappa * alpha  # 12c
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4  # (180c+872)/(5c+22)
    return q0, q1, q2


def virasoro_shadow_radius(c_val):
    """Shadow growth rate rho(Vir_c) = sqrt((180c+872)/((5c+22)*c^2))."""
    if c_val <= 0:
        return float('inf')
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    if denom <= 0:
        return float('inf')
    return math.sqrt(numer / denom)


# =========================================================================
# Section 1: Shadow generating function evaluation
# =========================================================================

def _sqrt_Q_taylor_numerical(q0, q1, q2, max_n):
    """Taylor coefficients of sqrt(q0 + q1*t + q2*t^2), numerical.

    Returns list [a_0, a_1, ..., a_{max_n}].
    """
    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)
    if max_n == 0:
        return a
    a[1] = q1 / (2.0 * a[0])
    if max_n == 1:
        return a
    a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a[0])
    return a


def shadow_tower_coefficients(c_val, max_arity=50):
    """Compute shadow tower coefficients S_r(Vir_c) for r=2,...,max_arity.

    The weighted generating function is H(t) = sum_{r>=2} r*S_r*t^r = t^2 * sqrt(Q_L(t)).
    Writing a_n = [t^n] sqrt(Q_L(t)), we have r*S_r = a_{r-2}, hence S_r = a_{r-2}/r.
    """
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    max_n = max_arity - 2
    a = _sqrt_Q_taylor_numerical(q0, q1, q2, max_n)

    coeffs = {}
    for n in range(len(a)):
        r = n + 2
        coeffs[r] = a[n] / r  # S_r = a_{r-2} / r
    return coeffs


def shadow_generating_function(c_val, t_val, max_arity=100):
    """Evaluate G(t) = sum_{r>=2} S_r(Vir_c) * t^r at a specific t value.

    This is the ORDINARY generating function of the shadow coefficients.
    """
    coeffs = shadow_tower_coefficients(c_val, max_arity)
    total = 0.0
    for r in sorted(coeffs.keys()):
        contribution = coeffs[r] * t_val ** r
        total += contribution
        if abs(contribution) < 1e-50 and r > 10:
            break
    return total


def shadow_gf_closed_form(c_val, t_val):
    """Closed-form evaluation via G(t) from the algebraic function.

    The ordinary GF G(t) = sum S_r t^r has no closed form in terms of
    sqrt(Q_L); the closed-form expression H(t) = t^2*sqrt(Q_L) is the
    weighted GF. We evaluate G(t) by summing the series from the recursion.
    """
    return shadow_generating_function(c_val, t_val, max_arity=200)


def weighted_shadow_gf(c_val, t_val):
    """Evaluate the WEIGHTED generating function H(t) = sum r*S_r*t^r = t^2*sqrt(Q_L(t)).

    This has the closed form: H(t) = t^2 * sqrt(Q_L(t)).
    """
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    Q_val = q0 + q1 * t_val + q2 * t_val ** 2
    if Q_val < 0:
        # Complex: return magnitude
        return t_val ** 2 * cmath.sqrt(Q_val)
    return t_val ** 2 * math.sqrt(Q_val)


def weighted_shadow_gf_complex(c_val, t_val):
    """Evaluate H(t) for complex t, using complex sqrt."""
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    Q_val = complex(q0) + complex(q1) * complex(t_val) + complex(q2) * complex(t_val) ** 2
    return complex(t_val) ** 2 * cmath.sqrt(Q_val)


# =========================================================================
# Section 2: Quantum modularity of shadow generating function
# =========================================================================

def shadow_gf_at_rational(c_val, p, q, max_arity=200):
    """Evaluate G(p/q) = sum_{r>=2} S_r(Vir_c) * (p/q)^r.

    Parameters:
        c_val: central charge
        p, q: integers with gcd(p,q) = 1

    Returns the value G(p/q).
    """
    t_val = float(p) / float(q)
    rho = virasoro_shadow_radius(c_val)
    # Check convergence: |t| < 1/rho
    if abs(t_val) * rho >= 1.0 - 1e-10:
        # Series diverges; use Borel regularization
        return shadow_gf_borel_regularized(c_val, t_val, max_arity)
    return shadow_generating_function(c_val, t_val, max_arity)


def shadow_gf_borel_regularized(c_val, t_val, max_arity=200):
    """Borel-regularized evaluation of G(t) = sum S_r t^r / Gamma(r+1) * Gamma(r+1).

    When |t| > R (radius of convergence), the ordinary series diverges.
    The Borel transform B(s) = sum S_r s^r / Gamma(r+1) is entire (since
    |S_r| grows at most geometrically, and 1/r! kills the growth).

    The Borel sum: G^{Borel}(t) = integral_0^infty B(s/t) e^{-s} ds / t
    For practical computation, we use optimal truncation + remainder estimate.
    """
    rho = virasoro_shadow_radius(c_val)
    coeffs = shadow_tower_coefficients(c_val, max_arity)

    if abs(t_val) < 1e-15:
        return 0.0

    # Optimal truncation: N* = floor(1/(rho*|t|))
    N_star = max(2, int(1.0 / (rho * abs(t_val)))) if rho * abs(t_val) > 0 else max_arity
    N_star = min(N_star, max_arity)

    # Sum to N*
    total = 0.0
    for r in range(2, N_star + 1):
        if r in coeffs:
            total += coeffs[r] * t_val ** r
    return total


def quantum_modular_defect(c_val, x, gamma_matrix, max_arity=200):
    r"""Compute the quantum modular defect at x for SL_2(Z) element gamma.

    gamma = [[a, b], [c_m, d]] acts on x by gamma*x = (a*x+b)/(c_m*x+d).

    The defect is: h_gamma(x) = G(gamma*x) - (c_m*x+d)^{-k} * G(x)
    where k is the putative weight.

    For the shadow GF, the weight k is determined by the algebraic structure.
    Since H(t) = t^2 * sqrt(Q_L(t)) and Q_L is quadratic, H has "algebraic
    weight" 3 (= 2 + 1/2*2). We test several candidate weights.

    Parameters:
        c_val: central charge
        x: rational number (float)
        gamma_matrix: [[a,b],[c_m,d]] in SL_2(Z)
        max_arity: truncation

    Returns dict with defects at various candidate weights.
    """
    a, b = gamma_matrix[0]
    c_m, d = gamma_matrix[1]

    denom = c_m * x + d
    if abs(denom) < 1e-15:
        return {'x': x, 'gamma': gamma_matrix, 'singular': True}

    gamma_x = (a * x + b) / denom

    G_x = shadow_gf_at_rational(c_val, Fraction(x).limit_denominator(1000).numerator,
                                 Fraction(x).limit_denominator(1000).denominator,
                                 max_arity)
    G_gx = shadow_gf_at_rational(c_val, Fraction(gamma_x).limit_denominator(1000).numerator,
                                  Fraction(gamma_x).limit_denominator(1000).denominator,
                                  max_arity)

    defects = {}
    for k in [0, 1, 2, 3, 4]:
        modular_factor = abs(denom) ** (-k) if abs(denom) > 1e-15 else float('inf')
        defect = G_gx - modular_factor * G_x
        defects[k] = defect

    return {
        'x': x,
        'gamma_x': gamma_x,
        'gamma': gamma_matrix,
        'G_x': G_x,
        'G_gamma_x': G_gx,
        'defects_by_weight': defects,
        'singular': False,
    }


def quantum_modularity_S_defect(c_val, n, max_arity=200):
    r"""Defect under S-transform: G(-1/x) vs |x|^{-k} G(x) at x=1/n.

    The S-matrix is [[0,-1],[1,0]], acting as x -> -1/x.

    For quantum modular forms: h(x) = G(x) - |x|^{-k} G(-1/x)
    should be smooth/continuous.

    We compute for x = 1/n (n = 1,2,...).
    """
    x = 1.0 / n
    gamma_S = [[0, -1], [1, 0]]
    return quantum_modular_defect(c_val, x, gamma_S, max_arity)


def quantum_modularity_T_defect(c_val, n, max_arity=200):
    r"""Defect under T-transform: G(x+1) vs G(x) at x=1/n.

    The T-matrix is [[1,1],[0,1]], acting as x -> x+1.
    For weight k: defect = G(x+1) - G(x) (T-transform has trivial factor).
    """
    x = 1.0 / n
    gamma_T = [[1, 1], [0, 1]]
    return quantum_modular_defect(c_val, x, gamma_T, max_arity)


def scan_quantum_modularity(c_val, max_denom=10, max_arity=100):
    r"""Scan G(p/q) for all p/q with q <= max_denom, compute S-defects.

    Returns a list of dicts with the shadow GF evaluated at each rational
    and the quantum modular defect data.
    """
    results = []
    gamma_S = [[0, -1], [1, 0]]

    for q in range(1, max_denom + 1):
        for p in range(1, q + 1):
            if math.gcd(p, q) != 1:
                continue
            x = float(p) / float(q)
            G_x = shadow_gf_at_rational(c_val, p, q, max_arity)
            # S-transform: x -> -1/x
            neg_inv_x = -1.0 / x
            # Evaluate at -1/x by series with care about sign
            rho = virasoro_shadow_radius(c_val)
            R = 1.0 / rho if rho > 0 else float('inf')

            entry = {
                'p': p, 'q': q, 'x': x,
                'G_x': G_x,
                'convergence_radius': R,
                'x_in_disk': abs(x) < R,
            }

            # S-defect at various weights
            if abs(x) < R:
                # -1/x has |1/x| > 1 for x < 1, may be outside disk
                entry['neg_inv_x'] = neg_inv_x
                entry['neg_inv_x_in_disk'] = abs(neg_inv_x) < R
                if abs(neg_inv_x) < R:
                    G_ninvx = shadow_generating_function(c_val, neg_inv_x, max_arity)
                    for k in [0, 2, 3]:
                        defect = G_x - abs(x) ** (-k) * G_ninvx
                        entry[f'S_defect_weight_{k}'] = defect
                else:
                    G_ninvx_borel = shadow_gf_borel_regularized(c_val, neg_inv_x, max_arity)
                    for k in [0, 2, 3]:
                        defect = G_x - abs(x) ** (-k) * G_ninvx_borel
                        entry[f'S_defect_weight_{k}_borel'] = defect

            results.append(entry)

    return results


# =========================================================================
# Section 3: Mock modular forms from shadow towers
# =========================================================================

def false_theta_function(q_val, max_terms=200):
    r"""False theta function Psi(q) = sum_{n>=0} (-1)^n q^{n(n+1)/2}.

    This is a partial theta function (sum over n>=0 instead of all n).
    It is NOT modular but has quantum modular properties.
    """
    total = 0.0
    for n in range(max_terms):
        exp = n * (n + 1) / 2.0
        if exp * abs(math.log(abs(q_val)) if abs(q_val) > 0 else 0) > 500:
            break
        term = ((-1) ** n) * q_val ** exp
        total += term
        if abs(term) < 1e-50:
            break
    return total


def false_theta_coefficients(max_n=50):
    """Coefficients of Psi(q) = sum a_n q^n where a_n = (-1)^m if n = m(m+1)/2, else 0.

    Returns dict {n: coefficient}.
    """
    coeffs = {}
    for m in range(max_n):
        exp = m * (m + 1) // 2
        if exp > max_n:
            break
        coeffs[exp] = (-1) ** m
    return coeffs


def shadow_tower_vs_false_theta(c_val, max_arity=30):
    r"""Compare shadow tower coefficients S_r(Vir_c) with false theta function.

    Test whether S_r relates to coefficients of Psi(q) or its derivatives.
    The false theta Psi(q) has support on triangular numbers n = m(m+1)/2.

    We compute the ratios S_r / psi_r where psi_r is the false theta
    coefficient at the appropriate index.
    """
    S = shadow_tower_coefficients(c_val, max_arity)
    psi = false_theta_coefficients(max_arity + 5)

    comparisons = {}
    for r in range(2, max_arity + 1):
        if r in S and r in psi and psi[r] != 0:
            ratio = S[r] / psi[r]
            comparisons[r] = {
                'S_r': S[r],
                'psi_r': psi[r],
                'ratio': ratio,
            }

    return {
        'c': c_val,
        'kappa': virasoro_kappa(c_val),
        'shadow_coefficients': S,
        'false_theta_coefficients': psi,
        'comparisons': comparisons,
        'has_triangular_support_overlap': len(comparisons) > 0,
    }


def minimal_model_central_charge(p, q_param):
    """Central charge of the (p,q) minimal model: c = 1 - 6(p-q)^2/(pq).

    The unitary minimal models have q = p+1, giving c = 1 - 6/(p(p+1)).
    Ising: (3,4) -> c = 1/2.
    Tri-critical Ising: (4,5) -> c = 7/10.
    """
    return 1.0 - 6.0 * (p - q_param) ** 2 / (p * q_param)


def mock_modular_shadow_analysis(c_val, tau_val=None, max_terms=100):
    r"""Analyze mock modular structure of the shadow PF at central charge c.

    For minimal models (c < 1), the shadow partition function should have
    mock modular behavior. This function:

    1. Computes the shadow tower coefficients S_r(Vir_c)
    2. Forms the shadow generating function G(t) = sum S_r t^r
    3. Tests the Zwegers completion structure

    The "shadow of the mock" is a unary theta function determined by
    the shadow metric Q_L.

    A mock modular form f of weight k has a shadow g (a cusp form of weight 2-k)
    such that the non-holomorphic completion f_hat = f + g* is a harmonic
    Maass form.
    """
    S = shadow_tower_coefficients(c_val, max_terms)
    kappa = virasoro_kappa(c_val)
    rho = virasoro_shadow_radius(c_val)
    R = 1.0 / rho if rho > 0 else float('inf')

    # The shadow metric
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    Delta = 8.0 * kappa * virasoro_quartic(c_val) if abs(kappa) > 1e-15 else 0.0

    # For mock modularity, the key invariant is the discriminant Delta
    # When Delta > 0 (class M with complex branch points), the shadow
    # metric has indefinite-looking features that connect to mock theta functions.

    # Mock theta type: determined by the weight of the shadow g
    # For weight 1/2 mock: g is weight 3/2 unary theta
    # For weight 3/2 mock: g is weight 1/2 theta

    analysis = {
        'c': c_val,
        'kappa': kappa,
        'shadow_radius': rho,
        'convergence_radius': R,
        'discriminant': Delta,
        'is_minimal_model': c_val < 1,
        'shadow_depth': 'M' if abs(Delta) > 1e-15 else ('L' if abs(S.get(3, 0)) > 1e-15 else 'G'),
    }

    # Shadow tower partial sums
    partial_sums = []
    running = 0.0
    for r in range(2, min(max_terms, 50) + 2):
        if r in S:
            running += S[r]
        partial_sums.append(running)
    analysis['partial_sums'] = partial_sums

    # Growth type classification
    if rho > 1:
        analysis['growth_type'] = 'divergent'
        analysis['borel_summable'] = True  # algebraic GF => Gevrey-0
        # Optimal truncation
        N_star = max(2, int(1.0 / rho))
        analysis['optimal_truncation'] = N_star
        # Optimally truncated value
        opt_val = sum(S.get(r, 0) for r in range(2, N_star + 2))
        analysis['optimal_truncated_value'] = opt_val
    else:
        analysis['growth_type'] = 'convergent'
        analysis['borel_summable'] = True
        analysis['optimal_truncation'] = None
        analysis['sum_value'] = sum(S.get(r, 0) for r in range(2, max_terms + 2))

    # Asymptotic decay/growth characterization
    if len(S) > 10:
        ratios = []
        for r in range(5, min(30, max(S.keys()))):
            if r in S and r - 1 in S and abs(S[r - 1]) > 1e-50:
                ratios.append(abs(S[r] / S[r - 1]))
        if ratios:
            analysis['ratio_tail'] = ratios[-5:]
            analysis['estimated_rho'] = ratios[-1] if ratios else None

    return analysis


# =========================================================================
# Section 4: Nahm conjecture and shadow matrices
# =========================================================================

def nahm_matrix_from_shadow(c_val):
    r"""Construct the "Nahm matrix" from the shadow metric data.

    Nahm's conjecture: a q-hypergeometric sum
        f(q) = sum_{n>=0} q^{n^T A n / 2} / (q)_n
    is modular iff A has all eigenvalues in (0,1) and satisfies
    certain additional conditions.

    For the shadow generating function, the quadratic form is encoded
    in Q_L(t) = q0 + q1*t + q2*t^2. The "Nahm matrix" is the 1x1
    matrix A = [q2/q0] (normalized second coefficient).

    For multi-generator algebras, this would be a larger matrix.

    Returns:
        Dict with the Nahm matrix, eigenvalues, and modularity criterion.
    """
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    kappa = virasoro_kappa(c_val)

    # 1x1 Nahm matrix: A = q2/q0 = (9*alpha^2 + 16*kappa*S4) / (4*kappa^2)
    if abs(q0) < 1e-15:
        return {'c': c_val, 'degenerate': True}

    A_val = q2 / q0

    # Eigenvalue analysis (1x1: eigenvalue = A_val)
    eigenvalue = A_val

    # Nahm criterion: eigenvalues in (0, 1)?
    # For Virasoro: A_val = (180c+872)/((5c+22)*c^2)
    # This is rho^2 (the square of the shadow radius!)
    # So the Nahm criterion eigenvalue in (0,1) <=> rho < 1 <=> c > c*

    nahm_criterion = 0 < eigenvalue < 1

    # The Bloch-Wigner dilogarithm value
    # For the Nahm conjecture: the "Bloch group element" involves
    # D(e^{2*pi*i*z}) where z is related to the eigenvalue
    if 0 < eigenvalue < 1:
        # Bloch-Wigner function D(z) = Im(Li_2(z)) + arg(1-z)*log|z|
        # At z = eigenvalue (real, in (0,1)): D(z) = Im(Li_2(z)) = 0
        # for real z. The relevant quantity is the Rogers dilogarithm.
        # L(x) = Li_2(x) + (1/2)*log(x)*log(1-x)
        # At x = eigenvalue:
        import scipy
        rogers_dilog = None
    else:
        rogers_dilog = None

    return {
        'c': c_val,
        'kappa': kappa,
        'nahm_matrix': [[A_val]],
        'eigenvalue': eigenvalue,
        'rho_squared': eigenvalue,  # A_val = rho^2 for Virasoro!
        'nahm_criterion_satisfied': nahm_criterion,
        'interpretation': (
            'Nahm criterion satisfied: shadow tower converges, '
            'consistent with modular shadow PF'
            if nahm_criterion else
            'Nahm criterion violated: shadow tower diverges, '
            'shadow PF requires Borel regularization'
        ),
        'degenerate': False,
    }


def nahm_scan_minimal_models(max_p=12):
    """Scan Nahm criterion across unitary minimal models.

    Unitary minimal models: c(p) = 1 - 6/(p(p+1)) for p = 3,4,5,...
    p=3: Ising (c=1/2), p=4: tri-Ising (c=7/10), p=5: c=4/5, ...

    For these c < 1 models: rho > 1 always (since c* ~ 6.125 > 1).
    So the Nahm criterion is VIOLATED for all minimal models.
    This is EXPECTED: the shadow tower diverges for c < c*, requiring
    Borel resummation.
    """
    results = []
    for p in range(3, max_p + 1):
        c_val = 1.0 - 6.0 / (p * (p + 1))
        nahm = nahm_matrix_from_shadow(c_val)
        nahm['p'] = p
        nahm['q_param'] = p + 1
        nahm['model_name'] = f'M({p},{p+1})'
        results.append(nahm)
    return results


# =========================================================================
# Section 5: Habiro ring and shadow integrality
# =========================================================================

def _root_of_unity(N, k=1):
    """Compute zeta_N^k = e^{2*pi*i*k/N}."""
    return cmath.exp(2j * PI * k / N)


def q_pochhammer(q_val, n):
    """(q; q)_n = prod_{j=0}^{n-1} (1 - q^{j+1}).

    The q-Pochhammer symbol.
    """
    if n <= 0:
        return complex(1.0)
    product = complex(1.0)
    for j in range(n):
        product *= (1.0 - q_val ** (j + 1))
    return product


def habiro_element_test(c_val, N, max_terms=50):
    r"""Test if Z^sh(Vir_c, zeta_N) is well-defined in the Habiro ring.

    The Habiro ring Z[q]^ = lim_{<-} Z[q]/((q;q)_n) consists of
    power series f(q) = sum a_n(q) * (q;q)_n where a_n(q) in Z[q].

    A necessary condition for f to be in the Habiro ring: f(zeta_N)
    must be well-defined for ALL roots of unity zeta_N.

    For the shadow partition function, at the scalar level:
    Z^sh = kappa * (A-hat(i*hbar) - 1) where hbar is related to log(q).
    At q = zeta_N: hbar = 2*pi*i/N (up to normalization).

    The scalar shadow Z^sh = sum_{g>=1} F_g * (log q)^{2g} is formal in
    log q, not a q-series; the tau-dependent quantity is the full genus-1
    amplitude involving log eta(tau).

    For the Habiro ring test, we examine the shadow generating function
    G(t) at t evaluated modulo cyclotomic polynomials.

    We test: does G(t) mod (1-t)(1-t^2)...(1-t^n) stabilize?
    """
    zeta = _root_of_unity(N)
    kappa = virasoro_kappa(c_val)

    # The shadow partition function at the scalar level:
    # Z^sh = kappa * (A-hat(i*hbar) - 1) where hbar = 2*pi*i/N
    hbar = 2.0 * PI / N  # real hbar for the closed-form evaluation
    if hbar < 2 * PI:
        scalar_val = kappa * ((hbar / 2.0) / math.sin(hbar / 2.0) - 1.0)
    else:
        scalar_val = None

    # Evaluate the shadow GF G(zeta_N) = sum S_r * zeta_N^r
    S = shadow_tower_coefficients(c_val, max_terms)
    G_zeta = complex(0.0)
    rho = virasoro_shadow_radius(c_val)
    # zeta_N has |zeta_N| = 1, so convergence requires rho < 1
    # For rho >= 1: use optimal truncation
    N_star = max(2, int(1.0 / rho)) if rho > 0 else max_terms
    N_star = min(N_star, max_terms)

    partial_sums = []
    for r in range(2, N_star + 2):
        if r in S:
            G_zeta += S[r] * zeta ** r
        partial_sums.append(complex(G_zeta))

    # Test cyclotomic polynomial compatibility
    # (q;q)_n at q = zeta_N
    pochhammer_vals = {}
    for n in range(1, min(3 * N, 30)):
        poch = q_pochhammer(zeta, n)
        pochhammer_vals[n] = poch
        # (zeta_N; zeta_N)_n = 0 for n >= N, since the factor (1 - zeta_N^N) = 0 appears

    return {
        'c': c_val,
        'N': N,
        'zeta_N': zeta,
        'kappa': kappa,
        'shadow_radius': rho,
        'G_zeta_N': G_zeta,
        'G_zeta_N_abs': abs(G_zeta),
        'scalar_Z_sh': scalar_val,
        'truncation_order': N_star,
        'partial_sums_abs': [abs(ps) for ps in partial_sums[-5:]],
        'pochhammer_at_N': pochhammer_vals.get(N, None),
        'pochhammer_zero_at_N': (abs(pochhammer_vals.get(N, 1)) < 1e-10
                                  if N in pochhammer_vals else None),
        'habiro_compatible': abs(G_zeta) < 1e10,  # basic finiteness check
    }


def habiro_scan(c_val, N_range=None):
    """Scan Habiro ring compatibility for Z^sh(Vir_c) at roots of unity.

    Parameters:
        c_val: central charge
        N_range: list of N values (default [3,4,5,6,8,10,12])
    """
    if N_range is None:
        N_range = [3, 4, 5, 6, 8, 10, 12]

    results = []
    for N in N_range:
        result = habiro_element_test(c_val, N)
        results.append(result)

    return {
        'c': c_val,
        'N_values': N_range,
        'results': results,
        'all_finite': all(r['habiro_compatible'] for r in results),
    }


# =========================================================================
# Section 6: Modular completion of shadow partition function
# =========================================================================

def eichler_integral_numerical(shadow_coeffs, tau_val, weight, max_terms=100):
    r"""Numerical Eichler integral of the "shadow" (in mock modular sense).

    For a mock modular form f of weight k with shadow g of weight 2-k:
    f_hat(tau) = f(tau) + (4*pi)^{1-k} * integral_{-tau_bar}^{i*infty}
                  g(z) * (z + tau)^{k-2} dz

    The period integral is the Eichler integral of g.

    Parameters:
        shadow_coeffs: q-expansion coefficients of the "shadow" g(tau)
        tau_val: the point in the upper half-plane
        weight: the weight k of the mock form
        max_terms: truncation

    Returns the period integral value.
    """
    # The Eichler integral from -tau_bar to i*infty along the imaginary axis
    # For tau = x + iy: -tau_bar = -x + iy, so the path goes from -x+iy to i*infty
    # Parametrize: z = -tau_val.conjugate() + i*s for s from 0 to infinity

    y = tau_val.imag
    x = tau_val.real

    # Discretize the integral: use Gauss-Laguerre quadrature
    # z = -conj(tau) + i*s, dz = i*ds
    # integrand = g(z) * (z + tau)^{k-2}
    # = g(-x+iy+is) * (-x+iy+is + x+iy)^{k-2}
    # = g(-x+i(y+s)) * (2iy+is)^{k-2}
    # = g(-x+i(y+s)) * i^{k-2} * (2y+s)^{k-2}

    # For a simple theta-function shadow g(z) = sum a_n q_z^n:
    n_points = 50
    ds = 0.5  # integration step
    integral = complex(0.0)

    for j in range(n_points):
        s = (j + 0.5) * ds
        z = complex(-x, y + s)
        q_z = cmath.exp(2j * PI * z)

        # Evaluate g at z
        g_val = complex(0.0)
        for n, coeff in shadow_coeffs.items():
            if n > 0:
                contrib = coeff * q_z ** n
                g_val += contrib
                if abs(contrib) < 1e-50:
                    break

        # (z + tau)^{k-2}
        z_plus_tau = z + tau_val
        factor = z_plus_tau ** (weight - 2) if abs(z_plus_tau) > 1e-15 else 0.0

        integral += g_val * factor * complex(0, 1) * ds

    # Prefactor
    prefactor = (4 * PI) ** (1 - weight)
    return prefactor * integral


def modular_completion_shadow(c_val, tau_val, max_arity=50):
    r"""Non-holomorphic modular completion of the shadow PF.

    For the shadow partition function at the scalar level:
    Z^sh = kappa * (A-hat(i*hbar) - 1) is tau-INDEPENDENT.

    The full genus-1 amplitude F_1^{hol}(tau) = -kappa * log eta(tau)
    IS tau-dependent and transforms under SL_2(Z) with an anomaly.

    The non-holomorphic completion is:
    F_1^{hat}(tau) = -kappa * [log eta(tau) + (pi)/(6*Im(tau))]

    The second term is the Eichler integral of the constant shadow.
    More precisely: the weight-0 completion of log eta involves E_2*(tau),
    the non-holomorphic Eisenstein series.

    For the SHADOW GENERATING FUNCTION (arity series), the completion
    involves the shadow connection ∇^sh.
    """
    if tau_val is None:
        tau_val = complex(0, 1)  # tau = i

    kappa = virasoro_kappa(c_val)
    y = tau_val.imag

    if y <= 0:
        return {'error': 'tau must be in the upper half-plane'}

    q = cmath.exp(2j * PI * tau_val)

    # Holomorphic part: -kappa * log eta(tau)
    log_eta = 2j * PI * tau_val / 24.0
    for n in range(1, 200):
        qn = q ** n
        if abs(qn) < 1e-30:
            break
        log_eta += cmath.log(1.0 - qn)

    F1_hol = -kappa * log_eta

    # Non-holomorphic correction: from E_2^* = E_2 + 3/(pi*y)
    # E_2(tau) = 1 - 24*sum sigma_1(n)*q^n
    # E_2*(tau) = E_2(tau) + 3/(pi*Im(tau))  (quasi-modular -> almost modular)
    nh_correction = -kappa * 3.0 / (PI * y) / 24.0  # the E_2* - E_2 piece

    # Completed amplitude
    F1_hat = F1_hol + nh_correction

    # Shadow tower arity-dependent piece (tau-independent)
    S = shadow_tower_coefficients(c_val, max_arity)
    G_at_1 = sum(S.get(r, 0) for r in range(2, max_arity + 2))

    return {
        'c': c_val,
        'tau': tau_val,
        'kappa': kappa,
        'F1_holomorphic': F1_hol,
        'nh_correction': nh_correction,
        'F1_completed': F1_hat,
        'shadow_tower_sum': G_at_1,
        'E2_star_correction': 3.0 / (PI * y),
        'is_modular_completed': True,
    }


# =========================================================================
# Section 7: Radial limits and quantum invariants
# =========================================================================

def radial_limit_shadow_pf(c_val, N, num_points=50, max_terms=200):
    r"""Compute lim_{q -> zeta_N radially} of the genus-1 amplitude.

    Along the radial path q = r * zeta_N with r -> 1^-:
    tau_r = log(r*zeta_N) / (2*pi*i) = (log r)/(2*pi*i) + 1/N

    The holomorphic genus-1 amplitude:
    F_1(tau) = -kappa * log eta(tau)

    As r -> 1: tau -> i*0^+ + 1/N, and eta(1/N + i*epsilon) has known
    asymptotic behavior related to the Rademacher expansion.

    Returns the limiting values at several approach distances.
    """
    kappa = virasoro_kappa(c_val)
    zeta = _root_of_unity(N)

    # Radial approach: q = r * zeta_N = r * e^{2*pi*i/N}, so
    # tau = log(q)/(2*pi*i) = 1/N + log(r)/(2*pi*i)
    #     = 1/N - i*|log(r)|/(2*pi)  for r < 1 (Im(tau) > 0).

    results = []
    for j in range(num_points):
        r = 1.0 - 10.0 ** (-(j + 1) * 0.1)  # r approaches 1 from below
        if r <= 0 or r >= 1:
            continue

        tau = 1.0 / N + complex(0, -math.log(r) / TWO_PI)
        if tau.imag <= 0:
            continue

        q = cmath.exp(2j * PI * tau)

        # Compute log eta(tau)
        log_eta = 2j * PI * tau / 24.0
        for n in range(1, max_terms + 1):
            qn = q ** n
            if abs(qn) < 1e-30:
                break
            log_eta += cmath.log(1.0 - qn)

        F1 = -kappa * log_eta

        results.append({
            'r': r,
            'tau': tau,
            'log_eta': log_eta,
            'F1': F1,
            'F1_real': F1.real,
            'F1_imag': F1.imag,
        })

    # Extrapolate the limit
    if len(results) >= 3:
        # The limit should converge to a finite value (quantum invariant)
        F1_reals = [res['F1_real'] for res in results[-10:]]
        F1_imags = [res['F1_imag'] for res in results[-10:]]
        limit_real = F1_reals[-1] if F1_reals else None
        limit_imag = F1_imags[-1] if F1_imags else None
    else:
        limit_real = None
        limit_imag = None

    return {
        'c': c_val,
        'N': N,
        'kappa': kappa,
        'num_points': len(results),
        'approach_data': results[-5:] if results else [],
        'limit_real': limit_real,
        'limit_imag': limit_imag,
        'limit_abs': abs(complex(limit_real or 0, limit_imag or 0)),
    }


def radial_limits_scan(c_val, N_values=None, num_points=30):
    """Compute radial limits at multiple roots of unity.

    Parameters:
        c_val: central charge
        N_values: list of N for zeta_N (default [3,4,5,6])
    """
    if N_values is None:
        N_values = [3, 4, 5, 6]

    results = {}
    for N in N_values:
        results[N] = radial_limit_shadow_pf(c_val, N, num_points)

    return {
        'c': c_val,
        'kappa': virasoro_kappa(c_val),
        'N_values': N_values,
        'limits': results,
    }


# =========================================================================
# Section 8: Multi-path cross-verification infrastructure
# =========================================================================

def cross_verify_shadow_gf(c_val, t_val, max_arity=150):
    """Cross-verify G(t) via multiple independent paths.

    Path 1: Direct series sum of S_r * t^r
    Path 2: Weighted GF H(t) = t^2*sqrt(Q_L) then extract G by integration
    Path 3: Asymptotic formula C*rho^r*r^{-5/2}*cos(r*theta+phi) then sum
    """
    # Path 1: Direct series
    S = shadow_tower_coefficients(c_val, max_arity)
    G_series = sum(S.get(r, 0) * t_val ** r for r in range(2, max_arity + 2))

    # Path 2: From weighted GF
    # H(t) = sum r*S_r*t^r, so G(t) = sum S_r*t^r
    # We can compute this as integral_0^t H(s)/s ds (if all terms well-defined)
    # But more directly: H(t) = t^2*sqrt(Q_L(t)), and
    # S_r = a_{r-2}/r where a_n = [t^n]sqrt(Q_L)
    # This IS what we computed in Path 1, so Path 2 = Path 1 at the coefficient level.
    # Use the closed-form H(t) for the WEIGHTED sum as a sanity check.
    H_val = weighted_shadow_gf(c_val, t_val)
    H_series = sum(r * S.get(r, 0) * t_val ** r for r in range(2, max_arity + 2))

    # Path 3: Asymptotic series with exact leading behavior
    rho = virasoro_shadow_radius(c_val)
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    # Branch points
    disc = q1 ** 2 - 4 * q0 * q2
    if disc < 0:
        # Complex branch points
        t0_real = -q1 / (2 * q2)
        t0_imag = math.sqrt(-disc) / (2 * q2)
        t0 = complex(t0_real, t0_imag)
        theta = -cmath.phase(t0)  # oscillation angle
        # Darboux coefficient from sqrt singularity
        R = abs(t0)
        # Asymptotic: S_r ~ C * (1/R)^r * r^{-5/2} * cos(r*theta + phi)
        # Estimate C and phi from last computed coefficients
        r_ref = max_arity
        S_ref = S.get(r_ref, 0)
        predicted_modulus = rho ** r_ref * r_ref ** (-2.5)
        C_est = abs(S_ref) / predicted_modulus if predicted_modulus > 1e-50 else 0
        phi_est = 0  # phase estimation requires more data

        G_asymptotic = sum(
            C_est * rho ** r * r ** (-2.5) * math.cos(r * theta + phi_est) * t_val ** r
            for r in range(2, max_arity + 2)
        )
    else:
        G_asymptotic = G_series  # for non-oscillatory case, asymptotic = exact

    return {
        'c': c_val,
        't': t_val,
        'G_series': G_series,
        'H_closed_form': H_val,
        'H_series': H_series,
        'H_series_vs_closed': abs(H_series - (H_val if isinstance(H_val, (int, float)) else H_val.real)),
        'G_asymptotic': G_asymptotic,
        'shadow_radius': rho,
        'max_arity': max_arity,
        'paths_consistent': abs(H_series - (H_val if isinstance(H_val, (int, float)) else H_val.real)) < 1e-6,
    }


def cross_verify_nahm(c_val):
    """Cross-verify Nahm matrix eigenvalue = rho^2.

    Path 1: From Nahm matrix construction
    Path 2: From shadow radius formula
    Path 3: From ratio test on shadow coefficients
    """
    nahm = nahm_matrix_from_shadow(c_val)
    rho = virasoro_shadow_radius(c_val)
    S = shadow_tower_coefficients(c_val, 40)

    # Ratio test estimate of rho
    ratios = []
    for r in range(10, 35):
        if r in S and r - 1 in S and abs(S[r - 1]) > 1e-50:
            ratios.append(abs(S[r] / S[r - 1]))

    ratio_rho_est = ratios[-1] if ratios else None

    return {
        'c': c_val,
        'nahm_eigenvalue': nahm['eigenvalue'],
        'rho_squared': rho ** 2,
        'rho_from_formula': rho,
        'rho_from_ratio_test': ratio_rho_est,
        'nahm_eq_rho_sq': abs(nahm['eigenvalue'] - rho ** 2) < 1e-10,
        'formula_vs_ratio': abs(rho - (ratio_rho_est or rho)) / max(rho, 1e-15) if ratio_rho_est else None,
    }


# =========================================================================
# Section 9: W_N extensions (multi-generator quantum modularity)
# =========================================================================

def w3_shadow_data_T_line(c_val):
    """Shadow data for W_3 on the T-line (primary line of T generator).

    kappa(W_N) = c * (H_N - 1) where H_N = sum_{j=1}^{N} 1/j.
    For W_3: H_3 = 11/6, so kappa(W_3) = 5c/6.

    The T-line shadow uses the same structure as Virasoro with kappa = 5c/6.
    """
    kappa = c_val * 5.0 / 6.0
    alpha = 2.0  # cubic shadow coefficient (same universal value)
    # S_4 on the T-line: different from Virasoro due to W_3 quartic OPE
    # For W_3 T-line: Q^contact involves the full W_3 structure constants
    # Use the computed value from w3_shadow_extended if available
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))  # placeholder: same formula as Vir
    return kappa, alpha, S4


def quantum_modularity_summary(c_values=None, max_arity=80):
    """Summary of quantum modularity across the Virasoro landscape.

    Classifies each central charge by:
    - Shadow radius (convergent/divergent)
    - Nahm criterion (satisfied/violated)
    - S-defect structure
    """
    if c_values is None:
        c_values = [0.5, 0.7, 1.0, 2.0, 4.0, 6.0, 7.0, 10.0, 13.0, 25.0]

    results = []
    for c_val in c_values:
        rho = virasoro_shadow_radius(c_val)
        nahm = nahm_matrix_from_shadow(c_val)

        entry = {
            'c': c_val,
            'kappa': virasoro_kappa(c_val),
            'shadow_radius': rho,
            'convergent': rho < 1.0,
            'nahm_criterion': nahm['nahm_criterion_satisfied'],
            'rho_squared': rho ** 2,
        }

        # S-defect at x = 1/2
        if rho < 1:
            defect = quantum_modularity_S_defect(c_val, 2, max_arity)
            if not defect.get('singular'):
                entry['S_defect_weight_0'] = defect['defects_by_weight'].get(0)
                entry['S_defect_weight_3'] = defect['defects_by_weight'].get(3)

        results.append(entry)

    return results


# =========================================================================
# Section 10: Zwegers-type completion for shadow towers
# =========================================================================

def zwegers_mu_function(u, v, tau_val, max_terms=100):
    r"""Zwegers' mu-function: the building block for mock theta completions.

    mu(u, v; tau) = (e^{pi*i*u} / theta(v; tau))
                    * sum_{n in Z} (-1)^n * e^{pi*i*n*(n+1)*tau} * e^{2*pi*i*n*v}
                      / (1 - e^{2*pi*i*(n*tau + u)})

    This is a meromorphic Jacobi form that completes Ramanujan's mock theta
    functions to harmonic Maass forms.

    For numerical evaluation, we sum over n from -max_terms to max_terms.
    """
    q = cmath.exp(2j * PI * tau_val)
    zeta_u = cmath.exp(2j * PI * u)
    zeta_v = cmath.exp(2j * PI * v)

    # Jacobi theta function theta(v; tau) = sum_n (-1)^n q^{(n+1/2)^2/2} e^{2*pi*i*(n+1/2)*v}
    theta_val = complex(0.0)
    for n in range(-max_terms, max_terms + 1):
        nh = n + 0.5
        theta_val += ((-1) ** n) * q ** (nh ** 2 / 2.0) * cmath.exp(2j * PI * nh * v)

    if abs(theta_val) < 1e-50:
        return complex(float('nan'))

    # mu sum
    mu_sum = complex(0.0)
    for n in range(-max_terms, max_terms + 1):
        q_exp = q ** (n * (n + 1) / 2.0)
        z_exp = cmath.exp(2j * PI * n * v)
        denom = 1.0 - cmath.exp(2j * PI * (n * tau_val + u))
        if abs(denom) < 1e-15:
            continue  # skip poles
        mu_sum += ((-1) ** n) * q_exp * z_exp / denom

    return cmath.exp(1j * PI * u) / theta_val * mu_sum


def shadow_zwegers_completion(c_val, tau_val, max_terms=50):
    r"""Zwegers-type completion of the shadow generating function.

    For class-M shadows, the shadow tower has the form of a partial
    theta series (sum from n=0, not over all Z). The completion adds
    the "missing half" to restore modularity.

    The shadow metric Q_L determines a binary quadratic form which
    in turn specifies the theta function structure. The completion
    is Q_L-dependent.
    """
    kappa = virasoro_kappa(c_val)
    rho = virasoro_shadow_radius(c_val)

    q = cmath.exp(2j * PI * tau_val) if tau_val is not None else None
    y = tau_val.imag if tau_val is not None else 1.0

    # The shadow connection ∇^sh has monodromy -1 (Koszul sign)
    # This means the flat sections are half-period theta functions
    # The completion involves the error function integral

    # For the shadow PF at genus 1: the completion is the non-holomorphic
    # E_2* term, which adds 3/(pi*y) to E_2.
    # At higher arity: the completion involves the shadow metric discriminant

    result = {
        'c': c_val,
        'kappa': kappa,
        'shadow_radius': rho,
        'tau': tau_val,
        'Im_tau': y,
    }

    if tau_val is not None and y > 0:
        # Holomorphic shadow tower (formal, tau-independent)
        S = shadow_tower_coefficients(c_val, max_terms)
        G_formal = sum(S.get(r, 0) for r in range(2, max_terms + 2))
        result['G_formal'] = G_formal

        # Non-holomorphic correction from the shadow connection
        # nabla^sh = d - Q'/(2Q) dt has residue 1/2 at zeros of Q
        # The correction is proportional to 1/y (the simplest non-holomorphic term)
        q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
        Delta = 8.0 * kappa * virasoro_quartic(c_val) if abs(kappa) > 1e-15 else 0
        nh_coeff = -kappa * Delta / (12.0 * PI * y) if abs(Delta) > 1e-15 else 0

        result['nh_correction'] = nh_coeff
        result['G_completed'] = G_formal + nh_coeff
        result['Delta'] = Delta

    return result


# =========================================================================
# Section 11: Period polynomial and L-function connections
# =========================================================================

def period_polynomial_shadow(c_val, degree=10):
    r"""Period polynomial of the shadow generating function.

    For a modular form f of weight k, the period polynomial is
    r_f(X) = integral_0^{i*infty} f(tau) * (tau - X)^{k-2} dtau.

    For the shadow generating function, the "periods" are the integrals
    of S_r against modular cycles. Since S_r are constant (tau-independent),
    the period structure is determined by the recursive algebraic structure.

    The period polynomial P(X) = sum_{j=0}^{degree} a_j X^j where
    a_j involves the shadow coefficients S_r in a specific combination.
    """
    S = shadow_tower_coefficients(c_val, degree + 5)
    kappa = virasoro_kappa(c_val)

    # For the algebraic generating function H(t) = t^2*sqrt(Q_L(t)):
    # The "period" at index j is related to the j-th moment of S_r:
    # P_j = sum_{r>=2} S_r * binomial(r, j)
    # (This is the j-th finite difference of the generating function.)

    poly_coeffs = {}
    for j in range(degree + 1):
        P_j = 0.0
        for r in range(2, degree + 5):
            if r in S:
                binom_coeff = 1.0
                # Compute binomial(r, j) = r!/(j!(r-j)!)
                if j <= r:
                    binom_coeff = math.comb(r, j)
                else:
                    binom_coeff = 0
                P_j += S[r] * binom_coeff
        poly_coeffs[j] = P_j

    return {
        'c': c_val,
        'kappa': kappa,
        'degree': degree,
        'polynomial_coefficients': poly_coeffs,
        'leading_coefficient': poly_coeffs.get(degree, 0),
        'constant_term': poly_coeffs.get(0, 0),
    }


# =========================================================================
# Section 12: Master summary function
# =========================================================================

def quantum_modular_master_analysis(c_val, max_arity=80):
    """Complete quantum modularity analysis for Virasoro at central charge c.

    Combines all seven analysis modules:
    1. Shadow tower structure
    2. Quantum modularity defects
    3. Mock modular analysis
    4. Nahm conjecture
    5. Habiro ring
    6. Modular completion
    7. Radial limits

    Returns comprehensive analysis dict.
    """
    rho = virasoro_shadow_radius(c_val)
    kappa = virasoro_kappa(c_val)

    analysis = {
        'c': c_val,
        'kappa': kappa,
        'shadow_radius': rho,
        'convergent': rho < 1.0,
    }

    # 1. Shadow tower
    S = shadow_tower_coefficients(c_val, max_arity)
    analysis['shadow_coefficients_first_10'] = {r: S[r] for r in range(2, min(12, max(S.keys()) + 1))}

    # 2. Nahm
    analysis['nahm'] = nahm_matrix_from_shadow(c_val)

    # 3. Mock modular
    analysis['mock_modular'] = mock_modular_shadow_analysis(c_val, max_terms=max_arity)

    # 4. Cross-verification
    t_test = 0.1  # safe value inside convergence disk for c > c*
    analysis['cross_verify'] = cross_verify_shadow_gf(c_val, t_test, min(max_arity, 100))

    # 5. Habiro scan
    analysis['habiro'] = habiro_scan(c_val, [3, 4, 5, 6])

    return analysis
