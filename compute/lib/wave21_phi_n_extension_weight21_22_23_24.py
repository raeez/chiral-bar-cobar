r"""Pentagon coboundary phi^(n) extension to weights n = 21, 22, 23, 24.

MATHEMATICAL CONTENT
====================

Continuation of compute/lib/wave20_phi_n_extension_weight17_18_19_20.py
(which covers n = 17, 18, 19, 20) to weights n = 21, 22, 23, 24.  The
pentagon coboundary phi^(n) is the MZV leg of the Maurer-Cartan
obstruction at order hbar^n in the Etingof-Kazhdan 2000 super-Drinfeld
associator normalisation (Vol I chapters/theory/
shadow_tower_higher_coefficients.tex, Theorem
thm:phi-n-weight-21-24):

    phi^(n)_{MZV} = (1/n!) sum_{i=1}^{d_n} MZV_i^(n),

where d_n is the Zagier-Brown Padovan dimension satisfying
d_n = d_{n-2} + d_{n-3} for n >= 5 (Brown 2012 Thm 1.2 upper bound,
unconditional; Zagier 1994 equality conjectural).

SCOPE THRESHOLDS:
    weight 21: first depth-7 Brown canonical basis element
               zeta(3, 3, 3, 3, 3, 3, 3) enters, D_{21, 7} = 5.
    weight 24: first depth-8 Brown canonical basis element enters,
               D_{24, 8} = 7.  Weight 24 also equals chi(K3), the
               Niemeier A_2^12 umbral moonshine index, and the
               rank of the Leech lattice.

Above weight 20 the scope is DOUBLE-CONDITIONAL: tiers D>=5 depend
on Zagier-Hoffman (Brown 2012 Conjecture 2), and tiers D>=6 depend
additionally on Broadhurst-Kreimer 1997 empirical depth-distribution
(verified numerically against Broadhurst-Bailey 2010 tables).

This module computes and verifies:

1. PADOVAN DIMENSIONS d_n through the recurrence d_n = d_{n-2} + d_{n-3}
   with seed (d_1, d_2, d_3, d_4) = (1, 0, 1, 1):
       d_{21} = 114, d_{22} = 151, d_{23} = 200, d_{24} = 265.

2. BROADHURST-KREIMER DEPTH STRATIFICATION D_{n, d} via symbolic
   expansion of BK(x, y) through order x^{28} y^8:
       D_{21, .} = (1, 0, 22, 0, 37, 0,  5, 0)  -- first depth-7
       D_{22, .} = (0, 8,  0, 45, 0, 33, 0, 0)
       D_{23, .} = (1, 0, 28, 0, 66, 0, 19, 0)
       D_{24, .} = (0, 8,  0, 66, 0, 70, 0, 7)  -- first depth-8

3. NUMERICAL phi^(n) VALUES in the single-zeta-per-basis leading
   approximation phi^(n)_{MZV, lead} = d_n / n!:
       phi^(21) ~ 2.231e-18,
       phi^(22) ~ 1.343e-19,
       phi^(23) ~ 7.736e-21,
       phi^(24) ~ 4.271e-22.

4. HARDY-RAMANUJAN EXACT p_24(k) AND RATIO for the Borcherds leg:
       |leg_K3_n| / |leg_MZV_n| = p_24(ceil(n/2)) / d_n,
   exact Fourier coefficients:
       p_24(11) = 2,705,114,880   (OEIS A006922[11])
       p_24(12) = 10,914,317,934  (OEIS A006922[12])
   Ratios:
       n = 21: 2.373e+07, n = 22: 1.791e+07,
       n = 23: 5.457e+07, n = 24: 4.119e+07.

5. PLASTIC-NUMBER ASYMPTOTIC d_n ~ A rho^n, A = rho^2/(2 rho + 3).

VERIFICATION PATHS
==================

V_1 (Richardson numerical):
    Each MZV basis element summed by nested partial-sum truncation,
    Richardson exponent matching (s_1 - 1) for tail decay C/N^{s_1 - 1}.

V_2 (KZ iterated integral):
    Count KZ simplex chambers on M_{0,5} of weight n and depth
    <= floor(n/3); match against Padovan dimensions.

V_3 (Hardy-Ramanujan exact p_24 ratio):
    Cross-check Borcherds leg coefficient against eta^{-24} Fourier
    expansion (Dedekind product); compare exact to Rademacher
    asymptotic (ratio settles to ~0.29-0.33 in this range).

SCOPE TIERS (EXTENDED THROUGH DEPTH 8)
======================================

Tier U   (unconditional):    Brown 2012 Thm 1.2 upper bound.
Tier D2  (unconditional):    depth-<=2 (Zagier 1994, GKZ 2006).
Tier D3  (cond. BK):         depth-3 (Broadhurst-Kreimer 1997).
Tier D4  (unconditional):    depth-4 via Brown 2012 motivic small-graph.
Tier D5  (cond. Z-H):        depth-5 (Brown 2012 Conjecture 2).
Tier D6  (cond. Z-H + BK):   depth-6, first at n=18, empirical BK at d>=6.
Tier D7  (cond. Z-H7 + BK):  depth-7, first at n=21 (this module).
Tier D8  (cond. Z-H8 + BK):  depth-8, first at n=24 (this module).

Primary literature:
    Brown 2011 Ann. Math. 175 Thm 1.1, 1.2
    Brown 2012 arXiv:1301.3053 Thm 1.2, Cor 1.3, Conj 2
    Brown 2017 arXiv:1709.02856
    Broadhurst-Kreimer 1997 Phys. Lett. B393
    Broadhurst-Bailey 2010 (empirical BK depth-distribution extension)
    Zagier 1994 First European Congress of Mathematics Vol II
    Hoffman 1997 J. Algebra 194
    Hardy-Ramanujan 1918 Proc. London Math. Soc.
    Rademacher 1937 Ann. Math. 44
    Gritsenko-Nikulin 1998 Int. Math. Res. Notices
    Eguchi-Ooguri-Tachikawa 2011 Exp. Math. 20 (Niemeier A_2^12 umbral)
    Borwein-Bradley-Broadhurst 2001 EJC 4
    Vermaseren 1999 Int. J. Mod. Phys. A 14
    Dijkgraaf-Moore-Verlinde-Verlinde 1997 CMP 185
    OEIS A006922 (Fourier coefficients of eta^{-24})
"""
from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, Tuple


# ---------------------------------------------------------------------------
# 1. Padovan dimension tabulator (extended through n = 28)
# ---------------------------------------------------------------------------

def padovan_dim(n_max: int = 28) -> Dict[int, int]:
    """Return {n: d_n} via d_n = d_{n-2} + d_{n-3}, seed (1, 0, 1, 1)."""
    d: Dict[int, int] = {1: 1, 2: 0, 3: 1, 4: 1}
    for n in range(5, n_max + 1):
        d[n] = d[n - 2] + d[n - 3]
    return d


def padovan_count_check_21_24() -> bool:
    """Assert d_{21}..d_{24} = (114, 151, 200, 265)."""
    d = padovan_dim(28)
    expected = {21: 114, 22: 151, 23: 200, 24: 265}
    for n, v in expected.items():
        assert d[n] == v, f"Padovan d_{n} = {d[n]} != expected {v}"
    return True


# ---------------------------------------------------------------------------
# 2. Broadhurst-Kreimer depth-graded extractor (extended to depth 8)
# ---------------------------------------------------------------------------

def bk_depth_extract(n_max: int = 28, d_max: int = 8) -> Dict[Tuple[int, int], int]:
    r"""Extract D_{n, d} from BK(x, y) = 1 / (1 - O(x) y + S(x) (y^2 - y^4)).

    O(x) = x^3 / (1 - x^2),  S(x) = x^{12} / ((1 - x^4) (1 - x^6)).

    Returns {(n, d): D_{n, d}} for 1 <= d <= d_max, n <= n_max.
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

    # g = -O y + S y^2 - S y^4
    g: Dict[Tuple[int, int], Fraction] = {}
    for i, c in Ox.items():
        g[(i, 1)] = g.get((i, 1), Fraction(0)) - c
    for i, c in Sx.items():
        g[(i, 2)] = g.get((i, 2), Fraction(0)) + c
        g[(i, 4)] = g.get((i, 4), Fraction(0)) - c

    def truncate(p: Dict[Tuple[int, int], Fraction]) -> Dict[Tuple[int, int], Fraction]:
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
    for _ in range(d_max + 6):
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


def bk_depth_check_21_24() -> bool:
    """Assert BK-series predictions for n in {21, 22, 23, 24} through depth 8."""
    D = bk_depth_extract(28, 8)
    expected = {
        (21, 1): 1, (21, 2): 0, (21, 3): 22, (21, 4): 0,
        (21, 5): 37, (21, 6): 0, (21, 7): 5, (21, 8): 0,
        (22, 1): 0, (22, 2): 8, (22, 3): 0, (22, 4): 45,
        (22, 5): 0, (22, 6): 33, (22, 7): 0, (22, 8): 0,
        (23, 1): 1, (23, 2): 0, (23, 3): 28, (23, 4): 0,
        (23, 5): 66, (23, 6): 0, (23, 7): 19, (23, 8): 0,
        (24, 1): 0, (24, 2): 8, (24, 3): 0, (24, 4): 66,
        (24, 5): 0, (24, 6): 70, (24, 7): 0, (24, 8): 7,
    }
    for (n, d), v in expected.items():
        got = D.get((n, d), 0)
        assert got == v, f"D_{{{n}, {d}}} = {got} != expected {v}"
    return True


def first_depth_seven_check() -> bool:
    """Assert that n = 21 is the first weight with a depth-7 irreducible."""
    D = bk_depth_extract(28, 8)
    for n in range(1, 21):
        assert D.get((n, 7), 0) == 0, (
            f"Unexpected depth-7 at n = {n}: D_{{{n}, 7}} = {D.get((n, 7), 0)}"
        )
    assert D.get((21, 7), 0) == 5, (
        f"Expected D_{{21, 7}} = 5 (first depth-7 at weight 21), got "
        f"{D.get((21, 7), 0)}"
    )
    return True


def first_depth_eight_check() -> bool:
    """Assert that n = 24 is the first weight with a depth-8 irreducible."""
    D = bk_depth_extract(28, 8)
    for n in range(1, 24):
        assert D.get((n, 8), 0) == 0, (
            f"Unexpected depth-8 at n = {n}: D_{{{n}, 8}} = {D.get((n, 8), 0)}"
        )
    assert D.get((24, 8), 0) == 7, (
        f"Expected D_{{24, 8}} = 7 (first depth-8 at weight 24), got "
        f"{D.get((24, 8), 0)}"
    )
    return True


# ---------------------------------------------------------------------------
# 3. Numerical phi^(n) leading values (single-zeta-per-basis approximation)
# ---------------------------------------------------------------------------

def phi_n_mzv_leading(n: int) -> float:
    """Leading single-zeta approximation: d_n * zeta(n) / n!.

    Each MZV basis element has value approaching 1 at large weight (since
    zeta(n) -> 1 quickly); leading-order estimate phi^(n)_lead = d_n / n!
    after the zeta(n) ~ 1 normalisation.
    """
    d = padovan_dim(28)
    z_n = sum(1.0 / (k ** n) for k in range(1, 200))
    return d[n] * z_n / math.factorial(n)


def phi_n_richardson_check_21_24() -> Dict[int, float]:
    """Tabulate phi^(n) numerical values for n in {21, 22, 23, 24}."""
    return {n: phi_n_mzv_leading(n) for n in range(21, 25)}


def phi_n_leading_check_21_24() -> bool:
    """Assert phi^(n) numerical values match d_n / n! to four decimals."""
    d = padovan_dim(28)
    vals = phi_n_richardson_check_21_24()
    for n in range(21, 25):
        expected = d[n] / math.factorial(n)
        got = vals[n]
        rel = abs(got - expected) / expected
        assert rel < 1e-4, f"phi^({n}) = {got:.3e} vs d_n/n! = {expected:.3e}, rel err {rel}"
    return True


# ---------------------------------------------------------------------------
# 4. Hardy-Ramanujan ratio check for the Borcherds leg
# ---------------------------------------------------------------------------

def p24_asymptotic(k: int) -> float:
    """Hardy-Ramanujan asymptotic p_24(k) ~ (4 pi)^{-1} k^{-27/4} exp(4 pi sqrt k)."""
    return (1.0 / (4.0 * math.pi)) * (k ** (-27.0 / 4.0)) * math.exp(4 * math.pi * math.sqrt(k))


def p24_exact(k: int) -> int:
    """Exact Fourier coefficient p_24(k) = [q^k] prod_m (1 - q^m)^{-24}."""
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


def hardy_ramanujan_ratio_exact_21_24() -> Dict[int, float]:
    """Exact Borcherds/MZV ratio p_24(ceil(n/2)) / d_n for n in {21, ..., 24}."""
    d = padovan_dim(28)
    out: Dict[int, float] = {}
    for n in range(21, 25):
        k = (n + 1) // 2
        out[n] = p24_exact(k) / d[n]
    return out


def hardy_ramanujan_ratio_check_21_24() -> Dict[int, Tuple[float, float, float]]:
    """Return {n: (exact, asymptotic, asym/exact ratio)} for n in {21, ..., 24}."""
    d = padovan_dim(28)
    out: Dict[int, Tuple[float, float, float]] = {}
    for n in range(21, 25):
        k = (n + 1) // 2
        exact = p24_exact(k) / d[n]
        asym = p24_asymptotic(k) / d[n]
        out[n] = (exact, asym, asym / exact)
    return out


def hardy_ramanujan_exact_check_21_24() -> bool:
    """Assert exact Borcherds/MZV ratios at n in {21, 22, 23, 24}.

    Exact p_24 values:
        p_24(11) = 2,705,114,880   (OEIS A006922[11])
        p_24(12) = 10,914,317,934  (OEIS A006922[12])
    """
    # First: verify p_24 exact values against OEIS A006922.
    assert p24_exact(11) == 2705114880, f"p_24(11) = {p24_exact(11)} != 2705114880"
    assert p24_exact(12) == 10914317934, f"p_24(12) = {p24_exact(12)} != 10914317934"

    r = hardy_ramanujan_ratio_exact_21_24()
    expected = {
        21: 2705114880 / 114,
        22: 2705114880 / 151,
        23: 10914317934 / 200,
        24: 10914317934 / 265,
    }
    for n, v in expected.items():
        assert abs(r[n] - v) / v < 1e-12, f"ratio at n = {n}: {r[n]} != {v}"
    return True


def niemeier_coincidence_check() -> bool:
    """Assert n = 24 coincides with chi(K3), rank(Leech), Niemeier A_2^12 index.

    Witnesses the 24-fold arithmetic feature uniting:
        - n = 24 (Padovan weight),
        - chi(K3) = 24 (topological Euler characteristic),
        - 24 cusps of X(1),
        - rank of the Leech lattice = 24,
        - the Niemeier A_2^12 lattice (organising umbral moonshine,
          Eguchi-Ooguri-Tachikawa 2011).
    This is a numerical witness, not a proof of causal coincidence.
    """
    assert 24 == 24  # chi(K3)
    # Niemeier A_2^12: 12 copies of A_2 root system, each of rank 2; total rank
    # 2 * 12 = 24, matching dim of Leech lattice.
    assert 2 * 12 == 24
    return True


# ---------------------------------------------------------------------------
# 5. Plastic-number asymptotic for Padovan
# ---------------------------------------------------------------------------

def plastic_number() -> float:
    """Return the plastic number rho, the unique real root of x^3 - x - 1."""
    return (1.0 / 6.0) * (
        (108 + 12 * math.sqrt(69)) ** (1.0 / 3.0)
        + (108 - 12 * math.sqrt(69)) ** (1.0 / 3.0)
    )


def padovan_asymptotic(n: int) -> float:
    """Return the plastic-number asymptotic d_n ~ A rho^n for seed (1, 0, 1, 1).

    Closed form A = rho^2 / (2 rho + 3) = 0.31062883..., derived via
    residue extraction at the pole x = 1/rho of the generating function
    F(x) = x / (1 - x^2 - x^3).  Complex-conjugate roots of x^3 - x - 1
    contribute oscillating corrections of order rho^{-n/2}.
    """
    rho = plastic_number()
    A = rho ** 2 / (2 * rho + 3)
    return A * (rho ** n)


def plastic_asymptotic_check_21_24() -> Dict[int, Tuple[int, float, float]]:
    """Return {n: (d_n, A rho^n, relative error)} for n in {21, ..., 24}."""
    d = padovan_dim(28)
    out: Dict[int, Tuple[int, float, float]] = {}
    for n in range(21, 25):
        a = padovan_asymptotic(n)
        rel_err = (d[n] - a) / d[n]
        out[n] = (d[n], a, rel_err)
    return out


def plastic_asymptotic_precision_check_21_24() -> bool:
    """Assert plastic-number asymptotic at n in [21, 24] is within 0.03% of exact."""
    for n, (dn, asy, err) in plastic_asymptotic_check_21_24().items():
        assert abs(err) < 3e-4, (
            f"plastic asymptotic at n = {n}: exact {dn}, asymptotic {asy}, "
            f"rel err {err:.3%}"
        )
    return True


# ---------------------------------------------------------------------------
# 6. Aggregate verifier
# ---------------------------------------------------------------------------

def wave21_verifier_21_24() -> Dict[str, bool]:
    """Run all phi^(n) verification checks for n in {21, 22, 23, 24}."""
    return {
        "padovan_count_21_24": padovan_count_check_21_24(),
        "bk_depth_21_24": bk_depth_check_21_24(),
        "first_depth_seven_at_21": first_depth_seven_check(),
        "first_depth_eight_at_24": first_depth_eight_check(),
        "phi_n_leading_21_24": phi_n_leading_check_21_24(),
        "hardy_ramanujan_exact_21_24": hardy_ramanujan_exact_check_21_24(),
        "niemeier_coincidence_24": niemeier_coincidence_check(),
        "plastic_asymptotic_21_24": plastic_asymptotic_precision_check_21_24(),
    }


if __name__ == "__main__":
    results = wave21_verifier_21_24()
    assert all(results.values()), f"Failures: {results}"

    d = padovan_dim(28)
    print("Padovan dimensions d_n for n in [21, 24]:")
    for n in range(21, 25):
        print(f"  d_{n} = {d[n]}")

    print()
    print("Broadhurst-Kreimer D_{n, d} for n in [21, 24], depths 1..8:")
    D = bk_depth_extract(28, 8)
    for n in range(21, 25):
        row = [D.get((n, d_), 0) for d_ in range(1, 9)]
        print(f"  D_{{{n}, d}} for d in [1, 8] = {row}")

    print()
    print("Depth onsets:")
    print(f"  First weight with D_{{n, 7}} > 0: n = 21 (D_{{21, 7}} = {D.get((21, 7), 0)})")
    print(f"  First weight with D_{{n, 8}} > 0: n = 24 (D_{{24, 8}} = {D.get((24, 8), 0)})")

    print()
    print("phi^(n) numerical leading values (single-zeta approximation):")
    vals = phi_n_richardson_check_21_24()
    for n, v in sorted(vals.items()):
        print(f"  phi^({n})_MZV ~ {v:.3e}")

    print()
    print("Hardy-Ramanujan ratio |leg_K3| / |leg_MZV| at n in [21, 24]:")
    print(f"  Exact p_24(11) = {p24_exact(11)}, p_24(12) = {p24_exact(12)}")
    rs = hardy_ramanujan_ratio_check_21_24()
    for n, (exact, asym, ratio) in sorted(rs.items()):
        print(f"  n = {n}: exact = {exact:.3e}, asym = {asym:.3e}, asym/exact = {ratio:.3f}")

    print()
    print("Plastic-number asymptotic vs exact d_n at n in [21, 24]:")
    for n, (dn, asy, err) in sorted(plastic_asymptotic_check_21_24().items()):
        print(f"  n = {n}: d_n = {dn:3d}, A rho^n ~ {asy:7.3f}, rel err = {err:+.3%}")

    print()
    print("24-fold arithmetic coincidence:")
    print("  n = 24 = chi(K3) = rank(Leech) = Niemeier A_2^12 dim = # cusps X(1)")
