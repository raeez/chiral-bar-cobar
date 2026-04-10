r"""Tests for principal W-algebra Koszul conductor engine.

THEOREM-LEVEL TESTS: For the principal W-algebra W(g, k) of a simple Lie
algebra g, the complementarity sum alpha(g) = c(k) + c(k') is level-independent
and equals 2*rank + 4*dim*h^v.  The Koszul conductor K(W(g)) = varrho(g)*alpha(g)
where varrho = sum 1/s_i over the conformal spins.

VERIFICATION PATHS for each hardcoded expected value:
    [DC] Direct computation from c(k) = rank - dim*h^v*(k+h^v-1)^2/(k+h^v)
    [CF] Cross-family consistency (A1 -> Vir, A2 -> W_3, etc.)
    [LC] Limiting case / boundary evaluation
    [LT] Literature: CLAUDE.md C4, C8, C18, C20; Bourbaki exponent tables

References:
    Fateev-Lukyanov (1988): central charge formula
    Feigin-Frenkel (1992): dual level k' = -k - 2h^v
    Bourbaki, Lie Groups Ch. IV-VI, Table V: exponents
    CLAUDE.md C4 (W_N kappa), C8 (Vir self-dual), C18 (Koszul complementarity)
"""

import pytest
import sys
import os
from fractions import Fraction

# Ensure compute.lib is importable.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from compute.lib.e8_koszul_conductor_engine import (
    central_charge,
    dual_level,
    alpha_closed_form,
    alpha_numerical,
    verify_k_independence,
    harmonic,
    varrho,
    kappa,
    koszul_conductor,
    self_dual_level,
    exponents_of,
    spins_of,
    verify_all,
    summary,
    LIE_ALGEBRA_DATA,
    ALPHA_E8,
    VARRHO_E8,
    K_E8,
    E8_EXPONENTS,
    E8_SPINS,
)


# =============================================================================
# Exponent and spin tables
# =============================================================================

class TestExponents:
    """Verify exponent tables against Bourbaki."""

    def test_A1_exponents(self):
        # VERIFIED: [LT] Bourbaki Table V, A_1: exponents = {1}; [DC] range(1,2) = [1].
        assert exponents_of('A1') == [1]

    def test_A2_exponents(self):
        # VERIFIED: [LT] Bourbaki Table V, A_2: exponents = {1, 2}; [DC] range(1,3) = [1,2].
        assert exponents_of('A2') == [1, 2]

    def test_E8_exponents(self):
        # VERIFIED: [LT] Bourbaki Table V, E_8: {1,7,11,13,17,19,23,29};
        # [DC] sum of exponents = 1+7+11+13+17+19+23+29 = 120 = h^v(E_8)*rank/something.
        # Actually sum = |Phi^+| = 120 for E_8. Correct.
        assert exponents_of('E8') == [1, 7, 11, 13, 17, 19, 23, 29]

    def test_E8_spins(self):
        # VERIFIED: [DC] exponents + 1; [LT] standard W(E_8) generator spins.
        assert spins_of('E8') == [2, 8, 12, 14, 18, 20, 24, 30]

    def test_G2_exponents(self):
        # VERIFIED: [LT] Bourbaki Table V, G_2: {1, 5}; [DC] sum = 6 = |Phi^+(G_2)|.
        assert exponents_of('G2') == [1, 5]

    def test_F4_exponents(self):
        # VERIFIED: [LT] Bourbaki Table V, F_4: {1, 5, 7, 11}; [DC] sum = 24 = |Phi^+(F_4)|.
        assert exponents_of('F4') == [1, 5, 7, 11]

    def test_D4_exponents(self):
        # VERIFIED: [LT] Bourbaki Table V, D_4: {1, 3, 3, 5}; [DC] sum = 12 = |Phi^+(D_4)|.
        assert exponents_of('D4') == [1, 3, 3, 5]


# =============================================================================
# Harmonic numbers
# =============================================================================

class TestHarmonic:
    """Verify harmonic number computation."""

    def test_H1(self):
        # VERIFIED: [DC] H_1 = 1; [LC] trivial base case.
        assert harmonic(1) == Fraction(1)

    def test_H2(self):
        # VERIFIED: [DC] 1 + 1/2 = 3/2; [CF] matches CLAUDE.md C19.
        assert harmonic(2) == Fraction(3, 2)

    def test_H3(self):
        # VERIFIED: [DC] 1 + 1/2 + 1/3 = 11/6; [CF] matches CLAUDE.md C19.
        assert harmonic(3) == Fraction(11, 6)

    def test_H8(self):
        # VERIFIED: [DC] 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8
        #   = 840/840 + 420/840 + 280/840 + 210/840 + 168/840 + 140/840 + 120/840 + 105/840
        #   = 2283/840 = 761/280;
        # [LC] float(761/280) = 2.71785714..., matching known H_8.
        assert harmonic(8) == Fraction(761, 280)


# =============================================================================
# Anomaly ratio (varrho)
# =============================================================================

class TestVarrho:
    """Verify anomaly ratios."""

    def test_varrho_A1(self):
        # VERIFIED: [DC] 1/2; [CF] H_2 - 1 = 1/2, matches CLAUDE.md C4 for W_2 = Vir.
        assert varrho('A1') == Fraction(1, 2)

    def test_varrho_A2(self):
        # VERIFIED: [DC] 1/2 + 1/3 = 5/6; [CF] H_3 - 1 = 5/6, matches CLAUDE.md C4 for W_3.
        assert varrho('A2') == Fraction(5, 6)

    def test_varrho_A_type_equals_HN_minus_1(self):
        """For A_{n} = sl_{n+1}, varrho = H_{n+1} - 1."""
        # VERIFIED: [DC] spins of A_n are {2,...,n+1}, so varrho = sum_{j=2}^{n+1} 1/j = H_{n+1}-1;
        # [CF] matches CLAUDE.md C4 structure.
        for n in range(1, 9):
            name = f'A{n}'
            if name in LIE_ALGEBRA_DATA:
                N = n + 1
                assert varrho(name) == harmonic(N) - 1, f"Failed for {name}"

    def test_varrho_E8(self):
        # VERIFIED: [DC] 1/2+1/8+1/12+1/14+1/18+1/20+1/24+1/30;
        # LCD = 2520: 1260+315+210+180+140+126+105+84 = 2420. 2420/2520 = 121/126.
        # [CF] NOT H_8-1 = 481/280; E_8 is not A-type, so H_N-1 formula does not apply.
        assert varrho('E8') == VARRHO_E8
        assert VARRHO_E8 == Fraction(121, 126)

    def test_varrho_G2(self):
        # VERIFIED: [DC] 1/2 + 1/6 = 2/3; [LC] spins {2,6}.
        assert varrho('G2') == Fraction(2, 3)

    def test_varrho_F4(self):
        # VERIFIED: [DC] 1/2 + 1/6 + 1/8 + 1/12 = 12/24+4/24+3/24+2/24 = 21/24 = 7/8;
        # [LC] spins {2,6,8,12}.
        assert varrho('F4') == Fraction(7, 8)


# =============================================================================
# Complementarity sum alpha
# =============================================================================

class TestAlpha:
    """Verify alpha(g) = c(k) + c(k') is k-independent."""

    def test_alpha_closed_form_A1(self):
        # VERIFIED: [DC] 2*1 + 4*3*2 = 2+24 = 26; [CF] c+c'=26 for Virasoro, CLAUDE.md C8.
        assert alpha_closed_form(1, 3, 2) == Fraction(26)

    def test_alpha_closed_form_A2(self):
        # VERIFIED: [DC] 2*2 + 4*8*3 = 4+96 = 100; [CF] direct expansion in docstring.
        assert alpha_closed_form(2, 8, 3) == Fraction(100)

    def test_alpha_closed_form_E8(self):
        # VERIFIED: [DC] 2*8 + 4*248*30 = 16+29760 = 29776;
        # [DC] numerical at k=1: c(1)+c(-61) = 29776.
        assert alpha_closed_form(8, 248, 30) == ALPHA_E8
        assert ALPHA_E8 == Fraction(29776)

    def test_alpha_closed_form_G2(self):
        # VERIFIED: [DC] 2*2 + 4*14*4 = 4+224 = 228; [DC] numerical at k=1.
        assert alpha_closed_form(2, 14, 4) == Fraction(228)

    def test_alpha_closed_form_F4(self):
        # VERIFIED: [DC] 2*4 + 4*52*9 = 8+1872 = 1880; [DC] numerical at k=1.
        assert alpha_closed_form(4, 52, 9) == Fraction(1880)

    def test_alpha_numerical_matches_closed_form(self):
        """Verify numerical alpha at k=1 matches closed form for all algebras."""
        for name, (rank, dim, hv) in LIE_ALGEBRA_DATA.items():
            assert (alpha_numerical(rank, dim, hv, Fraction(1))
                    == alpha_closed_form(rank, dim, hv)), f"Failed for {name}"

    @pytest.mark.parametrize("name", ['A1', 'A2', 'E6', 'E7', 'E8', 'F4', 'G2'])
    def test_k_independence(self, name):
        """Verify alpha is constant across 9 test levels."""
        rank, dim, hv = LIE_ALGEBRA_DATA[name]
        assert verify_k_independence(rank, dim, hv), f"k-independence failed for {name}"


# =============================================================================
# Koszul conductors
# =============================================================================

class TestKoszulConductor:
    """Verify K(W(g)) = varrho(g) * alpha(g)."""

    def test_K_virasoro(self):
        # VERIFIED: [DC] (1/2)*26 = 13; [CF] K(Vir) = 13 from CLAUDE.md C8/C18;
        # [LT] Virasoro self-dual at c=13 means kappa+kappa'=13.
        assert koszul_conductor('A1') == Fraction(13)

    def test_K_W3(self):
        # VERIFIED: [DC] (5/6)*100 = 250/3; [CF] CLAUDE.md C18 gives K(W_3)=250/3;
        # [LT] matches bp_koszul_conductor_engine.py cross-ref.
        assert koszul_conductor('A2') == Fraction(250, 3)

    def test_K_E8(self):
        # VERIFIED: [DC] (121/126)*29776 = 121*29776/126;
        # 121*29776 = 121*29776. 121*29000=3509000, 121*776=93896. Total=3602896.
        # 3602896/126 = 1801448/63.
        # [CF] cross-family: A1->13, A2->250/3 both correct.
        # [DC] 1801448/63 as float = 28594.412698...
        assert koszul_conductor('E8') == K_E8
        assert K_E8 == Fraction(1801448, 63)

    def test_K_G2(self):
        # VERIFIED: [DC] (2/3)*228 = 152; [DC] integer result.
        assert koszul_conductor('G2') == Fraction(152)

    def test_K_F4(self):
        # VERIFIED: [DC] (7/8)*1880 = 7*235 = 1645; [DC] integer result.
        assert koszul_conductor('F4') == Fraction(1645)

    def test_K_E6(self):
        # VERIFIED: [DC] varrho(E6) = 1/2+1/5+1/6+1/8+1/9+1/12;
        # LCD=360: 180+72+60+45+40+30=427. varrho=427/360.
        # alpha(E6) = 2*6+4*78*12 = 12+3744 = 3756.
        # K = (427/360)*3756 = 427*3756/360 = 1603812/360 = 133651/30.
        assert koszul_conductor('E6') == Fraction(133651, 30)

    def test_K_E7(self):
        # VERIFIED: [DC] varrho(E7) = 1/2+1/6+1/8+1/10+1/12+1/14+1/18;
        # LCD=2520: 1260+420+315+252+210+180+140=2777. varrho=2777/2520.
        # alpha(E7) = 2*7+4*133*18 = 14+9576 = 9590.
        # K = (2777/2520)*9590 = 2777*9590/2520 = 26631430/2520 = 380449/36.
        assert koszul_conductor('E7') == Fraction(380449, 36)


# =============================================================================
# Central charge function
# =============================================================================

class TestCentralCharge:
    """Verify c(g, k) at specific values."""

    def test_c_virasoro_k0(self):
        # c(sl_2, k=0) = 1 - 3*2*(0+2-1)^2/(0+2) = 1 - 6*1/2 = 1-3 = -2.
        # VERIFIED: [DC] 1 - 6/2 = -2; [LT] Vir at level 0 (non-unitary).
        assert central_charge(1, 3, 2, Fraction(0)) == Fraction(-2)

    def test_c_virasoro_k1(self):
        # c(sl_2, k=1) = 1 - 6*4/3 = 1 - 8 = -7.
        # VERIFIED: [DC] 1 - 3*2*4/3 = 1-8 = -7.
        assert central_charge(1, 3, 2, Fraction(1)) == Fraction(-7)

    def test_c_E8_k1(self):
        # c(E_8, k=1) = 8 - 248*30*30^2/31 = 8 - 248*30*900/31 = 8 - 6696000/31.
        # VERIFIED: [DC] 248*30 = 7440; 7440*900 = 6696000; 6696000/31; 8 - 6696000/31.
        # = (8*31 - 6696000)/31 = (248 - 6696000)/31 = -6695752/31.
        assert central_charge(8, 248, 30, Fraction(1)) == Fraction(-6695752, 31)


# =============================================================================
# Dual level
# =============================================================================

class TestDualLevel:
    """Verify Feigin-Frenkel dual level k' = -k - 2*h^v."""

    def test_dual_level_E8(self):
        # VERIFIED: [DC] -1 - 60 = -61; [LT] Feigin-Frenkel duality.
        assert dual_level(Fraction(1), 30) == Fraction(-61)

    def test_dual_level_sl2(self):
        # VERIFIED: [DC] -1 - 4 = -5; [LT] Vir: c -> 26-c iff k -> -k-4.
        assert dual_level(Fraction(1), 2) == Fraction(-5)

    def test_self_dual_E8(self):
        # VERIFIED: [DC] k_sd = -h^v = -30; [LT] fixed point of k -> -k-60.
        assert self_dual_level(30) == Fraction(-30)


# =============================================================================
# Kappa values
# =============================================================================

class TestKappa:
    """Verify kappa = varrho * c at specific levels."""

    def test_kappa_complementarity_E8(self):
        """kappa(E_8, k) + kappa(E_8, k') = K(E_8) for several k."""
        # VERIFIED: [DC] algebraic k-independence; [CF] works for A1, A2.
        K = koszul_conductor('E8')
        for k in [Fraction(1), Fraction(5), Fraction(-1), Fraction(1, 7)]:
            kp = dual_level(k, 30)
            assert kappa('E8', k) + kappa('E8', kp) == K

    def test_kappa_complementarity_A1(self):
        """kappa(Vir, k) + kappa(Vir, k') = 13 for several k."""
        # VERIFIED: [DC] varrho=1/2, alpha=26, K=13; [LT] CLAUDE.md C8.
        for k in [Fraction(0), Fraction(1), Fraction(-1), Fraction(3, 7)]:
            kp = dual_level(k, 2)
            assert kappa('A1', k) + kappa('A1', kp) == Fraction(13)


# =============================================================================
# Full verification
# =============================================================================

class TestFullVerification:
    """Run the engine's internal verify_all()."""

    def test_verify_all(self):
        assert verify_all()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
