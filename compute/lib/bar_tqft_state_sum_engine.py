r"""3D TQFT state sums from the bar complex as a modular functor.

MATHEMATICAL FRAMEWORK
======================

The genus-1 curved bar complex of a rational chiral algebra A produces:
  1. A Zhu algebra A(V) controlling genus-1 modules
  2. A modular S-matrix and T-matrix (genus-1 SL(2,Z) action)
  3. A spherical fusion category from {S,T} via Verlinde formula
  4. A modular tensor category (MTC) when the algebra is rational

These data feed into FOUR distinct 3-manifold state-sum constructions:

  TURAEV-VIRO (TV):
      State sum on triangulated 3-manifolds using 6j-symbols of a
      spherical fusion category.  TV(M) = sum over labelings of
      product of 6j-symbols * quantum dimensions.

  RESHETIKHIN-TURAEV (RT):
      Surgery presentation of 3-manifolds using a modular tensor category.
      Link invariants from braiding morphisms; 3-manifold invariants from
      Kirby moves.  Jones polynomial = RT for sl_2 in fundamental rep.

  WITTEN-RESHETIKHIN-TURAEV (WRT):
      RT specialized to sl_2 at level k, giving Z_k(M) for 3-manifolds.
      Lens spaces L(p,q) and Seifert-fibered manifolds have closed forms.

  CRANE-YETTER-KAUFFMAN (CYK):
      State sum for premodular categories that produces |WRT|^2 when
      the input is a modular category (TV-RT relation).

  LEVIN-WEN STRING-NET:
      Lattice Hamiltonian whose ground states realize the Drinfeld center
      Z(C) of the input fusion category C.  Ground state degeneracy on
      a closed surface Sigma_g equals dim Hom(1, Z(C))^{2g}.

CONNECTION TO THE SHADOW OBSTRUCTION TOWER
==========================================

The shadow free energy F_g(A) is the genus-g amplitude of the bar complex.
For sl_2 at level k, F_g(sl_2, k) = kappa(sl_2,k) * lambda_g^FP at all
genera (uniform-weight lane, AP32, thm:multi-weight-genus-expansion).

The Witten-Reshetikhin-Turaev invariant of a genus-g handlebody H_g is
the Verlinde number Z_g(sl_2, k) = sum_j (S_{0j})^{2-2g}.

The conjectural exponential link is:
    log Z_g(sl_2, k) ~ F_g(sl_2, k) + corrections

at large level k (semiclassical limit).  This is the bar complex / TQFT
correspondence at genus g.

VERIFIED CLAIMS (from existing engines)
========================================

  - Modular S-matrix S_{jl} = sqrt(2/(k+2))*sin(pi*(j+1)*(l+1)/(k+2))
    (verlinde_shadow_algebra.sl2_S_matrix, 87 tests)
  - Verlinde fusion rules N_{ij}^m via truncated Clebsch-Gordan
  - Quantum dimensions d_j = sin((j+1)*pi/(k+2))/sin(pi/(k+2))
  - Total quantum dimension D^2 = (k+2)/(2 sin^2(pi/(k+2)))
  - Conformal weights h_j = j(j+2)/(4(k+2))
  - kappa(sl_2, k) = 3(k+2)/4 = lambda_g coefficient (uniform-weight)

CONVENTIONS
===========
  - Cohomological grading, |d| = +1
  - sl_2 representation labels j = 0, 1, ..., k (= twice the spin)
  - Quantum integers [n]_q = sin(n*pi/(k+2)) / sin(pi/(k+2))
  - 6j-symbol convention: Racah-Wigner with quantum corrections
  - WRT normalization: Z(S^3) = S_{00} = sqrt(2/(k+2))*sin(pi/(k+2))
  - TV normalization: TV(S^3) = 1/D^2
  - Crane-Yetter normalization: CYK(M) = |WRT(M)|^2 for modular C

REFERENCES
==========
  Turaev (1994), Quantum invariants of knots and 3-manifolds, de Gruyter
  Turaev-Viro (1992), Topology 31, 865-902
  Reshetikhin-Turaev (1991), Invent. Math. 103, 547-597
  Witten (1989), Comm. Math. Phys. 121, 351-399
  Crane-Yetter (1993), Topology and its Applications 51, 71-90
  Crane-Yetter-Kauffman (1997), J. Knot Theory Ramif. 6, 177-234
  Levin-Wen (2005), Phys. Rev. B 71, 045110
  Bakalov-Kirillov (2001), Lectures on tensor categories and modular functors
  Kirillov-Balsam (2010), arXiv:1004.1533 (TV = RT(Z(C)))

Cross-references in monograph:
  thm:modular-characteristic (higher_genus_modular_koszul.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  bar_cohomology_genus1_engine.py (curved bar complex, Zhu algebra)
  verlinde_shadow_algebra.py (S-matrix, fusion, Verlinde formula)
  sft_bar_comparison_engine.py (SFT master equation = MC equation)
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple

import numpy as np

from compute.lib.verlinde_shadow_algebra import (
    sl2_S_matrix,
    sl2_T_matrix,
    sl2_quantum_dimensions,
    sl2_total_quantum_dimension_sq,
    sl2_conformal_weights,
    sl2_central_charge,
    sl2_kappa,
    sl2_fusion_coefficients,
    sl2_fusion_rules_explicit,
    sl2_twist,
)


# =========================================================================
# 1. Quantum integers, factorials, and 6j-symbols
# =========================================================================

def quantum_integer(n: int, k: int) -> float:
    r"""Quantum integer [n]_q for sl_2 at level k.

    [n]_q = sin(n*pi/(k+2)) / sin(pi/(k+2))

    where q = exp(i*pi/(k+2)).  Note [n]_q -> n as k -> infinity.

    For n in {0,1,...,k+1} the quantum integer is non-negative;
    [k+2]_q = 0 (the truncation that defines the level-k category).
    """
    n_int = k + 2
    if n == 0:
        return 0.0
    return math.sin(n * math.pi / n_int) / math.sin(math.pi / n_int)


def quantum_factorial(n: int, k: int) -> float:
    r"""Quantum factorial [n]_q! = [n]_q * [n-1]_q * ... * [1]_q.

    By convention [0]_q! = 1.
    """
    if n < 0:
        raise ValueError(f"Negative argument to quantum factorial: {n}")
    result = 1.0
    for i in range(1, n + 1):
        result *= quantum_integer(i, k)
    return result


def admissible_triple(j1: int, j2: int, j3: int, k: int) -> bool:
    r"""Test whether (j1, j2, j3) form an admissible triple at sl_2 level k.

    Admissibility:
      - j1+j2+j3 even (integer total isospin)
      - |j1-j2| <= j3 <= j1+j2 (triangle inequalities)
      - j1+j2+j3 <= 2k  (level truncation: j1+j2-j3, j2+j3-j1, j1+j3-j2 in [0,k])
      - all j_i in {0,1,...,k}

    Here j is twice the spin: j=0 vacuum, j=k highest integrable.
    """
    if not (0 <= j1 <= k and 0 <= j2 <= k and 0 <= j3 <= k):
        return False
    if (j1 + j2 + j3) % 2 != 0:
        return False
    if not (abs(j1 - j2) <= j3 <= j1 + j2):
        return False
    if j1 + j2 + j3 > 2 * k:
        return False
    return True


def quantum_theta(j1: int, j2: int, j3: int, k: int) -> float:
    r"""Quantum theta-net theta(j1,j2,j3) for an admissible triple.

    The theta-symbol is the value of the trivalent vertex graph (theta net)
    in the Kauffman-Lins normalization for sl_2 at level k.

    theta(j1,j2,j3) = (-1)^((j1+j2+j3)/2) * [(a+b+c+1)]! * [a]! * [b]! * [c]!
                       / ([a+b]! * [b+c]! * [a+c]!)

    where a = (j2+j3-j1)/2, b = (j1+j3-j2)/2, c = (j1+j2-j3)/2 are the
    half-perimeter parameters (each non-negative integer for an admissible triple).

    Returns 0 for non-admissible triples.
    """
    if not admissible_triple(j1, j2, j3, k):
        return 0.0
    a = (j2 + j3 - j1) // 2
    b = (j1 + j3 - j2) // 2
    c = (j1 + j2 - j3) // 2
    n = a + b + c
    sign = (-1) ** n
    num = quantum_factorial(n + 1, k) * quantum_factorial(a, k) * quantum_factorial(b, k) * quantum_factorial(c, k)
    denom = quantum_factorial(a + b, k) * quantum_factorial(b + c, k) * quantum_factorial(a + c, k)
    if denom == 0:
        return 0.0
    return sign * num / denom


def quantum_6j_symbol(j1: int, j2: int, j3: int, j4: int, j5: int, j6: int, k: int) -> float:
    r"""Quantum 6j-symbol {j1,j2,j3; j4,j5,j6}_q for sl_2 at level k.

    Computed via the Racah formula for the Kauffman-Lins normalization.
    The 6j-symbol is non-zero only when each of the four triples
    (j1,j2,j3), (j1,j5,j6), (j4,j2,j6), (j4,j5,j3) is admissible.

    Convention: real-valued ribbon 6j-symbol.  At classical limit k -> infinity
    these reduce (up to sign convention) to the classical Racah 6j-symbols.

    Returns 0 if any of the four triples is non-admissible.
    """
    triples = [
        (j1, j2, j3),
        (j1, j5, j6),
        (j4, j2, j6),
        (j4, j5, j3),
    ]
    for tr in triples:
        if not admissible_triple(*tr, k):
            return 0.0

    # Half-integer parameters from Racah formula
    a1 = (j1 + j2 + j3) // 2
    a2 = (j1 + j5 + j6) // 2
    a3 = (j4 + j2 + j6) // 2
    a4 = (j4 + j5 + j3) // 2
    b1 = (j1 + j2 + j4 + j5) // 2
    b2 = (j2 + j3 + j5 + j6) // 2
    b3 = (j1 + j3 + j4 + j6) // 2

    z_min = max(a1, a2, a3, a4)
    z_max = min(b1, b2, b3)
    if z_min > z_max:
        return 0.0

    # Triangle coefficient Delta(a,b,c)
    def Delta(x: int, y: int, z: int) -> float:
        if not admissible_triple(x, y, z, k):
            return 0.0
        s1 = (x + y - z) // 2
        s2 = (x - y + z) // 2
        s3 = (-x + y + z) // 2
        s4 = (x + y + z) // 2 + 1
        num = quantum_factorial(s1, k) * quantum_factorial(s2, k) * quantum_factorial(s3, k)
        if quantum_factorial(s4, k) == 0:
            return 0.0
        return num / quantum_factorial(s4, k)

    delta_prod = (
        Delta(j1, j2, j3) * Delta(j1, j5, j6) * Delta(j4, j2, j6) * Delta(j4, j5, j3)
    )
    if delta_prod == 0.0:
        return 0.0
    sqrt_delta = math.sqrt(abs(delta_prod))
    sign_delta = 1.0 if delta_prod >= 0 else -1.0

    # Racah sum
    total = 0.0
    for z in range(z_min, z_max + 1):
        term_sign = (-1) ** z
        num = quantum_factorial(z + 1, k)
        denom = (
            quantum_factorial(z - a1, k)
            * quantum_factorial(z - a2, k)
            * quantum_factorial(z - a3, k)
            * quantum_factorial(z - a4, k)
            * quantum_factorial(b1 - z, k)
            * quantum_factorial(b2 - z, k)
            * quantum_factorial(b3 - z, k)
        )
        if denom == 0:
            continue
        total += term_sign * num / denom
    return sign_delta * sqrt_delta * total


# =========================================================================
# 2. Turaev-Viro state sum on simple triangulations
# =========================================================================

def turaev_viro_S3(k: int) -> float:
    r"""Turaev-Viro invariant of S^3 from sl_2 at level k.

    The standard normalization gives TV(S^3) = 1/D^2 where
    D^2 = sum_j d_j^2 is the total quantum dimension squared.

    This is independent of the triangulation by Turaev-Viro's theorem.
    The single-tetrahedron triangulation of S^3 (boundary-glued 3-simplex)
    yields the closed-form result.
    """
    return 1.0 / sl2_total_quantum_dimension_sq(k)


def turaev_viro_S2_x_S1(k: int) -> float:
    r"""Turaev-Viro invariant of S^2 x S^1 at level k.

    By the general TV formula, TV(Sigma x S^1) = dim Z(Sigma) where
    Z(Sigma) is the Hilbert space attached to Sigma.  For Sigma = S^2,
    Z(S^2) is one-dimensional, so TV(S^2 x S^1) counts the number of
    simple objects in the modular category.

    For sl_2 at level k there are k+1 integrable representations, hence
    TV(S^2 x S^1) = k + 1.
    """
    return float(k + 1)


def turaev_viro_T3(k: int) -> float:
    r"""Turaev-Viro invariant of the 3-torus T^3 at level k.

    T^3 = T^2 x S^1.  By the general TV formula, TV(Sigma_g x S^1) =
    dim Z(Sigma_g), and for the torus Sigma_1 = T^2 the Hilbert space
    has dimension equal to the number of simple objects (= k+1 for sl_2).

    Hence TV(T^3) = k + 1.
    """
    return float(k + 1)


def turaev_viro_lens_space(p: int, q: int, k: int) -> float:
    r"""Turaev-Viro invariant of the lens space L(p,q) for sl_2 at level k.

    L(p,q) admits the surgery presentation as p/q surgery on the unknot.
    By the Kirillov-Balsam theorem TV(M) = |WRT(M)|^2 for an MTC,
    so TV(L(p,q),k) = |WRT(L(p,q),k)|^2.

    We compute via the surgery / WRT formula and square the modulus.
    """
    val = wrt_lens_space(p, q, k)
    return float(abs(val) ** 2)


# =========================================================================
# 3. Reshetikhin-Turaev / WRT invariants
# =========================================================================

def wrt_S3(k: int) -> float:
    r"""WRT invariant of S^3 for sl_2 at level k.

    Z(S^3) = S_{00} = sqrt(2/(k+2)) * sin(pi/(k+2)).

    This is the standard normalization in which Z(S^2 x S^1) = 1.
    """
    return float(math.sqrt(2.0 / (k + 2)) * math.sin(math.pi / (k + 2)))


def wrt_S2_x_S1(k: int) -> float:
    r"""WRT invariant of S^2 x S^1 for sl_2 at level k.

    Z(S^2 x S^1) = 1 in the standard normalization (Z(S^3) = S_{00}).
    This is the trace of the identity on the unique state of S^2.
    """
    return 1.0


def wrt_T3(k: int) -> int:
    r"""WRT invariant of T^3 = T^2 x S^1 for sl_2 at level k.

    Z(T^3) = dim Z(T^2) = number of simple objects = k+1.
    """
    return k + 1


def wrt_lens_space(p: int, q: int, k: int) -> complex:
    r"""WRT invariant of the lens space L(p,q) for sl_2 at level k.

    L(p,q) is obtained by p/q surgery on the unknot.  The general formula
    (Jeffrey 1992; Lawrence-Rozansky 1999) for L(p,q) at sl_2 level k is

        Z_k(L(p,q)) = (S * T^{a_1} * S * T^{a_2} * ... * S)_{00}

    where (a_1, a_2, ...) is the negative continued fraction expansion of p/q.

    For L(p,1) (the simplest case) this reduces to:
        Z_k(L(p,1)) = (S T^p S)_{00} = sum_j S_{0j} * T_{jj}^p * S_{j0}

    We implement the L(p,1) case directly.  For general (p,q) one needs
    the continued fraction expansion of p/q -- we provide a wrapper.
    """
    if q == 1:
        S = sl2_S_matrix(k)
        T = sl2_T_matrix(k)
        T_p = np.diag(np.diag(T) ** p)
        result = (S @ T_p @ S)[0, 0]
        return complex(result)
    # General case: build M = S T^{a_1} S T^{a_2} S ... from negative
    # continued fraction p/q = a_1 - 1/(a_2 - 1/(...))
    coefs = _negative_continued_fraction(p, q)
    S = sl2_S_matrix(k)
    T_diag = np.diag(sl2_T_matrix(k))
    M = S.astype(complex)
    for a in coefs:
        T_a = np.diag(T_diag ** a)
        M = M @ T_a @ S
    return complex(M[0, 0])


def _negative_continued_fraction(p: int, q: int) -> List[int]:
    r"""Negative continued fraction expansion p/q = a_1 - 1/(a_2 - 1/(...))."""
    coefs: List[int] = []
    a, b = p, q
    while b != 0:
        c = -(-a // b)  # ceiling division
        coefs.append(c)
        a, b = b, c * b - a
    return coefs


def wrt_seifert_fibered(genus: int, p_q_pairs: List[Tuple[int, int]], k: int) -> complex:
    r"""WRT invariant of a Seifert-fibered manifold (Lawrence-Rozansky formula).

    A Seifert-fibered 3-manifold is parametrized by a base orbifold of
    genus g and exceptional fibers (p_i, q_i).  The Lawrence-Rozansky
    formula expresses Z_k(M) as a sum over integrable highest weights:

        Z_k(M) = sum_j S_{0j}^{2-2g} * prod_i ((S * T^{a_i} * S)_{0j})^{...}

    Here we implement the simplest case: SFM with no exceptional fibers,
    which reduces to genus-g handlebody.  For exceptional fibers, the
    formula is more involved -- we provide a stub that raises for unsupported.

    For the no-fiber case (Sigma_g x S^1):
        Z_k(Sigma_g x S^1) = sum_j (S_{0j})^{2-2g}
    """
    if not p_q_pairs:
        # Sigma_g x S^1
        S = sl2_S_matrix(k)
        s00_powers = S[0, :] ** (2 - 2 * genus)
        return complex(np.sum(s00_powers))
    raise NotImplementedError(
        "Seifert-fibered with exceptional fibers requires Lawrence-Rozansky residue formula"
    )


# =========================================================================
# 4. Link invariants: Jones polynomial and HOMFLY
# =========================================================================

def jones_polynomial_unknot(k: int) -> float:
    r"""Jones polynomial of the unknot at level k.

    The unnormalized RT invariant of the unknot in the fundamental
    representation V_1 of sl_2 is the quantum dimension d_1 = [2]_q.

    Normalizing so that V(unknot) = 1 (the standard Jones convention)
    requires dividing by d_1 -- we return the unnormalized value.
    """
    return quantum_integer(2, k)


def jones_polynomial_hopf(k: int) -> complex:
    r"""Jones polynomial of the Hopf link at level k.

    The Hopf link is the (2,2) torus link.  Its unnormalized RT invariant
    in the fundamental representation is

        <Hopf>_{1,1} = S_{1,1} / S_{0,0}

    (the modular S-matrix entry, since the Hopf link evaluates to S).
    """
    S = sl2_S_matrix(k)
    return complex(S[1, 1] / S[0, 0])


def jones_polynomial_trefoil(k: int) -> complex:
    r"""Jones polynomial of the trefoil at level k.

    The trefoil is the (2,3) torus knot.  Its unnormalized RT invariant
    in the fundamental rep is the trace of the braid R^3 in the
    two-strand fundamental representation:

        <trefoil>_{1} = sum_m (S_{1,m}/S_{0,m}) * theta_m^3

    Here theta_m = exp(2*pi*i*h_m) is the twist.  This is exactly
    sl2_RT_trefoil from the Verlinde engine.
    """
    S = sl2_S_matrix(k)
    h = sl2_conformal_weights(k)
    theta = np.exp(2.0j * math.pi * h)
    j = 1
    result = 0.0j
    for m in range(k + 1):
        if abs(S[0, m]) > 1e-15:
            result += (S[j, m] / S[0, m]) * theta[m] ** 3
    return complex(result)


def jones_classical_value(knot: str, q: complex) -> complex:
    r"""Classical Jones polynomial value at given q for benchmark knots.

    Reference values (from the standard Jones polynomial convention):
      unknot:   V(q) = 1
      trefoil:  V(q) = -q^{-4} + q^{-3} + q^{-1}  (right-handed)
      figure8:  V(q) = q^{-2} - q^{-1} + 1 - q + q^2
      hopf+:    V(q) = -q^{-5/2} - q^{-1/2}  (positive Hopf link, two components)

    Args:
        knot: one of "unknot", "trefoil", "figure8"
        q: complex value of the variable
    """
    if knot == "unknot":
        return complex(1)
    if knot == "trefoil":
        return -q ** (-4) + q ** (-3) + q ** (-1)
    if knot == "figure8":
        return q ** (-2) - q ** (-1) + 1 - q + q ** 2
    raise ValueError(f"Unknown knot: {knot}")


# =========================================================================
# 5. Crane-Yetter-Kauffman state sum
# =========================================================================

def crane_yetter_S3_x_S1(k: int) -> float:
    r"""Crane-Yetter-Kauffman invariant of S^3 x S^1 at sl_2 level k.

    For a modular tensor category C, CYK(M) = |WRT(M)|^2 by the Kirillov-Balsam
    theorem (TV(M) = CYK(M) when input to TV is the Drinfeld center Z(C)).

    For S^3 x S^1 this is |Z(S^3 x S^1)|^2 = 1 (the four-manifold invariant
    of the standard 4-disk-bundle structure).

    Returns CYK(S^3 x S^1) = 1 in standard normalization.
    """
    # CYK is a 4-manifold invariant; restricted to 3-manifold-cross-S^1 it
    # detects the signature.  S^3 x S^1 has signature 0 hence trivial.
    return 1.0


def crane_yetter_equals_TV(k: int, M_label: str) -> bool:
    r"""Verify Crane-Yetter equals Turaev-Viro for the input MTC.

    By the Kirillov-Balsam theorem (arXiv:1004.1533): for a modular tensor
    category C, TV_C(M) = |WRT_C(M)|^2 = CYK_C(M).

    This is the categorical statement: TV is RT applied to the Drinfeld
    center, and for modular C the center splits as C boxed C^op so the
    invariant becomes |WRT|^2.

    Args:
        k: sl_2 level
        M_label: one of "S3", "S2xS1", "T3"

    Returns:
        True if TV equals CYK (= |WRT|^2) within numerical tolerance.
    """
    if M_label == "S3":
        tv = turaev_viro_S3(k)
        wrt = wrt_S3(k)
        return abs(tv - wrt ** 2) < 1e-10
    if M_label == "S2xS1":
        tv = turaev_viro_S2_x_S1(k)
        wrt = wrt_S2_x_S1(k)
        return abs(tv - wrt ** 2) < 1e-10
    if M_label == "T3":
        tv = turaev_viro_T3(k)
        wrt = wrt_T3(k)
        return abs(tv - wrt ** 2) < 1e-10
    raise ValueError(f"Unknown manifold: {M_label}")


# =========================================================================
# 6. Shadow free energy and the WRT exponentiation conjecture
# =========================================================================

def shadow_F_g(k: int, g: int) -> float:
    r"""Genus-g shadow free energy F_g(sl_2, k) on the uniform-weight lane.

    F_g(A) = kappa(A) * lambda_g^FP

    where lambda_g^FP is the integrated Faber-Pandharipande lambda class.
    For sl_2 at level k, kappa = 3(k+2)/4 and:
      F_0 = 0 (no genus-0 free energy class)
      F_1 = kappa/24
      F_g = kappa * |B_{2g}|/(2g*(2g-2))   for g >= 2

    This is the AP22 generating function (g, not 2g-2).
    """
    if g < 0:
        raise ValueError(f"Negative genus: {g}")
    kappa = sl2_kappa(k)
    if g == 0:
        return 0.0
    if g == 1:
        return kappa / 24.0
    # F_g = kappa * |B_{2g}| / (2g * (2g-2)) for g >= 2
    from sympy import bernoulli as sympy_bern
    B = abs(float(sympy_bern(2 * g)))
    return kappa * B / (2 * g * (2 * g - 2))


def wrt_handlebody(k: int, g: int) -> float:
    r"""WRT invariant of the genus-g handlebody H_g for sl_2 at level k.

    For closed orientable surfaces, Z(Sigma_g) is the Verlinde dimension
    Z_g = sum_j (S_{0j})^{2-2g}.  For the handlebody (the bounding 3-manifold)
    this same formula gives the dimension of the Hilbert space.

    Z_k(H_g) = sum_j S_{0j}^{2-2g}

    For g=1: Z_k(H_1) = sum_j 1 = k+1.
    For g=0: Z_k(H_0) = sum_j S_{0j}^2 = 1 (unitarity of S).
    """
    S = sl2_S_matrix(k)
    return float(np.sum(S[0, :] ** (2 - 2 * g)))


def wrt_exponentiation_conjecture(k: int, g: int) -> Dict[str, float]:
    r"""Test WRT(H_g, k) ~ exp(F_g(sl_2, k)) at large level k.

    The conjectural relation: at large k (semiclassical limit),

        log Z_k(H_g) ~ F_g(sl_2, k) + lower order

    where Z_k(H_g) = sum_j S_{0j}^{2-2g} is the Verlinde number and
    F_g = kappa(sl_2, k) * lambda_g^FP is the shadow free energy.

    This function returns both quantities and their difference.
    The conjecture is heuristic; the precise large-k asymptotic involves
    the Witten zeta function and Reidemeister torsion (Witten 1989).

    Returns dict with WRT_value, log_WRT, F_g, ratio.
    """
    Z = wrt_handlebody(k, g)
    Fg = shadow_F_g(k, g)
    log_Z = math.log(abs(Z)) if Z > 0 else float("-inf")
    ratio = log_Z / Fg if Fg != 0 else float("nan")
    return {
        "WRT_value": Z,
        "log_WRT": log_Z,
        "F_g": Fg,
        "ratio": ratio,
    }


# =========================================================================
# 7. Levin-Wen string-net model
# =========================================================================

def levin_wen_ground_state_dim_torus(k: int) -> int:
    r"""Levin-Wen ground state degeneracy on the 2-torus T^2 for sl_2 at level k.

    The Levin-Wen string-net Hamiltonian on a closed surface Sigma has
    ground state space isomorphic to the Hilbert space Z(Sigma) of the
    Drinfeld center Z(C) of the input fusion category C.

    For C = sl_2 at level k (which is already modular), Z(C) = C boxed C^op
    so dim Z(T^2) = (k+1)^2.

    Wait -- for a MODULAR input C, the Levin-Wen model realizes the doubled
    theory.  The ground state degeneracy on T^2 is (number of simples)^2
    when we use C as input but the model produces Z(C) phases.  More
    precisely, for input fusion category C the GSD on Sigma_g equals the
    number of simples of Z(C) raised to a function of g.

    For sl_2 level k as a modular input, dim Z(T^2)_{Z(C)} = |Irr(Z(C))|.
    Z(sl_2_k) has |Irr|^2 = (k+1)^2 simple objects (Drinfeld doubling).

    Hence GSD(T^2) = (k+1)^2.
    """
    return (k + 1) ** 2


def levin_wen_ground_state_dim_genus(k: int, g: int) -> int:
    r"""Levin-Wen ground state degeneracy on Sigma_g for sl_2 at level k.

    For a modular tensor category C with N simple objects, the Drinfeld
    center Z(C) has N^2 simple objects.  The Levin-Wen ground state
    degeneracy on Sigma_g equals the Verlinde formula for Z(C):

        GSD_{LW}(Sigma_g, C) = sum_{a in Irr(Z(C))} (S^{Z(C)}_{0a})^{2-2g}

    For C = sl_2_k modular, |Irr(Z(C))| = (k+1)^2 and the doubled S-matrix
    factorizes.  The GSD on Sigma_g for the doubled theory equals
    (Z_g(sl_2_k))^2 = (sum_j S_{0j}^{2-2g})^2.

    For g=1: GSD = (k+1)^2.  For g=0: GSD = 1 * 1 = 1.

    Args:
        k: sl_2 level
        g: surface genus

    Returns:
        integer ground state degeneracy
    """
    Z_g = wrt_handlebody(k, g)
    # The doubled Verlinde number rounds to integer for modular C
    return int(round(Z_g * Z_g))


def levin_wen_plaquette_term(k: int, j_in: int, j_out: int) -> float:
    r"""Schematic plaquette amplitude for the Levin-Wen Hamiltonian.

    The B_p plaquette operator acts as

        B_p^s |labels> = sum_{s'} (d_s' / D^2) * 6j-coefficients * |labels'>

    For a single edge transition j_in -> j_out via the s=1 (fundamental)
    plaquette excitation, the matrix element is:

        <j_out | B_p^{s=1} | j_in> = (d_1 / D^2) * delta_{adjacent}(j_in, j_out)

    where adjacency means j_out in {j_in - 1, j_in + 1} (sl_2 fusion with
    the fundamental rep).

    Returns the matrix element (zero if not adjacent).
    """
    if abs(j_in - j_out) != 1:
        return 0.0
    if not (0 <= j_in <= k and 0 <= j_out <= k):
        return 0.0
    d1 = quantum_integer(2, k)
    Dsq = sl2_total_quantum_dimension_sq(k)
    return d1 / Dsq


# =========================================================================
# 8. Verification harness: 6j orthogonality and pentagon
# =========================================================================

def verify_6j_orthogonality(k: int, j1: int, j2: int, j3: int, j4: int) -> float:
    r"""Test the orthogonality relation for 6j-symbols at sl_2 level k.

    The orthogonality relation is:

        sum_j d_j * {j1 j2 j; j3 j4 j5} * {j1 j2 j; j3 j4 j6} = delta_{j5, j6} / d_{j5}

    For our test we fix j1, j2, j3, j4 and check that

        sum_j d_j * {...; j5}^2 = 1/d_{j5} when j5 = j6

    Returns the maximum absolute violation across admissible (j5, j6).
    """
    max_err = 0.0
    d = sl2_quantum_dimensions(k)
    for j5 in range(k + 1):
        for j6 in range(k + 1):
            if d[j5] < 1e-15:
                continue
            total = 0.0
            for j in range(k + 1):
                v1 = quantum_6j_symbol(j1, j2, j, j3, j4, j5, k)
                v2 = quantum_6j_symbol(j1, j2, j, j3, j4, j6, k)
                total += d[j] * v1 * v2
            expected = 1.0 / d[j5] if j5 == j6 else 0.0
            err = abs(total - expected)
            if err > max_err:
                max_err = err
    return max_err


# =========================================================================
# 9. Bar fusion data extraction (consistency interface)
# =========================================================================

def bar_fusion_data(k: int) -> Dict[str, object]:
    r"""Extract the spherical fusion category data from the genus-1 bar complex
    for sl_2 at level k.

    Returns a dictionary containing:
      - num_simples: number of integrable representations (= k+1)
      - quantum_dimensions: array of d_j
      - total_quantum_dim_sq: D^2
      - fusion_coefficients: tensor N_{ij}^m
      - S_matrix: modular S
      - T_matrix: modular T
      - twists: theta_j
      - conformal_weights: h_j
      - central_charge: c
      - kappa: arity-2 shadow coefficient

    This is the interface from the bar complex (genus-1 curved bar +
    Zhu algebra) to TQFT state-sum data.
    """
    return {
        "num_simples": k + 1,
        "quantum_dimensions": sl2_quantum_dimensions(k),
        "total_quantum_dim_sq": sl2_total_quantum_dimension_sq(k),
        "fusion_coefficients": sl2_fusion_coefficients(k),
        "S_matrix": sl2_S_matrix(k),
        "T_matrix": sl2_T_matrix(k),
        "twists": sl2_twist(k),
        "conformal_weights": sl2_conformal_weights(k),
        "central_charge": sl2_central_charge(k),
        "kappa": sl2_kappa(k),
    }
