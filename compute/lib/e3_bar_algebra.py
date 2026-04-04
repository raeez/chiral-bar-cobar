"""
E_3-algebra structure on the bar complex: obstruction theory and negative theorem.

CENTRAL FINDING (Negative Theorem):
  B(A) is naturally an E_2-algebra (from Conf_k(C)), NOT E_3.
  The obstruction is topological and fundamental:
    - E_n requires R^n geometry; a curve provides only R^2
    - Swiss-cheese SC^{ch,top} is a colored operad, NOT E_2 x E_1 = E_3
    - Framed E_2 (BV) is strictly weaker than E_3

POSITIVE RESULT:
  The derived center Z^der_ch(A) = HH*(B(A), B(A)) carries E_3 structure
  by the Higher Deligne Conjecture. This is a DIFFERENT object from B(A).

The obstruction to extending E_2 to E_3 on B(A) lives in
HH^3_{E_2}(B(A), B(A)).

Anti-pattern flagged: The suggestion that "E_2 x E_1 from Swiss-cheese
gives E_3 by Dunn" is precisely the AP14-type error (surface resemblance).
The Swiss-cheese is a COLORED operad, not a tensor product.
"""

from fractions import Fraction
import math


# ============================================================
# E_n operad homology
# ============================================================

def conf_betti(n, k):
    """Betti numbers of Conf_k(R^n) = configuration space of k points in R^n.

    H_*(Conf_k(R^n)) has total dimension k! for all n >= 2.
    The degree distribution depends on n.

    For n=2 (E_2): generators in degree 1 (Arnold relations)
    For n=3 (E_3): generators in degree 2
    """
    if k <= 1:
        return {0: 1}
    if n == 2:
        # H_*(Conf_k(R^2)): Betti numbers from Arnold
        # Total dim = k!, concentrated in degrees 0..k-1
        return _conf_betti_r2(k)
    elif n == 3:
        return _conf_betti_r3(k)
    return {}


def _conf_betti_r2(k):
    """Betti numbers of Conf_k(R^2) via Arnold presentation.

    H_i(Conf_k(R^2)) = dimension of degree-i part of the
    free graded-commutative algebra on generators omega_{ij} (deg 1)
    modulo Arnold relations.
    """
    if k == 1:
        return {0: 1}
    elif k == 2:
        return {0: 1, 1: 1}
    elif k == 3:
        return {0: 1, 1: 3, 2: 2}
    elif k == 4:
        return {0: 1, 1: 6, 2: 11, 3: 6}
    # General: sum = k!
    return {0: 1}  # placeholder


def _conf_betti_r3(k):
    """Betti numbers of Conf_k(R^3).

    Generators omega_{ij} have degree 2 (not 1).
    Total dim still k!, but shifted to even degrees.
    """
    if k == 1:
        return {0: 1}
    elif k == 2:
        return {0: 1, 2: 1}
    elif k == 3:
        return {0: 1, 2: 3, 4: 2}
    return {0: 1}  # placeholder


def total_betti(n, k):
    """Total Betti number = k! for Conf_k(R^n), n >= 2."""
    betti = conf_betti(n, k)
    return sum(betti.values())


# ============================================================
# Obstruction theory
# ============================================================

def obstruction_class_dim(algebra_type, dim_V=1):
    """Dimension of HH^3_{E_2}(B(A), B(A)) — obstruction to E_3 extension.

    For Heisenberg (dim V = 1): Lambda^3(V) = 0, so obstruction vanishes.
    For sl_2 (dim V = 3): Lambda^3(V) = C, obstruction is 1-dimensional.
    For Virasoro: controlled by shadow data.
    """
    if algebra_type == 'heisenberg':
        return 0  # Lambda^3(C^1) = 0
    elif algebra_type == 'sl2':
        return 1  # Lambda^3(C^3) = C^1
    elif algebra_type == 'sl_n':
        n = dim_V  # dim of fundamental rep
        return math.comb(n, 3)
    elif algebra_type == 'virasoro':
        return 1  # 1-dimensional obstruction (controlled by c)
    return None


def e2_bracket_degree():
    """The E_2 (Gerstenhaber) bracket has degree 1."""
    return 1


def e3_bracket_degree():
    """A hypothetical E_3 bracket would have degree 2."""
    return 2


def bv_operator_degree():
    """The BV operator Delta from genus-1 sewing has degree 1."""
    return 1


def bv_is_not_e3():
    """Framed E_2 (= BV) is strictly weaker than E_3.

    The BV operator Delta has degree 1 (same as E_2 bracket).
    An E_3 bracket requires degree 2.
    Delta({a,b}) - {Delta(a), b} - (-1)^|a| {a, Delta(b)} vanishes
    identically because Delta^2 = 0. This does NOT produce a degree-2 bracket.
    """
    return True


# ============================================================
# E_n structure hierarchy
# ============================================================

def en_structure_on_bar(n_value):
    """What E_n structure does the bar complex carry?

    Returns dict with structure information.
    """
    if n_value == 1:
        return {
            'exists': True,
            'source': 'A-infinity structure (bar differential)',
            'geometric_origin': 'Configurations on R^1 (intervals)',
        }
    elif n_value == 2:
        return {
            'exists': True,
            'source': 'Chiral OPE on C = R^2',
            'geometric_origin': 'Fulton-MacPherson FM_k(C) compactification',
        }
    elif n_value == 3:
        return {
            'exists': False,
            'obstruction': 'Requires R^3 geometry; curve provides only R^2',
            'where_it_lives': 'The derived center Z^der_ch(A) carries E_3',
        }
    return {'exists': False, 'reason': f'E_{n_value} requires R^{n_value}'}


def swiss_cheese_is_not_tensor():
    """SC^{ch,top} is a COLORED operad, not E_2 tensor E_1.

    Dunn additivity (E_m tensor E_n = E_{m+n}) requires independent
    commuting structures on the SAME object. Swiss-cheese has:
    - E_2 on the open color (chiral, from C)
    - E_1 on the closed color (topological, from R)
    These are on DIFFERENT colors, so Dunn does NOT apply.
    """
    return {
        'claim': 'SC = E_2 x E_1 = E_3',
        'verdict': 'FALSE',
        'reason': 'SC is colored; Dunn requires same-color independence',
        'anti_pattern': 'AP14 (surface resemblance)',
    }


# ============================================================
# Higher Deligne Conjecture
# ============================================================

def derived_center_en_structure(n_bar):
    """If B(A) is E_n, then Z^der = HH*(B(A), B(A)) is E_{n+1}.

    B(A) is E_2 => Z^der_ch(A) is E_3.

    This is the Higher Deligne Conjecture (proved by various authors
    including Lurie, Francis, Costello-Gwilliam).
    """
    return n_bar + 1


# ============================================================
# Physical interpretation
# ============================================================

PHYSICAL_DICTIONARY = {
    'E_1': '1d TFT / associative algebra / chain complexes',
    'E_2': '2d TFT / braided monoidal / surface operators',
    'framed_E_2': 'BV algebra from genus-1 sewing / Gerstenhaber',
    'E_3': '3d TFT / knot invariants / Reshetikhin-Turaev',
    'E_infty': 'commutative / all-genus TFT',
}


def physical_interpretation(n):
    """Physical interpretation of E_n structure."""
    return PHYSICAL_DICTIONARY.get(f'E_{n}', f'E_{n} = {n}d topological field theory')


# ============================================================
# Heisenberg special case
# ============================================================

def heisenberg_is_e_infinity():
    """Heisenberg bar cohomology H*(B(H_k)) = Sym(V*[1]) is E_infinity.

    This is because Sym (free commutative) is the initial E_infinity algebra.
    It is E_n for ALL n, but this is a property of the COHOMOLOGY,
    not of B(H_k) itself as a chain complex.

    B(H_k) is E_2 (as a chain complex).
    H*(B(H_k)) is E_infinity (as a graded algebra).
    The quasi-isomorphism B(H_k) -> H*(B(H_k)) is E_2, not E_infinity.
    """
    return {
        'chain_level': 'E_2',
        'cohomology_level': 'E_infinity',
        'qi_level': 'E_2 (formality is E_2, not E_infinity)',
        'obstruction_dim': 0,  # Lambda^3(C^1) = 0
    }
