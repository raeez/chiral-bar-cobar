r"""Formal weighted-Riccati coefficients from Virasoro local data.

The vacuum Virasoro algebra canonically determines the sphere Ward
correlators ``G_n`` and their connected cumulants ``G_n^conn``.  They are
rational functions on ``Conf_n(P^1)``; see
``compute.lib.virasoro_ward_correlators``.  An ordered scalar coordinate
``S_n`` additionally uses ``H_res(Vir_c; X)``, an Arnold class, and a
normalized residue projection.

This module computes a different, completely specified object.  Put

    kappa = c/2,
    R_3 = 2,
    R_4 = 10 / (c (5c + 22)),

and define the weighted-Riccati series

    Q_L(t) = 4 kappa^2 + 12 kappa R_3 t
             + (9 R_3^2 + 16 kappa R_4) t^2,
    H_Ricc(t) = t^2 sqrt(Q_L(t)) = sum_{r >= 2} r R_r t^r.

Equivalently, its coefficients obey

    R_r = -(1/(2 r kappa))
          sum_{j+k=r+2, 3 <= j <= k < r} f(j,k) j k R_j R_k,

where ``f(j,k)=1`` for ``j<k`` and ``f(j,j)=1/2``.  The sum is over
unordered pairs.  Hence

    R_5 = -48 / (c^2 (5c + 22)),
    R_6 = 80 (45 c + 193) / (3 c^3 (5c + 22)^2).

The formal order-six relation

    2 R_2 C_6^rel + 2 R_3 R_5 + R_4^2 = 0

defines the distinct candidate

    C_6^rel = 4 (240 c + 1031) / (c^3 (5c + 22)^2),

on the regular domain ``c(5c+22) != 0``.  This relation supplies an
algebraic coefficient.  A singular-vector interpretation begins with an
explicit level-six radical/decoupling map from the vacuum-Verma radical to
the chosen quotient or residue model.

Thus ``R_6^Ricc`` and ``C_6^rel`` are exact outputs of two named formal
constructions.  A comparison with an ordered scalar
``S_6(Vir_c; H_res)`` is supplied by the corresponding residue map.  The
historical function names in this module return weighted-Riccati outputs so
that existing callers retain their algebraic-series semantics.
"""

from __future__ import annotations

import sympy as sp


# ---------------------------------------------------------------------------
# Core closed forms
# ---------------------------------------------------------------------------


def s5_riccati_candidate(c):
    """Return the exact arity-five coefficient of ``H_Ricc``."""

    c = sp.sympify(c)
    return -sp.Rational(48) / (c**2 * (5 * c + sp.Rational(22)))


def s6_riccati_candidate(c):
    """Return ``R_6^Ricc = 80(45c+193)/(3c^3(5c+22)^2)``.

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.  The regular domain is ``c(5c+22) != 0``; the
        rational continuation has poles at ``c=0`` and ``5c+22=0``.

    Returns
    -------
    sympy.Expr
        The arity-six coefficient of the weighted-Riccati series.
    """
    c = sp.sympify(c)
    return sp.Rational(80) * (45 * c + sp.Rational(193)) / (
        sp.Rational(3) * c**3 * (5 * c + sp.Rational(22)) ** 2
    )


def s6_relation_candidate(c):
    """Return ``C_6^rel = 4(240c+1031)/(c^3(5c+22)^2)``.

    This is the exact solution of the formal relation
    ``2 R_2 C_6^rel + 2 R_3 R_5 + R_4^2 = 0`` with the local seeds stated
    in the module docstring.  Its regular domain is
    ``c(5c+22) != 0``.  A singular-vector interpretation requires an
    explicit level-six radical/decoupling map.
    """

    c = sp.sympify(c)
    return sp.Rational(4) * (240 * c + sp.Rational(1031)) / (
        c**3 * (5 * c + sp.Rational(22)) ** 2
    )


def s6_null_candidate(c):
    """Compatibility alias for :func:`s6_relation_candidate`.

    The alias carries the formal-relation semantics of
    ``2 R_2 C_6^rel + 2 R_3 R_5 + R_4^2 = 0``.  A singular-vector reading
    begins after an explicit level-six radical/decoupling map has been
    supplied.
    """

    return s6_relation_candidate(c)


WEIGHT_SIX_RELATION_SEMANTICS = {
    "canonical_function": "s6_relation_candidate",
    "defining_relation": "2 R_2 C_6^rel + 2 R_3 R_5 + R_4^2 = 0",
    "domain": "c(5c+22) != 0",
    "status": "formal relation candidate",
    "singular_vector_requirement": "explicit level-six radical/decoupling map",
}


def s6_virasoro(c):
    """Compatibility name for the weighted-Riccati coefficient."""

    return s6_riccati_candidate(c)


def s7_virasoro(c):
    """Return the arity-seven weighted-Riccati coefficient.

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.

    Returns
    -------
    sympy.Expr
        Arity-seven weighted-Riccati coefficient.
    """
    c = sp.sympify(c)
    return sp.Rational(-2880) * (15 * c + sp.Rational(61)) / (
        sp.Rational(7) * c**4 * (5 * c + sp.Rational(22)) ** 2
    )


def s8_virasoro(c):
    """Return the arity-eight weighted-Riccati coefficient.

    Parameters
    ----------
    c : sympy expression or rational
        Central charge.

    Returns
    -------
    sympy.Expr
        Arity-eight weighted-Riccati coefficient.  At ``c=1`` its value is
        ``4144720/19683``.
    """
    c = sp.sympify(c)
    return sp.Rational(80) * (
        sp.Rational(2025) * c**2
        + sp.Rational(16470) * c
        + sp.Rational(33314)
    ) / (c**5 * (5 * c + sp.Rational(22)) ** 3)


def s10_virasoro(c):
    """Return the arity-ten weighted-Riccati coefficient.

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
        Arity-ten weighted-Riccati coefficient in ``Q(c)``.
    """
    c = sp.sympify(c)
    return sp.Rational(256) * (
        sp.Rational(91125) * c**3
        + sp.Rational(1050975) * c**2
        + sp.Rational(3989790) * c
        + sp.Rational(4969967)
    ) / (c**7 * (5 * c + sp.Rational(22)) ** 4)


def s9_virasoro(c):
    """Return the arity-nine weighted-Riccati coefficient.

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
        Arity-nine weighted-Riccati coefficient.
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
    """Large-``c`` leading term of the weighted-Riccati coefficient.

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
    """Large-``c`` subleading term of the weighted-Riccati coefficient.

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
    """Second large-``c`` correction of the weighted-Riccati coefficient.

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


def sub_sub_subleading_asymptotic(r):
    """Third large-``c`` correction of the weighted-Riccati coefficient.

    Theorem (thm:shadow-tower-tier-4-closed-form, main-thread 2026-04-17):

        Delta_r / A_r = -(22/5)^3
                       - (242/75) (r-4)(r-5)
                       - (11/810) (r-4)(r-5)(r-6)(r-7)
                       - (1/104976) (r-4)(r-5)(r-6)(r-7)(r-8)(r-9).

    Four-term structure (one term per factor pair from (r-4)(r-5)):
      - (-22/5)^3 = -10648/125: geometric-cube base case (from Phi_4 expansion)
      - -(242/75)(r-4)(r-5): tau^2 cross correction
      - -(11/810)(r-4)(r-5)(r-6)(r-7): tau cross correction
      - -(1/104976)(r-4)(r-5)(r-6)(r-7)(r-8)(r-9): pure Riccati sextic

    Proved via the sub-sub-subleading recurrence
      Delta_r = -(6(r-1)/r) Delta_{r-1}
               - (1/r) Sum_{j,k>=4, j+k=r+2} f(j,k) jk (A_j Gamma_k + B_j B_k + Gamma_j A_k),
    the quintic combinatorial identities
      Sum f(j,k) Q_jk = (r-5)(r-6)(r-7)(r-8)(r-9)/5   (for Q_jk = single-slot quartic)
      Sum f(j,k) R_jk = (r-5)(r-6)(r-7)(r-8)(r-9)/60  (for R_jk = cross-slot quadratic product)
    and variation-of-parameters telescoping with the sextic sum
      Sum_{s=5}^{r} (s-5)(s-6)(s-7)(s-8)(s-9) = (r-4)(r-5)(r-6)(r-7)(r-8)(r-9)/6.

    This is the first tier where the B_j B_k (subleading-squared) cross-term
    appears: at Tier 3 (Gamma_r) the B_j B_k term does NOT contribute (it first
    appears at Tier 4). Tier 4 is therefore the first layer where the full
    Riccati-source structure is visible.

    Parameters
    ----------
    r : int
        Shadow-tower weight, r >= 4.

    Returns
    -------
    sympy.Rational
        Sub-sub-subleading coefficient Delta_r.
    """
    if r < 4:
        raise ValueError("sub_sub_subleading_asymptotic requires r >= 4.")
    A_r = leading_asymptotic(r)
    tau3 = sp.Rational(22, 5) ** 3
    delta_r = -(
        tau3
        + sp.Rational(242, 75) * (r - 4) * (r - 5)
        + sp.Rational(11, 810) * (r - 4) * (r - 5) * (r - 6) * (r - 7)
        + sp.Rational(1, 104976) * (r - 4) * (r - 5) * (r - 6) * (r - 7) * (r - 8) * (r - 9)
    )
    return A_r * delta_r


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
    r"""Formal recurrence for the ``r``-th weighted-Riccati coefficient.

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
        The coefficient ``R_r`` obtained from the unordered-pair recurrence.

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
    """Return the weighted-Riccati sequence through ``max_r``.

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
        Map from ``r`` to ``R_r(c)``, simplified by
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
# Boundary values of the weighted-Riccati sequence
# ---------------------------------------------------------------------------
#
# These exact substitutions test the closed formulas and the recurrence at
# three regular values of the central charge.

BOUNDARY_VALUES = {
    # (r, c) -> R_r(c)
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


WEIGHT_SIX_RELATION_VALUES = {
    central_charge: sp.cancel(s6_relation_candidate(central_charge))
    for central_charge in (sp.Integer(1), sp.Rational(1, 2), sp.Integer(13))
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
# Each value is checked both by Laurent expansion of the displayed rational
# function and by the variation-of-parameters identity.
SUB_SUBLEADING_ASYMPTOTIC = {
    4: sp.Rational(968, 25),
    5: sp.Rational(-23232, 125),
    6: sp.Rational(73216, 75),
    7: sp.Rational(-963072, 175),
    8: sp.Rational(818144, 25),
    9: sp.Rational(-15169024, 75),
    10: sp.Rational(160482816, 125),
}
