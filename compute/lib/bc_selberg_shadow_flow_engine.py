r"""Selberg-type zeta function from the shadow connection flow.

MATHEMATICAL FRAMEWORK
======================

The shadow connection nabla^sh = d - Q'_L/(2Q_L) dt defines a logarithmic
connection on a trivial line bundle over the shadow parameter space L \ {Q=0}.
This connection has:

  - Regular singular points at the zeros of Q_L(t) with residue 1/2
  - Monodromy exp(2*pi*i * 1/2) = -1 (the Koszul sign)
  - Flat sections Phi(t) = sqrt(Q_L(t)/Q_L(0))

SHADOW FLOW AND CLOSED ORBITS
------------------------------

The shadow metric Q_L(t) = q0 + q1*t + q2*t^2 is a quadratic polynomial
whose zeros (branch points) t_+, t_- determine the geometry:

  - Class G/L/C: branch points are real or at infinity (finite tower)
  - Class M: branch points are a complex conjugate pair t_pm = a +/- ib

For CLASS M, define the "shadow flow" as follows. The double cover
Y^2 = Q_L(t) defines an elliptic-type curve. The period of the
connection around a branch point gives a CLOSED ORBIT.

ORBIT LENGTHS:
  The orbit encircling branch point t_0 has length

    ell(gamma) = 2*pi * |Res_{t_0}(Q'/(2Q))| * |t_0|

  Since Res = 1/2 at every simple zero, ell(gamma) = pi * |t_0|.

  For the Virasoro shadow connection:
    |t_0| = R (the convergence radius = 1/rho)
    ell(gamma) = pi / rho

  More precisely, the PERIOD of the connection along a small loop
  gamma around a branch point t_0 is:

    integral_gamma omega dt = 2*pi*i * Res_{t_0}(omega) = pi*i

  This gives monodromy exp(pi*i) = -1 (the Koszul sign).

  The "topological length" of gamma is the absolute value of the
  LOG of the monodromy eigenvalue:

    ell(gamma) = |log(-1)| = pi       (the TOPOLOGICAL orbit length)

  This is UNIVERSAL: all orbits have topological length pi, since
  all residues equal 1/2. The geometric length depends on the
  metric on the parameter space.

  For the GEOMETRIC length using the shadow metric Q_L as the metric
  on the base:

    ell_geom(gamma) = integral_gamma |omega| |dt|

  For a small circle of radius epsilon around t_0:
    omega ~ 1/(2(t-t_0))
    |omega| |dt| ~ |dt/(2(t-t_0))| = d(theta)/2 on a circle
    ell_geom = integral_0^{2*pi} d(theta)/2 = pi

  This confirms: ell_geom = pi (universal for simple zeros, independent
  of the algebra or the branch point location).

SHADOW SELBERG ZETA FUNCTION
-----------------------------

With orbit lengths ell(gamma_j), define:

  Z^{Sel}_A(s) = prod_j prod_{k>=0} (1 - M_j * exp(-(s+k)*ell(gamma_j)))

where M_j = -1 is the monodromy eigenvalue and ell(gamma_j) = pi is the
orbit length. Since there are exactly 2 branch points (counting):

  Z^{Sel}_A(s) = prod_{j=1}^{N_bp} prod_{k>=0} (1 - (-1) * exp(-(s+k)*pi))
              = prod_{j=1}^{N_bp} prod_{k>=0} (1 + exp(-(s+k)*pi))

For N_bp = 2 (class M with 2 simple branch points):

  Z^{Sel}_A(s) = [prod_{k>=0} (1 + exp(-(s+k)*pi))]^2

This has EXPLICIT EVALUATION via the Jacobi triple product and
q-Pochhammer identities:

  prod_{k>=0} (1 + q^k) = (-q; q)_inf  where q = e^{-pi}

RUELLE ZETA FUNCTION
--------------------

  zeta^{Ruelle}_A(s) = prod_j (1 - M_j * exp(-s*ell(gamma_j)))^{-1}
                     = prod_j (1 + exp(-s*pi))^{-1}

For N_bp = 2:
  zeta^{Ruelle}_A(s) = (1 + exp(-s*pi))^{-2}

ENHANCED CONSTRUCTION: GEOMETRIC ORBIT LENGTHS
-----------------------------------------------

Rather than using universal topological lengths, incorporate the
BRANCH POINT MODULUS |t_0| as a geometric scale factor:

  ell_A(gamma_j) = pi * |t_j|

For Virasoro:
  |t_0| = R_Vir(c) = 1/rho(c)
  ell_A(gamma) = pi / rho(c)

This makes the Selberg zeta FAMILY-DEPENDENT:

  Z^{Sel}_A(s) = [prod_{k>=0} (1 + exp(-(s+k)*pi/rho(A)))]^{N_bp}

The zeros of Z^{Sel}_A(s) occur where exp(-(s+k)*pi/rho(A)) = -1,
i.e., where (s+k)*pi/rho(A) = (2n+1)*pi*i for integer n:

  s = -k + (2n+1)*i*rho(A)

So the zeros lie on vertical lines Re(s) = -k for k = 0, 1, 2, ...
with imaginary parts spaced by 2*rho(A).

COMPARISON WITH RIEMANN ZEROS
------------------------------

The Riemann zeta zeros lie on Re(s) = 1/2 (conjecturally).
The shadow Selberg zeros lie on Re(s) = 0, -1, -2, ...

These are DIFFERENT objects with DIFFERENT spectral meanings:
  - Riemann zeros encode prime distribution
  - Shadow Selberg zeros encode branch-point monodromy

Any numerical alignment with Riemann zeros would be COINCIDENTAL
unless there is a deep structural reason. We test for this
systematically but expect NO systematic alignment.

DYNAMICAL ENTROPY
-----------------

The topological entropy of the shadow flow measures the exponential
growth rate of closed orbits. Since ALL orbits have the same
topological length pi (from the universal residue 1/2), the orbit
counting function is:

  N(T) = #{orbits of length <= T} = N_bp * floor(T/pi)

This grows LINEARLY, giving topological entropy h = 0.

For the WEIGHTED entropy using geometric lengths:

  h_A = lim_{T->inf} (1/T) * log #{gamma : ell_A(gamma) <= T}

Since we have finitely many prime orbits (N_bp = 2), their iterates
give N(T) ~ T / ell_min, so h_A = 0 again.

The vanishing of dynamical entropy reflects the INTEGRABILITY of the
shadow connection (it is a connection on a LINE BUNDLE, hence abelian).
Nonzero entropy would require a nonabelian connection, which could
arise from multi-channel shadow connections (rank > 1).

MULTI-CHANNEL SELBERG ZETA
---------------------------

For multi-generator algebras with shadow metric Q on a space of
dimension d > 1, the shadow connection is a connection on a
vector bundle of rank d. The monodromy representation is
rho: pi_1(L \ Sigma) -> GL(d), where Sigma is the discriminant
locus. The Selberg zeta is:

  Z^{Sel,d}_A(s) = prod_gamma prod_{k>=0} det(I - M_gamma * exp(-(s+k)*ell(gamma)))

where M_gamma is the monodromy matrix along gamma and ell(gamma)
is the geometric length. This is much richer: the monodromy
eigenvalues can be arbitrary, not just -1.

Manuscript references:
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-growth-rate (higher_genus_modular_koszul.tex)

CAUTION (AP1): kappa formulas are family-specific. Recompute from first principles.
CAUTION (AP9): S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP19): The bar complex propagator extracts residues along d log(z-w).
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP42): "Selberg zeta = shadow" is correct at the structural level;
    naive comparison with Riemann zeros should not be expected to work.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple


# ============================================================================
# 1. Shadow coefficient providers (self-contained)
# ============================================================================

def _virasoro_shadow_coefficients(c_val: float, max_r: int = 60) -> Dict[int, float]:
    """Shadow coefficients for Virasoro Vir_c via convolution recursion.

    S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L).
    Q_L(t) = c^2 + 12c*t + alpha(c)*t^2, alpha(c) = (180c + 872)/(5c + 22).
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")
    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    a0 = abs(c_val)
    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2.0 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))
    result = {}
    for n in range(len(a)):
        r = n + 2
        result[r] = a[n] / float(r)
    return result


def _heisenberg_shadow_coefficients(k_val: float, max_r: int = 60) -> Dict[int, float]:
    """Heisenberg shadow coefficients. S_2 = k, S_r = 0 for r >= 3."""
    result = {2: float(k_val)}
    for r in range(3, max_r + 1):
        result[r] = 0.0
    return result


def _affine_shadow_coefficients(
    dim_g: float, h_dual: float, k_val: float, max_r: int = 60,
) -> Dict[int, float]:
    """Affine KM shadow coefficients. kappa = dim(g)(k+h^v)/(2h^v), S_3 = alpha.
    S_r = 0 for r >= 4 (class L).
    """
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = 0.0
    return result


def _betagamma_shadow_coefficients(lam_val: float = 0.5, max_r: int = 60) -> Dict[int, float]:
    """Beta-gamma at weight lambda. Class C, terminates at arity 4."""
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0
    result = {2: kappa, 3: 2.0}
    if c_val != 0.0 and 5.0 * c_val + 22.0 != 0.0:
        result[4] = 10.0 / (c_val * (5.0 * c_val + 22.0))
    else:
        result[4] = 0.0
    for r in range(5, max_r + 1):
        result[r] = 0.0
    return result


# ============================================================================
# 2. Shadow metric and branch point geometry
# ============================================================================

def shadow_metric_Q(kappa: float, alpha: float, S4: float, t: complex) -> complex:
    """Evaluate Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2."""
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    return q0 + q1 * t + q2 * t * t


def shadow_metric_coefficients(kappa: float, alpha: float, S4: float) -> Tuple[float, float, float]:
    """Return (q0, q1, q2) for Q_L(t) = q0 + q1*t + q2*t^2."""
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    return q0, q1, q2


def branch_points(kappa: float, alpha: float, S4: float) -> Tuple[complex, complex]:
    """Zeros of Q_L(t): the branch points of the shadow flow.

    Returns (t_plus, t_minus) as complex numbers.
    For Delta > 0 (class M generic): complex conjugate pair.
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
    if abs(q2) < 1e-300:
        # Degenerate: Q is at most linear
        if abs(q1) < 1e-300:
            return (complex(float('inf')), complex(float('inf')))
        t0 = -q0 / q1
        return (complex(t0), complex(float('inf')))
    disc = q1 * q1 - 4.0 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)
    return (t_plus, t_minus)


def virasoro_shadow_data(c_val: float) -> Tuple[float, float, float, float]:
    """Return (kappa, alpha, S4, Delta) for Virasoro at central charge c."""
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4
    return kappa, alpha, S4, Delta


def virasoro_branch_points(c_val: float) -> Tuple[complex, complex]:
    """Branch points of the Virasoro shadow metric at central charge c."""
    kappa, alpha, S4, _ = virasoro_shadow_data(c_val)
    return branch_points(kappa, alpha, S4)


def virasoro_growth_rate(c_val: float) -> float:
    """Exact shadow growth rate rho(Vir_c) = 1/|t_0|.

    rho = sqrt((180c+872)/((5c+22)*c^2)).
    """
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    if denom <= 0:
        return float('inf')
    return math.sqrt(numer / denom)


def affine_sl2_shadow_data(k_val: float) -> Tuple[float, float, float, float]:
    """Return (kappa, alpha, S4, Delta) for affine sl_2."""
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    S4 = 0.0  # Class L: terminates at arity 3
    Delta = 0.0
    return kappa, alpha, S4, Delta


def heisenberg_shadow_data(k_val: float) -> Tuple[float, float, float, float]:
    """Return (kappa, alpha, S4, Delta) for Heisenberg."""
    return float(k_val), 0.0, 0.0, 0.0


# ============================================================================
# 3. Orbit geometry
# ============================================================================

@dataclass
class ShadowOrbit:
    """A closed orbit of the shadow flow around a branch point.

    Attributes:
        branch_point: the zero of Q_L around which the orbit wraps
        topological_length: |log(monodromy eigenvalue)| = pi (universal)
        geometric_length: pi * |branch_point| (family-dependent)
        monodromy: the monodromy eigenvalue (-1 for simple zeros)
        residue: the connection residue (1/2 for simple zeros)
        winding_number: how many times the orbit wraps (1 for primitive)
    """
    branch_point: complex
    topological_length: float
    geometric_length: float
    monodromy: complex
    residue: float
    winding_number: int = 1


def compute_orbits(
    kappa: float, alpha: float, S4: float,
) -> List[ShadowOrbit]:
    """Compute the closed orbits of the shadow flow.

    For a quadratic shadow metric Q_L with two branch points, there are
    exactly 2 primitive orbits (one around each branch point), plus their
    iterates (winding number > 1).

    Returns list of primitive orbits only. Iterate orbits can be generated
    by multiplying the lengths by the winding number.
    """
    t_plus, t_minus = branch_points(kappa, alpha, S4)
    orbits = []

    for bp in [t_plus, t_minus]:
        bp_mod = abs(bp)
        if bp_mod > 1e100:
            continue  # Branch point at infinity: no finite orbit
        orbits.append(ShadowOrbit(
            branch_point=bp,
            topological_length=math.pi,
            geometric_length=math.pi * bp_mod,
            monodromy=-1.0 + 0.0j,
            residue=0.5,
            winding_number=1,
        ))

    return orbits


def compute_orbits_with_iterates(
    kappa: float, alpha: float, S4: float,
    max_winding: int = 20,
) -> List[ShadowOrbit]:
    """Compute primitive orbits and their iterates up to given winding number."""
    primitives = compute_orbits(kappa, alpha, S4)
    all_orbits = []
    for prim in primitives:
        for n in range(1, max_winding + 1):
            all_orbits.append(ShadowOrbit(
                branch_point=prim.branch_point,
                topological_length=prim.topological_length * n,
                geometric_length=prim.geometric_length * n,
                monodromy=prim.monodromy ** n,  # (-1)^n
                residue=prim.residue,
                winding_number=n,
            ))
    return all_orbits


def virasoro_orbits(c_val: float) -> List[ShadowOrbit]:
    """Compute orbits for Virasoro at central charge c."""
    kappa, alpha, S4, _ = virasoro_shadow_data(c_val)
    return compute_orbits(kappa, alpha, S4)


def count_orbits_up_to_length(
    orbits: List[ShadowOrbit],
    T: float,
    use_geometric: bool = True,
    max_winding: int = 1000,
) -> int:
    """Count orbits (including iterates) with length <= T.

    Parameters
    ----------
    orbits : list of PRIMITIVE orbits
    T : length threshold
    use_geometric : if True, use geometric length; else topological
    max_winding : maximum winding number to consider
    """
    count = 0
    for orb in orbits:
        length = orb.geometric_length if use_geometric else orb.topological_length
        if length <= 0 or length > T:
            continue
        # This primitive orbit contributes floor(T/length) iterates
        n_max = min(int(T / length), max_winding)
        count += n_max
    return count


# ============================================================================
# 4. Selberg zeta function
# ============================================================================

def selberg_zeta_from_orbits(
    orbits: List[ShadowOrbit],
    s: complex,
    max_k: int = 50,
    use_geometric: bool = True,
) -> complex:
    """Compute the shadow Selberg zeta function.

    Z^{Sel}_A(s) = prod_gamma prod_{k>=0} (1 - M_gamma * exp(-(s+k)*ell(gamma)))

    where the outer product is over PRIMITIVE orbits gamma.

    Parameters
    ----------
    orbits : list of PRIMITIVE orbits
    s : complex parameter
    max_k : truncation of the k-product (converges exponentially)
    use_geometric : use geometric length (family-dependent) or topological
    """
    log_Z = 0.0 + 0.0j
    for orb in orbits:
        ell = orb.geometric_length if use_geometric else orb.topological_length
        M = orb.monodromy
        for k in range(max_k):
            factor = 1.0 - M * cmath.exp(-(s + k) * ell)
            if abs(factor) < 1e-300:
                # Zero of Z^Sel at this point
                return 0.0 + 0.0j
            log_Z += cmath.log(factor)
    return cmath.exp(log_Z)


def selberg_zeta_topological(
    N_bp: int,
    s: complex,
    max_k: int = 100,
) -> complex:
    """Selberg zeta using TOPOLOGICAL orbit lengths (all = pi).

    Z^{Sel}_A(s) = [prod_{k>=0} (1 + exp(-(s+k)*pi))]^{N_bp}

    Since M = -1 for all orbits: 1 - (-1)*exp(-x) = 1 + exp(-x).
    """
    log_Z = 0.0 + 0.0j
    for k in range(max_k):
        factor = 1.0 + cmath.exp(-(s + k) * math.pi)
        if abs(factor) < 1e-300:
            return 0.0 + 0.0j
        log_Z += cmath.log(factor)
    return cmath.exp(N_bp * log_Z)


def selberg_zeta_geometric(
    rho: float,
    N_bp: int,
    s: complex,
    max_k: int = 100,
) -> complex:
    """Selberg zeta using GEOMETRIC orbit lengths ell = pi/rho.

    Z^{Sel}_A(s) = [prod_{k>=0} (1 + exp(-(s+k)*pi/rho))]^{N_bp}
    """
    ell = math.pi / rho if rho > 0 else float('inf')
    if math.isinf(ell):
        return 1.0 + 0.0j  # No orbits
    log_Z = 0.0 + 0.0j
    for k in range(max_k):
        factor = 1.0 + cmath.exp(-(s + k) * ell)
        if abs(factor) < 1e-300:
            return 0.0 + 0.0j
        log_Z += cmath.log(factor)
    return cmath.exp(N_bp * log_Z)


def selberg_zeta_virasoro(c_val: float, s: complex, max_k: int = 100) -> complex:
    """Selberg zeta for Virasoro at central charge c.

    Uses geometric orbit length ell = pi/rho(c) with N_bp = 2 branch points.
    """
    rho = virasoro_growth_rate(c_val)
    return selberg_zeta_geometric(rho, 2, s, max_k)


# ============================================================================
# 5. Selberg zeta via trace formula (verification path 2)
# ============================================================================

def selberg_zeta_via_trace(
    orbits: List[ShadowOrbit],
    s: complex,
    max_winding: int = 200,
    use_geometric: bool = True,
) -> complex:
    """Compute log Z^{Sel}(s) via the trace formula:

    log Z^{Sel}(s) = -sum_gamma sum_{k>=1} M_gamma^k * exp(-s*k*ell(gamma))
                                             / (k * det(1 - P_gamma^k))

    For a rank-1 connection, P_gamma = M_gamma (the monodromy), so
    det(1 - P_gamma^k) = 1 - M_gamma^k.

    This is the SECOND independent computation path.

    WARNING: The standard Selberg trace formula relates log Z'(s)/Z(s) to
    spectral data. Here we use the Euler product/orbit sum directly.
    """
    log_Z = 0.0 + 0.0j
    for orb in orbits:
        ell = orb.geometric_length if use_geometric else orb.topological_length
        M = orb.monodromy
        for k in range(1, max_winding + 1):
            Mk = M ** k
            det_factor = 1.0 - Mk
            if abs(det_factor) < 1e-300:
                continue  # Skip singular terms
            term = Mk * cmath.exp(-s * k * ell) / (k * det_factor)
            log_Z -= term
    return cmath.exp(log_Z)


# ============================================================================
# 6. Ruelle zeta function
# ============================================================================

def ruelle_zeta_from_orbits(
    orbits: List[ShadowOrbit],
    s: complex,
    use_geometric: bool = True,
) -> complex:
    """Ruelle zeta function (no k-sum):

    zeta^{Ruelle}_A(s) = prod_gamma (1 - M_gamma * exp(-s*ell(gamma)))^{-1}
    """
    log_zeta = 0.0 + 0.0j
    for orb in orbits:
        ell = orb.geometric_length if use_geometric else orb.topological_length
        M = orb.monodromy
        factor = 1.0 - M * cmath.exp(-s * ell)
        if abs(factor) < 1e-300:
            return complex(float('inf'))
        log_zeta -= cmath.log(factor)
    return cmath.exp(log_zeta)


def ruelle_zeta_topological(N_bp: int, s: complex) -> complex:
    """Ruelle zeta with topological orbit lengths.

    zeta^{Ruelle}_A(s) = (1 + exp(-s*pi))^{-N_bp}
    """
    factor = 1.0 + cmath.exp(-s * math.pi)
    if abs(factor) < 1e-300:
        return complex(float('inf'))
    return factor ** (-N_bp)


def ruelle_zeta_geometric(rho: float, N_bp: int, s: complex) -> complex:
    """Ruelle zeta with geometric orbit lengths ell = pi/rho.

    zeta^{Ruelle}_A(s) = (1 + exp(-s*pi/rho))^{-N_bp}
    """
    ell = math.pi / rho if rho > 0 else float('inf')
    if math.isinf(ell):
        return 1.0 + 0.0j
    factor = 1.0 + cmath.exp(-s * ell)
    if abs(factor) < 1e-300:
        return complex(float('inf'))
    return factor ** (-N_bp)


def ruelle_zeta_virasoro(c_val: float, s: complex) -> complex:
    """Ruelle zeta for Virasoro at central charge c."""
    rho = virasoro_growth_rate(c_val)
    return ruelle_zeta_geometric(rho, 2, s)


# ============================================================================
# 7. Selberg-Ruelle relation
# ============================================================================

def selberg_ruelle_relation_check(
    orbits: List[ShadowOrbit],
    s: complex,
    max_k: int = 50,
    use_geometric: bool = True,
) -> Tuple[complex, complex]:
    """Verify the relation Z^{Sel}(s) = prod_{k>=0} zeta^{Ruelle}(s+k)^{-1}.

    Returns (Z_Sel, product_of_Ruelle_inverses) for comparison.
    """
    Z_sel = selberg_zeta_from_orbits(orbits, s, max_k, use_geometric)
    ruelle_product = 1.0 + 0.0j
    for k in range(max_k):
        zeta_r = ruelle_zeta_from_orbits(orbits, s + k, use_geometric)
        if abs(zeta_r) < 1e-300:
            break
        ruelle_product /= zeta_r
    return Z_sel, ruelle_product


# ============================================================================
# 8. Functional equation
# ============================================================================

def selberg_functional_equation_test(
    rho: float,
    N_bp: int,
    s: complex,
    max_k: int = 100,
) -> Tuple[complex, complex, complex]:
    """Test whether Z^{Sel}(s) = Z^{Sel}(1-s) * correction.

    For a classical Selberg zeta on a compact surface of genus g:
        Z(s)/Z(1-s) = exp(polynomial of degree 2g in s)

    For the shadow Selberg zeta, no such relation is expected in general
    because the underlying geometry is a meromorphic connection, not a
    compact Riemann surface.

    Returns (Z(s), Z(1-s), Z(s)/Z(1-s)).
    """
    Zs = selberg_zeta_geometric(rho, N_bp, s, max_k)
    Z1s = selberg_zeta_geometric(rho, N_bp, 1.0 - s, max_k)
    ratio = Zs / Z1s if abs(Z1s) > 1e-300 else complex(float('inf'))
    return Zs, Z1s, ratio


def functional_equation_scan(
    rho: float,
    N_bp: int,
    s_values: List[complex],
    max_k: int = 100,
) -> List[Tuple[complex, complex, complex, complex]]:
    """Scan the functional equation ratio Z(s)/Z(1-s) across multiple s values.

    Returns list of (s, Z(s), Z(1-s), Z(s)/Z(1-s)).
    """
    results = []
    for s in s_values:
        Zs, Z1s, ratio = selberg_functional_equation_test(rho, N_bp, s, max_k)
        results.append((s, Zs, Z1s, ratio))
    return results


# ============================================================================
# 9. Zeros of the Selberg zeta
# ============================================================================

def selberg_zeros_topological(
    N_bp: int,
    max_k: int = 10,
    max_n: int = 25,
) -> List[complex]:
    """Exact zeros of Z^{Sel} with topological orbit lengths.

    Z = [prod_{k>=0} (1 + exp(-(s+k)*pi))]^{N_bp}

    Zero when 1 + exp(-(s+k)*pi) = 0, i.e., exp(-(s+k)*pi) = -1,
    i.e., (s+k)*pi = (2n+1)*pi*i, i.e., s = -k + (2n+1)*i.
    """
    zeros = []
    for k in range(max_k):
        for n in range(-max_n, max_n + 1):
            zeros.append(complex(-k, 2 * n + 1))
    return sorted(zeros, key=lambda z: (abs(z.imag), z.real))


def selberg_zeros_geometric(
    rho: float,
    N_bp: int,
    max_k: int = 10,
    max_n: int = 25,
) -> List[complex]:
    """Exact zeros of Z^{Sel} with geometric orbit lengths ell = pi/rho.

    Zero when exp(-(s+k)*pi/rho) = -1, i.e., (s+k)*pi/rho = (2n+1)*pi*i,
    i.e., s = -k + (2n+1)*rho*i.

    The zeros lie on vertical lines Re(s) = -k with imaginary spacing 2*rho.
    """
    zeros = []
    for k in range(max_k):
        for n in range(-max_n, max_n + 1):
            zeros.append(complex(-k, (2 * n + 1) * rho))
    return sorted(zeros, key=lambda z: (abs(z.imag), z.real))


def selberg_zeros_virasoro(
    c_val: float,
    max_k: int = 5,
    max_n: int = 25,
) -> List[complex]:
    """Zeros of the Virasoro Selberg zeta."""
    rho = virasoro_growth_rate(c_val)
    return selberg_zeros_geometric(rho, 2, max_k, max_n)


def first_n_selberg_zeros(
    rho: float,
    N_bp: int,
    n: int = 50,
) -> List[complex]:
    """Return the first n zeros (by imaginary part magnitude) of Z^{Sel}.

    The zeros with smallest |Im(s)| are on Re(s) = 0:
        s = +/- rho * i, +/- 3*rho*i, +/- 5*rho*i, ...
    """
    zeros = []
    max_n_needed = n // (2 * max(N_bp, 1)) + 10
    max_k_needed = n // (2 * max_n_needed + 1) + 2
    for k in range(max_k_needed):
        for m in range(-max_n_needed, max_n_needed + 1):
            zeros.append(complex(-k, (2 * m + 1) * rho))

    # Sort by |Im(s)| then by Re(s) descending
    zeros.sort(key=lambda z: (abs(z.imag), -z.real))
    # Deduplicate
    unique = []
    for z in zeros:
        if not any(abs(z - u) < 1e-12 for u in unique):
            unique.append(z)
        if len(unique) >= n:
            break
    return unique[:n]


# ============================================================================
# 10. Comparison with Riemann zeros
# ============================================================================

# First 30 nontrivial Riemann zeta zeros (imaginary parts, positive side)
RIEMANN_ZERO_IMAG_PARTS = [
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739189, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167159,
    49.773832477672302, 52.970321477714460, 56.446247697063394,
    59.347044002602353, 60.831778524609809, 65.112544048081606,
    67.079810529494174, 69.546401711173979, 72.067157674481907,
    75.704690699083933, 77.144840068874805, 79.337375020249367,
    82.910380854086030, 84.735492980517050, 87.425274613125229,
    88.809111207634465, 92.491899270558484, 94.651344040519838,
    95.870634228245309, 98.831194218193692, 101.31785100573139,
]


def compare_with_riemann_zeros(
    rho: float,
    N_bp: int,
    n_zeros: int = 30,
) -> List[Tuple[float, float, float]]:
    """Compare shadow Selberg zeros with scaled Riemann zeros.

    The shadow zeros on Re(s) = 0 have imaginary parts (2n+1)*rho.
    The Riemann zeros have imaginary parts gamma_n.

    We compute the scaled Riemann zeros gamma_n / (2*pi) and compare
    with the shadow zero imaginary parts.

    Returns list of (shadow_zero_imag, nearest_riemann_scaled, difference).
    """
    n_avail = min(n_zeros, len(RIEMANN_ZERO_IMAG_PARTS))
    riemann_scaled = [g / (2.0 * math.pi) for g in RIEMANN_ZERO_IMAG_PARTS[:n_avail]]

    # Shadow zeros on Re(s) = 0 (positive imaginary part)
    shadow_imag = [(2 * n + 1) * rho for n in range(n_zeros)]

    results = []
    for si in shadow_imag[:n_avail]:
        # Find nearest Riemann zero
        diffs = [abs(si - ri) for ri in riemann_scaled]
        idx = diffs.index(min(diffs))
        results.append((si, riemann_scaled[idx], si - riemann_scaled[idx]))

    return results


def riemann_zero_alignment_score(
    rho: float,
    N_bp: int,
    n_zeros: int = 20,
) -> float:
    """Compute a score measuring alignment of shadow zeros with Riemann zeros.

    Score = 1/n * sum (min_j |shadow_i - riemann_j|) / riemann_j

    Lower score = better alignment. Score ~ 1 = random alignment.
    Score << 1 = systematic alignment (unexpected).
    """
    comparisons = compare_with_riemann_zeros(rho, N_bp, n_zeros)
    if not comparisons:
        return float('inf')
    total = 0.0
    for _, riem, diff in comparisons:
        if abs(riem) > 1e-10:
            total += abs(diff) / abs(riem)
        else:
            total += abs(diff)
    return total / len(comparisons)


# ============================================================================
# 11. Dynamical entropy
# ============================================================================

def dynamical_entropy_topological(
    orbits: List[ShadowOrbit],
    T_max: float = 100.0,
    n_points: int = 50,
) -> Tuple[List[float], List[float], float]:
    """Compute the topological entropy of the shadow flow.

    h = lim_{T->inf} (1/T) * log N(T)

    where N(T) = #{orbits of length <= T} (including iterates).

    For finitely many primitive orbits, N(T) grows LINEARLY:
    N(T) ~ sum_j T/ell_j, giving h = 0.

    Returns (T_values, N_values, estimated_entropy).
    """
    T_values = [T_max * (i + 1) / n_points for i in range(n_points)]
    N_values = []
    for T in T_values:
        N = count_orbits_up_to_length(orbits, T, use_geometric=True)
        N_values.append(float(N))

    # Estimate entropy from the last few points
    if len(T_values) >= 5 and N_values[-1] > 0:
        # h ~ log(N(T)) / T for large T
        h_estimates = []
        for i in range(len(T_values) - 5, len(T_values)):
            if N_values[i] > 0 and T_values[i] > 0:
                h_estimates.append(math.log(N_values[i]) / T_values[i])
        h = sum(h_estimates) / len(h_estimates) if h_estimates else 0.0
    else:
        h = 0.0

    return T_values, N_values, h


def dynamical_entropy_exact(orbits: List[ShadowOrbit]) -> float:
    """Exact dynamical entropy for the shadow flow.

    For a connection on a line bundle with finitely many branch points:
    h = 0 (integrability).

    This is because:
    1. The flow has finitely many primitive orbits.
    2. N(T) ~ c * T (linear growth, not exponential).
    3. Therefore lim log(N(T))/T = 0.

    The entropy vanishes because the shadow connection is ABELIAN
    (rank 1). Nonzero entropy requires a nonabelian connection.
    """
    return 0.0


# ============================================================================
# 12. Shadow spectral dimension and consistency
# ============================================================================

def shadow_spectral_dimension(rho: float) -> float:
    """Shadow spectral dimension d^sh(A) = 1 / log(1/rho) for class M.

    For classes G/L/C: rho = 0, d^sh = 0 (zero-dimensional spectrum).
    For class M with rho < 1: d^sh = 1/log(1/rho) > 0.
    For class M with rho >= 1: d^sh = infinity (non-summable tower).

    The spectral dimension controls the Weyl law for shadow coefficients:
    N^sh(eps) ~ eps^{-d^sh}.
    """
    if rho <= 0.0:
        return 0.0
    if rho >= 1.0:
        return float('inf')
    return 1.0 / math.log(1.0 / rho)


def selberg_consistency_with_spectral_dimension(
    rho: float,
    N_bp: int,
) -> Dict[str, float]:
    """Check that Selberg zero spacing is consistent with spectral dimension.

    The shadow Selberg zeros on Re(s) = 0 are spaced by 2*rho.
    The mean zero spacing should relate to the spectral dimension:
        mean_spacing ~ 1/d^sh ~ log(1/rho)

    Actually the zero spacing = 2*rho, while 1/d^sh = log(1/rho).
    These are DIFFERENT: the Selberg zero spacing depends on the orbit
    length, while the spectral dimension depends on the growth rate.
    They are related by rho = exp(-1/d^sh), so
        spacing = 2*exp(-1/d^sh).

    Returns dict of consistency data.
    """
    d_sh = shadow_spectral_dimension(rho)
    zero_spacing = 2.0 * rho
    predicted_spacing = 2.0 * math.exp(-1.0 / d_sh) if d_sh > 0 else 0.0

    return {
        'rho': rho,
        'spectral_dimension': d_sh,
        'zero_spacing': zero_spacing,
        'predicted_spacing_from_d_sh': predicted_spacing,
        'consistency': abs(zero_spacing - predicted_spacing) < 1e-10,
    }


# ============================================================================
# 13. Full landscape computation
# ============================================================================

@dataclass
class SelbergShadowData:
    """Complete Selberg-type data for a modular Koszul algebra."""
    name: str
    shadow_class: str
    kappa: float
    rho: float
    N_bp: int
    orbits: List[ShadowOrbit]
    spectral_dimension: float
    dynamical_entropy: float

    def selberg_zeta(self, s: complex, max_k: int = 50) -> complex:
        return selberg_zeta_from_orbits(self.orbits, s, max_k)

    def ruelle_zeta(self, s: complex) -> complex:
        return ruelle_zeta_from_orbits(self.orbits, s)

    def first_zeros(self, n: int = 50) -> List[complex]:
        return first_n_selberg_zeros(self.rho, self.N_bp, n)


def compute_selberg_data(
    name: str,
    shadow_class: str,
    kappa: float,
    alpha: float,
    S4: float,
) -> SelbergShadowData:
    """Compute complete Selberg data for a given algebra."""
    orbits = compute_orbits(kappa, alpha, S4)
    N_bp = len(orbits)

    bp_mods = [abs(o.branch_point) for o in orbits if abs(o.branch_point) < 1e100]
    rho = 1.0 / min(bp_mods) if bp_mods else 0.0

    d_sh = shadow_spectral_dimension(rho)
    h = dynamical_entropy_exact(orbits)

    return SelbergShadowData(
        name=name,
        shadow_class=shadow_class,
        kappa=kappa,
        rho=rho,
        N_bp=N_bp,
        orbits=orbits,
        spectral_dimension=d_sh,
        dynamical_entropy=h,
    )


def compute_virasoro_selberg_landscape(
    c_values: Optional[List[float]] = None,
) -> Dict[float, SelbergShadowData]:
    """Compute Selberg data for Virasoro across a range of central charges."""
    if c_values is None:
        c_values = [0.5, 1.0, 2.0, 4.0, 6.0, 7.0, 10.0, 13.0, 20.0, 25.0, 26.0]
    landscape = {}
    for c_val in c_values:
        try:
            kappa, alpha, S4, _ = virasoro_shadow_data(c_val)
            landscape[c_val] = compute_selberg_data(
                f'Vir_c={c_val}', 'M', kappa, alpha, S4,
            )
        except (ValueError, ZeroDivisionError):
            pass
    return landscape


def compute_full_selberg_landscape() -> Dict[str, SelbergShadowData]:
    """Compute Selberg data for the standard modular Koszul landscape."""
    landscape = {}

    # Heisenberg at k = 1
    kappa, alpha, S4, _ = heisenberg_shadow_data(1.0)
    landscape['Heis_k=1'] = compute_selberg_data('Heis_k=1', 'G', kappa, alpha, S4)

    # Affine sl_2 at k = 1
    kappa, alpha, S4, _ = affine_sl2_shadow_data(1.0)
    landscape['aff_sl2_k=1'] = compute_selberg_data('aff_sl2_k=1', 'L', kappa, alpha, S4)

    # Virasoro at c = 1/2 (Ising)
    kappa, alpha, S4, _ = virasoro_shadow_data(0.5)
    landscape['Vir_c=1/2'] = compute_selberg_data('Vir_c=1/2', 'M', kappa, alpha, S4)

    # Virasoro at c = 1
    kappa, alpha, S4, _ = virasoro_shadow_data(1.0)
    landscape['Vir_c=1'] = compute_selberg_data('Vir_c=1', 'M', kappa, alpha, S4)

    # Virasoro at c = 13 (self-dual)
    kappa, alpha, S4, _ = virasoro_shadow_data(13.0)
    landscape['Vir_c=13'] = compute_selberg_data('Vir_c=13', 'M', kappa, alpha, S4)

    # Virasoro at c = 25
    kappa, alpha, S4, _ = virasoro_shadow_data(25.0)
    landscape['Vir_c=25'] = compute_selberg_data('Vir_c=25', 'M', kappa, alpha, S4)

    return landscape


# ============================================================================
# 14. Class G/L exact computations (verification path 3)
# ============================================================================

def selberg_zeta_class_G_exact(k_val: float, s: complex, max_k: int = 100) -> complex:
    """Exact Selberg zeta for Heisenberg (class G): no branch points.

    Since Q_L = 4*k^2 (constant, no zeros for k != 0), there are
    NO branch points and hence NO orbits. Z^{Sel} = 1 (empty product).
    """
    return 1.0 + 0.0j


def ruelle_zeta_class_G_exact(k_val: float, s: complex) -> complex:
    """Exact Ruelle zeta for Heisenberg: 1 (empty product)."""
    return 1.0 + 0.0j


def selberg_zeta_class_L_exact(
    kappa: float, alpha: float, s: complex, max_k: int = 100,
) -> complex:
    """Exact Selberg zeta for affine KM (class L): branch points are real.

    Q_L = (2*kappa + 3*alpha*t)^2 (since Delta = 0 for class L).
    Double root at t_0 = -2*kappa/(3*alpha).
    Not a simple zero: connection has residue 1, not 1/2.
    The orbits around a double zero are TRIVIAL (logarithmic, not algebraic
    branching). Hence Z^{Sel} = 1.

    Actually, for a double root, the residue of Q'/(2Q) is 1, so the
    monodromy is exp(2*pi*i) = 1 (trivial). This means class L has no
    nontrivial closed orbits and Z^{Sel} = 1.
    """
    return 1.0 + 0.0j


# ============================================================================
# 15. Selberg-shadow zeta product (hybrid construction)
# ============================================================================

def shadow_selberg_product_zeta(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
    max_k: int = 30,
) -> complex:
    """Euler-type product over shadow arities:

    Z^{sh-Sel}_A(s) = prod_{r>=2} prod_{k>=0} (1 - S_r * r^{-(s+k)})

    This is a HYBRID construction: it uses the shadow coefficients as
    "orbit weights" and the arities as "orbit labels," building a Selberg-type
    product over the Dirichlet series data.

    NOT the same as the geometric Selberg zeta from orbits.
    Provided as an alternative construction for comparison.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    log_Z = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        for k in range(max_k):
            factor = 1.0 - Sr * r ** (-(s + k))
            if abs(factor) < 1e-300:
                return 0.0 + 0.0j
            log_Z += cmath.log(factor)
    return cmath.exp(log_Z)


# ============================================================================
# 16. Multi-channel Selberg zeta (rank > 1)
# ============================================================================

def multi_channel_selberg_zeta(
    monodromy_eigenvalues: List[complex],
    orbit_length: float,
    s: complex,
    max_k: int = 50,
) -> complex:
    """Multi-channel Selberg zeta for a rank-d connection.

    Z(s) = prod_{k>=0} det(I - M * exp(-(s+k)*ell))

    where M = diag(m_1, ..., m_d) is the monodromy matrix (diagonalized)
    and ell is the orbit length.

    det(I - M * q) = prod_i (1 - m_i * q) where q = exp(-(s+k)*ell).
    """
    log_Z = 0.0 + 0.0j
    for k in range(max_k):
        q = cmath.exp(-(s + k) * orbit_length)
        for m_i in monodromy_eigenvalues:
            factor = 1.0 - m_i * q
            if abs(factor) < 1e-300:
                return 0.0 + 0.0j
            log_Z += cmath.log(factor)
    return cmath.exp(log_Z)
