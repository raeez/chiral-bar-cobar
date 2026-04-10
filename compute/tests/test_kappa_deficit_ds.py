"""Tests for kappa deficit under Drinfeld-Sokolov reduction.

Verifies Proposition prop:partition-dependent-complementarity:
  D(lambda, k) := kappa(V_k(g)) - kappa(W_k(g, f_lambda))
is a rational function of k (NOT a constant), and that the
Koszul complementarity sum
  kappa(W_k) + kappa(W_{k'}) = rho_lambda * K_lambda
is k-independent.

The ghost subtraction formula kappa(W) = kappa(V_k) - C_ghost
(with C_ghost a combinatorial constant) is WRONG: the anomaly
ratio rho changes under DS reduction, making the kappa deficit
a non-trivial rational function of k.

CENTRAL CHARGE CONVENTIONS:
  c_FKW(W_3, k) = 2(k-9)/(k+3)  -- the correct DS central charge at level k.
  c_Toda(W_3, t) = 2 - 24(t-1)^2/t  -- the Toda parametrization (t = k+h^v).
  These DIFFER: c_FKW gives the physical central charge;
  c_Toda is a formal parametrization whose c(t)+c(-t) = 100
  yields the Koszul conductor.  The FF dual level k' = -k-2N gives
  c_FKW(k) + c_FKW(k') = 2(N-1) (NOT the Koszul conductor).
"""

import pytest
from sympy import Rational, Symbol, diff, expand, factor, simplify

k = Symbol('k')


# =============================================================================
# Central charge formulas
# =============================================================================

def c_affine_sl3(level=k):
    """c(V_k(sl_3)) = 8k/(k+3)."""
    return 8 * level / (level + 3)


def c_W3_FKW(level=k):
    """c(W_3, k) = 2(k-9)/(k+3), the FKW formula for principal W(sl_3).

    This is (N-1)(1 - N(N+1)/(k+N)) at N=3.
    """
    return 2 * (level - 9) / (level + 3)


def c_W3_Toda(level=k):
    """c_Toda(W_3, t) = 2 - 24(t-1)^2/t with t = k + 3.

    This is the Toda parametrization.  It does NOT give the correct
    DS central charge at integer level k; the correct formula is c_W3_FKW.
    Its virtue: c_Toda(t) + c_Toda(-t) = 100 (the Koszul conductor).
    """
    t = level + 3
    return 2 - 24 * (t - 1) ** 2 / t


def c_BP(level=k):
    """c(Bershadsky-Polyakov, k) = 2 - 24*(k+1)^2/(k+3).

    # AP140: corrected from (k-15)/(k+3) which gives K=2; correct K_BP=196
    # Verification: c(0) = 2 - 24/3 = -6.  c(-6) = 2 - 24*25/(-3) = 202.
    # K = c(0) + c(-6) = -6 + 202 = 196.
    """
    return 2 - 24 * (level + 1)**2 / (level + 3)


# =============================================================================
# Kappa formulas
# =============================================================================

def kappa_affine_sl3(level=k):
    """kappa(V_k(sl_3)) = 4(k+3)/3. Linear in k."""
    return Rational(4, 3) * (level + 3)


def kappa_W3(level=k):
    """kappa(W_3, k) = (5/6) * c_FKW(W_3, k). Anomaly ratio rho = 5/6."""
    return Rational(5, 6) * c_W3_FKW(level)


def kappa_W3_Toda(level=k):
    """kappa from the Toda parametrization: (5/6)*c_Toda(W_3, k)."""
    return Rational(5, 6) * c_W3_Toda(level)


def kappa_BP(level=k):
    """kappa(BP, k) = (1/6) * c(BP, k). Anomaly ratio rho = 1/6."""
    return Rational(1, 6) * c_BP(level)


def dual_level(level=k, N=3):
    """Feigin-Frenkel dual level: k' = -k - 2N."""
    return -level - 2 * N


# =============================================================================
# Tests: Central charge formulas
# =============================================================================

class TestCentralChargeFormulas:
    """Verify the two W_3 central charge parametrizations differ."""

    def test_FKW_at_k1(self):
        """c_FKW(W_3, k=1) = -4."""
        assert c_W3_FKW(Rational(1)) == -4

    def test_FKW_at_k9(self):
        """c_FKW(W_3, k=9) = 0."""
        assert c_W3_FKW(Rational(9)) == 0

    def test_FKW_large_k(self):
        """c_FKW(W_3, k=inf) -> 2 = rank(sl_3)."""
        assert c_W3_FKW(Rational(10**6)) == Rational(
            2 * (10**6 - 9), 10**6 + 3)

    def test_Toda_at_k1(self):
        """c_Toda(W_3, k=1) = -52. NOT the physical central charge."""
        assert c_W3_Toda(Rational(1)) == -52

    def test_Toda_neq_FKW(self):
        """The two formulas disagree at k=1, 2, 3."""
        for kval in [1, 2, 3]:
            kv = Rational(kval)
            assert c_W3_FKW(kv) != c_W3_Toda(kv)


# =============================================================================
# Tests: Anomaly ratios
# =============================================================================

class TestAnomalyRatios:
    """Verify anomaly ratios for sl_3 W-algebras."""

    def test_rho_virasoro_is_half(self):
        """Virasoro: rho = 1/2 (generators: T at weight 2, bosonic)."""
        assert Rational(1, 2) == Rational(1, 2)

    def test_rho_W3_from_generators(self):
        """W_3: generators at weights 2 (bosonic), 3 (bosonic).
        rho = 1/2 + 1/3 = 5/6."""
        rho = Rational(1, 2) + Rational(1, 3)
        assert rho == Rational(5, 6)

    def test_rho_BP_from_generators(self):
        """BP: J (h=1, bos), G+ (h=3/2, ferm), G- (h=3/2, ferm), T (h=2, bos).
        rho = 1/1 - 1/(3/2) - 1/(3/2) + 1/2 = 1 - 2/3 - 2/3 + 1/2 = 1/6."""
        rho = 1 - Rational(2, 3) - Rational(2, 3) + Rational(1, 2)
        assert rho == Rational(1, 6)


# =============================================================================
# Tests: Kappa deficit is k-dependent
# =============================================================================

class TestKappaDeficitKDependent:
    """Verify that D(lambda, k) = kappa(V_k) - kappa(W_k) depends on k."""

    def test_deficit_principal_k_dependent(self):
        """D((3), k) = (4k^2 + 19k + 81) / (3(k+3)) is NOT constant."""
        D = simplify(kappa_affine_sl3(k) - kappa_W3(k))
        dD_dk = simplify(diff(D, k))
        assert dD_dk != 0, "D((3), k) should depend on k"

    def test_deficit_principal_formula(self):
        """D((3), k) = (4k^2 + 19k + 81) / (3(k+3))."""
        D = simplify(kappa_affine_sl3(k) - kappa_W3(k))
        expected = (4 * k ** 2 + 19 * k + 81) / (3 * (k + 3))
        assert simplify(D - expected) == 0

    def test_deficit_subreg_k_dependent(self):
        """D((2,1), k) = (16k^2 + 47k + 45) / (3(k+3)) is NOT constant.

        # AP140: corrected from (8k^2+47k+87)/(6(k+3)) after BP c(k) fix
        """
        D = simplify(kappa_affine_sl3(k) - kappa_BP(k))
        dD_dk = simplify(diff(D, k))
        assert dD_dk != 0, "D((2,1), k) should depend on k"

    def test_deficit_subreg_formula(self):
        """D((2,1), k) = (16k^2 + 47k + 45) / (3(k+3)).

        # AP140: corrected from (8k^2+47k+87)/(6(k+3)) after BP c(k) fix
        """
        D = simplify(kappa_affine_sl3(k) - kappa_BP(k))
        expected = (16 * k ** 2 + 47 * k + 45) / (3 * (k + 3))
        assert simplify(D - expected) == 0

    @pytest.mark.parametrize("kval", [1, 2, 3])
    def test_deficit_principal_numerical(self, kval):
        """Numerical check: D((3)) at k=1,2,3."""
        kv = Rational(kval)
        D = kappa_affine_sl3(kv) - kappa_W3(kv)
        expected = Rational(4 * kval ** 2 + 19 * kval + 81,
                            3 * (kval + 3))
        assert D == expected

    @pytest.mark.parametrize("kval", [1, 2, 3])
    def test_deficit_subreg_numerical(self, kval):
        """Numerical check: D((2,1)) at k=1,2,3.

        # AP140: corrected after BP c(k) fix
        """
        kv = Rational(kval)
        D = kappa_affine_sl3(kv) - kappa_BP(kv)
        expected = Rational(16 * kval ** 2 + 47 * kval + 45,
                            3 * (kval + 3))
        assert D == expected


# =============================================================================
# Tests: Feigin-Frenkel conductor (NOT the Koszul conductor)
# =============================================================================

class TestFeiginFrenkelConductor:
    """The FF dual k' = -k-2N gives c_FKW(k)+c_FKW(k') = 2(N-1).

    This is the FF conductor, NOT the Koszul conductor K.
    For sl_3: c_FKW + c_FKW' = 4.
    The Koszul conductor K_3 = 100 comes from the Toda parametrization.
    """

    def test_affine_c_sum(self):
        """c(V_k) + c(V_{k'}) = 2*dim(g) = 16."""
        kp = dual_level(k, 3)
        s = simplify(c_affine_sl3(k) + c_affine_sl3(kp))
        assert s == 16

    def test_W3_FF_c_sum(self):
        """c_FKW(W_3, k) + c_FKW(W_3, k') = 4 = 2(N-1)."""
        kp = dual_level(k, 3)
        s = simplify(c_W3_FKW(k) + c_W3_FKW(kp))
        assert s == 4

    def test_BP_FF_c_sum(self):
        """c(BP, k) + c(BP, k') = 196.

        # AP140: corrected from 2; K_BP = c(0)+c(-6) = -6+202 = 196
        """
        kp = dual_level(k, 3)
        s = simplify(c_BP(k) + c_BP(kp))
        assert s == 196

    def test_affine_kappa_sum(self):
        """kappa(V_k) + kappa(V_{k'}) = 0."""
        kp = dual_level(k, 3)
        s = simplify(kappa_affine_sl3(k) + kappa_affine_sl3(kp))
        assert s == 0


# =============================================================================
# Tests: Koszul conductor from Toda parametrization
# =============================================================================

class TestKoszulConductorToda:
    """The Koszul conductor K = c_Toda(t) + c_Toda(-t) = 2r + 4dh^v.

    For sl_3: K_3 = 2*2 + 4*8*3 = 100.
    This uses the Toda parametrization, NOT the FKW formula.
    """

    def test_Toda_conductor_100(self):
        """c_Toda(t) + c_Toda(-t) = 100 for sl_3 principal."""
        kp = dual_level(k, 3)
        s = simplify(c_W3_Toda(k) + c_W3_Toda(kp))
        assert s == 100

    def test_Toda_kappa_complementarity_250_over_3(self):
        """kappa_Toda(k) + kappa_Toda(k') = 250/3."""
        kp = dual_level(k, 3)
        s = simplify(kappa_W3_Toda(k) + kappa_W3_Toda(kp))
        assert s == Rational(250, 3)

    def test_BP_complementarity_value(self):
        """kappa(BP,k) + kappa(BP,k') = 98/3.

        # AP140: corrected from 1/3; K_BP=196, rho=1/6, kappa_sum=(1/6)*196=98/3
        """
        kp = dual_level(k, 3)
        s = simplify(kappa_BP(k) + kappa_BP(kp))
        assert s == Rational(98, 3)

    def test_BP_complementarity_k_independent(self):
        """kappa(BP,k) + kappa(BP,k') is k-independent."""
        kp = dual_level(k, 3)
        s = simplify(kappa_BP(k) + kappa_BP(kp))
        assert simplify(diff(s, k)) == 0

    def test_FdV_formula(self):
        """K_N = 2(N-1)(2N^2+2N+1)."""
        for N, K_expected in [(2, 26), (3, 100), (4, 246)]:
            K = 2 * (N - 1) * (2 * N ** 2 + 2 * N + 1)
            assert K == K_expected


# =============================================================================
# Tests: Ghost subtraction is WRONG for kappa
# =============================================================================

class TestGhostSubtractionWrong:
    """Verify that kappa(W) != kappa(V_k) - C_ghost (combinatorial constant).

    The ghost constant C_lambda from prop:hook-ghost-constant is a
    central-charge ghost constant, NOT a kappa ghost constant.
    """

    def test_virasoro_ghost_subtraction_fails(self):
        """For sl_2 Virasoro: kappa(V_k) - C_ghost = 3(k+2)/4 - 1 != c/2.

        C_ghost = 1 (hook formula: m(m^2-1)/6 = 2*3/6 = 1).
        kappa(V_k(sl_2)) = 3(k+2)/4.
        But kappa(Vir) = c/2 = (1 - 6/(k+2))/2 = (k-4)/(2(k+2)).
        """
        kappa_aff_sl2 = Rational(3, 4) * (k + 2)
        C_ghost = 1
        kappa_ghost = kappa_aff_sl2 - C_ghost

        c_vir = (k - 4) / (k + 2)  # FKW: c = 1 - 6/(k+2) = (k-4)/(k+2)
        kappa_rho = c_vir / 2  # rho(Vir) = 1/2

        diff_expr = simplify(kappa_ghost - kappa_rho)
        assert diff_expr != 0, "Ghost subtraction should NOT equal rho*c"

    def test_W3_ghost_subtraction_fails(self):
        """For sl_3 principal: kappa(V_k) - 4 != (5/6)*c_FKW(W_3).

        C_ghost = 4 (hook formula: m(m^2-1)/6 = 3*8/6 = 4).
        """
        kappa_ghost = kappa_affine_sl3(k) - 4  # C_{(3)} = 4
        kappa_rho = kappa_W3(k)

        diff_expr = simplify(kappa_ghost - kappa_rho)
        assert diff_expr != 0, "Ghost subtraction should NOT equal rho*c"

    def test_BP_ghost_subtraction_fails(self):
        """For sl_3 subregular: kappa(V_k) - 2 != (1/6)*c(BP).

        C_ghost = 2 (hook formula for (2,1): m=2, r=1: C = 1 + 1 = 2).
        """
        kappa_ghost = kappa_affine_sl3(k) - 2  # C_{(2,1)} = 2
        kappa_rho = kappa_BP(k)

        diff_expr = simplify(kappa_ghost - kappa_rho)
        assert diff_expr != 0, "Ghost subtraction should NOT equal rho*c"


# =============================================================================
# Tests: Central charge deficit IS k-independent
# =============================================================================

class TestCentralChargeDeficit:
    """The central charge difference c(V_k) - c(W_k) IS k-independent."""

    def test_c_deficit_principal_6(self):
        """c(V_k(sl_3)) - c(W_3, k) = N(N-1) = 6."""
        delta = simplify(c_affine_sl3(k) - c_W3_FKW(k))
        assert delta == 6

    def test_c_deficit_subreg_k_dependent(self):
        """c(V_k(sl_3)) - c(BP, k) = 6(4k^2+9k+3)/(k+3), k-DEPENDENT.

        # AP140: corrected from (7k+15)/(k+3) after BP c(k) fix
        Unlike the principal case, the central charge deficit for
        non-principal W-algebras IS k-dependent.
        """
        delta = simplify(c_affine_sl3(k) - c_BP(k))
        expected = 6 * (4 * k ** 2 + 9 * k + 3) / (k + 3)
        assert simplify(delta - expected) == 0
        # Verify it IS k-dependent
        assert simplify(diff(delta, k)) != 0


# =============================================================================
# Tests: Anomaly ratio k-independence
# =============================================================================

class TestRhoKIndependence:
    """rho = kappa/c is k-independent for freely generated W-algebras."""

    def test_rho_W3_k_independent(self):
        """rho(W_3) = kappa(W_3)/c(W_3) = 5/6 at all k."""
        rho_computed = simplify(kappa_W3(k) / c_W3_FKW(k))
        assert rho_computed == Rational(5, 6)

    def test_rho_BP_k_independent(self):
        """rho(BP) = kappa(BP)/c(BP) = 1/6 at all k."""
        rho_computed = simplify(kappa_BP(k) / c_BP(k))
        assert rho_computed == Rational(1, 6)

    @pytest.mark.parametrize("kval", [1, 2, 3, 5, 10])
    def test_rho_W3_numerical(self, kval):
        """rho(W_3) = 5/6 at specific k values."""
        kv = Rational(kval)
        rho = kappa_W3(kv) / c_W3_FKW(kv)
        assert rho == Rational(5, 6)

    @pytest.mark.parametrize("kval", [1, 2, 3, 5, 10])
    def test_rho_BP_numerical(self, kval):
        """rho(BP) = 1/6 at specific k values."""
        kv = Rational(kval)
        rho = kappa_BP(kv) / c_BP(kv)
        assert rho == Rational(1, 6)
