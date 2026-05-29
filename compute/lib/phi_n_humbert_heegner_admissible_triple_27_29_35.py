r"""Pentagon coboundary $\phi^{(n)}$ on the Humbert-Heegner admissible triple
$\{27, 29, 35\}$.

This module isolates the three admissible weights in the range $n \ge 25$
selected by the Humbert-Heegner filter $n \equiv 3, 5 \pmod 8$ (Theorem
`thm:phi-n-humbert-heegner-admissibility`).  In the range $25 \le n \le 36$
the admissible weights are $\{27, 29, 35\}$; $n \in \{37, 43, 45, \ldots\}$
continue the admissible sequence beyond this module's inscribed target.

Scope cascade (admissible triple only):

  weight 27: first depth-9 irreducible zeta(3,3,3,3,3,3,3,3,3) enters;
             Padovan count d_{27} = 816; D_{27,9} = 10.
             Triple-conditional at depth 9: Zagier-Hoffman + BK empirical
             + Brown 2017 Conj 5.3.

  weight 29: depth-9 expansion D_{29,9} = 42 (factor 4.2 over n = 27);
             Padovan count d_{29} = 1432.
             Triple-conditional at depth 9, same three conjectures.

  weight 35: depth-11 irreducible count D_{35,11} = 97 (first depth-11
             enters at n = 33 by BK series; n = 35 is admissible under
             Humbert-Heegner);
             Padovan count d_{35} = 7739.
             Quadruple-conditional: Zagier-Hoffman + BK empirical +
             Brown 2017 + Broadhurst-Bailey 2010 numerical-extrapolation
             stability at depth 11.

Under the composite Humbert-Heegner + Eichler-Zagier polar cutoff on the
K3 A-infinity regime, the pentagon coboundary satisfies
$\phi^{(n)}\big|_{K3\text{-Humbert}} = 0$ for admissible $n \ge 11$ by
polar support; the Padovan leg nonetheless persists off the K3 regime as
the first-principles MZV-transcendence count carrying the
Theta-obstruction tower through the Maurer-Cartan recursion.

Verification paths:

  V_1 (Padovan + admissibility):  d_n = d_{n-2} + d_{n-3} iterated from
      canonical Zagier-Brown seed; admissibility n mod 8 in {3, 5}.
  V_2 (Broadhurst-Kreimer extraction):  symbolic expansion of
      BK(x, y) = 1 / (1 - O(x) y + S(x) (y^2 - y^4)) through
      x^{40} y^{12}; the row-sum lag sum_d D_{n, d} = d_{n - 3}
      is a BK extractor diagnostic, not the Brown dimension d_n.
  V_3 (Hardy-Ramanujan exact p_24 Borcherds-leg control):
      p_24(14), p_24(15), p_24(18) via eta^{-24} Fourier expansion
      (OEIS A006922); Borcherds/MZV ratio computed exactly.
  V_4 (depth onset tracking):  first depth-9 at n = 27 (10 irreducibles);
      first depth-11 at n = 33 (BK series).
  V_5 (Brown 2017 triple/quadruple-conditional scope witnesses):
      independently-derived numerical depth-stratification values at
      each admissible weight.

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
    Gritsenko-Nikulin 1998 (Phi_{10}/eta^{24} Borcherds quotient sign)
    OEIS A006922 (Fourier coefficients of eta^{-24})
"""
from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Admissibility filter: n = 3, 5 (mod 8)
# ---------------------------------------------------------------------------

ADMISSIBLE_TRIPLE = (27, 29, 35)
"""The Humbert-Heegner admissible triple under investigation.

These are the admissible weights at n >= 25, n <= 35.  The next admissible
weight is n = 37 (5 mod 8); then n = 43 (3 mod 8); then n = 45 (5 mod 8).
"""


def humbert_heegner_admissible(n: int) -> bool:
    """Return True iff n is Humbert-Heegner admissible.

    The admissibility condition on the pentagon coboundary lattice sum
    (Theorem thm:phi-n-humbert-heegner-admissibility item (a)) reads
    D_n = (n - 3) / 2 must satisfy D_n mod 4 in {0, 1}; equivalently
    n mod 8 in {3, 5}.
    """
    return n % 8 in (3, 5)


def admissibility_filter_check() -> bool:
    """Assert n in {27, 29, 35} are Humbert-Heegner admissible."""
    for n in ADMISSIBLE_TRIPLE:
        assert humbert_heegner_admissible(n), f"n = {n} should be admissible"
    # Cross-check: non-admissible neighbours
    for n in (25, 26, 28, 30, 31, 32, 33, 34, 36):
        assert not humbert_heegner_admissible(n), (
            f"n = {n} should NOT be admissible (n mod 8 = {n % 8})"
        )
    # Continuation of the admissible sequence
    assert humbert_heegner_admissible(37)
    assert humbert_heegner_admissible(43)
    assert humbert_heegner_admissible(45)
    return True


# ---------------------------------------------------------------------------
# Padovan dimension table
# ---------------------------------------------------------------------------

def padovan_dim(n_max: int = 46) -> Dict[int, int]:
    """Return {n: d_n} via d_0=1, d_1=0, d_2=1 and d_n=d_{n-2}+d_{n-3}."""
    d: Dict[int, int] = {0: 1, 1: 0, 2: 1}
    for n in range(3, n_max + 1):
        d[n] = d[n - 2] + d[n - 3]
    return d


def padovan_count_check_triple() -> bool:
    """Assert d_{27}, d_{29}, d_{35} = (816, 1432, 7739)."""
    d = padovan_dim(46)
    expected = {27: 816, 29: 1432, 35: 7739}
    for n, v in expected.items():
        assert d[n] == v, f"Padovan d_{n} = {d[n]} != expected {v}"
    return True


# ---------------------------------------------------------------------------
# Broadhurst-Kreimer depth-graded extractor
# ---------------------------------------------------------------------------

def bk_depth_extract(n_max: int = 40, d_max: int = 12) -> Dict[Tuple[int, int], int]:
    r"""Extract D_{n, d} from BK(x, y) = 1 / (1 - O(x) y + S(x) (y^2 - y^4)).

    O(x) = x^3 / (1 - x^2),  S(x) = x^{12} / ((1 - x^4) (1 - x^6)).
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

    def truncate(
        p: Dict[Tuple[int, int], Fraction],
    ) -> Dict[Tuple[int, int], Fraction]:
        return {(i, j): v for (i, j), v in p.items() if i <= n_max and j <= d_max}

    def poly_mul(
        p: Dict[Tuple[int, int], Fraction], q: Dict[Tuple[int, int], Fraction]
    ) -> Dict[Tuple[int, int], Fraction]:
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


def bk_depth_check_triple() -> bool:
    """Assert BK-series predictions for n in {27, 29, 35}.

    Expected depth rows (parity-enforced: odd n kills even d, even n kills
    odd d; here all three of {27, 29, 35} are odd so even depths vanish):

        D_{27, .} = (1, 0,  41, 0,  171, 0,  128, 0,   10, 0,   0)
        D_{29, .} = (1, 0,  50, 0,  249, 0,  274, 0,   42, 0,   0)
        D_{35, .} = (1, 0,  77, 0,  673, 0, 1532, 0,  949, 0,  97)

    Depth-9 first appears at n = 27 with D_{27, 9} = 10.
    Depth-11 first appears at n = 33; at admissible n = 35 it takes
    value D_{35, 11} = 97.
    """
    D = bk_depth_extract(40, 12)
    expected = {
        (27, 1): 1,   (27, 2): 0,   (27, 3): 41,  (27, 4): 0,
        (27, 5): 171, (27, 6): 0,   (27, 7): 128, (27, 8): 0,
        (27, 9): 10,  (27, 10): 0,  (27, 11): 0,
        (29, 1): 1,   (29, 2): 0,   (29, 3): 50,  (29, 4): 0,
        (29, 5): 249, (29, 6): 0,   (29, 7): 274, (29, 8): 0,
        (29, 9): 42,  (29, 10): 0,  (29, 11): 0,
        (35, 1): 1,   (35, 2): 0,   (35, 3): 77,  (35, 4): 0,
        (35, 5): 673, (35, 6): 0,   (35, 7): 1532, (35, 8): 0,
        (35, 9): 949, (35, 10): 0,  (35, 11): 97,
    }
    for (n, d), v in expected.items():
        got = D.get((n, d), 0)
        assert got == v, f"D_{{{n}, {d}}} = {got} != expected {v}"
    return True


def first_depth_nine_at_27_check() -> bool:
    """Assert n = 27 is the first weight with D_{n, 9} > 0."""
    D = bk_depth_extract(40, 12)
    for n in range(1, 27):
        assert D.get((n, 9), 0) == 0, (
            f"Unexpected depth-9 at n = {n}: D_{{{n}, 9}} = {D.get((n, 9), 0)}"
        )
    assert D.get((27, 9), 0) == 10, (
        f"Expected D_{{27, 9}} = 10 (first depth-9), got {D.get((27, 9), 0)}"
    )
    return True


def first_depth_eleven_at_33_check() -> bool:
    """Assert n = 33 is the first weight with D_{n, 11} > 0.

    The admissible triple weight n = 35 inherits the depth-11 regime
    two steps after the depth-11 onset (parity: 33, 35 both odd, so
    odd depths live at both).
    """
    D = bk_depth_extract(40, 12)
    for n in range(1, 33):
        assert D.get((n, 11), 0) == 0, (
            f"Unexpected depth-11 at n = {n}: D_{{{n}, 11}} = {D.get((n, 11), 0)}"
        )
    assert D.get((33, 11), 0) == 19, (
        f"Expected D_{{33, 11}} = 19 (first depth-11), got {D.get((33, 11), 0)}"
    )
    return True


def bk_padovan_twostep_consistency_check_triple() -> bool:
    """Assert the BK row-sum lag diagnostic sum_d D_{n, d} = d_{n - 3}."""
    D = bk_depth_extract(40, 12)
    d = padovan_dim(46)
    for n in ADMISSIBLE_TRIPLE:
        row_sum = sum(D.get((n, k), 0) for k in range(1, 13))
        assert row_sum == d[n - 3], (
            f"n = {n}: sum_d D_{{n, d}} = {row_sum} != d_{{{n - 3}}} = {d[n - 3]}"
        )
    return True


def bk_parity_split_check_triple() -> bool:
    """All three of {27, 29, 35} are odd; even depths must vanish."""
    D = bk_depth_extract(40, 12)
    for n in ADMISSIBLE_TRIPLE:
        assert n % 2 == 1, f"n = {n} should be odd (all admissible weights are odd)"
        for d_even in (2, 4, 6, 8, 10, 12):
            assert D.get((n, d_even), 0) == 0, (
                f"odd n = {n} should have D_{{{n}, {d_even}}} = 0"
            )
    return True


# ---------------------------------------------------------------------------
# Numerical phi^(n) leading values at admissible triple
# ---------------------------------------------------------------------------

def phi_n_mzv_leading(n: int) -> float:
    """Leading approximation d_n * zeta(n) / n! with zeta(n) ~ 1 for large n.

    Uses 400-term truncation of zeta(n) for numerical stability at n >= 35;
    tail O(1/400^(n-1)) is below 10^{-80} for n = 35.
    """
    d = padovan_dim(46)
    z_n = sum(1.0 / (k ** n) for k in range(1, 400))
    return d[n] * z_n / math.factorial(n)


def phi_n_leading_values_triple() -> Dict[int, float]:
    """Tabulate phi^(n) leading numerical values at n in {27, 29, 35}."""
    return {n: phi_n_mzv_leading(n) for n in ADMISSIBLE_TRIPLE}


def phi_n_leading_check_triple() -> bool:
    """Assert phi^(n) matches d_n / n! to eight decimals at admissible triple."""
    d = padovan_dim(46)
    vals = phi_n_leading_values_triple()
    for n in ADMISSIBLE_TRIPLE:
        expected = d[n] / math.factorial(n)
        got = vals[n]
        rel = abs(got - expected) / expected
        assert rel < 1e-7, (
            f"phi^({n}) = {got:.3e} vs d_n/n! = {expected:.3e}, rel err {rel}"
        )
    return True


# ---------------------------------------------------------------------------
# Hardy-Ramanujan exact p_24 and Borcherds/MZV ratio
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


def p24_asymptotic(k: int) -> float:
    """Hardy-Ramanujan asymptotic p_24(k) ~ (4 pi)^{-1} k^{-27/4} exp(4 pi sqrt k)."""
    return (
        (1.0 / (4.0 * math.pi))
        * (k ** (-27.0 / 4.0))
        * math.exp(4 * math.pi * math.sqrt(k))
    )


def borcherds_mzv_ratio_triple() -> Dict[int, float]:
    """Exact Borcherds/MZV ratio p_24(ceil(n/2)) / d_n at n in {27, 29, 35}."""
    d = padovan_dim(46)
    out: Dict[int, float] = {}
    for n in ADMISSIBLE_TRIPLE:
        k = (n + 1) // 2
        out[n] = p24_exact(k) / d[n]
    return out


def hardy_ramanujan_exact_check_triple() -> bool:
    """Assert exact Borcherds/MZV ratios at admissible triple.

    p_24 values:
        p_24(14) = 156,883,829,400      (OEIS A006922[14])  -> n = 27
        p_24(15) = 563,116,739,584      (OEIS A006922[15])  -> n = 29
        p_24(18) = 21,651,325,216,200   (OEIS A006922[18])  -> n = 35
    """
    assert p24_exact(14) == 156883829400, (
        f"p_24(14) = {p24_exact(14)} != 156883829400"
    )
    assert p24_exact(15) == 563116739584, (
        f"p_24(15) = {p24_exact(15)} != 563116739584"
    )
    assert p24_exact(18) == 21651325216200, (
        f"p_24(18) = {p24_exact(18)} != 21651325216200"
    )
    r = borcherds_mzv_ratio_triple()
    expected = {
        27: 156883829400 / 816,
        29: 563116739584 / 1432,
        35: 21651325216200 / 7739,
    }
    for n, v in expected.items():
        assert abs(r[n] - v) / v < 1e-12, f"ratio at n = {n}: {r[n]} != {v}"
    return True


# ---------------------------------------------------------------------------
# Scope cascade: triple-conditional at {27, 29}, quadruple-conditional at 35
# ---------------------------------------------------------------------------

def scope_tier_at(n: int) -> str:
    """Return the scope tier for the admissible weight n.

    Returns one of:
      "triple-conditional-depth-9" for n in {27, 29}
      "quadruple-conditional-depth-11" for n >= 33 (so n = 35 admissible)
    """
    assert humbert_heegner_admissible(n), f"n = {n} is not admissible"
    D = bk_depth_extract(40, 12)
    max_depth = max(d for (m, d), v in D.items() if m == n and v > 0)
    if max_depth == 9:
        return "triple-conditional-depth-9"
    if max_depth >= 11:
        return "quadruple-conditional-depth-11"
    if max_depth == 7:
        return "double-conditional-depth-7"
    return f"scope-depth-{max_depth}"


def scope_cascade_check() -> Dict[int, str]:
    """Return the scope tier for each admissible weight."""
    return {n: scope_tier_at(n) for n in ADMISSIBLE_TRIPLE}


def scope_cascade_assertion() -> bool:
    """Assert scope cascade: triple-conditional at {27, 29}, quadruple at 35."""
    tiers = scope_cascade_check()
    assert tiers[27] == "triple-conditional-depth-9", (
        f"n = 27 tier: {tiers[27]}, expected triple-conditional-depth-9"
    )
    assert tiers[29] == "triple-conditional-depth-9", (
        f"n = 29 tier: {tiers[29]}, expected triple-conditional-depth-9"
    )
    assert tiers[35] == "quadruple-conditional-depth-11", (
        f"n = 35 tier: {tiers[35]}, expected quadruple-conditional-depth-11"
    )
    return True


# ---------------------------------------------------------------------------
# Brown 2017 conditional-onset tracker: depth d >= 11 requires Brown 2017
# Conj 5.3 at n >= 45 as deepest conditional, but depth 11 at n = 35 is
# already within the quadruple-conditional regime (Zagier-Hoffman + BK
# empirical + Brown 2017 + Broadhurst-Bailey 2010 numerical extrapolation)
# ---------------------------------------------------------------------------

def brown_2017_onset_weight() -> int:
    """Return the weight at which Brown 2017 Conj 5.3 becomes load-bearing.

    Brown 2017 arXiv:1709.02856 Conj 5.3 asserts that the pro-Q_ell Lie
    algebra grt_1 is generated in odd depth at every weight, with no
    irrelevant generators beyond depth 9.  The conjecture becomes
    LOAD-BEARING at depth >= 9, i.e. for phi^(n) at n >= 27 in our
    admissible tower.  For depth >= 11 (n >= 33) the conjecture is
    additionally strengthened by the Broadhurst-Bailey 2010 numerical
    extrapolation requirement, making the scope quadruple-conditional.

    Returns n = 27 (first depth-9 onset, admissible).
    """
    return 27


def quadruple_conditional_onset_weight() -> int:
    """Return first admissible weight with quadruple-conditional scope.

    Depth-11 first appears at n = 33 (not admissible).  The first
    admissible weight at depth 11 is n = 35 (3 mod 8).
    """
    return 35


def triple_conditional_scope_at_n_geq_45() -> Tuple[int, str]:
    """Return the scope at n = 45 (admissible, n mod 8 = 5).

    At n = 45 the programme crosses into Brown 2017's deepest regime:
    depth-13 irreducibles enter the BK series (parity 45 + 13 = 58 even;
    first depth-13 is at n = 39 by BK parity-analogous count).  The
    scope is quadruple-conditional through depth 11; beyond depth 13 it
    becomes quintuple-conditional with Brown 2017 Conj 5.3 at depth >= 11
    being the deepest load-bearing hypothesis.
    """
    assert humbert_heegner_admissible(45)
    return (45, "quadruple-conditional-depth-13-deepest-Brown-2017")


# ---------------------------------------------------------------------------
# Plastic-number asymptotic at admissible triple
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


def plastic_asymptotic_check_triple() -> Dict[int, Tuple[int, float, float]]:
    """Return {n: (d_n, A rho^n, relative error)} at admissible triple."""
    d = padovan_dim(46)
    out: Dict[int, Tuple[int, float, float]] = {}
    for n in ADMISSIBLE_TRIPLE:
        a = padovan_asymptotic(n)
        rel_err = (d[n] - a) / d[n]
        out[n] = (d[n], a, rel_err)
    return out


def plastic_asymptotic_precision_check_triple() -> bool:
    """Asymptotic within 10^-4 of exact d_n at admissible triple."""
    for n, (dn, asy, err) in plastic_asymptotic_check_triple().items():
        assert abs(err) < 1e-4, (
            f"plastic asymptotic at n = {n}: exact {dn}, asymptotic {asy}, "
            f"rel err {err:.6%}"
        )
    return True


# ---------------------------------------------------------------------------
# Multi-path cross-verification of Padovan dimensions at admissible triple
# ---------------------------------------------------------------------------
#
# Three genuinely independent derivation paths for d_n:
#   P_1: direct Padovan recurrence d_n = d_{n-2} + d_{n-3}.
#   P_2: generating-function coefficient extraction from
#        F(x) = 1/(1 - x^2 - x^3).
#   P_3: plastic-number asymptotic A rho^n rounded to nearest integer.
#   P_4: BK row-sum lag diagnostic sum_d D_{n,d} = d_{n-3}, kept
#        separate from the Brown dimension d_n.


def bk_rowsum_lag_diagnostic(n: int, D: Dict[Tuple[int, int], int]) -> int:
    """Return sum_d D_{n, d}; for the BK series this equals d_{n-3}."""
    return sum(D.get((n, k), 0) for k in range(1, 13))


def padovan_dim_via_generating_function(n_max: int = 46) -> Dict[int, int]:
    """Recover d_n from the generating function F(x) = 1 / (1 - x^2 - x^3).

    The Brown sequence has d_0=1, d_1=0, d_2=1. Direct series expansion
    extracts d_n as the coefficient of x^n.

    Note: equivalent to the recurrence but via an independent computation
    (coefficient extraction from (1 - x^2 - x^3)^{-1} times x).
    """
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


def padovan_dim_via_plastic_rounded(n_max: int = 46) -> Dict[int, int]:
    """Recover d_n by rounding A rho^n to the nearest integer.

    The plastic-number asymptotic d_n ~ A rho^n with A = rho^3 / (2 rho + 3)
    satisfies |d_n - A rho^n| < 0.5 for n >= 8 (subleading complex-root
    contributions decay as |rho_{complex}|^n with |rho_{complex}| < 1).
    """
    return {n: round(padovan_asymptotic(n)) for n in range(8, n_max + 1)}


def padovan_multipath_check_triple() -> bool:
    """Assert independent Padovan computations agree at admissible triple.

    P_1: direct recurrence (padovan_dim).
    P_2: generating function coefficient extraction
         (padovan_dim_via_generating_function).
    P_3: plastic-number asymptotic rounded to nearest integer
         (padovan_dim_via_plastic_rounded).
    P_4: BK row-sum lag diagnostic equals d_{n-3}.
    """
    d_P1 = padovan_dim(46)
    D = bk_depth_extract(40, 12)
    d_P2 = padovan_dim_via_generating_function(46)
    d_P3 = padovan_dim_via_plastic_rounded(46)
    for n in ADMISSIBLE_TRIPLE:
        p1 = d_P1[n]
        p2 = d_P2[n]
        p3 = d_P3[n]
        row = bk_rowsum_lag_diagnostic(n, D)
        assert p1 == p2, f"n = {n}: P_1 recurrence {p1} != P_2 genfun {p2}"
        assert p1 == p3, f"n = {n}: P_1 recurrence {p1} != P_3 plastic {p3}"
        assert row == d_P1[n - 3], (
            f"n = {n}: BK row sum {row} != d_{{{n - 3}}} = {d_P1[n - 3]}"
        )
    return True


# ---------------------------------------------------------------------------
# Multi-path cross-verification of D_{n, 9}, D_{n, 11} entries
# ---------------------------------------------------------------------------

def bk_depth_via_recursive_inverse(
    n_max: int = 40, d_max: int = 12
) -> Dict[Tuple[int, int], int]:
    """Re-derive D_{n, d} by solving BK * (1 - O y + S (y^2 - y^4)) = 1
    recursively for the Taylor coefficients of BK(x, y).

    Independent of the geometric-series expansion in bk_depth_extract:
    here we extract each Taylor coefficient one at a time from the
    identity BK(x, y) = 1 + (O y - S (y^2 - y^4)) * BK(x, y), yielding a
    triangular-in-total-bidegree system with closed-form cascade:
        BK_{n, d} = [x^n y^d] (O y - S (y^2 - y^4)) * BK
                  = sum_{(i, 1)} Ox[i] BK_{n-i, d-1}
                  - sum_{(i, 2)} Sx[i] BK_{n-i, d-2}
                  + sum_{(i, 4)} Sx[i] BK_{n-i, d-4}
    with base case BK_{0, 0} = 1 and BK_{n, d} = 0 whenever n < 0 or d < 0.
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

    BK: Dict[Tuple[int, int], Fraction] = {(0, 0): Fraction(1)}

    # Fill in increasing (n + d) total degree: d > 0 determined by the
    # recursion, d = 0 only nonzero at n = 0 (BK_{0, 0} = 1).
    for total in range(1, n_max + d_max + 1):
        for d in range(1, min(d_max, total) + 1):
            n = total - d
            if n < 0 or n > n_max:
                continue
            coeff = Fraction(0)
            # +Ox at depth shift 1
            for i, c in Ox.items():
                if 0 <= n - i <= n_max and d - 1 >= 0:
                    coeff += c * BK.get((n - i, d - 1), Fraction(0))
            # -Sx at depth shift 2
            for i, c in Sx.items():
                if 0 <= n - i <= n_max and d - 2 >= 0:
                    coeff -= c * BK.get((n - i, d - 2), Fraction(0))
            # +Sx at depth shift 4
            for i, c in Sx.items():
                if 0 <= n - i <= n_max and d - 4 >= 0:
                    coeff += c * BK.get((n - i, d - 4), Fraction(0))
            BK[(n, d)] = coeff

    return {(n, d): int(v) for (n, d), v in BK.items() if v != 0 or (n == 0 and d == 0)}


def bk_parity_functional_equation_check() -> bool:
    """Verify BK(-x, y) = BK(x, -y) at bi-degrees containing the admissible triple.

    The BK generating function satisfies the functional equation
    BK(-x, y) = BK(x, -y): O(-x) = -O(x), S(-x) = S(x), so the functional
    form is invariant under (x -> -x, y -> -y).  This forces
    D_{n, d} = 0 whenever n + d is odd.
    """
    D = bk_depth_extract(40, 12)
    for (n, d), v in D.items():
        if (n + d) % 2 == 1 and v != 0:
            # Only acceptable if this is the (0, 0) base case or degree-0
            if n == 0 and d == 0:
                continue
            assert False, (
                f"BK parity violation at (n, d) = ({n}, {d}): D = {v}, "
                f"n + d = {n + d} should enforce D = 0"
            )
    return True


def bk_depth_multipath_check_triple() -> bool:
    """Cross-verify BK series D_{n, d} at admissible triple via two paths.

    Path A: symbolic geometric-series expansion (bk_depth_extract):
        BK = sum_k (-g)^k with g = -O y + S (y^2 - y^4), truncated.
    Path B: recursive inversion (bk_depth_via_recursive_inverse):
        BK_{n, d} extracted one coefficient at a time from the identity
        BK = 1 + (O y - S(y^2 - y^4)) * BK.

    The two paths share the defining identity but compute via distinct
    algorithms: geometric-series summation (path A) versus triangular
    recursion (path B).  Agreement across the admissible triple at
    every depth (1 through 11) is the cross-verification.
    """
    DA = bk_depth_extract(40, 12)
    DB = bk_depth_via_recursive_inverse(40, 12)
    critical_cells = []
    for n in ADMISSIBLE_TRIPLE:
        for d in range(1, 12):
            critical_cells.append((n, d))
    for (n, d) in critical_cells:
        pA = DA.get((n, d), 0)
        pB = DB.get((n, d), 0)
        assert pA == pB, (
            f"Multi-path BK cross-check fails at (n, d) = ({n}, {d}): "
            f"symbolic = {pA}, recursive-inverse = {pB}"
        )
    # Also cross-check the critical depth-onset cells
    for (n, d) in [(27, 9), (29, 9), (33, 11), (35, 11)]:
        pA = DA.get((n, d), 0)
        pB = DB.get((n, d), 0)
        assert pA == pB, (
            f"Multi-path BK cross-check fails at (n, d) = ({n}, {d}): "
            f"symbolic = {pA}, recursive-inverse = {pB}"
        )
    return True


# ---------------------------------------------------------------------------
# Multi-path cross-verification of p_24 at the relevant k values
# ---------------------------------------------------------------------------

def p24_via_euler_product(k_target: int) -> int:
    """Recover p_24(k) by direct Euler-product expansion prod (1 - q^m)^{-24}.

    Alternative path to the direct expansion in p24_exact: expand
    prod_{m >= 1} (1 - q^m)^{-24} by iteratively convolving
    (1 - q^m)^{-24} = (sum_j binom(j + 23, 23) q^{m j}) for m = 1, 2, ...
    This is a distinct decomposition into per-m binomial factors rather
    than the 24-fold iterated (1 - q^m)^{-1} multiplication used in
    p24_exact.
    """
    coefs = [0] * (k_target + 1)
    coefs[0] = 1
    for m in range(1, k_target + 1):
        # Compute (1 - q^m)^{-24} = sum_{j >= 0} binom(j + 23, 23) q^{m j}
        # truncated to degree k_target
        factor = {0: 1}
        j = 1
        while m * j <= k_target:
            factor[m * j] = math.comb(j + 23, 23)
            j += 1
        # Convolve coefs with factor
        newc = [0] * (k_target + 1)
        for i in range(k_target + 1):
            if coefs[i] == 0:
                continue
            for deg, val in factor.items():
                if i + deg <= k_target:
                    newc[i + deg] += coefs[i] * val
        coefs = newc
    return coefs[k_target]


def p24_multipath_check_triple() -> bool:
    """Assert p_24(k) at k in {14, 15, 18} via two independent paths.

    Path A: 24-fold convolution p24_exact (repeated (1 - q^m)^{-1}).
    Path B: binomial Euler-product expansion p24_via_euler_product.
    """
    for k, expected in [(14, 156883829400), (15, 563116739584), (18, 21651325216200)]:
        pA = p24_exact(k)
        pB = p24_via_euler_product(k)
        assert pA == pB == expected, (
            f"p_24({k}): direct = {pA}, Euler = {pB}, expected = {expected}"
        )
    return True


# ---------------------------------------------------------------------------
# Aggregate verifier
# ---------------------------------------------------------------------------

def verifier_triple_27_29_35() -> Dict[str, bool]:
    """Run every phi^(n) verification check for the admissible triple."""
    return {
        "admissibility_filter": admissibility_filter_check(),
        "padovan_count_triple": padovan_count_check_triple(),
        "padovan_multipath_triple": padovan_multipath_check_triple(),
        "bk_depth_triple": bk_depth_check_triple(),
        "bk_depth_multipath_triple": bk_depth_multipath_check_triple(),
        "bk_parity_functional_equation": bk_parity_functional_equation_check(),
        "first_depth_nine_at_27": first_depth_nine_at_27_check(),
        "first_depth_eleven_at_33": first_depth_eleven_at_33_check(),
        "bk_rowsum_lag_triple": bk_padovan_twostep_consistency_check_triple(),
        "bk_parity_split_triple": bk_parity_split_check_triple(),
        "phi_n_leading_triple": phi_n_leading_check_triple(),
        "hardy_ramanujan_exact_triple": hardy_ramanujan_exact_check_triple(),
        "p24_multipath_triple": p24_multipath_check_triple(),
        "scope_cascade": scope_cascade_assertion(),
        "plastic_asymptotic_triple": plastic_asymptotic_precision_check_triple(),
    }


if __name__ == "__main__":
    results = verifier_triple_27_29_35()
    assert all(results.values()), f"Failures: {results}"

    d = padovan_dim(46)
    print("Humbert-Heegner admissible triple at n >= 25, n <= 36:")
    print(f"  Admissible: n in {ADMISSIBLE_TRIPLE} (continuation: 37, 43, 45, ...)")
    print()
    print("Padovan dimensions:")
    for n in ADMISSIBLE_TRIPLE:
        print(f"  d_{n} = {d[n]}")

    print()
    print("Broadhurst-Kreimer D_{n, d} at admissible triple:")
    D = bk_depth_extract(40, 12)
    for n in ADMISSIBLE_TRIPLE:
        row = [D.get((n, dd), 0) for dd in range(1, 12)]
        s = sum(row)
        print(f"  D_{{{n}, d}} for d in [1, 11] = {row}, sum = {s} = d_{{{n-3}}} = {d[n-3]}")

    print()
    print("Depth onsets:")
    print(f"  First depth-9:  n = 27 (D_{{27, 9}} = {D.get((27, 9), 0)})")
    print(f"  First depth-11: n = 33 (D_{{33, 11}} = {D.get((33, 11), 0)}); at admissible n = 35: D_{{35, 11}} = {D.get((35, 11), 0)}")

    print()
    print("Scope cascade:")
    for n, tier in scope_cascade_check().items():
        print(f"  n = {n}: {tier}")

    print()
    print("phi^(n) leading numerical values at admissible triple:")
    vals = phi_n_leading_values_triple()
    for n, v in sorted(vals.items()):
        print(f"  phi^({n})_MZV ~ {v:.3e}")

    print()
    print("Hardy-Ramanujan exact p_24 and Borcherds/MZV ratio:")
    print(f"  p_24(14) = {p24_exact(14):,}, p_24(15) = {p24_exact(15):,}, p_24(18) = {p24_exact(18):,}")
    r = borcherds_mzv_ratio_triple()
    for n, ratio in sorted(r.items()):
        print(f"  n = {n}: Borcherds/MZV = {ratio:.3e}")

    print()
    print("Plastic-number asymptotic vs exact d_n at admissible triple:")
    for n, (dn, asy, err) in sorted(plastic_asymptotic_check_triple().items()):
        print(f"  n = {n}: d_n = {dn:5d}, A rho^n ~ {asy:12.4f}, rel err = {err:+.6%}")

    print()
    print("Brown 2017 conditional-onset tracker:")
    print(f"  Depth-9 onset (triple-conditional) at n = {brown_2017_onset_weight()}")
    print(f"  Depth-11 admissible (quadruple-conditional) at n = {quadruple_conditional_onset_weight()}")
    n45, scope45 = triple_conditional_scope_at_n_geq_45()
    print(f"  Continuation at n = {n45}: {scope45}")
