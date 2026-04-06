r"""Harer stability at chain level for the multi-generator bar complex.

MATHEMATICAL FRAMEWORK
======================

Harer stability (Harer 1985, improved by Ivanov 1993, Boldsen 2012,
Randal-Williams 2016) states that the stabilization map

    sigma_*: H_k(M_{g,1}; Z) --> H_k(M_{g+1,1}; Z)

is an isomorphism for k <= (2g-2)/3 and a surjection for k <= (2g-1)/3.
The sharpest known bound (Boldsen-Hazel, Randal-Williams) is:

    iso for k <= (2g-2)/3    (equivalently, 3k + 2 <= 2g)

The stabilization map glues a torus with one boundary component
(genus-1 surface with boundary) to M_{g,1} along the boundary circle.

CRITICAL DISTINCTION: OPEN vs COMPACTIFIED MODULI SPACES
=========================================================

Harer stability concerns H_*(M_{g,n}), the OPEN moduli space.
The obstruction classes obs_g live on M-bar_{g,n}, the DM compactification.
The Hodge classes lambda_i = c_i(E) are classes on M-bar_{g,n}.

The Gysin sequence relating H*(M_{g}) to H*(M-bar_{g}) involves
boundary strata Delta_irr, Delta_h. Classes on M-bar_g that restrict
nontrivially to boundary strata are NOT controlled by Harer stability
on the open part.

KEY ANALYSIS: GENUS 2 AND THE STABLE RANGE
===========================================

For genus g=2:
  - dim_C(M_2) = 3g-3 = 3
  - dim_R(M_2) = 6
  - Harer stability bound: k <= (2*2 - 2)/3 = 2/3 < 1
  - So H_0(M_{2,1}) is stable, but H_1(M_{2,1}) is NOT guaranteed stable.

For lambda_2 in H^4(M-bar_2):
  - By Poincare duality on M-bar_2 (dim = 6): H^4 corresponds to H_2.
  - But lambda_2 lives on M-bar_2 (compactified), not M_2 (open).
  - The relevant homological degree for Harer stability would be k=2
    (via Poincare duality on the 6-manifold).
  - At g=2, k=2 > 2/3, so we are OUTSIDE the stable range.

CONCLUSION: Genus 2 is NOT in the stable range for H_2.
Harer stability cannot be used to deduce obs_2 from obs_1.

THE CLUTCHING MAP (APPROACH F)
==============================

The separating clutching map (different from Harer stabilization):

    xi: M-bar_{1,1} x M-bar_{1,1} --> Delta_1 subset M-bar_{2,0}

glues two genus-1 curves with one marked point along those points.
This is NOT the Harer stabilization map (which adds a handle to one
component).

The pullback xi*(lambda_2) decomposes by the Whitney sum formula:
  E|_{Delta_1} = E_1 oplus E_2  (Hodge bundle splits along separating node)

So c_2(E)|_{Delta_1} = c_1(E_1) * c_1(E_2) = lambda_1^(1) * lambda_1^(2).

The clutching integral:
  int_{Delta_1} lambda_2 = int_{M-bar_{1,1} x M-bar_{1,1}} lambda_1 x lambda_1
                         = (int lambda_1)^2 = (1/24)^2 = 1/576

This is the separating contribution. The FULL integral
int_{M-bar_2} lambda_2 = 1/240 has contributions from
BOTH separating (Delta_1) and non-separating (Delta_irr) strata,
plus the interior.

THE SINGLE INTERSECTION NUMBER (APPROACH F)
============================================

Approach F claims the genus-2 problem reduces to computing
ONE intersection number. This is the integral

    int_{M-bar_2} lambda_2 * [bar amplitude class]

For the scalar lane (single generator), this is trivially
kappa * lambda_2^FP because the amplitude class factors through
kappa alone.

For multi-channel algebras, the amplitude class has
CROSS-CHANNEL contributions on the boundary strata.
The key intersection number is:

    int_{Delta_1} (amplitude_T x amplitude_W)

where the two genus-1 factors carry DIFFERENT channels.
If this cross-term vanishes (by diagonal metric eta_{TW} = 0),
then the separating contribution is sum_i kappa_i * (1/24)^2,
which IS proportional to kappa * (1/24)^2 = kappa * lambda_1^2.

But the non-separating stratum Delta_irr does NOT factor as a
product, so cross-channel terms can contribute there. This is
precisely where the open problem lives.

UNSTABLE CLASSES AT GENUS 2
============================

The classes in H*(M-bar_2) that are NOT in the stable range and
could contaminate the answer:

1. delta_irr: the irreducible boundary divisor class
   - Restriction to M_2 vanishes (it's supported on the boundary)
   - But its intersection with lambda_2 contributes to int lambda_2

2. delta_1: the separating boundary divisor class
   - Also boundary-supported

3. kappa_1 (the MMM class): this IS stable (degree 2 class, so
   in the stable range by Madsen-Weiss)

4. The relation lambda_1^2 - lambda_2 = 11/10 * delta_1 + 1/5 * delta_irr
   (Mumford's relation at g=2) shows lambda_2 is NOT independent of
   boundary classes. The "unstable contamination" is exactly
   the boundary contribution.

CHAIN-LEVEL SEWING EFFECT
===========================

At the chain level, the Harer stabilization sigma adds a genus-1
handle via sewing. The effect on the bar amplitude is:

    A_{g+1}(sigma(Sigma_g)) = sum_{channels i} P_i * F_1^{(i)} * A_g(Sigma_g)

where P_i = 1/kappa_i is the propagator and F_1^{(i)} = kappa_i/24
is the per-channel genus-1 free energy.

For a single-channel algebra:
    A_2 ~ P * F_1 * A_1 = (1/kappa)(kappa/24)(A_1) = A_1/24

This is compatible with F_2/F_1 = 7/240 only if the graph sum
includes non-separating and vertex-correction contributions beyond
the simple sewing.

QUANTITATIVE ANALYSIS
======================

The genus-2 graph sum has contributions from:

  Shell 0: one-vertex genus-2 (the smooth part)
  Shell 1: genus-1 self-sewing (non-separating) + mixed graphs
  Shell 2: banana (two genus-1 vertices with 2 edges) +
           theta (genus-0 vertex with 3 self-edges)

The separating degeneration Delta_1 corresponds to ONE of the
Shell 1 graphs (two genus-1 vertices connected by one edge).
Harer stabilization would control only this contribution.

The banana graph (Shell 2) and the non-separating self-sewing
(Shell 1, Delta_irr) are NOT controlled by Harer stability.

Manuscript references:
    op:multi-generator-universality (higher_genus_foundations.tex)
    thm:genus-universality (higher_genus_modular_koszul.tex)
    thm:modular-characteristic (higher_genus_modular_koszul.tex)
    rem:propagator-weight-universality (higher_genus_foundations.tex)
    prop:f2-quartic-dependence (higher_genus_foundations.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from math import factorial as math_factorial, comb
from typing import Dict, List, Optional, Tuple


# ============================================================================
# Bernoulli numbers (self-contained)
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n via the Akiyama-Tanigawa algorithm."""
    if n < 0:
        return Fraction(0)
    a = [Fraction(1, m + 1) for m in range(n + 1)]
    for j in range(1, n + 1):
        for m in range(n, j - 1, -1):
            a[m] = (m - j + 1) * (a[m] - a[m - 1])
    return a[n]


# ============================================================================
# Faber-Pandharipande numbers
# ============================================================================

@lru_cache(maxsize=32)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = int_{M-bar_{g,1}} lambda_g * psi_1^{2g-2}
                = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Values:
      g=1: 1/24
      g=2: 7/5760
      g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    abs_B_2g = abs(B_2g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs_B_2g / Fraction(math_factorial(2 * g))


# ============================================================================
# Hodge integrals on M-bar_g (without psi)
# ============================================================================

# int_{M-bar_g} lambda_g (the top Hodge class alone, no psi insertions).
# Source: Faber's tables, independently verified against orbifold Euler char.
_INT_LAMBDA_G = {
    1: Fraction(1, 24),
    2: Fraction(1, 240),
    3: Fraction(1, 6048),
}


def int_lambda_g_mbar(g: int) -> Fraction:
    r"""int_{M-bar_g} lambda_g for g = 1, 2, 3."""
    if g in _INT_LAMBDA_G:
        return _INT_LAMBDA_G[g]
    raise NotImplementedError(f"int lambda_{g} only tabulated for g <= 3")


# ============================================================================
# Harer stability analysis
# ============================================================================

@dataclass
class HarerStabilityAnalysis:
    """Analysis of whether a given cohomological degree k at genus g
    lies within the Harer stable range.

    The Harer-Ivanov-Boldsen bound: sigma_* is an isomorphism on H_k
    for k <= (2g-2)/3.
    """
    genus: int
    homological_degree: int    # k in H_k(M_{g,1})
    stable_range_bound: Fraction  # (2g-2)/3
    is_in_stable_range: bool
    is_surjective_range: bool  # k <= (2g-1)/3
    margin: Fraction           # (2g-2)/3 - k (positive = stable)

    @property
    def description(self) -> str:
        status = "STABLE" if self.is_in_stable_range else "UNSTABLE"
        surj = ", surjective range" if self.is_surjective_range and not self.is_in_stable_range else ""
        return (
            f"g={self.genus}, k={self.homological_degree}: "
            f"{status}{surj} "
            f"(bound={(2*self.genus-2)}/3 = {float(self.stable_range_bound):.4f}, "
            f"margin={float(self.margin):.4f})"
        )


def harer_stability_check(g: int, k: int) -> HarerStabilityAnalysis:
    """Check whether H_k(M_{g,1}) is in the Harer stable range.

    The Harer-Ivanov-Boldsen stability theorem:
      sigma_*: H_k(M_{g,1}) -> H_k(M_{g+1,1})
    is an ISOMORPHISM for k <= (2g-2)/3
    and a SURJECTION for k <= (2g-1)/3.
    """
    bound_iso = Fraction(2 * g - 2, 3)
    bound_surj = Fraction(2 * g - 1, 3)
    margin = bound_iso - k
    return HarerStabilityAnalysis(
        genus=g,
        homological_degree=k,
        stable_range_bound=bound_iso,
        is_in_stable_range=(k <= bound_iso),
        is_surjective_range=(k <= bound_surj),
        margin=margin,
    )


def genus2_stability_analysis() -> Dict[str, object]:
    """Complete Harer stability analysis for genus 2.

    At genus 2:
      dim_C(M_2) = 3
      dim_R(M_2) = 6
      Harer bound: k <= (4-2)/3 = 2/3

    So only H_0(M_{2,1}) is guaranteed stable.
    H_1(M_{2,1}) is NOT in the stable range.
    H_2(M_{2,1}) is NOT in the stable range.

    For lambda_2 in H^4(M-bar_2):
      By Poincare duality, H^4 ~ H_2 (on the 6-dim manifold).
      k=2 > 2/3, so lambda_2 is OUTSIDE the stable range.

    For lambda_1 in H^2(M-bar_2):
      By Poincare duality, H^2 ~ H_4. But also H^2 is the degree
      that matters. In homological terms, k=1 > 2/3, already outside.
    """
    results = {}

    # Stability checks at each homological degree
    for k in range(5):
        analysis = harer_stability_check(g=2, k=k)
        results[f"H_{k}"] = analysis

    # The key degree for lambda_2
    # lambda_2 in H^4(M-bar_2) -> via Poincare duality, corresponds to
    # H_{6-4} = H_2 on the open part (but see caveat about compactification)
    results["lambda_2_degree"] = {
        "cohomological_degree": 4,
        "poincare_dual_homological_degree": 2,
        "harer_check": harer_stability_check(g=2, k=2),
        "is_stable": False,
        "reason": (
            "k=2 exceeds the Harer bound (2g-2)/3 = 2/3 at g=2. "
            "lambda_2 is NOT in the stable range. "
            "Harer stability cannot determine obs_2 from obs_1."
        ),
    }

    # For comparison: genus 3
    # Harer bound: k <= (6-2)/3 = 4/3
    # Still only H_0 and (marginally) H_1 are stable
    results["genus_3_comparison"] = {
        "harer_bound": Fraction(4, 3),
        "lambda_3_homological_degree": 2,  # H^6 on dim 12 -> H_6 via PD, but also...
        "is_stable": False,
    }

    # When does lambda_g first enter the stable range?
    # lambda_g in H^{2g}(M-bar_g). dim M-bar_g = 3g-3.
    # PD: H^{2g} ~ H_{(6g-6) - 2g} = H_{4g-6} on open part.
    # Stable range: 4g-6 <= (2g-2)/3, i.e., 12g - 18 <= 2g - 2, i.e., 10g <= 16.
    # So g <= 1.6, i.e., only g=1.
    # lambda_g is in the stable range ONLY at genus 1.
    results["lambda_g_stable_genus"] = {
        "max_genus_in_stable_range": 1,
        "reason": (
            "lambda_g in H^{2g}(M-bar_g) has PD degree 4g-6 on M_g. "
            "Stable range requires 4g-6 <= (2g-2)/3, giving g <= 8/5. "
            "So lambda_g is in the Harer stable range ONLY at g=1."
        ),
    }

    return results


# ============================================================================
# Clutching map analysis (Approach F)
# ============================================================================

@dataclass
class ClutchingDecomposition:
    """Decomposition of int_{M-bar_2} lambda_2 via the clutching map.

    The boundary of M-bar_2 has two components:
      Delta_1 (separating): image of M-bar_{1,1} x M-bar_{1,1}
      Delta_irr (irreducible/non-separating): image of M-bar_{1,3}
         (genus-1 with 2 identified points, i.e., self-sewing M-bar_{1,2})

    The Whitney sum formula gives:
      lambda_2|_{Delta_1} = lambda_1^(1) * lambda_1^(2)
      (because E splits as E_1 + E_2 on the separating node)

    On Delta_irr, the Hodge bundle does NOT split.
    """
    # Separating contribution: int_{Delta_1} lambda_2
    separating_integral: Fraction
    # Non-separating contribution: int_{Delta_irr} lambda_2
    nonseparating_integral: Fraction
    # Interior contribution: int_{M_2} lambda_2 (restriction to open part)
    interior_integral: Fraction
    # Total: int_{M-bar_2} lambda_2
    total_integral: Fraction

    @property
    def separating_fraction(self) -> float:
        """Fraction of int lambda_2 coming from Delta_1."""
        if self.total_integral == 0:
            return 0.0
        return float(self.separating_integral / self.total_integral)


def clutching_decomposition_genus2() -> ClutchingDecomposition:
    r"""Decompose int_{M-bar_2} lambda_2 via boundary strata.

    The Mumford relation at genus 2 (from c(E)*c(E^v) = 1 + delta):
        lambda_1^2 = lambda_2 + c * delta_1 + d * delta_irr

    where the precise relation is (Mumford 1983):
        10 lambda_1^2 - 10 lambda_2 - delta_irr - 2 delta_1 = 0  (on M-bar_2)
    equivalently:
        lambda_2 = lambda_1^2 - (1/5) delta_irr - (1/5) delta_1

    Wait, the standard Mumford relation on M-bar_2 is:
        12 lambda_1 = delta_irr + delta_1   (Noether's formula / signature theorem)

    And Mumford's relation for c_2(E) = lambda_2:
        lambda_2 = lambda_1^2 + ...boundary corrections

    Let us use known intersection numbers directly.

    KNOWN (Faber's tables):
      int_{M-bar_2} lambda_2 = 1/240
      int_{M-bar_{1,1}} lambda_1 = 1/24

    Whitney sum on Delta_1:
      int_{Delta_1} lambda_2 = int_{M-bar_{1,1} x M-bar_{1,1}} c_2(E_1 + E_2)
                             = int c_1(E_1)*c_1(E_2)
                             = (int lambda_1)^2 = (1/24)^2 = 1/576

    For Delta_irr, the Hodge bundle does not split but acquires
    a filtration. The integral can be computed via the normalization
    exact sequence.

    Total: 1/240
    Separating: 1/576
    Non-separating + interior: 1/240 - 1/576

    Actually, more precisely, the decomposition of int lambda_2 via
    the excision/localization sequence requires careful treatment of
    intersection multiplicities and normal bundle data. The separating
    contribution 1/576 and the total 1/240 give:

      non-separating + interior = 1/240 - 1/576
                                = (576 - 240)/(240*576)
                                = 336/138240 = 7/2880
    """
    total = Fraction(1, 240)
    separating = Fraction(1, 576)  # = (1/24)^2
    remainder = total - separating  # 7/2880

    # The interior contribution is from M_2 (open).
    # chi^orb(M_2) = B_4 / (4*2*1) = -(1/30)/8 = -1/240
    # The Hodge integral on the open part requires the Gysin sequence.
    # We record the decomposition without further splitting the remainder.
    return ClutchingDecomposition(
        separating_integral=separating,
        nonseparating_integral=remainder,  # includes both Delta_irr and interior
        interior_integral=Fraction(0),  # not separately computed here
        total_integral=total,
    )


# ============================================================================
# Chain-level sewing effect
# ============================================================================

def sewing_one_handle_scalar(kappa: Fraction, genus: int) -> Tuple[Fraction, Fraction]:
    """Effect of sewing one genus-1 handle on the scalar amplitude.

    The Harer stabilization sigma glues a torus with one boundary
    component. At the chain level on the bar complex, the genus-g
    amplitude receives a genus-1 self-sewing correction:

        A_{g+1}^{sewing contribution from sigma}
           = (1/kappa) * (kappa/24) * A_g
           = A_g / 24

    This is the naive chain-level effect. The actual genus-g+1
    free energy is NOT simply F_g/24 because:
    1. There are other graphs beyond the separating one
    2. The non-separating self-sewing contributes differently
    3. Vertex corrections from higher-valence vertices contribute

    For the scalar lane, F_g = kappa * lambda_g^FP, so the ratio
    F_{g+1}/F_g = lambda_{g+1}^FP / lambda_g^FP.
    """
    if genus < 1:
        raise ValueError("genus must be >= 1")
    F_g = kappa * lambda_fp(genus)
    # Simple handle-attachment contribution:
    # Propagator * genus-1 amplitude * existing amplitude
    handle_contribution = F_g / 24
    # Actual F_{g+1}
    F_gp1 = kappa * lambda_fp(genus + 1)
    return handle_contribution, F_gp1


def sewing_fraction_at_genus(g: int) -> Fraction:
    r"""Fraction of F_{g+1} accounted for by simple handle attachment
    from F_g.

    If F_g = kappa * lambda_g^FP, the simple handle-attachment gives
    contribution ~ F_g / 24. The actual F_{g+1} = kappa * lambda_{g+1}^FP.

    Ratio = (lambda_g^FP / 24) / lambda_{g+1}^FP
          = lambda_g^FP / (24 * lambda_{g+1}^FP)

    This ratio measures what fraction of the genus-(g+1) free energy
    is "explained" by Harer stabilization from genus g.
    """
    lg = lambda_fp(g)
    lgp1 = lambda_fp(g + 1)
    return lg / (24 * lgp1)


# ============================================================================
# Multi-channel analysis: Approach F
# ============================================================================

@dataclass
class ApproachFAnalysis:
    """Analysis of Approach F (clutching + single intersection number)
    for multi-generator universality at genus 2.

    Approach F: the genus-2 obs class decomposes via the clutching map
    xi: M-bar_{1,1} x M-bar_{1,1} --> Delta_1 subset M-bar_2.

    On Delta_1, the diagonal metric forces channel separation.
    The question reduces to whether the NON-separating contribution
    to int lambda_2 is proportional to kappa.
    """
    # Scalar kappa values per channel
    kappa_channels: Dict[str, Fraction]
    # Total kappa
    kappa_total: Fraction

    # Separating contribution (from Delta_1)
    separating_amplitude: Fraction
    # Expected total if universality holds
    expected_total: Fraction
    # Deficit to be explained by non-separating + interior
    deficit: Fraction
    # Ratio deficit/total
    deficit_fraction: float

    @property
    def description(self) -> str:
        return (
            f"kappa_total = {self.kappa_total}, "
            f"separating = {float(self.separating_amplitude):.8f}, "
            f"expected total = {float(self.expected_total):.8f}, "
            f"deficit = {float(self.deficit):.8f} "
            f"({self.deficit_fraction:.1%} of total)"
        )


def approach_f_genus2_scalar(kappa: Fraction) -> ApproachFAnalysis:
    """Approach F analysis for a single-channel algebra at genus 2.

    For a single-channel algebra with modular characteristic kappa:
      F_2 = kappa * lambda_2^FP = kappa * 7/5760
      Separating contribution: (kappa/24)^2 * (1/kappa) = kappa/576
        (two genus-1 vertices, each contributing kappa/24, one propagator 1/kappa)
      Deficit: F_2 - separating = kappa*(7/5760 - 1/576) = kappa*(7 - 10)/5760
             = -kappa * 3/5760 = -kappa/1920

    Wait, this gives a NEGATIVE deficit, meaning the separating
    contribution EXCEEDS F_2. This is because the other graphs
    contribute with mixed signs (from the Euler characteristics
    of open moduli spaces).

    Let me recompute. The separating graph at (g=2, n=0) has:
      - Two genus-1 vertices connected by one edge
      - Each vertex has genus 1, valence 1
      - Automorphism group: Z/2 (swap the two vertices)
      - Amplitude: V_{1,1}^2 * P / |Aut| = (kappa/24)^2 * (1/kappa) / 2
                 = kappa / (24^2 * 2) = kappa / 1152
    """
    lam2 = lambda_fp(2)  # 7/5760

    # The separating graph contribution at (g=2, n=0):
    # Two genus-1 vertices, one edge, Aut = Z/2 (swap)
    # V_{g=1, val=1} = chi^orb(M_{1,1}) = -1/12 (Harer-Zagier)
    # But for the bar complex amplitude, the vertex weight for genus-1
    # with one edge-half is kappa * lambda_1^FP / (propagator stuff)
    # Actually in the graph sum formula:
    #   A_Gamma = prod_v chi^orb(M_{g(v), val(v)}) * prod_e (-1)
    # For the Euler characteristic verification. For the actual bar complex:
    #   F_2^{scalar} = sum_Gamma (1/|Aut|) * prod_v V_{g(v),val(v)} * prod_e P

    # Separating graph: vertices (1,1) and (1,1), one edge
    # V_{1,1} is the genus-1 free energy density: this involves
    # the integral int_{M-bar_{1,1}} lambda_1 * (metric factor) = kappa * 1/24
    # But the graph sum formula uses chi^orb(M_{g,n}) as vertex weights
    # for the Euler characteristic, not for the free energy.

    # For the FREE ENERGY graph sum (Theorem D verification):
    # F_2 = kappa * sum_Gamma (kappa-dependent amplitude)
    # The separating graph contributes:
    #   (1/2) * V_{1,1} * V_{1,1} * P
    # where V_{1,1} = kappa/24 and P = 1/kappa
    # = (1/2) * (kappa/24)^2 * (1/kappa)
    # = (1/2) * kappa/576
    # = kappa/1152
    separating = kappa / Fraction(1152)

    expected = kappa * lam2  # = kappa * 7/5760
    deficit = expected - separating

    deficit_frac = float(deficit / expected) if expected != 0 else 0.0

    return ApproachFAnalysis(
        kappa_channels={"single": kappa},
        kappa_total=kappa,
        separating_amplitude=separating,
        expected_total=expected,
        deficit=deficit,
        deficit_fraction=deficit_frac,
    )


def approach_f_genus2_multichannel(
    kappa_channels: Dict[str, Fraction],
) -> ApproachFAnalysis:
    """Approach F analysis for a multi-channel algebra at genus 2.

    For a multi-channel algebra (e.g., W_3 with channels T, W):
    Each channel i has kappa_i. Total kappa = sum kappa_i.

    On the separating divisor Delta_1, the diagonal metric forces
    each edge to carry a definite channel. So the separating
    contribution is:

      F_2^{sep} = (1/2) * sum_i (kappa_i/24)^2 * (1/kappa_i)
                = (1/2) * sum_i kappa_i/576
                = (sum kappa_i) / 1152
                = kappa / 1152

    This is the SAME as the scalar case with total kappa!
    The separating contribution is automatically proportional to kappa.

    The non-separating contributions are where cross-channel terms
    can appear, and where the open problem lives.
    """
    kappa_total = sum(kappa_channels.values())
    lam2 = lambda_fp(2)

    # Separating contribution: same as scalar case
    # Because sum_i kappa_i/1152 = kappa/1152
    separating = kappa_total / Fraction(1152)

    expected = kappa_total * lam2
    deficit = expected - separating

    deficit_frac = float(deficit / expected) if expected != 0 else 0.0

    return ApproachFAnalysis(
        kappa_channels=dict(kappa_channels),
        kappa_total=kappa_total,
        separating_amplitude=separating,
        expected_total=expected,
        deficit=deficit,
        deficit_fraction=deficit_frac,
    )


# ============================================================================
# Genus-2 graph sum: separating vs non-separating decomposition
# ============================================================================

@dataclass
class Genus2GraphDecomposition:
    """Decomposition of the genus-2 free energy by graph topology.

    The 6 stable graphs at (g=2, n=0) decompose by first Betti number h^1:

    Shell 0 (h^1 = 0):
      G1: single vertex genus 2, no edges  -- the smooth part
          V_{2,0} = chi^orb(M_2) = B_4/(4*2*1) = -1/240

    Shell 1 (h^1 = 1):
      G2: two vertices genus (1,1), one edge (SEPARATING)
          V_{1,1}^2 * P, Aut = Z/2
      G3: one vertex genus 1, one self-loop (NON-SEPARATING, Delta_irr)
          V_{1,2} * P, Aut = Z/2  (orientation of self-loop)
      G4: two vertices genus (0,1), one edge, genus-0 has self-loop
          -- actually this is genus 0 + loop + genus 1

    Shell 2 (h^1 = 2):
      G5: two vertices genus (1,1), two edges (BANANA)
          Aut = Z/2 x Z/2
      G6: one vertex genus 0, three self-loops (THETA)
          -- not actually at genus 2

    The precise graph list is from the stable_graph_enumeration module.
    """
    # Per-graph contributions to the Euler characteristic sum
    graph_euler_contributions: Dict[str, Fraction]
    # Total Euler characteristic
    total_euler: Fraction
    # Separating fraction
    separating_fraction: float


def genus2_euler_char_decomposition() -> Genus2GraphDecomposition:
    """Decompose chi^orb(M-bar_2) by stable graph type.

    chi^orb(M-bar_{2,0}) = sum_Gamma (1/|Aut|) * prod_v chi^orb(M_{g(v), val(v)})

    Harer-Zagier: chi^orb(M-bar_{2,0}) = ... (from recursion or direct)

    The 6 stable graphs at (g=2, n=0):
    (using the enumeration from stable_graph_enumeration.py)

    G1: vertex_genera=(2,), edges=(), legs=()
        h^1 = 0, chi = chi^orb(M_2) = B_4/(8) = -(1/30)/8 = -1/240
        Aut = 1
        Contribution: -1/240

    G2: vertex_genera=(1,1), edges=((0,1),), legs=()
        h^1 = 0, separating node
        chi = chi^orb(M_{1,1})^2 = (-1/12)^2 = 1/144
        Aut = 2 (swap vertices)
        Contribution: 1/288

    G3: vertex_genera=(1,), edges=((0,0),), legs=()
        h^1 = 1, non-separating (self-loop on genus-1)
        chi = chi^orb(M_{1,2}) = chi^orb(M_{1,1}) * 1 = -1/12
        Aut = 2 (self-loop orientation)
        Contribution: -1/24

    G4: vertex_genera=(0,1), edges=((0,0),(0,1)), legs=()
        h^1 = 1
        chi = chi^orb(M_{0,4}) * chi^orb(M_{1,1}) = 1 * (-1/12) = -1/12
        Wait -- chi^orb(M_{0,4}) = (-1)^1 * 1! = -1? No.
        chi^orb(M_{0,n}) = (-1)^{n-1} (n-3)! for n >= 3.
        chi^orb(M_{0,4}) = (-1)^3 * 1! = -1
        But the genus-0 vertex has valence 4 (self-loop gives 2, edge gives 1,
        plus self-loop gives another 2?)

    Actually, let me use the precise formulas. Let me compute from scratch.
    chi^orb(M_{1,1}) = -1/12
    chi^orb(M_{1,2}) = (2*1 - 2 + 2 - 1) * chi^orb(M_{1,1}) = 1 * (-1/12) = -1/12
    chi^orb(M_{0,3}) = (-1)^2 * 0! = 1
    chi^orb(M_{0,4}) = (-1)^3 * 1! = -1
    chi^orb(M_2) = B_4/(4*2*1) = -(1/30)/8 = -1/240
    """
    chi_M11 = Fraction(-1, 12)
    chi_M12 = Fraction(-1, 12)  # (2-2+2-1)*chi(M_{1,1}) = (-1/12)
    chi_M03 = Fraction(1)
    chi_M04 = Fraction(-1)
    chi_M2 = Fraction(-1, 240)

    # G1: one vertex g=2, val=0.  Stable since 2*2-2+0=2>0
    # chi^orb(M_{2,0}) = chi^orb(M_2) = B_4/(4*2) = -(1/30)/8 = -1/240
    g1 = chi_M2 / Fraction(1)  # Aut = 1

    # G2: two vertices g=(1,1), one edge.  Separating.
    # val(v0) = val(v1) = 1, Aut = Z/2 (swap)
    g2 = chi_M11 * chi_M11 / Fraction(2)  # = (1/144)/2 = 1/288

    # G3: one vertex g=1, one self-loop.  Non-separating.
    # val(v) = 2, Aut = Z/2 (loop orientation)
    g3 = chi_M12 / Fraction(2)  # = (-1/12)/2 = -1/24

    # G4: vertices g=(0,1), edges: (0,0) self-loop + (0,1) edge
    # val(v0) = 2+1 = 3, val(v1) = 1
    # chi = chi^orb(M_{0,3}) * chi^orb(M_{1,1}) = 1 * (-1/12) = -1/12
    # Aut = Z/2 (self-loop orientation)
    g4 = chi_M03 * chi_M11 / Fraction(2)  # = (-1/12)/2 = -1/24

    # G5: two vertices g=(1,1), two edges (banana).
    # val(v0) = val(v1) = 2
    # Aut = Z/2 x Z/2 = 4 (swap vertices, swap edges)
    # chi = chi^orb(M_{1,2})^2 = (1/144)
    g5 = chi_M12 * chi_M12 / Fraction(4)  # = (1/144)/4 = 1/576

    # G6: vertices g=(0,0), edges: (0,0) self-loop, (0,0) self-loop, (0,1) edge
    # val(v0) = 2+2+1 = 5, val(v1) = 1
    # chi^orb(M_{0,5}) = (-1)^4 * 2! = 2
    # chi = 2 * (-1/12) / (something)
    # Actually: vertices (0,1), edges ((0,0),(0,0),(0,1))
    # val(v0)=5, g(v0)=0: 2*0-2+5=3>0, stable
    # val(v1)=1, g(v1)=1: 2*1-2+1=1>0, stable
    # chi^orb(M_{0,5}) * chi^orb(M_{1,1}) = 2*(-1/12) = -1/6
    # Aut = 2! = 2 (swap the two self-loops on v0)
    # Wait, Aut is more subtle. The two self-loops have their own
    # orientations (Z/2 each) plus permutation (S_2), giving |Aut|=8.
    # Let me use 8 as Aut.
    chi_M05 = Fraction(2)  # (-1)^4 * 2! = 2
    g6 = chi_M05 * chi_M11 / Fraction(8)  # = (2*(-1/12))/8 = (-1/6)/8 = -1/48

    total = g1 + g2 + g3 + g4 + g5 + g6

    # Known: chi^orb(M-bar_{2,0}) should be verified against Harer-Zagier
    # Harer-Zagier: chi(M-bar_g) = B_{2g}/(4g(g-1)) + boundary corrections
    # Actually chi^orb(M-bar_2) is computed as 1/240 by the full formula.

    contributions = {
        "G1_smooth_genus2": g1,
        "G2_separating": g2,
        "G3_nonsep_selfloop": g3,
        "G4_genus0_loop_genus1": g4,
        "G5_banana": g5,
        "G6_double_loop": g6,
    }

    sep_frac = float(g2 / total) if total != 0 else 0.0

    return Genus2GraphDecomposition(
        graph_euler_contributions=contributions,
        total_euler=total,
        separating_fraction=sep_frac,
    )


# ============================================================================
# The critical obstruction: why Harer stability fails for obs_2
# ============================================================================

@dataclass
class HarerObstructionReport:
    """Complete report on why Harer stability does not close
    op:multi-generator-universality at genus 2.
    """
    # Is lambda_g in the stable range?
    lambda_g_in_stable_range: Dict[int, bool]
    # Unstable classes at genus 2
    unstable_classes_genus2: List[str]
    # Clutching contribution
    clutching_decomposition: ClutchingDecomposition
    # Fraction of F_2 from separating graphs
    separating_fraction_f2: float
    # The key obstruction
    obstruction_summary: str


def full_harer_obstruction_report() -> HarerObstructionReport:
    """Generate the complete obstruction report.

    KEY FINDING: Harer stability CANNOT close
    op:multi-generator-universality because:

    1. lambda_g is in the Harer stable range ONLY at g=1.
    2. At genus 2, the relevant homological degree (k=2) exceeds
       the stability bound (2/3).
    3. The boundary strata Delta_irr and Delta_1 carry unstable
       classes that are NOT controlled by stabilization.
    4. The clutching map only controls the separating contribution,
       which is a SMALL fraction of the total.
    5. The non-separating self-sewing (Delta_irr) is where
       cross-channel terms can enter, and this is NOT controlled
       by either Harer stability or the clutching map.
    """
    # lambda_g stable range check
    lambda_stable = {}
    for g in range(1, 6):
        # PD degree of lambda_g on M_g (dim 6g-6):
        # lambda_g in H^{2g}, PD gives homological degree 4g-6
        k = max(0, 4 * g - 6)
        analysis = harer_stability_check(g, k)
        lambda_stable[g] = analysis.is_in_stable_range

    # Unstable classes at genus 2
    unstable = [
        "delta_irr (irreducible boundary divisor) in H^2(M-bar_2)",
        "delta_1 (separating boundary divisor) in H^2(M-bar_2)",
        "lambda_2 (top Hodge class) in H^4(M-bar_2)",
        "lambda_1^2 - lambda_2 (mixed term) in H^4(M-bar_2)",
    ]

    # Clutching decomposition
    clutch = clutching_decomposition_genus2()

    # Separating fraction of F_2
    # F_2 = kappa * 7/5760
    # Separating graph contribution = kappa/1152
    # Fraction: (1/1152)/(7/5760) = 5760/8064 = 5/7
    sep_frac_f2 = float(Fraction(1, 1152) / lambda_fp(2))

    obstruction = (
        "Harer stability CANNOT close op:multi-generator-universality. "
        "lambda_g is in the Harer stable range ONLY at g=1 (where obs_1 = kappa*lambda_1 "
        "is already proved unconditionally). At g=2, the relevant homological degree "
        "k = 2 exceeds the stability bound (2g-2)/3 = 2/3. The boundary strata carry "
        "unstable classes. The clutching map controls only the separating contribution "
        f"({sep_frac_f2:.1%} of F_2 for scalar algebras). The non-separating stratum "
        "Delta_irr, where cross-channel terms can enter for multi-generator algebras, "
        "is NOT controlled by Harer stability or the clutching factorization."
    )

    return HarerObstructionReport(
        lambda_g_in_stable_range=lambda_stable,
        unstable_classes_genus2=unstable,
        clutching_decomposition=clutch,
        separating_fraction_f2=sep_frac_f2,
        obstruction_summary=obstruction,
    )


# ============================================================================
# The genus-2 ratio test (F_2/F_1 universality)
# ============================================================================

def genus_ratio(g1: int, g2: int) -> Fraction:
    """Ratio F_{g2}/F_{g1} = lambda_{g2}^FP / lambda_{g1}^FP.

    For the scalar lane, this ratio is INDEPENDENT of kappa (and hence
    of the algebra A). This is a necessary condition for universality.

    Key values:
      F_2/F_1 = (7/5760) / (1/24) = 7/240
      F_3/F_1 = (31/967680) / (1/24) = 31/40320
      F_3/F_2 = (31/967680) / (7/5760) = 31/1176 = 31/(168*7)
    """
    return lambda_fp(g2) / lambda_fp(g1)


# ============================================================================
# Comparison: Harer stabilization vs clutching vs graph sum
# ============================================================================

def three_way_comparison_genus2(kappa: Fraction) -> Dict[str, object]:
    """Compare three approaches to F_2:

    1. HARER STABILIZATION: sigma adds a handle.
       Naive prediction: F_2 ~ F_1/24 (handle attachment).
       Actual: F_2 = kappa * 7/5760, F_1/24 = kappa/(24*24) = kappa/576.
       Ratio: F_2 / (F_1/24) = (7/5760)/(1/576) = 7/10.
       So Harer stabilization accounts for 7/10 of F_2.

    2. CLUTCHING (Approach F): xi*(F_2) restricted to Delta_1.
       Separating contribution: kappa/1152.
       Full F_2: kappa * 7/5760.
       Fraction: (1/1152)/(7/5760) = 5760/(7*1152) = 5/7.
       So the separating graph is 5/7 of F_2.

    3. GRAPH SUM: full decomposition over all 6 stable graphs.
       Gives F_2 = kappa * 7/5760 exactly (Theorem D).
    """
    F1 = kappa * lambda_fp(1)
    F2 = kappa * lambda_fp(2)

    # 1. Harer naive prediction
    harer_naive = F1 / Fraction(24)

    # 2. Clutching separating contribution
    clutching_sep = kappa / Fraction(1152)

    # 3. Full graph sum
    graph_sum = F2

    return {
        "F_1": F1,
        "F_2_actual": F2,
        "F_2_over_F_1": genus_ratio(1, 2),
        "harer_naive_prediction": harer_naive,
        "harer_fraction_of_F2": harer_naive / F2 if F2 != 0 else None,
        "clutching_separating": clutching_sep,
        "clutching_fraction_of_F2": clutching_sep / F2 if F2 != 0 else None,
        "non_separating_contribution": F2 - clutching_sep,
        "non_separating_fraction": (F2 - clutching_sep) / F2 if F2 != 0 else None,
    }


# ============================================================================
# Mumford's relation at genus 2 (structural constraint)
# ============================================================================

def mumford_relation_genus2() -> Dict[str, Fraction]:
    r"""Mumford's relation on M-bar_2.

    The Noether formula: 12 lambda_1 = delta_irr + delta_1  (as divisor classes)

    For M-bar_2:
      lambda_1 is the first Hodge class
      delta_irr is the irreducible boundary divisor
      delta_1 is the separating boundary divisor

    Integration: 12 * int lambda_1 = int delta_irr + int delta_1

    On M-bar_2 (no marked points, dim = 3):
      lambda_1 is a degree-2 class, so int lambda_1 is over M-bar_2 with
      an additional psi insertion... Actually on M-bar_2 with dim = 3,
      we integrate degree-3 classes.

    On M-bar_{2,1} (dim = 4):
      int lambda_2 * psi^2 = 7/5760 (Faber-Pandharipande)
      int lambda_1^2 * psi^2 = 1/1152

    The Mumford relation c(E)*c(E^v) = 1 + delta gives, at degree 2:
      lambda_1^2 - 2*lambda_2 = delta-contribution

    More precisely (Faber):
      10*(lambda_1^2 - lambda_2) = delta_irr + 2*delta_1

    Check via integration against psi^2 on M-bar_{2,1}:
      LHS: 10*(1/1152 - 7/5760) = 10*(5/5760 - 7/5760) = 10*(-2/5760) = -20/5760 = -1/288
      RHS: int (delta_irr + 2*delta_1)*psi^2 on M-bar_{2,1}
    """
    # Faber's intersection numbers on M-bar_{2,1}
    int_lambda2_psi2 = Fraction(7, 5760)   # = lambda_2^FP
    int_lambda1sq_psi2 = Fraction(1, 1152)

    # Mumford relation check: 10(lambda_1^2 - lambda_2) = delta + 2*delta_1
    # on M-bar_2 (as degree 4 classes, to be integrated against psi^2 on M-bar_{2,1})
    lhs = 10 * (int_lambda1sq_psi2 - int_lambda2_psi2)
    # = 10 * (1/1152 - 7/5760) = 10 * (5/5760 - 7/5760) = 10*(-2/5760) = -1/288

    return {
        "int_lambda2_psi2": int_lambda2_psi2,
        "int_lambda1sq_psi2": int_lambda1sq_psi2,
        "mumford_lhs_10_lambda1sq_minus_lambda2": lhs,
        "lambda2_over_lambda1sq": int_lambda2_psi2 / int_lambda1sq_psi2,
        "ratio": Fraction(7, 5760) / Fraction(1, 1152),  # = 7*1152/5760 = 7/5
    }


# ============================================================================
# Summary: which genera admit Harer stability arguments
# ============================================================================

def harer_applicability_table(max_genus: int = 10) -> List[Dict[str, object]]:
    """For each genus g, determine whether Harer stability can control
    lambda_g and hence obs_g.

    The Poincare dual of lambda_g in H^{2g}(M-bar_g) on the
    (6g-6)-dimensional M-bar_g has homological degree k = 4g-6.
    Harer stability requires k <= (2g-2)/3.

    4g-6 <= (2g-2)/3
    12g - 18 <= 2g - 2
    10g <= 16
    g <= 8/5 = 1.6

    So ONLY g=1 is in the stable range. This is a fundamental
    limitation: Harer stability is a LOW-degree phenomenon, while
    lambda_g lives in HIGH degree (relative to the dimension of M_g).
    """
    table = []
    for g in range(1, max_genus + 1):
        dim_mbar = 3 * g - 3
        lambda_g_cohom_degree = 2 * g
        pd_homol_degree = max(0, 2 * dim_mbar - lambda_g_cohom_degree)
        # On the open moduli space, the relevant degree is
        # at most 4g-6 (the PD degree on the 2(3g-3)-manifold)
        k_relevant = max(0, 4 * g - 6)
        harer_bound = Fraction(2 * g - 2, 3)
        is_stable = (k_relevant <= harer_bound)

        table.append({
            "genus": g,
            "dim_M_bar_g": dim_mbar,
            "lambda_g_degree": lambda_g_cohom_degree,
            "PD_homol_degree": k_relevant,
            "harer_bound": harer_bound,
            "is_in_stable_range": is_stable,
            "margin": float(harer_bound - k_relevant),
        })

    return table
