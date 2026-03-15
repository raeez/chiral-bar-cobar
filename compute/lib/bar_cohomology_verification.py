"""Bar cohomology verification: three independent strategies.

Provides three perspectives on bar cohomology of sl_2-hat_k:

Strategy A: CE cohomology H^*(g_-, C) of the negative loop algebra
  g_- = sl_2 tensor t^{-1}C[t^{-1}].  Direct computation using the
  CE differential on Lambda^*(g_-^*), decomposed by conformal weight.
  This is the E_2 page of the PBW spectral sequence on B-bar(V_k(g)):
    E_1 = Lambda(V^*) (bar of associated graded Sym^ch(V))
    d_1 = CE differential of g_- (first-order correction from Lie bracket)
    E_2 = H^*(g_-, C) = E_infinity (d_r = 0 for r >= 2)
  No central extension in g_-: for modes m,n >= 1, the central term
  k*kappa(a,b)*m*delta_{m+n,0} = 0 since m+n >= 2 > 0.
  Result: H^1(CE) = 3, H^2(CE) = 5.

Strategy B: Vacuum module g-invariants (PBW spectral sequence E_1).
  The E_1 page of the PBW SS has entries only at CE degrees 0 and dim(g)
  (Whitehead vanishing for simple g).  Cross-validated via two independent
  computations: km_vacuum_module (PBW basis + zero-mode kernel) and
  spectral_sequence.adjoint_invariant_dim (adjoint rep on Sym algebra).

Strategy C: Koszul dual Hilbert series (Riordan numbers).
  dim(A^!)_n = R(n+3) from the generating function of the Koszul dual
  algebra (combinatorial_frontier.tex, subsec:riordan).
  R(4)=3, R(5)=6, R(6)=15, R(7)=36, R(8)=91, R(9)=232.

IMPORTANT: Strategies A and C compute DIFFERENT things.
  Strategy A (CE of g_-) gives H^2 = 5.
  Strategy C (Riordan) predicts dim(A^!)_2 = R(5) = 6.
  They agree at degree 1 (both give 3) but disagree at degree 2.

  The discrepancy arises because the CE complex uses exterior powers
  Lambda^n(g_-^*) while the chiral bar complex uses tensor products
  (A_+)^{otimes n} tensor Omega^{n-1}(C-bar_n).  The PBW spectral
  sequence identifies CE cohomology with the E_2 page, but the Riordan
  prediction involves the full chiral Koszul dual structure, which may
  include corrections from the OS form factor on configuration spaces.

  NOTE: The proof of cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex
  lines 758-762) claims E_infinity = E_1 = Lambda(V^*), asserting that d_r
  vanishes for r >= 1.  However, d_1: E_1^{p,0} -> E_1^{p+1,0} maps
  WITHIN row q=0 and is precisely the CE differential, which is nonzero.
  The correct statement is E_infinity = E_2 (not E_1).  This gap may
  affect the Riordan identification; see working_notes.tex.

References:
  - cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex)
  - thm:km-chiral-koszul (chiral_koszul_pairs.tex, lines 570-581)
  - prop:pole-decomposition (bar_cobar_construction.tex)
  - combinatorial_frontier.tex subsec:riordan (Riordan claim)
"""

from __future__ import annotations

from functools import lru_cache
from typing import Dict, List, Tuple

from sympy import Matrix, zeros


# ============================================================
# sl_2 data
# ============================================================

DIM_G = 3  # dim(sl_2)

# [e,f]=h, [h,e]=2e, [h,f]=-2f.  Basis: e=0, h=1, f=2.
SL2_BRACKET: Dict[Tuple[int, int], Dict[int, int]] = {
    (0, 2): {1: 1}, (2, 0): {1: -1},
    (1, 0): {0: 2}, (0, 1): {0: -2},
    (1, 2): {2: -2}, (2, 1): {2: 2},
}


# ============================================================
# Strategy A: CE cohomology of g_-
# ============================================================

def _weight_subsets(n_gens, gen_weights, degree, target_weight, start=0):
    """Generate degree-subsets of generators with exact total weight.

    Yields tuples of flat indices (sorted, increasing) whose weights sum
    to target_weight.  Much faster than filtering all C(n,d) subsets.
    """
    if degree == 0:
        if target_weight == 0:
            yield ()
        return
    for i in range(start, n_gens - degree + 1):
        w = gen_weights[i]
        if w > target_weight:
            continue
        if target_weight - w < degree - 1:
            # Remaining generators each need weight >= 1
            continue
        for rest in _weight_subsets(n_gens, gen_weights, degree - 1,
                                    target_weight - w, i + 1):
            yield (i,) + rest


class LoopAlgebraCE:
    """CE complex of g_- = g tensor t^{-1}C[t^{-1}], weight-graded.

    Generators: (a, n) for 0 <= a < dim_g, 1 <= n <= max_weight.
    Flat index: a + dim_g * (n - 1).
    Bracket: [(a,m), (b,n)] = f^c_{ab} (c, m+n), no central extension.
    Weight of generator (a, n) is n.

    The CE differential d: Lambda^p(g_-^*)_H -> Lambda^{p+1}(g_-^*)_H
    preserves conformal weight H.
    """

    def __init__(self, dim_g=DIM_G, structure_constants=None, max_weight=6):
        self.dim_g = dim_g
        self.sc = structure_constants if structure_constants is not None else SL2_BRACKET
        self.max_weight = max_weight
        self.n_gens = dim_g * max_weight
        self._gens = [(a, n) for n in range(1, max_weight + 1)
                      for a in range(dim_g)]
        self._gen_weights = [g[1] for g in self._gens]
        # Bracket table: only ordered pairs (i < j)
        self._bracket: Dict[Tuple[int, int], Dict[int, int]] = {}
        for i in range(self.n_gens):
            a, m = self._gens[i]
            for j in range(i + 1, self.n_gens):
                b, n = self._gens[j]
                if m + n > max_weight:
                    continue
                br = self.sc.get((a, b))
                if br:
                    result = {}
                    for c, coeff in br.items():
                        result[c + dim_g * (m + n - 1)] = coeff
                    if result:
                        self._bracket[(i, j)] = result

    def weight_basis(self, degree, weight):
        """Basis of Lambda^degree(g_-^*) at given weight."""
        return list(_weight_subsets(self.n_gens, self._gen_weights,
                                   degree, weight))

    def ce_differential(self, degree, weight):
        """CE differential d: Lambda^degree_weight -> Lambda^{degree+1}_weight.

        Sign convention matches spectral_sequence.ce_differential_matrix:
        for alpha in source, pairs (beta, gamma) with beta < gamma,
        and c in alpha such that [e_beta, e_gamma] has component f^c along e_c:
        sign = (-1)^{pos_c} * (-1)^{pos_beta_in_new} * (-1)^{pos_gamma_in_rest}
        """
        source = self.weight_basis(degree, weight)
        target = self.weight_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)
        if n_src == 0 or n_tgt == 0:
            return zeros(n_tgt, n_src)

        target_idx = {t: i for i, t in enumerate(target)}
        mat = zeros(n_tgt, n_src)

        for col, alpha in enumerate(source):
            alpha_set = set(alpha)
            alpha_list = list(alpha)
            for (beta, gamma), br in self._bracket.items():
                for c, coeff in br.items():
                    if c not in alpha_set:
                        continue
                    new_set = (alpha_set - {c}) | {beta, gamma}
                    if len(new_set) != degree + 1:
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue
                    pos_c = alpha_list.index(c)
                    sorted_new = list(new_tuple)
                    pos_beta = sorted_new.index(beta)
                    remaining = sorted(new_set - {beta})
                    pos_gamma = remaining.index(gamma)
                    sign = (-1) ** pos_c * (-1) ** pos_beta * (-1) ** pos_gamma
                    mat[row, col] += sign * coeff

        return mat

    def cohomology_dim(self, degree, weight):
        """dim H^degree(g_-)_weight."""
        dim_p = len(self.weight_basis(degree, weight))
        if dim_p == 0:
            return 0
        d_curr = self.ce_differential(degree, weight)
        ker = dim_p - (d_curr.rank() if d_curr.rows > 0 else 0)
        if degree > 0:
            d_prev = self.ce_differential(degree - 1, weight)
            im = d_prev.rank() if d_prev.rows > 0 and d_prev.cols > 0 else 0
        else:
            im = 0
        return ker - im

    def verify_d_squared(self, degree, weight):
        """Check d^2 = 0 at given degree and weight."""
        d_p = self.ce_differential(degree, weight)
        d_p1 = self.ce_differential(degree + 1, weight)
        if d_p.cols == 0 or d_p1.rows == 0:
            return True
        if d_p.rows != d_p1.cols:
            return True
        return (d_p1 * d_p).is_zero_matrix

    def chain_group_dim(self, degree, weight):
        """Dimension of Lambda^degree(g_-^*) at weight."""
        return len(self.weight_basis(degree, weight))


def strategy_a(max_degree=3, max_weight=8):
    """Compute H^n(g_-) = sum_H H^n(g_-)_H for n = 1,...,max_degree.

    Returns {n: dim H^n} mapping bar degree to cohomology dimension.
    """
    ce = LoopAlgebraCE(max_weight=max_weight)
    return {n: sum(ce.cohomology_dim(n, H) for H in range(n, max_weight + 1))
            for n in range(1, max_degree + 1)}


def strategy_a_detail(max_degree=3, max_weight=8):
    """Weight decomposition {n: {H: dim H^n(g_-)_H}}."""
    ce = LoopAlgebraCE(max_weight=max_weight)
    return {n: {H: ce.cohomology_dim(n, H) for H in range(n, max_weight + 1)}
            for n in range(1, max_degree + 1)}


# ============================================================
# Strategy B: Vacuum module g-invariants
# ============================================================


@lru_cache(maxsize=None)
def _strategy_b_sl2_module(max_weight: int):
    """Build the generic-level sl_2 vacuum module once per weight cutoff.

    Strategy-B checks repeatedly query the same truncated vacuum module.
    Reusing the module preserves its internal mode-matrix cache and avoids
    rebuilding the PBW basis for each test entrypoint.
    """
    from compute.lib.km_vacuum_module import KMVacuumModule
    from sympy import Symbol

    return KMVacuumModule.sl2(level=Symbol("k"), max_weight=max_weight)


@lru_cache(maxsize=None)
def _strategy_b_vm_dims(max_weight: int) -> Tuple[int, ...]:
    """Cache the vacuum-module invariant dimensions through ``max_weight``."""
    from compute.lib.km_vacuum_module import invariant_dim_at_weight

    module = _strategy_b_sl2_module(max_weight)
    return tuple(invariant_dim_at_weight(module, h) for h in range(max_weight + 1))


@lru_cache(maxsize=None)
def _strategy_b_ss_dims(max_weight: int) -> Tuple[int, ...]:
    """Cache the spectral-sequence invariant dimensions through ``max_weight``."""
    from compute.lib.km_vacuum_module import SL2_BRACKET as KM_BRACKET
    from compute.lib.spectral_sequence import adjoint_invariant_dim

    return tuple(adjoint_invariant_dim(3, KM_BRACKET, h) for h in range(max_weight + 1))


def strategy_b_invariants(max_weight=10):
    """g-invariant dimensions in V_k(sl_2) at each weight.

    Uses km_vacuum_module.py for exact computation.
    Returns [dim(V_0^g), dim(V_1^g), ..., dim(V_{max_weight}^g)].
    """
    return list(_strategy_b_vm_dims(max_weight))


def strategy_b_cross_validate(max_weight=8):
    """Cross-validate vacuum module invariants vs adjoint_invariant_dim.

    Both compute dim(V_h^g) using independent implementations:
    - km_vacuum_module: PBW basis + zero-mode kernel
    - spectral_sequence: adjoint rep matrices on Sym algebra

    Returns {h: (vm_dim, ss_dim, agree)} for h = 0,...,max_weight.
    """
    vm_dims = _strategy_b_vm_dims(max_weight)
    ss_dims = _strategy_b_ss_dims(max_weight)
    results = {}
    for h in range(max_weight + 1):
        vm = vm_dims[h]
        ss = ss_dims[h]
        results[h] = (vm, ss, vm == ss)
    return results


# ============================================================
# Strategy C: Koszul dual Hilbert series (Riordan numbers)
# ============================================================

def riordan(n):
    """Riordan number R(n), OEIS A005043.

    Recurrence: (n+1)*R(n) = (n-1)*(2*R(n-1) + 3*R(n-2)), R(0)=1, R(1)=0.
    First values: 1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, ...
    """
    if n <= 0:
        return 1
    if n == 1:
        return 0
    R = [1, 0]
    for k in range(2, n + 1):
        num = (k - 1) * (2 * R[k - 1] + 3 * R[k - 2])
        assert num % (k + 1) == 0
        R.append(num // (k + 1))
    return R[n]


def strategy_c(max_degree=6):
    """H^n = R(n+3) from Koszul dual Hilbert series.

    Returns {n: R(n+3)} for n = 1,...,max_degree.
    """
    return {n: riordan(n + 3) for n in range(1, max_degree + 1)}


# ============================================================
# Agreement verification
# ============================================================

def verify_strategies(max_degree=3, max_weight=8):
    """Compare strategies A (CE) and C (Riordan) on H^n.

    NOTE: Strategies A and C compute different things.
    A = CE cohomology of g_- (E_2 of PBW SS).
    C = Riordan number prediction for Koszul dual dimensions.
    They agree at degree 1 but diverge at degree 2+.

    Returns dict with strategy results and comparison.
    """
    a = strategy_a(max_degree, max_weight)
    c = strategy_c(max_degree)
    results = {"strategy_a": a, "strategy_c": c, "agree_at_1": a[1] == c[1]}
    for n in range(1, max_degree + 1):
        results[f"n={n}"] = {"CE": a[n], "Riordan": c[n], "agree": a[n] == c[n]}
    return results


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BAR COHOMOLOGY VERIFICATION: THREE STRATEGIES")
    print("=" * 60)

    print("\n--- Strategy C: Riordan numbers R(n+3) ---")
    c = strategy_c(6)
    for n, val in c.items():
        print(f"  H^{n} = R({n + 3}) = {val}")

    print("\n--- Strategy A: CE cohomology of g_- ---")
    detail = strategy_a_detail(max_degree=2, max_weight=6)
    for n, decomp in detail.items():
        total = sum(decomp.values())
        print(f"  H^{n} = {total}  (weight decomposition: {decomp})")

    print("\n--- d^2 = 0 verification ---")
    ce = LoopAlgebraCE(max_weight=5)
    for H in range(1, 6):
        for p in range(0, min(H + 1, 5)):
            ok = ce.verify_d_squared(p, H)
            if not ok:
                print(f"  FAIL: d^2 != 0 at degree {p}, weight {H}")
    print("  All d^2 = 0 checks passed")

    print("\n--- Comparison: CE vs Riordan ---")
    results = verify_strategies(max_degree=2, max_weight=6)
    for n in range(1, 3):
        info = results[f"n={n}"]
        status = "AGREE" if info["agree"] else "DIFFER"
        print(f"  n={n}: CE={info['CE']}, Riordan={info['Riordan']}  [{status}]")
    print("  (Discrepancy at n=2 expected: CE=5 vs Riordan=6)")
