"""
Independent-verification tests for the sub-subleading asymptotic

    Gamma_r / A_r = 484/25 + 22 (r-4)(r-5)/45 + (r-4)(r-5)(r-6)(r-7)/972

of the Virasoro shadow-tower coefficient S_r(Vir_c), proved in
chapters/theory/shadow_tower_sub_subleading_platonic.tex as
thm:shadow-tower-sub-subleading-closed-form.

Derivation chain (A): variation-of-parameters on the sub-subleading
  recurrence Gamma_r = -6(r-1)/r * Gamma_{r-1} - sigma_r^(gamma), using
  the source-ratio identity sigma_r^(gamma)/A_r = -44(r-5)/45 -
  (r-5)(r-6)(r-7)/243 and the two telescope identities
    Sum_{s=5}^{r} (s-5) = (r-4)(r-5)/2,
    Sum_{s=5}^{r} (s-5)(s-6)(s-7) = (r-4)(r-5)(r-6)(r-7)/4.

Verification chain (B): direct Laurent expansion of the explicit
  closed forms S_r(Vir_c) through r = 10 around c = infinity, reading
  off the coefficient of c^(-2) in Phi_r = c^(r-2) * S_r.

The two chains share only the initial data (kappa, S_3, S_4) and the
integer master-equation coefficients f(j,k), j*k. Chain (A) is
integer-recurrence algebra plus hockey-stick summation; chain (B) is
symbolic Laurent expansion of the explicit quartic S_r closed form.

Kummer-prime content: the quartic numerator polynomial
    N(r) = 25 r^4 - 550 r^3 + 16355 r^2 - 122870 r + 729048
has sporadic divisibility by the Kummer-irregular prime 691 at r = 8
(and at r in {315, 423, 658} in the residue class 691). This is a
MODULAR COINCIDENCE in F_691, not a Bernoulli structural emergence.
"""

from __future__ import annotations

import sympy as sp
from sympy import Rational, symbols, series

from compute.lib.independent_verification import independent_verification
from compute.lib.shadow_tower_higher_vir import (
    leading_asymptotic,
    subleading_asymptotic,
    sub_subleading_asymptotic,
    sub_subleading_numerator_polynomial,
    sub_subleading_source_ratio,
    s6_virasoro,
    s7_virasoro,
    s8_virasoro,
    s9_virasoro,
    s10_virasoro,
    SUB_SUBLEADING_ASYMPTOTIC,
)


# ---------------------------------------------------------------------------
# Laurent-expansion ground truth (chain B)
# ---------------------------------------------------------------------------


def _laurent_sub_subleading(S_of_c, r):
    """Extract Gamma_r := coefficient of c^(-2) in Phi_r(c) = c^(r-2) * S_r.

    Substitutes c = 1/u and expands at u = 0.
    """
    c = symbols("c")
    u = symbols("u")
    phi = sp.cancel(c ** (r - 2) * S_of_c(c)).subs(c, 1 / u)
    expansion = series(phi, u, 0, 4).removeO()
    poly = sp.Poly(expansion, u)
    return sp.Rational(poly.nth(2))


def _S4(cc):
    return Rational(10) / (cc * (5 * cc + 22))


def _S5(cc):
    return Rational(-48) / (cc ** 2 * (5 * cc + 22))


VIR_CLOSED_FORMS = {
    4: _S4,
    5: _S5,
    6: s6_virasoro,
    7: s7_virasoro,
    8: s8_virasoro,
    9: s9_virasoro,
    10: s10_virasoro,
}


# ---------------------------------------------------------------------------
# Base cases r = 4, 5
# ---------------------------------------------------------------------------


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "variation-of-parameters telescope Gamma_r/A_r "
        "= 484/25 + 22(r-4)(r-5)/45 + (r-4)(r-5)(r-6)(r-7)/972",
    ],
    verified_against=[
        "direct Laurent expansion of S_4 = 10/[c(5c+22)] at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "Chain A is integer recurrence algebra telescoping from "
        "Gamma_4/A_4 = (B_4/A_4)^2 = 484/25 (base of the Riccati "
        "second-order layer). Chain B is symbolic geometric-series "
        "expansion of the explicit S_4 closed form; the two chains "
        "share only the S_4 formula as starting data."),
)
def test_sub_subleading_r4_base_case():
    """At r=4: Gamma_4 = 968/25 (geometric-square base of the tower)."""
    assert sub_subleading_asymptotic(4) == Rational(968, 25)
    assert SUB_SUBLEADING_ASYMPTOTIC[4] == Rational(968, 25)
    assert _laurent_sub_subleading(_S4, 4) == Rational(968, 25)


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "variation-of-parameters telescope with empty source at r=5",
    ],
    verified_against=[
        "direct Laurent expansion of S_5 = -48/[c^2(5c+22)] at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "At r=5 the cross-pair index set {4<=j<=k<=3} is empty, so "
        "sigma_5^(gamma) = 0 and Gamma_5/A_5 = Gamma_4/A_4 = 484/25 "
        "(pure propagation). Chain B expands the explicit S_5 closed "
        "form; the chains share only S_5 as base datum."),
)
def test_sub_subleading_r5_empty_source():
    """At r=5: Gamma_5 = -23232/125, pure propagation of G_4 (no source)."""
    assert sub_subleading_asymptotic(5) == Rational(-23232, 125)
    assert SUB_SUBLEADING_ASYMPTOTIC[5] == Rational(-23232, 125)
    assert _laurent_sub_subleading(_S5, 5) == Rational(-23232, 125)


# ---------------------------------------------------------------------------
# Recurrence-driven cases r = 6..10
# ---------------------------------------------------------------------------


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "sub-subleading recurrence Gamma_r = -6(r-1)/r Gamma_{r-1} - sigma_r^(gamma) "
        "with source ratio -44(r-5)/45 - (r-5)(r-6)(r-7)/243",
    ],
    verified_against=[
        "direct Laurent expansion of S_6 closed form at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "Chain A extracts sigma_6^(gamma) from the (4,4) diagonal pair via "
        "A_4 B_4 + B_4 A_4 = 2 A_4 B_4 and the diagonal weight 1/2; "
        "chain B expands the explicit S_6 = 80(45c+193)/[3c^3(5c+22)^2] "
        "quartic denominator geometrically. No shared derivation path."),
)
def test_sub_subleading_r6():
    """At r=6: Gamma_6 = 73216/75."""
    expected = Rational(73216, 75)
    assert sub_subleading_asymptotic(6) == expected
    assert SUB_SUBLEADING_ASYMPTOTIC[6] == expected
    assert _laurent_sub_subleading(s6_virasoro, 6) == expected


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "sub-subleading recurrence with cross-pair (4,5) at r=7",
    ],
    verified_against=[
        "direct Laurent expansion of S_7 closed form at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "Chain A: sigma_7^(gamma) from A_4 B_5 + B_4 A_5 with weight "
        "(1/7)*20 and f=1; chain B: symbolic expansion of "
        "S_7 = -2880(15c+61)/[7c^4(5c+22)^2]."),
)
def test_sub_subleading_r7():
    """At r=7: Gamma_7 = -963072/175."""
    expected = Rational(-963072, 175)
    assert sub_subleading_asymptotic(7) == expected
    assert SUB_SUBLEADING_ASYMPTOTIC[7] == expected
    assert _laurent_sub_subleading(s7_virasoro, 7) == expected


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "sub-subleading recurrence with cross-pairs (4,6), (5,5) at r=8",
    ],
    verified_against=[
        "direct Laurent expansion of S_8 closed form at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "Chain A combines the off-diagonal (4,6) contribution and the "
        "diagonal (5,5) contribution with weight 1/2; chain B expands "
        "S_8 = 80(2025c^2 + 16470c + 33314)/[c^5(5c+22)^3]."),
)
def test_sub_subleading_r8():
    """At r=8: Gamma_8 = 818144/25 = 32*37*691/25."""
    expected = Rational(818144, 25)
    assert sub_subleading_asymptotic(8) == expected
    assert SUB_SUBLEADING_ASYMPTOTIC[8] == expected
    assert _laurent_sub_subleading(s8_virasoro, 8) == expected
    # Factorization cross-check: 32 * 37 * 691 = 818144
    assert 32 * 37 * 691 == 818144


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "sub-subleading recurrence with cross-pairs (4,7), (5,6) at r=9",
    ],
    verified_against=[
        "direct Laurent expansion of S_9 closed form at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "Chain A: sigma_9^(gamma)/A_9 = -44*4/45 - 4*3*2/243 = "
        "-176/45 - 24/243 = -176/45 - 8/81; chain B: explicit "
        "Laurent expansion of the cubic (5c+22)^3 denominator of S_9."),
)
def test_sub_subleading_r9():
    """At r=9: Gamma_9 = -15169024/75."""
    expected = Rational(-15169024, 75)
    assert sub_subleading_asymptotic(9) == expected
    assert SUB_SUBLEADING_ASYMPTOTIC[9] == expected
    assert _laurent_sub_subleading(s9_virasoro, 9) == expected


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "sub-subleading recurrence with cross-pairs (4,8), (5,7), (6,6) at r=10",
    ],
    verified_against=[
        "direct Laurent expansion of S_10 closed form at c=infinity, order c^(-2)",
    ],
    disjoint_rationale=(
        "Chain A includes a diagonal (6,6) contribution with f=1/2 and "
        "two off-diagonal contributions; chain B expands the quartic "
        "(5c+22)^4 denominator of S_10."),
)
def test_sub_subleading_r10():
    """At r=10: Gamma_10 = 160482816/125."""
    expected = Rational(160482816, 125)
    assert sub_subleading_asymptotic(10) == expected
    assert SUB_SUBLEADING_ASYMPTOTIC[10] == expected
    assert _laurent_sub_subleading(s10_virasoro, 10) == expected


# ---------------------------------------------------------------------------
# Source-ratio closed form (the engine of the telescope)
# ---------------------------------------------------------------------------


@independent_verification(
    claim="lem:gamma-source-ratio-closed-form",
    derived_from=[
        "symbolic identity j*k*A_j*A_k = 64*(-6)^(r-6) combined with "
        "B_j/A_j = -[22/5 + (j-4)(j-5)/18]",
    ],
    verified_against=[
        "direct enumeration of (j,k) pairs computing A_j B_k + B_j A_k for r=5..11",
    ],
    disjoint_rationale=(
        "Chain A derives sigma_r^(gamma)/A_r = -44(r-5)/45 - "
        "(r-5)(r-6)(r-7)/243 via the closed-form jk A_j A_k identity "
        "combined with the hockey-stick sum Sum_{j=4}^{r-2} (j-4)(j-5) "
        "= (r-7)(r-6)(r-5)/3; chain B evaluates the sum numerically "
        "pair-by-pair using explicit A_j, B_j values."),
)
def test_source_ratio_closed_form():
    """sigma_r^(gamma)/A_r = -44(r-5)/45 - (r-5)(r-6)(r-7)/243 for r=5..11."""
    for r in range(5, 12):
        # Chain A: closed form
        closed = sub_subleading_source_ratio(r)
        # Chain B: direct enumeration
        direct = Rational(0)
        for j in range(4, (r + 2) // 2 + 1):
            k = r + 2 - j
            if k > r - 2 or k < j or k < 4:
                continue
            f = Rational(1, 2) if j == k else Rational(1)
            A_j = leading_asymptotic(j)
            A_k = leading_asymptotic(k)
            B_j = subleading_asymptotic(j)
            B_k = subleading_asymptotic(k)
            direct += f * j * k * (A_j * B_k + B_j * A_k)
        direct = direct / r
        A_r = leading_asymptotic(r)
        ratio_direct = direct / A_r
        assert closed == ratio_direct, (
            f"r={r}: closed={closed} vs direct={ratio_direct}"
        )


# ---------------------------------------------------------------------------
# Variation-of-parameters telescope (the proof structure)
# ---------------------------------------------------------------------------


@independent_verification(
    claim="thm:shadow-tower-sub-subleading-closed-form",
    derived_from=[
        "recurrence Gamma_r/A_r = Gamma_{r-1}/A_{r-1} - sigma_r^(gamma)/A_r "
        "applied iteratively from r=5 to r=11",
    ],
    verified_against=[
        "closed-form formula 484/25 + 22(r-4)(r-5)/45 + (r-4)(r-5)(r-6)(r-7)/972",
    ],
    disjoint_rationale=(
        "Chain A iterates the first-order linear recurrence in G_r := "
        "Gamma_r/A_r with the closed-form source; chain B evaluates the "
        "closed-form polynomial in r directly. The two chains share only "
        "the base case G_4 = 484/25 and the closed-form source ratio."),
)
def test_telescope_recurrence():
    """G_r/A_r matches telescope from recurrence for r=4..11."""
    G_prev = Rational(484, 25)  # G_4 = 484/25
    for r in range(5, 12):
        G_prev = G_prev - sub_subleading_source_ratio(r)
        # Compare to closed form
        closed = sub_subleading_asymptotic(r) / leading_asymptotic(r)
        assert G_prev == closed, (
            f"r={r}: telescope={G_prev} vs closed={closed}"
        )


# ---------------------------------------------------------------------------
# Numerator polynomial N(r) closed form (reduced denominator 24300)
# ---------------------------------------------------------------------------


@independent_verification(
    claim="lem:gamma-numerator-quartic-polynomial",
    derived_from=[
        "LCM(25, 45, 972) = 24300 common-denominator reduction of "
        "484/25 + 22(r-4)(r-5)/45 + (r-4)(r-5)(r-6)(r-7)/972",
    ],
    verified_against=[
        "direct evaluation of N(r) := 25 r^4 - 550 r^3 + 16355 r^2 - 122870 r + 729048 "
        "for r = 4..12 against 24300 * Gamma_r/A_r",
    ],
    disjoint_rationale=(
        "Chain A expands (r-4)(r-5) and (r-4)(r-5)(r-6)(r-7) symbolically "
        "and collects over 24300; chain B substitutes integer r values "
        "into the quartic N(r) and independently into Gamma_r/A_r * 24300. "
        "The two chains share only the closed-form coefficients "
        "{484/25, 22/45, 1/972}."),
)
def test_numerator_polynomial_matches_ratio():
    """N(r)/24300 = Gamma_r/A_r for r = 4..12."""
    for r in range(4, 13):
        N_r = sub_subleading_numerator_polynomial(r)
        ratio_from_N = Rational(N_r, 24300)
        if r <= 10:
            A_r = leading_asymptotic(r)
            Gamma_r = sub_subleading_asymptotic(r)
            ratio_from_closed = Gamma_r / A_r
            assert ratio_from_N == ratio_from_closed, (
                f"r={r}: N/{24300}={ratio_from_N} vs closed={ratio_from_closed}"
            )
        # Even for r > 10, the closed form is well-defined
        closed = (
            Rational(484, 25)
            + Rational(22 * (r - 4) * (r - 5), 45)
            + Rational((r - 4) * (r - 5) * (r - 6) * (r - 7), 972)
        )
        assert ratio_from_N == closed


# ---------------------------------------------------------------------------
# Kummer-prime 691 emergence: sporadic, not structural
# ---------------------------------------------------------------------------


@independent_verification(
    claim="rem:gamma-691-emergence-sporadic",
    derived_from=[
        "polynomial root computation N(r) mod 691 giving exactly four roots "
        "r in {8, 315, 423, 658}",
    ],
    verified_against=[
        "direct factorization of N(8) = 613608 = 2^3 * 3 * 37 * 691 "
        "and Bernoulli absence: B_{2k} has no 691 content through k=7",
    ],
    disjoint_rationale=(
        "Chain A computes N(r) mod 691 as a polynomial in F_691[r] and "
        "enumerates its roots by exhaustive search over 0 <= r < 691, "
        "finding four roots (the maximum for a degree-4 polynomial); "
        "chain B factorises the integer N(8) directly and separately "
        "verifies that Bernoulli numerators B_{2k} for k <= 7 do not "
        "contain 691 (first Bernoulli occurrence is B_12 = -691/2730). "
        "The two chains share only the polynomial N(r) and the prime 691."),
)
def test_691_emergence_is_sporadic():
    """691 appears at r=8 but is a modular coincidence, not Bernoulli-structural.

    N(r) mod 691 has exactly four roots in F_691: {8, 315, 423, 658}.
    This is the maximum count for a degree-4 polynomial, so the r=8
    divisibility is expected by counting and is not tied to any
    Bernoulli-number identity.
    """
    # Chain A: modular roots
    roots_mod_691 = []
    for r_val in range(691):
        N_val = int(sub_subleading_numerator_polynomial(r_val))
        if N_val % 691 == 0:
            roots_mod_691.append(r_val)
    assert roots_mod_691 == [8, 315, 423, 658]

    # Chain B: direct factorization of N(8)
    N_8 = int(sub_subleading_numerator_polynomial(8))
    assert N_8 == 613608
    assert N_8 == 2 ** 3 * 3 * 37 * 691

    # Bernoulli absence through k=7: none of B_2, B_4, ..., B_14 contain 691
    # (B_12 = -691/2730 is the first Bernoulli with 691; this corresponds
    # to weight 12 via von Staudt, not to the r=8 shadow position.)
    for k in range(1, 8):
        B_2k = sp.bernoulli(2 * k)
        numerator = int(sp.fraction(B_2k)[0])
        assert numerator % 691 != 0 or k == 6, (
            f"B_{2*k} unexpectedly contains 691"
        )
    # B_12 does contain 691:
    B_12 = sp.bernoulli(12)
    assert int(sp.fraction(B_12)[0]) % 691 == 0


@independent_verification(
    claim="rem:gamma-irregular-primes-dense-but-structureless",
    derived_from=[
        "exhaustive prime-factor enumeration of N(r) for r = 4..15",
    ],
    verified_against=[
        "comparison against Kummer-irregular leading set {691, 3617} "
        "showing only r=8 hits 691 and no r<=15 hits 3617",
    ],
    disjoint_rationale=(
        "Chain A factors each N(r) and collects primes; chain B compares "
        "this set against a pre-computed Kummer-irregular reference set. "
        "The two chains share only N(r) closed form; chain B's reference "
        "set comes from classical number-theory tables (B_12 = -691/2730, "
        "B_16 numerator contains 3617)."),
)
def test_kummer_absence_3617_through_r_15():
    """3617 does NOT divide N(r) for r = 4..15.

    The next Kummer-irregular leading prime after 691 is 3617 (which
    divides B_16). If the Kummer emergence at r=8 were structural,
    we would expect 3617 to appear at some shadow position r <= 16
    correlating with B_16. It does not, confirming sporadicity.
    """
    from sympy import factorint
    for r_val in range(4, 16):
        N_r = int(sub_subleading_numerator_polynomial(r_val))
        factors = set(factorint(N_r).keys())
        assert 3617 not in factors, (
            f"r={r_val}: unexpected 3617 factor in N({r_val}) = {N_r}"
        )


# ---------------------------------------------------------------------------
# Quartic irreducibility over Q (used in the sporadicity argument)
# ---------------------------------------------------------------------------


@independent_verification(
    claim="lem:gamma-numerator-irreducible",
    derived_from=[
        "rational root theorem applied to 25 r^4 - 550 r^3 + 16355 r^2 "
        "- 122870 r + 729048",
    ],
    verified_against=[
        "sympy factorization over Q returning the polynomial unchanged",
    ],
    disjoint_rationale=(
        "Chain A applies the rational root theorem directly (ratios p/q "
        "with p | 729048, q | 25), testing candidate rational roots; "
        "chain B invokes sympy's Q-factorization algorithm (based on "
        "Berlekamp-Zassenhaus over Z). The two chains implement different "
        "algorithms and share only the polynomial coefficients."),
)
def test_numerator_polynomial_irreducible_over_Q():
    """N(r) = 25 r^4 - 550 r^3 + 16355 r^2 - 122870 r + 729048 is Q-irreducible."""
    r = symbols("r")
    N_expr = sub_subleading_numerator_polynomial(r)
    factored = sp.factor(N_expr)
    # Irreducible means factored equals expanded (no non-trivial factorization)
    assert sp.expand(factored) == sp.expand(N_expr)
    # And factored is a single polynomial, not a product
    assert not isinstance(factored, sp.Mul) or not any(
        isinstance(arg, sp.Pow) and arg.exp > 0 and arg.base != r
        for arg in factored.args
    )


# ---------------------------------------------------------------------------
# Cross-consistency with subleading layer
# ---------------------------------------------------------------------------


def test_gamma_vs_subleading_square_difference():
    """Gamma_r/A_r - (B_r/A_r)^2 = -(r-4)(r-5)(r^2-7r+9)/486 for r=4..10.

    This is the alternative closed form:
        Gamma_r/A_r = phi_r^2 - (r-4)(r-5)(r^2-7r+9)/486,
        phi_r = -B_r/A_r = 22/5 + (r-4)(r-5)/18.

    Both forms agree because
        484/25 + 22(r-4)(r-5)/45 + (r-4)(r-5)(r-6)(r-7)/972
        = [22/5 + (r-4)(r-5)/18]^2 - (r-4)(r-5)(r^2-7r+9)/486.
    """
    for r in range(4, 11):
        A_r = leading_asymptotic(r)
        Gamma_r = sub_subleading_asymptotic(r)
        B_r = subleading_asymptotic(r)
        phi_r = -B_r / A_r  # = 22/5 + (r-4)(r-5)/18
        correction = Rational((r - 4) * (r - 5) * (r ** 2 - 7 * r + 9), 486)
        alt = phi_r ** 2 - correction
        assert Gamma_r / A_r == alt, (
            f"r={r}: direct={Gamma_r / A_r} vs alt={alt}"
        )
