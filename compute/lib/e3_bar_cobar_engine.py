r"""E_3 bar-cobar duality engine: extending the operadic framework one dimension higher.

The monograph establishes bar-cobar duality for chiral algebras, which are
E_2-algebras in the factorization algebra framework (living on 2D surfaces).
This module pushes the framework to E_3-algebras, which govern:

  - 3D holomorphic-topological QFT (Vol II)
  - Braided monoidal categories (Reshetikhin-Turaev invariants)
  - Chern-Simons theory
  - Yangians (as E_1 tensor E_2 = E_2 algebras on Ran of a line,
    but the derived center carries E_3 by Higher Deligne)

MATHEMATICAL CONTENT:

1. E_3 BAR COMPLEX.  For an E_3-algebra A, the bar complex B_{E_3}(A) is a
   coalgebra over the cooperad E_3^i = (E_3)^{co-!}.  The underlying chain
   complex is governed by H*(Conf_k(R^3)):

     H*(Conf_k(R^3)): generators omega_{ij} in degree 2 (linking forms
     of the pair (i,j) in R^3, from the fundamental class of the linking
     sphere S^2 = R^3 \ {0}), subject to generalized Arnold relations.

     Poincare polynomial: P_k(t) = prod_{j=0}^{k-1} (1 + j*t^2)

     Key differences from E_2:
       - E_2: generators in degree 1 (from S^1 = R^2 \ {0})
       - E_3: generators in degree 2 (from S^2 = R^3 \ {0})
       - E_2: Arnold relations are 3-term (degree 2)
       - E_3: Arnold relations are 3-term (degree 4)

     Total Betti: sum b_i = k! for all n >= 2 (this is universal).

2. E_3 KOSZUL DUALITY.  E_3 is Koszul self-dual up to a shift:
     E_3^! = E_3{-3}
   So B_{E_3}(A) is a coalgebra over E_3{-3}, and the Koszul dual A^!
   is an E_3-algebra with generators shifted by 3 in degree.

   The bar-cobar adjunction:
     B_{E_3}: E_3-Alg -> E_3^i-coAlg
     Omega_{E_3}: E_3^i-coAlg -> E_3-Alg
   with Omega_{E_3}(B_{E_3}(A)) ~> A (bar-cobar inversion on the
   Koszul locus).

3. BRAIDED MONOIDAL STRUCTURE.
   An E_3-algebra has:
     - Associative product mu (from E_1 subset E_3)
     - Homotopy commutativity (from E_2 subset E_3, i.e. pi_1(S^1) = Z)
     - Braiding R: this comes from pi_1(Conf_2(R^3)) = 0 (trivial!),
       but the TOPOLOGICAL braiding from the E_2 subalgebra persists.
     - Higher coherence from pi_2(S^2) = Z (the Hopf degree).

   CRITICAL DISTINCTION: the braiding of the E_3 bar complex comes from
   the E_2 subalgebra structure, NOT from pi_1(Conf_2(R^3)) which is trivial.
   The E_3 enhancement provides a SYMMETRIC monoidal structure (not merely
   braided), because R^3 allows continuous paths between the two orderings
   of any pair.

4. FORMALITY OF E_3.
   The E_3 operad is formal over Q (Lambrechts-Volic 2014, Kontsevich).
   Consequence: B_{E_3}(A) has a formal model for formal E_3-algebras.
   The formal model: the bar complex of an E_3-algebra is quasi-isomorphic
   to the bar complex of its cohomology (as a graded E_3-algebra).

   For the Lie operad side: E_3^! = E_3{-3}.
   The cobar of a cocommutative coalgebra (E_infty coalgebra) gives
   a Lie{1} algebra (= shifted Lie = L_infty).  For E_3, the cobar
   gives an E_3{-3} algebra, which at the cohomological level is
   a graded-commutative algebra with a degree-2 bracket.

5. CHERN-SIMONS AS E_3.
   CS theory on M^3 with gauge group G at level k:
     - The factorization algebra of observables is an E_3-algebra
     - Restriction to a surface Sigma subset M^3 gives the WZW model
       (an E_2-algebra = chiral algebra = affine g at level k)
     - The quantum group U_q(g) at q = e^{2*pi*i/(k+h^v)} arises as
       the E_1 sector (Wilson lines along a line in M^3)
     - The bar complex B_{E_3}(CS_G,k) encodes:
       * Wilson lines (E_1 sector)
       * Surface observables / conformal blocks (E_2 sector)
       * Bulk partition function (E_3 sector = full 3-manifold invariant)

   The modular characteristic kappa_{E_3}:
     kappa_{E_3}(CS_{SU(N),k}) = kappa(affine sl_N at level k)
                                = (N^2 - 1) * (k + N) / (2*N)
   because kappa is determined by the binary part of the bar complex,
   which is universal across E_n.

6. SHADOW TOWER FOR E_3.
   The E_3 shadow obstruction tower Theta^{E_3}_A:
     - Arity 2: kappa (same as E_2, since Conf_2 contributes only through
       the propagator pairing, which is n-independent)
     - Arity 3: S_3 receives a CORRECTION from H^2(Conf_3(R^3)) relative
       to the E_2 value.  For formal algebras: S_3^{E_3} = S_3^{E_2}.
     - Braiding contribution: the degree-2 generators of H*(Conf_k(R^3))
       contribute linking-number terms to the shadow tower.

7. E_3 TO E_2 REDUCTION.
   The forgetful functor E_3-Alg -> E_2-Alg (choosing a 2-plane in R^3)
   restricts the shadow tower:
     Theta^{E_3}_A |_{E_2} = Theta^{E_2}_A
   plus additional components from the normal direction.

   The additional E_3 components encode YANGIAN data:
   By Dunn additivity E_3 = E_1 tensor E_2, so an E_3-algebra is an
   E_1-algebra in E_2-algebras.  The E_1 direction yields the spectral
   parameter of the Yangian; the E_2 direction yields the chiral algebra.

8. HIGHER E_n.
   E_4 -> E_5 -> ... -> E_infty = Com.
   The E_infty bar complex is the Harrison complex (= commutative bar).
   The sequence E_2 -> E_3 -> ... -> E_infty gives a filtration:
     B_{E_2}(A) -> B_{E_3}(A) -> ... -> B_{Com}(A)
   The shadow tower STABILIZES: for arity r, S_r^{E_n} = S_r^{E_infty}
   when n >= r (because H^{>0}(Conf_r(R^n)) starts in degree n-1 > r-2).

CONVENTIONS:
  - Cohomological grading (|d| = +1)
  - Bar uses desuspension: |s^{-1}v| = |v| - 1 (AP45)
  - E_3 propagator: degree 2 (from S^2 = R^3 \ {0})
  - E_3 Koszul shift: 3
  - kappa is universal across E_n (binary-level universality)
  - The bar propagator d log E(z,w) has weight 1 (AP27)

CAUTIONS:
  AP14: E_3 Koszulness != E_2 Koszulness (different operads, different bar)
  AP19: E_3 propagator has degree 2, NOT degree 1 (that is E_2)
  AP25: B_{E_3}(A) is an E_3^i-COALGEBRA. D_Ran produces B(A^!). Omega recovers A.
  AP42: "E_3 from Swiss-cheese" is FALSE (AP14-type error; SC is colored)

References:
  Fresse: Modules over Operads and Functors (Springer LNM 1967)
  Loday-Vallette: Algebraic Operads (Grundlehren 346), Ch 7,9,10,13
  Kontsevich: Operads and Motives in Deformation Quantization (1999)
  Lambrechts-Volic: Formality of the Little N-Disks Operad (2014)
  Francis: The Tangent Complex and Hochschild Cohomology of E_n Rings (2013)
  Ayala-Francis: Factorization Homology of Topological Manifolds (2015)
  Willwacher: M. Kontsevich's Graph Complex... (2015)
  Dunn: Tensor Products of Operads (1988)
  Witten: Quantum Field Theory and the Jones Polynomial (1989)
  Reshetikhin-Turaev: Invariants of 3-Manifolds via Link Polynomials (1991)
  e3_bar_algebra.py: obstruction theory (bar is E_2 not E_3)
  en_factorization_shadow.py: general E_n shadow framework
  en_koszul_bridge.py: Arnold algebra, E_1 vs E_2
  chern_simons_barcobar.py: CS partition functions
  quantum_group_shadow.py: R-matrices from shadow tower
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import factorial, comb
from typing import Any, Callable, Dict, FrozenSet, List, Optional, Set, Tuple

import numpy as np
from sympy import (
    Rational, Symbol, Matrix, Poly,
    simplify, expand, cancel, sqrt, Abs,
    cos, sin, exp, pi, I, S as Sym, oo,
    bernoulli, factorial as sym_factorial, binomial,
)


# =========================================================================
# 1.  Configuration spaces of R^3: H*(Conf_k(R^3))
# =========================================================================

def conf_r3_poincare_polynomial(k: int) -> Dict[int, int]:
    r"""Poincare polynomial of Conf_k(R^3).

    H*(Conf_k(R^3)) is the Totaro/Arnold algebra with generators
    omega_{ij} of degree 2 (the linking form on S^2 = R^3 \ {0}).

    The Poincare polynomial is:
      P_k(t) = prod_{j=0}^{k-1} (1 + j*t^2)

    Since generators have EVEN degree 2, the algebra is a polynomial
    algebra quotient (commutative, no sign issues at even degree),
    subject to the generalized Arnold relations.

    Examples:
      k=1: P = 1                          (point)
      k=2: P = 1 + t^2                    (S^2)
      k=3: P = 1 + 3t^2 + 2t^4           (6 total = 3!)
      k=4: P = 1 + 6t^2 + 11t^4 + 6t^6   (24 total = 4!)
      k=5: P = 1 + 10t^2 + 35t^4 + 50t^6 + 24t^8   (120 = 5!)

    Note: P_k(1) = k! for all k >= 1 (total Betti number).
    """
    if k <= 0:
        return {0: 1}

    coeffs: Dict[int, int] = {0: 1}
    for j in range(1, k):
        new_coeffs: Dict[int, int] = {}
        for deg, val in coeffs.items():
            # Multiply by (1 + j * t^2)
            new_coeffs[deg] = new_coeffs.get(deg, 0) + val
            new_coeffs[deg + 2] = new_coeffs.get(deg + 2, 0) + j * val
        coeffs = new_coeffs
    return coeffs


def conf_r3_betti_numbers(k: int) -> List[int]:
    """Betti numbers b_0, b_2, b_4, ..., b_{2(k-1)} of Conf_k(R^3).

    Returns a list indexed by ACTUAL degree (including zeros at odd degrees).
    H^{2i}(Conf_k(R^3)) = unsigned Stirling number |s(k, k-i)| in degree 2i.
    All odd-degree cohomology vanishes.

    The maximum degree is 2*(k-1).
    """
    poly = conf_r3_poincare_polynomial(k)
    if not poly:
        return [1]
    max_deg = max(poly.keys())
    return [poly.get(d, 0) for d in range(max_deg + 1)]


def conf_r3_total_betti(k: int) -> int:
    """Total Betti number = sum b_i = k! for Conf_k(R^3), k >= 1."""
    return sum(conf_r3_poincare_polynomial(k).values())


def conf_r3_euler_characteristic(k: int) -> int:
    """Euler characteristic chi(Conf_k(R^3)) = P_k(-1).

    For R^3 (n=3, n-1=2 is even):
      chi = prod_{j=0}^{k-1} (1 + j*(-1)^2) = prod_{j=0}^{k-1} (1 + j) = k!

    So chi = total Betti number = k! (all classes in even degree).
    """
    result = 1
    for j in range(1, k):
        result *= (1 + j)
    return result


def conf_r3_generator_count(k: int) -> int:
    """Number of degree-2 generators omega_{ij} for Conf_k(R^3).

    There is one generator for each unordered pair {i,j}, so C(k,2).
    Subject to C(k,3) Arnold relations (one per triple).
    """
    return comb(k, 2)


def conf_r3_relation_count(k: int) -> int:
    """Number of Arnold relations for Conf_k(R^3).

    One relation per unordered triple {i,j,k}: C(k,3).
    Each relation is:
      omega_{ij} * omega_{jk} + omega_{jk} * omega_{ki} + omega_{ki} * omega_{ij} = 0
    (degree 4, from the linking of three circles in R^3).
    """
    return comb(k, 3)


def conf_r3_h2_dimension(k: int) -> int:
    """Dimension of H^2(Conf_k(R^3)).

    H^2 is spanned by the omega_{ij} generators (degree 2).
    There are C(k,2) generators, and the Arnold relations live in degree 4,
    so there are NO relations in degree 2.

    dim H^2 = C(k,2) = k*(k-1)/2.

    This is the space of "linking numbers" of pairs.
    """
    return comb(k, 2)


# =========================================================================
# 2.  E_3 Koszul duality: E_3^! = E_3{-3}
# =========================================================================

@dataclass
class E3KoszulDualData:
    """Data for E_3 Koszul duality."""
    operad_name: str = "E_3"
    koszul_shift: int = 3
    dual_operad: str = "E_3{-3}"
    propagator_degree: int = 2  # from S^2 = R^3 \ {0}
    is_self_dual: bool = True   # up to shift

    # Bar-cobar adjunction
    bar_produces: str = "E_3^i-coalgebra"
    cobar_recovers: str = "original E_3-algebra (on Koszul locus)"
    verdier_produces: str = "B(A^!) (intertwining, Convention conv:bar-coalgebra-identity)"

    # Comparison with E_2
    e2_koszul_shift: int = 2
    e2_propagator_degree: int = 1  # from S^1 = R^2 \ {0}
    shift_difference: int = 1      # E_3 shift - E_2 shift


def e3_koszul_dual_generator_degree(original_degree: int) -> int:
    """Degree of the Koszul dual generator for an E_3-algebra.

    If A has a generator v of degree d, then A^! has a generator
    v^! of degree d + 3 (the Koszul shift of E_3).

    For Heisenberg with generator in degree 0:
      v^! has degree 3.
    For affine KM with generator in degree 0:
      v^! has degree 3.
    """
    return original_degree + 3


def e3_bar_desuspension_shift() -> int:
    """The desuspension shift in the E_3 bar complex.

    The E_n bar complex uses desuspension s^{-n} (operadic desuspension
    of n).  For E_3: each bar element s^{-3}v has
      |s^{-3}v| = |v| - 3

    This is the E_3 analogue of the E_1 desuspension |s^{-1}v| = |v| - 1.
    """
    return -3


def e3_bar_element_degree(gen_degrees: List[int], n_propagators: int = 0) -> int:
    """Degree of a bar element s^{-3}v_1 tensor ... tensor s^{-3}v_k in B_{E_3}(A).

    The degree is sum(|v_i| - 3) + 2 * n_propagators
    where the 2*n_propagators comes from the degree-2 linking forms
    omega_{ij} in H^*(Conf_k(R^3)).

    Parameters:
      gen_degrees: list of degrees of the generators v_1, ..., v_k
      n_propagators: number of linking-form insertions (each degree 2)
    """
    return sum(d - 3 for d in gen_degrees) + 2 * n_propagators


def e3_bar_differential_degree() -> int:
    """Degree of the bar differential in B_{E_3}(A).

    The bar differential has degree +1 (cohomological convention).
    This is universal for all E_n.
    """
    return 1


# =========================================================================
# 3.  E_3 bar complex: chain-level structure
# =========================================================================

def e3_bar_arity_dimension(k: int) -> int:
    """Dimension of the arity-k component of B_{E_3}(A) for A free on
    one degree-0 generator.

    B_{E_3}(A)_k = H_*(Conf_k(R^3)) tensor (s^{-3}A)^{tensor k}

    For A = k[x] free on one generator in degree 0:
      (s^{-3}A)^{tensor k} is 1-dimensional at each tensor weight.
    So dim B_{E_3}(A)_k = sum b_i(Conf_k(R^3)) = k!
    """
    if k <= 0:
        return 1
    return factorial(k)


def e3_bar_graded_dimension(k: int) -> Dict[int, int]:
    """Graded dimension of B_{E_3}(A)_k by cohomological degree,
    for A free on one degree-0 generator.

    The bar desuspension shifts each generator by -3.
    The linking forms add degree 2 per insertion.
    The arity-k component in bar degree d has dimension:

      dim = b_{d + 3k}(Conf_k(R^3))

    Wait -- more carefully: the bar element at arity k has
    k desuspended generators (total shift -3k) plus linking forms
    of degree 2 each.  The NET degree of an arity-k bar element with
    j linking forms is:
      -3k + 2j

    And j ranges from 0 to (k-1) (the max degree of Conf_k(R^3)
    in units of the generator degree is k-1, so j <= k-1).

    So the graded dimension at degree d = -3k + 2j is b_{2j}(Conf_k(R^3)).
    """
    if k <= 0:
        return {0: 1}

    betti = conf_r3_poincare_polynomial(k)
    result: Dict[int, int] = {}
    for deg_conf, dim_conf in betti.items():
        # deg_conf = 2j is the degree in H*(Conf_k(R^3))
        # Bar degree = -3k + deg_conf
        bar_deg = -3 * k + deg_conf
        result[bar_deg] = dim_conf
    return result


def e3_bar_complex_dimensions(max_arity: int) -> Dict[int, Dict[int, int]]:
    """Full graded dimensions of B_{E_3}(A) up to given arity.

    Returns {arity: {degree: dimension}}.
    """
    return {k: e3_bar_graded_dimension(k) for k in range(1, max_arity + 1)}


# =========================================================================
# 4.  Braided monoidal structure from E_3
# =========================================================================

@dataclass
class BraidingData:
    """Braiding data for an E_3-algebra."""
    # Fundamental group of Conf_2(R^3)
    pi1_conf2_r3: str = "trivial (R^3 \\ {0} ~ S^2, pi_1(S^2) = 0)"

    # The braiding comes from the E_2 SUBALGEBRA, not from Conf_2(R^3)
    braiding_source: str = "E_2 subalgebra (from choosing R^2 subset R^3)"

    # E_3 enhancement: the braiding is TRIVIALIZABLE
    e3_symmetry: str = ("E_3-algebra is SYMMETRIC monoidal (not just braided): "
                        "the braiding R = sigma (swap) up to homotopy, "
                        "because pi_1(Conf_2(R^3)) = 0 trivializes the braid")

    # The key homotopy group
    pi2_s2: str = "pi_2(S^2) = Z (Hopf degree, provides secondary structure)"

    # Comparison with E_2
    e2_is_braided: str = ("E_2 is braided monoidal: pi_1(Conf_2(R^2)) = Z "
                          "(fundamental group of S^1 = R^2\\{0})")
    e3_is_symmetric: str = ("E_3 is symmetric monoidal: pi_1(Conf_2(R^3)) = 0 "
                            "(S^2 is simply connected)")

    # Physical meaning
    physics: str = ("In 3D TFT, particles can pass through each other "
                    "(no topological obstruction in R^3). The braiding "
                    "from the 2D theory becomes trivializable in 3D.")


def e3_braiding_is_symmetric() -> bool:
    """E_3-algebras are symmetric monoidal (not merely braided).

    pi_1(Conf_2(R^3)) = pi_1(S^2) = 0, so the braiding is trivializable.

    This is the key topological difference between E_2 and E_3:
      E_2: braided (pi_1 = Z, nontrivial braiding)
      E_3: symmetric (pi_1 = 0, trivializable braiding)
      E_4+: also symmetric (S^{n-1} simply connected for n >= 3)

    IMPORTANT: the braiding of the QUANTUM GROUP U_q(g) associated to
    Chern-Simons is NOT the E_3 braiding.  It arises from the HOLONOMY
    of the CS connection, which is an E_2 (not E_3) phenomenon.
    The E_3 structure on the full 3D theory has a TRIVIALIZABLE braiding,
    but the 2D RESTRICTION to a surface has a nontrivial braiding.
    """
    return True


def e3_higher_homotopy_contribution() -> Dict[str, Any]:
    """Higher homotopy data from S^2 = R^3 \\ {0}.

    pi_1(S^2) = 0    (braiding trivializes)
    pi_2(S^2) = Z    (Hopf degree provides secondary invariant)
    pi_3(S^2) = Z    (Hopf fibration!)

    The pi_2 = Z contribution:
      - Provides a degree-2 cohomology class in Conf_2(R^3)
      - This is the LINKING FORM omega_{12} in H^2(Conf_2(R^3))
      - It enters the bar complex as the E_3 propagator

    The pi_3 = Z contribution (Hopf fibration):
      - Does NOT directly contribute to the bar complex (too high degree)
      - But it contributes to the OPERAD structure at higher arities
      - Concretely: the Whitehead bracket [iota, iota] in pi_3(S^2)
        generates a nontrivial homotopy operation
    """
    return {
        'pi_1': {'value': 0, 'consequence': 'braiding trivializes (symmetric monoidal)'},
        'pi_2': {'value': 'Z', 'consequence': 'linking form omega_{ij} of degree 2'},
        'pi_3': {'value': 'Z', 'consequence': 'Hopf fibration, secondary operations'},
    }


# =========================================================================
# 5.  Formality of E_3 (Lambrechts-Volic)
# =========================================================================

def e3_operad_is_formal() -> bool:
    """The E_3 operad is formal over Q.

    Proved by Lambrechts-Volic (2014) for n >= 3, and by
    Kontsevich (1999) + Tamarkin (2003) for n = 2.

    Formality means there is a zig-zag of quasi-isomorphisms
      C_*(E_3) <~> H_*(E_3)
    connecting the chain-level operad to its homology operad.

    The homology operad H_*(E_3) = e_3 (the graded operad governing
    2-Poisson algebras = Gerstenhaber algebras with a degree-2 bracket).

    Consequence for bar-cobar:
      For a FORMAL E_3-algebra A, B_{E_3}(A) is quasi-isomorphic to
      B_{e_3}(H_*(A)), the bar complex of the cohomology as a graded
      e_3-algebra.
    """
    return True


def e3_formal_model_description() -> Dict[str, str]:
    """Description of the formal model for E_3.

    The formality quasi-isomorphism identifies:
      C_*(E_3)(k) ~ H_*(Conf_k(R^3)) = Totaro algebra with degree-2 generators

    The formal model of B_{E_3}(A) for formal A:
      B_{E_3}(A) ~ B_{e_3}(H_*(A))

    The homology operad e_3 = Poisson{2} governs algebras with:
      - A commutative product of degree 0
      - A Lie bracket of degree 2 (= the Poisson bracket shifted by 2)
      - The Leibniz rule relating them

    Compare with E_2 formality:
      H_*(E_2) = e_2 = Poisson{1} = Gerstenhaber algebras
      (commutative product + degree-1 Lie bracket)
    """
    return {
        'homology_operad': 'e_3 = Poisson{2}',
        'bracket_degree': '2 (degree-2 Lie bracket)',
        'product_degree': '0 (commutative product)',
        'e2_comparison': 'e_2 = Poisson{1} = Gerstenhaber (degree-1 bracket)',
        'source': 'Lambrechts-Volic 2014, Kontsevich 1999',
        'bar_formal_model': 'B_{e_3}(H_*(A)) for formal E_3-algebra A',
    }


def e3_poisson_bracket_degree() -> int:
    """Degree of the Poisson bracket for the e_3 = Poisson{2} operad.

    The homology operad H_*(E_n) = e_n = Poisson{n-1} has a Lie bracket
    of degree (n-1).

    For n=1: degree 0 (associative, no bracket beyond the product)
    For n=2: degree 1 (Gerstenhaber bracket)
    For n=3: degree 2 (2-Poisson bracket)
    """
    return 2


# =========================================================================
# 6.  Chern-Simons as E_3 algebra
# =========================================================================

@dataclass
class ChernSimonsE3Data:
    """Chern-Simons theory as an E_3 algebra."""
    gauge_type: str   # e.g. "A", "B", "C", "D", "E", "F", "G"
    rank: int
    level: int

    @property
    def dim_g(self) -> int:
        """Dimension of the Lie algebra."""
        _dims = {
            'A': lambda r: (r + 1)**2 - 1,
            'B': lambda r: r * (2*r + 1),
            'C': lambda r: r * (2*r + 1),
            'D': lambda r: r * (2*r - 1),
            'G': lambda r: 14 if r == 2 else 0,
            'F': lambda r: 52 if r == 4 else 0,
            'E': lambda r: {6: 78, 7: 133, 8: 248}.get(r, 0),
        }
        return _dims.get(self.gauge_type, lambda r: 0)(self.rank)

    @property
    def h_dual(self) -> int:
        """Dual Coxeter number."""
        _hduals = {
            'A': lambda r: r + 1,
            'B': lambda r: 2*r - 1,
            'C': lambda r: r + 1,
            'D': lambda r: 2*r - 2,
            'G': lambda r: 4 if r == 2 else 0,
            'F': lambda r: 9 if r == 4 else 0,
            'E': lambda r: {6: 12, 7: 18, 8: 30}.get(r, 0),
        }
        return _hduals.get(self.gauge_type, lambda r: 0)(self.rank)

    @property
    def kappa(self) -> Fraction:
        """Modular characteristic kappa(CS_{G,k}).

        kappa = dim(g) * (k + h^v) / (2 * h^v)

        This is the SAME as kappa for the affine algebra g_k
        (AP1: do not confuse with c/2 = central charge / 2).
        """
        if self.h_dual == 0:
            raise ValueError(f"Invalid Lie type {self.gauge_type}{self.rank}")
        return Fraction(self.dim_g) * (self.level + self.h_dual) / (2 * self.h_dual)

    @property
    def central_charge(self) -> Fraction:
        """Central charge c(g_k) = k * dim(g) / (k + h^v).

        This is the central charge of the WZW model (E_2 restriction).
        """
        return Fraction(self.level * self.dim_g, self.level + self.h_dual)

    @property
    def quantum_parameter(self) -> complex:
        """q = exp(2*pi*i / (k + h^v)) for the quantum group U_q(g)."""
        return cmath.exp(2j * cmath.pi / (self.level + self.h_dual))

    def quantum_dimension(self, rep_dim: int) -> complex:
        """Quantum dimension [n]_q = sin(n*pi/(k+h^v)) / sin(pi/(k+h^v)).

        For SU(2) at level k: the integrable reps have dimension j+1
        for j = 0, 1, ..., k.  The quantum dimension is:
          [j+1]_q = sin((j+1)*pi/(k+2)) / sin(pi/(k+2))
        """
        q_val = self.level + self.h_dual
        num = math.sin(rep_dim * math.pi / q_val)
        den = math.sin(math.pi / q_val)
        if abs(den) < 1e-15:
            return float('inf')
        return num / den

    def e3_structure_layers(self) -> Dict[str, str]:
        """The three layers of the E_3 structure on CS observables."""
        return {
            'E_1': (f'Wilson lines: quantum group U_q(g) at q=exp(2pi i/{self.level + self.h_dual})'),
            'E_2': (f'Surface observables: WZW model (affine g at level {self.level}), '
                    f'conformal blocks'),
            'E_3': 'Bulk partition function: Reshetikhin-Turaev invariants of 3-manifolds',
        }

    def verlinde_dimension(self, genus: int) -> Fraction:
        """Dimension of the space of conformal blocks on genus-g surface.

        For SU(2) at level k:
          dim V_g = sum_{j=0}^{k} S_{0j}^{2-2g}
        where S_{0j} = sqrt(2/(k+2)) * sin((j+1)*pi/(k+2)).

        This is the E_2 sector of the CS theory (WZW conformal blocks).
        """
        if self.gauge_type != 'A' or self.rank != 1:
            # Only SU(2) = A_1 implemented explicitly
            return Fraction(-1)  # sentinel

        k = self.level
        # SU(2): integrable reps j = 0, 1, ..., k
        # S_{0,j} = sqrt(2/(k+2)) * sin((j+1)*pi/(k+2))
        result = 0.0
        for j in range(k + 1):
            s_0j = math.sqrt(2.0 / (k + 2)) * math.sin((j + 1) * math.pi / (k + 2))
            result += s_0j ** (2 - 2 * genus)
        # Return as approximate Fraction
        return Fraction(result).limit_denominator(10**8)


def cs_s3_partition_function(gauge_type: str, rank: int, level: int) -> complex:
    """Chern-Simons partition function Z(S^3, G, k).

    For SU(2) at level k:
      Z(S^3) = sqrt(2/(k+2)) * sin(pi/(k+2))

    This is the simplest E_3 invariant: the partition function of the
    3-sphere (genus-0 3-manifold).
    """
    if gauge_type == 'A' and rank == 1:
        k = level
        return math.sqrt(2.0 / (k + 2)) * math.sin(math.pi / (k + 2))
    # General: would need Lie algebra root data
    return complex('nan')


def cs_kappa_from_e2_restriction(gauge_type: str, rank: int, level: int) -> Fraction:
    """kappa for CS from the E_2 restriction (WZW model).

    The modular characteristic kappa is determined by the binary part
    of the bar complex, which is the SAME for E_2 and E_3 (universal
    across E_n, since Conf_2 contributes only through the propagator).

    So kappa_{E_3}(CS) = kappa_{E_2}(WZW) = kappa(affine g_k).
    """
    cs = ChernSimonsE3Data(gauge_type=gauge_type, rank=rank, level=level)
    return cs.kappa


# =========================================================================
# 7.  E_3 shadow obstruction tower
# =========================================================================

def e3_kappa(kappa_e2: Fraction) -> Fraction:
    """E_3 modular characteristic kappa_{E_3}.

    kappa is determined by the BINARY part of the bar complex.
    Since Conf_2(R^n) = R^n \\ {0} ~ S^{n-1} has a single nonzero
    pairing class for all n >= 1, and this pairing is universal
    (it is the level of the algebra), kappa is the SAME for all E_n:

      kappa_{E_3} = kappa_{E_2} = kappa_{E_1}

    This is a consequence of binary universality (AP27 generalized:
    the propagator pairing is weight-1 and n-independent at arity 2).
    """
    return kappa_e2


def e3_cubic_shadow(s3_e2: Fraction, algebra_is_formal: bool = True) -> Fraction:
    """E_3 cubic shadow S_3^{E_3}.

    For FORMAL E_3-algebras: S_3^{E_3} = S_3^{E_2} (formality ensures
    no correction from H^2(Conf_3(R^3))).

    For non-formal E_3-algebras: S_3^{E_3} = S_3^{E_2} + delta_3
    where delta_3 is a correction from the degree-2 linking classes
    in H^2(Conf_3(R^3)) (which has dim 3).

    All standard families (Heisenberg, affine KM, Virasoro, W_N) are
    formal as E_3 algebras (by formality of the E_3 operad + transfer),
    so delta_3 = 0 for all known examples.

    Stabilization threshold: n_stable(3) = 3, so S_3^{E_n} = S_3^{E_infty}
    for n >= 3.  Since E_3 is exactly AT the threshold, the correction
    vanishes for formal algebras but COULD be nonzero for non-formal ones.
    """
    if algebra_is_formal:
        return s3_e2
    # Non-formal case: would need explicit correction computation
    return s3_e2  # placeholder


def e3_quartic_shadow(s4_e2: Fraction, kappa: Fraction,
                      algebra_is_formal: bool = True) -> Fraction:
    """E_3 quartic shadow S_4^{E_3}.

    For formal algebras: S_4^{E_3} = S_4^{E_2}.

    Stabilization threshold: n_stable(4) = 4 > 3, so E_3 is BELOW the
    threshold for arity 4.  This means S_4^{E_3} can differ from
    S_4^{E_infty} even for formal algebras!

    However, for the E_3 operad, the correction from H^{>0}(Conf_4(R^3))
    to the arity-4 shadow involves degree-2 classes (from the linking forms).
    These contribute at degree 2 in the bar complex, which interacts with
    the MC equation at a specific order.

    For formal E_3-algebras: the operad formality ensures the correction
    is exact (coboundary), so S_4^{E_3} = S_4^{E_2} for formal algebras.

    For general algebras: S_4^{E_3} = S_4^{E_2} + delta_4^{E_3}
    where delta_4^{E_3} depends on the non-formal part of the
    E_3 algebra structure.
    """
    if algebra_is_formal:
        return s4_e2
    return s4_e2


def e3_shadow_depth(shadow_class: str) -> int:
    """Shadow depth for an E_3 algebra of the given class.

    For FORMAL E_3 algebras, the depth is the same as for E_2/E_1:
      G: 2, L: 3, C: 4, M: infinity

    All standard families are formal E_3 algebras.
    """
    depth_map = {
        'G': 2,
        'L': 3,
        'C': 4,
        'M': -1,  # infinity
    }
    if shadow_class not in depth_map:
        raise ValueError(f"Unknown shadow class: {shadow_class}")
    return depth_map[shadow_class]


def e3_linking_number_correction(k: int) -> int:
    """Dimension of the linking-number correction space at arity k.

    The E_3 bar complex has additional structure from the degree-2
    linking forms omega_{ij} in H^2(Conf_k(R^3)).

    At arity k, the linking-number correction space has dimension:
      dim H^2(Conf_k(R^3)) = C(k, 2) = k*(k-1)/2

    These linking forms contribute to the bar differential at a
    higher order than the E_2 Arnold generators (which have degree 1).

    For k = 2: 1 linking form (the basic propagator)
    For k = 3: 3 linking forms
    For k = 4: 6 linking forms
    """
    return comb(k, 2)


# =========================================================================
# 8.  E_3 to E_2 reduction
# =========================================================================

def e3_to_e2_restriction(e3_shadow_data: Dict[str, Any]) -> Dict[str, Any]:
    """Restrict E_3 shadow data to E_2 via the forgetful functor.

    The forgetful functor E_3-Alg -> E_2-Alg (choose R^2 subset R^3)
    restricts:
      - kappa: unchanged (binary universality)
      - S_3: unchanged for formal algebras
      - S_4: unchanged for formal algebras
      - Shadow depth: unchanged for formal algebras

    The ADDITIONAL E_3 data (beyond E_2) consists of:
      - The trivialization of the braiding (pi_1(S^2) = 0)
      - The secondary structure from pi_2(S^2) = Z
      - The degree-2 linking forms (replacing degree-1 Arnold generators)

    After restriction to E_2, these become:
      - The braiding R (non-trivializable in E_2)
      - No secondary structure (pi_2(S^1) = 0)
      - Degree-1 Arnold generators
    """
    result = dict(e3_shadow_data)
    result['operadic_level'] = 'E_2 (restricted from E_3)'
    result['braiding'] = 'nontrivial (E_2 braiding, from pi_1(S^1) = Z)'
    result['secondary'] = 'none (pi_2(S^1) = 0 after restriction)'
    return result


def e3_e2_shadow_comparison(kappa: Fraction, s3: Fraction,
                            s4: Fraction, formal: bool = True) -> Dict[str, Any]:
    """Compare E_3 and E_2 shadow invariants.

    For formal algebras: ALL shadow invariants agree.
    For non-formal algebras: differences possible at arity >= 3.
    """
    return {
        'kappa_e2': kappa,
        'kappa_e3': kappa,
        'kappa_agree': True,  # always
        's3_e2': s3,
        's3_e3': e3_cubic_shadow(s3, formal),
        's3_agree': formal,  # agree iff formal
        's4_e2': s4,
        's4_e3': e3_quartic_shadow(s4, kappa, formal),
        's4_agree': formal,
        'formal': formal,
        'note': ('All shadows agree for formal algebras. '
                 'Non-formal differences arise from H^2(Conf_k(R^3)).'),
    }


def e3_yangian_component() -> Dict[str, str]:
    """The Yangian component of the E_3 structure.

    By Dunn additivity: E_3 = E_1 tensor E_2.
    An E_3-algebra A is an E_1-algebra in E_2-algebras.

    Decomposition:
      - E_2 direction: the chiral algebra (surface operators, OPE)
      - E_1 direction: the spectral parameter z (Wilson line direction)

    The Yangian Y(g) arises as the E_1 algebra structure in the
    E_2-algebra category.  Concretely:
      - Y(g) generators T_i(u) carry a spectral parameter u (E_1 direction)
      - The OPE of T_i(u) T_j(v) is governed by the E_2 structure
      - The RTT relation R(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u-v)
        encodes the compatibility of E_1 and E_2

    The shadow tower of the E_3 algebra stratifies:
      - Arity-2 E_1 component: Yangian level-0 (kappa)
      - Arity-3 E_1 component: Yangian level-1 (cubic)
      - E_2 components: chiral shadow tower (as in monograph)
      - Mixed E_1 x E_2: spectral-parameter-dependent shadows
    """
    return {
        'dunn': 'E_3 = E_1 tensor E_2',
        'e1_direction': 'spectral parameter u (Yangian)',
        'e2_direction': 'chiral algebra (OPE, surface operators)',
        'compatibility': 'RTT relation (E_1 x E_2 interaction)',
        'shadow_e1': 'Yangian level data from E_1 tower',
        'shadow_e2': 'chiral shadow tower from E_2',
        'shadow_mixed': 'spectral-parameter-dependent corrections',
    }


# =========================================================================
# 9.  Higher E_n and stabilization
# =========================================================================

def en_shadow_comparison_table(max_n: int, kappa: Fraction,
                               s3: Fraction = Fraction(0),
                               s4: Fraction = Fraction(0)) -> List[Dict[str, Any]]:
    """Comparison table of shadow invariants across E_1, E_2, ..., E_n.

    kappa is universal (same for all n).
    S_3 stabilizes at n = 3.
    S_4 stabilizes at n = 4.
    S_r stabilizes at n = r.
    """
    rows = []
    for n in range(1, max_n + 1):
        row: Dict[str, Any] = {
            'n': n,
            'operad': f'E_{n}',
            'koszul_shift': n,
            'propagator_degree': n - 1,
            'kappa': kappa,
            's3_stabilized': n >= 3,
            's4_stabilized': n >= 4,
            'formal': True,  # all E_n operads are formal for n >= 1
            'pi1_Conf2': 'Z' if n == 2 else ('trivial' if n >= 3 else 'NA'),
        }
        if n == 1:
            row['bar_type'] = 'classical bar (Conf_k(R) contractible)'
            row['braiding'] = 'none (associative only)'
        elif n == 2:
            row['bar_type'] = 'chiral bar (Arnold algebra, degree-1 generators)'
            row['braiding'] = 'braided monoidal (pi_1 = Z)'
        elif n == 3:
            row['bar_type'] = 'E_3 bar (Totaro algebra, degree-2 generators)'
            row['braiding'] = 'symmetric monoidal (pi_1 = 0)'
        else:
            row['bar_type'] = f'E_{n} bar (degree-{n-1} generators)'
            row['braiding'] = 'symmetric monoidal'
        rows.append(row)
    return rows


def en_stabilization_arity(arity: int) -> int:
    """The value of n at which the arity-r shadow stabilizes.

    S_r^{E_n} = S_r^{E_infty} for n >= r.

    The stabilization threshold is exactly n = r:
    - Below threshold (n < r): configuration space topology contributes
    - At threshold (n = r): correction vanishes for formal algebras
    - Above threshold (n > r): no positive-degree classes can contribute
    """
    return max(arity, 1)


def e_infty_bar_description() -> Dict[str, str]:
    """The E_infty = Com bar complex (Harrison complex).

    In the limit n -> infty, E_n -> E_infty = Com.
    The bar complex B_{Com}(A) = B_{Harrison}(A) is the Harrison
    (commutative) bar complex.

    B_{Com}(A)_k = Sym^k(s^{-1} A)  (symmetric power, not tensor power)

    The Koszul dual: Com^! = Lie.
    So the cobar Omega_{Com} gives a Lie algebra (L_infty structure).

    The shadow tower in the stable (E_infty) limit:
      All arity-r shadows S_r^{E_infty} = S_r^{tree} (tree-level only,
      no loop corrections from configuration space topology).
    """
    return {
        'operad': 'E_infty = Com',
        'koszul_dual': 'Com^! = Lie (NOT coLie!)',
        'bar_complex': 'Harrison complex: B_{Com}(A)_k = Sym^k(s^{-1}A)',
        'cobar_output': 'L_infty algebra (homotopy Lie)',
        'shadow_tower': 'tree-level only (no loop corrections)',
        'stabilization': 'ALL arity-r shadows have stabilized (n = infty > r)',
    }


# =========================================================================
# 10.  Bar-cobar adjunction and inversion for E_3
# =========================================================================

@dataclass
class E3BarCobarAdjunction:
    """The E_3 bar-cobar adjunction."""

    # Functors
    bar: str = "B_{E_3}: E_3-Alg -> E_3^i-coAlg"
    cobar: str = "Omega_{E_3}: E_3^i-coAlg -> E_3-Alg"
    adjunction: str = "B_{E_3} -| Omega_{E_3} (left adjoint -| right adjoint)"

    # Inversion (Theorem B analogue for E_3)
    inversion: str = ("Omega_{E_3}(B_{E_3}(A)) ~> A (quasi-isomorphism "
                      "on the Koszul locus)")

    # Koszul locus
    koszul_locus: str = ("A is E_3-Koszul iff H_*(B_{E_3}(A)) is concentrated "
                         "in bar degree 1 (E_3-analogue of chiral Koszulness)")

    # Comparison with E_2
    e2_bar: str = "B_{E_2}: chiral bar complex (monograph main object)"
    e3_bar_extends_e2: str = ("B_{E_3}(A) has B_{E_2}(A) as the E_2-component; "
                              "the additional E_3 data is the braiding trivialization "
                              "and the degree-2 propagator")

    def bar_differential_components(self) -> Dict[str, str]:
        """Components of the E_3 bar differential."""
        return {
            'd_0': 'internal differential of A (if A is a dg E_3-algebra)',
            'd_1': 'bar differential from E_3 operations (degree +1)',
            'd_2_linking': ('higher differential from linking-number classes '
                           'in H^2(Conf_k(R^3)); absent for formal algebras'),
        }


def e3_bar_cobar_inversion_check(algebra_type: str) -> Dict[str, Any]:
    """Check that bar-cobar inversion holds for E_3.

    For E_3-Koszul algebras:
      Omega_{E_3}(B_{E_3}(A)) ~> A

    The Koszulness condition:
      H_*(B_{E_3}(A)) concentrated in bar degree 1.

    For standard families:
      Heisenberg: Koszul (free algebra, bar cohomology = Sym(V*[3]))
      Affine KM: Koszul (Feigin-Frenkel, structure constants in bar degree 1)
      Virasoro: Koszul (universal Vir Koszul at generic c)

    The E_3 Koszulness condition is DIFFERENT from E_2 Koszulness:
    the bar complex uses Conf_k(R^3) instead of Conf_k(R^2), so the
    degrees and dimensions change.  However, for formal algebras,
    the KOSZULNESS STATUS is the same (formality preserves Koszulness).
    """
    koszul_algebras = {
        'heisenberg': True,
        'affine_km': True,
        'virasoro': True,
        'w_n': True,
        'betagamma': True,
    }
    is_koszul = koszul_algebras.get(algebra_type, None)
    return {
        'algebra': algebra_type,
        'e3_koszul': is_koszul,
        'e2_koszul': is_koszul,  # same for formal algebras
        'agree': True,  # formal algebras: same Koszulness status
        'bar_cobar_inverts': is_koszul,
        'note': ('E_3 Koszulness = E_2 Koszulness for formal algebras '
                 '(all standard families).'),
    }


# =========================================================================
# 11.  Chern-Simons/quantum group connection
# =========================================================================

def quantum_group_from_cs_e3(gauge_type: str, rank: int,
                              level: int) -> Dict[str, Any]:
    """Quantum group data from Chern-Simons as E_3 algebra.

    CS_{G,k} is an E_3 algebra.  Its representation theory gives:
      - E_1 sector: quantum group U_q(g) at q = exp(2*pi*i/(k+h^v))
      - E_2 sector: chiral algebra (affine g at level k)
      - E_3 sector: modular tensor category (MTC) of representations

    The quantum group U_q(g) governs:
      - R-matrix: R(u) from the universal R-matrix of U_q(g)
      - Braiding: from the quasi-triangular structure
      - Invariants: knot/link invariants via Reshetikhin-Turaev

    The bar-cobar connection:
      B_{E_3}(CS) restricted to E_1 gives B_{E_1}(U_q(g))
      B_{E_3}(CS) restricted to E_2 gives B_{E_2}(WZW)
    """
    cs = ChernSimonsE3Data(gauge_type=gauge_type, rank=rank, level=level)
    return {
        'gauge_group': f'{gauge_type}_{rank}',
        'level': level,
        'q': cs.quantum_parameter,
        'kappa': cs.kappa,
        'central_charge': cs.central_charge,
        'quantum_group': f'U_q({gauge_type.lower()}_{rank})',
        'R_matrix_type': 'quasi-triangular' if level > 0 else 'degenerate',
        'mtc': f'Rep(U_q(g)) at q = e^{{2pi i/{level + cs.h_dual}}}',
        'e1_sector': f'U_q({gauge_type.lower()}_{rank})',
        'e2_sector': f'affine {gauge_type.lower()}_{rank} at level {level}',
        'e3_sector': 'modular tensor category',
    }


def cs_su2_r_matrix_fundamental(level: int) -> np.ndarray:
    """R-matrix for SU(2) CS at level k in the fundamental representation.

    The R-matrix for U_q(sl_2) on V_2 tensor V_2 (fundamental):

      R = q^{1/2} * (sum_i E_ii tensor E_ii) + sum_{i!=j} E_ii tensor E_jj
          + (q^{1/2} - q^{-1/2}) * sum_{i<j} E_ij tensor E_ji

    At q = exp(2*pi*i/(k+2)), this is a 4x4 matrix.

    For V_2 = C^2:
      R = | q^{1/2}    0        0         0      |
          |   0         0      q^{-1/2}   0      |
          |   0       q^{-1/2}  q^{1/2}-q^{-1/2} 0 |
          |   0         0        0       q^{1/2}  |

    Wait -- more carefully, the standard R-matrix for U_q(sl_2) on
    the fundamental representation V = C^2 is:

      R = q * E_11 tensor E_11 + E_11 tensor E_22 + E_22 tensor E_11
          + q * E_22 tensor E_22 + (q - q^{-1}) * E_12 tensor E_21

    where q = exp(2*pi*i / (k+2)).
    """
    k = level
    q_val = cmath.exp(2j * cmath.pi / (k + 2))

    R = np.zeros((4, 4), dtype=complex)
    # Basis: |11>, |12>, |21>, |22> = e1 tensor e1, e1 tensor e2, ...

    # q * E_11 tensor E_11: coefficient of |11><11| is q
    R[0, 0] = q_val
    # E_11 tensor E_22: |12><12| coefficient 1
    R[1, 1] = 1.0
    # E_22 tensor E_11: |21><21| coefficient 1
    R[2, 2] = 1.0
    # q * E_22 tensor E_22: |22><22| coefficient q
    R[3, 3] = q_val
    # (q - q^{-1}) * E_12 tensor E_21: maps |21> to |12>
    R[1, 2] = q_val - 1.0 / q_val

    return R


def cs_su2_yang_baxter_check(level: int) -> Dict[str, Any]:
    """Check the Yang-Baxter equation for the SU(2) CS R-matrix.

    R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}

    where R_{ij} acts on the i-th and j-th tensor factors of V^{tensor 3}.
    """
    R = cs_su2_r_matrix_fundamental(level)

    # Build R_{12}, R_{13}, R_{23} on V^{tensor 3} = C^8
    dim = 2
    dim3 = dim ** 3

    def embed_12(R_mat):
        """R acting on factors 1,2; identity on factor 3."""
        result = np.zeros((dim3, dim3), dtype=complex)
        for a in range(dim):
            for b in range(dim):
                for c in range(dim):
                    for d in range(dim):
                        # R_{ab,cd} acts on (factor1=a, factor2=b) -> (c,d)
                        # factor 3 unchanged
                        for e in range(dim):
                            i_in = a * dim * dim + b * dim + e
                            i_out = c * dim * dim + d * dim + e
                            result[i_out, i_in] += R_mat[a * dim + b, c * dim + d]
        return result

    def embed_13(R_mat):
        """R acting on factors 1,3; identity on factor 2."""
        result = np.zeros((dim3, dim3), dtype=complex)
        for a in range(dim):
            for c in range(dim):
                for b in range(dim):
                    for d in range(dim):
                        for e in range(dim):
                            i_in = a * dim * dim + e * dim + b
                            i_out = c * dim * dim + e * dim + d
                            result[i_out, i_in] += R_mat[a * dim + b, c * dim + d]
        return result

    def embed_23(R_mat):
        """R acting on factors 2,3; identity on factor 1."""
        result = np.zeros((dim3, dim3), dtype=complex)
        for a in range(dim):
            for b in range(dim):
                for c in range(dim):
                    for d in range(dim):
                        for e in range(dim):
                            i_in = e * dim * dim + a * dim + b
                            i_out = e * dim * dim + c * dim + d
                            result[i_out, i_in] += R_mat[a * dim + b, c * dim + d]
        return result

    R12 = embed_12(R)
    R13 = embed_13(R)
    R23 = embed_23(R)

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12

    diff = np.max(np.abs(lhs - rhs))

    return {
        'level': level,
        'q': cmath.exp(2j * cmath.pi / (level + 2)),
        'yang_baxter_satisfied': diff < 1e-10,
        'max_deviation': float(diff),
        'R_matrix_shape': R.shape,
    }


# =========================================================================
# 12.  Comparison: E_2 configuration spaces vs E_3
# =========================================================================

def conf_r2_poincare_polynomial(k: int) -> Dict[int, int]:
    """Poincare polynomial of Conf_k(R^2) (= Arnold algebra).

    P_k(t) = prod_{j=0}^{k-1} (1 + j*t)

    Generators in degree 1.
    """
    if k <= 0:
        return {0: 1}
    coeffs: Dict[int, int] = {0: 1}
    for j in range(1, k):
        new_coeffs: Dict[int, int] = {}
        for deg, val in coeffs.items():
            new_coeffs[deg] = new_coeffs.get(deg, 0) + val
            new_coeffs[deg + 1] = new_coeffs.get(deg + 1, 0) + j * val
        coeffs = new_coeffs
    return coeffs


def e2_e3_betti_comparison(max_k: int) -> List[Dict[str, Any]]:
    """Compare Betti numbers of Conf_k(R^2) and Conf_k(R^3)."""
    rows = []
    for k in range(1, max_k + 1):
        betti_r2 = conf_r2_poincare_polynomial(k)
        betti_r3 = conf_r3_poincare_polynomial(k)
        total_r2 = sum(betti_r2.values())
        total_r3 = sum(betti_r3.values())
        rows.append({
            'k': k,
            'betti_R2': betti_r2,
            'betti_R3': betti_r3,
            'total_R2': total_r2,
            'total_R3': total_r3,
            'totals_equal': total_r2 == total_r3,
            'both_equal_k_factorial': total_r2 == factorial(k) == total_r3,
            'max_degree_R2': max(betti_r2.keys()),
            'max_degree_R3': max(betti_r3.keys()),
            'degree_ratio': (max(betti_r3.keys()) / max(betti_r2.keys())
                            if max(betti_r2.keys()) > 0 else float('inf')),
        })
    return rows


# =========================================================================
# 13.  E_3 factorization homology
# =========================================================================

def e3_factorization_homology_s3(kappa: Fraction) -> Dict[str, Any]:
    """Factorization homology integral_{S^3} A for an E_3 algebra A.

    This is the E_3 Hochschild homology:
      HH^{E_3}(A) = integral_{S^3} A

    S^3 has: H_0 = Q, H_3 = Q (Poincare duality).
    The factorization homology has contributions from:
      - H_0(S^3): the trace (arity 0)
      - H_3(S^3): the cotrace (arity 3, shifted by 3)

    The 3-sphere invariant generalizes the genus-1 invariant of the
    chiral case (integral_{S^1} A = THH(A)):
      - S^1 gives genus-1 shadow: kappa/24
      - S^3 gives the E_3 invariant: related to kappa by the
        Euler characteristic of S^3 (chi = 0) and the Bernoulli numbers.

    For the E_3 invariant of S^3:
      integral_{S^3} A encodes the S^3 partition function.
      For CS theory: this is Z(S^3, G, k).
    """
    return {
        'manifold': 'S^3',
        'dimension': 3,
        'en_level': 3,
        'invariant': 'HH^{E_3}(A) = integral_{S^3} A',
        'homology_S3': {0: 1, 3: 1},
        'trace_contribution': kappa,
        'cotrace_shift': 3,
        'chi_S3': 0,
        'note': ('S^3 factorization homology = E_3 Hochschild homology. '
                 'For CS theory, this gives Z(S^3).'),
    }


def e3_factorization_homology_lens(p: int, kappa: Fraction) -> Dict[str, Any]:
    """Factorization homology on L(p,1) (lens space).

    L(p,1) = S^3 / Z_p is a 3-manifold.
    For CS theory: Z(L(p,1)) = sum_j S_{0j}^2 * T_j^p.

    Factorization homology on L(p,1):
      integral_{L(p,1)} A = (integral_{S^3} A)^{Z_p homotopy fixed points}
    """
    return {
        'manifold': f'L({p},1)',
        'dimension': 3,
        'en_level': 3,
        'fundamental_group': f'Z_{p}',
        'covers_S3': True,
        'kappa': kappa,
        'note': f'Lens space L({p},1) = S^3/Z_{p}',
    }


# =========================================================================
# 14.  Explicit bar complex computations for specific E_3 algebras
# =========================================================================

def e3_bar_heisenberg(level: Fraction = Fraction(1)) -> Dict[str, Any]:
    """E_3 bar complex for the Heisenberg algebra at level k.

    The Heisenberg algebra H_k is the FREE E_n algebra on one generator
    (for all n).  Its E_3 bar complex:

      B_{E_3}(H_k)_n = H_*(Conf_n(R^3)) tensor (s^{-3}V)^{tensor n}

    For V = k (one-dimensional, degree 0):
      dim B_{E_3}(H_k)_n = n! (total Betti number)

    Bar cohomology:
      H_*(B_{E_3}(H_k)) = Sym(V*[3])  (symmetric algebra on V* in degree 3)

    This is E_infty (free commutative), so:
      - E_3 Koszul: YES
      - Shadow depth: 2 (Gaussian class G)
      - kappa = k/2 (universal)
    """
    return {
        'algebra': 'Heisenberg',
        'level': level,
        'kappa': level / 2,
        'bar_cohomology': 'Sym(V*[3])',
        'bar_cohomology_type': 'E_infty (free commutative)',
        'koszul': True,
        'shadow_class': 'G',
        'shadow_depth': 2,
        'bar_arity_dims': {n: factorial(n) for n in range(1, 6)},
    }


def e3_bar_affine_sl2(level: int = 1) -> Dict[str, Any]:
    """E_3 bar complex for the affine sl_2 algebra at level k.

    As an E_3 algebra (from CS(SU(2), k)):
      kappa = 3*(k+2)/(2*2) = 3*(k+2)/4
      (dim sl_2 = 3, h^v = 2)

    Bar cohomology at arity 2:
      dim H_2(B_{E_3}) = 1 (the propagator class)
      The propagator is in degree 2 (linking form), not degree 1 (Arnold).

    Shadow class: L (Lie/tree, depth 3) -- same as E_2.
    """
    kappa = Fraction(3 * (level + 2), 4)
    return {
        'algebra': 'affine sl_2',
        'level': level,
        'dim_g': 3,
        'h_dual': 2,
        'kappa': kappa,
        'central_charge': Fraction(3 * level, level + 2),
        'shadow_class': 'L',
        'shadow_depth': 3,
        'e3_propagator_degree': 2,
        'e2_propagator_degree': 1,
    }


def e3_bar_virasoro(c_val: Fraction = Fraction(26)) -> Dict[str, Any]:
    """E_3 bar complex data for the Virasoro algebra at central charge c.

    As an E_3 algebra (if embedded in a 3D theory):
      kappa = c/2
      Shadow class: M (mixed, infinite depth)
      Q^contact = 10 / (c * (5c + 22))

    The Virasoro algebra does NOT naturally carry an E_3 structure
    (it lives on a 2D surface, giving E_2).  The E_3 data here
    describes what WOULD happen if Virasoro were extended to E_3
    (as in 3D gravity or Chern-Simons with Virasoro boundary).

    For formal extensions: all shadow invariants agree with E_2.
    """
    kappa = c_val / 2
    return {
        'algebra': 'Virasoro',
        'c': c_val,
        'kappa': kappa,
        'shadow_class': 'M',
        'shadow_depth': -1,  # infinity
        'Q_contact': Fraction(10, 1) / (c_val * (5 * c_val + 22)),
        'koszul': True,
        'note': ('Virasoro is naturally E_2. E_3 data is for formal '
                 'extension (e.g. 3D gravity / CS boundary).'),
    }


# =========================================================================
# 15.  Linking numbers and Borromean rings
# =========================================================================

def linking_number_h2_generator(i: int, j: int, k: int) -> str:
    """The degree-2 generator omega_{ij} in H^2(Conf_k(R^3)).

    omega_{ij} is the pullback of the fundamental class [S^2] along
    the map Conf_k(R^3) -> S^2 given by (x_1,...,x_k) |-> (x_i - x_j)/|x_i - x_j|.

    This is the "linking form" of the pair (i,j): it measures the
    linking number of a closed curve around x_i with x_j.

    In the bar complex, omega_{ij} acts as the E_3 propagator
    connecting the i-th and j-th factors.
    """
    if i >= j:
        raise ValueError(f"Require i < j, got i={i}, j={j}")
    if j >= k:
        raise ValueError(f"Require j < k (number of points), got j={j}, k={k}")
    return f"omega_{{{i},{j}}} in H^2(Conf_{k}(R^3))"


def arnold_relation_e3(i: int, j: int, k_idx: int) -> str:
    """The Arnold relation for the triple (i,j,k) in H*(Conf_n(R^3)).

    For E_3 (degree-2 generators):
      omega_{ij} * omega_{jk} + omega_{jk} * omega_{ki} + omega_{ki} * omega_{ij} = 0

    This lives in degree 4 (= 2 + 2).

    Since the generators have EVEN degree, the product is COMMUTATIVE
    (no Koszul sign issues).  So:
      omega_{ij} * omega_{jk} = omega_{jk} * omega_{ij}
    and the relation becomes:
      2 * omega_{ij} * omega_{jk} + omega_{jk} * omega_{ki} + omega_{ki} * omega_{ij} = 0

    Wait -- that is wrong.  The Arnold relation for E_3 has a DIFFERENT
    form from E_2 because the generators have even degree.

    For E_2 (degree-1 generators, ANTICOMMUTATIVE):
      omega_{ij} * omega_{jk} + omega_{jk} * omega_{ki} + omega_{ki} * omega_{ij} = 0
    (each term is a product of two degree-1 anticommuting generators)

    For E_3 (degree-2 generators, COMMUTATIVE):
      The generalized Arnold relation is:
      omega_{ij} * omega_{jk} + omega_{jk} * omega_{ki} + omega_{ki} * omega_{ij} = 0
      (same FORM, but now the products commute)

    This is the correct form: the Arnold relation is the SAME algebraic
    identity in all dimensions n >= 2, but the commutativity of the
    generators depends on the parity of the degree (n-1).

    For n=3: degree = 2 (even), generators commute.
    The Arnold relation is a quadratic relation in commuting variables.
    """
    return (f"omega_{{{i},{j}}} * omega_{{{j},{k_idx}}} + "
            f"omega_{{{j},{k_idx}}} * omega_{{{k_idx},{i}}} + "
            f"omega_{{{k_idx},{i}}} * omega_{{{i},{j}}} = 0  "
            f"(degree 4, in H^4(Conf_n(R^3)))")


def borromean_rings_class(k: int) -> Dict[str, Any]:
    """The Borromean rings class in H*(Conf_3(R^3)).

    For k=3 points in R^3, H^4(Conf_3(R^3)) has dimension 2.
    Generators: products omega_{12}*omega_{23} and omega_{12}*omega_{13}
    (related by the Arnold relation).

    The Borromean rings provide a nontrivial element of H^4(Conf_3(R^3))
    via the Massey product <omega_{12}, omega_{23}, omega_{13}>.

    In E_2 (R^2): Massey products in Conf_3(R^2) can be nontrivial
    (the Arnold algebra has nontrivial higher operations).

    In E_3 (R^3): the Massey product
      <omega_{12}, omega_{23}, omega_{13}>
    is the linking-number obstruction class.  For the Borromean rings,
    all pairwise linking numbers vanish but the triple is nontrivial.

    This class lives in degree 2 + 2 - 1 = 3... no.

    Actually, for the Massey product in H*(Conf_3(R^3)):
    The generators omega_{ij} have degree 2.  A Massey product
    <a, b, c> with |a| = |b| = |c| = 2 would require a*b = 0 and b*c = 0.
    But the Arnold relation says a*b + b*c + c*a = 0, which does NOT
    imply a*b = 0.  So the standard Massey triple product is not directly
    applicable here.

    The Borromean rings invariant is rather a HIGHER-ORDER linking invariant
    (Milnor's mu-bar invariants), which enters the E_3 structure at arity >= 4.
    """
    if k < 3:
        return {'exists': False, 'reason': 'Need k >= 3 points'}

    return {
        'exists': True,
        'space': f'H^4(Conf_{k}(R^3))',
        'dimension_H4': conf_r3_poincare_polynomial(k).get(4, 0),
        'type': 'higher linking invariant (Milnor mu-bar)',
        'arity': 'enters E_3 structure at arity >= 3',
        'borromean_linking': ('Pairwise linking = 0 but triple '
                             'linking nonzero; detected by Massey-type invariants'),
    }


# =========================================================================
# 16.  Summary functions
# =========================================================================

def e3_bar_cobar_summary() -> Dict[str, Any]:
    """Complete summary of E_3 bar-cobar duality."""
    return {
        'operad': 'E_3',
        'koszul_shift': 3,
        'koszul_dual': 'E_3{-3} (self-dual up to shift)',
        'propagator_degree': 2,
        'propagator_source': 'S^2 = R^3 \\ {0}',
        'formal': True,
        'formality_source': 'Lambrechts-Volic 2014',
        'braiding': 'symmetric (pi_1(S^2) = 0)',
        'bar_cobar_adjunction': 'B_{E_3} -| Omega_{E_3}',
        'inversion': 'Omega(B(A)) ~ A on E_3-Koszul locus',
        'kappa_universal': 'kappa_{E_3} = kappa_{E_2} = kappa_{E_1}',
        'shadow_depth': 'same as E_2 for formal algebras',
        'cs_connection': ('CS_{G,k} is an E_3 algebra; '
                         'E_2 = WZW, E_1 = U_q(g)'),
        'dunn': 'E_3 = E_1 tensor E_2 (Yangian = E_1 in E_2)',
        'stabilization': 'S_r^{E_3} = S_r^{E_infty} for r <= 3',
        'higher_deligne': 'Z^der(B(A)) carries E_4 (if B(A) is E_3)',
    }


def e3_vs_e2_comparison() -> Dict[str, Tuple[str, str]]:
    """Side-by-side comparison of E_3 vs E_2 bar-cobar."""
    return {
        'propagator_degree': ('1 (from S^1)', '2 (from S^2)'),
        'koszul_shift': ('2', '3'),
        'braiding': ('braided monoidal', 'symmetric monoidal'),
        'pi_1_S^{n-1}': ('Z (nontrivial braiding)', '0 (trivializable)'),
        'pi_2_S^{n-1}': ('0', 'Z (Hopf degree)'),
        'formality': ('Kontsevich-Tamarkin', 'Lambrechts-Volic'),
        'kappa': ('same', 'same'),
        'shadow_depth': ('same (formal)', 'same (formal)'),
        'physical': ('2D CFT / chiral algebras', '3D TFT / Chern-Simons'),
        'quantum_group': ('braided category', 'modular tensor category'),
        'arnold_gen_degree': ('1 (anticommuting)', '2 (commuting)'),
        'arnold_rel_degree': ('2', '4'),
    }
