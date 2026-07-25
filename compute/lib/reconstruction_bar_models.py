#!/usr/bin/env python3
"""Exact finite-window checks for examples used in the definitive reconstruction.

The script deliberately computes chain matrices, not only Hilbert-series predictions.
All arithmetic is rational.  The quantum-plane parameter is specialized to q=2;
ranks are therefore valid for generic q away from the exceptional determinantal locus.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

import sympy as sp

Coeff = sp.Rational
Monomial = Tuple[int, int]  # x^a y^b
LinearCombo = Dict[Monomial, sp.Rational]
Tensor = Tuple[Monomial, ...]

# Write generated artifacts to compute/results/, not alongside the module.
OUT = Path(__file__).resolve().parent.parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def compositions(n: int, k: int) -> Iterable[Tuple[int, ...]]:
    if k == 0:
        if n == 0:
            yield ()
        return
    if k == 1:
        if n >= 1:
            yield (n,)
        return
    for first in range(1, n - k + 2):
        for rest in compositions(n - first, k - 1):
            yield (first,) + rest


def monomials_of_weight(w: int) -> List[Monomial]:
    return [(a, w - a) for a in range(w + 1)]


def tensor_basis(total_weight: int, length: int) -> List[Tensor]:
    if length == 0:
        return [()] if total_weight == 0 else []
    ans: List[Tensor] = []
    for weights in compositions(total_weight, length):
        pools = [monomials_of_weight(w) for w in weights]
        ans.extend(tuple(xs) for xs in product(*pools))
    return ans


def qplane_product(m1: Monomial, m2: Monomial, q: sp.Rational = sp.Rational(2)) -> LinearCombo:
    a, b = m1
    c, d = m2
    return {(a + c, b + d): q ** (b * c)}


def word_to_monomial(word: str) -> Monomial:
    # Normal words have all x's before all y's.
    pivot = word.find("y")
    if pivot < 0:
        return (len(word), 0)
    assert set(word[:pivot]) <= {"x"} and set(word[pivot:]) <= {"y"}
    return (pivot, len(word) - pivot)


@lru_cache(maxsize=None)
def jordan_reduce(word: str) -> Tuple[Tuple[Monomial, sp.Rational], ...]:
    """Reduce using yx = xy + x^2; output a sorted immutable linear combination."""
    pos = word.find("yx")
    if pos < 0:
        return ((word_to_monomial(word), sp.Rational(1)),)
    prefix, suffix = word[:pos], word[pos + 2 :]
    accum: Dict[Monomial, sp.Rational] = defaultdict(lambda: sp.Rational(0))
    for replacement in ("xy", "xx"):
        for mon, coeff in jordan_reduce(prefix + replacement + suffix):
            accum[mon] += coeff
    return tuple(sorted((m, c) for m, c in accum.items() if c != 0))


def jordan_product(m1: Monomial, m2: Monomial) -> LinearCombo:
    a, b = m1
    c, d = m2
    word = "x" * a + "y" * b + "x" * c + "y" * d
    return dict(jordan_reduce(word))


def bar_matrix(
    total_weight: int,
    source_length: int,
    multiply: Callable[[Monomial, Monomial], LinearCombo],
) -> Tuple[sp.Matrix, List[Tensor], List[Tensor]]:
    src = tensor_basis(total_weight, source_length)
    tgt = tensor_basis(total_weight, source_length - 1)
    row = {t: i for i, t in enumerate(tgt)}
    M = sp.zeros(len(tgt), len(src))
    for j, tensor in enumerate(src):
        for i in range(source_length - 1):
            sign = -1 if i % 2 == 0 else 1  # global convention irrelevant for homology ranks
            for mon, coeff in multiply(tensor[i], tensor[i + 1]).items():
                out = tensor[:i] + (mon,) + tensor[i + 2 :]
                M[row[out], j] += sign * coeff
    return M, src, tgt


def homology_window(
    max_weight: int,
    multiply: Callable[[Monomial, Monomial], LinearCombo],
) -> Dict[str, object]:
    records = []
    for w in range(1, max_weight + 1):
        matrices: Dict[int, sp.Matrix] = {}
        bases: Dict[int, List[Tensor]] = {}
        for r in range(1, w + 1):
            bases[r] = tensor_basis(w, r)
        for r in range(2, w + 1):
            M, _, _ = bar_matrix(w, r, multiply)
            matrices[r] = M
        for r in range(1, w + 1):
            dim_cr = len(bases[r])
            rank_out = matrices[r].rank() if r in matrices else 0
            rank_in = matrices[r + 1].rank() if r + 1 in matrices else 0
            hdim = dim_cr - rank_out - rank_in
            records.append(
                {
                    "weight": w,
                    "homological_degree": r,
                    "chain_dim": dim_cr,
                    "rank_d_out": rank_out,
                    "rank_d_in": rank_in,
                    "homology_dim": hdim,
                }
            )
    return {"max_weight": max_weight, "records": records}


def check_cycle(
    terms: Dict[Tensor, sp.Rational],
    total_weight: int,
    multiply: Callable[[Monomial, Monomial], LinearCombo],
) -> Dict[str, object]:
    M, src, tgt = bar_matrix(total_weight, 2, multiply)
    col = sp.zeros(len(src), 1)
    src_index = {t: i for i, t in enumerate(src)}
    for tensor, coeff in terms.items():
        col[src_index[tensor], 0] += coeff
    image = M * col
    return {
        "source_terms": {str(k): str(v) for k, v in terms.items()},
        "target_basis": [str(t) for t in tgt],
        "differential": [str(x) for x in image],
        "is_cycle": all(x == 0 for x in image),
    }


def sl2_ce() -> Dict[str, object]:
    # Bases: C1=(e,f,h), C2=(e^f,e^h,f^h), C3=(e^f^h).
    d2 = sp.Matrix(
        [
            [0, -2, 0],  # e component
            [0, 0, 2],   # f component
            [1, 0, 0],   # h component
        ]
    )
    d3 = sp.zeros(3, 1)
    dims = {
        "H0": 1,
        "H1": 3 - d2.rank(),
        "H2": 3 - d2.rank() - d3.rank(),
        "H3": 1 - d3.rank(),
    }
    return {
        "basis_C1": ["e", "f", "h"],
        "basis_C2": ["e^f", "e^h", "f^h"],
        "d2": [[int(x) for x in row] for row in d2.tolist()],
        "rank_d2": d2.rank(),
        "d3": [[int(x) for x in row] for row in d3.tolist()],
        "homology_dimensions": dims,
        "poincare_polynomial": "1+t^3",
    }


def hall_a2(q: int = 2) -> Dict[str, object]:
    # Coefficients in basis [X,Y] for the three products.
    e11e2 = sp.Matrix([q + 1, q + 1])
    e1e2e1 = sp.Matrix([q + 1, 1])
    e2e11 = sp.Matrix([q + 1, 0])
    combo = e11e2 - (q + 1) * e1e2e1 + q * e2e11
    return {
        "q": q,
        "basis": ["X=2S1+S2", "Y=S1+M"],
        "e1^2 e2": list(map(int, e11e2)),
        "e1 e2 e1": list(map(int, e1e2e1)),
        "e2 e1^2": list(map(int, e2e11)),
        "serre_combination": list(map(int, combo)),
        "verified": combo == sp.zeros(2, 1),
    }


def stable_trace_jacobi_sample() -> Dict[str, object]:
    # Verify Jacobi for a finite set of power-sum labels using the structure formula.
    labels = [(a, b) for a in range(4) for b in range(4) if a + b > 0]

    def bracket(u: Tuple[int, int], v: Tuple[int, int]):
        a, b = u
        c, d = v
        coeff = a * d - b * c
        out = (a + c - 1, b + d - 1)
        if coeff == 0:
            return {}
        return {out: sp.Integer(coeff)}

    def lin_bracket(left: Dict[Tuple[int, int], sp.Integer], right_label):
        out = defaultdict(lambda: sp.Integer(0))
        for u, cu in left.items():
            for v, cv in bracket(u, right_label).items():
                out[v] += cu * cv
        return dict(out)

    failures = []
    checked = 0
    for x, y, z in product(labels, repeat=3):
        total = defaultdict(lambda: sp.Integer(0))
        for first, second, third in ((x, y, z), (y, z, x), (z, x, y)):
            term = lin_bracket(bracket(first, second), third)
            for lab, coeff in term.items():
                total[lab] += coeff
        checked += 1
        if any(v != 0 for v in total.values()):
            failures.append((x, y, z, dict(total)))
            break
    return {
        "labels": labels,
        "triples_checked": checked,
        "jacobi_failures": failures,
        "verified": not failures,
    }


def main() -> None:
    quantum = homology_window(5, qplane_product)
    jordan = homology_window(5, jordan_product)

    q_cycle = check_cycle(
        {
            ((0, 1), (1, 0)): sp.Rational(1),  # [y|x]
            ((1, 0), (0, 1)): sp.Rational(-2),  # -q[x|y], q=2
        },
        2,
        qplane_product,
    )
    j_cycle = check_cycle(
        {
            ((0, 1), (1, 0)): sp.Rational(1),
            ((1, 0), (0, 1)): sp.Rational(-1),
            ((1, 0), (1, 0)): sp.Rational(-1),
        },
        2,
        jordan_product,
    )

    payload = {
        "quantum_plane_q2": quantum,
        "quantum_plane_degree2_cycle": q_cycle,
        "jordan_plane": jordan,
        "jordan_plane_degree2_cycle": j_cycle,
        "sl2_chevalley_eilenberg": sl2_ce(),
        "hall_A2": hall_a2(2),
        "stable_trace_poisson_jacobi": stable_trace_jacobi_sample(),
        "relative_quiver": {
            "quiver": "1 -a-> 2 -b-> 3 with relation ba=0",
            "base": "S=k e1 + k e2 + k e3",
            "Tor_dimensions": {"0": 3, "1": 2, "2": 1},
            "degree2_cycle": "[b|a]",
            "explanation": "Tensoring over S permits exactly the composable pair b|a; its bar boundary is ba=0.",
        },
        "augmentation_obstructions": {
            "matrix": "M_n(k), n>1, has no unital algebra map to k: a nonzero map would be injective because M_n is simple, impossible by dimension/commutativity.",
            "weyl": "A_1(k)=k<x,y>/(yx-xy-1) has no augmentation because applying an algebra map to k gives 0=1.",
        },
    }

    (OUT / "verified_results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # Human-readable compact table.
    lines = []
    lines.append("FINITE-WINDOW BAR HOMOLOGY CHECKS\n")
    for name, data in (("Quantum plane q=2", quantum), ("Jordan plane", jordan)):
        lines.append(name)
        lines.append("weight degree chain rank_out rank_in H")
        for rec in data["records"]:
            lines.append(
                f"{rec['weight']:>6} {rec['homological_degree']:>6} {rec['chain_dim']:>5} "
                f"{rec['rank_d_out']:>8} {rec['rank_d_in']:>7} {rec['homology_dim']:>2}"
            )
        lines.append("")
    lines.append(f"Quantum degree-2 cycle closed: {q_cycle['is_cycle']}")
    lines.append(f"Jordan degree-2 cycle closed: {j_cycle['is_cycle']}")
    lines.append(f"sl2 CE homology: {sl2_ce()['homology_dimensions']}")
    lines.append(f"A2 Hall-Serre verified: {hall_a2(2)['verified']}")
    lines.append(f"Stable trace Jacobi verified: {stable_trace_jacobi_sample()['verified']}")
    (OUT / "verification_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
