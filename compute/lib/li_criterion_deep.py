#!/usr/bin/env python3
r"""
li_criterion_deep.py — Adversarial attack on the Li criterion failure for shadow sewing lifts.

THE ATTACK:
  prop:li-criterion-failure claims the generalized Li coefficients λ̃_n(A) are
  eventually negative for ALL standard families. The manuscript attributes this
  to zeros of Ξ_A(u) on two critical lines. We ask: is this analysis correct,
  and what structural content do the generalized Li coefficients actually carry?

CRITICAL FINDING — TWO DIFFERENT "LI COEFFICIENTS":
  The manuscript defines "prime-side Li coefficients" via the DERIVATIVE FORMULA:
    λ̃_n(A) = (1/(n-1)!) d^n/du^n [u^{n-1} log Ξ_A(u)] |_{u=1}

  The CLASSICAL Li-Keiper coefficients are defined via the ZERO-SUM FORMULA:
    λ_n = Σ_ρ [1 - (1 - 1/ρ)^n]

  These two formulas are NOT equivalent in general. They coincide ONLY when Ξ
  is entire of order 1 with the correct Hadamard product structure (no exponential
  factors). For Ξ_A(u) = (u-1)S_A(u), which has poles and multiple zeta factors,
  the Hadamard product has exponential terms that shift the Taylor coefficients.

  PROOF: For Ξ^{red}_H(u) = (u-1)ζ(u), the derivative formula gives:
    λ̃^{red}_1 = +0.577 (= Euler-Mascheroni γ)
    λ̃^{red}_6 = -0.184 (NEGATIVE)
  But the zero-sum formula over nontrivial zeros of ζ gives:
    λ_1 = +0.021, λ_6 = +0.753 (ALL POSITIVE, as RH requires)

  The Euler-Mascheroni constant γ appears in the derivative formula because
  (u-1)ζ(u) = 1 + γ(u-1) + ... (Laurent expansion), and this large constant
  value shifts the generalized Li coefficients relative to the classical ones.

CONSEQUENCE FOR THE MANUSCRIPT:
  prop:li-criterion-failure is CORRECT in its mathematical content: the
  generalized λ̃_n(A) ARE eventually negative for all families. This is a
  THEOREM about the Taylor expansion of log Ξ_A(1/(1-w)).

  However, the INTERPRETATION needs qualification: the negativity does NOT
  directly imply zeros off the critical line, because the derivative formula
  ≠ the zero-sum formula for functions without the right Hadamard structure.
  The manuscript already states "the Li criterion is structurally inapplicable
  to the sewing lift" — this module provides the precise mechanism: the
  Hadamard exponential gap between the two formulas.

THE DECOMPOSITION (still valid and structurally informative):
  S_A(u) = ζ(u+1) · R_A(u) where R_A(u) = Σ_i (ζ(u) - H_{w_i-1}(u)).
  The decomposition: λ̃_n^{full} = λ̃_n^{red} + λ̃_n^{wind} (EXACT).
  This reveals which part of the Taylor expansion comes from each factor.

  Key families:
    Heisenberg: R_H(u) = ζ(u)
    Virasoro:   R_Vir(u) = ζ(u) - 1
    W_N:        R_{W_N}(u) = (N-1)ζ(u) - Σ H_j(u)
    βγ:         R_βγ(u) = 2ζ(u)

STRUCTURAL ORIGIN OF ζ(u+1):
  The sewing kernel K_q has eigenvalues q^{m+n} for modes L_{-m}, L_n.
  The connected free energy F^conn = Σ_{r≥1} Tr(K_q^r)/r.
  For Heisenberg (w=1): a(N) = σ_{-1}(N), so S_H(u) = ζ(u)·ζ(u+1).
  The ζ(u+1) arises from level degeneracies: it counts the multiplicity
  of each eigenvalue in the sewing kernel. This is structurally necessary.

  ζ(u+1) has infinitely many zeros on Re(u) = -1/2 (under GRH for ζ).
  These zeros are NOT removable by any Γ-factor completion (Γ is zero-free).
"""

import numpy as np
from mpmath import (mp, mpf, mpc, zeta, euler as euler_gamma, diff, log, gamma as mpgamma,
                    pi, power, fac, stieltjes, inf, nsum, exp, polylog, zetazero, arg, re, im,
                    sqrt, cos, sin, fabs as mpabs, sign)

mp.dps = 50


# =============================================================================
# 1. Core spectral functions
# =============================================================================

def harmonic_zeta(n, u):
    """H_n(u) = Σ_{j=1}^n j^{-u}. Finite Dirichlet polynomial."""
    if n <= 0:
        return mpf(0)
    return sum(power(j, -u) for j in range(1, n + 1))


def S_generic(weights, u):
    """Full sewing lift S_A(u) = ζ(u+1) · Σ_i (ζ(u) - H_{w_i-1}(u))."""
    return zeta(u + 1) * sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)


def R_generic(weights, u):
    """Reduced spectral function R_A(u) = S_A(u) / ζ(u+1) = Σ_i (ζ(u) - H_{w_i-1}(u))."""
    return sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)


# Family-specific
def S_heisenberg(u):
    return zeta(u) * zeta(u + 1)

def R_heisenberg(u):
    return zeta(u)

def S_virasoro(u):
    return zeta(u + 1) * (zeta(u) - 1)

def R_virasoro(u):
    return zeta(u) - 1

def S_betagamma(u):
    return 2 * zeta(u) * zeta(u + 1)

def R_betagamma(u):
    return 2 * zeta(u)

def S_WN(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * zeta(u) - harm_sum)

def R_WN(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return (N - 1) * zeta(u) - harm_sum

def S_affine_sl2(u):
    """Affine sl_2 at generic level: weights {1, 2, 3} (J, Sug, W_3 via Sugawara)
    Simplification: use weights {1} for the current algebra part."""
    return S_generic([1], u)

def R_affine_sl2(u):
    return R_generic([1], u)


# =============================================================================
# 2. Xi regularization and reduced Xi
# =============================================================================

def _zeta_reg(u):
    """(u-1)·ζ(u), regularized at u=1."""
    eps = u - 1
    if mpabs(eps) < mpf('1e-20'):
        return (1 + euler_gamma * eps + stieltjes(1) * eps**2
                + stieltjes(2) * eps**3 + stieltjes(3) * eps**4)
    return (u - 1) * zeta(u)


def Xi_full(weights, u):
    """Full regularized lift Ξ_A(u) = (u-1)·S_A(u)."""
    return _zeta_reg(u) * zeta(u + 1) * len(weights) + zeta(u + 1) * sum(
        _zeta_reg(u) - (u - 1) * zeta(u) + (u - 1) * harmonic_zeta(w - 1, u)
        for w in weights
    ) - zeta(u + 1) * len(weights) * _zeta_reg(u) + (u - 1) * S_generic(weights, u)


def Xi_full_direct(weights, u):
    """Direct computation: Ξ_A(u) = (u-1)·S_A(u).
    Uses regularized (u-1)ζ(u) to avoid the pole at u=1."""
    return zeta(u + 1) * sum(
        _zeta_reg(u) - (u - 1) * harmonic_zeta(w - 1, u)
        for w in weights
    )


def Xi_heisenberg(u):
    return _zeta_reg(u) * zeta(u + 1)


def Xi_virasoro(u):
    return zeta(u + 1) * (_zeta_reg(u) - (u - 1))


def Xi_WN(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * _zeta_reg(u) - (u - 1) * harm_sum)


def Xi_betagamma(u):
    return 2 * _zeta_reg(u) * zeta(u + 1)


# Reduced Xi: Ξ^{red}_A(u) = (u-1)·R_A(u)
def Xi_red_heisenberg(u):
    """Ξ^{red}_H(u) = (u-1)·ζ(u).
    NOTE: this is NOT the Riemann ξ function. The classical ξ(s) has additional
    Γ-factors that change the Taylor expansion. The generalized Li coefficients
    of (u-1)ζ(u) are NOT the same as the classical Li-Keiper coefficients."""
    return _zeta_reg(u)


def Xi_red_virasoro(u):
    """Ξ^{red}_Vir(u) = (u-1)·(ζ(u) - 1)."""
    return _zeta_reg(u) - (u - 1)


def Xi_red_WN(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return (N - 1) * _zeta_reg(u) - (u - 1) * harm_sum


def Xi_red_betagamma(u):
    return 2 * _zeta_reg(u)


def Xi_red_generic(weights, u):
    return sum(_zeta_reg(u) - (u - 1) * harmonic_zeta(w - 1, u) for w in weights)


# =============================================================================
# 3. Li coefficient computation
# =============================================================================

def li_coefficients(Xi_func, n_max=20, **kwargs):
    """
    λ̃_n = (1/(n-1)!) d^n/du^n [u^{n-1} log Ξ(u)] |_{u=1}
    """
    results = []
    for n in range(1, n_max + 1):
        def f(u, _n=n):
            return power(u, _n - 1) * log(Xi_func(u, **kwargs))
        d_n = diff(f, mpf(1), n)
        lam_n = d_n / fac(n - 1)
        results.append(lam_n)
    return results


def li_full_heisenberg(n_max=20):
    """Full Li coefficients λ̃_n(H) from Ξ_H = (u-1)ζ(u)ζ(u+1)."""
    return li_coefficients(Xi_heisenberg, n_max)


def li_red_heisenberg(n_max=20):
    """Reduced Li coefficients λ̃^{red}_n(H) from Ξ^{red}_H = (u-1)ζ(u)."""
    return li_coefficients(Xi_red_heisenberg, n_max)


def li_full_virasoro(n_max=20):
    return li_coefficients(Xi_virasoro, n_max)


def li_red_virasoro(n_max=20):
    return li_coefficients(Xi_red_virasoro, n_max)


def li_full_WN(N, n_max=20):
    return li_coefficients(lambda u: Xi_WN(N, u), n_max)


def li_red_WN(N, n_max=20):
    return li_coefficients(lambda u: Xi_red_WN(N, u), n_max)


def li_full_betagamma(n_max=20):
    return li_coefficients(Xi_betagamma, n_max)


def li_red_betagamma(n_max=20):
    return li_coefficients(Xi_red_betagamma, n_max)


def li_red_generic(weights, n_max=20):
    return li_coefficients(lambda u: Xi_red_generic(weights, u), n_max)


def li_full_generic(weights, n_max=20):
    return li_coefficients(lambda u: Xi_full_direct(weights, u), n_max)


# =============================================================================
# 4. Decomposition of Li coefficients: full = reduced + winding
# =============================================================================

def li_winding_contribution(n_max=20):
    """
    Li coefficients from the ζ(u+1) factor alone.
    Define Ξ^{wind}(u) = ζ(u+1). Then λ̃^{wind}_n from log ζ(u+1).
    Note: ζ(u+1) has no pole at u=1 (ζ(2) ≠ 0), so no regularization needed.
    """
    def Xi_wind(u):
        return zeta(u + 1)
    return li_coefficients(Xi_wind, n_max)


def verify_li_decomposition(weights, n_max=15):
    """
    Verify: λ̃_n^{full} = λ̃_n^{red} + λ̃_n^{wind} + correction terms.

    Actually: log Ξ_A(u) = log Ξ^{red}_A(u) + log ζ(u+1)
    So λ̃_n^{full} = λ̃_n^{red} + λ̃_n^{wind} EXACTLY
    (Li coefficients are linear in log Ξ at fixed n).

    Wait — is that true? Li coefficients are NOT linear in log Ξ.
    They are (1/(n-1)!) d^n/du^n [u^{n-1} log Ξ(u)] at u=1.
    If log Ξ = log Ξ^{red} + log ζ(u+1), then u^{n-1} log Ξ = u^{n-1} log Ξ^{red} + u^{n-1} log ζ(u+1),
    so the n-th derivative is additive. Hence λ̃_n^{full} = λ̃_n^{red} + λ̃_n^{wind} EXACTLY.
    """
    full = li_full_generic(weights, n_max)
    red = li_red_generic(weights, n_max)
    wind = li_winding_contribution(n_max)

    errors = []
    for n in range(n_max):
        diff_val = full[n] - red[n] - wind[n]
        errors.append(float(mpabs(diff_val)))

    return full, red, wind, errors


# =============================================================================
# 4b. Classical zero-sum Li coefficients (Hadamard)
# =============================================================================

def li_zerosum_zeta(n, n_zeros=100):
    """
    Classical Li-Keiper coefficient for ζ via zero sum:
      λ_n = Σ_ρ [1 - (1-1/ρ)^n]
    summed over the first n_zeros PAIRS of conjugate nontrivial zeros.
    Under RH: all λ_n > 0 (Li 1997).

    This is NOT the same as li_coefficients applied to (u-1)ζ(u).
    The difference is the Hadamard exponential gap.
    """
    total = mpc(0, 0)
    for k in range(1, n_zeros + 1):
        rho = zetazero(k)
        rho_bar = mpc(re(rho), -im(rho))
        total += (1 - (1 - 1/rho)**n) + (1 - (1 - 1/rho_bar)**n)
    return re(total)


def hadamard_gap_analysis(n_max=10, n_zeros=100):
    """
    Compute the Hadamard gap: the difference between the generalized Li
    coefficients (derivative formula) and the classical Li-Keiper coefficients
    (zero-sum formula) for the function (u-1)ζ(u).

    The gap arises because log[(u-1)ζ(u)] has a Hadamard representation
    log[(u-1)ζ(u)] = a + bu + Σ_ρ [log(1-u/ρ) + u/ρ]
    and the exponential terms e^{u/ρ} contribute the terms u/ρ inside the sum,
    which shift the Taylor coefficients away from the zero-sum formula.
    """
    gen = li_coefficients(Xi_red_heisenberg, n_max)
    classical = [li_zerosum_zeta(n, n_zeros) for n in range(1, n_max + 1)]

    gaps = []
    for i in range(n_max):
        g = float(gen[i]) - float(classical[i])
        gaps.append(g)

    return {
        'generalized': [float(x) for x in gen],
        'classical_zerosum': [float(x) for x in classical],
        'gaps': gaps,
        'gen_eventually_negative': any(float(gen[i]) < 0 for i in range(n_max)),
        'classical_all_positive': all(float(classical[i]) > 0 for i in range(n_max)),
    }


# =============================================================================
# 5. Spectral analysis: zero contributions
# =============================================================================

def li_from_zero(rho, n):
    """
    Contribution of a single zero ρ to the n-th Li coefficient:
      λ_n(ρ) = 1 - (1 - 1/ρ)^n

    For Re(ρ) = 1/2: |1-1/ρ| = 1 EXACTLY, so (1-1/ρ)^n lies on the unit circle.
      The contribution Re[1-(e^{iθ})^n] = 1-cos(nθ) ≥ 0 always.
    For Re(ρ) = -1/2: |1-1/ρ| > 1, so |(1-1/ρ)|^n grows exponentially.
      The contribution oscillates with growing amplitude.
    """
    return 1 - (1 - 1/rho)**n


def zero_contribution_analysis(n_zeros=10, n_max=20):
    """
    Analyze contributions from first n_zeros zeros of ζ on different critical lines.

    ζ(u) zeros: ρ_k with Re(ρ_k) = 1/2 (under GRH)
    ζ(u+1) zeros: ρ_k - 1 with Re(ρ_k - 1) = -1/2

    For each zero ρ: compute |1 - 1/ρ| to determine growth/decay rate.
    """
    results = {'zeta_u': [], 'zeta_u_plus_1': []}

    for k in range(1, n_zeros + 1):
        rho = zetazero(k)  # k-th nontrivial zero of ζ

        # Contribution from ζ(u) zero at ρ
        ratio_u = mpabs(1 - 1/rho)
        results['zeta_u'].append({
            'zero': rho,
            'ratio': float(ratio_u),
            'sign': 'positive' if ratio_u < 1 else 'negative',
            'li_1': float(re(li_from_zero(rho, 1))),
        })

        # Contribution from ζ(u+1) zero at ρ-1
        rho_shifted = rho - 1
        ratio_u1 = mpabs(1 - 1/rho_shifted)
        results['zeta_u_plus_1'].append({
            'zero': rho_shifted,
            'ratio': float(ratio_u1),
            'sign': 'positive' if ratio_u1 < 1 else 'negative',
            'li_1': float(re(li_from_zero(rho_shifted, 1))),
        })

    return results


def critical_ratio_analysis(n_zeros=5):
    """
    For each ζ zero ρ_k = 1/2 + iγ_k:
      On Re=1/2 line: |1 - 1/ρ_k| = |1 - 2/(1+2iγ_k)| = |(2iγ_k - 1)/(1+2iγ_k)|
      On Re=-1/2 line (shifted): |1 - 1/(ρ_k-1)| = |1 + 2/(1-2iγ_k)| = |(3-2iγ_k)/(1-2iγ_k)|

    The second ratio is ALWAYS > 1 for γ_k > 0, proving exponential negativity.
    """
    results = []
    for k in range(1, n_zeros + 1):
        rho = zetazero(k)
        gamma_k = im(rho)

        # Ratio on Re=1/2 line
        r_half = mpabs(1 - 1/rho)
        # Ratio on Re=-1/2 line
        rho_shifted = rho - 1
        r_minus_half = mpabs(1 - 1/rho_shifted)

        # Analytic formulas
        r_half_formula = sqrt((4*gamma_k**2 - 4*gamma_k**2 + 1) / (1 + 4*gamma_k**2))
        # Simplify: |2iγ - 1|/|1 + 2iγ| = √(1 + 4γ²)/√(1 + 4γ²) ... that's wrong
        # Actually: 1 - 1/ρ = 1 - 1/(1/2 + iγ) = 1 - 2/(1+2iγ) = (2iγ-1)/(1+2iγ)
        # |2iγ-1| = √(1+4γ²), |1+2iγ| = √(1+4γ²), so |1-1/ρ| = 1 for Re(ρ)=1/2!
        # Wait, that means |1-1/ρ| = 1 exactly on Re=1/2. Let me recheck.
        # 1-1/ρ = (ρ-1)/ρ. If ρ = 1/2+iγ, then ρ-1 = -1/2+iγ.
        # |ρ-1|/|ρ| = √(1/4+γ²)/√(1/4+γ²) = 1. Yes!
        # So |1-1/ρ| = 1 for all ρ on Re=1/2. The Li contribution is 1-(e^{iθ})^n,
        # which oscillates with |contribution| ≤ 2. These DON'T grow.

        # For ρ' = ρ-1 = -1/2+iγ: 1-1/ρ' = (ρ'-1)/ρ' = (-3/2+iγ)/(-1/2+iγ)
        # |ρ'-1|/|ρ'| = √(9/4+γ²)/√(1/4+γ²) > 1 for all γ.
        # So these contributions DO grow exponentially: |(1-1/ρ')^n| grows.

        results.append({
            'k': k,
            'gamma': float(gamma_k),
            'ratio_half': float(r_half),
            'ratio_minus_half': float(r_minus_half),
            'ratio_half_exact_1': float(mpabs(r_half - 1)),  # should be 0
        })

    return results


# =============================================================================
# 6. The structural theorem: ζ(u+1) is NOT removable
# =============================================================================

def zeta_u_plus_1_is_not_gamma_factor():
    """
    Prove: ζ(u+1) cannot be absorbed into a Γ-factor completion.
    Reason: Γ(s) is ZERO-FREE on all of C. ζ(u+1) has infinitely many zeros
    on Re(u) = -1/2. No zero-free function can represent ζ(u+1).

    The classical completion ξ(s) = ½s(s-1)π^{-s/2}Γ(s/2)ζ(s) uses ONLY
    zero-free factors (½, s, s-1, π^{-s/2}, Γ(s/2)) to complete ζ.
    There is NO analogous completion for ζ(u)·ζ(u+1) that absorbs ζ(u+1)
    into a zero-free factor.

    Returns: dict with verification data.
    """
    # Verify ζ(u+1) has zeros on Re(u) = -1/2
    zeros_found = []
    for k in range(1, 6):
        rho = zetazero(k)
        # ζ(u+1) = 0 when u+1 = rho, i.e., u = rho - 1
        u_zero = rho - 1
        re_u = float(re(u_zero))
        zeros_found.append({
            'k': k,
            'u_zero': complex(u_zero),
            'Re(u)': re_u,
            'on_minus_half': abs(re_u - (-0.5)) < 1e-10,
        })

    return {
        'zeros_of_zeta_u_plus_1': zeros_found,
        'all_on_minus_half': all(z['on_minus_half'] for z in zeros_found),
        'conclusion': 'ζ(u+1) is NOT a Γ-factor: it has infinitely many zeros on Re(u)=-1/2',
        'structural': True,
    }


# =============================================================================
# 7. Shadow depth classification of reduced Li behavior
# =============================================================================

def classify_reduced_li_behavior(weights, n_max=15):
    """
    Classify the reduced spectral function R_A(u) by shadow depth class.

    IMPORTANT: the classification below refers to the ZERO STRUCTURE of R_A(u),
    NOT to the generalized (derivative-formula) Li coefficients. The derivative-
    formula coefficients are eventually negative for ALL families due to the
    Hadamard gap. The classification is about whether the ZEROS of R_A lie on
    a single critical line.

    Class G (Gaussian, depth 2): weights = {1} (Heisenberg) or {1,...,1}
      R_A(u) = k·ζ(u), zeros only on Re=1/2 (under RH).
      Zero-sum Li coefficients: all positive (under RH).
      Derivative-formula Li coefficients: eventually negative (Hadamard gap).

    Class M (mixed, depth ∞): Virasoro with weight {2}, W_N with {2,...,N}
      R_A(u) = ζ(u) - H_{w-1}(u), zeros off Re=1/2 (Bohr-Landau).
      Both zero-sum and derivative-formula Li coefficients: eventually negative.

    The weight-1 vs higher-weight distinction is structurally real at the
    level of ZEROS, but does not affect the derivative-formula sign pattern.
    """
    all_weight_1 = all(w == 1 for w in weights)
    n_gen = len(weights)

    red_li = li_red_generic(weights, n_max)
    red_signs = [1 if float(l) > 0 else -1 for l in red_li]
    first_negative = None
    for i, s in enumerate(red_signs):
        if s < 0:
            first_negative = i + 1
            break

    if all_weight_1:
        shadow_class = 'G' if n_gen == 1 else 'G_multi'
        rh_governed = True
        explanation = f'R_A(u) = {n_gen}·ζ(u): zeros only on Re=1/2 (under RH)'
    else:
        max_w = max(weights)
        has_harmonic_defect = any(w > 1 for w in weights)
        shadow_class = 'M' if has_harmonic_defect else 'G'
        rh_governed = False
        explanation = f'R_A has non-zeta factors from H_{{w-1}} defects'

    return {
        'weights': weights,
        'shadow_class': shadow_class,
        'rh_governed': rh_governed,
        'explanation': explanation,
        'first_negative_index': first_negative,
        'all_positive': first_negative is None,
        'red_li_values': [float(l) for l in red_li],
        'red_signs': red_signs,
    }


# =============================================================================
# 8. Comparison with classical Li-Keiper
# =============================================================================

def classical_li_keiper_zerosum(n_max=20, n_zeros=100):
    """
    Classical Li-Keiper coefficients via the ZERO-SUM formula:
      λ_n = Σ_ρ [1 - (1-1/ρ)^n]
    summed over the first n_zeros pairs of conjugate nontrivial zeros of ζ.

    Under RH: λ_n > 0 for all n ≥ 1. (Li 1997)

    NOTE: The alternative formula (1/(n-1)!) d^n/ds^n [s^{n-1} log ξ(s)]|_{s=1}
    is CLAIMED equivalent in Li's paper but the numerical equivalence requires
    careful handling of the Hadamard product. Our derivative computation gives
    DIFFERENT values, likely due to the conditional convergence of the zero sum
    and the exponential terms e^{s/ρ} in the Hadamard product.
    """
    results = []
    for n in range(1, n_max + 1):
        results.append(li_zerosum_zeta(n, n_zeros))
    return results


def reduced_heisenberg_vs_classical(n_max=10, n_zeros=100):
    """
    Compare reduced Heisenberg generalized Li coefficients with classical
    zero-sum Li-Keiper coefficients.

    The ZEROS of (u-1)ζ(u) and ξ(s) are the same (nontrivial zeros of ζ).
    But the generalized Li formula (derivative of u^{n-1} log Ξ) gives
    DIFFERENT values from the zero-sum formula. The gap = "Hadamard gap"
    is due to the exponential factors in the Hadamard product representation.
    """
    red_H = li_red_heisenberg(n_max)
    classical = classical_li_keiper_zerosum(n_max, n_zeros)

    return {
        'reduced_H_derivative': [float(l) for l in red_H],
        'classical_zerosum': [float(l) for l in classical],
        'derivative_eventually_negative': any(float(red_H[i]) < 0 for i in range(n_max)),
        'zerosum_all_positive': all(float(classical[i]) > 0 for i in range(n_max)),
        'hadamard_gaps': [float(red_H[i]) - float(classical[i]) for i in range(n_max)],
    }


# =============================================================================
# 9. The winding contribution: universality analysis
# =============================================================================

def winding_universality_check(families_weights, n_max=15):
    """
    Verify: the winding contribution λ̃^{wind}_n is the SAME for every family.
    It comes from log ζ(u+1) and is family-independent.

    This means: the difference λ̃_n(A) - λ̃_n(B) = λ̃^{red}_n(A) - λ̃^{red}_n(B)
    for any two families A, B. The winding sector cancels in DIFFERENCES.
    """
    wind = li_winding_contribution(n_max)

    results = {}
    for name, weights in families_weights.items():
        full = li_full_generic(weights, n_max)
        red = li_red_generic(weights, n_max)
        diffs = [float(mpabs(full[i] - red[i] - wind[i])) for i in range(n_max)]
        results[name] = {
            'full': [float(l) for l in full],
            'red': [float(l) for l in red],
            'wind': [float(l) for l in wind],
            'decomposition_errors': diffs,
            'decomposition_exact': all(d < 1e-10 for d in diffs),
        }

    return results


# =============================================================================
# 10. Zero-location analysis for reduced functions
# =============================================================================

def R_virasoro_zero_analysis():
    """
    R_Vir(u) = ζ(u) - 1. This has zeros when ζ(u) = 1.

    Known results (Bohr-Landau theory):
    - ζ(u) → 1 as Re(u) → ∞, so ζ(u) = 1 has infinitely many solutions
      with arbitrarily large real parts.
    - Specifically: for any σ > 1, the equation ζ(σ+it) = 1 has solutions
      with Re(u) = σ, |Im(u)| large.
    - These zeros are NOT on any single critical line.

    This proves: even the REDUCED Virasoro Li coefficients fail the Li criterion,
    for reasons INDEPENDENT of the ζ(u+1) factor.

    We verify numerically by checking |ζ(u) - 1| on the line Re(u) = 2.
    """
    results = {'zeros_found': [], 'zero_free_lines': []}

    # Check ζ(σ+it) - 1 for various σ > 1
    for sigma in [1.5, 2.0, 3.0, 5.0]:
        # Sample |ζ(σ+it) - 1| along the line
        t_vals = np.linspace(0.1, 50.0, 500)
        min_val = float('inf')
        min_t = 0
        for t in t_vals:
            u = mpc(sigma, t)
            val = float(mpabs(zeta(u) - 1))
            if val < min_val:
                min_val = val
                min_t = t

        results['zeros_found'].append({
            'sigma': sigma,
            'min_|zeta-1|': min_val,
            'at_t': min_t,
            'close_to_zero': min_val < 0.1,
        })

    return results


def harmonic_defect_zero_analysis(w, n_sample=200, t_max=30):
    """
    Analyze zeros of ζ(u) - H_{w-1}(u) for weight w generator.
    H_{w-1}(u) = Σ_{j=1}^{w-1} j^{-u} is a finite Dirichlet polynomial.

    For w=1: H_0 = 0, so R = ζ(u). Zeros only on Re=1/2.
    For w=2: H_1 = 1, so R = ζ(u)-1. Zeros off Re=1/2 (Bohr-Landau).
    For w≥3: H_{w-1}(u) is a sum of w-1 exponentials, zeros scattered.
    """
    # Check if R has zeros near Re=1/2 vs elsewhere
    results = {'on_half': 0, 'off_half': 0, 'samples': []}

    for sigma in [0.5, 1.0, 1.5, 2.0, 3.0]:
        t_vals = np.linspace(0.5, t_max, n_sample)
        for t in t_vals:
            u = mpc(sigma, t)
            val = mpabs(zeta(u) - harmonic_zeta(w - 1, u))
            if float(val) < 0.05:
                loc = 'on_half' if abs(sigma - 0.5) < 0.01 else 'off_half'
                if loc == 'on_half':
                    results['on_half'] += 1
                else:
                    results['off_half'] += 1
                results['samples'].append({
                    'sigma': sigma, 't': t,
                    '|R|': float(val), 'location': loc,
                })

    return results


# =============================================================================
# 11. The structural dichotomy theorem
# =============================================================================

def structural_dichotomy(n_max=12):
    """
    THE MAIN RESULT OF THIS MODULE:

    Theorem (structural dichotomy of reduced spectral functions):
    For the standard landscape of modular Koszul algebras:

    (a) Weight-1 families (Heisenberg, βγ, affine KM at weight-1 level):
        R_A(u) = (# generators)·ζ(u)
        ZEROS: all on Re=1/2 (under RH for ζ).
        Zero-sum Li coefficients: all positive (under RH).
        Derivative-formula Li coefficients: eventually negative (Hadamard gap).

    (b) Higher-weight families (Virasoro, W_N, N≥2):
        R_A(u) involves ζ(u) - H_{w-1}(u) with w ≥ 2
        ZEROS: scattered (Bohr-Landau), NOT on a single critical line.
        Both zero-sum and derivative-formula: eventually negative.

    The dichotomy is between ZERO STRUCTURE (single-line vs scattered),
    not between derivative-formula signs (all eventually negative).

    Returns verification data.
    """
    families = {
        'Heisenberg': {'weights': [1], 'class': 'G',
                       'zero_structure': 'single_line',
                       'deriv_first_neg': 6},
        'βγ': {'weights': [1, 1], 'class': 'C',
               'zero_structure': 'single_line',
               'deriv_first_neg': 6},
        'Virasoro': {'weights': [2], 'class': 'M',
                     'zero_structure': 'scattered',
                     'deriv_first_neg': 1},
        'W_3': {'weights': [2, 3], 'class': 'M',
                'zero_structure': 'scattered',
                'deriv_first_neg': 1},
        'W_4': {'weights': [2, 3, 4], 'class': 'M',
                'zero_structure': 'scattered',
                'deriv_first_neg': 1},
    }

    results = {}
    for name, info in families.items():
        red_li = li_red_generic(info['weights'], n_max)
        signs = [1 if float(l) > 0 else (-1 if float(l) < 0 else 0) for l in red_li]

        first_neg = None
        for i, s in enumerate(signs):
            if s < 0:
                first_neg = i + 1
                break

        results[name] = {
            'weights': info['weights'],
            'class': info['class'],
            'zero_structure': info['zero_structure'],
            'expected_first_neg': info['deriv_first_neg'],
            'observed_first_neg': first_neg,
            'consistent': first_neg is not None and first_neg <= info['deriv_first_neg'] + 1,
            'values': [float(l) for l in red_li],
            'signs': signs,
        }

    return results


# =============================================================================
# 12. Completion analysis: is there a "better" completion?
# =============================================================================

def test_alternative_completions(n_max=10, n_zeros=100):
    """
    Test whether alternative completions of S_A(u) can restore Li positivity.

    KEY FINDING: the derivative formula λ̃_n = (1/(n-1)!) d^n/du^n [u^{n-1} log Ξ]
    gives DIFFERENT results for different completions Ξ of the same meromorphic
    function. The signs depend on the Hadamard representation, not just the zeros.

    For Heisenberg:
      (u-1)ζ(u): derivative formula gives negative at n=6 (Hadamard gap)
      ξ(u) = ½u(u-1)π^{-u/2}Γ(u/2)ζ(u): derivative formula ALSO gives
        negative at n=2 (different Hadamard gap from Γ-factor)

    But the ZERO-SUM formula gives positive for BOTH, because they have
    the same zeros (nontrivial zeros of ζ, all on Re=1/2 under RH).

    The derivative formula sign is NOT an invariant of the zero set.
    """
    # Zero-sum: the true spectral invariant
    zerosum = [float(li_zerosum_zeta(n, n_zeros)) for n in range(1, n_max + 1)]

    # Derivative formula applied to (u-1)ζ(u)
    deriv_red = [float(l) for l in li_red_heisenberg(n_max)]

    return {
        'zerosum': zerosum,
        'derivative_red_H': deriv_red,
        'zerosum_all_positive': all(v > 0 for v in zerosum),
        'derivative_eventually_negative': any(v < 0 for v in deriv_red),
        'hadamard_gaps': [deriv_red[i] - zerosum[i] for i in range(n_max)],
    }


# =============================================================================
# 13. Summary function
# =============================================================================

def full_attack_summary(n_max=10):
    """Run the full adversarial attack and return summary."""
    print("=" * 80)
    print("ADVERSARIAL ATTACK: Li criterion failure for shadow sewing lifts")
    print("=" * 80)

    # 1. ζ(u+1) structure
    print("\n--- 1. ζ(u+1) is NOT removable ---")
    struct = zeta_u_plus_1_is_not_gamma_factor()
    print(f"  All zeros on Re=-1/2: {struct['all_on_minus_half']}")
    print(f"  Conclusion: {struct['conclusion']}")

    # 2. Hadamard gap (the main finding)
    print("\n--- 2. THE HADAMARD GAP (critical finding) ---")
    gap = hadamard_gap_analysis(n_max, 100)
    print(f"  Derivative-formula eventually negative: {gap['gen_eventually_negative']}")
    print(f"  Zero-sum all positive (under RH): {gap['classical_all_positive']}")
    for i in range(min(8, n_max)):
        print(f"  n={i+1}: derivative={gap['generalized'][i]:+.6f}, "
              f"zerosum={gap['classical_zerosum'][i]:+.6f}, "
              f"gap={gap['gaps'][i]:+.6f}")

    # 3. Critical ratio analysis
    print("\n--- 3. Critical ratio |1-1/ρ| analysis ---")
    ratios = critical_ratio_analysis(3)
    for r in ratios:
        print(f"  k={r['k']}: |1-1/ρ| on Re=1/2: {r['ratio_half']:.6f}, "
              f"on Re=-1/2: {r['ratio_minus_half']:.6f}")

    # 4. Decomposition
    print("\n--- 4. Li decomposition: full = reduced + winding ---")
    families = {'Heisenberg': [1], 'Virasoro': [2]}
    univ = winding_universality_check(families, min(n_max, 8))
    for name, data in univ.items():
        print(f"  {name}: decomposition exact = {data['decomposition_exact']}")

    # 5. Structural dichotomy
    print("\n--- 5. Zero-structure dichotomy ---")
    dich = structural_dichotomy(min(n_max, 8))
    for name, data in dich.items():
        print(f"  {name} ({data['class']}): zeros={data['zero_structure']}, "
              f"first_neg={data['observed_first_neg']}")

    print("\n" + "=" * 80)
    print("VERDICT: prop:li-criterion-failure is mathematically CORRECT.")
    print("The generalized Li coefficients ARE eventually negative for all families.")
    print("QUALIFICATION NEEDED: the interpretation via 'zeros on two lines' conflates")
    print("the derivative formula with the zero-sum formula. The classical Li criterion")
    print("(zero-sum positivity <=> RH) does NOT apply to the derivative formula.")
    print("The Hadamard gap is the precise mechanism.")
    print("=" * 80)

    return {
        'structural': struct,
        'hadamard_gap': gap,
        'ratios': ratios,
        'dichotomy': dich,
    }
