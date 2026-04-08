r"""Genus-3 multi-weight universality failure: extending delta_F_2(W_3) to genus 3.

At genus 2, the multi-weight genus expansion (thm:multi-weight-genus-expansion)
gives F_2(W_3) = kappa * lambda_2^FP + delta_F_2^cross, where
delta_F_2(W_3) = (c + 204)/(16c) > 0 (PROVED, 73 tests).

This engine pushes the computation to GENUS 3, computing:

1. lambda_3^FP = 31/967680 from Bernoulli numbers (3 independent paths)
2. delta_F_3^cross(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240 c^2)
   via direct closed-form and cross-checked against the graph-sum engine
3. The genus-3 planted-forest correction for Virasoro (single-generator,
   uniform-weight: delta_F_3^cross = 0, but delta_pf^{(3,0)} != 0)
4. A-hat generating function verification
5. Complementarity and cross-family checks
6. Growth analysis: delta_F_3/delta_F_2 ratio

EPISTEMIC STATUS
================

PROVED:
  - lambda_3^FP = 31/967680 (Bernoulli formula, 3 paths)
  - delta_F_3^cross(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240 c^2)
    (direct graph sum over 42 stable graphs, closed-form match, rational
    reconstruction, 7-path verification in theorem_thm_d_multiweight_frontier_engine)
  - F_3(W_3) = kappa * lambda_3^FP + delta_F_3^cross (definition)
  - delta_F_3 > 0 for all c > 0 (all numerator coefficients positive)
  - Virasoro is uniform-weight => delta_F_3^cross(Vir) = 0

CONJECTURAL:
  - The genus-3 planted-forest formula (eq:delta-pf-genus3-explicit) uses
    approximate genus-1+ vertex weights; the S_4/S_5 coefficients are exact
    but genus-1+ vertex coefficients are approximate.

Manuscript references:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
    eq:delta-pf-genus3-explicit (higher_genus_modular_koszul.tex)
    comp:w3-genus3-cross (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)

Kappa conventions (AP1/AP9, from landscape_census.tex):
    Heisenberg H_k:     kappa = k
    Virasoro Vir_c:      kappa = c/2
    W_3 at c:            kappa = 5c/6  (= kappa_T + kappa_W = c/2 + c/3)
    Affine V_k(sl_2):    kappa = 3(k+2)/4
    Beta-gamma:          kappa = 1

Shadow data (Virasoro, from landscape_census.tex):
    S_3 = 2
    S_4 = Q^contact = 10/[c(5c+22)]
    S_5 = -48/[c^2(5c+22)]
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# Section 1: Bernoulli numbers (self-contained, Akiyama-Tanigawa)
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n via Akiyama-Tanigawa algorithm.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42,
    B_8 = -1/30, B_10 = 5/66.
    """
    if n < 0:
        raise ValueError(f"Bernoulli requires n >= 0, got {n}")
    a = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        a[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


@lru_cache(maxsize=64)
def _bernoulli_recurrence(n: int) -> Fraction:
    """Exact Bernoulli number B_n via standard recurrence (independent path).

    sum_{k=0}^{n-1} C(n, k) B_k = 0 for n >= 2 with B_1 = -1/2.
    """
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        bk = _bernoulli_recurrence(k)
        if bk != 0:
            s += Fraction(comb(n + 1, k)) * bk
    return -s / Fraction(n + 1)


# ============================================================================
# Section 2: Faber-Pandharipande numbers (3 independent paths)
# ============================================================================

@lru_cache(maxsize=32)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    PATH 1: Direct from Bernoulli via Akiyama-Tanigawa.

    Exact values:
        g=1: 1/24
        g=2: 7/5760  (NOT 1/1152 -- AP38!)
        g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs(B2g) / Fraction(factorial(2 * g)))


def lambda_fp_path2(g: int) -> Fraction:
    r"""Faber-Pandharipande number via independent Bernoulli recurrence.

    PATH 2: Uses _bernoulli_recurrence instead of Akiyama-Tanigawa.
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli_recurrence(2 * g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs(B2g) / Fraction(factorial(2 * g)))


def lambda_fp_from_ahat(g: int) -> Fraction:
    r"""Faber-Pandharipande number from the A-hat genus expansion.

    PATH 3: A-hat(ix) = (x/2)/sin(x/2). The coefficient of x^{2g} is
    2^{2g} * lambda_g^FP. So lambda_g^FP = [coeff of x^{2g}] / 2^{2g}.

    The coefficient of x^{2g} in (x/2)/sinh(x/2) is
        (2 - 2^{2g}) * B_{2g} / (2g)!
    Substituting x -> ix: the coefficient of x^{2g} in A-hat(ix) is
        (-1)^g * (2 - 2^{2g}) * B_{2g} / (2g)!
    Since B_{2g} has sign (-1)^{g+1}:
        = 2 * (2^{2g-1} - 1) * |B_{2g}| / (2g)!
    Hence lambda_g^FP = this / 2^{2g} = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1}(2g)!).
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    ahat_coeff = Fraction(2) * (2 ** (2 * g - 1) - 1) * abs(B2g) / Fraction(factorial(2 * g))
    return ahat_coeff / Fraction(2 ** (2 * g))


# ============================================================================
# Section 3: Virasoro shadow data
# ============================================================================

def virasoro_shadow(c: Fraction) -> Dict[str, Fraction]:
    r"""Virasoro shadow data. Class M, r_max = infinity.

    kappa = c/2
    S_3 = 2
    S_4 = Q^contact = 10 / [c(5c+22)]
    S_5 = -48 / [c^2(5c+22)]

    S_5 first appears at genus 3 (cor:shadow-visibility-genus: g_min(S_5) = 3).
    """
    if c == Fraction(0):
        raise ValueError("c = 0: Virasoro degenerate")
    denom = c * (5 * c + 22)
    if denom == 0:
        raise ValueError("c = -22/5: quartic diverges")
    return {
        'kappa': c / 2,
        'S_3': Fraction(2),
        'S_4': Fraction(10) / denom,
        'S_5': Fraction(-48) / (c * denom),
    }


def w3_shadow(c: Fraction) -> Dict[str, Any]:
    r"""W_3 shadow data.

    Two channels: T (weight 2, kappa_T = c/2), W (weight 3, kappa_W = c/3).
    Total kappa(W_3) = 5c/6.
    T-line has same shadow data as Virasoro at c.
    W-line: S_3^W = 0 (Z_2 parity), S_4^W = 2560/[c(5c+22)^3].
    """
    vir = virasoro_shadow(c)
    return {
        'kappa_T': vir['kappa'],
        'kappa_W': c / 3,
        'kappa_total': Fraction(5) * c / 6,
        'S_3_T': vir['S_3'],
        'S_4_T': vir['S_4'],
        'S_5_T': vir['S_5'],
    }


def heisenberg_shadow(k: Fraction = Fraction(1)) -> Dict[str, Fraction]:
    """Heisenberg shadow data. Class G, r_max = 2. All higher shadows vanish."""
    return {
        'kappa': k,
        'S_3': Fraction(0),
        'S_4': Fraction(0),
        'S_5': Fraction(0),
    }


def affine_sl2_shadow(k: Fraction = Fraction(1)) -> Dict[str, Fraction]:
    r"""Affine V_k(sl_2) shadow data. Class L, r_max = 3.

    S_3 = 4/(k+2), S_4 = 0, S_5 = 0.
    """
    if k == Fraction(-2):
        raise ValueError("k = -2 is the critical level")
    return {
        'kappa': Fraction(3) * (k + 2) / Fraction(4),
        'S_3': Fraction(4) / (k + 2),
        'S_4': Fraction(0),
        'S_5': Fraction(0),
    }


# ============================================================================
# Section 4: Genus-2 cross-channel correction (baseline, PROVED)
# ============================================================================

def delta_F2_W3(c: Fraction) -> Fraction:
    r"""Cross-channel correction at genus 2: delta_F_2(W_3) = (c + 204)/(16c).

    PROVED. Computed by summing mixed-channel amplitudes over all 6 boundary
    stable graphs of M-bar_{2,0}. All numerator coefficients positive.
    """
    return (c + Fraction(204)) / (16 * c)


def delta_F2_W3_decomposition(c: Fraction) -> Dict[str, Fraction]:
    """Per-graph decomposition of delta_F_2(W_3)."""
    banana = Fraction(3) / c
    theta = Fraction(9) / (2 * c)
    lollipop = Fraction(1, 16)
    barbell = Fraction(21) / (4 * c)
    fig_eight = Fraction(0)
    dumbbell = Fraction(0)
    total = banana + theta + lollipop + barbell + fig_eight + dumbbell
    return {
        'banana': banana,
        'theta': theta,
        'lollipop': lollipop,
        'barbell': barbell,
        'fig_eight': fig_eight,
        'dumbbell': dumbbell,
        'total': total,
        'formula': delta_F2_W3(c),
        'match': total == delta_F2_W3(c),
    }


# ============================================================================
# Section 5: Genus-3 cross-channel correction (the new computation)
# ============================================================================

def delta_F3_W3(c: Fraction) -> Fraction:
    r"""Cross-channel correction at genus 3.

    delta_F_3(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)

    PROVED: computed by summing mixed-channel amplitudes over all 42 stable
    graphs of M-bar_{3,0}. The closed-form was obtained by rational
    reconstruction from integer c-evaluations and verified against the
    direct graph sum at 20+ integer values (7-path verification in
    theorem_thm_d_multiweight_frontier_engine.py).

    All numerator coefficients (5, 3792, 1149120, 217071360) are positive,
    so delta_F_3 > 0 for all c > 0.

    The c-power structure: numerator has degree 3 = 2g - 3 = 3, denominator
    has c^{g-1} = c^2. This matches the structural prediction from the
    loop-number decomposition: h^1 = k contributes at order c^{1-k}.
    """
    num = 5 * c**3 + 3792 * c**2 + 1149120 * c + 217071360
    return num / (138240 * c**2)


def delta_F3_W3_coefficients() -> Dict[str, Fraction]:
    """Numerator coefficients of delta_F_3(W_3) and denominator.

    delta_F_3 = (a_3 c^3 + a_2 c^2 + a_1 c + a_0) / (D * c^2)
    """
    return {
        'a_3': Fraction(5),
        'a_2': Fraction(3792),
        'a_1': Fraction(1149120),
        'a_0': Fraction(217071360),
        'D': Fraction(138240),
    }


def delta_F3_W3_from_universal(c: Fraction) -> Fraction:
    r"""Cross-check via the universal N-formula at N=3.

    The universal gravitational cross-channel at genus 3 is
    delta_F_3^grav(W_N, c) = D*c + C + B/c + A/c^2
    with coefficients that are polynomials in N.

    For W_3 (N=3), gravitational = full (no higher-spin exchange),
    so this should agree with delta_F_3_W3.
    """
    N = 3
    D = Fraction(N - 2, 27648)
    C = Fraction((N - 2) * (35 * N**2 + 133 * N + 234), 34560)
    B = Fraction((N - 2) * (15 * N**4 + 147 * N**3 + 517 * N**2
                            + 947 * N + 1686), 1728)
    A = Fraction((N - 2) * (120 * N**6 + 1300 * N**5 + 5918 * N**4
                            + 14786 * N**3 + 27592 * N**2
                            + 36369 * N + 56475), 1080)
    return D * c + C + B / c + A / c**2


# ============================================================================
# Section 6: Planted-forest correction at genus 3
# ============================================================================

def planted_forest_g3_generic(kappa: Fraction, S_3: Fraction,
                               S_4: Fraction, S_5: Fraction) -> Fraction:
    r"""Generic planted-forest correction delta_pf^{(3,0)}.

    From eq:delta-pf-genus3-explicit, the 11-term polynomial:

        delta_pf^{(3,0)} =
            7/8 * S_3 * S_5
          + 3/512 * S_3^3 * kappa
          - 5/128 * S_3^4
          - 167/96 * S_3^2 * S_4
          + 83/1152 * S_3 * S_4 * kappa
          - 343/2304 * S_3 * kappa
          - 1/4608 * S_3^2 * kappa^2
          - 1/82944 * S_3 * kappa^3
          - 7/12 * S_4^2
          + 1/1152 * S_4 * kappa^2
          - 1/96 * S_5 * kappa

    NOTE: genus-1+ vertex weights are approximate. The S_4/S_5 coefficients
    (7/8, -167/96, -7/12, -1/96) are exact. Mixed genus-0/genus-1 terms
    use the approximation ell_k^{(1)} ~ kappa for valence >= 3 vertices.
    """
    return (
        Fraction(7, 8) * S_3 * S_5
        + Fraction(3, 512) * S_3**3 * kappa
        - Fraction(5, 128) * S_3**4
        - Fraction(167, 96) * S_3**2 * S_4
        + Fraction(83, 1152) * S_3 * S_4 * kappa
        - Fraction(343, 2304) * S_3 * kappa
        - Fraction(1, 4608) * S_3**2 * kappa**2
        - Fraction(1, 82944) * S_3 * kappa**3
        - Fraction(7, 12) * S_4**2
        + Fraction(1, 1152) * S_4 * kappa**2
        - Fraction(1, 96) * S_5 * kappa
    )


def planted_forest_g3_virasoro(c: Fraction) -> Fraction:
    r"""Planted-forest correction for Virasoro at genus 3.

    Substitutes kappa = c/2, S_3 = 2, S_4 = 10/[c(5c+22)],
    S_5 = -48/[c^2(5c+22)].

    Virasoro is uniform-weight (single generator T), so
    delta_F_3^cross(Vir) = 0. The planted-forest correction is the
    ONLY beyond-scalar contribution for single-generator algebras.
    """
    sd = virasoro_shadow(c)
    return planted_forest_g3_generic(
        sd['kappa'], sd['S_3'], sd['S_4'], sd['S_5']
    )


def planted_forest_g3_heisenberg(k: Fraction = Fraction(1)) -> Fraction:
    """Planted-forest for Heisenberg: identically 0 (class G, all S_k = 0)."""
    sd = heisenberg_shadow(k)
    return planted_forest_g3_generic(
        sd['kappa'], sd['S_3'], sd['S_4'], sd['S_5']
    )


def planted_forest_g3_affine_sl2(k: Fraction = Fraction(1)) -> Fraction:
    r"""Planted-forest for affine V_k(sl_2) at genus 3.

    Class L: S_4 = S_5 = 0, so only S_3- and kappa-dependent terms survive.
    """
    sd = affine_sl2_shadow(k)
    return planted_forest_g3_generic(
        sd['kappa'], sd['S_3'], sd['S_4'], sd['S_5']
    )


# ============================================================================
# Section 7: Full genus-3 free energy decomposition
# ============================================================================

def genus3_free_energy(family: str,
                       param: Optional[Fraction] = None) -> Dict[str, Any]:
    r"""Complete genus-3 free energy decomposition.

    F_3(A) = kappa * lambda_3^FP + delta_pf^{(3,0)} + delta_F_3^cross

    For uniform-weight: delta_F_3^cross = 0.
    For multi-weight (W_3): delta_F_3^cross = (5c^3+3792c^2+...)/138240c^2.
    """
    fp3 = lambda_fp(3)

    if family == 'Heisenberg':
        k = param if param is not None else Fraction(1)
        kappa = k
        delta_pf = planted_forest_g3_heisenberg(k)
        delta_cross = Fraction(0)
        name = f'Heisenberg_k{k}'
    elif family == 'Virasoro':
        c = param if param is not None else Fraction(26)
        kappa = c / 2
        delta_pf = planted_forest_g3_virasoro(c)
        delta_cross = Fraction(0)
        name = f'Virasoro_c{c}'
    elif family == 'affine_sl2':
        k = param if param is not None else Fraction(1)
        kappa = Fraction(3) * (k + 2) / Fraction(4)
        delta_pf = planted_forest_g3_affine_sl2(k)
        delta_cross = Fraction(0)
        name = f'affine_sl2_k{k}'
    elif family == 'W_3':
        c = param if param is not None else Fraction(50)
        kappa = Fraction(5) * c / 6
        delta_pf = planted_forest_g3_virasoro(c)  # T-line projection
        delta_cross = delta_F3_W3(c)
        name = f'W_3_c{c}'
    else:
        raise ValueError(f"Unknown family: {family}")

    scalar = kappa * fp3
    total = scalar + delta_pf + delta_cross

    return {
        'name': name,
        'family': family,
        'kappa': kappa,
        'lambda_3_FP': fp3,
        'scalar_F3': scalar,
        'delta_pf': delta_pf,
        'delta_cross': delta_cross,
        'total_F3': total,
        'is_uniform_weight': delta_cross == 0,
    }


# ============================================================================
# Section 8: A-hat generating function verification
# ============================================================================

def ahat_verification(max_g: int = 5) -> Dict[int, Dict[str, Any]]:
    r"""Verify lambda_g^FP against the A-hat genus at multiple genera.

    The A-hat genus A-hat(ix) = (x/2)/sin(x/2) has the expansion
        A-hat(ix) = 1 + sum_{g>=1} a_g x^{2g}
    where a_g = 2^{2g} * lambda_g^FP.

    This provides an independent cross-check on the Bernoulli computation.
    """
    results = {}
    for g in range(1, max_g + 1):
        v1 = lambda_fp(g)
        v2 = lambda_fp_path2(g)
        v3 = lambda_fp_from_ahat(g)
        all_agree = (v1 == v2 == v3)
        results[g] = {
            'path1_akiyama_tanigawa': v1,
            'path2_recurrence': v2,
            'path3_ahat': v3,
            'all_agree': all_agree,
        }
    return results


# ============================================================================
# Section 9: Genus growth analysis
# ============================================================================

def cross_channel_growth() -> Dict[str, Any]:
    r"""Analyze the growth of delta_F_g^cross(W_3) from genus 2 to genus 3.

    At genus 2: delta_F_2 = (c + 204)/(16c)
    At genus 3: delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240c^2)

    The ratio delta_F_3/delta_F_2 at large c approaches
        (5c^3/(138240c^2)) / (c/(16c)) = (5c/138240) / (1/16) = 80c/138240 = c/1728.
    So the ratio grows linearly in c: the cross-channel correction grows
    FASTER than the scalar part (which grows like kappa * lambda_g ~ c).

    The growth in denominator complexity: 16c -> 138240c^2. The denominator
    of delta_F_g has c^{g-1} from the loop expansion.
    """
    results = {}
    for c_val in [1, 10, 26, 50, 100]:
        c = Fraction(c_val)
        d2 = delta_F2_W3(c)
        d3 = delta_F3_W3(c)
        fp2 = lambda_fp(2)
        fp3 = lambda_fp(3)
        kappa = Fraction(5) * c / 6
        scalar2 = kappa * fp2
        scalar3 = kappa * fp3

        results[c_val] = {
            'delta_F2': d2,
            'delta_F3': d3,
            'ratio_F3_F2': d3 / d2 if d2 != 0 else None,
            'scalar_F2': scalar2,
            'scalar_F3': scalar3,
            'cross_over_scalar_g2': d2 / scalar2 if scalar2 != 0 else None,
            'cross_over_scalar_g3': d3 / scalar3 if scalar3 != 0 else None,
        }
    return results


def genus3_positivity(c_values: Optional[List[int]] = None) -> Dict[int, bool]:
    r"""Verify delta_F_3(W_3) > 0 for positive c.

    All numerator coefficients (5, 3792, 1149120, 217071360) are positive,
    so delta_F_3 > 0 for all c > 0. Verify numerically.
    """
    if c_values is None:
        c_values = [1, 2, 5, 10, 13, 26, 50, 100, 1000]
    return {
        c_val: delta_F3_W3(Fraction(c_val)) > 0
        for c_val in c_values
    }


# ============================================================================
# Section 10: Complementarity at genus 3
# ============================================================================

def virasoro_complementarity_g3(c: Fraction) -> Dict[str, Any]:
    r"""Complementarity check at genus 3 for Virasoro.

    Koszul dual: Vir_c <-> Vir_{26-c}.
    kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.

    Scalar sum: F_3^scalar(c) + F_3^scalar(26-c) = 13 * lambda_3^FP.
    """
    c_dual = 26 - c
    fp3 = lambda_fp(3)

    kappa_c = c / 2
    kappa_dual = c_dual / 2
    scalar_sum = (kappa_c + kappa_dual) * fp3
    expected_scalar = Fraction(13) * fp3

    pf_c = planted_forest_g3_virasoro(c)
    pf_dual = planted_forest_g3_virasoro(c_dual)
    pf_sum = pf_c + pf_dual

    return {
        'c': c,
        'c_dual': c_dual,
        'scalar_sum': scalar_sum,
        'scalar_expected': expected_scalar,
        'scalar_match': scalar_sum == expected_scalar,
        'pf_c': pf_c,
        'pf_dual': pf_dual,
        'pf_sum': pf_sum,
    }


def w3_complementarity_g3(c: Fraction) -> Dict[str, Any]:
    r"""Complementarity check at genus 3 for W_3.

    Koszul dual: W_3 at c <-> W_3 at 100 - c (K_3 = 100).
    kappa(W_3) + kappa(W_3') = 5c/6 + 5(100-c)/6 = 500/6 = 250/3.

    Cross-channel sum: delta_F_3(c) + delta_F_3(100-c).
    """
    c_dual = 100 - c
    fp3 = lambda_fp(3)

    kappa = Fraction(5) * c / 6
    kappa_dual = Fraction(5) * c_dual / 6
    scalar_sum = (kappa + kappa_dual) * fp3
    expected_scalar = Fraction(250, 3) * fp3

    delta_c = delta_F3_W3(c)
    delta_dual = delta_F3_W3(c_dual)
    cross_sum = delta_c + delta_dual

    return {
        'c': c,
        'c_dual': c_dual,
        'scalar_sum': scalar_sum,
        'scalar_expected': expected_scalar,
        'scalar_match': scalar_sum == expected_scalar,
        'cross_c': delta_c,
        'cross_dual': delta_dual,
        'cross_sum': cross_sum,
    }


# ============================================================================
# Section 11: Genus-2 vs genus-3 comparison table
# ============================================================================

def genus_comparison_table(c_values: Optional[List[int]] = None) -> Dict[str, Any]:
    """Side-by-side genus 2 and genus 3 data for W_3.

    For each c, shows: scalar part, cross-channel, planted-forest, total.
    """
    if c_values is None:
        c_values = [1, 13, 26, 50, 100]

    fp2 = lambda_fp(2)
    fp3 = lambda_fp(3)
    table = {}

    for c_val in c_values:
        c = Fraction(c_val)
        kappa = Fraction(5) * c / 6

        # Genus 2
        scalar2 = kappa * fp2
        cross2 = delta_F2_W3(c)
        total2 = scalar2 + cross2

        # Genus 3
        scalar3 = kappa * fp3
        cross3 = delta_F3_W3(c)
        total3 = scalar3 + cross3

        table[c_val] = {
            'kappa': kappa,
            'g2_scalar': scalar2,
            'g2_cross': cross2,
            'g2_total': total2,
            'g3_scalar': scalar3,
            'g3_cross': cross3,
            'g3_total': total3,
            'g3_to_g2_cross_ratio': cross3 / cross2 if cross2 != 0 else None,
        }

    return table


# ============================================================================
# Section 12: Depth-class planted-forest consistency
# ============================================================================

def depth_class_consistency_g3() -> Dict[str, bool]:
    r"""Verify planted-forest respects depth classes at genus 3.

    Class G (S_3 = S_4 = S_5 = 0): delta_pf = 0.
    Class L (S_4 = S_5 = 0): only kappa, S_3 contribute.
    Class C (S_5 = 0): only kappa, S_3, S_4 contribute.
    """
    # Class G: Heisenberg
    G_zero = (planted_forest_g3_heisenberg(Fraction(1)) == Fraction(0))
    G_zero_k5 = (planted_forest_g3_heisenberg(Fraction(5)) == Fraction(0))

    # Class L: set S_4 = S_5 = 0 in the generic formula
    k_L = Fraction(3, 4) * (Fraction(1) + 2)  # kappa for sl_2 k=1
    S_3_L = Fraction(4, 3)
    pf_L = planted_forest_g3_generic(k_L, S_3_L, Fraction(0), Fraction(0))
    L_nonzero = (pf_L != Fraction(0))

    # Verify affine gives same result
    pf_aff = planted_forest_g3_affine_sl2(Fraction(1))
    L_consistent = (pf_L == pf_aff)

    # Class C: set S_5 = 0 but S_4 != 0
    pf_C = planted_forest_g3_generic(Fraction(1), Fraction(2), Fraction(1, 10), Fraction(0))
    C_nonzero = (pf_C != Fraction(0))

    return {
        'G_zero_k1': G_zero,
        'G_zero_k5': G_zero_k5,
        'L_nonzero': L_nonzero,
        'L_consistent_with_affine': L_consistent,
        'C_nonzero': C_nonzero,
    }


# ============================================================================
# Section 13: Shadow visibility genus check
# ============================================================================

def shadow_visibility_check() -> Dict[str, Any]:
    r"""Verify the shadow visibility genus (cor:shadow-visibility-genus).

    g_min(S_r) = floor(r/2) + 1.
    S_2 (kappa): g_min = 1. Appears at genus 1.
    S_3:         g_min = 2. Appears at genus 2.
    S_4:         g_min = 3. Appears at genus 3 (also at genus 2 via banana).
    S_5:         g_min = 3. FIRST appears at genus 3.

    At genus 2: the planted-forest depends on S_3 and kappa only
    (S_4 enters through the banana graph but not through planted-forest trees).
    At genus 3: S_5 enters for the first time.
    """
    # Genus-2 PF depends on S_3 only (for the tree formula)
    # Check: setting S_5 != 0 in the genus-2 formula has no effect
    # (genus-2 doesn't use S_5 at all)
    from compute.lib.theorem_genus2_planted_forest_gz26_engine import (
        planted_forest_g2 as pf_g2,
    )
    # genus-2 formula: S_3 * (10*S_3 - kappa) / 48
    # No S_5 dependence: correct.

    # Genus-3 PF: S_5 enters via the 7/8 * S_3 * S_5 and -1/96 * S_5 * kappa terms
    # Verify: setting S_5 to different values changes the result
    pf_S5_zero = planted_forest_g3_generic(
        Fraction(1), Fraction(2), Fraction(1, 10), Fraction(0))
    pf_S5_one = planted_forest_g3_generic(
        Fraction(1), Fraction(2), Fraction(1, 10), Fraction(1))
    S5_matters = (pf_S5_zero != pf_S5_one)

    return {
        'g_min_S2': 1,
        'g_min_S3': 2,
        'g_min_S4': 3,
        'g_min_S5': 3,
        'S5_first_at_g3': S5_matters,
    }


# ============================================================================
# Section 14: Full verification summary
# ============================================================================

def full_verification_summary() -> Dict[str, Any]:
    """Comprehensive verification of all genus-3 multi-weight computations.

    Cross-checks lambda_3^FP (3 paths), delta_F_3 (closed-form vs universal),
    planted-forest (depth-class consistency), complementarity, positivity.
    """
    summary = {}

    # 1. lambda_3^FP
    lam3 = lambda_fp(3)
    lam3_p2 = lambda_fp_path2(3)
    lam3_ahat = lambda_fp_from_ahat(3)
    summary['lambda_3_FP'] = {
        'value': lam3,
        'path1': lam3,
        'path2': lam3_p2,
        'path3_ahat': lam3_ahat,
        'all_agree': lam3 == lam3_p2 == lam3_ahat,
        'equals_31_over_967680': lam3 == Fraction(31, 967680),
    }

    # 2. delta_F_3 closed-form vs universal
    for c_val in [1, 10, 26, 50]:
        c = Fraction(c_val)
        closed = delta_F3_W3(c)
        universal = delta_F3_W3_from_universal(c)
        summary[f'delta_F3_c{c_val}'] = {
            'closed_form': closed,
            'universal_N3': universal,
            'match': closed == universal,
        }

    # 3. Positivity
    summary['positivity'] = genus3_positivity()

    # 4. Depth-class consistency
    summary['depth_class'] = depth_class_consistency_g3()

    return summary
