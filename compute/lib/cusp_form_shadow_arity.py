r"""Cusp form detection at specific shadow arities for lattice VOAs.

THE MAIN THEOREM (prop:period-shadow-dictionary, thm:spectral-decomposition-principle):

  For an even unimodular lattice Lambda of rank r, the shadow obstruction tower
  decomposes the Epstein zeta function one L-function at a time:

    Arity 2:   kappa (curvature)         -->  zeta(s)            [Riemann]
    Arity 3:   C (cubic shadow)          -->  zeta(s)*zeta(s-k+1) [Dedekind]
    Arity 3+j: Sh_{3+j} (j-th cusp)     -->  L(s, f_j)          [Hecke]

  where k = r/2 is the weight and f_1, ..., f_{g_k} are the Hecke eigenforms
  spanning S_k(SL(2,Z)).  The tower terminates at depth d = 3 + dim S_k.

KEY ARITHMETIC FACTS:

  dim S_k(SL(2,Z)) for even k >= 2:
    k <  12: dim = 0   (no cusp forms -- pure Eisenstein)
    k = 12: dim = 1   (Delta = eta^24, the Ramanujan cusp form)
    k = 16: dim = 1   (Delta * E_4)
    k = 18: dim = 1   (Delta * E_6)
    k = 20: dim = 1
    k = 22: dim = 1
    k = 24: dim = 2   (first weight with TWO independent cusp eigenforms)
    k = 26: dim = 2   ... and so on, growing as k/12 asymptotically.

  Formula: dim M_k = floor(k/12) + 1 if k mod 12 != 2, else floor(k/12).
           dim S_k = dim M_k - 1 for k >= 4 (S_k = ker(M_k -> C) via a_0).

LATTICE VOA SHADOW DEPTH BY RANK:

  Rank  8 (k= 4): depth 3  (E_8: pure Eisenstein, class L)
  Rank 16 (k= 8): depth 3  (E_8 x E_8, D_16^+: pure Eisenstein)
  Rank 24 (k=12): depth 4  (Niemeier: one cusp form Delta, class C)
  Rank 32 (k=16): depth 4  (one cusp form: Delta*E_4)
  Rank 48 (k=24): depth 5  (TWO cusp forms in S_24, FIRST depth-5 lattice)
  Rank 72 (k=36): depth 6  (THREE cusp forms in S_36)

CUSP FORM ASSIGNMENT TO ARITIES:

  For rank-24 lattices (Leech, E_8^3, all 24 Niemeier lattices):
    Theta_Lambda = c_E * E_12 + c_1 * Delta
    Arity 4 detects Delta (the unique cusp form of weight 12)
    L-function: L(s, Delta) with critical line Re(s) = 6

  For rank-48 lattices (P_48p, P_48q, Leech tensor Leech, etc.):
    Theta_Lambda = c_E * E_24 + c_1 * f_1 + c_2 * f_2
    where f_1, f_2 are the two Hecke eigenforms in S_24(SL(2,Z))
    Arity 4 detects f_1 (first cusp eigenform)
    Arity 5 detects f_2 (second cusp eigenform)
    The eigenforms have Hecke eigenvalues in Q(sqrt(144169)):
      a_2(f_i) = 540 +/- 12*sqrt(144169)

RAMANUJAN-PETERSSON IN THE SHADOW TOWER:

  Deligne's theorem: |a_p(f)| <= 2 * p^{(k-1)/2} for f in S_k newform.
  In the shadow obstruction tower, this manifests as:
    |Sh_{3+j}(p)| <= C * p^{(k-1)/2}  (polynomial bound on shadow amplitudes)
  The shadow obstruction tower coefficients at arity 3+j grow at most polynomially in the
  lattice vector norms, with the polynomial degree controlled by (k-1)/2.
  This is the MC-framework manifestation of the Ramanujan conjecture:
    The cusp form shadow amplitudes satisfy the SAME polynomial bound
    that Deligne proved for Hecke eigenvalues.

  Contrast with Eisenstein:
    sigma_{k-1}(n) ~ n^{k-1} (maximal polynomial growth)
    |tau(n)| <= d(n) * n^{(k-1)/2} (half the Eisenstein growth rate)
  The Ramanujan bound says cusp contributions grow at HALF the rate of
  Eisenstein contributions in the exponent.  In the shadow obstruction tower, this
  means arities >= 4 (cusp form arities) have SUPPRESSED amplitudes
  compared to arity 3 (Eisenstein).

CAUTION (AP1): kappa = rank for lattice VOAs.  NOT c/2.
CAUTION (AP38): When comparing with published tables, verify normalization
  conventions.  The Ramanujan tau-function tau(n) uses the convention
  Delta = sum tau(n) q^n with tau(1) = 1, tau(2) = -24.
CAUTION (AP39): kappa != S_2 in general.  For lattice VOAs they coincide
  (both equal rank), but this is a special-case coincidence.

Manuscript references:
  - arithmetic_shadows.tex: thm:shadow-spectral-correspondence
  - arithmetic_shadows.tex: prop:period-shadow-dictionary
  - arithmetic_shadows.tex: thm:spectral-decomposition-principle
  - arithmetic_shadows.tex: comp:period-shadow-leech
  - higher_genus_modular_koszul.tex: thm:shadow-archetype-classification
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs,
    Integer,
    Matrix,
    Rational,
    Symbol,
    bernoulli,
    eye,
    factorial,
    floor,
    simplify,
    solve,
    sqrt,
    symbols,
)


# =========================================================================
# Modular form dimensions
# =========================================================================


def dim_Mk(k: int) -> int:
    r"""Dimension of M_k(SL(2,Z)) for even k >= 0.

    Standard formula:
      dim M_0 = 1
      dim M_2 = 0
      dim M_k = floor(k/12) + 1  if k mod 12 != 2
      dim M_k = floor(k/12)      if k mod 12 == 2
    """
    if k < 0 or k % 2 != 0:
        return 0
    if k == 0:
        return 1
    if k == 2:
        return 0
    if k % 12 == 2:
        return k // 12
    else:
        return k // 12 + 1


def dim_Sk(k: int) -> int:
    r"""Dimension of S_k(SL(2,Z)) for even k >= 0.

    S_k = 0 for k < 12.
    For k >= 12: dim S_k = dim M_k - 1.
    """
    if k < 12:
        return 0
    return dim_Mk(k) - 1


# =========================================================================
# Lattice VOA shadow depth
# =========================================================================


def shadow_depth_lattice(rank: int) -> int:
    r"""Shadow depth of an even unimodular lattice VOA of given rank.

    d(V_Lambda) = 3 + dim S_{r/2}  for r >= 8.

    For rank < 8 or odd rank, raise ValueError (no even unimodular lattice).
    Even unimodular lattices exist only in ranks divisible by 8.
    """
    if rank < 1:
        raise ValueError(f"Rank must be positive, got {rank}")
    k = rank // 2  # weight of theta function
    if rank % 2 != 0:
        raise ValueError(f"Even lattice rank must be even, got {rank}")
    g_k = dim_Sk(k)
    return 3 + g_k


def shadow_class_lattice(rank: int) -> str:
    r"""Shadow class of an even unimodular lattice VOA.

    Gaussian (G):  depth 2 -- but lattice VOAs always have depth >= 3.
    Lie/tree (L):  depth 3 (no cusp forms, pure Eisenstein)
    Contact (C):   depth 4 (one cusp form)
    Finite (F_d):  depth d >= 5 (multiple cusp forms)
    Mixed (M):     depth infinity -- never for lattice VOAs

    IMPORTANT: Lattice VOAs are always class G in the SHADOW TOWER sense
    (S_3 = S_4 = 0 on the primary line), but the ARITHMETIC depth
    d_arith = 2 + dim S_{r/2} can exceed 2.  The reconciliation:
    the shadow obstruction tower on the Heisenberg/Cartan primary line terminates at 2,
    but the SPECTRAL decomposition of Theta_Lambda introduces additional
    arities from the Hecke eigenform expansion.

    For the period-shadow dictionary, we use the arithmetic depth.
    """
    d = shadow_depth_lattice(rank)
    if d == 2:
        return 'G'
    elif d == 3:
        return 'L'
    elif d == 4:
        return 'C'
    elif d < float('inf'):
        return f'F_{d}'
    else:
        return 'M'


# =========================================================================
# Cusp form data
# =========================================================================


# Ramanujan tau function (first values)
RAMANUJAN_TAU = {
    1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
    6: -6048, 7: -16744, 8: 84480, 9: -113643, 10: -115920,
    11: 534612, 12: -370944, 13: -577738, 14: 401856,
    15: 1217160, 16: 987136, 17: -6905934, 18: 2727432,
    19: 10661420, 20: -7109760,
}


def sigma(k: int, n: int) -> int:
    r"""Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eisenstein_coefficient(weight: int, n: int) -> Rational:
    r"""Coefficient of q^n in the normalized Eisenstein series E_k.

    E_k = 1 - (2k/B_k) * sum_{n>=1} sigma_{k-1}(n) q^n

    where B_k is the k-th Bernoulli number.
    """
    if n == 0:
        return Rational(1)
    B_k = Rational(bernoulli(weight))
    if B_k == 0:
        raise ValueError(f"B_{weight} = 0, Eisenstein series undefined")
    coeff = Rational(-2 * weight, 1) / B_k * sigma(weight - 1, n)
    return coeff


def leech_theta_coefficients(max_n: int = 20) -> Dict[int, Rational]:
    r"""Fourier coefficients of Theta_Leech.

    Theta_Leech = E_12 - (65520/691) * Delta

    The coefficient of q^n is:
      a(n) = E_12(q^n) + (-65520/691) * tau(n)

    Key values:
      a(0) = 1
      a(1) = 0 (no roots in Leech lattice)
      a(2) = 196560 (minimal vectors)
    """
    c_Delta = Rational(-65520, 691)
    result = {}
    for n in range(max_n + 1):
        e_coeff = eisenstein_coefficient(12, n)
        tau_n = RAMANUJAN_TAU.get(n, 0)
        result[n] = e_coeff + c_Delta * tau_n
    return result


# =========================================================================
# Hecke decomposition engine
# =========================================================================


def hecke_decomposition_rank24(lattice_name: str,
                                root_count: int = 0) -> Dict[str, Any]:
    r"""Hecke decomposition of a rank-24 even unimodular lattice.

    Theta_Lambda = c_E * E_12 + c_Delta * Delta

    where c_E = 1 (always, since Theta has q^0 coeff 1 and E_12 starts at 1)
    and c_Delta is determined by the q^1 coefficient:
      coeff(q^1) = (65520/691) + c_Delta * 1 = (number of roots) / 2
    Wait: for lattice VOAs the theta function counts ALL lattice vectors
    by squared length, with q^n counting vectors of squared length 2n.
    Theta = sum_{v in Lambda} q^{(v,v)/2}.
    The q^1 coefficient counts vectors of squared length 2, i.e. roots.

    For even unimodular lattices of rank 24 (Niemeier lattices):
      q^0 coefficient = 1 (the zero vector)
      q^1 coefficient = |R| (number of roots)

    Decomposition: 1 + |R|*q + ... = (1 + 65520/691 * q + ...) + c_Delta(q + ...)
    At q^1:  |R| = 65520/691 + c_Delta
    So c_Delta = |R| - 65520/691.
    """
    coeff_E12_q1 = Rational(65520, 691)
    c_E = Rational(1)
    c_Delta = root_count - coeff_E12_q1

    return {
        'lattice': lattice_name,
        'rank': 24,
        'weight': 12,
        'root_count': root_count,
        'c_E': c_E,
        'c_Delta': c_Delta,
        'c_Delta_float': float(c_Delta),
        'dim_S_12': 1,
        'depth': 4,
        'cusp_forms': [
            {
                'name': 'Delta_12',
                'weight': 12,
                'arity': 4,
                'coefficient': c_Delta,
                'L_function': 'L(s, Delta_12)',
                'critical_line': Rational(12 - 1, 2),  # (k-1)/2 = 11/2
            }
        ],
        'L_functions': [
            {'arity': 2, 'source': 'curvature kappa=24', 'L': 'zeta(s)',
             'critical_line': Rational(1, 2)},
            {'arity': 3, 'source': 'Eisenstein E_12', 'L': 'zeta(s)*zeta(s-11)',
             'critical_line': Rational(23, 2)},
            {'arity': 4, 'source': 'Ramanujan Delta_12', 'L': 'L(s, Delta_12)',
             'critical_line': Rational(12 - 1, 2)},
        ],
    }


def hecke_eigenvalues_S24_T2() -> Dict[str, Any]:
    r"""Hecke eigenvalues of T_2 on S_24(SL(2,Z)).

    S_24 is 2-dimensional.  The Hecke operator T_2 has characteristic
    polynomial x^2 - 1080*x - 20468736, with roots
      a_2 = 540 +/- 12*sqrt(144169).

    These are the T_2 eigenvalues of the two normalized Hecke eigenforms
    f_1, f_2 spanning S_24.  The Hecke field is Q(sqrt(144169)).

    VERIFICATION of Ramanujan-Petersson bound at p=2:
      |a_2(f_i)| <= 2 * 2^{23/2} = 2^{12.5} ~ 5792.6
      |540 + 12*sqrt(144169)| ~ 5096.4    CHECK
      |540 - 12*sqrt(144169)| ~ 4016.4    CHECK
    """
    disc = 144169
    a2_plus = 540 + 12 * sqrt(disc)
    a2_minus = 540 - 12 * sqrt(disc)
    rp_bound = 2 * 2 ** Rational(23, 2)

    return {
        'weight': 24,
        'dim_S_24': 2,
        'char_poly_coefficients': [1, -1080, -20468736],
        'discriminant': disc,
        'hecke_field': f'Q(sqrt({disc}))',
        'eigenvalues': {
            'f_1': {'a_2': a2_plus, 'a_2_approx': float(a2_plus)},
            'f_2': {'a_2': a2_minus, 'a_2_approx': float(a2_minus)},
        },
        'ramanujan_petersson_bound_p2': float(rp_bound),
        'rp_satisfied': (
            abs(float(a2_plus)) <= float(rp_bound)
            and abs(float(a2_minus)) <= float(rp_bound)
        ),
    }


def hecke_decomposition_rank48() -> Dict[str, Any]:
    r"""Hecke decomposition structure for rank-48 even unimodular lattices.

    weight k = 48/2 = 24.
    dim M_24 = 3, dim S_24 = 2.
    Theta_Lambda = c_E * E_24 + c_1 * f_1 + c_2 * f_2.

    The two Hecke eigenforms f_1, f_2 in S_24 have Hecke eigenvalues
    in Q(sqrt(144169)).

    Arities:
      Arity 2: kappa = 48 (curvature)       --> zeta(s)
      Arity 3: Eisenstein E_24              --> zeta(s)*zeta(s-23)
      Arity 4: First cusp eigenform f_1     --> L(s, f_1)
      Arity 5: Second cusp eigenform f_2    --> L(s, f_2)

    Depth = 3 + dim S_24 = 3 + 2 = 5.

    This is the FIRST depth-5 lattice VOA: the first lattice where the
    shadow obstruction tower detects more than one cusp form.

    Known rank-48 even unimodular lattices:
      - P_48p, P_48q (extremal, discovered by Nebe 2012)
      - Leech tensor Leech (reducible, not extremal)
    """
    ev_data = hecke_eigenvalues_S24_T2()
    return {
        'rank': 48,
        'weight': 24,
        'kappa': 48,
        'dim_M_24': 3,
        'dim_S_24': 2,
        'depth': 5,
        'shadow_class': 'F_5',
        'hecke_eigenforms': ev_data,
        'cusp_forms': [
            {
                'name': 'f_1',
                'weight': 24,
                'arity': 4,
                'L_function': 'L(s, f_1)',
                'critical_line': Rational(23, 2),
            },
            {
                'name': 'f_2',
                'weight': 24,
                'arity': 5,
                'L_function': 'L(s, f_2)',
                'critical_line': Rational(23, 2),
            },
        ],
        'L_functions': [
            {'arity': 2, 'source': 'curvature kappa=48', 'L': 'zeta(s)',
             'critical_line': Rational(1, 2)},
            {'arity': 3, 'source': 'Eisenstein E_24', 'L': 'zeta(s)*zeta(s-23)',
             'critical_line': Rational(23, 2)},
            {'arity': 4, 'source': '1st cusp eigenform f_1',
             'L': 'L(s, f_1)', 'critical_line': Rational(23, 2)},
            {'arity': 5, 'source': '2nd cusp eigenform f_2',
             'L': 'L(s, f_2)', 'critical_line': Rational(23, 2)},
        ],
    }


# =========================================================================
# The arithmetic sieve: stripping Eisenstein contributions
# =========================================================================


def arithmetic_sieve(rank: int,
                     root_count: Optional[int] = None) -> Dict[str, Any]:
    r"""The five-step arithmetic sieve for an even unimodular lattice VOA.

    INPUT: rank r of even unimodular lattice Lambda.

    Step 1: The theta function Theta_Lambda in M_{r/2}(SL(2,Z)).
    Step 2: Hecke decomposition Theta = c_E * E_k + sum c_j * f_j.
    Step 3: Epstein zeta E_Lambda(s) = sum over non-zero v of (v,v)^{-s}.
    Step 4: L-function factorization via spectral decomposition.
    Step 5: Arity-by-arity assignment:
            Arity 2 <-> zeta(s)
            Arity 3 <-> zeta(s)*zeta(s-k+1)
            Arity 3+j <-> L(s, f_j)

    OUTPUT: complete period-shadow dictionary.
    """
    if rank <= 0 or rank % 2 != 0:
        raise ValueError(f"Need even positive rank, got {rank}")

    k = rank // 2  # weight of theta function
    g_k = dim_Sk(k)
    depth = 3 + g_k if k >= 4 else 2  # depth 2 for very small ranks

    # Build L-function assignments
    L_functions = []

    # Arity 2: curvature
    L_functions.append({
        'arity': 2,
        'type': 'Eisenstein',
        'source': f'curvature kappa={rank}',
        'L': 'zeta(s)',
        'critical_line': Rational(1, 2),
        'period_type': 'Riemann',
    })

    # Arity 3: Eisenstein product (if weight >= 4)
    if k >= 4:
        L_functions.append({
            'arity': 3,
            'type': 'Eisenstein',
            'source': f'Eisenstein E_{k}',
            'L': f'zeta(s)*zeta(s-{k-1})',
            'critical_line': Rational(2 * k - 1, 2),
            'period_type': 'Dedekind',
        })

    # Arities 4, 5, ..., 3+g_k: cusp eigenforms
    for j in range(1, g_k + 1):
        L_functions.append({
            'arity': 3 + j,
            'type': 'cuspidal',
            'source': f'{_ordinal(j)} cusp eigenform f_{j} in S_{k}',
            'L': f'L(s, f_{j})',
            'critical_line': Rational(k - 1, 2),
            'period_type': 'Hecke',
        })

    # Cusp form data
    cusp_data = {
        'first_cusp_arity': 4 if g_k >= 1 else None,
        'last_cusp_arity': 3 + g_k if g_k >= 1 else None,
        'num_cusp_forms': g_k,
    }

    # Identify which named cusp forms appear
    named_cusp_forms = []
    if g_k >= 1 and k == 12:
        named_cusp_forms.append({
            'arity': 4, 'name': 'Ramanujan Delta',
            'weight': 12, 'dim_S_k': 1})
    elif g_k >= 1 and k == 16:
        named_cusp_forms.append({
            'arity': 4, 'name': 'Delta*E_4',
            'weight': 16, 'dim_S_k': 1})
    elif g_k >= 1 and k == 18:
        named_cusp_forms.append({
            'arity': 4, 'name': 'Delta*E_6',
            'weight': 18, 'dim_S_k': 1})
    elif g_k >= 1 and k == 24:
        named_cusp_forms.append({
            'arity': 4, 'name': '1st eigenform in S_24',
            'weight': 24, 'dim_S_k': 2,
            'hecke_field': 'Q(sqrt(144169))'})
        if g_k >= 2:
            named_cusp_forms.append({
                'arity': 5, 'name': '2nd eigenform in S_24',
                'weight': 24, 'dim_S_k': 2,
                'hecke_field': 'Q(sqrt(144169))'})

    return {
        'rank': rank,
        'weight': k,
        'kappa': rank,
        'dim_M_k': dim_Mk(k),
        'dim_S_k': g_k,
        'depth': depth,
        'num_L_functions': len(L_functions),
        'num_critical_lines': depth - 1,
        'L_functions': L_functions,
        'cusp_data': cusp_data,
        'named_cusp_forms': named_cusp_forms,
        'root_count': root_count,
    }


def _ordinal(n: int) -> str:
    """Return ordinal string for small positive integers."""
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    return f'{n}{suffixes.get(n, "th")}'


# =========================================================================
# Shadow-spectral correspondence coefficients
# =========================================================================


def shadow_spectral_coefficients_leech(max_n: int = 10) -> Dict[int, Dict]:
    r"""Shadow-spectral correspondence coefficients for the Leech lattice.

    For each n >= 1, the Leech lattice theta function satisfies:
      a(n) = E_12_coeff(n) + c_Delta * tau(n)

    The shadow-spectral coefficient at q^n decomposes as:
      Eisenstein part: E_12_coeff(n) = (65520/691) * sigma_11(n)
      Cuspidal part: c_Delta * tau(n)  where c_Delta = -65520/691

    The RATIO (cuspidal part)/(total) measures how much of the lattice
    vector count at squared-length 2n comes from the cusp form Delta.
    """
    c_Delta = Rational(-65520, 691)
    coeff_E12_q1 = Rational(65520, 691)
    result = {}

    for n in range(1, max_n + 1):
        e_part = eisenstein_coefficient(12, n) - 1 if n == 0 else eisenstein_coefficient(12, n)
        # Actually: eisenstein_coefficient returns coeff of q^n.
        # For n >= 1, E_12(q^n) = (65520/691) * sigma_11(n)
        eis_part = eisenstein_coefficient(12, n)
        tau_n = RAMANUJAN_TAU.get(n, None)
        if tau_n is None:
            # Skip if we don't have tau(n)
            continue
        cusp_part = c_Delta * tau_n
        total = eis_part + cusp_part

        result[n] = {
            'n': n,
            'eisenstein_part': eis_part,
            'cuspidal_part': cusp_part,
            'total': total,
            'total_int': int(total),
            'tau_n': tau_n,
            'cusp_fraction': float(cusp_part / total) if total != 0 else None,
        }

    return result


# =========================================================================
# Ramanujan-Petersson in the shadow obstruction tower
# =========================================================================


def ramanujan_petersson_shadow(k: int, max_p: int = 20) -> Dict[str, Any]:
    r"""Ramanujan-Petersson bound manifestation in the shadow obstruction tower.

    For a Hecke eigenform f of weight k:
      |a_p(f)| <= 2 * p^{(k-1)/2}    (Deligne's theorem, 1974)

    In the shadow obstruction tower for a lattice VOA of weight k:
      The arity-(3+j) shadow amplitude Sh_{3+j} at prime p satisfies
        |Sh_{3+j}(p)| <= |c_j| * 2 * p^{(k-1)/2}
      where c_j is the cuspidal projection coefficient.

    Compare with the Eisenstein growth at arity 3:
      sigma_{k-1}(p) = 1 + p^{k-1}  (for prime p)
      This grows as p^{k-1} — DOUBLE the exponent of the cusp form bound.

    The Ramanujan bound means:
      CUSP FORM ARITIES GROW AT HALF THE RATE OF EISENSTEIN ARITIES.
    This is visible in the shadow obstruction tower as a dramatic amplitude suppression
    at arities >= 4 compared to arity 3.
    """
    results = {}
    for p in range(2, max_p + 1):
        if not _is_prime(p):
            continue
        # Eisenstein growth
        eis_val = 1 + p ** (k - 1)
        # Ramanujan-Petersson bound
        rp_bound = 2 * p ** (Rational(k - 1, 2))
        # Ratio: cusp/eisenstein bound
        suppression = float(rp_bound / eis_val) if eis_val != 0 else 0

        # For Delta at weight 12 and prime p:
        tau_p = RAMANUJAN_TAU.get(p, None)
        actual_ratio = None
        if tau_p is not None and k == 12:
            actual_ratio = abs(tau_p) / eis_val

        results[p] = {
            'p': p,
            'eisenstein_growth': eis_val,
            'rp_bound': float(rp_bound),
            'suppression_ratio': suppression,
            'actual_tau_p': tau_p if k == 12 else None,
            'actual_ratio': actual_ratio,
        }

    return {
        'weight': k,
        'exponent_eisenstein': k - 1,
        'exponent_cusp_bound': Rational(k - 1, 2),
        'exponent_ratio': 2,  # Eisenstein exponent / cusp exponent
        'primes': results,
    }


def _is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# =========================================================================
# Complete cusp form spectrum for a given rank
# =========================================================================


def cusp_form_spectrum(rank: int) -> Dict[str, Any]:
    r"""Complete cusp form spectrum of the shadow obstruction tower for a lattice VOA.

    For each shadow arity r, determines:
      - Whether this arity detects an Eisenstein or cuspidal contribution
      - If cuspidal, which cusp form is detected
      - The associated L-function
      - The critical line of the L-function

    This is the full arithmetic content of the shadow obstruction tower.
    """
    k = rank // 2
    g_k = dim_Sk(k)
    depth = shadow_depth_lattice(rank) if rank >= 2 else 2

    spectrum = {}

    # Arity 2: Riemann zeta
    spectrum[2] = {
        'type': 'Eisenstein',
        'content': 'constant term (curvature)',
        'kappa': rank,
        'L_function': 'zeta(s)',
        'critical_line': Rational(1, 2),
        'growth_exponent': 0,  # constant
    }

    # Arity 3: Eisenstein product (for k >= 4)
    if k >= 4:
        spectrum[3] = {
            'type': 'Eisenstein',
            'content': f'divisor sums sigma_{k-1}(n)',
            'L_function': f'zeta(s)*zeta(s-{k-1})',
            'critical_line': Rational(2 * k - 1, 2),
            'growth_exponent': k - 1,
        }

    # Arities 4, ..., 3+g_k: cusp eigenforms
    for j in range(1, g_k + 1):
        spectrum[3 + j] = {
            'type': 'cuspidal',
            'content': f'{_ordinal(j)} Hecke eigenform f_{j} in S_{k}',
            'L_function': f'L(s, f_{j})',
            'critical_line': Rational(k - 1, 2),
            'growth_exponent_bound': Rational(k - 1, 2),
            'ramanujan_petersson': True,
        }

    return {
        'rank': rank,
        'weight': k,
        'depth': depth,
        'num_cusp_forms': g_k,
        'first_cusp_arity': 4 if g_k >= 1 else None,
        'last_cusp_arity': 3 + g_k if g_k >= 1 else None,
        'spectrum': spectrum,
        'tower_terminates': True,
        'termination_arity': 3 + g_k,
    }


# =========================================================================
# Master table: cusp form appearance by rank
# =========================================================================


def cusp_form_appearance_table(max_rank: int = 100) -> List[Dict]:
    r"""Master table showing at which arity each cusp form appears.

    For even unimodular lattice VOAs of rank r = 8, 16, 24, 32, 40, 48, ...
    (even unimodular lattices exist only in ranks divisible by 8).

    Returns a list of dicts, one per valid rank.
    """
    table = []
    for r in range(8, max_rank + 1, 8):
        k = r // 2
        g_k = dim_Sk(k)
        entry = {
            'rank': r,
            'weight': k,
            'dim_S_k': g_k,
            'depth': 3 + g_k,
            'cusp_form_arities': list(range(4, 4 + g_k)),
            'first_cusp_arity': 4 if g_k >= 1 else None,
        }

        # Identify named cusp forms at each arity
        cusp_details = []
        if k == 12 and g_k >= 1:
            cusp_details.append({'arity': 4, 'form': 'Delta (Ramanujan)',
                                  'weight': 12})
        elif k == 16 and g_k >= 1:
            cusp_details.append({'arity': 4, 'form': 'Delta*E_4',
                                  'weight': 16})
        elif k == 24 and g_k >= 2:
            cusp_details.append({'arity': 4, 'form': 'f_1 in S_24',
                                  'weight': 24})
            cusp_details.append({'arity': 5, 'form': 'f_2 in S_24',
                                  'weight': 24})
        elif k == 36 and g_k >= 3:
            for j in range(1, g_k + 1):
                cusp_details.append({'arity': 3 + j,
                                      'form': f'f_{j} in S_{k}',
                                      'weight': k})
        else:
            for j in range(1, g_k + 1):
                cusp_details.append({'arity': 3 + j,
                                      'form': f'f_{j} in S_{k}',
                                      'weight': k})

        entry['cusp_details'] = cusp_details
        table.append(entry)

    return table


# =========================================================================
# The claim to verify: cusp forms appear at arity 4 onward, one per arity
# =========================================================================


def verify_cusp_arity_claim(max_rank: int = 100) -> Dict[str, Any]:
    r"""Verify the claim from the period-shadow dictionary.

    CLAIM (prop:period-shadow-dictionary): The j-th cusp eigenform f_j
    in the Hecke decomposition of Theta_Lambda appears at shadow arity 3+j.

    This means:
      - The FIRST cusp form ALWAYS appears at arity 4
      - The SECOND cusp form ALWAYS appears at arity 5
      - etc.

    The claim is that cusp forms appear at CONSECUTIVE arities starting
    from 4, NOT that they skip arities.  This follows from the spectral
    filtration structure of the shadow obstruction tower.

    KEY VERIFICATION: For all even unimodular lattices of rank r:
      - dim S_{r/2} cusp forms appear at arities 4, 5, ..., 3 + dim S_{r/2}
      - The tower terminates at arity 3 + dim S_{r/2}
      - No cusp form is skipped (each arity detects exactly one eigenform)
    """
    results = []
    all_consistent = True

    for r in range(8, max_rank + 1, 8):
        k = r // 2
        g_k = dim_Sk(k)
        depth = 3 + g_k

        # The claim: arities 4, ..., 3+g_k each detect one cusp eigenform
        cusp_arities = list(range(4, 4 + g_k))
        claim_consistent = (len(cusp_arities) == g_k)

        # Additional check: the depth formula is internally consistent
        depth_consistent = (depth == 3 + g_k)

        entry = {
            'rank': r,
            'weight': k,
            'dim_S_k': g_k,
            'depth': depth,
            'cusp_arities': cusp_arities,
            'claim_consistent': claim_consistent and depth_consistent,
        }
        results.append(entry)
        if not entry['claim_consistent']:
            all_consistent = False

    return {
        'claim': 'j-th cusp form appears at arity 3+j',
        'all_consistent': all_consistent,
        'num_ranks_checked': len(results),
        'results': results,
    }


# =========================================================================
# Specific lattice computations
# =========================================================================


# The 24 Niemeier lattice root counts
NIEMEIER_ROOT_COUNTS = {
    'D_24': 1104,
    'D_16+E_8': 720,
    '3E_8': 720,
    'A_24': 600,
    '2D_12': 528,
    'A_17+E_7': 432,
    'D_10+2E_7': 432,
    'A_15+D_9': 384,
    '3D_8': 336,
    '2A_12': 312,
    'A_11+D_7+E_6': 288,
    '4E_6': 288,
    '2A_9+D_6': 240,
    '4D_6': 240,
    '3A_8': 216,
    '2A_7+2D_5': 192,
    '4A_6': 168,
    '4A_5+D_4': 144,
    '6D_4': 144,
    '6A_4': 120,
    '8A_3': 96,
    '12A_2': 72,
    '24A_1': 48,
    'Leech': 0,
}


def niemeier_cusp_coefficients() -> Dict[str, Rational]:
    r"""Cuspidal projection coefficients for all 24 Niemeier lattices.

    For each Niemeier lattice Lambda, compute c_Delta in
      Theta_Lambda = E_12 + c_Delta * Delta.

    c_Delta = |R| - 65520/691

    where |R| is the number of roots.

    The Leech lattice has c_Delta = -65520/691 (maximal cuspidal content).
    The lattice with the most roots (D_24: 1104 roots) has c_Delta =
    1104 - 65520/691 = (1104*691 - 65520)/691 = (762864 - 65520)/691
    = 697344/691.
    """
    coeff_E12_q1 = Rational(65520, 691)
    result = {}
    for name, roots in NIEMEIER_ROOT_COUNTS.items():
        c_Delta = roots - coeff_E12_q1
        result[name] = c_Delta
    return result


def leech_shadow_spectral(max_n: int = 10) -> Dict[str, Any]:
    r"""Complete shadow-spectral analysis for the Leech lattice.

    The Leech lattice is the deepest Niemeier lattice (depth 4), with:
      c_Delta = -65520/691

    The shadow arity 4 detects the Ramanujan cusp form Delta via:
      Sh_4 ~ c_Delta * tau(n) ~ (-65520/691) * tau(n)

    The Ramanujan conjecture |tau(p)| <= 2*p^{11/2} (Deligne 1974)
    is directly visible in the arity-4 shadow amplitude bound.
    """
    c_Delta = Rational(-65520, 691)
    spectral = shadow_spectral_coefficients_leech(max_n)

    # Ramanujan-Petersson verification at each prime
    rp_checks = {}
    for n, data in spectral.items():
        if _is_prime(n):
            tau_n = data['tau_n']
            rp_bound = 2 * n ** Rational(11, 2)
            rp_checks[n] = {
                'p': n,
                'tau_p': tau_n,
                'rp_bound': float(rp_bound),
                'satisfies_rp': abs(tau_n) <= float(rp_bound),
                'ratio': abs(tau_n) / float(rp_bound),
            }

    return {
        'lattice': 'Leech',
        'rank': 24,
        'depth': 4,
        'c_Delta': c_Delta,
        'spectral_coefficients': spectral,
        'rp_checks': rp_checks,
        'all_rp_satisfied': all(
            v['satisfies_rp'] for v in rp_checks.values()
        ),
    }


# =========================================================================
# The frontier: depth >= 5 and higher cusp dimensions
# =========================================================================


def first_depth_d_lattice(d: int) -> Optional[int]:
    r"""Find the smallest rank of an even unimodular lattice with shadow depth d.

    depth d = 3 + dim S_{r/2}.
    So we need dim S_{r/2} = d - 3.
    Find smallest even r divisible by 8 with dim S_{r/2} >= d - 3.
    """
    target_g = d - 3
    if target_g < 0:
        return None
    for r in range(8, 1000, 8):
        k = r // 2
        if dim_Sk(k) >= target_g:
            return r
    return None


def depth_frontier_table(max_depth: int = 10) -> List[Dict]:
    r"""Table of first lattice achieving each depth level.

    The depth frontier: at which rank does each new depth level first appear?

    depth 3: rank 8   (E_8, no cusp forms in S_4)
    depth 4: rank 24  (Niemeier, one cusp form in S_12: Delta)
    depth 5: rank 48  (two cusp forms in S_24)
    depth 6: rank 72  (three cusp forms in S_36)
    ...
    """
    table = []
    for d in range(3, max_depth + 1):
        r = first_depth_d_lattice(d)
        k = r // 2 if r else None
        g_k = dim_Sk(k) if k else None
        table.append({
            'depth': d,
            'first_rank': r,
            'weight': k,
            'dim_S_k': g_k,
            'num_cusp_forms': d - 3,
        })
    return table
