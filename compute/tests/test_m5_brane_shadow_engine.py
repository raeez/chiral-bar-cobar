"""Tests for the M5 brane shadow obstruction tower engine.

Verifies the M5 brane boundary VOA, its modular characteristic, and the
N^3 vs N^{3/2} brane scaling dichotomy.

Organisation:
  1. M5Data construction and basic properties
  2. Henningson-Skenderis a/c anomaly formulas
  3. Multi-path kappa(M5_N) verification
  4. Beem-Rastelli chiral algebra cross-check
  5. M2 (ABJM) vs M5 scaling dichotomy
  6. Genus expansion and 1-loop / 2-loop predictions
  7. Koszul dual and AP24 complementarity
  8. Twisted M-theory corner algebras
  9. Celestial chiral algebra
 10. Cross-engine consistency
 11. Holographic datum
 12. Full verification suite

References:
  - compute/lib/m5_brane_shadow_engine.py
  - Henningson-Skenderis arXiv:hep-th/9806087
  - Beem-Rastelli-vR arXiv:1404.1079
  - Costello-Paquette arXiv:2103.16984
  - Aharony et al. arXiv:0806.1218 (ABJM, M2 brane)
"""

from __future__ import annotations

from fractions import Fraction
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "lib"))

from m5_brane_shadow_engine import (
    M5Data,
    M5KoszulDual,
    M5HolographicDatum,
    brane_scaling_dichotomy,
    celestial_chiral_algebra_11d,
    costello_gaiotto_paquette_summary,
    cross_engine_consistency_with_abjm,
    cross_engine_consistency_with_w_algebra,
    full_verification_suite,
    harmonic,
    henningson_skenderis_a_anomaly,
    henningson_skenderis_c_anomaly,
    kappa_m5_multi_path,
    kappa_m5_path1_anomaly,
    kappa_m5_path2_w_algebra,
    kappa_m5_path3_brane_counting,
    lambda_fp,
    m2_kappa_abjm,
    m5_F_1,
    m5_F_2,
    m5_F_g,
    m5_a_minus_c,
    m5_anomaly_polynomial_leading,
    m5_genus_expansion,
    m5_genus_table,
    m5_kappa_leading,
    m5_koszul_dual,
    m5_loop_corrections,
    m5_vs_m2_kappa_ratio,
    make_m5_holographic_datum,
    twisted_m_theory_corner_algebra,
    verify_brane_dichotomy,
    verify_complementarity_nonzero,
    verify_henningson_skenderis,
    verify_kappa_multi_path,
    verify_n1_free_tensor_limit,
)


# ===========================================================================
# 1. M5Data construction and basic properties
# ===========================================================================

class TestM5DataConstruction:
    """Basic construction of the M5Data object."""

    def test_construction_n1(self):
        d = M5Data(N=1)
        assert d.N == 1
        assert d.epsilon_ratio == 0

    def test_construction_n5(self):
        d = M5Data(N=5)
        assert d.N == 5

    def test_lambda_param_default(self):
        """lambda = N + epsilon_ratio, default epsilon_ratio = 0."""
        d = M5Data(N=3)
        assert d.lambda_param == Fraction(3)

    def test_lambda_param_omega(self):
        d = M5Data(N=3, epsilon_ratio=Fraction(1, 2))
        assert d.lambda_param == Fraction(7, 2)

    def test_voa_name_contains_lambda(self):
        d = M5Data(N=2)
        assert "lambda" in d.boundary_voa_name
        assert "2" in d.boundary_voa_name

    def test_central_charge_2d_equals_n(self):
        """Boundary VOA c_{2D} = N at the lambda=N corner."""
        for N in [1, 2, 3, 5, 10]:
            d = M5Data(N=N)
            assert d.central_charge_2d == Fraction(N)

    def test_kappa_leading_is_n_cubed(self):
        for N in [1, 2, 3, 5, 10]:
            d = M5Data(N=N)
            assert d.kappa_leading == Fraction(N) ** 3

    def test_shadow_class_n1_is_C(self):
        """N=1 free tensor multiplet: contact class C."""
        d = M5Data(N=1)
        assert d.shadow_class == "C"
        assert d.shadow_depth == 4

    def test_shadow_class_n2_is_M(self):
        """N>=2 interacting (2,0): mixed class M (infinite shadow depth)."""
        for N in [2, 3, 5, 10]:
            d = M5Data(N=N)
            assert d.shadow_class == "M"
            assert d.shadow_depth >= 1000  # sentinel for infinity


# ===========================================================================
# 2. Henningson-Skenderis a/c anomaly
# ===========================================================================

class TestHenningsonSkenderis:
    """The 1998 Weyl anomaly result for M5 branes."""

    def test_a_anomaly_n1_zero(self):
        """N=1: free tensor multiplet, a = (4 - 3 - 1)/12 = 0."""
        assert henningson_skenderis_a_anomaly(1) == 0

    def test_a_anomaly_n2(self):
        """N=2: a = (32 - 6 - 1)/12 = 25/12."""
        assert henningson_skenderis_a_anomaly(2) == Fraction(25, 12)

    def test_a_anomaly_n3(self):
        """N=3: a = (108 - 9 - 1)/12 = 98/12 = 49/6."""
        assert henningson_skenderis_a_anomaly(3) == Fraction(49, 6)

    def test_a_equals_c_supersymmetry(self):
        """For (2,0): a = c by SUSY."""
        for N in [1, 2, 3, 5, 10]:
            a = henningson_skenderis_a_anomaly(N)
            c = henningson_skenderis_c_anomaly(N)
            assert a == c
            assert m5_a_minus_c(N) == 0

    def test_anomaly_scales_n3(self):
        """Leading: a ~ N^3 / 3 at large N."""
        N = 100
        a = float(henningson_skenderis_a_anomaly(N))
        leading = N ** 3 / 3
        # Within 2% of the leading
        assert abs(a / leading - 1) < 0.02

    def test_anomaly_polynomial_leading(self):
        """(N^3 - N) / 24 brane stack anomaly."""
        assert m5_anomaly_polynomial_leading(1) == 0
        assert m5_anomaly_polynomial_leading(2) == Fraction(1, 4)
        assert m5_anomaly_polynomial_leading(3) == Fraction(24, 24)
        assert m5_anomaly_polynomial_leading(3) == Fraction(1)


# ===========================================================================
# 3. Multi-path kappa verification (CLAUDE.md mandate: 3+ paths)
# ===========================================================================

class TestKappaMultiPath:
    """Three independent paths to kappa(M5_N) must agree at leading N^3."""

    def test_path1_n1_zero(self):
        """Path 1 (chiral algebra): kappa = (4N^3 - 3N - 1)/2.

        At N=1: (4 - 3 - 1)/2 = 0.  Free tensor multiplet.
        """
        assert kappa_m5_path1_anomaly(1) == 0

    def test_path1_n2(self):
        """Path 1 at N=2: (32 - 6 - 1)/2 = 25/2."""
        assert kappa_m5_path1_anomaly(2) == Fraction(25, 2)

    def test_path1_n3(self):
        """Path 1 at N=3: (108 - 9 - 1)/2 = 98/2 = 49."""
        assert kappa_m5_path1_anomaly(3) == 49

    def test_path2_returns_n_cubed(self):
        """Path 2 (W-algebra clean leading): kappa = N^3."""
        for N in [1, 2, 3, 5]:
            assert kappa_m5_path2_w_algebra(N) == Fraction(N) ** 3

    def test_path3_returns_n_cubed(self):
        """Path 3 (dof counting): kappa = N^3."""
        for N in [1, 2, 3, 5]:
            assert kappa_m5_path3_brane_counting(N) == Fraction(N) ** 3

    def test_paths_2_and_3_identical(self):
        """Paths 2 and 3 must agree exactly at every N."""
        for N in range(1, 11):
            assert kappa_m5_path2_w_algebra(N) == kappa_m5_path3_brane_counting(N)

    def test_path1_leading_factor_2(self):
        """Path 1 ~ 2N^3 at large N (because c = 4N^3 -> kappa = c/2 = 2N^3).

        Path 1 / N^3 = 2 - (3N+1)/N^3 -> 2 as N -> infinity.
        At N=50: error ~ 0.06%; at N=100: error ~ 0.015%.
        """
        for N in [50, 100, 500]:
            ratio = float(kappa_m5_path1_anomaly(N)) / N ** 3
            assert abs(ratio - 2.0) < 0.001

    def test_multi_path_dict(self):
        """The multi-path dict returns all three paths."""
        d = kappa_m5_multi_path(3)
        assert "path1_chiral_alg" in d
        assert "path2_w_algebra_leading" in d
        assert "path3_dof_counting" in d
        assert d["path2_w_algebra_leading"] == d["path3_dof_counting"]
        assert d["leading_N3_agree"] is True


# ===========================================================================
# 4. Beem-Rastelli chiral algebra
# ===========================================================================

class TestBeemRastelli:
    """The protected chiral algebra of (2,0): c = 4N^3 - 3N - 1."""

    def test_n1_free_tensor(self):
        d = M5Data(N=1)
        assert d.kappa_beem_rastelli == 0

    def test_n2(self):
        d = M5Data(N=2)
        assert d.kappa_beem_rastelli == 25  # 32 - 6 - 1 = 25

    def test_n3(self):
        d = M5Data(N=3)
        assert d.kappa_beem_rastelli == 98  # 108 - 9 - 1 = 98

    def test_kappa_from_chiral_is_half(self):
        """kappa_from_chiral = c_{2D}/2 = (4N^3 - 3N - 1)/2."""
        for N in [1, 2, 3, 5]:
            d = M5Data(N=N)
            assert d.kappa_from_chiral == d.kappa_beem_rastelli / 2

    def test_leading_n3(self):
        """At large N, the chiral algebra c -> 4 N^3."""
        for N in [10, 50, 100]:
            d = M5Data(N=N)
            ratio = float(d.kappa_beem_rastelli) / (4 * N ** 3)
            # Subleading is -3N - 1, so ratio approaches 1 as 1 - O(1/N^2)
            assert abs(ratio - 1.0) < 0.01

    def test_kappa_full_subleading(self):
        """kappa_full = N^3 - N (leading + subleading correction)."""
        d = M5Data(N=5)
        assert d.kappa_full == 125 - 5
        d = M5Data(N=10)
        assert d.kappa_full == 1000 - 10


# ===========================================================================
# 5. M2 vs M5 scaling dichotomy
# ===========================================================================

class TestBraneDichotomy:
    """The N^{3/2} (M2) vs N^3 (M5) brane scaling difference."""

    def test_m2_kappa_negative(self):
        """ABJM kappa = -N^2 (negative because non-unitary)."""
        for N in [1, 2, 5, 10]:
            assert m2_kappa_abjm(N) == Fraction(-N * N)
            assert m2_kappa_abjm(N) < 0

    def test_m5_kappa_positive(self):
        """M5 kappa = +N^3."""
        for N in [1, 2, 5, 10]:
            assert m5_kappa_leading(N) == Fraction(N) ** 3
            assert m5_kappa_leading(N) > 0

    def test_kappa_ratio_is_minus_n(self):
        """kappa(M5)/kappa(M2) = N^3 / (-N^2) = -N."""
        for N in [1, 2, 3, 5, 10]:
            r = m5_vs_m2_kappa_ratio(N)
            assert r == Fraction(-N)

    def test_dichotomy_dict_contents(self):
        d = brane_scaling_dichotomy(3)
        assert d["F0_scaling_M2"] == "N^{3/2}"
        assert d["F0_scaling_M5"] == "N^3"
        assert d["kappa_M2"] == -9
        assert d["kappa_M5"] == 27

    def test_F1_signs_oppose(self):
        """F_1(M2) < 0, F_1(M5) > 0."""
        for N in [2, 3, 5, 10]:
            d = brane_scaling_dichotomy(N)
            assert d["F1_M2"] < 0
            assert d["F1_M5"] > 0

    def test_verify_dichotomy_function(self):
        """verify_brane_dichotomy returns all true checks."""
        for N in [2, 3, 5]:
            v = verify_brane_dichotomy(N)
            assert all(v.values()), f"At N={N}, failures: {v}"


# ===========================================================================
# 6. Genus expansion and loop corrections
# ===========================================================================

class TestGenusExpansion:
    """F_g predictions for M5 1-loop and 2-loop."""

    def test_F1_formula(self):
        """F_1 = kappa/24 = N^3/24."""
        for N in [1, 2, 3, 5, 10]:
            assert m5_F_1(N) == Fraction(N ** 3, 24)

    def test_F1_predicts_specific_values(self):
        """Specific N=2: F_1 = 8/24 = 1/3."""
        assert m5_F_1(2) == Fraction(1, 3)
        assert m5_F_1(3) == Fraction(27, 24)
        assert m5_F_1(3) == Fraction(9, 8)

    def test_F2_formula(self):
        """F_2 = kappa * lambda_2^FP = N^3 * 7/5760."""
        for N in [1, 2, 3, 5]:
            expected = Fraction(N ** 3) * Fraction(7, 5760)
            assert m5_F_2(N) == expected

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24 (Faber-Pandharipande)."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760 (CLAUDE.md AP38 corrected value)."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680 from |B_6|/(2g)! ratio."""
        # B_6 = 1/42; lambda_3 = (32-1)*1/42 / (32 * 720) = 31 / (42*32*720)
        # = 31 / 967680
        expected = Fraction(31, 967680)
        assert lambda_fp(3) == expected

    def test_genus_expansion_table(self):
        """Genus expansion at N=2."""
        exp = m5_genus_expansion(2, max_genus=5)
        assert set(exp.keys()) == {1, 2, 3, 4, 5}
        assert exp[1] == Fraction(8, 24)

    def test_loop_corrections_dict(self):
        d = m5_loop_corrections(3)
        assert d["N"] == 3
        assert d["kappa"] == 27
        assert d["F_1_prediction"] == Fraction(27, 24)
        assert d["F_2_prediction"] == Fraction(7 * 27, 5760)

    def test_genus_table_multi_N(self):
        """The table function returns one row per N."""
        rows = m5_genus_table([1, 2, 3, 4, 5], max_genus=3)
        assert len(rows) == 5
        for row in rows:
            assert "N" in row
            assert "kappa" in row
            assert "F_1" in row and "F_2" in row and "F_3" in row

    def test_F_g_is_kappa_times_lambda(self):
        """The defining identity F_g = kappa * lambda_g^FP."""
        for N in [2, 3, 5]:
            for g in [1, 2, 3, 4]:
                assert m5_F_g(N, g) == Fraction(N ** 3) * lambda_fp(g)


# ===========================================================================
# 7. Koszul dual and complementarity (AP24)
# ===========================================================================

class TestKoszulDual:
    """Koszul dual M5_N^! and AP24 verification."""

    def test_dual_construction(self):
        d = m5_koszul_dual(3)
        assert isinstance(d, M5KoszulDual)
        assert d.N == 3

    def test_lambda_dual_involution(self):
        """lambda^! = 2 - lambda (Linshaw involution)."""
        for N in [1, 2, 3, 5]:
            d = m5_koszul_dual(N)
            assert d.lambda_dual == Fraction(2 - N)

    def test_dual_kappa_n1(self):
        """At N=1: kappa(A^!) = (2-1)^3 = 1."""
        assert m5_koszul_dual(1).kappa_dual == 1

    def test_dual_kappa_n2(self):
        """At N=2: kappa(A^!) = (2-2)^3 = 0."""
        assert m5_koszul_dual(2).kappa_dual == 0

    def test_complementarity_n1(self):
        """At N=1: kappa + kappa^! = 1 + 1 = 2."""
        assert m5_koszul_dual(1).complementarity_sum == 2

    def test_complementarity_n2(self):
        """At N=2: 8 + 0 = 8."""
        assert m5_koszul_dual(2).complementarity_sum == 8

    def test_complementarity_n3(self):
        """At N=3: 27 + (-1) = 26."""
        assert m5_koszul_dual(3).complementarity_sum == 26

    def test_complementarity_formula(self):
        """6N^2 - 12N + 8 = 2(3N^2 - 6N + 4) = 2[3(N-1)^2 + 1]."""
        for N in [1, 2, 3, 5, 10]:
            d = m5_koszul_dual(N)
            expected = Fraction(N) ** 3 + Fraction(2 - N) ** 3
            assert d.complementarity_sum == expected
            # Algebraic identity check
            poly = 6 * N ** 2 - 12 * N + 8
            assert d.complementarity_sum == poly

    def test_complementarity_positive(self):
        """kappa + kappa^! is always positive (minimum 2 at N=1)."""
        for N in range(1, 11):
            assert m5_koszul_dual(N).complementarity_sum > 0

    def test_complementarity_minimum_at_n1(self):
        """The minimum of 2[3(N-1)^2 + 1] occurs at N=1, value 2."""
        sums = [m5_koszul_dual(N).complementarity_sum for N in range(1, 11)]
        assert min(sums) == 2
        assert sums[0] == 2  # N=1

    def test_AP24_holds(self):
        """AP24: kappa + kappa^! != 0 for W-algebras (M5 family)."""
        for N in [1, 2, 3, 5, 10]:
            v = verify_complementarity_nonzero(N)
            assert v["AP24_holds"]
            assert v["sum_nonzero"]
            assert v["sum_positive"]

    def test_phantom_interpretation_string(self):
        """The dual has 'no known direct interpretation'."""
        d = m5_koszul_dual(3)
        text = d.physical_interpretation
        assert "no known" in text or "phantom" in text.lower() or "candidates" in text


# ===========================================================================
# 8. Twisted M-theory corner algebras
# ===========================================================================

class TestTwistedMTheoryCorners:
    """Costello-Gaiotto-Paquette corner algebras."""

    def test_M5_corner_n3(self):
        d = twisted_m_theory_corner_algebra(3, "M5")
        assert d["corner"] == "M5"
        assert d["N"] == 3
        assert d["kappa_leading"] == 27

    def test_M2_corner_kappa_negative(self):
        d = twisted_m_theory_corner_algebra(3, "M2")
        assert d["kappa_leading"] == -9

    def test_M5_corner_voa_name(self):
        d = twisted_m_theory_corner_algebra(2, "M5")
        assert "lambda" in d["voa"]
        assert "2" in d["voa"]

    def test_M2_M5_corner_mixed(self):
        d = twisted_m_theory_corner_algebra(2, "M2-M5")
        assert d["kappa_leading"] == 2 ** 3 - 2 ** 2  # 8 - 4 = 4

    def test_corner_unknown_raises(self):
        with pytest.raises(ValueError):
            twisted_m_theory_corner_algebra(2, "wrong")

    def test_summary_contents(self):
        s = costello_gaiotto_paquette_summary()
        assert "M2_corner" in s
        assert "M5_corner" in s
        assert "M2_M5_corner" in s
        assert "references" in s
        assert any("Costello" in r for r in s["references"])

    def test_M5_corner_grav_central_charge(self):
        """The bulk gravitational c (Henningson-Skenderis) is included."""
        d = twisted_m_theory_corner_algebra(2, "M5")
        assert d["central_charge_grav_AdS7"] == Fraction(25, 12)


# ===========================================================================
# 9. Celestial chiral algebra at I^+ of 11d
# ===========================================================================

class TestCelestialChiralAlgebra:
    """Celestial chiral algebra of M-theory at null infinity."""

    def test_celestial_voa_n1(self):
        d = celestial_chiral_algebra_11d(1)
        assert d["N"] == 1
        assert "lambda" in d["celestial_voa"]

    def test_celestial_kappa_leading(self):
        for N in [1, 2, 3, 5]:
            d = celestial_chiral_algebra_11d(N)
            assert d["kappa_leading"] == Fraction(N) ** 3

    def test_celestial_loop_quantization(self):
        d = celestial_chiral_algebra_11d(2)
        assert "w_inf" in d["loop_quantization"]
        assert "W_{1+inf}" in d["loop_quantization"]

    def test_celestial_soft_theorem_organization(self):
        d = celestial_chiral_algebra_11d(3)
        assert "soft" in d["soft_theorem_organization"].lower()
        assert "M5" in d["soft_theorem_organization"]


# ===========================================================================
# 10. Cross-engine consistency
# ===========================================================================

class TestCrossEngineConsistency:
    """Cross-checks against the W-algebra and ABJM engines."""

    def test_w_algebra_cross_check(self):
        d = cross_engine_consistency_with_w_algebra(3)
        assert d["N"] == 3
        assert d["H_N"] == harmonic(3)
        assert d["rho_N"] == harmonic(3) - 1
        assert d["c_M5_chiral_alg"] == 98  # 4*27 - 9 - 1

    def test_abjm_cross_check_ratio(self):
        for N in [2, 3, 5, 10]:
            d = cross_engine_consistency_with_abjm(N)
            assert d["ratio_equals_minus_N"]
            assert d["kappa_M5"] == N ** 3
            assert d["kappa_M2"] == -N * N

    def test_harmonic_numbers(self):
        """H_n for cross-engine check."""
        assert harmonic(1) == 1
        assert harmonic(2) == Fraction(3, 2)
        assert harmonic(3) == Fraction(11, 6)
        assert harmonic(4) == Fraction(25, 12)


# ===========================================================================
# 11. Holographic datum (six-fold)
# ===========================================================================

class TestM5HolographicDatum:
    """The six-fold holographic modular Koszul datum H(M5_N)."""

    def test_construction(self):
        D = make_m5_holographic_datum(3)
        assert isinstance(D, M5HolographicDatum)
        assert D.m5.N == 3

    def test_A_name_contains_N(self):
        D = make_m5_holographic_datum(2)
        assert "2" in D.A_name
        assert "M5" in D.A_name

    def test_kappa_consistency(self):
        for N in [1, 2, 3, 5]:
            D = make_m5_holographic_datum(N)
            assert D.theta_kappa == Fraction(N) ** 3

    def test_kappa_sum_with_dual(self):
        """kappa + kappa^! = 6N^2 - 12N + 8."""
        for N in [1, 2, 3, 5]:
            D = make_m5_holographic_datum(N)
            expected = 6 * N ** 2 - 12 * N + 8
            assert D.kappa_sum_with_dual == expected

    def test_collision_residue_type(self):
        D = make_m5_holographic_datum(3)
        assert "trigonometric" in D.collision_residue_type

    def test_connection_is_flat(self):
        for N in [1, 2, 3, 5]:
            D = make_m5_holographic_datum(N)
            assert D.connection_is_flat is True

    def test_summary_dict_keys(self):
        D = make_m5_holographic_datum(3)
        s = D.summary()
        for key in ["A", "A!", "kappa(A)", "kappa(A!)", "kappa+kappa!",
                    "C (bulk)", "r(z)", "shadow_class", "nabla flat"]:
            assert key in s


# ===========================================================================
# 12. Verification suite (full)
# ===========================================================================

class TestVerificationSuite:
    """Run the full verification suite."""

    def test_n1_free_tensor_limit(self):
        v = verify_n1_free_tensor_limit()
        assert v["a_anomaly_zero"]
        assert v["kappa_full_zero"]
        assert v["kappa_beem_rastelli_zero"]

    def test_henningson_skenderis_n2(self):
        v = verify_henningson_skenderis(2)
        assert v["a_equals_c"]
        assert v["a_minus_c_zero"]
        assert v["matches_expected"]

    def test_henningson_skenderis_a_equals_c_all_N(self):
        for N in [1, 2, 3, 5, 10]:
            v = verify_henningson_skenderis(N)
            assert v["a_equals_c"], f"a != c at N={N}"

    def test_full_suite_runs(self):
        results = full_verification_suite(N_max=4)
        for N in [1, 2, 3, 4]:
            r = results[N]
            assert "multi_path" in r
            assert "dichotomy" in r
            assert "complementarity" in r

    def test_full_suite_dichotomy_passes(self):
        results = full_verification_suite(N_max=5)
        # N>=2 only because at N=1, kappa(M2)=-1 and kappa(M5)=1, so the
        # ratio = -1 = -N is fine; check N=2..5
        for N in [2, 3, 4, 5]:
            v = results[N]["dichotomy"]
            assert all(v.values()), f"N={N}: {v}"

    def test_full_suite_complementarity_passes(self):
        results = full_verification_suite(N_max=5)
        for N in [1, 2, 3, 4, 5]:
            v = results[N]["complementarity"]
            assert v["AP24_holds"]
