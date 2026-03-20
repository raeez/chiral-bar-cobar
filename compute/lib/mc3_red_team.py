"""RED TEAM attack on conj:mc3-arbitrary-type.

OBJECTIVE: Enumerate every gap, weakness, and potential failure point in the
path from the type-A proof (thm:mc3-type-a-resolution) to arbitrary simple type.

THE TYPE-A PROOF USES FOUR PACKAGES:
  (i)   Baxter exact triangles from prefundamental CG closure
  (ii)  Shifted-prefundamental generation of compact objects
  (iii) Pro-Weyl recovery via Mittag-Leffler
  (iv)  DK on compacts, extended by Francis-Gaitsgory completion

ATTACK VECTORS (type-by-type):

A. SHORT ROOTS (B_n, C_n, F_4, G_2):
   Non-simply-laced types have two root lengths. The prefundamental L^-_i
   associated to a SHORT simple root alpha_i has a different infinite product
   formula: the relevant positive roots include roots of different lengths.
   The Baxter TQ relation uses the FUNDAMENTAL representations, but for
   short-root nodes the fundamental V_{omega_i} is NOT a minuscule rep
   (e.g., B_n: omega_1 is the vector rep, a short root, with dim 2n+1).
   The CG splitting V_{omega_i} x L^-_i -> bigoplus L^-_i(shifted) at the
   MODULE level (not just K_0) requires knowing Ext^1(L^-_i(a), L^-_i(b)) = 0
   for generic a, b. For short-root nodes, the Ext computation is HARDER
   because the relevant roots contain both short and long roots.

B. SPINOR REPRESENTATIONS (B_n, D_n):
   Types B_n and D_n have spinor representations attached to the end node(s).
   For B_n: omega_n is the spin rep (dim 2^n).
   For D_n: omega_{n-1}, omega_n are half-spin reps (dim 2^{n-1}).
   These are NOT obtainable as direct summands of tensor powers of the vector
   representation omega_1. The evaluation core identification
   (thm:eval-core-identification in type A) uses the fact that ALL fundamental
   reps are exterior powers of the standard rep. For B/D, this FAILS for
   spinor nodes: omega_n (B) and omega_{n-1}, omega_n (D) are not in
   Lambda^*(omega_1). So the "evaluation core" step (Step 1 of the type-A
   proof) must use a DIFFERENT generator set.

C. EXCEPTIONAL TYPES (E_6, E_7, E_8):
   No "standard" small representation to tensor with. The minimal
   representations have dimension 27 (E_6), 56 (E_7), 248 (E_8 adjoint).
   The Kostant multiplicity formula and Weyl group computations become
   vastly more expensive. More critically: the evaluation map
   Y(g) -> U(g) sends Yangian modules to g-modules, and for exceptional
   types the representation theory of the evaluation image is much less
   controlled. In particular, there is no analogue of "exterior powers of
   the standard rep generate everything" for E_8.

D. MINUSCULE SCARCITY:
   Minuscule representations (those with a single Weyl orbit of weights) are
   the simplest for CG decomposition. The count by type:
     A_n: n minuscule (all fundamental weights)
     B_n: 1 minuscule (omega_1, the vector rep)
     C_n: 1 minuscule (omega_n, but this is 2n-dimensional)
     D_n: 3 minuscule (omega_1, omega_{n-1}, omega_n)
     E_6: 2 minuscule (omega_1, omega_6)
     E_7: 1 minuscule (omega_7, dim 56)
     E_8: 0 minuscule (NONE!)
     F_4: 0 minuscule (NONE!)
     G_2: 0 minuscule (NONE!)
   For types with no minuscule reps, the CG decomposition at the module
   level is structurally harder: there are weight multiplicities > 1 in
   every nontrivial representation.

E. K_0-TO-MODULE GAP SCALING:
   The obstruction dimension delta_N(k) = p_N(k) - 1 where p_N is the
   N-colored partition function grows MUCH faster for higher rank:
     sl_2: delta(k) ~ exp(pi*sqrt(2k/3)) / (4*sqrt(3)*k)
     sl_N: delta_N(k) ~ C_N * exp(pi*sqrt(2Nk/3)) / k^{...}
   For exceptional types with rank 8 (E_8), this growth is astronomical.
   The K_0+Ext pincer attack (from MC3-RED swarm) shows that categorical
   splitting requires controlling Ext^1 whose dimension scales with delta.

F. HERNANDEZ-JIMBO PREFUNDAMENTAL CONSTRUCTION:
   For type A, the prefundamental L^-_i is constructed via:
     - Jimbo's q-analog + limit q -> 1 (HJ12, Thm 3.8)
     - Universal property: unique irreducible in a certain asymptotic category
   For non-type-A, Hernandez-Jimbo (2012, Section 5) EXTENDS the
   construction, but the proof uses DIFFERENT methods:
     - For simply-laced (ADE): Nakajima quiver variety construction
     - For non-simply-laced (BCFG): folding from simply-laced type
   The folding construction introduces an outer automorphism group action,
   and the character formula picks up a Langlands dual twist. This means
   the prefundamental for B_n comes from folding A_{2n-1}, introducing
   non-trivial fixed-point issues at the categorical level.

G. OUTER AUTOMORPHISM / SPINOR PARITY (D_n):
   D_n has an outer automorphism sigma swapping omega_{n-1} <-> omega_n.
   This introduces a Z/2 grading on the Yangian representation category.
   The half-spin prefundamentals L^-_{n-1} and L^-_n are SWAPPED by sigma.
   The CG decomposition must respect this grading, which means the
   exact-triangle lifts for the two spin nodes are NOT independent but
   linked by the outer automorphism. This is an additional categorical
   constraint not present in type A.

H. ESCAPE ROUTES:
   Even if the direct CG-splitting approach fails, the conjecture could be
   true via fundamentally different proof strategies:
   1. RTT realization: R-matrix approach (Faddeev-Reshetikhin-Takhtajan)
      gives a uniform Yangian presentation for all types. The R-matrix
      CG could bypass the prefundamental splitting.
   2. Maulik-Okounkov approach: geometric R-matrix from Nakajima varieties,
      uniform for ADE types (but NOT for non-simply-laced types without
      folding).
   3. Coulomb branch approach: BDGH construction gives Yangian as
      endomorphisms of a Coulomb branch, uniform for all types.
   Each escape route has its own gaps that we identify.

References:
  - Hernandez-Jimbo 2012, Section 5 (prefundamental for all types)
  - Hernandez 2006 (Kirillov-Reshetikhin modules and folding)
  - Nakajima 2004 (quiver varieties and crystals)
  - Maulik-Okounkov 2019 (quantum groups and quantum cohomology)
  - Braverman-Finkelberg-Nakajima 2019 (Coulomb branches)
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Dict, List, Tuple, Optional

from compute.lib.utils import partition_number


# ============================================================================
#  Dynkin diagram data for all simple types
# ============================================================================

# Cartan matrices for all rank-2 simple types + higher-rank data
CARTAN_MATRICES = {
    "A1": [[2]],
    "A2": [[2, -1], [-1, 2]],
    "A3": [[2, -1, 0], [-1, 2, -1], [0, -1, 2]],
    "A4": [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]],
    "B2": [[2, -1], [-2, 2]],
    "B3": [[2, -1, 0], [-1, 2, -1], [0, -2, 2]],
    "C2": [[2, -2], [-1, 2]],   # C_2 = B_2 transposed (Langlands dual)
    "C3": [[2, -1, 0], [-1, 2, -2], [0, -1, 2]],
    "D4": [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]],
    "D5": [[2, -1, 0, 0, 0], [-1, 2, -1, 0, 0], [0, -1, 2, -1, -1],
            [0, 0, -1, 2, 0], [0, 0, -1, 0, 2]],
    "G2": [[2, -1], [-3, 2]],
    "F4": [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]],
    "E6": [[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, -1],
            [0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 2]],
    "E7": [[2, -1, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0],
            [0, -1, 2, -1, 0, 0, -1], [0, 0, -1, 2, -1, 0, 0],
            [0, 0, 0, -1, 2, -1, 0], [0, 0, 0, 0, -1, 2, 0],
            [0, 0, -1, 0, 0, 0, 2]],
    "E8": [[2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0],
            [0, -1, 2, -1, 0, 0, 0, -1], [0, 0, -1, 2, -1, 0, 0, 0],
            [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0],
            [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 0, 0, 2]],
}

# Root system classification data
DYNKIN_DATA = {
    "A1": {"rank": 1, "n_positive_roots": 1, "weyl_order": 2, "coxeter": 2,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 1, "minuscule_nodes": [0]},
    "A2": {"rank": 2, "n_positive_roots": 3, "weyl_order": 6, "coxeter": 3,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 2, "minuscule_nodes": [0, 1]},
    "A3": {"rank": 3, "n_positive_roots": 6, "weyl_order": 24, "coxeter": 4,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 3, "minuscule_nodes": [0, 1, 2]},
    "A4": {"rank": 4, "n_positive_roots": 10, "weyl_order": 120, "coxeter": 5,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 4, "minuscule_nodes": [0, 1, 2, 3]},
    "B2": {"rank": 2, "n_positive_roots": 4, "weyl_order": 8, "coxeter": 4,
            "simply_laced": False, "has_spinor": True,
            "n_minuscule": 1, "minuscule_nodes": [0],
            "short_root_nodes": [0], "long_root_nodes": [1],
            "spinor_nodes": [1]},
    "B3": {"rank": 3, "n_positive_roots": 9, "weyl_order": 48, "coxeter": 6,
            "simply_laced": False, "has_spinor": True,
            "n_minuscule": 1, "minuscule_nodes": [0],
            "short_root_nodes": [0], "long_root_nodes": [1, 2],
            "spinor_nodes": [2]},
    "C2": {"rank": 2, "n_positive_roots": 4, "weyl_order": 8, "coxeter": 4,
            "simply_laced": False, "has_spinor": False,
            "n_minuscule": 1, "minuscule_nodes": [1],
            "short_root_nodes": [1], "long_root_nodes": [0]},
    "C3": {"rank": 3, "n_positive_roots": 9, "weyl_order": 48, "coxeter": 6,
            "simply_laced": False, "has_spinor": False,
            "n_minuscule": 1, "minuscule_nodes": [2],
            "short_root_nodes": [2], "long_root_nodes": [0, 1]},
    "D4": {"rank": 4, "n_positive_roots": 12, "weyl_order": 192, "coxeter": 6,
            "simply_laced": True, "has_spinor": True,
            "n_minuscule": 3, "minuscule_nodes": [0, 2, 3],
            "spinor_nodes": [2, 3],
            "outer_automorphism_order": 6,  # S_3 triality
            "vector_node": 0},
    "D5": {"rank": 5, "n_positive_roots": 20, "weyl_order": 1920, "coxeter": 8,
            "simply_laced": True, "has_spinor": True,
            "n_minuscule": 3, "minuscule_nodes": [0, 3, 4],
            "spinor_nodes": [3, 4],
            "outer_automorphism_order": 2,
            "vector_node": 0},
    "G2": {"rank": 2, "n_positive_roots": 6, "weyl_order": 12, "coxeter": 6,
            "simply_laced": False, "has_spinor": False,
            "n_minuscule": 0, "minuscule_nodes": [],
            "short_root_nodes": [0], "long_root_nodes": [1]},
    "F4": {"rank": 4, "n_positive_roots": 24, "weyl_order": 1152, "coxeter": 12,
            "simply_laced": False, "has_spinor": False,
            "n_minuscule": 0, "minuscule_nodes": [],
            "short_root_nodes": [2, 3], "long_root_nodes": [0, 1]},
    "E6": {"rank": 6, "n_positive_roots": 36, "weyl_order": 51840, "coxeter": 12,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 2, "minuscule_nodes": [0, 4]},
    "E7": {"rank": 7, "n_positive_roots": 63, "weyl_order": 2903040, "coxeter": 18,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 1, "minuscule_nodes": [5]},
    "E8": {"rank": 8, "n_positive_roots": 120, "weyl_order": 696729600, "coxeter": 30,
            "simply_laced": True, "has_spinor": False,
            "n_minuscule": 0, "minuscule_nodes": []},
}

# Fundamental representation dimensions
FUNDAMENTAL_DIMS = {
    "A1": [2],
    "A2": [3, 3],
    "A3": [4, 6, 4],
    "A4": [5, 10, 10, 5],
    "B2": [5, 4],       # vector (5), spin (4)
    "B3": [7, 21, 8],   # vector (7), adjoint (21), spin (8)
    "C2": [4, 5],       # standard (4), 5-dim
    "C3": [6, 14, 14],  # standard (6)
    "D4": [8, 28, 8, 8],   # vector (8), adjoint (28), half-spin (8), half-spin (8)
    "D5": [10, 45, 16, 16, 120],  # approximate; see below
    "G2": [7, 14],
    "F4": [52, 1274, 273, 26],  # dims of fundamental reps
    "E6": [27, 351, 2925, 351, 27, 78],  # approx: 27, 351, ...
    "E7": [133, 912, 8645, 365750, 27664, 1539, 56],
    "E8": [248, 30380, 2450240, 146325270, 6696000, 6899079264, 147250, 3875],
}

# Correct some E-type dims (minimal reps)
FUNDAMENTAL_DIMS["D5"] = [10, 45, 120, 16, 16]
FUNDAMENTAL_DIMS["E6"] = [27, 78, 2925, 351, 27, 351]  # standard ordering
FUNDAMENTAL_DIMS["E7"] = [133, 912, 8645, 365750, 27664, 1539, 56]
FUNDAMENTAL_DIMS["E8"] = [248, 30380, 2450240, 146325270, 6696000, 6899079264, 147250, 3875]

# Folding relations: non-simply-laced as folding of simply-laced
FOLDING_DATA = {
    "B2": {"parent": "A3", "fold_automorphism": "Z/2"},
    "B3": {"parent": "A5", "fold_automorphism": "Z/2"},
    "C2": {"parent": "D3", "fold_automorphism": "Z/2"},  # D3 = A3
    "C3": {"parent": "D4", "fold_automorphism": "Z/2"},  # uses triality on D4? No: A5 fold
    "G2": {"parent": "D4", "fold_automorphism": "Z/3"},  # triality fold
    "F4": {"parent": "E6", "fold_automorphism": "Z/2"},
}


# ============================================================================
#  S1. Multi-colored partition obstruction (K_0 -> module gap scaling)
# ============================================================================

@lru_cache(maxsize=4096)
def multi_partition(N: int, k: int) -> int:
    """N-colored partition function p_N(k).

    Generating function: prod_{n>=1} 1/(1-x^n)^N.
    For sl_{N+1}, the prefundamental character involves
    this N-colored partition function.
    """
    if k < 0:
        return 0
    if k == 0:
        return 1

    # DP: coefficients of prod_{n>=1} 1/(1-x^n)^N up to degree k
    dp = [0] * (k + 1)
    dp[0] = 1
    for part in range(1, k + 1):
        for j in range(part, k + 1):
            dp[j] += N * dp[j - part]
        # Above is WRONG for N > 1. Use proper power series multiplication.
        pass

    # Correct implementation: expand prod_{n>=1} 1/(1-x^n)^N
    # = prod_{n>=1} sum_{m>=0} binom(m+N-1, N-1) x^{mn}
    dp2 = [0] * (k + 1)
    dp2[0] = 1
    for n in range(1, k + 1):
        new_dp = dp2[:]
        for m in range(1, k // n + 1):
            coeff = _binom(m + N - 1, N - 1)
            for j in range(m * n, k + 1):
                new_dp[j] += coeff * dp2[j - m * n]
        dp2 = new_dp
    return dp2[k]


def _binom(n: int, k: int) -> int:
    """Binomial coefficient C(n, k)."""
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def obstruction_dimension_by_type(type_name: str, max_k: int = 20) -> Dict:
    """Compute the K_0-to-module obstruction dimension delta(k) for each type.

    For type X_r, the prefundamental L^-_i has character involving an
    infinite product over positive roots containing alpha_i. The number
    of such roots determines the "color count" for the partition function.

    Key insight: for node i, the number of relevant positive roots is
    n_rel(i) = |{beta > 0 : alpha_i in supp(beta)}|.

    The multi-partition obstruction at weight level k is:
    delta_i(k) = p_{n_rel(i)}(k) - 1

    where p_N is the N-colored partition function.
    """
    data = DYNKIN_DATA[type_name]
    rank = data["rank"]
    cartan = CARTAN_MATRICES[type_name]

    # Count positive roots containing each simple root
    # For simply-laced types, this is straightforward from the Cartan matrix
    # For type A_r: root alpha_{a..b} contains alpha_i iff a <= i <= b
    #   So n_rel(i) = (i+1) * (r-i) for 0-indexed
    # For general types: need to enumerate positive roots

    pos_roots = enumerate_positive_roots(type_name)
    n_roots_containing = []
    for i in range(rank):
        count = sum(1 for root in pos_roots if root[i] > 0)
        n_roots_containing.append(count)

    # Compute obstruction for each node
    node_data = {}
    max_obstruction = 0
    hardest_node = -1
    for i in range(rank):
        n_rel = n_roots_containing[i]
        obstructions = {}
        for k in range(1, max_k + 1):
            # For the multi-partition, we approximate with the simple formula
            # p_N(k) where N = n_rel
            pk = _multi_partition_dp(n_rel, k)
            delta = pk - 1
            obstructions[k] = delta
            if delta > max_obstruction:
                max_obstruction = delta
                hardest_node = i

        node_data[i] = {
            "node": i,
            "n_relevant_roots": n_rel,
            "obstructions": obstructions,
            "growth_rate": _estimate_growth_rate(n_rel),
        }

    return {
        "type": type_name,
        "rank": rank,
        "n_positive_roots": data["n_positive_roots"],
        "n_roots_containing": n_roots_containing,
        "node_data": node_data,
        "hardest_node": hardest_node,
        "max_obstruction_at_k20": max_obstruction,
    }


@lru_cache(maxsize=65536)
def _multi_partition_dp(N: int, k: int) -> int:
    """N-colored partition function via direct DP.

    p_N(k) = coefficient of x^k in prod_{n>=1} (1/(1-x^n))^N.
    """
    if k < 0:
        return 0
    if k == 0:
        return 1
    if N == 1:
        return partition_number(k)

    # Recurrence: p_N(k) = (1/k) * sum_{j=1}^{k} sigma_N(j) * p_N(k-j)
    # where sigma_N(j) = N * sigma_1(j) = N * sum_{d|j} d.
    # This is the standard recurrence for the N-colored partition function.
    result = 0
    for j in range(1, k + 1):
        # sigma_1(j) = sum of divisors of j
        s1 = sum(d for d in range(1, j + 1) if j % d == 0)
        result += N * s1 * _multi_partition_dp(N, k - j)
    return result // k


def _estimate_growth_rate(N: int) -> str:
    """Asymptotic growth rate of p_N(k).

    p_N(k) ~ C_N * k^{-(N+1)/2} * exp(pi * sqrt(2Nk/3))
    """
    return f"exp(pi*sqrt({2*N}/3 * k)) / k^{(N+1)/2}"


# ============================================================================
#  S2. Positive root enumeration for all types
# ============================================================================

def enumerate_positive_roots(type_name: str) -> List[Tuple[int, ...]]:
    """Enumerate all positive roots for the given type in simple root coordinates.

    A positive root is a tuple (c_1, ..., c_r) with c_i >= 0 representing
    the root c_1*alpha_1 + ... + c_r*alpha_r.

    Uses the standard algorithm: start with simple roots, repeatedly apply
    simple reflections, collect positive roots.
    """
    cartan = CARTAN_MATRICES[type_name]
    rank = len(cartan)

    # Simple roots: e_i
    simple = [tuple(1 if j == i else 0 for j in range(rank)) for i in range(rank)]
    roots = set()
    for s in simple:
        roots.add(s)

    # Repeatedly apply Weyl reflections to find all positive roots
    changed = True
    while changed:
        changed = False
        new_roots = set()
        for root in roots:
            for i in range(rank):
                # s_i(beta) = beta - <beta, alpha_i^vee> * alpha_i
                # <beta, alpha_i^vee> = sum_j c_j * A_{ji} where beta = sum c_j alpha_j
                inner = sum(root[j] * cartan[j][i] for j in range(rank))
                reflected = list(root)
                reflected[i] -= inner
                reflected = tuple(reflected)
                if all(c >= 0 for c in reflected) and any(c > 0 for c in reflected):
                    if reflected not in roots:
                        new_roots.add(reflected)
        if new_roots:
            roots |= new_roots
            changed = True

    return sorted(roots, key=lambda x: (sum(x), x))


# ============================================================================
#  S3. Minuscule representation analysis
# ============================================================================

def minuscule_analysis(type_name: str) -> Dict:
    """Analyze minuscule representation availability and its impact on MC3.

    A minuscule representation has all weights in a single Weyl orbit.
    This means every weight has multiplicity 1, which makes the CG
    decomposition V_{minuscule} x L^-_i much simpler to lift from K_0
    to modules: each shifted L^-_i summand has multiplicity exactly 1.

    For non-minuscule reps, weight multiplicities > 1 appear, and the
    CG lift must disentangle these multiplicities at the module level.
    """
    data = DYNKIN_DATA[type_name]
    rank = data["rank"]
    n_minuscule = data["n_minuscule"]
    minuscule_nodes = data["minuscule_nodes"]

    # Fundamental reps at non-minuscule nodes have weight mult > 1
    non_minuscule_nodes = [i for i in range(rank) if i not in minuscule_nodes]

    # For non-minuscule fundamentals, the max weight multiplicity grows
    # This is the source of the categorical difficulty
    fund_dims = FUNDAMENTAL_DIMS.get(type_name, [])

    generation_strategy = "EASY" if n_minuscule == rank else (
        "MODERATE" if n_minuscule >= rank // 2 else (
            "HARD" if n_minuscule >= 1 else "VERY_HARD"
        )
    )

    return {
        "type": type_name,
        "rank": rank,
        "n_minuscule": n_minuscule,
        "minuscule_nodes": minuscule_nodes,
        "non_minuscule_nodes": non_minuscule_nodes,
        "minuscule_fraction": n_minuscule / rank if rank > 0 else 0,
        "fundamental_dims": fund_dims,
        "generation_strategy": generation_strategy,
        "comment": _minuscule_comment(type_name, n_minuscule, rank),
    }


def _minuscule_comment(type_name: str, n_min: int, rank: int) -> str:
    """Generate diagnostic comment."""
    if n_min == rank:
        return "All fundamentals are minuscule (type A). CG lift is simplest."
    if n_min == 0:
        return (f"NO minuscule reps. Every fundamental V_{{omega_i}} has weight "
                f"multiplicities > 1. The CG decomposition at the module level "
                f"requires resolving multiplicity spaces — this is the HARDEST case.")
    if type_name.startswith("B") or type_name.startswith("D"):
        return (f"Only {n_min} of {rank} fundamentals are minuscule. "
                f"Spinor/non-minuscule nodes require different generation strategy.")
    return f"{n_min} of {rank} fundamentals are minuscule."


# ============================================================================
#  S4. Short root obstruction (non-simply-laced types)
# ============================================================================

def short_root_analysis(type_name: str) -> Dict:
    """Analyze the short-root obstruction for non-simply-laced types.

    In non-simply-laced types, the root system has two root lengths.
    The short roots and long roots have different squared lengths:
      B_n: |alpha_short|^2 = 1, |alpha_long|^2 = 2 (ratio 1:2)
      C_n: |alpha_short|^2 = 1, |alpha_long|^2 = 2 (ratio 1:2)
      G_2: |alpha_short|^2 = 1, |alpha_long|^2 = 3 (ratio 1:3)
      F_4: |alpha_short|^2 = 1, |alpha_long|^2 = 2 (ratio 1:2)

    The coroot alpha^vee = 2*alpha/|alpha|^2 differs between short and
    long roots. This means:
      <beta, alpha^vee_short> != <beta, alpha^vee_long> in general
    and the Baxter TQ relations have DIFFERENT structure at short vs long nodes.
    """
    data = DYNKIN_DATA[type_name]
    if data["simply_laced"]:
        return {
            "type": type_name,
            "simply_laced": True,
            "obstruction": "NONE (simply laced)",
        }

    short_nodes = data.get("short_root_nodes", [])
    long_nodes = data.get("long_root_nodes", [])
    cartan = CARTAN_MATRICES[type_name]
    rank = data["rank"]

    # The off-diagonal Cartan matrix entries reveal the asymmetry:
    # A_{ij} = <alpha_i, alpha_j^vee> = 2*<alpha_i, alpha_j>/|alpha_j|^2
    # For i short, j long: A_{ij} = -1 (typically)
    # For i long, j short: A_{ij} = -2 or -3 (B/C: -2, G2: -3)
    asymmetric_entries = []
    for i in range(rank):
        for j in range(rank):
            if i != j and cartan[i][j] != 0 and cartan[i][j] != cartan[j][i]:
                asymmetric_entries.append({
                    "i": i, "j": j,
                    "A_ij": cartan[i][j],
                    "A_ji": cartan[j][i],
                    "i_type": "short" if i in short_nodes else "long",
                    "j_type": "short" if j in short_nodes else "long",
                })

    # Langlands dual twist: the folding construction introduces an
    # involution on the root system data that swaps short <-> long
    folding = FOLDING_DATA.get(type_name, None)

    return {
        "type": type_name,
        "simply_laced": False,
        "short_nodes": short_nodes,
        "long_nodes": long_nodes,
        "asymmetric_cartan_entries": asymmetric_entries,
        "folding_parent": folding["parent"] if folding else None,
        "fold_automorphism": folding["fold_automorphism"] if folding else None,
        "obstruction": (
            "Cartan matrix asymmetry implies different Baxter TQ structure "
            "at short vs long nodes. The CG decomposition "
            f"V_{{omega_i}} x L^-_i for short node i has "
            "DIFFERENT filtration type than for long nodes. "
            "The Hernandez-Jimbo construction uses FOLDING from "
            f"{folding['parent'] if folding else '?'}, introducing "
            "fixed-point issues at the categorical level."
        ),
    }


# ============================================================================
#  S5. Spinor representation obstruction (B_n, D_n)
# ============================================================================

def spinor_obstruction_analysis(type_name: str) -> Dict:
    """Analyze the spinor representation obstruction.

    For B_n and D_n, the spinor nodes have fundamental representations
    that are NOT exterior powers of the vector representation.

    In type A, ALL fundamentals Lambda^k(V) are exterior powers.
    This means the evaluation core (thm:eval-core-identification) can be
    generated by a SINGLE representation (the standard V_{omega_1}).

    For B_n/D_n, spinor reps require a separate generator.
    This means the evaluation core step (Step 1 of the type-A proof)
    must be MODIFIED: the generators are NOT just {V_{omega_1}} but
    {V_{omega_1}} union {V_{omega_spin}}.
    """
    data = DYNKIN_DATA[type_name]
    if not data.get("has_spinor", False):
        return {
            "type": type_name,
            "has_spinor": False,
            "obstruction": "NONE (no spinor representation)",
        }

    spinor_nodes = data.get("spinor_nodes", [])
    fund_dims = FUNDAMENTAL_DIMS.get(type_name, [])
    rank = data["rank"]

    # Spinor dimension grows exponentially with rank
    spinor_dims = [fund_dims[i] for i in spinor_nodes if i < len(fund_dims)]

    # For D_n: outer automorphism swaps the two half-spinors
    outer_auto = data.get("outer_automorphism_order", 1)
    vector_node = data.get("vector_node", 0)

    # Key obstruction: spinor not in tensor algebra of vector
    # For B_n: spin(2n+1) -> SO(2n+1), spinor = 2^n, vector = 2n+1
    # The spinor is NOT in Lambda^*(C^{2n+1}) (wrong dimension).
    # It IS in the Clifford algebra, but this requires a different construction.

    # For D_n: half-spinors have dim 2^{n-1}.
    # They appear in the Clifford algebra of C^{2n}, but NOT as direct
    # summands of tensor powers of the vector rep.

    return {
        "type": type_name,
        "has_spinor": True,
        "spinor_nodes": spinor_nodes,
        "spinor_dims": spinor_dims,
        "outer_automorphism_order": outer_auto,
        "vector_node": vector_node,
        "vector_dim": fund_dims[vector_node] if vector_node < len(fund_dims) else None,
        "obstruction": (
            f"Spinor reps at nodes {spinor_nodes} have dims {spinor_dims}, "
            f"NOT in tensor algebra of vector rep (node {vector_node}, "
            f"dim {fund_dims[vector_node] if vector_node < len(fund_dims) else '?'}). "
            "Evaluation core identification requires SEPARATE spinor generators. "
            "CG decomposition V_spin x L^-_spin has fundamentally different "
            "structure from V_vector x L^-_vector."
        ),
        "evaluation_core_generators": (
            f"Must use {{V_{{omega_{vector_node+1}}}, "
            + ", ".join(f"V_{{omega_{s+1}}}" for s in spinor_nodes)
            + "} instead of just {V_{omega_1}}."
        ),
    }


# ============================================================================
#  S6. Exceptional type hardness ranking
# ============================================================================

def exceptional_hardness_ranking() -> Dict:
    """Rank all Dynkin types by hardness for the MC3 extension.

    Hardness factors:
    1. Minuscule scarcity (weight multiplicity complications)
    2. Root system complexity (number of positive roots)
    3. Weyl group size (computation complexity)
    4. Simply-laced vs not (folding complications)
    5. Spinor presence (generation strategy complications)
    6. Minimal representation dimension (CG computation cost)
    7. K_0 obstruction growth (multi-partition scaling)

    Returns ordered ranking from easiest to hardest.
    """
    types_to_rank = [
        "A1", "A2", "A3", "A4",
        "B2", "B3",
        "C2", "C3",
        "D4", "D5",
        "G2", "F4",
        "E6", "E7", "E8",
    ]

    scores = {}
    for t in types_to_rank:
        data = DYNKIN_DATA[t]
        rank = data["rank"]
        n_pos = data["n_positive_roots"]
        weyl = data["weyl_order"]
        n_min = data["n_minuscule"]

        # Score components (higher = harder)
        minuscule_penalty = (rank - n_min) * 10  # penalty for non-minuscule
        root_complexity = n_pos
        weyl_complexity = math.log(weyl + 1)  # log scale
        lacing_penalty = 0 if data["simply_laced"] else 20
        spinor_penalty = 15 if data.get("has_spinor", False) else 0

        # Minimal fundamental dimension (larger = harder CG)
        fund = FUNDAMENTAL_DIMS.get(t, [1])
        min_fund_dim = min(fund) if fund else 1
        dim_penalty = math.log(min_fund_dim + 1) * 5

        # K_0 obstruction: max relevant roots per node
        pos_roots = enumerate_positive_roots(t)
        max_rel = 0
        for i in range(rank):
            count = sum(1 for root in pos_roots if root[i] > 0)
            max_rel = max(max_rel, count)
        k0_penalty = max_rel * 3

        total = (minuscule_penalty + root_complexity + weyl_complexity +
                 lacing_penalty + spinor_penalty + dim_penalty + k0_penalty)

        scores[t] = {
            "total_score": round(total, 1),
            "minuscule_penalty": minuscule_penalty,
            "root_complexity": root_complexity,
            "weyl_complexity": round(weyl_complexity, 1),
            "lacing_penalty": lacing_penalty,
            "spinor_penalty": spinor_penalty,
            "dim_penalty": round(dim_penalty, 1),
            "k0_penalty": k0_penalty,
        }

    # Sort by score
    ranking = sorted(scores.items(), key=lambda x: x[1]["total_score"])

    return {
        "ranking": [(t, s["total_score"]) for t, s in ranking],
        "hardest_type": ranking[-1][0],
        "hardest_score": ranking[-1][1]["total_score"],
        "easiest_non_A": next(
            (t for t, _ in ranking if not t.startswith("A")), None
        ),
        "details": scores,
    }


# ============================================================================
#  S7. D_n spinor parity obstruction
# ============================================================================

def dn_spinor_parity_obstruction(n: int) -> Dict:
    """Analyze the spinor parity obstruction for D_n.

    D_n has an outer automorphism sigma swapping omega_{n-1} <-> omega_n.
    The Yangian Y(so_{2n}) inherits this as an automorphism.
    Prefundamentals: L^-_{n-1} and L^-_n are swapped by sigma.

    CG decomposition at spinor nodes:
      V_{omega_{n-1}} x L^-_{n-1} should decompose into shifted L^-_{n-1}'s
      V_{omega_n} x L^-_n should decompose into shifted L^-_n's

    But sigma links these: the exact triangle for node n-1 is the sigma-image
    of the exact triangle for node n. This means the categorical CG
    splitting for the two spin nodes are NOT independent.

    For D_4 (triality): there is an S_3 action permuting nodes 1, 3, 4.
    The CG decompositions at all three minuscule nodes are linked by triality.
    """
    if n < 3:
        return {"error": f"D_n requires n >= 3, got n={n}"}

    type_name = f"D{n}"
    data = DYNKIN_DATA.get(type_name)
    if data is None:
        # Compute from scratch
        rank = n
        spin_dim = 2 ** (n - 1)
        vector_dim = 2 * n
        outer_auto = 6 if n == 4 else 2
        data = {
            "rank": rank, "has_spinor": True,
            "spinor_nodes": [n - 2, n - 1],  # 0-indexed
            "outer_automorphism_order": outer_auto,
        }
    else:
        spin_dim = 2 ** (n - 1)
        vector_dim = 2 * n
        outer_auto = data.get("outer_automorphism_order", 2)

    # CG multiplicities at spinor nodes involve bi-spinor decomposition
    # V_{spin} x L^-_{spin} has dim(V_spin) = 2^{n-1} summands in CG
    # Each summand is a shifted L^-_{spin} with multiplicity from weight space
    # The weight multiplicities of the spin rep are ALL 1 (it is minuscule for D_n)
    # This is actually FAVORABLE: the CG at spinor nodes is as good as type A!

    spin_is_minuscule = True  # Always true for D_n spinors

    return {
        "type": f"D_{n}",
        "rank": n,
        "spin_dim": spin_dim,
        "vector_dim": vector_dim,
        "outer_automorphism_order": outer_auto,
        "spin_is_minuscule": spin_is_minuscule,
        "linked_cg": (
            "CG decompositions at nodes n-1 and n are linked by the outer "
            "automorphism sigma. Proving the categorical CG at one spinor "
            "node automatically gives it at the other via sigma-transport."
        ),
        "obstruction_severity": "LOW" if spin_is_minuscule else "HIGH",
        "reason": (
            "D_n spinors ARE minuscule, so all weight multiplicities are 1. "
            "The CG decomposition V_spin x L^-_spin has the same multiplicity "
            "structure as type A. The REAL obstruction is at the non-minuscule "
            f"nodes (e.g., node 2 for D_{n}, the adjoint rep of dim "
            f"{n * (2*n - 1)})."
        ),
        "actual_hard_node": 1 if n >= 4 else None,  # 0-indexed: node 2 in math notation
        "adjoint_dim": n * (2 * n - 1),
    }


# ============================================================================
#  S8. Hernandez-Jimbo construction uniformity
# ============================================================================

def hernandez_jimbo_uniformity_analysis() -> Dict:
    """Analyze whether the HJ prefundamental construction is uniform across types.

    For type A: HJ12 Theorem 3.8 gives L^-_i by q-deformation limit.
    For other types: HJ12 Section 5 extends to all types, but the method varies:

    Simply-laced (ADE):
      - Nakajima quiver variety construction available
      - q-character formula from crystal base theory
      - L^-_i well-defined and irreducible

    Non-simply-laced (BCFG):
      - Obtained by FOLDING from simply-laced type
      - B_n from A_{2n-1}, C_n from D_{n+1}, G_2 from D_4, F_4 from E_6
      - Folding introduces outer automorphism group action
      - The prefundamental is an EQUIVARIANT object under the fold

    KEY GAP: The categorical CG splitting
      V_{omega_i} x L^-_i ≅ bigoplus L^-_i(shifted)
    requires showing that the tensor product DECOMPOSES as a direct sum,
    not just as a filtration. In type A, this uses the fact that L^-_i
    is the unique irreducible with a given asymptotic character (HJZ25 Thm 3.8).
    For other types:
    - Simply-laced (DE): the same uniqueness holds (Nakajima 2004).
    - Non-simply-laced (BCFG): uniqueness holds by folding, but the
      direct-sum decomposition requires ADDITIONALLY showing that the
      folding functor preserves direct-sum decompositions.
    """
    type_analysis = {}

    for t, data in DYNKIN_DATA.items():
        if data["simply_laced"]:
            method = "Nakajima quiver variety / q-deformation limit"
            uniformity = "GOOD" if t.startswith("A") else "MODERATE"
            gap = ("Quiver variety construction available for ADE. "
                   "The categorical CG needs irreducibility + uniqueness, "
                   "both proved for ADE by Nakajima 2004.")
            if t.startswith("E"):
                uniformity = "MODERATE"
                gap = ("Nakajima construction exists but computations are hard. "
                       f"For {t}: Weyl group has order {data['weyl_order']}, "
                       f"making explicit CG verification expensive.")
        else:
            method = f"Folding from {FOLDING_DATA.get(t, {}).get('parent', '?')}"
            uniformity = "WEAK"
            gap = ("Folding introduces categorical complications: "
                   "the functor from the parent type to the folded type "
                   "must preserve direct-sum decompositions. This is NOT "
                   "automatic for infinite-dimensional modules.")

        type_analysis[t] = {
            "method": method,
            "uniformity": uniformity,
            "categorical_gap": gap,
        }

    return type_analysis


# ============================================================================
#  S9. Escape route analysis
# ============================================================================

def escape_route_analysis() -> Dict:
    """Analyze alternative proof strategies that could bypass the CG obstruction.

    Even if the direct Hernandez-Jimbo CG splitting approach fails for
    some types, the conjecture could still be true via different methods.
    """
    routes = {
        "RTT_realization": {
            "description": (
                "R-matrix approach (Faddeev-Reshetikhin-Takhtajan): "
                "uniform Yangian presentation for all types via R(u) = 1 + P/u. "
                "The RTT approach gives the Yangian as a quotient of a universal "
                "algebra defined by the Yang-Baxter equation."
            ),
            "coverage": "ALL types (uniform)",
            "gap": (
                "RTT gives PRESENTATION but not REPRESENTATION THEORY. "
                "The category O^sh and its compact objects still require "
                "understanding prefundamental modules. RTT bypasses the "
                "CG issue only if bar-cobar can be defined purely in terms "
                "of the RTT generators — which is not yet established."
            ),
            "viability": "LOW for bypassing CG",
        },
        "Maulik_Okounkov": {
            "description": (
                "Geometric R-matrix from Nakajima quiver varieties. "
                "Maulik-Okounkov 2019 gives a uniform construction of "
                "quantum groups via stable envelopes on symplectic "
                "resolutions."
            ),
            "coverage": "ADE types (quiver varieties exist); NOT non-simply-laced",
            "gap": (
                "Only works for ADE. For BCFG, would need equivariant "
                "version with respect to the folding automorphism. "
                "Maulik-Okounkov's construction is geometric and does "
                "not directly give the categorical CG decomposition."
            ),
            "viability": "MODERATE for ADE, NONE for BCFG",
        },
        "Coulomb_branch": {
            "description": (
                "BDGH construction (Braverman-Finkelberg-Nakajima): "
                "Yangian as endomorphism algebra of the BFN Coulomb branch."
            ),
            "coverage": "ALL types (Coulomb branches exist for all reductive G)",
            "gap": (
                "Coulomb branch gives the ALGEBRA structure uniformly. "
                "The module category structure (O^sh, compact objects, "
                "prefundamental modules) is NOT yet established via "
                "Coulomb branches for types outside A."
            ),
            "viability": "MODERATE (most promising for uniform approach)",
        },
        "direct_DK_without_CG": {
            "description": (
                "Prove DK equivalence directly on the evaluation category "
                "without passing through prefundamental generation. "
                "Use that the evaluation functor Y(g) -> U(g) identifies "
                "the compact evaluation objects with finite-dimensional g-modules."
            ),
            "coverage": "ALL types",
            "gap": (
                "This works for the EVALUATION CORE (Step 1 of type-A proof). "
                "The obstacle is extending from evaluation core to the FULL "
                "completed category. Without prefundamental CG, there is no "
                "mechanism to reach beyond evaluation objects."
            ),
            "viability": "LOW (avoids the wrong step)",
        },
    }

    # Overall assessment
    best_route = "Coulomb_branch"
    overall = (
        "The Coulomb branch approach is the most promising escape route. "
        "It provides the algebra uniformly for all types. The remaining "
        "gap is establishing the module category structure (O^sh, compacts, "
        "prefundamentals) in the Coulomb branch framework. This is an "
        "active research area (Ben Webster, Kamnitzer, Weekes, Yacobi)."
    )

    return {
        "routes": routes,
        "best_escape": best_route,
        "overall_assessment": overall,
    }


# ============================================================================
#  S10. Comprehensive vulnerability report
# ============================================================================

def comprehensive_vulnerability_report() -> Dict:
    """Generate the full RED TEAM report on conj:mc3-arbitrary-type.

    Synthesizes all attack vectors into a single assessment with
    severity rankings.
    """
    vulnerabilities = []

    # V1: E_8 has NO minuscule reps and largest Weyl group
    e8_min = minuscule_analysis("E8")
    vulnerabilities.append({
        "id": "V1",
        "severity": "CRITICAL",
        "target": "E_8",
        "description": (
            "E_8 has ZERO minuscule representations. Every fundamental "
            "has weight multiplicities > 1. The smallest fundamental "
            "is the adjoint (dim 248). CG decomposition at the module "
            "level requires resolving 248-dimensional multiplicity spaces. "
            f"Weyl group order: {DYNKIN_DATA['E8']['weyl_order']:,}."
        ),
        "impact": "Categorical CG splitting may FAIL for E_8.",
        "mitigation": "Coulomb branch approach bypasses CG entirely.",
    })

    # V2: F_4 has no minuscule AND is non-simply-laced
    f4_short = short_root_analysis("F4")
    vulnerabilities.append({
        "id": "V2",
        "severity": "CRITICAL",
        "target": "F_4",
        "description": (
            "F_4 combines TWO failure modes: (1) zero minuscule reps, "
            "and (2) non-simply-laced (short roots at nodes 3,4). "
            "The folding from E_6 introduces categorical complications "
            "on top of the weight multiplicity problem. "
            "Smallest fundamental: dim 26."
        ),
        "impact": "Double obstruction: multiplicity + folding.",
        "mitigation": "Folding from E_6 (which is better understood).",
    })

    # V3: G_2 ratio 1:3 root lengths
    g2_short = short_root_analysis("G2")
    vulnerabilities.append({
        "id": "V3",
        "severity": "HIGH",
        "target": "G_2",
        "description": (
            "G_2 has root length ratio 1:sqrt(3) (unique among simple types). "
            "The Cartan matrix has entry -3 (A_{21} = -3), making the "
            "coroot computation more extreme. Folding from D_4 via S_3 "
            "triality — the most complex folding operation. "
            "Zero minuscule reps."
        ),
        "impact": "Triality folding is categorically hard to control.",
        "mitigation": "G_2 has rank 2, so explicit computation is feasible.",
    })

    # V4: K_0 obstruction growth for high rank
    vulnerabilities.append({
        "id": "V4",
        "severity": "HIGH",
        "target": "All types with rank >= 4",
        "description": (
            "The K_0-to-module obstruction delta_N(k) = p_N(k) - 1 "
            "grows like exp(pi*sqrt(2Nk/3)). For E_8 (rank 8), the "
            "max relevant root count N_rel can be up to 120 (all positive "
            "roots), giving astronomical obstruction growth. "
            "The Ext^1 spaces that must vanish for CG splitting grow "
            "at least as fast as delta."
        ),
        "impact": "Character-level argument does not control Ext growth.",
        "mitigation": "Chromatic filtration still converges (E_1 page is finite).",
    })

    # V5: Spinor generation gap
    vulnerabilities.append({
        "id": "V5",
        "severity": "MODERATE",
        "target": "B_n (n >= 2), D_n (n >= 4)",
        "description": (
            "Spinor reps are not in the tensor algebra of the vector rep. "
            "The evaluation core needs separate spinor generators. "
            "For B_n: spin has dim 2^n (exponential in rank). "
            "For D_n: half-spins have dim 2^{n-1}."
        ),
        "impact": "Evaluation core identification needs modification.",
        "mitigation": (
            "D_n spinors ARE minuscule — weight mults are all 1. "
            "B_n spinor is quasi-minuscule. This is a MODERATE issue."
        ),
    })

    # V6: Non-uniform HJ construction
    vulnerabilities.append({
        "id": "V6",
        "severity": "MODERATE",
        "target": "BCFG types",
        "description": (
            "The Hernandez-Jimbo prefundamental for non-simply-laced types "
            "is constructed by FOLDING from a simply-laced parent. "
            "The folding functor must preserve direct-sum decompositions "
            "of infinite-dimensional modules. This is not automatic."
        ),
        "impact": "Folding may not preserve the CG direct-sum structure.",
        "mitigation": "Character-level CG is proved (folding does work at K_0).",
    })

    # V7: Pro-Weyl for non-type-A
    vulnerabilities.append({
        "id": "V7",
        "severity": "LOW",
        "target": "All non-A types",
        "description": (
            "Pro-Weyl recovery (Package iii) uses Mittag-Leffler on "
            "Weyl module truncation towers. The statement that transition "
            "maps are surjective is rank-independent. This package "
            "transfers without modification."
        ),
        "impact": "NONE — this step is uniform.",
        "mitigation": "Already acknowledged as rank-independent in the conjecture.",
    })

    # V8: Francis-Gaitsgory completion for non-type-A
    vulnerabilities.append({
        "id": "V8",
        "severity": "LOW",
        "target": "All non-A types",
        "description": (
            "FG pro-nilpotent completion (Package iv) uses only that "
            "Phi is an equivalence on compacts and both sides are "
            "compactly generated. This is a formal consequence."
        ),
        "impact": "NONE — formal step.",
        "mitigation": "Already acknowledged as rank-independent.",
    })

    # Synthesize
    critical = [v for v in vulnerabilities if v["severity"] == "CRITICAL"]
    high = [v for v in vulnerabilities if v["severity"] == "HIGH"]

    hardest_type = "E8"  # No minuscule, largest rank, largest Weyl group
    second_hardest = "F4"  # No minuscule + non-simply-laced

    return {
        "n_vulnerabilities": len(vulnerabilities),
        "n_critical": len(critical),
        "n_high": len(high),
        "vulnerabilities": vulnerabilities,
        "hardest_type": hardest_type,
        "second_hardest_type": second_hardest,
        "overall_assessment": (
            "The conjecture has TWO critical failure points: "
            "(1) E_8, which has no minuscule reps and requires resolving "
            "248-dimensional weight spaces in the CG decomposition; "
            "(2) F_4, which combines the no-minuscule problem with "
            "non-simply-laced folding complications. "
            "The type-A proof strategy DOES NOT directly generalize to "
            "these cases. However, the conjecture is LIKELY TRUE because "
            "the Coulomb branch approach provides a uniform alternative "
            "proof path. The REAL bottleneck is establishing the O^sh "
            "category structure for exceptional types, not the CG splitting."
        ),
        "recommended_attack_priority": [
            "E_8: test whether evaluation core generates compacts",
            "F_4: test whether folding preserves CG direct sums",
            "G_2: explicit CG computation (rank 2, feasible)",
            "D_4: triality compatibility of CG at three minuscule nodes",
        ],
    }


# ============================================================================
#  S11. Quantitative CG obstruction comparison across types
# ============================================================================

def cg_obstruction_comparison(max_k: int = 15) -> Dict:
    """Compare the CG obstruction dimension across all Dynkin types.

    For each type and each node i, compute:
    - n_rel(i) = number of positive roots containing alpha_i
    - delta_i(k) = p_{n_rel(i)}(k) - 1 for k = 1, ..., max_k
    - The MAXIMUM delta across all nodes at each k

    Returns comparative data showing which types have the worst scaling.
    """
    types_to_check = ["A2", "A3", "A4", "B2", "B3", "C3", "D4", "G2", "F4", "E6"]
    results = {}

    for t in types_to_check:
        data = DYNKIN_DATA[t]
        rank = data["rank"]
        pos_roots = enumerate_positive_roots(t)

        n_rel_per_node = []
        for i in range(rank):
            count = sum(1 for root in pos_roots if root[i] > 0)
            n_rel_per_node.append(count)

        max_n_rel = max(n_rel_per_node)

        # Compute max delta at each k
        max_deltas = {}
        for k in range(1, max_k + 1):
            max_d = 0
            for n_rel in n_rel_per_node:
                pk = _multi_partition_dp(n_rel, k)
                d = pk - 1
                if d > max_d:
                    max_d = d
            max_deltas[k] = max_d

        results[t] = {
            "rank": rank,
            "n_positive_roots": len(pos_roots),
            "n_rel_per_node": n_rel_per_node,
            "max_n_rel": max_n_rel,
            "max_deltas": max_deltas,
        }

    # Find worst type at each k
    worst_at_k = {}
    for k in range(1, max_k + 1):
        worst_type = max(results.keys(), key=lambda t: results[t]["max_deltas"][k])
        worst_at_k[k] = (worst_type, results[worst_type]["max_deltas"][k])

    return {
        "types_compared": types_to_check,
        "results": results,
        "worst_at_each_k": worst_at_k,
    }


# ============================================================================
#  S12. Type-by-type feasibility assessment
# ============================================================================

def type_by_type_feasibility() -> Dict:
    """For each Dynkin type, assess the feasibility of the MC3 extension.

    Grade: A (straightforward), B (moderate), C (hard), D (very hard), F (potentially fails).
    """
    assessments = {
        "A_n": {
            "grade": "A",
            "status": "PROVED (thm:mc3-type-a-resolution)",
            "reason": "All fundamentals minuscule, simple CG, no folding.",
        },
        "D_n": {
            "grade": "B",
            "status": "Expected to follow from type A methods",
            "reason": (
                "Simply-laced, 3 minuscule reps (vector + 2 half-spins). "
                "Spinors are minuscule so CG has mult-1 weights. "
                "Main gap: non-minuscule middle nodes (adjoint rep). "
                "Outer automorphism links spin nodes (helpful, not harmful)."
            ),
        },
        "B_n": {
            "grade": "C",
            "status": "Requires new input",
            "reason": (
                "Non-simply-laced. Only 1 minuscule (vector). Spinor is NOT "
                "minuscule (it IS quasi-minuscule: all weights have mult 1 "
                "except possibly the zero weight). Folding from A_{2n-1} "
                "introduces categorical issues. Short root node complicates "
                "Baxter TQ structure."
            ),
        },
        "C_n": {
            "grade": "C",
            "status": "Requires new input",
            "reason": (
                "Non-simply-laced (Langlands dual of B_n). Only 1 minuscule. "
                "Folding from D_{n+1}. The Langlands duality interchanges "
                "short and long roots, which affects the prefundamental "
                "character formula."
            ),
        },
        "E_6": {
            "grade": "B+",
            "status": "Expected to follow from DE methods",
            "reason": (
                "Simply-laced, 2 minuscule reps (27-dim). Nakajima quiver "
                "variety exists. Main challenge: rank 6 makes explicit "
                "computations expensive but not impossible. Weyl group "
                "order 51,840 is manageable."
            ),
        },
        "E_7": {
            "grade": "C+",
            "status": "Requires careful analysis",
            "reason": (
                "Simply-laced but only 1 minuscule (56-dim). 6 of 7 "
                "fundamentals are non-minuscule with weight multiplicities > 1. "
                "Weyl group order 2,903,040. Generation from the single "
                "minuscule rep is insufficient — need additional generators."
            ),
        },
        "E_8": {
            "grade": "D",
            "status": "HARDEST CASE — may require fundamentally new methods",
            "reason": (
                "Simply-laced but ZERO minuscule reps. Every fundamental "
                "has weight mults > 1. Smallest is the adjoint (248). "
                "Weyl group order 696,729,600. No small generator exists. "
                "Evaluation core must use large representations. "
                "CG decomposition extremely expensive."
            ),
        },
        "G_2": {
            "grade": "C-",
            "status": "Explicit computation feasible (rank 2)",
            "reason": (
                "Non-simply-laced, zero minuscule, triality folding from D_4. "
                "BUT rank 2 means explicit computation is feasible. "
                "Root length ratio 1:sqrt(3) (unique). "
                "The 7-dim fundamental is the smallest available."
            ),
        },
        "F_4": {
            "grade": "D",
            "status": "SECOND HARDEST — double obstruction",
            "reason": (
                "Non-simply-laced AND zero minuscule reps. "
                "Folding from E_6 introduces categorical complications. "
                "Short roots at nodes 3,4. "
                "Smallest fundamental: 26-dim (but node 4). "
                "Combined difficulty of multiplicity + folding."
            ),
        },
    }

    # Count grades
    grade_counts = {}
    for t, a in assessments.items():
        g = a["grade"][0]  # First character
        grade_counts[g] = grade_counts.get(g, 0) + 1

    return {
        "assessments": assessments,
        "grade_distribution": grade_counts,
        "proved": ["A_n"],
        "expected_straightforward": ["D_n", "E_6"],
        "requires_new_input": ["B_n", "C_n", "E_7", "G_2"],
        "may_require_new_methods": ["E_8", "F_4"],
    }
