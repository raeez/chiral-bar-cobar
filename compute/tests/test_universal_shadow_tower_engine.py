"""Comprehensive tests for the universal shadow tower engine.

Tests all six standard families: Heisenberg, Virasoro, affine sl_2,
W_3, betagamma, Bershadsky-Polyakov.

Every hardcoded expected value has a # VERIFIED comment citing 2+
independent derivation paths from different categories:
    [DC] direct computation
    [LT] literature (paper + eq #)
    [LC] limiting case
    [SY] symmetry
    [CF] cross-family
    [NE] numerical (>=10 digits)
    [DA] dimensional analysis
"""

from fractions import Fraction

import pytest

from compute.lib.universal_shadow_tower_engine import (
    ShadowTowerResult,
    affine_km,
    bernoulli,
    bershadsky_polyakov,
    betagamma,
    c_bc,
    c_betagamma,
    c_bp,
    classify_glcm,
    compute_free_energies,
    compute_shadow_tower,
    from_data,
    harmonic_number,
    heisenberg,
    kappa_affine_km,
    kappa_betagamma,
    kappa_bp,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_wn,
    lambda_fp,
    virasoro,
    w3_algebra,
)


# ============================================================================
# Bernoulli numbers and Faber-Pandharipande
# ============================================================================

class TestBernoulli:
    def test_B0(self):
        # VERIFIED: [DC] B_0 = 1 by definition; [LT] standard reference.
        assert bernoulli(0) == Fraction(1)

    def test_B1(self):
        # VERIFIED: [DC] B_1 = -1/2 by convention; [LT] Abramowitz-Stegun.
        assert bernoulli(1) == Fraction(-1, 2)

    def test_B2(self):
        # VERIFIED: [DC] B_2 = 1/6 from recursion; [LT] standard reference.
        assert bernoulli(2) == Fraction(1, 6)

    def test_B4(self):
        # VERIFIED: [DC] B_4 = -1/30 from recursion; [LT] standard reference.
        assert bernoulli(4) == Fraction(-1, 30)

    def test_B6(self):
        # VERIFIED: [DC] B_6 = 1/42 from recursion; [LT] standard reference.
        assert bernoulli(6) == Fraction(1, 42)

    def test_odd_vanish(self):
        # VERIFIED: [DC] B_n = 0 for odd n >= 3; [SY] symmetry of generating function.
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli(n) == Fraction(0)


class TestLambdaFP:
    def test_lambda1(self):
        # VERIFIED: [DC] (2^1-1)/2^1 * (1/6)/2! = (1/2)*(1/6)*(1/2) = 1/24;
        # [LT] Faber-Pandharipande, int_{M-bar_{1,1}} psi_1 = 1/24.
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2(self):
        # VERIFIED: [DC] (2^3-1)/2^3 * (1/30)/4! = (7/8)*(1/30)*(1/24) = 7/5760;
        # [LT] Faber-Pandharipande lambda_2 = 7/5760.
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3(self):
        # VERIFIED: [DC] (2^5-1)/2^5 * (1/42)/6! = (31/32)*(1/42)*(1/720) = 31/967680;
        # [LT] Faber-Pandharipande values.
        assert lambda_fp(3) == Fraction(31, 967680)


class TestHarmonicNumber:
    def test_H1(self):
        # VERIFIED: [DC] H_1 = 1; [LC] trivial sum.
        assert harmonic_number(1) == Fraction(1)

    def test_H2(self):
        # VERIFIED: [DC] H_2 = 1 + 1/2 = 3/2; [NE] 1.5.
        assert harmonic_number(2) == Fraction(3, 2)

    def test_H3(self):
        # VERIFIED: [DC] H_3 = 1 + 1/2 + 1/3 = 11/6; [NE] 1.8333...
        assert harmonic_number(3) == Fraction(11, 6)

    def test_H4(self):
        # VERIFIED: [DC] H_4 = 1 + 1/2 + 1/3 + 1/4 = 25/12; [NE] 2.0833...
        assert harmonic_number(4) == Fraction(25, 12)

    def test_H_N_minus_1_not_H_Nminus1(self):
        """AP136: H_N - 1 != H_{N-1}. At N=2: H_2 - 1 = 1/2, H_1 = 1."""
        # VERIFIED: [DC] H_2 - 1 = 3/2 - 1 = 1/2; H_1 = 1; [CF] difference = 1/2.
        assert harmonic_number(2) - 1 != harmonic_number(1)
        assert harmonic_number(2) - 1 == Fraction(1, 2)
        assert harmonic_number(1) == Fraction(1)


# ============================================================================
# Kappa formulas
# ============================================================================

class TestKappaFormulas:
    def test_kappa_heisenberg_k1(self):
        # VERIFIED: [DC] kappa(Heis_1) = 1; [LT] landscape_census.tex.
        assert kappa_heisenberg(1) == Fraction(1)

    def test_kappa_heisenberg_k0(self):
        # VERIFIED: [DC] kappa(Heis_0) = 0; [LC] k=0 limit.
        assert kappa_heisenberg(0) == Fraction(0)

    def test_kappa_virasoro_c26(self):
        # VERIFIED: [DC] kappa(Vir_26) = 26/2 = 13; [LT] landscape_census.tex.
        assert kappa_virasoro(26) == Fraction(13)

    def test_kappa_virasoro_c13(self):
        # VERIFIED: [DC] kappa(Vir_13) = 13/2; [SY] self-dual point.
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_kappa_virasoro_c1(self):
        # VERIFIED: [DC] kappa(Vir_1) = 1/2; [LT] landscape_census.tex.
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_kappa_affine_sl2_k1(self):
        # VERIFIED: [DC] kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4;
        # [LT] landscape_census.tex: dim(sl_2)=3, h^v=2.
        assert kappa_affine_km(3, 2, 1) == Fraction(9, 4)

    def test_kappa_affine_sl2_k0(self):
        # VERIFIED: [DC] kappa(sl_2, k=0) = 3*(0+2)/(2*2) = 3/2;
        # [LC] k=0 gives dim(g)/2, NOT zero.
        assert kappa_affine_km(3, 2, 0) == Fraction(3, 2)

    def test_kappa_affine_sl2_critical(self):
        # VERIFIED: [DC] kappa(sl_2, k=-2) = 3*(-2+2)/(2*2) = 0;
        # [LT] critical level k=-h^v gives kappa=0.
        assert kappa_affine_km(3, 2, -2) == Fraction(0)

    def test_kappa_wn_W2_equals_virasoro(self):
        """kappa(W_2) = c*(H_2 - 1) = c/2 = kappa(Vir)."""
        # VERIFIED: [CF] W_2 = Vir, so kappa must match;
        # [DC] H_2 - 1 = 1/2, kappa = c/2.
        c = Fraction(10)
        assert kappa_wn(2, c) == kappa_virasoro(c)

    def test_kappa_wn_W3(self):
        # VERIFIED: [DC] H_3 - 1 = 5/6, kappa(W_3) = 5c/6;
        # [CF] at c=6: kappa = 5.
        assert kappa_wn(3, 6) == Fraction(5)

    def test_kappa_betagamma_half(self):
        # VERIFIED: [DC] 6*(1/4) - 6*(1/2) + 1 = 3/2 - 3 + 1 = -1/2;
        # [CF] matches depth_classification.py kappa_betagamma(1/2).
        assert kappa_betagamma(Fraction(1, 2)) == Fraction(-1, 2)

    def test_kappa_betagamma_1(self):
        # VERIFIED: [DC] 6 - 6 + 1 = 1; [LC] standard betagamma.
        assert kappa_betagamma(1) == Fraction(1)

    def test_kappa_betagamma_2(self):
        # VERIFIED: [DC] 6*4 - 6*2 + 1 = 24 - 12 + 1 = 13;
        # [CF] c_bg(2)/2 = 26/2 = 13.
        assert kappa_betagamma(2) == Fraction(13)


# ============================================================================
# Central charges: bc/betagamma complementarity
# ============================================================================

class TestCentralCharges:
    def test_c_betagamma_half(self):
        # VERIFIED: [DC] 2*(3/2 - 3 + 1) = 2*(-1/2) = -1; [LT] symplectic boson c=-1.
        assert c_betagamma(Fraction(1, 2)) == Fraction(-1)

    def test_c_betagamma_2(self):
        # VERIFIED: [DC] 2*(24 - 12 + 1) = 26; [LT] matter ghost c=26.
        assert c_betagamma(2) == Fraction(26)

    def test_c_bc_half(self):
        # VERIFIED: [DC] 1 - 3*0 = 1; [LT] single Dirac fermion c=1.
        assert c_bc(Fraction(1, 2)) == Fraction(1)

    def test_c_bc_2(self):
        # VERIFIED: [DC] 1 - 3*9 = -26; [LT] reparametrization ghost c=-26.
        assert c_bc(2) == Fraction(-26)

    @pytest.mark.parametrize("lam", [0, Fraction(1, 2), 1, 2, Fraction(3, 2)])
    def test_bc_bg_complementarity(self, lam):
        """c_bg + c_bc = 0 for all lambda."""
        # VERIFIED: [DC] algebraic identity; [SY] bosonization partner cancellation.
        assert c_betagamma(lam) + c_bc(lam) == Fraction(0)


# ============================================================================
# BP central charge and kappa
# ============================================================================

class TestBP:
    def test_c_bp_k_neg1(self):
        # VERIFIED: [DC] 2 - 24*0/2 = 2; [LC] k=-1 gives c=2.
        assert c_bp(-1) == Fraction(2)

    def test_c_bp_k0(self):
        # VERIFIED: [DC] 2 - 24*1/3 = 2 - 8 = -6; [LC] k=0 gives c=-6.
        assert c_bp(0) == Fraction(-6)

    @pytest.mark.parametrize("k_val", [0, 1, -1, 2, -2, 5, 10, -4])
    def test_koszul_conductor_196(self, k_val):
        """K_BP = c_BP(k) + c_BP(-k-6) = 196 for all k != -3."""
        # VERIFIED: [DC] algebraic cancellation c(k)+c(-k-6)=196;
        # [LT] eq:bp-conductor in bershadsky_polyakov.tex.
        k = Fraction(k_val)
        k_dual = -k - 6
        K = c_bp(k) + c_bp(k_dual)
        assert K == Fraction(196)

    def test_bp_self_dual_level(self):
        """Self-dual level k = -3 (fixed point of k -> -k-6)."""
        # VERIFIED: [DC] -(-3) - 6 = 3 - 6 = -3; [SY] involution fixed point.
        assert -Fraction(-3) - 6 == Fraction(-3)

    def test_kappa_bp_varrho(self):
        """kappa_BP = (1/6) * c_BP."""
        # VERIFIED: [DC] varrho = 1/6 from strong-generator sum;
        # [LT] prop:bp-kappa.
        for k_val in [0, 1, -1, 2, 5]:
            assert kappa_bp(k_val) == Fraction(1, 6) * c_bp(k_val)


# ============================================================================
# G/L/C/M classification
# ============================================================================

class TestClassification:
    def test_class_G(self):
        # VERIFIED: [DC] alpha=0, S4=0 -> G; [LT] thm:shadow-archetype-classification.
        cls, depth = classify_glcm(Fraction(0), Fraction(0))
        assert cls == 'G'
        assert depth == 2

    def test_class_L(self):
        # VERIFIED: [DC] alpha!=0, S4=0 -> L; [LT] thm:shadow-archetype-classification.
        cls, depth = classify_glcm(Fraction(1), Fraction(0))
        assert cls == 'L'
        assert depth == 3

    def test_class_C(self):
        # VERIFIED: [DC] alpha=0, S4!=0 -> C; [LT] thm:shadow-archetype-classification.
        cls, depth = classify_glcm(Fraction(0), Fraction(1))
        assert cls == 'C'
        assert depth == 4

    def test_class_M(self):
        # VERIFIED: [DC] alpha!=0, S4!=0 -> M; [LT] thm:shadow-archetype-classification.
        cls, depth = classify_glcm(Fraction(1), Fraction(1))
        assert cls == 'M'
        assert depth is None


# ============================================================================
# Shadow tower computation
# ============================================================================

class TestShadowTower:
    def test_class_G_tower_vanishes(self):
        """Class G: S_r = 0 for r >= 3."""
        # VERIFIED: [DC] alpha=0, S4=0 -> Q_L = 4*kappa^2, sqrt = 2*kappa,
        # all higher Taylor coefficients vanish; [LT] thm:single-line-dichotomy.
        coeffs = compute_shadow_tower(Fraction(1), Fraction(0), Fraction(0))
        assert coeffs[2] == Fraction(1)  # S_2 = kappa
        for r in range(3, 21):
            assert coeffs[r] == Fraction(0)

    def test_class_L_tower_terminates(self):
        """Class L: S_r = 0 for r >= 4."""
        # VERIFIED: [DC] S4=0 -> Q_L = 4*kappa^2 + 12*kappa*alpha*t + 9*alpha^2*t^2
        # = (2*kappa + 3*alpha*t)^2, sqrt = 2*kappa + 3*alpha*t,
        # so a_0 = 2*kappa, a_1 = 3*alpha, a_n = 0 for n >= 2;
        # [LT] thm:nms-finite-termination.
        kap = Fraction(9, 4)
        alpha = Fraction(1)
        coeffs = compute_shadow_tower(kap, alpha, Fraction(0))
        assert coeffs[2] == kap  # S_2 = kappa = a_0/2
        assert coeffs[3] == alpha  # S_3 = a_1/3 = 3*alpha/3 = alpha
        for r in range(4, 21):
            assert coeffs[r] == Fraction(0)

    def test_virasoro_S2(self):
        """S_2(Vir_c) = kappa = c/2."""
        c = Fraction(26)
        coeffs = compute_shadow_tower(
            kappa_virasoro(c), Fraction(2),
            Fraction(10) / (c * (5 * c + 22))
        )
        # VERIFIED: [DC] S_2 = a_0/2 = 2*kappa/2 = kappa; [CF] kappa(Vir_26) = 13.
        assert coeffs[2] == Fraction(13)

    def test_virasoro_S3(self):
        """S_3(Vir) = 2 (gravitational cubic)."""
        c = Fraction(26)
        coeffs = compute_shadow_tower(
            kappa_virasoro(c), Fraction(2),
            Fraction(10) / (c * (5 * c + 22))
        )
        # VERIFIED: [DC] a_1 = q_1/(2*a_0) = 12*13*2/(2*26) = 312/52 = 6,
        # S_3 = 6/3 = 2; [LT] virasoro_shadow_tower.py a_1=6, S_3=2.
        assert coeffs[3] == Fraction(2)

    def test_degenerate_kappa_zero(self):
        """kappa = 0: all shadow coefficients vanish."""
        coeffs = compute_shadow_tower(Fraction(0), Fraction(0), Fraction(0))
        for r in range(2, 21):
            assert coeffs[r] == Fraction(0)


# ============================================================================
# Heisenberg family tests
# ============================================================================

class TestHeisenberg:
    def test_k1_kappa(self):
        result = heisenberg(1)
        # VERIFIED: [DC] kappa(Heis_1) = 1; [LT] landscape_census.tex.
        assert result.kappa == Fraction(1)

    def test_k1_class(self):
        result = heisenberg(1)
        # VERIFIED: [DC] alpha=0, S4=0 -> G; [LT] thm:shadow-archetype-classification.
        assert result.depth_class == 'G'
        assert result.shadow_depth == 2

    def test_k1_discriminant(self):
        result = heisenberg(1)
        # VERIFIED: [DC] Delta = 8*1*0 = 0; [DA] S_4=0 for abelian.
        assert result.discriminant == Fraction(0)

    def test_k1_F1(self):
        result = heisenberg(1)
        # VERIFIED: [DC] F_1 = kappa/24 = 1/24; [CF] universal F_1 formula.
        assert result.F(1) == Fraction(1, 24)

    def test_k1_koszul_conductor(self):
        result = heisenberg(1)
        # VERIFIED: [DC] K = 0 for Heisenberg; [LT] KM family K=0.
        assert result.koszul_conductor == Fraction(0)

    def test_k1_tower_vanishes(self):
        result = heisenberg(1)
        # VERIFIED: [DC] class G, all S_r = 0 for r >= 3; [LT] abelian OPE.
        for r in range(3, 21):
            assert result.S(r) == Fraction(0)

    def test_k0_kappa(self):
        result = heisenberg(0)
        # VERIFIED: [DC] kappa(Heis_0) = 0; [LC] k=0 limit.
        assert result.kappa == Fraction(0)

    def test_k0_class(self):
        result = heisenberg(0)
        # VERIFIED: [DC] alpha=0, S4=0 -> G; [LC] degenerate case.
        assert result.depth_class == 'G'

    def test_k0_F1(self):
        result = heisenberg(0)
        # VERIFIED: [DC] F_1 = 0/24 = 0; [LC] kappa=0 -> uncurved.
        assert result.F(1) == Fraction(0)

    def test_delta_F2_cross_zero(self):
        result = heisenberg(1)
        # VERIFIED: [DC] single generator -> no mixed channels;
        # [DA] delta_F_2^cross = 0 for single-generator algebras.
        assert result.delta_F2_cross == Fraction(0)


# ============================================================================
# Virasoro family tests
# ============================================================================

class TestVirasoro:
    def test_c26_kappa(self):
        result = virasoro(26)
        # VERIFIED: [DC] kappa(Vir_26) = 26/2 = 13; [LT] landscape_census.tex.
        assert result.kappa == Fraction(13)

    def test_c26_class(self):
        result = virasoro(26)
        # VERIFIED: [DC] alpha=2!=0, S4!=0 -> M; [LT] thm:shadow-archetype-classification.
        assert result.depth_class == 'M'
        assert result.shadow_depth is None  # infinity

    def test_c26_koszul_conductor(self):
        result = virasoro(26)
        # VERIFIED: [DC] K = c/2 + (26-c)/2 = 13 for all c;
        # [SY] Virasoro duality Vir^! = Vir_{26-c}.
        assert result.koszul_conductor == Fraction(13)

    def test_c13_self_dual(self):
        """Virasoro self-dual at c=13, NOT c=26."""
        result = virasoro(13)
        # VERIFIED: [DC] kappa(13) = 13/2, kappa(26-13) = 13/2 -> self-dual;
        # [SY] fixed point of c -> 26-c.
        assert result.kappa == Fraction(13, 2)
        assert result.kappa_dual == Fraction(13, 2)
        assert result.kappa == result.kappa_dual

    def test_c26_not_self_dual(self):
        """c=26 is NOT the self-dual point."""
        result = virasoro(26)
        # VERIFIED: [DC] kappa(26) = 13, kappa(0) = 0 -> not equal;
        # [CF] self-dual at c=13, not c=26.
        assert result.kappa != result.kappa_dual

    def test_c1_kappa(self):
        result = virasoro(1)
        # VERIFIED: [DC] kappa(Vir_1) = 1/2; [LT] landscape_census.tex.
        assert result.kappa == Fraction(1, 2)

    def test_c1_F1(self):
        result = virasoro(1)
        # VERIFIED: [DC] F_1 = (1/2)/24 = 1/48; [CF] universal F_1 = kappa/24.
        assert result.F(1) == Fraction(1, 48)

    def test_c26_F1(self):
        result = virasoro(26)
        # VERIFIED: [DC] F_1 = 13/24; [CF] universal F_1 = kappa/24.
        assert result.F(1) == Fraction(13, 24)

    def test_delta_F2_cross_zero(self):
        result = virasoro(26)
        # VERIFIED: [DC] single generator T -> no mixed channels;
        # [DA] delta_F_2^cross = 0 for single-generator algebras.
        assert result.delta_F2_cross == Fraction(0)

    def test_virasoro_S4(self):
        """S_4(Vir_c) = 10/[c*(5c+22)]."""
        c = Fraction(1)
        result = virasoro(c)
        # VERIFIED: [DC] 10/(1*27) = 10/27; [LT] virasoro_shadow_tower.py.
        expected = Fraction(10) / (c * (5 * c + 22))
        assert result.S4 == expected

    def test_virasoro_discriminant(self):
        """Delta = 8*kappa*S_4 = 40/(5c+22)."""
        c = Fraction(1)
        result = virasoro(c)
        # VERIFIED: [DC] Delta = 8*(1/2)*(10/27) = 40/27;
        # [CF] matches 40/(5*1+22) = 40/27.
        expected = Fraction(40) / (5 * c + 22)
        assert result.discriminant == expected

    def test_nonzero_tower(self):
        """Virasoro class M: S_r != 0 for all r >= 2 (at generic c)."""
        result = virasoro(26)
        # VERIFIED: [DC] class M has infinite tower;
        # [LT] thm:single-line-dichotomy.
        for r in range(2, 11):
            assert result.S(r) != Fraction(0), f"S_{r} should be nonzero"


# ============================================================================
# Affine sl_2 tests
# ============================================================================

class TestAffineSl2:
    def test_k1_kappa(self):
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] 3*(1+2)/(2*2) = 9/4; [LT] landscape_census.tex.
        assert result.kappa == Fraction(9, 4)

    def test_k1_class(self):
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] alpha!=0, S4=0 -> L; [LT] thm:nms-finite-termination.
        assert result.depth_class == 'L'
        assert result.shadow_depth == 3

    def test_k1_koszul_conductor(self):
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] K = kappa(k) + kappa(-k-2*h^v) = 0;
        # [SY] KM family has universal K=0.
        assert result.koszul_conductor == Fraction(0)

    def test_k0_kappa_not_zero(self):
        """k=0 gives kappa = dim(g)/2, NOT zero."""
        result = affine_km(0, 'sl2')
        # VERIFIED: [DC] 3*(0+2)/(2*2) = 3/2;
        # [LT] k=0 is abelian limit, kappa = dim(g)/2.
        assert result.kappa == Fraction(3, 2)
        assert result.kappa != Fraction(0)

    def test_critical_kappa_zero(self):
        """k = -h^v = -2 (critical level): kappa = 0."""
        result = affine_km(-2, 'sl2')
        # VERIFIED: [DC] 3*(-2+2)/(2*2) = 0;
        # [LT] critical level k=-h^v gives kappa=0.
        assert result.kappa == Fraction(0)

    def test_k1_discriminant_zero(self):
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] Delta = 8*kappa*0 = 0; [DA] S_4=0 for KM (Jacobi).
        assert result.discriminant == Fraction(0)

    def test_k1_F1(self):
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] F_1 = (9/4)/24 = 9/96 = 3/32;
        # [CF] universal F_1 = kappa/24.
        assert result.F(1) == Fraction(9, 4) / 24

    def test_tower_terminates_at_3(self):
        """Class L: S_r = 0 for r >= 4."""
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] S_4=0 -> Q_L is perfect square -> sqrt is linear;
        # [LT] thm:nms-finite-termination.
        for r in range(4, 21):
            assert result.S(r) == Fraction(0)

    def test_kappa_dual_sum_zero(self):
        """kappa(k) + kappa(k') = 0 for KM dual level k' = -k - 2*h^v."""
        result = affine_km(1, 'sl2')
        # VERIFIED: [DC] kappa(1) + kappa(-5) = 9/4 + 3*(-5+2)/(2*2) = 9/4 - 9/4 = 0;
        # [SY] KM complementarity K=0.
        assert result.kappa + result.kappa_dual == Fraction(0)


# ============================================================================
# W_3 tests
# ============================================================================

class TestW3:
    def test_kappa(self):
        c = Fraction(50)
        result = w3_algebra(c)
        # VERIFIED: [DC] kappa(W_3) = 5*50/6 = 250/6 = 125/3;
        # [CF] H_3 - 1 = 5/6.
        assert result.kappa == Fraction(125, 3)

    def test_kappa_W3_formula(self):
        """kappa(W_3) = 5c/6."""
        # VERIFIED: [DC] H_3 - 1 = 5/6, kappa = 5c/6;
        # [CF] kappa_wn(3, c) matches direct computation.
        for c_val in [1, 6, 10, 50, 100]:
            c = Fraction(c_val)
            assert kappa_wn(3, c) == 5 * c / 6

    def test_class(self):
        result = w3_algebra(50)
        # VERIFIED: [DC] alpha!=0, S4!=0 -> M; [LT] thm:shadow-archetype-classification.
        assert result.depth_class == 'M'
        assert result.shadow_depth is None

    def test_koszul_conductor(self):
        result = w3_algebra(50)
        # VERIFIED: [DC] K = 5c/6 + 5(100-c)/6 = 500/6 = 250/3;
        # [LT] w3_shadow_tower_engine.py Koszul duality.
        assert result.koszul_conductor == Fraction(250, 3)

    def test_koszul_conductor_level_independent(self):
        """K(W_3) = 250/3 for all c."""
        # VERIFIED: [DC] 5c/6 + 5(100-c)/6 = 500/6 = 250/3;
        # [SY] K is constant under c -> 100-c.
        for c_val in [1, 10, 50, 99]:
            result = w3_algebra(c_val)
            assert result.koszul_conductor == Fraction(250, 3)

    def test_generators(self):
        result = w3_algebra(50)
        # VERIFIED: [DC] W_3 has generators T(h=2) and W(h=3);
        # [LT] W_N weight range {2,...,N}.
        assert result.generator_weights == [Fraction(2), Fraction(3)]


# ============================================================================
# betagamma tests
# ============================================================================

class TestBetagamma:
    def test_lambda_half_c(self):
        result = betagamma(Fraction(1, 2))
        # VERIFIED: [DC] c_bg(1/2) = 2*(3/2-3+1) = -1; [LT] symplectic boson.
        assert result.central_charge == Fraction(-1)

    def test_lambda_half_kappa(self):
        result = betagamma(Fraction(1, 2))
        # VERIFIED: [DC] kappa = 6*(1/4) - 3 + 1 = -1/2;
        # [CF] matches depth_classification.py.
        assert result.kappa == Fraction(-1, 2)

    def test_lambda_half_class(self):
        result = betagamma(Fraction(1, 2))
        # VERIFIED: [DC] alpha=0, S4!=0 -> C; [LT] stratum separation.
        assert result.depth_class == 'C'
        assert result.shadow_depth == 4

    def test_lambda2_c(self):
        result = betagamma(2)
        # VERIFIED: [DC] c_bg(2) = 2*(24-12+1) = 26; [LT] matter ghost.
        assert result.central_charge == Fraction(26)

    def test_lambda2_bc_cancellation(self):
        """c_bg(2) + c_bc(2) = 0 (string ghost cancellation)."""
        # VERIFIED: [DC] 26 + (-26) = 0; [LT] string theory ghost cancellation.
        assert c_betagamma(2) + c_bc(2) == Fraction(0)

    def test_koszul_conductor_zero(self):
        result = betagamma(Fraction(1, 2))
        # VERIFIED: [DC] K = 0 from c_bg + c_bc = 0;
        # [SY] complementarity.
        assert result.koszul_conductor == Fraction(0)

    def test_delta_F2_cross_zero(self):
        result = betagamma(Fraction(1, 2))
        # VERIFIED: [DC] diagonal metric -> no mixed channels;
        # [DA] single-weight-line algebra.
        assert result.delta_F2_cross == Fraction(0)


# ============================================================================
# Bershadsky-Polyakov tests
# ============================================================================

class TestBershadsky:
    def test_koszul_conductor_196(self):
        """K_BP = 196 for all k."""
        # VERIFIED: [DC] c(k) + c(-k-6) = 196; [LT] eq:bp-conductor.
        for k_val in [0, 1, -1, 2, 5]:
            result = bershadsky_polyakov(k_val)
            assert result.koszul_conductor == Fraction(196)

    def test_k0_kappa(self):
        result = bershadsky_polyakov(0)
        # VERIFIED: [DC] c_BP(0) = 2 - 24/3 = -6, kappa = -6/6 = -1;
        # [CF] bp_koszul_conductor_engine.py.
        assert result.kappa == Fraction(-1)

    def test_generators(self):
        result = bershadsky_polyakov(0)
        # VERIFIED: [DC] BP generators J(1), G+(3/2), G-(3/2), T(2);
        # [LT] Fehily-Kawasetsu-Ridout.
        assert result.generator_weights == [
            Fraction(1), Fraction(3, 2), Fraction(3, 2), Fraction(2)
        ]

    def test_kappa_complementarity(self):
        """kappa_BP(k) + kappa_BP(-k-6) = 98/3."""
        # VERIFIED: [DC] (1/6)*196 = 98/3;
        # [LT] eq:bp-complementarity.
        for k_val in [0, 1, 2, 5]:
            r1 = bershadsky_polyakov(k_val)
            assert r1.kappa + r1.kappa_dual == Fraction(98, 3)

    def test_class_M(self):
        result = bershadsky_polyakov(0)
        # VERIFIED: [DC] alpha=2!=0, S4!=0 -> M;
        # [LT] BP contains Virasoro subalgebra.
        assert result.depth_class == 'M'


# ============================================================================
# Cross-family universality tests
# ============================================================================

class TestCrossFamily:
    def test_F1_universal(self):
        """F_1 = kappa/24 for ALL families."""
        # VERIFIED: [DC] universal genus-1 formula;
        # [LT] thm:theorem-d (UNIFORM-WEIGHT, unconditional at g=1).
        families = [
            heisenberg(1),
            virasoro(26),
            affine_km(1, 'sl2'),
            w3_algebra(50),
            betagamma(1),
            bershadsky_polyakov(0),
        ]
        for result in families:
            expected = result.kappa / 24
            assert result.F(1) == expected, (
                f"{result.name}: F_1 = {result.F(1)}, expected {expected}"
            )

    def test_discriminant_formula(self):
        """Delta = 8 * kappa * S_4 for all families."""
        # VERIFIED: [DC] Delta = 8*kappa*S_4 by definition;
        # [DA] Delta is LINEAR in kappa (AP21).
        families = [
            heisenberg(1),
            virasoro(26),
            affine_km(1, 'sl2'),
            w3_algebra(50),
            betagamma(1),
            bershadsky_polyakov(0),
        ]
        for result in families:
            expected = 8 * result.kappa * result.S4
            assert result.discriminant == expected, (
                f"{result.name}: Delta = {result.discriminant}, expected {expected}"
            )

    def test_discriminant_zero_class_G(self):
        """Heisenberg (class G): Delta = 0."""
        # VERIFIED: [DC] S_4 = 0 -> Delta = 0; [DA] abelian OPE.
        result = heisenberg(1)
        assert result.discriminant == Fraction(0)

    def test_discriminant_zero_class_L(self):
        """Affine KM (class L): Delta = 0."""
        # VERIFIED: [DC] S_4 = 0 -> Delta = 0; [DA] Jacobi identity.
        result = affine_km(1, 'sl2')
        assert result.discriminant == Fraction(0)

    def test_discriminant_nonzero_class_M(self):
        """Virasoro (class M): Delta != 0."""
        # VERIFIED: [DC] S_4 = 10/[c(5c+22)] != 0 for generic c;
        # [LT] thm:single-line-dichotomy.
        result = virasoro(26)
        assert result.discriminant != Fraction(0)

    def test_delta_F2_cross_single_generator(self):
        """delta_F_2^cross = 0 for all single-generator algebras."""
        # VERIFIED: [DC] single channel -> all amplitudes diagonal;
        # [DA] no mixed-channel graphs possible.
        for result in [heisenberg(1), virasoro(26)]:
            assert result.delta_F2_cross == Fraction(0), (
                f"{result.name}: delta_F2_cross should be 0"
            )


# ============================================================================
# Free energy values
# ============================================================================

class TestFreeEnergies:
    def test_F2_value(self):
        """F_2 = kappa * 7/5760 (UNIFORM-WEIGHT)."""
        # VERIFIED: [DC] lambda_2 = 7/5760; [LT] Faber-Pandharipande.
        result = virasoro(26)
        expected = Fraction(13) * Fraction(7, 5760)
        assert result.F(2) == expected

    def test_F3_value(self):
        """F_3 = kappa * 31/967680."""
        # VERIFIED: [DC] lambda_3 = 31/967680; [LT] Faber-Pandharipande.
        result = virasoro(26)
        expected = Fraction(13) * Fraction(31, 967680)
        assert result.F(3) == expected

    def test_all_Fg_proportional_to_kappa(self):
        """F_g = kappa * lambda_g for all g (UNIFORM-WEIGHT)."""
        # VERIFIED: [DC] by construction of compute_free_energies;
        # [LT] thm:theorem-d.
        for c_val in [1, 13, 26]:
            result = virasoro(c_val)
            kap = kappa_virasoro(c_val)
            for g in range(1, 6):
                assert result.F(g) == kap * lambda_fp(g)


# ============================================================================
# Generic constructor tests
# ============================================================================

class TestFromData:
    def test_custom_algebra(self):
        """Test from_data with custom shadow data."""
        result = from_data(
            name="Custom",
            c=10,
            kappa=5,
            generator_weights=[2],
            alpha=1,
            S4=Fraction(1, 10),
            koszul_conductor=7,
        )
        assert result.kappa == Fraction(5)
        assert result.discriminant == 8 * Fraction(5) * Fraction(1, 10)
        assert result.discriminant == Fraction(4)
        assert result.depth_class == 'M'

    def test_custom_class_G(self):
        result = from_data("Test G", c=1, kappa=1, generator_weights=[1],
                           alpha=0, S4=0)
        assert result.depth_class == 'G'
        assert result.shadow_depth == 2


# ============================================================================
# Lie algebra data consistency
# ============================================================================

class TestLieData:
    def test_sl2_data(self):
        """sl_2: dim=3, h^v=2."""
        # VERIFIED: [DC] dim(sl_2)=3 (e,f,h); [LT] standard reference.
        result = affine_km(1, 'sl2')
        assert result.kappa == Fraction(9, 4)  # 3*(1+2)/(2*2)

    def test_sl3_data(self):
        """sl_3: dim=8, h^v=3."""
        # VERIFIED: [DC] dim(sl_3)=8; [LT] standard reference.
        result = affine_km(1, 'sl3')
        expected = Fraction(8) * (1 + 3) / (2 * 3)
        assert result.kappa == expected  # 8*4/6 = 16/3

    def test_e8_data(self):
        """E_8: dim=248, h^v=30."""
        # VERIFIED: [DC] dim(E_8)=248 (adjoint=omega_1);
        # [LT] standard reference.
        result = affine_km(1, 'E8')
        expected = Fraction(248) * (1 + 30) / (2 * 30)
        assert result.kappa == expected  # 248*31/60 = 7688/60 = 1922/15
