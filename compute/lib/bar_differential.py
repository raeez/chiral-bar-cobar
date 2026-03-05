"""Chiral bar differential: exact numerical computation.

Computes the bar cohomology of KM algebras at level 0 (uncurved)
by building the bar differential as an explicit matrix.

The bar complex B-bar^n = g^{⊗n} ⊗ OS^{n-1}(C_n) with differential
d: B-bar^n -> B-bar^{n-1} that contracts pairs via the Lie bracket
and restricts OS forms via Poincaré residue.

Convention: d(a_1⊗...⊗a_n ⊗ ω) = Σ_{i<j} ±[a_i,a_j]⊗(others)⊗∂_{ij}(ω)
where ∂_{ij}: OS^{n-1}(C_n) → OS^{n-2}(C_{n-1}) is the Poincaré residue
along the diagonal D_{ij}.

Key insight: the OPE pole combined with the OS form η_{ij} = dε/ε produces
a double pole dε/ε², whose residue is 0. So d₂ = 0 for KM algebras.
Only d_{n≥3} can be nonzero (via Poincaré residue on OS forms of degree ≥ 2).
"""

import numpy as np
from itertools import product as iter_product
from typing import Dict, List, Tuple, Optional


# ---------------------------------------------------------------------------
# Lie algebra structure constants
# ---------------------------------------------------------------------------

def sl2_structure_constants() -> Tuple[List[str], np.ndarray]:
    """sl₂ = {e, h, f} with [h,e]=2e, [h,f]=-2f, [e,f]=h."""
    names = ['e', 'h', 'f']
    d = 3
    f = np.zeros((d, d, d))
    # [e, f] = h  → f[0,2,1] = 1
    f[0, 2, 1] = 1
    f[2, 0, 1] = -1
    # [h, e] = 2e → f[1,0,0] = 2
    f[1, 0, 0] = 2
    f[0, 1, 0] = -2
    # [h, f] = -2f → f[1,2,2] = -2
    f[1, 2, 2] = -2
    f[2, 1, 2] = 2
    return names, f


def sl3_structure_constants() -> Tuple[List[str], np.ndarray]:
    """sl₃ = {e1, e2, e12, h1, h2, f1, f2, f12} with standard conventions.

    Cartan matrix: A = [[2,-1],[-1,2]].
    e12 = [e1, e2], f12 = [f2, f1] = -[f1, f2].
    """
    names = ['e1', 'e2', 'e12', 'h1', 'h2', 'f1', 'f2', 'f12']
    d = 8
    f = np.zeros((d, d, d))

    # Index mapping: e1=0, e2=1, e12=2, h1=3, h2=4, f1=5, f2=6, f12=7
    e1, e2, e12, h1, h2, f1, f2, f12 = range(8)

    def set_bracket(a, b, c, val):
        f[a, b, c] += val
        f[b, a, c] -= val

    # [h1, e1] = 2*e1
    set_bracket(h1, e1, e1, 2)
    # [h1, e2] = -e2
    set_bracket(h1, e2, e2, -1)
    # [h1, e12] = e12  (since e12 has root α1+α2, and <α1+α2, α1^vee> = 2-1=1)
    set_bracket(h1, e12, e12, 1)
    # [h2, e1] = -e1
    set_bracket(h2, e1, e1, -1)
    # [h2, e2] = 2*e2
    set_bracket(h2, e2, e2, 2)
    # [h2, e12] = e12  (since <α1+α2, α2^vee> = -1+2=1)
    set_bracket(h2, e12, e12, 1)

    # [h1, f1] = -2*f1
    set_bracket(h1, f1, f1, -2)
    # [h1, f2] = f2
    set_bracket(h1, f2, f2, 1)
    # [h1, f12] = -f12
    set_bracket(h1, f12, f12, -1)
    # [h2, f1] = f1
    set_bracket(h2, f1, f1, 1)
    # [h2, f2] = -2*f2
    set_bracket(h2, f2, f2, -2)
    # [h2, f12] = -f12
    set_bracket(h2, f12, f12, -1)

    # [h1, h2] = 0 (Cartan commutes)

    # [e1, e2] = e12
    set_bracket(e1, e2, e12, 1)
    # [e1, e12] = 0 (since α1 + (α1+α2) is not a root)
    # [e2, e12] = 0 (same reason)

    # [f1, f2] = -f12  (so f12 = [f2, f1])
    set_bracket(f1, f2, f12, -1)
    # [f1, f12] = 0
    # [f2, f12] = 0

    # [e1, f1] = h1
    set_bracket(e1, f1, h1, 1)
    # [e2, f2] = h2
    set_bracket(e2, f2, h2, 1)
    # [e12, f12] = h1 + h2
    set_bracket(e12, f12, h1, 1)
    set_bracket(e12, f12, h2, 1)

    # [e1, f2] = 0 (different simple roots)
    # [e2, f1] = 0

    # [e1, f12] = -f2  (lowering: [e1, [f2,f1]] = [[e1,f2],f1]+[f2,[e1,f1]] = 0+[f2,h1] = f2... sign?)
    # Actually: [e1, f12] where f12 = [f2,f1].
    # [e1, [f2,f1]] = [[e1,f2],f1] + [f2,[e1,f1]] = 0 + [f2, h1] = -f2 (since [h1,f2]=f2 → [f2,h1]=-f2)
    # Wait: [h1,f2] = f2, so [f2,h1] = -f2.
    # So [e1, f12] = -f2.
    set_bracket(e1, f12, f2, -1)

    # [e2, f12] = f1
    # [e2, [f2,f1]] = [[e2,f2],f1] + [f2,[e2,f1]] = [h2,f1] + 0 = f1 (since [h2,f1]=f1)
    set_bracket(e2, f12, f1, 1)

    # [e12, f1] = -e2
    # [[e1,e2], f1] = [[e1,f1],e2] + [e1,[e2,f1]] = [h1,e2] + 0 = -e2
    set_bracket(e12, f1, e2, -1)

    # [e12, f2] = e1
    # [[e1,e2], f2] = [[e1,f2],e2] + [e1,[e2,f2]] = 0 + [e1,h2] = -[h2,e1] = e1
    set_bracket(e12, f2, e1, 1)

    return names, f


def verify_jacobi(names: List[str], f: np.ndarray) -> bool:
    """Verify Jacobi identity: [[a,b],c] + [[b,c],a] + [[c,a],b] = 0."""
    d = len(names)
    max_err = 0.0
    for a in range(d):
        for b in range(d):
            for c in range(d):
                # [[a,b],c]
                val = 0.0
                for k in range(d):
                    val += f[a, b, k] * f[k, c, :]  # not right
                # Do it properly
                pass
    # Simpler: compute [f[a,b,:], c] and sum cyclically
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for e in range(d):
                    total = 0.0
                    for k in range(d):
                        total += f[a, b, k] * f[k, c, e]  # [[a,b],c]_e
                        total += f[b, c, k] * f[k, a, e]  # [[b,c],a]_e
                        total += f[c, a, k] * f[k, b, e]  # [[c,a],b]_e
                    max_err = max(max_err, abs(total))
    return max_err < 1e-10


# ---------------------------------------------------------------------------
# Orlik-Solomon algebra
# ---------------------------------------------------------------------------

def os_basis(n: int, degree: int) -> List[Tuple[Tuple[int, int], ...]]:
    """Basis for OS^degree(C_n) using the broken circuit construction.

    We use the lex-first broken circuit basis: monomials η_{i1,j1}∧...∧η_{ik,jk}
    where (i1,j1) < ... < (ik,jk) in lex order, and the monomial contains
    no broken circuit.

    A circuit in the complete graph K_n is a cycle. The "broken circuit"
    (with respect to lex ordering) is obtained by removing the lex-largest edge.
    The NBC (no-broken-circuit) basis consists of monomials that avoid all
    broken circuits.

    For degree = n-1 (top degree): the NBC basis consists of spanning trees
    of the "star" form: all edges (1,j) for j=2,...,n give one monomial,
    and others from the NBC construction.

    Returns list of monomials, each a tuple of (i,j) pairs with i < j.
    """
    if degree == 0:
        return [()]  # empty monomial = constant 1

    # Generate all edges of K_n
    edges = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

    # Find broken circuits: for each 3-cycle (i,j,k) with i<j<k,
    # the circuit is {(i,j), (j,k), (i,k)}. The lex-largest edge is (j,k).
    # Broken circuit = {(i,j), (i,k)} (remove largest = (j,k)).
    # Actually: broken circuit = circuit minus lex-largest edge.
    # Circuit = {(i,j), (j,k), (i,k)}, lex order: (i,j) < (i,k) < (j,k).
    # Broken circuit = {(i,j), (i,k)}.

    broken_circuits = set()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                # Circuit: (i,j), (i,k), (j,k). Lex largest = (j,k).
                # Broken circuit = {(i,j), (i,k)}.
                broken_circuits.add(frozenset({(i, j), (i, k)}))

    # Generate all degree-k monomials from edges, lex ordered
    from itertools import combinations
    basis = []
    for mono in combinations(edges, degree):
        # Check if monomial contains any broken circuit
        mono_set = set(mono)
        contains_bc = False
        for bc in broken_circuits:
            if bc.issubset(mono_set):
                contains_bc = True
                break
        if not contains_bc:
            basis.append(mono)

    return basis


def os_top_basis(n: int) -> List[Tuple[Tuple[int, int], ...]]:
    """Basis for top-degree OS^{n-1}(C_n).

    For the top degree, we use a different construction:
    basis elements correspond to labeled rooted forests on [n] with n-1 edges,
    i.e., spanning trees of K_n.

    But the NBC basis is simpler: for top degree, it's the set of
    (n-1)-subsets of edges that form spanning trees and contain no
    broken circuit.

    Actually, for the OS algebra the top degree n-1 has dim (n-1)!.
    The NBC basis at top degree is: for each permutation σ of {2,...,n},
    the monomial η_{σ(2),σ(3)} ∧ η_{σ(3),σ(4)} ∧ ... is NOT the right form.

    Let me use a simpler basis: the "star basis" centered at vertex 1.
    """
    return os_basis(n, n - 1)


def poincare_residue_matrix(n: int, i: int, j: int) -> np.ndarray:
    """Compute the Poincaré residue map ∂_{ij}: OS^{n-1}(C_n) → OS^{n-2}(C_{n-1}).

    The Poincaré residue along D_{ij} = {z_i = z_j}:
    1. Decompose ω = η_{ij} ∧ α + β (where β has no η_{ij} in free exterior algebra)
    2. Res_{D_{ij}}(ω) = α|_{D_{ij}} (restrict to z_i = z_j, relabel)

    IMPORTANT: This uses the FREE exterior algebra, not the OS quotient.
    The Arnold relation is a pointwise identity of forms, so working in the
    free exterior algebra and then projecting to OS gives consistent results.

    Returns matrix M where M[target_idx, source_idx] gives the coefficient.
    """
    source_basis = os_top_basis(n)
    target_basis = os_top_basis(n - 1)

    if not source_basis or not target_basis:
        return np.zeros((len(target_basis) if target_basis else 0,
                         len(source_basis) if source_basis else 0))

    # Relabeling: when merging z_i and z_j (i < j), keep i, remove j.
    # Points {1,...,n} → {1,...,n}\{j}, relabeled to {1,...,n-1}.
    # Relabel map: k → k if k < j, k → k-1 if k > j. Merged point stays at i.
    def relabel(edge, merge_i, merge_j):
        """Relabel an edge (a,b) after merging merge_i and merge_j (i < j)."""
        a, b = edge
        # Replace merge_j with merge_i
        if a == merge_j:
            a = merge_i
        if b == merge_j:
            b = merge_i
        # Relabel: remove index merge_j
        if a > merge_j:
            a -= 1
        if b > merge_j:
            b -= 1
        # Normalize: ensure a < b
        if a > b:
            a, b = b, a
        if a == b:
            return None  # self-edge, shouldn't happen in valid forms
        return (a, b)

    M = np.zeros((len(target_basis), len(source_basis)))
    edge_ij = (min(i, j), max(i, j))

    for s_idx, mono in enumerate(source_basis):
        # Check if η_{ij} appears in this monomial
        if edge_ij not in mono:
            # No η_{ij} factor → Poincaré residue is 0
            continue

        # Find position of η_{ij} in the monomial
        pos = mono.index(edge_ij)

        # Sign from moving η_{ij} to front: (-1)^pos
        sign = (-1) ** pos

        # Remaining edges after removing η_{ij}
        remaining = list(mono[:pos]) + list(mono[pos + 1:])

        # Relabel remaining edges (merge i,j)
        relabeled = []
        valid = True
        for edge in remaining:
            new_edge = relabel(edge, min(i, j), max(i, j))
            if new_edge is None:
                valid = False
                break
            relabeled.append(new_edge)

        if not valid:
            continue

        # Sort the relabeled edges (to match target basis ordering)
        # and track the sign from the reordering
        relabeled_tuple = tuple(sorted(relabeled))

        # Count transpositions needed to sort
        perm_sign = 1
        temp = list(relabeled)
        for idx_a in range(len(temp)):
            for idx_b in range(idx_a + 1, len(temp)):
                if temp[idx_a] > temp[idx_b]:
                    temp[idx_a], temp[idx_b] = temp[idx_b], temp[idx_a]
                    perm_sign *= -1

        # Find target index
        if relabeled_tuple in target_basis:
            t_idx = target_basis.index(relabeled_tuple)
            M[t_idx, s_idx] = sign * perm_sign
        else:
            # Need to express in terms of target basis using Arnold relations
            # For now, try to find it by NBC reduction
            coeff = _express_in_nbc_basis(relabeled_tuple, n - 1, len(remaining), target_basis)
            for t_idx, c in coeff.items():
                M[t_idx, s_idx] += sign * perm_sign * c

    return M


def _express_in_nbc_basis(mono_tuple, n, degree, basis):
    """Express a monomial in terms of the NBC basis using Arnold relations.

    Returns dict {basis_index: coefficient}.
    """
    if mono_tuple in basis:
        return {basis.index(mono_tuple): 1.0}

    # Check for Arnold relation: find a broken circuit subset
    # and use the Arnold relation to rewrite.
    mono_set = set(mono_tuple)
    mono_list = list(mono_tuple)

    # Find broken circuits in the monomial
    for idx_a in range(len(mono_list)):
        for idx_b in range(idx_a + 1, len(mono_list)):
            ea = mono_list[idx_a]
            eb = mono_list[idx_b]
            # Check if {ea, eb} is a broken circuit
            # A broken circuit comes from a 3-cycle: for i < j < k,
            # the broken circuit is {(i,j), (i,k)} (removing lex-largest (j,k))
            # So: ea = (i,j), eb = (i,k) with j < k → missing edge is (j,k)
            ia, ja = ea
            ib, jb = eb
            if ia == ib:  # same first vertex
                # Broken circuit from triangle (ia, ja, jb) if ja < jb
                # or (ia, jb, ja) if jb < ja
                if ja != jb:
                    i_val = ia
                    j_val = min(ja, jb)
                    k_val = max(ja, jb)
                    # Broken circuit = {(i,j), (i,k)}, missing = (j,k)
                    # Arnold: η_{ij}∧η_{ik} = η_{ij}∧η_{jk} + η_{jk}∧η_{ik}
                    # Wait, let me use the specific Arnold relation.
                    # Actually the Arnold relation for the OS algebra says:
                    # η_{ij}∧η_{jk} + η_{jk}∧η_{ki} + η_{ki}∧η_{ij} = 0
                    # For the standard form:
                    # η_{ab}∧η_{bc} = η_{ab}∧η_{ac} + η_{ac}∧η_{bc}
                    # (This is the manuscript's convention, line 581)

                    # We have {(i,j), (i,k)} = {(i_val,j_val), (i_val,k_val)}
                    # This is a broken circuit. Rewrite using:
                    # η_{i,j}∧η_{i,k} = η_{i,j}∧η_{j,k} - η_{i,k}∧η_{j,k}
                    # NO wait. From Arnold (line 581): η₁₂∧η₂₃ = η₁₂∧η₁₃ + η₁₃∧η₂₃
                    # So: η₁₂∧η₁₃ = η₁₂∧η₂₃ - η₁₃∧η₂₃
                    # In general: η_{ij}∧η_{ik} = η_{ij}∧η_{jk} - η_{ik}∧η_{jk}
                    # where (j,k) is the missing edge from the broken circuit.

                    # Replace: in the monomial, replace (i,j)∧(i,k) with
                    # (i,j)∧(j,k) - (i,k)∧(j,k)
                    missing = (j_val, k_val)

                    # Term 1: replace (i,k) with (j,k), same sign
                    new_mono_1 = list(mono_list)
                    # Find which is (i,j) and which is (i,k)
                    if ea == (i_val, j_val):
                        pos_ij, pos_ik = idx_a, idx_b
                    else:
                        pos_ij, pos_ik = idx_b, idx_a
                    new_mono_1[pos_ik] = missing
                    new_mono_1_sorted = tuple(sorted(new_mono_1))

                    # Count sign from sorting
                    sign_1 = _sort_sign(new_mono_1)

                    # Term 2: replace (i,j) with (j,k), swap sign
                    new_mono_2 = list(mono_list)
                    new_mono_2[pos_ij] = missing
                    # And swap positions of (j,k) and (i,k) relative to original
                    # Actually: η_{ij}∧η_{ik} at positions (pos_ij, pos_ik)
                    # becomes η_{ij}∧η_{jk} - η_{ik}∧η_{jk}
                    # Term 2 has η_{ik} at pos_ij and η_{jk} at pos_ik
                    # Wait, I need to be more careful. Let me just handle the
                    # case of degree 1 (two OS generators → one target generator)
                    # since that's what we need for n=3→n=2.

                    # For simplicity, just try both and recurse
                    result = {}

                    coeff_1 = _express_in_nbc_basis(
                        tuple(sorted(new_mono_1)), n, degree, basis)
                    s1 = _sort_sign(new_mono_1) * _sort_sign(list(mono_list))
                    for idx, c in coeff_1.items():
                        result[idx] = result.get(idx, 0) + s1 * c

                    # Term 2: -(i,k)∧(j,k)
                    new_mono_2 = list(mono_list)
                    new_mono_2[pos_ij] = (i_val, k_val)
                    new_mono_2[pos_ik] = missing
                    coeff_2 = _express_in_nbc_basis(
                        tuple(sorted(new_mono_2)), n, degree, basis)
                    s2 = _sort_sign(new_mono_2) * _sort_sign(list(mono_list))
                    for idx, c in coeff_2.items():
                        result[idx] = result.get(idx, 0) - s2 * c

                    return result

    # If no broken circuit found, it should be in the basis
    # This shouldn't happen
    return {}


def _sort_sign(lst):
    """Compute the sign of the permutation needed to sort lst."""
    sign = 1
    temp = list(lst)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
                sign *= -1
    return sign


# ---------------------------------------------------------------------------
# Bar differential matrix
# ---------------------------------------------------------------------------

def bar_differential_matrix(dim_g: int, sc: np.ndarray, n: int) -> np.ndarray:
    """Build the bar differential d: B-bar^n → B-bar^{n-1} as a matrix.

    B-bar^n = g^{⊗n} ⊗ OS^{n-1}(C_n), dim = dim_g^n × (n-1)!
    B-bar^{n-1} = g^{⊗(n-1)} ⊗ OS^{n-2}(C_{n-1}), dim = dim_g^{n-1} × (n-2)!

    The differential contracts each pair (i,j) via the bracket and
    restricts the OS form via Poincaré residue.

    At level k=0 for KM algebras: d_2 = 0 (combined pole cancellation).
    So we only implement d_{n≥3}.

    For n=2: returns zero matrix (d_2 = 0).
    For n≥3: implements the bracket + Poincaré residue.

    Parameters:
        dim_g: dimension of the Lie algebra
        sc: structure constants, sc[a,b,c] = f^{ab}_c
        n: source bar degree (d goes from B-bar^n to B-bar^{n-1})
    """
    import math

    if n <= 1:
        return np.zeros((1, dim_g))  # d_1: g → C is zero

    if n == 2:
        # d_2 = 0 (combined pole cancellation for KM at any level)
        source_dim = dim_g ** 2  # × 1 (OS^1(C_2) = 1-dim)
        target_dim = dim_g  # × 1 (OS^0(C_1) = 1-dim)
        return np.zeros((target_dim, source_dim))

    # For n ≥ 3:
    source_os = os_top_basis(n)
    target_os = os_top_basis(n - 1)

    source_os_dim = len(source_os)
    target_os_dim = len(target_os)

    source_dim = dim_g ** n * source_os_dim
    target_dim = dim_g ** (n - 1) * target_os_dim

    M = np.zeros((target_dim, source_dim))

    # Precompute Poincaré residue matrices for each pair (i,j)
    res_matrices = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            res_matrices[(i, j)] = poincare_residue_matrix(n, i, j)

    # Iterate over all source basis elements
    for gen_idx in range(dim_g ** n):
        # Decode generator indices: gen_idx encodes (a_1, ..., a_n) in base dim_g
        gens = []
        temp = gen_idx
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g
        gens = list(reversed(gens))  # gens[0] = a_1, ..., gens[n-1] = a_n

        for os_s_idx in range(source_os_dim):
            source_idx = gen_idx * source_os_dim + os_s_idx

            # Apply d = Σ_{i<j} bracket(a_i, a_j) ⊗ ∂_{ij}
            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):
                    a_i = gens[i - 1]  # 0-indexed
                    a_j = gens[j - 1]

                    # Poincaré residue of the OS form
                    res_M = res_matrices[(i, j)]

                    for os_t_idx in range(target_os_dim):
                        res_coeff = res_M[os_t_idx, os_s_idx]
                        if abs(res_coeff) < 1e-10:
                            continue

                        # Bracket [a_i, a_j]
                        for c in range(dim_g):
                            bracket_coeff = sc[a_i, a_j, c]
                            if abs(bracket_coeff) < 1e-10:
                                continue

                            # Build target generator tuple:
                            # Replace a_i with [a_i, a_j] = c, remove a_j
                            # Convention: merged element goes to position min(i,j),
                            # other elements shift to fill the gap.
                            target_gens = []
                            for k in range(n):
                                if k == i - 1:
                                    target_gens.append(c)
                                elif k == j - 1:
                                    continue
                                else:
                                    target_gens.append(gens[k])

                            # Encode target generator index
                            target_gen_idx = 0
                            for k, g in enumerate(target_gens):
                                target_gen_idx = target_gen_idx * dim_g + g

                            target_idx = target_gen_idx * target_os_dim + os_t_idx

                            # Sign: Koszul sign from moving (i,j) past other elements
                            # For degree-0 generators (KM currents), sign = (-1)^(j-i-1)
                            # Actually, the sign convention needs care.
                            # For now, use the sign from the definition:
                            # σ(i,j) accounts for the number of elements between i and j.
                            koszul_sign = (-1) ** (j - i - 1)

                            coeff = koszul_sign * bracket_coeff * res_coeff
                            M[target_idx, source_idx] += coeff

    return M


def compute_bar_cohomology(dim_g: int, sc: np.ndarray, max_degree: int = 4,
                           verbose: bool = True) -> Dict[int, int]:
    """Compute bar cohomology dimensions H^n for n = 1, ..., max_degree.

    H^n = ker(d_n: B-bar^n → B-bar^{n-1}) / im(d_{n+1}: B-bar^{n+1} → B-bar^n)

    Since d_2 = 0 for KM algebras: H^1 = B-bar^1 = dim(g).

    Returns dict {n: dim H^n}.
    """
    import math

    result = {}

    # H^1 = dim(g) (since d_2 = 0 and d_1 = 0)
    result[1] = dim_g
    if verbose:
        print(f"H^1 = {dim_g} (d_1 = 0, d_2 = 0)")

    # Compute d_n matrices for n = 3, ..., max_degree+1
    d_matrices = {}
    for deg in range(2, max_degree + 2):
        if verbose:
            os_dim = math.factorial(deg - 1)
            total_dim = dim_g ** deg * os_dim
            print(f"Building d_{deg}: dim {total_dim} → ...", end=" ", flush=True)
        d_matrices[deg] = bar_differential_matrix(dim_g, sc, deg)
        if verbose:
            print(f"shape {d_matrices[deg].shape}, rank = {np.linalg.matrix_rank(d_matrices[deg])}")

    # Compute cohomology
    for deg in range(2, max_degree + 1):
        # H^deg = ker(d_deg) / im(d_{deg+1})
        d_out = d_matrices[deg]  # d_deg: B^deg → B^{deg-1}
        d_in = d_matrices[deg + 1]  # d_{deg+1}: B^{deg+1} → B^deg

        rank_out = np.linalg.matrix_rank(d_out)
        rank_in = np.linalg.matrix_rank(d_in)

        chain_dim = d_out.shape[1]  # dim B^deg
        ker_dim = chain_dim - rank_out
        im_dim = rank_in

        h_deg = ker_dim - im_dim
        result[deg] = h_deg

        if verbose:
            print(f"H^{deg} = ker(d_{deg})/im(d_{deg+1}) = {ker_dim}/{im_dim} = {h_deg}")

    return result


# ---------------------------------------------------------------------------
# Quick tests
# ---------------------------------------------------------------------------

def test_sl2():
    """Test bar cohomology for sl₂."""
    names, sc = sl2_structure_constants()
    assert verify_jacobi(names, sc), "sl₂ Jacobi failed!"
    print("=== sl₂ bar cohomology ===")
    print(f"dim(sl₂) = {len(names)}")
    result = compute_bar_cohomology(len(names), sc, max_degree=3, verbose=True)
    print(f"\nResults: {result}")
    print(f"Expected: {{1: 3, 2: 6, 3: 15}}")
    return result


def test_sl3():
    """Test bar cohomology for sl₃."""
    names, sc = sl3_structure_constants()
    assert verify_jacobi(names, sc), "sl₃ Jacobi failed!"
    print("=== sl₃ bar cohomology ===")
    print(f"dim(sl₃) = {len(names)}")
    result = compute_bar_cohomology(len(names), sc, max_degree=3, verbose=True)
    print(f"\nResults: {result}")
    print(f"Expected: {{1: 8, 2: 36, 3: 204}}")
    return result


if __name__ == "__main__":
    test_sl2()
    print()
    test_sl3()
