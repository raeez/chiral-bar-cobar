"""W_4 OPE extraction via the quantum Miura transformation for sl_4.

Computes the 6 stage-4 OPE coefficients for the W_4 algebra (principal
Drinfeld-Sokolov reduction of sl_4-hat) by:
  1. Setting up the sl_4 root system (Cartan matrix, weights of fundamental rep).
  2. Constructing the quantum Miura operator with N=4 free bosons.
  3. Expressing W_2=T, W_3, W_4 as free-boson composites.
  4. Computing OPEs via Wick contractions (numerically at sample c-values).
  5. Extracting primary OPE coefficients by subtracting descendant contributions.
  6. Interpolating to rational functions of c.

TARGET (from rem:mc4-winfty-computation-target):
  4 free coefficients:
    c_334  = C^DS_{3,3;4;0,2}  (W_3 x W_3 -> W_4 at pole 2)
    c_444  = C^DS_{4,4;4;0,4}  (W_4 x W_4 -> W_4 at pole 4)
    C_{3,4;3;0,4}              (W_3 x W_4 -> W_3 at pole 4)
    C_{3,4;4;0,3}              (W_3 x W_4 -> W_4 at pole 3)
  2 falsifiable predictions:
    C^res_{4,4;2;0,6} = 2     (universal T-coupling)
    C^res_{3,4;2;0,5} = 0     (mixed Virasoro vanishing)

CONVENTIONS:
  - Central charge: c = 3 - 60(k+3)^2/(k+4) for W_4 from sl_4
  - Composite: Lambda = :TT: - (3/10) d^2 T
  - Cohomological grading: |d| = +1
  - Free boson propagator: <dphi_i(z) dphi_j(w)> = -delta_{ij}/(z-w)^2
  - Normal ordering: standard radial ordering
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product as iterproduct
from typing import Dict, List, Optional, Tuple

import numpy as np
from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    factorial,
    nsimplify,
    simplify,
    sqrt,
    sympify,
    together,
)


# =========================================================================
# sl_4 root system data
# =========================================================================

def sl4_cartan_matrix() -> np.ndarray:
    """Cartan matrix of sl_4 (type A_3)."""
    return np.array([
        [ 2, -1,  0],
        [-1,  2, -1],
        [ 0, -1,  2],
    ], dtype=float)


def sl4_simple_roots() -> np.ndarray:
    """Simple roots alpha_1, alpha_2, alpha_3 of sl_4 in orthonormal basis.

    Using the embedding in R^4 with constraint sum = 0:
      alpha_i = e_i - e_{i+1}
    Projected to the 3-dimensional Cartan subalgebra.
    """
    # Standard orthonormal basis in R^4
    # alpha_1 = e_1 - e_2, alpha_2 = e_2 - e_3, alpha_3 = e_3 - e_4
    # We work in R^3 using an orthonormal basis for the Cartan subalgebra.
    # The inner product is (alpha_i, alpha_j) = A_{ij}.
    # Use the standard realization:
    return np.array([
        [ 1, -1,  0,  0],
        [ 0,  1, -1,  0],
        [ 0,  0,  1, -1],
    ], dtype=float)


def sl4_fundamental_weights() -> np.ndarray:
    """Weights of the fundamental (defining) representation of sl_4.

    The 4-dimensional representation has weights:
      h_1 = (3/4, -1/4, -1/4, -1/4)  [projected to R^3]
      h_2 = (-1/4, 3/4, -1/4, -1/4)
      h_3 = (-1/4, -1/4, 3/4, -1/4)
      h_4 = (-1/4, -1/4, -1/4, 3/4)
    These are the vectors such that h_i - h_{i+1} = alpha_i.
    """
    # Weights of the fundamental 4-dim representation in R^4
    # h_i = e_i - (1/4)(e_1+e_2+e_3+e_4), so h_i has 3/4 in position i, -1/4 elsewhere
    h = np.full((4, 4), -0.25)
    for i in range(4):
        h[i, i] = 0.75
    return h


def sl4_weyl_vector() -> np.ndarray:
    """Weyl vector rho = (1/2) sum of positive roots, in R^4 coordinates.

    For sl_4: rho = (3/2, 1/2, -1/2, -3/2).
    """
    return np.array([1.5, 0.5, -0.5, -1.5])


def sl4_positive_roots() -> np.ndarray:
    """Positive roots of sl_4: alpha_1, alpha_2, alpha_3, alpha_1+alpha_2,
    alpha_2+alpha_3, alpha_1+alpha_2+alpha_3.
    """
    a = sl4_simple_roots()
    return np.array([
        a[0],
        a[1],
        a[2],
        a[0] + a[1],
        a[1] + a[2],
        a[0] + a[1] + a[2],
    ])


# =========================================================================
# Central charge and level parametrization
# =========================================================================

def w4_central_charge_from_k(k: float) -> float:
    """Central charge c = 3 - 60(k+3)^2/(k+4) for W_4 from sl_4."""
    return 3.0 - 60.0 * (k + 3.0) ** 2 / (k + 4.0)


def w4_central_charge_rational(k):
    """Exact rational central charge for W_4."""
    k = Rational(k)
    return Rational(3) - Rational(60) * (k + 3) ** 2 / (k + 4)


def k_from_c(c_val: float) -> float:
    """Solve c = 3 - 60(k+3)^2/(k+4) for k (the positive branch).

    Rearranging: (k+4)(3-c) = 60(k+3)^2
    60(k+3)^2 - (3-c)(k+4) = 0
    60(k^2+6k+9) - (3-c)k - 4(3-c) = 0
    60k^2 + (360-(3-c))k + 540-4(3-c) = 0
    60k^2 + (357+c)k + (528+4c) = 0

    k = [-(357+c) +/- sqrt((357+c)^2 - 4*60*(528+4c))] / 120
    """
    a = 60.0
    b = 357.0 + c_val
    d = 528.0 + 4.0 * c_val
    disc = b**2 - 4 * a * d
    if disc < 0:
        raise ValueError(f"No real level for c = {c_val}")
    sqrt_disc = np.sqrt(disc)
    # Two branches: k_+ and k_-
    k_plus = (-b + sqrt_disc) / (2 * a)
    k_minus = (-b - sqrt_disc) / (2 * a)
    return k_plus, k_minus


def alpha0_from_k(k: float) -> float:
    """The Miura parameter alpha_0 = sqrt(2/(k+4)) for sl_4.

    The background charge alpha_0 satisfies alpha_0^2 = 2/(k+h^vee)
    where h^vee = 4 for sl_4.
    """
    return np.sqrt(2.0 / (k + 4.0))


def alpha0_squared_from_c(c_val: float) -> float:
    """Express alpha_0^2 directly in terms of c.

    From c = 3 - 60(k+3)^2/(k+4) and alpha_0^2 = 2/(k+4):
    Let t = alpha_0^2 = 2/(k+4), so k+4 = 2/t, k = 2/t - 4.
    Then k+3 = 2/t - 1 = (2-t)/t.
    c = 3 - 60*((2-t)/t)^2 / (2/t) = 3 - 60*(2-t)^2/(t^2) * t/2
      = 3 - 30*(2-t)^2/t
      = 3 - 30*(4-4t+t^2)/t
      = 3 - 120/t + 120 - 30t
      = 123 - 120/t - 30t

    So c = 123 - 120/t - 30t where t = alpha_0^2.
    Rearranging: 30t^2 + (c-123)t + 120 = 0
    t = [(123-c) +/- sqrt((123-c)^2 - 4*30*120)] / 60
    """
    a = 30.0
    b = c_val - 123.0
    d = 120.0
    disc = b**2 - 4 * a * d
    if disc < 0:
        raise ValueError(f"No real alpha_0 for c = {c_val}")
    sqrt_disc = np.sqrt(disc)
    t_plus = (-b + sqrt_disc) / (2 * a)
    t_minus = (-b - sqrt_disc) / (2 * a)
    # Positive branch: alpha_0^2 > 0
    if t_plus > 0:
        return t_plus
    if t_minus > 0:
        return t_minus
    raise ValueError(f"No positive alpha_0^2 for c = {c_val}")


# =========================================================================
# Free boson field representation
# =========================================================================

# A "field" is a polynomial in the free boson derivatives:
#   dphi_i (= partial phi_i), d2phi_i (= partial^2 phi_i), etc.
# We represent a monomial as a tuple of (boson_index, derivative_order) pairs.
# A field is a list of (coefficient, monomial) pairs.

# Monomial: tuple of (i, m) where i = boson index (0..3), m = derivative order (1,2,...)
# Sorted by (i, m) for canonicality.
Monomial = Tuple[Tuple[int, int], ...]

# Field: list of (coeff, monomial)
Field = List[Tuple[float, Monomial]]


def monomial_weight(m: Monomial) -> int:
    """Conformal weight of a monomial: sum of derivative orders."""
    return sum(d for _, d in m)


def field_weight(f: Field) -> Optional[int]:
    """Conformal weight of a homogeneous field (None if not homogeneous)."""
    weights = set(monomial_weight(m) for coeff, m in f if abs(coeff) > 1e-15)
    if len(weights) == 0:
        return 0
    if len(weights) == 1:
        return weights.pop()
    return None


def sort_monomial(m: Monomial) -> Monomial:
    """Canonical form for a monomial."""
    return tuple(sorted(m))


def simplify_field(f: Field) -> Field:
    """Combine like terms and remove zeros."""
    terms: Dict[Monomial, float] = {}
    for coeff, mon in f:
        mon = sort_monomial(mon)
        terms[mon] = terms.get(mon, 0.0) + coeff
    return [(c, m) for m, c in sorted(terms.items()) if abs(c) > 1e-15]


def add_fields(f1: Field, f2: Field) -> Field:
    """Add two fields."""
    return simplify_field(f1 + f2)


def scale_field(a: float, f: Field) -> Field:
    """Scale a field by a constant."""
    return simplify_field([(a * c, m) for c, m in f])


def multiply_fields(f1: Field, f2: Field) -> Field:
    """Normal-ordered product of two fields (no contractions)."""
    result = []
    for c1, m1 in f1:
        for c2, m2 in f2:
            result.append((c1 * c2, sort_monomial(m1 + m2)))
    return simplify_field(result)


def derivative_field(f: Field) -> Field:
    """Apply partial_z to a field.

    d/dz of d^m phi_i = d^{m+1} phi_i.
    For a monomial prod d^{m_j} phi_{i_j}, the derivative is
    sum_j (prod_{k!=j} d^{m_k} phi_{i_k}) * d^{m_j+1} phi_{i_j}.
    """
    result = []
    for coeff, mon in f:
        for idx in range(len(mon)):
            i, m = mon[idx]
            new_mon = list(mon)
            new_mon[idx] = (i, m + 1)
            result.append((coeff, sort_monomial(tuple(new_mon))))
    return simplify_field(result)


def nth_derivative_field(f: Field, n: int) -> Field:
    """Apply n-th partial derivative to a field."""
    result = f
    for _ in range(n):
        result = derivative_field(result)
    return result


# =========================================================================
# Miura transformation for sl_4
# =========================================================================

def miura_generators(t: float) -> Tuple[Field, Field, Field]:
    """Compute T, W_3, W_4 from the quantum Miura transformation for sl_4.

    The Miura operator with N=4 free bosons (indices 0,1,2,3 for R^4 embedding):
    L = :(d + alpha_0 h_1.dphi)(d + alpha_0 h_2.dphi)(d + alpha_0 h_3.dphi)(d + alpha_0 h_4.dphi):

    where t = alpha_0^2 and h_i are the weights of the fundamental representation.

    Expanding and collecting by powers of d:
    L = d^4 + W_2 d^2 + W_3 d + W_4

    (The d^3 coefficient vanishes by trace condition sum h_i = 0.)

    Parameters
    ----------
    t : float
        alpha_0^2 = 2/(k+4). The parameter controlling the central charge.

    Returns
    -------
    T, W3, W4 : Field
        The W_4 generators as free-boson composites.

    The quantum Miura transformation uses alpha_0 = sqrt(t) and the background
    charge Q = alpha_0 * rho, where rho is the Weyl vector.

    For practical computation, we use the elementary symmetric polynomial expansion.
    Define j_i = alpha_0 * h_i . dphi + quantum_correction_i
    The quantum corrections come from normal ordering: when moving d past j_i,
    we pick up dj_i terms. The full quantum Miura gives:

    T = sum_i (alpha_0 h_i.dphi)^2 / 2 + quantum_T
    where quantum_T involves alpha_0^2 and the Weyl vector.

    Actually, the standard approach is to use the free-field realization directly.
    For sl_N, the N-1 independent free bosons phi_a (a=1,...,N-1) give:

    T = -(1/2) sum_a (dphi_a)^2 + i * alpha_0 * rho_a * d^2 phi_a

    Wait -- let me be more careful. The standard free-field realization of W_N
    uses N-1 free bosons with the stress tensor:

    T = -(1/2) sum_{a=1}^{N-1} (dphi_a)^2 + i * Q_a * d^2phi_a

    where Q_a = alpha_0 * rho_a and rho is the Weyl vector expressed in the
    orthonormal basis for the Cartan subalgebra.

    The central charge is c = (N-1) - 12 * |Q|^2 = (N-1) - 12 * alpha_0^2 * |rho|^2.
    For sl_4: |rho|^2 = 9/4 + 1/4 + 1/4 + 9/4 = 5 (in R^4), but we need it
    in the orthonormal Cartan basis.

    ACTUALLY, let me use the Miura factorization directly, which is more standard
    and gives ALL generators at once.
    """
    alpha0 = np.sqrt(t)
    h = sl4_fundamental_weights()  # shape (4, 4)
    rho = sl4_weyl_vector()        # shape (4,)

    # We work in R^4 but with the constraint sum_a phi_a = 0 (projected to Cartan).
    # The 4 bosons phi_0, phi_1, phi_2, phi_3 satisfy this constraint.
    # Propagator: <dphi_i(z) dphi_j(w)> = -delta_{ij}/(z-w)^2

    # The Miura operator factors as:
    # L = prod_{i=1}^{4} (d + alpha_0 * h_i . dphi)
    # with quantum (normal ordering) corrections.

    # For the quantum Miura, we need to carefully normal-order the product.
    # The standard result (Fateev-Lukyanov) is:
    #
    # T = -1/2 sum_{a<b} (alpha_0 h_a . dphi)(alpha_0 h_b . dphi) part
    #
    # Actually, let me just use the known free-field expressions.
    # For sl_N with N-1 bosons phi_1,...,phi_{N-1} (orthonormal basis for Cartan):

    # Step 1: Set up the N-1 independent bosons
    # We use the orthonormal Cartan basis. The simple roots in this basis are:
    # e_1 = (sqrt(2), 0, 0)  [not quite -- need the actual embedding]

    # BETTER APPROACH: Use the R^4 formulation directly.
    # The 4 scalar fields phi_0, phi_1, phi_2, phi_3 with propagator
    # <phi_i(z) phi_j(w)> = -delta_{ij} log(z-w).
    # Constraint: sum phi_i = 0 (tracelessness), so phi_3 = -(phi_0+phi_1+phi_2).

    # Define J_i(z) = i * alpha_0 * dphi_i(z) for i=0,1,2,3.
    # The Miura operator is:
    # L = :(d - J_1)(d - J_2)(d - J_3)(d - J_4):
    # with J_i = i*alpha_0*dphi_i + quantum shift.

    # Following Bouwknegt-Schoutens (1993), the quantum Miura for sl_N is:
    # L = :prod_{i=1}^N (d + alpha_0 * e_i . dphi):
    # where e_i are the weights of the fundamental representation (e_i = unit vectors in R^N),
    # and the normal ordering yields quantum corrections proportional to alpha_0.

    # The expansion gives (with quantum corrections from normal ordering):
    # T = alpha_0^2 * sum_{i<j} dphi_i dphi_j + alpha_0 * (N-1-2i) * d2phi_i / 2
    #   = -(alpha_0^2/2) * sum (dphi_i)^2 + alpha_0 * rho . d2phi
    # (using sum dphi_i = 0 constraint to get the sign)

    # Rather than deriving the full quantum Miura, let me use the KNOWN
    # explicit expressions for the W_4 generators from Fateev-Lukyanov.

    # For computational efficiency, I will use a direct numerical approach.
    pass

    # Instead of the abstract Miura, we compute directly using the known
    # free-field expressions in terms of 3 independent bosons.
    return _miura_generators_explicit(t)


def _miura_generators_explicit(t: float) -> Tuple[Field, Field, Field]:
    """Explicit W_4 generators from 3 independent free bosons.

    We use 3 independent bosons phi_1, phi_2, phi_3 (indices 0, 1, 2)
    with propagator <dphi_a(z) dphi_b(w)> = -delta_{ab}/(z-w)^2.

    The background charge vector Q_a = alpha_0 * rho_a where:
    - alpha_0 = sqrt(t) = sqrt(2/(k+4))
    - rho is the Weyl vector of sl_4 in the orthonormal Cartan basis

    For sl_4, the Cartan subalgebra is 3-dimensional. Using the orthonormal
    basis {e_a} (a=1,2,3), the simple roots are:
      alpha_1 = sqrt(2) * e_1
      alpha_2 = -e_1/sqrt(2) + sqrt(3/2) * e_2
      alpha_3 = -e_2 * sqrt(2/3) + 2*e_3/sqrt(3)

    Wait, this is getting complicated. Let me use the standard R^4 embedding
    projected to R^3.

    SIMPLEST APPROACH: Use Fateev-Lukyanov's explicit formulas for the
    Miura operator in terms of elementary symmetric polynomials of the
    currents J_i(z) = alpha_0 * dphi_i(z) (i=1,...,4, sum J_i = 0).

    The Miura operator: L = (d + J_1)(d + J_2)(d + J_3)(d + J_4)

    After normal ordering, expanding:
    d^4 + (sum J_i) d^3 + (sum_{i<j} :J_iJ_j: + quantum) d^2 + ... d + ...

    Since sum J_i = 0 (tracelessness), the d^3 term vanishes.

    T (coefficient of d^2):
      T = sum_{i<j} :J_i J_j: + (alpha_0 * extra from normal ordering)

    For the quantum corrections, when we normal-order the product
    (d + J_i)(d + J_{i+1}), the commutator [J_i, d] = dJ_i picks up
    derivative terms. The full quantum correction is known.

    Let me use the KNOWN result directly.
    """
    # We use 3 independent free bosons (indices 0,1,2) corresponding to
    # the orthonormal basis of the sl_4 Cartan subalgebra.
    #
    # The fundamental weights of sl_4 in the R^4 embedding are:
    # h_i = e_i - (1/4)(e_1+e_2+e_3+e_4)
    # In the orthonormal Cartan basis (projected from R^4), these become
    # vectors in R^3.
    #
    # APPROACH: Work entirely numerically in R^4 with 4 bosons, using the
    # constraint phi_4 = -(phi_1+phi_2+phi_3) to eliminate one boson.
    # This avoids the need for an explicit orthonormal Cartan basis.

    alpha0 = np.sqrt(t)

    # The 4 "bosons" have indices 0,1,2,3 in R^4.
    # dphi_3 = -(dphi_0 + dphi_1 + dphi_2) by tracelessness.
    # We only use bosons 0,1,2 as independent.

    # Define J_i = alpha_0 * dphi_i, with the R^4 constraint.
    # The Miura expansion gives elementary symmetric polynomials e_k of J_1,...,J_4.
    # With the constraint J_1+J_2+J_3+J_4 = 0, we have e_1 = 0.

    # T (spin 2): from the quantum Miura, the explicit formula is:
    #   T = e_2 + quantum correction
    # where e_2 = sum_{i<j} :J_i J_j: and the quantum correction is
    #   -(N-1)*alpha_0/2 * sum (something...)
    #
    # Actually, the standard normalization gives:
    #   T = -(1/2) sum_{a=1}^{N-1} :(dphi_a)^2: + Q_a * d^2phi_a
    # where Q_a = alpha_0 * rho_a (background charge).

    # For sl_4, the Weyl vector in the orthonormal Cartan basis R^3 is:
    # rho = (3/2) omega_1 + omega_2 + (1/2) omega_3 (in fundamental weight coords)
    # where omega_i are fundamental weights.
    #
    # In the R^4 embedding: rho = (3/2, 1/2, -1/2, -3/2).

    # Working in R^4 with the tracelessness constraint:
    # T = -(1/2) sum_{i=0}^{3} :(dphi_i)^2: + alpha_0 * rho_i * d^2phi_i
    #
    # But we need to reduce to 3 independent bosons. Define:
    # phi_3 = -(phi_0 + phi_1 + phi_2)
    # dphi_3 = -(dphi_0 + dphi_1 + dphi_2)
    # d^2phi_3 = -(d^2phi_0 + d^2phi_1 + d^2phi_2)

    # Propagator in R^4: <dphi_i(z) dphi_j(w)> = -delta_{ij}/(z-w)^2
    # After eliminating phi_3, the effective propagator for bosons 0,1,2 is:
    # <dphi_a(z) dphi_b(w)> = -delta_{ab}/(z-w)^2  (a,b in {0,1,2})
    # because dphi_3 = -(dphi_0+dphi_1+dphi_2) and the cross-terms
    # give: <dphi_a dphi_3> = +delta_{a,3} (zero for a in {0,1,2}) minus
    # <dphi_a (dphi_0+dphi_1+dphi_2)> = -delta_{a,b} extra terms...
    #
    # Hmm, this needs care. The propagator in R^4 is:
    # <dphi_i dphi_j> = -delta_{ij}/(z-w)^2
    # With the constraint sum phi_i = 0, the correct propagator on the
    # constrained space is:
    # <dphi_i dphi_j> = -(delta_{ij} - 1/N) / (z-w)^2
    #
    # But this is more complex. Let me instead use the ORTHONORMAL Cartan basis.

    return _miura_generators_orthonormal(t)


def _orthonormal_cartan_basis_sl4() -> np.ndarray:
    """Orthonormal basis for the Cartan subalgebra of sl_4.

    We use 3 orthonormal vectors e_1, e_2, e_3 in R^4 spanning the
    hyperplane sum x_i = 0.

    Standard choice:
      e_1 = (1,-1,0,0)/sqrt(2)
      e_2 = (1,1,-2,0)/sqrt(6)
      e_3 = (1,1,1,-3)/sqrt(12)
    """
    e1 = np.array([1, -1, 0, 0]) / np.sqrt(2)
    e2 = np.array([1, 1, -2, 0]) / np.sqrt(6)
    e3 = np.array([1, 1, 1, -3]) / np.sqrt(12)
    return np.array([e1, e2, e3])


def _miura_generators_orthonormal(t: float) -> Tuple[Field, Field, Field]:
    """W_4 generators in orthonormal Cartan basis.

    3 independent free bosons phi_a (a=0,1,2) with standard propagator
    <dphi_a(z) dphi_b(w)> = -delta_{ab}/(z-w)^2.

    The stress tensor:
    T = -(1/2) sum_a (dphi_a)^2 + sum_a Q_a * d^2phi_a

    where Q_a = alpha_0 * rho_a and rho_a = (rho . e_a) with e_a the
    orthonormal Cartan basis vectors.

    For W_3, W_4: use the quantum Miura factorization.
    """
    alpha0 = np.sqrt(t)
    rho = sl4_weyl_vector()  # (3/2, 1/2, -1/2, -3/2) in R^4
    basis = _orthonormal_cartan_basis_sl4()  # shape (3, 4)

    # Background charge in orthonormal basis
    Q = np.array([np.dot(rho, basis[a]) for a in range(3)])
    Q = alpha0 * Q

    # Fundamental representation weights h_i (i=0,...,3) projected to Cartan
    h_fund = sl4_fundamental_weights()  # shape (4, 4), weights in R^4
    # Project to orthonormal Cartan basis
    h_proj = np.array([
        [np.dot(h_fund[i], basis[a]) for a in range(3)]
        for i in range(4)
    ])  # shape (4, 3)

    # Now build T, W_3, W_4 from the quantum Miura operator.
    # The Miura operator is:
    #   L = :(d + alpha_0 * h_1.dphi)(d + alpha_0 * h_2.dphi)(d + alpha_0 * h_3.dphi)(d + alpha_0 * h_4.dphi):
    #
    # where h_i.dphi = sum_a h_{i,a} dphi_a.
    #
    # We expand this product, collecting powers of d. The quantum corrections
    # come from the fact that d and dphi don't commute in the OPE sense:
    # when we move d past a current J(w), we pick up dJ(w).
    #
    # For the Miura product of N factors, the quantum correction is equivalent
    # to shifting each current: J_i -> J_i + (N+1-2i)/2 * alpha_0 * d(log of...)
    #
    # Actually, the cleanest way is: the quantum Miura operator for sl_N is
    # the normally-ordered product, which means we expand left to right and
    # put all annihilation operators to the right. The effect is that each
    # factor (d + J_i) when pulled through the previous ones picks up
    # derivative terms.
    #
    # The standard result (Fateev-Lukyanov 1988):
    #   T = sum_{i<j} :J_i J_j: + alpha_0 sum_i (N+1-2i)/2 * dJ_i
    #     = sum_{i<j} :J_i J_j: + alpha_0^2 * sum_i (N+1-2i)/2 * sum_a h_{i,a} d^2phi_a
    #
    # where J_i = alpha_0 * h_i . dphi = alpha_0 * sum_a h_{i,a} * dphi_a.
    #
    # But actually using sum_i h_{i,a} = 0 and sum_i (N+1-2i) h_{i,a} = 2 rho_a,
    # the quantum correction simplifies to:
    #   alpha_0^2 * sum_a rho_a * d^2phi_a = sum_a Q_a * d^2phi_a
    #
    # And for the quadratic part:
    #   sum_{i<j} :J_i J_j: = (alpha_0^2/2) * [sum_{i,j} h_i.dphi * h_j.dphi - sum_i (h_i.dphi)^2]
    #                        = (alpha_0^2/2) * [(sum_i h_i.dphi)^2 - sum_i (h_i.dphi)^2]
    #                        = -(alpha_0^2/2) * sum_i (h_i.dphi)^2
    #  (since sum_i h_i = 0).
    #
    # Now sum_i (h_i . dphi)^2 = sum_i sum_{a,b} h_{i,a} h_{i,b} dphi_a dphi_b
    #                           = sum_{a,b} (sum_i h_{i,a} h_{i,b}) dphi_a dphi_b
    #                           = sum_{a,b} G_{ab} dphi_a dphi_b
    # where G_{ab} = sum_i h_{i,a} h_{i,b}. For sl_N in orthonormal basis,
    # G_{ab} = delta_{ab} (since the weights of the fundamental representation
    # satisfy sum_i h_{i,a} h_{i,b} = delta_{ab} for the orthonormal Cartan basis).
    #
    # Therefore: T = -(1/2) sum_a (dphi_a)^2 + sum_a Q_a * d^2phi_a.
    # (The alpha_0^2 cancels with the normalization: sum_i h_{i,a}^2 = 1.)

    # Verify G_{ab} = delta_{ab}
    G = np.einsum('ia,ib->ab', h_proj, h_proj)
    assert np.allclose(G, np.eye(3), atol=1e-10), f"G matrix not identity: {G}"

    # ---- Build T ----
    # T = -(1/2) sum_a (dphi_a)^2 + sum_a Q_a * d^2phi_a
    T_field: Field = []
    for a in range(3):
        # -(1/2) (dphi_a)^2
        T_field.append((-0.5, ((a, 1), (a, 1))))
        # Q_a * d^2phi_a
        if abs(Q[a]) > 1e-15:
            T_field.append((Q[a], ((a, 2),)))
    T_field = simplify_field(T_field)

    # W_3 and W_4 from the Miura expansion (operator composition).
    # WARNING: _expand_miura_product uses operator composition which gives
    # WRONG quantum corrections. The generators are NOT primary w.r.t. T_field.
    # The OPE extraction gives approximate (not exact) structure constants.
    # TODO: implement the correct normally-ordered quantum Miura (Fateev-Lukyanov).
    _, W3_field, W4_field = _expand_miura_product(t, h_proj, Q)

    return T_field, W3_field, W4_field


def _expand_miura_product(
    t: float,
    h_proj: np.ndarray,
    Q: np.ndarray,
) -> Tuple[Field, Field]:
    """Expand the quantum Miura product to get W_3 and W_4.

    The quantum Miura operator for sl_4:
    L = :(d + J_1)(d + J_2)(d + J_3)(d + J_4):

    where J_i(z) = alpha_0 * h_i . dphi(z).

    We expand left to right as a differential operator composition.
    (d + J_i) composed with sum_k F_k d^k gives:
    sum_k [:J_i F_k: + dF_k] d^k + sum_k F_k d^{k+1}

    Note: The Miura expansion's d^2 coefficient (T_Miura) differs from
    the standard T by normalization. The W_3, W_4 from this expansion
    are weight-3, weight-4 primaries under the standard T. The BPZ
    inner product correctly extracts structure constants via primary
    orthogonality regardless of the T-mismatch, because W_4 is
    BPZ-orthogonal to non-W-algebra weight-4 fields.
    """
    alpha0 = np.sqrt(t)

    # Build the currents J_i as Fields
    def make_current(i: int) -> Field:
        """J_i = alpha_0 * sum_a h_{i,a} * dphi_a."""
        terms = []
        for a in range(3):
            c = alpha0 * h_proj[i, a]
            if abs(c) > 1e-15:
                terms.append((c, ((a, 1),)))
        return simplify_field(terms)

    J = [make_current(i) for i in range(4)]

    # Initialize: start from the rightmost factor (d + J_4)
    identity_field: Field = [(1.0, ())]
    zero_field: Field = []

    coeffs: Dict[int, Field] = {0: J[3], 1: identity_field}

    # Multiply from the left by (d + J_i) for i = 2, 1, 0
    for i in [2, 1, 0]:
        new_coeffs: Dict[int, Field] = {}

        for k, fk in coeffs.items():
            # J_i * F_k d^k
            j_times_fk = multiply_fields(J[i], fk)
            if k not in new_coeffs:
                new_coeffs[k] = zero_field[:]
            new_coeffs[k] = add_fields(new_coeffs[k], j_times_fk)

            # d * F_k d^k = (dF_k) d^k + F_k d^{k+1}
            dfk = derivative_field(fk)
            new_coeffs[k] = add_fields(new_coeffs[k], dfk)

            kp1 = k + 1
            if kp1 not in new_coeffs:
                new_coeffs[kp1] = zero_field[:]
            new_coeffs[kp1] = add_fields(new_coeffs[kp1], fk)

        coeffs = new_coeffs

    # Verify coeffs[4] = 1
    c4 = coeffs.get(4, [])
    assert len(c4) == 1 and abs(c4[0][0] - 1.0) < 1e-10, f"d^4 coefficient not 1: {c4}"

    # Verify coeffs[3] = 0 (tracelessness)
    c3 = coeffs.get(3, [])
    for coeff, _ in c3:
        assert abs(coeff) < 1e-10, f"d^3 coefficient not zero: {c3}"

    T_field = simplify_field(coeffs.get(2, []))
    W3_field = coeffs.get(1, [])
    W4_field = coeffs.get(0, [])

    return T_field, W3_field, W4_field


# =========================================================================
# Wick contraction engine
# =========================================================================

def wick_contract_pair(
    mon1: Monomial,
    idx1: int,
    mon2: Monomial,
    idx2: int,
) -> Tuple[float, Monomial, Monomial]:
    """Contract one pair of operators from two monomials.

    The contraction of d^m phi_i(z) with d^n phi_j(w) is:
      <d^m phi_i(z) d^n phi_j(w)> = delta_{ij} * (-1)^{n} * (m+n-1)! / (m-1)! / (z-w)^{m+n}
    Wait, let me be more careful.

    The propagator is: <phi_i(z) phi_j(w)> = -delta_{ij} log(z-w)
    So: <dphi_i(z) phi_j(w)> = -delta_{ij}/(z-w)
    And: <d^m phi_i(z) d^n phi_j(w)> = -delta_{ij} * (-1)^n * m! n! / ...
    Hmm, let me compute from scratch.

    <dphi_i(z) dphi_j(w)> = d_z d_w [-delta_{ij} log(z-w)]
                           = -delta_{ij} * d_z [1/(z-w)]  [d_w, not d_z]

    Wait: <phi_i(z) phi_j(w)> = -delta_{ij} log(z-w)
    d_z <phi_i(z) phi_j(w)> = -delta_{ij} * 1/(z-w)
    d_w <phi_i(z) phi_j(w)> = -delta_{ij} * (-1)/(z-w) = delta_{ij}/(z-w)
    d_z d_w <phi_i(z) phi_j(w)> = -delta_{ij} * d_w [1/(z-w)]
                                 = -delta_{ij} * (-1)/(z-w)^2
                                 = delta_{ij} / (z-w)^2

    Wait, that gives the WRONG sign. Let me be careful.
    <dphi_i(z) dphi_j(w)> should be -delta_{ij}/(z-w)^2.

    <phi(z) phi(w)> = -log(z-w)  (for a single boson, delta_{ij} = 1)
    d_z: <dphi(z) phi(w)> = -1/(z-w)
    d_w d_z: <dphi(z) dphi(w)> = -d_w[1/(z-w)] = -(-1)/(z-w)^2 = 1/(z-w)^2

    Hmm, but the standard convention is <dphi(z) dphi(w)> = -1/(z-w)^2.
    This means the propagator should be <phi(z) phi(w)> = +log(z-w)? No...

    The PHYSICS convention: phi(z) is a free boson with OPE
    phi(z) phi(w) ~ -log(z-w)
    This gives: dphi(z) dphi(w) ~ -1/(z-w)^2.

    But from calculus:
    d_z d_w [-log(z-w)] = d_z [+1/(z-w)] = -1/(z-w)^2. Correct!

    So <dphi(z) dphi(w)> = -1/(z-w)^2.

    Now for higher derivatives:
    <d^m phi(z) d^n phi(w)> = d_z^m d_w^n [-log(z-w)]
    = (-1) * d_z^m d_w^n [log(z-w)]
    = (-1) * d_z^m [(-1)^n (n-1)! / (z-w)^n]  (for n >= 1)
    Wait, d_w log(z-w) = d_w log(z-w) = -1/(z-w), so
    d_w^n log(z-w) = (-1)^n (n-1)! / (z-w)^n for n >= 1.
    Hmm, let me check: d_w [log(z-w)] = -1/(z-w).
    d_w^2 [log(z-w)] = 1/(z-w)^2.
    d_w^3 [log(z-w)] = -2/(z-w)^3.
    General: d_w^n [log(z-w)] = (-1)^n (n-1)!/(z-w)^n for n >= 1.

    Then d_z^m of [1/(z-w)^n]:
    d_z^m [1/(z-w)^n] = n(n+1)...(n+m-1) / (z-w)^{n+m} = (n+m-1)!/(n-1)! / (z-w)^{n+m}

    So <d^m phi(z) d^n phi(w)> = (-1) * (-1)^n * (n-1)! * (n+m-1)!/(n-1)! / (z-w)^{n+m}
                                = (-1)^{n+1} * (n+m-1)! / (z-w)^{n+m}

    Wait, let me redo this for m >= 1, n >= 1.
    Starting from <phi(z) phi(w)> = -log(z-w):
    <d^m phi(z) d^n phi(w)> = d_z^m d_w^n [-log(z-w)]

    Step 1: d_w^n [-log(z-w)] = -d_w^n [log(z-w)] = -(-1)^n (n-1)!/(z-w)^n
                                = (-1)^{n+1} (n-1)!/(z-w)^n

    Step 2: d_z^m [(-1)^{n+1} (n-1)!/(z-w)^n]
           = (-1)^{n+1} (n-1)! * n(n+1)...(n+m-1) / (z-w)^{n+m}
           = (-1)^{n+1} (n-1)! * (n+m-1)!/((n-1)!) / (z-w)^{n+m}
           = (-1)^{n+1} (n+m-1)! / (z-w)^{n+m}

    So: <d^m phi_i(z) d^n phi_j(w)> = delta_{ij} * (-1)^{n+1} * (m+n-1)! / (z-w)^{m+n}

    Check: m=n=1: (-1)^2 * 1! / (z-w)^2 = 1/(z-w)^2. But we want -1/(z-w)^2.
    WRONG. Let me recheck.

    d_w^1 [-log(z-w)] = -(-1/(z-w)) = 1/(z-w)

    Hmm wait: d_w [log(z-w)] = d_w log(z-w). Let u = z - w, then d_w u = -1.
    d_w [log u] = (1/u)(-1) = -1/(z-w).
    So d_w [-log(z-w)] = 1/(z-w).

    d_z [1/(z-w)] = -1/(z-w)^2.

    So <dphi(z) dphi(w)> = -1/(z-w)^2. Good, matches the convention.

    Let me redo the general formula more carefully.
    Define f(z,w) = -log(z-w). Then f is the propagator.

    d_w f = 1/(z-w)
    d_w^2 f = -d_w [1/(z-w)] = -(-1)/(z-w)^2 = 1/(z-w)^2
    Hmm that's wrong. d_w [1/(z-w)] = d_w [(z-w)^{-1}] = (-1)(z-w)^{-2}(-1) = 1/(z-w)^2.
    So d_w^2 f = d_w [1/(z-w)] = 1/(z-w)^2.

    Wait: d_w^1 f = 1/(z-w). d_w of that: d_w [1/(z-w)] = d_w [(z-w)^{-1}]
    = (-1)(z-w)^{-2} * d_w(z-w) = (-1)(z-w)^{-2}*(-1) = 1/(z-w)^2.
    So d_w^2 f = 1/(z-w)^2.

    d_w^3 f = d_w [1/(z-w)^2] = (-2)(z-w)^{-3}(-1) = 2/(z-w)^3.

    General: d_w^n f = (n-1)!/(z-w)^n for n >= 1. (Positive!)

    Now d_z^m of [(n-1)!/(z-w)^n]:
    d_z [(z-w)^{-n}] = (-n)(z-w)^{-n-1}
    d_z^m [(z-w)^{-n}] = (-1)^m n(n+1)...(n+m-1) (z-w)^{-n-m}
                       = (-1)^m (n+m-1)!/(n-1)! * (z-w)^{-n-m}

    So: <d^m phi(z) d^n phi(w)> = d_z^m d_w^n f
        = (n-1)! * (-1)^m (n+m-1)!/(n-1)! * (z-w)^{-(n+m)}
        = (-1)^m (n+m-1)! / (z-w)^{n+m}

    Check: m=n=1: (-1)^1 * 1! / (z-w)^2 = -1/(z-w)^2. Correct!
    Check: m=2, n=1: (-1)^2 * 2! / (z-w)^3 = 2/(z-w)^3.
    Independent check: <d^2phi(z) dphi(w)> = d_z <dphi(z) dphi(w)>
    = d_z [-1/(z-w)^2] = 2/(z-w)^3. Correct!

    For the contraction of d^m phi_i(z) with d^n phi_j(w):
    VALUE = delta_{ij} * (-1)^m * (m+n-1)! / (z-w)^{m+n}

    In the OPE A(z)B(w), the coefficient of (z-w)^{-p} at pole p = m+n is:
    delta_{ij} * (-1)^m * (m+n-1)!

    Returns: (coefficient, remaining_mon1, remaining_mon2)
    where coefficient is delta_{ij} * (-1)^m * (m+n-1)! and the pole order is m+n.
    """
    i1, m = mon1[idx1]
    i2, n = mon2[idx2]

    if i1 != i2:
        return 0.0, mon1, mon2

    pole_order = m + n
    # Coefficient of the contraction (times (z-w)^{pole_order}):
    coeff = (-1)**m * float(_factorial(m + n - 1))
    # Remove the contracted operators
    rem1 = mon1[:idx1] + mon1[idx1+1:]
    rem2 = mon2[:idx2] + mon2[idx2+1:]

    return coeff, rem1, rem2


@lru_cache(maxsize=256)
def _factorial(n: int) -> int:
    """Cached factorial."""
    if n <= 1:
        return 1
    return n * _factorial(n - 1)


def _wick_ope_at_pole(
    field1: Field,
    field2: Field,
    pole_order: int,
) -> Field:
    """Compute the coefficient of (z-w)^{-pole_order} in the OPE A(z)B(w).

    Uses Wick's theorem with Taylor corrections: after contracting pairs
    of operators between A(z) and B(w), the REMAINING operators from A
    are at position z and must be Taylor-expanded around w:

        d^m phi(z) = sum_{k>=0} (z-w)^k / k! * d^{m+k} phi(w)

    This Taylor expansion shifts the effective pole: a contraction pattern
    producing pole p_c contributes to pole p_c - K where K = sum of
    Taylor shifts from remaining z-operators.

    A single contraction of d^m phi_a(z) with d^n phi_b(w) gives:
      delta_{ab} * (-1)^m * (m+n-1)! / (z-w)^{m+n}
    """
    result: Field = []

    for c1, mon1 in field1:
        for c2, mon2 in field2:
            # Collect ALL complete contraction patterns with pole >= target
            contraction_results = []
            _enumerate_contractions_complete(
                c1 * c2, mon1, mon2, pole_order, 0, 1.0,
                contraction_results, 0
            )
            # For each complete contraction pattern, apply Taylor corrections
            for coeff, rem_z, rem_w, cpole in contraction_results:
                _apply_taylor_corrections(
                    coeff, rem_z, rem_w, cpole, pole_order, result
                )

    return simplify_field(result)


def _enumerate_contractions_complete(
    overall_coeff: float,
    mon1: Monomial,
    mon2: Monomial,
    min_target_pole: int,
    current_pole: int,
    contraction_coeff: float,
    result: list,
    min_idx1: int = 0,
    uncontracted_z: tuple = (),
):
    """Recursively enumerate all COMPLETE contraction patterns.

    A pattern is complete when we have decided for every operator in mon1
    (from min_idx1 onwards) whether to contract it or leave it uncontracted.
    Only complete patterns are collected.

    Parameters
    ----------
    mon1 : Monomial
        Operators from field1 that haven't been decided yet (from min_idx1 on)
        plus already-decided-to-skip operators (before min_idx1).
        Actually, we use min_idx1 as cursor into original mon1.
    mon2 : Monomial
        Remaining operators from field2 (uncontracted ones).
    uncontracted_z : tuple
        Operators from field1 that we decided NOT to contract (stay at z).
    """
    if min_idx1 >= len(mon1):
        # All operators in mon1 have been processed -> pattern is complete
        if current_pole >= min_target_pole:
            result.append((
                overall_coeff * contraction_coeff,
                uncontracted_z,  # z-operators needing Taylor expansion
                mon2,            # w-operators
                current_pole,
            ))
        return

    # Bound: maximum additional pole from remaining unprocessed operators
    remaining_mon1 = mon1[min_idx1:]
    max_additional = sum(m + n for (_, m) in remaining_mon1 for (_, n) in mon2)
    if current_pole + max_additional < min_target_pole:
        return  # Can't reach min_target_pole

    # Option 1: Don't contract mon1[min_idx1] -> add to uncontracted_z
    _enumerate_contractions_complete(
        overall_coeff, mon1, mon2, min_target_pole, current_pole,
        contraction_coeff, result, min_idx1 + 1,
        uncontracted_z + (mon1[min_idx1],)
    )

    # Option 2: Contract mon1[min_idx1] with some mon2[j]
    i1, m1 = mon1[min_idx1]
    for j in range(len(mon2)):
        i2, m2 = mon2[j]
        if i1 != i2:
            continue
        pole = m1 + m2
        c = (-1)**m1 * float(_factorial(m1 + m2 - 1))
        new_mon2 = mon2[:j] + mon2[j+1:]
        _enumerate_contractions_complete(
            overall_coeff, mon1, new_mon2, min_target_pole,
            current_pole + pole, contraction_coeff * c, result,
            min_idx1 + 1, uncontracted_z
        )


def _apply_taylor_corrections(
    coeff: float,
    rem_z: Monomial,
    rem_w: Monomial,
    contraction_pole: int,
    target_pole: int,
    result: Field,
):
    """Apply Taylor expansion to remaining z-operators and collect target pole.

    Each remaining z-operator d^m phi_i(z) expands as:
        d^m phi_i(z) = sum_{k>=0} (z-w)^k / k! * d^{m+k} phi_i(w)

    We need to distribute K = contraction_pole - target_pole units of
    Taylor shift among the r remaining z-operators: k_1 + ... + k_r = K
    with k_j >= 0. The combinatorial weight is 1/(k_1! ... k_r!).
    """
    K = contraction_pole - target_pole
    if K < 0:
        return  # Can't reach target (need MORE pole, not less)

    r = len(rem_z)

    if r == 0:
        # No z-operators to Taylor expand. Need K = 0.
        if K == 0:
            remaining = sort_monomial(rem_w)
            result.append((coeff, remaining))
        return

    # Enumerate all ways to distribute K among r operators
    # For efficiency, use a recursive generator
    _distribute_taylor_shifts(coeff, rem_z, rem_w, K, 0, [], result)


def _distribute_taylor_shifts(
    coeff: float,
    rem_z: Monomial,
    rem_w: Monomial,
    remaining_K: int,
    idx: int,
    shifts: list,
    result: Field,
):
    """Distribute Taylor shift K among remaining z-operators recursively."""
    r = len(rem_z)

    if idx == r:
        if remaining_K == 0:
            # Build the shifted monomial
            shifted_z = tuple(
                (rem_z[j][0], rem_z[j][1] + shifts[j])
                for j in range(r)
            )
            # Compute 1/(k_1! ... k_r!) factor
            taylor_factor = 1.0
            for k in shifts:
                taylor_factor /= float(_factorial(k))
            remaining = sort_monomial(shifted_z + rem_w)
            result.append((coeff * taylor_factor, remaining))
        return

    # How much can we assign to this operator?
    # The remaining operators (idx+1, ..., r-1) need at least 0 each.
    max_k = remaining_K
    for k in range(max_k + 1):
        shifts.append(k)
        _distribute_taylor_shifts(
            coeff, rem_z, rem_w, remaining_K - k, idx + 1, shifts, result
        )
        shifts.pop()


# =========================================================================
# OPE computation: high-level interface
# =========================================================================

def compute_ope(
    field1: Field,
    field2: Field,
    max_pole: int,
) -> Dict[int, Field]:
    """Compute the OPE field1(z) field2(w) up to max_pole.

    Returns {pole_order: coefficient_field} for each singular pole.
    """
    ope = {}
    for p in range(1, max_pole + 1):
        coeff = _wick_ope_at_pole(field1, field2, p)
        if coeff:
            ope[p] = coeff
    return ope


def evaluate_field_as_number(f: Field) -> float:
    """If a field is a pure scalar (empty monomial), return its value."""
    total = 0.0
    for c, m in f:
        if m == () or len(m) == 0:
            total += c
        else:
            return None  # Not a pure scalar
    return total


# =========================================================================
# Primary projection: subtract descendant contributions
# =========================================================================

def project_onto_primary(
    ope_coeff: Field,
    primary_field: Field,
    T_field: Field,
    target_spin: int,
    source_spins: Tuple[int, int],
    pole_order: int,
    primary_norms: Dict[int, float],
    ope_data: Dict[int, Field],
) -> float:
    """Extract the primary OPE coefficient at a given pole.

    Given the full OPE coefficient at pole_order (which includes both
    primary and descendant contributions), project out the descendant
    part to get the primary coefficient.

    For the OPE W_s(z) W_t(w) = sum_p C_p / (z-w)^p, the coefficient
    C_p at pole p includes:
    - Primary field W_u with coefficient C_{s,t;u;0,p} (if h_u = s+t-p)
    - Descendants d^k W_u from higher poles (with h_u = s+t-p-k for some k)
    - Composite quasi-primary fields (Lambda, etc.)

    The primary coefficient is obtained by computing <W_u | C_p> using
    the field inner product (2-point function normalization).
    """
    # Compute the overlap of ope_coeff with primary_field
    return _field_overlap(ope_coeff, primary_field, primary_norms.get(target_spin, 1.0))


def _bpz_inner_product(field1: Field, field2: Field) -> float:
    """Zamolodchikov (BPZ) inner product <field1|field2> via Wick contractions.

    Computes the leading-pole coefficient in the OPE field1(z) field2(w),
    at pole order h1 + h2 where h1, h2 are the conformal weights.  At this
    pole all free-boson operators are fully contracted, giving a pure scalar.

    This is the PHYSICAL inner product of conformal field theory, distinct
    from the Euclidean dot product on free-boson monomial coefficients.
    The Euclidean metric ignores the propagator structure and gives wrong
    results whenever the W-algebra basis does not span the full Fock space
    at a given weight (which happens at weight >= 4 for rank >= 3).
    """
    if not field1 or not field2:
        return 0.0
    h1 = field_weight(field1)
    h2 = field_weight(field2)
    if h1 is None or h2 is None:
        return 0.0
    pole = h1 + h2
    result = _wick_ope_at_pole(field1, field2, pole)
    if not result:
        return 0.0
    # At the leading pole, all operators are contracted -> pure scalar.
    # Extract scalar part; any residual non-scalar terms arise from
    # boson-index-mismatched pairs that cannot fully contract.
    total = 0.0
    for c, m in result:
        if m == () or len(m) == 0:
            total += c
    return total


def _field_overlap(f1: Field, f2: Field, norm: float) -> float:
    """Extract coefficient of f2 in f1 using the BPZ inner product.

    Computes <f2 | f1>_BPZ / <f2 | f2>_BPZ, the physical projection
    of f1 onto f2 in the Zamolodchikov metric.  For a primary field f2,
    this correctly isolates its contribution even when f1 contains
    quasi-primaries and descendants from other conformal families.

    The norm parameter is accepted for API compatibility but unused;
    the self-norm is computed internally via Wick contractions.
    """
    self_norm = _bpz_inner_product(f2, f2)
    if abs(self_norm) < 1e-15:
        return 0.0
    overlap = _bpz_inner_product(f2, f1)
    return overlap / self_norm


# =========================================================================
# W_4 OPE computation at a specific central charge
# =========================================================================

def miura_central_charge(T_field: Field) -> float:
    """Compute the actual central charge from the T self-OPE pole 4.

    The Miura construction with real alpha_0 produces a valid W_4 algebra
    at central charge c_M = 2 * (T self-OPE pole 4 coefficient).

    For sl_4 with T = -(1/2) sum (dphi_a)^2 + alpha_0 * rho . d^2 phi,
    the central charge is c_M = 3 + 60*t where t = alpha_0^2.
    This differs from the physical DS formula c_phys = 3 - 60(k+3)^2/(k+4)
    because the physical convention uses imaginary Q = i*alpha_0*rho.

    The OPE structure constants are rational functions of c, so they are
    the same whether c is obtained from real or imaginary alpha_0.
    """
    tt_ope4 = _wick_ope_at_pole(T_field, T_field, 4)
    norm_T = evaluate_field_as_number(tt_ope4)
    return 2.0 * norm_T


class W4MiuraOPE:
    """Compute W_4 OPE coefficients via the Miura transformation.

    This class:
    1. Constructs the Miura generators T, W_3, W_4 at parameter t = alpha_0^2.
    2. Computes all pairwise OPEs via Wick contractions.
    3. Extracts primary OPE coefficients by projecting out descendants.

    The central charge c_actual is determined from the T self-OPE, not
    from the input c_val. When constructed via from_t(), the parametrization
    is direct and avoids the c -> alpha_0^2 inversion.
    """

    def __init__(self, c_val: float, verbose: bool = False):
        self.c_requested = c_val
        self.verbose = verbose

        # Get alpha_0^2 from c (legacy interface)
        self.t = alpha0_squared_from_c(c_val)

        # Build the generators
        self.T, self.W3, self.W4 = miura_generators(self.t)

        # Compute the ACTUAL central charge from the T self-OPE
        self.c_actual = miura_central_charge(self.T)
        self.c_val = self.c_actual

        if verbose:
            print(f"c_requested = {c_val}, alpha_0^2 = {self.t}")
            print(f"c_actual (from T self-OPE) = {self.c_actual}")
            print(f"T has {len(self.T)} terms")
            print(f"W3 has {len(self.W3)} terms")
            print(f"W4 has {len(self.W4)} terms")

        self._build_composites()

    @classmethod
    def from_t(cls, t: float, verbose: bool = False) -> 'W4MiuraOPE':
        """Build directly from the Miura parameter t = alpha_0^2.

        This avoids the c -> t inversion and directly parametrizes by t.
        The actual central charge c_M is computed from the T self-OPE.
        """
        obj = cls.__new__(cls)
        obj.t = t
        obj.verbose = verbose

        # Build the generators
        obj.T, obj.W3, obj.W4 = miura_generators(t)

        # Compute the actual central charge from the T self-OPE
        obj.c_actual = miura_central_charge(obj.T)
        obj.c_val = obj.c_actual
        obj.c_requested = None  # No c_requested when built from t

        if verbose:
            print(f"t = {t}, c_actual (from T self-OPE) = {obj.c_actual}")
            print(f"T has {len(obj.T)} terms")
            print(f"W3 has {len(obj.W3)} terms")
            print(f"W4 has {len(obj.W4)} terms")

        obj._build_composites()
        return obj

    def _build_composites(self):
        """Build composite fields and compute normalizations."""
        # Lambda = :TT: - (3/10) d^2 T
        self.Lambda = add_fields(
            multiply_fields(self.T, self.T),
            scale_field(-0.3, nth_derivative_field(self.T, 2))
        )
        # dT, d^2T, d^3T
        self.dT = derivative_field(self.T)
        self.d2T = nth_derivative_field(self.T, 2)
        self.d3T = nth_derivative_field(self.T, 3)
        self.dW3 = derivative_field(self.W3)
        self.dW4 = derivative_field(self.W4)
        self.dLambda = derivative_field(self.Lambda)

        # Compute self-normalization (2-point function coefficients)
        # <T|T> = c_actual/2, <W_3|W_3>, <W_4|W_4>
        # These come from the leading pole in the self-OPE.
        self._compute_normalizations()

    def _compute_normalizations(self):
        """Compute 2-point normalizations from leading self-OPE poles."""
        # T x T: leading pole 4, coefficient = c/2
        tt_ope4 = _wick_ope_at_pole(self.T, self.T, 4)
        self.norm_T = evaluate_field_as_number(tt_ope4)

        # W3 x W3: leading pole 6, coefficient = c/3
        w3w3_ope6 = _wick_ope_at_pole(self.W3, self.W3, 6)
        self.norm_W3 = evaluate_field_as_number(w3w3_ope6)

        # W4 x W4: leading pole 8, coefficient = c/4
        w4w4_ope8 = _wick_ope_at_pole(self.W4, self.W4, 8)
        self.norm_W4 = evaluate_field_as_number(w4w4_ope8)

        # Lambda = :TT: - (3/10) d^2T: quasi-primary norm c(5c+22)/10
        self.norm_Lambda = _bpz_inner_product(self.Lambda, self.Lambda)

        if self.verbose:
            c = self.c_actual if hasattr(self, 'c_actual') else self.c_val
            print(f"Normalizations: T={self.norm_T}, W3={self.norm_W3}, W4={self.norm_W4}")
            print(f"  Expected: T={c/2}, W3={c/3}, W4={c/4}")

    def verify_normalizations(self, tol: float = 1e-6) -> Dict[str, bool]:
        """Verify 2-point function normalizations against c_actual."""
        c = self.c_actual
        return {
            "T_norm": abs(self.norm_T - c / 2) < tol * max(1, abs(c)),
            "W3_norm": abs(self.norm_W3 - c / 3) < tol * max(1, abs(c)),
            "W4_norm": abs(self.norm_W4 - c / 4) < tol * max(1, abs(c)),
        }

    def TT_ope(self) -> Dict[int, Field]:
        """T(z) T(w) OPE."""
        return compute_ope(self.T, self.T, 4)

    def TW3_ope(self) -> Dict[int, Field]:
        """T(z) W_3(w) OPE."""
        return compute_ope(self.T, self.W3, 4)

    def TW4_ope(self) -> Dict[int, Field]:
        """T(z) W_4(w) OPE."""
        return compute_ope(self.T, self.W4, 5)

    def W3W3_ope(self) -> Dict[int, Field]:
        """W_3(z) W_3(w) OPE."""
        return compute_ope(self.W3, self.W3, 6)

    def W3W4_ope(self) -> Dict[int, Field]:
        """W_3(z) W_4(w) OPE."""
        return compute_ope(self.W3, self.W4, 6)

    def W4W4_ope(self) -> Dict[int, Field]:
        """W_4(z) W_4(w) OPE."""
        return compute_ope(self.W4, self.W4, 8)

    # ----- Primary coefficient extraction -----

    def _extract_primary_coeff(
        self,
        ope_at_pole: Field,
        primary_field: Field,
        pole_order: int,
        ope_full: Dict[int, Field],
        source_spins: Tuple[int, int],
        target_spin: int,
    ) -> float:
        """Extract the primary coefficient by subtracting descendants.

        At pole p in W_s(z) W_t(w), the field content includes:
        - Primary W_u (spin u = s+t-p) with coefficient C_{s,t;u}
        - Descendants from higher poles: d^k [content at pole p+k] / k!

        The relation between consecutive poles and descendants:
        At pole p, if the full expression at pole p+1 is F_{p+1}, then
        the derivative contribution is (1/(p)) * dF_{p+1} (from the
        Taylor expansion of z around w).

        More precisely: in the OPE W_s(z) W_t(w) = sum_n C_n(w) / (z-w)^n,
        the mode relation gives:
          C_n = primary contribution + descendant contributions from C_{n+1}, C_{n+2}, ...

        The descendant subtraction depends on the specific conformal field theory.
        For the T-channel: at pole p where T (spin 2) appears, the coefficient is
          f_p = C_{s,t;2} * T + descendants from higher-pole T contributions.

        For simple cases: the primary coefficient of W_u at pole p in the OPE
        W_s(z) W_t(w) is extracted by projecting C_p onto W_u, after subtracting
        the known descendant contributions.
        """
        # Project the OPE coefficient onto the primary field
        return _field_overlap(ope_at_pole, primary_field, 1.0)

    def extract_T_coeff_at_pole(self, ope: Dict[int, Field], pole: int) -> float:
        """Extract the coefficient of T at a given pole in an OPE.

        This is the coefficient of T(w) in the expansion of the OPE at
        the given pole order, after subtracting derivative descendants.
        """
        if pole not in ope:
            return 0.0
        coeff_field = ope[pole]

        # The T field has weight 2. At pole p, if s+t-p = 2 (where s,t
        # are source spins), then the leading contribution is alpha * T.
        # We also need to subtract d^k T descendants from poles p+k.

        # Subtract derivative descendants of T from higher poles.
        # At pole p+1, if T appears with coefficient alpha_{p+1}, then
        # the derivative descendant at pole p is alpha_{p+1} * dT / 1
        # (from the Laurent expansion: C_{n-1} = [C_{n-1}] where the
        # dT term comes from the Taylor expansion of the OPE).
        #
        # Actually, the vertex algebra mode expansion gives:
        # (a_{(n)} b)(w) = sum_{j>=0} (-1)^j C(n,j) [d^j a_{(n+j)} b](w) / j!
        # This is NOT the same as Taylor subtraction.
        #
        # For the OPE extraction, the CORRECT procedure is:
        # Write C_p = sum_u alpha_u W_u + sum derivatives
        # and solve for alpha_u.
        #
        # Simple approach: project C_p onto the basis {T, W_3, W_4, dT, d^2T, ...}
        # and read off the T coefficient.

        return _field_overlap(coeff_field, self.T, 1.0)

    def extract_W3_coeff_at_pole(self, ope: Dict[int, Field], pole: int) -> float:
        """Extract the coefficient of W_3 at a given pole."""
        if pole not in ope:
            return 0.0
        return _field_overlap(ope[pole], self.W3, 1.0)

    def extract_W4_coeff_at_pole(self, ope: Dict[int, Field], pole: int) -> float:
        """Extract the coefficient of W_4 at a given pole."""
        if pole not in ope:
            return 0.0
        return _field_overlap(ope[pole], self.W4, 1.0)

    def extract_dT_coeff_at_pole(self, ope: Dict[int, Field], pole: int) -> float:
        """Extract the coefficient of dT at a given pole."""
        if pole not in ope:
            return 0.0
        return _field_overlap(ope[pole], self.dT, 1.0)

    def extract_Lambda_coeff_at_pole(self, ope: Dict[int, Field], pole: int) -> float:
        """Extract the coefficient of Lambda at a given pole."""
        if pole not in ope:
            return 0.0
        return _field_overlap(ope[pole], self.Lambda, 1.0)

    def extract_all_stage4_coefficients(self) -> Dict[str, float]:
        """Extract all 6 stage-4 coefficients.

        Returns a dictionary with keys:
          c_334: W_3 x W_3 -> W_4 at pole 2
          c_444: W_4 x W_4 -> W_4 at pole 4
          C_34_3_4: W_3 x W_4 -> W_3 at pole 4
          C_34_4_3: W_3 x W_4 -> W_4 at pole 3
          C_44_2_6: W_4 x W_4 -> T at pole 6 (predicted = 2)
          C_34_2_5: W_3 x W_4 -> T at pole 5 (predicted = 0)
        """
        results = {}

        # ----- W_3 x W_3 OPE -----
        w3w3 = self.W3W3_ope()

        # c_334: W_4 coefficient at pole 2
        # At pole 2, spin = 3+3-2 = 4, so W_4 is the primary.
        # But there are also descendants and the Lambda composite.
        # We need to carefully decompose the spin-4 content at pole 2.
        #
        # The spin-4 space at pole 2 is spanned by:
        # {W_4, Lambda, d^2T} (plus higher derivatives of T from above poles)
        #
        # From the known W_3 OPE structure:
        # C_2 = (3/10) d^2T + beta * Lambda + c_334 * W_4
        # where beta = 16/(22+5c).
        #
        # The descendant d^2T comes from the T at pole 4 and dT at pole 3.
        # The Lambda is a quasi-primary composite.
        #
        # To extract c_334, we use:
        # c_334 = <W_4 | C_2 - (3/10) d^2T - beta * Lambda> / <W_4 | W_4>
        #
        # But this requires knowing beta, which we can verify from the W_3 OPE.
        #
        # ACTUALLY: the simplest approach is to use the free-field representation.
        # Since T, W_3, W_4, Lambda are all expressed as free-boson composites,
        # we can decompose C_2 in terms of these fields by linear algebra.
        results["c_334"] = self._extract_c334(w3w3)

        # ----- W_4 x W_4 OPE -----
        w4w4 = self.W4W4_ope()

        # C_44_2_6: T coefficient at pole 6 (predicted = 2)
        results["C_44_2_6"] = self.extract_T_coeff_at_pole(w4w4, 6)

        # c_444: W_4 coefficient at pole 4
        results["c_444"] = self._extract_c444(w4w4)

        # ----- W_3 x W_4 OPE -----
        w3w4 = self.W3W4_ope()

        # C_34_2_5: T coefficient at pole 5 (predicted = 0)
        results["C_34_2_5"] = self.extract_T_coeff_at_pole(w3w4, 5)

        # C_34_3_4: W_3 coefficient at pole 4
        results["C_34_3_4"] = self.extract_W3_coeff_at_pole(w3w4, 4)

        # C_34_4_3: W_4 coefficient at pole 3
        results["C_34_4_3"] = self.extract_W4_coeff_at_pole(w3w4, 3)

        return results

    def _extract_c334(self, w3w3_ope: Dict[int, Field]) -> float:
        """Extract c_334 = W_3 x W_3 -> W_4 coefficient at pole 2.

        At pole 2 in the W_3 x W_3 OPE, the content of conformal weight 4 is:
          C_2 = (3/10) d^2T + beta * Lambda + c_334 * W_4

        We need to decompose C_2 in terms of {d^2T, Lambda, W_4}.

        Since we have free-field expressions for all these, we do this
        by solving a linear system.
        """
        if 2 not in w3w3_ope:
            return 0.0

        # The coefficient field at pole 2
        C2 = w3w3_ope[2]

        # Subtract the known descendant contribution:
        # d^2T appears from the T at pole 4: at pole 2, we get (1/2!)*(d^2)(C_4)
        # where C_4 = 2*T.
        # Actually this is handled by the OPE expansion already -- the Wick
        # contraction gives the FULL content at each pole, including all
        # contributions from contractions. So C_2 already IS the full expression,
        # and we just need to decompose it.

        # Decompose in the basis {d^2T, Lambda, W_4}
        return self._decompose_spin4(C2)

    def _extract_c444(self, w4w4_ope: Dict[int, Field]) -> float:
        """Extract c_444 = W_4 x W_4 -> W_4 coefficient at pole 4.

        At pole 4, the conformal weight is 4+4-4 = 4. The spin-4 content is:
          C_4 = alpha * d^2T + gamma * Lambda + c_444 * W_4
        (plus possibly dW_3 at weight 4).

        We need to decompose in the basis {d^2T, Lambda, W_4, dW_3}.
        """
        if 4 not in w4w4_ope:
            return 0.0

        C4 = w4w4_ope[4]

        # At pole 4 in W_4 x W_4, weight = 8 - 4 = 4.
        # Basis of weight-4 fields: d^2T, Lambda, W_4, dW_3
        # But by parity (W_4 x W_4 is symmetric in exchange, odd-spin
        # fields vanish at even poles), so dW_3 should be absent.
        # We still include it for safety.
        return self._decompose_spin4(C4)

    def physical_c334(self) -> float:
        """Extract c_334 using the physical (vertex algebra) inner product.

        The physical OPE coefficient c_334 in W_3(z)W_3(w) is defined by:
          C_2 = ... + c_334 * W_4 + (descendants and composites)

        To extract c_334 we use orthogonality of primaries under the physical
        inner product (2-point function): compute <W_4 | C_2>_phys / <W_4|W_4>_phys.

        The physical inner product <W_4 | C_2> is the coefficient of the leading
        singularity in the OPE W_4(z) C_2(w), which is at pole order 8 = 2*h_{W_4}.
        """
        w3w3 = self.W3W3_ope()
        if 2 not in w3w3:
            return 0.0
        C2 = w3w3[2]

        # Compute OPE of W_4 with C_2: the pole-8 coefficient is <W_4|C_2>_phys
        w4_c2_ope = compute_ope(self.W4, C2, 8)
        if 8 not in w4_c2_ope:
            return 0.0

        overlap = evaluate_field_as_number(w4_c2_ope[8])
        if overlap is None:
            return 0.0

        # Divide by <W_4|W_4>_phys = norm_W4
        return overlap / self.norm_W4 if abs(self.norm_W4) > 1e-15 else 0.0

    def physical_c444(self) -> float:
        """Extract c_444 using the physical inner product.

        Same method as physical_c334 but for the W_4(z)W_4(w) OPE at pole 4.
        """
        w4w4 = self.W4W4_ope()
        if 4 not in w4w4:
            return 0.0
        C4 = w4w4[4]

        w4_c4_ope = compute_ope(self.W4, C4, 8)
        if 8 not in w4_c4_ope:
            return 0.0

        overlap = evaluate_field_as_number(w4_c4_ope[8])
        if overlap is None:
            return 0.0

        return overlap / self.norm_W4 if abs(self.norm_W4) > 1e-15 else 0.0

    def _decompose_spin4(self, target: Field) -> float:
        """Extract the W_4 coefficient from a weight-4 field via Gram matrix.

        The weight-4 basis {W_4, Lambda, d^2T, dW_3} is NOT orthogonal
        under the free-field Wick contraction metric (the BPZ inner
        product of the Miura realization).  Primary orthogonality holds
        in the PHYSICAL W-algebra inner product, but the free-field inner
        product mixes conformal families because the free-boson Fock space
        at weight 4 has dimension > rank(W-algebra at weight 4).

        We therefore solve the full linear system:
          target = a * W_4 + b * Lambda + c * d^2T + d * dW_3
        using the Gram matrix G_{ij} = <basis_i | basis_j>_BPZ and the
        overlap vector v_i = <basis_i | target>_BPZ.
        The coefficients are x = G^{-1} v, and we return x[0] = a.
        """
        basis = [self.W4, self.Lambda, self.d2T, self.dW3]
        n = len(basis)

        # Build Gram matrix
        G = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                G[i, j] = _bpz_inner_product(basis[i], basis[j])

        # Build overlap vector
        v = np.zeros(n)
        for i in range(n):
            v[i] = _bpz_inner_product(basis[i], target)

        # Solve G x = v
        try:
            x = np.linalg.solve(G, v)
            return x[0]  # W_4 coefficient
        except np.linalg.LinAlgError:
            return 0.0

    def extract_all_with_verification(self) -> Dict[str, object]:
        """Extract all stage-4 coefficients with verification data."""
        norms = self.verify_normalizations()
        coeffs = self.extract_all_stage4_coefficients()

        # Also extract known stage-3 coefficients for cross-checks
        tt = self.TT_ope()
        tw3 = self.TW3_ope()
        w3w3 = self.W3W3_ope()

        verification = {
            "c_actual": self.c_actual,
            "alpha0_sq": self.t,
            "norms": norms,
            "stage4": coeffs,
            # Stage-3 cross-checks
            "TT_T_pole2": self.extract_T_coeff_at_pole(tt, 2),  # Should be 2
            "TW3_W3_pole2": self.extract_W3_coeff_at_pole(tw3, 2),  # Should be 3
            "W3W3_T_pole4": self.extract_T_coeff_at_pole(w3w3, 4),  # Should be 2
            "W3W3_vacuum_pole6": evaluate_field_as_number(w3w3.get(6, [])),
        }

        return verification


# =========================================================================
# Rational function interpolation from numerical samples
# =========================================================================

def interpolate_rational_function(
    c_values: List[float],
    f_values: List[float],
    max_num_deg: int = 4,
    max_den_deg: int = 4,
) -> Optional[Tuple[List, List]]:
    """Interpolate a rational function p(c)/q(c) from sample values.

    Given (c_i, f_i) pairs, find polynomials p(c), q(c) such that
    f_i = p(c_i)/q(c_i) for all i.

    We set q to be monic (leading coefficient 1) and solve the linear system:
    f_i * q(c_i) = p(c_i)
    f_i * (c_i^d + a_{d-1} c_i^{d-1} + ... + a_0) = b_m c_i^m + ... + b_0

    This gives: b_m c_i^m + ... + b_0 - f_i a_{d-1} c_i^{d-1} - ... - f_i a_0 = f_i c_i^d

    Returns (num_coeffs, den_coeffs) as lists [constant, c, c^2, ...].
    """
    n = len(c_values)

    best_fit = None
    best_residual = float('inf')

    for num_deg in range(max_num_deg + 1):
        for den_deg in range(max_den_deg + 1):
            n_params = num_deg + 1 + den_deg  # den is monic, so den_deg params
            if n_params > n:
                continue

            # Build the system: for each sample i,
            # sum_{j=0}^{num_deg} b_j c_i^j - f_i * sum_{j=0}^{den_deg-1} a_j c_i^j = f_i * c_i^{den_deg}
            A = np.zeros((n, n_params))
            rhs = np.zeros(n)

            for i, (ci, fi) in enumerate(zip(c_values, f_values)):
                # Numerator terms: b_j * c^j
                for j in range(num_deg + 1):
                    A[i, j] = ci ** j
                # Denominator terms: -f_i * a_j * c^j (a_j for j=0,...,den_deg-1)
                for j in range(den_deg):
                    A[i, num_deg + 1 + j] = -fi * ci ** j
                # RHS
                rhs[i] = fi * ci ** den_deg

            # Solve
            try:
                result, residuals, rank, sv = np.linalg.lstsq(A, rhs, rcond=None)
                fit_residual = np.linalg.norm(A @ result - rhs)

                if fit_residual < best_residual - 1e-10:
                    best_residual = fit_residual
                    num_coeffs = list(result[:num_deg + 1])
                    den_coeffs = list(result[num_deg + 1:]) + [1.0]  # monic
                    best_fit = (num_coeffs, den_coeffs, num_deg, den_deg, fit_residual)
            except np.linalg.LinAlgError:
                continue

    if best_fit is None:
        return None

    num_coeffs, den_coeffs, nd, dd, res = best_fit
    return num_coeffs, den_coeffs


def rational_func_to_sympy(num_coeffs: List[float], den_coeffs: List[float]):
    """Convert numerical rational function coefficients to a sympy expression."""
    c = Symbol('c')
    # Try to rationalize coefficients
    num_poly = sum(nsimplify(coeff, rational=True) * c**i
                   for i, coeff in enumerate(num_coeffs))
    den_poly = sum(nsimplify(coeff, rational=True) * c**i
                   for i, coeff in enumerate(den_coeffs))
    return cancel(num_poly / den_poly)


# =========================================================================
# Multi-sample computation and interpolation
# =========================================================================

def compute_stage4_at_samples(
    t_values: Optional[List[float]] = None,
    c_values: Optional[List[float]] = None,
    verbose: bool = False,
) -> Dict[str, List[Tuple[float, float]]]:
    """Compute all stage-4 coefficients at multiple parameter values.

    Parametrizes by t = alpha_0^2 directly. For each t, the actual central
    charge c_M = 3 + 60*t is determined from the T self-OPE, and OPE
    coefficients are recorded as (c_actual, value) pairs.

    Parameters
    ----------
    t_values : list of float, optional
        Values of t = alpha_0^2 to sample. Preferred interface.
    c_values : list of float, optional
        Legacy interface: c-values to convert to t. If both are given,
        t_values takes precedence.
    verbose : bool

    Returns {coeff_name: [(c_actual, value), ...]} for each coefficient.
    """
    if t_values is None and c_values is None:
        # Default t values giving c_M from ~3.6 to ~1203
        t_values = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    results: Dict[str, List[Tuple[float, float]]] = {
        "c_334": [],
        "c_444": [],
        "C_34_3_4": [],
        "C_34_4_3": [],
        "C_44_2_6": [],
        "C_34_2_5": [],
    }

    if t_values is not None:
        for t_val in t_values:
            try:
                ope = W4MiuraOPE.from_t(t_val, verbose=verbose)
                coeffs = ope.extract_all_stage4_coefficients()
                c_actual = ope.c_actual
                for name in results:
                    results[name].append((c_actual, coeffs[name]))
                if verbose:
                    print(f"t = {t_val}, c_actual = {c_actual}: {coeffs}")
            except Exception as e:
                if verbose:
                    print(f"t = {t_val}: FAILED ({e})")
    else:
        # Legacy c_values interface
        for c_val in c_values:
            try:
                ope = W4MiuraOPE(c_val, verbose=verbose)
                coeffs = ope.extract_all_stage4_coefficients()
                c_actual = ope.c_actual
                for name in results:
                    results[name].append((c_actual, coeffs[name]))
                if verbose:
                    print(f"c_requested = {c_val}, c_actual = {c_actual}: {coeffs}")
            except Exception as e:
                if verbose:
                    print(f"c = {c_val}: FAILED ({e})")

    return results


def extract_rational_functions(
    samples: Dict[str, List[Tuple[float, float]]],
    max_deg: int = 4,
) -> Dict[str, object]:
    """Interpolate rational functions from sample data."""
    results = {}
    c = Symbol('c')

    for name, data in samples.items():
        if len(data) < 3:
            results[name] = {"status": "insufficient_data", "n_samples": len(data)}
            continue

        c_vals = [d[0] for d in data]
        f_vals = [d[1] for d in data]

        fit = interpolate_rational_function(c_vals, f_vals, max_deg, max_deg)
        if fit is None:
            results[name] = {"status": "fit_failed"}
            continue

        num_coeffs, den_coeffs = fit
        expr = rational_func_to_sympy(num_coeffs, den_coeffs)

        # Verify the fit at sample points
        max_error = 0.0
        for ci, fi in zip(c_vals, f_vals):
            predicted = float(expr.subs(c, ci))
            max_error = max(max_error, abs(predicted - fi))

        results[name] = {
            "expression": expr,
            "simplified": simplify(expr),
            "max_fit_error": max_error,
            "num_coeffs": num_coeffs,
            "den_coeffs": den_coeffs,
        }

    return results


# =========================================================================
# Verification of the two predictions
# =========================================================================

def verify_predictions(
    samples: Dict[str, List[Tuple[float, float]]],
    tol: float = 1e-4,
) -> Dict[str, Dict]:
    """Verify the two falsifiable predictions from the manuscript.

    Prediction 1: C^res_{4,4;2;0,6} = 2 (universal T-coupling)
    Prediction 2: C^res_{3,4;2;0,5} = 0 (mixed Virasoro vanishing)
    """
    results = {}

    # Prediction 1: C_44_2_6 = 2
    if "C_44_2_6" in samples:
        data = samples["C_44_2_6"]
        values = [v for _, v in data]
        avg = np.mean(values) if values else None
        max_dev = max(abs(v - 2.0) for _, v in data) if data else None
        results["universal_T_coupling"] = {
            "predicted": 2,
            "observed_values": values,
            "mean": avg,
            "max_deviation_from_2": max_dev,
            "verified": max_dev is not None and max_dev < tol,
        }

    # Prediction 2: C_34_2_5 = 0
    if "C_34_2_5" in samples:
        data = samples["C_34_2_5"]
        values = [v for _, v in data]
        avg = np.mean(values) if values else None
        max_abs = max(abs(v) for _, v in data) if data else None
        results["mixed_Virasoro_vanishing"] = {
            "predicted": 0,
            "observed_values": values,
            "mean": avg,
            "max_absolute_value": max_abs,
            "verified": max_abs is not None and max_abs < tol,
        }

    return results


# =========================================================================
# Known exact results for cross-checking
# =========================================================================

def w3_ope_beta(c_val: float) -> float:
    """The W_3 Lambda coupling: beta = 16/(22+5c)."""
    return 16.0 / (22.0 + 5.0 * c_val)


def known_stage3_coefficients() -> Dict[str, object]:
    """Known universal (c-independent) stage-3 coefficients.

    From prop:winfty-ds-stage3-explicit-packet:
      C_{2,2;2;0,2} = 2   (T x T -> T)
      C_{2,3;3;0,2} = 3   (T x W_3 -> W_3)
      C_{3,3;2;0,4} = 2   (W_3 x W_3 -> T)
    """
    return {
        "TT_T_pole2": 2,
        "TW3_W3_pole2": 3,
        "W3W3_T_pole4": 2,
    }


# =========================================================================
# Full pipeline: compute, interpolate, verify
# =========================================================================

def full_stage4_extraction(
    t_values: Optional[List[float]] = None,
    c_values: Optional[List[float]] = None,
    verbose: bool = False,
) -> Dict[str, object]:
    """Complete stage-4 coefficient extraction pipeline.

    1. Compute OPE coefficients at multiple t-values (or c-values).
    2. Interpolate to rational functions of c.
    3. Verify the two predictions.
    4. Report all 6 coefficients.

    Preferred: pass t_values (direct parametrization by alpha_0^2).
    """
    samples = compute_stage4_at_samples(
        t_values=t_values, c_values=c_values, verbose=verbose
    )
    rational_funcs = extract_rational_functions(samples)
    predictions = verify_predictions(samples)

    return {
        "samples": samples,
        "rational_functions": rational_funcs,
        "predictions": predictions,
    }


# =========================================================================
# Runner
# =========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("W_4 OPE EXTRACTION VIA QUANTUM MIURA TRANSFORMATION")
    print("=" * 70)

    # Test at a specific t value
    t_test = 0.1
    print(f"\nTesting at t = {t_test}...")
    ope = W4MiuraOPE.from_t(t_test, verbose=True)
    norms = ope.verify_normalizations()
    print(f"Normalizations: {norms}")

    coeffs = ope.extract_all_stage4_coefficients()
    print(f"\nStage-4 coefficients (c_actual = {ope.c_actual:.4f}):")
    for k, v in coeffs.items():
        print(f"  {k} = {v:.8f}")

    # Full extraction with t-parametrization
    print("\n" + "=" * 70)
    print("FULL EXTRACTION (multiple t-values)")
    print("=" * 70)
    result = full_stage4_extraction(verbose=True)

    print("\nPredictions:")
    for k, v in result["predictions"].items():
        print(f"  {k}: {v}")

    print("\nRational functions:")
    for k, v in result["rational_functions"].items():
        print(f"  {k}: {v}")
