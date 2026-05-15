"""Exact NBC Orlik-Solomon algebra for Conf_n(C).

This module is the rational oracle for the type-A braid arrangement.  It
uses the no-broken-circuit basis and exact SymPy rational linear algebra.
The NumPy-facing ``os_algebra`` module may convert these matrices to floats,
but the reduction and residue decisions live here.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations
from typing import Dict, Iterable, List, Tuple

import numpy as np
from sympy import Matrix, Rational


Pair = Tuple[int, int]
Monomial = Tuple[Pair, ...]


def make_pair(i: int, j: int) -> Pair:
    return (min(i, j), max(i, j))


def all_pairs(n: int) -> List[Pair]:
    return [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]


def monomial_basis(n: int, k: int) -> List[Monomial]:
    if k < 0:
        return []
    if k == 0:
        return [()]
    return [tuple(combo) for combo in combinations(all_pairs(n), k)]


def _perm_sign(items: List[Pair], target: List[Pair]) -> int:
    pos = {p: i for i, p in enumerate(target)}
    perm = [pos[p] for p in items]
    inversions = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inversions += int(perm[i] > perm[j])
    return -1 if inversions % 2 else 1


def _simple_cycles(n: int) -> List[Tuple[Pair, ...]]:
    cycles = []
    vertices = list(range(1, n + 1))
    for length in range(3, n + 1):
        for subset in combinations(vertices, length):
            v0 = subset[0]
            seen = set()
            for perm in permutations(subset[1:]):
                path = [v0] + list(perm)
                edges = tuple(sorted(make_pair(path[i], path[(i + 1) % length])
                                     for i in range(length)))
                key = frozenset(edges)
                if key not in seen:
                    seen.add(key)
                    cycles.append(edges)
    return cycles


@lru_cache(maxsize=128)
def simple_cycles(n: int) -> Tuple[Monomial, ...]:
    return tuple(_simple_cycles(n))


def is_nbc(monomial: Monomial, n: int) -> bool:
    """Return whether a monomial is no-broken-circuit for lex edge order."""
    edge_set = set(monomial)
    for cycle in simple_cycles(n):
        ordered = sorted(cycle)
        broken = set(ordered[1:])
        if broken.issubset(edge_set):
            return False
    return True


@lru_cache(maxsize=128)
def nbc_basis(n: int, k: int) -> Tuple[Monomial, ...]:
    return tuple(m for m in monomial_basis(n, k) if is_nbc(m, n))


def _circuit_boundary(cycle: Monomial, degree_mons: List[Monomial],
                      mon_idx: Dict[Monomial, int]) -> List[Rational]:
    row = [Rational(0) for _ in degree_mons]
    edges = sorted(cycle)
    for omit in range(len(edges)):
        remaining = tuple(edges[i] for i in range(len(edges)) if i != omit)
        if remaining in mon_idx:
            row[mon_idx[remaining]] += Rational((-1) ** omit)
    return row


def _relation_rows(n: int, k: int, mons: List[Monomial]) -> List[List[Rational]]:
    if k <= 0:
        return []
    mon_idx = {m: i for i, m in enumerate(mons)}
    rows: List[List[Rational]] = []

    for cycle in simple_cycles(n):
        m = len(cycle) - 1
        if m > k:
            continue
        m_mons = monomial_basis(n, m)
        m_idx = {mm: i for i, mm in enumerate(m_mons)}
        boundary = _circuit_boundary(cycle, m_mons, m_idx)

        complement_degree = k - m
        complements: Iterable[Monomial]
        if complement_degree == 0:
            complements = [()]
        else:
            complements = combinations(all_pairs(n), complement_degree)

        for complement in complements:
            comp_set = set(complement)
            row = [Rational(0) for _ in mons]
            for idx, coeff in enumerate(boundary):
                if coeff == 0:
                    continue
                term = m_mons[idx]
                if set(term) & comp_set:
                    continue
                combined = list(term) + list(complement)
                ordered = tuple(sorted(combined))
                if len(set(combined)) != len(combined):
                    continue
                if ordered not in mon_idx:
                    continue
                row[mon_idx[ordered]] += coeff * _perm_sign(combined, list(ordered))
            if any(x != 0 for x in row):
                rows.append(row)
    return rows


@lru_cache(maxsize=128)
def _reduction_data(n: int, k: int):
    mons = monomial_basis(n, k)
    nbc = list(nbc_basis(n, k))
    non_nbc = [m for m in mons if m not in set(nbc)]
    ordered = non_nbc + nbc
    ordered_idx = {m: i for i, m in enumerate(ordered)}
    nbc_idx = {m: i for i, m in enumerate(nbc)}

    if not mons:
        return mons, nbc, {}, []

    rows_native = _relation_rows(n, k, mons)
    if rows_native:
        native_idx = {m: i for i, m in enumerate(mons)}
        rows = [
            [row[native_idx[m]] for m in ordered]
            for row in rows_native
        ]
        rref, pivots = Matrix(rows).rref()
        rref_rows = []
        for r, pivot in enumerate(pivots):
            rref_rows.append((pivot, [Rational(rref[r, c]) for c in range(len(ordered))]))
    else:
        rref_rows = []

    return mons, nbc, ordered_idx, rref_rows


def reduce_to_nbc(n: int, k: int, element: Dict[Monomial, object]) -> Dict[Monomial, Rational]:
    """Reduce an exact monomial-coordinate element to the NBC basis."""
    mons, nbc, ordered_idx, rref_rows = _reduction_data(n, k)
    if not mons:
        return {}
    nbc_set = set(nbc)
    coeffs = {m: Rational(0) for m in nbc}

    for mon, coeff in element.items():
        if coeff == 0:
            continue
        if mon not in ordered_idx:
            raise ValueError(f"Monomial {mon} is not a degree-{k} monomial on Conf_{n}")
        q = Rational(coeff)
        if mon in nbc_set:
            coeffs[mon] += q
            continue
        col = ordered_idx[mon]
        pivot_row = None
        for pivot, row in rref_rows:
            if pivot == col:
                pivot_row = row
                break
        if pivot_row is None:
            raise ValueError(f"No exact OS reduction row for non-NBC monomial {mon}")
        for basis_mon in nbc:
            a = pivot_row[ordered_idx[basis_mon]]
            if a:
                coeffs[basis_mon] -= q * a

    return {m: c for m, c in coeffs.items() if c != 0}


def wedge(n: int, left: Dict[Monomial, object], right: Dict[Monomial, object]) -> Dict[Monomial, Rational]:
    """Exact wedge product followed by NBC reduction."""
    raw: Dict[Monomial, Rational] = {}
    degree = None
    for lm, lc in left.items():
        for rm, rc in right.items():
            combined = list(lm) + list(rm)
            if len(set(combined)) != len(combined):
                continue
            ordered = tuple(sorted(combined))
            degree = len(ordered)
            raw[ordered] = raw.get(ordered, Rational(0)) + Rational(lc) * Rational(rc) * _perm_sign(combined, list(ordered))
    if degree is None:
        return {}
    return reduce_to_nbc(n, degree, raw)


def edge(i: int, j: int) -> Dict[Monomial, Rational]:
    return {(make_pair(i, j),): Rational(1)}


def residue(n: int, k: int, i: int, j: int,
            element: Dict[Monomial, object]) -> Dict[Monomial, Rational]:
    """Exact Poincare residue Res_{ij}: OS^k(n) -> OS^{k-1}(n-1)."""
    p = make_pair(i, j)
    i_min, i_max = p

    def relabel(x: int) -> int:
        if x == i_max:
            return i_min
        if x > i_max:
            return x - 1
        return x

    raw: Dict[Monomial, Rational] = {}
    for mon, coeff in element.items():
        if p not in mon:
            continue
        pos = list(mon).index(p)
        sign = Rational((-1) ** pos)
        remaining = [e for e in mon if e != p]
        relabeled = []
        valid = True
        for a, b in remaining:
            ra, rb = relabel(a), relabel(b)
            if ra == rb:
                valid = False
                break
            relabeled.append(make_pair(ra, rb))
        if not valid or len(set(relabeled)) != len(relabeled):
            continue
        ordered = tuple(sorted(relabeled))
        raw[ordered] = raw.get(ordered, Rational(0)) + Rational(coeff) * sign * _perm_sign(relabeled, list(ordered))
    return reduce_to_nbc(n - 1, k - 1, raw)


def basis_matrix_numpy(n: int, k: int) -> Tuple[List[Monomial], np.ndarray]:
    """Return all monomials and NBC basis rows as a NumPy view."""
    mons = monomial_basis(n, k)
    idx = {m: i for i, m in enumerate(mons)}
    basis = list(nbc_basis(n, k))
    mat = np.zeros((len(basis), len(mons)), dtype=float)
    for r, mon in enumerate(basis):
        mat[r, idx[mon]] = 1.0
    return mons, mat


def residue_matrix_exact(n: int, k: int, i: int, j: int) -> Matrix:
    """Matrix of the exact residue in NBC bases."""
    src = list(nbc_basis(n, k))
    tgt = list(nbc_basis(n - 1, k - 1))
    tgt_idx = {m: r for r, m in enumerate(tgt)}
    mat = [[Rational(0) for _ in src] for _ in tgt]
    for c, mon in enumerate(src):
        image = residue(n, k, i, j, {mon: Rational(1)})
        for target_mon, coeff in image.items():
            mat[tgt_idx[target_mon]][c] = coeff
    return Matrix(mat)


def residue_matrix_numpy(n: int, k: int, i: int, j: int) -> np.ndarray:
    return np.array(residue_matrix_exact(n, k, i, j).tolist(), dtype=float)


def arnold_triangle_relation(a: int, b: int, c: int) -> Dict[Monomial, Rational]:
    """The degree-two Arnold relation on {a,b,c}, reduced to NBC form."""
    edges = sorted([make_pair(a, b), make_pair(a, c), make_pair(b, c)])
    raw: Dict[Monomial, Rational] = {}
    for omit in range(3):
        mon = tuple(edges[i] for i in range(3) if i != omit)
        raw[mon] = raw.get(mon, Rational(0)) + Rational((-1) ** omit)
    n = max(a, b, c)
    return reduce_to_nbc(n, 2, raw)


def verify_exact_oracle(max_n: int = 6) -> Dict[str, bool]:
    results: Dict[str, bool] = {}
    for n in range(2, max_n + 1):
        for k in range(n):
            results[f"NBC dim OS^{k}({n})"] = len(nbc_basis(n, k)) == _poincare_dim(n, k)
    results["Arnold triangle 123 reduces to zero"] = arnold_triangle_relation(1, 2, 3) == {}
    R = residue_matrix_exact(3, 2, 1, 2)
    results["Res_12 exact shape"] = R.shape == (1, 2)
    results["Res_12 exact nonzero"] = any(x != 0 for x in R)
    return results


def _poincare_dim(n: int, k: int) -> int:
    if k < 0 or k >= n:
        return 0
    coeffs = [1]
    for i in range(1, n):
        nxt = [0] * (len(coeffs) + 1)
        for j, coeff in enumerate(coeffs):
            nxt[j] += coeff
            nxt[j + 1] += i * coeff
        coeffs = nxt
    return coeffs[k]
