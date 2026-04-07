r"""
koszul_epstein_moment_matrix.py — Quartic residue moment matrix from the shadow obstruction tower.

THE CONSTRUCTION:

The shadow obstruction tower yields shadow coefficients S_2 = kappa, S_3 = alpha,
S_4 = Q^contact, S_5, S_6, ... for each chiral algebra.  These coefficients
arise as Taylor coefficients of H(t) = t^2 * sqrt(Q_L(t)), where Q_L is the
shadow metric.

The SHADOW HANKEL MATRIX of order r is the r x r matrix

    (H_r)_{i,j}  =  S_{i+j+2},   i,j = 0, 1, ..., r-1

so that:
    H_1 = (S_2) = (kappa)
    H_2 = ((S_2, S_3), (S_3, S_4))
    H_3 = ((S_2, S_3, S_4), (S_3, S_4, S_5), (S_4, S_5, S_6))
    ...

This is a Hankel matrix: constant along anti-diagonals.

MOMENT PROBLEM INTERPRETATION:

If there exists a positive measure mu on R such that

    S_{r+2} = integral x^r d mu(x)    for r = 0, 1, 2, ...

then the Hamburger moment conditions require det(H_r) >= 0 for all r, with
strict inequality when the measure has r or more points of support.

More precisely:
  - det(H_r) > 0 for all r:  mu is a positive measure with infinite support.
  - det(H_r) > 0 for r <= N, det(H_{N+1}) = 0:  mu is supported on N points.
  - det(H_r) < 0 for some r:  NO positive measure exists.  The "spectral
    measure" is SIGNED.

The moment matrix captures the quartic and higher residue structure of the
constrained Epstein zeta function associated to the shadow metric.

SHADOW DEPTH CLASSES:

  G (Gaussian, Heisenberg):   S_r = 0 for r >= 3.
      H_1 = (kappa).  det = kappa > 0.  H_r = 0 for r >= 2.
      Measure: point mass at 0 with weight kappa.

  L (Lie/tree, affine KM):   S_r = 0 for r >= 4.  S_3 = alpha != 0.
      H_2 = ((kappa, alpha), (alpha, 0)).  det = -alpha^2 < 0.
      SIGNED.  No positive measure exists.

  C (Contact, beta-gamma):   S_r = 0 for r >= 5.  S_4 != 0.
      H_2 det = kappa * S_4 - alpha^2.  Sign depends on algebra.

  M (Mixed, Virasoro/W_N):   All S_r nonzero.
      Infinite tower.  Full Hankel analysis applies.

KEY RESULT (from computation):

For Virasoro at generic c > 0:
  det(H_1) = c/2 > 0.
  det(H_2) = c/2 * 10/(c(5c+22)) - 4 = (10/(5c+22) - 4) = (10 - 20c - 88)/(5c+22)
           = -(20c+78)/(5c+22) < 0 for all c > 0.

So det(H_2) < 0 at ALL positive central charges for Virasoro.  The spectral
measure is SIGNED from the very first Hankel minor beyond the trivial one.
This is a STRUCTURAL result: the shadow obstruction tower of any class-L or class-M
algebra with nonzero cubic shadow has a signed spectral measure.

The physical meaning: the constrained Epstein zeta is NOT a standard positive-
definite Epstein zeta.  It belongs to a different analytic class.  The DH
counterexamples (Davenport-Heilbronn, etc.) use positive-definite forms;
the shadow metric produces a SIGNED moment problem, which is in a genuinely
different universality class.

Manuscript references:
    prop:hankel-extraction (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    eq:shadow-hankel (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    from sympy import Rational, Symbol, simplify, sqrt as sym_sqrt, factor
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# ================================================================
# 1. Shadow coefficient computation (self-contained, from first principles)
# ================================================================

def virasoro_shadow_data(c_val):
    r"""Return (kappa, alpha, S4) for Virasoro at central charge c.

    kappa = c/2,  alpha = 2,  S4 = 10/(c(5c+22)).

    These are exact if c_val is a Fraction; numeric otherwise.
    """
    if isinstance(c_val, Fraction):
        kappa = c_val / 2
        alpha = Fraction(2)
        S4 = Fraction(10) / (c_val * (5 * c_val + 22))
        return kappa, alpha, S4
    c = float(c_val)
    return c / 2.0, 2.0, 10.0 / (c * (5 * c + 22))


def heisenberg_shadow_data(k=1):
    r"""Shadow data for Heisenberg at level k.

    kappa = k (AP39: NOT k/2),  alpha = 0,  S4 = 0.
    Class G: tower terminates at arity 2.
    """
    if isinstance(k, Fraction):
        return k, Fraction(0), Fraction(0)
    return float(k), 0.0, 0.0


def affine_km_shadow_data(dim_g, k, h_dual):
    r"""Shadow data for affine Kac-Moody g-hat at level k.

    kappa = dim(g) * (k + h^v) / (2 h^v)
    alpha = 2 (the universal cubic)
    S4 = 0 (class L: tree-level, terminates at arity 3)
    Delta = 0.

    Class L algebras have S_r = 0 for r >= 4.
    """
    if isinstance(k, Fraction):
        kappa = Fraction(dim_g) * (k + h_dual) / (2 * h_dual)
        return kappa, Fraction(2), Fraction(0)
    kappa = float(dim_g) * (float(k) + float(h_dual)) / (2.0 * float(h_dual))
    return kappa, 2.0, 0.0


def betagamma_shadow_data(c_val):
    r"""Shadow data for beta-gamma at central charge c = -2 * lambda.

    kappa = c/2 = -lambda
    alpha = 2
    S4 = Q^contact_bg (nonzero, computed from OPE)

    Class C: tower terminates at arity 4.

    For the standard beta-gamma system (c = -2):
        kappa = -1, alpha = 2, S4 = -5/16.
    """
    if isinstance(c_val, Fraction):
        kappa = c_val / 2
        alpha = Fraction(2)
        # beta-gamma quartic: S4 = -5/(16*kappa) when alpha=2
        # From the manuscript: Q^contact_bg computed from explicit OPE
        # For c = -2: S4 = -5/16, giving Delta = 8*(-1)*(-5/16) = 5/2
        # General formula: S4 = 10/(c(5c+22)) same as Virasoro (beta-gamma IS Virasoro at c=-2)
        # but beta-gamma terminates because of stratum separation at arity 5
        S4 = Fraction(10) / (c_val * (5 * c_val + 22))
        return kappa, alpha, S4
    c = float(c_val)
    kappa = c / 2.0
    alpha = 2.0
    S4 = 10.0 / (c * (5 * c + 22))
    return kappa, alpha, S4


def shadow_coefficients_from_data(kappa, alpha, S4, max_r=30):
    r"""Compute shadow coefficients S_2, ..., S_{max_r} from shadow data.

    Uses the convolution recursion from f^2 = Q_L:
        f(t) = sqrt(Q_L(t)),  Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
        S_r = a_{r-2} / r   where a_n = [t^n] f(t).

    The recursion:
        a_0 = sqrt(q0) = 2*|kappa|
        a_1 = q1 / (2*a0) = 12*kappa*alpha / (2*2*|kappa|) = 3*alpha * sign(kappa)
        a_2 = (q2 - a_1^2) / (2*a0)
        a_n = -(1/(2*a0)) * sum_{j=1}^{n-1} a_j * a_{n-j}   for n >= 3
    """
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    a0 = math.sqrt(float(q0))
    if a0 == 0:
        return {r: 0.0 for r in range(2, max_r + 1)}

    max_n = max_r - 2
    a = [0.0] * (max_n + 1)
    a[0] = a0
    if max_n >= 1:
        a[1] = float(q1) / (2.0 * a0)
    if max_n >= 2:
        a[2] = (float(q2) - a[1] ** 2) / (2.0 * a0)
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a0)

    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


def shadow_coefficients_virasoro(c_val, max_r=30):
    r"""Shadow obstruction tower for Virasoro at central charge c."""
    kappa, alpha, S4 = virasoro_shadow_data(c_val)
    return shadow_coefficients_from_data(kappa, alpha, S4, max_r)


# ================================================================
# 2. Shadow Hankel matrix (the moment matrix)
# ================================================================

def shadow_hankel_matrix(shadow_coeffs, r):
    r"""Build the r x r shadow Hankel matrix.

    (H_r)_{i,j} = S_{i+j+2}   for i,j = 0, ..., r-1.

    Requires shadow_coeffs to contain keys 2, 3, ..., 2r.

    Parameters:
        shadow_coeffs: Dict mapping arity -> coefficient value.
        r: Order of the Hankel matrix.

    Returns:
        r x r list-of-lists.
    """
    H = [[0.0] * r for _ in range(r)]
    for i in range(r):
        for j in range(r):
            key = i + j + 2
            if key in shadow_coeffs:
                H[i][j] = float(shadow_coeffs[key])
            else:
                raise KeyError(
                    f"Shadow coefficient S_{key} needed for H_{r} but not provided. "
                    f"Need S_2 through S_{2*r}."
                )
    return H


def hankel_det(H):
    r"""Determinant of a small matrix (list-of-lists) via LU decomposition.

    For matrices up to ~10x10, this is adequate.
    Uses Gaussian elimination with partial pivoting.
    """
    n = len(H)
    # Copy
    M = [row[:] for row in H]
    det = 1.0
    for col in range(n):
        # Partial pivoting
        max_row = col
        max_val = abs(M[col][col])
        for row in range(col + 1, n):
            if abs(M[row][col]) > max_val:
                max_val = abs(M[row][col])
                max_row = row
        if max_row != col:
            M[col], M[max_row] = M[max_row], M[col]
            det *= -1
        if abs(M[col][col]) < 1e-300:
            return 0.0
        det *= M[col][col]
        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for k in range(col + 1, n):
                M[row][k] -= factor * M[col][k]
    return det


def shadow_hankel_determinants(shadow_coeffs, max_r=6):
    r"""Compute det(H_1), det(H_2), ..., det(H_{max_r}).

    Returns list of determinants.  The r-th entry (0-indexed) is det(H_{r+1}).
    """
    dets = []
    for r in range(1, max_r + 1):
        needed = 2 * r
        if needed not in shadow_coeffs:
            break
        H = shadow_hankel_matrix(shadow_coeffs, r)
        dets.append(hankel_det(H))
    return dets


def moment_matrix_sign_sequence(shadow_coeffs, max_r=6):
    r"""Sign sequence of det(H_1), det(H_2), ..., det(H_{max_r}).

    Returns list of +1, 0, or -1.

    INTERPRETATION:
      All positive:  positive measure (standard moment problem).
      Some negative: signed measure (no positive measure exists).
      Zero:          degenerate (measure supported on finitely many points).

    For the shadow obstruction tower:
      Class G (Heisenberg):  (+, 0, 0, ...)  — point mass at 0.
      Class L (affine KM):   (+, -, ...)     — signed from rank 2.
      Class M (Virasoro):    (+, -, ...)     — signed from rank 2.
    """
    dets = shadow_hankel_determinants(shadow_coeffs, max_r)
    signs = []
    for d in dets:
        if abs(d) < 1e-100:
            signs.append(0)
        elif d > 0:
            signs.append(1)
        else:
            signs.append(-1)
    return signs


# ================================================================
# 3. Exact (Fraction-based) computation for small matrices
# ================================================================

def shadow_hankel_matrix_exact(shadow_coeffs_exact, r):
    r"""Build the r x r shadow Hankel matrix with exact (Fraction) entries.

    Parameters:
        shadow_coeffs_exact: Dict mapping arity -> Fraction.
        r: Order.

    Returns:
        r x r list-of-lists of Fractions.
    """
    H = [[Fraction(0)] * r for _ in range(r)]
    for i in range(r):
        for j in range(r):
            key = i + j + 2
            if key in shadow_coeffs_exact:
                H[i][j] = shadow_coeffs_exact[key]
            else:
                raise KeyError(f"Shadow coefficient S_{key} needed but not provided.")
    return H


def hankel_det_exact(H):
    r"""Exact determinant via bareiss algorithm (fraction-free for Fractions).

    For small matrices (r <= 6), this is perfectly fine.
    """
    n = len(H)
    if n == 1:
        return H[0][0]
    if n == 2:
        return H[0][0] * H[1][1] - H[0][1] * H[1][0]
    if n == 3:
        return (H[0][0] * (H[1][1] * H[2][2] - H[1][2] * H[2][1])
                - H[0][1] * (H[1][0] * H[2][2] - H[1][2] * H[2][0])
                + H[0][2] * (H[1][0] * H[2][1] - H[1][1] * H[2][0]))

    # General: Gaussian elimination with Fractions
    M = [row[:] for row in H]
    det = Fraction(1)
    for col in range(n):
        # Find pivot
        pivot_row = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]
            det *= -1
        det *= M[col][col]
        pivot = M[col][col]
        for row in range(col + 1, n):
            f = Fraction(M[row][col], pivot) if isinstance(pivot, int) else M[row][col] / pivot
            for k in range(col + 1, n):
                M[row][k] -= f * M[col][k]
            M[row][col] = Fraction(0)
    return det


# ================================================================
# 4. Virasoro moment matrix analysis
# ================================================================

def virasoro_hankel_analysis(c_val, max_r=6):
    r"""Full Hankel analysis for Virasoro at central charge c.

    Returns dict with:
        shadow_coeffs: {r: S_r}
        hankel_dets: [det(H_1), ..., det(H_{max_r})]
        sign_sequence: [sgn det(H_1), ...]
        is_positive: True iff all dets > 0 (positive measure)
        first_negative: first r where det(H_r) < 0 (or None)
        summary: string description
    """
    max_arity = 2 * max_r
    coeffs = shadow_coefficients_virasoro(c_val, max_arity)
    dets = shadow_hankel_determinants(coeffs, max_r)
    signs = []
    first_neg = None
    for i, d in enumerate(dets):
        if abs(d) < 1e-100:
            signs.append(0)
        elif d > 0:
            signs.append(1)
        else:
            signs.append(-1)
            if first_neg is None:
                first_neg = i + 1  # 1-indexed rank
    all_pos = all(s == 1 for s in signs)
    return {
        'c': c_val,
        'shadow_coeffs': coeffs,
        'hankel_dets': dets,
        'sign_sequence': signs,
        'is_positive': all_pos,
        'first_negative': first_neg,
    }


def virasoro_H2_det_exact(c_val):
    r"""Exact det(H_2) for Virasoro.

    H_2 = ((S_2, S_3), (S_3, S_4)) = ((c/2, 2), (2, 10/(c(5c+22))))

    det(H_2) = c/2 * 10/(c(5c+22)) - 4
             = 5/(5c+22) - 4
             = (5 - 20c - 88) / (5c+22)
             = -(20c + 83) / (5c+22)

    For c > 0: numerator -(20c+83) < 0, denominator 5c+22 > 0.
    So det(H_2) < 0 for ALL c > 0.

    For c = -22/5 (Lee-Yang): denominator vanishes (S_4 has a pole).
    For c in (-83/20, 0) and 5c+22 > 0, i.e. c in (-83/20, 0):
      numerator = -(20c+83) > 0 when 20c+83 < 0, i.e. c < -83/20.
      But 5c+22 > 0 requires c > -22/5 = -4.4, and -83/20 = -4.15.
      So for c in (-4.4, -4.15): numerator > 0, denom > 0 => det > 0.
      For c in (-4.15, 0): numerator < 0, denom > 0 => det < 0.

    CONCLUSION: det(H_2) < 0 for ALL c > 0 (and most c < 0).
    The spectral measure is SIGNED for Virasoro at any physical c.
    """
    if isinstance(c_val, Fraction):
        c = c_val
        return -(20 * c + 83) / (5 * c + 22)
    c = float(c_val)
    return -(20 * c + 83) / (5 * c + 22)


def virasoro_H2_det_derivation():
    r"""Return a string showing the exact derivation of det(H_2) for Virasoro.

    This is an independent verification, NOT using the recursion.
    """
    return (
        "det(H_2) = S_2 * S_4 - S_3^2\n"
        "         = (c/2) * 10/(c(5c+22)) - 2^2\n"
        "         = 5/(5c+22) - 4\n"
        "         = (5 - 4(5c+22)) / (5c+22)\n"
        "         = (5 - 20c - 88) / (5c+22)\n"
        "         = -(20c + 83) / (5c+22)\n"
        "\n"
        "For c > 0: 20c+83 > 0, 5c+22 > 0, so det < 0.\n"
        "The spectral measure is SIGNED at all positive central charges."
    )


# ================================================================
# 5. Multi-family comparison
# ================================================================

def class_G_moment_analysis(kappa):
    r"""Moment analysis for class G (Heisenberg/Gaussian).

    Shadow data: S_2 = kappa, S_r = 0 for r >= 3.
    H_1 = (kappa).  det = kappa.  Positive iff kappa > 0 (i.e. k > 0).
    H_r = 0 for r >= 2 (all entries in rows/cols >= 1 are zero).

    Spectral interpretation: point mass mu = kappa * delta(x=0).
    """
    return {
        'class': 'G',
        'kappa': kappa,
        'H1_det': float(kappa),
        'H2_det': 0.0,  # S_3 = S_4 = 0 => det = kappa*0 - 0 = 0
        'sign_sequence': [1 if kappa > 0 else (-1 if kappa < 0 else 0), 0],
        'is_positive': True,  # degenerate positive (point mass)
        'interpretation': 'Point mass at origin with weight kappa',
    }


def class_L_moment_analysis(kappa, alpha):
    r"""Moment analysis for class L (affine Kac-Moody, tree-level).

    Shadow data: S_2 = kappa, S_3 = alpha, S_r = 0 for r >= 4.
    H_1 = (kappa).  det = kappa > 0.
    H_2 = ((kappa, alpha), (alpha, 0)).  det = -alpha^2.
    H_3 entries involve S_4 = 0, S_5 = 0, S_6 = 0.

    det(H_2) = -alpha^2 < 0 whenever alpha != 0.
    SIGNED for all nonzero cubic shadow.

    Spectral interpretation: the "measure" has negative part.
    Equivalently: the shadow obstruction tower OPE coefficients satisfy
    a signed integral representation, not a positive one.
    """
    det_H2 = -float(alpha) ** 2
    return {
        'class': 'L',
        'kappa': float(kappa),
        'alpha': float(alpha),
        'H1_det': float(kappa),
        'H2_det': det_H2,
        'sign_sequence': [
            1 if kappa > 0 else (-1 if kappa < 0 else 0),
            -1 if alpha != 0 else 0,
        ],
        'is_positive': False,  # alpha != 0 => signed
        'interpretation': 'Signed measure (negative Hankel det at rank 2)',
    }


def class_M_moment_analysis(c_val, max_r=6):
    r"""Full moment analysis for class M (Virasoro/W_N).

    The infinite shadow obstruction tower gives a full sequence of Hankel determinants.
    """
    result = virasoro_hankel_analysis(c_val, max_r)
    result['class'] = 'M'
    if result['first_negative'] is not None:
        result['interpretation'] = (
            f"Signed measure (first negative det at rank {result['first_negative']})"
        )
    else:
        result['interpretation'] = 'Positive measure (all dets positive)'
    return result


# ================================================================
# 6. Shadow Hankel matrix in exact rational arithmetic
# ================================================================

def virasoro_shadow_coefficients_exact(c_frac, max_r=12):
    r"""Exact shadow coefficients for Virasoro as Fractions.

    Uses the convolution recursion with Fraction arithmetic.

    Parameters:
        c_frac: Fraction (central charge).
        max_r: maximum arity.

    Returns:
        Dict mapping r -> Fraction.
    """
    c = c_frac
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    # sqrt(q0) = 2*|kappa| = c (for c > 0)
    # For exact Fraction work, assume c > 0 so sqrt(c^2) = c.
    if c <= 0:
        raise ValueError("Exact computation requires c > 0 (positive Fraction).")
    a0 = c  # sqrt(4*(c/2)^2) = sqrt(c^2) = c

    max_n = max_r - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = a0
    if max_n >= 1:
        a[1] = q1 / (2 * a0)
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a0)
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a0)

    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


def virasoro_hankel_dets_exact(c_frac, max_r=4):
    r"""Exact Hankel determinants for Virasoro.

    Returns list of Fractions: [det(H_1), det(H_2), ..., det(H_{max_r})].
    """
    max_arity = 2 * max_r
    coeffs = virasoro_shadow_coefficients_exact(c_frac, max_arity)
    dets = []
    for r in range(1, max_r + 1):
        H = shadow_hankel_matrix_exact(coeffs, r)
        dets.append(hankel_det_exact(H))
    return dets


# ================================================================
# 7. Cross-family Hankel determinant table
# ================================================================

def hankel_landscape(max_r=4):
    r"""Compute Hankel determinants for all standard families.

    Returns dict mapping family name -> analysis dict.
    """
    landscape = {}

    # Class G: Heisenberg
    landscape['Heisenberg_k1'] = class_G_moment_analysis(Fraction(1, 2))

    # Class L: affine sl_2 at level 1
    # kappa = dim(sl2)*(k+h^v)/(2*h^v) = 3*(1+2)/(2*2) = 9/4
    landscape['sl2_k1'] = class_L_moment_analysis(Fraction(9, 4), Fraction(2))

    # Class L: affine sl_3 at level 1
    # kappa = 8*(1+3)/(2*3) = 16/3
    landscape['sl3_k1'] = class_L_moment_analysis(Fraction(16, 3), Fraction(2))

    # Class M: Virasoro at various c
    for c_num, c_label in [
        (Fraction(1, 2), 'Ising_c1/2'),
        (Fraction(7, 10), 'TIM_c7/10'),
        (Fraction(1), 'c1'),
        (Fraction(13), 'selfdual_c13'),
        (Fraction(26), 'critical_c26'),
    ]:
        try:
            result = virasoro_hankel_analysis(float(c_num), max_r)
            result['class'] = 'M'
            landscape[f'Virasoro_{c_label}'] = result
        except (ZeroDivisionError, ValueError):
            pass

    return landscape


# ================================================================
# 8. Spectral measure reconstruction (formal)
# ================================================================

def signed_spectral_decomposition_info():
    r"""Explanation of the signed spectral measure.

    The shadow Hankel matrix having negative determinants means:
    S_{r+2} = integral x^r d mu(x) where mu is a SIGNED measure.

    This signed measure mu = mu^+ - mu^- with:
      mu^+ = positive part
      mu^- = negative part
    total variation |mu| = mu^+ + mu^-.

    The Stieltjes transform s(z) = integral d mu(x)/(z-x) still exists
    and has an asymptotic expansion s(z) ~ sum S_{r+2} / z^{r+1}.
    But now s(z) is NOT a Herglotz function (does not map upper half plane
    to upper half plane), which means the associated "spectral problem"
    lives outside the standard positive-definite framework.

    For the constrained Epstein zeta: this means the zeta function
    epsilon_Q(s) is NOT a standard Epstein zeta of a positive definite form.
    It is an "Epstein-like" function associated to an indefinite quadratic
    form, or more precisely, to a signed moment problem.

    Connection to DH counterexamples:
      Davenport-Heilbronn (1936) constructed Epstein zetas of POSITIVE DEFINITE
      forms with zeros off the critical line.  Those forms have h(d) > 1.
      The shadow metric Q_L is positive definite (for c > -22/5), but the
      MOMENT PROBLEM is signed.  These are different obstructions:
      - DH: positive form, but class number > 1 => no Euler product.
      - Shadow: positive form, but signed moments => non-positive spectral measure.
      The shadow case is in a different analytic class from DH.
    """
    return "Signed spectral measure: see docstring."


# ================================================================
# 9. Alternating Hankel determinants (Turán-type invariants)
# ================================================================

def turan_ratios(shadow_coeffs, max_r=6):
    r"""Turán-type ratios det(H_r) / (det(H_{r-1}) * det(H_{r+1})).

    For a positive measure, these are related to the Christoffel-Darboux
    kernel and are always positive.  For signed measures, they can be
    negative or diverge.

    Returns list of (r, ratio) pairs.
    """
    dets = shadow_hankel_determinants(shadow_coeffs, max_r)
    ratios = []
    for i in range(1, len(dets) - 1):
        r = i + 1  # rank r
        if abs(dets[i - 1]) > 1e-300 and abs(dets[i + 1]) > 1e-300:
            ratio = dets[i] ** 2 / (dets[i - 1] * dets[i + 1])
            ratios.append((r, ratio))
        else:
            ratios.append((r, float('inf')))
    return ratios


# ================================================================
# 10. Schur complement extraction of higher contacts
# ================================================================

def schur_complement_sequence(shadow_coeffs, max_r=5):
    r"""Schur complements of the shadow Hankel matrix.

    The Schur complement of H_r in H_{r+1} extracts the "intrinsic"
    contribution at arity 2r+2, not already determined by lower arities.

    sc_r = H_{r+1}[r,r] - H_{r+1}[r, 0:r] * H_r^{-1} * H_{r+1}[0:r, r]

    When H_r is positive definite, sc_r = det(H_{r+1}) / det(H_r).
    In general (signed case), this ratio still gives the Schur complement.

    Returns list of (r, schur_complement) pairs.
    """
    dets = shadow_hankel_determinants(shadow_coeffs, max_r + 1)
    schurs = []
    for i in range(len(dets) - 1):
        r = i + 1
        if abs(dets[i]) > 1e-300:
            sc = dets[i + 1] / dets[i]
            schurs.append((r, sc))
        else:
            schurs.append((r, float('inf')))
    return schurs


# ================================================================
# 11. Positivity phase diagram (c-dependence)
# ================================================================

def positivity_scan(c_values, max_r=4):
    r"""Scan det(H_r) over a range of central charges.

    Returns dict mapping c -> sign_sequence.
    Useful for finding the positivity boundary (if any).
    """
    results = {}
    for c_val in c_values:
        try:
            analysis = virasoro_hankel_analysis(c_val, max_r)
            results[c_val] = analysis['sign_sequence']
        except (ZeroDivisionError, ValueError):
            results[c_val] = None
    return results


def positivity_boundary_H2():
    r"""The exact c-value where det(H_2) changes sign for Virasoro.

    det(H_2) = -(20c + 83) / (5c + 22)

    Zeros: 20c + 83 = 0 => c = -83/20 = -4.15
    Poles: 5c + 22 = 0 => c = -22/5 = -4.4

    Sign chart:
      c < -4.4:  (-)(-)/(-)  = +/-  [need careful analysis]
      c in (-4.4, -4.15):  (-)(-)/( +) = +
      c in (-4.15, 0):  (-)(+)/(+) = -
      c > 0:  (-)(+)/(+) = -

    For c < -22/5: both 20c+83 < 0 and 5c+22 < 0, so det = (-)(-)/(- ) = - > 0? NO:
    -(20c+83)/(5c+22). Let c = -5: -(20*(-5)+83)/(5*(-5)+22) = -(-100+83)/(-25+22) = -(-17)/(-3) = -(17/3) < 0.
    Hmm, let me recompute.

    At c = -5:  -(20(-5)+83)/(5(-5)+22) = -(- 100+83)/(-25+22) = -(-17)/(-3) = -(17/3) ≈ -5.67.
    At c = -4.3: -(20(-4.3)+83)/(5(-4.3)+22) = -(-86+83)/(-21.5+22) = -(-3)/(0.5) = 6.
    At c = -4: -(20(-4)+83)/(5(-4)+22) = -(-80+83)/(-20+22) = -(3)/(2) = -1.5.

    So: positive for c in (-22/5, -83/20) ≈ (-4.4, -4.15).
    Negative everywhere else where defined.
    """
    return {
        'zero': Fraction(-83, 20),  # det = 0
        'pole': Fraction(-22, 5),    # det diverges
        'positive_interval': (Fraction(-22, 5), Fraction(-83, 20)),
        'negative_for_c_positive': True,
    }


# ================================================================
# 12. Higher Hankel determinant exact formulas
# ================================================================

def virasoro_H3_det_exact(c_val):
    r"""Exact det(H_3) for Virasoro.

    det(H_3) = -8*(9000*c^2 + 81710*c + 185909) / (3*c^3*(5c+22)^3)

    The numerator quadratic 9000c^2 + 81710c + 185909 has discriminant
    81710^2 - 4*9000*185909 = -16199900 < 0 and constant term 185909 > 0,
    so it is POSITIVE for ALL real c.

    Therefore det(H_3) = -8*(positive) / (3*c^3*(5c+22)^3) < 0 for all c > 0.

    THEOREM: det(H_3) < 0 for ALL c > 0.

    Combined with det(H_2) < 0 for all c > 0 (from virasoro_H2_det_exact),
    the first TWO nontrivial Hankel minors are BOTH negative for all c > 0.
    The spectral measure is signed, with the negativity starting at rank 2.

    Derivation: symbolic computation via sympy, verified at c=1/2, 1, 5, 13, 26.
    """
    if isinstance(c_val, Fraction):
        c = c_val
        num = 9000 * c ** 2 + 81710 * c + 185909
        denom = 3 * c ** 3 * (5 * c + 22) ** 3
        return Fraction(-8) * num / denom
    c = float(c_val)
    return -8 * (9000 * c ** 2 + 81710 * c + 185909) / (3 * c ** 3 * (5 * c + 22) ** 3)


def virasoro_H3_det_formula():
    r"""Exact det(H_3) for Virasoro (symbolic).

    H_3 = ((S_2, S_3, S_4),
           (S_3, S_4, S_5),
           (S_4, S_5, S_6))

    This is a 3x3 determinant involving S_2 through S_6.
    Compute symbolically to verify sign.
    """
    if not HAS_SYMPY:
        return None
    c = Symbol('c', positive=True)
    kappa = c / 2
    alpha = Rational(2)
    S4_val = Rational(10) / (c * (5 * c + 22))

    # Need S_5 and S_6 from the recursion
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4_val

    a0 = c  # sqrt(c^2)
    a1 = q1 / (2 * a0)
    a2 = (q2 - a1 ** 2) / (2 * a0)
    # a3
    conv3 = a1 * a2 + a2 * a1
    a3 = -conv3 / (2 * a0)
    # a4
    conv4 = a1 * a3 + a2 * a2 + a3 * a1
    a4 = -conv4 / (2 * a0)

    S = {
        2: a0 / 2,        # a_{0}/2
        3: a1 / 3,        # a_{1}/3
        4: a2 / 4,        # a_{2}/4
        5: a3 / 5,        # a_{3}/5
        6: a4 / 6,        # a_{4}/6
    }

    # Verify S_2 = c/2, S_3 = 2
    s2_check = simplify(S[2] - kappa)
    s3_check = simplify(S[3] - alpha)

    H3 = [
        [S[2], S[3], S[4]],
        [S[3], S[4], S[5]],
        [S[4], S[5], S[6]],
    ]

    det_val = (H3[0][0] * (H3[1][1] * H3[2][2] - H3[1][2] * H3[2][1])
               - H3[0][1] * (H3[1][0] * H3[2][2] - H3[1][2] * H3[2][0])
               + H3[0][2] * (H3[1][0] * H3[2][1] - H3[1][1] * H3[2][0]))

    det_simplified = simplify(det_val)
    det_factored = factor(det_val)

    return {
        'shadow_coeffs': S,
        's2_check': s2_check,
        's3_check': s3_check,
        'det_H3_raw': det_val,
        'det_H3_simplified': det_simplified,
        'det_H3_factored': det_factored,
    }


# ================================================================
# 13. Affine Kac-Moody moment analysis
# ================================================================

def affine_km_hankel_analysis(dim_g, k, h_dual, max_r=4):
    r"""Hankel analysis for affine Kac-Moody.

    Class L: S_r = 0 for r >= 4.
    H_1 = (kappa), det = kappa > 0 (for k > -h^v).
    H_2 = ((kappa, alpha), (alpha, 0)), det = -alpha^2 < 0.
    H_r for r >= 3: involves S_4 = S_5 = ... = 0, so these are
    highly degenerate.

    The signed measure for class L:
      S_2 = kappa, S_3 = alpha (nonzero), S_{r+2} = 0 for r >= 2.
      This means integral x^r d mu(x) = 0 for r >= 2.
      Combined with integral d mu = kappa and integral x d mu = alpha:
      mu must have support only at x = 0 and one other point, with
      the second moment vanishing.  But integral d mu = kappa and
      integral x d mu = alpha with all higher moments zero is impossible
      for a POSITIVE measure on more than one point (Carleman condition).
      Indeed: a positive measure with integral x d mu = alpha != 0
      requires integral x^2 d mu >= alpha^2 / kappa > 0 (Cauchy-Schwarz),
      but S_4 = 0 gives integral x^2 d mu = 0.  Contradiction.
    """
    kappa, alpha, S4 = affine_km_shadow_data(dim_g, k, h_dual)
    result = class_L_moment_analysis(kappa, alpha)
    result['dim_g'] = dim_g
    result['level'] = k
    result['h_dual'] = h_dual
    return result


# ================================================================
# 14. Invariant ratios
# ================================================================

def normalized_hankel_sequence(shadow_coeffs, max_r=6):
    r"""Normalized Hankel sequence: det(H_r) / kappa^r.

    For class G: [1, 0, 0, ...].
    For class L: [1, -alpha^2/kappa^2, ...].
    For class M: nontrivial oscillating sequence.

    The normalization by kappa^r removes the overall scale.
    """
    kappa = shadow_coeffs.get(2, 0)
    if abs(float(kappa)) < 1e-300:
        return []
    kappa_f = float(kappa)
    dets = shadow_hankel_determinants(shadow_coeffs, max_r)
    return [d / kappa_f ** (i + 1) for i, d in enumerate(dets)]
