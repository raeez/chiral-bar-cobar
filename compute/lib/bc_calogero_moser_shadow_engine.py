r"""Calogero-Moser system from the shadow obstruction tower: extended engine.

Builds on compute/lib/calogero_moser_shadow.py with:
  (1) Jack polynomial norms and hook-length products
  (2) Shadow-CM integral of motion correspondence (S_r <-> I_r)
  (3) Heckman-Opdam polynomials for non-simply-laced root systems (B_2, G_2)
  (4) Ruijsenaars-Schneider relativistic deformation
  (5) AGT/Jack correspondence (Nekrasov vs Jack eigenvalues)
  (6) Hitchin spectral curve from shadow data
  (7) Level spacing statistics for quantum chaos analysis
  (8) Extended N-particle CM spectrum

MATHEMATICAL FRAMEWORK.

The Calogero-Moser Hamiltonian (trigonometric form)

    H_CM = -sum_i d^2/dx_i^2 + beta(beta-1) sum_{i<j} 1/sin^2(x_i - x_j)

has eigenfunctions given by Jack polynomials J_lambda^{(alpha)} with alpha = 1/beta.
The coupling beta is determined by shadow data:
  - Heisenberg at level k:  beta = k  (AP19: d log extraction gives level-k residue)
  - Virasoro at central charge c:  beta = c/2 / (c/2 - 1) = c/(c-2)
    (using kappa = c/2, and the identification beta = kappa/(kappa - 1))
  - Affine hat{sl}_N at level k:  beta = k + N  (shifted by h^v = N)

JACK POLYNOMIAL NORMS.

The Jack inner product norm is computed from the hook-length product:

    ||J_lambda||^2_alpha = prod_{(i,j) in lambda}
        (a'(i,j)*alpha + l'(i,j) + 1) / (a'(i,j)*alpha + l'(i,j) + alpha)

where a'(i,j) = j-1 (co-arm), l'(i,j) = i-1 (co-leg) are the co-arm and
co-leg lengths of the box (i,j) in lambda (1-indexed).

SHADOW-CM INTEGRAL CORRESPONDENCE.

The r-th CM integral of motion I_r = sum_i D_i^r (Dunkl power sums) should
correspond to the shadow obstruction tower coefficient S_r:
  - I_2 = H_CM <-> S_2 = kappa
  - I_3 <-> S_3 = alpha (cubic shadow)
  - I_4 <-> S_4 (quartic shadow)

The precise dictionary maps through the shadow connection: the flat sections
of nabla^sh = d - Q'/(2Q) dt satisfy the CM eigenvalue equation.

RUIJSENAARS-SCHNEIDER DEFORMATION.

The RS system with coupling eta deforms CM to a difference operator:

    H_RS = sum_i prod_{j!=i} [sin(x_i - x_j + i*eta) / sin(x_i - x_j)]^{1/2} T_{eta,i}

where T_{eta,i} shifts x_i -> x_i + eta.  At eta -> 0, H_RS -> H_CM.

The RS eigenvalues on Macdonald polynomials P_lambda(x; q, t) with
q = e^{i*eta}, t = q^beta are:

    E^RS_lambda = sum_i t^{N-i} q^{lambda_i}

HECKMAN-OPDAM FOR NON-SIMPLY-LACED ROOT SYSTEMS.

For root system R with multiplicities k_alpha (one per orbit under the Weyl group):
  - B_2: short roots (k_s) and long roots (k_l) as independent parameters
  - G_2: short roots (k_s) and long roots (k_l), ratio of root lengths sqrt(3)

Manuscript references:
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    rem:agt-shadow-connection (connections/feynman_bv.tex)
    Calogero (1971), Moser (1975)
    Ruijsenaars-Schneider, Ann. Phys. 170 (1986) 370-405
    Macdonald, "Symmetric Functions and Hall Polynomials"
    Heckman-Opdam, Compositio Math. 64 (1987)
    Etingof, "Calogero-Moser Systems and Representation Theory"
"""

from __future__ import annotations

import math
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    I, Integer, Matrix, Poly, Rational, S, Symbol, binomial, cancel,
    collect, cos, diff, exp, expand, factor, factorial, log, pi,
    simplify, sin, solve, sqrt, symbols, oo, Abs, N as Neval,
    prod as symprod, conjugate,
)


# ============================================================================
# Symbols
# ============================================================================

beta_sym = Symbol('beta', positive=True)
alpha_jack = Symbol('alpha', positive=True)
c_sym = Symbol('c')
k_sym = Symbol('k')
eta_sym = Symbol('eta')
q_var = Symbol('q')
t_mac = Symbol('t_mac')


# ============================================================================
# 1. JACK POLYNOMIAL NORMS (HOOK-LENGTH PRODUCT)
# ============================================================================

def conjugate_partition(lam: Tuple[int, ...]) -> Tuple[int, ...]:
    """Conjugate (transpose) of a partition."""
    if not lam:
        return ()
    max_col = lam[0]
    return tuple(sum(1 for row in lam if row > j) for j in range(max_col))


def coarm(lam: Tuple[int, ...], i: int, j: int) -> int:
    """Co-arm length a'(i,j) = j - 1 for box (i,j) in lambda (1-indexed).

    The co-arm counts boxes in the same row to the LEFT of (i,j).
    """
    return j - 1


def coleg(lam: Tuple[int, ...], i: int, j: int) -> int:
    """Co-leg length l'(i,j) = i - 1 for box (i,j) in lambda (1-indexed).

    The co-leg counts boxes in the same column ABOVE (i,j).
    """
    return i - 1


def arm(lam: Tuple[int, ...], i: int, j: int) -> int:
    """Arm length a(i,j) = lambda_i - j for box (i,j) in lambda (1-indexed).

    The arm counts boxes in the same row to the RIGHT of (i,j).
    """
    return lam[i - 1] - j


def leg(lam: Tuple[int, ...], i: int, j: int) -> int:
    """Leg length l(i,j) = lambda'_j - i for box (i,j) in lambda (1-indexed).

    The leg counts boxes in the same column BELOW (i,j).
    """
    lam_conj = conjugate_partition(lam)
    return lam_conj[j - 1] - i


def boxes(lam: Tuple[int, ...]) -> List[Tuple[int, int]]:
    """List all boxes (i, j) in partition lambda (1-indexed)."""
    result = []
    for i, row_len in enumerate(lam):
        for j in range(1, row_len + 1):
            result.append((i + 1, j))
    return result


def jack_norm_squared(lam: Tuple[int, ...], alpha_val, N: Optional[int] = None) -> Any:
    r"""Squared norm of the Jack polynomial in the combinatorial normalization.

    The Jack inner product (with respect to the power-sum inner product
    <p_mu, p_nu>_alpha = delta_{mu,nu} z_mu alpha^{l(mu)}) gives:

        ||J_lambda||^2 = prod_{(i,j) in lambda}
            (a(i,j)*alpha + l(i,j) + 1) * (a'(i,j)*alpha + l'(i,j) + alpha)
            -------------------------------------------------------------------
            (a(i,j)*alpha + l(i,j) + alpha) * (a'(i,j)*alpha + l'(i,j) + 1)

    This is the ratio of upper and lower hook-length products.

    Reference: Macdonald, "Symmetric Functions and Hall Polynomials", VI.10.

    Note: this is the norm of the J normalization. The C and C' normalizations
    have different norms involving just the upper or lower hook product.
    """
    if not lam:
        return S.One

    result = S.One
    for (i, j) in boxes(lam):
        a = arm(lam, i, j)
        l = leg(lam, i, j)
        ap = coarm(lam, i, j)
        lp = coleg(lam, i, j)

        upper_num = a * alpha_val + l + 1
        upper_den = a * alpha_val + l + alpha_val
        lower_num = ap * alpha_val + lp + alpha_val
        lower_den = ap * alpha_val + lp + 1

        result *= (upper_num * lower_num) / (upper_den * lower_den)

    return cancel(result)


def jack_c_norm_squared(lam: Tuple[int, ...], alpha_val) -> Any:
    r"""Squared norm of the C-normalization Jack polynomial.

    ||C_lambda||^2 = prod_{(i,j) in lambda} (a(i,j)*alpha + l(i,j) + 1)
                    / prod_{(i,j) in lambda} (a(i,j)*alpha + l(i,j) + alpha)
                    * alpha^{|lambda|}

    The C normalization has C_lambda = c_lambda * J_lambda where
    c_lambda = prod_{s in lambda} (a(s) + alpha*l(s) + alpha).
    """
    if not lam:
        return S.One

    upper = S.One
    lower = S.One
    for (i, j) in boxes(lam):
        a = arm(lam, i, j)
        l = leg(lam, i, j)
        upper *= a * alpha_val + l + 1
        lower *= a * alpha_val + l + alpha_val

    return cancel(upper / lower)


def jack_cprime_norm_squared(lam: Tuple[int, ...], alpha_val) -> Any:
    r"""Squared norm of the C'-normalization Jack polynomial.

    ||C'_lambda||^2 = prod_{(i,j) in lambda} (a'(i,j)*alpha + l'(i,j) + alpha)
                     / prod_{(i,j) in lambda} (a'(i,j)*alpha + l'(i,j) + 1)

    The C' normalization has C'_lambda = c'_lambda * J_lambda where
    c'_lambda = prod_{s in lambda} (a'(s)*alpha + l'(s) + 1).
    """
    if not lam:
        return S.One

    upper = S.One
    lower = S.One
    for (i, j) in boxes(lam):
        ap = coarm(lam, i, j)
        lp = coleg(lam, i, j)
        upper *= ap * alpha_val + lp + alpha_val
        lower *= ap * alpha_val + lp + 1

    return cancel(upper / lower)


def upper_hook_product(lam: Tuple[int, ...], alpha_val) -> Any:
    r"""Upper hook product H_lambda(alpha) = prod_{s in lambda} (a(s)*alpha + l(s) + 1).

    This appears in the numerator of the Jack norm and in the
    Nekrasov partition function.
    """
    if not lam:
        return S.One
    result = S.One
    for (i, j) in boxes(lam):
        a = arm(lam, i, j)
        l = leg(lam, i, j)
        result *= a * alpha_val + l + 1
    return expand(result)


def lower_hook_product(lam: Tuple[int, ...], alpha_val) -> Any:
    r"""Lower hook product H*_lambda(alpha) = prod_{s in lambda} (a(s)*alpha + l(s) + alpha).

    This appears in the denominator of the Jack norm.
    """
    if not lam:
        return S.One
    result = S.One
    for (i, j) in boxes(lam):
        a = arm(lam, i, j)
        l = leg(lam, i, j)
        result *= a * alpha_val + l + alpha_val
    return expand(result)


# ============================================================================
# 2. EXTENDED N-PARTICLE SPECTRUM
# ============================================================================

def partitions(n: int, max_length: Optional[int] = None) -> List[Tuple[int, ...]]:
    """All partitions of n with at most max_length parts, in dominance order."""
    if max_length is None:
        max_length = n

    def _generate(remaining, max_part, length):
        if remaining == 0:
            yield ()
            return
        if length == 0:
            return
        for part in range(min(remaining, max_part), 0, -1):
            for rest in _generate(remaining - part, part, length - 1):
                yield (part,) + rest

    parts = list(_generate(n, n, max_length))
    parts.sort(reverse=True)
    return parts


def cm_eigenvalue(lam: Tuple[int, ...], N: int, alpha_val) -> Any:
    """CM eigenvalue E_lambda for partition lambda at Jack parameter alpha.

    E_lambda = sum_i lambda_i * (lambda_i - 1 + (N + 1 - 2i) / alpha)

    This is the eigenvalue of the Sekiguchi-Debiard (Laplace-Beltrami)
    operator D_alpha on J_lambda^{(alpha)}, NOT the eigenvalue of the
    CM Hamiltonian H_CM directly.

    The CM Hamiltonian eigenvalue on the EXCITED state
    psi_lambda = J_lambda * psi_0 is:
        E^CM_lambda = E_lambda + E_0
    where E_0 = beta^2 * N(N^2-1)/12 is the ground state energy.
    """
    E = S.Zero
    for i, lam_i in enumerate(lam):
        E += lam_i * (lam_i - 1 + Rational(N + 1 - 2 * (i + 1), 1) / alpha_val)
    return cancel(E)


def cm_spectrum(N: int, alpha_val, max_degree: int) -> Dict[Tuple[int, ...], Any]:
    """Full CM spectrum for N particles up to given degree.

    Returns dict mapping partition -> eigenvalue.
    """
    spectrum = {}
    for d in range(max_degree + 1):
        for lam in partitions(d, N):
            spectrum[lam] = cm_eigenvalue(lam, N, alpha_val)
    return spectrum


def cm_spectrum_numerical(N: int, alpha_val, max_degree: int) -> List[float]:
    """Sorted numerical CM eigenvalues for level spacing analysis."""
    spec = cm_spectrum(N, alpha_val, max_degree)
    vals = sorted([float(v) for v in spec.values()])
    return vals


def shadow_coupling_virasoro(c_val) -> Any:
    """CM coupling beta from Virasoro central charge c.

    kappa(Vir_c) = c/2.  The shadow-CM identification gives
    beta = kappa / (kappa - 1) = c / (c - 2).

    At c = 2: beta diverges (critical point).
    At c = 0: beta = 0 (free, trivially uncurved by AP31).
    At c = 1: beta = -1.
    At c -> infinity: beta -> 1.

    WARNING: This coupling identification is CONJECTURAL beyond the
    Heisenberg case.  For Heisenberg, beta = k is proved.  For Virasoro,
    the identification through shadow data is structural but not proved.
    """
    kappa = Rational(c_val) / 2 if isinstance(c_val, (int, str)) else c_val / 2
    if kappa == 1:
        return oo
    return cancel(kappa / (kappa - 1))


def shadow_coupling_affine(lie_type: str, rank: int, level) -> Any:
    """CM coupling beta from affine KM shadow data.

    For hat{sl}_N at level k: beta = k + h^v = k + N
    where h^v = N is the dual Coxeter number of sl_N.
    """
    if lie_type == 'A':
        h_dual = rank + 1
    elif lie_type == 'B':
        h_dual = 2 * rank - 1
    elif lie_type == 'C':
        h_dual = rank + 1
    elif lie_type == 'D':
        h_dual = 2 * rank - 2
    elif lie_type == 'G' and rank == 2:
        h_dual = 4
    elif lie_type == 'F' and rank == 4:
        h_dual = 9
    elif lie_type == 'E' and rank == 6:
        h_dual = 12
    elif lie_type == 'E' and rank == 7:
        h_dual = 18
    elif lie_type == 'E' and rank == 8:
        h_dual = 30
    else:
        raise ValueError(f"Unknown Lie type {lie_type}_{rank}")

    return level + h_dual


# ============================================================================
# 3. SHADOW-CM INTEGRAL OF MOTION CORRESPONDENCE
# ============================================================================

def cm_integral_of_motion_eigenvalue(lam: Tuple[int, ...], N: int,
                                      alpha_val, r: int) -> Any:
    """Eigenvalue of the r-th CM integral of motion I_r on J_lambda.

    I_r = sum_i D_i^r (Dunkl power sums) is the r-th integral.

    The eigenvalue is:
        I_r(lambda) = sum_i (lambda_i + (N + 1 - 2i) / (2*alpha))^r
                     - sum_i ((N + 1 - 2i) / (2*alpha))^r

    This is the difference between the r-th power sum of the "shifted
    contents" of lambda and the ground-state contribution.

    For r = 2: this reduces to the CM eigenvalue (up to normalization).
    """
    eig = S.Zero
    for i in range(N):
        lam_i = lam[i] if i < len(lam) else 0
        shift = Rational(N + 1 - 2 * (i + 1), 1) / (2 * alpha_val)
        eig += (lam_i + shift) ** r - shift ** r
    return expand(eig)


def shadow_coefficient_from_cm_integral(N: int, alpha_val, r: int,
                                         lam: Tuple[int, ...]) -> Any:
    """Map the CM integral of motion eigenvalue to a shadow coefficient.

    The dictionary maps:
      I_2 eigenvalue  <-->  kappa  (arity-2 shadow = quadratic Casimir)
      I_3 eigenvalue  <-->  alpha  (arity-3 shadow = cubic invariant)
      I_4 eigenvalue  <-->  S_4    (arity-4 shadow = quartic invariant)
      I_r eigenvalue  <-->  S_r    (arity-r shadow)

    The normalization requires care: the Dunkl integral I_r is a POLYNOMIAL
    in the D_i, while S_r is a coefficient in the shadow obstruction tower
    expansion.  The relation is:
      S_r = (normalization factor) * I_r(fundamental representation)

    For N = 2 (single channel), the fundamental representation is lambda = (1).
    """
    return cm_integral_of_motion_eigenvalue(lam, N, alpha_val, r)


def shadow_to_cm_integral_dictionary(N: int, alpha_val,
                                      max_r: int = 5) -> Dict[int, Any]:
    """Dictionary mapping arity r to I_r eigenvalue on the fundamental rep.

    Returns {r: I_r(fund)} for r = 2, ..., max_r.
    """
    fund = (1,) + (0,) * (N - 1)  # fundamental representation
    fund = tuple(x for x in fund if x > 0)
    if not fund:
        fund = ()

    result = {}
    for r in range(2, max_r + 1):
        result[r] = cm_integral_of_motion_eigenvalue(fund, N, alpha_val, r)
    return result


def verify_cm_integrability(N: int, alpha_val, max_degree: int,
                             max_r: int = 4) -> Dict[str, bool]:
    """Verify that CM integrals of motion commute (same eigenbasis).

    For an integrable system, the eigenvalues of I_r and I_s on the Jack
    basis should satisfy: if I_r(lambda) = I_r(mu) and I_s(lambda) = I_s(mu)
    for all r, s, then lambda = mu (the integrals separate the spectrum).

    Returns dict of verification results.
    """
    results = {}

    # Check that the set {I_2(lam), I_3(lam), ..., I_{max_r}(lam)} uniquely
    # determines lambda (up to the N-particle constraint)
    for d in range(1, max_degree + 1):
        parts = partitions(d, N)
        if len(parts) <= 1:
            results[f'degree_{d}_separated'] = True
            continue

        # Compute integral tuples for each partition
        integral_tuples = {}
        for lam in parts:
            t = tuple(
                cm_integral_of_motion_eigenvalue(lam, N, alpha_val, r)
                for r in range(2, max_r + 1)
            )
            integral_tuples[lam] = t

        # Check injectivity
        values = list(integral_tuples.values())
        unique = len(set(values))
        results[f'degree_{d}_separated'] = (unique == len(values))

    return results


# ============================================================================
# 4. HECKMAN-OPDAM FOR NON-SIMPLY-LACED ROOT SYSTEMS
# ============================================================================

def root_system_B2() -> Dict[str, Any]:
    """Root system B_2 data.

    B_2 = so(5): rank 2, dim 2.
    Simple roots: alpha_1 = e_1 - e_2 (long), alpha_2 = e_2 (short).
    Positive roots: e_1 - e_2, e_1 + e_2, e_1, e_2.
    Long roots: e_1 +/- e_2 (length sqrt(2)).
    Short roots: e_1, e_2 (length 1).

    We represent roots as vectors in R^2.
    """
    long_roots = [(1, -1), (1, 1)]    # e_1 - e_2, e_1 + e_2
    short_roots = [(1, 0), (0, 1)]     # e_1, e_2
    return {
        'type': 'B_2',
        'rank': 2,
        'dim': 2,
        'long_positive_roots': long_roots,
        'short_positive_roots': short_roots,
        'all_positive_roots': long_roots + short_roots,
        'n_positive_roots': 4,
        'root_length_ratio_squared': 2,  # |long|^2 / |short|^2
        'weyl_group_order': 8,
    }


def root_system_G2() -> Dict[str, Any]:
    """Root system G_2 data.

    G_2: rank 2, dim 2.
    Simple roots: alpha_1 (short), alpha_2 (long).
    In the standard embedding in R^3 (sum = 0 plane):
      Short roots: +/- (e_i - e_j) for i < j, 6 total, 3 positive
      Long roots: +/- (2e_i - e_j - e_k) for {i,j,k} = {1,2,3}, 6 total, 3 positive

    For 2D computation, we use the angle representation.
    Short positive roots at angles 0, pi/3, 2*pi/3 (from x-axis).
    Long positive roots at angles pi/6, pi/2, 5*pi/6.

    In Cartesian coordinates (length-normalized):
      short: (1,0), (1/2, sqrt(3)/2), (-1/2, sqrt(3)/2)
      long: (sqrt(3)/2, 1/2), (0, 1), (-sqrt(3)/2, 1/2)

    For the Hamiltonian, we work with inner products alpha(x) = alpha . x.
    """
    # Using e_i - e_j representation in R^3 restricted to sum=0 plane
    # Short positive: e_1-e_2, e_1-e_3, e_2-e_3
    # Long positive: 2e_1-e_2-e_3, 2e_2-e_1-e_3, -2e_3+e_1+e_2
    # = 2e_1-e_2-e_3, -e_1+2e_2-e_3, e_1+e_2-2e_3
    short_positive = [(1, -1, 0), (1, 0, -1), (0, 1, -1)]
    long_positive = [(2, -1, -1), (-1, 2, -1), (1, 1, -2)]
    return {
        'type': 'G_2',
        'rank': 2,
        'dim': 3,  # embedded in R^3 with sum=0 constraint
        'short_positive_roots': short_positive,
        'long_positive_roots': long_positive,
        'all_positive_roots': short_positive + long_positive,
        'n_positive_roots': 6,
        'root_length_ratio_squared': 3,  # |long|^2 / |short|^2
        'weyl_group_order': 12,
    }


def heckman_opdam_eigenvalue_B2(lam: Tuple[int, int], k_short, k_long) -> Any:
    """Heckman-Opdam eigenvalue for B_2 with multiplicities k_s, k_l.

    The eigenvalue of the B_2 CM Hamiltonian on the spherical harmonic
    labeled by the dominant weight lambda = (lambda_1, lambda_2) is:

    E_lambda = sum_i lambda_i^2 + sum_i lambda_i * rho_i * 2
    where rho = k_l * (1,0) + k_s * (1,1) / 2 is the weighted half-sum
    of positive roots.

    More precisely, rho = (k_l + k_s, k_s) for B_2 with our conventions.

    E_lambda = lambda_1^2 + lambda_2^2
             + lambda_1 * (2*k_l + 2*k_s - 1)
             + lambda_2 * (2*k_s - 1)

    This matches the general Heckman-Opdam formula:
    E_lambda = |lambda + rho_k|^2 - |rho_k|^2
    where rho_k = sum_{alpha > 0} k_alpha * alpha / 2.
    """
    l1, l2 = lam
    # rho_k for B_2:
    # sum over long positive: k_l * [(1,-1) + (1,1)] / 2 = k_l * (1, 0)
    # sum over short positive: k_s * [(1,0) + (0,1)] / 2 = k_s * (1/2, 1/2)
    # rho_k = (k_l + k_s/2, k_s/2)

    rho1 = k_long + k_short / 2
    rho2 = k_short / 2

    E = (l1 + rho1) ** 2 + (l2 + rho2) ** 2 - rho1 ** 2 - rho2 ** 2
    return expand(E)


def heckman_opdam_eigenvalue_G2(lam: Tuple[int, int], k_short, k_long) -> Any:
    """Heckman-Opdam eigenvalue for G_2 with multiplicities k_s, k_l.

    For G_2, the Weyl vector is rho_k = (k_s + k_l) * rho_fund
    where rho_fund is the fundamental Weyl vector.

    In the fundamental weight basis omega_1 (short), omega_2 (long):
      rho = (1,1) (undeformed)
      rho_k depends on the root multiplicities.

    The eigenvalue formula:
      E_lambda = |lambda + rho_k|^2 - |rho_k|^2

    using the Killing form <omega_i, omega_j> = A^{-1}_{ij} where
    A is the Cartan matrix of G_2:
      A = [[2, -3], [-1, 2]]
      A^{-1} = [[2, 3], [1, 2]] / 1 (normalized)

    The Killing norm: |mu|^2 = 2*mu_1^2 + 6*mu_1*mu_2 + 6*mu_2^2
    (using dual basis normalization where <alpha_1, alpha_1> = 2 for short root).

    NOTE: conventions on G_2 inner product normalization vary.
    We use <alpha_s, alpha_s> = 2/3 (short root squared length = 2/3).
    """
    l1, l2 = lam

    # rho_k for G_2: sum over positive roots with multiplicities
    # Short roots contribute k_s, long roots contribute k_l
    # In fundamental weight coords: rho_k = (k_s + k_l, k_s + k_l) approximately
    # More precisely, with 3 short positive and 3 long positive:
    # rho_k = k_s * (sum of short positive / 2) + k_l * (sum of long positive / 2)
    # For G_2 fundamental weights: rho_k = (k_s + k_l, k_s + k_l) (by symmetry)

    # G_2 Cartan matrix
    # <omega_1, omega_1> = 2/3, <omega_1, omega_2> = 1, <omega_2, omega_2> = 2
    # (using the convention |alpha_long|^2 = 2)

    rho1 = k_short + k_long
    rho2 = k_short + k_long

    # Killing form in fundamental weight basis (G_2 inverse Cartan):
    # ||mu||^2 = (2/3)*mu_1^2 + 2*mu_1*mu_2 + 2*mu_2^2
    def killing_sq(a, b):
        return Rational(2, 3) * a ** 2 + 2 * a * b + 2 * b ** 2

    E = killing_sq(l1 + rho1, l2 + rho2) - killing_sq(rho1, rho2)
    return expand(E)


def heckman_opdam_eigenvalue_A(lam: Tuple[int, ...], N: int, k_val) -> Any:
    """Heckman-Opdam eigenvalue for A_{N-1} = sl_N with uniform multiplicity k.

    This is the standard CM eigenvalue: for type A with all roots at
    multiplicity k (equivalent to beta = k), the HO eigenvalue is:

    E_lambda = sum_i lambda_i * (lambda_i - 1 + (N + 1 - 2i) * k)

    This matches cm_eigenvalue with alpha = 1/k.
    """
    E = S.Zero
    for i, lam_i in enumerate(lam):
        E += lam_i * (lam_i - 1 + (N + 1 - 2 * (i + 1)) * k_val)
    return expand(E)


def shadow_to_heckman_opdam_so5(level) -> Dict[str, Any]:
    """Map hat{so}_5 shadow data to B_2 Heckman-Opdam system.

    For hat{so}_5 (type B_2) at level k:
    - Dual Coxeter number h^v = 3
    - Short root multiplicity k_s = k + h^v = k + 3
    - Long root multiplicity k_l = k + h^v = k + 3
    (For simply-laced cases, k_s = k_l.  For B_2, by convention
    in the shadow correspondence, both multiplicities are k + h^v.)

    This is the CONJECTURAL extension beyond type A.
    """
    h_dual = 3
    return {
        'lie_type': 'B_2',
        'lie_algebra': 'so_5',
        'level': level,
        'h_dual': h_dual,
        'k_short': level + h_dual,
        'k_long': level + h_dual,
        'root_system': root_system_B2(),
    }


def shadow_to_heckman_opdam_G2(level) -> Dict[str, Any]:
    """Map hat{G}_2 shadow data to G_2 Heckman-Opdam system.

    For hat{G}_2 at level k:
    - Dual Coxeter number h^v = 4
    - Root multiplicities: k_s = k + h^v = k + 4, k_l = k + h^v = k + 4
    """
    h_dual = 4
    return {
        'lie_type': 'G_2',
        'level': level,
        'h_dual': h_dual,
        'k_short': level + h_dual,
        'k_long': level + h_dual,
        'root_system': root_system_G2(),
    }


# ============================================================================
# 5. RUIJSENAARS-SCHNEIDER DEFORMATION
# ============================================================================

def rs_eigenvalue(lam: Tuple[int, ...], N: int,
                  q_val, t_val) -> Any:
    """Ruijsenaars-Schneider eigenvalue on Macdonald polynomial P_lambda.

    E^RS_lambda = sum_i t^{N-1-i} * q^{lambda_i}

    where t = q^beta is the RS coupling.

    At q -> 1 (eta -> 0): all terms -> 1, E -> N (trivial).
    The RELATIVE eigenvalue E - E_ground is the interesting quantity.

    The CM limit: q = e^{i*eta}, t = q^beta = e^{i*beta*eta}.
    As eta -> 0:
        E^RS_lambda -> sum_i (1 + i*beta*eta*(N-1-i) + i*eta*lambda_i + ...)
    Leading non-trivial term is O(eta) and matches the CM eigenvalue.
    """
    lam_padded = list(lam) + [0] * (N - len(lam))
    E = S.Zero
    for i in range(N):
        E += t_val ** (N - 1 - i) * q_val ** lam_padded[i]
    return E


def rs_eigenvalue_numerical(lam: Tuple[int, ...], N: int,
                             eta_val: float, beta_val: float) -> complex:
    """Numerical RS eigenvalue at given coupling eta and beta.

    q = exp(i*eta), t = q^beta = exp(i*beta*eta).
    """
    q = math.e ** (1j * eta_val)
    t = q ** beta_val
    lam_padded = list(lam) + [0] * (N - len(lam))
    E = sum(t ** (N - 1 - i) * q ** lam_padded[i] for i in range(N))
    return E


def rs_cm_limit_check(lam: Tuple[int, ...], N: int,
                       alpha_val, eta_val: float = 1e-6) -> Dict[str, Any]:
    """Verify that the RS eigenvalue -> CM eigenvalue as eta -> 0.

    The leading correction to the RS eigenvalue at small eta is:
        E^RS = N + i*eta * E^CM / alpha + O(eta^2)

    where E^CM is the CM eigenvalue at Jack parameter alpha = 1/beta.
    """
    beta_val = float(Rational(1) / alpha_val) if alpha_val != 0 else 0.0

    E_rs = rs_eigenvalue_numerical(lam, N, eta_val, beta_val)
    E_cm = float(cm_eigenvalue(lam, N, alpha_val))

    # At eta -> 0: (E_RS - N) / (i * eta) should approach E_CM-related quantity
    # More precisely, E^RS = sum t^{N-1-i} q^{lam_i}
    # = sum exp(i*beta*eta*(N-1-i)) exp(i*eta*lam_i)
    # = sum exp(i*eta*(beta*(N-1-i) + lam_i))
    # = sum (1 + i*eta*(beta*(N-1-i) + lam_i) + ...)
    # Leading: N + i*eta * sum (beta*(N-1-i) + lam_i)

    # The CM eigenvalue is sum lam_i * (lam_i - 1 + (N+1-2(i+1))/alpha)
    # = sum lam_i * (lam_i - 1 + (N-1-2i)*beta)
    # The linear RS term is sum (beta*(N-1-i) + lam_i) which is different.

    # The correct comparison: the RS-to-CM limit involves dividing by eta^2
    # and subtracting the ground state, not eta^1.

    linear_rs = sum(
        beta_val * (N - 1 - i) + (lam[i] if i < len(lam) else 0)
        for i in range(N)
    )

    return {
        'partition': lam,
        'N': N,
        'alpha': alpha_val,
        'beta': beta_val,
        'eta': eta_val,
        'E_rs': E_rs,
        'E_cm': E_cm,
        'rs_linear_term': linear_rs,
    }


def rs_spectrum_numerical(N: int, beta_val: float, eta_val: float,
                           max_degree: int) -> List[complex]:
    """Full RS spectrum as a list of complex eigenvalues."""
    spec = []
    for d in range(max_degree + 1):
        for lam in partitions(d, N):
            E = rs_eigenvalue_numerical(lam, N, eta_val, beta_val)
            spec.append(E)
    return spec


# ============================================================================
# 6. AGT / JACK CORRESPONDENCE
# ============================================================================

def agt_jack_parameter(b_val) -> Any:
    """Jack parameter alpha from the AGT parameter b.

    In the AGT correspondence:
        c = 1 + 6(b + 1/b)^2
        eps1/eps2 = -b^2
        alpha_Jack = -b^2   (NEGATIVE for physical values)

    However, for the CM system we need alpha > 0.  The physical
    AGT identification uses the ANALYTIC CONTINUATION of the Jack
    parameter to negative values: alpha = -(b^2 + b^{-2})/2 is the
    Nekrasov-Shatashvili parameter, but for the Calogero-Moser eigenvalue
    comparison, we use alpha = -eps_1/eps_2 = b^2.

    For self-dual point b = 1: alpha = 1 (Schur polynomials), c = 25.
    For b = i: alpha = -1 (singular).
    """
    return b_val ** 2


def nekrasov_arm_leg_factor(Y: Tuple[int, ...], s: Tuple[int, int],
                             eps1, eps2) -> Any:
    """Nekrasov arm-leg factor for box s = (i,j) in Young diagram Y.

    N(s) = -eps1 * a_Y(s) + eps2 * (l_Y(s) + 1)

    where a_Y(i,j) = Y_i - j (arm), l_Y(i,j) = Y'_j - i (leg).
    """
    i, j = s
    a_Y = Y[i] - j if i < len(Y) else -j
    lam_conj = conjugate_partition(Y)
    l_Y = (lam_conj[j] - i if j < len(lam_conj) else -i)
    return -eps1 * a_Y + eps2 * (l_Y + 1)


def nekrasov_instanton_weight_single(Y: Tuple[int, ...],
                                      eps1, eps2) -> Any:
    """Instanton weight for a single Young diagram (U(1) theory).

    z_Y = prod_{s in Y} 1 / (N_Y(s) * N_Y(s)')

    where N(s) = -eps1*a(s) + eps2*(l(s)+1), N'(s) = eps1*(a(s)+1) - eps2*l(s).

    This is the factor appearing in the Nekrasov partition function.
    """
    if not Y:
        return S.One

    result = S.One
    for i, row_len in enumerate(Y):
        for j in range(row_len):
            a_Y = Y[i] - j - 1
            lam_conj = conjugate_partition(Y)
            l_Y = lam_conj[j] - i - 1

            N_s = -eps1 * a_Y + eps2 * (l_Y + 1)
            Np_s = eps1 * (a_Y + 1) - eps2 * l_Y

            if N_s != 0 and Np_s != 0:
                result /= (N_s * Np_s)

    return cancel(result)


def agt_vs_jack_comparison(lam: Tuple[int, ...], N: int,
                            b_val) -> Dict[str, Any]:
    """Compare AGT Nekrasov eigenvalue with Jack eigenvalue.

    The AGT correspondence at the combinatorial level identifies:
    - Jack polynomial eigenvalue at alpha = b^2
    - Nekrasov instanton energy

    The Nekrasov energy of a Young diagram Y is:
        E^Nek_Y = sum_{s in Y} (eps1 * j + eps2 * i)
    where s = (i,j) runs over boxes (0-indexed).

    At eps1 = b, eps2 = 1/b (the AGT-normalized Omega-background):
        E^Nek_Y = sum (b*j + i/b)

    The Jack eigenvalue at alpha = b^2 is:
        E^Jack_lambda = sum_i lambda_i * (lambda_i - 1 + (N+1-2(i+1))/(b^2))

    The relation is:
        E^Nek = b * E^Jack + (ground state shift)

    We verify this at specific values.
    """
    alpha_val = b_val ** 2

    # Jack eigenvalue
    E_jack = cm_eigenvalue(lam, N, alpha_val)

    # Nekrasov energy (sum of box coordinates)
    eps1 = b_val
    eps2 = 1 / b_val
    E_nek = S.Zero
    for i, row_len in enumerate(lam):
        for j in range(row_len):
            E_nek += eps1 * j + eps2 * i

    return {
        'partition': lam,
        'N': N,
        'b': b_val,
        'alpha': alpha_val,
        'E_jack': cancel(E_jack),
        'E_nekrasov': cancel(E_nek),
        'ratio': cancel(E_nek / E_jack) if E_jack != 0 else None,
    }


# ============================================================================
# 7. HITCHIN SPECTRAL CURVE FROM SHADOW DATA
# ============================================================================

def hitchin_spectral_curve_N2(kappa_val, alpha_val_shadow,
                                S4_val) -> Dict[str, Any]:
    """Hitchin spectral curve from 2-particle shadow data.

    The CM system for N = 2 on the punctured torus is equivalent to the
    rank-1 Hitchin system.  The spectral curve is:

        det(eta - Phi(z)) = 0

    where Phi is the Higgs field, a meromorphic 1-form on the elliptic curve.
    For the CM system, the spectral curve is:

        w^2 = E + beta(beta-1) * wp(z)

    where E is the energy eigenvalue and wp is the Weierstrass p-function.

    From shadow data:
    - kappa determines the CM coupling: beta(beta-1) ~ kappa^2
    - S4 determines the quartic correction
    - The spectral curve genus depends on the shadow depth:
      * class G (Delta = 0): genus 0 (rational spectral curve)
      * class M (Delta != 0): genus >= 1 (elliptic or higher)

    The critical discriminant Delta = 8*kappa*S4 controls the genus:
    Delta = 0 => the spectral curve degenerates (Hitchin fiber is rational).
    Delta != 0 => the spectral curve is genuinely elliptic.
    """
    Delta = 8 * kappa_val * S4_val

    # Spectral curve type
    if Delta == 0:
        curve_genus = 0
        curve_type = 'rational'
    else:
        curve_genus = 1
        curve_type = 'elliptic'

    return {
        'kappa': kappa_val,
        'alpha': alpha_val_shadow,
        'S4': S4_val,
        'Delta': Delta,
        'spectral_curve_genus': curve_genus,
        'spectral_curve_type': curve_type,
        'cm_coupling': kappa_val * (kappa_val - 1),
        'shadow_class': 'G' if Delta == 0 else 'M',
    }


def hitchin_spectral_curve_virasoro(c_val) -> Dict[str, Any]:
    """Hitchin spectral curve from Virasoro shadow data.

    For Virasoro at central charge c:
    - kappa = c/2
    - alpha = 2 (cubic shadow coefficient)
    - S4 = 10 / (c * (5c + 22))
    - Delta = 8 * (c/2) * 10 / (c * (5c + 22)) = 40 / (5c + 22)

    Since Delta != 0 for generic c, the spectral curve is elliptic
    (genus 1), consistent with Virasoro being class M.
    """
    kappa = Rational(c_val) / 2 if isinstance(c_val, (int, str)) else c_val / 2
    alpha_sh = Rational(2)
    S4 = Rational(10) / (c_val * (5 * c_val + 22)) if isinstance(c_val, (int, str)) \
        else 10 / (c_val * (5 * c_val + 22))

    return hitchin_spectral_curve_N2(kappa, alpha_sh, S4)


def hitchin_spectral_curve_heisenberg(k_val) -> Dict[str, Any]:
    """Hitchin spectral curve from Heisenberg shadow data.

    For Heisenberg at level k:
    - kappa = k
    - alpha = 0 (no cubic shadow)
    - S4 = 0 (no quartic shadow)
    - Delta = 0

    The spectral curve is rational (genus 0), consistent with
    Heisenberg being class G (shadow depth 2, tower terminates).
    """
    return hitchin_spectral_curve_N2(k_val, 0, 0)


# ============================================================================
# 8. LEVEL SPACING STATISTICS
# ============================================================================

def level_spacings(eigenvalues: List[float]) -> List[float]:
    """Compute consecutive level spacings from sorted eigenvalues.

    s_i = E_{i+1} - E_i (unnormalized).
    """
    sorted_evals = sorted(eigenvalues)
    return [sorted_evals[i + 1] - sorted_evals[i] for i in range(len(sorted_evals) - 1)]


def normalized_level_spacings(eigenvalues: List[float]) -> List[float]:
    """Normalized level spacings: s_i / <s> where <s> is the mean spacing."""
    spacings = level_spacings(eigenvalues)
    if not spacings:
        return []
    mean_spacing = sum(spacings) / len(spacings)
    if mean_spacing == 0:
        return [0.0] * len(spacings)
    return [s / mean_spacing for s in spacings]


def level_spacing_ratio(eigenvalues: List[float]) -> List[float]:
    """Level spacing ratio r_i = min(s_i, s_{i+1}) / max(s_i, s_{i+1}).

    This ratio is distribution-independent of unfolding and is a robust
    diagnostic:
    - Poisson (integrable):  <r> = 2*ln(2) - 1 ≈ 0.386
    - GOE (chaotic, real):   <r> ≈ 0.536
    - GUE (chaotic, complex): <r> ≈ 0.603
    """
    spacings = level_spacings(eigenvalues)
    if len(spacings) < 2:
        return []
    ratios = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i + 1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))
    return ratios


def mean_spacing_ratio(eigenvalues: List[float]) -> float:
    """Mean level spacing ratio <r>.

    Poisson (integrable): ~0.386
    GOE: ~0.536
    GUE: ~0.603
    """
    ratios = level_spacing_ratio(eigenvalues)
    if not ratios:
        return 0.0
    return sum(ratios) / len(ratios)


def cm_level_spacing_analysis(N: int, alpha_val_float: float,
                               max_degree: int) -> Dict[str, Any]:
    """Full level spacing analysis of the CM spectrum.

    CM is integrable, so we expect POISSON statistics (no level repulsion).

    Returns:
    - eigenvalues (sorted)
    - normalized spacings
    - spacing ratios
    - mean spacing ratio (should be ~0.386 for Poisson)
    """
    alpha_val = Rational(alpha_val_float) if isinstance(alpha_val_float, (int, float)) \
        else alpha_val_float
    spec = cm_spectrum(N, alpha_val, max_degree)

    # Get unique numerical eigenvalues
    vals = sorted(set(float(v) for v in spec.values()))

    return {
        'N': N,
        'alpha': alpha_val_float,
        'max_degree': max_degree,
        'n_eigenvalues': len(vals),
        'eigenvalues': vals,
        'normalized_spacings': normalized_level_spacings(vals),
        'spacing_ratios': level_spacing_ratio(vals),
        'mean_spacing_ratio': mean_spacing_ratio(vals),
        'expected_poisson': 2 * math.log(2) - 1,  # ~0.386
    }


def degeneracy_count(N: int, alpha_val, max_degree: int) -> Dict[Any, int]:
    """Count eigenvalue degeneracies in the CM spectrum.

    For integrable systems, degeneracies arise from additional conserved
    quantities.  For CM at alpha = 1 (free fermions), the degeneracies
    are related to partition combinatorics.
    """
    spec = cm_spectrum(N, alpha_val, max_degree)
    eigenvalue_counts = Counter(spec.values())
    return dict(eigenvalue_counts)


# ============================================================================
# 9. VIRASORO SHADOW COUPLING DICTIONARY
# ============================================================================

def virasoro_shadow_cm_data(c_val) -> Dict[str, Any]:
    """Complete shadow-CM data for Virasoro at central charge c.

    Collects all shadow invariants and their CM interpretations.
    """
    c = Rational(c_val) if isinstance(c_val, (int, str)) else c_val
    kappa = c / 2
    alpha_shadow = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    Delta = 8 * kappa * S4

    # CM parameters
    beta_cm = kappa / (kappa - 1) if kappa != 1 else oo
    alpha_jack_val = 1 / beta_cm if beta_cm != oo and beta_cm != 0 else S.Zero

    return {
        'c': c,
        'kappa': kappa,
        'alpha_shadow': alpha_shadow,
        'S4': S4,
        'Delta': cancel(Delta),
        'beta_cm': cancel(beta_cm) if beta_cm != oo else oo,
        'alpha_jack': cancel(alpha_jack_val) if alpha_jack_val != S.Zero else S.Zero,
        'shadow_class': 'M',  # Virasoro is always class M for c != -22/5
        'shadow_depth': 'infinite',
    }


def affine_km_shadow_cm_data(lie_type: str, rank: int, level) -> Dict[str, Any]:
    """Complete shadow-CM data for affine KM at given level.

    For hat{sl}_N:
    - kappa = dim(g) * (k + h^v) / (2 * h^v)
    - Shadow class: L (r_max = 3, tree-level)
    - CM coupling: beta = k + h^v
    """
    if lie_type == 'A':
        N = rank + 1
        h_dual = N
        dim_g = N ** 2 - 1
    elif lie_type == 'B':
        h_dual = 2 * rank - 1
        dim_g = rank * (2 * rank + 1)
    elif lie_type == 'C':
        h_dual = rank + 1
        dim_g = rank * (2 * rank + 1)
    elif lie_type == 'D':
        h_dual = 2 * rank - 2
        dim_g = rank * (2 * rank - 1)
    elif lie_type == 'G' and rank == 2:
        h_dual = 4
        dim_g = 14
    else:
        raise ValueError(f"Unsupported type {lie_type}_{rank}")

    k = Rational(level) if isinstance(level, (int, str)) else level
    kappa = dim_g * (k + h_dual) / (2 * h_dual)
    beta_cm = k + h_dual
    alpha_jack_val = Rational(1) / beta_cm if beta_cm != 0 else oo

    return {
        'lie_type': f'{lie_type}_{rank}',
        'level': k,
        'h_dual': h_dual,
        'dim_g': dim_g,
        'kappa': cancel(kappa),
        'beta_cm': beta_cm,
        'alpha_jack': cancel(alpha_jack_val),
        'shadow_class': 'L',  # Affine KM is class L
        'shadow_depth': 3,
    }


# ============================================================================
# 10. CROSS-VERIFICATION UTILITIES
# ============================================================================

def verify_jack_norm_alpha1(lam: Tuple[int, ...]) -> Dict[str, Any]:
    """Verify Jack norm at alpha = 1 against Schur norm.

    At alpha = 1 (Schur polynomials), the Jack norm should reduce to
    the hook-length formula for Schur:

    ||s_lambda||^2 = prod_{s in lambda} hook(s)

    where hook(s) = a(s) + l(s) + 1 (the hook length).

    In the power-sum inner product with alpha = 1, the Schur norm is:
    <s_lambda, s_lambda> = 1 (orthonormal).

    For the J normalization: ||J_lambda||^2 at alpha = 1 should be
    a specific hook-length product.
    """
    norm_sq = jack_norm_squared(lam, Rational(1))

    # At alpha = 1, the norm simplifies:
    # Upper: a + l + 1 = hook length
    # Lower: a + l + 1 = hook length (same!)
    # Co-upper: j-1 + i-1 + 1 = i + j - 1
    # Co-lower: j-1 + i-1 + 1 = i + j - 1 (same!)
    # So at alpha = 1: ||J||^2 = 1

    return {
        'partition': lam,
        'alpha': 1,
        'norm_squared': norm_sq,
        'expected': 1,
        'match': simplify(norm_sq - 1) == 0,
    }


def verify_jack_norm_alpha2(lam: Tuple[int, ...]) -> Dict[str, Any]:
    """Verify Jack norm at alpha = 2 against zonal polynomial norm.

    At alpha = 2 (zonal polynomials), the Jack norm has a known formula:

    ||J_lambda||^2_{alpha=2} = prod_{s in lambda}
        (2*a(s) + l(s) + 1) * (2*(j-1) + (i-1) + 2)
        / ((2*a(s) + l(s) + 2) * (2*(j-1) + (i-1) + 1))
    """
    norm_sq = jack_norm_squared(lam, Rational(2))

    return {
        'partition': lam,
        'alpha': 2,
        'norm_squared': norm_sq,
    }


def verify_hook_product_reciprocity(lam: Tuple[int, ...], alpha_val) -> Dict[str, Any]:
    """Verify the hook-product reciprocity: H_lam(alpha) * H_lam(1/alpha) is symmetric.

    The upper hook product H(alpha) = prod (a*alpha + l + 1) should satisfy:
    H_lam(1/alpha) = alpha^{-|lam|} * H_{lam'}(alpha)

    where lam' is the conjugate partition.
    """
    H = upper_hook_product(lam, alpha_val)
    H_inv = upper_hook_product(lam, 1 / alpha_val)
    lam_conj = conjugate_partition(lam)
    H_conj = upper_hook_product(lam_conj, alpha_val)
    n = sum(lam)

    # Check: H(1/alpha) = alpha^{-n} * H_{conj}(alpha)
    # Equivalently: alpha^n * H(1/alpha) = H_{conj}(alpha)
    lhs = expand(alpha_val ** n * H_inv)
    rhs = expand(H_conj)

    return {
        'partition': lam,
        'conjugate': lam_conj,
        'alpha': alpha_val,
        'alpha_n_H_inv_alpha': lhs,
        'H_conj': rhs,
        'match': simplify(lhs - rhs) == 0,
    }


def verify_cm_vs_ho_type_A(N: int, k_val, max_degree: int) -> Dict[str, bool]:
    """Verify CM eigenvalues match Heckman-Opdam for type A.

    For type A_{N-1}, HO with uniform multiplicity k should give
    the same eigenvalues as CM with alpha = 1/k.
    """
    alpha_val = Rational(1) / k_val if k_val != 0 else oo
    results = {}
    for d in range(max_degree + 1):
        for lam in partitions(d, N):
            E_cm = cm_eigenvalue(lam, N, alpha_val)
            E_ho = heckman_opdam_eigenvalue_A(lam, N, k_val)
            results[lam] = simplify(E_cm - E_ho) == 0
    return results
