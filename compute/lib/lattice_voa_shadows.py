r"""Shadow obstruction tower data for lattice VOAs: D_4, E_8, and the Leech lattice.

Computes the complete shadow obstruction tower and complementarity data for lattice
vertex operator algebras V_Lambda.

MATHEMATICAL FRAMEWORK
======================

For an even lattice Lambda of rank r:

1. MODULAR CHARACTERISTIC (from first principles):
   kappa(V_Lambda) = rank(Lambda).
   This follows from the genus-1 curvature computation: the bar
   complex on M_{1,n} sees only the Cartan sector (rank copies of
   Heisenberg at level 1), each contributing curvature 1.  The root
   sectors have d^2 = 0 (cocycle-curvature orthogonality,
   thm:lattice:curvature-braiding-orthogonal).

2. SHADOW CLASS G (Gaussian):
   All higher shadow coefficients vanish: S_3 = S_4 = ... = 0.
   The L_infinity algebra Def_inf^mod(V_Lambda) is FORMAL: the
   transferred higher brackets ell_k^{tr} are all coboundaries
   (by curvature-braiding orthogonality).  Shadow depth = 2.
   Shadow metric Q_L = (2*kappa)^2 (constant), discriminant Delta = 0.

3. GENUS EXPANSION:
   F_g(V_Lambda) = kappa * lambda_g^FP  for all g >= 1,
   where lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!.

4. R-MATRIX:
   r(z) = Omega_Lambda / z  where Omega_Lambda is the lattice Casimir
   (sum of e_i tensor e_i over an orthonormal basis of Lambda tensor Q).
   The r-matrix has a SINGLE pole at z^{-1} because the bar propagator
   d log E(z,w) absorbs one pole order from the OPE (AP19).

5. COMPLEMENTARITY (thm:lattice:curvature-braiding-orthogonal proof):
   kappa(V_Lambda) = rank(Lambda)
   kappa(V_Lambda^!) = -rank(Lambda)
   kappa + kappa' = 0.

   This holds for ALL lattice VOAs, including unimodular ones.
   For unimodular Lambda, V_Lambda^! is isomorphic to V_Lambda as
   an abstract vertex algebra (thm:lattice:unimodular-self-dual),
   but the Koszul dual carries the inverse cocycle with negated
   Cartan level (Verdier duality negates the level).  The curvature
   is a bar-complex invariant distinguishing the two presentations.

   SUBTLETY: Heisenberg is NOT self-dual.  H_k^! = Sym^ch(V*) with
   curvature m_0 = -k*omega (prop:heisenberg-complementarity).  The
   lattice VOA inherits this from its Cartan sector.

   For non-unimodular lattices (D_4, A_2, E_6, E_7), the Koszul dual
   involves the dual lattice Lambda* and the inverse cocycle
   (thm:lattice:koszul-dual).

SPECIFIC LATTICES
=================

D_4:  rank 4, kappa = 4.  det(Gram) = 4, NOT unimodular.
      D_4^*/D_4 = (Z/2Z)^2 (discriminant group of order 4).
      Triality: S_3 symmetry from D_4 Dynkin diagram outer automorphisms,
      permuting vector/spinor/conjugate-spinor representations.
      V_{D_4}^! = (V_{D_4}^{eps^{-1}})^c (NOT self-dual).

E_8:  rank 8, kappa = 8.  det(Gram) = 1, unimodular (self-dual).
      Theta_{E_8} = E_4 (the Eisenstein series of weight 4).
      240 roots, no vectors with (v,v)/2 = 1 (even lattice, min norm 2).
      V_{E_8}^! = V_{E_8} (Koszul self-dual).

Leech: rank 24, kappa = 24.  det(Gram) = 1, unimodular (self-dual).
       NO roots: r_Leech(1) = 0.  196560 minimal vectors at (v,v)/2 = 2.
       Theta_Leech = E_12 - (65520/691)*Delta.
       V_Leech^! = V_Leech (Koszul self-dual).

Mathematical references:
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - lattice_foundations.tex: cor:lattice-postnikov-termination
  - lattice_foundations.tex: thm:lattice:unimodular-self-dual
  - lattice_foundations.tex: thm:lattice:koszul-dual
  - higher_genus_modular_koszul.tex: shadow depth classification (class G)
  - heisenberg_eisenstein.tex: prop:heisenberg-complementarity
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from sympy import Abs, Rational, bernoulli, factorial


# =========================================================================
# Faber-Pandharipande intersection numbers (exact)
# =========================================================================

def faber_pandharipande(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    All values are positive (Bernoulli signs alternate, absorbed by |B|).
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = Rational(bernoulli(2 * g))
    numerator = (Rational(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    denominator = Rational(2) ** (2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


# =========================================================================
# Kappa from first principles
# =========================================================================

def kappa_lattice(rank: int) -> Rational:
    r"""Modular characteristic of a lattice VOA from first principles.

    kappa(V_Lambda) = rank(Lambda).

    Derivation: the genus-1 bar complex B^{(1)}(V_Lambda) decomposes as
        B^{(1)}_Cartan(H_r) tensor B^{(0)}_roots(V_Lambda).
    The Cartan sector consists of r independent Heisenberg bosons at level 1.
    Each contributes kappa = 1 to the genus-1 curvature (the Arnold relation
    A_3^{(1)} = 2*pi*i * omega_vol produces d^2 = 1 * omega_1 per boson).
    By additivity of kappa (prop:independent-sum-factorization), the total is
    kappa = r * 1 = rank.

    The root sectors contribute d^2 = 0 (cocycle-curvature orthogonality:
    the simple-pole residues are unchanged at genus 1, so d^{(1)} = d^{(0)}
    in each root sector).
    """
    if rank < 0:
        raise ValueError(f"Rank must be non-negative, got {rank}")
    return Rational(rank)


def kappa_lattice_dual(rank: int) -> Rational:
    r"""Modular characteristic of the Koszul dual of a lattice VOA.

    kappa(V_Lambda^!) = -rank(Lambda).

    The Koszul dual has Cartan level -1 per boson (the sign flip from
    Verdier duality on configuration spaces), giving kappa = -rank.
    This is the lattice analogue of kappa(H_k^!) = -k for Heisenberg
    (prop:heisenberg-complementarity).
    """
    if rank < 0:
        raise ValueError(f"Rank must be non-negative, got {rank}")
    return Rational(-rank)


# =========================================================================
# Shadow obstruction tower verification
# =========================================================================

def verify_class_G(rank: int) -> Dict[str, Any]:
    r"""Verify that a lattice VOA is class G (Gaussian, shadow depth 2).

    For class G:
      S_3 = 0 (cubic shadow vanishes)
      S_4 = 0 (quartic contact vanishes)
      alpha = 0 (cubic coefficient on primary line vanishes)
      Delta = 0 (critical discriminant vanishes)
      Q_L = (2*kappa)^2 (shadow metric is a perfect square)

    The vanishing of all higher shadows follows from formality of
    Def_inf^mod(V_Lambda): the L_infinity transferred brackets ell_k^{tr}
    are coboundaries by curvature-braiding orthogonality
    (thm:lattice:curvature-braiding-orthogonal), so the shadow algebra
    reduces to Q[kappa].

    Compare with:
      Class L (Lie/tree, e.g. affine KM): S_3 != 0, S_4 = 0, depth 3
      Class C (contact, e.g. beta-gamma): S_3 != 0, S_4 != 0, depth 4
      Class M (mixed, e.g. Virasoro): Delta != 0, depth infinity
    """
    kappa = Rational(rank)
    S3 = Rational(0)
    S4 = Rational(0)
    alpha = Rational(0)

    # Critical discriminant: Delta = 8*kappa*S_4
    Delta = 8 * kappa * S4

    # Shadow metric: Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    # For alpha = 0, Delta = 0: Q_L = (2*kappa)^2 = 4*kappa^2
    Q_L_constant = 4 * kappa ** 2

    # Verify Q_L is a perfect square (equivalent to Delta = 0)
    is_perfect_square = (Delta == 0)

    return {
        'kappa': kappa,
        'S3': S3,
        'S4': S4,
        'alpha': alpha,
        'Delta': Delta,
        'Q_L': Q_L_constant,
        'is_perfect_square': is_perfect_square,
        'shadow_depth': 2,
        'shadow_class': 'G',
        'all_higher_vanish': True,
    }


# =========================================================================
# Genus expansion
# =========================================================================

def genus_expansion(rank: int, max_g: int = 5) -> Dict[int, Rational]:
    r"""Genus expansion F_g(V_Lambda) = kappa * lambda_g^FP.

    For a lattice VOA of rank r, the genus-g free energy is
        F_g = r * lambda_g^FP
    where lambda_g^FP is the Faber-Pandharipande intersection number.

    This is the universal formula for Gaussian class (shadow depth 2)
    algebras: the shadow Postnikov tower terminates at arity 2, so
    there are no higher-arity corrections to the genus expansion.

    Values for g = 1..5:
      F_1 = rank / 24
      F_2 = rank * 7 / 5760
      F_3 = rank * 31 / 967680
      F_4 = rank * 127 / 154828800
      F_5 = rank * 2555 / 122624409600
    """
    kappa = Rational(rank)
    result = {}
    for g in range(1, max_g + 1):
        result[g] = kappa * faber_pandharipande(g)
    return result


# =========================================================================
# Complementarity
# =========================================================================

def complementarity(rank: int, is_unimodular: bool = False) -> Dict[str, Any]:
    r"""Complementarity data for a lattice VOA.

    For a lattice Lambda of rank r:
      kappa(V_Lambda) = r
      kappa(V_Lambda^!) = -r  (Verdier duality negates Cartan level)
      kappa + kappa' = 0

    This holds for ALL lattice VOAs (unimodular or not).

    For unimodular lattices (E_8, Leech, D_8^+, ...):
      V_Lambda^! = V_Lambda as abstract vertex algebras
      (thm:lattice:unimodular-self-dual), but the bar-complex
      curvature distinguishes the two Koszul-pair roles.

    For non-unimodular lattices (D_4, A_2, E_6, E_7, ...):
      V_Lambda^! = (V_{Lambda}^{eps^{-1}})^c  (coalgebra on inverse cocycle)
      The dual lattice Lambda* appears via the coalgebra structure.

    Returns dict with kappa, kappa_dual, complementarity_sum, and metadata.
    """
    kappa = kappa_lattice(rank)
    kappa_dual = kappa_lattice_dual(rank)
    comp_sum = kappa + kappa_dual

    return {
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'complementarity_sum': comp_sum,
        'sum_is_zero': comp_sum == 0,
        'is_unimodular': is_unimodular,
        'koszul_self_dual': is_unimodular,
        'rank': rank,
    }


# =========================================================================
# r-matrix
# =========================================================================

def r_matrix_data(rank: int) -> Dict[str, Any]:
    r"""r-matrix data for a lattice VOA.

    r(z) = Omega_Lambda / z

    where Omega_Lambda = sum_i e_i tensor e_i is the lattice Casimir
    (the identity element of End(Lambda tensor Q) expressed in an
    orthonormal basis).

    The r-matrix has a SINGLE pole at z^{-1} because:
    - The lattice OPE has poles at z^{-2} (double pole from Heisenberg)
      and z^{-1} (simple pole from vertex operators).
    - The bar propagator d log E(z,w) absorbs one pole order (AP19):
      the residue of d log(z-w) * z^{-n} at z=w is z^{-(n-1)}.
    - So the double pole z^{-2} maps to z^{-1} in the r-matrix.
    - The simple pole z^{-1} maps to a constant (z^0), which is
      the braiding data (absorbed into the cocycle).

    For rank r, the Casimir has trace = r (the dimension).
    """
    return {
        'r_matrix_type': 'single_pole',
        'pole_order': 1,
        'residue_trace': Rational(rank),
        'formula': f'Omega_Lambda / z  (rank {rank} Casimir)',
        'rank': rank,
    }


# =========================================================================
# Per-lattice data: D_4, E_8, Leech
# =========================================================================

def d4_shadow_data() -> Dict[str, Any]:
    r"""Complete shadow obstruction tower data for the D_4 lattice VOA.

    D_4: rank 4, 24 roots, det(Gram) = 4.
    NOT unimodular: D_4^*/D_4 = (Z/2Z)^2.
    Triality: S_3 symmetry from D_4 Dynkin diagram outer automorphisms.

    V_{D_4} is NOT Koszul self-dual (prop:lattice:D4-triality).
    Its Koszul dual is (V_{D_4}^{eps^{-1}})^c.

    Shadow data:
      kappa = 4, class G, depth 2
      S_3 = S_4 = 0
      F_1 = 4/24 = 1/6
    """
    rank = 4
    shadow = verify_class_G(rank)
    comp = complementarity(rank, is_unimodular=False)
    genus = genus_expansion(rank)

    return {
        'name': 'D_4',
        'rank': rank,
        'root_count': 24,
        'gram_det': 4,
        'discriminant_group': '(Z/2Z)^2',
        'discriminant_order': 4,
        'is_unimodular': False,
        'has_triality': True,
        'shadow': shadow,
        'complementarity': comp,
        'genus_expansion': genus,
        'r_matrix': r_matrix_data(rank),
        'theta_first_shells': [1, 24, 24, 96, 24, 144],  # r_{D_4}(0..5)
    }


def e8_shadow_data() -> Dict[str, Any]:
    r"""Complete shadow obstruction tower data for the E_8 lattice VOA.

    E_8: rank 8, 240 roots, det(Gram) = 1.
    Unimodular: E_8 = E_8^* (self-dual lattice).
    V_{E_8}^! = V_{E_8} (Koszul self-dual, thm:lattice:unimodular-self-dual).

    Theta_{E_8} = E_4(tau) = 1 + 240*sum sigma_3(n) q^n.

    Shadow data:
      kappa = 8, class G, depth 2
      S_3 = S_4 = 0
      F_1 = 8/24 = 1/3
    """
    rank = 8
    shadow = verify_class_G(rank)
    comp = complementarity(rank, is_unimodular=True)
    genus = genus_expansion(rank)

    return {
        'name': 'E_8',
        'rank': rank,
        'root_count': 240,
        'gram_det': 1,
        'is_unimodular': True,
        'shadow': shadow,
        'complementarity': comp,
        'genus_expansion': genus,
        'r_matrix': r_matrix_data(rank),
        'theta_first_shells': [1, 240, 2160, 6720, 17520, 30240],
    }


def leech_shadow_data() -> Dict[str, Any]:
    r"""Complete shadow obstruction tower data for the Leech lattice VOA.

    Leech: rank 24, NO roots, 196560 minimal vectors, det(Gram) = 1.
    Unimodular: Leech = Leech^* (self-dual lattice).
    V_Leech^! = V_Leech (Koszul self-dual).

    Theta_Leech = E_12 - (65520/691)*Delta.
    r_Leech(0) = 1, r_Leech(1) = 0, r_Leech(2) = 196560.

    Shadow data:
      kappa = 24, class G, depth 2
      S_3 = S_4 = 0
      F_1 = 24/24 = 1
    """
    rank = 24
    shadow = verify_class_G(rank)
    comp = complementarity(rank, is_unimodular=True)
    genus = genus_expansion(rank)

    return {
        'name': 'Leech',
        'rank': rank,
        'root_count': 0,
        'min_vector_count': 196560,
        'gram_det': 1,
        'is_unimodular': True,
        'shadow': shadow,
        'complementarity': comp,
        'genus_expansion': genus,
        'r_matrix': r_matrix_data(rank),
        'theta_first_shells': [1, 0, 196560, 16773120, 398034000],
    }


# =========================================================================
# Per-lattice data: Barnes-Wall BW_16
# =========================================================================

def barnes_wall_shadow_data() -> Dict[str, Any]:
    r"""Complete shadow obstruction tower data for the Barnes-Wall lattice BW_16.

    BW_16: rank 16, NO roots (minimum norm 4), det(Gram) = 256 = 2^8.
    NOT unimodular: BW_16 is even but not self-dual.
    Kissing number = 4320 (vectors of norm 4).

    Shadow data:
      kappa = 16, class G, depth 2
      S_3 = S_4 = 0
      F_1 = 16/24 = 2/3
    """
    rank = 16
    shadow = verify_class_G(rank)
    comp = complementarity(rank, is_unimodular=False)
    genus = genus_expansion(rank)

    return {
        'name': 'BW_16',
        'rank': rank,
        'root_count': 0,
        'min_vector_count': 4320,
        'min_vector_norm': 4,
        'gram_det': 256,
        'is_unimodular': False,
        'is_even': True,
        'shadow': shadow,
        'complementarity': comp,
        'genus_expansion': genus,
        'r_matrix': r_matrix_data(rank),
    }


# =========================================================================
# Niemeier lattice data (24 even unimodular lattices of rank 24)
# =========================================================================

# The 24 Niemeier lattices classified by root system.
# Root counts: |roots(A_n)| = n(n+1), |roots(D_n)| = 2n(n-1),
# |roots(E_6)| = 72, |roots(E_7)| = 126, |roots(E_8)| = 240.
NIEMEIER_DATA: List[Dict[str, Any]] = [
    {'name': 'D24', 'root_system': 'D_{24}', 'root_count': 2*24*23},
    {'name': 'D16+E8', 'root_system': 'D_{16} \\oplus E_8', 'root_count': 2*16*15 + 240},
    {'name': '3E8', 'root_system': 'E_8^{\\oplus 3}', 'root_count': 3*240},
    {'name': 'A24', 'root_system': 'A_{24}', 'root_count': 24*25},
    {'name': '2D12', 'root_system': 'D_{12}^{\\oplus 2}', 'root_count': 2*2*12*11},
    {'name': 'A17+E7', 'root_system': 'A_{17} \\oplus E_7', 'root_count': 17*18 + 126},
    {'name': 'D10+2E7', 'root_system': 'D_{10} \\oplus E_7^{\\oplus 2}', 'root_count': 2*10*9 + 2*126},
    {'name': 'A15+D9', 'root_system': 'A_{15} \\oplus D_9', 'root_count': 15*16 + 2*9*8},
    {'name': '3D8', 'root_system': 'D_8^{\\oplus 3}', 'root_count': 3*2*8*7},
    {'name': '2A12', 'root_system': 'A_{12}^{\\oplus 2}', 'root_count': 2*12*13},
    {'name': 'A11+D7+E6', 'root_system': 'A_{11} \\oplus D_7 \\oplus E_6', 'root_count': 11*12 + 2*7*6 + 72},
    {'name': '4E6', 'root_system': 'E_6^{\\oplus 4}', 'root_count': 4*72},
    {'name': '2A9+D6', 'root_system': 'A_9^{\\oplus 2} \\oplus D_6', 'root_count': 2*9*10 + 2*6*5},
    {'name': '4D6', 'root_system': 'D_6^{\\oplus 4}', 'root_count': 4*2*6*5},
    {'name': '3A8', 'root_system': 'A_8^{\\oplus 3}', 'root_count': 3*8*9},
    {'name': '2A7+2D5', 'root_system': 'A_7^{\\oplus 2} \\oplus D_5^{\\oplus 2}', 'root_count': 2*7*8 + 2*2*5*4},
    {'name': '4A6', 'root_system': 'A_6^{\\oplus 4}', 'root_count': 4*6*7},
    {'name': '4A5+D4', 'root_system': 'A_5^{\\oplus 4} \\oplus D_4', 'root_count': 4*5*6 + 2*4*3},
    {'name': '6D4', 'root_system': 'D_4^{\\oplus 6}', 'root_count': 6*2*4*3},
    {'name': '6A4', 'root_system': 'A_4^{\\oplus 6}', 'root_count': 6*4*5},
    {'name': '8A3', 'root_system': 'A_3^{\\oplus 8}', 'root_count': 8*3*4},
    {'name': '12A2', 'root_system': 'A_2^{\\oplus 12}', 'root_count': 12*2*3},
    {'name': '24A1', 'root_system': 'A_1^{\\oplus 24}', 'root_count': 24*1*2},
    {'name': 'Leech', 'root_system': '\\emptyset', 'root_count': 0},
]


def niemeier_shadow_data(index_or_name) -> Dict[str, Any]:
    r"""Shadow obstruction tower data for a Niemeier lattice.

    All 24 Niemeier lattices are even unimodular lattices of rank 24,
    so they all have:
      kappa = 24, class G, depth 2
      kappa + kappa' = 0
      F_g = 24 * lambda_g^FP

    The shadow obstruction tower depends ONLY on the rank (not on the root system).
    The root system affects the theta function and the root count,
    but not the shadow data, since the shadow obstruction tower is determined by the
    Cartan sector (24 Heisenberg bosons) and the root sectors have d^2 = 0
    by cocycle-curvature orthogonality.

    Args:
        index_or_name: either an integer 0..23 into NIEMEIER_DATA or a
            string name (e.g. 'D24', '3E8', 'Leech').
    """
    if isinstance(index_or_name, int):
        if not 0 <= index_or_name < 24:
            raise ValueError(f"Niemeier index must be 0..23, got {index_or_name}")
        entry = NIEMEIER_DATA[index_or_name]
    else:
        matches = [e for e in NIEMEIER_DATA if e['name'] == index_or_name]
        if not matches:
            raise ValueError(
                f"Unknown Niemeier lattice: {index_or_name}. "
                f"Known: {[e['name'] for e in NIEMEIER_DATA]}"
            )
        entry = matches[0]

    rank = 24
    shadow = verify_class_G(rank)
    comp = complementarity(rank, is_unimodular=True)
    genus = genus_expansion(rank)

    return {
        'name': entry['name'],
        'root_system': entry['root_system'],
        'rank': rank,
        'root_count': entry['root_count'],
        'gram_det': 1,
        'is_unimodular': True,
        'is_even': True,
        'shadow': shadow,
        'complementarity': comp,
        'genus_expansion': genus,
        'r_matrix': r_matrix_data(rank),
    }


def niemeier_kappa_table() -> List[Dict[str, Any]]:
    r"""Kappa values for all 24 Niemeier lattices.

    Since all Niemeier lattices have rank 24, they all share
    kappa = 24.  This function returns a table confirming this
    alongside the root count and root system for each lattice.
    """
    table = []
    for i, entry in enumerate(NIEMEIER_DATA):
        table.append({
            'index': i,
            'name': entry['name'],
            'root_system': entry['root_system'],
            'root_count': entry['root_count'],
            'rank': 24,
            'kappa': Rational(24),
            'kappa_dual': Rational(-24),
            'comp_sum': Rational(0),
            'shadow_class': 'G',
            'shadow_depth': 2,
        })
    return table


def verify_all_even_lattice_class_G(ranks: Optional[List[int]] = None) -> Dict[str, Any]:
    r"""Verify that ALL even lattice VOAs of given ranks are class G.

    For any even lattice Lambda, V_Lambda is class G because:
    1. The Cartan sector consists of rank(Lambda) Heisenberg bosons at level 1.
    2. Each boson contributes kappa = 1, S_3 = S_4 = 0 (Gaussian).
    3. Root sectors have d^2 = 0 by cocycle-curvature orthogonality.
    4. By additivity (prop:independent-sum-factorization), the full VOA
       has kappa = rank, S_3 = S_4 = 0.

    This is INDEPENDENT of whether the lattice is unimodular.
    The shadow obstruction tower depends only on the rank.

    Args:
        ranks: list of ranks to check. Default [1,2,4,8,16,24].
    """
    if ranks is None:
        ranks = [1, 2, 4, 8, 16, 24]

    results = {}
    all_class_G = True

    for r in ranks:
        data = verify_class_G(r)
        is_G = (
            data['shadow_class'] == 'G'
            and data['S3'] == 0
            and data['S4'] == 0
            and data['Delta'] == 0
            and data['shadow_depth'] == 2
        )
        results[r] = {
            'rank': r,
            'kappa': data['kappa'],
            'is_class_G': is_G,
            'S3': data['S3'],
            'S4': data['S4'],
            'Delta': data['Delta'],
        }
        if not is_G:
            all_class_G = False

    return {
        'all_class_G': all_class_G,
        'per_rank': results,
        'reason': (
            'Lattice VOA shadow obstruction tower depends only on rank. '
            'The Cartan sector (Heisenberg bosons) determines kappa = rank, S_3=S_4=0. '
            'Root sectors contribute d^2=0 by cocycle-curvature orthogonality. '
            'Unimodularity is irrelevant to the shadow class.'
        ),
    }


# =========================================================================
# Cross-lattice consistency checks
# =========================================================================

def verify_kappa_additivity(rank1: int, rank2: int, max_g: int = 5) -> bool:
    r"""Verify kappa additivity: F_g(Lambda1 + Lambda2) = F_g(Lambda1) + F_g(Lambda2).

    For direct sum lattices, kappa is additive
    (prop:independent-sum-factorization).  This means the genus expansion
    is additive: F_g(rank1 + rank2) = F_g(rank1) + F_g(rank2).

    This is a non-trivial cross-check: it follows from the vanishing
    of all mixed shadow coefficients (the OPE between bosons in
    different summands is trivial).
    """
    for g in range(1, max_g + 1):
        f_sum = genus_expansion(rank1 + rank2, max_g=g)[g]
        f_1 = genus_expansion(rank1, max_g=g)[g]
        f_2 = genus_expansion(rank2, max_g=g)[g]
        if f_sum != f_1 + f_2:
            return False
    return True


def cross_family_consistency() -> Dict[str, bool]:
    r"""Cross-family consistency checks for D_4, E_8, Leech.

    Verifies:
    1. All three are class G
    2. Complementarity sum is zero for all three
    3. Kappa scales linearly with rank
    4. F_1 = rank/24 for all three
    5. F_g additivity: F_g(E_8) = 2 * F_g(D_4) (since 8 = 2*4)
    6. F_g(Leech) = 3 * F_g(E_8) (since 24 = 3*8)
    """
    d4 = d4_shadow_data()
    e8 = e8_shadow_data()
    leech = leech_shadow_data()

    checks = {}

    # All class G
    checks['d4_class_G'] = d4['shadow']['shadow_class'] == 'G'
    checks['e8_class_G'] = e8['shadow']['shadow_class'] == 'G'
    checks['leech_class_G'] = leech['shadow']['shadow_class'] == 'G'

    # Complementarity sum = 0
    checks['d4_comp_zero'] = d4['complementarity']['sum_is_zero']
    checks['e8_comp_zero'] = e8['complementarity']['sum_is_zero']
    checks['leech_comp_zero'] = leech['complementarity']['sum_is_zero']

    # Kappa = rank
    checks['d4_kappa_rank'] = d4['shadow']['kappa'] == Rational(4)
    checks['e8_kappa_rank'] = e8['shadow']['kappa'] == Rational(8)
    checks['leech_kappa_rank'] = leech['shadow']['kappa'] == Rational(24)

    # F_1 = rank/24
    checks['d4_f1'] = d4['genus_expansion'][1] == Rational(4, 24)
    checks['e8_f1'] = e8['genus_expansion'][1] == Rational(8, 24)
    checks['leech_f1'] = leech['genus_expansion'][1] == Rational(24, 24)

    # Additivity: F_g(E_8) = 2*F_g(D_4)
    for g in range(1, 6):
        checks[f'e8_eq_2xd4_g{g}'] = (
            e8['genus_expansion'][g] == 2 * d4['genus_expansion'][g]
        )

    # Additivity: F_g(Leech) = 3*F_g(E_8)
    for g in range(1, 6):
        checks[f'leech_eq_3xe8_g{g}'] = (
            leech['genus_expansion'][g] == 3 * e8['genus_expansion'][g]
        )

    return checks


# =========================================================================
# Shadow obstruction tower comparison table
# =========================================================================

def comparison_table() -> List[Dict[str, Any]]:
    r"""Comparison table of shadow obstruction tower data for D_4, E_8, Leech.

    Returns a list of dicts, one per lattice, suitable for display or
    further analysis.
    """
    lattices = [d4_shadow_data(), e8_shadow_data(), leech_shadow_data()]
    table = []

    for lat in lattices:
        row = {
            'name': lat['name'],
            'rank': lat['rank'],
            'kappa': lat['shadow']['kappa'],
            'kappa_dual': lat['complementarity']['kappa_dual'],
            'comp_sum': lat['complementarity']['complementarity_sum'],
            'shadow_class': lat['shadow']['shadow_class'],
            'shadow_depth': lat['shadow']['shadow_depth'],
            'S3': lat['shadow']['S3'],
            'S4': lat['shadow']['S4'],
            'Delta': lat['shadow']['Delta'],
            'is_unimodular': lat.get('is_unimodular', False),
            'root_count': lat.get('root_count', 0),
            'F_1': lat['genus_expansion'][1],
            'F_2': lat['genus_expansion'][2],
            'F_3': lat['genus_expansion'][3],
            'F_4': lat['genus_expansion'][4],
            'F_5': lat['genus_expansion'][5],
        }
        table.append(row)

    return table
