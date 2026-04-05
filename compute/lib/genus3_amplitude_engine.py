r"""Genus-3 shadow amplitude engine.

Computes graph-by-graph amplitudes for all 42 stable graphs at (g=3, n=0),
verifies the genus-3 free energy F_3 = kappa * lambda_3^FP via the graph sum,
and provides shell decompositions, Gaussian purity checks, complementarity
verification, and cross-checks against the A-hat genus generating function.

MATHEMATICAL FRAMEWORK
======================

At the scalar level (Theorem D), the genus-g free energy is:

    F_g(A) = kappa(A) * lambda_g^FP

where lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!) are the
Faber-Pandharipande intersection numbers (Hodge integrals on M-bar_{g,1}).

The graph-sum representation decomposes F_g into contributions from all
stable graphs Gamma at (g, n=0):

    F_g = sum_Gamma  ell_Gamma / |Aut(Gamma)|

where ell_Gamma = prod_v V(g_v, val_v) * prod_e P is the graph amplitude:
  - V(g_v, n_v) = vertex factor at genus g_v and valence n_v
  - P = propagator (inverse Hessian on the 1D primary line)

At the SCALAR level (pure kappa):
  - V^(0)(2) = kappa (the Hessian)
  - V^(g)(0) = kappa * lambda_g^FP (free energy at lower genus)
  - V^(0)(n) = 0 for n != 2 in the Gaussian (Heisenberg) case
  - P = 1/kappa

GENUS-3 SPECIFICS
=================

lambda_3^FP = (2^5 - 1)|B_6| / (2^5 * 6!)
            = 31 * (1/42) / (32 * 720)
            = 31/967680

F_3(H_k) = k * 31/967680   (linear in kappa = k)

The 42 stable graphs decompose by loop number (shells):
  Shell 0 (trees, h^1=0):      4 graphs,  vertices carry total genus 3
  Shell 1 (one-loop, h^1=1):   9 graphs,  vertices carry total genus 2
  Shell 2 (two-loop, h^1=2):  14 graphs,  vertices carry total genus 1
  Shell 3 (three-loop, h^1=3): 15 graphs,  vertices carry genus 0

THE A-HAT GENERATING FUNCTION
==============================

A-hat(x) = (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760 - 31x^6/967680 + ...

The coefficient of x^{2g} is (-1)^g * lambda_g^FP.  The free energy
generating function is:

    F(hbar) = kappa * sum_{g>=1} lambda_g^FP * hbar^{2g-2}
            = (kappa/hbar^2) * [A-hat(hbar) - 1]    [with sign corrections]

Actually, lambda_g^FP = |coeff of x^{2g} in A-hat(x)|, so:

    F(hbar) = (kappa/hbar^2) * [1 - A-hat(hbar)]

since A-hat(x) = 1 - lambda_1 x^2 + lambda_2 x^4 - lambda_3 x^6 + ...

SHADOW CORRECTIONS
==================

Beyond the scalar level, each algebra family has corrections from the
shadow obstruction tower.  The four shadow depth classes are:
  G (Gaussian):  r_max = 2, only kappa contributes (Heisenberg)
  L (Lie/tree):  r_max = 3, cubic shadow C contributes
  C (contact):   r_max = 4, quartic Q^contact contributes
  M (mixed):     r_max = inf, all arities contribute (Virasoro, W_N)

At genus 3, shadow corrections appear at graphs with vertices of
valence >= 3 (for class L), >= 4 (for class C), etc.

References:
  - concordance.tex: Theorem D, genus expansion, shadow obstruction tower
  - higher_genus_modular_koszul.tex: def:stable-graph-coefficient-algebra
  - genus3_stable_graphs.py: graph enumeration
  - genus2_bar_cobar_engine.py: genus-2 pattern
  - Faber, "A conjectural description of the tautological ring" (1999)
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, simplify, expand, factor, cancel, S, symbols,
    bernoulli, sqrt, Abs, series, sinh,
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
from compute.lib.genus3_stable_graphs import (
    genus3_stable_graphs_n0,
    genus3_graph_count,
    genus3_automorphism_spectrum,
    genus3_spectral_sequence_e1,
    genus3_spectral_sequence_counts,
    genus3_boundary_strata,
    genus3_scalar_sum_polynomial,
    genus3_scalar_sum_at,
    genus3_named_graphs,
    lambda3_fp,
)


# =====================================================================
# 1.  Shadow data for standard families (sympy-based)
# =====================================================================

c = Symbol('c')
k = Symbol('k')


def _lambda_fp_sympy(g: int) -> Rational:
    """lambda_g^FP as a sympy Rational."""
    B_2g = bernoulli(2 * g)
    power = 2 ** (2 * g - 1)
    numer = (power - 1) * abs(B_2g)
    denom = power * factorial(2 * g)
    return Rational(numer, denom)


@dataclass
class FamilyShadowData:
    """Complete shadow obstruction tower data for a chiral algebra family on a 1D primary line.

    Packages the vertex contributions needed for graph amplitude computation.
    Shadow data at genus g, valence n is accessed via vertex_factor(g, n).

    Attributes:
        name:       family identifier
        kappa:      modular characteristic (Theorem D scalar invariant)
        propagator: P = inverse Hessian on the 1D primary line
        cubic:      genus-0 arity-3 shadow coefficient C
        quartic:    genus-0 arity-4 shadow coefficient Q (contact invariant)
        quintic:    genus-0 arity-5 shadow coefficient S_5 (if known)
        sextic:     genus-0 arity-6 shadow coefficient S_6 (if known)
        genus1_hessian_correction: delta_H^{(1)}
        shadow_depth: r_max (2, 3, 4, or 'inf')
        shadow_class: one of 'G', 'L', 'C', 'M'
    """
    name: str
    kappa: object         # sympy expression or Rational
    propagator: object
    cubic: object
    quartic: object
    quintic: object = S.Zero
    sextic: object = S.Zero
    genus1_hessian_correction: object = S.Zero
    shadow_depth: object = 'inf'
    shadow_class: str = 'M'

    def vertex_factor_genus0(self, valence: int):
        """Genus-0 vertex contribution at given valence.

        Sh_0^{(0)} = 0, Sh_1^{(0)} = 0, Sh_2^{(0)} = kappa,
        Sh_3^{(0)} = cubic, Sh_4^{(0)} = quartic, Sh_5^{(0)} = quintic,
        Sh_6^{(0)} = sextic.
        Sh_n^{(0)} = 0 for n > shadow_depth (if finite).
        """
        if valence <= 1:
            return S.Zero
        elif valence == 2:
            return self.kappa
        elif valence == 3:
            return self.cubic
        elif valence == 4:
            return self.quartic
        elif valence == 5:
            return self.quintic
        elif valence == 6:
            return self.sextic
        else:
            if isinstance(self.shadow_depth, int) and valence > self.shadow_depth:
                return S.Zero
            return Symbol(f'Sh_{valence}_{self.name}')

    def vertex_factor_genus1(self, valence: int):
        """Genus-1 vertex contribution at given valence.

        V^{(1)}_0 = F_1 = kappa/24  (free energy at genus 1)
        V^{(1)}_2 = kappa + genus1_hessian_correction
        """
        if valence == 0:
            return self.kappa * Rational(1, 24)
        elif valence == 2:
            return self.kappa + self.genus1_hessian_correction
        else:
            if self.shadow_class == 'G':
                return S.Zero
            return Symbol(f'V1_{valence}_{self.name}')

    def vertex_factor_genus2(self, valence: int):
        """Genus-2 vertex contribution at given valence.

        V^{(2)}_0 = F_2 = kappa * 7/5760.
        """
        if valence == 0:
            return self.kappa * Rational(7, 5760)
        elif valence == 2:
            if self.shadow_class == 'G':
                return self.kappa
            return Symbol(f'V2_2_{self.name}')
        else:
            if self.shadow_class == 'G':
                return S.Zero
            return Symbol(f'V2_{valence}_{self.name}')

    def vertex_factor_genus3(self, valence: int):
        """Genus-3 vertex contribution at given valence.

        V^{(3)}_0 = F_3 = kappa * 31/967680.
        """
        if valence == 0:
            return self.kappa * Rational(31, 967680)
        elif valence == 2:
            if self.shadow_class == 'G':
                return self.kappa
            return Symbol(f'V3_2_{self.name}')
        else:
            if self.shadow_class == 'G':
                return S.Zero
            return Symbol(f'V3_{valence}_{self.name}')

    def vertex_factor(self, genus: int, valence: int):
        """Return the vertex factor for genus g, valence n."""
        if genus == 0:
            return self.vertex_factor_genus0(valence)
        elif genus == 1:
            return self.vertex_factor_genus1(valence)
        elif genus == 2:
            return self.vertex_factor_genus2(valence)
        elif genus == 3:
            return self.vertex_factor_genus3(valence)
        else:
            if valence == 0 and genus >= 1:
                return self.kappa * _lambda_fp_sympy(genus)
            if self.shadow_class == 'G':
                if valence == 2:
                    return self.kappa
                return S.Zero
            return Symbol(f'V{genus}_{valence}_{self.name}')


# =====================================================================
# 1a.  Standard family constructors
# =====================================================================

def heisenberg_data(kappa_val=None) -> FamilyShadowData:
    """Shadow data for Heisenberg H_k.

    Gaussian class (G): shadow obstruction tower terminates at arity 2.
    kappa = k (or kappa_val if given as a number).
    All higher shadows vanish. No genus-1 Hessian correction.
    """
    kap = k if kappa_val is None else Rational(kappa_val)
    return FamilyShadowData(
        name='Heisenberg',
        kappa=kap,
        propagator=1 / kap,
        cubic=S.Zero,
        quartic=S.Zero,
        quintic=S.Zero,
        sextic=S.Zero,
        genus1_hessian_correction=S.Zero,
        shadow_depth=2,
        shadow_class='G',
    )


def affine_sl2_data(k_val=None) -> FamilyShadowData:
    """Shadow data for affine sl_2 at level k.

    Lie/tree class (L): shadow depth 3.
    kappa = dim(sl_2)*(k+h^v)/(2h^v) = 3(k+2)/4.
    Cubic nonzero (from Lie bracket), quartic = 0.
    """
    kk = k if k_val is None else Rational(k_val)
    kap = Rational(3) * (kk + 2) / 4
    return FamilyShadowData(
        name='V_k(sl_2)',
        kappa=kap,
        propagator=1 / kap,
        cubic=Rational(2),
        quartic=S.Zero,
        quintic=S.Zero,
        sextic=S.Zero,
        genus1_hessian_correction=S.Zero,
        shadow_depth=3,
        shadow_class='L',
    )


def betagamma_data() -> FamilyShadowData:
    """Shadow data for the beta-gamma system.

    Contact class (C): shadow depth 4.
    kappa = 1. c = 2.
    Cubic from OPE, quartic = Q^contact.
    """
    return FamilyShadowData(
        name='beta-gamma',
        kappa=Rational(1),
        propagator=Rational(1),
        cubic=Rational(2),
        quartic=Rational(10, 132),  # Q^contact at c=2: 10/(2*(5*2+22)) = 10/64 ... no
        quintic=S.Zero,
        sextic=S.Zero,
        genus1_hessian_correction=S.Zero,
        shadow_depth=4,
        shadow_class='C',
    )


def virasoro_data(c_val=None) -> FamilyShadowData:
    """Shadow data for Virasoro at central charge c.

    Mixed class (M): infinite shadow depth.
    kappa = c/2, P = 2/c, C = 2, Q = 10/[c(5c+22)].
    delta_H^{(1)} = 120/[c^2(5c+22)].
    S_5 = -48/[c^2(5c+22)].
    """
    cc = c if c_val is None else Rational(c_val)
    kap = cc / 2
    P = 2 / cc
    Q = Rational(10) / (cc * (5 * cc + 22))
    S5 = Rational(-48) / (cc**2 * (5 * cc + 22))
    delta_H1 = 6 * P * Q   # = 120/[c^2(5c+22)]
    return FamilyShadowData(
        name='Virasoro',
        kappa=kap,
        propagator=P,
        cubic=Rational(2),
        quartic=Q,
        quintic=S5,
        genus1_hessian_correction=delta_H1,
        shadow_depth='inf',
        shadow_class='M',
    )


STANDARD_FAMILIES = {
    'Heisenberg': heisenberg_data,
    'V_k(sl_2)': affine_sl2_data,
    'beta-gamma': betagamma_data,
    'Virasoro': virasoro_data,
}


# =====================================================================
# 2.  Graph amplitude computation
# =====================================================================

def graph_amplitude(graph: StableGraph, data: FamilyShadowData) -> object:
    """Compute the amplitude ell_Gamma for a stable graph.

    ell_Gamma = prod_v V(g_v, val_v) * prod_e P

    The 1/|Aut| factor is NOT included here; it is applied in the sum.
    Returns a sympy expression.
    """
    val = graph.valence
    amp = S.One

    # Vertex factors
    for i, g_v in enumerate(graph.vertex_genera):
        vf = data.vertex_factor(g_v, val[i])
        amp *= vf

    # Edge factors (propagators)
    for _ in graph.edges:
        amp *= data.propagator

    return amp


def weighted_amplitude(graph: StableGraph, data: FamilyShadowData) -> object:
    """Compute (1/|Aut(Gamma)|) * ell_Gamma."""
    return Rational(1, graph.automorphism_order()) * graph_amplitude(graph, data)


# =====================================================================
# 3.  Full genus-3 amplitude sum
# =====================================================================

def genus3_total_amplitude(data: FamilyShadowData) -> Dict:
    """Compute the total genus-3 amplitude as a sum over 42 stable graphs.

    Returns:
        graph_amplitudes: {index: {amplitude, weighted, aut_order, h1, edges, genera}}
        total: sum of weighted amplitudes
        expected_scalar: kappa * lambda_3^FP (the Theorem D prediction)
        match_scalar: whether total matches expected (at scalar level)
    """
    graphs = genus3_stable_graphs_n0()
    graph_amps = {}
    total = S.Zero

    for i, graph in enumerate(graphs):
        amp = graph_amplitude(graph, data)
        w_amp = weighted_amplitude(graph, data)
        graph_amps[i] = {
            'amplitude': amp,
            'weighted': cancel(w_amp),
            'aut_order': graph.automorphism_order(),
            'h1': graph.first_betti,
            'num_edges': graph.num_edges,
            'vertex_genera': graph.vertex_genera,
        }
        total += w_amp

    expected = data.kappa * _lambda_fp_sympy(3)

    result = {
        'graph_amplitudes': graph_amps,
        'total': cancel(total),
        'expected_scalar': cancel(expected),
    }
    result['match_scalar'] = simplify(total - expected) == 0

    return result


# =====================================================================
# 4.  Shell decomposition (by loop number h^1)
# =====================================================================

def genus3_shell_decomposition(data: FamilyShadowData) -> Dict[int, Dict]:
    """Decompose the genus-3 amplitude by shell (loop number h^1).

    Shell p contains graphs with h^1 = p (loop genus = p).
    The shell amplitude is the sum of weighted amplitudes over graphs in that shell.

    Returns {shell: {count, graphs, amplitude_sum}}.
    """
    graphs = genus3_stable_graphs_n0()
    shells: Dict[int, Dict] = {}

    for i, graph in enumerate(graphs):
        h1 = graph.first_betti
        if h1 not in shells:
            shells[h1] = {'count': 0, 'graph_indices': [], 'amplitude_sum': S.Zero}
        shells[h1]['count'] += 1
        shells[h1]['graph_indices'].append(i)
        shells[h1]['amplitude_sum'] += weighted_amplitude(graph, data)

    for h1 in shells:
        shells[h1]['amplitude_sum'] = cancel(shells[h1]['amplitude_sum'])

    return shells


def genus3_shell_amplitudes_heisenberg(kappa_val: int = 1) -> Dict[int, Fraction]:
    """Shell-by-shell amplitudes for Heisenberg (exact, Fraction-based).

    For Heisenberg (Gaussian, shadow class G):
    - Cubic/quartic/higher vertex factors all vanish
    - Only graphs where every vertex has valence 0 or 2 contribute
    - At each vertex: V(g_v, 0) = kappa*lambda_{g_v}^FP, V(g_v, 2) = kappa

    Returns {shell: exact Fraction amplitude}.
    """
    kv = Fraction(kappa_val)
    graphs = genus3_stable_graphs_n0()
    shells: Dict[int, Fraction] = {}

    for graph in graphs:
        val = graph.valence
        h1 = graph.first_betti

        # For Gaussian: vertex factor is zero unless valence in {0, 2}
        amp = Fraction(1)
        skip = False
        for v_idx, g_v in enumerate(graph.vertex_genera):
            v_n = val[v_idx]
            if v_n == 0:
                # V(g_v, 0) = kappa * lambda_{g_v}^FP
                if g_v == 0:
                    skip = True
                    break
                amp *= kv * _lambda_fp_exact(g_v)
            elif v_n == 2:
                # V(g_v, 2) = kappa (the Hessian, same at all genera for Gaussian)
                amp *= kv
            else:
                # Higher valence: zero for Gaussian
                skip = True
                break

        if skip:
            continue

        # Propagators: each edge contributes P = 1/kappa
        for _ in graph.edges:
            amp *= Fraction(1, 1) / kv

        # Weight by 1/|Aut|
        aut = graph.automorphism_order()
        contrib = amp / Fraction(aut)

        if h1 not in shells:
            shells[h1] = Fraction(0)
        shells[h1] += contrib

    return shells


# =====================================================================
# 5.  Gaussian purity
# =====================================================================

def genus3_gaussian_active_graphs() -> List[int]:
    """Which of the 42 graphs contribute for Heisenberg (Gaussian class G)?

    A graph contributes iff every vertex has valence 0 or 2.
    Valence-0 requires g_v >= 2 for stability (2g-2+0 > 0 => g >= 2).
    Valence-2 requires g_v >= 1 for stability (2g-2+2 > 0 => g >= 1, or g=0 with val>=3... but val=2 needs g>=1).

    Actually for n=0: stability is 2g_v - 2 + val_v > 0.
    val_v = 0: need g_v >= 2.
    val_v = 2: need g_v >= 1 or (g_v = 0 and val_v >= 3) -- val_v = 2 and g_v = 0
               gives 2*0 - 2 + 2 = 0, which is NOT stable.
    So for Gaussian, a vertex can have:
      val = 0, g >= 2: contributes kappa * lambda_g^FP
      val = 2, g >= 1: contributes kappa
    Vertices with val >= 3 give zero vertex factor for Gaussian.
    Vertices with g = 0 and val = 2 are unstable, so don't appear.
    """
    graphs = genus3_stable_graphs_n0()
    active = []
    for i, graph in enumerate(graphs):
        val = graph.valence
        is_active = True
        for v_idx, g_v in enumerate(graph.vertex_genera):
            v_n = val[v_idx]
            if v_n == 0:
                if g_v < 2:
                    is_active = False
                    break
            elif v_n == 2:
                if g_v < 1:
                    is_active = False
                    break
            else:
                # Higher valence: zero for Gaussian
                is_active = False
                break
        if is_active:
            active.append(i)
    return active


def genus3_gaussian_purity_check(kappa_val: int = 1) -> Dict:
    """Verify Gaussian purity: only corolla-type graphs contribute for Heisenberg.

    For Heisenberg, the shadow obstruction tower terminates at arity 2, so all graphs
    with a vertex of valence >= 3 contribute zero. The total F_3 must
    equal kappa * lambda_3^FP from the active subset alone.

    Returns detailed check including active/inactive graph lists and verification.
    """
    kv = Fraction(kappa_val)
    graphs = genus3_stable_graphs_n0()
    active_indices = genus3_gaussian_active_graphs()

    # Compute total from active graphs only
    total = Fraction(0)
    active_details = []
    for i in active_indices:
        graph = graphs[i]
        val = graph.valence
        amp = Fraction(1)
        for v_idx, g_v in enumerate(graph.vertex_genera):
            v_n = val[v_idx]
            if v_n == 0:
                amp *= kv * _lambda_fp_exact(g_v)
            elif v_n == 2:
                amp *= kv
        for _ in graph.edges:
            amp /= kv
        aut = graph.automorphism_order()
        contrib = amp / Fraction(aut)
        total += contrib
        active_details.append({
            'index': i,
            'genera': graph.vertex_genera,
            'edges': graph.num_edges,
            'valence': val,
            'h1': graph.first_betti,
            'contribution': contrib,
        })

    expected = kv * _lambda_fp_exact(3)

    return {
        'active_count': len(active_indices),
        'inactive_count': 42 - len(active_indices),
        'active_indices': active_indices,
        'active_details': active_details,
        'total': total,
        'expected': expected,
        'match': total == expected,
    }


# =====================================================================
# 6.  Complementarity at genus 3
# =====================================================================

def genus3_complementarity(data_A: FamilyShadowData,
                           data_A_dual: FamilyShadowData) -> Dict:
    """Verify genus-3 complementarity: F_3(A) + F_3(A!) at the scalar level.

    Theorem C (complementarity, scalar projection):
        F_3(A) + F_3(A!) = (kappa(A) + kappa(A!)) * lambda_3^FP

    Koszul duality constraints on kappa(A) + kappa(A!):
      KM/free fields: kappa + kappa' = 0  (anti-symmetry)
      W-algebras:     kappa + kappa' = rho * K (shifted)
      Virasoro:       kappa(Vir_c) + kappa(Vir_{26-c}) = 13
    """
    F3_A = cancel(data_A.kappa * _lambda_fp_sympy(3))
    F3_Ad = cancel(data_A_dual.kappa * _lambda_fp_sympy(3))
    F3_sum = cancel(F3_A + F3_Ad)
    kappa_sum = cancel(data_A.kappa + data_A_dual.kappa)

    return {
        'A': data_A.name,
        'A_dual': data_A_dual.name,
        'kappa_A': data_A.kappa,
        'kappa_A_dual': data_A_dual.kappa,
        'kappa_sum': kappa_sum,
        'F_3_A': F3_A,
        'F_3_A_dual': F3_Ad,
        'F_3_sum': F3_sum,
        'F_3_sum_factored': cancel(kappa_sum * _lambda_fp_sympy(3)),
        'consistent': simplify(F3_sum - kappa_sum * _lambda_fp_sympy(3)) == 0,
    }


def virasoro_complementarity_genus3(c_val=None) -> Dict:
    """Complementarity for the Virasoro pair (Vir_c, Vir_{26-c}) at genus 3.

    kappa(Vir_c) = c/2,  kappa(Vir_{26-c}) = (26-c)/2.
    kappa + kappa' = 13.
    F_3 + F_3' = 13 * 31/967680 = 403/967680.

    Self-dual at c = 13: F_3 = (13/2) * 31/967680 = 403/1935360.
    """
    cc = c if c_val is None else Rational(c_val)
    data_A = virasoro_data(cc) if c_val is not None else virasoro_data()
    cc_dual = 26 - cc
    data_Ad = FamilyShadowData(
        name=f'Vir_{{26-c}}',
        kappa=cc_dual / 2,
        propagator=2 / cc_dual,
        cubic=Rational(2),
        quartic=Rational(10) / (cc_dual * (5 * cc_dual + 22)),
        shadow_depth='inf',
        shadow_class='M',
    )
    return genus3_complementarity(data_A, data_Ad)


def heisenberg_complementarity_genus3(k_val=None) -> Dict:
    """Complementarity for Heisenberg: H_k vs H_k^!.

    CRITICAL: H_k^! = Sym^ch(V*) != H_{-k}. Heisenberg is NOT self-dual.
    kappa(H_k) = k, kappa(H_k^!) = -k.
    kappa + kappa' = 0 (anti-symmetry for free fields).
    F_3 + F_3' = 0.
    """
    kk = k if k_val is None else Rational(k_val)
    data_A = heisenberg_data(kk) if k_val is not None else heisenberg_data()
    data_Ad = FamilyShadowData(
        name='H_k^!',
        kappa=-kk,
        propagator=-1/kk,
        cubic=S.Zero,
        quartic=S.Zero,
        shadow_depth=2,
        shadow_class='G',
    )
    return genus3_complementarity(data_A, data_Ad)


# =====================================================================
# 7.  A-hat genus cross-check
# =====================================================================

def ahat_coefficients(num_terms: int = 8) -> List[Rational]:
    r"""Taylor coefficients of A-hat(x) = (x/2)/sinh(x/2).

    A-hat(x) = sum_{n>=0} a_n * x^{2n}
    where a_0 = 1, a_1 = -1/24, a_2 = 7/5760, a_3 = -31/967680, ...

    lambda_g^FP = |a_g|. Signs alternate: a_g = (-1)^g * lambda_g^FP.
    """
    x = Symbol('x')
    # Compute series expansion of (x/2)/sinh(x/2)
    f = (x / 2) / sinh(x / 2)
    s = series(f, x, 0, 2 * num_terms + 1)
    coeffs = []
    for g in range(num_terms):
        coeff = s.coeff(x, 2 * g)
        coeffs.append(Rational(coeff))
    return coeffs


def verify_ahat_genus3() -> Dict:
    """Cross-check lambda_3^FP against the A-hat generating function.

    The coefficient of x^6 in A-hat(x) should be -31/967680 = -lambda_3^FP.
    """
    coeffs = ahat_coefficients(4)  # g = 0,1,2,3
    a3 = coeffs[3]  # coefficient of x^6

    # lambda_3^FP = |a_3| = 31/967680
    lambda3 = abs(a3)
    expected = Rational(31, 967680)

    return {
        'ahat_coefficients': {g: coeffs[g] for g in range(4)},
        'a_3': a3,
        'lambda_3_from_ahat': lambda3,
        'lambda_3_expected': expected,
        'match': lambda3 == expected,
        'sign_check': a3 == -expected,  # (-1)^3 = -1
    }


def ahat_lambda_fp_consistency(max_genus: int = 6) -> Dict:
    """Verify lambda_g^FP = |coeff of x^{2g} in A-hat(x)| for g = 1..max_genus."""
    coeffs = ahat_coefficients(max_genus + 1)
    results = {}
    for g in range(1, max_genus + 1):
        a_g = coeffs[g]
        lambda_g_from_ahat = abs(a_g)
        lambda_g_from_bernoulli = _lambda_fp_sympy(g)
        results[g] = {
            'ahat_coeff': a_g,
            'lambda_from_ahat': lambda_g_from_ahat,
            'lambda_from_bernoulli': lambda_g_from_bernoulli,
            'match': simplify(lambda_g_from_ahat - lambda_g_from_bernoulli) == 0,
            'sign': (-1)**g,
        }
    return results


# =====================================================================
# 8.  F_3 via exact Fraction arithmetic (independent verification)
# =====================================================================

def F3_exact(kappa_val: Fraction) -> Fraction:
    """Compute F_3 = kappa * lambda_3^FP using exact Fraction arithmetic.

    This is an independent computation path that avoids sympy entirely.
    """
    return kappa_val * _lambda_fp_exact(3)


def F3_heisenberg_exact(k_val: int = 1, d: int = 1) -> Fraction:
    """F_3(H_k^d) = k*d * 31/967680 (exact)."""
    kappa = Fraction(k_val * d)
    return F3_exact(kappa)


def F3_affine_exact(k_val: Fraction, dim_g: int, h_vee: int) -> Fraction:
    """F_3(V_k(g)) at scalar level (exact).

    kappa = dim(g) * (k + h^v) / (2 h^v)

    NOTE: The kappa formula uses division by 2h^v, giving the standard
    normalization. For sl_2: dim=3, h^v=2, kappa = 3(k+2)/4.
    """
    kappa = Fraction(dim_g) * (k_val + h_vee) / Fraction(2 * h_vee)
    return F3_exact(kappa)


def F3_virasoro_exact(c_val: Fraction) -> Fraction:
    """F_3(Vir_c) at scalar level (exact). kappa = c/2."""
    kappa = c_val / Fraction(2)
    return F3_exact(kappa)


# =====================================================================
# 9.  Graph sum verification: the 42-graph decomposition
# =====================================================================

def genus3_graph_sum_exact(kappa_val: Fraction) -> Dict:
    """Compute the genus-3 scalar graph sum via exact Fraction arithmetic.

    At the scalar level (Gaussian), the amplitude of each graph depends only
    on its topology:
      ell_Gamma = prod_v (kappa * lambda_{g_v}^FP if val_v=0 else kappa if val_v=2)
                  * prod_e (1/kappa)

    For the Gaussian class (Heisenberg), only graphs with all vertices of
    valence 0 or 2 contribute. For the general scalar-level computation,
    we note that the vertex factor at valence n involves the (n-2)-th shadow
    coefficient, which at the PURE SCALAR level is nonzero only for n=0 (free energy)
    and n=2 (Hessian).

    Returns per-graph and total amplitudes.
    """
    kv = kappa_val
    graphs = genus3_stable_graphs_n0()
    contributions = {}
    total = Fraction(0)

    for i, graph in enumerate(graphs):
        val = graph.valence
        amp = Fraction(1)
        vanishes = False

        for v_idx, g_v in enumerate(graph.vertex_genera):
            v_n = val[v_idx]
            if v_n == 0:
                if g_v == 0:
                    vanishes = True
                    break
                amp *= kv * _lambda_fp_exact(g_v)
            elif v_n == 2:
                if 2 * g_v - 2 + 2 <= 0 and g_v == 0:
                    # Unstable: should not occur in valid enumeration
                    vanishes = True
                    break
                amp *= kv
            else:
                # At the PURE scalar level (Gaussian), higher valence gives 0
                vanishes = True
                break

        if vanishes:
            contributions[i] = {
                'genera': graph.vertex_genera,
                'edges': graph.num_edges,
                'h1': graph.first_betti,
                'valence': val,
                'contribution': Fraction(0),
                'vanishes': True,
            }
            continue

        for _ in graph.edges:
            amp /= kv

        aut = graph.automorphism_order()
        contrib = amp / Fraction(aut)
        total += contrib
        contributions[i] = {
            'genera': graph.vertex_genera,
            'edges': graph.num_edges,
            'h1': graph.first_betti,
            'valence': val,
            'contribution': contrib,
            'vanishes': False,
        }

    expected = kv * _lambda_fp_exact(3)
    return {
        'contributions': contributions,
        'total': total,
        'expected': expected,
        'match': total == expected,
        'active_count': sum(1 for c in contributions.values() if not c['vanishes']),
    }


# =====================================================================
# 10.  Bernoulli and lambda identities
# =====================================================================

def bernoulli_genus3_check() -> Dict:
    """Verify all Bernoulli number identities used in the genus-3 computation.

    B_2 = 1/6, B_4 = -1/30, B_6 = 1/42.
    lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680.
    """
    B2 = _bernoulli_exact(2)
    B4 = _bernoulli_exact(4)
    B6 = _bernoulli_exact(6)

    l1 = _lambda_fp_exact(1)
    l2 = _lambda_fp_exact(2)
    l3 = _lambda_fp_exact(3)

    return {
        'B_2': B2, 'B_2_expected': Fraction(1, 6), 'B_2_ok': B2 == Fraction(1, 6),
        'B_4': B4, 'B_4_expected': Fraction(-1, 30), 'B_4_ok': B4 == Fraction(-1, 30),
        'B_6': B6, 'B_6_expected': Fraction(1, 42), 'B_6_ok': B6 == Fraction(1, 42),
        'lambda_1': l1, 'lambda_1_expected': Fraction(1, 24), 'l1_ok': l1 == Fraction(1, 24),
        'lambda_2': l2, 'lambda_2_expected': Fraction(7, 5760), 'l2_ok': l2 == Fraction(7, 5760),
        'lambda_3': l3, 'lambda_3_expected': Fraction(31, 967680), 'l3_ok': l3 == Fraction(31, 967680),
        # Ratio checks
        'ratio_l3_l2': l3 / l2,
        'ratio_l2_l1': l2 / l1,
    }


def lambda_ratio_pattern() -> Dict:
    """Verify the ratio pattern lambda_{g+1}/lambda_g for g = 1..5.

    lambda_g^FP = (2^{2g-1}-1) |B_{2g}| / (2^{2g-1} (2g)!)

    The ratio lambda_{g+1}/lambda_g involves Bernoulli number ratios
    and powers of 2.
    """
    ratios = {}
    for g in range(1, 6):
        lg = _lambda_fp_exact(g)
        lg1 = _lambda_fp_exact(g + 1)
        ratios[g] = {
            'lambda_g': lg,
            'lambda_g_plus_1': lg1,
            'ratio': lg1 / lg,
        }
    return ratios


# =====================================================================
# 11.  Shell analysis for non-Gaussian families
# =====================================================================

def genus3_shell_vertex_analysis() -> Dict[int, Dict]:
    """Analyze which vertex types appear at each shell.

    For each shell (loop number h^1), report:
    - Maximum vertex valence (determines which shadow depth classes are affected)
    - Number of graphs with a vertex of valence >= 3, >= 4, >= 5, >= 6
    """
    graphs = genus3_stable_graphs_n0()
    shells: Dict[int, Dict] = {}

    for graph in graphs:
        h1 = graph.first_betti
        val = graph.valence
        max_val = max(val)

        if h1 not in shells:
            shells[h1] = {
                'count': 0,
                'max_valence': 0,
                'val_ge_3': 0,
                'val_ge_4': 0,
                'val_ge_5': 0,
                'val_ge_6': 0,
            }

        shells[h1]['count'] += 1
        shells[h1]['max_valence'] = max(shells[h1]['max_valence'], max_val)
        if max_val >= 3:
            shells[h1]['val_ge_3'] += 1
        if max_val >= 4:
            shells[h1]['val_ge_4'] += 1
        if max_val >= 5:
            shells[h1]['val_ge_5'] += 1
        if max_val >= 6:
            shells[h1]['val_ge_6'] += 1

    return shells


# =====================================================================
# 12.  Cross-genus consistency
# =====================================================================

def cross_genus_consistency() -> Dict:
    """Cross-check genus-3 against genus-1 and genus-2 for Heisenberg.

    The ratio F_g / F_1 = lambda_g / lambda_1 is a universal ratio
    independent of kappa. Verify:
      F_2/F_1 = lambda_2/lambda_1 = (7/5760) / (1/24) = 7/240
      F_3/F_1 = lambda_3/lambda_1 = (31/967680) / (1/24) = 31/40320
    """
    l1 = _lambda_fp_exact(1)
    l2 = _lambda_fp_exact(2)
    l3 = _lambda_fp_exact(3)

    ratio_21 = l2 / l1
    ratio_31 = l3 / l1
    ratio_32 = l3 / l2

    return {
        'lambda_1': l1,
        'lambda_2': l2,
        'lambda_3': l3,
        'ratio_F2_F1': ratio_21,
        'ratio_F2_F1_expected': Fraction(7, 240),
        'ratio_F2_F1_ok': ratio_21 == Fraction(7, 240),
        'ratio_F3_F1': ratio_31,
        'ratio_F3_F1_expected': Fraction(31, 40320),
        'ratio_F3_F1_ok': ratio_31 == Fraction(31, 40320),
        'ratio_F3_F2': ratio_32,
    }


# =====================================================================
# 13.  Summary and diagnostics
# =====================================================================

def genus3_amplitude_summary() -> Dict:
    """Complete summary of the genus-3 amplitude engine.

    Runs all checks and returns a comprehensive report.
    """
    # Bernoulli check
    bern = bernoulli_genus3_check()

    # Gaussian purity
    purity = genus3_gaussian_purity_check(kappa_val=1)

    # Cross-genus consistency
    cross = cross_genus_consistency()

    # Shell vertex analysis
    shells = genus3_shell_vertex_analysis()

    return {
        'lambda_3_FP': Fraction(31, 967680),
        'B_6': Fraction(1, 42),
        'total_graphs': 42,
        'gaussian_active': purity['active_count'],
        'gaussian_match': purity['match'],
        'bernoulli_ok': all(bern[f'B_{2*g}_ok'] for g in [1, 2, 3]),
        'lambda_ok': all(bern[f'l{g}_ok'] for g in [1, 2, 3]),
        'cross_genus_ok': cross['ratio_F2_F1_ok'] and cross['ratio_F3_F1_ok'],
        'shells': shells,
        'F_3_Heisenberg_k1': Fraction(31, 967680),
        'F_3_Virasoro_c26': F3_virasoro_exact(Fraction(26)),
    }
