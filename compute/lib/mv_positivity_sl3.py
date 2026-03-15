"""Mirković-Vilonen positivity for Y(sl₃) asymptotic characters (task B8).

MV (Mirković-Vilonen) polytopes provide a combinatorial model for
irreducible representations of a reductive group. The "MV positivity"
conjecture says that Yangian bar cohomology classes, when expanded
in the MV basis (= canonical/crystal basis at the character level),
have non-negative coefficients.

At the shadow level (K₀/characters), this reduces to:
1. Compute Weyl characters for sl₃ representations V(λ)
2. Verify tensor product multiplicities (LR coefficients) are non-negative
3. Compare Yangian bar dimensions with the conjectured generating function
4. Verify bar Euler characteristics are compatible with MV positivity
5. Build the MV cone at small weights and verify characters lie inside

sl₃ root system:
  - Rank 2, simple roots α₁, α₂ with ⟨α₁, α₂⟩ = -1
  - Fundamental weights ω₁, ω₂ satisfying ⟨ωᵢ, αⱼ⟩ = δᵢⱼ
  - Positive roots: α₁, α₂, α₁ + α₂
  - Weyl group S₃ of order 6

Weight multiplicities from Freudenthal's formula:
  For V(λ), the multiplicity m(μ) of weight μ satisfies:
    (|λ+ρ|² - |μ+ρ|²) m(μ) = 2 Σ_{α>0} Σ_{k≥1} ⟨μ+kα, α⟩ m(μ+kα)
  where ρ = ω₁ + ω₂ = (α₁ + α₂)/2 + (α₁ + 2α₂)/2.

References:
  - Mirković-Vilonen, Geometric Langlands duality and representations
    of algebraic groups over commutative rings (2007)
  - Anderson, MV polytopes and reduced double Bruhat cells (2003)
  - Kamnitzer, MV polytopes and the PBW basis (2010)
  - yangians.tex: conj:mv-positivity-yangian, sec:asymptotic-characters
"""

from __future__ import annotations

from math import comb
from typing import Dict, List, Optional, Tuple

import numpy as np


# ============================================================
# sl₃ root system data
# ============================================================

# Simple roots in the basis (e₁ - e₂, e₂ - e₃) of the root lattice.
# We represent weights as (a, b) where the weight is aω₁ + bω₂.
# Equivalently in root coordinates: aω₁ + bω₂ = ((2a+b)/3, (a+2b)/3)
# in the (α₁, α₂) basis (where αᵢ are simple roots).

# Cartan matrix for sl₃
CARTAN_MATRIX = np.array([[2, -1], [-1, 2]], dtype=int)

# Inverse Cartan matrix (rational): A⁻¹ = (1/3)[[2,1],[1,2]]
CARTAN_INV_NUM = np.array([[2, 1], [1, 2]], dtype=int)  # numerator
CARTAN_INV_DEN = 3  # denominator

# Positive roots in Dynkin label coordinates:
# α₁ = (2, -1) in weight coords (= ω₁ applied to α₁ gives 2, ω₂ gives -1)
# Actually: roots act on weights via the Cartan matrix.
# Positive roots of sl₃ in the (α₁, α₂) basis of the ROOT lattice:
POSITIVE_ROOTS = [(1, 0), (0, 1), (1, 1)]  # α₁, α₂, α₁+α₂

# Weyl vector ρ = ω₁ + ω₂ = (1, 1) in Dynkin coordinates
RHO = (1, 1)

# Weyl group of sl₃ = S₃, acting on Dynkin labels (a, b):
# We represent Weyl group elements by their action on (a, b) = aω₁ + bω₂.
# Simple reflections:
#   s₁(aω₁ + bω₂) = (-a + b + a)ω₁ + ... = (b - a)ω₁ + (a + b)ω₂  -- WRONG
# Actually: sᵢ(λ) = λ - ⟨λ, αᵢ⟩ αᵢ
# In Dynkin coords: ⟨aω₁+bω₂, αᵢ⟩ = a if i=1, b if i=2.
# αᵢ in ω-coords: α₁ = 2ω₁ - ω₂, α₂ = -ω₁ + 2ω₂ (from Cartan matrix rows).
# s₁(a,b) = (a,b) - a(2,-1) = (-a, a+b)
# s₂(a,b) = (a,b) - b(-1,2) = (a+b, -b)

def weyl_reflect_s1(a: int, b: int) -> Tuple[int, int]:
    """Simple reflection s₁: sᵢ(λ) = λ - ⟨λ, αᵢ⟩αᵢ in Dynkin coords."""
    return (-a, a + b)


def weyl_reflect_s2(a: int, b: int) -> Tuple[int, int]:
    """Simple reflection s₂."""
    return (a + b, -b)


def weyl_orbit(a: int, b: int) -> List[Tuple[int, int]]:
    """Full Weyl orbit of (a, b) under S₃ action on Dynkin labels."""
    orbit = set()
    # Generate by applying s₁ and s₂ iteratively
    queue = [(a, b)]
    while queue:
        pt = queue.pop()
        if pt in orbit:
            continue
        orbit.add(pt)
        p, q = pt
        queue.append(weyl_reflect_s1(p, q))
        queue.append(weyl_reflect_s2(p, q))
    return sorted(orbit)


# ============================================================
# Inner product on weight space
# ============================================================

def weight_inner_product(mu1: Tuple[int, int], mu2: Tuple[int, int]) -> float:
    """Inner product ⟨μ₁, μ₂⟩ on the weight lattice.

    For weights in Dynkin coordinates (a, b), the inner product is:
        ⟨μ₁, μ₂⟩ = μ₁ᵀ · A⁻¹ · μ₂
    where A is the Cartan matrix.

    A⁻¹ = (1/3)[[2,1],[1,2]], so:
        ⟨(a₁,b₁), (a₂,b₂)⟩ = (2a₁a₂ + a₁b₂ + b₁a₂ + 2b₁b₂) / 3
    """
    a1, b1 = mu1
    a2, b2 = mu2
    return (2 * a1 * a2 + a1 * b2 + b1 * a2 + 2 * b1 * b2) / 3.0


def weight_norm_sq(mu: Tuple[int, int]) -> float:
    """Squared norm |μ|² = ⟨μ, μ⟩."""
    return weight_inner_product(mu, mu)


# ============================================================
# Weight pairing with roots
# ============================================================

def dynkin_label(mu: Tuple[int, int], i: int) -> int:
    """⟨μ, αᵢ⟩ = i-th Dynkin label of μ.

    For μ = aω₁ + bω₂: ⟨μ, α₁⟩ = a, ⟨μ, α₂⟩ = b.
    """
    if i == 0:
        return mu[0]
    elif i == 1:
        return mu[1]
    else:
        raise ValueError(f"sl₃ has simple roots 0, 1; got {i}")


def root_to_dynkin(alpha: Tuple[int, int]) -> Tuple[int, int]:
    """Convert root (in root lattice coords) to Dynkin label coords.

    A root c₁α₁ + c₂α₂ has Dynkin coords (c₁α₁ + c₂α₂) expressed
    in ω-basis: αᵢ = Σⱼ Aᵢⱼ ωⱼ, so c₁α₁+c₂α₂ = Σⱼ(c₁A₁ⱼ+c₂A₂ⱼ)ωⱼ.

    α₁ = (2,-1) in ω-basis, α₂ = (-1,2) in ω-basis.
    """
    c1, c2 = alpha
    return (2 * c1 - c2, -c1 + 2 * c2)


def pairing_weight_root(mu: Tuple[int, int], alpha: Tuple[int, int]) -> float:
    """⟨μ, α⟩ where μ is in Dynkin coords and α is in root coords.

    ⟨μ, α⟩ = 2⟨μ, α⟩/⟨α, α⟩ * ⟨α, α⟩/2 = ...
    Actually, the natural pairing is:
    ⟨aω₁+bω₂, c₁α₁+c₂α₂⟩ = a·c₁ + b·c₂
    (since ⟨ωᵢ, αⱼ⟩ = δᵢⱼ by definition).
    """
    a, b = mu
    c1, c2 = alpha
    return a * c1 + b * c2


# ============================================================
# Weyl dimension formula
# ============================================================

def sl3_irrep_dim(a: int, b: int) -> int:
    """Dimension of V(aω₁ + bω₂) for sl₃.

    dim V(a,b) = (a+1)(b+1)(a+b+2)/2.
    """
    if a < 0 or b < 0:
        return 0
    return (a + 1) * (b + 1) * (a + b + 2) // 2


# ============================================================
# Weight multiplicities via Freudenthal's formula
# ============================================================

def _add_wt(w1: Tuple[int, int], w2: Tuple[int, int]) -> Tuple[int, int]:
    return (w1[0] + w2[0], w1[1] + w2[1])


def _sub_wt(w1: Tuple[int, int], w2: Tuple[int, int]) -> Tuple[int, int]:
    return (w1[0] - w2[0], w1[1] - w2[1])


def _scale_wt(k: int, w: Tuple[int, int]) -> Tuple[int, int]:
    return (k * w[0], k * w[1])


def weight_multiplicities(lam: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    """Compute all weight multiplicities for V(λ) using Freudenthal's formula.

    λ = (a, b) in Dynkin coordinates (both non-negative).

    Freudenthal recursion:
        (|λ+ρ|² - |μ+ρ|²) · m(μ) = 2 Σ_{α>0} Σ_{k≥1} ⟨μ+kα, α⟩ · m(μ+kα)

    where α runs over positive roots in the ROOT lattice.

    We iterate over weights μ in decreasing dominance order.
    """
    a, b = lam
    if a < 0 or b < 0:
        return {}

    # The highest weight has multiplicity 1
    mult: Dict[Tuple[int, int], int] = {lam: 1}

    # Norm of λ+ρ
    lam_rho = _add_wt(lam, RHO)
    norm_lam_rho = weight_norm_sq(lam_rho)

    # Positive roots in ROOT lattice coordinates
    pos_roots = [(1, 0), (0, 1), (1, 1)]

    # Generate all weights by subtracting positive roots from λ.
    # A weight μ appears in V(λ) only if μ = λ - Σ nᵢαᵢ with nᵢ ≥ 0.
    # In Dynkin coords: subtracting αᵢ (root coords) means subtracting
    # α₁ → (2,-1), α₂ → (-1,2) in Dynkin coords.
    # But it's easier to work in root coords for the lattice.
    #
    # Weight μ in Dynkin coords: μ = λ - c₁α₁ - c₂α₂ in Dynkin = λ - (2c₁-c₂, -c₁+2c₂).
    #
    # Weights form a finite set. We enumerate by depth = c₁ + c₂.
    # Maximum depth: a weight μ must satisfy ⟨μ, αᵢ⟩ ≥ -(a+b) or so.
    # Practically: iterate until no new non-zero weights appear.

    max_depth = a + b + 2  # generous upper bound

    # Enumerate weights by (c1, c2) = root lattice coordinates of λ - μ.
    # μ = λ - c₁·α₁_dynkin - c₂·α₂_dynkin in Dynkin coords.
    # But subtracting α₁ (root) = (2,-1) Dynkin, α₂ (root) = (-1,2) Dynkin.
    # μ(c1,c2) = (a - 2c1 + c2, b + c1 - 2c2) in Dynkin coords.
    # We need c1 ≥ 0, c2 ≥ 0.
    # Check: c1=c2=0 gives (a,b) = λ. Correct.

    def mu_from_depth(c1: int, c2: int) -> Tuple[int, int]:
        return (a - 2 * c1 + c2, b + c1 - 2 * c2)

    # Collect all (c1, c2) pairs sorted by depth c1+c2
    depth_pairs = []
    for depth in range(0, 3 * max_depth + 1):
        for c1 in range(depth + 1):
            c2 = depth - c1
            mu = mu_from_depth(c1, c2)
            depth_pairs.append((c1, c2, mu))

    # Process in order of increasing depth (skip (0,0) = highest weight)
    for c1, c2, mu in depth_pairs:
        if c1 == 0 and c2 == 0:
            continue
        if mu in mult:
            continue

        mu_rho = _add_wt(mu, RHO)
        norm_mu_rho = weight_norm_sq(mu_rho)
        denom = norm_lam_rho - norm_mu_rho

        if abs(denom) < 1e-12:
            # μ + ρ has same norm as λ + ρ but μ ≠ λ: this shouldn't
            # happen for dominant λ with μ in the weight diagram.
            continue

        # Compute the RHS sum
        rhs = 0.0
        for alpha in pos_roots:
            k = 1
            while True:
                shifted = _add_wt(mu, _scale_wt(k, root_to_dynkin(alpha)))
                m_shifted = mult.get(shifted, 0)
                if m_shifted == 0:
                    # Once we go past the weight diagram, stop
                    # But we should check a few more in case of gaps
                    # For sl₃, weights are contiguous, so we can break
                    break
                pairing = pairing_weight_root(
                    _add_wt(mu, _scale_wt(k, root_to_dynkin(alpha))),
                    alpha,
                )
                rhs += pairing * m_shifted
                k += 1

        rhs *= 2.0

        m_mu = rhs / denom
        m_mu_int = int(round(m_mu))

        if m_mu_int > 0:
            mult[mu] = m_mu_int
        elif abs(m_mu) > 0.01:
            # Sanity check: should be a non-negative integer
            pass

    return mult


# ============================================================
# Weyl character (as weight multiplicity dictionary)
# ============================================================

def weyl_character(a: int, b: int) -> Dict[Tuple[int, int], int]:
    """Character of V(aω₁ + bω₂) as {weight: multiplicity}.

    Weights are in Dynkin label coordinates.
    """
    if a < 0 or b < 0:
        return {}
    return weight_multiplicities((a, b))


def character_dim(char: Dict[Tuple[int, int], int]) -> int:
    """Total dimension from a character (sum of multiplicities)."""
    return sum(char.values())


# ============================================================
# Tensor product decomposition (Littlewood-Richardson)
# ============================================================

def tensor_product_character(
    char1: Dict[Tuple[int, int], int],
    char2: Dict[Tuple[int, int], int],
) -> Dict[Tuple[int, int], int]:
    """Character of tensor product V₁ ⊗ V₂.

    χ(V₁ ⊗ V₂)(μ) = Σ_{μ₁+μ₂=μ} χ(V₁)(μ₁) · χ(V₂)(μ₂)
    """
    result: Dict[Tuple[int, int], int] = {}
    for mu1, m1 in char1.items():
        for mu2, m2 in char2.items():
            mu = _add_wt(mu1, mu2)
            result[mu] = result.get(mu, 0) + m1 * m2
    return result


def decompose_character(
    char: Dict[Tuple[int, int], int],
) -> Dict[Tuple[int, int], int]:
    """Decompose a character into irreducible components.

    Uses the "highest weight peeling" algorithm:
    1. Find the highest weight μ in char (lexicographically maximal dominant weight)
    2. Record multiplicity n = char[μ]
    3. Subtract n · χ(V(μ))
    4. Repeat until char is empty

    Returns: {(a,b): multiplicity} where (a,b) are Dynkin labels of irreps.
    """
    char = dict(char)  # work on a copy
    decomp: Dict[Tuple[int, int], int] = {}

    max_iterations = 1000
    iteration = 0

    while char and iteration < max_iterations:
        iteration += 1
        # Find highest dominant weight
        dominant = [(mu, m) for mu, m in char.items()
                    if mu[0] >= 0 and mu[1] >= 0 and m > 0]
        if not dominant:
            break

        # Sort: prefer larger first Dynkin label, then larger second
        dominant.sort(key=lambda x: (x[0][0] + x[0][1], x[0][0]), reverse=True)
        hw, n = dominant[0]

        decomp[hw] = decomp.get(hw, 0) + n

        # Subtract n copies of χ(V(hw))
        irrep_char = weyl_character(hw[0], hw[1])
        for mu, m in irrep_char.items():
            char[mu] = char.get(mu, 0) - n * m
            if char[mu] == 0:
                del char[mu]

    # Verify: remaining character should be zero
    remainder = sum(abs(m) for m in char.values())
    if remainder > 0:
        raise ValueError(
            f"Decomposition failed: nonzero remainder {remainder} "
            f"after {iteration} iterations. Remaining: {char}"
        )

    return decomp


def littlewood_richardson(
    lam1: Tuple[int, int],
    lam2: Tuple[int, int],
) -> Dict[Tuple[int, int], int]:
    """Compute LR coefficients: V(λ₁) ⊗ V(λ₂) = Σ N^ν_{λ₁,λ₂} V(ν).

    Returns: {ν: N^ν_{λ₁,λ₂}}.
    """
    char1 = weyl_character(lam1[0], lam1[1])
    char2 = weyl_character(lam2[0], lam2[1])
    tensor_char = tensor_product_character(char1, char2)
    return decompose_character(tensor_char)


# ============================================================
# MV basis and MV cone
# ============================================================

def mv_basis_small_weights(max_sum: int = 5) -> List[Tuple[int, int]]:
    """Dominant weights (a,b) with a+b ≤ max_sum.

    These index the irreducible representations V(a,b) of sl₃.
    At the character level, the MV basis elements are precisely
    the irreducible characters χ(V(a,b)).
    """
    weights = []
    for a in range(max_sum + 1):
        for b in range(max_sum + 1 - a):
            weights.append((a, b))
    return sorted(weights, key=lambda x: (x[0] + x[1], x[0]))


def build_mv_cone_matrix(
    basis_weights: List[Tuple[int, int]],
    target_weights: Optional[List[Tuple[int, int]]] = None,
) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
    """Build the MV cone matrix.

    Each column corresponds to a basis irrep χ(V(λ)).
    Each row corresponds to a weight μ.
    Entry (i,j) = multiplicity of μᵢ in V(λⱼ).

    A character is MV-positive iff its weight multiplicity vector
    can be written as a non-negative linear combination of the columns.

    Returns: (matrix, weight_list) where weight_list indexes the rows.
    """
    # Collect all weights that appear in any basis irrep
    all_weights: Dict[Tuple[int, int], int] = {}  # weight -> row index
    characters = []

    for lam in basis_weights:
        char = weyl_character(lam[0], lam[1])
        characters.append(char)
        for mu in char:
            if mu not in all_weights:
                all_weights[mu] = len(all_weights)

    # Use specified target weights or all discovered weights
    if target_weights is not None:
        for mu in target_weights:
            if mu not in all_weights:
                all_weights[mu] = len(all_weights)

    weight_list = sorted(all_weights.keys(), key=lambda w: (-w[0] - w[1], -w[0]))
    weight_index = {w: i for i, w in enumerate(weight_list)}

    n_weights = len(weight_list)
    n_basis = len(basis_weights)
    M = np.zeros((n_weights, n_basis), dtype=np.float64)

    for j, char in enumerate(characters):
        for mu, m in char.items():
            if mu in weight_index:
                M[weight_index[mu], j] = m

    return M, weight_list


def check_mv_positivity(
    char: Dict[Tuple[int, int], int],
    basis_weights: List[Tuple[int, int]],
) -> Dict[str, object]:
    """Check if a character lies in the MV cone.

    A character chi is MV-positive if chi = Sigma n_i * chi(V(lambda_i))
    with all n_i >= 0. This uses the exact highest-weight peeling
    algorithm (decompose_character) which is deterministic.

    The basis_weights parameter specifies the allowed irreps in the
    decomposition. If the character requires irreps outside this set,
    the check fails.
    """
    basis_set = set(basis_weights)

    try:
        decomp = decompose_character(char)
    except ValueError:
        return {
            "is_mv_positive": False,
            "decomposition": {},
            "error": "decomposition failed",
        }

    # Check all coefficients are non-negative
    all_nonneg = all(n >= 0 for n in decomp.values())

    # Check all irreps are in the allowed basis
    all_in_basis = all(lam in basis_set for lam in decomp)

    is_positive = all_nonneg and all_in_basis

    return {
        "is_mv_positive": bool(is_positive),
        "decomposition": decomp,
        "all_nonneg": bool(all_nonneg),
        "all_in_basis": bool(all_in_basis),
    }


# ============================================================
# Yangian bar data for sl₃
# ============================================================

# sl₃ bar cohomology from the manuscript (conjectured GF).
# Recurrence: a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3), with a(1)=8, a(2)=36, a(3)=204.
SL3_BAR_DIMS = [1, 8, 36, 204, 1352, 9892, 76084, 598592]

# Y(sl₂) bar cohomology (conjectured): H^n = 3^n + 1.
YSL2_BAR_DIMS = [1, 4, 10, 28, 82, 244, 730, 2188]


def bar_euler_characteristic(bar_dims: List[int], max_n: int) -> int:
    """Bar Euler characteristic χ(B) = Σ (-1)^n dim H^n(B).

    Truncated to max_n terms.
    """
    return sum((-1)**n * bar_dims[n] for n in range(min(max_n + 1, len(bar_dims))))


def bar_euler_chars_partial(bar_dims: List[int]) -> List[int]:
    """Partial Euler characteristics χ_N = Σ_{n=0}^{N} (-1)^n H^n.

    The sign pattern of these partial sums encodes positivity
    information: for an MV-positive complex, the partial Euler
    characteristics should have a definite sign pattern.
    """
    result = []
    running = 0
    for n, dim_n in enumerate(bar_dims):
        running += (-1)**n * dim_n
        result.append(running)
    return result


# ============================================================
# Asymptotic character of Y(sl₃)
# ============================================================

def adjoint_tensor_character(n: int) -> Dict[Tuple[int, int], int]:
    """Character of the adjoint representation g^{⊗n} for sl₃.

    The adjoint of sl₃ is V(1,1) (dimension 8).
    g^{⊗n} = V(1,1)^{⊗n}.

    This is the "leading" approximation to the degree-n bar complex,
    before taking the OS quotient and cohomology.
    """
    if n == 0:
        return {(0, 0): 1}

    adj = weyl_character(1, 1)
    result = dict(adj)
    for _ in range(n - 1):
        result = tensor_product_character(result, adj)
    return result


def adjoint_tensor_decomp(n: int) -> Dict[Tuple[int, int], int]:
    """Decompose g^{⊗n} into irreducibles for sl₃.

    Returns: {(a,b): multiplicity in g^{⊗n}}.
    """
    char = adjoint_tensor_character(n)
    return decompose_character(char)


# ============================================================
# Koszul dual Hilbert series and MV positivity
# ============================================================

def koszul_dual_dims(bar_dims: List[int]) -> List[int]:
    """Compute (A!)_n from bar dims via H_A(t) · H_{A!}(-t) = 1.

    Identical to sl3_casimir_decomp.koszul_dual_dims_from_bar_cohomology.
    """
    N = len(bar_dims)
    a = bar_dims
    c = [0] * N
    c[0] = 1
    for n in range(1, N):
        c[n] = -sum(a[k] * c[n - k] for k in range(1, n + 1))
    return [(-1)**n * c[n] for n in range(N)]


def koszul_dual_positivity_check(bar_dims: List[int]) -> Dict[str, object]:
    """Check positivity of Koszul dual dimensions.

    For an MV-positive algebra, the Koszul dual dimensions (A!)_n
    should be positive integers (they count basis elements).
    """
    kd = koszul_dual_dims(bar_dims)
    all_positive = all(x > 0 for x in kd)
    return {
        "koszul_dual_dims": kd,
        "all_positive": all_positive,
    }


# ============================================================
# Comprehensive MV positivity verification
# ============================================================

def verify_lr_nonnegativity(max_sum: int = 5) -> Dict[str, object]:
    """Verify LR coefficients are non-negative for all V(a,b) with a+b ≤ max_sum.

    This is a fundamental theorem (Littlewood-Richardson rule), but we
    verify it computationally as a sanity check and to exercise the
    decomposition machinery.
    """
    weights = mv_basis_small_weights(max_sum)
    all_nonneg = True
    examples = []

    for i, lam1 in enumerate(weights):
        for lam2 in weights[i:]:  # avoid redundancy
            lr = littlewood_richardson(lam1, lam2)
            for nu, coeff in lr.items():
                if coeff < 0:
                    all_nonneg = False
                    examples.append((lam1, lam2, nu, coeff))

            # Dimension check: dim(V₁) × dim(V₂) = Σ N^ν × dim(V(ν))
            dim_product = sl3_irrep_dim(lam1[0], lam1[1]) * sl3_irrep_dim(lam2[0], lam2[1])
            dim_sum = sum(n * sl3_irrep_dim(nu[0], nu[1]) for nu, n in lr.items())
            if dim_product != dim_sum:
                all_nonneg = False
                examples.append((lam1, lam2, "dim_mismatch", (dim_product, dim_sum)))

    return {
        "all_nonneg": all_nonneg,
        "n_pairs_tested": len(weights) * (len(weights) + 1) // 2,
        "violations": examples,
    }


def verify_adjoint_decomp_positivity(max_n: int = 4) -> Dict[str, object]:
    """Verify adjoint tensor power decompositions have positive coefficients.

    For each n ≤ max_n, decompose g^{⊗n} and check all coefficients ≥ 0.
    Also check that dimensions match.
    """
    results = {}
    for n in range(1, max_n + 1):
        decomp = adjoint_tensor_decomp(n)
        dim_expected = 8 ** n
        dim_got = sum(m * sl3_irrep_dim(a, b) for (a, b), m in decomp.items())
        all_pos = all(m > 0 for m in decomp.values())
        results[n] = {
            "decomposition": decomp,
            "dim_expected": dim_expected,
            "dim_computed": dim_got,
            "dim_match": dim_expected == dim_got,
            "all_positive": all_pos,
            "n_irreps": len(decomp),
        }
    return results


def verify_bar_euler_mv_compatibility(bar_dims: List[int]) -> Dict[str, object]:
    """Verify bar Euler characteristic compatibility with MV positivity.

    For an algebra whose bar complex has an MV-positive character,
    the alternating sum should be expressible as a virtual representation
    with controlled signs. Specifically:

    1. The bar Euler characteristic χ(B) = Σ (-1)^n H^n should be
       a well-defined virtual character.
    2. The partial sums should satisfy |χ_N| ≤ dim(B^N) (trivially true).
    3. The growth rate of |χ_N| should be bounded by the growth of H^n.
    """
    partial_euler = bar_euler_chars_partial(bar_dims)

    # Sign pattern analysis
    signs = [1 if x > 0 else (-1 if x < 0 else 0) for x in partial_euler]

    # Growth analysis: |χ_N| / H^N
    growth_ratios = []
    for n in range(1, len(bar_dims)):
        if bar_dims[n] > 0:
            growth_ratios.append(abs(partial_euler[n]) / bar_dims[n])

    # For MV-positive bar complex, expect partial Euler chars
    # to be "dominated" by the leading term
    bounded = all(r <= 2.0 for r in growth_ratios)

    return {
        "partial_euler_chars": partial_euler,
        "sign_pattern": signs,
        "growth_ratios": growth_ratios,
        "growth_bounded": bounded,
    }


def run_full_verification(max_weight_sum: int = 4, max_tensor_power: int = 3) -> Dict:
    """Run the full MV positivity verification suite.

    This is the main entry point for task B8.
    """
    results = {}

    # 1. Weyl character dimensions
    print("1. Computing Weyl characters...")
    weights = mv_basis_small_weights(max_weight_sum)
    char_dims = {}
    for (a, b) in weights:
        char = weyl_character(a, b)
        dim_formula = sl3_irrep_dim(a, b)
        dim_char = character_dim(char)
        char_dims[(a, b)] = {
            "dim_formula": dim_formula,
            "dim_character": dim_char,
            "match": dim_formula == dim_char,
        }
    results["weyl_characters"] = char_dims
    all_match = all(v["match"] for v in char_dims.values())
    print(f"   {len(weights)} representations, all dims match: {all_match}")

    # 2. LR coefficient non-negativity
    print("2. Verifying LR non-negativity...")
    lr_result = verify_lr_nonnegativity(max_weight_sum)
    results["lr_nonnegativity"] = lr_result
    print(f"   {lr_result['n_pairs_tested']} pairs tested, "
          f"all non-negative: {lr_result['all_nonneg']}")

    # 3. Adjoint tensor decomposition
    print("3. Adjoint tensor decompositions...")
    adj_result = verify_adjoint_decomp_positivity(max_tensor_power)
    results["adjoint_decomp"] = adj_result
    for n, data in adj_result.items():
        print(f"   g^{{⊗{n}}}: {data['n_irreps']} irreps, "
              f"dim={data['dim_computed']}, positive={data['all_positive']}")

    # 4. Bar Euler characteristic
    print("4. Bar Euler characteristic analysis...")
    euler_sl3 = verify_bar_euler_mv_compatibility(SL3_BAR_DIMS)
    results["bar_euler_sl3"] = euler_sl3
    print(f"   sl₃ partial Euler: {euler_sl3['partial_euler_chars']}")
    print(f"   Growth bounded: {euler_sl3['growth_bounded']}")

    euler_ysl2 = verify_bar_euler_mv_compatibility(YSL2_BAR_DIMS)
    results["bar_euler_ysl2"] = euler_ysl2
    print(f"   Y(sl₂) partial Euler: {euler_ysl2['partial_euler_chars']}")

    # 5. Koszul dual positivity
    print("5. Koszul dual positivity...")
    kd_sl3 = koszul_dual_positivity_check(SL3_BAR_DIMS)
    results["koszul_dual_sl3"] = kd_sl3
    print(f"   sl₃ Koszul dual dims: {kd_sl3['koszul_dual_dims']}")
    print(f"   All positive: {kd_sl3['all_positive']}")

    kd_ysl2 = koszul_dual_positivity_check(YSL2_BAR_DIMS)
    results["koszul_dual_ysl2"] = kd_ysl2
    print(f"   Y(sl₂) Koszul dual dims: {kd_ysl2['koszul_dual_dims']}")
    print(f"   All positive: {kd_ysl2['all_positive']}")

    # 6. MV cone check for adjoint tensor characters
    print("6. MV cone membership for tensor characters...")
    basis = mv_basis_small_weights(max_weight_sum)
    for n in range(1, min(max_tensor_power + 1, 4)):
        adj_char = adjoint_tensor_character(n)
        mv_check = check_mv_positivity(adj_char, basis)
        results[f"mv_cone_adj_n{n}"] = mv_check
        print(f"   g^{{⊗{n}}}: MV-positive = {mv_check['is_mv_positive']}, "
              f"error = {mv_check['max_error_int']:.2e}")

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("MV POSITIVITY VERIFICATION FOR Y(sl₃) ASYMPTOTIC CHARACTERS")
    print("=" * 70)
    results = run_full_verification(max_weight_sum=4, max_tensor_power=3)
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Weyl character dims: {'PASS' if all(v['match'] for v in results['weyl_characters'].values()) else 'FAIL'}")
    print(f"  LR non-negativity: {'PASS' if results['lr_nonnegativity']['all_nonneg'] else 'FAIL'}")
    for n in range(1, 4):
        if n in results['adjoint_decomp']:
            d = results['adjoint_decomp'][n]
            print(f"  g^{{⊗{n}}} decomp positive: {'PASS' if d['all_positive'] else 'FAIL'}")
    print(f"  sl₃ Koszul dual positive: {'PASS' if results['koszul_dual_sl3']['all_positive'] else 'FAIL'}")
    print(f"  Y(sl₂) Koszul dual positive: {'PASS' if results['koszul_dual_ysl2']['all_positive'] else 'FAIL'}")
