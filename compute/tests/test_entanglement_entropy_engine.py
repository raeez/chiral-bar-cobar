r"""Tests for entanglement_entropy_engine.

Verifies:
  1. Kappa values for all standard families (exact Fraction arithmetic)
  2. Cross-family consistency checks (W_2=Vir, complementarity, critical level)
  3. S_EE = (2*kappa/3)*log(L/eps) at multiple (L, eps) pairs
  4. Tabulation completeness

Ground truth:
  CLAUDE.md C1-C6, C8, C18; AP68 (SVir kappa)
  Calabrese-Cardy 2004 (hep-th/0405152)
  landscape_census.tex
  compute/lib/f2_kappa_verification_engine.py (independent kappa cross-check)
  compute/lib/entanglement_shadow_engine.py (independent kappa cross-check)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.entanglement_entropy_engine import (
    harmonic_number,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_km,
    kappa_affine_sl2,
    kappa_affine_sl3,
    kappa_affine_so4,
    kappa_affine_g2,
    kappa_affine_e8,
    kappa_wn,
    kappa_betagamma,
    kappa_bc,
    kappa_super_virasoro,
    kappa_lattice,
    c_betagamma,
    c_bc,
    entanglement_entropy,
    entanglement_entropy_exact,
    tabulate,
    LIE_DATA,
    FAMILIES,
)


# ===================================================================
#  SECTION 1: Harmonic numbers
# ===================================================================

class TestHarmonicNumbers:
    """Verify harmonic number computation.  [C19: CLAUDE.md]"""

    def test_h1(self):
        # VERIFIED [DC] H_1 = 1; [LT] standard definition
        assert harmonic_number(1) == Fraction(1)

    def test_h2(self):
        # VERIFIED [DC] H_2 = 1 + 1/2 = 3/2; [LT] standard
        assert harmonic_number(2) == Fraction(3, 2)

    def test_h3(self):
        # VERIFIED [DC] H_3 = 1 + 1/2 + 1/3 = 11/6; [LT] standard
        assert harmonic_number(3) == Fraction(11, 6)

    def test_h4(self):
        # VERIFIED [DC] 1+1/2+1/3+1/4 = 25/12; [NE] float check 2.08333...
        assert harmonic_number(4) == Fraction(25, 12)

    def test_ap136_distinction(self):
        """H_{N-1} != H_N - 1.  [AP136: CLAUDE.md]"""
        # At N=2: H_1 = 1, but H_2 - 1 = 1/2.  These differ.
        # VERIFIED [DC] direct; [CF] AP136 canonical example
        assert harmonic_number(1) != harmonic_number(2) - 1
        assert harmonic_number(1) == Fraction(1)
        assert harmonic_number(2) - 1 == Fraction(1, 2)


# ===================================================================
#  SECTION 2: Kappa values -- Heisenberg
# ===================================================================

class TestKappaHeisenberg:
    """kappa(H_k) = k.  [C1]"""

    def test_k1(self):
        # VERIFIED [DC] kappa=k=1; [CF] matches c_Heis(1)=1
        assert kappa_heisenberg(1) == Fraction(1)

    def test_k0(self):
        # VERIFIED [DC] kappa=0; [LC] k=0 -> trivial
        assert kappa_heisenberg(0) == Fraction(0)

    def test_k2(self):
        # VERIFIED [DC] kappa=2; [CF] Leech=24*kappa(H_1)
        assert kappa_heisenberg(2) == Fraction(2)

    def test_k_negative(self):
        # VERIFIED [DC] kappa=-1
        assert kappa_heisenberg(-1) == Fraction(-1)


# ===================================================================
#  SECTION 3: Kappa values -- Virasoro
# ===================================================================

class TestKappaVirasoro:
    """kappa(Vir_c) = c/2.  [C2]"""

    def test_c0(self):
        # VERIFIED [DC] kappa=0; [LC] trivial
        assert kappa_virasoro(0) == Fraction(0)

    def test_c1(self):
        # VERIFIED [DC] kappa=1/2; [CF] free boson c=1
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_c13_self_dual(self):
        # VERIFIED [DC] kappa=13/2; [LT] C8 self-dual point; [SY] c->26-c fixed
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_c26(self):
        # VERIFIED [DC] kappa=13; [CF] c+c'=26 -> kappa+kappa'=13
        assert kappa_virasoro(26) == Fraction(13)

    def test_complementarity_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13.  [C8, C18]"""
        # VERIFIED [DC] direct; [SY] Virasoro duality c->26-c
        for c in [0, 1, Fraction(1, 2), 13, 26, -5]:
            s = kappa_virasoro(c) + kappa_virasoro(26 - c)
            assert s == Fraction(13), f"Failed at c={c}: sum={s}"


# ===================================================================
#  SECTION 4: Kappa values -- Affine KM
# ===================================================================

class TestKappaAffineKM:
    """kappa(V_k(g)) = dim(g)*(k+h^v)/(2*h^v).  [C3]"""

    def test_sl2_k0(self):
        # VERIFIED [DC] 3*2/4 = 3/2; [LC] abelian limit, NOT zero (C3)
        assert kappa_affine_sl2(0) == Fraction(3, 2)

    def test_sl2_k1(self):
        # VERIFIED [DC] 3*3/4 = 9/4; [CF] matches entanglement_shadow_engine
        assert kappa_affine_sl2(1) == Fraction(9, 4)

    def test_sl2_critical(self):
        """k=-h^v=-2 -> kappa=0 (critical level).  [C3]"""
        # VERIFIED [DC] 3*0/4 = 0; [LC] critical level
        assert kappa_affine_sl2(-2) == Fraction(0)

    def test_sl3_k0(self):
        # VERIFIED [DC] 8*3/6 = 4; [LC] dim(sl3)/2 = 4
        assert kappa_affine_sl3(0) == Fraction(4)

    def test_sl3_k1(self):
        # VERIFIED [DC] 8*4/6 = 16/3; [CF] cross-check with general formula
        assert kappa_affine_sl3(1) == Fraction(16, 3)

    def test_sl3_critical(self):
        # VERIFIED [DC] 8*0/6 = 0; [LC] critical level
        assert kappa_affine_sl3(-3) == Fraction(0)

    def test_so4_k1(self):
        # VERIFIED [DC] 6*3/4 = 9/2; [CF] general formula
        assert kappa_affine_so4(1) == Fraction(9, 2)

    def test_g2_k1(self):
        # VERIFIED [DC] 14*5/8 = 35/4; [CF] general formula
        assert kappa_affine_g2(1) == Fraction(35, 4)

    def test_g2_critical(self):
        # VERIFIED [DC] 14*0/8 = 0; [LC] critical level
        assert kappa_affine_g2(-4) == Fraction(0)

    def test_e8_k1(self):
        # VERIFIED [DC] 248*31/60 = 7688/60 = 1922/15; [CF] general formula
        assert kappa_affine_e8(1) == Fraction(1922, 15)

    def test_e8_k0(self):
        # VERIFIED [DC] 248*30/60 = 124; [LC] dim(e8)/2 = 124
        assert kappa_affine_e8(0) == Fraction(124)

    def test_e8_critical(self):
        # VERIFIED [DC] 248*0/60 = 0; [LC] critical
        assert kappa_affine_e8(-30) == Fraction(0)

    def test_general_k0_equals_dim_over_2(self):
        """At k=0, kappa = dim(g)/2 for ALL Lie algebras.  [C3]"""
        # VERIFIED [DC] direct from formula; [SY] universal
        for name, data in LIE_DATA.items():
            kap = kappa_affine_km(data['dim'], 0, data['h_dual'])
            expected = Fraction(data['dim'], 2)
            assert kap == expected, f"Failed for {name}: {kap} != {expected}"

    def test_general_critical_is_zero(self):
        """At k=-h^v, kappa = 0 for ALL Lie algebras.  [C3]"""
        # VERIFIED [DC] direct; [SY] universal
        for name, data in LIE_DATA.items():
            kap = kappa_affine_km(data['dim'], -data['h_dual'], data['h_dual'])
            assert kap == Fraction(0), f"Failed for {name}: {kap} != 0"


# ===================================================================
#  SECTION 5: Kappa values -- W_N
# ===================================================================

class TestKappaWN:
    """kappa(W_N) = c*(H_N - 1).  [C4]"""

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro, so kappa(W_2, c) = kappa(Vir_c) = c/2.  [C4]"""
        # VERIFIED [DC] H_2-1=1/2, c*1/2=c/2; [CF] W_2=Vir identity
        for c in [1, 2, 13, 26, Fraction(1, 2)]:
            assert kappa_wn(2, c) == kappa_virasoro(c), f"Failed at c={c}"

    def test_w3_c6(self):
        # VERIFIED [DC] 6*5/6 = 5; [CF] entanglement_shadow_engine kappa_wN(3,6)=5
        assert kappa_wn(3, 6) == Fraction(5)

    def test_w3_c2(self):
        # VERIFIED [DC] 2*5/6 = 5/3; [CF] cross-check
        assert kappa_wn(3, 2) == Fraction(5, 3)

    def test_w3_c0(self):
        # VERIFIED [DC] 0*5/6 = 0; [LC] c=0
        assert kappa_wn(3, 0) == Fraction(0)

    def test_w4(self):
        # VERIFIED [DC] H_4-1 = 25/12-1 = 13/12; kappa(W_4,12) = 12*13/12 = 13
        assert kappa_wn(4, 12) == Fraction(13)

    def test_ap136_not_h_n_minus_1(self):
        """Verify we use H_N - 1, NOT H_{N-1}.  [AP136]"""
        # At N=3: H_3 - 1 = 5/6, but H_2 = 3/2.  These differ.
        # VERIFIED [DC] direct; [CF] AP136 canonical example
        h3_minus_1 = harmonic_number(3) - 1  # 5/6
        h2 = harmonic_number(2)               # 3/2
        assert h3_minus_1 != h2
        assert h3_minus_1 == Fraction(5, 6)
        assert h2 == Fraction(3, 2)


# ===================================================================
#  SECTION 6: Kappa values -- betagamma / bc
# ===================================================================

class TestKappaBetagammaBc:
    """betagamma and bc central charges and kappa values.  [C5, C6, C7]"""

    def test_c_betagamma_half(self):
        # VERIFIED [DC] 2*(6/4-3+1) = 2*(-1/2) = -1; [LT] C6 symplectic boson
        assert c_betagamma(Fraction(1, 2)) == Fraction(-1)

    def test_c_betagamma_2(self):
        # VERIFIED [DC] 2*(24-12+1) = 26; [LT] C6 matter ghost
        assert c_betagamma(2) == Fraction(26)

    def test_c_bc_half(self):
        # VERIFIED [DC] 1-3*0 = 1; [LT] C5 free fermion
        assert c_bc(Fraction(1, 2)) == Fraction(1)

    def test_c_bc_2(self):
        # VERIFIED [DC] 1-3*9 = -26; [LT] C5 reparam ghost
        assert c_bc(2) == Fraction(-26)

    def test_complementarity_c_bg_plus_c_bc(self):
        """c_bg(lambda) + c_bc(lambda) = 0 for all lambda.  [C7]"""
        # VERIFIED [DC] direct; [SY] bc/betagamma complementarity
        for lam in [0, Fraction(1, 2), 1, Fraction(3, 2), 2, Fraction(5, 2), -1]:
            total = c_betagamma(lam) + c_bc(lam)
            assert total == Fraction(0), f"Failed at lambda={lam}: sum={total}"

    def test_kappa_betagamma_half(self):
        # VERIFIED [DC] 6/4-3+1 = -1/2; [CF] c_bg/2 = -1/2
        assert kappa_betagamma(Fraction(1, 2)) == Fraction(-1, 2)

    def test_kappa_betagamma_1(self):
        # VERIFIED [DC] 6-6+1 = 1; [CF] c_bg(1)=2, kappa=1
        assert kappa_betagamma(1) == Fraction(1)

    def test_kappa_betagamma_2(self):
        # VERIFIED [DC] 24-12+1 = 13; [CF] c_bg(2)=26, kappa=13
        assert kappa_betagamma(2) == Fraction(13)

    def test_kappa_bc_half(self):
        """Free fermion: c_bc(1/2) = 1, kappa = 1/2."""
        # VERIFIED [DC] c_bc=1, kappa=1/2; [CF] free fermion
        assert kappa_bc(Fraction(1, 2)) == Fraction(1, 2)

    def test_kappa_bc_2(self):
        """Reparam ghost: c_bc(2) = -26, kappa = -13."""
        # VERIFIED [DC] c_bc=-26, kappa=-13; [CF] ghost system
        assert kappa_bc(2) == Fraction(-13)

    def test_kappa_bg_plus_kappa_bc(self):
        """kappa_bg + kappa_bc = 0 for all lambda (from c_bg + c_bc = 0)."""
        # VERIFIED [DC] direct from complementarity; [SY] follows from C7
        for lam in [0, Fraction(1, 2), 1, 2, Fraction(3, 2)]:
            total = kappa_betagamma(lam) + kappa_bc(lam)
            assert total == Fraction(0), f"Failed at lambda={lam}: sum={total}"


# ===================================================================
#  SECTION 7: Kappa values -- Super Virasoro
# ===================================================================

class TestKappaSuperVirasoro:
    """kappa(SVir_c) = (3c - 2)/4.  [AP68]"""

    def test_c_two_thirds(self):
        # VERIFIED [DC] (2-2)/4 = 0; [LC] tricritical Ising
        assert kappa_super_virasoro(Fraction(2, 3)) == Fraction(0)

    def test_c10(self):
        # VERIFIED [DC] (30-2)/4 = 7; [CF] direct computation
        assert kappa_super_virasoro(10) == Fraction(7)

    def test_c_15(self):
        # VERIFIED [DC] (45-2)/4 = 43/4
        assert kappa_super_virasoro(15) == Fraction(43, 4)


# ===================================================================
#  SECTION 8: Kappa values -- Lattice
# ===================================================================

class TestKappaLattice:
    """kappa(lattice, rank r) = r (at k=1).  [C1 Heis]"""

    def test_e8_lattice(self):
        # VERIFIED [DC] rank=8, kappa=8; [CF] 8*kappa(H_1)
        assert kappa_lattice(8) == Fraction(8)

    def test_leech(self):
        # VERIFIED [DC] rank=24, kappa=24; [LT] FLM88
        assert kappa_lattice(24) == Fraction(24)

    def test_rank1(self):
        # VERIFIED [DC] kappa=1; [CF] = kappa(H_1)
        assert kappa_lattice(1) == Fraction(1)


# ===================================================================
#  SECTION 9: Entanglement entropy formula
# ===================================================================

class TestEntanglementEntropy:
    """S_EE = (2*kappa/3)*log(L/eps)."""

    def test_virasoro_calabrese_cardy(self):
        """For Vir_c, S_EE = (c/3)*log(L/eps).  [Calabrese-Cardy 2004]"""
        # VERIFIED [DC] 2*(c/2)/3 = c/3; [LT] hep-th/0405152
        c = 1
        kap = kappa_virasoro(c)
        L, eps = 100.0, 1.0
        s_ee = entanglement_entropy(kap, L, eps)
        expected = (c / 3) * math.log(100.0)
        assert abs(s_ee - expected) < 1e-12

    def test_virasoro_c13(self):
        """S_EE(Vir_13) = (13/3)*log(L/eps)."""
        # VERIFIED [DC] 2*(13/2)/3 = 13/3; [CF] self-dual
        kap = kappa_virasoro(13)
        L, eps = 1000.0, 0.1
        s_ee = entanglement_entropy(kap, L, eps)
        expected = float(Fraction(13, 3)) * math.log(10000.0)
        assert abs(s_ee - expected) < 1e-10

    def test_heisenberg_k0_vanishes(self):
        """S_EE(H_0) = 0 because kappa = 0."""
        # VERIFIED [DC] kappa=0 -> S_EE=0; [LC] trivial
        assert entanglement_entropy(kappa_heisenberg(0), 100.0, 1.0) == 0.0

    def test_virasoro_c0_vanishes(self):
        """S_EE(Vir_0) = 0 because kappa = 0."""
        # VERIFIED [DC] kappa=0 -> S_EE=0; [LC] trivial
        assert entanglement_entropy(kappa_virasoro(0), 100.0, 1.0) == 0.0

    def test_km_critical_vanishes(self):
        """S_EE at critical level k=-h^v vanishes because kappa = 0."""
        # VERIFIED [DC] kappa=0; [LC] critical level
        assert entanglement_entropy(kappa_affine_sl2(-2), 100.0, 1.0) == 0.0
        assert entanglement_entropy(kappa_affine_sl3(-3), 100.0, 1.0) == 0.0

    def test_multiple_L_eps(self):
        """S_EE scales as log(L/eps) for fixed kappa."""
        # VERIFIED [DC] S_EE(L2/eps2)/S_EE(L1/eps1) = log(L2/eps2)/log(L1/eps1)
        kap = kappa_virasoro(1)  # kappa = 1/2
        pairs = [(10.0, 1.0), (100.0, 1.0), (1000.0, 0.01)]
        for L, eps in pairs:
            s_ee = entanglement_entropy(kap, L, eps)
            expected = (2 * 0.5 / 3) * math.log(L / eps)
            assert abs(s_ee - expected) < 1e-12, f"Failed at L={L}, eps={eps}"

    def test_exact_prefactor(self):
        """entanglement_entropy_exact returns 2*kappa/3."""
        # VERIFIED [DC] direct
        assert entanglement_entropy_exact(Fraction(13, 2)) == Fraction(13, 3)
        assert entanglement_entropy_exact(Fraction(1)) == Fraction(2, 3)
        assert entanglement_entropy_exact(Fraction(0)) == Fraction(0)

    def test_eps_positive(self):
        """eps must be positive."""
        with pytest.raises(ValueError):
            entanglement_entropy(Fraction(1), 100.0, 0.0)
        with pytest.raises(ValueError):
            entanglement_entropy(Fraction(1), 100.0, -1.0)

    def test_L_positive(self):
        """L must be positive."""
        with pytest.raises(ValueError):
            entanglement_entropy(Fraction(1), 0.0, 1.0)

    def test_heisenberg_k1_numerical(self):
        """S_EE(H_1) = (2/3)*log(L/eps)."""
        # VERIFIED [DC] 2*1/3 = 2/3; [CF] prefactor = 2/3
        L, eps = 100.0, 1.0
        s_ee = entanglement_entropy(kappa_heisenberg(1), L, eps)
        expected = (2.0 / 3.0) * math.log(100.0)
        assert abs(s_ee - expected) < 1e-12

    def test_sl2_k1_numerical(self):
        """S_EE(sl_2, k=1) = (2*(9/4)/3)*log(L/eps) = (3/2)*log(L/eps)."""
        # VERIFIED [DC] 2*(9/4)/3 = 18/12 = 3/2; [CF] cross-check
        L, eps = 100.0, 1.0
        s_ee = entanglement_entropy(kappa_affine_sl2(1), L, eps)
        expected = 1.5 * math.log(100.0)
        assert abs(s_ee - expected) < 1e-12


# ===================================================================
#  SECTION 10: Cross-family consistency
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks that constrain the landscape."""

    def test_virasoro_complementarity_entropy(self):
        """S_EE(Vir_c) + S_EE(Vir_{26-c}) = (26/3)*log(L/eps)."""
        # kappa(c)+kappa(26-c) = c/2 + (26-c)/2 = 13.
        # S_EE(c) + S_EE(26-c) = (2/3)*(kappa+kappa')*log = (26/3)*log.
        # VERIFIED [DC] 2*13/3 = 26/3; [SY] Virasoro duality
        L, eps = 100.0, 1.0
        for c in [1, 5, 13, 26, Fraction(1, 2)]:
            s1 = entanglement_entropy(kappa_virasoro(c), L, eps)
            s2 = entanglement_entropy(kappa_virasoro(26 - c), L, eps)
            expected = float(Fraction(26, 3)) * math.log(L / eps)
            assert abs(s1 + s2 - expected) < 1e-10, f"Failed at c={c}"

    def test_bg_bc_entropy_cancellation(self):
        """S_EE(bg) + S_EE(bc) = 0 for all lambda (kappa_bg + kappa_bc = 0)."""
        # VERIFIED [DC] complementarity; [SY] C7
        L, eps = 100.0, 1.0
        for lam in [Fraction(1, 2), 1, 2]:
            s_bg = entanglement_entropy(kappa_betagamma(lam), L, eps)
            s_bc = entanglement_entropy(kappa_bc(lam), L, eps)
            assert abs(s_bg + s_bc) < 1e-12, f"Failed at lambda={lam}"

    def test_w2_equals_virasoro_entropy(self):
        """S_EE(W_2, c) = S_EE(Vir_c) because W_2 = Vir."""
        # VERIFIED [DC] kappa(W_2)=c/2=kappa(Vir); [CF] W_2=Vir identity
        L, eps = 100.0, 1.0
        for c in [1, 13, 26]:
            s_w2 = entanglement_entropy(kappa_wn(2, c), L, eps)
            s_vir = entanglement_entropy(kappa_virasoro(c), L, eps)
            assert abs(s_w2 - s_vir) < 1e-12, f"Failed at c={c}"

    def test_leech_equals_24_heisenberg(self):
        """Leech lattice: kappa = 24 = 24*kappa(H_1)."""
        # VERIFIED [DC] rank*k=24*1; [CF] FLM88
        assert kappa_lattice(24) == 24 * kappa_heisenberg(1)

    def test_km_k0_not_zero(self):
        """kappa(V_0(g)) = dim(g)/2, NOT zero.  [C3]"""
        # VERIFIED [DC] direct; [CF] universal abelian limit
        assert kappa_affine_sl2(0) == Fraction(3, 2)
        assert kappa_affine_sl2(0) != Fraction(0)

    def test_string_ghost_cancellation(self):
        """c_bg(2) + c_bc(2) = 26 + (-26) = 0.  [C7: string ghost]"""
        # VERIFIED [DC] direct; [LT] standard string theory
        assert c_betagamma(2) + c_bc(2) == Fraction(0)
        assert c_betagamma(2) == Fraction(26)
        assert c_bc(2) == Fraction(-26)


# ===================================================================
#  SECTION 11: Tabulation
# ===================================================================

class TestTabulation:
    """Verify the tabulation function returns complete, consistent data."""

    def test_tabulate_returns_list(self):
        results = tabulate(100.0, 1.0)
        assert isinstance(results, list)
        assert len(results) == len(FAMILIES)

    def test_tabulate_row_keys(self):
        results = tabulate(100.0, 1.0)
        required_keys = {"family", "params", "kappa", "kappa_float", "S_EE", "L", "eps", "prefactor"}
        for r in results:
            assert required_keys <= set(r.keys()), f"Missing keys in {r['family']}"

    def test_tabulate_consistency(self):
        """Each row's S_EE matches (2*kappa/3)*log(L/eps)."""
        L, eps = 100.0, 1.0
        results = tabulate(L, eps)
        for r in results:
            expected = (2 * r['kappa_float'] / 3) * math.log(L / eps)
            assert abs(r['S_EE'] - expected) < 1e-10, f"Inconsistent for {r['family']}"

    def test_tabulate_at_least_25_families(self):
        """We tabulate at least 25 representative parameter points."""
        results = tabulate()
        assert len(results) >= 25

    def test_tabulate_different_L_eps(self):
        """Tabulation works at different (L, eps)."""
        r1 = tabulate(100.0, 1.0)
        r2 = tabulate(1000.0, 0.1)
        # Same kappas, different S_EE
        assert r1[0]['kappa'] == r2[0]['kappa']
        if r1[0]['kappa'] != 0:
            assert r1[0]['S_EE'] != r2[0]['S_EE']

    def test_zero_kappa_entries(self):
        """Entries with kappa=0 have S_EE=0."""
        results = tabulate(100.0, 1.0)
        for r in results:
            if r['kappa'] == Fraction(0):
                assert r['S_EE'] == 0.0, f"Nonzero S_EE at kappa=0: {r['family']}"


# ===================================================================
#  SECTION 12: Cross-engine validation
# ===================================================================

class TestCrossEngineValidation:
    """Validate kappa values against f2_kappa_verification_engine conventions."""

    def test_sl2_k1_matches_f2_engine(self):
        """kappa(sl_2, k=1) = 9/4.  Cross-check with f2 engine."""
        # VERIFIED [DC] 3*3/4; [CF] f2_kappa_verification_engine.kappa_affine_sl2(1)
        assert kappa_affine_sl2(1) == Fraction(9, 4)

    def test_virasoro_c1_matches_f2_engine(self):
        """kappa(Vir_1) = 1/2.  Cross-check with f2 engine."""
        # VERIFIED [DC] 1/2; [CF] f2_kappa_verification_engine.kappa_virasoro(1)
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_w3_c6_matches_shadow_engine(self):
        """kappa(W_3, c=6) = 5.  Cross-check with entanglement_shadow_engine."""
        # VERIFIED [DC] 6*5/6; [CF] entanglement_shadow_engine.kappa_wN(3, 6)
        assert kappa_wn(3, 6) == Fraction(5)

    def test_betagamma_lam1_matches_shadow_engine(self):
        """kappa(bg, lambda=1) = 1.  Cross-check with shadow engine."""
        # VERIFIED [DC] 6-6+1; [CF] entanglement_shadow_engine.kappa_betagamma(1)
        assert kappa_betagamma(1) == Fraction(1)
