r"""W_6 multi-generator shadow obstruction tower.

The W_6 algebra = DS(sl_6, f_prin) has 5 strong generators:
    T   (spin 2, stress tensor)
    W_3 (spin 3)
    W_4 (spin 4)
    W_5 (spin 5)
    W_6 (spin 6)

This is the MOST COMPLEX W-algebra shadow tower explicitly computed.

CENTRAL CHARGE:
    c(W_6, k) = 5(1 - 42/(k+6)) = 5(k+6-42)/(k+6) = 5(k-36)/(k+6)

FEIGIN-FRENKEL DUALITY:
    k' = -k - 12 (dual Coxeter number h^v = 6 for sl_6)
    c(k) + c(k') = 2(N-1) = 10

MODULAR CHARACTERISTIC:
    κ(W_6) = (H_6 - 1)·c where H_6 = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 = 49/20
    So ρ(6) = H_6 - 1 = 29/20
    κ(W_6) = (29/20)·c

FIVE PRIMARY LINES (deformation space is 5-dimensional):
    T-line:   κ_T = c/2, Virasoro shadow tower
    W_3-line: κ_3 = c/3, Z_2 parity kills odd arities
    W_4-line: κ_4 = c/4
    W_5-line: κ_5 = c/5, Z_2 parity kills odd arities
    W_6-line: κ_6 = c/6

SHADOW DEPTH: Infinite (class M) on all non-Gaussian lines.

DS REDUCTION:
    sl_6 (class L, depth 3) → W_6 (class M, depth ∞).
    Ghost sector: c_ghost = N(N-1) = 30 (level-independent).
    κ_ghost = 15.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
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

# Generator spins for W_6
W6_SPINS = [2, 3, 4, 5, 6]
W6_RANK = 5  # Number of generators = N - 1 = 5


# =============================================================================
# 1. Central charge and Feigin-Frenkel duality
# =============================================================================

def w6_central_charge(level=None):
    r"""Central charge c(W_6, k) = 5(1 - 42/(k+6)) = 5(k-36)/(k+6).

    From DS(sl_6) at level k:
      c = (N-1)(1 - N(N+1)/(k+N)) with N=6
        = 5(1 - 42/(k+6))
        = 5(k-36)/(k+6)

    Special values:
      k=1: c = 5·(-35)/7 = -25
      k=6: c = 5·(-30)/12 = -25/2
      k=36: c = 0
      k→∞: c → 5
    """
    if level is None:
        level = k
    return Rational(5) * (level - 36) / (level + 6)


def w6_central_charge_frac(k_val):
    """Central charge as exact Fraction."""
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val
    return Fraction(5) * (kv - 36) / (kv + 6)


def w6_ff_dual_level(level=None):
    r"""Feigin-Frenkel dual level: k' = -k - 2h^v = -k - 12 for sl_6."""
    if level is None:
        level = k
    return -level - 12


def w6_ff_central_charge_sum():
    r"""c(k) + c(k') = 2(N-1) = 10 under Feigin-Frenkel.

    Verify: c(-k-12) = 5(-k-12-36)/(-k-12+6) = 5(-k-48)/(-k-6) = 5(k+48)/(k+6)
    Sum: 5(k-36)/(k+6) + 5(k+48)/(k+6) = 5·(2k+12)/(k+6) = 10(k+6)/(k+6) = 10. ✓
    """
    return Rational(10)


# =============================================================================
# 2. Kappa (modular characteristic)
# =============================================================================

def w6_anomaly_ratio():
    r"""Anomaly ratio ρ(W_6) = H_6 - 1 = 1/2 + 1/3 + 1/4 + 1/5 + 1/6.

    = 30/60 + 20/60 + 15/60 + 12/60 + 10/60 = 87/60 = 29/20.
    """
    return Rational(29, 20)


def w6_kappa_total(c_val=None):
    r"""Total modular characteristic κ(W_6) = (29/20)·c.

    Decomposition: κ = Σ_{s=2}^{6} c/s = c/2 + c/3 + c/4 + c/5 + c/6
                     = c(30+20+15+12+10)/60 = 87c/60 = 29c/20.
    """
    cc = c_val if c_val is not None else c
    return Rational(29, 20) * cc


def w6_kappa_channel(spin, c_val=None):
    """Kappa for each generator channel: κ_s = c/s."""
    assert spin in W6_SPINS, f"W_6 has no spin-{spin} generator"
    cc = c_val if c_val is not None else c
    return cc / spin


def w6_kappa_total_frac(k_val):
    """Exact Fraction κ(W_6) at level k."""
    c_w = w6_central_charge_frac(k_val)
    return Fraction(29, 20) * c_w


# Multiple verification methods for kappa
def w6_kappa_from_channels(c_val=None):
    """κ from sum of channels: c/2 + c/3 + c/4 + c/5 + c/6 = 29c/20."""
    cc = c_val if c_val is not None else c
    return sum(cc / s for s in W6_SPINS)


def w6_kappa_from_anomaly_ratio(c_val=None):
    """κ from anomaly ratio: (H_6 - 1)·c = (29/20)·c."""
    cc = c_val if c_val is not None else c
    return w6_anomaly_ratio() * cc


# =============================================================================
# 3. Shadow data for each primary line
# =============================================================================

def t_line_shadow_data(c_val=None):
    r"""T-line shadow data: identical to Virasoro at the same c."""
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

    κ_3 = c/3, α_3 = 0 (Z_2 parity), S4_3 = 2560/(c(5c+22)^3).
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
    """W_4-line shadow data. α_4 from cubic self-coupling (if present)."""
    cc = c_val if c_val is not None else c
    return {
        'kappa': cc / 4, 'alpha': Rational(0),
        'S4': cancel(Rational(10) / (cc * (5 * cc + 22))),
        'Delta': cancel(8 * (cc / 4) * Rational(10) / (cc * (5 * cc + 22))),
        'depth_class': 'M', 'depth': None,
        'spin': 4, 'line': 'W_4',
        'note': 'Quartic from Λ-exchange; exact value requires bootstrap',
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
        'note': 'Quartic from Λ-exchange; exact value requires bootstrap',
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
        'note': 'Quartic from Λ-exchange; exact value requires bootstrap',
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
    c_w = w6_central_charge_frac(k_val)
    kappa = c_w / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c_w * (5 * c_w + 22))
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    sign = 1 if kappa > 0 else -1
    coeffs = _convolution_coefficients_frac(q0, q1, q2, max_r - 2, sign)
    return {r + 2: coeffs[r] / (r + 2) for r in range(len(coeffs))}


# =============================================================================
# 5. Quartic contact invariant
# =============================================================================

def w6_quartic_contact_T_line(c_val=None):
    r"""Quartic contact invariant on T-line: Q^contact = 10/(c(5c+22))."""
    cc = c_val if c_val is not None else c
    return Rational(10) / (cc * (5 * cc + 22))


def w6_quartic_contact_T_at_level(k_val):
    """Exact Q^contact on T-line at DS level k."""
    c_w = w6_central_charge_frac(k_val)
    return Fraction(10) / (c_w * (5 * c_w + 22))


# =============================================================================
# 6. Mixing polynomial and propagator variance
# =============================================================================

def w6_kappas(c_val=None):
    """Curvature eigenvalues: [c/2, c/3, c/4, c/5, c/6]."""
    cc = c_val if c_val is not None else c
    return [cc / s for s in W6_SPINS]


def w6_propagator_variance_structural():
    r"""Structural propagator variance for W_6.

    δ = Σ f_i²/κ_i - (Σ f_i)²/(Σ κ_i)

    For W_6, the mixing polynomial has degree ≥ 6 in c
    (from 5 channels with 4 independent ratios).
    The exact computation requires the full 5-channel quartic tensor.
    """
    # The structural estimate uses T-line Virasoro quartic only
    cc = c
    Q0 = Rational(10) / (cc * (5 * cc + 22))
    alpha_33 = Rational(16) / (5 * cc + 22)
    kappas = w6_kappas()
    # Placeholder gradients from Λ-exchange
    fs = [4 * Q0 * (1 + sum(s * alpha_33 for s in W6_SPINS[1:]))] + \
         [4 * Q0 * alpha_33 for _ in W6_SPINS[1:]]
    term1 = sum(f ** 2 / kap for f, kap in zip(fs, kappas))
    term2 = sum(fs) ** 2 / sum(kappas)
    return cancel(term1 - term2)


# =============================================================================
# 7. Shadow growth rate
# =============================================================================

def w6_t_line_growth_rate_sq(c_val=None):
    r"""Squared growth rate ρ_T² on T-line (= Virasoro)."""
    cc = c_val if c_val is not None else c
    return cancel((180 * cc + 872) / ((5 * cc + 22) * cc ** 2))


def w6_t_line_growth_rate(c_val):
    """Numerical T-line growth rate at a specific c."""
    c_num = float(c_val)
    rho_sq = (180 * c_num + 872) / ((5 * c_num + 22) * c_num ** 2)
    return math.sqrt(abs(rho_sq))


def w6_growth_rate_at_level(k_val):
    """Growth rate on T-line at DS level k."""
    c_w = float(w6_central_charge_frac(Fraction(k_val)))
    return w6_t_line_growth_rate(c_w)


# =============================================================================
# 8. Complementarity (Koszul duality)
# =============================================================================

def w6_kappa_complementarity(k_val):
    r"""Verify κ(W_6, k) + κ(W_6, k') where k' = -k - 12.

    κ(k) + κ(k') = (29/20)(c(k) + c(k')) = (29/20)·10 = 29/2.
    """
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val
    kappa = w6_kappa_total_frac(kv)
    kappa_dual = w6_kappa_total_frac(-kv - 12)
    return {
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'sum': kappa + kappa_dual,
        'expected': Fraction(29, 2),
        'matches': kappa + kappa_dual == Fraction(29, 2),
    }


# =============================================================================
# 9. DS pipeline: sl_6 → W_6 shadow comparison
# =============================================================================

def w6_ds_ghost_central_charge():
    """Ghost central charge for DS(sl_6): c_ghost = N(N-1) = 30."""
    return Fraction(30)


def w6_ds_pipeline(k_val, max_arity=8):
    r"""Complete DS shadow comparison for sl_6 → W_6 at level k."""
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    # Central charges: dim(sl_6) = 35, h^v = 6
    c_sl6 = Fraction(35) * kv / (kv + 6)
    c_w6 = w6_central_charge_frac(kv)
    c_gh = w6_ds_ghost_central_charge()

    # Kappa values
    kap_sl6 = Fraction(35) * (kv + 6) / 12  # dim·(k+h^v)/(2h^v)
    kap_w6 = w6_kappa_total_frac(kv)
    kap_gh = c_gh / 2  # = 15

    # Shadow towers on T-line
    tower_w6 = t_line_tower_exact_at_level(kv, max_arity)

    # sl_6 shadow: class L, depth 3
    kap_sl6_val = kap_sl6
    q0 = 4 * kap_sl6_val ** 2
    q1 = 12 * kap_sl6_val  # alpha = 1
    q2 = Fraction(9)  # 9*1^2 + 16*kappa*0 = 9
    sign = 1 if kap_sl6_val > 0 else -1
    coeffs_sl6 = _convolution_coefficients_frac(q0, q1, q2, max_arity - 2, sign)
    tower_sl6 = {r + 2: coeffs_sl6[r] / (r + 2) for r in range(len(coeffs_sl6))}

    return {
        'N': 6,
        'k': kv,
        'c_sl6': c_sl6,
        'c_w6': c_w6,
        'c_ghost': c_gh,
        'c_additive': c_sl6 == c_w6 + c_gh,
        'kappa_sl6': kap_sl6,
        'kappa_w6': kap_w6,
        'kappa_ghost': kap_gh,
        'tower_sl6': tower_sl6,
        'tower_w6': tower_w6,
        'depth_increase': tower_sl6.get(4, Fraction(0)) == 0 and tower_w6.get(4, Fraction(0)) != 0,
    }


# =============================================================================
# 10. Large-N scaling: W_6 in context
# =============================================================================

def w6_in_large_n_context(k_val=None):
    r"""W_6 invariants in the context of the N=2,...,6 sequence.

    Returns a dict of key invariants for comparison.
    """
    if k_val is None:
        k_val = Fraction(5)
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    from compute.lib.w5_shadow_tower import (
        wn_central_charge, wn_kappa_total, wn_ff_sum, wn_kappa_ff_sum,
    )

    results = {}
    for N in range(2, 7):
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
            'ghost_c': Fraction(N * (N - 1)),
        }

    return results


# =============================================================================
# 11. Summary
# =============================================================================

def w6_full_summary(k_val=None):
    """Complete W_6 shadow tower summary."""
    if k_val is None:
        k_val = Fraction(5)
    kv = Fraction(k_val) if not isinstance(k_val, Fraction) else k_val

    c_w = w6_central_charge_frac(kv)
    kap = w6_kappa_total_frac(kv)
    Q_contact = w6_quartic_contact_T_at_level(kv)
    rho = w6_growth_rate_at_level(kv)
    comp = w6_kappa_complementarity(kv)
    tower = t_line_tower_exact_at_level(kv, 8)

    return {
        'N': 6,
        'k': kv,
        'c': c_w,
        'kappa_total': kap,
        'kappa_channels': {s: c_w / s for s in W6_SPINS},
        'Q_contact_T': Q_contact,
        'rho_T': rho,
        'complementarity': comp,
        'tower_T': tower,
        'depth_class': 'M',
        'ff_sum': w6_ff_central_charge_sum(),
        'anomaly_ratio': w6_anomaly_ratio(),
    }


if __name__ == '__main__':
    print("=" * 70)
    print("W_6 Shadow Obstruction Tower")
    print("=" * 70)

    summary = w6_full_summary(Fraction(5))
    print(f"Level k = 5")
    print(f"  c(W_6) = {summary['c']} = {float(summary['c']):.6f}")
    print(f"  κ(W_6) = {summary['kappa_total']} = {float(summary['kappa_total']):.6f}")
    print(f"  Q^contact_T = {summary['Q_contact_T']}")
    print(f"  ρ_T = {summary['rho_T']:.6f}")
    print(f"  κ + κ' = {summary['complementarity']['sum']}")
    print(f"\n  T-line tower:")
    for r in sorted(summary['tower_T'].keys()):
        print(f"    S_{r} = {summary['tower_T'][r]} = {float(summary['tower_T'][r]):.8f}")
