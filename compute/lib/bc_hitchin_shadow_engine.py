r"""BC-98: Hitchin system spectral curves from shadow data.

MATHEMATICAL FRAMEWORK
======================

The Hitchin system on a curve X with gauge group G has spectral curve
Sigma subset T*X defined by the characteristic polynomial of the Higgs
field phi.  The shadow programme's data (kappa, S_3, S_4, ...) encodes
a spectral curve in the Hitchin base.

1. SHADOW HITCHIN SPECTRAL CURVE
   For sl_2, the Hitchin spectral curve is eta^2 + phi_2(z) = 0 where
   phi_2 in H^0(X, K^2).  The shadow identification: phi_2 = kappa * omega
   where omega is the canonical class.

   For sl_N: det(eta - Phi) = 0 gives
   eta^N + phi_2 eta^{N-2} + phi_3 eta^{N-3} + ... + phi_N = 0.
   Shadow identification: phi_r = S_r(A) * omega^r (shadow coefficient
   IS the r-th Hitchin differential).

2. HITCHIN BASE AND SHADOW LOCUS
   The Hitchin base B = oplus_{j=2}^N H^0(X, K^j).  The shadow tower
   gives a map Hit: A -> (S_2, S_3, ..., S_N) in B.

3. DISCRIMINANT
   The discriminant locus D subset B where the spectral curve degenerates:
   - sl_2: D = {phi_2 = 0}, i.e., kappa = 0.
   - sl_3: D = {4 phi_2^3 + 27 phi_3^2 = 0}.

4. WKB AND SHADOW CONNECTION
   The Hitchin system's Abelian differentials give the WKB approximation
   to flat sections of nabla^sh = d - Q'/(2Q) dt.

5. HITCHIN FIBRATION
   Over a generic point b in B, the Hitchin fiber is the Jacobian of the
   spectral curve Sigma_b.  The shadow fiber Jac(Sigma_A) has dimension
   = genus(Sigma_A), computed via Riemann-Hurwitz.

6. STOKES GRAPH
   The Stokes graph of the spectral curve (WKB diagram) has edges where
   Re(int P dz) = 0.  These are the BPS rays.

7. OPERS
   The Hitchin section picks out opers.  For sl_2: psi'' + phi_2 psi = 0.
   The shadow oper: psi'' + kappa omega psi = 0.

VERIFICATION PATHS:
    Path 1: Hitchin discriminant = shadow discriminant Delta (independent)
    Path 2: WKB approximation matches flat section of nabla^sh
    Path 3: Genus of spectral curve from Riemann-Hurwitz vs topology
    Path 4: Stokes graph topology
    Path 5: Oper monodromy from spectral curve vs direct ODE

References:
    Hitchin (1987): "The self-duality equations on a Riemann surface"
    hitchin_shadow_engine.py (existing module)
    spectral_curve_engine.py (existing module)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Sequence

import numpy as np


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PI = math.pi
TWO_PI = 2.0 * PI


# =========================================================================
# Section 1: Shadow data for standard families
# =========================================================================

def kappa_virasoro(c) -> float:
    r"""Modular characteristic kappa(Vir_c) = c/2.

    AP1/AP9: authoritative formula from landscape_census.tex.
    AP20: this is kappa(A) for A = Vir_c, NOT kappa_eff.
    AP48: kappa = c/2 is specific to Virasoro, NOT a general VOA formula.
    """
    return float(c) / 2.0


def kappa_heisenberg(k) -> float:
    r"""Modular characteristic kappa(H_k) = k.

    Heisenberg at level k: single generator of weight 1.
    AP39: kappa(H_k) = k, NOT k/2 or c/2.
    """
    return float(k)


def kappa_kac_moody(dim_g: int, k, h_dual: int) -> float:
    r"""Modular characteristic kappa for affine KM.

    kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v).

    AP1: this is NOT c/2 in general (diverges from Sugawara c at rank > 1).
    AP39: kappa != S_2 for non-Virasoro families.
    """
    return float(dim_g) * (float(k) + float(h_dual)) / (2.0 * float(h_dual))


def virasoro_S3(c_val: float) -> float:
    r"""Cubic shadow coefficient S_3 for Virasoro.

    S_3(Vir_c) = 2 (universal for Virasoro, from the L_{-1}^3 vertex).
    The 2 comes from the T(z)T(w) OPE structure.
    """
    return 2.0


def virasoro_S4(c_val: float) -> float:
    r"""Quartic shadow coefficient S_4 for Virasoro.

    S_4(Vir_c) = Q^contact = 10/[c(5c+22)].
    """
    return 10.0 / (c_val * (5.0 * c_val + 22.0))


def virasoro_S5(c_val: float) -> float:
    r"""Quintic shadow coefficient S_5 for Virasoro.

    S_5(Vir_c) = -48/[c^2(5c+22)].
    """
    if abs(c_val) < 1e-15:
        return float('inf')
    return -48.0 / (c_val**2 * (5.0 * c_val + 22.0))


def affine_sl2_S3(k_val: float) -> float:
    """Cubic shadow for sl_2^(1): S_3 = 2*h^v/(k+h^v) = 4/(k+2)."""
    return 4.0 / (k_val + 2.0)


def affine_sl2_S4(k_val: float) -> float:
    """Quartic shadow for sl_2^(1): S_4 = 0 (class L, Jacobi kills quartic)."""
    return 0.0


def shadow_data(family: str, params: Dict[str, float]) -> Dict[str, float]:
    r"""Return shadow data (kappa, S_3, S_4, S_5) for a given algebra family.

    Parameters
    ----------
    family : str
        One of 'virasoro', 'heisenberg', 'affine_sl2', 'affine_sl3',
        'affine_slN', 'w3'.
    params : dict
        Parameters: 'c' for Virasoro, 'k' for Heisenberg/affine, 'N' for slN.

    Returns
    -------
    dict with keys 'kappa', 'S3', 'S4', 'S5', 'class', 'depth'.
    """
    if family == 'virasoro':
        c = params['c']
        kap = kappa_virasoro(c)
        return {
            'kappa': kap,
            'S3': virasoro_S3(c),
            'S4': virasoro_S4(c),
            'S5': virasoro_S5(c),
            'class': 'M',
            'depth': float('inf'),
        }
    elif family == 'heisenberg':
        k = params['k']
        return {
            'kappa': kappa_heisenberg(k),
            'S3': 0.0,
            'S4': 0.0,
            'S5': 0.0,
            'class': 'G',
            'depth': 2,
        }
    elif family == 'affine_sl2':
        k = params['k']
        kap = kappa_kac_moody(3, k, 2)
        return {
            'kappa': kap,
            'S3': affine_sl2_S3(k),
            'S4': affine_sl2_S4(k),
            'S5': 0.0,
            'class': 'L',
            'depth': 3,
        }
    elif family == 'affine_sl3':
        k = params['k']
        kap = kappa_kac_moody(8, k, 3)
        return {
            'kappa': kap,
            'S3': 1.0,
            'S4': 0.0,
            'S5': 0.0,
            'class': 'L',
            'depth': 3,
        }
    elif family == 'affine_slN':
        k = params['k']
        N = int(params['N'])
        dim_g = N * N - 1
        h_v = N
        kap = kappa_kac_moody(dim_g, k, h_v)
        return {
            'kappa': kap,
            'S3': 1.0,
            'S4': 0.0,
            'S5': 0.0,
            'class': 'L',
            'depth': 3,
        }
    elif family == 'w3':
        c = params['c']
        kap = kappa_virasoro(c)
        S3 = virasoro_S3(c)
        S4 = virasoro_S4(c)
        return {
            'kappa': kap,
            'S3': S3,
            'S4': S4,
            'S5': virasoro_S5(c),
            'class': 'M',
            'depth': float('inf'),
        }
    else:
        raise ValueError(f"Unknown family: {family}")


# =========================================================================
# Section 2: Hitchin spectral curve from shadow data
# =========================================================================

def shadow_spectral_curve_sl2(kappa_val: float) -> Dict[str, Any]:
    r"""Spectral curve for the sl_2 shadow Hitchin system.

    The curve: eta^2 + kappa * omega = 0 in T*X.

    For genus 0 (X = P^1): omega = dz^2/z^2, giving
    eta^2 + kappa/z^2 = 0, i.e., eta = +/- sqrt(kappa)/z.

    This is a double cover of P^1, ramified at z = 0, infty.
    By Riemann-Hurwitz: genus(Sigma) = 0 for 2 branch points
    (2g-2 = 2*(-2) + 2 => g = 0).

    For genus 1 (X = elliptic): omega = dz^2 (flat), giving
    eta^2 + kappa = 0, i.e., Sigma = two parallel copies of X.
    genus(Sigma) = 1 if kappa != 0, as unramified double cover of genus 1
    consists of two components each of genus 1 (disconnected) or a connected
    cover of genus 1.

    Returns
    -------
    dict with keys:
        'phi2': the Hitchin base coordinate (= kappa)
        'discriminant': discriminant of the curve (= -4 * kappa)
        'is_singular': whether the curve is singular (kappa = 0)
        'branch_points_P1': branch points on P^1 (z=0, z=infty)
        'genus_P1': genus of spectral curve over P^1
        'genus_elliptic': genus of spectral curve over elliptic
    """
    phi2 = kappa_val
    # Spectral polynomial: eta^2 + phi2 = 0
    # Discriminant of eta^2 + phi2 as polynomial in eta: disc = -4 * phi2
    disc = -4.0 * phi2

    return {
        'phi2': phi2,
        'discriminant': disc,
        'is_singular': abs(kappa_val) < 1e-15,
        'branch_points_P1': [0.0, float('inf')],
        'genus_P1': 0,  # Riemann-Hurwitz: 2g-2 = 2*(2*0-2) + 2 => g=0
        'genus_elliptic': 1,  # Unramified double cover of genus-1
    }


def shadow_spectral_curve_sl3(kappa_val: float, S3_val: float) -> Dict[str, Any]:
    r"""Spectral curve for the sl_3 shadow Hitchin system.

    The curve: eta^3 + phi_2 * eta + phi_3 = 0.

    Shadow identification:
        phi_2 = kappa (= S_2, the arity-2 shadow)
        phi_3 = S_3 (the arity-3 shadow)

    Discriminant of the depressed cubic eta^3 + p*eta + q:
        Delta_3 = -4p^3 - 27q^2

    With p = phi_2 = kappa, q = phi_3 = S_3:
        Delta_3 = -4 kappa^3 - 27 S_3^2

    NOTE: The sign convention.  In the spectral polynomial
    eta^3 - q_2 eta - q_3 = 0 (Hitchin convention with minus signs),
    setting q_2 = -phi_2, q_3 = -phi_3 gives
    Delta = 4 q_2^3 - 27 q_3^2 = -4 phi_2^3 - 27 phi_3^2.
    """
    phi2 = kappa_val
    phi3 = S3_val

    # Discriminant of eta^3 + phi2 * eta + phi3 = 0
    disc = -4.0 * phi2**3 - 27.0 * phi3**2

    # Roots of the cubic (Cardano)
    roots = _cubic_roots(phi2, phi3)

    return {
        'phi2': phi2,
        'phi3': phi3,
        'discriminant': disc,
        'is_singular': abs(disc) < 1e-12,
        'roots': roots,
        'genus_P1': _genus_spectral_triple_cover_P1(disc),
    }


def _cubic_roots(p: float, q: float) -> List[complex]:
    r"""Roots of eta^3 + p*eta + q = 0 via numpy."""
    coeffs = [1.0, 0.0, p, q]
    return list(np.roots(coeffs))


def _genus_spectral_triple_cover_P1(disc: float) -> int:
    r"""Genus of the degree-3 spectral curve over P^1.

    For a degree-N cover of P^1, Riemann-Hurwitz gives:
    2g(Sigma) - 2 = N*(2*0 - 2) + R
    where R is the total ramification.

    For a generic triple cover with simple ramification:
    R = number of branch points (each contributing 1 to ramification).
    The number of branch points equals the degree of the discriminant
    as a section of K^(N(N-1)).

    For sl_3 on P^1 with constant coefficients (phi_2, phi_3 constant):
    the spectral curve is a plane cubic in eta, z, which over P^1
    with constant Hitchin data is actually P^1 x {3 sheets}.
    Genus = 0 when the cover is totally split (disc != 0).
    When disc = 0, sheets collide and genus can jump.

    More precisely: with phi_r in H^0(P^1, K^r), for constant phi_r
    on the affine chart there are no branch points, so g = 0.
    """
    # For constant Hitchin data on P^1, the spectral curve is genus 0
    return 0


def shadow_spectral_curve_slN(N: int, shadow_coeffs: Dict[int, float]) -> Dict[str, Any]:
    r"""Spectral curve for sl_N shadow Hitchin system.

    eta^N + phi_2 eta^{N-2} + phi_3 eta^{N-3} + ... + phi_N = 0

    shadow_coeffs = {2: S_2, 3: S_3, ..., N: S_N}
    """
    # Build polynomial coefficients [1, 0, phi_2, phi_3, ..., phi_N]
    coeffs = [1.0, 0.0]
    for d in range(2, N + 1):
        coeffs.append(shadow_coeffs.get(d, 0.0))

    roots = list(np.roots(coeffs))

    # Discriminant via resultant: product of (r_i - r_j)^2
    disc = 1.0
    for i in range(len(roots)):
        for j in range(i + 1, len(roots)):
            disc *= (roots[i] - roots[j])**2
    # Normalize sign
    disc = complex(disc).real if abs(complex(disc).imag) < 1e-10 else complex(disc)

    return {
        'N': N,
        'coefficients': coeffs,
        'roots': roots,
        'discriminant': disc,
        'hitchin_base_dim': N - 1,
    }


# =========================================================================
# Section 3: Hitchin base map (shadow locus)
# =========================================================================

def hitchin_base_map(family: str, params: Dict[str, float], N: int = 2) -> Dict[str, float]:
    r"""Map from algebra to Hitchin base coordinates.

    Hit: A -> (S_2, S_3, ..., S_N) in B = oplus H^0(K^j).

    For sl_2: Hit(A) = (kappa(A),).
    For sl_3: Hit(A) = (kappa(A), S_3(A)).
    """
    data = shadow_data(family, params)
    result = {'S2': data['kappa']}  # S_2 = kappa for Virasoro (AP39 warning)
    if N >= 3:
        result['S3'] = data['S3']
    if N >= 4:
        result['S4'] = data['S4']
    if N >= 5:
        result['S5'] = data['S5']
    return result


def shadow_hitchin_locus(families_and_params: List[Tuple[str, Dict[str, float]]],
                         N: int = 2) -> List[Dict[str, float]]:
    r"""Compute the shadow Hitchin locus for a collection of algebras.

    Returns a list of Hitchin base coordinates, one per algebra.
    """
    return [hitchin_base_map(fam, params, N) for fam, params in families_and_params]


# =========================================================================
# Section 4: Discriminant comparison — Hitchin vs shadow
# =========================================================================

def hitchin_discriminant_sl2(phi2: float) -> float:
    r"""Discriminant of sl_2 spectral curve: eta^2 + phi2 = 0.

    disc = -4 * phi2.
    Vanishes iff phi2 = 0, i.e., kappa = 0.
    """
    return -4.0 * phi2


def hitchin_discriminant_sl3(phi2: float, phi3: float) -> float:
    r"""Discriminant of sl_3 spectral curve: eta^3 + phi2*eta + phi3 = 0.

    Delta_3 = -4 phi2^3 - 27 phi3^2.
    """
    return -4.0 * phi2**3 - 27.0 * phi3**2


def shadow_critical_discriminant(kappa_val: float, S4_val: float) -> float:
    r"""Shadow critical discriminant Delta = 8*kappa*S_4.

    From the monograph (def:shadow-metric):
    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    with Delta = 8*kappa*S_4.

    Delta = 0 <=> class G/L (tower terminates).
    Delta != 0 <=> class M (infinite tower).
    """
    return 8.0 * kappa_val * S4_val


def verify_discriminant_sl3_vs_shadow(c_val: float) -> Dict[str, Any]:
    r"""Verify that Hitchin discriminant for sl_3 relates to shadow discriminant.

    For W_3 at central charge c:
        kappa = c/2, S_3 = 2, S_4 = 10/[c(5c+22)]
        shadow Delta = 8*kappa*S_4 = 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)

    Hitchin discriminant with phi_2 = kappa, phi_3 = S_3:
        Delta_H = -4 kappa^3 - 27 S_3^2

    These are NOT the same object: the Hitchin discriminant detects
    SPECTRAL CURVE degeneration (sheets collide), while the shadow
    discriminant detects TOWER TERMINATION (Q_L becomes a perfect square).

    The mathematical relationship: the shadow discriminant is a
    PROJECTION of the Hitchin discriminant to the shadow metric sector,
    specifically the coefficient of t^2 in Q_L relative to the perfect-square part.
    """
    kap = kappa_virasoro(c_val)
    s3 = virasoro_S3(c_val)
    s4 = virasoro_S4(c_val)

    # Shadow discriminant
    delta_shadow = shadow_critical_discriminant(kap, s4)

    # Hitchin discriminant with shadow coordinates
    delta_hitchin = hitchin_discriminant_sl3(kap, s3)

    # Shadow metric coefficients
    alpha = s3
    q0 = (2.0 * kap)**2
    q1 = 12.0 * kap * alpha
    q2 = 9.0 * alpha**2 + 2.0 * delta_shadow

    return {
        'c': c_val,
        'kappa': kap,
        'S3': s3,
        'S4': s4,
        'delta_shadow': delta_shadow,
        'delta_hitchin': delta_hitchin,
        'shadow_metric_Q0': q0,
        'shadow_metric_Q1': q1,
        'shadow_metric_Q2': q2,
        'shadow_is_perfect_square': abs(delta_shadow) < 1e-12,
        'hitchin_is_singular': abs(delta_hitchin) < 1e-12,
    }


# =========================================================================
# Section 5: Shadow connection and WKB
# =========================================================================

def shadow_metric_Q(kappa_val: float, alpha_val: float, S4_val: float, t: float) -> float:
    r"""Shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Delta = 8*kappa*S_4.
    """
    Delta = 8.0 * kappa_val * S4_val
    return (2.0 * kappa_val + 3.0 * alpha_val * t)**2 + 2.0 * Delta * t**2


def shadow_metric_Q_prime(kappa_val: float, alpha_val: float, S4_val: float, t: float) -> float:
    r"""Derivative Q_L'(t) = d/dt Q_L(t)."""
    Delta = 8.0 * kappa_val * S4_val
    return 2.0 * 3.0 * alpha_val * (2.0 * kappa_val + 3.0 * alpha_val * t) + 4.0 * Delta * t


def shadow_connection_coefficient(kappa_val: float, alpha_val: float,
                                  S4_val: float, t: float) -> float:
    r"""Connection coefficient of nabla^sh = d - Q'/(2Q) dt.

    Returns -Q'/(2Q) evaluated at t.
    """
    Q = shadow_metric_Q(kappa_val, alpha_val, S4_val, t)
    Qp = shadow_metric_Q_prime(kappa_val, alpha_val, S4_val, t)
    if abs(Q) < 1e-30:
        return float('inf')
    return -Qp / (2.0 * Q)


def flat_section_shadow(kappa_val: float, alpha_val: float,
                        S4_val: float, t: float) -> float:
    r"""Flat section of nabla^sh: Phi(t) = sqrt(Q_L(t)/Q_L(0)).

    AP23: This is the flat section, NOT the shadow generating function
    H(t) = t^2 * Phi(t).
    """
    Q0 = shadow_metric_Q(kappa_val, alpha_val, S4_val, 0.0)
    Qt = shadow_metric_Q(kappa_val, alpha_val, S4_val, t)
    if Q0 <= 0:
        return float('nan')
    return math.sqrt(abs(Qt / Q0))


def wkb_approximation_sl2(kappa_val: float, z: complex) -> complex:
    r"""WKB approximation for the sl_2 shadow spectral curve on P^1.

    Spectral curve: eta^2 + kappa/z^2 = 0
    => eta = +/- i*sqrt(kappa)/z

    WKB: psi ~ exp(int eta dz) = exp(+/- i*sqrt(kappa)*log(z))
         = z^{+/- i*sqrt(kappa)}

    For real kappa > 0: oscillatory solution z^{i*sqrt(kappa)}.
    For real kappa < 0: power-law solution z^{sqrt(|kappa|)}.
    """
    if z == 0:
        return complex(0, 0)
    sqrt_kappa = cmath.sqrt(complex(kappa_val))
    return cmath.exp(1j * sqrt_kappa * cmath.log(z))


def verify_wkb_vs_flat_section(kappa_val: float, alpha_val: float,
                               S4_val: float, t_values: Sequence[float]) -> Dict[str, Any]:
    r"""Compare WKB from spectral curve with flat section of nabla^sh.

    For the sl_2 shadow with constant kappa on P^1:
    The WKB gives psi ~ z^{i*sqrt(kappa)}.
    The flat section gives Phi(t) = sqrt(Q(t)/Q(0)).

    These are DIFFERENT objects on DIFFERENT spaces:
    - WKB is on the curve X (function of z).
    - Flat section is on the deformation space (function of t).

    The connection is that the WKB phase integral at genus 0
    reproduces the shadow partition function.
    """
    flat_values = [flat_section_shadow(kappa_val, alpha_val, S4_val, t)
                   for t in t_values]
    Q_values = [shadow_metric_Q(kappa_val, alpha_val, S4_val, t)
                for t in t_values]

    return {
        'kappa': kappa_val,
        't_values': list(t_values),
        'flat_section': flat_values,
        'Q_values': Q_values,
    }


# =========================================================================
# Section 6: Hitchin fibration — genus of spectral curves
# =========================================================================

def riemann_hurwitz_genus(g_base: int, degree: int, num_branch_points: int,
                          ramification_type: str = 'simple') -> int:
    r"""Genus of a cover via Riemann-Hurwitz.

    2g(Sigma) - 2 = degree * (2*g_base - 2) + R

    For simple ramification: each branch point contributes
    ramification index e-1 = 1 (simple), so R = num_branch_points.

    For total ramification at each branch point: e = degree,
    so R = num_branch_points * (degree - 1).
    """
    if ramification_type == 'simple':
        R = num_branch_points
    elif ramification_type == 'total':
        R = num_branch_points * (degree - 1)
    else:
        raise ValueError(f"Unknown ramification type: {ramification_type}")

    two_g_minus_2 = degree * (2 * g_base - 2) + R
    g = (two_g_minus_2 + 2) // 2
    return max(g, 0)


def spectral_curve_genus_sl2(g_base: int, kappa_val: float) -> Dict[str, Any]:
    r"""Genus of the sl_2 spectral double cover.

    eta^2 + kappa * omega = 0 over a curve X of genus g_base.

    The double cover is branched at zeros of kappa * omega.

    For g_base = 0 (P^1):
      omega = K_{P^1}^2, a section of O(-4) on P^1. The section
      dz^2/z^2 has a double zero at z=0 and double pole at infty
      (or choose the global section: degree of K^2 = -4, so no
      global holomorphic section).  For the meromorphic section,
      the double cover has branch points at the zeros of kappa*omega.

      With the standard model eta^2 + kappa/z^2 = 0: branch locus
      is z=0, z=infty (2 points), giving Riemann-Hurwitz:
      2g - 2 = 2*(2*0-2) + 2 = -2, so g = 0.

    For g_base = 1:
      omega = dz^2 (flat), kappa*omega is nonvanishing for kappa != 0.
      The double cover is UNRAMIFIED, 2g-2 = 2*(2*1-2) + 0 = 0, g=1.
      (Two disconnected copies of the elliptic curve.)

    For g_base >= 2:
      degree(K^2) = 2*(2g-2) = 4g-4.
      Number of zeros of omega (generic section) = 4g-4.
      Branch points of double cover = 4g-4 (all simple).
      2g(Sigma)-2 = 2*(2g_base-2) + (4g_base-4) = 4g_base-4 + 4g_base-4 = 8g_base-8.
      g(Sigma) = 4g_base - 3.
    """
    if g_base == 0:
        # Double cover of P^1 branched at 2 points
        g_spec = riemann_hurwitz_genus(0, 2, 2, 'simple')
        num_branch = 2
    elif g_base == 1:
        # Unramified double cover of elliptic curve
        g_spec = 1
        num_branch = 0
    else:
        # Generic: deg(K^2) = 4g-4 zeros, all simple branch points
        num_branch = 4 * g_base - 4
        g_spec = riemann_hurwitz_genus(g_base, 2, num_branch, 'simple')

    return {
        'g_base': g_base,
        'degree': 2,
        'num_branch_points': num_branch,
        'genus_spectral': g_spec,
        'formula': f'4*{g_base}-3={4*g_base-3}' if g_base >= 2 else f'{g_spec}',
    }


def spectral_curve_genus_sl3(g_base: int) -> Dict[str, Any]:
    r"""Genus of the sl_3 spectral triple cover.

    eta^3 + phi_2 eta + phi_3 = 0 over a curve X of genus g_base.

    For generic Hitchin data:
    - phi_2 in H^0(K^2): deg = 4g-4
    - phi_3 in H^0(K^3): deg = 6g-6
    - Discriminant -4 phi_2^3 - 27 phi_3^2 in H^0(K^6): deg = 12g-12
    - Number of branch points = 12g-12 (simple branching generically)

    Riemann-Hurwitz: 2g(Sigma)-2 = 3*(2g_base-2) + (12g_base-12)
                                 = 6g_base-6 + 12g_base-12
                                 = 18g_base - 18
    g(Sigma) = 9g_base - 8.

    For g_base = 0 with constant data: no branch points, g = 0.
    For g_base = 1: deg(K^6) = 0, so 0 branch points (generically
    nonzero constant discriminant), g(Sigma) = 1.
    For g_base >= 2: g(Sigma) = 9g_base - 8.
    """
    if g_base == 0:
        g_spec = 0
        num_branch = 0
    elif g_base == 1:
        g_spec = 1
        num_branch = 0
    else:
        num_branch = 12 * g_base - 12  # deg of discriminant section
        g_spec = 9 * g_base - 8

    return {
        'g_base': g_base,
        'degree': 3,
        'num_branch_points': num_branch,
        'genus_spectral': g_spec,
    }


def spectral_curve_genus_slN(N: int, g_base: int) -> Dict[str, Any]:
    r"""Genus of the sl_N spectral degree-N cover.

    For generic Hitchin data on a curve of genus g_base:
    The discriminant is a section of K^{N(N-1)}, so
    deg = N(N-1)(2g_base-2).

    Number of branch points = N(N-1)(2g_base-2) for g_base >= 2.
    Riemann-Hurwitz:
    2g(Sigma)-2 = N*(2g_base-2) + N(N-1)*(2g_base-2)
                = (N + N(N-1))*(2g_base-2)
                = N^2 * (2g_base-2)

    g(Sigma) = N^2*(g_base-1) + 1.

    Cross-check: sl_2: N=2, g(Sigma) = 4(g-1)+1 = 4g-3. Matches.
    sl_3: N=3, g(Sigma) = 9(g-1)+1 = 9g-8. Matches.
    """
    if g_base == 0:
        g_spec = 0
    elif g_base == 1:
        g_spec = 1
    else:
        g_spec = N * N * (g_base - 1) + 1

    num_branch = N * (N - 1) * max(2 * g_base - 2, 0) if g_base >= 2 else 0

    return {
        'g_base': g_base,
        'N': N,
        'degree': N,
        'num_branch_points': num_branch,
        'genus_spectral': g_spec,
        'formula': f'{N}^2*({g_base}-1)+1={g_spec}',
    }


# =========================================================================
# Section 7: Stokes graph from spectral curve
# =========================================================================

def stokes_rays_sl2_P1(kappa_val: float, num_points: int = 100) -> Dict[str, Any]:
    r"""Stokes graph of the sl_2 shadow spectral curve on P^1.

    Spectral curve: eta^2 + kappa/z^2 = 0.
    The two sheets: eta_+/- = +/- i*sqrt(kappa)/z.

    The Stokes condition: Re(int_{z_0}^{z} (eta_+ - eta_-) dz) = 0.

    eta_+ - eta_- = 2i*sqrt(kappa)/z.
    int (2i*sqrt(kappa)/z) dz = 2i*sqrt(kappa)*log(z).

    For z = r*e^{i*theta}:
    2i*sqrt(kappa)*(ln r + i*theta) = 2i*sqrt(kappa)*ln(r) - 2*sqrt(kappa)*theta.

    Re(...) = -2*sqrt(kappa)*theta (for real positive kappa).

    So Re = 0 iff theta = 0 (or theta = pi).
    The Stokes graph consists of two rays: the positive and negative real axes.

    For kappa < 0: sqrt(kappa) is purely imaginary, so
    2i*(i*sqrt(|kappa|))*log(z) = -2*sqrt(|kappa|)*log(z),
    Re(...) = -2*sqrt(|kappa|)*ln(r), which vanishes iff r = 1 (unit circle).
    """
    if kappa_val > 0:
        # Stokes rays along real axis
        sqrt_k = math.sqrt(kappa_val)
        rays = [
            {'direction': 0.0, 'label': 'positive real axis'},
            {'direction': PI, 'label': 'negative real axis'},
        ]
        stokes_type = 'radial'
    elif kappa_val < 0:
        # Stokes curve is the unit circle
        sqrt_k = math.sqrt(-kappa_val)
        theta_vals = np.linspace(0, 2 * PI, num_points)
        rays = [{'theta': float(th), 'r': 1.0} for th in theta_vals]
        stokes_type = 'circular'
    else:
        rays = []
        stokes_type = 'degenerate'
        sqrt_k = 0.0

    return {
        'kappa': kappa_val,
        'sqrt_kappa': sqrt_k if kappa_val >= 0 else 1j * math.sqrt(-kappa_val),
        'stokes_type': stokes_type,
        'rays': rays,
        'num_stokes_rays': 2 if kappa_val > 0 else (num_points if kappa_val < 0 else 0),
    }


def stokes_graph_sl2_genus_g(g_base: int, kappa_val: float = 1.0) -> Dict[str, Any]:
    r"""Topology of the Stokes graph for sl_2 on a genus-g curve.

    For a degree-2 spectral curve over a genus-g curve with
    n branch points (= 4g-4 for g >= 2):

    The Stokes graph has:
    - Vertices: the branch points (turning points)
    - Edges: Stokes lines connecting them
    - Number of edges = 2*(degree-1)*(2g-2+n_poles)

    For sl_2 (degree 2) with no poles on a compact curve:
    edges = 2*(2-1)*(2g_base-2) = 2*(2g_base-2) for the base curve's
    contribution.

    For g_base = 0: special (meromorphic differentials).
    For g_base >= 2: edges = 3*(4g-4) by Strebel's theorem
    (3 edges from each simple zero of the quadratic differential).
    """
    if g_base == 0:
        num_zeros = 0  # meromorphic, poles at 0, infty
        num_edges = 2  # the two radial Stokes rays
    elif g_base == 1:
        num_zeros = 0  # flat metric on torus
        num_edges = 0
    else:
        num_zeros = 4 * g_base - 4  # zeros of generic phi_2 in H^0(K^2)
        num_edges = 3 * num_zeros  # 3 edges from each simple zero

    return {
        'g_base': g_base,
        'num_zeros_phi2': num_zeros,
        'num_stokes_edges': num_edges,
        'topology': 'Strebel' if g_base >= 2 else 'degenerate',
    }


# =========================================================================
# Section 8: Opers and monodromy
# =========================================================================

def shadow_oper_sl2_P1(kappa_val: float) -> Dict[str, Any]:
    r"""Shadow oper for sl_2 on P^1.

    The oper equation: psi'' + kappa/z^2 * psi = 0.

    This is a regular singular ODE at z = 0 (Euler equation).
    The indicial equation: s(s-1) + kappa = 0, i.e., s^2 - s + kappa = 0.

    Solutions: s = (1 +/- sqrt(1 - 4*kappa))/2.

    Basis of solutions: psi_+/- = z^{s_+/-}.

    Monodromy around z = 0: psi -> e^{2*pi*i*s} * psi.
    M = diag(e^{2*pi*i*s_+}, e^{2*pi*i*s_-}).

    Eigenvalues: e^{pi*i*(1+sqrt(1-4kappa))}, e^{pi*i*(1-sqrt(1-4kappa))}.

    Special values:
    - kappa = 0: s = 0, 1. Monodromy = diag(1, e^{2pi i}) = Id. TRIVIAL.
    - kappa = 1/4: s = 1/2, 1/2. Monodromy has a JORDAN BLOCK (log term).
    - kappa = c/2 for Virasoro: s = (1 +/- sqrt(1-2c))/2.
    """
    # Indicial roots
    discriminant = 1.0 - 4.0 * kappa_val
    sqrt_disc = cmath.sqrt(discriminant)
    s_plus = (1.0 + sqrt_disc) / 2.0
    s_minus = (1.0 - sqrt_disc) / 2.0

    # Monodromy eigenvalues
    mono_plus = cmath.exp(2.0j * PI * s_plus)
    mono_minus = cmath.exp(2.0j * PI * s_minus)

    # Trace of monodromy
    mono_trace = mono_plus + mono_minus

    # Is monodromy unipotent (trace = 2)?
    is_unipotent = abs(mono_trace - 2.0) < 1e-10

    return {
        'kappa': kappa_val,
        'indicial_discriminant': discriminant,
        'sqrt_discriminant': sqrt_disc,
        's_plus': s_plus,
        's_minus': s_minus,
        'monodromy_eigenvalue_plus': mono_plus,
        'monodromy_eigenvalue_minus': mono_minus,
        'monodromy_trace': mono_trace,
        'is_unipotent': is_unipotent,
        'is_resonant': abs(s_plus - s_minus - round(complex(s_plus - s_minus).real)) < 1e-10
        if isinstance(s_plus - s_minus, (int, float, complex)) else False,
    }


def oper_monodromy_virasoro(c_val: float) -> Dict[str, Any]:
    r"""Oper monodromy for Virasoro at central charge c.

    kappa = c/2. Indicial roots: s = (1 +/- sqrt(1-2c))/2.

    Special cases:
    - c = 0: kappa = 0, s = 0,1. Trivial monodromy.
    - c = 1/2: kappa = 1/4. RESONANT (s_+ - s_- = 0).
    - c = 1: kappa = 1/2. s = (1 +/- i)/2.
    - c = 13: kappa = 13/2. SELF-DUAL point.
    - c = 25: kappa = 25/2. Partner of c=1 under c -> 26-c.
    - c = 26: kappa = 13. Critical dimension (ghost cancellation).
    """
    kap = kappa_virasoro(c_val)
    return shadow_oper_sl2_P1(kap)


def oper_monodromy_landscape(c_values: Sequence[float]) -> List[Dict[str, Any]]:
    r"""Compute oper monodromy across a landscape of central charges."""
    return [oper_monodromy_virasoro(c) for c in c_values]


# =========================================================================
# Section 9: Nonabelianization (Gaiotto-Moore-Neitzke)
# =========================================================================

def nonabelianization_sl2(kappa_val: float, theta_phase: float = 0.0) -> Dict[str, Any]:
    r"""Nonabelianization for the sl_2 shadow on P^1.

    The nonabelianization map (GMN 2013) lifts abelian connections
    on the spectral curve Sigma to nonabelian connections on X.

    For sl_2 with spectral curve eta^2 + kappa/z^2 = 0:
    Sigma is a double cover.  The abelian connection on Sigma is
    d + eta = d +/- i*sqrt(kappa)/z on each sheet.

    The nonabelian connection on P^1 is:
    nabla = d + A(z) where A(z) = [[0, sqrt(kappa)/z], [sqrt(kappa)/z, 0]]
    (in an appropriate gauge).

    The shadow connection nabla^sh = d - Q'/(2Q) dt lives on the
    DEFORMATION SPACE, not on the curve X.  The comparison:
    - nabla^sh is the QUANTIZATION of the Hitchin connection.
    - The nonabelianized connection is the CLASSICAL Hitchin connection.
    - They agree at leading order in the WKB expansion.
    """
    sqrt_kap = cmath.sqrt(complex(kappa_val))
    phase = cmath.exp(1j * theta_phase)

    # Abelian differentials on the two sheets
    ab_diff_plus = 1j * sqrt_kap * phase
    ab_diff_minus = -1j * sqrt_kap * phase

    # Nonabelian connection matrix (off-diagonal)
    A_matrix = np.array([
        [0, complex(sqrt_kap * phase)],
        [complex(sqrt_kap * phase), 0],
    ], dtype=complex)

    # Monodromy of the nonabelian connection (formal)
    # For a circle of radius 1: exp(2*pi*i * A_matrix) formally
    mono_eigenval_1 = cmath.exp(2.0j * PI * sqrt_kap)
    mono_eigenval_2 = cmath.exp(-2.0j * PI * sqrt_kap)

    return {
        'kappa': kappa_val,
        'abelian_plus': ab_diff_plus,
        'abelian_minus': ab_diff_minus,
        'connection_matrix': A_matrix,
        'monodromy_eigenvalues': (mono_eigenval_1, mono_eigenval_2),
        'monodromy_trace': mono_eigenval_1 + mono_eigenval_2,
    }


def verify_nonabelianization_vs_oper(kappa_val: float) -> Dict[str, Any]:
    r"""Verify that nonabelianization monodromy matches oper monodromy.

    The oper has indicial roots s_+/- = (1 +/- sqrt(1-4kappa))/2.
    The nonabelianization has eigenvalues exp(+/- 2*pi*i*sqrt(kappa)).

    These are DIFFERENT: the oper encodes the QUANTUM connection
    (includes the 1/2 shift from the spin structure), while the
    nonabelianization is CLASSICAL.

    The relation: the oper monodromy eigenvalues are
    exp(2*pi*i*(1+/-sqrt(1-4kappa))/2) = -exp(+/- pi*i*sqrt(1-4kappa)).
    The nonabelian ones are exp(+/- 2*pi*i*sqrt(kappa)).

    At large kappa: sqrt(1-4kappa) ~ 2i*sqrt(kappa), so
    oper eigenvalue ~ -exp(+/- 2*pi*sqrt(kappa)) (REAL, exponential growth).
    Nonabelian eigenvalue ~ exp(+/- 2*pi*i*sqrt(kappa)) (on unit circle).

    They agree in ABSOLUTE VALUE only when kappa is real and negative
    (then both are on the unit circle).
    """
    oper = shadow_oper_sl2_P1(kappa_val)
    nonab = nonabelianization_sl2(kappa_val)

    # Compare traces
    oper_trace = oper['monodromy_trace']
    nonab_trace = nonab['monodromy_trace']

    return {
        'kappa': kappa_val,
        'oper_trace': oper_trace,
        'nonab_trace': nonab_trace,
        'traces_differ': abs(complex(oper_trace) - complex(nonab_trace)) > 1e-10,
        'oper_is_real': abs(complex(oper_trace).imag) < 1e-10,
        'nonab_is_real': abs(complex(nonab_trace).imag) < 1e-10,
    }


# =========================================================================
# Section 10: Hitchin section and shadow locus landscape
# =========================================================================

def standard_landscape_hitchin_map() -> Dict[str, Dict[str, float]]:
    r"""Hitchin base coordinates for all standard families.

    Returns (S_2, S_3, S_4) for each family at typical parameter values.

    AP39: S_2 = kappa for Virasoro, but S_2 != kappa in general.
    """
    landscape = {}

    # Virasoro at c = 1, 13, 25, 26
    for c in [1, 13, 25, 26]:
        kap = kappa_virasoro(c)
        landscape[f'Vir_c{c}'] = {
            'S2': kap,
            'S3': virasoro_S3(c),
            'S4': virasoro_S4(c),
            'class': 'M',
        }

    # Heisenberg at k = 1
    landscape['Heis_k1'] = {
        'S2': kappa_heisenberg(1),
        'S3': 0.0,
        'S4': 0.0,
        'class': 'G',
    }

    # Affine sl_2 at k = 1
    landscape['aff_sl2_k1'] = {
        'S2': kappa_kac_moody(3, 1, 2),
        'S3': 1.0,
        'S4': 0.0,
        'class': 'L',
    }

    # Affine sl_3 at k = 1
    landscape['aff_sl3_k1'] = {
        'S2': kappa_kac_moody(8, 1, 3),
        'S3': 1.0,
        'S4': 0.0,
        'class': 'L',
    }

    return landscape


def hitchin_discriminant_landscape(landscape: Optional[Dict] = None) -> Dict[str, Dict[str, float]]:
    r"""Compute Hitchin discriminants for the standard landscape.

    For each algebra, compute the sl_2 and sl_3 Hitchin discriminants.
    """
    if landscape is None:
        landscape = standard_landscape_hitchin_map()

    results = {}
    for name, data in landscape.items():
        s2 = data['S2']
        s3 = data.get('S3', 0.0)
        s4 = data.get('S4', 0.0)

        disc_2 = hitchin_discriminant_sl2(s2)
        disc_3 = hitchin_discriminant_sl3(s2, s3)
        delta_shadow = shadow_critical_discriminant(s2, s4)

        results[name] = {
            'S2': s2,
            'S3': s3,
            'S4': s4,
            'hitchin_disc_sl2': disc_2,
            'hitchin_disc_sl3': disc_3,
            'shadow_discriminant': delta_shadow,
            'class': data.get('class', '?'),
        }

    return results


# =========================================================================
# Section 11: Spectral curve degeneration and shadow depth
# =========================================================================

def shadow_depth_from_spectral(kappa_val: float, S3_val: float,
                               S4_val: float) -> Dict[str, Any]:
    r"""Classify shadow depth from the spectral curve viewpoint.

    Shadow metric: Q(t) = (2kappa + 3*alpha*t)^2 + 2*Delta*t^2
    with alpha = S_3, Delta = 8*kappa*S_4.

    - Delta = 0 and alpha = 0: class G, depth 2 (Gaussian, terminates).
    - Delta = 0 and alpha != 0: class L, depth 3 (Lie, terminates).
    - Delta != 0 and Q has a zero: class C, depth 4 (contact, terminates
      by stratum separation).
    - Delta != 0 and Q has no real zero: class M, depth infinity
      (mixed, infinite tower).
    """
    Delta = 8.0 * kappa_val * S4_val

    if abs(Delta) < 1e-15:
        if abs(S3_val) < 1e-15:
            return {'class': 'G', 'depth': 2, 'Delta': Delta}
        else:
            return {'class': 'L', 'depth': 3, 'Delta': Delta}

    # Q(t) = (2kappa + 3*S3*t)^2 + 2*Delta*t^2
    # = 4kappa^2 + 12kappa*S3*t + (9*S3^2 + 2*Delta)*t^2
    a = 9.0 * S3_val**2 + 2.0 * Delta
    b = 12.0 * kappa_val * S3_val
    c_coeff = 4.0 * kappa_val**2

    # Discriminant of the quadratic at^2 + bt + c
    disc_Q = b**2 - 4.0 * a * c_coeff

    if disc_Q >= 0:
        # Q has real zeros => class C (stratum separation terminates at 4)
        return {'class': 'C', 'depth': 4, 'Delta': Delta, 'disc_Q': disc_Q}
    else:
        # Q is positive definite => class M (infinite tower)
        return {'class': 'M', 'depth': float('inf'), 'Delta': Delta, 'disc_Q': disc_Q}


# =========================================================================
# Section 12: Virasoro spectral curves at special central charges
# =========================================================================

def virasoro_spectral_data(c_val: float) -> Dict[str, Any]:
    r"""Complete spectral curve data for Virasoro at central charge c.

    Computes:
    1. Shadow data (kappa, S3, S4, S5)
    2. sl_2 spectral curve + discriminant
    3. sl_3 spectral curve + discriminant
    4. Oper data + monodromy
    5. Shadow depth classification
    6. WKB data
    """
    kap = kappa_virasoro(c_val)
    s3 = virasoro_S3(c_val)
    s4 = virasoro_S4(c_val)
    s5 = virasoro_S5(c_val) if abs(c_val) > 1e-10 else float('inf')

    spec_sl2 = shadow_spectral_curve_sl2(kap)
    spec_sl3 = shadow_spectral_curve_sl3(kap, s3)
    oper = oper_monodromy_virasoro(c_val)
    depth = shadow_depth_from_spectral(kap, s3, s4)
    disc_comparison = verify_discriminant_sl3_vs_shadow(c_val)

    return {
        'c': c_val,
        'kappa': kap,
        'S3': s3,
        'S4': s4,
        'S5': s5,
        'spectral_sl2': spec_sl2,
        'spectral_sl3': spec_sl3,
        'oper': oper,
        'depth': depth,
        'discriminant_comparison': disc_comparison,
    }


# =========================================================================
# Section 13: Complementarity of spectral data under Koszul duality
# =========================================================================

def koszul_dual_virasoro(c_val: float) -> float:
    r"""Koszul dual central charge for Virasoro: c' = 26 - c.

    AP8: self-dual at c = 13, NOT c = 26.
    AP24: kappa + kappa' = c/2 + (26-c)/2 = 13, NOT 0.
    """
    return 26.0 - c_val


def spectral_complementarity(c_val: float) -> Dict[str, Any]:
    r"""Compare spectral data of A and A! for Virasoro.

    A = Vir_c, A! = Vir_{26-c}.
    kappa(A) + kappa(A!) = c/2 + (26-c)/2 = 13.

    The spectral curves:
    A:  eta^2 + c/2 * omega = 0
    A!: eta^2 + (26-c)/2 * omega = 0

    The sum of kappas is 13 (AP24).
    The product: kappa * kappa' = c(26-c)/4.
    Maximum at c = 13: kappa = kappa' = 13/2, product = 169/4.
    """
    c_dual = koszul_dual_virasoro(c_val)
    kap = kappa_virasoro(c_val)
    kap_dual = kappa_virasoro(c_dual)

    oper_A = oper_monodromy_virasoro(c_val)
    oper_A_dual = oper_monodromy_virasoro(c_dual)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'kappa': kap,
        'kappa_dual': kap_dual,
        'kappa_sum': kap + kap_dual,
        'kappa_product': kap * kap_dual,
        'oper_A': oper_A,
        'oper_A_dual': oper_A_dual,
        'self_dual': abs(c_val - 13.0) < 1e-10,
    }


# =========================================================================
# Section 14: Genus of Hitchin fiber (abelian variety dimension)
# =========================================================================

def hitchin_fiber_dimension_sl2(g_base: int) -> int:
    r"""Dimension of the generic Hitchin fiber for sl_2 on genus g_base.

    The generic fiber is the Jacobian of the spectral curve Sigma.
    dim Jac(Sigma) = genus(Sigma).

    For sl_2: genus(Sigma) = 4g_base - 3 for g_base >= 2.
    """
    data = spectral_curve_genus_sl2(g_base, 1.0)  # kappa doesn't affect genus
    return data['genus_spectral']


def hitchin_fiber_dimension_slN(N: int, g_base: int) -> int:
    r"""Dimension of the generic Hitchin fiber for sl_N.

    dim = genus(Sigma) = N^2(g_base-1) + 1 for g_base >= 2.

    Cross-check: dim(Hitchin base) = sum_{j=2}^N dim H^0(K^j)
                                    = sum_{j=2}^N (2j-1)(g-1)
                                    = (N^2-1)(g-1)
    dim(fiber) = N^2(g-1)+1 vs dim(base) = (N^2-1)(g-1).
    Total dim = 2*(N^2-1)*(g-1) = dim T*Bun_G. Correct.
    """
    data = spectral_curve_genus_slN(N, g_base)
    return data['genus_spectral']


def hitchin_base_dimension(N: int, g_base: int) -> int:
    r"""Dimension of the Hitchin base for sl_N on genus g_base.

    B = oplus_{j=2}^N H^0(K^j).
    dim H^0(K^j) = (2j-1)(g-1) for g >= 2 by Riemann-Roch.
    dim B = sum_{j=2}^N (2j-1)(g-1) = (N^2-1)(g-1).
    """
    if g_base < 2:
        # Special cases
        if g_base == 0:
            return 0  # No holomorphic differentials on P^1
        elif g_base == 1:
            return N - 1  # Each H^0(K^j) is 1-dimensional for j >= 1
    return (N * N - 1) * (g_base - 1)


# =========================================================================
# Section 15: Complete Hitchin-shadow report
# =========================================================================

def hitchin_shadow_report(family: str, params: Dict[str, float],
                          g_base: int = 2) -> Dict[str, Any]:
    r"""Complete Hitchin-shadow analysis for an algebra.

    Computes all spectral curve data, discriminants, opers, genera, etc.
    """
    data = shadow_data(family, params)
    kap = data['kappa']
    s3 = data['S3']
    s4 = data['S4']

    report = {
        'family': family,
        'params': params,
        'shadow_data': data,
    }

    # Spectral curves
    report['spectral_sl2'] = shadow_spectral_curve_sl2(kap)
    report['spectral_sl3'] = shadow_spectral_curve_sl3(kap, s3)

    # Discriminants
    report['hitchin_disc_sl2'] = hitchin_discriminant_sl2(kap)
    report['hitchin_disc_sl3'] = hitchin_discriminant_sl3(kap, s3)
    report['shadow_discriminant'] = shadow_critical_discriminant(kap, s4)

    # Genera
    report['genus_sl2'] = spectral_curve_genus_sl2(g_base, kap)
    report['genus_sl3'] = spectral_curve_genus_sl3(g_base)

    # Oper
    report['oper'] = shadow_oper_sl2_P1(kap)

    # Depth
    report['depth_class'] = shadow_depth_from_spectral(kap, s3, s4)

    # Stokes
    if kap != 0:
        report['stokes'] = stokes_rays_sl2_P1(kap)

    return report
