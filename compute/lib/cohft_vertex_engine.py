r"""CohFT vertex engine: computes all vertex factors V(g,n) from first principles.

MATHEMATICAL FRAMEWORK
======================

The shadow CohFT assigns tautological classes Omega_{g,n}(A) in H*(M-bar_{g,n})
to each chirally Koszul algebra A.  The CohFT vertex factor is:

    V(g,n) = int_{M-bar_{g,n}} Omega_{g,n}(A)

At genus 0: V(0,n) = S_n(A), the shadow coefficients (family-specific).

At genus >= 1, the Givental-Teleman reconstruction theorem (thm:cohft-reconstruction)
gives V(g,n) in terms of the universal R-matrix and Witten-Kontsevich numbers:

    V(g,n) = SUM_{d_1+...+d_n = 3g-3+n} (PROD R_{d_i}) * <tau_{d_1}...tau_{d_n}>_g

where:
  - R_d = coefficient of z^d in R(z) = exp(SUM B_{2k}/(2k(2k-1)) z^{2k-1})
  - <tau_{d_1}...tau_{d_n}>_g = Witten-Kontsevich intersection number (DVV recursion)
  - The dimension constraint sum d_i = 3g - 3 + n ensures the integral is nonzero

KEY PROPERTY: The R-matrix is UNIVERSAL (Hodge).  Family-specific information
enters only through genus-0 vertex factors V(0,n) = S_n.

The FULL genus-g free energy is computed by the graph sum:
    F_g(A) = SUM_Gamma (1/|Aut(Gamma)|) * PROD_v V(g_v, n_v) * PROD_e P

where P = 1/kappa is the propagator and the sum is over stable graphs.

References:
  thm:cohft-reconstruction (higher_genus_modular_koszul.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
  prop:givental-vertex-reconstruction (thqg_fredholm_partition_functions.tex)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, S, cancel, expand, simplify, bernoulli, factorial

from compute.lib.shadow_cohft_tautological import (
    wk_intersection,
)
from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    genus2_stable_graphs_n0,
)


# =========================================================================
# Section 1: R-matrix coefficients (computed from correct Bernoulli numbers)
# =========================================================================

# NOTE: The existing givental_r_matrix_from_ahat() in shadow_cohft_tautological.py
# uses a buggy Bernoulli recursion (_bernoulli_exact uses C(m,k) instead of
# C(m+1,k)), producing WRONG R-matrix coefficients (e.g., R_1 = 0 instead of 1/12).
# We implement the R-matrix correctly here using sympy.bernoulli.

_R_CACHE: Optional[List[Fraction]] = None
_R_MAX_ORDER: int = 0


def _bernoulli_fraction(n: int) -> Fraction:
    """Correct Bernoulli number B_n as exact Fraction, via sympy."""
    b = bernoulli(n)
    return Fraction(int(b.p), int(b.q))


def r_matrix_coefficients(max_d: int = 12) -> List[Fraction]:
    r"""Compute Givental R-matrix coefficients R_0, R_1, ..., R_{max_d}.

    R(z) = exp(f(z)) where f(z) = SUM_{k>=1} B_{2k}/(2k(2k-1)) z^{2k-1}.

    The exponent has only ODD powers of z:
        f(z) = (1/12)z - (1/360)z^3 + (1/1260)z^5 - ...

    Computation: R'(z) = f'(z) R(z) with R(0) = 1.

    Known values:
        R_0 = 1
        R_1 = 1/12
        R_2 = 1/288
        R_3 = -139/51840

    Returns list [R_0, R_1, ..., R_{max_d}] as exact Fraction values.
    """
    global _R_CACHE, _R_MAX_ORDER
    if _R_CACHE is not None and _R_MAX_ORDER >= max_d:
        return _R_CACHE[:max_d + 1]

    # Exponent coefficients: f(z) = SUM a_{2k-1} z^{2k-1}
    exponent = {}
    for kk in range(1, max_d + 2):
        deg = 2 * kk - 1
        if deg > max_d + 1:
            break
        B2k = _bernoulli_fraction(2 * kk)
        exponent[deg] = B2k / Fraction(2 * kk * (2 * kk - 1))

    # f'(z) coefficients: f'(z) = SUM (2k-1) a_{2k-1} z^{2k-2}
    fprime = [Fraction(0)] * (max_d + 2)
    for deg, coeff in exponent.items():
        if deg - 1 < len(fprime):
            fprime[deg - 1] += Fraction(deg) * coeff

    # R'(z) = f'(z) * R(z), R(0) = 1  (Cauchy product)
    R = [Fraction(0)] * (max_d + 1)
    R[0] = Fraction(1)
    for n in range(max_d):
        s = Fraction(0)
        for j in range(min(n + 1, len(fprime))):
            if n - j < len(R):
                s += fprime[j] * R[n - j]
        if n + 1 < len(R):
            R[n + 1] = s / Fraction(n + 1)

    _R_CACHE = R
    _R_MAX_ORDER = max_d
    return R[:max_d + 1]


# =========================================================================
# Section 2: Integer partition enumeration for vertex factors
# =========================================================================

def _compositions(total: int, n_parts: int) -> List[Tuple[int, ...]]:
    """All n-tuples of nonneg integers summing to total."""
    if n_parts == 0:
        return [()] if total == 0 else []
    if n_parts == 1:
        return [(total,)]
    result = []
    for first in range(total + 1):
        for rest in _compositions(total - first, n_parts - 1):
            result.append((first,) + rest)
    return result


# =========================================================================
# Section 3: CohFT vertex factors from Givental reconstruction
# =========================================================================

@lru_cache(maxsize=512)
def cohft_vertex_raw(g: int, n: int) -> Fraction:
    r"""Raw CohFT vertex factor T(g,n) from Givental reconstruction.

    T(g,n) = SUM_{d_1+...+d_n = 3g-3+n, d_i >= 0}
             (PROD R_{d_i}) * <tau_{d_1}...tau_{d_n}>_g

    This is the Hodge vertex factor: it depends only on g, n
    and the universal R-matrix, NOT on the algebra A.

    For n = 0:
      - g = 0: undefined (M_{0,0} unstable, returns 0)
      - g = 1: F_1^{top} = 1/24 (from dilaton equation)
      - g >= 2: T(g,0) = lambda_g^FP (Faber-Pandharipande)

    Returns exact Fraction.
    """
    # Special case: g=1, n=0 (M_{1,0} unstable but F_1 defined via dilaton)
    if g == 1 and n == 0:
        return Fraction(1, 24)

    if 2 * g - 2 + n <= 0:
        return Fraction(0)

    # Special case: n = 0
    if n == 0:
        # g >= 2: the Hodge integral lambda_g^FP
        B2g = Fraction(bernoulli(2 * g))
        power = 2 ** (2 * g - 1)
        return Fraction((power - 1) * abs(B2g), power * int(factorial(2 * g)))

    # General case: n >= 1
    dim = 3 * g - 3 + n  # dimension constraint
    if dim < 0:
        return Fraction(0)

    R = r_matrix_coefficients(max(dim, 12))

    total = Fraction(0)
    for comp in _compositions(dim, n):
        # comp = (d_1, ..., d_n) with sum = dim
        # Check all d_i are within R-matrix range
        if any(d >= len(R) for d in comp):
            continue
        # Product of R-coefficients
        r_prod = Fraction(1)
        for d in comp:
            r_prod *= R[d]
        # WK intersection number
        wk = wk_intersection(g, comp)
        total += r_prod * wk

    return total


# =========================================================================
# Section 4: Named vertex factor values
# =========================================================================

def vertex_factor_table(max_g: int = 3, max_n: int = 4) -> Dict[Tuple[int, int], Fraction]:
    """Compute table of all CohFT vertex factors V(g,n) for g <= max_g, n <= max_n."""
    table = {}
    for g in range(0, max_g + 1):
        for n in range(0, max_n + 1):
            if 2 * g - 2 + n > 0:
                table[(g, n)] = cohft_vertex_raw(g, n)
    return table


# =========================================================================
# Section 5: Full graph-sum free energy at genus 2
# =========================================================================

def _graph_amplitude_full(graph: StableGraph, shadow_data: Dict, R_coeffs: List[Fraction]) -> Fraction:
    """Compute the full graph amplitude using CohFT vertex factors.

    For genus-0 vertices: uses shadow_data[n] = S_n (family-specific).
    For genus >= 1 vertices: uses cohft_vertex_raw(g, n) (universal Hodge).
    Propagator: P = shadow_data['propagator'].

    Parameters
    ----------
    graph : StableGraph
    shadow_data : dict with keys 'kappa', 'propagator', and integer keys for S_n
    R_coeffs : list of R-matrix coefficients (not used directly, but ensures cache)
    """
    valences = graph.valence

    amp = Fraction(1)

    # Vertex factors
    for i, g_v in enumerate(graph.vertex_genera):
        n_v = valences[i]
        if g_v == 0:
            # Genus-0: use shadow data S_n
            sn = shadow_data.get(n_v, Fraction(0))
            amp *= sn
        else:
            # Genus >= 1: use CohFT vertex factor
            vf = cohft_vertex_raw(g_v, n_v)
            amp *= vf

    # Edge factors (propagator)
    P = shadow_data['propagator']
    for _ in graph.edges:
        amp *= P

    return amp


def genus2_free_energy_full(kappa, S3, S4, propagator=None) -> Dict:
    r"""Compute the FULL genus-2 free energy from graph sum with CohFT vertex factors.

    Uses the 6 stable graphs at (g=2, n=0).

    For genus-0 vertices: V(0,2) = kappa, V(0,3) = S3, V(0,4) = S4.
    For genus >= 1 vertices: V(g,n) from cohft_vertex_raw (universal).
    Propagator: P = 1/kappa.

    Parameters
    ----------
    kappa : Fraction — modular characteristic
    S3 : Fraction — cubic shadow coefficient
    S4 : Fraction — quartic shadow coefficient (Q^contact)
    propagator : Fraction (default 1/kappa)

    Returns dict with individual graph amplitudes and total.
    """
    if propagator is None:
        propagator = Fraction(1) / kappa

    shadow_data = {
        'kappa': kappa,
        'propagator': propagator,
        2: kappa,       # V(0,2) = kappa
        3: S3,          # V(0,3) = cubic shadow
        4: S4,          # V(0,4) = quartic shadow
        0: Fraction(0), # V(0,0) undefined
        1: Fraction(0), # V(0,1) = 0 (string equation)
    }

    # Ensure R-matrix cached
    R = r_matrix_coefficients(12)

    graphs = genus2_stable_graphs_n0()
    names = ['smooth_g2', 'irr_node', 'banana', 'separating', 'theta', 'mixed']

    results = {}
    total = Fraction(0)

    for name, graph in zip(names, graphs):
        amp = _graph_amplitude_full(graph, shadow_data, R)
        aut = graph.automorphism_order()
        weighted = amp / Fraction(aut)
        results[name] = {
            'amplitude': amp,
            'aut': aut,
            'weighted': weighted,
        }
        total += weighted

    return {
        'graphs': results,
        'total': total,
        'kappa': kappa,
        'S3': S3,
        'S4': S4,
    }


def heisenberg_F2_graph_sum(kappa=None) -> Fraction:
    """Genus-2 graph sum for Heisenberg using raw Givental vertex factors.

    NOTE: This does NOT match the Hodge partition function kappa * lambda_2^FP
    because the bare propagator P = 1/kappa misses the dressed propagator
    corrections from the R-matrix.  The raw Givental vertex factors T(g,n)
    require the DRESSED propagator P^R(psi,psi') = eta^{-1}/(psi+psi')
    (integrated over psi-classes at the edge) to reproduce the correct CohFT.

    The difference between the raw graph sum and kappa * lambda_2^FP quantifies
    the edge-dressing correction, which is:
        delta_edge = F_2^{raw} - kappa * lambda_2^FP
    """
    k = kappa if kappa is not None else Fraction(1)
    result = genus2_free_energy_full(k, Fraction(0), Fraction(0))
    return result['total']


def edge_dressing_correction_g2(kappa=None) -> Fraction:
    """The edge-dressing correction at genus 2.

    delta = F_2^{raw Givental} - kappa * lambda_2^FP

    This is the amount by which the raw (bare-propagator) graph sum
    overestimates the Hodge CohFT partition function.  It comes from
    the difference between the bare propagator 1/kappa and the dressed
    propagator integral over psi-classes at the edge.
    """
    k = kappa if kappa is not None else Fraction(1)
    raw = heisenberg_F2_graph_sum(k)
    target = k * Fraction(7, 5760)
    return raw - target


def virasoro_F2_symbolic():
    """Genus-2 free energy for Virasoro as sympy expression in c.

    kappa = c/2, S3 = 2, S4 = 10/(c(5c+22)), P = 2/c.
    """
    c = Symbol('c')
    kappa = c / 2
    S3 = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    P = 2 / c

    graphs = genus2_stable_graphs_n0()
    names = ['smooth_g2', 'irr_node', 'banana', 'separating', 'theta', 'mixed']

    total = S.Zero
    graph_results = {}

    for name, graph in zip(names, graphs):
        valences = graph.valence
        amp = S.One

        for i, g_v in enumerate(graph.vertex_genera):
            n_v = valences[i]
            if g_v == 0:
                if n_v == 2:
                    amp *= kappa
                elif n_v == 3:
                    amp *= S3
                elif n_v == 4:
                    amp *= S4
                else:
                    amp *= S.Zero
            else:
                vf = cohft_vertex_raw(g_v, n_v)
                amp *= Rational(vf.numerator, vf.denominator)

        for _ in graph.edges:
            amp *= P

        aut = graph.automorphism_order()
        weighted = cancel(amp / aut)
        graph_results[name] = weighted
        total += weighted

    return {
        'graphs': graph_results,
        'total': cancel(total),
    }


# =========================================================================
# Section 6: Complementarity at CohFT level
# =========================================================================

def virasoro_F2_complementarity():
    """Verify F_2(c) + F_2(26-c) for Virasoro including shadow corrections.

    Returns the sum as a sympy expression in c.
    """
    c = Symbol('c')

    # F_2(c)
    r1 = virasoro_F2_symbolic()
    F2_c = r1['total']

    # F_2(26-c): substitute c -> 26-c
    F2_dual = F2_c.subs(c, 26 - c)

    total = cancel(expand(F2_c + F2_dual))
    return {
        'F2_c': F2_c,
        'F2_dual': F2_dual,
        'sum': total,
    }


# =========================================================================
# Section 7: Modular operad vertex factors from MC equation
# =========================================================================

def operad_vertex_V11(S3, kappa):
    r"""V^{operad}(1,1) from MC equation at (g=1,n=1).

    MC: V(1,1) + Delta(S_3) = 0, where Delta(S_3) = 3*S_3/kappa.
    Result: V(1,1) = -3*S_3/kappa.
    Gaussian: 0. Virasoro: -12/c.
    """
    return -3 * S3 / kappa


def operad_vertex_V12(S3, S4, kappa):
    r"""V^{operad}(1,2) from MC equation at (g=1,n=2).

    MC: V(1,2) + [S_3,V(1,1)]/kappa + Delta(S_4) = 0.
    Result: V(1,2) = 3*S_3**2/kappa**2 - 6*S_4/kappa.
    Gaussian: 0. Virasoro: (240c+936)/(c^2(5c+22)).
    """
    return 3 * S3**2 / kappa**2 - 6 * S4 / kappa


def virasoro_F2_operad():
    """Full genus-2 Virasoro free energy from MC-derived vertex factors.

    F_2 = 7c/11520 + (240c+941)/(c^3(5c+22)) + 296/(3c^3).
    Self-dual: F_2(13) = F_2(13)^!.
    """
    c = Symbol('c')
    kappa = c / 2
    S3 = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    P = 2 / c

    V11 = operad_vertex_V11(S3, kappa)
    V12 = operad_vertex_V12(S3, S4, kappa)

    corolla = kappa * Rational(7, 5760)
    irr_node = V12 * P / 2
    banana = S4 * P**2 / 8
    separating = V11**2 * P / 2
    theta = S3**2 * P**3 / 12
    mixed = S3 * V11 * P**2 / 2

    graphs = {
        'corolla': cancel(corolla),
        'irr_node': cancel(irr_node),
        'banana': cancel(banana),
        'separating': cancel(separating),
        'theta': cancel(theta),
        'mixed': cancel(mixed),
    }
    total = cancel(sum(graphs.values()))
    return {'graphs': graphs, 'total': total, 'V11': cancel(V11), 'V12': cancel(V12)}


def virasoro_F2_complementarity_operad():
    """F_2(c) + F_2(26-c) with MC-derived vertex factors."""
    c = Symbol('c')
    result = virasoro_F2_operad()
    F2_c = result['total']
    F2_dual = F2_c.subs(c, 26 - c)
    return {'F2_c': F2_c, 'F2_dual': cancel(F2_dual), 'sum': cancel(expand(F2_c + F2_dual))}


# =========================================================================
# Section 8: Utility — vertex factor display
# =========================================================================

def print_vertex_table(max_g: int = 3, max_n: int = 4):
    """Print a formatted table of CohFT vertex factors."""
    table = vertex_factor_table(max_g, max_n)
    print(f"{'(g,n)':<10} {'V(g,n)':<30} {'float':<15}")
    print("-" * 55)
    for (g, n), v in sorted(table.items()):
        print(f"({g},{n}){'':<5} {str(v):<30} {float(v):.10f}")
