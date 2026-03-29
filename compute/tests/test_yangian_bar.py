"""Tests for compute/lib/yangian_bar.py — Yangian bar complex and E_1-chiral structure.

Verifies:
  - Yangian generator counts (dim(g) per level)
  - RTT relation counts (dim(g)^2)
  - E_1 bar complex structure metadata
  - E_1 bar degree 2 dimensions
  - Koszulness status metadata
  - Coulomb branch data
  - Chiral bar cohomology (conjectured formula 3^n + 1)
  - Kunneth gl_2 decomposition
  - Serre correction pattern
  - Recurrence relation a(n) = 4*a(n-1) - 3*a(n-2)
  - Cross-family consistency (sl_2 vs sl_3 scaling)

References:
  yangians_foundations.tex, yangians_computations.tex
  thm:e1-duality-main in koszul_pair_structure.tex
  conj:yangian-bar-gf in genus_expansions.tex
"""

import pytest
from sympy import Rational

from compute.lib.yangian_bar import (
    YANGIAN_DATA,
    yangian_generator_count,
    yangian_rtt_relation_count,
    e1_bar_structure,
    e1_bar_deg2_dim,
    yangian_koszulness_status,
    coulomb_branch_data,
    YANGIAN_BAR_COHOMOLOGY_KNOWN,
    yangian_bar_cohomology_conjectured,
    yangian_bar_kunneth_gl2,
    yangian_serre_correction,
    verify_yangian,
)


# ═══════════════════════════════════════════════════════════════
# Import test
# ═══════════════════════════════════════════════════════════════

class TestImport:
    def test_module_loads(self):
        """Module imports without error."""
        import compute.lib.yangian_bar
        assert hasattr(compute.lib.yangian_bar, 'YANGIAN_DATA')


# ═══════════════════════════════════════════════════════════════
# Yangian data
# ═══════════════════════════════════════════════════════════════

class TestYangianData:
    def test_sl2_dimension(self):
        """dim(sl_2) = 3."""
        assert YANGIAN_DATA["sl2"]["g_dim"] == 3

    def test_sl3_dimension(self):
        """dim(sl_3) = 8."""
        assert YANGIAN_DATA["sl3"]["g_dim"] == 8

    def test_sl2_basis_count(self):
        """sl_2 basis should have 3 elements."""
        assert len(YANGIAN_DATA["sl2"]["basis"]) == 3

    def test_sl3_basis_count(self):
        """sl_3 basis should have 8 elements."""
        assert len(YANGIAN_DATA["sl3"]["basis"]) == 8

    def test_sl2_basis_standard(self):
        """sl_2 basis should be {e, h, f}."""
        assert set(YANGIAN_DATA["sl2"]["basis"]) == {"e", "h", "f"}


# ═══════════════════════════════════════════════════════════════
# Generator counts
# ═══════════════════════════════════════════════════════════════

class TestGeneratorCount:
    def test_sl2_level0(self):
        """Y(sl_2) level 0: 3 generators (J^e_0, J^h_0, J^f_0)."""
        assert yangian_generator_count("sl2", 0) == 3

    def test_sl2_level1(self):
        """Y(sl_2) through level 1: 6 generators."""
        assert yangian_generator_count("sl2", 1) == 6

    def test_sl2_level_n(self):
        """Y(sl_2) through level N: 3*(N+1) generators."""
        for N in range(10):
            assert yangian_generator_count("sl2", N) == 3 * (N + 1)

    def test_sl3_level0(self):
        """Y(sl_3) level 0: 8 generators."""
        assert yangian_generator_count("sl3", 0) == 8

    def test_sl3_level_n(self):
        """Y(sl_3) through level N: 8*(N+1) generators."""
        for N in range(10):
            assert yangian_generator_count("sl3", N) == 8 * (N + 1)

    def test_monotone_increasing(self):
        """Generator count is strictly increasing with level."""
        for g in ["sl2", "sl3"]:
            prev = 0
            for N in range(10):
                current = yangian_generator_count(g, N)
                assert current > prev
                prev = current


# ═══════════════════════════════════════════════════════════════
# RTT relations
# ═══════════════════════════════════════════════════════════════

class TestRTTRelations:
    def test_sl2_rtt_count(self):
        """sl_2 RTT: dim(g)^2 = 9 relations."""
        assert yangian_rtt_relation_count("sl2") == 9

    def test_sl3_rtt_count(self):
        """sl_3 RTT: dim(g)^2 = 64 relations."""
        assert yangian_rtt_relation_count("sl3") == 64

    def test_rtt_is_dim_squared(self):
        """RTT relation count = dim(g)^2 for all g."""
        for g in ["sl2", "sl3"]:
            dim = YANGIAN_DATA[g]["g_dim"]
            assert yangian_rtt_relation_count(g) == dim ** 2


# ═══════════════════════════════════════════════════════════════
# E_1 bar complex structure
# ═══════════════════════════════════════════════════════════════

class TestE1BarStructure:
    def test_sl2_structure(self):
        """E_1 bar structure for sl_2 should specify E_1 operad."""
        s = e1_bar_structure("sl2")
        assert "E_1" in s["operad"]
        assert "Conf_n(R)" in s["config_space"]

    def test_koszul_dual_sl2(self):
        """E_1 Koszul dual of Y(sl_2) is U_q(sl_2)."""
        s = e1_bar_structure("sl2")
        assert s["koszul_dual"] == "U_q(sl_2)"

    def test_koszul_dual_sl3(self):
        """E_1 Koszul dual of Y(sl_3) is U_q(sl_3)."""
        s = e1_bar_structure("sl3")
        assert s["koszul_dual"] == "U_q(sl_3)"

    def test_noncommutative_framework(self):
        """E_1 framework is noncommutative."""
        s = e1_bar_structure("sl2")
        assert "noncommutative" in s["framework"]


# ═══════════════════════════════════════════════════════════════
# E_1 bar degree 2
# ═══════════════════════════════════════════════════════════════

class TestE1BarDeg2:
    def test_sl2_bar_deg2(self):
        """B^2_{E_1}(sl_2) = dim(g)^2 = 9."""
        assert e1_bar_deg2_dim("sl2") == 9

    def test_sl3_bar_deg2(self):
        """B^2_{E_1}(sl_3) = dim(g)^2 = 64."""
        assert e1_bar_deg2_dim("sl3") == 64

    def test_bar_deg2_consistent_with_dim(self):
        """B^2_{E_1} = dim(g)^2 for all g."""
        for g in ["sl2", "sl3"]:
            dim = YANGIAN_DATA[g]["g_dim"]
            assert e1_bar_deg2_dim(g) == dim ** 2


# ═══════════════════════════════════════════════════════════════
# Chiral bar cohomology (conjectured)
# ═══════════════════════════════════════════════════════════════

class TestBarCohomology:
    """Test the conjectured bar cohomology formula H^n = 3^n + 1."""

    def test_known_values(self):
        """Conjectured formula matches all known computed values."""
        for n, expected in YANGIAN_BAR_COHOMOLOGY_KNOWN.items():
            assert yangian_bar_cohomology_conjectured(n) == expected

    def test_formula_3n_plus_1(self):
        """H^n(Y(sl_2)) = 3^n + 1 for n >= 1."""
        for n in range(1, 10):
            assert yangian_bar_cohomology_conjectured(n) == 3**n + 1

    def test_degree_zero(self):
        """H^0 = 1 (vacuum)."""
        assert yangian_bar_cohomology_conjectured(0) == 1

    def test_recurrence(self):
        """a(n) = 4*a(n-1) - 3*a(n-2) for a(n) = 3^n + 1.

        This recurrence is the structural prediction from the conjectured GF.
        Verify it independently: 4*(3^{n-1}+1) - 3*(3^{n-2}+1)
          = 4*3^{n-1} + 4 - 3^{n-1} - 3 = 3*3^{n-1} + 1 = 3^n + 1.
        """
        for n in range(3, 15):
            a_n = yangian_bar_cohomology_conjectured(n)
            a_n1 = yangian_bar_cohomology_conjectured(n - 1)
            a_n2 = yangian_bar_cohomology_conjectured(n - 2)
            assert a_n == 4 * a_n1 - 3 * a_n2

    def test_monotone_increasing(self):
        """Bar cohomology dimensions should be strictly increasing."""
        for n in range(1, 20):
            assert yangian_bar_cohomology_conjectured(n + 1) > yangian_bar_cohomology_conjectured(n)

    def test_growth_rate(self):
        """Growth rate should approach 3 (dominant eigenvalue of recurrence).

        a(n+1)/a(n) -> 3 as n -> infinity.
        """
        for n in [10, 20, 50]:
            ratio = yangian_bar_cohomology_conjectured(n + 1) / yangian_bar_cohomology_conjectured(n)
            assert abs(ratio - 3.0) < 0.01


# ═══════════════════════════════════════════════════════════════
# Kunneth / Serre correction
# ═══════════════════════════════════════════════════════════════

class TestKunnethSerre:
    """Test the gl_2 Kunneth decomposition and Serre correction."""

    def test_kunneth_matches_at_low_degrees(self):
        """At degrees 1-2, the Kunneth decomposition matches the Yangian."""
        for n in [1, 2]:
            kunneth = yangian_bar_kunneth_gl2(n)
            yangian = YANGIAN_BAR_COHOMOLOGY_KNOWN[n]
            assert kunneth == yangian

    def test_serre_correction_zero_at_deg_1(self):
        """Serre correction vanishes at degree 1."""
        assert yangian_serre_correction(1) == 0

    def test_serre_correction_zero_at_deg_2(self):
        """Serre correction vanishes at degree 2."""
        assert yangian_serre_correction(2) == 0

    def test_serre_correction_nonzero_at_deg_3(self):
        """Serre correction = 3 at degree 3 (first nonzero)."""
        assert yangian_serre_correction(3) == 3

    def test_serre_correction_nonnegative(self):
        """Serre correction should be non-negative (additional classes)."""
        for n in range(1, 10):
            assert yangian_serre_correction(n) >= 0


# ═══════════════════════════════════════════════════════════════
# Koszulness status
# ═══════════════════════════════════════════════════════════════

class TestKoszulnessStatus:
    def test_sl2_conjectured(self):
        """Y(sl_2) Koszulness is conjectured."""
        status = yangian_koszulness_status("sl2")
        assert status["status"] == "conjectured"

    def test_sl3_conjectured(self):
        """Y(sl_3) Koszulness is conjectured."""
        status = yangian_koszulness_status("sl3")
        assert status["status"] == "conjectured"


# ═══════════════════════════════════════════════════════════════
# Coulomb branch
# ═══════════════════════════════════════════════════════════════

class TestCoulombBranch:
    def test_sl2_coulomb_data(self):
        """Coulomb branch data for sl_2 should specify Yangian."""
        data = coulomb_branch_data("sl2")
        assert "Y(sl2)" in data["algebra"]
        assert "Coulomb" in data["geometry"]

    def test_koszul_dual_is_quantum_group(self):
        """Koszul dual should reference the quantum group."""
        data = coulomb_branch_data("sl2")
        assert "U_q" in data["koszul_dual"]


# ═══════════════════════════════════════════════════════════════
# Full verification suite
# ═══════════════════════════════════════════════════════════════

class TestVerifyYangian:
    def test_all_verifications_pass(self):
        """The module's built-in verify_yangian() should all pass."""
        results = verify_yangian()
        for name, ok in results.items():
            assert ok, f"FAIL: {name}"


# ═══════════════════════════════════════════════════════════════
# Cross-family consistency (AP10 prevention)
# ═══════════════════════════════════════════════════════════════

class TestCrossFamilyConsistency:
    """Cross-family checks to prevent hardcoded-wrong-expected-value errors."""

    def test_generator_scaling_sl2_vs_sl3(self):
        """Generator counts scale as dim(g): sl_3/sl_2 ratio = 8/3."""
        for N in range(5):
            ratio = yangian_generator_count("sl3", N) / yangian_generator_count("sl2", N)
            assert abs(ratio - 8 / 3) < 1e-10

    def test_rtt_scaling_sl2_vs_sl3(self):
        """RTT counts scale as dim(g)^2: sl_3/sl_2 ratio = 64/9."""
        ratio = yangian_rtt_relation_count("sl3") / yangian_rtt_relation_count("sl2")
        assert abs(ratio - 64 / 9) < 1e-10

    def test_bar_deg2_scaling(self):
        """E_1 bar deg 2 scales as dim(g)^2."""
        ratio = e1_bar_deg2_dim("sl3") / e1_bar_deg2_dim("sl2")
        assert abs(ratio - 64 / 9) < 1e-10
