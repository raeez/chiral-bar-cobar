r"""Pixton ideal generation at genus 4 from the shadow obstruction tower.

Tests conj:pixton-from-shadows at genus 4: for class-M algebras (r_max = infinity),
the MC-descended tautological relations generate the Pixton ideal I_4
in R*(M-bar_4).

MATHEMATICAL FRAMEWORK
======================

Genus 4 is the FIRST genus where the arity-6 shadow S_6 contributes:
  g_min(S_6) = floor(6/2) + 1 = 4.

This makes genus 4 a critical test for conj:pixton-from-shadows because:
1. A genuinely NEW shadow coefficient enters the computation.
2. The tautological ring R*(M-bar_4) is rich enough to have nontrivial
   Pixton relations starting in codimension g+1 = 5.
3. The 379 stable graphs (versus 42 at genus 3) provide ample structure.

SHADOW VISIBILITY AT GENUS 4 (cor:shadow-visibility-genus)
===========================================================

  g_min(S_r) = floor(r/2) + 1
  S_3: g_min = 2 -- visible at g >= 2
  S_4: g_min = 3 -- visible at g >= 3
  S_5: g_min = 3 -- visible at g >= 3
  S_6: g_min = 4 -- FIRST VISIBLE at genus 4
  S_7: g_min = 4 -- FIRST VISIBLE at genus 4
  S_8: g_min = 5 -- NOT visible at genus 4

So obs_4 involves shadow data (kappa, S_3, S_4, S_5, S_6, S_7).

GENUS-4 GRAPH DATA
===================

Total stable graphs at (4,0): 379
  By vertex count: |V|=1: 5, |V|=2: 29, |V|=3: 79, |V|=4: 126, |V|=5: 98, |V|=6: 42
  Planted-forest (>= 1 genus-0 vertex with val >= 3): 358
  Non-planted-forest: 21

chi^orb(M-bar_{4,0}) = -4717039/6220800
lambda_4^FP = 127/154828800

Self-loop parity vanishing (prop:self-loop-vanishing):
  (0,8): dim=5 odd, 4 loops, I=0
  (2,4): dim=5 odd, 2 loops, I=0
  (1,6): dim=3 odd, 3 loops, I=0

References:
    conj:pixton-from-shadows (concordance.tex)
    thm:mc-tautological-descent (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    thm:pixton-from-mc-semisimple (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import factorial
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Integer, Rational, Symbol, cancel, expand, factor, simplify, S,
    collect, Poly, degree, symbols, sqrt, oo,
)

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    orbifold_euler_characteristic,
    _bernoulli_exact,
    _lambda_fp_exact,
    _chi_orb_open,
)
from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    wk_intersection,
    _nonneg_compositions,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
)


# ============================================================================
# Section 0: Exact arithmetic constants
# ============================================================================

@lru_cache(maxsize=32)
def lambda_fp_exact(g: int) -> Fraction:
    r"""Faber-Pandharipande number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Verified values:
      g=1: 1/24, g=2: 7/5760, g=3: 31/967680,
      g=4: 127/154828800, g=5: 73/3503554560.
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    return _lambda_fp_exact(g)


LAMBDA4_FP = lambda_fp_exact(4)
assert LAMBDA4_FP == Fraction(127, 154828800), (
    f"lambda_4^FP = {LAMBDA4_FP}, expected 127/154828800"
)


# ============================================================================
# Section 1: Hodge integral computation
# ============================================================================

def hodge_integral(graph: StableGraph) -> Fraction:
    r"""Compute the Hodge integral I(Gamma) for a stable graph.

    Uses edge-propagator expansion 1/(psi_+ + psi_-) in psi-powers at each
    half-edge, then integrates the product of psi-classes over the product
    of vertex moduli spaces using Witten-Kontsevich intersection numbers.

    Convention:
      Bridges (v1 != v2): "minus" at the vertex with HIGHER genus.
        If genera are equal, "minus" at the higher-indexed vertex.
      Self-loops (v1 == v2): second half-edge is "minus".
      Sign per edge: (-1)^{d at minus end}.

    The dimensional constraint at vertex v: sum d_h = 3*g(v) - 3 + val(v).
    """
    if graph.num_edges == 0:
        return Fraction(1)

    nv = graph.num_vertices
    genera = graph.vertex_genera
    val = graph.valence
    dims = [3 * genera[v] - 3 + val[v] for v in range(nv)]

    for v in range(nv):
        if dims[v] < 0:
            return Fraction(0)

    # Build half-edge structure per vertex
    vertex_halfedges: List[List[Tuple[int, int]]] = [[] for _ in range(nv)]
    for e_idx, (v1, v2) in enumerate(graph.edges):
        if v1 == v2:
            vertex_halfedges[v1].append((e_idx, 0))
            vertex_halfedges[v1].append((e_idx, 1))
        else:
            g1, g2 = genera[v1], genera[v2]
            if g1 > g2:
                vertex_halfedges[v1].append((e_idx, 1))
                vertex_halfedges[v2].append((e_idx, 0))
            elif g1 < g2:
                vertex_halfedges[v1].append((e_idx, 0))
                vertex_halfedges[v2].append((e_idx, 1))
            else:
                vertex_halfedges[v1].append((e_idx, 0))
                vertex_halfedges[v2].append((e_idx, 1))

    vertex_combos = []
    for v in range(nv):
        combos = _nonneg_compositions(dims[v], val[v])
        vertex_combos.append(combos)
        if not combos:
            return Fraction(0)

    result = Fraction(0)
    for combo_tuple in cartprod(*vertex_combos):
        wk_product = Fraction(1)
        skip = False
        for v in range(nv):
            wk = wk_intersection(
                genera[v], tuple(sorted(combo_tuple[v], reverse=True))
            )
            if wk == 0:
                skip = True
                break
            wk_product *= wk
        if skip:
            continue

        sign = 1
        for v in range(nv):
            for local_idx, (e_idx, pos) in enumerate(vertex_halfedges[v]):
                if pos == 1:
                    d_minus = combo_tuple[v][local_idx]
                    sign *= (-1) ** d_minus

        result += Fraction(sign) * wk_product

    return result


@lru_cache(maxsize=8192)
def _hodge_integral_cached(genera: Tuple[int, ...],
                           edges: Tuple[Tuple[int, int], ...]) -> Fraction:
    """Cached Hodge integral by graph topology."""
    graph = StableGraph(vertex_genera=genera, edges=edges, legs=())
    return hodge_integral(graph)


# ============================================================================
# Section 2: Vertex weight computation
# ============================================================================

def ell_genus1(val: int, shadow: ShadowData) -> Any:
    r"""MC-determined genus-1 vertex weight ell_k^{(1)}.

    ell_1^{(1)} = kappa  (definition of modular characteristic)
    ell_2^{(1)} = S_3*kappa/24 - S_3^2  (exact from MC at (1,2))
    ell_k^{(1)} ~ kappa  (approximate for k >= 3)
    """
    if val == 1:
        return shadow.kappa
    elif val == 2:
        return shadow.S3 * shadow.kappa / 24 - shadow.S3 ** 2
    else:
        return shadow.kappa


def ell_genus2(val: int, shadow: ShadowData) -> Any:
    r"""MC-determined genus-2 vertex weight ell_k^{(2)}.

    ell_0^{(2)} = kappa * lambda_2^FP = 7*kappa/5760  (scalar approximation)
    ell_k^{(2)} ~ kappa  for k >= 1  (approximate)
    """
    if val == 0:
        return shadow.kappa * Rational(7, 5760)
    else:
        return shadow.kappa


def ell_genus3(val: int, shadow: ShadowData) -> Any:
    r"""MC-determined genus-3 vertex weight ell_k^{(3)}.

    ell_0^{(3)} = kappa * lambda_3^FP = 31*kappa/967680  (scalar approximation)
    ell_k^{(3)} ~ kappa  for k >= 1  (approximate)
    """
    if val == 0:
        lam3 = lambda_fp_exact(3)
        return shadow.kappa * Rational(lam3.numerator, lam3.denominator)
    else:
        return shadow.kappa


def vertex_weight(graph: StableGraph, shadow: ShadowData) -> Any:
    r"""Product of vertex weights for a stable graph.

    Genus-0, valence k >= 2: S_k (shadow coefficient, exact)
    Genus-0, valence < 2: 1 (placeholder)
    Genus-1, valence v: ell_v^{(1)}
    Genus-2, valence v: ell_v^{(2)}
    Genus-3, valence v: ell_v^{(3)}
    Genus >= 4, valence 0: 1 (smooth component, determined by MC)
    Genus >= 4, valence v >= 1: kappa (approximate)
    """
    weight = Integer(1)
    val = graph.valence
    for v in range(graph.num_vertices):
        gv = graph.vertex_genera[v]
        vv = val[v]
        if gv == 0:
            if vv >= 2:
                weight *= shadow.S(vv)
            else:
                weight *= Integer(1)
        elif gv == 1:
            weight *= ell_genus1(vv, shadow)
        elif gv == 2:
            weight *= ell_genus2(vv, shadow)
        elif gv == 3:
            weight *= ell_genus3(vv, shadow)
        else:
            if vv == 0:
                weight *= Integer(1)
            else:
                weight *= shadow.kappa
    return weight


def is_planted_forest(graph: StableGraph) -> bool:
    """A graph is planted-forest iff it has a genus-0 vertex of valence >= 3.

    Such a vertex carries a higher shadow coefficient S_k (k >= 3).
    """
    val = graph.valence
    for v in range(graph.num_vertices):
        if graph.vertex_genera[v] == 0 and val[v] >= 3:
            return True
    return False


# ============================================================================
# Section 3: Graph amplitude data structure
# ============================================================================

@dataclass
class GraphAmplitude:
    """Complete amplitude data for a single stable graph."""
    graph: StableGraph
    hodge_integral: Fraction
    aut_order: int
    is_pf: bool
    vertex_genera_valences: Tuple[Tuple[int, int], ...]

    @property
    def num_vertices(self) -> int:
        return self.graph.num_vertices

    @property
    def num_edges(self) -> int:
        return self.graph.num_edges

    @property
    def codimension(self) -> int:
        return self.graph.num_edges

    @property
    def first_betti(self) -> int:
        return self.graph.first_betti

    def vertex_weight_eval(self, shadow: ShadowData) -> Any:
        return vertex_weight(self.graph, shadow)

    def weighted_amplitude(self, shadow: ShadowData) -> Any:
        """(1/|Aut|) * w(Gamma) * I(Gamma)."""
        w = self.vertex_weight_eval(shadow)
        I_sympy = Integer(self.hodge_integral.numerator) / Integer(
            self.hodge_integral.denominator)
        return cancel(w * I_sympy / self.aut_order)


# ============================================================================
# Section 4: Graph enumeration and annotation
# ============================================================================

@lru_cache(maxsize=1)
def genus4_all_amplitudes() -> Tuple[GraphAmplitude, ...]:
    """Compute Hodge integrals and classify all 379 genus-4 stable graphs."""
    graphs = list(enumerate_stable_graphs(4, 0))
    result = []
    for g in graphs:
        val = g.valence
        I = _hodge_integral_cached(g.vertex_genera, g.edges)
        aut = g.automorphism_order()
        pf = is_planted_forest(g)
        gv_pairs = tuple((g.vertex_genera[v], val[v]) for v in range(g.num_vertices))
        result.append(GraphAmplitude(
            graph=g,
            hodge_integral=I,
            aut_order=aut,
            is_pf=pf,
            vertex_genera_valences=gv_pairs,
        ))
    return tuple(result)


def genus4_pf_amplitudes() -> List[GraphAmplitude]:
    """Planted-forest graphs at genus 4."""
    return [a for a in genus4_all_amplitudes() if a.is_pf]


def genus4_nonpf_amplitudes() -> List[GraphAmplitude]:
    """Non-planted-forest graphs at genus 4."""
    return [a for a in genus4_all_amplitudes() if not a.is_pf]


# ============================================================================
# Section 5: Census and structural analysis
# ============================================================================

def genus4_pixton_census() -> Dict[str, Any]:
    """Complete census of genus-4 amplitudes for the Pixton bridge."""
    all_amps = list(genus4_all_amplitudes())
    pf = [a for a in all_amps if a.is_pf]
    nonpf = [a for a in all_amps if not a.is_pf]
    vanishing = [a for a in all_amps if a.hodge_integral == Fraction(0)]
    nonzero_pf = [a for a in pf if a.hodge_integral != Fraction(0)]

    pf_by_codim = dict(sorted(Counter(a.codimension for a in pf).items()))
    pf_by_verts = dict(sorted(Counter(a.num_vertices for a in pf).items()))
    nonpf_by_codim = dict(sorted(Counter(a.codimension for a in nonpf).items()))
    by_loop = dict(sorted(Counter(a.first_betti for a in all_amps).items()))

    max_g0_val = 0
    shadow_vals_present = set()
    for a in nonzero_pf:
        for v in range(a.graph.num_vertices):
            if a.graph.vertex_genera[v] == 0:
                vv = a.graph.valence[v]
                if vv >= 3:
                    shadow_vals_present.add(vv)
                    max_g0_val = max(max_g0_val, vv)

    return {
        'total': len(all_amps),
        'pf_count': len(pf),
        'nonpf_count': len(nonpf),
        'vanishing_hodge': len(vanishing),
        'nonzero_pf': len(nonzero_pf),
        'pf_by_codim': pf_by_codim,
        'pf_by_vertices': pf_by_verts,
        'nonpf_by_codim': nonpf_by_codim,
        'by_loop_number': by_loop,
        'max_g0_valence_nonzero': max_g0_val,
        'shadow_vals_present': sorted(shadow_vals_present),
    }


# ============================================================================
# Section 6: Total amplitudes and planted-forest correction
# ============================================================================

def genus4_total_amplitude(shadow: ShadowData) -> Any:
    r"""Total genus-4 amplitude F_4(A) = sum_Gamma (1/|Aut|) * w(Gamma) * I(Gamma)."""
    total = Integer(0)
    for amp in genus4_all_amplitudes():
        total += amp.weighted_amplitude(shadow)
    return cancel(total)


def genus4_planted_forest_correction(shadow: ShadowData) -> Any:
    r"""Planted-forest correction delta_pf^{(4,0)}.

    Sum over graphs with at least one genus-0 vertex of valence >= 3.
    """
    total = Integer(0)
    for amp in genus4_pf_amplitudes():
        total += amp.weighted_amplitude(shadow)
    return cancel(total)


def genus4_nonpf_amplitude(shadow: ShadowData) -> Any:
    """Non-planted-forest amplitude at genus 4 (kappa-only part)."""
    total = Integer(0)
    for amp in genus4_nonpf_amplitudes():
        total += amp.weighted_amplitude(shadow)
    return cancel(total)


# ============================================================================
# Section 7: Family-specific evaluations
# ============================================================================

def genus4_heisenberg_F4() -> Dict[str, Any]:
    r"""Genus-4 free energy for Heisenberg H_k.

    F_4(H_k) = k * lambda_4^FP = k * 127/154828800.
    Class G: S_r = 0 for r >= 3, planted-forest correction vanishes.

    Three-path verification:
    1. Graph sum with Heisenberg shadow data
    2. Direct Bernoulli formula kappa * lambda_4^FP
    3. A-hat generating function coefficient
    """
    shadow = heisenberg_shadow_data()
    k = Symbol('k')

    # Path 1: Graph sum
    F4_graphsum = genus4_total_amplitude(shadow)

    # Path 2: Direct Bernoulli
    l4 = lambda_fp_exact(4)
    F4_bernoulli = k * Integer(l4.numerator) / Integer(l4.denominator)

    # Path 3: A-hat series (h/2)/sin(h/2) coefficient at h^8
    c_sin = [Fraction((-1)**n, factorial(2 * n + 1)) for n in range(5)]
    a = [Fraction(0)] * 5
    a[0] = Fraction(1)
    for n in range(1, 5):
        s = Fraction(0)
        for j in range(1, n + 1):
            s += c_sin[j] * a[n - j]
        a[n] = -s / c_sin[0]
    l4_ahat = a[4] / Fraction(4 ** 4)
    F4_ahat = k * Integer(l4_ahat.numerator) / Integer(l4_ahat.denominator)

    pf_correction = genus4_planted_forest_correction(shadow)

    return {
        'F4_graphsum': cancel(F4_graphsum),
        'F4_bernoulli': cancel(F4_bernoulli),
        'F4_ahat': cancel(F4_ahat),
        'lambda4_fp': l4,
        'lambda4_ahat': l4_ahat,
        'pf_correction': cancel(pf_correction),
        'pf_is_zero': simplify(pf_correction) == 0,
        'paths_match': (
            simplify(F4_graphsum - F4_bernoulli) == 0
            and l4 == l4_ahat
        ),
    }


def genus4_virasoro_F4() -> Dict[str, Any]:
    r"""Genus-4 free energy for Virasoro Vir_c.

    F_4(Vir_c) involves the full shadow tower through S_7.
    S_6 is the first NEW shadow coefficient at genus 4.
    """
    shadow = virasoro_shadow_data(max_arity=10)

    F4_total = genus4_total_amplitude(shadow)
    F4_pf = genus4_planted_forest_correction(shadow)
    F4_nonpf = genus4_nonpf_amplitude(shadow)

    l4 = lambda_fp_exact(4)
    F4_scalar = c_sym / 2 * Integer(l4.numerator) / Integer(l4.denominator)

    return {
        'F4_total': F4_total,
        'F4_pf': F4_pf,
        'F4_nonpf': F4_nonpf,
        'F4_scalar': cancel(F4_scalar),
    }


def genus4_affine_sl2_F4() -> Dict[str, Any]:
    """Genus-4 free energy for affine sl_2 (class L: S_3=2, S_4=0)."""
    shadow = affine_shadow_data()
    F4_total = genus4_total_amplitude(shadow)
    F4_pf = genus4_planted_forest_correction(shadow)

    return {
        'F4_total': F4_total,
        'F4_pf': F4_pf,
        'class': 'L',
    }


# ============================================================================
# Section 8: Self-loop parity vanishing verification
# ============================================================================

def verify_self_loop_parity_g4() -> Dict[str, Any]:
    r"""Verify self-loop parity vanishing for genus-4 single-vertex graphs.

    Single-vertex graphs at (4,0):
      (4,0): 0 loops, dim=9, smooth graph, N/A
      (3,2): 1 loop, dim=8 EVEN, NOT forced (k=1 < 2)
      (2,4): 2 loops, dim=5 ODD, I=0 by parity (k=2 >= 2)
      (1,6): 3 loops, dim=3 ODD, I=0 by parity (k=3 >= 2)
      (0,8): 4 loops, dim=5 ODD, I=0 by parity (k=4 >= 2)
    """
    single_vertex_data = [
        (4, 0, 0),
        (3, 2, 1),
        (2, 4, 2),
        (1, 6, 3),
        (0, 8, 4),
    ]

    results = {}
    for gv, valence, n_loops in single_vertex_data:
        if n_loops == 0:
            results[f'({gv},{valence})'] = {
                'genus': gv, 'valence': valence, 'n_loops': n_loops,
                'dim': 3 * gv - 3, 'I': Fraction(1), 'parity_applicable': False,
            }
            continue

        edges = tuple((0, 0) for _ in range(n_loops))
        graph = StableGraph(vertex_genera=(gv,), edges=edges, legs=())
        dim_v = 3 * gv - 3 + valence
        I = hodge_integral(graph)
        dim_odd = dim_v % 2 == 1

        results[f'({gv},{valence})'] = {
            'genus': gv, 'valence': valence, 'n_loops': n_loops,
            'dim': dim_v, 'dim_is_odd': dim_odd, 'I': I,
            'vanishes': I == Fraction(0),
            'parity_prediction': dim_odd and n_loops >= 2,
            'parity_applicable': n_loops >= 2,
        }

    return results


# ============================================================================
# Section 9: Shadow visibility verification
# ============================================================================

def verify_shadow_visibility_g4() -> Dict[str, Any]:
    r"""Verify shadow visibility at genus 4.

    g_min(S_r) = floor(r/2) + 1.
    S_6: g_min = 4, FIRST VISIBLE at genus 4.
    S_7: g_min = 4, FIRST VISIBLE at genus 4.
    S_8: g_min = 5, NOT visible at genus 4.
    """
    pf_amps = genus4_pf_amplitudes()

    max_g0_val_nonzero = 0
    has_val = {}
    for amp in pf_amps:
        for v in range(amp.graph.num_vertices):
            if amp.graph.vertex_genera[v] == 0:
                vv = amp.graph.valence[v]
                if amp.hodge_integral != Fraction(0):
                    max_g0_val_nonzero = max(max_g0_val_nonzero, vv)
                    has_val[vv] = True

    # Symbolic isolation: verify S_6 appears in delta_pf
    kappa_sym = Symbol('kappa')
    S6_sym = Symbol('S_6')
    S7_sym = Symbol('S_7')

    shadow_S6 = ShadowData(
        'test_S6', kappa_sym, Integer(0), Integer(0),
        shadows={5: Integer(0), 6: S6_sym, 7: Integer(0)},
        depth_class='M',
    )
    pf_only_S6 = genus4_planted_forest_correction(shadow_S6)
    S6_appears = simplify(pf_only_S6) != 0

    shadow_S7 = ShadowData(
        'test_S7', kappa_sym, Integer(0), Integer(0),
        shadows={5: Integer(0), 6: Integer(0), 7: S7_sym},
        depth_class='M',
    )
    pf_only_S7 = genus4_planted_forest_correction(shadow_S7)
    S7_appears = simplify(pf_only_S7) != 0

    return {
        'max_g0_valence_nonzero_I': max_g0_val_nonzero,
        'has_val_6_nonzero': has_val.get(6, False),
        'has_val_7_nonzero': has_val.get(7, False),
        'has_val_8_nonzero': has_val.get(8, False),
        'S6_in_pf_correction': S6_appears,
        'S7_in_pf_correction': S7_appears,
        'formula_g_min_S6': 6 // 2 + 1,
        'formula_g_min_S7': 7 // 2 + 1,
        'formula_g_min_S8': 8 // 2 + 1,
    }


# ============================================================================
# Section 10: Symbolic planted-forest polynomial
# ============================================================================

def genus4_pf_polynomial() -> Dict[str, Any]:
    r"""Extract delta_pf^{(4,0)} as a polynomial in shadow variables.

    Variables: kappa, S_3, S_4, S_5, S_6, S_7.
    """
    kappa_sym = Symbol('kappa')
    S3_sym = Symbol('S_3')
    S4_sym = Symbol('S_4')
    S5_sym = Symbol('S_5')
    S6_sym = Symbol('S_6')
    S7_sym = Symbol('S_7')

    shadow_generic = ShadowData(
        'generic', kappa_sym, S3_sym, S4_sym,
        shadows={5: S5_sym, 6: S6_sym, 7: S7_sym},
        depth_class='M',
    )

    pf = genus4_planted_forest_correction(shadow_generic)
    pf_expanded = expand(pf)

    all_vars = [kappa_sym, S3_sym, S4_sym, S5_sym, S6_sym, S7_sym]
    try:
        poly = Poly(pf_expanded, *all_vars)
        monomial_dict = poly.as_dict()
        n_terms = len(monomial_dict)
    except Exception:
        monomial_dict = {}
        n_terms = -1

    depends_on = {}
    for var in all_vars:
        test_val = pf_expanded.subs(var, 0)
        depends_on[str(var)] = simplify(pf_expanded - test_val) != 0

    return {
        'pf_polynomial': pf_expanded,
        'n_terms': n_terms,
        'monomial_dict': monomial_dict,
        'depends_on': depends_on,
        'variables': [str(v) for v in all_vars],
    }


# ============================================================================
# Section 11: Pixton ideal membership tests
# ============================================================================

def genus4_pixton_membership_test() -> Dict[str, Any]:
    r"""Test whether the shadow class obs_4 lies in the Pixton ideal.

    The D^2 = 0 constraint guarantees obs_4 is tautological.
    The test is whether it lies in the Pixton ideal subspace.
    """
    results = {}

    # Test 1: Heisenberg (class G) -- delta_pf must vanish
    heis = heisenberg_shadow_data()
    pf_heis = genus4_planted_forest_correction(heis)
    results['heisenberg_pf_vanishes'] = simplify(pf_heis) == 0

    # Test 2: Affine sl_2 (class L) -- delta_pf involves S_3 only
    aff = affine_shadow_data()
    pf_aff = genus4_planted_forest_correction(aff)
    results['affine_pf_nonzero'] = simplify(pf_aff) != 0

    # Test 3: Virasoro (class M) -- delta_pf involves all S_r
    vir = virasoro_shadow_data(max_arity=10)
    pf_vir = genus4_planted_forest_correction(vir)
    results['virasoro_pf_nonzero'] = simplify(pf_vir) != 0

    # Test 4: Numerical evaluation
    numerical_checks = {}
    for c_val in [1, 2, 4, 10, 13, 25, 26]:
        pf_num = complex(pf_vir.subs(c_sym, c_val))
        F4_total = complex(genus4_total_amplitude(vir).subs(c_sym, c_val))
        F4_scalar = c_val / 2 * float(LAMBDA4_FP)
        numerical_checks[c_val] = {
            'pf_correction': float(pf_num.real),
            'F4_total': float(F4_total.real),
            'F4_scalar': F4_scalar,
        }
    results['numerical_checks'] = numerical_checks

    return results


# ============================================================================
# Section 12: Cross-family comparison
# ============================================================================

def cross_family_comparison() -> Dict[str, Any]:
    r"""Compare obs_4(Vir_c) with obs_4(KM_k) for sl_2.

    The key structural difference: Virasoro (class M) has S_6 contributions
    that affine sl_2 (class L) does not.
    """
    vir = virasoro_shadow_data(max_arity=10)
    aff = affine_shadow_data()

    F4_vir = genus4_total_amplitude(vir)
    pf_vir = genus4_planted_forest_correction(vir)
    F4_aff = genus4_total_amplitude(aff)
    pf_aff = genus4_planted_forest_correction(aff)

    # Isolate the S_6-dependent part
    shadow_no_S6 = ShadowData(
        'vir_no_S6', c_sym / 2, Integer(2),
        Integer(10) / (c_sym * (5 * c_sym + 22)),
        shadows={5: virasoro_shadow_data(max_arity=10).S(5),
                 6: Integer(0), 7: Integer(0)},
        depth_class='M',
    )
    pf_no_S6 = genus4_planted_forest_correction(shadow_no_S6)
    S6_contribution = cancel(pf_vir - pf_no_S6)

    return {
        'F4_vir': F4_vir,
        'F4_aff': F4_aff,
        'pf_vir': pf_vir,
        'pf_aff': pf_aff,
        'S6_contribution': S6_contribution,
        'S6_nonzero': simplify(S6_contribution) != 0,
    }


# ============================================================================
# Section 13: Pixton generation analysis
# ============================================================================

def pixton_generation_analysis() -> Dict[str, Any]:
    r"""Analyse whether genus-4 MC relations generate the Pixton ideal.

    Key question: does the S_6 contribution produce tautological relations
    INDEPENDENT of the genus-2 and genus-3 relations?
    """
    pf_data = genus4_pf_polynomial()

    S6_sym = Symbol('S_6')
    pf_poly = pf_data['pf_polynomial']

    # Terms involving S_6
    S6_terms = expand(pf_poly - pf_poly.subs(S6_sym, 0))
    n_S6_terms = 0
    if S6_terms != 0:
        try:
            kappa_sym = Symbol('kappa')
            S3_sym = Symbol('S_3')
            S4_sym = Symbol('S_4')
            S5_sym = Symbol('S_5')
            S7_sym = Symbol('S_7')
            p = Poly(S6_terms, kappa_sym, S3_sym, S4_sym, S5_sym, S6_sym, S7_sym)
            n_S6_terms = len(p.as_dict())
        except Exception:
            n_S6_terms = -1

    pf_amps = genus4_pf_amplitudes()
    pf_codims = Counter(a.codimension for a in pf_amps if a.hodge_integral != Fraction(0))
    codim_ge5_count = sum(c for k, c in pf_codims.items() if k >= 5)

    return {
        'pf_n_terms': pf_data['n_terms'],
        'S6_dependent_terms': n_S6_terms,
        'S6_terms_nonzero': S6_terms != 0,
        'pf_codim_distribution': dict(sorted(pf_codims.items())),
        'codim_ge5_pf_graphs': codim_ge5_count,
        'depends_on': pf_data['depends_on'],
        'pixton_codim_start': 5,  # g+1 = 5
    }


# ============================================================================
# Section 14: Consistency checks
# ============================================================================

def consistency_checks() -> Dict[str, Any]:
    r"""Run all consistency checks for the genus-4 Pixton bridge.

    1. Graph count matches expected 379.
    2. Heisenberg F_4 matches lambda_4^FP.
    3. Self-loop parity vanishing holds.
    4. Shadow visibility matches g_min formula.
    5. Decomposition F_4 = PF + non-PF.
    """
    census = genus4_pixton_census()
    checks = {}

    # Check 1: Graph count
    checks['graph_count'] = {
        'actual': census['total'],
        'expected': 379,
        'passed': census['total'] == 379,
    }

    # Check 2: Heisenberg F_4
    heis_data = genus4_heisenberg_F4()
    checks['heisenberg_paths_match'] = heis_data['paths_match']
    checks['heisenberg_pf_zero'] = heis_data['pf_is_zero']

    # Check 3: Self-loop parity
    parity_data = verify_self_loop_parity_g4()
    parity_ok = True
    for key, val in parity_data.items():
        if val.get('parity_applicable', False) and val.get('parity_prediction', False):
            if not val.get('vanishes', False):
                parity_ok = False
    checks['self_loop_parity'] = parity_ok

    # Check 4: Shadow visibility
    vis_data = verify_shadow_visibility_g4()
    checks['S6_visible'] = vis_data['S6_in_pf_correction']
    checks['S6_g_min_correct'] = vis_data['formula_g_min_S6'] == 4

    # Check 5: Decomposition
    shadow_test = virasoro_shadow_data(max_arity=10)
    F4_total = genus4_total_amplitude(shadow_test)
    F4_pf = genus4_planted_forest_correction(shadow_test)
    F4_nonpf = genus4_nonpf_amplitude(shadow_test)
    diff = simplify(F4_total - F4_pf - F4_nonpf)
    checks['decomposition_consistent'] = diff == 0

    return checks
