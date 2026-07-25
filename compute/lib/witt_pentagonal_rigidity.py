"""Chevalley-Eilenberg cohomology of graded Lie algebras, exact over Q.

Supports the pentagonal-rigidity theorem for the positive Witt algebra
L_1 = <e_1, e_2, ...>, [e_i, e_j] = (j - i) e_{i+j}, and the falsification of
the circulating Motzkin/Riordan bar-cohomology dimension formulas.

Cochains C^n = Lambda^n(g^*), basis = strictly increasing tuples of generators.
The differential is the degree +1 derivation determined by

    d e^k = - sum_{i<j} c_{ij}^k e^i ^ e^j,      [e_i, e_j] = sum_k c_{ij}^k e_k

extended by the graded Leibniz rule.  Each e^k has degree 1, so

    d(e^{k_1} ^ ... ^ e^{k_n}) = sum_p (-1)^p e^{k_1} ^ ... ^ d(e^{k_p}) ^ ... ^ e^{k_n}

with p zero-indexed.  The Koszul sign (-1)^p is what makes d^2 = 0; dropping it
produces negative Betti numbers, so check_d_squared is called on every space
whose cohomology is reported rather than being assumed.

Reference values:
  Goncharova (1973): dim H^n(L_1) = 2 for n >= 1, in weights (3n^2 -+ n)/2.
  Whitehead: H^*(sl_2; k) = Lambda(c_3), Betti numbers 1, 0, 0, 1.
  Euler: prod_{n>=1} (1 - q^n) = sum_{m in Z} (-1)^m q^{m(3m-1)/2}.
"""

from fractions import Fraction
from itertools import combinations

__all__ = [
    "GradedLie",
    "rank_Q",
    "motzkin",
    "riordan",
    "euler_function_coefficients",
    "pentagonal_numbers",
    "witt_positive",
    "sl2",
]


def rank_Q(rows):
    """Rank over Q of a sparse matrix given as a list of dict{col: Fraction}."""
    pivots = {}
    rank = 0
    for row in rows:
        r = dict(row)
        while r:
            c = min(r)
            if c in pivots:
                p = pivots[c]
                f = r[c] / p[c]
                for cc, v in p.items():
                    nv = r.get(cc, Fraction(0)) - f * v
                    if nv == 0:
                        r.pop(cc, None)
                    else:
                        r[cc] = nv
            else:
                pivots[c] = r
                rank += 1
                break
    return rank


def _sort_sign(arr):
    """Sort distinct ints, returning (tuple, sign); (None, 0) if a repeat occurs."""
    if len(set(arr)) != len(arr):
        return None, 0
    arr = list(arr)
    sign = 1
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sign = -sign
    return tuple(arr), sign


class GradedLie:
    """A weight-graded Lie algebra presented by structure constants."""

    def __init__(self, weights, bracket):
        """weights: {gen: weight}.  bracket: {(i, j): {k: coeff}} with i < j."""
        self.weights = dict(weights)
        self.gens = sorted(weights)
        self.dual = {}
        for (i, j), coeffs in bracket.items():
            if i >= j:
                raise ValueError("bracket keys must be ordered pairs i < j")
            for k, c in coeffs.items():
                if c:
                    self.dual.setdefault(k, []).append((Fraction(-c), i, j))

    def cochains(self, n, w):
        if n < 0:
            return []
        if n == 0:
            return [()] if w == 0 else []
        return [t for t in combinations(self.gens, n)
                if sum(self.weights[g] for g in t) == w]

    def d(self, tup):
        """Differential of one basis cochain, as dict{tuple: Fraction}."""
        out = {}
        for pos, k in enumerate(tup):
            terms = self.dual.get(k)
            if not terms:
                continue
            rest = tup[:pos] + tup[pos + 1:]
            leibniz = (-1) ** pos
            for c, i, j in terms:
                key, sgn = _sort_sign(list(rest[:pos]) + [i, j] + list(rest[pos:]))
                if sgn == 0:
                    continue
                out[key] = out.get(key, Fraction(0)) + c * leibniz * sgn
        return {k: v for k, v in out.items() if v != 0}

    def matrix(self, n, w):
        """d^n : C^n_w -> C^{n+1}_w as (rows, source basis, target basis)."""
        src = self.cochains(n, w)
        tgt = self.cochains(n + 1, w)
        index = {t: i for i, t in enumerate(tgt)}
        rows = []
        for t in src:
            img = self.d(t)
            stray = [k for k in img if k not in index]
            if stray:
                raise AssertionError(
                    f"d left the weight-{w} degree-{n + 1} space: {stray}")
            rows.append({index[k]: v for k, v in img.items()})
        return rows, src, tgt

    def check_d_squared(self, n, w):
        """Assert d^{n+1} . d^n = 0 on C^n_w."""
        for t in self.cochains(n, w):
            acc = {}
            for k1, v1 in self.d(t).items():
                for k2, v2 in self.d(k1).items():
                    acc[k2] = acc.get(k2, Fraction(0)) + v1 * v2
            bad = {k: v for k, v in acc.items() if v != 0}
            if bad:
                raise AssertionError(f"d^2 != 0 on {t} in weight {w}: {bad}")

    def cohomology(self, n, w, verify=True):
        """Return (dim H^n_w, dim C^n_w)."""
        if verify:
            if n >= 1:
                self.check_d_squared(n - 1, w)
            self.check_d_squared(n, w)
        rows_n, src_n, _ = self.matrix(n, w)
        rank_out = rank_Q(rows_n)
        if n == 0:
            rank_in = 0
        else:
            rows_prev, _, _ = self.matrix(n - 1, w)
            rank_in = rank_Q(rows_prev)
        return len(src_n) - rank_out - rank_in, len(src_n)


def witt_positive(nmode):
    """L_1 truncated to modes e_1, ..., e_nmode."""
    weights = {i: i for i in range(1, nmode + 1)}
    bracket = {(i, j): {i + j: (j - i)}
               for i in range(1, nmode + 1)
               for j in range(i + 1, nmode + 1)
               if i + j <= nmode}
    return GradedLie(weights, bracket)


def sl2():
    """sl_2 with basis e = 1, f = 2, h = 3; [e,f] = h, [e,h] = -2e, [f,h] = 2f."""
    return GradedLie({1: 0, 2: 0, 3: 0},
                     {(1, 2): {3: 1}, (1, 3): {1: -2}, (2, 3): {2: 2}})


def motzkin(n):
    """M(z) = 1 + zM + z^2 M^2, M(0) = 1."""
    M = [0] * (n + 1)
    M[0] = 1
    for k in range(1, n + 1):
        M[k] = M[k - 1] + sum(M[j] * M[k - 2 - j] for j in range(0, k - 1))
    return M


def riordan(n):
    """R(k) = ((k-1)(2R(k-1) + 3R(k-2)))/(k+1), R(0) = 1, R(1) = 0."""
    R = [Fraction(0)] * (n + 1)
    R[0] = Fraction(1)
    for k in range(2, n + 1):
        R[k] = Fraction((k - 1) * (2 * R[k - 1] + 3 * R[k - 2]), k + 1)
    if any(r.denominator != 1 for r in R):
        raise AssertionError("Riordan recurrence left the integers")
    return [int(r) for r in R]


def euler_function_coefficients(n):
    """Coefficients of prod_{k>=1} (1 - q^k) up to q^n."""
    coeffs = [0] * (n + 1)
    coeffs[0] = 1
    for k in range(1, n + 1):
        new = coeffs[:]
        for j in range(0, n + 1 - k):
            new[j + k] -= coeffs[j]
        coeffs = new
    return coeffs


def pentagonal_numbers(bound):
    """Generalized pentagonal numbers (3m^2 +- m)/2 not exceeding bound."""
    out = set()
    m = 0
    while True:
        m += 1
        a, b = (3 * m * m - m) // 2, (3 * m * m + m) // 2
        if a > bound:
            break
        out.add(a)
        if b <= bound:
            out.add(b)
    return sorted({0} | out)
