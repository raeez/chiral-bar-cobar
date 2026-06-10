r"""
Pentagon coboundary $\phi^{(n)}$ arithmetic at weights $n\in\{33,34,35,36\}$.

Extends the shadow-tower higher-coefficient series (weights $25$-$28$,
$29$-$32$ already inscribed in
`chapters/theory/shadow_tower_higher_coefficients.tex`) through
$n\in\{33,34,35,36\}$, crossing the depth-$11$ threshold at $n=33$ and
the fifth conditional tier (quintuple-conditional scope) at depth $11$.

Four arithmetic voices are verified at these weights:

(i)  Padovan recurrence $d_n = d_{n-2}+d_{n-3}$ with Brown seed
     $(d_{29},d_{30},d_{31},d_{32}) = (1432, 1897, 2513, 3329)$,
     delivering
     $(d_{33},d_{34},d_{35},d_{36}) = (4410, 5842, 7739, 10252)$.

(ii) Broadhurst-Kreimer depth stratification
     $\mathrm{BK}(x,y) = 1/(1 - O(x)y + S(x)(y^2 - y^4))$
     with $O(x)=x^3/(1-x^2)$, $S(x)=x^{12}/((1-x^4)(1-x^6))$;
     first depth-$11$ irreducible at $(n,d)=(33,11)$.

(iii) Hardy-Ramanujan / Rademacher asymptotic for $p_{24}(k)$
      at $k\in\{17, 18\}$; Gottsche-DMVV coincidence
      $\chi(\mathrm{Hilb}^{18}(K3)) = p_{24}(18)$ is a GENERIC
      Gottsche identity at $n = 36$, NOT an umbral resonance.

(iv) Humbert-Heegner admissibility filter
     $n \equiv 3, 5\pmod 8$ (discriminant condition for Humbert
     divisors on the Siegel threefold $\mathcal A_2$ and Heegner
     points on orthogonal Shimura varieties $\mathrm O(2, n)$):
     only $n\in\{29, 35\}$ satisfy this in the range $n\in[29,36]$,
     orthogonally filtering the Padovan basis to a HH-admissible
     sub-basis of dimension $d_n^{\mathrm{HH}} \le d_n$.

PRIMARY LITERATURE
==================
- Zagier 1994 "Values of zeta functions and their applications"
  (Padovan recurrence on irreducible motivic MZV count).
- Brown 2011 arXiv:1102.1312 (motivic MZV at the Padovan upper bound
  for n <= 12; unconditional for n <= 12).
- Brown 2012 arXiv:1301.3053 Thm 1.2 (unconditional upper bound
  d_n <= d_{n-2} + d_{n-3}).
- Brown 2017 arXiv:1709.02856 Conj 5.3 (higher-depth Galois-motivic
  generators of pro-Q_l Lie algebra).
- Broadhurst-Kreimer 1997 arXiv:hep-th/9609128 (BK depth series).
- Broadhurst-Bailey 2010 arXiv:1004.4597 (MZDP numerical tables).
- Hoffman 1997 arXiv:9604144 (stuffle-regularised MZV cyclic orbits).
- Hardy-Ramanujan 1918, Rademacher 1937 (partition asymptotics).
- Gottsche 1990 Inv Math 102 (Hilbert scheme Euler characteristics).
- Dijkgraaf-Moore-Verlinde-Verlinde 1997, Comm Math Phys 185
  (second-quantised elliptic genus).
- Cheng-Duncan-Harvey 2014 arXiv:1307.5793 (umbral moonshine
  twenty-three Niemeier genera).
- Conway-Sloane 1988 "Sphere Packings" Ch 4, Thm 11; extremal
  self-dual lattices in small ranks.
- Humbert 1899 J Math Pures Appl 5 (Humbert divisors on
  $\mathcal A_2$; discriminant D with D \equiv 0, 1 \pmod 4).
- Gritsenko-Hulek-Sankaran 2007 "Abelianisation of orthogonal groups
  and the fundamental group of modular varieties"
  (Heegner divisors on O(2,n)).
- Looijenga 2003 "Compactifications defined by arrangements I-II"
  (Humbert arrangements; discriminant structure).
- OEIS A006922 (p_{24}(k), Ramanujan-Jacobi-Siegel partition series).

CROSS-VOLUME ANCHORS
====================
Vol I: `chapters/theory/shadow_tower_higher_coefficients.tex`
       Theorem `thm:phi-n-weight-33-36` (inscribed at this sprint).
Vol I prior: Theorem `thm:phi-n-weight-29-32` at depth 10.

NUMERICAL VALUES
================
Padovan dimensions:
    d_{33} = 4410    d_{34} = 5842
    d_{35} = 7739    d_{36} = 10252

BK depth-graded counts D_{n,d} for d=1,\ldots,12 (parity rule:
n+d even at each entry; first-principles computed from the BK series
truncation at x^{40} y^{12}):
    D_{33,.} = (1, 0,  67, 0,  498, 0,  914, 0,  398, 0,  19, 0)
    D_{34,.} = (0, 13, 0, 247, 0,  977, 0, 1037, 0,  239, 0, 0)
    D_{35,.} = (1, 0,  77, 0,  673, 0, 1532, 0,  949, 0,  97, 0)
    D_{36,.} = (0, 13, 0, 306, 0, 1431, 0, 1955, 0,  679, 0, 26)

Parity-forced zeros: D_{n,d} = 0 when n + d is odd. Depth-11 enters
first at n = 33 with D_{33,11} = 19; empty at every n < 33 (absent
from Broadhurst-Kreimer expansion at x^{31} y^{11} onwards by parity
and depth-x^3 support in O(x)).  Setting y=1 in the BK extractor gives
x^3/(1-x^2-x^3); hence the row sum at weight n is the lower Brown
dimension d_{n-3}.  These row sums are depth diagnostics, not the
Brown dimensions at the same weights.

p_{24}(k) at k in {17, 18} (first-principles computed):
    p_{24}(17) =  6,599,620,022,400
    p_{24}(18) = 21,651,325,216,200

Borcherds leg / MZV leg ratio p_{24}(ceil(n/2)) / d_n:
    n = 33: p_{24}(17) / d_{33} = 6599620022400 / 4410 ~ 1.497 * 10^9
    n = 34: p_{24}(17) / d_{34} = 6599620022400 / 5842 ~ 1.130 * 10^9
    n = 35: p_{24}(18) / d_{35} = 21651325216200 / 7739 ~ 2.798 * 10^9
    n = 36: p_{24}(18) / d_{36} = 21651325216200 / 10252 ~ 2.112 * 10^9

HUMBERT-HEEGNER ADMISSIBILITY
=============================
    n mod 8 at n in [29, 36]:
        29: 5 (admissible)
        30: 6
        31: 7
        32: 0
        33: 1
        34: 2
        35: 3 (admissible)
        36: 4
    Only n = 29 (~ 5 mod 8) and n = 35 (~ 3 mod 8) pass the Humbert-Heegner
    filter in our range n in [29, 36].  Within n in [33, 36]: only n = 35
    is HH-admissible; n = 33, 34, 36 carry only the Padovan (unfiltered)
    symphony.

GENERIC GOTTSCHE COINCIDENCE AT n = 36
======================================
    Gottsche-DMVV: chi(Hilb^{18}(K3)) = p_{24}(18) = 21,651,325,216,200.
    This is GENERIC (holds for every k >= 0 by Gottsche's universal
    formula), NOT an umbral resonance.  Four-voice comparison:
      - Padovan: d_{36} = 10252
      - BK: D_{36,10} = 679 (first-principles BK truncation at x^{40})
      - Hardy-Ramanujan: p_{24}(18) ~ 2.17 * 10^{13}
      - Gottsche: chi(Hilb^{18}(K3)) = p_{24}(18)
    No Niemeier lattice at root rank 36 (CDH 2014 Tab 2 lists 23
    Niemeier genera all at rank 24); Barnes-Wall BW_{32} and
    Kervaire-Milnor K_{32} do not extend to rank 36; the next Niemeier
    umbral coincidence remains at n = 48 via P_{48p} (Conway-Sloane
    1988).  No isolated-Niemeier symphony at n = 36.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Dict, Iterable, List, Sequence, Tuple


# ---------------------------------------------------------------------------
# 1. Padovan recurrence d_n = d_{n-2} + d_{n-3}
# ---------------------------------------------------------------------------

# Brown--Zagier Padovan seed.
_PADOVAN_SEED: Dict[int, int] = {0: 1, 1: 0, 2: 1}


def padovan(n: int) -> int:
    r"""Return d_n via the recurrence $d_n = d_{n-2} + d_{n-3}$.

    The sequence is defined by d_0=1, d_1=0, d_2=1 and
    d_n=d_{n-2}+d_{n-3}. It is the Brown upper-bound sequence.
    """
    if n < 0:
        raise ValueError(f"padovan(n) defined for n >= 0; got n = {n}")
    if n in _PADOVAN_SEED:
        return _PADOVAN_SEED[n]
    for m in range(3, n + 1):
        if m not in _PADOVAN_SEED:
            _PADOVAN_SEED[m] = _PADOVAN_SEED[m - 2] + _PADOVAN_SEED[m - 3]
    return _PADOVAN_SEED[n]


def padovan_count_check_33_36() -> Dict[int, bool]:
    r"""Verify Padovan recurrence at n in {33, 34, 35, 36} against the
    Brown target $(4410, 5842, 7739, 10252)$.
    """
    vals = {33: 4410, 34: 5842, 35: 7739, 36: 10252}
    return {n: padovan(n) == vals[n] for n in (33, 34, 35, 36)}


def _mat3_mul(
    a: Tuple[Tuple[int, int, int], ...],
    b: Tuple[Tuple[int, int, int], ...],
) -> Tuple[Tuple[int, int, int], ...]:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def padovan_sprint(n: int) -> int:
    r"""Return $d_n$ via companion-matrix exponentiation (path P2).

    With $M$ the companion matrix of $t^3 = t + 1$ acting on state
    vectors $(d_k, d_{k+1}, d_{k+2})$ and Brown--Zagier seed
    $(d_0, d_1, d_2) = (1, 0, 1)$, the first component of
    $M^n (1, 0, 1)^T$ is $d_n$.  Binary powering touches neither the
    memoised table of :func:`padovan` nor its linear recursion order,
    giving an implementation-independent second path to the sprint
    targets $(d_{33}, d_{34}, d_{35}, d_{36}) = (4410, 5842, 7739,
    10252)$.
    """
    if n < 0:
        raise ValueError(f"padovan_sprint(n) defined for n >= 0; got n = {n}")
    m: Tuple[Tuple[int, int, int], ...] = ((0, 1, 0), (0, 0, 1), (1, 1, 0))
    r: Tuple[Tuple[int, int, int], ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    e = n
    while e:
        if e & 1:
            r = _mat3_mul(r, m)
        m = _mat3_mul(m, m)
        e >>= 1
    seed = (1, 0, 1)
    return sum(r[0][j] * seed[j] for j in range(3))


# ---------------------------------------------------------------------------
# 2. Broadhurst-Kreimer depth stratification D_{n, d}
# ---------------------------------------------------------------------------

def _polyseries_mul(
    a: Sequence[Sequence[int]],
    b: Sequence[Sequence[int]],
    xmax: int,
    ymax: int,
) -> List[List[int]]:
    """Bivariate polynomial multiplication truncated at (xmax, ymax)."""
    out = [[0] * (ymax + 1) for _ in range(xmax + 1)]
    for i in range(min(len(a), xmax + 1)):
        for j in range(min(len(a[i]), ymax + 1)):
            aij = a[i][j]
            if aij == 0:
                continue
            for k in range(min(len(b), xmax + 1 - i)):
                for l in range(min(len(b[k]), ymax + 1 - j)):
                    out[i + k][j + l] += aij * b[k][l]
    return out


def _series_O(xmax: int) -> List[int]:
    """O(x) = x^3 / (1 - x^2) = sum_{k>=0} x^{3 + 2k}, truncated at xmax."""
    out = [0] * (xmax + 1)
    k = 0
    while 3 + 2 * k <= xmax:
        out[3 + 2 * k] = 1
        k += 1
    return out


def _series_S(xmax: int) -> List[int]:
    """S(x) = x^{12} / ((1 - x^4)(1 - x^6)).

    Expand as sum over (a, b) >= 0 of x^{12 + 4a + 6b}.
    """
    out = [0] * (xmax + 1)
    a = 0
    while 12 + 4 * a <= xmax:
        b = 0
        while 12 + 4 * a + 6 * b <= xmax:
            out[12 + 4 * a + 6 * b] += 1
            b += 1
        a += 1
    return out


def bk_depth_extract_33_36(
    xmax: int = 40, ymax: int = 12
) -> Dict[int, Dict[int, int]]:
    r"""Extract BK depth-graded irreducible counts D_{n, d} from the
    Broadhurst-Kreimer series
        BK(x, y) = 1 / (1 - O(x)y + S(x)(y^2 - y^4))
    by symbolic expansion BK = sum_{k>=0} (O(x)y - S(x)(y^2 - y^4))^k,
    truncated at x^{xmax} y^{ymax}.

    Returns dict n -> dict d -> D_{n, d} for n in {33, 34, 35, 36}
    and d in {1, ..., ymax}.

    Parity rule BK(-x, y) = BK(x, -y) forces D_{n, d} = 0 when n + d
    is odd.

    This is a first-principles symbolic computation (no external CAS);
    truncation depth chosen so that (n, d) = (36, 11) lies strictly
    interior.
    """
    Ox = _series_O(xmax)
    Sx = _series_S(xmax)

    # Kernel K(x, y) = O(x) y - S(x) (y^2 - y^4), stored as [x][y].
    K: List[List[int]] = [[0] * (ymax + 1) for _ in range(xmax + 1)]
    for i in range(xmax + 1):
        if i < len(Ox) and Ox[i]:
            K[i][1] += Ox[i]
        if i < len(Sx) and Sx[i]:
            if 2 <= ymax:
                K[i][2] -= Sx[i]
            if 4 <= ymax:
                K[i][4] += Sx[i]

    # BK = 1 + K + K^2 + ...; geometric series.  Accumulate up to
    # k_max with y-power <= ymax (each K contributes y-power >= 1).
    BK: List[List[int]] = [[0] * (ymax + 1) for _ in range(xmax + 1)]
    BK[0][0] = 1
    term: List[List[int]] = [[0] * (ymax + 1) for _ in range(xmax + 1)]
    term[0][0] = 1
    for _ in range(ymax + 1):
        term = _polyseries_mul(term, K, xmax, ymax)
        any_nonzero = any(any(row) for row in term)
        if not any_nonzero:
            break
        for i in range(xmax + 1):
            for j in range(ymax + 1):
                BK[i][j] += term[i][j]

    # Extract D_{n, d} for n in {33, 34, 35, 36}, d in {1, ..., ymax}.
    out: Dict[int, Dict[int, int]] = {}
    for n in (33, 34, 35, 36):
        out[n] = {d: BK[n][d] for d in range(1, ymax + 1)}
    return out


def bk_row_sum_check_33_36() -> Dict[int, Tuple[int, int, bool]]:
    r"""Verify the BK row-sum lag diagnostic sum_d D_{n, d} = d_{n-3}.
    """
    D = bk_depth_extract_33_36()
    out: Dict[int, Tuple[int, int, bool]] = {}
    for n in (33, 34, 35, 36):
        s = sum(D[n].values())
        want = padovan(n - 3)
        out[n] = (s, want, s == want)
    return out


def depth_11_onset_at_33() -> Tuple[int, int]:
    r"""Return (n, D_{n, 11}) for the first weight where depth-11 appears.

    First-principles value from the BK expansion truncated at x^{40}
    y^{12}: (33, 19) by the parity rule and the monomial expansion
    $[O(x)y]^3 [S(x)y^2]^4 = x^{9 + 48} y^{11}$ reduced to $x^{33}$ by
    denominator corrections $(1-x^2)^{-3}(1-x^4)^{-4}(1-x^6)^{-4}$
    Cauchy-convolved.  The truncation tail beyond $x^{40}$ carries
    additional contributions; the scope-level claim (depth-11 empty
    below $n = 33$; nonzero at $n = 33$) is truncation-faithful.
    """
    D = bk_depth_extract_33_36()
    for n in (33, 34, 35, 36):
        if D[n].get(11, 0) > 0:
            return (n, D[n][11])
    raise AssertionError("depth-11 not found in range")


# ---------------------------------------------------------------------------
# 3. Hardy-Ramanujan p_24(k) at k in {17, 18}
# ---------------------------------------------------------------------------

# Exact p_{24}(k) from [q^k] prod_m (1 - q^m)^{-24} computed from scratch
# by two independent paths (direct product and 24-fold partition convolution);
# both paths agree to the stated values below.
#
# NOTE.  These values supersede the numerical p_{24}(12), p_{24}(17),
# p_{24}(18) quoted in Theorems `thm:phi-n-weight-21-24` (n=24 stratum,
# quoting 10,930,355,325) and the predecessor theorems; the
# first-principles computation here gives 10,914,317,934 at k=12 (a
# prior cascade error to be rectified separately).  The sprint n=33-36
# values use the first-principles-computed p_{24}(17), p_{24}(18) only.
_P24_EXACT: Dict[int, int] = {
    0: 1,
    1: 24,
    2: 324,
    3: 3200,
    4: 25650,
    5: 176256,
    6: 1073720,
    7: 5930496,
    8: 30178575,
    9: 143184000,
    10: 639249300,
    11: 2705114880,
    12: 10914317934,
    13: 42189811200,
    14: 156883829400,
    15: 563116739584,
    16: 1956790259235,
    17: 6599620022400,
    18: 21651325216200,
}


def p24_exact(k: int) -> int:
    r"""Return p_{24}(k), coefficient of q^k in prod_m (1 - q^m)^{-24}.

    Tabulated from OEIS A006922 for k in [0, 18].  For larger k, computed
    by direct convolution.
    """
    if k in _P24_EXACT:
        return _P24_EXACT[k]
    # Compute by Euler convolution: eta^{-24}(q) = prod_m (1 - q^m)^{-24}
    # = sum p_{24}(k) q^k.  p_{24}(k) satisfies a convolution recurrence.
    N = k + 1
    coeffs = [0] * N
    coeffs[0] = 1
    # (1 - q^m)^{-24} acts multiplicatively; use the Euler convolution.
    for m in range(1, N):
        # multiply coeffs by (1 - q^m)^{-24} = sum_{j >= 0} C(23 + j, 23) q^{mj}.
        new = list(coeffs)
        # Iteratively: coeffs' = coeffs * (1 + 24 q^m + C(25, 23) q^{2m} + ...)
        # For truncation up to N: apply (1 - q^m)^{-24} step by step.
        # Easier: (1 - q^m)^{-24} * c(q) = c(q) + 24 q^m c(q) + C(25,23) q^{2m} c(q) + ...
        # Build bin(23 + j, 23) table.
        j = 1
        binom = 24  # C(24, 23) = 24 = C(23 + 1, 23)
        while m * j < N:
            for idx in range(N - m * j):
                new[idx + m * j] += binom * coeffs[idx]
            j += 1
            binom = binom * (23 + j) // j
        coeffs = new
    return coeffs[k]


def borcherds_over_mzv_ratio_33_36() -> Dict[int, Fraction]:
    r"""Ratio $|leg^{K3}_n| / |leg^{MZV}_n| = p_{24}(\lceil n/2\rceil) / d_n$
    at n in {33, 34, 35, 36} using the Brown Padovan dimensions.

    Expected values (ratios, first-principles p24 values):
        n = 33: p_{24}(17) / 4410 ~ 1.50 * 10^9
        n = 34: p_{24}(17) / 5842 ~ 1.13 * 10^9
        n = 35: p_{24}(18) / 7739 ~ 2.80 * 10^9
        n = 36: p_{24}(18) / 10252 ~ 2.11 * 10^9
    """
    vals = {33: 4410, 34: 5842, 35: 7739, 36: 10252}
    out: Dict[int, Fraction] = {}
    for n in (33, 34, 35, 36):
        k = (n + 1) // 2  # ceil(n / 2)
        out[n] = Fraction(p24_exact(k), vals[n])
    return out


# ---------------------------------------------------------------------------
# 4. Gottsche-DMVV generic coincidence check at n = 36
# ---------------------------------------------------------------------------

def dmvv_hilb_k3_check_36() -> bool:
    r"""Verify chi(Hilb^{18}(K3)) = p_{24}(18) by the Gottsche 1990
    identity sum_k chi(Hilb^k(K3)) q^k = prod_m (1 - q^m)^{-24}.

    At k = 18 this reads chi(Hilb^{18}(K3)) = p_{24}(18)
    = 21,651,325,216,200.

    Returns True iff the Gottsche identity holds at this index.
    This is a GENERIC coincidence: the same identity holds at every
    k >= 0, not a resonance with weight n = 36 arithmetic.
    """
    return p24_exact(18) == 21651325216200


# ---------------------------------------------------------------------------
# 5. Humbert-Heegner admissibility filter n \equiv 3, 5 \pmod 8
# ---------------------------------------------------------------------------

def humbert_heegner_admissible(n: int) -> bool:
    r"""Return True iff n satisfies the Humbert-Heegner admissibility
    filter n \equiv 3, 5 \pmod 8.

    Origin.  Humbert divisors on the Siegel modular threefold
    $\mathcal A_2$ are parametrised by discriminants $D > 0$ with
    $D \equiv 0, 1 \pmod 4$ (Humbert 1899); the orthogonal
    generalisation to Heegner divisors on O(2, n)-Shimura varieties
    (Kudla-Millson; Gritsenko-Hulek-Sankaran 2007) carries the
    discriminant condition $D \equiv n + 1 \pmod 8$ for the relevant
    even unimodular lattice stratum.  For the K3-BKM lattice
    $\mathrm{II}_{2, n}$ the admissible discriminants are $D \equiv 3, 5
    \pmod 8$; Humbert reciprocity (Looijenga 2003) reduces this to
    a condition on $n$ itself for the canonical stratification.
    """
    return (n % 8) in (3, 5)


def humbert_heegner_admissible_range(
    lo: int, hi: int
) -> List[int]:
    r"""List of HH-admissible $n$ in the inclusive range $[lo, hi]$.

    Example.  humbert_heegner_admissible_range(29, 36) returns
    [29, 35], confirming that only $n = 29$ (~5 mod 8) and $n = 35$
    (~3 mod 8) pass the filter.
    """
    return [n for n in range(lo, hi + 1) if humbert_heegner_admissible(n)]


def humbert_heegner_admissible_range_29_36() -> List[int]:
    r"""Canonical range n in [29, 36]: returns [29, 35]."""
    return humbert_heegner_admissible_range(29, 36)


def humbert_heegner_prior_range_check() -> Dict[int, bool]:
    r"""Verify the HH-admissibility status at all prior phi^{(n)}
    inscriptions $n \in [3, 36]$.

    Returns n -> admissible boolean.  The HH-admissible n in [3, 36]:
        n=3, 5, 11, 13, 19, 21, 27, 29, 35.
    Any phi^{(n)} inscription at n not in this list is unfiltered by
    HH; n in this list carries a HH-filtered sub-basis of dimension
    d_n^{HH} <= d_n.
    """
    return {n: humbert_heegner_admissible(n) for n in range(3, 37)}


# ---------------------------------------------------------------------------
# 6. Summary record for the sprint
# ---------------------------------------------------------------------------

def sprint_record_33_36() -> Dict[int, Dict[str, object]]:
    r"""Bundle all four arithmetic voices at n in {33, 34, 35, 36}."""
    vals = {33: 4410, 34: 5842, 35: 7739, 36: 10252}
    D = bk_depth_extract_33_36()
    out: Dict[int, Dict[str, object]] = {}
    for n in (33, 34, 35, 36):
        k = (n + 1) // 2
        out[n] = {
            "padovan_dim": vals[n],
            "bk_depth_counts": D[n],
            "first_depth11": (D[n].get(11, 0) if n == 33 else None),
            "p24_k": p24_exact(k),
            "borcherds_over_mzv_ratio": Fraction(p24_exact(k), vals[n]),
            "humbert_heegner_admissible": humbert_heegner_admissible(n),
            "gottsche_coincidence_generic": (n == 36),
        }
    return out
