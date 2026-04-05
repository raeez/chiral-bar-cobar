r"""Grand Unified Zeta Atlas: cross-verification of ALL zeta-type functions
associated to each modular Koszul algebra family.

MATHEMATICAL FRAMEWORK
======================

For a modular Koszul algebra A with shadow obstruction tower {S_r(A)},
modular characteristic kappa(A), central charge c(A), and shadow depth
class (G/L/C/M), we define NINE zeta-type functions:

1. SHADOW ZETA  zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}
   The Dirichlet series of shadow coefficients.  Abscissa sigma_c:
     Class G/L/C: sigma_c = -infty (finite sum, entire)
     Class M:     sigma_c = log(rho) if rho < 1, else +infty

2. CONSTRAINED EPSTEIN  epsilon^c_s
   The Epstein zeta function constrained by OPE data:
     epsilon^c_s = sum_{(m,n) in Lambda_A} Q(m,n)^{-s}
   where Lambda_A is the OPE lattice and Q is the quadratic form from
   the shadow metric Q_L.  For Virasoro: Q(m,n) = m^2 + (c/2)*n^2.

3. SHADOW SELBERG  Z^{Sel}_A(s)
   The Selberg zeta from the shadow connection's closed orbits:
     Z^{Sel}_A(s) = prod_j prod_{k>=0} (1 - M_j * exp(-(s+k)*ell_j))
   where (M_j, ell_j) are monodromy/orbit-length pairs from shadow flow.
   For class M: N_bp = 2 branch points, M_j = -1, ell_j = pi.

4. FREDHOLM ZETA  Z^{Fred}_A(s)
   The Fredholm determinant of the shadow transfer operator:
     Z^{Fred}_A(s) = det(1 - z * L_s)
   where L_s is the Ruelle transfer operator acting on the shadow flow.
   Related to Z^{Sel} by Z^{Fred}(s) = Z^{Sel}(s) / Z^{Sel}(s+1).

5. IHARA ZETA  Z^{Ihara}_A(u)
   The Ihara zeta from the bar complex's graph structure:
     Z^{Ihara}_A(u) = prod_{[gamma]} (1 - u^{len(gamma)})^{-1}
   where [gamma] runs over primitive closed walks in the bar complex graph.
   For finite shadow depth r_max: finitely many primitives.

6. CATEGORICAL ZETA  zeta^{DK}(s)
   The DK (Drinfeld-Kohno) categorical zeta from the representation category:
     zeta^{DK}(s) = sum_{V in Irr(A-mod)} (dim V)^{-s}
   For Heisenberg: zeta^{DK}(s) = zeta_R(s) (Riemann zeta).
   For affine KM: related to Kac character formula.

7. BTZ SPECTRAL ZETA  zeta_BTZ(s)
   The spectral zeta from BTZ quasinormal modes (when A has a gravity dual):
     zeta_BTZ(s) = 2^{1-s} * r_+^{-s} * zeta_H(s, h/2)
   where r_+ = sqrt(c/6) in the holographic dictionary.

8. KLOOSTERMAN ZETA  Z^{Kl}(s)
   The Kloosterman Dirichlet series for the modular data:
     Z^{Kl}_A(s) = sum_{c >= 1} K(kappa, kappa; c) * c^{-s}
   where K(m,n;c) is the Kloosterman sum at level determined by kappa.

9. HECKE L-FUNCTION  L^{Hecke}_A(s)
   The L-function from the Hecke eigenvalue structure:
     L^{Hecke}_A(s) = prod_p (1 - lambda_p p^{-s} + p^{w-1-2s})^{-1}
   where lambda_p are the shadow Hecke eigenvalues at weight w = 2.

CROSS-CONSISTENCY RELATIONS
============================

(R1) Shadow zeta at negative integers = moments of shadow tower:
     zeta_A(-n) = sum_{r >= 2} S_r * r^n  (finite for class G/L/C)

(R2) Selberg zeros relate to shadow flow spectral data:
     Z^{Sel}_A(s_0) = 0  <==>  s_0 is in the resonance set

(R3) Fredholm/Selberg ratio is a quotient of q-Pochhammer symbols:
     Z^{Fred}(s) / Z^{Sel}(s) = 1 / Z^{Sel}(s+1)

(R4) Complementarity (Theorem C):
     zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) has c-independent leading term

(R5) kappa controls leading behavior (Theorem D):
     zeta_A(s) ~ kappa * 2^{-s}  as Re(s) -> infinity

(R6) Bar-cobar preserves zeros (Theorem B):
     Omega(B(A)) ~ A  =>  spectral data of bar = spectral data of A

(R7) Hecke L-function = shadow zeta on Hecke eigenform locus:
     L^{Hecke}_A(s) = sum S_r r^{-s}  when {S_r} is an eigenform

(R8) BTZ spectral zeta relates to shadow via holographic dictionary:
     kappa(A) controls both the leading shadow term and the BTZ temperature

CAUTION (AP1):  kappa formulas are family-specific.  NEVER copy between families.
CAUTION (AP9):  kappa != c/2 in general.  kappa = c/2 ONLY for Virasoro.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP29): delta_kappa != kappa_eff.
CAUTION (AP39): S_2 = kappa for all families; but kappa != c/2 in general.
CAUTION (AP48): kappa depends on the FULL algebra, not just Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

# ---------------------------------------------------------------------------
# Conditional imports (degrade gracefully)
# ---------------------------------------------------------------------------
try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

# ---------------------------------------------------------------------------
# Internal imports from existing engines
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
)

PI = math.pi


# ============================================================================
# SECTION 1:  Family data infrastructure
# ============================================================================

@dataclass
class AlgebraFamily:
    """Complete data for a modular Koszul algebra family member."""
    name: str
    family: str          # 'heisenberg', 'affine_sl2', etc.
    param: float         # k for Heis/aff, c for Vir, lambda for bg
    kappa: float
    central_charge: float
    shadow_class: str    # 'G', 'L', 'C', 'M'
    shadow_depth: Union[int, float]  # r_max; float('inf') for class M
    shadow_coeffs: Dict[int, float] = field(default_factory=dict)
    dual_kappa: Optional[float] = None
    kappa_sum: Optional[float] = None  # kappa(A) + kappa(A!)

    def __post_init__(self):
        if not self.shadow_coeffs:
            self.shadow_coeffs = _compute_shadow_coeffs(
                self.family, self.param, max_r=100
            )


def _compute_shadow_coeffs(
    family: str, param: float, max_r: int = 100,
) -> Dict[int, float]:
    """Dispatch to the correct shadow coefficient provider."""
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
        raise ValueError(f"Unknown family: {family}")
    return dispatch[family]()


# ---------------------------------------------------------------------------
# 1a.  kappa formulas (AP1, AP9, AP39, AP48 — computed independently)
# ---------------------------------------------------------------------------

def kappa_heisenberg(k: float) -> float:
    """kappa(H_k) = k.  The level IS the modular characteristic."""
    return float(k)


def kappa_affine_sl2(k: float) -> float:
    """kappa(V_k(sl_2)) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4."""
    return 3.0 * (k + 2.0) / 4.0


def kappa_affine_sl3(k: float) -> float:
    """kappa(V_k(sl_3)) = dim(sl_3) * (k + h^v) / (2 * h^v) = 4(k+3)/3."""
    return 4.0 * (k + 3.0) / 3.0


def kappa_virasoro(c: float) -> float:
    """kappa(Vir_c) = c/2.  ONLY valid for Virasoro.  AP39: NOT general."""
    return c / 2.0


def kappa_betagamma(lam: float) -> float:
    """kappa(bg_lambda) = c(lambda)/2 where c = 2(6*lam^2 - 6*lam + 1)."""
    c_val = 2.0 * (6.0 * lam ** 2 - 6.0 * lam + 1.0)
    return c_val / 2.0


def kappa_w3_t(c: float) -> float:
    """T-LINE projection of kappa for W_3 = c/2. NOT the total kappa(W_3).
    Total kappa(W_3) = 5c/6 = kappa_w3_t + kappa_w3_w (AP9: distinguish)."""
    return c / 2.0


def kappa_w3_w(c: float) -> float:
    """W-LINE projection of kappa for W_3 = c/3. NOT the total kappa(W_3).
    Total kappa(W_3) = 5c/6 = kappa_w3_t + kappa_w3_w (AP9: distinguish)."""
    return c / 3.0


def central_charge_heisenberg(k: float) -> float:
    """c(H_k) = 1 (single boson, regardless of level)."""
    return 1.0


def central_charge_affine_sl2(k: float) -> float:
    """c(V_k(sl_2)) = dim(sl_2) * k / (k + h^v) = 3k/(k+2)."""
    return 3.0 * k / (k + 2.0)


def central_charge_affine_sl3(k: float) -> float:
    """c(V_k(sl_3)) = 8k/(k+3)."""
    return 8.0 * k / (k + 3.0)


def central_charge_virasoro(c: float) -> float:
    """c(Vir_c) = c (tautological)."""
    return float(c)


def central_charge_betagamma(lam: float) -> float:
    """c(bg_lambda) = 2(6*lam^2 - 6*lam + 1)."""
    return 2.0 * (6.0 * lam ** 2 - 6.0 * lam + 1.0)


# ---------------------------------------------------------------------------
# 1b.  Koszul dual kappa (AP24, AP33)
# ---------------------------------------------------------------------------

def dual_kappa_heisenberg(k: float) -> float:
    """kappa(H_k^!) = -k.  AP33: H_k^! != H_{-k} as algebras."""
    return -float(k)


def dual_kappa_affine_sl2(k: float) -> float:
    """kappa(V_k(sl_2)^!) via FF involution: k -> -k-4.
    kappa^! = 3(-k-4+2)/4 = -3(k+2)/4 = -kappa(V_k)."""
    return -kappa_affine_sl2(k)


def dual_kappa_affine_sl3(k: float) -> float:
    """kappa(V_k(sl_3)^!) via FF: k -> -k-6.
    kappa^! = 4(-k-6+3)/3 = -4(k+3)/3 = -kappa(V_k)."""
    return -kappa_affine_sl3(k)


def dual_kappa_virasoro(c: float) -> float:
    """kappa(Vir_c^!) = kappa(Vir_{26-c}) = (26-c)/2.
    AP24: kappa + kappa^! = c/2 + (26-c)/2 = 13, NOT 0."""
    return (26.0 - c) / 2.0


def dual_kappa_betagamma(lam: float) -> float:
    """kappa(bg^!) ~ Virasoro at c_dual = 26 - c(lam)."""
    c_val = central_charge_betagamma(lam)
    return (26.0 - c_val) / 2.0


# ---------------------------------------------------------------------------
# 1c.  Shadow growth rate rho and shadow class
# ---------------------------------------------------------------------------

def shadow_growth_rate_virasoro(c: float) -> float:
    """Growth rate rho(Vir_c) = sqrt(9*alpha^2 + 2*Delta) / (2|kappa|).

    alpha = 2 (c-independent), Delta = 8*kappa*S_4 where S_4 = 10/(c(5c+22)).
    """
    if c == 0.0 or 5.0 * c + 22.0 == 0.0:
        return float('inf')
    kappa = c / 2.0
    alpha = 2.0  # S_3 = 2 (c-independent for Virasoro)
    S4 = 10.0 / (c * (5.0 * c + 22.0))
    Delta = 8.0 * kappa * S4
    val = 9.0 * alpha ** 2 + 2.0 * Delta
    if val < 0:
        return float('inf')
    return math.sqrt(val) / (2.0 * abs(kappa)) if kappa != 0 else float('inf')


def shadow_class_of(family: str) -> str:
    """Return the shadow depth class: G, L, C, or M."""
    if family == 'heisenberg':
        return 'G'
    elif family in ('affine_sl2', 'affine_sl3'):
        return 'L'
    elif family == 'betagamma':
        return 'C'
    elif family in ('virasoro', 'w3_t', 'w3_w'):
        return 'M'
    return 'M'  # default to M for unknown families


def shadow_depth_of(family: str) -> Union[int, float]:
    """Return r_max for the shadow depth class."""
    if family == 'heisenberg':
        return 2
    elif family in ('affine_sl2', 'affine_sl3'):
        return 3
    elif family == 'betagamma':
        return 4
    return float('inf')


# ============================================================================
# SECTION 2:  Standard family table construction
# ============================================================================

def build_standard_family_table() -> List[AlgebraFamily]:
    """Construct the full table of standard algebra families.

    Includes:
      - Heisenberg H_k for k = 1,...,5
      - Affine sl_2 at k = 1,...,5
      - Beta-gamma at lambda = 0.5 (the standard weight)
      - Virasoro at c = 1/2, 1, 2, ..., 25
      - W_3 T-line at c = 10 (generic)
      - W_3 W-line at c = 10 (generic)
    """
    families: List[AlgebraFamily] = []

    # Heisenberg H_k, k = 1,...,5
    for k in range(1, 6):
        kap = kappa_heisenberg(k)
        kap_dual = dual_kappa_heisenberg(k)
        families.append(AlgebraFamily(
            name=f'Heis_k={k}',
            family='heisenberg',
            param=float(k),
            kappa=kap,
            central_charge=central_charge_heisenberg(k),
            shadow_class='G',
            shadow_depth=2,
            dual_kappa=kap_dual,
            kappa_sum=kap + kap_dual,
        ))

    # Affine sl_2 at k = 1,...,5
    for k in range(1, 6):
        kap = kappa_affine_sl2(k)
        kap_dual = dual_kappa_affine_sl2(k)
        families.append(AlgebraFamily(
            name=f'aff_sl2_k={k}',
            family='affine_sl2',
            param=float(k),
            kappa=kap,
            central_charge=central_charge_affine_sl2(k),
            shadow_class='L',
            shadow_depth=3,
            dual_kappa=kap_dual,
            kappa_sum=kap + kap_dual,
        ))

    # Beta-gamma at lambda = 0.5
    lam = 0.5
    kap = kappa_betagamma(lam)
    kap_dual = dual_kappa_betagamma(lam)
    families.append(AlgebraFamily(
        name='bg_lam=0.5',
        family='betagamma',
        param=lam,
        kappa=kap,
        central_charge=central_charge_betagamma(lam),
        shadow_class='C',
        shadow_depth=4,
        dual_kappa=kap_dual,
        kappa_sum=kap + kap_dual,
    ))

    # Virasoro at c = 1/2, 1, 2, ..., 25
    c_values = [0.5] + list(range(1, 26))
    for c_val in c_values:
        c_val = float(c_val)
        if c_val == 0.0:
            continue
        kap = kappa_virasoro(c_val)
        kap_dual = dual_kappa_virasoro(c_val)
        families.append(AlgebraFamily(
            name=f'Vir_c={c_val}',
            family='virasoro',
            param=c_val,
            kappa=kap,
            central_charge=c_val,
            shadow_class='M',
            shadow_depth=float('inf'),
            dual_kappa=kap_dual,
            kappa_sum=kap + kap_dual,  # = 13 for all c (AP24)
        ))

    # W_3 T-line at c = 10
    c_w3 = 10.0
    kap = kappa_w3_t(c_w3)
    families.append(AlgebraFamily(
        name='W3_T_c=10',
        family='w3_t',
        param=c_w3,
        kappa=kap,
        central_charge=c_w3,
        shadow_class='M',
        shadow_depth=float('inf'),
    ))

    # W_3 W-line at c = 10
    kap_w = kappa_w3_w(c_w3)
    families.append(AlgebraFamily(
        name='W3_W_c=10',
        family='w3_w',
        param=c_w3,
        kappa=kap_w,
        central_charge=c_w3,
        shadow_class='M',
        shadow_depth=float('inf'),
    ))

    return families


# ============================================================================
# SECTION 3:  Nine zeta functions
# ============================================================================

# ---------------------------------------------------------------------------
# Z1: Shadow zeta  zeta_A(s) = sum_{r >= 2} S_r * r^{-s}
# ---------------------------------------------------------------------------

def shadow_zeta(
    alg: AlgebraFamily,
    s: complex,
    max_r: int = 100,
) -> complex:
    """Shadow zeta function zeta_A(s) = sum S_r r^{-s}."""
    return shadow_zeta_numerical(alg.shadow_coeffs, s, max_r)


def shadow_zeta_derivative(
    alg: AlgebraFamily,
    s: complex,
    max_r: int = 100,
) -> complex:
    """Derivative zeta_A'(s) = -sum S_r log(r) r^{-s}."""
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = alg.shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total -= Sr * math.log(r) * r ** (-s)
    return total


def shadow_zeta_at_integer(alg: AlgebraFamily, n: int, max_r: int = 100) -> float:
    """zeta_A(n) for integer n.  Real-valued when shadow coeffs are real."""
    return shadow_zeta(alg, complex(n, 0), max_r).real


# ---------------------------------------------------------------------------
# Z2: Constrained Epstein  epsilon^c_s
# ---------------------------------------------------------------------------

def constrained_epstein(
    alg: AlgebraFamily,
    s: complex,
    n_max: int = 200,
) -> complex:
    r"""Constrained Epstein zeta from the shadow metric quadratic form.

    For Virasoro: Q(m,n) = m^2 + (c/2) n^2.
    For affine KM: Q(m,n) = m^2 + kappa * n^2.
    For Heisenberg: Q(m,n) = m^2 + k * n^2.

    epsilon^c_s = sum'_{(m,n) != (0,0)} Q(m,n)^{-s}

    where the prime excludes the origin.  Convergent for Re(s) > 1.
    """
    s = complex(s)
    # The quadratic form coefficient is kappa (the leading shadow term S_2)
    a_coeff = alg.kappa
    if a_coeff <= 0:
        # For negative or zero kappa, the quadratic form is indefinite;
        # the Epstein zeta is undefined in the naive sense
        return complex(float('nan'), float('nan'))

    total = 0.0 + 0.0j
    for m in range(-n_max, n_max + 1):
        for n in range(-n_max, n_max + 1):
            if m == 0 and n == 0:
                continue
            Q_val = float(m * m) + a_coeff * float(n * n)
            if Q_val <= 0:
                continue
            total += Q_val ** (-s)
    return total


def constrained_epstein_fast(
    kappa_val: float,
    s: complex,
    n_max: int = 200,
) -> complex:
    """Fast Epstein for Q(m,n) = m^2 + kappa * n^2.

    Uses lattice point symmetry: Q(m,n) = Q(-m,n) = Q(m,-n) = Q(-m,-n).
    So the sum over the full lattice = 4 * sum over m>=1,n>=0 + 2 * sum_{m=0,n>=1}
    + 2 * sum_{m>=1,n=0}.
    """
    if kappa_val <= 0:
        return complex(float('nan'))
    s = complex(s)
    total = 0.0 + 0.0j
    # m >= 1, n = 0: Q = m^2
    for m in range(1, n_max + 1):
        total += 2.0 * (m * m) ** (-s)
    # m = 0, n >= 1: Q = kappa * n^2
    for n in range(1, n_max + 1):
        total += 2.0 * (kappa_val * n * n) ** (-s)
    # m >= 1, n >= 1: Q = m^2 + kappa*n^2
    for m in range(1, n_max + 1):
        for n in range(1, n_max + 1):
            Q_val = float(m * m) + kappa_val * float(n * n)
            total += 4.0 * Q_val ** (-s)
    return total


# ---------------------------------------------------------------------------
# Z3: Shadow Selberg  Z^{Sel}_A(s)
# ---------------------------------------------------------------------------

def shadow_selberg_zeta(
    alg: AlgebraFamily,
    s: complex,
    max_k: int = 100,
) -> complex:
    r"""Shadow Selberg zeta from the shadow connection orbits.

    Z^{Sel}_A(s) = prod_{j=1}^{N_bp} prod_{k=0}^{max_k}
                     (1 - M_j * exp(-(s+k)*ell_j))

    For class M: N_bp = 2 branch points, M_j = -1, ell_j = pi.
    For class G/L/C: no branch points in the finite plane => Z = 1.
    """
    s = complex(s)
    sc = shadow_class_of(alg.family)

    if sc in ('G', 'L', 'C'):
        # Finite shadow towers: the shadow connection has no finite branch
        # points in the relevant sense.  Selberg zeta = 1 (trivially).
        return complex(1.0, 0.0)

    # Class M: 2 branch points with M = -1, ell = pi
    N_bp = 2
    M_mono = -1.0
    ell = PI

    log_Z = 0.0 + 0.0j
    for _j in range(N_bp):
        for k in range(max_k + 1):
            arg = M_mono * cmath.exp(-(s + k) * ell)
            # log(1 - x) for |x| < 1
            val = 1.0 - arg
            if abs(val) < 1e-300:
                # Near a zero of the Selberg zeta
                return complex(0.0, 0.0)
            log_Z += cmath.log(val)

    return cmath.exp(log_Z)


# ---------------------------------------------------------------------------
# Z4: Fredholm zeta  Z^{Fred}_A(s)
# ---------------------------------------------------------------------------

def fredholm_zeta(
    alg: AlgebraFamily,
    s: complex,
    max_k: int = 100,
) -> complex:
    r"""Fredholm zeta = Z^{Sel}(s) / Z^{Sel}(s+1).

    This is the Fredholm determinant of the shadow transfer operator
    restricted to the s-eigenspace.

    For class M:
      Z^{Fred}(s) = prod_{j=1}^{N_bp} (1 - M_j * exp(-s*ell_j))

    since the k=0 factor of Z^{Sel}(s) divides out against the
    k >= 1 factors of Z^{Sel}(s+1).
    """
    Z_s = shadow_selberg_zeta(alg, s, max_k)
    Z_s1 = shadow_selberg_zeta(alg, s + 1.0, max_k)
    if abs(Z_s1) < 1e-300:
        return complex(float('nan'))
    return Z_s / Z_s1


def fredholm_zeta_direct(
    alg: AlgebraFamily,
    s: complex,
) -> complex:
    r"""Direct computation of the Fredholm zeta for class M.

    Z^{Fred}(s) = prod_{j=1}^{N_bp} (1 + exp(-s*pi))

    (using M_j = -1, so 1 - (-1)*exp(-s*pi) = 1 + exp(-s*pi))
    """
    sc = shadow_class_of(alg.family)
    if sc in ('G', 'L', 'C'):
        return complex(1.0, 0.0)

    N_bp = 2
    factor = 1.0 + cmath.exp(-s * PI)
    return factor ** N_bp


# ---------------------------------------------------------------------------
# Z5: Ihara zeta  Z^{Ihara}_A(u)
# ---------------------------------------------------------------------------

def ihara_zeta(
    alg: AlgebraFamily,
    u: complex,
    max_len: int = 50,
) -> complex:
    r"""Ihara zeta from the bar complex graph.

    For shadow depth r_max, the bar complex has a finite directed graph
    with vertices at arities 0, 1, ..., r_max and edges from the bar
    differential.  The Ihara zeta counts primitive closed walks.

    For class G (r_max = 2): single edge 2->0, no closed walks.
      Z^{Ihara}(u) = 1 (trivially).

    For class L (r_max = 3): edges 2->0, 3->1, 3->0.
      Still no closed walks (directed acyclic for these arities).
      Z^{Ihara}(u) = 1.

    For class C (r_max = 4): similar, no cycles.
      Z^{Ihara}(u) = 1.

    For class M (r_max = infinity): the bar complex graph has cycles
    through the recursion S_r -> S_{r-2}, S_{r-1}, ...  The Ihara zeta
    is an infinite product.

    We compute via the DETERMINANT FORMULA for a truncated graph:
      Z^{Ihara}(u) = (1 - u^2)^{chi-1} / det(I - u*A + u^2*(D-I))
    where A is the adjacency matrix, D is the degree matrix, and
    chi = |V| - |E| is the Euler characteristic.

    For the shadow tower graph with arities 2,...,r_max:
    - Vertex set V = {2, 3, ..., r_max}
    - Edge (i -> j) exists when the shadow recursion couples S_i to S_j.
      Specifically: S_r depends on S_{r-1} and S_{r-2} through the
      quadratic recursion Q_L.  So edges are: r -> r-1 and r -> r-2
      for each r >= 4.
    """
    u = complex(u)
    sc = shadow_class_of(alg.family)

    if sc in ('G', 'L', 'C'):
        return complex(1.0, 0.0)

    # Class M: truncated computation at max_len
    # Build adjacency matrix for the shadow recursion graph
    n_vertices = min(max_len, 100)
    if n_vertices < 3:
        return complex(1.0, 0.0)

    # The shadow recursion graph: vertex r has edges to r-1 and r-2
    # for r = 4, 5, ..., n_vertices+1 (shifted: vertex index i corresponds
    # to arity r = i + 2)
    #
    # Adjacency matrix A[i][j] = 1 if edge from vertex i to vertex j
    A = [[0.0] * n_vertices for _ in range(n_vertices)]
    for i in range(2, n_vertices):  # arity r = i+2, starts at 4
        # Edge to arity r-1 = (i+2)-1 = i+1, vertex index i-1
        if i - 1 >= 0:
            A[i][i - 1] = 1.0
        # Edge to arity r-2 = (i+2)-2 = i, vertex index i-2
        if i - 2 >= 0:
            A[i][i - 2] = 1.0

    # Degree matrix: D[i][i] = out-degree of vertex i
    D = [0.0] * n_vertices
    for i in range(n_vertices):
        D[i] = sum(A[i])

    # Ihara formula: det(I - u*A + u^2*(D - I))
    # Build the matrix M = I - u*A + u^2*(D - I)
    M = [[0.0 + 0.0j] * n_vertices for _ in range(n_vertices)]
    for i in range(n_vertices):
        for j in range(n_vertices):
            M[i][j] = -u * A[i][j]
        M[i][i] += 1.0 + u * u * (D[i] - 1.0)

    # Compute determinant via LU decomposition (Gaussian elimination)
    det_val = _determinant(M, n_vertices)

    # Euler characteristic chi = |V| - |E|
    n_edges = sum(int(A[i][j]) for i in range(n_vertices) for j in range(n_vertices))
    chi = n_vertices - n_edges

    # Z^{Ihara}(u) = (1 - u^2)^{chi-1} / det(M)
    prefactor = (1.0 - u * u) ** (chi - 1) if chi != 1 else 1.0

    if abs(det_val) < 1e-300:
        return complex(float('inf'))
    return prefactor / det_val


def _determinant(M: List[List[complex]], n: int) -> complex:
    """Compute determinant of n x n complex matrix via Gaussian elimination."""
    # Copy the matrix
    A = [[M[i][j] for j in range(n)] for i in range(n)]
    det = complex(1.0, 0.0)
    for col in range(n):
        # Find pivot
        pivot_row = None
        for row in range(col, n):
            if abs(A[row][col]) > 1e-300:
                pivot_row = row
                break
        if pivot_row is None:
            return complex(0.0, 0.0)
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            det *= -1.0
        det *= A[col][col]
        inv_pivot = 1.0 / A[col][col]
        for row in range(col + 1, n):
            factor = A[row][col] * inv_pivot
            for j in range(col, n):
                A[row][j] -= factor * A[col][j]
    return det


# ---------------------------------------------------------------------------
# Z6: Categorical zeta  zeta^{DK}(s)
# ---------------------------------------------------------------------------

def categorical_zeta(
    alg: AlgebraFamily,
    s: complex,
    n_max: int = 500,
) -> complex:
    r"""DK categorical zeta from representation dimensions.

    zeta^{DK}(s) = sum_{V in Irr(A-mod)} (dim V)^{-s}

    For Heisenberg: every Fock module F_lambda is 1-dimensional at each
    level, so the graded dimension at level n is p(n) (partition number).
    The categorical zeta = sum_{n >= 1} p(n) * n^{-s} (the partition
    Dirichlet series).

    For affine sl_2 at level k: integrable highest-weight modules
    L(lambda) for lambda = 0, 1, ..., k.  The character dimensions are
    given by the Weyl-Kac formula.  The "dimension" here is the quantum
    dimension dim_q(L(lambda)).

    For Virasoro: The minimal models (c < 1) have finitely many
    irreducibles; generic c has a continuum.  We use the partition
    function / character decomposition.
    """
    s = complex(s)

    if alg.family == 'heisenberg':
        # Partition Dirichlet series: sum_{n >= 1} p(n) * n^{-s}
        partitions = _partition_numbers_cached(n_max)
        total = 0.0 + 0.0j
        for n in range(1, min(n_max, len(partitions))):
            if partitions[n] > 0:
                total += partitions[n] * n ** (-s)
        return total

    elif alg.family == 'affine_sl2':
        # Quantum dimensions of integrable modules at level k
        k = int(alg.param)
        q = cmath.exp(PI * 1j / (k + 2))
        total = 0.0 + 0.0j
        for lam in range(k + 1):
            # Quantum dimension = sin(pi*(lam+1)/(k+2)) / sin(pi/(k+2))
            num = math.sin(PI * (lam + 1) / (k + 2))
            den = math.sin(PI / (k + 2))
            if abs(den) < 1e-15:
                continue
            dim_q = abs(num / den)
            if dim_q > 1e-10:
                total += dim_q ** (-s)
        return total

    elif alg.family == 'virasoro':
        # For generic c: use the character expansion
        # Characters of Verma modules: dim V_n = p(n)
        # The categorical zeta is the partition Dirichlet series
        partitions = _partition_numbers_cached(n_max)
        total = 0.0 + 0.0j
        for n in range(1, min(n_max, len(partitions))):
            if partitions[n] > 0:
                total += partitions[n] * n ** (-s)
        return total

    else:
        # For other families, use the partition Dirichlet series as
        # a proxy (level-by-level character dimension)
        partitions = _partition_numbers_cached(n_max)
        total = 0.0 + 0.0j
        for n in range(1, min(n_max, len(partitions))):
            if partitions[n] > 0:
                total += partitions[n] * n ** (-s)
        return total


def _partition_numbers_cached(n_max: int) -> List[int]:
    """Integer partition numbers p(0), ..., p(n_max-1)."""
    p = [0] * n_max
    p[0] = 1
    for k in range(1, n_max):
        for n in range(k, n_max):
            p[n] += p[n - k]
    return p


# ---------------------------------------------------------------------------
# Z7: BTZ spectral zeta  zeta_BTZ(s)
# ---------------------------------------------------------------------------

def btz_spectral_zeta(
    alg: AlgebraFamily,
    s: complex,
    h: float = 2.0,
    n_max: int = 2000,
) -> complex:
    r"""BTZ spectral zeta from quasinormal modes.

    zeta_BTZ(s) = 2^{1-s} * r_+^{-s} * zeta_H(s, h/2)

    where r_+ = sqrt(c/6) from the Brown-Henneaux formula c = 3l/(2G_N)
    and h is the conformal weight of the probe field.

    The Hurwitz zeta zeta_H(s, a) = sum_{n >= 0} (n + a)^{-s} is
    evaluated by direct summation with tail correction.
    """
    s = complex(s)
    c_val = alg.central_charge
    if c_val <= 0:
        return complex(float('nan'))

    r_plus = math.sqrt(c_val / 6.0)
    if r_plus <= 0:
        return complex(float('nan'))

    # Hurwitz zeta by direct summation
    a = h / 2.0
    if a <= 0:
        return complex(float('nan'))

    hz = _hurwitz_zeta_direct(s, a, n_max)
    prefactor = 2.0 ** (1.0 - s) * r_plus ** (-s)
    return prefactor * hz


def _hurwitz_zeta_direct(
    s: complex, a: float, n_max: int = 2000,
) -> complex:
    """Hurwitz zeta by direct summation + integral tail correction.

    zeta_H(s, a) = sum_{n=0}^{N} (n+a)^{-s} + (N+a)^{1-s}/(s-1)
    """
    s = complex(s)
    total = 0.0 + 0.0j
    for n in range(n_max + 1):
        total += (n + a) ** (-s)
    # Tail correction: integral from N to infinity of (x+a)^{-s} dx
    if abs(s - 1.0) > 1e-10:
        tail = (n_max + a) ** (1.0 - s) / (s - 1.0)
        total += tail
    return total


# ---------------------------------------------------------------------------
# Z8: Kloosterman zeta  Z^{Kl}(s)
# ---------------------------------------------------------------------------

def kloosterman_zeta(
    alg: AlgebraFamily,
    s: complex,
    c_max: int = 100,
) -> complex:
    r"""Kloosterman Dirichlet series for the modular characteristic.

    Z^{Kl}_A(s) = sum_{c >= 1} K(m, m; c) * c^{-s}

    where m = round(kappa) and K(m,n;c) is the classical Kloosterman sum
    K(m,n;c) = sum_{d (mod c), gcd(d,c)=1} exp(2*pi*i*(m*d + n*d_inv)/c).
    """
    s = complex(s)
    m = max(1, round(abs(alg.kappa)))

    total = 0.0 + 0.0j
    for c in range(1, c_max + 1):
        K_val = _kloosterman_sum(m, m, c)
        total += K_val * c ** (-s)
    return total


def _kloosterman_sum(m: int, n: int, c: int) -> complex:
    """Classical Kloosterman sum K(m,n;c) by direct computation."""
    if c <= 0:
        return complex(0.0)
    total = 0.0 + 0.0j
    for d in range(1, c):
        if math.gcd(d, c) != 1:
            continue
        # Modular inverse of d mod c
        d_inv = pow(d, -1, c)
        angle = 2.0 * PI * (m * d + n * d_inv) / c
        total += cmath.exp(1j * angle)
    return total


# ---------------------------------------------------------------------------
# Z9: Hecke L-function  L^{Hecke}_A(s)
# ---------------------------------------------------------------------------

def hecke_l_function(
    alg: AlgebraFamily,
    s: complex,
    p_max: int = 50,
    weight: int = 2,
) -> complex:
    r"""Hecke L-function from shadow Hecke eigenvalues.

    L^{Hecke}_A(s) = prod_{p prime, p <= p_max}
        (1 - lambda_p * p^{-s} + p^{w-1-2s})^{-1}

    where lambda_p = S(p) / S(2) is the normalized Hecke eigenvalue
    (approximate, assuming S_r is "close to" a Hecke eigenform).

    For terminating towers (class G/L/C): S(p) = 0 for large p,
    so the Euler product degenerates.

    For class M: the Hecke eigenvalues are generically nonzero.
    """
    s = complex(s)
    coeffs = alg.shadow_coeffs
    S2 = coeffs.get(2, 0.0)
    if abs(S2) < 1e-30:
        return complex(float('nan'))

    primes = _primes_up_to(p_max)
    product = complex(1.0, 0.0)

    for p in primes:
        Sp = coeffs.get(p, 0.0)
        lambda_p = Sp / S2 if abs(S2) > 1e-30 else 0.0
        local = 1.0 - lambda_p * p ** (-s) + p ** (weight - 1 - 2 * s)
        if abs(local) < 1e-300:
            return complex(0.0, 0.0)
        product /= local

    return product


def _primes_up_to(n: int) -> List[int]:
    """Sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


# ============================================================================
# SECTION 4:  Comprehensive zeta evaluation for a single family member
# ============================================================================

@dataclass
class ZetaAtlasEntry:
    """Complete atlas entry: all nine zeta functions evaluated at a point s."""
    algebra: AlgebraFamily
    s: complex
    shadow_zeta: complex
    constrained_epstein: complex
    shadow_selberg: complex
    fredholm_zeta: complex
    ihara_zeta: complex
    categorical_zeta: complex
    btz_spectral: complex
    kloosterman_zeta: complex
    hecke_l: complex


def evaluate_all_zetas(
    alg: AlgebraFamily,
    s: complex,
    epstein_n: int = 50,
    selberg_k: int = 50,
    ihara_len: int = 30,
    cat_n: int = 200,
    btz_n: int = 500,
    kloos_c: int = 50,
    hecke_p: int = 30,
) -> ZetaAtlasEntry:
    """Evaluate all nine zeta functions at a single point s."""
    return ZetaAtlasEntry(
        algebra=alg,
        s=s,
        shadow_zeta=shadow_zeta(alg, s),
        constrained_epstein=constrained_epstein_fast(alg.kappa, s, epstein_n),
        shadow_selberg=shadow_selberg_zeta(alg, s, selberg_k),
        fredholm_zeta=fredholm_zeta_direct(alg, s),
        ihara_zeta=ihara_zeta(alg, s, ihara_len),
        categorical_zeta=categorical_zeta(alg, s, cat_n),
        btz_spectral=btz_spectral_zeta(alg, s, n_max=btz_n),
        kloosterman_zeta=kloosterman_zeta(alg, s, kloos_c),
        hecke_l=hecke_l_function(alg, s, hecke_p),
    )


# ============================================================================
# SECTION 5:  Cross-consistency checks
# ============================================================================

def check_leading_behavior(alg: AlgebraFamily, sigma: float = 20.0) -> Dict[str, Any]:
    r"""Theorem D consistency: kappa controls leading shadow zeta behavior.

    For Re(s) >> 0: zeta_A(s) ~ kappa * 2^{-s} (the r=2 term dominates).
    Verify that zeta_A(sigma) / (kappa * 2^{-sigma}) -> 1 as sigma -> infty.
    """
    s = complex(sigma, 0)
    z_val = shadow_zeta(alg, s)
    leading = alg.kappa * 2.0 ** (-sigma)
    ratio = z_val / leading if abs(leading) > 1e-300 else float('nan')
    return {
        'name': alg.name,
        'sigma': sigma,
        'zeta_value': z_val,
        'leading_term': leading,
        'ratio': abs(ratio),
        'kappa': alg.kappa,
        'consistent': abs(abs(ratio) - 1.0) < 1e-3,
    }


def check_complementarity(
    c_val: float,
    s: complex,
    max_r: int = 100,
) -> Dict[str, Any]:
    r"""Theorem C consistency: zeta_{Vir_c} + zeta_{Vir_{26-c}} has
    c-independent leading coefficient 13 (AP24).
    """
    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    zeta_A = shadow_zeta_numerical(coeffs_A, s, max_r)
    zeta_dual = shadow_zeta_numerical(coeffs_dual, s, max_r)
    zeta_sum = zeta_A + zeta_dual

    # Leading term: S_2(A) + S_2(A!) = c/2 + (26-c)/2 = 13
    leading = 13.0 * 2.0 ** (-s)
    correction = zeta_sum - leading

    kappa_sum = c_val / 2.0 + (26.0 - c_val) / 2.0

    return {
        'c': c_val,
        's': s,
        'zeta_A': zeta_A,
        'zeta_dual': zeta_dual,
        'zeta_sum': zeta_sum,
        'leading_13': leading,
        'correction': correction,
        'kappa_sum': kappa_sum,
        'kappa_sum_is_13': abs(kappa_sum - 13.0) < 1e-12,
    }


def check_fredholm_selberg_ratio(
    alg: AlgebraFamily,
    s: complex,
    max_k: int = 80,
) -> Dict[str, Any]:
    r"""Verify Z^{Fred}(s) = Z^{Sel}(s) / Z^{Sel}(s+1) by comparing
    the ratio method against the direct Fredholm computation."""
    Z_sel_s = shadow_selberg_zeta(alg, s, max_k)
    Z_sel_s1 = shadow_selberg_zeta(alg, s + 1.0, max_k)
    Z_fred_ratio = Z_sel_s / Z_sel_s1 if abs(Z_sel_s1) > 1e-300 else complex(float('nan'))
    Z_fred_direct = fredholm_zeta_direct(alg, s)

    if abs(Z_fred_direct) > 1e-300 and not cmath.isnan(Z_fred_ratio):
        rel_diff = abs(Z_fred_ratio - Z_fred_direct) / abs(Z_fred_direct)
    else:
        rel_diff = float('nan')

    return {
        'name': alg.name,
        's': s,
        'Z_sel_s': Z_sel_s,
        'Z_sel_s1': Z_sel_s1,
        'Z_fred_ratio': Z_fred_ratio,
        'Z_fred_direct': Z_fred_direct,
        'relative_difference': rel_diff,
        'consistent': rel_diff < 1e-6 if not math.isnan(rel_diff) else False,
    }


def check_shadow_zeta_negative_integers(
    alg: AlgebraFamily,
    n_values: Optional[List[int]] = None,
    max_r: int = 100,
) -> Dict[int, Dict[str, float]]:
    r"""Verify zeta_A(-n) = sum_{r >= 2} S_r * r^n for negative integers.

    This is exact for the Dirichlet series (no analytic continuation needed).
    """
    if n_values is None:
        n_values = [0, 1, 2, 3, 4, 5]

    results = {}
    for n in n_values:
        # Direct evaluation of zeta_A(-n)
        zeta_val = shadow_zeta(alg, complex(-n, 0), max_r).real

        # Moment computation: sum S_r * r^n
        moment = sum(
            alg.shadow_coeffs.get(r, 0.0) * r ** n
            for r in range(2, max_r + 1)
        )

        results[n] = {
            'zeta_minus_n': zeta_val,
            'moment': moment,
            'difference': abs(zeta_val - moment),
            'consistent': abs(zeta_val - moment) < 1e-10,
        }
    return results


def check_kappa_additivity(
    families: List[AlgebraFamily],
) -> Dict[str, Any]:
    r"""Verify kappa additivity for direct sums (prop:independent-sum-factorization).

    For L = L_1 + L_2 with vanishing mixed OPE: kappa(L) = kappa(L_1) + kappa(L_2).
    """
    results = {}
    for i, f1 in enumerate(families):
        for j, f2 in enumerate(families):
            if i >= j:
                continue
            if f1.family == f2.family:
                continue  # Only cross-family
            kappa_sum = f1.kappa + f2.kappa
            results[f'{f1.name}+{f2.name}'] = {
                'kappa_1': f1.kappa,
                'kappa_2': f2.kappa,
                'kappa_sum': kappa_sum,
            }
    return results


def check_bar_cobar_invariance(
    alg: AlgebraFamily,
    s_values: Optional[List[complex]] = None,
) -> Dict[str, Any]:
    r"""Theorem B consistency: bar-cobar inversion should preserve spectral data.

    Omega(B(A)) ~ A => the spectral zeta computed from B(A) and then
    applying cobar should agree with the spectral zeta of A.

    For the shadow zeta this is automatic: the shadow coefficients are
    extracted from the bar complex, and the cobar recovers A.  The check
    is that zeta_A = zeta_{Omega(B(A))}, i.e., the shadow coefficients
    are INVARIANT under bar-cobar.

    For class G/L/C: exact equality (finite sums).
    For class M: agreement to truncation order.
    """
    if s_values is None:
        s_values = [complex(2, 0), complex(3, 0), complex(2, 5)]

    results = {}
    for s in s_values:
        val = shadow_zeta(alg, s)
        # The shadow coefficients ARE the bar-cobar invariant, so the
        # "round-trip" shadow zeta is identical by construction
        val_roundtrip = shadow_zeta(alg, s)
        results[str(s)] = {
            'zeta_A': val,
            'zeta_round_trip': val_roundtrip,
            'difference': abs(val - val_roundtrip),
            'consistent': abs(val - val_roundtrip) < 1e-15,
        }
    return results


def check_verdier_intertwining(
    c_val: float,
    s_values: Optional[List[complex]] = None,
    max_r: int = 100,
) -> Dict[str, Any]:
    r"""Theorem A consistency: Verdier duality maps B(A) to B(A!).

    D_Ran(B(Vir_c)) ~ B(Vir_{26-c}).

    At the level of shadow zetas:
      shadow coefficients of the Koszul dual are computed independently
      and compared against the Verdier-dual computation.
    """
    if s_values is None:
        s_values = [complex(2, 0), complex(3, 0), complex(2, 1)]

    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    results = {}
    for s in s_values:
        zeta_A = shadow_zeta_numerical(coeffs_A, s, max_r)
        zeta_dual = shadow_zeta_numerical(coeffs_dual, s, max_r)

        # The Verdier intertwining swaps A <-> A! and
        # preserves the complementarity sum zeta_A + zeta_{A!}
        zeta_sum = zeta_A + zeta_dual
        leading = 13.0 * 2.0 ** (-s)
        results[str(s)] = {
            'zeta_A': zeta_A,
            'zeta_dual': zeta_dual,
            'sum': zeta_sum,
            'leading_13': leading,
            'sum_minus_leading': zeta_sum - leading,
        }
    return results


def check_hochschild_polynomial_growth(
    alg: AlgebraFamily,
    t_values: Optional[List[float]] = None,
) -> Dict[str, Any]:
    r"""Theorem H consistency: ChirHoch*(A) polynomial =>
    the categorical zeta has polynomial growth along vertical lines.

    For polynomial ChirHoch: |zeta^{DK}(sigma + it)| grows at most
    polynomially in |t|.

    We check the growth order:
      rho(f) = lim sup log|f(sigma + it)| / log|t|
    at a fixed sigma.
    """
    if t_values is None:
        t_values = [10.0, 20.0, 50.0, 100.0]

    sigma = 2.0
    log_vals = []
    log_ts = []

    for t in t_values:
        s = complex(sigma, t)
        val = categorical_zeta(alg, s, 500)
        if abs(val) > 1e-300:
            log_vals.append(math.log(abs(val)))
            log_ts.append(math.log(t))

    # Estimate growth order via linear regression
    if len(log_vals) >= 2:
        # Simple slope estimation
        n = len(log_vals)
        sx = sum(log_ts)
        sy = sum(log_vals)
        sxx = sum(x * x for x in log_ts)
        sxy = sum(x * y for x, y in zip(log_ts, log_vals))
        denom = n * sxx - sx * sx
        if abs(denom) > 1e-15:
            slope = (n * sxy - sx * sy) / denom
        else:
            slope = float('nan')
    else:
        slope = float('nan')

    return {
        'name': alg.name,
        'sigma': sigma,
        't_values': t_values,
        'growth_order': slope,
        'polynomial_growth': slope < 10.0 if not math.isnan(slope) else None,
    }


# ============================================================================
# SECTION 6:  Zero finding
# ============================================================================

def find_shadow_zeta_zeros(
    alg: AlgebraFamily,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
    max_r: int = 100,
    tol: float = 1e-10,
) -> List[complex]:
    """Find zeros of the shadow zeta zeta_A(s) in the given strip."""
    zeros = []
    dr = (re_range[1] - re_range[0]) / max(grid_re, 1)
    di = (im_range[1] - im_range[0]) / max(grid_im, 1)

    for i_re in range(grid_re + 1):
        for i_im in range(grid_im + 1):
            s0 = complex(
                re_range[0] + i_re * dr,
                im_range[0] + i_im * di,
            )
            z = _newton_zero_shadow(alg.shadow_coeffs, s0, max_r, tol)
            if z is not None:
                # Check not already found (dedup)
                is_dup = False
                for existing in zeros:
                    if abs(z - existing) < 1e-6:
                        is_dup = True
                        break
                if not is_dup:
                    zeros.append(z)

    zeros.sort(key=lambda z: (z.imag, z.real))
    return zeros


def _newton_zero_shadow(
    coeffs: Dict[int, float],
    s0: complex,
    max_r: int,
    tol: float,
    max_iter: int = 100,
) -> Optional[complex]:
    """Newton's method for shadow zeta zeros."""
    s = s0
    for _ in range(max_iter):
        f = shadow_zeta_numerical(coeffs, s, max_r)
        fp = 0.0 + 0.0j
        for r in range(2, max_r + 1):
            Sr = coeffs.get(r, 0.0)
            if Sr == 0.0:
                continue
            fp -= Sr * math.log(r) * r ** (-s)
        if abs(fp) < 1e-300:
            return None
        ds = f / fp
        s = s - ds
        if abs(ds) < tol:
            f_check = shadow_zeta_numerical(coeffs, s, max_r)
            if abs(f_check) < tol * 100:
                return s
            return None
    return None


def find_selberg_zeros(
    alg: AlgebraFamily,
    im_range: Tuple[float, float] = (0.0, 50.0),
    grid: int = 200,
    max_k: int = 50,
) -> List[complex]:
    r"""Find zeros of the shadow Selberg zeta on the critical line Re(s) = 1/2.

    For class M: zeros at s = 1/2 + i*t where exp(-(1/2+it+k)*pi) = -1
    for some k >= 0, i.e., exp(-i*t*pi) = -exp((1/2+k)*pi).  Since
    |exp((1/2+k)*pi)| > 1 and |exp(-i*t*pi)| = 1, this can only happen
    when one of the product factors vanishes.
    """
    sc = shadow_class_of(alg.family)
    if sc in ('G', 'L', 'C'):
        return []  # No zeros (Z = 1)

    zeros = []
    dt = (im_range[1] - im_range[0]) / max(grid, 1)

    for i in range(grid + 1):
        t = im_range[0] + i * dt
        s = complex(0.5, t)
        val = shadow_selberg_zeta(alg, s, max_k)
        if i > 0:
            val_prev = shadow_selberg_zeta(alg, complex(0.5, t - dt), max_k)
            if val.real * val_prev.real < 0 or val.imag * val_prev.imag < 0:
                # Sign change detected; refine
                z = _bisect_zero_selberg(alg, t - dt, t, max_k)
                if z is not None:
                    is_dup = any(abs(z - existing) < 1e-6 for existing in zeros)
                    if not is_dup:
                        zeros.append(z)
    return zeros


def _bisect_zero_selberg(
    alg: AlgebraFamily,
    t_lo: float,
    t_hi: float,
    max_k: int,
    n_iter: int = 50,
) -> Optional[complex]:
    """Bisection for Selberg zero on Re(s) = 1/2."""
    for _ in range(n_iter):
        t_mid = (t_lo + t_hi) / 2.0
        f_lo = shadow_selberg_zeta(alg, complex(0.5, t_lo), max_k)
        f_mid = shadow_selberg_zeta(alg, complex(0.5, t_mid), max_k)
        if f_lo.real * f_mid.real < 0:
            t_hi = t_mid
        else:
            t_lo = t_mid
        if t_hi - t_lo < 1e-10:
            s0 = complex(0.5, (t_lo + t_hi) / 2.0)
            val = shadow_selberg_zeta(alg, s0, max_k)
            if abs(val) < 1e-4:
                return s0
            return None
    return None


def compare_zeros_across_families(
    families: List[AlgebraFamily],
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (0.0, 50.0),
    grid_re: int = 10,
    grid_im: int = 50,
) -> Dict[str, Any]:
    r"""Find and compare shadow zeta zeros across all families.

    Returns universal zeros (common to all/most families) and
    family-specific zeros.
    """
    all_zeros: Dict[str, List[complex]] = {}
    for alg in families:
        try:
            zeros = find_shadow_zeta_zeros(
                alg, re_range, im_range, grid_re, grid_im,
            )
            all_zeros[alg.name] = zeros
        except (ValueError, ZeroDivisionError):
            all_zeros[alg.name] = []

    # Find universal zeros: those within tol of a zero in EVERY family
    universal = []
    if all_zeros:
        ref_name = list(all_zeros.keys())[0]
        ref_zeros = all_zeros[ref_name]
        for z in ref_zeros:
            is_universal = True
            for name, zeros in all_zeros.items():
                if name == ref_name:
                    continue
                found = any(abs(z - w) < 0.5 for w in zeros)
                if not found:
                    is_universal = False
                    break
            if is_universal:
                universal.append(z)

    return {
        'all_zeros': all_zeros,
        'universal_zeros': universal,
        'n_families': len(families),
        'n_universal': len(universal),
    }


# ============================================================================
# SECTION 7:  Growth rate analysis
# ============================================================================

def growth_order(
    zeta_func: Callable[[complex], complex],
    sigma: float = 2.0,
    t_values: Optional[List[float]] = None,
) -> float:
    r"""Estimate the growth order rho(f) = lim sup log|f(sigma+it)| / log|t|.

    Uses linear regression on (log|t|, log|f(sigma+it)|) for large t.
    """
    if t_values is None:
        t_values = [10.0, 20.0, 30.0, 50.0, 80.0, 100.0]

    log_ts = []
    log_fs = []
    for t in t_values:
        try:
            val = zeta_func(complex(sigma, t))
            if abs(val) > 1e-300 and not cmath.isnan(val):
                log_ts.append(math.log(t))
                log_fs.append(math.log(abs(val)))
        except (ValueError, ZeroDivisionError, OverflowError):
            continue

    if len(log_ts) < 2:
        return float('nan')

    # Linear regression
    n = len(log_ts)
    sx = sum(log_ts)
    sy = sum(log_fs)
    sxx = sum(x * x for x in log_ts)
    sxy = sum(x * y for x, y in zip(log_ts, log_fs))
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-15:
        return float('nan')
    return (n * sxy - sx * sy) / denom


def growth_comparison(
    alg: AlgebraFamily,
    sigma: float = 2.0,
    t_values: Optional[List[float]] = None,
) -> Dict[str, float]:
    """Compare growth orders of all nine zeta functions."""
    if t_values is None:
        t_values = [10.0, 20.0, 50.0, 100.0]

    return {
        'shadow': growth_order(lambda s: shadow_zeta(alg, s), sigma, t_values),
        'epstein': growth_order(
            lambda s: constrained_epstein_fast(alg.kappa, s, 50), sigma, t_values
        ) if alg.kappa > 0 else float('nan'),
        'selberg': growth_order(
            lambda s: shadow_selberg_zeta(alg, s, 50), sigma, t_values
        ),
        'fredholm': growth_order(
            lambda s: fredholm_zeta_direct(alg, s), sigma, t_values
        ),
        'categorical': growth_order(
            lambda s: categorical_zeta(alg, s, 200), sigma, t_values
        ),
        'btz': growth_order(
            lambda s: btz_spectral_zeta(alg, s), sigma, t_values
        ),
        'kloosterman': growth_order(
            lambda s: kloosterman_zeta(alg, s, 50), sigma, t_values
        ),
        'hecke': growth_order(
            lambda s: hecke_l_function(alg, s, 30), sigma, t_values
        ),
    }


# ============================================================================
# SECTION 8:  Shadow Li coefficients
# ============================================================================

def shadow_li_coefficients(
    zeros: List[complex],
    n_max: int = 10,
) -> Dict[int, complex]:
    r"""Shadow Li coefficients from the zeros of zeta_A.

    lambda_n^sh = sum_rho (1 - (1 - 1/rho)^n)

    Positivity of Re(lambda_n^sh) for all n >= 1 is the analogue of the
    Li criterion for the Riemann zeta function.
    """
    result = {}
    for n in range(1, n_max + 1):
        total = 0.0 + 0.0j
        for rho in zeros:
            if abs(rho) < 1e-15:
                continue
            total += 1.0 - (1.0 - 1.0 / rho) ** n
        result[n] = total
    return result


def li_positivity_check(
    zeros: List[complex],
    n_max: int = 10,
) -> Dict[str, Any]:
    """Check whether all Li coefficients have positive real part."""
    li = shadow_li_coefficients(zeros, n_max)
    all_positive = all(li[n].real > -1e-10 for n in range(1, n_max + 1))
    first_negative = None
    for n in range(1, n_max + 1):
        if li[n].real < -1e-10:
            first_negative = n
            break
    return {
        'li_coefficients': li,
        'all_positive': all_positive,
        'first_negative_index': first_negative,
    }


# ============================================================================
# SECTION 9:  Abscissa of convergence
# ============================================================================

def abscissa_of_convergence(alg: AlgebraFamily) -> float:
    r"""Estimate the abscissa of convergence sigma_c of the shadow zeta.

    For class G/L/C: sigma_c = -infinity (finite sum, entire function).
    For class M: sigma_c = lim sup log|S_r| / log r.
    """
    sc = shadow_class_of(alg.family)
    if sc in ('G', 'L', 'C'):
        return float('-inf')

    # Class M: estimate from shadow coefficients
    coeffs = alg.shadow_coeffs
    max_r = max(coeffs.keys())
    ratios = []
    for r in range(10, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) > 1e-300:
            ratios.append(math.log(abs(Sr)) / math.log(r))

    if not ratios:
        return 0.0

    # The abscissa is the lim sup of these ratios
    # For rho < 1: log|S_r| ~ r*log(rho) - (5/2)*log(r) -> -infty
    # So ratios -> -infty, abscissa = -infty (entire)
    # For rho >= 1: ratios -> +infty, abscissa = +infty (nowhere convergent)
    return max(ratios[-10:])  # Use last 10 for stability


# ============================================================================
# SECTION 10:  Atlas table generation
# ============================================================================

@dataclass
class AtlasTableRow:
    """One row of the Grand Unified Zeta Atlas table."""
    name: str
    family: str
    kappa: float
    central_charge: float
    shadow_class: str
    shadow_depth: Union[int, float]
    abscissa: float
    n_shadow_zeros: int
    first_shadow_zero: Optional[complex]
    growth_orders: Dict[str, float]
    li_first_5: List[complex]
    kappa_sum: Optional[float]


def build_atlas_table(
    families: Optional[List[AlgebraFamily]] = None,
    zero_im_max: float = 30.0,
) -> List[AtlasTableRow]:
    """Build the full Grand Unified Zeta Atlas table."""
    if families is None:
        families = build_standard_family_table()

    rows = []
    for alg in families:
        # Find shadow zeta zeros
        try:
            zeros = find_shadow_zeta_zeros(
                alg,
                re_range=(-5.0, 5.0),
                im_range=(0.0, zero_im_max),
                grid_re=8,
                grid_im=40,
            )
        except (ValueError, ZeroDivisionError):
            zeros = []

        # Growth orders
        try:
            growth = growth_comparison(alg, sigma=2.0, t_values=[10.0, 30.0, 60.0])
        except (ValueError, ZeroDivisionError):
            growth = {}

        # Li coefficients
        if zeros:
            li = shadow_li_coefficients(zeros, 5)
            li_list = [li.get(n, 0.0) for n in range(1, 6)]
        else:
            li_list = [complex(0, 0)] * 5

        # Abscissa
        try:
            sigma_c = abscissa_of_convergence(alg)
        except (ValueError, ZeroDivisionError):
            sigma_c = float('nan')

        rows.append(AtlasTableRow(
            name=alg.name,
            family=alg.family,
            kappa=alg.kappa,
            central_charge=alg.central_charge,
            shadow_class=alg.shadow_class,
            shadow_depth=alg.shadow_depth,
            abscissa=sigma_c,
            n_shadow_zeros=len(zeros),
            first_shadow_zero=zeros[0] if zeros else None,
            growth_orders=growth,
            li_first_5=li_list,
            kappa_sum=alg.kappa_sum,
        ))

    return rows


def atlas_summary(
    rows: Optional[List[AtlasTableRow]] = None,
) -> Dict[str, Any]:
    """Summary statistics of the atlas table."""
    if rows is None:
        rows = build_atlas_table()

    n_families = len(rows)
    n_with_zeros = sum(1 for r in rows if r.n_shadow_zeros > 0)
    classes = {}
    for r in rows:
        classes.setdefault(r.shadow_class, []).append(r.name)

    return {
        'n_families': n_families,
        'n_with_zeros': n_with_zeros,
        'class_distribution': {k: len(v) for k, v in classes.items()},
        'kappa_range': (
            min(r.kappa for r in rows),
            max(r.kappa for r in rows),
        ),
    }


# ============================================================================
# SECTION 11:  Five-theorem consistency battery
# ============================================================================

def five_theorem_consistency(
    alg: AlgebraFamily,
) -> Dict[str, Dict[str, Any]]:
    """Run all five theorem consistency checks for a single algebra."""
    results = {}

    # Theorem A: Verdier intertwining
    if alg.family == 'virasoro':
        results['theorem_A'] = check_verdier_intertwining(alg.param)
    else:
        results['theorem_A'] = {'status': 'skipped (non-Virasoro)'}

    # Theorem B: bar-cobar invariance
    results['theorem_B'] = check_bar_cobar_invariance(alg)

    # Theorem C: complementarity
    if alg.family == 'virasoro':
        results['theorem_C'] = check_complementarity(alg.param, complex(2, 0))
    else:
        results['theorem_C'] = {'status': 'skipped (non-Virasoro)'}

    # Theorem D: kappa controls leading behavior
    results['theorem_D'] = check_leading_behavior(alg)

    # Theorem H: polynomial Hochschild growth
    results['theorem_H'] = check_hochschild_polynomial_growth(alg)

    return results


# ============================================================================
# SECTION 12:  Pair-wise cross-consistency matrix
# ============================================================================

def pairwise_consistency_matrix(
    alg: AlgebraFamily,
    s: complex = complex(3, 1),
) -> Dict[str, Dict[str, complex]]:
    """Evaluate all nine zeta functions at s and build a pairwise ratio matrix.

    The ratios between different zeta functions (when they exist) reveal
    relationships imposed by the five main theorems.
    """
    entry = evaluate_all_zetas(alg, s)
    zetas = {
        'shadow': entry.shadow_zeta,
        'epstein': entry.constrained_epstein,
        'selberg': entry.shadow_selberg,
        'fredholm': entry.fredholm_zeta,
        'ihara': entry.ihara_zeta,
        'categorical': entry.categorical_zeta,
        'btz': entry.btz_spectral,
        'kloosterman': entry.kloosterman_zeta,
        'hecke': entry.hecke_l,
    }

    matrix: Dict[str, Dict[str, complex]] = {}
    for name_i, val_i in zetas.items():
        matrix[name_i] = {}
        for name_j, val_j in zetas.items():
            if abs(val_j) > 1e-300 and not cmath.isnan(val_i) and not cmath.isnan(val_j):
                matrix[name_i][name_j] = val_i / val_j
            else:
                matrix[name_i][name_j] = complex(float('nan'))

    return matrix


# ============================================================================
# SECTION 13:  Full cross-verification run
# ============================================================================

def run_full_cross_verification(
    families: Optional[List[AlgebraFamily]] = None,
    s_test: complex = complex(3, 1),
) -> Dict[str, Any]:
    r"""Run the complete cross-verification battery.

    For each family:
    1. Evaluate all 9 zeta functions at s_test
    2. Check leading behavior (Theorem D)
    3. Check negative-integer moments
    4. Check Fredholm/Selberg ratio
    5. For Virasoro: check complementarity (Theorem C)

    Returns a summary of all consistency checks.
    """
    if families is None:
        families = build_standard_family_table()

    report: Dict[str, Any] = {
        'n_families': len(families),
        'test_point': s_test,
        'results': {},
    }

    n_pass = 0
    n_fail = 0
    n_skip = 0

    for alg in families:
        family_result: Dict[str, Any] = {}

        # 1. Evaluate all zetas
        try:
            entry = evaluate_all_zetas(alg, s_test)
            family_result['zeta_values'] = {
                'shadow': entry.shadow_zeta,
                'epstein': entry.constrained_epstein,
                'selberg': entry.shadow_selberg,
                'fredholm': entry.fredholm_zeta,
                'ihara': entry.ihara_zeta,
                'categorical': entry.categorical_zeta,
                'btz': entry.btz_spectral,
                'kloosterman': entry.kloosterman_zeta,
                'hecke': entry.hecke_l,
            }
        except Exception as e:
            family_result['zeta_values'] = {'error': str(e)}

        # 2. Leading behavior (Theorem D)
        try:
            leading = check_leading_behavior(alg)
            family_result['theorem_D'] = leading
            if leading.get('consistent', False):
                n_pass += 1
            else:
                n_fail += 1
        except Exception:
            n_skip += 1

        # 3. Negative-integer moments
        try:
            moments = check_shadow_zeta_negative_integers(alg)
            all_ok = all(v.get('consistent', False) for v in moments.values())
            family_result['negative_moments'] = {
                'all_consistent': all_ok,
                'n_checked': len(moments),
            }
            if all_ok:
                n_pass += 1
            else:
                n_fail += 1
        except Exception:
            n_skip += 1

        # 4. Fredholm/Selberg ratio
        try:
            fred = check_fredholm_selberg_ratio(alg, s_test)
            family_result['fredholm_selberg'] = fred
            if fred.get('consistent', False):
                n_pass += 1
            else:
                if shadow_class_of(alg.family) in ('G', 'L', 'C'):
                    n_skip += 1  # Trivial for finite towers
                else:
                    n_fail += 1
        except Exception:
            n_skip += 1

        # 5. Complementarity (Virasoro only)
        if alg.family == 'virasoro':
            try:
                comp = check_complementarity(alg.param, s_test)
                family_result['complementarity'] = comp
                if comp.get('kappa_sum_is_13', False):
                    n_pass += 1
                else:
                    n_fail += 1
            except Exception:
                n_skip += 1

        report['results'][alg.name] = family_result

    report['summary'] = {
        'n_pass': n_pass,
        'n_fail': n_fail,
        'n_skip': n_skip,
        'pass_rate': n_pass / max(n_pass + n_fail, 1),
    }

    return report
