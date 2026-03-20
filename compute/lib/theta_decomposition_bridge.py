#!/usr/bin/env python3
r"""
theta_decomposition_bridge.py — Non-lattice bridge via theta function decomposition.

THE KEY IDEA: Minimal model characters are built from Jacobi theta functions,
which are themselves lattice objects. The Ising model (M(4,3), c=1/2) characters
decompose as:

  chi_0(q)     = (sqrt(theta_3/eta) + sqrt(theta_4/eta)) / 2    [h=0, identity]
  chi_{1/2}(q) = (sqrt(theta_3/eta) - sqrt(theta_4/eta)) / 2    [h=1/2, fermion]
  chi_{1/16}(q)= sqrt(theta_2 / (2*eta))                        [h=1/16, twist]

These theta functions are lattice theta functions for Z with different
characteristics. So the Ising characters, despite being "non-lattice", are
built from LATTICE objects.

If |chi_i|^2 decomposes as a linear combination of Epstein zeta integrands
from auxiliary lattices, then the lattice bridge applies to each term
separately, and the shadow-spectral correspondence extends by linearity.

GENERAL MINIMAL MODELS M(p,q): Characters via Rocha-Caridi formula involve
theta functions Theta_{r,s}(tau) at level 2pq:
  Theta_{r,s}(tau) = sum_{n in Z} q^{(2pqn + ps - qr)^2 / (4pq)}

These correspond to the lattice Z/sqrt(2pq) with shifted characteristic.
The associated Epstein zeta is a Dirichlet L-function with character
defined by the residue class ps - qr mod 2pq.

ARCHITECTURE:
  1. Theta functions (theta_2, theta_3, theta_4, eta)
  2. Ising character decomposition and verification
  3. |chi|^2 decomposition into theta products
  4. Jacobi identity simplification of Z_Ising
  5. Mellin transforms / Epstein zeta from theta
  6. Cross-term analysis
  7. General M(p,q) theta decomposition
  8. Auxiliary lattice identification
"""

import numpy as np
import math
from fractions import Fraction

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Jacobi theta functions and Dedekind eta
# ============================================================

def theta_2(tau, nmax=500):
    r"""theta_2(tau) = 2 sum_{n=0}^{inf} q^{(n+1/2)^2/2}, q = exp(2 pi i tau).

    Convention: theta_2(tau) = sum_{n in Z} q^{(n+1/2)^2/2}.
    """
    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    result = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        exp_val = (n + mpmath.mpf('0.5')) ** 2 / 2
        result += q ** exp_val
    return result


def theta_3(tau, nmax=500):
    r"""theta_3(tau) = sum_{n in Z} q^{n^2/2}, q = exp(2 pi i tau)."""
    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    result = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        result += q ** (mpmath.mpf(n) ** 2 / 2)
    return result


def theta_4(tau, nmax=500):
    r"""theta_4(tau) = sum_{n in Z} (-1)^n q^{n^2/2}, q = exp(2 pi i tau)."""
    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    result = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        result += (-1) ** n * q ** (mpmath.mpf(n) ** 2 / 2)
    return result


def dedekind_eta(tau, nmax=500):
    r"""eta(tau) = q^{1/24} prod_{n=1}^{inf} (1 - q^n), q = exp(2 pi i tau)."""
    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    result = q ** (mpmath.mpf(1) / 24)
    for n in range(1, nmax + 1):
        result *= (1 - q ** n)
    return result


def theta_2_mpmath(tau, nmax=500):
    """Wrapper returning mpmath complex."""
    return theta_2(tau, nmax)


def theta_3_mpmath(tau, nmax=500):
    """Wrapper returning mpmath complex."""
    return theta_3(tau, nmax)


def theta_4_mpmath(tau, nmax=500):
    """Wrapper returning mpmath complex."""
    return theta_4(tau, nmax)


# ============================================================
# 2. Ising model characters — direct q-series
# ============================================================

def ising_character_qseries(h, tau, nmax=300):
    r"""Compute Ising model character chi_h(q) via direct q-series.

    For M(4,3) with c = 1/2:
      chi_0 = q^{-1/48} (1 + q^2 + q^3 + 2q^4 + 2q^5 + 3q^6 + ...)
      chi_{1/2} = q^{23/48} (1 + q + q^2 + q^3 + 2q^4 + 2q^5 + 3q^6 + ...)
      chi_{1/16} = q^{1/24} (1 + q + q^2 + 2q^3 + 2q^4 + 3q^5 + 4q^6 + ...)

    Uses the Rocha-Caridi formula for M(4,3):
      chi_{r,s}(q) = (1/eta(q)) * sum_{n in Z} (q^{a_+(n)} - q^{a_-(n)})
    where a_pm(n) = (24n +/- (4s - 3r))^2 / 48.

    Primary fields: (1,1) -> h=0, (1,2) -> h=1/2, (2,1) -> h=1/16.
    """
    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    eta = dedekind_eta(tau, nmax)

    p, pp = 4, 3  # M(4,3)

    if abs(h) < 1e-10:
        r, s = 1, 1
    elif abs(h - 0.5) < 1e-10:
        r, s = 1, 2
    elif abs(h - 1.0 / 16) < 1e-10:
        r, s = 2, 1
    else:
        raise ValueError(f"Unknown Ising primary h={h}")

    # Rocha-Caridi for M(p, p') with p=4, p'=3:
    # chi_{r,s} = (Theta_{m+, pq} - Theta_{m-, pq}) / eta
    # where m+ = ps - qr, m- = ps + qr, and k = pq = 12.
    # Theta_{m, k}(tau) = sum_{n in Z} q^{(2kn + m)^2 / (4k)}
    # So: a_+(n) = (24n + (ps-qr))^2/48, a_-(n) = (24n + (ps+qr))^2/48
    shift_plus = p * s - pp * r    # ps - qr
    shift_minus = p * s + pp * r   # ps + qr

    result = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        a_plus = mpmath.mpf(2 * p * pp * n + shift_plus) ** 2 / (4 * p * pp)
        a_minus = mpmath.mpf(2 * p * pp * n + shift_minus) ** 2 / (4 * p * pp)
        result += q ** a_plus - q ** a_minus
    result /= eta
    return result


def ising_character_theta(h, tau, nmax=500):
    r"""Compute Ising character via theta decomposition.

    chi_0     = (sqrt(theta_3/eta) + sqrt(theta_4/eta)) / 2
    chi_{1/2} = (sqrt(theta_3/eta) - sqrt(theta_4/eta)) / 2
    chi_{1/16} = sqrt(theta_2 / (2*eta))
    """
    t3 = theta_3(tau, nmax)
    t4 = theta_4(tau, nmax)
    t2 = theta_2(tau, nmax)
    eta = dedekind_eta(tau, nmax)

    sq3 = mpmath.sqrt(t3 / eta)
    sq4 = mpmath.sqrt(t4 / eta)

    if abs(h) < 1e-10:
        return (sq3 + sq4) / 2
    elif abs(h - 0.5) < 1e-10:
        return (sq3 - sq4) / 2
    elif abs(h - 1.0 / 16) < 1e-10:
        return mpmath.sqrt(t2 / (2 * eta))
    else:
        raise ValueError(f"Unknown h={h}")


# ============================================================
# 3. |chi|^2 decomposition
# ============================================================

def chi_squared_decomposition(h, y, nmax=500):
    r"""Compute |chi_h(iy)|^2 and its theta decomposition.

    On the imaginary axis tau = iy, all theta functions are real and positive.

    Returns dict with:
      'chi_sq': |chi_h|^2 from q-series
      'chi_sq_theta': |chi_h|^2 from theta decomposition
      'theta_terms': constituent terms
    """
    tau = mpmath.mpc(0, y)

    # Theta values (real on imaginary axis)
    t2 = theta_2(tau, nmax)
    t3 = theta_3(tau, nmax)
    t4 = theta_4(tau, nmax)
    eta_val = dedekind_eta(tau, nmax)

    # On imaginary axis, all are real
    t2r = mpmath.re(t2)
    t3r = mpmath.re(t3)
    t4r = mpmath.re(t4)
    eta_r = mpmath.re(eta_val)

    # |chi|^2 from theta
    if abs(h) < 1e-10:
        # |chi_0|^2 = (sqrt(t3/eta) + sqrt(t4/eta))^2 / 4
        sq3 = mpmath.sqrt(t3r / eta_r)
        sq4 = mpmath.sqrt(t4r / eta_r)
        chi_sq_theta = (sq3 + sq4) ** 2 / 4
        terms = {
            'theta3_over_eta': t3r / eta_r,
            'theta4_over_eta': t4r / eta_r,
            'cross': mpmath.sqrt(t3r * t4r) / eta_r,
        }
    elif abs(h - 0.5) < 1e-10:
        sq3 = mpmath.sqrt(t3r / eta_r)
        sq4 = mpmath.sqrt(t4r / eta_r)
        chi_sq_theta = (sq3 - sq4) ** 2 / 4
        terms = {
            'theta3_over_eta': t3r / eta_r,
            'theta4_over_eta': t4r / eta_r,
            'cross': -mpmath.sqrt(t3r * t4r) / eta_r,
        }
    elif abs(h - 1.0 / 16) < 1e-10:
        chi_sq_theta = t2r / (2 * eta_r)
        terms = {'theta2_over_2eta': t2r / (2 * eta_r)}
    else:
        raise ValueError(f"Unknown h={h}")

    # |chi|^2 from q-series
    chi_qs = ising_character_qseries(h, tau, min(nmax, 300))
    chi_sq_qs = mpmath.re(chi_qs) ** 2  # Real on imaginary axis

    return {
        'chi_sq': float(chi_sq_qs),
        'chi_sq_theta': float(chi_sq_theta),
        'theta_terms': {k: float(v) for k, v in terms.items()},
    }


def ising_partition_function(y, nmax=500):
    r"""Compute Z_Ising = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2 at tau=iy.

    Also compute the theta-function decomposition and Jacobi simplification.

    KEY IDENTITY: |chi_0|^2 + |chi_{1/2}|^2
      = (1/4)(sqrt(t3/eta)+sqrt(t4/eta))^2 + (1/4)(sqrt(t3/eta)-sqrt(t4/eta))^2
      = (1/2)(t3/eta + t4/eta)

    So Z_Ising = (1/2)(t3 + t4)/eta + t2/(2*eta) = (t2 + t3 + t4)/(2*eta)

    On the imaginary axis, all are real.
    """
    tau = mpmath.mpc(0, y)

    t2 = mpmath.re(theta_2(tau, nmax))
    t3 = mpmath.re(theta_3(tau, nmax))
    t4 = mpmath.re(theta_4(tau, nmax))
    eta_val = mpmath.re(dedekind_eta(tau, nmax))

    # Individual |chi|^2
    sq3 = mpmath.sqrt(t3 / eta_val)
    sq4 = mpmath.sqrt(t4 / eta_val)

    chi0_sq = float((sq3 + sq4) ** 2 / 4)
    chi12_sq = float((sq3 - sq4) ** 2 / 4)
    chi116_sq = float(t2 / (2 * eta_val))

    Z_direct = chi0_sq + chi12_sq + chi116_sq

    # Simplified form: cross terms cancel
    # |chi_0|^2 + |chi_{1/2}|^2 = (t3 + t4)/(2*eta)
    sum_01 = float((t3 + t4) / (2 * eta_val))

    # Full Z = (t2 + t3 + t4)/(2*eta)
    Z_simplified = float((t2 + t3 + t4) / (2 * eta_val))

    return {
        'chi0_sq': chi0_sq,
        'chi12_sq': chi12_sq,
        'chi116_sq': chi116_sq,
        'Z_direct': Z_direct,
        'Z_simplified': Z_simplified,
        'cross_term_cancellation': abs(sum_01 - chi0_sq - chi12_sq) < 1e-10,
        'theta2': float(t2),
        'theta3': float(t3),
        'theta4': float(t4),
        'eta': float(eta_val),
    }


# ============================================================
# 4. Jacobi identity verification
# ============================================================

def jacobi_abstruse_identity(y, nmax=500):
    r"""Verify the Jacobi abstruse identity: theta_3^4 = theta_2^4 + theta_4^4.

    This is the key identity for simplifying Z_Ising.
    Also check: theta_2*theta_3*theta_4 = 2*eta^3 (Jacobi triple product).
    """
    tau = mpmath.mpc(0, y)

    t2 = theta_2(tau, nmax)
    t3 = theta_3(tau, nmax)
    t4 = theta_4(tau, nmax)
    eta_val = dedekind_eta(tau, nmax)

    # theta_3^4 = theta_2^4 + theta_4^4
    lhs = mpmath.re(t3 ** 4)
    rhs = mpmath.re(t2 ** 4 + t4 ** 4)
    abstruse_error = float(abs(lhs - rhs))

    # theta_2 * theta_3 * theta_4 = 2*eta^3
    product = mpmath.re(t2 * t3 * t4)
    eta_cube = mpmath.re(2 * eta_val ** 3)
    triple_error = float(abs(product - eta_cube))

    return {
        'abstruse_lhs': float(lhs),
        'abstruse_rhs': float(rhs),
        'abstruse_error': abstruse_error,
        'triple_product_lhs': float(product),
        'triple_product_rhs': float(eta_cube),
        'triple_error': triple_error,
    }


# ============================================================
# 5. Lattice Epstein zeta from theta functions
# ============================================================

def theta_mellin_epstein(j, s, nmax=500, ymin=0.01, ymax=50.0, npts=2000):
    r"""Compute the Mellin transform of |theta_j|^2 restricted to imaginary axis.

    For theta_3(iy) = sum_n exp(-pi*y*n^2):
      integral_0^inf theta_3(iy)^2 * y^{s-1} dy
    is related to the Epstein zeta E_{Z^2}(s).

    More precisely, for the LATTICE theta function:
      Theta_Z(tau) = theta_3(tau) = sum_{n in Z} q^{n^2/2}

    The Epstein zeta of Z is:
      E_Z(s) = sum_{n != 0} |n|^{-2s} = 2*zeta(2s)

    For Z^2 (by Rankin-Selberg unfolding of |theta_3|^2):
      E_{Z^2}(s) = 4*zeta(s)*L(s, chi_{-4})

    We compute numerically by direct summation of the Dirichlet series.
    """
    if j == 2:
        # theta_2: q^{(n+1/2)^2/2}, lattice Z + 1/2
        # Epstein: sum_{n in Z} |n+1/2|^{-2s} = 2*(2^{2s}-1)*zeta(2s)
        # = 2*sum_{n>=0} (n+1/2)^{-2s}
        # = 2*((2^{2s}-1)/(2^{2s}))*2*zeta(2s) ... let's compute directly
        result = mpmath.mpf(0)
        for n in range(0, nmax):
            result += 2 * mpmath.mpf(n + mpmath.mpf('0.5')) ** (-2 * s)
        return float(result)
    elif j == 3:
        # theta_3: q^{n^2/2}, lattice Z
        # E_Z(s) = 2*zeta(2s)
        return float(2 * mpmath.zeta(2 * s))
    elif j == 4:
        # theta_4: (-1)^n * q^{n^2/2}, NOT a standard lattice theta
        # |theta_4|^2 at tau=iy is real: (sum (-1)^n e^{-pi*y*n^2})^2
        # This factors through the TWISTED lattice: sum over Z with (-1)^n weight
        # Mellin gives 2*(1-2^{1-2s})*zeta(2s) = 2*eta_D(2s) where eta_D = Dirichlet eta
        # = 2*(1-2^{1-2s})*zeta(2s)
        return float(2 * (1 - mpmath.power(2, 1 - 2 * s)) * mpmath.zeta(2 * s))
    else:
        raise ValueError(f"j must be 2, 3, or 4, got {j}")


def epstein_z_squared(s, nmax=1000):
    r"""Epstein zeta E_{Z^2}(s) = sum_{(m,n)!=(0,0)} (m^2+n^2)^{-s}.

    This equals 4*zeta(s)*L(s, chi_{-4}) where chi_{-4} = Kronecker symbol (-4/n).
    chi_{-4}(n) = 0 if n even, 1 if n=1 mod 4, -1 if n=3 mod 4.
    """
    # Direct: 4*zeta(s)*L(s, chi_{-4})
    zeta_s = mpmath.zeta(s)

    # L(s, chi_{-4}) = sum_{n=1}^inf chi_{-4}(n) / n^s
    # = 1 - 1/3^s + 1/5^s - 1/7^s + ...
    L_val = mpmath.mpf(0)
    for n in range(1, nmax + 1):
        if n % 2 == 0:
            continue
        chi = 1 if n % 4 == 1 else -1
        L_val += mpmath.mpf(chi) / mpmath.power(n, s)

    return float(4 * zeta_s * L_val)


def epstein_z_squared_direct(s, nmax=100):
    r"""Direct lattice sum for E_{Z^2}(s) = sum_{(m,n)!=(0,0)} (m^2+n^2)^{-s}."""
    result = mpmath.mpf(0)
    for m in range(-nmax, nmax + 1):
        for n in range(-nmax, nmax + 1):
            if m == 0 and n == 0:
                continue
            result += mpmath.mpf(m ** 2 + n ** 2) ** (-s)
    return float(result)


def dirichlet_L_chi4(s, nmax=2000):
    r"""L(s, chi_{-4}) = sum_{n odd} chi_{-4}(n) / n^s.

    chi_{-4}(1)=1, chi_{-4}(3)=-1, chi_{-4}(5)=1, chi_{-4}(7)=-1, ...
    Also known as the Dirichlet beta function beta(s).
    """
    result = mpmath.mpf(0)
    for n in range(1, nmax + 1):
        if n % 2 == 0:
            continue
        chi = 1 if n % 4 == 1 else -1
        result += mpmath.mpf(chi) / mpmath.power(n, s)
    return float(result)


# ============================================================
# 6. Ising Z Epstein decomposition
# ============================================================

def ising_z_epstein_decomposition(s):
    r"""Decompose Z_Ising into Epstein zeta contributions.

    On the imaginary axis tau=iy:
      Z_Ising(y) = (theta_2(iy) + theta_3(iy) + theta_4(iy)) / (2*eta(iy))

    The Mellin transform of Z_Ising * y^{s-1} dy decomposes into:
      (1/2) * [Mellin(theta_2/eta) + Mellin(theta_3/eta) + Mellin(theta_4/eta)]

    Each theta_j/eta is the CHARACTER of a representation. The Mellin of
    the partition function gives Epstein-type zetas.

    For the DIAGONAL modular invariant |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2,
    the individual terms involve:

    1. |chi_0|^2 + |chi_{1/2}|^2 = (theta_3 + theta_4)/(2*eta)  [on imag axis]
       Mellin of this involves E_Z^{(3)} + E_Z^{(4)} type sums.

    2. |chi_{1/16}|^2 = theta_2/(2*eta)
       Mellin involves E_Z^{(2)} type sum (shifted lattice).

    We return the Dirichlet series coefficients.
    """
    # The key observation: on the imaginary axis,
    # theta_j(iy)/eta(iy) are real and decay, so their Mellin transforms exist.
    #
    # theta_3(iy)/eta(iy) = sum_{n in Z} e^{-pi*y*n^2} / (e^{-pi*y/12} prod(1-e^{-2*pi*y*k}))
    # This does NOT factor as a simple Dirichlet series in general.
    #
    # However, for the PARTITION FUNCTION approach:
    # Z = sum_h d_h * q^{h - c/24}  (including all states)
    # Mellin(Z * y^s dy) = sum_h d_h * (2*pi*(h-c/24))^{-s} * Gamma(s)
    #
    # For Ising: c=1/2, so c/24 = 1/48.
    # Primaries: h=0 (d=1), h=1/2 (d=1), h=1/16 (d=1).
    # Descendants: Virasoro modules built on these.
    #
    # The "Epstein" zeta is:
    # epsilon^c_s = sum_{primary lambda} (h_lambda)^{-s}
    # For Ising: epsilon^{1/2}_s = (1/2)^{-s} + (1/16)^{-s} = 2^s + 16^s
    # (excluding h=0 vacuum).

    # Primary Epstein
    h_values = [mpmath.mpf('0.5'), mpmath.mpf(1) / 16]
    epstein_primary = sum(h ** (-s) for h in h_values)

    # Full character Epstein (including descendants)
    # This requires the full q-expansion, computed separately.

    return {
        'primary_epstein': float(epstein_primary),
        'h_values': [float(h) for h in h_values],
        'num_primaries': len(h_values),
    }


# ============================================================
# 7. Rocha-Caridi theta functions for general M(p,q)
# ============================================================

def rocha_caridi_theta(r, s, p, q_param, tau, nmax=500):
    r"""Theta function Theta_{r,s}(tau) at level 2pq.

    Theta_{r,s}(tau) = sum_{n in Z} exp(2*pi*i*tau * (2pq*n + ps - qr)^2 / (4pq))

    This is a theta function for the 1D lattice Z with
    quadratic form Q(n) = (2pq*n + (ps-qr))^2 / (4pq)
    i.e., for lattice vectors of the form (2pq*n + shift)/sqrt(4pq).

    Parameters
    ----------
    r, s : int
        Kac table indices. 1 <= r <= q_param-1, 1 <= s <= p-1.
    p, q_param : int
        Minimal model parameters. p > q_param, gcd(p,q_param) = 1.
    """
    q_val = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    shift = p * s - q_param * r
    level = 4 * p * q_param

    result = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        arg = mpmath.mpf(2 * p * q_param * n + shift) ** 2 / level
        result += q_val ** arg
    return result


def minimal_model_character(r, s, p, q_param, tau, nmax=500):
    r"""Character of M(p,q) primary (r,s) via Rocha-Caridi formula.

    chi_{r,s}(q) = (Theta_{r,s}(tau) - Theta_{r,-s}(tau)) / eta(tau)

    where Theta_{r,-s} = Theta with shift ps+qr instead of ps-qr.

    Conformal weight: h_{r,s} = ((pr - qs)^2 - (p-q)^2) / (4pq).
    Central charge: c = 1 - 6(p-q)^2/(pq).
    """
    theta_plus = rocha_caridi_theta(r, s, p, q_param, tau, nmax)
    # Theta_{r,-s} has shift p*(-s) - q*r = -(ps + qr)
    # But by periodicity, Theta_{r,-s}(tau) = sum_n q^{(2pqn - ps - qr)^2/(4pq)}
    q_val = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    shift_minus = -(p * s + q_param * r)
    level = 4 * p * q_param
    theta_minus = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        arg = mpmath.mpf(2 * p * q_param * n + shift_minus) ** 2 / level
        theta_minus += q_val ** arg

    eta_val = dedekind_eta(tau, nmax)
    return (theta_plus - theta_minus) / eta_val


def minimal_model_data(p, q_param):
    r"""Return central charge and Kac table for M(p,q).

    c = 1 - 6(p-q)^2/(pq)
    h_{r,s} = ((pr - qs)^2 - (p-q)^2)/(4pq)
    for 1 <= r <= q-1, 1 <= s <= p-1, with identification (r,s) ~ (q-r, p-s).
    """
    c = 1 - 6 * (p - q_param) ** 2 / (p * q_param)

    primaries = {}
    seen = set()
    for r in range(1, q_param):
        for s in range(1, p):
            # Identification: (r,s) ~ (q-r, p-s)
            r2, s2 = q_param - r, p - s
            key = tuple(sorted([(r, s), (r2, s2)]))
            if key in seen:
                continue
            seen.add(key)
            h = ((p * r - q_param * s) ** 2 - (p - q_param) ** 2) / (4 * p * q_param)
            primaries[(r, s)] = float(h)

    return {
        'c': float(c),
        'primaries': primaries,
        'num_primaries': len(primaries),
        'p': p,
        'q': q_param,
        'level': 2 * p * q_param,
    }


# ============================================================
# 8. Ising as M(4,3): level-24 theta functions
# ============================================================

def ising_level24_decomposition(tau, nmax=500):
    r"""Express Ising characters as level-24 theta functions.

    For M(4,3), level = 2*4*3 = 24.
    Theta_{r,s}(tau) at level 24 with shifts:
      (1,1): shift = 4*1 - 3*1 = 1,   Theta_{1,1} = sum_n q^{(24n+1)^2/48}
      (1,2): shift = 4*2 - 3*1 = 5,   Theta_{1,2} = sum_n q^{(24n+5)^2/48}
      (2,1): shift = 4*1 - 3*2 = -2,  Theta_{2,1} = sum_n q^{(24n-2)^2/48}

    And the "minus" thetas:
      Theta_{1,-1}: shift = -(4*1+3*1) = -7,  sum_n q^{(24n-7)^2/48}
      Theta_{1,-2}: shift = -(4*2+3*1) = -11, sum_n q^{(24n-11)^2/48}
      Theta_{2,-1}: shift = -(4*1+3*2) = -10, sum_n q^{(24n-10)^2/48}

    Characters:
      chi_{1,1} = (Theta_{1,1} - Theta_{1,-1}) / eta
      chi_{1,2} = (Theta_{1,2} - Theta_{1,-2}) / eta
      chi_{2,1} = (Theta_{2,1} - Theta_{2,-1}) / eta
    """
    q_val = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    eta_val = dedekind_eta(tau, nmax)

    level = 48  # denominator = 4*p*q = 4*4*3 = 48

    # Shifts for the three primaries
    shifts = {
        (1, 1): (1, -7),    # (ps-qr, -(ps+qr))
        (1, 2): (5, -11),
        (2, 1): (-2, -10),
    }

    thetas = {}
    characters = {}
    for (r, s), (shift_p, shift_m) in shifts.items():
        # Theta_plus
        theta_p = mpmath.mpf(0)
        for n in range(-nmax, nmax + 1):
            arg = mpmath.mpf(24 * n + shift_p) ** 2 / level
            theta_p += q_val ** arg

        # Theta_minus
        theta_m = mpmath.mpf(0)
        for n in range(-nmax, nmax + 1):
            arg = mpmath.mpf(24 * n + shift_m) ** 2 / level
            theta_m += q_val ** arg

        thetas[(r, s)] = {'plus': theta_p, 'minus': theta_m}
        characters[(r, s)] = (theta_p - theta_m) / eta_val

    return {
        'thetas': thetas,
        'characters': characters,
        'level': 24,
        'denominator': level,
    }


def ising_dirichlet_characters(s_val, nmax=5000):
    r"""Identify the Dirichlet characters for Ising (level 24) Epstein zetas.

    For Theta_{r,s}(tau) = sum_{n in Z} q^{(24n + a)^2 / 48}
    where a = ps - qr, the Mellin transform gives:

    E_{r,s}(s) = sum_{n in Z, n != 0, n ≡ a (mod 24)} |n|^{-2s} / (48)^s
               + (if a=0): excluded

    This is a partial zeta function: sum over integers in residue class a mod 24.

    The partial zeta function zeta(s; a, 24) = sum_{n>=1, n ≡ a (24)} n^{-s}
    decomposes into Dirichlet L-functions:
      zeta(s; a, N) = (1/phi(N)) sum_{chi mod N} conj(chi(a)) * L(s, chi)

    For N = 24, phi(24) = 8. The Dirichlet characters mod 24 are products
    of characters mod 8 and mod 3.

    Returns the decomposition for each Ising residue class.
    """
    N = 24
    # Residue classes for Ising level-24 thetas
    # (r,s) = (1,1): a = 1 mod 24 and a = 7 mod 24
    # (r,s) = (1,2): a = 5 mod 24 and a = 11 mod 24
    # (r,s) = (2,1): a = 22 mod 24 (equiv -2) and a = 14 mod 24 (equiv -10)
    # Note: a = -2 mod 24 = 22, a = -10 mod 24 = 14

    residue_classes = {
        (1, 1): {'plus': 1, 'minus': 17},     # 24-7=17
        (1, 2): {'plus': 5, 'minus': 13},     # 24-11=13
        (2, 1): {'plus': 22, 'minus': 14},    # -2 mod 24 = 22, -10 mod 24 = 14
    }

    # Compute partial zeta for each residue class
    results = {}
    for (r, s_idx), classes in residue_classes.items():
        for label, a in classes.items():
            # zeta(s; a, 24) + zeta(s; 24-a, 24) = sum_{n ≡ ±a (24)} n^{-s}
            partial = mpmath.mpf(0)
            for n in range(1, nmax + 1):
                if n % N == a or n % N == (N - a) % N:
                    partial += mpmath.power(n, -s_val)
            results[(r, s_idx, label)] = float(partial)

    # The "theta Epstein" for each character is:
    # sum over n ≡ a (24): n^{-2s} (from the n^2/48 exponent, after Mellin)
    # Actually: Mellin of q^{n^2/(48)} at tau=iy gives
    # integral e^{-pi*y*n^2/24} y^{s-1} dy = (pi*n^2/24)^{-s} Gamma(s)
    # So the Dirichlet series is sum_{n ≡ a (24)} (n^2/48)^{-s} * Gamma(s)/...
    # = (48)^s * sum_{n ≡ a (24)} n^{-2s}

    theta_epsteins = {}
    for (r, s_idx), classes in residue_classes.items():
        for label, a in classes.items():
            val = mpmath.mpf(0)
            for n in range(1, nmax + 1):
                if n % N == a or n % N == (N - a) % N:
                    val += mpmath.power(n, -2 * s_val)
            theta_epsteins[(r, s_idx, label)] = float(val)

    return {
        'residue_classes': residue_classes,
        'partial_zetas': results,
        'theta_epsteins': theta_epsteins,
        'modulus': N,
    }


# ============================================================
# 9. Cross-term Mellin analysis
# ============================================================

def cross_term_numerical(y, nmax=500):
    r"""Compute the cross term Re(sqrt(theta_3 * conj(theta_4))) / |eta|^2.

    On the imaginary axis tau = iy:
      theta_3 and theta_4 are both REAL, so
      sqrt(theta_3 * theta_4) is real.
      The cross term simplifies to sqrt(theta_3 * theta_4) / eta.

    This cross term appears in |chi_0|^2 - |chi_{1/2}|^2 = sqrt(t3*t4)/eta.

    KEY: sqrt(theta_3 * theta_4) has the product expansion:
      sqrt(theta_3 * theta_4) = prod_{n=1}^inf (1-q^n)(1+q^{2n-1})
    which is related to theta functions at DOUBLE the period.
    """
    tau = mpmath.mpc(0, y)
    t3 = mpmath.re(theta_3(tau, nmax))
    t4 = mpmath.re(theta_4(tau, nmax))
    eta_val = mpmath.re(dedekind_eta(tau, nmax))

    cross = mpmath.sqrt(t3 * t4) / eta_val

    # Also: theta_3(tau)*theta_4(tau) = theta_4(2*tau)^2
    # (Landen-type identity)
    # Actually: theta_3(q)*theta_4(q) = theta_4(q^2)^2 (? -- let's check)
    tau2 = mpmath.mpc(0, 2 * y)
    t4_double = mpmath.re(theta_4(tau2, nmax))

    # The correct identity is:
    # theta_3(tau) * theta_4(tau) = theta_3(2*tau)^2 - ... nope
    # Let's just record the numerical values and check identities
    # Actually: theta_2(2tau)^2 = theta_3(tau)^2 - theta_4(tau)^2
    # And: theta_3(2tau)^2 = (theta_3(tau)^2 + theta_4(tau)^2)/2
    t3_double = mpmath.re(theta_3(tau2, nmax))
    t2_double = mpmath.re(theta_2(tau2, nmax))

    return {
        'cross_term': float(cross),
        'theta3': float(t3),
        'theta4': float(t4),
        'eta': float(eta_val),
        'sqrt_t3_t4': float(mpmath.sqrt(t3 * t4)),
        # Check: theta_3(2tau)^2 = (theta_3^2 + theta_4^2)/2
        'doubling_check_lhs': float(t3_double ** 2),
        'doubling_check_rhs': float((t3 ** 2 + t4 ** 2) / 2),
    }


def cross_term_mellin_numerical(s_val, ymin=0.01, ymax=50.0, npts=5000):
    r"""Numerical Mellin transform of the cross term sqrt(t3*t4)/eta at tau=iy.

    integral_0^inf sqrt(theta_3(iy)*theta_4(iy)) / eta(iy) * y^{s-1} dy

    We use Gauss-Legendre quadrature on [ymin, ymax] (exponential decay
    ensures the tails are negligible).

    The result should be compared with known L-functions to identify
    whether the cross term gives a standard or new L-function.
    """
    # Change of variable: t = log(y), y = e^t, dy = e^t dt
    # integral = integral_{log(ymin)}^{log(ymax)} f(e^t) * e^{ts} dt

    from functools import lru_cache

    # Use simple trapezoidal on log scale
    log_ymin = math.log(ymin)
    log_ymax = math.log(ymax)
    dt = (log_ymax - log_ymin) / npts

    result = mpmath.mpf(0)
    for i in range(npts + 1):
        t = log_ymin + i * dt
        y = math.exp(t)
        tau = mpmath.mpc(0, y)

        t3 = mpmath.re(theta_3(tau, 200))
        t4 = mpmath.re(theta_4(tau, 200))
        eta_val = mpmath.re(dedekind_eta(tau, 200))

        if eta_val < 1e-50:
            continue

        f = mpmath.sqrt(t3 * t4) / eta_val
        weight = 1.0 if (i == 0 or i == npts) else 2.0 if i % 2 == 0 else 4.0
        # Trapezoidal
        if i == 0 or i == npts:
            weight = 0.5
        else:
            weight = 1.0

        result += weight * f * mpmath.power(y, s_val) * dt

    return float(result)


# ============================================================
# 10. General minimal model M(p,q) theta decomposition
# ============================================================

def tricritical_ising_data():
    r"""M(5,4): tricritical Ising model.

    c = 7/10, level = 2*5*4 = 40.
    Primaries: h = 0, 1/10, 3/5, 3/2, 3/80, 7/16.
    """
    return minimal_model_data(5, 4)


def lee_yang_data():
    r"""M(5,2): Lee-Yang model.

    c = -22/5, level = 2*5*2 = 20.
    Primaries: h = 0, -1/5.
    """
    return minimal_model_data(5, 2)


def three_state_potts_data():
    r"""M(6,5): three-state Potts model.

    c = 4/5, level = 2*6*5 = 60.
    """
    return minimal_model_data(6, 5)


def auxiliary_lattice_data(p, q_param):
    r"""Compute auxiliary lattice for M(p,q).

    The level-2pq theta functions Theta_{r,s} correspond to the
    1D lattice Z with quadratic form Q(n) = n^2/(4pq), restricted
    to the coset n ≡ (ps - qr) mod 2pq.

    The auxiliary lattice has:
      - Rank: 1
      - Gram matrix: [1/(2pq)]  (or equivalently Z/sqrt(2pq))
      - Discriminant: 2pq
      - Self-dual iff 2pq = 1 (never for p>q>1)
      - Class number: h(D) where D = -4*2pq (fundamental discriminant)

    For Ising (p=4, q=3): level=24, disc=24, NOT self-dual.
    """
    level = 2 * p * q_param
    disc = level  # discriminant of the quadratic form

    # Number of distinct residue classes needed
    # for the Kac table: 1 <= r <= q-1, 1 <= s <= p-1
    num_primaries = (p - 1) * (q_param - 1) // 2
    residue_classes = set()
    for r in range(1, q_param):
        for s in range(1, p):
            shift = (p * s - q_param * r) % (2 * level)
            residue_classes.add(shift)
            shift_m = (-(p * s + q_param * r)) % (2 * level)
            residue_classes.add(shift_m)

    return {
        'p': p,
        'q': q_param,
        'level': level,
        'discriminant': disc,
        'gram_matrix': [[Fraction(1, level)]],
        'self_dual': (level == 1),
        'num_primaries': num_primaries,
        'num_residue_classes': len(residue_classes),
        'residue_classes': sorted(residue_classes),
    }


# ============================================================
# 11. Full Epstein decomposition of Z_Ising
# ============================================================

def ising_full_epstein_decomposition(s_val, nmax=5000):
    r"""Full Epstein decomposition of Z_Ising.

    Z_Ising = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2

    Each |chi_{r,s}|^2 involves products of level-24 theta functions divided
    by |eta|^2. The Mellin transform of each term gives:

    epsilon^{1/2}_s(Ising) = sum_i |c_i|^2 * E_i(s)

    where E_i are partial zeta functions (Dirichlet series over residue classes
    mod 24).

    Since the residue class decomposition gives:
      zeta(s; a, N) = (1/phi(N)) sum_{chi mod N} conj(chi(a)) L(s, chi)

    the E_i are LINEAR COMBINATIONS of Dirichlet L-functions mod 24.

    Dirichlet characters mod 24:
      phi(24) = 8, so there are 8 characters.
      24 = 8 * 3, so chars mod 24 = (chars mod 8) x (chars mod 3).
      Chars mod 8: trivial, chi_8^(1), chi_8^(2), chi_8^(3) [4 chars, even part]
      Chars mod 3: trivial, chi_3 [2 chars]
      Total: 8 characters.

    The L-functions are:
      L(s, chi_0) = zeta(s) * (1 - 2^{-s}) * (1 - 3^{-s})  [removed 2,3 factors]
      L(s, chi_{-4}) = Dirichlet beta function
      L(s, chi_{-3}) = L(s, Legendre symbol mod 3)
      L(s, chi_{12}) = ...
      etc.

    We compute the primary Epstein zeta (sum over primaries only, not descendants)
    and the full partition-function Epstein.
    """
    # Primary Epstein: sum over conformal weights
    # h = 0 (excluded as vacuum), h = 1/2, h = 1/16
    h_vals = [mpmath.mpf('0.5'), mpmath.mpf(1) / 16]
    primary_eps = sum(h ** (-s_val) for h in h_vals)

    # Level-24 partial zeta functions for each character
    # chi_{1,1}: sum over n ≡ 1 or 23 (mod 24), MINUS sum over n ≡ 7 or 17 (mod 24)
    # Then the theta Epstein is sum n^{-2s} over these classes

    # Character Epstein: from the level-24 theta function structure
    # For each (r,s), the character chi_{r,s} = (Theta_{a+} - Theta_{a-})/eta
    # |chi_{r,s}|^2 = |Theta_{a+} - Theta_{a-}|^2 / |eta|^2
    # On imaginary axis, this is (Theta_{a+} - Theta_{a-})^2 / eta^2
    # = (Theta_{a+}^2 - 2*Theta_{a+}*Theta_{a-} + Theta_{a-}^2) / eta^2

    # Residue classes mod 48 (the actual level of n^2 in the exponent)
    # For (1,1): a+ = 1 → n ≡ ±1 (48); a- = 7 → n ≡ ±7 (48)
    # Wait -- actually mod 24 since Theta uses (24n + a)^2/48

    # The Dirichlet series for the theta function:
    # Theta_{a}(iy) = sum_{m ≡ a (24)} exp(-pi*y*m^2/24)
    # So the partial Dirichlet series is D_a(s) = sum_{m>0, m ≡ ±a (24)} m^{-2s}

    partial_zetas = {}
    for a in [1, 5, 7, 10, 11, 13, 14, 17, 22]:
        val = mpmath.mpf(0)
        a_mod = a % 24
        neg_a = (24 - a_mod) % 24
        for n in range(1, nmax + 1):
            if n % 24 == a_mod or (neg_a != a_mod and n % 24 == neg_a):
                val += mpmath.power(n, -2 * s_val)
        partial_zetas[a] = float(val)

    # Full zeta(2s) for comparison
    full_zeta_2s = float(mpmath.zeta(2 * s_val))

    # Sum of all partial zetas should give zeta(2s) (up to the n ≡ 0 (24) terms)
    all_classes_sum = mpmath.mpf(0)
    for a in range(0, 24):
        val = mpmath.mpf(0)
        for n in range(1, nmax + 1):
            if n % 24 == a:
                val += mpmath.power(n, -2 * s_val)
        all_classes_sum += val

    return {
        'primary_epstein': float(primary_eps),
        'partial_zetas': partial_zetas,
        'full_zeta_2s': full_zeta_2s,
        'all_classes_sum': float(all_classes_sum),
        'all_classes_vs_zeta': float(abs(all_classes_sum - mpmath.zeta(2 * s_val))),
    }


def dirichlet_characters_mod24():
    r"""Enumerate Dirichlet characters mod 24.

    24 = 8 * 3, so characters factor as chi = chi_8 x chi_3.
    Units mod 24: {1, 5, 7, 11, 13, 17, 19, 23} (phi(24) = 8).

    Characters mod 8: 4 characters
      chi_0: all 1
      chi_1 = chi_{-4}: 1 -> 1, 3 -> -1, 5 -> -1, 7 -> 1
                         (Kronecker symbol (-4/n))
      chi_2 = chi_{-1}: 1 -> 1, 3 -> 1, 5 -> 1, 7 -> 1 ... actually
              mod 8 units = {1,3,5,7}
              chi_0(8) = (1,1,1,1)
              chi_{-4} values: (-4/1)=1, (-4/3)=-1, (-4/5)=-1, (-4/7)=1
              chi_{-1} = (-1/n): 1,1,-1,-1? No: (-1/1)=1, (-1/3)=-1, (-1/5)=1, (-1/7)=-1
              chi_4 = chi_{-4}*chi_{-1}: 1,-1*-1=1, -1*1=-1, 1*-1=-1
              wait, let me be more careful.

    We'll compute them directly.
    """
    N = 24
    units = [n for n in range(1, N) if math.gcd(n, N) == 1]
    # units = [1, 5, 7, 11, 13, 17, 19, 23]

    # A character mod 24 is determined by its values on generators of (Z/24Z)*.
    # (Z/24Z)* ≅ Z/2 x Z/2 x Z/2 (all elements have order 1 or 2)
    # Generators: 5, 7, 11 (any 3 of the 7 non-trivial units)
    # Actually: 5^2 = 25 = 1 mod 24, 7^2 = 49 = 1 mod 24, 11^2 = 121 = 1 mod 24
    # So every unit has order 2 except 1. Group = (Z/2)^3.

    # All 8 characters are determined by signs on {5, 7, 11}:
    characters = {}
    for s5 in [1, -1]:
        for s7 in [1, -1]:
            for s11 in [1, -1]:
                chi_vals = {}
                # Determine chi on all units
                # 1 -> 1 always
                # 5 -> s5
                # 7 -> s7
                # 11 -> s11
                # 13 = 5*7*11 mod 24: chi(13) = s5*s7*s11
                # Actually 5*7 = 35 = 11 mod 24. So 5*7 = 11.
                # Then 5*11 = 55 = 7 mod 24. And 7*11 = 77 = 5 mod 24.
                # And 5*7*11 = 385 = 385-16*24 = 385-384 = 1 mod 24.
                # So the group is generated by 5 and 7 (since 11=5*7).
                # This means s11 = s5*s7 (not independent!).
                # (Z/24Z)* = {1, 5, 7, 11, 13, 17, 19, 23}
                # 11 = 5*7, 13 = 5*7*... let me recompute.
                # 5*7 = 35 mod 24 = 11. OK.
                # 5*11 = 55 mod 24 = 7. OK.
                # 5*13 = 65 mod 24 = 17.
                # So 17 = 5*13. But 13 mod 24: 13*13 = 169 = 169-7*24 = 1. So 13 has order 2.
                # Let me just list: {1, 5, 7, 11=5*7, 13, 17=5*13, 19=7*13, 23=5*7*13}
                # So generators are {5, 7, 13} with all orders 2.
                pass

    # Let me just compute all characters directly as Kronecker symbols
    # The 8 characters mod 24 correspond to discriminants d dividing 24*...
    # Simpler: use known characters.
    # Actually, for our purposes, what matters is which L-functions appear
    # in the partial zeta decomposition. Let me compute this differently.

    # Characters mod 24 are products of chars mod 8 and chars mod 3.
    # Chars mod 3: trivial chi_0, and chi_{-3}(n) = (n/3) Legendre symbol
    #   chi_{-3}(1) = 1, chi_{-3}(2) = -1

    # Chars mod 8: (Z/8Z)* = {1,3,5,7} ≅ Z/2 x Z/2
    #   chi_0(8): (1,1,1,1)
    #   chi_{-4}: Kronecker (-4/n): (1,-1,-1,1) [conductor 4]
    #   chi_{-1}: Kronecker (-1/n): (1,-1,1,-1) [conductor ... ]
    #   Actually (-1/1)=1, (-1/3)=(-1)^{(9-1)/8}... hmm, let me use Jacobi.
    #   chi_{-1}(1)=1, chi_{-1}(3)=-1... no. (-1/n) for n odd = (-1)^{(n-1)/2}
    #   (-1/1)=1, (-1/3)=-1, (-1/5)=1, (-1/7)=-1
    #   So chi_{-1}: (1,-1,1,-1)
    #   chi_4 = chi_{-4}*chi_{-1}: (1,1,-1,-1)
    # Wait: product of (1,-1,-1,1) and (1,-1,1,-1) = (1,1,-1,-1).

    chars_mod8 = {
        'chi0_8': {1: 1, 3: 1, 5: 1, 7: 1},
        'chi_{-4}': {1: 1, 3: -1, 5: -1, 7: 1},
        'chi_{-1}': {1: 1, 3: -1, 5: 1, 7: -1},
        'chi_4': {1: 1, 3: 1, 5: -1, 7: -1},
    }

    chars_mod3 = {
        'chi0_3': {1: 1, 2: 1},
        'chi_{-3}': {1: 1, 2: -1},
    }

    # Build all 8 characters mod 24
    all_chars = {}
    for name8, c8 in chars_mod8.items():
        for name3, c3 in chars_mod3.items():
            name = f"{name8}_x_{name3}"
            vals = {}
            for n in units:
                vals[n] = c8[n % 8] * c3[n % 3] if (n % 8 in c8 and n % 3 in c3) else 0
            all_chars[name] = vals

    return {
        'units': units,
        'characters': all_chars,
        'phi_24': len(units),
    }


def partial_zeta_dirichlet_decomposition(a, s_val, nmax=5000):
    r"""Decompose partial zeta zeta(s; a, 24) into Dirichlet L-functions.

    zeta(s; a, 24) = sum_{n ≡ a (24)} n^{-s}
                   = (1/8) sum_{chi mod 24} conj(chi(a)) L(s, chi)

    Returns the coefficients conj(chi(a))/8 for each character.
    """
    N = 24
    units = [n for n in range(1, N) if math.gcd(n, N) == 1]

    # Only applies when gcd(a, 24) = 1
    if math.gcd(a, N) != 1:
        return {'error': f'a={a} not coprime to 24', 'a': a}

    # Characters mod 24 as CRT of mod 8 and mod 3
    # We'll compute L(s, chi) and the coefficients numerically
    # Characters mod 24 are completely multiplicative functions
    # chi(n) = 0 if gcd(n, 24) > 1.
    # For coprime n, factor via CRT: n mod 8 and n mod 3.
    #
    # Characters mod 8: (Z/8Z)* = {1,3,5,7} ~ Z/2 x Z/2
    # Labelled by their values on generators:
    #   triv:     (1,1,1,1)
    #   chi_{-4}: (1,-1,-1,1) -- Kronecker (-4/.)
    #   chi_{-1}: (1,-1,1,-1) -- Kronecker (-1/.), i.e., (-1)^{(n-1)/2}
    #   chi_4:    (1,1,-1,-1) -- product of above two
    #
    # Characters mod 3: (Z/3Z)* = {1,2} ~ Z/2
    #   triv:     (1,1)
    #   chi_{-3}: (1,-1) -- Legendre symbol (n/3)

    # Precompute character table on units mod 24
    units_24 = [n for n in range(1, 24) if math.gcd(n, 24) == 1]
    # = [1, 5, 7, 11, 13, 17, 19, 23]

    chi8_table = {
        'triv': {1: 1, 3: 1, 5: 1, 7: 1},
        'chi_{-4}': {1: 1, 3: -1, 5: -1, 7: 1},
        'chi_{-1}': {1: 1, 3: -1, 5: 1, 7: -1},
        'chi_4': {1: 1, 3: 1, 5: -1, 7: -1},
    }
    chi3_table = {
        'triv': {1: 1, 2: 1},
        'chi_{-3}': {1: 1, 2: -1},
    }

    # Full character table mod 24
    chi24_table = {}
    for n8, c8 in chi8_table.items():
        for n3, c3 in chi3_table.items():
            name = f"{n8}_x_{n3}"
            vals = {}
            for u in units_24:
                vals[u] = c8[u % 8] * c3[u % 3]
            chi24_table[name] = vals

    # Build chi function: chi(n) for arbitrary positive n
    def make_chi_fn(char_vals):
        def chi_fn(n):
            if math.gcd(n, 24) != 1:
                return 0
            return char_vals[n % 24]
        return chi_fn

    chi_table = {}
    for name, vals in chi24_table.items():
        chi_table[name] = make_chi_fn(vals)

    # Compute L(s, chi) for each character
    L_values = {}
    for name, chi_fn in chi_table.items():
        L_val = mpmath.mpf(0)
        for n in range(1, nmax + 1):
            cv = chi_fn(n)
            if cv != 0:
                L_val += cv * mpmath.power(n, -s_val)
        L_values[name] = float(L_val)

    # Coefficients: conj(chi(a))/phi(N)
    coeffs = {}
    for name, chi_fn in chi_table.items():
        cv = chi_fn(a)
        coeffs[name] = cv / 8.0  # phi(24) = 8

    # Verify: sum of coeffs * L = partial zeta
    reconstructed = sum(coeffs[name] * L_values[name] for name in chi_table)
    direct = mpmath.mpf(0)
    for n in range(1, nmax + 1):
        if n % N == a:
            direct += mpmath.power(n, -s_val)

    return {
        'a': a,
        'L_values': L_values,
        'coefficients': coeffs,
        'reconstructed': float(reconstructed),
        'direct': float(direct),
        'error': float(abs(reconstructed - float(direct))),
    }


# ============================================================
# 12. Shadow depth prediction from L-function count
# ============================================================

def shadow_depth_from_l_functions(p, q_param):
    r"""Predict the shadow depth of M(p,q) from its theta decomposition.

    The L-functions appearing in the Epstein decomposition of Z_{M(p,q)}
    are Dirichlet L-functions mod 2pq. The number of DISTINCT critical
    lines depends on the number of distinct L-functions.

    For M(p,q):
      - Level = 2pq
      - Characters mod 2pq with phi(2pq) distinct characters
      - Each character contributes L(s, chi) with functional equation
        relating s to 1-s (for the full character Dirichlet series)
      - Critical line at Re(s) = 1/2 for each primitive character

    However, for the THETA Dirichlet series (with n^{-2s} from n^2/level),
    the critical line is at Re(s) = 1/4 (since E(s) ~ sum n^{-2s}).

    Shadow depth prediction:
      - Ising M(4,3): c=1/2, minimal model, shadow depth = M (mixed/infinite)
        since c < 1 has degenerate representation theory
      - Actually for the VOA itself (not the module category),
        the shadow depth depends on the OPE structure.
    """
    data = minimal_model_data(p, q_param)

    # Number of L-functions = number of distinct primitive Dirichlet characters
    # appearing in the decomposition of the partition function
    level = 2 * p * q_param

    # phi(level) distinct characters mod level
    phi_level = sum(1 for n in range(1, level) if math.gcd(n, level) == 1)

    # Number of primaries
    num_prim = data['num_primaries']

    return {
        'model': f'M({p},{q_param})',
        'c': data['c'],
        'level': level,
        'phi_level': phi_level,
        'num_primaries': num_prim,
        'primaries': data['primaries'],
    }


# ============================================================
# 13. Verification utilities
# ============================================================

def verify_theta_jacobi_relation(y, nmax=500):
    r"""Verify multiple Jacobi theta identities at tau = iy.

    1. theta_3^4 = theta_2^4 + theta_4^4 (abstruse identity)
    2. theta_2*theta_3*theta_4 = 2*eta^3 (triple product)
    3. theta_3^2 = theta_2^2 + theta_4^2 ... no, this is FALSE.
       Actually: theta_3(2tau)^2 = (theta_3(tau)^2 + theta_4(tau)^2)/2
    4. theta_2(2tau)^2 = (theta_3(tau)^2 - theta_4(tau)^2)/2
    """
    tau = mpmath.mpc(0, y)
    tau2 = mpmath.mpc(0, 2 * y)

    t2 = mpmath.re(theta_2(tau, nmax))
    t3 = mpmath.re(theta_3(tau, nmax))
    t4 = mpmath.re(theta_4(tau, nmax))
    eta_val = mpmath.re(dedekind_eta(tau, nmax))

    t2_2 = mpmath.re(theta_2(tau2, nmax))
    t3_2 = mpmath.re(theta_3(tau2, nmax))

    results = {}

    # 1. Abstruse: theta_3^4 = theta_2^4 + theta_4^4
    results['abstruse'] = {
        'lhs': float(t3 ** 4),
        'rhs': float(t2 ** 4 + t4 ** 4),
        'error': float(abs(t3 ** 4 - t2 ** 4 - t4 ** 4)),
    }

    # 2. Triple product: theta_2*theta_3*theta_4 = 2*eta^3
    results['triple_product'] = {
        'lhs': float(t2 * t3 * t4),
        'rhs': float(2 * eta_val ** 3),
        'error': float(abs(t2 * t3 * t4 - 2 * eta_val ** 3)),
    }

    # 3. Doubling: theta_3(2tau)^2 = (theta_3(tau)^2 + theta_4(tau)^2)/2
    results['doubling_t3'] = {
        'lhs': float(t3_2 ** 2),
        'rhs': float((t3 ** 2 + t4 ** 2) / 2),
        'error': float(abs(t3_2 ** 2 - (t3 ** 2 + t4 ** 2) / 2)),
    }

    # 4. Doubling: theta_2(2tau)^2 = (theta_3(tau)^2 - theta_4(tau)^2)/2
    # Hmm, let me check: this might have a different convention factor.
    # Actually theta_2(2tau) = sqrt(theta_3(tau)^2 - theta_4(tau)^2)... not quite.
    # Let me just check numerically.
    results['doubling_t2'] = {
        'lhs': float(t2_2 ** 2),
        'rhs_candidate': float((t3 ** 2 - t4 ** 2) / 2),
    }

    return results
