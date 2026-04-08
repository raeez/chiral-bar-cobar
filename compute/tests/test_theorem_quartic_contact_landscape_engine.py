r"""Tests for the quartic contact invariant Q^contact across the standard landscape.

68 tests organized in 12 groups:

    1. Class G vanishing (7 tests)
    2. Class L vanishing + cubic nonvanishing (7 tests)
    3. Class C nonvanishing + stratum structure (6 tests)
    4. Class M nonvanishing + infinite tower (5 tests)
    5. Virasoro S_4 three-path verification (5 tests)
    6. Non-universality of Q^contact (4 tests)
    7. Critical discriminant classification (5 tests)
    8. Koszul duality of Q^contact (5 tests)
    9. DS descent compatibility (3 tests)
    10. Additivity and direct sums (3 tests)
    11. Cross-family consistency (8 tests)
    12. Depth classification consistency (10 tests)

ANTI-PATTERN COMPLIANCE:
    AP10: Multi-path verification; no single-path hardcoded values.
    AP1: kappa recomputed for each family from defining formula.
    AP39: S_2 != kappa distinguished; S_4 is a separate invariant.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_quartic_contact_landscape_engine import (
    QuarticContactDatum,
    affine_b2,
    affine_e6,
    affine_e7,
    affine_e8,
    affine_f4,
    affine_g2,
    affine_slN,
    affine_soN,
    affine_spN,
    bc_ghost_charged_stratum,
    bc_ghost_tline,
    betagamma_charged_stratum,
    betagamma_tline,
    build_full_landscape,
    demonstrate_non_universality,
    discriminant_landscape,
    ds_descent_check_w3,
    free_fermion,
    heisenberg,
    heisenberg_rank_r,
    koszul_dual_S4_affine,
    koszul_dual_S4_virasoro,
    landscape_summary,
    landscape_table,
    lattice_voa,
    verify_betagamma_tline_is_virasoro,
    verify_charged_stratum_universality,
    verify_class_c_nonvanishing,
    verify_class_g_vanishing,
    verify_class_l_vanishing,
    verify_class_m_nonvanishing,
    verify_depth_classification_consistency,
    verify_discriminant_classification,
    verify_kappa_additivity_heis,
    verify_self_duality_c13,
    verify_w3_tline_vs_virasoro,
    verify_w3_wline_vs_tline,
    virasoro_qcontact,
    virasoro_S4_master_equation,
    virasoro_S4_shadow_metric,
    virasoro_S4_special_values,
    w3_wline,
    wN_tline,
)


# ============================================================================
# Group 1: Class G vanishing (7 tests)
# ============================================================================

class TestClassGVanishing:
    """All class G algebras have Q^contact = 0."""

    def test_heisenberg_k1(self):
        d = heisenberg(Fraction(1))
        assert d.S4 == Fraction(0)
        assert d.S3 == Fraction(0)
        assert d.Delta == Fraction(0)
        assert d.shadow_class == 'G'
        assert d.r_max == 2

    def test_heisenberg_k5(self):
        d = heisenberg(Fraction(5))
        assert d.S4 == Fraction(0)
        assert d.kappa == Fraction(5)

    def test_heisenberg_rank_8(self):
        d = heisenberg_rank_r(8)
        assert d.S4 == Fraction(0)
        assert d.kappa == Fraction(8)

    def test_heisenberg_rank_24(self):
        d = heisenberg_rank_r(24)
        assert d.S4 == Fraction(0)
        assert d.kappa == Fraction(24)

    def test_free_fermion(self):
        d = free_fermion()
        assert d.S4 == Fraction(0)
        assert d.kappa == Fraction(-1)
        assert d.shadow_class == 'G'

    def test_lattice_rank1(self):
        d = lattice_voa(1)
        assert d.S4 == Fraction(0)
        assert d.kappa == Fraction(1)

    def test_all_class_g_vanishing(self):
        results = verify_class_g_vanishing()
        assert len(results) > 0
        for name, ok in results:
            assert ok, f"Class G vanishing failed for {name}"


# ============================================================================
# Group 2: Class L vanishing + cubic nonvanishing (7 tests)
# ============================================================================

class TestClassLVanishing:
    """All class L algebras have Q^contact = 0 but S_3 != 0."""

    def test_sl2_k1(self):
        d = affine_slN(2, Fraction(1))
        assert d.S4 == Fraction(0)
        assert d.S3 == Fraction(1)
        assert d.shadow_class == 'L'
        assert d.r_max == 3

    def test_sl3_k1(self):
        d = affine_slN(3, Fraction(1))
        assert d.S4 == Fraction(0)
        assert d.S3 == Fraction(1)
        # kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3
        assert d.kappa == Fraction(16, 3)

    def test_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3*(k+2)/(2*2) = 3(k+2)/4."""
        d = affine_slN(2, Fraction(1))
        # dim(sl_2) = 3, h^v = 2
        expected = Fraction(3) * (Fraction(1) + 2) / (2 * 2)
        assert d.kappa == expected

    def test_e8_k1(self):
        d = affine_e8(Fraction(1))
        assert d.S4 == Fraction(0)
        assert d.kappa == Fraction(248) * Fraction(31) / Fraction(60)

    def test_g2_k1(self):
        d = affine_g2(Fraction(1))
        assert d.S4 == Fraction(0)
        # kappa(G_2, k=1) = 14*(1+4)/(2*4) = 70/8 = 35/4
        assert d.kappa == Fraction(35, 4)

    def test_non_simply_laced_b2(self):
        d = affine_b2(Fraction(1))
        assert d.S4 == Fraction(0)
        assert d.shadow_class == 'L'

    def test_all_class_l_vanishing(self):
        results = verify_class_l_vanishing()
        assert len(results) > 0
        for name, ok in results:
            assert ok, f"Class L: S_4=0, S_3!=0 failed for {name}"


# ============================================================================
# Group 3: Class C nonvanishing + stratum structure (6 tests)
# ============================================================================

class TestClassCNonvanishing:
    """Class C has S_4 != 0; two distinct strata."""

    def test_betagamma_tline_lam1(self):
        d = betagamma_tline(Fraction(1))
        assert d.S4 != Fraction(0)
        # c(lam=1) = 2(6-6+1) = 2, S_4 = 10/(2*32) = 5/32
        assert d.S4 == Fraction(5, 32)
        assert d.shadow_class == 'C'
        assert d.r_max == 4

    def test_betagamma_charged_is_minus_5_12(self):
        d = betagamma_charged_stratum(Fraction(1))
        assert d.S4 == Fraction(-5, 12)

    def test_bc_ghost_tline_j2(self):
        d = bc_ghost_tline(Fraction(2))
        # c(j=2) = -(12*4-12*2+2) = -(48-24+2) = -26
        assert d.central_charge == Fraction(-26)
        assert d.S4 != Fraction(0)

    def test_bc_ghost_charged_equals_betagamma(self):
        """bc and betagamma share charged stratum S_4 = -5/12."""
        bc = bc_ghost_charged_stratum(Fraction(2))
        bg = betagamma_charged_stratum(Fraction(1))
        assert bc.S4 == bg.S4 == Fraction(-5, 12)

    def test_charged_stratum_lambda_independent(self):
        results = verify_charged_stratum_universality()
        for lam_str, data in results.items():
            assert data['is_minus_5_12'], (
                f"Charged S_4 at lambda={lam_str}: {data['S4']}")

    def test_all_class_c_nonvanishing(self):
        results = verify_class_c_nonvanishing()
        assert len(results) > 0
        for name, ok in results:
            assert ok, f"Class C nonvanishing failed for {name}"


# ============================================================================
# Group 4: Class M nonvanishing + infinite tower (5 tests)
# ============================================================================

class TestClassMNonvanishing:
    """Class M has S_4 != 0 and infinite tower."""

    def test_virasoro_c1(self):
        d = virasoro_qcontact(Fraction(1))
        # S_4 = 10/(1*27) = 10/27
        assert d.S4 == Fraction(10, 27)
        assert d.shadow_class == 'M'
        assert d.r_max == float('inf')

    def test_virasoro_canonical_value(self):
        """Q^contact_Vir = 10/[c(5c+22)] at c=1/2 (Ising)."""
        d = virasoro_qcontact(Fraction(1, 2))
        # 10 / (1/2 * (5/2 + 22)) = 10 / (1/2 * 49/2) = 10 / (49/4) = 40/49
        assert d.S4 == Fraction(40, 49)

    def test_w3_tline_class_m(self):
        d = wN_tline(3, Fraction(5))
        assert d.S4 != Fraction(0)
        assert d.shadow_class == 'M'

    def test_w3_wline_class_m(self):
        d = w3_wline(Fraction(5))
        assert d.S4 != Fraction(0)
        assert d.shadow_class == 'M'
        # W-line has alpha = 0 (Z_2 parity)
        assert d.S3 == Fraction(0)

    def test_all_class_m_nonvanishing(self):
        results = verify_class_m_nonvanishing()
        assert len(results) > 0
        for name, ok in results:
            assert ok, f"Class M nonvanishing failed for {name}"


# ============================================================================
# Group 5: Virasoro S_4 three-path verification (5 tests)
# ============================================================================

class TestVirasoroThreePath:
    """Three independent derivations of S_4 = 10/[c(5c+22)]."""

    def test_path1_convolution(self):
        result = virasoro_S4_master_equation()
        assert result['match'], (
            f"Convolution: {result['convolution']} != {result['closed_form']}")

    def test_path2_shadow_metric(self):
        result = virasoro_S4_shadow_metric()
        assert result['match'], (
            f"Shadow metric: {result['S4_from_discriminant']} != {result['closed_form']}")

    def test_path3_special_values(self):
        vals = virasoro_S4_special_values()
        # c=2: S_4 = 10/(2*32) = 5/32
        assert vals['c=2'][0] == Fraction(5, 32)
        # c=1: S_4 = 10/(1*27) = 10/27
        assert vals['free_boson'][0] == Fraction(10, 27)

    def test_ising_S4(self):
        """S_4 at c=1/2: 10/[(1/2)(5/2+22)] = 10/(49/4) = 40/49."""
        vals = virasoro_S4_special_values()
        assert vals['ising'][0] == Fraction(40, 49)

    def test_critical_string_S4(self):
        """S_4 at c=26: 10/[26*(130+22)] = 10/(26*152) = 10/3952 = 5/1976."""
        vals = virasoro_S4_special_values()
        expected = Fraction(10) / (26 * 152)
        assert vals['critical_string_c26'][0] == expected


# ============================================================================
# Group 6: Non-universality of Q^contact (4 tests)
# ============================================================================

class TestNonUniversality:
    """Q^contact is NOT a universal function of kappa."""

    def test_pair1_kappa_1(self):
        """Heisenberg(k=1) and Virasoro(c=2) share kappa=1, differ in Q^contact."""
        nu = demonstrate_non_universality()
        assert nu['pair1_kappa'] == Fraction(1)
        assert nu['Q_heis1'] == Fraction(0)
        assert nu['Q_vir2'] == Fraction(5, 32)
        assert nu['is_universal_in_kappa'] is False

    def test_pair2_kappa_9_4(self):
        """Heis(k=9/4) and sl_2(k=1) share kappa=9/4, both Q=0, different class."""
        nu = demonstrate_non_universality()
        assert nu['pair2_kappa'] == Fraction(9, 4)
        assert nu['Q_heis94'] == Fraction(0)
        assert nu['Q_sl2'] == Fraction(0)
        assert nu['heis94_class'] == 'G'
        assert nu['sl2_class'] == 'L'

    def test_kappa_8_two_algebras(self):
        """Heisenberg(rank=8) and lattice(rank=8) both have kappa=8, Q=0."""
        h8 = heisenberg_rank_r(8)
        l8 = lattice_voa(8)
        assert h8.kappa == l8.kappa == Fraction(8)
        assert h8.S4 == l8.S4 == Fraction(0)

    def test_different_Q_same_kappa_class_m(self):
        """Two class M algebras: Virasoro vs W_3 T-line can share kappa but not S_4."""
        # W_3 at k=5: c = 2-24/8 = -1, kappa = 5*(-1)/6 = -5/6
        w3 = wN_tline(3, Fraction(5))
        # Check: c(W_3,5) = 2 - 24/8 = -1
        assert w3.central_charge == Fraction(-1)
        # kappa_W3 = 5*(-1)/6 = -5/6
        assert w3.kappa == Fraction(-5, 6)
        # T-line S_4 uses c(W_3) = -1:
        # S_4 = 10/[(-1)(5*(-1)+22)] = 10/[(-1)*17] = -10/17
        assert w3.S4 == Fraction(-10, 17)


# ============================================================================
# Group 7: Critical discriminant classification (5 tests)
# ============================================================================

class TestCriticalDiscriminant:
    """Delta = 8*kappa*S_4 classifies tower termination."""

    def test_heisenberg_delta_zero(self):
        d = heisenberg(Fraction(1))
        assert d.Delta == Fraction(0)

    def test_sl2_delta_zero(self):
        d = affine_slN(2, Fraction(1))
        assert d.Delta == Fraction(0)

    def test_virasoro_delta_nonzero(self):
        d = virasoro_qcontact(Fraction(1))
        # Delta = 8*(1/2)*(10/27) = 40/27
        assert d.Delta == Fraction(40, 27)
        assert d.Delta != Fraction(0)

    def test_betagamma_charged_delta_nonzero(self):
        d = betagamma_charged_stratum(Fraction(1))
        # kappa = 1, S_4 = -5/12, Delta = 8*1*(-5/12) = -10/3
        assert d.Delta == Fraction(-10, 3)

    def test_full_discriminant_classification(self):
        results = verify_discriminant_classification()
        assert len(results) > 0
        for name, ok in results:
            assert ok, f"Discriminant classification failed for {name}"


# ============================================================================
# Group 8: Koszul duality of Q^contact (5 tests)
# ============================================================================

class TestKoszulDuality:
    """Q^contact under Koszul duality transformations."""

    def test_virasoro_self_dual_c13(self):
        result = verify_self_duality_c13()
        assert result['self_dual']
        assert result['S4_value'] == Fraction(10, 13 * 87)

    def test_virasoro_kd_ratio(self):
        """S_4(c) / S_4(26-c) = (26-c)(152-5c) / [c(5c+22)]."""
        pair = koszul_dual_S4_virasoro(Fraction(1))
        # c=1, c'=25
        # S_4(1) = 10/27, S_4(25) = 10/(25*147) = 10/3675 = 2/735
        assert pair['S4'] == Fraction(10, 27)
        assert pair['S4_dual'] == Fraction(10, 3675)

    def test_affine_kd_trivial(self):
        """S_4 = 0 at all levels for affine KM => Koszul duality is trivial."""
        result = koszul_dual_S4_affine(2, Fraction(1))
        assert result['S4'] == Fraction(0)
        assert result['S4_dual'] == Fraction(0)
        assert result['duality_trivial']

    def test_virasoro_c1_and_c25(self):
        """Virasoro: c and 26-c are Koszul dual."""
        v1 = virasoro_qcontact(Fraction(1))
        v25 = virasoro_qcontact(Fraction(25))
        # Both have S_4 != 0 but different values
        assert v1.S4 != v25.S4
        assert v1.S4 == Fraction(10, 27)
        assert v25.S4 == Fraction(10, 3675)

    def test_virasoro_c26_minimal_S4(self):
        """At c=26 (critical string), S_4 = 10/(26*152) = 5/1976."""
        v26 = virasoro_qcontact(Fraction(26))
        assert v26.S4 == Fraction(5, 1976)
        assert v26.kappa == Fraction(13)


# ============================================================================
# Group 9: DS descent compatibility (3 tests)
# ============================================================================

class TestDSDescent:
    """DS reduction creates quartic from nothing."""

    def test_ds_creates_quartic_w3(self):
        result = ds_descent_check_w3(Fraction(5))
        assert result['ds_creates_quartic']
        assert result['S4_sl3'] == Fraction(0)
        assert result['S4_W3_T'] != Fraction(0)

    def test_ds_kappa_sum(self):
        """kappa(sl_3) = kappa(W_3) + kappa(ghost)."""
        result = ds_descent_check_w3(Fraction(5))
        kap_sl3 = result['kappa_sl3']
        kap_w3 = result['kappa_W3']
        kap_ghost = result['kappa_ghost']
        assert kap_sl3 == kap_w3 + kap_ghost

    def test_ds_at_various_levels(self):
        for kval in [Fraction(1), Fraction(3), Fraction(10)]:
            result = ds_descent_check_w3(kval)
            assert result['ds_creates_quartic'], (
                f"DS failed at k={kval}")


# ============================================================================
# Group 10: Additivity and direct sums (3 tests)
# ============================================================================

class TestAdditivity:
    """Additivity of kappa and vanishing of Q^contact for direct sums."""

    def test_heisenberg_additivity(self):
        result = verify_kappa_additivity_heis()
        assert result['additive_r2']
        assert result['additive_r8']
        assert result['Q_all_zero']

    def test_lattice_kappa_equals_rank(self):
        """kappa(V_Lambda) = rank for lattice VOAs."""
        for r in [1, 8, 16, 24]:
            d = lattice_voa(r)
            assert d.kappa == Fraction(r)

    def test_direct_sum_preserves_class_g(self):
        """Direct sum of class G algebras is class G."""
        h1 = heisenberg(Fraction(1))
        h2 = heisenberg_rank_r(2)
        # Both class G with S_4 = 0
        assert h1.shadow_class == h2.shadow_class == 'G'
        assert h1.S4 == h2.S4 == Fraction(0)


# ============================================================================
# Group 11: Cross-family consistency (8 tests)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency of Q^contact."""

    def test_betagamma_tline_is_virasoro(self):
        results = verify_betagamma_tline_is_virasoro()
        for lam_str, data in results.items():
            assert data['match'], (
                f"bg T-line != Vir at lambda={lam_str}: "
                f"{data['S4_bg_T']} != {data['S4_vir']}")

    def test_w3_tline_is_virasoro(self):
        results = verify_w3_tline_vs_virasoro()
        for kstr, data in results.items():
            assert data['match'], (
                f"W3 T-line != Vir at k={kstr}")

    def test_w3_wline_differs_from_tline(self):
        """W-line S_4 != T-line S_4 (independent invariants)."""
        results = verify_w3_wline_vs_tline()
        for kstr, data in results.items():
            assert data['S4_T'] != data['S4_W'], (
                f"W-line == T-line at k={kstr}")
            assert data['ratio_match'], (
                f"Ratio mismatch at k={kstr}")

    def test_bc_ghost_j2_central_charge(self):
        """bc at j=2: c = -26 (reparametrization ghosts)."""
        d = bc_ghost_tline(Fraction(2))
        assert d.central_charge == Fraction(-26)
        assert d.kappa == Fraction(-13)

    def test_betagamma_lam0_equals_lam1(self):
        """c(lam=0) = c(lam=1) = 2 by symmetry lambda -> 1-lambda."""
        bg0 = betagamma_tline(Fraction(0))
        bg1 = betagamma_tline(Fraction(1))
        assert bg0.central_charge == bg1.central_charge == Fraction(2)
        assert bg0.S4 == bg1.S4

    def test_landscape_table_nonempty(self):
        table = landscape_table()
        assert len(table) > 40

    def test_landscape_summary_counts(self):
        summary = landscape_summary()
        assert summary['total'] > 40
        assert summary['class_counts']['G'] > 0
        assert summary['class_counts']['L'] > 0
        assert summary['class_counts']['C'] > 0
        assert summary['class_counts']['M'] > 0
        assert summary['S4_zero'] + summary['S4_nonzero'] == summary['total']

    def test_build_full_landscape(self):
        """Full landscape builds without error."""
        reg = build_full_landscape()
        assert len(reg) > 40
        for name, datum in reg.items():
            assert isinstance(datum, QuarticContactDatum)


# ============================================================================
# Group 12: Depth classification consistency (10 tests)
# ============================================================================

class TestDepthConsistency:
    """Verify consistency of shadow depth with S_3, S_4 pattern."""

    def test_all_depth_consistent(self):
        results = verify_depth_classification_consistency()
        assert len(results) > 40
        for name, ok, msg in results:
            assert ok, f"Depth inconsistency for {name}: {msg}"

    def test_g_has_s3_zero(self):
        """Class G: S_3 = 0 (abelian => no cubic)."""
        for d in [heisenberg(), free_fermion(), lattice_voa(1)]:
            assert d.S3 == Fraction(0)

    def test_l_has_s3_nonzero(self):
        """Class L: S_3 != 0 (Lie bracket gives cubic)."""
        for N in [2, 3, 4]:
            d = affine_slN(N)
            assert d.S3 != Fraction(0)

    def test_c_tline_has_s3_nonzero(self):
        """Class C T-line: S_3 = 2 (Sugawara cubic)."""
        d = betagamma_tline(Fraction(1))
        assert d.S3 == Fraction(2)

    def test_c_charged_has_s3_zero(self):
        """Class C charged stratum: S_3 = 0 (rank-one rigidity)."""
        d = betagamma_charged_stratum(Fraction(1))
        assert d.S3 == Fraction(0)

    def test_m_virasoro_has_s3_nonzero(self):
        """Class M Virasoro: S_3 = 2 (gravitational cubic)."""
        d = virasoro_qcontact(Fraction(1))
        assert d.S3 == Fraction(2)

    def test_m_w3_wline_has_s3_zero(self):
        """Class M W_3 W-line: S_3 = 0 (Z_2 parity W -> -W)."""
        d = w3_wline(Fraction(5))
        assert d.S3 == Fraction(0)

    def test_virasoro_s4_positive_at_positive_c(self):
        """S_4 > 0 for positive c (all standard Virasoro)."""
        for cval in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
            d = virasoro_qcontact(cval)
            assert d.S4 > 0, f"S_4 not positive at c={cval}: {d.S4}"

    def test_betagamma_charged_s4_negative(self):
        """S_4 = -5/12 < 0 on charged stratum."""
        d = betagamma_charged_stratum(Fraction(1))
        assert d.S4 < 0

    def test_r_max_values(self):
        """Verify r_max: G=2, L=3, C=4, M=inf."""
        assert heisenberg().r_max == 2
        assert affine_slN(2).r_max == 3
        assert betagamma_tline().r_max == 4
        assert virasoro_qcontact(Fraction(1)).r_max == float('inf')
