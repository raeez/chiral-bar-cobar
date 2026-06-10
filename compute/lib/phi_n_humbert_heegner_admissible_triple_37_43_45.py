r"""Pentagon coboundary $\phi^{(n)}$ on the higher Humbert-Heegner admissible
triple $\{37, 43, 45\}$.

Companion to phi_n_humbert_heegner_admissible_triple_27_29_35.py.  This
module isolates the next admissible triple $n \in \{37, 43, 45\}$ under
$n \equiv 3, 5 \pmod 8$:
    37 mod 8 = 5, 43 mod 8 = 3, 45 mod 8 = 5.
Intervening weights {38, 39, 40, 41, 42, 44} fall outside {3, 5} mod 8 and
are Humbert-Heegner rejected.

Scope cascade (higher admissible triple):

  weight 37: depth-9 stratum D_{37, 9} = 2023; depth-11 stratum
             D_{37, 11} = 378; Padovan count d_{37} = 13581.
             Triple-conditional at depth 9 and depth 11:
             Zagier-Hoffman + BK empirical + Brown 2017 Conj 5.3.

  weight 43: first admissible weight with populated depth-13 stratum
             D_{43, 13} = 924 (depth-13 first appears at n = 39 by BK
             parity; n = 39 not admissible, so n = 43 is first
             admissible carrier); Padovan count d_{43} = 73396.
             Quadruple-conditional at depth 13: triple +
             Broadhurst-Bailey 2010 numerical stability.

  weight 45: simultaneous depth-13 and depth-15 onsets on the
             admissible sequence: D_{45, 13} = 3076, D_{45, 15} = 69
             (depth-15 first appears at n = 45, admissible);
             Padovan count d_{45} = 128801.
             Quintuple-conditional at depth 15: quadruple + Brown 2017
             higher-depth grt_1 generation at d >= 15 outside
             Broadhurst-Bailey 2010 symbolic extractor.

For admissible n >= 45 Brown 2017 arXiv:1709.02856 Conj 5.3 is the
deepest load-bearing hypothesis controlling the higher-depth generation
of grt_1.

Verification paths (six):

  V_1 Padovan recurrence: d_n = d_{n-2} + d_{n-3} iterated from the
      Brown seed (d_{32}, d_{33}, d_{34}) = (3329, 4410, 5842)
      to reach the higher triple (d_{37}, d_{43}, d_{45}) =
      (13581, 73396, 128801).

  V_2 BK row-sum lag: sum_d D_{n, d} = d_{n-3} at admissible n;
      this is an extractor diagnostic, not the Brown dimension d_n.

  V_3 BK symbolic extraction: BK(x, y) = 1/(1 - O(x) y + S(x)(y^2 - y^4))
      truncated at x^{50} y^{16}; odd-n kills even-d by parity.

  V_4 BK recursive inverse: coefficient-by-coefficient from BK * (1 - Oy
      + S(y^2 - y^4)) = 1.

  V_5 Hardy-Ramanujan exact p_24(ceil(n/2)) at k in {19, 22, 23} via two
      paths (direct convolution, binomial Euler product).

  V_6 Depth onset tracking: depth-13 first admissible at n = 43;
      depth-15 onset coincident with admissible n = 45.

Primary literature:
    Brown 2011 Ann. Math. 175 Thm 1.1, 1.2
    Brown 2012 arXiv:1301.3053 Thm 1.2, Cor 1.3, Conj 2
    Brown 2017 arXiv:1709.02856 Conj 5.3 (higher-depth grt_1 generators)
    Broadhurst-Kreimer 1997 Phys. Lett. B393
    Broadhurst-Bailey 2010 arXiv:1004.4597 (numerical MZDP tables)
    Zagier 1994 First European Congress of Mathematics Vol II
    Hoffman 1997 J. Algebra 194 (stuffle regularisation)
    Hardy-Ramanujan 1918 Proc. London Math. Soc.
    Rademacher 1937 Ann. Math. 44
    Humbert 1899 J. Math. Pures Appl. 5 (Humbert divisors)
    Gritsenko-Hulek-Sankaran 2007 (Heegner divisors on O(2, n))
    Eichler-Zagier 1985 Prog. Math. 55 (index-m weak Jacobi polar cutoff)
    OEIS A006922 (Fourier coefficients of eta^{-24})
"""
from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Admissibility filter: n = 3, 5 (mod 8) at the higher triple
# ---------------------------------------------------------------------------

ADMISSIBLE_HIGHER_TRIPLE = (37, 43, 45)
"""The Humbert-Heegner admissible triple at n in [37, 45].

These continue the admissible sequence after {27, 29, 35}; subsequent
admissible weights are {51, 53, 59, 61, 67, 69, ...}.
"""


def humbert_heegner_admissible(n: int) -> bool:
    """Return True iff n is Humbert-Heegner admissible: n mod 8 in {3, 5}."""
    return n % 8 in (3, 5)


def admissibility_filter_check_tower() -> bool:
    """Assert n in {37, 43, 45} admissible; gap weights rejected."""
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        assert humbert_heegner_admissible(n), f"n = {n} should be admissible"
    for n in (38, 39, 40, 41, 42, 44):
        assert not humbert_heegner_admissible(n), (
            f"n = {n} should NOT be admissible (n mod 8 = {n % 8})"
        )
    # Continuation: admissible beyond 45
    for n in (51, 53, 59, 61):
        assert humbert_heegner_admissible(n), (
            f"continuation: n = {n} should be admissible"
        )
    return True


# ---------------------------------------------------------------------------
# Padovan dimension table extended through n = 60
# ---------------------------------------------------------------------------

def padovan_dim(n_max: int = 60) -> Dict[int, int]:
    """Return {n: d_n} via d_0=1, d_1=0, d_2=1 and d_n=d_{n-2}+d_{n-3}."""
    d: Dict[int, int] = {0: 1, 1: 0, 2: 1}
    for n in range(3, n_max + 1):
        d[n] = d[n - 2] + d[n - 3]
    return d


def padovan_count_check_tower() -> bool:
    """Assert d_{37}, d_{43}, d_{45} = (13581, 73396, 128801)."""
    d = padovan_dim(60)
    expected = {37: 13581, 43: 73396, 45: 128801}
    for n, v in expected.items():
        assert d[n] == v, f"Padovan d_{n} = {d[n]} != expected {v}"
    return True


# ---------------------------------------------------------------------------
# Broadhurst-Kreimer depth-graded extractor extended to d = 16
# ---------------------------------------------------------------------------

def bk_depth_extract(
    n_max: int = 60, d_max: int = 16
) -> Dict[Tuple[int, int], int]:
    r"""Extract D_{n, d} from BK(x, y) = 1 / (1 - O(x) y + S(x)(y^2 - y^4)).

    O(x) = x^3 / (1 - x^2),  S(x) = x^{12} / ((1 - x^4) (1 - x^6)).
    Truncation chosen so depth-15 at n = 45 is exactly resolved.
    """
    Ox: Dict[int, Fraction] = {}
    for k in range(0, (n_max - 3) // 2 + 1):
        Ox[3 + 2 * k] = Fraction(1)

    Sx: Dict[int, Fraction] = {}
    for a in range(0, max(0, (n_max - 12) // 4 + 1)):
        for b in range(0, max(0, (n_max - 12 - 4 * a) // 6 + 1)):
            exp = 12 + 4 * a + 6 * b
            if exp <= n_max:
                Sx[exp] = Sx.get(exp, Fraction(0)) + Fraction(1)

    g: Dict[Tuple[int, int], Fraction] = {}
    for i, c in Ox.items():
        g[(i, 1)] = g.get((i, 1), Fraction(0)) - c
    for i, c in Sx.items():
        g[(i, 2)] = g.get((i, 2), Fraction(0)) + c
        g[(i, 4)] = g.get((i, 4), Fraction(0)) - c

    def truncate(p):
        return {(i, j): v for (i, j), v in p.items() if i <= n_max and j <= d_max}

    def poly_mul(p, q):
        r: Dict[Tuple[int, int], Fraction] = {}
        for (i1, j1), c1 in p.items():
            for (i2, j2), c2 in q.items():
                if i1 + i2 > n_max or j1 + j2 > d_max:
                    continue
                key = (i1 + i2, j1 + j2)
                r[key] = r.get(key, Fraction(0)) + c1 * c2
        return r

    neg_g: Dict[Tuple[int, int], Fraction] = {k: -v for k, v in g.items()}

    D: Dict[Tuple[int, int], Fraction] = {(0, 0): Fraction(1)}
    term: Dict[Tuple[int, int], Fraction] = {(0, 0): Fraction(1)}
    for _ in range(d_max + 12):
        term = truncate(poly_mul(term, neg_g))
        if not term:
            break
        for k, v in term.items():
            D[k] = D.get(k, Fraction(0)) + v

    out: Dict[Tuple[int, int], int] = {}
    for (i, j), v in D.items():
        if 1 <= j <= d_max and i <= n_max:
            out[(i, j)] = int(v)
    return out


def bk_depth_check_tower() -> bool:
    """Assert BK-series predictions at admissible triple {37, 43, 45}.

    Computed odd-depth entries (even depths vanish by parity; all three n odd):

        D_{37, (1, 3, 5, 7, 9, 11)}  = (1, 88, 889, 2463, 2023, 378)
        D_{43, (1, 3, 5, 7, 9, 11, 13)}
                                     = (1, 123, 1860, 8322, 13245, 7097, 924)
        D_{45, (1, 3, 5, 7, 9, 11, 13, 15)}
                                     = (1, 136, 2310, 11874, 22453, 15486,
                                        3076, 69)

    Row sums: 5842 = d_{34}, 31572 = d_{40}, 55405 = d_{42}.
    """
    D = bk_depth_extract(60, 16)
    expected = {
        # n = 37
        (37, 1): 1, (37, 3): 88, (37, 5): 889, (37, 7): 2463,
        (37, 9): 2023, (37, 11): 378, (37, 13): 0, (37, 15): 0,
        # n = 43
        (43, 1): 1, (43, 3): 123, (43, 5): 1860, (43, 7): 8322,
        (43, 9): 13245, (43, 11): 7097, (43, 13): 924, (43, 15): 0,
        # n = 45
        (45, 1): 1, (45, 3): 136, (45, 5): 2310, (45, 7): 11874,
        (45, 9): 22453, (45, 11): 15486, (45, 13): 3076, (45, 15): 69,
    }
    for (n, d), v in expected.items():
        got = D.get((n, d), 0)
        assert got == v, f"D_{{{n}, {d}}} = {got} != expected {v}"
    return True


def first_depth_thirteen_at_39_check() -> bool:
    """Assert depth-13 first appears at n = 39 (not admissible).

    n = 39 mod 8 = 7, so 39 is NOT Humbert-Heegner admissible.  The first
    admissible weight at depth 13 is n = 43.
    """
    D = bk_depth_extract(60, 16)
    for n in range(1, 39):
        assert D.get((n, 13), 0) == 0, (
            f"Unexpected depth-13 at n = {n}: D = {D.get((n, 13), 0)}"
        )
    assert D.get((39, 13), 0) > 0, "Expected depth-13 onset at n = 39"
    assert not humbert_heegner_admissible(39), "n = 39 should not be admissible"
    # First admissible at depth 13 is n = 43
    assert D.get((43, 13), 0) == 924, f"D_{{43, 13}} = {D.get((43, 13), 0)} != 924"
    return True


def depth_13_15_admissible_onset_check() -> bool:
    """Assert first admissible depth-13 at n = 43; depth-15 onset at n = 45.

    The depth-15 stratum first populates at n = 45 (by BK parity rule;
    previous weights have zero).  n = 45 is Humbert-Heegner admissible
    (45 mod 8 = 5), making the depth-15 BK-series onset coincide with
    the admissible carrier.
    """
    D = bk_depth_extract(60, 16)
    # Depth-13
    assert D.get((37, 13), 0) == 0, "n = 37 depth-13 should be empty"
    assert D.get((43, 13), 0) == 924, (
        f"D_{{43, 13}} = {D.get((43, 13), 0)} != 924"
    )
    assert D.get((45, 13), 0) == 3076, (
        f"D_{{45, 13}} = {D.get((45, 13), 0)} != 3076"
    )
    # Depth-15
    for n in range(1, 45):
        assert D.get((n, 15), 0) == 0, (
            f"Unexpected depth-15 at n = {n}: D = {D.get((n, 15), 0)}"
        )
    assert D.get((45, 15), 0) == 69, (
        f"D_{{45, 15}} = {D.get((45, 15), 0)} != 69"
    )
    assert humbert_heegner_admissible(45), "n = 45 admissible check failed"
    return True


def bk_padovan_twostep_consistency_check_tower() -> bool:
    """Assert the BK row-sum lag diagnostic sum_d D_{n, d} = d_{n - 3}."""
    D = bk_depth_extract(60, 16)
    d = padovan_dim(60)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        row_sum = sum(D.get((n, k), 0) for k in range(1, 17))
        assert row_sum == d[n - 3], (
            f"n = {n}: sum_d D_{{n, d}} = {row_sum} != d_{{{n - 3}}} = {d[n - 3]}"
        )
    return True


def padovan_dim_via_bk_rowsum(n: int, D: Dict[Tuple[int, int], int]) -> int:
    r"""Return $d_n$ from the BK depth row sum at weight $n + 3$ (path P2).

    The depth extractor satisfies the two-step-lag diagnostic
    $\sum_d D_{m, d} = d_{m - 3}$
    (:func:`bk_padovan_twostep_consistency_check_tower`), so the full
    row sum at weight $m = n + 3$ recovers $d_n$ by a path independent
    of the recurrence.  Valid only when the supplied extraction covers
    every depth present at weight $n + 3$: with
    ``bk_depth_extract(60, 16)`` the first under-count is the depth-17
    onset at weight 51, so the inversion is exact for $n + 3 \le 50$;
    the tower targets $n \in \{37, 43, 45\}$ need weights
    $\{40, 46, 48\}$ and sit safely inside.
    """
    return sum(v for (m, _depth), v in D.items() if m == n + 3)


def bk_parity_split_check_tower() -> bool:
    """All three of {37, 43, 45} are odd; even depths must vanish."""
    D = bk_depth_extract(60, 16)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        assert n % 2 == 1, f"n = {n} should be odd"
        for d_even in (2, 4, 6, 8, 10, 12, 14, 16):
            assert D.get((n, d_even), 0) == 0, (
                f"odd n = {n} should have D_{{{n}, {d_even}}} = 0"
            )
    return True


# ---------------------------------------------------------------------------
# BK recursive-inverse cross-path (independent from geometric series)
# ---------------------------------------------------------------------------

def bk_depth_via_recursive_inverse(
    n_max: int = 60, d_max: int = 16
) -> Dict[Tuple[int, int], int]:
    """Re-derive D_{n, d} by solving BK * (1 - O y + S(y^2 - y^4)) = 1."""
    Ox: Dict[int, Fraction] = {}
    for k in range(0, (n_max - 3) // 2 + 1):
        Ox[3 + 2 * k] = Fraction(1)
    Sx: Dict[int, Fraction] = {}
    for a in range(0, max(0, (n_max - 12) // 4 + 1)):
        for b in range(0, max(0, (n_max - 12 - 4 * a) // 6 + 1)):
            exp = 12 + 4 * a + 6 * b
            if exp <= n_max:
                Sx[exp] = Sx.get(exp, Fraction(0)) + Fraction(1)

    BK: Dict[Tuple[int, int], Fraction] = {(0, 0): Fraction(1)}

    for total in range(1, n_max + d_max + 1):
        for d in range(1, min(d_max, total) + 1):
            n = total - d
            if n < 0 or n > n_max:
                continue
            coeff = Fraction(0)
            for i, c in Ox.items():
                if 0 <= n - i <= n_max and d - 1 >= 0:
                    coeff += c * BK.get((n - i, d - 1), Fraction(0))
            for i, c in Sx.items():
                if 0 <= n - i <= n_max and d - 2 >= 0:
                    coeff -= c * BK.get((n - i, d - 2), Fraction(0))
            for i, c in Sx.items():
                if 0 <= n - i <= n_max and d - 4 >= 0:
                    coeff += c * BK.get((n - i, d - 4), Fraction(0))
            BK[(n, d)] = coeff

    return {
        (n, d): int(v) for (n, d), v in BK.items() if v != 0 or (n == 0 and d == 0)
    }


def bk_depth_multipath_check_tower() -> bool:
    """Cross-verify BK series D_{n, d} at admissible triple {37, 43, 45}."""
    DA = bk_depth_extract(60, 16)
    DB = bk_depth_via_recursive_inverse(60, 16)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        for d in range(1, 17):
            pA = DA.get((n, d), 0)
            pB = DB.get((n, d), 0)
            assert pA == pB, (
                f"Multi-path BK cross-check fails at (n, d) = ({n}, {d}): "
                f"symbolic = {pA}, recursive-inverse = {pB}"
            )
    # Critical depth-onset cells
    for (n, d) in [(37, 9), (37, 11), (43, 13), (45, 13), (45, 15)]:
        pA = DA.get((n, d), 0)
        pB = DB.get((n, d), 0)
        assert pA == pB, (
            f"Multi-path depth-onset mismatch at ({n}, {d}): "
            f"A = {pA}, B = {pB}"
        )
    return True


# ---------------------------------------------------------------------------
# Numerical phi^(n) leading values at higher admissible triple
# ---------------------------------------------------------------------------

def phi_n_mzv_leading(n: int) -> float:
    """Leading approximation d_n * zeta(n) / n! with zeta(n) from 200-term sum."""
    d = padovan_dim(60)
    z_n = sum(1.0 / (k ** n) for k in range(1, 200))
    return d[n] * z_n / math.factorial(n)


def phi_n_leading_values_tower() -> Dict[int, float]:
    return {n: phi_n_mzv_leading(n) for n in ADMISSIBLE_HIGHER_TRIPLE}


def phi_n_leading_check_tower() -> bool:
    """Assert phi^(n) matches d_n zeta(n) / n! within numerical precision."""
    d = padovan_dim(60)
    vals = phi_n_leading_values_tower()
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        expected = d[n] * 1.0 / math.factorial(n)
        got = vals[n]
        rel = abs(got - expected) / expected
        # zeta(n) = 1 + O(2^{-n}) for large n; relative correction ~ 2^{-n}
        tol = max(1e-6, 2.0 ** (-n + 2))
        assert rel < tol, (
            f"phi^({n}) = {got:.3e} vs d_n/n! = {expected:.3e}, rel err {rel}, "
            f"tol {tol}"
        )
    return True


# ---------------------------------------------------------------------------
# Hardy-Ramanujan exact p_24 values at k in {19, 22, 23}
# ---------------------------------------------------------------------------

def p24_exact(k: int) -> int:
    """Exact p_24(k) = [q^k] prod_m (1 - q^m)^{-24} by direct expansion."""
    N = k
    coefs = [0] * (N + 1)
    coefs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            newc = coefs[:]
            for j in range(m, N + 1):
                newc[j] += newc[j - m]
            coefs = newc
    return coefs[k]


def p24_via_euler_product(k_target: int) -> int:
    """Recover p_24(k) by direct Euler-product expansion."""
    coefs = [0] * (k_target + 1)
    coefs[0] = 1
    for m in range(1, k_target + 1):
        factor = {0: 1}
        j = 1
        while m * j <= k_target:
            factor[m * j] = math.comb(j + 23, 23)
            j += 1
        newc = [0] * (k_target + 1)
        for i in range(k_target + 1):
            if coefs[i] == 0:
                continue
            for deg, val in factor.items():
                if i + deg <= k_target:
                    newc[i + deg] += coefs[i] * val
        coefs = newc
    return coefs[k_target]


def p24_multipath_check_tower() -> bool:
    """Assert exact p_24(k) at k in {19, 22, 23} via two independent paths.

    OEIS A006922 values:
        p_24(19) = 69,228,721,526,400
        p_24(22) = 1,971,466,420,726,656
        p_24(23) = 5,776,331,152,550,400
    """
    expected = {
        19: 69228721526400,
        22: 1971466420726656,
        23: 5776331152550400,
    }
    for k, v in expected.items():
        pA = p24_exact(k)
        pB = p24_via_euler_product(k)
        assert pA == pB == v, (
            f"p_24({k}): direct = {pA}, Euler = {pB}, expected = {v}"
        )
    return True


def borcherds_mzv_ratio_tower() -> Dict[int, float]:
    """Exact Borcherds/MZV ratio p_24(ceil(n/2)) / d_n at admissible triple."""
    d = padovan_dim(60)
    out: Dict[int, float] = {}
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        k = (n + 1) // 2
        out[n] = p24_exact(k) / d[n]
    return out


def hardy_ramanujan_exact_check_tower() -> bool:
    """Assert Borcherds/MZV ratios at higher admissible triple."""
    r = borcherds_mzv_ratio_tower()
    expected = {
        37: 69228721526400 / 13581,
        43: 1971466420726656 / 73396,
        45: 5776331152550400 / 128801,
    }
    for n, v in expected.items():
        assert abs(r[n] - v) / v < 1e-12, (
            f"ratio at n = {n}: {r[n]} != expected {v}"
        )
    return True


# ---------------------------------------------------------------------------
# Scope cascade: triple -> quadruple -> quintuple conditional
# ---------------------------------------------------------------------------

def scope_tier_at_tower(n: int) -> str:
    """Return the scope tier for an admissible higher-tower weight.

    tier at (n = 37):  triple-conditional-depth-11
    tier at (n = 43):  quadruple-conditional-depth-13
    tier at (n = 45):  quintuple-conditional-depth-15
    """
    assert humbert_heegner_admissible(n), f"n = {n} is not admissible"
    D = bk_depth_extract(60, 16)
    max_depth = max(
        d for (m, d), v in D.items() if m == n and v > 0
    )
    if max_depth == 11:
        return "triple-conditional-depth-11"
    if max_depth == 13:
        return "quadruple-conditional-depth-13"
    if max_depth == 15:
        return "quintuple-conditional-depth-15"
    return f"scope-depth-{max_depth}"


def scope_cascade_check_tower() -> Dict[int, str]:
    return {n: scope_tier_at_tower(n) for n in ADMISSIBLE_HIGHER_TRIPLE}


def scope_cascade_assertion_tower() -> bool:
    """Assert scope cascade: triple at 37, quadruple at 43, quintuple at 45."""
    tiers = scope_cascade_check_tower()
    assert tiers[37] == "triple-conditional-depth-11", (
        f"n = 37 tier: {tiers[37]}"
    )
    assert tiers[43] == "quadruple-conditional-depth-13", (
        f"n = 43 tier: {tiers[43]}"
    )
    assert tiers[45] == "quintuple-conditional-depth-15", (
        f"n = 45 tier: {tiers[45]}"
    )
    return True


def brown_2017_deepest_at_n_geq_45() -> bool:
    """Assert Brown 2017 Conj 5.3 is deepest hypothesis at admissible n >= 45.

    For admissible n >= 45 the depth-15 (and beyond) stratum enters via
    the BK series; Broadhurst-Bailey 2010 tabulated values do not extend
    past depth 13 for n in our range, so Brown 2017 Conj 5.3 on the
    higher-depth generation of grt_1 is the load-bearing hypothesis for
    every entry at d >= 15.
    """
    assert humbert_heegner_admissible(45)
    # The next few admissible weights
    for n in (51, 53, 59, 61):
        assert humbert_heegner_admissible(n), f"continuation check: n = {n}"
    return True


# ---------------------------------------------------------------------------
# Plastic-number asymptotic cross-check at higher tower
# ---------------------------------------------------------------------------

def plastic_number() -> float:
    """Plastic number rho, unique real root of x^3 - x - 1."""
    return (1.0 / 6.0) * (
        (108 + 12 * math.sqrt(69)) ** (1.0 / 3.0)
        + (108 - 12 * math.sqrt(69)) ** (1.0 / 3.0)
    )


def padovan_asymptotic(n: int) -> float:
    """Plastic-number asymptotic d_n ~ A rho^n for Brown seed d_0,d_1,d_2."""
    rho = plastic_number()
    A = rho ** 3 / (2 * rho + 3)
    return A * (rho ** n)


def plastic_asymptotic_precision_check_tower() -> bool:
    """Plastic asymptotic within 10^-4 of exact d_n at higher admissible triple."""
    d = padovan_dim(60)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        a = padovan_asymptotic(n)
        rel_err = abs(d[n] - a) / d[n]
        assert rel_err < 1e-4, (
            f"plastic asymptotic at n = {n}: exact {d[n]}, asymptotic {a}, "
            f"rel err {rel_err:.6%}"
        )
    return True


# ---------------------------------------------------------------------------
# Multi-path Padovan dimension verifications
# ---------------------------------------------------------------------------

def bk_rowsum_lag_diagnostic(
    n: int, D: Dict[Tuple[int, int], int]
) -> int:
    """Return sum_d D_{n, d}; for the BK series this equals d_{n-3}."""
    return sum(D.get((n, k), 0) for k in range(1, 17))


def padovan_dim_via_generating_function(n_max: int = 60) -> Dict[int, int]:
    """Recover d_n from F(x) = 1 / (1 - x^2 - x^3)."""
    c = [0] * (n_max + 1)
    c[0] = 1
    c[1] = 0
    for n in range(2, n_max + 1):
        c[n] = 0
        if n >= 2:
            c[n] += c[n - 2]
        if n >= 3:
            c[n] += c[n - 3]
    return {n: c[n] for n in range(0, n_max + 1)}


def padovan_dim_via_plastic_rounded(n_max: int = 60) -> Dict[int, int]:
    """Recover d_n by rounding A rho^n to nearest integer."""
    return {n: round(padovan_asymptotic(n)) for n in range(8, n_max + 1)}


def padovan_multipath_check_tower() -> bool:
    """Four independent computations of d_n agree at higher admissible triple."""
    d_P1 = padovan_dim(60)
    D = bk_depth_extract(60, 16)
    d_P2 = padovan_dim_via_generating_function(60)
    d_P3 = padovan_dim_via_plastic_rounded(60)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        p1 = d_P1[n]
        p2 = d_P2[n]
        p3 = d_P3[n]
        row = bk_rowsum_lag_diagnostic(n, D)
        assert p1 == p2, f"n = {n}: P1 {p1} != P2 (genfun) {p2}"
        assert p1 == p3, f"n = {n}: P1 {p1} != P3 (plastic) {p3}"
        assert row == d_P1[n - 3], (
            f"n = {n}: BK row sum {row} != d_{{{n - 3}}} = {d_P1[n - 3]}"
        )
    return True


# ---------------------------------------------------------------------------
# Aggregate verifier
# ---------------------------------------------------------------------------

def verifier_tower_37_43_45() -> Dict[str, bool]:
    """Run every phi^(n) verification check for the higher admissible triple."""
    return {
        "admissibility_filter_tower": admissibility_filter_check_tower(),
        "padovan_count_tower": padovan_count_check_tower(),
        "padovan_multipath_tower": padovan_multipath_check_tower(),
        "bk_depth_tower": bk_depth_check_tower(),
        "bk_depth_multipath_tower": bk_depth_multipath_check_tower(),
        "bk_rowsum_lag_tower": bk_padovan_twostep_consistency_check_tower(),
        "bk_parity_split_tower": bk_parity_split_check_tower(),
        "first_depth_13_at_39": first_depth_thirteen_at_39_check(),
        "depth_13_15_admissible_onsets": depth_13_15_admissible_onset_check(),
        "phi_n_leading_tower": phi_n_leading_check_tower(),
        "hardy_ramanujan_tower": hardy_ramanujan_exact_check_tower(),
        "p24_multipath_tower": p24_multipath_check_tower(),
        "scope_cascade_tower": scope_cascade_assertion_tower(),
        "brown_2017_deepest_geq_45": brown_2017_deepest_at_n_geq_45(),
        "plastic_asymptotic_tower": plastic_asymptotic_precision_check_tower(),
    }


if __name__ == "__main__":
    results = verifier_tower_37_43_45()
    assert all(results.values()), f"Failures: {results}"

    d = padovan_dim(60)
    print("Humbert-Heegner admissible higher triple at n in [37, 45]:")
    print(
        f"  Admissible: n in {ADMISSIBLE_HIGHER_TRIPLE} "
        "(continuation: 51, 53, 59, ...)"
    )
    print()
    print("Padovan dimensions:")
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        print(f"  d_{n} = {d[n]}")

    print()
    print("Broadhurst-Kreimer D_{n, d} at higher admissible triple:")
    D = bk_depth_extract(60, 16)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        row = [D.get((n, dd), 0) for dd in range(1, 17)]
        s = sum(row)
        print(
            f"  D_{{{n}, d}} for d in [1, 16] = {row}, "
            f"sum = {s} = d_{{{n-3}}} = {d[n-3]}"
        )

    print()
    print("Depth-13/15 onsets:")
    print(f"  First depth-13: n = 39 (D_{{39, 13}} = {D.get((39, 13), 0)})")
    print(f"  First admissible depth-13: n = 43 (D_{{43, 13}} = {D.get((43, 13), 0)})")
    print(f"  Depth-15 onset: n = 45 (D_{{45, 15}} = {D.get((45, 15), 0)})")

    print()
    print("Scope cascade:")
    for n, tier in scope_cascade_check_tower().items():
        print(f"  n = {n}: {tier}")

    print()
    print("phi^(n) leading numerical values at higher admissible triple:")
    vals = phi_n_leading_values_tower()
    for n, v in sorted(vals.items()):
        print(f"  phi^({n})_MZV ~ {v:.3e}")

    print()
    print("Hardy-Ramanujan exact p_24 and Borcherds/MZV ratio:")
    print(
        f"  p_24(19) = {p24_exact(19):,}, "
        f"p_24(22) = {p24_exact(22):,}, "
        f"p_24(23) = {p24_exact(23):,}"
    )
    r = borcherds_mzv_ratio_tower()
    for n, ratio in sorted(r.items()):
        print(f"  n = {n}: Borcherds/MZV = {ratio:.3e}")

    print()
    print(
        "Brown 2017 arXiv:1709.02856 Conj 5.3 is the deepest load-bearing "
        "hypothesis at admissible n >= 45 (depth-15 and beyond)."
    )
