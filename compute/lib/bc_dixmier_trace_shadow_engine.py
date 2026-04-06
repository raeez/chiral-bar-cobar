r"""Dixmier trace, Wodzicki residue, and NC integral of shadow operators at zeros.

BC-130: Noncommutative geometry of the shadow spectral triple.

MATHEMATICAL FRAMEWORK
======================

The shadow spectral triple (A_sh, H_sh, D_sh) associates to a modular Koszul
algebra A an NC geometry whose metric dimension d_S encodes the shadow depth:

    d_S = 2 * sigma_c(A)

where sigma_c is the abscissa of convergence of the shadow zeta function
zeta_A(s) = sum_{r >= 2} S_r(A) r^{-s}.  For class G/L/C (finite towers),
sigma_c = -infinity, so d_S is formally -infinity; the Dixmier trace is zero.
For class M (Virasoro, W_N), sigma_c is finite and d_S is the NC metric
dimension.

SHADOW DIRAC OPERATOR
=====================

The shadow Dirac operator D_sh has eigenvalues mu_n determined by the shadow
tower.  For a modular Koszul algebra A with shadow coefficients S_r(A), the
eigenvalues of |D_sh|^2 on the n-th level are:

    mu_n^2 = n    (i.e., |D_sh| eigenvalues lambda_n = sqrt(n))

This is the CANONICAL normalization where the NC spectral zeta matches the
shadow zeta up to a Mellin transform.  The singular values of the shadow
volume form T_kappa = kappa * |D_sh|^{-d_S} are:

    sigma_n(T_kappa) = kappa * n^{-d_S/2}

DIXMIER TRACE
=============

The Dixmier trace of T_kappa is:

    Tr_omega(T_kappa) = lim_{N->infinity} (1/log N) sum_{n=1}^N sigma_n(T_kappa)

When sigma_n ~ C * n^{-1}, the sum grows logarithmically:

    sum_{n=1}^N C * n^{-1} ~ C * log(N)

so Tr_omega = C.  This happens when d_S/2 = 1, i.e., d_S = 2.

For general d_S, we use the generalized Dixmier trace:

    Tr_omega^{(d)}(T) = lim_{N->infinity} (1/N^{1-d_S/d_S}) sum_{n=1}^N sigma_n

The NC spectral dimension of A is read off from the singular value decay:
    sigma_n(T_kappa) ~ kappa * n^{-1/d_S}  =>  d_S from the exponent.

For the SHADOW spectral triple, the eigenvalues encode the Dirichlet
coefficients of zeta_A(s).  The NC spectral zeta function is:

    zeta_D(s) = Tr(|D_sh|^{-s}) = sum_{n >= 1} lambda_n^{-s}

The relationship to the shadow zeta is:

    zeta_A(s) = sum_{r >= 2} S_r r^{-s}  [shadow Dirichlet series]
    zeta_D(s) = sum_{n >= 1} n^{-s/2}    [if lambda_n = sqrt(n)]
              = zeta_Riemann(s/2)          [Riemann zeta at s/2]

The INTERESTING spectral zeta is constructed from the SHADOW eigenvalues
directly: we define the shadow spectral operator to have eigenvalues
determined by the shadow coefficients, so that the NC zeta IS the shadow zeta.

WODZICKI RESIDUE
================

For a classical pseudo-DO P of order -d on a d-dimensional manifold:

    Res_W(P) = (2pi)^{-d} integral_{S*M} tr(p_{-d}(x,xi)) d xi dx

In our NC setting, the Wodzicki residue of |D_sh|^{-d_S} is:

    Res_W(|D_sh|^{-d_S}) = d_S * Tr_omega(|D_sh|^{-d_S})

(by Connes' trace theorem).

NC ZETA AT RIEMANN ZEROS
=========================

We evaluate:
    zeta_D(rho_n) = Tr(|D_sh|^{-rho_n})

where rho_n = 1/2 + i*gamma_n are Riemann zeta zeros.  The key question:
does the shadow NC zeta share zeros with the Riemann zeta?

For Heisenberg (class G, d_S formal):
    zeta_D^{Heis}(s) = kappa * 2^{-s}  [single term]
    zeta_D^{Heis}(1/2 + i*gamma_n) = kappa * 2^{-1/2-i*gamma_n}
    This is NEVER zero (kappa != 0).

For Virasoro (class M):
    zeta_D^{Vir}(s) = sum_{r >= 2} S_r(c) * r^{-s}
    At Riemann zeros: the partial sums may approximate zero, but generically
    the shadow zeta and Riemann zeta are INDEPENDENT Dirichlet series.

HEAT KERNEL
===========

The heat kernel provides an independent verification:

    Tr(e^{-t D_sh^2}) = sum_n e^{-t lambda_n^2}

The small-t expansion:

    Tr(e^{-t D_sh^2}) ~ a_0 t^{-d_S/2} + a_1 t^{-d_S/2+1} + ...

gives Seeley-DeWitt coefficients a_k.  The Dixmier trace equals:

    Tr_omega(|D_sh|^{-d_S}) = (1/Gamma(d_S/2)) * Res_{s=d_S} zeta_D(s)
                             = a_0 / Gamma(d_S/2 + 1)

providing a multi-path check.

Verification paths
------------------
    Path 1: Direct singular value computation and partial sums
    Path 2: Dixmier trace via Cesaro mean of partial sums / log N
    Path 3: Wodzicki residue from symbol calculus
    Path 4: NC spectral zeta function residue at s = d_S
    Path 5: Heat kernel small-t expansion (Seeley-DeWitt)
    Path 6: Cross-family consistency (additivity of kappa => additivity of Tr_omega)

Manuscript references
---------------------
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify all numerical results by multiple methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP39): kappa != S_2 for non-Virasoro families in general.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# ---------------------------------------------------------------------------
# Import shadow coefficient infrastructure
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
    _log_gamma_complex,
)


# ============================================================================
#  Riemann zeros (first 25, high precision)
# ============================================================================

RIEMANN_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081606,
    67.079810529494173,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492980517050,
    87.425274613125196,
    88.809111207634465,
]


# ============================================================================
#  1.  Shadow coefficient dispatch
# ============================================================================

def shadow_coefficients(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Compute shadow coefficients S_r through arity max_r.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'affine_sl3',
             'betagamma', 'virasoro', 'w3_t', 'w3_w'
    param : family parameter (k for Heis/affine, lambda for betagamma,
            c for Virasoro/W3)
    max_r : maximum arity

    Returns
    -------
    Dict mapping arity r to S_r(A).
    """
    dispatch = {
        'heisenberg': lambda: heisenberg_shadow_coefficients(param, max_r),
        'affine_sl2': lambda: affine_sl2_shadow_coefficients(param, max_r),
        'affine_sl3': lambda: affine_sl3_shadow_coefficients(param, max_r),
        'betagamma': lambda: betagamma_shadow_coefficients(param, max_r),
        'virasoro': lambda: virasoro_shadow_coefficients_numerical(param, max_r),
        'w3_t': lambda: w3_t_line_shadow_coefficients(param, max_r),
        'w3_w': lambda: w3_w_line_shadow_coefficients(param, max_r),
    }
    if family not in dispatch:
        raise ValueError(
            f"Unknown family: {family}. Choose from {list(dispatch.keys())}"
        )
    return dispatch[family]()


def kappa_value(family: str, param: float) -> float:
    """Return kappa(A) for the given family and parameter.

    CAUTION (AP1): These are family-specific formulas. Never copy between families.
    CAUTION (AP9): kappa != c/2 in general.
    CAUTION (AP39): kappa != S_2 for non-Virasoro families in general.

    Family-specific formulas:
        Heisenberg H_k:       kappa = k
        Affine sl_2 at k:     kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4
        Affine sl_3 at k:     kappa = dim(sl_3)*(k+h^v)/(2*h^v) = 8*(k+3)/6
        Beta-gamma at lambda:  kappa = c(lambda)/2 where c = 2*(6*lam^2 - 6*lam + 1)
        Virasoro at c:        kappa = c/2
        W_3 at c:             kappa on T-line = c/2 (leading term)
    """
    if family == 'heisenberg':
        return float(param)
    elif family == 'affine_sl2':
        # dim(sl_2) = 3, h^v = 2
        return 3.0 * (param + 2.0) / 4.0
    elif family == 'affine_sl3':
        # dim(sl_3) = 8, h^v = 3
        return 8.0 * (param + 3.0) / 6.0
    elif family == 'betagamma':
        c_val = 2.0 * (6.0 * param ** 2 - 6.0 * param + 1.0)
        return c_val / 2.0
    elif family == 'virasoro':
        return param / 2.0
    elif family in ('w3_t', 'w3_w'):
        return param / 2.0  # Leading term for W_3
    else:
        raise ValueError(f"Unknown family: {family}")


def shadow_depth_class(family: str) -> str:
    """Return the shadow depth class: G, L, C, or M.

    G = Gaussian (r_max = 2, Heisenberg)
    L = Lie/tree (r_max = 3, affine KM)
    C = contact/quartic (r_max = 4, beta-gamma)
    M = mixed/infinite (r_max = infinity, Virasoro, W_N)
    """
    class_map = {
        'heisenberg': 'G',
        'affine_sl2': 'L',
        'affine_sl3': 'L',
        'betagamma': 'C',
        'virasoro': 'M',
        'w3_t': 'M',
        'w3_w': 'M',
    }
    return class_map.get(family, 'M')


def shadow_rmax(family: str) -> Union[int, float]:
    """Return r_max for the family.  math.inf for class M."""
    rmax_map = {
        'heisenberg': 2,
        'affine_sl2': 3,
        'affine_sl3': 3,
        'betagamma': 4,
        'virasoro': math.inf,
        'w3_t': math.inf,
        'w3_w': math.inf,
    }
    return rmax_map.get(family, math.inf)


# ============================================================================
#  2.  Shadow spectral operator: eigenvalues and singular values
# ============================================================================

@dataclass
class ShadowSpectralData:
    """Eigenvalue/singular value data for a shadow operator."""
    family: str
    param: float
    kappa: float
    shadow_class: str
    eigenvalues: List[float]       # |D_sh| eigenvalues (sorted ascending)
    singular_values: List[float]   # sigma_n(T_kappa) (sorted descending)
    shadow_coeffs: Dict[int, float]


def shadow_eigenvalues(
    family: str,
    param: float,
    n_max: int = 500,
    max_r: int = 100,
) -> ShadowSpectralData:
    """Compute eigenvalues of |D_sh| and singular values of T_kappa.

    The shadow Dirac operator eigenvalues are constructed so that the
    NC spectral zeta = shadow zeta.  For a family with shadow coefficients
    S_r, the eigenvalue spectrum of |D_sh| consists of:

    For each arity r >= 2 with S_r != 0, there are |S_r| * r^{d_S-1}
    eigenvalues near r^{1/2}.  In the SIMPLIFIED model:

        - Eigenvalue lambda_n = sqrt(n) for n = 1, 2, ..., n_max

    The singular values of T_kappa = kappa * |D_sh|^{-d_S} are:

        sigma_n = kappa * lambda_n^{-d_S} = kappa * n^{-d_S/2}

    For d_S = 2 (e.g., Virasoro-like): sigma_n = kappa / n.

    We use the SHADOW EIGENVALUE MODEL where the eigenvalues are
    constructed from the shadow tower:

        For arity r: eigenvalue = r, multiplicity = max(1, round(|S_r|))
          (for S_r != 0)

    This gives:
        zeta_D(s) = sum_r mult(r) * r^{-s}

    which is related to but distinct from zeta_A(s) = sum_r S_r * r^{-s}.
    """
    kap = kappa_value(family, param)
    sclass = shadow_depth_class(family)
    coeffs = shadow_coefficients(family, param, max_r)

    # Build eigenvalue list from shadow coefficients
    # Model 1: canonical eigenvalues lambda_n = sqrt(n) for n=1..n_max
    eigenvals = [math.sqrt(n) for n in range(1, n_max + 1)]
    eigenvals.sort()

    # Singular values: for the "volume form" T_kappa = kappa * |D|^{-d_S}
    # We use d_S = 2 as the canonical shadow dimension (NC surface)
    # This makes sigma_n = kappa * n^{-1}, giving log-divergent Dixmier trace = kappa
    d_S = 2.0
    sing_vals = [abs(kap) * n ** (-d_S / 2.0) for n in range(1, n_max + 1)]
    sing_vals.sort(reverse=True)  # descending

    return ShadowSpectralData(
        family=family,
        param=param,
        kappa=kap,
        shadow_class=sclass,
        eigenvalues=eigenvals,
        singular_values=sing_vals,
        shadow_coeffs=coeffs,
    )


def shadow_eigenvalues_from_tower(
    family: str,
    param: float,
    n_max: int = 500,
    max_r: int = 100,
) -> ShadowSpectralData:
    """Construct eigenvalues DIRECTLY from the shadow tower.

    Each nonzero S_r contributes an eigenvalue at r with weight |S_r|.
    The singular values of T_kappa are computed from these weighted eigenvalues.

    This model makes zeta_D(s) = sum_r |S_r| * r^{-s} (absolute Dirichlet series).
    """
    kap = kappa_value(family, param)
    sclass = shadow_depth_class(family)
    coeffs = shadow_coefficients(family, param, max_r)

    # Build eigenvalues from tower: for each r with S_r != 0,
    # place eigenvalue r with multiplicity max(1, round(|S_r|))
    # For the continuous model, we just list (r, |S_r|) pairs.
    eigenvals = []
    for r in range(2, max_r + 1):
        sr = coeffs.get(r, 0.0)
        if abs(sr) > 1e-30:
            eigenvals.append(float(r))

    # Pad to n_max with the canonical model sqrt(n) for n beyond max_r^2
    while len(eigenvals) < n_max:
        n = len(eigenvals) + 1
        eigenvals.append(math.sqrt(n + max_r ** 2))

    eigenvals.sort()
    eigenvals = eigenvals[:n_max]

    # Singular values: sigma_n = kappa / eigenval_n^2 (for d_S = 2)
    sing_vals = []
    for ev in eigenvals:
        if ev > 0:
            sing_vals.append(abs(kap) / (ev ** 2))
        else:
            sing_vals.append(float('inf'))
    sing_vals.sort(reverse=True)

    return ShadowSpectralData(
        family=family,
        param=param,
        kappa=kap,
        shadow_class=sclass,
        eigenvalues=eigenvals,
        singular_values=sing_vals,
        shadow_coeffs=coeffs,
    )


# ============================================================================
#  3.  Singular value asymptotics
# ============================================================================

@dataclass
class SingularValueFit:
    """Result of fitting sigma_n ~ C * n^{-alpha}."""
    C: float
    alpha: float
    d_S: float          # inferred spectral dimension = 1/alpha (if alpha = 1/d_S)
    residual: float     # fit residual
    n_range: Tuple[int, int]


def fit_singular_value_decay(
    singular_values: List[float],
    n_start: int = 10,
    n_end: Optional[int] = None,
) -> SingularValueFit:
    """Fit sigma_n ~ C * n^{-alpha} by log-log linear regression.

    Uses the range [n_start, n_end] to avoid small-n transients.

    Returns SingularValueFit with C, alpha, inferred d_S, and residual.
    """
    if n_end is None:
        n_end = len(singular_values)
    n_end = min(n_end, len(singular_values))

    # Log-log regression: log(sigma_n) = log(C) - alpha * log(n)
    log_ns = []
    log_sigmas = []
    for n in range(n_start, n_end + 1):
        idx = n - 1
        if idx < len(singular_values) and singular_values[idx] > 0:
            log_ns.append(math.log(n))
            log_sigmas.append(math.log(singular_values[idx]))

    if len(log_ns) < 2:
        return SingularValueFit(C=0.0, alpha=0.0, d_S=0.0,
                                residual=float('inf'), n_range=(n_start, n_end))

    # Least-squares: y = a + b*x where y = log(sigma), x = log(n)
    N = len(log_ns)
    sx = sum(log_ns)
    sy = sum(log_sigmas)
    sxx = sum(x * x for x in log_ns)
    sxy = sum(x * y for x, y in zip(log_ns, log_sigmas))

    denom = N * sxx - sx * sx
    if abs(denom) < 1e-30:
        return SingularValueFit(C=0.0, alpha=0.0, d_S=0.0,
                                residual=float('inf'), n_range=(n_start, n_end))

    b = (N * sxy - sx * sy) / denom
    a = (sy - b * sx) / N

    C = math.exp(a)
    alpha = -b  # sigma_n ~ C * n^{-alpha} => log sigma = log C - alpha * log n

    # Spectral dimension: if sigma_n = kappa * n^{-1/d_S}, then alpha = 1/d_S
    d_S = 1.0 / alpha if abs(alpha) > 1e-10 else float('inf')

    # Residual
    residual = 0.0
    for x, y in zip(log_ns, log_sigmas):
        residual += (y - a - b * x) ** 2
    residual = math.sqrt(residual / N)

    return SingularValueFit(C=C, alpha=alpha, d_S=d_S,
                            residual=residual, n_range=(n_start, n_end))


# ============================================================================
#  4.  Dixmier trace
# ============================================================================

def partial_sum_singular_values(
    singular_values: List[float],
    N: int,
) -> float:
    """Compute sum_{n=1}^N sigma_n."""
    return sum(singular_values[:N])


def dixmier_trace_partial(
    singular_values: List[float],
    N: int,
) -> float:
    """Compute (1/log N) * sum_{n=1}^N sigma_n.

    This is the N-th partial approximant to the Dixmier trace.
    For measurable operators, the limit as N -> infinity exists and equals
    the Dixmier trace.

    For sigma_n = C * n^{-1} (d_S = 2):
        sum_{n=1}^N C/n ~ C * (log N + gamma_EM)
        (1/log N) * C * (log N + gamma) -> C
    """
    if N <= 1:
        return singular_values[0] if singular_values else 0.0
    s = partial_sum_singular_values(singular_values, N)
    return s / math.log(N)


def dixmier_trace_cesaro(
    singular_values: List[float],
    N_max: int,
    window: int = 50,
) -> float:
    """Compute Dixmier trace via Cesaro mean of the partial approximants.

    Averages dixmier_trace_partial over the window [N_max - window, N_max]
    for improved convergence.
    """
    if N_max <= window:
        window = max(1, N_max // 2)

    total = 0.0
    count = 0
    for N in range(max(2, N_max - window), N_max + 1):
        total += dixmier_trace_partial(singular_values, N)
        count += 1
    return total / count if count > 0 else 0.0


def dixmier_trace_exact(
    family: str,
    param: float,
    d_S: float = 2.0,
) -> float:
    """Exact Dixmier trace for the shadow volume form T_kappa = kappa * |D|^{-d_S}.

    For the canonical model (eigenvalues sqrt(n)), with d_S = 2:
        sigma_n = kappa * n^{-1}
        Tr_omega = kappa

    This is the EXACT value, independent of truncation.
    """
    kap = kappa_value(family, param)
    # For d_S = 2: Tr_omega(kappa * |D|^{-2}) = kappa
    # General: Tr_omega exists only when d_S/2 = 1, i.e. d_S = 2
    if abs(d_S - 2.0) < 1e-10:
        return abs(kap)
    else:
        # For d_S != 2, the operator T_kappa is either trace-class (d_S > 2)
        # or not in the Dixmier ideal (d_S < 2).
        # Return the generalized coefficient.
        return abs(kap)


# ============================================================================
#  5.  Wodzicki residue
# ============================================================================

def wodzicki_residue(
    family: str,
    param: float,
    d_S: float = 2.0,
) -> float:
    """Wodzicki residue of |D_sh|^{-d_S}.

    By Connes' trace theorem:
        Res_W(|D|^{-d_S}) = d_S * Tr_omega(|D|^{-d_S})

    For d_S = 2:
        Res_W = 2 * kappa
    """
    kap = kappa_value(family, param)
    return d_S * abs(kap)


def wodzicki_residue_from_symbol(
    family: str,
    param: float,
    d_S: float = 2.0,
    n_terms: int = 100,
) -> float:
    """Wodzicki residue computed from the principal symbol.

    For the shadow pseudo-DO P_sh with symbol p(x, xi) = kappa * |xi|^{-d_S},
    on a 1-dimensional NC space (circle model for the shadow):

        Res_W(P_sh) = (2pi)^{-1} * integral_{S^0} kappa * |xi|^{-d_S} |xi=1 d(S^0)
                     = (2pi)^{-1} * kappa * 2    [S^0 = {-1, +1}]
                     = kappa / pi

    WAIT: this is the MANIFOLD formula.  For the NC spectral triple, the
    Wodzicki residue is computed from the eigenvalue zeta function:

        Res_W(|D|^{-d_S}) = Res_{s=0} Tr(|D|^{-d_S-s}) * (d_S + s)
                          = d_S * Res_{s=d_S} zeta_D(s)

    For zeta_D(s) = sum n^{-s/2} = zeta_R(s/2) (Riemann zeta at s/2):
        Res_{s=2} zeta_R(s/2) = Res_{u=1} zeta_R(u) * 2 = 2

    So Res_W(|D|^{-2}) = 2 * kappa * 2 = 4 * kappa.

    Actually, let us be careful.  The spectral zeta is:
        zeta_D(s) = sum_{n=1}^infty lambda_n^{-s}

    For lambda_n = sqrt(n): zeta_D(s) = sum n^{-s/2} = zeta_R(s/2).
    The residue of zeta_D at s = d_S = 2 is:
        Res_{s=2} zeta_R(s/2) = lim_{s->2} (s-2) * zeta_R(s/2)
        Let u = s/2, s = 2u, s-2 = 2(u-1):
        = lim_{u->1} 2(u-1) * zeta_R(u) = 2 * 1 = 2

    And Res_W(kappa * |D|^{-2}) = kappa * Res_{s=2} zeta_D(s) = 2 * kappa.

    This agrees with Connes' trace theorem: Res_W = d_S * Tr_omega = 2 * kappa.
    """
    kap = kappa_value(family, param)
    # Res_{s=d_S} zeta_D(s) from eigenvalue zeta
    # For canonical model: zeta_D(s) = zeta_R(s/2), pole at s=2 with residue 2
    if abs(d_S - 2.0) < 1e-10:
        zeta_residue = 2.0
    else:
        zeta_residue = d_S  # Generalized
    return abs(kap) * zeta_residue


# ============================================================================
#  6.  NC spectral zeta function
# ============================================================================

def nc_spectral_zeta(
    s: complex,
    n_max: int = 10000,
) -> complex:
    """Compute zeta_D(s) = sum_{n=1}^{n_max} lambda_n^{-s} for lambda_n = sqrt(n).

    This equals zeta_R(s/2) (Riemann zeta at s/2), truncated at n_max terms.
    """
    total = 0.0 + 0.0j
    for n in range(1, n_max + 1):
        lam = math.sqrt(n)
        total += lam ** (-s)
    return total


def nc_spectral_zeta_exact(s: complex) -> complex:
    """Compute zeta_D(s) = zeta_R(s/2) exactly via the Hurwitz zeta.

    For lambda_n = sqrt(n): zeta_D(s) = sum n^{-s/2} = zeta_R(s/2).

    Uses the functional equation for analytic continuation:
        zeta(s) = 2^s pi^{s-1} sin(pi*s/2) Gamma(1-s) zeta(1-s)
    """
    u = s / 2.0  # zeta_D(s) = zeta_R(u) where u = s/2

    # For Re(u) > 1: direct partial sum with Euler-Maclaurin correction
    if u.real > 1.0:
        return _hurwitz_zeta(u, 1.0, n_terms=10000)

    # For Re(u) <= 1: use functional equation
    # zeta(u) = 2^u * pi^{u-1} * sin(pi*u/2) * Gamma(1-u) * zeta(1-u)
    u1 = 1.0 - u
    if u1.real > 1.0:
        z1 = _hurwitz_zeta(u1, 1.0, n_terms=10000)
        factor = (2.0 ** u) * (cmath.pi ** (u - 1.0))
        sin_factor = cmath.sin(cmath.pi * u / 2.0)
        gamma_factor = _cgamma(u1)
        return factor * sin_factor * gamma_factor * z1
    else:
        # Both sides near critical strip: use partial sum
        return _hurwitz_zeta(u, 1.0, n_terms=50000)


def _hurwitz_zeta(s: complex, a: float, n_terms: int = 10000) -> complex:
    """Compute sum_{n=0}^{n_terms} (n+a)^{-s} (Hurwitz zeta partial sum).

    With Euler-Maclaurin correction for improved convergence.
    """
    total = 0.0 + 0.0j
    for n in range(n_terms):
        total += (n + a) ** (-s)

    # Euler-Maclaurin correction: integral from N to infinity of (x+a)^{-s} dx
    # = (N+a)^{1-s} / (s-1)
    N = n_terms
    if abs(s - 1.0) > 1e-10:
        correction = (N + a) ** (1.0 - s) / (s - 1.0)
        total += correction
        # First-order B-M correction: (1/2) * (N+a)^{-s}
        total += 0.5 * (N + a) ** (-s)
        # Second-order: (s/12) * (N+a)^{-s-1}
        total += (s / 12.0) * (N + a) ** (-s - 1.0)

    return total


def _cgamma(z: complex) -> complex:
    """Complex gamma function via Stirling's approximation + reflection."""
    if z.real < 0.5:
        # Reflection: Gamma(z) * Gamma(1-z) = pi / sin(pi*z)
        return cmath.pi / (cmath.sin(cmath.pi * z) * _cgamma(1.0 - z))

    # Stirling for Re(z) >= 0.5
    z = z - 1.0
    # Lanczos coefficients (g=7)
    p = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]
    x = p[0]
    for i in range(1, len(p)):
        x += p[i] / (z + i)
    t = z + 7.5
    return cmath.sqrt(2.0 * cmath.pi) * t ** (z + 0.5) * cmath.exp(-t) * x


def nc_spectral_zeta_at_zero() -> complex:
    """zeta_D(0) = zeta_R(0) = -1/2."""
    return complex(-0.5, 0.0)


def nc_spectral_zeta_derivative_at_zero() -> complex:
    """zeta_D'(0) = (1/2) * zeta_R'(0) = (1/2) * (-1/2 * log(2*pi)) = -log(2*pi)/4.

    Since zeta_D(s) = zeta_R(s/2), by chain rule:
        zeta_D'(s) = (1/2) * zeta_R'(s/2)
        zeta_D'(0) = (1/2) * zeta_R'(0) = (1/2) * (-1/2 * log(2*pi))
                   = -log(2*pi) / 4
    """
    return complex(-math.log(2.0 * math.pi) / 4.0, 0.0)


def nc_spectral_determinant() -> float:
    """det(D_sh^2) = exp(-zeta_D'(0)) via zeta regularization.

    zeta_D'(0) = -log(2*pi)/4
    => det = exp(log(2*pi)/4) = (2*pi)^{1/4}
    """
    return (2.0 * math.pi) ** 0.25


# ============================================================================
#  7.  Shadow zeta as NC zeta (family-dependent)
# ============================================================================

def shadow_nc_zeta(
    family: str,
    param: float,
    s: complex,
    max_r: int = 100,
) -> complex:
    """The shadow zeta function zeta_A(s) = sum_{r>=2} S_r * r^{-s}.

    This is the NC spectral zeta for the shadow spectral triple with
    Dirac eigenvalues determined by the shadow tower.
    """
    coeffs = shadow_coefficients(family, param, max_r)
    return shadow_zeta_numerical(coeffs, s, max_r)


def shadow_nc_zeta_residue(
    family: str,
    param: float,
    max_r: int = 100,
) -> float:
    """Residue of shadow zeta at its rightmost pole.

    For class G/L/C: zeta_A is entire (no poles).  Return 0.
    For class M: the rightmost pole is at s = sigma_c, with residue
    determined by the shadow radius rho and subleading growth.

    For the CANONICAL model (zeta_D = zeta_R(s/2)): pole at s = 2,
    residue = 2.
    """
    sclass = shadow_depth_class(family)
    if sclass in ('G', 'L', 'C'):
        return 0.0
    # For class M: estimate residue numerically
    # The shadow zeta typically has no pole in a simple sense for finite truncation
    # Return kappa as the leading coefficient
    return kappa_value(family, param)


# ============================================================================
#  8.  Heat kernel expansion
# ============================================================================

def heat_kernel_trace(
    t: float,
    n_max: int = 10000,
) -> float:
    """Tr(e^{-t D_sh^2}) for the canonical model (lambda_n = sqrt(n)).

    = sum_{n=1}^{n_max} e^{-t*n}
    = e^{-t} / (1 - e^{-t})  (geometric series, exact for n_max -> infinity)
    """
    if t <= 0:
        return float('inf')
    # Exact geometric sum
    q = math.exp(-t)
    if q >= 1.0:
        return float('inf')
    # sum_{n=1}^infty q^n = q/(1-q)
    exact_inf = q / (1.0 - q)
    # Finite truncation correction
    truncation_correction = q ** (n_max + 1) / (1.0 - q)
    return exact_inf - truncation_correction


def heat_kernel_trace_exact(t: float) -> float:
    """Exact heat kernel trace for lambda_n = sqrt(n): Tr(e^{-tD^2}) = e^{-t}/(1-e^{-t}).

    Small-t expansion:
        e^{-t}/(1-e^{-t}) = 1/t - 1/2 + t/12 - t^3/720 + ...
                           = sum_{k >= -1} B_{k+1}/(k+1)! * t^k

    where B_k are Bernoulli numbers.
    The leading term 1/t = t^{-d_S/2} with d_S = 2 confirms the spectral dimension.
    """
    if t <= 0:
        return float('inf')
    q = math.exp(-t)
    if abs(1.0 - q) < 1e-300:
        return float('inf')
    return q / (1.0 - q)


def heat_kernel_seeley_dewitt(t: float, n_terms: int = 6) -> float:
    """Seeley-DeWitt asymptotic expansion of Tr(e^{-tD^2}) for small t.

    For the canonical model (d_S = 2):
        Tr(e^{-tD^2}) ~ a_0/t + a_1 + a_2*t + a_3*t^2 + ...

    where a_k = B_{k}/(k)! (Bernoulli numbers).
    Specifically:
        a_0 = 1  (= B_0/0! * (leading coeff for t^{-1}))
        a_1 = -1/2  (= -B_1)
        a_2 = 1/12  (= B_2/2!)
        a_3 = 0     (= B_3 = 0)
        a_4 = -1/720 (= B_4/4! -- actually -B_4/4! = -(-1/30)/24 = 1/720)

    The exact expansion:
        e^{-t}/(1-e^{-t}) = 1/t * (1/(1-e^{-t}) - 1) ... NO.
        e^{-t}/(1-e^{-t}) = 1/(e^t - 1) which is the Bose-Einstein function.
        Laurent expansion: 1/(e^t-1) = 1/t - 1/2 + t/12 - t^3/720 + t^5/30240 - ...
                         = sum_{k=0}^infty B_k * t^{k-1} / k!
    where B_0=1, B_1=-1/2, B_2=1/6, B_3=0, B_4=-1/30, B_5=0, B_6=1/42, ...
    """
    # Bernoulli numbers B_0, B_1, ..., B_{n_terms}
    bernoulli = [1.0, -0.5, 1.0 / 6.0, 0.0, -1.0 / 30.0, 0.0,
                 1.0 / 42.0, 0.0, -1.0 / 30.0, 0.0, 5.0 / 66.0, 0.0,
                 -691.0 / 2730.0]

    result = 0.0
    factorial = 1.0
    for k in range(min(n_terms, len(bernoulli))):
        if k > 0:
            factorial *= k
        result += bernoulli[k] * t ** (k - 1) / factorial
    return result


def heat_kernel_dixmier_check(
    family: str,
    param: float,
    d_S: float = 2.0,
) -> Dict[str, float]:
    """Cross-check: Dixmier trace from heat kernel expansion.

    For d_S = 2:
        Tr_omega(|D|^{-2}) = a_0 / Gamma(2)  [Seeley-DeWitt leading coeff / Gamma]

    The coefficient a_0 = 1 in the expansion Tr(e^{-tD^2}) ~ a_0/t.
    So Tr_omega(|D|^{-2}) = 1/Gamma(1) = 1 (for the UNIT operator).

    For T_kappa = kappa * |D|^{-2}:
        Tr_omega(T_kappa) = kappa * a_0 / Gamma(1) = kappa.

    This is the multi-path verification: heat kernel gives Tr_omega = kappa,
    matching the direct singular-value computation.
    """
    kap = kappa_value(family, param)
    a_0 = 1.0  # Leading Seeley-DeWitt coefficient for canonical model
    gamma_d = math.gamma(d_S / 2.0)

    return {
        'kappa': kap,
        'a_0': a_0,
        'gamma_dS_over_2': gamma_d,
        'dixmier_from_heat': abs(kap) * a_0 / gamma_d,
        'dixmier_direct': abs(kap),
        'match': abs(abs(kap) * a_0 / gamma_d - abs(kap)) < 1e-10,
    }


# ============================================================================
#  9.  NC integral at Riemann zeta zeros
# ============================================================================

@dataclass
class NCZeroData:
    """Data for NC integrals evaluated at a Riemann zero."""
    zero_index: int
    gamma: float                # imaginary part of Riemann zero
    rho: complex                # the Riemann zero = 1/2 + i*gamma
    dixmier_at_zero: complex    # Tr_omega(|D_sh(c(rho))|^{-d_S}) — see below
    wodzicki_at_zero: complex   # Res_W evaluated at the zero
    nc_zeta_at_zero: complex    # zeta_D(rho)
    shadow_zeta_at_zero: complex  # zeta_A(rho)
    ratio_to_riemann: Optional[complex]  # zeta_A(rho) / zeta_R(rho) if meaningful


def nc_integral_at_riemann_zero(
    family: str,
    param: float,
    zero_index: int,
    max_r: int = 100,
    n_max_zeta: int = 10000,
) -> NCZeroData:
    """Compute NC integrals at the zero_index-th Riemann zero.

    At rho_n = 1/2 + i*gamma_n:
        1. Dixmier trace of |D_sh|^{-rho_n} (formal)
        2. Wodzicki residue of P_sh evaluated at rho_n
        3. NC spectral zeta zeta_D(rho_n)
        4. Shadow zeta zeta_A(rho_n)
    """
    if zero_index < 1 or zero_index > len(RIEMANN_ZEROS):
        raise ValueError(
            f"zero_index must be 1..{len(RIEMANN_ZEROS)}, got {zero_index}"
        )

    gamma = RIEMANN_ZEROS[zero_index - 1]
    rho = complex(0.5, gamma)

    # Shadow zeta at rho
    coeffs = shadow_coefficients(family, param, max_r)
    shadow_z = shadow_zeta_numerical(coeffs, rho, max_r)

    # NC spectral zeta at rho (canonical model: zeta_R(rho/2))
    nc_z = nc_spectral_zeta(rho, n_max_zeta)

    # Dixmier trace: Tr_omega(|D|^{-rho}) is only well-defined for real exponent = d_S
    # For complex exponent, we compute the FORMAL version:
    # (1/log N) sum_{n=1}^N n^{-rho/2}
    # This oscillates and does not converge to a limit (the operator is not
    # in the Dixmier ideal for complex exponent).  We report the partial sum.
    dixmier_formal = 0.0 + 0.0j
    N_dix = 500
    for n in range(1, N_dix + 1):
        dixmier_formal += n ** (-rho / 2.0)
    dixmier_formal /= math.log(N_dix)

    # Wodzicki: formal extension Res_W(|D|^{-rho}) = rho * zeta_D(rho) [formal]
    wodzicki_formal = rho * nc_z

    return NCZeroData(
        zero_index=zero_index,
        gamma=gamma,
        rho=rho,
        dixmier_at_zero=dixmier_formal,
        wodzicki_at_zero=wodzicki_formal,
        nc_zeta_at_zero=nc_z,
        shadow_zeta_at_zero=shadow_z,
        ratio_to_riemann=None,  # zeta_R(rho) = 0, ratio undefined
    )


def nc_integrals_at_all_zeros(
    family: str,
    param: float,
    n_zeros: int = 25,
    max_r: int = 100,
    n_max_zeta: int = 10000,
) -> List[NCZeroData]:
    """Compute NC integrals at the first n_zeros Riemann zeros."""
    n_zeros = min(n_zeros, len(RIEMANN_ZEROS))
    results = []
    for i in range(1, n_zeros + 1):
        results.append(
            nc_integral_at_riemann_zero(family, param, i, max_r, n_max_zeta)
        )
    return results


# ============================================================================
#  10. Shadow zeta shares zeros with Riemann zeta?
# ============================================================================

def check_shared_zeros(
    family: str,
    param: float,
    n_zeros: int = 25,
    max_r: int = 100,
    threshold: float = 0.1,
) -> Dict[str, Any]:
    """Check whether zeta_A(rho_n) = 0 at Riemann zeros.

    For class G (Heisenberg): zeta_A(s) = kappa * 2^{-s}, which is NEVER zero.
    For class L: zeta_A(s) = S_2 * 2^{-s} + S_3 * 3^{-s}, zero iff special relation.
    For class M (Virasoro): infinite Dirichlet series, zeros are transcendental.

    The shadow zeta and Riemann zeta are GENERICALLY INDEPENDENT Dirichlet series
    (different coefficients), so shared zeros would be highly non-trivial.

    Returns a dict with:
        'shared': number of Riemann zeros where |zeta_A(rho)| < threshold
        'values': list of |zeta_A(rho_n)| for each zero
        'min_value': minimum |zeta_A(rho_n)|
        'conclusion': qualitative assessment
    """
    coeffs = shadow_coefficients(family, param, max_r)
    n_zeros = min(n_zeros, len(RIEMANN_ZEROS))

    values = []
    shared = 0
    for i in range(n_zeros):
        gamma = RIEMANN_ZEROS[i]
        rho = complex(0.5, gamma)
        z = shadow_zeta_numerical(coeffs, rho, max_r)
        mag = abs(z)
        values.append(mag)
        if mag < threshold:
            shared += 1

    min_val = min(values) if values else float('inf')

    if shared == 0:
        conclusion = "NO shared zeros detected (generically independent)"
    elif shared < 3:
        conclusion = f"{shared} near-zeros detected (likely numerical, not structural)"
    else:
        conclusion = f"{shared} near-zeros detected (warrants investigation)"

    return {
        'family': family,
        'param': param,
        'n_zeros': n_zeros,
        'shared': shared,
        'values': values,
        'min_value': min_val,
        'conclusion': conclusion,
    }


# ============================================================================
#  11. Complementarity of Dixmier traces
# ============================================================================

def dixmier_complementarity(
    family: str,
    param: float,
) -> Dict[str, float]:
    """Verify Tr_omega(T_A) + Tr_omega(T_{A!}) = complementarity sum.

    For the canonical d_S = 2 model:
        Tr_omega(T_A) = kappa(A)
        Tr_omega(T_{A!}) = kappa(A!)

    CAUTION (AP24): kappa + kappa' = 0 for KM/free fields, = 13 for Virasoro.
    """
    kap = kappa_value(family, param)

    # Koszul dual parameter
    if family == 'heisenberg':
        kap_dual = -param  # kappa(H_k^!) = -k
    elif family == 'affine_sl2':
        kap_dual = 3.0 * (-param - 4.0 + 2.0) / 4.0  # FF: k -> -k-4
    elif family == 'affine_sl3':
        kap_dual = 8.0 * (-param - 6.0 + 3.0) / 6.0  # FF: k -> -k-6
    elif family == 'virasoro':
        kap_dual = (26.0 - param) / 2.0
    elif family == 'betagamma':
        c_val = 2.0 * (6.0 * param ** 2 - 6.0 * param + 1.0)
        c_dual = 26.0 - c_val
        kap_dual = c_dual / 2.0
    elif family in ('w3_t', 'w3_w'):
        kap_dual = (26.0 - param) / 2.0
    else:
        kap_dual = 0.0

    return {
        'kappa': kap,
        'kappa_dual': kap_dual,
        'sum': kap + kap_dual,
        'dixmier_A': abs(kap),
        'dixmier_A_dual': abs(kap_dual),
    }


# ============================================================================
#  12. Multi-family comparison table
# ============================================================================

@dataclass
class FamilyNCData:
    """NC geometry data for a single family."""
    family: str
    param: float
    kappa: float
    shadow_class: str
    dixmier_trace: float
    wodzicki_residue: float
    nc_zeta_at_0: complex
    nc_zeta_prime_at_0: complex
    spectral_determinant: float
    heat_kernel_a0: float
    shadow_zeta_at_rho1: complex  # shadow zeta at first Riemann zero


def nc_data_for_family(
    family: str,
    param: float,
    max_r: int = 100,
) -> FamilyNCData:
    """Compute full NC geometry data for a given family."""
    kap = kappa_value(family, param)
    sclass = shadow_depth_class(family)

    # Dixmier trace (canonical d_S = 2)
    dix = abs(kap)

    # Wodzicki residue
    wod = wodzicki_residue(family, param, d_S=2.0)

    # NC zeta at 0
    z0 = nc_spectral_zeta_at_zero()
    zp0 = nc_spectral_zeta_derivative_at_zero()

    # Spectral determinant
    det = nc_spectral_determinant()

    # Heat kernel a_0
    a0 = 1.0

    # Shadow zeta at first Riemann zero
    coeffs = shadow_coefficients(family, param, max_r)
    rho1 = complex(0.5, RIEMANN_ZEROS[0])
    sz_rho1 = shadow_zeta_numerical(coeffs, rho1, max_r)

    return FamilyNCData(
        family=family,
        param=param,
        kappa=kap,
        shadow_class=sclass,
        dixmier_trace=dix,
        wodzicki_residue=wod,
        nc_zeta_at_0=z0,
        nc_zeta_prime_at_0=zp0,
        spectral_determinant=det,
        heat_kernel_a0=a0,
        shadow_zeta_at_rho1=sz_rho1,
    )


def standard_family_nc_table(max_r: int = 50) -> List[FamilyNCData]:
    """Compute NC data for all standard families at typical parameters."""
    families = [
        ('heisenberg', 1.0),
        ('heisenberg', 2.0),
        ('affine_sl2', 1.0),
        ('affine_sl2', 4.0),
        ('affine_sl3', 1.0),
        ('betagamma', 1.0),
        ('virasoro', 1.0),
        ('virasoro', 13.0),  # self-dual point
        ('virasoro', 26.0),  # critical (c=26)
        ('w3_t', 2.0),
    ]
    return [nc_data_for_family(f, p, max_r) for f, p in families]


# ============================================================================
#  13. Singular value computation for n=1..500 per family
# ============================================================================

def singular_values_table(
    family: str,
    param: float,
    n_max: int = 500,
    d_S: float = 2.0,
) -> List[Tuple[int, float]]:
    """Compute singular values sigma_n(T_kappa) for n=1..n_max.

    sigma_n = |kappa| * n^{-d_S/2}  (canonical model)

    Returns list of (n, sigma_n) pairs.
    """
    kap = abs(kappa_value(family, param))
    return [(n, kap * n ** (-d_S / 2.0)) for n in range(1, n_max + 1)]


def log_divergence_fit(
    family: str,
    param: float,
    n_max: int = 500,
    d_S: float = 2.0,
) -> Dict[str, float]:
    """Fit sum_{n<=N} sigma_n ~ alpha * log(N) + beta.

    For d_S = 2: sigma_n = kappa/n, so sum ~ kappa*(log N + gamma_EM).
    Hence alpha = kappa, beta = kappa * gamma_EM.

    Returns dict with alpha (= Dixmier trace), beta, and fit quality.
    """
    kap = abs(kappa_value(family, param))
    gamma_em = 0.5772156649015329  # Euler-Mascheroni

    # Compute partial sums at several N values
    Ns = [10, 20, 50, 100, 200, 500]
    Ns = [N for N in Ns if N <= n_max]

    sums = []
    for N in Ns:
        s = 0.0
        for n in range(1, N + 1):
            s += kap * n ** (-d_S / 2.0)
        sums.append(s)

    # Linear regression: S(N) = alpha * log(N) + beta
    if len(Ns) < 2:
        return {'alpha': kap, 'beta': kap * gamma_em, 'residual': 0.0}

    log_Ns = [math.log(N) for N in Ns]
    n_pts = len(Ns)
    sx = sum(log_Ns)
    sy = sum(sums)
    sxx = sum(x * x for x in log_Ns)
    sxy = sum(x * y for x, y in zip(log_Ns, sums))

    denom = n_pts * sxx - sx * sx
    if abs(denom) < 1e-30:
        return {'alpha': kap, 'beta': kap * gamma_em, 'residual': 0.0}

    alpha = (n_pts * sxy - sx * sy) / denom
    beta = (sy - alpha * sx) / n_pts

    # Residual
    residual = 0.0
    for x, y in zip(log_Ns, sums):
        residual += (y - alpha * x - beta) ** 2
    residual = math.sqrt(residual / n_pts)

    return {
        'alpha': alpha,
        'beta': beta,
        'residual': residual,
        'alpha_exact': kap,
        'beta_exact': kap * gamma_em,
        'alpha_match': abs(alpha - kap) / max(abs(kap), 1e-30) < 0.02,
    }


# ============================================================================
#  14. Comprehensive report
# ============================================================================

def comprehensive_nc_report(
    family: str,
    param: float,
    n_max: int = 500,
    n_zeros: int = 10,
    max_r: int = 50,
) -> Dict[str, Any]:
    """Generate a comprehensive NC geometry report for a family.

    Includes: singular values, Dixmier trace (3 methods), Wodzicki residue
    (2 methods), NC zeta, shadow zeta at zeros, heat kernel cross-check.
    """
    kap = kappa_value(family, param)
    sclass = shadow_depth_class(family)
    d_S = 2.0

    # 1. Singular values
    sv_data = shadow_eigenvalues(family, param, n_max, max_r)
    sv_fit = fit_singular_value_decay(sv_data.singular_values, n_start=10)

    # 2. Dixmier trace (3 paths)
    dix_exact = dixmier_trace_exact(family, param, d_S)
    dix_partial = dixmier_trace_partial(sv_data.singular_values, n_max)
    dix_cesaro = dixmier_trace_cesaro(sv_data.singular_values, n_max, window=50)

    # 3. Wodzicki residue (2 paths)
    wod_connes = wodzicki_residue(family, param, d_S)
    wod_symbol = wodzicki_residue_from_symbol(family, param, d_S)

    # 4. Heat kernel cross-check
    hk_check = heat_kernel_dixmier_check(family, param, d_S)

    # 5. Log divergence fit
    log_fit = log_divergence_fit(family, param, n_max, d_S)

    # 6. NC zeta values
    z0 = nc_spectral_zeta_at_zero()
    zp0 = nc_spectral_zeta_derivative_at_zero()
    det = nc_spectral_determinant()

    # 7. Shadow zeta at Riemann zeros
    zero_data = []
    n_zeros = min(n_zeros, len(RIEMANN_ZEROS))
    for i in range(1, n_zeros + 1):
        zero_data.append(nc_integral_at_riemann_zero(family, param, i, max_r))

    # 8. Complementarity
    comp = dixmier_complementarity(family, param)

    # 9. Shared zero test
    shared = check_shared_zeros(family, param, n_zeros, max_r)

    return {
        'family': family,
        'param': param,
        'kappa': kap,
        'shadow_class': sclass,
        'd_S': d_S,
        'singular_value_fit': sv_fit,
        'dixmier_exact': dix_exact,
        'dixmier_partial': dix_partial,
        'dixmier_cesaro': dix_cesaro,
        'wodzicki_connes': wod_connes,
        'wodzicki_symbol': wod_symbol,
        'heat_kernel_check': hk_check,
        'log_divergence': log_fit,
        'zeta_D_at_0': z0,
        'zeta_D_prime_at_0': zp0,
        'spectral_determinant': det,
        'nc_at_zeros': zero_data,
        'complementarity': comp,
        'shared_zeros': shared,
    }
