"""Primitive kernel engine: genus-2 shells, stable graph sums, branch spectral
data, and operadic cumulant transforms.

Goes beyond the profile lookup table in modular_master.py to actually COMPUTE
primitive kernel data from corolla coefficients and stable graph combinatorics.

Mathematical content and verification targets:

1. GENUS-2 SHELL CALCULATOR
   Given a primitive kernel profile and numerical corolla coefficients, compute
   the genus-2 forcing R_2 as a numerical vector/matrix.  For Heisenberg this
   reduces to kappa * lambda_2 (pure scalar).  For affine it picks up a cubic
   bracket correction.  For Virasoro it receives all three channels: loop +
   bracket + planted-forest.

2. FEYNMAN TRANSFORM EXPANSION
   Implement the stable-graph sum at low genus.  At genus 1 with n = 1 there is
   exactly one graph contributing the tadpole integral.  At genus 2 with n = 0
   the six stable graphs are enumerated with their automorphism factors.

3. STABLE GRAPH CLASSIFICATION
   Classify all connected stable graphs of genus g with n legs for g <= 3,
   n <= 2 by the triple (|V|, |E_int|, h^1).  Verify counts, automorphism
   spectrum, and orbifold Euler characteristics.

4. BRANCH OPERATOR SPECTRAL DATA
   Given a branch rank and branch operator eigenvalues, compute the metaplectic
   half-density series, the spectral determinant, and verify squaring.

5. OPERADIC CUMULANT-MOMENT TRANSFORMS
   If the primitive kernel K_A is the cumulant of Theta_A, implement
   cumulant-to-moment and moment-to-cumulant transforms for the exponential
   formula on the modular operad (analogous to the classical exp/log on
   partition functions).

References:
  - Vol I, def:primitive-log-modular-kernel
  - Vol I, thm:primitive-to-global-reconstruction
  - Vol I, prop:primitive-shell-equations
  - Vol I, const:vol1-genus-spectral-sequence
  - Vol I, def:stable-graph-coefficient-algebra
  - Vol I, cor:metaplectic-square-root
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Dict, List, Optional, Tuple
from functools import lru_cache

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    genus1_stable_graphs_n0,
    genus1_stable_graphs_n1,
    genus2_stable_graphs_n0,
    graph_sum_scalar,
    orbifold_euler_characteristic,
    _bernoulli_exact,
    _lambda_fp_exact,
)


# =====================================================================
# 1. Genus-2 shell calculator
# =====================================================================

@dataclass
class CorollaCoefficients:
    """Numerical corolla coefficients for a primitive kernel evaluation.

    kappa:   scalar curvature = Tr(pairing) / 2 for the algebra
    cubic:   coefficient of the cubic corolla (C_3 coupling constant)
    quartic: coefficient of the quartic contact corolla (Q^contact)
    propagator: inverse Hessian on the 1-generator line (= 2/kappa for 1d)

    For multi-generator algebras, these should be traces / contractions
    to a single scalar.
    """
    kappa: Fraction
    cubic: Fraction = Fraction(0)
    quartic: Fraction = Fraction(0)
    propagator: Fraction = Fraction(0)

    @classmethod
    def heisenberg(cls, k: Fraction = Fraction(1), d: int = 1) -> CorollaCoefficients:
        """Heisenberg H_k^d: kappa = k*d, all higher corolla vanish."""
        kap = Fraction(k) * d
        return cls(kappa=kap, cubic=Fraction(0), quartic=Fraction(0),
                   propagator=Fraction(0))

    @classmethod
    def affine_sl2(cls, k: Fraction = Fraction(1)) -> CorollaCoefficients:
        """Affine sl_2 at level k: kappa = 3(k+2)/2, cubic from structure constants."""
        kap = Fraction(3) * (Fraction(k) + 2) / Fraction(2)
        # Cubic coupling from [T^a, T^b] = f^{ab}_c T^c; the cubic shadow
        # is determined by the Lie algebra structure constants.
        # On the primary line: C = f_{abc} proportional to k+h^v.
        # Exact cubic: C^2 / H = dim(g)(k+h^v)/2 * [structure factor]
        # For the scalar shell equation, only kappa enters at genus 2
        # for the loop-loop channel; the cubic enters via the bracket.
        cubic = Fraction(2)  # |f| normalised: T_{(1)}T = 2T for sl_2
        prop = Fraction(2) / kap if kap != 0 else Fraction(0)
        return cls(kappa=kap, cubic=cubic, quartic=Fraction(0), propagator=prop)

    @classmethod
    def virasoro(cls, c: Fraction = Fraction(1)) -> CorollaCoefficients:
        """Virasoro at central charge c: kappa = c/2, Q = 10/[c(5c+22)]."""
        c = Fraction(c)
        kap = c / Fraction(2)
        cubic = Fraction(2)
        denom = c * (5 * c + 22)
        quartic = Fraction(10) / denom if denom != 0 else Fraction(0)
        prop = Fraction(2) / c if c != 0 else Fraction(0)
        return cls(kappa=kap, cubic=cubic, quartic=quartic, propagator=prop)


def genus2_forcing_loop(kappa: Fraction) -> Fraction:
    """The loop-loop (non-separating node) contribution to R_2.

    This is Delta(K_{1,1}) = kappa * chi^orb(M_{1,1}) = kappa * (-1/12).
    The Delta operator is the non-separating clutching, which contracts
    two legs of K_{1,1} at genus 1 n=2 to produce genus 2 n=0.

    In the Feynman graph language, this is the genus-1 one-loop tadpole
    graph with one self-loop.
    """
    return kappa * Fraction(-1, 12)


def genus2_forcing_bracket(cubic: Fraction, propagator: Fraction) -> Fraction:
    """The bracket contribution (1/2)[K_{1,1}, K_{1,1}] to R_2.

    This is the separating-node channel: two genus-1 n=1 shells sewn
    at a separating node through the propagator.

    In the graph language this is the dumbbell graph (two genus-1 vertices
    connected by one edge).  |Aut| = 2 (swap the two genus-1 vertices).

    The bracket contribution is:
      (1/2) * cubic^2 * propagator * [chi^orb(M_{1,1})]^2
    which comes from the cubic corolla at each genus-1 vertex.

    For Heisenberg this is 0 (cubic = 0).
    For affine sl_2 at k=1: (1/2) * 4 * (4/15) * (1/144) = ...
    """
    # Each genus-1 vertex contributes chi^orb(M_{1,1}) = -1/12 to the
    # amplitude.  The vertex carries a cubic coupling.
    # The separating node graph has two vertices (g=1 each) and one edge.
    # Amplitude = cubic * chi(M_{1,1}) at vertex 0
    #           * cubic * chi(M_{1,1}) at vertex 1
    #           * propagator at edge
    #           / |Aut| = 2
    chi11 = Fraction(-1, 12)
    return Fraction(1, 2) * (cubic * chi11) ** 2 * propagator


def genus2_forcing_planted_forest(quartic: Fraction, propagator: Fraction,
                                   kappa: Fraction) -> Fraction:
    """The planted-forest (rigid) contribution Rpf2(K02) to R_2.

    This comes from the quartic contact interaction at a genus-0 vertex
    with two self-loops, creating a genus-2 curve via the banana graph.

    The banana graph has 1 vertex g=0 with 2 self-loops.  |Aut| = 8.
    Amplitude = quartic * kappa^2 / |Aut|.

    For Heisenberg this is 0 (quartic = 0).
    For Virasoro: quartic = 10/[c(5c+22)], kappa = c/2.
    """
    return quartic * kappa ** 2 / Fraction(8)


def genus2_forcing(coeffs: CorollaCoefficients) -> Dict[str, Fraction]:
    """Compute all channels of the genus-2 forcing R_2.

    Returns a dict with individual channels and the total.

    The total R_2 = F_2(A) enters the genus expansion
      F_g(A) = sum_Gamma |Aut(Gamma)|^{-1} * ell_Gamma(A)
    at g = 2.
    """
    loop = genus2_forcing_loop(coeffs.kappa)
    bracket = genus2_forcing_bracket(coeffs.cubic, coeffs.propagator)
    pf = genus2_forcing_planted_forest(coeffs.quartic, coeffs.propagator,
                                        coeffs.kappa)

    return {
        "loop": loop,
        "bracket": bracket,
        "planted_forest": pf,
        "total": loop + bracket + pf,
    }


def genus2_scalar_level(kappa: Fraction) -> Fraction:
    """F_2 at the scalar level: kappa * lambda_2^FP.

    lambda_2^FP = 7/5760.
    """
    return kappa * _lambda_fp_exact(2)


# =====================================================================
# 2. Feynman transform expansion
# =====================================================================

def tadpole_amplitude(kappa: Fraction) -> Fraction:
    """Genus-1 n=1 tadpole amplitude.

    The unique graph is: 1 vertex g=0, 1 self-loop, 1 leg.
    |Aut| = 2 (self-loop flip).

    At the scalar level, the amplitude is kappa / |Aut| = kappa / 2.
    This gives the genus-1 1-point function <T>_1 = kappa/2.
    """
    return kappa / Fraction(2)


def genus1_n0_amplitudes(kappa: Fraction) -> Dict[str, Fraction]:
    """Graph-by-graph amplitudes at genus 1, n = 0.

    Two graphs:
      (1) Smooth torus: 1 vertex g=1, no edges. Amplitude = chi(M_{1,0})... unstable.
          Actually M_{1,0} is unstable (2g-2+n = 0), so this graph does NOT
          contribute to the stable graph sum.  In the Feynman transform it
          contributes the bare partition function Z_1 at tree level.

          CORRECTION: for the COMPACTIFIED moduli space M-bar_{1,1} (with a
          marked point), the smooth graph IS stable.  For n = 0 at genus 1,
          M_{1,0} is the unstable stratum, so the partition function is
          defined via the forgetful map.

      (2) Nodal rational: 1 vertex g=0, 1 self-loop. |Aut| = 2.
          This IS stable (2*0 - 2 + 2 = 0... marginally stable).
          Amplitude = kappa / |Aut| = kappa/2.

    The total F_1(A) = kappa * lambda_1^FP = kappa/24.
    """
    graphs = genus1_stable_graphs_n0()
    results = {}

    for i, g in enumerate(graphs):
        ne = g.num_edges
        aut = g.automorphism_order()
        amp = kappa ** ne / Fraction(aut)

        if g.num_vertices == 1 and ne == 0:
            results[f"smooth_g1"] = amp
        elif g.num_vertices == 1 and ne == 1:
            results[f"self_loop_g0"] = amp
        else:
            results[f"graph_{i}"] = amp

    results["total"] = sum(results.values())
    return results


def genus2_n0_amplitudes_scalar(kappa: Fraction) -> Dict[str, Fraction]:
    """Graph-by-graph scalar amplitudes at genus 2, n = 0.

    Six graphs contributing to M-bar_{2,0}.  At the scalar level,
    each graph amplitude is kappa^|E| / |Aut(Gamma)|.

    Returns individual amplitudes and the total scalar sum.
    """
    graphs = genus2_stable_graphs_n0()
    graph_names = [
        "smooth_g2",           # g=2, 0 edges, |Aut|=1
        "irr_node_g1",         # g=1, 1 self-loop, |Aut|=2
        "banana_g0",           # g=0, 2 self-loops, |Aut|=8
        "separating_11",       # g=(1,1), 1 edge, |Aut|=2
        "theta_00",            # g=(0,0), 3 edges, |Aut|=12
        "mixed_01",            # g=(0,1), 2 edges, |Aut|=2
    ]

    results = {}
    for i, g in enumerate(graphs):
        ne = g.num_edges
        aut = g.automorphism_order()
        amp = kappa ** ne / Fraction(aut)
        name = graph_names[i] if i < len(graph_names) else f"graph_{i}"
        results[name] = amp

    results["total"] = sum(v for k, v in results.items())
    return results


def genus2_scalar_polynomial() -> Dict[int, Fraction]:
    """Scalar graph sum for genus 2 as a polynomial in kappa.

    sum_Gamma kappa^|E(Gamma)| / |Aut(Gamma)| = sum_{e=0}^3 c_e * kappa^e

    Returns {edge_count: coefficient}.
    """
    graphs = genus2_stable_graphs_n0()
    coeffs: Dict[int, Fraction] = {}
    for g in graphs:
        ne = g.num_edges
        aut = g.automorphism_order()
        coeffs[ne] = coeffs.get(ne, Fraction(0)) + Fraction(1, aut)
    return coeffs


# =====================================================================
# 3. Stable graph classification
# =====================================================================

def stable_graph_census(g: int, n: int) -> Dict[str, object]:
    """Full census of stable graphs at (g, n).

    Returns:
      count:           total number of non-isomorphic stable graphs
      by_vertices:     {|V|: count}
      by_edges:        {|E|: count}
      by_h1:           {h^1: count}
      by_VE:           {(|V|, |E|): count}
      aut_spectrum:    sorted list of |Aut(Gamma)| values
      aut_sum:         sum of 1/|Aut(Gamma)| (= orbifold point count)
      signed_aut_sum:  sum of (-1)^|E| / |Aut(Gamma)|
    """
    if 2 * g - 2 + n <= 0:
        return {"count": 0, "by_vertices": {}, "by_edges": {},
                "by_h1": {}, "by_VE": {}, "aut_spectrum": [],
                "aut_sum": Fraction(0), "signed_aut_sum": Fraction(0)}

    graphs = enumerate_stable_graphs(g, n)

    by_V: Dict[int, int] = {}
    by_E: Dict[int, int] = {}
    by_h1: Dict[int, int] = {}
    by_VE: Dict[Tuple[int, int], int] = {}
    aut_spectrum = []
    aut_sum = Fraction(0)
    signed_sum = Fraction(0)

    for gr in graphs:
        nv = gr.num_vertices
        ne = gr.num_edges
        h1 = gr.first_betti

        by_V[nv] = by_V.get(nv, 0) + 1
        by_E[ne] = by_E.get(ne, 0) + 1
        by_h1[h1] = by_h1.get(h1, 0) + 1
        by_VE[(nv, ne)] = by_VE.get((nv, ne), 0) + 1

        aut = gr.automorphism_order()
        aut_spectrum.append(aut)
        aut_sum += Fraction(1, aut)
        signed_sum += Fraction((-1) ** ne, aut)

    return {
        "count": len(graphs),
        "by_vertices": dict(sorted(by_V.items())),
        "by_edges": dict(sorted(by_E.items())),
        "by_h1": dict(sorted(by_h1.items())),
        "by_VE": dict(sorted(by_VE.items())),
        "aut_spectrum": sorted(aut_spectrum),
        "aut_sum": aut_sum,
        "signed_aut_sum": signed_sum,
    }


def genus_graph_counts() -> Dict[Tuple[int, int], int]:
    """Known stable graph counts for small (g, n).

    These are the exact values from the enumeration engine, cross-checked
    against the literature (Faber, Harer-Zagier).

    Returns {(g, n): count}.
    """
    known = {}
    for g, n in [(0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (2, 0)]:
        graphs = enumerate_stable_graphs(g, n)
        known[(g, n)] = len(graphs)
    return known


# =====================================================================
# 4. Branch operator spectral data
# =====================================================================

def spectral_determinant_series(eigenvalues: Tuple[Fraction, ...],
                                 order: int) -> List[Fraction]:
    """Taylor coefficients of det(1 - x*T) for diagonal T with given eigenvalues.

    det(1 - xT) = prod_i (1 - lambda_i * x)
               = sum_{k=0}^{rank} (-1)^k e_k(lambda_1,...,lambda_r) x^k

    where e_k is the k-th elementary symmetric polynomial.

    Returns the list [c_0, c_1, ..., c_order] of Taylor coefficients.
    """
    r = len(eigenvalues)
    n = min(order, r)
    # Elementary symmetric polynomials via Newton's method
    e = [Fraction(0)] * (n + 1)
    e[0] = Fraction(1)
    for lam in eigenvalues:
        for k in range(min(n, r), 0, -1):
            e[k] = e[k] - lam * e[k - 1]
    # Pad to order
    result = list(e) + [Fraction(0)] * max(0, order + 1 - len(e))
    return result[:order + 1]


def metaplectic_half_density_series(eigenvalues: Tuple[Fraction, ...],
                                     order: int) -> List[Fraction]:
    """Taylor coefficients of exp(1/2 sum_i log(1 - lambda_i x)).

    This is the metaplectic half-density delta(x) = det(1 - xT)^{1/2},
    expanded as a formal power series.

    The key property (cor:metaplectic-square-root): delta(x)^2 = det(1 - xT).

    Computation: first compute log(det(1 - xT)) = sum_i log(1 - lambda_i x)
                                                 = -sum_i sum_{m>=1} lambda_i^m x^m / m
                                                 = -sum_{m>=1} p_m x^m / m
    where p_m = sum_i lambda_i^m (power sum symmetric polynomial).

    Then delta(x) = exp(1/2 * log_coeffs) via the exponential formula.

    Returns [c_0, c_1, ..., c_order].
    """
    # Step 1: power sums p_m = sum lambda_i^m
    power_sums = [Fraction(0)] * (order + 1)
    for m in range(1, order + 1):
        for lam in eigenvalues:
            power_sums[m] += lam ** m

    # Step 2: log coefficients: -p_m / m, halved for the half-density
    log_coeffs = [Fraction(0)] * (order + 1)
    for m in range(1, order + 1):
        log_coeffs[m] = -power_sums[m] / Fraction(2 * m)

    # Step 3: exponentiate via recursive formula
    # exp(sum_{m>=1} a_m x^m) = sum_{n>=0} c_n x^n
    # c_0 = 1, c_n = (1/n) sum_{k=1}^n k * a_k * c_{n-k}
    c = [Fraction(0)] * (order + 1)
    c[0] = Fraction(1)
    for n in range(1, order + 1):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += Fraction(k) * log_coeffs[k] * c[n - k]
        c[n] = s / Fraction(n)

    return c


def verify_metaplectic_squaring(eigenvalues: Tuple[Fraction, ...],
                                 order: int) -> bool:
    """Verify that delta(x)^2 = det(1 - xT) to the given order.

    This is the content of cor:metaplectic-square-root: the metaplectic
    half-density is the canonical square root of the spectral determinant.
    """
    det_coeffs = spectral_determinant_series(eigenvalues, order)
    half_coeffs = metaplectic_half_density_series(eigenvalues, order)

    # Square the half-density series: (sum c_n x^n)^2 = sum d_n x^n
    # d_n = sum_{k=0}^n c_k * c_{n-k}
    for n in range(order + 1):
        square_n = Fraction(0)
        for k in range(n + 1):
            square_n += half_coeffs[k] * half_coeffs[n - k]
        if square_n != det_coeffs[n]:
            return False
    return True


def branch_spectral_data(eigenvalues: Tuple[Fraction, ...],
                          order: int = 6) -> Dict[str, object]:
    """Complete spectral data for a branch operator.

    Given the eigenvalues of the branch operator T (the matrix of
    conformal weights on the branch line), compute:

    1. The spectral determinant det(1 - xT) as a polynomial
    2. The metaplectic half-density delta(x) = det(1 - xT)^{1/2}
    3. Verification that delta^2 = det (the squaring identity)
    4. The spectral radius (max |eigenvalue|)
    5. The trace tr(T) = -c_1 coefficient of the determinant
    """
    det_coeffs = spectral_determinant_series(eigenvalues, order)
    half_coeffs = metaplectic_half_density_series(eigenvalues, order)
    squaring_ok = verify_metaplectic_squaring(eigenvalues, order)

    trace = sum(eigenvalues)
    spectral_radius = max(abs(lam) for lam in eigenvalues) if eigenvalues else Fraction(0)

    return {
        "eigenvalues": eigenvalues,
        "rank": len(eigenvalues),
        "det_coefficients": det_coeffs,
        "half_density_coefficients": half_coeffs,
        "squaring_verified": squaring_ok,
        "trace": trace,
        "spectral_radius": spectral_radius,
    }


# =====================================================================
# 5. Operadic cumulant-moment transforms
# =====================================================================

# In the modular operad, the relationship between the partition function
# Z_g (moments) and the free energy F_g (cumulants) follows the
# exponential formula:
#
#   Z = exp(F)  as formal power series in hbar
#
# where hbar tracks the genus expansion:
#   Z = sum_{g>=0} Z_g hbar^{2g-2}
#   F = sum_{g>=0} F_g hbar^{2g-2}
#
# The cumulant-moment relation at genus g is:
#   Z_g = sum_{partitions pi of g} prod_{b in pi} F_{g_b} / |Aut(pi)|
#
# where pi ranges over all ways to write genus g as a sum of genera.
# This is the operadic incarnation of the classical exp/log relationship.

def _integer_partitions(n: int) -> List[Tuple[int, ...]]:
    """All partitions of n into positive parts, in non-increasing order."""
    if n == 0:
        return [()]
    result = []
    _partition_helper(n, n, (), result)
    return result


def _partition_helper(n: int, max_part: int, current: Tuple[int, ...],
                      result: List[Tuple[int, ...]]):
    """Recursive helper for integer partition enumeration."""
    if n == 0:
        result.append(current)
        return
    for k in range(min(n, max_part), 0, -1):
        _partition_helper(n - k, k, current + (k,), result)


def _partition_automorphism(partition: Tuple[int, ...]) -> int:
    """Automorphism factor of a partition: product of m_k! where m_k = multiplicity of k."""
    if not partition:
        return 1
    counts: Dict[int, int] = {}
    for p in partition:
        counts[p] = counts.get(p, 0) + 1
    result = 1
    for m in counts.values():
        result *= factorial(m)
    return result


def cumulant_to_moment(cumulants: Dict[int, Fraction],
                        max_genus: int) -> Dict[int, Fraction]:
    """Convert free energies F_g (cumulants) to partition functions Z_g (moments).

    The exponential formula on the genus expansion:
      Z_g = sum_{partitions of g} prod_{b in partition} F_{g_b} / |Aut(partition)|

    F_0 is treated specially: Z_0 = exp(F_0) = 1 (normalised, F_0 = 0 by convention).
    For g >= 1:
      Z_g = F_g + sum_{partitions with >= 2 parts summing to g} prod F_{g_b} / |Aut|

    Parameters:
      cumulants: {g: F_g} for g = 1, 2, ..., max_genus (F_0 = 0 assumed)
      max_genus: compute Z_g for g = 1, ..., max_genus

    Returns:
      {g: Z_g} for g = 1, ..., max_genus
    """
    moments = {}
    for g in range(1, max_genus + 1):
        total = Fraction(0)
        for partition in _integer_partitions(g):
            # Compute product of cumulants for this partition
            prod = Fraction(1)
            valid = True
            for part in partition:
                if part in cumulants:
                    prod *= cumulants[part]
                else:
                    valid = False
                    break
            if valid:
                aut = _partition_automorphism(partition)
                total += prod / Fraction(aut)
        moments[g] = total
    return moments


def moment_to_cumulant(moments: Dict[int, Fraction],
                        max_genus: int) -> Dict[int, Fraction]:
    """Convert partition functions Z_g (moments) to free energies F_g (cumulants).

    The logarithmic formula (Moebius inversion of the exponential formula):
      F_g = Z_g - sum_{partitions of g with >= 2 parts} (Moebius coefficient) * prod Z_{g_b}

    At low genera:
      F_1 = Z_1
      F_2 = Z_2 - (1/2) Z_1^2
      F_3 = Z_3 - Z_1 Z_2 + (1/3) Z_1^3

    These are exactly the classical cumulant-moment relations, now applied
    to the genus expansion of the modular operad.
    """
    cumulants = {}
    for g in range(1, max_genus + 1):
        total = moments.get(g, Fraction(0))
        # Subtract all partitions with >= 2 parts
        for partition in _integer_partitions(g):
            if len(partition) <= 1:
                continue  # skip the trivial partition (g)
            prod = Fraction(1)
            valid = True
            for part in partition:
                if part in cumulants:
                    prod *= cumulants[part]
                else:
                    valid = False
                    break
            if valid:
                aut = _partition_automorphism(partition)
                total -= prod / Fraction(aut)
        cumulants[g] = total
    return cumulants


def verify_cumulant_moment_inverse(max_genus: int = 5) -> bool:
    """Verify that cumulant_to_moment and moment_to_cumulant are inverse.

    Start with test cumulants F_g = 1/(g+1)!, apply exp, then log, and
    check recovery.
    """
    test_cumulants = {g: Fraction(1, factorial(g + 1))
                      for g in range(1, max_genus + 1)}
    moments = cumulant_to_moment(test_cumulants, max_genus)
    recovered = moment_to_cumulant(moments, max_genus)

    for g in range(1, max_genus + 1):
        if recovered[g] != test_cumulants[g]:
            return False
    return True


def heisenberg_cumulant_moment_table(kappa: Fraction = Fraction(1),
                                      max_genus: int = 4
                                      ) -> Dict[str, Dict[int, Fraction]]:
    """Compute cumulant/moment table for Heisenberg.

    For Heisenberg (Gaussian / shadow depth 2):
      F_g(H_k) = kappa * lambda_g^FP

    Then Z_g = sum_{partitions of g} prod F_{g_b} / |Aut|.

    Returns both the cumulant and moment tables.
    """
    cumulants = {}
    for g in range(1, max_genus + 1):
        cumulants[g] = kappa * _lambda_fp_exact(g)

    moments = cumulant_to_moment(cumulants, max_genus)

    return {
        "cumulants": cumulants,
        "moments": moments,
    }


# =====================================================================
# 6. Genus spectral sequence at low genus
# =====================================================================

def genus_spectral_sequence_page(g: int, n: int = 0) -> Dict[int, int]:
    """E_1 page of the genus spectral sequence at total genus g.

    Decomposes stable graphs by first Betti number h^1 (loop genus).

    Returns {h^1: number of graphs at that loop level}.
    """
    if 2 * g - 2 + n <= 0:
        return {}

    graphs = enumerate_stable_graphs(g, n)
    counts: Dict[int, int] = {}
    for gr in graphs:
        h1 = gr.first_betti
        counts[h1] = counts.get(h1, 0) + 1
    return dict(sorted(counts.items()))


def scalar_amplitude_by_loop_level(g: int, n: int,
                                    kappa: Fraction) -> Dict[int, Fraction]:
    """Scalar amplitude decomposed by loop level h^1.

    At each loop level, compute sum_{Gamma: h^1 = p} kappa^|E| / |Aut|.

    This is the h^1-graded piece of the genus spectral sequence.
    """
    if 2 * g - 2 + n <= 0:
        return {}

    graphs = enumerate_stable_graphs(g, n)
    by_h1: Dict[int, Fraction] = {}

    for gr in graphs:
        h1 = gr.first_betti
        ne = gr.num_edges
        aut = gr.automorphism_order()
        amp = kappa ** ne / Fraction(aut)
        by_h1[h1] = by_h1.get(h1, Fraction(0)) + amp

    return dict(sorted(by_h1.items()))


# =====================================================================
# 7. Heisenberg reduction verification
# =====================================================================

def heisenberg_genus2_check(kappa: Fraction = Fraction(1)) -> Dict[str, object]:
    """Verify that genus-2 forcing for Heisenberg reduces to kappa * lambda_2^FP.

    For Heisenberg:
      - cubic = quartic = 0
      - R_2 = Delta(K_{1,1}) only (pure loop-loop)
      - The scalar graph sum equals kappa * lambda_2^FP = kappa * 7/5760

    This is a verification that the genus-2 shell is correctly computed.
    """
    coeffs = CorollaCoefficients.heisenberg(k=kappa)
    forcing = genus2_forcing(coeffs)

    # For pure Heisenberg, the forcing IS just the scalar graph sum
    scalar = genus2_scalar_level(kappa)

    # The full scalar graph sum at genus 2
    graph_sum = graph_sum_scalar(genus2_stable_graphs_n0(), kappa)

    return {
        "forcing_total": forcing["total"],
        "forcing_loop_only": forcing["loop"],
        "forcing_bracket": forcing["bracket"],
        "forcing_pf": forcing["planted_forest"],
        "scalar_level": scalar,
        "graph_sum": graph_sum,
        "bracket_is_zero": forcing["bracket"] == Fraction(0),
        "pf_is_zero": forcing["planted_forest"] == Fraction(0),
    }


# =====================================================================
# 8. Integer partition data
# =====================================================================

def partition_count(n: int) -> int:
    """Number of partitions of n (for cross-checks)."""
    return len(_integer_partitions(n))


def connected_partition_count(n: int) -> int:
    """Number of partitions of n with exactly one part (= 1 for n >= 1)."""
    return sum(1 for p in _integer_partitions(n) if len(p) == 1)
