r"""BRST spectral sequence engine for the (3,2) nilpotent in sl_5.

The partition (3,2) of 5 is the MINIMAL non-hook partition in type A.
Its nilradical n_+ is 10-dimensional and 4-STEP NILPOTENT, with
half-integer grades from the mixed-parity Jordan blocks (sizes 3 and 2).
This makes it the decisive test for conj:ds-kd-arbitrary-nilpotent:
if the Kazhdan filtration spectral sequence degenerates at E_1, it
strongly supports the conjecture; if not, the conjecture requires
restriction or reformulation.

NILPOTENT ORBIT DATA:
  Partition: (3,2).  Transpose: (2,2,1).
  Weighted Dynkin diagram: (0, 1, 1, 0).
  Orbit dimension: 16.  Centralizer dimension: dim(g^f) = 8.
  Orbit class: two_row_nonhook.
  Hook transport (Fehily, CLNS) does NOT apply.

ROOT SYSTEM OF sl_5:
  Simple roots: alpha_1, alpha_2, alpha_3, alpha_4.
  Positive roots: 10 = C(5,2) roots e_i - e_j for 1 <= i < j <= 5.
  Cartan matrix: standard A_4.

DYNKIN GRADING (ad(h/2)-eigenvalue decomposition of sl_5):
  The sl_2-triple (e, h, f) for partition (3,2) has
    h = diag(2, 0, -2, 1, -1) in blocks diag(diag(2,0,-2), diag(1,-1))
  so x = h/2 = (1, 0, -1, 1/2, -1/2) and grade(E_{ij}) = x_i - x_j.

  The grading has HALF-INTEGER grades because the Jordan blocks have
  different parities (sizes 3 and 2).  Root space decomposition:

  Grade -2:   1 root space   (E_{31})
  Grade -3/2: 2 root spaces  (E_{34}, E_{51})
  Grade -1:   3 root spaces  (E_{21}, E_{32}, E_{54})
  Grade -1/2: 4 root spaces  (E_{24}, E_{35}, E_{41}, E_{52})
  Grade  0:   0 root spaces  + 4 Cartan = 4-dim
  Grade +1/2: 4 root spaces  (E_{14}, E_{25}, E_{42}, E_{53})
  Grade +1:   3 root spaces  (E_{12}, E_{23}, E_{45})
  Grade +3/2: 2 root spaces  (E_{15}, E_{43})
  Grade +2:   1 root space   (E_{13})

  Total root spaces: 1+2+3+4+0+4+3+2+1 = 20.  With Cartan: 20+4 = 24.

n_+ STRUCTURE (10-dimensional, 4-step nilpotent):
  n_+^{1/2} (grade 1/2, 4-dim): E_{14}, E_{25}, E_{42}, E_{53}
  n_+^{1}   (grade 1,   3-dim): E_{12}, E_{23}, E_{45}
  n_+^{3/2} (grade 3/2, 2-dim): E_{15}, E_{43}
  n_+^{2}   (grade 2,   1-dim): E_{13}

  10 non-trivial brackets within n_+, including:
    [E_{14}, E_{42}] = E_{12}  (grade 1/2 + 1/2 -> 1)
    [E_{12}, E_{23}] = E_{13}  (grade 1 + 1 -> 2)
    [E_{14}, E_{43}] = E_{13}  (grade 1/2 + 3/2 -> 2)
    [E_{14}, E_{45}] = E_{15}  (grade 1/2 + 1 -> 3/2)
    etc.
  n_+ is 4-step nilpotent: [n_+, [n_+, [n_+, n_+]]] != 0 but
  the next iterated bracket vanishes (grade 5/2 is empty).

  NOTE: The feasibility report (brst_sl5_32_feasibility.md) incorrectly
  claimed dim(n_+) = 8 and 2-step nilpotency.  That analysis ignored
  half-integer grades from the mixed-parity Jordan blocks.  The correct
  values are dim(n_+) = 10 and nilpotency step 4.

BRST CHARGE DECOMPOSITION:
  Q_DS = Q_st + Q_gh
  Q_st: standard Koszul part (contracts n_+ generators against antighosts).
  Q_gh: ghost-ghost part encoding the 10 non-trivial brackets in n_+.
        Each term has the form f^{ij}_{pq,rs} c_pq c_rs b_ij.
  Both Q_st and Q_gh have Kazhdan filtration degree 0.

GHOST SYSTEM:
  10 bc-ghost pairs, one per root in n_+.
  Grade 1/2 ghosts: 4 pairs, b weight 1/2, c weight 1/2.
  Grade 1 ghosts:   3 pairs, b weight 0,   c weight 1.
  Grade 3/2 ghosts: 2 pairs, b weight -1/2, c weight 3/2.
  Grade 2 ghosts:   1 pair,  b weight -1,  c weight 2.
  Ghost number ranges from -10 to +10 (21 sectors).

W-ALGEBRA GENERATORS (from g^f, 8-dimensional):
  h=1:   1 bosonic   (J)
  h=3/2: 2 fermionic (G+, G-)
  h=2:   2 bosonic   (T, W2)
  h=5/2: 2 fermionic (G+', G-')
  h=3:   1 bosonic   (W3)
  Total: 4 bosonic + 4 fermionic = 8 strong generators.

CENTRAL CHARGE:
  c(3,2; k) = 2 - 108/(k+5) = 2(k - 49)/(k + 5).

References:
    Kac-Roan-Wakimoto (2003): quantum DS reduction for arbitrary nilpotent
    Fehily (2022): hook-type inverse reduction (does NOT cover (3,2))
    Manuscript: conj:ds-kd-arbitrary-nilpotent, rem:abelian-nonabelian-nilradical
    Feasibility: compute/audit/brst_sl5_32_feasibility.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, Symbol, simplify, sympify, zeros

# Import orbit data from canonical engine (single source of truth, AAP3).
from compute.lib.nonprincipal_ds_orbits import (
    centralizer_dimension_sl_n,
    is_hook_partition,
    normalize_partition,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)


k = Symbol('k')

# ============================================================================
# Constants
# ============================================================================

PARTITION = (3, 2)
PARTITION_T = (2, 2, 1)
N = 5
H_DUAL = 5  # dual Coxeter number of sl_5
WEIGHTED_DYNKIN = (0, 1, 1, 0)

# sl_5 root system data.
# Simple roots alpha_i = e_i - e_{i+1}, i = 1..4.
# Positive roots: e_i - e_j for 1 <= i < j <= 5.
NUM_SIMPLE_ROOTS = N - 1  # = 4
NUM_POSITIVE_ROOTS = N * (N - 1) // 2  # = 10
DIM_SL5 = N * N - 1  # = 24

# Cartan matrix for A_4 (sl_5).
CARTAN_MATRIX = (
    (2, -1, 0, 0),
    (-1, 2, -1, 0),
    (0, -1, 2, -1),
    (0, 0, -1, 2),
)


# ============================================================================
# 1. Root system of sl_5
# ============================================================================

def positive_roots_sl5() -> List[Tuple[int, int]]:
    """All positive roots of sl_5 as pairs (i, j) with 1 <= i < j <= 5.

    Each pair (i, j) represents the root e_i - e_j.
    Returns 10 = C(5, 2) roots.
    """
    return [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)]


def simple_roots_sl5() -> List[Tuple[int, int]]:
    """Simple roots alpha_i = e_i - e_{i+1} for i = 1..4."""
    return [(i, i + 1) for i in range(1, N)]


def root_height(root: Tuple[int, int]) -> int:
    """Height of the root e_i - e_j in the simple root basis.

    height(e_i - e_j) = j - i.
    """
    return root[1] - root[0]


# ============================================================================
# 2. Dynkin grading for partition (3,2)
# ============================================================================

def sl2_triple_diagonal() -> Tuple[int, ...]:
    """Diagonal entries of h in the sl_2-triple for partition (3,2).

    For partition (3,2), the Jordan blocks have sizes 3 and 2.
    Block of size 3: eigenvalues 2, 0, -2.
    Block of size 2: eigenvalues 1, -1.
    So h = diag(2, 0, -2, 1, -1).

    Returns the tuple (2, 0, -2, 1, -1).
    """
    # Standard convention: within each Jordan block of size p,
    # the eigenvalues are p-1, p-3, ..., -(p-1).
    # Block of size 3: 2, 0, -2
    # Block of size 2: 1, -1
    return (2, 0, -2, 1, -1)


def half_grading_values() -> Tuple[Rational, ...]:
    """ad(h/2)-eigenvalues x_i = h_i / 2 for each basis index.

    Returns (1, 0, -1, 1/2, -1/2).
    """
    h_diag = sl2_triple_diagonal()
    return tuple(Rational(h, 2) for h in h_diag)


def dynkin_grade_of_root(i: int, j: int) -> Rational:
    """ad(h/2)-eigenvalue of the root space E_{ij} (1-indexed).

    grade(E_{ij}) = x_i - x_j where x = h/2.
    """
    x = half_grading_values()
    return x[i - 1] - x[j - 1]


def grading_decomposition() -> Dict[Rational, List[Tuple[int, int]]]:
    """Full ad(h/2)-grading decomposition of sl_5 root spaces.

    Returns dict mapping grade -> list of root spaces (i, j) at that grade.
    Includes both positive and negative roots but NOT Cartan elements.
    """
    decomp: Dict[Rational, List[Tuple[int, int]]] = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            g = dynkin_grade_of_root(i, j)
            decomp.setdefault(g, []).append((i, j))
    return decomp


def grade_dimensions() -> Dict[Rational, int]:
    """Dimensions of each graded piece g_j (root spaces only, excluding Cartan).

    For the (3,2) grading, expected:
      grade -2: 4, grade -1: 4, grade 0: 4 (root spaces),
      grade +1: 4, grade +2: 4.
    Cartan is always in grade 0 and contributes 4 more to dim(g_0).
    """
    decomp = grading_decomposition()
    return {g: len(roots) for g, roots in decomp.items()}


# ============================================================================
# 3. n_+ basis and structure
# ============================================================================

def n_plus_basis() -> List[Tuple[int, int]]:
    """Basis of n_+ = direct sum of positive-grade root spaces.

    For partition (3,2) in sl_5, the grading has half-integer grades:
      n_+^{1/2} (grade 1/2, 4-dim): E_{14}, E_{25}, E_{42}, E_{53}
      n_+^{1}   (grade 1,   3-dim): E_{12}, E_{23}, E_{45}
      n_+^{3/2} (grade 3/2, 2-dim): E_{15}, E_{43}
      n_+^{2}   (grade 2,   1-dim): E_{13}
    Total dim(n_+) = 10.

    Returns list of (i, j) pairs (1-indexed) with grade > 0, sorted by grade.
    """
    decomp = grading_decomposition()
    basis = []
    for g in sorted(decomp.keys()):
        if g > 0:
            basis.extend(sorted(decomp[g]))
    return basis


def n_plus_grade_decomposition() -> Dict[Rational, List[Tuple[int, int]]]:
    """Grade decomposition of n_+ (positive-grade root spaces only).

    Returns dict mapping positive grade -> list of root spaces.
    """
    decomp = grading_decomposition()
    return {g: sorted(roots) for g, roots in decomp.items() if g > 0}


def n_plus_dimension() -> int:
    """Dimension of n_+.

    For (3,2) in sl_5: dim(n_+) = 10.
    (4 at grade 1/2) + (3 at grade 1) + (2 at grade 3/2) + (1 at grade 2).
    """
    return len(n_plus_basis())


def n_plus_is_abelian() -> bool:
    """Check whether n_+ is abelian.

    n_+ is abelian iff no bracket of two positive-grade elements lands
    in n_+ (all products exceed the max grade).
    For (3,2): n_+ has grades 1/2, 1, 3/2, 2, and many brackets land
    within n_+ (e.g., [n_+^{1/2}, n_+^{1/2}] lands at grade 1),
    so n_+ is NON-ABELIAN.
    """
    grades = n_plus_grade_decomposition()
    if len(grades) <= 1:
        return True
    # Check if any bracket of grade-g1 and grade-g2 elements lands in n_+.
    max_grade = max(grades.keys())
    for g1 in grades:
        for g2 in grades:
            if g1 + g2 <= max_grade and g1 + g2 > 0:
                # Potential non-trivial bracket at grade g1 + g2.
                # Check if any [E_{ij}, E_{kl}] = delta_{jk} E_{il} is nonzero
                # with grade(E_{ij}) = g1 and grade(E_{kl}) = g2.
                for (i, j) in grades[g1]:
                    for (kk, l) in grades[g2]:
                        if j == kk and i != l:
                            return False
    return True


def n_plus_nilpotency_step() -> int:
    """Nilpotency step of n_+.

    Returns r such that n_+^{(r)} = 0 but n_+^{(r-1)} != 0,
    where n_+^{(1)} = n_+, n_+^{(k+1)} = [n_+, n_+^{(k)}].

    For (3,2): n_+ is 2-step nilpotent ([n_+^1, n_+^1] = n_+^2,
    [n_+, n_+^2] = 0 since grade 3 is empty).
    """
    grades = n_plus_grade_decomposition()
    max_grade = max(grades.keys())
    # The nilpotency step equals the number of distinct positive grades,
    # since each bracket raises the grade by at least 1.
    return len(grades)


def n_plus_brackets() -> List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    """Non-trivial brackets [E_{ij}, E_{kl}] = E_{il} within n_+.

    Returns list of ((i,j), (k,l), (i,l)) triples where
    [E_{ij}, E_{kl}] = E_{il} with j == k, i != l, and all three
    root spaces lie in n_+.

    For (3,2) in sl_5, there are exactly 10 such brackets, including:
      [E_{14}, E_{42}] = E_{12}  (grade 1/2 + 1/2 -> 1)
      [E_{12}, E_{23}] = E_{13}  (grade 1 + 1 -> 2)
      [E_{14}, E_{43}] = E_{13}  (grade 1/2 + 3/2 -> 2)
      [E_{14}, E_{45}] = E_{15}  (grade 1/2 + 1 -> 3/2)
    The full list is computed dynamically from the grading.
    """
    n_plus = set(n_plus_basis())
    brackets = []
    for (i, j) in n_plus:
        for (kk, l) in n_plus:
            if j == kk and i != l and (i, l) in n_plus:
                brackets.append(((i, j), (kk, l), (i, l)))
    return brackets


# ============================================================================
# 4. Ghost system
# ============================================================================

@dataclass(frozen=True)
class GhostPair:
    """A bc-ghost pair for one root in n_+."""
    root: Tuple[int, int]       # the n_+ root this ghost pair corresponds to
    grade: Rational             # ad(h/2)-grade of the root
    b_weight: Rational          # conformal weight of b (antighost)
    c_weight: Rational          # conformal weight of c (ghost)
    label: str                  # human-readable label


def ghost_basis() -> List[GhostPair]:
    """Ghost pairs for the BRST complex of (3,2) in sl_5.

    One bc-ghost pair per root in n_+.  The conformal weights are:
      For a root at grade j: c has weight j, b has weight 1 - j.

    Grade 1/2 ghosts (4 pairs): b weight 1/2, c weight 1/2.
    Grade 1 ghosts   (3 pairs): b weight 0,   c weight 1.
    Grade 3/2 ghosts (2 pairs): b weight -1/2, c weight 3/2.
    Grade 2 ghosts   (1 pair):  b weight -1,   c weight 2.

    Total: 10 ghost pairs. Ghost number ranges from -10 to +10 (21 sectors).
    """
    grades = n_plus_grade_decomposition()
    pairs = []
    for g in sorted(grades.keys()):
        for root in grades[g]:
            i, j = root
            pairs.append(GhostPair(
                root=root,
                grade=g,
                b_weight=1 - g,
                c_weight=g,
                label=f'bc_{{{i}{j}}}',
            ))
    return pairs


def ghost_number_range() -> Tuple[int, int]:
    """Range of ghost numbers in the BRST complex.

    Ghost number p ranges from -N_gh to +N_gh where N_gh = dim(n_+).
    For (3,2): p in [-10, +10], giving 21 sectors.
    """
    n_gh = n_plus_dimension()
    return (-n_gh, n_gh)


def num_ghost_sectors() -> int:
    """Number of ghost-number sectors.

    For (3,2): 2 * 10 + 1 = 21 sectors.
    """
    lo, hi = ghost_number_range()
    return hi - lo + 1


# ============================================================================
# 5. BRST differential -- SCAFFOLD (not yet implemented)
# ============================================================================

def brst_differential_q_st(delta: int, ghost_num: int):
    """Standard Koszul part Q_st of the BRST differential.

    Q_st contracts n_+ generators against antighosts: it is the standard
    Chevalley-Eilenberg differential for the Lie algebra n_+ acting on
    V_k(sl_5) tensored with the ghost Fock space.

    At conformal weight delta and ghost number ghost_num, Q_st is a
    finite-dimensional matrix.

    Parameters
    ----------
    delta : int
        Conformal weight (non-negative integer).
    ghost_num : int
        Ghost number (integer in [-10, +10]).

    Returns
    -------
    Matrix
        The matrix of Q_st at the given (delta, ghost_num).
    """
    raise NotImplementedError(
        f"Q_st at (Delta={delta}, p={ghost_num}): requires building the "
        f"PBW Fock space basis at weight {delta} and assembling the "
        f"Chevalley-Eilenberg contraction matrix. See feasibility report "
        f"Phase 2 for the algorithm."
    )


def brst_differential_q_gh(delta: int, ghost_num: int):
    """Ghost-ghost part Q_gh of the BRST differential.

    Q_gh encodes the non-abelian bracket structure of n_+.
    It consists of 10 terms, each of the form
      f^{ij}_{pq,rs} c_{pq} c_{rs} b_{ij}
    corresponding to the 10 non-trivial brackets within n_+.

    The structure constants are all +/- 1 (standard sl_N normalization).

    Parameters
    ----------
    delta : int
        Conformal weight.
    ghost_num : int
        Ghost number.

    Returns
    -------
    Matrix
        The matrix of Q_gh at the given (delta, ghost_num).
    """
    raise NotImplementedError(
        f"Q_gh at (Delta={delta}, p={ghost_num}): requires assembling "
        f"the 10 cubic ghost terms from the n_+ brackets. Each term "
        f"is bilinear in c-ghosts and linear in a b-ghost. "
        f"See feasibility report Phase 2."
    )


def brst_differential(delta: int, ghost_num: int):
    """Full BRST differential Q = Q_st + Q_gh.

    Parameters
    ----------
    delta : int
        Conformal weight.
    ghost_num : int
        Ghost number.

    Returns
    -------
    Matrix
        The BRST matrix at (delta, ghost_num).
    """
    raise NotImplementedError(
        f"Full BRST Q at (Delta={delta}, p={ghost_num}): assemble as "
        f"Q_st + Q_gh after implementing both components."
    )


# ============================================================================
# 6. Kazhdan filtration
# ============================================================================

def kazhdan_filtration_data() -> Dict[str, object]:
    """Kazhdan filtration data for the (3,2) BRST complex.

    The Kazhdan filtration on V_k(sl_5) is defined by:
      F^p = span of PBW monomials with Kazhdan degree >= p,
    where Kazhdan degree of J^a_n is:
      deg_K(J^a_n) = max(0, -n) + grade(a).

    Key structural point for (3,2):
      Both Q_st and Q_gh have Kazhdan filtration degree 0.
      Therefore d_0 = Q_st + Q_gh on the associated graded.
      The spectral sequence question is whether H*(d_0) gives the
      W-algebra at each conformal weight.

    Returns dict with filtration metadata.
    """
    return {
        'partition': PARTITION,
        'max_grade': 2,
        'num_filtration_layers': 5,  # grades 0, 1/2, 1, 3/2, 2
        'q_st_filtration_degree': 0,
        'q_gh_filtration_degree': 0,
        'd_0_is_full_brst': True,
        'note': (
            'Since both Q_st and Q_gh have Kazhdan filtration degree 0, '
            'the leading differential d_0 on gr_K is the FULL BRST '
            'differential. For abelian n_+, Q_gh = 0 and d_0 = Q_st is '
            'the standard Koszul differential with automatic E_1 degeneration. '
            'For this non-abelian case, E_1 degeneration is the central question.'
        ),
    }


def kazhdan_filtration():
    """Build the explicit Kazhdan filtration on the BRST complex.

    This requires constructing the PBW basis with Kazhdan degree
    bookkeeping and decomposing by filtration layers.

    Returns
    -------
    object
        Filtration data structure.
    """
    raise NotImplementedError(
        "Kazhdan filtration construction: requires PBW basis with "
        "Kazhdan degree tracking. See feasibility report, Phase 1."
    )


# ============================================================================
# 7. Spectral sequence
# ============================================================================

def spectral_sequence_e1_page(delta: int):
    """Compute the E_1 page of the Kazhdan spectral sequence at weight delta.

    E_1^{p,q} = H^{p+q}(gr_K^p, d_0) at conformal weight delta.

    Since d_0 = Q_st + Q_gh for the (3,2) case (both components have
    Kazhdan degree 0), E_1 is the cohomology of the full BRST differential
    on the associated graded of the Kazhdan filtration.

    If the spectral sequence degenerates at E_1 (i.e., E_1 = E_infty),
    then the BRST cohomology at ghost number 0 gives the W-algebra
    W^k(sl_5, f_{(3,2)}).

    Expected dimensions at ghost number 0 (from generator spectrum):
      delta=0: 1 (vacuum)
      delta=1: 1 (J current)
      delta=2: 3 (T + 2 bosonic generators)
      delta=3: 2 (highest bosonic generator + descendant)

    Parameters
    ----------
    delta : int
        Conformal weight.

    Returns
    -------
    dict
        Mapping ghost_number -> dim(E_1) at that ghost number and weight.
    """
    raise NotImplementedError(
        f"E_1 page at Delta={delta}: requires computing ker(Q)/im(Q) "
        f"at each ghost number sector. See feasibility report Phase 3. "
        f"Matrix sizes at ghost# 0: ~1 (Delta=0), ~30-50 (Delta=1), "
        f"~200-400 (Delta=2), ~1000-3000 (Delta=3)."
    )


def w_algebra_character_prediction() -> Dict[int, Dict[str, int]]:
    """Expected BRST cohomology dimensions from the W-algebra character.

    If the BRST spectral sequence degenerates at E_1, the ghost-number-0
    cohomology should match these dimensions at each conformal weight.

    Returns dict mapping conformal weight -> {ghost_num: expected_dim}.
    Only ghost number 0 (where the W-algebra lives) is listed.
    """
    return {
        0: {0: 1},   # vacuum
        1: {0: 1},   # J current
        2: {0: 3},   # T + 2 bosonic generators
        3: {0: 2},   # W3 highest bosonic + 1 descendant of T
    }


# ============================================================================
# 8. Central charge (from canonical engine)
# ============================================================================

def central_charge(level=None):
    """Central charge c(3,2; k) = 2 - 108/(k+5) = 2(k-49)/(k+5).

    Uses the KRW formula from the canonical hook_type_w_duality engine.
    """
    from compute.lib.hook_type_w_duality import krw_central_charge
    if level is None:
        level = k
    return krw_central_charge(PARTITION, sympify(level))
