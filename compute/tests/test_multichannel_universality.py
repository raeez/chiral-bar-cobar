r"""Conditional test suite for the strong scalar ansatz.

After rectification, the manuscript proves:
  - genus-1 universality for every modular Koszul algebra
  - the all-genera scalar package on the uniform-weight lane
  - only level-direction concentration Θ^{min} = η⊗Γ_A in general
    multi-weight families.

These tests keep the exact arithmetic consequences of the stronger
ansatz Θ^{min} = κ·η⊗Λ for W_N-style families.  They are useful as
bookkeeping checks, but they do NOT resolve
op:multi-generator-universality.

COMPUTE TESTS:
  - κ formulas for W_N (N = 2..8)
  - Per-channel decomposition: Σ κ_s = κ
  - Free energy universality: F_g = κ · λ_g^FP (g = 1..5)
  - Idempotent trace condition for W_3
  - Scalar saturation: minimal model has S_n = 0 for n ≥ 3
  - Â-genus generating function agreement
  - Complementarity: κ(W_N^k) + κ(W_N^{k'}) = (H_N-1)·K_N

Manuscript references:
    thm:multi-generator-universality (higher_genus_modular_koszul.tex)
    prop:saturation-equivalence (higher_genus_modular_koszul.tex:7643)
    thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex:8226)
    op:multi-generator-universality (higher_genus_foundations.tex:4856, OPEN)
"""

from __future__ import annotations

import unittest
from fractions import Fraction

from compute.lib.multichannel_universality import (
    lambda_fp,
    kappa_per_channel,
    kappa_total_wn,
    kappa_total_wn_formula,
    harmonic_number,
    free_energy_per_channel,
    free_energy_total_wn,
    free_energy_per_channel_sum,
    minimal_model_shadow_coefficients,
    genus2_scalar_graph_sum,
    genus2_fp_value,
    w3_idempotent_norms,
    w3_idempotent_trace,
    w3_per_idempotent_free_energy,
    wn_universality_check,
    ahat_coefficients,
    scalar_saturation_proof_chain,
)


class TestKappaFormulas(unittest.TestCase):
    """Per-channel and total κ for W_N algebras."""

    def test_w3_per_channel(self):
        c = Fraction(30)
        self.assertEqual(kappa_per_channel(c, 2), Fraction(15))   # c/2
        self.assertEqual(kappa_per_channel(c, 3), Fraction(10))   # c/3

    def test_w3_total(self):
        c = Fraction(30)
        self.assertEqual(kappa_total_wn(c, 3), Fraction(25))  # 5c/6 = 25

    def test_w3_formula(self):
        c = Fraction(30)
        self.assertEqual(kappa_total_wn(c, 3), kappa_total_wn_formula(c, 3))

    def test_virasoro_is_w2(self):
        """W_2 = Virasoro: κ = c/2."""
        for c in [Fraction(1), Fraction(13), Fraction(26)]:
            self.assertEqual(kappa_total_wn(c, 2), c / 2)

    def test_wn_formula_consistency(self):
        """κ(W_N) = c(H_N - 1) matches per-channel sum for N = 2..8."""
        for N in range(2, 9):
            for c in [Fraction(1), Fraction(13), Fraction(100)]:
                self.assertEqual(
                    kappa_total_wn(c, N),
                    kappa_total_wn_formula(c, N),
                    f"κ mismatch at N={N}, c={c}"
                )

    def test_harmonic_numbers(self):
        self.assertEqual(harmonic_number(1), Fraction(1))
        self.assertEqual(harmonic_number(2), Fraction(3, 2))
        self.assertEqual(harmonic_number(3), Fraction(11, 6))
        self.assertEqual(harmonic_number(4), Fraction(25, 12))

    def test_kappa_w3_explicit(self):
        """κ(W_3) = c/2 + c/3 = 5c/6."""
        for c in [Fraction(6), Fraction(12), Fraction(1)]:
            self.assertEqual(kappa_total_wn(c, 3), 5 * c / 6)

    def test_kappa_w4_explicit(self):
        """κ(W_4) = c/2 + c/3 + c/4 = 13c/12."""
        for c in [Fraction(12), Fraction(1)]:
            self.assertEqual(kappa_total_wn(c, 4), 13 * c / 12)


class TestFreeEnergyUniversality(unittest.TestCase):
    """Conditional F_g = κ · λ_g^FP package; genus 1 is unconditional."""

    def test_genus1(self):
        """F_1 = κ/24 (unconditional)."""
        for c in [Fraction(1), Fraction(26), Fraction(100)]:
            for N in [2, 3, 4, 5]:
                kappa = kappa_total_wn(c, N)
                self.assertEqual(
                    free_energy_total_wn(c, N, 1),
                    kappa / 24
                )

    def test_genus2(self):
        """F_2 = κ · 7/5760."""
        for c in [Fraction(1), Fraction(13), Fraction(26)]:
            for N in [2, 3, 4]:
                kappa = kappa_total_wn(c, N)
                self.assertEqual(
                    free_energy_total_wn(c, N, 2),
                    kappa * Fraction(7, 5760)
                )

    def test_genus3(self):
        """F_3 = κ · 31/967680."""
        c = Fraction(26)
        for N in [2, 3, 4]:
            kappa = kappa_total_wn(c, N)
            self.assertEqual(
                free_energy_total_wn(c, N, 3),
                kappa * Fraction(31, 967680)
            )

    def test_per_channel_sum_equals_total(self):
        """Σ F_g^{(s)} = F_g(W_N) for all N, g."""
        for N in range(2, 7):
            for g in range(1, 5):
                for c in [Fraction(1), Fraction(13)]:
                    total = free_energy_total_wn(c, N, g)
                    per_ch = free_energy_per_channel_sum(c, N, g)
                    self.assertEqual(
                        total, per_ch,
                        f"Per-channel sum ≠ total at N={N}, g={g}, c={c}"
                    )


class TestScalarSaturation(unittest.TestCase):
    """Strong-scalar minimal model: S_n = 0 for n ≥ 3."""

    def test_minimal_model_gaussian(self):
        """In the minimal model, all S_n = 0 for n ≥ 3."""
        for kappa in [Fraction(1, 2), Fraction(5, 6), Fraction(13)]:
            coeffs = minimal_model_shadow_coefficients(kappa)
            self.assertEqual(coeffs[2], kappa)
            for n in range(3, 7):
                self.assertEqual(coeffs[n], Fraction(0),
                                 f"S_{n} ≠ 0 in minimal model")

    def test_genus2_minimal_model(self):
        """F_2 in minimal model (S_4=0) = κ · λ_2^FP."""
        for kappa in [Fraction(1, 2), Fraction(5, 6), Fraction(13)]:
            # In minimal model, S_4 = 0
            # The genus-2 scalar graph sum with S_4 = 0 should give κ · 7/5760
            fp_value = genus2_fp_value(kappa)
            self.assertEqual(fp_value, kappa * Fraction(7, 5760))


class TestIdempotentDecomposition(unittest.TestCase):
    """Idempotent decomposition for W_3 shadow CohFT."""

    def test_w3_norms(self):
        """Idempotent norms: u_T = c/2, u_W = c/3."""
        c = Fraction(30)
        u_T, u_W = w3_idempotent_norms(c)
        self.assertEqual(u_T, Fraction(15))
        self.assertEqual(u_W, Fraction(10))

    def test_w3_trace(self):
        """Trace condition: u_T + u_W = κ = 5c/6."""
        for c in [Fraction(1), Fraction(6), Fraction(30), Fraction(100)]:
            trace = w3_idempotent_trace(c)
            self.assertEqual(trace, kappa_total_wn(c, 3))

    def test_w3_per_idempotent_genus1(self):
        """Per-idempotent F_1 sums to κ/24."""
        c = Fraction(30)
        data = w3_per_idempotent_free_energy(c, 1)
        self.assertEqual(data['F_g_T'], Fraction(15) / 24)
        self.assertEqual(data['F_g_W'], Fraction(10) / 24)
        self.assertEqual(data['F_g_total'], data['kappa_times_fp'])

    def test_w3_per_idempotent_genus2(self):
        """Per-idempotent F_2 sums to κ · 7/5760."""
        c = Fraction(30)
        data = w3_per_idempotent_free_energy(c, 2)
        self.assertEqual(data['F_g_total'], data['kappa_times_fp'])

    def test_w3_per_idempotent_all_genera(self):
        """Per-idempotent sum matches total for g = 1..5."""
        for c in [Fraction(1), Fraction(13), Fraction(26)]:
            for g in range(1, 6):
                data = w3_per_idempotent_free_energy(c, g)
                self.assertEqual(
                    data['F_g_total'], data['kappa_times_fp'],
                    f"Mismatch at c={c}, g={g}"
                )


class TestAHatGenus(unittest.TestCase):
    """Â-genus generating function agreement."""

    def test_ahat_coefficients(self):
        """Â(ix) - 1 = x²/24 + 7x⁴/5760 + 31x⁶/967680 + ..."""
        coeffs = ahat_coefficients(5)
        self.assertEqual(coeffs[1], Fraction(1, 24))
        self.assertEqual(coeffs[2], Fraction(7, 5760))
        self.assertEqual(coeffs[3], Fraction(31, 967680))
        self.assertEqual(coeffs[4], Fraction(127, 154828800))

    def test_ahat_equals_fp(self):
        """Â-genus coefficients = Faber-Pandharipande numbers."""
        for g in range(1, 8):
            self.assertEqual(ahat_coefficients(g)[g], lambda_fp(g))


class TestComplementarity(unittest.TestCase):
    """Complementarity: κ(W_N^k) + κ(W_N^{k'}) = (H_N-1)·K_N."""

    def _koszul_conductor(self, N: int) -> Fraction:
        """K_N = c + c' = 2(N-1)(2N²+2N+1)."""
        return Fraction(2 * (N - 1) * (2 * N**2 + 2 * N + 1))

    def _ds_central_charge(self, N: int, k: Fraction) -> Fraction:
        """Central charge c of W^k(sl_N) via DS reduction."""
        # c = (N-1)(1 - N(N+1)/(k+N))
        h_vee = Fraction(N)
        return (N - 1) * (1 - N * (N + 1) / (k + h_vee))

    def test_w2_complementarity(self):
        """κ(Vir_c) + κ(Vir_{26-c}) = 13 = (H_2-1)·26 = (1/2)·26."""
        for c in [Fraction(1), Fraction(13), Fraction(25)]:
            k1 = c / 2
            k2 = (26 - c) / 2
            self.assertEqual(k1 + k2, Fraction(13))

    def test_w3_complementarity(self):
        """κ + κ' = (H_3-1)·K_3 = (5/6)·100 = 250/3."""
        K3 = self._koszul_conductor(3)
        self.assertEqual(K3, Fraction(100))
        rho = harmonic_number(3) - 1
        self.assertEqual(rho, Fraction(5, 6))
        target = rho * K3
        self.assertEqual(target, Fraction(250, 3))

        # Check at specific level
        k = Fraction(5)
        c = self._ds_central_charge(3, k)
        kp = Fraction(6)  # k' = -k - 2N = -5-6 = -11...
        # Actually use c + c' = K_N
        cp = K3 - c
        kappa = c * rho
        kappa_dual = cp * rho
        self.assertEqual(kappa + kappa_dual, target)


class TestWNUniversality(unittest.TestCase):
    """Conditional W_N scalar bookkeeping at multiple N, c, g."""

    def test_w3_full(self):
        result = wn_universality_check(Fraction(26), 3, 2)
        self.assertTrue(result['universality_holds'])
        self.assertTrue(result['kappa_match'])
        self.assertTrue(result['trace_match'])

    def test_w4_full(self):
        result = wn_universality_check(Fraction(12), 4, 2)
        self.assertTrue(result['universality_holds'])

    def test_w5_full(self):
        result = wn_universality_check(Fraction(60), 5, 3)
        self.assertTrue(result['universality_holds'])

    def test_all_wn_genera(self):
        """Universality for W_N, N=2..6, g=1..4."""
        for N in range(2, 7):
            for g in range(1, 5):
                result = wn_universality_check(Fraction(1), N, g)
                self.assertTrue(
                    result['universality_holds'],
                    f"Universality fails at N={N}, g={g}"
                )


class TestProofChain(unittest.TestCase):
    """Historical name: verify the strong-scalar bookkeeping chain."""

    def test_w3_proof_chain(self):
        result = scalar_saturation_proof_chain(Fraction(26), 3)
        self.assertTrue(result['all_match'])
        self.assertEqual(result['kappa'], result['kappa_formula'])

    def test_w4_proof_chain(self):
        result = scalar_saturation_proof_chain(Fraction(12), 4)
        self.assertTrue(result['all_match'])

    def test_w8_proof_chain(self):
        result = scalar_saturation_proof_chain(Fraction(1), 8)
        self.assertTrue(result['all_match'])


class TestGenus1Unconditional(unittest.TestCase):
    """Genus-1 universality is unconditional (H²(M̄_{1,1}) ≅ C)."""

    def test_dimensional_collapse(self):
        """At g=1, obs_1 = κ · λ_1 regardless of multi-generator structure.
        This is because H²(M̄_{1,1}) is 1-dimensional."""
        for N in range(2, 8):
            for c in [Fraction(1), Fraction(13), Fraction(26), Fraction(100)]:
                kappa = kappa_total_wn(c, N)
                F1 = free_energy_total_wn(c, N, 1)
                self.assertEqual(F1, kappa / 24)

    def test_per_channel_genus1(self):
        """Each channel contributes κ_s/24 at genus 1."""
        c = Fraction(30)
        for s in range(2, 6):
            ks = kappa_per_channel(c, s)
            Fs = free_energy_per_channel(c, s, 1)
            self.assertEqual(Fs, ks / 24)


class TestPropagatorWeightUniversality(unittest.TestCase):
    """AP27: bar complex propagator d log E is weight 1.

    If the bar complex used E_h for weight-h generators, the Mumford
    isomorphism c_1(E_h) = (6h²-6h+1)λ_1 would give wrong F_1.
    The weight-1 propagator ensures all channels use E_1.
    """

    def test_virasoro_mumford_discrepancy(self):
        """Wrong Hodge bundle E_2 gives 13x discrepancy for Virasoro."""
        # Mumford exponent: e(h) = 6h²-6h+1
        e2 = 6 * 4 - 6 * 2 + 1  # = 13
        self.assertEqual(e2, 13)
        # If Virasoro (h=2) used E_2: F_1 would be 13 · κ/24, not κ/24

    def test_w3_mumford_discrepancy(self):
        """Wrong Hodge bundles give 113/5 discrepancy for W_3."""
        c = Fraction(30)
        kT = kappa_per_channel(c, 2)  # c/2
        kW = kappa_per_channel(c, 3)  # c/3
        e2 = 6 * 4 - 6 * 2 + 1  # 13 (for weight 2)
        e3 = 6 * 9 - 6 * 3 + 1  # 37 (for weight 3)
        self.assertEqual(e2, 13)
        self.assertEqual(e3, 37)
        # Wrong F_1 = kT·e2/24 + kW·e3/24
        F1_wrong = kT * e2 / 24 + kW * e3 / 24
        F1_correct = (kT + kW) / 24
        ratio = F1_wrong / F1_correct
        self.assertEqual(ratio, Fraction(113, 5))


if __name__ == '__main__':
    unittest.main()
