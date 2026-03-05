"""Chiral bar differential v2: correct Poincaré residue computation.

Key insight: The Poincaré residue ∂_{ij} operates on OS forms via:
  1. Use Arnold relations to write ω = η_{ij} ∧ α + β (with no η_{ij} in β)
  2. Res_{D_{ij}}(ω) = α|_{z_i=z_j} (restrict and relabel)

The differential d₃: B̄³ → B̄² is:
  d₃(a⊗b⊗c, ω) = +[a,b]⊗c · ∂₁₂(ω) - [a,c]⊗b · ∂₁₃(ω) + a⊗[b,c] · ∂₂₃(ω)

Signs: (-1)^{j-i-1} for moving element at position j past intervening elements.
"""

import numpy as np
from typing import Dict, List, Tuple
from itertools import combinations


# ---------------------------------------------------------------------------
# Lie algebra structure constants
# ---------------------------------------------------------------------------

def sl2_structure_constants():
    """sl₂ = {e,h,f} with [h,e]=2e, [h,f]=-2f, [e,f]=h."""
    d = 3
    f = np.zeros((d, d, d))
    e, h, fgen = 0, 1, 2
    # [e, f] = h
    f[e, fgen, h] = 1; f[fgen, e, h] = -1
    # [h, e] = 2e
    f[h, e, e] = 2; f[e, h, e] = -2
    # [h, f] = -2f
    f[h, fgen, fgen] = -2; f[fgen, h, fgen] = 2
    return d, f


def sl3_structure_constants():
    """sl₃ with basis {e1,e2,e12,h1,h2,f1,f2,f12}, e12=[e1,e2], f12=[f2,f1]."""
    d = 8
    f = np.zeros((d, d, d))
    e1, e2, e12, h1, h2, f1, f2, f12 = range(8)

    def sb(a, b, c, v):
        f[a, b, c] += v; f[b, a, c] -= v

    # Cartan on positive roots
    sb(h1, e1, e1, 2); sb(h1, e2, e2, -1); sb(h1, e12, e12, 1)
    sb(h2, e1, e1, -1); sb(h2, e2, e2, 2); sb(h2, e12, e12, 1)
    # Cartan on negative roots
    sb(h1, f1, f1, -2); sb(h1, f2, f2, 1); sb(h1, f12, f12, -1)
    sb(h2, f1, f1, 1); sb(h2, f2, f2, -2); sb(h2, f12, f12, -1)
    # Positive root brackets
    sb(e1, e2, e12, 1)
    # Negative root brackets
    sb(f1, f2, f12, -1)  # f12 = [f2,f1]
    # e-f brackets
    sb(e1, f1, h1, 1); sb(e2, f2, h2, 1)
    sb(e12, f12, h1, 1); sb(e12, f12, h2, 1)
    # Cross brackets
    sb(e1, f12, f2, -1); sb(e2, f12, f1, 1)
    sb(e12, f1, e2, -1); sb(e12, f2, e1, 1)
    return d, f


def verify_jacobi(d, f):
    """Verify Jacobi identity for structure constants."""
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for e in range(d):
                    total = sum(f[a, b, k] * f[k, c, e] +
                                f[b, c, k] * f[k, a, e] +
                                f[c, a, k] * f[k, b, e] for k in range(d))
                    if abs(total) > 1e-10:
                        return False
    return True


# ---------------------------------------------------------------------------
# NBC basis for OS algebra
# ---------------------------------------------------------------------------

def nbc_basis(n, degree):
    """No-broken-circuit basis for OS^degree(C_n).

    Edges of K_n ordered lexicographically: (1,2) < (1,3) < ... < (n-1,n).
    Broken circuit from triangle (i,j,k) with i<j<k: remove lex-largest (j,k),
    giving broken circuit {(i,j), (i,k)}.
    NBC basis = degree-subsets of edges containing no broken circuit.
    """
    if degree == 0:
        return [()]
    edges = [(i, j) for i in range(1, n+1) for j in range(i+1, n+1)]
    broken = set()
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                broken.add(frozenset({(i, j), (i, k)}))
    basis = []
    for mono in combinations(edges, degree):
        if not any(bc.issubset(set(mono)) for bc in broken):
            basis.append(mono)
    return basis


# ---------------------------------------------------------------------------
# Poincaré residue via Arnold relation decomposition
# ---------------------------------------------------------------------------

def poincare_residue(n, i, j):
    """Compute ∂_{ij}: OS^{n-1}(C_n) → OS^{n-2}(C_{n-1}).

    Uses Arnold relations to decompose each basis form as η_{ij} ∧ α + β,
    then Res = α restricted to z_i = z_j with relabeling.

    Returns matrix M[target, source].
    """
    source = nbc_basis(n, n - 1)
    target = nbc_basis(n - 1, n - 2)
    if not source or not target:
        return np.zeros((max(len(target), 1), max(len(source), 1)))

    M = np.zeros((len(target), len(source)))
    edge = (min(i, j), max(i, j))

    for s_idx, mono in enumerate(source):
        # Decompose mono in the free exterior algebra as η_{ij} ∧ α + β
        # using Arnold relations: η_{ab}∧η_{ac} = η_{ab}∧η_{bc} - η_{ac}∧η_{bc}
        # (where b<c and (b,c) is the missing edge from the broken circuit {(a,b),(a,c)})
        alpha = _extract_factor(mono, edge, n)
        if alpha is None:
            continue

        # Restrict α to z_i = z_j and relabel
        for coeff, remaining in alpha:
            restricted = _restrict_and_relabel(remaining, min(i, j), max(i, j), n)
            if restricted is None:
                continue
            for rc, rmono in restricted:
                t_idx = _find_in_basis(rmono, target)
                if t_idx >= 0:
                    M[t_idx, s_idx] += coeff * rc

    return M


def _extract_factor(mono, edge, n):
    """Decompose monomial in free exterior algebra to extract η_{edge} factor.

    Returns list of (coefficient, remaining_edges) pairs for the α part,
    or None if the monomial doesn't contain edge even after Arnold rewriting.

    We work in the free exterior algebra and use Arnold relations to rewrite
    until we can extract the desired edge as a factor.
    """
    mono = list(mono)

    # Direct extraction: if edge is in the monomial
    if edge in mono:
        pos = mono.index(edge)
        sign = (-1) ** pos
        remaining = mono[:pos] + mono[pos+1:]
        return [(sign, tuple(remaining))]

    # Need Arnold relation to introduce the edge.
    # Arnold: for triangle (a,b,c) with a<b<c:
    #   η_{ab}∧η_{ac} = η_{ab}∧η_{bc} - η_{ac}∧η_{bc}
    # Equivalently: η_{ab}∧η_{bc} = η_{ab}∧η_{ac} + η_{ac}∧η_{bc}
    #
    # Strategy: find an edge sharing a vertex with our target edge,
    # and use Arnold to introduce the target.

    i, j = edge  # i < j

    # Look for edges sharing vertex i or j with our target (i,j)
    for pos, e in enumerate(mono):
        a, b = e
        if a == i:
            # Have (i, b). Need (i, j). Triangle (i, min(b,j), max(b,j)).
            if b != j:
                # Arnold: η_{i,min}∧η_{i,max} = η_{i,min}∧η_{min,max} - η_{i,max}∧η_{min,max}
                # We have (i,b). If b < j: we have η_{ib}, need η_{ij}.
                #   η_{ib}∧η_{ij} = η_{ib}∧η_{bj} - η_{ij}∧η_{bj} ... no
                # Let me think differently.
                # We want to replace some (i,b) by involving (i,j).
                # From Arnold: η_{ib}∧η_{bj} = η_{ib}∧η_{ij} + η_{ij}∧η_{bj}
                # So if we can find (b,j) in our monomial, great.
                # But we might not have (b,j).
                pass  # Fall through to general method
        if b == j:
            if a != i:
                pass  # similar
        if a == j:
            if b != i:  # can't happen since a < b and i < j
                pass
        if b == i:
            if a != j:  # a < b = i, so a < i < j
                pass

    # General approach: expand using Arnold relations recursively.
    # This is complex for degree > 2. Use the matrix approach instead.
    return _extract_factor_general(tuple(mono), edge, n)


def _extract_factor_general(mono, edge, n):
    """General extraction using systematic Arnold rewriting.

    For a monomial ω = η_{e1}∧...∧η_{ek}, decompose as η_{edge}∧α + β.

    Uses the fact that in OS^*(C_n), every form can be written uniquely
    in terms of any valid basis. We compute the decomposition by working
    in coordinates.
    """
    # Build the full OS algebra as a vector space with the NBC basis,
    # and compute the projection onto the η_{edge} ∧ OS^{k-1} subspace.

    degree = len(mono)
    basis = nbc_basis(n, degree)

    # First express mono in the NBC basis
    mono_coords = _express_in_nbc(mono, basis, n, degree)
    if mono_coords is None:
        return None

    # For each NBC basis element, extract the η_{edge} factor
    result = []
    for b_idx, coeff in enumerate(mono_coords):
        if abs(coeff) < 1e-10:
            continue
        bmono = basis[b_idx]
        if edge in bmono:
            pos = list(bmono).index(edge)
            sign = (-1) ** pos
            remaining = bmono[:pos] + bmono[pos+1:]
            result.append((coeff * sign, remaining))
        # If edge not in this basis element, it contributes to β, not α

    return result if result else None


def _express_in_nbc(mono, basis, n, degree):
    """Express a monomial (tuple of edges) in the NBC basis.

    Uses Arnold relations to reduce broken circuits.
    Returns coordinate vector, or None on failure.
    """
    coords = np.zeros(len(basis))

    # Check if already in basis
    mono_sorted = tuple(sorted(mono))
    sign = _sort_sign(list(mono))

    for idx, b in enumerate(basis):
        if tuple(b) == mono_sorted:
            coords[idx] = sign
            return coords

    # Find a broken circuit in the monomial and use Arnold to rewrite
    mono_list = list(mono_sorted)
    for pi in range(len(mono_list)):
        for pj in range(pi + 1, len(mono_list)):
            ea = mono_list[pi]
            eb = mono_list[pj]
            ia, ja = ea
            ib, jb = eb
            if ia == ib:  # broken circuit: {(i,j1), (i,j2)} with j1 < j2
                i_val = ia
                j1 = min(ja, jb)
                j2 = max(ja, jb)
                # Arnold: η_{i,j1}∧η_{i,j2} = η_{i,j1}∧η_{j1,j2} - η_{i,j2}∧η_{j1,j2}
                missing = (j1, j2)

                # Term 1: replace (i,j2) with (j1,j2)
                m1 = list(mono_sorted)
                idx_ij2 = m1.index((i_val, j2))
                m1[idx_ij2] = missing
                s1 = _sort_sign(m1)
                m1_sorted = tuple(sorted(m1))

                # Term 2: replace (i,j1) with (j1,j2), flip sign
                m2 = list(mono_sorted)
                idx_ij1 = m2.index((i_val, j1))
                m2[idx_ij1] = missing
                s2 = _sort_sign(m2)
                m2_sorted = tuple(sorted(m2))

                # Arnold: sorted_mono = sign * (s1 * m1_sorted - s2 * m2_sorted)
                # But sign from original sort was already accounted for
                c1 = _express_in_nbc(m1_sorted, basis, n, degree)
                c2 = _express_in_nbc(m2_sorted, basis, n, degree)

                if c1 is not None and c2 is not None:
                    return sign * (s1 * c1 - s2 * c2)
                return None

    # No broken circuit found but not in basis — shouldn't happen
    return None


def _sort_sign(lst):
    """Sign of permutation to sort lst."""
    sign = 1
    temp = list(lst)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
                sign *= -1
    return sign


def _restrict_and_relabel(edges, i, j, n):
    """Restrict edges to z_i = z_j and relabel to {1,...,n-1}.

    Merge: z_j → z_i (replace j with i in all edges, then relabel
    by removing j from {1,...,n}).

    Returns list of (coefficient, relabeled_mono) pairs.
    """
    new_edges = []
    for e in edges:
        a, b = e
        # Replace j with i
        if a == j: a = i
        if b == j: b = i
        # Relabel: remove index j
        if a > j: a -= 1
        if b > j: b -= 1
        # Normalize
        if a > b: a, b = b, a
        if a == b:
            return None  # degenerate
        new_edges.append((a, b))

    # Sort and track sign
    sign = _sort_sign(new_edges)
    sorted_edges = tuple(sorted(new_edges))
    return [(sign, sorted_edges)]


def _find_in_basis(mono, basis):
    """Find index of mono in basis, or -1."""
    for idx, b in enumerate(basis):
        if tuple(b) == tuple(mono):
            return idx
    return -1


# ---------------------------------------------------------------------------
# Bar differential
# ---------------------------------------------------------------------------

def bar_differential(dim_g, sc, n):
    """Build d_n: B̄ⁿ → B̄ⁿ⁻¹ as a matrix.

    d_n(a₁⊗...⊗aₙ, ω) = Σ_{i<j} (-1)^{j-i-1} [aᵢ,aⱼ]⊗(others) · ∂_{ij}(ω)

    Merged element [aᵢ,aⱼ] goes to position i, aⱼ deleted, others shift.
    """
    import math

    if n <= 1:
        return np.zeros((1, dim_g))

    if n == 2:
        # d₂ = 0 (combined pole cancellation)
        # source = g^{⊗2} ⊗ OS¹(C₂), target = g ⊗ OS⁰(C₁)
        return np.zeros((dim_g, dim_g ** 2))

    src_os = nbc_basis(n, n - 1)
    tgt_os = nbc_basis(n - 1, n - 2)
    src_os_dim = len(src_os)
    tgt_os_dim = len(tgt_os)
    src_dim = dim_g ** n * src_os_dim
    tgt_dim = dim_g ** (n - 1) * tgt_os_dim

    M = np.zeros((tgt_dim, src_dim))

    # Precompute residue matrices
    res = {}
    for ii in range(1, n + 1):
        for jj in range(ii + 1, n + 1):
            res[(ii, jj)] = poincare_residue(n, ii, jj)

    # Iterate source
    for gen_idx in range(dim_g ** n):
        # Decode
        gens = []
        tmp = gen_idx
        for _ in range(n):
            gens.append(tmp % dim_g)
            tmp //= dim_g
        gens.reverse()

        for os_s in range(src_os_dim):
            s_idx = gen_idx * src_os_dim + os_s

            for ii in range(1, n + 1):
                for jj in range(ii + 1, n + 1):
                    ai = gens[ii - 1]
                    aj = gens[jj - 1]

                    # Koszul sign: (-1)^{j-i-1}
                    ksign = (-1) ** (jj - ii - 1)

                    for c in range(dim_g):
                        bc = sc[ai, aj, c]
                        if abs(bc) < 1e-10:
                            continue

                        for os_t in range(tgt_os_dim):
                            rc = res[(ii, jj)][os_t, os_s]
                            if abs(rc) < 1e-10:
                                continue

                            # Build target gens: [ai,aj]=c at pos i, delete pos j
                            tgens = []
                            for k in range(n):
                                if k == ii - 1:
                                    tgens.append(c)
                                elif k == jj - 1:
                                    continue
                                else:
                                    tgens.append(gens[k])

                            tgen_idx = 0
                            for g in tgens:
                                tgen_idx = tgen_idx * dim_g + g

                            t_idx = tgen_idx * tgt_os_dim + os_t
                            M[t_idx, s_idx] += ksign * bc * rc

    return M


def compute_cohomology(dim_g, sc, max_deg=4, verbose=True):
    """Compute H^n(B̄(g)) for n = 1..max_deg."""
    result = {1: dim_g}
    if verbose:
        print(f"H^1 = {dim_g}")

    matrices = {}
    for deg in range(2, max_deg + 2):
        if verbose:
            import math
            chain = dim_g ** deg * math.factorial(deg - 1)
            print(f"Building d_{deg} (chain dim {chain})...", end=" ", flush=True)
        matrices[deg] = bar_differential(dim_g, sc, deg)
        if verbose:
            r = np.linalg.matrix_rank(matrices[deg])
            print(f"shape {matrices[deg].shape}, rank {r}")

    for deg in range(2, max_deg + 1):
        d_out = matrices[deg]
        d_in = matrices[deg + 1]
        rank_out = np.linalg.matrix_rank(d_out)
        rank_in = np.linalg.matrix_rank(d_in)
        chain_dim = d_out.shape[1]
        ker = chain_dim - rank_out
        h = ker - rank_in
        result[deg] = h
        if verbose:
            print(f"H^{deg} = dim(ker d_{deg}) - dim(im d_{deg+1}) = {ker} - {rank_in} = {h}")

    return result


def check_d_squared(dim_g, sc, n, verbose=True):
    """Verify d_{n-1} ∘ d_n = 0."""
    d_n = bar_differential(dim_g, sc, n)
    d_nm1 = bar_differential(dim_g, sc, n - 1)
    product = d_nm1 @ d_n
    maxval = np.max(np.abs(product))
    if verbose:
        print(f"d_{n-1} ∘ d_{n}: max entry = {maxval:.2e}")
    return maxval < 1e-8


if __name__ == "__main__":
    print("=== Verifying Jacobi ===")
    d2, sc2 = sl2_structure_constants()
    d3, sc3 = sl3_structure_constants()
    print(f"sl2 Jacobi: {verify_jacobi(d2, sc2)}")
    print(f"sl3 Jacobi: {verify_jacobi(d3, sc3)}")

    print("\n=== OS basis dimensions ===")
    for n in range(2, 6):
        for deg in range(n):
            b = nbc_basis(n, deg)
            print(f"  OS^{deg}(C_{n}) dim = {len(b)}")

    print("\n=== Poincaré residues for C_3 → C_2 ===")
    for i, j in [(1, 2), (1, 3), (2, 3)]:
        R = poincare_residue(3, i, j)
        print(f"  ∂_{i}{j} = {R.flatten()}")

    print("\n=== d² check ===")
    check_d_squared(d2, sc2, 3)
    check_d_squared(d2, sc2, 4)

    print("\n=== sl₂ bar cohomology ===")
    result2 = compute_cohomology(d2, sc2, max_deg=4, verbose=True)
    print(f"Result: {result2}")
    print(f"Expected: {{1:3, 2:6, 3:15, 4:36}}")

    print("\n=== sl₃ bar cohomology ===")
    result3 = compute_cohomology(d3, sc3, max_deg=3, verbose=True)
    print(f"Result: {result3}")
    print(f"Expected: {{1:8, 2:36, 3:204}}")
