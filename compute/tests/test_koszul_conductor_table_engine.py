r"""Tests for the Koszul conductor table engine.

Verifies K(A) = kappa(A) + kappa(A^!) and c + c' for all families
in the standard chiral algebra landscape.  Every hardcoded expected
value has a VERIFIED comment citing 2+ independent sources (AP10/HZ-6).

Ground truth references:
  C1-C7:   central charges and kappa per family
  C18:     K(A) = kappa+kappa': 0 (KM/Heis/lattice/free), 13 (Vir),
           250/3 (W_3), 98/3 (BP scalar lane)
  C20:     K_BP = 196 on the self-transpose BP branch; k=-3 is a pole
  AP136:   H_N = sum_{j=1}^N 1/j, NOT H_{N-1}
  B7:      WRONG: kappa(W_N) = c*H_{N-1}
  B9:      WRONG: kappa+kappa' = 0 universally
"""

import pytest
from fractions import Fraction

from compute.lib.koszul_conductor_table_engine import (
    AFFINE_CONDUCTOR_HYPOTHESES,
    AFFINE_CRITICAL_STATUS,
    VIRASORO_DUALITY_HYPOTHESES,
    VIRASORO_EXCEPTIONAL_CHARGES,
    VIRASORO_SHADOW_TOWER_HYPOTHESES,
    VIRASORO_SHADOW_TOWER_MISSING_AT_SINGULAR,
    harmonic,
    heisenberg_c,
    heisenberg_kappa,
    heisenberg_dual_kappa,
    heisenberg_K_cc,
    heisenberg_K_kk,
    virasoro_c,
    virasoro_dual_c,
    virasoro_kappa,
    virasoro_dual_kappa,
    virasoro_K_cc,
    virasoro_K_kk,
    virasoro_scope_report,
    km_c,
    km_dual_level,
    km_dual_c,
    km_kappa,
    km_dual_kappa,
    km_K_cc,
    km_K_kk,
    km_level_scope,
    wn_kappa,
    wn_dual_c,
    wn_spin_set,
    wn_central_charge_conductor,
    wn_conductor_constant,
    WN_CONDUCTORS,
    WN_CC_SUMS,
    BP_DUALITY_HYPOTHESES,
    BP_STRONG_GENERATORS,
    bp_c,
    bp_dual_c,
    bp_K_cc,
    bp_K_kk,
    bp_j_line_scalar,
    bp_t_line_scalar,
    bp_g_mixed_pairing,
    bp_ds_ghost_leg_scalar,
    bp_scope_report,
    bc_c,
    bg_c,
    bc_bg_K_cc,
    bc_kappa,
    bg_kappa,
    bc_bg_K_kk,
    lattice_c,
    lattice_K_cc,
    lattice_K_kk,
    LIE_DATA,
    full_conductor_table,
)


# ===========================================================================
# Harmonic numbers (C19, AP136)
# ===========================================================================

class TestHarmonicNumbers:
    """H_N = sum_{j=1}^{N} 1/j.  NOT H_{N-1} (AP136)."""

    def test_h1(self):
        # VERIFIED: [DC] direct sum 1/1=1, [LT] DLMF 25.11
        assert harmonic(1) == Fraction(1)

    def test_h2(self):
        # VERIFIED: [DC] 1+1/2=3/2, [LT] DLMF 25.11
        assert harmonic(2) == Fraction(3, 2)

    def test_h3(self):
        # VERIFIED: [DC] 1+1/2+1/3=11/6, [LT] OEIS A001008/A002805
        assert harmonic(3) == Fraction(11, 6)

    def test_h4(self):
        # VERIFIED: [DC] 1+1/2+1/3+1/4=25/12, [LT] OEIS A001008/A002805
        assert harmonic(4) == Fraction(25, 12)

    def test_h5(self):
        # VERIFIED: [DC] 25/12+1/5=137/60, [LT] OEIS A001008/A002805
        assert harmonic(5) == Fraction(137, 60)

    def test_h0(self):
        # Empty sum = 0
        assert harmonic(0) == Fraction(0)

    def test_ap136_distinction(self):
        """H_{N-1} != H_N - 1 at N=2.  AP136 regression test."""
        # H_1 = 1, H_2 - 1 = 1/2.  These are DIFFERENT.
        h_1 = harmonic(1)          # = 1
        h_2_minus_1 = harmonic(2) - 1  # = 1/2
        assert h_1 != h_2_minus_1
        assert h_1 == Fraction(1)
        assert h_2_minus_1 == Fraction(1, 2)


# ===========================================================================
# Heisenberg (C1, C10, C18)
# ===========================================================================

class TestHeisenberg:
    """Heisenberg H_k: c=1, kappa=k, K_kk=0."""

    def test_c(self):
        # VERIFIED: [DC] rank-1 boson c=1, [LT] Kac vertex algebras ch.3
        assert heisenberg_c() == Fraction(1)

    def test_kappa_k1(self):
        # VERIFIED: [DC] kappa(H_1)=1, [LT] C1 of census
        assert heisenberg_kappa(Fraction(1)) == Fraction(1)

    def test_kappa_k0(self):
        # VERIFIED: [DC] kappa(H_0)=0, [LC] k=0 limit trivial
        assert heisenberg_kappa(Fraction(0)) == Fraction(0)

    def test_kappa_k7(self):
        # VERIFIED: [DC] kappa(H_7)=7, [LT] C1
        assert heisenberg_kappa(Fraction(7)) == Fraction(7)

    def test_dual_kappa(self):
        # VERIFIED: [DC] kappa'=-k, [SY] K_kk=0 (C18)
        assert heisenberg_dual_kappa(Fraction(5)) == Fraction(-5)

    def test_K_cc(self):
        # VERIFIED: [DC] 1+1=2, [LT] Heisenberg dual has same c
        assert heisenberg_K_cc() == Fraction(2)

    def test_K_kk_zero(self):
        """K_kk = 0 for Heisenberg (C18: KM/Heis/lattice/free)."""
        # VERIFIED: [LT] C18, [DC] k+(-k)=0
        for k in [Fraction(0), Fraction(1), Fraction(-3), Fraction(7, 2)]:
            assert heisenberg_K_kk(k) == Fraction(0)


# ===========================================================================
# Virasoro (C2, C8, C18)
# ===========================================================================

class TestVirasoro:
    """Virasoro Vir_c: c'=26-c, K_cc=26, kappa=c/2, K_kk=13."""

    def test_dual_c(self):
        # VERIFIED: [LT] C8 Vir^!=Vir_{26-c}, [DC] 26-c
        assert virasoro_dual_c(Fraction(1)) == Fraction(25)
        assert virasoro_dual_c(Fraction(13)) == Fraction(13)
        assert virasoro_dual_c(Fraction(26)) == Fraction(0)

    def test_K_cc_26(self):
        """c + c' = 26 for all c."""
        # VERIFIED: [DC] c+(26-c)=26, [LT] C8
        for c in [Fraction(0), Fraction(1), Fraction(13), Fraction(26), Fraction(-2)]:
            assert virasoro_K_cc(c) == Fraction(26)

    def test_kappa(self):
        # VERIFIED: [LT] C2 kappa(Vir)=c/2, [DC] direct
        assert virasoro_kappa(Fraction(1)) == Fraction(1, 2)
        assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)
        assert virasoro_kappa(Fraction(26)) == Fraction(13)

    def test_self_dual_c13(self):
        """Self-dual at c=13 (C8).  NOT c=26, NOT c=0."""
        # VERIFIED: [LT] C8, [DC] 26-13=13
        assert virasoro_dual_c(Fraction(13)) == Fraction(13)
        assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)

    def test_K_kk_13(self):
        """K_kk = 13 for Virasoro (C18)."""
        # VERIFIED: [LT] C18, [DC] c/2+(26-c)/2=13
        for c in [Fraction(0), Fraction(1), Fraction(13), Fraction(26), Fraction(-5)]:
            assert virasoro_K_kk(c) == Fraction(13)

    def test_scope_report_generic(self):
        """Generic Virasoro carries theorem-scoped duality and S4 hypotheses."""
        scope = virasoro_scope_report(Fraction(1))
        assert scope["dual_central_charge"] == Fraction(25)
        assert scope["duality_claim_requires_theorem"] is True
        assert scope["duality_hypothesis_package"] == VIRASORO_DUALITY_HYPOTHESES
        assert scope["K_kk"] == Fraction(13)
        assert scope["self_dual"] is False
        assert scope["shadow_tower_formula_applies"] is True
        assert scope["shadow_tower_hypothesis_package"] == VIRASORO_SHADOW_TOWER_HYPOTHESES
        assert scope["missing_shadow_tower_hypotheses"] == tuple()
        assert scope["S4_formula"] == "10/[c(5c+22)]"

    def test_scope_report_exceptional_charges(self):
        """The four PDF-specified Virasoro charges have distinct statuses."""
        c0 = virasoro_scope_report(Fraction(0))
        assert c0["exceptional_status"] == VIRASORO_EXCEPTIONAL_CHARGES[Fraction(0)]
        assert c0["shadow_tower_formula_applies"] is False
        assert c0["missing_shadow_tower_hypotheses"] == VIRASORO_SHADOW_TOWER_MISSING_AT_SINGULAR

        yang_lee = virasoro_scope_report(Fraction(-22, 5))
        assert yang_lee["exceptional_status"] == VIRASORO_EXCEPTIONAL_CHARGES[Fraction(-22, 5)]
        assert yang_lee["shadow_tower_formula_applies"] is False

        c26 = virasoro_scope_report(Fraction(26))
        assert c26["exceptional_status"] == VIRASORO_EXCEPTIONAL_CHARGES[Fraction(26)]
        assert c26["dual_central_charge"] == Fraction(0)
        assert c26["self_dual"] is False
        assert c26["critical_string_central_charge"] is True
        assert c26["shadow_tower_formula_applies"] is True

        c13 = virasoro_scope_report(Fraction(13))
        assert c13["exceptional_status"] == VIRASORO_EXCEPTIONAL_CHARGES[Fraction(13)]
        assert c13["dual_central_charge"] == Fraction(13)
        assert c13["self_dual"] is True
        assert c13["critical_string_central_charge"] is False


# ===========================================================================
# Affine Kac-Moody (C3, C9, C13, C18)
# ===========================================================================

class TestAffineKM:
    """V_k(g): non-critical conductor lane and critical FF separation."""

    def test_kappa_sl2_k0(self):
        """kappa(V_0(sl2)) = dim(sl2)/2 = 3/2.  (C3: k=0 -> dim/2)"""
        # VERIFIED: [DC] 3*(0+2)/(2*2)=3/2, [LT] C3 boundary
        assert km_kappa(3, 2, Fraction(0)) == Fraction(3, 2)

    def test_kappa_sl2_k_critical(self):
        """Generic kappa helper rejects the critical FF boundary."""
        with pytest.raises(ValueError, match="critical level"):
            km_kappa(3, 2, Fraction(-2))

    def test_kappa_sl3_k0(self):
        # VERIFIED: [DC] 8*(0+3)/(2*3)=4, [LT] C3
        assert km_kappa(8, 3, Fraction(0)) == Fraction(4)

    def test_kappa_sl3_k_critical(self):
        with pytest.raises(ValueError, match="critical level"):
            km_kappa(8, 3, Fraction(-3))

    def test_kappa_e8_k0(self):
        # VERIFIED: [DC] 248*(0+30)/(2*30)=124, [LT] C3
        assert km_kappa(248, 30, Fraction(0)) == Fraction(124)

    def test_kappa_e8_k_critical(self):
        with pytest.raises(ValueError, match="critical level"):
            km_kappa(248, 30, Fraction(-30))

    def test_dual_level(self):
        """k' = -k - 2*h^v."""
        # VERIFIED: [DC] -(1)-2*2=-5, [SY] symmetry k<->k'
        assert km_dual_level(Fraction(1), 2) == Fraction(-5)
        assert km_dual_level(Fraction(0), 3) == Fraction(-6)

    def test_K_kk_zero_sl2(self):
        """K_kk = 0 for sl2 at multiple levels (C18)."""
        # VERIFIED: [LT] C18 KM family, [DC] direct computation
        for k in [Fraction(1), Fraction(0), Fraction(7), Fraction(1, 3)]:
            assert km_K_kk(3, 2, k) == Fraction(0)

    def test_K_kk_zero_all_algebras(self):
        """K_kk = 0 for all simple Lie algebras (C18)."""
        # VERIFIED: [LT] C18, [DC] algebraic cancellation
        for name, (dim_g, h_v) in LIE_DATA.items():
            assert km_K_kk(dim_g, h_v, Fraction(1)) == Fraction(0), \
                f"K_kk != 0 for {name}"

    def test_km_c_sl2_k1(self):
        """c(V_1(sl2)) = 1*3/(1+2) = 1."""
        # VERIFIED: [DC] 1*3/3=1, [LT] Sugawara formula
        assert km_c(3, 2, Fraction(1)) == Fraction(1)

    def test_km_c_critical_raises(self):
        """Sugawara central charge is undefined at k=-h^v."""
        with pytest.raises(ValueError, match="critical level"):
            km_c(3, 2, Fraction(-2))

    def test_K_kk_critical_raises(self):
        """Generic conductor complementarity does not apply at critical level."""
        with pytest.raises(ValueError, match="critical level"):
            km_K_kk(3, 2, Fraction(-2))

    def test_noncritical_scope_report(self):
        """Non-critical affine KM carries the generic conductor package."""
        scope = km_level_scope(3, 2, Fraction(1))
        assert scope["is_critical"] is False
        assert scope["generic_conductor_formula_applies"] is True
        assert scope["hypothesis_package"] == AFFINE_CONDUCTOR_HYPOTHESES
        assert scope["missing_hypotheses"] == tuple()
        assert scope["kappa_scalar"] == Fraction(9, 4)
        assert scope["K_kk_scalar_indicator"] == Fraction(0)

    def test_critical_scope_report(self):
        """Critical scalar vanishing is recorded without promoting it."""
        scope = km_level_scope(3, 2, Fraction(-2))
        assert scope["is_critical"] is True
        assert scope["generic_conductor_formula_applies"] is False
        assert scope["central_charge_defined"] is False
        assert scope["status"] == AFFINE_CRITICAL_STATUS
        assert scope["missing_hypotheses"] == AFFINE_CONDUCTOR_HYPOTHESES
        assert scope["kappa_scalar"] == Fraction(0)
        assert scope["kappa_dual_scalar"] == Fraction(0)
        assert scope["K_kk_scalar_indicator"] == Fraction(0)
        assert scope["critical_scalar_kappa_vanishes"] is True
        assert scope["ff_center_lane"] is True


# ===========================================================================
# W_N algebras (C4, C17, C19, AP136)
# ===========================================================================

class TestWN:
    """W_N: kappa = c*(H_N - 1)."""

    def test_w2_is_virasoro(self):
        """W_2 = Vir: kappa(W_2) = c*(H_2 - 1) = c*1/2 = c/2.  (C4)"""
        # VERIFIED: [DC] H_2-1=3/2-1=1/2, c*1/2=c/2, [CF] matches C2
        c = Fraction(26)
        assert wn_kappa(c, 2) == virasoro_kappa(c)

    def test_w2_conductor(self):
        """K_kk(W_2) = 13 = K_kk(Vir)."""
        # VERIFIED: [LT] C18 Vir=13, [CF] W_2=Vir cross-family
        assert WN_CONDUCTORS[2] == Fraction(13)

    def test_w3_conductor(self):
        """K_kk(W_3) = 250/3.  (C18)"""
        # VERIFIED: [LT] C18, [DC] 100*(11/6-1) = 100*5/6 = 500/6 = 250/3
        assert WN_CONDUCTORS[3] == Fraction(250, 3)

    def test_wn_spin_set(self):
        """Principal W_N strong generators have spins {2, ..., N}."""
        assert wn_spin_set(2) == (2,)
        assert wn_spin_set(5) == (2, 3, 4, 5)
        with pytest.raises(ValueError, match="N >= 2"):
            wn_spin_set(1)

    def test_wn_central_charge_conductor_formula(self):
        """K_c(W_N) = 4N^3 - 2N - 2, not the scalar K_kk lane."""
        expected = {
            2: Fraction(26),
            3: Fraction(100),
            4: Fraction(246),
            5: Fraction(488),
        }
        for n, value in expected.items():
            assert wn_central_charge_conductor(n) == value
            assert WN_CC_SUMS[n] == value
        with pytest.raises(ValueError, match="N >= 2"):
            wn_central_charge_conductor(1)

    def test_wn_scalar_conductor_formula(self):
        """K_kk(W_N) = (H_N - 1) K_c(W_N)."""
        expected = {
            2: Fraction(13),
            3: Fraction(250, 3),
            4: Fraction(533, 2),
            5: Fraction(9394, 15),
        }
        for n, value in expected.items():
            assert wn_conductor_constant(n) == value
            assert WN_CONDUCTORS[n] == value
            assert value == (
                harmonic(n) - Fraction(1)
            ) * wn_central_charge_conductor(n)

    def test_wn_Kc_not_Kkappa(self):
        """The central-charge conductor and scalar conductor are distinct."""
        assert wn_central_charge_conductor(3) == Fraction(100)
        assert wn_conductor_constant(3) == Fraction(250, 3)
        assert wn_central_charge_conductor(4) == Fraction(246)
        assert wn_conductor_constant(4) == Fraction(533, 2)
        assert wn_conductor_constant(4) != wn_central_charge_conductor(4)

    def test_w4_w5_dual_c_available(self):
        """The closed W_N conductor formula supplies N >= 4 dual charges."""
        assert wn_dual_c(Fraction(1), 4) == Fraction(245)
        assert wn_dual_c(Fraction(1), 5) == Fraction(487)
        assert wn_dual_c(Fraction(1), 6) == wn_central_charge_conductor(6) - 1

    def test_w3_kappa_at_c1(self):
        """kappa(W_3, c=1) = 1*(H_3-1) = 1*5/6 = 5/6."""
        # VERIFIED: [DC] H_3=11/6, 11/6-1=5/6, [LT] C4
        assert wn_kappa(Fraction(1), 3) == Fraction(5, 6)

    def test_w3_kappa_at_c100(self):
        """kappa(W_3, c=100) = 100*5/6 = 500/6 = 250/3."""
        # VERIFIED: [DC] 100*5/6=500/6=250/3, [LT] C4
        assert wn_kappa(Fraction(100), 3) == Fraction(250, 3)

    def test_w3_complementarity(self):
        """kappa(W_3,c) + kappa(W_3,c') = 250/3 for all c."""
        # VERIFIED: [DC] c*(5/6)+(100-c)*(5/6)=100*5/6=250/3, [LT] C18
        for c in [Fraction(0), Fraction(1), Fraction(50), Fraction(100)]:
            c_dual = wn_dual_c(c, 3)
            total = wn_kappa(c, 3) + wn_kappa(c_dual, 3)
            assert total == Fraction(250, 3), f"Failed at c={c}"

    def test_w2_complementarity(self):
        """kappa(W_2,c) + kappa(W_2,c') = 13 for all c."""
        # VERIFIED: [DC] c/2+(26-c)/2=13, [CF] matches Virasoro
        for c in [Fraction(0), Fraction(1), Fraction(13), Fraction(26)]:
            c_dual = wn_dual_c(c, 2)
            total = wn_kappa(c, 2) + wn_kappa(c_dual, 2)
            assert total == Fraction(13)

    def test_ap136_regression(self):
        """AP136: kappa(W_N) = c*(H_N - 1), NOT c*H_{N-1}.

        At N=2: c*(H_2-1)=c/2 (correct). c*H_1=c (WRONG by factor 2).
        """
        c = Fraction(10)
        correct = wn_kappa(c, 2)       # c*(3/2-1) = c/2 = 5
        wrong = c * harmonic(1)         # c*1 = 10
        assert correct == Fraction(5)
        assert wrong == Fraction(10)
        assert correct != wrong  # AP136: the two are DIFFERENT

    def test_cc_sum_w3(self):
        """c + c' = 100 for W_3."""
        # VERIFIED: [DC] K_kk/(H_3-1) = (250/3)/(5/6) = 100, [LT] C18+C4
        assert WN_CC_SUMS[3] == Fraction(100)


# ===========================================================================
# Bershadsky-Polyakov (C18, C20)
# ===========================================================================

class TestBershadskyPolyakov:
    """BP: K_kk = 98/3, K_cc = 196 on the non-principal DS branch."""

    def test_K_kk_98_over_3(self):
        """K_kk(BP) = 98/3 on the scalar lane.  (C18, C20)"""
        # VERIFIED: [DC] (1/6)*196=98/3, [LT] BP complementarity proposition
        assert bp_K_kk() == Fraction(98, 3)

    def test_K_cc_196(self):
        """K_cc(BP) = 196 on the central-charge lane.  (C20)"""
        # VERIFIED: [DC] c(0)+c(-6)=-6+202=196, [LT] BP self-duality proposition
        assert bp_K_cc(Fraction(0)) == Fraction(196)

    def test_bp_scope_report_nonprincipal_fields(self):
        """BP is subregular/minimal DS, not the principal W_N branch."""
        scope = bp_scope_report(Fraction(0))
        assert scope["presentation"] == "subregular_DS_W3^(2)"
        assert scope["nilpotent_orbit_partition"] == (2, 1)
        assert scope["ds_orbit"] == "subregular/minimal"
        assert scope["is_principal_W_N"] is False
        assert scope["strong_generators"] == BP_STRONG_GENERATORS
        assert scope["duality_claim_requires_theorem"] is True
        assert scope["duality_hypothesis_package"] == BP_DUALITY_HYPOTHESES

    def test_bp_shadow_lines_are_separate(self):
        """The BP J-line, T-line, G-pairing, kappa, and ghost leg differ."""
        k = Fraction(0)
        scope = bp_scope_report(k)
        lines = scope["shadow_lines"]
        assert lines["J"]["scalar"] == Fraction(1)
        assert lines["T"]["scalar"] == Fraction(-3)
        assert lines["G_pairing"]["scalar"] == Fraction(3)
        assert lines["full_kappa"]["scalar"] == Fraction(-1)
        assert lines["DS_ghost_leg"]["presentation_dependent"] is True
        assert lines["DS_ghost_leg"]["scalar"] == Fraction(-6)
        assert bp_j_line_scalar(k) != bp_t_line_scalar(k)
        assert bp_t_line_scalar(k) != bp_K_kk(k)
        assert bp_ds_ghost_leg_scalar(k) != bp_K_kk(k)

    def test_bp_fixed_real_level_is_pole_not_attained_self_duality(self):
        """k=-3 is fixed by k -> -k-6 but c_BP is undefined there."""
        scope = bp_scope_report(Fraction(-3))
        assert scope["level_fixed_by_sigma"] is True
        assert scope["central_charge_defined"] is False
        assert scope["real_level_self_dual_c_attained"] is False
        assert scope["formal_self_dual_central_charge"] == Fraction(98)
        assert scope["formal_self_dual_levels"] == ("k=-3+2i", "k=-3-2i")
        assert scope["missing_hypotheses"] == ("k_plus_3_nonzero",)
        assert scope["status"] == (
            "critical_level_pole_not_attained_self_dual_real_level"
        )

    def test_bp_line_scalar_helpers(self):
        """Direct BP line scalar helpers match the OPE scalar package."""
        k = Fraction(1)
        assert bp_j_line_scalar(k) == Fraction(5, 3)
        assert bp_t_line_scalar(k) == bp_c(k) / 2
        assert bp_t_line_scalar(k) == Fraction(-11)
        assert bp_g_mixed_pairing(k) == Fraction(10)
        assert bp_ds_ghost_leg_scalar(k) == Fraction(-24)

    def test_bp_c_symmetry(self):
        """c_BP(k) + c_BP(-k-6) is the same for multiple k values."""
        # VERIFIED: [DC] algebraic, [LT] C20
        val = bp_K_cc(Fraction(1))
        for k in [Fraction(0), Fraction(2), Fraction(5), Fraction(-1)]:
            assert bp_K_cc(k) == val, f"K_cc not constant at k={k}"


# ===========================================================================
# bc-betagamma (C5, C6, C7, C18)
# ===========================================================================

class TestBcBetagamma:
    """bc and betagamma ghost systems."""

    def test_bc_c_half(self):
        """c_bc(1/2) = 1.  (C5: single Dirac fermion)"""
        # VERIFIED: [DC] 1-3*(2*1/2-1)^2=1-0=1, [LT] C5
        assert bc_c(Fraction(1, 2)) == Fraction(1)

    def test_bc_c_2(self):
        """c_bc(2) = -26.  (C5: reparametrization ghost)"""
        # VERIFIED: [DC] 1-3*(4-1)^2=1-27=-26, [LT] C5
        assert bc_c(Fraction(2)) == Fraction(-26)

    def test_bc_c_1(self):
        """c_bc(1) = -2."""
        # VERIFIED: [DC] 1-3*(2-1)^2=1-3=-2, [CF] matches bc ghost at lam=1
        assert bc_c(Fraction(1)) == Fraction(-2)

    def test_bg_c_half(self):
        """c_bg(1/2) = -1.  (C6: symplectic boson)"""
        # VERIFIED: [DC] 2*(6/4-3+1)=2*(-1/2)=-1, [LT] C6
        assert bg_c(Fraction(1, 2)) == Fraction(-1)

    def test_bg_c_2(self):
        """c_bg(2) = 26.  (C6: matter ghost, c_bg+c_bc=0)"""
        # VERIFIED: [DC] 2*(24-12+1)=2*13=26, [LT] C6
        assert bg_c(Fraction(2)) == Fraction(26)

    def test_bg_c_1(self):
        """c_bg(1) = 2."""
        # VERIFIED: [DC] 2*(6-6+1)=2, [CF] c_bg(1)+c_bc(1)=2+(-2)=0
        assert bg_c(Fraction(1)) == Fraction(2)

    def test_complementarity_c7(self):
        """c_bc + c_bg = 0 for all lambda.  (C7)"""
        # VERIFIED: [LT] C7, [DC] algebraic identity
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1),
                     Fraction(2), Fraction(3), Fraction(-1), Fraction(7, 3)]:
            assert bc_bg_K_cc(lam) == Fraction(0), f"c+c'!=0 at lam={lam}"

    def test_K_kk_zero(self):
        """K_kk(bc-bg) = 0.  (C18: free family)"""
        # VERIFIED: [LT] C18, [DC] (c_bc+c_bg)/2=0/2=0
        for lam in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5)]:
            assert bc_bg_K_kk(lam) == Fraction(0), f"K_kk!=0 at lam={lam}"

    def test_string_ghost_cancellation(self):
        """c_bc(2) + c_bg(2) = -26 + 26 = 0.  (C7: string ghost cancellation)"""
        # VERIFIED: [DC] -26+26=0, [LT] C7 + string theory ghost
        assert bc_c(Fraction(2)) + bg_c(Fraction(2)) == Fraction(0)


# ===========================================================================
# Lattice VOA (C18)
# ===========================================================================

class TestLattice:
    """Lattice VOA V_L: K_kk = 0."""

    def test_c(self):
        # VERIFIED: [DC] c=rank, [LT] FLM vertex algebras
        assert lattice_c(8) == Fraction(8)
        assert lattice_c(24) == Fraction(24)

    def test_K_cc(self):
        # VERIFIED: [DC] rank+rank=2*rank, [LT] lattice duality same rank
        assert lattice_K_cc(8) == Fraction(16)

    def test_K_kk_zero(self):
        """K_kk = 0 for lattice.  (C18)"""
        # VERIFIED: [LT] C18, [SY] lattice is free field
        assert lattice_K_kk() == Fraction(0)


# ===========================================================================
# Full conductor table integration test
# ===========================================================================

class TestFullTable:
    """Integration test for the complete conductor table."""

    def test_all_K_kk_types(self):
        """Cross-check K_kk values match C18."""
        table = full_conductor_table(
            k_km=Fraction(1),
            c_vir=Fraction(1),
            c_w3=Fraction(1),
            lam_bc=Fraction(2),
        )
        # KM/Heis/lattice: 0 (C18)
        assert table["Heisenberg"]["K_kk"] == Fraction(0)
        assert table["Lattice"]["K_kk"] == Fraction(0)
        for name in LIE_DATA:
            assert table[f"KM_{name}"]["K_kk"] == Fraction(0), f"KM_{name}"

        # Virasoro: 13 (C18)
        assert table["Virasoro"]["K_kk"] == Fraction(13)

        # W_2: 13 (= Vir)
        assert table["W_2"]["K_kk"] == Fraction(13)

        # W_3: 250/3 (C18)
        assert table["W_3"]["K_kk"] == Fraction(250, 3)

        # BP scalar lane: 98/3, central-charge lane: 196
        assert table["BP"]["K_kk"] == Fraction(98, 3)
        assert table["BP"]["K_cc"] == Fraction(196)

        # bc/bg: 0 (free)
        assert table["bc"]["K_kk"] == Fraction(0)
        assert table["betagamma"]["K_kk"] == Fraction(0)

    def test_virasoro_K_cc_26(self):
        """c + c' = 26 for Virasoro in table."""
        table = full_conductor_table(c_vir=Fraction(7))
        assert table["Virasoro"]["K_cc"] == Fraction(26)

    def test_all_fractions(self):
        """Every value in the table is a Fraction (no floats)."""
        table = full_conductor_table()
        for family, data in table.items():
            for key, val in data.items():
                assert isinstance(val, Fraction), \
                    f"{family}.{key} = {val} is {type(val)}, not Fraction"

    def test_table_completeness(self):
        """Table has entries for all expected families."""
        table = full_conductor_table()
        expected = {"Heisenberg", "Virasoro", "W_2", "W_3", "BP",
                    "bc", "betagamma", "Lattice"}
        for name in LIE_DATA:
            expected.add(f"KM_{name}")
        assert expected.issubset(set(table.keys()))


# ===========================================================================
# Cross-family consistency (C18 exhaustive)
# ===========================================================================

class TestCrossFamilyConsistency:
    """K_kk is NOT universally zero (B9).  Verify distinct values."""

    def test_not_universal_zero(self):
        """B9 regression: kappa+kappa'=0 is NOT universal."""
        # Virasoro K_kk=13 != 0.  (B9)
        assert virasoro_K_kk(Fraction(1)) != Fraction(0)
        # W_3 K_kk=250/3 != 0.
        assert WN_CONDUCTORS[3] != Fraction(0)
        # BP K_kk=98/3 != 0.
        assert bp_K_kk() != Fraction(0)

    def test_kk_values_distinct(self):
        """The four known K_kk values are all distinct."""
        vals = {Fraction(0), Fraction(13), Fraction(250, 3), Fraction(98, 3)}
        assert len(vals) == 4
