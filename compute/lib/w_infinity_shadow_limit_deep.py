r"""Finite-N and formal large-N diagnostics for principal W_N shadows.

Certified finite-N scalar constants in this module are:

1. Fateev-Lukyanov central charge
   c(W_N,k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).
2. Principal W_N modular characteristic
   kappa(W_N) = c(H_N - 1) = sum_{s=2}^{N} c/s.
3. Virasoro T-line constants
   S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)],
   S_5 = -48/[c^2(5c+22)] on c(5c+22) != 0.
4. Principal W_3 W-line quartic constant
   S_4^W = 2560/[c(5c+22)^3].
5. Feigin-Frenkel central-charge conductor
   K_N^c = c(k) + c(-k-2N) = 4N^3 - 2N - 2.

The large-N functions below are formal diagnostics of these scalar
finite-N formulas.  They do not certify an analytic W_infinity object,
an all-genus partition function, a tau function, Borel/resurgent
summability, integrable-hierarchy membership, or a multi-channel
inverse limit.  Higher-spin channels beyond the T-line are marked
non-certified unless a local exact finite-N formula is available.

In the fixed positive 't Hooft parameter lambda = N/(k+N) lane,
k+N = N/lambda and

    c(N,lambda) = (N-1) - (N^2-1)(N-lambda)^2/lambda,

so c ~ -N^4/lambda for fixed lambda > 0.  The lambda = 0 free-field
lane c = N-1 is a separate singular boundary diagnostic.

Object firewall: A, B(A), A^i, A^!, and Z_ch^der(A) are distinct.
Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.  The
Verdier/continuous-linear branch controls A^!; Hochschild cochains
control the derived centre.
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl


FINITE_N_EXACT = "finite_N_exact"
FORMAL_LIMIT_DIAGNOSTIC = "formal_N_limit_diagnostic"
SCALAR_AHAT_BERNOULLI = "scalar_ahat_bernoulli"
NOT_CERTIFIED = "not_certified"


def claim_certification_firewall() -> Dict[str, Dict[str, Any]]:
    """Certification boundary for data produced by this engine."""
    return {
        "finite_N_constants": {
            "certified": True,
            "lane": FINITE_N_EXACT,
            "sources": (
                "chapters/examples/landscape_census.tex",
                "compute/lib/wn_central_charge_canonical.py",
                "chapters/examples/w_algebras_deep.tex",
            ),
        },
        "formal_N_limit_diagnostics": {
            "certified": True,
            "lane": FORMAL_LIMIT_DIAGNOSTIC,
            "analytic_certified": False,
        },
        "scalar_ahat_bernoulli_lane": {
            "certified": True,
            "lane": SCALAR_AHAT_BERNOULLI,
            "partition_function_certified": False,
        },
        "multiweight_cross_channel_data": {
            "certified": False,
            "finite_certified_cases": ("T-line", "principal W_3 W-line"),
        },
        "winfinity_inverse_limit": {
            "certified": False,
            "tline_formal_compatible": True,
        },
        "all_genus_partition_function": {"certified": False},
        "analytic_tau_function": {"certified": False},
        "borel_resurgence": {"certified": False},
        "integrable_hierarchy_membership": {"certified": False},
    }


# ============================================================================
# 1.  Fundamental arithmetic (exact Fraction)
# ============================================================================

@lru_cache(maxsize=256)
def harmonic(n: int) -> Fraction:
    """H_n = 1 + 1/2 + ... + 1/n.  H_0 = 0."""
    if n <= 0:
        return Fraction(0)
    return sum(Fraction(1, j) for j in range(1, n + 1))


@lru_cache(maxsize=64)
def bernoulli_number(n: int) -> Fraction:
    """Bernoulli number B_n, exact for the scalar Faber-Pandharipande lane."""
    if n < 0:
        raise ValueError("Bernoulli index must be non-negative")
    work = [Fraction(0) for _ in range(n + 1)]
    for m in range(n + 1):
        work[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            work[j - 1] = j * (work[j - 1] - work[j])
    return work[0]


def scalar_ahat_bernoulli_free_energy(kappa_val: Fraction, genus: int) -> Fraction:
    r"""Scalar Faber-Pandharipande/A-hat coefficient.

    F_g = kappa * ((2^(2g-1)-1)/2^(2g-1)) * |B_{2g}|/(2g)!.
    This is a scalar lambda_g coefficient, not an all-genus partition
    function and not a tau-function certification.
    """
    if genus < 1:
        raise ValueError("genus must be at least 1")
    weight = Fraction(2 ** (2 * genus - 1) - 1, 2 ** (2 * genus - 1))
    bernoulli = abs(bernoulli_number(2 * genus))
    return kappa_val * weight * bernoulli / math.factorial(2 * genus)


def anomaly_ratio(N: int) -> Fraction:
    r"""Anomaly ratio rho(W_N) = H_N - 1 = sum_{s=2}^{N} 1/s.

    kappa(W_N) = rho(N) * c.
    N=2: rho = 1/2 (Virasoro).
    N=3: rho = 5/6.
    N=4: rho = 13/12.
    """
    if N < 2:
        return Fraction(0)
    return harmonic(N) - 1


def c_WN(N: int, k_val: Fraction) -> Fraction:
    r"""Central charge of principal W_N at level k.

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

    Fateev-Lukyanov formula.  Decisive test: N=2, k=1 gives c=-7.
    Complementarity: c(k) + c(-k-2N) = 2(N-1) + 4N(N^2-1).
    """
    return canonical_c_wn_fl(N, k_val)


def kappa_total(N: int, c_val: Fraction) -> Fraction:
    """Total modular characteristic kappa(W_N) = (H_N - 1) * c."""
    return anomaly_ratio(N) * c_val


def kappa_channel(s: int, c_val: Fraction) -> Fraction:
    """Channel curvature kappa_s = c/s for the spin-s generator."""
    return c_val / Fraction(s)


def ghost_central_charge(N: int) -> Fraction:
    """Ghost sector central charge c_ghost = N(N-1) (level-independent)."""
    return Fraction(N * (N - 1))


def ghost_kappa(N: int) -> Fraction:
    """Ghost sector kappa = c_ghost/2 = N(N-1)/2."""
    return Fraction(N * (N - 1), 2)


def ff_dual_level(N: int, k_val: Fraction) -> Fraction:
    """Feigin-Frenkel dual level: k' = -k - 2h^v = -k - 2N."""
    return -k_val - 2 * Fraction(N)


def ff_central_charge_sum(N: int) -> Fraction:
    r"""c(k) + c(k') = 2(N-1) + 4N(N^2-1) under Feigin-Frenkel duality.

    Freudenthal-de Vries identity.  Independent of k.
    At N=2: 26.  At N=3: 100.  At N=4: 246.
    Source: wn_central_charge_canonical.py::complementarity_sum.
    """
    # VERIFIED: c_wn_fl(2,1)+c_wn_fl(2,-5)=26, c_wn_fl(3,1)+c_wn_fl(3,-7)=100
    return Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))


# ============================================================================
# 2.  't Hooft parameterization
# ============================================================================

def thooft_c(N: int, lam: float) -> float:
    r"""Central charge in the 't Hooft limit (float version).

    lambda = N/(k+N), so k = N*(1-lam)/lam.
    Delegates to canonical Fateev-Lukyanov formula.
    At lambda = 0: c = N-1 (free field limit).
    """
    if abs(lam) < 1e-30:
        return float(N - 1)
    k_val = N * (1.0 - lam) / lam
    return float(canonical_c_wn_fl(N, Fraction(k_val).limit_denominator(10**12)))


def thooft_c_exact(N: int, lam: Fraction) -> Fraction:
    r"""Exact central charge at 't Hooft coupling lambda = N/(k+N).

    Inverts lambda = N/(k+N) to k = N(1-lam)/lam, then applies canonical
    Fateev-Lukyanov formula c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).
    """
    if lam == 0:
        return Fraction(N - 1)
    kN = Fraction(N) / lam          # k + N
    k_val = kN - Fraction(N)        # k
    return canonical_c_wn_fl(N, k_val)


def thooft_kappa_total(N: int, lam: float) -> float:
    """Total kappa in the 't Hooft limit."""
    rho = float(anomaly_ratio(N))
    return rho * thooft_c(N, lam)


def thooft_c_large_N(N: int, lam: float) -> float:
    r"""Large-N asymptotic of central charge at fixed lambda.

    c = (N-1) - (N^2-1)*(N-lam)^2/lam
      ~ -N^4 * lam^{-1} for large N at fixed lam > 0.

    For lam = 0: c ~ N-1 (free-field limit).
    """
    if abs(lam) < 1e-30:
        return float(N - 1)
    return (N - 1) - (N * N - 1) * (N - lam) ** 2 / lam


def thooft_regime_analysis(lam: float, N_values: Optional[List[int]] = None) -> List[Dict]:
    """Tabulate the formal 't Hooft substitution as a function of N.

    The analytic positive-c regime is not inferred from this scalar table.
    """
    if N_values is None:
        N_values = list(range(2, 31))

    results = []
    for N in N_values:
        c_val = thooft_c(N, lam)
        kap = thooft_kappa_total(N, lam)
        rho_T = _rho_tline(c_val) if c_val > 0 else None

        results.append({
            'N': N,
            'c': c_val,
            'kappa_total': kap,
            'rho_T': rho_T,
            'c_positive': c_val > 0,
            'positive_c_bound_certified': False,
            'analytic_certified': False,
        })
    return results


# ============================================================================
# 3.  Shadow tower computation (single-channel, float arithmetic)
# ============================================================================

def _rho_tline(c_val: float) -> Optional[float]:
    """Shadow growth rate on the T-line (Virasoro).

    rho = sqrt((180c + 872)/((5c+22)*c^2))
    """
    if c_val <= 0 or (5 * c_val + 22) <= 0:
        return None
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    if denom <= 0:
        return None
    return math.sqrt(numer / denom)


def shadow_tower_single_channel(kap: float, alpha: float, S4: float,
                                max_arity: int = 10) -> Dict[int, float]:
    r"""Shadow tower on a single primary line via convolution recursion.

    Q_L(t) = (2*kap)^2 + 12*kap*alpha*t + (9*alpha^2 + 16*kap*S4)*t^2.
    f(t) = sqrt(Q_L(t)) = sum a_n t^n.
    S_r = a_{r-2} / r.

    Uses the standard recursion:
        a_0 = 2*kap
        a_1 = q1 / (2*a_0)
        a_2 = (q2 - a_1^2) / (2*a_0)
        a_n = -(sum_{j=1}^{n-1} a_j * a_{n-j}) / (2*a_0)  for n >= 3
    """
    if abs(kap) < 1e-100:
        return {r: 0.0 for r in range(2, max_arity + 1)}

    q0 = 4.0 * kap ** 2
    q1 = 12.0 * kap * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kap * S4

    a0 = 2.0 * kap
    coeffs = [a0]

    max_n = max_arity - 2
    if max_n >= 1:
        a1 = q1 / (2.0 * a0)
        coeffs.append(a1)
    if max_n >= 2:
        a2 = (q2 - a1 * a1) / (2.0 * a0)
        coeffs.append(a2)
    for n in range(3, max_n + 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv_sum / (2.0 * a0))

    tower = {}
    for n in range(len(coeffs)):
        r = n + 2
        tower[r] = coeffs[n] / r
    return tower


def shadow_tower_tline(c_val: float, max_arity: int = 10) -> Dict[int, float]:
    """T-line shadow tower: Virasoro sub-tower at central charge c."""
    if abs(c_val) < 1e-100:
        return {r: 0.0 for r in range(2, max_arity + 1)}
    if abs(5.0 * c_val + 22.0) < 1e-100:
        raise ValueError("singular Virasoro shadow surface c(5c+22)=0")
    kap = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    return shadow_tower_single_channel(kap, alpha, S4, max_arity)


def shadow_tower_wline_w3(c_val: float, max_arity: int = 10) -> Dict[int, float]:
    r"""W-line shadow tower for W_3 (spin-3 channel).

    kappa_W = c/3, alpha_W = 0 (Z_2 parity), S4_W = 2560/(c*(5c+22)^3).
    The Z_2 parity W -> -W forces alpha = 0 (odd arities vanish on the W-line).
    """
    if abs(c_val) < 1e-100:
        return {r: 0.0 for r in range(2, max_arity + 1)}
    kap = c_val / 3.0
    alpha = 0.0
    denom = c_val * (5.0 * c_val + 22.0) ** 3
    if abs(denom) < 1e-100:
        return {r: 0.0 for r in range(2, max_arity + 1)}
    S4 = 2560.0 / denom
    return shadow_tower_single_channel(kap, alpha, S4, max_arity)


# ============================================================================
# 4.  Multi-channel shadow data for general W_N
# ============================================================================

def wn_channel_data(N: int, c_val: float) -> List[Dict]:
    r"""Finite scalar channel data for W_N.

    W_N has N-1 generators of spins s = 2, 3, ..., N.
    Each channel has:
        kappa_s = c/s
        alpha_s: cubic shadow when known
        S4_s: quartic shadow when locally certified
        Delta_s = 8*kappa_s*S4_s when S4_s is known

    The T-line (s=2) data is the exact Virasoro formula.
    The principal W_3 W-line is exact in the local manuscript.
    General s >= 3 data depends on full W_N OPE/cross-channel structure
    and is not inferred from the finite scalar kappa_s value.
    """
    channels = []

    if abs(c_val) < 1e-100:
        for s in range(2, N + 1):
            channels.append({
                'spin': s,
                'kappa': 0.0,
                'alpha': 0.0,
                'S4': 0.0,
                'Delta': 0.0,
                'depth_class': 'degenerate',
                'certification': FINITE_N_EXACT,
            })
        return channels

    for s in range(2, N + 1):
        kap = c_val / s

        if s == 2:
            alpha = 2.0
            denom = c_val * (5.0 * c_val + 22.0)
            S4 = 10.0 / denom if abs(denom) > 1e-100 else None
            certification = FINITE_N_EXACT if S4 is not None else NOT_CERTIFIED
        elif N == 3 and s == 3:
            alpha = 0.0
            denom = c_val * (5.0 * c_val + 22.0) ** 3
            S4 = 2560.0 / denom if abs(denom) > 1e-100 else None
            certification = FINITE_N_EXACT if S4 is not None else NOT_CERTIFIED
        else:
            alpha = None
            S4 = None
            certification = NOT_CERTIFIED

        Delta = 8.0 * kap * S4 if S4 is not None else None
        if Delta is None:
            depth_class = NOT_CERTIFIED
        elif abs(Delta) > 1e-100:
            depth_class = 'M'
        elif abs(S4) > 1e-100:
            depth_class = 'C'
        elif alpha is not None and abs(alpha) > 1e-100:
            depth_class = 'L'
        else:
            depth_class = 'G'

        channels.append({
            'spin': s,
            'kappa': kap,
            'alpha': alpha,
            'S4': S4,
            'Delta': Delta,
            'depth_class': depth_class,
            'certification': certification,
        })

    return channels


def wn_kappa_decomposition(N: int, c_val: float) -> Dict:
    r"""Decomposition of total kappa into channel contributions.

    kappa(W_N) = sum_{s=2}^{N} c/s = c * (H_N - 1)

    Verification: direct sum vs formula.
    """
    channel_sum = sum(c_val / s for s in range(2, N + 1))
    formula = float(anomaly_ratio(N)) * c_val
    return {
        'N': N,
        'c': c_val,
        'channel_sum': channel_sum,
        'formula': formula,
        'match': abs(channel_sum - formula) < 1e-10 * max(abs(formula), 1e-100),
        'anomaly_ratio': float(anomaly_ratio(N)),
    }


# ============================================================================
# 5.  Large-N scaling of shadow coefficients
# ============================================================================

def large_N_tline_scaling(N_values: Optional[List[int]] = None,
                          k_val: float = 5.0,
                          max_arity: int = 8) -> Dict[str, Any]:
    r"""Analyze the N-dependence of T-line shadow coefficients at fixed level k.

    The T-line data depends on N only through c(W_N, k).  At fixed k:
        c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

    For large N at fixed k: c ~ -N^4.
    The central charge goes to -infinity quartically: the shadow tower on the
    T-line enters the negative-c regime where the standard growth rate
    formula does not apply directly.

    Returns: per-arity scaling analysis, central charge data.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20]

    c_data = []
    tower_data = {r: [] for r in range(2, max_arity + 1)}

    for N in N_values:
        k_frac = Fraction(k_val).limit_denominator(10**12)
        if k_frac + N == 0:
            continue
        c_val = float(canonical_c_wn_fl(N, k_frac))
        c_data.append((N, c_val))

        if abs(c_val) < 1e-100 or abs(5 * c_val + 22) < 1e-100:
            continue
        try:
            tower = shadow_tower_tline(c_val, max_arity)
            for r in range(2, max_arity + 1):
                if r in tower and math.isfinite(tower[r]):
                    tower_data[r].append((N, tower[r]))
        except (ValueError, ZeroDivisionError):
            continue

    # Extract scaling exponents via log-log fit on last two valid points
    exponents = {}
    for r in range(2, max_arity + 1):
        pts = tower_data[r]
        if len(pts) >= 2:
            N1, s1 = pts[-2]
            N2, s2 = pts[-1]
            if abs(s1) > 1e-100 and abs(s2) > 1e-100 and s1 * s2 > 0:
                exp = math.log(abs(s2) / abs(s1)) / math.log(N2 / N1)
            else:
                exp = None
        else:
            exp = None
        exponents[r] = exp

    return {
        'c_data': c_data,
        'tower_data': tower_data,
        'exponents': exponents,
        'regime': 'fixed_k',
    }


def large_N_thooft_scaling(lam: float = 0.1,
                           N_values: Optional[List[int]] = None,
                           max_arity: int = 8) -> Dict[str, Any]:
    r"""Formal N-dependence of T-line coefficients after the 't Hooft substitution.

    At fixed lambda = N/(k+N),
        c = (N-1) - (N^2-1)(N-lambda)^2/lambda.

    For fixed lambda > 0 this is negative quartic in N in the canonical
    Fateev-Lukyanov normalization.  The table is therefore a finite-scalar
    diagnostic, not an analytic large-N certification.
    """
    if N_values is None:
        N_values = list(range(2, 51))

    c_data = []
    tower_data = {r: [] for r in range(2, max_arity + 1)}
    kappa_data = []
    rho_data = []

    for N in N_values:
        c_val = thooft_c(N, lam)
        if abs(c_val) < 1e-100 or abs(5 * c_val + 22) < 1e-100:
            continue
        c_data.append((N, c_val))

        kap_total = thooft_kappa_total(N, lam)
        kappa_data.append((N, kap_total))

        rho = _rho_tline(c_val)
        if rho is not None:
            rho_data.append((N, rho))

        try:
            tower = shadow_tower_tline(c_val, max_arity)
            for r in range(2, max_arity + 1):
                if r in tower and math.isfinite(tower[r]):
                    tower_data[r].append((N, tower[r]))
        except (ValueError, ZeroDivisionError):
            continue

    # Scaling exponents
    exponents = {}
    for r in range(2, max_arity + 1):
        pts = tower_data[r]
        if len(pts) >= 2:
            N1, s1 = pts[-2]
            N2, s2 = pts[-1]
            if abs(s1) > 1e-100 and abs(s2) > 1e-100 and s1 * s2 > 0:
                exp = math.log(abs(s2) / abs(s1)) / math.log(N2 / N1)
            else:
                exp = None
        else:
            exp = None
        exponents[r] = exp

    return {
        'lambda': lam,
        'c_data': c_data,
        'tower_data': tower_data,
        'kappa_data': kappa_data,
        'rho_data': rho_data,
        'exponents': exponents,
        'regime': 'thooft',
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        'analytic_certified': False,
    }


# ============================================================================
# 6.  1/N expansion: planar shadow and corrections
# ============================================================================

def planar_shadow_tline(lam: float, max_arity: int = 10) -> Dict[str, Any]:
    r"""Numerical finite-N fit for a putative T-line planar coefficient.

    In the 't Hooft limit at fixed lambda, the T-line central charge is
        c(N, lam) = (N-1) - (N^2-1)(N-lam)^2/lam  (exact in lambda)

    For fixed lambda > 0: c ~ -N^4/lambda.

    The T-line shadow coefficients S_r depend on c only.  So we can
    sample them as functions of N at fixed lambda and fit in 1/N when
    enough positive-c points exist.

    The result is a diagnostic fit.  It is not an analytic planar limit
    or hierarchy-membership certificate.
    """
    candidate_N = [10, 20, 30, 50, 80, 100, 150, 200]
    N_values = [n for n in candidate_N if thooft_c(n, lam) > 0]

    if len(N_values) < 3:
        return {
            'lambda': lam,
            'error': 'insufficient positive-c points',
            'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
            'analytic_certified': False,
        }

    # Collect S_r(N)
    sr_data = {r: [] for r in range(2, max_arity + 1)}
    for N in N_values:
        c_val = thooft_c(N, lam)
        if c_val <= 0 or abs(5 * c_val + 22) < 1e-100:
            continue
        try:
            tower = shadow_tower_tline(c_val, max_arity)
            for r in range(2, max_arity + 1):
                if r in tower and math.isfinite(tower[r]):
                    sr_data[r].append((N, tower[r]))
        except (ValueError, ZeroDivisionError):
            continue

    # Fit S_r(N) = a + b/N + c/N^2 via least squares (at most 3 terms)
    planar = {}
    corrections = {}
    for r in range(2, max_arity + 1):
        pts = sr_data[r]
        if len(pts) < 3:
            planar[r] = None
            corrections[r] = None
            continue

        # Use the last 3 points for a simple 3-parameter fit
        # S_r = a + b/N + d/N^2
        # Build system: each row is [1, 1/N, 1/N^2], RHS is S_r
        import numpy as np
        Ns = np.array([p[0] for p in pts], dtype=float)
        Ss = np.array([p[1] for p in pts], dtype=float)
        A = np.column_stack([np.ones_like(Ns), 1.0 / Ns, 1.0 / Ns ** 2])
        try:
            coeffs, residuals, rank, sv = np.linalg.lstsq(A, Ss, rcond=None)
            planar[r] = coeffs[0]
            corrections[r] = {'c1': coeffs[1], 'c2': coeffs[2]}
        except np.linalg.LinAlgError:
            planar[r] = None
            corrections[r] = None

    return {
        'lambda': lam,
        'planar_coefficients': planar,
        'one_over_N_corrections': corrections,
        'N_values_used': N_values,
        'sr_data': sr_data,
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        'analytic_certified': False,
    }


def one_over_N_expansion_kappa(lam: float, N_values: Optional[List[int]] = None) -> Dict:
    r"""1/N expansion of the NORMALIZED kappa.

    kappa(W_N) / N = (H_N - 1) * c / N

    For large N: H_N - 1 ~ log(N) + gamma - 1 (Euler-Mascheroni gamma ~ 0.5772).
    For fixed lambda > 0 in the canonical normalization,
    c/N ~ -N^3/lambda.

    So kappa/N ~ -(N^3/lambda)(log(N) + gamma - 1).
    For lambda > 0: kappa/N ~ -(N^3/lambda)log(N) -> -infinity.
    For lambda = 0: kappa/N ~ (log(N) + gamma - 1) -> infinity (slowly).

    The NORMALIZED quantity kappa/(N*c) = (H_N-1)/N -> 0 as N -> infinity
    (harmonic number grows as log(N), so (H_N-1)/N ~ log(N)/N -> 0).

    The quotient kappa/(c log N) tends to 1 when c != 0 is used only as
    the finite-N scalar central charge.
    """
    if N_values is None:
        N_values = list(range(3, 51))

    gamma_em = 0.5772156649015329  # Euler-Mascheroni

    results = []
    for N in N_values:
        c_val = thooft_c(N, lam)
        rho_N = float(anomaly_ratio(N))
        kap = rho_N * c_val

        # Asymptotic prediction
        log_N = math.log(N)
        rho_asymp = log_N + gamma_em - 1.0

        results.append({
            'N': N,
            'c': c_val,
            'rho_exact': rho_N,
            'rho_asymp': rho_asymp,
            'rho_error': abs(rho_N - rho_asymp),
            'kappa': kap,
            'kappa_over_N': kap / N if N > 0 else None,
            'kappa_over_logN': kap / log_N if log_N > 0 else None,
        })

    return {
        'lambda': lam,
        'gamma_EM': gamma_em,
        'data': results,
    }


# ============================================================================
# 7.  Shadow growth rate convergence
# ============================================================================

def growth_rate_convergence(lam: float = 0.0,
                            N_values: Optional[List[int]] = None) -> Dict[str, Any]:
    r"""T-line algebraic growth diagnostic for sampled N.

    Since the T-line rho depends only on c:
        rho_T(c) = sqrt((180c + 872)/((5c+22)*c^2))

    At lambda = 0 (free field): c = N-1, so
        rho_T(N-1) = sqrt((180(N-1) + 872)/((5(N-1)+22)*(N-1)^2))
                   = sqrt((180N + 692)/((5N+17)*(N-1)^2))
                   ~ sqrt(180/(5*N^2)) = sqrt(36/N^2) = 6/N for large N.

    Thus rho_T -> 0 as 6/N on the lambda = 0 scalar lane.  The flag
    rho < 1 is an algebraic coefficient diagnostic, not analytic
    convergence of a partition function or tau function.

    At fixed lambda > 0: c ~ -N^4/lambda for large N.
    If lam = 0: rho ~ 6/N.
    """
    if N_values is None:
        N_values = list(range(2, 51))

    data = []
    for N in N_values:
        c_val = thooft_c(N, lam) if lam > 0 else float(N - 1)
        if c_val <= 0 or abs(5 * c_val + 22) < 1e-100:
            continue
        rho = _rho_tline(c_val)
        if rho is None:
            continue

        # Asymptotic prediction at lambda=0: rho ~ 6/N
        rho_asymp = 6.0 / N if lam == 0 else None

        data.append({
            'N': N,
            'c': c_val,
            'rho': rho,
            'rho_asymp': rho_asymp,
            'rho_times_N': rho * N,
            'rho_times_c': rho * c_val,
            'convergent': rho < 1.0,
        })

    # Limit: rho * N at lambda=0 should converge to 6
    rho_N_products = [d['rho_times_N'] for d in data]
    limit_rho_N = rho_N_products[-1] if rho_N_products else None

    return {
        'lambda': lam,
        'data': data,
        'rho_times_N_limit': limit_rho_N,
        'rho_limit': data[-1]['rho'] if data else None,
        'expected_rho_times_N': 6.0 if lam == 0 else None,
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        'analytic_certified': False,
    }


def growth_rate_all_channels(N: int, c_val: float) -> Dict[str, Optional[float]]:
    r"""Certified channel growth diagnostics for W_N.

    rho_s = sqrt((9*alpha_s^2 + 2*Delta_s)) / (2*|kappa_s|)

    For the T-line (s=2): fully computed.
    For s >= 3: requires finite-N OPE data; only the principal W_3 W-line
    is certified in this module.
    """
    result = {}

    # T-line
    rho_T = _rho_tline(c_val)
    result['T'] = rho_T if rho_T is not None else 0.0

    # Higher-spin channels: would need S4 data from OPE
    for s in range(3, N + 1):
        kap = c_val / s
        if abs(kap) < 1e-100:
            result[f'W_{s}'] = 0.0
            continue
        if s == 3 and N == 3:
            denom = c_val * (5.0 * c_val + 22.0) ** 3
            if abs(denom) > 1e-100:
                S4_W = 2560.0 / denom
                Delta_W = 8.0 * kap * S4_W
                numer_sq = 2.0 * Delta_W  # alpha=0 for W-line
                if numer_sq > 0:
                    result['W_3'] = math.sqrt(numer_sq) / (2.0 * abs(kap))
                else:
                    result['W_3'] = 0.0
            else:
                result['W_3'] = 0.0
        else:
            result[f'W_{s}'] = None  # unknown without OPE data

    return result


# ============================================================================
# 8.  Koszul conductor scaling
# ============================================================================

def koszul_conductor_ff(N: int) -> Fraction:
    """Feigin-Frenkel central-charge conductor K_N^c.

    K_N^c = c(k) + c(-k-2N) = 2(N-1) + 4N(N^2-1)
          = 4N^3 - 2N - 2.

    This scalar conductor does not construct A^!, Omega(B(A)), or the
    Hochschild derived centre.
    """
    return ff_central_charge_sum(N)


def kappa_sum_ff(N: int) -> Fraction:
    r"""kappa(W_N, k) + kappa(W_N, k') under FF duality.

    kappa + kappa' = rho(N) * (c + c')
                   = (H_N - 1) * [2(N-1) + 4N(N^2-1)].

    N=2: 13.
    N=3: 250/3.
    N=4: 533/2.
    N=5: 9394/15.
    """
    return ff_central_charge_sum(N) * anomaly_ratio(N)


def chiral_koszul_conductor(N: int) -> Optional[Fraction]:
    r"""Central-charge conductor on the principal W_N FF/Verdier branch.

    Local canonical formula:
        K_N^c = 4N^3 - 2N - 2.

    The historical function name is retained for compatibility.  The
    returned scalar is not a bar-cobar inversion statement and not a
    Hochschild/bulk computation.
    """
    return ff_central_charge_sum(N)


def koszul_conductor_scaling(N_values: Optional[List[int]] = None) -> List[Dict]:
    r"""Formal large-N scaling of the FF/Verdier scalar conductor.

    K_N^c = 4N^3 - 2N - 2 ~ 4N^3.

    The kappa complementarity sum:
    kappa + kappa' = rho(N) * K_N^c
                     ~ (log(N) + gamma - 1) * 4N^3

    This grows as N^3 * log(N), so the complementarity sum diverges.
    """
    if N_values is None:
        N_values = list(range(2, 21))

    results = []
    for N in N_values:
        K = chiral_koszul_conductor(N)
        K_float = float(K)
        rho_N = float(anomaly_ratio(N))
        kap_sum = rho_N * K_float

        results.append({
            'N': N,
            'K': K_float,
            'K_over_N3': K_float / N ** 3 if N > 0 else None,
            'K_over_2N3': K_float / (2.0 * N ** 3) if N > 0 else None,
            'K_over_4N3': K_float / (4.0 * N ** 3) if N > 0 else None,
            'rho': rho_N,
            'kappa_sum': kap_sum,
            'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        })

    return results


# ============================================================================
# 9.  Higher-spin limit (lambda = 0)
# ============================================================================

def higher_spin_shadow(N_values: Optional[List[int]] = None,
                       max_arity: int = 8) -> Dict[str, Any]:
    r"""T-line scalar diagnostics on the lambda = 0 free-field boundary.

    At lambda = 0: k -> infinity, c = N-1.
    This function uses only the Virasoro T-line shadow constants at
    c = N-1.  It does not certify a higher-spin/CFT duality.

    Shadow data at c = N-1:
    - kappa_T = (N-1)/2
    - S4_T = 10/((N-1)(5(N-1)+22)) = 10/((N-1)(5N+17))
    - Delta_T = 40/(5N+17)
    - rho_T = sqrt((180(N-1)+872)/((5(N-1)+22)*(N-1)^2))
            = sqrt((180N+692)/((5N+17)*(N-1)^2))
            ~ 6/N for large N.

    The normalized entries are finite-N diagnostics of this scalar lane.
    """
    if N_values is None:
        N_values = list(range(2, 31))

    data = []
    for N in N_values:
        c_val = float(N - 1)
        if c_val <= 0:
            continue

        tower = shadow_tower_tline(c_val, max_arity)
        rho = _rho_tline(c_val)
        kap_total = float(anomaly_ratio(N)) * c_val

        normalized = {}
        for r in range(2, max_arity + 1):
            if r in tower:
                normalized[r] = tower[r] * N ** (r - 2)

        data.append({
            'N': N,
            'c': c_val,
            'kappa_T': c_val / 2.0,
            'kappa_total': kap_total,
            'rho_T': rho,
            'rho_times_N': rho * N if rho else None,
            'tower': tower,
            'normalized': normalized,
        })

    return {
        'limit': 'higher_spin_lambda_0',
        'data': data,
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        'analytic_certified': False,
    }


def higher_spin_delta_scaling(N_values: Optional[List[int]] = None) -> List[Dict]:
    r"""Scaling of the critical discriminant Delta in the higher-spin limit.

    Delta_T = 40/(5c+22) = 40/(5(N-1)+22) = 40/(5N+17)

    For large N on the T-line: Delta ~ 8/N.  This is a scalar
    Virasoro-channel diagnostic; it is not a statement about the full
    multi-channel W_infinity shadow metric.
    """
    if N_values is None:
        N_values = list(range(2, 51))

    results = []
    for N in N_values:
        c_val = float(N - 1)
        Delta = 40.0 / (5.0 * c_val + 22.0) if c_val > -22.0 / 5 else None

        results.append({
            'N': N,
            'c': c_val,
            'Delta': Delta,
            'Delta_times_N': Delta * N if Delta else None,
            'asymptotic_8_over_N': 8.0 / N,
        })

    return results


# ============================================================================
# 10.  Finite prefix compatibility diagnostics
# ============================================================================

def universal_shadow_projection(N_target: int, N_source: int,
                                c_val: float, max_arity: int = 8) -> Dict:
    r"""Compare finite scalar prefix data for W_{N_source} and W_{N_target}.

    At a fixed scalar central charge c, the T-line towers agree because
    both are the same Virasoro computation.  The kappa_s prefix also
    agrees formally.  This function does not certify an algebra map,
    a multi-channel OPE projection, or an inverse-limit object.
    """
    assert N_source > N_target >= 2

    tower_source = shadow_tower_tline(c_val, max_arity)
    tower_target = shadow_tower_tline(c_val, max_arity)

    # T-line prefixes match because both calls use the same Virasoro data.
    tline_match = True
    for r in range(2, max_arity + 1):
        if r in tower_source and r in tower_target:
            if abs(tower_source[r] - tower_target[r]) > 1e-12:
                tline_match = False
                break

    channels_source = wn_channel_data(N_source, c_val)
    channels_target = wn_channel_data(N_target, c_val)

    channel_match = True
    for i in range(N_target - 1):
        if abs(channels_source[i]['kappa'] - channels_target[i]['kappa']) > 1e-12:
            channel_match = False
            break

    return {
        'N_source': N_source,
        'N_target': N_target,
        'c': c_val,
        'tline_match': tline_match,
        'channel_match': channel_match,
        'projection_certified': False,
        'multi_channel_ope_certified': False,
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        'kappa_source': sum(ch['kappa'] for ch in channels_source),
        'kappa_target': sum(ch['kappa'] for ch in channels_target),
    }


def inverse_limit_consistency(c_val: float,
                              N_values: Optional[List[int]] = None,
                              max_arity: int = 8) -> Dict:
    r"""Check finite T-line compatibility across sampled N.

    For any two N values with the same c, the T-line towers are IDENTICAL.
    This is because the T-line only depends on c (Virasoro universality).

    This is a finite scalar compatibility check.  It does not certify
    a multi-channel inverse limit Theta_{W_infinity}.
    """
    if N_values is None:
        N_values = [3, 5, 7, 10, 15, 20]

    towers = {}
    kappas = {}
    for N in N_values:
        towers[N] = shadow_tower_tline(c_val, max_arity)
        kappas[N] = float(anomaly_ratio(N)) * c_val

    # Check all T-line towers agree
    ref = towers[N_values[0]]
    all_agree = True
    for N in N_values[1:]:
        for r in range(2, max_arity + 1):
            if r in ref and r in towers[N]:
                if abs(ref[r] - towers[N][r]) > 1e-12:
                    all_agree = False
                    break

    return {
        'c': c_val,
        'tline_all_agree': all_agree,
        'kappa_sequence': [(N, kappas[N]) for N in N_values],
        'kappa_growth': 'logarithmic',  # H_N ~ log(N)
        'tower': ref,
        'inverse_limit_certified': False,
        'multi_channel_ope_certified': False,
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
    }


# ============================================================================
# 11.  Normalized shadow coefficients for scalar scaling
# ============================================================================

def normalized_shadow_coefficients(N: int, c_val: float,
                                   max_arity: int = 10) -> Dict[int, float]:
    r"""Finite scalar normalizations of T-line shadow coefficients.

    Several normalization schemes:
    (a) S_r / kappa^{r/2}: a diagnostic rescaling
    (b) S_r * c^p with p = 0 for r <= 3 and p = r-2 for r >= 4
    (c) S_r * N^{r-2}: a lambda=0 diagnostic rescaling

    S_r(Vir) = [t^{r-2}] sqrt(Q(t)) / r, where Q is quadratic in t.
    The Taylor coefficients of sqrt(Q) at large c scale as:
    a_0 = c, a_1 = 6, a_2 = (9*4 + 16*(c/2)*10/(c*(5c+22)))/(2c)
    after subtracting a_1^2, so a_2 = 40/[c(5c+22)] and
    S_4 ~ 2/c^2.

    More generally, a_n ~ C_n / c^{n-1} for large c, so
    S_r = O(c^{-(r-2)}) for r >= 4 in this scalar recursion.
    """
    tower = shadow_tower_tline(c_val, max_arity)

    kap = c_val / 2.0
    result = {}
    for r in range(2, max_arity + 1):
        sr = tower.get(r, 0.0)
        c_power = 0 if r <= 3 else r - 2
        result[r] = {
            'raw': sr,
            'kappa_normalized': sr / abs(kap) ** (r / 2.0) if abs(kap) > 1e-100 else None,
            'c_power': c_power,
            'c_stripped': sr * c_val ** c_power if abs(c_val) > 1e-100 else None,
            'N_stripped': sr * N ** (r - 2),
        }

    return result


def large_c_asymptotics(max_arity: int = 10) -> Dict[int, float]:
    r"""Asymptotic shadow coefficients at large c (free-field/higher-spin limit).

    S_r(Vir_c) for c -> infinity:
    S_2 = c/2 ~ c/2
    S_3 = 2 (constant, independent of c)
    S_4 = 10/(c(5c+22)) ~ 2/c^2
    S_5 ~ -48/(5c^3)
    S_r = O(1/c^{r-2}) for r >= 4 in this scalar recursion

    These are large-c scalar asymptotics, not analytic planar
    partition-function coefficients.
    """
    c_values = [100.0, 500.0, 1000.0, 5000.0, 10000.0]
    asymp = {}

    for r in range(2, max_arity + 1):
        vals = []
        for c_val in c_values:
            tower = shadow_tower_tline(c_val, max_arity)
            sr = tower.get(r, 0.0)
            if r <= 3:
                vals.append(sr)
            else:
                vals.append(sr * c_val ** (r - 2))
        asymp[r] = vals[-1]

    return asymp


# ============================================================================
# 12.  Cross-verification infrastructure
# ============================================================================

def verify_anomaly_ratio_formula() -> Dict:
    """Cross-verify the anomaly ratio rho(N) = H_N - 1 against direct sum.

    Path 1: rho(N) = H_N - 1 (harmonic number formula).
    Path 2: rho(N) = sum_{s=2}^{N} 1/s (direct sum of channel weights).
    """
    results = {}
    for N in range(2, 21):
        path1 = anomaly_ratio(N)
        path2 = sum(Fraction(1, s) for s in range(2, N + 1))
        results[N] = {
            'path1': path1,
            'path2': path2,
            'match': path1 == path2,
        }
    return results


def verify_ff_duality_sum() -> Dict:
    """Verify the Freudenthal-de Vries c-sum under FF duality."""
    results = {}
    for N in [2, 3, 4, 5, 7, 10]:
        for k_val in [Fraction(1), Fraction(3), Fraction(5), Fraction(10)]:
            k_dual = ff_dual_level(N, k_val)
            c1 = c_WN(N, k_val)
            try:
                c2 = c_WN(N, k_dual)
            except ValueError:
                continue
            s = c1 + c2
            expected = ff_central_charge_sum(N)
            results[(N, k_val)] = {
                'c1': c1,
                'c2': c2,
                'sum': s,
                'expected': expected,
                'match': s == expected,
            }
    return results


def verify_koszul_conductor_consistency() -> Dict:
    r"""Verify the scalar identity kappa + kappa' = rho * K_N^c.

    This is a conductor identity on the finite scalar branch; it does not
    construct A^!, Omega(B(A)), or Z_ch^der(A).
    """
    results = {}
    for N in [2, 3, 4, 5]:
        K = ff_central_charge_sum(N)
        rho = anomaly_ratio(N)
        expected_sum = rho * Fraction(K)
        results[N] = {
            'K': K,
            'rho': rho,
            'kappa_sum': expected_sum,
            'kappa_sum_float': float(expected_sum),
            'constructs_dual_object': False,
        }
    return results


def verify_tline_universality(c_val: float = 10.0, max_arity: int = 8) -> Dict:
    r"""Cross-engine verification that the T-line shadow is INDEPENDENT of N.

    Imports t_line_tower_numerical from independent W_N shadow tower
    engines (N = 3, 5, 6, 7) and compares their output against this
    engine's shadow_tower_tline.

    The W_4 engine (w4_multivariable_shadow) is symbolic/multivariable and
    does not expose a numerical T-line tower; it is tested via its shadow
    data (kappa, alpha, S4) instead.

    Mathematical content: the T-line shadow uses kappa_T = c/2, alpha_T = 2,
    S4_T = 10/(c(5c+22)).  These are the Virasoro sub-contributions and are
    N-independent finite scalar data.
    """
    ref_tower = shadow_tower_tline(c_val, max_arity)

    engine_results = {}
    engines_tested = []
    engines_skipped = []
    all_match = True
    tol = 1e-10

    # --- Engine: w3_shadow_tower_engine ---
    try:
        from w3_shadow_tower_engine import (
            t_line_tower_numerical as w3_tower,
            t_line_shadow_data as w3_tline_data,
        )
        tower_w3 = w3_tower(c_val, max_arity)
        data_w3 = w3_tline_data(c_val)
        mismatches_w3 = {}
        for r in range(2, max_arity + 1):
            diff = abs(tower_w3.get(r, 0.0) - ref_tower.get(r, 0.0))
            if diff > tol:
                mismatches_w3[r] = diff
                all_match = False
        engine_results['W3'] = {
            'tower': tower_w3,
            'kappa': float(data_w3['kappa']),
            'alpha': float(data_w3['alpha']),
            'S4': float(data_w3['S4']),
            'mismatches': mismatches_w3,
            'match': len(mismatches_w3) == 0,
        }
        engines_tested.append('W3')
    except ImportError:
        engines_skipped.append('W3')

    # --- Engine: w5_shadow_tower ---
    try:
        from w5_shadow_tower import (
            t_line_tower_numerical as w5_tower,
            t_line_shadow_data as w5_tline_data,
        )
        tower_w5 = w5_tower(c_val, max_arity)
        data_w5 = w5_tline_data(c_val)
        mismatches_w5 = {}
        for r in range(2, max_arity + 1):
            diff = abs(tower_w5.get(r, 0.0) - ref_tower.get(r, 0.0))
            if diff > tol:
                mismatches_w5[r] = diff
                all_match = False
        engine_results['W5'] = {
            'tower': tower_w5,
            'kappa': float(data_w5['kappa']),
            'alpha': float(data_w5['alpha']),
            'S4': float(data_w5['S4']),
            'mismatches': mismatches_w5,
            'match': len(mismatches_w5) == 0,
        }
        engines_tested.append('W5')
    except ImportError:
        engines_skipped.append('W5')

    # --- Engine: w6_shadow_tower ---
    try:
        from w6_shadow_tower import (
            t_line_tower_numerical as w6_tower,
            t_line_shadow_data as w6_tline_data,
        )
        tower_w6 = w6_tower(c_val, max_arity)
        data_w6 = w6_tline_data(c_val)
        mismatches_w6 = {}
        for r in range(2, max_arity + 1):
            diff = abs(tower_w6.get(r, 0.0) - ref_tower.get(r, 0.0))
            if diff > tol:
                mismatches_w6[r] = diff
                all_match = False
        engine_results['W6'] = {
            'tower': tower_w6,
            'kappa': float(data_w6['kappa']),
            'alpha': float(data_w6['alpha']),
            'S4': float(data_w6['S4']),
            'mismatches': mismatches_w6,
            'match': len(mismatches_w6) == 0,
        }
        engines_tested.append('W6')
    except ImportError:
        engines_skipped.append('W6')

    # --- Engine: w7_shadow_tower ---
    try:
        from w7_shadow_tower import (
            t_line_tower_numerical as w7_tower,
            t_line_shadow_data as w7_tline_data,
        )
        tower_w7 = w7_tower(c_val, max_arity)
        data_w7 = w7_tline_data(c_val)
        mismatches_w7 = {}
        for r in range(2, max_arity + 1):
            diff = abs(tower_w7.get(r, 0.0) - ref_tower.get(r, 0.0))
            if diff > tol:
                mismatches_w7[r] = diff
                all_match = False
        engine_results['W7'] = {
            'tower': tower_w7,
            'kappa': float(data_w7['kappa']),
            'alpha': float(data_w7['alpha']),
            'S4': float(data_w7['S4']),
            'mismatches': mismatches_w7,
            'match': len(mismatches_w7) == 0,
        }
        engines_tested.append('W7')
    except ImportError:
        engines_skipped.append('W7')

    # --- Shadow data consistency: verify (kappa, alpha, S4) across engines ---
    data_consistent = True
    ref_kappa = c_val / 2.0
    ref_alpha = 2.0
    ref_S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    data_mismatches = {}
    for eng_name, eng_data in engine_results.items():
        for param in ('kappa', 'alpha', 'S4'):
            ref_param = {'kappa': ref_kappa, 'alpha': ref_alpha, 'S4': ref_S4}[param]
            if abs(eng_data[param] - ref_param) > tol:
                data_mismatches[(eng_name, param)] = (eng_data[param], ref_param)
                data_consistent = False

    return {
        'c': c_val,
        'tline_universal': all_match and data_consistent,
        'tower': ref_tower,
        'engines_tested': engines_tested,
        'engines_skipped': engines_skipped,
        'engine_results': engine_results,
        'data_consistent': data_consistent,
        'data_mismatches': data_mismatches,
        'num_engines_tested': len(engines_tested),
    }


def comprehensive_scaling_analysis(lam: float = 0.0,
                                   max_arity: int = 8) -> Dict[str, Any]:
    r"""Formal scalar large-N diagnostics at fixed 't Hooft coupling.

    Computes:
    1. Central charge scaling: c(N) vs N
    2. Total kappa scaling: kappa(N) vs N
    3. T-line rho scaling: rho(N) vs N
    4. T-line S_r scaling: S_r(N) vs N
    5. sampled coefficient tables
    """
    if lam == 0:
        N_values = list(range(2, 51))
    else:
        N_max = int(1.0 / lam)
        N_values = [n for n in range(2, min(N_max + 1, 51))]

    c_vs_N = []
    kappa_vs_N = []
    rho_vs_N = []
    sr_vs_N = {r: [] for r in range(2, max_arity + 1)}

    for N in N_values:
        c_val = thooft_c(N, lam)
        if c_val <= 0:
            continue

        c_vs_N.append((N, c_val))
        kappa_vs_N.append((N, thooft_kappa_total(N, lam)))

        rho = _rho_tline(c_val)
        if rho is not None:
            rho_vs_N.append((N, rho))

        try:
            tower = shadow_tower_tline(c_val, max_arity)
            for r in range(2, max_arity + 1):
                if r in tower and math.isfinite(tower[r]):
                    sr_vs_N[r].append((N, tower[r]))
        except (ValueError, ZeroDivisionError):
            continue

    # Extract large-N behavior for rho*N
    rho_N_limit = rho_vs_N[-1][1] * rho_vs_N[-1][0] if rho_vs_N else None

    return {
        'lambda': lam,
        'c_vs_N': c_vs_N,
        'kappa_vs_N': kappa_vs_N,
        'rho_vs_N': rho_vs_N,
        'sr_vs_N': sr_vs_N,
        'rho_times_N_limit': rho_N_limit,
        'claim_class': FORMAL_LIMIT_DIAGNOSTIC,
        'analytic_certified': False,
    }
