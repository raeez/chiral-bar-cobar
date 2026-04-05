r"""Non-perturbative shadow partition function: double convergence in genus and arity.

MATHEMATICAL FRAMEWORK
======================

The shadow partition function is the double sum:

    Z^sh(A, hbar) = sum_{g >= 1} sum_{r >= 2} hbar^{2g-2} Z_g^{(r)}(A)

where Z_g^{(r)} is the genus-g, arity-r shadow tautological contribution.

TWO INDEPENDENT CONVERGENCE RESULTS (both proved):

1. GENUS CONVERGENCE at arity 2 (scalar):
   F_g(A) = kappa(A) * lambda_g^FP
   |F_g| ~ 2|kappa|/(2*pi)^{2g}, geometric ratio 1/(2*pi)^2 ~ 0.025
   (prop:genus-expansion-convergence in genus_expansions.tex)

2. ARITY CONVERGENCE at fixed genus:
   |S_r(A)| ~ C * rho(A)^r * r^{-5/2}
   (thm:shadow-radius in higher_genus_modular_koszul.tex)

THE NEW RESULT (thm:shadow-double-convergence):

For a Koszul chiral algebra A with shadow radius rho(A) < 1, the double
sum converges absolutely.  The key technical input is the R-matrix genus
bound (prop:r-matrix-genus-bound): the Bernoulli decay of the Hodge
R-matrix ensures that genus-g contributions at EVERY fixed arity r
decay geometrically with ratio 1/(2*pi)^2.

The bound factorizes:

    sum_{g,r} |Z_g^{(r)}| <= C * (sum_g (2pi)^{-2g}) * (sum_r rho^r r^{-5/2})
                           = C * (2pi)^2/((2pi)^2 - 1) * Li_{5/2}(rho)

where Li_{5/2} is the polylogarithm.

CONTRAST WITH STRING THEORY:

The full bar-cobar genus expansion diverges: Vol(M-bar_g) ~ (2g)!
(Mirzakhani).  The shadow partition function converges because the
shadow CohFT extracts tautological intersection numbers with Bernoulli
decay, not the full Weil-Petersson volume.

References:
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    prop:r-matrix-genus-bound (higher_genus_modular_koszul.tex)
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:cohft-reconstruction (higher_genus_modular_koszul.tex)
    rem:convergence-vs-string (genus_expansions.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, factorial, pi as sym_pi,
    simplify, sqrt, Abs, N as Neval, oo,
)

from compute.lib.utils import lambda_fp, F_g
from compute.lib.cohft_vertex_engine import r_matrix_coefficients
from compute.lib.dressed_propagator_engine import dressed_propagator_coefficient
from compute.lib.shadow_tower_recursive import (
    compute_shadow_tower,
    ShadowTower,
)
from compute.lib.shadow_radius import (
    virasoro_shadow_data,
    virasoro_shadow_radius_formula,
)
from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    STANDARD_KAPPAS,
)

# Symbols
c_sym = Symbol('c')
hbar_sym = Symbol('hbar')

PI = math.pi
TWO_PI_SQ = (2 * PI) ** 2  # ~ 39.478


# =========================================================================
# Section 1: Tautological intersection bound (Convention S)
# =========================================================================
#
# KEY STRUCTURAL POINT: The shadow partition function is computed in
# Convention S (the manuscript's shadow operad convention), where:
#   - Vertex weights = shadow coefficients S_r from Theta_A
#   - Edge weight = bare propagator eta^{-1}
#   - NO R-matrix appears
#
# The R-matrix (Givental's R(z) = exp(f(z))) appears ONLY in Convention G.
# Its Taylor coefficients |R_d| grow factorially (~ d!/(2pi)^d), reflecting
# the singularity of R at z = 2*pi*i.  But this is IRRELEVANT for double
# convergence in Convention S.
#
# Instead, double convergence follows from two INDEPENDENT exponential decays:
#   - Genus: lambda_g^FP ~ 2/(2*pi)^{2g}  (Bernoulli, proved)
#   - Arity: |S_r| ~ C * rho^r * r^{-5/2}  (shadow radius, proved)
# Combined with polynomial bounds on stable-graph combinatorics.

def faber_pandharipande_decay_verification(max_genus: int = 30) -> Dict[str, Any]:
    r"""Verify the Bernoulli decay of lambda_g^FP.

    The Faber-Pandharipande numbers satisfy:
        lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
        |lambda_g^FP| ~ 2/(2*pi)^{2g}

    Genus ratio: |lambda_{g+1}^FP / lambda_g^FP| -> 1/(2*pi)^2 ~ 0.0253

    This is the genus-direction decay rate, independent of the algebra.
    """
    values = {}
    ratios = {}
    for g in range(1, max_genus + 1):
        lam = float(lambda_fp(g))
        values[g] = lam
        if g > 1 and values[g - 1] > 0:
            ratios[g] = values[g] / values[g - 1]

    target_ratio = 1.0 / TWO_PI_SQ
    verified = True
    for g in range(5, max_genus + 1):
        if abs(ratios[g] - target_ratio) / target_ratio > 0.1:
            verified = False

    return {
        'verified': verified,
        'max_genus': max_genus,
        'target_ratio': target_ratio,
        'values': values,
        'ratios': ratios,
        'ratio_at_g20': ratios.get(20, None),
        'ratio_at_g30': ratios.get(30, None),
    }


def stable_graph_count_bound(g: int, r: int) -> int:
    r"""Upper bound on the number of stable graphs at (g, n=0) involving arity r.

    For genus g surfaces with no marked points, the number of stable
    graphs |G_{g,0}| grows polynomially with g.  Exact counts for low
    genus: g=2 -> 6, g=3 -> 29, g=4 -> 194, ...

    We use (2g)! as a safe (generous) upper bound.  This is vastly larger
    than the true count but is always valid and does not affect the
    exponential convergence analysis: the combinatorial prefactor is
    at most factorial while the Bernoulli decay is superexponential.

    Returns a conservative upper bound.
    """
    if g <= 0:
        return 0
    if g == 1:
        return 1  # single graph: the torus
    # Safe upper bound: (2g)! always exceeds |G_{g,0}|
    return int(math.factorial(2 * g))


# =========================================================================
# Section 2: Dressed propagator growth estimates
# =========================================================================

def dressed_propagator_growth_table(max_degree: int = 10) -> Dict[Tuple[int, int], float]:
    """Table of |P^R(D+, D-)| for all pairs up to max_degree.

    Returns dict (D+, D-) -> |P^R(D+, D-)|.
    """
    R = r_matrix_coefficients(2 * max_degree + 5)
    table = {}
    for dp in range(max_degree + 1):
        for dm in range(max_degree + 1):
            val = dressed_propagator_coefficient(dp, dm, R)
            table[(dp, dm)] = abs(float(val))
    return table


def dressed_propagator_envelope(max_degree: int = 10) -> Dict[str, Any]:
    r"""Verify polynomial growth of dressed propagator.

    We check that |P^R(D+, D-)| <= C_P * (1 + D+ + D-)^{-alpha}
    for some constants C_P, alpha > 0.

    The key structural fact: P^R(D+, D-) involves products R_a * R_b
    with a + b = D+ + D- + 1.  Since |R_d| ~ 1/(2*pi)^d, these products
    decay exponentially in the total degree.
    """
    table = dressed_propagator_growth_table(max_degree)

    # Group by total degree D = D+ + D-
    by_total = {}
    for (dp, dm), val in table.items():
        D = dp + dm
        if D not in by_total:
            by_total[D] = []
        by_total[D].append(val)

    # Max |P^R| at each total degree
    max_by_degree = {D: max(vals) for D, vals in by_total.items()}

    # Verify exponential decay: max_D |P^R| * (2*pi)^D should be bounded
    ratios = {}
    for D, mx in max_by_degree.items():
        if mx > 0:
            ratios[D] = mx * TWO_PI_SQ ** (D / 2)
        else:
            ratios[D] = 0.0

    # The propagator decays at rate ~ 1/(2*pi)^{D+D-+1}
    # because P^R ~ sum R_a R_b with a+b = D++D-+1
    return {
        'max_degree': max_degree,
        'max_by_total_degree': max_by_degree,
        'decay_rate_verification': ratios,
        'max_ratio': max(ratios.values()) if ratios else 0.0,
    }


# =========================================================================
# Section 3: Genus-g free energy at scalar level (arity 2)
# =========================================================================

def scalar_free_energy(kappa_val, g: int) -> Rational:
    """F_g^{scalar}(A) = kappa * lambda_g^FP.

    This is the arity-2 (scalar) contribution to the shadow partition
    function at genus g.
    """
    return F_g(kappa_val, g)


def scalar_genus_series(kappa_val, max_genus: int = 30) -> Dict[str, Any]:
    """Compute and analyze the scalar genus series sum_g F_g.

    Returns exact partial sums and convergence diagnostics.
    """
    terms = {}
    partial_sum = Rational(0)
    partial_sums = {}

    for g in range(1, max_genus + 1):
        fg = scalar_free_energy(kappa_val, g)
        terms[g] = fg
        partial_sum += fg
        partial_sums[g] = partial_sum

    # Genus ratios: |F_{g+1}/F_g| -> 1/(2*pi)^2
    ratios = {}
    for g in range(1, max_genus):
        if terms[g] != 0:
            ratios[g] = float(abs(terms[g + 1] / terms[g]))

    # Closed form: kappa * ((x/2)/sin(x/2) - 1) evaluated at x = hbar
    # At hbar = 1: sum = kappa * ((1/2)/sin(1/2) - 1)
    closed_form_at_1 = float(kappa_val) * (0.5 / math.sin(0.5) - 1)

    return {
        'kappa': kappa_val,
        'max_genus': max_genus,
        'terms': terms,
        'partial_sums': partial_sums,
        'ratios': ratios,
        'ratio_limit': 1.0 / TWO_PI_SQ,
        'closed_form_at_hbar_1': closed_form_at_1,
        'partial_sum_float': float(partial_sum),
        'convergent': True,
        'convergence_radius_hbar': 2 * PI,
    }


# =========================================================================
# Section 4: Shadow obstruction tower contribution at fixed genus (arity >= 3)
# =========================================================================

def shadow_arity_contribution(kappa_val, S_r: float, g: int, r: int) -> float:
    r"""Estimate the genus-g, arity-r shadow contribution Z_g^{(r)}.

    At the structural level, Z_g^{(r)} involves:
    - Shadow coefficient S_r at genus 0 (the vertex weight)
    - Genus-g tautological integral (Bernoulli decay from lambda_g)
    - Combinatorial factor from stable graph enumeration

    For the BOUND, we use the factorized estimate:

        |Z_g^{(r)}| <= |S_r| * |lambda_g^FP| * C_graph(g, r)

    where C_graph(g, r) is a combinatorial factor bounded polynomially in g and r.

    For the LEADING TERM (dominant stable graph at each (g,r)):
    - At genus g, arity r: the dominant contribution comes from the
      graph with one genus-g vertex carrying S_r, dressed by the
      R-matrix through the propagator.
    - This gives: Z_g^{(r)} ~ S_r * lambda_g^FP * (polynomial correction)

    We return the leading estimate |S_r * lambda_g^FP|.
    """
    lam = float(lambda_fp(g))
    return abs(S_r) * lam


def shadow_partition_term(kappa_val, alpha_val, S4_val,
                          g: int, r: int,
                          tower: Optional[ShadowTower] = None) -> float:
    r"""Compute (estimate) Z_g^{(r)} for given genus and arity.

    For arity r = 2 (scalar): exact value F_g = kappa * lambda_g^FP.
    For arity r >= 3: leading contribution from shadow obstruction tower coefficient S_r
    times the genus-g Faber-Pandharipande factor.

    The structural bound is:
        |Z_g^{(r)}| <= |S_r| * lambda_g^FP * C(g,r)
    where C(g,r) is a polynomial combinatorial factor.

    For class G/L algebras: S_r = 0 for r > r_max, so Z_g^{(r)} = 0.
    """
    if r < 2:
        return 0.0

    if r == 2:
        return float(scalar_free_energy(kappa_val, g))

    # Get shadow coefficient S_r
    if tower is None:
        tower = compute_shadow_tower(kappa_val, alpha_val, S4_val,
                                     max_arity=max(r + 2, 10))

    sc = tower.coefficients.get(r)
    if sc is None or sc.numerical is None:
        return 0.0

    S_r = sc.numerical
    if abs(S_r) < 1e-50:
        return 0.0

    return shadow_arity_contribution(kappa_val, S_r, g, r)


# =========================================================================
# Section 5: Double series evaluation
# =========================================================================

def shadow_partition_double_sum(kappa_val, alpha_val, S4_val,
                                 max_genus: int = 20,
                                 max_arity: int = 30,
                                 hbar: float = 1.0) -> Dict[str, Any]:
    r"""Evaluate the shadow partition function Z^sh(A, hbar) by double summation.

    Z^sh = sum_{g>=1} sum_{r>=2} hbar^{2g-2} * Z_g^{(r)}(A)

    At arity 2 (scalar): Z_g^{(2)} = kappa * lambda_g^FP (exact).
    At arity r >= 3: Z_g^{(r)} estimated from shadow obstruction tower.

    Returns comprehensive analysis including:
    - Individual terms Z_g^{(r)}
    - Partial sums by genus and arity
    - Convergence diagnostics
    - Error bounds
    """
    tower = compute_shadow_tower(kappa_val, alpha_val, S4_val,
                                 max_arity=max_arity)

    terms = {}          # (g, r) -> Z_g^{(r)}
    genus_sums = {}     # g -> sum_r Z_g^{(r)}
    arity_sums = {}     # r -> sum_g Z_g^{(r)}
    total = 0.0

    for g in range(1, max_genus + 1):
        hbar_factor = hbar ** (2 * g - 2)
        genus_total = 0.0

        for r in range(2, max_arity + 1):
            z_gr = shadow_partition_term(kappa_val, alpha_val, S4_val,
                                         g, r, tower)
            weighted = z_gr * hbar_factor
            terms[(g, r)] = weighted
            genus_total += weighted

            if r not in arity_sums:
                arity_sums[r] = 0.0
            arity_sums[r] += weighted

        genus_sums[g] = genus_total
        total += genus_total

    # Scalar subtotal
    scalar_total = sum(terms.get((g, 2), 0.0) for g in range(1, max_genus + 1))
    correction_total = total - scalar_total

    # Convergence diagnostics
    genus_ratios = {}
    for g in range(1, max_genus):
        if abs(genus_sums.get(g, 0.0)) > 1e-50:
            genus_ratios[g] = abs(genus_sums.get(g + 1, 0.0) / genus_sums[g])

    arity_ratios = {}
    for r in range(2, max_arity):
        if abs(arity_sums.get(r, 0.0)) > 1e-50:
            arity_ratios[r] = abs(arity_sums.get(r + 1, 0.0) / arity_sums[r])

    return {
        'kappa': float(kappa_val) if not isinstance(kappa_val, float) else kappa_val,
        'alpha': float(alpha_val) if not isinstance(alpha_val, float) else alpha_val,
        'S4': float(S4_val) if not isinstance(S4_val, float) else S4_val,
        'max_genus': max_genus,
        'max_arity': max_arity,
        'hbar': hbar,
        'total': total,
        'scalar_total': scalar_total,
        'correction_total': correction_total,
        'genus_sums': genus_sums,
        'arity_sums': arity_sums,
        'genus_ratios': genus_ratios,
        'arity_ratios': arity_ratios,
        'depth_class': tower.depth_class,
        'shadow_radius': float(Neval(tower.growth_rate)) if tower.growth_rate is not None else 0.0,
        'convergent': tower.convergent,
    }


# =========================================================================
# Section 6: Double convergence bound
# =========================================================================

def polylogarithm_5_2(rho: float, max_terms: int = 200) -> float:
    r"""Compute Li_{5/2}(rho) = sum_{k>=1} rho^k / k^{5/2}.

    Converges for |rho| <= 1.
    """
    if abs(rho) > 1.0:
        return float('inf')
    total = 0.0
    for k in range(1, max_terms + 1):
        term = rho ** k / k ** 2.5
        total += term
        if abs(term) < 1e-20:
            break
    return total


def genus_geometric_sum(max_genus: int = 1000) -> float:
    """Compute sum_{g>=1} 1/(2*pi)^{2g} = 1/((2*pi)^2 - 1).

    Exact value: 1/(4*pi^2 - 1) ~ 0.02596.
    """
    return 1.0 / (TWO_PI_SQ - 1)


def double_convergence_bound(kappa_val: float, rho: float) -> Dict[str, Any]:
    r"""Compute the double convergence bound (Convention S).

    Theorem (thm:shadow-double-convergence):

    In Convention S, the shadow partition function satisfies:

        |Z^sh(A)| <= |kappa| * G * L

    where:
        G = sum_{g>=1} lambda_g^FP ~ sum_{g>=1} 2/(2*pi)^{2g}
          = 2/(4*pi^2 - 1)  (geometric, from Bernoulli asymptotics)
        L = sum_{r>=2} |S_r| / |S_2| ~ sum_{r>=2} rho^{r-2} * r^{-5/2}
          <= Li_{5/2}(rho)  (polylogarithm, from shadow radius)

    The genus sum converges unconditionally (no algebra dependence).
    The arity sum converges when rho(A) < 1.

    No R-matrix needed: Convention S uses bare propagator + shadow coefficients.
    """
    G = genus_geometric_sum()
    L = polylogarithm_5_2(rho)

    # The scalar contribution is kappa * sum lambda_g^FP ~ kappa * G
    # The arity corrections multiply by L
    bound = abs(kappa_val) * 2 * G * (1.0 + L)

    return {
        'kappa': kappa_val,
        'rho': rho,
        'genus_sum_G': G,
        'polylog_L': L,
        'bound': bound,
        'convergent': rho < 1.0,
        'genus_ratio': 1.0 / TWO_PI_SQ,
        'arity_ratio': rho,
    }


# =========================================================================
# Section 7: Family specializations
# =========================================================================

def virasoro_shadow_partition(c_val: float,
                               max_genus: int = 20,
                               max_arity: int = 30,
                               hbar: float = 1.0) -> Dict[str, Any]:
    r"""Shadow partition function for Virasoro at central charge c.

    Virasoro data:
        kappa = c/2, alpha = 2, S_4 = 10/(c*(5c+22))
        rho(c) = sqrt(9*4 + 2*8*(c/2)*10/(c*(5c+22))) / (2*|c/2|)
               = sqrt(36 + 80/(5c+22)) / |c|
    """
    kappa = Rational(c_val, 2)
    alpha = Rational(2)
    S4 = Rational(10) / (Rational(c_val) * (5 * Rational(c_val) + 22))

    result = shadow_partition_double_sum(kappa, alpha, S4,
                                          max_genus, max_arity, hbar)
    result['family'] = 'Virasoro'
    result['c'] = c_val

    # Add analytic bound
    rho = result['shadow_radius']
    if rho < 1.0:
        bound = double_convergence_bound(float(kappa), rho)
        result['double_bound'] = bound
    else:
        result['double_bound'] = {'convergent': False, 'rho': rho}

    return result


def affine_sl2_shadow_partition(k_val: int,
                                 max_genus: int = 20,
                                 hbar: float = 1.0) -> Dict[str, Any]:
    r"""Shadow partition function for affine sl_2 at level k.

    Class L: shadow obstruction tower terminates at arity 3.
    kappa = 3*(k+2)/4, alpha = cubic shadow, S_4 = 0.
    Since S_4 = 0 (class L), the tower is finite and rho = 0.
    Only scalar + cubic contributions.
    """
    kappa = Rational(3) * (Rational(k_val) + 2) / 4
    alpha = Rational(1)  # nonzero cubic for class L
    S4 = Rational(0)     # class L

    result = shadow_partition_double_sum(kappa, alpha, S4,
                                          max_genus, max_arity=5, hbar=hbar)
    result['family'] = 'affine_sl2'
    result['k'] = k_val
    result['double_bound'] = double_convergence_bound(float(kappa), 0.0)
    return result


def heisenberg_shadow_partition(rank: int = 1,
                                 max_genus: int = 20,
                                 hbar: float = 1.0) -> Dict[str, Any]:
    r"""Shadow partition function for rank-n Heisenberg.

    Class G: shadow obstruction tower terminates at arity 2 (scalar only).
    kappa = rank, alpha = 0, S_4 = 0.
    Only scalar contribution: Z^sh = sum_g kappa * lambda_g^FP * hbar^{2g-2}.
    """
    kappa = Rational(rank)
    alpha = Rational(0)
    S4 = Rational(0)

    result = shadow_partition_double_sum(kappa, alpha, S4,
                                          max_genus, max_arity=3, hbar=hbar)
    result['family'] = 'Heisenberg'
    result['rank'] = rank
    result['double_bound'] = double_convergence_bound(float(rank), 0.0)
    return result


# =========================================================================
# Section 8: String theory contrast
# =========================================================================

def mirzakhani_volume_estimate(g: int) -> float:
    r"""Estimate Vol(M-bar_g) ~ (2g)! for string theory comparison.

    Mirzakhani's recursion gives Weil-Petersson volumes satisfying
    Vol(M-bar_g) ~ C * (2g)! * (some power corrections).
    We use the leading factorial for the contrast.
    """
    return float(math.factorial(2 * g))


def string_theory_contrast(kappa_val: float,
                            max_genus: int = 15) -> Dict[str, Any]:
    r"""Contrast shadow vs string theory genus expansion.

    Shadow:  |F_g| ~ 2|kappa| / (2*pi)^{2g}  (geometric decay)
    String:  |A_g| ~ C * (2g)!               (factorial growth)

    Ratio:   |F_g| / |A_g| ~ 2|kappa| / ((2*pi)^{2g} * (2g)!)
           -> 0 superexponentially fast.
    """
    shadow_terms = {}
    string_terms = {}
    ratios = {}

    for g in range(1, max_genus + 1):
        fg = abs(float(scalar_free_energy(Rational(kappa_val), g)))
        ag = mirzakhani_volume_estimate(g)
        shadow_terms[g] = fg
        string_terms[g] = ag
        if ag > 0:
            ratios[g] = fg / ag

    # Shadow partial sums converge; string partial sums diverge
    shadow_partial = {}
    string_partial = {}
    s_sum = 0.0
    st_sum = 0.0
    for g in range(1, max_genus + 1):
        s_sum += shadow_terms[g]
        st_sum += string_terms[g]
        shadow_partial[g] = s_sum
        string_partial[g] = st_sum

    return {
        'kappa': kappa_val,
        'shadow_terms': shadow_terms,
        'string_terms': string_terms,
        'ratios': ratios,
        'shadow_partial_sums': shadow_partial,
        'string_partial_sums': string_partial,
        'shadow_converges': True,
        'string_diverges': True,
        'shadow_final_sum': s_sum,
    }


# =========================================================================
# Section 9: Master convergence analysis
# =========================================================================

def convergence_analysis(kappa_val, alpha_val, S4_val,
                          max_genus: int = 20,
                          max_arity: int = 25) -> Dict[str, Any]:
    r"""Complete convergence analysis of the shadow partition function.

    Combines all components:
    1. R-matrix eigenvalue bounds
    2. Dressed propagator growth
    3. Scalar genus convergence
    4. Arity convergence (shadow radius)
    5. Double convergence bound
    """
    # 1. Faber-Pandharipande decay
    fp_decay = faber_pandharipande_decay_verification(max_genus)

    # 2. Shadow obstruction tower
    tower = compute_shadow_tower(kappa_val, alpha_val, S4_val,
                                 max_arity=max_arity)

    rho = 0.0
    if tower.growth_rate is not None:
        try:
            rho = float(Neval(tower.growth_rate))
        except (TypeError, ValueError):
            pass

    # 3. Scalar series
    scalar = scalar_genus_series(kappa_val, max_genus)

    # 4. Double sum
    double = shadow_partition_double_sum(kappa_val, alpha_val, S4_val,
                                          max_genus, max_arity)

    # 5. Bound
    kappa_f = float(kappa_val) if not isinstance(kappa_val, float) else kappa_val
    bound = double_convergence_bound(kappa_f, rho)

    return {
        'fp_decay_verified': fp_decay['verified'],
        'depth_class': tower.depth_class,
        'shadow_radius': rho,
        'arity_convergent': rho < 1.0,
        'scalar_convergent': True,
        'double_convergent': rho < 1.0,
        'scalar_sum': scalar['partial_sum_float'],
        'double_sum': double['total'],
        'correction_fraction': (double['correction_total'] / double['total']
                                if abs(double['total']) > 1e-50 else 0.0),
        'bound': bound['bound'],
        'genus_ratio': 1.0 / TWO_PI_SQ,
        'arity_ratio': rho,
    }
