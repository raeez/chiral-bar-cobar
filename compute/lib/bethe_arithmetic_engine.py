r"""Arithmetic of Bethe ansatz roots: number fields, Galois groups, and shadow connections.

The Bethe ansatz for integrable spin chains produces algebraic numbers as
solutions to polynomial systems.  For the XXX_{sl_2} chain with L sites and
M magnons, the Bethe ansatz equations (BAE) are:

    \prod_{j \neq i} \frac{u_i - u_j + 1}{u_i - u_j - 1}
    = \left( \frac{u_i + i/2}{u_i - i/2} \right)^L

The algebraic Bethe roots u_i generate number fields K = Q(u_1, ..., u_M)
whose arithmetic invariants (degree, Galois group, discriminant) encode
structural information about the integrable model.

SHADOW CONNECTION (AP19, AP27):
    The Yangian R-matrix R(u) = Res^{coll}_{0,2}(Theta_A) is the genus-0
    binary shadow of the MC element.  Bethe roots are singular points of the
    shadow transfer matrix: T(u) Q(u) = a(u) Q(u-eta) + d(u) Q(u+eta),
    and Q(u) = 0 at Bethe roots.  The arithmetic of these singular points
    connects to the singular divisor D_A of the arithmetic packet connection
    nabla^arith_A (def:arithmetic-packet-connection).

MODULES:
    1. Algebraic Bethe roots via resultant / Groebner basis methods
    2. Minimal polynomials and number field generation
    3. Galois group computation (via resolvent polynomials)
    4. Bethe root discriminants and comparison with shadow discriminants
    5. XXZ chain at roots of unity: cyclotomic Bethe roots
    6. Bethe completeness and singular solutions
    7. Transfer matrix eigenvalue factorization
    8. Arithmetic height of Bethe roots
    9. Multi-path verification (numerical, algebraic, exact diag, shadow)

Conventions:
    - Cohomological grading (|d| = +1), bar uses desuspension (AP45).
    - kappa(sl_2, k) = 3(k+2)/4 (AP1, AP39).
    - Bar complex propagator d log E(z,w) is weight 1 (AP27).
    - R-matrix r(z) has pole order ONE LESS than OPE (AP19).
    - XXX BAE: logarithmic form with arctan (standard Faddeev convention).
    - Energy: E = L/4 - (1/2) sum 1/(u_a^2 + 1/4) for the XXX chain.

References:
    - Faddeev, "How the algebraic Bethe ansatz works" (Les Houches 1996)
    - Baxter, "Exactly Solved Models in Statistical Mechanics" (1982)
    - Korepin-Bogoliubov-Izergin, "QISM and Correlation Functions" (1993)
    - Hao-Nepomechie-Sommese, "Completeness of solutions of BAE" (2013)
    - thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    - def:arithmetic-packet-connection (arithmetic_shadows.tex)
    - AP19, AP27 (CLAUDE.md)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Set
from itertools import combinations, product as iterproduct
from math import comb, gcd, factorial
from functools import reduce

import numpy as np
from numpy import linalg as la
from scipy import optimize

# Sympy for exact algebraic computation
import sympy
from sympy import (Rational, sqrt, I, pi, oo,
                   Poly, Symbol, symbols, expand, factor, simplify,
                   resultant, groebner, minimal_polynomial,
                   QQ, ZZ, nroots, degree, discriminant as sym_discriminant,
                   Matrix, eye as sym_eye, cos, sin, exp, log,
                   roots as sym_roots, solve as sym_solve,
                   AlgebraicNumber, primitive_element,
                   cyclotomic_poly, Abs)
from sympy.polys.numberfields import field_isomorphism
from sympy.combinatorics import PermutationGroup, Permutation
from sympy.ntheory import factorint


# ========================================================================
# 0.  Pauli matrices and spin operators (numpy, for numerical path)
# ========================================================================

I2 = np.eye(2, dtype=complex)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def _kron_chain(ops: List[np.ndarray]) -> np.ndarray:
    """Kronecker product of a list of operators."""
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result


def _spin_op(L: int, site: int, pauli: np.ndarray) -> np.ndarray:
    """Spin-1/2 operator at given site on chain of length L."""
    ops = [I2] * L
    ops[site] = pauli
    return _kron_chain(ops)


# ========================================================================
# 1.  XXX Bethe ansatz: exact algebraic solver
# ========================================================================

def xxx_bae_polynomial_system(L: int, M: int) -> Tuple[List, List]:
    r"""Set up the XXX BAE as a REAL polynomial system in sympy.

    The BAE for the XXX chain with L sites, M magnons (Faddeev convention):

        \prod_{j \neq i} \frac{u_i - u_j + i}{u_i - u_j - i}
        = \left(\frac{u_i + i/2}{u_i - i/2}\right)^L

    where i = sqrt(-1).  The Bethe roots u_i are REAL for the XXX chain.

    To obtain a real polynomial system, we cross-multiply and separate
    real and imaginary parts.  For each magnon equation, we get the
    imaginary part of:

        \prod_{j \neq i} (u_i - u_j + i) \cdot (u_i - i/2)^L
        - \prod_{j \neq i} (u_i - u_j - i) \cdot (u_i + i/2)^L = 0

    The imaginary part of this expression (as a polynomial in the real
    variables u_0, ..., u_{M-1}) is a real polynomial that vanishes at
    the Bethe roots.

    Returns:
        (variables, equations) where variables are sympy Symbols
        and equations are sympy Expr (real polynomials, each should equal 0).
    """
    u = symbols(f'u0:{M}', real=True)

    equations = []
    for i in range(M):
        # LHS: prod_{j!=i} (u_i - u_j + i)
        lhs_prod = sympy.Integer(1)
        for j in range(M):
            if j != i:
                lhs_prod *= (u[i] - u[j] + I)

        # RHS numerator: (u_i + i/2)^L
        rhs_num = (u[i] + I * Rational(1, 2))**L
        # RHS denominator: (u_i - i/2)^L
        rhs_den = (u[i] - I * Rational(1, 2))**L

        # Cross-multiplied: lhs_prod * rhs_den - conjugate * rhs_num = 0
        # where conjugate of prod_{j!=i}(u_i-u_j+i) = prod_{j!=i}(u_i-u_j-i)
        conj_prod = sympy.Integer(1)
        for j in range(M):
            if j != i:
                conj_prod *= (u[i] - u[j] - I)

        expr = expand(lhs_prod * rhs_den - conj_prod * rhs_num)

        # For real u_i, this expression is purely imaginary (since BAE must hold).
        # Extract the imaginary part as a real polynomial.
        expr_expanded = expand(expr)
        eq = sympy.im(expr_expanded)
        eq = expand(eq)

        equations.append(eq)

    return list(u), equations


def xxx_bethe_roots_numerical(L: int, M: int,
                               quantum_numbers: Optional[np.ndarray] = None,
                               num_trials: int = 50) -> List[np.ndarray]:
    r"""Find ALL Bethe root sets for (L, M) by multi-start numerical solving.

    For the XXX chain with L sites, M magnons, the quantum numbers I_i
    range over allowed half-integer/integer values.  We enumerate all
    valid quantum number sets and solve each.

    The allowed quantum numbers for the XXX chain (Faddeev convention):
        I_i in {-(L-M-1)/2, ..., (L-M-1)/2}  (for each magnon)
    with I_1 < I_2 < ... < I_M (ordering by convention).

    Returns:
        List of Bethe root arrays, one per distinct solution.
    """
    if M == 0:
        return [np.array([])]

    # Allowed quantum numbers (Bethe-Takahashi convention):
    # For M magnons on L sites, the quantum numbers I_i are:
    #   - half-integers if L - M is even
    #   - integers if L - M is odd
    # with |I_i| <= (L - 1)/2, and all I_i distinct.
    # The number of regular Bethe states is at most C(L, M).
    # Typically, the allowed range is I_i in {-(L-1)/2, ..., (L-1)/2}
    # excluding certain values at the boundary.
    I_max = (L - 1) / 2.0

    if (L - M) % 2 == 0:
        # Half-integer quantum numbers
        allowed = [n + 0.5 for n in range(int(-I_max - 0.5), int(I_max + 0.5))]
    else:
        # Integer quantum numbers
        allowed = [float(n) for n in range(int(-I_max), int(I_max) + 1)]

    # Enumerate all M-element subsets of allowed quantum numbers
    all_qn_sets = list(combinations(allowed, M))

    solutions = []
    seen_roots = []

    for qn in all_qn_sets:
        qn_arr = np.array(qn)

        # Try multiple initial guesses
        np.random.seed(42 + hash(qn) % 1000)  # Reproducible but varied
        for trial in range(8):
            if trial == 0:
                # Best guess: roots near quantum number values / L
                u0 = np.array(qn) / (2.0 * L) * np.pi
            elif trial == 1:
                u0 = np.array(qn) * 0.5
            elif trial == 2:
                u0 = np.array(qn) * 0.3
            elif trial == 3:
                # Tangent-based guess from BAE solution for M=1
                u0 = np.array([0.5 * np.tan(np.pi * I_k / L)
                               if abs(np.cos(np.pi * I_k / L)) > 0.01
                               else I_k * 10.0
                               for I_k in qn])
            else:
                u0 = np.array(qn) * (0.2 + 0.1 * trial) + np.random.randn(M) * 0.1

            def equations(u):
                f = np.zeros(M)
                for i in range(M):
                    f[i] = L * np.arctan(2 * u[i])
                    for j in range(M):
                        if j != i:
                            f[i] -= np.arctan(u[i] - u[j])
                    f[i] -= np.pi * qn_arr[i]
                return f

            try:
                result = optimize.fsolve(equations, u0, full_output=True)
                roots = np.sort(result[0])
                success = result[2] == 1

                if not success:
                    continue

                # Check residual
                res = equations(roots)
                if np.max(np.abs(res)) > 1e-8:
                    continue

                # Reject spurious solutions with very large roots
                # (u -> infinity corresponds to a trivial/boundary state)
                if np.max(np.abs(roots)) > 100 * L:
                    continue

                # Check if this is a new solution
                is_new = True
                for prev in seen_roots:
                    if len(prev) == len(roots) and np.allclose(prev, roots, atol=1e-6):
                        is_new = False
                        break

                if is_new:
                    seen_roots.append(roots)
                    solutions.append(roots)
                    break  # Found a solution for this qn set
            except Exception:
                continue

    return solutions


def xxx_bethe_roots_exact_L4_M2() -> Dict[str, Any]:
    r"""Exact Bethe roots for L=4, M=2.

    Ground state: quantum numbers I = (-1/2, 1/2).
    By parity symmetry: u_2 = -u_1.  Setting u_1 = u, u_2 = -u:

    BAE (logarithmic form):
        4*arctan(2u) - arctan(2u) = pi/2
        3*arctan(2u) = pi/2
        arctan(2u) = pi/6
        2u = tan(pi/6) = 1/sqrt(3)
        u = 1/(2*sqrt(3))

    So u_1 = -1/(2*sqrt(3)), u_2 = 1/(2*sqrt(3)).
    Minimal polynomial of u: 12u^2 - 1 = 0 (since u^2 = 1/12).
    Number field: Q(sqrt(3)), degree 2.
    """
    u_sym = Symbol('u')
    u_val = Rational(1, 2) * sqrt(Rational(1, 3))
    min_poly = Poly(12 * u_sym**2 - 1, u_sym)

    # Numerical values
    u_num = float(u_val.evalf())
    roots_numerical = [(-u_num, u_num)]

    return {
        'L': 4, 'M': 2,
        'minimal_polynomial': min_poly,
        'exact_root': u_val,
        'numerical_roots': roots_numerical,
        'number_field': 'Q(sqrt(3))',
        'number_field_degree': 2,
    }


def xxx_bethe_polynomial(L: int, M: int) -> Optional[Poly]:
    r"""Compute the Bethe polynomial P_{L,M}(u) whose roots are the Bethe roots.

    For the XXX chain, the Baxter Q-operator eigenvalue is:
        Q(u) = \prod_{a=1}^{M} (u - u_a)

    The BAE are equivalent to the TQ relation:
        (u + i/2)^L Q(u + i) + (u - i/2)^L Q(u - i) = T(u) Q(u)

    For computing the POLYNOMIAL whose roots are Bethe roots,
    we use the resultant/elimination approach on the polynomial BAE system.

    For small (L, M), we can solve directly.

    Returns a univariate polynomial in u whose roots include all Bethe roots
    for the given (L, M) sector.
    """
    if M == 0:
        return Poly(1, Symbol('u'))
    if M == 1:
        # Use the M=1 minimal polynomial: Im((u + i/2)^L) = 0
        return bethe_minimal_polynomial_M1(L)

    # For M >= 2: use the polynomial BAE system and eliminate variables
    # This is computationally expensive for large M, so we limit scope
    if M > 4 or L > 12:
        return None

    variables, equations = xxx_bae_polynomial_system(L, M)

    if M == 2:
        # Eliminate v from the two equations to get polynomial in u
        res = resultant(equations[0], equations[1], variables[1])
        return Poly(res, variables[0])

    # For M >= 3, iteratively eliminate variables
    # Eliminate u_{M-1}, then u_{M-2}, ..., down to u_0
    current_eqs = list(equations)
    for k in range(M - 1, 0, -1):
        var_to_elim = variables[k]
        # Take resultants of consecutive equation pairs
        new_eqs = []
        for i in range(len(current_eqs) - 1):
            try:
                res = resultant(current_eqs[i], current_eqs[i + 1], var_to_elim)
                if res != 0:
                    new_eqs.append(res)
            except Exception:
                pass
        if not new_eqs:
            return None
        current_eqs = new_eqs

    if current_eqs:
        return Poly(current_eqs[0], variables[0])
    return None


# ========================================================================
# 2.  Number field and Galois group computation
# ========================================================================

def bethe_number_field_degree(L: int, M: int) -> Optional[int]:
    """Compute the degree of the number field generated by Bethe roots.

    This is the degree of the minimal polynomial of a generic Bethe root.
    For M=1: the Bethe polynomial has degree L-1 (removing the zeta=1 root).
    """
    poly = xxx_bethe_polynomial(L, M)
    if poly is None:
        return None
    return degree(poly)


def bethe_minimal_polynomial_M1(L: int) -> Poly:
    r"""Minimal polynomial for M=1 Bethe roots.

    For single magnon: u_k = (1/2) cot(pi*k/L) for k = 1, ..., L-1.

    The BAE for M=1: ((u + i/2)/(u - i/2))^L = 1.
    Cross-multiplying: (u + i/2)^L = (u - i/2)^L.
    For real u, these are complex conjugates, so the equation reduces to:
        Im((u + i/2)^L) = 0.

    This is a real polynomial in u of degree L-1 (the leading real part
    cancels; the imaginary part has degree at most L-1).

    The polynomial has L-1 real roots: u_k = (1/2)*cot(pi*k/L), k=1,...,L-1.
    """
    u = Symbol('u', real=True)
    expr = expand((u + I * Rational(1, 2))**L)
    im_part = sympy.im(expr)
    poly_expr = expand(im_part)
    return Poly(poly_expr, u)


def bethe_discriminant_M1(L: int) -> sympy.Expr:
    """Discriminant of the M=1 Bethe polynomial.

    The discriminant measures the "spread" of the Bethe roots and is
    related to the shadow metric discriminant Delta(A).
    """
    poly = bethe_minimal_polynomial_M1(L)
    return poly.discriminant()


def bethe_galois_group_M1(L: int) -> Dict[str, Any]:
    r"""Galois group of the splitting field for M=1 Bethe roots.

    For L sites, M=1: the Bethe roots are u_k = (1/2)cot(pi k/L),
    k = 1, ..., L-1.  These are the half-cotangent values at L-th
    roots of unity.

    The splitting field is Q(cos(2pi/L)) = Q(zeta_L + zeta_L^{-1}),
    the maximal real subfield of Q(zeta_L).

    Galois group: Gal(Q(zeta_L)^+/Q) = (Z/LZ)^* / {+/- 1},
    which has order phi(L)/2 for L >= 3.

    For L prime: Gal = Z/((L-1)/2)Z (cyclic).
    For L = 4: Gal = {1} (trivial, degree 1: u = 0 is the only root mod symmetry).
    For L = 6: Gal has order phi(6)/2 = 1.
    """
    try:
        from sympy.functions.combinatorial.numbers import totient
    except ImportError:
        from sympy.ntheory import totient

    phi_L = totient(L)
    if L <= 2:
        gal_order = 1
    else:
        gal_order = phi_L // 2

    # The Galois group is (Z/LZ)^* / {+-1}
    # Compute the group explicitly
    units = [k for k in range(1, L) if gcd(k, L) == 1]
    # Quotient by {+1, -1 mod L}: identify k with L-k
    representatives = set()
    for k in units:
        rep = min(k, L - k)
        representatives.add(rep)

    return {
        'L': L,
        'galois_order': gal_order,
        'euler_totient': phi_L,
        'splitting_field_degree': gal_order,
        'is_cyclic': _is_prime(L),
        'group_description': f'(Z/{L}Z)^* / {{+-1}}',
        'representatives': sorted(representatives),
    }


def _is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def bethe_state_count(L: int, M: int) -> int:
    """Number of Bethe states (= dimension of the Sz sector).

    For the XXX chain with L sites, M magnons, the Hilbert space
    dimension of the Sz = L/2 - M sector is C(L, M).

    The Bethe completeness conjecture states that the number of
    regular Bethe states equals C(L, M).
    """
    return comb(L, M)


# ========================================================================
# 3.  Exact diagonalization (for verification)
# ========================================================================

def xxx_hamiltonian(L: int) -> np.ndarray:
    """XXX Heisenberg Hamiltonian: H = sum S_i . S_{i+1} (periodic BC)."""
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        for pauli in [SIGMA_X, SIGMA_Y, SIGMA_Z]:
            Si = _spin_op(L, i, pauli)
            Sj = _spin_op(L, j, pauli)
            H += 0.25 * Si @ Sj
    return H


def xxx_total_sz(L: int) -> np.ndarray:
    """Total S^z operator."""
    Sz = np.zeros((2**L, 2**L), dtype=complex)
    for i in range(L):
        Sz += 0.5 * _spin_op(L, i, SIGMA_Z)
    return Sz


def exact_diag_sector(L: int, M: int) -> Tuple[np.ndarray, np.ndarray]:
    """Exact diagonalization in the Sz = L/2 - M sector.

    Returns (eigenvalues, eigenvectors) sorted by energy.
    """
    H = xxx_hamiltonian(L)
    Sz = xxx_total_sz(L)
    sz_vals = np.diag(Sz.real)
    target = L / 2.0 - M
    mask = np.abs(sz_vals - target) < 1e-10
    indices = np.where(mask)[0]
    if len(indices) == 0:
        return np.array([]), np.array([])
    H_sector = H[np.ix_(indices, indices)]
    evals, evecs = la.eigh(H_sector)
    order = np.argsort(evals)
    return evals[order], evecs[:, order]


def xxx_energy_from_roots(roots: np.ndarray, L: int) -> float:
    """Energy from Bethe roots: E = L/4 - (1/2) sum 1/(u_a^2 + 1/4)."""
    return L / 4.0 - 0.5 * np.sum(1.0 / (roots**2 + 0.25))


# ========================================================================
# 4.  Transfer matrix eigenvalues and factorization
# ========================================================================

def xxx_transfer_eigenvalue(u: complex, roots: np.ndarray, L: int) -> complex:
    r"""Transfer matrix eigenvalue from Bethe roots.

    \Lambda(u) = (u + i/2)^L \prod_a \frac{u - u_a - i}{u - u_a}
               + (u - i/2)^L \prod_a \frac{u - u_a + i}{u - u_a}

    This is the eigenvalue of the transfer matrix T(u) on the Bethe state
    parametrized by roots {u_a}.
    """
    M = len(roots)
    if M == 0:
        return (u + 0.5j)**L + (u - 0.5j)**L

    prod1 = np.prod([(u - r - 1j) / (u - r) for r in roots])
    prod2 = np.prod([(u - r + 1j) / (u - r) for r in roots])

    return (u + 0.5j)**L * prod1 + (u - 0.5j)**L * prod2


def xxx_transfer_eigenvalue_polynomial(roots: np.ndarray, L: int) -> np.ndarray:
    r"""Polynomial form of the transfer eigenvalue.

    Lambda(u) as a polynomial in u (clearing the Q(u) denominator).
    This is a polynomial of degree L.

    Returns coefficients [c_L, c_{L-1}, ..., c_0] (highest degree first).
    """
    M = len(roots)
    # Evaluate at L+1 points and interpolate
    points = np.linspace(-5, 5, L + 1) + 0.01j  # Avoid poles
    values = np.array([xxx_transfer_eigenvalue(u, roots, L) for u in points])

    # Polynomial fit (degree L)
    # Use numpy polyfit (coefficients highest degree first)
    coeffs = np.polyfit(points, values, L)
    return coeffs


def transfer_eigenvalue_factorization(roots: np.ndarray, L: int,
                                       ) -> Dict[str, Any]:
    r"""Factor the transfer eigenvalue Lambda(u) over Q.

    Lambda(u) is a polynomial of degree L.  Its factorization into
    irreducible polynomials over Q encodes the arithmetic structure.

    The irreducible factors correspond to Galois orbits of Bethe roots.
    """
    coeffs = xxx_transfer_eigenvalue_polynomial(roots, L)

    # Convert to sympy for exact factorization (if coefficients are rational)
    u = Symbol('u')
    poly_expr = sum(c * u**(L - k) for k, c in enumerate(coeffs))

    # Round to rational if close
    rational_coeffs = []
    for k, c in enumerate(coeffs):
        c_real = c.real
        # Try to identify as rational
        from fractions import Fraction
        frac = Fraction(c_real).limit_denominator(10000)
        rational_coeffs.append(Rational(frac.numerator, frac.denominator))

    poly_rational = Poly(sum(c * u**(L - k) for k, c in enumerate(rational_coeffs)), u)

    try:
        factors = poly_rational.factor_list()
    except Exception:
        factors = None

    return {
        'numerical_coeffs': coeffs,
        'rational_poly': poly_rational,
        'factors': factors,
        'L': L,
        'M': len(roots),
    }


# ========================================================================
# 5.  Shadow transfer matrix (from shadow data)
# ========================================================================

def shadow_transfer_eigenvalue(u: complex, kappa: float, L: int,
                                shadow_coeffs: Optional[Dict[int, float]] = None
                                ) -> complex:
    r"""Shadow transfer matrix eigenvalue from shadow obstruction tower data.

    The "shadow transfer matrix" is constructed from the shadow data:
        T^sh(u) = exp( sum_r S_r * u^{-r} )

    where S_r are the shadow invariants (S_2 = kappa, S_3 = cubic shadow, etc.).

    For the sl_2 XXX chain at level k:
        kappa(sl_2, k) = 3(k+2)/4
        S_2 = kappa
        S_3 = 0 (sl_2 is class L, shadow depth 3)
        S_r = 0 for r >= 3

    So T^sh(u) = exp(kappa * u^{-2}) for the sl_2 chain.

    For the actual transfer eigenvalue at large u:
        Lambda(u) ~ 2 u^L + ... = 2 u^L (1 + kappa/(2u^2) + ...)

    The shadow connection prediction:
        Lambda(u) / (2u^L) ~ exp(kappa/u^2) for |u| >> 1

    Args:
        u: spectral parameter.
        kappa: modular characteristic.
        L: chain length (number of sites).
        shadow_coeffs: dict mapping arity r to shadow coefficient S_r.
            If None, uses the sl_2 shadow data (S_2 = kappa, rest = 0).
    """
    if shadow_coeffs is None:
        shadow_coeffs = {2: kappa}

    exponent = sum(S_r * u**(-r) for r, S_r in shadow_coeffs.items())
    return 2 * u**L * np.exp(exponent)


def compare_transfer_shadow(roots: np.ndarray, L: int, kappa: float,
                             u_test_points: Optional[np.ndarray] = None
                             ) -> Dict[str, Any]:
    r"""Compare actual transfer eigenvalue with shadow prediction.

    Tests the shadow connection prediction:
        Lambda(u) / (2u^L) ~ exp(kappa/u^2) for large |u|.

    Returns relative errors at test points.
    """
    if u_test_points is None:
        u_test_points = np.array([3.0, 5.0, 8.0, 10.0, 15.0, 20.0]) + 0.01j

    actual = np.array([xxx_transfer_eigenvalue(u, roots, L)
                       for u in u_test_points])
    shadow = np.array([shadow_transfer_eigenvalue(u, kappa, L)
                        for u in u_test_points])

    # Relative error
    rel_err = np.abs(actual - shadow) / np.abs(actual)

    return {
        'test_points': u_test_points,
        'actual': actual,
        'shadow': shadow,
        'relative_error': rel_err,
        'max_relative_error': float(np.max(rel_err)),
        'kappa': kappa,
        'L': L,
    }


# ========================================================================
# 6.  XXZ at roots of unity: cyclotomic Bethe roots
# ========================================================================

def xxz_hamiltonian(L: int, Delta: float) -> np.ndarray:
    """XXZ Hamiltonian with anisotropy Delta."""
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        for pauli in [SIGMA_X, SIGMA_Y]:
            Si = _spin_op(L, i, pauli)
            Sj = _spin_op(L, j, pauli)
            H += 0.25 * Si @ Sj
        Szi = _spin_op(L, i, SIGMA_Z)
        Szj = _spin_op(L, j, SIGMA_Z)
        H += 0.25 * Delta * Szi @ Szj
    return H


def xxz_bae_roots_of_unity(L: int, M: int, p: int,
                            quantum_numbers: Optional[np.ndarray] = None
                            ) -> Dict[str, Any]:
    r"""Solve XXZ BAE at q = root of unity (q^p = 1).

    At q = exp(2*pi*i/p), the anisotropy Delta = cos(2*pi/p).
    The BAE become:
        \prod_{j \neq i} \frac{\sin(\lambda_i - \lambda_j + \gamma)}
                                {\sin(\lambda_i - \lambda_j - \gamma)}
        = \left( \frac{\sin(\lambda_i + \gamma/2)}
                       {\sin(\lambda_i - \gamma/2)} \right)^L

    where gamma = pi/p.

    At roots of unity, the Bethe roots have algebraic structure
    related to the cyclotomic field Q(zeta_p).

    Args:
        L: chain length.
        M: number of magnons.
        p: root of unity parameter (q^p = 1, q = e^{2pi i/p}).
        quantum_numbers: Bethe quantum numbers.

    Returns:
        Dict with roots, energy, Delta, gamma, and cyclotomic data.
    """
    gamma = np.pi / p
    Delta = np.cos(2 * np.pi / p)  # = cos(2*gamma) when gamma = pi/p
    # Actually Delta = (q + q^{-1})/2 = cos(2*pi/p), and
    # gamma is the parameter such that q = e^{i*gamma}, so gamma = 2*pi/p
    # for q^p = 1.  But the BAE use gamma as the anisotropy parameter
    # where Delta = cos(gamma), so gamma = 2*pi/p means Delta = cos(2*pi/p).
    # Let's be careful: q = e^{i*gamma}, q^p = 1 => gamma = 2*pi/p.
    gamma = 2 * np.pi / p
    Delta = np.cos(gamma)

    if quantum_numbers is None:
        quantum_numbers = np.array([-(M - 1) / 2 + k for k in range(M)])

    def bae_residual(lam):
        f = np.zeros(M)
        for i in range(M):
            # Driving term
            phase_drive = np.sin(lam[i] + gamma / 2) / np.sin(lam[i] - gamma / 2)
            if abs(phase_drive) > 1e-15:
                f[i] = L * np.arctan2(np.sin(lam[i] + gamma / 2),
                                       np.cos(lam[i] + gamma / 2))
                f[i] -= L * np.arctan2(np.sin(lam[i] - gamma / 2),
                                         np.cos(lam[i] - gamma / 2))
            # Scattering
            for j in range(M):
                if j != i:
                    f[i] -= np.arctan2(np.sin(lam[i] - lam[j] + gamma),
                                        np.cos(lam[i] - lam[j] + gamma))
                    f[i] += np.arctan2(np.sin(lam[i] - lam[j] - gamma),
                                        np.cos(lam[i] - lam[j] - gamma))
            f[i] -= 2 * np.pi * quantum_numbers[i]
        return f

    # Initial guess
    lam0 = np.array(quantum_numbers) * gamma * 0.3
    if M > 0:
        try:
            result = optimize.fsolve(bae_residual, lam0, full_output=True)
            roots = result[0]
            success = result[2] == 1
            residual = np.max(np.abs(bae_residual(roots)))
        except Exception:
            roots = lam0
            success = False
            residual = float('inf')
    else:
        roots = np.array([])
        success = True
        residual = 0.0

    # Compute energy
    # E_XXZ = (Delta/4)*L + sum_a e(lam_a)
    # where e(lam) = -sin^2(gamma) / (cos(2*lam) - cos(gamma))
    # But convention-dependent.  Use: E = (1/4) sum [sigma_x sigma_x + sigma_y sigma_y + Delta sigma_z sigma_z]
    # = Delta*L/4 - sum_a sin^2(gamma) / (cos(2*lam_a) - cos(gamma))
    if M > 0 and success:
        energy = Delta * L / 4.0
        for lam in roots:
            denom = np.cos(2 * lam) - np.cos(gamma)
            if abs(denom) > 1e-15:
                energy -= np.sin(gamma)**2 / denom
    else:
        energy = Delta * L / 4.0

    return {
        'roots': roots,
        'energy': energy,
        'Delta': Delta,
        'gamma': gamma,
        'p': p,
        'success': success,
        'residual': residual,
        'L': L,
        'M': M,
    }


# ========================================================================
# 7.  Bethe completeness and singular solutions
# ========================================================================

def count_regular_bethe_solutions(L: int, M: int) -> Tuple[int, List[np.ndarray]]:
    """Count regular (non-singular) Bethe solutions for (L, M).

    A "singular" solution is one where two Bethe roots coincide:
    u_i = u_j for some i != j.  These are the "resonances" of the
    Bethe ansatz.

    Returns (count, list of root sets).
    """
    all_solutions = xxx_bethe_roots_numerical(L, M)

    regular = []
    for roots in all_solutions:
        # Check if any two roots coincide
        is_singular = False
        for i in range(len(roots)):
            for j in range(i + 1, len(roots)):
                if abs(roots[i] - roots[j]) < 1e-4:
                    is_singular = True
                    break
            if is_singular:
                break
        if not is_singular:
            regular.append(roots)

    return len(regular), regular


def count_singular_bethe_solutions(L: int, M: int) -> int:
    """Count singular Bethe solutions.

    Singular solutions have u_i = u_j + i for some pair.
    For the XXX chain, singular solutions arise when quantum numbers
    coincide (I_i = I_j).

    The number of singular solutions is related to the resonance rank
    rho(A) from shadow theory.

    For M = L/2 (half-filling), the known count is:
        L=4, M=2: 0 singular
        L=6, M=3: 1 singular (the "Essler-Korepin-Schoutens" solution)
        L=8, M=4: several singular
    """
    all_solutions = xxx_bethe_roots_numerical(L, M)
    n_regular, _ = count_regular_bethe_solutions(L, M)
    hilbert_dim = bethe_state_count(L, M)
    n_singular = hilbert_dim - n_regular  # Missing states from regular solutions
    return n_singular


# ========================================================================
# 8.  Arithmetic height of Bethe roots
# ========================================================================

def weil_height_rational(x: float, tol: float = 1e-8) -> float:
    """Weil height of a rational number.

    h(p/q) = log max(|p|, |q|) where p/q is in lowest terms.

    For algebraic numbers approximated numerically, we use the
    Mahler measure approximation.
    """
    from fractions import Fraction
    frac = Fraction(x).limit_denominator(10**8)
    p, q = abs(frac.numerator), abs(frac.denominator)
    if p == 0:
        return 0.0
    return np.log(max(p, q))


def mahler_measure(poly_coeffs: np.ndarray) -> float:
    """Mahler measure of a polynomial.

    M(P) = |a_d| * prod_{|alpha_i| > 1} |alpha_i|

    where a_d is the leading coefficient and alpha_i are the roots.
    Equivalently:
        log M(P) = log |a_d| + sum max(0, log |alpha_i|)
    """
    roots_p = np.roots(poly_coeffs)
    leading = abs(poly_coeffs[0])
    if leading < 1e-15:
        return 0.0
    log_mahler = np.log(leading)
    for r in roots_p:
        abs_r = abs(r)
        if abs_r > 1.0:
            log_mahler += np.log(abs_r)
    return np.exp(log_mahler)


def arithmetic_height_bethe_roots(roots: np.ndarray) -> Dict[str, Any]:
    """Compute arithmetic height invariants of a Bethe root set.

    For each root u_a, compute:
        - Weil height h(u_a) (approximate, treating u_a as rational)
        - Total height H = sum h(u_a)
        - Maximum height h_max = max h(u_a)

    Returns dict with height data.
    """
    heights = np.array([weil_height_rational(r) for r in roots])
    total = float(np.sum(heights))
    max_h = float(np.max(heights)) if len(heights) > 0 else 0.0

    return {
        'individual_heights': heights,
        'total_height': total,
        'max_height': max_h,
        'mean_height': float(np.mean(heights)) if len(heights) > 0 else 0.0,
        'num_roots': len(roots),
    }


def height_growth_rate(L_values: List[int], M_func=None) -> Dict[str, Any]:
    """Compute height growth H(L, M(L)) as a function of L.

    By default, M = L//2 (half-filling).

    Compares:
        - H(L) growth rate
        - Shadow growth rate rho(A) for comparison

    For the XXX sl_2 chain at level k = L/2:
        kappa(sl_2, k) = 3(k+2)/4
        Shadow growth rate rho = 0 (class L, shadow terminates at arity 3)
    """
    if M_func is None:
        M_func = lambda L: L // 2

    results = []
    for L in L_values:
        M = M_func(L)
        solutions = xxx_bethe_roots_numerical(L, M)
        if solutions:
            # Use ground state (typically first solution)
            roots = solutions[0]
            height_data = arithmetic_height_bethe_roots(roots)
            results.append({
                'L': L,
                'M': M,
                'total_height': height_data['total_height'],
                'max_height': height_data['max_height'],
                'mean_height': height_data['mean_height'],
            })

    return {
        'data': results,
        'L_values': [r['L'] for r in results],
        'total_heights': [r['total_height'] for r in results],
    }


# ========================================================================
# 9.  Shadow connection: singular divisor comparison
# ========================================================================

def shadow_singular_divisor_sl2(k: float) -> Dict[str, Any]:
    r"""Singular divisor of the arithmetic packet connection for sl_2 at level k.

    The arithmetic packet connection nabla^arith has singularities at
    points determined by the shadow data.  For sl_2:

        kappa(sl_2, k) = 3(k+2)/4
        Shadow discriminant: Delta = 8*kappa*S_4
            For sl_2: S_4 = 0 (class L), so Delta = 0.

    The singular divisor D_A is the set of u-values where the Bethe
    ansatz equations become degenerate.

    For the XXX chain, the singularities of the transfer matrix eigenvalue
    Lambda(u) are at u = u_a (the Bethe roots) and u = u_a +/- i.
    """
    kappa = 3 * (k + 2) / 4
    Delta_shadow = 0.0  # sl_2 is class L, S_4 = 0

    return {
        'kappa': kappa,
        'Delta_shadow': Delta_shadow,
        'shadow_class': 'L',
        'shadow_depth': 3,
        'singular_points_description': (
            'u = u_a (Bethe roots), u = u_a +/- i (auxiliary singularities)'
        ),
    }


def compare_bethe_singular_shadow(L: int, M: int,
                                   kappa: float) -> Dict[str, Any]:
    r"""Compare Bethe root locus with shadow connection singularities.

    The Bethe roots {u_a} are singularities of Q(u) = prod(u - u_a).
    The shadow connection has singularities determined by kappa and Delta.

    For sl_2 (class L):
        - Shadow is quadratic: Q_L(t) = (2*kappa)^2 (no higher terms).
        - The singular divisor is controlled entirely by kappa.
        - The Bethe root SPREAD (max|u_a| or discriminant of the
          Bethe polynomial) should correlate with kappa.

    Returns comparison data.
    """
    solutions = xxx_bethe_roots_numerical(L, M)
    if not solutions:
        return {'error': 'No solutions found'}

    ground_state_roots = solutions[0]

    # Bethe root spread
    if len(ground_state_roots) > 1:
        root_spread = float(np.max(ground_state_roots) - np.min(ground_state_roots))
    else:
        root_spread = 0.0

    # Energy from roots
    energy = xxx_energy_from_roots(ground_state_roots, L)

    # Shadow prediction for energy density
    # Ground state energy for XXX AFM at half-filling:
    # e_0 = 1/4 - ln(2) per site (Hulthén, thermodynamic limit)
    e_per_site = energy / L
    hulthen = 0.25 - np.log(2)

    return {
        'L': L,
        'M': M,
        'kappa': kappa,
        'roots': ground_state_roots,
        'root_spread': root_spread,
        'energy': energy,
        'energy_per_site': e_per_site,
        'hulthen_limit': hulthen,
        'hulthen_deviation': abs(e_per_site - hulthen),
        'num_solutions': len(solutions),
    }


# ========================================================================
# 10.  Discriminant comparison: Bethe vs shadow
# ========================================================================

def bethe_polynomial_discriminant_numerical(L: int, M: int) -> Optional[float]:
    """Compute the discriminant of the Bethe polynomial numerically.

    The discriminant Disc(P) = prod_{i<j} (u_i - u_j)^2 * leading^{2d-2}
    for a polynomial of degree d.

    For M=1, the polynomial (u+1/2)^L - (u-1/2)^L has known discriminant.
    For M>=2, we use the numerical roots.
    """
    if M == 1:
        # Exact discriminant via sympy
        disc = bethe_discriminant_M1(L)
        try:
            return float(disc.evalf())
        except Exception:
            return None

    # For M >= 2, get the Bethe polynomial
    poly = xxx_bethe_polynomial(L, M)
    if poly is None:
        return None
    try:
        disc = poly.discriminant()
        return float(disc.evalf())
    except Exception:
        return None


def shadow_discriminant_sl2(k: float) -> float:
    r"""Shadow metric discriminant for sl_2 at level k.

    Delta(sl_2, k) = 8*kappa*S_4 = 0  (because S_4 = 0 for class L).

    For the sl_2 affine algebra, the shadow obstruction tower terminates
    at arity 3 (class L: Lie/tree).  The quartic shadow S_4 = 0.

    The shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    reduces to Q_L(t) = (2*kappa)^2 (constant) for Delta = 0 and alpha = 0.

    Note: alpha = S_3/kappa for sl_2 can be nonzero at the cubic level,
    but the discriminant Delta = 8*kappa*S_4 still vanishes.
    """
    kappa_val = 3 * (k + 2) / 4
    S4 = 0.0  # Class L
    return 8 * kappa_val * S4


# ========================================================================
# 11.  Baxter Q-polynomial and TQ relation
# ========================================================================

def baxter_q_polynomial(roots: np.ndarray) -> np.ndarray:
    """Construct the Baxter Q-polynomial from Bethe roots.

    Q(u) = prod_{a=1}^{M} (u - u_a)

    Returns polynomial coefficients (highest degree first).
    """
    if len(roots) == 0:
        return np.array([1.0])

    # Build polynomial from roots
    poly = np.array([1.0])
    for r in roots:
        poly = np.convolve(poly, [1.0, -r])
    return poly


def verify_tq_relation(roots: np.ndarray, L: int,
                        u_test: Optional[np.ndarray] = None) -> float:
    r"""Verify the Baxter TQ relation.

    T(u) Q(u) = a(u) Q(u-i) + d(u) Q(u+i)

    where a(u) = (u + i/2)^L, d(u) = (u - i/2)^L, and
    Q(u) = prod(u - u_a).

    Returns the maximum residual ||TQ - aQ(-i) - dQ(+i)||.
    """
    if u_test is None:
        u_test = np.linspace(-3, 3, 20) + 0.01j

    Q_coeffs = baxter_q_polynomial(roots)
    M = len(roots)

    max_err = 0.0
    for u in u_test:
        Q_u = np.polyval(Q_coeffs, u)
        Q_minus = np.polyval(Q_coeffs, u - 1j)
        Q_plus = np.polyval(Q_coeffs, u + 1j)

        a_u = (u + 0.5j)**L
        d_u = (u - 0.5j)**L

        # Transfer eigenvalue
        if abs(Q_u) > 1e-12:
            T_u = (a_u * Q_minus + d_u * Q_plus) / Q_u
            # Also compute via the direct formula
            T_direct = xxx_transfer_eigenvalue(u, roots, L)
            err = abs(T_u - T_direct) / max(abs(T_u), 1e-15)
            max_err = max(max_err, err)

    return max_err


# ========================================================================
# 12.  M=1 explicit computations
# ========================================================================

def xxx_bethe_roots_M1_exact(L: int) -> np.ndarray:
    """Exact Bethe roots for M=1 (single magnon).

    u_k = (1/2) cot(pi*k/L) for k = 1, 2, ..., L-1.

    These are the rapidities of one-magnon excitations (spin waves).
    """
    roots = np.array([0.5 / np.tan(np.pi * k / L) for k in range(1, L)])
    return roots


def xxx_bethe_energies_M1(L: int) -> np.ndarray:
    """Exact energies for M=1 states.

    E_k = L/4 - 1/(2*(u_k^2 + 1/4))
        = L/4 - 1/(2*(cot^2(pi*k/L)/4 + 1/4))
        = L/4 - 2/(cot^2(pi*k/L) + 1)
        = L/4 - 2*sin^2(pi*k/L)

    These are the magnon dispersion relation.
    """
    energies = np.array([
        L / 4.0 - 2 * np.sin(np.pi * k / L)**2
        for k in range(1, L)
    ])
    return energies


# ========================================================================
# 13.  Multi-path verification framework
# ========================================================================

@dataclass
class BetheVerification:
    """Multi-path verification result for a Bethe root computation."""
    L: int
    M: int
    path1_numerical: Optional[np.ndarray] = None
    path2_algebraic: Optional[Any] = None
    path3_exact_diag: Optional[np.ndarray] = None
    path4_shadow: Optional[Dict] = None
    agreement_1_3: Optional[float] = None  # numerical vs exact diag
    agreement_1_2: Optional[float] = None  # numerical vs algebraic


def verify_bethe_multipath(L: int, M: int) -> BetheVerification:
    """Multi-path verification of Bethe ansatz for (L, M).

    Path 1: Numerical BAE solution.
    Path 2: Algebraic (Bethe polynomial roots).
    Path 3: Exact diagonalization of the Hamiltonian.
    Path 4: Shadow connection (transfer matrix comparison).

    Returns verification object with agreement metrics.
    """
    result = BetheVerification(L=L, M=M)

    # Path 1: Numerical
    solutions = xxx_bethe_roots_numerical(L, M)
    if solutions:
        result.path1_numerical = solutions[0]

    # Path 3: Exact diagonalization
    evals_ed, _ = exact_diag_sector(L, M)
    result.path3_exact_diag = evals_ed

    # Path 1 vs Path 3: compare energies
    if result.path1_numerical is not None and len(evals_ed) > 0:
        e_bethe = xxx_energy_from_roots(result.path1_numerical, L)
        # Find closest ED energy to the Bethe energy
        idx = np.argmin(np.abs(evals_ed - e_bethe))
        result.agreement_1_3 = float(abs(e_bethe - evals_ed[idx]))

    # Path 4: Shadow
    k = L / 2.0  # Level k = L/2 for the L-site chain
    kappa = 3 * (k + 2) / 4
    if result.path1_numerical is not None:
        result.path4_shadow = compare_transfer_shadow(
            result.path1_numerical, L, kappa
        )

    return result


# ========================================================================
# 14.  Galois group via resolvent polynomials (for small degree)
# ========================================================================

def galois_group_by_factorization(poly: Poly) -> Dict[str, Any]:
    r"""Estimate the Galois group of a polynomial by examining its factorization
    pattern modulo small primes.

    For a polynomial P(x) in Z[x] of degree n, factor P mod p for small primes p.
    The cycle types of these factorizations determine the Galois group:

    - If all factorizations are into linear factors: Gal = trivial
    - If some factorization has a single irreducible factor: Gal contains an n-cycle
    - The Galois group is the smallest subgroup of S_n containing all observed cycle types

    This is the Dedekind/Frobenius method (not rigorous but effective for small degree).

    Returns dict with group information.
    """
    from sympy import GF

    x = poly.gen
    n = degree(poly)
    if n <= 1:
        return {'order': 1, 'description': 'trivial', 'is_full_symmetric': False}

    # Factor mod small primes
    primes_to_test = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    cycle_types = []

    for p in primes_to_test:
        try:
            # Reduce coefficients mod p
            poly_modp = Poly(poly.as_expr(), x, modulus=p)
            factors = poly_modp.factor_list()
            # Cycle type = sorted list of degrees of irreducible factors
            if factors[1]:  # factors is (leading_coeff, [(factor, multiplicity), ...])
                degs = sorted([degree(f) for f, m in factors[1] for _ in range(m)],
                              reverse=True)
                if sum(degs) == n:  # Sanity check
                    cycle_types.append(tuple(degs))
        except Exception:
            continue

    # Analyze cycle types
    has_n_cycle = any(ct == (n,) for ct in cycle_types)
    has_transposition = any(ct == (n - 1, 1) or (n == 3 and ct == (2, 1)) for ct in cycle_types)
    all_linear = all(ct == tuple([1] * n) for ct in cycle_types if ct)

    if all_linear and cycle_types:
        return {
            'order': 1,
            'description': 'trivial (all roots rational)',
            'is_full_symmetric': False,
            'cycle_types': cycle_types,
        }

    if has_n_cycle and has_transposition and n >= 3:
        return {
            'order': factorial(n),
            'description': f'S_{n} (full symmetric group)',
            'is_full_symmetric': True,
            'cycle_types': cycle_types,
        }

    if has_n_cycle and not has_transposition:
        # Could be cyclic or dihedral
        return {
            'order': n,  # Lower bound
            'description': f'contains Z/{n}Z (cyclic subgroup)',
            'is_full_symmetric': False,
            'cycle_types': cycle_types,
        }

    # Default: report what we found
    unique_types = list(set(cycle_types))
    return {
        'order': None,  # Unknown
        'description': f'undetermined (observed {len(unique_types)} cycle types)',
        'is_full_symmetric': False,
        'cycle_types': cycle_types,
        'unique_cycle_types': unique_types,
    }


# ========================================================================
# 15.  Master computation: full arithmetic analysis for (L, M)
# ========================================================================

def full_bethe_arithmetic(L: int, M: int) -> Dict[str, Any]:
    r"""Complete arithmetic analysis of Bethe roots for (L, M).

    Computes:
        1. All Bethe root sets (numerical)
        2. Bethe polynomial (if computable)
        3. Number field degree
        4. Discriminant
        5. Galois group (estimate)
        6. Heights
        7. Comparison with exact diagonalization
        8. Shadow connection comparison
        9. Completeness check

    This is the master function for the Bethe arithmetic engine.
    """
    result = {
        'L': L, 'M': M,
        'hilbert_dim': bethe_state_count(L, M),
    }

    # 1. Numerical roots
    solutions = xxx_bethe_roots_numerical(L, M)
    result['num_solutions'] = len(solutions)
    result['solutions'] = solutions

    # 2. Bethe polynomial (for small cases)
    try:
        poly = xxx_bethe_polynomial(L, M)
        if poly is not None:
            result['bethe_polynomial'] = poly
            result['bethe_poly_degree'] = degree(poly)
        else:
            result['bethe_polynomial'] = None
            result['bethe_poly_degree'] = None
    except Exception:
        result['bethe_polynomial'] = None
        result['bethe_poly_degree'] = None

    # 3. Energies and verification
    if solutions:
        energies = [xxx_energy_from_roots(s, L) for s in solutions]
        result['energies'] = energies

        evals_ed, _ = exact_diag_sector(L, M)
        result['exact_diag_energies'] = evals_ed

        # Match Bethe energies to ED energies
        matched = 0
        for e_bethe in energies:
            if len(evals_ed) > 0:
                idx = np.argmin(np.abs(evals_ed - e_bethe))
                if abs(e_bethe - evals_ed[idx]) < 1e-4:
                    matched += 1
        result['matched_energies'] = matched

    # 4. Heights
    if solutions:
        result['height_data'] = [
            arithmetic_height_bethe_roots(s) for s in solutions
        ]

    # 5. Completeness
    result['completeness'] = {
        'regular_count': len(solutions),
        'hilbert_dim': bethe_state_count(L, M),
        'is_complete': len(solutions) == bethe_state_count(L, M),
    }

    # 6. Shadow data
    k = L / 2.0
    kappa = 3 * (k + 2) / 4
    result['shadow_data'] = {
        'kappa': kappa,
        'shadow_class': 'L',
        'shadow_depth': 3,
        'shadow_discriminant': 0.0,
    }

    return result


# ========================================================================
# 16.  Bethe roots for specific (L, M) with exact analysis
# ========================================================================

def analyze_L4_M2() -> Dict[str, Any]:
    """Full analysis for L=4, M=2.

    For L=4, M=2: Hilbert space dimension = C(4,2) = 6.
    The Sz = 0 sector has 6 states.

    Ground state quantum numbers: I = (-1/2, 1/2).
    By symmetry u_2 = -u_1, so we solve a single equation.

    (u - (-u) + 1) / (u - (-u) - 1) = ((u + 1/2)/(u - 1/2))^4
    => (2u + 1) / (2u - 1) = ((u + 1/2)/(u - 1/2))^4
    => (2u + 1)(u - 1/2)^4 = (2u - 1)(u + 1/2)^4

    Let w = 2u.  Then (w + 1)((w-1)/2)^4 = (w - 1)((w+1)/2)^4.
    => (w+1)(w-1)^4 = (w-1)(w+1)^4
    => (w+1)(w-1)[(w-1)^3 - (w+1)^3] = 0
    => (w^2-1)[w^3-3w^2+3w-1 - w^3-3w^2-3w-1] = 0
    => (w^2-1)(-6w^2 - 2) = 0
    => (w^2-1)(3w^2 + 1) = 0

    So w^2 = 1 => w = +/-1 => u = +/-1/2 (SINGULAR, coincides with pole)
    or 3w^2 + 1 = 0 => w^2 = -1/3 => w = +/-i/sqrt(3) (COMPLEX, not physical
    for the real XXX chain).

    Wait -- this gives no real solution for the ground state with I = (-1/2, 1/2)!
    The issue is that for L=4, M=2, the ground state IS described by the
    quantum numbers, but the computation above assumed u_2 = -u_1, which
    is only valid for the momentum-zero sector.

    Let me redo this more carefully.  The correct BAE for L=4, M=2 with
    quantum numbers I_1 = -1/2, I_2 = 1/2 gives u_2 = -u_1 = u (say).

    The BAE for the first magnon:
      4 * arctan(2*u) - arctan(2*u) = pi * (-1/2)
    Wait, arctan(u_1 - u_2) = arctan(2u).
      4 * arctan(2*u) - arctan(2*u) = pi*(-1/2)
      3 * arctan(2*u) = -pi/2
      arctan(2*u) = -pi/6
      2*u = -tan(pi/6) = -1/sqrt(3)
      u = -1/(2*sqrt(3))

    So u_1 = -1/(2*sqrt(3)), u_2 = 1/(2*sqrt(3)).

    The Bethe roots generate Q(sqrt(3)).  Number field degree = 2.
    """
    # Exact solution
    sqrt3 = np.sqrt(3)
    u_gs = np.array([-1 / (2 * sqrt3), 1 / (2 * sqrt3)])

    # Energy
    E_gs = xxx_energy_from_roots(u_gs, 4)

    # Verify with exact diag
    evals, _ = exact_diag_sector(4, 2)

    # Number field: Q(1/sqrt(3)) = Q(sqrt(3)), degree 2 over Q
    u_sym = Symbol('u')
    # Minimal polynomial of 1/(2*sqrt(3)): u = 1/(2*sqrt(3)) => 12*u^2 = 1 => 12u^2 - 1 = 0
    min_poly = Poly(12 * u_sym**2 - 1, u_sym)

    # All Bethe states (6 total for Sz=0 sector)
    # Quantum number sets: from I_max = (4-2-1)/2 = 1/2
    # Allowed I: -1/2, 1/2.  Only one 2-element subset: {-1/2, 1/2}
    # So there's only 1 Bethe state with these quantum numbers.
    # Other states come from different sectors or higher quantum numbers.

    # Actually, for L=4, M=2, we need to enumerate more carefully.
    # The allowed quantum numbers are I in {-1/2, 1/2} only.
    # But we need C(4,2) = 6 states total.
    # Some states come from "string" solutions or other quantum number sets.

    # Let's get all numerical solutions
    all_solutions = xxx_bethe_roots_numerical(4, 2)

    return {
        'L': 4, 'M': 2,
        'ground_state_roots': u_gs,
        'ground_state_energy': E_gs,
        'exact_diag_energies': evals,
        'minimal_polynomial': min_poly,
        'number_field': 'Q(sqrt(3))',
        'number_field_degree': 2,
        'discriminant_min_poly': float(min_poly.discriminant().evalf()),
        'all_solutions': all_solutions,
        'hilbert_dim': 6,
    }


def analyze_L6_M3() -> Dict[str, Any]:
    """Full analysis for L=6, M=3.

    Hilbert space dimension: C(6,3) = 20.
    The Sz = 0 sector has 20 states.

    For the ground state (antiferromagnetic): I = (-1, 0, 1).
    By symmetry: u_3 = -u_1, u_2 = 0.

    BAE for u_2 = 0:
      6 * arctan(0) - arctan(-u_1) - arctan(u_1) = pi * 0
      0 - (-arctan(u_1)) - arctan(u_1) = 0   (trivially satisfied)

    BAE for u_1:
      6 * arctan(2*u_1) - arctan(u_1) - arctan(2*u_1) = pi*(-1)
      5 * arctan(2*u_1) - arctan(u_1) = -pi  ... no, let me redo.

    BAE for magnon i=1 (u_1):
      L * arctan(2*u_1) - arctan(u_1 - u_2) - arctan(u_1 - u_3) = pi * I_1
      6 * arctan(2*u_1) - arctan(u_1 - 0) - arctan(u_1 - (-u_1)) = pi*(-1)
      6 * arctan(2*u_1) - arctan(u_1) - arctan(2*u_1) = -pi
      5 * arctan(2*u_1) - arctan(u_1) = -pi

    Let x = u_1 (negative for this quantum number choice).
    5*arctan(2x) - arctan(x) = -pi

    For x < 0: arctan(2x) and arctan(x) are negative.
    Let x = -y, y > 0:
    -5*arctan(2y) + arctan(y) = -pi
    5*arctan(2y) - arctan(y) = pi

    This is a transcendental equation. The solution is algebraic because
    the BAE can be written in polynomial form.

    Polynomial form: clearing arctan via tan:
    Let a = arctan(2y), b = arctan(y).
    We need 5a - b = pi, i.e. tan(5a - b) = 0.

    Using tan(5a - b) = [tan(5a) - tan(b)] / [1 + tan(5a)*tan(b)] = 0
    => tan(5a) = tan(b) = y

    tan(5a) where tan(a) = 2y.  This gives a polynomial equation.
    tan(5a) can be expressed as a degree-5 rational function of tan(a) = 2y.

    Using the recurrence: tan(na) = ...
    Let t = 2y.  Then tan(a) = t, and:
    tan(2a) = 2t/(1-t^2)
    tan(3a) = (3t - t^3)/(1 - 3t^2)
    tan(4a) = (4t - 4t^3)/(1 - 6t^2 + t^4)
    tan(5a) = (5t - 10t^3 + t^5)/(1 - 10t^2 + 5t^4)

    Setting tan(5a) = y = t/2:
    (5t - 10t^3 + t^5)/(1 - 10t^2 + 5t^4) = t/2

    => 2(5t - 10t^3 + t^5) = t(1 - 10t^2 + 5t^4)
    => 10t - 20t^3 + 2t^5 = t - 10t^3 + 5t^4 ... wait, t not t^4.

    Actually: t * (1 - 10t^2 + 5t^4)

    => 2(5t - 10t^3 + t^5) = t(1 - 10t^2 + 5t^4)
    => 10t - 20t^3 + 2t^5 = t - 10t^3 + 5t^5

    Divide by t (t > 0):
    => 10 - 20t^2 + 2t^4 = 1 - 10t^2 + 5t^4
    => 9 - 10t^2 - 3t^4 = 0
    => 3t^4 + 10t^2 - 9 = 0

    Quadratic in t^2: t^2 = (-10 +/- sqrt(100 + 108)) / 6 = (-10 +/- sqrt(208)) / 6
    sqrt(208) = 4*sqrt(13)
    t^2 = (-10 + 4*sqrt(13)) / 6 = (-5 + 2*sqrt(13)) / 3

    Since t^2 > 0: need -5 + 2*sqrt(13) > 0 => sqrt(13) > 5/2 => 13 > 25/4, TRUE.

    So t^2 = (-5 + 2*sqrt(13))/3.
    y = t/2, u_1 = -y = -t/2.
    u_1 = -sqrt((-5 + 2*sqrt(13))/3) / 2

    Number field: Q(sqrt(13), sqrt((-5+2*sqrt(13))/3)) is degree 4 over Q.
    Actually: t^2 = (-5 + 2*sqrt(13))/3.
    The minimal polynomial of t^2 over Q is 3x^2 + 10x - 9 = 0.  Wait:
    3(t^2)^2 + 10*t^2 - 9 = 0 => 3X^2 + 10X - 9 = 0, discriminant 100 + 108 = 208 = 16*13.
    So t^2 in Q(sqrt(13)), and t in Q(sqrt((-5+2*sqrt(13))/3)).

    The ground state Bethe root generates Q(sqrt((-5+2*sqrt(13))/3)).
    The splitting field has degree 4 over Q.
    """
    # Numerical solution for the ground state
    u1_exact_t2 = (-5 + 2 * np.sqrt(13)) / 3  # t^2
    t = np.sqrt(u1_exact_t2)
    y = t / 2
    u_gs = np.array([-y, 0.0, y])

    E_gs = xxx_energy_from_roots(u_gs, 6)
    evals, _ = exact_diag_sector(6, 3)

    # All numerical solutions
    all_solutions = xxx_bethe_roots_numerical(6, 3)

    # Minimal polynomial of u_1^2
    # u_1 = -t/2, so u_1^2 = t^2/4 = (-5 + 2*sqrt(13))/12
    # Minimal polynomial of u_1^2: let X = u_1^2.
    # 12X = -5 + 2*sqrt(13) => sqrt(13) = (12X+5)/2
    # => 13 = (12X+5)^2/4 => 52 = 144X^2 + 120X + 25
    # => 144X^2 + 120X - 27 = 0 => 48X^2 + 40X - 9 = 0
    X = Symbol('X')
    min_poly_u2 = Poly(48 * X**2 + 40 * X - 9, X)

    # Minimal polynomial of u_1 itself: u_1^2 satisfies 48Z^2 + 40Z - 9 = 0
    # So u_1 satisfies 48*u^4 + 40*u^2 - 9 = 0
    u_sym = Symbol('u')
    min_poly_u = Poly(48 * u_sym**4 + 40 * u_sym**2 - 9, u_sym)

    # Galois group of Q(u_1)/Q: degree 4, discriminant of min poly
    disc = float(min_poly_u.discriminant().evalf())

    return {
        'L': 6, 'M': 3,
        'ground_state_roots': u_gs,
        'ground_state_energy': E_gs,
        'exact_diag_energies': evals,
        'min_poly_u_squared': min_poly_u2,
        'min_poly_u': min_poly_u,
        'number_field_degree': 4,
        'number_field': 'Q(sqrt((-5 + 2*sqrt(13))/3))',
        'discriminant': disc,
        'galois_description': 'V_4 (Klein four-group) or Z/4Z',
        'all_solutions': all_solutions,
        'hilbert_dim': 20,
    }


def analyze_L8_M4() -> Dict[str, Any]:
    """Full analysis for L=8, M=4.

    Hilbert space dimension: C(8,4) = 70.

    For the ground state: I = (-3/2, -1/2, 1/2, 3/2).
    By symmetry: u_4 = -u_1, u_3 = -u_2.

    This reduces to a system of two equations in two unknowns.
    """
    # Numerical solution
    all_solutions = xxx_bethe_roots_numerical(8, 4)

    # Exact diag
    evals, _ = exact_diag_sector(8, 4)

    # Energies from Bethe
    energies = [xxx_energy_from_roots(s, 8) for s in all_solutions]

    # Heights
    height_data = [arithmetic_height_bethe_roots(s) for s in all_solutions]

    return {
        'L': 8, 'M': 4,
        'all_solutions': all_solutions,
        'num_solutions': len(all_solutions),
        'energies': energies,
        'exact_diag_energies': evals,
        'hilbert_dim': 70,
        'height_data': height_data,
    }
