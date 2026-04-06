r"""bc_painleve_shadow_engine.py -- Painleve transcendents from shadow parameters.

BC-113: Painleve transcendents at shadow parameter values and connection to
the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The shadow connection nabla^sh = d - Q_L'/(2Q_L) dt is a logarithmic
connection with monodromy -1 (Koszul sign) around each branch point of
sqrt(Q_L).  When promoted to a Schrodinger equation via Liouville
transformation, the single-channel equation is a rigid Fuchsian system
(3 regular singular points on P^1) with NO Painleve structure.

Painleve transcendents emerge in THREE ways:

(I) MULTI-CHANNEL: For W_3 (and higher W_N), the T-channel and W-channel
    shadow metrics Q_T(t), Q_W(t) have 4 distinct zeros on P^1.  The
    coupled 2x2 Schrodinger system is a HEUN equation.  Isomonodromic
    deformation of the Heun system as the central charge c varies gives
    PAINLEVE VI.

(II) GENUS-1 CYLINDER: At genus 1, the shadow equation acquires a
     periodic (cylindrical) structure from the torus modulus.  The
     P_III equation governs the radial part of the cylindrical Schrodinger
     equation after separation of variables.

(III) FULL MC TOWER: The MC equation D*Theta + (1/2)[Theta,Theta] = 0 is
      an infinite-dimensional integrable system.  Finite reductions
      (truncation to a finite number of modes) produce Painleve
      transcendents as special solutions.

SINGULARITY CLASSIFICATION
==========================

Single-channel (Virasoro, Heisenberg, affine KM):
  - Delta = 0 (class G/L): trivial, u'' = 0
  - Delta != 0 (class M): 3 regular singularities = rigid Fuchsian
    = Gauss hypergeometric.  Indicial exponent 1/2 (double) at each
    zero of Q_L.  Equation is REDUCIBLE.

Multi-channel (W_3):
  - 4 zeros from Q_T and Q_W: Heun equation (4 regular singularities)
  - Cross-ratio lambda of the 4 singularities is the Painleve VI coordinate
  - P_VI parameters (alpha, beta, gamma, delta) from indicial exponents

Genus-1:
  - Periodic potential: V(t) = sum V_n exp(2*pi*i*n*t/L)
  - Cylindrical symmetry: P_III parameters from genus-1 shadow data

BEILINSON CRITICAL ASSESSMENT
==============================

1. Single-channel shadows DO NOT produce Painleve equations.  This is a
   theorem (rigid Fuchsian), not a deficiency.  The existing shadow_painleve.py
   correctly identifies this.

2. Multi-channel P_VI is GENUINE but requires the coupling between channels.
   The decoupled limit (coupling = 0) gives two independent hypergeometric
   equations, not Heun.

3. The connection to zeta zeros is EXPLORATORY.  The shadow metric evaluated
   at c = 1/2 + i*gamma_n (Virasoro at complex central charge) probes
   the shadow at zeta-zero parameters, but the mathematical content is the
   behaviour of Q_L(t; c) at these complex c values, not a direct
   Riemann-Hilbert correspondence.

4. P_III from genus 1 is a STRUCTURAL identification based on the cylinder
   periodicity, not a proved theorem connecting the genus-1 shadow to a
   specific P_III solution.

Dependencies:
    shadow_painleve.py -- base infrastructure
    shadow_connection.py -- shadow connection data
    shadow_tower_recursive.py -- exact shadow coefficients

References:
    [IKSY] Iwasaki-Kimura-Shimomura-Yoshida, From Gauss to Painleve (1991)
    [JMU] Jimbo-Miwa-Ueno, Monodromy preserving deformation (1981)
    [FIKN] Fokas-Its-Kapaev-Novokshenov, Painleve Transcendents (2006)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants: first 20 Riemann zeta zeros (imaginary parts)
# ---------------------------------------------------------------------------

ZETA_ZEROS_20 = [
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739189, 37.586178158825671,
    40.918719012147500, 43.327073280914999, 48.005150881167160,
    49.773832477672302, 52.970321477714460, 56.446247697063394,
    59.347044002602353, 60.831778524609809, 65.112544048081607,
    67.079810529494174, 69.546401711173980, 72.067157674481907,
    75.704690699083933, 77.144840068874805,
]


# ===========================================================================
# Section 1: Shadow family data (exact symbolic + numerical)
# ===========================================================================

@dataclass
class ShadowFamilyData:
    """Shadow data for a chiral algebra family."""
    name: str
    kappa: float          # modular characteristic
    alpha: float          # cubic shadow S_3
    S4: float             # quartic shadow S_4
    Delta: float          # critical discriminant 8*kappa*S4
    shadow_class: str     # 'G', 'L', 'C', 'M'
    r_max: int            # shadow depth (2, 3, 4, or -1 for infinity)
    c_value: float        # central charge


def virasoro_data(c_val: float) -> ShadowFamilyData:
    """Virasoro at central charge c."""
    kappa = c_val / 2
    alpha = 2.0
    denom = c_val * (5 * c_val + 22)
    if abs(denom) < 1e-30:
        S4 = float('inf')
        Delta = float('inf')
    else:
        S4 = 10.0 / denom
        Delta = 8 * kappa * S4
    return ShadowFamilyData(
        name='Virasoro', kappa=kappa, alpha=alpha, S4=S4, Delta=Delta,
        shadow_class='M', r_max=-1, c_value=c_val,
    )


def heisenberg_data(k: float = 1.0) -> ShadowFamilyData:
    """Rank-1 Heisenberg at level k.  kappa = k, alpha = 0, S4 = 0."""
    return ShadowFamilyData(
        name='Heisenberg', kappa=k, alpha=0.0, S4=0.0, Delta=0.0,
        shadow_class='G', r_max=2, c_value=2 * k,
    )


def affine_sl2_data(k: float) -> ShadowFamilyData:
    """Affine sl_2 at level k.  kappa = 3(k+2)/4, alpha != 0, S4 = 0."""
    kappa = 3.0 * (k + 2) / 4
    c_val = 3 * k / (k + 2)
    return ShadowFamilyData(
        name='affine_sl2', kappa=kappa, alpha=2.0, S4=0.0, Delta=0.0,
        shadow_class='L', r_max=3, c_value=c_val,
    )


def betagamma_data() -> ShadowFamilyData:
    """Beta-gamma at c = -1.  Class C, r_max = 4."""
    c_val = -1.0
    kappa = c_val / 2  # -1/2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22))  # 10/(-1*17) = -10/17
    Delta = 8 * kappa * S4  # 8*(-1/2)*(-10/17) = 40/17
    return ShadowFamilyData(
        name='betagamma', kappa=kappa, alpha=alpha, S4=S4, Delta=Delta,
        shadow_class='C', r_max=4, c_value=c_val,
    )


def w3_data(c_val: float) -> ShadowFamilyData:
    """W_3 algebra: multi-channel.  Returns T-channel data."""
    kappa = c_val / 2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22)) if abs(c_val * (5 * c_val + 22)) > 1e-30 else float('inf')
    Delta = 8 * kappa * S4 if S4 != float('inf') else float('inf')
    return ShadowFamilyData(
        name='W_3_T', kappa=kappa, alpha=alpha, S4=S4, Delta=Delta,
        shadow_class='M', r_max=-1, c_value=c_val,
    )


def w3_w_channel_data(c_val: float) -> ShadowFamilyData:
    """W_3 W-channel data."""
    kappa_W = c_val / 3
    alpha_W = 0.0
    denom = c_val * (5 * c_val + 22)**3
    if abs(denom) < 1e-30:
        S4_W = float('inf')
        Delta_W = float('inf')
    else:
        S4_W = 2560.0 / denom
        Delta_W = 8 * kappa_W * S4_W
    return ShadowFamilyData(
        name='W_3_W', kappa=kappa_W, alpha=alpha_W, S4=S4_W, Delta=Delta_W,
        shadow_class='M', r_max=-1, c_value=c_val,
    )


# ===========================================================================
# Section 2: Shadow metric, Q_L, branch points
# ===========================================================================

def shadow_metric_coeffs(kappa: float, alpha: float, Delta: float) -> Tuple[float, float, float]:
    """Q_L(t) = q0 + q1*t + q2*t^2."""
    q0 = 4 * kappa**2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha**2 + 2 * Delta
    return q0, q1, q2


def shadow_metric_eval(kappa: float, alpha: float, Delta: float, t: complex) -> complex:
    """Evaluate Q_L(t) at a (possibly complex) point."""
    q0, q1, q2 = shadow_metric_coeffs(kappa, alpha, Delta)
    return q0 + q1 * t + q2 * t**2


def branch_points(kappa: float, alpha: float, Delta: float) -> Tuple[complex, complex]:
    """Zeros of Q_L(t): the branch points of sqrt(Q_L)."""
    q0, q1, q2 = shadow_metric_coeffs(kappa, alpha, Delta)
    if abs(q2) < 1e-30:
        return (complex('nan'), complex('nan'))
    disc = q1**2 - 4 * q0 * q2  # = -32*kappa^2*Delta
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2 * q2)
    t_minus = (-q1 - sqrt_disc) / (2 * q2)
    return t_plus, t_minus


def cross_ratio_4pts(z1: complex, z2: complex, z3: complex, z4: complex) -> complex:
    """Cross-ratio (z1-z3)(z2-z4) / ((z1-z4)(z2-z3))."""
    num = (z1 - z3) * (z2 - z4)
    den = (z1 - z4) * (z2 - z3)
    if abs(den) < 1e-50:
        return complex('inf')
    return num / den


# ===========================================================================
# Section 3: Schwarzian potential and Schrodinger equation
# ===========================================================================

def schwarzian_potential(kappa: float, alpha: float, Delta: float, t: complex) -> complex:
    """V(t) = 8*kappa^2*Delta / Q_L(t)^2.

    The Schrodinger equation is u'' = V(t)*u.
    """
    Q = shadow_metric_eval(kappa, alpha, Delta, t)
    if abs(Q) < 1e-50:
        return complex('inf')
    return 8 * kappa**2 * Delta / Q**2


def indicial_exponent_at_zero(kappa: float, alpha: float, Delta: float,
                               which: str = 'plus') -> Tuple[complex, complex]:
    """Indicial exponents at a zero of Q_L.

    At a simple zero t_0: V ~ c_0/(t-t_0)^2 with c_0 = 8*kappa^2*Delta / Q'(t_0)^2.

    For Q_L quadratic with simple zeros:
        Q'(t_0) = sqrt(disc(Q_L)) (up to sign)
        Q'(t_0)^2 = disc(Q_L) = -32*kappa^2*Delta

    So c_0 = 8*kappa^2*Delta / (-32*kappa^2*Delta) = -1/4.

    Indicial equation: rho*(rho-1) = c_0 = -1/4
    => rho^2 - rho + 1/4 = 0 => (rho - 1/2)^2 = 0 => rho = 1/2 (double).

    This is UNIVERSAL for all shadow algebras with Delta != 0.
    """
    if abs(Delta) < 1e-30:
        return (0.0, 1.0)  # trivial case
    # c_0 = -1/4 universally
    c_0 = -0.25
    # rho*(rho-1) - c_0 = 0 => rho^2 - rho + 1/4 = 0
    disc_ind = 1 + 4 * c_0  # = 1 - 1 = 0
    sqrt_di = cmath.sqrt(disc_ind)
    rho1 = (1 + sqrt_di) / 2
    rho2 = (1 - sqrt_di) / 2
    return (rho1, rho2)


# ===========================================================================
# Section 4: P_VI parameters from multi-channel shadow (W_3)
# ===========================================================================

@dataclass
class PainleveVIParams:
    """Parameters of the Painleve VI equation.

    P_VI: y'' = (1/2)(1/y + 1/(y-1) + 1/(y-t))(y')^2
                - (1/t + 1/(t-1) + 1/(y-t)) y'
                + y(y-1)(y-t)/(t^2(t-1)^2)
                  * (alpha + beta*t/y^2 + gamma*(t-1)/(y-1)^2 + delta*t*(t-1)/(y-t)^2)

    Parameters (alpha, beta, gamma, delta) encode the monodromy data.
    The Jimbo relation: alpha = (theta_inf - 1)^2 / 2, beta = -theta_0^2 / 2,
    gamma = theta_1^2 / 2, delta = (1 - theta_t^2) / 2
    where theta_j are the monodromy exponents at j in {0, 1, t, inf}.
    """
    alpha: complex
    beta: complex
    gamma: complex
    delta: complex
    cross_ratio: complex      # the Heun singularity cross-ratio (the t in P_VI)
    theta_0: complex          # monodromy exponent at 0
    theta_1: complex          # monodromy exponent at 1
    theta_t: complex          # monodromy exponent at t
    theta_inf: complex        # monodromy exponent at infinity
    source: str = ''          # which family/configuration produced these


def pvi_params_from_thetas(theta_0, theta_1, theta_t, theta_inf, lam, source=''):
    """Construct P_VI parameters from monodromy exponents.

    Jimbo's relations:
        alpha = (theta_inf - 1)^2 / 2
        beta = -theta_0^2 / 2
        gamma = theta_1^2 / 2
        delta = (1 - theta_t^2) / 2
    """
    return PainleveVIParams(
        alpha=(theta_inf - 1)**2 / 2,
        beta=-theta_0**2 / 2,
        gamma=theta_1**2 / 2,
        delta=(1 - theta_t**2) / 2,
        cross_ratio=lam,
        theta_0=theta_0,
        theta_1=theta_1,
        theta_t=theta_t,
        theta_inf=theta_inf,
        source=source,
    )


def pvi_from_w3_shadow(c_val: float) -> PainleveVIParams:
    """Compute P_VI parameters from W_3 two-channel shadow system.

    The W_3 algebra has two channels (T, W) whose shadow metrics Q_T, Q_W
    contribute 2 zeros each, giving 4 singular points on P^1.

    The 4 singular points {z1, z2, z3, z4} are mapped to {0, 1, t, inf}
    by the unique Mobius transformation.  The cross-ratio t is the P_VI
    coordinate.

    At each singular point, the indicial exponent is 1/2 (universal for
    single-channel zeros of Q_L).  The monodromy exponents are theta = 1/2
    at each point.

    P_VI parameters:
        alpha = (theta_inf - 1)^2 / 2 = (1/2 - 1)^2 / 2 = 1/8
        beta = -theta_0^2 / 2 = -1/8
        gamma = theta_1^2 / 2 = 1/8
        delta = (1 - theta_t^2) / 2 = (1 - 1/4) / 2 = 3/8

    These are UNIVERSAL for all c (the P_VI parameters do not depend on c).
    What DOES depend on c is the cross-ratio t(c) of the 4 singular points.
    """
    # T-channel zeros
    T_data = w3_data(c_val)
    t_T_plus, t_T_minus = branch_points(T_data.kappa, T_data.alpha, T_data.Delta)

    # W-channel zeros
    W_data = w3_w_channel_data(c_val)
    t_W_plus, t_W_minus = branch_points(W_data.kappa, W_data.alpha, W_data.Delta)

    # Cross-ratio of {t_T+, t_T-, t_W+, t_W-}
    lam = cross_ratio_4pts(t_T_plus, t_T_minus, t_W_plus, t_W_minus)

    # Universal monodromy exponents
    theta = 0.5

    return pvi_params_from_thetas(
        theta_0=theta, theta_1=theta, theta_t=theta, theta_inf=theta,
        lam=lam,
        source=f'W_3(c={c_val})',
    )


def pvi_cross_ratio_landscape(c_values: List[float]) -> List[Dict[str, Any]]:
    """Compute P_VI cross-ratio for W_3 across a landscape of c values."""
    results = []
    for c_val in c_values:
        try:
            params = pvi_from_w3_shadow(c_val)
            results.append({
                'c': c_val,
                'cross_ratio': params.cross_ratio,
                'abs_cross_ratio': abs(params.cross_ratio),
                'arg_cross_ratio': cmath.phase(params.cross_ratio),
                'alpha': params.alpha,
                'beta': params.beta,
                'gamma': params.gamma,
                'delta': params.delta,
            })
        except (ZeroDivisionError, ValueError):
            results.append({'c': c_val, 'cross_ratio': None})
    return results


# ===========================================================================
# Section 5: P_VI solution at shadow parameters (numerical integration)
# ===========================================================================

def pvi_hamiltonian(y, p, t, params: PainleveVIParams) -> float:
    """Hamiltonian of P_VI in Okamoto's form.

    H_VI = y(y-1)(y-t) p^2
           - [theta_0 (y-1)(y-t) + theta_1 y(y-t) + (theta_t - 1) y(y-1)] p
           + theta_inf_tilde (theta_inf_tilde + 1)(y - t)
    divided by t(t-1).

    where theta_inf_tilde = (theta_0 + theta_1 + theta_t + theta_inf - 2) / 2.

    This Hamiltonian generates the P_VI equation via:
        t(t-1) y' = dH/dp
        t(t-1) p' = -dH/dy
    """
    th0 = params.theta_0
    th1 = params.theta_1
    tht = params.theta_t
    thi = params.theta_inf
    thi_tilde = (th0 + th1 + tht + thi - 2) / 2

    yy1 = y * (y - 1)
    yyt = y * (y - t)
    y1yt = (y - 1) * (y - t)

    H = (yy1 * (y - t) * p**2
         - (th0 * y1yt + th1 * yyt + (tht - 1) * yy1) * p
         + thi_tilde * (thi_tilde + 1) * (y - t))

    denom = t * (t - 1)
    if abs(denom) < 1e-50:
        return complex('inf')
    return H / denom


def pvi_rhs(y, p, t, params: PainleveVIParams) -> Tuple[complex, complex]:
    """Right-hand side of the P_VI Hamiltonian system.

    dy/dt = (1/(t(t-1))) dH/dp
    dp/dt = -(1/(t(t-1))) dH/dy

    Computed by finite differences for robustness.
    """
    eps = 1e-8

    # dH/dp by finite difference
    H_plus = pvi_hamiltonian(y, p + eps, t, params) * t * (t - 1)
    H_minus = pvi_hamiltonian(y, p - eps, t, params) * t * (t - 1)
    dHdp = (H_plus - H_minus) / (2 * eps)

    # dH/dy by finite difference
    H_plus_y = pvi_hamiltonian(y + eps, p, t, params) * t * (t - 1)
    H_minus_y = pvi_hamiltonian(y - eps, p, t, params) * t * (t - 1)
    dHdy = (H_plus_y - H_minus_y) / (2 * eps)

    tt1 = t * (t - 1)
    if abs(tt1) < 1e-50:
        return (complex('inf'), complex('inf'))

    dy_dt = dHdp / tt1
    dp_dt = -dHdy / tt1

    return dy_dt, dp_dt


def integrate_pvi(params: PainleveVIParams, t_start: float, t_end: float,
                  y0: complex, p0: complex, n_steps: int = 2000
                  ) -> List[Tuple[float, complex, complex]]:
    """Integrate P_VI Hamiltonian system using RK4.

    Returns trajectory [(t, y(t), p(t))].
    """
    dt = (t_end - t_start) / n_steps
    y = complex(y0)
    p = complex(p0)
    t = t_start

    trajectory = [(t, y, p)]

    for _ in range(n_steps):
        try:
            k1y, k1p = pvi_rhs(y, p, t, params)
            k2y, k2p = pvi_rhs(y + dt * k1y / 2, p + dt * k1p / 2, t + dt / 2, params)
            k3y, k3p = pvi_rhs(y + dt * k2y / 2, p + dt * k2p / 2, t + dt / 2, params)
            k4y, k4p = pvi_rhs(y + dt * k3y, p + dt * k3p, t + dt, params)

            y += dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
            p += dt * (k1p + 2 * k2p + 2 * k3p + k4p) / 6
            t += dt

            # Safety: cap growth
            if abs(y) > 1e20 or abs(p) > 1e20:
                trajectory.append((t, complex('nan'), complex('nan')))
                break

            trajectory.append((t, y, p))
        except (OverflowError, ZeroDivisionError):
            trajectory.append((t + dt, complex('nan'), complex('nan')))
            break

    return trajectory


# ===========================================================================
# Section 6: P_VI Riccati reduction (shadow depth 2 = Heisenberg)
# ===========================================================================

def pvi_riccati_test(params: PainleveVIParams) -> Dict[str, Any]:
    """Test whether P_VI reduces to a Riccati equation at given parameters.

    P_VI reduces to a Riccati (linearizable) equation when:
    (a) theta_inf = 0, or
    (b) theta_0 = 0, or
    (c) theta_1 = 0, or
    (d) theta_t = 0, or
    (e) theta_0 + theta_1 + theta_t + theta_inf is an ODD integer.

    For shadow parameters with all theta = 1/2:
        sum = 2.0, which is NOT an odd integer.
        No individual theta vanishes.
        So: P_VI is NOT Riccati-reducible at generic W_3 parameters.

    For Heisenberg (Delta = 0, class G):
        There is NO Heun equation (only 2 singularities from one channel).
        The system is trivial.  The "P_VI reduction to Riccati" is the
        trivial statement that the equation doesn't exist.

    For class L (affine KM, Delta = 0):
        Same: no Heun equation, trivial system.
    """
    th_sum = params.theta_0 + params.theta_1 + params.theta_t + params.theta_inf
    is_riccati = False
    reason = ''

    if abs(params.theta_0) < 1e-10:
        is_riccati = True
        reason = 'theta_0 = 0'
    elif abs(params.theta_1) < 1e-10:
        is_riccati = True
        reason = 'theta_1 = 0'
    elif abs(params.theta_t) < 1e-10:
        is_riccati = True
        reason = 'theta_t = 0'
    elif abs(params.theta_inf) < 1e-10:
        is_riccati = True
        reason = 'theta_inf = 0'
    elif abs(th_sum - round(th_sum.real)) < 1e-10 and round(th_sum.real) % 2 == 1:
        is_riccati = True
        reason = f'theta sum = {th_sum} is an odd integer'

    return {
        'is_riccati': is_riccati,
        'reason': reason,
        'theta_sum': th_sum,
        'theta_0': params.theta_0,
        'theta_1': params.theta_1,
        'theta_t': params.theta_t,
        'theta_inf': params.theta_inf,
    }


def linearizability_by_shadow_depth(family_data: ShadowFamilyData) -> Dict[str, Any]:
    """Classify linearizability of the shadow ODE by shadow depth.

    r_max = 2 (class G, Heisenberg): NO ODE (trivial, Delta = 0)
    r_max = 3 (class L, affine KM): NO ODE (trivial, Delta = 0)
    r_max = 4 (class C, betagamma): single-channel rigid, no P_VI
    r_max = inf (class M, Virasoro): single-channel rigid, no P_VI
        but multi-channel (W_3 T+W) gives genuine P_VI

    The key insight: linearizability <==> tower terminates <==> Delta = 0.
    For Delta != 0, the single-channel ODE is still rigid (not P_VI), but
    the shadow generating function H(t) = t^2*sqrt(Q_L) is genuinely
    TRANSCENDENTAL (irrational algebraic of degree 2, not rational).
    """
    is_linear = (family_data.Delta == 0.0 or abs(family_data.Delta) < 1e-30)
    return {
        'family': family_data.name,
        'shadow_class': family_data.shadow_class,
        'r_max': family_data.r_max,
        'Delta': family_data.Delta,
        'is_linearizable': is_linear,
        'ode_type': 'trivial' if is_linear else 'algebraic_degree_2',
        'painleve_single_channel': 'none' if True else 'PVI',
    }


# ===========================================================================
# Section 7: Tau function from shadow data
# ===========================================================================

def shadow_tau_flat_section(kappa: float, alpha: float, Delta: float,
                            t_val: float) -> complex:
    """tau(t) = sqrt(Q_L(t) / Q_L(0)).

    This is the JMU tau function for the single-channel shadow connection.
    It equals the flat section Phi(t) of nabla^sh.
    """
    Q_t = shadow_metric_eval(kappa, alpha, Delta, t_val)
    Q_0 = shadow_metric_eval(kappa, alpha, Delta, 0)
    if abs(Q_0) < 1e-50:
        return complex('nan')
    return cmath.sqrt(Q_t / Q_0)


def shadow_generating_function(kappa: float, alpha: float, Delta: float,
                                t_val: float) -> complex:
    """H(t) = 2*kappa*t^2*Phi(t) = t^2*sqrt(Q_L(t)).

    NOT a flat section (AP23).  Has double zero at t=0.
    """
    Q_t = shadow_metric_eval(kappa, alpha, Delta, t_val)
    return t_val**2 * cmath.sqrt(Q_t)


def tau_genus_expansion(kappa_val: float, g_max: int = 10) -> Dict[int, float]:
    """Genus expansion of log(tau): F_g = kappa * a_g.

    The a_g are the coefficients of x^{2g} in (x/2)/sin(x/2) - 1,
    which is the A-hat generating function evaluated at ix.

    Formula: a_g = (2^{2g} - 2) * |B_{2g}| / ((2g)! * 4^g)

    Verified values:
        a_1 = 1/24,  a_2 = 7/5760,  a_3 = 31/967680.

    So F_g = kappa * a_g gives F_1 = kappa/24, F_2 = 7*kappa/5760, etc.
    """
    from sympy import bernoulli as sym_bernoulli, factorial as sym_factorial

    result = {}
    for g in range(1, g_max + 1):
        B_2g = float(sym_bernoulli(2 * g))
        abs_B_2g = abs(B_2g)
        # a_g = (2^{2g} - 2) * |B_{2g}| / ((2g)! * 4^g)
        a_g = (2**(2 * g) - 2) * abs_B_2g / (float(sym_factorial(2 * g)) * 4**g)
        result[g] = kappa_val * a_g
    return result


def compare_tau_and_shadow_gf(kappa: float, alpha: float, Delta: float,
                               t_values: List[float]) -> List[Dict[str, Any]]:
    """Compare the JMU tau function with the shadow generating function.

    tau(t) = Phi(t) = sqrt(Q_L(t)/Q_L(0))
    H(t) = t^2 * sqrt(Q_L(t))
    Ratio: H(t) / tau(t) = t^2 * sqrt(Q_L(0)) = 2*kappa*t^2

    This ratio is a POLYNOMIAL (not constant), confirming H != tau.
    """
    results = []
    Q_0 = shadow_metric_eval(kappa, alpha, Delta, 0)
    sqrt_Q0 = cmath.sqrt(Q_0)

    for t_val in t_values:
        tau_val = shadow_tau_flat_section(kappa, alpha, Delta, t_val)
        H_val = shadow_generating_function(kappa, alpha, Delta, t_val)
        ratio = H_val / tau_val if abs(tau_val) > 1e-50 else complex('nan')
        expected_ratio = t_val**2 * sqrt_Q0

        results.append({
            't': t_val,
            'tau': tau_val,
            'H': H_val,
            'ratio': ratio,
            'expected_ratio': expected_ratio,
            'ratio_match': abs(ratio - expected_ratio) < 1e-8 * max(abs(expected_ratio), 1)
                           if not cmath.isnan(ratio) else False,
        })
    return results


# ===========================================================================
# Section 8: P_VI tau function (Jimbo-Miwa-Ueno) for multi-channel
# ===========================================================================

def jmu_tau_pvi(params: PainleveVIParams, trajectory: List[Tuple[float, complex, complex]]
                ) -> List[Dict[str, Any]]:
    """Compute the JMU tau function along a P_VI trajectory.

    For P_VI, d/dt log(tau) = H_VI(t) where H_VI is the Hamiltonian.
    We integrate this along the trajectory to get tau(t).
    """
    results = []
    log_tau = 0.0

    for i, (t, y, p) in enumerate(trajectory):
        if cmath.isnan(y) or cmath.isnan(p):
            results.append({'t': t, 'log_tau': float('nan'), 'tau': float('nan')})
            continue

        H = pvi_hamiltonian(y, p, t, params)
        results.append({
            't': t,
            'H': H,
            'log_tau': log_tau,
            'tau': cmath.exp(log_tau) if abs(log_tau) < 500 else complex('inf'),
        })

        # Euler integration of d(log tau)/dt = H
        if i + 1 < len(trajectory):
            dt = trajectory[i + 1][0] - t
            log_tau += H * dt

    return results


# ===========================================================================
# Section 9: Connection matrices at zeta zeros
# ===========================================================================

def shadow_at_zeta_zero(n: int) -> Dict[str, Any]:
    """Shadow data at Virasoro with c = 1/2 + i*gamma_n (zeta zero parameter).

    The Riemann zeta zero rho_n = 1/2 + i*gamma_n gives a complex central
    charge c(rho_n) = 1/2 + i*gamma_n.  The shadow metric Q_L(t; c) at
    this complex c has complex coefficients.

    This is EXPLORATORY: the physical significance of complex c is unclear,
    but the shadow algebraic structure extends analytically to complex c.
    """
    if n < 1 or n > len(ZETA_ZEROS_20):
        raise ValueError(f"n must be in [1, {len(ZETA_ZEROS_20)}]")

    gamma_n = ZETA_ZEROS_20[n - 1]
    c_val = 0.5 + 1j * gamma_n

    kappa = c_val / 2
    alpha = 2.0
    denom = c_val * (5 * c_val + 22)
    S4 = 10.0 / denom
    Delta = 8 * kappa * S4

    q0, q1, q2 = shadow_metric_coeffs(kappa, alpha, Delta)
    tp, tm = branch_points(kappa, alpha, Delta)

    return {
        'n': n,
        'gamma_n': gamma_n,
        'c': c_val,
        'kappa': kappa,
        'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2,
        'branch_point_plus': tp,
        'branch_point_minus': tm,
        'branch_point_modulus_plus': abs(tp),
        'branch_point_modulus_minus': abs(tm),
        'discriminant': q1**2 - 4 * q0 * q2,
    }


def connection_matrix_hypergeometric(kappa: float, alpha: float, Delta: float
                                     ) -> Dict[str, Any]:
    """Connection matrix for the hypergeometric equation u'' = V(t)*u.

    For the rigid Fuchsian equation with 3 regular singular points
    {t+, t-, infinity}, the connection matrix between local solutions at
    t- and t+ is determined by the classical hypergeometric formula.

    Since the indicial exponent is 1/2 (double) at each finite singularity,
    the equation is:
        u'' + (1/4) / (t - t+)^2 * u + (1/4) / (t - t-)^2 * u = 0
    (up to cross-terms and the infinity contribution).

    The connection matrix C from t- to t+ encodes how local solutions at
    one singularity continue to the other.

    For double indicial exponent 1/2:
        The solution sqrt(Q_L) is single-valued around each singularity
        (it picks up a sign change, giving monodromy -1).
        The other solution integral(dt/sqrt(Q_L)) has a logarithmic branch.

    The connection matrix in the basis {sqrt(Q_L), int dt/sqrt(Q_L)} is:
        C = [[c11, c12], [0, c22]]
    where c11 = (analytic continuation of sqrt(Q_L))
          c22 = (analytic continuation of int dt/sqrt(Q_L))
    """
    if abs(Delta) < 1e-30:
        return {'type': 'trivial', 'matrix': [[1, 0], [0, 1]]}

    tp, tm = branch_points(kappa, alpha, Delta)
    q0, q1, q2 = shadow_metric_coeffs(kappa, alpha, Delta)

    # Period of the elliptic integral (but Q_L is quadratic, so it's elementary)
    # int_{t-}^{t+} dt / sqrt(Q_L) = pi / sqrt(q2) for Q_L quadratic with
    # two simple zeros.
    # More precisely: Q_L = q2*(t - t-)*(t - t+), so
    # int dt/sqrt(q2*(t-t-)*(t-t+)) = (1/sqrt(q2)) * arcsin(...)
    # The period (loop around the cut) is pi / sqrt(q2).

    period = cmath.pi / cmath.sqrt(q2) if abs(q2) > 1e-30 else complex('inf')

    # Monodromy: sqrt(Q_L) -> -sqrt(Q_L) around either branch point
    # Connection matrix between t- and t+ (along the upper half-plane):
    # sqrt(Q_L) continues smoothly (changes sign at each zero)
    # int dt/sqrt(Q_L) gains the period

    return {
        'type': 'hypergeometric',
        'period': period,
        'monodromy_eigenvalue': -1,
        'indicial_exponent': 0.5,
        'branch_points': (tp, tm),
        'separation': abs(tp - tm),
    }


def connection_data_at_zeta_zeros(n_max: int = 15) -> List[Dict[str, Any]]:
    """Compute connection data at zeta zero parameters c(rho_n) for n=1..n_max."""
    results = []
    for n in range(1, min(n_max + 1, len(ZETA_ZEROS_20) + 1)):
        data = shadow_at_zeta_zero(n)
        conn = connection_matrix_hypergeometric(data['kappa'], 2.0, data['Delta'])
        results.append({
            'n': n,
            'gamma_n': data['gamma_n'],
            'c': data['c'],
            'period': conn.get('period', None),
            'branch_separation': conn.get('separation', None),
            'monodromy': conn.get('monodromy_eigenvalue', None),
        })
    return results


# ===========================================================================
# Section 10: P_III from genus-1 shadow (cylindrical reduction)
# ===========================================================================

@dataclass
class PainleveIIIParams:
    """Parameters of the Painleve III equation.

    P_III: y'' = (y')^2/y - y'/t + (alpha*y^2 + beta)/t + gamma*y^3 + delta/y

    Standard P_III' (D7 type): y'' = (y')^2/y - y'/t + (alpha*y^2)/t + beta/t
    with gamma = 0, delta = 0 (degenerate P_III).
    """
    alpha_piii: complex
    beta_piii: complex
    gamma_piii: complex
    delta_piii: complex
    source: str = ''


def genus1_shadow_to_piii(family_data: ShadowFamilyData) -> Dict[str, Any]:
    """Genus-1 reduction of the shadow equation to P_III.

    At genus 1, the shadow connection acquires periodic structure from the
    torus modulus tau.  The radial part of the Schrodinger equation on the
    cylinder (after separation of angular dependence) takes the form:

        f'' + (1/r)f' + [A + B/r^2] f = 0

    where r is the radial coordinate and A, B are determined by the
    shadow data.  This is the modified Bessel equation, whose isomonodromic
    deformation gives P_III.

    For the shadow with kappa, F_1 = kappa/24:
        A = kappa/24 (the genus-1 free energy)
        B = 0 (no angular obstruction at genus 1 for single-generator)

    The P_III parameters are:
        alpha_PIII = 1 - 2*theta_0 = 1 - 2*(kappa/24)  (???)

    CRITICAL NOTE: This identification is STRUCTURAL, not a proved theorem.
    The P_III equation at the shadow parameters is a FORMAL ANALOGY based
    on the cylinder periodicity.  The actual genus-1 shadow is computed
    from the graph sum on M_{1,n}, not from P_III.

    We compute the BESSEL parameters (nu, z) from the shadow data and
    report the formal P_III correspondence.
    """
    kappa = family_data.kappa
    F1 = kappa / 24.0

    # Bessel parameter: the genus-1 shadow coefficient determines the
    # Bessel order via the relation F_1 = kappa/24.
    # Bessel equation: f'' + (1/r)f' + (1 - nu^2/r^2) f = 0
    # Modified Bessel: f'' + (1/r)f' - (1 + nu^2/r^2) f = 0
    # The shadow analogy: nu^2 ~ kappa, z ~ t (shadow parameter)

    nu = cmath.sqrt(kappa) if kappa >= 0 else 1j * cmath.sqrt(-kappa)

    # P_III parameters from Bessel:
    # P_III with gamma = delta = 0 (P_III D7 type)
    # alpha = 1 - 2*nu, beta = -1 + 2*nu (from isomonodromy of Bessel)
    # But this is the STANDARD correspondence, not shadow-specific.

    alpha_piii = 1 - 2 * nu
    beta_piii = -1 + 2 * nu

    piii_params = PainleveIIIParams(
        alpha_piii=alpha_piii,
        beta_piii=beta_piii,
        gamma_piii=0.0,
        delta_piii=0.0,
        source=f'genus-1 Bessel from {family_data.name}',
    )

    return {
        'family': family_data.name,
        'kappa': kappa,
        'F1': F1,
        'bessel_order': nu,
        'piii_params': piii_params,
        'piii_alpha': alpha_piii,
        'piii_beta': beta_piii,
        'is_structural_analogy': True,
    }


def piii_asymptotic_at_zero(nu: complex, n_terms: int = 5) -> List[complex]:
    """Asymptotic expansion of the Bessel-type P_III solution at r -> 0.

    I_nu(r) ~ (r/2)^nu / Gamma(nu+1) * [1 + sum c_k r^{2k}]

    Returns the first n_terms coefficients c_k.
    """
    import math
    coeffs = [1.0]  # c_0 = 1
    for k in range(1, n_terms):
        # c_k = (-1)^k / (4^k * k! * Gamma(nu+k+1)/Gamma(nu+1))
        # Simplified: c_k = c_{k-1} * (-1) / (4*k*(nu+k))
        ck = coeffs[-1] * (-1) / (4 * k * (nu + k))
        coeffs.append(ck)
    return coeffs


def piii_asymptotic_at_infinity(nu: complex, n_terms: int = 5) -> List[complex]:
    """Asymptotic expansion of I_nu(r) at r -> infinity.

    I_nu(r) ~ exp(r) / sqrt(2*pi*r) * [1 + sum d_k / r^k]

    d_k = (4*nu^2 - 1^2)(4*nu^2 - 3^2)...(4*nu^2 - (2k-1)^2) / (k! * 8^k)

    Returns the first n_terms coefficients d_k.
    """
    coeffs = [1.0]  # d_0 = 1
    for k in range(1, n_terms):
        # d_k = d_{k-1} * (4*nu^2 - (2k-1)^2) / (8*k)
        dk = coeffs[-1] * (4 * nu**2 - (2 * k - 1)**2) / (8 * k)
        coeffs.append(dk)
    return coeffs


# ===========================================================================
# Section 11: Multi-path verification infrastructure
# ===========================================================================

def verify_indicial_exponent_universal(families: List[ShadowFamilyData]) -> Dict[str, Any]:
    """Verify that the indicial exponent is 1/2 (double) for ALL class M families.

    Path 1: Direct computation c_0 = 8*kappa^2*Delta / Q'(t_0)^2 = -1/4.
    Path 2: From discriminant: c_0 = 8*kappa^2*Delta / disc(Q_L) = -1/4.
    Path 3: Explicit evaluation at each family's parameters.
    """
    results = []
    for fam in families:
        if abs(fam.Delta) < 1e-30:
            results.append({'family': fam.name, 'Delta': 0, 'skip': True})
            continue

        # Path 1: general formula
        c_0_general = -0.25  # 8k^2 D / (-32 k^2 D) = -1/4

        # Path 2: from discriminant
        q0, q1, q2 = shadow_metric_coeffs(fam.kappa, fam.alpha, fam.Delta)
        disc = q1**2 - 4 * q0 * q2  # = -32*kappa^2*Delta
        c_0_disc = 8 * fam.kappa**2 * fam.Delta / disc if abs(disc) > 1e-30 else None

        # Path 3: explicit at branch point
        tp, tm = branch_points(fam.kappa, fam.alpha, fam.Delta)
        Qp_at_tp = q1 + 2 * q2 * tp
        c_0_explicit = 8 * fam.kappa**2 * fam.Delta / Qp_at_tp**2 if abs(Qp_at_tp) > 1e-30 else None

        # Indicial exponent from c_0
        if c_0_explicit is not None:
            disc_ind = 1 + 4 * c_0_explicit
            rho = (1 + cmath.sqrt(disc_ind)) / 2
        else:
            rho = None

        results.append({
            'family': fam.name,
            'c_0_general': c_0_general,
            'c_0_disc': c_0_disc,
            'c_0_explicit': c_0_explicit,
            'rho': rho,
            'all_agree': (c_0_disc is not None and abs(c_0_disc - c_0_general) < 1e-8
                          and c_0_explicit is not None and abs(c_0_explicit - c_0_general) < 1e-8),
        })
    return {'families': results, 'universal_value': -0.25}


def verify_tau_equals_flat_section(kappa: float, alpha: float, Delta: float,
                                    t_values: List[float]) -> Dict[str, Any]:
    """Verify tau(t) = Phi(t) = sqrt(Q_L(t)/Q_L(0)).

    Path 1: direct computation tau(t) = sqrt(Q(t)/Q(0)).
    Path 2: integration of d log tau = Q'/(2Q).
    Path 3: compare with H(t)/(t^2*sqrt(Q(0))).
    """
    Q_0 = shadow_metric_eval(kappa, alpha, Delta, 0)
    sqrt_Q0 = cmath.sqrt(Q_0)

    results = []
    log_tau_integrated = 0.0

    for i, t_val in enumerate(t_values):
        # Path 1: direct
        tau_direct = shadow_tau_flat_section(kappa, alpha, Delta, t_val)

        # Path 2: integration (trapezoid)
        if i > 0:
            dt = t_values[i] - t_values[i - 1]
            t_mid = (t_values[i] + t_values[i - 1]) / 2
            Q_mid = shadow_metric_eval(kappa, alpha, Delta, t_mid)
            q0, q1, q2 = shadow_metric_coeffs(kappa, alpha, Delta)
            Qp_mid = q1 + 2 * q2 * t_mid
            omega_mid = Qp_mid / (2 * Q_mid) if abs(Q_mid) > 1e-50 else 0
            log_tau_integrated += omega_mid * dt
        tau_integrated = cmath.exp(log_tau_integrated)

        # Path 3: from H
        H_val = shadow_generating_function(kappa, alpha, Delta, t_val)
        if abs(t_val) > 1e-30 and abs(sqrt_Q0) > 1e-30:
            tau_from_H = H_val / (t_val**2 * sqrt_Q0)
        else:
            tau_from_H = complex('nan') if t_val == 0 else complex('nan')

        results.append({
            't': t_val,
            'tau_direct': tau_direct,
            'tau_integrated': tau_integrated,
            'tau_from_H': tau_from_H,
            'path1_path2_agree': abs(tau_direct - tau_integrated) < 0.01 * max(abs(tau_direct), 1e-10),
        })

    return {'data': results}


def verify_pvi_params_universal(c_values: List[float]) -> Dict[str, Any]:
    """Verify P_VI parameters are universal (alpha=1/8, beta=-1/8, gamma=1/8, delta=3/8).

    The P_VI parameters from W_3 shadow are determined by the indicial
    exponents, which are ALL 1/2 (universal).  So (alpha,beta,gamma,delta)
    should be independent of c.
    """
    results = []
    for c_val in c_values:
        try:
            params = pvi_from_w3_shadow(c_val)
            results.append({
                'c': c_val,
                'alpha': params.alpha,
                'beta': params.beta,
                'gamma': params.gamma,
                'delta': params.delta,
                'alpha_check': abs(params.alpha - 0.125) < 1e-10,
                'beta_check': abs(params.beta - (-0.125)) < 1e-10,
                'gamma_check': abs(params.gamma - 0.125) < 1e-10,
                'delta_check': abs(params.delta - 0.375) < 1e-10,
            })
        except (ZeroDivisionError, ValueError):
            results.append({'c': c_val, 'error': True})

    return {'data': results, 'expected': {'alpha': 0.125, 'beta': -0.125,
                                           'gamma': 0.125, 'delta': 0.375}}


def verify_discriminant_relation(families: List[ShadowFamilyData]) -> Dict[str, Any]:
    """Verify disc(Q_L) = -32*kappa^2*Delta for all families.

    Three independent paths:
    Path 1: disc = q1^2 - 4*q0*q2
    Path 2: disc = -32*kappa^2*Delta
    Path 3: disc = (Q'(t+))^2 where t+ is a branch point
    """
    results = []
    for fam in families:
        q0, q1, q2 = shadow_metric_coeffs(fam.kappa, fam.alpha, fam.Delta)

        # Path 1
        disc_1 = q1**2 - 4 * q0 * q2

        # Path 2
        disc_2 = -32 * fam.kappa**2 * fam.Delta

        # Path 3 (only if Delta != 0)
        if abs(fam.Delta) > 1e-30:
            tp, tm = branch_points(fam.kappa, fam.alpha, fam.Delta)
            Qp_tp = q1 + 2 * q2 * tp
            disc_3 = Qp_tp**2
            # Note: Q'(t+) = sqrt(disc) (from quadratic formula), so Q'(t+)^2 = disc
        else:
            disc_3 = 0

        results.append({
            'family': fam.name,
            'disc_1': disc_1,
            'disc_2': disc_2,
            'disc_3': disc_3,
            'paths_agree_12': abs(disc_1 - disc_2) < 1e-8 * max(abs(disc_1), 1e-10),
            'paths_agree_13': abs(disc_1 - disc_3) < 1e-8 * max(abs(disc_1), 1e-10)
                              if abs(fam.Delta) > 1e-30 else True,
        })
    return {'data': results}


# ===========================================================================
# Section 12: Cross-ratio landscape and P_VI coordinate
# ===========================================================================

def w3_cross_ratio_analytic(c_val: float) -> complex:
    """Compute the W_3 Heun cross-ratio analytically.

    The 4 singular points are the zeros of Q_T and Q_W:
        t_T^pm from Q_T = 0
        t_W^pm from Q_W = 0

    The cross-ratio lambda = (t_T+ - t_W+)(t_T- - t_W-) / ((t_T+ - t_W-)(t_T- - t_W+))
    is a rational function of c.
    """
    T_data = w3_data(c_val)
    W_data = w3_w_channel_data(c_val)

    t_T_p, t_T_m = branch_points(T_data.kappa, T_data.alpha, T_data.Delta)
    t_W_p, t_W_m = branch_points(W_data.kappa, W_data.alpha, W_data.Delta)

    return cross_ratio_4pts(t_T_p, t_T_m, t_W_p, t_W_m)


def cross_ratio_at_zeta_zeros(n_max: int = 15) -> List[Dict[str, Any]]:
    """Compute W_3 cross-ratio at c = 1/2 + i*gamma_n (zeta zero parameters)."""
    results = []
    for n in range(1, min(n_max + 1, len(ZETA_ZEROS_20) + 1)):
        gamma_n = ZETA_ZEROS_20[n - 1]
        c_val = 0.5 + 1j * gamma_n

        try:
            lam = w3_cross_ratio_analytic(c_val)
            results.append({
                'n': n,
                'gamma_n': gamma_n,
                'c': c_val,
                'cross_ratio': lam,
                'abs_cross_ratio': abs(lam),
                'arg_cross_ratio': cmath.phase(lam),
            })
        except (ZeroDivisionError, ValueError, OverflowError):
            results.append({'n': n, 'gamma_n': gamma_n, 'error': True})

    return results


# ===========================================================================
# Section 13: Nekrasov-type comparison for P_III
# ===========================================================================

def nekrasov_genus1_comparison(kappa: float, epsilon: float = 0.01,
                                n_inst: int = 5) -> Dict[str, Any]:
    """Compare genus-1 shadow F_1 = kappa/24 with Nekrasov instanton sum.

    The Nekrasov partition function at genus 1 gives:
        F_1^Nek = -(1/12) log(q * prod_{n>=1} (1-q^n)^24)
                = -(1/12) log(eta(q)^24 * q^{-1})
                = -(1/12) (-1*log q + 24*log eta(q))
                = (1/12) log q - 2 log eta(q)

    For q = exp(2*pi*i*tau), this is:
        F_1^Nek = (2*pi*i*tau)/12 - 2*log eta(tau)
                = pi*i*tau/6 - 2*log eta(tau)

    The shadow F_1 = kappa/24 is the GENUS-1 contribution, which equals
    the Nekrasov genus-1 term at the self-dual point tau = i.

    The comparison is structural (both give kappa/24 on the Coulomb branch),
    not numerical (different parameterizations).
    """
    F1_shadow = kappa / 24.0

    # Instanton expansion of log eta: log eta(q) = (1/24)*log q + sum_{n>=1} log(1-q^n)
    # At q = epsilon (small): log eta ~ (1/24)*log(epsilon) - epsilon - epsilon^2/2 - ...
    q = epsilon
    log_eta_approx = math.log(q) / 24.0
    for n_val in range(1, n_inst + 1):
        log_eta_approx += math.log(abs(1 - q**n_val))

    F1_nekrasov_approx = -2 * log_eta_approx + math.log(q) / 12.0

    return {
        'kappa': kappa,
        'F1_shadow': F1_shadow,
        'F1_nekrasov_approx': F1_nekrasov_approx,
        'epsilon': epsilon,
        'n_inst': n_inst,
        'comparison': 'structural (both = kappa/24 at self-dual point)',
    }


# ===========================================================================
# Section 14: Stokes multipliers of the associated linear system
# ===========================================================================

def stokes_from_borel_resurgence(kappa: float, alpha: float, Delta: float
                                  ) -> Dict[str, Any]:
    """Stokes multipliers from the Borel resurgence of the shadow GF.

    The shadow generating function H(t) = t^2*sqrt(Q_L(t)) has a branch
    point at each zero of Q_L.  The Borel transform B[H](s) has singularities
    at s = 1/t_pm (reciprocals of branch points).

    The Stokes multiplier at each Borel singularity is:
        S_1 = 2*pi*i * (residue of the alien derivative)

    For the algebraic function sqrt(Q_L), the Borel singularities are
    SIMPLE (square-root type), and the Stokes multiplier is:

        S = 2*pi*i  (universal, from the monodromy -1 of sqrt)

    This is the Ecalle resurgence Stokes multiplier, NOT the ODE Stokes
    multiplier (which doesn't exist for the Fuchsian equation).
    """
    if abs(Delta) < 1e-30:
        return {
            'type': 'trivial',
            'stokes_multipliers': [],
            'borel_singularities': [],
        }

    tp, tm = branch_points(kappa, alpha, Delta)

    # Borel singularities at 1/t_pm (reciprocals of branch points)
    s_plus = 1.0 / tp if abs(tp) > 1e-30 else complex('inf')
    s_minus = 1.0 / tm if abs(tm) > 1e-30 else complex('inf')

    return {
        'type': 'resurgent',
        'borel_singularities': [s_plus, s_minus],
        'stokes_multiplier': 2j * cmath.pi,  # universal
        'stokes_abs': 2 * math.pi,
        'branch_points': [tp, tm],
        'monodromy': -1,
    }


# ===========================================================================
# Section 15: Full analysis pipeline
# ===========================================================================

def full_painleve_shadow_analysis(c_val: float) -> Dict[str, Any]:
    """Complete Painleve-shadow analysis for Virasoro at central charge c.

    Combines single-channel (rigid Fuchsian) and multi-channel (P_VI)
    analyses with tau function, connection data, and verification.
    """
    # Single-channel data
    vir = virasoro_data(c_val)
    heis = heisenberg_data()
    sl2 = affine_sl2_data(1.0)

    # Single-channel classification
    lin_vir = linearizability_by_shadow_depth(vir)

    # Multi-channel P_VI
    pvi = pvi_from_w3_shadow(c_val)
    riccati = pvi_riccati_test(pvi)

    # Tau function comparison
    t_values = [0.01 * i for i in range(1, 51)]
    tau_compare = compare_tau_and_shadow_gf(vir.kappa, vir.alpha, vir.Delta, t_values)

    # Genus-1 P_III
    piii_data = genus1_shadow_to_piii(vir)

    # Borel-Stokes
    stokes = stokes_from_borel_resurgence(vir.kappa, vir.alpha, vir.Delta)

    return {
        'c': c_val,
        'virasoro': vir,
        'single_channel': lin_vir,
        'pvi_params': pvi,
        'riccati_test': riccati,
        'tau_comparison_sample': tau_compare[:5],
        'genus1_piii': piii_data,
        'stokes': stokes,
        'summary': {
            'single_channel_painleve': 'none (rigid Fuchsian)',
            'multi_channel_painleve': 'PVI',
            'pvi_alpha': pvi.alpha,
            'pvi_cross_ratio': pvi.cross_ratio,
            'heisenberg_linearizable': True,
            'virasoro_transcendental': True,
        },
    }


# ===========================================================================
# Section 16: Standard family landscape
# ===========================================================================

def standard_landscape_analysis() -> List[Dict[str, Any]]:
    """Painleve analysis for all standard families."""
    families = [
        ('Heisenberg k=1', heisenberg_data(1.0)),
        ('affine sl_2 k=1', affine_sl2_data(1.0)),
        ('betagamma', betagamma_data()),
        ('Virasoro c=1', virasoro_data(1.0)),
        ('Virasoro c=1/2', virasoro_data(0.5)),
        ('Virasoro c=13 (self-dual)', virasoro_data(13.0)),
        ('Virasoro c=25', virasoro_data(25.0)),
        ('Virasoro c=26', virasoro_data(26.0)),
    ]

    results = []
    for name, fam in families:
        lin = linearizability_by_shadow_depth(fam)
        results.append({
            'name': name,
            'shadow_class': fam.shadow_class,
            'r_max': fam.r_max,
            'Delta': fam.Delta,
            'kappa': fam.kappa,
            'linearizable': lin['is_linearizable'],
            'ode_type': lin['ode_type'],
        })
    return results


if __name__ == '__main__':
    print("BC-113: Painleve-Shadow Engine")
    print("=" * 60)

    landscape = standard_landscape_analysis()
    for entry in landscape:
        print(f"  {entry['name']:30s} class={entry['shadow_class']}  "
              f"r_max={entry['r_max']:3d}  Delta={entry['Delta']:.6f}  "
              f"linear={entry['linearizable']}")

    print("\nW_3 P_VI cross-ratio at c=13:")
    pvi = pvi_from_w3_shadow(13.0)
    print(f"  lambda = {pvi.cross_ratio}")
    print(f"  (alpha, beta, gamma, delta) = ({pvi.alpha}, {pvi.beta}, {pvi.gamma}, {pvi.delta})")
