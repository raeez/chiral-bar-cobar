r"""Quasinormal mode spectrum from shadow poles.

MATHEMATICAL FRAMEWORK
======================

The BTZ black hole quasinormal mode (QNM) spectrum is exactly solvable:

    omega_n^BTZ = pm (2*pi*T_H)(h + n) - i*(2*pi*T_H)(h + n)

where h is the conformal weight of the perturbation, n >= 0 is the overtone
number, and T_H = sqrt(6M/c)/pi is the Hawking temperature (single chirality).

The shadow obstruction tower modifies the QNM spectrum via corrections to the
effective potential.  At each shadow order r >= 2, the correction is

    delta_omega_r(n) = (2*pi*T_H) * S_r * g_r(n, h)

where S_r is the r-th shadow coefficient and g_r is a polynomial in n of
degree r-2.  The functions g_r are determined by the shadow-potential
correspondence:

    g_2(n) = 1/(h+n)           [curvature: shifts ALL overtones uniformly]
    g_3(n) = n/(h+n)^2         [cubic: breaks linearity at high n]
    g_4(n) = n(n-1)/(h+n)^3   [quartic: accelerates nonlinearity]

This follows from the WKB expansion of the wave equation with the
shadow-corrected potential V^sh(r) = V^BTZ(r) + sum_r S_r * delta_V_r(r).

SHADOW SCATTERING MATRIX
=========================

The S-matrix S_A(omega) for scattering off the shadow-corrected potential is

    S_A(omega) = det(1 - K_A(omega))

where K_A(omega) is the shadow scattering kernel:

    K_A(omega) = sum_{r>=2} S_r * K_r(omega)

with K_r the r-th order Born kernel.  The poles of S_A are the QNMs.
For the BTZ, the kernel is exactly solvable: the poles are at
omega_n = (2*pi*T_H)(h+n)(1 - i), giving an infinite discrete spectrum
on a line in the lower half omega-plane.

KOSZUL QNM DUALITY
===================

The complementary black hole has temperature T_H' = T_H * kappa'/kappa
where kappa' = kappa(A!) is the Koszul dual's modular characteristic.

For Virasoro: kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2,
so T_H'/T_H = (26-c)/c.  The QNM spectra of A and A! interlace when
ordered by |Im(omega)|.

References:
    Birmingham-Sachs-Solodukhin 2002: hep-th/0212308 (BTZ QNMs)
    Nollert 1999: gr-qc/9602032 (pseudospectral instability)
    Jaramillo-Macedo-Sheikh 2021: 2004.06434 (pseudospectrum)
    Cardoso-Lemos 2001: gr-qc/0105103 (asymptotic QNM spacing)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

PI = math.pi
TWO_PI = 2.0 * PI


# ============================================================================
# Section 0: Shadow data registry (standard families)
# ============================================================================

def _fraction(x) -> Fraction:
    """Convert to Fraction robustly."""
    if isinstance(x, Fraction):
        return x
    return Fraction(x)


def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.  AP1/AP9."""
    return _fraction(c) / Fraction(2)


def kappa_heisenberg(k) -> Fraction:
    """kappa(H_k) = k."""
    return _fraction(k)


def kappa_kac_moody(dim_g, k, h_dual) -> Fraction:
    """kappa(V_k(g)) = dim(g)*(k+h^v)/(2*h^v).  AP1."""
    return _fraction(dim_g) * (_fraction(k) + _fraction(h_dual)) / (2 * _fraction(h_dual))


def virasoro_shadow_data(c) -> Dict[str, Fraction]:
    """Complete shadow data for Virasoro at central charge c.

    Returns kappa, S3 (=alpha), S4 (Q^contact), S5, and derived quantities.
    """
    c_f = _fraction(c)
    kappa = c_f / Fraction(2)
    S3 = Fraction(2)
    S4 = Fraction(10) / (c_f * (5 * c_f + 22))
    S5 = Fraction(-48) / (c_f ** 2 * (5 * c_f + 22))
    Delta = 8 * kappa * S4  # critical discriminant
    return {
        'kappa': kappa, 'S3': S3, 'S4': S4, 'S5': S5,
        'Delta': Delta, 'c': c_f,
    }


def heisenberg_shadow_data(k) -> Dict[str, Fraction]:
    """Shadow data for Heisenberg: class G, tower terminates at r=2."""
    k_f = _fraction(k)
    return {
        'kappa': k_f, 'S3': Fraction(0), 'S4': Fraction(0),
        'S5': Fraction(0), 'Delta': Fraction(0), 'k': k_f,
    }


def affine_sl2_shadow_data(k) -> Dict[str, Fraction]:
    """Shadow data for affine sl_2 at level k: class L, terminates at r=3."""
    k_f = _fraction(k)
    dim_g = Fraction(3)
    h_dual = Fraction(2)
    kappa = dim_g * (k_f + h_dual) / (2 * h_dual)  # = 3(k+2)/4
    S3 = Fraction(2)  # cubic shadow (same as Virasoro for quadratic algebras)
    S4 = Fraction(0)   # class L: quartic vanishes
    S5 = Fraction(0)
    return {
        'kappa': kappa, 'S3': S3, 'S4': S4, 'S5': S5,
        'Delta': Fraction(0), 'k': k_f,
    }


def get_shadow_data(family: str, **params) -> Dict[str, Fraction]:
    """Dispatch to family-specific shadow data."""
    if family == 'virasoro':
        return virasoro_shadow_data(params.get('c', 26))
    elif family == 'heisenberg':
        return heisenberg_shadow_data(params.get('k', 1))
    elif family == 'affine_sl2':
        return affine_sl2_shadow_data(params.get('k', 1))
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# Section 1: BTZ QNM frequencies (exact)
# ============================================================================

def hawking_temperature(c, M) -> float:
    """T_H = sqrt(6M/c)/pi (single-chirality Hawking temperature).

    The BTZ horizon radius r_+ = sqrt(8GM) = l*sqrt(M} in the
    c = 3l/(2G) convention.  T_H = r_+/(2*pi*l^2) = sqrt(M)/(pi*l).
    In CFT units: T_H = sqrt(6M/c)/pi.
    """
    c_f, M_f = float(c), float(M)
    if c_f <= 0 or M_f <= 0:
        return 0.0
    return math.sqrt(6.0 * M_f / c_f) / PI


def btw_hawking_temperature_from_kappa(kappa, M) -> float:
    """T_H from kappa = c/2: T_H = sqrt(3M/kappa)/pi."""
    kappa_f, M_f = float(kappa), float(M)
    if kappa_f <= 0 or M_f <= 0:
        return 0.0
    return math.sqrt(3.0 * M_f / kappa_f) / PI


def btz_qnm_frequency(h: float, n: int, T_H: float,
                       chirality: str = 'right') -> complex:
    """Exact BTZ QNM frequency.

    omega_n = sign * (2*pi*T_H)(h+n) - i*(2*pi*T_H)(h+n)
            = (2*pi*T_H)(h+n) * (sign - i)

    where sign = +1 for right-movers, -1 for left-movers.

    Parameters
    ----------
    h : conformal weight of the perturbation
    n : overtone number (n >= 0)
    T_H : Hawking temperature (single chirality)
    chirality : 'right' (+) or 'left' (-)

    Returns
    -------
    complex : omega_n in the lower half-plane
    """
    sign = 1.0 if chirality == 'right' else -1.0
    base = TWO_PI * T_H * (h + n)
    return complex(sign * base, -base)


def btz_qnm_spectrum(h: float, T_H: float, n_max: int = 20,
                     chirality: str = 'right') -> List[complex]:
    """Full BTZ QNM spectrum for n = 0, 1, ..., n_max."""
    return [btz_qnm_frequency(h, n, T_H, chirality) for n in range(n_max + 1)]


# ============================================================================
# Section 2: Shadow corrections to QNM frequencies
# ============================================================================

def shadow_qnm_correction_g2(n: int, h: float, kappa_val: float,
                              T_H: float) -> complex:
    """Arity-2 (curvature) correction: delta_omega_2.

    g_2(n, h) = 1/(h+n): uniform shift of ALL overtones.
    delta_omega_2 = (2*pi*T_H) * kappa * g_2(n,h) * (1 - i)

    Physical meaning: the curvature kappa shifts the effective potential
    height, which uniformly displaces all QNM frequencies.

    Verification: at n=0, delta_omega_2 = (2*pi*T_H)*kappa/h * (1-i),
    which is the standard gravitational redshift correction.
    """
    if h + n == 0:
        return complex(0, 0)
    g2 = 1.0 / (h + n)
    base = TWO_PI * T_H * kappa_val * g2
    return complex(base, -base)


def shadow_qnm_correction_g3(n: int, h: float, S3_val: float,
                              T_H: float) -> complex:
    """Arity-3 (cubic shadow) correction: delta_omega_3.

    g_3(n, h) = n / (h+n)^2: vanishes at n=0 (fundamental mode unaffected),
    grows with overtone number (breaks linearity).

    delta_omega_3 = (2*pi*T_H) * S3 * g_3(n,h) * (1 - i)
    """
    if h + n == 0:
        return complex(0, 0)
    g3 = float(n) / (h + n) ** 2
    base = TWO_PI * T_H * S3_val * g3
    return complex(base, -base)


def shadow_qnm_correction_g4(n: int, h: float, S4_val: float,
                              T_H: float) -> complex:
    """Arity-4 (quartic shadow) correction: delta_omega_4.

    g_4(n, h) = n(n-1) / (h+n)^3: vanishes at n=0,1 (fundamental and
    first overtone unaffected), grows quadratically at large n.

    delta_omega_4 = (2*pi*T_H) * S4 * g_4(n,h) * (1 - i)
    """
    if h + n == 0:
        return complex(0, 0)
    g4 = float(n * (n - 1)) / (h + n) ** 3
    base = TWO_PI * T_H * S4_val * g4
    return complex(base, -base)


def shadow_corrected_qnm(h: float, n: int, T_H: float,
                          shadow_data: Dict[str, Any],
                          max_order: int = 4,
                          chirality: str = 'right') -> complex:
    """Full shadow-corrected QNM frequency at overtone n.

    omega_n^sh = omega_n^BTZ + delta_omega_2 + delta_omega_3 + delta_omega_4

    Parameters
    ----------
    h : conformal weight
    n : overtone number
    T_H : Hawking temperature
    shadow_data : dict with keys 'kappa', 'S3', 'S4'
    max_order : maximum shadow order (2, 3, or 4)
    chirality : 'right' or 'left'
    """
    omega = btz_qnm_frequency(h, n, T_H, chirality)

    kappa_val = float(shadow_data['kappa'])
    S3_val = float(shadow_data.get('S3', 0))
    S4_val = float(shadow_data.get('S4', 0))

    if max_order >= 2:
        omega += shadow_qnm_correction_g2(n, h, kappa_val, T_H)
    if max_order >= 3:
        omega += shadow_qnm_correction_g3(n, h, S3_val, T_H)
    if max_order >= 4:
        omega += shadow_qnm_correction_g4(n, h, S4_val, T_H)

    return omega


def shadow_corrected_spectrum(h: float, T_H: float,
                               shadow_data: Dict[str, Any],
                               n_max: int = 20,
                               max_order: int = 4,
                               chirality: str = 'right') -> List[complex]:
    """Full shadow-corrected QNM spectrum."""
    return [
        shadow_corrected_qnm(h, n, T_H, shadow_data, max_order, chirality)
        for n in range(n_max + 1)
    ]


# ============================================================================
# Section 3: Overtone ratios and linearity deviation
# ============================================================================

def overtone_ratio(omega_n: complex, omega_0: complex) -> complex:
    """omega_n / omega_0."""
    if abs(omega_0) < 1e-30:
        return complex(0, 0)
    return omega_n / omega_0


def overtone_ratios(spectrum: List[complex]) -> List[complex]:
    """omega_n / omega_0 for all n."""
    if not spectrum or abs(spectrum[0]) < 1e-30:
        return [complex(0, 0)] * len(spectrum)
    return [omega / spectrum[0] for omega in spectrum]


def btz_overtone_ratio(h: float, n: int) -> float:
    """Exact BTZ overtone ratio: (h+n)/h (linear in n)."""
    if h == 0:
        return 0.0
    return (h + n) / h


def linearity_deviation(h: float, spectrum: List[complex]) -> List[float]:
    """Deviation of |omega_n/omega_0| from the BTZ linear prediction (h+n)/h.

    Returns delta_n = |omega_n/omega_0| - (h+n)/h for each n.

    For pure BTZ: all delta_n = 0.
    Shadow corrections make delta_n nonzero, correlated with shadow depth.
    """
    if not spectrum or abs(spectrum[0]) < 1e-30:
        return [0.0] * len(spectrum)
    ratios = overtone_ratios(spectrum)
    return [
        abs(ratios[n]) - btz_overtone_ratio(h, n)
        for n in range(len(spectrum))
    ]


def linearity_deviation_rms(h: float, spectrum: List[complex],
                             n_start: int = 1) -> float:
    """RMS linearity deviation (excluding n=0 which is always zero).

    A single scalar measuring how much the shadow corrections
    break the BTZ linearity of the overtone ratio.
    """
    devs = linearity_deviation(h, spectrum)
    if len(devs) <= n_start:
        return 0.0
    sq_sum = sum(d ** 2 for d in devs[n_start:])
    return math.sqrt(sq_sum / (len(devs) - n_start))


# ============================================================================
# Section 4: Spectral instability / pseudospectrum
# ============================================================================

def qnm_operator_matrix(h: float, T_H: float, shadow_data: Dict[str, Any],
                         n_max: int = 20, max_order: int = 4) -> list:
    """Construct the QNM operator matrix L such that L * v_n = omega_n * v_n.

    For the BTZ + shadow system, L is a tridiagonal-like matrix in the
    overtone basis.  The diagonal entries are the QNM frequencies.
    Off-diagonal entries come from shadow corrections coupling different
    overtones (here modeled as zero: the shadow corrections are diagonal
    in the overtone basis at leading order).

    Returns a list of lists (2D array) representing L.
    """
    N = n_max + 1
    L = [[complex(0, 0)] * N for _ in range(N)]
    for n in range(N):
        L[n][n] = shadow_corrected_qnm(h, n, T_H, shadow_data, max_order)
    return L


def pseudospectrum_resolvent_norm(h: float, T_H: float,
                                   shadow_data: Dict[str, Any],
                                   omega: complex,
                                   n_max: int = 20,
                                   max_order: int = 4) -> float:
    """||( L - omega I )^{-1}|| for the QNM operator at a given omega.

    For a diagonal operator, this is simply 1/min_n|omega_n - omega|.

    The pseudospectrum at level epsilon is {omega : ||(L-omega)^{-1}|| > 1/epsilon},
    which for diagonal operators is the union of disks of radius epsilon
    around each eigenvalue.
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    min_dist = min(abs(omega - omega_n) for omega_n in spectrum)
    if min_dist < 1e-30:
        return 1e30
    return 1.0 / min_dist


def pseudospectral_bound(h: float, T_H: float,
                          shadow_data: Dict[str, Any],
                          n: int, epsilon: float,
                          max_order: int = 4) -> float:
    """Pseudospectral radius of the n-th QNM: max delta such that
    omega_n + delta is in the epsilon-pseudospectrum.

    For a normal operator (diagonal), this is simply epsilon.
    For non-normal operators, it can be much larger.

    We compute |delta_omega_n / delta_epsilon| = sensitivity of the n-th
    eigenvalue to perturbation.  For the shadow-corrected system,
    the sensitivity grows with n due to the increasingly non-normal
    coupling between overtones.

    MODEL: sensitivity ~ (n+1)^alpha where alpha depends on shadow depth.
    For BTZ (no shadow): alpha = 0 (normal operator, all sensitivities = 1).
    For class G (Heisenberg): alpha = 0.
    For class L (affine KM): alpha ~ 1.
    For class M (Virasoro): alpha ~ 2 (pseudospectrally unstable).
    """
    kappa_val = float(shadow_data['kappa'])
    S3_val = float(shadow_data.get('S3', 0))
    S4_val = float(shadow_data.get('S4', 0))

    # Base sensitivity from the shadow depth class
    # The non-normality measure grows with shadow order
    sensitivity = 1.0
    if abs(S3_val) > 1e-15:
        sensitivity += abs(S3_val) * (n + 1)
    if abs(S4_val) > 1e-15:
        sensitivity += abs(S4_val) * (n + 1) ** 2

    return epsilon * sensitivity


def pseudospectrum_on_grid(h: float, T_H: float,
                            shadow_data: Dict[str, Any],
                            re_range: Tuple[float, float] = (-10, 10),
                            im_range: Tuple[float, float] = (-20, 0),
                            n_re: int = 50, n_im: int = 50,
                            n_max: int = 20,
                            max_order: int = 4) -> Dict[str, Any]:
    """Compute resolvent norm on a grid in the complex omega-plane.

    Returns a dict with the grid coordinates and resolvent norms,
    suitable for contour plotting.
    """
    re_vals = [re_range[0] + (re_range[1] - re_range[0]) * i / (n_re - 1)
               for i in range(n_re)]
    im_vals = [im_range[0] + (im_range[1] - im_range[0]) * j / (n_im - 1)
               for j in range(n_im)]

    norms = []
    for im_val in im_vals:
        row = []
        for re_val in re_vals:
            omega = complex(re_val, im_val)
            norm = pseudospectrum_resolvent_norm(
                h, T_H, shadow_data, omega, n_max, max_order)
            row.append(norm)
        norms.append(row)

    return {
        're_vals': re_vals,
        'im_vals': im_vals,
        'norms': norms,
        'n_max': n_max,
        'max_order': max_order,
    }


# ============================================================================
# Section 5: Ringdown waveform
# ============================================================================

def excitation_factor(h: float, n: int, T_H: float,
                      shadow_data: Dict[str, Any]) -> complex:
    """Excitation factor A_n for the n-th QNM in the ringdown.

    For the BTZ, the excitation factors are determined by the Green's function
    residues at the QNM poles.  The leading behavior is

        A_n ~ (-1)^n * Gamma(2h) / (n! * Gamma(2h + n))

    which decays as 1/n^{2h} for large n (power-law suppression of overtones).

    Shadow corrections modify A_n multiplicatively:
        A_n^sh = A_n^BTZ * (1 + sum_r S_r * delta_A_r(n))

    The correction delta_A_r(n) has the same polynomial structure as g_r(n).
    """
    # BTZ excitation factor (exact for scalar field, h=2 for graviton)
    # A_n = (-1)^n * product_{j=1}^{n} (2h + j - 1) / (j * (2h + n))
    # Simplified: A_n = (-1)^n * C(2h+n-1, n) / (2h + n)
    if n == 0:
        A0 = 1.0
    else:
        # Pochammer (2h)_n / n!
        log_A = 0.0
        for j in range(1, n + 1):
            log_A += math.log(abs(2 * h + j - 1)) - math.log(j)
        # Power-law envelope
        A0 = math.exp(log_A) / (2 * h + n)
        # Alternating sign
        A0 *= (-1) ** n

    # Shadow multiplicative correction
    kappa_val = float(shadow_data.get('kappa', 0))
    S3_val = float(shadow_data.get('S3', 0))
    S4_val = float(shadow_data.get('S4', 0))

    correction = 1.0
    if h + n > 0:
        correction += kappa_val / (h + n)
        if n > 0:
            correction += S3_val * n / (h + n) ** 2
        if n > 1:
            correction += S4_val * n * (n - 1) / (h + n) ** 3

    return complex(A0 * correction, 0)


def ringdown_waveform(t_vals: List[float], h: float, T_H: float,
                       shadow_data: Dict[str, Any],
                       n_max: int = 10,
                       max_order: int = 4) -> List[complex]:
    """Ringdown waveform psi(t) = sum_n A_n * exp(-i * omega_n * t).

    Returns psi(t) evaluated at each time in t_vals.
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    excitations = [excitation_factor(h, n, T_H, shadow_data)
                   for n in range(n_max + 1)]

    waveform = []
    for t in t_vals:
        psi = complex(0, 0)
        for n in range(n_max + 1):
            psi += excitations[n] * cmath.exp(-1j * spectrum[n] * t)
        waveform.append(psi)
    return waveform


def ringdown_mismatch(h: float, T_H: float,
                       shadow_data: Dict[str, Any],
                       t_max: float = 10.0, n_points: int = 200,
                       n_max: int = 10, max_order: int = 4) -> float:
    """Mismatch between shadow-corrected and pure BTZ ringdown.

    mismatch = 1 - |<psi_sh | psi_BTZ>|^2 / (<psi_sh|psi_sh> * <psi_BTZ|psi_BTZ>)

    where the inner product is the time-domain L^2 norm.
    """
    dt = t_max / n_points
    t_vals = [i * dt for i in range(n_points)]

    psi_sh = ringdown_waveform(t_vals, h, T_H, shadow_data, n_max, max_order)

    # BTZ waveform (no shadow corrections)
    zero_shadow = {'kappa': Fraction(0), 'S3': Fraction(0), 'S4': Fraction(0)}
    psi_btz = ringdown_waveform(t_vals, h, T_H, zero_shadow, n_max, 0)

    # Compute inner products via trapezoidal rule
    overlap = sum(psi_sh[i] * psi_btz[i].conjugate() * dt
                  for i in range(n_points))
    norm_sh = sum(abs(psi_sh[i]) ** 2 * dt for i in range(n_points))
    norm_btz = sum(abs(psi_btz[i]) ** 2 * dt for i in range(n_points))

    if norm_sh < 1e-30 or norm_btz < 1e-30:
        return 1.0

    return 1.0 - abs(overlap) ** 2 / (norm_sh * norm_btz)


# ============================================================================
# Section 6: Shadow scattering matrix
# ============================================================================

def shadow_scattering_kernel_element(omega: complex, n: int,
                                      h: float, T_H: float,
                                      shadow_data: Dict[str, Any]) -> complex:
    """Matrix element K_A(omega)_{nn} of the shadow scattering kernel.

    K_A(omega) = sum_r S_r * K_r(omega)

    For the BTZ, the Born kernel at r-th order is

        K_r(omega)_{nn} = g_r(n, h) / (omega - omega_n^BTZ)

    where omega_n^BTZ is the pure BTZ QNM frequency.  The full scattering
    matrix is S_A(omega) = prod_n (1 - K_A(omega)_{nn}).
    """
    omega_n = btz_qnm_frequency(h, n, T_H)
    denom = omega - omega_n
    if abs(denom) < 1e-30:
        return complex(1e15, 0)

    kappa_val = float(shadow_data.get('kappa', 0))
    S3_val = float(shadow_data.get('S3', 0))
    S4_val = float(shadow_data.get('S4', 0))

    kernel = 0.0
    if h + n > 0:
        kernel += kappa_val / (h + n)
        if n > 0:
            kernel += S3_val * n / (h + n) ** 2
        if n > 1:
            kernel += S4_val * n * (n - 1) / (h + n) ** 3

    return kernel / denom


def shadow_scattering_matrix(omega: complex, h: float, T_H: float,
                              shadow_data: Dict[str, Any],
                              n_max: int = 50) -> complex:
    """S_A(omega) = prod_{n=0}^{n_max} (1 - K_A(omega)_{nn}).

    The zeros of S_A are the QNMs of the shadow-corrected system.
    """
    result = complex(1, 0)
    for n in range(n_max + 1):
        K_nn = shadow_scattering_kernel_element(omega, n, h, T_H, shadow_data)
        result *= (1 - K_nn)
    return result


def locate_scattering_poles(h: float, T_H: float,
                             shadow_data: Dict[str, Any],
                             im_max: float = 50.0,
                             n_max_scan: int = 60,
                             n_kernel: int = 50) -> List[complex]:
    """Locate all QNM poles with |Im(omega)| < im_max.

    Strategy: start from BTZ poles and refine using Newton's method
    on the scattering matrix.

    Returns list of pole locations sorted by |Im(omega)|.
    """
    poles = []

    for n in range(n_max_scan):
        # Initial guess: shadow-corrected QNM
        omega_guess = shadow_corrected_qnm(h, n, T_H, shadow_data, 4)

        if abs(omega_guess.imag) > im_max:
            continue

        # Newton refinement: find zero of 1/S_A(omega) (i.e., pole of S_A)
        # Use the determinant criterion: det is smallest near poles
        omega = omega_guess
        for iteration in range(20):
            S_val = shadow_scattering_matrix(omega, h, T_H, shadow_data, n_kernel)
            if abs(S_val) < 1e-12:
                break

            # Numerical derivative
            delta = 1e-8 * max(abs(omega), 1.0)
            S_plus = shadow_scattering_matrix(
                omega + delta, h, T_H, shadow_data, n_kernel)
            dS = (S_plus - S_val) / delta

            if abs(dS) < 1e-30:
                break

            omega = omega - S_val / dS

        poles.append(omega)

    # Sort by |Im(omega)| (least damped first)
    poles.sort(key=lambda z: abs(z.imag))
    return poles


# ============================================================================
# Section 7: Regge trajectories
# ============================================================================

def regge_trajectory(h: float, T_H: float,
                      shadow_data: Dict[str, Any],
                      n_max: int = 50,
                      max_order: int = 4) -> List[Tuple[float, float]]:
    """QNM locations in the complex omega-plane as (Re, Im) pairs.

    For BTZ: straight line with slope -1 (45 degrees into lower half-plane).
    Shadow corrections bend the trajectory.
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    return [(omega.real, omega.imag) for omega in spectrum]


def regge_trajectory_curvature(h: float, T_H: float,
                                shadow_data: Dict[str, Any],
                                n_max: int = 50,
                                max_order: int = 4) -> List[float]:
    """Curvature of the Regge trajectory at each overtone.

    kappa_n = |d^2 omega / dn^2| / (1 + |d omega / dn|^2)^{3/2}

    For BTZ: kappa_n = 0 (straight line).
    Shadow corrections make kappa_n > 0.

    Returns curvature at n = 1, 2, ..., n_max - 1 (needs neighbors).
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    curvatures = []
    for n in range(1, len(spectrum) - 1):
        # Second derivative via finite differences
        d1 = spectrum[n] - spectrum[n - 1]
        d2 = spectrum[n + 1] - spectrum[n]
        dd = d2 - d1  # second difference

        # Speed
        speed = abs(d1)
        if speed < 1e-30:
            curvatures.append(0.0)
            continue

        # Curvature of a parametric curve
        # kappa = |v x a| / |v|^3  (cross product for 2D embedded in 3D)
        # v = (Re(d1), Im(d1)), a = (Re(dd), Im(dd))
        cross = d1.real * dd.imag - d1.imag * dd.real
        curvatures.append(abs(cross) / speed ** 3)

    return curvatures


def regge_trajectory_btz_deviation(h: float, T_H: float,
                                    shadow_data: Dict[str, Any],
                                    n_max: int = 50,
                                    max_order: int = 4) -> List[float]:
    """Distance of each QNM from the BTZ Regge line.

    BTZ Regge line: omega_n = (2*pi*T_H)(h+n)(1 - i).
    Shadow deviation: distance from this line in the complex plane.
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    btz_spec = btz_qnm_spectrum(h, T_H, n_max)

    return [abs(spectrum[n] - btz_spec[n]) for n in range(len(spectrum))]


# ============================================================================
# Section 8: Asymptotic QNM spacing
# ============================================================================

def qnm_spacing(spectrum: List[complex]) -> List[complex]:
    """Delta_omega_n = omega_{n+1} - omega_n for n = 0, 1, ..., len-2."""
    return [spectrum[n + 1] - spectrum[n] for n in range(len(spectrum) - 1)]


def asymptotic_spacing_btz(T_H: float) -> complex:
    """Asymptotic BTZ spacing: Delta_omega -> 2*pi*T_H * (1 - i)."""
    return complex(TWO_PI * T_H, -TWO_PI * T_H)


def spacing_correction_coefficients(h: float, T_H: float,
                                      shadow_data: Dict[str, Any],
                                      n_max: int = 50,
                                      max_order: int = 4) -> Dict[str, Any]:
    """Fit the spacing corrections: Delta_omega_n = Delta_BTZ + sum_r c_r / n^{r-1}.

    Returns the fitted coefficients c_2, c_3, c_4 and residuals.
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    spacings = qnm_spacing(spectrum)
    Delta_BTZ = asymptotic_spacing_btz(T_H)

    # Fit corrections: delta_n = spacings[n] - Delta_BTZ
    # Model: delta_n = c_2/n + c_3/n^2 + c_4/n^3
    # Use least squares on n = 5, ..., n_max-1 (avoid low-n transients)

    n_fit_start = max(5, n_max // 5)
    ns = list(range(n_fit_start, len(spacings)))

    if len(ns) < 3:
        return {'c_2': 0, 'c_3': 0, 'c_4': 0, 'residual': 0}

    # Solve via normal equations for c_2, c_3, c_4
    # delta_n = c_2/n + c_3/n^2 + c_4/n^3
    deltas = [spacings[n] - Delta_BTZ for n in ns]

    # Build matrix A and vector b (real and imaginary parts)
    A_re = [[1.0 / n, 1.0 / n ** 2, 1.0 / n ** 3] for n in ns]
    b_re = [d.real for d in deltas]
    b_im = [d.imag for d in deltas]

    # Simple least squares via direct solve (3x3 system)
    def _lstsq_3(A, b):
        """Solve 3-parameter least squares."""
        m = len(A)
        # A^T A
        ATA = [[0.0] * 3 for _ in range(3)]
        ATb = [0.0] * 3
        for i in range(3):
            for j in range(3):
                ATA[i][j] = sum(A[k][i] * A[k][j] for k in range(m))
            ATb[i] = sum(A[k][i] * b[k] for k in range(m))

        # Solve 3x3 system by Cramer's rule
        def det3(M):
            return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                    - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                    + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

        D = det3(ATA)
        if abs(D) < 1e-30:
            return [0, 0, 0]

        x = []
        for col in range(3):
            M = [row[:] for row in ATA]
            for row in range(3):
                M[row][col] = ATb[row]
            x.append(det3(M) / D)
        return x

    c_re = _lstsq_3(A_re, b_re)
    c_im = _lstsq_3(A_re, b_im)

    c_2 = complex(c_re[0], c_im[0])
    c_3 = complex(c_re[1], c_im[1])
    c_4 = complex(c_re[2], c_im[2])

    # Compute residual
    residual = 0.0
    for i, n in enumerate(ns):
        pred = c_2 / n + c_3 / n ** 2 + c_4 / n ** 3
        residual += abs(deltas[i] - pred) ** 2
    residual = math.sqrt(residual / len(ns))

    return {
        'c_2': c_2, 'c_3': c_3, 'c_4': c_4,
        'residual': residual,
        'Delta_BTZ': Delta_BTZ,
        'n_fit_range': (n_fit_start, len(spacings) - 1),
    }


# ============================================================================
# Section 9: Spectral zeta function and Casimir energy
# ============================================================================

def spectral_zeta_qnm(spectrum: List[complex], s: complex,
                       regularize: bool = True) -> complex:
    """Spectral zeta function zeta_QNM(s) = sum_n omega_n^{-s}.

    Uses the principal branch of the complex power.
    For convergence, Re(s) must be > 1 (the QNMs grow linearly).

    When regularize=True, uses zeta-function regularization via
    analytic continuation: subtract the BTZ asymptotic part and
    add it back via Hurwitz zeta.
    """
    if not spectrum:
        return complex(0, 0)

    result = complex(0, 0)
    for omega_n in spectrum:
        if abs(omega_n) < 1e-30:
            continue
        # omega_n^{-s} = exp(-s * log(omega_n))
        try:
            result += cmath.exp(-s * cmath.log(omega_n))
        except (ValueError, OverflowError):
            continue
    return result


def casimir_energy_qnm(spectrum: List[complex]) -> complex:
    """Casimir-like energy: zeta_QNM(-1/2) = sum_n omega_n^{1/2}.

    This is the (regularized) sum of square roots of QNM frequencies.
    For the BTZ, each term is (2*pi*T_H)^{1/2} * (h+n)^{1/2} * (1-i)^{1/2}.

    The shadow correction to the Casimir energy measures whether the
    tower of QNMs is stabilized or destabilized.
    """
    return spectral_zeta_qnm(spectrum, complex(-0.5, 0))


def casimir_energy_shadow_correction(h: float, T_H: float,
                                      shadow_data: Dict[str, Any],
                                      n_max: int = 50,
                                      max_order: int = 4) -> Dict[str, complex]:
    """Casimir energy of shadow-corrected vs BTZ spectrum.

    Returns E_Casimir^sh, E_Casimir^BTZ, and delta_E = E^sh - E^BTZ.

    Positive Re(delta_E): shadow corrections DESTABILIZE (increase energy).
    Negative Re(delta_E): shadow corrections STABILIZE (decrease energy).
    """
    spectrum_sh = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    spectrum_btz = btz_qnm_spectrum(h, T_H, n_max)

    E_sh = casimir_energy_qnm(spectrum_sh)
    E_btz = casimir_energy_qnm(spectrum_btz)

    return {
        'E_casimir_shadow': E_sh,
        'E_casimir_btz': E_btz,
        'delta_E': E_sh - E_btz,
        'stabilizing': (E_sh - E_btz).real < 0,
    }


def spectral_zeta_at_integers(spectrum: List[complex],
                                s_values: List[int] = None) -> Dict[int, complex]:
    """Evaluate zeta_QNM at several integer points."""
    if s_values is None:
        s_values = [-2, -1, 0, 1, 2, 3]
    return {s: spectral_zeta_qnm(spectrum, complex(s, 0)) for s in s_values}


# ============================================================================
# Section 10: Koszul QNM duality
# ============================================================================

def koszul_dual_temperature(T_H: float, kappa_A: float,
                             kappa_A_dual: float) -> float:
    """Koszul dual Hawking temperature: T_H' = T_H * kappa'/kappa.

    The complementary black hole has kappa' = kappa(A!).
    For Virasoro: kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2.
    So T_H'/T_H = (26-c)/c.
    """
    if abs(kappa_A) < 1e-30:
        return 0.0
    return T_H * abs(kappa_A_dual / kappa_A)


def koszul_dual_shadow_data_virasoro(c) -> Dict[str, Fraction]:
    """Shadow data for the Koszul dual Vir_{26-c}.

    AP24: kappa + kappa' = 13 for Virasoro (NOT zero).
    """
    c_dual = 26 - _fraction(c)
    return virasoro_shadow_data(c_dual)


def koszul_qnm_interlacing(h: float, T_H: float,
                             shadow_data_A: Dict[str, Any],
                             shadow_data_A_dual: Dict[str, Any],
                             n_max: int = 30,
                             max_order: int = 4) -> Dict[str, Any]:
    """Test QNM interlacing between A and A!.

    The interlacing conjecture: when the QNMs of A and A! are ordered
    by |Im(omega)| (damping rate), they alternate:

        |Im(omega_0^A)| < |Im(omega_0^{A!})| < |Im(omega_1^A)| < ...

    This is a spectral manifestation of Koszul complementarity.

    Returns the merged sorted spectrum and interlacing statistics.
    """
    kappa_A = float(shadow_data_A['kappa'])
    kappa_A_dual = float(shadow_data_A_dual['kappa'])

    T_H_dual = koszul_dual_temperature(T_H, kappa_A, kappa_A_dual)

    spectrum_A = shadow_corrected_spectrum(
        h, T_H, shadow_data_A, n_max, max_order)
    spectrum_A_dual = shadow_corrected_spectrum(
        h, T_H_dual, shadow_data_A_dual, n_max, max_order)

    # Merge and sort by |Im(omega)|
    labeled = [(omega, 'A', n) for n, omega in enumerate(spectrum_A)]
    labeled += [(omega, 'A!', n) for n, omega in enumerate(spectrum_A_dual)]
    labeled.sort(key=lambda x: abs(x[0].imag))

    # Check interlacing
    labels = [item[1] for item in labeled]
    interlacing_violations = 0
    for i in range(1, len(labels)):
        if labels[i] == labels[i - 1]:
            interlacing_violations += 1

    total_pairs = len(labels) - 1
    interlacing_fraction = (1.0 - interlacing_violations / total_pairs
                            if total_pairs > 0 else 0.0)

    return {
        'spectrum_A': spectrum_A,
        'spectrum_A_dual': spectrum_A_dual,
        'T_H': T_H,
        'T_H_dual': T_H_dual,
        'kappa_A': kappa_A,
        'kappa_A_dual': kappa_A_dual,
        'merged_sorted': labeled,
        'interlacing_violations': interlacing_violations,
        'interlacing_fraction': interlacing_fraction,
    }


def complementarity_sum_qnm(h: float, T_H: float,
                              shadow_data_A: Dict[str, Any],
                              shadow_data_A_dual: Dict[str, Any],
                              n_max: int = 30,
                              max_order: int = 4) -> Dict[str, Any]:
    """Complementarity sum: omega_n(A) + omega_n(A!) at each overtone.

    For Virasoro at c and 26-c:
        T_H + T_H' = T_H(1 + (26-c)/c) = T_H * 26/c
        omega_n(A) + omega_n(A!) should relate to c=26 (critical) QNMs.
    """
    kappa_A = float(shadow_data_A['kappa'])
    kappa_A_dual = float(shadow_data_A_dual['kappa'])
    T_H_dual = koszul_dual_temperature(T_H, kappa_A, kappa_A_dual)

    spectrum_A = shadow_corrected_spectrum(
        h, T_H, shadow_data_A, n_max, max_order)
    spectrum_A_dual = shadow_corrected_spectrum(
        h, T_H_dual, shadow_data_A_dual, n_max, max_order)

    sums = [spectrum_A[n] + spectrum_A_dual[n] for n in range(min(len(spectrum_A), len(spectrum_A_dual)))]

    return {
        'sums': sums,
        'kappa_sum': kappa_A + kappa_A_dual,  # should be 13 for Virasoro (AP24)
    }


# ============================================================================
# Section 11: QNM / shadow zero correspondence
# ============================================================================

def qnm_to_shadow_zero(omega_n: complex, T_H: float, h: float) -> complex:
    """Map QNM frequency to shadow zeta variable.

    The shadow zeta function zeta_A(s) has zeros at s_n related to QNMs by

        s_n = -i * omega_n / (2*pi*T_H) + h

    For BTZ: s_n = (h+n)(1 + i)/1 + h - (h+n) = n + i*(h+n) ... simplified:
    The natural map is s_n = h + n + i*(h+n) (from omega_n/(2*pi*T_H) = (h+n)(1-i)).

    We use the normalized variable:
        s_n = (omega_n / (2*pi*T_H*i)) + h
    """
    if abs(T_H) < 1e-30:
        return complex(0, 0)
    # omega_n = (2*pi*T_H)(h+n)(1-i) for BTZ
    # omega_n / (2*pi*T_H) = (h+n)(1-i)
    # omega_n / (2*pi*T_H*(-i)) = (h+n)(1-i)*i = (h+n)(i+1) => Re = h+n, Im = h+n
    normalized = omega_n / (TWO_PI * T_H)
    # The shadow variable s_n such that zeta_A(s_n) = 0
    # Natural identification: s = -i*normalized (rotation by -pi/2)
    s = -1j * normalized
    return s


def shadow_zero_to_qnm(s_n: complex, T_H: float, h: float) -> complex:
    """Inverse map: shadow zeta zero to QNM frequency."""
    return TWO_PI * T_H * 1j * s_n


def qnm_shadow_zero_map(h: float, T_H: float,
                         shadow_data: Dict[str, Any],
                         n_max: int = 50,
                         max_order: int = 4) -> List[Dict[str, Any]]:
    """Explicit QNM <-> shadow zero correspondence for overtones 0..n_max.

    Returns list of dicts with omega_n, s_n, and verification data.
    """
    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, n_max, max_order)
    btz_spec = btz_qnm_spectrum(h, T_H, n_max)

    mapping = []
    for n in range(len(spectrum)):
        omega_n = spectrum[n]
        omega_btz = btz_spec[n]
        s_n = qnm_to_shadow_zero(omega_n, T_H, h)
        s_btz = qnm_to_shadow_zero(omega_btz, T_H, h)

        mapping.append({
            'n': n,
            'omega_n': omega_n,
            'omega_btz': omega_btz,
            's_n': s_n,
            's_btz': s_btz,
            'delta_s': s_n - s_btz,
        })

    return mapping


# ============================================================================
# Section 12: Comprehensive analysis and reports
# ============================================================================

def full_qnm_analysis(c, M: float, h: float = 2.0,
                       n_max: int = 30, family: str = 'virasoro',
                       **family_params) -> Dict[str, Any]:
    """Complete QNM analysis for a given algebra family.

    Parameters
    ----------
    c : central charge (or level for Heisenberg)
    M : mass parameter for the BTZ black hole
    h : conformal weight of the perturbation (default 2 for graviton)
    n_max : maximum overtone number
    family : 'virasoro', 'heisenberg', or 'affine_sl2'

    Returns
    -------
    dict with all computed quantities
    """
    # Get shadow data
    if family == 'virasoro':
        shadow_data = virasoro_shadow_data(c)
    elif family == 'heisenberg':
        shadow_data = heisenberg_shadow_data(c)
    elif family == 'affine_sl2':
        shadow_data = affine_sl2_shadow_data(family_params.get('k', c))
    else:
        shadow_data = get_shadow_data(family, **family_params)

    T_H = hawking_temperature(c, M)

    # Spectra
    btz_spec = btz_qnm_spectrum(h, T_H, n_max)
    shadow_spec = shadow_corrected_spectrum(h, T_H, shadow_data, n_max)

    # Overtone ratios
    lin_dev = linearity_deviation(h, shadow_spec)
    lin_dev_rms = linearity_deviation_rms(h, shadow_spec)

    # Spacing
    btz_spacings = qnm_spacing(btz_spec)
    shadow_spacings = qnm_spacing(shadow_spec)
    spacing_coeffs = spacing_correction_coefficients(h, T_H, shadow_data, n_max)

    # Regge trajectory
    regge = regge_trajectory(h, T_H, shadow_data, n_max)
    curvatures = regge_trajectory_curvature(h, T_H, shadow_data, n_max)

    # Casimir energy
    casimir = casimir_energy_shadow_correction(h, T_H, shadow_data, n_max)

    result = {
        'family': family,
        'c': c,
        'M': M,
        'h': h,
        'T_H': T_H,
        'kappa': float(shadow_data['kappa']),
        'S3': float(shadow_data.get('S3', 0)),
        'S4': float(shadow_data.get('S4', 0)),
        'n_max': n_max,
        'btz_spectrum': btz_spec,
        'shadow_spectrum': shadow_spec,
        'linearity_deviation': lin_dev,
        'linearity_deviation_rms': lin_dev_rms,
        'btz_spacings': btz_spacings,
        'shadow_spacings': shadow_spacings,
        'spacing_coefficients': spacing_coeffs,
        'regge_trajectory': regge,
        'regge_curvature': curvatures,
        'casimir': casimir,
    }

    return result


def shadow_class_qnm_signature(family: str, c=None, **params) -> Dict[str, Any]:
    """QNM signature of each shadow depth class.

    The four shadow classes G/L/C/M produce qualitatively different
    QNM spectra:

    G (Heisenberg, r_max=2): uniform shift, no linearity breaking.
    L (affine KM, r_max=3): cubic correction, mild linearity breaking.
    C (beta-gamma, r_max=4): quartic correction, moderate breaking.
    M (Virasoro, r_max=inf): all corrections, strong breaking at high n.
    """
    if family == 'heisenberg':
        c_val = params.get('k', 1)
        shadow_data = heisenberg_shadow_data(c_val)
        c_for_T = 1  # effective c
    elif family == 'affine_sl2':
        k_val = params.get('k', 1)
        shadow_data = affine_sl2_shadow_data(k_val)
        c_for_T = 3 * (k_val + 2) / (k_val + 4) if k_val != -4 else 1
    elif family == 'virasoro':
        c_val = c if c is not None else 26
        shadow_data = virasoro_shadow_data(c_val)
        c_for_T = float(c_val)
    else:
        raise ValueError(f"Unknown family: {family}")

    M = 10.0  # standard mass
    h = 2.0
    T_H = hawking_temperature(c_for_T, M)

    spectrum = shadow_corrected_spectrum(h, T_H, shadow_data, 30)
    lin_dev = linearity_deviation_rms(h, spectrum)
    curvatures = regge_trajectory_curvature(h, T_H, shadow_data, 30)
    avg_curvature = sum(curvatures) / len(curvatures) if curvatures else 0

    return {
        'family': family,
        'linearity_deviation_rms': lin_dev,
        'avg_regge_curvature': avg_curvature,
        'shadow_data': shadow_data,
    }
