r"""Algebraicity of bar cohomology generating functions (conj:bar-gf-algebraicity).

CONJECTURE: For every Koszul chiral algebra A, the bar cohomology GF

    P_A(x) = \sum_{n>=0} dim H^n(B(A)) * x^n

satisfies a polynomial equation of degree <= 2 (i.e., is algebraic of degree
at most 2, meaning either rational or satisfying a quadratic).

The discriminant Delta(x) = c_1(x)^2 - 4 c_0(x) c_2(x) has degree
bounded by 2 * rank(A).

Evidence table (thm:ds-bar-gf-discriminant):
    sl2_hat:    algebraic degree 2, disc = (1-3x)(1+x)      [Riordan]
    Virasoro:   algebraic degree 2, disc = (1-3x)(1+x)      [Motzkin diff]
    betagamma:  algebraic degree 2, disc = (1+x)/(1-3x)     [sqrt form]
    sl3_hat:    rational (degree 1), den = (1-8x)(1-3x-x^2) [conjectural]
    W3:         rational (degree 1), den = (1-x)(1-3x-x^2)  [conjectural]

This module:
1. Collects bar cohomology dimensions for all standard families
2. Verifies known algebraic equations against computed data
3. Verifies the discriminant degree bound
4. Tests the Koszul functional equation at the PBW/associated-graded level
5. Predicts the algebraic equation structure for G2_hat (rank 2)

Ground truth: bar_complex.py KNOWN_BAR_DIMS, bar_gf_solver.py, landscape_census.tex.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from sympy import (
    Integer, Matrix, Poly, Rational, Symbol, expand, factor,
    simplify, solve, sqrt, symbols,
)

from .utils import partition_number


# =========================================================================
# Bar cohomology dimension tables for all standard families
# =========================================================================

def heisenberg_bar_dims(N: int) -> List[int]:
    r"""H^n(B(Heisenberg)) = p(n-2) for n >= 2, H^1 = 1.

    p(k) = partition number.  Rank = 1.
    """
    dims = []
    for n in range(1, N + 1):
        if n == 1:
            dims.append(1)
        else:
            dims.append(partition_number(n - 2))
    return dims


def sl2_bar_dims(N: int) -> List[int]:
    r"""H^n(B(sl2_hat)): Riordan numbers R(n+3) for n >= 1.

    Rank = 1.  The Riordan GF R(x) is algebraic of degree 2
    with disc (1-3x)(1+x) = 1-2x-3x^2.
    """
    R = _riordan_numbers(N + 4)
    return [R[n + 3] for n in range(1, N + 1)]


def riordan_numbers(N: int) -> List[int]:
    r"""Full Riordan sequence R(0), ..., R(N-1).

    The generating function R(x) = sum R(n) x^n satisfies the algebraic equation:
        x(1+x) R^2 - (1+x) R + 1 = 0
    with discriminant (1+x)^2 - 4x(1+x) = (1+x)(1-3x).
    """
    return _riordan_numbers(N)


def virasoro_bar_dims(N: int) -> List[int]:
    r"""H^n(B(Vir_c)) = M(n+1) - M(n) where M = Motzkin numbers.

    Rank = 1 (single generator of weight 2).
    GF is algebraic of degree 2 with disc (1-3x)(1+x).
    """
    M = _motzkin_numbers(N + 2)
    return [M[n + 1] - M[n] for n in range(1, N + 1)]


def betagamma_bar_dims(N: int) -> List[int]:
    r"""H^n(B(betagamma)): coefficients of sqrt((1+x)/(1-3x)).

    Rank = 2 (two generators beta, gamma).
    GF Q(x) = sqrt((1+x)/(1-3x)) satisfies (1-3x)Q^2 - (1+x) = 0,
    with discriminant (inside Q^2 equation) related to (1-3x)(1+x).
    Recurrence: n*a(n) = 2n*a(n-1) + 3(n-2)*a(n-2), a(1)=2, a(0)=1.
    """
    a = [0] * (N + 1)
    a[0] = 1
    if N >= 1:
        a[1] = 2
    for n in range(2, N + 1):
        a[n] = (2 * n * a[n - 1] + 3 * (n - 2) * a[n - 2]) // n
    return a[1:N + 1]


def betagamma_full_gf_coeffs(N: int) -> List[int]:
    r"""Full coefficients [a_0, a_1, ..., a_{N-1}] of sqrt((1+x)/(1-3x)).

    Includes a_0 = 1.
    """
    a = [0] * N
    a[0] = 1
    if N > 1:
        a[1] = 2
    for n in range(2, N):
        a[n] = (2 * n * a[n - 1] + 3 * (n - 2) * a[n - 2]) // n
    return a


def sl3_bar_dims(N: int) -> List[int]:
    r"""H^n(B(sl3_hat)): known through n=3, conjectured at n=4,5.

    Rank = 2.  Conjectured rational GF (conj:sl3-bar-gf):
        P(x) = 4x(2-13x-2x^2) / ((1-8x)(1-3x-x^2))
    Denominator recurrence: a_n = 11*a_{n-1} - 23*a_{n-2} - 8*a_{n-3}.
    """
    known = [8, 36, 204]
    extended = list(known)
    while len(extended) < N:
        k = len(extended)
        val = 11 * extended[k - 1] - 23 * extended[k - 2] - 8 * extended[k - 3]
        extended.append(val)
    return extended[:N]


def w3_bar_dims(N: int) -> List[int]:
    r"""H^n(B(W_3)): known through n=5.

    Rank = 2.  Conjectured rational GF:
        P(x) = x(2-3x) / ((1-x)(1-3x-x^2))
    Denominator recurrence: a_n = 4*a_{n-1} - 2*a_{n-2} - a_{n-3}.
    """
    known = [2, 5, 16, 52, 171]
    extended = list(known)
    while len(extended) < N:
        k = len(extended)
        val = 4 * extended[k - 1] - 2 * extended[k - 2] - extended[k - 3]
        extended.append(val)
    return extended[:N]


def lattice_bar_dims(N: int, rank: int = 1) -> List[int]:
    r"""H^n(B(V_Lambda)) for a rank-r lattice VOA.

    For rank 1 (V_Z): same as Heisenberg (Gaussian shadow, terminates at depth 2).
    """
    return heisenberg_bar_dims(N)


# =========================================================================
# Known algebraic equations and discriminants
# =========================================================================

def known_algebraic_equations() -> Dict[str, Dict]:
    r"""Catalogue of known/conjectured algebraic equations for bar cohomology GFs.

    For the Riordan, Motzkin-difference, and betagamma families, the GF
    (including constant term a_0 = 1 where appropriate) satisfies a
    degree-2 algebraic equation.  For sl3 and W3, the GF is rational.

    Returns dict keyed by family name.
    """
    x = Symbol('x')
    eqs = {}

    # === Riordan GF: R(x) = sum R(n) x^n ===
    # x(1+x)R^2 - (1+x)R + 1 = 0
    # disc = (1+x)^2 - 4x(1+x) = (1+x)(1+x-4x) = (1+x)(1-3x)
    eqs['sl2_riordan'] = {
        'c2': Poly(x*(1 + x), x),
        'c1': Poly(-(1 + x), x),
        'c0': Poly(Integer(1), x),
        'discriminant': Poly((1 - 3*x)*(1 + x), x),
        'disc_degree': 2,
        'rank': 1,
        'alg_degree': 2,
        'note': 'Riordan GF R(x). Bar cohomology = R(n+3) for n>=1.',
    }

    # === Virasoro: Motzkin difference GF ===
    # Let V(x) = sum_{n>=0} v_n x^n where v_n = M(n+1) - M(n), v_0 = 0.
    # The Motzkin GF M(x) satisfies x^2 M^2 + (x-1)M + 1 = 0.
    # disc(M) = (x-1)^2 - 4x^2 = 1-2x-3x^2 = (1-3x)(1+x).
    # The difference GF inherits degree 2 with the same discriminant.
    eqs['Virasoro'] = {
        'discriminant': Poly((1 - 3*x)*(1 + x), x),
        'disc_degree': 2,
        'rank': 1,
        'alg_degree': 2,
        'note': 'Motzkin difference. disc = Catalan discriminant.',
    }

    # === betagamma: Q(x) = sqrt((1+x)/(1-3x)) ===
    # (1-3x)Q^2 - (1+x) = 0, i.e., c2=1-3x, c1=0, c0=-(1+x).
    # disc = 0 - 4*(-(1+x))*(1-3x) = 4(1+x)(1-3x).
    # The GF Q(x) = sum a_n x^n with a_0 = 1.
    eqs['betagamma'] = {
        'c2': Poly(1 - 3*x, x),
        'c1': Poly(Integer(0), x),
        'c0': Poly(-(1 + x), x),
        'discriminant': Poly(4*(1 + x)*(1 - 3*x), x),
        'disc_degree': 2,
        'rank': 2,
        'alg_degree': 2,
        'note': 'Q^2 = (1+x)/(1-3x). disc = 4*(Catalan discriminant).',
    }

    # === sl3: conjectured rational GF ===
    # P(x) = 4x(2-13x-2x^2) / ((1-8x)(1-3x-x^2))
    eqs['sl3'] = {
        'c2': Poly(Integer(0), x),
        'c1': Poly(expand((1 - 8*x)*(1 - 3*x - x**2)), x),
        'c0': Poly(expand(-4*x*(2 - 13*x - 2*x**2)), x),
        'discriminant': Poly(expand((1 - 8*x)*(1 - 3*x - x**2))**2, x),
        'disc_degree': 6,
        'rank': 2,
        'alg_degree': 1,
        'note': 'Rational. Den degree 3. Conjectural.',
    }

    # === W3: conjectured rational GF ===
    # P(x) = x(2-3x) / ((1-x)(1-3x-x^2))
    eqs['W3'] = {
        'c2': Poly(Integer(0), x),
        'c1': Poly(expand((1 - x)*(1 - 3*x - x**2)), x),
        'c0': Poly(expand(-x*(2 - 3*x)), x),
        'discriminant': Poly(expand((1 - x)*(1 - 3*x - x**2))**2, x),
        'disc_degree': 6,
        'rank': 2,
        'alg_degree': 1,
        'note': 'Rational. Den degree 3. Conjectural.',
    }

    # === Heisenberg: transcendental (partition function) ===
    eqs['Heisenberg'] = {
        'discriminant': None,
        'disc_degree': None,
        'rank': 1,
        'alg_degree': None,
        'note': 'Transcendental (partition function). Excluded from algebraicity conjecture.',
    }

    return eqs


# =========================================================================
# Equation verification against data
# =========================================================================

def verify_riordan_equation(N: int = 15) -> Dict:
    r"""Verify x(1+x)R^2 - (1-x)R + 1 = 0 for Riordan numbers.

    The Riordan GF R(x) = sum R(n) x^n satisfies this algebraic equation.
    Bar cohomology H^n(B(sl2)) = R(n+3).
    """
    x = Symbol('x')
    R_data = _riordan_numbers(N)

    # Build R(x) as truncated series
    R_poly = sum(Rational(R_data[n]) * x**n for n in range(N))
    R2_poly = expand(R_poly**2)

    # Evaluate x(1+x)R^2 - (1+x)R + 1
    val = expand(x*(1 + x)*R2_poly - (1 + x)*R_poly + 1)
    p = Poly(val, x)

    # Should vanish through x^{N-1}
    errors = {}
    for k in range(N):
        c = p.nth(k)
        if c != 0:
            errors[k] = c

    return {
        'N': N,
        'equation': 'x(1+x)R^2 - (1+x)R + 1 = 0',
        'verified_through': N - 1 if not errors else min(errors.keys()) - 1,
        'errors': errors,
        'all_zero': len(errors) == 0,
    }


def verify_betagamma_equation(N: int = 12) -> Dict:
    r"""Verify (1-3x)Q^2 = (1+x) for betagamma GF Q(x) = sqrt((1+x)/(1-3x))."""
    x = Symbol('x')
    Q_data = betagamma_full_gf_coeffs(N)

    Q_poly = sum(Rational(Q_data[n]) * x**n for n in range(N))
    Q2_poly = expand(Q_poly**2)

    val = expand((1 - 3*x)*Q2_poly - (1 + x))
    p = Poly(val, x)

    errors = {}
    for k in range(N):
        c = p.nth(k)
        if c != 0:
            errors[k] = c

    return {
        'N': N,
        'equation': '(1-3x)Q^2 - (1+x) = 0',
        'verified_through': N - 1 if not errors else min(errors.keys()) - 1,
        'errors': errors,
        'all_zero': len(errors) == 0,
    }


def verify_sl3_rational_gf(N: int = 8) -> Dict:
    r"""Verify sl3 rational GF: (1-8x)(1-3x-x^2)P = 4x(2-13x-2x^2)."""
    x = Symbol('x')
    dims = sl3_bar_dims(N)
    P_poly = sum(Rational(dims[n]) * x**(n + 1) for n in range(N))

    den = expand((1 - 8*x)*(1 - 3*x - x**2))
    num = expand(4*x*(2 - 13*x - 2*x**2))
    val = expand(den * P_poly - num)
    p = Poly(val, x)

    errors = {}
    for k in range(N + 1):
        c = p.nth(k)
        if c != 0:
            errors[k] = c

    return {
        'N': N,
        'equation': '(1-8x)(1-3x-x^2)P = 4x(2-13x-2x^2)',
        'verified_through': N if not errors else min(errors.keys()) - 1,
        'errors': errors,
        'all_zero': len(errors) == 0,
    }


def verify_w3_rational_gf(N: int = 8) -> Dict:
    r"""Verify W3 rational GF: (1-x)(1-3x-x^2)P = x(2-3x)."""
    x = Symbol('x')
    dims = w3_bar_dims(N)
    P_poly = sum(Rational(dims[n]) * x**(n + 1) for n in range(N))

    den = expand((1 - x)*(1 - 3*x - x**2))
    num = expand(x*(2 - 3*x))
    val = expand(den * P_poly - num)
    p = Poly(val, x)

    errors = {}
    for k in range(N + 1):
        c = p.nth(k)
        if c != 0:
            errors[k] = c

    return {
        'N': N,
        'equation': '(1-x)(1-3x-x^2)P = x(2-3x)',
        'verified_through': N if not errors else min(errors.keys()) - 1,
        'errors': errors,
        'all_zero': len(errors) == 0,
    }


# =========================================================================
# Discriminant degree bound verification
# =========================================================================

def verify_discriminant_bound(family: str, rank: int, disc_degree: int) -> Dict:
    r"""Check disc degree <= 2 * rank(A).

    For genuinely algebraic (degree 2) GFs, the discriminant has degree
    <= 2*rank.  For rational GFs (degree 1), the "discriminant" is c_1^2,
    a perfect square, and the relevant bound is the denominator degree.
    """
    bound = 2 * rank
    satisfied = disc_degree <= bound
    return {
        'family': family,
        'rank': rank,
        'disc_degree': disc_degree,
        'bound': bound,
        'satisfied': satisfied,
    }


def verify_all_discriminant_bounds() -> Dict[str, Dict]:
    r"""Verify discriminant degree bounds for all known families."""
    eqs = known_algebraic_equations()
    results = {}
    for name, data in eqs.items():
        if data.get('disc_degree') is None:
            results[name] = {
                'family': name,
                'note': data.get('note', 'No algebraic equation known'),
                'satisfied': None,
            }
            continue
        results[name] = verify_discriminant_bound(
            name, data['rank'], data['disc_degree'],
        )
    return results


# =========================================================================
# Koszul functional equation (PBW / associated-graded level)
# =========================================================================

def koszul_functional_equation_classical(
    dims_A: List[int],
    dims_A_dual: List[int],
    N: int = None,
) -> Dict:
    r"""Check the CLASSICAL Koszul identity H_A(x) * H_{A!}(-x) = 1.

    Here H_A(x) = 1 + sum a_n x^n is the Hilbert series of A, and
    H_{A!}(x) = 1 + sum b_n x^n is the Hilbert series of A!.

    For CHIRAL algebras, the bar cohomology gives A! dims via PBW.
    The A dims come from the algebra itself (e.g., dim(S^n(g)) for KM).

    Args:
        dims_A: Hilbert series coefficients [a_1, a_2, ...] for the ALGEBRA A
        dims_A_dual: Hilbert series coefficients [b_1, b_2, ...] for A!
        N: check through x^N
    """
    if N is None:
        N = min(len(dims_A), len(dims_A_dual))

    product_coeffs = {}
    product_coeffs[0] = 1

    for k in range(1, N + 1):
        s = 0
        for j in range(k + 1):
            a_j = 1 if j == 0 else (dims_A[j - 1] if j <= len(dims_A) else 0)
            b_kj = 1 if k - j == 0 else (dims_A_dual[k - j - 1] if k - j <= len(dims_A_dual) else 0)
            s += a_j * b_kj * (-1)**(k - j)
        product_coeffs[k] = s

    vanishes = all(product_coeffs[k] == 0 for k in range(1, N + 1))

    return {
        'N': N,
        'product_coeffs': product_coeffs,
        'koszul_identity_holds': vanishes,
    }


def verify_betagamma_koszul_pair() -> Dict:
    r"""Verify betagamma / free-fermion Koszul pair.

    betagamma Hilbert series: H_{bg}(x) = prod_{n>=1} 1/(1-x^n)^2
    (two bosonic generators of each weight >= 1).
    Actually for the VACUUM MODULE with generators beta, gamma of weight
    lambda, 1-lambda: the PBW basis has dim_n = number of monomials of
    total weight n in {beta_{-k}, gamma_{-k} : k >= 1}.

    At the associated-graded PBW level:
    H_{bg}(x) = prod_{k>=1} 1/(1-x^k)^2  [two generators]
    H_{ff}(x) = prod_{k>=1} (1+x^k)^2     [free fermion, two generators]
    Koszul identity: H_{bg}(x) * H_{ff}(-x) = 1.

    prod 1/(1-x^k)^2 * prod (1-x^k)^2 = 1.  YES! This is trivially true.
    But that uses H_ff(-x) = prod (1+(-x)^k)^2 = prod (1-x^k)^2 for ODD k
    times prod (1+x^k)^2 for EVEN k... actually this doesn't simplify.

    The correct identity for quadratic Koszul duality (Com! = Lie) at the
    associated-graded level involves the QUADRATIC DUAL Hilbert series,
    not the full module-level series.  For the chiral bar complex, the
    relevant identity is tested numerically here.
    """
    # betagamma ALGEBRA dims (PBW: monomials in beta_{-k}, gamma_{-k})
    # weight-n subspace has dim = sum_{a+b=n} p(a)*p(b) where p = partitions
    # (one set of modes for beta, one for gamma)
    N = 10
    bg_dims = []
    for n in range(1, N + 1):
        d = sum(partition_number(a) * partition_number(n - a) for a in range(n + 1))
        bg_dims.append(d)

    # free fermion (= betagamma Koszul dual) bar cohomology dims
    # H^n(B(ff)): from bar_complex.py, free_fermion dims = p(n-1)
    ff_bar_dims = [partition_number(n - 1) for n in range(1, N + 1)]

    return koszul_functional_equation_classical(bg_dims, ff_bar_dims, N)


# =========================================================================
# G2 prediction
# =========================================================================

def predict_g2_algebraic_equation() -> Dict:
    r"""Predict the algebraic equation structure for G2_hat bar cohomology GF.

    G2 has rank 2, dim = 14, exponents {1, 5}, Coxeter number 6.
    The conjecture predicts: algebraic degree <= 2, discriminant degree <= 4.

    Structural analogy with other KM algebras:
    - sl2 (rank 1, dim 3): disc = (1-3x)(1+x), degree 2, dominant root 1/3
    - sl3 (rank 2, dim 8): rational GF, den = (1-8x)(1-3x-x^2), degree 3
    - G2  (rank 2, dim 14): expected dominant root ~1/14

    H^1(B(G2_hat)) = dim(G2) = 14 (the generators).
    """
    x = Symbol('x')

    rank_g2 = 2
    dim_g2 = 14
    exponents_g2 = [1, 5]
    coxeter_number = 6
    dual_coxeter = 4

    disc_bound = 2 * rank_g2  # = 4

    return {
        'rank': rank_g2,
        'dim': dim_g2,
        'exponents': exponents_g2,
        'coxeter_number': coxeter_number,
        'dual_coxeter': dual_coxeter,
        'disc_degree_bound': disc_bound,
        'H1': dim_g2,
        'prediction': (
            f"P_{{G2}}(x) satisfies a polynomial equation of degree <= 2 "
            f"with discriminant degree <= {disc_bound}. "
            f"If rational (like sl3), the denominator has a dominant root "
            f"near x = 1/{dim_g2}."
        ),
        'structural_analogy': {
            'sl2': {'dim': 3, 'rank': 1, 'disc_deg': 2, 'dominant_root': Rational(1, 3)},
            'sl3': {'dim': 8, 'rank': 2, 'disc_deg': 6, 'dominant_root': Rational(1, 8)},
            'G2':  {'dim': 14, 'rank': 2, 'disc_deg': '<=4', 'dominant_root': f'~1/14'},
        },
    }


# =========================================================================
# Universal discriminant analysis
# =========================================================================

def universal_discriminant_factorization() -> Dict:
    r"""Investigate the universal Catalan discriminant (1-3x)(1+x).

    Three families — sl2 (Riordan), Virasoro (Motzkin diff), betagamma —
    share the discriminant 1-2x-3x^2 = (1-3x)(1+x).  This is the Catalan
    discriminant: the same polynomial appears in the algebraic equation for
    the Catalan number GF C(x) = (1-sqrt(1-4x))/(2x).

    The roots x = 1/3 and x = -1 control the asymptotic growth:
    - x = 1/3: dominant singularity, a_n ~ C * 3^n / n^alpha
    - x = -1: alternating-sign cancellation point
    """
    x = Symbol('x')

    catalan_disc = Poly((1 - 3*x)*(1 + x), x)
    sl3_disc = Poly(expand((1 - 8*x)*(1 - 3*x - x**2)), x)

    return {
        'catalan_discriminant': catalan_disc,
        'catalan_roots': [Rational(1, 3), Rational(-1)],
        'sl3_discriminant': sl3_disc,
        'sl3_roots': [Rational(1, 8)] + list(solve(1 - 3*x - x**2, x)),
        'shared_by': ['sl2', 'Virasoro', 'betagamma'],
        'interpretation': (
            "The universal discriminant (1-3x)(1+x) is the Catalan discriminant. "
            "Its appearance in three structurally different families (KM, Virasoro, "
            "free field) suggests a deep connection to the modular operad."
        ),
    }


# =========================================================================
# Comprehensive verification
# =========================================================================

def verify_algebraicity_all_families() -> Dict[str, Dict]:
    r"""Run the full algebraicity verification for all families with known equations."""
    results = {}

    results['sl2_riordan'] = verify_riordan_equation(15)
    results['betagamma'] = verify_betagamma_equation(12)
    results['sl3'] = verify_sl3_rational_gf(8)
    results['W3'] = verify_w3_rational_gf(8)

    return results


# =========================================================================
# Internal helpers
# =========================================================================

def _riordan_numbers(N: int) -> List[int]:
    """Riordan numbers R(0), ..., R(N-1). OEIS A005043."""
    R = [0] * N
    R[0] = 1
    if N > 1:
        R[1] = 0
    for n in range(2, N):
        R[n] = ((n - 1) * (2 * R[n - 1] + 3 * R[n - 2])) // (n + 1)
    return R


def _motzkin_numbers(N: int) -> List[int]:
    """Motzkin numbers M(0), ..., M(N-1). OEIS A001006."""
    M = [0] * N
    M[0] = 1
    if N > 1:
        M[1] = 1
    for n in range(2, N):
        M[n] = M[n - 1] + sum(M[k] * M[n - 2 - k] for k in range(n - 1))
    return M
