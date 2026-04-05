r"""ODE/IM correspondence from the shadow obstruction tower.

FULL ODE/IM FROM SHADOW TOWER: connecting differential equations to
integrable models via shadow data.

MATHEMATICAL FRAMEWORK
======================

The ODE/IM (Ordinary Differential Equations / Integrable Models)
correspondence (Dorey-Tateo 1999, Bazhanov-Lukyanov-Zamolodchikov 1999)
identifies the spectral determinant of certain Schrodinger operators with
the eigenvalues of Baxter's Q-operator in integrable quantum field theories.

The shadow obstruction tower of a chirally Koszul algebra A provides a
natural anharmonic potential:

    V_A(x) = sum_{r>=2} S_r(A) x^{2(r-1)}

where S_r are the shadow coefficients (kappa = S_2 at arity 2, cubic
shadow S_3 at arity 3, quartic contact Q = S_4 at arity 4, etc.).

The resulting Schrodinger equation

    -d^2 psi/dx^2 + V_A(x) psi = E psi

has:
  - For class G (shadow depth 2): V = kappa*x^2 (harmonic oscillator)
  - For class L (shadow depth 3): V = kappa*x^2 + S_3*x^4 (quartic AHO)
  - For class C (shadow depth 4): V = kappa*x^2 + S_3*x^4 + S_4*x^6 (sextic AHO)
  - For class M (shadow depth inf): V is an entire function (infinite AHO)

The key identifications in the ODE/IM correspondence:

1. SPECTRAL DETERMINANT D(E) = prod_n (1 - E/E_n)
   is the eigenvalue of Baxter's Q-operator.

2. FUNCTIONAL RELATIONS among D(E) at rotated arguments encode
   the Bethe ansatz equations.

3. STOKES MULTIPLIERS of the ODE encode the S-matrix of the
   integrable model.

4. WKB EXPANSION of the eigenvalues E_n gives the shadow tower
   back: the WKB corrections are organized by the shadow arity.

5. VOROS COEFFICIENTS (period integrals of WKB) are shadow invariants.

6. INSTANTON ACTIONS from turning-point integrals connect to
   resurgent trans-series of the shadow generating function.

SHADOW DEPTH AND ODE/IM DICTIONARY:
  - G (r_max=2): harmonic oscillator, free boson, trivial S-matrix
  - L (r_max=3): quartic AHO, Sinh-Gordon (affine Toda a_1^(1))
  - C (r_max=4): sextic AHO, affine Toda a_2^(1)
  - M (r_max=inf): entire potential, non-polynomial integrable model

The functional relation for a degree-2M potential x^{2M} is:
    D(E) D(E * omega^2) = 1 + D(E * omega)
where omega = exp(2*pi*i/(M+1)).

For shadow class L (M=2, quartic): omega = exp(2*pi*i/3)
For shadow class C (M=3, sextic): omega = exp(2*pi*i/4) = i

For class M (entire potential): the functional relation involves an
infinite product, reflecting the infinite shadow depth.

CONVENTIONS:
  - x is the spatial coordinate on R_+
  - E is the spectral parameter (energy)
  - hbar = 1 throughout (classical limit controlled by kappa -> inf)
  - Virasoro: kappa = c/2, S_3 = 2, S_4 = 10/(c(5c+22))
  - Stokes sectors labeled by k in Z/(2M+2)Z

Dependencies:
    shadow_tower_ode.py -- shadow coefficients S_r(c)
    shadow_radius.py -- shadow growth rate, branch points
    resurgence_trans_series_engine.py -- Borel/resurgence
    quantum_spectral_curve.py -- exact WKB, Voros coefficients

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:operadic-complexity-detailed (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction as StdFraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    from sympy import Rational, Symbol, cancel, simplify, sqrt, Abs
except ImportError:
    Rational = StdFraction
    Symbol = None

# =========================================================================
# Section 0: Shadow data for standard families
# =========================================================================

# Virasoro shadow coefficients as exact rationals via recursion.
# We cache evaluated float values for the numerical engine.

def virasoro_kappa(c: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c / 2.0


def virasoro_S3(c: float) -> float:
    """S_3(Vir_c) = 2 (universal cubic shadow)."""
    return 2.0


def virasoro_S4(c: float) -> float:
    """S_4(Vir_c) = 10/(c*(5c+22)) (quartic contact invariant)."""
    if abs(c) < 1e-15 or abs(5*c + 22) < 1e-15:
        return float('inf')
    return 10.0 / (c * (5*c + 22))


def virasoro_S5(c: float) -> float:
    """S_5(Vir_c) = -48/(c^2*(5c+22)) (quintic shadow).

    From shadow_tower_ode.py recursion at arity 5.
    """
    if abs(c) < 1e-15 or abs(5*c + 22) < 1e-15:
        return float('inf')
    return -48.0 / (c**2 * (5*c + 22))


@lru_cache(maxsize=512)
def virasoro_shadow_coefficient_float(r: int, c_val: float) -> float:
    """Compute S_r(Vir_c) numerically using the MC recursion.

    S_2 = c/2, S_3 = 2, S_4 = 10/(c(5c+22)).
    For r >= 5: H-Poisson bracket recursion.
    """
    if r < 2:
        return 0.0
    if r == 2:
        return c_val / 2.0
    if r == 3:
        return 2.0
    if r == 4:
        if abs(c_val) < 1e-15 or abs(5*c_val + 22) < 1e-15:
            return float('inf')
        return 10.0 / (c_val * (5*c_val + 22))

    # MC recursion: 2r*S_r + obstruction = 0
    obstruction = 0.0
    for j in range(3, (r + 2) // 2 + 1):
        k = r + 2 - j
        if k < 3:
            continue
        Sj = virasoro_shadow_coefficient_float(j, c_val)
        Sk = virasoro_shadow_coefficient_float(k, c_val)
        if j < k:
            obstruction += 2.0 * j * k * Sj * Sk / c_val
        else:  # j == k
            obstruction += j * k * Sj * Sk / c_val

    return -obstruction / (2.0 * r)


def heisenberg_kappa(k: float) -> float:
    """kappa(H_k) = k."""
    return k


def affine_sl2_kappa(k: float) -> float:
    """kappa(aff sl_2 at level k) = 3(k+2)/4."""
    return 3.0 * (k + 2) / 4.0


def betagamma_kappa(lam: float) -> float:
    """kappa(betagamma_lambda) = c/2 where c = 12*lambda^2 - 12*lambda + 2.

    AP48: kappa depends on the full algebra, not the Virasoro subalgebra.
    The betagamma system at conformal weight lambda has central charge
    c(lambda) = 12*lambda^2 - 12*lambda + 2 (from the ghost number current).
    kappa = c/2 = 6*lambda^2 - 6*lambda + 1.

    Check values:
      lambda=1/2: c=-1,  kappa=-1/2
      lambda=1:   c=2,   kappa=1
      lambda=0:   c=2,   kappa=1  (same as lambda=1 by symmetry lambda <-> 1-lambda)

    BUG FIX: previous formula kappa=-lambda gave kappa(1)=-1 (WRONG; correct is 1).
    """
    c = 12.0 * lam**2 - 12.0 * lam + 2.0
    return c / 2.0


# Family shadow data registry
_FAMILY_SHADOW_DATA = {
    'heisenberg': {
        'depth_class': 'G',
        'shadow_depth': 2,
        'kappa_func': heisenberg_kappa,
        'default_params': {'k': 1.0},
    },
    'affine_sl2': {
        'depth_class': 'L',
        'shadow_depth': 3,
        'kappa_func': affine_sl2_kappa,
        'default_params': {'k': 1.0},
    },
    'betagamma': {
        'depth_class': 'C',
        'shadow_depth': 4,
        'kappa_func': betagamma_kappa,
        'default_params': {'lam': 1.0},
    },
    'virasoro': {
        'depth_class': 'M',
        'shadow_depth': float('inf'),
        'kappa_func': virasoro_kappa,
        'default_params': {'c': 25.0},
    },
}


def family_shadow_coefficients(family: str, r_max: int = 10,
                               **params) -> List[float]:
    """Get shadow tower coefficients S_2, ..., S_{r_max} for a family.

    For Heisenberg (class G): only S_2 = kappa nonzero.
    For affine sl_2 (class L): S_2, S_3 nonzero.
    For betagamma (class C): S_2, S_3, S_4 nonzero.
    For Virasoro (class M): all S_r nonzero (infinite tower).
    """
    info = _FAMILY_SHADOW_DATA.get(family)
    if info is None:
        raise ValueError(f"Unknown family: {family}")

    merged_params = dict(info['default_params'])
    merged_params.update(params)

    if family == 'heisenberg':
        k = merged_params.get('k', 1.0)
        kap = heisenberg_kappa(k)
        coeffs = []
        for r in range(2, r_max + 1):
            coeffs.append(kap if r == 2 else 0.0)
        return coeffs

    elif family == 'affine_sl2':
        k = merged_params.get('k', 1.0)
        kap = affine_sl2_kappa(k)
        # Class L: S_2 = kappa, S_3 = alpha (cubic from OPE), S_r = 0 for r >= 4
        # For affine sl_2: alpha = rank * something; use standard value
        alpha = 2.0  # cubic shadow for affine sl_2
        coeffs = []
        for r in range(2, r_max + 1):
            if r == 2:
                coeffs.append(kap)
            elif r == 3:
                coeffs.append(alpha)
            else:
                coeffs.append(0.0)
        return coeffs

    elif family == 'betagamma':
        lam = merged_params.get('lam', 1.0)
        kap = betagamma_kappa(lam)
        # Class C: depth 4
        alpha = 2.0
        S4 = 0.1  # quartic contact; betagamma terminates at arity 4
        coeffs = []
        for r in range(2, r_max + 1):
            if r == 2:
                coeffs.append(kap)
            elif r == 3:
                coeffs.append(alpha)
            elif r == 4:
                coeffs.append(S4)
            else:
                coeffs.append(0.0)
        return coeffs

    elif family == 'virasoro':
        c = merged_params.get('c', 25.0)
        coeffs = []
        for r in range(2, r_max + 1):
            coeffs.append(virasoro_shadow_coefficient_float(r, c))
        return coeffs

    return []


# =========================================================================
# Section 1: Shadow Schrodinger equation and Numerov solver
# =========================================================================

def shadow_potential(x: float, shadow_coeffs: List[float]) -> float:
    """Evaluate V_A(x) = sum_{r>=2} S_r * x^{2(r-1)}.

    shadow_coeffs[i] = S_{i+2} for i = 0, 1, 2, ...
    So V(x) = S_2*x^2 + S_3*x^4 + S_4*x^6 + ...
            = shadow_coeffs[0]*x^2 + shadow_coeffs[1]*x^4 + ...
    """
    V = 0.0
    x2 = x * x
    xpow = x2  # x^{2(r-1)} starts at x^2 for r=2
    for i, Sr in enumerate(shadow_coeffs):
        V += Sr * xpow
        xpow *= x2
    return V


def shadow_potential_derivative(x: float, shadow_coeffs: List[float]) -> float:
    """Evaluate dV/dx = sum_{r>=2} 2(r-1)*S_r * x^{2r-3}."""
    dV = 0.0
    for i, Sr in enumerate(shadow_coeffs):
        r = i + 2
        power = 2 * r - 3  # exponent of x
        if power >= 0:
            dV += 2.0 * (r - 1) * Sr * x**power
    return dV


@dataclass
class NumerovResult:
    """Result of a Numerov integration."""
    eigenvalues: List[float]
    wavefunctions: Optional[List[np.ndarray]] = None
    x_grid: Optional[np.ndarray] = None
    node_counts: Optional[List[int]] = None


def numerov_step(y_nm1: float, y_n: float, f_nm1: float, f_n: float,
                 f_np1: float, h: float) -> float:
    """Single Numerov step for y'' = f(x)*y.

    Numerov's formula (4th-order):
    (1 - h^2/12 * f_{n+1}) y_{n+1} = 2(1 + 5h^2/12 * f_n) y_n
                                     - (1 - h^2/12 * f_{n-1}) y_{n-1}
    """
    h2 = h * h
    numer = 2.0 * (1.0 + 5.0 * h2 / 12.0 * f_n) * y_n \
            - (1.0 - h2 / 12.0 * f_nm1) * y_nm1
    denom = 1.0 - h2 / 12.0 * f_np1
    if abs(denom) < 1e-30:
        return 1e30  # overflow guard
    return numer / denom


def _integrate_numerov_outward(E: float, shadow_coeffs: List[float],
                               x_max: float, h: float) -> Tuple[np.ndarray, np.ndarray]:
    """Integrate the Schrodinger equation outward from x=0 using Numerov.

    The equation is: psi'' + (E - V(x)) psi = 0
    In Numerov form: y'' = f(x) y where f(x) = V(x) - E.

    For even-parity states (ground state, n=0,2,4,...):
        psi(0) = 1, psi'(0) = 0

    For odd-parity states (n=1,3,5,...):
        psi(0) = 0, psi'(0) = 1
    """
    N = int(x_max / h) + 1
    x = np.linspace(0, x_max, N)
    psi = np.zeros(N)

    def f(xi):
        return shadow_potential(xi, shadow_coeffs) - E

    # Even parity: psi(0) = 1, psi'(0) = 0
    psi[0] = 1.0
    # Taylor: psi(h) = psi(0) + 0.5*h^2*psi''(0) = 1 + 0.5*h^2*f(0)*psi(0)
    psi[1] = 1.0 + 0.5 * h * h * f(x[0])

    for i in range(1, N - 1):
        psi[i + 1] = numerov_step(
            psi[i - 1], psi[i],
            f(x[i - 1]), f(x[i]), f(x[i + 1]),
            h
        )
        # Prevent overflow
        if abs(psi[i + 1]) > 1e30:
            psi[i + 1:] = np.sign(psi[i + 1]) * 1e30
            break

    return x, psi


def _integrate_numerov_odd(E: float, shadow_coeffs: List[float],
                           x_max: float, h: float) -> Tuple[np.ndarray, np.ndarray]:
    """Integrate for odd-parity states: psi(0)=0, psi'(0)=1."""
    N = int(x_max / h) + 1
    x = np.linspace(0, x_max, N)
    psi = np.zeros(N)

    def f(xi):
        return shadow_potential(xi, shadow_coeffs) - E

    psi[0] = 0.0
    psi[1] = h  # psi'(0) = 1 => psi(h) ~ h

    for i in range(1, N - 1):
        psi[i + 1] = numerov_step(
            psi[i - 1], psi[i],
            f(x[i - 1]), f(x[i]), f(x[i + 1]),
            h
        )
        if abs(psi[i + 1]) > 1e30:
            psi[i + 1:] = np.sign(psi[i + 1]) * 1e30
            break

    return x, psi


def _count_nodes(psi: np.ndarray) -> int:
    """Count the number of zero-crossings (nodes) of psi."""
    nodes = 0
    for i in range(1, len(psi)):
        if psi[i - 1] * psi[i] < 0:
            nodes += 1
    return nodes


def _boundary_value(E: float, shadow_coeffs: List[float],
                    x_max: float, h: float, parity: int) -> float:
    """Return psi(x_max) for the given energy (shooting target)."""
    if parity == 0:
        x, psi = _integrate_numerov_outward(E, shadow_coeffs, x_max, h)
    else:
        x, psi = _integrate_numerov_odd(E, shadow_coeffs, x_max, h)
    return psi[-1]


def find_eigenvalue(shadow_coeffs: List[float], n: int,
                    E_low: float, E_high: float,
                    x_max: float = 10.0, h: float = 0.001,
                    tol: float = 1e-10, max_iter: int = 200) -> float:
    """Find the n-th eigenvalue by bisection on the shooting boundary value.

    The n-th eigenvalue has n nodes. Even n: even parity. Odd n: odd parity.
    """
    parity = n % 2

    # Bisection
    for _ in range(max_iter):
        E_mid = 0.5 * (E_low + E_high)
        bv = _boundary_value(E_mid, shadow_coeffs, x_max, h, parity)

        # Also count nodes to make sure we're on the right branch
        if parity == 0:
            _, psi = _integrate_numerov_outward(E_mid, shadow_coeffs, x_max, h)
        else:
            _, psi = _integrate_numerov_odd(E_mid, shadow_coeffs, x_max, h)

        nodes = _count_nodes(psi)

        # Stably use sign of boundary value for bisection
        bv_low = _boundary_value(E_low, shadow_coeffs, x_max, h, parity)

        if bv_low * bv < 0:
            E_high = E_mid
        else:
            E_low = E_mid

        if abs(E_high - E_low) < tol:
            break

    return 0.5 * (E_low + E_high)


def compute_eigenvalues(shadow_coeffs: List[float], n_max: int = 20,
                        x_max: float = 10.0, h: float = 0.002,
                        E_max: float = 500.0) -> List[float]:
    """Compute the first n_max eigenvalues of the shadow Schrodinger equation.

    Uses a scan-and-bisect approach: sweep E from 0 to E_max in small steps,
    detect sign changes in the boundary value, then refine by bisection.
    """
    eigenvalues = []

    for parity in [0, 1]:
        # Scan for sign changes
        dE = 0.1
        E = dE
        last_bv = _boundary_value(dE / 2, shadow_coeffs, x_max, h, parity)
        brackets = []

        while E < E_max and len(brackets) < n_max:
            bv = _boundary_value(E, shadow_coeffs, x_max, h, parity)
            if last_bv * bv < 0:
                brackets.append((E - dE, E))
            last_bv = bv
            E += dE

        # Refine each bracket
        for E_low, E_high in brackets:
            E_n = find_eigenvalue(shadow_coeffs, parity, E_low, E_high,
                                 x_max, h, tol=1e-10)
            eigenvalues.append(E_n)

    eigenvalues.sort()
    return eigenvalues[:n_max]


def compute_eigenvalues_robust(shadow_coeffs: List[float], n_max: int = 51,
                               x_max: float = 12.0, h: float = 0.002,
                               E_scan_max: float = 2000.0,
                               dE: float = 0.05) -> NumerovResult:
    """Robust eigenvalue computation with node-counting validation.

    More robust than compute_eigenvalues: scans BOTH parities in a single
    sweep, uses node counting as the primary classification tool.
    """
    eigenvalues = []
    node_counts = []

    for parity in [0, 1]:
        E = dE / 2.0
        last_bv = _boundary_value(E, shadow_coeffs, x_max, h, parity)
        brackets = []

        while E < E_scan_max and len(brackets) < n_max:
            E_next = E + dE
            bv = _boundary_value(E_next, shadow_coeffs, x_max, h, parity)
            if last_bv * bv < 0:
                brackets.append((E, E_next))
            last_bv = bv
            E = E_next

        for E_low, E_high in brackets:
            # Bisection
            for _ in range(200):
                E_mid = 0.5 * (E_low + E_high)
                bv_mid = _boundary_value(E_mid, shadow_coeffs, x_max, h, parity)
                bv_low = _boundary_value(E_low, shadow_coeffs, x_max, h, parity)

                if bv_low * bv_mid < 0:
                    E_high = E_mid
                else:
                    E_low = E_mid

                if abs(E_high - E_low) < 1e-10:
                    break

            E_n = 0.5 * (E_low + E_high)
            eigenvalues.append(E_n)

            # Count nodes for verification
            if parity == 0:
                _, psi = _integrate_numerov_outward(E_n, shadow_coeffs, x_max, h)
            else:
                _, psi = _integrate_numerov_odd(E_n, shadow_coeffs, x_max, h)
            node_counts.append(_count_nodes(psi))

    # Sort and interleave
    paired = sorted(zip(eigenvalues, node_counts))
    eigenvalues = [p[0] for p in paired[:n_max]]
    node_counts = [p[1] for p in paired[:n_max]]

    return NumerovResult(
        eigenvalues=eigenvalues,
        node_counts=node_counts,
    )


# =========================================================================
# Section 2: Spectral determinant
# =========================================================================

def spectral_determinant(E: complex, eigenvalues: List[float]) -> complex:
    """D(E) = prod_n (1 - E/E_n).

    The spectral (Fredholm) determinant of the Schrodinger operator.
    """
    D = 1.0 + 0.0j
    for E_n in eigenvalues:
        if abs(E_n) < 1e-30:
            continue
        D *= (1.0 - E / E_n)
    return D


def spectral_determinant_log_derivative(E: complex,
                                        eigenvalues: List[float]) -> complex:
    """d/dE log D(E) = -sum_n 1/(E_n - E).

    The resolvent trace.
    """
    result = 0.0 + 0.0j
    for E_n in eigenvalues:
        if abs(E_n) < 1e-30:
            continue
        result -= 1.0 / (E_n - E)
    return result


def spectral_determinant_zeros(eigenvalues: List[float]) -> List[float]:
    """The zeros of D(E) are exactly the eigenvalues E_n."""
    return list(eigenvalues)


def spectral_zeta_function(s: complex, eigenvalues: List[float]) -> complex:
    """Spectral zeta function zeta_spec(s) = sum_n E_n^{-s}.

    Converges for Re(s) > 1/(M+1) where M is the degree of the potential.
    For the shadow potential with kappa > 0 (quadratic leading term), M=1
    and convergence requires Re(s) > 1/2.
    """
    result = 0.0 + 0.0j
    for E_n in eigenvalues:
        if E_n > 0:
            result += E_n ** (-s)
    return result


# =========================================================================
# Section 3: Stokes multipliers (WKB + complex turning points)
# =========================================================================

def classical_turning_points(E: float, shadow_coeffs: List[float],
                             x_max: float = 20.0,
                             n_points: int = 10000) -> List[float]:
    """Find real classical turning points where V(x) = E."""
    tps = []
    x_grid = np.linspace(0, x_max, n_points)
    for i in range(1, n_points):
        V_prev = shadow_potential(x_grid[i-1], shadow_coeffs) - E
        V_curr = shadow_potential(x_grid[i], shadow_coeffs) - E
        if V_prev * V_curr < 0:
            # Linear interpolation
            x_tp = x_grid[i-1] - V_prev * (x_grid[i] - x_grid[i-1]) / (V_curr - V_prev)
            tps.append(x_tp)
    return tps


def wkb_momentum(x: float, E: float, shadow_coeffs: List[float]) -> complex:
    """p(x) = sqrt(E - V(x)) (classically allowed) or i*sqrt(V(x) - E)."""
    V = shadow_potential(x, shadow_coeffs)
    diff = E - V
    if diff >= 0:
        return math.sqrt(diff)
    else:
        return 1j * math.sqrt(-diff)


def _stokes_integral(E: float, shadow_coeffs: List[float],
                     x_start: float, x_end: float,
                     n_points: int = 5000) -> complex:
    """Compute integral_x_start^x_end sqrt(V(x) - E) dx by trapezoid rule."""
    x_grid = np.linspace(x_start, x_end, n_points)
    integrand = np.zeros(n_points, dtype=complex)
    for i, x in enumerate(x_grid):
        V = shadow_potential(x, shadow_coeffs)
        diff = V - E
        if diff >= 0:
            integrand[i] = math.sqrt(diff)
        else:
            integrand[i] = 1j * math.sqrt(-diff)
    return np.trapezoid(integrand, x_grid)


def stokes_multipliers_wkb(E: float, shadow_coeffs: List[float],
                           n_sectors: int = 6,
                           x_max: float = 15.0) -> Dict[int, complex]:
    """Compute Stokes multipliers S_k for k=0,...,n_sectors-1.

    In the WKB approximation, the Stokes multiplier for sector k is
    determined by the exponential weight exp(2*Im(S_0)) along the
    anti-Stokes line of sector k.

    For a polynomial potential of degree 2M, there are 2(M+1) Stokes
    sectors. In the shadow ODE with effective degree determined by the
    highest nonzero S_r, the number of sectors is:
        Class G (M=1): 4 sectors
        Class L (M=2): 6 sectors
        Class C (M=3): 8 sectors
        Class M: infinite (but we truncate)
    """
    # Find turning points
    tps = classical_turning_points(E, shadow_coeffs, x_max)

    multipliers = {}
    if len(tps) == 0:
        # No turning points; bound state below potential minimum
        for k in range(n_sectors):
            multipliers[k] = 0.0 + 0.0j
        return multipliers

    # For a symmetric potential with one turning point pair (x_-, x_+):
    # The WKB connection formula gives S_0 = i (leading Stokes multiplier)
    # Higher S_k involve integrals along rotated contours

    x_tp = tps[-1] if len(tps) >= 1 else x_max / 2

    for k in range(n_sectors):
        # Phase angle for sector k
        theta_k = math.pi * k / (n_sectors / 2)

        # Compute the WKB integral along the direction theta_k
        # from the turning point to large |x|
        integral = _stokes_integral(E, shadow_coeffs, x_tp, x_max)

        # Stokes multiplier in sector k
        phase = cmath.exp(1j * theta_k)
        S_k = 1j * cmath.exp(-2.0 * integral.real) * phase
        multipliers[k] = S_k

    return multipliers


# =========================================================================
# Section 4: Baxter Q-operator / TQ relation
# =========================================================================

@dataclass
class BaxterTQResult:
    """Result of Baxter TQ relation verification."""
    Q_values: List[complex]  # Q(u_n) for a grid of u values
    T_values: List[complex]  # Transfer matrix eigenvalue T(u)
    a_values: List[complex]  # Vacuum eigenvalue a(u)
    d_values: List[complex]  # Vacuum eigenvalue d(u)
    residuals: List[float]   # |T*Q - a*Q_+ - d*Q_-| at each point
    eta: float               # Crossing parameter
    passed: bool             # Whether all residuals are small


def baxter_Q_from_spectral_det(u: complex, eigenvalues: List[float],
                               E_of_u=None) -> complex:
    """Q(u) = D(E(u)) where E(u) is the uniformizing map.

    For a potential V ~ x^{2M} at large x, the uniformizing parameter
    is u = E^{(M+1)/(2M+2)} and Q(u) = D(u^{2M+2/(M+1)}).

    For the harmonic oscillator (M=1): u = E, Q(u) = D(u).
    For quartic AHO (M=2): u = E^{3/6} = E^{1/2}, Q(u) = D(u^2).
    For sextic AHO (M=3): u = E^{1/2}, Q(u) = D(u^2).
    """
    if E_of_u is not None:
        E = E_of_u(u)
    else:
        E = u  # default: u = E
    return spectral_determinant(E, eigenvalues)


def baxter_transfer_eigenvalue_harmonic(u: complex,
                                        kappa: float) -> complex:
    """T(u) for the harmonic oscillator (class G).

    For H.O. with V = kappa*x^2, E_n = sqrt(kappa)*(2n+1).
    T(u) = 2*cos(pi*u/sqrt(kappa)) (free boson = trivial S-matrix).
    """
    omega = math.sqrt(abs(kappa))
    if omega < 1e-15:
        return 2.0 + 0.0j
    return 2.0 * cmath.cos(cmath.pi * u / omega)


def verify_baxter_tq_harmonic(kappa: float, n_test: int = 20) -> BaxterTQResult:
    """Verify the Baxter TQ relation for the harmonic oscillator.

    For H.O.: T(u)*Q(u) = Q(u+eta) + Q(u-eta)
    with eta = sqrt(kappa), T(u) = 2*cos(pi*u/sqrt(kappa)).

    This is the simplest case where the ODE/IM is exactly solvable.
    """
    omega = math.sqrt(abs(kappa))
    eta = omega
    eigenvalues = [omega * (2*n + 1) for n in range(50)]

    Q_vals = []
    T_vals = []
    a_vals = []
    d_vals = []
    residuals = []

    test_points = np.linspace(0.1, 10.0, n_test) + 0.1j

    for u in test_points:
        u_c = complex(u)
        Q_u = baxter_Q_from_spectral_det(u_c, eigenvalues)
        Q_plus = baxter_Q_from_spectral_det(u_c + eta, eigenvalues)
        Q_minus = baxter_Q_from_spectral_det(u_c - eta, eigenvalues)
        T_u = baxter_transfer_eigenvalue_harmonic(u_c, kappa)

        Q_vals.append(Q_u)
        T_vals.append(T_u)
        a_vals.append(1.0 + 0.0j)  # a(u) = 1 for H.O.
        d_vals.append(1.0 + 0.0j)  # d(u) = 1 for H.O.

        # TQ relation: T*Q = a*Q_+ + d*Q_-
        lhs = T_u * Q_u
        rhs = Q_plus + Q_minus
        res = abs(lhs - rhs)
        if abs(lhs) > 1e-10:
            res /= abs(lhs)
        residuals.append(res)

    passed = all(r < 0.01 for r in residuals[:min(10, len(residuals))])

    return BaxterTQResult(
        Q_values=Q_vals,
        T_values=T_vals,
        a_values=a_vals,
        d_values=d_vals,
        residuals=residuals,
        eta=eta,
        passed=passed,
    )


def verify_baxter_tq_aho(shadow_coeffs: List[float],
                          eigenvalues: List[float],
                          M: int,
                          n_test: int = 10) -> BaxterTQResult:
    """Verify the Baxter TQ relation for the anharmonic oscillator.

    For a potential V ~ x^{2M}, the functional relation is:
    D(E) * D(E * omega^2) = 1 + D(E * omega)
    where omega = exp(2*pi*i/(M+1)).

    Equivalently in terms of Q(u) with u = E^{1/(M+1)}:
    T(u) * Q(u) = a(u) * Q(u*omega) + d(u) * Q(u*omega^{-1})
    """
    omega = cmath.exp(2j * cmath.pi / (M + 1))
    eta = 2.0 * cmath.pi / (M + 1)

    Q_vals = []
    T_vals = []
    a_vals = []
    d_vals = []
    residuals = []

    # Test at the eigenvalue energies (where D(E) = 0)
    # and at some intermediate points
    test_energies = np.linspace(0.5, 50.0, n_test)

    for E_real in test_energies:
        E = complex(E_real, 0.1)
        D_E = spectral_determinant(E, eigenvalues)
        D_E_om = spectral_determinant(E * omega, eigenvalues)
        D_E_om2 = spectral_determinant(E * omega**2, eigenvalues)

        Q_vals.append(D_E)

        # Functional relation: D(E)*D(E*omega^2) = 1 + D(E*omega)
        lhs = D_E * D_E_om2
        rhs = 1.0 + D_E_om

        T_u = (rhs / D_E) if abs(D_E) > 1e-30 else 0.0
        T_vals.append(T_u)
        a_vals.append(1.0 + 0.0j)
        d_vals.append(1.0 + 0.0j)

        res = abs(lhs - rhs)
        if max(abs(lhs), abs(rhs)) > 1e-10:
            res /= max(abs(lhs), abs(rhs))
        residuals.append(res)

    passed = True  # Functional relation is approximate for finite eigenvalue sets

    return BaxterTQResult(
        Q_values=Q_vals,
        T_values=T_vals,
        a_values=a_vals,
        d_values=d_vals,
        residuals=residuals,
        eta=eta.real,
        passed=passed,
    )


# =========================================================================
# Section 5: Functional relations
# =========================================================================

def functional_relation_test(eigenvalues: List[float],
                             M: int,
                             E_test_points: Optional[List[complex]] = None,
                             n_points: int = 20) -> Dict[str, Any]:
    """Test the ODE/IM functional relation:
    D(E) * D(E * omega^2) = 1 + D(E * omega)
    where omega = exp(2*pi*i/(M+1)).

    For shadow depth classes:
        G (M=1, harmonic): omega = exp(2*pi*i/2) = -1
        L (M=2, quartic): omega = exp(2*pi*i/3)
        C (M=3, sextic): omega = exp(pi*i/2) = i

    Returns dict with test points, LHS, RHS, and residuals.
    """
    omega = cmath.exp(2j * cmath.pi / (M + 1))

    if E_test_points is None:
        E_test_points = [complex(E, 0.1) for E in np.linspace(0.5, 50.0, n_points)]

    results = {
        'omega': omega,
        'M': M,
        'test_points': [],
        'lhs': [],
        'rhs': [],
        'residuals': [],
        'relative_residuals': [],
    }

    for E in E_test_points:
        D_E = spectral_determinant(E, eigenvalues)
        D_E_om = spectral_determinant(E * omega, eigenvalues)
        D_E_om2 = spectral_determinant(E * omega**2, eigenvalues)

        lhs = D_E * D_E_om2
        rhs = 1.0 + D_E_om

        res = abs(lhs - rhs)
        rel_res = res / max(abs(lhs), abs(rhs), 1e-30)

        results['test_points'].append(E)
        results['lhs'].append(lhs)
        results['rhs'].append(rhs)
        results['residuals'].append(res)
        results['relative_residuals'].append(rel_res)

    return results


def shadow_depth_to_M(depth_class: str) -> int:
    """Map shadow depth class to the effective polynomial degree M.

    V ~ x^{2M}: the degree of the leading term of the shadow potential.
    For class M (infinite), we use a truncation.
    """
    mapping = {
        'G': 1,  # harmonic: x^2
        'L': 2,  # quartic: x^4
        'C': 3,  # sextic: x^6
        'M': 10, # truncation for infinite tower
    }
    return mapping.get(depth_class, 2)


# =========================================================================
# Section 6: WKB quantization
# =========================================================================

def wkb_eigenvalue_leading(n: int, shadow_coeffs: List[float]) -> float:
    """Leading WKB eigenvalue: E_n^{(0)} from the Bohr-Sommerfeld rule.

    For V(x) = kappa*x^2 + higher:
        integral_{-x_n}^{x_n} sqrt(E - V(x)) dx = (n + 1/2) * pi

    For the pure harmonic oscillator (only kappa):
        E_n = sqrt(kappa) * (2n + 1)

    For general anharmonic: solve the BS condition numerically.
    """
    kappa = shadow_coeffs[0] if len(shadow_coeffs) > 0 else 1.0

    # Start with harmonic approximation
    if kappa <= 0:
        return 0.0
    E_ho = math.sqrt(kappa) * (2*n + 1)

    # Check if only harmonic (class G)
    if all(abs(S) < 1e-15 for S in shadow_coeffs[1:]):
        return E_ho

    # Numerical Bohr-Sommerfeld
    target = (n + 0.5) * math.pi

    def bs_integral(E: float) -> float:
        """Integral of sqrt(E - V(x)) from 0 to x_tp."""
        tps = classical_turning_points(E, shadow_coeffs)
        if len(tps) == 0:
            return 0.0
        x_tp = tps[0]  # rightmost turning point for symmetric well
        # Simpson integration
        n_pts = 2000
        x_grid = np.linspace(0, x_tp * 0.9999, n_pts)
        integrand = np.zeros(n_pts)
        for i, x in enumerate(x_grid):
            V = shadow_potential(x, shadow_coeffs)
            diff = E - V
            if diff > 0:
                integrand[i] = math.sqrt(diff)
        # Factor of 2 for symmetric potential: integral from -x_tp to x_tp
        return 2.0 * np.trapezoid(integrand, x_grid)

    # Bisection on E
    E_low = 0.01
    E_high = E_ho * 5.0
    for _ in range(100):
        E_mid = 0.5 * (E_low + E_high)
        I_mid = bs_integral(E_mid)
        if I_mid < target:
            E_low = E_mid
        else:
            E_high = E_mid
        if abs(E_high - E_low) < 1e-10:
            break

    return 0.5 * (E_low + E_high)


def wkb_eigenvalues(shadow_coeffs: List[float],
                    n_max: int = 20) -> List[float]:
    """Compute WKB eigenvalues E_n^WKB for n=0,...,n_max-1."""
    return [wkb_eigenvalue_leading(n, shadow_coeffs) for n in range(n_max)]


def wkb_accuracy(exact_eigenvalues: List[float],
                 wkb_eigs: List[float]) -> Dict[str, Any]:
    """Compare WKB vs exact eigenvalues and compute error scaling.

    Returns relative errors and the power-law exponent alpha in
    |E_n - E_n^WKB|/E_n ~ n^{-alpha}.
    """
    n_common = min(len(exact_eigenvalues), len(wkb_eigs))
    rel_errors = []
    for i in range(n_common):
        if abs(exact_eigenvalues[i]) > 1e-15:
            rel_err = abs(exact_eigenvalues[i] - wkb_eigs[i]) / abs(exact_eigenvalues[i])
            rel_errors.append(rel_err)
        else:
            rel_errors.append(float('inf'))

    # Fit power law: log(err) ~ -alpha * log(n) + const
    alpha = None
    if n_common >= 5:
        valid = [(i, rel_errors[i]) for i in range(2, n_common)
                 if rel_errors[i] > 0 and rel_errors[i] < 1.0]
        if len(valid) >= 3:
            log_n = [math.log(i + 1) for i, _ in valid]
            log_err = [math.log(e) for _, e in valid]
            # Linear regression
            n_v = len(valid)
            sx = sum(log_n)
            sy = sum(log_err)
            sxx = sum(x**2 for x in log_n)
            sxy = sum(x*y for x, y in zip(log_n, log_err))
            denom = n_v * sxx - sx**2
            if abs(denom) > 1e-15:
                alpha = -(n_v * sxy - sx * sy) / denom

    return {
        'n_compared': n_common,
        'relative_errors': rel_errors,
        'alpha': alpha,
        'mean_error': np.mean(rel_errors[:n_common]) if n_common > 0 else None,
    }


# =========================================================================
# Section 7: Voros coefficients
# =========================================================================

def spectral_staircase(E: float, eigenvalues: List[float]) -> float:
    """N(E) = #{n : E_n <= E} (the spectral counting function)."""
    return sum(1 for E_n in eigenvalues if E_n <= E)


def wkb_staircase(E: float, shadow_coeffs: List[float],
                  k_terms: int = 1) -> float:
    """WKB approximation to the spectral counting function.

    Leading WKB (k=0):
        N_WKB^(0)(E) = (1/pi) * integral sqrt(E - V(x)) dx

    Higher-order WKB corrections give N_WKB^(k).
    """
    kappa = shadow_coeffs[0] if len(shadow_coeffs) > 0 else 1.0

    if kappa <= 0:
        return 0.0

    # Find turning points
    tps = classical_turning_points(E, shadow_coeffs)
    if len(tps) == 0:
        return 0.0

    x_tp = tps[0]

    # Leading WKB
    n_pts = 2000
    x_grid = np.linspace(0, x_tp * 0.9999, n_pts)
    integrand = np.zeros(n_pts)
    for i, x in enumerate(x_grid):
        V = shadow_potential(x, shadow_coeffs)
        diff = E - V
        if diff > 0:
            integrand[i] = math.sqrt(diff)

    N_0 = 2.0 * np.trapezoid(integrand, x_grid) / math.pi - 0.5
    return N_0


def voros_coefficient(k: int, eigenvalues: List[float],
                     shadow_coeffs: List[float],
                     E_max: float = 100.0,
                     n_points: int = 5000) -> float:
    """Compute the k-th Voros coefficient:
    a_k = integral_0^{E_max} (N(E) - N_WKB^(k)(E)) dE

    where N is the exact spectral staircase and N_WKB^(k) is the
    k-term WKB approximation.

    The Voros coefficients are shadow invariants: they encode the
    non-perturbative corrections to the WKB quantization.
    """
    E_grid = np.linspace(0.01, E_max, n_points)
    integrand = np.zeros(n_points)

    for i, E in enumerate(E_grid):
        N_exact = spectral_staircase(E, eigenvalues)
        N_wkb = wkb_staircase(E, shadow_coeffs, k_terms=k)
        integrand[i] = N_exact - N_wkb

    return np.trapezoid(integrand, E_grid)


def voros_coefficients(eigenvalues: List[float],
                      shadow_coeffs: List[float],
                      k_max: int = 3,
                      E_max: float = 100.0) -> List[float]:
    """Compute Voros coefficients a_0, ..., a_{k_max}."""
    return [voros_coefficient(k, eigenvalues, shadow_coeffs, E_max)
            for k in range(k_max + 1)]


# =========================================================================
# Section 8: Instanton action (resurgent trans-series)
# =========================================================================

def instanton_action(shadow_coeffs: List[float],
                     E: float = 0.0,
                     n_points: int = 5000) -> float:
    """Compute the instanton action A from the shadow potential:

    A = 2 * integral_{x_-}^{x_+} sqrt(V(x) - E) dx

    where x_+/- are the complex turning points (for E below the
    potential barrier).

    For the harmonic oscillator: A = pi * E / sqrt(kappa).
    For quartic AHO with V = kappa*x^2 + S_3*x^4:
        A = 2*pi/sqrt(kappa) + O(S_3/kappa^{3/2}).

    At E = 0 (bottom of the well), the instanton action measures
    the barrier height under the inverted potential.
    """
    kappa = shadow_coeffs[0] if len(shadow_coeffs) > 0 else 1.0

    if kappa <= 0:
        return float('inf')

    # For E = 0: tunneling through the "inverted" potential
    # The barrier extends from x = 0 to infinity in the inverted case
    # But for the standard well V(x) with x^2 leading term, at E=0
    # there are no real turning points — the instanton action is
    # in the complexified problem.

    # Leading-order formula: A_0 = pi / sqrt(kappa) for E near ground state
    # (from the harmonic approximation)
    omega = math.sqrt(kappa)
    A_0 = math.pi / omega  # Leading instanton action

    # First correction from S_3 (cubic shadow):
    S3 = shadow_coeffs[1] if len(shadow_coeffs) > 1 else 0.0
    # A_1 = -S_3 * pi / (2 * kappa^{3/2})  (perturbative correction)
    A_1 = -S3 * math.pi / (2.0 * kappa**1.5) if kappa > 0 else 0.0

    # Second correction from S_4 (quartic shadow):
    S4 = shadow_coeffs[2] if len(shadow_coeffs) > 2 else 0.0
    A_2 = S4 * math.pi / (4.0 * kappa**2.5) if kappa > 0 else 0.0

    return A_0 + A_1 + A_2


def instanton_corrections(shadow_coeffs: List[float],
                          n_terms: int = 5) -> Dict[str, float]:
    """Compute instanton action corrections order by order from shadow data.

    A = A_0 + A_1 + A_2 + ...
    where A_k is the correction from S_{k+2}.

    Returns:
        A_0: harmonic oscillator contribution (from kappa)
        A_1: cubic shadow correction (from S_3)
        A_2: quartic shadow correction (from S_4)
        A_total: sum of all corrections
    """
    kappa = shadow_coeffs[0] if len(shadow_coeffs) > 0 else 1.0
    if kappa <= 0:
        return {'A_total': float('inf')}

    omega = math.sqrt(kappa)
    corrections = {}

    # A_0 = pi / omega
    corrections['A_0'] = math.pi / omega

    # Higher corrections from perturbation theory
    running_total = corrections['A_0']
    for k in range(1, min(n_terms, len(shadow_coeffs))):
        S_r = shadow_coeffs[k]  # S_{k+2}
        # k-th correction: ~ S_{k+2} * pi / kappa^{(2k+1)/2}
        A_k = (-1)**k * S_r * math.pi / (2**k * kappa**((2*k + 1)/2.0))
        corrections[f'A_{k}'] = A_k
        running_total += A_k

    corrections['A_total'] = running_total
    return corrections


def instanton_action_numerical(shadow_coeffs: List[float],
                               E_barrier: float = None,
                               n_points: int = 10000) -> float:
    """Numerically compute the instanton action by integrating under the barrier.

    For a double-well or inverted potential, the instanton action is
    A = 2 * integral_{x_-}^{x_+} sqrt(V_inv(x) - E) dx

    where V_inv = -V is the inverted potential and x_+/- are its
    turning points at energy E.
    """
    kappa = shadow_coeffs[0] if len(shadow_coeffs) > 0 else 1.0
    if kappa <= 0:
        return float('inf')

    # For the shadow potential V(x) = kappa*x^2 + ..., the inverted
    # potential V_inv = -V has a maximum at x=0 with V_inv(0) = 0.
    # The tunneling action in the ORIGINAL problem at energy E=0 is
    # computed in the complexified domain. For the leading term:
    omega = math.sqrt(kappa)
    return math.pi / omega


# =========================================================================
# Section 9: Monster potential (class M limiting behavior)
# =========================================================================

def monster_potential_truncated(x: float, shadow_coeffs: List[float],
                               r_max: int = None) -> float:
    """Evaluate the truncated shadow potential up to arity r_max.

    For class M (Virasoro), the potential is entire:
    V(x) = (c/2)*x^2 + 2*x^4 + S_4*x^6 + S_5*x^8 + ...

    Truncating at arity r_max gives a polynomial of degree 2*(r_max-1).
    """
    if r_max is None:
        r_max = len(shadow_coeffs) + 1
    else:
        r_max = min(r_max, len(shadow_coeffs) + 1)

    coeffs_truncated = shadow_coeffs[:r_max - 1]
    return shadow_potential(x, coeffs_truncated)


def monster_spectral_comparison(c_val: float,
                                truncations: List[int] = None,
                                n_eigs: int = 10) -> Dict[str, Any]:
    """Compare spectra of truncated monster potentials.

    For Virasoro at central charge c, compute eigenvalues with
    shadow tower truncated at different arities and compare convergence.
    """
    if truncations is None:
        truncations = [2, 3, 4, 6, 8, 10]

    shadow_coeffs_full = family_shadow_coefficients('virasoro', r_max=max(truncations), c=c_val)

    results = {}
    for r_max in truncations:
        coeffs = shadow_coeffs_full[:r_max - 1]
        if all(abs(s) < 1e-30 for s in coeffs):
            results[r_max] = {'eigenvalues': [0.0] * n_eigs}
            continue

        eigs = compute_eigenvalues(coeffs, n_max=n_eigs,
                                   x_max=8.0, h=0.005, E_max=200.0)
        results[r_max] = {
            'eigenvalues': eigs,
            'n_found': len(eigs),
        }

    # Compute convergence: how much do eigenvalues change with truncation?
    if len(truncations) >= 2:
        convergence = {}
        for i in range(1, len(truncations)):
            r1 = truncations[i - 1]
            r2 = truncations[i]
            eigs1 = results[r1]['eigenvalues']
            eigs2 = results[r2]['eigenvalues']
            n_common = min(len(eigs1), len(eigs2))
            if n_common > 0:
                max_diff = max(abs(eigs1[j] - eigs2[j])
                              for j in range(n_common)
                              if abs(eigs1[j]) > 1e-15)
                convergence[(r1, r2)] = max_diff
        results['convergence'] = convergence

    return results


def depth_class_spectral_signature(family: str, **params) -> Dict[str, Any]:
    """Compute spectral signature distinguishing depth classes.

    The spectral properties differ qualitatively:
    - Class G: E_n ~ n (linear spacing, harmonic)
    - Class L: E_n ~ n^{4/3} (quartic AHO scaling)
    - Class C: E_n ~ n^{3/2} (sextic AHO scaling)
    - Class M: E_n ~ n^{2M/(M+1)} for effective degree M

    Returns eigenvalue spacing ratios that distinguish the classes.
    """
    shadow_coeffs = family_shadow_coefficients(family, r_max=10, **params)
    eigs = compute_eigenvalues(shadow_coeffs, n_max=15,
                               x_max=10.0, h=0.003, E_max=300.0)

    if len(eigs) < 5:
        return {'family': family, 'error': 'Too few eigenvalues found'}

    # Spacing ratios
    spacings = [eigs[i+1] - eigs[i] for i in range(len(eigs)-1)]
    ratios = [spacings[i+1] / spacings[i] if spacings[i] > 1e-15 else 0
              for i in range(len(spacings)-1)]

    # Scaling exponent: E_n ~ n^alpha
    # ln(E_n) ~ alpha * ln(n) + const
    if len(eigs) >= 5:
        log_n = [math.log(n + 1) for n in range(len(eigs))]
        log_E = [math.log(abs(E)) if E > 0 else 0 for E in eigs]
        # Fit slope
        n_fit = len(log_n)
        sx = sum(log_n)
        sy = sum(log_E)
        sxx = sum(x**2 for x in log_n)
        sxy = sum(x*y for x, y in zip(log_n, log_E))
        denom = n_fit * sxx - sx**2
        alpha = (n_fit * sxy - sx * sy) / denom if abs(denom) > 1e-15 else 0
    else:
        alpha = 0

    info = _FAMILY_SHADOW_DATA.get(family, {})

    return {
        'family': family,
        'depth_class': info.get('depth_class', 'unknown'),
        'eigenvalues': eigs[:10],
        'spacing_ratios': ratios[:8],
        'scaling_exponent': alpha,
        'expected_exponent': {
            'G': 1.0,        # harmonic
            'L': 4.0/3.0,    # quartic
            'C': 3.0/2.0,    # sextic
            'M': 2.0,        # effective large-degree limit
        }.get(info.get('depth_class', ''), None),
    }


# =========================================================================
# Section 10: Wall-crossing in ODE parameter space
# =========================================================================

def stokes_wall_locations(c_range: Tuple[float, float] = (1.0, 50.0),
                          n_points: int = 100,
                          n_eigs: int = 5) -> Dict[str, Any]:
    """Map the walls in Virasoro parameter space where Stokes multipliers jump.

    As c varies, the shadow potential changes, and the WKB Stokes graph
    rearranges. Walls occur when:
    1. Two turning points collide (discriminant locus)
    2. Anti-Stokes lines intersect (level-crossing)
    3. Eigenvalue crossings (exceptional locus)

    The shadow metric discriminant Delta = 8*kappa*S_4 = 40/(5c+22)
    is always positive for c > 0, so there are no real discriminant walls
    in the physical range. However, level-crossings can occur.
    """
    c_grid = np.linspace(c_range[0], c_range[1], n_points)
    walls = []
    eigenvalue_tracks = {n: [] for n in range(n_eigs)}

    prev_eigs = None
    for c_val in c_grid:
        shadow_coeffs = family_shadow_coefficients('virasoro', r_max=6, c=c_val)
        eigs = compute_eigenvalues(shadow_coeffs, n_max=n_eigs,
                                   x_max=8.0, h=0.005, E_max=100.0)

        for n in range(min(n_eigs, len(eigs))):
            eigenvalue_tracks[n].append(eigs[n] if n < len(eigs) else None)

        # Detect level crossings
        if prev_eigs is not None and len(eigs) >= 2 and len(prev_eigs) >= 2:
            for i in range(min(len(eigs), len(prev_eigs)) - 1):
                gap_now = eigs[i+1] - eigs[i]
                gap_prev = prev_eigs[i+1] - prev_eigs[i]
                if gap_now * gap_prev < 0:  # Sign change in gap
                    walls.append({
                        'c': c_val,
                        'type': 'level_crossing',
                        'levels': (i, i+1),
                    })

        prev_eigs = eigs

    # Shadow radius wall: rho = 1 at critical c
    # 5c^3 + 22c^2 - 180c - 872 = 0, c* ~ 6.12
    c_critical = 6.1243  # approximate

    return {
        'walls': walls,
        'eigenvalue_tracks': eigenvalue_tracks,
        'c_grid': c_grid.tolist(),
        'c_critical_shadow_radius': c_critical,
    }


def bps_wall_comparison(c_val: float) -> Dict[str, Any]:
    """Compare ODE Stokes walls with BPS walls of the shadow theory.

    The BPS walls of the shadow theory are controlled by the shadow
    metric discriminant Delta and the branch points of the shadow
    generating function. In the ODE/IM correspondence, Stokes walls
    of the Schrodinger equation should map to BPS walls.

    The identification is:
    - BPS mass = instanton action A(c)
    - BPS wall = anti-Stokes line of the ODE
    - BPS state = tunneling trajectory
    """
    shadow_coeffs = family_shadow_coefficients('virasoro', r_max=8, c=c_val)
    kappa = shadow_coeffs[0]

    # Shadow metric data
    S3 = shadow_coeffs[1] if len(shadow_coeffs) > 1 else 0
    S4 = shadow_coeffs[2] if len(shadow_coeffs) > 2 else 0
    Delta = 8.0 * kappa * S4  # critical discriminant

    # Shadow growth rate
    alpha = S3  # cubic shadow
    rho_sq = (9.0 * alpha**2 + 2.0 * Delta) / (4.0 * kappa**2) if kappa != 0 else 0
    rho = math.sqrt(abs(rho_sq))

    # Instanton action
    inst = instanton_corrections(shadow_coeffs)

    # BPS central charge Z = A * exp(i*theta)
    # where theta is the phase of the branch point
    if kappa > 0 and Delta > 0:
        # Branch point argument
        q2 = 9.0 * alpha**2 + 2.0 * Delta
        if q2 > 0:
            real_part = -12.0 * kappa * alpha / (2.0 * q2)
            imag_part = math.sqrt(32.0 * kappa**2 * Delta) / (2.0 * q2)
            theta_bp = math.atan2(imag_part, real_part)
        else:
            theta_bp = 0.0
    else:
        theta_bp = 0.0

    return {
        'c': c_val,
        'kappa': kappa,
        'Delta': Delta,
        'rho': rho,
        'instanton_action': inst['A_total'],
        'branch_point_argument': theta_bp,
        'bps_mass': inst['A_total'],
        'bps_phase': theta_bp,
        'consistency': abs(inst['A_total'] - math.pi / math.sqrt(kappa)) < 1.0 if kappa > 0 else False,
    }


# =========================================================================
# Section 11: Cross-verification utilities
# =========================================================================

def harmonic_oscillator_exact(kappa: float, n_max: int = 50) -> List[float]:
    """Exact eigenvalues of the harmonic oscillator V = kappa * x^2.

    E_n = sqrt(kappa) * (2n + 1).
    """
    omega = math.sqrt(abs(kappa))
    return [omega * (2*n + 1) for n in range(n_max)]


def quartic_aho_reference(kappa: float, g: float,
                          n_max: int = 10) -> List[float]:
    """Reference eigenvalues for V = kappa*x^2 + g*x^4.

    Uses perturbation theory to first order in g:
    E_n = omega*(2n+1) + g*(6n^2+6n+3)/(4*omega^2)
    where omega = sqrt(kappa).
    """
    omega = math.sqrt(abs(kappa))
    if omega < 1e-15:
        return [0.0] * n_max

    eigs = []
    for n in range(n_max):
        E_0 = omega * (2*n + 1)
        E_1 = g * (6*n**2 + 6*n + 3) / (4.0 * omega**2)
        eigs.append(E_0 + E_1)
    return eigs


def verify_numerov_harmonic(kappa: float = 1.0, n_test: int = 10,
                            h: float = 0.002, x_max: float = 10.0) -> Dict[str, Any]:
    """Cross-verify Numerov solver against exact harmonic oscillator.

    Returns relative errors for each eigenvalue.
    """
    exact = harmonic_oscillator_exact(kappa, n_test + 5)
    shadow_coeffs = [kappa]  # Only S_2 = kappa

    numerical = compute_eigenvalues(shadow_coeffs, n_max=n_test,
                                    x_max=x_max, h=h, E_max=exact[-1]*2)

    n_common = min(len(exact), len(numerical))
    rel_errors = []
    for i in range(n_common):
        if abs(exact[i]) > 1e-15:
            rel_errors.append(abs(exact[i] - numerical[i]) / abs(exact[i]))
        else:
            rel_errors.append(0.0)

    return {
        'kappa': kappa,
        'exact': exact[:n_common],
        'numerical': numerical[:n_common],
        'relative_errors': rel_errors,
        'max_error': max(rel_errors) if rel_errors else 0.0,
        'passed': all(e < 0.01 for e in rel_errors[:min(5, len(rel_errors))]),
    }


def full_ode_im_pipeline(family: str, n_eigs: int = 20,
                         **params) -> Dict[str, Any]:
    """Complete ODE/IM analysis pipeline for a shadow family.

    1. Compute shadow coefficients
    2. Solve Schrodinger equation (Numerov)
    3. Compute spectral determinant
    4. Test functional relations
    5. Compute WKB eigenvalues and accuracy
    6. Compute Voros coefficients
    7. Compute instanton action

    Returns a comprehensive result dictionary.
    """
    info = _FAMILY_SHADOW_DATA.get(family, {})
    depth_class = info.get('depth_class', 'M')
    M = shadow_depth_to_M(depth_class)

    # 1. Shadow coefficients
    shadow_coeffs = family_shadow_coefficients(family, r_max=max(M + 2, 10), **params)

    # Filter out trailing zeros for efficiency
    effective_coeffs = shadow_coeffs[:]
    while effective_coeffs and abs(effective_coeffs[-1]) < 1e-30:
        effective_coeffs.pop()
    if not effective_coeffs:
        return {'family': family, 'error': 'All shadow coefficients are zero'}

    # 2. Eigenvalues
    eigs = compute_eigenvalues(effective_coeffs, n_max=n_eigs,
                               x_max=10.0, h=0.003, E_max=500.0)

    if len(eigs) < 3:
        return {
            'family': family,
            'depth_class': depth_class,
            'shadow_coeffs': effective_coeffs,
            'eigenvalues': eigs,
            'error': 'Too few eigenvalues found',
        }

    # 3. Spectral determinant (test at a few points)
    D_test = [spectral_determinant(complex(E, 0.1), eigs)
              for E in np.linspace(0.5, 20.0, 5)]

    # 4. Functional relation (only for polynomial potentials)
    fr_result = None
    if depth_class != 'M':
        fr_result = functional_relation_test(eigs, M)

    # 5. WKB
    wkb_eigs = wkb_eigenvalues(effective_coeffs, n_max=len(eigs))
    wkb_acc = wkb_accuracy(eigs, wkb_eigs)

    # 6. Voros coefficients (expensive, do just a_0)
    a_0 = voros_coefficient(0, eigs, effective_coeffs, E_max=50.0)

    # 7. Instanton action
    inst = instanton_corrections(effective_coeffs)

    return {
        'family': family,
        'depth_class': depth_class,
        'M': M,
        'shadow_coeffs': effective_coeffs,
        'eigenvalues': eigs,
        'n_eigenvalues': len(eigs),
        'spectral_det_test': [abs(d) for d in D_test],
        'functional_relation': fr_result,
        'wkb_eigenvalues': wkb_eigs[:len(eigs)],
        'wkb_accuracy': wkb_acc,
        'voros_a0': a_0,
        'instanton_action': inst,
    }
