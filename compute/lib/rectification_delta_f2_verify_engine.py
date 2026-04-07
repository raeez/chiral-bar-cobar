r"""Independent verification engine for delta_F_2^{grav}(W_N).

ADVERSARIAL RED-TEAM VERIFICATION of the claim:

    delta_F_2^{grav}(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)

This engine is built FROM SCRATCH with ZERO imports from the multi-weight
cross-channel engine. Every computation is independent.

MATHEMATICAL SETUP
==================

The genus-2 stable graph sum for the gravitational-only W_N Frobenius
algebra computes:

    F_2(W_N, c) = sum_{Gamma} (1/|Aut(Gamma)|)
                  * sum_{sigma: E(Gamma) -> {2,3,...,N}} A(Gamma, sigma)

where A(Gamma, sigma) is the product of:
  - Propagators: prod_e  w(sigma(e)) / c   where w(j) = conformal weight j
  - Vertex factors: prod_v V_{g(v)}(channels_at_v; c)

The diagonal part (all channels identical) gives kappa(W_N) * lambda_2^FP.
The cross-channel part (mixed channels) is delta_F_2^cross.

For the GRAVITATIONAL-ONLY Frobenius algebra:
  - Channels: T (weight 2), W_3 (weight 3), ..., W_N (weight N)
  - 3-point: C_{T,T,T} = c;  C_{T,W_j,W_j} = c;  all others = 0
  - Propagator: eta^{jj} = j/c   (inverse metric, from AP27)
  - Higher-genus vertex: V_{g,n}(j,j,...,j) = (c/j)*lambda_g^FP
  - Higher-genus mixed vertex: V_{g,n}(j1,...) = 0 if channels not all same

The 7 genus-2 stable graphs of M_bar_{2,0}:

Graph 0 (smooth):       1 vertex, genus 2, 0 edges, |Aut| = 1
Graph 1 (figure-eight): 1 vertex, genus 1, val 2, 1 self-loop, |Aut| = 2
Graph 2 (banana):       1 vertex, genus 0, val 4, 2 self-loops, |Aut| = 8
Graph 3 (dumbbell):     2 vertices, genus (1,1), 1 bridge, |Aut| = 2
Graph 4 (theta):        2 vertices, genus (0,0), val (3,3), 3 bridges, |Aut| = 12
Graph 5 (lollipop):     2 vertices, genus (0,1)+(1,1), 1 self-loop + 1 bridge, |Aut| = 2
Graph 6 (barbell):      2 vertices, genus (0,0), 2 self-loops + 1 bridge, |Aut| = 8

CORRECTNESS VERIFICATION:
  h^1 + sum(g_v) = 2 for all graphs (genus-2 constraint).
  2*g_v + val_v >= 3 for all vertices (stability).

References:
    thm:multi-weight-genus-expansion, AP27, Faber-Pandharipande
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product as cartprod
from math import comb, factorial, gcd
from typing import Dict, List, NamedTuple, Optional, Tuple


# ============================================================================
# Bernoulli numbers (independent implementation via recurrence)
# ============================================================================

def bernoulli_number(n: int) -> Fraction:
    """Exact Bernoulli number B_n via Akiyama-Tanigawa algorithm."""
    if n < 0:
        raise ValueError(f"Bernoulli number requires n >= 0, got {n}")
    # Use the standard recurrence
    a = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        a[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


def lambda_fp_independent(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number (independent computation).

    lambda_g^FP = int_{M_bar_{g,0}} lambda_g
               = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

    Verified values:
      g=1: 1/24
      g=2: 7/5760
      g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_FP requires g >= 1, got {g}")
    B2g = bernoulli_number(2 * g)
    abs_B2g = abs(B2g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs_B2g / Fraction(factorial(2 * g))


# ============================================================================
# Genus-2 stable graph data (hardcoded, independent enumeration)
# ============================================================================

class Genus2Graph(NamedTuple):
    """A genus-2 stable graph with n=0 marked points."""
    name: str
    vertex_genera: Tuple[int, ...]
    edges: Tuple[Tuple[int, int], ...]  # (v1, v2), v1 <= v2 for self-loops
    automorphism_order: int

    @property
    def num_vertices(self) -> int:
        return len(self.vertex_genera)

    @property
    def num_edges(self) -> int:
        return len(self.edges)

    @property
    def first_betti(self) -> int:
        # For connected graphs: h^1 = |E| - |V| + 1
        return self.num_edges - self.num_vertices + 1

    @property
    def arithmetic_genus(self) -> int:
        return self.first_betti + sum(self.vertex_genera)

    def valence(self) -> Tuple[int, ...]:
        val = [0] * self.num_vertices
        for v1, v2 in self.edges:
            if v1 == v2:
                val[v1] += 2
            else:
                val[v1] += 1
                val[v2] += 1
        return tuple(val)

    @property
    def is_stable(self) -> bool:
        val = self.valence()
        for v in range(self.num_vertices):
            if 2 * self.vertex_genera[v] - 2 + val[v] <= 0:
                return False
        return True


def genus2_stable_graphs_independent() -> List[Genus2Graph]:
    """The 7 stable graphs of M_bar_{2,0}, enumerated independently.

    Enumeration by number of vertices:

    1-vertex graphs (loop genus = edges - 1 + 1 = edges):
      - smooth: genus 2, 0 edges (loop genus 0, vertex genus 2)
        Stability: 2*2 + 0 = 4 >= 3. OK.
      - figure-eight: genus 1, 1 self-loop (loop genus 1, vertex genus 1)
        val = 2. Stability: 2*1 + 2 = 4 >= 3. OK.
      - banana (double self-loop): genus 0, 2 self-loops (loop genus 2)
        val = 4. Stability: 2*0 + 4 = 4 >= 3. OK.

    2-vertex graphs (loop genus = edges - 2 + 1 = edges - 1):
      - dumbbell: genera (1,1), 1 bridge (loop genus 0)
        vals = (1,1). Stability: 2*1+1=3 >= 3, 2*1+1=3 >= 3. OK.
      - theta: genera (0,0), 3 bridges (loop genus 2)
        vals = (3,3). Stability: 2*0+3=3 >= 3. OK.
      - lollipop: genera (0,1) or (1,0), 1 self-loop on genus-0 vertex + 1 bridge
        Say vertex 0 has genus 0, self-loop, and bridge -> val=3.
        Vertex 1 has genus 1, one bridge end -> val=1.
        Stability: 2*0+3=3 >= 3, 2*1+1=3 >= 3. OK.
        Loop genus = 2 - 1 = 1, plus self-loop gives h^1 = 2-2+1 = 1.
        Arithmetic genus = 1 + 0 + 1 = 2. OK.
      - barbell: genera (0,0), 2 self-loops (one on each vertex) + 1 bridge
        Vertex 0: self-loop + bridge -> val = 3. Stability: 0+3 = 3 >= 3. OK.
        Vertex 1: self-loop + bridge -> val = 3. Stability: 0+3 = 3 >= 3. OK.
        h^1 = 3 - 2 + 1 = 2. Arithmetic genus = 2 + 0 + 0 = 2. OK.

    3-vertex or more: Not possible at genus 2 with n=0 and stability.
      - 3 vertices with genera (0,0,0): need h^1 = 2, so |E| = 2-0+3-1 = 4 edges.
        Each vertex needs val >= 3. Min total valence = 9. Each edge contributes 2
        to total valence (non-self-loops) or 2 (self-loops). With 4 edges:
        max total valence = 8 < 9. Impossible.
      - 3 vertices with genera (1,0,0): h^1 = 1, |E| = 3. Min val: 1+3+3 = 7.
        Max from 3 edges: 6 < 7. Impossible.
      - 3 vertices with genera (0,1,0): same analysis, impossible.

    So exactly 7 graphs.

    Automorphism groups (computed by hand):
      - smooth: trivial, |Aut| = 1
      - figure-eight: self-loop can be flipped, |Aut| = 2
      - banana: S_2 for each self-loop * S_2 swapping the two loops = 2*2*2 = 8
        Wait: more carefully. Two self-loops share a vertex. An automorphism
        can swap the two loops (giving factor 2) and flip each loop (giving 2*2).
        Total: 2 * 2 * 2 = 8. But half-edge permutations: 2 half-edges per loop,
        so 4 half-edges total. Aut = {id, swap_loops, flip_loop1, flip_loop2,
        swap+flip1, swap+flip2, swap+flip_both, flip_both} = D_4 has order 8.
      - dumbbell: swap the two vertices (and their loops), |Aut| = 2
      - theta: S_3 on the 3 bridges * Z/2 swapping vertices = 6 * 2 = 12.
        Actually: S_3 permutes the 3 parallel edges, and swapping the vertices
        is compatible with each permutation. |Aut| = 12.
      - lollipop: the self-loop on vertex 0 can be flipped, |Aut| = 2.
        Swapping vertices is NOT possible (different genera).
      - barbell: swap the two vertices (and their self-loops) * flip each self-loop.
        Total: 2 (swap) * 2 (flip loop 0) * 2 (flip loop 1) = 8.
        But vertex swap and independent flips: |Aut| = 8.
    """
    return [
        Genus2Graph(
            name='smooth',
            vertex_genera=(2,),
            edges=(),
            automorphism_order=1,
        ),
        Genus2Graph(
            name='figure_eight',
            vertex_genera=(1,),
            edges=((0, 0),),
            automorphism_order=2,
        ),
        Genus2Graph(
            name='banana',
            vertex_genera=(0,),
            edges=((0, 0), (0, 0)),
            automorphism_order=8,
        ),
        Genus2Graph(
            name='dumbbell',
            vertex_genera=(1, 1),
            edges=((0, 1),),
            automorphism_order=2,
        ),
        Genus2Graph(
            name='theta',
            vertex_genera=(0, 0),
            edges=((0, 1), (0, 1), (0, 1)),
            automorphism_order=12,
        ),
        Genus2Graph(
            name='lollipop',
            vertex_genera=(0, 1),
            edges=((0, 0), (0, 1)),
            automorphism_order=2,
        ),
        Genus2Graph(
            name='barbell',
            vertex_genera=(0, 0),
            edges=((0, 0), (0, 1), (1, 1)),
            automorphism_order=8,
        ),
    ]


# ============================================================================
# Gravitational Frobenius algebra for W_N
# ============================================================================

def grav_C3(i: int, j: int, k: int, c: Fraction) -> Fraction:
    """Gravitational 3-point structure constant C^{grav}_{ijk}.

    Channels are labeled by conformal weights: i, j, k in {2, 3, ..., N}.
    Weight 2 = stress tensor T.

    Parity selection rule: channels with odd conformal weight (3, 5, 7, ...)
    carry Z_2 parity. The total number of odd-weight channels at each vertex
    must be EVEN.

    Non-vanishing gravitational 3-point couplings:
      C_{2,2,2} = c        (TTT)
      C_{2,j,j} = c        (T W_j W_j) for any j >= 3
      C_{2,2,j} = 0        for j >= 3 (T x T OPE does not produce W_j primaries)

    All couplings with three distinct non-T channels vanish in the
    gravitational approximation (no higher-spin exchange).

    Args:
        i, j, k: conformal weights (integers >= 2)
        c: central charge (Fraction)

    Returns:
        C^{grav}_{ijk} as Fraction
    """
    # Parity check: count odd-weight channels
    odd_count = sum(1 for w in [i, j, k] if w % 2 == 1)
    if odd_count % 2 == 1:
        return Fraction(0)

    # Sort for canonical form
    triple = tuple(sorted([i, j, k]))

    # TTT
    if triple == (2, 2, 2):
        return c

    # T W_j W_j (exactly one 2, and the other two match)
    if triple[0] == 2 and triple[1] == triple[2] and triple[1] >= 3:
        return c

    # T T W_j: the stress tensor OPE T(z)T(w) produces only T (and descendants),
    # not higher-spin primaries W_j for j >= 3. So C_{2,2,j} = 0 for j >= 3.
    # (Even if parity allows it for even j.)
    if triple[0] == 2 and triple[1] == 2 and triple[2] >= 3:
        return Fraction(0)

    # All other triples: 0 in gravitational approximation
    # (no W_j x W_k -> W_l exchange without specific OPE couplings)
    return Fraction(0)


def grav_propagator(weight: int, c: Fraction) -> Fraction:
    """Inverse metric eta^{jj} = j/c.

    The bar propagator d log E(z,w) has weight 1 in both variables (AP27).
    The metric on the weight-j channel is eta_{jj} = c/j.
    The propagator (inverse metric) is eta^{jj} = j/c.
    """
    return Fraction(weight, 1) / c


def grav_kappa_channel(weight: int, c: Fraction) -> Fraction:
    """Per-channel modular characteristic kappa_j = c/j."""
    return c / Fraction(weight)


def grav_kappa_total(N: int, c: Fraction) -> Fraction:
    """Total kappa(W_N) = sum_{j=2}^{N} c/j = c * (H_N - 1)."""
    return sum(c / Fraction(j) for j in range(2, N + 1))


# ============================================================================
# Vertex factors
# ============================================================================

def grav_V0_factorize(channels: Tuple[int, ...], c: Fraction,
                      all_weights: Tuple[int, ...]) -> Fraction:
    r"""Genus-0 n-point vertex factor via recursive factorization.

    V_0(a, b, rest...) = sum_m eta^{mm} * C_{a,b,m} * V_0(m, rest...)

    Base case n=3: V_0(a,b,c) = C_{abc}.

    The sum over intermediate channels m runs over all weights in all_weights.
    """
    n = len(channels)
    if n < 3:
        raise ValueError(f"Genus-0 vertex needs n >= 3, got {n}")
    if n == 3:
        return grav_C3(channels[0], channels[1], channels[2], c)

    a, b = channels[0], channels[1]
    rest = channels[2:]
    total = Fraction(0)
    for m in all_weights:
        c3 = grav_C3(a, b, m, c)
        if c3 == 0:
            continue
        sub_val = grav_V0_factorize((m,) + rest, c, all_weights)
        if sub_val == 0:
            continue
        total += grav_propagator(m, c) * c3 * sub_val
    return total


def grav_vertex_factor(gv: int, channels: Tuple[int, ...], c: Fraction,
                       all_weights: Tuple[int, ...]) -> Fraction:
    """Vertex factor V_{g,n}(channels).

    g >= 1: diagonal principle. All channels must be identical.
      V_{g,n}(j,...,j) = kappa_j * lambda_g^FP = (c/j) * lambda_g
      V_{g,n}(mixed) = 0

    g = 0: recursive Frobenius factorization.
    """
    n = len(channels)
    if n == 0:
        return Fraction(0)

    if gv == 0:
        if n < 3:
            raise ValueError(f"Genus-0 vertex needs n >= 3, got {n}")
        return grav_V0_factorize(channels, c, all_weights)
    else:
        # Higher genus: diagonal
        if len(set(channels)) > 1:
            return Fraction(0)
        return grav_kappa_channel(channels[0], c) * lambda_fp_independent(gv)


# ============================================================================
# Graph amplitude computation
# ============================================================================

def half_edge_channels(graph: Genus2Graph, sigma: Tuple[int, ...]
                       ) -> List[Tuple[int, ...]]:
    """Compute per-vertex half-edge channel assignments.

    For each edge (v1, v2):
      - If v1 == v2 (self-loop): two half-edges at v1, both with sigma[e]
      - If v1 != v2 (bridge): one half-edge at v1, one at v2, both sigma[e]
    """
    nv = graph.num_vertices
    he: List[List[int]] = [[] for _ in range(nv)]

    for e_idx, (v1, v2) in enumerate(graph.edges):
        ch = sigma[e_idx]
        if v1 == v2:
            he[v1].append(ch)
            he[v1].append(ch)
        else:
            he[v1].append(ch)
            he[v2].append(ch)

    return [tuple(he[v]) for v in range(nv)]


def graph_amplitude_raw(graph: Genus2Graph, sigma: Tuple[int, ...],
                        c: Fraction, all_weights: Tuple[int, ...]) -> Fraction:
    """Raw amplitude A(Gamma, sigma) WITHOUT the 1/|Aut| factor.

    = prod_e eta^{sigma(e)} * prod_v V_{g(v)}(he_channels_at_v)
    """
    ne = graph.num_edges
    if ne == 0:
        return Fraction(0)

    he_chs = half_edge_channels(graph, sigma)

    # Propagator product
    prop = Fraction(1)
    for e_idx in range(ne):
        prop *= grav_propagator(sigma[e_idx], c)

    # Vertex factors
    vf = Fraction(1)
    for v_idx in range(graph.num_vertices):
        gv = graph.vertex_genera[v_idx]
        chs = he_chs[v_idx]
        if len(chs) == 0:
            continue
        vf_v = grav_vertex_factor(gv, chs, c, all_weights)
        if vf_v == 0:
            return Fraction(0)
        vf *= vf_v

    return prop * vf


def graph_amplitude_decomposed(graph: Genus2Graph, c: Fraction,
                               all_weights: Tuple[int, ...]
                               ) -> Dict[str, Fraction]:
    """Sum amplitude over all channel assignments, split into diagonal/mixed.

    Divides by |Aut(Gamma)|.
    """
    ne = graph.num_edges
    if ne == 0:
        return {'diagonal': Fraction(0), 'mixed': Fraction(0),
                'total': Fraction(0)}

    aut = graph.automorphism_order
    diag = Fraction(0)
    mixed = Fraction(0)

    for sigma in cartprod(all_weights, repeat=ne):
        amp = graph_amplitude_raw(graph, sigma, c, all_weights)
        if amp == 0:
            continue
        if len(set(sigma)) <= 1:
            diag += amp
        else:
            mixed += amp

    return {
        'diagonal': diag / aut,
        'mixed': mixed / aut,
        'total': (diag + mixed) / aut,
    }


# ============================================================================
# Full genus-2 cross-channel correction
# ============================================================================

def delta_F2_grav_graph_sum(N: int, c: Fraction) -> Fraction:
    """Compute delta_F_2^{grav}(W_N, c) by summing over all 7 genus-2 graphs.

    This is the MIXED (cross-channel) part of the genus-2 free energy,
    using the gravitational-only Frobenius algebra.
    """
    all_weights = tuple(range(2, N + 1))
    graphs = genus2_stable_graphs_independent()

    total_mixed = Fraction(0)
    for graph in graphs:
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        total_mixed += decomp['mixed']

    return total_mixed


def delta_F2_grav_per_graph(N: int, c: Fraction) -> Dict[str, Dict[str, Fraction]]:
    """Per-graph decomposition of delta_F_2^{grav}(W_N, c)."""
    all_weights = tuple(range(2, N + 1))
    graphs = genus2_stable_graphs_independent()

    result = {}
    for graph in graphs:
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        result[graph.name] = decomp

    return result


# ============================================================================
# The claimed N-formula (to be verified)
# ============================================================================

def claimed_B(N: int) -> Fraction:
    """Claimed: B(N) = (N-2)(N+3)/96."""
    return Fraction((N - 2) * (N + 3), 96)


def claimed_A(N: int) -> Fraction:
    """Claimed: A(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24."""
    return Fraction((N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33), 24)


def claimed_formula(N: int, c: Fraction) -> Fraction:
    """Claimed: delta_F_2^{grav}(W_N, c) = B(N) + A(N)/c."""
    return claimed_B(N) + claimed_A(N) / c


# ============================================================================
# Alternative formula derivation via graph-by-graph analysis
# ============================================================================

def kappa_total_independent(N: int, c: Fraction) -> Fraction:
    """kappa(W_N) = c * (H_N - 1) = c * sum_{j=2}^N 1/j."""
    return sum(c / Fraction(j) for j in range(2, N + 1))


def harmonic_minus_one_independent(N: int) -> Fraction:
    """H_N - 1 = sum_{j=2}^N 1/j."""
    return sum(Fraction(1, j) for j in range(2, N + 1))


def sum_inverse_squares(N: int) -> Fraction:
    """sum_{j=2}^N 1/j^2."""
    return sum(Fraction(1, j * j) for j in range(2, N + 1))


def sum_inverse_cubes(N: int) -> Fraction:
    """sum_{j=2}^N 1/j^3."""
    return sum(Fraction(1, j * j * j) for j in range(2, N + 1))


def harmonic_sum(N: int, power: int) -> Fraction:
    """sum_{j=2}^N 1/j^power."""
    return sum(Fraction(1, j**power) for j in range(2, N + 1))


# ============================================================================
# Algebraic derivation: express graph amplitudes in terms of harmonic sums
# ============================================================================

def derive_graph_amplitudes_symbolic(N: int, c: Fraction) -> Dict[str, Fraction]:
    """Compute each graph's mixed amplitude using explicit harmonic sums.

    This provides an ALGEBRAIC verification path: the amplitudes should
    be expressible in terms of harmonic sums H^{(k)}_N = sum_{j=2}^N 1/j^k.

    Let H1 = H_N - 1 = sum 1/j, H2 = sum 1/j^2, H3 = sum 1/j^3.
    Let lambda = lambda_2^FP = 7/5760.

    Graph-by-graph analysis of the gravitational-only amplitude:
    (derived independently below)
    """
    H1 = harmonic_minus_one_independent(N)
    H2 = sum_inverse_squares(N)
    H3 = sum_inverse_cubes(N)
    lam2 = lambda_fp_independent(2)  # 7/5760
    lam1 = lambda_fp_independent(1)  # 1/24

    # --- Graph 0: smooth ---
    # 1 vertex, genus 2, 0 edges. No amplitude. Mixed = 0.
    smooth = Fraction(0)

    # --- Graph 1: figure-eight ---
    # 1 vertex (genus 1), 1 self-loop, |Aut| = 2.
    # sigma = (j) for some weight j.
    # Amplitude = propagator(j) * V_{1,2}(j,j)
    #           = (j/c) * (c/j) * lambda_1
    #           = lambda_1 = 1/24.
    # This is the SAME for all j. So diagonal sum = (N-1) * (1/24),
    # but there are no "mixed" assignments since there's only 1 edge.
    # Mixed = 0 for figure-eight.
    figure_eight = Fraction(0)

    # --- Graph 2: banana ---
    # 1 vertex (genus 0), 2 self-loops, |Aut| = 8.
    # sigma = (j1, j2) for weights j1, j2.
    # Amplitude = prop(j1)*prop(j2) * V_{0,4}(j1,j1,j2,j2)
    # V_{0,4}(a,a,b,b) = sum_m eta^{mm} * C_{a,a,m} * C_{m,b,b}
    # In the gravitational Frobenius algebra:
    #   C_{a,a,m} is nonzero only when m=2 (T channel) and a can be anything,
    #   OR when m=a and a=2.
    #   Wait: C_{j,j,m} = c if m=2 (by C_{T,W_j,W_j} = c, using T=2).
    #   And C_{j,j,m} = c if m=j and j=2 (TTT = c).
    #   Hmm, but what about C_{j,j,j} for j >= 3? In the gravitational
    #   approximation, C_{j,j,j} = 0 for j >= 3 (requires higher-spin exchange).
    #   WAIT: Actually, C_{j,j,2} = c (this is C_{T,W_j,W_j} by symmetry).
    #   And C_{2,2,2} = c. So C_{j,j,m} = c when m = 2, for ALL j.
    #   And C_{j,j,m} = 0 for m != 2 (in the gravitational approximation),
    #   EXCEPT C_{2,2,2} = c which is already covered by m=2.
    #
    # So V_{0,4}(a,a,b,b) = eta^{22} * C_{a,a,2} * C_{2,b,b}
    #                      = (2/c) * c * c = 2c.
    #
    # This holds for ALL (a,b), not just a=b. So:
    # A(banana, (j1,j2)) = (j1/c)*(j2/c) * 2c = 2*j1*j2/c.
    #
    # Diagonal: sum_{j} 2*j^2/c. Mixed: sum_{j1 != j2} 2*j1*j2/c.
    # Total: sum_{j1,j2} 2*j1*j2/c = 2*(sum j)^2/c.
    # Diagonal: 2*(sum j^2)/c.
    # Mixed: 2*((sum j)^2 - sum j^2)/c = 2*((c*H1)^2 - ...).
    # Wait, sum_{j=2}^N j = N(N+1)/2 - 1. Let S1 = sum j = N(N+1)/2 - 1.
    # And sum j^2 = N(N+1)(2N+1)/6 - 1. Let S2 = sum j^2.
    #
    # Total amplitude (before /|Aut|): sum_{j1,j2} 2*j1*j2/c = 2*S1^2/c.
    # Diagonal: 2*S2/c. Mixed: 2*(S1^2 - S2)/c.
    # After /|Aut| = /8: mixed_banana = (S1^2 - S2)/(4c).

    S1 = sum(j for j in range(2, N + 1))
    S2 = sum(j * j for j in range(2, N + 1))
    banana_mixed = Fraction(S1 * S1 - S2, 4) / c

    # --- Graph 3: dumbbell ---
    # 2 vertices (genus 1, 1), 1 bridge (0->1), |Aut| = 2.
    # sigma = (j) for weight j.
    # A = prop(j) * V_{1,1}(j) * V_{1,1}(j) = (j/c) * (c/j * lam1)^2
    #   = (j/c) * c^2/(j^2) * lam1^2 = c * lam1^2 / j.
    # This depends on j.
    # Diagonal: sum_j c*lam1^2/j = c*lam1^2*H1. Per channel: c*lam1^2/j.
    # Only 1 edge, so no mixed assignments. Mixed = 0.
    dumbbell_mixed = Fraction(0)

    # --- Graph 4: theta ---
    # 2 vertices (genus 0, 0), 3 bridges, all (0->1), |Aut| = 12.
    # sigma = (j1, j2, j3) for weights j1, j2, j3.
    # At vertex 0: half-edges j1, j2, j3. V_{0,3}(j1,j2,j3) = C_{j1,j2,j3}.
    # At vertex 1: half-edges j1, j2, j3. V_{0,3}(j1,j2,j3) = C_{j1,j2,j3}.
    # A = prop(j1)*prop(j2)*prop(j3) * C_{j1,j2,j3}^2.
    #
    # Non-vanishing gravitational C_{j1,j2,j3}:
    #   (2,2,2) -> c
    #   (2,j,j) for j>=3 -> c (parity-allowed)
    #
    # So sigma must be one of:
    #   (2,2,2): A = (2/c)^3 * c^2 = 8c^2/c^3 = 8/c.
    #   Permutations of (2,j,j) for j>=3: A = (2/c)*(j/c)*(j/c) * c^2
    #     = 2*j^2*c^2/c^3 = 2*j^2/c.
    #     Number of permutations: 3 (the 2 can be in any of 3 positions).
    #
    # Let's enumerate more carefully.
    # sigma is an ordered triple. Non-vanishing configs:
    #   (2,2,2): 1 assignment.
    #   Perms of (2,j,j) for each j>=3: 3 assignments per j.
    #     But parity: j must have even total odd count at each vertex.
    #     At each vertex, half-edges are (j1,j2,j3). The odd count is the
    #     number of odd j_k among j1,j2,j3.
    #     For (2,j,j) where j is odd (j=3,5,...): odd count = 2 (even). OK.
    #     For (2,j,j) where j is even (j=4,6,...): odd count = 0. OK.
    #   Perms of (j,j,k) with j,k >= 3, j!=k: need C_{j,j,k} != 0.
    #     C_{j,j,k} = 0 in gravitational approx (no higher-spin exchange) unless k=2.
    #     Since j >= 3 and k >= 3, these all vanish.
    #
    # Total for theta:
    # Diagonal: (2,2,2) -> A = 8/c. Permutations of (2,j,j) with j1=j2=j3=same:
    #   But (2,j,j) has DISTINCT channels (2 and j), so it's MIXED unless j=2.
    #   (2,2,2) is diagonal. (2,j,j) for j>=3 is mixed.
    #
    # Diagonal: only (2,2,2) -> A = 8/c. After /12: 8/(12c) = 2/(3c).
    # But wait, is there (j,j,j) for j>=3? C_{j,j,j} = 0 for j>=3 in grav.
    # So diagonal: just (2,2,2).
    #
    # Mixed: for each j >= 3, 3 permutations of (2,j,j), each with
    #   A = (2/c)*(j/c)^2 * c^2 = 2j^2/c.
    # Total mixed sum (before /|Aut|): sum_{j=3}^N 3 * 2*j^2/c = 6*(sum_{j=3}^N j^2)/c.
    # After /12: (sum_{j=3}^N j^2) / (2c).

    S2_from3 = sum(j * j for j in range(3, N + 1))  # sum j^2 for j=3..N
    theta_mixed = Fraction(S2_from3, 2) / c

    # --- Graph 5: lollipop ---
    # 2 vertices: vertex 0 (genus 0, self-loop + bridge, val=3),
    #             vertex 1 (genus 1, bridge, val=1).
    # Edges: (0,0) = self-loop, (0,1) = bridge. |Aut| = 2.
    # sigma = (j1, j2) where j1 = self-loop channel, j2 = bridge channel.
    #
    # At vertex 0: half-edges from self-loop (j1, j1) + bridge (j2) = (j1, j1, j2).
    #   V_{0,3}(j1, j1, j2) = C_{j1, j1, j2}.
    #   In gravitational: C_{j1,j1,j2} = c if j2 = 2 (T channel),
    #   AND additionally C_{2,2,2} = c.
    #   So: C_{j1,j1,j2} = c if j2=2 (regardless of j1), or if j1=2 and j2=2.
    #   Wait: C_{j,j,2} = c for ALL j (including j=2: C_{2,2,2} = c).
    #   And C_{j,j,k} = 0 for k >= 3 (gravitational approx).
    #   So the constraint is j2 = 2.
    #
    # At vertex 1: half-edge from bridge (j2).
    #   V_{1,1}(j2) = kappa_{j2} * lambda_1 = (c/j2) * (1/24).
    #
    # So sigma must have j2 = 2 (the bridge channel must be T).
    # A(lollipop, (j1, 2)) = prop(j1)*prop(2) * C_{j1,j1,2} * V_{1,1}(2)
    #   = (j1/c)*(2/c) * c * (c/2)*(1/24)
    #   = (j1/c)*(2/c) * c * c/(48)
    #   = j1 * 2 * c / (48 * c^2)
    #   Hmm, let me recompute more carefully.
    #   prop(j1) = j1/c, prop(2) = 2/c.
    #   V_{0,3}(j1,j1,2) = C_{j1,j1,2} = c.
    #   V_{1,1}(2) = (c/2) * lambda_1 = (c/2)*(1/24) = c/48.
    #   A = (j1/c)*(2/c) * c * (c/48) = 2*j1 * c / (48*c^2) = j1/(24c).
    #   Wait: (j1/c)*(2/c) = 2*j1/c^2. Times c = 2*j1/c. Times c/48 = 2*j1/(48) = j1/24.
    #   A = j1/24.
    #
    # This is INDEPENDENT OF c. Interesting.
    #
    # Diagonal: j1 = 2 (both edges have channel 2). A = 2/24 = 1/12.
    # Mixed: j1 != 2, j2 = 2. So j1 in {3,...,N}. A(j1) = j1/24.
    # Total mixed (before /|Aut|): sum_{j=3}^N j/24 = (S1-2)/24 where S1=sum_{j=2}^N j.
    # After /2: (S1-2)/48.
    #
    # Hmm wait. j2 MUST be 2 (bridge channel). j1 is the self-loop channel.
    # If j1 = j2 = 2: diagonal. If j1 != 2 and j2 = 2: we have two edges
    # with channels (j1, 2), which uses two DISTINCT channels -> mixed.
    # If j1 = 2, j2 = 2: channels (2, 2) -> one channel -> diagonal.
    # If j1 != 2, j2 != 2: then j2 >= 3, and V_{0,3} = C_{j1,j1,j2} = 0 (grav).
    # So only j2=2 contributes.

    S1_from3 = sum(j for j in range(3, N + 1))  # sum j for j=3..N
    lollipop_mixed = Fraction(S1_from3, 48)

    # --- Graph 6: barbell ---
    # 2 vertices (genus 0, 0), edges: (0,0), (0,1), (1,1). |Aut| = 8.
    # sigma = (j1, j2, j3) where j1 = self-loop on v0, j2 = bridge, j3 = self-loop on v1.
    #
    # At vertex 0: half-edges from self-loop (j1,j1) + bridge (j2) = (j1,j1,j2).
    #   V_{0,3}(j1,j1,j2) = C_{j1,j1,j2} = c if j2=2, else 0 (grav).
    #
    # At vertex 1: half-edges from bridge (j2) + self-loop (j3,j3) = (j2,j3,j3).
    #   V_{0,3}(j2,j3,j3) = C_{j2,j3,j3} = c if j2=2, else 0 (grav).
    #
    # So j2 = 2 is REQUIRED (bridge must carry T channel).
    # A(barbell, (j1, 2, j3)) = prop(j1)*prop(2)*prop(j3)
    #   * C_{j1,j1,2} * C_{2,j3,j3}
    #   = (j1/c)*(2/c)*(j3/c) * c * c
    #   = 2*j1*j3*c^2 / c^3 = 2*j1*j3/c.
    #
    # Diagonal: j1 = j2 = j3 all same channel. Since j2=2, need j1=j3=2.
    #   A = 2*2*2/c = 8/c.
    #   After /|Aut|=8: 1/c.
    # Mixed: j2=2, and not all edges same channel.
    #   If j1 = j3 = 2: diagonal (channels (2,2,2)).
    #   If j1 != 2 or j3 != 2: mixed (channels include 2 and something else).
    #   But wait: if j1 = j3 != 2 and j2 = 2: channels are (j1, 2, j1),
    #   which has two distinct channels -> mixed.
    #   If j1 != j3 and j2 = 2: channels (j1, 2, j3), three distinct if j1,j3 >= 3
    #   and j1 != j3 -> mixed. Two distinct if one of j1,j3 = 2 -> mixed.
    #
    # Mixed sum (before /|Aut|):
    #   sum_{(j1,j3) != (2,2)} 2*j1*j3/c
    #   = 2/c * (sum_{j1=2}^N sum_{j3=2}^N j1*j3 - 2*2)
    #   = 2/c * (S1^2 - 4)
    #   Actually: sum_all = sum_{j1} sum_{j3} 2*j1*j3/c = 2*S1^2/c.
    #   Diagonal = 2*2*2/c = 8/c.
    #   Mixed = 2*(S1^2 - 4)/c.
    #   After /8: (S1^2 - 4)/(4c).

    barbell_mixed = Fraction(S1 * S1 - 4, 4) / c

    return {
        'smooth': smooth,
        'figure_eight': figure_eight,
        'banana': banana_mixed,
        'dumbbell': dumbbell_mixed,
        'theta': theta_mixed,
        'lollipop': lollipop_mixed,
        'barbell': barbell_mixed,
    }


def delta_F2_grav_symbolic(N: int, c: Fraction) -> Fraction:
    """Compute delta_F_2^{grav} using the algebraic/symbolic expressions.

    Third independent verification path: via explicit harmonic sum formulas.
    """
    amps = derive_graph_amplitudes_symbolic(N, c)
    return sum(amps.values())


# ============================================================================
# Large-c (constant) and 1/c (subleading) analysis
# ============================================================================

def extract_B_N_from_large_c(N: int) -> Fraction:
    """Extract B(N) = lim_{c->inf} delta_F_2^{grav}(W_N, c).

    From the symbolic analysis:
      banana_mixed ~ (S1^2 - S2)/(4c) -> 0
      theta_mixed ~ S2_from3/(2c) -> 0
      lollipop_mixed = (S1-2)/48  (constant!)
      barbell_mixed ~ (S1^2 - 4)/(4c) -> 0

    So B(N) = lollipop contribution = (S1-2)/48.
    But wait: S1 = sum_{j=2}^N j = N(N+1)/2 - 1.
    S1 - 2 = N(N+1)/2 - 3.
    B(N) = (N(N+1)/2 - 3) / 48 = (N(N+1) - 6) / 96 = (N^2+N-6)/96 = (N-2)(N+3)/96.

    Confirmed: B(N) = (N-2)(N+3)/96.
    """
    S1 = N * (N + 1) // 2 - 1  # sum_{j=2}^N j
    return Fraction(S1 - 2, 48)


def extract_A_N_from_graphs(N: int) -> Fraction:
    """Extract A(N) = coefficient of 1/c in delta_F_2^{grav}(W_N, c).

    From the symbolic analysis:
      banana: (S1^2 - S2)/4
      theta: S2_from3/2
      lollipop: 0 (the lollipop contribution is c-independent)
      barbell: (S1^2 - 4)/4

    A(N) = (S1^2 - S2)/4 + S2_from3/2 + (S1^2 - 4)/4
         = (S1^2 - S2 + S1^2 - 4)/4 + S2_from3/2
         = (2*S1^2 - S2 - 4)/4 + S2_from3/2.

    Now S2 = sum_{j=2}^N j^2 = 4 + S2_from3.
    S2_from3 = S2 - 4.

    A(N) = (2*S1^2 - S2 - 4)/4 + (S2 - 4)/2
         = (2*S1^2 - S2 - 4 + 2*S2 - 8)/4
         = (2*S1^2 + S2 - 12)/4.

    Let's verify with known sums.
    S1 = N(N+1)/2 - 1.
    S2 = N(N+1)(2N+1)/6 - 1.

    So A(N) = (2*(N(N+1)/2-1)^2 + N(N+1)(2N+1)/6 - 1 - 12) / 4.
    """
    S1 = sum(j for j in range(2, N + 1))
    S2 = sum(j * j for j in range(2, N + 1))
    S2_from3 = S2 - 4

    A = Fraction(S1 * S1 - S2, 4) + Fraction(S2_from3, 2) + Fraction(S1 * S1 - 4, 4)
    return A


def verify_A_N_polynomial(N: int) -> bool:
    """Verify that A(N) = (N-2)(3N^3+14N^2+22N+33)/24."""
    computed = extract_A_N_from_graphs(N)
    claimed = Fraction((N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33), 24)
    return computed == claimed


# ============================================================================
# Newton interpolation for closed-form extraction
# ============================================================================

def newton_interpolate_delta_F2(N: int, num_points: int = 6
                                ) -> Dict[str, object]:
    """Extract the rational function delta_F_2 = P(c)/Q(c) by interpolation.

    Since delta_F_2 = B + A/c, we can verify by computing at 2 c-values
    and solving for A and B.
    """
    c1, c2 = Fraction(1), Fraction(2)
    d1 = delta_F2_grav_graph_sum(N, c1)
    d2 = delta_F2_grav_graph_sum(N, c2)

    # d1 = B + A,  d2 = B + A/2
    # d1 - d2 = A/2, so A = 2*(d1 - d2)
    # B = d1 - A = d1 - 2*(d1 - d2) = 2*d2 - d1
    A_extracted = 2 * (d1 - d2)
    B_extracted = 2 * d2 - d1

    # Verify at a third point
    c3 = Fraction(3)
    d3 = delta_F2_grav_graph_sum(N, c3)
    d3_predicted = B_extracted + A_extracted / c3

    return {
        'A': A_extracted,
        'B': B_extracted,
        'A_matches_claim': A_extracted == claimed_A(N),
        'B_matches_claim': B_extracted == claimed_B(N),
        'verified_at_c3': d3 == d3_predicted,
    }


# ============================================================================
# W_3 specific check: delta_F2 = (c+204)/(16c)
# ============================================================================

def verify_W3_genus2(c: Fraction) -> Dict[str, Fraction]:
    """Verify delta_F_2(W_3) = (c+204)/(16c) independently."""
    graph_sum = delta_F2_grav_graph_sum(3, c)
    closed_form = (c + Fraction(204)) / (16 * c)
    symbolic = delta_F2_grav_symbolic(3, c)
    return {
        'graph_sum': graph_sum,
        'closed_form': closed_form,
        'symbolic': symbolic,
        'all_agree': graph_sum == closed_form == symbolic,
    }
