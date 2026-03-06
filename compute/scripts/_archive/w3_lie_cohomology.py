#!/usr/bin/env python3
"""
Compute W₃ bar cohomology via PBW spectral sequence.

For a Koszul vertex algebra, the PBW spectral sequence collapses at E₂:
  E₁ = Λ(V*) (exterior algebra on mode dual space)
  d₁ = Chevalley-Eilenberg differential from classical Poisson bracket
  E₂ = H*(L, ℂ) = bar cohomology

The Lie algebra L for W₃ is:
  Generators: L_{-m} (m≥2), W_{-m} (m≥3)
  Brackets:
    [L_{-m}, L_{-n}] = (n-m) L_{-(m+n)}  (Witt subalgebra)
    [L_{-m}, W_{-n}] = (n-2m) W_{-(m+n)}
    [W_{-m}, W_{-n}] = β(m,n) L_{-(m+n)}  (classical W₃ bracket)

The coefficient β(m,n) comes from the W-W OPE zeroth product
in the classical limit (PBW level 0).

For the Virasoro algebra (L alone), this gives the Goncharova/Fuchs computation
of H*(L₁, ℂ) where L₁ = {L_{-m} : m ≥ 2} is the Witt subalgebra.
"""

from fractions import Fraction as F
from itertools import combinations
import sys

# ===== W₃ Lie algebra structure constants =====

def ww_bracket_coeff(m, n):
    """
    Coefficient of L_{-(m+n)} in [W_{-m}, W_{-n}] (classical W₃).

    From [W_a, W_b] = Σ C(a+2,j) (W_{(j)}W)_{a+b}
    where the linear part involves:
      j=3: 2T → 2 L_{a+b}
      j=2: ∂T → -(a+b+2) L_{a+b}
      j=1: 3/10 ∂²T → 3/10 (a+b+2)(a+b+3) L_{a+b}
      j=0: -1/15 ∂³T → -1/15 (a+b+2)(a+b+3)(a+b+4) L_{a+b}

    For [W_{-m}, W_{-n}], set a=-m, b=-n.
    """
    a, b = -m, -n  # actual mode indices
    s = a + b  # = -(m+n)

    def binom(nn, k):
        """Generalized binomial coefficient C(nn, k) = nn*(nn-1)*...*(nn-k+1)/k!"""
        if k < 0: return F(0)
        if k == 0: return F(1)
        result = F(1)
        for i in range(k):
            result *= F(nn - i)
        for i in range(1, k + 1):
            result /= F(i)
        return result

    # j=3: C(a+2,3) * 2
    t3 = binom(a + 2, 3) * 2
    # j=2: C(a+2,2) * (-(s+2))  where s=a+b
    t2 = binom(a + 2, 2) * (-(s + 2))
    # j=1: C(a+2,1) * 3/10 * (s+2)*(s+3)
    t1 = binom(a + 2, 1) * F(3, 10) * (s + 2) * (s + 3)
    # j=0: C(a+2,0) * (-1/15) * (s+2)*(s+3)*(s+4)
    t0 = binom(a + 2, 0) * F(-1, 15) * (s + 2) * (s + 3) * (s + 4)

    return t3 + t2 + t1 + t0


def bracket(gen_i, gen_j, max_weight):
    """
    Compute [gen_i, gen_j] in the classical W₃ Lie algebra.
    gen_i, gen_j are tuples ('L', m) or ('W', m) meaning L_{-m} or W_{-m}.
    Returns a list of (coefficient, gen) pairs.
    """
    ti, mi = gen_i
    tj, mj = gen_j
    result = []
    target_m = mi + mj  # weight of the bracket output

    if target_m > max_weight:
        return []

    if ti == 'L' and tj == 'L':
        # [L_{-mi}, L_{-mj}] = (mj - mi) L_{-(mi+mj)}
        c = F(mj - mi)
        if c != 0 and target_m >= 2:
            result.append((c, ('L', target_m)))
    elif ti == 'L' and tj == 'W':
        # [L_{-mi}, W_{-mj}] = (mj - 2*mi) W_{-(mi+mj)}
        c = F(mj - 2 * mi)
        if c != 0 and target_m >= 3:
            result.append((c, ('W', target_m)))
    elif ti == 'W' and tj == 'L':
        # [W_{-mi}, L_{-mj}] = -[L_{-mj}, W_{-mi}] = -(mi - 2*mj) W_{-(mi+mj)}
        c = F(-(mi - 2 * mj))
        if c != 0 and target_m >= 3:
            result.append((c, ('W', target_m)))
    elif ti == 'W' and tj == 'W':
        # [W_{-mi}, W_{-mj}] = β(mi,mj) L_{-(mi+mj)}
        c = ww_bracket_coeff(mi, mj)
        if c != 0 and target_m >= 2:
            result.append((c, ('L', target_m)))

    return result


def compute_ce_cohomology(max_weight, algebra='W3'):
    """
    Compute Chevalley-Eilenberg cohomology H^n(L, ℂ) weight by weight.

    The CE complex: Λ^n(L*) with differential
    d: Λ^n(L*) -> Λ^{n+1}(L*)
    (dω)(x_0,...,x_n) = Σ_{i<j} (-1)^{i+j} ω([x_i,x_j], x_0,...,x̂_i,...,x̂_j,...,x_n)

    We use the dual picture: basis of L indexed by generators,
    and the CE differential maps n-cochains to (n+1)-cochains.
    """
    # Generators up to weight max_weight
    gens = []
    gen_index = {}
    for m in range(2, max_weight + 1):
        gen_index[('L', m)] = len(gens)
        gens.append(('L', m))
    if algebra in ('W3', 'W3_trunc'):
        for m in range(3, max_weight + 1):
            gen_index[('W', m)] = len(gens)
            gens.append(('W', m))

    N = len(gens)
    print(f"Algebra: {algebra}, max_weight={max_weight}, {N} generators")

    # Weight of each generator
    def gen_weight(g):
        return g[1]

    # Precompute brackets
    bracket_table = {}
    for i in range(N):
        for j in range(i + 1, N):
            br = bracket(gens[i], gens[j], max_weight)
            if br:
                bracket_table[(i, j)] = br

    # For each weight h, compute the CE complex at that weight
    # Λ^n(L*)_h = {subsets S ⊂ {0,...,N-1} with |S|=n and Σ weight(gens[i] for i in S) = h}

    # CE differential: d(e^{i_1} ∧ ... ∧ e^{i_n}) =
    # Σ_{a<b in S} (-1)^{pos(a)+pos(b)+1} [structure const] e^{bracket} ∧ (rest)

    # Actually, the CE differential on Λ^n(L*) acts by:
    # (dφ)(v_0,...,v_n) = Σ_{i<j} (-1)^{i+j} φ([v_i,v_j], v_0,...,v̂_i,...,v̂_j,...,v_n)
    # In the dual basis:
    # d(e^{i_1} ∧ ... ∧ e^{i_n}) maps to Λ^{n+1}(L*)
    # by: for each bracket [e_a, e_b] = c^k_{ab} e_k,
    # d includes a term ± c^k_{ab} · (e^a ∧ e^b) wedged into the form.

    # More concretely: enumerate basis of Λ^n_h as sorted tuples.

    results = {}

    for h in range(2, max_weight + 1):
        # Enumerate all n-element subsets of generators with total weight h
        # for n = 0, 1, 2, ..., h//2

        spaces = {}  # n -> list of basis elements (sorted tuples of gen indices)

        for n in range(0, N + 1):
            basis_n = []
            for combo in combinations(range(N), n):
                wt = sum(gen_weight(gens[i]) for i in combo)
                if wt == h:
                    basis_n.append(combo)
            if basis_n:
                spaces[n] = basis_n

        # For each pair (n, n+1), compute the CE differential matrix
        # d: Λ^n_h -> Λ^{n+1}_h

        for n in sorted(spaces.keys()):
            if n + 1 not in spaces:
                continue

            source = spaces[n]
            target = spaces[n + 1]

            if not source or not target:
                continue

            # Build matrix: rows = target basis, cols = source basis
            # d maps source to target
            target_index = {t: idx for idx, t in enumerate(target)}
            mat = [[F(0)] * len(source) for _ in range(len(target))]

            for col, src in enumerate(source):
                src_set = set(src)
                src_list = list(src)

                # The CE differential: for each pair (a,b) of generators NOT in src,
                # if [e_a, e_b] = c^k e_k where k IS in src,
                # we add a term with e^a ∧ e^b replacing e^k.
                #
                # Actually that's the wrong direction. Let me think again.
                #
                # The CE COBOUNDARY operator d: C^n -> C^{n+1} is:
                # (dω)(x_0,...,x_n) = Σ_{i<j} (-1)^{i+j} ω([x_i,x_j], x_0,...,x̂_i,...,x̂_j,...,x_n)
                #
                # For ω = e^{k_1} ∧ ... ∧ e^{k_n} (dual basis):
                # ω([x_i,x_j], x_0,...) is nonzero only if the argument set
                # (with [x_i,x_j] replacing x_i,x_j) matches {k_1,...,k_n}.
                #
                # So (dω)(x_0,...,x_n) ≠ 0 iff:
                # there exist i<j such that [x_i,x_j] has a component along some e_k
                # and {x_0,...,x̂_i,...,x̂_j,...,x_n} ∪ {e_k} = {k_1,...,k_n}
                # i.e., {x_0,...,x̂_i,...,x̂_j,...,x_n} = {k_1,...,k_n} \ {e_k}

                # Equivalently, in the DUAL picture:
                # d(e^{k_1} ∧ ... ∧ e^{k_n}) = Σ over structure constants
                #   c^{k_r}_{ab} with a < b, a,b ∉ {k_1,...,k_n}, k_r ∈ {k_1,...,k_n}
                #   (-1)^{r+1} ... hmm this is getting complicated.

                # Let me use the standard formula:
                # d(e^{k_1} ∧ ... ∧ e^{k_n}) =
                #   -Σ_{r=1}^{n} Σ_{b ∉ {k_1,...,k_n}} c^{k_r}_{k_r,b-stuff}...

                # Actually the cleanest way:
                # The CE differential in the exterior algebra basis is:
                # d = Σ_{a<b,k} c^k_{ab} e^a ∧ e^b ∧ ι_{e_k}
                # where ι_{e_k} is the contraction (interior product).
                # So d(e^{k_1}∧...∧e^{k_n}) = Σ_{a<b,k} c^k_{ab} e^a ∧ e^b ∧ ι_{e_k}(e^{k_1}∧...∧e^{k_n})
                # = Σ_{a<b} Σ_{r: k_r is in structure constants}
                #   c^{k_r}_{ab} (-1)^{r-1} e^a ∧ e^b ∧ e^{k_1}∧...∧ê^{k_r}∧...∧e^{k_n}
                # where a,b must NOT be in {k_1,...,k_n}\{k_r}
                # and {a,b} must be ordered and not equal to any remaining k_s.

                for r, kr in enumerate(src_list):
                    # For each k_r in the source set,
                    # contract and look for brackets [e_a, e_b] = c * e_{k_r} + ...
                    # where a, b are NOT in remaining = src \ {k_r}
                    remaining = set(src_set)
                    remaining.remove(kr)

                    # Find all (a,b) with a<b such that [e_a, e_b] has a component along e_{k_r}
                    for (a, b), br_list in bracket_table.items():
                        for coeff, gen_result in br_list:
                            if gen_result not in gen_index:
                                continue
                            result_idx = gen_index[gen_result]
                            if result_idx != kr:
                                continue
                            # Found: [e_a, e_b] has component coeff * e_{k_r}
                            # Check a, b not in remaining
                            if a in remaining or b in remaining:
                                continue
                            # Also a != b (guaranteed by a<b from bracket_table)
                            # Build target: {a, b} ∪ remaining
                            target_set = remaining | {a, b}
                            target_tuple = tuple(sorted(target_set))
                            if len(target_tuple) != n + 1:
                                continue  # collision
                            if target_tuple not in target_index:
                                continue

                            # Sign: (-1)^{r} from contraction,
                            # then sign from inserting a,b into the remaining list
                            # ι_{k_r} on e^{k_1}∧...∧e^{k_n} gives (-1)^{r} e^{k_1}∧...∧ê^{k_r}∧...
                            # (where r is 0-indexed position)
                            sign_contract = (-1) ** r

                            # Now we need to insert a and b into the sorted remaining
                            # to get the target_tuple, and track the sign
                            rem_sorted = sorted(remaining)
                            # Insert a: count how many elements of rem_sorted are < a
                            pos_a = sum(1 for x in rem_sorted if x < a)
                            sign_a = (-1) ** pos_a
                            # Insert b: count elements < b in (rem_sorted with a inserted)
                            extended = sorted(rem_sorted + [a])
                            pos_b = sum(1 for x in extended if x < b)
                            sign_b = (-1) ** pos_b

                            total_sign = sign_contract * sign_a * sign_b

                            row = target_index[target_tuple]
                            mat[row][col] += (-1) * coeff * total_sign
                            # The (-1) comes from the CE differential convention:
                            # d = -Σ c^k_{ab} e^a ∧ e^b ∧ ι_k
                            # (the negative sign ensures d² = 0 with [,] convention)

            # Store the matrix dimensions for later
            if n not in results:
                results[n] = {'dim': {}, 'ker': {}, 'im': {}}
            if n + 1 not in results:
                results[n + 1] = {'dim': {}, 'ker': {}, 'im': {}}

            results[n]['dim'][h] = results[n].get('dim', {}).get(h, len(source))
            results[n + 1]['dim'][h] = results[n + 1].get('dim', {}).get(h, len(target))

            # Compute rank of mat
            rank = gaussian_rank(mat, len(target), len(source))

            # im(d: Λ^n -> Λ^{n+1}) at weight h has dimension = rank
            results[n + 1]['im'][h] = results[n + 1].get('im', {}).get(h, 0) + rank
            # For the kernel computation, we need ker(d: Λ^n -> Λ^{n+1})
            # But we're computing d: Λ^n -> Λ^{n+1}, so
            # ker at degree n = dim(Λ^n) - rank(d: Λ^n -> Λ^{n+1})
            # BUT we also need to add the contribution from d: Λ^{n-1} -> Λ^n
            # Let me store ranks and compute cohomology at the end

        # Also record dimensions for degrees with no outgoing differential
        for n in spaces:
            if n not in results:
                results[n] = {'dim': {}, 'ker': {}, 'im': {}}
            results[n]['dim'][h] = len(spaces[n])

    return results, gens, gen_index, N


def gaussian_rank(mat, nrows, ncols):
    """Compute rank of matrix over rationals."""
    if nrows == 0 or ncols == 0:
        return 0
    A = [row[:] for row in mat]
    r = 0
    for col in range(ncols):
        piv = None
        for row in range(r, nrows):
            if A[row][col] != 0:
                piv = row
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][col]
        for row in range(nrows):
            if row != r and A[row][col] != 0:
                fac = A[row][col] / pv
                for c2 in range(ncols):
                    A[row][c2] -= fac * A[r][c2]
        r += 1
    return r


def compute_ce_weight_graded(max_weight, algebra='W3'):
    """
    Compute CE cohomology weight by weight using the differential
    d: Λ^n_h -> Λ^{n+1}_h (the weight-preserving part).

    Return dim H^n = Σ_h dim H^n_h.
    """
    # Generators
    gens = []
    gen_index = {}
    for m in range(2, max_weight + 1):
        gen_index[('L', m)] = len(gens)
        gens.append(('L', m))
    if algebra in ('W3',):
        for m in range(3, max_weight + 1):
            gen_index[('W', m)] = len(gens)
            gens.append(('W', m))

    N = len(gens)

    # Precompute brackets
    bracket_cache = {}
    for i in range(N):
        for j in range(i + 1, N):
            br = bracket(gens[i], gens[j], max_weight)
            for coeff, gen_result in br:
                if gen_result in gen_index:
                    k = gen_index[gen_result]
                    if (i, j) not in bracket_cache:
                        bracket_cache[(i, j)] = []
                    bracket_cache[(i, j)].append((coeff, k))

    # For each weight h, build the complex and compute cohomology
    # Store: rank of d: Λ^n_h -> Λ^{n+1}_h for each (n, h)

    dim_table = {}  # (n, h) -> dim Λ^n_h
    rank_table = {}  # (n, h) -> rank of d: Λ^n_h -> Λ^{n+1}_h

    for h in range(2, max_weight + 1):
        # Enumerate basis for each degree n
        spaces = {}
        for n in range(0, N + 1):
            basis = []
            for combo in combinations(range(N), n):
                wt = sum(gens[i][1] for i in combo)
                if wt == h:
                    basis.append(combo)
            if basis:
                spaces[n] = basis
                dim_table[(n, h)] = len(basis)

        # Compute differential d: Λ^n -> Λ^{n+1} at weight h
        for n in sorted(spaces.keys()):
            if n + 1 not in spaces:
                rank_table[(n, h)] = 0
                continue

            source = spaces[n]
            target = spaces[n + 1]
            target_idx = {t: i for i, t in enumerate(target)}

            mat = [[F(0)] * len(source) for _ in range(len(target))]

            for col, src in enumerate(source):
                src_set = set(src)
                src_list = list(src)

                for r_pos, kr in enumerate(src_list):
                    remaining = list(src_list)
                    remaining.pop(r_pos)
                    rem_set = set(remaining)
                    sign_contract = (-1) ** r_pos

                    for (a, b), br_list in bracket_cache.items():
                        if a in rem_set or b in rem_set:
                            continue
                        for coeff, k_idx in br_list:
                            if k_idx != kr:
                                continue

                            new_set = set(remaining) | {a, b}
                            if len(new_set) != n + 1:
                                continue
                            new_tuple = tuple(sorted(new_set))
                            if new_tuple not in target_idx:
                                continue

                            # Sign computation
                            rem_sorted = sorted(remaining)
                            pos_a = sum(1 for x in rem_sorted if x < a)
                            temp = sorted(rem_sorted + [a])
                            pos_b = sum(1 for x in temp if x < b)

                            total_sign = sign_contract * ((-1) ** pos_a) * ((-1) ** pos_b)

                            row = target_idx[new_tuple]
                            mat[row][col] += (-1) * coeff * total_sign

            rank_table[(n, h)] = gaussian_rank(mat, len(target), len(source))

    # Compute cohomology: H^n_h = dim Λ^n_h - rank(d: Λ^n -> Λ^{n+1}) - rank(d: Λ^{n-1} -> Λ^n)
    # i.e., H^n_h = ker(d^n_h) / im(d^{n-1}_h) = (dim - rank_out) - rank_in

    cohom = {}  # n -> total dim H^n
    cohom_by_weight = {}  # (n, h) -> dim H^n_h

    max_n = max(n for (n, h) in dim_table) if dim_table else 0

    for n in range(0, max_n + 1):
        total = 0
        for h in range(2, max_weight + 1):
            dim_n_h = dim_table.get((n, h), 0)
            rank_out = rank_table.get((n, h), 0)  # rank of d: Λ^n_h -> Λ^{n+1}_h
            rank_in = rank_table.get((n - 1, h), 0)  # rank of d: Λ^{n-1}_h -> Λ^n_h

            h_n_h = dim_n_h - rank_out - rank_in
            if h_n_h != 0:
                cohom_by_weight[(n, h)] = h_n_h
                total += h_n_h

        if total != 0:
            cohom[n] = total

    return cohom, cohom_by_weight


if __name__ == '__main__':
    # First verify on Virasoro
    print("=" * 70)
    print("VIRASORO (L₁ subalgebra of Witt)")
    print("Expected: H^1=1, H^2=2, H^3=5, H^4=12, H^5=30")
    print("=" * 70)

    for mw in [10, 14, 18]:
        print(f"\n--- max_weight = {mw} ---")
        cohom, cohom_wt = compute_ce_weight_graded(mw, algebra='Virasoro')
        print(f"H^n dimensions: {dict(sorted(cohom.items()))}")
        # Show weight distribution for small n
        for n in range(1, 6):
            wts = {h: d for (nn, h), d in cohom_wt.items() if nn == n and d != 0}
            if wts:
                print(f"  H^{n} by weight: {dict(sorted(wts.items()))} = {sum(wts.values())}")

    print("\n\n" + "=" * 70)
    print("W₃ ALGEBRA")
    print("Expected: H^1=2, H^2=5, H^3=16, H^4=52, H^5=?")
    print("=" * 70)

    for mw in [10, 14, 18]:
        print(f"\n--- max_weight = {mw} ---")
        cohom, cohom_wt = compute_ce_weight_graded(mw, algebra='W3')
        print(f"H^n dimensions: {dict(sorted(cohom.items()))}")
        for n in range(1, 7):
            wts = {h: d for (nn, h), d in cohom_wt.items() if nn == n and d != 0}
            if wts:
                print(f"  H^{n} by weight: {dict(sorted(wts.items()))} = {sum(wts.values())}")
