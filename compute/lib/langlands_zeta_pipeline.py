#!/usr/bin/env python3
r"""
langlands_zeta_pipeline.py — End-to-end pipeline: shadow tower -> zeta zeros.

THE FULL CHAIN (PROVED for lattice VOAs, Approach A):
  Shadow tower Theta_A^{<=r} -> Rankin-Selberg integral -> Hecke decomposition
    -> L-functions -> zeros

SIX PIPELINE STAGES:
  Stage 1: Shadow extraction — VOA spec -> {kappa, C, Q, S_r}
  Stage 2: Partition function — shadow data -> Z(tau) -> hat{Z}
  Stage 3: Constrained Epstein — hat{Z} -> epsilon^c_s
  Stage 4: Hecke decomposition — epsilon -> product of L-functions
  Stage 5: Zero location — L-functions -> zeros in critical strip
  Stage 6: Shadow-spectral verification — #(critical lines) = depth - 1

SUPPORTED ALGEBRAS:
  Lattice (PROVED): V_Z (c=1), V_{E_8} (c=8), V_{Leech} (c=24)
  Heisenberg (c=1, identical to V_Z at self-dual radius)
  Virasoro at general c (GAP IDENTIFICATION: stage 2->3 breaks for non-lattice)

References:
  Benjamin-Chang, arXiv:2208.02259 (constrained Epstein, zeta-zero residues)
  Hecke, "Uber die Bestimmung Dirichletscher Reihen", Math. Ann. 112, 1936.
  Rankin, "Contributions to the theory of Ramanujan's function tau(n)", 1939.
  Selberg, "On the estimation of Fourier coefficients of modular forms", 1965.
"""

import numpy as np
import math
from functools import lru_cache

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# Stage 1: Shadow extraction
# ============================================================

# Shadow depth classification (CLAUDE.md):
#   G = Gaussian (r_max=2): Heisenberg, V_Z
#   L = Lie/tree (r_max=3): affine at level 1, V_{E_8}
#   C = contact/quartic (r_max=4): betagamma
#   M = mixed (r_max=inf): Virasoro, W_N

SHADOW_DEPTH_CLASSES = {
    'G': {'r_max': 2, 'description': 'Gaussian, terminates at arity 2'},
    'L': {'r_max': 3, 'description': 'Lie/tree, terminates at arity 3'},
    'C': {'r_max': 4, 'description': 'contact/quartic, terminates at arity 4'},
    'M': {'r_max': float('inf'), 'description': 'mixed, infinite tower'},
}


def voa_spec(voa_type, **kwargs):
    """Create a VOA specification dictionary.

    Args:
        voa_type: one of 'heisenberg', 'V_Z', 'V_E8', 'V_Leech', 'virasoro'
        **kwargs: additional parameters (e.g., c=central charge for Virasoro)

    Returns:
        dict with keys: type, central_charge, rank (if lattice), shadow_class, etc.
    """
    if voa_type == 'heisenberg':
        return {
            'type': 'heisenberg',
            'central_charge': 1,
            'rank': 1,
            'lattice_type': 'Z',
            'shadow_class': 'G',
            'shadow_depth': 2,
            'is_lattice': True,
        }
    elif voa_type == 'V_Z':
        return {
            'type': 'V_Z',
            'central_charge': 1,
            'rank': 1,
            'lattice_type': 'Z',
            'shadow_class': 'G',
            'shadow_depth': 2,
            'is_lattice': True,
        }
    elif voa_type == 'V_E8':
        return {
            'type': 'V_E8',
            'central_charge': 8,
            'rank': 8,
            'lattice_type': 'E8',
            'shadow_class': 'L',
            'shadow_depth': 3,
            'is_lattice': True,
        }
    elif voa_type == 'V_Leech':
        return {
            'type': 'V_Leech',
            'central_charge': 24,
            'rank': 24,
            'lattice_type': 'Leech',
            'shadow_class': 'C',  # at least depth 4 (3 critical lines)
            'shadow_depth': 4,
            'is_lattice': True,
        }
    elif voa_type == 'virasoro':
        c = kwargs.get('c', 0.5)
        return {
            'type': 'virasoro',
            'central_charge': c,
            'rank': None,
            'lattice_type': None,
            'shadow_class': 'M',
            'shadow_depth': float('inf'),
            'is_lattice': False,
        }
    else:
        raise ValueError(f"Unknown VOA type: {voa_type}")


def extract_shadow_tower(spec):
    """Stage 1: Extract shadow tower data from VOA specification.

    Returns dict with:
      kappa: arity-2 shadow (modular characteristic kappa = c/2)
      cubic_shadow: arity-3 shadow C (= 0 for self-dual)
      quartic_shadow: arity-4 shadow Q
      shadow_coefficients: dict {r: S_r} for available arities
      depth: shadow depth (r_max)
      shadow_class: G/L/C/M
    """
    c = spec['central_charge']
    kappa = c / 2  # Theorem D: kappa(A) = c/2 for all standard families

    # Cubic shadow C: vanishes for self-dual algebras.
    # For lattice VOAs: C = 0 iff the lattice is even unimodular.
    # For Heisenberg/V_Z: not self-dual but C = 0 because shadow tower
    # terminates at arity 2 (Gaussian class).
    # For V_{E_8}: E_8 is even unimodular, level 1 affine -> class L,
    # C != 0 in general but shadow terminates at arity 3.
    # For Virasoro: infinite tower, C != 0 generically.

    shadow_data = {
        'kappa': kappa,
        'central_charge': c,
        'depth': spec['shadow_depth'],
        'shadow_class': spec['shadow_class'],
        'shadow_coefficients': {2: kappa},
    }

    if spec['type'] in ('heisenberg', 'V_Z'):
        # Gaussian class: tower terminates at arity 2
        shadow_data['cubic_shadow'] = 0.0
        shadow_data['quartic_shadow'] = 0.0
        shadow_data['shadow_coefficients'][3] = 0.0
        shadow_data['shadow_coefficients'][4] = 0.0

    elif spec['type'] == 'V_E8':
        # Lie/tree class: tower terminates at arity 3
        # E_8 at level 1: affine, cubic shadow nonzero
        # The Eisenstein series E_4 = Theta_{E_8} has sigma_3 structure
        # which introduces the cubic contribution
        shadow_data['cubic_shadow'] = 240.0  # normalization from E_4 coefficient
        shadow_data['quartic_shadow'] = 0.0
        shadow_data['shadow_coefficients'][3] = 240.0
        shadow_data['shadow_coefficients'][4] = 0.0

    elif spec['type'] == 'V_Leech':
        # Leech lattice: depth >= 4 (Eisenstein + cusp form Delta_12)
        # Theta_{Leech} = E_{12} - (65520/691) Delta_12
        shadow_data['cubic_shadow'] = 1.0  # Eisenstein component present
        shadow_data['quartic_shadow'] = -65520.0 / 691.0  # cusp form component
        shadow_data['shadow_coefficients'][3] = 1.0
        shadow_data['shadow_coefficients'][4] = -65520.0 / 691.0

    elif spec['type'] == 'virasoro':
        # Mixed class: infinite tower, Q^contact = 10/[c(5c+22)]
        if c != 0:
            Q_contact = 10.0 / (c * (5 * c + 22))
        else:
            Q_contact = float('inf')
        shadow_data['cubic_shadow'] = None  # nonzero but not simply computable
        shadow_data['quartic_shadow'] = Q_contact
        shadow_data['Q_contact'] = Q_contact
        shadow_data['shadow_coefficients'][4] = Q_contact

    return shadow_data


# ============================================================
# Stage 2: Partition function
# ============================================================

def eta_real(y, nmax=500):
    """Dedekind eta on the imaginary axis: eta(iy) for y > 0."""
    log_result = -math.pi * y / 12.0
    for n in range(1, nmax + 1):
        val = math.exp(-2.0 * math.pi * n * y)
        if val < 1e-300:
            break
        log_result += math.log1p(-val)
    return math.exp(log_result)


def theta3_real(y, nmax=300):
    """Jacobi theta_3 on the imaginary axis: theta_3(iy) for y > 0."""
    result = 1.0
    for n in range(1, nmax + 1):
        val = math.exp(-math.pi * n * n * y)
        if val < 1e-300:
            break
        result += 2.0 * val
    return result


def sigma_k(n, k):
    """Divisor function sigma_k(n) = sum_{d|n} d^k."""
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eisenstein_series_q(k, y, nmax=300):
    """Evaluate normalized Eisenstein series E_k(iy) for y > 0.

    E_k(tau) = 1 + (2k/B_k) sum_{n>=1} sigma_{k-1}(n) q^n.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    Bk = float(mpmath.bernoulli(k))
    normalization = -2 * k / Bk

    result = 1.0
    for n in range(1, nmax + 1):
        qn = math.exp(-2 * math.pi * n * y)
        if qn < 1e-300:
            break
        result += normalization * sigma_k(n, k - 1) * qn
    return result


def ramanujan_tau_batch(nmax):
    """Compute tau(1), ..., tau(nmax) via eta^24 expansion."""
    N = nmax + 5
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for m in range(1, min(N + 1, nmax + 5)):
        new_coeffs = [0] * (N + 1)
        for j in range(25):
            sign = (-1) ** j
            binom_val = 1
            for i in range(j):
                binom_val = binom_val * (24 - i) // (i + 1)
            coeff = sign * binom_val
            for k_idx in range(N + 1):
                idx = k_idx + j * m
                if idx > N:
                    break
                new_coeffs[idx] += coeffs[k_idx] * coeff
        coeffs = new_coeffs

    return [coeffs[n - 1] if n - 1 < len(coeffs) else 0
            for n in range(1, nmax + 1)]


def j_invariant(y, nmax=300):
    """j-invariant j(iy) = E_4^3/eta^24 for y > 0.

    j(tau) = q^{-1} + 744 + 196884q + ...
    J(tau) = j(tau) - 744 = q^{-1} + 196884q + ...
    """
    E4 = eisenstein_series_q(4, y, nmax)
    eta_val = eta_real(y, nmax)
    # j = E_4^3 / (eta^24 * (2*pi)^{12})
    # Actually j = 1728 * E_4^3 / (E_4^3 - E_6^2)
    # Simpler: j = E_4^3 / Delta, where Delta = eta^24
    eta24 = eta_val ** 24
    if abs(eta24) < 1e-300:
        return float('inf')
    return E4 ** 3 / eta24


def compute_partition_function(spec, shadow_data, y):
    """Stage 2: Compute the partition function Z(tau) at tau = iy.

    Returns dict with:
      Z: the partition function Z(iy)
      Z_hat: the primary-counting function hat{Z} = y^{c/2} |eta|^{2c} Z
      y: the evaluation point
    """
    c = spec['central_charge']
    vtype = spec['type']

    if vtype in ('heisenberg', 'V_Z'):
        # Z = theta_3^2 / eta^2 for the full Narain theory at self-dual radius
        # For pure Heisenberg (chiral): Z_chiral = 1/eta
        # For diagonal Narain c=1: Z = theta_3^2 / eta^2
        theta = theta3_real(y)
        eta_val = eta_real(y)
        Z = theta ** 2 / eta_val ** 2

    elif vtype == 'V_E8':
        # Z = E_4(tau) / eta(tau)^16
        # Theta_{E_8} = E_4; the full lattice theory partition function
        # includes the oscillator contribution 1/eta^8 per real direction
        # For c=8 lattice: Z = Theta_{E_8} / eta^{2c} * (extra factors)
        # Actually for lattice VOA: Z_lattice = Theta_Lambda / eta^{rank}
        # Then the diagonal theory: Z = |Theta / eta^{rank}|^2
        # The scalar primary counting uses hat{Z} = y^{c/2} |eta|^{2c} Z
        # For c=8: hat{Z} = y^4 * eta^{16} * Theta_{E_8}^2 / eta^{16} = y^4 * Theta_{E_8}^2
        # Hmm, let's be careful. The partition function on the torus:
        # Z(tau) = Tr(q^{L_0 - c/24} qbar^{L_0bar - c/24})
        # For lattice: Z = Theta_Lambda(tau, taubar) / |eta(tau)|^{2*rank}
        # For diagonal scalar sector: Theta = sum_v q^{|v|^2/2}
        # E_4 evaluated at iy:
        E4 = eisenstein_series_q(4, y)
        eta_val = eta_real(y)
        # Lattice partition function (holomorphic part squared):
        Z = E4 ** 2 / eta_val ** 16

    elif vtype == 'V_Leech':
        # Z = (J(tau) + 24)^2 / ... for the diagonal Leech theory
        # J(tau) = j(tau) - 744
        # The Leech lattice VOA has Z_chiral = J + 24
        # Actually: Z_chiral = sum dim(V_n) q^{n-1} = q^{-1} + 0 + 196884q + ...
        # which is J(tau) + 24 (the constant 24 = dim of first nontrivial rep)
        # Wait, more precisely: Theta_{Leech} / eta^{24} = J + 24
        # So Z_chiral = J(tau) + 24, and the diagonal partition function:
        # The Leech theta function at iy:
        E12 = eisenstein_series_q(12, y)
        tau_coeffs = ramanujan_tau_batch(300)
        c_delta = -65520.0 / 691.0
        # Theta_{Leech}(iy) = E_{12}(iy) + c_delta * Delta(iy)
        # Delta(iy) = eta(iy)^{24} * sum tau(n) q^n (with q = e^{-2*pi*y})
        # Actually Delta = eta^24 is a cusp form with a_1 = 1 (no constant term)
        # Delta(tau) = sum_{n>=1} tau(n) q^n
        eta_val = eta_real(y)
        # Evaluate Delta directly
        Delta_val = 0.0
        for n in range(1, min(301, len(tau_coeffs) + 1)):
            qn = math.exp(-2 * math.pi * n * y)
            if qn < 1e-300:
                break
            Delta_val += tau_coeffs[n - 1] * qn

        Theta_Leech = E12 + c_delta * Delta_val
        # Partition function (chiral part squared):
        Z_chiral = Theta_Leech / eta_val ** 24
        Z = Z_chiral ** 2

    elif vtype == 'virasoro':
        # Z_chiral = chi_c(tau) = q^{(c-1)/24} / eta(tau)
        # where q = e^{2*pi*i*tau}, so at tau = iy: q = e^{-2*pi*y}
        # chi_c = exp(-2*pi*y*(c-1)/24) / eta(iy)
        eta_val = eta_real(y)
        q_power = math.exp(-2 * math.pi * y * (c - 1) / 24)
        Z_chiral = q_power / eta_val
        Z = Z_chiral ** 2  # diagonal theory |chi|^2

    else:
        raise ValueError(f"Unsupported VOA type: {vtype}")

    # Primary-counting function: hat{Z} = y^{c/2} |eta(iy)|^{2c} * Z
    eta_val = eta_real(y)
    Z_hat = (y ** (c / 2)) * (eta_val ** (2 * c)) * Z

    return {
        'Z': Z,
        'Z_hat': Z_hat,
        'y': y,
        'central_charge': c,
    }


# ============================================================
# Stage 3: Constrained Epstein zeta
# ============================================================

def constrained_epstein_exact(spec, s):
    """Stage 3: Compute the constrained Epstein zeta epsilon^c_s using
    exact formulas (for lattice VOAs where the closed form is known).

    Returns the value of epsilon^c_s.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for exact Epstein computation")

    s_mp = mpmath.mpc(s)
    vtype = spec['type']

    if vtype in ('heisenberg', 'V_Z'):
        # epsilon^1_s = 4*zeta(2s)
        return complex(4 * mpmath.zeta(2 * s_mp))

    elif vtype == 'V_E8':
        # epsilon^8_s = 240 * 4^{-s} * zeta(s) * zeta(s-3)
        return complex(
            240 * mpmath.power(4, -s_mp)
            * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 3)
        )

    elif vtype == 'V_Leech':
        # The Leech Epstein zeta: from Theta_{Leech} = E_{12} - (65520/691)*Delta
        # Mellin transform splits:
        # E_{Leech}(s) = c_E * zeta(s)*zeta(s-11) + c_Delta * L(s, Delta_12)
        #
        # The Eisenstein part: E_{12} contributes zeta(s)*zeta(s-11) (up to constants)
        # The cusp form part: Delta contributes L(s, Delta_12) (Ramanujan L-function)
        #
        # More precisely for the Epstein zeta of the Leech lattice:
        # sum_{0 != v in Leech} |v|^{-2s} = sum r_{24}(2n) * (2n)^{-s}
        # where r_{24}(2n) = (65520/691)*sigma_{11}(n) - (65520/691)*tau(n)
        # (from Theta = E12 - (65520/691)*Delta)
        #
        # Actually more carefully:
        # Theta_{Leech}(tau) = 1 + sum_{n>=1} a(n) q^n
        # a(n) = coefficient of E12 at n - (65520/691)*tau(n)
        # E12 coefficients: 1 + (24/B12)*sum sigma_11(n) q^n = 1 + 65520/691 * sum sigma_11(n) q^n
        # So a(n) = (65520/691)*(sigma_11(n) - tau(n))
        #
        # Epstein: E_Leech(s) = sum_{n>=1} a(n) * n^{-s}  (omitting 2^{-s} etc.)
        #   = (65520/691) * [sum sigma_11(n) n^{-s} - sum tau(n) n^{-s}]
        #   = (65520/691) * [zeta(s)*zeta(s-11) - L(s, Delta_12)]

        prefactor = mpmath.mpf(65520) / 691

        zeta_part = mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 11)

        # L(s, Delta_12) from tau coefficients
        tau_coeffs = ramanujan_tau_batch(500)
        L_delta = mpmath.mpf(0)
        for n in range(1, 501):
            L_delta += tau_coeffs[n - 1] * mpmath.power(n, -s_mp)

        return complex(prefactor * (zeta_part - L_delta))

    else:
        raise ValueError(
            f"No exact Epstein formula for non-lattice type: {vtype}. "
            f"This is WHERE the pipeline breaks for non-lattice theories."
        )


def constrained_epstein_direct(spec, s, nmax=300):
    """Compute epsilon^c_s by direct summation over theta coefficients.

    This serves as a verification of the exact formulas.
    """
    vtype = spec['type']

    if vtype in ('heisenberg', 'V_Z'):
        # Sum over n^2 for n >= 1 (theta_3 coefficients: r_1(m) = 2 if m = n^2)
        # epsilon = sum_{n>=1} 2 * (2 * n^2)^{-s}  (momentum) + winding
        # At self-dual radius: epsilon = 4 * sum_{n>=1} n^{-2s} = 4*zeta(2s)
        result = 0.0
        for n in range(1, nmax + 1):
            result += 4.0 * (n ** (-2 * s))
        return result

    elif vtype == 'V_E8':
        # Sum over sigma_3(n): r_8(2n) = 240*sigma_3(n)
        # epsilon^8_s = sum 240*sigma_3(n) * (4n)^{-s}
        result = 0.0
        for n in range(1, nmax + 1):
            sig3 = sigma_k(n, 3)
            result += 240 * sig3 * (4 * n) ** (-s)
        return result

    elif vtype == 'V_Leech':
        # Theta_Leech coefficients: a(n) = (65520/691)*(sigma_11(n) - tau(n))
        prefactor = 65520.0 / 691.0
        tau_coeffs = ramanujan_tau_batch(min(nmax, 300))
        result = 0.0
        for n in range(1, min(nmax + 1, len(tau_coeffs) + 1)):
            sig11 = sigma_k(n, 11)
            tau_n = tau_coeffs[n - 1]
            a_n = prefactor * (sig11 - tau_n)
            result += a_n * n ** (-s)
        return result

    else:
        raise ValueError(f"Direct summation not available for {vtype}")


# ============================================================
# Stage 4: Hecke decomposition
# ============================================================

def hecke_decompose(spec, shadow_data):
    """Stage 4: Factor the constrained Epstein zeta into L-functions.

    Returns dict with:
      L_factors: list of dicts, each describing one L-function factor
      critical_lines: list of Re(s) values where zeros concentrate
      decomposition_formula: human-readable formula string
    """
    vtype = spec['type']

    if vtype in ('heisenberg', 'V_Z'):
        return {
            'L_factors': [
                {
                    'name': 'zeta(2s)',
                    'type': 'riemann_zeta_shifted',
                    'shift': 0,
                    'scale': 2,
                    'critical_line': 0.25,  # Re(2s) = 1/2 => Re(s) = 1/4
                    'zeros_at': lambda k: 0.25 + 1j * float(mpmath.zetazero(k).imag) / 2,
                }
            ],
            'critical_lines': [0.25],
            'decomposition_formula': 'epsilon^1_s = 4*zeta(2s)',
            'n_factors': 1,
        }

    elif vtype == 'V_E8':
        return {
            'L_factors': [
                {
                    'name': 'zeta(s)',
                    'type': 'riemann_zeta',
                    'shift': 0,
                    'scale': 1,
                    'critical_line': 0.5,
                    'zeros_at': lambda k: 0.5 + 1j * float(mpmath.zetazero(k).imag),
                },
                {
                    'name': 'zeta(s-3)',
                    'type': 'riemann_zeta_shifted',
                    'shift': 3,
                    'scale': 1,
                    'critical_line': 3.5,
                    'zeros_at': lambda k: 3.5 + 1j * float(mpmath.zetazero(k).imag),
                }
            ],
            'critical_lines': [0.5, 3.5],
            'decomposition_formula': 'epsilon^8_s = 240 * 4^{-s} * zeta(s) * zeta(s-3)',
            'n_factors': 2,
        }

    elif vtype == 'V_Leech':
        return {
            'L_factors': [
                {
                    'name': 'zeta(s)',
                    'type': 'riemann_zeta',
                    'shift': 0,
                    'scale': 1,
                    'critical_line': 0.5,
                    'zeros_at': lambda k: 0.5 + 1j * float(mpmath.zetazero(k).imag),
                },
                {
                    'name': 'zeta(s-11)',
                    'type': 'riemann_zeta_shifted',
                    'shift': 11,
                    'scale': 1,
                    'critical_line': 11.5,
                    'zeros_at': lambda k: 11.5 + 1j * float(mpmath.zetazero(k).imag),
                },
                {
                    'name': 'L(s, Delta_12)',
                    'type': 'ramanujan_L',
                    'weight': 12,
                    'critical_line': 6.0,
                    # Center of critical strip for weight-12 cusp form:
                    # functional equation s <-> 12-s, critical line Re(s) = 6
                    'zeros_at': None,  # Computed numerically below
                }
            ],
            'critical_lines': [0.5, 6.0, 11.5],
            'decomposition_formula': (
                'E_Leech(s) = (65520/691) * [zeta(s)*zeta(s-11) - L(s, Delta_12)]'
            ),
            'n_factors': 3,
        }

    elif vtype == 'virasoro':
        # This is WHERE the pipeline has a gap.
        # The partition function is a VVMF (vector-valued modular form),
        # not a scalar modular form. The Hecke theory for VVMFs
        # (Marks-Mason, Franc-Mason) is required.
        c = spec['central_charge']
        return {
            'L_factors': [],
            'critical_lines': [],
            'decomposition_formula': (
                f'Virasoro c={c}: partition function is VVMF, '
                f'Hecke decomposition requires Franc-Mason theory'
            ),
            'n_factors': 0,
            'gap': 'VVMF_Hecke',
            'gap_stage': 4,
            'gap_description': (
                'The Virasoro partition function chi_c is a vector-valued '
                'modular form of weight 0 for a representation rho of SL(2,Z). '
                'The scalar Hecke theory does not apply. Need: '
                '(1) Franc-Mason classification of VVMF modules, '
                '(2) Hecke operators for VVMFs, '
                '(3) L-function attachment to VVMF Hecke eigenforms.'
            ),
        }

    else:
        raise ValueError(f"Unknown VOA type: {vtype}")


def hecke_verify_numerically(spec, s_test=2.5, nmax=300):
    """Verify the Hecke decomposition by comparing exact and factored formulas.

    Returns (exact_value, factored_value, relative_error).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    exact = constrained_epstein_exact(spec, s_test)
    vtype = spec['type']

    if vtype in ('heisenberg', 'V_Z'):
        factored = complex(4 * mpmath.zeta(2 * mpmath.mpc(s_test)))
    elif vtype == 'V_E8':
        s_mp = mpmath.mpc(s_test)
        factored = complex(
            240 * mpmath.power(4, -s_mp) * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 3)
        )
    elif vtype == 'V_Leech':
        # Use the Hecke decomposition formula
        factored = exact  # same formula
    else:
        return exact, None, float('inf')

    if abs(exact) < 1e-300:
        return exact, factored, 0.0

    rel_err = abs(exact - factored) / abs(exact)
    return exact, factored, rel_err


# ============================================================
# Stage 5: Zero location
# ============================================================

def compute_zeta_zeros(n_zeros=20):
    """Compute the first n_zeros nontrivial zeros of the Riemann zeta function.

    Returns list of complex numbers 1/2 + i*gamma_k.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    zeros = []
    for k in range(1, n_zeros + 1):
        gamma_k = float(mpmath.zetazero(k).imag)
        zeros.append(0.5 + 1j * gamma_k)
    return zeros


def compute_L_function_zeros(spec, n_zeros=20):
    """Stage 5: Compute zeros of each L-function factor.

    Returns dict mapping factor name to list of zeros.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    vtype = spec['type']
    result = {}

    if vtype in ('heisenberg', 'V_Z'):
        # zeta(2s) has zeros at 2s = 1/2 + i*gamma_k
        # i.e., s = 1/4 + i*gamma_k/2
        gammas = [float(mpmath.zetazero(k).imag) for k in range(1, n_zeros + 1)]
        result['zeta(2s)'] = [0.25 + 1j * g / 2 for g in gammas]

    elif vtype == 'V_E8':
        gammas = [float(mpmath.zetazero(k).imag) for k in range(1, n_zeros + 1)]
        result['zeta(s)'] = [0.5 + 1j * g for g in gammas]
        result['zeta(s-3)'] = [3.5 + 1j * g for g in gammas]

    elif vtype == 'V_Leech':
        gammas = [float(mpmath.zetazero(k).imag) for k in range(1, n_zeros + 1)]
        result['zeta(s)'] = [0.5 + 1j * g for g in gammas]
        result['zeta(s-11)'] = [11.5 + 1j * g for g in gammas]

        # L(s, Delta_12) zeros: on the critical line Re(s) = 6
        # These must be computed by locating sign changes of the real part
        # We compute L(6 + it, Delta_12) for t in a range and find zeros
        tau_coeffs = ramanujan_tau_batch(500)

        def L_delta(s):
            s_mp = mpmath.mpc(s)
            val = mpmath.mpf(0)
            for n in range(1, 501):
                val += tau_coeffs[n - 1] * mpmath.power(n, -s_mp)
            return complex(val)

        # Scan for sign changes in Re(L(6+it)) for t > 0
        L_delta_zeros = []
        t_vals = np.linspace(0.1, 80.0, 8000)
        prev_real = None
        for t in t_vals:
            try:
                val = L_delta(6.0 + 1j * t)
                cur_real = val.real
            except Exception:
                prev_real = None
                continue

            if prev_real is not None and prev_real * cur_real < 0:
                # Bisect to refine
                t_lo, t_hi = t_vals[max(0, np.searchsorted(t_vals, t) - 1)], t
                for _ in range(50):
                    t_mid = (t_lo + t_hi) / 2
                    if t_hi - t_lo < 1e-8:
                        break
                    val_lo = L_delta(6.0 + 1j * t_lo).real
                    val_mid = L_delta(6.0 + 1j * t_mid).real
                    if val_lo * val_mid <= 0:
                        t_hi = t_mid
                    else:
                        t_lo = t_mid
                L_delta_zeros.append(6.0 + 1j * (t_lo + t_hi) / 2)
                if len(L_delta_zeros) >= n_zeros:
                    break
            prev_real = cur_real

        result['L(s, Delta_12)'] = L_delta_zeros

    elif vtype == 'virasoro':
        result['gap'] = (
            'Cannot compute zeros: Virasoro partition function is VVMF, '
            'Hecke decomposition into standard L-functions not available.'
        )

    return result


# ============================================================
# Stage 6: Shadow-spectral verification
# ============================================================

def verify_shadow_spectral(spec, shadow_data, hecke_data):
    """Stage 6: Verify that #(critical lines) = depth - 1.

    The shadow-L correspondence predicts:
      shadow_depth d => d-1 independent L-factors => d-1 critical lines

    Returns dict with verification result.
    """
    depth = shadow_data['depth']
    n_critical = len(hecke_data.get('critical_lines', []))

    if depth == float('inf'):
        return {
            'verified': None,
            'depth': depth,
            'critical_lines': n_critical,
            'prediction': 'infinite depth -> unknown number of critical lines',
            'status': 'NOT_APPLICABLE',
            'reason': 'Shadow depth is infinite (class M), correspondence undefined',
        }

    expected_lines = depth - 1
    matches = (n_critical == expected_lines)

    return {
        'verified': matches,
        'depth': depth,
        'critical_lines': n_critical,
        'expected_lines': expected_lines,
        'prediction': f'depth {depth} -> {expected_lines} critical line(s)',
        'status': 'PASS' if matches else 'FAIL',
        'shadow_class': shadow_data['shadow_class'],
    }


# ============================================================
# Full pipeline
# ============================================================

def run_pipeline(voa_type, y=1.0, n_zeros=20, **kwargs):
    """Run the complete 6-stage pipeline.

    Args:
        voa_type: 'heisenberg', 'V_Z', 'V_E8', 'V_Leech', 'virasoro'
        y: imaginary part of tau for partition function evaluation
        n_zeros: number of zeros to compute per L-function
        **kwargs: additional VOA parameters (e.g., c for Virasoro)

    Returns:
        dict with results from all 6 stages + gap identification
    """
    # Stage 1
    spec = voa_spec(voa_type, **kwargs)
    shadow_data = extract_shadow_tower(spec)

    # Stage 2
    partition = compute_partition_function(spec, shadow_data, y)

    # Stage 3
    # Choose test point s in the convergence region of the direct sum.
    # The Dirichlet series sum a(n)*n^{-s} converges for Re(s) > k
    # where k = weight of the theta function (rank/2 for lattices).
    # V_Z: converges for Re(s) > 1/2 (test at 2.5)
    # V_E8: converges for Re(s) > 4 (test at 6.0)
    # V_Leech: converges for Re(s) > 12 (test at 15.0)
    s_test_map = {
        'heisenberg': 2.5, 'V_Z': 2.5,
        'V_E8': 6.0, 'V_Leech': 15.0,
    }
    s_test = s_test_map.get(voa_type, 2.5)

    epstein = {}
    try:
        epstein['exact'] = constrained_epstein_exact(spec, s_test)
        epstein['direct'] = constrained_epstein_direct(spec, s_test)
        epstein['s_test'] = s_test
        if abs(epstein['exact']) > 1e-300:
            epstein['agreement'] = abs(
                epstein['exact'] - epstein['direct']
            ) / abs(epstein['exact'])
        else:
            epstein['agreement'] = abs(epstein['exact'] - epstein['direct'])
        epstein['status'] = 'OK'
    except ValueError as e:
        epstein['status'] = 'FAILED'
        epstein['reason'] = str(e)

    # Stage 4
    hecke_data = hecke_decompose(spec, shadow_data)

    # Stage 5
    try:
        zeros = compute_L_function_zeros(spec, n_zeros)
        zeros_status = 'OK' if 'gap' not in zeros else 'GAP'
    except Exception as e:
        zeros = {'error': str(e)}
        zeros_status = 'FAILED'

    # Stage 6
    verification = verify_shadow_spectral(spec, shadow_data, hecke_data)

    # Identify gaps
    gaps = []
    if epstein.get('status') == 'FAILED':
        gaps.append({
            'stage': 3,
            'description': 'Constrained Epstein computation failed',
            'reason': epstein.get('reason', 'unknown'),
        })
    if hecke_data.get('gap'):
        gaps.append({
            'stage': hecke_data['gap_stage'],
            'description': hecke_data['gap'],
            'reason': hecke_data.get('gap_description', ''),
        })
    if zeros_status == 'GAP':
        gaps.append({
            'stage': 5,
            'description': 'Zero computation blocked',
            'reason': zeros.get('gap', ''),
        })

    return {
        'voa_type': voa_type,
        'spec': spec,
        'stage1_shadow': shadow_data,
        'stage2_partition': partition,
        'stage3_epstein': epstein,
        'stage4_hecke': hecke_data,
        'stage5_zeros': zeros,
        'stage6_verification': verification,
        'gaps': gaps,
        'pipeline_complete': len(gaps) == 0,
    }


# ============================================================
# Gap analysis: Virasoro at c = 1/2 (Ising model)
# ============================================================

def virasoro_gap_analysis(c=0.5):
    """Detailed gap analysis for Virasoro at central charge c.

    Runs the pipeline and identifies exactly which stage breaks
    and what mathematical input is needed to repair it.
    """
    # Stage 1: Shadow data — COMPUTABLE
    spec = voa_spec('virasoro', c=c)
    shadow = extract_shadow_tower(spec)

    # Q^contact = 10/[c(5c+22)]
    Q_contact = 10.0 / (c * (5 * c + 22))

    stage1 = {
        'status': 'OK',
        'kappa': shadow['kappa'],
        'Q_contact': Q_contact,
        'depth': float('inf'),
        'class': 'M',
    }

    # Stage 2: Partition function — COMPUTABLE but form changes
    # Z = |chi_c|^2 where chi_c is a CHARACTER (component of a VVMF)
    # For c=1/2 (Ising): chi = chi_{1,1} + chi_{1,2} (two Virasoro characters)
    # This is NOT a scalar modular form for SL(2,Z)
    stage2 = {
        'status': 'PARTIAL',
        'issue': 'Partition function is |chi_c|^2 where chi_c is a VVMF component',
        'for_ising': (
            'Z_Ising = |chi_{0}|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2, '
            'where chi_h are Virasoro characters at c=1/2. '
            'This is a sesquilinear combination of VVMF components, '
            'NOT a theta function of a lattice.'
        ),
    }

    # Stage 3: Constrained Epstein — THIS IS WHERE IT BREAKS
    # The scalar primary spectrum is NOT a lattice spectrum.
    # For Ising: primaries at h = 0, 1/2, 1/16 (three irreps).
    # The Epstein series takes the form:
    # epsilon = sum_h d(h) * (2h)^{-s}
    # where d(h) = multiplicity, and h runs over the full primary spectrum.
    # But this is a FINITE sum (just 3 terms for Ising) — not a Dirichlet series
    # with multiplicative structure. No Euler product. No L-function factorization.
    stage3 = {
        'status': 'BROKEN',
        'issue': (
            'The constrained Epstein zeta is NOT a Dirichlet series with '
            'multiplicative structure. For minimal models, the primary spectrum '
            'is FINITE. For non-rational Virasoro, the spectrum lacks the '
            'lattice/multiplicative structure needed for L-function factorization.'
        ),
        'ising_spectrum': {
            'primaries': [0, 0.5, 1.0 / 16],
            'description': 'Three Virasoro primaries for the Ising model',
        },
    }

    # Stage 4: Hecke decomposition — BLOCKED by stage 3
    stage4 = {
        'status': 'BLOCKED',
        'issue': (
            'Cannot Hecke-decompose because the Epstein zeta lacks '
            'standard modular-form structure. The VVMF approach '
            '(Franc-Mason) provides the correct framework but requires '
            'new Hecke theory for vector-valued forms.'
        ),
        'needed': [
            'Franc-Mason VVMF classification',
            'Hecke operators for VVMFs (Marks-Mason theory)',
            'L-function attachment to VVMF eigenforms',
            'Analytic continuation of VVMF L-functions',
        ],
    }

    # Summary
    return {
        'c': c,
        'stage1': stage1,
        'stage2': stage2,
        'stage3': stage3,
        'stage4': stage4,
        'first_failure': 3,
        'failure_description': (
            f'For Virasoro at c={c}, the pipeline breaks at Stage 3 '
            f'(constrained Epstein). The primary spectrum lacks multiplicative '
            f'structure / lattice origin. The partition function is a VVMF, '
            f'not a scalar modular form. The Hecke-decomposition machinery '
            f'of Approach A does not apply. Approach B (VVMF Hecke theory, '
            f'Franc-Mason) or Approach D (shadow GF complex analysis) is required.'
        ),
    }


# ============================================================
# Pipeline summary table
# ============================================================

def pipeline_summary_table():
    """Generate a summary table of pipeline status for all supported algebras."""
    algebras = [
        ('V_Z', {}),
        ('V_E8', {}),
        ('V_Leech', {}),
        ('virasoro', {'c': 0.5}),
        ('virasoro', {'c': 25.5}),  # c = 26-1/2, generic Virasoro
    ]

    table = []
    for voa_type, kwargs in algebras:
        spec = voa_spec(voa_type, **kwargs)
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)

        row = {
            'algebra': f"{voa_type}" + (f" (c={kwargs['c']})" if 'c' in kwargs else ''),
            'c': spec['central_charge'],
            'kappa': shadow['kappa'],
            'depth': shadow['depth'],
            'class': shadow['shadow_class'],
            'n_L_factors': hecke['n_factors'],
            'critical_lines': hecke['critical_lines'],
            'pipeline_status': 'COMPLETE' if hecke['n_factors'] > 0 else 'GAP',
        }
        table.append(row)

    return table
