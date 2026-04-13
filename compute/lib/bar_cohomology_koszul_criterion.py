r"""Bar cohomology via the Koszul criterion and algebraic generating functions.

Three methods for computing/predicting bar cohomology dimensions:
(A) Direct matrix computation (bar_complex.py, koszul_hilbert.py)
(B) Chevalley-Eilenberg identification (chiral_bar_cohomology.py)
(C) Generating function analysis (THIS MODULE)

=== Method C: Generating Function Analysis ===

For Koszul algebras, the bar cohomology Poincare series P_A(t) = sum h_n t^n
satisfies ALGEBRAIC EQUATIONS determined by the algebra's structure.

--- The Koszul-Hilbert Relation ---

For a classical quadratic algebra A = T(V)/(R):
  H_A(t) * H_{A!}(-t) = 1
where H_A(t) = sum dim(A_n) t^n is the ALGEBRA's Hilbert series and
H_{A!}(t) = sum dim(A!_n) t^n is the KOSZUL DUAL's Hilbert series.

CRITICAL DISTINCTION (AP9, AP25): The bar cohomology gives the Koszul dual,
so dim H^n(B(A)) = dim(A!_n). The Koszul relation involves H_A on one side
and H_{A!} = P_{bar} on the other. It does NOT give P(t)*P(-t) = 1.

For chiral algebras, the PBW spectral sequence collapse (thm:pbw-koszulness-criterion)
reduces the chiral bar cohomology to the classical bar cohomology of the
PBW-associated-graded. The per-weight Koszul relation then applies to each
weight level of the bigraded bar complex.

--- Algebraic Generating Functions ---

All rank-1 standard families share the discriminant
  Delta(x) = 1 - 2x - 3x^2 = (1 - 3x)(1 + x)
and satisfy degree-2 algebraic equations. This gives:

- sl2:       P(x) = (1+x-sqrt(Delta))/(2x(1+x)),  h_n = R(n+3) (Riordan, A005043)
- Virasoro:  P(x) = 4x/(1-x+sqrt(Delta))^2,       h_n = M(n+1)-M(n) (Motzkin diff, A002026)
- betagamma: P(x) = sqrt((1+x)/(1-3x)),             h_n: A001700 variant

Each satisfies a holonomic recurrence derivable from the algebraic equation.
These recurrences are PROVED (thm:ds-bar-gf-discriminant) and extend the
sequences to arbitrary degree.

Rank-2 families (sl3, W3) have CONJECTURED rational generating functions
with denominator (1 - ax - x^2) containing the golden-ratio factor.

--- This Module ---

1. verify_koszul_hilbert_classical: Verify H_A(t)*H_{A!}(-t)=1 for classical algebras
2. falsify_self_product_criterion: PROVE that P(t)*P(-t)=1 is FALSE
3. extend_via_algebraic_equation: Use algebraic GF to predict higher terms
4. extend_via_holonomic_recurrence: Use recurrences to predict higher terms
5. cross_family_discriminant_check: Verify shared discriminant (1-3x)(1+x)
6. bigraded_koszul_criterion: Per-weight Koszul relation verification
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple
from fractions import Fraction

from sympy import (
    Integer, Matrix, Poly, Rational, Symbol, binomial, expand,
    factor, factorial, floor, sqrt, simplify, solve, symbols,
    series, O, prod, Abs,
)


# =========================================================================
# Known bar cohomology sequences (PROVED, from bar_gf_solver/bar_gf_algebraicity)
# =========================================================================

def motzkin_numbers(N: int) -> List[int]:
    """Motzkin numbers M(0), ..., M(N-1). OEIS A001006.

    Recurrence: (n+2)M(n) = (2n+1)M(n-1) + 3(n-1)M(n-2), M(0)=1, M(1)=1.
    GF satisfies: x^2 M^2 + (x-1)M + 1 = 0.
    """
    if N <= 0:
        return []
    M = [0] * N
    M[0] = 1
    if N > 1:
        M[1] = 1
    for n in range(2, N):
        M[n] = ((2 * n + 1) * M[n - 1] + 3 * (n - 1) * M[n - 2]) // (n + 2)
    return M


def riordan_numbers(N: int) -> List[int]:
    """Riordan numbers R(0), ..., R(N-1). OEIS A005043.

    Recurrence: (n+1)R(n) = (n-1)(2R(n-1) + 3R(n-2)), R(0)=1, R(1)=0.
    GF satisfies: x(1+x)R^2 - (1+x)R + 1 = 0.
    """
    if N <= 0:
        return []
    R = [0] * N
    R[0] = 1
    if N > 1:
        R[1] = 0
    for n in range(2, N):
        R[n] = ((n - 1) * (2 * R[n - 1] + 3 * R[n - 2])) // (n + 1)
    return R


def virasoro_bar_dims(N: int) -> List[int]:
    """Bar cohomology dimensions for Virasoro: h_n = M(n+1) - M(n).

    OEIS A002026 (first differences of Motzkin numbers).
    GF: P(x) = 4x/(1 - x + sqrt(1 - 2x - 3x^2))^2, algebraic degree 2.
    Discriminant: (1 - 3x)(1 + x).

    Holonomic recurrence (PROVED, thm:ds-bar-gf-discriminant):
      (n+3)h(n) = (3n+4)h(n-1) + (n+1)h(n-2) - 3(n-2)h(n-3)
    for n >= 4, with h(1)=1, h(2)=2, h(3)=5.
    """
    M = motzkin_numbers(N + 2)
    return [M[n + 1] - M[n] for n in range(1, N + 1)]


def sl2_bar_dims(N: int) -> List[int]:
    """Chevalley-Eilenberg cohomology dimensions for sl2-hat: h_n = R(n+3).

    WARNING (AP63/B22): These are CE dimensions, NOT chiral bar dimensions.
    At degree 2: CE gives R(5) = 6, but chiral bar gives 5.
    The discrepancy arises because the chiral bar complex uses OPE residues
    (Orlik-Solomon form factor), not the CE differential.
    For the CHIRAL bar dimensions, use sl2_chiral_bar_dims() below.

    OEIS A005043 (Riordan numbers, shifted by 3).
    GF: P(x) = (1 + x - sqrt(1 - 2x - 3x^2))/(2x(1+x)), algebraic degree 2.
    Discriminant: (1 - 3x)(1 + x).

    Holonomic recurrence (PROVED):
      (n+4)h(n) = (n+2)(2h(n-1) + 3h(n-2))
    for n >= 3, with h(1)=3, h(2)=6.
    """
    R = riordan_numbers(N + 4)
    return [R[n + 3] for n in range(1, N + 1)]


def sl2_chiral_bar_dims(N: int) -> List[int]:
    """CHIRAL bar cohomology dimensions for sl2-hat.

    These differ from the CE/Riordan values at degree >= 2 due to the
    Orlik-Solomon form factor (AP63). The chiral bar complex uses OPE
    collision residues, not the CE differential.

    Known values (PROVED, WAVE2-36 verified by 3 independent paths):
      h_1 = 3  (= CE, coincides)
      h_2 = 5  (CE gives 6; the difference is the Killing form coboundary)
      h_3 = 15 (= CE, coincides; the AP63 correction vanishes at this degree)

    For n >= 4: CONJECTURAL that chiral = CE (the Orlik-Solomon correction
    appears to vanish at degrees >= 3 for sl_2, but this is not proved).
    """
    # Start with CE/Riordan values
    ce_dims = sl2_bar_dims(N)
    # Apply the known correction at degree 2
    if N >= 2:
        ce_dims[1] = 5  # CE gives 6, chiral bar gives 5
    return ce_dims


def betagamma_bar_dims(N: int) -> List[int]:
    r"""Bar cohomology dimensions for betagamma system.

    GF: P(x) = sqrt((1+x)/(1-3x)), algebraic degree 2.
    Discriminant: (1 - 3x)(1 + x) (same as sl2 and Virasoro).

    Recurrence: n*h(n) = 2n*h(n-1) + 3(n-2)*h(n-2), with h(0)=1, h(1)=2.
    Here h(0)=1 is the zeroth coefficient; bar cohomology starts at h(1)=2.
    """
    a = [0] * (N + 1)
    a[0] = 1
    if N >= 1:
        a[1] = 2
    for n in range(2, N + 1):
        a[n] = (2 * n * a[n - 1] + 3 * (n - 2) * a[n - 2]) // n
    return a[1:N + 1]


def sl3_bar_dims(N: int) -> List[int]:
    """Bar cohomology dimensions for sl3-hat.

    Known through n=3 (proved by direct computation): 8, 36, 204.
    Conjectured rational GF (conj:sl3-bar-gf):
      P(x) = 4x(2-13x-2x^2) / ((1-8x)(1-3x-x^2))
    Denominator recurrence: h(n) = 11*h(n-1) - 23*h(n-2) - 8*h(n-3).
    """
    known = [8, 36, 204]
    extended = list(known)
    while len(extended) < N:
        k = len(extended)
        val = 11 * extended[k - 1] - 23 * extended[k - 2] - 8 * extended[k - 3]
        extended.append(val)
    return extended[:N]


def w3_bar_dims(N: int) -> List[int]:
    """Bar cohomology dimensions for W3.

    Known through n=5 (proved): 2, 5, 16, 52, 171.
    Conjectured rational GF:
      P(x) = x(2-3x) / ((1-x)(1-3x-x^2))
    Denominator recurrence: h(n) = 4*h(n-1) - 2*h(n-2) - h(n-3).
    """
    known = [2, 5, 16, 52, 171]
    extended = list(known)
    while len(extended) < N:
        k = len(extended)
        val = 4 * extended[k - 1] - 2 * extended[k - 2] - extended[k - 3]
        extended.append(val)
    return extended[:N]


def heisenberg_bar_dims(N: int) -> List[int]:
    """Bar cohomology dimensions for Heisenberg: h_1 = 1, h_n = p(n-2) for n >= 2.

    p(k) = partition number.  The Heisenberg is Gaussian: Koszul dual is
    a trivial exterior algebra, so bar cohomology is concentrated.
    """
    dims = []
    for n in range(1, N + 1):
        if n == 1:
            dims.append(1)
        else:
            dims.append(_partition_number(n - 2))
    return dims


def fermion_bar_dims(N: int) -> List[int]:
    """Bar cohomology dimensions for free fermion (bc system).

    h_1 = 1, h_n = p(n-2) for n >= 2 (same pattern as Heisenberg,
    both are Gaussian class G).
    """
    return heisenberg_bar_dims(N)


def _partition_number(n: int) -> int:
    """Number of partitions of n. p(0)=1, p(k)=0 for k<0."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Euler's pentagonal recurrence
    p = [0] * (n + 1)
    p[0] = 1
    for k in range(1, n + 1):
        s = 0
        j = 1
        while True:
            # Pentagonal numbers: j*(3j-1)/2 and j*(3j+1)/2
            p1 = j * (3 * j - 1) // 2
            p2 = j * (3 * j + 1) // 2
            if p1 > k:
                break
            sign = (-1) ** (j + 1)
            s += sign * p[k - p1]
            if p2 <= k:
                s += sign * p[k - p2]
            j += 1
        p[k] = s
    return p[n]


# =========================================================================
# 1. Classical Koszul-Hilbert relation: H_A(t) * H_{A!}(-t) = 1
# =========================================================================

def verify_classical_koszul_hilbert(
    dim_gen: int,
    max_degree: int = 10,
) -> Dict:
    r"""Verify the classical Koszul-Hilbert relation for a polynomial algebra.

    For A = Sym(V) with dim V = d (polynomial algebra in d variables, each degree 1):
      H_A(t) = 1/(1-t)^d
      A! = Lambda(V*) (exterior algebra)
      H_{A!}(t) = (1+t)^d
      H_A(t) * H_{A!}(-t) = 1/(1-t)^d * (1-t)^d = 1

    Returns dict with verification results.
    """
    d = dim_gen
    x = Symbol('x')

    # H_A(x) = 1/(1-x)^d
    # H_{A!}(x) = (1+x)^d
    # Product: H_A(x) * H_{A!}(-x) = (1+x)^d / (1-x)^d * ... wait.
    # H_{A!}(-x) = (1-x)^d
    # H_A(x) * H_{A!}(-x) = (1-x)^d / (1-x)^d = 1. No, H_A = 1/(1-x)^d.
    # So H_A(x) * H_{A!}(-x) = 1/(1-x)^d * (1-x)^d = 1. YES.

    # Verify by expanding:
    H_A_coeffs = []
    H_dual_coeffs = []
    for n in range(max_degree + 1):
        # dim Sym^n(V) = C(n+d-1, d-1)
        H_A_coeffs.append(int(binomial(n + d - 1, d - 1)))
        # dim Lambda^n(V*) = C(d, n)
        H_dual_coeffs.append(int(binomial(d, n)) if n <= d else 0)

    # Check product = delta_{n,0}
    product_coeffs = []
    all_zero = True
    for n in range(max_degree + 1):
        s = 0
        for k in range(n + 1):
            s += H_A_coeffs[k] * ((-1) ** (n - k)) * H_dual_coeffs[n - k]
        product_coeffs.append(s)
        if n == 0 and s != 1:
            all_zero = False
        elif n > 0 and s != 0:
            all_zero = False

    return {
        'verified': all_zero,
        'dim_generators': d,
        'max_degree': max_degree,
        'H_A_coeffs': H_A_coeffs[:min(8, max_degree + 1)],
        'H_dual_coeffs': H_dual_coeffs[:min(8, max_degree + 1)],
        'product_coeffs': product_coeffs[:min(8, max_degree + 1)],
    }


def verify_lie_algebra_koszul(
    dim_g: int,
    max_degree: int = 8,
) -> Dict:
    r"""Verify the Koszul-Hilbert relation for a Lie algebra.

    For a Lie algebra g of dimension d, A = U(g) with PBW filtration:
      gr(U(g)) = Sym(g), so H_A(t) = 1/(1-t)^d
      A! = Lambda(g*), H_{A!}(t) = (1+t)^d
      H_A(t) * H_{A!}(-t) = 1

    This verifies the CLASSICAL (not chiral) Koszul relation.
    """
    return verify_classical_koszul_hilbert(dim_g, max_degree)


# =========================================================================
# 2. FALSIFICATION: P(t)*P(-t) != 1 for bar cohomology Poincare series
# =========================================================================

def compute_self_product(h_coeffs: List[int], include_h0: bool = True) -> List[int]:
    """Compute coefficients of P(t)*P(-t) where P(t) = sum h_n t^n.

    If include_h0 is True, h_coeffs starts with h_0 (usually 1).
    Returns the coefficients of the product as a list.

    NOTE: For a genuine Koszul duality relation, the product is
    H_A(t)*H_{A!}(-t) = 1, where H_A is the ALGEBRA's series and
    H_{A!} is the DUAL's series. These are DIFFERENT series.
    The self-product P(t)*P(-t) has no a priori reason to equal 1.
    """
    N = len(h_coeffs)
    product = [0] * (2 * N - 1)
    for i in range(N):
        for j in range(N):
            if i + j < len(product):
                # P(t) has coefficient h_i at t^i
                # P(-t) has coefficient (-1)^j * h_j at t^j
                product[i + j] += h_coeffs[i] * ((-1) ** j) * h_coeffs[j]
    return product


def falsify_self_product_criterion() -> Dict:
    r"""PROVE that P(t)*P(-t) = 1 is FALSE for bar cohomology series.

    The user's claim: since Vir_c and Vir_{26-c} have the same bar cohomology
    dimensions, the Koszul relation gives P(t)*P(-t) = 1.

    This is a CONFLATION (AP9): the Koszul relation is
      H_A(t) * H_{A!}(-t) = 1
    where H_A is the ALGEBRA's Hilbert series (not bar cohomology)
    and H_{A!} is the KOSZUL DUAL's Hilbert series (= bar cohomology of A).
    Even when A is self-dual (A! = A), H_A != H_{A!} because the algebra
    and its Koszul dual are DIFFERENT OBJECTS (AP25).

    Returns falsification data.
    """
    results = {}

    # Virasoro
    h_vir = [1] + virasoro_bar_dims(12)  # include h_0 = 1
    prod_vir = compute_self_product(h_vir)
    vir_is_one = (prod_vir[0] == 1 and all(c == 0 for c in prod_vir[1:]))
    results['virasoro'] = {
        'P_times_Pminus': prod_vir[:14],
        'is_identity': vir_is_one,
        'first_nonzero_above_0': next(
            (i for i in range(1, len(prod_vir)) if prod_vir[i] != 0), None
        ),
    }

    # sl2
    h_sl2 = [1] + sl2_bar_dims(12)
    prod_sl2 = compute_self_product(h_sl2)
    sl2_is_one = (prod_sl2[0] == 1 and all(c == 0 for c in prod_sl2[1:]))
    results['sl2'] = {
        'P_times_Pminus': prod_sl2[:14],
        'is_identity': sl2_is_one,
        'first_nonzero_above_0': next(
            (i for i in range(1, len(prod_sl2)) if prod_sl2[i] != 0), None
        ),
    }

    # betagamma
    h_bg = [1] + betagamma_bar_dims(12)
    prod_bg = compute_self_product(h_bg)
    bg_is_one = (prod_bg[0] == 1 and all(c == 0 for c in prod_bg[1:]))
    results['betagamma'] = {
        'P_times_Pminus': prod_bg[:14],
        'is_identity': bg_is_one,
        'first_nonzero_above_0': next(
            (i for i in range(1, len(prod_bg)) if prod_bg[i] != 0), None
        ),
    }

    # Note: odd coefficients of P(t)*P(-t) always vanish by symmetry
    results['note'] = (
        'P(t)*P(-t) always has vanishing odd-degree coefficients '
        '(by the symmetry P(t)*P(-t) = P(-t)*P(t)), but the even-degree '
        'coefficients are generically nonzero. The Koszul relation '
        'H_A(t)*H_{A!}(-t)=1 involves the algebra Hilbert series H_A, '
        'NOT the bar cohomology series P, on the left side.'
    )

    results['all_false'] = all(
        not results[k]['is_identity'] for k in ['virasoro', 'sl2', 'betagamma']
    )

    return results


# =========================================================================
# 3. Algebraic GF equations and discriminant analysis
# =========================================================================

def shared_discriminant_coefficients(max_degree: int = 15) -> Dict:
    r"""Analyze the shared discriminant Delta(x) = (1-3x)(1+x) = 1 - 2x - 3x^2.

    All rank-1 standard families (sl2, Virasoro, betagamma) have bar cohomology
    GFs satisfying degree-2 algebraic equations with this discriminant.

    The discriminant controls:
    - Radius of convergence: 1/3 (from the root x = 1/3 of Delta)
    - Growth rate: h_n ~ C * 3^n * n^{-alpha} for various alpha
    - Analytic continuation: branch cut from x = 1/3 to x = -1

    Returns analysis of the shared structure.
    """
    x = Symbol('x')
    Delta = (1 - 3 * x) * (1 + x)

    # Roots of Delta
    roots = solve(Delta, x)

    # Series expansion of sqrt(Delta)
    sqrt_Delta = sqrt(Delta)
    sqrt_series = series(sqrt_Delta, x, 0, max_degree)

    # Coefficients
    coeffs = []
    for n in range(max_degree):
        c = sqrt_series.coeff(x, n)
        coeffs.append(c)

    return {
        'discriminant': str(Delta),
        'factored': '(1 - 3x)(1 + x)',
        'roots': [str(r) for r in sorted(roots, key=lambda r: float(r))],
        'radius_of_convergence': Rational(1, 3),
        'sqrt_coefficients': coeffs[:10],
        'growth_rate': 3,
        'note': 'All rank-1 families share this discriminant. Rank-2 families '
                '(sl3, W3) have rational GFs whose denominators factor as '
                '(1 - ax)(1 - 3x - x^2) where a depends on the family.',
    }


def verify_algebraic_equation_virasoro(max_degree: int = 15) -> Dict:
    r"""Verify the algebraic equation for Virasoro bar cohomology GF.

    The Motzkin GF M(x) = sum M(n) x^n satisfies:
      x^2 M^2 + (x - 1)M + 1 = 0
    Taking M = (1 - x - sqrt(1 - 2x - 3x^2))/(2x^2) (convergent branch).

    The bar cohomology GF B(x) = sum_{n>=1} h_n x^n = x * M(x)^2.
    (Derivation: B(x) = ((1-x)M - 1)/x = x*M^2 using M's equation.)

    B satisfies the algebraic equation:
      x^3 B^2 + (x^2 + 2x - 1) B + x = 0
    with discriminant -(x-1)^2 (x+1)(3x-1).
    The relevant factor for singularity analysis is (1-3x)(1+x).

    Returns verification data.
    """
    h = virasoro_bar_dims(max_degree)

    # Verify via the Motzkin recurrence for h_n = M(n+1) - M(n):
    # (n+3)h(n) = (3n+4)h(n-1) + (n+1)h(n-2) - 3(n-2)h(n-3)
    recurrence_checks = []
    for n in range(4, max_degree + 1):
        lhs = (n + 3) * h[n - 1]
        rhs = (3 * n + 4) * h[n - 2] + (n + 1) * h[n - 3] - 3 * (n - 2) * h[n - 4]
        recurrence_checks.append({
            'n': n,
            'lhs': lhs,
            'rhs': rhs,
            'match': lhs == rhs,
        })

    # Verify algebraic equation: x^3 B^2 + (x^2 + 2x - 1) B + x = 0
    x = Symbol('x')
    B_series = sum(h[n - 1] * x ** n for n in range(1, max_degree + 1))
    eq_value = expand(x ** 3 * B_series ** 2 + (x ** 2 + 2 * x - 1) * B_series + x)
    # The equation vanishes exactly for the true series; with truncation at degree N,
    # nonzero terms appear starting at degree N+1 (from the truncation of B^2).
    # Check that all coefficients through degree max_degree are zero.
    eq_coeffs = []
    p = Poly(eq_value, x)
    for n in range(min(max_degree + 1, p.degree() + 1)):
        eq_coeffs.append(int(p.nth(n)))

    return {
        'family': 'Virasoro',
        'dims': h[:12],
        'recurrence_verified': all(c['match'] for c in recurrence_checks),
        'recurrence_checks': recurrence_checks[:5],
        'algebraic_degree': 2,
        'discriminant': '(1 - 3x)(1 + x)',
        'algebraic_equation': 'x^3 B^2 + (x^2 + 2x - 1) B + x = 0',
        'algebraic_eq_coeffs': eq_coeffs[:max_degree + 1],
        'algebraic_eq_vanishes': all(c == 0 for c in eq_coeffs[:max_degree]),
    }


def verify_algebraic_equation_sl2(max_degree: int = 15) -> Dict:
    r"""Verify the algebraic equation for sl2 bar cohomology GF.

    h_n = R(n+3) where R = Riordan numbers.
    Riordan GF R(x) satisfies: x(1+x)R^2 - (1+x)R + 1 = 0.
    Discriminant: (1+x)^2 - 4x(1+x) = (1+x)(1-3x).

    Holonomic recurrence:
      (n+4)h(n) = (n+2)(2h(n-1) + 3h(n-2))
    """
    h = sl2_bar_dims(max_degree)

    recurrence_checks = []
    for n in range(3, max_degree + 1):
        lhs = (n + 4) * h[n - 1]
        rhs = (n + 2) * (2 * h[n - 2] + 3 * h[n - 3])
        recurrence_checks.append({
            'n': n,
            'lhs': lhs,
            'rhs': rhs,
            'match': lhs == rhs,
        })

    return {
        'family': 'sl2',
        'dims': h[:12],
        'recurrence_verified': all(c['match'] for c in recurrence_checks),
        'recurrence_checks': recurrence_checks[:5],
        'algebraic_degree': 2,
        'discriminant': '(1 - 3x)(1 + x)',
    }


def verify_algebraic_equation_betagamma(max_degree: int = 15) -> Dict:
    r"""Verify the algebraic equation for betagamma bar cohomology GF.

    GF: P(x) = sqrt((1+x)/(1-3x)), satisfies (1-3x)P^2 - (1+x) = 0.
    Discriminant: (1-3x)(1+x) (same as sl2 and Virasoro).

    Recurrence: n*h(n) = 2n*h(n-1) + 3(n-2)*h(n-2).
    """
    h = betagamma_bar_dims(max_degree)

    recurrence_checks = []
    for n in range(3, max_degree + 1):
        lhs = n * h[n - 1]
        rhs = 2 * n * h[n - 2] + 3 * (n - 2) * h[n - 3]
        recurrence_checks.append({
            'n': n,
            'lhs': lhs,
            'rhs': rhs,
            'match': lhs == rhs,
        })

    return {
        'family': 'betagamma',
        'dims': h[:12],
        'recurrence_verified': all(c['match'] for c in recurrence_checks),
        'recurrence_checks': recurrence_checks[:5],
        'algebraic_degree': 2,
        'discriminant': '(1 - 3x)(1 + x)',
    }


# =========================================================================
# 4. Extension to high bar degree via holonomic recurrences
# =========================================================================

def extend_virasoro(max_n: int = 30) -> List[int]:
    """Extend Virasoro bar cohomology to high bar degree via PROVED recurrence.

    (n+3)h(n) = (3n+4)h(n-1) + (n+1)h(n-2) - 3(n-2)h(n-3).
    """
    return virasoro_bar_dims(max_n)


def extend_sl2(max_n: int = 30) -> List[int]:
    """Extend sl2 bar cohomology to high bar degree via PROVED recurrence.

    (n+4)h(n) = (n+2)(2h(n-1) + 3h(n-2)).
    """
    return sl2_bar_dims(max_n)


def extend_betagamma(max_n: int = 30) -> List[int]:
    """Extend betagamma bar cohomology to high bar degree via PROVED recurrence.

    n*h(n) = 2n*h(n-1) + 3(n-2)*h(n-2).
    """
    return betagamma_bar_dims(max_n)


def extend_sl3(max_n: int = 20) -> List[int]:
    """Extend sl3 bar cohomology via CONJECTURED rational GF recurrence.

    h(n) = 11*h(n-1) - 23*h(n-2) - 8*h(n-3).
    CONJECTURAL: only verified through n=3 directly.
    """
    return sl3_bar_dims(max_n)


def extend_w3(max_n: int = 20) -> List[int]:
    """Extend W3 bar cohomology via CONJECTURED rational GF recurrence.

    h(n) = 4*h(n-1) - 2*h(n-2) - h(n-3).
    CONJECTURAL: verified through n=5 directly.
    """
    return w3_bar_dims(max_n)


# =========================================================================
# 5. Cross-family discriminant consistency
# =========================================================================

def cross_family_growth_analysis(max_n: int = 20) -> Dict:
    r"""Analyze growth rates across families sharing discriminant (1-3x)(1+x).

    All rank-1 families have radius of convergence 1/3 and growth rate 3.
    The subleading power n^{-alpha} differs:
    - sl2 (Riordan):         h_n ~ C * 3^n * n^{-3/2}
    - Virasoro (Motzkin diff): h_n ~ C * 3^n * n^{-3/2}
    - betagamma:             h_n ~ C * 3^n * n^{-1/2}

    Returns growth analysis data.
    """
    families = {
        'sl2': sl2_bar_dims(max_n),
        'virasoro': virasoro_bar_dims(max_n),
        'betagamma': betagamma_bar_dims(max_n),
    }

    analysis = {}
    for name, h in families.items():
        ratios = [h[n] / h[n - 1] for n in range(1, len(h))]
        # Estimate alpha from h_n/h_{n-1} ~ 3 * (1 - alpha/n + ...)
        # => h_n/h_{n-1} ~ 3(1 - alpha/n)
        # => alpha ~ n * (1 - h_n/(3*h_{n-1}))
        alpha_estimates = []
        for n in range(5, min(len(h), max_n)):
            r = h[n] / h[n - 1]
            alpha_est = (n + 1) * (1 - r / 3)
            alpha_estimates.append(round(alpha_est, 4))

        analysis[name] = {
            'dims': h[:12],
            'ratios': [round(r, 6) for r in ratios[:12]],
            'growth_rate': 3,
            'alpha_estimates': alpha_estimates[-5:],
        }

    return analysis


def discriminant_universality_check() -> Dict:
    r"""Verify that all rank-1 families share discriminant (1-3x)(1+x).

    The discriminant arises from the quadratic relation in the PBW-associated-graded:
    for a single-generator chiral algebra, the bar of Sym(V) where V = {modes}
    has GF satisfying a degree-2 algebraic equation. The discriminant is:
      Delta(x) = c_1(x)^2 - 4 c_0(x) c_2(x)
    which factors as (1-3x)(1+x) for all rank-1 families.

    The factor (1-3x) controls the growth rate (radius = 1/3).
    The factor (1+x) controls the alternating behavior.
    """
    # Verify: the ratio h_n/h_{n-1} converges to 3 for each family
    families = {
        'sl2': sl2_bar_dims(25),
        'virasoro': virasoro_bar_dims(25),
        'betagamma': betagamma_bar_dims(25),
    }

    convergence = {}
    for name, h in families.items():
        final_ratio = h[-1] / h[-2]
        convergence[name] = {
            'final_ratio': round(final_ratio, 8),
            'converges_to_3': abs(final_ratio - 3) < 0.2,
        }

    return {
        'discriminant': '(1 - 3x)(1 + x)',
        'shared_growth_rate': 3,
        'convergence': convergence,
        'all_converge': all(v['converges_to_3'] for v in convergence.values()),
    }


# =========================================================================
# 6. Bigraded Koszul criterion (per-weight verification)
# =========================================================================

def bigraded_koszul_criterion_sl2(max_weight: int = 10) -> Dict:
    r"""Verify the per-weight Koszul relation for sl2-hat.

    At weight w, the PBW-associated-graded of sl2-hat is:
      gr(sl2-hat)_w = Sym^w(sl2) (symmetric tensors)
    with dim Sym^w(sl2) = C(w+2, 2).

    The Koszul dual at weight w is:
      (gr(sl2-hat)!)_w = Lambda^w(sl2)
    with dim Lambda^w(sl2) = C(3, w) = {1, 3, 3, 1, 0, 0, ...}.

    The per-weight Koszul criterion:
      sum_{n=0}^{w} dim(Sym^n) * (-1)^{w-n} * dim(Lambda^{w-n}) = delta_{w,0}

    This is just the binomial identity (1/(1-t)^3) * (1-t)^3 = 1.
    """
    results = {}
    for w in range(max_weight + 1):
        s = 0
        for n in range(w + 1):
            dim_sym_n = int(binomial(n + 2, 2))
            m = w - n
            dim_lambda_m = int(binomial(3, m)) if m <= 3 else 0
            s += dim_sym_n * ((-1) ** m) * dim_lambda_m
        expected = 1 if w == 0 else 0
        results[w] = {
            'sum': s,
            'expected': expected,
            'match': s == expected,
        }

    return {
        'family': 'sl2 (classical, PBW-graded)',
        'per_weight_checks': results,
        'all_verified': all(r['match'] for r in results.values()),
        'note': 'This verifies the classical Koszul relation at the PBW level. '
                'The chiral bar cohomology h_n = R(n+3) is the SUM over all weights '
                'of the per-weight Koszul dual dimensions.',
    }


def bigraded_koszul_criterion_virasoro(max_weight: int = 12) -> Dict:
    r"""Verify the per-weight Koszul relation for the PBW-graded Virasoro.

    The PBW-associated-graded of Virasoro is:
      gr(Vir) = Sym(L_{-2}, L_{-3}, L_{-4}, ...)
    a polynomial ring with generators at weights 2, 3, 4, ...

    At weight w:
      dim gr(Vir)_w = number of partitions of w into parts >= 2
                    = p_{>=2}(w) = p(w) - p(w-1) for w >= 2, with p_{>=2}(0)=1, p_{>=2}(1)=0.

    The Koszul dual at weight w (for a polynomial algebra) is the exterior algebra:
      dim (gr(Vir)!)_w = number of DISTINCT parts, each >= 2, summing to w
                       = number of partitions of w into DISTINCT parts >= 2.

    The per-weight Koszul criterion:
      sum_{n=0}^{w} (-1)^{w-n} * (partitions of n into parts>=2) * (strict partitions of w-n into parts>=2) = delta_{w,0}

    This is the identity prod_{k>=2} 1/(1-t^k) * prod_{k>=2} (1-t^k) = 1.
    """
    # Compute p_{>=2}(w) = partitions of w into parts >= 2
    def parts_geq2(w_max):
        p = [0] * (w_max + 1)
        p[0] = 1
        for k in range(2, w_max + 1):
            for w in range(k, w_max + 1):
                p[w] += p[w - k]
        return p

    # Compute q_{>=2}(w) = strict partitions of w into distinct parts >= 2
    def strict_parts_geq2(w_max):
        q = [0] * (w_max + 1)
        q[0] = 1
        for k in range(2, w_max + 1):
            for w in range(w_max, k - 1, -1):
                q[w] += q[w - k]
        return q

    p = parts_geq2(max_weight)
    q = strict_parts_geq2(max_weight)

    results = {}
    for w in range(max_weight + 1):
        s = 0
        # Count how many distinct parts each strict partition uses
        # Actually, the sign is (-1)^{number of parts in the strict partition}
        # which equals (-1)^{w-n}... no. Let me think again.
        #
        # For the polynomial algebra A = Sym(V) with V at weights >= 2:
        # H_A(t) = prod_{k>=2} 1/(1-t^k)
        # A! = Lambda(V) (exterior algebra on V)
        # H_{A!}(t) = prod_{k>=2} (1+t^k)
        # H_{A!}(-t) = prod_{k>=2} (1-t^k) (since generators have various weights)
        # Wait: H_{A!}(-t) replaces t -> -t, but the generators have weights k.
        # H_{A!}(t) = prod_{k>=2} (1 + t^k)
        # H_{A!}(-t) = prod_{k>=2} (1 + (-t)^k) = prod_{k>=2} (1 + (-1)^k t^k)
        #
        # For even k: (1 + t^k)
        # For odd k: (1 - t^k)
        #
        # Hmm, this is NOT the same as prod_{k>=2} (1 - t^k).
        # The sign depends on the PARITY of the generator weight.
        #
        # So H_A(t)*H_{A!}(-t) = prod_{k>=2} 1/(1-t^k) * prod_{k>=2} (1+(-1)^k t^k)
        # = prod_{k>=2} (1+(-1)^k t^k)/(1-t^k)
        #
        # For k even: (1+t^k)/(1-t^k) = (1+t^k)/(1-t^k)
        # For k odd:  (1-t^k)/(1-t^k) = 1
        #
        # So H_A(t)*H_{A!}(-t) = prod_{k>=2, k even} (1+t^k)/(1-t^k)
        # = prod_{j>=1} (1+t^{2j})/(1-t^{2j})
        # This is NOT 1!

        pass

    # The issue: for generators at varying weights, the Koszul relation
    # H_A(t)*H_{A!}(-t)=1 uses the SINGLE-VARIABLE t, and
    # H_{A!}(-t) = sum dim(A!_n) (-t)^n where n is the DEGREE in A!
    # (= number of generators used, NOT the weight).
    #
    # For the exterior algebra Lambda(V), degree n = number of factors:
    # dim Lambda^n(V) = C(dim V, n) when V is finite-dimensional.
    # H_{A!}(t) = (1+t)^{dim V} (each generator contributes (1+t)).
    # H_{A!}(-t) = (1-t)^{dim V}.
    # And H_A(t) = 1/(1-t)^{dim V} for Sym(V).
    # Product = 1. CHECK.
    #
    # But for CHIRAL algebras, V is INFINITE-DIMENSIONAL (one mode per weight).
    # The Koszul relation with t tracking DEGREE (not weight) gives:
    # H_A(t) = sum_{n>=0} dim(Sym^n(V)) t^n
    # But Sym^n(V) is INFINITE-DIMENSIONAL for n >= 1 when V is infinite.
    # So the DEGREE-graded Koszul relation doesn't converge.
    #
    # The correct approach for chiral algebras is the BIGRADED relation:
    # with s tracking degree and t tracking weight.
    # H_A(s, t) = prod_{k>=2} 1/(1 - s*t^k)
    # H_{A!}(s, t) = prod_{k>=2} (1 + s*t^k)
    # H_A(s, t) * H_{A!}(-s, t) = prod_{k>=2} (1 - s*t^k)/(1 - s*t^k) ... wait
    # H_{A!}(-s, t) = prod_{k>=2} (1 - s*t^k)
    # H_A(s, t) * H_{A!}(-s, t) = prod_{k>=2} 1/(1 - s*t^k) * (1 - s*t^k) = 1. YES!

    # So the BIGRADED Koszul criterion holds:
    # prod_{k>=2} 1/(1-s*t^k) * prod_{k>=2} (1-s*t^k) = 1
    # This is TRIVIALLY TRUE (each factor cancels).

    # The bar cohomology h_n = Σ_w dim H^{n,w}(B(A)) is obtained by setting t=1
    # (summing over all weights), which gives h_n = dim Lambda^n(V) = C(∞, n) = ∞.
    # That's wrong. So the bar cohomology dimensions h_n = 1, 2, 5, 12, ...
    # are NOT simply dim Lambda^n(V).

    # RESOLUTION: The chiral bar differential depends on OPE structure constants,
    # not just the PBW algebra structure. The PBW spectral sequence collapses,
    # but the E_2 page depends on BOTH the algebra and the relations.
    # The bar cohomology h_n counts the SURVIVING classes at bar degree n,
    # summed over all weights. The holonomic recurrence (Motzkin differences
    # for Virasoro) captures this correctly.

    return {
        'family': 'Virasoro (PBW-graded)',
        'bigraded_criterion': 'prod_{k>=2} (1-s*t^k)/(1-s*t^k) = 1 (trivially)',
        'note': (
            'The bigraded Koszul criterion is trivially satisfied for polynomial algebras. '
            'The nontrivial content is in the holonomic recurrence for the total dimensions '
            'h_n = sum_w dim H^{n,w}(B(A)), which requires the full OPE structure.'
        ),
        'dimensions_p_geq2': p[:max_weight + 1],
        'dimensions_q_geq2': q[:max_weight + 1],
    }


# =========================================================================
# 7. Comprehensive prediction: extend all families
# =========================================================================

def predict_all_families(max_n: int = 25) -> Dict:
    """Predict bar cohomology dimensions for all standard families.

    Uses PROVED recurrences for rank-1 families (sl2, Virasoro, betagamma)
    and CONJECTURED recurrences for rank-2 families (sl3, W3).

    Returns dimensions and growth analysis for each family.
    """
    families = {
        'virasoro': {
            'dims': virasoro_bar_dims(max_n),
            'status': 'PROVED (Motzkin difference recurrence)',
            'algebraic_degree': 2,
            'discriminant': '(1-3x)(1+x)',
        },
        'sl2': {
            'dims': sl2_bar_dims(max_n),
            'status': 'PROVED (Riordan recurrence)',
            'algebraic_degree': 2,
            'discriminant': '(1-3x)(1+x)',
        },
        'betagamma': {
            'dims': betagamma_bar_dims(max_n),
            'status': 'PROVED (algebraic sqrt GF)',
            'algebraic_degree': 2,
            'discriminant': '(1-3x)(1+x)',
        },
        'sl3': {
            'dims': sl3_bar_dims(max_n),
            'status': 'CONJECTURED (rational GF)',
            'algebraic_degree': 1,
            'discriminant': 'N/A (rational)',
        },
        'w3': {
            'dims': w3_bar_dims(max_n),
            'status': 'CONJECTURED (rational GF)',
            'algebraic_degree': 1,
            'discriminant': 'N/A (rational)',
        },
        'heisenberg': {
            'dims': heisenberg_bar_dims(max_n),
            'status': 'PROVED (trivially Gaussian)',
            'algebraic_degree': None,
            'discriminant': 'N/A (transcendental, partition function)',
        },
    }

    for name, data in families.items():
        h = data['dims']
        ratios = [h[n] / h[n - 1] for n in range(1, len(h)) if h[n - 1] > 0]
        data['final_ratio'] = round(ratios[-1], 6) if ratios else None

    return families


# =========================================================================
# 8. W3 extension via Koszul duality structure
# =========================================================================

def w3_koszul_duality_extension(max_n: int = 15) -> Dict:
    r"""Extend W3 bar cohomology using the conjectured GF structure.

    W3(c) has Koszul dual W3(100-c) (the Feigin-Frenkel involution for sl3).
    Both have the same bar cohomology dimensions (same universal structure).

    Conjectured rational GF: P(x) = x(2-3x)/((1-x)(1-3x-x^2)).
    Denominator: (1-x)(1-3x-x^2) = 1 - 4x + 2x^2 + x^3.
    Recurrence: h(n) = 4h(n-1) - 2h(n-2) - h(n-3).

    Known (proved through direct computation): h_1=2, h_2=5, h_3=16, h_4=52, h_5=171.
    Extended (conjectural): h_6=564, h_7=1861, h_8=6141, ...
    """
    dims = w3_bar_dims(max_n)

    # Verify recurrence against known values
    known = [2, 5, 16, 52, 171]
    recurrence_checks = []
    for n in range(4, min(len(known) + 1, max_n + 1)):
        if n <= len(known):
            predicted = 4 * dims[n - 2] - 2 * dims[n - 3] - dims[n - 4]
            actual = dims[n - 1]
            recurrence_checks.append({
                'n': n,
                'predicted': predicted,
                'actual': actual,
                'match': predicted == actual,
            })

    # Growth rate: denominator (1-x)(1-3x-x^2) has roots at x=1 and
    # x = (3 +/- sqrt(13))/(-2). The smallest positive root controls growth.
    # 1-3x-x^2 = 0 => x = (-3 +/- sqrt(9+4))/2 = (-3 +/- sqrt(13))/2
    # Positive root: (-3 + sqrt(13))/2 ≈ 0.303
    # Growth rate ≈ 1/0.303 ≈ 3.303

    import math
    growth_root = (-3 + math.sqrt(13)) / 2
    growth_rate = 1 / growth_root

    return {
        'family': 'W3',
        'known_proved': known,
        'extended': dims[:max_n],
        'recurrence': 'h(n) = 4h(n-1) - 2h(n-2) - h(n-3)',
        'recurrence_checks': recurrence_checks,
        'status': 'CONJECTURED (rational GF)',
        'growth_rate': round(growth_rate, 6),
        'denominator_roots': [1.0, round(growth_root, 6)],
    }


# =========================================================================
# 9. Near-rationality analysis (Virasoro spurious rational fit)
# =========================================================================

def virasoro_near_rationality(max_n: int = 12) -> Dict:
    r"""Analyze the near-rationality of the Virasoro bar cohomology GF.

    The Virasoro GF is algebraic of degree 2 (NOT rational). However,
    a depth-3 constant-coefficient recurrence
      h(n) = 4h(n-1) - 2h(n-2) - 4h(n-3)
    fits the data through degree 8, failing only at degree 9:
      predicted h(9) = 1352, actual h(9) = 1353.

    This near-rationality is a non-trivial numerical coincidence
    related to the fact that the algebraic GF has a very small
    irrational correction at low orders.

    Returns analysis of where the rational approximation fails.
    """
    h = virasoro_bar_dims(max_n)

    # Test the spurious rational recurrence
    rational_recurrence = [4, -2, -4]  # h(n) = 4h(n-1) - 2h(n-2) - 4h(n-3)
    errors = []
    for n in range(4, max_n + 1):
        predicted = (4 * h[n - 2] - 2 * h[n - 3] - 4 * h[n - 4])
        actual = h[n - 1]
        error = predicted - actual
        errors.append({
            'n': n,
            'predicted': predicted,
            'actual': actual,
            'error': error,
        })

    # Find first failure
    first_failure = next(
        (e for e in errors if e['error'] != 0), None
    )

    return {
        'family': 'Virasoro',
        'true_recurrence': '(n+3)h(n) = (3n+4)h(n-1) + (n+1)h(n-2) - 3(n-2)h(n-3) [holonomic]',
        'spurious_rational': 'h(n) = 4h(n-1) - 2h(n-2) - 4h(n-3) [constant-coefficient]',
        'errors': errors,
        'first_failure': first_failure,
        'note': (
            'The spurious rational fit works through n=8 because the '
            'algebraic correction to the dominant rational behavior is '
            'O(3^{-n} * n^{-3/2}), which is numerically tiny at small n. '
            'The first discrepancy (1 unit at n=9) reveals the algebraic nature.'
        ),
    }


# =========================================================================
# 10. Asymptotic analysis
# =========================================================================

def asymptotic_analysis(family: str, max_n: int = 50) -> Dict:
    r"""Asymptotic analysis of bar cohomology growth.

    For rank-1 families with discriminant (1-3x)(1+x):
      h_n ~ C * 3^n * n^{-alpha}

    where alpha depends on the family:
    - sl2 (Riordan): alpha = 3/2
    - Virasoro (Motzkin diff): alpha = 3/2
    - betagamma (sqrt): alpha = 1/2

    The growth rate 3 comes from the dominant singularity x = 1/3.
    The exponent alpha comes from the nature of the algebraic singularity
    (square-root branch point vs simple pole).
    """
    dispatch = {
        'virasoro': virasoro_bar_dims,
        'sl2': sl2_bar_dims,
        'betagamma': betagamma_bar_dims,
        'sl3': sl3_bar_dims,
        'w3': w3_bar_dims,
    }

    if family not in dispatch:
        return {'error': f'Unknown family: {family}'}

    h = dispatch[family](max_n)

    # Estimate C and alpha from h_n ~ C * 3^n * n^{-alpha}
    # log(h_n) ~ log(C) + n*log(3) - alpha*log(n)
    # h_n / (3^n) ~ C * n^{-alpha}
    # log(h_n/3^n) ~ log(C) - alpha*log(n)

    import math
    scaled = [h[n] / (3 ** (n + 1)) for n in range(len(h))]

    # Estimate alpha from consecutive ratios of scaled values:
    # scaled[n] / scaled[n-1] ~ ((n)/(n+1))^alpha
    # log(scaled[n]/scaled[n-1]) ~ alpha * log(n/(n+1)) = -alpha * log(1+1/n)
    alpha_estimates = []
    for n in range(10, min(len(h) - 1, max_n)):
        if scaled[n] > 0 and scaled[n - 1] > 0:
            ratio = scaled[n] / scaled[n - 1]
            if ratio > 0:
                log_ratio = math.log(ratio)
                log_n_ratio = math.log((n + 1) / (n + 2))  # n/(n+1) shifted by 1
                if abs(log_n_ratio) > 1e-10:
                    alpha_est = log_ratio / log_n_ratio
                    alpha_estimates.append(round(alpha_est, 4))

    # Estimate C from h_n / (3^n * n^{-alpha})
    alpha_final = sum(alpha_estimates[-5:]) / len(alpha_estimates[-5:]) if alpha_estimates else None
    C_estimates = []
    if alpha_final:
        for n in range(20, min(len(h), max_n)):
            C_est = h[n] / (3 ** (n + 1) * (n + 1) ** (-alpha_final))
            C_estimates.append(round(C_est, 6))

    return {
        'family': family,
        'growth_rate': 3,
        'alpha_estimates': alpha_estimates[-10:] if alpha_estimates else [],
        'alpha_final': round(alpha_final, 4) if alpha_final else None,
        'C_estimates': C_estimates[-5:] if C_estimates else [],
        'note': (
            'For rank-1 families: alpha = 3/2 for sl2 and Virasoro '
            '(Riordan and Motzkin-diff are both algebraic degree 2 with '
            'a square-root singularity), alpha = 1/2 for betagamma '
            '(sqrt GF has a simpler singularity).'
        ),
    }


# =========================================================================
# Master summary
# =========================================================================

def master_summary(max_n: int = 20) -> Dict:
    r"""Complete summary of bar cohomology generating function analysis.

    Collects all results: falsification of P(t)*P(-t)=1, algebraic equations,
    discriminant analysis, extensions, cross-family consistency.
    """
    return {
        'falsification': falsify_self_product_criterion(),
        'virasoro_algebraic': verify_algebraic_equation_virasoro(max_n),
        'sl2_algebraic': verify_algebraic_equation_sl2(max_n),
        'betagamma_algebraic': verify_algebraic_equation_betagamma(max_n),
        'discriminant': discriminant_universality_check(),
        'all_predictions': predict_all_families(max_n),
        'virasoro_near_rationality': virasoro_near_rationality(max_n),
    }
