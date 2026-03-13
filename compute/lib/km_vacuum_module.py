"""Kac-Moody vacuum module with exact mode matrices.

This module provides the truncated vacuum module V_k(g) for a simple Lie algebra g,
with exact J^a_n mode matrices. The primary use case is computing g-invariants in
each weight space, which are the surviving terms on the E_1 page of the PBW spectral
sequence for bar cohomology.

Key facts:
  - The vacuum module V_k(g) = Ind^{hat{g}}_{g[t] + CK} C, with K acting as k.
  - PBW basis: J^{a_1}_{-n_1} ... J^{a_r}_{-n_r} |0> with n_1 >= ... >= n_r >= 1,
    and a_i <= a_{i+1} when n_i = n_{i+1} (colored partitions in PBW order).
  - dim V_h = coefficient of q^h in prod_{n>=1} (1-q^n)^{-dim(g)}.
  - Commutation: [J^a_m, J^b_n] = f^c_{ab} J^c_{m+n} + k*kappa(a,b)*m*delta_{m+n,0}.
  - Vacuum: J^a_n |0> = 0 for n >= 0.
  - Zero modes J^a_0 act as the adjoint representation on each weight space.

CONVENTIONS:
  - sl_2 basis: e=0, h=1, f=2 (same as genus1_pbw_sl2.py)
  - Killing form: kappa(h,h) = 2, kappa(e,f) = kappa(f,e) = 1
  - Structure constants: [e,f] = h, [h,e] = 2e, [h,f] = -2f
  - State = tuple of (mode, gen_index) pairs in PBW order:
    primary sort mode descending, secondary sort gen_index ascending
"""

from __future__ import annotations

from math import comb
from typing import Dict, List, Tuple

from sympy import Matrix, Rational, Symbol, sympify, zeros


# A PBW state is a tuple of (mode, gen_index) pairs in normal order.
# Example: ((3, 0), (2, 1), (1, 0)) = J^0_{-3} J^1_{-2} J^0_{-1} |0>
State = Tuple[Tuple[int, int], ...]


# ---------------------------------------------------------------------------
# sl_2 data (shared with genus1_pbw_sl2.py)
# ---------------------------------------------------------------------------

SL2_BRACKET: Dict[Tuple[int, int], Dict[int, Rational]] = {
    (0, 2): {1: Rational(1)},    # [e, f] = h
    (2, 0): {1: Rational(-1)},   # [f, e] = -h
    (1, 0): {0: Rational(2)},    # [h, e] = 2e
    (0, 1): {0: Rational(-2)},   # [e, h] = -2e
    (1, 2): {2: Rational(-2)},   # [h, f] = -2f
    (2, 1): {2: Rational(2)},    # [f, h] = 2f
}

SL2_KILLING: Dict[Tuple[int, int], Rational] = {
    (0, 2): Rational(1),   # kappa(e, f) = 1
    (2, 0): Rational(1),   # kappa(f, e) = 1
    (1, 1): Rational(2),   # kappa(h, h) = 2
}


def sl2_data() -> Tuple[int, Dict, Dict]:
    """Return (dim_g, structure_constants, killing_form) for sl_2."""
    return 3, SL2_BRACKET, SL2_KILLING


# ---------------------------------------------------------------------------
# PBW basis generation
# ---------------------------------------------------------------------------

def km_pbw_basis(dim_g: int, weight: int) -> List[State]:
    """PBW basis for KM vacuum module at conformal weight.

    Returns list of colored partition states sorted in PBW order.
    Weight 0 gives [()] (vacuum state).
    """
    if weight == 0:
        return [()]
    if weight < 0:
        return []
    result: List[State] = []
    _generate_colored_partitions(dim_g, weight, weight, 0, (), result)
    return result


def _generate_colored_partitions(
    dim_g: int,
    remaining: int,
    max_mode: int,
    min_gen: int,
    current: State,
    result: List[State],
) -> None:
    """Recursively generate colored partitions in PBW order.

    Args:
        dim_g: number of generators
        remaining: remaining weight to distribute
        max_mode: maximum allowed mode for next factor
        min_gen: minimum gen index if next factor has mode == max_mode
        current: state built so far
        result: accumulator list
    """
    if remaining == 0:
        result.append(current)
        return
    for mode in range(min(max_mode, remaining), 0, -1):
        gen_start = min_gen if mode == max_mode else 0
        for gen in range(gen_start, dim_g):
            _generate_colored_partitions(
                dim_g, remaining - mode, mode, gen,
                current + ((mode, gen),), result,
            )


def vacuum_module_dims(dim_g: int, max_weight: int) -> List[int]:
    """Vacuum module dimensions at each weight via the character formula.

    dim V_h = coefficient of q^h in prod_{n>=1} (1-q^n)^{-dim_g}.
    """
    table = [0] * (max_weight + 1)
    table[0] = 1
    for n in range(1, max_weight + 1):
        # Multiply by 1/(1-q^n)^{dim_g} using binomial series
        for w in range(max_weight, n - 1, -1):
            for k in range(1, w // n + 1):
                binom = comb(k + dim_g - 1, dim_g - 1)
                if w - k * n >= 0:
                    table[w] += table[w - k * n] * binom
    return table


# ---------------------------------------------------------------------------
# KMVacuumModule class
# ---------------------------------------------------------------------------

class KMVacuumModule:
    """Truncated Kac-Moody vacuum module with exact J^a_n matrices.

    Models V_k(g) up to a given conformal weight, with the full
    affine Lie algebra commutation relations.
    """

    def __init__(
        self,
        dim_g: int,
        structure_constants: Dict[Tuple[int, int], Dict[int, Rational]],
        killing_form: Dict[Tuple[int, int], Rational],
        level=Symbol("k"),
        max_weight: int = 8,
    ):
        self.dim_g = dim_g
        self.structure_constants = structure_constants
        self.killing_form = killing_form
        self.level = sympify(level)
        self.max_weight = max_weight
        self.basis: Dict[int, List[State]] = {
            h: km_pbw_basis(dim_g, h) for h in range(max_weight + 1)
        }
        self._mode_cache: Dict[Tuple[int, int, int], Matrix] = {}
        self._casimir_cache: Dict[int, Matrix] = {}
        self._casimir_eigen_cache: Dict[int, Dict[Rational, int]] = {}
        self._invariant_dim_cache: Dict[int, int] = {}

    @classmethod
    def sl2(cls, level=Symbol("k"), max_weight: int = 8) -> "KMVacuumModule":
        """Create vacuum module for sl_2-hat at level k."""
        dim_g, sc, kf = sl2_data()
        return cls(dim_g, sc, kf, level=level, max_weight=max_weight)

    def basis_at_weight(self, weight: int) -> List[State]:
        """PBW basis at given conformal weight."""
        return self.basis.get(weight, [])

    def weight_dim(self, weight: int) -> int:
        """Dimension of the weight space."""
        return len(self.basis_at_weight(weight))

    def mode_matrix(self, gen_idx: int, mode: int, weight_source: int) -> Matrix:
        """Matrix of J^{gen_idx}_{mode}: V_h -> V_{h-mode} on the truncated module.

        Args:
            gen_idx: generator index (0 to dim_g-1)
            mode: mode number (positive = annihilation, negative = creation)
            weight_source: conformal weight of the source space

        Returns:
            Matrix with rows indexed by target basis, columns by source basis.
        """
        key = (gen_idx, mode, weight_source)
        if key in self._mode_cache:
            return self._mode_cache[key]

        weight_target = weight_source - mode
        source_basis = self.basis_at_weight(weight_source)
        target_basis = (
            self.basis_at_weight(weight_target)
            if 0 <= weight_target <= self.max_weight
            else []
        )

        mat = zeros(len(target_basis), len(source_basis))
        if not source_basis or not target_basis:
            self._mode_cache[key] = mat
            return mat

        target_index = {state: idx for idx, state in enumerate(target_basis)}
        for col, state in enumerate(source_basis):
            for result_state, coeff in self._mode_on_pbw(gen_idx, mode, state).items():
                row = target_index.get(result_state)
                if row is not None:
                    mat[row, col] += coeff

        self._mode_cache[key] = mat
        return mat

    def adjoint_action_matrix(self, gen_idx: int, weight: int) -> Matrix:
        """Matrix of ad(e_{gen_idx}) = J^{gen_idx}_0 on weight space V_h.

        The zero modes J^a_0 act as the adjoint representation of g
        on each weight space of the vacuum module.
        """
        return self.mode_matrix(gen_idx, 0, weight)

    # -------------------------------------------------------------------
    # Internal: mode action on PBW states
    # -------------------------------------------------------------------

    def _mode_on_pbw(
        self, gen_idx: int, mode: int, state: State
    ) -> Dict[State, object]:
        """Apply J^{gen_idx}_{mode} to a PBW state.

        For mode >= 0: annihilation/zero mode, commute right through state.
        For mode < 0: creation operator, insert in PBW order.
        """
        if not state:
            # Acting on vacuum |0>
            if mode >= 0:
                return {}  # J^a_n |0> = 0 for n >= 0
            return {((-mode, gen_idx),): Rational(1)}

        if mode < 0:
            # Creation: insert J^{gen_idx}_{mode} = J^{gen_idx}_{-|mode|} into PBW
            return self._insert_mode(gen_idx, -mode, state)

        # Annihilation or zero mode: commute past leftmost factor
        first_mode, first_gen = state[0]
        rest = state[1:]
        result: Dict[State, object] = {}

        # Term 1: commutator [J^{gen_idx}_{mode}, J^{first_gen}_{-first_mode}]
        # = sum_c f^c_{gen_idx, first_gen} J^c_{mode - first_mode}
        # + k * kappa(gen_idx, first_gen) * mode * delta_{mode, first_mode}
        bracket = self.structure_constants.get((gen_idx, first_gen), {})
        new_mode = mode - first_mode
        for c, coeff in bracket.items():
            for s, sc in self._mode_on_pbw(c, new_mode, rest).items():
                result[s] = result.get(s, Rational(0)) + coeff * sc

        # Central term: k * kappa(a, b) * m * delta_{m+n,0}
        # Here m = mode (annihilation), n = -first_mode, so m+n = mode - first_mode
        if mode == first_mode and mode > 0:
            kappa = self.killing_form.get((gen_idx, first_gen), Rational(0))
            if kappa != 0:
                central = self.level * kappa * Rational(mode)
                rest_state = rest if rest else ()
                result[rest_state] = result.get(rest_state, Rational(0)) + central

        # Term 2: J^{first_gen}_{-first_mode} * J^{gen_idx}_{mode}(rest)
        # = reinsert first_gen at first_mode into the result of mode acting on rest
        for s, sc in self._mode_on_pbw(gen_idx, mode, rest).items():
            for lifted, lc in self._insert_mode(first_gen, first_mode, s).items():
                result[lifted] = result.get(lifted, Rational(0)) + sc * lc

        return {s: c for s, c in result.items() if c != 0}

    def _insert_mode(
        self, gen_idx: int, mode_number: int, state: State
    ) -> Dict[State, object]:
        """Insert creation operator J^{gen_idx}_{-mode_number} into PBW state.

        Reorders using commutation relations to maintain PBW normal order.
        Returns dict {state: coefficient}.
        """
        if not state:
            return {((mode_number, gen_idx),): Rational(1)}

        first_mode, first_gen = state[0]
        rest = state[1:]

        # Check if already in PBW order:
        # (mode_number, gen_idx) comes first if mode_number > first_mode,
        # or mode_number == first_mode and gen_idx <= first_gen
        if mode_number > first_mode or (
            mode_number == first_mode and gen_idx <= first_gen
        ):
            return {((mode_number, gen_idx),) + state: Rational(1)}

        # Need to commute: use [J^a_{-m}, J^b_{-n}] = f^c_{ab} J^c_{-(m+n)}
        # (no central term since both modes are negative and -(m+n) < 0)
        result: Dict[State, object] = {}

        # Recursive: insert into rest, then re-insert first factor
        for s, sc in self._insert_mode(gen_idx, mode_number, rest).items():
            for lifted, lc in self._insert_mode(first_gen, first_mode, s).items():
                result[lifted] = result.get(lifted, Rational(0)) + sc * lc

        # Commutator: [J^{gen_idx}_{-mode_number}, J^{first_gen}_{-first_mode}]
        # = f^c_{gen_idx, first_gen} J^c_{-(mode_number + first_mode)}
        bracket = self.structure_constants.get((gen_idx, first_gen), {})
        combined_mode = mode_number + first_mode
        for c, coeff in bracket.items():
            for s, sc in self._insert_mode(c, combined_mode, rest).items():
                result[s] = result.get(s, Rational(0)) + coeff * sc

        return {s: c for s, c in result.items() if c != 0}


# ---------------------------------------------------------------------------
# Verification functions
# ---------------------------------------------------------------------------

# Expected vacuum module dims for sl_2: prod_{n>=1} (1-q^n)^{-3}
SL2_VACUUM_DIMS = [1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, 2640, 4599, 7868]


def verify_vacuum_dims(dim_g: int = 3, max_weight: int = 8) -> Dict[str, bool]:
    """Verify PBW basis dimensions match the character formula."""
    char_dims = vacuum_module_dims(dim_g, max_weight)
    results: Dict[str, bool] = {}
    for h in range(max_weight + 1):
        basis = km_pbw_basis(dim_g, h)
        expected = char_dims[h]
        results[f"dim V_{h} = {expected}"] = (len(basis) == expected)
    return results


def verify_zero_mode_commutation(max_weight: int = 6) -> Dict[str, bool]:
    """Verify [J^a_0, J^b_0] = f^c_{ab} J^c_0 on each weight space.

    The zero modes must form a representation of g.
    """
    module = KMVacuumModule.sl2(max_weight=max_weight)
    dim_g = module.dim_g
    results: Dict[str, bool] = {}

    for h in range(1, max_weight + 1):
        d = module.weight_dim(h)
        if d == 0:
            continue
        all_ok = True
        for a in range(dim_g):
            for b in range(dim_g):
                # [J^a_0, J^b_0] on V_h
                ja = module.adjoint_action_matrix(a, h)
                jb = module.adjoint_action_matrix(b, h)
                comm = ja * jb - jb * ja
                # Expected: f^c_{ab} J^c_0
                expected = zeros(d, d)
                bracket = module.structure_constants.get((a, b), {})
                for c, coeff in bracket.items():
                    expected += coeff * module.adjoint_action_matrix(c, h)
                if comm != expected:
                    all_ok = False
                    break
            if not all_ok:
                break
        results[f"[J^a_0, J^b_0] = f J^c_0 on V_{h}"] = all_ok
    return results


def verify_creation_annihilation(max_weight: int = 5) -> Dict[str, bool]:
    """Verify [J^a_m, J^b_{-n}] = f^c_{ab} J^c_{m-n} + k*kappa*m*delta on low weights.

    Tests the fundamental commutation relation by checking mode matrices.
    """
    module = KMVacuumModule.sl2(max_weight=max_weight + 2)
    dim_g = module.dim_g
    results: Dict[str, bool] = {}

    for h in range(1, min(max_weight + 1, 4)):
        d_h = module.weight_dim(h)
        if d_h == 0:
            continue
        for a in range(dim_g):
            # [J^a_1, J^a_{-1}] on V_h should equal:
            # f^c_{a,a} J^c_0 + k*kappa(a,a)*1
            # For sl_2: [e,e]=0, [h,h]=0, [f,f]=0, kappa(e,e)=0, kappa(f,f)=0
            # kappa(h,h)=2, so [J^h_1, J^h_{-1}] = 2k on V_h
            jm1 = module.mode_matrix(a, -1, h)       # V_h -> V_{h+1}
            j1 = module.mode_matrix(a, 1, h + 1)     # V_{h+1} -> V_h
            j1_jm1 = j1 * jm1

            j1_h = module.mode_matrix(a, 1, h)       # V_h -> V_{h-1}
            if h >= 1:
                jm1_up = module.mode_matrix(a, -1, h - 1)  # V_{h-1} -> V_h
                if jm1_up.rows > 0 and j1_h.rows > 0:
                    jm1_j1 = jm1_up * j1_h
                else:
                    jm1_j1 = zeros(d_h, d_h)
            else:
                jm1_j1 = zeros(d_h, d_h)

            comm = j1_jm1 - jm1_j1

            # Expected: bracket + central
            bracket = module.structure_constants.get((a, a), {})
            expected = zeros(d_h, d_h)
            for c, coeff in bracket.items():
                expected += coeff * module.adjoint_action_matrix(c, h)
            kappa_aa = module.killing_form.get((a, a), Rational(0))
            if kappa_aa != 0:
                from sympy import eye
                expected += module.level * kappa_aa * eye(d_h)

            results[f"[J^{a}_1, J^{a}_-1] on V_{h}"] = (comm == expected)

    return results


def invariant_dim_at_weight(module: KMVacuumModule, weight: int) -> int:
    """Dimension of g-invariants in weight-h vacuum module.

    Invariants = intersection of ker(J^a_0) for all a.
    """
    cached = module._invariant_dim_cache.get(weight)
    if cached is not None:
        return cached

    if weight == 0:
        module._invariant_dim_cache[weight] = 1
        return 1  # vacuum is always invariant

    d = module.weight_dim(weight)
    if d == 0:
        module._invariant_dim_cache[weight] = 0
        return 0

    if module.dim_g == 3:
        eigenvals = casimir_eigenvalues_at_weight(module, weight)
        multiplicity = int(eigenvals.get(Rational(0), 0))
        module._invariant_dim_cache[weight] = multiplicity
        return multiplicity

    # Stack all zero-mode matrices and find kernel
    mats = [module.adjoint_action_matrix(a, weight) for a in range(module.dim_g)]
    stacked = mats[0]
    for m in mats[1:]:
        stacked = stacked.col_join(m)

    kernel_dim = d - stacked.rank()
    module._invariant_dim_cache[weight] = kernel_dim
    return kernel_dim


def invariant_dims_through_weight(
    dim_g: int = 3, max_weight: int = 8, level=Symbol("k")
) -> List[int]:
    """Compute g-invariant dimensions at each weight in the vacuum module.

    For sl_2 at generic k, the sequence should be:
    1, 0, 1, 1, 3, 3, 8, 9, 19, ...
    matching adjoint_invariant_dim from spectral_sequence.py.
    """
    if dim_g == 3:
        sc, kf = SL2_BRACKET, SL2_KILLING
    else:
        raise ValueError(f"Only sl_2 (dim_g=3) supported, got dim_g={dim_g}")

    module = KMVacuumModule(dim_g, sc, kf, level=level, max_weight=max_weight)
    return [invariant_dim_at_weight(module, h) for h in range(max_weight + 1)]


# ---------------------------------------------------------------------------
# Casimir decomposition
# ---------------------------------------------------------------------------

def casimir_matrix_at_weight(module: KMVacuumModule, weight: int) -> Matrix:
    """Casimir C_2 of the g zero-mode action on V_h.

    For sl_2: C_2 = sum_{a,b} kappa^{ab} J^a_0 J^b_0
    = J^0_0 J^2_0 + J^2_0 J^0_0 + (1/2) J^1_0 J^1_0

    Eigenvalue on spin-j irrep: 2j(j+1) (with our normalization).
    """
    cached = module._casimir_cache.get(weight)
    if cached is not None:
        return cached

    d = module.weight_dim(weight)
    if d == 0:
        empty = zeros(0, 0)
        module._casimir_cache[weight] = empty
        return empty

    # Inverse Killing form for sl_2
    inv_killing = {
        (0, 2): Rational(1),
        (2, 0): Rational(1),
        (1, 1): Rational(1, 2),
    }

    C = zeros(d, d)
    for (a, b), coeff in inv_killing.items():
        ja = module.adjoint_action_matrix(a, weight)
        jb = module.adjoint_action_matrix(b, weight)
        C += coeff * ja * jb

    module._casimir_cache[weight] = C
    return C


def casimir_eigenvalues_at_weight(
    module: KMVacuumModule, weight: int
) -> Dict[Rational, int]:
    """Casimir eigenvalues on V_h with multiplicities.

    Returns {eigenvalue: multiplicity}.
    For sl_2, eigenvalue 2j(j+1) corresponds to spin-j irrep (dim 2j+1).
    """
    cached = module._casimir_eigen_cache.get(weight)
    if cached is not None:
        return cached

    C = casimir_matrix_at_weight(module, weight)
    if C.rows == 0:
        module._casimir_eigen_cache[weight] = {}
        return {}

    eigenvals = C.eigenvals()
    module._casimir_eigen_cache[weight] = eigenvals
    return eigenvals


def irrep_decomposition_at_weight(
    module: KMVacuumModule, weight: int
) -> Dict[int, int]:
    """Decompose V_h into sl_2 irreps.

    Returns {spin: copies} where spin j means the (2j+1)-dimensional irrep.
    Total dimension check: sum(copies * (2*spin+1)) == dim V_h.
    """
    eigenvals = casimir_eigenvalues_at_weight(module, weight)
    decomposition: Dict[int, int] = {}
    for ev, mult in eigenvals.items():
        # ev = 2*j*(j+1), solve for j
        j = _spin_from_eigenvalue(int(ev))
        copies = mult // (2 * j + 1)
        decomposition[j] = copies
    return decomposition


def _spin_from_eigenvalue(ev: int) -> int:
    """Recover spin j from Casimir eigenvalue 2j(j+1)."""
    for j in range(100):
        if 2 * j * (j + 1) == ev:
            return j
    raise ValueError(f"Cannot recover spin from eigenvalue {ev}")


def lowest_weight_dim_at_weight(module: KMVacuumModule, weight: int) -> int:
    """Dimension of lowest weight vectors (ker J^f_0 ∩ ker J^e_0) at weight h.

    For sl_2, lowest weight vectors are killed by both raising and lowering operators.
    Actually, for the standard convention e=raising, f=lowering:
    lowest weight = ker(J^f_0) = ker(J^2_0).
    But in our PBW convention, "lowest weight" means the bottom of an irrep.

    We use: new irreps starting at weight h = ker(J^a_1 for all a) intersected
    with V_h. This is dim(V_h) - rank(stacked J^a_1 matrices).
    """
    d = module.weight_dim(weight)
    if d == 0:
        return 0
    if weight == 0:
        return 1

    # Stack all J^a_1: V_h -> V_{h-1}
    mats = []
    for a in range(module.dim_g):
        mat = module.mode_matrix(a, 1, weight)
        if mat.rows > 0:
            mats.append(mat)

    if not mats:
        return d

    stacked = mats[0]
    for m in mats[1:]:
        stacked = stacked.col_join(m)

    return d - stacked.rank()


# ---------------------------------------------------------------------------
# Sugawara construction
# ---------------------------------------------------------------------------

def sugawara_l0_matrix(module: KMVacuumModule, weight: int) -> Matrix:
    """Sugawara L_0 on V_h.

    L_0 = (1/(2(k + h^v))) sum_{a,b} kappa^{ab} sum_{n>0} J^a_{-n} J^b_n
         + (1/(2(k + h^v))) sum_{a,b} kappa^{ab} J^a_0 J^b_0

    On V_h, L_0 should act as the scalar h (conformal weight).

    For sl_2: h^v = 2 (dual Coxeter number).
    """
    d = module.weight_dim(weight)
    if d == 0:
        return zeros(0, 0)

    k = module.level
    h_dual = Rational(2)  # for sl_2
    prefactor = Rational(1, 1) / (2 * (k + h_dual))

    inv_killing = {
        (0, 2): Rational(1),
        (2, 0): Rational(1),
        (1, 1): Rational(1, 2),
    }

    L0 = zeros(d, d)

    # Zero mode contribution: J^a_0 J^b_0
    for (a, b), coeff in inv_killing.items():
        ja0 = module.adjoint_action_matrix(a, weight)
        jb0 = module.adjoint_action_matrix(b, weight)
        L0 += coeff * ja0 * jb0

    # Positive mode contributions: 2 * sum_{n=1}^{weight} kappa^{ab} J^a_{-n} J^b_n
    # Factor of 2 from: sum_{m in Z} :J^a_m J^b_{-m}: = J^a_0 J^b_0 + 2*sum_{n>0} J^a_{-n} J^b_n
    # (using symmetry of kappa^{ab} to combine m>0 and m<0 terms)
    for n in range(1, weight + 1):
        target_weight = weight - n
        if target_weight < 0:
            break
        for (a, b), coeff in inv_killing.items():
            jb_n = module.mode_matrix(b, n, weight)        # V_h -> V_{h-n}
            ja_mn = module.mode_matrix(a, -n, target_weight)  # V_{h-n} -> V_h
            if ja_mn.rows > 0 and jb_n.rows > 0:
                L0 += Rational(2) * coeff * ja_mn * jb_n

    return prefactor * L0


def verify_sugawara_l0(max_weight: int = 5) -> Dict[str, bool]:
    """Verify Sugawara L_0 = h on V_h."""
    from sympy import eye, simplify

    k = Symbol("k")
    module = KMVacuumModule.sl2(level=k, max_weight=max_weight)
    results: Dict[str, bool] = {}

    for h in range(1, max_weight + 1):
        d = module.weight_dim(h)
        if d == 0:
            continue
        L0 = sugawara_l0_matrix(module, h)
        expected = Rational(h) * eye(d)
        # Simplify each entry (rational functions of k)
        diff = L0 - expected
        is_zero = all(
            simplify(diff[i, j]) == 0
            for i in range(d)
            for j in range(d)
        )
        results[f"L_0 = {h} on V_{h}"] = is_zero

    return results
