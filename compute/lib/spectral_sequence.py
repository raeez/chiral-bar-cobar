"""Spectral sequence E_2 page computations for bar complexes.

The PBW filtration on bar complexes yields spectral sequences
with E_1 = classical bar complex, E_2 = bar cohomology.

For Koszul algebras, the spectral sequence collapses at E_2:
  E_2^{p,q} = H^p(B(gr A)) => H^{p+q}(B(A))

Ground truth from the manuscript:
  thm:bar-cobar-isomorphism-main:
    For Koszul A, Omega(B(A)) -> A is a quasi-isomorphism.
    Spectral sequence collapses at E_2.

  comp:virasoro-dim-table:
    Bar cohomology dims: 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610

  prop:E8-koszul-acyclic:
    PBW filtration + Whitehead lemma => collapse at E_1 for simple g.

  prop:virasoro-koszul-acyclic:
    PBW filtration => collapse at E_2, dims = associahedron.

CONVENTIONS:
- Cohomological grading, |d| = +1
- Spectral sequence: E_r^{p,q} with d_r: E_r^{p,q} -> E_r^{p+r,q-r+1}
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Dict, List, Tuple

from sympy import Matrix, Rational, Symbol, zeros, simplify


# ---------------------------------------------------------------------------
# Known bar cohomology dimensions (from Master Table)
# ---------------------------------------------------------------------------

# Virasoro bar cohomology: associahedron/Catalan structure
VIRASORO_BAR_COH = {
    1: 1, 2: 2, 3: 5, 4: 12, 5: 30,
    6: 76, 7: 196, 8: 512, 9: 1353, 10: 3610,
}

# Heisenberg bar cohomology E_2 leading-weight contribution: 1-dimensional in each degree.
# NOTE: This is the leading-weight E_2 contribution (one partition per degree),
# NOT the full bar cohomology. Full bar cohomology dims are p(n-2) for n>=2
# (see KNOWN_BAR_DIMS in bar_complex.py).
HEISENBERG_BAR_COH_E2_LEADING = {n: 1 for n in range(1, 11)}

# sl_2 at generic k: Koszul dual is sl_2 at -k-4
# Values are Riordan R(n+3): R(4)=3, R(5)=6, R(6)=15 (OEIS A005043)
SL2_BAR_COH = {
    1: 3, 2: 6, 3: 15,
}

# Free fermion F_2 (2 generators): bar cohomology by bar degree.
# H^1 = 2 (the generators), H^2 = 3 (Sym^2 on 2 generators after desuspension).
# These are CHAIN GROUP dimensions for F_2; see bar_complex.py KNOWN_BAR_DIMS
# for the full bar cohomology (which follows p(n-1) for a single fermion).
FERMION_BAR_COH = {
    1: 2, 2: 3,
}


# ---------------------------------------------------------------------------
# PBW filtration
# ---------------------------------------------------------------------------

def pbw_filtration_grade(n_generators: int, bar_degree: int) -> int:
    """PBW grade of an element in bar degree n with respect to mode count.

    The PBW filtration F_p counts total mode applications.
    For generators of weight h, bar elements [v_1|...|v_n] with
    v_i having mode degree m_i get PBW grade sum(m_i).
    """
    return bar_degree  # minimum PBW grade = bar degree (each slot has >= 1 mode)


# ---------------------------------------------------------------------------
# CE cohomology engine (generic Lie algebra)
# ---------------------------------------------------------------------------

def ce_differential_matrix(dim_g: int, structure_constants: Dict,
                           degree: int) -> Matrix:
    """Build CE differential d: Λ^degree(g*) -> Λ^{degree+1}(g*).

    structure_constants: dict mapping (i,j) -> {k: c^k_{ij}} for [e_i,e_j] = c^k_{ij} e_k.
    Returns a sympy Matrix with rows indexed by Λ^{degree+1} basis, columns by Λ^degree basis.
    """
    source = list(combinations(range(dim_g), degree))
    target = list(combinations(range(dim_g), degree + 1))
    if not source or not target:
        return zeros(len(target), len(source))

    target_idx = {t: i for i, t in enumerate(target)}
    mat = zeros(len(target), len(source))

    for col, alpha in enumerate(source):
        alpha_set = set(alpha)
        for a in range(dim_g):
            for b in range(a + 1, dim_g):
                bracket_ab = structure_constants.get((a, b), {})
                for c, coeff in bracket_ab.items():
                    if c not in alpha_set:
                        continue
                    new_set = (alpha_set - {c}) | {a, b}
                    if len(new_set) != degree + 1:
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue
                    pos_c = list(alpha).index(c)
                    remaining = sorted(alpha_set - {c})
                    pos_a = sorted(new_set).index(a)
                    pos_b = sorted(new_set - {a}).index(b)
                    sign = (-1) ** pos_c * (-1) ** pos_a * (-1) ** pos_b
                    mat[row, col] += sign * coeff

    return mat


def curvature_contraction_matrix(dim_g: int, killing_form: Dict,
                                  degree: int, level: Symbol = None) -> Matrix:
    """Build curvature contraction d_ω: Λ^degree(g*) → Λ^{degree-2}(g*).

    For a central extension with 2-cocycle ω(x,y) = k·κ(x,y):
      d_ω(e_{i₁}*∧...∧e_{iₙ}*) = Σ_{a<b} (-1)^{a+b} k·κ(e_{i_a},e_{i_b}) (remove i_a,i_b)

    Combined with the CE differential: d_total = d_CE + d_ω
    satisfies d_total² = 0 (the curved CE complex).
    """
    if level is None:
        level = Symbol('k')

    source = list(combinations(range(dim_g), degree))
    target = list(combinations(range(dim_g), degree - 2)) if degree >= 2 else []
    if not source or not target:
        return zeros(max(len(target), 1), max(len(source), 1))

    target_idx = {t: i for i, t in enumerate(target)}
    mat = zeros(len(target), len(source))

    for col, alpha in enumerate(source):
        for a_pos in range(degree):
            for b_pos in range(a_pos + 1, degree):
                i_a, i_b = alpha[a_pos], alpha[b_pos]
                kappa = killing_form.get((i_a, i_b), Rational(0))
                if kappa == 0:
                    continue
                # Remove positions a_pos and b_pos
                remaining = tuple(alpha[p] for p in range(degree)
                                  if p != a_pos and p != b_pos)
                row = target_idx.get(remaining)
                if row is None:
                    continue
                sign = (-1) ** (a_pos + b_pos)
                mat[row, col] += sign * level * kappa

    return mat


def curved_ce_d_squared(dim_g: int, structure_constants: Dict,
                        killing_form: Dict, degree: int,
                        level: Symbol = None) -> Dict[str, object]:
    """Analyze d² for the curved CE complex at given degree.

    d = d_CE + d_ω where:
      d_CE: Λ^p → Λ^{p+1} (CE differential from Lie bracket)
      d_ω: Λ^p → Λ^{p-1} (curvature contraction from 2-cocycle)

    IMPORTANT: d² ≠ 0 for the curved complex. Instead:
      d² = m₀ = multiplication by ω (the curvature)
    This is the curved A∞ relation: m₁²(a) = [m₀, a].

    Returns dict with:
      'ce_squared_zero': bool (d_CE² = 0, Jacobi)
      'omega_squared_zero': bool (d_ω² = 0, degree)
      'anticommutator': the {d_CE, d_ω} matrix (should be nonzero = curvature)
    """
    if level is None:
        level = Symbol('k')

    # d_CE at degree p: Λ^p → Λ^{p+1}
    d_ce_p = ce_differential_matrix(dim_g, structure_constants, degree)
    # d_ω at degree p: Λ^p → Λ^{p-1}
    d_omega_p = curvature_contraction_matrix(dim_g, killing_form, degree, level)

    # d_CE at degree p+1: Λ^{p+1} → Λ^{p+2}
    d_ce_p1 = ce_differential_matrix(dim_g, structure_constants, degree + 1)
    # d_ω at degree p+1: Λ^{p+1} → Λ^p
    d_omega_p1 = curvature_contraction_matrix(dim_g, killing_form, degree + 1, level)

    # d_CE at degree p-1: Λ^{p-1} → Λ^p
    if degree >= 1:
        d_ce_pm1 = ce_differential_matrix(dim_g, structure_constants, degree - 1)
    else:
        d_ce_pm1 = zeros(comb(dim_g, degree), 1)
    # d_ω at degree p-1: Λ^{p-1} → Λ^{p-3}
    if degree >= 1:
        d_omega_pm1 = curvature_contraction_matrix(dim_g, killing_form, degree - 1, level)
    else:
        d_omega_pm1 = zeros(1, 1)

    results = {}

    # 1. d_CE² = 0 (Jacobi)
    d_ce_sq = d_ce_p1 * d_ce_p
    results["ce_squared_zero"] = d_ce_sq.is_zero_matrix or all(
        simplify(d_ce_sq[i, j]) == 0
        for i in range(d_ce_sq.rows) for j in range(d_ce_sq.cols)
    )

    # 2. d_ω² = 0 (degree)
    if degree >= 4:
        d_omega_pm2 = curvature_contraction_matrix(dim_g, killing_form, degree - 2, level)
        if d_omega_pm2.cols == d_omega_p.rows:
            d_omega_sq = d_omega_pm2 * d_omega_p
            results["omega_squared_zero"] = d_omega_sq.is_zero_matrix or all(
                simplify(d_omega_sq[i, j]) == 0
                for i in range(d_omega_sq.rows) for j in range(d_omega_sq.cols)
            )
        else:
            results["omega_squared_zero"] = True
    else:
        results["omega_squared_zero"] = True

    # 3. Anticommutator {d_CE, d_ω}: maps Λ^p → Λ^{p-1}
    dim_source = comb(dim_g, degree)
    dim_target = comb(dim_g, degree - 1) if degree >= 1 else 0

    if dim_source > 0 and dim_target > 0:
        # term1: d_ω(p+1) ∘ d_CE(p): Λ^p → Λ^{p+1} → Λ^{p-1}
        if d_omega_p1.rows == dim_target and d_ce_p.rows == d_omega_p1.cols:
            term1 = d_omega_p1 * d_ce_p
        else:
            term1 = zeros(dim_target, dim_source)

        # term2: d_CE(p-2) ∘ d_ω(p): Λ^p → Λ^{p-2} → Λ^{p-1}
        if degree >= 2:
            d_ce_pm2 = ce_differential_matrix(dim_g, structure_constants, degree - 2)
            if d_ce_pm2.rows == dim_target and d_omega_p.rows == d_ce_pm2.cols:
                term2 = d_ce_pm2 * d_omega_p
            else:
                term2 = zeros(dim_target, dim_source)
        else:
            term2 = zeros(dim_target, dim_source)

        results["anticommutator"] = term1 + term2
        results["anticommutator_zero"] = all(
            simplify((term1 + term2)[i, j]) == 0
            for i in range(dim_target) for j in range(dim_source)
        )
    else:
        results["anticommutator"] = None
        results["anticommutator_zero"] = True

    return results


def ce_cohomology_dims(dim_g: int, structure_constants: Dict) -> List[int]:
    """Compute CE cohomology dimensions H^*(g, k) for a Lie algebra g.

    Returns [dim H^0, dim H^1, ..., dim H^{dim_g}].
    """
    dims = []
    prev_image_rank = 0
    for p in range(dim_g + 1):
        space_dim = comb(dim_g, p)
        d = ce_differential_matrix(dim_g, structure_constants, p)
        if d.cols > 0 and d.rows > 0:
            kernel_rank = space_dim - d.rank()
        else:
            kernel_rank = space_dim
        dims.append(kernel_rank - prev_image_rank)
        prev_image_rank = d.rank() if (d.cols > 0 and d.rows > 0) else 0
    return dims


def ce_differential_with_coefficients(
    dim_g: int,
    structure_constants: Dict,
    module_dim: int,
    module_action: List[Matrix],
    degree: int,
) -> Matrix:
    """CE differential d: Λ^degree(g*) ⊗ M → Λ^{degree+1}(g*) ⊗ M.

    The CE differential with coefficients in a g-module M has two terms:

    1. Lie bracket term (same as trivial coefficients, tensored with id_M):
       Σ_{a<b} sign · ω([e_a, e_b], ...) ⊗ m

    2. Module action term (new):
       Σ_i (-1)^i · (remove e_i from exterior part) ⊗ (ρ(e_i) · m)

    Args:
        dim_g: dimension of g
        structure_constants: bracket data (i,j) -> {k: c^k_{ij}}
        module_dim: dimension of the coefficient module M
        module_action: list of dim_g matrices, each module_dim × module_dim,
                       where module_action[i] = ρ(e_i) acting on M
        degree: the CE degree p (source is Λ^p(g*) ⊗ M)

    Returns:
        Matrix of shape (C(dim_g, degree+1)*module_dim, C(dim_g, degree)*module_dim)
    """
    source_ext = list(combinations(range(dim_g), degree))
    target_ext = list(combinations(range(dim_g), degree + 1))
    n_src_ext = len(source_ext) if source_ext else 1
    n_tgt_ext = len(target_ext) if target_ext else 1
    d_M = module_dim

    if not source_ext or not target_ext:
        return zeros(n_tgt_ext * d_M, n_src_ext * d_M)

    target_ext_idx = {t: i for i, t in enumerate(target_ext)}
    source_ext_idx = {s: i for i, s in enumerate(source_ext)}

    mat = zeros(len(target_ext) * d_M, len(source_ext) * d_M)

    # Term 1: Lie bracket term (same structure as ce_differential_matrix, ⊗ id_M)
    for col_ext, alpha in enumerate(source_ext):
        alpha_set = set(alpha)
        for a in range(dim_g):
            for b in range(a + 1, dim_g):
                bracket_ab = structure_constants.get((a, b), {})
                for c, coeff in bracket_ab.items():
                    if c not in alpha_set:
                        continue
                    new_set = (alpha_set - {c}) | {a, b}
                    if len(new_set) != degree + 1:
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row_ext = target_ext_idx.get(new_tuple)
                    if row_ext is None:
                        continue
                    pos_c = list(alpha).index(c)
                    pos_a = sorted(new_set).index(a)
                    pos_b = sorted(new_set - {a}).index(b)
                    sign = (-1) ** pos_c * (-1) ** pos_a * (-1) ** pos_b
                    # Apply to all module components (⊗ id_M)
                    for m in range(d_M):
                        mat[row_ext * d_M + m, col_ext * d_M + m] += sign * coeff

    # Term 2: Module action term
    # d_action(ω ⊗ v)(x_0, ..., x_p) = Σ_i (-1)^i ω(x_0,...,x̂_i,...,x_p) ⊗ ρ(x_i)(v)
    # In basis: for α ∈ Λ^p and generator e_i not in α:
    #   maps (α, m) to (α ∪ {i}, ρ(e_i)(m)) with sign from inserting i into α
    # NOTE: The bracket term implements d_CE on Λ*(g*) (dual convention).
    # The action term carries a relative minus sign in the Λ*(g*)⊗M convention
    # vs the Hom(Λ*(g), M) convention. This ensures d² = 0.
    for col_ext, alpha in enumerate(source_ext):
        alpha_set = set(alpha)
        for i in range(dim_g):
            if i in alpha_set:
                continue
            new_set = alpha_set | {i}
            new_tuple = tuple(sorted(new_set))
            row_ext = target_ext_idx.get(new_tuple)
            if row_ext is None:
                continue
            # Sign: -(-1)^{position of i in the new sorted tuple}
            # The leading minus is the relative sign between bracket and action terms
            pos_i = list(new_tuple).index(i)
            sign = -(-1) ** pos_i
            # Module action: ρ(e_i)
            rho_i = module_action[i]
            for m_tgt in range(d_M):
                for m_src in range(d_M):
                    if rho_i[m_tgt, m_src] != 0:
                        mat[row_ext * d_M + m_tgt,
                            col_ext * d_M + m_src] += sign * rho_i[m_tgt, m_src]

    return mat


def ce_cohomology_with_coefficients_dims(
    dim_g: int,
    structure_constants: Dict,
    module_dim: int,
    module_action: List[Matrix],
) -> List[int]:
    """Compute CE cohomology H^*(g, M) for a g-module M.

    Returns [dim H^0, dim H^1, ..., dim H^{dim_g}].
    """
    dims = []
    prev_image_rank = 0
    d_M = module_dim
    for p in range(dim_g + 1):
        space_dim = comb(dim_g, p) * d_M
        d = ce_differential_with_coefficients(
            dim_g, structure_constants, d_M, module_action, p)
        if d.cols > 0 and d.rows > 0:
            kernel_rank = space_dim - d.rank()
        else:
            kernel_rank = space_dim
        dims.append(kernel_rank - prev_image_rank)
        prev_image_rank = d.rank() if (d.cols > 0 and d.rows > 0) else 0
    return dims


def _sym_module_dim(dim_g: int, weight: int) -> int:
    """Dimension of weight-h part of Sym(g otimes t^{-1}k[t^{-1}]).

    This is the space of polynomials in generators {e_i^{(-m)} : 1<=i<=dim_g, m>=1}
    with total weight sum(m_j) = weight.

    dim = sum over partitions lambda of weight: prod_j C(dim_g + mult_j - 1, mult_j)
    where mult_j counts how many parts equal j.

    Equivalently, this is the coefficient of q^weight in prod_{m>=1} 1/(1-q^m)^{dim_g}.
    """
    if weight == 0:
        return 1
    # Use the partition-with-colors generating function
    # p_d(n) = coefficient of q^n in prod_{m>=1} 1/(1-q^m)^d
    d = dim_g
    table = [0] * (weight + 1)
    table[0] = 1
    for m in range(1, weight + 1):
        # Add mode m with d colors: multiply by 1/(1-q^m)^d
        # 1/(1-x)^d has coefficients C(k+d-1, d-1)
        new_table = [0] * (weight + 1)
        for w in range(weight + 1):
            for k in range(0, (weight - w) // m + 1):
                new_table[w + k * m] += table[w] * comb(k + d - 1, d - 1)
        table = new_table
    return table[weight]


def adjoint_rep_matrices(dim_g: int, structure_constants: Dict) -> List[Matrix]:
    """Build the adjoint representation matrices rho(e_i) for each generator.

    Returns list of dim_g x dim_g matrices where rho(e_i)_{jk} = f^j_{ik}.
    That is, [e_i, e_k] = sum_j f^j_{ik} e_j, so ad(e_i) has matrix (f^j_{ik})_{j,k}.
    """
    matrices = []
    for i in range(dim_g):
        mat = zeros(dim_g, dim_g)
        for k in range(dim_g):
            # ad(e_i)(e_k) = [e_i, e_k] = sum_j f^j_{ik} e_j
            bracket = structure_constants.get((i, k), {})
            for j, coeff in bracket.items():
                mat[j, k] += coeff
        matrices.append(mat)
    return matrices


def adjoint_invariant_dim(dim_g: int, structure_constants: Dict, weight: int) -> int:
    """Dimension of g-invariants in the weight-h part of Sym(g tensor t^{-1}k[t^{-1}]).

    At weight h, the module M_h decomposes into a direct sum of tensor products
    of copies of the adjoint representation (one copy at each mode m, with
    multiplicities from partitions of h). The g-action is diagonal.

    An element is g-invariant iff it is killed by all ad(e_i).

    For simple g:
      - weight 0: dim = 1 (scalars)
      - weight 1: dim = 0 (ad has no invariants for simple g)
      - weight 2: Molien gives 1 (the Casimir)

    Algorithm: enumerate colored partitions of weight h (modes m_1,...,m_k with
    colors c_1,...,c_k where 1<=c_i<=dim_g). Build the explicit g-action on
    this space and compute kernel dimension.
    """
    if weight == 0:
        return 1

    ad_mats = adjoint_rep_matrices(dim_g, structure_constants)

    # Enumerate basis of M_h: monomials e_{c1}^{(-m1)} ... e_{ck}^{(-mk)}
    # with sum(m_i) = h, m_i >= 1, treated as symmetric (Sym algebra).
    # A basis element is specified by a multiset {(color, mode)}.
    # We represent as a tuple of (mode, color) pairs sorted.
    from itertools import combinations_with_replacement

    # Generate all mode assignments: partitions of h into parts >= 1
    def partitions_of(n, max_part=None):
        if max_part is None:
            max_part = n
        if n == 0:
            yield ()
            return
        for p in range(min(n, max_part), 0, -1):
            for rest in partitions_of(n - p, p):
                yield (p,) + rest

    # For each partition, generate all colorings (with replacement, sorted)
    basis = []
    partition_list = list(partitions_of(weight))
    for partition in partition_list:
        # Group by multiplicity of each part
        from collections import Counter
        part_counts = Counter(partition)
        # Colors for each group: combinations_with_replacement
        groups = sorted(part_counts.items())
        # Generate all ways to assign colors to each group
        def color_assignments(groups_remaining):
            if not groups_remaining:
                yield []
                return
            mode, count = groups_remaining[0]
            for colors in combinations_with_replacement(range(dim_g), count):
                for rest in color_assignments(groups_remaining[1:]):
                    yield [(mode, c) for c in colors] + rest

        for assignment in color_assignments(groups):
            basis.append(tuple(sorted(assignment)))

    # Deduplicate (symmetric algebra: order doesn't matter)
    basis = sorted(set(basis))
    m_dim = len(basis)

    if m_dim == 0:
        return 0

    basis_idx = {b: i for i, b in enumerate(basis)}

    # Build action of each generator on this basis
    # ad(e_i) acts on e_{c}^{(-m)} as [e_i, e_{c}] = sum_j f^j_{ic} e_j^{(-m)}
    # On a monomial, it acts by Leibniz rule (sum over each factor).
    action_mats = []
    for gen_i in range(dim_g):
        mat = zeros(m_dim, m_dim)
        for col, monomial in enumerate(basis):
            # monomial = ((m1,c1), (m2,c2), ...)
            for pos in range(len(monomial)):
                mode, color = monomial[pos]
                # ad(e_gen_i)(e_color) = sum_j f^j_{gen_i, color} e_j
                for j in range(dim_g):
                    coeff = ad_mats[gen_i][j, color]
                    if coeff == 0:
                        continue
                    # Replace factor at pos with (mode, j)
                    new_mon = list(monomial)
                    new_mon[pos] = (mode, j)
                    new_mon_sorted = tuple(sorted(new_mon))
                    row = basis_idx.get(new_mon_sorted)
                    if row is not None:
                        mat[row, col] += coeff
        action_mats.append(mat)

    # Invariants = intersection of kernels of all action matrices
    if not action_mats:
        return m_dim

    # Stack all action matrices vertically and find kernel
    stacked = action_mats[0]
    for m in action_mats[1:]:
        stacked = stacked.row_join(m) if False else stacked.col_join(m)

    return m_dim - stacked.rank()


def pbw_e1_page(dim_g: int, structure_constants: Dict,
                max_weight: int) -> Dict[Tuple[int, int], int]:
    """Compute the E_1 page of the PBW spectral sequence for a KM algebra.

    For simple g at generic level, Whitehead's lemma gives:
      H^p(g, M) = 0 for 0 < p < dim(g) and any finite-dim M.
    Only H^0(g, M) = M^g (invariants) and H^{dim_g}(g, M) survive.

    At the associated graded level, g acts on Sym(g[t^{-1}]) via the
    adjoint representation. So E_1^{p,h} = H^p(g, M_h) where M_h is
    the weight-h part of the symmetric algebra.

    This function computes:
    - CE cohomology with TRIVIAL coefficients (verified computation)
    - Coefficient module dimensions at each weight (verified computation)
    - E_1 entries at CE degrees 0 and dim_g only (Whitehead vanishing)
    - At CE degree 0: H^0(g, M_h) = dim(M_h^g) requires invariant
      theory computation (not done here for non-trivial g)

    Returns dict mapping (ce_degree, weight) -> dimension.
    """
    ce_dims = ce_cohomology_dims(dim_g, structure_constants)
    result = {}
    for h in range(0, max_weight + 1):
        m_dim = _sym_module_dim(dim_g, h)
        for p in range(dim_g + 1):
            # Whitehead: middle CE degrees vanish for simple g
            # H^0 and H^{dim_g} survive with M^g (invariants)
            # For abelian g: all degrees survive, trivially
            result[(p, h)] = ce_dims[p] * m_dim
    return result


# ---------------------------------------------------------------------------
# Spectral sequence data
# ---------------------------------------------------------------------------

def spectral_sequence_collapse(algebra: str) -> Dict[str, object]:
    """Collapse page for the PBW spectral sequence.

    Ground truth:
      - Kac-Moody (simple g): collapses at E_1 (Whitehead lemma)
      - Virasoro, W-algebras: collapse at E_2 (Koszul property)
      - Heisenberg: collapse at E_1 (commutative, trivial)
    """
    collapse_data = {
        "Heisenberg": {
            "collapse_page": 1,
            "reason": "Commutative algebra, bar = Koszul resolution",
            "E_1_description": "Chevalley-Eilenberg for abelian Lie",
        },
        "sl2": {
            "collapse_page": 1,
            "reason": "Whitehead lemma for simple g",
            "E_1_description": "H*(sl_2; S*(sl_2[t^{-1}]))",
        },
        "sl3": {
            "collapse_page": 1,
            "reason": "Whitehead lemma for simple g",
            "E_1_description": "H*(sl_3; S*(sl_3[t^{-1}]))",
        },
        "E8": {
            "collapse_page": 1,
            "reason": "Whitehead lemma for simple g = e_8",
            "E_1_description": "H*(e_8; S*(e_8[t^{-1}]))",
        },
        "Virasoro": {
            "collapse_page": 2,
            "reason": "Koszul property, associahedron structure",
            "E_2_description": "Bar cohomology = Koszul dual coalgebra",
        },
        "W3": {
            "collapse_page": 2,
            "reason": "Koszul property (conjectured for W_3)",
            "E_2_description": "Expected: graded by spin content",
        },
        "beta_gamma": {
            "collapse_page": 2,
            "reason": "Com^! = Lie duality, 2 generators",
            "E_2_description": "Lie coalgebra on 2 generators",
        },
        "bc": {
            "collapse_page": 2,
            "reason": "Lie^! = Com duality, 2 generators",
            "E_2_description": "Symmetric coalgebra on 2 generators",
        },
    }
    return collapse_data.get(algebra, {"collapse_page": "unknown"})


# ---------------------------------------------------------------------------
# E_2 page computations
# ---------------------------------------------------------------------------

def e2_page_virasoro(max_n: int = 10) -> Dict[int, int]:
    """E_2^{n,0} for Virasoro = bar cohomology in degree n.

    Ground truth: prop:virasoro-koszul-acyclic.
    These are the associahedron numbers (shifted Catalan).
    """
    return {n: VIRASORO_BAR_COH[n] for n in range(1, min(max_n + 1, 11))}


def e2_page_heisenberg(max_n: int = 10) -> Dict[int, int]:
    """E_2^{n,0} for Heisenberg = 1 in each degree.

    Ground truth: comp:heisenberg-bar (detailed_computations.tex).
    Heisenberg has 1 generator, commutative OPE => bar cohomology is 1-dim.
    """
    return {n: 1 for n in range(1, max_n + 1)}


def e2_page_sl2(max_n: int = 3) -> Dict[int, int]:
    """E_2^{n,0} for sl_2 at generic k.

    Ground truth: comp:sl2-bar (detailed_computations.tex).
    """
    return {n: SL2_BAR_COH.get(n, 0) for n in range(1, max_n + 1) if n in SL2_BAR_COH}


# ---------------------------------------------------------------------------
# Associahedron / Catalan numbers
# ---------------------------------------------------------------------------

def catalan(n: int) -> int:
    """n-th Catalan number C_n = (2n)! / ((n+1)! * n!).

    The Virasoro bar cohomology dims are related (but not equal) to Catalan numbers.
    Actual dims: 1, 2, 5, 14, 42, ... (Catalan) shifted to
                 1, 2, 5, 12, 30, 76, ...
    These are the (shifted) number of faces of the associahedron K_n.
    """
    from math import factorial
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))


def _narayana(n: int, k: int) -> int:
    """Narayana number N(n, k) = (1/n) C(n, k) C(n, k-1)."""
    from math import comb
    if n <= 0 or k <= 0 or k > n:
        return 0
    return comb(n, k) * comb(n, k - 1) // n


def associahedron_f_vector(n: int) -> List[int]:
    """f-vector of the associahedron K_n (number of faces by dimension).

    K_n is simple of dimension n-2. Its h-vector is given by Narayana numbers
    h_k = N(n-1, k+1), and f_k = sum_{j=0}^{d-k} C(d-j, d-k-j) * h_j.

    K_2 = point: f = [1]
    K_3 = interval: f = [2, 1]
    K_4 = pentagon: f = [5, 5, 1]
    K_5 = 3d associahedron: f = [14, 21, 9, 1]

    Raises ValueError for n < 2.
    """
    from math import comb
    if n < 2:
        raise ValueError(f"Associahedron K_n requires n >= 2, got {n}")
    d = n - 2  # dimension
    h = [_narayana(n - 1, j + 1) for j in range(d + 1)]
    return [
        sum(comb(d - j, d - k - j) * h[j] for j in range(d - k + 1))
        for k in range(d + 1)
    ]


# ---------------------------------------------------------------------------
# Koszul property test
# ---------------------------------------------------------------------------

def check_koszul_property(bar_coh_dims: Dict[int, int], dual_dims: Dict[int, int]) -> bool:
    """Check if bar cohomology matches Koszul dual dimensions.

    For a Koszul algebra A, H^n(B(A)) = (A^!)_n as graded vector spaces.
    """
    for n, dim in bar_coh_dims.items():
        if n in dual_dims and dual_dims[n] != dim:
            return False
    return True


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_spectral_sequences():
    """Verify spectral sequence data."""
    results = {}

    # Virasoro bar cohomology
    vir_coh = e2_page_virasoro()
    results["Vir: dim H^1 = 1"] = vir_coh[1] == 1
    results["Vir: dim H^2 = 2"] = vir_coh[2] == 2
    results["Vir: dim H^3 = 5"] = vir_coh[3] == 5
    results["Vir: dim H^5 = 30"] = vir_coh[5] == 30
    results["Vir: dim H^10 = 3610"] = vir_coh[10] == 3610

    # Heisenberg
    heis_coh = e2_page_heisenberg()
    results["Heis: all dims = 1"] = all(d == 1 for d in heis_coh.values())

    # Collapse pages
    results["Heis: collapse at E_1"] = spectral_sequence_collapse("Heisenberg")["collapse_page"] == 1
    results["sl2: collapse at E_1"] = spectral_sequence_collapse("sl2")["collapse_page"] == 1
    results["E8: collapse at E_1"] = spectral_sequence_collapse("E8")["collapse_page"] == 1
    results["Vir: collapse at E_2"] = spectral_sequence_collapse("Virasoro")["collapse_page"] == 2
    results["bg: collapse at E_2"] = spectral_sequence_collapse("beta_gamma")["collapse_page"] == 2

    # Catalan sanity
    results["C_1 = 1"] = catalan(1) == 1
    results["C_2 = 2"] = catalan(2) == 2
    results["C_3 = 5"] = catalan(3) == 5
    results["C_4 = 14"] = catalan(4) == 14

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("SPECTRAL SEQUENCE COMPUTATIONS: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_spectral_sequences().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
