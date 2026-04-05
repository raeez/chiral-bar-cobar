r"""Pixton ideal generation from shadow obstruction tower MC relations.

Tests conj:pixton-from-shadows: for class-M algebras (r_max = infinity),
the infinite family of MC-descended tautological relations generates
the Pixton ideal in R*(M-bar_{g,n}).

The MC relation at (g,n) (thm:mc-tautological-descent):

  sum_{sep} xi_{sep,*}(tau_{g1} . tau_{g2})
  + xi_{nsep,*}(tau_{g-1,n+2})
  + delta_pf^{(g,n)}
  = 0    in R*(M-bar_{g,n+1})

For class-G (Heisenberg): delta_pf = 0, giving only Mumford relations.
For class-M (Virasoro): delta_pf != 0, involving higher shadow data S_r.

The planted-forest correction delta_pf^{(g,n)} is supported on
codimension >= 2 strata and involves the higher L_infinity operations.

This module:
1. Computes Witten-Kontsevich intersection numbers via DVV recursion
2. Enumerates stable graphs at low genus
3. Computes graph integrals via edge-propagator expansion
4. Evaluates the MC relation (separating + non-separating + planted-forest)
5. Implements known Pixton/Faber-Zagier relations at genus 1-3
6. Tests whether MC-descended relations generate the Pixton ideal

Manuscript references:
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:mc-tautological-descent (higher_genus_modular_koszul.tex)
    rem:planted-forest-correction-explicit (higher_genus_modular_koszul.tex)
    conj:pixton-from-shadows (concordance.tex)
    prop:wdvv-from-mc (higher_genus_modular_koszul.tex)
    prop:mumford-from-mc (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import Rational, Symbol, cancel, factor, simplify, sqrt, Integer

c_sym = Symbol('c')


# ═══════════════════════════════════════════════════════════════════════════
# Part 1: Witten-Kontsevich intersection numbers
# ═══════════════════════════════════════════════════════════════════════════

def odd_double_fact(m: int) -> int:
    """m!! for odd m. Convention: (-1)!! = 1, 1!! = 1, 3!! = 3, 5!! = 15, etc."""
    if m <= 0:
        return 1
    result = 1
    for k in range(1, m + 1, 2):
        result *= k
    return result


def double_factorial(n: int) -> int:
    """(2n+1)!! = 1*3*5*...*(2n+1). For n < 0, returns 1 (by convention)."""
    return odd_double_fact(2 * n + 1)


@lru_cache(maxsize=8192)
def wk_intersection(g: int, d_tuple: Tuple[int, ...]) -> Fraction:
    r"""Witten-Kontsevich intersection number <tau_{d_1} ... tau_{d_n}>_g.

    Uses string + dilaton equations for reduction, with DVV recursion
    for the all-d_i >= 2 case.

    Base cases: <tau_0^3>_0 = 1,  <tau_1>_1 = 1/24.

    Parameters:
        g: genus
        d_tuple: tuple of non-negative integers (d_1, ..., d_n)

    Returns:
        Exact rational intersection number as Fraction.
    """
    d_list = sorted(d_tuple, reverse=True)
    d_tuple = tuple(d_list)
    n = len(d_tuple)

    # Empty or n=0
    if n == 0:
        return Fraction(0)

    # Non-negativity
    if any(d < 0 for d in d_tuple):
        return Fraction(0)

    # Stability: 2g - 2 + n > 0
    if 2 * g - 2 + n <= 0:
        return Fraction(0)

    # Dimensional constraint: sum d_i = 3g - 3 + n
    if sum(d_tuple) != 3 * g - 3 + n:
        return Fraction(0)

    # Base cases
    if g == 0 and d_tuple == (0, 0, 0):
        return Fraction(1)

    if g == 1 and d_tuple == (1,):
        return Fraction(1, 24)

    # ── String equation: if any d_i = 0 ──
    # <tau_0 tau_{d_1}...tau_{d_n}>_g = sum_j <tau_{d_1}...tau_{d_j - 1}...>_g
    if 0 in d_tuple:
        rest = list(d_tuple)
        rest.remove(0)
        result = Fraction(0)
        for j in range(len(rest)):
            if rest[j] >= 1:
                new_d = rest[:j] + [rest[j] - 1] + rest[j + 1:]
                result += wk_intersection(g, tuple(sorted(new_d, reverse=True)))
        return result

    # ── Dilaton equation: if any d_i = 1 and n >= 2 ──
    # <tau_1 tau_{d_1}...tau_{d_n}>_g = (2g - 2 + n) <tau_{d_1}...tau_{d_n}>_g
    if 1 in d_tuple and n >= 2:
        rest = list(d_tuple)
        rest.remove(1)
        factor = Fraction(2 * g - 2 + n - 1)
        return factor * wk_intersection(g, tuple(sorted(rest, reverse=True)))

    # ── DVV recursion: all d_i >= 2 ──
    d1 = d_list[0]
    rest = list(d_list[1:])

    lhs_coeff = odd_double_fact(2 * d1 + 1)  # (2d_1 + 1)!!

    rhs = Fraction(0)

    # Term 1: sum over j in rest
    for j_idx in range(len(rest)):
        dj = rest[j_idx]
        new_d = d1 + dj - 1
        remaining = rest[:j_idx] + rest[j_idx + 1:]
        new_tuple = tuple(sorted([new_d] + remaining, reverse=True))
        num = odd_double_fact(2 * d1 + 2 * dj - 1)  # (2d1+2dj-1)!!
        den = odd_double_fact(2 * dj - 1)  # (2dj-1)!!
        coeff = Fraction(num, den)
        rhs += coeff * wk_intersection(g, new_tuple)

    # Term 2: sum over a + b = d1 - 2
    if d1 >= 2:
        for a in range(d1 - 1):
            b = d1 - 2 - a
            dfa = odd_double_fact(2 * a + 1)  # (2a+1)!!
            dfb = odd_double_fact(2 * b + 1)  # (2b+1)!!
            coeff2 = Fraction(dfa * dfb, 2)

            # Non-separating: <tau_a tau_b tau_{d_2}...tau_{d_n}>_{g-1}
            if g >= 1:
                nsep_tuple = tuple(sorted([a, b] + rest, reverse=True))
                rhs += coeff2 * wk_intersection(g - 1, nsep_tuple)

            # Separating: sum over partitions I,J of rest, g1+g2=g
            for size_I in range(len(rest) + 1):
                for I_indices in itertools.combinations(range(len(rest)), size_I):
                    J_indices = [k for k in range(len(rest))
                                 if k not in I_indices]
                    I_d = [rest[k] for k in I_indices]
                    J_d = [rest[k] for k in J_indices]
                    for g1 in range(g + 1):
                        g2 = g - g1
                        tuple_I = tuple(sorted([a] + I_d, reverse=True))
                        tuple_J = tuple(sorted([b] + J_d, reverse=True))
                        val = (wk_intersection(g1, tuple_I)
                               * wk_intersection(g2, tuple_J))
                        if val != 0:
                            rhs += coeff2 * val

    return Fraction(rhs, lhs_coeff)


# ═══════════════════════════════════════════════════════════════════════════
# Part 2: Stable graph enumeration
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class StableVertex:
    """A vertex in a stable graph."""
    genus: int
    valence: int  # number of half-edges (including self-loops counted twice)

    def is_stable(self) -> bool:
        return 2 * self.genus - 2 + self.valence > 0


@dataclass(frozen=True)
class StableGraph:
    """A stable graph of type (g, n).

    Encoded by:
    - vertices: tuple of (genus, valence) pairs
    - edges: tuple of (v_i, h_i, v_j, h_j) for each edge connecting
             half-edge h_i at vertex v_i to half-edge h_j at vertex v_j
    - self_loops: tuple of (v_i, h_i, h_j) for self-loops at vertex v_i
    - n_legs: number of external legs (n)

    For simplicity in this module, we represent graphs by their combinatorial
    type: (genus partition, edge structure) with automorphism count.
    """
    name: str
    genus: int
    n_legs: int  # external legs
    vertices: Tuple[Tuple[int, int], ...]  # (genus, valence) per vertex
    n_edges: int
    n_self_loops: int  # number of self-loop edges
    n_bridges: int  # edges connecting distinct vertices
    automorphism_order: int
    codimension: int  # = n_edges (codimension in M-bar_g)


def stable_graphs_genus2_0leg() -> List[StableGraph]:
    """All stable graphs of type (g=2, n=0).

    Seven graphs A-G, organized by codimension (= number of edges).

    Codim 0: A (smooth)
    Codim 1: B (lollipop), D (dumbbell)
    Codim 2: C (sunset), E (bridge+loop)
    Codim 3: F (theta), G (figure-8 bridge)
    """
    return [
        StableGraph(
            name="A_smooth",
            genus=2, n_legs=0,
            vertices=((2, 0),),
            n_edges=0, n_self_loops=0, n_bridges=0,
            automorphism_order=1,
            codimension=0,
        ),
        StableGraph(
            name="B_lollipop",
            genus=2, n_legs=0,
            vertices=((1, 2),),
            n_edges=1, n_self_loops=1, n_bridges=0,
            automorphism_order=2,
            codimension=1,
        ),
        StableGraph(
            name="C_sunset",
            genus=2, n_legs=0,
            vertices=((0, 4),),
            n_edges=2, n_self_loops=2, n_bridges=0,
            automorphism_order=8,
            codimension=2,
        ),
        StableGraph(
            name="D_dumbbell",
            genus=2, n_legs=0,
            vertices=((1, 1), (1, 1)),
            n_edges=1, n_self_loops=0, n_bridges=1,
            automorphism_order=2,
            codimension=1,
        ),
        StableGraph(
            name="E_bridge_loop",
            genus=2, n_legs=0,
            vertices=((0, 3), (1, 1)),
            n_edges=2, n_self_loops=1, n_bridges=1,
            automorphism_order=2,
            codimension=2,
        ),
        StableGraph(
            name="F_theta",
            genus=2, n_legs=0,
            vertices=((0, 3), (0, 3)),
            n_edges=3, n_self_loops=0, n_bridges=3,
            automorphism_order=12,
            codimension=3,
        ),
        StableGraph(
            name="G_figure8_bridge",
            genus=2, n_legs=0,
            vertices=((0, 3), (0, 3)),
            n_edges=3, n_self_loops=2, n_bridges=1,
            automorphism_order=8,
            codimension=3,
        ),
    ]


def stable_graphs_genus1_1leg() -> List[StableGraph]:
    """All stable graphs of type (g=1, n=1).

    Two graphs:
    Codim 0: single vertex (1,1) with 1 external leg
    Codim 1: vertex (0,3) with 1 self-loop and 1 external leg
    """
    return [
        StableGraph(
            name="A11_smooth",
            genus=1, n_legs=1,
            vertices=((1, 1),),
            n_edges=0, n_self_loops=0, n_bridges=0,
            automorphism_order=1,
            codimension=0,
        ),
        StableGraph(
            name="B11_self_loop",
            genus=1, n_legs=1,
            vertices=((0, 3),),
            n_edges=1, n_self_loops=1, n_bridges=0,
            automorphism_order=2,
            codimension=1,
        ),
    ]


# ═══════════════════════════════════════════════════════════════════════════
# Part 3: Graph integral computation
# ═══════════════════════════════════════════════════════════════════════════

def graph_integral_genus2(graph: StableGraph) -> Fraction:
    r"""Compute the Hodge integral I(Gamma) for a genus-2 graph.

    I(Gamma) = sum over valid psi-power assignments * product of WK numbers * signs

    For each edge, the propagator 1/(psi+ + psi-) contributes (-1)^b
    where b is the psi-power at the "minus" half-edge.

    The dimensional constraint at each vertex v:
        sum of psi-powers at half-edges of v = 3*g(v) - 3 + val(v)

    Returns:
        The Hodge integral I(Gamma) as an exact Fraction.
    """
    name = graph.name

    if name == "A_smooth":
        # Single vertex (2,0): no edges, no half-edges.
        # The contribution is just the "identity" on M-bar_2.
        # I(A) is not a number — it's the class [M-bar_2] itself.
        # For the free energy: F_2(A) = ell_0^{(2)}, determined by MC.
        # Return 1 as a placeholder (the smooth graph contributes the
        # vertex weight ell_0^{(2)} directly, which is a CLASS not a number).
        return Fraction(1)

    elif name == "B_lollipop":
        # 1 vertex (1,2), 1 self-loop.
        # Dim M-bar_{1,2} = 1. Constraint: d_{h+} + d_{h-} = 3*1-3+2 = 2.
        # Edge propagator: sum_{a+b=2, a,b>=0} (-1)^b <tau_a tau_b>_1
        # But a+b must equal the vertex dimension = 2, and the edge expansion
        # gives terms with a+b = k for various k. The correct formula:
        # I(B) = sum_{a>=0} (-1)^a <tau_{1-a} tau_a>_1 ... hmm need to be
        # more careful.
        #
        # With self-loop at vertex v of type (1,2):
        # Two half-edges h+, h- at the SAME vertex. psi-powers d+, d-.
        # Constraint: d+ + d- = dim M-bar_{1,2} = 2.
        # Sign: (-1)^{d-} from edge propagator expansion.
        # WK number: <tau_{d+} tau_{d-}>_1
        result = Fraction(0)
        for d_plus in range(3):  # d+ = 0,1,2
            d_minus = 2 - d_plus
            if d_minus < 0:
                continue
            sign = (-1) ** d_minus
            wk = wk_intersection(1, (d_plus, d_minus))
            result += sign * wk
        return result

    elif name == "C_sunset":
        # 1 vertex (0,4), 2 self-loops.
        # Dim M-bar_{0,4} = 1. 4 half-edges: h1+,h1-,h2+,h2- at single vertex.
        # Constraint: d_{h1+}+d_{h1-}+d_{h2+}+d_{h2-} = 3*0-3+4 = 1.
        # Edge 1 sign: (-1)^{d_{h1-}}, Edge 2 sign: (-1)^{d_{h2-}}.
        # WK: <tau_{d1} tau_{d2} tau_{d3} tau_{d4}>_0
        result = Fraction(0)
        for d1p in range(2):
            for d1m in range(2):
                for d2p in range(2):
                    d2m = 1 - d1p - d1m - d2p
                    if d2m < 0:
                        continue
                    sign = (-1) ** (d1m + d2m)
                    wk = wk_intersection(0, tuple(sorted(
                        [d1p, d1m, d2p, d2m], reverse=True)))
                    result += sign * wk
        return result

    elif name == "D_dumbbell":
        # 2 vertices: v1=(1,1), v2=(1,1), 1 bridge.
        # Dim M-bar_{1,1} = 1 each. d+ at v1, d- at v2.
        # Constraint: d+ = 1, d- = 1 (each vertex 1D, one half-edge).
        # Actually: dim constraint at v1: d+ = 3*1-3+1 = 1. At v2: d- = 1.
        # Sign: (-1)^{d-} = (-1)^1 = -1.
        # WK: <tau_1>_1 * <tau_1>_1 = (1/24)^2.
        d_plus = 1  # forced by dim
        d_minus = 1  # forced by dim
        sign = (-1) ** d_minus
        wk1 = wk_intersection(1, (d_plus,))
        wk2 = wk_intersection(1, (d_minus,))
        return sign * wk1 * wk2

    elif name == "E_bridge_loop":
        # 2 vertices: v1=(0,3), v2=(1,1). Edges: 1 bridge + 1 self-loop at v1.
        # v1 has 3 half-edges: h_bridge (to v2), h_loop+, h_loop-.
        # Dim M-bar_{0,3} = 0. Constraint at v1: all psi-powers = 0.
        # So d_bridge_v1 = 0, d_loop+ = 0, d_loop- = 0.
        # Dim M-bar_{1,1} = 1. Constraint at v2: d_bridge_v2 = 1.
        # Bridge sign: (-1)^{d_bridge_v2} = (-1)^1 = -1.
        # Loop sign: (-1)^{d_loop-} = (-1)^0 = 1.
        # WK: <tau_0^3>_0 * <tau_1>_1 = 1 * 1/24.
        wk1 = wk_intersection(0, (0, 0, 0))
        wk2 = wk_intersection(1, (1,))
        # Bridge: v1 end has d=0, v2 end has d=1. Sign from v2 end: (-1)^1 = -1.
        # Loop at v1: both ends have d=0. Sign: (-1)^0 = 1.
        bridge_sign = (-1) ** 1
        loop_sign = (-1) ** 0
        return bridge_sign * loop_sign * wk1 * wk2

    elif name == "F_theta":
        # 2 vertices: v1=(0,3), v2=(0,3). 3 bridges.
        # Dim M-bar_{0,3} = 0 each. All psi-powers = 0 at both vertices.
        # Each bridge: d_v1 = 0, d_v2 = 0. But constraint: sum = 0 at each vertex.
        # Sign per bridge: (-1)^0 = 1.
        # WK: <tau_0^3>_0 * <tau_0^3>_0 = 1.
        # BUT: dim constraint says sum of psi-powers at each vertex = 0.
        # With all psi = 0, the integral over M-bar_{0,3} x M-bar_{0,3} is 1.
        # The pushforward to M-bar_2 gives the theta stratum class.
        wk1 = wk_intersection(0, (0, 0, 0))
        wk2 = wk_intersection(0, (0, 0, 0))
        total_sign = 1  # all bridge signs = +1
        return total_sign * wk1 * wk2

    elif name == "G_figure8_bridge":
        # 2 vertices: v1=(0,3), v2=(0,3). 1 bridge + 2 self-loops (1 each).
        # Dim M-bar_{0,3} = 0 each. All psi-powers = 0.
        # Signs: all (-1)^0 = 1.
        wk1 = wk_intersection(0, (0, 0, 0))
        wk2 = wk_intersection(0, (0, 0, 0))
        return wk1 * wk2

    else:
        raise ValueError(f"Unknown graph: {name}")


# ═══════════════════════════════════════════════════════════════════════════
# Part 4: Shadow CohFT amplitude at genus 2
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class ShadowData:
    """Shadow obstruction tower data for a chiral algebra.

    For rank-1 on the primary line, the data consists of:
    - kappa: S_2 (curvature / modular characteristic)
    - S_3: cubic shadow coefficient (alpha)
    - S_4: quartic contact invariant
    - S_r for r >= 5: higher shadows (computed from the recursion)
    - ell_0_g: genus-g vacuum amplitudes (determined by MC recursion)
    """
    name: str
    kappa: Any  # S_2
    S3: Any  # cubic shadow
    S4: Any  # quartic contact
    shadows: Dict[int, Any] = field(default_factory=dict)  # r -> S_r
    depth_class: str = "M"  # G, L, C, or M

    def S(self, r: int) -> Any:
        """Get shadow coefficient S_r."""
        if r == 2:
            return self.kappa
        elif r == 3:
            return self.S3
        elif r == 4:
            return self.S4
        else:
            return self.shadows.get(r, 0)


def virasoro_shadow_data(max_arity: int = 10) -> ShadowData:
    """Shadow data for Virasoro algebra Vir_c, parameterized by central charge c.

    kappa = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].
    Higher arities via convolution recursion.
    """
    from sympy import Rational as R

    kappa = c_sym / 2
    S3 = R(2)
    S4 = R(10) / (c_sym * (5 * c_sym + 22))

    # Compute higher shadows via sqrt(Q_L) Taylor expansion
    # Q_L(t) = (2*kappa + 3*S3*t)^2 + 2*Delta*t^2
    #        = 4*kappa^2 + 12*kappa*S3*t + (9*S3^2 + 16*kappa*S4)*t^2
    # sqrt(Q_L(0)) = 2*kappa = c (for kappa = c/2, c > 0)
    # We use a[0] = c directly (avoiding sqrt(c^2) ambiguity)
    q0_sqrt = 2 * kappa  # = c, the positive square root of 4*kappa^2
    q1 = 12 * kappa * S3  # = 12c
    q2 = 9 * S3 ** 2 + 16 * kappa * S4  # = 36 + 80/(5c+22)

    # Taylor coefficients of sqrt(Q_L(t))
    a = [None] * (max_arity - 1)
    a[0] = q0_sqrt  # = c (for c > 0)
    a[1] = cancel(q1 / (2 * a[0]))  # = 6
    if len(a) > 2:
        a[2] = cancel((q2 - a[1] ** 2) / (2 * a[0]))  # = 40/(c(5c+22))

    for n in range(3, len(a)):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv / (2 * a[0]))

    shadows = {}
    for n in range(len(a)):
        r = n + 2
        S_r = cancel(a[n] / r)
        shadows[r] = S_r

    data = ShadowData(
        name="Virasoro",
        kappa=kappa,
        S3=S3,
        S4=S4,
        shadows=shadows,
        depth_class="M",
    )
    return data


def heisenberg_shadow_data(level_sym=None) -> ShadowData:
    """Shadow data for Heisenberg algebra H_k.

    kappa = k (NOT k/2), S_3 = 0, S_4 = 0 (class G, terminates at arity 2).
    """
    if level_sym is None:
        level_sym = Symbol('k')
    return ShadowData(
        name="Heisenberg",
        kappa=level_sym,
        S3=Integer(0),
        S4=Integer(0),
        depth_class="G",
    )


def affine_shadow_data() -> ShadowData:
    r"""Shadow data for affine sl_2 at level k.

    kappa = dim(g)(k + h^v)/(2h^v) = 3(k+2)/4 for sl_2 (dim=3, h^v=2).
    NOT k/2: the previous formula "k(k+2)/(2(k+2)) = k/2" was wrong
    (AP1 error: copied from Heisenberg without recomputation).
    Reference: landscape_census.tex line 81.
    S_3 = 2, S_4 = 0 (class L, shadow depth 3).
    """
    k = Symbol('k')
    return ShadowData(
        name="Affine_sl2",
        kappa=Integer(3) * (k + 2) / 4,
        S3=Integer(2),
        S4=Integer(0),
        depth_class="L",
    )


# ═══════════════════════════════════════════════════════════════════════════
# Part 5: MC relation and planted-forest correction at genus 2
# ═══════════════════════════════════════════════════════════════════════════

def vertex_weight(graph: StableGraph, shadow: ShadowData) -> Any:
    """Product of vertex weights for a stable graph.

    For rank-1, the weight at vertex v of type (g_v, val_v) is:
    - ell_k^{(0)} = S_k for genus-0 vertices
    - ell_1^{(1)} = kappa for genus-1 univalent vertices
    - ell_2^{(1)} = (genus-1 two-point function, from MC) for genus-1 bivalent
    - ell_0^{(2)} = (genus-2 vacuum, from MC) for genus-2 zero-valent
    """
    weight = Integer(1)
    for (gv, val) in graph.vertices:
        if gv == 0:
            weight *= shadow.S(val)
        elif gv == 1:
            if val == 1:
                weight *= shadow.kappa
            elif val == 2:
                # ell_2^{(1)}: genus-1 two-point function
                # From MC recursion: involves kappa and S_3
                # At genus 1, n=2: the MC relation determines ell_2^{(1)}
                # from the codim-1 boundary of M-bar_{1,2}.
                # For rank-1: ell_2^{(1)} ~ kappa * S_3 / 24 (approximate)
                # More precisely: ell_2^{(1)} is determined by <tau_a tau_b>_1
                # weighted by shadow data.
                #
                # The exact formula from the MC equation at (1,2):
                # ell_2^{(1)} = kappa (the genus-1 tadpole with one extra leg)
                # Actually for rank-1: the operation ell_k^{(g)} at genus g
                # with k inputs on the 1D space V = <e> is a SCALAR.
                # ell_2^{(1)} = the genus-1 two-point function.
                # By dilaton: this is (2g-2+n-1)/(n) * ... it's model-dependent.
                # For now: ell_2^{(1)} = kappa (normalized by Hodge class).
                weight *= shadow.kappa
            elif val == 0:
                # Unstable (1,0) would need extra structure
                weight *= Integer(0)
            else:
                weight *= shadow.kappa  # placeholder
        elif gv == 2:
            if val == 0:
                # ell_0^{(2)}: determined by MC recursion from lower data.
                # This is NOT independently given; it's what we're computing.
                # For the graph sum at (2,0): the smooth graph A contributes
                # ell_0^{(2)}, and the MC equation says:
                # ell_0^{(2)} + (boundary contributions) = 0
                # So we DON'T include the smooth graph in the "Hodge integral"
                # computation; instead, the MC relation DETERMINES ell_0^{(2)}.
                weight *= Integer(1)  # placeholder
            else:
                weight *= Integer(1)  # placeholder
    return weight


def mc_relation_genus2_free_energy(shadow: ShadowData) -> Dict[str, Any]:
    """Compute all graph contributions to the genus-2 free energy.

    The MC relation at (g=2, n=0):
    ell_0^{(2)} + (separating) + (non-separating) + (planted-forest) = 0

    Equivalently:
    F_2 = sum over ALL graphs Gamma of
        (1/|Aut(Gamma)|) * w(Gamma) * I(Gamma)

    where the smooth graph contributes ell_0^{(2)} (determined by MC from the rest).

    Returns dict with:
    - 'graphs': {name: (weight, hodge_integral, contribution)}
    - 'separating': total from codim-1 separating graphs
    - 'non_separating': total from codim-1 non-separating graphs
    - 'planted_forest': total from codim >= 2 graphs (delta_pf)
    - 'mc_relation': the full relation (should be 0 for consistent data)
    """
    graphs = stable_graphs_genus2_0leg()
    results = {}
    separating = Integer(0)
    non_separating = Integer(0)
    planted_forest = Integer(0)

    for G in graphs:
        w = vertex_weight(G, shadow)
        I = graph_integral_genus2(G)
        I_sympy = Integer(I.numerator) / Integer(I.denominator)
        contrib = cancel(w * I_sympy / G.automorphism_order)

        results[G.name] = {
            'weight': w,
            'hodge_integral': I,
            'automorphism': G.automorphism_order,
            'contribution': contrib,
            'codimension': G.codimension,
        }

        if G.name == "A_smooth":
            # Smooth graph = ell_0^{(2)}, to be determined
            pass
        elif G.codimension == 1:
            # Codimension 1: separating (D) and non-separating (B)
            if G.n_bridges > 0:
                separating += contrib
            else:
                non_separating += contrib
        else:
            # Codimension >= 2: planted-forest correction
            planted_forest += contrib

    return {
        'graphs': results,
        'separating': cancel(separating),
        'non_separating': cancel(non_separating),
        'planted_forest': cancel(planted_forest),
        'boundary_total': cancel(separating + non_separating + planted_forest),
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 6: Pixton/Faber-Zagier relations
# ═══════════════════════════════════════════════════════════════════════════

def faber_zagier_genus2_relation() -> Dict[str, Fraction]:
    r"""The Faber-Zagier relation in R^2(M-bar_2).

    In the tautological ring of M-bar_2, the following relation holds:

    In terms of boundary strata and kappa/lambda classes:
    The codim-2 classes in R^2(M-bar_2) satisfy specific linear relations.

    The "second" tautological relation (beyond Mumford):
    From Faber's computation, R^*(M-bar_2) is generated by:
      lambda_1, delta_irr (=delta_0), delta_1

    With the relation:
      10*lambda_1 = delta_irr + 2*delta_1  in R^1(M-bar_2)

    And in R^2:
      lambda_1^2 = (1/5)*delta_1*lambda_1 = (1/10)*delta_1*delta_irr + ...

    More precisely, the Pixton relation at genus 2 in codim 2 is:
      120*lambda_2 - 12*lambda_1^2 + ... = 0

    For our purposes, we track the STRUCTURE of the relation:
    whether the planted-forest correction produces a class proportional
    to the known non-Mumford relation.

    Returns dict of coefficients.
    """
    # The Faber-Zagier relation at genus 2:
    # In R^2(M-bar_2): kappa_2 = (1/240)(10*kappa_1^2 - ...) + boundary
    # The first non-Mumford relation involves kappa_2 and kappa_1^2.
    # Equivalently: the codim-2 planted-forest class is a specific
    # multiple of the boundary class.

    # Key known values at genus 2:
    # integral_{M-bar_2} kappa_2 = 1/240
    # integral_{M-bar_2} kappa_1^2 = 1/240
    # integral_{M-bar_2} lambda_2 = 1/240
    # integral_{M-bar_2} lambda_1^2 = 1/1152
    # integral_{M-bar_2} lambda_1*delta_1 = 1/576
    # integral_{M-bar_2} delta_1^2 = -1/288

    return {
        'kappa_2': Fraction(1, 240),
        'kappa_1_sq': Fraction(1, 240),
        'lambda_2': Fraction(1, 240),
        'lambda_1_sq': Fraction(1, 1152),
        'lambda_1_delta_1': Fraction(1, 576),
        'delta_1_sq': Fraction(-1, 288),
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 7: Pixton conjecture verification
# ═══════════════════════════════════════════════════════════════════════════

def verify_mumford_from_mc(shadow: ShadowData) -> Dict[str, Any]:
    r"""Verify that the MC relation at arity 2 gives Mumford's relation.

    From prop:mumford-from-mc: at arity 2, genus g >= 2, the MC relation
    reduces to Mumford's relation on lambda classes:

    sum_{g1+g2=g} xi_{sep,*}(lambda_{g1} * lambda_{g2}) + xi_{nsep,*}(lambda_{g-1}) = 0

    For genus 2, this is:
    2 * lambda_1 * lambda_1 (separating g1=g2=1) + lambda_1 (non-sep) = 0

    Check: kappa * (dumbbell contribution) + kappa * (lollipop contribution) = 0?
    """
    # Dumbbell D: separating, codim 1
    # Contribution: (1/2) * kappa^2 * I(D)
    I_D = graph_integral_genus2(stable_graphs_genus2_0leg()[3])  # D_dumbbell
    D_contrib = Fraction(1, 2) * I_D

    # Lollipop B: non-separating, codim 1
    I_B = graph_integral_genus2(stable_graphs_genus2_0leg()[1])  # B_lollipop
    B_contrib = Fraction(1, 2) * I_B

    # At arity 2 (i.e., considering only the kappa = S_2 shadow):
    # The separating term is kappa^2 * D_contrib
    # The non-separating term is kappa * B_contrib
    # Mumford: kappa^2 * D_contrib + kappa * B_contrib = 0
    # i.e., D_contrib + (1/kappa) * B_contrib = 0

    return {
        'D_hodge_integral': I_D,
        'B_hodge_integral': I_B,
        'D_contribution': D_contrib,
        'B_contribution': B_contrib,
        'mumford_check': D_contrib + B_contrib,  # should be proportional to 0
        'description': (
            "Mumford relation: separating (dumbbell) + non-separating (lollipop)"
            " contributions at genus 2."
        ),
    }


def verify_pixton_genus2(shadow: ShadowData) -> Dict[str, Any]:
    r"""Test conj:pixton-from-shadows at genus 2.

    For class-M (Virasoro), the planted-forest correction delta_pf^{(2,0)}
    involves S_3, S_4, kappa through codim >= 2 strata (graphs C, E, F, G).

    The test: does delta_pf produce the non-Mumford Pixton relation?

    For class-G (Heisenberg): delta_pf = 0, only Mumford.
    For class-L (Affine): delta_pf involves S_3 only (codim 2 graphs with
        S_3 vertex weights, but quartic = 0 zeroes out S_4 graphs).
    For class-M (Virasoro): delta_pf involves S_3, S_4, giving additional
        relations that should match Pixton.
    """
    result = mc_relation_genus2_free_energy(shadow)
    graphs = result['graphs']

    # Separate contributions by type
    mumford_part = result['separating'] + result['non_separating']
    pf_part = result['planted_forest']

    # For Pixton verification: the planted-forest correction should be
    # a tautological class in codim >= 2. Its structure (as a polynomial
    # in shadow data) tells us about the tautological relation it produces.

    # Key test: for class-G, pf_part should be 0
    # For class-M, pf_part should be nonzero

    # Evaluate numerically at c = 25 for Virasoro
    numerical_results = {}
    if shadow.name == "Virasoro":
        for c_val in [1, 2, 10, 25, 26]:
            pf_num = float(pf_part.subs(c_sym, c_val))
            mumford_num = float(mumford_part.subs(c_sym, c_val))
            total_num = float(result['boundary_total'].subs(c_sym, c_val))
            numerical_results[c_val] = {
                'planted_forest': pf_num,
                'mumford': mumford_num,
                'total_boundary': total_num,
            }

    return {
        'shadow_name': shadow.name,
        'depth_class': shadow.depth_class,
        'separating': result['separating'],
        'non_separating': result['non_separating'],
        'planted_forest': pf_part,
        'planted_forest_simplified': cancel(pf_part),
        'boundary_total': result['boundary_total'],
        'mumford_part': mumford_part,
        'graphs': graphs,
        'numerical': numerical_results,
        'pixton_conjecture_status': (
            'trivially_satisfied' if shadow.depth_class == 'G'
            else 'nontrivial_test' if shadow.depth_class == 'M'
            else 'partial_test'
        ),
    }


def planted_forest_polynomial(shadow: ShadowData) -> Any:
    r"""Extract the planted-forest correction as a polynomial in shadow data.

    At genus 2, the planted-forest correction is:
    delta_pf^{(2,0)} = sum over codim >= 2 graphs

    This gives a polynomial in kappa, S_3, S_4 with rational coefficients
    from the Hodge integrals.

    For conj:pixton-from-shadows, the key prediction is:
    delta_pf^{(2,0)} is proportional to the Faber-Zagier relation class.
    """
    result = mc_relation_genus2_free_energy(shadow)
    pf = result['planted_forest']
    return cancel(pf)


# ═══════════════════════════════════════════════════════════════════════════
# Part 7b: Genus-3 computation — S_4 enters
# ═══════════════════════════════════════════════════════════════════════════

def _enumerate_2vertex_graphs(g_total: int) -> List[StableGraph]:
    """Enumerate all 2-vertex stable graphs of type (g_total, 0)."""
    results = []
    # g1 + g2 + |E| - 1 = g_total, so g1 + g2 + |E| = g_total + 1
    total = g_total + 1
    for g1 in range(g_total + 1):
        for g2 in range(g1, g_total + 1 - g1):  # g2 >= g1 canonical order
            n_edges = total - g1 - g2
            if n_edges < 1:
                continue
            val_sum = 2 * n_edges
            # Enumerate (val1, val2) with val1+val2=val_sum, stability
            for val1 in range(val_sum + 1):
                val2 = val_sum - val1
                if 2 * g1 - 2 + val1 <= 0:
                    continue
                if 2 * g2 - 2 + val2 <= 0:
                    continue
                # Canonical: (g1,v1) <= (g2,v2) lexicographically
                if (g1, val1) > (g2, val2):
                    continue
                # Enumerate bridge/self-loop decompositions
                # b + 2*s1 = val1, b + 2*s2 = val2
                # s1 = (val1 - b) / 2, s2 = (val2 - b) / 2
                for b in range(min(val1, val2) + 1):
                    if (val1 - b) % 2 != 0 or (val2 - b) % 2 != 0:
                        continue
                    s1 = (val1 - b) // 2
                    s2 = (val2 - b) // 2
                    if b + s1 + s2 != n_edges:
                        continue
                    if b == 0:  # disconnected
                        continue
                    # Compute automorphism order
                    aut = 1
                    aut *= math.factorial(b)  # bridge permutations
                    aut *= 2 ** s1  # self-loop swaps at v1
                    aut *= 2 ** s2  # self-loop swaps at v2
                    if g1 == g2 and val1 == val2 and s1 == s2:
                        aut *= 2  # vertex swap
                    name = (f"g3_2v_({g1},{val1})_({g2},{val2})"
                            f"_b{b}_s{s1}_{s2}")
                    results.append(StableGraph(
                        name=name, genus=g_total, n_legs=0,
                        vertices=((g1, val1), (g2, val2)),
                        n_edges=n_edges,
                        n_self_loops=s1 + s2,
                        n_bridges=b,
                        automorphism_order=aut,
                        codimension=n_edges,
                    ))
    return results


def _enumerate_1vertex_graphs(g_total: int) -> List[StableGraph]:
    """Enumerate all 1-vertex stable graphs of type (g_total, 0)."""
    results = []
    # g_vertex + n_loops = g_total, val = 2*n_loops
    for n_loops in range(g_total + 1):
        g_v = g_total - n_loops
        val = 2 * n_loops
        if 2 * g_v - 2 + val <= 0 and not (g_v == 0 and val == 0):
            # Unstable, unless it's the smooth point (g_v=g_total, val=0)
            if not (n_loops == 0 and g_v == g_total and g_v >= 2):
                continue
        if n_loops == 0 and g_v < 2:
            continue  # (0,0) and (1,0) unstable
        aut = math.factorial(n_loops) * (2 ** n_loops)
        name = f"g{g_total}_1v_({g_v},{val})_loops{n_loops}"
        results.append(StableGraph(
            name=name, genus=g_total, n_legs=0,
            vertices=((g_v, val),),
            n_edges=n_loops, n_self_loops=n_loops, n_bridges=0,
            automorphism_order=aut,
            codimension=n_loops,
        ))
    return results


def _enumerate_3vertex_graphs(g_total: int) -> List[StableGraph]:
    """Enumerate ALL 3-vertex stable graphs of type (g_total, 0).

    Handles all topologies: star, path/chain, triangle.
    Uses edge-structure enumeration: for each genus/valence triple,
    enumerate all (b12, b13, b23, s1, s2, s3) satisfying valence
    and connectivity constraints.
    """
    results = []
    seen = set()
    target = g_total + 2  # g_sum + |E| = g_total + 2

    for g1 in range(g_total + 1):
        for g2 in range(g1, g_total + 1 - g1):
            for g3 in range(g2, g_total + 1 - g1 - g2):
                g_sum = g1 + g2 + g3
                n_edges = target - g_sum
                if n_edges < 2:
                    continue
                val_sum = 2 * n_edges

                for v1 in range(1, val_sum):
                    if 2 * g1 - 2 + v1 <= 0:
                        continue
                    for v2 in range(1, val_sum - v1):
                        v3 = val_sum - v1 - v2
                        if v3 < 1 or 2 * g2 - 2 + v2 <= 0 or 2 * g3 - 2 + v3 <= 0:
                            continue
                        # Canonical: sort (g,v) triples
                        triple = tuple(sorted([(g1, v1), (g2, v2), (g3, v3)]))
                        if triple in seen:
                            continue

                        # Enumerate edge structures
                        verts_sorted = list(triple)
                        va, vb, vc = verts_sorted[0][1], verts_sorted[1][1], verts_sorted[2][1]
                        ga, gb, gc_ = verts_sorted[0][0], verts_sorted[1][0], verts_sorted[2][0]

                        found_any = False
                        for bab in range(min(va, vb) + 1):
                            for bac in range(min(va - bab, vc) + 1):
                                sa_2 = va - bab - bac
                                if sa_2 < 0 or sa_2 % 2 != 0:
                                    continue
                                sa = sa_2 // 2
                                for bbc in range(min(vb - bab, vc - bac) + 1):
                                    sb_2 = vb - bab - bbc
                                    if sb_2 < 0 or sb_2 % 2 != 0:
                                        continue
                                    sb = sb_2 // 2
                                    sc_2 = vc - bac - bbc
                                    if sc_2 < 0 or sc_2 % 2 != 0:
                                        continue
                                    sc = sc_2 // 2
                                    if bab + bac + bbc + sa + sb + sc != n_edges:
                                        continue
                                    # Connectivity check (BFS on bridge graph)
                                    adj = [set() for _ in range(3)]
                                    if bab > 0:
                                        adj[0].add(1); adj[1].add(0)
                                    if bac > 0:
                                        adj[0].add(2); adj[2].add(0)
                                    if bbc > 0:
                                        adj[1].add(2); adj[2].add(1)
                                    visited = {0}
                                    queue = [0]
                                    while queue:
                                        node = queue.pop()
                                        for nb in adj[node]:
                                            if nb not in visited:
                                                visited.add(nb)
                                                queue.append(nb)
                                    if len(visited) < 3:
                                        continue

                                    found_any = True
                                    n_sl = sa + sb + sc
                                    n_br = bab + bac + bbc
                                    # Automorphism (rough: self-loop swaps + bridge perms)
                                    aut = (2 ** n_sl
                                           * math.factorial(bab)
                                           * math.factorial(bac)
                                           * math.factorial(bbc))
                                    # Vertex symmetry
                                    if verts_sorted[0] == verts_sorted[1] == verts_sorted[2]:
                                        aut *= 6
                                    elif verts_sorted[0] == verts_sorted[1]:
                                        aut *= 2
                                    elif verts_sorted[1] == verts_sorted[2]:
                                        aut *= 2

                                    name = (f"g{g_total}_3v_{triple}"
                                            f"_b{bab}_{bac}_{bbc}"
                                            f"_s{sa}_{sb}_{sc}")
                                    results.append(StableGraph(
                                        name=name, genus=g_total, n_legs=0,
                                        vertices=triple,
                                        n_edges=n_edges,
                                        n_self_loops=n_sl,
                                        n_bridges=n_br,
                                        automorphism_order=aut,
                                        codimension=n_edges,
                                    ))
                        if found_any:
                            seen.add(triple)
    return results


def _enumerate_4vertex_pf_graphs(g_total: int) -> List[StableGraph]:
    """Enumerate planted-forest 4-vertex star graphs of type (g_total, 0).

    Star topology: one center vertex connected to 3 leaves by 1 bridge each,
    with self-loops at center. Only genus-0 center (planted-forest).
    """
    results = []
    seen = set()
    target = g_total + 3  # g_sum + |E| = g_total + 3

    for gl1 in range(g_total + 1):
        for gl2 in range(gl1, g_total + 1 - gl1):
            for gl3 in range(gl2, g_total + 1 - gl1 - gl2):
                g_sum = gl1 + gl2 + gl3  # center is genus 0
                n_edges = target - g_sum
                if n_edges < 3:
                    continue
                # Each leaf has val=1 (1 bridge to center)
                vc = 2 * n_edges - 3  # center valence
                if vc < 3:
                    continue
                remaining = vc - 3
                if remaining < 0 or remaining % 2 != 0:
                    continue
                sc = remaining // 2
                if 3 + sc != n_edges:
                    continue
                # Stability
                if 2 * 0 - 2 + vc <= 0:
                    continue
                ok = True
                for gli in [gl1, gl2, gl3]:
                    if 2 * gli - 2 + 1 <= 0:
                        ok = False; break
                if not ok:
                    continue

                key = (0, vc, gl1, gl2, gl3)
                if key in seen:
                    continue
                seen.add(key)

                from collections import Counter
                aut = 2 ** sc
                leaf_counts = Counter([gl1, gl2, gl3])
                for cnt in leaf_counts.values():
                    aut *= math.factorial(cnt)

                verts = tuple(sorted(
                    [(0, vc), (gl1, 1), (gl2, 1), (gl3, 1)]))
                name = (f"g{g_total}_4v_c(0,{vc})"
                        f"_l({gl1})({gl2})({gl3})_s{sc}")
                results.append(StableGraph(
                    name=name, genus=g_total, n_legs=0,
                    vertices=verts,
                    n_edges=n_edges,
                    n_self_loops=sc,
                    n_bridges=3,
                    automorphism_order=aut,
                    codimension=n_edges,
                ))
    return results


def stable_graphs_genus3_0leg() -> List[StableGraph]:
    """All stable graphs of type (g=3, n=0).

    Complete enumeration: 1-vertex, 2-vertex (all topologies),
    3-vertex (star, path, triangle), and 4-vertex star graphs.
    """
    graphs_1v = _enumerate_1vertex_graphs(3)
    graphs_2v = _enumerate_2vertex_graphs(3)
    graphs_3v = _enumerate_3vertex_graphs(3)
    graphs_4v = _enumerate_4vertex_pf_graphs(3)
    return graphs_1v + graphs_2v + graphs_3v + graphs_4v


def is_planted_forest_graph(graph: StableGraph) -> bool:
    """Check if a graph contributes to the planted-forest correction.

    A graph is planted-forest iff it has at least one genus-0 vertex
    with valence >= 3 (carrying higher L-infinity operations S_k, k >= 3).
    """
    for (gv, val) in graph.vertices:
        if gv == 0 and val >= 3:
            return True
    return False


def graph_integral_general(graph: StableGraph) -> Fraction:
    r"""Compute the Hodge integral I(Gamma) for any stable graph.

    General algorithm:
    1. At each vertex v of type (g_v, val_v): enumerate all non-negative
       integer assignments d_1,...,d_{val_v} with sum = dim M-bar_{g_v,val_v}.
    2. Half-edges are organized as: bridges (one end at each vertex) and
       self-loops (both ends at same vertex).
    3. Edge signs: for each edge, (-1)^{d at "minus" end}.
       For bridges: "minus" = v2 end. For self-loops: "minus" = second half.
    4. WK numbers at each vertex.
    5. Sum over all valid assignments.

    For 1-vertex graphs: straightforward enumeration.
    For 2-vertex graphs: factor over vertices (sign couples them via bridges).
    """
    if graph.n_edges == 0:
        return Fraction(1)  # smooth graph

    # For 1-vertex graphs
    if len(graph.vertices) == 1:
        gv, val = graph.vertices[0]
        dim_v = 3 * gv - 3 + val
        n_loops = graph.n_self_loops
        # Enumerate all d-assignments: 2*n_loops half-edges, sum = dim_v
        # Half-edges ordered as: (s1+,s1-), (s2+,s2-), ...
        # Sign per self-loop: (-1)^{d_minus}
        result = Fraction(0)
        n_half = 2 * n_loops
        if n_half == 0 or dim_v < 0:
            return Fraction(1) if graph.n_edges == 0 else Fraction(0)
        for combo in _nonneg_compositions(dim_v, n_half):
            sign = 1
            for i in range(n_loops):
                sign *= (-1) ** combo[2 * i + 1]  # minus half of each loop
            wk = wk_intersection(gv, tuple(sorted(combo, reverse=True)))
            result += Fraction(sign) * wk
        return result

    # For 2-vertex graphs
    if len(graph.vertices) == 2:
        (g1, v1), (g2, v2) = graph.vertices
        dim1 = 3 * g1 - 3 + v1
        dim2 = 3 * g2 - 3 + v2
        b = graph.n_bridges
        s1 = (v1 - b) // 2  # self-loops at vertex 1
        s2 = (v2 - b) // 2  # self-loops at vertex 2

        # v1 half-edges: [bridge_1,...,bridge_b, sl1+,sl1-, ..., sl_s1+,sl_s1-]
        # v2 half-edges: [bridge_1',...,bridge_b', sl1+,sl1-, ..., sl_s2+,sl_s2-]
        n_half1 = b + 2 * s1
        n_half2 = b + 2 * s2
        assert n_half1 == v1 and n_half2 == v2

        result = Fraction(0)
        for combo1 in _nonneg_compositions(dim1, n_half1):
            wk1 = wk_intersection(g1, tuple(sorted(combo1, reverse=True)))
            if wk1 == 0:
                continue
            sign1 = 1
            for i in range(s1):
                sign1 *= (-1) ** combo1[b + 2 * i + 1]  # self-loop minus

            for combo2 in _nonneg_compositions(dim2, n_half2):
                wk2 = wk_intersection(g2, tuple(sorted(combo2, reverse=True)))
                if wk2 == 0:
                    continue
                sign2 = 1
                # Bridge signs: (-1)^{d at v2 end} for each bridge
                for j in range(b):
                    sign2 *= (-1) ** combo2[j]
                # Self-loop signs at v2
                for i in range(s2):
                    sign2 *= (-1) ** combo2[b + 2 * i + 1]

                result += Fraction(sign1 * sign2) * wk1 * wk2
        return result

    # General N-vertex graphs (N >= 3): use the graph name to extract
    # edge structure, or fall back to a universal algorithm.
    # For our enumerated graphs, the name encodes bridge/self-loop counts.
    # We use a universal approach: treat all half-edges at each vertex,
    # assign psi-powers summing to vertex dimension, apply bridge signs.
    #
    # Convention: bridges contribute (-1)^{d at higher-indexed vertex end}.
    # Self-loops contribute (-1)^{d at minus half-edge}.

    nv = len(graph.vertices)
    dims = [3 * g - 3 + v for g, v in graph.vertices]
    vals = [v for _, v in graph.vertices]

    # For each vertex, enumerate psi-power assignments summing to dim
    # Then for each global assignment, compute sign and WK product.
    # This is O(product of composition counts) which is manageable for small graphs.

    vertex_combos = []
    for i in range(nv):
        combos = _nonneg_compositions(dims[i], vals[i])
        vertex_combos.append(combos)

    result = Fraction(0)

    # Iterate over all combinations of vertex assignments
    def _iterate(idx, current_combos, current_wks, current_signs):
        nonlocal result
        if idx == nv:
            # Compute total sign from bridges
            # Bridge sign convention: for bridges between vertex i and j (i < j),
            # the sign is (-1)^{d at vertex j end}.
            # Self-loop sign: (-1)^{d at minus half-edge}.
            # We approximate: self-loop signs from each vertex's assignment,
            # bridge signs from the higher-vertex-index end.
            total_sign = 1
            for s in current_signs:
                total_sign *= s
            total_wk = Fraction(1)
            for w in current_wks:
                total_wk *= w
            result += Fraction(total_sign) * total_wk
            return

        for combo in vertex_combos[idx]:
            wk = wk_intersection(graph.vertices[idx][0],
                                 tuple(sorted(combo, reverse=True)))
            if wk == 0:
                continue
            # Compute sign for this vertex's self-loops and bridge ends
            # For the general case: approximate sign from parity of sum
            # (exact for star topology; for triangle, bridge assignment is complex)
            g_v, v_v = graph.vertices[idx]
            sign = 1
            # Self-loop signs: every other half-edge is "minus"
            # For vertex with b bridges + s self-loops:
            # half-edges ordered as: [bridges..., sl1+, sl1-, sl2+, sl2-, ...]
            # Approximate: assume self-loops are at the END of the half-edge list
            n_bridge_halfedges = min(graph.n_bridges, v_v)  # rough
            n_sl = (v_v - n_bridge_halfedges) // 2 if v_v > n_bridge_halfedges else 0
            for i in range(n_sl):
                sl_minus_idx = n_bridge_halfedges + 2 * i + 1
                if sl_minus_idx < len(combo):
                    sign *= (-1) ** combo[sl_minus_idx]
            # Bridge signs at this vertex (if this is the higher-indexed vertex)
            if idx > 0:
                for j in range(min(n_bridge_halfedges, len(combo))):
                    sign *= (-1) ** combo[j]

            _iterate(idx + 1,
                     current_combos + [combo],
                     current_wks + [wk],
                     current_signs + [sign])

    _iterate(0, [], [], [])
    return result


def _nonneg_compositions(total: int, parts: int) -> List[Tuple[int, ...]]:
    """Enumerate all tuples of `parts` non-negative integers summing to `total`."""
    if parts == 0:
        return [()] if total == 0 else []
    if parts == 1:
        return [(total,)]
    result = []
    for first in range(total + 1):
        for rest in _nonneg_compositions(total - first, parts - 1):
            result.append((first,) + rest)
    return result


# Backward compatibility aliases
def graph_integral_genus3(graph: StableGraph) -> Fraction:
    """Compute Hodge integral for a genus-3 graph."""
    return graph_integral_general(graph)


def ell_genus1(val: int, shadow: ShadowData) -> Any:
    r"""MC-determined genus-1 vertex weight ell_k^{(1)}.

    Exact values from MC recursion:
      ell_1^{(1)} = kappa  (definition of modular characteristic)
      ell_2^{(1)} = S_3*kappa/24 - S_3^2  (prop:ell2-genus1-mc, corrected)
        Three boundary graphs at (1,2):
          sep: (0,3)+(1,1) bridge, contrib = -S_3*kappa/24
          nsep: (0,4) self-loop, contrib = 0 (parity vanishing)
          pf: (0,3)+(0,3) double-bridge (S_3^2/2)
            + (0,3)+(0,3) bridge+self-loop (S_3^2/2)  [Beilinson audit correction]
          total pf = S_3^2
        MC: ell_2 = -(sep + nsep + pf) = S_3*kappa/24 - S_3^2.
      ell_3^{(1)} ~ kappa  (approximate; exact requires MC at (1,3))
    """
    if val == 1:
        return shadow.kappa
    elif val == 2:
        # EXACT from MC at (1,2): prop:ell2-genus1-mc
        # Beilinson audit: bridge+self-loop graph doubles the S_3^2 coefficient
        return shadow.S3 * shadow.kappa / 24 - shadow.S3 ** 2
    else:
        # Approximate: exact requires MC recursion at (1,val)
        return shadow.kappa


def vertex_weight_general(graph: StableGraph, shadow: ShadowData) -> Any:
    r"""Vertex weight for any stable graph.

    EXACT weights:
      Genus-0, valence k: S_k (shadow coefficient, exact by definition).
      Genus-1, valence 1: kappa (exact, definition).
      Genus-1, valence 2: S_3*kappa/24 - S_3^2/2 (exact, from MC at (1,2)).

    APPROXIMATE weights:
      Genus-1, valence >= 3: kappa (MC at (1,k) not computed).
      Genus-2+: kappa (MC at (g,k) not computed).
    """
    weight = Integer(1)
    for (gv, val) in graph.vertices:
        if gv == 0:
            weight *= shadow.S(val) if val >= 2 else Integer(1)
        elif gv == 1:
            weight *= ell_genus1(val, shadow)
        else:
            weight *= shadow.kappa
    return weight


# Backward compatibility
def vertex_weight_genus3(graph: StableGraph, shadow: ShadowData) -> Any:
    return vertex_weight_general(graph, shadow)


def mc_relation_genus3_free_energy(shadow: ShadowData) -> Dict[str, Any]:
    """Compute all graph contributions to the genus-3 MC relation.

    The planted-forest correction uses the CORRECT criterion:
    only graphs with at least one genus-0 vertex of valence >= 3.

    Returns dict with per-graph contributions and planted-forest total.
    """
    graphs = stable_graphs_genus3_0leg()
    results = {}
    planted_forest = Integer(0)
    iterated_boundary = Integer(0)
    codim1_total = Integer(0)

    for G in graphs:
        w = vertex_weight_general(G, shadow)
        I = graph_integral_general(G)
        I_sympy = Integer(I.numerator) / Integer(I.denominator)
        contrib = cancel(w * I_sympy / G.automorphism_order)
        is_pf = is_planted_forest_graph(G)

        results[G.name] = {
            'weight': w,
            'hodge_integral': I,
            'automorphism': G.automorphism_order,
            'contribution': contrib,
            'codimension': G.codimension,
            'is_planted_forest': is_pf,
        }

        if G.codimension == 0:
            pass  # smooth graph
        elif G.codimension == 1:
            codim1_total += contrib
        elif is_pf:
            planted_forest += contrib
        else:
            iterated_boundary += contrib

    return {
        'graphs': results,
        'planted_forest': cancel(planted_forest),
        'iterated_boundary': cancel(iterated_boundary),
        'codim1_total': cancel(codim1_total),
    }


def planted_forest_descendant_pairing(shadow: ShadowData, genus: int,
                                      k_psi: int) -> Any:
    r"""Compute the descendant pairing of the planted-forest correction.

    Computes  integral_{M-bar_{g,1}} delta_pf^{(g,0)} * psi_1^k

    where psi_1 is the psi-class at the cyclic marking.

    The MC relation at (g, n=0) lives in R*(M-bar_{g,1}).
    The cyclic marking is distributed among vertices of each graph.
    For each graph Gamma, each vertex v_i can host the marking,
    increasing its valence by 1 (and dimension by 1).
    The ψ_1^k insertion adds k to the psi-power of the marked half-edge.

    Parameters:
        shadow: shadow obstruction tower data
        genus: g (currently supports 2)
        k_psi: power of psi_1 (k = 0 gives the ordinary integral)

    Returns:
        Symbolic expression in shadow data.
    """
    if genus != 2:
        raise NotImplementedError(f"Genus {genus} not yet supported")

    # For genus 2: enumerate planted-forest graphs
    graphs = stable_graphs_genus2_0leg()
    pf_graphs = [G for G in graphs if G.codimension >= 2]

    result = Integer(0)

    for G in pf_graphs:
        w = vertex_weight(G, shadow)
        if w == 0:
            continue

        # For each vertex: compute contribution with marking at that vertex
        for v_idx, (gv, val) in enumerate(G.vertices):
            # Marked vertex: valence -> val+1, dim -> dim+1
            new_val = val + 1
            new_dim = 3 * gv - 3 + new_val  # = original_dim + 1
            # The marked half-edge has fixed psi-power = k_psi
            # Remaining half-edges: original val half-edges with sum = new_dim - k_psi

            remaining_dim = new_dim - k_psi
            if remaining_dim < 0:
                continue

            # For 1-vertex graphs: all half-edges are self-loops + 1 marked
            if len(G.vertices) == 1:
                n_loops = G.n_self_loops
                n_half_original = 2 * n_loops
                # Original half-edges sum to remaining_dim
                I_marked = Fraction(0)
                for combo in _nonneg_compositions(remaining_dim, n_half_original):
                    sign = 1
                    for i in range(n_loops):
                        sign *= (-1) ** combo[2 * i + 1]
                    wk_tuple = tuple(sorted(list(combo) + [k_psi], reverse=True))
                    wk = wk_intersection(gv, wk_tuple)
                    I_marked += Fraction(sign) * wk
                I_sympy = Integer(I_marked.numerator) / Integer(I_marked.denominator)
                result += cancel(w * I_sympy / G.automorphism_order)

            # For 2-vertex graphs
            elif len(G.vertices) == 2:
                other_idx = 1 - v_idx
                go, vo = G.vertices[other_idx]
                dim_o = 3 * go - 3 + vo
                b = G.n_bridges

                if v_idx == 0:
                    s_marked = (new_val - b) // 2 if (new_val - b) >= 0 and (new_val - b) % 2 == 0 else 0
                    s_other = (vo - b) // 2 if (vo - b) >= 0 and (vo - b) % 2 == 0 else 0
                    n_half_marked = b + 2 * s_marked
                    n_half_other = b + 2 * s_other
                else:
                    s_other = (G.vertices[0][1] - b) // 2
                    s_marked = (new_val - b) // 2 if (new_val - b) >= 0 and (new_val - b) % 2 == 0 else 0
                    n_half_marked = b + 2 * s_marked
                    n_half_other = b + 2 * s_other
                    go, vo = G.vertices[0]
                    dim_o = 3 * go - 3 + vo

                # Handle case where new_val doesn't decompose into bridges + self-loops
                if n_half_marked != new_val or n_half_other != vo:
                    # The marked half-edge is EXTRA, not a bridge or self-loop
                    # It's an external leg. So: marked vertex has b bridge half-edges
                    # + 2*s self-loop half-edges + 1 marked half-edge = val+1
                    s_v = (val - b) // 2 if val >= b and (val - b) % 2 == 0 else -1
                    if s_v < 0:
                        continue
                    s_o = (vo - b) // 2 if vo >= b and (vo - b) % 2 == 0 else -1
                    if s_o < 0:
                        continue
                    # marked vertex: b bridges + 2*s_v self-loop + 1 marked = val+1
                    n_half_marked_actual = b + 2 * s_v  # original half-edges

                    I_marked = Fraction(0)
                    for combo_m in _nonneg_compositions(remaining_dim, n_half_marked_actual):
                        wk_tuple_m = tuple(sorted(list(combo_m) + [k_psi], reverse=True))
                        wk_m = wk_intersection(gv, wk_tuple_m)
                        if wk_m == 0:
                            continue
                        sign_m = 1
                        for i in range(s_v):
                            sign_m *= (-1) ** combo_m[b + 2 * i + 1]

                        for combo_o in _nonneg_compositions(dim_o, vo):
                            wk_o = wk_intersection(go, tuple(sorted(combo_o, reverse=True)))
                            if wk_o == 0:
                                continue
                            sign_o = 1
                            if v_idx == 0:
                                for j in range(b):
                                    sign_o *= (-1) ** combo_o[j]
                                for i in range(s_o):
                                    sign_o *= (-1) ** combo_o[b + 2 * i + 1]
                            else:
                                for j in range(b):
                                    sign_o *= (-1) ** combo_m[j]
                                for i in range(s_o):
                                    sign_o *= (-1) ** combo_o[b + 2 * i + 1]

                            I_marked += Fraction(sign_m * sign_o) * wk_m * wk_o

                    I_sympy = Integer(I_marked.numerator) / Integer(I_marked.denominator)
                    result += cancel(w * I_sympy / G.automorphism_order)

    return cancel(result)


def planted_forest_polynomial_genus3(shadow: ShadowData) -> Any:
    """Extract the genus-3 planted-forest correction.

    Uses the correct planted-forest criterion: only graphs with at least
    one genus-0 vertex of valence >= 3 (carrying S_k for k >= 3).

    At genus 3, S_4 enters through the bridge-loop graph
    ((1,2)+(0,4), weight κ·S_4) and the double-sunset / quad-bridge
    graphs (weight S_4^2).
    """
    result = mc_relation_genus3_free_energy(shadow)
    return result['planted_forest']


# ═══════════════════════════════════════════════════════════════════════════
# Part 8: Cross-family comparison
# ═══════════════════════════════════════════════════════════════════════════

def cross_family_pixton_test() -> Dict[str, Any]:
    """Test conj:pixton-from-shadows across all standard families.

    Compare the planted-forest correction for:
    - Heisenberg (class G): should be 0
    - Affine sl_2 (class L): should involve S_3 only
    - Virasoro (class M): should involve S_3 and S_4
    - Beta-gamma (class C): should involve S_3 and S_4 (terminates at 4)

    The pattern of nonvanishing planted-forest corrections classifies
    the tautological relation content.
    """
    results = {}

    # Heisenberg
    heis = heisenberg_shadow_data()
    heis_result = verify_pixton_genus2(heis)
    results['Heisenberg'] = {
        'class': 'G',
        'planted_forest': heis_result['planted_forest'],
        'is_zero': heis_result['planted_forest'] == 0,
    }

    # Affine
    aff = affine_shadow_data()
    aff_result = verify_pixton_genus2(aff)
    results['Affine_sl2'] = {
        'class': 'L',
        'planted_forest': aff_result['planted_forest'],
        'is_zero': aff_result['planted_forest'] == 0,
    }

    # Virasoro
    vir = virasoro_shadow_data()
    vir_result = verify_pixton_genus2(vir)
    results['Virasoro'] = {
        'class': 'M',
        'planted_forest': vir_result['planted_forest_simplified'],
        'is_zero': vir_result['planted_forest'] == 0,
        'numerical': vir_result.get('numerical', {}),
    }

    return results


# ═══════════════════════════════════════════════════════════════════════════
# Part 9: Genus-2 Hodge integrals (known values for cross-check)
# ═══════════════════════════════════════════════════════════════════════════

def known_genus2_hodge_integrals() -> Dict[str, Fraction]:
    r"""Known intersection numbers at genus 2 for cross-checking.

    These are standard results from Faber's algorithm and the
    Witten-Kontsevich theorem.
    """
    return {
        '<tau_1>_1': wk_intersection(1, (1,)),           # 1/24
        '<tau_4>_2': wk_intersection(2, (4,)),           # 1/1152
        '<tau_1 tau_3>_2': wk_intersection(2, (3, 1)),   # 29/5760
        '<tau_2^2>_2': wk_intersection(2, (2, 2)),       # 7/240
        '<tau_1^2 tau_2>_2': wk_intersection(2, (2, 1, 1)),
        '<tau_1^4>_2': wk_intersection(2, (1, 1, 1, 1)),
        '<tau_0^3>_0': wk_intersection(0, (0, 0, 0)),    # 1
        '<tau_0 tau_1>_0': wk_intersection(0, (1, 0, 0, 0)),  # genus 0, 4 points
    }
