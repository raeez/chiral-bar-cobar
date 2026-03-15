"""Baxter TQ relation for Y(sl_3) at K_0 level — task B4 for MC3 path.

For Y(sl_3), Zhang's three-term TQ relation generalizes the sl_2 case.
The key identity in K_0(O_Y) is:

    [V_{omega_i}] * [M(lambda)] = sum_{mu in weights(V_{omega_i})} [M(lambda + mu)]

where V_{omega_i} is a fundamental evaluation module and M(lambda) is
a Verma module of highest weight lambda.

This module verifies:
  1. The sl_3 weight lattice (rank 2, simple roots alpha_1, alpha_2).
  2. Kostant partition function for sl_3 (positive roots alpha_1, alpha_2, alpha_1+alpha_2).
  3. Formal characters of finite-dim reps: V_{omega_1} (3-dim standard),
     V_{omega_2} (3-dim dual), V_{omega_1+omega_2} (8-dim adjoint).
  4. Verma module characters M(lambda) with Kostant multiplicities.
  5. TQ relations: [V_{omega_i}] tensor [M(lambda)] = sum [M(lambda+mu)].
  6. Chebyshev-like structure: [V_{omega_1}]^2 = [V_{2*omega_1}] + [V_{omega_2}].
  7. Adjoint rep tensor formula.

Mathematical setup:
  - sl_3 root system: simple roots alpha_1, alpha_2; positive roots alpha_1, alpha_2, alpha_1+alpha_2.
  - Fundamental weights omega_1, omega_2 satisfying <omega_i, alpha_j^vee> = delta_{ij}.
  - In the alpha-basis: omega_1 = (2/3)*alpha_1 + (1/3)*alpha_2,
                         omega_2 = (1/3)*alpha_1 + (2/3)*alpha_2.
  - We work in the omega-basis for weights: lambda = a*omega_1 + b*omega_2 encoded as (a, b).
  - Cartan matrix: A = [[2, -1], [-1, 2]].
  - alpha_1 = 2*omega_1 - omega_2 = (2, -1), alpha_2 = -omega_1 + 2*omega_2 = (-1, 2).
  - Positive roots in omega-basis: alpha_1 = (2,-1), alpha_2 = (-1,2), alpha_1+alpha_2 = (1,1).
  - Weyl group S_3, with reflections s_1, s_2. Weyl vector rho = omega_1 + omega_2 = (1,1).

CONVENTIONS:
  - Cohomological grading (consistent with the monograph).
  - Weights are tuples (a, b) in the omega-basis.
  - K_0 classes are formal sums of weight-space dimensions.

References:
  - yangians.tex, sec:yangian-rep-bar, conj:baxter-exact-triangles
  - Zhang, Shifted Yangians and TQ relations
  - Hernandez-Jimbo, Representations of quantum affinizations
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Weight data types
# ---------------------------------------------------------------------------

# A weight is a tuple (a, b) in the omega-basis (fundamental weight coords).
Weight = Tuple[int, int]

# A formal character is a dict: weight -> multiplicity.
FormalCharacter = Dict[Weight, int]


def weight_add(w1: Weight, w2: Weight) -> Weight:
    """Add two weights in the omega-basis."""
    return (w1[0] + w2[0], w1[1] + w2[1])


def weight_sub(w1: Weight, w2: Weight) -> Weight:
    """Subtract two weights."""
    return (w1[0] - w2[0], w1[1] - w2[1])


def weight_neg(w: Weight) -> Weight:
    """Negate a weight."""
    return (-w[0], -w[1])


def weight_scale(n: int, w: Weight) -> Weight:
    """Scale a weight by an integer."""
    return (n * w[0], n * w[1])


# ---------------------------------------------------------------------------
# sl_3 root data
# ---------------------------------------------------------------------------

# Simple roots in omega-basis: alpha_i = sum_j A_{ij} omega_j
# where A is the Cartan matrix [[2,-1],[-1,2]].
ALPHA_1: Weight = (2, -1)
ALPHA_2: Weight = (-1, 2)
ALPHA_12: Weight = (1, 1)  # alpha_1 + alpha_2

# All positive roots
POSITIVE_ROOTS: List[Weight] = [ALPHA_1, ALPHA_2, ALPHA_12]

# Fundamental weights
OMEGA_1: Weight = (1, 0)
OMEGA_2: Weight = (0, 1)

# Weyl vector
RHO: Weight = (1, 1)

# Cartan matrix
CARTAN_MATRIX = [[2, -1], [-1, 2]]


def inner_product(w1: Weight, w2: Weight) -> int:
    """Compute the inner product <w1, w2> using the inverse Cartan matrix.

    The bilinear form on the weight lattice is given by:
        <omega_i, omega_j> = (A^{-1})_{ij}

    For sl_3: A^{-1} = (1/3) * [[2, 1], [1, 2]].

    To keep things integral, we return 3 * <w1, w2>.
    """
    # 3 * <w1, w2> = 2*a1*a2 + (a1*b2 + b1*a2) + 2*b1*b2
    return 2 * w1[0] * w2[0] + w1[0] * w2[1] + w1[1] * w2[0] + 2 * w1[1] * w2[1]


def pairing(w: Weight, coroot_index: int) -> int:
    """Compute <w, alpha_i^vee> = sum_j A_{ij} * w_j (in omega coords).

    Actually, since w = sum_k w_k omega_k and <omega_k, alpha_i^vee> = delta_{ki},
    we have <w, alpha_i^vee> = w_i (the i-th Dynkin label).

    Wait, that's the definition: <omega_i, alpha_j^vee> = delta_{ij},
    so <w, alpha_j^vee> = w_j (j-th coordinate in omega-basis).
    """
    if coroot_index == 1:
        return w[0]
    elif coroot_index == 2:
        return w[1]
    else:
        raise ValueError(f"Invalid coroot index: {coroot_index}")


# ---------------------------------------------------------------------------
# Weyl group
# ---------------------------------------------------------------------------

def weyl_reflect_s1(w: Weight) -> Weight:
    """Simple reflection s_1: w -> w - <w, alpha_1^vee> * alpha_1.

    <w, alpha_1^vee> = w[0] (the first Dynkin label).
    s_1(a, b) = (a, b) - a * (2, -1) = (-a, b + a).
    """
    a, b = w
    return (-a, b + a)


def weyl_reflect_s2(w: Weight) -> Weight:
    """Simple reflection s_2: w -> w - <w, alpha_2^vee> * alpha_2.

    <w, alpha_2^vee> = w[1].
    s_2(a, b) = (a, b) - b * (-1, 2) = (a + b, -b).
    """
    a, b = w
    return (a + b, -b)


def weyl_orbit(w: Weight) -> List[Weight]:
    """Compute the full Weyl orbit of a weight under S_3.

    The Weyl group of sl_3 is S_3, generated by s_1, s_2.
    Elements: {1, s_1, s_2, s_1 s_2, s_2 s_1, s_1 s_2 s_1 = w_0}.
    """
    orbit = set()
    # Generate by applying s_1, s_2 repeatedly
    queue = [w]
    while queue:
        v = queue.pop()
        if v in orbit:
            continue
        orbit.add(v)
        queue.append(weyl_reflect_s1(v))
        queue.append(weyl_reflect_s2(v))
    return sorted(orbit)


def is_dominant(w: Weight) -> bool:
    """Check if a weight is dominant: all Dynkin labels >= 0."""
    return w[0] >= 0 and w[1] >= 0


# ---------------------------------------------------------------------------
# Kostant partition function
# ---------------------------------------------------------------------------

def kostant_partition(beta: Weight, max_depth: int = 100) -> int:
    """Compute the Kostant partition function p(beta) for sl_3.

    p(beta) = number of ways to write beta = n_1*alpha_1 + n_2*alpha_2 + n_3*(alpha_1+alpha_2)
    with n_1, n_2, n_3 >= 0.

    In omega-coordinates:
      n_1*(2,-1) + n_2*(-1,2) + n_3*(1,1) = (a, b)

    This gives:
      2*n_1 - n_2 + n_3 = a
      -n_1 + 2*n_2 + n_3 = b

    Adding: n_1 + n_2 + 2*n_3 = a + b, so n_3 ranges over [0, (a+b)//2].
    From the first equation: n_1 = (a + n_2 - n_3) / 2... let me solve more carefully.

    From the two equations:
      n_1 = (2a + b - 3*n_3) / 3  (from 2*eq1 + eq2)
        Wait: 2*(2n_1 - n_2 + n_3) + (-n_1 + 2n_2 + n_3) = 2a + b
              3n_1 + 3n_3 = 2a + b, so n_1 = (2a + b - 3n_3) / 3.
      Similarly: n_2 = (a + 2b - 3n_3) / 3.

    So for p(beta) > 0: we need 2a+b and a+2b both divisible by 3 (mod n_3 adjustments).

    Actually, let me just solve directly. We need:
      2*n_1 - n_2 + n_3 = a
      -n_1 + 2*n_2 + n_3 = b
      n_1, n_2, n_3 >= 0

    Sum: n_1 + n_2 + 2*n_3 = a + b.
    Subtract eq2 from eq1: 3*n_1 - 3*n_2 = a - b, so n_1 - n_2 = (a-b)/3.

    Hmm, (a-b) might not be divisible by 3. Let's use a brute force approach
    which is simpler and correct.
    """
    a, b = beta
    count = 0
    # n_3 * (1,1): contributes (n_3, n_3)
    # Remaining: (a - n_3, b - n_3) must be n_1*(2,-1) + n_2*(-1,2)
    # 2*n_1 - n_2 = a - n_3
    # -n_1 + 2*n_2 = b - n_3
    # Solve: 3*n_1 = 2*(a-n_3) + (b-n_3) = 2a+b - 3*n_3
    #        3*n_2 = (a-n_3) + 2*(b-n_3) = a+2b - 3*n_3
    for n_3 in range(max_depth):
        num_1 = 2 * a + b - 3 * n_3
        num_2 = a + 2 * b - 3 * n_3
        if num_1 < 0 or num_2 < 0:
            break
        if num_1 % 3 != 0 or num_2 % 3 != 0:
            continue
        n_1 = num_1 // 3
        n_2 = num_2 // 3
        if n_1 >= 0 and n_2 >= 0:
            count += 1
    return count



# ---------------------------------------------------------------------------
# Finite-dimensional representations
# ---------------------------------------------------------------------------

def weyl_dimension(hw: Weight) -> int:
    """Dimension of the irreducible sl_3 representation with highest weight hw.

    Weyl dimension formula for sl_3:
      dim V(a*omega_1 + b*omega_2) = (a+1)(b+1)(a+b+2)/2.
    """
    a, b = hw
    if a < 0 or b < 0:
        return 0
    return (a + 1) * (b + 1) * (a + b + 2) // 2


def sl3_fd_character(hw: Weight, max_depth: int = 50) -> FormalCharacter:
    """Formal character of the irreducible finite-dimensional sl_3 rep V(hw).

    Uses the Freudenthal multiplicity formula to compute weight multiplicities.

    For general highest weights (a, b) with a, b >= 0:
    - Weights are lambda - (n_1*alpha_1 + n_2*alpha_2) with n_i >= 0,
      constrained to be in the convex hull of the Weyl orbit of lambda.
    - Multiplicities computed by Freudenthal recursion.
    """
    a, b = hw
    if a < 0 or b < 0:
        return {}

    # Trivial rep
    if (a, b) == (0, 0):
        return {(0, 0): 1}

    return _freudenthal_character(hw, max_depth)


def _weight_level(hw: Weight, mu: Weight) -> int:
    """Compute the level of mu below hw.

    The level is defined as n_1 + n_2 where hw - mu = n_1*alpha_1 + n_2*alpha_2
    in the simple root basis. Since alpha_1 = (2,-1) and alpha_2 = (-1,2),
    we solve: (2,-1)*n_1 + (-1,2)*n_2 = hw - mu.

    Returns -1 if hw - mu is not a non-negative integer combination of simple roots.
    """
    da, db = weight_sub(hw, mu)
    # 2*n_1 - n_2 = da, -n_1 + 2*n_2 = db
    # 3*n_1 = 2*da + db, 3*n_2 = da + 2*db
    num_1 = 2 * da + db
    num_2 = da + 2 * db
    if num_1 < 0 or num_2 < 0:
        return -1
    if num_1 % 3 != 0 or num_2 % 3 != 0:
        return -1
    n_1 = num_1 // 3
    n_2 = num_2 // 3
    return n_1 + n_2


def _is_in_weight_polytope(hw: Weight, mu: Weight) -> bool:
    """Check if mu is in the weight polytope of V(hw).

    A weight mu is in the convex hull of W * hw iff for every positive
    root alpha, we have |<mu, alpha^vee>| <= <hw, alpha^vee> when hw is
    dominant.

    For sl_3 with dominant hw = (a, b), the conditions are:
      |<mu, alpha_1^vee>| <= a, i.e., |mu[0]| <= a
      |<mu, alpha_2^vee>| <= b, i.e., |mu[1]| <= b
      |<mu, (alpha_1+alpha_2)^vee>| <= a+b, i.e., |mu[0]+mu[1]| <= a+b

    Wait: alpha_1^vee pairs with omega_i as delta_{1i}, so <mu, alpha_1^vee> = mu[0].
    And (alpha_1+alpha_2)^vee = alpha_1^vee + alpha_2^vee, so
    <mu, (alpha_1+alpha_2)^vee> = mu[0] + mu[1].

    The conditions are: for every w in W and every simple root alpha_i,
    <w(mu), alpha_i^vee> <= <hw, alpha_i^vee>. Equivalently, for every
    positive root alpha: <mu, alpha^vee> <= <hw, alpha^vee>.
    And since W acts, also: <w_0(mu), alpha^vee> <= <hw, alpha^vee>,
    which gives -<mu, w_0(alpha^vee)> <= <hw, alpha^vee>.
    Since w_0 permutes positive roots (for sl_3, w_0 swaps alpha_1, alpha_2
    and fixes alpha_1+alpha_2 up to sign), we get:

    For sl_3, the necessary and sufficient conditions for mu in the
    convex hull of W*hw (with hw = (a,b) dominant) are:
      (i)   mu[0] + mu[1] <= a + b   (from alpha_1+alpha_2)
      (ii)  mu[0] - 2*mu[1] <= 2*a - b  ... Hmm, this is getting complicated.

    Let me just use the characterization: mu is in the weight polytope iff
    for every w in W, hw - w(mu) is a non-negative rational combination of
    simple roots. Since we're on the weight lattice, we check that
    _weight_level(hw, w(mu)) >= 0 for all w in W.
    """
    for w_mu in weyl_orbit(mu):
        if _weight_level(hw, w_mu) < 0:
            return False
    return True


def _enumerate_weights_fd(hw: Weight) -> List[Weight]:
    """Enumerate all weights of the finite-dim rep V(hw).

    We enumerate mu = hw - n_1*alpha_1 - n_2*alpha_2 for n_1, n_2 >= 0,
    and check that mu is in the weight polytope (convex hull of W*hw).
    """
    a, b = hw
    # The lowest weight is w_0(hw) = (-b, -a).
    # hw - w_0(hw) = (a+b, a+b). In simple root coords:
    # (a+b, a+b) = n_1*(2,-1) + n_2*(-1,2), solving: 3n_1 = 3(a+b), n_1 = a+b, n_2 = a+b.
    # So max n_1 = max n_2 = a + b.
    max_n = a + b
    weights = []
    for n_1 in range(max_n + 1):
        for n_2 in range(max_n + 1):
            mu = weight_sub(hw, weight_add(weight_scale(n_1, ALPHA_1),
                                            weight_scale(n_2, ALPHA_2)))
            if _is_in_weight_polytope(hw, mu):
                weights.append(mu)
    return weights


def _freudenthal_character(hw: Weight, max_depth: int = 50) -> FormalCharacter:
    """Compute character via Freudenthal's multiplicity formula.

    The formula is:
      (<lambda+rho, lambda+rho> - <mu+rho, mu+rho>) * m(mu)
        = 2 * sum_{alpha > 0} sum_{k >= 1} <mu + k*alpha, alpha> * m(mu + k*alpha)

    where m(mu) is the multiplicity of weight mu in V(lambda).
    We use our inner_product which returns 3*<,> to keep everything integral.
    """
    result: FormalCharacter = {hw: 1}

    # Compute 3 * <lambda+rho, lambda+rho>
    lam_rho = weight_add(hw, RHO)
    norm_lam_rho = inner_product(lam_rho, lam_rho)

    # Enumerate all potential weights and sort by level (highest first)
    all_weights = _enumerate_weights_fd(hw)
    # Sort by level below hw (ascending), so we process higher weights first
    all_weights.sort(key=lambda mu: _weight_level(hw, mu))

    for mu in all_weights:
        if mu == hw:
            continue  # Already set to 1

        mu_rho = weight_add(mu, RHO)
        norm_mu_rho = inner_product(mu_rho, mu_rho)
        denominator = norm_lam_rho - norm_mu_rho

        if denominator == 0:
            # mu + rho is a Weyl translate of hw + rho -> this shouldn't
            # happen for mu != hw in the interior. But if it does,
            # the multiplicity equals that of hw (= 1).
            result[mu] = 1
            continue

        numerator = 0
        for alpha in POSITIVE_ROOTS:
            k = 1
            while True:
                mu_k_alpha = weight_add(mu, weight_scale(k, alpha))
                m_upper = result.get(mu_k_alpha, 0)
                if m_upper == 0:
                    break
                # 3 * <mu + k*alpha, alpha>
                ip = inner_product(mu_k_alpha, alpha)
                numerator += 2 * ip * m_upper
                k += 1

        mult = numerator // denominator
        if mult > 0:
            result[mu] = mult

    return {w: m for w, m in result.items() if m > 0}


def standard_rep_character() -> FormalCharacter:
    """Character of V_{omega_1} (3-dimensional standard representation).

    Weights: omega_1, omega_2 - omega_1, -omega_2
    In omega-basis: (1,0), (-1,1), (0,-1).
    All multiplicities 1.
    """
    return {(1, 0): 1, (-1, 1): 1, (0, -1): 1}


def dual_rep_character() -> FormalCharacter:
    """Character of V_{omega_2} (3-dimensional dual representation).

    Weights: omega_2, omega_1 - omega_2, -omega_1
    In omega-basis: (0,1), (1,-1), (-1,0).
    All multiplicities 1.
    """
    return {(0, 1): 1, (1, -1): 1, (-1, 0): 1}


def adjoint_rep_character() -> FormalCharacter:
    """Character of V_{omega_1 + omega_2} (8-dimensional adjoint representation).

    Weights of sl_3 adjoint:
    - Roots: +-alpha_1, +-alpha_2, +-(alpha_1+alpha_2) — 6 weights, multiplicity 1 each
    - Zero weight: (0,0) with multiplicity 2 (rank of sl_3)

    In omega-basis:
    - alpha_1 = (2,-1), -alpha_1 = (-2,1)
    - alpha_2 = (-1,2), -alpha_2 = (1,-2)
    - alpha_1+alpha_2 = (1,1), -(alpha_1+alpha_2) = (-1,-1)
    - 0 = (0,0) with multiplicity 2
    """
    return {
        (2, -1): 1, (-2, 1): 1,
        (-1, 2): 1, (1, -2): 1,
        (1, 1): 1, (-1, -1): 1,
        (0, 0): 2,
    }


def symmetric_square_character() -> FormalCharacter:
    """Character of V_{2*omega_1} (6-dimensional symmetric square of standard).

    Highest weight (2,0). Weyl dimension = 3*1*4/2 = 6.
    Weights: (2,0), (0,1), (-2,2), (1,-1), (-1,0), (0,-2).
    Wait, let me compute carefully.

    V(2,0) = Sym^2(V(1,0)).
    Weights of V(1,0): (1,0), (-1,1), (0,-1).
    Sym^2 weights: all (wi + wj) for i <= j:
      (1,0)+(1,0) = (2,0)
      (1,0)+(-1,1) = (0,1)
      (1,0)+(0,-1) = (1,-1)
      (-1,1)+(-1,1) = (-2,2)
      (-1,1)+(0,-1) = (-1,0)
      (0,-1)+(0,-1) = (0,-2)
    All multiplicity 1. Total: 6 weights.
    """
    return {
        (2, 0): 1, (0, 1): 1, (1, -1): 1,
        (-2, 2): 1, (-1, 0): 1, (0, -2): 1,
    }


def dual_symmetric_square_character() -> FormalCharacter:
    """Character of V_{2*omega_2} (6-dimensional symmetric square of dual).

    Highest weight (0,2). Dim = 1*3*4/2 = 6.
    Weights: negatives of V(2,0) weights (since V(0,2) = V(2,0)*).
    """
    return {weight_neg(w): m for w, m in symmetric_square_character().items()}


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def tensor_product_characters(chi1: FormalCharacter,
                              chi2: FormalCharacter) -> FormalCharacter:
    """Compute the character of the tensor product.

    (chi1 tensor chi2)(mu) = sum_{mu1 + mu2 = mu} chi1(mu1) * chi2(mu2).
    """
    result: FormalCharacter = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = weight_add(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def sum_characters(*chars: FormalCharacter) -> FormalCharacter:
    """Compute the direct sum of formal characters."""
    result: FormalCharacter = {}
    for chi in chars:
        for w, m in chi.items():
            result[w] = result.get(w, 0) + m
    return result


def subtract_characters(chi1: FormalCharacter,
                        chi2: FormalCharacter) -> FormalCharacter:
    """Subtract chi2 from chi1 (for exact sequence verification)."""
    result = dict(chi1)
    for w, m in chi2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


def formal_character_equal(chi1: FormalCharacter,
                           chi2: FormalCharacter) -> bool:
    """Compare two formal characters.

    For infinite-dimensional modules, both should be truncated to the
    same depth before comparison.
    """
    all_weights = set(chi1.keys()) | set(chi2.keys())
    for w in all_weights:
        if chi1.get(w, 0) != chi2.get(w, 0):
            return False
    return True


def character_dimension(chi: FormalCharacter) -> int:
    """Total dimension (sum of all multiplicities)."""
    return sum(chi.values())


# ---------------------------------------------------------------------------
# Verma module characters
# ---------------------------------------------------------------------------

def sl3_verma_character(lam: Weight, depth: int = 10) -> FormalCharacter:
    """Formal character of the Verma module M(lambda) for sl_3.

    M(lambda) has weights lambda - beta with multiplicity p(beta),
    where p is the Kostant partition function: the number of ways
    to write beta as a non-negative integer combination of positive roots.

    The depth parameter controls how far below lambda we go:
    we enumerate all beta = n_1*alpha_1 + n_2*alpha_2 for
    0 <= n_1, n_2 <= depth (simple root coefficients).

    Each such beta has multiplicity p(beta) computed exactly by the
    Kostant partition function (which also counts decompositions using
    the non-simple positive root alpha_1+alpha_2).
    """
    result: FormalCharacter = {}

    for n_1 in range(depth + 1):
        for n_2 in range(depth + 1):
            # beta in simple root coordinates: n_1*alpha_1 + n_2*alpha_2
            beta = weight_add(weight_scale(n_1, ALPHA_1),
                              weight_scale(n_2, ALPHA_2))
            mu = weight_sub(lam, beta)
            p = kostant_partition(beta)
            if p > 0:
                result[mu] = p

    return result



# ---------------------------------------------------------------------------
# Baxter TQ relation in K_0
# ---------------------------------------------------------------------------

def baxter_tq_standard(lam: Weight, depth: int = 10) -> Tuple[FormalCharacter,
                                                                FormalCharacter]:
    """Verify the TQ relation for V_{omega_1} (standard rep) in K_0.

    [V_{omega_1}] * [M(lambda)] = [M(lambda + omega_1)]
                                 + [M(lambda + omega_2 - omega_1)]
                                 + [M(lambda - omega_2)]

    The shifts are the weights of V_{omega_1}: (1,0), (-1,1), (0,-1).

    Returns:
        (lhs_character, rhs_character).
    """
    V_std = standard_rep_character()
    M_lam = sl3_verma_character(lam, depth=depth)

    # LHS: tensor product
    lhs = tensor_product_characters(V_std, M_lam)

    # RHS: sum of shifted Verma modules
    weights_of_V = [(1, 0), (-1, 1), (0, -1)]
    summands = [sl3_verma_character(weight_add(lam, mu), depth=depth)
                for mu in weights_of_V]
    rhs = sum_characters(*summands)

    return lhs, rhs


def verify_baxter_tq_standard(lam: Weight, depth: int = 10) -> bool:
    """Check the TQ identity for V_{omega_1} at K_0 level."""
    lhs, rhs = baxter_tq_standard(lam, depth=depth)
    return formal_character_equal(lhs, rhs)


def baxter_tq_dual(lam: Weight, depth: int = 10) -> Tuple[FormalCharacter,
                                                            FormalCharacter]:
    """Verify the TQ relation for V_{omega_2} (dual rep) in K_0.

    [V_{omega_2}] * [M(lambda)] = [M(lambda + omega_2)]
                                 + [M(lambda + omega_1 - omega_2)]
                                 + [M(lambda - omega_1)]

    The shifts are the weights of V_{omega_2}: (0,1), (1,-1), (-1,0).
    """
    V_dual = dual_rep_character()
    M_lam = sl3_verma_character(lam, depth=depth)

    lhs = tensor_product_characters(V_dual, M_lam)

    weights_of_V = [(0, 1), (1, -1), (-1, 0)]
    summands = [sl3_verma_character(weight_add(lam, mu), depth=depth)
                for mu in weights_of_V]
    rhs = sum_characters(*summands)

    return lhs, rhs


def verify_baxter_tq_dual(lam: Weight, depth: int = 10) -> bool:
    """Check the TQ identity for V_{omega_2} at K_0 level."""
    lhs, rhs = baxter_tq_dual(lam, depth=depth)
    return formal_character_equal(lhs, rhs)


def baxter_tq_adjoint(lam: Weight, depth: int = 10) -> Tuple[FormalCharacter,
                                                               FormalCharacter]:
    """Verify the TQ relation for V_{omega_1 + omega_2} (adjoint rep) in K_0.

    [V_{adj}] * [M(lambda)] = sum_{mu in weights(adj)} mult(mu) * [M(lambda + mu)]

    The adjoint has 8 weights (with the zero weight having multiplicity 2):
      (2,-1), (-2,1), (-1,2), (1,-2), (1,1), (-1,-1) — mult 1 each
      (0,0) — mult 2
    """
    V_adj = adjoint_rep_character()
    M_lam = sl3_verma_character(lam, depth=depth)

    lhs = tensor_product_characters(V_adj, M_lam)

    # RHS: sum over weights of adjoint (with multiplicities)
    rhs: FormalCharacter = {}
    for mu, mult in V_adj.items():
        M_shifted = sl3_verma_character(weight_add(lam, mu), depth=depth)
        for w, m in M_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    return lhs, rhs


def verify_baxter_tq_adjoint(lam: Weight, depth: int = 10) -> bool:
    """Check the TQ identity for the adjoint rep at K_0 level."""
    lhs, rhs = baxter_tq_adjoint(lam, depth=depth)
    return formal_character_equal(lhs, rhs)


def baxter_tq_general(V_char: FormalCharacter, lam: Weight,
                       depth: int = 10) -> Tuple[FormalCharacter, FormalCharacter]:
    """General TQ relation for any finite-dim rep V.

    [V] * [M(lambda)] = sum_{mu in weights(V)} mult_V(mu) * [M(lambda + mu)]

    This is the Clebsch-Gordan decomposition at K_0 level for Verma modules.
    """
    M_lam = sl3_verma_character(lam, depth=depth)
    lhs = tensor_product_characters(V_char, M_lam)

    rhs: FormalCharacter = {}
    for mu, mult in V_char.items():
        M_shifted = sl3_verma_character(weight_add(lam, mu), depth=depth)
        for w, m in M_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    return lhs, rhs


def verify_baxter_tq_general(V_char: FormalCharacter, lam: Weight,
                              depth: int = 10) -> bool:
    """Verify the general TQ identity."""
    lhs, rhs = baxter_tq_general(V_char, lam, depth=depth)
    return formal_character_equal(lhs, rhs)


# ---------------------------------------------------------------------------
# Short exact sequence (filtration) structure
# ---------------------------------------------------------------------------

def ses_dimension_check_standard(lam: Weight,
                                  depth: int = 10) -> Dict[Weight, Tuple[int, int]]:
    """Weight-by-weight comparison for the standard rep TQ identity.

    For each weight mu:
      dim(V_{omega_1} tensor M(lam))_mu = sum_{nu in weights(V)} dim M(lam+nu)_mu

    Returns dict: weight -> (dim_tensor, dim_rhs).
    """
    V_std = standard_rep_character()
    M_lam = sl3_verma_character(lam, depth=depth)
    tensor = tensor_product_characters(V_std, M_lam)

    weights_of_V = [(1, 0), (-1, 1), (0, -1)]
    rhs: FormalCharacter = {}
    for mu in weights_of_V:
        M_shifted = sl3_verma_character(weight_add(lam, mu), depth=depth)
        for w, m in M_shifted.items():
            rhs[w] = rhs.get(w, 0) + m

    all_weights = set(tensor.keys()) | set(rhs.keys())
    result = {}
    for w in all_weights:
        result[w] = (tensor.get(w, 0), rhs.get(w, 0))
    return result


def verify_ses_standard(lam: Weight, depth: int = 10) -> bool:
    """Verify the SES holds weight-by-weight for the standard rep."""
    data = ses_dimension_check_standard(lam, depth=depth)
    return all(d_t == d_r for d_t, d_r in data.values())


# ---------------------------------------------------------------------------
# Chebyshev-like structure / fusion rules
# ---------------------------------------------------------------------------

def verify_clebsch_gordan_V1_squared() -> bool:
    """Verify [V_{omega_1}]^2 = [V_{2*omega_1}] + [V_{omega_2}] in K_0.

    This is the sl_3 Clebsch-Gordan decomposition:
      V(1,0) tensor V(1,0) = V(2,0) + V(0,1)
    (Sym^2 + Lambda^2 of the standard rep)

    Dimensions: 3 * 3 = 9 = 6 + 3.
    """
    V_std = standard_rep_character()
    product = tensor_product_characters(V_std, V_std)

    V_sym2 = symmetric_square_character()  # V(2,0), dim 6
    V_dual = dual_rep_character()  # V(0,1), dim 3

    rhs = sum_characters(V_sym2, V_dual)
    return formal_character_equal(product, rhs)


def verify_clebsch_gordan_V2_squared() -> bool:
    """Verify [V_{omega_2}]^2 = [V_{2*omega_2}] + [V_{omega_1}].

    V(0,1) tensor V(0,1) = V(0,2) + V(1,0).
    Dimensions: 3 * 3 = 9 = 6 + 3.
    """
    V_dual = dual_rep_character()
    product = tensor_product_characters(V_dual, V_dual)

    V_dsym2 = dual_symmetric_square_character()  # V(0,2), dim 6
    V_std = standard_rep_character()  # V(1,0), dim 3

    rhs = sum_characters(V_dsym2, V_std)
    return formal_character_equal(product, rhs)


def verify_clebsch_gordan_V1_V2() -> bool:
    """Verify [V_{omega_1}] * [V_{omega_2}] = [V_{omega_1+omega_2}] + [V_0].

    V(1,0) tensor V(0,1) = V(1,1) + V(0,0).
    Dimensions: 3 * 3 = 9 = 8 + 1.
    """
    V_std = standard_rep_character()
    V_dual = dual_rep_character()
    product = tensor_product_characters(V_std, V_dual)

    V_adj = adjoint_rep_character()  # V(1,1), dim 8
    V_triv = {(0, 0): 1}  # V(0,0), dim 1

    rhs = sum_characters(V_adj, V_triv)
    return formal_character_equal(product, rhs)


def verify_adjoint_decomposition() -> bool:
    """Verify the adjoint tensor product decomposition.

    V(1,1) tensor V(1,0) = V(2,1) + V(0,2) + V(1,0).
    Dimensions: 8 * 3 = 24 = 15 + 6 + 3.

    Weights of V(2,1): Weyl dim = 3*2*5/2 = 15.
    Weights of V(0,2): Weyl dim = 1*3*4/2 = 6.
    Weights of V(1,0): dim 3.
    """
    V_adj = adjoint_rep_character()
    V_std = standard_rep_character()
    product = tensor_product_characters(V_adj, V_std)

    V_21 = sl3_fd_character((2, 1))
    V_02 = sl3_fd_character((0, 2))
    V_10 = standard_rep_character()

    rhs = sum_characters(V_21, V_02, V_10)
    return formal_character_equal(product, rhs)


# ---------------------------------------------------------------------------
# Kostant partition function verification
# ---------------------------------------------------------------------------

def verify_kostant_basic() -> bool:
    """Verify basic values of the Kostant partition function.

    p(0) = 1 (empty sum).
    p(alpha_i) = 1 for each simple root.
    p(alpha_1 + alpha_2) = 2 (either alpha_1+alpha_2 as one root, or alpha_1 + alpha_2 separately).
    p(2*alpha_1) = 1 (only 2*alpha_1, since alpha_1+alpha_2 - alpha_2 uses negative coeff).

    Wait: p(2*alpha_1 + alpha_2) = ?
    2*alpha_1 + alpha_2 in omega-coords: 2*(2,-1) + (-1,2) = (3,0).
    Decompositions: n_1*alpha_1 + n_2*alpha_2 + n_3*alpha_12 = (3,0).
    (3,0) = 2*n_1 - n_2 + n_3 = 3, -n_1 + 2*n_2 + n_3 = 0.
    From second: n_1 = 2*n_2 + n_3. Sub into first: 2*(2*n_2+n_3) - n_2 + n_3 = 3*n_2 + 3*n_3 = 3.
    So n_2 + n_3 = 1. Solutions: (n_2,n_3) in {(0,1),(1,0)}.
    (0,1): n_1=1, check: 2-0+1=3, -1+0+1=0. Yes.
    (1,0): n_1=2, check: 4-1+0=3, -2+2+0=0. Yes.
    So p(3,0) = 2.
    """
    checks = [
        (kostant_partition((0, 0)), 1),
        (kostant_partition(ALPHA_1), 1),
        (kostant_partition(ALPHA_2), 1),
        (kostant_partition(ALPHA_12), 2),  # alpha_1+alpha_2 as single root, OR alpha_1 + alpha_2
        (kostant_partition((4, -2)), 1),   # 2*alpha_1 = (4,-2): only 2*alpha_1
        (kostant_partition((3, 0)), 2),    # 2*alpha_1 + alpha_2 (see above)
    ]
    return all(actual == expected for actual, expected in checks)


def verify_kostant_verma_top() -> bool:
    """Verify that the top weight of M(lambda) has multiplicity 1.

    p((0,0)) = 1, so lambda itself appears with multiplicity 1.
    """
    return kostant_partition((0, 0)) == 1


# ---------------------------------------------------------------------------
# Shift operator interpretation
# ---------------------------------------------------------------------------

def verify_shift_operator_standard(max_tests: int = 5, depth: int = 8) -> bool:
    """Verify that [V_{omega_1}] acts as a 3-term shift operator on the
    lattice of Verma module classes.

    [V_{omega_1}] * [M(a,b)] = [M(a+1,b)] + [M(a-1,b+1)] + [M(a,b-1)]
    """
    for a in range(max_tests):
        for b in range(max_tests):
            if not verify_baxter_tq_standard((a, b), depth=depth):
                return False
    return True


def verify_shift_operator_dual(max_tests: int = 5, depth: int = 8) -> bool:
    """Verify that [V_{omega_2}] acts as a 3-term shift operator.

    [V_{omega_2}] * [M(a,b)] = [M(a,b+1)] + [M(a+1,b-1)] + [M(a-1,b)]
    """
    for a in range(max_tests):
        for b in range(max_tests):
            if not verify_baxter_tq_dual((a, b), depth=depth):
                return False
    return True


# ---------------------------------------------------------------------------
# K_0 lattice generation
# ---------------------------------------------------------------------------

def build_k0_lattice_standard(max_a: int = 4, max_b: int = 4,
                               depth: int = 8) -> Dict[Weight, FormalCharacter]:
    """Build a portion of the K_0 lattice using the standard TQ relation.

    Starting from M(0,0), recursively apply:
      [M(a+1,b)] = [V_{omega_1}] * [M(a,b)] - [M(a-1,b+1)] - [M(a,b-1)]

    We precompute M for a grid and verify consistency.
    """
    lattice: Dict[Weight, FormalCharacter] = {}
    for a in range(max_a + 1):
        for b in range(max_b + 1):
            lattice[(a, b)] = sl3_verma_character((a, b), depth=depth)
    return lattice


def verify_k0_lattice_consistency(max_a: int = 3, max_b: int = 3,
                                   depth: int = 8) -> bool:
    """Verify that the K_0 lattice is consistent with the TQ relation.

    For each (a,b) in the grid, check:
      [V_{omega_1}] * [M(a,b)] = [M(a+1,b)] + [M(a-1,b+1)] + [M(a,b-1)]
    """
    V_std = standard_rep_character()
    for a in range(max_a + 1):
        for b in range(max_b + 1):
            lam = (a, b)
            M_lam = sl3_verma_character(lam, depth=depth)
            tensor = tensor_product_characters(V_std, M_lam)

            weights_of_V = [(1, 0), (-1, 1), (0, -1)]
            rhs: FormalCharacter = {}
            for mu in weights_of_V:
                M_shifted = sl3_verma_character(weight_add(lam, mu), depth=depth)
                for w, m in M_shifted.items():
                    rhs[w] = rhs.get(w, 0) + m

            if not formal_character_equal(tensor, rhs):
                return False
    return True


# ---------------------------------------------------------------------------
# Verification suite
# ---------------------------------------------------------------------------

def verify_all() -> Dict[str, bool]:
    """Run all verification checks."""
    results = {}

    # Kostant partition function
    results["Kostant basic values"] = verify_kostant_basic()
    results["Kostant top weight p(0)=1"] = verify_kostant_verma_top()

    # Finite-dim character dimensions
    results["dim V(1,0) = 3"] = character_dimension(standard_rep_character()) == 3
    results["dim V(0,1) = 3"] = character_dimension(dual_rep_character()) == 3
    results["dim V(1,1) = 8"] = character_dimension(adjoint_rep_character()) == 8
    results["dim V(2,0) = 6"] = character_dimension(symmetric_square_character()) == 6
    results["dim V(0,2) = 6"] = character_dimension(dual_symmetric_square_character()) == 6

    # Weyl dimension formula
    for hw, expected_dim in [((0, 0), 1), ((1, 0), 3), ((0, 1), 3),
                             ((1, 1), 8), ((2, 0), 6), ((0, 2), 6),
                             ((2, 1), 15), ((1, 2), 15), ((3, 0), 10)]:
        results[f"Weyl dim V{hw} = {expected_dim}"] = weyl_dimension(hw) == expected_dim

    # Clebsch-Gordan rules
    results["CG: V(1,0)^2 = V(2,0)+V(0,1)"] = verify_clebsch_gordan_V1_squared()
    results["CG: V(0,1)^2 = V(0,2)+V(1,0)"] = verify_clebsch_gordan_V2_squared()
    results["CG: V(1,0)*V(0,1) = V(1,1)+V(0,0)"] = verify_clebsch_gordan_V1_V2()

    # TQ for standard rep
    for a in range(4):
        for b in range(4):
            lam = (a, b)
            results[f"TQ standard lam={lam}"] = verify_baxter_tq_standard(lam)

    # TQ for dual rep
    for a in range(4):
        for b in range(4):
            lam = (a, b)
            results[f"TQ dual lam={lam}"] = verify_baxter_tq_dual(lam)

    # TQ for adjoint
    for lam in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        results[f"TQ adjoint lam={lam}"] = verify_baxter_tq_adjoint(lam)

    # K_0 lattice consistency
    results["K_0 lattice consistency (standard)"] = verify_k0_lattice_consistency(3, 3)

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("SL_3 BAXTER TQ RELATION: K_0 VERIFICATION FOR MC3")
    print("=" * 70)

    results = verify_all()
    n_pass = sum(1 for v in results.values() if v)
    n_fail = sum(1 for v in results.values() if not v)

    for name, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print(f"\n{n_pass} passed, {n_fail} failed out of {len(results)} checks.")
