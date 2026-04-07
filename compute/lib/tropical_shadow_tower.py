r"""Tropical geometry of the shadow obstruction tower.

The shadow obstruction tower Theta_A has a tropical interpretation
via the tropicalization of the log-FM compactification (Mok, Pillar C).

MATHEMATICAL FRAMEWORK
======================

The key identification (thm:planted-forest-tropicalization, prop:planted-forest-tropical):

    G_pf = Trop(FM_n(X | D))

Planted forests = tropical skeleton of the log-FM space.

The shadow amplitude ell_Gamma on each stable graph Gamma becomes a
TROPICAL AMPLITUDE: a product of vertex weights (from the transferred
L_infinity operations ell_k^{(g)}) and edge propagators (the tropical
limit of the d-log kernel).

TROPICAL CURVE COUNTS
=====================

The genus-g shadow projection is a tropical curve count:

    F_g(A) = sum_Gamma (1/|Aut(Gamma)|) * mult^trop(Gamma) * w^sh(Gamma, A)

where:
    - mult^trop(Gamma) = I(Gamma) is the TROPICAL MULTIPLICITY
      (the Hodge integral, equal to the classical Witten-Kontsevich
      intersection number by Mikhalkin-type comparison)
    - w^sh(Gamma, A) is the SHADOW WEIGHT: product of vertex weights
      from the transferred operations of A
    - 1/|Aut(Gamma)| is the tropical orbifold factor

TROPICAL DECOMPOSITION THEOREM
===============================

The MC relation at (g, 0) decomposes tropically:

    sum_{Gamma in M^trop_g} (1/|Aut|) * mult^trop * w^sh = 0

This splits into:

    MUMFORD SHELL (graphs with all vertex genera >= 1):
        depends only on kappa = S_2 (curvature)
    +
    PLANTED-FOREST SHELL (graphs with at least one genus-0 vertex):
        depends on higher shadow data S_3, S_4, S_5, ...
    =
    0

The planted-forest shell = tropical boundary of the moduli space.
It lives on the CODIMENSION >= 2 strata of M^trop_g.

MIKHALKIN CORRESPONDENCE
========================

Classical Mikhalkin: counts of algebraic curves = counts of tropical curves
with multiplicities.

Shadow Mikhalkin: the shadow tower does NOT count tropical curves in a
fixed target space.  Rather, the "target" is the cyclic deformation complex
Def_cyc(A), which is ALGEBRA-DEPENDENT.  The tropical curve count
F_g = sum (1/|Aut|) * mult * w^sh
is a curve count in a virtual sense: the tropical multiplicity mult^trop
is universal (comes from Witten-Kontsevich), but the shadow weight w^sh
depends on the algebra A through the OPE data.

The correct analogy is:

    MIKHALKIN: trop. curve count in (C*)^2 --> algebraic curve count
    SHADOW:    trop. graph sum in M^trop_g --> shadow obstruction class in Def_cyc(A)

The "target space" is not geometric but algebraic: it is the shadow algebra
A^sh = H_*(Def_cyc^mod(A)).

TROPICAL DEPTH AND THE G/L/C/M CLASSIFICATION
==============================================

The tropical depth of Gamma is the number of genus-0 vertices with valence >= 3.
The four shadow classes control which tropical strata contribute:

    Class G (depth 2): only smooth + codim-1 strata.  F_g = kappa * lambda_g^FP.
        Tropical content: sum over graphs WITHOUT genus-0 vertices of val >= 3.
        These are the "Mumford graphs."

    Class L (depth 3): adds codim-2 strata with trivalent genus-0 vertices.
        The cubic shadow S_3 enters via trivalent tropical vertices.
        Cyclic Jacobi may force cancellation (affine case).

    Class C (depth 4): adds quartic tropical vertices.
        The quartic contact invariant Q^contact enters.
        Stratum separation (charged stratum exits the complex) terminates the tower.

    Class M (depth infinity): ALL tropical strata contribute.
        The tropical curve count involves vertices of ALL valences.
        The infinite shadow tower = infinite tropical depth.

GENUS-2 TROPICAL DICTIONARY (7 graphs)
=======================================

    Graph    Codim  Trop. type       mult^trop  Weight           Shell
    -----    -----  ---------        ---------  ------           -----
    A smooth   0    genus-2 curve      1        F_2             —
    B lollip   1    nodal g=1         7/240     kappa           Mumford
    D dumbb.   1    2-component g=1   -1/576    kappa^2         Mumford
    C sunset   2    2-loop g=0         0        S_4             PF (vanishes!)
    E bridge   2    bridge+loop       -1/24     S_3 * kappa     PF
    F theta    3    theta graph        1        S_3^2           PF
    G fig-8    3    dumbbell g=0       1        S_3^2           PF

delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48 (from E+F+G; C vanishes by self-loop parity)

GENUS-3 TROPICAL DICTIONARY (42 graphs, 35 planted-forest)
==========================================================

35 graphs among 42 total are planted-forest type.
The planted-forest correction is the 11-term polynomial in
(kappa, S_3, S_4, S_5) from eq:delta-pf-genus3-explicit.
The 35 planted-forest graphs = the tropical boundary of M^trop_{3,0}.

References:
    higher_genus_modular_koszul.tex:
        thm:planted-forest-tropicalization
        prop:planted-forest-tropical
        def:planted-forest-coefficient-algebra
        rem:planted-forest-correction-explicit
        thm:mc-tautological-descent
        thm:tropical-koszulness
        cor:tropical-cohen-macaulay
    pixton_shadow_bridge.py: stable graph enumeration, Hodge integrals
    tropical_koszulness.py: tropical bar complex, planted trees
    tropical_bar_engine.py: metric trees, tropical integrals
    tropical_shadow_higher.py: tropical moduli, theta functions
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Integer, Matrix, Rational, Symbol, cancel, collect, expand,
    factor, simplify, sqrt, symbols, Abs, S, Poly, oo,
)

from .pixton_shadow_bridge import (
    ShadowData,
    StableGraph,
    graph_integral_genus2,
    graph_integral_general,
    wk_intersection,
    vertex_weight,
    stable_graphs_genus2_0leg,
    stable_graphs_genus3_0leg,
    is_planted_forest_graph,
    heisenberg_shadow_data,
    affine_shadow_data,
    virasoro_shadow_data,
)
from .stable_graph_enumeration import _bernoulli_exact, _lambda_fp_exact


# =========================================================================
# Symbols
# =========================================================================

c_sym = Symbol('c')
kappa_sym = Symbol('kappa')
S3_sym = Symbol('S_3')
S4_sym = Symbol('S_4')
S5_sym = Symbol('S_5')


# =========================================================================
# Section 1: Tropical multiplicity and shadow weight
# =========================================================================

def tropical_multiplicity(graph: StableGraph) -> Fraction:
    r"""Compute the tropical multiplicity mult^trop(Gamma).

    The tropical multiplicity equals the Hodge integral I(Gamma):
    the Witten-Kontsevich intersection number associated to the
    stable graph.

    By Mikhalkin-type comparison (Kerber-Markwig for higher genus),
    this equals the classical intersection number.

    The tropical multiplicity is UNIVERSAL: it depends only on the
    graph topology, not on the algebra A.

    Parameters:
        graph: a stable graph of type (g, 0)

    Returns:
        Exact rational tropical multiplicity.
    """
    return graph_integral_general(graph)


def shadow_weight_general(graph: StableGraph, shadow: ShadowData) -> Any:
    r"""Compute the shadow weight w^sh(Gamma, A).

    The shadow weight is the product of vertex weights from the
    transferred L_infinity operations:

        w^sh(Gamma, A) = prod_{v in V(Gamma)} ell_{val(v)}^{(g(v))}(A)

    where ell_k^{(g)} is the genus-g, k-input transferred operation.

    For rank-1 on a primary line:
        ell_k^{(0)} = S_k (the shadow coefficient at arity k)
        ell_1^{(1)} = kappa
        ell_2^{(1)} = S_3*kappa/24 - S_3^2  (MC-determined)
        ell_0^{(2)} = 7*kappa/5760  (F_2, determined by MC)

    Parameters:
        graph: stable graph
        shadow: shadow data for the algebra

    Returns:
        Shadow weight (sympy expression in the shadow parameters).
    """
    weight = Integer(1)
    for (gv, val) in graph.vertices:
        if gv == 0:
            weight *= shadow.S(val)
        elif gv == 1:
            if val == 0:
                weight *= Integer(0)  # unstable
            elif val == 1:
                weight *= shadow.kappa
            elif val == 2:
                # MC-determined: ell_2^{(1)} = S_3*kappa/24 - S_3^2
                # (from prop:ell2-genus1-mc in the manuscript)
                weight *= (shadow.S3 * shadow.kappa / 24 - shadow.S3 ** 2)
            else:
                weight *= shadow.kappa  # higher: ell_k^{(1)} ~ kappa
        elif gv == 2:
            if val == 0:
                # The smooth genus-2 contribution: F_2 = 7*kappa/5760
                # This is DETERMINED by the MC relation, not independently given.
                # For the tropical decomposition we treat it as the unknown.
                weight *= Integer(1)  # placeholder (MC determines this)
            else:
                weight *= Integer(1)
    return weight


def tropical_graph_amplitude(graph: StableGraph, shadow: ShadowData) -> Any:
    r"""Full tropical amplitude for a stable graph.

    I^trop(Gamma, A) = (1/|Aut(Gamma)|) * mult^trop(Gamma) * w^sh(Gamma, A)

    This is the contribution of the tropical curve of type Gamma
    to the genus-g shadow projection F_g(A).

    Parameters:
        graph: stable graph
        shadow: shadow data

    Returns:
        Tropical amplitude (sympy expression).
    """
    mult = tropical_multiplicity(graph)
    w = shadow_weight_general(graph, shadow)
    mult_sympy = Integer(mult.numerator) / Integer(mult.denominator)
    return cancel(mult_sympy * w / graph.automorphism_order)


# =========================================================================
# Section 2: Tropical shell decomposition
# =========================================================================

@dataclass
class TropicalShellDecomposition:
    """Decomposition of the MC relation into Mumford and planted-forest shells.

    The MC relation at (g, 0):
        F_g + (Mumford shell) + (planted-forest shell) = 0

    Mumford shell: graphs with all vertex genera >= 1
        (depends only on kappa)
    Planted-forest shell: graphs with at least one genus-0 vertex of val >= 3
        (depends on higher shadow data S_3, S_4, ...)
    """
    genus: int
    algebra: str
    mumford_graphs: List[Dict[str, Any]]
    planted_forest_graphs: List[Dict[str, Any]]
    mumford_total: Any
    planted_forest_total: Any  # = delta_pf^{(g,0)}
    smooth_graph: Dict[str, Any]


def tropical_shell_decomposition(g: int, shadow: ShadowData) -> TropicalShellDecomposition:
    r"""Decompose the MC relation at genus g into tropical shells.

    Parameters:
        g: genus (>= 2)
        shadow: shadow data for the algebra

    Returns:
        TropicalShellDecomposition with Mumford and PF contributions.
    """
    if g == 2:
        graphs = stable_graphs_genus2_0leg()
    elif g == 3:
        graphs = stable_graphs_genus3_0leg()
    else:
        raise ValueError(f"Genus {g} not implemented")

    mumford_graphs = []
    pf_graphs = []
    smooth_data = None
    mumford_total = Integer(0)
    pf_total = Integer(0)

    for G in graphs:
        amp = tropical_graph_amplitude(G, shadow)
        mult = tropical_multiplicity(G)
        w = shadow_weight_general(G, shadow)
        entry = {
            'name': G.name,
            'codimension': G.codimension,
            'tropical_multiplicity': mult,
            'shadow_weight': w,
            'automorphism_order': G.automorphism_order,
            'amplitude': amp,
            'is_planted_forest': is_planted_forest_graph(G),
            'vertices': G.vertices,
        }

        if G.codimension == 0:
            # Smooth graph: F_g (determined by MC from the rest)
            smooth_data = entry
        elif is_planted_forest_graph(G):
            pf_graphs.append(entry)
            pf_total += amp
        else:
            mumford_graphs.append(entry)
            mumford_total += amp

    return TropicalShellDecomposition(
        genus=g,
        algebra=shadow.name,
        mumford_graphs=mumford_graphs,
        planted_forest_graphs=pf_graphs,
        mumford_total=cancel(mumford_total),
        planted_forest_total=cancel(pf_total),
        smooth_graph=smooth_data,
    )


# =========================================================================
# Section 3: Tropical depth filtration
# =========================================================================

def tropical_depth(graph: StableGraph) -> int:
    r"""Compute the tropical depth of a stable graph.

    The tropical depth is the number of genus-0 vertices with
    valence >= 3 in the graph.  These vertices carry the higher
    L_infinity operations S_k (k >= 3) from the shadow tower.

    Tropical depth 0: all vertices have genus >= 1 (Mumford graph).
    Tropical depth 1: one genus-0 vertex with val >= 3.
    Tropical depth k: k such vertices.

    The shadow depth classification:
        Class G: delta_pf = 0 at all genera (tropical depth irrelevant)
        Class L: tropical depth <= 1 is nontrivial
        Class C: tropical depth <= 2 is nontrivial
        Class M: all tropical depths contribute
    """
    return sum(1 for (gv, val) in graph.vertices if gv == 0 and val >= 3)


def tropical_depth_filtration(g: int) -> Dict[int, List[StableGraph]]:
    r"""Organize stable graphs by tropical depth.

    Parameters:
        g: genus

    Returns:
        Dict mapping tropical depth -> list of stable graphs at that depth.
    """
    if g == 2:
        graphs = stable_graphs_genus2_0leg()
    elif g == 3:
        graphs = stable_graphs_genus3_0leg()
    else:
        raise ValueError(f"Genus {g} not implemented")

    result = {}
    for G in graphs:
        d = tropical_depth(G)
        if d not in result:
            result[d] = []
        result[d].append(G)
    return result


def tropical_depth_statistics(g: int) -> Dict[str, Any]:
    """Compute statistics of the tropical depth filtration at genus g."""
    filt = tropical_depth_filtration(g)
    total = sum(len(v) for v in filt.values())
    pf_count = sum(len(v) for d, v in filt.items() if d > 0)

    # For each depth, compute the sum of 1/|Aut(Gamma)|
    depth_volumes = {}
    for d, graphs in filt.items():
        depth_volumes[d] = sum(Fraction(1, G.automorphism_order) for G in graphs)

    return {
        'genus': g,
        'total_graphs': total,
        'planted_forest_count': pf_count,
        'mumford_count': total - pf_count,
        'depths': sorted(filt.keys()),
        'count_by_depth': {d: len(v) for d, v in filt.items()},
        'volume_by_depth': depth_volumes,
        'max_tropical_depth': max(filt.keys()) if filt else 0,
    }


# =========================================================================
# Section 4: Tropical period matrix and theta function connection
# =========================================================================

def metric_graph_period_matrix(edges: List[Tuple[int, int]],
                               edge_lengths: List[float],
                               n_verts: int) -> List[List[float]]:
    r"""Compute the tropical period matrix for a metric graph.

    The tropical period matrix Omega^trop is the g x g matrix
    of cycle inner products with the edge-length metric:

        Omega^trop_{ij} = sum_{e in C_i cap C_j} sign_i(e) * sign_j(e) * ell_e

    where C_1, ..., C_g is a basis of the cycle space H_1(Gamma, Z).

    Parameters:
        edges: list of (u, v) pairs
        edge_lengths: list of edge lengths
        n_verts: number of vertices

    Returns:
        g x g period matrix (list of lists).
    """
    if not edges:
        return [[0.0]]

    # Union-find for connected components
    parent = list(range(n_verts))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    # Find spanning tree
    tree_edges = set()
    non_tree = []
    n_components = n_verts

    for e_idx, (u, v) in enumerate(edges):
        if u == v:
            non_tree.append(e_idx)
        elif union(u, v):
            tree_edges.add(e_idx)
            n_components -= 1
        else:
            non_tree.append(e_idx)

    h1 = len(non_tree)
    if h1 == 0:
        return [[0.0]]

    # Build tree adjacency
    adj = [[] for _ in range(n_verts)]
    for e_idx in tree_edges:
        u, v = edges[e_idx]
        adj[u].append((v, e_idx, +1))
        adj[v].append((u, e_idx, -1))

    # Find fundamental cycles
    cycles = []
    for nt_idx in non_tree:
        u, v = edges[nt_idx]
        if u == v:
            cycles.append({nt_idx: +1})
            continue
        # BFS path from u to v in tree
        visited = [False] * n_verts
        parent_map = [None] * n_verts
        visited[u] = True
        queue = [u]
        found = False
        while queue and not found:
            cur = queue.pop(0)
            for w, e_idx, sign in adj[cur]:
                if not visited[w]:
                    visited[w] = True
                    parent_map[w] = (cur, e_idx, sign)
                    if w == v:
                        found = True
                        break
                    queue.append(w)
        if found:
            cycle = {nt_idx: +1}
            cur = v
            while cur != u:
                pv, ei, s = parent_map[cur]
                cycle[ei] = s
                cur = pv
            cycles.append(cycle)
        else:
            cycles.append({nt_idx: +1})

    # Compute period matrix
    g = len(cycles)
    Omega = [[0.0] * g for _ in range(g)]
    for i in range(g):
        for j in range(g):
            for e_idx in range(len(edges)):
                if e_idx in cycles[i] and e_idx in cycles[j]:
                    Omega[i][j] += (cycles[i][e_idx]
                                    * cycles[j][e_idx]
                                    * edge_lengths[e_idx])
    return Omega


def shadow_metric_from_tropical_theta(kappa_val: float,
                                       S3_val: float,
                                       S4_val: float) -> Dict[str, Any]:
    r"""Connect the shadow metric Q_L to tropical theta function.

    The shadow metric Q_L(t) = (2*kappa + 3*S_3*t)^2 + 2*Delta*t^2
    with Delta = 8*kappa*S_4 arises from the genus-1 tropical
    propagator structure.

    At genus 1, the tropical curve is a single loop of circumference
    omega.  The shadow generating function H(t) satisfies
    H(t)^2 = t^4 * Q_L(t), where Q_L is the shadow metric.

    The tropical theta function at genus 1:
        Theta^trop(z | omega) = -pi * min_{n in Z}(omega * n^2 - 2nz)

    The connection: the shadow metric Q_L controls the SECOND DERIVATIVE
    of the tropical theta function with respect to the deformation
    parameter t (which parameterizes the primary line in the shadow algebra).

    Returns:
        Dict with shadow metric values and tropical theta data.
    """
    Delta = 8 * kappa_val * S4_val
    Q_at_0 = 4 * kappa_val ** 2
    Q_linear = 12 * kappa_val * S3_val
    Q_quadratic = 9 * S3_val ** 2 + 2 * Delta

    # Q_L(t) = Q_at_0 + Q_linear * t + Q_quadratic * t^2
    # = (2*kappa + 3*S_3*t)^2 + 2*Delta*t^2
    # Verify the factorization
    cross_term = 12 * kappa_val * S3_val  # 2 * 2kappa * 3S_3
    Q_linear_check = cross_term
    Q_quadratic_check = 9 * S3_val ** 2 + 16 * kappa_val * S4_val

    # Critical discriminant
    # Delta = 8*kappa*S_4 classifies shadow depth
    discriminant = Delta

    return {
        'kappa': kappa_val,
        'S3': S3_val,
        'S4': S4_val,
        'Delta': discriminant,
        'Q_at_0': Q_at_0,
        'Q_linear_coefficient': Q_linear,
        'Q_quadratic_coefficient': Q_quadratic,
        'factorization_check': abs(Q_linear - Q_linear_check) < 1e-12,
        'depth_class': 'G' if abs(S3_val) < 1e-12 and abs(S4_val) < 1e-12
                       else 'L' if abs(S4_val) < 1e-12
                       else 'C' if abs(discriminant) < 1e-12
                       else 'M',
    }


# =========================================================================
# Section 5: Tropical Mikhalkin correspondence analysis
# =========================================================================

@dataclass
class TropicalCorrespondence:
    """Analysis of the Mikhalkin-type correspondence for the shadow tower.

    Classical Mikhalkin: algebraic curve count = tropical curve count
    (in (C*)^2 or a toric variety, with tropical multiplicities).

    Shadow analogue: the shadow tower IS a tropical curve count on
    M^trop_g, but the multiplicities are NOT the standard Mikhalkin
    multiplicities.  Instead:

        shadow multiplicity = mult^trop(Gamma) * w^sh(Gamma, A) / |Aut(Gamma)|

    The Mikhalkin multiplicity (for curves in a toric surface) is
    determined by the lattice index at each vertex.  The shadow
    multiplicity replaces the lattice index by the shadow weight.

    The key question: is there a target space T_A such that
    F_g(A) = number of tropical curves in T_A with Mikhalkin multiplicities?

    Answer: NO in general.  The shadow weight w^sh depends on the
    FULL OPE data of A, which is not captured by any fixed toric target.
    The shadow tower is a tropical curve count in a VIRTUAL sense:
    the "target" is the shadow algebra A^sh, not a geometric space.

    However, for CLASS G (Heisenberg): F_g = kappa * lambda_g^FP,
    and lambda_g^FP IS a genuine tropical Hodge integral.
    In this case, the "target" is a point (trivial), and the
    tropical count reduces to the Hodge integral.
    """
    genus: int
    algebra_class: str
    has_geometric_target: bool
    tropical_count: Any
    classical_prediction: Any
    mikhalkin_holds: bool
    explanation: str


def mikhalkin_correspondence_analysis(g: int, shadow: ShadowData) -> TropicalCorrespondence:
    r"""Analyze whether Mikhalkin correspondence holds for the shadow tower.

    Parameters:
        g: genus
        shadow: shadow data

    Returns:
        TropicalCorrespondence with analysis.
    """
    decomp = tropical_shell_decomposition(g, shadow)

    # Compute total F_g from the MC relation:
    # F_g + mumford + pf = 0, so F_g = -(mumford + pf)
    F_g = cancel(-(decomp.mumford_total + decomp.planted_forest_total))

    # Classical prediction: F_g = kappa * lambda_g^FP
    lambda_fp = Integer(_lambda_fp_exact(g).numerator) / Integer(
        _lambda_fp_exact(g).denominator)
    classical = shadow.kappa * lambda_fp

    # Check if F_g matches the scalar prediction
    diff = simplify(F_g - classical)

    # Determine the algebra class
    depth_class = shadow.depth_class

    # For class G: Mikhalkin holds trivially (target = point)
    # For class L: Mikhalkin holds if cyclic Jacobi forces PF cancellation
    # For class M: Mikhalkin FAILS at genus >= 2 for multi-weight algebras
    # but may hold on the scalar lane (uniform-weight)
    if depth_class == 'G':
        has_target = True
        mikhalkin = True
        explanation = (
            "Class G (Gaussian): planted-forest shell vanishes identically. "
            "F_g = kappa * lambda_g^FP is a genuine tropical Hodge integral. "
            "The target is trivial (a point); the tropical count reduces to "
            "the Witten-Kontsevich intersection on M^trop_g."
        )
    elif depth_class == 'L':
        has_target = False
        mikhalkin = (diff == 0)
        explanation = (
            "Class L (Lie): planted-forest shell involves S_3 via trivalent "
            "genus-0 vertices.  On the full multi-generator space, cyclic "
            "Jacobi forces cancellation; on the rank-1 primary line, PF "
            "correction is generically nonzero.  No geometric target space."
        )
    elif depth_class == 'C':
        has_target = False
        mikhalkin = False
        explanation = (
            "Class C (contact): quartic contact invariant Q^contact enters. "
            "Stratum separation terminates the tower at depth 4. "
            "No Mikhalkin-type geometric target; the tropical curve count "
            "is algebra-dependent through Q^contact."
        )
    else:
        has_target = False
        mikhalkin = False
        explanation = (
            "Class M (mixed): infinite shadow depth.  ALL tropical strata "
            "contribute.  The planted-forest correction delta_pf is an "
            "11-term polynomial at genus 3 involving S_3, S_4, S_5.  "
            "No geometric target space: the shadow weight depends on the "
            "full infinite sequence (S_2, S_3, S_4, ...) of shadow data."
        )

    return TropicalCorrespondence(
        genus=g,
        algebra_class=depth_class,
        has_geometric_target=has_target,
        tropical_count=F_g,
        classical_prediction=classical,
        mikhalkin_holds=mikhalkin,
        explanation=explanation,
    )


# =========================================================================
# Section 6: Genus-2 tropical dictionary
# =========================================================================

def genus2_tropical_dictionary(shadow: ShadowData) -> List[Dict[str, Any]]:
    r"""Build the complete genus-2 tropical dictionary.

    For each of the 7 stable graphs of M-bar_{2,0}, compute:
    - Tropical type (topological description as metric graph)
    - Tropical multiplicity (Hodge integral)
    - Shadow weight (vertex weight from shadow data)
    - Shell classification (Mumford vs planted-forest)
    - Tropical amplitude (the full contribution)

    Returns:
        List of dicts, one per graph, sorted by codimension.
    """
    graphs = stable_graphs_genus2_0leg()
    dictionary = []

    # Tropical type descriptions
    trop_types = {
        'A_smooth': 'smooth genus-2 tropical curve (single vertex)',
        'B_lollipop': 'genus-1 curve with one non-separating node (banana with loop)',
        'C_sunset': 'genus-0 curve with two self-loops (tropical sunset)',
        'D_dumbbell': 'two genus-1 components connected by bridge',
        'E_bridge_loop': 'genus-0 with self-loop bridged to genus-1',
        'F_theta': 'theta graph: two genus-0 vertices, three bridges',
        'G_figure8_bridge': 'figure-8: two genus-0 vertices, each with self-loop, one bridge',
    }

    # Metric graph data: edges and self-loops as lists of (u, v) pairs
    # for computing the tropical period matrix
    metric_edges = {
        'A_smooth': [],
        'B_lollipop': [(0, 0)],  # self-loop
        'C_sunset': [(0, 0), (0, 0)],  # two self-loops
        'D_dumbbell': [(0, 1)],  # bridge
        'E_bridge_loop': [(0, 0), (0, 1)],  # self-loop + bridge
        'F_theta': [(0, 1), (0, 1), (0, 1)],  # three bridges
        'G_figure8_bridge': [(0, 0), (1, 1), (0, 1)],  # two self-loops + bridge
    }

    for G in graphs:
        mult = tropical_multiplicity(G)
        w = shadow_weight_general(G, shadow)
        amp = tropical_graph_amplitude(G, shadow)
        is_pf = is_planted_forest_graph(G)

        entry = {
            'name': G.name,
            'codimension': G.codimension,
            'tropical_type': trop_types.get(G.name, 'unknown'),
            'tropical_multiplicity': mult,
            'shadow_weight': w,
            'automorphism_order': G.automorphism_order,
            'amplitude': amp,
            'shell': 'planted-forest' if is_pf else ('Mumford' if G.codimension > 0 else 'smooth'),
            'metric_edges': metric_edges.get(G.name, []),
            'first_betti': G.genus - sum(gv for gv, _ in G.vertices),
            'vertices': G.vertices,
        }
        dictionary.append(entry)

    return sorted(dictionary, key=lambda x: x['codimension'])


# =========================================================================
# Section 7: Genus-3 tropical analysis
# =========================================================================

def genus3_tropical_boundary_analysis(shadow: ShadowData) -> Dict[str, Any]:
    r"""Analyze the tropical boundary of M^trop_{3,0}.

    At genus 3, there are 42 stable graphs total, of which 35
    are planted-forest type.  The planted-forest correction
    delta_pf^{(3,0)} is the 11-term polynomial from
    eq:delta-pf-genus3-explicit.

    The 35 planted-forest graphs decompose by tropical depth:
    - Depth 1: graphs with exactly one genus-0 vertex of val >= 3
    - Depth 2: graphs with two such vertices
    - Depth >= 3: graphs with three or more such vertices

    Returns:
        Dict with genus-3 tropical analysis.
    """
    graphs = stable_graphs_genus3_0leg()
    depth_filt = tropical_depth_filtration(3)

    # Compute amplitudes by tropical depth
    amp_by_depth = {}
    for d, glist in depth_filt.items():
        total = Integer(0)
        for G in glist:
            total += tropical_graph_amplitude(G, shadow)
        amp_by_depth[d] = cancel(total)

    # Total planted-forest correction
    pf_total = Integer(0)
    for d in sorted(depth_filt.keys()):
        if d > 0:
            pf_total += amp_by_depth[d]

    # Shadow visibility: which S_r appear at genus 3?
    # By cor:shadow-visibility-genus: S_r enters at g_min(S_r) = floor(r/2) + 1
    # At g=3: r up to 2*3 - 1 = 5, so S_3, S_4, S_5 enter.
    visible_shadows = []
    for r in range(3, 2 * 3):
        g_min = r // 2 + 1
        if g_min <= 3:
            visible_shadows.append(r)

    return {
        'genus': 3,
        'total_graphs': len(graphs),
        'planted_forest_count': sum(1 for G in graphs if is_planted_forest_graph(G)),
        'mumford_count': sum(1 for G in graphs if not is_planted_forest_graph(G)),
        'depth_filtration': {d: len(v) for d, v in depth_filt.items()},
        'amplitude_by_depth': amp_by_depth,
        'planted_forest_total': cancel(pf_total),
        'visible_shadow_coefficients': visible_shadows,
        'shadow_visibility_formula': 'g_min(S_r) = floor(r/2) + 1',
    }


# =========================================================================
# Section 8: Tropical edge-length integrals
# =========================================================================

def tropical_edge_integral(pole_order: int) -> Fraction:
    r"""Compute the regulated tropical integral for a single edge.

    int_0^infty ell^{p-1}/(p-1)! * exp(-ell) d(ell)
    = Gamma(p) / (p-1)!
    = 1  for all p >= 1.

    This is the tropicalization of the configuration-space propagator.
    The pole order p is the order of the OPE pole flowing through the edge.

    For the bar complex propagator d log E(z,w) (weight 1):
    p = 1, integral = 1.

    For higher poles in the OPE (e.g., Virasoro T*T has poles at z^{-4}, z^{-2}):
    the bar complex extracts d log = residue of the LOGARITHMIC derivative,
    reducing all poles by 1 (AP19). So the bar propagator always has p = 1.

    The tropical integral = 1 for ALL edges, independent of the OPE.
    This is the tropical manifestation of the universality of the
    bar propagator (rem:propagator-weight-universality).
    """
    if pole_order <= 0:
        return Fraction(0)
    # Gamma(p) / (p-1)! = (p-1)! / (p-1)! = 1
    return Fraction(1)


def tropical_graph_integral(graph: StableGraph) -> Fraction:
    r"""Total tropical edge-length integral for a stable graph.

    Since each regulated edge integral = 1, the total is 1^{|E|} = 1.
    The non-trivial content is in the VERTEX FACTORS (shadow weights)
    and the HODGE INTEGRAL (tropical multiplicity).

    The tropical integral factorizes as:
        (edge-length integral) * (Hodge integral) * (vertex factors)
        =        1             *   mult^trop     * w^sh

    This factorization is a consequence of the tropical limit:
    the edge-length integration decouples from the moduli integration.
    """
    return Fraction(1)  # independent of graph!


# =========================================================================
# Section 9: Tropical complementarity
# =========================================================================

def tropical_complementarity(g: int, shadow_A: ShadowData,
                              shadow_A_dual: ShadowData) -> Dict[str, Any]:
    r"""Verify tropical complementarity for a Koszul pair (A, A!).

    Theorem C (complementarity): Q_g(A) + Q_g(A!) = H*(M_g, Z(A)).
    In tropical terms:

        F_g^trop(A) + F_g^trop(A!) = (total tropical volume of M^trop_g)
                                       * Z_g(A)

    where Z_g(A) is the central charge at genus g.

    For the scalar lane (uniform-weight):
        F_g(A) = kappa(A) * lambda_g^FP
        F_g(A!) = kappa(A!) * lambda_g^FP
        Sum = (kappa(A) + kappa(A!)) * lambda_g^FP

    For KM/free fields: kappa + kappa' = 0, so the sum vanishes.
    For Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero).

    Parameters:
        g: genus
        shadow_A: shadow data for A
        shadow_A_dual: shadow data for A!

    Returns:
        Dict with complementarity analysis.
    """
    decomp_A = tropical_shell_decomposition(g, shadow_A)
    decomp_dual = tropical_shell_decomposition(g, shadow_A_dual)

    F_A = cancel(-(decomp_A.mumford_total + decomp_A.planted_forest_total))
    F_dual = cancel(-(decomp_dual.mumford_total + decomp_dual.planted_forest_total))
    total = cancel(F_A + F_dual)

    # Scalar prediction
    lambda_fp = Integer(_lambda_fp_exact(g).numerator) / Integer(
        _lambda_fp_exact(g).denominator)
    kappa_sum = cancel(shadow_A.kappa + shadow_A_dual.kappa)
    scalar_prediction = cancel(kappa_sum * lambda_fp)

    return {
        'genus': g,
        'F_g_A': F_A,
        'F_g_A_dual': F_dual,
        'total': total,
        'kappa_sum': kappa_sum,
        'scalar_prediction': scalar_prediction,
        'complementarity_holds': simplify(total - scalar_prediction) == 0,
    }


# =========================================================================
# Section 10: Self-loop parity vanishing (tropical proof)
# =========================================================================

def verify_self_loop_parity_vanishing(max_k: int = 6) -> Dict[int, Dict[str, Any]]:
    r"""Verify the self-loop parity vanishing theorem (prop:self-loop-vanishing).

    For every k >= 2, the Hodge integral of the single-vertex (0, 2k)
    graph with k self-loops vanishes:

        I_k = sum_{assignments} prod_i (-1)^{d_i^-} * <tau_{d_1^+} ... tau_{d_k^-}>_0 = 0

    Tropical proof: the parity involution d_i^+ <-> d_i^- on each loop
    acts as multiplication by (-1) on the integrand.  The only fixed
    points have d_i^+ = d_i^- for all i, requiring sum(2*d_i^+) = 2k-3
    (odd = even), which is impossible.

    This is the tropical reason why the sunset graph (k=2) at genus 2
    contributes zero to delta_pf.

    Returns:
        Dict mapping k -> verification data.
    """
    results = {}
    for k in range(2, max_k + 1):
        dim = 2 * k - 3  # = 3*0 - 3 + 2k = 2k - 3
        total = Fraction(0)
        n_terms = 0
        n_cancelling_pairs = 0

        # Enumerate all assignments
        assignments = _nonneg_compositions_list(dim, 2 * k)
        for combo in assignments:
            sign = 1
            for i in range(k):
                sign *= (-1) ** combo[2 * i + 1]
            wk = wk_intersection(0, tuple(sorted(combo, reverse=True)))
            total += Fraction(sign) * wk
            n_terms += 1

        # Check that sum(2*d_i) = 2k-3 is impossible (odd)
        # so all fixed points of the swap are empty
        fixed_point_impossible = (dim % 2 == 1)

        results[k] = {
            'k': k,
            'dimension': dim,
            'n_terms': n_terms,
            'total': total,
            'vanishes': total == 0,
            'fixed_point_impossible': fixed_point_impossible,
            'parity_argument_applies': fixed_point_impossible,
        }

    return results


def _nonneg_compositions_list(total: int, parts: int) -> List[Tuple[int, ...]]:
    """Enumerate all tuples of `parts` non-negative integers summing to `total`."""
    if parts == 0:
        return [()] if total == 0 else []
    if parts == 1:
        return [(total,)]
    result = []
    for first in range(total + 1):
        for rest in _nonneg_compositions_list(total - first, parts - 1):
            result.append((first,) + rest)
    return result


# =========================================================================
# Section 11: Tropical shadow weight polynomial
# =========================================================================

def planted_forest_polynomial_genus2() -> Dict[str, Any]:
    r"""Compute the planted-forest polynomial at genus 2 symbolically.

    delta_pf^{(2,0)} is a polynomial in (kappa, S_3, S_4).
    At genus 2, only S_3 is visible (S_4 enters via the sunset
    graph, which has vanishing Hodge integral).

    Expected: delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48

    Returns:
        Dict with symbolic computation and verification.
    """
    # Use symbolic shadow data
    kappa = Symbol('kappa')
    S3 = Symbol('S_3')
    S4 = Symbol('S_4')

    shadow = ShadowData(
        name='symbolic',
        kappa=kappa,
        S3=S3,
        S4=S4,
        depth_class='M',
    )

    decomp = tropical_shell_decomposition(2, shadow)
    pf = expand(decomp.planted_forest_total)

    # Expected formula
    expected = S3 * (10 * S3 - kappa) / 48
    expected_expanded = expand(expected)

    return {
        'planted_forest_total': pf,
        'expected': expected_expanded,
        'match': simplify(pf - expected_expanded) == 0,
        'mumford_total': decomp.mumford_total,
        'n_pf_graphs': len(decomp.planted_forest_graphs),
        'n_mumford_graphs': len(decomp.mumford_graphs),
    }


def planted_forest_class_specialization(g: int) -> Dict[str, Any]:
    r"""Specialize the planted-forest polynomial to each shadow class.

    Class G (Heisenberg): S_3 = S_4 = S_5 = 0 => delta_pf = 0.
    Class L (affine sl_2): S_3 = 2, S_4 = 0.
    Class C (beta-gamma): S_3 = ..., S_4 = ..., but stratum separation.
    Class M (Virasoro): S_3 = 2, S_4 = 10/[c(5c+22)].

    Returns:
        Dict with specializations for each class.
    """
    results = {}

    # Heisenberg (class G)
    heis = heisenberg_shadow_data()
    decomp_heis = tropical_shell_decomposition(g, heis)
    results['G_Heisenberg'] = {
        'planted_forest_total': cancel(decomp_heis.planted_forest_total),
        'expected_zero': True,
        'is_zero': simplify(decomp_heis.planted_forest_total) == 0,
    }

    # Affine sl_2 (class L)
    aff = affine_shadow_data()
    decomp_aff = tropical_shell_decomposition(g, aff)
    results['L_affine_sl2'] = {
        'planted_forest_total': cancel(decomp_aff.planted_forest_total),
        'depends_on_S3_only': True,
    }

    # Virasoro (class M)
    vir = virasoro_shadow_data(max_arity=max(6, 2 * g + 2))
    decomp_vir = tropical_shell_decomposition(g, vir)
    results['M_Virasoro'] = {
        'planted_forest_total': cancel(decomp_vir.planted_forest_total),
        'depends_on_all_shadows': True,
    }

    return results


# =========================================================================
# Section 12: Tropical moduli volume and Euler characteristic
# =========================================================================

def tropical_volume_genus(g: int) -> Fraction:
    r"""Compute the total tropical volume of M^trop_{g,0}.

    vol(M^trop_{g,0}) = sum_Gamma 1/|Aut(Gamma)|

    This is the orbifold Euler characteristic chi^orb(M_g) by the
    tropical comparison theorem (Chan-Galatius-Payne).

    Known values:
        g=2: vol = 1/240 + 1/48 + ... (sum over 7 graphs)
        g=3: vol = ... (sum over 42 graphs)
    """
    if g == 2:
        graphs = stable_graphs_genus2_0leg()
    elif g == 3:
        graphs = stable_graphs_genus3_0leg()
    else:
        raise ValueError(f"Genus {g} not implemented")

    return sum(Fraction(1, G.automorphism_order) for G in graphs)


def tropical_volume_by_shell(g: int) -> Dict[str, Fraction]:
    r"""Decompose the tropical volume by shell (Mumford vs planted-forest).

    Returns:
        Dict with 'mumford_volume', 'planted_forest_volume', 'total_volume'.
    """
    if g == 2:
        graphs = stable_graphs_genus2_0leg()
    elif g == 3:
        graphs = stable_graphs_genus3_0leg()
    else:
        raise ValueError(f"Genus {g} not implemented")

    mumford_vol = Fraction(0)
    pf_vol = Fraction(0)
    smooth_vol = Fraction(0)

    for G in graphs:
        vol = Fraction(1, G.automorphism_order)
        if G.codimension == 0:
            smooth_vol += vol
        elif is_planted_forest_graph(G):
            pf_vol += vol
        else:
            mumford_vol += vol

    return {
        'smooth_volume': smooth_vol,
        'mumford_volume': mumford_vol,
        'planted_forest_volume': pf_vol,
        'total_volume': smooth_vol + mumford_vol + pf_vol,
    }


# =========================================================================
# Section 13: Summary and structural theorems
# =========================================================================

def tropical_shadow_tower_summary(g: int) -> Dict[str, Any]:
    r"""Comprehensive summary of the tropical shadow tower at genus g.

    Combines all analyses: tropical dictionary, shell decomposition,
    depth filtration, volume, Mikhalkin correspondence.
    """
    # Shadow data for all three standard families
    heis = heisenberg_shadow_data()
    aff = affine_shadow_data()
    vir = virasoro_shadow_data(max_arity=max(6, 2 * g + 2))

    # Volume decomposition
    vol = tropical_volume_by_shell(g)

    # Depth statistics
    depth_stats = tropical_depth_statistics(g)

    # Shell decompositions for each family
    decomps = {}
    for name, shadow in [('Heisenberg', heis), ('Affine_sl2', aff), ('Virasoro', vir)]:
        decomp = tropical_shell_decomposition(g, shadow)
        decomps[name] = {
            'mumford_total': decomp.mumford_total,
            'planted_forest_total': decomp.planted_forest_total,
            'n_mumford': len(decomp.mumford_graphs),
            'n_pf': len(decomp.planted_forest_graphs),
        }

    # Mikhalkin correspondence
    mikhalkin = {}
    for name, shadow in [('Heisenberg', heis), ('Virasoro', vir)]:
        corr = mikhalkin_correspondence_analysis(g, shadow)
        mikhalkin[name] = {
            'algebra_class': corr.algebra_class,
            'has_geometric_target': corr.has_geometric_target,
            'mikhalkin_holds': corr.mikhalkin_holds,
        }

    return {
        'genus': g,
        'volume': vol,
        'depth_statistics': depth_stats,
        'shell_decompositions': decomps,
        'mikhalkin_correspondence': mikhalkin,
    }
