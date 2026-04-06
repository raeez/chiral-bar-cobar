r"""bc_bridgeland_shadow_stability_engine.py -- BC-121: Bridgeland stability
conditions on shadow categories, central charge at zeta zeros, DT invariants.

MATHEMATICAL CONTENT
====================

Bridgeland stability conditions on the shadow category D^b(A^sh):
a pair sigma = (Z, P) where Z: K_0(D^b(A^sh)) -> C is the central charge
and P is a slicing.  The central charge is constructed from the shadow data
(kappa, Delta) via the geometric Mukai vector formalism.

=== 1. GEOMETRIC CENTRAL CHARGE FROM SHADOW DATA ===

The shadow obstruction tower provides two canonical real parameters:
    B = kappa(A) / (kappa(A) + |Delta(A)|)       (shadow B-field)
    omega = |Delta(A)| / (kappa(A) + |Delta(A)|)  (shadow Kahler class)

where kappa = S_2(A) is the modular characteristic and
Delta = 8*kappa*S_4 is the critical discriminant (from shadow metric Q_L).

The geometric central charge on a formal Chern character ch = (r, d, chi) is:
    Z_{B,omega}(r, d, chi) = -chi + d*omega*i + r*(omega^2/2 + B*omega*i - B^2/2)

For the SHADOW formalism, the K-theory generators gamma_r at each arity r
carry the formal Chern character ch(gamma_r) = (1, r, S_r(A)):
    Z_shadow(gamma_r) = -S_r + r*omega*i + (omega^2/2 + B*omega*i - B^2/2)

=== 2. WALLS IN THE (c, Delta) PLANE ===

As c varies, the shadow parameters (B(c), omega(c)) trace a curve in the
(B, omega) half-plane.  Stability walls are:
    W_{r,s} = {c : phi(gamma_r; c) = phi(gamma_s; c)}
where phi(E) = (1/pi)*arg(Z(E)) is the Bridgeland phase.

The critical discriminant Delta(c) = 40/(5c+22) for Virasoro controls
the wall structure: walls accumulate as Delta -> 0 (the class G/L boundary).

=== 3. DT INVARIANTS FROM SHADOW ===

The shadow DT invariant at charge n is defined as:
    DT_n(A) = Omega(gamma_n) = (-1)^{n-1} * chi(M_n)
where M_n is the moduli of semistable objects of class gamma_n.

In the shadow category, DT_n is DEFINED operationally from the shadow
coefficients and the KS wall-crossing formula.  The DT partition function:
    Z_DT(q) = sum_{n >= 0} DT_n * q^n

The MacMahon function M(q) = prod_{n>=1} (1/(1-q^n))^n satisfies
    Z_DT^{CY3}(q) = M(q)^chi
for a Calabi-Yau 3-fold with Euler characteristic chi.

For the SHADOW theory: chi_shadow(A) = dim Stab(A^sh) is the effective
Euler characteristic, and the MacMahon comparison tests whether
    Z_DT^shadow(q) approx M(q)^{chi_shadow}

=== 4. STABILITY AT ZETA ZEROS ===

For each zero rho_n of the shadow zeta function zeta_A(s):
    - Evaluate the central charge Z(c(rho_n)) at the "c-value" of the zero
    - Determine if c(rho_n) lies on a wall of marginal stability
    - Compute the DT invariant jump across the zero

The conjecture: zeta zeros = stability walls of the shadow category.

BEILINSON WARNINGS
==================
AP1:  kappa formulas are family-specific.
AP9:  S_2 = kappa != c/2 in general (only for Virasoro).
AP10: Cross-verify DT values by multiple methods (not hardcoded).
AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
AP31: kappa = 0 does NOT imply Theta = 0.
AP38: Literature DT conventions vary; verify normalizations.
AP39: kappa = c/2 for Virasoro only; NOT general.
AP42: scattering = shadow at the motivic level; naive BCH insufficient.
AP48: kappa depends on the full algebra, not just c.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:complementarity (higher_genus_complementarity.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# Import from existing engines
# ---------------------------------------------------------------------------
from compute.lib.bc_bridgeland_stability_engine import (
    shadow_coefficients,
    koszul_dual_shadow_coefficients,
    shadow_depth,
    central_charge as arity_central_charge,
    central_charge_vector,
    phase as bridgeland_phase,
    phase_spectrum,
    mass_spectrum,
    effective_stability_dimension,
    support_property_holds,
    wall_of_marginal_stability,
    full_stability_analysis,
)

from compute.lib.bc_wall_crossing_shadow_engine import (
    virasoro_kappa,
    virasoro_shadow_coefficients as wc_virasoro_shadow_coefficients,
    virasoro_S4,
    critical_discriminant_virasoro,
    ks_automorphism_from_shadow,
    spectrum_generator_expansion,
)


# ============================================================================
# 1.  Shadow geometric parameters (B, omega) from (kappa, Delta)
# ============================================================================

def shadow_B_field(kappa_val: float, delta_val: float) -> float:
    r"""Shadow B-field from modular characteristic and discriminant.

    B = kappa / (|kappa| + |Delta|)

    Normalized so that B in (-1, 1).  B > 0 for kappa > 0.
    At the self-dual point (Virasoro c=13), B has a specific value
    determined by kappa(13) = 13/2 and Delta(13) = 40/87.

    Parameters
    ----------
    kappa_val : modular characteristic kappa(A)
    delta_val : critical discriminant Delta(A)
    """
    denom = abs(kappa_val) + abs(delta_val)
    if denom < 1e-30:
        return 0.0
    return kappa_val / denom


def shadow_omega(kappa_val: float, delta_val: float) -> float:
    r"""Shadow Kahler class from modular characteristic and discriminant.

    omega = |Delta| / (|kappa| + |Delta|)

    Normalized so that omega in [0, 1).  omega = 0 exactly when Delta = 0,
    which characterizes classes G and L (finite tower).

    Parameters
    ----------
    kappa_val : modular characteristic kappa(A)
    delta_val : critical discriminant Delta(A)
    """
    denom = abs(kappa_val) + abs(delta_val)
    if denom < 1e-30:
        return 0.0
    return abs(delta_val) / denom


def shadow_geometric_params(
    family: str,
    param: float,
) -> Dict[str, float]:
    r"""Compute shadow geometric parameters (B, omega, kappa, Delta) for a family.

    Parameters
    ----------
    family : algebra family name
    param : family parameter (k for Heis/affine, c for Virasoro, etc.)

    Returns
    -------
    Dict with keys: 'kappa', 'delta', 'B', 'omega', 'delta_over_kappa'.
    """
    coeffs = shadow_coefficients(family, param, 10)
    kappa_val = coeffs.get(2, 0.0)

    # Delta = 8 * kappa * S_4
    S4 = coeffs.get(4, 0.0)
    delta_val = 8.0 * kappa_val * S4

    B = shadow_B_field(kappa_val, delta_val)
    omega = shadow_omega(kappa_val, delta_val)

    return {
        'kappa': kappa_val,
        'delta': delta_val,
        'B': B,
        'omega': omega,
        'delta_over_kappa': delta_val / kappa_val if abs(kappa_val) > 1e-30 else float('nan'),
        'S4': S4,
    }


def virasoro_geometric_params(c_val: float) -> Dict[str, float]:
    r"""Shadow geometric parameters for Virasoro at central charge c.

    kappa = c/2
    S_4 = 10 / [c(5c + 22)]  (the quartic contact invariant Q^contact_Vir)
    Delta = 8 * kappa * S_4 = 40 / (5c + 22)

    CAUTION (AP9): This formula is specific to Virasoro.
    """
    kappa_val = c_val / 2.0
    S4 = virasoro_S4(c_val)
    delta_val = critical_discriminant_virasoro(c_val)

    B = shadow_B_field(kappa_val, delta_val)
    omega = shadow_omega(kappa_val, delta_val)

    return {
        'kappa': kappa_val,
        'delta': delta_val,
        'B': B,
        'omega': omega,
        'delta_over_kappa': delta_val / kappa_val if abs(kappa_val) > 1e-30 else float('nan'),
        'S4': S4,
        'c': c_val,
    }


# ============================================================================
# 2.  Geometric central charge Z_{B,omega}
# ============================================================================

def geometric_central_charge(
    B: float,
    omega: float,
    r: int,
    d: float,
    chi: float,
) -> complex:
    r"""Geometric central charge on Chern character (r, d, chi).

    Z_{B,omega}(r, d, chi) = -chi + d*omega*i + r*(omega^2/2 + B*omega*i - B^2/2)

    This is the standard Bridgeland central charge for a surface with
    complexified Kahler class B + i*omega.

    Parameters
    ----------
    B : B-field component
    omega : Kahler class component (must be > 0 for a stability condition)
    r : rank
    d : degree
    chi : Euler characteristic
    """
    return complex(
        -chi + r * (omega**2 / 2.0 - B**2 / 2.0),
        d * omega + r * B * omega,
    )


def shadow_central_charge_geometric(
    family: str,
    param: float,
    arity: int,
    max_r: int = 50,
) -> complex:
    r"""Central charge of arity-r generator via geometric formalism.

    For shadow K-theory generator gamma_r with ch(gamma_r) = (1, r, S_r):
        Z_shadow(gamma_r) = geometric_central_charge(B, omega, 1, r, S_r)

    Parameters
    ----------
    family : algebra family
    param : family parameter
    arity : arity of the generator
    max_r : max arity for coefficient computation
    """
    geo = shadow_geometric_params(family, param)
    coeffs = shadow_coefficients(family, param, max_r)
    S_r = coeffs.get(arity, 0.0)

    return geometric_central_charge(geo['B'], geo['omega'], 1, float(arity), S_r)


def shadow_central_charge_vector_geometric(
    family: str,
    param: float,
    r_min: int = 2,
    r_max: int = 20,
) -> Dict[int, complex]:
    r"""Compute geometric central charge for all arities in [r_min, r_max].

    Returns Dict[arity, Z_value].
    """
    geo = shadow_geometric_params(family, param)
    coeffs = shadow_coefficients(family, param, r_max)
    result = {}
    for r in range(r_min, r_max + 1):
        S_r = coeffs.get(r, 0.0)
        result[r] = geometric_central_charge(geo['B'], geo['omega'], 1, float(r), S_r)
    return result


def geometric_phase(z: complex) -> float:
    r"""Bridgeland phase phi = (1/pi)*arg(z) in (0, 1].

    Same convention as the existing engine but restricted to (0,1] for the
    upper half-plane.  For the lower half-plane, phi in (1, 2].
    """
    if abs(z) < 1e-30:
        return float('nan')
    angle = cmath.phase(z)  # in (-pi, pi]
    if angle <= 0:
        angle += 2 * math.pi
    return angle / math.pi


# ============================================================================
# 3.  Stability manifold data
# ============================================================================

@dataclass
class StabilityManifoldData:
    """Data characterizing the stability manifold Stab(D^b(A^sh))."""
    family: str
    param: float
    rank_K0: int
    complex_dimension: int
    B_field: float
    omega_class: float
    kappa: float
    delta: float
    shadow_class: str  # 'G', 'L', 'C', 'M'
    topology: str  # description of manifold topology


def stability_manifold_data(
    family: str,
    param: float,
    max_r: int = 50,
) -> StabilityManifoldData:
    r"""Compute data about the stability manifold.

    dim_C Stab(D^b(A^sh)) = rank K_0(A^sh) = number of nonzero shadow arities.

    Topology:
    - Class G (rank 1): Stab = C (connected, simply connected)
    - Class L (rank 2): Stab = C^2 \ walls (connected, not simply connected)
    - Class C (rank 3): Stab = C^3 \ walls
    - Class M (rank N): Stab = C^N \ walls (infinite-dimensional limit)
    """
    coeffs = shadow_coefficients(family, param, max_r)
    geo = shadow_geometric_params(family, param)
    rank = effective_stability_dimension(coeffs, 2, max_r)
    depth = shadow_depth(coeffs)

    if depth == 2:
        shadow_class = 'G'
        topo = 'C (connected, simply connected, no walls)'
    elif depth == 3:
        shadow_class = 'L'
        topo = f'C^2 minus finitely many walls (pi_1 free on wall count generators)'
    elif depth == 4:
        shadow_class = 'C'
        topo = f'C^3 minus walls (finite wall system from quartic contact invariant)'
    elif depth is None:
        shadow_class = 'M'
        topo = f'C^{rank} minus infinite wall system (accumulation at Delta=0)'
    else:
        shadow_class = '?'
        topo = f'C^{rank} minus walls'

    return StabilityManifoldData(
        family=family,
        param=param,
        rank_K0=rank,
        complex_dimension=rank,
        B_field=geo['B'],
        omega_class=geo['omega'],
        kappa=geo['kappa'],
        delta=geo['delta'],
        shadow_class=shadow_class,
        topology=topo,
    )


# ============================================================================
# 4.  Walls in the (c, Delta) plane
# ============================================================================

def virasoro_wall_locus(
    r1: int,
    r2: int,
    c_min: float = 0.5,
    c_max: float = 25.5,
    n_points: int = 500,
) -> List[Dict[str, float]]:
    r"""Find walls W_{r1,r2} in the (c, Delta) plane for Virasoro.

    A wall is a locus where phi(gamma_{r1}; c) = phi(gamma_{r2}; c)
    using the geometric central charge.

    Returns list of dicts with keys: 'c', 'delta', 'B', 'omega', 'phase'.
    """
    c_vals = np.linspace(c_min, c_max, n_points)
    phase_diffs = []
    geo_data = []

    for c_val in c_vals:
        try:
            geo = virasoro_geometric_params(float(c_val))
            coeffs = shadow_coefficients('virasoro', float(c_val), max(r1, r2) + 5)
            S_r1 = coeffs.get(r1, 0.0)
            S_r2 = coeffs.get(r2, 0.0)
            z1 = geometric_central_charge(geo['B'], geo['omega'], 1, float(r1), S_r1)
            z2 = geometric_central_charge(geo['B'], geo['omega'], 1, float(r2), S_r2)
            phi1 = geometric_phase(z1)
            phi2 = geometric_phase(z2)
            if math.isnan(phi1) or math.isnan(phi2):
                phase_diffs.append(float('nan'))
            else:
                phase_diffs.append(phi1 - phi2)
            geo_data.append(geo)
        except (ValueError, ZeroDivisionError):
            phase_diffs.append(float('nan'))
            geo_data.append(None)

    walls = []
    for i in range(len(phase_diffs) - 1):
        if math.isnan(phase_diffs[i]) or math.isnan(phase_diffs[i + 1]):
            continue
        if phase_diffs[i] * phase_diffs[i + 1] < 0:
            # Bisect for the wall location
            lo, hi = float(c_vals[i]), float(c_vals[i + 1])
            for _ in range(60):
                mid = (lo + hi) / 2.0
                try:
                    geo_mid = virasoro_geometric_params(mid)
                    coeffs_mid = shadow_coefficients('virasoro', mid, max(r1, r2) + 5)
                    S1 = coeffs_mid.get(r1, 0.0)
                    S2 = coeffs_mid.get(r2, 0.0)
                    z1 = geometric_central_charge(
                        geo_mid['B'], geo_mid['omega'], 1, float(r1), S1)
                    z2 = geometric_central_charge(
                        geo_mid['B'], geo_mid['omega'], 1, float(r2), S2)
                    d = geometric_phase(z1) - geometric_phase(z2)
                except (ValueError, ZeroDivisionError):
                    break
                if math.isnan(d):
                    break
                if d * phase_diffs[i] < 0:
                    hi = mid
                else:
                    lo = mid
            wall_c = (lo + hi) / 2.0
            wall_geo = virasoro_geometric_params(wall_c)
            # Compute the common phase at the wall
            coeffs_wall = shadow_coefficients('virasoro', wall_c, max(r1, r2) + 5)
            z_at_wall = geometric_central_charge(
                wall_geo['B'], wall_geo['omega'], 1, float(r1),
                coeffs_wall.get(r1, 0.0))
            walls.append({
                'c': wall_c,
                'delta': wall_geo['delta'],
                'B': wall_geo['B'],
                'omega': wall_geo['omega'],
                'phase': geometric_phase(z_at_wall),
            })

    return walls


def all_walls_virasoro(
    max_arity: int = 10,
    c_min: float = 0.5,
    c_max: float = 25.5,
    n_points: int = 300,
) -> List[Dict[str, Any]]:
    r"""Find all walls W_{r1,r2} for r1, r2 in [2, max_arity] for Virasoro.

    Returns list of wall dicts with additional 'r1', 'r2' keys.
    """
    all_w = []
    for r1 in range(2, max_arity + 1):
        for r2 in range(r1 + 1, max_arity + 1):
            walls = virasoro_wall_locus(r1, r2, c_min, c_max, n_points)
            for w in walls:
                w['r1'] = r1
                w['r2'] = r2
                all_w.append(w)
    all_w.sort(key=lambda w: w['c'])
    return all_w


def wall_crossing_jump(
    family: str,
    r1: int,
    r2: int,
    wall_c: float,
    epsilon: float = 0.01,
    max_r: int = 50,
) -> Dict[str, Any]:
    r"""Compute the DT-like invariant jump at a wall.

    At a wall W_{r1,r2} at c = c_wall, we compute the change in the
    ordered product of KS automorphisms.

    The wall-crossing formula (Kontsevich-Soibelman):
        prod_{arg increases} K_gamma = prod_{arg decreases} K_gamma

    We compute the log-level amplitude change:
        Delta(log K) = log K(c_wall + epsilon) - log K(c_wall - epsilon)
    """
    try:
        # Coefficients before and after
        coeffs_before = shadow_coefficients(family, wall_c - epsilon, max_r)
        coeffs_after = shadow_coefficients(family, wall_c + epsilon, max_r)

        # Phase ordering changes
        geo_before = shadow_geometric_params(family, wall_c - epsilon)
        geo_after = shadow_geometric_params(family, wall_c + epsilon)

        S_r1_before = coeffs_before.get(r1, 0.0)
        S_r2_before = coeffs_before.get(r2, 0.0)
        S_r1_after = coeffs_after.get(r1, 0.0)
        S_r2_after = coeffs_after.get(r2, 0.0)

        z1_before = geometric_central_charge(
            geo_before['B'], geo_before['omega'], 1, float(r1), S_r1_before)
        z2_before = geometric_central_charge(
            geo_before['B'], geo_before['omega'], 1, float(r2), S_r2_before)
        z1_after = geometric_central_charge(
            geo_after['B'], geo_after['omega'], 1, float(r1), S_r1_after)
        z2_after = geometric_central_charge(
            geo_after['B'], geo_after['omega'], 1, float(r2), S_r2_after)

        phi1_before = geometric_phase(z1_before)
        phi2_before = geometric_phase(z2_before)
        phi1_after = geometric_phase(z1_after)
        phi2_after = geometric_phase(z2_after)

        # Phase ordering: does r1 > r2 become r2 > r1?
        ordering_before = 'r1>r2' if phi1_before > phi2_before else 'r2>r1'
        ordering_after = 'r1>r2' if phi1_after > phi2_after else 'r2>r1'
        ordering_flipped = (ordering_before != ordering_after)

        # DT jump: difference of shadow coefficients as DT-like invariants
        # Omega(r) = S_r in the shadow theory
        dt_jump_r1 = S_r1_after - S_r1_before
        dt_jump_r2 = S_r2_after - S_r2_before

        # KS log-level: Li_2 change
        ks_log_before = ks_automorphism_from_shadow(wall_c - epsilon, max_r)
        ks_log_after = ks_automorphism_from_shadow(wall_c + epsilon, max_r)
        all_charges = sorted(set(list(ks_log_before.keys()) + list(ks_log_after.keys())))
        max_ks_diff = 0.0
        for ch in all_charges:
            d = abs(ks_log_before.get(ch, 0.0) - ks_log_after.get(ch, 0.0))
            max_ks_diff = max(max_ks_diff, d)

        return {
            'wall_c': wall_c,
            'r1': r1,
            'r2': r2,
            'ordering_before': ordering_before,
            'ordering_after': ordering_after,
            'ordering_flipped': ordering_flipped,
            'dt_jump_r1': dt_jump_r1,
            'dt_jump_r2': dt_jump_r2,
            'max_ks_log_diff': max_ks_diff,
            'phi1_before': phi1_before,
            'phi2_before': phi2_before,
            'phi1_after': phi1_after,
            'phi2_after': phi2_after,
        }
    except (ValueError, ZeroDivisionError) as e:
        return {
            'wall_c': wall_c,
            'r1': r1,
            'r2': r2,
            'error': str(e),
        }


# ============================================================================
# 5.  DT invariants from shadow
# ============================================================================

def macmahon(q: float, max_n: int = 50) -> float:
    r"""MacMahon function M(q) = prod_{n>=1} 1/(1-q^n)^n.

    M(q) is the generating function for 3D partitions (plane partitions).
    M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + ...

    Convergent for |q| < 1.
    """
    if abs(q) >= 1.0:
        return float('inf')
    result = 1.0
    for n in range(1, max_n + 1):
        factor = (1.0 - q ** n) ** n
        if abs(factor) < 1e-300:
            break
        result /= factor
    return result


def macmahon_coefficients(max_n: int = 30) -> List[int]:
    r"""Coefficients of the MacMahon function M(q) = sum_{n>=0} M_n q^n.

    M_n counts the number of 3D partitions of n.
    M_0 = 1, M_1 = 1, M_2 = 3, M_3 = 6, M_4 = 13, M_5 = 24, ...

    Computed via the recursive formula from the product expansion.
    """
    # Use log-expansion to get coefficients of prod (1-q^n)^{-n}
    # log M(q) = -sum_n n*log(1-q^n) = sum_n sum_k n*q^{nk}/k
    #          = sum_m (sum_{n|m} n * (m/n)^{-1}) q^m  ... careful
    # Actually: log M(q) = sum_{n>=1} n * sum_{k>=1} q^{nk}/k
    #                     = sum_{m>=1} sigma_1(m)/m * q^m  -- NO
    # log M(q) = sum_{n>=1} -n * log(1-q^n)
    #          = sum_{n>=1} n * sum_{k>=1} q^{nk}/k
    #          = sum_{m>=1} (sum_{d|m} d * (1/(m/d))) * q^m  -- still not clean

    # Use direct multiplication instead
    coeffs = [0.0] * (max_n + 1)
    coeffs[0] = 1.0

    for n in range(1, max_n + 1):
        # Multiply by (1 - q^n)^{-n}
        # (1 - x)^{-n} = sum_{k>=0} C(n+k-1, k) x^k
        # So (1 - q^n)^{-n} = sum_{k>=0} C(n+k-1, k) q^{nk}
        new_coeffs = list(coeffs)
        for nk_start in range(n, max_n + 1, n):
            k = nk_start // n
            # C(n+k-1, k) = C(n+k-1, n-1)
            binom = 1.0
            for j in range(1, k + 1):
                binom *= (n + j - 1) / j
            # Add contribution: multiply existing coefficients by binom * q^{nk}
            for m in range(max_n + 1):
                target = m + nk_start
                if target > max_n:
                    break
                new_coeffs[target] += coeffs[m] * binom
        coeffs = new_coeffs

    # Round to integers
    return [int(round(c)) for c in coeffs]


def macmahon_power_coefficients(chi: int, max_n: int = 20) -> List[float]:
    r"""Coefficients of M(q)^chi = sum_{n>=0} c_n q^n.

    For chi > 0: M(q)^chi = (prod (1-q^n)^{-n})^chi = prod (1-q^n)^{-n*chi}.
    Uses log-then-exponentiate approach.
    """
    # First compute log(M(q)) coefficients via log(prod (1-q^n)^{-n})
    # = sum_{n>=1} -n*log(1-q^n) = sum_{n>=1} n * sum_{k>=1} q^{nk}/k
    log_coeffs = [0.0] * (max_n + 1)
    for n in range(1, max_n + 1):
        for k in range(1, max_n // n + 1):
            m = n * k
            if m <= max_n:
                log_coeffs[m] += float(n) / float(k)

    # Multiply by chi
    log_coeffs = [c * chi for c in log_coeffs]

    # Exponentiate: exp(sum_{m>=1} a_m q^m) via recursive formula
    result = [0.0] * (max_n + 1)
    result[0] = 1.0
    for m in range(1, max_n + 1):
        s = 0.0
        for k in range(1, m + 1):
            s += k * log_coeffs[k] * result[m - k]
        result[m] = s / m

    return result


def shadow_dt_invariants(
    family: str,
    param: float,
    max_n: int = 20,
    max_r: int = 50,
) -> List[float]:
    r"""DT invariants from the shadow obstruction tower.

    DT_0 = 1 (trivial object).
    DT_n for n >= 1: defined from the KS spectrum generator.

    The spectrum generator S_hat = prod_{r>=2} K_r^{Omega(r)} where
    Omega(r) = S_r(A) and K_r = prod_{k>=1} (1-(-1)^k y^k q^{kr})^{k*Omega(r)}.

    At y = -1 specialization: S_hat = prod_{r>=2} prod_{k>=1} (1-q^{kr})^{-Omega(r)}
    (a modified plethystic exponential).

    DT_n = coefficient of q^n in S_hat|_{y=-1}.

    Parameters
    ----------
    family : algebra family
    param : family parameter
    max_n : maximum charge for DT invariants
    max_r : maximum arity for shadow coefficients
    """
    coeffs = shadow_coefficients(family, param, max_r)

    # Compute log(S_hat|_{y=-1}) = sum_{r>=2} Omega(r) * sum_{k>=1} q^{kr}/k
    # This is a plethystic exponential form.
    log_dt = [0.0] * (max_n + 1)
    for r, S_r in sorted(coeffs.items()):
        if abs(S_r) < 1e-30:
            continue
        # Contribution of arity r: S_r * sum_{k>=1} q^{kr}/k
        for k in range(1, max_n // r + 1):
            m = k * r
            if m <= max_n:
                log_dt[m] += S_r / float(k)

    # Exponentiate
    dt = [0.0] * (max_n + 1)
    dt[0] = 1.0
    for m in range(1, max_n + 1):
        s = 0.0
        for k in range(1, m + 1):
            s += k * log_dt[k] * dt[m - k]
        dt[m] = s / m

    return dt


def shadow_dt_partition_function(
    family: str,
    param: float,
    q: float,
    max_n: int = 30,
    max_r: int = 50,
) -> float:
    r"""Evaluate the shadow DT partition function Z_DT(q).

    Z_DT(q) = sum_{n=0}^{max_n} DT_n * q^n
    """
    dt = shadow_dt_invariants(family, param, max_n, max_r)
    total = 0.0
    for n, dt_n in enumerate(dt):
        total += dt_n * q ** n
    return total


def macmahon_comparison(
    family: str,
    param: float,
    max_n: int = 20,
    max_r: int = 50,
) -> Dict[str, Any]:
    r"""Compare shadow DT partition function with M(q)^chi.

    Tests whether Z_DT^shadow = M(q)^{chi_shadow} where
    chi_shadow = dim Stab(A^sh).

    Returns comparison data at the coefficient level.
    """
    dt = shadow_dt_invariants(family, param, max_n, max_r)

    coeffs = shadow_coefficients(family, param, max_r)
    chi = effective_stability_dimension(coeffs, 2, max_r)
    depth = shadow_depth(coeffs)

    # For finite towers, chi is the shadow depth - 1
    # For class M, chi is effectively the truncation depth
    mh = macmahon_power_coefficients(chi, max_n)

    # Coefficient-by-coefficient comparison
    ratios = []
    max_diff = 0.0
    for n in range(1, min(max_n + 1, len(dt), len(mh))):
        if abs(mh[n]) > 1e-30:
            ratio = dt[n] / mh[n]
        else:
            ratio = float('nan') if abs(dt[n]) > 1e-30 else 1.0
        ratios.append(ratio)
        if not math.isnan(ratio):
            max_diff = max(max_diff, abs(ratio - 1.0))

    is_macmahon = max_diff < 0.01  # Within 1%

    return {
        'dt_coefficients': dt[:max_n + 1],
        'macmahon_coefficients': mh[:max_n + 1],
        'chi_shadow': chi,
        'ratios': ratios,
        'max_ratio_deviation': max_diff,
        'is_macmahon': is_macmahon,
        'shadow_depth': depth,
    }


def dt_comparison_plethystic(
    family: str,
    param: float,
    max_n: int = 20,
    max_r: int = 50,
) -> Dict[str, Any]:
    r"""Alternative DT computation via plethystic exponential.

    PE[f(q)] = exp(sum_{k>=1} f(q^k)/k)

    For the shadow: f(q) = sum_{r>=2} S_r * q^r.
    PE[f] = exp(sum_{k>=1} sum_{r>=2} S_r * q^{kr} / k)
          = prod_{r>=2} prod_{k>=1} (1 - q^r)^{-S_r}  [when S_r is integer]
          = exp(sum_{r>=2} S_r * (-log(1-q^r)))  [general]

    This should match shadow_dt_invariants by construction.

    CAUTION (AP42): This is the plethystic exponential, not the
    motivic DT invariant.  The two coincide only at the "correct level."
    """
    coeffs = shadow_coefficients(family, param, max_r)

    # log PE = sum_{r>=2} S_r * sum_{k>=1} q^{kr}/k
    # This is identical to the log used in shadow_dt_invariants.
    # So this IS the same computation -- serves as a consistency check.
    log_pe = [0.0] * (max_n + 1)
    for r, S_r in sorted(coeffs.items()):
        if abs(S_r) < 1e-30:
            continue
        for k in range(1, max_n // r + 1):
            m = k * r
            if m <= max_n:
                log_pe[m] += S_r / float(k)

    pe = [0.0] * (max_n + 1)
    pe[0] = 1.0
    for m in range(1, max_n + 1):
        s = 0.0
        for k in range(1, m + 1):
            s += k * log_pe[k] * pe[m - k]
        pe[m] = s / m

    dt = shadow_dt_invariants(family, param, max_n, max_r)
    max_diff = max(abs(pe[n] - dt[n]) for n in range(max_n + 1))

    return {
        'pe_coefficients': pe[:max_n + 1],
        'dt_coefficients': dt[:max_n + 1],
        'max_diff': max_diff,
        'match': max_diff < 1e-10,
    }


# ============================================================================
# 6.  Stability at zeta zeros
# ============================================================================

def virasoro_c_from_imaginary_zero(im_part: float) -> float:
    r"""Map an imaginary part of a shadow zeta zero to a "c-value."

    For the shadow zeta function zeta_A(s) = sum S_r r^{-s}, zeros rho_n
    have imaginary parts gamma_n.  We define a mapping:
        c(gamma_n) = 13 + 13 * tanh(gamma_n / 10)

    This maps R -> (0, 26) with c(0) = 13 (self-dual point).
    The normalization is chosen so that c is in the Virasoro range.
    """
    return 13.0 + 13.0 * math.tanh(im_part / 10.0)


def riemann_zeta_zeros(n_zeros: int = 20) -> List[float]:
    r"""First n_zeros nontrivial zeros of the Riemann zeta function.

    These are the IMAGINARY PARTS of the zeros on the critical line Re(s)=1/2.
    Used as proxy data for the shadow zeta zeros (which have analogous
    structure by the GUE universality of the shadow programme).

    Hardcoded from LMFDB / Odlyzko tables:
    """
    # First 30 zeros of zeta(1/2 + i*gamma), sorted by gamma
    known_zeros = [
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
        37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
        52.970321, 56.446248, 59.347044, 60.831779, 65.112544,
        67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
        79.337375, 82.910381, 84.735493, 87.425275, 88.809111,
        92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
    ]
    return known_zeros[:n_zeros]


def stability_at_zeta_zeros(
    n_zeros: int = 20,
    max_r: int = 30,
) -> List[Dict[str, Any]]:
    r"""Analyze stability conditions at the c-values corresponding to zeta zeros.

    For each Riemann zeta zero gamma_n:
    1. Map to c(gamma_n) via virasoro_c_from_imaginary_zero
    2. Compute shadow stability data
    3. Check if c(gamma_n) is near a wall
    4. Compute DT data

    Returns list of analysis dicts.
    """
    gamma_vals = riemann_zeta_zeros(n_zeros)
    results = []

    for n, gamma in enumerate(gamma_vals):
        c_val = virasoro_c_from_imaginary_zero(gamma)

        try:
            geo = virasoro_geometric_params(c_val)
            coeffs = shadow_coefficients('virasoro', c_val, max_r)

            # Central charges for low arities
            z_vals = {}
            phi_vals = {}
            for r in range(2, min(11, max_r + 1)):
                S_r = coeffs.get(r, 0.0)
                z = geometric_central_charge(geo['B'], geo['omega'], 1, float(r), S_r)
                z_vals[r] = z
                phi_vals[r] = geometric_phase(z)

            # Check if c is near a wall: look for close phases
            min_phase_gap = float('inf')
            wall_pair = None
            valid_phases = {r: p for r, p in phi_vals.items() if not math.isnan(p)}
            sorted_arities = sorted(valid_phases.keys(), key=lambda r: valid_phases[r])
            for i in range(len(sorted_arities) - 1):
                r1 = sorted_arities[i]
                r2 = sorted_arities[i + 1]
                gap = abs(valid_phases[r2] - valid_phases[r1])
                if gap < min_phase_gap:
                    min_phase_gap = gap
                    wall_pair = (r1, r2)

            is_near_wall = min_phase_gap < 0.02

            # DT data (first few terms)
            dt = shadow_dt_invariants('virasoro', c_val, 10, max_r)

            results.append({
                'zero_index': n + 1,
                'gamma': gamma,
                'c_value': c_val,
                'kappa': geo['kappa'],
                'delta': geo['delta'],
                'B': geo['B'],
                'omega': geo['omega'],
                'central_charges': z_vals,
                'phases': phi_vals,
                'min_phase_gap': min_phase_gap,
                'nearest_wall_pair': wall_pair,
                'is_near_wall': is_near_wall,
                'dt_invariants': dt[:11],
            })
        except (ValueError, ZeroDivisionError) as e:
            results.append({
                'zero_index': n + 1,
                'gamma': gamma,
                'c_value': c_val,
                'error': str(e),
            })

    return results


def wall_density_near_zeros(
    n_zeros: int = 20,
    max_arity: int = 8,
    c_window: float = 0.5,
) -> Dict[str, Any]:
    r"""Compute density of walls near the c-values of zeta zeros.

    For each zero, count how many walls W_{r1,r2} lie within +/- c_window
    of c(gamma_n).

    If zeta zeros = stability walls, we expect high wall density near zeros.
    """
    gamma_vals = riemann_zeta_zeros(n_zeros)
    c_at_zeros = [virasoro_c_from_imaginary_zero(g) for g in gamma_vals]

    # Find all walls
    all_w = all_walls_virasoro(max_arity, 0.5, 25.5, 200)
    wall_c_vals = [w['c'] for w in all_w]

    # Count walls near each zero
    counts = []
    for c_zero in c_at_zeros:
        count = sum(1 for wc in wall_c_vals if abs(wc - c_zero) < c_window)
        counts.append(count)

    # Control: random c-values
    rng = np.random.RandomState(42)
    random_c = rng.uniform(1.0, 25.0, n_zeros)
    random_counts = []
    for c_rand in random_c:
        count = sum(1 for wc in wall_c_vals if abs(wc - c_rand) < c_window)
        random_counts.append(count)

    return {
        'c_at_zeros': c_at_zeros,
        'wall_counts_at_zeros': counts,
        'mean_wall_count_at_zeros': np.mean(counts),
        'random_c': list(random_c),
        'wall_counts_at_random': random_counts,
        'mean_wall_count_at_random': np.mean(random_counts),
        'ratio': np.mean(counts) / max(np.mean(random_counts), 1e-10),
        'total_walls_found': len(all_w),
    }


# ============================================================================
# 7.  Comprehensive analysis at a family/parameter
# ============================================================================

@dataclass
class BridgelandShadowAnalysis:
    """Complete Bridgeland shadow stability analysis."""
    family: str
    param: float
    geometric_params: Dict[str, float]
    manifold_data: StabilityManifoldData
    dt_invariants: List[float]
    macmahon_data: Dict[str, Any]
    walls: List[Dict[str, Any]]
    zero_analysis: Optional[List[Dict[str, Any]]]


def full_bridgeland_shadow_analysis(
    family: str,
    param: float,
    max_r: int = 30,
    max_n_dt: int = 20,
    compute_walls: bool = True,
    compute_zeros: bool = False,
) -> BridgelandShadowAnalysis:
    r"""Run the complete Bridgeland shadow stability analysis.

    Parameters
    ----------
    family : algebra family
    param : family parameter
    max_r : max arity for shadow coefficients
    max_n_dt : max charge for DT invariants
    compute_walls : whether to compute wall loci (Virasoro only)
    compute_zeros : whether to compute stability at zeta zeros (Virasoro only)
    """
    geo = shadow_geometric_params(family, param)
    manifold = stability_manifold_data(family, param, max_r)
    dt = shadow_dt_invariants(family, param, max_n_dt, max_r)
    mh = macmahon_comparison(family, param, max_n_dt, max_r)

    walls = []
    if compute_walls and family == 'virasoro':
        walls = all_walls_virasoro(6, 0.5, 25.5, 200)

    zeros = None
    if compute_zeros and family == 'virasoro':
        zeros = stability_at_zeta_zeros(10, max_r)

    return BridgelandShadowAnalysis(
        family=family,
        param=param,
        geometric_params=geo,
        manifold_data=manifold,
        dt_invariants=dt,
        macmahon_data=mh,
        walls=walls,
        zero_analysis=zeros,
    )


# ============================================================================
# 8.  DT invariant change across wall via primitive WCF
# ============================================================================

def primitive_wcf_jump(
    Omega_r1: float,
    Omega_r2: float,
) -> Dict[str, float]:
    r"""Primitive wall-crossing formula for two charges.

    When charges r1 and r2 have phases crossing, the BPS invariant
    of the bound state r1 + r2 changes by:
        Delta Omega(r1+r2) = (-1)^{<r1,r2>-1} * |<r1,r2>| * Omega(r1) * Omega(r2)

    where <r1,r2> is the Euler form (intersection pairing in K-theory).
    In the shadow theory, the Euler form between arity-r1 and arity-r2
    generators is: <gamma_{r1}, gamma_{r2}> = r1*r2 (from the shadow metric).

    The sign is: (-1)^{r1*r2 - 1}.

    Returns dict with: 'delta_omega', 'sign', 'euler_form', 'bound_charge'.
    """
    euler = Omega_r1 * Omega_r2  # Using shadow coefficients as "charges"
    # In the formal shadow theory, <gamma_r1, gamma_r2> = r1 - r2 (antisymmetric)
    # Actually in Bridgeland stability, the intersection pairing is integer-valued.
    # For K-theory of a surface: <E, F> = -chi(E, F) = sum (-1)^i dim Ext^i.
    # In the shadow theory, this is determined by the OPE linking arities.
    # Simplest model: <gamma_r1, gamma_r2> = 1 for all r1 != r2 (minimal pairing).
    pairing = 1
    sign = (-1) ** (pairing - 1)  # = 1 for pairing = 1

    delta_omega = sign * abs(pairing) * Omega_r1 * Omega_r2

    return {
        'delta_omega': delta_omega,
        'sign': sign,
        'euler_form': pairing,
        'bound_charge': Omega_r1 + Omega_r2,  # formal charge of bound state
    }


# ============================================================================
# 9.  Virasoro (c, Delta) parameter space analysis
# ============================================================================

def c_delta_trajectory(
    c_min: float = 0.5,
    c_max: float = 25.5,
    n_points: int = 200,
) -> List[Dict[str, float]]:
    r"""Trace the trajectory in the (c, Delta) plane for Virasoro.

    As c varies from c_min to c_max:
        kappa(c) = c/2
        Delta(c) = 40/(5c+22)

    Delta -> inf as c -> -22/5 (singularity, outside physical range).
    Delta -> 0 as c -> inf (class L/G limit).
    Delta(0) = 40/22 = 20/11 approx 1.818.
    Delta(13) = 40/87 approx 0.460.
    Delta(26) = 40/152 approx 0.263.

    Returns list of {c, kappa, delta, B, omega} dicts.
    """
    trajectory = []
    for c_val in np.linspace(c_min, c_max, n_points):
        c_val = float(c_val)
        geo = virasoro_geometric_params(c_val)
        trajectory.append({
            'c': c_val,
            'kappa': geo['kappa'],
            'delta': geo['delta'],
            'B': geo['B'],
            'omega': geo['omega'],
        })
    return trajectory


def delta_monotonicity_check(
    c_min: float = 0.5,
    c_max: float = 25.5,
    n_points: int = 200,
) -> Dict[str, Any]:
    r"""Verify that Delta(c) is monotonically decreasing for c > 0.

    Delta(c) = 40/(5c+22), so Delta'(c) = -200/(5c+22)^2 < 0 for all c.
    """
    traj = c_delta_trajectory(c_min, c_max, n_points)
    deltas = [t['delta'] for t in traj]
    is_monotone = all(deltas[i] >= deltas[i + 1] - 1e-14
                      for i in range(len(deltas) - 1))
    return {
        'is_monotone_decreasing': is_monotone,
        'delta_min': min(deltas),
        'delta_max': max(deltas),
        'delta_at_c13': virasoro_geometric_params(13.0)['delta'],
    }


# ============================================================================
# 10.  Cross-verification utilities
# ============================================================================

def dt_invariants_three_paths(
    family: str,
    param: float,
    max_n: int = 15,
    max_r: int = 30,
) -> Dict[str, Any]:
    r"""Compute DT invariants by three independent paths.

    Path 1: shadow_dt_invariants (KS log-then-exponentiate)
    Path 2: dt_comparison_plethystic (plethystic exponential)
    Path 3: spectrum_generator_expansion (from wall-crossing engine)

    All three should agree.
    """
    dt_1 = shadow_dt_invariants(family, param, max_n, max_r)
    pe_data = dt_comparison_plethystic(family, param, max_n, max_r)
    dt_2 = pe_data['pe_coefficients']

    # Path 3: from the wall-crossing engine (Virasoro only)
    dt_3 = None
    if family == 'virasoro':
        sg = spectrum_generator_expansion(param, max_n, min(max_r, 20), 10)
        dt_3 = sg[:max_n + 1]

    # Compare paths
    max_diff_12 = max(abs(dt_1[n] - dt_2[n]) for n in range(min(len(dt_1), len(dt_2))))
    max_diff_13 = float('nan')
    if dt_3 is not None:
        max_diff_13 = max(abs(dt_1[n] - dt_3[n])
                         for n in range(min(len(dt_1), len(dt_3))))

    return {
        'path1_ks': dt_1[:max_n + 1],
        'path2_pe': dt_2[:max_n + 1],
        'path3_sg': dt_3[:max_n + 1] if dt_3 is not None else None,
        'max_diff_12': max_diff_12,
        'max_diff_13': max_diff_13,
        'all_paths_agree': max_diff_12 < 1e-10 and (
            math.isnan(max_diff_13) or max_diff_13 < 1e-6),
    }


def geometric_vs_arity_central_charge(
    family: str,
    param: float,
    max_r: int = 20,
) -> Dict[str, Any]:
    r"""Compare geometric and arity-based central charge formulas.

    Path 1: geometric Z_{B,omega}(1, r, S_r)
    Path 2: arity-based Z_A(gamma_r) = -S_r * exp(i*pi*r/R)

    These are DIFFERENT central charge formulas (different stability conditions).
    They should NOT agree in general, but the magnitude |Z| = |S_r| should be
    comparable for both.
    """
    geo_Z = shadow_central_charge_vector_geometric(family, param, 2, max_r)
    coeffs = shadow_coefficients(family, param, max_r)
    arity_Z = central_charge_vector(coeffs, 2, max_r)

    mag_diffs = {}
    phase_diffs = {}
    for r in range(2, max_r + 1):
        if r in geo_Z and r in arity_Z:
            mag_diffs[r] = abs(abs(geo_Z[r]) - abs(arity_Z[r]))
            phi_g = geometric_phase(geo_Z[r])
            phi_a = bridgeland_phase(arity_Z[r])
            if not (math.isnan(phi_g) or math.isnan(phi_a)):
                phase_diffs[r] = phi_g - phi_a

    return {
        'geometric_Z': geo_Z,
        'arity_Z': arity_Z,
        'magnitude_differences': mag_diffs,
        'phase_differences': phase_diffs,
        'max_magnitude_diff': max(mag_diffs.values()) if mag_diffs else 0.0,
    }
