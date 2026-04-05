r"""Gap D analysis: central L-values, all-genera Beurling kernel convergence, circularity.

Two problems from arithmetic_shadows.tex (Remark rem:genus2-beurling-kernel, items (iv)
and rem:bocherer-escalation):

PART 1 — GAP D NORM MISMATCH.

The genus-2 Beurling kernel K^{(2)}_Lambda(D,D) involves L(1/2, pi_f x chi_D) at a
single point s = 1/2 (via the Boecherer factorization / Waldspurger formula). The
Nyman-Beurling criterion requires the FULL L^2(0,1) norm of the dilation functions
rho_theta(x) = {theta/x} - theta{1/x}. This norm encodes information about ALL zeros
of zeta (or the relevant L-function) on the critical strip, not just the central value.

KEY FINDING: central values at s=1/2 do NOT by themselves determine zero locations.
They determine the "value at the center" but not the "shape of the L-function on the
critical line." The moment problem for L(1/2, Sym^r f x chi_D) across all (r, D) DOES
determine the Satake parameters (by the Sato-Tate equidistribution perspective), but
this requires data for ALL r simultaneously — not one genus at a time.

The gap between "spectral support matches" (genus-2 kernel lives on Re(s)=1/2)
and "norm matches" (need full L^2 control) is the difference between:
  - knowing the L-function AT a single point on the critical line, and
  - knowing the L^2 norm of a function determined by the L-function ON the full line.

PART 2 — ALL-GENERA CONVERGENCE AND CIRCULARITY.

The genus-g MC contributes L(1/2, Sym^{g-1} f x chi_D). The escalation principle
claims the limit K^{(infty)} = varprojlim K^{(g)} recovers the full Nyman-Beurling
spectral content.

THREE OBSTRUCTIONS:

(a) Analytic conductor growth: The analytic conductor of Sym^{g-1}(f) x chi_D is
    ~ C(f)^g * |D|^g, where C(f) depends on the weight and level. The central value
    L(1/2, ...) fluctuates with amplitude ~ (log conductor)^{g(g+1)/4} (random matrix
    prediction, Keating-Snaith). The kernel entry K^{(g)} thus grows super-polynomially
    in g unless normalized.

(b) Non-vanishing failure: L(1/2, Sym^{g-1} f x chi_D) can vanish (sign of functional
    equation can be -1 for certain g, D). The kernel K^{(g)} has rank defects at such
    (g, D) pairs. The all-genera kernel inherits these rank defects.

(c) CIRCULARITY: The symmetric power transfer Sym^{g-1}: GL(2) -> GL(g) is proved
    unconditionally only for g <= 5:
      g=1: trivial (identity)
      g=2: Gelbart-Jacquet 1978
      g=3: Kim-Shahidi 2002
      g=4: Kim 2003
      g=5: Newton-Thorne 2021 (via modularity of symmetric powers for holomorphic
           forms of weight >= 2, using Calegari-Geraghty-Taylor potential automorphy)
    For g >= 6: conditional on Langlands functoriality GL(2) -> GL(g). But Langlands
    functoriality IS the very thing the arithmetic programme aims to approach. Using
    Sym^{g-1} for g >= 6 in the Beurling kernel requires assuming the conclusion.

    More precisely: the Newton-Thorne result proves Sym^n for all n, but ONLY for
    holomorphic modular forms of weight >= 2 over totally real fields. For Maass forms
    or weight-1 forms, Sym^n with n >= 5 remains open.

    The circularity is: to access L(1/2, Sym^{g-1} f x chi_D) at the MC level, the
    programme needs the Boecherer-type factorization at genus g, which requires knowing
    that the genus-g Siegel modular form is automorphic on GSp(2g). This IS established
    for theta series of lattices (by construction), but the passage from "MC determines
    Fourier coefficients" to "MC determines L-values" requires the L-function to be
    defined (automorphic), which requires the very functoriality being probed.

QUANTITATIVE ANALYSIS:

We compute:
1. The "moment problem completeness" — can {L(1/2, Sym^r f x chi_D)}_{r,D} determine
   all Satake parameters? (Yes, in principle; no, at finite genus.)
2. Conductor growth and random-matrix predictions for |K^{(g)}(D,D)|.
3. Root-number signs: when does L(1/2, Sym^{g-1} f x chi_D) = 0 for parity reasons?
4. The circularity frontier: which genera are unconditional?

References:
  - Nyman (1950), "On the one-dimensional translation group and semigroup"
  - Beurling (1955), "A closure problem related to the Riemann zeta-function"
  - Baez-Duarte (2003), "A strengthening of the Nyman-Beurling criterion"
  - Boecherer (1986), "Uber die Fourier-Jacobi-Entwicklung..."
  - Newton-Thorne (2021), "Symmetric power functoriality for holomorphic modular forms"
  - Keating-Snaith (2000), "Random matrix theory and L-functions at s=1/2"
  - Waldspurger (1981), "Sur les coefficients de Fourier..."
  - arithmetic_shadows.tex: rem:genus2-beurling-kernel, rem:bocherer-escalation
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


# ============================================================================
# 1. NYMAN-BEURLING CRITERION: WHAT THE L^2 NORM ENCODES
# ============================================================================

def nyman_beurling_norm_squared(theta: float, nmax: int = 2000) -> float:
    r"""Compute ||rho_theta||^2_{L^2(0,1)} for the Nyman-Beurling dilation function.

    rho_theta(x) = {theta/x} - theta * {1/x}

    where {y} = y - floor(y) is the fractional part.

    The L^2 norm is:
      ||rho_theta||^2 = integral_0^1 |rho_theta(x)|^2 dx

    This can be expressed via the Mellin transform as:
      ||rho_theta||^2 = sum_{m,n >= 1} c_m(theta) * conj(c_n(theta)) / (m*n*(m+n))

    where c_n(theta) = theta^n/n - floor(theta^n/n) type coefficients.

    For numerical purposes, we use direct quadrature.

    Parameters
    ----------
    theta : float
        Dilation parameter in (0, 1).
    nmax : int
        Number of quadrature points.

    Returns
    -------
    float
        ||rho_theta||^2.
    """
    if theta <= 0 or theta >= 1:
        raise ValueError(f"theta must be in (0, 1), got {theta}")

    # Trapezoidal rule on (epsilon, 1) to avoid x=0 singularity
    eps = 1e-8
    dx = (1.0 - eps) / nmax
    total = 0.0

    for i in range(nmax):
        x = eps + (i + 0.5) * dx
        frac_theta_x = (theta / x) - math.floor(theta / x)
        frac_1_x = (1.0 / x) - math.floor(1.0 / x)
        rho = frac_theta_x - theta * frac_1_x
        total += rho * rho * dx

    return total


def nyman_beurling_gram_matrix(
    thetas: List[float],
    nmax: int = 2000,
) -> np.ndarray:
    r"""Compute the Gram matrix G_{ij} = <rho_{theta_i}, rho_{theta_j}>_{L^2(0,1)}.

    The Nyman-Beurling criterion: RH iff the constant function 1 lies in the
    L^2(0,1) closure of span{rho_theta : theta in (0,1)}.

    Equivalently: RH iff inf_{c} ||1 - sum c_i rho_{theta_i}||^2 -> 0 as
    the theta-set grows.

    The Gram matrix controls this approximation.
    """
    n = len(thetas)
    G = np.zeros((n, n))

    eps = 1e-8
    dx = (1.0 - eps) / nmax

    # Build rho values for all thetas at all quadrature points
    rho_vals = np.zeros((n, nmax))
    for k in range(n):
        theta = thetas[k]
        for i in range(nmax):
            x = eps + (i + 0.5) * dx
            frac_theta_x = (theta / x) - math.floor(theta / x)
            frac_1_x = (1.0 / x) - math.floor(1.0 / x)
            rho_vals[k, i] = frac_theta_x - theta * frac_1_x

    # Gram matrix from inner products
    for j1 in range(n):
        for j2 in range(j1, n):
            val = np.sum(rho_vals[j1] * rho_vals[j2]) * dx
            G[j1, j2] = val
            G[j2, j1] = val

    return G


def nyman_beurling_distance_to_one(
    thetas: List[float],
    nmax: int = 2000,
) -> Dict[str, Any]:
    r"""Compute the distance from 1 to span{rho_theta}_theta in L^2(0,1).

    This is the Nyman-Beurling distance d_N = inf ||1 - sum c_j rho_{theta_j}||.
    The computation solves the normal equations: G c = b, where
    b_j = <1, rho_{theta_j}>_{L^2}.

    RH iff d_N -> 0 as the theta-set is enriched.
    """
    n = len(thetas)
    G = nyman_beurling_gram_matrix(thetas, nmax)

    eps = 1e-8
    dx = (1.0 - eps) / nmax

    # Compute b_j = <1, rho_{theta_j}>
    b = np.zeros(n)
    for k in range(n):
        theta = thetas[k]
        for i in range(nmax):
            x = eps + (i + 0.5) * dx
            frac_theta_x = (theta / x) - math.floor(theta / x)
            frac_1_x = (1.0 / x) - math.floor(1.0 / x)
            rho = frac_theta_x - theta * frac_1_x
            b[k] += rho * dx

    # ||1||^2 = integral_0^1 1 dx = 1
    norm_one_sq = 1.0

    # Solve Gc = b via least squares (G may be singular)
    try:
        c, residuals, rank, sv = np.linalg.lstsq(G, b, rcond=None)
        approx_norm_sq = np.dot(c, G @ c) - 2 * np.dot(c, b) + norm_one_sq
        # More stable: d^2 = ||1||^2 - b^T G^{-1} b
        # when G is invertible
        if np.linalg.matrix_rank(G) == n:
            d_sq = norm_one_sq - np.dot(b, np.linalg.solve(G, b))
        else:
            d_sq = max(0.0, approx_norm_sq)
    except np.linalg.LinAlgError:
        d_sq = float('inf')
        c = np.zeros(n)

    return {
        'distance_squared': max(0.0, d_sq),
        'distance': math.sqrt(max(0.0, d_sq)),
        'coefficients': c.tolist(),
        'gram_rank': np.linalg.matrix_rank(G),
        'gram_eigenvalues': sorted(np.linalg.eigvalsh(G).tolist()),
        'n_thetas': n,
    }


# ============================================================================
# 2. CENTRAL L-VALUE: WHAT A SINGLE POINT DETERMINES
# ============================================================================

def central_value_information_content() -> Dict[str, Any]:
    r"""Analyze what L(1/2, pi x chi_D) determines vs what NB needs.

    The genus-2 kernel K^{(2)}(D,D') involves L(1/2, pi_f x chi_D) at a
    SINGLE point s = 1/2 on the critical line.

    What this determines:
    - Whether pi_f x chi_D has a zero at s = 1/2 (non-vanishing).
    - The "height" of the L-function at the center.
    - Combined with all D: the L-function restricted to twists at the center.

    What this does NOT determine:
    - The zeros of L(s, pi_f x chi_D) at other points on the critical line.
    - The L^2 norm of the L-function on the critical line.
    - The zero density near s = 1/2.
    - Whether ALL zeros lie on Re(s) = 1/2.

    The MOMENT PROBLEM: if we know L(1/2, Sym^r f x chi_D) for ALL (r, D),
    we know all the Satake parameters alpha_p of f, because:
      L(s, Sym^r f) = prod_p prod_{j=0}^r (1 - alpha_p^j * conj(alpha_p)^{r-j} p^{-s})^{-1}
    and the central values determine the completed L-function up to a finite
    number of bad primes. But knowing the Satake parameters is EQUIVALENT to
    knowing the L-function, so the moment problem is in principle solvable.

    The catch: at FINITE genus g, we only know Sym^{r} for r <= g-1.
    The first g-1 symmetric powers determine a finite number of Newton sums
    of the Satake parameters, not all of them.
    """
    return {
        'genus_2_determines': [
            'L(1/2, pi_f x chi_D) for all fundamental D < 0',
            'Non-vanishing at center for each twist',
            'Relative sizes of central values across twists',
        ],
        'genus_2_does_not_determine': [
            'L(s, pi_f x chi_D) for s != 1/2 on critical line',
            'L^2(0,1) norm of Nyman-Beurling dilation functions',
            'Zero locations away from s = 1/2',
            'Zero density on critical line',
            'RH for the individual L-functions',
        ],
        'all_genera_determines': [
            'L(1/2, Sym^r f x chi_D) for all r >= 0 and all D',
            'All Satake parameters alpha_p (via moment problem)',
            'Full L-function L(s, f x chi_D) for all s',
            'Hence: all zeros (and RH if true)',
        ],
        'circularity_at_finite_g': (
            'At genus g, only Sym^r for r <= g-1 accessible. '
            'This gives the first g-1 power sums of Satake parameters, '
            'which determine alpha_p only for #(Satake params) <= g-1. '
            'For GL(2): 2 Satake params, so g >= 3 suffices for a SINGLE prime p, '
            'but not uniformly over all p.'
        ),
        'gap_d_conclusion': (
            'Gap D is NOT closable at any finite genus. The all-genera limit '
            'K^{(infty)} would close it in principle, but K^{(infty)} requires '
            'Langlands functoriality at all g (circularity). The gap between '
            '"spectral support matches" and "norm matches" is irreducible at '
            'finite genus.'
        ),
    }


# ============================================================================
# 3. SYMMETRIC POWER L-FUNCTIONS: CONDUCTOR GROWTH
# ============================================================================

def symmetric_power_conductor(g: int, weight: int = 22, level: int = 1) -> float:
    r"""Analytic conductor of L(s, Sym^{g-1} f) for f of given weight and level.

    The analytic conductor of L(s, Sym^n f) for f of weight k, level N is:
      C(Sym^n f) ~ N^n * prod_{j=0}^n (k-1+2j) / (2*pi)
    (up to constants depending on n).

    More precisely, the archimedean conductor (from Gamma factors):
      For Sym^n of a holomorphic form of weight k:
        Gamma factors at s=1/2: prod_{j=0}^n Gamma_R(s + mu_j)
        with mu_j = |k-1-2j|/2 for j = 0, ..., n.
      The conductor ~ prod (1 + |mu_j|).

    For the finite part: C_fin = N^{n+1} for level N.

    The TOTAL analytic conductor grows as ~ k^{(n+1)} * N^{n+1}.

    Parameters
    ----------
    g : int
        Genus (symmetric power is Sym^{g-1}).
    weight : int
        Weight of the elliptic eigenform.
    level : int
        Level (1 for full modular group).

    Returns
    -------
    float
        Log of the analytic conductor (base e).
    """
    n = g - 1  # symmetric power degree
    if n < 0:
        return 0.0

    # Archimedean part: product of (1 + |mu_j|) where mu_j = |weight-1-2j|/2
    log_arch = 0.0
    for j in range(n + 1):
        mu_j = abs(weight - 1 - 2 * j) / 2.0
        log_arch += math.log(1.0 + mu_j)

    # Finite part
    log_fin = (n + 1) * math.log(max(level, 1))

    return log_arch + log_fin


def keating_snaith_moment_prediction(g: int, weight: int = 22) -> Dict[str, Any]:
    r"""Random matrix prediction for |L(1/2, Sym^{g-1} f)|^2.

    Keating-Snaith (2000) predict that for a family of L-functions with
    analytic conductor C:
      <|L(1/2)|^{2k}> ~ a(k) * g(k) * (log C)^{k^2}

    where a(k) is an arithmetic factor and g(k) = G(1+k)^2/G(1+2k) with
    G the Barnes G-function.

    For the second moment (k=1):
      <|L(1/2)|^2> ~ (log C)

    For the family of quadratic twists L(1/2, Sym^{g-1} f x chi_D):
      C ~ |D|^{g} * C_infty(g, weight)

    So the "typical" central value squared is ~ g * log|D| + O(1).

    The kernel entry K^{(g)}(D,D) ~ sum_f |B_f(D)|^2 / <f,f> involves
    the Boecherer-type coefficients, which are proportional to central values
    (for SK lifts via Waldspurger, for genuine forms via Boecherer conjecture/DPSS20).

    Returns
    -------
    dict
        Predicted sizes and growth rates.
    """
    n = g - 1  # symmetric power degree
    log_cond = symmetric_power_conductor(g, weight)

    # Predicted typical |L(1/2)|^2 ~ log(conductor)
    predicted_moment = log_cond

    # Number of eigenforms contributing at genus g:
    # dim S_k(Sp(2g, Z)) grows polynomially in k and exponentially in g
    # For the Leech lattice at genus g, k = r/2 = 12.
    # Crude: dim ~ g^{O(g)} for fixed k.

    # For the kernel to converge, we need the contributions to be summable.
    # The kernel entry is K^{(g)} ~ dim * |L(1/2)|^2 * |D|^{k-2} / <f,f>
    # The Petersson norm <f,f> for Siegel forms of degree g grows as ~ C(f)^{g+1}
    # (Shimura). So the ratio |L(1/2)|^2 / <f,f> ~ (log C) / C^{g+1}.

    return {
        'genus': g,
        'sym_power_degree': n,
        'log_analytic_conductor': log_cond,
        'predicted_moment_second': predicted_moment,
        'convergence_factor': (
            f'|L(1/2)|^2 / <f,f> ~ log(C) / C^{{g+1}} which DOES converge '
            f'rapidly in g (the Petersson norm grows much faster than the central value).'
        ),
        'kernel_growth': (
            f'K^{{({g})}} contribution is suppressed by the Petersson norm. '
            f'The issue is not convergence of the SERIES but convergence of '
            f'the SPECTRAL CONTENT to the full critical-line data.'
        ),
    }


# ============================================================================
# 4. ROOT NUMBER AND NON-VANISHING
# ============================================================================

def symmetric_power_root_number(
    g: int,
    D: int,
    weight: int = 22,
) -> int:
    r"""Sign of the functional equation for L(s, Sym^{g-1} f x chi_D).

    The functional equation is L(s, pi) = epsilon(pi) * L(1-s, tilde{pi}).
    For self-dual representations (like symmetric powers of GL(2)):
      epsilon = +1 or -1.
    If epsilon = -1, then L(1/2, pi) = 0 (forced vanishing).

    For Sym^n(f) with f of weight k, level 1:
    - Sym^n is self-dual since f has trivial nebentypus.
    - epsilon(Sym^n f) = (-1)^{n(n+1)/2} * ... (depends on level, character).
    - For level 1 and trivial character:
        epsilon(Sym^n f) = (-1)^{floor(n/2)} when n is even
                         = +1                 when n is odd

    Twisting by chi_D:
    - epsilon(Sym^n f x chi_D) = epsilon(Sym^n f) * chi_D(-1)^{n+1} * |D|^{...} / ...
    - For fundamental D < 0: chi_D(-1) = -1 (since D < 0, the field is imaginary).
    - So twisting by chi_D multiplies the root number by (-1)^{n+1} when D < 0.

    Combining: epsilon(Sym^n f x chi_D) = (-1)^{floor(n/2)} * (-1)^{n+1} for D < 0.

    This is a simplified analysis. The actual root number depends on local factors
    at all primes dividing the conductor. For level 1, only the archimedean
    factor matters.

    Parameters
    ----------
    g : int
        Genus (Sym^{g-1}).
    D : int
        Fundamental discriminant (D < 0).
    weight : int
        Weight of the eigenform.

    Returns
    -------
    int
        +1 or -1 (predicted root number).
    """
    n = g - 1  # symmetric power degree

    # Simplified root number computation for level 1, weight k, Sym^n, twist chi_D
    # This is an APPROXIMATION (ignoring ramified local factors beyond archimedean).

    # Archimedean sign: depends on n and weight parity
    if n % 2 == 0:
        arch_sign = (-1) ** (n // 2)
    else:
        arch_sign = 1

    # Twist sign for D < 0
    if D < 0:
        twist_sign = (-1) ** (n + 1)
    else:
        twist_sign = 1

    return arch_sign * twist_sign


def root_number_table(
    genus_max: int = 12,
    disc_list: Optional[List[int]] = None,
) -> Dict[str, Any]:
    r"""Compute root numbers for L(1/2, Sym^{g-1} f_{22} x chi_D) across genera.

    When epsilon = -1, L(1/2) = 0 is forced. These are "parity zeros" that
    create rank defects in K^{(g)}.

    Returns a table of (g, D) -> epsilon, plus statistics.
    """
    if disc_list is None:
        disc_list = [-3, -4, -7, -8, -11, -15, -20, -24, -35, -40]

    table = {}
    forced_vanishing = []
    for g in range(1, genus_max + 1):
        for D in disc_list:
            eps = symmetric_power_root_number(g, D)
            table[(g, D)] = eps
            if eps == -1:
                forced_vanishing.append((g, D))

    # Statistics
    total = len(table)
    n_minus = len(forced_vanishing)

    return {
        'table': table,
        'forced_vanishing': forced_vanishing,
        'total_entries': total,
        'n_forced_zero': n_minus,
        'fraction_forced_zero': n_minus / total if total > 0 else 0,
        'genera_with_all_negative': [
            g for g in range(1, genus_max + 1)
            if all(table.get((g, D), 1) == -1 for D in disc_list)
        ],
        'conclusion': (
            f'{n_minus}/{total} entries have epsilon=-1 (forced vanishing). '
            f'These create rank defects in the genus-g Beurling kernel. '
            f'The all-genera kernel inherits these gaps: at each genus, '
            f'certain discriminants contribute zero to the kernel.'
        ),
    }


# ============================================================================
# 5. CIRCULARITY ANALYSIS: SYMMETRIC POWER FUNCTORIALITY STATUS
# ============================================================================

def sym_power_functoriality_status() -> Dict[str, Any]:
    r"""Status of Sym^n: GL(2) -> GL(n+1) functoriality.

    The Langlands functoriality conjecture predicts the existence of the
    symmetric power transfer for automorphic representations. The status:

    UNCONDITIONAL (for all automorphic forms on GL(2)):
      Sym^1: trivial (identity)
      Sym^2: Gelbart-Jacquet (1978)
      Sym^3: Kim-Shahidi (2002)
      Sym^4: Kim (2003)

    CONDITIONAL / PARTIAL:
      Sym^n for all n: Newton-Thorne (2021), but ONLY for regular algebraic
      automorphic representations of GL(2) over totally real fields with
      distinct Hodge-Tate weights. This covers:
        - Holomorphic modular forms of weight >= 2 for GL(2)/Q
        - Hilbert modular forms of parallel weight >= 2
      Does NOT cover:
        - Maass forms (non-algebraic)
        - Weight 1 forms
        - Forms over non-totally-real fields

    For the arithmetic programme:
      - The eigenform f_22 (weight 22, level 1) IS covered by Newton-Thorne.
      - Sym^n f_22 is automorphic for ALL n (unconditional).
      - The Boecherer-type factorization at genus g requires Sym^{g-1}.
        For f_22: this is unconditional at all g.
      - BUT: the programme aims to prove things about L-functions MORE GENERALLY.
        For a general L-function L(s, pi), Sym^n pi for n >= 5 is open.

    The circularity: the programme uses Sym^{g-1} functoriality as an INPUT
    to access central L-values at genus g. If the goal is to prove properties
    of L-functions (like RH) that would IMPLY functoriality, then using
    functoriality as an input is circular.

    HOWEVER: for the specific case of f_22 (or any holomorphic eigenform of
    weight >= 2 over Q), there is NO circularity because Newton-Thorne is
    unconditional. The circularity only arises when trying to extend the
    programme beyond the holomorphic-algebraic regime.
    """
    status = {}
    for n in range(1, 20):
        if n <= 1:
            status[n] = {
                'status': 'UNCONDITIONAL',
                'reference': 'trivial',
                'covers': 'all GL(2) automorphic representations',
            }
        elif n == 2:
            status[n] = {
                'status': 'UNCONDITIONAL',
                'reference': 'Gelbart-Jacquet 1978',
                'covers': 'all GL(2) automorphic representations',
            }
        elif n == 3:
            status[n] = {
                'status': 'UNCONDITIONAL',
                'reference': 'Kim-Shahidi 2002',
                'covers': 'all GL(2) automorphic representations',
            }
        elif n == 4:
            status[n] = {
                'status': 'UNCONDITIONAL',
                'reference': 'Kim 2003',
                'covers': 'all GL(2) automorphic representations',
            }
        else:
            status[n] = {
                'status': 'CONDITIONAL',
                'reference': 'Newton-Thorne 2021 (holomorphic wt >= 2 over totally real)',
                'covers': (
                    'holomorphic modular forms of weight >= 2 over totally real fields; '
                    'NOT Maass forms, NOT weight 1'
                ),
                'unconditional_for_f22': True,
                'unconditional_for_general': False,
            }

    return {
        'symmetric_powers': status,
        'newton_thorne_scope': (
            'Newton-Thorne (2021) proves Sym^n for all n, but only for regular '
            'algebraic (= holomorphic weight >= 2) automorphic representations '
            'of GL(2) over totally real fields. For f_22 specifically: unconditional '
            'at all n.'
        ),
        'circularity_assessment': {
            'for_f22': (
                'NO circularity for f_22 (weight 22, level 1). Newton-Thorne gives '
                'Sym^n f_22 for all n unconditionally. The programme can access '
                'L(1/2, Sym^{g-1} f_22 x chi_D) at all genera without circular inputs.'
            ),
            'for_general_forms': (
                'CIRCULARITY EXISTS for Maass forms and weight-1 forms. Sym^n for n >= 5 '
                'is open for these. If the programme aims to prove RH for such L-functions '
                'using the all-genera Beurling kernel, it would need Sym^n as input, '
                'creating a logical circle.'
            ),
            'structural_assessment': (
                'The circularity is PARTIAL, not total. For the holomorphic algebraic '
                'regime (weight >= 2, totally real), Newton-Thorne breaks the circle. '
                'The programme can proceed unconditionally within this regime. Extension '
                'to Maass forms requires new ideas.'
            ),
        },
    }


def circularity_genus_frontier(weight: int = 22) -> Dict[str, Any]:
    r"""For each genus g, determine whether the Beurling kernel K^{(g)} is
    unconditionally defined.

    Unconditional if either:
    (a) g <= 5 (Sym^{g-1} is unconditional for all GL(2) forms), or
    (b) The eigenform is holomorphic of weight >= 2 (Newton-Thorne applies at all g).

    For the Leech lattice theta series with f_22 (weight 22): unconditional at all g.
    For a hypothetical Maass form contribution: unconditional only for g <= 5.
    """
    results = {}
    for g in range(1, 20):
        n = g - 1  # symmetric power degree
        unconditional_general = n <= 4  # Kim's theorem covers Sym^4
        unconditional_holomorphic = True  # Newton-Thorne

        results[g] = {
            'sym_power_degree': n,
            'unconditional_for_all_GL2': unconditional_general,
            'unconditional_for_holomorphic_wt_ge_2': unconditional_holomorphic,
            'unconditional_for_f22': True,  # always
            'reference': (
                'trivial' if n == 0 else
                'Gelbart-Jacquet 1978' if n == 1 else
                'Gelbart-Jacquet 1978' if n == 2 else
                'Kim-Shahidi 2002' if n == 3 else
                'Kim 2003' if n == 4 else
                'Newton-Thorne 2021 (holomorphic only)'
            ),
        }

    return {
        'genus_table': results,
        'circularity_frontier_general': 5,  # last genus unconditional for all GL(2)
        'circularity_frontier_holomorphic': float('inf'),  # no frontier for weight >= 2
        'conclusion': (
            'For holomorphic eigenforms of weight >= 2 (including f_22 relevant '
            'to the Leech lattice): the Beurling kernel K^{(g)} is unconditionally '
            'defined at ALL genera. Newton-Thorne (2021) eliminates the circularity '
            'in this regime. For Maass forms: circularity begins at genus 6.'
        ),
    }


# ============================================================================
# 6. ALL-GENERA KERNEL: CONVERGENCE ANALYSIS
# ============================================================================

def all_genera_kernel_convergence(
    genus_max: int = 15,
    weight: int = 22,
    disc_list: Optional[List[int]] = None,
) -> Dict[str, Any]:
    r"""Analyze convergence of K^{(infty)} = varprojlim_g K^{(g)}.

    The kernel at genus g involves:
      K^{(g)}(D, D') = sum_{f in B_k(Sp(2g,Z))} B_f(D) * conj(B_f(D')) / <f,f>

    For convergence of the projective limit, we need the contributions at
    successive genera to stabilize or decay.

    KEY ISSUES:
    1. The spaces S_k(Sp(2g,Z)) grow with g (more eigenforms contribute).
    2. The Petersson norms <f,f> also grow with g.
    3. The Boecherer coefficients B_f(D) may grow or decay.

    The FORMAL structure of the projective limit:
      K^{(infty)} is NOT a direct sum/limit of K^{(g)}.
      Rather, the escalation principle says the SPECTRAL CONTENT increases
      with g. At genus g, K^{(g)} accesses Sym^{g-1} L-values; as g -> infty,
      these cover all automorphic spectral data.

    The convergence question is whether the MAP from genus-g MC data to the
    Beurling kernel converges, not whether the kernel entries converge.

    QUANTITATIVE: We estimate the contribution at each genus via conductor growth.
    """
    if disc_list is None:
        disc_list = [-3, -4, -7, -8, -11, -15, -20, -24]

    genus_data = []
    for g in range(1, genus_max + 1):
        log_cond = symmetric_power_conductor(g, weight)

        # Dimension of S_{weight/2}(Sp(2g, Z)) — crude estimate
        # For g = 1: dim S_{11}(SL_2(Z)) = 0 (weight 11 is odd, use weight 22: dim = 1)
        # For g = 2: dim S_{12}(Sp(4,Z)) = 1
        # For g >= 3: grows rapidly
        # Crude: dim ~ g^{g} / g! (by Weyl character formula asymptotics)
        if g == 1:
            dim_est = 1  # S_22(SL_2(Z))
        elif g == 2:
            dim_est = 1  # S_12(Sp(4,Z))
        else:
            # Very rough: dim S_k(Sp(2g,Z)) ~ (k-g)^{g(g+1)/2} / prod_{j=1}^g j!
            # for k >> g. Here k = 12 (Leech lattice, rank 24, k = r/2 = 12).
            # For g >= 3, k = 12 is SMALL relative to g, so many spaces vanish.
            # Actually: for g > k, S_k(Sp(2g,Z)) = 0 by the Witt bound.
            # For k = 12: nonzero only for g <= 12 roughly.
            if g <= 12:
                dim_est = max(0, int(math.comb(g + 2, 3) * 0.1))
            else:
                dim_est = 0

        # Root number: fraction of D with forced vanishing
        n_forced = sum(
            1 for D in disc_list
            if symmetric_power_root_number(g, D) == -1
        )

        genus_data.append({
            'genus': g,
            'sym_power_degree': g - 1,
            'log_analytic_conductor': log_cond,
            'cusp_space_dim_estimate': dim_est,
            'n_forced_vanishing': n_forced,
            'n_disc': len(disc_list),
            'fraction_forced_vanishing': n_forced / len(disc_list),
        })

    # Convergence assessment
    # The key quantity: does K^{(g)} add "new spectral information" at each g?
    # At genus g, K^{(g)} involves Sym^{g-1}. The NEW information at genus g
    # compared to genus g-1 is the (g-1)-th symmetric power.
    # Newton's identities: the first n power sums p_1, ..., p_n determine
    # the first n elementary symmetric polynomials e_1, ..., e_n.
    # For GL(2): Satake has 2 parameters (alpha_p, beta_p).
    # p_1 = alpha + beta = a(p), p_2 = alpha^2 + beta^2 = a(p)^2 - 2p^{k-1}.
    # So: p_1 determines {alpha+beta, alpha*beta} completely.
    # Extra Sym^r for r >= 2 gives redundant information for GL(2)!
    # The VALUE is in the TWISTED central values L(1/2, ... x chi_D),
    # which give information about the ANALYTIC BEHAVIOR, not just Satake params.

    return {
        'genus_data': genus_data,
        'convergence_assessment': (
            'The projective limit K^{(infty)} is well-defined formally as a '
            'compatible system of positive semi-definite kernels. Convergence '
            'in the operator norm is GUARANTEED because each K^{(g)} adds a '
            'positive semi-definite correction (new eigenforms contribute new '
            'rank-one terms). The limit exists as a positive operator on '
            'ell^2(fundamental discriminants). The QUESTION is whether the '
            'limit operator has the same KERNEL (null space) as the NB operator.'
        ),
        'spectral_completeness': (
            'At genus g, the kernel encodes L(1/2, Sym^{g-1} f x chi_D). For GL(2), '
            'Sym^1 already determines the Satake parameters. The higher symmetric '
            'powers give ANALYTIC information (central values of higher L-functions) '
            'rather than new arithmetic information. The all-genera limit captures '
            'the full "motivic" content of f, which includes all L-values — and hence '
            'all zeros by Weierstrass factorization — but only at the FORMAL level.'
        ),
        'operator_convergence': (
            'CONVERGENT: K^{(g)} is a monotone increasing sequence of PSD operators '
            '(each genus adds new eigenforms). The limit K^{(infty)} exists as a '
            'bounded operator. But "K^{(infty)} has the same null space as NB" is '
            'a statement about completeness, not convergence — and completeness '
            'requires Langlands functoriality (circularity for Maass forms).'
        ),
    }


# ============================================================================
# 7. MOMENT PROBLEM: SATAKE PARAMETER RECOVERY
# ============================================================================

def satake_recovery_from_central_values(
    genus_max: int = 10,
) -> Dict[str, Any]:
    r"""Analyze how many Satake parameters can be recovered from genus-g data.

    For GL(2): the Satake parameters at prime p are (alpha_p, beta_p) with
    alpha_p * beta_p = p^{k-1} and alpha_p + beta_p = a_f(p).

    The symmetric power L-values give:
      L(s, Sym^n f) = prod_p prod_{j=0}^n (1 - alpha_p^{n-j} beta_p^j p^{-s})^{-1}

    The central value L(1/2, Sym^n f x chi_D) encodes information about
    the n-th power sums of the Satake parameters ACROSS all primes (weighted
    by chi_D and the Dirichlet series).

    For GL(2), alpha_p and beta_p are determined by a_f(p) alone (since
    alpha*beta = p^{k-1} is known). So Sym^1 suffices for Satake recovery.
    The higher symmetric powers provide ANALYTIC information: they determine
    the L-function at the center, which encodes zero distribution information.

    For GL(n) with n > 2: the Satake parameters are n complex numbers with
    constraints. Recovery requires Sym^r for r up to n-1 (by Newton's identities).
    """
    recovery_data = []
    for g in range(1, genus_max + 1):
        n = g - 1  # available symmetric power

        # For GL(2): n = 0 gives Sym^0 = trivial (just zeta), no Satake info.
        # n = 1 gives L(s, f) which determines a_f(p) for all p -> full Satake.
        # n >= 2: redundant for GL(2) Satake, but gives new L-values.

        if n == 0:
            satake_info = 'None (trivial L-function)'
            analytic_info = 'zeta-values only'
        elif n == 1:
            satake_info = 'COMPLETE for GL(2) (a_f(p) determines alpha_p, beta_p)'
            analytic_info = 'L(1/2, f x chi_D) for all D'
        else:
            satake_info = f'Redundant for GL(2); needed for GL({n+1})'
            analytic_info = f'L(1/2, Sym^{n} f x chi_D) for all D'

        recovery_data.append({
            'genus': g,
            'sym_power': n,
            'satake_recovery': satake_info,
            'analytic_content': analytic_info,
        })

    return {
        'recovery_data': recovery_data,
        'gl2_satake_genus': 2,  # genus 2 (Sym^1) suffices for GL(2) Satake
        'analytic_content_new_at_genus': (
            'Each genus adds L(1/2, Sym^{g-1} f x chi_D). For GL(2), '
            'this is analytically new information (a new L-function value) '
            'but arithmetically redundant (the Satake parameters are already '
            'known from Sym^1). The value is in the ANALYTIC side: central '
            'values of higher symmetric powers encode the "shape" of the '
            'L-function, needed for the Nyman-Beurling L^2 norm.'
        ),
    }


# ============================================================================
# 8. COMPARISON: WHAT GENUS-2 ACHIEVES VS WHAT NB NEEDS
# ============================================================================

def gap_d_quantitative_analysis(
    nmax_nb: int = 1000,
) -> Dict[str, Any]:
    r"""Quantitative comparison of genus-2 Beurling kernel vs NB criterion.

    The NB criterion: RH iff d_N = dist(1, span{rho_theta}) -> 0.
    The genus-2 kernel K^{(2)} provides: L(1/2, pi_f x chi_D) for SK lifts.

    The gap: K^{(2)} gives a FINITE-RANK approximation to the NB kernel.
    The NB kernel has INFINITE rank (it involves all zeta-zeros).

    We estimate:
    1. The rank of K^{(2)} for the Leech lattice (= dim S_12(Sp(4,Z)) = 1).
    2. The distance from K^{(2)} to the NB kernel in operator norm.
    3. The rate at which K^{(g)} approaches the NB kernel.
    """
    # NB Gram matrix for some thetas
    thetas = [1 / n for n in range(2, 12)]  # theta = 1/2, 1/3, ..., 1/11
    nb_data = nyman_beurling_distance_to_one(thetas, nmax=nmax_nb)

    # Genus-2 rank
    leech_rank = 1  # dim S_12(Sp(4,Z)) = 1

    # Rough estimate: the NB kernel at these thetas has rank ~ len(thetas)
    # The genus-2 kernel is rank 1. The "fraction of NB information captured"
    # is ~ 1 / (effective NB rank).
    nb_effective_rank = nb_data['gram_rank']

    return {
        'nb_distance': nb_data,
        'genus_2_kernel_rank': leech_rank,
        'nb_gram_effective_rank': nb_effective_rank,
        'rank_deficit': nb_effective_rank - leech_rank,
        'information_fraction': (
            f'K^{{(2)}} has rank {leech_rank}; the NB Gram matrix has effective '
            f'rank {nb_effective_rank}. The genus-2 kernel captures '
            f'~{100*leech_rank/max(1,nb_effective_rank):.1f}% of the NB degrees '
            f'of freedom.'
        ),
        'gap_d_conclusion': (
            'Gap D is NOT closable at genus 2. The genus-2 kernel provides a '
            'rank-1 positive operator (from the unique Siegel cusp form chi_12), '
            'while the NB criterion requires approximation of a unit function '
            'in an infinite-dimensional L^2 space. The spectral support matches '
            '(both on Re(s)=1/2), but the rank is far too low. Higher genera '
            'increase the rank, but Gap D requires the all-genera limit '
            'K^{(infty)}.'
        ),
    }


# ============================================================================
# 9. GENUS-g BOECHERER-TYPE FORMULA: STRUCTURE
# ============================================================================

def genus_g_boecherer_structure(g: int) -> Dict[str, Any]:
    r"""Describe the expected Boecherer-type formula at genus g.

    At genus 1: Rankin-Selberg integral, L-values at Re(s) > 1.
    At genus 2: Boecherer factorization, L(1/2, pi_f x chi_D) via Waldspurger.
    At genus g: Conjectural Boecherer-type, L(1/2, pi_F) for GSp(2g) automorphic
                representations F. Via symmetric power transfer:
                    pi_F  contains  Sym^{g-1}(pi_f)  component
                which accesses L(1/2, Sym^{g-1} f x chi_D).

    The Boecherer conjecture at genus g is:
    For a degree-g Siegel Hecke eigenform F with spinor L-function L(s, F, spin),
      |B_F(D)|^2 / <F, F>  =  C(F) * L(1/2, F, spin x chi_D) * |D|^{...}

    The refined version (Furusawa-Morimoto for g=2, conjectural for g >= 3)
    relates the Fourier coefficients to central L-values with explicit constants.

    Status:
    - g = 1: classical (Hecke theory, no Boecherer needed)
    - g = 2: proved for SK lifts (Waldspurger), proved for genuine forms (DPSS20)
    - g = 3: conjectural (some cases by Heim, Katsurada, Kohnen)
    - g >= 4: conjectural (open, part of the Langlands programme)
    """
    if g == 1:
        return {
            'genus': g,
            'status': 'CLASSICAL',
            'l_function': 'L(s, f) via Rankin-Selberg (Re(s) > 1)',
            'central_access': False,
            'reference': 'Hecke 1937',
        }
    elif g == 2:
        return {
            'genus': g,
            'status': 'PROVED',
            'l_function': 'L(1/2, pi_F x chi_D) at center',
            'central_access': True,
            'reference': 'Waldspurger 1981 (SK); DPSS20 (genuine)',
            'sk_mechanism': 'Waldspurger: |c(|D|)|^2 ~ L(k-1, g x chi_D) |D|^{k-2}',
            'genuine_mechanism': 'Boecherer conjecture (DPSS20)',
        }
    elif g == 3:
        return {
            'genus': g,
            'status': 'PARTIALLY PROVED',
            'l_function': 'L(1/2, pi_F x chi_D) for Sp(6)',
            'central_access': True,
            'reference': 'Heim, Katsurada-Kohnen (partial cases)',
            'sym_power_needed': 'Sym^2 (Gelbart-Jacquet: unconditional)',
        }
    else:
        return {
            'genus': g,
            'status': 'CONJECTURAL',
            'l_function': f'L(1/2, pi_F x chi_D) for GSp({2*g})',
            'central_access': True,
            'reference': f'Langlands programme (Sym^{g-1} transfer needed)',
            'sym_power_needed': f'Sym^{g-1}',
            'sym_power_status': (
                'unconditional for holomorphic wt >= 2 (Newton-Thorne)' if g - 1 >= 5
                else f'unconditional ({"Kim" if g-1 == 4 else "Kim-Shahidi" if g-1 == 3 else "Gelbart-Jacquet"})'
            ),
        }


# ============================================================================
# 10. COMBINED ASSESSMENT
# ============================================================================

def full_gap_d_analysis(
    genus_max: int = 12,
    nmax_nb: int = 800,
) -> Dict[str, Any]:
    r"""Complete analysis of Gap D: norm mismatch, convergence, circularity.

    Returns a structured assessment of:
    1. What genus-2 achieves (spectral support match, but rank-1 kernel).
    2. Whether K^{(infty)} converges (yes, as a positive operator).
    3. Whether K^{(infty)} closes Gap D (requires Langlands for Maass forms;
       unconditional for holomorphic weight >= 2).
    4. The circularity (partial: broken by Newton-Thorne for algebraic regime).
    """
    # Part 1: Central value information content
    info = central_value_information_content()

    # Part 2: Conductor growth and moments
    moments = [
        keating_snaith_moment_prediction(g)
        for g in range(1, min(genus_max, 8) + 1)
    ]

    # Part 3: Root numbers and forced vanishing
    root_nums = root_number_table(genus_max)

    # Part 4: Circularity
    circ = circularity_genus_frontier()

    # Part 5: Convergence
    conv = all_genera_kernel_convergence(genus_max)

    # Part 6: Quantitative gap (NB distance)
    try:
        gap_quant = gap_d_quantitative_analysis(nmax_nb)
    except Exception:
        gap_quant = {'error': 'NB computation failed'}

    # Part 7: Moment/Satake recovery
    satake = satake_recovery_from_central_values()

    # Part 8: Boecherer structure at each genus
    boecherer = {g: genus_g_boecherer_structure(g) for g in range(1, min(genus_max, 6) + 1)}

    return {
        'central_value_info': info,
        'moment_predictions': moments,
        'root_numbers': root_nums,
        'circularity': circ,
        'convergence': conv,
        'quantitative_gap': gap_quant,
        'satake_recovery': satake,
        'boecherer_genus_g': boecherer,
        'summary': {
            'can_central_values_close_gap_d': (
                'NO at finite genus. The genus-2 kernel K^{(2)} lives on Re(s)=1/2 '
                '(correct spectral support) but has rank 1 (far too low). Central '
                'values at s=1/2 do not determine the L^2 norm on the full critical '
                'line. The all-genera limit K^{(infty)} would in principle capture '
                'all spectral data, but requires: (a) Boecherer-type formulas at all '
                'genera (conjectural for g >= 4), and (b) the ANALYTICAL content of '
                'knowing L(1/2, Sym^{g-1} f x chi_D) for all g to reconstruct the '
                'full L-function.'
            ),
            'does_k_infty_converge': (
                'YES as a positive operator. K^{(g)} is a monotone increasing '
                'sequence of PSD operators. The limit exists and is bounded. '
                'But convergence of the OPERATOR is not the same as convergence of '
                'the SPECTRAL CONTENT to the Nyman-Beurling spectral content. The '
                'latter requires completeness of the symmetric power family, which '
                'is a deep result in automorphic forms.'
            ),
            'the_circularity': (
                'PARTIAL. For holomorphic eigenforms of weight >= 2 (including f_22): '
                'NO circularity. Newton-Thorne (2021) proves Sym^n for all n '
                'unconditionally in this regime. For Maass forms: circularity begins '
                'at genus 6 (Sym^5 is the last unconditional symmetric power for '
                'general GL(2) forms). The programme is self-consistent within the '
                'holomorphic algebraic regime but cannot bootstrap to the full '
                'automorphic landscape without external input.'
            ),
        },
    }
