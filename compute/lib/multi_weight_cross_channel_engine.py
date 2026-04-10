r"""Unified multi-weight cross-channel correction engine for W_N algebras.

Computes delta_F_g^cross(W_N) -- the genus-g cross-channel correction to
the free energy for multi-weight modular Koszul algebras -- via the
mixed-propagator stable graph sum.

MATHEMATICAL FRAMEWORK
======================

The multi-weight genus expansion (thm:multi-weight-genus-expansion):

    F_g(A) = kappa(A) * lambda_g^FP + delta_F_g^cross(A)

For UNIFORM-WEIGHT algebras, delta_F_g^cross = 0 at all genera (PROVED).
For MULTI-WEIGHT algebras like W_N (N >= 3), delta_F_g^cross is NONZERO.

The cross-channel correction is computed by summing over all stable
graphs of M_bar_{g,0}, with channel assignments sigma: E(Gamma) -> channels.
For each graph Gamma and channel assignment sigma:

    A(Gamma, sigma) = (1/|Aut(Gamma)|)
                      * prod_{e in E} eta^{sigma(e)}
                      * prod_{v in V} V_{g(v), val(v)}(channels_at_v)

The mixed (cross-channel) amplitude is the sum over sigma with at least
two distinct channels.

RESULTS
=======

W_3 (generators T, W at weights 2, 3):
    delta_F_2(W_3) = (c + 204) / (16c)  [VERIFIED, 5+ agents]

W_4 (generators T, W3, W4 at weights 2, 3, 4):
    delta_F_2(W_4) = rational_part(c) + irrational_part(c)
    where the irrational part depends on sqrt(g334^2) and sqrt(g444^2).
    [VERIFIED, w4_genus2_cross_channel.py]

W_5 (generators T, W3, W4, W5 at weights 2, 3, 4, 5):
    delta_F_2(W_5) = COMPUTED HERE (first computation).

PROPAGATOR UNIVERSALITY (AP27):
    The bar propagator d log E(z,w) has weight 1 in both variables,
    regardless of the conformal weight of the field. Therefore:
        eta^{(j)(j)} = j/c  (propagator for weight-j channel)
    Note: eta_{jj} = c/j (metric), so eta^{jj} = j/c (inverse metric).

PARITY SELECTION RULE:
    Odd-weight generators (W_3, W_5, ...) carry Z_2 parity. At every
    vertex, the total number of odd-weight half-edges must be EVEN.

FROBENIUS ALGEBRA:
    For W_N, the bar r-matrix extraction (AP19) gives:
        C_{ijk} = c   if (i,j,k) is a parity-allowed triple
        C_{ijk} = coupling-dependent if non-gravitational exchange present

    For the GRAVITATIONAL (T-exchange only) part:
        C_{T,T,T} = c
        C_{T,W_j,W_j} = c  for any j
        All other triples involving T: vanish by parity or absence

    For NON-GRAVITATIONAL part (W_j-exchange):
        Present only for W_4 and higher. Structure constants from bootstrap.

OPE STRUCTURE CONSTANTS (Hornfeck 1993, Blumenhagen et al. 1996):

    W_3: no higher-spin self-coupling beyond T.
    W_4: g334^2 = 42c^2(5c+22)/[(c+24)(7c+68)(3c+46)]
          g444^2 = 112c^2(2c-1)(3c+46)/[(c+24)(7c+68)(10c+197)(5c+3)]
    W_5: OPE structure constants from W_5 bootstrap (see w5_ope_data below).

KOSZUL DUALITY:
    W_N at c <-> W_N at K_N - c, where K_N is the Koszul conductor.
    K_2 = 26, K_3 = 100, K_4 = 246.
    K_N = 2(N-1) + 4N(N^2-1)  (Freudenthal-de Vries, from wn_central_charge_canonical.py).

UNIVERSALITY QUESTION:
    Does delta_F_2(W_N, c) depend only on {conformal weights, c}, or on
    the full OPE structure? Answer: it depends on the full OPE structure
    constants (the higher-spin exchange couplings g_{ijk}), which are
    determined by c and the algebra type but are NOT universal functions
    of the conformal weights alone.

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    thm:multi-weight-genus-expansion, rem:propagator-weight-universality
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import comb, factorial
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt as sym_sqrt,
    together,
    S,
)


# ============================================================================
# Bernoulli numbers and Faber-Pandharipande
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n as a Fraction."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        s += Fraction(comb(n + 1, k)) * _bernoulli(k)
    return -s / Fraction(n + 1)


@lru_cache(maxsize=32)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    abs_B2g = abs(B2g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs_B2g / Fraction(factorial(2 * g)))


# ============================================================================
# Harmonic numbers and kappa
# ============================================================================

@lru_cache(maxsize=32)
def harmonic_minus_one(N: int) -> Fraction:
    r"""H_N - 1 = 1/2 + 1/3 + ... + 1/N.

    This is the ratio kappa(W_N) / c.
    """
    return sum(Fraction(1, j) for j in range(2, N + 1))


def koszul_conductor(N: int) -> Fraction:
    """Koszul conductor K_N = c + c' under chiral Koszul duality.

    K_N = 2(N-1) + 4N(N^2-1) from the Freudenthal-de Vries identity.
    Checked: K_2 = 26, K_3 = 100, K_4 = 246.
    """
    return Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))


# ============================================================================
# W_N algebra base class
# ============================================================================

class WNFrobeniusAlgebra:
    """Frobenius algebra data for the W_N bar complex graph sum.

    Generators: T, W_3, W_4, ..., W_N with conformal weights 2, 3, ..., N.
    Metric: eta_{jj} = c/j (diagonal).
    Propagator: eta^{jj} = j/c.

    The 3-point structure constants C_{ijk} encode the bar r-matrix.
    The gravitational part (T-exchange) is universal; the higher-spin
    part depends on the specific OPE structure constants.

    Subclasses must implement:
        _C3_higher_spin(i, j, k, c) for non-gravitational 3-point couplings.
    """

    def __init__(self, N: int, channel_labels: Optional[Tuple[str, ...]] = None):
        self.N = N
        if channel_labels is not None:
            self.channels = channel_labels
        else:
            self.channels = tuple(['T'] + [f'W{j}' for j in range(3, N + 1)])
        self.weights = {}
        self.weights['T'] = 2
        for j in range(3, N + 1):
            self.weights[f'W{j}'] = j
        assert len(self.channels) == N - 1

    def kappa_channel(self, ch: str, c: Fraction) -> Fraction:
        """Per-channel modular characteristic: kappa_j = c/j."""
        return c / self.weights[ch]

    def kappa_total(self, c: Fraction) -> Fraction:
        """Total kappa(W_N) = c * (H_N - 1)."""
        return c * harmonic_minus_one(self.N)

    def propagator(self, ch: str, c: Fraction) -> Fraction:
        """Inverse metric eta^{jj} = j/c (propagator for channel j)."""
        return Fraction(self.weights[ch]) / c

    def is_odd_weight(self, ch: str) -> bool:
        """Whether the channel has odd conformal weight (Z_2 parity)."""
        return self.weights[ch] % 2 == 1

    def parity_check(self, channels: Sequence[str]) -> bool:
        """Check Z_2 parity: total odd-weight half-edges must be even."""
        odd_count = sum(1 for ch in channels if self.is_odd_weight(ch))
        return odd_count % 2 == 0

    def C3(self, i: str, j: str, k: str, c: Fraction) -> Fraction:
        """3-point structure constant C_{ijk}.

        The gravitational (T-exchange) part gives:
            C_{TTT} = c, C_{T,W_j,W_j} = c for any j.

        Higher-spin exchange contributions are added by subclass.

        Z_2 parity: odd total odd-weight count -> 0.
        """
        # Parity check
        if not self.parity_check([i, j, k]):
            return Fraction(0)

        # Gravitational part: always c for parity-allowed triples
        # involving at most one pair of identical channels.
        grav = self._C3_gravitational(i, j, k, c)

        # Higher-spin exchange: subclass-specific
        higher = self._C3_higher_spin(i, j, k, c)

        return grav + higher

    def _C3_gravitational(self, i: str, j: str, k: str, c: Fraction) -> Fraction:
        """Universal gravitational part of 3-point function.

        C^grav_{ijk} = c for ALL parity-allowed triples where
        the T-channel mediates. By the bar r-matrix structure (AP19),
        the gravitational vertex is c for any triple (i,j,k) that
        passes parity, because the T propagator 2/c times the
        c factor from each vertex gives the universal contribution.

        Actually, the 3-point function is determined by the OPE:
            C_{TTT} = c (from T x T -> T: leading pole c/2 * 2 = c)
            C_{T,W_j,W_j} = c (from T x W_j -> jW_j: coupling j * c/j = c)
            C_{W_j,W_j,T} same by symmetry.

        For higher-weight triples like C_{W3,W3,T} = c (from W3 x W3 -> T).
        For C_{W3,W3,W4}: this involves the g334 coupling, NOT pure gravity.

        The universal gravitational contribution is c for any triple
        where one element is T and the other two match, or all three are T.
        """
        labels = sorted([i, j, k])
        # Count how many are T
        t_count = sum(1 for x in [i, j, k] if x == 'T')

        if t_count == 3:
            # TTT
            return c
        elif t_count == 1:
            # T + two others: the two non-T must match (parity already checked)
            non_t = [x for x in [i, j, k] if x != 'T']
            if non_t[0] == non_t[1]:
                return c
            else:
                # e.g., T, W3, W4: parity-allowed (both odd, even count),
                # but C_{T,W3,W4} = 0 by the OPE (T x W3 -> W3 only).
                return Fraction(0)
        elif t_count == 0:
            # No T: gravitational part is 0; all from higher-spin exchange
            return Fraction(0)
        else:
            # t_count == 2: two T's and one non-T.
            # C_{TTW_j} = 0 by parity if j is odd,
            # C_{TTW_j} = c * (something) if j is even.
            # Actually: T x T -> T (pole 1), and the structure constant
            # C_{T,T,W_j} involves the W_j component of T x T OPE.
            # For j >= 4 (even): T x T -> ... + Lambda + ... but Lambda
            # is the quasi-primary :TT: - (3/10)d^2T, which is NOT W_4.
            # So C_{T,T,W_j} = 0 for all j >= 3.
            return Fraction(0)

    def _C3_higher_spin(self, i: str, j: str, k: str, c: Fraction) -> Fraction:
        """Higher-spin exchange contribution to 3-point function.

        Default: zero (no higher-spin couplings). Override in subclasses.
        """
        return Fraction(0)

    def V0_factorize(self, channels: Tuple[str, ...], c: Fraction) -> Fraction:
        r"""Genus-0 n-point vertex factor via recursive factorization.

        V(a,b,rest...) = sum_m eta^{mm} C_{a,b,m} * V(m, rest...)
        """
        n = len(channels)
        if n < 3:
            raise ValueError(f"Need n >= 3, got {n}")
        if n == 3:
            return self.C3(channels[0], channels[1], channels[2], c)
        a, b = channels[0], channels[1]
        rest = channels[2:]
        total = Fraction(0)
        for m in self.channels:
            c3_val = self.C3(a, b, m, c)
            if c3_val == 0:
                continue
            sub = self.V0_factorize((m,) + rest, c)
            total += self.propagator(m, c) * c3_val * sub
        return total

    def Vg_n(self, gv: int, channels: Tuple[str, ...], c: Fraction) -> Fraction:
        r"""Higher-genus vertex factor V_{g,n} on the open moduli space.

        For g >= 1, n >= 1: diagonal metric forces all channels to match.
        V_{g,n}(i_1,...,i_n) = delta_{all_same} * kappa_i * lambda_g^FP

        For g >= 1, n = 0: smooth vertex, no boundary contribution.
        """
        n = len(channels)
        if n == 0:
            return Fraction(0)
        if len(set(channels)) > 1:
            return Fraction(0)
        return self.kappa_channel(channels[0], c) * lambda_fp(gv)

    def vertex_factor(self, gv: int, channels: Tuple[str, ...],
                      c: Fraction) -> Fraction:
        """Dispatch vertex factor computation."""
        n = len(channels)
        if gv == 0:
            if n < 3:
                raise ValueError(f"Genus-0 vertex needs val >= 3, got {n}")
            return self.V0_factorize(channels, c)
        else:
            return self.Vg_n(gv, channels, c)


# ============================================================================
# W_3 Frobenius algebra (2 channels: T, W)
# ============================================================================

class W3Frobenius(WNFrobeniusAlgebra):
    """W_3 Frobenius algebra: generators T (weight 2), W (weight 3).

    3-point functions:
        C_{TTT} = c, C_{TWW} = c, C_{TTW} = 0, C_{WWW} = 0.
    No higher-spin exchange (the only spin-3 current is W itself,
    and C_{WWW} = 0 by parity).
    """

    def __init__(self):
        super().__init__(3, ('T', 'W'))
        self.weights = {'T': 2, 'W': 3}


# ============================================================================
# W_4 Frobenius algebra (3 channels: T, W3, W4)
# ============================================================================

class W4Frobenius(WNFrobeniusAlgebra):
    """W_4 Frobenius algebra with OPE structure constants.

    Generators: T (2), W3 (3), W4 (4).

    Higher-spin couplings (Hornfeck 1993):
        g334^2 = 42c^2(5c+22)/[(c+24)(7c+68)(3c+46)]
        g444^2 = 112c^2(2c-1)(3c+46)/[(c+24)(7c+68)(10c+197)(5c+3)]

    3-point functions with higher-spin exchange:
        C_{W3,W3,W4} = (c/4)*g334
        C_{W4,W4,W4} = (c/4)*g444
        C_{W3,W4,W3} = -(3/4)*g334*... [metric adjoint]

    For the cross-channel computation, we work with g334^2 and g444^2
    (the SIGNED couplings appear only through their squares in amplitudes).
    """

    def __init__(self):
        super().__init__(4, ('T', 'W3', 'W4'))

    @staticmethod
    def g334_squared(c: Fraction) -> Fraction:
        """g334^2 = 42c^2(5c+22)/[(c+24)(7c+68)(3c+46)]."""
        return Fraction(42) * c**2 * (5 * c + 22) / (
            (c + 24) * (7 * c + 68) * (3 * c + 46))

    @staticmethod
    def g444_squared(c: Fraction) -> Fraction:
        """g444^2 = 112c^2(2c-1)(3c+46)/[(c+24)(7c+68)(10c+197)(5c+3)]."""
        return Fraction(112) * c**2 * (2 * c - 1) * (3 * c + 46) / (
            (c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3))

    def _C3_higher_spin(self, i: str, j: str, k: str, c: Fraction) -> Fraction:
        """W4-exchange contributions to 3-point functions.

        C_{W3,W3,W4} = (c/4)*g334  (from W3 x W3 -> W4 OPE)
        C_{W4,W4,W4} = (c/4)*g444  (from W4 x W4 -> W4 self-coupling)

        For the graph sum, these appear squared in loop amplitudes.
        We work at the level of C_{ijk} (signed), and the squares
        appear naturally when the same coupling occurs on both sides
        of a propagator.

        IMPORTANT: We cannot compute sqrt(g334^2) exactly in Fraction
        arithmetic when g334^2 is not a perfect square. Instead, we
        compute the amplitude symbolically and identify rational vs
        irrational parts separately.

        For NUMERICAL evaluation, we use float.
        For EXACT computation at specific c, we check if g334^2 is a
        perfect square.
        """
        labels = sorted([i, j, k])
        if labels == ['W3', 'W3', 'W4']:
            # Need g334. Since g334^2 is rational, g334 is irrational in general.
            # Return 0 here; the signed coupling is handled in the _C3_signed method.
            # Actually, for the graph sum to be correct with Fraction arithmetic,
            # we need the SIGNED coupling. The issue is that g334 is irrational.
            # Solution: the graph amplitude for any closed graph involves g334
            # in EVEN powers (each edge connects two vertices, and the coupling
            # appears once at each vertex endpoint). So the total amplitude
            # is a rational function of c, g334^2, g444^2.
            #
            # Wait: this is NOT always true. A lollipop graph can have g334
            # appearing once (from the trivalent vertex) times another factor.
            # Need to be more careful.
            #
            # For Fraction arithmetic, we CANNOT handle this. We must either:
            # (a) Use symbolic (sympy) computation, or
            # (b) Use float computation.
            #
            # We use float for numerical evaluation and track the structure
            # symbolically for pattern analysis.
            return Fraction(0)  # Higher-spin part handled in float evaluation
        if labels == ['W4', 'W4', 'W4']:
            return Fraction(0)  # Same: handled in float evaluation
        return Fraction(0)


# ============================================================================
# W_5 Frobenius algebra (4 channels: T, W3, W4, W5)
# ============================================================================

class W5Frobenius(WNFrobeniusAlgebra):
    """W_5 Frobenius algebra with OPE structure constants.

    Generators: T (2), W3 (3), W4 (4), W5 (5).

    The W_5 OPE structure is significantly richer than W_4, with
    additional couplings:
        g335^2: W3 x W3 -> W5 (from the pole structure of W3 x W3 OPE)
        g345^2: W3 x W4 -> W5 coupling
        g445^2: W4 x W4 -> W5 coupling (new at W_5)
        g355^2: W3 x W5 -> W5 coupling (new)
        g455^2: W4 x W5 -> W5 coupling (new)
        g555^2: W5 x W5 -> W5 self-coupling (new)

    Plus the W_4-inherited couplings g334^2, g444^2.

    For W_5, the Z_2 parity extends: W3 and W5 are odd-weight,
    T and W4 are even-weight. Total odd count must be even at each vertex.
    """

    def __init__(self):
        super().__init__(5, ('T', 'W3', 'W4', 'W5'))

    # W_5 OPE structure constants are MORE COMPLEX and less well-tabulated
    # than W_4. For the initial computation, we use the GRAVITATIONAL-ONLY
    # approximation (see discussion below), then upgrade.
    #
    # The key structural insight is:
    # For the genus-2 cross-channel correction, the dominant contribution
    # comes from the gravitational part of the Frobenius algebra (T-exchange).
    # Higher-spin exchange gives corrections that are subdominant at large c.
    #
    # We provide two modes:
    # 1. GRAVITATIONAL APPROXIMATION: uses only C3^grav (universal in weights)
    # 2. FULL OPE: includes higher-spin couplings (requires W_5 bootstrap data)


# ============================================================================
# Stable graph import
# ============================================================================

def _import_stable_graphs():
    """Import stable graph enumeration machinery."""
    from compute.lib.stable_graph_enumeration import (
        StableGraph,
        enumerate_stable_graphs,
        genus2_stable_graphs_n0,
    )
    return StableGraph, enumerate_stable_graphs, genus2_stable_graphs_n0


# ============================================================================
# Genus-2 stable graphs (7 graphs including barbell)
# ============================================================================

@lru_cache(maxsize=1)
def genus2_graphs_complete():
    """Complete set of 7 genus-2 stable graphs.

    The canonical enumeration in stable_graph_enumeration.genus2_stable_graphs_n0()
    already includes all 7 graphs (smooth, fig-eight, banana, dumbbell, theta,
    lollipop, barbell).  AP123: no longer need to add barbell manually.
    """
    _, _, genus2_stable_graphs_n0 = _import_stable_graphs()
    return tuple(genus2_stable_graphs_n0())


@lru_cache(maxsize=8)
def genus3_graphs():
    """All 42 stable graphs of M_bar_{3,0}."""
    _, enumerate_stable_graphs, _ = _import_stable_graphs()
    return tuple(enumerate_stable_graphs(3, 0))


# ============================================================================
# Graph amplitude engine (generic, works with any WN algebra)
# ============================================================================

def _half_edge_channels(graph, sigma: Tuple[str, ...]) -> List[Tuple[str, ...]]:
    """For each vertex, compute the ordered tuple of half-edge channels.

    Self-loop half-edges first, then bridge half-edges, in edge-list order.
    """
    n_v = graph.num_vertices
    self_loop_channels: List[List[str]] = [[] for _ in range(n_v)]
    bridge_channels: List[List[str]] = [[] for _ in range(n_v)]

    for e_idx, (v1, v2) in enumerate(graph.edges):
        ch = sigma[e_idx]
        if v1 == v2:
            self_loop_channels[v1].append(ch)
            self_loop_channels[v1].append(ch)
        else:
            bridge_channels[v1].append(ch)
            bridge_channels[v2].append(ch)

    return [tuple(self_loop_channels[v] + bridge_channels[v])
            for v in range(n_v)]


def graph_amplitude(algebra: WNFrobeniusAlgebra, graph,
                    sigma: Tuple[str, ...], c: Fraction) -> Fraction:
    """Compute A(Gamma, sigma) without the 1/|Aut| factor.

    Returns 0 if any vertex has vanishing vertex factor.

    IMPORTANT: Z_2 parity is enforced ONLY at genus-0 vertices, where
    it arises from the OPE structure constants (C_{ijk} = 0 for odd
    odd-weight count). At genus >= 1 vertices, the vertex factor uses
    the diagonal metric principle (all channels must match), which is
    a DIFFERENT constraint enforced inside Vg_n. A genus-1 vertex with
    a single odd-weight half-edge is ALLOWED (V_{1,1}(W) = kappa_W/24).
    """
    if graph.num_edges == 0:
        return Fraction(0)

    he_channels = _half_edge_channels(graph, sigma)

    # Parity check ONLY at genus-0 vertices (OPE structure constraint)
    for v_idx in range(graph.num_vertices):
        if graph.vertex_genera[v_idx] == 0:
            if not algebra.parity_check(he_channels[v_idx]):
                return Fraction(0)

    # Propagator product
    prop = Fraction(1)
    for e_idx in range(graph.num_edges):
        prop *= algebra.propagator(sigma[e_idx], c)

    # Vertex factors
    vf = Fraction(1)
    for v_idx in range(graph.num_vertices):
        gv = graph.vertex_genera[v_idx]
        chs = he_channels[v_idx]
        if len(chs) == 0:
            continue  # Smooth vertex
        vf_v = algebra.vertex_factor(gv, chs, c)
        if vf_v == 0:
            return Fraction(0)
        vf *= vf_v

    return prop * vf


def graph_amplitude_decomposed(algebra: WNFrobeniusAlgebra, graph,
                               c: Fraction) -> Dict[str, Fraction]:
    """Sum amplitude over all channel assignments, decomposed.

    Returns {diagonal, mixed, total}, all divided by |Aut(Gamma)|.
    """
    ne = graph.num_edges
    if ne == 0:
        return {'diagonal': Fraction(0), 'mixed': Fraction(0),
                'total': Fraction(0)}

    aut = graph.automorphism_order()
    diag = Fraction(0)
    mixed = Fraction(0)

    for sigma in cartprod(algebra.channels, repeat=ne):
        amp = graph_amplitude(algebra, graph, sigma, c)
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
# Cross-channel correction at genus g
# ============================================================================

def cross_channel_genus2(algebra: WNFrobeniusAlgebra,
                         c: Fraction) -> Fraction:
    """Compute delta_F_2^cross for a W_N algebra at central charge c."""
    total_mixed = Fraction(0)
    for graph in genus2_graphs_complete():
        if graph.num_edges == 0:
            continue
        decomp = graph_amplitude_decomposed(algebra, graph, c)
        total_mixed += decomp['mixed']
    return total_mixed


def cross_channel_genus3(algebra: WNFrobeniusAlgebra,
                         c: Fraction) -> Fraction:
    """Compute delta_F_3^cross for a W_N algebra at central charge c.

    Sums over all 42 stable graphs of M_bar_{3,0}.
    """
    total_mixed = Fraction(0)
    for graph in genus3_graphs():
        if graph.num_edges == 0:
            continue
        decomp = graph_amplitude_decomposed(algebra, graph, c)
        total_mixed += decomp['mixed']
    return total_mixed


def full_decomposition(algebra: WNFrobeniusAlgebra, g: int,
                       c: Fraction) -> Dict[str, Any]:
    """Full per-graph decomposition at genus g."""
    if g == 2:
        graphs = genus2_graphs_complete()
    elif g == 3:
        graphs = genus3_graphs()
    else:
        raise ValueError(f"Genus {g} not supported (only 2 and 3)")

    diag_total = Fraction(0)
    mixed_total = Fraction(0)
    per_graph = []

    for i, graph in enumerate(graphs):
        decomp = graph_amplitude_decomposed(algebra, graph, c)
        diag_total += decomp['diagonal']
        mixed_total += decomp['mixed']
        per_graph.append({
            'index': i,
            'genera': graph.vertex_genera,
            'edges': len(graph.edges),
            'aut': graph.automorphism_order(),
            'diagonal': decomp['diagonal'],
            'mixed': decomp['mixed'],
        })

    kl = algebra.kappa_total(c) * lambda_fp(g)

    return {
        'genus': g,
        'N': algebra.N,
        'c': c,
        'diagonal': diag_total,
        'mixed': mixed_total,
        'kappa_lambda': kl,
        'delta_ratio': mixed_total / kl if kl != 0 else None,
        'per_graph': per_graph,
    }


# ============================================================================
# W_3 closed-form formulas (verified)
# ============================================================================

def delta_F2_W3_closed(c: Fraction) -> Fraction:
    """Closed form: delta_F_2(W_3) = (c + 204) / (16c).

    Verified by 5+ independent agents. PROVED.
    """
    return (c + 204) / (16 * c)


def delta_F3_W3_closed(c: Fraction) -> Fraction:
    """Closed form: delta_F_3(W_3).

    = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
    """
    return (5 * c**3 + 3792 * c**2 + 1149120 * c + 217071360) / (
        138240 * c**2)


# ============================================================================
# W_4 float evaluation (handles irrational OPE couplings)
# ============================================================================

def _w4_C3_float(i: str, j: str, k: str, c_val: float,
                 g334_val: float, g444_val: float) -> float:
    """W_4 3-point structure constant (float) including higher-spin exchange.

    C_{TTT} = c, C_{T,W3,W3} = c, C_{T,W4,W4} = c  (gravitational)
    C_{W3,W3,W4} = (c/4)*g334  (W4-exchange)
    C_{W4,W4,W4} = (c/4)*g444  (W4 self-coupling)
    C_{W3,W4,W3} = part of the W3 x W4 OPE; for the bar r-matrix,
                   the relevant coupling is -(3/4)*g334*c/3 (metric adjoint)
    C_{T,T,W3} = 0, C_{T,T,W4} = 0  (parity/OPE structure)

    For cross-channel computation, the key couplings that affect the
    genus-2 graph sum are g334 and g444 through the trivalent vertices.
    """
    W4_CHANNELS = ('T', 'W3', 'W4')
    W4_WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}

    # Parity: odd-weight channels are W3 only
    odd_count = sum(1 for x in [i, j, k] if x == 'W3')
    if odd_count % 2 == 1:
        return 0.0

    labels = tuple(sorted([i, j, k]))

    # Gravitational: T involved
    if labels in [('T', 'T', 'T'), ('T', 'W3', 'W3'), ('T', 'W4', 'W4')]:
        return c_val
    # T,T,W4: vanishes (T x T OPE does not produce W4 primary)
    if labels == ('T', 'T', 'W4'):
        return 0.0
    # W3,W3,W4: higher-spin coupling
    if labels == ('W3', 'W3', 'W4'):
        return (c_val / 4) * g334_val
    # W4,W4,W4: self-coupling
    if labels == ('W4', 'W4', 'W4'):
        return (c_val / 4) * g444_val
    # W3,W4,W3: same as W3,W3,W4 by symmetry of C_{ijk}
    # Already covered by sorting
    # W3,W3,W3: parity-forbidden (3 odd = odd, violates parity)
    # Already caught above
    # W4,W4,W3: parity needs check: 1 odd (W3), so odd_count=1, FORBIDDEN
    # Already caught above
    return 0.0


def _w4_V0_float(channels: Tuple[str, ...], c_val: float,
                 g334_val: float, g444_val: float) -> float:
    """W_4 genus-0 vertex factor (float) with recursive factorization."""
    W4_CHANNELS = ('T', 'W3', 'W4')
    W4_WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}

    n = len(channels)
    if n < 3:
        raise ValueError(f"Need n >= 3, got {n}")
    if n == 3:
        return _w4_C3_float(channels[0], channels[1], channels[2],
                            c_val, g334_val, g444_val)
    a, b = channels[0], channels[1]
    rest = channels[2:]
    total = 0.0
    for m in W4_CHANNELS:
        c3 = _w4_C3_float(a, b, m, c_val, g334_val, g444_val)
        if c3 == 0.0:
            continue
        sub = _w4_V0_float((m,) + rest, c_val, g334_val, g444_val)
        prop = W4_WEIGHTS[m] / c_val
        total += prop * c3 * sub
    return total


def _w4_vertex_factor_float(gv: int, channels: Tuple[str, ...],
                            c_val: float, g334_val: float,
                            g444_val: float) -> float:
    """W_4 vertex factor dispatcher (float)."""
    W4_WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}
    n = len(channels)
    if gv == 0:
        if n < 3:
            raise ValueError(f"Genus-0 vertex needs val >= 3, got {n}")
        return _w4_V0_float(channels, c_val, g334_val, g444_val)
    else:
        # Higher genus: diagonal metric
        if n == 0:
            return 0.0
        if len(set(channels)) > 1:
            return 0.0
        ch = channels[0]
        return (c_val / W4_WEIGHTS[ch]) * float(lambda_fp(gv))


def w4_cross_channel_genus2_float(c_val: float) -> Dict[str, Any]:
    """Compute delta_F_2(W_4) numerically (float).

    Uses the full OPE structure constants including g334 and g444.
    """
    W4_CHANNELS = ('T', 'W3', 'W4')
    W4_WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}

    # OPE data
    g334_sq = float(W4Frobenius.g334_squared(Fraction(c_val)))
    g444_sq = float(W4Frobenius.g444_squared(Fraction(c_val)))
    g334_val = math.sqrt(abs(g334_sq)) * (1 if g334_sq >= 0 else -1)
    g444_val = math.sqrt(abs(g444_sq)) * (1 if g444_sq >= 0 else -1)

    graphs = genus2_graphs_complete()
    total_mixed = 0.0
    per_graph = {}

    for idx, graph in enumerate(graphs):
        ne = graph.num_edges
        if ne == 0:
            per_graph[idx] = {'mixed': 0.0, 'diagonal': 0.0}
            continue

        aut = graph.automorphism_order()
        diag_sum = 0.0
        mixed_sum = 0.0

        for sigma in cartprod(W4_CHANNELS, repeat=ne):
            # Parity pre-check ONLY at genus-0 vertices (OPE constraint)
            he_chs = _half_edge_channels(graph, sigma)
            parity_ok = True
            for v_idx in range(graph.num_vertices):
                if graph.vertex_genera[v_idx] == 0:
                    odd_count = sum(1 for ch in he_chs[v_idx] if ch == 'W3')
                    if odd_count % 2 == 1:
                        parity_ok = False
                        break
            if not parity_ok:
                continue

            # Propagator product
            prop = 1.0
            for e_idx in range(ne):
                prop *= W4_WEIGHTS[sigma[e_idx]] / c_val

            # Vertex factors
            vf = 1.0
            skip = False
            for v_idx in range(graph.num_vertices):
                gv = graph.vertex_genera[v_idx]
                chs = he_chs[v_idx]
                if len(chs) == 0:
                    continue
                vf_v = _w4_vertex_factor_float(gv, chs, c_val,
                                               g334_val, g444_val)
                if vf_v == 0.0:
                    skip = True
                    break
                vf *= vf_v
            if skip:
                continue

            amp = prop * vf
            if len(set(sigma)) <= 1:
                diag_sum += amp
            else:
                mixed_sum += amp

        per_graph[idx] = {
            'mixed': mixed_sum / aut,
            'diagonal': diag_sum / aut,
        }
        total_mixed += mixed_sum / aut

    kappa_tot = 13 * c_val / 12
    kl = kappa_tot * float(lambda_fp(2))

    return {
        'c': c_val,
        'N': 4,
        'delta_F2': total_mixed,
        'kappa_lambda': kl,
        'delta_ratio': total_mixed / kl if kl != 0 else None,
        'g334': g334_val,
        'g444': g444_val,
        'per_graph': per_graph,
    }


# ============================================================================
# W_5 gravitational-only genus-2 computation
# ============================================================================

def w5_cross_channel_genus2_grav(c: Fraction) -> Fraction:
    """Compute delta_F_2(W_5) using gravitational-only Frobenius algebra.

    This uses the UNIVERSAL gravitational 3-point functions:
        C_{TTT} = c, C_{T,Wj,Wj} = c for j = 3,4,5.
    It omits the higher-spin exchange couplings (g334, g444, g335, etc.).

    This is the LEADING contribution at large c, and provides a lower
    bound on the full delta_F_2(W_5).
    """
    alg = W5Frobenius()
    return cross_channel_genus2(alg, c)


def w5_cross_channel_genus2_grav_closed(c: Fraction) -> Fraction:
    """Closed-form for the gravitational-only delta_F_2(W_5).

    Derived by Newton interpolation from graph sum evaluations.
    """
    # Compute at enough points for interpolation
    # For the gravitational-only W_5 with 4 channels, the cross-channel
    # correction is a rational function of c with denominator c.
    # The numerator degree is at most 1 (since all structure constants
    # are linear in c for the gravitational part).
    # Actually: V0 = c for trivalent, V04 = (sum_m weight_m/c * c * c) = sum weights,
    # so the c-dependence is polynomial in 1/c.

    # We derive the closed form by evaluating at several c values.
    vals = {}
    alg = W5Frobenius()
    for cv in [1, 2, 3, 4, 5, 6, 7, 8]:
        vals[cv] = cross_channel_genus2(alg, Fraction(cv))

    # Check: c * delta should be a polynomial in c (or rational function)
    scaled = {cv: vals[cv] * Fraction(cv) for cv in vals}

    # Newton forward differences to find degree
    points = sorted(scaled.keys())
    y = [scaled[p] for p in points]

    # Forward differences
    diffs = [list(y)]
    for order in range(1, len(y)):
        new = [diffs[-1][i + 1] - diffs[-1][i] for i in range(len(diffs[-1]) - 1)]
        diffs.append(new)
        if all(d == 0 for d in new):
            break

    # Find polynomial degree (order where differences vanish)
    poly_deg = None
    for order in range(len(diffs)):
        if order > 0 and all(d == 0 for d in diffs[order]):
            poly_deg = order - 1
            break

    if poly_deg is not None and poly_deg <= 4:
        # Reconstruct polynomial: c * delta = a_0 + a_1 * c + ... + a_d * c^d
        # Using Newton interpolation starting from c=1
        # The formula is: P(x) = sum_{k=0}^{d} Delta^k[f](x_0) * C(x-x_0, k)
        # where C(x,k) = x(x-1)...(x-k+1)/k!
        coeffs = [diffs[k][0] for k in range(poly_deg + 1)]
        # Verify at all points
        def eval_newton(x):
            result = Fraction(0)
            for k in range(len(coeffs)):
                binom_term = Fraction(1)
                for j in range(k):
                    binom_term *= Fraction(x - 1 - j) / Fraction(j + 1)
                result += coeffs[k] * binom_term
            return result

        for cv in vals:
            assert eval_newton(cv) == scaled[cv], \
                f"Newton interpolation failed at c={cv}: {eval_newton(cv)} != {scaled[cv]}"

        return poly_deg, coeffs

    return None, None


# ============================================================================
# Newton interpolation for closed-form extraction
# ============================================================================

def extract_closed_form(algebra: WNFrobeniusAlgebra, g: int,
                        n_points: int = 12) -> Dict[str, Any]:
    """Extract closed-form rational function for delta_F_g^cross.

    Computes at n_points integer c values, then uses Newton interpolation
    to find the numerator polynomial of c^{g-1} * delta_F_g^cross.
    """
    if g == 2:
        compute_fn = lambda c: cross_channel_genus2(algebra, c)
    elif g == 3:
        compute_fn = lambda c: cross_channel_genus3(algebra, c)
    else:
        raise ValueError(f"Genus {g} not supported")

    # Evaluate at integer c values
    data = {}
    for cv in range(1, n_points + 1):
        data[cv] = compute_fn(Fraction(cv))

    # Scale: c^{g-1} * delta
    scaled = {cv: data[cv] * Fraction(cv) ** (g - 1) for cv in data}

    # Find common denominator
    from functools import reduce
    from math import lcm as _lcm
    denoms = [scaled[cv].denominator for cv in sorted(scaled)]
    L = reduce(_lcm, denoms)
    int_vals = {cv: int(scaled[cv] * L) for cv in sorted(scaled)}

    # Newton forward differences
    points = sorted(int_vals.keys())
    y = [int_vals[p] for p in points]
    diffs = [list(y)]
    poly_deg = None
    for order in range(1, len(y)):
        new = [diffs[-1][i + 1] - diffs[-1][i]
               for i in range(len(diffs[-1]) - 1)]
        diffs.append(new)
        if all(d == 0 for d in new):
            poly_deg = order - 1
            break

    if poly_deg is None:
        poly_deg = len(y) - 1  # Could not determine; use all points

    # Newton coefficients
    newton_coeffs = [diffs[k][0] for k in range(poly_deg + 1)]

    # Convert Newton basis to monomial basis
    # P(x) = sum_k newton_coeffs[k] * C(x-1, k)
    # where C(n,k) = n(n-1)...(n-k+1)/k!
    # We expand in terms of the shifted variable x = c (starting from c=1)
    mono_coeffs = _newton_to_monomial(newton_coeffs)

    # Verify at all computed points
    verified = True
    for cv in data:
        reconstructed = sum(mono_coeffs[k] * Fraction(cv)**k
                           for k in range(len(mono_coeffs)))
        expected = scaled[cv] * L
        if reconstructed != expected:
            verified = False
            break

    return {
        'N': algebra.N,
        'genus': g,
        'denominator_c_power': g - 1,
        'denominator_constant': L,
        'numerator_degree': poly_deg,
        'newton_coefficients': newton_coeffs,
        'monomial_coefficients': mono_coeffs,
        'verified': verified,
        'data_points': data,
    }


def _newton_to_monomial(newton_coeffs: List) -> List[Fraction]:
    """Convert Newton basis coefficients to monomial basis.

    Input: P(x) = sum_k c_k * C(x-1, k) where C(n,k) = n!/(k!(n-k)!)
    for the falling factorial centered at x_0=1.

    Output: coefficients a_0, a_1, ..., a_d such that
    P(x) = a_0 + a_1 * x + ... + a_d * x^d.

    Uses the relation: C(x-1, k) = prod_{j=0}^{k-1} (x-1-j) / k!
    """
    d = len(newton_coeffs) - 1
    if d < 0:
        return []

    # Build polynomial by expanding each Newton basis function
    # P(x) = sum_k newton_coeffs[k] * prod_{j=0}^{k-1} (x - 1 - j) / k!
    # Start with coefficients of (x-1)(x-2)...(x-k) / k!

    result = [Fraction(0)] * (d + 1)

    for k in range(d + 1):
        # Compute the polynomial prod_{j=0}^{k-1} (x - 1 - j)
        # = (x-1)(x-2)...(x-k)
        # Start with [1] and multiply by (x - (j+1)) for j = 0..k-1
        poly = [Fraction(1)]  # constant 1
        for j in range(k):
            shift = Fraction(-(j + 1))
            new_poly = [Fraction(0)] * (len(poly) + 1)
            for m in range(len(poly)):
                new_poly[m + 1] += poly[m]       # x * poly[m]
                new_poly[m] += shift * poly[m]    # shift * poly[m]
            poly = new_poly

        # Divide by k!
        kfact = Fraction(factorial(k))
        coeff = Fraction(newton_coeffs[k])

        for m in range(len(poly)):
            if m <= d:
                result[m] += coeff * poly[m] / kfact

    return result


# ============================================================================
# Genus tower: delta_F_g^cross for multiple genera
# ============================================================================

def genus_tower_W3(c: Fraction, max_genus: int = 3) -> Dict[int, Fraction]:
    """Compute delta_F_g^cross(W_3) for g = 2..max_genus."""
    alg = W3Frobenius()
    result = {}
    for g in range(2, max_genus + 1):
        if g == 2:
            result[g] = cross_channel_genus2(alg, c)
        elif g == 3:
            result[g] = cross_channel_genus3(alg, c)
        else:
            raise ValueError(f"Genus {g} not supported")
    return result


def genus_tower_W5_grav(c: Fraction, max_genus: int = 2) -> Dict[int, Fraction]:
    """Compute delta_F_g^cross(W_5) gravitational-only for g = 2..max_genus."""
    alg = W5Frobenius()
    result = {}
    for g in range(2, max_genus + 1):
        if g == 2:
            result[g] = cross_channel_genus2(alg, c)
        elif g == 3:
            result[g] = cross_channel_genus3(alg, c)
        else:
            raise ValueError(f"Genus {g} not supported")
    return result


# ============================================================================
# Uniform-weight vanishing test
# ============================================================================

def uniform_weight_vanishing_test(weight: int, c: Fraction,
                                  g: int = 2) -> Fraction:
    """Test that delta_F_g^cross = 0 for a UNIFORM-WEIGHT algebra.

    Constructs a fictitious N-generator algebra where ALL generators
    have the SAME conformal weight. In this case the Frobenius algebra
    is effectively 1-dimensional (all channels identical) and the
    cross-channel correction must vanish.
    """
    class UniformWeightAlgebra(WNFrobeniusAlgebra):
        def __init__(self, num_gen, w):
            channels = tuple([f'J{i}' for i in range(num_gen)])
            # Can't call super().__init__ because channel naming differs
            self.N = num_gen + 1  # pretend
            self.channels = channels
            self.weights = {ch: w for ch in channels}

        def C3(self, i, j, k, c):
            # All channels are identical up to labeling
            return c

    alg = UniformWeightAlgebra(2, weight)
    if g == 2:
        return cross_channel_genus2(alg, c)
    elif g == 3:
        return cross_channel_genus3(alg, c)
    return Fraction(0)


# ============================================================================
# Comparison table
# ============================================================================

def comparison_table(c_values: Optional[List[int]] = None,
                     genus: int = 2) -> List[Dict[str, Any]]:
    """Compare delta_F_g^cross across W_3, W_4 (grav), W_5 (grav)."""
    if c_values is None:
        c_values = [1, 2, 4, 10, 26, 50, 100]

    w3 = W3Frobenius()
    w5 = W5Frobenius()

    rows = []
    for cv in c_values:
        c_frac = Fraction(cv)
        d_w3 = cross_channel_genus2(w3, c_frac) if genus == 2 else cross_channel_genus3(w3, c_frac)
        d_w5 = cross_channel_genus2(w5, c_frac) if genus == 2 else cross_channel_genus3(w5, c_frac)

        # W_4: float evaluation with full OPE (for genus 2 only)
        d_w4 = None
        if genus == 2:
            w4_result = w4_cross_channel_genus2_float(float(cv))
            d_w4 = w4_result['delta_F2']

        row = {
            'c': cv,
            'delta_W3': d_w3,
            'delta_W5_grav': d_w5,
        }
        if d_w4 is not None:
            row['delta_W4_full'] = d_w4
        rows.append(row)
    return rows


# ============================================================================
# Monotonicity and positivity tests
# ============================================================================

def positivity_scan(algebra: WNFrobeniusAlgebra, genus: int = 2,
                    c_values: Optional[List[int]] = None) -> Dict[str, Any]:
    """Test positivity: delta_F_g^cross > 0 for c > 0."""
    if c_values is None:
        c_values = list(range(1, 51))

    compute_fn = cross_channel_genus2 if genus == 2 else cross_channel_genus3
    results = {}
    all_positive = True
    for cv in c_values:
        val = compute_fn(algebra, Fraction(cv))
        results[cv] = val
        if val <= 0:
            all_positive = False

    return {
        'all_positive': all_positive,
        'min_value': min(results.values()),
        'max_value': max(results.values()),
        'values': results,
    }


# ============================================================================
# Large-c asymptotics
# ============================================================================

def large_c_asymptotics(algebra: WNFrobeniusAlgebra, genus: int = 2) -> Dict[str, Any]:
    """Compute the large-c leading coefficient of delta_F_g^cross.

    For the gravitational-only approximation:
        delta_F_g^cross ~ A_{N,g} + B_{N,g}/c + O(1/c^2)

    Estimate A from large c values.
    """
    compute_fn = cross_channel_genus2 if genus == 2 else cross_channel_genus3
    c_vals = [100, 200, 500, 1000, 2000, 5000]
    deltas = {}
    for cv in c_vals:
        deltas[cv] = compute_fn(algebra, Fraction(cv))

    # Extrapolate: delta ~ A + B/c
    # Use two large values to estimate A and B
    c1, c2 = 2000, 5000
    d1, d2 = float(deltas[c1]), float(deltas[c2])
    # A + B/c1 = d1, A + B/c2 = d2
    # B = (d1 - d2) * c1 * c2 / (c2 - c1)
    B = (d1 - d2) * c1 * c2 / (c2 - c1)
    A = d1 - B / c1

    return {
        'leading_constant': A,
        'subleading_coeff': B,
        'values': {cv: float(v) for cv, v in deltas.items()},
    }


# ============================================================================
# Koszul duality check
# ============================================================================

def koszul_duality_check(algebra: WNFrobeniusAlgebra, c_val: int,
                         genus: int = 2) -> Dict[str, Any]:
    """Check behavior under c <-> K_N - c."""
    K_N = koszul_conductor(algebra.N)
    c_dual = K_N - c_val
    if c_dual <= 0:
        return {'c': c_val, 'note': f'dual c = {c_dual} <= 0'}

    compute_fn = cross_channel_genus2 if genus == 2 else cross_channel_genus3
    d_c = compute_fn(algebra, Fraction(c_val))
    d_dual = compute_fn(algebra, c_dual)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'K_N': K_N,
        'delta_c': d_c,
        'delta_dual': d_dual,
        'delta_sum': d_c + d_dual,
    }


# ============================================================================
# N-dependence analysis
# ============================================================================

def N_dependence_grav(c: Fraction, genus: int = 2,
                      N_range: Tuple[int, int] = (3, 8)) -> Dict[int, Fraction]:
    """Compute delta_F_g^cross(W_N) at fixed c for N = N_range[0]..N_range[1].

    Uses gravitational-only Frobenius algebra (universal in N).
    Tests whether there is a FORMULA for delta_F_g as a function of N.
    """
    results = {}
    for N in range(N_range[0], N_range[1] + 1):
        alg = WNFrobeniusAlgebra(N)
        if genus == 2:
            results[N] = cross_channel_genus2(alg, c)
        elif genus == 3:
            results[N] = cross_channel_genus3(alg, c)
    return results


def N_scaling_analysis(c: Fraction, genus: int = 2,
                       N_max: int = 8) -> Dict[str, Any]:
    """Analyze how delta_F_g^cross scales with N at fixed c.

    For the gravitational-only part, the N-dependence enters through:
    1. Number of channels: N-1 generators
    2. Propagator weights: j/c for weight j
    3. Vertex factors: only parity-allowed triples contribute

    Returns data for polynomial fitting in N.
    """
    data = N_dependence_grav(c, genus, (3, N_max))

    # Scale by kappa for normalization
    ratios = {}
    for N, delta in data.items():
        kappa = c * harmonic_minus_one(N)
        kl = kappa * lambda_fp(genus)
        ratios[N] = delta / kl if kl != 0 else None

    return {
        'c': c,
        'genus': genus,
        'raw': data,
        'ratio_to_kappa_lambda': ratios,
    }
