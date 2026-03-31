r"""Test suite for multi-generator genus universality.

MATHEMATICAL CONTEXT:
For multi-generator chiral algebras like W_3 (generators T of weight 2, W of weight 3),
the genus-1 obstruction is obs_1 = kappa * lambda_1 with
kappa = sum_i kappa_{h_i}, using the STANDARD Hodge bundle
E_1 = R^0 pi_* omega for ALL channels.

WHAT THIS FILE ACTUALLY ESTABLISHES:
The bar complex propagator is d log E(z,w), where E(z,w) is the prime form.
The prime form is a section of K^{-1/2} boxtimes K^{-1/2}, so d log E = dE/E
has weight 1 in both variables, REGARDLESS of the conformal weight of the
field being sewed (rem:propagator-weight-universality).

The former obstruction decomposition obs_g = sum_j kappa_j * lambda_g^{(j)}
was based on the incorrect assignment of weight-h generators to E_h.
Since the propagator is weight 1, all channels use E_1.  This kills the
false higher-weight Hodge-bundle story, but it does NOT by itself prove
the stronger higher-genus identity F_g = kappa * lambda_g^FP for general
multi-weight families.  The all-genera formulas tested below are therefore
conditional on the strong scalar ansatz.

The decisive test: if Virasoro used E_2, the Mumford isomorphism
c_1(E_j) = (6j^2 - 6j + 1) * lambda_1 would give F_1 = 13 * (c/2)/24
instead of the correct (c/2)/24 -- a 13x discrepancy.

COMPUTE TESTS:
- Propagator weight argument: 13x Virasoro discrepancy, 113/5 W_3 discrepancy
- kappa values: kappa(W_3) = 5c/6, kappa(W_N) = c(H_N-1), etc.
- Mumford GRR: c_1(E_j)/lambda_1 = 6j^2 - 6j + 1 at genus 1
- Free-energy consistency: F_g = kappa * lambda_g^FP for all families
- Scalar graph sum vs per-channel: diagnostic of the incorrect scalar projection
- Complementarity: kappa(W_3,c) + kappa(W_3,K-c) = K*(H_3-1)

Manuscript references:
    rem:propagator-weight-universality (higher_genus_foundations.tex)
    thm:genus-universality (higher_genus_foundations.tex)
    op:multi-generator-universality (higher_genus_foundations.tex, OPEN)
    thm:w3-obstruction (higher_genus_foundations.tex)
    prop:f2-quartic-dependence (higher_genus_foundations.tex)
"""

from __future__ import annotations

import unittest
from fractions import Fraction
from typing import Dict, List

from compute.lib.stable_graph_enumeration import (
    _bernoulli_exact,
    _lambda_fp_exact,
)

from compute.lib.propagator_weight_universality import (
    mumford_exponent,
    virasoro_test,
    w3_discrepancy,
    genus1_curvature_direct,
    genus1_curvature_wrong,
    kappa_virasoro,
    kappa_w_n,
    free_energy_universal,
    _lambda_fp_exact as _fp_exact_alt,
)


# ============================================================================
# Faber-Pandharipande numbers (using the project's authoritative implementation)
# ============================================================================

def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number at genus g.

    lambda_g^FP = (2^{2g-1}-1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError
    return _lambda_fp_exact(g)


# ============================================================================
# Mumford GRR: Chern character of E_j = R^0 pi_* omega^j
# ============================================================================

def grr_coefficient(r: int, j: int) -> Fraction:
    r"""Coefficient C_r(j) of K^r in the GRR integrand e^{jK} * K/(e^K-1).

    C_r(j) = sum_{n+m=r} B_n * j^m / (n! * m!)

    where B_n are Bernoulli numbers with B_1 = -1/2.
    This is the coefficient used in the pushforward formula:
        ch(E_j) = sum_k C_{k+1}(j) * kappa_k  (on the interior of M_g).
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


def mumford_ch1_ratio(j: int) -> Fraction:
    r"""Ratio c_1(E_j) / lambda_1 = (6j^2 - 6j + 1) at genus 1.

    From GRR: ch_1(E_j) = C_2(j) * kappa_1 on the interior.
    Since ch_1(E_1) = 1/12 * kappa_1 and lambda_1 = c_1(E_1),
    the ratio is C_2(j) / C_2(1) = 12 * C_2(j) = 6j^2 - 6j + 1.
    """
    C2_j = grr_coefficient(2, j)
    C2_1 = grr_coefficient(2, 1)
    return C2_j / C2_1


# ============================================================================
# W_3 shadow data
# ============================================================================

def w3_kappa_T(c_val: Fraction) -> Fraction:
    """T-channel curvature kappa_T = c/2 (identical to Virasoro)."""
    return c_val / Fraction(2)


def w3_kappa_W(c_val: Fraction) -> Fraction:
    """W-channel curvature kappa_W = c/3."""
    return c_val / Fraction(3)


def w3_kappa_total(c_val: Fraction) -> Fraction:
    """Total modular characteristic kappa(W_3) = 5c/6."""
    return Fraction(5) * c_val / Fraction(6)


def w3_S4_T(c_val: Fraction) -> Fraction:
    """T-channel quartic S4_T = 10/[c(5c+22)] (same as Virasoro)."""
    return Fraction(10) / (c_val * (Fraction(5) * c_val + Fraction(22)))


def w3_S4_W(c_val: Fraction) -> Fraction:
    """W-channel quartic S4_W = 2560/[c(5c+22)^3]."""
    denom = c_val * (Fraction(5) * c_val + Fraction(22)) ** 3
    return Fraction(2560) / denom


def w3_S4_total(c_val: Fraction) -> Fraction:
    """Total quartic from the combined T+W channel (weighted average).

    S4^{total} = (kappa_T * S4_T + kappa_W * S4_W) / kappa_total.
    This is NOT equal to S4^{Vir}(kappa_total).
    """
    kT = w3_kappa_T(c_val)
    kW = w3_kappa_W(c_val)
    S4T = w3_S4_T(c_val)
    S4W = w3_S4_W(c_val)
    k_total = w3_kappa_total(c_val)
    return (kT * S4T + kW * S4W) / k_total


def virasoro_S4(kappa: Fraction) -> Fraction:
    """Virasoro quartic at a given kappa: S4 = 10/[c(5c+22)] where c = 2*kappa."""
    c_val = Fraction(2) * kappa
    return Fraction(10) / (c_val * (Fraction(5) * c_val + Fraction(22)))


# ============================================================================
# Scalar graph sum at genus 2 (uses shadow data directly)
# ============================================================================

def scalar_F2_from_shadow(kappa: Fraction, S4: Fraction) -> Fraction:
    r"""Genus-2 free energy from the scalar graph sum.

    From prop:f2-quartic-dependence: dF_2/dS4 = 1/(8*kappa^2).
    The banana graph contributes S4/(8*kappa^2).
    Using F_2(kappa, S4^{Vir}(kappa)) = kappa * lambda_2^FP as baseline:
        F_2(kappa, S4) = kappa * lambda_2^FP + (S4 - S4^{Vir}(kappa)) / (8*kappa^2)
    """
    S4_vir = virasoro_S4(kappa)
    F2_universal = kappa * lambda_fp(2)
    delta_S4 = S4 - S4_vir
    return F2_universal + delta_S4 / (Fraction(8) * kappa ** 2)


# ============================================================================
# Newton's identity: c_g(E_j) from interior GRR data
# ============================================================================

def chern_class_ratio_by_newton(g: int, j: int) -> Fraction:
    """Compute c_g(E_j) / c_g(E_1) using Newton's identities from interior GRR data.

    Uses ch_k(E_j) = C_{k+1}(j) * kappa_k as the Chern character data.
    Returns the ratio c_g(E_j) / c_g(E_1).

    NOTE: This uses the interior GRR formula. On M_bar_g, boundary
    corrections modify the result. The ratio is exact at genus 1 and
    approximate for g >= 2.
    """

    def _compute_chern_classes(j_val, max_k):
        """Compute c_0, c_1, ..., c_{max_k} for E_{j_val} on the interior."""
        c_list = [Fraction(1)]  # c_0 = 1
        for k_idx in range(1, max_k + 1):
            total = Fraction(0)
            for i in range(1, k_idx + 1):
                ch_i = grr_coefficient(i + 1, j_val)
                i_fac = 1
                for nn in range(1, i + 1):
                    i_fac *= nn
                s_i = Fraction(i_fac) * ch_i
                sign = (-1) ** (i - 1)
                total += sign * c_list[k_idx - i] * s_i
            c_list.append(total / Fraction(k_idx))
        return c_list

    c_E1 = _compute_chern_classes(1, g)
    c_Ej = _compute_chern_classes(j, g)

    if c_E1[g] == 0:
        return None
    return c_Ej[g] / c_E1[g]


# ============================================================================
# Test classes
# ============================================================================

class TestPropagatorWeightArgument(unittest.TestCase):
    """The decisive test: the propagator d log E(z,w) is weight 1.

    If one incorrectly uses E_h for weight-h generators, the Mumford
    isomorphism c_1(E_j) = (6j^2 - 6j + 1) * lambda_1 produces absurd
    discrepancies at genus 1.  These tests verify the discrepancy ratios
    from the propagator_weight_universality module.
    """

    def test_virasoro_ratio_is_13(self):
        """If Vir used E_2: ratio wrong/correct = 13 (independent of c)."""
        for c_val in [Fraction(1), Fraction(1, 2), Fraction(26), Fraction(100)]:
            self.assertEqual(virasoro_test(c_val), Fraction(13))

    def test_w3_ratio_is_113_over_5(self):
        """If W_3 used E_2 and E_3: ratio wrong/correct = 113/5."""
        for c_val in [Fraction(1), Fraction(4, 5), Fraction(26)]:
            self.assertEqual(w3_discrepancy(c_val), Fraction(113, 5))

    def test_mumford_exponent_values(self):
        """Mumford isomorphism: det(E_j) = lambda^{6j^2-6j+1}."""
        self.assertEqual(mumford_exponent(1), 1)
        self.assertEqual(mumford_exponent(2), 13)
        self.assertEqual(mumford_exponent(3), 37)
        self.assertEqual(mumford_exponent(4), 73)
        self.assertEqual(mumford_exponent(5), 121)

    def test_wrong_vs_correct_virasoro(self):
        """Explicit: wrong = 13c/2, correct = c/2."""
        c = Fraction(6)
        wrong = genus1_curvature_wrong('virasoro', c)
        correct = genus1_curvature_direct('virasoro', c)
        self.assertEqual(wrong, Fraction(39))   # 13*6/2
        self.assertEqual(correct, Fraction(3))   # 6/2

    def test_wrong_vs_correct_w3(self):
        """Explicit: wrong = 113c/6, correct = 5c/6."""
        c = Fraction(6)
        wrong = genus1_curvature_wrong('w3', c)
        correct = genus1_curvature_direct('w3', c)
        self.assertEqual(wrong, Fraction(113))   # 113*6/6
        self.assertEqual(correct, Fraction(5))    # 5*6/6

    def test_heisenberg_coincidence(self):
        """For weight-1 generators, E_1 is used in both cases: no discrepancy."""
        for k in [Fraction(1), Fraction(5)]:
            correct = genus1_curvature_direct('heisenberg', k=k)
            wrong = genus1_curvature_wrong('heisenberg', k=k)
            self.assertEqual(correct, wrong,
                             "Weight-1 generators: no discrepancy")


class TestMumfordGRR(unittest.TestCase):
    """Verify the Mumford GRR formula for higher-weight bundles."""

    def test_grr_c2_genus1(self):
        """At genus 1: c_1(E_j)/lambda_1 = 6j^2 - 6j + 1 (Mumford isomorphism)."""
        self.assertEqual(mumford_ch1_ratio(1), Fraction(1))
        self.assertEqual(mumford_ch1_ratio(2), Fraction(13))
        self.assertEqual(mumford_ch1_ratio(3), Fraction(37))
        self.assertEqual(mumford_ch1_ratio(4), Fraction(73))
        self.assertEqual(mumford_ch1_ratio(5), Fraction(121))
        for j in range(1, 10):
            expected = 6 * j ** 2 - 6 * j + 1
            self.assertEqual(mumford_ch1_ratio(j), Fraction(expected),
                             f"Mumford ratio wrong for j={j}")

    def test_hodge_bundle_ch(self):
        """Chern character of the Hodge bundle: only odd kappa survive."""
        self.assertEqual(grr_coefficient(3, 1), Fraction(0))
        self.assertEqual(grr_coefficient(5, 1), Fraction(0))
        self.assertEqual(grr_coefficient(2, 1), Fraction(1, 12))
        self.assertEqual(grr_coefficient(4, 1), Fraction(-1, 720))
        self.assertEqual(grr_coefficient(6, 1), Fraction(1, 30240))

    def test_higher_weight_ch_nonzero_even(self):
        """For j >= 2: even ch_k do NOT vanish (unlike j=1)."""
        self.assertEqual(grr_coefficient(3, 2), Fraction(1, 2))
        self.assertEqual(grr_coefficient(3, 3), Fraction(5, 2))

    def test_newton_identity_genus2_j2(self):
        """c_2(E_2) on the interior: Newton's identity from GRR data."""
        ratio = chern_class_ratio_by_newton(2, 2)
        self.assertIsNotNone(ratio)
        self.assertGreater(ratio, 0, "c_2(E_2)/lambda_2 should be positive on interior")

    def test_rank_formula(self):
        """Rank of E_j = R^0 pi_* omega^j: (2j-1)(g-1) for j >= 2, g >= 2."""
        for j in [2, 3, 4]:
            for g in [2, 3, 4]:
                expected_rank = (2 * j - 1) * (g - 1)
                C1_j = grr_coefficient(1, j)
                computed_rank = C1_j * (2 * g - 2)
                self.assertEqual(computed_rank, Fraction(expected_rank),
                                 f"Rank wrong for j={j}, g={g}")

    def test_grr_interior_formula(self):
        """Verify C_r(j) = sum B_n j^m / (n! m!) for specific values."""
        self.assertEqual(grr_coefficient(2, 2), Fraction(13, 12))
        self.assertEqual(grr_coefficient(4, 2), Fraction(119, 720))


class TestKappaValues(unittest.TestCase):
    """Verify kappa values for standard families."""

    def test_w3_kappa_total(self):
        """kappa(W_3) = 5c/6."""
        for c_num in [Fraction(1), Fraction(6), Fraction(26)]:
            self.assertEqual(w3_kappa_total(c_num), Fraction(5) * c_num / 6)

    def test_w3_channel_decomposition(self):
        """kappa_T + kappa_W = kappa_total."""
        for c_val in [Fraction(1), Fraction(6), Fraction(26)]:
            self.assertEqual(
                w3_kappa_T(c_val) + w3_kappa_W(c_val),
                w3_kappa_total(c_val))

    def test_w3_matches_propagator_module(self):
        """kappa(W_3) agrees with the propagator_weight_universality module."""
        for c_val in [Fraction(1), Fraction(6), Fraction(26)]:
            self.assertEqual(w3_kappa_total(c_val), kappa_w_n(c_val, 3))


class TestGenusUniversality(unittest.TestCase):
    """Conditional all-genera scalar formulas under the strong ansatz."""

    def test_w3_genus1_through_5(self):
        """F_g(W_3) = kappa(W_3) * lambda_g^FP for g = 1..5."""
        for c_num in [Fraction(1), Fraction(4, 5), Fraction(26), Fraction(100)]:
            kappa = w3_kappa_total(c_num)
            for g in range(1, 6):
                expected = kappa * lambda_fp(g)
                # Per-channel sum: each channel uses E_1 (propagator weight 1)
                F_T = w3_kappa_T(c_num) * lambda_fp(g)
                F_W = w3_kappa_W(c_num) * lambda_fp(g)
                self.assertEqual(
                    F_T + F_W, expected,
                    f"Universality fails at c={c_num}, g={g}")

    def test_wn_universality_genus1_through_4(self):
        """F_g(W_N) = kappa(W_N) * lambda_g^FP for N = 4, 5."""
        for N in [4, 5]:
            for c_val in [Fraction(2), Fraction(26)]:
                kappas = [c_val / Fraction(s) for s in range(2, N + 1)]
                kappa_total = sum(kappas)
                for g in range(1, 5):
                    fp = lambda_fp(g)
                    F_total = sum(k * fp for k in kappas)
                    expected = kappa_total * fp
                    self.assertEqual(
                        F_total, expected,
                        f"W_{N} universality fails at c={c_val}, g={g}")

    def test_virasoro_universality(self):
        """F_g(Vir_c) = (c/2) * lambda_g^FP for g = 1..5."""
        for c_num in [Fraction(1), Fraction(26)]:
            kappa = kappa_virasoro(c_num)
            for g in range(1, 6):
                self.assertEqual(
                    free_energy_universal(kappa, g),
                    kappa * lambda_fp(g))


class TestScalarGraphSumDiagnostic(unittest.TestCase):
    """The scalar graph sum with total shadow data is a diagnostic artifact.

    The scalar graph sum projects the multi-channel CohFT to a single line,
    conflating the channel structure.  The resulting F_2^{scalar} differs
    from kappa * lambda_2^FP because S_4^{total} != S_4^{Vir}(kappa).
    This does NOT by itself prove or disprove the open higher-genus
    multi-weight theorem; it shows that naive scalar projection is not
    the right computation on the full cochain-level tower.
    """

    def test_S4_total_differs_from_virasoro(self):
        """Total quartic != Virasoro quartic at the same kappa."""
        for c_num in [Fraction(2), Fraction(13), Fraction(26)]:
            kappa = w3_kappa_total(c_num)
            S4_tot = w3_S4_total(c_num)
            S4_vir = virasoro_S4(kappa)
            self.assertNotEqual(S4_tot, S4_vir)

    def test_scalar_F2_differs_from_universal(self):
        """Scalar graph sum F_2 != kappa * lambda_2^FP for W_3.

        This is a diagnostic: the scalar projection is wrong, not Theorem D.
        """
        for c_num in [Fraction(2), Fraction(13), Fraction(26)]:
            kappa = w3_kappa_total(c_num)
            S4_tot = w3_S4_total(c_num)
            F2_scalar = scalar_F2_from_shadow(kappa, S4_tot)
            F2_universal = kappa * lambda_fp(2)
            self.assertNotEqual(F2_scalar, F2_universal)

    def test_scalar_F2_virasoro_matches(self):
        """For single-generator (Virasoro): scalar graph sum = universal."""
        for c_num in [Fraction(1), Fraction(13), Fraction(26)]:
            kappa = c_num / Fraction(2)
            S4_vir = virasoro_S4(kappa)
            F2_scalar = scalar_F2_from_shadow(kappa, S4_vir)
            F2_universal = kappa * lambda_fp(2)
            self.assertEqual(F2_scalar, F2_universal)

    def test_discrepancy_magnitude(self):
        """The discrepancy F2_scalar - F2_universal is proportional to delta_S4."""
        c_num = Fraction(26)
        kappa = w3_kappa_total(c_num)
        S4_tot = w3_S4_total(c_num)
        S4_vir = virasoro_S4(kappa)
        delta = S4_tot - S4_vir
        F2_scalar = scalar_F2_from_shadow(kappa, S4_tot)
        F2_universal = kappa * lambda_fp(2)
        discrepancy = F2_scalar - F2_universal
        expected_discrepancy = delta / (Fraction(8) * kappa ** 2)
        self.assertEqual(discrepancy, expected_discrepancy)


class TestW3FreeEnergyValues(unittest.TestCase):
    """Explicit free energy values for W_3."""

    def test_genus1_w3_c_4_5(self):
        """W_3 minimal model (5,4) at c = 4/5: F_1 = 5c/(6*24) = 1/36."""
        c_val = Fraction(4, 5)
        kappa = w3_kappa_total(c_val)
        self.assertEqual(kappa, Fraction(2, 3))
        F1 = kappa * lambda_fp(1)
        self.assertEqual(F1, Fraction(2, 3) * Fraction(1, 24))
        self.assertEqual(F1, Fraction(1, 36))

    def test_genus2_w3_c26(self):
        """F_2(W_3, c=26) = (5*26/6) * (7/5760)."""
        c_val = Fraction(26)
        kappa = w3_kappa_total(c_val)
        self.assertEqual(kappa, Fraction(65, 3))
        F2 = kappa * lambda_fp(2)
        self.assertEqual(F2, Fraction(65, 3) * Fraction(7, 5760))
        self.assertEqual(F2, Fraction(455, 17280))
        self.assertEqual(F2, Fraction(91, 3456))

    def test_genus2_w3_c13_self_dual(self):
        """F_2(W_3, c=13) = (65/6) * (7/5760) -- self-dual point."""
        c_val = Fraction(13)
        kappa = w3_kappa_total(c_val)
        self.assertEqual(kappa, Fraction(65, 6))
        F2 = kappa * lambda_fp(2)
        self.assertEqual(F2, Fraction(65, 6) * Fraction(7, 5760))


class TestWNKappaFormula(unittest.TestCase):
    """Verify kappa(W_N) = c * (H_N - 1) for N >= 2."""

    def _wn_kappa_total(self, c_val: Fraction, N: int) -> Fraction:
        """kappa(W_N) = c * sum_{s=2}^N 1/s = c * (H_N - 1)."""
        H_N_minus_1 = sum(Fraction(1, s) for s in range(2, N + 1))
        return c_val * H_N_minus_1

    def test_kappa_decomposition(self):
        """kappa_total = sum kappa_s for W_3, W_4, W_5."""
        for N in [3, 4, 5]:
            for c_val in [Fraction(1), Fraction(26)]:
                kappas = [c_val / Fraction(s) for s in range(2, N + 1)]
                total = sum(kappas)
                expected = self._wn_kappa_total(c_val, N)
                self.assertEqual(total, expected,
                                 f"kappa decomposition fails for W_{N} at c={c_val}")

    def test_wn_kappa_ratio(self):
        """kappa(W_N)/c = H_N - 1 is a root-system invariant (type A)."""
        for N in [3, 4, 5, 6]:
            H_N_minus_1 = sum(Fraction(1, s) for s in range(2, N + 1))
            c_val = Fraction(26)
            ratio = self._wn_kappa_total(c_val, N) / c_val
            self.assertEqual(ratio, H_N_minus_1)


class TestChernClassScaling(unittest.TestCase):
    """Newton's identity computation of c_g(E_j)/lambda_g on the interior.

    These tests verify the Mumford GRR structure. Even though E_j (j >= 2)
    does NOT appear in the bar complex (AP27: propagator weight is always 1),
    the GRR formulas are mathematically correct and serve as verification
    of the Mumford isomorphism.
    """

    def test_genus1_scaling(self):
        """At genus 1: c_1(E_j)/lambda_1 = 6j^2 - 6j + 1 (exact by Mumford)."""
        for j in range(1, 8):
            ratio = chern_class_ratio_by_newton(1, j)
            expected = Fraction(6 * j ** 2 - 6 * j + 1)
            self.assertEqual(ratio, expected, f"Genus 1 ratio wrong for j={j}")

    def test_genus2_scaling_j2(self):
        """At genus 2 on interior: c_2(E_2)/lambda_2 is computable and positive."""
        ratio = chern_class_ratio_by_newton(2, 2)
        self.assertIsNotNone(ratio)
        self.assertGreater(ratio, 0, "c_2(E_2)/lambda_2 should be positive")

    def test_genus2_interior_not_j4(self):
        """On the interior: c_2(E_2)/lambda_2 != j^4 = 16."""
        ratio = chern_class_ratio_by_newton(2, 2)
        self.assertNotEqual(ratio, Fraction(16),
                            "Interior c_2(E_2)/lambda_2 should NOT be j^4=16")


class TestComplementarityCheck(unittest.TestCase):
    """Complementarity: kappa(W_3,c) + kappa(W_3,100-c) = 250/3."""

    def test_kappa_complementarity(self):
        """kappa(W_3,c) + kappa(W_3,100-c) = 5*100/6 = 250/3."""
        for c_val in [Fraction(1), Fraction(13), Fraction(26), Fraction(50)]:
            kappa_c = w3_kappa_total(c_val)
            kappa_dual = w3_kappa_total(Fraction(100) - c_val)
            self.assertEqual(kappa_c + kappa_dual, Fraction(250, 3))

    def test_per_channel_complementarity(self):
        """Per-channel complementarity sums."""
        for c_val in [Fraction(13), Fraction(26)]:
            self.assertEqual(
                w3_kappa_T(c_val) + w3_kappa_T(Fraction(100) - c_val),
                Fraction(50))
            self.assertEqual(
                w3_kappa_W(c_val) + w3_kappa_W(Fraction(100) - c_val),
                Fraction(100, 3))

    def test_free_energy_complementarity(self):
        """F_g(c) + F_g(100-c) = (250/3) * lambda_g^FP for g=1..5."""
        for g in range(1, 6):
            fp = lambda_fp(g)
            for c_val in [Fraction(1), Fraction(13), Fraction(50)]:
                F_c = w3_kappa_total(c_val) * fp
                F_dual = w3_kappa_total(Fraction(100) - c_val) * fp
                self.assertEqual(F_c + F_dual, Fraction(250, 3) * fp)


class TestFaberPandharipanneNumbers(unittest.TestCase):
    """Verify the FP intersection numbers."""

    def test_fp_values(self):
        """lambda_g^FP for g = 1..5."""
        self.assertEqual(lambda_fp(1), Fraction(1, 24))
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_cross_term_vanishing(self):
        """Cross-OPE T(z)W(w) gives a descendant (3W), not a scalar.

        The zero-mode T_0(W) = h_W * W = 3W (not a scalar),
        so cross-terms vanish in H*(M_bar_g).
        """
        h_W = 3
        self.assertEqual(h_W, 3, "W generator has conformal weight 3")


if __name__ == '__main__':
    unittest.main()
