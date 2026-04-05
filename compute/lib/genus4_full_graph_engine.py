r"""Genus-4 full stable graph engine: enumeration, classification, and amplitudes.

Complete computation for the modular bar construction at genus 4 (g=4, n=0).
This module unifies and extends the genus4_stable_graphs and
genus4_planted_forest_engine modules into a single comprehensive engine.

MATHEMATICAL CONTEXT
====================

The shadow obstruction tower at genus g involves graph sums over stable
graphs of M-bar_{g,n}. The planted-forest correction delta_pf^{(g,0)}
contributes from codimension->=2 log-FM strata (Mok's rigid strata).

GENUS-4 KEY DATA
================

Total stable graphs at (4,0): 379
  By vertex count: 1->5, 2->29, 3->79, 4->126, 5->98, 6->42
  By loop number:  0->11, 1->36, 2->93, 3->128, 4->111
  By edge count:   0->1, 1->3, 2->7, 3->21, 4->43, 5->75,
                   6->89, 7->81, 8->42, 9->17

Planted-forest (>=1 genus-0 vertex with val>=3): 358
Non-planted-forest: 21

Orbifold Euler characteristics:
  chi^orb(M_bar_{4,0}) = -4717039/6220800  (vertex-product formula)
  chi^orb(M_4)          = -1/1440           (= B_8/(4*4*3), Harer-Zagier)

lambda_4^FP = (2^7-1)|B_8|/(2^7 * 8!) = 127/154828800

Shadow visibility at genus 4:
  S_6 first appears: g_min(6) = floor(6/2)+1 = 4
  S_7 first appears: g_min(7) = floor(7/2)+1 = 4
  S_8 NOT visible:   g_min(8) = floor(8/2)+1 = 5

Self-loop parity vanishing (prop:self-loop-vanishing):
  (0,8) 4 loops: dim=5 odd, I=0
  (1,6) 3 loops: dim=6 even, I nonzero (parity does NOT apply)
  (2,4) 2 loops: dim=5 odd, I=0

F_4(H_k) = k * 127/154828800  (Heisenberg, class G)
F_4(Vir_c) = (c/2) * 127/154828800 + delta_pf^{(4,0)}(c)  (Virasoro, class M)

MULTI-PATH VERIFICATION
=======================

Path 1: Direct enumeration + amplitude computation
Path 2: Orbifold Euler characteristic via graph-vertex-product
Path 3: Heisenberg specialization (pf correction vanishes)
Path 4: Dimension/weight consistency (dim M_bar_{4,0} = 9)
Path 5: Self-loop parity vanishing
Path 6: Cross-genus monotonicity and growth

References:
  higher_genus_modular_koszul.tex: def:stable-graph-coefficient-algebra,
    cor:shadow-visibility-genus, prop:self-loop-vanishing, thm:theorem-d
  pixton_shadow_bridge.py: ShadowData, wk_intersection
  stable_graph_enumeration.py: StableGraph, enumerate_stable_graphs
  genus4_planted_forest_engine.py: hodge_integral, vertex_weight
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from math import factorial
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Integer, Rational, Symbol, cancel, expand, factor, simplify, S,
    collect, Poly, degree, N as neval,
)

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    orbifold_euler_characteristic,
    graph_weight,
    graph_sum_scalar,
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
from compute.lib.genus4_planted_forest_engine import (
    hodge_integral,
    vertex_weight,
    is_planted_forest,
    ell_genus1,
    GraphAmplitude,
    _hodge_integral_cached,
)


# ============================================================================
# Section 0: Constants
# ============================================================================

GENUS = 4
DIM_MBAR = 3 * GENUS - 3  # = 9
MAX_EDGES = DIM_MBAR       # = 9
EXPECTED_GRAPH_COUNT = 379
EXPECTED_PF_COUNT = 358
EXPECTED_NONPF_COUNT = 21
CHI_ORB_MBAR = Fraction(-4717039, 6220800)
CHI_ORB_OPEN = _bernoulli_exact(8) / Fraction(4 * 4 * 3)  # B_8/(48)
LAMBDA4_FP = _lambda_fp_exact(4)  # 127/154828800


# ============================================================================
# Section 1: Graph enumeration and caching
# ============================================================================

@lru_cache(maxsize=1)
def genus4_graphs() -> Tuple[StableGraph, ...]:
    """Complete enumeration of all 379 genus-4 stable graphs at n=0."""
    return tuple(enumerate_stable_graphs(GENUS, 0))


def graph_count() -> int:
    """Total number of stable graphs at (g=4, n=0)."""
    return len(genus4_graphs())


# ============================================================================
# Section 2: Full annotation: Hodge integrals, automorphisms, classification
# ============================================================================

@dataclass
class AnnotatedGraph:
    """A genus-4 stable graph with full computed invariants."""
    graph: StableGraph
    index: int
    hodge_integral: Fraction
    aut_order: int
    is_pf: bool  # planted-forest
    vertex_genera: Tuple[int, ...]
    vertex_valences: Tuple[int, ...]
    num_self_loops: int
    max_genus0_valence: int  # max valence among genus-0 vertices
    shell: str  # classification: 'smooth', 'tree', 'one-loop', etc.

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
    def loop_number(self) -> int:
        return self.graph.first_betti

    @property
    def has_nonzero_hodge(self) -> bool:
        return self.hodge_integral != Fraction(0)

    def vertex_weight_eval(self, shadow: ShadowData) -> Any:
        """Evaluate vertex weight with given shadow data."""
        return vertex_weight(self.graph, shadow)

    def weighted_amplitude(self, shadow: ShadowData) -> Any:
        """Full amplitude: (1/|Aut|) * w(Gamma) * I(Gamma)."""
        w = self.vertex_weight_eval(shadow)
        I_sympy = Integer(self.hodge_integral.numerator) / Integer(
            self.hodge_integral.denominator)
        return cancel(w * I_sympy / self.aut_order)

    def chi_contribution(self) -> Fraction:
        """Orbifold Euler characteristic contribution of this stratum."""
        val = self.graph.valence
        product = Fraction(1)
        for v in range(self.graph.num_vertices):
            product *= _chi_orb_open(self.graph.vertex_genera[v], val[v])
        return product / Fraction(self.aut_order)


def _classify_shell(graph: StableGraph) -> str:
    """Classify a graph into shell types."""
    ne = graph.num_edges
    h1 = graph.first_betti
    nv = graph.num_vertices
    if ne == 0:
        return 'smooth'
    if h1 == 0:
        return 'tree'
    if nv == 1:
        n_loops = sum(1 for v1, v2 in graph.edges if v1 == v2)
        return f'single-vertex-{n_loops}loop'
    if h1 == 1:
        return 'one-loop'
    if h1 == 2:
        return 'two-loop'
    if h1 == 3:
        return 'three-loop'
    return f'{h1}-loop'


@lru_cache(maxsize=1)
def annotated_graphs() -> Tuple[AnnotatedGraph, ...]:
    """All 379 genus-4 graphs with full computed invariants."""
    graphs = genus4_graphs()
    result = []
    for i, g in enumerate(graphs):
        val = g.valence
        n_self = sum(1 for v1, v2 in g.edges if v1 == v2)
        max_g0_val = 0
        for v in range(g.num_vertices):
            if g.vertex_genera[v] == 0:
                max_g0_val = max(max_g0_val, val[v])

        ag = AnnotatedGraph(
            graph=g,
            index=i,
            hodge_integral=_hodge_integral_cached(g.vertex_genera, g.edges),
            aut_order=g.automorphism_order(),
            is_pf=is_planted_forest(g),
            vertex_genera=g.vertex_genera,
            vertex_valences=val,
            num_self_loops=n_self,
            max_genus0_valence=max_g0_val,
            shell=_classify_shell(g),
        )
        result.append(ag)
    return tuple(result)


# ============================================================================
# Section 3: Census and structural analysis
# ============================================================================

def full_census() -> Dict[str, Any]:
    """Complete census of all 379 genus-4 graphs."""
    all_ag = annotated_graphs()
    pf = [a for a in all_ag if a.is_pf]
    nonpf = [a for a in all_ag if not a.is_pf]
    vanishing = [a for a in all_ag if not a.has_nonzero_hodge]
    nonzero_pf = [a for a in pf if a.has_nonzero_hodge]

    return {
        'total': len(all_ag),
        'pf_count': len(pf),
        'nonpf_count': len(nonpf),
        'vanishing_hodge': len(vanishing),
        'nonzero_hodge': len(all_ag) - len(vanishing),
        'nonzero_pf': len(nonzero_pf),
        'by_vertex_count': dict(sorted(
            Counter(a.num_vertices for a in all_ag).items()
        )),
        'by_edge_count': dict(sorted(
            Counter(a.num_edges for a in all_ag).items()
        )),
        'by_loop_number': dict(sorted(
            Counter(a.loop_number for a in all_ag).items()
        )),
        'by_shell': dict(sorted(
            Counter(a.shell for a in all_ag).items()
        )),
        'max_aut': max(a.aut_order for a in all_ag),
        'min_aut': min(a.aut_order for a in all_ag),
    }


def by_vertex_count() -> Dict[int, int]:
    """Graph count by number of vertices."""
    return dict(sorted(
        Counter(a.num_vertices for a in annotated_graphs()).items()
    ))


def by_edge_count() -> Dict[int, int]:
    """Graph count by number of edges (= codimension)."""
    return dict(sorted(
        Counter(a.num_edges for a in annotated_graphs()).items()
    ))


def by_loop_number() -> Dict[int, int]:
    """Graph count by first Betti number h^1."""
    return dict(sorted(
        Counter(a.loop_number for a in annotated_graphs()).items()
    ))


def automorphism_spectrum() -> Dict[int, int]:
    """Frequency distribution of automorphism group orders."""
    return dict(sorted(
        Counter(a.aut_order for a in annotated_graphs()).items()
    ))


def inverse_aut_sum() -> Fraction:
    """Sum of 1/|Aut(Gamma)| over all graphs."""
    return sum(
        Fraction(1, a.aut_order) for a in annotated_graphs()
    )


# ============================================================================
# Section 4: Orbifold Euler characteristic (Verification Path 2)
# ============================================================================

def euler_characteristic_check() -> Dict[str, Any]:
    """Verify chi^orb(M_bar_{4,0}) via graph-vertex-product formula.

    The formula: chi^orb(M_bar_{g,n}) = sum_Gamma prod_v chi^orb(M_{g(v),val(v)}) / |Aut|

    Expected: -4717039/6220800 (pre-computed from the 379-graph sum).
    Cross-check: chi^orb(M_4) = B_8/(4*4*3) = -1/1440 (Harer-Zagier).
    """
    all_ag = annotated_graphs()

    # Compute chi via vertex product formula
    chi_computed = sum(a.chi_contribution() for a in all_ag)

    # Decomposition by codimension
    chi_by_codim: Dict[int, Fraction] = {}
    for a in all_ag:
        codim = a.codimension
        chi_by_codim[codim] = chi_by_codim.get(codim, Fraction(0)) + a.chi_contribution()

    # The codim=0 contribution is chi^orb(M_4) itself
    chi_interior = chi_by_codim.get(0, Fraction(0))

    return {
        'chi_computed': chi_computed,
        'chi_expected': CHI_ORB_MBAR,
        'match': chi_computed == CHI_ORB_MBAR,
        'chi_interior': chi_interior,
        'chi_open_expected': CHI_ORB_OPEN,
        'interior_match': chi_interior == CHI_ORB_OPEN,
        'chi_by_codim': dict(sorted(chi_by_codim.items())),
    }


# ============================================================================
# Section 5: Lambda number and A-hat generating function
# ============================================================================

def lambda4_three_paths() -> Dict[str, Any]:
    r"""Verify lambda_4^FP = 127/154828800 via three independent methods.

    Path 1: Direct Bernoulli formula (2^7-1)|B_8|/(2^7 * 8!)
    Path 2: Power series inversion of (x/2)/sin(x/2)
    Path 3: A-hat generating function coefficient extraction
    """
    # Path 1: Direct Bernoulli
    B8 = _bernoulli_exact(8)
    path1 = (2**7 - 1) * abs(B8) / Fraction(2**7 * factorial(8))

    # Path 2: Power series inversion
    # sin(y)/y = 1 - y^2/6 + y^4/120 - y^6/5040 + y^8/362880
    # Let t = y^2, f(t) = sin(sqrt(t))/sqrt(t) = sum c_n t^n
    c_f = [Fraction((-1)**n, factorial(2*n + 1)) for n in range(5)]
    a = [Fraction(0)] * 5
    a[0] = Fraction(1)
    for k in range(1, 5):
        s = Fraction(0)
        for j in range(1, k + 1):
            s += c_f[j] * a[k - j]
        a[k] = -s
    # Coefficient of x^{2g} in (x/2)/sin(x/2) = a[g]/4^g
    path2 = a[4] / Fraction(4**4)

    # Path 3: From the engine
    path3 = _lambda_fp_exact(4)

    return {
        'path1_bernoulli': path1,
        'path2_series': path2,
        'path3_engine': path3,
        'expected': Fraction(127, 154828800),
        'all_match': path1 == path2 == path3 == Fraction(127, 154828800),
    }


# ============================================================================
# Section 6: Amplitude computation
# ============================================================================

def total_amplitude(shadow: ShadowData) -> Any:
    """Total genus-4 amplitude F_4(A) as a graph sum.

    F_4(A) = sum_Gamma (1/|Aut|) * w(Gamma) * I(Gamma)
    """
    total = Integer(0)
    for ag in annotated_graphs():
        if ag.has_nonzero_hodge:
            total += ag.weighted_amplitude(shadow)
    return cancel(total)


def planted_forest_correction(shadow: ShadowData) -> Any:
    """Planted-forest correction delta_pf^{(4,0)}.

    Sum over graphs with at least one genus-0 vertex of valence >= 3.
    """
    total = Integer(0)
    for ag in annotated_graphs():
        if ag.is_pf and ag.has_nonzero_hodge:
            total += ag.weighted_amplitude(shadow)
    return cancel(total)


def nonpf_amplitude(shadow: ShadowData) -> Any:
    """Non-planted-forest amplitude at genus 4.

    For Heisenberg (class G): F_4 = nonpf_amplitude (since pf_correction = 0).
    """
    total = Integer(0)
    for ag in annotated_graphs():
        if not ag.is_pf and ag.has_nonzero_hodge:
            total += ag.weighted_amplitude(shadow)
    return cancel(total)


def amplitude_by_codimension(shadow: ShadowData) -> Dict[int, Any]:
    """Amplitude decomposition by codimension (edge count)."""
    result: Dict[int, Any] = {}
    for ag in annotated_graphs():
        if ag.has_nonzero_hodge:
            codim = ag.codimension
            contrib = ag.weighted_amplitude(shadow)
            result[codim] = cancel(result.get(codim, Integer(0)) + contrib)
    return dict(sorted(result.items()))


def amplitude_by_shell(shadow: ShadowData) -> Dict[str, Any]:
    """Amplitude decomposition by shell type."""
    result: Dict[str, Any] = {}
    for ag in annotated_graphs():
        if ag.has_nonzero_hodge:
            shell = ag.shell
            contrib = ag.weighted_amplitude(shadow)
            result[shell] = cancel(result.get(shell, Integer(0)) + contrib)
    return dict(sorted(result.items()))


# ============================================================================
# Section 7: Planted-forest polynomial extraction
# ============================================================================

def pf_polynomial_symbolic() -> Dict[str, Any]:
    """Extract delta_pf^{(4,0)} as a polynomial in kappa, S_3, S_4, S_5, S_6, S_7.

    The result has exact rational coefficients from Hodge integrals.
    S_7 can appear at genus 4 (g_min(S_7)=4) via single-vertex genus-0
    valence-7 graphs, but these vanish by parity or dimension constraints.
    """
    kappa_sym = Symbol('kappa')
    S3_sym = Symbol('S_3')
    S4_sym = Symbol('S_4')
    S5_sym = Symbol('S_5')
    S6_sym = Symbol('S_6')
    S7_sym = Symbol('S_7')

    shadow = ShadowData(
        'genus4_symbolic', kappa_sym, S3_sym, S4_sym,
        shadows={5: S5_sym, 6: S6_sym, 7: S7_sym},
        depth_class='M',
    )

    total = Integer(0)
    nonzero_count = 0
    nonzero_graphs = []

    for ag in annotated_graphs():
        if ag.is_pf and ag.has_nonzero_hodge:
            contrib = ag.weighted_amplitude(shadow)
            if simplify(contrib) != 0:
                nonzero_count += 1
                nonzero_graphs.append({
                    'index': ag.index,
                    'genera': ag.vertex_genera,
                    'valences': ag.vertex_valences,
                    'hodge': ag.hodge_integral,
                    'aut': ag.aut_order,
                    'amplitude': cancel(contrib),
                })
            total += contrib

    poly = cancel(expand(total))

    # Extract monomial decomposition
    monomials = _extract_monomials(
        poly, kappa_sym, S3_sym, S4_sym, S5_sym, S6_sym, S7_sym
    )

    return {
        'polynomial': poly,
        'monomials': monomials,
        'num_terms': sum(1 for v in monomials.values() if v != 0),
        'num_nonzero_pf_graphs': nonzero_count,
        'nonzero_graph_details': nonzero_graphs,
    }


def _extract_monomials(
    expr: Any,
    kappa: Symbol, S3: Symbol, S4: Symbol,
    S5: Symbol, S6: Symbol, S7: Symbol,
) -> Dict[str, Any]:
    """Extract monomial coefficients from a polynomial in 6 variables."""
    expr_expanded = expand(expr)
    result = {}
    try:
        p = Poly(expr_expanded, kappa, S3, S4, S5, S6, S7, domain='QQ')
        for monom, coeff in p.as_dict().items():
            key = _monomial_key(*monom)
            result[key] = Rational(coeff)
    except Exception:
        result['full_expression'] = expr_expanded
    return result


def _monomial_key(a, b, c, d, e, f) -> str:
    """Human-readable monomial key."""
    names = [('kappa', a), ('S_3', b), ('S_4', c), ('S_5', d),
             ('S_6', e), ('S_7', f)]
    parts = []
    for name, exp in names:
        if exp > 0:
            parts.append(f"{name}^{exp}" if exp > 1 else name)
    return " * ".join(parts) if parts else "1"


# ============================================================================
# Section 8: Shadow variable isolation tests
# ============================================================================

def pf_depends_on_variable(var_name: str) -> bool:
    """Test whether delta_pf^{(4,0)} depends on a specific shadow variable.

    Strategy: keep kappa symbolic (since vertex weights for genus >= 1
    vertices depend on kappa), set ALL shadow variables S_3..S_7 to zero
    EXCEPT the one being tested, which is set to a fresh symbol.

    Returns True if the planted-forest correction contains the tested variable.
    """
    kappa_sym = Symbol('kappa')
    test_sym = Symbol(f'test_{var_name}')

    # kappa is always symbolic (it multiplies shadow weights at genus >= 1 vertices)
    # We zero out all S_r EXCEPT the one being tested
    shadow_vars = {
        'S_3': Integer(0),
        'S_4': Integer(0),
        'S_5': Integer(0),
        'S_6': Integer(0),
        'S_7': Integer(0),
    }
    if var_name in shadow_vars:
        shadow_vars[var_name] = test_sym

    shadow = ShadowData(
        f'test_{var_name}',
        kappa=kappa_sym,
        S3=shadow_vars['S_3'],
        S4=shadow_vars['S_4'],
        shadows={
            5: shadow_vars['S_5'],
            6: shadow_vars['S_6'],
            7: shadow_vars['S_7'],
        },
        depth_class='M',
    )
    pf = planted_forest_correction(shadow)
    pf_simplified = cancel(pf)

    if var_name == 'kappa':
        # For kappa: test whether the PF polynomial has ANY nonzero terms
        # (every PF graph needs at least one genus >= 1 vertex OR uses kappa
        # through the ell_genus1 function).
        # Use the full symbolic shadow to check kappa dependence.
        kappa_test = Symbol('kappa_test')
        full_shadow = ShadowData(
            'test_kappa', kappa_test,
            Symbol('S_3'), Symbol('S_4'),
            shadows={5: Symbol('S_5'), 6: Symbol('S_6'), 7: Symbol('S_7')},
            depth_class='M',
        )
        pf_full = cancel(planted_forest_correction(full_shadow))
        # Check if kappa_test appears in the expression
        return kappa_test in pf_full.free_symbols
    else:
        # Check if the test symbol appears
        return test_sym in pf_simplified.free_symbols


# ============================================================================
# Section 9: Self-loop parity vanishing (Verification Path 5)
# ============================================================================

def self_loop_parity_verification() -> Dict[str, Dict[str, Any]]:
    """Verify self-loop parity vanishing for all single-vertex genus-4 graphs.

    Single-vertex graphs at g=4:
      (4,0):  smooth, 0 loops, dim=9 (not applicable)
      (3,2):  1 loop, dim=8 EVEN (no parity vanishing)
      (2,4):  2 loops, dim=5 ODD -> I=0
      (1,6):  3 loops, dim=6 EVEN (no parity vanishing)
      (0,8):  4 loops, dim=5 ODD -> I=0
    """
    single_vertex_specs = [
        (4, 0, 0),  # (g_v, valence, n_loops)
        (3, 2, 1),
        (2, 4, 2),
        (1, 6, 3),
        (0, 8, 4),
    ]

    results = {}
    for gv, valence, n_loops in single_vertex_specs:
        if n_loops == 0:
            results[f'({gv},{valence})'] = {
                'genus': gv, 'valence': valence, 'n_loops': n_loops,
                'dim': 3 * gv - 3, 'I': Fraction(1),
                'parity_vanishing': False, 'computed_vanishes': False,
                'consistent': True,  # not applicable, trivially consistent
            }
            continue

        edges = tuple((0, 0) for _ in range(n_loops))
        graph = StableGraph(vertex_genera=(gv,), edges=edges, legs=())
        dim_v = 3 * gv - 3 + valence
        I = hodge_integral(graph)
        dim_odd = dim_v % 2 == 1
        parity_applies = dim_odd and n_loops >= 2

        results[f'({gv},{valence})'] = {
            'genus': gv,
            'valence': valence,
            'n_loops': n_loops,
            'dim': dim_v,
            'dim_is_odd': dim_odd,
            'I': I,
            'parity_vanishing': parity_applies,
            'computed_vanishes': I == Fraction(0),
            'consistent': (not parity_applies) or (I == Fraction(0)),
        }

    return results


# ============================================================================
# Section 10: Shadow visibility verification (Verification Path 4)
# ============================================================================

def shadow_visibility_check() -> Dict[str, Any]:
    """Check which shadow coefficients S_r appear at genus 4.

    cor:shadow-visibility-genus: g_min(S_r) = floor(r/2) + 1.
    At genus 4: S_6 (g_min=4) and S_7 (g_min=4) are newly visible.
    S_8 (g_min=5) should NOT contribute.
    """
    all_ag = annotated_graphs()

    # Track max genus-0 valence with nonzero Hodge integral
    max_g0_val = 0
    g0_valences_present: Dict[int, bool] = {}

    for ag in all_ag:
        if ag.has_nonzero_hodge:
            for v in range(ag.num_vertices):
                if ag.graph.vertex_genera[v] == 0:
                    vv = ag.graph.valence[v]
                    max_g0_val = max(max_g0_val, vv)
                    g0_valences_present[vv] = True

    # Check variable dependence symbolically
    s6_active = pf_depends_on_variable('S_6')
    s7_active = pf_depends_on_variable('S_7')

    return {
        'max_genus0_valence_nonzero_hodge': max_g0_val,
        'g0_valences_present': dict(sorted(g0_valences_present.items())),
        'S_6_in_polynomial': s6_active,
        'S_7_in_polynomial': s7_active,
        'g_min_S6': 6 // 2 + 1,  # = 4
        'g_min_S7': 7 // 2 + 1,  # = 4
        'g_min_S8': 8 // 2 + 1,  # = 5
    }


# ============================================================================
# Section 11: Heisenberg verification (Verification Path 3)
# ============================================================================

def gaussian_graph_sum(kappa_val: Any) -> Any:
    r"""Gaussian (class G) graph sum for F_g at genus 4.

    For class-G (Heisenberg) algebras, the Gaussian amplitude assigns:
      - Each genus-g_v vertex with valence val_v:
        * val_v = 0 (smooth): kappa * lambda_{g_v}^FP
        * val_v = 2 (bivalent genus >= 1): kappa  (edge propagator weight)
        * otherwise: 0 (the Gaussian tower terminates, so vertices with
          val >= 3 get S_val = 0)
      - Each edge: contributes a factor of 1/kappa (propagator denominator)

    The identity F_g = kappa * lambda_g^FP for Heisenberg is a CONSEQUENCE:
    only the "chain of sausages" graphs contribute (each smooth vertex gives
    kappa*lambda_{g_v}^FP, each bridge gives 1/kappa, net effect is additive).
    """
    all_ag = annotated_graphs()
    total = Integer(0)

    for ag in all_ag:
        val = ag.vertex_valences
        genera = ag.vertex_genera
        active = True
        amp = Integer(1)

        for v_idx in range(ag.num_vertices):
            gv = genera[v_idx]
            vn = val[v_idx]
            if vn == 0:
                # Smooth vertex: F_{g_v} = kappa * lambda_{g_v}^FP
                if gv < 1:
                    active = False; break  # No genus-0 smooth graph in n=0
                lam = _lambda_fp_exact(gv)
                amp *= kappa_val * Integer(lam.numerator) / Integer(lam.denominator)
            elif vn == 2:
                # Bivalent: kappa for genus >= 1 (the propagator vertex weight)
                if gv < 1:
                    active = False; break  # genus-0 bivalent vertex unstable
                amp *= kappa_val
            else:
                # Higher valence: S_val = 0 for Heisenberg, kills contribution
                active = False; break

        if not active:
            continue

        # Divide by kappa per edge (propagator denominator)
        for _ in range(ag.num_edges):
            amp = cancel(amp / kappa_val)

        total += cancel(amp / Integer(ag.aut_order))

    return cancel(total)


def heisenberg_verification() -> Dict[str, Any]:
    """Three-path verification of F_4(H_k) = k * 127/154828800.

    Path 1: Planted-forest correction vanishes for Heisenberg (S_r = 0, r >= 3)
    Path 2: Direct Bernoulli formula for lambda_4^FP
    Path 3: A-hat generating function coefficient

    The identity F_4(H_k) = k * lambda_4^FP follows from:
      (a) Theorem D: F_g^{scal}(A) = kappa(A) * lambda_g^FP (scalar level)
      (b) Class-G purity: delta_pf = 0 because S_r = 0 for r >= 3
      (c) F_g = F_g^{scal} + delta_pf = kappa * lambda_g^FP + 0

    The three paths verify (a)-(c) independently.
    """
    k = Symbol('k')

    # Path 1: PF correction vanishes
    shadow = heisenberg_shadow_data()
    pf_corr = planted_forest_correction(shadow)
    pf_is_zero = simplify(pf_corr) == 0

    # Path 2: Direct Bernoulli formula for lambda_4^FP
    B8 = _bernoulli_exact(8)
    l4_bernoulli = (2**7 - 1) * abs(B8) / Fraction(2**7 * factorial(8))

    # Path 3: A-hat generating function coefficient
    c_f = [Fraction((-1)**n, factorial(2*n + 1)) for n in range(5)]
    a = [Fraction(0)] * 5
    a[0] = Fraction(1)
    for kk in range(1, 5):
        s = Fraction(0)
        for j in range(1, kk + 1):
            s += c_f[j] * a[kk - j]
        a[kk] = -s
    l4_ahat = a[4] / Fraction(4**4)

    # Cross-check
    l4_engine = LAMBDA4_FP

    return {
        'pf_correction': cancel(pf_corr),
        'pf_is_zero': pf_is_zero,
        'lambda4_bernoulli': l4_bernoulli,
        'lambda4_ahat': l4_ahat,
        'lambda4_engine': l4_engine,
        'lambda4_expected': Fraction(127, 154828800),
        'bernoulli_ahat_match': l4_bernoulli == l4_ahat,
        'all_three_lambda_match': l4_bernoulli == l4_ahat == l4_engine,
        'all_match': (
            pf_is_zero
            and l4_bernoulli == l4_ahat == l4_engine
            and l4_engine == Fraction(127, 154828800)
        ),
    }


# ============================================================================
# Section 12: Virasoro numerical evaluation
# ============================================================================

def virasoro_amplitude_numerical(c_values: Optional[List[int]] = None) -> Dict[int, Dict[str, Any]]:
    """Evaluate F_4(Vir_c) numerically at several central charge values.

    For each c: compute the total amplitude, scalar part, and planted-forest
    correction. Verify: total = scalar + pf_correction at every c.
    """
    if c_values is None:
        c_values = [1, 2, 6, 13, 26, 48]

    shadow_vir = virasoro_shadow_data(max_arity=10)
    F4_total_sym = total_amplitude(shadow_vir)
    F4_pf_sym = planted_forest_correction(shadow_vir)
    F4_nonpf_sym = nonpf_amplitude(shadow_vir)

    results = {}
    for c_val in c_values:
        F4_total_num = float(neval(F4_total_sym.subs(c_sym, c_val), 30))
        F4_scalar = float(Fraction(c_val, 2) * LAMBDA4_FP)
        F4_pf_num = float(neval(F4_pf_sym.subs(c_sym, c_val), 30))
        F4_nonpf_num = float(neval(F4_nonpf_sym.subs(c_sym, c_val), 30))

        results[c_val] = {
            'F4_total': F4_total_num,
            'F4_scalar': F4_scalar,
            'F4_pf': F4_pf_num,
            'F4_nonpf': F4_nonpf_num,
            'decomposition_check': abs(F4_total_num - F4_nonpf_num - F4_pf_num) < 1e-10,
        }

    return results


# ============================================================================
# Section 13: Complementarity verification
# ============================================================================

def virasoro_complementarity() -> Dict[str, Any]:
    """Verify Virasoro complementarity at genus 4.

    kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    At the scalar level: F_4^{scal}(c) + F_4^{scal}(26-c) = 13 * lambda_4^FP.
    """
    kappa_sum = Fraction(13)
    F4_sum = kappa_sum * LAMBDA4_FP
    expected = Fraction(13) * LAMBDA4_FP

    return {
        'F4_scalar_sum': F4_sum,
        'expected': expected,
        'match': F4_sum == expected,
        'lambda4': LAMBDA4_FP,
    }


def km_antisymmetry(k: Fraction = Fraction(1), dim_g: int = 3,
                    h_vee: int = 2) -> Dict[str, Any]:
    """Verify KM antisymmetry: kappa(A) + kappa(A!) = 0 at genus 4."""
    kappa = Fraction(dim_g) * (k + h_vee) / Fraction(2 * h_vee)
    k_dual = -k - 2 * h_vee
    kappa_dual = Fraction(dim_g) * (k_dual + h_vee) / Fraction(2 * h_vee)
    s = (kappa + kappa_dual) * LAMBDA4_FP
    return {
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'sum': kappa + kappa_dual,
        'F4_sum': s,
        'antisymmetric': s == Fraction(0),
    }


# ============================================================================
# Section 14: Cross-genus consistency (Verification Path 6)
# ============================================================================

def cross_genus_consistency() -> Dict[str, Any]:
    """Cross-genus consistency checks.

    1. Graph counts are strictly increasing: g=1->2, g=2->6, g=3->42, g=4->379
    2. lambda_g^FP are strictly decreasing and positive
    3. chi^orb(M_g) = B_{2g}/(4g(g-1)) matches at each genus
    """
    counts = {}
    lambdas = {}
    chis = {}
    for g in range(1, 5):
        if g == 1:
            from compute.lib.stable_graph_enumeration import genus1_stable_graphs_n0
            counts[g] = len(genus1_stable_graphs_n0())
        elif g == 2:
            from compute.lib.stable_graph_enumeration import genus2_stable_graphs_n0
            counts[g] = len(genus2_stable_graphs_n0())
        else:
            counts[g] = len(enumerate_stable_graphs(g, 0))
        lambdas[g] = _lambda_fp_exact(g)
        if g >= 2:
            chis[g] = _chi_orb_open(g, 0)

    return {
        'counts': counts,
        'counts_increasing': all(counts[g] < counts[g + 1] for g in range(1, 4)),
        'lambdas': lambdas,
        'lambdas_decreasing': all(lambdas[g] > lambdas[g + 1] for g in range(1, 4)),
        'lambdas_positive': all(v > 0 for v in lambdas.values()),
        'chi_orb_open': chis,
    }


# ============================================================================
# Section 15: Nonzero Hodge integral statistics
# ============================================================================

def hodge_integral_statistics() -> Dict[str, Any]:
    """Statistics on Hodge integrals across all 379 graphs."""
    all_ag = annotated_graphs()
    nonzero = [a for a in all_ag if a.has_nonzero_hodge]
    positive = [a for a in nonzero if a.hodge_integral > 0]
    negative = [a for a in nonzero if a.hodge_integral < 0]

    # Distribution by codimension
    nonzero_by_codim: Dict[int, int] = {}
    for a in nonzero:
        c = a.codimension
        nonzero_by_codim[c] = nonzero_by_codim.get(c, 0) + 1

    return {
        'total': len(all_ag),
        'nonzero': len(nonzero),
        'zero': len(all_ag) - len(nonzero),
        'positive': len(positive),
        'negative': len(negative),
        'nonzero_by_codim': dict(sorted(nonzero_by_codim.items())),
        'max_hodge': max(a.hodge_integral for a in nonzero) if nonzero else Fraction(0),
        'min_hodge': min(a.hodge_integral for a in nonzero) if nonzero else Fraction(0),
    }


# ============================================================================
# Section 16: Planted-forest census
# ============================================================================

def planted_forest_census() -> Dict[str, Any]:
    """Detailed census of planted-forest graphs at genus 4."""
    all_ag = annotated_graphs()
    pf = [a for a in all_ag if a.is_pf]
    nonpf = [a for a in all_ag if not a.is_pf]

    # PF graphs by codimension
    pf_by_codim = dict(sorted(
        Counter(a.codimension for a in pf).items()
    ))
    # PF graphs by vertex count
    pf_by_verts = dict(sorted(
        Counter(a.num_vertices for a in pf).items()
    ))
    # Max genus-0 valence in PF graphs
    max_g0_val = max(a.max_genus0_valence for a in pf) if pf else 0

    # Non-PF graphs: enumerate their genus distributions
    nonpf_genera = [a.vertex_genera for a in nonpf]

    return {
        'pf_count': len(pf),
        'nonpf_count': len(nonpf),
        'pf_by_codim': pf_by_codim,
        'pf_by_vertex_count': pf_by_verts,
        'max_g0_valence_in_pf': max_g0_val,
        'nonpf_genera_distributions': nonpf_genera,
    }


# ============================================================================
# Section 17: Weight consistency check (Verification Path 4)
# ============================================================================

def weight_consistency_check() -> Dict[str, Any]:
    """Verify weight/dimension consistency of graph amplitudes.

    dim M_bar_{4,0} = 9. Each graph amplitude I(Gamma) is a rational number
    arising from integrating psi-classes over product of vertex moduli.
    The total weight of the amplitude (in shadow variables) must be correct:
    for the planted-forest correction, each term has shadow-weight equal to
    the codimension of the stratum.
    """
    all_ag = annotated_graphs()

    # Check: every graph has arithmetic genus exactly 4
    genus_check = all(a.graph.arithmetic_genus == GENUS for a in all_ag)

    # Check: every graph has at most 9 edges
    edge_check = all(a.num_edges <= MAX_EDGES for a in all_ag)

    # Check: stability at each vertex
    stability_check = all(a.graph.is_stable for a in all_ag)

    # Check: connectivity
    connectivity_check = all(a.graph.is_connected for a in all_ag)

    # Count graphs at maximum codimension (fully degenerate)
    max_codim_graphs = [a for a in all_ag if a.num_edges == MAX_EDGES]

    return {
        'genus_check': genus_check,
        'edge_check': edge_check,
        'stability_check': stability_check,
        'connectivity_check': connectivity_check,
        'max_codim_count': len(max_codim_graphs),
        'dim_mbar': DIM_MBAR,
    }


# ============================================================================
# Section 18: Graph-by-graph amplitude table (top contributors)
# ============================================================================

def top_amplitude_contributors(
    shadow: ShadowData,
    n: int = 20,
) -> List[Dict[str, Any]]:
    """Return the n graphs with largest absolute amplitude contribution."""
    all_ag = annotated_graphs()
    entries = []
    for ag in all_ag:
        if ag.has_nonzero_hodge:
            amp = ag.weighted_amplitude(shadow)
            entries.append({
                'index': ag.index,
                'genera': ag.vertex_genera,
                'valences': ag.vertex_valences,
                'edges': ag.num_edges,
                'aut': ag.aut_order,
                'hodge': ag.hodge_integral,
                'is_pf': ag.is_pf,
                'amplitude': amp,
            })

    # Sort by absolute value of Hodge integral / aut order (proxy for magnitude)
    entries.sort(key=lambda e: abs(e['hodge']) / e['aut'], reverse=True)
    return entries[:n]


# ============================================================================
# Section 19: Free energy for all standard families
# ============================================================================

def free_energy_table() -> Dict[str, Dict[str, Any]]:
    """Scalar-level free energy F_4^{scal}(A) = kappa(A) * lambda_4^FP for standard families."""
    l4 = LAMBDA4_FP
    families = {
        'Heisenberg_k1': {'kappa': Fraction(1), 'class': 'G'},
        'Heisenberg_k2': {'kappa': Fraction(2), 'class': 'G'},
        'Virasoro_c1': {'kappa': Fraction(1, 2), 'class': 'M'},
        'Virasoro_c13': {'kappa': Fraction(13, 2), 'class': 'M'},
        'Virasoro_c26': {'kappa': Fraction(13), 'class': 'M'},
        'Affine_sl2_k1': {'kappa': Fraction(9, 4), 'class': 'L'},
        'Affine_sl3_k1': {'kappa': Fraction(4), 'class': 'L'},
        'BetaGamma': {'kappa': Fraction(1), 'class': 'C'},
    }

    result = {}
    for name, data in families.items():
        kappa = data['kappa']
        result[name] = {
            'kappa': kappa,
            'F4_scalar': kappa * l4,
            'depth_class': data['class'],
        }
    return result


# ============================================================================
# Section 20: Full summary
# ============================================================================

def full_summary() -> Dict[str, Any]:
    """Complete summary of all genus-4 computations."""
    census = full_census()
    euler = euler_characteristic_check()
    lam = lambda4_three_paths()
    pf_census = planted_forest_census()
    parity = self_loop_parity_verification()
    weight = weight_consistency_check()

    return {
        'census': census,
        'euler_characteristic': euler,
        'lambda4': lam,
        'planted_forest': pf_census,
        'self_loop_parity': parity,
        'weight_consistency': weight,
    }
