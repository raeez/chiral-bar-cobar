"""Tests for the All-Genus Chiral Homology Package.

Verifies the complete chiral homology computation across all genera,
all standard families, and all computational levels.

WHAT IS TESTED (proved content only — no conjectural claims):

  LAYER I:   Scalar genus tower F_g = kappa * lambda_g^FP (Theorem D)
             Universal, all levels, all genera.

  LAYER II:  PBW genus-independence at GENERIC level (MC1)
             Bar cohomology dimensions match genus-0 at all genera.

  LAYER III: Complementarity kappa(A) + kappa(A!) (Theorem C)
             Level-independent, root-datum constant.

  LAYER IV:  Verlinde formula at INTEGRABLE levels
             Conformal block dimensions as separate data.

ADVERSARIAL NOTES (what we do NOT claim):
  - We do NOT claim fiberwise genus-independence at integrable levels.
  - We do NOT claim Verlinde recovery from the bar complex is proved.
    (Remark rem:verlinde-vs-kappa flags this as an OPEN test.)
  - The monograph formula Z_g = sum (d_j)^{2-2g} is the normalized
    partition function, which can be non-integer for g >= 2.
    The conformal block dimension uses exponent (2g-2) instead.
"""

import math
import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.chiral_homology_allgenus import (
    BAR_COHOMOLOGY,
    bar_hilbert_series,
    fiberwise_chiral_homology_dim,
    verify_pbw_genus_independence,
    chiral_homology_package,
    complementarity_kappa_sum,
    spectral_discriminant,
    heisenberg_bar_cohomology_predicted,
    verlinde_conformal_blocks_sl2,
    verify_allgenus_package,
)
from compute.lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_sl2, kappa_sl3,
    kappa_g2, kappa_b2, kappa_w3,
    genus_table,
)
from compute.lib.utils import lambda_fp, F_g, partition_number


# ============================================================================
# LAYER I: SCALAR GENUS TOWER (Theorem D — PROVED, universal)
# ============================================================================

class TestScalarGenusTower:
    """F_g(A) = kappa(A) * lambda_g^FP.  Universal.  All levels."""

    def test_ahat_heisenberg(self):
        """F_g(H_1) = lambda_g^FP for all g."""
        for g in range(1, 11):
            assert F_g(Rational(1), g) == lambda_fp(g)

    def test_ahat_sl2(self):
        """F_g(sl2_k) = 3(k+2)/4 * lambda_g for all g, k."""
        for k_val in [1, 2, 5, 10]:
            kv = kappa_sl2(k_val)
            for g in range(1, 6):
                assert F_g(kv, g) == kv * lambda_fp(g)

    def test_ahat_virasoro(self):
        """F_g(Vir_c) = (c/2) * lambda_g for all g, c."""
        for c_val in [1, 2, 13, 25, 26]:
            kv = kappa_virasoro(c_val)
            for g in range(1, 6):
                assert F_g(kv, g) == kv * lambda_fp(g)

    def test_critical_level_vanishing(self):
        """At critical level k = -h*, kappa = 0, so F_g = 0 for all g."""
        assert kappa_sl2(-2) == 0
        assert kappa_sl3(-3) == 0
        assert kappa_g2(-4) == 0
        assert kappa_b2(-3) == 0
        for g in range(1, 11):
            assert F_g(Rational(0), g) == 0

    def test_genus1_obstruction(self):
        """F_1 = kappa/24."""
        assert F_g(Rational(1), 1) == Rational(1, 24)
        assert F_g(kappa_virasoro(2), 1) == Rational(1, 24)
        assert F_g(kappa_sl2(1), 1) == Rational(9, 4) / 24

    def test_bernoulli_asymptotics(self):
        """lambda_{g+1}/lambda_g -> 1/(2pi)^2 as g -> inf."""
        target = 1 / (2 * math.pi) ** 2
        for g in range(8, 15):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            assert ratio > target * 0.95
            assert ratio < 1

    def test_convergence_radius_2pi(self):
        """(2pi)^{2g} * lambda_g -> 2 as g -> inf."""
        for g in range(10, 16):
            val = float((2 * math.pi) ** (2 * g) * lambda_fp(g))
            assert abs(val - 2) < 0.5

    def test_sl2_genus_table_manuscript(self):
        """F_g(sl2, k=1) matches manuscript Table comp:sl2-genus-table."""
        kv = kappa_sl2(1)  # = 9/4
        table = genus_table(kv, max_genus=3)
        assert table[1] == Rational(3, 32)
        assert table[2] == Rational(7, 2560)
        assert table[3] == Rational(31, 430080)

    def test_virasoro_c26_bosonic_string(self):
        """F_g(Vir_26) = 13 * lambda_g (bosonic string target space)."""
        kv = kappa_virasoro(26)
        assert kv == 13
        for g in range(1, 6):
            assert F_g(kv, g) == 13 * lambda_fp(g)

    def test_genus_tower_exact_arithmetic(self):
        """All F_g are exact rationals, positive, through g = 10."""
        table = genus_table(Rational(1), max_genus=10)
        assert len(table) == 10
        for g, fg in table.items():
            assert fg > 0
            assert isinstance(fg, Rational)


# ============================================================================
# LAYER II: PBW GENUS-INDEPENDENCE AT GENERIC LEVEL (MC1)
# ============================================================================

class TestPBWGenusIndependence:
    """At generic level: bar cohomology dims are genus-independent."""

    def test_heisenberg_generic(self):
        assert all(verify_pbw_genus_independence("Heisenberg", 10))

    def test_virasoro_generic(self):
        assert all(verify_pbw_genus_independence("Virasoro", 10))

    def test_sl2_generic(self):
        assert all(verify_pbw_genus_independence("sl2", 10))

    def test_sl3_generic(self):
        assert all(verify_pbw_genus_independence("sl3", 10))

    def test_betagamma_generic(self):
        assert all(verify_pbw_genus_independence("betagamma", 10))

    def test_free_fermion_generic(self):
        assert all(verify_pbw_genus_independence("free_fermion", 10))

    def test_heisenberg_is_partitions(self):
        """H^n(B-bar(H)) = p(n-1) (partition numbers)."""
        for n in range(1, 9):
            assert BAR_COHOMOLOGY["Heisenberg"][n] == partition_number(n - 1)

    def test_betagamma_matches_heisenberg(self):
        """betagamma and Heisenberg share the same bar cohomology (same sheet)."""
        h_dims = bar_hilbert_series("Heisenberg")
        bg_dims = bar_hilbert_series("betagamma")
        for n in h_dims:
            if n in bg_dims:
                assert h_dims[n] == bg_dims[n]

    def test_sl2_h1_equals_dim_g(self):
        """H^1(B-bar(g_k)) = dim(g) (degree-1 = generators)."""
        assert BAR_COHOMOLOGY["sl2"][1] == 3   # dim(sl_2)
        assert BAR_COHOMOLOGY["sl3"][1] == 8   # dim(sl_3)


# ============================================================================
# LAYER III: COMPLEMENTARITY (Theorem C — PROVED)
# ============================================================================

class TestComplementarity:
    """kappa(A) + kappa(A!) = root-datum constant.  Level-independent."""

    def test_km_zero(self):
        """Affine KM: kappa(g_k) + kappa(g_{-k-2h*}) = 0."""
        for k_val in [1, 2, 3, 5, 10, 100]:
            assert kappa_sl2(k_val) + kappa_sl2(-k_val - 4) == 0
        for k_val in [1, 2, 5]:
            assert kappa_sl3(k_val) + kappa_sl3(-k_val - 6) == 0

    def test_virasoro_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        for c_val in [0, 1, 2, 13, 25, 26, Rational(1, 2)]:
            assert kappa_virasoro(c_val) + kappa_virasoro(26 - c_val) == 13

    def test_virasoro_selfdual_c13(self):
        """Virasoro self-dual at c = 13 (NOT c = 26)."""
        assert kappa_virasoro(13) == kappa_virasoro(26 - 13)

    def test_w3_250_over_3(self):
        """kappa(W3_c) + kappa(W3_{100-c}) = 250/3."""
        for c_val in [2, 10, 50]:
            assert kappa_w3(c_val) + kappa_w3(100 - c_val) == Rational(250, 3)

    def test_complementarity_allgenera(self):
        """F_g(A) + F_g(A!) = constant * lambda_g at every genus."""
        for g in range(1, 8):
            for k_val in [1, 3, 7]:
                assert F_g(kappa_sl2(k_val), g) + F_g(kappa_sl2(-k_val - 4), g) == 0
        for g in range(1, 8):
            for c_val in [1, 7, 13]:
                s = F_g(kappa_virasoro(c_val), g) + F_g(kappa_virasoro(26 - c_val), g)
                assert s == 13 * lambda_fp(g)

    def test_discriminant_shared(self):
        """DS-related families share spectral discriminant."""
        assert spectral_discriminant("Virasoro") == spectral_discriminant("sl2")
        assert spectral_discriminant("Heisenberg") == spectral_discriminant("betagamma")

    def test_complementarity_sums(self):
        assert complementarity_kappa_sum("sl2") == 0
        assert complementarity_kappa_sum("Virasoro") == 13
        assert complementarity_kappa_sum("W3") == Rational(250, 3)
        assert complementarity_kappa_sum("Heisenberg") == 0


# ============================================================================
# LAYER IV: VERLINDE AT INTEGRABLE LEVELS
# ============================================================================

class TestVerlindeIntegrable:
    """Verlinde conformal block dimensions (separate from bar complex).

    Remark rem:verlinde-vs-kappa: Verlinde recovery from bar complex is OPEN.
    """

    def test_sl2_genus0(self):
        for k in range(1, 8):
            assert verlinde_conformal_blocks_sl2(k, 0) == 1

    def test_sl2_genus1(self):
        for k in range(1, 10):
            assert verlinde_conformal_blocks_sl2(k, 1) == k + 1

    def test_sl2_k1_constant(self):
        """SU(2) level 1: V_g = 2 for all g >= 1."""
        for g in range(1, 6):
            assert verlinde_conformal_blocks_sl2(1, g) == 2

    def test_sl2_k2_genus2(self):
        """SU(2) k=2, g=2: d_j = {1, sqrt(2), 1}, sum d_j^2 = 4."""
        assert verlinde_conformal_blocks_sl2(2, 2) == 4

    def test_sl2_k2_genus3(self):
        """SU(2) k=2, g=3: sum d_j^4 = 1 + 4 + 1 = 6."""
        assert verlinde_conformal_blocks_sl2(2, 3) == 6

    def test_verlinde_are_integers(self):
        for k in range(1, 6):
            for g in range(1, 5):
                v = verlinde_conformal_blocks_sl2(k, g)
                assert isinstance(v, int) and v > 0

    def test_verlinde_growth(self):
        """For k >= 2, conformal block dims grow with genus."""
        for k in [2, 3, 4]:
            assert verlinde_conformal_blocks_sl2(k, 3) >= verlinde_conformal_blocks_sl2(k, 2)

    def test_scalar_tower_vs_verlinde(self):
        """F_g (c_1 of det bundle) and Verlinde (rank) are independent data."""
        for k_val in [1, 2, 3]:
            kv = kappa_sl2(k_val)
            for g in range(1, 4):
                fg = F_g(kv, g)
                vn = verlinde_conformal_blocks_sl2(k_val, g)
                assert fg > 0 and vn > 0
                assert isinstance(fg, Rational)
                assert isinstance(vn, int)


# ============================================================================
# KAPPA MASTER TABLE
# ============================================================================

class TestKappaMasterTable:
    def test_kappa_km_formula(self):
        assert kappa_sl2(0) == Rational(3, 2)
        assert kappa_sl2(1) == Rational(9, 4)
        assert kappa_sl3(0) == Rational(4)
        assert kappa_sl3(1) == Rational(16, 3)
        assert kappa_g2(0) == Rational(7)
        assert kappa_b2(0) == Rational(5)

    def test_kappa_virasoro(self):
        assert kappa_virasoro(0) == 0
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(26) == 13

    def test_kappa_w3(self):
        assert kappa_w3(0) == 0
        assert kappa_w3(6) == 5

    def test_kappa_additivity(self):
        assert kappa_heisenberg(1) + kappa_heisenberg(2) == kappa_heisenberg(3)

    def test_kappa_antisymmetry(self):
        for k_val in [0, 1, 2, 5]:
            assert kappa_sl2(k_val) + kappa_sl2(-k_val - 4) == 0


# ============================================================================
# HILBERT SERIES STRUCTURE
# ============================================================================

class TestHilbertSeries:
    def test_heisenberg_monotone(self):
        dims = bar_hilbert_series("Heisenberg")
        prev = 0
        for n in sorted(dims.keys()):
            if n >= 3:
                assert dims[n] >= prev
            prev = dims[n]

    def test_virasoro_growth_bounded(self):
        dims = bar_hilbert_series("Virasoro")
        keys = sorted(dims.keys())
        for i in range(1, len(keys)):
            if keys[i] == keys[i - 1] + 1 and dims[keys[i - 1]] > 0:
                assert 1 <= dims[keys[i]] / dims[keys[i - 1]] <= 5


# ============================================================================
# COMPLETE PACKAGE
# ============================================================================

class TestCompletePackage:
    def test_heisenberg(self):
        pkg = chiral_homology_package("Heisenberg", 1, max_genus=5)
        assert pkg["kappa"] == 1
        assert pkg["pbw_genus_independent_at_generic_level"] is True
        assert pkg["genus_tower"][1] == Rational(1, 24)

    def test_verlinde_status_open(self):
        pkg = chiral_homology_package("sl2", 1)
        assert "OPEN" in pkg["verlinde_recovery_status"]

    def test_master_heisenberg(self):
        for name, ok in verify_allgenus_package("Heisenberg").items():
            assert ok, f"Heisenberg: {name}"

    def test_master_virasoro(self):
        for name, ok in verify_allgenus_package("Virasoro").items():
            assert ok, f"Virasoro: {name}"

    def test_master_sl2(self):
        for name, ok in verify_allgenus_package("sl2").items():
            assert ok, f"sl2: {name}"


# ============================================================================
# EDGE CASES
# ============================================================================

class TestEdgeCases:
    def test_uncurved_c0(self):
        assert kappa_virasoro(0) == 0

    def test_dual_uncurved_c26(self):
        assert kappa_virasoro(26) == 13
        assert kappa_virasoro(0) == 0

    def test_critical_level_all(self):
        assert kappa_sl2(-2) == 0
        assert kappa_sl3(-3) == 0
        assert kappa_g2(-4) == 0
        assert kappa_b2(-3) == 0
