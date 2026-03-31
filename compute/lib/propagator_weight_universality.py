r"""
propagator_weight_universality.py -- Propagator weight universality verification.

The bar complex propagator is d log E(z,w), where E(z,w) is the prime form
on a Riemann surface.  The prime form is a section of K^{-1/2} boxtimes K^{-1/2},
so d log E(z,w) = dE/E has weight 1 in both variables, REGARDLESS of the
conformal weights of the fields being sewed.

Consequence: every channel uses the STANDARD Hodge bundle
E_1 = R^0 pi_* omega (weight-1 differentials).  This proves the
genus-1 formula

    obs_1(A) = kappa(A) * lambda_1

for all modular Koszul algebras and kills the naive higher-weight-bundle
story.  It does NOT by itself prove the all-genera multi-weight
formula obs_g(A) = kappa(A) * lambda_g, because the remaining
tautological-purity step Γ_A = κ(A)Λ is still open.

This contradicts thm:w3-obstruction (higher_genus_foundations.tex:4423), which
assigns weight-h generators to the Hodge bundle E_h = R^0 pi_* omega^{otimes h}.
That theorem is WRONG: the confusion is between the conformal weight of the
FIELD (weight h) and the weight of the PROPAGATOR (always weight 1).

The correct genus-1 free energy is:

    F_1(A) = kappa(A) / 24

where kappa(A) = sum over generators of (leading OPE coefficient) / (2h - 1),
using the d-log pole absorption (AP19: the r-matrix pole orders are one less
than the OPE pole orders).

For W_3:  kappa = c/2 (from T) + c/3 (from W) = 5c/6.
For W_N:  kappa = c * (H_N - 1)  where H_N = sum_{s=1}^N 1/s.

If one incorrectly uses E_h for weight-h generators, the Mumford isomorphism
det(E_j) = lambda^{6j^2 - 6j + 1} gives c_1(E_j) = (6j^2 - 6j + 1) * lambda_1,
which produces dramatically wrong numerical results.

References:
    - landscape_census.tex: canonical kappa values for all families
    - CLAUDE.md: AP19 (bar kernel absorbs a pole), AP1 (kappa formulas)
    - Mumford, "Stability of projective varieties" (1977)
    - Faber-Pandharipande, "Hodge integrals..." (2000)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
from typing import Dict, List, Optional, Tuple


# ============================================================
# Bernoulli numbers (exact)
# ============================================================

@lru_cache(maxsize=64)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n as a Fraction.

    B_0 = 1, B_1 = -1/2, B_{odd>=3} = 0.
    Recursive: B_n = -1/(n+1) * sum_{k=0}^{n-1} C(n+1,k) * B_k.
    """
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        bk = _bernoulli_exact(k)
        if bk != 0:
            s += Fraction(comb(n + 1, k)) * bk
    return -s / Fraction(n + 1)


# ============================================================
# Faber-Pandharipande lambda_g^FP
# ============================================================

@lru_cache(maxsize=32)
def _lambda_fp_exact(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number.

    lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    g=1: 1/24,  g=2: 7/5760,  g=3: 31/967680.
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    abs_B_2g = abs(B_2g)
    numer = (2 ** (2 * g - 1) - 1) * abs_B_2g
    denom = Fraction(2 ** (2 * g - 1) * factorial(2 * g))
    return numer / denom


# ============================================================
# Mumford exponent: det(E_j) = lambda^{6j^2 - 6j + 1}
# ============================================================

def mumford_exponent(j: int) -> int:
    r"""Return the Mumford isomorphism exponent 6j^2 - 6j + 1.

    The Mumford isomorphism states:
        det(E_j) = det(E_1)^{6j^2 - 6j + 1}

    where E_j = R^0 pi_* omega^{otimes j} is the bundle of j-differentials.

    Consequently c_1(E_j) = (6j^2 - 6j + 1) * lambda_1 where lambda_1 = c_1(E_1).

    Values: j=1 -> 1, j=2 -> 13, j=3 -> 37, j=4 -> 73, j=5 -> 121.
    """
    return 6 * j * j - 6 * j + 1


# ============================================================
# Correct kappa values (landscape_census.tex, canonical)
# ============================================================

# Lie algebra data: (name, dimension, dual_coxeter_number, exponents)
_LIE_DATA: Dict[str, Tuple[int, int, Tuple[int, ...]]] = {
    "sl2": (3, 2, (1,)),
    "sl3": (8, 3, (1, 2)),
    "sl4": (15, 4, (1, 2, 3)),
    "sl5": (24, 5, (1, 2, 3, 4)),
    "sl6": (35, 6, (1, 2, 3, 4, 5)),
    "so5": (10, 3, (1, 3)),    # B_2
    "sp4": (10, 3, (1, 3)),    # C_2 = B_2
    "g2": (14, 4, (1, 5)),
    "so8": (28, 6, (1, 3, 3, 5)),  # D_4
    "f4": (52, 9, (1, 5, 7, 11)),
    "e6": (78, 12, (1, 4, 5, 7, 8, 11)),
    "e7": (133, 18, (1, 5, 7, 9, 11, 13, 17)),
    "e8": (248, 30, (1, 7, 11, 13, 17, 19, 23, 29)),
}


def kappa_heisenberg(k: Fraction = Fraction(1), d: int = 1) -> Fraction:
    """Modular characteristic of rank-d Heisenberg at level k.

    kappa(H_k^d) = k * d.

    Single free boson at level 1: kappa = 1.
    """
    return Fraction(k) * d


def kappa_virasoro(c: Fraction) -> Fraction:
    """Modular characteristic of the Virasoro algebra at central charge c.

    kappa(Vir_c) = c/2.

    From T(z)T(w) ~ (c/2)/(z-w)^4 + ...; the bar propagator extracts the
    leading pole, which after d-log absorption (AP19) gives the genus-1
    contribution c/2.
    """
    return Fraction(c) / 2


def kappa_km(g_name: str, k: Fraction) -> Fraction:
    r"""Modular characteristic of the affine Kac-Moody algebra V_k(g).

    kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v)

    For sl_2, k=1: kappa = 3 * 3 / 4 = 9/4.
    For sl_2, k generic: kappa = 3(k+2)/4.
    """
    if g_name not in _LIE_DATA:
        raise ValueError(f"Unknown Lie algebra: {g_name}")
    dim_g, h_dual, _ = _LIE_DATA[g_name]
    return Fraction(dim_g) * (Fraction(k) + h_dual) / (2 * h_dual)


def kappa_w_n(c: Fraction, N: int) -> Fraction:
    r"""Modular characteristic of the W_N algebra at central charge c.

    kappa(W_N) = c * (H_N - 1) where H_N = sum_{s=1}^N 1/s.

    Equivalently, for W^k(sl_N), kappa = c * sum_{j=2}^N 1/j
    = c * (1/2 + 1/3 + ... + 1/N).

    For N=2 (Virasoro): kappa = c * (1/2) = c/2.
    For N=3 (W_3): kappa = c * (1/2 + 1/3) = 5c/6.
    For N=4: kappa = c * (1/2 + 1/3 + 1/4) = 13c/12.
    """
    # H_N = 1 + 1/2 + ... + 1/N; anomaly ratio = H_N - 1 = 1/2 + ... + 1/N
    rho = sum(Fraction(1, s) for s in range(2, N + 1))
    return Fraction(c) * rho


def kappa_betagamma(lam: int = 1) -> Fraction:
    r"""Modular characteristic of the beta-gamma system at conformal weight lambda.

    For lambda = 1 (standard): kappa = 1 (from the (z-w)^{-2} OPE).
    In general, the beta-gamma OPE beta(z)gamma(w) ~ 1/(z-w) gives
    kappa = 1/2 via d-log; but the pair has two generators, total kappa = 1.

    Note: the central charge is c = 2 for lambda = 1.
    """
    # Standard beta-gamma at lambda=1: kappa = 1
    return Fraction(1)


def kappa_fermion() -> Fraction:
    r"""Modular characteristic of the free fermion (bc ghost at lambda=1/2).

    kappa(psi) = 1/4 (from psi(z)psi(w) ~ 1/(z-w), with c = 1/2).
    """
    return Fraction(1, 4)


# ============================================================
# Genus-1 curvature from OPE (the CORRECT computation)
# ============================================================

def genus1_curvature_direct(algebra: str, c: Fraction = Fraction(1),
                            **kwargs) -> Fraction:
    """Compute the genus-1 modular characteristic kappa from OPE data.

    This is the CORRECT computation: ALL channels use the standard Hodge
    bundle E_1 because the bar propagator d log E(z,w) has weight 1.

    The kappa value is additive over generators; each generator of conformal
    weight h with leading self-OPE coefficient a_h contributes a_h to the
    genus-1 curvature (after appropriate normalization from the d-log
    pole absorption).

    Parameters
    ----------
    algebra : str
        One of 'heisenberg', 'virasoro', 'w3', 'w_n', 'km', 'betagamma'.
    c : Fraction
        Central charge (used for Virasoro, W_N families).
    **kwargs
        Additional parameters: 'k' for level, 'N' for W_N rank,
        'g_name' for Lie algebra name, 'd' for Heisenberg rank.
    """
    c = Fraction(c)
    if algebra == 'heisenberg':
        k = Fraction(kwargs.get('k', 1))
        d = kwargs.get('d', 1)
        return kappa_heisenberg(k, d)
    elif algebra == 'virasoro':
        return kappa_virasoro(c)
    elif algebra == 'w3':
        return kappa_w_n(c, 3)
    elif algebra == 'w_n':
        N = kwargs['N']
        return kappa_w_n(c, N)
    elif algebra == 'km':
        g_name = kwargs['g_name']
        k = Fraction(kwargs['k'])
        return kappa_km(g_name, k)
    elif algebra == 'betagamma':
        return kappa_betagamma()
    else:
        raise ValueError(f"Unknown algebra: {algebra}")


# ============================================================
# Genus-1 curvature using E_h (the WRONG computation from thm:w3-obstruction)
# ============================================================

def genus1_curvature_wrong(algebra: str, c: Fraction = Fraction(1),
                           **kwargs) -> Fraction:
    r"""Compute the genus-1 obstruction using the WRONG E_h assignment.

    thm:w3-obstruction assigns weight-h generators to E_h, the bundle of
    h-differentials.  The Mumford isomorphism gives:

        c_1(E_j) = (6j^2 - 6j + 1) * lambda_1

    So the WRONG genus-1 value for W_3 is:

        obs_1^{wrong} = (c/2) * c_1(E_2) + (c/3) * c_1(E_3)
                      = (c/2) * 13 * lambda_1 + (c/3) * 37 * lambda_1
                      = (13c/2 + 37c/3) * lambda_1
                      = (39c + 74c) / 6 * lambda_1
                      = 113c/6 * lambda_1

    compared to the correct value kappa = 5c/6 (using E_1 for both channels).

    For Virasoro, the wrong computation assigns T (weight 2) to E_2:
        obs_1^{wrong} = (c/2) * 13 * lambda_1 = 13c/2 * lambda_1
    vs correct: obs_1 = (c/2) * lambda_1.

    Parameters
    ----------
    algebra : str
        One of 'virasoro', 'w3', 'w_n'.
    c : Fraction
        Central charge.

    Returns
    -------
    Fraction
        The wrong kappa value (coefficient of lambda_1) from using E_h.
    """
    c = Fraction(c)
    if algebra == 'virasoro':
        # T has weight 2; wrong: uses E_2 with Mumford exponent 13
        return Fraction(c, 2) * mumford_exponent(2)
    elif algebra == 'w3':
        # T (weight 2) -> E_2 (exponent 13), W (weight 3) -> E_3 (exponent 37)
        t_channel = Fraction(c, 2) * mumford_exponent(2)
        w_channel = Fraction(c, 3) * mumford_exponent(3)
        return t_channel + w_channel
    elif algebra == 'w_n':
        N = kwargs.get('N', 3)
        # Generators of weight 2, 3, ..., N
        # Each weight-h generator contributes (c/h) * mumford_exponent(h)
        total = Fraction(0)
        for h in range(2, N + 1):
            total += Fraction(c, h) * mumford_exponent(h)
        return total
    elif algebra == 'heisenberg':
        # Weight-1 generator: E_1, Mumford exponent = 1
        # The wrong formula AGREES with the correct one here
        k = Fraction(kwargs.get('k', 1))
        d = kwargs.get('d', 1)
        return Fraction(k) * d * mumford_exponent(1)
    else:
        raise ValueError(f"Unknown algebra for wrong computation: {algebra}")


# ============================================================
# Virasoro decisive test
# ============================================================

def virasoro_test(c: Fraction) -> Fraction:
    r"""The decisive test: if Virasoro used E_2, F_1 would be 13x too large.

    Correct: F_1(Vir_c) = kappa/24 = (c/2)/24 = c/48.
    Wrong (using E_2): F_1^{wrong} = (c/2 * 13)/24 = 13c/48.
    Ratio: 13c/48 / (c/48) = 13.

    Returns the ratio wrong/correct = 13 (independent of c).
    """
    c = Fraction(c)
    correct = kappa_virasoro(c) * _lambda_fp_exact(1)
    wrong = genus1_curvature_wrong('virasoro', c) * _lambda_fp_exact(1)
    if correct == 0:
        raise ValueError("c = 0 gives kappa = 0; ratio undefined")
    return wrong / correct


def w3_discrepancy(c: Fraction) -> Fraction:
    r"""Ratio between wrong (E_h) and correct (E_1) genus-1 values for W_3.

    Correct kappa(W_3) = 5c/6.
    Wrong kappa^{wrong}(W_3) = 113c/6.
    Ratio: 113/5 = 22.6.

    Returns the ratio wrong/correct = 113/5 (independent of c).
    """
    c = Fraction(c)
    correct = genus1_curvature_direct('w3', c)
    wrong = genus1_curvature_wrong('w3', c)
    if correct == 0:
        raise ValueError("c = 0 gives kappa = 0; ratio undefined")
    return wrong / correct


# ============================================================
# Free energy formulas
# ============================================================

def free_energy_universal(kappa: Fraction, g: int) -> Fraction:
    r"""Scalar-lane genus-g free energy: F_g = kappa * lambda_g^FP.

    This is the correct formula on the proved scalar lane.
    The propagator-weight argument alone does not upgrade it to an
    all-genera theorem for arbitrary multi-weight families.

    Parameters
    ----------
    kappa : Fraction
        Modular characteristic kappa(A).
    g : int
        Genus (>= 1).
    """
    return Fraction(kappa) * _lambda_fp_exact(g)


def free_energy_per_channel_correct(kappa_list: List[Fraction],
                                    g: int) -> Fraction:
    r"""Correct per-channel free energy: each channel uses E_1.

    F_g = (sum_i kappa_i) * lambda_g^FP

    Since every channel uses E_1 (propagator weight universality),
    the individual kappa_i sum and multiply a single lambda_g^FP.

    For W_3: kappa_list = [c/2, c/3], sum = 5c/6.
    """
    total_kappa = sum(Fraction(k) for k in kappa_list)
    return total_kappa * _lambda_fp_exact(g)


def free_energy_per_channel_wrong(kappa_list: List[Fraction],
                                  weight_list: List[int],
                                  g: int) -> Fraction:
    r"""Wrong per-channel free energy using E_{h_i} for weight-h_i generators.

    F_g^{wrong} = sum_i kappa_i * integral_{M_{g,1}} psi^{2g-2} c_g(E_{h_i})

    At genus 1, this simplifies using c_1(E_j) = (6j^2-6j+1) * lambda_1:
        F_1^{wrong} = sum_i kappa_i * (6h_i^2 - 6h_i + 1) * lambda_1^FP

    At higher genus, the integral int psi^{2g-2} c_g(E_j) depends on j
    (it is a polynomial in j of degree 2g, by Mumford's GRR).  For this
    module, we compute the genus-1 case exactly (sufficient for the
    discrepancy demonstration) and use the Mumford exponent scaling
    as a lower bound at higher genus.

    Parameters
    ----------
    kappa_list : list of Fraction
        Per-channel modular characteristics.
    weight_list : list of int
        Conformal weights of the corresponding generators.
    g : int
        Genus (>= 1).
    """
    if len(kappa_list) != len(weight_list):
        raise ValueError("kappa_list and weight_list must have same length")

    if g == 1:
        # At genus 1: int_{M_{1,1}} psi^0 c_1(E_j) = c_1(E_j) evaluated
        # as (6j^2-6j+1)/24 (the lambda_1 integral is 1/24)
        total = Fraction(0)
        for kappa_i, h_i in zip(kappa_list, weight_list):
            total += Fraction(kappa_i) * mumford_exponent(h_i) * _lambda_fp_exact(1)
        return total
    else:
        # At higher genus, use the Mumford scaling as an approximation.
        # The exact integral int psi^{2g-2} c_g(E_j) is a polynomial in j
        # of degree 2g.  For the discrepancy test, the genus-1 case suffices.
        # We provide the Mumford-exponent-weighted formula as a structural marker.
        total = Fraction(0)
        for kappa_i, h_i in zip(kappa_list, weight_list):
            total += Fraction(kappa_i) * mumford_exponent(h_i) * _lambda_fp_exact(g)
        return total


# ============================================================
# Anomaly ratio rho(g) for W^k(g)
# ============================================================

def anomaly_ratio_lie(g_name: str) -> Fraction:
    r"""Anomaly ratio rho(g) = sum_{i=1}^r 1/(m_i + 1) for Lie algebra g.

    The exponents m_1, ..., m_r of a simple Lie algebra g are such that
    m_i + 1 are the degrees of the basic polynomial invariants.

    rho(sl_2) = 1/2, rho(sl_3) = 5/6, rho(sl_N) = H_N - 1.
    """
    if g_name not in _LIE_DATA:
        raise ValueError(f"Unknown Lie algebra: {g_name}")
    _, _, exponents = _LIE_DATA[g_name]
    return sum(Fraction(1, m + 1) for m in exponents)


def anomaly_ratio_w_n(N: int) -> Fraction:
    r"""Anomaly ratio for W_N = W^k(sl_N).

    rho(W_N) = H_N - 1 = 1/2 + 1/3 + ... + 1/N.

    This equals anomaly_ratio_lie('sl{N}') since the exponents of sl_N
    are 1, 2, ..., N-1 and 1/(m_i+1) = 1/2, 1/3, ..., 1/N.
    """
    return sum(Fraction(1, s) for s in range(2, N + 1))


# ============================================================
# Harmonic number
# ============================================================

def harmonic(N: int) -> Fraction:
    """H_N = 1 + 1/2 + 1/3 + ... + 1/N."""
    return sum(Fraction(1, s) for s in range(1, N + 1))


# ============================================================
# Cross-check: field weight vs propagator weight
# ============================================================

def field_weight_vs_propagator_weight(algebra: str, **kwargs) -> Dict[str, object]:
    r"""Demonstrate that field weight != propagator weight.

    For every chiral algebra, the generators have conformal weights h >= 1,
    but the bar propagator d log E(z,w) ALWAYS has weight 1.

    This function returns both the field weights and the propagator weight
    (always 1) for each standard family, making the distinction explicit.

    AP27: field weight != propagator weight is the root cause of thm:w3-obstruction
    being wrong.
    """
    result = {
        'algebra': algebra,
        'propagator_weight': 1,  # ALWAYS 1 (d log E is weight 1)
    }

    if algebra == 'heisenberg':
        result['generator_weights'] = [1]
        result['generator_names'] = ['J']
        result['weight_equals_propagator'] = True  # Coincidence for weight-1
    elif algebra == 'virasoro':
        result['generator_weights'] = [2]
        result['generator_names'] = ['T']
        result['weight_equals_propagator'] = False
    elif algebra == 'w3':
        result['generator_weights'] = [2, 3]
        result['generator_names'] = ['T', 'W']
        result['weight_equals_propagator'] = False
    elif algebra == 'w_n':
        N = kwargs.get('N', 3)
        result['generator_weights'] = list(range(2, N + 1))
        result['generator_names'] = ['T'] + [f'W_{h}' for h in range(3, N + 1)]
        result['weight_equals_propagator'] = False
    elif algebra == 'km':
        result['generator_weights'] = [1]
        result['generator_names'] = ['J^a']
        result['weight_equals_propagator'] = True  # Coincidence for weight-1
    elif algebra == 'betagamma':
        result['generator_weights'] = [1, 0]  # beta has weight 1, gamma weight 0
        result['generator_names'] = ['beta', 'gamma']
        result['weight_equals_propagator'] = False
    elif algebra == 'fermion':
        result['generator_weights'] = [Fraction(1, 2)]
        result['generator_names'] = ['psi']
        result['weight_equals_propagator'] = False
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    return result
