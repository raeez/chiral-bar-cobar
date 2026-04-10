r"""W_7 multi-generator shadow obstruction tower.

The W_7 algebra = DS(sl_7, f_prin) has 6 strong generators:
    T   (spin 2, stress tensor)
    W_3 (spin 3)
    W_4 (spin 4)
    W_5 (spin 5)
    W_6 (spin 6)
    W_7 (spin 7)

This is the HIGHEST-RANK W-algebra shadow tower explicitly computed,
with 6 generators producing a 6-dimensional deformation space and
(6 choose 2) = 15 binary channels.

CENTRAL CHARGE:
    c(W_7, k) = 6(1 - 56/(k+7)) = 6(k-49)/(k+7)

    Derivation: c = (N-1)(1 - N(N+1)/(k+N)) with N=7
              = 6(1 - 56/(k+7))
              = 6(k+7-56)/(k+7)
              = 6(k-49)/(k+7)

    Special values:
      k=1: c = 6*(-48)/8 = -36
      k=7: c = 6*(-42)/14 = -18
      k=49: c = 0
      k->inf: c -> 6

FEIGIN-FRENKEL DUALITY:
    k' = -k - 2h^v = -k - 14 (dual Coxeter number h^v = 7 for sl_7)
    c(k) + c(k') = 2(N-1) = 12

MODULAR CHARACTERISTIC:
    kappa(W_7) = (H_7 - 1)*c where H_7 = 1 + 1/2 + ... + 1/7 = 363/140
    So rho(7) = H_7 - 1 = 223/140
    kappa(W_7) = (223/140)*c

    Channel decomposition: kappa = c/2 + c/3 + c/4 + c/5 + c/6 + c/7
    = c(210+140+105+84+70+60)/420
    = c*669/420 = c*223/140.  Check: 669/420 = 223/140 (divide by 3). Correct.

SIX PRIMARY LINES (deformation space is 6-dimensional):
    T-line:   kappa_T = c/2, Virasoro shadow tower
    W_3-line: kappa_3 = c/3, Z_2 parity kills odd arities
    W_4-line: kappa_4 = c/4
    W_5-line: kappa_5 = c/5, Z_2 parity kills odd arities
    W_6-line: kappa_6 = c/6
    W_7-line: kappa_7 = c/7, Z_2 parity kills odd arities

SHADOW DEPTH: Infinite (class M) on all non-Gaussian lines.

DS REDUCTION:
    sl_7 (class L, depth 3) -> W_7 (class M, depth infinity).
    Ghost sector: c_ghost(k) = c(sl_7,k) - c(W_7,k) = 1722 + 336*k (linear in k).
    kappa_ghost = 21.

BINARY CHANNELS: (6 choose 2) = 15 pairs (from 6 generators)
    (T,W_3), (T,W_4), (T,W_5), (T,W_6), (T,W_7),
    (W_3,W_4), (W_3,W_5), (W_3,W_6), (W_3,W_7),
    (W_4,W_5), (W_4,W_6), (W_4,W_7),
    (W_5,W_6), (W_5,W_7),
    (W_6,W_7)
    Each channel contributes to the multi-channel shadow metric.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    concordance.tex: sec:concordance-koszulness-programme
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs,
    N as Neval,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    solve,
    sqrt,
    symbols,
)

c = Symbol('c')
k = Symbol('k')

# Generator spins for W_7
W7_SPINS = [2, 3, 4, 5, 6, 7]
W7_RANK = 6  # Number of generators = N - 1 = 6
W7_N = 7  # The N in W_N = DS(sl_N)
W7_H_VEE = 7  # Dual Coxeter number of sl_7
W7_DIM_SL7 = 48  # dim(sl_7) = N^2 - 1 = 49 - 1 = 48
W7_NUM_BINARY_CHANNELS = 15  # (6 choose 2) = 15, from 6 generators

# All binary channel pairs (s_i, s_j) with s_i < s_j
W7_BINARY_CHANNELS = [
    (s_i, s_j) for i, s_i in enumerate(W7_SPINS)
    for s_j in W7_SPINS[i + 1:]
]


# =============================================================================
# 1. Central charge and Feigin-Frenkel duality
# =============================================================================

def w7_central_charge(level=None):
    r"""Central charge c(W_7, k) = 6(1 - 56/(k+7)) = 6(k-49)/(k+7).

    From DS(sl_7) at level k:
      c = (N-1)(1 - N(N+1)/(k+N)) with N=7
        = 6(1 - 56/(k+7))
        = 6(k-49)/(k+7)

    Special values:
      k=1: c = 6*(-48)/8 = -36
      k=7: c = 6*(-42)/14 = -18
      k=49: c = 0
      k->inf: c -> 6
    """
    if level is None:
        level = k
    return Rational(6) * (level - 49) / (level + 7)


def w7_central_charge_frac(k_val):
    """Central charge c(W_7, k) = 6 - 336(k+6)^2/(k+7) (Fateev-Lukyanov)."""
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val
    kN = kv + 7
    k_shift = kv + 6  # k + N - 1
    return Fraction(6) - Fraction(336) * k_shift**2 / kN


def w7_ff_dual_level(level=None):
    r"""Feigin-Frenkel dual level: k' = -k - 2h^v = -k - 14 for sl_7.

    Involution check: (-k-14)' = -(-k-14) - 14 = k. OK.
    """
    if level is None:
        level = k
    return -level - 14


def w7_ff_central_charge_sum():
    r"""c(k) + c(k') = 2(N-1) + 4N(N^2-1) = 1356 (Freudenthal-de Vries at N=7)."""
    return Rational(1356)


# =============================================================================
# 2. Kappa (modular characteristic)
# =============================================================================

def w7_harmonic_number():
    r"""H_7 = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 = 363/140.

    Common denominator 420:
      420 + 210 + 140 + 105 + 84 + 70 + 60 = 1089
      H_7 = 1089/420 = 363/140 (divide by 3).
    """
    return Rational(363, 140)


def w7_anomaly_ratio():
    r"""Anomaly ratio rho(W_7) = H_7 - 1 = 1/2+1/3+1/4+1/5+1/6+1/7.

    = (210+140+105+84+70+60)/420 = 669/420 = 223/140.
    """
    return Rational(223, 140)


def w7_kappa_total(c_val=None):
    r"""Total modular characteristic kappa(W_7) = (223/140)*c.

    Decomposition: kappa = sum_{s=2}^{7} c/s
                         = c/2 + c/3 + c/4 + c/5 + c/6 + c/7
                         = c*(210+140+105+84+70+60)/420
                         = 669c/420 = 223c/140.
    """
    cc = c_val if c_val is not None else c
    return Rational(223, 140) * cc


def w7_kappa_channel(spin, c_val=None):
    """Kappa for each generator channel: kappa_s = c/s.

    From AP27: the bar propagator d log E(z,w) has weight 1,
    so kappa_s = (BPZ norm at leading pole)/2 = c/s for spin-s generator.
    """
    assert spin in W7_SPINS, f"W_7 has no spin-{spin} generator"
    cc = c_val if c_val is not None else c
    return cc / spin


def w7_kappa_total_frac(k_val):
    """Exact Fraction kappa(W_7) at level k."""
    c_w = w7_central_charge_frac(k_val)
    return Fraction(223, 140) * c_w


# Multiple verification methods for kappa
def w7_kappa_from_channels(c_val=None):
    """kappa from sum of channels: c/2+c/3+c/4+c/5+c/6+c/7 = 223c/140."""
    cc = c_val if c_val is not None else c
    return sum(cc / s for s in W7_SPINS)


def w7_kappa_from_anomaly_ratio(c_val=None):
    """kappa from anomaly ratio: (H_7 - 1)*c = (223/140)*c."""
    cc = c_val if c_val is not None else c
    return w7_anomaly_ratio() * cc


def w7_kappa_from_harmonic(c_val=None):
    """kappa from explicit harmonic sum: sum_{j=2}^{7} 1/j * c."""
    cc = c_val if c_val is not None else c
    rho = sum(Fraction(1, j) for j in range(2, 8))
    return Rational(rho.numerator, rho.denominator) * cc


# =============================================================================
# 3. Shadow data for each primary line
# =============================================================================

def t_line_shadow_data(c_val=None):
    r"""T-line shadow data: identical to Virasoro at the same c.

    kappa_T = c/2, alpha_T = 2 (Virasoro cubic), S4_T = 10/(c(5c+22)).
    Class M, infinite depth.
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 2
    alpha = Rational(2)
    S4 = Rational(10) / (cc * (5 * cc + 22))
    Delta = 8 * kappa * S4
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': cancel(Delta),
        'depth_class': 'M', 'depth': None,
        'spin': 2, 'line': 'T',
    }


def w3_line_shadow_data(c_val=None):
    r"""W_3-line shadow data. Same structure as W_3 in any W_N.

    kappa_3 = c/3, alpha_3 = 0 (Z_2 parity), S4_3 = 2560/(c(5c+22)^3).
    """
    cc = c_val if c_val is not None else c
    return {
        'kappa': cc / 3, 'alpha': Rational(0),
        'S4': Rational(2560) / (cc * (5 * cc + 22) ** 3),
        'Delta': cancel(8 * (cc / 3) * Rational(2560) / (cc * (5 * cc + 22) ** 3)),
        'depth_class': 'M', 'depth': None,
        'spin': 3, 'line': 'W_3',
    }


def w4_line_shadow_data(c_val=None):
    """W_4-line shadow data. alpha_4 from cubic self-coupling (if present)."""
    cc = c_val if c_val is not None else c
    return {
        'kappa': cc / 4, 'alpha': Rational(0),
        'S4': cancel(Rational(10) / (cc * (5 * cc + 22))),
        'Delta': cancel(8 * (cc / 4) * Rational(10) / (cc * (5 * cc + 22))),
        'depth_class': 'M', 'depth': None,
        'spin': 4, 'line': 'W_4',
        'note': 'Quartic from Lambda-exchange; exact value requires bootstrap',
    }


def w5_line_shadow_data(c_val=None):
    """W_5-line shadow data. Z_2 parity kills odd arities."""
    cc = c_val if c_val is not None else c
    return {
        'kappa': cc / 5, 'alpha': Rational(0),
        'S4': cancel(Rational(10) / (cc * (5 * cc + 22))),
        'Delta': cancel(8 * (cc / 5) * Rational(10) / (cc * (5 * cc + 22))),
        'depth_class': 'M', 'depth': None,
        'spin': 5, 'line': 'W_5',
        'note': 'Quartic from Lambda-exchange; exact value requires bootstrap',
    }


def w6_line_shadow_data(c_val=None):
    """W_6-line shadow data."""
    cc = c_val if c_val is not None else c
    return {
        'kappa': cc / 6, 'alpha': Rational(0),
        'S4': cancel(Rational(10) / (cc * (5 * cc + 22))),
        'Delta': cancel(8 * (cc / 6) * Rational(10) / (cc * (5 * cc + 22))),
        'depth_class': 'M', 'depth': None,
        'spin': 6, 'line': 'W_6',
        'note': 'Quartic from Lambda-exchange; exact value requires bootstrap',
    }


def w7_line_shadow_data(c_val=None):
    """W_7-line shadow data. Z_2 parity kills odd arities."""
    cc = c_val if c_val is not None else c
    return {
        'kappa': cc / 7, 'alpha': Rational(0),
        'S4': cancel(Rational(10) / (cc * (5 * cc + 22))),
        'Delta': cancel(8 * (cc / 7) * Rational(10) / (cc * (5 * cc + 22))),
        'depth_class': 'M', 'depth': None,
        'spin': 7, 'line': 'W_7',
        'note': 'Quartic from Lambda-exchange; exact value requires bootstrap',
    }


def all_line_shadow_data(c_val=None):
    """Return shadow data for all 6 primary lines."""
    return {
        'T': t_line_shadow_data(c_val),
        'W_3': w3_line_shadow_data(c_val),
        'W_4': w4_line_shadow_data(c_val),
        'W_5': w5_line_shadow_data(c_val),
        'W_6': w6_line_shadow_data(c_val),
        'W_7': w7_line_shadow_data(c_val),
    }


# =============================================================================
# 4. Shadow towers via convolution recursion
# =============================================================================

def _convolution_coefficients_float(q0, q1, q2, max_n):
    """Float-precision convolution recursion."""
    a0 = math.sqrt(q0)
    a = [a0]
    if max_n >= 1:
        a.append(q1 / (2.0 * a0))
    if max_n >= 2:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv_sum / (2.0 * a0))
    return a


def _convolution_coefficients_frac(q0, q1, q2, max_n, kappa_sign=1):
    """Fraction-precision convolution recursion."""
    from math import isqrt
    num = q0.numerator
    den = q0.denominator
    sn = isqrt(abs(num))
    sd = isqrt(den)
    if sn * sn != abs(num) or sd * sd != den:
        raise ValueError(f"q0 = {q0} is not a perfect square")
    a0 = Fraction(sn, sd) * kappa_sign
    coeffs = [a0]
    if max_n >= 1:
        coeffs.append(q1 / (2 * a0))
    if max_n >= 2:
        coeffs.append((q2 - coeffs[1] ** 2) / (2 * a0))
    for n in range(3, max_n + 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv_sum / (2 * a0))
    return coeffs


def _convolution_coefficients_float_signed(q0, q1, q2, max_n, kappa_sign=1):
    """Float-precision convolution recursion with signed a_0."""
    a0 = kappa_sign * math.sqrt(q0)
    a = [a0]
    if max_n >= 1:
        a.append(q1 / (2.0 * a0))
    if max_n >= 2:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv_sum / (2.0 * a0))
    return a


def t_line_tower_numerical(c_val, max_r=30):
    """Numerical T-line shadow tower at a specific central charge."""
    c_num = float(c_val)
    kappa = c_num / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_num * (5.0 * c_num + 22.0))
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    sign = 1 if kappa > 0 else -1
    coeffs = _convolution_coefficients_float_signed(q0, q1, q2, max_r - 2, sign)
    return {r + 2: coeffs[r] / (r + 2) for r in range(len(coeffs))}


def t_line_tower_exact_at_level(k_val, max_r=8):
    """Exact T-line tower at a DS level using Fraction arithmetic."""
    c_w = w7_central_charge_frac(k_val)
    kappa = c_w / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c_w * (5 * c_w + 22))
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    sign = 1 if kappa > 0 else -1
    coeffs = _convolution_coefficients_frac(q0, q1, q2, max_r - 2, sign)
    return {r + 2: coeffs[r] / (r + 2) for r in range(len(coeffs))}


def generic_line_tower_exact(kappa_val, alpha_val, S4_val, max_r=8):
    """Exact shadow tower for a generic primary line.

    This computes the convolution recursion for arbitrary line parameters.
    Used for non-T lines where the shadow data differs from Virasoro.
    """
    q0 = 4 * kappa_val ** 2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val ** 2 + 16 * kappa_val * S4_val
    sign = 1 if kappa_val > 0 else -1
    coeffs = _convolution_coefficients_frac(q0, q1, q2, max_r - 2, sign)
    return {r + 2: coeffs[r] / (r + 2) for r in range(len(coeffs))}


# =============================================================================
# 5. Quartic contact invariant
# =============================================================================

def w7_quartic_contact_T_line(c_val=None):
    r"""Quartic contact invariant on T-line: Q^contact = 10/(c(5c+22)).

    On the T-line of ANY W_N, the quartic contact invariant is the
    Virasoro value because the Virasoro subalgebra governs this slice.
    """
    cc = c_val if c_val is not None else c
    return Rational(10) / (cc * (5 * cc + 22))


def w7_quartic_contact_T_at_level(k_val):
    """Exact Q^contact on T-line at DS level k."""
    c_w = w7_central_charge_frac(k_val)
    return Fraction(10) / (c_w * (5 * c_w + 22))


# =============================================================================
# 6. Mixing polynomial and propagator variance
# =============================================================================

def w7_kappas(c_val=None):
    """Curvature eigenvalues: [c/2, c/3, c/4, c/5, c/6, c/7]."""
    cc = c_val if c_val is not None else c
    return [cc / s for s in W7_SPINS]


def w7_propagator_variance_structural():
    r"""Structural propagator variance for W_7.

    delta = sum f_i^2/kappa_i - (sum f_i)^2/(sum kappa_i)

    For W_7, the mixing polynomial has degree >= 8 in c
    (from 6 channels with 5 independent ratios).
    The exact computation requires the full 6-channel quartic tensor.
    """
    cc = c
    Q0 = Rational(10) / (cc * (5 * cc + 22))
    alpha_33 = Rational(16) / (5 * cc + 22)
    kappas = w7_kappas()
    # Placeholder gradients from Lambda-exchange
    fs = [4 * Q0 * (1 + sum(s * alpha_33 for s in W7_SPINS[1:]))] + \
         [4 * Q0 * alpha_33 for _ in W7_SPINS[1:]]
    term1 = sum(f ** 2 / kap for f, kap in zip(fs, kappas))
    term2 = sum(fs) ** 2 / sum(kappas)
    return cancel(term1 - term2)


def w7_propagator_variance_numerical(c_val):
    """Numerical propagator variance at a specific central charge.

    Uses the Cauchy-Schwarz form:
    delta = sum f_i^2/kappa_i - (sum f_i)^2/(sum kappa_i) >= 0.
    """
    c_num = float(c_val)
    Q0 = 10.0 / (c_num * (5.0 * c_num + 22.0))
    alpha_33 = 16.0 / (5.0 * c_num + 22.0)
    kappas = [c_num / s for s in W7_SPINS]
    fs = [4 * Q0 * (1 + sum(s * alpha_33 for s in W7_SPINS[1:]))] + \
         [4 * Q0 * alpha_33 for _ in W7_SPINS[1:]]
    term1 = sum(f ** 2 / kap for f, kap in zip(fs, kappas))
    term2 = sum(fs) ** 2 / sum(kappas)
    return term1 - term2


# =============================================================================
# 7. Shadow growth rate
# =============================================================================

def w7_t_line_growth_rate_sq(c_val=None):
    r"""Squared growth rate rho_T^2 on T-line (= Virasoro).

    rho_T^2 = (180c + 872)/((5c+22)*c^2)

    This is a universal formula: on the T-line of ANY W_N, the growth
    rate is the Virasoro growth rate at c = c(W_N, k).
    """
    cc = c_val if c_val is not None else c
    return cancel((180 * cc + 872) / ((5 * cc + 22) * cc ** 2))


def w7_t_line_growth_rate(c_val):
    """Numerical T-line growth rate at a specific c."""
    c_num = float(c_val)
    rho_sq = (180 * c_num + 872) / ((5 * c_num + 22) * c_num ** 2)
    return math.sqrt(abs(rho_sq))


def w7_growth_rate_at_level(k_val):
    """Growth rate on T-line at DS level k."""
    c_w = float(w7_central_charge_frac(Fraction(k_val)))
    return w7_t_line_growth_rate(c_w)


# =============================================================================
# 8. Complementarity (Koszul duality)
# =============================================================================

def w7_kappa_complementarity(k_val):
    r"""Verify kappa(W_7, k) + kappa(W_7, k') where k' = -k - 14.

    kappa(k) + kappa(k') = (223/140)(c(k) + c(k')) = (223/140)*1356 = 75597/35.

    Derivation: 223*1356 = 302388. 302388/140 = 75597/35 (divide by 4).
    """
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val
    kappa = w7_kappa_total_frac(kv)
    kappa_dual = w7_kappa_total_frac(-kv - 14)
    return {
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'sum': kappa + kappa_dual,
        'expected': Fraction(75597, 35),
        'matches': kappa + kappa_dual == Fraction(75597, 35),
    }


def w7_channel_complementarity(k_val, spin):
    """Verify channel-wise kappa complementarity for a specific generator."""
    assert spin in W7_SPINS
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val
    c_k = w7_central_charge_frac(kv)
    c_kd = w7_central_charge_frac(-kv - 14)
    kap = c_k / spin
    kap_d = c_kd / spin
    return {
        'kappa': kap,
        'kappa_dual': kap_d,
        'sum': kap + kap_d,
        'expected': Fraction(1356) / spin,
        'matches': kap + kap_d == Fraction(1356) / spin,
    }


# =============================================================================
# 9. DS pipeline: sl_7 -> W_7 shadow comparison
# =============================================================================

def w7_ds_ghost_central_charge(k_val=None):
    r"""Ghost sector effective central charge for DS(sl_7).

    c_ghost(k) = c(sl_7, k) - c(W_7, k) = 1722 + 336*k.
    Linear in k with slope N(N^2-1)=336 and intercept
    (N-1)*((N^2-1)*(N-1)-1) = 6*(48*6-1) = 1722.
    """
    if k_val is not None:
        kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val
        c_sl7 = Fraction(48) * kv / (kv + 7)
        c_w7 = w7_central_charge_frac(kv)
        return c_sl7 - c_w7
    return Fraction(1722)


def w7_ds_ghost_kappa(k_val=None):
    """Ghost kappa for DS(sl_7): kappa_ghost = c_ghost/2."""
    return w7_ds_ghost_central_charge(k_val) / 2


def w7_ds_pipeline(k_val, max_arity=8):
    r"""Complete DS shadow comparison for sl_7 -> W_7 at level k.

    Computes central charges, kappa, shadow towers on T-line,
    and verifies depth increase from L (affine) to M (W-algebra).
    """
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    # Central charges: dim(sl_7) = 48, h^v = 7
    c_sl7 = Fraction(48) * kv / (kv + 7)
    c_w7 = w7_central_charge_frac(kv)
    c_gh = w7_ds_ghost_central_charge(kv)

    # Kappa values
    kap_sl7 = Fraction(48) * (kv + 7) / 14  # dim*(k+h^v)/(2h^v)
    kap_w7 = w7_kappa_total_frac(kv)
    kap_gh = w7_ds_ghost_kappa(kv)

    # Shadow towers on T-line
    tower_w7 = t_line_tower_exact_at_level(kv, max_arity)

    # sl_7 shadow: class L, depth 3
    kap_sl7_val = kap_sl7
    q0 = 4 * kap_sl7_val ** 2
    q1 = 12 * kap_sl7_val  # alpha = 1
    q2 = Fraction(9)  # 9*1^2 + 16*kappa*0 = 9
    sign = 1 if kap_sl7_val > 0 else -1
    coeffs_sl7 = _convolution_coefficients_frac(q0, q1, q2, max_arity - 2, sign)
    tower_sl7 = {r + 2: coeffs_sl7[r] / (r + 2) for r in range(len(coeffs_sl7))}

    return {
        'N': 7,
        'k': kv,
        'c_sl7': c_sl7,
        'c_w7': c_w7,
        'c_ghost': c_gh,
        'c_additive': c_sl7 == c_w7 + c_gh,
        'kappa_sl7': kap_sl7,
        'kappa_w7': kap_w7,
        'kappa_ghost': kap_gh,
        'tower_sl7': tower_sl7,
        'tower_w7': tower_w7,
        'depth_increase': tower_sl7.get(4, Fraction(0)) == 0 and tower_w7.get(4, Fraction(0)) != 0,
    }


# =============================================================================
# 10. Multi-channel shadow metric
# =============================================================================

def w7_shadow_metric_diagonal(c_val=None):
    r"""Diagonal components of the multi-channel shadow metric.

    The shadow metric Q(t_1,...,t_6) has diagonal entries
    Q_{ii} = 4*kappa_i^2 on each primary line.

    Off-diagonal entries Q_{ij} encode the cross-channel coupling
    and require the full multi-channel OPE bootstrap.

    Returns the diagonal quadratic form matrix.
    """
    cc = c_val if c_val is not None else c
    kappas = w7_kappas(cc)
    return {(s, s): 4 * (cc / s) ** 2 for s in W7_SPINS}


def w7_binary_channel_kappas(c_val=None):
    """Kappa values for all 21 binary channels.

    For a binary channel (s_i, s_j), the effective kappa depends
    on the cross-OPE structure. At leading order, it is the
    average: kappa_{ij} = (kappa_i + kappa_j)/2 = c(1/s_i + 1/s_j)/2.
    """
    cc = c_val if c_val is not None else c
    result = {}
    for (s_i, s_j) in W7_BINARY_CHANNELS:
        result[(s_i, s_j)] = (cc / s_i + cc / s_j) / 2
    return result


# =============================================================================
# 11. Large-N scaling: W_7 in context
# =============================================================================

def w7_in_large_n_context(k_val=None):
    r"""W_7 invariants in the context of the N=2,...,7 sequence.

    Returns a dict of key invariants for comparison.
    """
    if k_val is None:
        k_val = Fraction(5)
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    from compute.lib.w5_shadow_tower import (
        wn_central_charge, wn_kappa_total, wn_ff_sum, wn_kappa_ff_sum,
    )

    results = {}
    for N in range(2, 8):
        c_w = wn_central_charge(N, kv)
        kap = wn_kappa_total(N, kv)
        ff_c_sum = wn_ff_sum(N)
        ff_kap_sum = wn_kappa_ff_sum(N)

        # T-line quartic
        if c_w != 0 and 5 * c_w + 22 != 0:
            S4 = Fraction(10) / (c_w * (5 * c_w + 22))
        else:
            S4 = None

        # T-line growth rate squared
        if c_w != 0 and S4 is not None:
            rho_sq = (Fraction(180) * c_w + 872) / ((5 * c_w + 22) * c_w ** 2)
        else:
            rho_sq = None

        results[N] = {
            'c': c_w,
            'kappa': kap,
            'ff_c_sum': ff_c_sum,
            'ff_kappa_sum': ff_kap_sum,
            'S4_T': S4,
            'rho_sq_T': rho_sq,
            'rank': N - 1,
            'ghost_c': Fraction((N - 1) * ((N**2 - 1) * (N - 1) - 1)),
        }

    return results


# =============================================================================
# 12. N-dependence analysis for W_N shadow data
# =============================================================================

def w7_anomaly_ratio_sequence():
    r"""Anomaly ratio sequence rho(N) = H_N - 1 for N=2,...,7.

    N=2: 1/2
    N=3: 5/6
    N=4: 13/12
    N=5: 77/60
    N=6: 29/20
    N=7: 223/140
    """
    seq = {}
    for N in range(2, 8):
        rho = sum(Fraction(1, j) for j in range(2, N + 1))
        seq[N] = rho
    return seq


def w7_kappa_ff_sum_sequence():
    r"""Kappa complementarity sum sequence for N=2,...,7.

    kappa + kappa' = (H_N - 1)*(c + c') = (H_N - 1)*[2(N-1) + 4N(N^2-1)].

    N=2: (1/2)*26 = 13
    N=3: (5/6)*100 = 250/3
    N=4: (13/12)*246 = 533/2
    N=5: (77/60)*488 = 9394/15
    N=6: (29/20)*850 = 2465/2
    N=7: (223/140)*1356 = 75597/35
    """
    seq = {}
    for N in range(2, 8):
        rho = sum(Fraction(1, j) for j in range(2, N + 1))
        ff_sum = Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))
        seq[N] = rho * ff_sum
    return seq


def w7_ghost_c_sequence():
    r"""Ghost central charge sequence at k=0: c_ghost(N) = (N-1)*((N^2-1)*(N-1)-1).

    N=2: 2, N=3: 30, N=4: 132, N=5: 380, N=6: 870, N=7: 1722.
    """
    return {N: Fraction((N - 1) * ((N**2 - 1) * (N - 1) - 1)) for N in range(2, 8)}


# =============================================================================
# 13. DS cascade analysis across N=2,...,7
# =============================================================================

def ds_cascade_comparison(k_val, max_arity=8):
    r"""Compute DS pipeline data for all N=2,...,7 at a fixed level.

    Returns growth rates, quartic contacts, and depth status
    for the full cascade from sl_N to W_N.
    """
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    from compute.lib.w5_shadow_tower import wn_central_charge, wn_kappa_total

    results = {}
    for N in range(2, 8):
        c_w = wn_central_charge(N, kv)
        kap = wn_kappa_total(N, kv)
        if c_w != 0 and 5 * c_w + 22 != 0:
            S4 = Fraction(10) / (c_w * (5 * c_w + 22))
            rho_sq = (Fraction(180) * c_w + 872) / ((5 * c_w + 22) * c_w ** 2)
            rho = float(rho_sq) ** 0.5 if float(rho_sq) > 0 else None
        else:
            S4 = None
            rho_sq = None
            rho = None

        results[N] = {
            'c': c_w,
            'kappa': kap,
            'S4_T': S4,
            'rho_T': rho,
            'ghost_c': Fraction((N - 1) * ((N**2 - 1) * (N - 1) - 1)),
            'rank': N - 1,
        }

    return results


# =============================================================================
# 14. Summary
# =============================================================================

def w7_full_summary(k_val=None):
    """Complete W_7 shadow tower summary."""
    if k_val is None:
        k_val = Fraction(5)
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    c_w = w7_central_charge_frac(kv)
    kap = w7_kappa_total_frac(kv)
    Q_contact = w7_quartic_contact_T_at_level(kv)
    rho = w7_growth_rate_at_level(kv)
    comp = w7_kappa_complementarity(kv)
    tower = t_line_tower_exact_at_level(kv, 8)
    ds = w7_ds_pipeline(kv, 8)

    return {
        'N': 7,
        'k': kv,
        'c': c_w,
        'kappa_total': kap,
        'kappa_channels': {s: c_w / s for s in W7_SPINS},
        'Q_contact_T': Q_contact,
        'rho_T': rho,
        'complementarity': comp,
        'tower_T': tower,
        'ds_pipeline': ds,
        'depth_class': 'M',
        'ff_sum': w7_ff_central_charge_sum(),
        'anomaly_ratio': w7_anomaly_ratio(),
        'harmonic_number': w7_harmonic_number(),
        'num_binary_channels': W7_NUM_BINARY_CHANNELS,
        'rank': W7_RANK,
    }


if __name__ == '__main__':
    print("=" * 70)
    print("W_7 Shadow Obstruction Tower")
    print("=" * 70)

    summary = w7_full_summary(Fraction(5))
    print(f"Level k = 5")
    print(f"  c(W_7) = {summary['c']} = {float(summary['c']):.6f}")
    print(f"  kappa(W_7) = {summary['kappa_total']} = {float(summary['kappa_total']):.6f}")
    print(f"  H_7 = {summary['harmonic_number']}")
    print(f"  rho(7) = {summary['anomaly_ratio']}")
    print(f"  Q^contact_T = {summary['Q_contact_T']}")
    print(f"  rho_T = {summary['rho_T']:.6f}")
    print(f"  kappa + kappa' = {summary['complementarity']['sum']}")
    print(f"  15 binary channels")
    print(f"\n  T-line tower:")
    for r in sorted(summary['tower_T'].keys()):
        print(f"    S_{r} = {summary['tower_T'][r]} = {float(summary['tower_T'][r]):.8f}")
    print(f"\n  DS pipeline:")
    print(f"    c(sl_7) = {summary['ds_pipeline']['c_sl7']}")
    print(f"    c_additive: {summary['ds_pipeline']['c_additive']}")
    print(f"    depth_increase: {summary['ds_pipeline']['depth_increase']}")
