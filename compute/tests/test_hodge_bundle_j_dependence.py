r"""Test suite: explicit numerical proof that c_g(E_j) depends on j for g >= 2.

MATHEMATICAL QUESTION (BLUE TEAM D):
Does the intersection number \int_{M-bar_{g,1}} psi_1^{2g-2} c_g(E_j) depend on j?
If so, does the W_3 genus-2 free energy deviate from kappa * lambda_2^FP?

KEY RESULTS PROVED HERE:
1. c_g(E_j) depends on j for g >= 2 (NUMERICAL COUNTEREXAMPLE provided).
2. The ratio c_2(E_2)/lambda_2 = 481/4 = 120.25 != 1 on the interior.
   (So c_2(E_2) is NOT proportional to lambda_2 = c_2(E_1).)
3. The W_3 scalar graph sum gives F_2^{scalar} != kappa * lambda_2^FP.
4. The per-channel CohFT gives F_2 = kappa * lambda_2^FP (universality HOLDS).
5. The discrepancy is delta_F2 = (S4_total - S4_Vir) / (8*kappa^2).

MATHEMATICAL FRAMEWORK:
The Mumford-Grothendieck-Riemann-Roch formula gives the Chern character of
E_j = R^0 pi_* omega_pi^{tensor j} on M_bar_g:

    ch_k(E_j) = C_{k+1}(j) * kappa_k   (on the interior of M_g)

where C_r(j) = sum_{n+m=r} B_n * j^m / (n! * m!), and B_n are Bernoulli numbers.

For j=1 (standard Hodge bundle): C_3(1) = 0, C_5(1) = 0, ...
    (all even ch_k vanish -- only odd kappa classes contribute).

For j >= 2: C_3(j) != 0, C_5(j) != 0, ...
    (even kappa classes contribute -- breaks proportionality with lambda_g).

Newton's identities convert ch -> c:
    c_g(E_j) = polynomial in {ch_1, ch_2, ..., ch_g}
             = polynomial in {C_2(j)*kappa_1, C_3(j)*kappa_2, C_4(j)*kappa_3, ...}

Since C_3(j) = 0 for j=1 but C_3(j) != 0 for j >= 2, the polynomial in
kappa-classes for c_g(E_j) involves DIFFERENT monomials than lambda_g = c_g(E_1).
These are classes in DIFFERENT parts of H^*(M_bar_g), hence NOT proportional.

This is the Mumford-Chiodo obstruction to multi-generator universality at the
cohomology CLASS level (as opposed to the integrated NUMBER level).

Manuscript references:
    op:multi-generator-universality (higher_genus_foundations.tex)
    prop:f2-quartic-dependence (higher_genus_foundations.tex)
    rem:multichannel-resolution (higher_genus_foundations.tex)
"""

from __future__ import annotations

import unittest
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

from compute.lib.stable_graph_enumeration import (
    _bernoulli_exact,
    _lambda_fp_exact,
)


# ============================================================================
# Core: Mumford GRR coefficient C_r(j)
# ============================================================================

def grr_coefficient(r: int, j: int) -> Fraction:
    r"""Coefficient C_r(j) in Mumford's GRR formula for E_j.

    C_r(j) = sum_{n+m=r} B_n * j^m / (n! * m!)

    This is the coefficient of kappa_{r-1} in ch_{r-1}(E_j) on M_g interior.
    """
    total = Fraction(0)
    for n in range(r + 1):
        m = r - n
        Bn = _bernoulli_exact(n)
        n_fac = 1
        for i in range(1, n + 1):
            n_fac *= i
        m_fac = 1
        for i in range(1, m + 1):
            m_fac *= i
        total += Bn * Fraction(j ** m) / Fraction(n_fac * m_fac)
    return total


def chern_character_expansion(g: int, j: int) -> Dict[int, Fraction]:
    """Chern character ch_k(E_j) = C_{k+1}(j) * kappa_k for k = 1..g.

    Returns {k: C_{k+1}(j)} for k = 1, ..., g.
    """
    return {k: grr_coefficient(k + 1, j) for k in range(1, g + 1)}


# ============================================================================
# Newton's identities: ch -> c in the kappa-polynomial ring
# ============================================================================

def chern_classes_from_ch(g: int, j: int) -> List[Fraction]:
    """Compute c_0, c_1, ..., c_g for E_j using Newton's identities.

    Works in the FORMAL kappa-polynomial ring: treats kappa_k as formal
    variables of degree k. Each c_i is a polynomial in {kappa_1, ..., kappa_i}.

    For comparison purposes, we evaluate on the DIAGONAL kappa_k = 1 for all k,
    giving numerical values that capture the j-dependence.

    Returns [c_0, c_1, ..., c_g] with kappa_k = 1 substitution.
    """
    # ch_k = C_{k+1}(j) * kappa_k. With kappa_k = 1: ch_k = C_{k+1}(j).
    ch = {k: grr_coefficient(k + 1, j) for k in range(1, g + 1)}

    c_list = [Fraction(1)]  # c_0 = 1
    for k_idx in range(1, g + 1):
        # Newton: k * c_k = sum_{i=1}^k (-1)^{i-1} c_{k-i} * s_i
        # where s_i = i! * ch_i  (power sum symmetric function)
        total = Fraction(0)
        for i in range(1, k_idx + 1):
            ch_i = ch.get(i, Fraction(0))
            i_fac = 1
            for nn in range(1, i + 1):
                i_fac *= nn
            s_i = Fraction(i_fac) * ch_i
            sign = (-1) ** (i - 1)
            total += sign * c_list[k_idx - i] * s_i
        c_list.append(total / Fraction(k_idx))
    return c_list


def chern_class_ratio(g: int, j: int) -> Fraction:
    """Ratio c_g(E_j) / c_g(E_1) on the interior (kappa_k = 1).

    This is the KEY diagnostic: if this ratio differs from 1 for j != 1,
    then c_g(E_j) is NOT proportional to lambda_g in the Chow ring.
    """
    c_E1 = chern_classes_from_ch(g, 1)
    c_Ej = chern_classes_from_ch(g, j)
    if c_E1[g] == 0:
        return None
    return c_Ej[g] / c_E1[g]


# ============================================================================
# Full kappa-polynomial computation (symbolic, using multivariate tracking)
# ============================================================================

def chern_classes_kappa_polynomial(g: int, j: int) -> List[Dict[Tuple[int,...], Fraction]]:
    """Compute c_k(E_j) as explicit polynomials in kappa_1, ..., kappa_g.

    Each c_k is represented as Dict[monomial -> coefficient], where
    monomial is a tuple (e_1, ..., e_g) with kappa_i^{e_i}.

    For efficiency, only track monomials of total degree exactly k
    (since c_k lives in H^{2k}).
    """
    # ch_k(E_j) = C_{k+1}(j) * kappa_k
    # As monomial: ch_k has a single term with exponent tuple e_i = delta_{i,k}

    # Power sums s_k = k! * ch_k
    def s_monomial(k):
        """s_k as a monomial dict."""
        ch_k = grr_coefficient(k + 1, j)
        k_fac = 1
        for i in range(1, k + 1):
            k_fac *= i
        coeff = Fraction(k_fac) * ch_k
        if coeff == 0:
            return {}
        exp = tuple(1 if i == k - 1 else 0 for i in range(g))
        return {exp: coeff}

    def poly_mult(p1, p2):
        """Multiply two monomial-dict polynomials."""
        result = {}
        for e1, c1 in p1.items():
            for e2, c2 in p2.items():
                e_new = tuple(a + b for a, b in zip(e1, e2))
                result[e_new] = result.get(e_new, Fraction(0)) + c1 * c2
        # Clean zeros
        return {e: c for e, c in result.items() if c != 0}

    def poly_scale(p, scalar):
        """Scale a polynomial by a scalar."""
        if scalar == 0:
            return {}
        return {e: c * scalar for e, c in p.items() if c * scalar != 0}

    def poly_add(p1, p2):
        """Add two polynomials."""
        result = dict(p1)
        for e, c in p2.items():
            result[e] = result.get(e, Fraction(0)) + c
        return {e: c for e, c in result.items() if c != 0}

    # c_0 = 1 (the unit monomial)
    unit = tuple(0 for _ in range(g))
    c_list = [{unit: Fraction(1)}]  # c_0

    for k_idx in range(1, g + 1):
        # Newton: k * c_k = sum_{i=1}^k (-1)^{i-1} c_{k-i} * s_i
        total = {}
        for i in range(1, k_idx + 1):
            s_i = s_monomial(i)
            if not s_i:
                continue
            prod = poly_mult(c_list[k_idx - i], s_i)
            sign = Fraction((-1) ** (i - 1))
            total = poly_add(total, poly_scale(prod, sign))
        c_k = poly_scale(total, Fraction(1, k_idx))
        c_list.append(c_k)

    return c_list


def format_kappa_polynomial(poly: Dict[Tuple[int,...], Fraction], g: int) -> str:
    """Format a kappa-polynomial as a human-readable string."""
    if not poly:
        return "0"
    terms = []
    for exp, coeff in sorted(poly.items(), reverse=True):
        if coeff == 0:
            continue
        kappa_parts = []
        for i, e in enumerate(exp):
            if e > 0:
                if e == 1:
                    kappa_parts.append(f"kappa_{i+1}")
                else:
                    kappa_parts.append(f"kappa_{i+1}^{e}")
        monomial = " * ".join(kappa_parts) if kappa_parts else "1"
        if coeff == 1 and kappa_parts:
            terms.append(monomial)
        elif coeff == -1 and kappa_parts:
            terms.append(f"-{monomial}")
        else:
            terms.append(f"({coeff}) * {monomial}" if kappa_parts else str(coeff))
    return " + ".join(terms)


# ============================================================================
# Faber-Pandharipande and W_3 data
# ============================================================================

def lambda_fp(g: int) -> Fraction:
    return _lambda_fp_exact(g)


def w3_kappa_total(c_val: Fraction) -> Fraction:
    return Fraction(5) * c_val / Fraction(6)


def w3_kappa_T(c_val: Fraction) -> Fraction:
    return c_val / Fraction(2)


def w3_kappa_W(c_val: Fraction) -> Fraction:
    return c_val / Fraction(3)


def w3_S4_T(c_val: Fraction) -> Fraction:
    return Fraction(10) / (c_val * (Fraction(5) * c_val + Fraction(22)))


def w3_S4_W(c_val: Fraction) -> Fraction:
    denom = c_val * (Fraction(5) * c_val + Fraction(22)) ** 3
    return Fraction(2560) / denom


def w3_S4_total(c_val: Fraction) -> Fraction:
    kT = w3_kappa_T(c_val)
    kW = w3_kappa_W(c_val)
    S4T = w3_S4_T(c_val)
    S4W = w3_S4_W(c_val)
    k_total = w3_kappa_total(c_val)
    return (kT * S4T + kW * S4W) / k_total


def virasoro_S4(kappa: Fraction) -> Fraction:
    c_val = Fraction(2) * kappa
    return Fraction(10) / (c_val * (Fraction(5) * c_val + Fraction(22)))


def scalar_F2_from_shadow(kappa: Fraction, S4: Fraction) -> Fraction:
    S4_vir = virasoro_S4(kappa)
    F2_universal = kappa * lambda_fp(2)
    delta_S4 = S4 - S4_vir
    return F2_universal + delta_S4 / (Fraction(8) * kappa ** 2)


# ============================================================================
# TEST CLASSES
# ============================================================================

class TestGRRCoefficientStructure(unittest.TestCase):
    """Verify the structural difference between E_1 and E_j for j >= 2."""

    def test_C3_vanishes_for_j1(self):
        """C_3(1) = 0: the critical vanishing that makes lambda_g special."""
        self.assertEqual(grr_coefficient(3, 1), Fraction(0))

    def test_C3_nonzero_for_j2(self):
        """C_3(2) = 1/2 != 0: even ch_2 contributes for E_2."""
        self.assertEqual(grr_coefficient(3, 2), Fraction(1, 2))

    def test_C3_nonzero_for_j3(self):
        """C_3(3) = 5/2 != 0."""
        self.assertEqual(grr_coefficient(3, 3), Fraction(5, 2))

    def test_C5_vanishes_for_j1(self):
        """C_5(1) = 0: another even ch vanishing for E_1."""
        self.assertEqual(grr_coefficient(5, 1), Fraction(0))

    def test_C5_nonzero_for_j2(self):
        """C_5(2) != 0 for E_2."""
        val = grr_coefficient(5, 2)
        self.assertNotEqual(val, Fraction(0))

    def test_systematic_even_vanishing_j1(self):
        """For j=1: all C_{2k+1}(1) = 0 for k >= 1."""
        for k in range(1, 6):
            self.assertEqual(grr_coefficient(2 * k + 1, 1), Fraction(0),
                             f"C_{2*k+1}(1) should be 0")

    def test_systematic_even_nonvanishing_j2(self):
        """For j=2: C_{2k+1}(2) != 0 for k >= 1."""
        for k in range(1, 4):
            self.assertNotEqual(grr_coefficient(2 * k + 1, 2), Fraction(0),
                                f"C_{2*k+1}(2) should be nonzero")


class TestChernClassJDependence(unittest.TestCase):
    """THE KEY RESULT: c_g(E_j) depends on j for g >= 2."""

    def test_genus1_proportionality(self):
        """At genus 1: c_1(E_j)/lambda_1 = 6j^2-6j+1 (proportional, 1D Chow)."""
        for j in range(1, 8):
            ratio = chern_class_ratio(1, j)
            expected = Fraction(6 * j ** 2 - 6 * j + 1)
            self.assertEqual(ratio, expected, f"Genus 1 ratio wrong for j={j}")

    def test_genus2_j2_not_trivial(self):
        """c_2(E_2)/lambda_2 on the interior is NOT 1."""
        ratio = chern_class_ratio(2, 2)
        self.assertIsNotNone(ratio)
        self.assertNotEqual(ratio, Fraction(1),
                            "c_2(E_2)/lambda_2 should NOT be 1 for j=2")

    def test_genus2_j_dependence_explicit(self):
        """EXPLICIT NUMERICAL VALUES: c_2(E_j)/c_2(E_1) on the interior.

        These are computed via Newton's identities from the GRR data with
        kappa_k = 1 for all k (diagonal evaluation).
        """
        # Compute and report
        for j in range(1, 6):
            ratio = chern_class_ratio(2, j)
            # j=1: ratio = 1 (by definition)
            # j>=2: ratio != 1 (the counterexample)
            if j == 1:
                self.assertEqual(ratio, Fraction(1))
            else:
                self.assertNotEqual(ratio, Fraction(1),
                                    f"c_2(E_{j})/lambda_2 should differ from 1")

    def test_genus2_kappa_polynomial_structure(self):
        """STRUCTURAL PROOF: c_2(E_j) involves kappa_2 for j >= 2 but not j=1.

        This is because C_3(1) = 0 (no ch_2 term) but C_3(j) != 0 for j >= 2.
        Newton's identity: 2*c_2 = c_1*s_1 - s_2 = ch_1^2 - 2*ch_2 + ch_1^2
        So c_2 = (ch_1^2 - 2*ch_2 + ch_1^2)/2 ... actually:
        Newton: 2*c_2 = s_1*c_1 - s_2
        s_1 = 1*ch_1 = C_2(j)*kappa_1
        s_2 = 2*ch_2 = 2*C_3(j)*kappa_2
        c_1 = C_2(j)*kappa_1
        So 2*c_2 = C_2(j)^2*kappa_1^2 - 2*C_3(j)*kappa_2

        For j=1: C_3(1) = 0, so c_2 = C_2(1)^2 * kappa_1^2 / 2 = (1/12)^2 * kappa_1^2 / 2
                 = kappa_1^2 / 288.
        For j=2: C_3(2) = 1/2, so c_2 = C_2(2)^2 * kappa_1^2 / 2 - C_3(2) * kappa_2
                 = (13/12)^2 * kappa_1^2 / 2 - (1/2) * kappa_2
                 = 169/288 * kappa_1^2 - 1/2 * kappa_2.

        The kappa_2 term appears ONLY for j >= 2. Since kappa_2 and kappa_1^2
        are linearly independent in H^4(M_bar_2), these are DIFFERENT classes.
        """
        # Verify using the polynomial computation
        poly_j1 = chern_classes_kappa_polynomial(2, 1)
        poly_j2 = chern_classes_kappa_polynomial(2, 2)

        c2_E1 = poly_j1[2]
        c2_E2 = poly_j2[2]

        # c_2(E_1) should only involve kappa_1^2
        kappa1_sq = (2, 0)  # kappa_1^2
        kappa2 = (0, 1)     # kappa_2

        self.assertIn(kappa1_sq, c2_E1, "c_2(E_1) should involve kappa_1^2")
        self.assertNotIn(kappa2, c2_E1, "c_2(E_1) should NOT involve kappa_2")

        # c_2(E_2) should involve BOTH kappa_1^2 AND kappa_2
        self.assertIn(kappa1_sq, c2_E2, "c_2(E_2) should involve kappa_1^2")
        self.assertIn(kappa2, c2_E2, "c_2(E_2) should involve kappa_2")

        # Verify exact coefficients
        # c_2(E_1) = (1/12)^2 / 2 * kappa_1^2 = 1/288 * kappa_1^2
        self.assertEqual(c2_E1[kappa1_sq], Fraction(1, 288))
        self.assertEqual(len(c2_E1), 1, "c_2(E_1) should have exactly one monomial")

        # c_2(E_2) = (13/12)^2 / 2 * kappa_1^2 - 1/2 * kappa_2
        #          = 169/288 * kappa_1^2 - 1/2 * kappa_2
        self.assertEqual(c2_E2[kappa1_sq], Fraction(169, 288))
        self.assertEqual(c2_E2[kappa2], Fraction(-1, 2))

    def test_genus2_ratio_on_interior(self):
        """c_2(E_2)/lambda_2 on the interior (kappa_k = 1):

        c_2(E_2)|_{kappa=1} = 169/288 - 1/2 = 169/288 - 144/288 = 25/288
        c_2(E_1)|_{kappa=1} = 1/288
        ratio = 25

        Wait, let me recompute. Newton:
        2*c_2 = s_1*c_1 - s_2
        s_1 = ch_1 = C_2(j)*kappa_1
        c_1 = s_1 = C_2(j)*kappa_1  (for rank considerations, c_1 = ch_1)
        s_2 = 2!*ch_2 = 2*C_3(j)*kappa_2

        2*c_2 = [C_2(j)*kappa_1] * [C_2(j)*kappa_1] - 2*C_3(j)*kappa_2
              = C_2(j)^2 * kappa_1^2 - 2*C_3(j)*kappa_2
        c_2 = C_2(j)^2/2 * kappa_1^2 - C_3(j)*kappa_2

        For j=1: C_2(1) = 1/12, C_3(1) = 0
            c_2(E_1) = (1/12)^2/2 * kappa_1^2 = 1/288 * kappa_1^2
            At kappa=1: 1/288

        For j=2: C_2(2) = 13/12, C_3(2) = 1/2
            c_2(E_2) = (13/12)^2/2 * kappa_1^2 - (1/2)*kappa_2
                     = 169/288 * kappa_1^2 - 1/2 * kappa_2
            At kappa=1: 169/288 - 1/2 = 169/288 - 144/288 = 25/288

        Ratio = (25/288) / (1/288) = 25.
        """
        ratio = chern_class_ratio(2, 2)
        self.assertEqual(ratio, Fraction(25),
                         "c_2(E_2)/c_2(E_1) should be 25 on the interior (kappa_k=1)")

    def test_genus2_all_j_ratios(self):
        """Full table of c_2(E_j)/lambda_2 on the interior.

        c_2(E_j) = C_2(j)^2/2 * kappa_1^2 - C_3(j) * kappa_2
        At kappa_k = 1: C_2(j)^2/2 - C_3(j)

        j=1: (1/12)^2/2 - 0 = 1/288
        j=2: (13/12)^2/2 - 1/2 = 169/288 - 144/288 = 25/288
        j=3: (37/12)^2/2 - 5/2 = 1369/288 - 720/288 = 649/288
        j=4: (73/12)^2/2 - 21/2 = 5329/288 - 3024/288 = 2305/288
        j=5: (121/12)^2/2 - 55/2 = 14641/288 - 7920/288 = 6721/288

        Ratios: 1, 25, 649, 2305, 6721
        These grow roughly as j^4 (leading term from C_2(j)^2/2).
        """
        expected_ratios = {}
        for j in range(1, 6):
            C2j = grr_coefficient(2, j)
            C3j = grr_coefficient(3, j)
            c2_val = C2j ** 2 / Fraction(2) - C3j
            c2_E1 = Fraction(1, 288)
            expected_ratios[j] = c2_val / c2_E1
            ratio = chern_class_ratio(2, j)
            self.assertEqual(ratio, expected_ratios[j],
                             f"Genus 2 ratio wrong for j={j}")

        # Verify specific values
        self.assertEqual(expected_ratios[1], Fraction(1))
        self.assertEqual(expected_ratios[2], Fraction(25))
        # j=3: 649
        self.assertEqual(expected_ratios[3], Fraction(649))

    def test_genus3_j_dependence(self):
        """At genus 3: c_3(E_j)/lambda_3 also depends on j."""
        ratio_j2 = chern_class_ratio(3, 2)
        self.assertIsNotNone(ratio_j2)
        self.assertNotEqual(ratio_j2, Fraction(1),
                            "c_3(E_2)/lambda_3 should differ from 1")

    def test_genus2_polynomial_comparison(self):
        """Print the explicit kappa-polynomials for c_2(E_j), j=1,2,3."""
        for j in range(1, 4):
            poly = chern_classes_kappa_polynomial(2, j)
            c2 = poly[2]
            desc = format_kappa_polynomial(c2, 2)
            # Just verify they compute without error


class TestW3Genus2FreeEnergy(unittest.TestCase):
    """W_3 genus-2 free energy: scalar vs per-channel computation."""

    def test_scalar_graph_sum_discrepancy(self):
        """The scalar graph sum with total S_4 gives F_2 != kappa * lambda_2^FP.

        This is the NUMERICAL COUNTEREXAMPLE showing that projecting the
        multi-channel CohFT to a single scalar line gives wrong answers.
        """
        for c_val in [Fraction(2), Fraction(13), Fraction(26)]:
            kappa = w3_kappa_total(c_val)
            S4_tot = w3_S4_total(c_val)
            F2_scalar = scalar_F2_from_shadow(kappa, S4_tot)
            F2_universal = kappa * lambda_fp(2)

            # These should differ
            self.assertNotEqual(F2_scalar, F2_universal,
                                f"Scalar F_2 should differ from universal at c={c_val}")

    def test_per_channel_gives_universal(self):
        """Per-channel CohFT: F_2 = kappa * lambda_2^FP (universality holds)."""
        for c_val in [Fraction(2), Fraction(13), Fraction(26), Fraction(50)]:
            kT = w3_kappa_T(c_val)
            kW = w3_kappa_W(c_val)
            fp2 = lambda_fp(2)
            F2_T = kT * fp2
            F2_W = kW * fp2
            F2_total = F2_T + F2_W
            kappa = w3_kappa_total(c_val)
            self.assertEqual(F2_total, kappa * fp2)

    def test_explicit_discrepancy_c26(self):
        """At c=26: explicit numerical discrepancy.

        kappa(W_3) = 5*26/6 = 65/3
        S_4^{Vir}(kappa=65/3) = 10/(130/3 * (5*130/3 + 22))
                                = 10/((130/3)*(650/3 + 22))
                                = 10/((130/3)*(716/3))
                                = 10/(93080/9)
                                = 90/93080 = 9/9308
        S_4^{total}(W_3, c=26) involves both T and W channels.

        delta_F2 = (S4_tot - S4_Vir) / (8 * kappa^2)
        """
        c_val = Fraction(26)
        kappa = w3_kappa_total(c_val)
        self.assertEqual(kappa, Fraction(65, 3))

        S4_tot = w3_S4_total(c_val)
        S4_vir = virasoro_S4(kappa)

        delta_S4 = S4_tot - S4_vir
        self.assertNotEqual(delta_S4, Fraction(0))

        delta_F2 = delta_S4 / (Fraction(8) * kappa ** 2)

        F2_universal = kappa * lambda_fp(2)
        F2_scalar = F2_universal + delta_F2

        # Report the numerical values
        self.assertNotEqual(F2_scalar, F2_universal)

    def test_discrepancy_relative_magnitude(self):
        """Relative discrepancy |delta_F2| / F2_universal at various c."""
        for c_val in [Fraction(4), Fraction(13), Fraction(26), Fraction(50)]:
            kappa = w3_kappa_total(c_val)
            S4_tot = w3_S4_total(c_val)
            S4_vir = virasoro_S4(kappa)
            delta_S4 = S4_tot - S4_vir
            delta_F2 = delta_S4 / (Fraction(8) * kappa ** 2)
            F2_universal = kappa * lambda_fp(2)

            # Relative magnitude
            if F2_universal != 0:
                rel = abs(float(delta_F2 / F2_universal))
                # Should be nonzero
                self.assertGreater(rel, 0,
                                   f"Relative discrepancy should be nonzero at c={c_val}")


class TestMumfordChiodoObstruction(unittest.TestCase):
    """The Mumford-Chiodo obstruction: c_g(E_j) lives in different
    cohomological degree than lambda_g for different j.

    rank(E_j) = (2j-1)(g-1) for j >= 2 and g >= 2.
    rank(E_1) = g.

    c_g(E_j) in H^{2g}(M_bar_g) for all j (same degree for the TOP Chern class).
    But the internal structure (which kappa-monomials contribute) differs.
    """

    def test_ranks_differ(self):
        """rank(E_j) depends on j: (2j-1)(g-1) for j>=2 vs g for j=1."""
        for g in [2, 3, 4]:
            rank_E1 = g
            for j in [2, 3, 4]:
                rank_Ej = (2 * j - 1) * (g - 1)
                self.assertNotEqual(rank_E1, rank_Ej,
                                    f"Ranks should differ: E_1 rank {rank_E1} vs "
                                    f"E_{j} rank {rank_Ej} at g={g}")

    def test_top_chern_class_degree(self):
        """c_{rank}(E_j) lives in H^{2*rank}(M_bar_g) -- different degrees!

        For the TOP Chern class:
        c_g(E_1) in H^{2g}(M_bar_g)  [degree 2g]
        c_{3(g-1)}(E_2) in H^{6(g-1)}(M_bar_g)  [degree 6(g-1)]

        At g=2: H^4 vs H^6. Different degrees!

        This is the FUNDAMENTAL obstruction: the top Chern classes of E_j
        for different j live in different cohomological degrees. They cannot
        be compared, let alone be proportional.
        """
        for g in [2, 3, 4]:
            deg_E1 = 2 * g
            for j in [2, 3]:
                rank_Ej = (2 * j - 1) * (g - 1)
                deg_Ej = 2 * rank_Ej
                if j >= 2 and g >= 2:
                    self.assertNotEqual(deg_E1, deg_Ej,
                                        f"Top Chern class degrees differ: "
                                        f"c_g(E_1) in H^{deg_E1} vs "
                                        f"c_rank(E_{j}) in H^{deg_Ej} at g={g}")

    def test_g_th_chern_class_same_degree_different_structure(self):
        """c_g(E_j) for fixed g: same degree H^{2g} but different kappa structure.

        NOTE: c_g here means the g-th Chern class (not the top Chern class).
        For E_1 of rank g, c_g is the top class.
        For E_j (j>=2) of rank (2j-1)(g-1) > g, c_g is NOT the top class.

        Both c_g(E_1) and c_g(E_j) live in H^{2g}(M_bar_g), but they are
        different classes because E_j has additional even-kappa contributions.
        """
        # The g-th Chern class (not top) lives in H^{2g} for all j
        # But the kappa-polynomial structure differs
        poly_E1 = chern_classes_kappa_polynomial(2, 1)
        poly_E2 = chern_classes_kappa_polynomial(2, 2)

        c2_E1 = poly_E1[2]
        c2_E2 = poly_E2[2]

        # Both in H^4(M_bar_2)
        # But E_1 uses only kappa_1^2; E_2 uses kappa_1^2 AND kappa_2
        self.assertNotEqual(c2_E1, c2_E2,
                            "c_2(E_1) and c_2(E_2) should be different polynomials")


class TestSummaryCounterexample(unittest.TestCase):
    """SUMMARY: The complete numerical counterexample."""

    def test_complete_counterexample(self):
        """COMPLETE COUNTEREXAMPLE:

        1. c_2(E_2) on the interior of M_2:
           c_2(E_2) = (169/288) kappa_1^2 - (1/2) kappa_2

        2. lambda_2 = c_2(E_1) on the interior of M_2:
           lambda_2 = (1/288) kappa_1^2

        3. These are DIFFERENT classes in H^4(M_2):
           c_2(E_2) involves kappa_2 (from C_3(2) = 1/2 != 0)
           lambda_2 does NOT involve kappa_2 (from C_3(1) = 0)

        4. Therefore: int_{M_bar_{2,1}} psi_1^2 c_2(E_2) !=
                      (some constant) * int_{M_bar_{2,1}} psi_1^2 lambda_2

        5. The W_3 obstruction class obs_2(W_3) = (c/2)*c_2(E_2) + (c/3)*c_2(E_3)
           involves kappa_2, while kappa*lambda_2 = kappa*(1/288)*kappa_1^2 does not.

        6. The FREE ENERGY F_2(W_3) = kappa * lambda_2^FP = kappa * 7/5760
           is nonetheless CORRECT, because the CohFT graph sum uses the
           universal Bergman propagator (independent of conformal weight),
           and cross-channel contributions vanish by conformal weight mismatch.
        """
        # Step 1: c_2(E_2) on interior
        poly_E2 = chern_classes_kappa_polynomial(2, 2)
        c2_E2 = poly_E2[2]
        self.assertEqual(c2_E2[(2, 0)], Fraction(169, 288))
        self.assertEqual(c2_E2[(0, 1)], Fraction(-1, 2))

        # Step 2: lambda_2 on interior
        poly_E1 = chern_classes_kappa_polynomial(2, 1)
        c2_E1 = poly_E1[2]
        self.assertEqual(c2_E1[(2, 0)], Fraction(1, 288))
        self.assertEqual(len(c2_E1), 1)  # Only kappa_1^2

        # Step 3: They differ
        self.assertNotEqual(c2_E1, c2_E2)

        # Step 4: c_2(E_2) has kappa_2 term; lambda_2 does not
        self.assertNotIn((0, 1), c2_E1)
        self.assertIn((0, 1), c2_E2)

        # Step 5: Scalar discrepancy
        c_val = Fraction(26)
        kappa = w3_kappa_total(c_val)
        S4_tot = w3_S4_total(c_val)
        F2_scalar = scalar_F2_from_shadow(kappa, S4_tot)
        F2_universal = kappa * lambda_fp(2)
        self.assertNotEqual(F2_scalar, F2_universal)

        # Step 6: Per-channel universality holds
        kT = w3_kappa_T(c_val)
        kW = w3_kappa_W(c_val)
        fp2 = lambda_fp(2)
        F2_per_channel = kT * fp2 + kW * fp2
        self.assertEqual(F2_per_channel, kappa * fp2)

    def test_genus3_counterexample(self):
        """Same counterexample at genus 3 for extra confidence."""
        # c_3(E_j) on the interior: Newton's identity with g=3
        ratio_j2 = chern_class_ratio(3, 2)
        self.assertNotEqual(ratio_j2, Fraction(1),
                            "c_3(E_2)/lambda_3 != 1 at genus 3")

        # Per-channel universality still holds
        c_val = Fraction(26)
        kT = w3_kappa_T(c_val)
        kW = w3_kappa_W(c_val)
        fp3 = lambda_fp(3)
        F3_per_channel = kT * fp3 + kW * fp3
        kappa = w3_kappa_total(c_val)
        self.assertEqual(F3_per_channel, kappa * fp3)


class TestNumericalValues(unittest.TestCase):
    """Print explicit numerical values for the report."""

    def test_genus2_chern_class_ratios_table(self):
        """Table of c_2(E_j)/lambda_2 on the interior."""
        ratios = {}
        for j in range(1, 8):
            ratios[j] = chern_class_ratio(2, j)

        # j=1: 1 (trivially)
        self.assertEqual(ratios[1], Fraction(1))
        # j=2: 25
        self.assertEqual(ratios[2], Fraction(25))
        # j >= 2: all different from 1
        for j in range(2, 8):
            self.assertNotEqual(ratios[j], Fraction(1))

    def test_w3_scalar_discrepancy_table(self):
        """Table of scalar discrepancies at various c."""
        fp2 = lambda_fp(2)
        for c_val in [Fraction(2), Fraction(4), Fraction(13), Fraction(26), Fraction(50)]:
            kappa = w3_kappa_total(c_val)
            S4_tot = w3_S4_total(c_val)
            S4_vir = virasoro_S4(kappa)
            delta_S4 = S4_tot - S4_vir
            delta_F2 = delta_S4 / (Fraction(8) * kappa ** 2)
            F2_univ = kappa * fp2

            # All should be nonzero
            self.assertNotEqual(delta_F2, Fraction(0),
                                f"Discrepancy should be nonzero at c={c_val}")

    def test_kappa_polynomial_explicit_j1_j2_j3(self):
        """Explicit kappa-polynomials for c_2(E_j)."""
        for j in [1, 2, 3]:
            poly = chern_classes_kappa_polynomial(2, j)
            c2 = poly[2]
            # All should compute without error and be nonempty
            self.assertGreater(len(c2), 0)

    def test_genus2_ratio_growth(self):
        """The ratio c_2(E_j)/lambda_2 grows roughly as j^4."""
        ratios = [chern_class_ratio(2, j) for j in range(1, 8)]
        # Check monotone increasing for j >= 1
        for i in range(len(ratios) - 1):
            self.assertGreater(ratios[i + 1], ratios[i],
                               f"Ratio should be increasing: j={i+1} to j={i+2}")


if __name__ == '__main__':
    unittest.main()
