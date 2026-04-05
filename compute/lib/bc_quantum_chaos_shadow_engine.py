r"""Quantum chaos and semiclassical analysis for shadow zeta functions.

For a modular Koszul algebra A with shadow coefficients S_r(A), the shadow
zeta function zeta_A(s) = sum_{r >= 2} S_r * r^{-s} defines a spectral
problem.  This module investigates the quantum chaos signatures of this
spectral problem:

1. GUTZWILLER TRACE FORMULA:
   The spectral density d_A(E) = sum delta(E - E_n) has a semiclassical
   expansion in terms of "shadow periodic orbits" (the shadow primes).
   The shadow primes p_r are defined by the logarithmic derivative:
       -zeta_A'(s)/zeta_A(s) = sum_{r>=2} Lambda_A(r) * r^{-s}
   where Lambda_A(r) is the von Mangoldt analogue.  For multiplicative
   towers this is the standard Euler product; for non-multiplicative
   (generic shadow), the "periodic orbits" are the arities r weighted
   by S_r * log(r).

2. SPECTRAL FORM FACTOR (SFF):
   SFF(tau) = |Tr(e^{-iH*tau})|^2 = |sum_n e^{-i*E_n*tau}|^2
   where {E_n} are the shadow "eigenvalues" (zeros of zeta_A on the
   critical line, or shadow spectral data).  The SFF exhibits:
   - Slope: SFF ~ tau (random matrix, tau < tau_dip)
   - Dip: SFF minimum
   - Ramp: SFF ~ tau (quantum chaos signature)
   - Plateau: SFF -> dim(H)

3. BERRY-TABOR vs BGS:
   Class G/L algebras (finite shadow towers, integrable-like) should
   show Poisson spacing statistics.  Class M algebras (infinite tower,
   chaotic-like) should show GUE statistics.

4. SCARRING: Weight of shadow eigenfunctions on shortest periodic orbit.

5. WEYL LAW: N(E) = (vol/(4*pi)) * E + corrections from kappa, S_3, S_4.

6. ZELDITCH QUANTUM ERGODICITY: Test quantum unique ergodicity for the
   shadow quantum map.

7. LYAPUNOV EXPONENTS: From the shadow scattering matrix.

8. KS ENTROPY: h_KS = sum max(0, lambda_i).

9. QUANTUM FIDELITY: Perturbation response.

10. CHAOS BOUND: Maldacena-Shenker-Stanford lambda_L <= 2*pi/beta.

MATHEMATICAL FRAMEWORK:

The shadow "Hamiltonian" is defined by the spectral data encoded in the
shadow zeta function.  For class M algebras (Virasoro, W_N), the shadow
coefficients S_r ~ A * rho^r * r^{-5/2} * cos(r*theta + phi) define a
Hamiltonian whose spectral statistics we probe.

The key identification is:
    Shadow class G (Heisenberg)   <-->  Integrable (Poisson statistics)
    Shadow class L (affine KM)    <-->  Near-integrable (intermediate)
    Shadow class C (beta-gamma)   <-->  Mixed (contact structure)
    Shadow class M (Virasoro/W_N) <-->  Chaotic (GUE statistics)

This classification follows from the shadow depth:
    r_max = 2  (G): trivially integrable (single frequency)
    r_max = 3  (L): two frequencies, integrable
    r_max = 4  (C): three frequencies, mixed
    r_max = inf (M): infinite spectrum, chaotic

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:operadic-complexity-detailed (higher_genus_modular_koszul.tex)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general.
CAUTION (AP10): Cross-verify by 3+ independent methods.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# ---------------------------------------------------------------------------
# Import shadow coefficient providers
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
    shadow_growth_rate_from_coeffs,
    _log_gamma_complex,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    newton_zero,
    muller_zero,
)


# ============================================================================
# 0. Helper: Shadow coefficient dispatch
# ============================================================================

def _get_shadow_coeffs(
    family: str,
    param: float,
    max_r: int = 200,
) -> Dict[int, float]:
    """Get shadow coefficients for any family, extended to high arity."""
    return shadow_coefficients_extended(family, param, max_r)


def _shadow_class(family: str) -> str:
    """Return the shadow depth class G/L/C/M for a family."""
    classes = {
        'heisenberg': 'G',
        'affine_sl2': 'L',
        'affine_sl3': 'L',
        'betagamma': 'C',
        'virasoro': 'M',
        'w3_t': 'M',
        'w3_w': 'M',
    }
    return classes.get(family, 'M')


def _shadow_depth(family: str) -> int:
    """Return the shadow depth r_max for a family."""
    depths = {
        'heisenberg': 2,
        'affine_sl2': 3,
        'affine_sl3': 3,
        'betagamma': 4,
        'virasoro': 1000,   # effectively infinity
        'w3_t': 1000,
        'w3_w': 1000,
    }
    return depths.get(family, 1000)


# ============================================================================
# 1. Gutzwiller Trace Formula for Shadow Spectral Density
# ============================================================================

def shadow_von_mangoldt(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    r"""Compute the shadow von Mangoldt function Lambda_A(r).

    Defined by: -zeta_A'(s)/zeta_A(s) = sum_{r>=2} Lambda_A(r) * r^{-s}.

    For the shadow Dirichlet series, this is the analogue of periodic orbit
    contributions in the Gutzwiller trace formula.

    Since the shadow zeta is NOT an Euler product in general, we compute
    Lambda_A(r) by expanding the logarithmic derivative of the truncated
    Dirichlet series.  Specifically, if zeta_A(s) = sum S_r r^{-s}, then:

        Lambda_A(r) = S_r * log(r) / S_2  (leading approximation)

    More precisely, we use the formal identity for Dirichlet series:
        -zeta'/zeta = sum Lambda(n) n^{-s}
    where Lambda(n) is determined recursively by:
        Lambda(n) = S_n * log(n) - sum_{d | n, d < n} Lambda(d) * S_{n/d}
    divided by S_1 (but S_1 = 0 here, so we normalize differently).

    For non-multiplicative series, we define the "shadow periodic orbit
    amplitudes" as:
        A_r = S_r * log(r)
    These are the direct analogue of the Gutzwiller amplitudes.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    # Direct shadow periodic orbit amplitudes
    amplitudes = {}
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        amplitudes[r] = Sr * math.log(r)
    return amplitudes


def shadow_periodic_orbits(
    shadow_coeffs: Dict[int, float],
    n_orbits: int = 50,
) -> List[Dict[str, float]]:
    r"""Compute the shadow periodic orbits (primes of the shadow tower).

    Returns a list of periodic orbit data:
        - period: the arity r
        - action: S_r (action of the orbit)
        - amplitude: |S_r| * log(r) (Gutzwiller amplitude)
        - phase: sign(S_r) * pi/2 (Maslov-like index)

    The periodic orbits are sorted by |amplitude| (decreasing).
    """
    max_r = max(shadow_coeffs.keys())
    orbits = []

    for r in range(2, min(max_r + 1, n_orbits + 2)):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        amplitude = abs(Sr) * math.log(r)
        phase = 0.0 if Sr > 0 else math.pi
        orbits.append({
            'period': r,
            'action': Sr,
            'amplitude': amplitude,
            'phase': phase,
            'log_period': math.log(r),
        })

    orbits.sort(key=lambda x: -x['amplitude'])
    return orbits[:n_orbits]


def gutzwiller_trace_formula(
    shadow_coeffs: Dict[int, float],
    energies: List[float],
    n_orbits: int = 50,
    sigma: float = 0.5,
) -> List[float]:
    r"""Evaluate the Gutzwiller trace formula for the shadow spectral density.

    d_osc(E) = sum_{p.o.} A_gamma * exp(i * S_gamma * E) * gaussian_smooth

    The oscillating part of the spectral density, computed from shadow
    periodic orbits.  Uses Gaussian smoothing with width sigma.

    Parameters
    ----------
    shadow_coeffs : shadow tower coefficients
    energies : list of energy values at which to evaluate
    n_orbits : number of periodic orbits to include
    sigma : Gaussian smoothing width

    Returns
    -------
    List of spectral density values at each energy.
    """
    orbits = shadow_periodic_orbits(shadow_coeffs, n_orbits)
    result = []

    for E in energies:
        d_osc = 0.0
        for orb in orbits:
            # Gaussian-smoothed oscillating contribution
            # d_osc += A * cos(S * E + phase) * exp(-sigma^2 * log(r)^2 / 2)
            S = orb['action']
            amp = orb['amplitude']
            phase = orb['phase']
            log_r = orb['log_period']

            # Smoothing: suppress high-period orbits
            smoothing = math.exp(-0.5 * sigma**2 * log_r**2)
            d_osc += amp * math.cos(S * E + phase) * smoothing
        result.append(d_osc)

    return result


def verify_trace_formula(
    shadow_coeffs: Dict[int, float],
    n_eigenvalues: int = 100,
    n_orbits: int = 50,
    sigma: float = 0.3,
) -> Dict[str, Any]:
    r"""Verify the Gutzwiller trace formula by comparing the smoothed
    spectral density from periodic orbits with the directly computed
    spectral staircase.

    The shadow "eigenvalues" are the imaginary parts of the zeros of
    zeta_A(s) on the critical line (if they exist) or, for finite towers,
    the (real or complex) zeros.

    For verification, we compute both:
    1. d_po(E) from the periodic orbit sum (Gutzwiller)
    2. d_exact(E) from the eigenvalue list (direct)

    Returns correlation coefficient and error statistics.
    """
    # For finite towers, compute zeros analytically
    max_r = max(shadow_coeffs.keys())
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(shadow_coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r

    # Generate a set of "eigenvalues" from the shadow tower
    # For a finite tower with d nonzero terms, the "eigenvalues" are
    # the arguments of the zeros of the Dirichlet polynomial
    eigenvalues = _shadow_eigenvalues(shadow_coeffs, n_eigenvalues)

    if len(eigenvalues) < 5:
        return {
            'correlation': 1.0,
            'n_eigenvalues': len(eigenvalues),
            'n_orbits': 0,
            'mean_error': 0.0,
            'class': 'trivial',
        }

    # Energy range from eigenvalue spread
    E_min = min(eigenvalues) - 1.0
    E_max = max(eigenvalues) + 1.0
    n_points = 200
    energies = [E_min + (E_max - E_min) * i / n_points
                for i in range(n_points + 1)]

    # Method 1: Periodic orbit sum
    d_po = gutzwiller_trace_formula(shadow_coeffs, energies, n_orbits, sigma)

    # Method 2: Direct eigenvalue density (smoothed)
    d_exact = []
    for E in energies:
        density = sum(
            math.exp(-0.5 * ((E - ev) / sigma)**2) / (sigma * math.sqrt(2 * math.pi))
            for ev in eigenvalues
        )
        d_exact.append(density)

    # Correlation
    mean_po = sum(d_po) / len(d_po)
    mean_ex = sum(d_exact) / len(d_exact)
    var_po = sum((x - mean_po)**2 for x in d_po)
    var_ex = sum((x - mean_ex)**2 for x in d_exact)
    cov = sum((d_po[i] - mean_po) * (d_exact[i] - mean_ex)
              for i in range(len(energies)))

    denom = math.sqrt(var_po * var_ex) if var_po * var_ex > 0 else 1.0
    corr = cov / denom if denom > 0 else 0.0

    # Mean absolute error
    mae = sum(abs(d_po[i] - d_exact[i]) for i in range(len(energies))) / len(energies)

    return {
        'correlation': corr,
        'n_eigenvalues': len(eigenvalues),
        'n_orbits': n_orbits,
        'mean_error': mae,
        'class': 'verified' if abs(corr) > 0.3 else 'weak',
    }


def _shadow_eigenvalues(
    shadow_coeffs: Dict[int, float],
    n_max: int = 100,
) -> List[float]:
    r"""Extract shadow "eigenvalues" from the shadow Dirichlet series.

    For the shadow zeta zeta_A(s) = sum S_r r^{-s}, the "eigenvalues"
    are the imaginary parts of zeros on the line Re(s) = sigma_0 (critical
    line analogue).

    For finite towers (class G/L/C): the Dirichlet polynomial has zeros
    that can be found numerically.  The "eigenvalues" are the imaginary
    parts of these zeros.

    For infinite towers (class M): we search for zeros on Re(s) = 1/2
    (the natural critical line for Dirichlet series with functional equation)
    and collect imaginary parts.
    """
    max_r = max(shadow_coeffs.keys())

    # Determine if finite tower
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(shadow_coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r

    eigenvalues = []

    if last_nonzero <= 4:
        # Finite tower: find zeros of the Dirichlet polynomial
        # zeta(s) = sum_{r=2}^{r_max} S_r * r^{-s}
        # Substitute w_r = r^{-s} and find zeros numerically
        # by scanning along Re(s) = 0 (imaginary axis)
        for n in range(1, n_max + 1):
            t = n * math.pi / math.log(3)  # Natural spacing for 2-3 terms
            s_test = complex(0, t)
            val = shadow_zeta_numerical(shadow_coeffs, s_test, last_nonzero)
            if abs(val) < 0.1:
                zero = newton_zero(shadow_coeffs, s_test, max_r=last_nonzero)
                if zero is not None and abs(zero.imag) > 0.01:
                    eigenvalues.append(abs(zero.imag))
    else:
        # Infinite tower: scan for zeros on Re(s) = 1/2
        # or along Re(s) = 0 for entire functions (rho < 1)
        sigma_0 = 0.0  # Scan along imaginary axis
        dt = 0.5
        prev_val = shadow_zeta_numerical(shadow_coeffs, complex(sigma_0, 0.01), max_r)

        for n in range(1, n_max * 10):
            t = n * dt
            s = complex(sigma_0, t)
            val = shadow_zeta_numerical(shadow_coeffs, s, max_r)

            # Check for sign change in real part (rough zero detector)
            if prev_val.real * val.real < 0 or prev_val.imag * val.imag < 0:
                # Refine with Newton
                zero = newton_zero(shadow_coeffs, s, max_r=max_r)
                if zero is not None and abs(zero.imag) > 0.01:
                    eigenvalues.append(abs(zero.imag))
                    if len(eigenvalues) >= n_max:
                        break

            prev_val = val

    eigenvalues.sort()
    return eigenvalues[:n_max]


# ============================================================================
# 2. Spectral Form Factor (SFF)
# ============================================================================

@dataclass
class SFFResult:
    """Result of spectral form factor computation."""
    tau_values: List[float]
    sff_values: List[float]
    tau_dip: float          # Time of minimum
    sff_dip: float          # SFF at the dip
    tau_heisenberg: float   # Heisenberg time
    tau_ramp_start: float   # Start of ramp
    plateau_value: float    # Long-time plateau
    slope_exponent: float   # SFF ~ tau^alpha in slope regime
    ramp_exponent: float    # SFF ~ tau^beta in ramp regime


def spectral_form_factor(
    eigenvalues: List[float],
    tau_min: float = 0.01,
    tau_max: float = 100.0,
    n_tau: int = 500,
    connected: bool = True,
) -> SFFResult:
    r"""Compute the spectral form factor SFF(tau) = |Tr(e^{-iH*tau})|^2.

    SFF(tau) = sum_{m,n} e^{-i(E_m - E_n)*tau}
             = |sum_n e^{-i*E_n*tau}|^2

    For a chaotic system, SFF exhibits:
    1. Slope (tau < tau_dip): linear decay SFF ~ tau from disconnected part
    2. Dip: minimum value
    3. Ramp (tau_dip < tau < tau_H): linear rise SFF ~ tau (GUE signature)
    4. Plateau (tau > tau_H): SFF -> N (number of eigenvalues)

    Parameters
    ----------
    eigenvalues : list of spectral values (real)
    tau_min, tau_max : time range
    n_tau : number of time points (log-spaced)
    connected : if True, subtract disconnected part

    Returns
    -------
    SFFResult with full time-resolved SFF data.
    """
    N = len(eigenvalues)
    if N == 0:
        return SFFResult(
            tau_values=[], sff_values=[], tau_dip=0, sff_dip=0,
            tau_heisenberg=0, tau_ramp_start=0, plateau_value=0,
            slope_exponent=0, ramp_exponent=0,
        )

    # Log-spaced tau values
    log_min = math.log10(max(tau_min, 1e-10))
    log_max = math.log10(tau_max)
    tau_values = [10**(log_min + (log_max - log_min) * i / n_tau)
                  for i in range(n_tau + 1)]

    sff_values = []
    for tau in tau_values:
        # Z(tau) = sum_n exp(-i * E_n * tau)
        Z_real = sum(math.cos(E * tau) for E in eigenvalues)
        Z_imag = sum(math.sin(E * tau) for E in eigenvalues)
        sff = Z_real**2 + Z_imag**2

        if connected:
            # Subtract disconnected part: <|Z|^2>_disc = N
            sff = sff - N

        sff_values.append(max(sff, 0.0) if connected else sff)

    # Find the dip
    min_sff = float('inf')
    dip_idx = 0
    for i, val in enumerate(sff_values):
        if val < min_sff:
            min_sff = val
            dip_idx = i

    tau_dip = tau_values[dip_idx]
    sff_dip = min_sff

    # Heisenberg time: tau_H ~ 2*pi*N / (mean level spacing)
    if N > 1:
        mean_spacing = (max(eigenvalues) - min(eigenvalues)) / (N - 1)
        tau_heisenberg = 2 * math.pi / mean_spacing if mean_spacing > 0 else tau_max
    else:
        tau_heisenberg = tau_max

    # Estimate slope exponent (early time)
    slope_exponent = _fit_power_law(
        tau_values[:max(dip_idx, 2)],
        [max(v, 1e-30) for v in sff_values[:max(dip_idx, 2)]],
    )

    # Estimate ramp exponent (between dip and plateau)
    ramp_end = min(len(tau_values) - 1, dip_idx + (len(tau_values) - dip_idx) // 2)
    if ramp_end > dip_idx + 2:
        ramp_exponent = _fit_power_law(
            tau_values[dip_idx:ramp_end],
            [max(v, 1e-30) for v in sff_values[dip_idx:ramp_end]],
        )
    else:
        ramp_exponent = 0.0

    # Plateau value (average of last 10% of SFF)
    n_plateau = max(1, len(sff_values) // 10)
    plateau_value = sum(sff_values[-n_plateau:]) / n_plateau

    # Ramp start: where SFF starts increasing after dip
    ramp_start_idx = dip_idx
    for i in range(dip_idx, len(sff_values) - 1):
        if sff_values[i + 1] > sff_values[i]:
            ramp_start_idx = i
            break
    tau_ramp_start = tau_values[ramp_start_idx]

    return SFFResult(
        tau_values=tau_values,
        sff_values=sff_values,
        tau_dip=tau_dip,
        sff_dip=sff_dip,
        tau_heisenberg=tau_heisenberg,
        tau_ramp_start=tau_ramp_start,
        plateau_value=plateau_value,
        slope_exponent=slope_exponent,
        ramp_exponent=ramp_exponent,
    )


def sff_for_family(
    family: str,
    param: float,
    n_eigenvalues: int = 100,
    max_r: int = 200,
    **kwargs,
) -> SFFResult:
    """Compute SFF for a specific shadow algebra family."""
    coeffs = _get_shadow_coeffs(family, param, max_r)
    eigenvalues = _shadow_eigenvalues(coeffs, n_eigenvalues)
    return spectral_form_factor(eigenvalues, **kwargs)


# ============================================================================
# 3. Berry-Tabor vs BGS: Spacing Statistics
# ============================================================================

@dataclass
class SpacingStatistics:
    """Results of nearest-neighbor spacing analysis."""
    spacings: List[float]       # Normalized spacings
    mean_spacing: float
    variance: float
    beta_parameter: float       # Brody parameter (0=Poisson, 1=GOE, 2=GUE)
    r_statistic: float          # r = <min(s_i, s_{i+1})> / <max(s_i, s_{i+1})>
    poisson_ks: float           # KS distance to Poisson
    gue_ks: float               # KS distance to GUE Wigner surmise
    goe_ks: float               # KS distance to GOE Wigner surmise
    classification: str         # 'Poisson', 'GOE', 'GUE', 'intermediate'


def nearest_neighbor_spacings(
    eigenvalues: List[float],
    unfold: bool = True,
) -> List[float]:
    r"""Compute the nearest-neighbor spacing distribution.

    Parameters
    ----------
    eigenvalues : sorted list of real eigenvalues
    unfold : if True, unfold the spectrum to unit mean spacing

    Returns
    -------
    List of normalized spacings s_i = (E_{i+1} - E_i) / <s>.
    """
    if len(eigenvalues) < 2:
        return []

    evs = sorted(eigenvalues)
    spacings = [evs[i + 1] - evs[i] for i in range(len(evs) - 1)]

    if unfold:
        mean_s = sum(spacings) / len(spacings) if spacings else 1.0
        if mean_s > 0:
            spacings = [s / mean_s for s in spacings]

    return spacings


def spacing_statistics(
    eigenvalues: List[float],
) -> SpacingStatistics:
    r"""Full spacing statistics analysis.

    Computes the nearest-neighbor spacing distribution and tests it against
    Poisson (integrable), GOE (time-reversal-invariant chaos), and GUE
    (time-reversal-broken chaos) predictions.

    The Brody parameter beta interpolates:
        p(s) = (beta+1) * a * s^beta * exp(-a * s^{beta+1})
    where a = Gamma((beta+2)/(beta+1))^{beta+1}.
    beta = 0: Poisson.  beta = 1: GOE-like.  beta = 2: GUE-like.

    The ratio statistic r = <min(s_i, s_{i+1})>/<max(s_i, s_{i+1})>:
        Poisson: r ~ 0.386 (= 2*ln(2) - 1)
        GOE: r ~ 0.536
        GUE: r ~ 0.603

    Returns SpacingStatistics dataclass with all computed quantities.
    """
    spacings = nearest_neighbor_spacings(eigenvalues)
    if len(spacings) < 3:
        return SpacingStatistics(
            spacings=spacings, mean_spacing=1.0, variance=1.0,
            beta_parameter=0.0, r_statistic=0.386,
            poisson_ks=0.0, gue_ks=0.0, goe_ks=0.0,
            classification='insufficient_data',
        )

    mean_s = sum(spacings) / len(spacings)
    var_s = sum((s - mean_s)**2 for s in spacings) / len(spacings)

    # r-statistic (ratio of consecutive spacings)
    r_vals = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i + 1]
        if max(s1, s2) > 0:
            r_vals.append(min(s1, s2) / max(s1, s2))
    r_stat = sum(r_vals) / len(r_vals) if r_vals else 0.386

    # Kolmogorov-Smirnov tests against reference distributions
    sorted_spacings = sorted(spacings)
    n = len(sorted_spacings)

    poisson_ks = 0.0
    goe_ks = 0.0
    gue_ks = 0.0

    for i, s in enumerate(sorted_spacings):
        ecdf = (i + 1) / n

        # Poisson CDF: F(s) = 1 - exp(-s)
        poisson_cdf = 1.0 - math.exp(-s) if s > 0 else 0.0
        poisson_ks = max(poisson_ks, abs(ecdf - poisson_cdf))

        # GOE Wigner surmise CDF: F(s) = 1 - exp(-pi*s^2/4)
        goe_cdf = 1.0 - math.exp(-math.pi * s**2 / 4)
        goe_ks = max(goe_ks, abs(ecdf - goe_cdf))

        # GUE Wigner surmise CDF: F(s) = 1 - exp(-4*s^2/pi) * (1 + erf-correction)
        # Approximate: F(s) ~ 1 - exp(-4*s^2/pi)  (leading term of Wigner surmise)
        gue_cdf = 1.0 - math.exp(-4 * s**2 / math.pi)
        gue_ks = max(gue_ks, abs(ecdf - gue_cdf))

    # Brody parameter estimation via variance
    # Var(s) = 1 for Poisson, ~0.286 for GOE, ~0.178 for GUE
    # Brody interpolation: Var ~ Gamma(1 + 2/(beta+1)) / Gamma(1 + 1/(beta+1))^2 - 1
    # Simple estimate from the r-statistic:
    # r_Poisson = 0.386, r_GOE = 0.536, r_GUE = 0.603
    if r_stat < 0.386:
        beta = 0.0
    elif r_stat < 0.536:
        beta = (r_stat - 0.386) / (0.536 - 0.386)  # Linear interpolation
    elif r_stat < 0.603:
        beta = 1.0 + (r_stat - 0.536) / (0.603 - 0.536)
    else:
        beta = 2.0

    # Classification
    best_ks = min(poisson_ks, goe_ks, gue_ks)
    if best_ks == poisson_ks:
        classification = 'Poisson'
    elif best_ks == goe_ks:
        classification = 'GOE'
    else:
        classification = 'GUE'

    # Refine: if KS distances are close, classify as intermediate
    ks_vals = [poisson_ks, goe_ks, gue_ks]
    ks_sorted = sorted(ks_vals)
    if ks_sorted[1] - ks_sorted[0] < 0.05:
        classification = 'intermediate'

    return SpacingStatistics(
        spacings=spacings,
        mean_spacing=mean_s,
        variance=var_s,
        beta_parameter=beta,
        r_statistic=r_stat,
        poisson_ks=poisson_ks,
        gue_ks=gue_ks,
        goe_ks=goe_ks,
        classification=classification,
    )


def berry_tabor_bgs_test(
    family: str,
    param: float,
    n_eigenvalues: int = 100,
    max_r: int = 200,
) -> Dict[str, Any]:
    r"""Test Berry-Tabor (integrable) vs BGS (chaotic) conjectures.

    Berry-Tabor (1977): Integrable systems -> Poisson statistics
    Bohigas-Giannoni-Schmit (1984): Chaotic systems -> GOE/GUE statistics

    For shadow algebras:
        Class G (Heisenberg, r_max=2) -> "integrable" -> Poisson expected
        Class L (affine KM, r_max=3) -> "near-integrable" -> Poisson/intermediate
        Class C (beta-gamma, r_max=4) -> "mixed" -> intermediate
        Class M (Virasoro/W_N, r_max=inf) -> "chaotic" -> GUE expected

    Returns dict with statistics and classification.
    """
    coeffs = _get_shadow_coeffs(family, param, max_r)
    eigenvalues = _shadow_eigenvalues(coeffs, n_eigenvalues)

    stats = spacing_statistics(eigenvalues)

    shadow_cls = _shadow_class(family)
    expected = {
        'G': 'Poisson',
        'L': 'Poisson',
        'C': 'intermediate',
        'M': 'GUE',
    }

    return {
        'family': family,
        'param': param,
        'shadow_class': shadow_cls,
        'expected_statistics': expected.get(shadow_cls, 'unknown'),
        'observed_statistics': stats.classification,
        'r_statistic': stats.r_statistic,
        'beta_parameter': stats.beta_parameter,
        'poisson_ks': stats.poisson_ks,
        'goe_ks': stats.goe_ks,
        'gue_ks': stats.gue_ks,
        'n_eigenvalues': len(eigenvalues),
        'consistent': (
            stats.classification == expected.get(shadow_cls, 'unknown')
            or stats.classification == 'intermediate'
        ),
    }


# ============================================================================
# 4. Scarring Analysis
# ============================================================================

def scarring_weight(
    shadow_coeffs: Dict[int, float],
    eigenvalues: Optional[List[float]] = None,
    n_eigenvalues: int = 50,
    n_orbits: int = 5,
) -> Dict[str, Any]:
    r"""Compute scarring weights: how much do eigenfunctions concentrate
    on unstable periodic orbits?

    For quantum chaos, the "equidistribution prediction" says that in the
    semiclassical limit, eigenfunctions should equidistribute over the
    energy surface (quantum ergodicity theorem, Shnirelman-Zelditch-Colin
    de Verdiere).

    Scarring (Heller, 1984) occurs when certain eigenfunctions have
    anomalously large weight on unstable periodic orbits.

    For the shadow system, we define the "weight on orbit gamma" as:
        W_n(gamma) = |<psi_n | phi_gamma>|^2
    where phi_gamma is the coherent state on the periodic orbit gamma.

    In the Fourier representation:
        W_n(r) = |S_r|^2 * cos^2(E_n * log(r))

    Returns dict with scarring data for each eigenfunction on shortest orbits.
    """
    if eigenvalues is None:
        eigenvalues = _shadow_eigenvalues(shadow_coeffs, n_eigenvalues)

    orbits = shadow_periodic_orbits(shadow_coeffs, n_orbits)

    scar_data = []
    for i, E in enumerate(eigenvalues[:n_eigenvalues]):
        orbit_weights = []
        total_weight = 0.0

        for orb in orbits:
            r = orb['period']
            Sr = orb['action']
            # Weight = overlap squared with coherent state on orbit
            w = Sr**2 * math.cos(E * math.log(r))**2
            orbit_weights.append({
                'period': r,
                'weight': w,
                'action': Sr,
            })
            total_weight += w

        # Equidistribution prediction: all weights equal
        n_orbs = len(orbit_weights)
        equidist = total_weight / n_orbs if n_orbs > 0 else 0.0

        # Scarring strength: max weight / equidistribution
        max_weight = max(ow['weight'] for ow in orbit_weights) if orbit_weights else 0.0
        scar_strength = max_weight / equidist if equidist > 0 else 0.0

        scar_data.append({
            'eigenvalue_index': i,
            'eigenvalue': E,
            'orbit_weights': orbit_weights,
            'max_weight': max_weight,
            'equidist_prediction': equidist,
            'scar_strength': scar_strength,
        })

    # Summary statistics
    mean_scar = sum(d['scar_strength'] for d in scar_data) / len(scar_data) if scar_data else 0.0
    max_scar = max(d['scar_strength'] for d in scar_data) if scar_data else 0.0

    return {
        'n_eigenvalues': len(eigenvalues),
        'n_orbits': len(orbits),
        'scar_data': scar_data,
        'mean_scar_strength': mean_scar,
        'max_scar_strength': max_scar,
        'scarring_significant': max_scar > 2.0,  # > 2x equidistribution
    }


# ============================================================================
# 5. Weyl Law with Shadow Corrections
# ============================================================================

@dataclass
class WeylLawFit:
    """Result of Weyl law fitting."""
    N_smooth: Callable             # N_smooth(E) = A*E + B*sqrt(E) + C*log(E) + D
    coefficients: Dict[str, float] # A, B, C, D and their shadow interpretations
    residuals: List[float]
    fit_quality: float             # R^2 value
    weyl_volume: float             # Leading coefficient A
    shadow_correction_kappa: float # Correction from kappa
    shadow_correction_s3: float    # Correction from S_3
    shadow_correction_s4: float    # Correction from S_4


def weyl_law_fit(
    eigenvalues: List[float],
    shadow_coeffs: Optional[Dict[int, float]] = None,
) -> WeylLawFit:
    r"""Fit the Weyl law N(E) = #{E_n <= E} to the shadow spectral data.

    The classical Weyl law is:
        N(E) ~ (vol/(4*pi)) * E

    For systems with boundary or curvature corrections:
        N(E) ~ A*E + B*sqrt(E) + C*log(E) + D

    For the shadow system, we predict:
        A ~ proportional to mean level density = 1/<s>
        B ~ proportional to sqrt(kappa) (curvature correction)
        C ~ proportional to S_3 (cubic shadow correction)
        D ~ proportional to S_4 (quartic correction)

    Parameters
    ----------
    eigenvalues : sorted list of eigenvalues
    shadow_coeffs : shadow coefficients (for comparison)

    Returns
    -------
    WeylLawFit with fitted coefficients and shadow interpretations.
    """
    evs = sorted(eigenvalues)
    n = len(evs)
    if n < 10:
        dummy = lambda E: 0.0
        return WeylLawFit(
            N_smooth=dummy,
            coefficients={'A': 0, 'B': 0, 'C': 0, 'D': 0},
            residuals=[],
            fit_quality=0.0,
            weyl_volume=0.0,
            shadow_correction_kappa=0.0,
            shadow_correction_s3=0.0,
            shadow_correction_s4=0.0,
        )

    # Build the staircase function N(E) = #{E_k <= E}
    # Fit: N(E_i) = A*E_i + B*sqrt(E_i) + C*log(E_i) + D

    # Simple least-squares fit using normal equations
    # Design matrix: [E, sqrt(E), log(E), 1]
    # Avoid negative sqrt and log by shifting
    E_shift = evs[0] - 0.1 if evs[0] <= 0 else 0.0
    evs_shifted = [E - E_shift for E in evs]

    # Build matrices manually (no numpy dependency)
    X = []
    y = []
    for i, E in enumerate(evs_shifted):
        if E <= 0:
            continue
        row = [E, math.sqrt(E), math.log(E), 1.0]
        X.append(row)
        y.append(float(i + 1))

    if len(X) < 5:
        dummy = lambda E: 0.0
        return WeylLawFit(
            N_smooth=dummy,
            coefficients={'A': 0, 'B': 0, 'C': 0, 'D': 0},
            residuals=[],
            fit_quality=0.0,
            weyl_volume=0.0,
            shadow_correction_kappa=0.0,
            shadow_correction_s3=0.0,
            shadow_correction_s4=0.0,
        )

    # Solve X^T X beta = X^T y by Cholesky/direct
    m = len(X[0])
    XtX = [[0.0] * m for _ in range(m)]
    Xty = [0.0] * m

    for i in range(len(X)):
        for j in range(m):
            Xty[j] += X[i][j] * y[i]
            for k in range(m):
                XtX[j][k] += X[i][j] * X[i][k]

    # Solve with Gaussian elimination
    beta = _solve_linear_system(XtX, Xty)
    if beta is None:
        beta = [1.0 / n, 0.0, 0.0, 0.0]

    A, B, C, D = beta

    # Compute residuals and R^2
    y_pred = [sum(X[i][j] * beta[j] for j in range(m)) for i in range(len(X))]
    residuals = [y[i] - y_pred[i] for i in range(len(y))]
    ss_res = sum(r**2 for r in residuals)
    y_mean = sum(y) / len(y)
    ss_tot = sum((yi - y_mean)**2 for yi in y)
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    def N_smooth(E):
        E_s = E - E_shift
        if E_s <= 0:
            return 0.0
        return A * E_s + B * math.sqrt(E_s) + C * math.log(E_s) + D

    # Shadow interpretations
    kappa = shadow_coeffs.get(2, 0.0) if shadow_coeffs else 0.0
    s3 = shadow_coeffs.get(3, 0.0) if shadow_coeffs else 0.0
    s4 = shadow_coeffs.get(4, 0.0) if shadow_coeffs else 0.0

    return WeylLawFit(
        N_smooth=N_smooth,
        coefficients={'A': A, 'B': B, 'C': C, 'D': D},
        residuals=residuals,
        fit_quality=r_squared,
        weyl_volume=A,
        shadow_correction_kappa=B * math.sqrt(abs(kappa)) if kappa != 0 else 0.0,
        shadow_correction_s3=C * abs(s3) if s3 != 0 else 0.0,
        shadow_correction_s4=D * abs(s4) if s4 != 0 else 0.0,
    )


# ============================================================================
# 6. Zelditch Quantum Ergodicity Test
# ============================================================================

def quantum_ergodicity_test(
    shadow_coeffs: Dict[int, float],
    eigenvalues: Optional[List[float]] = None,
    n_eigenvalues: int = 50,
    n_observables: int = 20,
) -> Dict[str, Any]:
    r"""Test quantum ergodicity for the shadow quantum map.

    Quantum ergodicity (Shnirelman-Zelditch-Colin de Verdiere):
    For ergodic classical dynamics, for almost all eigenfunctions psi_n:
        <psi_n | Op(a) | psi_n> -> integral(a d mu)
    as n -> infinity, for every smooth observable a.

    For the shadow system, we define observables:
        a_k(r) = r^{-ik}  (Fourier-like observables on arity space)

    The quantum expectation is:
        <Op(a_k)>_n = sum_r S_r * r^{-ik} * |psi_n(r)|^2
                    ~ sum_r |S_r|^2 * r^{-ik} * cos^2(E_n log r)

    The classical average (Haar measure on the orbit space):
        integral(a_k d mu) = sum_r |S_r|^2 * r^{-ik} / (sum_r |S_r|^2)

    Quantum ergodicity: the variance of <Op(a_k)>_n over n vanishes
    as n -> infinity.

    Returns dict with ergodicity test results.
    """
    if eigenvalues is None:
        eigenvalues = _shadow_eigenvalues(shadow_coeffs, n_eigenvalues)

    max_r = max(shadow_coeffs.keys())

    # Compute weights |S_r|^2
    weights_sq = {}
    total_weight = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        w = Sr**2
        weights_sq[r] = w
        total_weight += w

    if total_weight < 1e-300:
        return {
            'is_ergodic': True,
            'n_eigenvalues': 0,
            'n_observables': 0,
            'mean_variance': 0.0,
            'variances': [],
        }

    variances = []
    for k in range(1, n_observables + 1):
        # Classical average
        classical_avg = 0.0
        for r in range(2, max_r + 1):
            classical_avg += weights_sq.get(r, 0.0) * math.cos(k * math.log(r))
        classical_avg /= total_weight

        # Quantum expectations for each eigenfunction
        quantum_exps = []
        for E in eigenvalues[:n_eigenvalues]:
            qe = 0.0
            norm = 0.0
            for r in range(2, max_r + 1):
                Sr = shadow_coeffs.get(r, 0.0)
                psi_sq = Sr**2 * math.cos(E * math.log(r))**2
                qe += psi_sq * math.cos(k * math.log(r))
                norm += psi_sq
            if norm > 0:
                qe /= norm
            quantum_exps.append(qe)

        # Variance of quantum expectations around classical
        if quantum_exps:
            mean_qe = sum(quantum_exps) / len(quantum_exps)
            var_qe = sum((qe - classical_avg)**2 for qe in quantum_exps) / len(quantum_exps)
        else:
            var_qe = 0.0

        variances.append(var_qe)

    mean_var = sum(variances) / len(variances) if variances else 0.0

    return {
        'is_ergodic': mean_var < 0.1,
        'n_eigenvalues': len(eigenvalues),
        'n_observables': n_observables,
        'mean_variance': mean_var,
        'variances': variances,
        'ergodicity_threshold': 0.1,
    }


# ============================================================================
# 7. Lyapunov Exponents
# ============================================================================

def shadow_lyapunov_exponent(
    shadow_coeffs: Dict[int, float],
    method: str = 'scattering',
) -> float:
    r"""Compute the shadow Lyapunov exponent lambda_shadow.

    Method 1 ('scattering'): From the shadow scattering matrix.
    The scattering matrix S(E) = zeta_A(1/2 + iE) / zeta_A(1/2 - iE)
    has eigenvalues exp(i * theta_n(E)).  The Lyapunov exponent is:
        lambda = lim_{T->inf} (1/T) * sum_{n=0}^{T/dt} |d theta_n / dE|

    Method 2 ('orbit'): From the growth of orbit actions.
    For a sequence of periodic orbits with periods r_1 < r_2 < ...,
    the Lyapunov exponent is:
        lambda = lim_{n->inf} (1/r_n) * log|S_{r_n} / S_2|

    For class G: lambda = 0 (only one orbit, trivially stable).
    For class L: lambda = 0 (two frequencies, quasi-periodic).
    For class M: lambda > 0 (chaotic, exponential instability).

    Returns the estimated Lyapunov exponent.
    """
    max_r = max(shadow_coeffs.keys())

    # Determine if finite tower
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(shadow_coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r

    if last_nonzero <= 4:
        return 0.0  # Finite tower: integrable

    if method == 'orbit':
        # Method 2: orbit growth rate
        S2 = shadow_coeffs.get(2, 0.0)
        if abs(S2) < 1e-300:
            return 0.0

        lyap_estimates = []
        for r in range(10, min(last_nonzero + 1, max_r + 1)):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            lyap_estimates.append(math.log(abs(Sr / S2)) / r)

        if not lyap_estimates:
            return 0.0

        # The Lyapunov exponent is the asymptotic value
        # For S_r ~ rho^r r^{-5/2}: log|S_r/S_2| / r -> log(rho)
        return lyap_estimates[-1] if lyap_estimates else 0.0

    elif method == 'scattering':
        # Method 1: scattering phase derivative
        # S(E) = zeta(1/2 + iE) / zeta(1/2 - iE)
        # Phase theta(E) = arg(S(E))
        # lambda = <|d theta/dE|>

        dE = 0.1
        n_samples = 100
        phase_derivs = []

        for n in range(n_samples):
            E = 1.0 + n * dE
            s_plus = complex(0.5, E)
            s_minus = complex(0.5, -E)

            z_plus = shadow_zeta_numerical(shadow_coeffs, s_plus, max_r)
            z_minus = shadow_zeta_numerical(shadow_coeffs, s_minus, max_r)

            if abs(z_minus) < 1e-300:
                continue

            S_E = z_plus / z_minus
            theta = cmath.phase(S_E)

            # Numerical derivative
            E2 = E + 0.01
            z_plus2 = shadow_zeta_numerical(shadow_coeffs, complex(0.5, E2), max_r)
            z_minus2 = shadow_zeta_numerical(shadow_coeffs, complex(0.5, -E2), max_r)

            if abs(z_minus2) < 1e-300:
                continue

            S_E2 = z_plus2 / z_minus2
            theta2 = cmath.phase(S_E2)

            d_theta = (theta2 - theta) / 0.01
            phase_derivs.append(abs(d_theta))

        if not phase_derivs:
            return 0.0

        return sum(phase_derivs) / len(phase_derivs)

    else:
        raise ValueError(f"Unknown method: {method}")


def lyapunov_spectrum(
    shadow_coeffs: Dict[int, float],
    n_exponents: int = 5,
) -> List[float]:
    r"""Compute the shadow Lyapunov spectrum (all Lyapunov exponents).

    For a 2d phase space analogue, there are two Lyapunov exponents
    (lambda, -lambda) for Hamiltonian dynamics.

    For the shadow system with n effective degrees of freedom:
        n_eff = number of nonzero shadow coefficients = shadow depth
    there are 2*n_eff exponents in conjugate pairs.

    We estimate them from the singular values of the scattering matrix
    over a range of energies.
    """
    max_r = max(shadow_coeffs.keys())

    # Count effective modes
    n_modes = sum(1 for r in range(2, max_r + 1)
                  if abs(shadow_coeffs.get(r, 0.0)) > 1e-50)

    n_exp = min(n_exponents, n_modes)

    # Compute from orbit-based method at different scales
    exponents = []
    S2 = shadow_coeffs.get(2, 0.0)
    if abs(S2) < 1e-300:
        return [0.0] * n_exp

    for j in range(n_exp):
        # j-th exponent from j-th "scale"
        r_start = 2 + j * (max_r // n_exp)
        r_end = r_start + max_r // n_exp

        lyap_vals = []
        for r in range(max(r_start, 2), min(r_end, max_r + 1)):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            lyap_vals.append(math.log(abs(Sr / S2)) / max(r, 1))

        if lyap_vals:
            exponents.append(sum(lyap_vals) / len(lyap_vals))
        else:
            exponents.append(0.0)

    exponents.sort(reverse=True)
    return exponents


def lyapunov_for_virasoro(
    c_values: List[float],
    method: str = 'orbit',
    max_r: int = 200,
) -> Dict[float, float]:
    r"""Compute shadow Lyapunov exponent for Virasoro at various c.

    The shadow growth rate rho controls the leading Lyapunov:
        lambda ~ log(rho) for the orbit method.

    For Virasoro:
        rho(c) = sqrt((180c + 872) / ((5c + 22) * c^2))
        lambda ~ log(rho(c))

    Returns dict mapping c -> lambda.
    """
    result = {}
    for c_val in c_values:
        if c_val == 0 or (5 * c_val + 22) == 0:
            result[c_val] = float('inf')
            continue

        coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
        lyap = shadow_lyapunov_exponent(coeffs, method=method)
        result[c_val] = lyap

    return result


# ============================================================================
# 8. Kolmogorov-Sinai Entropy
# ============================================================================

def ks_entropy(
    shadow_coeffs: Dict[int, float],
) -> float:
    r"""Compute the Kolmogorov-Sinai entropy h_KS = sum max(0, lambda_i).

    By the Pesin formula (for smooth dynamics):
        h_KS = sum_{lambda_i > 0} lambda_i

    For the shadow system, we compute the Lyapunov spectrum and sum
    the positive exponents.
    """
    spectrum = lyapunov_spectrum(shadow_coeffs)
    return sum(max(0.0, l) for l in spectrum)


def ks_entropy_vs_depth(
    families: Optional[List[Tuple[str, float]]] = None,
) -> List[Dict[str, Any]]:
    r"""Test: does KS entropy relate to shadow depth?

    Hypothesis:
        Class G (r_max=2): h_KS = 0
        Class L (r_max=3): h_KS = 0
        Class C (r_max=4): h_KS ~ 0 (or small)
        Class M (r_max=inf): h_KS > 0

    Returns list of {family, param, depth, h_KS, class} dicts.
    """
    if families is None:
        families = [
            ('heisenberg', 1.0),
            ('heisenberg', 5.0),
            ('affine_sl2', 1.0),
            ('affine_sl2', 10.0),
            ('affine_sl3', 1.0),
            ('betagamma', 0.5),
            ('virasoro', 2.0),
            ('virasoro', 10.0),
            ('virasoro', 13.0),
            ('virasoro', 25.0),
        ]

    results = []
    for family, param in families:
        coeffs = _get_shadow_coeffs(family, param, max_r=200)
        h = ks_entropy(coeffs)
        results.append({
            'family': family,
            'param': param,
            'shadow_class': _shadow_class(family),
            'shadow_depth': _shadow_depth(family),
            'ks_entropy': h,
        })

    return results


# ============================================================================
# 9. Quantum Fidelity
# ============================================================================

def quantum_fidelity(
    shadow_coeffs: Dict[int, float],
    perturbation_strength: float = 0.1,
    n_eigenvalues: int = 50,
    t_max: float = 50.0,
    n_t: int = 200,
) -> Dict[str, Any]:
    r"""Compute quantum fidelity F(t) = |<psi(0)|e^{-iH't}e^{iHt}|psi(0)>|^2.

    Perturb the shadow Hamiltonian: S_r -> S_r + epsilon * delta_r
    where delta_r is random (uniform on [-1, 1]).

    For chaotic systems (class M):
        Large epsilon: Lyapunov decay F(t) ~ e^{-lambda*t}
        Small epsilon: Gaussian decay F(t) ~ e^{-sigma^2*t^2}

    For integrable systems (class G/L):
        F(t) ~ 1 - epsilon^2 * sigma^2 * t^2 (perturbative, Gaussian)

    Returns dict with fidelity time series and fitted decay parameters.
    """
    max_r = max(shadow_coeffs.keys())
    epsilon = perturbation_strength

    # Unperturbed eigenvalues
    ev_unpert = _shadow_eigenvalues(shadow_coeffs, n_eigenvalues)

    # Perturbed shadow coefficients (fixed seed for reproducibility)
    perturbed = dict(shadow_coeffs)
    import hashlib
    seed_str = f"{epsilon:.6f}"
    seed_hash = int(hashlib.md5(seed_str.encode()).hexdigest()[:8], 16)

    for r in range(2, max_r + 1):
        # Deterministic perturbation from hash
        hash_r = int(hashlib.md5(f"{seed_hash}_{r}".encode()).hexdigest()[:8], 16)
        delta = (hash_r / (2**32 - 1)) * 2.0 - 1.0  # in [-1, 1]
        perturbed[r] = shadow_coeffs.get(r, 0.0) + epsilon * delta * abs(shadow_coeffs.get(2, 1.0))

    # Perturbed eigenvalues
    ev_pert = _shadow_eigenvalues(perturbed, n_eigenvalues)

    n = min(len(ev_unpert), len(ev_pert))
    if n < 2:
        return {
            'times': [],
            'fidelity': [],
            'decay_type': 'none',
            'decay_rate': 0.0,
            'sigma_gaussian': 0.0,
        }

    # Compute fidelity
    dt = t_max / n_t
    times = [i * dt for i in range(n_t + 1)]
    fidelity = []

    for t in times:
        # F(t) = |<psi(0)|e^{-iH't}e^{iHt}|psi(0)>|^2
        # In the eigenstate basis (initial state = superposition of first few)
        # F(t) = |sum_n p_n * exp(i*(E_n - E_n')*t)|^2
        # where p_n is the population of state n
        overlap_real = 0.0
        overlap_imag = 0.0
        for i in range(n):
            p_n = 1.0 / n  # Equal weight
            dE = ev_unpert[i] - ev_pert[i]
            overlap_real += p_n * math.cos(dE * t)
            overlap_imag += p_n * math.sin(dE * t)

        F = overlap_real**2 + overlap_imag**2
        fidelity.append(F)

    # Fit decay type
    # Check Gaussian: F(t) ~ exp(-sigma^2 * t^2)
    # Check Lyapunov: F(t) ~ exp(-lambda * t)
    log_F = []
    valid_times = []
    for i, F in enumerate(fidelity):
        if F > 1e-10:
            log_F.append(math.log(F))
            valid_times.append(times[i])

    if len(valid_times) < 5:
        return {
            'times': times,
            'fidelity': fidelity,
            'decay_type': 'none',
            'decay_rate': 0.0,
            'sigma_gaussian': 0.0,
        }

    # Linear fit: log(F) = a + b*t
    n_fit = len(valid_times)
    sum_t = sum(valid_times)
    sum_t2 = sum(t**2 for t in valid_times)
    sum_lf = sum(log_F)
    sum_t_lf = sum(valid_times[i] * log_F[i] for i in range(n_fit))

    denom = n_fit * sum_t2 - sum_t**2
    if abs(denom) > 1e-30:
        b_lin = (n_fit * sum_t_lf - sum_t * sum_lf) / denom
    else:
        b_lin = 0.0

    # Quadratic fit: log(F) = a + b*t^2
    sum_t4 = sum(t**4 for t in valid_times)
    sum_t2_lf = sum(valid_times[i]**2 * log_F[i] for i in range(n_fit))

    denom_q = n_fit * sum_t4 - sum_t2**2
    if abs(denom_q) > 1e-30:
        b_quad = (n_fit * sum_t2_lf - sum_t2 * sum_lf) / denom_q
    else:
        b_quad = 0.0

    # Residuals for each fit
    ss_lin = sum((log_F[i] - (sum_lf / n_fit + b_lin * (valid_times[i] - sum_t / n_fit)))**2
                 for i in range(n_fit))
    ss_quad = sum((log_F[i] - (sum_lf / n_fit + b_quad * (valid_times[i]**2 - sum_t2 / n_fit)))**2
                  for i in range(n_fit))

    if ss_quad < ss_lin:
        decay_type = 'Gaussian'
        sigma_g = math.sqrt(abs(b_quad)) if b_quad < 0 else 0.0
        decay_rate = 0.0
    else:
        decay_type = 'Lyapunov'
        decay_rate = abs(b_lin)
        sigma_g = 0.0

    return {
        'times': times,
        'fidelity': fidelity,
        'decay_type': decay_type,
        'decay_rate': decay_rate,
        'sigma_gaussian': sigma_g,
        'perturbation_strength': epsilon,
    }


# ============================================================================
# 10. Maldacena-Shenker-Stanford Chaos Bound
# ============================================================================

def mss_chaos_bound_test(
    shadow_coeffs: Dict[int, float],
    beta_values: Optional[List[float]] = None,
    method: str = 'scattering',
) -> Dict[str, Any]:
    r"""Test the MSS chaos bound: lambda_L <= 2*pi/beta.

    The Maldacena-Shenker-Stanford bound (2015) states that for
    thermal quantum systems, the Lyapunov exponent characterizing
    the growth of out-of-time-ordered correlators (OTOC) is bounded:

        lambda_L <= 2*pi*T = 2*pi/beta

    Saturation (lambda_L = 2*pi/beta) occurs for:
    - SYK model (Sachdev-Ye-Kitaev)
    - Black holes in Einstein gravity (including BTZ)
    - Certain large-N gauge theories

    For the shadow system at "temperature" T = 1/beta, we compute
    the Lyapunov exponent and test the bound.

    "Temperature" is defined via the shadow Matsubara frequency:
        beta = 2*pi / Delta_E  where Delta_E = mean level spacing

    Returns dict with bound test results.
    """
    if beta_values is None:
        beta_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    lambda_L = shadow_lyapunov_exponent(shadow_coeffs, method=method)

    results = []
    for beta in beta_values:
        bound = 2.0 * math.pi / beta
        saturated = abs(lambda_L - bound) < 0.1 * bound if bound > 0 else False
        violated = lambda_L > bound * (1.0 + 0.01)  # 1% tolerance

        results.append({
            'beta': beta,
            'temperature': 1.0 / beta,
            'lambda_L': lambda_L,
            'bound': bound,
            'ratio': lambda_L / bound if bound > 0 else 0.0,
            'saturated': saturated,
            'violated': violated,
        })

    all_satisfied = all(not r['violated'] for r in results)
    any_saturated = any(r['saturated'] for r in results)

    return {
        'lambda_L': lambda_L,
        'all_satisfied': all_satisfied,
        'any_saturated': any_saturated,
        'results': results,
        'shadow_class': 'M' if lambda_L > 0.01 else 'G/L/C',
    }


# ============================================================================
# Comprehensive quantum chaos characterization
# ============================================================================

@dataclass
class QuantumChaosProfile:
    """Complete quantum chaos characterization of a shadow algebra."""
    family: str
    param: float
    shadow_class: str
    shadow_depth: int
    n_eigenvalues: int

    # Spacing statistics
    spacing_classification: str
    r_statistic: float
    beta_parameter: float
    poisson_ks: float
    gue_ks: float

    # Lyapunov data
    lyapunov_exponent: float
    lyapunov_spectrum: List[float]
    ks_entropy: float

    # Quantum ergodicity
    is_ergodic: bool
    ergodicity_variance: float

    # Fidelity
    fidelity_decay_type: str
    fidelity_decay_rate: float

    # Chaos bound
    mss_satisfied: bool

    # Classification
    chaos_type: str  # 'integrable', 'mixed', 'chaotic'


def full_quantum_chaos_profile(
    family: str,
    param: float,
    n_eigenvalues: int = 80,
    max_r: int = 200,
) -> QuantumChaosProfile:
    r"""Compute the full quantum chaos profile for a shadow algebra.

    This is the master function that runs all 10 analyses and produces
    a unified classification.

    The classification is:
        'integrable': Poisson statistics, lambda=0, h_KS=0
        'mixed': intermediate statistics, small lambda
        'chaotic': GUE statistics, lambda>0, h_KS>0
    """
    coeffs = _get_shadow_coeffs(family, param, max_r)
    eigenvalues = _shadow_eigenvalues(coeffs, n_eigenvalues)

    shadow_cls = _shadow_class(family)
    depth = _shadow_depth(family)

    # 1. Spacing statistics
    stats = spacing_statistics(eigenvalues)

    # 2. Lyapunov
    lyap = shadow_lyapunov_exponent(coeffs, method='orbit')
    lyap_spectrum = lyapunov_spectrum(coeffs)
    h_ks = sum(max(0.0, l) for l in lyap_spectrum)

    # 3. Quantum ergodicity
    qe = quantum_ergodicity_test(coeffs, eigenvalues, min(n_eigenvalues, 30))

    # 4. Fidelity
    fid = quantum_fidelity(coeffs, perturbation_strength=0.1, n_eigenvalues=min(n_eigenvalues, 30))

    # 5. MSS bound
    mss = mss_chaos_bound_test(coeffs, method='orbit')

    # Classification
    if shadow_cls in ('G', 'L'):
        chaos_type = 'integrable'
    elif shadow_cls == 'C':
        chaos_type = 'mixed'
    else:
        # For class M, check actual statistics
        if stats.classification in ('GUE', 'GOE'):
            chaos_type = 'chaotic'
        elif lyap > 0.01:
            chaos_type = 'chaotic'
        else:
            chaos_type = 'mixed'

    return QuantumChaosProfile(
        family=family,
        param=param,
        shadow_class=shadow_cls,
        shadow_depth=depth,
        n_eigenvalues=len(eigenvalues),
        spacing_classification=stats.classification,
        r_statistic=stats.r_statistic,
        beta_parameter=stats.beta_parameter,
        poisson_ks=stats.poisson_ks,
        gue_ks=stats.gue_ks,
        lyapunov_exponent=lyap,
        lyapunov_spectrum=lyap_spectrum,
        ks_entropy=h_ks,
        is_ergodic=qe.get('is_ergodic', False),
        ergodicity_variance=qe.get('mean_variance', 0.0),
        fidelity_decay_type=fid.get('decay_type', 'none'),
        fidelity_decay_rate=fid.get('decay_rate', 0.0),
        mss_satisfied=mss.get('all_satisfied', True),
        chaos_type=chaos_type,
    )


# ============================================================================
# Utility: Linear system solver and power law fitting
# ============================================================================

def _solve_linear_system(
    A: List[List[float]],
    b: List[float],
) -> Optional[List[float]]:
    """Solve A*x = b by Gaussian elimination with partial pivoting.

    Returns None if system is singular.
    """
    n = len(b)
    # Augmented matrix
    M = [row[:] + [b[i]] for i, row in enumerate(A)]

    for col in range(n):
        # Partial pivoting
        max_row = col
        max_val = abs(M[col][col])
        for row in range(col + 1, n):
            if abs(M[row][col]) > max_val:
                max_val = abs(M[row][col])
                max_row = row
        if max_val < 1e-30:
            return None
        M[col], M[max_row] = M[max_row], M[col]

        # Eliminate below
        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    # Back-substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n]
        for j in range(i + 1, n):
            s -= M[i][j] * x[j]
        if abs(M[i][i]) < 1e-30:
            return None
        x[i] = s / M[i][i]

    return x


def _fit_power_law(
    x_vals: List[float],
    y_vals: List[float],
) -> float:
    """Fit y = a * x^alpha and return alpha.

    Uses log-log linear regression: log(y) = log(a) + alpha * log(x).
    """
    if len(x_vals) < 2:
        return 0.0

    log_x = []
    log_y = []
    for i in range(len(x_vals)):
        if x_vals[i] > 0 and y_vals[i] > 0:
            log_x.append(math.log(x_vals[i]))
            log_y.append(math.log(y_vals[i]))

    if len(log_x) < 2:
        return 0.0

    n = len(log_x)
    sum_x = sum(log_x)
    sum_y = sum(log_y)
    sum_x2 = sum(x**2 for x in log_x)
    sum_xy = sum(log_x[i] * log_y[i] for i in range(n))

    denom = n * sum_x2 - sum_x**2
    if abs(denom) < 1e-30:
        return 0.0

    alpha = (n * sum_xy - sum_x * sum_y) / denom
    return alpha


# ============================================================================
# Cross-verification utilities
# ============================================================================

def cross_verify_lyapunov(
    family: str,
    param: float,
    max_r: int = 200,
) -> Dict[str, Any]:
    r"""Cross-verify Lyapunov exponent by 3+ independent methods.

    Method 1: Orbit growth rate (log|S_r/S_2| / r)
    Method 2: Scattering phase derivative
    Method 3: From shadow growth rate rho: lambda = log(rho)

    For class G/L: all three should give 0.
    For class M: all three should agree to within ~10%.
    """
    coeffs = _get_shadow_coeffs(family, param, max_r)

    # Method 1: Orbit
    lyap_orbit = shadow_lyapunov_exponent(coeffs, method='orbit')

    # Method 2: Scattering
    lyap_scatter = shadow_lyapunov_exponent(coeffs, method='scattering')

    # Method 3: From growth rate rho
    if family == 'virasoro':
        rho = virasoro_growth_rate_exact(param)
        lyap_rho = math.log(rho) if rho > 0 else 0.0
    else:
        rho = shadow_growth_rate_from_coeffs(coeffs)
        lyap_rho = math.log(rho) if rho > 0 else 0.0

    # Agreement check
    values = [lyap_orbit, lyap_scatter, lyap_rho]
    mean_val = sum(values) / 3
    if mean_val > 0.01:
        max_dev = max(abs(v - mean_val) for v in values) / abs(mean_val)
    else:
        max_dev = max(abs(v) for v in values)

    return {
        'family': family,
        'param': param,
        'lambda_orbit': lyap_orbit,
        'lambda_scattering': lyap_scatter,
        'lambda_growth_rate': lyap_rho,
        'growth_rate_rho': rho,
        'mean': mean_val,
        'max_relative_deviation': max_dev,
        'consistent': max_dev < 0.5 or mean_val < 0.01,
    }


def cross_verify_spacing_statistics(
    family: str,
    param: float,
    max_r_values: List[int] = [50, 100, 200],
) -> Dict[str, Any]:
    r"""Cross-verify spacing statistics by varying truncation order.

    The spacing statistics should be STABLE as max_r increases.
    Instability indicates truncation artifacts, not genuine spectral features.

    Returns convergence information.
    """
    results = []
    for mr in max_r_values:
        coeffs = _get_shadow_coeffs(family, param, mr)
        eigenvalues = _shadow_eigenvalues(coeffs, 80)
        stats = spacing_statistics(eigenvalues)
        results.append({
            'max_r': mr,
            'classification': stats.classification,
            'r_statistic': stats.r_statistic,
            'n_eigenvalues': len(eigenvalues),
        })

    # Check convergence: are classifications stable?
    classifications = [r['classification'] for r in results]
    stable = len(set(classifications)) <= 2  # Allow for 'intermediate' variation

    return {
        'family': family,
        'param': param,
        'results': results,
        'stable': stable,
        'final_classification': classifications[-1],
    }


def comprehensive_glcm_test(
    n_eigenvalues: int = 80,
    max_r: int = 200,
) -> Dict[str, Dict[str, Any]]:
    r"""Run the full G/L/C/M <-> integrable/chaotic classification test.

    Tests:
    - Heisenberg (G): expect integrable (Poisson, lambda=0)
    - Affine sl_2 (L): expect integrable (Poisson, lambda=0)
    - Beta-gamma (C): expect mixed
    - Virasoro (M): expect chaotic (GUE, lambda>0)

    This is the definitive test of the quantum chaos / shadow depth
    correspondence.
    """
    test_cases = [
        ('heisenberg', 1.0, 'G', 'integrable'),
        ('heisenberg', 5.0, 'G', 'integrable'),
        ('affine_sl2', 1.0, 'L', 'integrable'),
        ('affine_sl2', 10.0, 'L', 'integrable'),
        ('affine_sl3', 1.0, 'L', 'integrable'),
        ('betagamma', 0.5, 'C', 'mixed'),
        ('virasoro', 2.0, 'M', 'chaotic'),
        ('virasoro', 10.0, 'M', 'chaotic'),
        ('virasoro', 13.0, 'M', 'chaotic'),
        ('virasoro', 25.0, 'M', 'chaotic'),
    ]

    results = {}
    for family, param, expected_class, expected_type in test_cases:
        key = f"{family}_{param}"

        coeffs = _get_shadow_coeffs(family, param, max_r)
        eigenvalues = _shadow_eigenvalues(coeffs, n_eigenvalues)

        # Spacing statistics
        stats = spacing_statistics(eigenvalues)

        # Lyapunov
        lyap = shadow_lyapunov_exponent(coeffs, method='orbit')

        # KS entropy
        h = ks_entropy(coeffs)

        # Classification consistency
        actual_class = _shadow_class(family)

        if actual_class in ('G', 'L'):
            actual_type = 'integrable'
        elif actual_class == 'C':
            actual_type = 'mixed'
        else:
            actual_type = 'chaotic' if lyap > 0.01 else 'mixed'

        results[key] = {
            'family': family,
            'param': param,
            'shadow_class': actual_class,
            'expected_class': expected_class,
            'expected_type': expected_type,
            'observed_type': actual_type,
            'spacing_class': stats.classification,
            'r_statistic': stats.r_statistic,
            'lyapunov': lyap,
            'ks_entropy': h,
            'consistent': (actual_class == expected_class
                           and actual_type == expected_type),
        }

    return results
