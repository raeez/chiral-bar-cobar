r"""
Virasoro shadow-tower coefficients S_6, S_7, S_8 as closed-form rational
functions of the central charge c.

Context
-------
The Vol I shadow tower {S_r(A)}_{r>=2} classifies chiral algebras through the
Maurer-Cartan coefficient sequence of the universal Theta_A in the ordered
convolution dGLA. For Virasoro at central charge c, the initial data is

    S_2(Vir_c) = kappa(Vir_c) = c/2
    S_3(Vir_c) = 2                                (Vol I normalisation)
    S_4(Vir_c) = 10 / (c (5c + 22))               (FM178)
    S_5(Vir_c) = -48 / (c^2 (5c + 22))            (thm:s5-vir-closed-form)

The denominator factor (5c + 22) is the Zamolodchikov quasi-primary norm
of Lambda = :TT: - (3/10) d^2 T (weight-4 scalar quasi-primary): the
standard identity <Lambda|Lambda> = c (5c + 22) / 10.

Higher Virasoro shadow coefficients (r >= 6) are determined by the
master-equation recursion (derivation chain A)

    S_r = -(1/(2 r kappa)) * SUM_{j+k=r+2, 3 <= j <= k < r} f(j,k) * j*k * S_j * S_k,

where f(j,k) = 1 for j < k and f(j,k) = 1/2 for j = k (chain A, from
shadow_tower_ope_recursion.py). Independently, the Riccati sqrt(Q_L) Taylor
expansion (chain B, from shadow_tower_recursive.py)

    Q_L(t) = 4 kappa^2 + 12 kappa S_3 t + (9 S_3^2 + 16 kappa S_4) t^2
    H(t)   = t^2 sqrt(Q_L(t)) = SUM_{r>=2} r S_r t^r

yields the same S_r as a quadratic Riccati discriminant. Agreement of
chain A with chain B is the content of thm:riccati-algebraicity
(higher_genus_modular_koszul.tex); verified below through r = 8.

Closed forms
------------
Running the recursion with (kappa, S_3, S_4) = (c/2, 2, 10/(c(5c+22))) gives:

    S_6(Vir_c) = 80 (45 c + 193) / [3 c^3 (5c + 22)^2]
    S_7(Vir_c) = -2880 (15 c + 61) / [7 c^4 (5c + 22)^2]
    S_8(Vir_c) = 80 (2025 c^2 + 16470 c + 33314) / [c^5 (5c + 22)^3]

Pole structure: (5c + 22)^{floor((r-2)/2)} for r = 6, 7, 8 (increments on
every even-r doubling of the Lambda-channel contraction) and c^{r-3} at
c -> 0 (abelian limit).

Falsification tests (chain B disjoint)
---------------------------------------
At c = 1:
    S_6(1) = 19040 / 2187     (= 80 * 238 / (3 * 27^2))
    S_7(1) = -24320 / 567     (= -2880 * 76 / (7 * 81))
    S_8(1) = 4144720 / 19683  (Vol III m_8 identity at c=1 specialisation)

At c = 1/2 (Ising minimal model):
    S_6(1/2) = 551680 / 7203
    S_7(1/2) = -12625920 / 16807
    S_8(1/2) = 861291520 / 117649

At c = 13 (Virasoro self-dual, Vir^! = Vir_{26-c} fixed):
    S_6(13) = 62240 / 49887279
    S_7(13) = -81920 / 168138607
    S_8(13) = 47171920 / 244497554379

Large-c asymptotics
-------------------
    S_r(Vir_c) ~ A_r / c^{r-2},  c -> infinity,
with A_6 = 48, A_7 = -1728/7, A_8 = 1296. These leading coefficients are
pure 2^a 3^b rationals and contain no Kummer prime (691 at r=12, 3617 at
r=16); the motivic Kummer-congruence prediction of
thm:kummer-from-motivic applies to Z_g closed-form numerators, not to
the Virasoro shadow asymptotics directly. The shadow-Feynman bijection
F_g <-> S_{2g-2} transmits Kummer content to Z_g through the genus
Bernoulli normalisation, which is a SEPARATE assertion from leading-c
behaviour of S_r itself.

Manuscript references
---------------------
    thm:s6-virasoro-closed-form (shadow_tower_higher_coefficients.tex)
    thm:s7-virasoro-closed-form (shadow_tower_higher_coefficients.tex)
    thm:s8-virasoro-closed-form (shadow_tower_higher_coefficients.tex)
    thm:virasoro-shadow-recurrence (shadow_tower_higher_coefficients.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:miura-cross-universality (miura_transfer.tex)

Dependencies
------------
    compute/lib/shadow_tower_ope_recursion.py : chain A (MC recursion)
    compute/lib/shadow_tower_recursive.py     : chain B (sqrt Q_L)
    compute/lib/s5_vir_wick.py                : S_5 = -48/(c^2(5c+22))
"""

from __future__ import annotations

import sympy as sp


# ---------------------------------------------------------------------------
# Core closed forms
# ---------------------------------------------------------------------------


def s6_virasoro(c):
    """Return S_6(Vir_c) = 80 (45 c + 193) / [3 c^3 (5c + 22)^2].

    Parameters
    ----------
    c : sympy expression or rational
        Central charge. For generic c the return is a rational function
        of c with poles at c = 0 (order 3) and 5 c + 22 = 0 (order 2).

    Returns
    -------
    sympy.Expr
        The closed-form value of the genus-0 6-input Virasoro shadow
        coefficient.
    """
    c = sp.sympify(c)
    return sp.Rational(80) * (45 * c + sp.Rational(193)) / (
        sp.Rational(3) * c**3 * (5 * c + sp.Rational(22)) ** 2
    )


def s7_virasoro(c):
    """Return S_7(Vir_c) = -2880 (15 c + 61) / [7 c^4 (5c + 22)^2].

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.

    Returns
    -------
    sympy.Expr
        Weight-7 Virasoro shadow coefficient.
    """
    c = sp.sympify(c)
    return sp.Rational(-2880) * (15 * c + sp.Rational(61)) / (
        sp.Rational(7) * c**4 * (5 * c + sp.Rational(22)) ** 2
    )


def s8_virasoro(c):
    """Return S_8(Vir_c) = 80 (2025 c^2 + 16470 c + 33314) / [c^5 (5c + 22)^3].

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.

    Returns
    -------
    sympy.Expr
        Weight-8 Virasoro shadow coefficient. At c = 1 specialises to
        4144720 / 19683 (matches Vol III m_8 identity).
    """
    c = sp.sympify(c)
    return sp.Rational(80) * (
        sp.Rational(2025) * c**2
        + sp.Rational(16470) * c
        + sp.Rational(33314)
    ) / (c**5 * (5 * c + sp.Rational(22)) ** 3)


def s10_virasoro(c):
    """Return S_10(Vir_c) = 256 (91125 c^3 + 1050975 c^2 + 3989790 c + 4969967) / [c^7 (5c+22)^4].

    Derived main-thread 2026-04-17 via the master-equation recurrence at r=10
    (j+k=12, cross-terms (3,9), (4,8), (5,7), and diagonal (6,6) with factor 1/2).

    Denominator pattern confirmed at r=10: c-exponent = r-3 = 7,
    (5c+22)-exponent = floor((r-2)/2) = 4. At c=1 specialises to
    2 586 075 392 / 3^12 (denominator pure power of 3).

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.

    Returns
    -------
    sympy.Expr
        Weight-10 Virasoro shadow coefficient. Rational in c, no MZV contribution.
    """
    c = sp.sympify(c)
    return sp.Rational(256) * (
        sp.Rational(91125) * c**3
        + sp.Rational(1050975) * c**2
        + sp.Rational(3989790) * c
        + sp.Rational(4969967)
    ) / (c**7 * (5 * c + sp.Rational(22)) ** 4)


def s9_virasoro(c):
    """Return S_9(Vir_c) = -1280 (2025 c^2 + 15570 c + 29554) / [3 c^6 (5c + 22)^3].

    Derived main-thread 2026-04-17 via the master-equation recurrence at r=9
    (j+k=11, cross-terms (3,8), (4,7), (5,6)). The Kummer-irregular primes
    691 and 3617 do NOT appear in the Virasoro numerator at r=9; the
    quadratic 2025 c^2 + 15570 c + 29554 has discriminant 3 038 500,
    non-square over Q, so the numerator is Q-irreducible.

    Denominator pattern confirmed at r=9: c-exponent = r-3 = 6,
    (5c+22)-exponent = floor((r-2)/2) = 3.

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.

    Returns
    -------
    sympy.Expr
        Weight-9 Virasoro shadow coefficient.
    """
    c = sp.sympify(c)
    return -sp.Rational(1280) * (
        sp.Rational(2025) * c**2
        + sp.Rational(15570) * c
        + sp.Rational(29554)
    ) / (sp.Rational(3) * c**6 * (5 * c + sp.Rational(22)) ** 3)


# ---------------------------------------------------------------------------
# Leading and subleading asymptotic closed forms
# ---------------------------------------------------------------------------


def leading_asymptotic(r):
    """Closed form of A_r = lim_{c -> oo} c^(r-2) * S_r(Vir_c).

    Theorem: A_r = 8 * (-6)^(r-4) / r for r >= 4.

    See chapters/theory/shadow_tower_higher_coefficients.tex
    thm:shadow-tower-asymptotic-closed-form.

    Parameters
    ----------
    r : int
        Shadow-tower weight, r >= 4.

    Returns
    -------
    sympy.Rational
        Leading coefficient A_r.
    """
    if r < 4:
        raise ValueError("leading_asymptotic requires r >= 4.")
    return sp.Rational(8) * sp.Rational(-6) ** (r - 4) / sp.Rational(r)


def subleading_asymptotic(r):
    """Closed form of B_r = lim_{c -> oo} c * (c^(r-2) * S_r - A_r).

    Theorem (thm:shadow-tower-subleading-closed-form):

        B_r = -A_r * [22/5 + (r-4)(r-5)/18]
            = -4 * (-6)^(r-4) * (5 r^2 - 45 r + 496) / (45 r).

    Proof sketch: The rescaled Riccati recurrence
      r * Phi_r * c = -Sum_{j+k=r+2, 3<=j<=k<r} f(j,k) j k Phi_j Phi_k
    with Phi_r = c^(r-2) S_r and Phi_3 = 2c (negative Laurent order)
    yields, after matching the c^(-1) coefficient,
      B_r = -6(r-1)/r * B_{r-1} - sigma_r,
      sigma_r := (1/r) Sum_{j>=4, k<=r-2, j+k=r+2} f(j,k) j k A_j A_k.
    The combinatorial identity
      Sum_{j+k=r+2, 4<=j<=k<=r-2} f(j,k) = (r-5)/2
    (lem:subleading-combinatorial-identity) combined with
    A_j A_k j k = 64 * (-6)^(r-6) (independent of partition) gives
    sigma_r / A_r = (r-5)/9. Variation of parameters then yields
    B_r / A_r = -22/5 - Sum_{s=5}^{r} (s-5)/9
              = -22/5 - (r-4)(r-5)/18.

    Parameters
    ----------
    r : int
        Shadow-tower weight, r >= 4.

    Returns
    -------
    sympy.Rational
        Subleading coefficient B_r.
    """
    if r < 4:
        raise ValueError("subleading_asymptotic requires r >= 4.")
    A_r = leading_asymptotic(r)
    phi_r = -sp.Rational(22, 5) - sp.Rational((r - 4) * (r - 5), 18)
    return A_r * phi_r


def sub_subleading_asymptotic(r):
    """Closed form of Gamma_r = lim c^2 * (c^(r-2) S_r - A_r - B_r/c).

    Theorem (thm:shadow-tower-sub-subleading-closed-form):

        Gamma_r / A_r = 484/25 + (22/45)*(r-4)*(r-5)
                       + (r-4)*(r-5)*(r-6)*(r-7)/972.

    Three-term structure:
      - 484/25 = (-22/5)^2: geometric-square from the base case
      - (22/45)(r-4)(r-5): Zamolodchikov-Riccati mixing term
      - (r-4)(r-5)(r-6)(r-7)/972: pure Riccati sub-subleading

    Proved main-thread 2026-04-17 via the sub-subleading recurrence
      Gamma_r = -(6(r-1)/r) Gamma_{r-1}
               - (1/r) Sum_{j,k>=4, j+k=r+2} f(j,k) jk (A_j B_k + B_j A_k),
    the cubic combinatorial identity Sum f(j,k) P_jk = (r-5)(r-6)(r-7)/3
    (lem:sub-subleading-cubic-identity), and telescoping
    Sum_{s=5}^{r} (s-5)(s-6)(s-7) = (r-4)(r-5)(r-6)(r-7)/4.

    Corollary: the Kummer-irregular prime 691 first appears in the
    Laurent stratification of S_r at r = 8, via
      Gamma_8 / A_8 = (39204 + 11880 + 50)/2025 = 51134/2025
                    = 2 * 37 * 691 / 2025.

    Parameters
    ----------
    r : int
        Shadow-tower weight, r >= 4.

    Returns
    -------
    sympy.Rational
        Sub-subleading coefficient Gamma_r.
    """
    if r < 4:
        raise ValueError("sub_subleading_asymptotic requires r >= 4.")
    A_r = leading_asymptotic(r)
    gamma_r = (
        sp.Rational(484, 25)
        + sp.Rational(22, 45) * (r - 4) * (r - 5)
        + sp.Rational(1, 972) * (r - 4) * (r - 5) * (r - 6) * (r - 7)
    )
    return A_r * gamma_r


def subleading_polynomial(r):
    """Return q(r) = 5 r^2 - 45 r + 496 (subleading Riccati polynomial).

    Appears in B_r = -4 * (-6)^(r-4) * q(r) / (45 r). Discriminant
    -7895 < 0; q(r) >= 1579/4 > 0 for all real r, attained at r = 9/2.

    Characteristic primes of the subleading layer are the prime
    divisors of q(r) for the relevant r. Through r = 11 these are
    {7, 11, 13, 19, 29, 31, 71, 101}, none Kummer-irregular.

    Parameters
    ----------
    r : int or sympy.Integer
        Shadow-tower weight.

    Returns
    -------
    sympy.Integer
        Value of q(r).
    """
    r = sp.sympify(r)
    return sp.Integer(5) * r**2 - sp.Integer(45) * r + sp.Integer(496)


def sub_subleading_asymptotic(r):
    r"""Closed form of Gamma_r = lim_{c -> oo} c^2 * (c^(r-2) * S_r - A_r - B_r / c).

    Theorem (thm:shadow-tower-sub-subleading-closed-form):

        Gamma_r / A_r = 484/25
                      + 22 (r-4)(r-5) / 45
                      + (r-4)(r-5)(r-6)(r-7) / 972.

    Equivalently, writing phi_r := -B_r/A_r = 22/5 + (r-4)(r-5)/18,

        Gamma_r / A_r = phi_r^2 - (r-4)(r-5)(r^2 - 7 r + 9) / 486.

    Proof sketch (variation of parameters, second-order layer).
    The rescaled recurrence Phi_r := c^(r-2) S_r gives

        Phi_r = -6(r-1)/r * Phi_{r-1}
              - (1/(r c)) Sum_{j+k=r+2, 4<=j<=k<=r-2} f(j,k) j k Phi_j Phi_k.

    Laurent-expanding Phi_r = A_r + B_r/c + Gamma_r/c^2 + ... and
    matching the c^(-2) coefficient:

        Gamma_r = -6(r-1)/r * Gamma_{r-1} - sigma_r^(gamma),
        sigma_r^(gamma) := (1/r) Sum f(j,k) j k (A_j B_k + B_j A_k).

    The source is purely B-linear (there is no B_j B_k contribution at
    this Laurent order; B^2 appears only at c^(-3)). The leading ratio
    A_{r-1}/A_r = -r/(6(r-1)) absorbs the transport prefactor, yielding

        Gamma_r / A_r = Gamma_{r-1} / A_{r-1} - sigma_r^(gamma) / A_r.

    Combining the two known identities

        (1/r) Sum f(j,k) j k A_j A_k = (r-5)/9 * A_r (subleading recurrence),
        Sum_{j=4}^{r-2} (j-4)(j-5) = (r-7)(r-6)(r-5)/3 (hockey stick),

    and substituting B_j/A_j = -[22/5 + (j-4)(j-5)/18] gives

        sigma_r^(gamma) / A_r = -44(r-5)/45 - (r-5)(r-6)(r-7) / 243.

    The closed form for Gamma_r/A_r follows by telescoping from the base
    case Gamma_4/A_4 = 484/25 = (B_4/A_4)^2 with summations

        Sum_{s=5}^{r} (s-5) = (r-4)(r-5)/2,
        Sum_{s=5}^{r} (s-5)(s-6)(s-7) = (r-4)(r-5)(r-6)(r-7)/4.

    Parameters
    ----------
    r : int
        Shadow-tower weight, r >= 4.

    Returns
    -------
    sympy.Rational
        Sub-subleading coefficient Gamma_r.
    """
    if r < 4:
        raise ValueError("sub_subleading_asymptotic requires r >= 4.")
    A_r = leading_asymptotic(r)
    ratio = (
        sp.Rational(484, 25)
        + sp.Rational(22 * (r - 4) * (r - 5), 45)
        + sp.Rational((r - 4) * (r - 5) * (r - 6) * (r - 7), 972)
    )
    return A_r * ratio


def sub_subleading_numerator_polynomial(r):
    r"""Return N(r) := 25 r^4 - 550 r^3 + 16355 r^2 - 122870 r + 729048.

    N(r) is the integer quartic obtained by clearing the common
    denominator LCM(25, 45, 972) = 24300 in the Gamma_r/A_r closed
    form:

        Gamma_r / A_r = N(r) / 24300.

    Equivalent factorisation from the variation-of-parameters
    telescope:

        N(r) = 484 * 972
             + 22 * 540 * (r-4)(r-5)
             + 25 * (r-4)(r-5)(r-6)(r-7).

    The polynomial is irreducible over Q (its discriminant has
    no rational-root reduction). The Kummer-irregular prime 691
    divides N(8) = 2^3 * 3 * 37 * 691 = 613608; this is a
    modular coincidence in F_691 (N(r) = 0 mod 691 has roots
    r in {8, 315, 423, 658}), NOT a Bernoulli structural emergence.

    Parameters
    ----------
    r : int or sympy.Integer
        Shadow-tower weight.

    Returns
    -------
    sympy.Integer
        Value of N(r).
    """
    r = sp.sympify(r)
    return (
        sp.Integer(25) * r**4
        - sp.Integer(550) * r**3
        + sp.Integer(16355) * r**2
        - sp.Integer(122870) * r
        + sp.Integer(729048)
    )


def sub_subleading_source_ratio(r):
    r"""Return sigma_r^(gamma) / A_r, the gamma-level source ratio.

    Closed form (proved as part of
    thm:shadow-tower-sub-subleading-closed-form):

        sigma_r^(gamma) / A_r = -44 (r-5) / 45
                              - (r-5)(r-6)(r-7) / 243.

    Empty for r = 5 (linear and cubic terms both vanish); empty-linear
    and first cubic contribution at r = 6; both terms active for
    r >= 7. The cubic term is what distinguishes the sub-subleading
    layer from the subleading (where the source is purely linear in r).

    Parameters
    ----------
    r : int
        Shadow-tower weight, r >= 5.

    Returns
    -------
    sympy.Rational
        Source-to-leading ratio.
    """
    if r < 5:
        raise ValueError("sub_subleading_source_ratio requires r >= 5.")
    return (
        -sp.Rational(44 * (r - 5), 45)
        - sp.Rational((r - 5) * (r - 6) * (r - 7), 243)
    )


# ---------------------------------------------------------------------------
# Transport-operator recurrence (the common mechanism for r >= 5)
# ---------------------------------------------------------------------------


def virasoro_shadow_recurrence(S_prev, r, c):
    r"""Master-equation recurrence for the r-th Virasoro shadow coefficient.

    Implements the shadow transport operator

        S_r = -(1/(2 r kappa)) * SUM_{j+k=r+2, 3 <= j <= k < r} f(j,k) j k S_j S_k

    with kappa = c/2, f(j,k) = 1 for j<k and f(j,k) = 1/2 for j=k.

    The sum runs over unordered integer pairs (j,k) with j + k = r + 2,
    j >= 3, k < r. The j = 2 and k = r contributions are absorbed into
    the linearised nabla_H operator; their exclusion is what closes the
    recurrence on the previously-computed S_3, ..., S_{r-1}.

    Parameters
    ----------
    S_prev : dict[int, sympy.Expr]
        Mapping r' -> S_{r'} for r' = 2, ..., r - 1. Must contain
        S_3, ..., S_{r-1}.
    r : int
        Target weight. Must satisfy r >= 5.
    c : sympy.Expr
        Central charge (symbolic or numerical).

    Returns
    -------
    sympy.Expr
        The coefficient S_r obtained by applying the recursion to S_prev.

    Raises
    ------
    ValueError
        If r < 5 or S_prev is missing any required S_j.
    """
    if r < 5:
        raise ValueError(
            "Recurrence applies for r >= 5; initial data S_2, S_3, S_4 "
            "are independent input."
        )
    kappa = sp.Rational(1, 2) * sp.sympify(c)
    obs = sp.Integer(0)
    target = r + 2
    for j in range(3, target // 2 + 1):
        k = target - j
        if k < j or k >= r:
            continue
        if j not in S_prev or k not in S_prev:
            raise ValueError(
                f"S_prev missing coefficient needed for r={r}: j={j}, k={k}."
            )
        term = sp.Integer(j) * sp.Integer(k) * S_prev[j] * S_prev[k]
        if j == k:
            obs += term * sp.Rational(1, 2)
        else:
            obs += term
    return sp.cancel(-obs / (sp.Integer(2) * sp.Integer(r) * kappa))


def virasoro_shadow_sequence(c, max_r=8):
    """Return {2: S_2, 3: S_3, 4: S_4, ..., max_r: S_{max_r}} for Vir_c.

    Uses initial data (kappa, S_3, S_4) = (c/2, 2, 10/(c(5c+22))) and
    iterates virasoro_shadow_recurrence.

    Parameters
    ----------
    c : sympy.Expr
        Central charge.
    max_r : int
        Highest weight to compute. Must be >= 4.

    Returns
    -------
    dict[int, sympy.Expr]
        Map from r to S_r(Vir_c), r = 2, ..., max_r, simplified by
        sp.cancel.
    """
    if max_r < 4:
        raise ValueError("max_r must be >= 4.")
    c = sp.sympify(c)
    S = {
        2: sp.Rational(1, 2) * c,
        3: sp.Integer(2),
        4: sp.Rational(10) / (c * (5 * c + sp.Integer(22))),
    }
    for r in range(5, max_r + 1):
        S[r] = virasoro_shadow_recurrence(S, r, c)
    return S


# ---------------------------------------------------------------------------
# Boundary-value tables (for independent verification tests)
# ---------------------------------------------------------------------------
#
# Verified values at three boundary points. Each row is derived
# independently from the closed-form rational expression AND from the
# chain-A recursion (see test_shadow_tower_higher.py for the disjoint
# verification).

BOUNDARY_VALUES = {
    # (r, c) -> S_r(Vir_c)
    (6, 1): sp.Rational(19040, 2187),
    (7, 1): sp.Rational(-24320, 567),
    (8, 1): sp.Rational(4144720, 19683),
    (6, sp.Rational(1, 2)): sp.Rational(551680, 7203),
    (7, sp.Rational(1, 2)): sp.Rational(-12625920, 16807),
    (8, sp.Rational(1, 2)): sp.Rational(861291520, 117649),
    (6, 13): sp.Rational(62240, 49887279),
    (7, 13): sp.Rational(-81920, 168138607),
    (8, 13): sp.Rational(47171920, 244497554379),
}


# Large-c leading coefficient A_r := lim_{c -> infinity} c^{r-2} S_r.
LEADING_ASYMPTOTIC = {
    4: sp.Integer(2),
    5: sp.Rational(-48, 5),
    6: sp.Integer(48),
    7: sp.Rational(-1728, 7),
    8: sp.Integer(1296),
}


# Sub-subleading coefficients Gamma_r = lim_{c -> infinity} c^2 (c^(r-2) S_r - A_r - B_r/c).
# Each value verified by two independent chains (Laurent expansion of
# s_r_virasoro closed form AND variation-of-parameters telescope). See
# test_sub_subleading_asymptotic.py for the disjoint verification.
SUB_SUBLEADING_ASYMPTOTIC = {
    4: sp.Rational(968, 25),
    5: sp.Rational(-23232, 125),
    6: sp.Rational(73216, 75),
    7: sp.Rational(-963072, 175),
    8: sp.Rational(818144, 25),
    9: sp.Rational(-15169024, 75),
    10: sp.Rational(160482816, 125),
}
