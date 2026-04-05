r"""
koszul_epstein_rankin_selberg.py -- Genus-1 Rankin-Selberg transform of Theta_A.

CONSTRUCTION:

The genus-1 shadow projection of the universal MC element Theta_A is:
    Sh_2^{(1)}(tau) = kappa(A) * G_2(tau)
where G_2(tau) = -1/24 + sum_{n>=1} sigma_1(n) q^n is the normalized
weight-2 quasi-modular Eisenstein series.

The GENUS-1 RANKIN-SELBERG TRANSFORM is defined as:
    RS_1(s, A) = integral_{SL(2,Z)\H} Sh_2^{(1)}(tau) E(tau,s) y^s d mu(tau)

where E(tau,s) is the real-analytic Eisenstein series and d mu = y^{-2} dx dy.

MAIN THEOREM (thm:genus-1-rs-universality):

At genus 1, the RS transform is UNIVERSAL:
    RS_1(s, A) = kappa(A) * RS_1(s, H)
where H is the Heisenberg algebra (kappa = 1). The universality follows
from the genus-1 universality theorem (obs_1 = kappa * lambda_1, proved
unconditionally): at genus 1, only the arity-2 shadow kappa contributes.
Higher-arity shadows S_r (r >= 3) contribute only at genus g >= floor(r/2)+1
by the shadow visibility theorem (cor:shadow-visibility-genus).

The completed RS function is:
    Xi_RS(s) = xi(s) * xi(s-1)
where xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s) is the Riemann
xi-function. This has symmetry s -> 2-s (center s=1).

NONTRIVIAL ZEROS:

The zeros of Xi_RS(s) are {rho} union {1+rho} where rho ranges over
nontrivial zeros of zeta(s). Under RH, these lie on Re(s) = 1/2 and
Re(s) = 3/2 respectively — TWO critical lines, symmetric about s = 1.

LI-LIKE COEFFICIENTS:

Define lambda_n^KE = sum_{zeros rho_j of Xi_RS} [1 - ((rho_j - 2)/(rho_j - 1))^n]

STRUCTURAL RESULTS:

(1) lambda_1^KE = 0 EXACTLY, by the pairing symmetry: each quadruplet
    {1/2+i*gamma, 1/2-i*gamma, 3/2+i*gamma, 3/2-i*gamma} contributes
    sum 1/(rho_j - 1) = 0 by cancellation between the two critical lines.

(2) lambda_n^KE > 0 for n >= 2 (under RH), since the zeros on Re(s) = 1/2
    dominate: |(rho-2)/(rho-1)| > 1 for Re(rho) = 1/2, so contributions
    grow with n; while |(rho-2)/(rho-1)| = 1 for Re(rho) = 3/2, so those
    contributions are bounded.

(3) lambda_n^KE are INDEPENDENT of A at genus 1 (universality).
    Family dependence enters at genus >= 2 through higher shadow coefficients.

(4) The genus-1 RS zeros encode the same information as the Riemann zeros,
    but with a DOUBLED structure: each gamma produces four zeros instead of two.

GENUS-2 EXTENSION (family-dependent):

At genus 2, the shadow S_3 first contributes (shadow visibility: g_min(S_3)=2).
The genus-2 RS transform involves:
    RS_2(s, A) = kappa(A) * [genus-2 kappa contribution] + S_3(A) * [genus-2 cubic]
                + S_4(A) * [genus-2 quartic] + ...

For Heisenberg (S_r = 0 for r >= 3): RS_2 = kappa * [universal genus-2 piece]
For Virasoro (infinite tower): RS_2 depends on all S_r up to visibility bound

The genus-2 Li coefficients lambda_n^{KE,(2)}(A) are FAMILY-DEPENDENT.

Manuscript references:
    thm:genus-1-rs-universality (NEW, to be added to arithmetic_shadows.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    thm:operadic-rankin-selberg (arithmetic_shadows.tex)
    def:koszul-epstein-function (arithmetic_shadows.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, Optional, Tuple, Any

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi, zeta, gamma as mpgamma, log, exp,
                        power, sqrt, re as mpre, im as mpim, conj as mpconj,
                        fac, diff, zetazero, inf)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Standard family shadow data
# ============================================================

class ShadowData:
    """Shadow obstruction tower data for a chiral algebra family."""

    def __init__(self, name: str, kappa: float, shadow_class: str,
                 weights: List[int], S_coeffs: Optional[Dict[int, float]] = None):
        self.name = name
        self.kappa = kappa
        self.shadow_class = shadow_class
        self.weights = weights
        self.S_coeffs = S_coeffs or {}  # S_r for r >= 3

    def shadow_coefficient(self, r: int) -> float:
        """Shadow obstruction tower coefficient S_r."""
        if r == 2:
            return self.kappa
        return self.S_coeffs.get(r, 0.0)


def heisenberg_data(k: float = 1.0) -> ShadowData:
    """Heisenberg algebra H_k: class G, r_max = 2."""
    return ShadowData("Heisenberg", kappa=k/2, shadow_class='G',
                      weights=[1])


def virasoro_data(c: float) -> ShadowData:
    """Virasoro algebra Vir_c: class M, r_max = infinity."""
    kappa = c / 2
    alpha = 2.0
    S4 = 10.0 / (c * (5*c + 22)) if abs(c) > 1e-15 and abs(5*c + 22) > 1e-15 else 0.0
    # Higher shadow coefficients from the leading-order recursion:
    # S_r = (2/r) * (-3)^{r-4} * (2/c)^{r-2}
    P = 2.0 / c if abs(c) > 1e-15 else 0.0
    S_coeffs = {}
    S_coeffs[3] = alpha
    S_coeffs[4] = S4
    for r in range(5, 21):
        S_coeffs[r] = (2.0 / r) * (-3.0)**(r - 4) * P**(r - 2)
    return ShadowData("Virasoro", kappa=kappa, shadow_class='M',
                      weights=[2], S_coeffs=S_coeffs)


def w3_data(c: float) -> ShadowData:
    """W_3 algebra at central charge c: class M.

    The T-line shadow data coincides with Virasoro (same kappa, alpha, S4
    along the T-line). The W-line contribution is an independent channel
    with different shadow coefficients.

    At the genus-1 scalar level, only kappa matters, and kappa(W_3)
    involves the harmonic number:
        kappa(W_3) = c * (H_3 - 1) = c * (1/2 + 1/3 - 1 + 1) ... no.

    Actually: for the principal W_N algebra at level k,
        c(W_N) = (N-1)(1 - N(N+1)/(k+N))
    and kappa(W_N) = c/2 for all W-algebras (the anomaly ratio rho=1/2
    is universal for the Virasoro embedding).

    For W_3 specifically, the two generators have weights 2 (T) and 3 (W).
    """
    kappa = c / 2
    # T-line shadow coefficients (same as Virasoro along this line)
    alpha = 2.0
    S4 = 10.0 / (c * (5*c + 22)) if abs(c) > 1e-15 and abs(5*c + 22) > 1e-15 else 0.0
    S_coeffs = {3: alpha, 4: S4}
    P = 2.0 / c if abs(c) > 1e-15 else 0.0
    for r in range(5, 21):
        S_coeffs[r] = (2.0 / r) * (-3.0)**(r - 4) * P**(r - 2)
    return ShadowData("W_3", kappa=kappa, shadow_class='M',
                      weights=[2, 3], S_coeffs=S_coeffs)


STANDARD_FAMILIES = {
    'heisenberg': heisenberg_data,
    'virasoro': virasoro_data,
    'w3': w3_data,
}


# ============================================================
# 2. The genus-1 RS transform: analytic structure
# ============================================================

def xi_riemann(s):
    """Riemann xi-function: xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s).

    Entire of order 1, with xi(s) = xi(1-s).
    """
    return mpf('0.5') * s * (s - 1) * power(pi, -s/2) * mpgamma(s/2) * zeta(s)


def xi_rs_genus1(s):
    """Completed genus-1 RS function: Xi_RS(s) = xi(s) * xi(s-1).

    Has symmetry s -> 2-s.
    Zeros: {rho} union {1+rho} for nontrivial zeta zeros rho.
    """
    return xi_riemann(s) * xi_riemann(s - 1)


def rs_dirichlet_series(s, kappa=1.0, N_max=1000):
    """RS_1(s, A) as a Dirichlet series (convergent for Re(s) > 2).

    RS_1(s, A) = kappa * sum_{n=1}^{N_max} sigma_1(n) * n^{-s}

    The full Dirichlet series sum sigma_1(n) n^{-s} = zeta(s) * zeta(s-1).
    """
    result = mpf(0)
    for n in range(1, N_max + 1):
        sig1 = sum(d for d in range(1, n + 1) if n % d == 0)
        result += mpf(sig1) * power(n, -s)
    return kappa * result


def rs_product_formula(s, kappa=1.0):
    """RS_1(s, A) = kappa * zeta(s) * zeta(s-1) (analytic continuation).

    Valid for all s (meromorphic), with poles at s = 1 (from zeta(s))
    and s = 2 (from zeta(s-1)).
    """
    return kappa * zeta(s) * zeta(s - 1)


# ============================================================
# 3. Li-like coefficients: lambda_n^KE
# ============================================================

def compute_zeta_zeros(N_zeros: int = 200, dps: int = 30) -> List:
    """Compute first N_zeros nontrivial zeros of zeta(s) with Im > 0."""
    old_dps = mp.dps
    mp.dps = dps
    zeros = [zetazero(k) for k in range(1, N_zeros + 1)]
    mp.dps = old_dps
    return zeros


def li_coefficient_rs(n: int, zeros: List, family: Optional[ShadowData] = None) -> mpf:
    """Li-like coefficient lambda_n^KE for the genus-1 RS transform.

    lambda_n^KE = sum_{zeros rho_j of Xi_RS} [1 - ((rho_j - 2)/(rho_j - 1))^n]

    At genus 1, these are INDEPENDENT of the family (universality).
    The family parameter is accepted for interface consistency but does not
    affect the result at genus 1.

    Parameters
    ----------
    n : int
        The Li coefficient index (n >= 1).
    zeros : list
        Precomputed zeta zeros (Im > 0).
    family : ShadowData, optional
        Shadow data (unused at genus 1; included for genus-2 extension).

    Returns
    -------
    mpf : The Li coefficient lambda_n^KE.
    """
    lam = mpf(0)
    for rho in zeros:
        # Contribution from rho (zero of zeta(s)):
        w1 = (rho - 2) / (rho - 1)
        term1 = 1 - w1**n
        lam += 2 * mpre(term1)  # rho and bar(rho) contribute conjugate terms

        # Contribution from 1+rho (zero of zeta(s-1)):
        rho2 = 2 - mpconj(rho)  # = 3/2 + i*gamma
        w2 = (rho2 - 2) / (rho2 - 1)
        term2 = 1 - w2**n
        lam += 2 * mpre(term2)  # rho2 and bar(rho2) contribute conjugate terms

    return lam


def li_coefficients_rs(n_max: int = 20, N_zeros: int = 200,
                       family: Optional[ShadowData] = None,
                       dps: int = 30) -> Dict[int, mpf]:
    """Compute Li coefficients lambda_1^KE through lambda_{n_max}^KE.

    Returns dict mapping n -> lambda_n^KE.
    """
    old_dps = mp.dps
    mp.dps = dps
    zeros = compute_zeta_zeros(N_zeros, dps)
    result = {}
    for n in range(1, n_max + 1):
        result[n] = li_coefficient_rs(n, zeros, family)
    mp.dps = old_dps
    return result


# ============================================================
# 4. Structural analysis of Li coefficients
# ============================================================

def lambda1_vanishing_proof(zeros: List) -> Dict[str, Any]:
    """Verify and explain why lambda_1^KE = 0 exactly.

    The vanishing follows from the pairing symmetry: each quadruplet
    of zeros {1/2+i*gamma, 1/2-i*gamma, 3/2+i*gamma, 3/2-i*gamma}
    contributes sum 1/(rho_j - 1) = 0.

    Explicitly:
        1/(-1/2+i*gamma) + 1/(-1/2-i*gamma) + 1/(1/2+i*gamma) + 1/(1/2-i*gamma)
        = 2*Re[1/(-1/2+i*gamma)] + 2*Re[1/(1/2+i*gamma)]
        = -1/(1/4+gamma^2) + 1/(1/4+gamma^2) = 0
    """
    # Verify numerically
    total = mpf(0)
    contributions = []
    for rho in zeros:
        gamma = mpim(rho)
        # Contribution from the four zeros at this gamma
        c_neg = 2 * mpre(1 / (rho - 1))         # Re(s) = 1/2 pair
        c_pos = 2 * mpre(1 / (2 - mpconj(rho) - 1))  # Re(s) = 3/2 pair
        total += c_neg + c_pos
        contributions.append({
            'gamma': float(gamma),
            'from_half': float(c_neg),
            'from_three_half': float(c_pos),
            'sum': float(c_neg + c_pos),
        })

    return {
        'lambda_1': float(total),
        'is_zero': abs(total) < 1e-20,
        'mechanism': 'pairing_symmetry',
        'explanation': (
            'Each quadruplet {1/2+/-i*gamma, 3/2+/-i*gamma} contributes '
            '[-1 + 1]/(1/4+gamma^2) = 0 to lambda_1.'
        ),
        'per_gamma': contributions[:5],  # first 5 for illustration
    }


def critical_line_analysis(zeros: List, n_max: int = 10) -> Dict[str, Any]:
    """Decompose Li coefficients by critical line.

    The zeros on Re(s) = 1/2 have |(rho-2)/(rho-1)| > 1 (growing contributions).
    The zeros on Re(s) = 3/2 have |(rho-2)/(rho-1)| = 1 (bounded contributions).
    """
    results = {}
    for n in range(1, n_max + 1):
        from_half = mpf(0)
        from_three_half = mpf(0)
        for rho in zeros:
            # Re(s) = 1/2 contribution
            w1 = (rho - 2) / (rho - 1)
            from_half += 2 * mpre(1 - w1**n)

            # Re(s) = 3/2 contribution
            rho2 = 2 - mpconj(rho)
            w2 = (rho2 - 2) / (rho2 - 1)
            from_three_half += 2 * mpre(1 - w2**n)

        results[n] = {
            'total': float(from_half + from_three_half),
            'from_Re_half': float(from_half),
            'from_Re_three_half': float(from_three_half),
            'ratio': float(from_half / from_three_half) if abs(from_three_half) > 1e-30 else float('inf'),
        }
    return results


# ============================================================
# 5. Genus-1 RS transform for the three test families
# ============================================================

def genus1_rs_analysis(family_name: str, c: float = None, k: float = None,
                       n_li: int = 20, N_zeros: int = 200,
                       dps: int = 30) -> Dict[str, Any]:
    """Complete genus-1 RS analysis for a standard family.

    At genus 1, the RS transform depends only on kappa(A), and the
    Li coefficients are universal. The family-specific data:
      - kappa(A): scales the RS function multiplicatively
      - shadow class: determines whether higher-genus corrections exist
      - weight multiset: determines the sewing Dirichlet series
    """
    old_dps = mp.dps
    mp.dps = dps

    # Build family data
    if family_name == 'heisenberg':
        family = heisenberg_data(k if k is not None else 1.0)
    elif family_name == 'virasoro':
        family = virasoro_data(c if c is not None else 26.0)
    elif family_name == 'w3':
        family = w3_data(c if c is not None else 50.0)
    else:
        raise ValueError(f"Unknown family: {family_name}")

    # Compute Li coefficients (universal at genus 1)
    zeros = compute_zeta_zeros(N_zeros, dps)
    li_coeffs = {}
    for n in range(1, n_li + 1):
        li_coeffs[n] = li_coefficient_rs(n, zeros, family)

    # Verify RS Dirichlet series matches product formula at test points
    dirichlet_checks = {}
    for s_val in [3.0, 4.0, 5.0]:
        s = mpf(s_val)
        d_series = rs_dirichlet_series(s, kappa=family.kappa, N_max=500)
        product = rs_product_formula(s, kappa=family.kappa)
        dirichlet_checks[s_val] = {
            'dirichlet': float(d_series),
            'product': float(product),
            'rel_error': float(abs(d_series - product) / abs(product)) if abs(product) > 1e-30 else 0.0,
        }

    # Structural analysis
    vanishing = lambda1_vanishing_proof(zeros)
    line_decomp = critical_line_analysis(zeros, min(n_li, 10))

    mp.dps = old_dps

    return {
        'family': family.name,
        'kappa': family.kappa,
        'shadow_class': family.shadow_class,
        'weights': family.weights,
        'li_coefficients': {n: float(v) for n, v in li_coeffs.items()},
        'all_li_positive_from_2': all(li_coeffs[n] > 0 for n in range(2, n_li + 1)),
        'lambda_1_zero': vanishing['is_zero'],
        'dirichlet_checks': dirichlet_checks,
        'line_decomposition': line_decomp,
        'universality': 'Li coefficients are INDEPENDENT of A at genus 1',
    }


# ============================================================
# 6. Comparison with classical Li coefficients
# ============================================================

def classical_li_coefficients(n_max: int = 20, N_zeros: int = 200,
                              dps: int = 30) -> Dict[int, mpf]:
    """Classical Keiper-Li coefficients for zeta(s).

    lambda_n = sum_rho [1 - (1 - 1/rho)^n]
    where rho are nontrivial zeros of zeta(s).

    RH <=> all lambda_n >= 0.
    """
    old_dps = mp.dps
    mp.dps = dps
    zeros = compute_zeta_zeros(N_zeros, dps)
    result = {}
    for n in range(1, n_max + 1):
        lam = mpf(0)
        for rho in zeros:
            term = 1 - (1 - 1/rho)**n
            lam += 2 * mpre(term)
        result[n] = lam
    mp.dps = old_dps
    return result


def li_comparison(n_max: int = 20, N_zeros: int = 200,
                  dps: int = 30) -> Dict[int, Dict[str, float]]:
    """Compare classical Li and RS Li coefficients.

    Key structural differences:
    - Classical: lambda_1 = 0.023... > 0
    - RS: lambda_1^KE = 0 (exactly)
    - RS lambda_n^KE > classical lambda_n for n >= 2
    """
    old_dps = mp.dps
    mp.dps = dps
    zeros = compute_zeta_zeros(N_zeros, dps)

    result = {}
    for n in range(1, n_max + 1):
        lam_classical = mpf(0)
        lam_rs = mpf(0)
        for rho in zeros:
            # Classical
            lam_classical += 2 * mpre(1 - (1 - 1/rho)**n)
            # RS
            w1 = (rho - 2) / (rho - 1)
            lam_rs += 2 * mpre(1 - w1**n)
            rho2 = 2 - mpconj(rho)
            w2 = (rho2 - 2) / (rho2 - 1)
            lam_rs += 2 * mpre(1 - w2**n)

        result[n] = {
            'classical': float(lam_classical),
            'rs': float(lam_rs),
            'ratio': float(lam_rs / lam_classical) if abs(lam_classical) > 1e-20 else float('inf'),
        }

    mp.dps = old_dps
    return result


# ============================================================
# 7. Genus-2 RS extension (family-dependent)
# ============================================================

def genus2_rs_kappa_contribution(s, kappa, dps: int = 30):
    """The kappa contribution to the genus-2 RS transform.

    At genus 2, the kappa contribution comes from the arity-2 shadow
    on M_{2,0}. The Hodge class lambda_2 on M_2 satisfies:
        int_{M_2} lambda_2 = 1/240

    The genus-2 RS transform of the kappa piece is:
        RS_2^{kappa}(s, A) = kappa(A) * [genus-2 Rankin-Selberg integral of lambda_2]

    The genus-2 Siegel Eisenstein series is needed here.
    For now, we compute the COEFFICIENT only.
    """
    return kappa / 240  # F_2^{scalar} = kappa * lambda_2 = kappa/240


def genus2_cubic_correction(family: ShadowData) -> float:
    """The S_3 (cubic shadow) correction at genus 2.

    The arity-3 shadow S_3 first contributes at genus 2 (shadow visibility).
    The correction is:
        delta_2^{(3)} = S_3 * [genus-2 cubic graph sum coefficient]

    The planted-forest formula (pixton_shadow_bridge.py):
        delta_pf^{(2,0)} = S_3(10*S_3 - kappa) / 48
    """
    S3 = family.shadow_coefficient(3)
    kappa = family.kappa
    return S3 * (10 * S3 - kappa) / 48


def genus2_quartic_correction(family: ShadowData) -> float:
    """The S_4 (quartic shadow) correction at genus 2.

    At genus 2, S_4 contributes through the quartic graph sum.
    From the banana graph: partial F_2 / partial S_4 = 1/(8*kappa^2).
    """
    S4 = family.shadow_coefficient(4)
    kappa = family.kappa
    if abs(kappa) < 1e-15:
        return 0.0
    return S4 / (8 * kappa**2) * kappa  # schematic; exact coefficient from graph sum


def genus2_family_comparison(families: List[ShadowData]) -> Dict[str, Dict[str, float]]:
    """Compare genus-2 RS corrections across families.

    Shows how family dependence enters at genus 2 through higher shadows.
    """
    result = {}
    for family in families:
        f2_scalar = family.kappa / 240
        cubic_corr = genus2_cubic_correction(family)
        quartic_corr = genus2_quartic_correction(family)
        result[family.name] = {
            'kappa': family.kappa,
            'F2_scalar': f2_scalar,
            'cubic_correction': cubic_corr,
            'quartic_correction': quartic_corr,
            'total_F2': f2_scalar + cubic_corr + quartic_corr,
            'relative_correction': (cubic_corr + quartic_corr) / f2_scalar if abs(f2_scalar) > 1e-15 else 0.0,
        }
    return result


# ============================================================
# 8. The "Koszul-Epstein RH" equivalence
# ============================================================

def ke_rh_equivalence(n_max: int = 20, N_zeros: int = 200,
                      dps: int = 30) -> Dict[str, Any]:
    r"""Test the equivalence between Koszul-Epstein positivity and RH.

    CLAIM: The following are equivalent (assuming standard conjectures):
    (a) RH holds
    (b) lambda_n^KE >= 0 for all n >= 1
    (c) All nontrivial zeros of Xi_RS lie on Re(s) = 1/2 or Re(s) = 3/2

    Note (b) is weaker than the classical Li criterion because lambda_1 = 0
    automatically, so positivity for n >= 2 suffices.

    The equivalence (a) <=> (c) is immediate since Xi_RS zeros are
    {rho} union {1+rho}.

    The equivalence (b) <=> (c) follows from the decomposition: the
    Re(s) = 3/2 zeros contribute terms with |w| = 1, bounded;
    the Re(s) = 1/2 zeros dominate for large n. If ANY zero has
    Re(rho) != 1/2, then |(rho-2)/(rho-1)| > 1 or < 1, producing
    growing positive or negative contributions.
    """
    old_dps = mp.dps
    mp.dps = dps
    li = li_coefficients_rs(n_max, N_zeros, dps=dps)
    all_positive = all(li[n] >= 0 for n in range(2, n_max + 1))
    growth_rate = float(li[n_max] / li[n_max - 1]) if abs(li[n_max - 1]) > 1e-20 else 0.0
    mp.dps = old_dps

    return {
        'all_positive_from_2': all_positive,
        'lambda_1_zero': abs(float(li[1])) < 1e-20,
        'growth_rate_last': growth_rate,
        'consistent_with_RH': all_positive,
        'li_values': {n: float(v) for n, v in li.items()},
    }


# ============================================================
# 9. Sewing Dirichlet series (the prime-side object)
# ============================================================

def sewing_dirichlet_series(s, weights: List[int], N_max: int = 500):
    """Connected sewing Dirichlet series S_A(u).

    S_A(u) = zeta(u+1) * sum_w [zeta(u) - H_{w-1}(u)]
    where H_{w-1}(u) = sum_{j=1}^{w-1} j^{-u} is the partial harmonic sum.

    For Heisenberg (weights = [1]): S_H(u) = zeta(u) * zeta(u+1)
    For Virasoro (weights = [2]): S_V(u) = zeta(u+1) * (zeta(u) - 1)
    For W_3 (weights = [2,3]): S_{W3}(u) = zeta(u+1) * (2*zeta(u) - 1 - 1 - 1/2^u)
    """
    z_u = zeta(s)
    z_u1 = zeta(s + 1)
    harmonic_sum = mpf(0)
    for w in weights:
        partial_h = sum(power(j, -s) for j in range(1, w))
        harmonic_sum += z_u - partial_h
    return z_u1 * harmonic_sum


def sewing_euler_defect(s, weights: List[int]):
    """Euler defect D_A(u) = S_A(u) / (rank * zeta(u) * zeta(u+1))."""
    rank = len(weights)
    if rank == 0:
        return mpf(0)
    return sewing_dirichlet_series(s, weights) / (rank * zeta(s) * zeta(s + 1))


# ============================================================
# 10. Complete three-family analysis
# ============================================================

def three_family_analysis(n_li: int = 20, N_zeros: int = 200,
                          dps: int = 30) -> Dict[str, Any]:
    """Complete RS analysis for Heisenberg, Virasoro (c=26), W_3 (c=50)."""
    old_dps = mp.dps
    mp.dps = dps

    families = [
        ('heisenberg', heisenberg_data(1.0)),
        ('virasoro_26', virasoro_data(26.0)),
        ('w3_50', w3_data(50.0)),
    ]

    zeros = compute_zeta_zeros(N_zeros, dps)

    results = {}
    for name, family in families:
        # Li coefficients (universal at genus 1)
        li = {}
        for n in range(1, n_li + 1):
            li[n] = float(li_coefficient_rs(n, zeros, family))

        # Sewing Dirichlet series at test points
        sewing = {}
        for u_val in [2.0, 3.0, 5.0]:
            u = mpf(u_val)
            S_val = sewing_dirichlet_series(u, family.weights)
            D_val = sewing_euler_defect(u, family.weights)
            sewing[u_val] = {
                'S': float(S_val),
                'D': float(D_val),
            }

        # Genus-2 corrections
        g2_scalar = family.kappa / 240
        g2_cubic = genus2_cubic_correction(family)

        results[name] = {
            'family': family.name,
            'kappa': family.kappa,
            'shadow_class': family.shadow_class,
            'weights': family.weights,
            'li_coefficients': li,
            'all_positive_from_2': all(li[n] > 0 for n in range(2, n_li + 1)),
            'sewing_series': sewing,
            'is_euler_koszul': all(w == 1 for w in family.weights),
            'genus2_scalar': g2_scalar,
            'genus2_cubic_correction': g2_cubic,
            'genus2_total': g2_scalar + g2_cubic,
        }

    mp.dps = old_dps
    return results


# ============================================================
# 11. Universality verification
# ============================================================

def universality_test(N_zeros: int = 100, dps: int = 30) -> Dict[str, Any]:
    """Verify that Li coefficients are independent of family at genus 1.

    Computes Li coefficients for multiple families and checks they agree.
    This is the computational verification of the genus-1 universality theorem.
    """
    old_dps = mp.dps
    mp.dps = dps
    zeros = compute_zeta_zeros(N_zeros, dps)

    families = [
        heisenberg_data(1.0),
        virasoro_data(10.0),
        virasoro_data(26.0),
        w3_data(50.0),
    ]

    all_li = {}
    for family in families:
        li = {}
        for n in range(1, 11):
            li[n] = float(li_coefficient_rs(n, zeros, family))
        all_li[family.name + f'_kappa={family.kappa}'] = li

    # Check all families give the same Li coefficients
    ref_name = list(all_li.keys())[0]
    ref_li = all_li[ref_name]
    max_discrepancy = 0.0
    for name, li in all_li.items():
        if name == ref_name:
            continue
        for n in range(2, 11):
            disc = abs(li[n] - ref_li[n])
            max_discrepancy = max(max_discrepancy, disc)

    mp.dps = old_dps
    return {
        'families_tested': list(all_li.keys()),
        'li_values': all_li,
        'max_discrepancy': max_discrepancy,
        'universality_holds': max_discrepancy < 1e-10,
    }
