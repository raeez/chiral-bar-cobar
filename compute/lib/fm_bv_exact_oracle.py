"""Exact NBC/Orlik-Solomon oracle for local FM residue algebra.

This module is the proof-grade replacement for float/SVD coordinate
machinery when only the local configuration-space algebra is needed.
It works in the no-broken-circuit basis of the braid arrangement
OS^*(Conf_n(C)) and keeps all coefficients in ``fractions.Fraction``.

Conventions:
  - vertices are 1-indexed;
  - edges are unordered pairs ``(i, j)`` with ``i < j``;
  - edge order is lexicographic;
  - products are exterior products, then reduced to NBC normal form;
  - residues remove ``eta_ij`` with the Koszul sign from its wedge position
    and then merge labels ``i`` and ``j``.
"""

from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations
from typing import Dict, Iterable, List, Optional, Tuple


Edge = Tuple[int, int]
Monomial = Tuple[Edge, ...]
Vector = Dict[Monomial, Fraction]


def edge(i: int, j: int) -> Edge:
    """Canonical unordered edge."""
    if i == j:
        raise ValueError("OS edge requires distinct vertices")
    return (i, j) if i < j else (j, i)


def _all_edges(n: int) -> Tuple[Edge, ...]:
    return tuple((i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1))


def _edge_rank(n: int) -> Dict[Edge, int]:
    return {e: idx for idx, e in enumerate(_all_edges(n))}


def _canonicalize(n: int, edges: Iterable[Edge]) -> Tuple[int, Monomial]:
    """Return exterior sign and lexicographically sorted monomial."""
    ranks = _edge_rank(n)
    raw = [edge(*e) for e in edges]
    if len(set(raw)) != len(raw):
        return 0, ()
    inversions = 0
    raw_ranks = [ranks[e] for e in raw]
    for i in range(len(raw_ranks)):
        for j in range(i + 1, len(raw_ranks)):
            if raw_ranks[i] > raw_ranks[j]:
                inversions += 1
    sign = -1 if inversions % 2 else 1
    return sign, tuple(sorted(raw, key=lambda e: ranks[e]))


def _is_forest(vertices: int, monomial: Monomial) -> bool:
    parent = list(range(vertices + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in monomial:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
    return True


@lru_cache(maxsize=64)
def circuits(n: int) -> Tuple[Monomial, ...]:
    """All simple cycles of the complete graph K_n as sorted edge tuples."""
    ranks = _edge_rank(n)
    found = set()
    out: List[Monomial] = []
    vertices = tuple(range(1, n + 1))
    for length in range(3, n + 1):
        for verts in combinations(vertices, length):
            start = min(verts)
            rest = [v for v in verts if v != start]
            for perm in permutations(rest):
                path = (start,) + perm
                cycle = tuple(edge(path[i], path[(i + 1) % length]) for i in range(length))
                key = frozenset(cycle)
                if key in found:
                    continue
                found.add(key)
                out.append(tuple(sorted(key, key=lambda e: ranks[e])))
    return tuple(out)


def _broken_circuit(n: int, monomial: Monomial) -> Optional[Tuple[Monomial, Monomial]]:
    """Find a circuit C whose broken circuit C minus min(C) lies in monomial."""
    s = set(monomial)
    for c in circuits(n):
        broken = c[1:]
        if set(broken).issubset(s):
            return c, broken
    return None


def is_nbc(n: int, monomial: Monomial) -> bool:
    """True iff the monomial is an independent no-broken-circuit set."""
    sign, mon = _canonicalize(n, monomial)
    return sign != 0 and _is_forest(n, mon) and _broken_circuit(n, mon) is None


@lru_cache(maxsize=256)
def nbc_basis(n: int, degree: int) -> Tuple[Monomial, ...]:
    """NBC basis of OS^degree(Conf_n(C))."""
    if degree < 0 or degree >= n:
        return ()
    return tuple(
        mon for mon in combinations(_all_edges(n), degree)
        if is_nbc(n, mon)
    )


def os_dimension_exact(n: int, degree: int) -> int:
    """Exact OS dimension from the NBC basis."""
    if degree == 0:
        return 1
    return len(nbc_basis(n, degree))


def reduce_os_nbc(n: int, monomial: Iterable[Edge]) -> Vector:
    """Reduce one exterior monomial to the NBC basis."""
    sign, mon = _canonicalize(n, monomial)
    if sign == 0:
        return {}
    reduced = _reduce_sorted(n, mon)
    if sign == 1:
        return reduced
    return {m: -c for m, c in reduced.items()}


@lru_cache(maxsize=4096)
def _reduce_sorted(n: int, mon: Monomial) -> Vector:
    if not _is_forest(n, mon):
        return {}
    bc = _broken_circuit(n, mon)
    if bc is None:
        return {mon: Fraction(1)}

    c, broken = bc
    rest = tuple(e for e in mon if e not in set(broken))

    # OS relation for sorted circuit c:
    #   sum_i (-1)^i e_{c without c_i} = 0.
    # The i=0 term is the broken circuit.  Multiply by rest and solve
    # for the current monomial in canonical coordinates.
    s0, m0 = _canonicalize(n, list(broken) + list(rest))
    if m0 != mon or s0 == 0:
        raise RuntimeError("broken-circuit reduction lost its leading monomial")

    out: Vector = {}
    for idx in range(1, len(c)):
        candidate = [e for j, e in enumerate(c) if j != idx] + list(rest)
        si, mi = _canonicalize(n, candidate)
        if si == 0:
            continue
        coeff = Fraction(-((-1) ** idx) * si, s0)
        for red_mon, red_coeff in _reduce_sorted(n, mi).items():
            out[red_mon] = out.get(red_mon, Fraction(0)) + coeff * red_coeff
    return {m: q for m, q in out.items() if q}


def add_vectors(*vectors: Vector) -> Vector:
    out: Vector = {}
    for vec in vectors:
        for mon, coeff in vec.items():
            out[mon] = out.get(mon, Fraction(0)) + coeff
    return {m: q for m, q in out.items() if q}


def wedge(n: int, left: Vector, right: Vector) -> Vector:
    """Exterior product of two exact OS vectors, reduced to NBC form."""
    out: Vector = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            for mon, coeff in reduce_os_nbc(n, lm + rm).items():
                out[mon] = out.get(mon, Fraction(0)) + lc * rc * coeff
    return {m: q for m, q in out.items() if q}


def eta(n: int, i: int, j: int) -> Vector:
    """The OS generator eta_ij as an exact vector."""
    return {(edge(i, j),): Fraction(1)}


def arnold_triangle(n: int, i: int, j: int, k: int) -> Vector:
    """Arnold/OS circuit relation for the triangle on vertices i,j,k."""
    tri = tuple(sorted((edge(i, j), edge(i, k), edge(j, k)), key=lambda e: _edge_rank(n)[e]))
    terms: List[Vector] = []
    for omit in range(3):
        coeff = Fraction((-1) ** omit)
        mon = tuple(e for idx, e in enumerate(tri) if idx != omit)
        terms.append({mon: coeff})
    return add_vectors(*terms)


def reduce_vector(n: int, vector: Vector) -> Vector:
    """Reduce a linear combination of monomials to NBC normal form."""
    out: Vector = {}
    for mon, coeff in vector.items():
        for red_mon, red_coeff in reduce_os_nbc(n, mon).items():
            out[red_mon] = out.get(red_mon, Fraction(0)) + coeff * red_coeff
    return {m: q for m, q in out.items() if q}


def _relabel_after_collision(i: int, j: int, point: int) -> int:
    low, high = min(i, j), max(i, j)
    if point == high:
        return low
    if point > high:
        return point - 1
    return point


def residue(n: int, vector: Vector, i: int, j: int) -> Vector:
    """Exact Poincare residue Res_{D_ij}: OS^d(n) -> OS^{d-1}(n-1)."""
    p = edge(i, j)
    out: Vector = {}
    for mon, coeff in reduce_vector(n, vector).items():
        if p not in mon:
            continue
        pos = mon.index(p)
        sign = Fraction(-1 if pos % 2 else 1)
        remaining = [e for e in mon if e != p]
        relabeled: List[Edge] = []
        valid = True
        for a, b in remaining:
            ra = _relabel_after_collision(i, j, a)
            rb = _relabel_after_collision(i, j, b)
            if ra == rb:
                valid = False
                break
            relabeled.append(edge(ra, rb))
        if not valid:
            continue
        for red_mon, red_coeff in reduce_os_nbc(n - 1, relabeled).items():
            out[red_mon] = out.get(red_mon, Fraction(0)) + coeff * sign * red_coeff
    return {m: q for m, q in out.items() if q}


def double_residue(n: int, vector: Vector, first: Edge, second: Edge) -> Vector:
    """Iterated exact residue, reducing after each collision."""
    return residue(n - 1, residue(n, vector, *first), *second)


def second_order_deviation(n: int, a: Vector, b: Vector, c: Vector) -> Vector:
    """BV second-order deviation for the residue-free product model.

    In the exact OS algebra alone the product is associative and graded
    commutative.  This function returns the associator
    (a wedge b) wedge c - a wedge (b wedge c), which must vanish in NBC
    normal form.  It is a small exact oracle for tests that must not rely
    on floating-point coordinate representatives before adding analytic
    BV kernels.
    """
    left = wedge(n, wedge(n, a, b), c)
    right = wedge(n, a, wedge(n, b, c))
    return add_vectors(left, {m: -q for m, q in right.items()})
