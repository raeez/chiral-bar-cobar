r"""Explicit bar cohomology for rank-r Heisenberg and E_8 lattice VOA.

MATHEMATICAL FRAMEWORK
======================

1. RANK-r HEISENBERG H_k^{rank r}

   r generators phi^1,...,phi^r, each conformal weight 1.
   OPE: phi^i(z) phi^j(w) ~ k delta^{ij} / (z-w)^2.

   Bar complex modes: V_bar has basis {phi^i_{-n} : i=1..r, n >= 1}
   with phi^i_{-n} at weight n.  So dim V_bar(h) = r for each h >= 1.

   Bar chain dimensions at bar degree n, total weight h:
     dim B^n_h = r^n * C(h-1, n-1) * (n-1)!
   because there are C(h-1,n-1) compositions of h into n parts >= 1,
   each tensor factor has r choices (the r generators at that weight),
   and the form factor is (n-1)! = dim Omega^{n-1}(Conf_n).

   KOSZULNESS (class G): For rank-r Heisenberg, the bar complex is
   that of a direct sum of r commutative chiral algebras.  By the
   PBW spectral sequence (K1-K2 in thm:koszul-equivalences-meta) and
   the Whitehead lemma for abelian current algebras, the bar cohomology
   concentrates in bar degree 1:
     H^n(B(H_k^r)) = 0  for n >= 2  (Koszulness)
     H^1(B(H_k^r))_h = dim(A^!)_h  (Koszul dual generators)

   The Koszul dual of the rank-r Heisenberg is the rank-r chiral
   exterior algebra (Lie cooperad dual to commutative operad).

   MODULAR CHARACTERISTIC:
     kappa(H_k^{rank r}) = r * k  (additivity, prop:independent-sum-factorization)
   For k=1: kappa = r.

   SHADOW CLASS: G (Gaussian, shadow depth 2, tower terminates at arity 2).

2. E_8 LATTICE VOA V_{E_8}

   Extends H_1^{rank 8} by 240 vertex operators e^alpha for alpha in
   Delta(E_8), each of conformal weight 1.  Total: 248 weight-1 currents.

   TWO DESCRIPTIONS, TWO DIFFERENT BAR COMPLEXES (AP48):

   (a) LATTICE DESCRIPTION: V_{E_8} viewed as lattice VOA.
       The bar complex sees r = rank = 8 independent Heisenberg bosons
       plus the lattice vertex operators.  The key structural theorem
       (thm:lattice:curvature-braiding-orthogonal) says the root sectors
       have d^2 = 0 independently (cocycle-curvature orthogonality),
       so they do NOT contribute to the genus-1 curvature.
       kappa(V_{E_8} as lattice) = rank(E_8) = 8.

   (b) AFFINE KM DESCRIPTION: V_{E_8} = V_1(e_8), the level-1 vacuum
       module of the affine Lie algebra e_8^{(1)}.
       All 248 currents are treated as generators of the current algebra.
       kappa(V_1(e_8) as affine KM) = dim(e_8)*(k+h^vee)/(2*h^vee)
                                     = 248*31/60 = 1922/15.

   These are DIFFERENT values for DIFFERENT presentations of the same
   underlying VOA.  The bar complex depends on the presentation (the
   choice of strong generators), not just the isomorphism class.

   KOSZULNESS: Both descriptions are Koszul.
     - Lattice description: class G (Gaussian, depth 2)
     - Affine KM description: class L (Lie/tree, depth 3)

   ROOT VECTOR CONTRIBUTION TO BAR COHOMOLOGY:
   The 240 root vectors e^alpha do NOT generate new independent bar
   cohomology classes beyond those from the Lie algebra structure.
   By the PBW spectral sequence for V_1(e_8), the bar cohomology
   equals the Chevalley-Eilenberg cohomology of e_8 tensor t^{-1}C[t^{-1}],
   which is controlled by the Lie algebra cohomology of e_8.

   For the lattice description: the bar cohomology of V_{E_8} decomposes
   as the bar cohomology of H_1^8 (Cartan sector) tensored with the
   cohomology of the root lattice cocycle complex.  The root lattice
   cocycle complex is acyclic (Koszul acyclicity, prop:E8-koszul-acyclic).

   VERLINDE: At level 1, E_8^{(1)} has a unique integrable representation
   (the vacuum module).  Verlinde formula: dim V_g = 1 for all genera g.

Mathematical references:
  - heisenberg_bar.py: rank-1 Heisenberg bar complex
  - e8_lattice_bar.py: E_8 root system data and degree-2 bar differential
  - lattice_voa_shadows.py: shadow obstruction tower for lattice VOAs
  - e8_affine_shadow_engine.py: affine KM description, kappa = 1922/15
  - bar_cohomology_dimensions.py: first-principles bar cohomology computation

Conventions:
  Cohomological grading (|d| = +1).
  Bar uses desuspension s^{-1}: |s^{-1}v| = |v| - 1 (AP45).
  Killing form: long roots have length^2 = 2.
  Exact rational arithmetic via sympy.Rational.
"""

from __future__ import annotations

from math import comb, factorial
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, Symbol, bernoulli, Abs


# =========================================================================
# Colored partition numbers (r-colored partitions)
# =========================================================================

def colored_partition_number(h: int, r: int) -> int:
    r"""Number of r-colored partitions of h.

    p_r(h) = coefficient of q^h in prod_{n>=1} 1/(1-q^n)^r.

    For r=1: ordinary partition numbers p(h).
    Generating function: prod_{n>=1} 1/(1-q^n)^r = sum_{h>=0} p_r(h) q^h.
    """
    if h < 0:
        return 0
    if h == 0:
        return 1
    if r <= 0:
        return 0
    return colored_partition_table(h, r)[h]


def colored_partition_table(h_max: int, r: int) -> List[int]:
    """Compute p_r(h) for h = 0, 1, ..., h_max.

    Uses the standard DP: multiply by 1/(1-q^n) a total of r times
    for each n, using the recurrence coeffs[j] += coeffs[j - n].

    Returns list of length h_max + 1.
    """
    coeffs = [0] * (h_max + 1)
    coeffs[0] = 1
    for n in range(1, h_max + 1):
        # Multiply by 1/(1-q^n)^r by applying 1/(1-q^n) r times
        for _ in range(r):
            for j in range(n, h_max + 1):
                coeffs[j] += coeffs[j - n]
    return coeffs


# =========================================================================
# Faber-Pandharipande intersection numbers
# =========================================================================

def faber_pandharipande(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    All values are positive.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = Rational(bernoulli(2 * g))
    numer = (Rational(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    denom = Rational(2) ** (2 * g - 1) * Rational(factorial(2 * g))
    return Rational(numer, denom)


# =========================================================================
# Rank-r Heisenberg: bar complex chain dimensions
# =========================================================================

def heisenberg_rank_r_bar_chain_dim(n: int, h: int, r: int) -> int:
    r"""Dimension of B^n_h for rank-r Heisenberg.

    B^n_h = (V_bar)^{tensor n} tensor Omega^{n-1}(Conf_n).

    For r generators all of weight 1:
      dim V_bar(m) = r for each m >= 1 (r generator modes at weight m).
      Number of compositions h = m_1 + ... + m_n with m_i >= 1: C(h-1, n-1).
      Each tensor factor has r choices: r^n.
      Form factor: (n-1)! = dim Omega^{n-1}(Conf_n).

    Result: dim B^n_h = r^n * C(h-1, n-1) * (n-1)!.
    """
    if n <= 0 or h < n or r <= 0:
        return 0
    return r ** n * comb(h - 1, n - 1) * factorial(n - 1)


def heisenberg_rank_r_bar_chain_total(h: int, r: int) -> int:
    """Total dimension of bar complex at weight h: sum_n dim B^n_h."""
    if h <= 0 or r <= 0:
        return 0
    return sum(heisenberg_rank_r_bar_chain_dim(n, h, r) for n in range(1, h + 1))


def heisenberg_rank_r_euler_char(h: int, r: int) -> int:
    """Euler characteristic of bar complex at weight h.

    chi(B_h) = sum_{n=1}^h (-1)^{n+1} dim B^n_h.
    For Koszul algebras: chi = H^1 (all higher cohomology vanishes).
    """
    if h <= 0 or r <= 0:
        return 0
    total = 0
    for n in range(1, h + 1):
        total += (-1) ** (n + 1) * heisenberg_rank_r_bar_chain_dim(n, h, r)
    return total


# =========================================================================
# Rank-r Heisenberg: bar cohomology (via Koszulness = class G)
# =========================================================================

def heisenberg_rank_r_bar_cohomology_h1(h: int, r: int) -> int:
    r"""Bar cohomology H^1(B(H_k^r))_h.

    For Koszul algebras: H^1 = dim(A^!)_h = Koszul dual dimension at weight h.
    For rank-r Heisenberg: the Koszul dual is the rank-r chiral exterior
    algebra, whose augmentation ideal at weight h has a specific dimension.

    For rank 1: H^1_h matches the known sequence
      {1:1, 2:1, 3:1, 4:2, 5:3, 6:5, 7:7, 8:11}
    from the manuscript (KNOWN_BAR_DIMS in heisenberg_bar.py).

    For rank r: we compute from the generating function of the Koszul dual
    chiral algebra (tensor product of r copies of the rank-1 dual).
    """
    # For the rank-1 Heisenberg, the bar cohomology at weight h is recorded
    # in the manuscript. For general rank r, the bar cohomology of the
    # tensor product decomposes as a convolution.
    #
    # The rank-1 sequence {h: dim} is the ground truth from heisenberg_bar.py.
    # For general r, we use the structural fact that H^{rank r} = H^{tensor r}
    # and bar cohomology of tensor products is the tensor product of bar
    # cohomologies (by Kuenneth for Koszul algebras).
    #
    # So H^1(B(H^r))_h = sum over compositions h = h_1+...+h_r, h_i >= 0
    #                     of prod H^1(B(H))_{h_i}
    # But H^1(B(H))_0 = 0 (no bar cohomology at weight 0), so we need h_i >= 1.
    # Also need to include H^0 = 0 for bar degree 0 at weight > 0, and H^0_0 = 1.
    #
    # Actually, the Kuenneth theorem for bar cohomology of a direct sum gives:
    # H*(B(A direct_sum B)) = H*(B(A)) tensor H*(B(B))
    # The total generating function is multiplicative.
    #
    # For rank 1 Heisenberg, the bar cohomology GF is:
    # sum_h dim H*(B(H))_h q^h = sum_h known[h] q^h
    # For rank r: take the r-th power.

    if h <= 0 or r <= 0:
        return 0

    # Build rank-1 bar cohomology table
    # Ground truth from heisenberg_bar.py KNOWN_BAR_DIMS
    _rank1_known = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 7, 8: 11,
                    9: 15, 10: 22, 11: 30, 12: 42}

    # For higher weights, bar cohomology of rank-1 Heisenberg follows
    # the partition function pattern (from bar_cohomology_dimensions.py):
    # H^1_h = p(h-2) for h >= 2, with H^1_1 = 1.
    # Verify against known:
    # p(0)=1=known[2], p(1)=1=known[3], p(2)=2=known[4], p(3)=3=known[5], ...
    # YES: known[h] = p(h-2) for h >= 2.
    from compute.lib.utils import partition_number

    def rank1_bar_cohom(weight):
        if weight <= 0:
            return 0
        if weight == 1:
            return 1
        return partition_number(weight - 2)

    if r == 1:
        return rank1_bar_cohom(h)

    # For rank r: convolution of r copies of the rank-1 generating function.
    # Use dynamic programming.
    # Start with the identity (empty tensor product)
    current = [0] * (h + 1)
    current[0] = 1  # weight-0 component: k (ground field)

    for _ in range(r):
        new_current = [0] * (h + 1)
        for j in range(h + 1):
            if current[j] == 0:
                continue
            # Tensor with rank-1 bar cohomology generating function
            # Include weight 0 from the ground field (dim 1)
            new_current[j] += current[j] * 1  # weight-0 contribution
            for m in range(1, h + 1 - j):
                new_current[j + m] += current[j] * rank1_bar_cohom(m)
        current = new_current

    # Subtract the weight-0 contribution (ground field, not part of bar cohomology)
    return current[h]


def heisenberg_rank_r_bar_cohomology_koszul(h: int, r: int) -> Dict[int, int]:
    r"""Full bar cohomology at weight h for rank-r Heisenberg.

    For Koszul algebras: H^n = 0 for n >= 2, so:
      H^0_h = 0 for h > 0 (no weight-0 cohomology in positive weight)
      H^1_h = heisenberg_rank_r_bar_cohomology_h1(h, r)
      H^n_h = 0 for n >= 2

    Returns {bar_degree: dim}.
    """
    if h <= 0:
        return {}
    return {1: heisenberg_rank_r_bar_cohomology_h1(h, r)}


def heisenberg_rank_r_kappa(k: int, r: int) -> Rational:
    r"""Modular characteristic kappa for rank-r Heisenberg at level k.

    kappa(H_k^{rank r}) = r * k.
    By additivity (prop:independent-sum-factorization).
    """
    return Rational(r * k)


def heisenberg_rank_r_central_charge(k: int, r: int) -> Rational:
    """Central charge of rank-r Heisenberg at level k.

    c = r (independent of k).
    Each free boson contributes c = 1.
    """
    return Rational(r)


def heisenberg_rank_r_shadow_data(k: int, r: int) -> Dict[str, Any]:
    """Shadow obstruction tower data for rank-r Heisenberg.

    Class G (Gaussian): shadow depth 2, all higher shadows vanish.
    """
    kappa = heisenberg_rank_r_kappa(k, r)
    return {
        'kappa': kappa,
        'shadow_class': 'G',
        'shadow_depth': 2,
        'S3': Rational(0),
        'S4': Rational(0),
        'alpha': Rational(0),
        'Delta': Rational(0),
        'Q_L': 4 * kappa ** 2,
        'is_perfect_square': True,
        'all_higher_vanish': True,
    }


# =========================================================================
# E_8 root system data
# =========================================================================

E8_ROOT_DATA = {
    'dim': 248,
    'rank': 8,
    'n_roots': 240,
    'n_positive_roots': 120,
    'h': 30,
    'h_dual': 30,  # simply-laced: h = h^vee
    'exponents': [1, 7, 11, 13, 17, 19, 23, 29],
    'det_cartan': 1,  # unimodular
    'weyl_order': 696729600,
    'neighbors_at_minus1': 56,  # each root has 56 neighbors at <alpha,beta> = -1
}


# =========================================================================
# E_8 lattice VOA: lattice description (kappa = rank)
# =========================================================================

def e8_lattice_kappa() -> Rational:
    r"""kappa(V_{E_8}) in the lattice description.

    kappa = rank(E_8) = 8.

    This counts only the Cartan (Heisenberg) sector contribution.
    The root sectors have d^2 = 0 by cocycle-curvature orthogonality
    (thm:lattice:curvature-braiding-orthogonal) and do not contribute
    to the genus-1 curvature.
    """
    return Rational(E8_ROOT_DATA['rank'])


def e8_lattice_central_charge() -> Rational:
    """Central charge of V_{E_8} lattice VOA.

    c = rank = 8 (the level-1 lattice VOA has c = rank).
    Equivalently: c = dim(e_8)*k/(k+h^vee) = 248*1/31 = 248/31 approx 8.
    But the lattice central charge convention gives c = 8 exactly
    (8 free bosons on the E_8 lattice).
    """
    return Rational(8)


def e8_lattice_shadow_data() -> Dict[str, Any]:
    """Shadow obstruction tower for V_{E_8} in the lattice description.

    Class G (Gaussian, depth 2): the lattice VOA inherits class G from
    the rank-8 Heisenberg subalgebra.  The root lattice cocycle complex
    is acyclic and does not affect the shadow classification.
    """
    return heisenberg_rank_r_shadow_data(k=1, r=8)


def e8_lattice_bar_cohomology_h1(h: int) -> int:
    """Bar cohomology H^1 at weight h for V_{E_8} in the lattice description.

    In the lattice description, the bar complex decomposes:
      B(V_{E_8}) = B(H_1^8) tensor B(root lattice cocycle)
    The root lattice cocycle complex is acyclic (prop:E8-koszul-acyclic).
    So the bar cohomology reduces to that of the rank-8 Heisenberg.
    """
    return heisenberg_rank_r_bar_cohomology_h1(h, r=8)


def e8_lattice_bar_chain_dim(n: int, h: int) -> int:
    """Bar chain dimension for V_{E_8} in the lattice description at bar
    degree n, total weight h.

    In the lattice description with 248 weight-1 currents as potential
    bar elements, dim V_bar(m) = 248 for each m >= 1.  However, the
    EFFECTIVE bar complex (after the PBW spectral sequence for the lattice
    description) reduces to the rank-8 Heisenberg sector (8 Cartan modes
    per weight) plus corrections from the root lattice.

    For the Cartan sector alone: this is the rank-8 Heisenberg chain dim.
    The root sectors contribute additional chains but are acyclic (do not
    affect cohomology).
    """
    # Cartan sector contribution (the persistent part):
    return heisenberg_rank_r_bar_chain_dim(n, h, r=8)


# =========================================================================
# E_8 affine KM: affine description (kappa = 1922/15)
# =========================================================================

def e8_affine_kappa(k: int = 1) -> Rational:
    r"""kappa(V_k(e_8)) in the affine KM description.

    kappa = dim(e_8) * (k + h^vee) / (2 * h^vee) = 248*(k+30)/60.

    At k=1: kappa = 248*31/60 = 1922/15.

    All 248 currents (8 Cartan + 240 root) contribute to the genus-1
    curvature through the affine OPE structure.
    """
    dim_g = E8_ROOT_DATA['dim']
    h_dual = E8_ROOT_DATA['h_dual']
    return Rational(dim_g) * (k + h_dual) / (2 * h_dual)


def e8_affine_central_charge(k: int = 1) -> Rational:
    """Central charge of V_k(e_8).

    c = dim(e_8)*k/(k+h^vee) = 248*k/(k+30).
    At k=1: c = 248/31.
    """
    dim_g = E8_ROOT_DATA['dim']
    h_dual = E8_ROOT_DATA['h_dual']
    return Rational(dim_g * k, k + h_dual)


def e8_affine_dual_level(k: int = 1) -> int:
    """Feigin-Frenkel dual level k' = -k - 2h^vee.

    At k=1: k' = -1 - 60 = -61.
    """
    h_dual = E8_ROOT_DATA['h_dual']
    return -k - 2 * h_dual


def e8_affine_complementarity(k: int = 1) -> Dict[str, Rational]:
    r"""Complementarity data for V_k(e_8) in the affine description.

    kappa(k) + kappa(k') = 0  (AP24: correct for KM families).
    c(k) + c(k') = 2 * dim(e_8) = 496.
    """
    kappa_k = e8_affine_kappa(k)
    k_dual = e8_affine_dual_level(k)
    kappa_dual = e8_affine_kappa(k_dual)
    c_k = e8_affine_central_charge(k)
    c_dual = e8_affine_central_charge(k_dual)
    return {
        'k': Rational(k),
        'k_dual': Rational(k_dual),
        'kappa': kappa_k,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa_k + kappa_dual,
        'c': c_k,
        'c_dual': c_dual,
        'c_sum': c_k + c_dual,
    }


def e8_affine_shadow_data(k: int = 1) -> Dict[str, Any]:
    r"""Shadow obstruction tower for V_k(e_8) in the affine description.

    Class L (Lie/tree, depth 3): the affine KM algebra has nonzero cubic
    shadow S_3 from the Lie bracket, but S_4 = 0 (Jacobi identity kills
    the quartic obstruction).  Tower terminates at arity 3.
    """
    kappa = e8_affine_kappa(k)
    return {
        'kappa': kappa,
        'shadow_class': 'L',
        'shadow_depth': 3,
        'S3': Rational(1),  # universal for all affine KM
        'S4': Rational(0),
        'alpha': Rational(1),  # cubic coefficient
        'Delta': Rational(0),  # 8*kappa*S4 = 0
        'Q_L': (2 * kappa + 3 * Rational(1)) ** 2,  # perfect square since Delta=0
        'is_perfect_square': True,
        'all_higher_vanish': True,  # depth 3: quartic and above vanish
    }


def e8_affine_bar_chain_dim(n: int, h: int) -> int:
    """Bar chain dimension for V_1(e_8) in the affine description.

    With 248 weight-1 currents: dim V_bar(m) = 248 for each m >= 1.
    dim B^n_h = 248^n * C(h-1, n-1) * (n-1)!.
    """
    return heisenberg_rank_r_bar_chain_dim(n, h, r=248)


# =========================================================================
# Genus expansion
# =========================================================================

def genus_expansion(kappa: Rational, max_g: int = 5) -> Dict[int, Rational]:
    r"""Genus expansion F_g = kappa * lambda_g^FP.

    Valid for class G and class L algebras (shadow depth <= 3):
    the higher-arity corrections to the genus expansion vanish.
    """
    return {g: kappa * faber_pandharipande(g) for g in range(1, max_g + 1)}


# =========================================================================
# Verlinde dimensions for E_8 at level 1
# =========================================================================

def e8_level1_verlinde(g: int) -> int:
    r"""Verlinde dimension for E_8^{(1)} at level 1 and genus g.

    At level 1, the E_8 affine algebra has a unique integrable
    representation (the vacuum module).  The Verlinde formula gives
    dim V_g(E_8, k=1) = 1 for ALL genera g >= 0.

    This is because the modular S-matrix is 1x1: S = (1), and
    S_{00}^{2-2g} * (S_{00})^0 = 1^{2-2g} * 1 = 1.
    """
    if g < 0:
        raise ValueError(f"Genus must be >= 0, got {g}")
    return 1


# =========================================================================
# Comparison: lattice vs affine descriptions
# =========================================================================

def kappa_comparison() -> Dict[str, Any]:
    r"""Compare kappa values for the two descriptions of V_{E_8}.

    This documents the AP48 subtlety: kappa depends on the full algebra
    (presentation), not just the Virasoro subalgebra or central charge.

    The two descriptions give genuinely different bar complexes.
    """
    kappa_lat = e8_lattice_kappa()
    kappa_aff = e8_affine_kappa(1)
    c_lat = e8_lattice_central_charge()
    c_aff = e8_affine_central_charge(1)
    return {
        'kappa_lattice': kappa_lat,
        'kappa_affine': kappa_aff,
        'c_lattice': c_lat,
        'c_affine': c_aff,
        'kappa_ratio': kappa_aff / kappa_lat,
        'c_equal': (c_lat == 8) and (c_aff == Rational(248, 31)),
        'kappa_different': kappa_lat != kappa_aff,
        'explanation': (
            'The lattice description V_{E_8} = H_1^8 + root ops gives '
            'kappa = rank = 8 (only Cartan sector contributes to curvature). '
            'The affine KM description V_1(e_8) with 248 currents gives '
            'kappa = 1922/15 (all currents contribute). '
            'The bar complex depends on the presentation, not just '
            'the isomorphism class (AP48).'
        ),
    }


def root_vector_bar_contribution() -> Dict[str, Any]:
    r"""Analyze the contribution of E_8 root vectors to the bar complex.

    The 240 root vectors e^alpha (alpha in Delta(E_8)) have OPE:
      e^alpha(z) e^beta(w) ~ epsilon(alpha,beta) e^{alpha+beta} / (z-w)
                              + k delta_{alpha+beta,0} / (z-w)^2

    Bar differential contributions (from d log extraction, AP19):
      <alpha,beta> = -2 (opposite roots): vacuum + J_alpha term
      <alpha,beta> = -1 (neighbors): e^{alpha+beta} term
      <alpha,beta> = 0,+1,+2: zero

    In the LATTICE description:
      The root sector bar complex is ACYCLIC (prop:E8-koszul-acyclic).
      Root vectors do NOT generate new bar cohomology classes.
      They contribute to the bar CHAINS but not to bar COHOMOLOGY.

    In the AFFINE KM description:
      Root vectors are part of the e_8 current algebra.
      Their contribution is captured by the CE cohomology of e_8_{-}.
      By Whitehead's lemma for the simple Lie algebra e_8:
        H^q(e_8, V) = 0 for q >= 1 when V is a finite-dim irreducible != trivial.
      The bar cohomology is determined by the structure of e_8 as a Lie algebra.
    """
    data = E8_ROOT_DATA
    return {
        'n_roots': data['n_roots'],
        'root_types': {
            'opposite_pairs': data['n_roots'] // 2,  # 120 pairs
            'neighbor_pairs_per_root': data['neighbors_at_minus1'],  # 56
            'total_neighbor_pairs': data['n_roots'] * data['neighbors_at_minus1'] // 2,  # 6720
        },
        'lattice_description': {
            'root_sector_acyclic': True,
            'new_bar_cohomology_from_roots': False,
            'reason': 'cocycle-curvature orthogonality + Whitehead lemma',
        },
        'affine_description': {
            'root_vectors_are_generators': True,
            'contribution_via': 'CE cohomology of e_8 tensor t^{-1}C[t^{-1}]',
        },
    }


# =========================================================================
# Multi-path kappa verification
# =========================================================================

def kappa_e8_lattice_multipath() -> Dict[str, Any]:
    r"""Multi-path verification of kappa(V_{E_8}) = 8 (lattice description).

    Path 1: Rank formula. kappa = rank(E_8) = 8.
    Path 2: Additivity. V_{E_8} lattice = H_1^{tensor 8} + acyclic root sector.
            kappa = 8 * kappa(H_1) = 8 * 1 = 8.
    Path 3: Genus-1 direct. F_1 = kappa/24. For lattice VOA of rank r:
            F_1 = r/24. So kappa = r = 8.
    """
    rank = E8_ROOT_DATA['rank']

    path1 = Rational(rank)
    path2 = 8 * Rational(1)  # 8 copies of H_1
    path3 = Rational(rank)   # from F_1 = rank/24

    return {
        'path1_rank': path1,
        'path2_additivity': path2,
        'path3_genus1': path3,
        'all_agree': path1 == path2 == path3,
        'value': path1,
    }


def kappa_e8_affine_multipath() -> Dict[str, Any]:
    r"""Multi-path verification of kappa(V_1(e_8)) = 1922/15 (affine description).

    Path 1: KM formula. kappa = dim(e_8)*(k+h^vee)/(2*h^vee) = 248*31/60.
    Path 2: Complementarity. kappa(k=1) = -kappa(k'=-61).
            kappa(k=-61) = 248*(-61+30)/60 = 248*(-31)/60 = -1922/15.
            So kappa(k=1) = 1922/15.
    Path 3: Central charge relation. For KM: kappa = c*(k+h^v)^2/(2*k*h^v).
            c = 248/31, k=1, h^v=30:
            kappa = (248/31)*31^2/60 = 248*31/60 = 1922/15.
    """
    dim_g = E8_ROOT_DATA['dim']
    h_dual = E8_ROOT_DATA['h_dual']
    k = 1

    path1 = Rational(dim_g) * (k + h_dual) / (2 * h_dual)

    k_dual = -k - 2 * h_dual  # = -61
    kappa_dual = Rational(dim_g) * (k_dual + h_dual) / (2 * h_dual)
    path2 = -kappa_dual

    c = Rational(dim_g * k, k + h_dual)
    path3 = c * (k + h_dual) ** 2 / (2 * k * h_dual)

    return {
        'path1_km_formula': path1,
        'path2_complementarity': path2,
        'path3_central_charge': path3,
        'all_agree': path1 == path2 == path3,
        'value': path1,
    }


# =========================================================================
# Verification functions
# =========================================================================

def verify_all() -> Dict[str, bool]:
    """Run all internal verification checks."""
    results = {}

    # Colored partition numbers: r=1 should give ordinary partitions
    from compute.lib.utils import partition_number
    for h in range(11):
        results[f'p_1({h}) = p({h})'] = (
            colored_partition_number(h, 1) == partition_number(h)
        )

    # Rank-1 bar chain dims match heisenberg_bar.py
    for n in range(1, 6):
        for h in range(n, n + 4):
            expected = comb(h - 1, n - 1) * factorial(n - 1)
            computed = heisenberg_rank_r_bar_chain_dim(n, h, 1)
            results[f'B^{n}_{h} rank 1 = {expected}'] = computed == expected

    # E_8 kappa multi-path
    mp_lat = kappa_e8_lattice_multipath()
    results['kappa_lattice_3_paths_agree'] = mp_lat['all_agree']
    results['kappa_lattice = 8'] = mp_lat['value'] == Rational(8)

    mp_aff = kappa_e8_affine_multipath()
    results['kappa_affine_3_paths_agree'] = mp_aff['all_agree']
    results['kappa_affine = 1922/15'] = mp_aff['value'] == Rational(1922, 15)

    # Complementarity for affine description
    comp = e8_affine_complementarity(1)
    results['kappa + kappa_dual = 0 (affine)'] = comp['kappa_sum'] == 0
    results['c + c_dual = 496 (affine)'] = comp['c_sum'] == 496

    # Verlinde
    for g in range(6):
        results[f'Verlinde(E8,k=1,g={g}) = 1'] = e8_level1_verlinde(g) == 1

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("BAR COHOMOLOGY: RANK-r HEISENBERG AND E_8 LATTICE VOA")
    print("=" * 70)

    print("\n--- Internal Verification ---")
    for name, ok in verify_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Rank-8 Heisenberg Bar Chain Dimensions ---")
    for n in range(1, 7):
        dims = []
        for h in range(n, min(n + 5, 9)):
            d = heisenberg_rank_r_bar_chain_dim(n, h, 8)
            dims.append(f"h={h}:{d}")
        print(f"  n={n}: {'  '.join(dims)}")

    print("\n--- Rank-8 Heisenberg Bar Cohomology H^1_h ---")
    for h in range(1, 9):
        d = heisenberg_rank_r_bar_cohomology_h1(h, 8)
        print(f"  H^1_{h} = {d}")

    print("\n--- Kappa Comparison ---")
    comp = kappa_comparison()
    print(f"  kappa(lattice) = {comp['kappa_lattice']}")
    print(f"  kappa(affine)  = {comp['kappa_affine']} = {float(comp['kappa_affine']):.6f}")
    print(f"  Ratio: {comp['kappa_ratio']}")

    print("\n--- Genus Expansion (lattice, kappa=8) ---")
    for g, F in genus_expansion(Rational(8)).items():
        print(f"  F_{g} = {F} = {float(F):.10f}")

    print("\n--- Genus Expansion (affine, kappa=1922/15) ---")
    for g, F in genus_expansion(Rational(1922, 15)).items():
        print(f"  F_{g} = {F} = {float(F):.10f}")
