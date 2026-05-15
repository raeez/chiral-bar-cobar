r"""Scalar zeta-zero evaluations for the twisted-holography package.

The manuscript datum is the seven-entry typed record

    H(T) = (A, A^i, A^!, C, r(z), Theta_A, nabla^hol).

This module does not construct the full holomorphic-topological theory.  It
keeps a scalar/typed-summary shadow of the datum while evaluating numerical
functions at parameters built from the positive imaginary parts rho_n of the
nontrivial zeros 1/2 + i*rho_n of the Riemann zeta function.

The zeta-zero evaluation is exploratory.  There is no theorem or physical
principle in this repository that identifies Riemann zeta zeros with modular,
BTZ, celestial, or Chern-Simons parameters.  The map

    tau_n = i * (1 + rho_n) / (4*pi)

is only a convergence-friendly probe: q_n = exp(2*pi*i*tau_n)
= exp(-(1+rho_n)/2).  It is not the Selberg zeta of the BTZ quotient; that
geometry is handled by bc_btz_spectral_zeta_engine.py.

The rigorous scalar computations retained here are:
  - q-series partition functions with q = exp(2*pi*i*tau);
  - Faber-Pandharipande lambda_g numbers and F_g = kappa(A) lambda_g;
  - Cardy/BTZ algebraic identities at the chosen beta_n;
  - Chern-Simons solid-torus normalizations at integer level;
  - annulus trace kappa(A) lambda_1;
  - typed separation of B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A).

The numerical probes at rho_n are recorded as probes, not as holographic
predictions.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple


# ===========================================================================
# Constants
# ===========================================================================

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2
EULER_GAMMA = 0.5772156649015329  # Euler-Mascheroni constant

# First 30 nontrivial zeros of the Riemann zeta function (imaginary parts).
# These are the positive imaginary parts rho_n such that zeta(1/2 + i*rho_n) = 0.
# Source: LMFDB / Odlyzko tables, verified to 10+ digits.
RIEMANN_ZETA_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081607,
    67.079810529494174,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492980517050,
    87.425274613125196,
    88.809111207634465,
    92.491899270558484,
    94.651344040519838,
    95.870634228245309,
    98.831194218193692,
    101.31785100573139,
]


HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)

TYPED_FIREWALL_OBJECTS: Tuple[str, ...] = (
    "A",
    "B(A)",
    "A^i",
    "A^!",
    "Omega(B(A))",
    "Z_ch^der(A)",
)


def _as_fraction(x) -> Fraction:
    """Coerce exact scalar input to Fraction."""
    if isinstance(x, Fraction):
        return x
    return Fraction(x)


def _fraction_label(x) -> str:
    """Compact exact label for algebra names."""
    frac = _as_fraction(x)
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


# ===========================================================================
# Section 1: Modular characteristics (exact arithmetic)
# ===========================================================================

def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.

    This is kappa(A) for A = Vir_c.  It is not kappa_eff, which adds the
    ghost contribution.
    """
    return _as_fraction(c) / Fraction(2)


def kappa_heisenberg(k) -> Fraction:
    """kappa(H_k) = k.

    Single generator of weight 1 at level k.
    """
    return _as_fraction(k)


def kappa_kac_moody(dim_g: int, k, h_dual) -> Fraction:
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2*h^v).

    This is the affine-family modular characteristic, not c/2 in general.
    """
    return Fraction(dim_g) * (_as_fraction(k) + _as_fraction(h_dual)) / (2 * _as_fraction(h_dual))


def kappa_wn(c, N: int) -> Fraction:
    """kappa(W_N) = c * (H_N - 1) where H_N = sum_{j=1}^N 1/j.

    This agrees with Virasoro at N=2 and differs from c/2 for N >= 3.
    """
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    return _as_fraction(c) * (H_N - 1)


def central_charge_km(dim_g: int, k, h_dual) -> Fraction:
    """Central charge c(V_k(g)) = k * dim(g) / (k + h^v)."""
    return _as_fraction(k) * Fraction(dim_g) / (_as_fraction(k) + _as_fraction(h_dual))


def central_charge_betagamma(lam=1) -> Fraction:
    r"""Central charge of the bosonic beta-gamma system.

    c_{beta gamma}(lambda) = 2 * (6 lambda^2 - 6 lambda + 1).
    """
    lam = _as_fraction(lam)
    return 2 * (6 * lam * lam - 6 * lam + 1)


def kappa_betagamma(lam=1) -> Fraction:
    r"""Modular characteristic of beta-gamma_lambda.

    kappa(beta gamma_lambda) = c_{beta gamma}(lambda) / 2
    = 6 lambda^2 - 6 lambda + 1.
    """
    return central_charge_betagamma(lam) / 2


def central_charge_bc(lam=1) -> Fraction:
    r"""Central charge of the fermionic bc system.

    c_{bc}(lambda) = -2 * (6 lambda^2 - 6 lambda + 1).
    """
    return -central_charge_betagamma(lam)


def kappa_bc(lam=1) -> Fraction:
    r"""Modular characteristic of bc_lambda.

    The beta-gamma/bc free-field pair cancels on the scalar lane:
    kappa(beta gamma_lambda) + kappa(bc_lambda) = 0.
    """
    return central_charge_bc(lam) / 2


def kappa_ghost() -> Fraction:
    """kappa(bc ghosts) = -13.

    The bc ghost system for the bosonic string has c_ghost = -26,
    so kappa(ghost) = c_ghost/2 = -13.  (Treated as Virasoro at c=-26.)
    """
    return Fraction(-13)


def kappa_eff(kappa_matter: Fraction) -> Fraction:
    """Effective curvature kappa_eff = kappa(matter) + kappa(ghost).

    Vanishes at c_matter = 26 (bosonic string critical dimension).
    """
    return kappa_matter + kappa_ghost()


def delta_kappa(kappa_A: Fraction, kappa_A_dual: Fraction) -> Fraction:
    """Complementarity asymmetry delta_kappa = kappa(A) - kappa(A!).

    For KM/free fields: delta_kappa = 2*kappa(A) (since kappa+kappa'=0).
    For Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, so
      delta_kappa = c/2 - (26-c)/2 = c - 13.
    """
    return kappa_A - kappa_A_dual


# ===========================================================================
# Section 2: Faber-Pandharipande intersection numbers
# ===========================================================================

@lru_cache(maxsize=64)
def _bernoulli_2g(g: int) -> Fraction:
    """Exact Bernoulli number B_{2g}."""
    _TABLE = {
        1: Fraction(1, 6),
        2: Fraction(-1, 30),
        3: Fraction(1, 42),
        4: Fraction(-1, 30),
        5: Fraction(5, 66),
        6: Fraction(-691, 2730),
        7: Fraction(7, 6),
        8: Fraction(-3617, 510),
        9: Fraction(43867, 798),
        10: Fraction(-174611, 330),
    }
    if g in _TABLE:
        return _TABLE[g]
    try:
        from sympy import bernoulli as sympy_bernoulli, Rational
        return Fraction(Rational(sympy_bernoulli(2 * g)))
    except ImportError:
        raise ValueError(f"B_{{{2*g}}} not hardcoded and sympy unavailable")


def _factorial_fraction(n: int) -> Fraction:
    """n! as exact Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    These are positive for all g >= 1; the absolute Bernoulli value fixes the
    sign convention.

    Verified values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B_2g = _bernoulli_2g(g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B_2g)
    den = power * _factorial_fraction(2 * g)
    return num / den


# ===========================================================================
# Section 3: Zeta-zero to modular parameter mapping (formal probe)
# ===========================================================================

def zeta_zero(n: int) -> float:
    """Return the n-th nontrivial zero imaginary part rho_n (1-indexed).

    These are the positive imaginary parts of the nontrivial zeros of
    the Riemann zeta function: zeta(1/2 + i*rho_n) = 0.
    """
    if n < 1 or n > len(RIEMANN_ZETA_ZEROS):
        raise ValueError(
            f"Zeta zero index must be in [1, {len(RIEMANN_ZETA_ZEROS)}], got {n}"
        )
    return RIEMANN_ZETA_ZEROS[n - 1]


def modular_parameter_from_zeta_zero(n: int) -> complex:
    r"""Map zeta zero rho_n to modular parameter tau_n.

    Formal probe map:
        tau_n = i * (1 + rho_n) / (4*pi)

    This places tau in the upper half-plane (Im(tau) > 0) for rho_n > 0.
    The nome is q_n = e^{2*pi*i*tau_n} = e^{-(1+rho_n)/2}.

    The map is chosen so that |q_n| < 1
    (ensuring convergence of q-series) and so that larger rho_n gives
    smaller |q_n| (stronger convergence).  No physical derivation is assumed.
    """
    rho_n = zeta_zero(n)
    return 1j * (1.0 + rho_n) / (4.0 * PI)


def nome_from_zeta_zero(n: int) -> complex:
    r"""Nome q_n = e^{2*pi*i*tau_n} at the n-th zeta zero parameter.

    q_n = e^{-(1 + rho_n)/2}.

    Since rho_1 ~ 14.13, we have |q_1| ~ e^{-7.57} ~ 5.2e-4.
    The q-series converges extremely rapidly at all zeta zero parameters.
    """
    rho_n = zeta_zero(n)
    return cmath.exp(-(1.0 + rho_n) / 2.0)


def spectral_parameter_from_zeta_zero(n: int) -> complex:
    r"""Spectral parameter s_n = 1/2 + i*rho_n on the critical line.

    This is the standard parameterization of the critical strip:
    the n-th zero is at s_n = 1/2 + i*rho_n.
    """
    rho_n = zeta_zero(n)
    return complex(0.5, rho_n)


def mellin_parameter_from_zeta_zero(n: int) -> complex:
    r"""Mellin/conformal dimension probe Delta_n = 1/2 + i*rho_n.

    In celestial holography, the Mellin transform of a bulk scattering
    amplitude has conformal dimension Delta.  This function sets Delta to
    the Riemann-zero spectral parameter for a formal numerical probe.

    This identification is formal.  Celestial conformal dimensions are
    real for physical operators; complex Delta corresponds to principal-series
    representations (which DO appear in the celestial basis, cf. Pasterski-
    Shao-Strominger).  The claim that zeta zeros have special significance
    for celestial amplitudes is not established.
    """
    return spectral_parameter_from_zeta_zero(n)


# ===========================================================================
# Section 4: Boundary partition functions
# ===========================================================================

def dedekind_eta(tau: complex, n_max: int = 200) -> complex:
    r"""Dedekind eta function: eta(tau) = q^{1/24} * prod_{n>=1} (1 - q^n).

    Parameters
    ----------
    tau : complex
        Modular parameter with Im(tau) > 0.
    n_max : int
        Product truncation (200 terms gives machine precision for |q| < 0.9).
    """
    if tau.imag <= 0:
        raise ValueError(f"Need Im(tau) > 0, got Im(tau) = {tau.imag}")
    q = cmath.exp(2.0 * PI * 1j * tau)
    # q^{1/24}
    prefactor = cmath.exp(2.0 * PI * 1j * tau / 24.0)
    product = complex(1.0, 0.0)
    q_power = q
    for _ in range(1, n_max + 1):
        product *= (1.0 - q_power)
        q_power *= q
    return prefactor * product


def boundary_partition_virasoro(tau: complex, c: float = 26.0,
                                 n_max: int = 200) -> complex:
    r"""Verma-character boundary partition function for Virasoro.

    The computed scalar is

        Z(tau) = q^{-c/24} * prod_{n>=1} (1 - q^n)^{-1},

    with q = exp(2*pi*i*tau).  This is the Verma-module character used by
    the numerical probes, not the irreducible vacuum VOA character with the
    L_{-1} quotient removed.
    """
    if tau.imag <= 0:
        raise ValueError(f"Need Im(tau) > 0, got Im(tau) = {tau.imag}")
    q = cmath.exp(2.0 * PI * 1j * tau)
    # q^{-c/24}
    vacuum_factor = cmath.exp(-2.0 * PI * 1j * tau * c / 24.0)
    # 1 / prod_{n>=1}(1-q^n)
    product = complex(1.0, 0.0)
    q_power = q
    for n in range(1, n_max + 1):
        product *= (1.0 - q_power)
        q_power *= q
    return vacuum_factor / product


def boundary_partition_heisenberg(tau: complex, k: float = 1.0,
                                   n_max: int = 200) -> complex:
    r"""Boundary partition function for the Heisenberg algebra at level k.

    Single free boson: Z(tau) = q^{-1/24} / prod_{n>=1}(1-q^n) = 1/eta(tau).

    For the rank-r Heisenberg (r free bosons):
        Z(tau) = 1 / eta(tau)^r

    Here we compute for a single boson (rank 1).  The central charge is 1.
    """
    eta_val = dedekind_eta(tau, n_max)
    if abs(eta_val) < 1e-300:
        return complex(float('inf'), 0)
    return 1.0 / eta_val


def boundary_partition_km(tau: complex, dim_g: int, k: int, h_dual: int,
                           n_max: int = 200) -> complex:
    r"""Boundary partition function for affine KM at level k.

    For V_k(g), the vacuum character is:
        chi_0(tau) = q^{-c/24} * prod_{n>=1} (1-q^n)^{-dim(g)}
                   = q^{-c/24} / eta(tau)^{dim(g)} * q^{dim(g)/24}
                   = q^{(-c+dim(g))/24} / eta(tau)^{dim(g)}

    where c = k*dim(g)/(k+h^v).

    This is the CHARACTER of the vacuum module, not the full partition
    function (which would sum over all integrable modules).
    """
    c = float(k) * dim_g / (float(k) + float(h_dual))
    q = cmath.exp(2.0 * PI * 1j * tau)
    vacuum_factor = cmath.exp(-2.0 * PI * 1j * tau * c / 24.0)
    product = complex(1.0, 0.0)
    q_power = q
    for n in range(1, n_max + 1):
        product *= (1.0 - q_power) ** dim_g
        q_power *= q
    return vacuum_factor / product


# ===========================================================================
# Section 5: Boundary partition at zeta-zero parameters
# ===========================================================================

def boundary_Z_at_zeta_zero(n: int, c: float = 26.0,
                             algebra: str = 'virasoro',
                             **kwargs) -> complex:
    r"""Evaluate the boundary partition function at the n-th zeta zero parameter.

    tau_n = i*(1+rho_n)/(4*pi), used only as a formal numerical probe.

    Returns Z_partial(tau_n) for the specified algebra.
    """
    tau = modular_parameter_from_zeta_zero(n)
    if algebra == 'virasoro':
        return boundary_partition_virasoro(tau, c=c)
    elif algebra == 'heisenberg':
        return boundary_partition_heisenberg(tau)
    elif algebra == 'kac_moody':
        dim_g = kwargs.get('dim_g', 3)
        k = kwargs.get('k', 1)
        h_dual = kwargs.get('h_dual', 2)
        return boundary_partition_km(tau, dim_g, k, h_dual)
    else:
        raise ValueError(f"Unknown algebra: {algebra}")


def boundary_Z_table(c: float = 26.0, n_max: int = 10,
                      algebra: str = 'virasoro',
                      **kwargs) -> Dict[int, complex]:
    """Table of Z_partial(tau_n) for n = 1..n_max."""
    return {
        n: boundary_Z_at_zeta_zero(n, c=c, algebra=algebra, **kwargs)
        for n in range(1, n_max + 1)
    }


# ===========================================================================
# Section 6: Bulk shadow at zeta-zero parameters
# ===========================================================================

def bulk_shadow_Fg(kappa_val: Fraction, g: int) -> Fraction:
    r"""Scalar free energy F_g = kappa * lambda_g^FP.

    This is the SCALAR LANE contribution (proved for uniform-weight
    algebras at all genera; genus 1 unconditional for all families).

    This scalar projection depends on kappa, not on the full Theta_A.
    Higher-arity corrections exist for class M algebras at g >= 2.
    """
    return Fraction(kappa_val) * lambda_fp(g)


def bulk_shadow_effective(c_matter: float, g: int) -> float:
    r"""Effective bulk shadow: F_g^{eff} = kappa_eff * lambda_g^FP.

    kappa_eff = kappa(matter) + kappa(ghost) = c/2 - 13.
    At c=26: kappa_eff = 0, so ALL scalar free energies vanish.
    This is the anomaly cancellation condition for the bosonic string.
    """
    kappa_m = kappa_virasoro(Fraction(c_matter))
    kappa_e = kappa_eff(kappa_m)
    return float(kappa_e * lambda_fp(g))


def bulk_shadow_table(c_matter: float, g_max: int = 5) -> Dict[str, Any]:
    r"""Table of bulk shadow data.

    Returns both the matter and effective (matter+ghost) free energies.
    """
    kappa_m = kappa_virasoro(Fraction(c_matter))
    kappa_e = kappa_eff(kappa_m)

    matter = {g: float(bulk_shadow_Fg(kappa_m, g)) for g in range(1, g_max + 1)}
    effective = {g: float(bulk_shadow_Fg(kappa_e, g)) for g in range(1, g_max + 1)}

    return {
        'c_matter': c_matter,
        'kappa_matter': float(kappa_m),
        'kappa_ghost': float(kappa_ghost()),
        'kappa_eff': float(kappa_e),
        'F_g_matter': matter,
        'F_g_effective': effective,
        'anomaly_cancelled': (kappa_e == 0),
    }


# ===========================================================================
# Section 6b: Seven-entry typed package
# ===========================================================================

def _algebra_label(algebra: str = 'virasoro', c: float = 26.0, **kwargs) -> str:
    """Human-readable boundary algebra label for the A slot."""
    if algebra == 'virasoro':
        return f"Vir_{_fraction_label(c)}"
    if algebra == 'heisenberg':
        return f"H_{_fraction_label(kwargs.get('k', kwargs.get('level', 1)))}"
    if algebra == 'kac_moody':
        dim_g = kwargs.get('dim_g', 3)
        k = kwargs.get('k', 1)
        h_dual = kwargs.get('h_dual', 2)
        return f"V_{_fraction_label(k)}(g_dim={dim_g},h_dual={h_dual})"
    if algebra == 'betagamma':
        return f"betagamma_{_fraction_label(kwargs.get('lam', 1))}"
    if algebra == 'bc':
        return f"bc_{_fraction_label(kwargs.get('lam', 1))}"
    raise ValueError(f"Unknown algebra: {algebra}")


def _dual_label(algebra: str = 'virasoro', c: float = 26.0, **kwargs) -> str:
    """Human-readable Verdier/Koszul companion label for the A^! slot."""
    if algebra == 'virasoro':
        return f"Vir_{_fraction_label(_as_fraction(26) - _as_fraction(c))}"
    if algebra == 'heisenberg':
        return "Sym^ch(V*)"
    if algebra == 'kac_moody':
        return f"Verdier/Koszul companion of {_algebra_label(algebra, c, **kwargs)}"
    if algebra == 'betagamma':
        return f"bc_{_fraction_label(kwargs.get('lam', 1))}"
    if algebra == 'bc':
        return f"betagamma_{_fraction_label(kwargs.get('lam', 1))}"
    raise ValueError(f"Unknown algebra: {algebra}")


def _kappa_for_algebra(algebra: str = 'virasoro', c: float = 26.0, **kwargs) -> Fraction:
    """Exact kappa(A) for supported A-slot families."""
    if algebra == 'virasoro':
        return kappa_virasoro(c)
    if algebra == 'heisenberg':
        return kappa_heisenberg(kwargs.get('k', kwargs.get('level', 1)))
    if algebra == 'kac_moody':
        return kappa_kac_moody(
            kwargs.get('dim_g', 3),
            kwargs.get('k', 1),
            kwargs.get('h_dual', 2),
        )
    if algebra == 'betagamma':
        return kappa_betagamma(kwargs.get('lam', 1))
    if algebra == 'bc':
        return kappa_bc(kwargs.get('lam', 1))
    raise ValueError(f"Unknown algebra: {algebra}")


def _r_matrix_summary(algebra: str = 'virasoro', c: float = 26.0, **kwargs) -> str:
    """Scalar r(z) slot with line/contact data kept out of the closed slot."""
    if algebra == 'virasoro':
        return f"r^Vir(z) = {_fraction_label(kappa_virasoro(c))}/z^3 + 2T/z"
    if algebra == 'heisenberg':
        k = kwargs.get('k', kwargs.get('level', 1))
        return f"r^Heis(z) = {_fraction_label(k)}/z"
    if algebra == 'kac_moody':
        k = kwargs.get('k', 1)
        return f"r^KM(z) = {_fraction_label(k)}*Omega/z"
    if algebra in ('betagamma', 'bc'):
        return "closed r(z) = 0; simple OPE/contact datum is boundary data"
    raise ValueError(f"Unknown algebra: {algebra}")


def seven_entry_package_at_zeta_zero(
    n: int,
    c: float = 26.0,
    algebra: str = 'virasoro',
    **kwargs,
) -> Dict[str, Any]:
    r"""Return the seven-entry scalar/typed-summary package.

    The package entries are exactly

        (A, A^i, A^!, C, r(z), Theta_A, nabla^hol).

    The zeta zero index is validated so that this record can be attached to
    zeta-zero scans, but the typed package itself is a property of A and its
    scalar shadow, not a property of the zero rho_n.
    """
    zeta_zero(n)
    A = _algebra_label(algebra, c, **kwargs)
    return {
        "A": A,
        "A^i": f"H^*(B^ch({A})) bar-dual coalgebra",
        "A^!": _dual_label(algebra, c, **kwargs),
        "C": f"Z_ch^der({A}) = C_ch^bullet({A},{A})",
        "r(z)": _r_matrix_summary(algebra, c, **kwargs),
        "Theta_A": _kappa_for_algebra(algebra, c, **kwargs),
        "nabla^hol": True,
    }


def typed_object_firewall(
    c: float = 26.0,
    algebra: str = 'virasoro',
    **kwargs,
) -> Dict[str, Any]:
    """Separate B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A)."""
    A = _algebra_label(algebra, c, **kwargs)
    A_dual = _dual_label(algebra, c, **kwargs)
    return {
        "A": f"{A}: boundary chiral algebra",
        "B(A)": (
            f"B(A) = B^ch({A}) is the chiral bar coalgebra complex; "
            "its cohomology gives A^i, but the complex is not A^i itself"
        ),
        "A^i": (
            f"A^i = H^*(B^ch({A})) bar-dual coalgebra; "
            "not B(A), not A^!, not Omega(B(A)), and not Z_ch^der(A)"
        ),
        "A^!": (
            f"{A_dual}: Verdier/Koszul companion; "
            "not B(A), not A^i, not Omega(B(A)), and not Z_ch^der(A)"
        ),
        "Omega(B(A))": (
            f"Omega(B(A)) recovers {A} by bar-cobar inversion; "
            "not A^! and not Z_ch^der(A)"
        ),
        "Z_ch^der(A)": (
            f"Z_ch^der({A}) is the chiral Hochschild/derived-center C slot; "
            "not B(A), not A^i, not A^!, and not Omega(B(A))"
        ),
        "forbidden_identifications": (
            "B(A) != A^i",
            "A^i != A^!",
            "Omega(B(A)) != A^!",
            "Z_ch^der(A) != Omega(B(A))",
            "Z_ch^der(A) != A^!",
        ),
    }


# ===========================================================================
# Section 7: Twisted partition function (refined index)
# ===========================================================================

def twisted_partition_virasoro(tau: complex, z: complex, c: float = 26.0,
                                J_max: int = 50, n_max: int = 200) -> complex:
    r"""Twisted partition function Z(tau, z) = Tr(q^{L_0-c/24} y^{J_0}).

    For a Virasoro algebra, there is no conserved U(1) current J_0 unless
    we add one (e.g., spectral flow or a free boson).  For the Heisenberg
    extension of Virasoro (free boson + Virasoro), we have J_0 = a_0
    (zero mode of the free boson).  The twisted partition function is:

        Z(tau, z) = q^{-c/24} * y^0 * prod_{n>=1} (1-q^n)^{-1}
                  * sum_m y^m q^{m^2/(2k)}    [Heisenberg zero-mode sum]

    For the pure Virasoro without a conserved current, Z(tau, z) degenerates
    to Z(tau, 0) = Z(tau).  We compute the HEISENBERG-EXTENDED version.

    Parameters
    ----------
    tau : complex with Im(tau) > 0
    z : complex (the twist parameter; y = e^{2*pi*i*z})
    c : central charge
    J_max : truncation for zero-mode sum
    n_max : product truncation
    """
    if tau.imag <= 0:
        raise ValueError(f"Need Im(tau) > 0, got {tau.imag}")

    q = cmath.exp(2.0 * PI * 1j * tau)
    y = cmath.exp(2.0 * PI * 1j * z)

    # Vacuum factor
    vacuum = cmath.exp(-2.0 * PI * 1j * tau * c / 24.0)

    # Oscillator product: prod_{n>=1} (1-q^n)^{-1}
    product = complex(1.0, 0.0)
    q_power = q
    for _ in range(1, n_max + 1):
        product *= (1.0 - q_power)
        q_power *= q
    oscillator = 1.0 / product

    # Zero-mode sum: sum_{m=-J_max}^{J_max} y^m q^{m^2/2}
    # (k=1 Heisenberg; for general k, replace m^2/2 -> m^2/(2k))
    # Compute via log to avoid overflow: y^m * q^{m^2/2} = exp(m*log(y) + m^2*pi*i*tau)
    log_y = cmath.log(y) if abs(y) > 1e-300 else complex(-1e300, 0)
    zero_mode_sum = complex(0.0, 0.0)
    for m in range(-J_max, J_max + 1):
        log_term = m * log_y + PI * 1j * tau * m * m
        # Skip terms with extremely large negative real part (underflow)
        if log_term.real > -500:
            zero_mode_sum += cmath.exp(log_term)

    return vacuum * oscillator * zero_mode_sum


def twisted_Z_at_zeta_zero(n: int, c: float = 26.0,
                             z_mode: str = 'half_rho') -> complex:
    r"""Twisted partition function at zeta-zero parameters.

    Parameters
    ----------
    n : zeta zero index (1-indexed)
    c : central charge
    z_mode : how to set the twist parameter z
        'half_rho': z = rho_n / 2  (formal probe)
        'spectral': z = (1/2 + i*rho_n) / 2  (formal probe)
        'zero': z = 0 (reduces to untwisted partition function)
    """
    tau = modular_parameter_from_zeta_zero(n)
    rho_n = zeta_zero(n)

    if z_mode == 'half_rho':
        z = complex(0, rho_n / 2.0)
    elif z_mode == 'spectral':
        z = complex(0.25, rho_n / 4.0)
    elif z_mode == 'zero':
        z = complex(0, 0)
    else:
        raise ValueError(f"Unknown z_mode: {z_mode}")

    return twisted_partition_virasoro(tau, z, c=c)


# ===========================================================================
# Section 8: Celestial OPE at zeta-zero Mellin parameters
# ===========================================================================

def celestial_soft_factor(Delta: complex, spin: int = 2) -> complex:
    r"""Leading celestial soft factor S^{(0)} at conformal dimension Delta.

    For spin-s conformal primary operators on the celestial sphere,
    the leading soft theorem (Strominger 2014) gives:

        S^{(0)}_{s}(Delta) = 1 / (Delta - 1)     [supertranslation, s=0]
        S^{(1)}_{s}(Delta) = 1 / (Delta - 1)^2   [superrotation, s=1]

    For graviton scattering (s=2), the Weinberg soft factor is:
        S_0^grav(Delta) = kappa / (Delta - 1)

    where kappa here is the gravitational coupling (NOT the modular
    characteristic of the manuscript; regrettable notational collision).

    We compute with the coupling set to 1 (normalized soft factor).

    Parameters
    ----------
    Delta : complex conformal dimension (Mellin parameter)
    spin : spin of the soft particle (0, 1, or 2)
    """
    if abs(Delta - 1.0) < 1e-15:
        return complex(float('inf'), 0)
    if spin == 0:
        return 1.0 / (Delta - 1.0)
    elif spin == 1:
        return 1.0 / (Delta - 1.0) ** 2
    elif spin == 2:
        return 1.0 / (Delta - 1.0)
    else:
        # General spin: S^{(0)} ~ 1/(Delta - 1 + s - 2)
        return 1.0 / (Delta - 1.0 + spin - 2.0)


def celestial_collinear_kernel(
    Delta_1: complex,
    Delta_2: complex,
    spin_1: int = 2,
    spin_2: int = 2,
    normalization: str = "unit_euler_beta",
) -> complex:
    r"""Unshifted Euler-beta collinear kernel B(Delta_1, Delta_2).

    The scalar kernel stored by this engine is

        B(Delta_1, Delta_2) = Gamma(Delta_1) * Gamma(Delta_2) / Gamma(Delta_1 + Delta_2)

    with unit normalization and no spin, colour, coupling, or shifted-weight
    dressing.  The spin parameters are retained for API compatibility but do
    not change this scalar Euler-beta value.
    """
    if normalization != "unit_euler_beta":
        raise ValueError(f"Unknown kernel normalization: {normalization}")
    try:
        import scipy.special as sp
        g1 = sp.gamma(complex(Delta_1))
        g2 = sp.gamma(complex(Delta_2))
        g12 = sp.gamma(complex(Delta_1 + Delta_2))
        if abs(g12) < 1e-300:
            return complex(float('inf'), 0)
        return g1 * g2 / g12
    except ImportError:
        return _gamma_ratio_fallback(Delta_1, Delta_2)


def _gamma_ratio_fallback(a: complex, b: complex) -> complex:
    """Fallback Beta(a,b) = Gamma(a)*Gamma(b)/Gamma(a+b) via Stirling."""
    a_complex = complex(a)
    b_complex = complex(b)
    if abs(a_complex.imag) < 1e-15 and abs(b_complex.imag) < 1e-15:
        if a_complex.real > 0 and b_complex.real > 0:
            numerator = math.gamma(a_complex.real) * math.gamma(b_complex.real)
            denominator = math.gamma(a_complex.real + b_complex.real)
            return complex(numerator / denominator, 0.0)

    # Stirling: log Gamma(z) ~ z*log(z) - z - 0.5*log(z) + 0.5*log(2*pi)
    def log_stirling(z):
        z = complex(z)
        return z * cmath.log(z) - z - 0.5 * cmath.log(z) + 0.5 * math.log(TWO_PI)

    log_beta = log_stirling(a) + log_stirling(b) - log_stirling(a + b)
    return cmath.exp(log_beta)


def celestial_at_zeta_zero(n: int, spin: int = 2) -> Dict[str, Any]:
    r"""Celestial soft factor and collinear kernel at zeta-zero parameter.

    Delta_n = 1/2 + i*rho_n  (the spectral parameter on the critical line).

    This evaluation has no established physical meaning.
    The celestial conformal dimension for physical gravitons is real.
    Complex Delta corresponds to principal-series representations.
    """
    Delta = mellin_parameter_from_zeta_zero(n)
    rho_n = zeta_zero(n)

    soft = celestial_soft_factor(Delta, spin)
    collinear = celestial_collinear_kernel(Delta, Delta, spin, spin)

    return {
        'n': n,
        'rho_n': rho_n,
        'Delta': Delta,
        'soft_factor': soft,
        'collinear_kernel': collinear,
        'kernel_normalization': 'unit_euler_beta',
        'abs_soft': abs(soft),
        'abs_collinear': abs(collinear),
    }


# ===========================================================================
# Section 9: BTZ black hole at zeta-zero parameters
# ===========================================================================

def btz_at_zeta_zero(n: int, c: float = 26.0) -> Dict[str, Any]:
    r"""BTZ black hole thermodynamics at zeta-zero modular parameter.

    The BTZ modular parameter tau = i*beta/(2*pi) where beta = 1/T_H.
    From tau_n = i*(1+rho_n)/(4*pi), we read off:
        beta_n = (1+rho_n)/2
        T_H_n = 2/(1+rho_n)

    The Bekenstein-Hawking entropy at this temperature:
        S_BH = pi^2 * c * T_H / 3 = 2*pi^2*c / (3*(1+rho_n))

    The Cardy formula (matching CFT counting):
        S_Cardy = (pi^2/3) * c * T   (high-T)
    """
    rho_n = zeta_zero(n)
    tau_n = modular_parameter_from_zeta_zero(n)

    beta_n = (1.0 + rho_n) / 2.0
    T_H_n = 1.0 / beta_n

    # Bekenstein-Hawking / Cardy entropy
    # S = pi^2 * c * T / 3 = pi^2 * c / (3 * beta)
    S_BH = PI ** 2 * c / (3.0 * beta_n)

    # Nome
    q_n = nome_from_zeta_zero(n)

    # Tachyon mass at c=26: m^2 = -1/alpha' = -4 in conventions where alpha'=1/2
    # The tachyon vertex operator has dimension h = alpha' m^2 / 4 + 1 = 0
    # at the mass shell.  At the BTZ temperature T_H:
    # The thermal mass correction: m_eff^2 = m^2 + pi^2 * T_H^2 * (c-2)/6
    # For c=26: m_eff^2 = -4 + pi^2 * T_H^2 * 4 = -4 + 4*pi^2/(beta^2)
    alpha_prime = 0.5  # alpha' = 1/2 convention
    m_sq_tachyon = -4.0  # in alpha' = 1/2 units
    if c == 26.0:
        thermal_mass_sq = m_sq_tachyon + 4.0 * PI ** 2 / (beta_n ** 2)
        hagedorn_beta = PI * math.sqrt(2.0 * alpha_prime * (c - 2.0))
        tachyon_condensed = (beta_n < hagedorn_beta)
    else:
        thermal_mass_sq = None
        hagedorn_beta = None
        tachyon_condensed = None

    # One-loop correction: S_1 = -(3/2) * log(S_BH/(2*pi))
    if S_BH > 0:
        S_1_loop = -1.5 * math.log(S_BH / TWO_PI)
    else:
        S_1_loop = 0.0

    return {
        'n': n,
        'rho_n': rho_n,
        'tau_n': tau_n,
        'beta_n': beta_n,
        'T_H': T_H_n,
        'S_BH': S_BH,
        'S_1_loop': S_1_loop,
        'q_n': q_n,
        'abs_q': abs(q_n),
        'c': c,
        'thermal_mass_sq': thermal_mass_sq,
        'hagedorn_beta': hagedorn_beta,
        'tachyon_condensed': tachyon_condensed,
    }


def cardy_entropy(c: float, Delta: float) -> float:
    r"""Cardy formula: S = 2*pi*sqrt(c*Delta/6).

    This is the asymptotic (high-energy) entropy for a 2d CFT of central
    charge c at conformal dimension Delta >> c/24.
    """
    if c * Delta <= 0:
        return 0.0
    return 2.0 * PI * math.sqrt(c * Delta / 6.0)


def cardy_matches_btz(c: float, beta: float, tol: float = 1e-10) -> bool:
    r"""Verify that Cardy entropy matches BTZ entropy at inverse temperature beta.

    The BTZ entropy S_BH = pi^2*c/(3*beta).
    The Cardy entropy at energy E = pi^2*c/(6*beta^2) is
        S_Cardy = 2*pi*sqrt(c*E/6) = 2*pi*sqrt(c * pi^2*c/(36*beta^2))
                = pi^2*c / (3*beta).

    In the canonical ensemble at temperature T = 1/beta:
        E = (pi^2 / 6) * c * T^2 = (pi^2 * c) / (6 * beta^2)
        S = beta * E + log Z ~ (pi^2 / 3) * c * T = (pi^2 * c) / (3 * beta)

    The Cardy formula in the microcanonical ensemble:
        S(E) = 2*pi*sqrt(c*E/6) = 2*pi*sqrt(c * (pi^2*c)/(36*beta^2))
             = 2*pi * pi*sqrt(c^2/(36)) / beta
             = 2*pi^2*c / (6*beta)
             = pi^2*c / (3*beta)
    """
    S_btz = PI ** 2 * c / (3.0 * beta)
    E = PI ** 2 * c / (6.0 * beta ** 2)
    S_cardy = cardy_entropy(c, E)
    return abs(S_btz - S_cardy) < tol * max(abs(S_btz), 1.0)


# ===========================================================================
# Section 10: Anomaly polynomial
# ===========================================================================

def anomaly_polynomial_I4(c: float, p1: float = 1.0) -> float:
    r"""Gravitational anomaly 4-form I_4 for a 2d CFT.

    I_4 = (c/24) * p_1(R)

    where p_1(R) = -(1/(8*pi^2)) * Tr(R^2) is the first Pontryagin class.
    This is the gravitational anomaly that obstructs coupling to curved
    backgrounds.

    At c=26: I_4 = 26/24 * p_1 = 13/12 * p_1.
    At c=0: I_4 = 0 (no gravitational anomaly for topological theory).

    Parameters
    ----------
    c : central charge
    p1 : value of p_1(R) (set to 1 for the coefficient)
    """
    return c * p1 / 24.0


def anomaly_polynomial_I8(c: float, p1: float = 1.0,
                           p2: float = 0.0) -> float:
    r"""Anomaly 8-form I_8 for the scalar comparison system.

    For a 6d (2,0) SCFT (relevant for M5-branes), the anomaly polynomial is:
        I_8 = (1/48) * [p_2(R) - (1/4)*(p_1(R))^2 + (1/4)*p_1(R)*p_1(N)]

    For the HT (holomorphic-topological) system at central charge c:
    the coefficient of p_2 is determined by the a-anomaly, and p_1^2
    by the c-anomaly.  In 2d, I_8 reduces to products of I_4 by factorization.

    In the zeta-zero scan the curvature parameter is scaled by rho_n.
    That scan has no established physical meaning.

    Parameters
    ----------
    c : central charge (determines the anomaly coefficients)
    p1 : first Pontryagin class value
    p2 : second Pontryagin class value
    """
    # For the 2d scalar comparison, I_8 factorizes as products of 4-forms
    # I_8 = c_1 * p_2 + c_2 * p_1^2
    # where c_1 = c^2/576, c_2 = -c^2/2304 (from squaring I_4)
    c1_coeff = c ** 2 / 576.0
    c2_coeff = -c ** 2 / 2304.0
    return c1_coeff * p2 + c2_coeff * p1 ** 2


def anomaly_at_zeta_zero(n: int, c: float = 26.0) -> Dict[str, float]:
    r"""Anomaly polynomial evaluated with rho_n-scaled curvature.

    This sets p_1 = rho_n * omega as a formal numerical probe.
    """
    rho_n = zeta_zero(n)
    I4 = anomaly_polynomial_I4(c, p1=rho_n)
    I8 = anomaly_polynomial_I8(c, p1=rho_n, p2=rho_n ** 2)
    return {
        'n': n,
        'rho_n': rho_n,
        'I4': I4,
        'I8': I8,
        'c': c,
    }


# ===========================================================================
# Section 11: 3D holomorphic Chern-Simons
# ===========================================================================

def cs_partition_solid_torus(k: int, rank: int = 1,
                              tau: Optional[complex] = None) -> complex:
    r"""Chern-Simons partition function on the solid torus S^1 x D^2.

    For U(1) CS at level k (integer):
        Z_{CS}(S^1 x D^2; k) = 1/sqrt(k)

    For SU(2) CS at level k:
        Z_{CS}(S^1 x D^2; k) = sqrt(2/(k+2)) * sin(pi/(k+2))

    For general SU(N) at level k, the partition function on the solid torus
    (with trivial boundary condition = vacuum representation) is:

        Z = (vol(G) / (k+h^v)^{dim(G)/2}) * prod_{alpha > 0}
            2*sin(pi*<alpha, rho>/(k+h^v))

    For U(1): this simplifies to 1/sqrt(k).

    Parameters
    ----------
    k : Chern-Simons level (must be positive integer for well-defined theory)
    rank : 1 for U(1), 2 for SU(2), etc.
    tau : optional modular parameter (for the solid torus with complex structure)
    """
    if k <= 0:
        raise ValueError(f"CS level must be positive integer, got k={k}")

    if rank == 1:
        # U(1) at level k
        Z = 1.0 / math.sqrt(float(k))
    elif rank == 2:
        # SU(2) at level k: Z = sqrt(2/(k+2)) * sin(pi/(k+2))
        kp = float(k) + 2.0
        Z = math.sqrt(2.0 / kp) * math.sin(PI / kp)
    else:
        # General rank: use the Weyl volume formula
        # Z ~ k^{-dim(G)/2} * (volume factor)
        # For SU(N): dim = N^2-1, h^v = N
        N = rank
        dim_g = N ** 2 - 1
        h_dual = N
        kp = float(k) + h_dual
        Z = kp ** (-dim_g / 2.0)
        # Weyl denominator product (simplified)
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                Z *= 2.0 * math.sin(PI * (j - i) / kp)
    return complex(Z, 0.0)


def cs_at_zeta_zero(n: int, rank: int = 2) -> Dict[str, Any]:
    r"""CS partition function at level k_n derived from zeta zero.

    Formal probe: k_n = round((1+rho_n)/2).
    CS level must be a positive integer, so we round to the nearest integer.

    For rho_1 ~ 14.13: k_1 ~ round(7.57) = 8.
    For rho_2 ~ 21.02: k_2 ~ round(11.01) = 11.
    """
    rho_n = zeta_zero(n)
    k_float = (1.0 + rho_n) / 2.0
    k_int = max(1, round(k_float))

    Z = cs_partition_solid_torus(k_int, rank)

    return {
        'n': n,
        'rho_n': rho_n,
        'k_float': k_float,
        'k_int': k_int,
        'rank': rank,
        'Z_CS': Z,
        'abs_Z': abs(Z),
    }


# ===========================================================================
# Section 12: Open/closed duality at zeta-zero parameters
# ===========================================================================

def annulus_trace_genus1(kappa_val) -> Fraction:
    r"""Annulus trace at genus 1: Tr_A = kappa * lambda_1 = kappa/24.

    PROVED (thm:annulus-trace): the annulus trace Tr_A in HH_*(A)
    at genus 1 is kappa(A) * lambda_1^FP.

    This is the first modular shadow of the open sector.  It is not the
    derived center C = Z_ch^der(A).
    """
    return Fraction(kappa_val) * lambda_fp(1)


def derived_center_dimension(algebra: str = 'heisenberg',
                              weight_max: int = 4) -> Dict[int, int]:
    r"""Dimensions of the chiral derived center Z^der_ch(A) by weight.

    The derived center (Hochschild cohomology of A) has:
        H^0 = center Z(A)
        H^1 = outer derivations
        H^2 = first-order deformations

    For Heisenberg at weight w:
        dim H^0(w) = 1 for all w >= 0 (generated by 1, J, J^2, ...)
        dim H^1(w) = 1 for w >= 1 (derivation J_{-w})
        dim H^2(w) = 0 for w <= 1; dim H^2(2) = 1 (the level deformation)

    For Virasoro at weight w:
        dim H^0(w) = p(w) (partitions, Verma module)
        dim H^1(0) = 0, dim H^1(2) = 1 (the T-derivation)
        dim H^2(0) = 1 (the central extension c)

    These are SIMPLIFIED (weight-truncated) computations.
    The full derived center requires the entire chiral Hochschild complex.
    """
    dims: Dict[int, int] = {}
    if algebra == 'heisenberg':
        for w in range(weight_max + 1):
            dims[w] = 1  # H^0 only, simplified
    elif algebra == 'virasoro':
        # Partition function of Verma module (H^0 contribution)
        for w in range(weight_max + 1):
            dims[w] = _partition_count(w)
    else:
        for w in range(weight_max + 1):
            dims[w] = 1
    return dims


def _partition_count(n: int) -> int:
    """Integer partition count p(n)."""
    if n < 0:
        return 0
    if n <= 1:
        return 1
    # Dynamic programming
    p = [0] * (n + 1)
    p[0] = 1
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            p[j] += p[j - k]
    return p[n]


def open_closed_at_zeta_zero(n: int, c: float = 26.0) -> Dict[str, Any]:
    r"""Open/closed data at zeta-zero parameters.

    Returns the annulus trace, boundary partition function, complementarity
    data (c vs 26-c), and typed seven-entry package data.
    """
    rho_n = zeta_zero(n)
    tau_n = modular_parameter_from_zeta_zero(n)

    kappa_A = kappa_virasoro(Fraction(c))
    kappa_A_dual = kappa_virasoro(Fraction(26) - Fraction(c))

    annulus = annulus_trace_genus1(kappa_A)
    annulus_dual = annulus_trace_genus1(kappa_A_dual)

    # For Virasoro: kappa + kappa' = c/2 + (26-c)/2 = 13
    kappa_sum = kappa_A + kappa_A_dual

    Z_boundary = boundary_partition_virasoro(tau_n, c=c)
    Z_boundary_dual = boundary_partition_virasoro(tau_n, c=26.0 - c)
    seven_entry = seven_entry_package_at_zeta_zero(n, c=c)
    firewall = typed_object_firewall(c=c)

    return {
        'n': n,
        'rho_n': rho_n,
        'tau_n': tau_n,
        'c': c,
        'c_dual': 26.0 - c,
        'kappa': float(kappa_A),
        'kappa_dual': float(kappa_A_dual),
        'kappa_sum': float(kappa_sum),
        'kappa_sum_exact': kappa_sum,
        'annulus_trace': float(annulus),
        'annulus_trace_dual': float(annulus_dual),
        'Z_boundary': Z_boundary,
        'Z_boundary_dual': Z_boundary_dual,
        'abs_Z_boundary': abs(Z_boundary),
        'abs_Z_boundary_dual': abs(Z_boundary_dual),
        'seven_entry_package': seven_entry,
        'typed_firewall': firewall,
        'A': seven_entry['A'],
        'A^i': seven_entry['A^i'],
        'A^!': seven_entry['A^!'],
        'C': seven_entry['C'],
    }


# ===========================================================================
# Section 13: Complementarity and scalar typed dictionary
# ===========================================================================

def complementarity_check(c: float) -> Dict[str, Any]:
    r"""Complementarity data for the Koszul pair (Vir_c, Vir_{26-c}).

    kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    NOT zero (except at c=13 where kappa = kappa' = 13/2).

    delta_kappa = kappa - kappa' = c/2 - (26-c)/2 = c - 13.
    kappa_eff = kappa(matter) + kappa(ghost) = c/2 - 13 = (c-26)/2.

    At c=13: delta_kappa = 0 (self-dual point).
    At c=26: kappa_eff = 0 (anomaly cancellation, critical string).
    These are different conditions at different central charges.
    """
    kappa_A = kappa_virasoro(Fraction(c))
    kappa_A_dual = kappa_virasoro(Fraction(26) - Fraction(c))

    return {
        'c': c,
        'c_dual': 26.0 - float(c),
        'kappa': float(kappa_A),
        'kappa_dual': float(kappa_A_dual),
        'kappa_sum': float(kappa_A + kappa_A_dual),
        'delta_kappa': float(kappa_A - kappa_A_dual),
        'kappa_eff': float(kappa_eff(kappa_A)),
        'is_self_dual': (c == 13),
        'is_critical': (c == 26),
        'complementarity_holds': (kappa_A + kappa_A_dual == Fraction(13)),
    }


def holographic_dictionary_entry(c: float, n: int) -> Dict[str, Any]:
    r"""Full scalar/typed dictionary entry at zeta zero n for central charge c.

    Compiles:
      - Boundary: Z_partial, kappa, annulus trace
      - Bulk: shadow F_g, kappa_eff, BTZ data
      - Complementarity: c vs 26-c
      - Celestial: soft factor at Delta_n
      - CS: partition function at k_n
      - Anomaly: I_4, I_8
    """
    boundary = open_closed_at_zeta_zero(n, c)
    bulk = bulk_shadow_table(c)
    btz = btz_at_zeta_zero(n, c)
    celestial = celestial_at_zeta_zero(n)
    cs = cs_at_zeta_zero(n)
    anomaly = anomaly_at_zeta_zero(n, c)
    comp = complementarity_check(c)
    seven_entry = seven_entry_package_at_zeta_zero(n, c=c)
    firewall = typed_object_firewall(c=c)

    return {
        'boundary': boundary,
        'bulk': bulk,
        'btz': btz,
        'celestial': celestial,
        'cs': cs,
        'anomaly': anomaly,
        'complementarity': comp,
        'seven_entry_package': seven_entry,
        'typed_firewall': firewall,
    }


# ===========================================================================
# Section 14: Shadow partition function at zeta-zero temperature
# ===========================================================================

def shadow_partition_at_zeta_zero(n: int, c: float = 26.0,
                                   g_max: int = 5,
                                   use_effective: bool = False) -> Dict[str, Any]:
    r"""Shadow partition function Z^sh evaluated at zeta-zero BTZ temperature.

    Z^sh = exp(sum_{g=1}^{g_max} hbar^{2g} F_g)

    where hbar = 2*pi / S_BH (inverse Bekenstein-Hawking entropy).

    Parameters
    ----------
    n : zeta zero index
    c : central charge
    g_max : maximum genus in the shadow expansion
    use_effective : if True, use kappa_eff instead of kappa(A)
    """
    btz = btz_at_zeta_zero(n, c)
    S_BH = btz['S_BH']

    if S_BH <= 0:
        return {'error': 'S_BH <= 0', 'n': n, 'c': c}

    hbar = TWO_PI / S_BH

    if use_effective:
        kappa_val = kappa_eff(kappa_virasoro(Fraction(c)))
    else:
        kappa_val = kappa_virasoro(Fraction(c))

    F_table = {}
    exponent = 0.0
    for g in range(1, g_max + 1):
        Fg = float(Fraction(kappa_val) * lambda_fp(g))
        F_table[g] = Fg
        exponent += hbar ** (2 * g) * Fg

    Z_sh = math.exp(exponent)

    return {
        'n': n,
        'c': c,
        'rho_n': btz['rho_n'],
        'S_BH': S_BH,
        'hbar': hbar,
        'kappa': float(kappa_val),
        'F_g': F_table,
        'exponent': exponent,
        'Z_sh': Z_sh,
        'g_max': g_max,
    }


# ===========================================================================
# Section 15: Summary and cross-verification
# ===========================================================================

def cardy_btz_consistency(c: float, n_zeros: int = 10) -> List[Dict[str, Any]]:
    r"""Verify Cardy-BTZ consistency at each zeta-zero parameter.

    At each temperature T_n = 2/(1+rho_n):
      - S_BH = pi^2*c/(3*beta_n) from the BTZ geometry
      - S_Cardy = 2*pi*sqrt(c*E_n/6) from the Cardy formula with E_n = pi^2*c/(6*beta_n^2)
      - These must agree (proved identity, not numerological)

    This is a MATHEMATICAL CONSISTENCY CHECK of the formulas, not a
    physical prediction about zeta zeros.
    """
    results = []
    for n in range(1, n_zeros + 1):
        btz = btz_at_zeta_zero(n, c)
        beta = btz['beta_n']
        S_BH = btz['S_BH']

        E_n = PI ** 2 * c / (6.0 * beta ** 2)
        S_Cardy = cardy_entropy(c, E_n)

        match = abs(S_BH - S_Cardy) < 1e-10 * max(abs(S_BH), 1.0)

        results.append({
            'n': n,
            'rho_n': btz['rho_n'],
            'beta': beta,
            'S_BH': S_BH,
            'S_Cardy': S_Cardy,
            'match': match,
            'relative_error': abs(S_BH - S_Cardy) / max(abs(S_BH), 1e-300),
        })
    return results


def tachyon_mass_at_zeta_zeros(n_max: int = 10) -> List[Dict[str, Any]]:
    r"""Tachyon effective mass at zeta-zero BTZ temperatures (c=26 only).

    The bosonic string tachyon has m^2 = -4/alpha' = -4 (alpha'=1/2).
    The thermal mass shift: m_eff^2 = m^2 + (4*pi^2/beta^2).

    The Hagedorn temperature: beta_H = pi*sqrt(2*alpha'*(c-2)) = pi*sqrt(24) ~ 15.4.
    For beta < beta_H: tachyon condensation occurs (m_eff^2 > 0 not sufficient
    to prevent instability; the Hagedorn temperature is the real criterion).
    """
    results = []
    alpha_prime = 0.5
    m_sq = -4.0  # m^2 = -4/alpha' with alpha'=1/2 gives m^2 = -4 in these units
    hagedorn_beta = PI * math.sqrt(2.0 * alpha_prime * 24.0)  # c-2 = 24 for c=26

    for n in range(1, n_max + 1):
        btz = btz_at_zeta_zero(n, c=26.0)
        beta = btz['beta_n']
        m_eff_sq = m_sq + 4.0 * PI ** 2 / (beta ** 2)

        results.append({
            'n': n,
            'rho_n': btz['rho_n'],
            'beta': beta,
            'hagedorn_beta': hagedorn_beta,
            'm_sq_bare': m_sq,
            'm_eff_sq': m_eff_sq,
            'tachyonic': (m_eff_sq < 0),
            'below_hagedorn': (beta < hagedorn_beta),
        })
    return results


def full_holographic_scan(c: float = 26.0, n_max: int = 10,
                           g_max: int = 5) -> Dict[str, Any]:
    r"""Full scan of scalar typed data at zeta-zero parameters.

    Returns a comprehensive dictionary with all computations.

    The zeta-zero evaluations are formal probes.  The
    mathematically rigorous content is the formulas themselves (partition
    functions, Cardy, BTZ, shadows, CS), not their evaluation at
    zeta-zero parameters.
    """
    boundary_table = boundary_Z_table(c, n_max)
    shadow_table = {
        n: shadow_partition_at_zeta_zero(n, c, g_max)
        for n in range(1, n_max + 1)
    }
    btz_table = {n: btz_at_zeta_zero(n, c) for n in range(1, n_max + 1)}
    cs_table = {n: cs_at_zeta_zero(n) for n in range(1, n_max + 1)}
    consistency = cardy_btz_consistency(c, n_max)
    comp = complementarity_check(c)
    seven_entry = seven_entry_package_at_zeta_zero(1, c=c)
    firewall = typed_object_firewall(c=c)

    return {
        'c': c,
        'n_max': n_max,
        'g_max': g_max,
        'boundary': boundary_table,
        'shadow': shadow_table,
        'btz': btz_table,
        'cs': cs_table,
        'cardy_consistency': consistency,
        'complementarity': comp,
        'seven_entry_package': seven_entry,
        'typed_firewall': firewall,
    }
