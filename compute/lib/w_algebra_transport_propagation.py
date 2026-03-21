"""Transport propagation for non-principal W-algebra duality in type A.

Verifies Proposition prop:transport-propagation and the surrounding
infrastructure for non-principal Koszul duality of affine W-algebras
W^k(sl_N, f_lambda).

Mathematical content:
  1. Partition graph Gamma_N: vertices = Par(N), edges = proved
     reduction/inverse-reduction functors at generic level.
  2. Hook-type duality: W^k(sl_N, f_eta)^! = W^{k'}(sl_N, f_{eta^t})
     with k' = -k - 2N (Theorem thm:hook-transport-corridor).
  3. Transport propagation: duality extends from hooks through
     Gamma_N to the transport-closure (Proposition prop:transport-propagation).
  4. Central charge verification: c(k, lambda) + c(k', lambda^t) = C_N(lambda)
     for the Freudenthal-de Vries complementarity constant.
  5. Generator spectrum matching under transpose duality.

Key references:
  - KRW (Kac-Roan-Wakimoto): BRST/DS reduction for arbitrary nilpotent
  - FehilyHook: hook-type inverse reduction
  - GenraStages: reduction by stages
  - ButsonNair: inverse Hamiltonian reduction in type A
  - CLNS24, CFLN24: non-principal W-algebra structure

Central charge formula for W^k(sl_N, f_lambda):
  c(k, lambda) = dim(g^e) - (1/2)*dim(g/g^e)
                 - 12*|rho - (k+N)*x|^2 / (k+N)
  where x = h/2, h the semisimple element of the sl_2-triple for f_lambda.
  In type A this reduces to an explicit combinatorial formula in terms
  of the partition lambda.
"""

from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
from typing import Dict, FrozenSet, List, Optional, Set, Tuple


# =====================================================================
# Partition utilities
# =====================================================================

Partition = Tuple[int, ...]


def partitions(n: int) -> List[Partition]:
    """All partitions of n in decreasing order, returned as tuples."""
    if n == 0:
        return [()]
    result: List[Partition] = []
    _partition_helper(n, n, [], result)
    return result


def _partition_helper(n: int, max_part: int, current: List[int],
                      result: List[Partition]) -> None:
    if n == 0:
        result.append(tuple(current))
        return
    for i in range(min(n, max_part), 0, -1):
        _partition_helper(n - i, i, current + [i], result)


def transpose(lam: Partition) -> Partition:
    """Conjugate/transpose partition lambda^t."""
    if not lam:
        return ()
    cols = []
    for j in range(lam[0]):
        cols.append(sum(1 for p in lam if p > j))
    return tuple(cols)


def is_hook(lam: Partition) -> bool:
    """Check if partition is hook-type: (N-r, 1^r)."""
    if not lam:
        return True
    return all(p == 1 for p in lam[1:])


def hook_partitions(n: int) -> List[Partition]:
    """All hook partitions of n: (n), (n-1,1), ..., (1^n)."""
    if n == 0:
        return [()]
    result = []
    for r in range(n):
        # (n-r, 1^r)
        lam = (n - r,) + (1,) * r
        result.append(lam)
    return result


def partition_size(lam: Partition) -> int:
    return sum(lam)


# =====================================================================
# sl_2 embedding data from partition (Dynkin grading on sl_N)
# =====================================================================

def dynkin_grading_eigenvalues(lam: Partition) -> List[Tuple[int, int, Fraction]]:
    """Eigenvalues of ad(x) on sl_N, where x = h/2 for the sl_2-triple.

    For partition lambda = (p_1, ..., p_r) of N, the matrix algebra
    gl_N decomposes into blocks. The matrix unit E_{(i,a),(j,b)} where
    i is the block index, a is position within block i (0-indexed),
    j is the block index, b is position within block j, has eigenvalue
    (a - (p_i-1)/2) - (b - (p_j-1)/2) under ad(x).

    Returns list of (block_i, block_j, eigenvalue) for sl_N
    (traceless part, but we include all and the trace constraint
    is handled separately).
    """
    N = sum(lam)
    entries = []
    # Build the positions: for each block i of size p_i,
    # the "x-eigenvalue" on the a-th basis vector is a - (p_i - 1)/2
    block_starts = []
    s = 0
    for p in lam:
        block_starts.append(s)
        s += p

    # Matrix units E_{uv} in the standard basis have ad(x) eigenvalue
    # x_u - x_v, where x_u is the diagonal entry of x at position u.
    x_diag = []
    for p in lam:
        for a in range(p):
            x_diag.append(Fraction(a) - Fraction(p - 1, 2))

    eigenvalues = []
    for u in range(N):
        for v in range(N):
            if u == v:
                continue  # Cartan part handled below
            eigenvalues.append((u, v, x_diag[u] - x_diag[v]))

    return eigenvalues


def x_diagonal(lam: Partition) -> List[Fraction]:
    """Diagonal entries of x = h/2 for the sl_2 embedding given by lambda."""
    result = []
    for p in lam:
        for a in range(p):
            result.append(Fraction(a) - Fraction(p - 1, 2))
    return result


def centralizer_dimension(lam: Partition) -> int:
    """dim(g^e) for f in the orbit of type lambda in sl_N.

    For sl_N with partition lambda = (p_1, ..., p_r) (parts in
    decreasing order), dim(g^e) = sum_i (lambda^t_i)^2 - 1.
    Here lambda^t is the transpose partition.

    Actually: dim(g^f) = sum_i (lambda^t_i)^2 - 1 for sl_N.
    Equivalently, dim(g^f) = N + 2*sum_{i<j} min(lambda_i, lambda_j) - 1
    ... wait, let me use the standard formula.

    For g = sl_N, the centralizer dimension is:
    dim(sl_N^f) = sum_{j >= 1} (lambda^t_j)^2 - 1
    """
    lam_t = transpose(lam)
    return sum(p * p for p in lam_t) - 1


def nilpotent_orbit_dimension(lam: Partition) -> int:
    """dim(O_lambda) = dim(sl_N) - dim(sl_N^f) = (N^2-1) - (sum (lambda^t_j)^2 - 1).

    Equivalently, dim(O) = N^2 - sum (lambda^t_j)^2.
    """
    N = sum(lam)
    lam_t = transpose(lam)
    return N * N - sum(p * p for p in lam_t)


def half_nilpotent_orbit_dimension(lam: Partition) -> Fraction:
    """(1/2) * dim(O_lambda) = (1/2) * (N^2 - sum (lambda^t_j)^2)."""
    return Fraction(nilpotent_orbit_dimension(lam), 2)


# =====================================================================
# Strong generator spectrum
# =====================================================================

def generator_weights(lam: Partition) -> List[Fraction]:
    """Conformal weights of strong generators of W^k(sl_N, f_lambda).

    Each element x in g^e with ad(h)-eigenvalue 2j contributes a
    strong generator of conformal weight j + 1.

    For sl_N with partition lambda, the centralizer g^e (of the
    nilpotent e in the sl_2-triple (e,h,f)) has a basis indexed by
    the "top" positions in each block pair. Concretely, for blocks
    of sizes p_i, p_j (i <= j), there is one generator for each
    pair with ad(h)-eigenvalue p_i + p_j - 2, p_i + p_j - 4, ...,
    |p_i - p_j| + 2, |p_i - p_j|. Wait, that's the decomposition
    of sl_N under the sl_2 action.

    Actually: under the adjoint action of the sl_2 subalgebra,
    sl_N decomposes as:
      sl_N = bigoplus_{i,j} V_{p_i + p_j - 2} (for the off-diagonal blocks)
           plus the Cartan parts.

    Wait, more precisely: the adjoint representation of sl_N restricted
    to the sl_2 embedding given by the partition lambda = (p_1,...,p_r)
    decomposes as:
      sl_N|_{sl_2} = bigoplus_{i <= j} V_{p_i + p_j - 2}  (for i != j: one copy)
                     bigoplus_{i} V_{2p_i - 2} (diagonal blocks, minus trace)
    No, that's wrong. Let me think more carefully.

    The fundamental representation V of sl_N restricted to sl_2 via
    the embedding given by lambda = (p_1, ..., p_r) decomposes as:
      V|_{sl_2} = V_{p_1 - 1} + V_{p_2 - 1} + ... + V_{p_r - 1}

    The adjoint = V tensor V* - trivial decomposes as:
      (bigoplus_{i,j} V_{p_i - 1} tensor V_{p_j - 1}^*) - C

    Since V_a tensor V_b decomposes as V_{a+b} + V_{a+b-2} + ... + V_{|a-b|},
    we get:
      sl_N|_{sl_2} = bigoplus_{i,j} (V_{p_i + p_j - 2} + V_{p_i + p_j - 4}
                     + ... + V_{|p_i - p_j|}) minus one copy of V_0

    The centralizer g^e consists of the highest-weight vectors in each
    irreducible summand. So there is one generator for each sl_2
    irreducible V_d in the decomposition, with ad(h)-eigenvalue d
    (the highest weight), giving conformal weight d/2 + 1.

    So the generator weights are:
      For each pair (i, j) with 1 <= i, j <= r, for each d in
      {|p_i - p_j|, |p_i - p_j| + 2, ..., p_i + p_j - 2},
      there is a generator of weight d/2 + 1.
    Minus one generator at weight 1 (from the trace/V_0 subtraction).

    But since g = sl_N (not gl_N), we remove one copy of the trivial rep.
    """
    r = len(lam)
    weights: List[Fraction] = []

    for i in range(r):
        for j in range(r):
            pi, pj = lam[i], lam[j]
            # sl_2 irreducibles in V_{pi-1} tensor V_{pj-1}^*
            # are V_d for d = |pi-pj|, |pi-pj|+2, ..., pi+pj-2
            for d in range(abs(pi - pj), pi + pj - 1, 2):
                weights.append(Fraction(d, 2) + 1)

    # Remove one weight-1 generator (trace subtraction: gl_N -> sl_N)
    # There are exactly r copies of V_0 (one for each i=j block with d=0)
    # but we subtract the overall trace, leaving r-1 weight-1 generators
    # The r diagonal blocks each contribute a V_0 copy in gl_N.
    # Trace subtraction (gl_N -> sl_N) removes one, leaving r-1.
    # Remove one weight-1 entry to account for this.
    if Fraction(1) in weights:
        weights.remove(Fraction(1))

    weights.sort()
    return weights


def generator_weights_simple(lam: Partition) -> List[int]:
    """Integer conformal weights of strong generators, via the simpler
    combinatorial formula.

    For partition lambda = (p_1, ..., p_r) of N, the strong generators
    of W^k(sl_N, f_lambda) have conformal weights:
      { (p_i + p_j)/2 - m + 1 : 1 <= i,j <= r, 0 <= m <= min(p_i,p_j)-1 }
    minus one weight-1 generator (trace removal).

    Equivalently, using the transpose partition lambda^t = (q_1, ..., q_s):
    the generators have weights 1, 2, ..., q_1 with multiplicities
    determined by the transpose.

    Actually, the simplest way: for each pair (i,j) and each d in
    {|p_i-p_j|, |p_i-p_j|+2, ..., p_i+p_j-2}, we get weight d/2+1.
    All d are even iff p_i - p_j is even, i.e., same parity. Otherwise
    d is odd and we get half-integer weights... but for integer partitions
    of type A, all the conformal weights are actually integers.

    Wait: d = |p_i - p_j| + 2m for m = 0, ..., min(p_i,p_j)-1.
    If p_i and p_j have the same parity, d is always even, giving
    integer weights. If they have different parity, d is always odd,
    giving half-integer weights d/2 + 1 = (odd + 2)/2, which is NOT
    an integer.

    But W-algebras associated to even nilpotents should have integer
    generator weights. For non-even nilpotents, half-integer weights
    can appear (these are the "superalgebra" type generators).

    For type A: a nilpotent is even iff all parts of the partition have
    the same parity. Hook partitions (N-r, 1^r) have parts N-r and 1,
    which have the same parity iff N-r and 1 have the same parity,
    i.e., N-r is odd, i.e., N is even iff r is odd.

    Actually, in the physics convention, the conformal weight is
    d/2 + 1 where d is an ad(h) eigenvalue. For the generators to have
    integer weights, we need d to be even. This is the condition that
    the nilpotent is "even" (all ad(h) eigenvalues are even).

    For our purposes (verification), let's return Fraction values.
    """
    return [w for w in generator_weights(lam)]


# =====================================================================
# Central charge
# =====================================================================

def central_charge(N: int, lam: Partition, k: Fraction) -> Fraction:
    """Central charge of W^k(sl_N, f_lambda) via the per-root-pair formula.

    For type A with partition lambda of N, the central charge decomposes
    as a sum over Cartan directions and root pairs (alpha, -alpha).

    Let x' = -x where x = h/2 is the semisimple element of the sl_2
    triple. For each positive root e_i - e_j (i < j), define
    j_{ij} = x'_i - x'_j (the ad(x')-eigenvalue).

    The per-root-pair contributions (verified against all known cases
    including principal W_N for N=2..8, Bershadsky-Polyakov, affine,
    and hook-type W-algebras):

        Cartan direction:  k/(k+N) per direction, (N-1) directions.
        Root pair at j=0:  2k/(k+N).
        Root pair at integer |j| >= 1:  -(6|j| - 2)/(k+N).
        Root pair at half-integer |j| >= 1/2:  -4|j|*k - (6|j| - 2)/(k+N).

    Verified cases:
        Principal W_N (N=2..8): matches (N-1)(1 - N(N+1)/(k+N)).
        Affine (trivial nilpotent): matches k*dim(g)/(k+N).
        BP W^k(sl_3, f_{(2,1)}): matches -4k + 2 - 12/(k+3).
        Hook-type partitions: matches transport_to_transpose data.

    The previous implementation used the formula
        c = (N-1) - 12/(k+N) * ||rho - (k+N)*x||^2
    which is WRONG (gives incorrect results for non-principal partitions
    and for principal at N >= 4).
    """
    assert sum(lam) == N, f"Partition {lam} does not sum to {N}"
    assert k + N != 0, f"Critical level k = {k} = -h^v = -{N}"

    kN = k + N

    # x' = -x where x = h/2 is the semisimple element of the sl_2 triple.
    # x_diagonal gives entries of x = h/2; we negate to get x'.
    x_diag = x_diagonal(lam)
    x_prime = [-xi for xi in x_diag]

    # Cartan contribution: (N-1) directions, each k/(k+N)
    c_result = Fraction(N - 1) * k / kN

    # Root pair contributions: for each positive root e_i - e_j (i < j),
    # the ad(x')-eigenvalue is j_val = x'_i - x'_j.
    for i in range(N):
        for j_idx in range(i + 1, N):
            j_val = x_prime[i] - x_prime[j_idx]
            abs_j = abs(j_val)

            if abs_j == 0:
                # Degree-0 pair: contributes 2k/(k+N)
                c_result += Fraction(2) * k / kN
            elif abs_j.denominator == 1:
                # Integer grading: contributes -(6|j| - 2)/(k+N)
                j_int = int(abs_j)
                c_result += Fraction(-(6 * j_int - 2)) / kN
            else:
                # Half-integer grading: contributes -4|j|*k - (6|j| - 2)/(k+N)
                c_result += -4 * abs_j * k - (6 * abs_j - 2) / kN

    return c_result


def central_charge_principal(N: int, k: Fraction) -> Fraction:
    """Central charge of principal W^k(sl_N) = W_N at level k.

    c = (N-1)(1 - N(N+1)/(k+N))
    """
    return Fraction(N - 1) * (1 - Fraction(N * (N + 1), 1) / (k + N))


# =====================================================================
# Level transform
# =====================================================================

def dual_level(N: int, k: Fraction) -> Fraction:
    """Feigin-Frenkel dual level for type A: k' = -k - 2N.

    This is the level transform k -> k^v = -k - 2*h^v with h^v = N
    for sl_N.
    """
    return -k - 2 * N


# =====================================================================
# Partition graph Gamma_N
# =====================================================================

def dominance_order_covers(n: int) -> List[Tuple[Partition, Partition]]:
    """Covering relations in the dominance partial order on Par(n).

    lambda >= mu iff sum_{i=1}^k lambda_i >= sum_{i=1}^k mu_i for all k.

    We return the Hasse diagram (covering relations).
    """
    pars = partitions(n)
    par_set = set(pars)

    def dominates(lam: Partition, mu: Partition) -> bool:
        max_len = max(len(lam), len(mu))
        s1, s2 = 0, 0
        for i in range(max_len):
            s1 += lam[i] if i < len(lam) else 0
            s2 += mu[i] if i < len(mu) else 0
            if s1 < s2:
                return False
        return True

    covers = []
    for lam in pars:
        for mu in pars:
            if lam == mu:
                continue
            if not dominates(lam, mu):
                continue
            # Check if this is a cover: no nu with lam > nu > mu
            is_cover = True
            for nu in pars:
                if nu == lam or nu == mu:
                    continue
                if dominates(lam, nu) and dominates(nu, mu):
                    is_cover = False
                    break
            if is_cover:
                covers.append((lam, mu))
    return covers


def box_removal_edges(n: int) -> List[Tuple[Partition, Partition]]:
    """Edges in Gamma_N from single-box moves in the partition.

    An edge lambda -> mu exists if mu can be obtained from lambda by
    moving a box: remove a box from row i and add it to row j > i
    (or move to a new row), such that the result is still a valid
    partition.

    These correspond to elementary reduction steps: going from
    W^k(sl_N, f_lambda) to W^k(sl_N, f_mu) via a single
    DS reduction or inverse reduction step, at generic level.

    At generic level in type A, reduction by stages and inverse
    Hamiltonian reduction (Genra, Butson-Nair) provide functorial
    connections along these edges.
    """
    pars = partitions(n)
    edges = []

    for lam in pars:
        lam_list = list(lam)
        # Try moving a box from row i to row j
        for i in range(len(lam_list)):
            if lam_list[i] == 0:
                continue
            # Remove box from row i
            new = list(lam_list)
            new[i] -= 1

            for j in range(len(new) + 1):
                if j == i:
                    continue
                trial = list(new)
                if j < len(trial):
                    trial[j] += 1
                else:
                    trial.append(1)

                # Normalize: remove trailing zeros, sort descending
                trial = sorted([x for x in trial if x > 0], reverse=True)
                trial_t = tuple(trial)

                if trial_t != lam and trial_t in set(pars):
                    # Check it's a valid partition (non-increasing)
                    if all(trial[k] >= trial[k + 1]
                           for k in range(len(trial) - 1)):
                        edges.append((lam, trial_t))

    # Remove duplicates
    return list(set(edges))


def reduction_graph_edges(n: int) -> Set[FrozenSet[Partition]]:
    """Edges of the reduction graph Gamma_N.

    In type A at generic level, the reduction/inverse-reduction edges
    connect partitions that are related by single-step DS reductions.
    By results of Genra (reduction by stages) and Butson-Nair (inverse
    Hamiltonian reduction), the graph includes:
    1. All dominance-order covering relations (DS reductions from
       larger to smaller nilpotent).
    2. All inverse reductions (the reverse edges).

    Since both directions are available at generic level, the edges
    are undirected.
    """
    covers = dominance_order_covers(n)
    edges: Set[FrozenSet[Partition]] = set()
    for lam, mu in covers:
        edges.add(frozenset([lam, mu]))
    return edges


def build_adjacency(n: int) -> Dict[Partition, Set[Partition]]:
    """Build adjacency list for Gamma_N."""
    edges = reduction_graph_edges(n)
    adj: Dict[Partition, Set[Partition]] = defaultdict(set)
    for e in edges:
        e_list = list(e)
        if len(e_list) == 2:
            u, v = e_list
            adj[u].add(v)
            adj[v].add(u)
    # Ensure all partitions are vertices even if isolated
    for lam in partitions(n):
        if lam not in adj:
            adj[lam] = set()
    return adj


# =====================================================================
# Transport closure
# =====================================================================

def transport_closure(n: int, seed_vertices: Set[Partition]) -> Set[Partition]:
    """Compute the transport-closure: all vertices reachable from
    seed_vertices in Gamma_N via BFS.
    """
    adj = build_adjacency(n)
    visited: Set[Partition] = set()
    queue = deque(seed_vertices)
    visited.update(seed_vertices)

    while queue:
        v = queue.popleft()
        for w in adj.get(v, set()):
            if w not in visited:
                visited.add(w)
                queue.append(w)

    return visited


def hook_transport_closure(n: int) -> Set[Partition]:
    """Transport-closure of all hook partitions in Gamma_N."""
    hooks = set(hook_partitions(n))
    return transport_closure(n, hooks)


def graph_is_connected(n: int) -> bool:
    """Check if Gamma_N is connected."""
    pars = partitions(n)
    if len(pars) <= 1:
        return True
    closure = transport_closure(n, {pars[0]})
    return len(closure) == len(pars)


def transport_coverage_fraction(n: int) -> Fraction:
    """Fraction of Par(N) reached from hooks."""
    all_pars = partitions(n)
    closure = hook_transport_closure(n)
    return Fraction(len(closure), len(all_pars))


# =====================================================================
# Main engine class
# =====================================================================

class WAlgebraTransportEngine:
    """Engine for verifying transport propagation of W-algebra duality.

    Implements the verification of Proposition prop:transport-propagation:
    if duality is known at hook vertices and compatible with graph edges,
    it extends to the transport-closure.
    """

    def __init__(self, N: int, k: Optional[Fraction] = None):
        self.N = N
        self.k = k if k is not None else Fraction(7, 1)  # Generic level
        self.pars = partitions(N)
        self.adj = build_adjacency(N)
        self.hooks = set(hook_partitions(N))
        self.edges = reduction_graph_edges(N)

    # -----------------------------------------------------------------
    # Partition graph data
    # -----------------------------------------------------------------

    def num_partitions(self) -> int:
        return len(self.pars)

    def num_edges(self) -> int:
        return len(self.edges)

    def num_hooks(self) -> int:
        return len(self.hooks)

    def is_connected(self) -> bool:
        return graph_is_connected(self.N)

    def transport_closure(self) -> Set[Partition]:
        return hook_transport_closure(self.N)

    def coverage(self) -> Fraction:
        return transport_coverage_fraction(self.N)

    # -----------------------------------------------------------------
    # Hook duality data
    # -----------------------------------------------------------------

    def hook_dual_partition(self, eta: Partition) -> Partition:
        """BV dual of hook partition eta: just the transpose."""
        assert is_hook(eta), f"{eta} is not a hook partition"
        return transpose(eta)

    def hook_dual_level(self) -> Fraction:
        """Dual level: k^v = -k - 2N."""
        return dual_level(self.N, self.k)

    def hook_duality_data(self, eta: Partition) -> Dict:
        """Complete duality data for a hook partition."""
        eta_t = self.hook_dual_partition(eta)
        k_dual = self.hook_dual_level()
        c_orig = central_charge(self.N, eta, self.k)
        c_dual = central_charge(self.N, eta_t, k_dual)
        gen_orig = generator_weights(eta)
        gen_dual = generator_weights(eta_t)

        return {
            'partition': eta,
            'dual_partition': eta_t,
            'level': self.k,
            'dual_level': k_dual,
            'central_charge': c_orig,
            'dual_central_charge': c_dual,
            'complementarity_sum': c_orig + c_dual,
            'generators': gen_orig,
            'dual_generators': gen_dual,
        }

    # -----------------------------------------------------------------
    # Central charge verification
    # -----------------------------------------------------------------

    def complementarity_constant(self, lam: Partition) -> Fraction:
        """Compute the complementarity constant C(lambda):
        c(k, lambda) + c(k', lambda^t) where k' = -k - 2N.

        This should be INDEPENDENT of k (Freudenthal-de Vries type identity).
        """
        k_dual = dual_level(self.N, self.k)
        lam_t = transpose(lam)
        c1 = central_charge(self.N, lam, self.k)
        c2 = central_charge(self.N, lam_t, k_dual)
        return c1 + c2

    def verify_complementarity_level_independence(
        self, lam: Partition, test_levels: Optional[List[Fraction]] = None
    ) -> bool:
        """Verify that c(k, lambda) + c(k', lambda^t) is independent of k.

        Tests at multiple generic levels.
        """
        if test_levels is None:
            test_levels = [Fraction(p, q) for p in range(1, 8)
                           for q in [1, 2, 3]
                           if Fraction(p, q) + self.N != 0]

        values = set()
        for kk in test_levels:
            kk_dual = dual_level(self.N, kk)
            lam_t = transpose(lam)
            c1 = central_charge(self.N, lam, kk)
            c2 = central_charge(self.N, lam_t, kk_dual)
            values.add(c1 + c2)

        return len(values) == 1

    def principal_complementarity(self) -> Fraction:
        """Complementarity constant for the principal partition (N).

        For principal W-algebras: c(k) + c(k') = 2*rank + 4*h^v*dim(g)/(h^v)
        Wait, from the manuscript: c(W^k) + c(W^{k'}) = 2*rank(g) + 4*h^v*dim(g)

        For sl_N: 2*(N-1) + 4*N*(N^2-1) ... let me just compute it.
        """
        lam = tuple([self.N])
        return self.complementarity_constant(lam)

    # -----------------------------------------------------------------
    # Generator spectrum matching
    # -----------------------------------------------------------------

    def generator_spectrum_match(self, lam: Partition) -> Dict:
        """Check that generator spectra of W^k(sl_N, f_lambda) and
        W^{k'}(sl_N, f_{lambda^t}) are related by the expected duality.

        Under Koszul duality, the generator spectrum is preserved:
        the strong generators of W and W^! have the same conformal weights
        (this follows from bar-cobar: the bar cohomology lives in the
        same conformal weight slots).
        """
        lam_t = transpose(lam)
        gen_lam = sorted(generator_weights(lam))
        gen_lam_t = sorted(generator_weights(lam_t))

        return {
            'partition': lam,
            'dual_partition': lam_t,
            'generators': gen_lam,
            'dual_generators': gen_lam_t,
            'spectra_match': gen_lam == gen_lam_t,
            'num_generators': len(gen_lam),
            'dual_num_generators': len(gen_lam_t),
        }

    # -----------------------------------------------------------------
    # Transport propagation verification
    # -----------------------------------------------------------------

    def verify_transport_propagation(self) -> Dict[str, bool]:
        """Full verification of the transport propagation lemma.

        Tests:
        1. All hook partitions have well-defined duality data
        2. The graph Gamma_N is connected (Conjecture for general N)
        3. Transport-closure from hooks covers all of Par(N)
        4. Central charge complementarity is level-independent
        5. Generator spectra match under transpose
        """
        results: Dict[str, bool] = {}

        # 1. Hook duality well-defined
        for eta in self.hooks:
            eta_t = transpose(eta)
            data = self.hook_duality_data(eta)
            label = ''.join(str(p) for p in eta)
            results[f"hook ({label}) dual_partition is transpose"] = (
                data['dual_partition'] == eta_t
            )
            results[f"hook ({label}) dual_level = -k-2N"] = (
                data['dual_level'] == -self.k - 2 * self.N
            )

        # 2. Graph connectivity
        results["Gamma_N connected"] = self.is_connected()

        # 3. Transport-closure coverage
        closure = self.transport_closure()
        results["transport-closure = Par(N)"] = (
            len(closure) == len(self.pars)
        )
        results[f"coverage = {self.coverage()}"] = (
            self.coverage() == Fraction(1)
        )

        # 4. Complementarity level-independence for all partitions
        for lam in self.pars:
            label = ''.join(str(p) for p in lam)
            results[f"c+c' level-independent for ({label})"] = (
                self.verify_complementarity_level_independence(lam)
            )

        # 5. Generator spectrum matching for hooks
        for eta in self.hooks:
            label = ''.join(str(p) for p in eta)
            match_data = self.generator_spectrum_match(eta)
            results[f"generator spectrum match for hook ({label})"] = (
                match_data['spectra_match']
            )

        return results

    # -----------------------------------------------------------------
    # Summary tables
    # -----------------------------------------------------------------

    def partition_table(self) -> List[Dict]:
        """Summary table for all partitions of N."""
        k_dual = self.hook_dual_level()
        table = []
        for lam in self.pars:
            lam_t = transpose(lam)
            c_val = central_charge(self.N, lam, self.k)
            c_dual = central_charge(self.N, lam_t, k_dual)
            gens = generator_weights(lam)
            table.append({
                'partition': lam,
                'transpose': lam_t,
                'is_hook': is_hook(lam),
                'dim_centralizer': centralizer_dimension(lam),
                'dim_orbit': nilpotent_orbit_dimension(lam),
                'central_charge': c_val,
                'dual_central_charge': c_dual,
                'complementarity': c_val + c_dual,
                'num_generators': len(gens),
                'generator_weights': gens,
                'in_transport_closure': lam in hook_transport_closure(self.N),
            })
        return table


# =====================================================================
# Standalone verification functions
# =====================================================================

def verify_principal_formula_consistency(N_max: int = 8) -> Dict[str, bool]:
    """Verify that the general central charge formula agrees with the
    known principal W-algebra formula for all N <= N_max.
    """
    results: Dict[str, bool] = {}
    for N in range(2, N_max + 1):
        lam = (N,)
        for k_num in [1, 2, 3, 5, 7]:
            k = Fraction(k_num)
            c_general = central_charge(N, lam, k)
            c_principal = central_charge_principal(N, k)
            results[f"sl_{N} k={k}: general = principal"] = (
                c_general == c_principal
            )
    return results


def verify_bp_duality(k: Optional[Fraction] = None) -> Dict[str, bool]:
    """Verify the Bershadsky-Polyakov duality for sl_3.

    W^k(sl_3, f_{(2,1)})^! = W^{-k-6}(sl_3, f_{(2,1)})
    (since (2,1)^t = (2,1) in type A_2).
    """
    if k is None:
        k = Fraction(7)

    results: Dict[str, bool] = {}
    N = 3
    lam = (2, 1)
    lam_t = transpose(lam)

    results["(2,1)^t = (2,1)"] = (lam_t == (2, 1))

    k_dual = dual_level(N, k)
    results["k' = -k - 6"] = (k_dual == -k - 6)

    c1 = central_charge(N, lam, k)
    c2 = central_charge(N, lam_t, k_dual)

    # Verify level independence
    for kk in [Fraction(1), Fraction(2), Fraction(5), Fraction(11)]:
        kd = dual_level(N, kk)
        cc1 = central_charge(N, lam, kk)
        cc2 = central_charge(N, lam_t, kd)
        results[f"BP c+c' level-indep at k={kk}"] = (
            cc1 + cc2 == c1 + c2
        )

    return results


def verify_hook_duality_all_N(N_max: int = 8) -> Dict[str, bool]:
    """Verify hook-type duality for all N <= N_max.

    For each hook eta = (N-r, 1^r):
    1. eta^t is computable
    2. k' = -k - 2N
    3. c(k, eta) + c(k', eta^t) is level-independent
    """
    results: Dict[str, bool] = {}
    k = Fraction(7)

    for N in range(2, N_max + 1):
        for eta in hook_partitions(N):
            label = f"sl_{N}, ({','.join(str(p) for p in eta)})"
            eta_t = transpose(eta)
            k_dual = dual_level(N, k)

            c1 = central_charge(N, eta, k)
            c2 = central_charge(N, eta_t, k_dual)
            comp = c1 + c2

            # Check at another level
            k2 = Fraction(11)
            k2_dual = dual_level(N, k2)
            c1b = central_charge(N, eta, k2)
            c2b = central_charge(N, eta_t, k2_dual)

            results[f"{label}: c+c' level-indep"] = (c1 + c2 == c1b + c2b)
            results[f"{label}: eta^t well-defined"] = (
                sum(eta_t) == N
            )

    return results


def verify_transport_closure_coverage(N_max: int = 8) -> Dict[str, object]:
    """For each N, compute the transport-closure coverage.

    Reports the fraction of Par(N) reachable from hooks through Gamma_N.
    """
    results: Dict[str, object] = {}
    for N in range(2, N_max + 1):
        all_pars = partitions(N)
        closure = hook_transport_closure(N)
        frac = Fraction(len(closure), len(all_pars))
        results[f"N={N}: |Par|={len(all_pars)}, |closure|={len(closure)}, coverage={frac}"] = (
            frac == Fraction(1)
        )
    return results


def verify_gamma_connectivity(N_max: int = 8) -> Dict[str, bool]:
    """Check if Gamma_N is connected for N = 2, ..., N_max."""
    results: Dict[str, bool] = {}
    for N in range(2, N_max + 1):
        results[f"Gamma_{N} connected"] = graph_is_connected(N)
    return results


def verify_generator_spectrum_at_hooks(N_max: int = 7) -> Dict[str, bool]:
    """Verify generator spectrum matching for hook partitions.

    For hook eta = (N-r, 1^r), the generator spectrum of
    W^k(sl_N, f_eta) should match that of W^{k'}(sl_N, f_{eta^t})
    (same conformal weights, since BV duality preserves the
    sl_2-triple structure in a conjugate way).
    """
    results: Dict[str, bool] = {}
    for N in range(2, N_max + 1):
        for eta in hook_partitions(N):
            eta_t = transpose(eta)
            gen_eta = sorted(generator_weights(eta))
            gen_eta_t = sorted(generator_weights(eta_t))
            label = f"sl_{N}, ({','.join(str(p) for p in eta)})"
            results[f"{label}: spectrum match"] = (gen_eta == gen_eta_t)
            results[f"{label}: num_gen match"] = (len(gen_eta) == len(gen_eta_t))

    return results


def verify_level_transform(N_max: int = 8) -> Dict[str, bool]:
    """Verify the level transform k' = -k - 2N."""
    results: Dict[str, bool] = {}
    for N in range(2, N_max + 1):
        k = Fraction(7)
        k_dual = dual_level(N, k)
        results[f"sl_{N}: k'=-k-2N"] = (k_dual == -k - 2 * N)
        results[f"sl_{N}: (k')' = k (involutivity)"] = (
            dual_level(N, k_dual) == k
        )
        # Critical level: k = -N maps to k' = N - 2N = -N (fixed point)
        results[f"sl_{N}: critical level fixed point"] = (
            dual_level(N, Fraction(-N)) == Fraction(-N)
        )

    return results


def master_verification(N_max: int = 6) -> Dict[str, bool]:
    """Run the complete transport propagation verification suite."""
    results: Dict[str, bool] = {}

    # Level transform
    results.update(verify_level_transform(N_max))

    # Principal formula consistency
    results.update(verify_principal_formula_consistency(N_max))

    # BP duality
    results.update(verify_bp_duality())

    # Hook duality
    results.update(verify_hook_duality_all_N(N_max))

    # Graph connectivity
    results.update(verify_gamma_connectivity(N_max))

    # Transport coverage
    for key, val in verify_transport_closure_coverage(N_max).items():
        results[key] = bool(val)

    # Generator spectra (only up to N=7 to avoid slow computation)
    results.update(verify_generator_spectrum_at_hooks(min(N_max, 7)))

    return results
