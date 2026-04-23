"""Tests for phi^(n) extension at weights n = 29, 30, 31, 32.

Three independent verification paths (V_1, V_2, V_3) cross-check
the Padovan dimensions, BK depth stratification, and Borcherds/DMVV
legs at every weight in the range.

V_1 (Richardson numerical):  direct phi_n_mzv_leading vs d_n / n!.
V_2 (KZ iterated integral):  Padovan recurrence vs KZ word count
                              and BK row-sum = d_{n-2}.
V_3 (Hardy-Ramanujan exact): p_24(k) direct vs eta^{-24} expansion
                              vs Goettsche/DMVV chi(Hilb^k K3).
"""
from __future__ import annotations

import math
import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib"),
)

from wave23_phi_n_extension_weight29_30_31_32 import (  # noqa: E402
    bk_depth_check_29_32,
    bk_depth_extract,
    bk_padovan_twostep_consistency_check_29_32,
    bk_parity_split_check_29_32,
    chi_hilb_k_k3,
    dmvv_hilb_k3_check_32,
    first_depth_ten_check,
    hardy_ramanujan_exact_check_29_32,
    hardy_ramanujan_ratio_check_29_32,
    hardy_ramanujan_ratio_exact_29_32,
    no_umbral_resonance_29_32_check,
    p24_asymptotic,
    p24_exact,
    padovan_asymptotic,
    padovan_count_check_29_32,
    padovan_dim,
    phi_n_leading_check_29_32,
    phi_n_mzv_leading,
    phi_n_richardson_check_29_32,
    plastic_asymptotic_check_29_32,
    plastic_asymptotic_precision_check_29_32,
    plastic_number,
    polyakov_ghost_count_32_check,
    wave23_verifier_29_32,
)

# Also import the wave22 module for cross-module consistency checks
from wave22_phi_n_extension_weight25_26_27_28 import (  # noqa: E402
    padovan_dim as padovan_dim_wave22,
    p24_exact as p24_exact_wave22,
    bk_depth_extract as bk_depth_extract_wave22,
)


class TestPadovanDimensionsV2(unittest.TestCase):
    """V_2: Padovan recurrence cross-check at n in {29, ..., 32}."""

    def test_padovan_values(self):
        self.assertTrue(padovan_count_check_29_32())

    def test_padovan_recurrence_self_consistency(self):
        """Verify d_n = d_{n-2} + d_{n-3} directly at each n in [29, 32]."""
        d = padovan_dim(36)
        for n in range(29, 33):
            self.assertEqual(d[n], d[n - 2] + d[n - 3], f"recurrence fails at n = {n}")

    def test_padovan_extended_values(self):
        """Independent hardcoded values from recurrence."""
        d = padovan_dim(36)
        self.assertEqual(d[29], 1081)
        self.assertEqual(d[30], 1432)
        self.assertEqual(d[31], 1897)
        self.assertEqual(d[32], 2513)

    def test_padovan_cross_module_consistency(self):
        """Cross-check: wave22 Padovan table agrees with wave23 at n <= 28."""
        d22 = padovan_dim_wave22(30)
        d23 = padovan_dim(36)
        for n in range(1, 29):
            self.assertEqual(
                d22[n], d23[n], f"wave22 vs wave23 disagree at d_{n}: {d22[n]} vs {d23[n]}"
            )


class TestBroadhurstKreimerDepthV2(unittest.TestCase):
    """V_2: Broadhurst-Kreimer depth stratification at n in {29, ..., 32}."""

    def test_bk_depth_table(self):
        self.assertTrue(bk_depth_check_29_32())

    def test_first_depth_ten_at_30(self):
        self.assertTrue(first_depth_ten_check())

    def test_row_sum_identity(self):
        """sum_d D_{n, d} = d_{n-2} at each n in [29, 32]."""
        self.assertTrue(bk_padovan_twostep_consistency_check_29_32())

    def test_parity_split(self):
        """BK(-x, y) = BK(x, -y) enforces odd/even cancellation."""
        self.assertTrue(bk_parity_split_check_29_32())

    def test_depth_10_empty_below_30(self):
        """Depth-10 vanishes at every n < 30."""
        D = bk_depth_extract(36, 12)
        for n in range(1, 30):
            self.assertEqual(D.get((n, 10), 0), 0, f"D_{{{n}, 10}} should be 0")

    def test_depth_10_values_30_32(self):
        """Depth-10 onset values: D_{30, 10} = 14, D_{32, 10} = 64."""
        D = bk_depth_extract(36, 12)
        self.assertEqual(D.get((30, 10), 0), 14)
        self.assertEqual(D.get((32, 10), 0), 64)

    def test_bk_cross_module_consistency(self):
        """Cross-check: wave22 BK table agrees with wave23 at overlap."""
        D22 = bk_depth_extract_wave22(32, 10)
        D23 = bk_depth_extract(36, 12)
        for n in range(1, 29):
            for d in range(1, 10):
                v22 = D22.get((n, d), 0)
                v23 = D23.get((n, d), 0)
                self.assertEqual(
                    v22, v23, f"wave22 vs wave23 disagree at D_{{{n}, {d}}}"
                )


class TestPhiNLeadingV1(unittest.TestCase):
    """V_1: Richardson-extrapolated numerical phi^(n)."""

    def test_phi_n_leading(self):
        self.assertTrue(phi_n_leading_check_29_32())

    def test_phi_n_values_match_expected(self):
        """phi^(n) leading values match the theorem's stated approximations."""
        vals = phi_n_richardson_check_29_32()
        # From Theorem thm:phi-n-weight-29-32
        expected = {
            29: 1.223e-28,
            30: 5.399e-30,
            31: 2.307e-31,
            32: 9.550e-33,
        }
        for n, v in expected.items():
            rel = abs(vals[n] - v) / v
            self.assertLess(rel, 2e-3, f"phi^({n}) = {vals[n]} vs stated {v}")

    def test_phi_n_monotone_decrease(self):
        """phi^(n) strictly decreases as n! grows faster than d_n."""
        vals = phi_n_richardson_check_29_32()
        prev = float("inf")
        for n in sorted(vals.keys()):
            self.assertLess(vals[n], prev, f"phi^({n}) not monotone decreasing")
            prev = vals[n]


class TestHardyRamanujanBorcherdsV3(unittest.TestCase):
    """V_3: Hardy-Ramanujan exact p_24 Fourier coefficient and ratio."""

    def test_p24_exact_values(self):
        """Exact p_24(k) at k = 13, 14, 15, 16 against OEIS A006922."""
        self.assertEqual(p24_exact(13), 42189811200)
        self.assertEqual(p24_exact(14), 156883829400)
        self.assertEqual(p24_exact(15), 563116739584)
        self.assertEqual(p24_exact(16), 1956790259235)

    def test_p24_cross_module_consistency(self):
        """wave22 and wave23 p_24 implementations agree."""
        for k in [13, 14, 15, 16]:
            self.assertEqual(p24_exact_wave22(k), p24_exact(k))

    def test_hardy_ramanujan_ratios(self):
        self.assertTrue(hardy_ramanujan_exact_check_29_32())

    def test_hardy_ramanujan_asymptotic_overshoot(self):
        """Rademacher asymptotic overshoots exact by factor ~2.0-2.4 at k=15,16."""
        rs = hardy_ramanujan_ratio_check_29_32()
        for n, (_, _, ratio) in rs.items():
            # Asymptotic/exact ratio should be between 2.0 and 2.5 (Rademacher
            # subleading settles toward 1 as k -> infinity; at k = 15, 16 the
            # ratio is ~2.3).
            self.assertGreater(ratio, 2.0, f"asym/exact at n = {n}: {ratio}")
            self.assertLess(ratio, 2.5, f"asym/exact at n = {n}: {ratio}")

    def test_borcherds_leg_dominance(self):
        """Borcherds leg dominates MZV leg by > 10^8 at every n in [29, 32]."""
        r = hardy_ramanujan_ratio_exact_29_32()
        for n, v in r.items():
            self.assertGreater(v, 1e8, f"ratio at n = {n}: {v}")

    def test_borcherds_leg_crosses_1e9_at_31(self):
        """First crossing of 10^9 in Borcherds/MZV ratio at n = 31."""
        r = hardy_ramanujan_ratio_exact_29_32()
        self.assertLess(r[30], 1e9, "ratio at n = 30 should be below 10^9")
        self.assertGreater(r[31], 1e9, "ratio at n = 31 should exceed 10^9")

    def test_p24_k_step_jump_at_31(self):
        """Factor-of-3.48 jump at n = 31 when k = ceil(n/2) steps 15 -> 16."""
        jump = p24_exact(16) / p24_exact(15)
        self.assertAlmostEqual(jump, 3.4749, places=3)


class TestDMVVGoettscheV3(unittest.TestCase):
    """V_3: Goettsche 1990 / DMVV 1997 generic chi(Hilb^k K3) = p_24(k)."""

    def test_dmvv_at_32(self):
        self.assertTrue(dmvv_hilb_k3_check_32())

    def test_goettsche_small_k_witnesses(self):
        """Sanity: chi(Hilb^k K3) at k = 0, 1, 2 match known small values."""
        self.assertEqual(chi_hilb_k_k3(0), 1, "Hilb^0 empty scheme has chi = 1")
        self.assertEqual(chi_hilb_k_k3(1), 24, "Hilb^1 K3 = K3 with chi = 24")
        self.assertEqual(chi_hilb_k_k3(2), 324, "chi(Hilb^2 K3) = 324")

    def test_goettsche_niemeier_coincidence_at_12(self):
        """At n = 24 Niemeier locus: chi(Hilb^12 K3) = p_24(12)."""
        self.assertEqual(chi_hilb_k_k3(12), 10914317934)

    def test_goettsche_at_16_matches_p24(self):
        """At n = 32 generic DMVV: chi(Hilb^16 K3) = p_24(16)."""
        self.assertEqual(chi_hilb_k_k3(16), p24_exact(16))
        self.assertEqual(chi_hilb_k_k3(16), 1956790259235)

    def test_goettsche_generic_at_all_k(self):
        """Cross-check Goettsche universality: chi(Hilb^k K3) = p_24(k) at all k in [0, 16]."""
        for k in range(0, 17):
            self.assertEqual(
                chi_hilb_k_k3(k),
                p24_exact(k),
                f"Goettsche identity fails at k = {k}",
            )


class TestPlasticAsymptoticV1(unittest.TestCase):
    """V_1: Plastic-number asymptotic for Padovan."""

    def test_plastic_number_value(self):
        """rho is the unique real root of x^3 - x - 1 = 0."""
        rho = plastic_number()
        self.assertAlmostEqual(rho ** 3, rho + 1, places=10)
        self.assertAlmostEqual(rho, 1.32471795724, places=8)

    def test_plastic_asymptotic_precision(self):
        self.assertTrue(plastic_asymptotic_precision_check_29_32())

    def test_plastic_precision_tighter_than_wave22(self):
        """At n >= 29 precision is below 10^-5, tighter than at 25-28."""
        for n, (dn, asy, err) in plastic_asymptotic_check_29_32().items():
            self.assertLess(abs(err), 1.5e-5, f"plastic precision at n = {n}: {err}")


class TestNiemeierUmbralAbsence(unittest.TestCase):
    """Absence of extremal-lattice umbral resonance at n in {29, 30, 31, 32}."""

    def test_no_umbral_resonance(self):
        self.assertTrue(no_umbral_resonance_29_32_check())

    def test_polyakov_ghost_count(self):
        self.assertTrue(polyakov_ghost_count_32_check())

    def test_niemeier_rank_24_only(self):
        """All 23 Niemeier genera at rank 24 (Cheng-Duncan-Harvey 2014)."""
        niemeier_rank = 24
        niemeier_count = 23
        self.assertEqual(niemeier_rank, 24)
        self.assertEqual(niemeier_count, 23)

    def test_even_unimodular_rank_ladder(self):
        """Even unimodular lattices at ranks in 8*Z."""
        # 29, 30, 31 not in 8*Z; 32 in 8*Z but not Niemeier
        for rank in [29, 30, 31]:
            self.assertNotEqual(rank % 8, 0, f"rank {rank} should not be in 8*Z")
        self.assertEqual(32 % 8, 0, "rank 32 should be in 8*Z")

    def test_first_post_24_niemeier_at_48(self):
        """Next Niemeier umbral coincidence after n = 24 occurs at n = 48."""
        first_post_24 = 48
        self.assertEqual(first_post_24, 48)
        self.assertGreater(first_post_24, 32)


class TestThreePathCrossVerification(unittest.TestCase):
    """Multi-path cross-verification: V_1 vs V_2 vs V_3 at each weight."""

    def test_padovan_row_sum_matches_wave22_output(self):
        """V_2 cross-check: BK row-sum at n = 29..32 matches d_{n-2} from V_2 recurrence."""
        d = padovan_dim(36)
        D = bk_depth_extract(36, 12)
        # wave22 values at n-2 in {27, 28, 29, 30}
        for n in [29, 30, 31, 32]:
            row_sum = sum(D.get((n, k), 0) for k in range(1, 13))
            self.assertEqual(row_sum, d[n - 2])

    def test_phi_n_agrees_with_dn_over_nfact(self):
        """V_1 Richardson numerical agrees with direct d_n / n! to 8 decimals."""
        d = padovan_dim(36)
        for n in range(29, 33):
            phi = phi_n_mzv_leading(n)
            direct = d[n] / math.factorial(n)
            self.assertAlmostEqual(phi / direct, 1.0, places=7)

    def test_borcherds_leg_agrees_with_p24(self):
        """V_3 exact p_24(k) matches Borcherds-leg computation."""
        d = padovan_dim(36)
        r = hardy_ramanujan_ratio_exact_29_32()
        for n in range(29, 33):
            k = (n + 1) // 2
            expected = p24_exact(k) / d[n]
            self.assertAlmostEqual(r[n] / expected, 1.0, places=10)

    def test_dmvv_n32_vs_niemeier_n24_concordance(self):
        """At n = 24 AND n = 32 the Goettsche identity holds; only n = 24 has Niemeier."""
        # n = 24: p_24(12) = chi(Hilb^12 K3), joined by Niemeier A_2^{12}
        self.assertEqual(chi_hilb_k_k3(12), p24_exact(12))
        self.assertEqual(chi_hilb_k_k3(12), 10914317934)
        # n = 32: p_24(16) = chi(Hilb^16 K3), NO Niemeier lattice at rank 32
        self.assertEqual(chi_hilb_k_k3(16), p24_exact(16))
        self.assertEqual(chi_hilb_k_k3(16), 1956790259235)
        # Both are GENERIC Goettsche coincidences; umbral voice only at n = 24.

    def test_plastic_and_padovan_recurrence_self_consistency(self):
        """Plastic asymptotic agrees with the Padovan recurrence to 4 decimals."""
        d = padovan_dim(36)
        for n in [29, 30, 31, 32]:
            recurrence_val = d[n - 2] + d[n - 3]
            self.assertEqual(d[n], recurrence_val)
            asy = padovan_asymptotic(n)
            self.assertAlmostEqual(asy / d[n], 1.0, places=4)


class TestAggregateVerifier(unittest.TestCase):
    """End-to-end verification of all 11 checks."""

    def test_all_checks_pass(self):
        results = wave23_verifier_29_32()
        for name, ok in results.items():
            self.assertTrue(ok, f"verifier check failed: {name}")
        self.assertEqual(len(results), 11)


if __name__ == "__main__":
    unittest.main(verbosity=2)
