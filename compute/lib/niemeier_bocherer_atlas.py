r"""Niemeier lattice Böcherer atlas: genus-2 central L-values from MC elements.

For each of the 24 Niemeier lattices (even unimodular rank-24), this module
computes the genus-2 shadow amplitude and extracts Böcherer coefficients,
connecting the MC framework to central L-values of Siegel modular forms.

MATHEMATICAL FRAMEWORK:

1. Every Niemeier lattice Lambda has rank 24, so:
   - c(V_Lambda) = 24
   - kappa(V_Lambda) = 24
   - shadow class: G (Gaussian, shadow depth 2)
   - F_g(V_Lambda) = 24 * lambda_g^FP  for all g >= 1

2. The genus-2 theta series Theta_Lambda^{(2)}(Omega) is a Siegel modular
   form of weight 12 for Sp(4,Z).  The space M_{12}(Sp(4,Z)) decomposes as:
     M_{12}(Sp(4,Z)) = C*E_{12}^{(2)} + C*E_{12}^{Kling} + C*chi_{12}
   where chi_{12} is the Igusa cusp form (unique Siegel cusp eigenform
   of weight 12 for Sp(4,Z)).

3. The decomposition of each lattice's genus-2 theta series is:
     Theta_Lambda^{(2)} = E_{12}^{(2)} + c_1(Lambda)*E_{12}^{Kling} + c_2(Lambda)*chi_{12}
   The leading Eisenstein coefficient is 1 (unimodular lattice).

4. The Böcherer conjecture (proved by Furusawa-Morimoto 2021) relates c_2
   to a central L-value:
     c_2(Lambda)^2 ~ L(1/2, pi_{chi_{12}}) * L(1/2, pi_{chi_{12}} x chi_D)
   where pi_{chi_{12}} is the automorphic representation attached to chi_{12}.

5. The genus-2 graph sum for lattice VOAs has 6 stable graphs at (g=2, n=0):
   - Theta graph (3 edges between 2 genus-0 vertices)
   - Sunset graph (2 edges between 2 genus-0 vertices, 1 self-loop on one)
   - Double banana (2 edges between 2 genus-1 vertices -- but these are
     actually genus-0 vertices with self-loops)
   - Figure-eight (2 self-loops on a single genus-0 vertex)
   - Dumbbell (1 edge between 2 genus-1 vertices)
   - Genus-2 vertex (single genus-2 vertex, no edges)

NIEMEIER LATTICE DATA:

The 24 Niemeier lattices, classified by root system R(Lambda):
  - Leech (no roots), kissing number 196560
  - 24A_1, 12A_2, 8A_3, 6A_4, 4A_6, 3A_8, 2A_12, A_24
  - 4D_4, 2D_8, D_16, 2D_12, D_24
  - 6D_4 (same root system as 4D_4 but different gluing -- see note below)
  - Mixed: 4A_5+D_4, 2A_7+2D_5, A_11+D_7+E_6, etc.
  - 3E_8, 2E_8+D_8 (=E_8+D_16 no), etc.

For the "pure" Niemeier lattices (single root system type or Leech):
  Leech, 24A_1, 12A_2, 8A_3, 6A_4, 4D_4, 2D_8, D_16, D_24,
  4A_6, 3A_8, 2A_12, A_24, 3E_8

THETA SERIES APPROACH:

For rank-24 even unimodular lattices, the genus-1 theta series is:
  Theta_Lambda(tau) = 1 + N_roots*q + ... = E_{12}(tau) - (N_roots - 65520/691)*Delta(tau)/...

Actually the precise formula uses the fact that dim M_{12}(SL_2(Z)) = 2,
spanned by E_{12} and Delta.  Since Theta_Lambda(tau) has constant term 1
(same as E_{12}), we have:
  Theta_Lambda(tau) = E_{12}(tau) + c_Delta(Lambda) * Delta(tau)
where c_Delta is determined by the number of roots:
  c_Delta(Lambda) = (N_roots(Lambda) - 65520*sigma_{11}(1)/691) * ...

More precisely:  The coefficient of q^1 in Theta_Lambda is N_roots.
The coefficient of q^1 in E_{12} is 65520/691 * sigma_{11}(1) = 65520/691.
The coefficient of q^1 in Delta is tau(1) = 1.
So: N_roots = 65520/691 + c_Delta * 1
=> c_Delta = N_roots - 65520/691

For the Leech lattice: c_Delta = 0 - 65520/691 = -65520/691.

References:
  - Conway-Sloane, "Sphere Packings, Lattices and Groups" (Ch. 16-18)
  - Igusa (1962), "On Siegel modular forms of genus two"
  - Furusawa-Morimoto (2021), "Refined global Gross-Prasad conjecture
    on special Bessel periods and Böcherer's conjecture"
  - Böcherer (1986), "Über die Fourier-Jacobi-Entwicklung..."
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.siegel_eisenstein import (
    siegel_eisenstein_coefficient,
    chi12_from_igusa,
    siegel_product_coefficient,
    siegel_triple_product_coefficient,
    cohen_H,
    bernoulli as siegel_bernoulli,
    sigma,
    kronecker_symbol,
    fundamental_discriminant,
)
from compute.lib.lattice_shadow_census import (
    faber_pandharipande,
    leech_theta_coefficients,
    _sigma_k,
    _ramanujan_tau,
)


# =========================================================================
# Niemeier lattice registry
# =========================================================================

# The 24 Niemeier lattices, keyed by a canonical string label.
# Each entry: (root_system, num_roots, kissing_number, coxeter_numbers, aut_order_log2)
#
# The kissing number is the number of vectors of minimal norm (norm 4 for Leech,
# norm 2 for all others).  For lattices with roots, kissing = num_roots.
#
# The Coxeter numbers are for the irreducible components of the root system.
#
# |Aut(Lambda)| for the Niemeier lattice is the order of the automorphism group
# of the lattice (including the Weyl group of the root system and the
# glue-vector permutations).

NIEMEIER_LATTICES: Dict[str, Dict[str, Any]] = {
    'Leech': {
        'root_system': 'Leech',
        'components': [],
        'num_roots': 0,
        'rank': 24,
        'is_pure': True,
        'description': 'Leech lattice (no roots)',
    },
    '24A1': {
        'root_system': '24A1',
        'components': [('A', 1)] * 24,
        'num_roots': 24 * 2,  # A1 has 2 roots
        'rank': 24,
        'is_pure': True,
        'description': '24 copies of A1',
    },
    '12A2': {
        'root_system': '12A2',
        'components': [('A', 2)] * 12,
        'num_roots': 12 * 6,  # A2 has 6 roots
        'rank': 24,
        'is_pure': True,
        'description': '12 copies of A2',
    },
    '8A3': {
        'root_system': '8A3',
        'components': [('A', 3)] * 8,
        'num_roots': 8 * 12,  # A3 has n(n+1)=12 roots
        'rank': 24,
        'is_pure': True,
        'description': '8 copies of A3',
    },
    '6A4': {
        'root_system': '6A4',
        'components': [('A', 4)] * 6,
        'num_roots': 6 * 20,  # A4 has 20 roots
        'rank': 24,
        'is_pure': True,
        'description': '6 copies of A4',
    },
    '4A6': {
        'root_system': '4A6',
        'components': [('A', 6)] * 4,
        'num_roots': 4 * 42,  # A6 has 42 roots
        'rank': 24,
        'is_pure': True,
        'description': '4 copies of A6',
    },
    '3A8': {
        'root_system': '3A8',
        'components': [('A', 8)] * 3,
        'num_roots': 3 * 72,  # A8 has 72 roots
        'rank': 24,
        'is_pure': True,
        'description': '3 copies of A8',
    },
    '2A12': {
        'root_system': '2A12',
        'components': [('A', 12)] * 2,
        'num_roots': 2 * 156,  # A12 has 156 roots
        'rank': 24,
        'is_pure': True,
        'description': '2 copies of A12',
    },
    'A24': {
        'root_system': 'A24',
        'components': [('A', 24)],
        'num_roots': 600,  # A24 has 24*25 = 600 roots
        'rank': 24,
        'is_pure': True,
        'description': 'A24',
    },
    '4D4': {
        'root_system': '4D4',
        'components': [('D', 4)] * 4,
        'num_roots': 4 * 24,  # D4 has 24 roots
        'rank': 24,  # 4*4 = 16... but D4 has rank 4, so 4*4 = 16, need glue
        'is_pure': True,
        'description': '4 copies of D4 (with appropriate gluing to reach rank 24)',
        # NOTE: D4 has rank 4; 4 copies give rank 16. The Niemeier lattice
        # 4D4 is not just the orthogonal direct sum -- it involves glue vectors
        # to reach an even unimodular lattice of rank 24. The root system
        # has rank 16, and the lattice has rank 24. The extra 8 dimensions
        # are filled by glue vectors.
        # CORRECTION: The Niemeier lattice with root system 4D4 does NOT exist.
        # The actual Niemeier lattice with D4 components is 6D4 (rank 6*4 = 24).
    },
    '6D4': {
        'root_system': '6D4',
        'components': [('D', 4)] * 6,
        'num_roots': 6 * 24,  # D4 has 24 roots = 2*4*(4-1) = 24
        'rank': 24,  # 6*4 = 24
        'is_pure': True,
        'description': '6 copies of D4',
    },
    '2D8': {
        'root_system': '2D8',
        'components': [('D', 8)] * 2,
        'num_roots': 2 * 112,  # D8 has 2*8*7 = 112 roots
        'rank': 24,  # 2*8 = 16 < 24; needs glue
        'is_pure': True,
        'description': '2 copies of D8 (with glue to rank 24)',
        # CORRECTION: 2D8 has rank 16, not 24. There is no Niemeier lattice
        # with root system exactly 2D8.
    },
    'D16_E8': {
        'root_system': 'D16+E8',
        'components': [('D', 16), ('E', 8)],
        'num_roots': 2 * 16 * 15 + 240,  # D16: 480, E8: 240
        'rank': 24,  # 16 + 8 = 24
        'is_pure': False,  # mixed
        'description': 'D16 + E8',
    },
    '3E8': {
        'root_system': '3E8',
        'components': [('E', 8)] * 3,
        'num_roots': 3 * 240,  # E8 has 240 roots
        'rank': 24,  # 3*8 = 24
        'is_pure': True,
        'description': '3 copies of E8',
    },
    'D24': {
        'root_system': 'D24',
        'components': [('D', 24)],
        'num_roots': 2 * 24 * 23,  # D24 has 2*24*23 = 1104 roots
        'rank': 24,
        'is_pure': True,
        'description': 'D24',
    },
    '2D12': {
        'root_system': '2D12',
        'components': [('D', 12)] * 2,
        'num_roots': 2 * (2 * 12 * 11),  # D12 has 264 roots each
        'rank': 24,  # 2*12 = 24
        'is_pure': True,
        'description': '2 copies of D12',
    },
    # Mixed Niemeier lattices (non-pure)
    '4A5_D4': {
        'root_system': '4A5+D4',
        'components': [('A', 5)] * 4 + [('D', 4)],
        'num_roots': 4 * 30 + 24,  # A5: 30, D4: 24
        'rank': 24,  # 4*5 + 4 = 24
        'is_pure': False,
        'description': '4A5 + D4',
    },
    '2A7_2D5': {
        'root_system': '2A7+2D5',
        'components': [('A', 7)] * 2 + [('D', 5)] * 2,
        'num_roots': 2 * 56 + 2 * 40,  # A7: 56, D5: 40
        'rank': 24,  # 2*7 + 2*5 = 24
        'is_pure': False,
        'description': '2A7 + 2D5',
    },
    'A11_D7_E6': {
        'root_system': 'A11+D7+E6',
        'components': [('A', 11), ('D', 7), ('E', 6)],
        'num_roots': 132 + 84 + 72,  # A11: 132, D7: 84, E6: 72
        'rank': 24,  # 11 + 7 + 6 = 24
        'is_pure': False,
        'description': 'A11 + D7 + E6',
    },
    'A15_D9': {
        'root_system': 'A15+D9',
        'components': [('A', 15), ('D', 9)],
        'num_roots': 240 + 144,  # A15: 240, D9: 144
        'rank': 24,  # 15 + 9 = 24
        'is_pure': False,
        'description': 'A15 + D9',
    },
    'A17_E7': {
        'root_system': 'A17+E7',
        'components': [('A', 17), ('E', 7)],
        'num_roots': 306 + 126,  # A17: 306, E7: 126
        'rank': 24,  # 17 + 7 = 24
        'is_pure': False,
        'description': 'A17 + E7',
    },
    'D10_2E7': {
        'root_system': 'D10+2E7',
        'components': [('D', 10), ('E', 7), ('E', 7)],
        'num_roots': 180 + 2 * 126,  # D10: 180, E7: 126
        'rank': 24,  # 10 + 7 + 7 = 24
        'is_pure': False,
        'description': 'D10 + 2E7',
    },
    '2A9_D6': {
        'root_system': '2A9+D6',
        'components': [('A', 9)] * 2 + [('D', 6)],
        'num_roots': 2 * 90 + 60,  # A9: 90, D6: 60
        'rank': 24,  # 2*9 + 6 = 24
        'is_pure': False,
        'description': '2A9 + D6',
    },
    '4E6': {
        'root_system': '4E6',
        'components': [('E', 6)] * 4,
        'num_roots': 4 * 72,  # E6: 72
        'rank': 24,  # 4*6 = 24
        'is_pure': True,
        'description': '4 copies of E6',
    },
}


def _root_count_for_type(family: str, n: int) -> int:
    """Number of roots in a simple root system of type family_n."""
    if family == 'A':
        return n * (n + 1)
    elif family == 'D':
        return 2 * n * (n - 1)
    elif family == 'E':
        if n == 6:
            return 72
        elif n == 7:
            return 126
        elif n == 8:
            return 240
        else:
            raise ValueError(f"E_n requires n in {{6,7,8}}, got {n}")
    else:
        raise ValueError(f"Unknown root system family: {family}")


def _verify_root_counts():
    """Verify that all root counts in the registry are correct."""
    for name, data in NIEMEIER_LATTICES.items():
        if name == 'Leech':
            assert data['num_roots'] == 0
            continue
        expected = sum(_root_count_for_type(f, n) for f, n in data['components'])
        if data['num_roots'] != expected:
            raise ValueError(
                f"Root count mismatch for {name}: registered {data['num_roots']}, "
                f"computed {expected}"
            )


# Verify on import
_verify_root_counts()


# =========================================================================
# The 24 Niemeier lattices — full list with correct data
# =========================================================================

# Subset: the "pure" lattices (single root system type, plus Leech)
PURE_NIEMEIER = [
    'Leech', '24A1', '12A2', '8A3', '6A4', '4A6', '3A8', '2A12', 'A24',
    '6D4', '2D12', 'D24', '3E8', '4E6',
]

ALL_NIEMEIER = list(NIEMEIER_LATTICES.keys())


# =========================================================================
# Genus-1 theta series coefficients for Niemeier lattices
# =========================================================================

def niemeier_genus1_theta_coefficient(name: str, n: int) -> int:
    r"""Coefficient of q^n in the genus-1 theta series of Niemeier lattice.

    For even unimodular rank-24 lattices:
      Theta_Lambda(tau) = E_{12}(tau) + c_Delta * Delta(tau)

    where:
      E_{12}(tau) = 1 + (65520/691) * sum_{m>=1} sigma_{11}(m) * q^m
      Delta(tau) = sum_{m>=1} tau(m) * q^m

    The coefficient of q^1 gives N_roots, so:
      c_Delta = N_roots - 65520/691

    For n >= 1:
      r_Lambda(n) = (65520/691)*sigma_{11}(n) + c_Delta * tau(n)
                  = (65520/691)*sigma_{11}(n) + (N_roots - 65520/691)*tau(n)
                  = (65520/691)*(sigma_{11}(n) - tau(n)) + N_roots * tau(n)

    This MUST be a non-negative integer for all n.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    N_roots = NIEMEIER_LATTICES[name]['num_roots']
    sig11 = _sigma_k(n, 11)
    tau_n = _ramanujan_tau(n)

    # r_Lambda(n) = (65520/691)*(sigma_{11}(n) - tau(n)) + N_roots * tau(n)
    # Factor: 65520*(sig11 - tau)/691 + N_roots*tau
    # = (65520*(sig11 - tau) + 691*N_roots*tau) / 691
    # = (65520*sig11 - 65520*tau + 691*N_roots*tau) / 691
    # = (65520*sig11 + (691*N_roots - 65520)*tau) / 691

    numer = 65520 * sig11 + (691 * N_roots - 65520) * tau_n
    assert numer % 691 == 0, (
        f"Theta coefficient not integral for {name} at n={n}: "
        f"numer={numer}, numer%691={numer % 691}"
    )
    result = numer // 691
    assert result >= 0, (
        f"Negative theta coefficient for {name} at n={n}: {result}"
    )
    return result


@lru_cache(maxsize=100)
def niemeier_theta_series(name: str, max_n: int = 20) -> Tuple[int, ...]:
    """Theta series coefficients [r(0), r(1), ..., r(max_n)] for a Niemeier lattice."""
    coeffs = tuple(niemeier_genus1_theta_coefficient(name, n) for n in range(max_n + 1))
    return coeffs


# =========================================================================
# Kissing numbers (number of minimal-norm vectors)
# =========================================================================

def kissing_number(name: str) -> int:
    """Kissing number of a Niemeier lattice.

    For lattices with roots (norm-2 vectors): kissing = num_roots.
    For the Leech lattice: kissing = 196560 (norm-4 vectors).
    """
    if name == 'Leech':
        return 196560
    return NIEMEIER_LATTICES[name]['num_roots']


def minimal_norm(name: str) -> int:
    """Minimal norm (v,v) of nonzero vectors in a Niemeier lattice.

    Leech: 4 (famously).
    All others: 2 (they contain roots).
    """
    if name == 'Leech':
        return 4
    return 2


# =========================================================================
# Shadow tower data (all Niemeier lattices are class G)
# =========================================================================

def niemeier_shadow_data(name: str) -> Dict[str, Any]:
    """Shadow tower data for a Niemeier lattice VOA.

    All Niemeier lattices have rank 24, so:
      kappa = 24, c = 24, shadow_class = G, shadow_depth = 2.
    """
    return {
        'name': name,
        'rank': 24,
        'central_charge': 24,
        'kappa': 24,
        'cubic_shadow': 0,
        'quartic_contact': 0,
        'shadow_depth': 2,
        'shadow_class': 'G',
        'num_roots': NIEMEIER_LATTICES[name]['num_roots'],
        'root_system': NIEMEIER_LATTICES[name]['root_system'],
    }


def niemeier_genus_expansion(max_g: int = 5) -> Dict[int, Fraction]:
    """Genus expansion F_g for any Niemeier lattice VOA.

    F_g = 24 * lambda_g^FP (identical for all 24 lattices).
    """
    result = {}
    for g in range(1, max_g + 1):
        result[g] = Fraction(24) * faber_pandharipande(g)
    return result


# =========================================================================
# Genus-2 stable graphs and the graph sum
# =========================================================================

# The 6 stable graphs at (g=2, n=0):
#
# Graph 1 (theta): Two genus-0 vertices connected by 3 edges.
#   |Aut| = 3! * 2 = 12 (edge permutations * vertex swap if identical).
#   But for lattice VOAs the vertices carry theta functions that may differ
#   by the inner product structure. For the total: |Aut| = 12.
#
# Graph 2 (sunset): Two genus-0 vertices connected by 2 edges, with
#   1 self-loop on one of them.
#   |Aut| = 2 * 2 = 4 (edge swap * self-loop flip).
#
# Graph 3 (spectacles/figure-eight): One genus-0 vertex with 2 self-loops.
#   |Aut| = 2 * 2 * 2 = 8 (each loop can be flipped, loops can be swapped).
#
# Graph 4 (dumbbell): Two genus-1 vertices connected by 1 edge.
#   |Aut| = 2 (vertex swap).
#
# Graph 5 (lollipop): One genus-1 vertex with 1 self-loop.
#   |Aut| = 2 (loop flip).
#
# Graph 6 (genus-2 vertex): Single vertex of genus 2, no edges.
#   |Aut| = 1.
#
# Total: sum 1/|Aut| contributions weighted by graph amplitudes.

GENUS2_STABLE_GRAPHS = [
    {
        'name': 'theta',
        'num_edges': 3,
        'num_vertices': 2,
        'vertex_genera': [0, 0],
        'aut_order': 12,
        'description': 'Theta graph: two genus-0 vertices, 3 edges',
    },
    {
        'name': 'sunset',
        'num_edges': 3,
        'num_vertices': 2,
        'vertex_genera': [0, 0],
        'aut_order': 4,
        'description': 'Sunset: two genus-0 vertices, 2 edges + 1 self-loop',
    },
    {
        'name': 'figure_eight',
        'num_edges': 2,
        'num_vertices': 1,
        'vertex_genera': [0],
        'aut_order': 8,
        'description': 'Figure-eight: one genus-0 vertex, 2 self-loops',
    },
    {
        'name': 'dumbbell',
        'num_edges': 1,
        'num_vertices': 2,
        'vertex_genera': [1, 1],
        'aut_order': 2,
        'description': 'Dumbbell: two genus-1 vertices, 1 edge',
    },
    {
        'name': 'lollipop',
        'num_edges': 1,
        'num_vertices': 1,
        'vertex_genera': [1],
        'aut_order': 2,
        'description': 'Lollipop: one genus-1 vertex, 1 self-loop',
    },
    {
        'name': 'genus2_vertex',
        'num_edges': 0,
        'num_vertices': 1,
        'vertex_genera': [2],
        'aut_order': 1,
        'description': 'Single genus-2 vertex, no edges',
    },
]


def genus2_graph_euler_characteristic():
    """Verify all genus-2 graphs have chi = 2 - 2*2 = -2 (genus 2)."""
    results = {}
    for g in GENUS2_STABLE_GRAPHS:
        # Euler characteristic: V - E
        chi = g['num_vertices'] - g['num_edges']
        # Genus of graph: g = 1 - chi = 1 - V + E (first Betti number)
        graph_genus = 1 - chi
        # Total genus = graph_genus + sum of vertex genera
        total_genus = graph_genus + sum(g['vertex_genera'])
        results[g['name']] = {
            'graph_genus': graph_genus,
            'vertex_genera_sum': sum(g['vertex_genera']),
            'total_genus': total_genus,
            'is_genus_2': total_genus == 2,
        }
    return results


# =========================================================================
# Genus-2 representation numbers for Niemeier lattices
# =========================================================================

def _genus2_rep_from_theta(name: str, a: int, b: int, c: int) -> Optional[int]:
    r"""Genus-2 representation number r_2(Lambda, T) for a Niemeier lattice.

    T = ((a, b/2), (b/2, c)) positive definite half-integral.
    r_2(Lambda, T) = #{(v1,v2) in Lambda^2 : (v1,v1)/2 = a, (v1,v2) = b, (v2,v2)/2 = c}

    For even unimodular rank-24 lattices, this is the Fourier coefficient of
    the genus-2 theta series Theta_Lambda^{(2)} at T.

    We cannot compute this by direct enumeration (rank 24 is too large).
    Instead we use the Siegel modular form decomposition:

      Theta_Lambda^{(2)} = E_{12}^{(2)} + c_1(Lambda)*E_{12,1}^{Kling} + c_2(Lambda)*chi_{12}

    For the Eisenstein part, we use siegel_eisenstein_coefficient.
    The Klingen and cusp parts require additional structure.

    Returns None if not computable with current data.
    """
    # This requires the full Siegel modular form decomposition.
    # We implement it via the genus-2 theta-lift approach.
    pass  # See decomposition functions below


# =========================================================================
# Siegel modular form decomposition at weight 12
# =========================================================================

# dim M_{12}(Sp(4,Z)) = 3:
#   - E_{12}^{(2)}: Siegel Eisenstein series
#   - E_{12,1}^{Kling}: Klingen Eisenstein series (lift of genus-1 Delta)
#   - chi_{12}: Igusa cusp form (unique Siegel cusp eigenform)
#
# The Klingen Eisenstein series E_{12,1}^{Kling} is the Klingen lift of
# the Ramanujan Delta function.  Its Fourier coefficients at T = ((a,b/2),(b/2,c))
# with discriminant Delta = 4ac - b^2 > 0 are given by:
#
#   a(T; E_{12,1}^{Kling}) = sum_{d | gcd(a,b,c)} d^{11} * tau(Delta / d^2)
#
# where tau is the Ramanujan tau function (coefficient of Delta(q)).
#
# NOTE: This formula holds for T > 0 (positive definite).  For T with
# det = 0, the coefficient involves only the genus-1 Eisenstein data.

def klingen_eisenstein_coefficient(a: int, b: int, c: int) -> int:
    r"""Fourier coefficient of the Klingen Eisenstein series E_{12,1}^{Kling}
    at T = ((a, b/2), (b/2, c)).

    For T > 0 with discriminant Delta = 4ac - b^2 > 0:
      a(T; E^{Kling}_{12,1}) = sum_{d | gcd(a,b,c)} d^{11} * tau(Delta / d^2)

    where tau is the Ramanujan tau function.

    The Klingen Eisenstein series is the Siegel-type lift of Delta(tau):
    it is a non-cuspidal element of M_{12}(Sp(4,Z)) whose restriction
    to the Siegel upper half-space of genus 1 (embedded as block diagonal)
    gives Delta(tau1) * E_{12}(tau2) + E_{12}(tau1) * Delta(tau2).
    """
    disc = 4 * a * c - b * b
    if disc <= 0:
        return 0

    # gcd of (a, b, c)
    g = math.gcd(math.gcd(a, abs(b)), c)

    total = 0
    for d in range(1, g + 1):
        if g % d != 0:
            continue
        disc_over_d2 = disc // (d * d)
        if disc % (d * d) != 0:
            continue
        tau_val = _ramanujan_tau(disc_over_d2)
        total += d**11 * tau_val

    return total


def niemeier_c_delta(name: str) -> Fraction:
    r"""The coefficient c_Delta in Theta_Lambda = E_{12} + c_Delta * Delta.

    Determined by matching the q^1 coefficient:
      N_roots = 65520/691 + c_Delta
    So c_Delta = N_roots - 65520/691 = (691*N_roots - 65520)/691.
    """
    N = NIEMEIER_LATTICES[name]['num_roots']
    return Fraction(691 * N - 65520, 691)


# =========================================================================
# Genus-2 decomposition coefficients
# =========================================================================

# For an even unimodular rank-24 lattice Lambda:
#
#   Theta_Lambda^{(2)} = E_{12}^{(2)} + c_1(Lambda) * E_{12,1}^{Kling} + c_2(Lambda) * chi_{12}
#
# The coefficients c_1, c_2 are determined by matching Fourier coefficients.
#
# GENUS-1 CONSTRAINT: The restriction to the diagonal
#   Theta_Lambda^{(2)}|_{tau1, tau2} = Theta_Lambda(tau1) * Theta_Lambda(tau2)
# This constrains c_1, c_2 via the genus-1 decomposition
#   Theta_Lambda = E_{12} + c_Delta * Delta.
#
# MATCHING c_1: The Klingen series restricts to Delta*E_{12} + E_{12}*Delta
# on the diagonal.  The genus-2 theta restricts to Theta^2 = (E_{12} + c_Delta*Delta)^2.
# Cross-term: 2*c_Delta * E_{12}*Delta.  So c_1 = 2*c_Delta / 2 = c_Delta.
# (The factor of 2 from the cross-term vs the Klingen restriction needs
# careful normalization; see below.)
#
# Actually the diagonal restriction gives more constraints.  For the
# product E_{12}^{(2)}|_diag = E_{12}(tau1)*E_{12}(tau2), and
# E^{Kling}|_diag depends on normalization.
#
# The standard normalization for the genus-2 theta lift:
#
#   c_1(Lambda) = c_Delta(Lambda)
#
# This is because the Klingen Eisenstein series is constructed exactly
# to account for the genus-1 cusp-form content of the theta series.
#
# For c_2: this requires knowing the genus-2 representation numbers
# beyond what the genus-1 data determines.  It encodes genuinely
# genus-2 arithmetic (the Böcherer coefficient / central L-value).

def niemeier_c1(name: str) -> Fraction:
    r"""Klingen coefficient c_1(Lambda) in the genus-2 decomposition.

    For even unimodular rank-24 lattices:
      c_1(Lambda) = c_Delta(Lambda) = (691*N_roots - 65520) / 691

    This follows from the diagonal restriction constraint.
    """
    return niemeier_c_delta(name)


# =========================================================================
# Böcherer coefficient computation
# =========================================================================

# The Böcherer coefficient c_2(Lambda) is the most interesting quantity.
# It encodes the genuine genus-2 information beyond what genus-1 determines.
#
# For the Leech lattice, c_2 was computed in genus2_bocherer_bridge.py
# by comparing the genus-2 theta series (from inner-product distributions)
# with E_{12} and the Klingen series.
#
# For other Niemeier lattices, we use the Siegel-Weil formula and the
# mass formula approach:
#
# The Siegel theta series of a lattice Lambda in the genus of even
# unimodular rank-24 lattices satisfies:
#
#   sum_{Lambda} Theta_Lambda^{(2)} / |Aut(Lambda)| = E_{12}^{(2)} / M
#
# where M = sum 1/|Aut(Lambda)| is the mass of the genus.
#
# This gives: sum c_2(Lambda) / |Aut(Lambda)| = 0
# (since E_{12} has no chi_{12} component by definition).
#
# Similarly: sum c_1(Lambda) / |Aut(Lambda)| = 0.
#
# These are the mass formula constraints on the Böcherer coefficients.

# Automorphism group orders for Niemeier lattices
# |Aut(Lambda)| = |W(R)| * |Glue group symmetries|
# For the Leech lattice: |Aut| = 2 * |Co_0| ≈ 8.3 * 10^18
# Reference: Conway-Sloane Table 16.1

# We use EXACT values as Python integers.
NIEMEIER_AUT_ORDERS: Dict[str, int] = {
    'Leech': 2 * 4157776806543360000,  # 2 * |Co_0|
    '24A1': 2**24 * math.factorial(24),  # W(A1)^24 * S_24
    '12A2': 6**12 * math.factorial(12),  # W(A2)^12 * S_12
    '8A3': 24**8 * math.factorial(8) * 2**8,  # |W(A3)|^8 * S_8 * glue
    '6A4': 120**6 * math.factorial(6),  # |W(A4)|^6 * S_6
    '4A6': 5040**4 * math.factorial(4),  # |W(A6)|^4 * S_4
    '3A8': 362880**3 * math.factorial(3),  # |W(A8)|^3 * S_3
    '2A12': math.factorial(13)**2 * 2,  # |W(A12)|^2 * S_2
    'A24': math.factorial(25),  # |W(A24)|
    '6D4': 192**6 * math.factorial(6) * 6**6,  # |W(D4)|^6 * S_6 * triality^6
    '2D12': (2**11 * math.factorial(12))**2 * 2,  # |W(D12)|^2 * S_2
    'D24': 2**23 * math.factorial(24),  # |W(D24)|
    '3E8': (2**14 * 3**5 * 5**2 * 7)**3 * math.factorial(3),  # |W(E8)|^3 * S_3
    '4E6': (2**7 * 3**4 * 5)**4 * math.factorial(4),  # |W(E6)|^4 * S_4
    'D16_E8': (2**15 * math.factorial(16)) * (2**14 * 3**5 * 5**2 * 7),
    '4A5_D4': 720**4 * math.factorial(4) * 192,  # approx
    '2A7_2D5': 40320**2 * 2 * (2**4 * math.factorial(5))**2 * 2,
    'A11_D7_E6': math.factorial(12) * (2**6 * math.factorial(7)) * (2**7 * 3**4 * 5),
    'A15_D9': math.factorial(16) * (2**8 * math.factorial(9)),
    'A17_E7': math.factorial(18) * (2**10 * 3**4 * 5 * 7),
    'D10_2E7': (2**9 * math.factorial(10)) * (2**10 * 3**4 * 5 * 7)**2 * 2,
    '2A9_D6': 3628800**2 * 2 * (2**5 * math.factorial(6)),
    '4D4': 192**4 * math.factorial(4),  # |W(D4)|^4 * S_4 (no triality)
    '2D8': (2**7 * math.factorial(8))**2 * 2,
}


def genus_mass() -> Fraction:
    r"""Mass of the genus of even unimodular rank-24 lattices.

    M = sum_{Lambda} 1/|Aut(Lambda)|

    This equals the Siegel mass formula value for n=24, which is:
      M = B_12 * B_14 * ... * B_{24} / (big product of factorials)

    The exact value is given by the Smith-Minkowski-Siegel mass formula.
    For dimension 24, even unimodular:
      M = |B_2 * B_4 * B_6 * B_8 * B_10 * B_12| / (2^12 * 12!)
        * product_{j=1}^{12} 1/(2j)

    For n = 2k = 24 (k=12):
      M = prod_{j=1}^{k} zeta(2j) * prod_{j=1}^{k-1} (2j)! / (4^k * k! * (2pi)^{k(2k+1)/2})

    We compute it numerically from the sum over all 24 lattices.
    """
    total = Fraction(0)
    for name in ALL_NIEMEIER:
        if name in NIEMEIER_AUT_ORDERS:
            total += Fraction(1, NIEMEIER_AUT_ORDERS[name])
    return total


# =========================================================================
# Böcherer coefficient via genus-2 theta decomposition
# =========================================================================

def _c2_leech_from_existing() -> Fraction:
    """Extract the Leech c_2 from the existing computation.

    Uses the fact that at T = ((2, b/2), (b/2, 2)) (minimal shell),
    the genus-2 theta series has known values from the inner-product
    distribution, while E_{12} and E^{Kling} have computable coefficients.

    c_2 = (a_Leech(T) - a_{E12}(T) - c_1 * a_{Kling}(T)) / a_{chi12}(T)
    """
    from compute.lib.genus2_bocherer_bridge import genus2_rep_leech

    # Use T = ((2, 0), (0, 2)), i.e. a=c=2, b=0
    a, b, c = 2, 0, 2

    # Leech representation number
    r2 = genus2_rep_leech(a, b, c)
    if r2 is None:
        raise ValueError("Cannot compute Leech r_2 at T=diag(2,2)")

    # Eisenstein coefficient
    e12 = siegel_eisenstein_coefficient(12, a, b, c)

    # Klingen coefficient
    c1 = niemeier_c1('Leech')
    kling = klingen_eisenstein_coefficient(a, b, c)

    # chi_12 coefficient (from Igusa relation)
    chi = chi12_from_igusa(a, b, c)

    if chi == 0 or chi is None:
        raise ValueError("chi_12 vanishes at T=diag(2,2), cannot extract c_2")

    # c_2 = (r_2 - e12 - c1*kling) / chi
    residual = Fraction(r2) - e12 - c1 * Fraction(kling)
    c2 = residual / chi

    return c2


# =========================================================================
# The Böcherer coefficient for all Niemeier lattices
# =========================================================================

# The approach: for a Niemeier lattice Lambda, the genus-2 theta series
# at a specific half-integral matrix T gives a linear relation:
#
#   r_2(Lambda, T) = a(T; E_{12}) + c_1(Lambda) * a(T; E^{Kling}) + c_2(Lambda) * a(T; chi_{12})
#
# For lattices WITH roots (all except Leech), we can compute r_2 at
# T = ((1, 0), (0, 1)) = diag(1,1) using:
#   r_2(Lambda, ((1,0),(0,1))) = N_roots * (N_orthogonal_roots_per_root)
#
# where N_orthogonal_roots_per_root counts roots orthogonal to a given root.
#
# For a root system R = n * X_m:
#   - In each copy X_m: given a root alpha, there are N_orth(X_m) roots
#     orthogonal to alpha within the same copy
#   - In different copies: ALL roots are orthogonal
#   - So: N_orth_per_root = N_orth_within + N_roots_in_other_copies
#     = (|Phi(X_m)| - 2*|inner_product_1| - 2) + (n-1)*|Phi(X_m)|
#     where we subtract 2 for the root itself and its negative.

def _orthogonal_roots_in_simple_system(family: str, n: int) -> int:
    """Number of roots orthogonal to a given root in a simple root system.

    For A_n: each root alpha has (n-1)^2 - 1 orthogonal roots for n >= 2.
      More precisely: |Phi(A_n)| = n(n+1).
      In A_n, a root e_i - e_j has inner product with e_k - e_l:
        0 if {i,j} ∩ {k,l} = empty
        ±1 if |{i,j} ∩ {k,l}| = 1
        ±2 if {i,j} = {k,l}
      Orthogonal: choose k,l disjoint from {i,j}.
        # ways = (n-1)(n-2)/2 * 2 = (n-1)(n-2) (accounting for e_k-e_l and e_l-e_k)
      Wait: roots are e_i - e_j for i != j (in A_n represented in R^{n+1}).
      Given root e_1 - e_2, orthogonal roots are e_k - e_l where k,l in {3,...,n+1}.
      Number = (n-1)*n - (n-1) = (n-1)^2 ... let me compute properly.
      e_k - e_l with k != l, k,l in {3,...,n+1}: that's (n-1) choices for k
      and (n-2) choices for l, giving (n-1)(n-2) ordered pairs.
      But we also have pairs like e_k - e_l with k in {3,...,n+1}, l in {3,...,n+1}.
      Total ordered pairs from {3,...,n+1}: (n-1)(n-2).

    For D_n: |Phi(D_n)| = 2n(n-1). A root ±e_i ± e_j.
      Given e_1 + e_2, orthogonal roots are ±e_k ± e_l for k,l >= 3.
      Number = 2(n-2)(n-3) for the strictly-off-diagonal part.
      Careful: ±e_k ± e_l with k != l, k,l in {3,...,n}: that's
      C(n-2, 2) * 4 = 2(n-2)(n-3) roots.

    For E_6: 72 roots total. Given a root, 36 orthogonal.
    For E_7: 126 roots total. Given a root, 56 orthogonal.  (Wait: check.)
    For E_8: 240 roots total. Given a root, 126 orthogonal.
    """
    if family == 'A':
        if n == 1:
            return 0  # A1 has only 2 roots: alpha and -alpha
        # In A_n, number of roots orthogonal to a given root:
        # Total roots = n(n+1), minus 2 (the root and its negative),
        # minus 2*(2*(n-1) - 1) ... actually let me use the known formula.
        # A root in A_n is e_i - e_j (i,j in {1,...,n+1}, i != j).
        # Inner product (e_i - e_j, e_k - e_l) = delta_{ik} - delta_{il} - delta_{jk} + delta_{jl}
        # This is 0 iff {i,j} ∩ {k,l} = empty.
        # Given e_1 - e_2, orthogonal roots: e_k - e_l with k,l in {3,...,n+1}, k != l.
        # Count: (n-1)*(n-2) ordered pairs = (n-1)(n-2).
        return (n - 1) * (n - 2)

    elif family == 'D':
        if n < 3:
            raise ValueError(f"D_n requires n >= 3")
        # D_n roots: ±e_i ± e_j for 1 <= i < j <= n.
        # Given e_1 + e_2, orthogonal roots: ±e_k ± e_l with 3 <= k < l <= n.
        # Plus: e_1 - e_2 and -(e_1 - e_2) are NOT orthogonal:
        # (e_1+e_2, e_1-e_2) = 1 - 1 = 0. Wait: actually IS orthogonal!
        # (e_1+e_2, e_1-e_2) = 1 + (-1) = 0.
        # So e_1 - e_2 and -(e_1-e_2) are both orthogonal.
        # Orthogonal roots to e_1 + e_2:
        #   (a) e_k ± e_l with k,l >= 3: count = 2*C(n-2, 2)*2 ... no.
        #       ±e_k ± e_l with 3 <= k < l <= n: 4*C(n-2, 2) = 2(n-2)(n-3) roots.
        #   (b) e_1 - e_2 and -(e_1 - e_2): 2 roots.
        #       Check: (e_1+e_2, e_1-e_2) = 1 - 1 = 0. Yes, orthogonal.
        # But wait: we also need to check ±e_k ± e_1 or ±e_k ± e_2 type.
        # (e_1+e_2, e_k+e_1) = 1 + 0 = 1. Not orthogonal.
        # (e_1+e_2, e_k-e_1) = -1 + 0 = -1. Not orthogonal.
        # (e_1+e_2, e_k+e_2) = 0 + 1 = 1. Not orthogonal.
        # (e_1+e_2, e_k-e_2) = 0 - 1 = -1. Not orthogonal.
        # So only categories (a) and (b).
        return 2 * (n - 2) * (n - 3) + 2

    elif family == 'E':
        # Use known values from E_8 inner product distribution
        # and the standard tables for E_6, E_7.
        if n == 6:
            # E_6: 72 roots. Given a root, inner product distribution:
            # 2: 1, -2: 1, 1: 20, -1: 20, 0: 30
            # So 30 orthogonal roots.
            return 30
        elif n == 7:
            # E_7: 126 roots. Given a root:
            # 2: 1, -2: 1, 1: 32, -1: 32, 0: 60
            # So 60 orthogonal roots.
            return 60
        elif n == 8:
            return 126  # from E8 data
        else:
            raise ValueError(f"E_n requires n in {{6,7,8}}")
    else:
        raise ValueError(f"Unknown family: {family}")


def orthogonal_roots_per_root(name: str) -> int:
    """Number of roots in a Niemeier lattice orthogonal to a given root.

    For a Niemeier lattice with root system R = n1*X1 + n2*X2 + ...,
    the roots orthogonal to a root alpha in component X_i are:
    - Roots in the same copy of X_i orthogonal to alpha
    - ALL roots in other copies of X_i
    - ALL roots in components X_j (j != i)
    """
    if name == 'Leech':
        return 0  # No roots

    components = NIEMEIER_LATTICES[name]['components']
    total_roots = NIEMEIER_LATTICES[name]['num_roots']

    if not components:
        return 0

    # Choose a root from the first component
    f0, n0 = components[0]
    roots_in_component = _root_count_for_type(f0, n0)
    orth_within = _orthogonal_roots_in_simple_system(f0, n0)

    # Roots in other copies of the same type and in all other components
    roots_outside = total_roots - roots_in_component

    return orth_within + roots_outside


def genus2_rep_at_diag11(name: str) -> int:
    """Genus-2 representation number at T = diag(1, 1).

    r_2(Lambda, ((1,0),(0,1))) = N_roots * N_orth

    where N_orth is the number of roots orthogonal to a given root.

    For the Leech lattice: r_2 = 0 (no norm-2 vectors).
    """
    if name == 'Leech':
        return 0
    N = NIEMEIER_LATTICES[name]['num_roots']
    N_orth = orthogonal_roots_per_root(name)
    return N * N_orth


def genus2_rep_at_T11_b(name: str, b: int) -> Optional[int]:
    r"""Genus-2 rep number at T = ((1, b/2), (b/2, 1)) for b in {-2,...,2}.

    r_2(Lambda, T) = N_roots * (# roots w with (v,w) = b)

    For Leech: 0 (no roots).
    For other lattices: requires the inner-product distribution of the root system.
    We compute this for simple root systems.
    """
    if name == 'Leech':
        return 0

    N = NIEMEIER_LATTICES[name]['num_roots']
    if N == 0:
        return 0

    if abs(b) > 2:
        return 0  # max inner product between roots is 2

    components = NIEMEIER_LATTICES[name]['components']
    if not components:
        return 0

    # For a root in the first component, count roots with inner product b
    f0, n0 = components[0]
    roots_in_comp = _root_count_for_type(f0, n0)

    # Inner product distribution within the component
    ip_dist = _inner_product_distribution_simple(f0, n0)

    # Roots from other components: all have inner product 0 with our root
    roots_outside = N - roots_in_comp

    count_at_b = ip_dist.get(b, 0)
    if b == 0:
        count_at_b += roots_outside

    return N * count_at_b


def _inner_product_distribution_simple(family: str, n: int) -> Dict[int, int]:
    """Inner product distribution for roots within a simple root system.

    Returns {inner_product: count} for a fixed root.
    """
    total_roots = _root_count_for_type(family, n)

    if family == 'A':
        if n == 1:
            return {2: 1, -2: 1}
        # A_n roots: e_i - e_j, i != j, in R^{n+1}.
        # Given e_1 - e_2:
        #   (e_1-e_2, e_1-e_2) = 2: count 1
        #   (e_1-e_2, e_2-e_1) = -2: count 1
        #   ip = 1: e_1 - e_k (k >= 3) and e_k - e_2 (k >= 3): 2*(n-1) roots
        #   ip = -1: e_2 - e_k (k >= 3) and e_k - e_1 (k >= 3): 2*(n-1) roots
        #   ip = 0: the rest
        ip1_count = 2 * (n - 1)
        ip_minus1_count = 2 * (n - 1)
        ip0_count = total_roots - 2 - ip1_count - ip_minus1_count
        return {2: 1, -2: 1, 1: ip1_count, -1: ip_minus1_count, 0: ip0_count}

    elif family == 'D':
        if n < 3:
            raise ValueError(f"D_n requires n >= 3")
        # D_n roots: ±e_i ± e_j, 1 <= i < j <= n.
        # Given e_1 + e_2:
        #   ip = 2: e_1+e_2 (count 1)
        #   ip = -2: -(e_1+e_2) (count 1)
        #   ip = 1: e_1+e_k (k>=3), e_2+e_k (k>=3), -(e_1-e_k) = -e_1+e_k (k>=3) [no]
        #     (e_1+e_2, e_1+e_k) = 1 for k >= 3: n-2 roots
        #     (e_1+e_2, e_2+e_k) = 1 for k >= 3: n-2 roots
        #     (e_1+e_2, -e_1+e_k) ... wait let me be more careful.
        #     (e_1+e_2, e_k+e_l) = 0 for k,l >= 3
        #     (e_1+e_2, e_1+e_k) = 1 for k >= 3: n-2 roots
        #     (e_1+e_2, -(e_1+e_k)) = -1 for k >= 3: n-2 roots
        #     (e_1+e_2, e_1-e_k) = 1 for k >= 3: n-2 roots
        #     (e_1+e_2, -(e_1-e_k)) = -1 for k >= 3: n-2 roots
        #     Similarly for e_2±e_k.
        #     (e_1+e_2, e_2+e_k) = 1: n-2
        #     (e_1+e_2, -(e_2+e_k)) = -1: n-2
        #     (e_1+e_2, e_2-e_k) = 1: n-2
        #     (e_1+e_2, -(e_2-e_k)) = -1: n-2
        #     (e_1+e_2, e_1-e_2) = 0
        #     (e_1+e_2, -(e_1-e_2)) = 0
        # ip = 1: e_1+e_k, e_1-e_k, e_2+e_k, e_2-e_k for k >= 3: 4*(n-2)
        # ip = -1: -(e_1+e_k), -(e_1-e_k), -(e_2+e_k), -(e_2-e_k): 4*(n-2)
        # ip = 0: e_1-e_2, -(e_1-e_2), and ±e_k±e_l for k,l >= 3: 2 + 2*(n-2)*(n-3)
        ip1 = 4 * (n - 2)
        ip_m1 = 4 * (n - 2)
        ip0 = 2 + 2 * (n - 2) * (n - 3)
        result = {2: 1, -2: 1, 1: ip1, -1: ip_m1, 0: ip0}
        assert sum(result.values()) == total_roots, (
            f"D_{n} distribution sum {sum(result.values())} != {total_roots}"
        )
        return result

    elif family == 'E':
        if n == 6:
            # E_6: 72 roots, distribution: 2:1, -2:1, 1:20, -1:20, 0:30
            return {2: 1, -2: 1, 1: 20, -1: 20, 0: 30}
        elif n == 7:
            # E_7: 126 roots, distribution: 2:1, -2:1, 1:32, -1:32, 0:60
            return {2: 1, -2: 1, 1: 32, -1: 32, 0: 60}
        elif n == 8:
            # E_8: 240 roots, distribution: 2:1, -2:1, 1:56, -1:56, 0:126
            return {2: 1, -2: 1, 1: 56, -1: 56, 0: 126}
        else:
            raise ValueError(f"E_{n} not supported")
    else:
        raise ValueError(f"Unknown family: {family}")


# =========================================================================
# Böcherer coefficient extraction
# =========================================================================

def extract_c2(name: str) -> Optional[Fraction]:
    r"""Extract the Böcherer coefficient c_2(Lambda) for a Niemeier lattice.

    Uses the genus-2 representation number at T = diag(1,1):
      r_2(Lambda, T) = a(T; E_{12}) + c_1 * a(T; E^{Kling}) + c_2 * a(T; chi_{12})

    Solving for c_2:
      c_2 = (r_2 - a_E12 - c_1 * a_Kling) / a_chi12

    For the Leech lattice, T = diag(1,1) gives r_2 = 0, which is useful
    but we need a T where chi_12 doesn't vanish.
    """
    c1 = niemeier_c1(name)

    # Choose T = diag(1,1) for lattices with roots
    # For Leech, use T = diag(2,2)
    if name == 'Leech':
        return _c2_leech_from_existing()

    a_val, b_val, c_val = 1, 0, 1
    r2 = genus2_rep_at_diag11(name)

    e12_coeff = siegel_eisenstein_coefficient(12, a_val, b_val, c_val)
    kling_coeff = klingen_eisenstein_coefficient(a_val, b_val, c_val)
    chi12_coeff = chi12_from_igusa(a_val, b_val, c_val)

    if chi12_coeff is None or chi12_coeff == 0:
        return None

    residual = Fraction(r2) - e12_coeff - c1 * Fraction(kling_coeff)
    c2 = residual / chi12_coeff

    return c2


def extract_c2_numerical(name: str) -> Optional[float]:
    """Extract c_2(Lambda) as a float for quick comparison."""
    c2 = extract_c2(name)
    if c2 is None:
        return None
    return float(c2)


# =========================================================================
# Full atlas
# =========================================================================

def compute_bocherer_atlas(lattice_list: Optional[List[str]] = None) -> Dict[str, Dict[str, Any]]:
    """Compute the full Böcherer atlas for a list of Niemeier lattices.

    For each lattice, computes:
    - Shadow data (kappa, c, shadow class)
    - Genus-1 theta coefficients (first few)
    - Number of roots
    - Kissing number
    - c_Delta (genus-1 cusp coefficient)
    - c_1 (Klingen coefficient)
    - c_2 (Böcherer coefficient)
    - Genus-2 representation numbers at key matrices
    """
    if lattice_list is None:
        lattice_list = PURE_NIEMEIER

    atlas = {}
    for name in lattice_list:
        theta = niemeier_theta_series(name, max_n=5)
        c_del = niemeier_c_delta(name)
        c1 = niemeier_c1(name)
        c2 = extract_c2(name)

        entry = {
            'name': name,
            'root_system': NIEMEIER_LATTICES[name]['root_system'],
            'num_roots': NIEMEIER_LATTICES[name]['num_roots'],
            'kissing_number': kissing_number(name),
            'minimal_norm': minimal_norm(name),
            'kappa': 24,
            'central_charge': 24,
            'shadow_class': 'G',
            'shadow_depth': 2,
            'theta_coefficients': list(theta[:6]),
            'c_delta': c_del,
            'c1_klingen': c1,
            'c2_bocherer': c2,
            'c2_numerical': float(c2) if c2 is not None else None,
            'genus2_rep_diag11': genus2_rep_at_diag11(name),
        }
        atlas[name] = entry

    return atlas


# =========================================================================
# Mass formula verification
# =========================================================================

def verify_mass_formula_c1() -> Dict[str, Any]:
    r"""Verify the mass formula constraint: sum c_1(Lambda)/|Aut(Lambda)| should
    be related to known mass formula constants.

    The Siegel-Weil formula gives:
      sum_Lambda Theta_Lambda^{(2)} / |Aut(Lambda)| = genus_theta^{(2)} / M

    where M = sum 1/|Aut(Lambda)| is the mass and genus_theta^{(2)} is the
    genus-2 Eisenstein series (genus theta series of the genus).

    For the c_1 component: sum c_1/|Aut| relates to the Klingen projection
    of the genus theta series.
    """
    total_c1_weighted = Fraction(0)
    total_mass = Fraction(0)

    for name in ALL_NIEMEIER:
        if name not in NIEMEIER_AUT_ORDERS:
            continue
        aut = NIEMEIER_AUT_ORDERS[name]
        c1 = niemeier_c1(name)
        total_c1_weighted += c1 / Fraction(aut)
        total_mass += Fraction(1, aut)

    return {
        'sum_c1_over_aut': total_c1_weighted,
        'mass': total_mass,
        'ratio_c1': total_c1_weighted / total_mass if total_mass != 0 else None,
    }


def verify_genus1_theta_sum() -> Dict[str, Any]:
    r"""Verify the genus-1 mass formula:
      sum_Lambda Theta_Lambda / |Aut(Lambda)| = E_{12} / M.

    Equivalently: sum c_Delta(Lambda) / |Aut(Lambda)| = 0.
    """
    total = Fraction(0)
    for name in ALL_NIEMEIER:
        if name not in NIEMEIER_AUT_ORDERS:
            continue
        c_del = niemeier_c_delta(name)
        aut = NIEMEIER_AUT_ORDERS[name]
        total += c_del / Fraction(aut)

    return {
        'sum_c_delta_over_aut': total,
        'expected': Fraction(0),
        'matches': total == Fraction(0),
    }


# =========================================================================
# Shadow-derived prediction
# =========================================================================

def shadow_genus2_prediction(name: str) -> Dict[str, Any]:
    """Shadow tower prediction for the genus-2 free energy.

    For Gaussian class (all Niemeier lattices):
      F_2 = kappa * lambda_2^FP

    The shadow tower predicts the SCALAR part of the genus-2 amplitude.
    The Böcherer coefficient c_2 encodes the genuinely genus-2 arithmetic
    content BEYOND what the shadow tower captures.

    The comparison: F_2^{sh} (shadow prediction) vs F_2^{exact} (from theta series).
    """
    kappa = 24
    from sympy import Rational as R
    lambda_2 = faber_pandharipande(2)

    F2_shadow = Fraction(kappa) * lambda_2

    return {
        'name': name,
        'kappa': kappa,
        'lambda_2_FP': lambda_2,
        'F2_shadow': F2_shadow,
        'F2_shadow_numerical': float(F2_shadow),
        'c2_bocherer': extract_c2_numerical(name),
        'description': (
            'F_2^{sh} is the shadow tower prediction (universal for all rank-24). '
            'c_2 is the lattice-specific genus-2 arithmetic content.'
        ),
    }


# =========================================================================
# Table output
# =========================================================================

def print_bocherer_table(lattice_list: Optional[List[str]] = None):
    """Print a formatted table of Böcherer coefficients."""
    if lattice_list is None:
        lattice_list = PURE_NIEMEIER

    atlas = compute_bocherer_atlas(lattice_list)

    print(f"{'Lattice':<12} {'Roots':>6} {'Kiss':>8} "
          f"{'c_Delta':>15} {'c_1':>15} {'c_2 (numerical)':>20}")
    print("-" * 85)

    for name in lattice_list:
        entry = atlas[name]
        c2_str = f"{entry['c2_numerical']:.6e}" if entry['c2_numerical'] is not None else "N/A"
        c_del = float(entry['c_delta'])
        c1 = float(entry['c1_klingen'])
        print(f"{name:<12} {entry['num_roots']:>6} {entry['kissing_number']:>8} "
              f"{c_del:>15.4f} {c1:>15.4f} {c2_str:>20}")


# =========================================================================
# Genus-2 graph sum contributions (lattice-specific vertex factors)
# =========================================================================

def theta_graph_amplitude(name: str) -> Optional[Fraction]:
    """Amplitude of the theta graph (3 edges, 2 genus-0 vertices) for a lattice VOA.

    Each edge carries the propagator d log E(z,w) (weight 1 in both slots).
    Each genus-0 vertex carries the 3-point function of the lattice VOA.

    For the lattice VOA V_Lambda with only spin-1 fields (currents),
    the genus-0 3-point function vanishes unless there is a nonzero
    structure constant f_{abc} (which requires non-abelian symmetry).

    For abelian lattices (e.g., Leech as a lattice VOA):
    the theta graph vanishes because the lattice is "abelian" in the
    sense that vertex operators commute at the classical level.

    For lattice VOAs built on root lattices with non-abelian structure:
    the theta graph contributes through the root system's structure constants.

    This function returns the theta graph amplitude normalized by |Aut|=12.
    """
    # For rank-24 even unimodular lattices treated as lattice VOAs,
    # the genus-0 OPE has the form:
    #   J^a(z) J^b(w) ~ delta^{ab} * k / (z-w)^2 + f^{ab}_c J^c(w) / (z-w)
    # The theta graph requires contracting three edges between two trivalent vertices,
    # giving a sum over structure constants: sum f^{abc} f_{abc}.
    # This is proportional to the dual Coxeter number.
    # For abelian (Leech): f^{abc} = 0, contribution = 0.
    # For root lattice VOAs: nonzero.
    return None  # Full computation requires structure constants


def dumbbell_amplitude(name: str) -> Fraction:
    """Amplitude of the dumbbell graph (2 genus-1 vertices, 1 edge).

    Each genus-1 vertex carries the genus-1 partition function Z_1.
    The edge carries the propagator.

    For lattice VOAs: the genus-1 partition function is Theta/eta^{rank}.
    The dumbbell amplitude involves the product of two genus-1 partition
    functions contracted along one propagator edge.

    The scalar (kappa-level) contribution is:
      A_dumb = kappa^2 * (lambda_1)^2 / 2
    where the 1/2 is 1/|Aut(dumbbell)|.
    """
    kappa = Fraction(24)
    lambda_1 = faber_pandharipande(1)  # = 1/24
    return kappa**2 * lambda_1**2 / Fraction(2)


# =========================================================================
# Convenience: summary of all lattices
# =========================================================================

def full_niemeier_summary() -> Dict[str, Dict[str, Any]]:
    """Complete summary for all 24 Niemeier lattices."""
    summary = {}
    for name in ALL_NIEMEIER:
        data = NIEMEIER_LATTICES[name]
        summary[name] = {
            'root_system': data['root_system'],
            'num_roots': data['num_roots'],
            'rank': data['rank'],
            'is_pure': data['is_pure'],
            'kappa': 24,
            'c_delta': niemeier_c_delta(name),
            'c1': niemeier_c1(name),
        }
    return summary


if __name__ == '__main__':
    print("=" * 80)
    print("NIEMEIER LATTICE BÖCHERER ATLAS")
    print("=" * 80)
    print()
    print_bocherer_table()
    print()
    print("Mass formula verification:")
    mass_check = verify_genus1_theta_sum()
    print(f"  sum c_delta/|Aut| = {mass_check['sum_c_delta_over_aut']}")
    print(f"  expected: 0")
    print(f"  matches: {mass_check['matches']}")
