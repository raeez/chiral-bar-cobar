r"""Tests for the symmetric orbifold kappa linearity theorem.

THEOREM: kappa(Sym^N(X)) = N * kappa(X).

Four independent proofs, each verified computationally:
  Proof 1: Twist sector decomposition (untwisted = N*kappa, twisted = 0 at g=1)
  Proof 2: DMVV partition function (Borcherds product leading asymptotics)
  Proof 3: Hecke operators (T_N multiplies kappa by N)
  Proof 4: Bar complex direct (N independent copies at genus 1)

Multi-path verification mandate: every claim tested by at least 3 paths.

55+ tests organized into 12 sections.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.theorem_symn_kappa_engine import (
    SEED_FREE_BOSON,
    SEED_K3,
    SEED_LEECH,
    SEED_T4,
    SEED_VIRASORO_GENERIC,
    SeedData,
    bar_genus1_orbifold_projection,
    bar_genus1_single_copy_obs,
    bar_genus1_tensor_product_obs,
    colored_partitions,
    conjugacy_class_size,
    cross_copy_first_genus,
    cross_family_kappa_comparison,
    dmvv_connected_f1,
    dmvv_log_coefficients,
    extract_kappa_from_dmvv,
    f1_sym_n,
    f2_sym_n_scalar_lane,
    fg_sym_n_scalar_lane,
    hecke_identity_contribution,
    hecke_sublattice_count,
    kappa_first_differences,
    kappa_second_differences,
    linear_regression_kappa,
    number_of_conjugacy_classes,
    partitions_of,
    proof1_twist_sector_decomposition,
    proof2_dmvv_extraction,
    proof3_hecke_operators,
    proof4_bar_complex_direct,
    sigma_minus1,
    twist_field_conformal_weight,
    twist_sector_conformal_weight,
    untwisted_sector_kappa,
    verify_all_four_proofs,
    verify_kappa_additivity,
    verify_kappa_multiplicativity_failure,
    verify_kappa_not_c_over_2,
    verify_linearity_range,
)

F = Fraction


# =========================================================================
# Section 1: Partition combinatorics (6 tests)
# =========================================================================

class TestPartitionCombinatorics:
    """Partition enumeration and conjugacy class sizes."""

    def test_partitions_small(self):
        """Partitions of 1..5."""
        assert len(partitions_of(1)) == 1
        assert len(partitions_of(2)) == 2
        assert len(partitions_of(3)) == 3
        assert len(partitions_of(4)) == 5
        assert len(partitions_of(5)) == 7

    def test_partitions_zero(self):
        """Partition of 0 is the empty partition."""
        assert partitions_of(0) == [()]

    def test_class_equation(self):
        """Sum of conjugacy class sizes = N! for N = 1..7."""
        for N in range(1, 8):
            parts = partitions_of(N)
            total = sum(conjugacy_class_size(p, N) for p in parts)
            assert total == math.factorial(N), f"Class equation fails for S_{N}"

    def test_conjugacy_classes_count(self):
        """Number of conjugacy classes = number of partitions."""
        for N in range(1, 8):
            assert number_of_conjugacy_classes(N) == len(partitions_of(N))

    def test_identity_class_size(self):
        """The identity class has size 1."""
        for N in range(1, 7):
            identity = tuple([1] * N)
            assert conjugacy_class_size(identity, N) == 1

    def test_full_cycle_class_size(self):
        """The full N-cycle class has size (N-1)!."""
        for N in range(2, 7):
            full_cycle = (N,)
            assert conjugacy_class_size(full_cycle, N) == math.factorial(N - 1)


# =========================================================================
# Section 2: Twist field conformal weights (6 tests)
# =========================================================================

class TestTwistWeights:
    """Conformal weights of twist fields in Sym^N(X)."""

    def test_identity_weight_zero(self):
        """h_twist(identity) = 0 for any c."""
        for c in [F(1), F(6), F(24)]:
            assert twist_field_conformal_weight(c, 1) == F(0)

    def test_z2_twist_free_boson(self):
        """Z_2 twist of c=1: h = (1/24)(4-1)/2 = 1/16."""
        assert twist_field_conformal_weight(F(1), 2) == F(1, 16)

    def test_z2_twist_k3(self):
        """Z_2 twist of c=6: h = (6/24)(4-1)/2 = 3/8."""
        assert twist_field_conformal_weight(F(6), 2) == F(3, 8)

    def test_z3_twist_free_boson(self):
        """Z_3 twist of c=1: h = (1/24)(9-1)/3 = 1/9."""
        assert twist_field_conformal_weight(F(1), 3) == F(1, 9)

    def test_twist_sector_weight_additive(self):
        """h_twist((2,3)) = h_twist(Z_2) + h_twist(Z_3)."""
        c = F(6)
        h_23 = twist_sector_conformal_weight(c, (2, 3))
        h_2 = twist_field_conformal_weight(c, 2)
        h_3 = twist_field_conformal_weight(c, 3)
        assert h_23 == h_2 + h_3

    def test_all_twisted_sectors_positive_weight(self):
        """All non-identity sectors have h_twist > 0 for c > 0."""
        for N in range(2, 8):
            identity = tuple([1] * N)
            for p in partitions_of(N):
                h = twist_sector_conformal_weight(F(6), p)
                if p == identity:
                    assert h == F(0)
                else:
                    assert h > F(0), f"Non-identity {p} has h = {h} <= 0"


# =========================================================================
# Section 3: Proof 1 — Twist sector decomposition (7 tests)
# =========================================================================

class TestProof1TwistSectors:
    """Proof 1: kappa from twist sector decomposition."""

    def test_proof1_n1_k3(self):
        """N=1: kappa(K3) = 2."""
        r = proof1_twist_sector_decomposition(SEED_K3, 1)
        assert r["match"]
        assert r["kappa_computed"] == F(2)

    def test_proof1_n5_k3(self):
        """N=5: kappa(Sym^5(K3)) = 10."""
        r = proof1_twist_sector_decomposition(SEED_K3, 5)
        assert r["match"]
        assert r["kappa_computed"] == F(10)

    def test_proof1_range_free_boson(self):
        """kappa(Sym^N(boson)) = N for N=1..10."""
        for N in range(1, 11):
            r = proof1_twist_sector_decomposition(SEED_FREE_BOSON, N)
            assert r["match"], f"Proof 1 fails at N={N} for free boson"
            assert r["kappa_computed"] == F(N)

    def test_proof1_range_k3(self):
        """kappa(Sym^N(K3)) = 2N for N=1..10."""
        for N in range(1, 11):
            r = proof1_twist_sector_decomposition(SEED_K3, N)
            assert r["match"], f"Proof 1 fails at N={N} for K3"
            assert r["kappa_computed"] == F(2 * N)

    def test_proof1_twisted_zero(self):
        """Twisted sector contribution is zero at genus 1."""
        for N in range(2, 8):
            r = proof1_twist_sector_decomposition(SEED_K3, N)
            assert r["twisted_contribution"] == F(0)

    def test_proof1_class_equation(self):
        """Class equation verified for all N in proof 1."""
        for N in range(2, 8):
            r = proof1_twist_sector_decomposition(SEED_K3, N)
            assert r["class_equation_ok"]

    def test_proof1_all_twisted_positive(self):
        """All non-identity sectors have positive h in proof 1."""
        for N in range(2, 8):
            r = proof1_twist_sector_decomposition(SEED_K3, N)
            assert r["all_twisted_h_positive"]


# =========================================================================
# Section 4: Proof 2 — DMVV extraction (6 tests)
# =========================================================================

class TestProof2DMVV:
    """Proof 2: kappa from DMVV / Borcherds product."""

    def test_sigma_minus1_primes(self):
        """sigma_{-1}(p) = 1 + 1/p for primes p."""
        for p in [2, 3, 5, 7, 11]:
            assert sigma_minus1(p) == F(1) + F(1, p)

    def test_sigma_minus1_composite(self):
        """sigma_{-1}(6) = 1 + 1/2 + 1/3 + 1/6 = 2."""
        assert sigma_minus1(6) == F(2)

    def test_dmvv_connected_f1_k3(self):
        """F_1^{conn}(1, K3) = chi(K3) * sigma_{-1}(1) = 24."""
        assert dmvv_connected_f1(24, 1) == F(24)

    def test_dmvv_log_vs_sigma(self):
        """DMVV log coefficients match chi * sigma_{-1}(N) for K3."""
        chi = 24
        N_max = 10
        log_coeffs = dmvv_log_coefficients(chi, N_max)
        for N in range(1, N_max + 1):
            expected = F(chi) * sigma_minus1(N)
            assert log_coeffs[N - 1] == expected, \
                f"Log series mismatch at N={N}: {log_coeffs[N-1]} != {expected}"

    def test_proof2_n5_k3(self):
        """Proof 2 gives kappa(Sym^5(K3)) = 10."""
        r = proof2_dmvv_extraction(SEED_K3, 5)
        assert r["match"]
        assert r["kappa_computed"] == F(10)

    def test_proof2_linearity_check(self):
        """Linearity verified via first differences."""
        for N in range(2, 8):
            r = proof2_dmvv_extraction(SEED_K3, N)
            assert r["linearity_check"]


# =========================================================================
# Section 5: Proof 3 — Hecke operators (5 tests)
# =========================================================================

class TestProof3Hecke:
    """Proof 3: kappa from Hecke operators."""

    def test_hecke_sublattice_count(self):
        """sigma_1(N) for small N."""
        assert hecke_sublattice_count(1) == 1
        assert hecke_sublattice_count(2) == 3
        assert hecke_sublattice_count(3) == 4
        assert hecke_sublattice_count(4) == 7
        assert hecke_sublattice_count(6) == 12

    def test_hecke_identity_contribution_equals_n(self):
        """The identity sublattice contributes N."""
        for N in range(1, 20):
            assert hecke_identity_contribution(N) == N

    def test_proof3_n1_k3(self):
        """Proof 3 at N=1 for K3."""
        r = proof3_hecke_operators(SEED_K3, 1)
        assert r["match"]
        assert r["kappa_computed"] == F(2)

    def test_proof3_range(self):
        """Proof 3 gives kappa = N*kappa(X) for N=1..10."""
        for N in range(1, 11):
            r = proof3_hecke_operators(SEED_K3, N)
            assert r["match"], f"Proof 3 fails at N={N}"

    def test_proof3_free_boson_range(self):
        """Proof 3 for free boson: kappa(Sym^N) = N."""
        for N in range(1, 11):
            r = proof3_hecke_operators(SEED_FREE_BOSON, N)
            assert r["match"]
            assert r["kappa_computed"] == F(N)


# =========================================================================
# Section 6: Proof 4 — Bar complex direct (6 tests)
# =========================================================================

class TestProof4BarComplex:
    """Proof 4: kappa from bar complex genus-1 decomposition."""

    def test_single_copy_obs1(self):
        """obs_1(K3) = kappa(K3)/24 = 2/24 = 1/12."""
        assert bar_genus1_single_copy_obs(SEED_K3) == F(1, 12)

    def test_tensor_obs1_additive(self):
        """obs_1(X^{otimes N}) = N * obs_1(X)."""
        for N in range(1, 8):
            obs_N = bar_genus1_tensor_product_obs(SEED_K3, N)
            obs_1 = bar_genus1_single_copy_obs(SEED_K3)
            assert obs_N == N * obs_1

    def test_orbifold_preserves_obs1(self):
        """Orbifold projection preserves obs_1 at genus 1."""
        for N in range(1, 8):
            tensor_obs = bar_genus1_tensor_product_obs(SEED_K3, N)
            orbifold_obs = bar_genus1_orbifold_projection(SEED_K3, N)
            assert tensor_obs == orbifold_obs

    def test_cross_copy_first_at_genus2(self):
        """Cross-copy contributions first appear at genus 2."""
        assert cross_copy_first_genus(SEED_K3) == 2
        assert cross_copy_first_genus(SEED_FREE_BOSON) == 2

    def test_proof4_range_k3(self):
        """Proof 4 gives kappa(Sym^N(K3)) = 2N for N=1..10."""
        for N in range(1, 11):
            r = proof4_bar_complex_direct(SEED_K3, N)
            assert r["match"], f"Proof 4 fails at N={N}"
            assert r["kappa_computed"] == F(2 * N)

    def test_proof4_leech(self):
        """Proof 4 for Leech: kappa(Sym^N) = 24N.  AP48: NOT 12N."""
        for N in range(1, 6):
            r = proof4_bar_complex_direct(SEED_LEECH, N)
            assert r["match"]
            assert r["kappa_computed"] == F(24 * N)
            assert r["kappa_computed"] != F(12 * N)  # AP48


# =========================================================================
# Section 7: Four-proof convergence (6 tests)
# =========================================================================

class TestFourProofConvergence:
    """Central test: all four proofs must agree."""

    def test_all_four_agree_k3_n5(self):
        """All four proofs agree for Sym^5(K3): kappa = 10."""
        r = verify_all_four_proofs(SEED_K3, 5)
        assert r["all_match_expected"]
        assert r["pairwise_agree"]
        assert r["kappa_expected"] == F(10)

    def test_all_four_agree_free_boson_n7(self):
        """All four proofs agree for Sym^7(free boson): kappa = 7."""
        r = verify_all_four_proofs(SEED_FREE_BOSON, 7)
        assert r["all_match_expected"]
        assert r["pairwise_agree"]

    def test_all_four_agree_t4_n3(self):
        """All four proofs agree for Sym^3(T^4): kappa = 6."""
        r = verify_all_four_proofs(SEED_T4, 3)
        assert r["all_match_expected"]
        assert r["kappa_expected"] == F(6)

    def test_all_four_agree_leech_n2(self):
        """All four proofs agree for Sym^2(Leech): kappa = 48."""
        r = verify_all_four_proofs(SEED_LEECH, 2)
        assert r["all_match_expected"]
        assert r["kappa_expected"] == F(48)

    def test_linearity_range_k3(self):
        """Full range N=1..8 all four proofs agree for K3."""
        r = verify_linearity_range(SEED_K3, list(range(1, 9)))
        assert r["all_ok"]

    def test_linearity_range_free_boson(self):
        """Full range N=1..8 all four proofs agree for free boson."""
        r = verify_linearity_range(SEED_FREE_BOSON, list(range(1, 9)))
        assert r["all_ok"]


# =========================================================================
# Section 8: Additivity and structure (5 tests)
# =========================================================================

class TestAdditivityStructure:
    """Structural properties: additivity, non-multiplicativity, differences."""

    def test_additivity_k3(self):
        """kappa(Sym^{3+4}) = kappa(Sym^3) + kappa(Sym^4) for K3."""
        r = verify_kappa_additivity(SEED_K3, 3, 4)
        assert r["match"]
        assert r["kappa_sum"] == F(14)
        assert r["kappa_N1_plus_N2"] == F(14)

    def test_additivity_range(self):
        """Additivity for all (N1, N2) with N1+N2 <= 10."""
        for N1 in range(1, 6):
            for N2 in range(1, 6):
                r = verify_kappa_additivity(SEED_K3, N1, N2)
                assert r["match"], f"Additivity fails for N1={N1}, N2={N2}"

    def test_multiplicativity_fails_for_kappa_neq_1(self):
        """kappa is additive, not multiplicative (unless kappa(X)=1)."""
        r = verify_kappa_multiplicativity_failure(SEED_K3, 2, 3)
        # kappa(K3) = 2 != 1, so not multiplicative
        assert not r["is_multiplicative"]

    def test_multiplicativity_accidental_for_kappa_1(self):
        """For free boson (kappa=1), multiplicativity is accidental."""
        r = verify_kappa_multiplicativity_failure(SEED_FREE_BOSON, 2, 3)
        # kappa(boson) = 1, so N*M*1 = N*M*1^2 (accidental match)
        assert r["is_multiplicative"]
        assert r["reason"] != ""

    def test_first_differences_constant(self):
        """First differences of kappa(Sym^N) all equal kappa(X)."""
        diffs = kappa_first_differences(SEED_K3, 10)
        for d in diffs:
            assert d == SEED_K3.kappa


# =========================================================================
# Section 9: N-dependence structural verification (5 tests)
# =========================================================================

class TestNDependenceStructure:
    """Structural tests on the N-dependence of kappa."""

    def test_second_differences_zero(self):
        """Second differences of kappa(Sym^N) are all zero (exact linearity)."""
        diffs2 = kappa_second_differences(SEED_K3, 10)
        for d in diffs2:
            assert d == F(0), f"Non-zero second difference: {d}"

    def test_linear_regression_k3(self):
        """Linear regression: slope = kappa(K3) = 2, intercept = 0."""
        r = linear_regression_kappa(SEED_K3, 10)
        assert r["exact_linearity"]
        assert r["slope"] == F(2)
        assert r["intercept"] == F(0)

    def test_linear_regression_free_boson(self):
        """Linear regression: slope = 1, intercept = 0."""
        r = linear_regression_kappa(SEED_FREE_BOSON, 10)
        assert r["exact_linearity"]
        assert r["slope"] == F(1)

    def test_linear_regression_leech(self):
        """Linear regression: slope = 24, intercept = 0."""
        r = linear_regression_kappa(SEED_LEECH, 10)
        assert r["exact_linearity"]
        assert r["slope"] == F(24)

    def test_kappa_at_n0(self):
        """kappa(Sym^0(X)) = 0 for all seeds."""
        for seed in [SEED_K3, SEED_FREE_BOSON, SEED_T4, SEED_LEECH]:
            r = proof1_twist_sector_decomposition(seed, 0)
            assert r["kappa_computed"] == F(0)


# =========================================================================
# Section 10: Free energy F_g scaling (5 tests)
# =========================================================================

class TestFreeEnergyScaling:
    """F_g(Sym^N(X)) = N * kappa(X) * lambda_g^FP on the scalar lane."""

    def test_f1_k3_n1(self):
        """F_1(K3) = kappa(K3)/24 = 2/24 = 1/12."""
        assert f1_sym_n(SEED_K3, 1) == F(1, 12)

    def test_f1_k3_n5(self):
        """F_1(Sym^5(K3)) = 5*2/24 = 10/24 = 5/12."""
        assert f1_sym_n(SEED_K3, 5) == F(5, 12)

    def test_f1_scales_linearly(self):
        """F_1(Sym^N) = N * F_1(X)."""
        f1_single = f1_sym_n(SEED_K3, 1)
        for N in range(2, 11):
            assert f1_sym_n(SEED_K3, N) == N * f1_single

    def test_f2_k3_n1(self):
        """F_2(K3) = 2 * 7/5760 = 7/2880."""
        assert f2_sym_n_scalar_lane(SEED_K3, 1) == F(7, 2880)

    def test_f2_scales_linearly(self):
        """F_2(Sym^N) = N * F_2(X) on scalar lane."""
        f2_single = f2_sym_n_scalar_lane(SEED_K3, 1)
        for N in range(2, 8):
            assert f2_sym_n_scalar_lane(SEED_K3, N) == N * f2_single


# =========================================================================
# Section 11: AP48 cross-checks (5 tests)
# =========================================================================

class TestAP48CrossChecks:
    """AP48: kappa != c/2 for non-Virasoro algebras."""

    def test_k3_kappa_not_c_over_2(self):
        """kappa(Sym^N(K3)) = 2N != 3N = c(Sym^N(K3))/2."""
        for N in range(1, 6):
            assert verify_kappa_not_c_over_2(SEED_K3, N)

    def test_t4_kappa_not_c_over_2(self):
        """kappa(Sym^N(T^4)) = 2N != 3N = c(Sym^N(T^4))/2."""
        for N in range(1, 6):
            assert verify_kappa_not_c_over_2(SEED_T4, N)

    def test_leech_kappa_not_c_over_2(self):
        """kappa(Sym^N(Leech)) = 24N != 12N = c(Sym^N(Leech))/2.  AP48."""
        for N in range(1, 4):
            assert verify_kappa_not_c_over_2(SEED_LEECH, N)

    def test_cross_family_comparison(self):
        """Cross-family kappa comparison at N=5."""
        r = cross_family_kappa_comparison(5)
        # K3 and T^4: kappa != c/2
        assert r["K3"]["kappa_not_c_over_2"]
        assert r["T4"]["kappa_not_c_over_2"]
        # Leech: kappa != c/2
        assert r["Leech"]["kappa_not_c_over_2"]
        # K3 kappa = 10, not 15
        assert r["K3"]["kappa"] == F(10)
        assert r["K3"]["c_over_2"] == F(15)

    def test_free_boson_kappa_equals_c(self):
        """For free boson: kappa = k = c.  (Not c/2 unless c=2!)"""
        # kappa(H_1) = 1, c = 1, so kappa = c (not c/2)
        for N in range(1, 6):
            kappa = N * SEED_FREE_BOSON.kappa
            c_sym = N * SEED_FREE_BOSON.central_charge
            assert kappa == c_sym  # kappa = c for Heisenberg at level 1


# =========================================================================
# Section 12: Colored partitions and DMVV consistency (4 tests)
# =========================================================================

class TestColoredPartitionsDMVV:
    """Colored partition counts and DMVV consistency."""

    def test_colored_partitions_1_color(self):
        """1-colored partitions = ordinary partitions: p(1)=1, p(2)=2, p(3)=3, p(4)=5."""
        expected = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for n, p_n in expected.items():
            assert colored_partitions(n, 1) == p_n

    def test_colored_partitions_k3(self):
        """24-colored partitions: chi(Hilb^N(K3))."""
        # chi(Hilb^0) = 1, chi(Hilb^1) = 24, chi(Hilb^2) = 324
        assert colored_partitions(0, 24) == 1
        assert colored_partitions(1, 24) == 24
        assert colored_partitions(2, 24) == 324

    def test_colored_partitions_k3_n3(self):
        """chi(Hilb^3(K3)) = 3200."""
        assert colored_partitions(3, 24) == 3200

    def test_dmvv_log_consistency_independent(self):
        """Two independent computations of log Z agree for K3.

        Path 1: chi * sigma_{-1}(N) (analytic formula).
        Path 2: Power-series log of Gottsche generating function (numerical).
        """
        chi = 24
        N_max = 8
        log_coeffs = dmvv_log_coefficients(chi, N_max)
        for N in range(1, N_max + 1):
            analytic = F(chi) * sigma_minus1(N)
            numerical = log_coeffs[N - 1]
            assert analytic == numerical, \
                f"DMVV log inconsistency at N={N}: {analytic} vs {numerical}"
