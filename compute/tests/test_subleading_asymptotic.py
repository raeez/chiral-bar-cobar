"""
Independent-verification tests for the subleading asymptotic

    B_r = -A_r * [22/5 + (r-4)(r-5)/18]

of the Virasoro shadow-tower coefficient S_r(Vir_c), proved in
chapters/theory/shadow_tower_higher_coefficients.tex as
thm:shadow-tower-subleading-closed-form.

Derivation chain (A): variation-of-parameters on the subleading
  recurrence B_r = -6(r-1)/r * B_{r-1} - sigma_r, using the
  combinatorial identity Sum f(j,k) = (r-5)/2 and the source-ratio
  identity sigma_r / A_r = (r-5)/9.

Verification chain (B): direct Laurent expansion of the explicit
  closed forms S_r(Vir_c) through r = 10 around c = infinity, reading
  off the coefficient of c^(-1) in Phi_r = c^(r-2) * S_r.

The two chains share only the initial data (S_3, S_4) = (2,
  10/[c(5c+22)]) and the integer master-equation coefficients f(j,k),
  j*k. Chain (A) is integer-recurrence algebra; chain (B) is
  symbolic Laurent expansion. No derivation path beyond the
  shared base data.
"""

from __future__ import annotations

import sympy as sp
from sympy import Rational, symbols, series

from compute.lib.independent_verification import independent_verification
from compute.lib.shadow_tower_higher_vir import (
    leading_asymptotic,
    subleading_asymptotic,
    subleading_polynomial,
    s6_virasoro,
    s7_virasoro,
    s8_virasoro,
    s9_virasoro,
    s10_virasoro,
)


# ---------------------------------------------------------------------------
# Laurent-expansion ground truth (chain B)
# ---------------------------------------------------------------------------


def _laurent_subleading(S_of_c, r):
    """Extract B_r := coefficient of c^(-1) in Phi_r(c) = c^(r-2) * S_r.

    Substitutes c = 1/u and expands at u = 0.
    """
    c = symbols("c")
    u = symbols("u")
    phi = sp.cancel(c ** (r - 2) * S_of_c(c)).subs(c, 1 / u)
    expansion = series(phi, u, 0, 3).removeO()
    poly = sp.Poly(expansion, u)
    # coefficient of u^1 = B_r
    return sp.Rational(poly.nth(1))


VIR_CLOSED_FORMS = {
    6: s6_virasoro,
    7: s7_virasoro,
    8: s8_virasoro,
    9: s9_virasoro,
    10: s10_virasoro,
}


# ---------------------------------------------------------------------------
# Base cases: r = 4, 5
# ---------------------------------------------------------------------------


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "variation-of-parameters recurrence B_r = -6(r-1)/r B_{r-1} - sigma_r",
    ],
    verified_against=[
        "direct Laurent expansion of S_4 = 10/[c(5c+22)] at c=infinity",
    ],
    disjoint_rationale=(
        "Integer recurrence on rational coefficients (chain A) vs "
        "symbolic geometric-series expansion of the explicit S_4 closed "
        "form (chain B); the two chains share only S_4 as base datum."),
)
def test_subleading_r4_base_case():
    """At r=4: B_4 = -44/5 (geometric-series base of the tower)."""
    assert subleading_asymptotic(4) == Rational(-44, 5)
    # Chain B verification
    c = symbols("c")
    S4 = lambda cc: Rational(10) / (cc * (5 * cc + 22))
    assert _laurent_subleading(S4, 4) == Rational(-44, 5)


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "variation-of-parameters recurrence with empty source at r=5",
    ],
    verified_against=[
        "direct Laurent expansion of S_5 = -48/[c^2(5c+22)] at c=infinity",
    ],
    disjoint_rationale=(
        "The r=5 case has empty cross-pair index set (no j,k with "
        "4<=j<=k<=3), so sigma_5 = 0 and B_5 = -6*4/5 * B_4 only; "
        "chain B verifies by direct geometric-series expansion of S_5."),
)
def test_subleading_r5_empty_source():
    """At r=5: B_5 = 1056/25, pure propagation of B_4 (no source)."""
    assert subleading_asymptotic(5) == Rational(1056, 25)
    c = symbols("c")
    S5 = lambda cc: Rational(-48) / (cc**2 * (5 * cc + 22))
    assert _laurent_subleading(S5, 5) == Rational(1056, 25)


# ---------------------------------------------------------------------------
# Recurrence-driven cases r = 6..10
# ---------------------------------------------------------------------------


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "subleading recurrence with source sigma_6 / A_6 = 1/9 from (4,4) pair",
    ],
    verified_against=[
        "direct Laurent expansion of S_6 closed form at c=infinity",
    ],
    disjoint_rationale=(
        "Chain A extracts sigma_6 = (1/6)*(1/2)*16*A_4^2 = 32/6 from the "
        "diagonal (4,4) term; chain B expands the explicit quartic "
        "denominator of S_6 geometrically. No shared derivation path."),
)
def test_subleading_r6():
    """At r=6: B_6 = -3248/15 (first Riccati-source contribution)."""
    expected = Rational(-3248, 15)
    assert subleading_asymptotic(6) == expected
    assert _laurent_subleading(s6_virasoro, 6) == expected


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "subleading recurrence with source sigma_7 / A_7 = 2/9 from (4,5) pair",
    ],
    verified_against=[
        "direct Laurent expansion of S_7 closed form at c=infinity",
    ],
    disjoint_rationale=(
        "Chain A: sigma_7 = (1/7)*20*A_4*A_5 = (20/7)*2*(-48/5) = -384/7; "
        "chain B: symbolic expansion of S_7 = -2880(15c+61)/[7c^4(5c+22)^2]."),
)
def test_subleading_r7():
    """At r=7: B_7 = 40896/35."""
    expected = Rational(40896, 35)
    assert subleading_asymptotic(7) == expected
    assert _laurent_subleading(s7_virasoro, 7) == expected


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "subleading recurrence with source from pairs (4,6), (5,5)",
    ],
    verified_against=[
        "direct Laurent expansion of S_8 closed form at c=infinity",
    ],
    disjoint_rationale=(
        "Chain A: sigma_8 = (1/8)*(24*A_4*A_6 + (1/2)*25*A_5^2) = 432; "
        "chain B: expansion of S_8 = 80(2025c^2 + 16470c + 33314)/[c^5(5c+22)^3]."),
)
def test_subleading_r8():
    """At r=8: B_8 = -32832/5."""
    expected = Rational(-32832, 5)
    assert subleading_asymptotic(8) == expected
    assert _laurent_subleading(s8_virasoro, 8) == expected


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "subleading recurrence with source from pairs (4,7), (5,6)",
    ],
    verified_against=[
        "direct Laurent expansion of S_9 closed form at c=infinity",
    ],
    disjoint_rationale=(
        "Chain A: sigma_9 / A_9 = 4/9 from triangular-number telescoping; "
        "chain B: explicit Laurent expansion of the quartic (5c+22)^3 "
        "denominator of S_9."),
)
def test_subleading_r9():
    """At r=9: B_9 = 190464/5."""
    expected = Rational(190464, 5)
    assert subleading_asymptotic(9) == expected
    assert _laurent_subleading(s9_virasoro, 9) == expected


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "subleading recurrence with source from pairs (4,8), (5,7), (6,6)",
    ],
    verified_against=[
        "direct Laurent expansion of S_10 closed form at c=infinity",
    ],
    disjoint_rationale=(
        "Chain A: sigma_10 includes a diagonal (6,6) contribution with "
        "f=1/2; chain B: expansion of the cubic (5c+22)^4 denominator of "
        "S_10."),
)
def test_subleading_r10():
    """At r=10: B_10 = -5660928/25."""
    expected = Rational(-5660928, 25)
    assert subleading_asymptotic(10) == expected
    assert _laurent_subleading(s10_virasoro, 10) == expected


# ---------------------------------------------------------------------------
# Combinatorial identity (lem:subleading-combinatorial-identity)
# ---------------------------------------------------------------------------


@independent_verification(
    claim="lem:subleading-combinatorial-identity",
    derived_from=[
        "parity case analysis of index set {(j,k): j+k=r+2, 4<=j<=k<=r-2}",
    ],
    verified_against=[
        "direct enumeration over integer pairs for r = 5, 6, ..., 12",
    ],
    disjoint_rationale=(
        "Parity case analysis (chain A) is integer arithmetic on ceilings; "
        "direct enumeration (chain B) iterates over the finite index set "
        "pair by pair. No shared derivation path."),
)
def test_combinatorial_identity_f_sum():
    """Sum_{j+k=r+2, 4<=j<=k<=r-2} f(j,k) = (r-5)/2 for r = 5..12."""
    for r in range(5, 13):
        total = Rational(0)
        for j in range(4, (r + 2) // 2 + 1):
            k = r + 2 - j
            if k < j or k > r - 2 or k < 4:
                continue
            f = Rational(1, 2) if j == k else Rational(1)
            total += f
        expected = Rational(r - 5, 2)
        assert total == expected, f"Failed at r={r}: got {total}, expected {expected}"


# ---------------------------------------------------------------------------
# Source-to-leading ratio (proof Step 3 of thm:shadow-tower-subleading-closed-form)
# ---------------------------------------------------------------------------


@independent_verification(
    claim="thm:shadow-tower-subleading-closed-form",
    derived_from=[
        "closed form A_r = 8*(-6)^(r-4)/r combined with combinatorial identity",
    ],
    verified_against=[
        "direct computation of sigma_r / A_r from explicit A_j, A_k values",
    ],
    disjoint_rationale=(
        "Chain A derives sigma_r / A_r = (r-5)/9 via the symbolic identity "
        "j*k*A_j*A_k = 64*(-6)^(r-6); chain B evaluates the sum numerically "
        "using explicit A_j values for each r. The two chains share only "
        "the closed-form A_r; the combinatorial identity is used only in A."),
)
def test_source_to_leading_ratio():
    """sigma_r / A_r = (r-5)/9 for r = 5..11."""
    for r in range(5, 12):
        sig = Rational(0)
        for j in range(4, (r + 2) // 2 + 1):
            k = r + 2 - j
            if k < j or k > r - 2 or k < 4:
                continue
            f = Rational(1, 2) if j == k else Rational(1)
            sig += f * j * k * leading_asymptotic(j) * leading_asymptotic(k)
        sig = sig / r
        ratio = sig / leading_asymptotic(r)
        expected = Rational(r - 5, 9)
        assert ratio == expected, f"Failed at r={r}: got {ratio}, expected {expected}"


# ---------------------------------------------------------------------------
# Characteristic-prime layer (cor:subleading-characteristic-primes)
# ---------------------------------------------------------------------------


def test_subleading_polynomial_positivity():
    """q(r) = 5 r^2 - 45 r + 496 is positive for all real r.

    Discriminant -7895 < 0 (elementary); q(9/2) = 1579/4 is the minimum.
    """
    for r in range(-20, 30):
        assert subleading_polynomial(r) > 0
    assert subleading_polynomial(Rational(9, 2)) == Rational(1579, 4)


def test_subleading_primes_not_kummer_through_r_11():
    """Characteristic primes of q(r) for r<=11 are below 691 (first Kummer)."""
    KUMMER_IRREGULAR_LEADING = {691, 3617}
    for r in range(4, 12):
        q_r = int(subleading_polynomial(r))
        # factor q_r
        n = q_r
        d = 2
        primes = set()
        while d * d <= n:
            while n % d == 0:
                primes.add(d)
                n //= d
            d += 1
        if n > 1:
            primes.add(n)
        assert primes.isdisjoint(KUMMER_IRREGULAR_LEADING), (
            f"r={r}: q(r) = {q_r} has prime factors {primes} "
            f"intersecting Kummer-irregular leading set."
        )
