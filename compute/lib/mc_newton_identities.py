r"""mc_newton_identities.py -- Newton's identities from the MC bracket.

THE ALGEBRAIC HEART: The MC equation [Theta, Theta] = 0, projected to
genus 0, arity r+1, yields Newton's identity

    p_r = e_1 * p_{r-1} - e_2 * p_{r-2}

where p_r = alpha^r + beta^r (power sums = shadow coefficients via
p_r = -r * S_r) and e_1 = alpha + beta, e_2 = alpha * beta are
elementary symmetric polynomials = Satake parameters.

For the Ramanujan Delta function (weight 12, level 1):
  alpha_p + beta_p = tau(p),  alpha_p * beta_p = p^11.

Newton's identities determine {alpha_p, beta_p} from {p_1, p_2}.
For GL(n), Newton's identities from n power sums determine n Satake
parameters.  The shadow tower provides infinitely many power sums,
but for n=2 variables, all p_r for r >= 3 are determined by p_1, p_2
via the two-variable Newton recurrence.

MULTI-CHANNEL (W_3): Two generators T (weight 2) and W (weight 3)
produce mixed power sums in the 2d deformation space.  The Newton
identities involve coupled recursions on (x_T, x_W) channels.

GENUS-g CORRECTIONS: At genus 0, Newton's identity is the standard
algebraic identity.  At genus g >= 1, the MC equation receives
contributions from genus-g compositions in the modular operad.  The
genus-1 correction involves tr(m_2^{r-1}) and the propagator
E_2*(tau).  These corrections are QUASI-MODULAR (AP15: E_2* is
quasi-modular, not holomorphic).

References:
  prop:mc-bracket-determines-atoms (arithmetic_shadows.tex, line 2608)
  prop:shadow-symmetric-power (arithmetic_shadows.tex, line 4840)
  rem:operadic-transfer (arithmetic_shadows.tex, line 4937)
  mc_newton_spectral.py (existing module: Newton algebra + MC bracket)
  symmetric_power_shadow.py (existing module: Satake, symmetric powers)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =====================================================================
# Section 1: Ramanujan tau function (self-contained)
# =====================================================================

@lru_cache(maxsize=256)
def ramanujan_tau(n: int) -> int:
    r"""Coefficients of Delta = q * prod_{m>=1} (1 - q^m)^{24}.

    tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472,
    tau(5) = 4830, tau(6) = -6048, tau(7) = -16744, ...
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    return coeffs[n - 1] if n - 1 <= N else 0


# =====================================================================
# Section 2: Satake parameters
# =====================================================================

def satake_parameters(a_p: Union[int, float, complex],
                      k: int, p: int) -> Tuple[complex, complex]:
    r"""Satake parameters alpha_p, beta_p from Hecke eigenvalue a(p).

    alpha + beta = a(p),  alpha * beta = p^{k-1}.
    Roots of X^2 - a(p)*X + p^{k-1} = 0.

    Ramanujan bound (Deligne for k >= 2): |alpha| = |beta| = p^{(k-1)/2}.
    """
    disc = a_p * a_p - 4 * p ** (k - 1)
    if isinstance(disc, complex) or disc < 0:
        sqrt_d = cmath.sqrt(disc if isinstance(disc, complex) else complex(disc))
    else:
        sqrt_d = complex(math.sqrt(disc))
    alpha = (a_p + sqrt_d) / 2
    beta = (a_p - sqrt_d) / 2
    return alpha, beta


# =====================================================================
# Section 3: Power sums from Satake parameters
# =====================================================================

def power_sum(alpha: complex, beta: complex, r: int) -> complex:
    r"""p_r = alpha^r + beta^r via the two-variable Newton recurrence.

    Recurrence: p_r = e_1 * p_{r-1} - e_2 * p_{r-2}
    where e_1 = alpha + beta, e_2 = alpha * beta.
    Initial: p_0 = 2, p_1 = e_1.

    This avoids large complex exponentials for high r.
    """
    e1 = alpha + beta
    e2 = alpha * beta
    if r == 0:
        return 2.0
    if r == 1:
        return e1
    p_prev2 = 2.0   # p_0
    p_prev1 = e1     # p_1
    for _ in range(2, r + 1):
        p_curr = e1 * p_prev1 - e2 * p_prev2
        p_prev2 = p_prev1
        p_prev1 = p_curr
    return p_curr


def power_sums_direct(alpha: complex, beta: complex,
                      max_r: int) -> Dict[int, complex]:
    """Compute p_1, ..., p_{max_r} via direct exponentiation."""
    return {r: alpha ** r + beta ** r for r in range(1, max_r + 1)}


def power_sums_recursive(alpha: complex, beta: complex,
                         max_r: int) -> Dict[int, complex]:
    """Compute p_1, ..., p_{max_r} via Newton recurrence."""
    return {r: power_sum(alpha, beta, r) for r in range(1, max_r + 1)}


# =====================================================================
# Section 4: Newton identity verification
# =====================================================================

def newton_identity_residual(p: Dict[int, complex], e1: complex,
                             e2: complex, r: int) -> complex:
    r"""Residual of Newton's identity at level r for two variables.

    Newton's identity (n=2 variables):
        p_r - e_1 * p_{r-1} + e_2 * p_{r-2} = 0     for r >= 3
        p_2 - e_1 * p_1 + 2 * e_2 = 0                for r = 2
        p_1 - e_1 = 0                                  for r = 1

    Returns the residual (should be zero if the identity holds).
    """
    if r == 1:
        return p[1] - e1
    if r == 2:
        return p[2] - e1 * p[1] + 2 * e2
    return p[r] - e1 * p.get(r - 1, 0) + e2 * p.get(r - 2, 0)


def verify_newton_all_arities(alpha: complex, beta: complex,
                              max_r: int = 8) -> Dict[str, Any]:
    r"""Verify Newton's identities at all arities for Satake pair (alpha, beta).

    Returns dict with power sums, elementary symmetric polys, and residuals.
    """
    e1 = alpha + beta
    e2 = alpha * beta
    p_direct = power_sums_direct(alpha, beta, max_r)
    p_recursive = power_sums_recursive(alpha, beta, max_r)

    residuals = {}
    for r in range(1, max_r + 1):
        res = newton_identity_residual(p_direct, e1, e2, r)
        residuals[r] = res

    # Check consistency of direct vs recursive
    consistency = {}
    for r in range(1, max_r + 1):
        diff = abs(p_direct[r] - p_recursive[r])
        consistency[r] = diff

    return {
        'alpha': alpha,
        'beta': beta,
        'e1': e1,
        'e2': e2,
        'power_sums_direct': p_direct,
        'power_sums_recursive': p_recursive,
        'newton_residuals': residuals,
        'direct_vs_recursive': consistency,
        'all_newton_hold': all(
            abs(v) / max(abs(p_direct.get(r, 0)), 1) < 1e-6
            for r, v in residuals.items()
        ),
        'all_consistent': all(
            v / max(abs(p_direct.get(r, 0)), 1) < 1e-6
            for r, v in consistency.items()
        ),
    }


# =====================================================================
# Section 5: Ramanujan Delta verification at specific primes
# =====================================================================

def delta_satake_at_prime(p: int) -> Dict[str, Any]:
    r"""Satake parameters for Ramanujan Delta at prime p.

    Delta is weight 12, level 1.  a(p) = tau(p), alpha*beta = p^11.
    Ramanujan conjecture (Deligne 1974): |alpha_p| = |beta_p| = p^{11/2}.
    """
    a_p = ramanujan_tau(p)
    alpha, beta = satake_parameters(a_p, 12, p)
    ram_bound = 2 * p ** (11 / 2)

    return {
        'prime': p,
        'tau_p': a_p,
        'alpha': alpha,
        'beta': beta,
        'e1': alpha + beta,
        'e2': alpha * beta,
        'abs_alpha': abs(alpha),
        'abs_beta': abs(beta),
        'ramanujan_bound': ram_bound,
        'satisfies_ramanujan': abs(a_p) <= ram_bound + 1e-6,
        'abs_product': abs(alpha * beta),
        'expected_product': p ** 11,
    }


def delta_newton_verification(p: int, max_r: int = 8) -> Dict[str, Any]:
    r"""Full Newton identity verification for Delta at prime p.

    Computes power sums p_1, ..., p_{max_r} and verifies Newton's
    identity at each level.
    """
    info = delta_satake_at_prime(p)
    alpha = info['alpha']
    beta = info['beta']
    verification = verify_newton_all_arities(alpha, beta, max_r)
    verification['prime'] = p
    verification['tau_p'] = info['tau_p']
    verification['ramanujan'] = info['satisfies_ramanujan']
    return verification


def delta_power_sums_table(p: int, max_r: int = 8) -> Dict[int, complex]:
    r"""Table of power sums p_r(alpha_p, beta_p) for Delta at prime p."""
    info = delta_satake_at_prime(p)
    return power_sums_direct(info['alpha'], info['beta'], max_r)


# =====================================================================
# Section 6: Atoms from MC reconstruction
# =====================================================================

def atoms_from_power_sums(p1: complex, p2: complex) -> Tuple[complex, complex]:
    r"""Reconstruct (alpha, beta) from (p_1, p_2).

    e_1 = p_1,  e_2 = (p_1^2 - p_2) / 2.
    Then alpha, beta are roots of X^2 - e_1*X + e_2 = 0.
    """
    e1 = p1
    e2 = (p1 ** 2 - p2) / 2
    disc = e1 ** 2 - 4 * e2
    sqrt_d = cmath.sqrt(disc)
    alpha = (e1 + sqrt_d) / 2
    beta = (e1 - sqrt_d) / 2
    return alpha, beta


def verify_reconstruction(alpha_true: complex, beta_true: complex,
                          max_r: int = 8) -> Dict[str, Any]:
    r"""Verify that atoms can be reconstructed from power sums.

    Compute p_1, p_2, reconstruct alpha, beta, then verify all higher
    power sums match.
    """
    p_true = power_sums_direct(alpha_true, beta_true, max_r)
    alpha_rec, beta_rec = atoms_from_power_sums(p_true[1], p_true[2])

    # The reconstructed pair may be swapped
    match_direct = (abs(alpha_rec - alpha_true) < 1e-6
                    and abs(beta_rec - beta_true) < 1e-6)
    match_swapped = (abs(alpha_rec - beta_true) < 1e-6
                     and abs(beta_rec - alpha_true) < 1e-6)

    # Verify all power sums from reconstructed atoms
    p_rec = power_sums_direct(alpha_rec, beta_rec, max_r)
    power_sum_errors = {r: abs(p_true[r] - p_rec[r]) for r in range(1, max_r + 1)}

    return {
        'alpha_true': alpha_true,
        'beta_true': beta_true,
        'alpha_reconstructed': alpha_rec,
        'beta_reconstructed': beta_rec,
        'match_direct': match_direct,
        'match_swapped': match_swapped,
        'match': match_direct or match_swapped,
        'power_sum_errors': power_sum_errors,
        'all_power_sums_match': all(v < 1e-6 for v in power_sum_errors.values()),
    }


# =====================================================================
# Section 7: GL(n) Newton identities (n > 2)
# =====================================================================

def newton_identity_gln(p: Dict[int, complex],
                        e: Dict[int, complex],
                        n: int, r: int) -> complex:
    r"""Newton's identity for GL(n) at level r.

    For n variables alpha_1, ..., alpha_n:
        p_r = sum_{j=1}^{min(r,n)} (-1)^{j-1} e_j * p_{r-j}
              + (-1)^{r-1} * r * e_r      (if r <= n)

    Equivalently (for r >= 1):
        p_r - e_1 p_{r-1} + e_2 p_{r-2} - ... + (-1)^{r-1} r e_r = 0   (r <= n)
        p_r - e_1 p_{r-1} + e_2 p_{r-2} - ... + (-1)^{n-1} e_n p_{r-n} = 0  (r > n)

    Returns the residual (should be zero).
    """
    total = p.get(r, 0)
    upper = min(r, n)
    for j in range(1, upper + 1):
        sign = (-1) ** j
        if j == r and r <= n:
            total += sign * r * e.get(j, 0)
        else:
            total += sign * e.get(j, 0) * p.get(r - j, 0)
    return total


def elementary_from_power_sums_gln(p: Dict[int, complex],
                                   n: int) -> Dict[int, complex]:
    r"""Recover elementary symmetric polynomials e_1, ..., e_n from power sums.

    Uses Newton's identities solved for e_r:
        r * e_r = sum_{j=1}^{r-1} (-1)^{j-1} e_{r-j} p_j + (-1)^{r-1} p_r
    """
    e = {}
    for r in range(1, n + 1):
        total = 0
        for j in range(1, r):
            total += (-1) ** (j - 1) * e.get(r - j, 0) * p.get(j, 0)
        total += (-1) ** (r - 1) * p.get(r, 0)
        e[r] = total / r
    return e


def verify_newton_gln(alphas: Sequence[complex],
                      max_r: int = 10) -> Dict[str, Any]:
    r"""Verify Newton's identities for GL(n) Satake parameters.

    For n Satake parameters alpha_1, ..., alpha_n, all p_r for r > n
    are determined by p_1, ..., p_n via Newton's identities.  The
    shadow tower provides infinitely many power sums; the ADDITIONAL
    constraints beyond Newton at r > n are TRIVIALLY satisfied (they
    are consequences of the characteristic polynomial having degree n).
    """
    n = len(alphas)
    # Compute power sums directly
    p = {}
    for r in range(1, max_r + 1):
        p[r] = sum(a ** r for a in alphas)

    # Compute elementary symmetric polynomials directly
    from itertools import combinations
    e_direct = {}
    for k in range(1, n + 1):
        e_direct[k] = sum(math.prod(combo) if all(isinstance(x, (int, float)) for x in combo)
                          else _cprod(combo)
                          for combo in combinations(alphas, k))

    # Compute elementary from Newton's identities
    e_newton = elementary_from_power_sums_gln(p, n)

    # Verify Newton at all arities
    residuals = {}
    for r in range(1, max_r + 1):
        residuals[r] = newton_identity_gln(p, e_direct, n, r)

    # Verify e_direct vs e_newton
    e_errors = {k: abs(e_direct[k] - e_newton.get(k, 0))
                for k in range(1, n + 1)}

    return {
        'n': n,
        'alphas': alphas,
        'power_sums': p,
        'elementary_direct': e_direct,
        'elementary_newton': e_newton,
        'e_errors': e_errors,
        'newton_residuals': residuals,
        'all_newton_hold': all(abs(v) < 1e-6 for v in residuals.values()),
        'all_e_match': all(v < 1e-6 for v in e_errors.values()),
    }


def _cprod(vals):
    """Product of a sequence of complex numbers."""
    result = 1
    for v in vals:
        result *= v
    return result


# =====================================================================
# Section 8: Multi-channel Newton (W_3)
# =====================================================================

def w3_shadow_seeds(c_val: float) -> Dict[str, float]:
    r"""Shadow tower seeds for W_3 at central charge c.

    W_3 has two generators: T (weight 2) and W (weight 3).
    The shadow tower lives on the 2d deformation space (x_T, x_W).

    Arity-2 shadows (curvatures):
        kappa_TT = c/2      (Virasoro sector)
        kappa_WW = 5c/6     (W-sector, from landscape_census)
        kappa_TW = 0         (no mixed quadratic coupling)

    Arity-3 shadow (cubic):
        alpha = 16 / (22 + 5c)   (W_3 structure constant squared)
        C_TTT = -6/c^2 * alpha_Vir = 0 (Virasoro cubic is zero by parity)
        C_TTW = 0 (by parity: odd number of W)
        C_TWW = function of c (from W_3 OPE)
        C_WWW = function of c (from W_3 OPE)

    Arity-4 shadow: three channels Q_TT, Q_TW, Q_WW.
    """
    if abs(c_val) < 1e-10 or abs(5 * c_val + 22) < 1e-10:
        raise ValueError(f"Singular central charge c = {c_val}")

    kappa_TT = c_val / 2
    kappa_WW = 5 * c_val / 6

    # W_3 structure constant alpha(c) = 16/(22 + 5c)
    alpha_w3 = 16 / (22 + 5 * c_val)

    # Cubic shadows: C_{333}^2 = 64(7c+68)(2c-1) / [5c(c+24)(5c+22)]
    # C_TWW involves a nontrivial coupling from the W_3 OPE
    # The T-channel cubic C_TTT = 0 (Virasoro parity)
    # The mixed C_TTW = 0 (spin parity: T has spin 2, W has spin 3)
    # C_TWW ~ (structure constant) from TW->W OPE
    # C_WWW ~ from WW->W OPE

    return {
        'c': c_val,
        'kappa_TT': kappa_TT,
        'kappa_WW': kappa_WW,
        'kappa_TW': 0.0,
        'alpha_w3': alpha_w3,
        'shadow_depth_T': float('inf'),   # Virasoro: infinite tower
        'shadow_depth_W': float('inf'),   # W-sector: infinite tower
    }


def w3_mixed_newton_recursion(c_val: float, max_r: int = 6) -> Dict[str, Any]:
    r"""Multi-channel Newton recursion for W_3.

    The MC equation on the 2d deformation space (x_T, x_W) gives
    coupled Newton-type recursions.  At genus 0, the T-channel
    is the standard Virasoro recursion.  The W-channel recursion
    involves mixed brackets [Sh_T, Sh_W] and [Sh_W, Sh_W].

    For the T-channel: the Virasoro single-line tower with
        S_r^{(T)} = S_r^{Vir}(c)   (standard Virasoro shadow)

    For the W-channel: the recursion involves the coupling alpha(c).

    STRUCTURE: Define the full shadow as
        Sh_r = sum_{|I|=r} S_I * x^I
    where I = (i_T, i_W) with |I| = i_T + i_W.

    The MC recursion at arity r+1 gives:
        S_{(r,0)} = f(S_{(j,k)} for j+k < r)   [pure T-channel]
        S_{(r-1,1)} = g(...)                      [mixed]
        ...
        S_{(0,r)} = h(...)                        [pure W-channel]

    For Newton identities: on each 1d slice (the T-line, the W-line,
    and mixed directions), Newton's identity holds with appropriate
    effective Satake parameters.
    """
    seeds = w3_shadow_seeds(c_val)

    # T-channel: standard Virasoro tower
    # S_2^T = kappa_T = c/2
    kappa_T = seeds['kappa_TT']

    # W-channel curvature
    kappa_W = seeds['kappa_WW']

    # On the T-line (x_W = 0): pure Virasoro
    # S_r^T satisfies Newton with e1_T, e2_T determined from kappa_T
    # On the W-line (x_T = 0): the recursion involves kappa_W and W-sector OPE

    # Effective Satake parameters for each channel
    # T-channel (Virasoro): single atom at lambda_eff = -6/c
    lambda_T = -6 / c_val if abs(c_val) > 1e-10 else 0
    # Power sums on T-line
    p_T = {r: lambda_T ** r for r in range(1, max_r + 1)}

    # W-channel effective coupling from kappa_W = 5c/6
    # For the W-channel the effective coupling is different
    # The W-line shadow metric Q_W(t) has discriminant involving alpha(c)
    alpha_w3 = seeds['alpha_w3']
    # S_3 on W-line: cubic shadow
    S3_W = -alpha_w3 / (6 * kappa_W) if abs(kappa_W) > 1e-10 else 0

    return {
        'c': c_val,
        'seeds': seeds,
        'T_channel': {
            'kappa': kappa_T,
            'effective_coupling': lambda_T,
            'power_sums': p_T,
        },
        'W_channel': {
            'kappa': kappa_W,
            'alpha': alpha_w3,
            'S3_W': S3_W,
        },
        'channels': ['TT', 'TW', 'WW'],
        'note': ('Multi-channel Newton identities couple T and W '
                 'through mixed brackets. On each 1d slice, '
                 'Newton holds with slice-specific Satake parameters.'),
    }


# =====================================================================
# Section 9: Genus-g Newton corrections
# =====================================================================

def genus_g_newton_correction(alpha: complex, beta: complex,
                              g: int, r: int) -> Dict[str, Any]:
    r"""Structure of the genus-g correction to Newton's identity.

    At genus 0: the standard Newton identity p_r = e1*p_{r-1} - e2*p_{r-2}.

    At genus g >= 1: the MC equation receives contributions from genus-g
    compositions in the modular operad.  The genus-g correction to
    Newton's identity at arity r+1 is:

        p_r^{(g)} = e1 * p_{r-1}^{(g)} - e2 * p_{r-2}^{(g)} + delta_r^{(g)}

    where delta_r^{(g)} comes from the genus-g graph sums.

    GENUS-1 CORRECTION:
    At genus 1, the correction involves the trace tr(m_2^{r-1}),
    which for the two-variable case (Satake type) gives:

        delta_r^{(1)} = (kappa / 24) * d/dr [p_r]
                      = (kappa / 24) * (alpha^r log(alpha) + beta^r log(beta))

    This is the genus-1 anomaly coefficient times the logarithmic
    derivative of the power sum.

    IMPORTANT (AP15): The genus-1 propagator is E_2*(tau), which is
    QUASI-MODULAR.  The correction delta_r^{(1)} involves quasi-modular
    forms, NOT holomorphic modular forms.

    GENUS-2 AND HIGHER:
    At genus g >= 2, the corrections involve planted-forest graph sums.
    For genus 2: delta_r^{(2)} involves S_3*(10*S_3 - kappa)/48
    (the planted-forest correction, eq:delta-pf-genus2-explicit).

    The key observation: the genus-g Newton identity has the SAME
    homogeneous part (e1*p_{r-1} - e2*p_{r-2}) as genus 0, but with
    an inhomogeneous correction delta_r^{(g)} that depends on the
    modular data of the algebra.
    """
    e1 = alpha + beta
    e2 = alpha * beta
    p_r = alpha ** r + beta ** r
    p_rm1 = alpha ** (r - 1) + beta ** (r - 1) if r >= 2 else e1
    p_rm2 = alpha ** (r - 2) + beta ** (r - 2) if r >= 3 else 2.0

    # Genus-0 residual (should be zero)
    genus0_res = p_r - e1 * p_rm1 + e2 * p_rm2

    # Genus-1 correction structure
    if g == 1:
        # The correction involves log derivatives
        # delta_r^{(1)} ~ kappa/24 * (alpha^r * log(alpha) + beta^r * log(beta))
        # For the Ramanujan Delta at prime p:
        #   kappa = c/2 where c = rank of lattice (here c relates to weight k=12)
        # The genus-1 correction is the first-order modular anomaly.

        # Formal structure: tr(m_2^{r-1}) gives a (r-1)-fold iterated
        # composition in genus 1.  This equals:
        #   sum_j alpha_j^{r-1} * (genus-1 propagator at alpha_j)
        try:
            if abs(alpha) > 0 and abs(beta) > 0:
                log_a = cmath.log(alpha)
                log_b = cmath.log(beta)
                delta_g1 = alpha ** r * log_a + beta ** r * log_b
            else:
                delta_g1 = 0
        except (ValueError, ZeroDivisionError):
            delta_g1 = 0

        return {
            'genus': g,
            'arity': r,
            'genus0_residual': genus0_res,
            'correction_structure': 'kappa/24 * (alpha^r log(alpha) + beta^r log(beta))',
            'delta_formal': delta_g1,
            'note': ('Genus-1 correction involves quasi-modular E_2* (AP15). '
                     'The trace tr(m_2^{r-1}) encodes iterated genus-1 '
                     'compositions.'),
        }

    elif g >= 2:
        return {
            'genus': g,
            'arity': r,
            'genus0_residual': genus0_res,
            'correction_structure': f'genus-{g} planted-forest graph sum',
            'note': (f'At genus {g}, the correction involves {g}-loop '
                     f'planted-forest graphs. The genus-{g} Newton identity '
                     f'has the same homogeneous part but an inhomogeneous '
                     f'correction from modular operad composition.'),
        }

    return {
        'genus': g,
        'arity': r,
        'genus0_residual': genus0_res,
    }


# =====================================================================
# Section 10: Beyond Newton -- GL(n) constraints
# =====================================================================

def beyond_newton_analysis(n: int, max_r: int = 20) -> Dict[str, Any]:
    r"""Analyze what the shadow tower provides beyond Newton for GL(n).

    For GL(n) with n Satake parameters, Newton's identities from
    {p_1, ..., p_n} determine all p_r for r > n.  The shadow tower
    provides p_r for all r >= 2.

    ANSWER TO THE DEEP QUESTION:
    For GL(2) (n=2), the shadow tower provides p_r for all r >= 2,
    but Newton's identity p_r = e1*p_{r-1} - e2*p_{r-2} means ALL
    p_r for r >= 3 are determined by (p_1, p_2).  So the shadow
    tower at arities > 4 provides NO additional constraints on
    the Satake parameters {alpha, beta}.  The constraints are
    EXACTLY Newton's identities -- they are tautologically satisfied.

    For GL(n) with n > 2: Newton's identities from {p_1, ..., p_n}
    determine {e_1, ..., e_n} and hence all p_r for r > n.
    The shadow tower still provides p_r for all r, but the
    additional constraints beyond arity n+2 are consequences of
    the first n power sums.

    WHAT IS NEW from the MC equation beyond Newton:
    1. GENUS CORRECTIONS: At genus g >= 1, the MC equation provides
       corrections to Newton's identity (Section 9).  These are
       NOT classical Newton identities -- they involve modular
       data (E_2*, Hodge classes, planted-forest graphs).

    2. POSITIVITY: The MC bracket defines a positive-definite form
       on the shadow space (thm:petersson-identification), which
       constrains the WEIGHTS c_j in the Hecke decomposition
       but NOT the eigenvalues a_j(p).

    3. CROSS-PRIME COHERENCE: The MC equation holds simultaneously
       at ALL primes.  Newton's identities are prime-local (they
       hold independently at each p).  The MC equation imposes
       GLOBAL coherence through the modular form structure of Theta_A.
    """
    # For n variables: p_r for r > n is determined by p_1,...,p_n
    # Number of independent constraints: n (the elementary sym polys)
    # Number of power sums from shadow at arity r=2,...,R: R-1
    # For R > n+1: the extra R-1-n power sums are redundant (Newton consequences)

    independent_from_shadow = min(n, max_r - 1)
    redundant = max(0, max_r - 1 - n)

    return {
        'gl_rank': n,
        'max_arity_checked': max_r,
        'independent_power_sums': independent_from_shadow,
        'redundant_power_sums': redundant,
        'newton_determines_all': True,
        'genus0_beyond_newton': 'NOTHING (all genus-0 constraints are Newton)',
        'genus1_beyond_newton': ('Quasi-modular corrections delta_r^{(1)} '
                                 'involving E_2* and trace of iterated '
                                 'compositions'),
        'higher_genus_beyond_newton': ('Planted-forest graph sum corrections '
                                       'at each genus'),
        'cross_prime_coherence': ('MC equation holds at ALL primes '
                                  'simultaneously, imposing global '
                                  'automorphic structure'),
        'positivity': ('MC bracket form is positive-definite on '
                       'cusp-form subspace (Petersson), constraining '
                       'Hecke decomposition WEIGHTS but not EIGENVALUES'),
    }


# =====================================================================
# Section 11: Comprehensive Delta verification
# =====================================================================

def delta_comprehensive_verification(primes: Optional[List[int]] = None,
                                     max_r: int = 8) -> Dict[str, Any]:
    r"""Full Newton identity verification for Ramanujan Delta at multiple primes.

    Verifies:
    1. Satake parameters satisfy alpha*beta = p^11 at each prime
    2. Ramanujan bound |alpha| = |beta| = p^{11/2} (Deligne)
    3. Newton's identity at each arity
    4. Power sum consistency (direct vs recursive)
    5. Atom reconstruction from (p_1, p_2)
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]

    results = {}
    for p in primes:
        sat = delta_satake_at_prime(p)
        newton = delta_newton_verification(p, max_r)
        recon = verify_reconstruction(sat['alpha'], sat['beta'], max_r)

        results[p] = {
            'satake': sat,
            'newton': newton,
            'reconstruction': recon,
            'product_correct': abs(sat['abs_product'] - p ** 11) < 1,
            'ramanujan_holds': sat['satisfies_ramanujan'],
            'all_newton_hold': newton['all_newton_hold'],
            'atoms_reconstructed': recon['match'],
        }

    # Summary
    all_ok = all(
        r['product_correct'] and r['ramanujan_holds']
        and r['all_newton_hold'] and r['atoms_reconstructed']
        for r in results.values()
    )

    return {
        'primes': primes,
        'max_arity': max_r,
        'per_prime': results,
        'all_passed': all_ok,
    }
