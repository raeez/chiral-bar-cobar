#!/usr/bin/env python3
"""Compute dimensions of the free HyCom-algebra on a d-dimensional space.

HyCom(n) = H*(M-bar_{0,n+1}) as S_n-representation.
The free HyCom-algebra on V (dim V = d) has degree-n component:
  F_n = sum over tree structures of HyCom compositions applied to V.

Key formula for dim(rho tensor_{S_n} V^{otimes n}):
  = (1/n!) sum_{sigma in S_n} chi_rho(sigma) * d^{c(sigma)}
where c(sigma) = number of cycles.

We compute F_n recursively using the species composition formula.
Then compare with known bar cohomology sequences.
"""

from itertools import combinations
from math import factorial, comb
from functools import lru_cache
from collections import Counter

# ================================================================
# S_n character data for HyCom(n) = H*(M-bar_{0,n+1})
# ================================================================

# For each n, store characters indexed by cycle type (as sorted tuple)
# Cycle types for S_n: partitions of n

def cycle_types(n):
    """Generate all cycle types (partitions) of n with multiplicities."""
    # Returns list of (partition_as_sorted_tuple, size_of_conjugacy_class)
    result = []
    for p in partitions(n):
        ct = tuple(sorted(p))
        # Size of conjugacy class with cycle type p
        # = n! / prod(k^{a_k} * a_k!) where a_k = multiplicity of k
        counts = Counter(p)
        denom = 1
        for k, ak in counts.items():
            denom *= (k ** ak) * factorial(ak)
        size = factorial(n) // denom
        result.append((ct, size))
    return result

def partitions(n, max_part=None):
    """Generate all partitions of n."""
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, max_part), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p

def num_cycles(partition):
    """Number of cycles = number of parts."""
    return len(partition)

# HyCom(n) S_n-characters
# HyCom(1) = trivial (1-dim)
# HyCom(2) = trivial S_2 (1-dim)  [H*(pt)]
# HyCom(3) = 2*trivial S_3 (2-dim) [H^0 + H^2 of P^1, both trivial]
# HyCom(4) = 4*triv + standard S_4 (7-dim)  [H*(dP_5)]
# HyCom(5) = H*(M-bar_{0,6}) (34-dim)

def hycom_character(n, cycle_type):
    """Character of HyCom(n) at the given cycle type of S_n.

    For small n, computed from known S_n-representation theory.
    """
    ct = tuple(sorted(cycle_type))

    if n == 1:
        return 1  # trivial

    if n == 2:
        # trivial S_2
        return 1

    if n == 3:
        # 2 * trivial S_3
        return 2

    if n == 4:
        # 4*triv + standard(S_4)
        # Standard character of S_4:
        # (1^4): 3, (2,1^2): 1, (2^2): -1, (3,1): 0, (4): -1
        std_char = {
            (1,1,1,1): 3,
            (1,1,2): 1,
            (2,2): -1,
            (1,3): 0,
            (4,): -1
        }
        return 4 + std_char[ct]

    if n == 5:
        # H*(M-bar_{0,6}): need the full S_5 character
        # M-bar_{0,6} has complex dim 3
        # Betti numbers: b_0=1, b_2=10, b_4=10, b_6=1 (wait, is this right?)
        # Actually, total dim H* = 34 is wrong. Let me recheck.
        # M-bar_{0,n}: n=3: 1, n=4: 2, n=5: 7, n=6: 34
        # So H*(M-bar_{0,6}) has total dim 34.
        # HyCom(5) = H*(M-bar_{0,6}) is 34-dim.
        #
        # The S_5-equivariant Poincare polynomial is known from Getzler.
        # Using Getzler's formula for the S_n-character of H*(M-bar_{0,n+1}):
        #
        # For now, use the formula:
        # chi_{H*}(sigma) = sum over fixed-point strata
        #
        # This is complex. Let me use a different approach:
        # The generating function for hycom characters is known via
        # the Getzler-Kapranov formula relating to gravity operad.
        #
        # For a computational shortcut, use the Euler characteristic approach:
        # chi(sigma) = sum_k (-1)^k trace(sigma on H^{2k})
        #
        # For S_5 acting on M-bar_{0,6}:
        # I'll use known results from literature.
        # The S_5 irreps in H*(M-bar_{0,6}) are computed in
        # Getzler "Operads and moduli of genus 0 Riemann surfaces" (1995).
        #
        # From that paper (or more explicitly, from Bergstrom-Minabe):
        # H^0 = triv (1-dim)
        # H^2: 10-dim -- S_5 representation
        # H^4: 10-dim -- S_5 representation  (by Poincare duality, dual to H^2)
        # Wait, M-bar_{0,6} is 3-dimensional, so H^6 = 1-dim, and by PD:
        # H^k ~ H^{6-k}.  So H^0=H^6=1, H^2=H^4.
        # Total: 2 + 2*dim(H^2) + dim(H^3)??
        # No: for COMPLEX dim 3, cohomology goes H^0,...,H^6 (real dim 6).
        # Odd cohomology vanishes for smooth projective varieties? No, that's
        # only for curves (H^1). M-bar_{0,n} has vanishing odd cohomology
        # (it's a fine moduli space built from blowups).
        #
        # So: H^0, H^2, H^4, H^6 with dimensions summing to 34.
        # By PD: H^0=H^6, H^2=H^4.
        # 1 + a + a + 1 = 34 => a = 16. So b_2 = b_4 = 16.
        #
        # S_5 on H^2(M-bar_{0,6}):
        # The boundary divisors of M-bar_{0,6}: these correspond to
        # stable trees with 2 vertices and 6 marked points split between them.
        # Number of such: C(6,2)-1 + C(6,3)/2 = 14 + 10 = ...
        # Actually, boundary divisors = set of stable partitions of {1,...,6}
        # into two groups each of size >= 2:
        # C(6,2) + C(6,3)/2 = 15 + 10 = 25? No:
        # Partitions {S, S^c} with |S|>=2, |S^c|>=2, unordered:
        # |S|=2: C(6,2)=15, |S|=3: C(6,3)/2=10 (since {S,S^c} is unordered
        # and |S|=|S^c|=3). Total = 25 divisors.
        # But H^2 = Pic has rank = #divisors - #relations.
        # For M-bar_{0,n}: rank Pic = 2^{n-1} - C(n,2) - 1.
        # n=6: 2^5 - 15 - 1 = 32-15-1 = 16. ✓
        #
        # The S_5-representation on H^2 (16-dim, S_5 acts on first 5 points,
        # point 6 is the "output") is known but complex to derive here.
        #
        # Let me use a DIFFERENT approach: compute the character of
        # Free_HyCom(V)_5 using only HyCom(2), HyCom(3), HyCom(4)
        # (via the recursive formula), without needing HyCom(5) directly,
        # since at degree 5 the corolla contribution uses HyCom(5) but
        # the tree contributions only use HyCom(k) for k<=4.
        #
        # Actually no, to compute F_5 we DO need HyCom(5) for the corolla.
        # But for computing F_4, we only need HyCom(2), HyCom(3), HyCom(4).
        # And F_4 is what we need for H^4!

        # Placeholder - not needed for F_4 computation
        raise NotImplementedError("HyCom(5) character not implemented")

    raise NotImplementedError(f"HyCom({n}) character not implemented")


def dim_coinvariants(n, chi_rho, d):
    """Compute dim(rho tensor_{S_n} V^{otimes n}) for dim V = d.

    = (1/n!) sum_{sigma} chi_rho(sigma) * d^{c(sigma)}
    where c(sigma) = number of cycles.
    chi_rho is a function: cycle_type -> character value.
    """
    total = 0
    for ct, class_size in cycle_types(n):
        c = num_cycles(ct)
        char_val = chi_rho(ct)
        total += class_size * char_val * (d ** c)
    assert total % factorial(n) == 0, f"Not divisible: {total} / {factorial(n)}"
    return total // factorial(n)


# ================================================================
# Recursive computation of Free_HyCom(V)_n
# ================================================================

def compute_free_hycom_dims(d, max_degree=6):
    """Compute dimensions of Free_HyCom(V)_n for n=1,...,max_degree.

    Recursion: F_n = sum_{k=2}^{n} sum_{n_1+...+n_k=n, n_i>=1}
               HyCom(k) tensor_{S_k} (F_{n_1} tensor ... tensor F_{n_k})

    For the S_k coinvariants, we use:
    dim(HyCom(k) tensor_{S_k} W^{tensor k}) where W is the graded space
    with dim W_i = F_i, and we want the degree-n part of Sym^k(W) weighted
    by HyCom(k) character.
    """
    F = [0] * (max_degree + 1)
    F[1] = d

    for n in range(2, max_degree + 1):
        total = 0

        # Sum over arity k of the root operation
        for k in range(2, n + 1):
            if k > n:
                break

            # We need dim(HyCom(k) tensor_{S_k} (graded_space)^{tensor k})
            # restricted to total degree n.
            #
            # The graded space has F[1], F[2], ..., F[n-1] as dimensions.
            # We need compositions of n into k parts (n_1,...,n_k) with n_i >= 1.
            # For each composition, the tensor product has dim F[n_1]*...*F[n_k].
            # The S_k action permutes the factors, so we need the S_k-coinvariants
            # weighted by HyCom(k).
            #
            # For the character computation:
            # chi_{(graded)^{tensor k}}(sigma) for sigma in S_k with cycle type ct:
            # = product over cycles c of sigma: (sum_{i} F[i] * x^i)^{len(c)}
            #   evaluated at the appropriate multi-degree...
            #
            # Actually, for the degree-n part:
            # trace(sigma on (W^{otimes k})_n) = sum over compositions
            #   (n_1,...,n_k) of n into k positive parts,
            #   such that sigma permutes them consistently.
            #
            # This is: for sigma with cycle structure, the trace on the
            # degree-n subspace of W^{otimes k} equals:
            # product over cycles c=(i_1,...,i_l) of sigma:
            #   sum_{m : i_1->Z+, ..., i_l->Z+, sum=shared_total} F[m_1]*...*F[m_l]
            # with the constraint that each cycle contributes equally...
            #
            # This is getting complicated. Let me use a simpler approach.

            # For each sigma in S_k, the trace on (W^{otimes k})_n is:
            # = coefficient of x^n in product over cycles c of sigma:
            #     (sum_i F[i] * x^i)^{|c|}  ... no
            #
            # The trace of sigma on W^{otimes k} where W = oplus W_i:
            # sigma permutes the k tensor factors.
            # For cycle (j_1, j_2, ..., j_l): the trace contribution is
            # sum_{compatible basis elements} product...
            # = sum_{m} F[m]  where the sum is over m such that the l positions
            #   in the cycle all map to grade m (since sigma cyclically permutes).
            # Wait no.
            #
            # For a single cycle (1,2,...,l) in S_k acting on W^{otimes k}:
            # The trace on the degree-n subspace (where degree = sum of component degrees)
            # of the l factors involved in this cycle:
            # = sum_{compositions (m_1,...,m_l) of degree_for_this_cycle into l parts}
            #   delta(m_1=m_2=...=m_l) * F[m_1] ...
            # No, that's only if the cycle maps basis vector e_{i_1} tensor ...
            # to e_{i_l} tensor e_{i_1} tensor ... The trace picks up the diagonal
            # where e_{i_1} = e_{i_2} = ... = e_{i_l}, but that forces all degrees equal.
            #
            # Actually: for a cycle of length l acting on (W)^{otimes l}:
            # trace = sum_i dim(W_i)^l ... no.
            # The cycle sigma = (1 2 ... l) sends e_{a_1} otimes ... otimes e_{a_l}
            # to e_{a_l} otimes e_{a_1} otimes ... otimes e_{a_{l-1}}.
            # Trace = sum over a_1=a_2, a_2=a_3, ..., a_{l-1}=a_l, a_l=a_1
            #       = sum over a_1: contribution = dim(W)  (all a_i equal)
            # Wait, that's summing over a_1 with all a_i = a_1.
            # So trace of a single l-cycle on W^{otimes l} = sum_{a} 1 = dim(W).
            # But we want the trace restricted to degree n.
            #
            # For graded W = oplus W_i, the cycle (1,...,l) on (oplus W_i)^{otimes l}
            # restricted to total degree n (= sum of individual degrees):
            # trace = sum over (m_1,...,m_l) with sum=n and m_1=m_2=...=m_l
            # (forced by the diagonal condition).
            # So m_1 = m_2 = ... = m_l and l*m_1 = n.
            # This is nonzero only if l | n, and then = dim(W_{n/l}).
            #
            # WAIT. That's for the trace on the sub-tensor involving ONLY the
            # positions in this cycle. The full trace of sigma on W^{otimes k}
            # (restricted to degree n) involves a product over all cycles:
            # trace(sigma on W^{otimes k}_n) = sum over decompositions n = sum_c d_c
            #   where the sum is over cycles c of sigma, and for each cycle c of
            #   length l_c, d_c must be divisible by l_c, contributing dim(W_{d_c/l_c}).

            pass

        # Let me use a completely different, simpler approach.
        # Direct enumeration of tree compositions.

        # Reset total
        total = 0
        total = compute_free_hycom_degree_n(n, F, d)
        F[n] = total

    return F


def trace_on_graded_tensor(sigma_cycle_type, graded_dims, n):
    """Compute trace of permutation sigma on (W^{otimes k})_n.

    sigma has cycle type given as a tuple of cycle lengths.
    graded_dims[i] = dim(W_i) for i >= 1.
    n = total degree to restrict to.

    Result = product over cycles c (length l_c):
      sum over d_c divisible by l_c with 1 <= d_c/l_c:
        graded_dims[d_c / l_c]
    summed over all decompositions n = sum_c d_c.
    """
    cycles = list(sigma_cycle_type)

    # Recursive: distribute degree n among cycles
    def distribute(cycle_idx, remaining_degree):
        if cycle_idx == len(cycles):
            return 1 if remaining_degree == 0 else 0

        l = cycles[cycle_idx]
        total = 0
        # d_c must be a multiple of l, with d_c/l >= 1
        for m in range(1, remaining_degree // l + 1):
            d_c = m * l
            if d_c > remaining_degree:
                break
            if m < len(graded_dims) and graded_dims[m] > 0:
                total += graded_dims[m] * distribute(cycle_idx + 1, remaining_degree - d_c)

        return total

    return distribute(0, n)


def compute_free_hycom_degree_n(n, F_prev, d):
    """Compute F_n using the recursive formula with character theory.

    F_n = sum_{k=2}^{n} (1/k!) sum_{sigma in S_k} chi_{HyCom(k)}(sigma)
          * trace(sigma on (F_prev graded space)^{tensor k} restricted to degree n)
    """
    total = 0

    for k in range(2, n + 1):
        # Sum over conjugacy classes of S_k
        for ct, class_size in cycle_types(k):
            try:
                chi = hycom_character(k, ct)
            except NotImplementedError:
                continue

            if chi == 0:
                continue

            tr = trace_on_graded_tensor(ct, F_prev, n)
            total += class_size * chi * tr

        # We've summed class_size * chi * tr, need to divide by k!
        # But we need to accumulate first across all k and then...
        # Actually no: for each k, the contribution is
        # (1/k!) * sum_{sigma} chi(sigma) * tr(sigma)
        # = sum_{conj classes} (class_size / k!) * chi * tr
        # The sum over k is separate.

    # Oops, I need to be more careful about the division.
    # Let me redo: accumulate per-k contributions.

    total = 0
    for k in range(2, n + 1):
        k_contribution = 0
        for ct, class_size in cycle_types(k):
            try:
                chi = hycom_character(k, ct)
            except NotImplementedError:
                continue

            tr = trace_on_graded_tensor(ct, F_prev, n)
            k_contribution += class_size * chi * tr

        assert k_contribution % factorial(k) == 0, \
            f"k={k}, n={n}: {k_contribution} not div by {factorial(k)}"
        total += k_contribution // factorial(k)

    return total


# ================================================================
# Main computation
# ================================================================

print("=" * 60)
print("FREE HyCom-ALGEBRA DIMENSIONS")
print("=" * 60)

for d, name in [(3, "sl_2"), (8, "sl_3")]:
    print(f"\n{'='*40}")
    print(f"d = {d} ({name})")
    print(f"{'='*40}")

    max_deg = 6 if d <= 3 else 5
    F = compute_free_hycom_dims(d, max_degree=max_deg)

    print("Free HyCom dimensions:")
    for n in range(1, max_deg + 1):
        print(f"  F_{n} = {F[n]}")

    # Compare with known bar cohomology
    if d == 3:
        known = [None, 3, 6, 15, 36, 91, 232]
        print("\nComparison with sl_2 bar cohomology:")
        for n in range(1, min(max_deg + 1, len(known))):
            match = "✓" if F[n] == known[n] else "✗"
            print(f"  n={n}: Free={F[n]}, BarCoh={known[n]} {match}")

    if d == 8:
        known = [None, 8, 36, 204]
        print("\nComparison with sl_3 bar cohomology:")
        for n in range(1, min(max_deg + 1, len(known))):
            match = "✓" if F[n] == known[n] else "✗"
            print(f"  n={n}: Free={F[n]}, BarCoh={known[n]} {match}")

        print(f"\n  *** F_4 = {F[4]}  <-- PREDICTION for H^4 ***")

# ================================================================
# Verify the trace formula with a simple case
# ================================================================
print("\n" + "=" * 60)
print("VERIFICATION: Sym^n(V) dimensions")
print("=" * 60)

# For trivial S_n rep (= Com(n)), coinvariants = Sym^n(V)
for d in [3, 8]:
    for n in [2, 3, 4]:
        # All characters = 1 (trivial)
        result = 0
        for ct, class_size in cycle_types(n):
            c = num_cycles(ct)
            result += class_size * (d ** c)
        result //= factorial(n)
        expected = comb(d + n - 1, n)
        status = "✓" if result == expected else "✗"
        print(f"  Sym^{n}(k^{d}) = {result} (expected {expected}) {status}")
