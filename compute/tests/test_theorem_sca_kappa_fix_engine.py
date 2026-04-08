r"""Tests for the superconformal algebra kappa fix engine.

AP49 cross-volume verification: N=2 SCA and N=4 small SCA kappa formulas.

Multi-path verification (AP mandate: >= 3 independent paths per claim):
  - Direct formula evaluation
  - Coset decomposition
  - Complementarity sum constancy
  - Limiting cases (k=0, k=1, k->inf)
  - Cross-family consistency
  - Comparison with Vol I authoritative values
  - Comparison with existing compute engines
  - AP48 violation detection (kappa != c/2)

Target: >= 30 tests.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_sca_kappa_fix_engine import (
    # N=2 SCA
    n2_central_charge,
    n2_level_from_c,
    kappa_n2_from_level,
    kappa_n2_from_c,
    kappa_n2_coset_decomposition,
    n2_koszul_dual_c,
    n2_complementarity_sum,
    n2_kappa_multipath,
    # N=4 small SCA
    n4_central_charge,
    n4_level_from_c,
    kappa_n4_from_level,
    kappa_n4_from_c,
    n4_koszul_dual_c,
    n4_complementarity_sum_ff,
    n4_complementarity_sum_cy,
    n4_kappa_multipath,
    # N=1 SVir
    kappa_svir,
    # Hierarchy
    superconformal_hierarchy,
    # AP49 verification
    verify_n2_ap49_discrepancy,
    verify_n4_ap49_discrepancy,
)


# ============================================================================
# N=2 SCA: kappa = (6-c)/(2(3-c)) = (k+4)/4
# ============================================================================

class TestN2KappaFormula:
    """Verify the correct N=2 SCA kappa formula."""

    def test_n2_kappa_at_c1_k1(self):
        """At c=1 (k=1): kappa = (6-1)/(2*2) = 5/4."""
        assert kappa_n2_from_c(Fraction(1)) == Fraction(5, 4)
        assert kappa_n2_from_level(Fraction(1)) == Fraction(5, 4)

    def test_n2_kappa_at_c2_k2(self):
        """At c=2 (k=2): kappa = (6-2)/(2*1) = 2."""
        c = Fraction(2)
        k = n2_level_from_c(c)
        assert k == Fraction(4)  # k = 2*2/(3-2) = 4
        assert kappa_n2_from_c(c) == Fraction(2)
        assert kappa_n2_from_level(k) == Fraction(2)

    def test_n2_kappa_not_c_over_2(self):
        """AP49/AP48: kappa(N=2) != c/2 for any c != 0."""
        for c_val in [Fraction(1), Fraction(2), Fraction(5, 2)]:
            kappa_correct = kappa_n2_from_c(c_val)
            kappa_wrong = c_val / 2
            assert kappa_correct != kappa_wrong, (
                f"At c={c_val}: kappa should NOT equal c/2"
            )

    def test_n2_kappa_pole_at_c3(self):
        """kappa has a pole at c=3 (free-field limit k->inf)."""
        with pytest.raises(ValueError, match="pole"):
            kappa_n2_from_c(Fraction(3))

    def test_n2_kappa_at_k0(self):
        """At k=0: c = 0, kappa = (0+4)/4 = 1."""
        assert kappa_n2_from_level(Fraction(0)) == Fraction(1)
        assert n2_central_charge(Fraction(0)) == Fraction(0)

    def test_n2_kappa_at_critical_level(self):
        """At k=-4 (critical level for the coset): kappa = (-4+4)/4 = 0."""
        assert kappa_n2_from_level(Fraction(-4)) == Fraction(0)
        # c = 3*(-4)/(-4+2) = -12/(-2) = 6
        assert n2_central_charge(Fraction(-4)) == Fraction(6)

    def test_n2_level_c_roundtrip(self):
        """k -> c -> k should be identity."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5), Fraction(-1)]:
            c = n2_central_charge(k_val)
            k_back = n2_level_from_c(c)
            assert k_back == k_val

    def test_n2_formula_equivalence(self):
        """(6-c)/(2(3-c)) = (k+4)/4 for corresponding k, c."""
        for k_val in [Fraction(1), Fraction(2), Fraction(3), Fraction(10)]:
            c = n2_central_charge(k_val)
            from_c = kappa_n2_from_c(c)
            from_k = kappa_n2_from_level(k_val)
            assert from_c == from_k


class TestN2CosetDecomposition:
    """Verify kappa via the Kazama-Suzuki coset decomposition."""

    def test_coset_at_k1(self):
        """At k=1: coset gives kappa = 3*3/4 + 1/2 - 3/2 = 9/4 + 1/2 - 3/2 = 5/4."""
        result = kappa_n2_coset_decomposition(Fraction(1))
        assert result['kappa_sl2_k'] == Fraction(9, 4)  # 3*(1+2)/4
        assert result['kappa_fermion'] == Fraction(1, 2)
        assert result['kappa_u1_denom'] == Fraction(3, 2)  # 1/2 + 1
        assert result['kappa_total'] == Fraction(5, 4)
        assert result['formula_check'] is True

    def test_coset_at_k2(self):
        """At k=2: kappa = 3*4/4 + 1/2 - 2 = 3 + 1/2 - 2 = 3/2."""
        result = kappa_n2_coset_decomposition(Fraction(2))
        assert result['kappa_total'] == Fraction(3, 2)
        assert result['formula_check'] is True

    def test_coset_agrees_with_direct(self):
        """Coset decomposition agrees with direct formula for all test levels."""
        for k_val in [Fraction(1), Fraction(3), Fraction(5), Fraction(-1)]:
            result = kappa_n2_coset_decomposition(k_val)
            direct = kappa_n2_from_level(k_val)
            assert result['kappa_total'] == direct


class TestN2Complementarity:
    """Verify kappa(c) + kappa(6-c) = 1."""

    def test_complementarity_sum_at_c1(self):
        """At c=1: kappa(1) + kappa(5) = 5/4 + (-1/4) = 1? Let's check."""
        # kappa(1) = (6-1)/(2*2) = 5/4
        # kappa(5) = (6-5)/(2*(3-5)) = 1/(-4) = -1/4
        assert n2_complementarity_sum(Fraction(1)) == Fraction(1)

    def test_complementarity_sum_at_c2(self):
        """At c=2: kappa(2) + kappa(4) should be 1."""
        assert n2_complementarity_sum(Fraction(2)) == Fraction(1)

    def test_complementarity_sum_constant(self):
        """The complementarity sum is 1 for all c != 3."""
        for c_val in [Fraction(1), Fraction(2), Fraction(1, 2),
                      Fraction(5), Fraction(-1), Fraction(10)]:
            assert n2_complementarity_sum(c_val) == Fraction(1)

    def test_koszul_dual_involution(self):
        """c -> 6-c is an involution: (6-(6-c)) = c."""
        for c_val in [Fraction(1), Fraction(2), Fraction(-3)]:
            assert n2_koszul_dual_c(n2_koszul_dual_c(c_val)) == c_val


class TestN2Multipath:
    """Multi-path verification (3+ paths)."""

    def test_multipath_at_c1(self):
        """All 3 paths agree at c=1."""
        result = n2_kappa_multipath(Fraction(1))
        assert result['all_agree'] is True
        assert result['comp_is_one'] is True

    def test_multipath_at_c2(self):
        """All 3 paths agree at c=2."""
        result = n2_kappa_multipath(Fraction(2))
        assert result['all_agree'] is True
        assert result['comp_is_one'] is True


# ============================================================================
# N=4 small SCA: kappa = 2k = c/3
# ============================================================================

class TestN4KappaFormula:
    """Verify the correct N=4 small SCA kappa formula."""

    def test_n4_kappa_at_k1_c6(self):
        """At k=1 (c=6, K3): kappa = 2."""
        assert kappa_n4_from_level(Fraction(1)) == Fraction(2)
        assert kappa_n4_from_c(Fraction(6)) == Fraction(2)

    def test_n4_kappa_at_k2_c12(self):
        """At k=2 (c=12): kappa = 4."""
        assert kappa_n4_from_level(Fraction(2)) == Fraction(4)
        assert kappa_n4_from_c(Fraction(12)) == Fraction(4)

    def test_n4_kappa_not_c_over_2(self):
        """AP48: kappa(N=4) = c/3 != c/2."""
        for c_val in [Fraction(6), Fraction(12), Fraction(18)]:
            assert kappa_n4_from_c(c_val) != c_val / 2

    def test_n4_kappa_is_c_over_3(self):
        """kappa = c/3 for all c."""
        for c_val in [Fraction(6), Fraction(12), Fraction(18), Fraction(-6)]:
            assert kappa_n4_from_c(c_val) == c_val / 3

    def test_n4_kappa_ratio_to_virasoro(self):
        """kappa(N=4) / kappa(Vir) = 2/3."""
        for c_val in [Fraction(6), Fraction(12), Fraction(18)]:
            kappa_n4 = kappa_n4_from_c(c_val)
            kappa_vir = c_val / 2
            assert kappa_n4 / kappa_vir == Fraction(2, 3)

    def test_n4_level_c_roundtrip(self):
        """k -> c -> k should be identity."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5)]:
            c = n4_central_charge(k_val)
            k_back = n4_level_from_c(c)
            assert k_back == k_val


class TestN4KoszulDuality:
    """Verify N=4 Koszul duality: c -> -c - 24."""

    def test_n4_dual_at_c6(self):
        """At c=6: c' = -6-24 = -30."""
        assert n4_koszul_dual_c(Fraction(6)) == Fraction(-30)

    def test_n4_dual_involution(self):
        """c -> -c-24 is an involution: -(-c-24)-24 = c."""
        for c_val in [Fraction(6), Fraction(12), Fraction(-30)]:
            assert n4_koszul_dual_c(n4_koszul_dual_c(c_val)) == c_val

    def test_n4_self_dual_at_minus_12(self):
        """Self-dual point: c = -12 (k = -2 = -h^v(su_2))."""
        assert n4_koszul_dual_c(Fraction(-12)) == Fraction(-12)

    def test_n4_ff_complementarity_is_minus_8(self):
        """Under FF involution: kappa + kappa' = -8 (constant)."""
        for c_val in [Fraction(6), Fraction(12), Fraction(-30), Fraction(0)]:
            assert n4_complementarity_sum_ff(c_val) == Fraction(-8)

    def test_n4_cy_complementarity_is_zero(self):
        """Under CY duality (k -> -k): kappa + kappa' = 0."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5)]:
            assert n4_complementarity_sum_cy(k_val) == Fraction(0)


class TestN4Multipath:
    """Multi-path verification for N=4."""

    def test_multipath_at_k1(self):
        """All paths agree at k=1 (K3)."""
        result = n4_kappa_multipath(Fraction(1))
        assert result['agree'] is True
        assert result['not_virasoro'] is True
        assert result['path1_level'] == Fraction(2)
        assert result['ff_comp_sum'] == Fraction(-8)
        assert result['cy_comp_sum'] == Fraction(0)

    def test_multipath_at_k2(self):
        """All paths agree at k=2."""
        result = n4_kappa_multipath(Fraction(2))
        assert result['agree'] is True
        assert result['not_virasoro'] is True
        assert result['path1_level'] == Fraction(4)


# ============================================================================
# N=1 SVir (completeness)
# ============================================================================

class TestN1SVir:
    """Verify N=1 super-Virasoro kappa."""

    def test_svir_at_self_dual(self):
        """At c=15/2: kappa = (3*15/2 - 2)/4 = (45/2 - 2)/4 = 41/8."""
        assert kappa_svir(Fraction(15, 2)) == Fraction(41, 8)

    def test_svir_complementarity(self):
        """kappa(c) + kappa(15-c) = 41/4."""
        for c_val in [Fraction(1), Fraction(5), Fraction(15, 2)]:
            comp = kappa_svir(c_val) + kappa_svir(15 - c_val)
            assert comp == Fraction(41, 4)


# ============================================================================
# Superconformal hierarchy
# ============================================================================

class TestHierarchy:
    """Verify the corrected superconformal complementarity hierarchy."""

    def test_hierarchy_monotone_decreasing(self):
        """13 > 41/4 > 1 > -8."""
        h = superconformal_hierarchy()
        sums = [
            h['N0_Vir']['comp_sum'],
            h['N1_SVir']['comp_sum'],
            h['N2_SCA']['comp_sum'],
            h['N4_small']['comp_sum'],
        ]
        assert sums == [Fraction(13), Fraction(41, 4), Fraction(1), Fraction(-8)]
        for i in range(len(sums) - 1):
            assert sums[i] > sums[i + 1]

    def test_hierarchy_all_w_type(self):
        """All entries in the hierarchy are W-type (nonzero comp sum)."""
        h = superconformal_hierarchy()
        for key, data in h.items():
            assert data['type'] == 'W-type'
            assert data['comp_sum'] != 0


# ============================================================================
# AP49 discrepancy verification
# ============================================================================

class TestAP49Discrepancies:
    """Verify the detected cross-volume discrepancies."""

    def test_n2_discrepancy_detected(self):
        """N=2: correct is 5/4, Vol II had 1/2."""
        result = verify_n2_ap49_discrepancy()
        assert result['correct_kappa'] == Fraction(5, 4)
        assert result['wrong_kappa'] == Fraction(1, 2)
        assert result['is_discrepant'] is True
        assert result['discrepancy_ratio'] == Fraction(5, 2)

    def test_n4_discrepancy_detected(self):
        """N=4: correct kappa is 2, Vol II had 3 (c/2)."""
        result = verify_n4_ap49_discrepancy()
        assert result['correct_kappa'] == Fraction(2)
        assert result['wrong_kappa_vol2'] == Fraction(3)
        assert result['correct_dual_c'] == Fraction(-30)
        assert result['wrong_dual_c'] == Fraction(6)  # 12-6
        assert result['correct_comp_sum'] == Fraction(-8)
        assert result['correct_self_dual'] == Fraction(-12)


# ============================================================================
# Cross-engine consistency
# ============================================================================

class TestCrossEngineConsistency:
    """Verify consistency with existing compute engines."""

    def test_n2_agrees_with_n2_kappa_resolution(self):
        """Compare with the existing n2_kappa_resolution.py."""
        from compute.lib.n2_kappa_resolution import kappa_n2_correct
        for c_val in [Fraction(1), Fraction(2), Fraction(5, 2)]:
            assert kappa_n2_from_c(c_val) == kappa_n2_correct(c_val)

    def test_n4_agrees_with_cy_n4sca_k3_engine(self):
        """Compare with the existing cy_n4sca_k3_engine.py at k=1."""
        from compute.lib.cy_n4sca_k3_engine import kappa_n4_k3, kappa_n4_general
        assert kappa_n4_from_level(Fraction(1)) == kappa_n4_k3()
        assert kappa_n4_from_level(Fraction(1)) == kappa_n4_general(Fraction(1))
        assert kappa_n4_from_level(Fraction(2)) == kappa_n4_general(Fraction(2))

    def test_n2_agrees_with_ap49_engine(self):
        """Compare with theorem_cross_volume_ap49_engine.py."""
        from compute.lib.theorem_cross_volume_ap49_engine import kappa_n2_sca
        for c_val in [Fraction(1), Fraction(2), Fraction(5)]:
            assert kappa_n2_from_c(c_val) == kappa_n2_sca(c_val)
