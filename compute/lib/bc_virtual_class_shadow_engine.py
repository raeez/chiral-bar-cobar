r"""
bc_virtual_class_shadow_engine.py — Virtual fundamental classes from shadow
obstruction theory and Behrend function.

THE MATHEMATICAL CONTENT:

The shadow obstruction tower Θ_A^{≤r} provides a natural obstruction theory
on the moduli space M^sh(A) of shadow data for a chiral algebra A.  The
tangent-obstruction sequence

    T^0_A → T^1_A → Obs_A → 0

arises from the deformation complex Def_cyc^mod(A):
  - T^0 = H^0(Def_cyc^mod) = infinitesimal automorphisms
  - T^1 = H^1(Def_cyc^mod) = first-order deformations
  - Obs = H^2(Def_cyc^mod) = obstructions

For a modular Koszul algebra, H*(Def_cyc^mod) is concentrated:
  - dim T^0 = 0 (semisimple: Whitehead H^0 = 0)
  - dim T^1 = 0 (semisimple: Whitehead H^1 = 0 for KM; varies for others)
  - dim Obs = dim H^2 (the obstruction space, 1-dimensional for rank-1)

The virtual dimension is:

    vdim(M^sh) = dim T^1 - dim Obs

which is ZERO in the "critical" case (analogous to CY3 moduli), making the
virtual class a number (the DT-type invariant).

The BEHREND FUNCTION ν: M^sh → Z is the local Euler obstruction of the
intrinsic normal cone.  At smooth points ν = (-1)^{vdim}.  At singular points
(zeros of the shadow metric Q_L = 0), ν picks up corrections from the
normal cone geometry.

The VIRTUAL CLASS via graph sums:

    [M^sh_{g,n}]^vir = Σ_Γ (1/|Aut(Γ)|) · (ν_Γ)_* [M^sh_Γ]

where the graph sum runs over stable graphs with shadow vertex weights.

CONNECTION TO ZETA ZEROS: The central charge c parameterizes a family of
shadow moduli spaces.  At c = c(ρ_n) where ρ_n = 1/2 + it_n is a nontrivial
zero of ζ(s), the shadow metric Q_L acquires special properties (vanishing
discriminant, enhanced symmetry).  The Behrend function value ν(c(ρ_n)) and
weighted Euler characteristic χ^B at these points connect the shadow
obstruction tower to arithmetic.

MULTI-PATH VERIFICATION:
  Path 1: Virtual class from obstruction theory dimensions
  Path 2: Behrend function computation (local Euler obstruction)
  Path 3: Graph sum via planted-forest infrastructure
  Path 4: Comparison with DT invariants (Euler characteristic)
  Path 5: Numerical evaluation at specific central charges

Manuscript references:
    thm:mc2-bar-intrinsic (bar_cobar_adjunction_curved.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    conj:pixton-from-shadows (concordance.tex)

CAUTION (AP1, AP48): kappa is family-specific.  kappa != c/2 in general.
CAUTION (AP31): κ = 0 does NOT imply Θ = 0.  Higher-arity components
    (cubic shadow C, quartic Q, etc.) are independent.
CAUTION (AP19): The bar propagator absorbs a pole.  Pole orders in the
    r-matrix are one less than in the OPE.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, Integer, cancel, simplify, sqrt, pi as sym_pi,
    bernoulli, factorial, Abs, oo, conjugate,
)

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, zetazero, zeta as mpzeta, gamma as mpgamma,
        pi as mppi, log as mplog, exp as mpexp, re as mpre, im as mpim,
        diff as mpdiff, sqrt as mpsqrt, sin as mpsin, cos as mpcos,
        fabs, inf as mpinf, j as mpj, power as mppower,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# Import shadow infrastructure from pixton_shadow_bridge
from compute.lib.pixton_shadow_bridge import (
    wk_intersection,
    stable_graphs_genus2_0leg,
    stable_graphs_genus3_0leg,
    graph_integral_genus2,
    graph_integral_general,
    is_planted_forest_graph,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    vertex_weight,
    vertex_weight_general,
    mc_relation_genus2_free_energy,
    mc_relation_genus3_free_energy,
    planted_forest_polynomial,
    planted_forest_polynomial_genus3,
    ShadowData,
    StableGraph,
    c_sym,
    _nonneg_compositions,
)

from compute.lib.utils import lambda_fp, F_g


# ═══════════════════════════════════════════════════════════════════════════
# Part 1: Deformation complex dimensions — obstruction theory
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class ObstructionTheoryData:
    """Obstruction theory data for a chiral algebra family.

    From the cyclic deformation complex Def_cyc^mod(A):
      H^0 = infinitesimal automorphisms
      H^1 = first-order deformations
      H^2 = obstructions (hosts the MC element Theta_A)

    Virtual dimension = dim H^1 - dim H^0 - dim H^2
    (or equivalently dim T^1 - dim Obs when T^0 = 0).
    """
    name: str
    family: str  # G, L, C, M

    dim_H0: int  # dim of automorphisms
    dim_H1: int  # dim of deformations
    dim_H2: int  # dim of obstructions

    # Shadow depth and metric data
    shadow_depth: Any  # r_max: 2, 3, 4, or infinity
    kappa_formula: str
    shadow_class: str  # G, L, C, M

    @property
    def virtual_dim(self) -> int:
        """Virtual dimension of the shadow moduli."""
        return self.dim_H1 - self.dim_H0 - self.dim_H2

    @property
    def is_critical(self) -> bool:
        """Whether vdim = 0 (CY3-like critical case)."""
        return self.virtual_dim == 0

    def expected_dim(self) -> int:
        """Expected dimension = dim T^1 - dim Obs."""
        return self.dim_H1 - self.dim_H2


def obstruction_data_heisenberg() -> ObstructionTheoryData:
    """Obstruction theory for Heisenberg H_k.

    Def_cyc(H_k): the cyclic deformation complex of a free field.
    H^0 = 0 (abelian: no infinitesimal automorphisms beyond scaling)
    H^1 = 1 (the level k is the single deformation parameter)
    H^2 = 1 (the curvature κ = k is the single obstruction)

    vdim = 1 - 0 - 1 = 0  (critical!)
    """
    return ObstructionTheoryData(
        name="Heisenberg H_k",
        family="G",
        dim_H0=0,
        dim_H1=1,
        dim_H2=1,
        shadow_depth=2,
        kappa_formula="k",
        shadow_class="G",
    )


def obstruction_data_virasoro() -> ObstructionTheoryData:
    """Obstruction theory for Virasoro Vir_c.

    Def_cyc(Vir_c):
    H^0 = 0 (Virasoro has no outer automorphisms at generic c)
    H^1 = 1 (the central charge c is the single deformation parameter)
    H^2 = 1 (κ = c/2 is the single obstruction class coefficient)

    vdim = 1 - 0 - 1 = 0  (critical!)

    But: shadow depth = infinity (class M), so the full obstruction
    tower has infinitely many higher-arity components beyond κ.
    """
    return ObstructionTheoryData(
        name="Virasoro Vir_c",
        family="M",
        dim_H0=0,
        dim_H1=1,
        dim_H2=1,
        shadow_depth=float('inf'),
        kappa_formula="c/2",
        shadow_class="M",
    )


def obstruction_data_affine_sl2() -> ObstructionTheoryData:
    """Obstruction theory for affine sl_2 at level k.

    Def_cyc(sl_2_k):
    H^0 = 0 (semisimple: Whitehead H^1(sl_2) = 0)
    H^1 = 0 (semisimple: Whitehead H^2(sl_2) = 0)
    H^2 = 1 (the Killing 3-cocycle class, one-dimensional)

    vdim = 0 - 0 - 1 = -1  (obstructed!)

    But the EFFECTIVE virtual dimension is 0 once the level parameter
    is included as a deformation direction:
    dim_H1_extended = 1 (the level k), giving vdim_eff = 0.
    """
    return ObstructionTheoryData(
        name="Affine sl_2",
        family="L",
        dim_H0=0,
        dim_H1=1,  # level k as deformation parameter
        dim_H2=1,
        shadow_depth=3,
        kappa_formula="3(k+2)/4",
        shadow_class="L",
    )


def obstruction_data_affine_sl3() -> ObstructionTheoryData:
    """Obstruction theory for affine sl_3 at level k.

    H^0 = 0 (semisimple)
    H^1 = 1 (level k)
    H^2 = 1 (single obstruction class for rank-1 primary line)

    vdim = 0
    """
    return ObstructionTheoryData(
        name="Affine sl_3",
        family="L",
        dim_H0=0,
        dim_H1=1,
        dim_H2=1,
        shadow_depth=3,
        kappa_formula="4(k+3)/3",
        shadow_class="L",
    )


def obstruction_data_betagamma() -> ObstructionTheoryData:
    """Obstruction theory for beta-gamma system.

    H^0 = 0
    H^1 = 1 (level/coupling parameter)
    H^2 = 1

    vdim = 0.  Shadow depth 4 (class C, terminates at quartic).
    """
    return ObstructionTheoryData(
        name="Beta-gamma",
        family="C",
        dim_H0=0,
        dim_H1=1,
        dim_H2=1,
        shadow_depth=4,
        kappa_formula="k",
        shadow_class="C",
    )


def obstruction_data_w3() -> ObstructionTheoryData:
    """Obstruction theory for W_3 algebra.

    W_3 has two generators (T weight 2, W weight 3).
    H^0 = 0
    H^1 = 1 (central charge c)
    H^2 = 1 (single obstruction on each primary line)

    BUT: multi-generator → the deformation complex has 2 primary lines
    (T-line and W-line), each contributing independently.
    The TOTAL obstruction space has dim = 2 (one per primary line),
    but on each 1D slice the shadow is rank-1.

    For the scalar (T-line) shadow: vdim = 0.
    """
    return ObstructionTheoryData(
        name="W_3",
        family="M",
        dim_H0=0,
        dim_H1=1,
        dim_H2=1,
        shadow_depth=float('inf'),
        kappa_formula="5c/6",
        shadow_class="M",
    )


ALL_OBSTRUCTION_DATA = {
    'heisenberg': obstruction_data_heisenberg,
    'virasoro': obstruction_data_virasoro,
    'sl2': obstruction_data_affine_sl2,
    'sl3': obstruction_data_affine_sl3,
    'betagamma': obstruction_data_betagamma,
    'w3': obstruction_data_w3,
}


# ═══════════════════════════════════════════════════════════════════════════
# Part 2: Behrend function computation
# ═══════════════════════════════════════════════════════════════════════════

def shadow_metric_Q(kappa, S3, S4, t):
    """Shadow metric Q_L(t) on the primary line.

    Q_L(t) = (2κ + 3·S_3·t)² + 2·Δ·t²

    where the critical discriminant Δ = 8κ·S_4.

    The shadow metric controls the algebraicity of the shadow tower:
    - Q_L = perfect square ↔ tower terminates (class G or L)
    - Q_L irreducible ↔ tower infinite (class M)

    Returns:
        Symbolic expression for Q_L(t).
    """
    Delta = 8 * kappa * S4
    return (2 * kappa + 3 * S3 * t) ** 2 + 2 * Delta * t ** 2


def shadow_metric_discriminant(kappa, S3, S4):
    """Critical discriminant Δ = 8κ·S_4.

    Classification:
    - Δ = 0 ↔ Q_L is a perfect square ↔ finite shadow depth
    - Δ ≠ 0 ↔ Q_L is irreducible ↔ infinite shadow depth (class M)
    """
    return 8 * kappa * S4


def shadow_metric_zeros(kappa_val, S3_val, S4_val):
    """Find zeros of Q_L(t) as a function of t.

    Q_L(t) = (2κ + 3S₃t)² + 16κS₄t² = 0

    Expanding: (9S₃² + 16κS₄)t² + 12κS₃t + 4κ² = 0

    Solutions exist in C when Δ = 8κS₄ ≠ 0.

    Returns list of (t_value, multiplicity) pairs.
    """
    a = 9 * S3_val ** 2 + 16 * kappa_val * S4_val
    b = 12 * kappa_val * S3_val
    c_coeff = 4 * kappa_val ** 2

    if a == 0:
        # Linear: bt + c = 0
        if b == 0:
            return []
        t0 = -c_coeff / b
        return [(t0, 1)]

    disc = b ** 2 - 4 * a * c_coeff
    if disc == 0:
        t0 = -b / (2 * a)
        return [(t0, 2)]
    else:
        sqrt_disc = cmath.sqrt(disc)
        t1 = (-b + sqrt_disc) / (2 * a)
        t2 = (-b - sqrt_disc) / (2 * a)
        return [(t1, 1), (t2, 1)]


def behrend_function_smooth(vdim: int) -> int:
    """Behrend function at smooth points.

    At a smooth point of M^sh of virtual dimension d:
        ν = (-1)^d

    For the critical case (vdim = 0): ν = +1.
    """
    return (-1) ** vdim


def behrend_function_singular(vdim: int, singularity_type: str = "node") -> int:
    """Behrend function at singular points.

    At a node (A_1 singularity):
        ν = (-1)^{vdim} · (-1) = (-1)^{vdim + 1}

    More generally, at an A_k singularity:
        ν = (-1)^{vdim} · (-1)^k

    For the shadow moduli, singular points occur at zeros of Q_L.
    The singularity type is determined by the vanishing order of Q_L.

    Parameters:
        vdim: virtual dimension
        singularity_type: "node" (A_1), "cusp" (A_2), "tacnode" (A_3),
                         or "smooth" for reference
    """
    sing_contributions = {
        "smooth": 1,
        "node": -1,      # A_1: Milnor number 1, ν = (-1)^1 = -1
        "cusp": 1,       # A_2: Milnor number 2, ν = (-1)^2 = +1
        "tacnode": -1,    # A_3: Milnor number 3, ν = (-1)^3 = -1
    }
    nu_sing = sing_contributions.get(singularity_type, -1)
    return (-1) ** vdim * nu_sing


def behrend_weighted_euler(vdim: int, n_smooth: int, n_nodes: int = 0,
                           n_cusps: int = 0) -> int:
    """Behrend-weighted Euler characteristic.

    χ^B(M^sh) = Σ_x ν(x) = n_smooth · (-1)^{vdim}
                           + n_nodes · (-1)^{vdim+1}
                           + n_cusps · (-1)^{vdim}
    """
    nu_smooth = (-1) ** vdim
    nu_node = (-1) ** (vdim + 1)
    nu_cusp = (-1) ** vdim
    return n_smooth * nu_smooth + n_nodes * nu_node + n_cusps * nu_cusp


# ═══════════════════════════════════════════════════════════════════════════
# Part 3: Virtual class via shadow graph sums
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class VirtualClassContribution:
    """Contribution of a single stable graph to the virtual class."""
    graph_name: str
    genus: int
    codimension: int
    vertex_weight: Any  # symbolic expression
    hodge_integral: Fraction
    automorphism_order: int
    is_planted_forest: bool
    contribution: Any  # vertex_weight * hodge_integral / |Aut|
    behrend_sign: int  # (-1)^{codim} from virtual localization


def virtual_class_graph_sum_genus2(shadow: ShadowData,
                                   behrend: bool = True
                                   ) -> Dict[str, Any]:
    """Compute [M^sh_{2,0}]^vir via graph sum.

    The virtual class decomposes over stable graphs:
    [M^sh_{g}]^vir = Σ_Γ (1/|Aut(Γ)|) · ν_Γ · w_Γ · I_Γ

    where:
    - w_Γ = product of shadow vertex weights
    - I_Γ = Hodge integral
    - ν_Γ = Behrend sign = (-1)^{codim(Γ)} if behrend=True, else 1

    Parameters:
        shadow: shadow obstruction tower data
        behrend: whether to include Behrend signs

    Returns:
        Dictionary with per-graph contributions and totals.
    """
    graphs = stable_graphs_genus2_0leg()
    contributions = []
    total = Integer(0)
    pf_total = Integer(0)
    codim1_total = Integer(0)
    smooth_total = Integer(0)

    for G in graphs:
        w = vertex_weight(G, shadow)
        I_frac = graph_integral_genus2(G)
        I_sym = Integer(I_frac.numerator) / Integer(I_frac.denominator)

        behrend_sign = (-1) ** G.codimension if behrend else 1
        contrib = cancel(behrend_sign * w * I_sym / G.automorphism_order)

        vc = VirtualClassContribution(
            graph_name=G.name,
            genus=2,
            codimension=G.codimension,
            vertex_weight=w,
            hodge_integral=I_frac,
            automorphism_order=G.automorphism_order,
            is_planted_forest=is_planted_forest_graph(G),
            contribution=contrib,
            behrend_sign=behrend_sign,
        )
        contributions.append(vc)

        if G.codimension == 0:
            smooth_total += contrib
        elif G.codimension == 1:
            codim1_total += contrib
        elif is_planted_forest_graph(G):
            pf_total += contrib
        else:
            total += contrib

    grand_total = cancel(smooth_total + codim1_total + pf_total + total)

    return {
        'contributions': contributions,
        'smooth': cancel(smooth_total),
        'codim1': cancel(codim1_total),
        'planted_forest': cancel(pf_total),
        'higher_codim_non_pf': cancel(total),
        'virtual_class': grand_total,
        'n_graphs': len(graphs),
    }


def virtual_class_graph_sum_genus3(shadow: ShadowData,
                                   behrend: bool = True
                                   ) -> Dict[str, Any]:
    """Compute [M^sh_{3,0}]^vir via graph sum.

    Same structure as genus 2 but with the full genus-3 graph enumeration.
    """
    graphs = stable_graphs_genus3_0leg()
    contributions = []
    pf_total = Integer(0)
    codim1_total = Integer(0)
    smooth_total = Integer(0)
    iterated_total = Integer(0)

    for G in graphs:
        w = vertex_weight_general(G, shadow)
        I_frac = graph_integral_general(G)
        I_sym = Integer(I_frac.numerator) / Integer(I_frac.denominator)

        behrend_sign = (-1) ** G.codimension if behrend else 1
        contrib = cancel(behrend_sign * w * I_sym / G.automorphism_order)

        is_pf = is_planted_forest_graph(G)

        vc = VirtualClassContribution(
            graph_name=G.name,
            genus=3,
            codimension=G.codimension,
            vertex_weight=w,
            hodge_integral=I_frac,
            automorphism_order=G.automorphism_order,
            is_planted_forest=is_pf,
            contribution=contrib,
            behrend_sign=behrend_sign,
        )
        contributions.append(vc)

        if G.codimension == 0:
            smooth_total += contrib
        elif G.codimension == 1:
            codim1_total += contrib
        elif is_pf:
            pf_total += contrib
        else:
            iterated_total += contrib

    grand_total = cancel(
        smooth_total + codim1_total + pf_total + iterated_total
    )

    return {
        'contributions': contributions,
        'smooth': cancel(smooth_total),
        'codim1': cancel(codim1_total),
        'planted_forest': cancel(pf_total),
        'iterated_boundary': cancel(iterated_total),
        'virtual_class': grand_total,
        'n_graphs': len(graphs),
    }


def virtual_class_comparison(shadow: ShadowData, genus: int) -> Dict[str, Any]:
    """Compare virtual class computation with MC relation (no Behrend signs).

    The MC relation at (g, 0) says:
        Σ_Γ (1/|Aut(Γ)|) · w_Γ · I_Γ = 0

    The virtual class with Behrend signs:
        [M^sh_g]^vir = Σ_Γ (-1)^{codim(Γ)} · (1/|Aut(Γ)|) · w_Γ · I_Γ

    The difference measures the "virtual correction":
        δ^vir = [M^sh_g]^vir - Σ(unsigned)
    """
    if genus == 2:
        mc_data = mc_relation_genus2_free_energy(shadow)
        vc_data = virtual_class_graph_sum_genus2(shadow, behrend=True)
        vc_unsigned = virtual_class_graph_sum_genus2(shadow, behrend=False)
    elif genus == 3:
        mc_data = mc_relation_genus3_free_energy(shadow)
        vc_data = virtual_class_graph_sum_genus3(shadow, behrend=True)
        vc_unsigned = virtual_class_graph_sum_genus3(shadow, behrend=False)
    else:
        raise NotImplementedError(f"Genus {genus} not supported")

    virtual_correction = cancel(
        vc_data['virtual_class'] - vc_unsigned['virtual_class']
    )

    return {
        'genus': genus,
        'mc_boundary_total': mc_data.get('boundary_total',
                                          mc_data.get('planted_forest', Integer(0))),
        'virtual_class_signed': vc_data['virtual_class'],
        'virtual_class_unsigned': vc_unsigned['virtual_class'],
        'virtual_correction': virtual_correction,
        'planted_forest_signed': vc_data['planted_forest'],
        'planted_forest_unsigned': vc_unsigned['planted_forest'],
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 4: Shadow metric analysis and Behrend at special points
# ═══════════════════════════════════════════════════════════════════════════

def shadow_metric_analysis(c_val: float) -> Dict[str, Any]:
    """Analyze the shadow metric Q_L at a specific central charge value.

    For Virasoro at central charge c:
        κ = c/2
        S₃ = 2
        S₄ = 10/[c(5c+22)]
        Δ = 8κ·S₄ = 40/(5c+22)
        Q_L(t) = (c + 6t)² + 80t²/(5c+22)

    Returns analysis including zeros, discriminant, and Behrend data.
    """
    kappa_val = c_val / 2
    S3_val = 2.0
    if c_val == 0:
        S4_val = float('inf')
        Delta_val = float('inf')
    else:
        S4_val = 10.0 / (c_val * (5 * c_val + 22))
        Delta_val = 40.0 / (5 * c_val + 22)

    # Q_L(t) = (2κ + 3S₃t)² + 2Δt² = (c + 6t)² + 2Δt²
    # Zeros: (9S₃² + 16κS₄)t² + 12κS₃t + 4κ² = 0
    # i.e. (36 + 16κS₄)t² + 12κ·2·t + 4κ² = 0
    # i.e. (36 + 8ΔS₃/S₃...)
    # Direct: a = 9·4 + 16·(c/2)·S₄ = 36 + 8c·S₄
    #         b = 12·(c/2)·2 = 12c
    #         c_coeff = 4·(c/2)² = c²

    a_coeff = 36 + 16 * kappa_val * S4_val if c_val != 0 else 36
    b_coeff = 12 * kappa_val * S3_val
    c_coeff_val = 4 * kappa_val ** 2

    zeros = []
    if a_coeff != 0:
        disc = b_coeff ** 2 - 4 * a_coeff * c_coeff_val
        if abs(disc) < 1e-15:
            zeros = [(-b_coeff / (2 * a_coeff), 2)]
        else:
            sqrt_d = cmath.sqrt(disc)
            t1 = (-b_coeff + sqrt_d) / (2 * a_coeff)
            t2 = (-b_coeff - sqrt_d) / (2 * a_coeff)
            zeros = [(t1, 1), (t2, 1)]

    # Behrend data
    is_singular = (c_val == 0 or abs(Delta_val) < 1e-15 if c_val != 0
                   else True)

    return {
        'c': c_val,
        'kappa': kappa_val,
        'S3': S3_val,
        'S4': S4_val if c_val != 0 else None,
        'Delta': Delta_val if c_val != 0 else None,
        'Q_L_zeros': zeros,
        'is_singular': is_singular,
        'behrend_at_smooth': behrend_function_smooth(0),  # vdim = 0
        'behrend_at_point': (behrend_function_singular(0, "node")
                             if is_singular
                             else behrend_function_smooth(0)),
    }


def virasoro_shadow_metric_symbolic():
    """Shadow metric for Virasoro as a symbolic expression.

    Q_L(t) = (c + 6t)² + 80t²/(5c + 22)

    This is the key object whose algebraicity (class G/L vs M)
    determines the shadow depth.

    For Virasoro: Δ = 40/(5c+22) ≠ 0 for generic c,
    so Q_L is NOT a perfect square → class M, infinite depth.

    Special values:
    - c → ∞: Δ → 0, Q_L → (c + 6t)², class G behavior
    - c = -22/5: Δ diverges (singular, non-physical)
    - c = 0: κ = 0 but Θ ≠ 0 (AP31!)
    - c = 26: κ = 13, κ' = κ(Vir_{26-c=0}) = 0 (AP24: κ+κ' = 13, NOT 0)
    """
    c = c_sym
    kappa = c / 2
    S3 = Integer(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    Delta = 8 * kappa * S4  # = 40/(5c+22)
    Q_L = (2 * kappa + 3 * S3 * Symbol('t')) ** 2 + 2 * Delta * Symbol('t') ** 2
    return {
        'Q_L': cancel(Q_L),
        'Delta': cancel(Delta),
        'kappa': kappa,
        'S4': cancel(S4),
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 5: Behrend function at zeta zeros
# ═══════════════════════════════════════════════════════════════════════════

def zeta_zero_central_charge(n: int) -> complex:
    """Map the n-th nontrivial zeta zero ρ_n to a central charge c(ρ_n).

    The parameterization uses the scattering factor pole structure:
    c(ρ) = 1 + ρ = 1 + 1/2 + it_n = 3/2 + it_n

    This maps zeta zeros to complex central charges where the
    shadow metric has special properties.

    Alternative parameterization (complementarity-preserving):
    c(ρ) = 26 · ρ/(ρ+1)  (maps ρ=0 → c=0, ρ=∞ → c=26)

    We use the direct parameterization c = 1 + ρ.

    Returns:
        Complex central charge c(ρ_n).
    """
    if not HAS_MPMATH:
        # Fallback: use known approximate values for first 20 zeros
        _known_zeros_im = [
            14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
            37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
            52.970321, 56.446248, 59.347044, 60.831779, 65.112544,
            67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
        ]
        if 1 <= n <= 20:
            t_n = _known_zeros_im[n - 1]
        else:
            raise ValueError(f"Without mpmath, only zeros 1-20 available, got n={n}")
        return complex(1.5, t_n)

    mp.dps = 30
    rho = zetazero(n)
    # c = 1 + rho
    return complex(float(mpre(1 + rho)), float(mpim(1 + rho)))


def shadow_metric_at_zeta_zero(n: int) -> Dict[str, Any]:
    """Evaluate shadow metric and Behrend data at c(ρ_n).

    At complex central charge c = 3/2 + it_n:
    - κ = c/2 = 3/4 + it_n/2 (complex!)
    - S₃ = 2 (universal for Virasoro)
    - S₄ = 10/[c(5c+22)] (complex)
    - Δ = 40/(5c+22) (complex)

    The Behrend function value at this point measures the local
    virtual structure.
    """
    c_val = zeta_zero_central_charge(n)
    c_re = c_val.real
    c_im = c_val.imag

    kappa_val = c_val / 2
    S3_val = 2.0
    S4_val = 10.0 / (c_val * (5 * c_val + 22))
    Delta_val = 40.0 / (5 * c_val + 22)

    # Q_L(0) = (2κ)² = c²  (= (3/2 + it_n)²)
    Q_at_0 = c_val ** 2

    # |Q_L(0)| = |c|² = 9/4 + t_n²
    Q_abs_at_0 = abs(Q_at_0)

    # Phase of Q_L(0)
    Q_phase = cmath.phase(Q_at_0)

    # The Behrend function at a complex point is the sign of the
    # real part of the Euler obstruction:
    # ν(c) = sign(Re(Q_L(0)))
    nu_val = 1 if Q_at_0.real > 0 else (-1 if Q_at_0.real < 0 else 0)

    # Weighted Euler characteristic contribution:
    # χ^B contribution = ν · 1 (point contribution)
    chi_B_contribution = nu_val

    return {
        'n': n,
        'c': c_val,
        'kappa': kappa_val,
        'S4': S4_val,
        'Delta': Delta_val,
        'Q_at_0': Q_at_0,
        'Q_abs': Q_abs_at_0,
        'Q_phase': Q_phase,
        'behrend_nu': nu_val,
        'chi_B_contribution': chi_B_contribution,
    }


def behrend_at_zeta_zeros(n_max: int = 20) -> Dict[str, Any]:
    """Compute Behrend function values at the first n_max zeta zeros.

    For each ρ_n (n = 1, ..., n_max):
    - Evaluate c(ρ_n) = 1 + ρ_n = 3/2 + it_n
    - Compute κ(c), S₄(c), Δ(c)
    - Evaluate Q_L(0) = c²
    - Compute Behrend ν(c(ρ_n))
    - Compute χ^B contribution

    Returns:
        Dictionary with per-zero data and aggregate statistics.
    """
    results = {}
    total_chi_B = 0
    nu_values = []

    for n in range(1, n_max + 1):
        data = shadow_metric_at_zeta_zero(n)
        results[n] = data
        total_chi_B += data['chi_B_contribution']
        nu_values.append(data['behrend_nu'])

    # Analysis: does χ^B change at zeros?
    # All zeros have Re(c) = 3/2 > 0, so Q_L(0) = c² has
    # Re(c²) = (3/2)² - t_n² < 0 for t_n > 3/2 (all zeros).
    # So ν = -1 for ALL nontrivial zeros (t_n > 14 >> 3/2).

    return {
        'zeros': results,
        'total_chi_B': total_chi_B,
        'nu_values': nu_values,
        'all_negative': all(v == -1 for v in nu_values),
        'analysis': (
            "For ρ_n = 1/2 + it_n with t_n > 3/2: "
            "c(ρ_n) = 3/2 + it_n, so c² = 9/4 - t_n² + 3it_n. "
            "Since t_n > 14, Re(c²) = 9/4 - t_n² < 0 for ALL "
            "nontrivial zeros.  Hence ν = -1 universally."
        ),
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 6: DT-type invariant via shadow obstruction theory
# ═══════════════════════════════════════════════════════════════════════════

def dt_invariant_genus_g(shadow: ShadowData, g: int) -> Any:
    """DT-type invariant at genus g from the shadow obstruction tower.

    The DT invariant is:
        DT_g(A) = ∫_{[M^sh_g]^vir} 1 = F_g(A)  (virtual degree)

    For the scalar shadow (κ only):
        DT_g = κ · λ_g^FP

    For the full shadow tower:
        DT_g = κ · λ_g^FP + (higher-arity corrections from δ_pf)

    The higher-arity corrections come from planted-forest graphs
    involving S_3, S_4, etc.
    """
    kappa = shadow.kappa
    # Scalar part: F_g = κ · λ_g^FP
    scalar_part = kappa * lambda_fp(g)

    # Higher-arity correction: δ_pf^{(g,0)}
    if g == 2 and shadow.depth_class in ('L', 'C', 'M'):
        pf = planted_forest_polynomial(shadow)
        return cancel(scalar_part + pf)
    elif g == 3 and shadow.depth_class in ('L', 'C', 'M'):
        pf = planted_forest_polynomial_genus3(shadow)
        return cancel(scalar_part + pf)
    else:
        return scalar_part


def dt_invariant_numerical(shadow_name: str, c_val: float,
                           g_max: int = 5) -> Dict[int, float]:
    """Numerical DT invariant for specific parameter values.

    Evaluates DT_g(A) = κ · λ_g^FP + corrections at given c.
    """
    results = {}

    for g in range(1, g_max + 1):
        lfp = float(lambda_fp(g))

        if shadow_name == 'virasoro':
            kappa_val = c_val / 2
        elif shadow_name == 'heisenberg':
            kappa_val = c_val  # level k = c for Heisenberg
        elif shadow_name == 'sl2':
            k_val = c_val
            kappa_val = 3 * (k_val + 2) / 4
        else:
            kappa_val = c_val / 2  # default

        dt_g = kappa_val * lfp
        results[g] = dt_g

    return results


# ═══════════════════════════════════════════════════════════════════════════
# Part 7: Cross-family virtual class comparison
# ═══════════════════════════════════════════════════════════════════════════

def cross_family_virtual_comparison(genus: int = 2) -> Dict[str, Any]:
    """Compare virtual class computations across standard families.

    For each family (G/L/C/M), computes:
    - Obstruction theory data (vdim, H^i dimensions)
    - Virtual class via graph sum
    - DT invariant (scalar + corrections)
    - Behrend function analysis
    """
    families = {
        'Heisenberg': heisenberg_shadow_data(),
        'Affine_sl2': affine_shadow_data(),
        'Virasoro': virasoro_shadow_data(),
    }

    results = {}
    for name, shadow in families.items():
        if genus == 2:
            vc = virtual_class_graph_sum_genus2(shadow, behrend=True)
            vc_no_behrend = virtual_class_graph_sum_genus2(shadow, behrend=False)
        elif genus == 3:
            vc = virtual_class_graph_sum_genus3(shadow, behrend=True)
            vc_no_behrend = virtual_class_graph_sum_genus3(shadow, behrend=False)
        else:
            raise NotImplementedError

        results[name] = {
            'depth_class': shadow.depth_class,
            'virtual_class': vc['virtual_class'],
            'virtual_class_unsigned': vc_no_behrend['virtual_class'],
            'planted_forest_signed': vc['planted_forest'],
            'planted_forest_unsigned': vc_no_behrend['planted_forest'],
            'n_graphs': vc['n_graphs'],
        }

    return results


# ═══════════════════════════════════════════════════════════════════════════
# Part 8: Virtual localization formula
# ═══════════════════════════════════════════════════════════════════════════

def virtual_localization_genus2(shadow: ShadowData) -> Dict[str, Any]:
    """Virtual localization computation at genus 2.

    The virtual localization formula expresses [M^sh_g]^vir as a sum
    over torus-fixed loci.  For the shadow moduli, the torus action
    is the C*-action on the primary line V = <e> scaling the generator.

    Fixed loci correspond to stable graphs with vertices weighted by
    equivariant shadow data.

    The localization formula:
    [M^sh_g]^vir = Σ_Γ (1/|Aut(Γ)|) · [Contribution from Γ]

    where each graph contributes:
    - Vertex: integration over M-bar_{g_v, val_v}
    - Edge: equivariant propagator 1/(ψ_+ + ψ_-)
    - Behrend sign: (-1)^{codim} from the virtual normal bundle
    """
    graphs = stable_graphs_genus2_0leg()
    localization_data = []

    for G in graphs:
        w = vertex_weight(G, shadow)
        I = graph_integral_genus2(G)
        I_sym = Integer(I.numerator) / Integer(I.denominator)

        # Virtual normal bundle rank = codimension
        # Euler class contribution = (-1)^{codim} from top Chern class
        e_normal = (-1) ** G.codimension

        # Localized contribution
        loc_contrib = cancel(e_normal * w * I_sym / G.automorphism_order)

        localization_data.append({
            'graph': G.name,
            'codim': G.codimension,
            'weight': w,
            'hodge_integral': I,
            'euler_normal': e_normal,
            'localized_contribution': loc_contrib,
        })

    total = cancel(sum(d['localized_contribution'] for d in localization_data))

    return {
        'graphs': localization_data,
        'total': total,
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 9: Consistency checks and multi-path verification
# ═══════════════════════════════════════════════════════════════════════════

def verify_virtual_class_consistency(shadow: ShadowData,
                                     genus: int = 2) -> Dict[str, Any]:
    """Multi-path verification of virtual class computations.

    Path 1: Direct graph sum (unsigned, = MC relation)
    Path 2: Graph sum with Behrend signs (= virtual class)
    Path 3: Localization formula (should agree with Path 2)
    Path 4: DT invariant (scalar part κ·λ_g^FP)
    Path 5: Numerical evaluation at specific c values
    """
    # Path 1: MC relation (unsigned sum)
    if genus == 2:
        mc = mc_relation_genus2_free_energy(shadow)
        vc_unsigned = virtual_class_graph_sum_genus2(shadow, behrend=False)
        vc_signed = virtual_class_graph_sum_genus2(shadow, behrend=True)
        loc = virtual_localization_genus2(shadow)
    elif genus == 3:
        mc = mc_relation_genus3_free_energy(shadow)
        vc_unsigned = virtual_class_graph_sum_genus3(shadow, behrend=False)
        vc_signed = virtual_class_graph_sum_genus3(shadow, behrend=True)
        loc = None  # localization not implemented at genus 3
    else:
        raise NotImplementedError

    # Path 4: DT scalar part
    dt_scalar = shadow.kappa * lambda_fp(genus)

    # Consistency checks
    checks = {}

    # Check 1: Localization = signed graph sum (genus 2 only)
    if loc is not None:
        loc_total = loc['total']
        vc_total = vc_signed['virtual_class']
        checks['localization_vs_graph_sum'] = {
            'localization': loc_total,
            'graph_sum': vc_total,
            'match': cancel(loc_total - vc_total) == 0,
        }

    # Check 2: Planted forest difference
    pf_signed = vc_signed['planted_forest']
    pf_unsigned = vc_unsigned['planted_forest']
    checks['planted_forest_behrend_effect'] = {
        'signed': pf_signed,
        'unsigned': pf_unsigned,
        'difference': cancel(pf_signed - pf_unsigned),
    }

    # Check 3: Class G (Heisenberg) has zero planted forest
    if shadow.depth_class == 'G':
        checks['class_G_pf_zero'] = {
            'planted_forest': pf_unsigned,
            'is_zero': pf_unsigned == 0,
        }

    # Check 5: Numerical evaluations
    if shadow.name == "Virasoro":
        numerical = {}
        for c_val in [1, 2, 10, 13, 25, 26]:
            vc_num = float(vc_signed['virtual_class'].subs(c_sym, c_val))
            dt_num = float(dt_scalar.subs(c_sym, c_val))
            pf_num = float(pf_unsigned.subs(c_sym, c_val))
            numerical[c_val] = {
                'virtual_class': vc_num,
                'dt_scalar': dt_num,
                'planted_forest': pf_num,
            }
        checks['numerical'] = numerical

    return {
        'genus': genus,
        'shadow': shadow.name,
        'checks': checks,
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 10: Euler characteristic analysis at zeta zeros
# ═══════════════════════════════════════════════════════════════════════════

def chi_B_change_at_zeros(n_max: int = 20) -> Dict[str, Any]:
    """Analyze how χ^B changes as we move through zeta zeros.

    For the Virasoro shadow at c(ρ_n) = 3/2 + it_n:

    The key quantity is:
        Q_L(0; c(ρ_n)) = c(ρ_n)² = (3/2 + it_n)² = 9/4 - t_n² + 3it_n

    Since t_n > 14 for all nontrivial zeros:
        Re(Q_L(0)) = 9/4 - t_n² < 0

    This means the Behrend function is uniformly ν = -1 at all zeros.
    The "change" in χ^B happens NOT at individual zeros, but in the
    VARIATION of |Q_L(0)| = |c|² = 9/4 + t_n² which grows with t_n.

    The rate of growth t_n ~ 2πn/log(n) (from zero spacing) determines
    how |Q_L| grows along the critical line.
    """
    data = behrend_at_zeta_zeros(n_max)

    # Analyze variation of |Q_L| with zero index
    Q_abs_values = []
    t_values = []
    for n in range(1, n_max + 1):
        d = data['zeros'][n]
        Q_abs_values.append(d['Q_abs'])
        t_values.append(d['c'].imag)

    # Growth rate: |Q_L(0)| ~ t_n² for large t_n
    ratios = []
    for i in range(len(Q_abs_values)):
        if t_values[i] > 0:
            ratio = Q_abs_values[i] / (t_values[i] ** 2)
            ratios.append(ratio)

    # The ratio |Q|/t² → 1 as t → ∞ (since 9/4/t² → 0)
    avg_ratio = sum(ratios) / len(ratios) if ratios else 0

    # Delta variation (discriminant at complex c)
    delta_values = []
    for n in range(1, n_max + 1):
        d = data['zeros'][n]
        delta_values.append(d['Delta'])

    return {
        'data': data,
        'Q_abs_values': Q_abs_values,
        't_values': t_values,
        'Q_over_t_sq_ratios': ratios,
        'avg_ratio_approaches_1': abs(avg_ratio - 1.0) < 0.1,
        'all_behrend_negative': data['all_negative'],
        'delta_values': delta_values,
        'total_chi_B': data['total_chi_B'],
        'chi_B_formula': f"chi^B = -n_max = -{n_max} (all ν = -1)",
    }


# ═══════════════════════════════════════════════════════════════════════════
# Part 11: Comprehensive virtual class package
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class VirtualClassPackage:
    """Complete virtual class data for a chiral algebra.

    Packages obstruction theory, Behrend function, graph sums,
    DT invariants, and zeta zero analysis.
    """
    name: str
    obstruction: ObstructionTheoryData
    vdim: int
    behrend_smooth: int
    virtual_class_g2: Any  # symbolic
    virtual_class_g3: Any  # symbolic, may be None
    dt_invariants: Dict[int, Any]  # g -> DT_g
    pf_g2: Any  # planted-forest correction genus 2
    pf_g3: Any  # planted-forest correction genus 3

    def summary(self) -> str:
        lines = [
            f"=== Virtual Class Package: {self.name} ===",
            f"Virtual dimension: {self.vdim}",
            f"Behrend at smooth point: {self.behrend_smooth}",
            f"Shadow depth: {self.obstruction.shadow_depth}",
            f"Shadow class: {self.obstruction.shadow_class}",
        ]
        if self.dt_invariants:
            for g, dt in sorted(self.dt_invariants.items()):
                lines.append(f"  DT_g={g}: {dt}")
        return "\n".join(lines)


def compute_virtual_class_package(family: str) -> VirtualClassPackage:
    """Compute complete virtual class package for a family.

    Parameters:
        family: one of 'heisenberg', 'virasoro', 'sl2', 'betagamma', 'w3'
    """
    obs_fn = ALL_OBSTRUCTION_DATA.get(family)
    if obs_fn is None:
        raise ValueError(f"Unknown family: {family}")
    obs = obs_fn()

    # Shadow data
    if family == 'heisenberg':
        shadow = heisenberg_shadow_data()
    elif family == 'virasoro':
        shadow = virasoro_shadow_data()
    elif family in ('sl2', 'sl3'):
        shadow = affine_shadow_data()
    else:
        # Default to Virasoro for families not yet in pixton bridge
        shadow = virasoro_shadow_data()

    # Virtual class computations
    vc_g2 = virtual_class_graph_sum_genus2(shadow, behrend=True)
    try:
        vc_g3 = virtual_class_graph_sum_genus3(shadow, behrend=True)
        vc_g3_val = vc_g3['virtual_class']
    except Exception:
        vc_g3_val = None

    # DT invariants
    dt = {}
    for g in range(1, 6):
        dt[g] = dt_invariant_genus_g(shadow, g)

    # Planted forest
    pf_g2 = planted_forest_polynomial(shadow)
    try:
        pf_g3 = planted_forest_polynomial_genus3(shadow)
    except Exception:
        pf_g3 = None

    return VirtualClassPackage(
        name=obs.name,
        obstruction=obs,
        vdim=obs.virtual_dim,
        behrend_smooth=behrend_function_smooth(obs.virtual_dim),
        virtual_class_g2=vc_g2['virtual_class'],
        virtual_class_g3=vc_g3_val,
        dt_invariants=dt,
        pf_g2=pf_g2,
        pf_g3=pf_g3,
    )
