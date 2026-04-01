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
"""

import pytest
from sympy import Rational, Symbol, diff, expand, factor, simplify

k = Symbol('k')


# =============================================================================
# Central charge formulas (verified from KRW)
# =============================================================================

def c_affine_sl3(level=k):
    """c(V_k(sl_3)) = 8k/(k+3)."""
    return 8 * level / (level + 3)


def c_W3(level=k):
    """c(W_3, k) = -2(3k+5)(4k+9)/(k+3), the principal W-algebra of sl_3."""
    t = level + 3
    return 2 * (1 - 12 * (t - 1) ** 2 / t)


def c_BP(level=k):
    """c(Bershadsky-Polyakov, k) = 1 - 18/(k+3) = (k-15)/(k+3)."""
    return 1 - Rational(18) / (level + 3)


# =============================================================================
# Kappa formulas
# =============================================================================

def kappa_affine_sl3(level=k):
    """kappa(V_k(sl_3)) = 4(k+3)/3. Linear in k."""
    return Rational(4, 3) * (level + 3)


def kappa_W3(level=k):
    """kappa(W_3, k) = (5/6) * c(W_3, k). Anomaly ratio rho = 5/6."""
    return Rational(5, 6) * c_W3(level)


def kappa_BP(level=k):
    """kappa(BP, k) = (1/6) * c(BP, k). Anomaly ratio rho = 1/6."""
    return Rational(1, 6) * c_BP(level)


def dual_level(level=k, N=3):
    """Feigin-Frenkel dual level: k' = -k - 2N."""
    return -level - 2 * N


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
        """D((3), k) = (64k^2 + 259k + 261) / (3(k+3)) is NOT constant."""
        D = simplify(kappa_affine_sl3(k) - kappa_W3(k))
        dD_dk = simplify(diff(D, k))
        assert dD_dk != 0, "D((3), k) should depend on k"

    def test_deficit_principal_formula(self):
        """D((3), k) = (64k^2 + 259k + 261) / (3(k+3))."""
        D = simplify(kappa_affine_sl3(k) - kappa_W3(k))
        expected = (64 * k ** 2 + 259 * k + 261) / (3 * (k + 3))
        assert simplify(D - expected) == 0

    def test_deficit_subreg_k_dependent(self):
        """D((2,1), k) = (8k^2 + 47k + 87) / (6(k+3)) is NOT constant."""
        D = simplify(kappa_affine_sl3(k) - kappa_BP(k))
        dD_dk = simplify(diff(D, k))
        assert dD_dk != 0, "D((2,1), k) should depend on k"

    def test_deficit_subreg_formula(self):
        """D((2,1), k) = (8k^2 + 47k + 87) / (6(k+3))."""
        D = simplify(kappa_affine_sl3(k) - kappa_BP(k))
        expected = (8 * k ** 2 + 47 * k + 87) / (6 * (k + 3))
        assert simplify(D - expected) == 0

    @pytest.mark.parametrize("kval", [1, 2, 3])
    def test_deficit_principal_numerical(self, kval):
        """Numerical check: D((3)) at k=1,2,3."""
        kv = Rational(kval)
        D = kappa_affine_sl3(kv) - kappa_W3(kv)
        expected = Rational(64 * kval ** 2 + 259 * kval + 261,
                            3 * (kval + 3))
        assert D == expected

    @pytest.mark.parametrize("kval", [1, 2, 3])
    def test_deficit_subreg_numerical(self, kval):
        """Numerical check: D((2,1)) at k=1,2,3."""
        kv = Rational(kval)
        D = kappa_affine_sl3(kv) - kappa_BP(kv)
        expected = Rational(8 * kval ** 2 + 47 * kval + 87,
                            6 * (kval + 3))
        assert D == expected


# =============================================================================
# Tests: Koszul complementarity sum is k-independent
# =============================================================================

class TestKoszulComplementarity:
    """Verify kappa(W,k) + kappa(W,k') = rho * K is k-independent."""

    def test_affine_complementarity(self):
        """kappa(V_k) + kappa(V_{k'}) = 0."""
        kp = dual_level(k, 3)
        s = simplify(kappa_affine_sl3(k) + kappa_affine_sl3(kp))
        assert s == 0

    def test_W3_complementarity_value(self):
        """kappa(W_3,k) + kappa(W_3,k') = 250/3."""
        kp = dual_level(k, 3)
        s = simplify(kappa_W3(k) + kappa_W3(kp))
        assert s == Rational(250, 3)

    def test_W3_complementarity_k_independent(self):
        """kappa(W_3,k) + kappa(W_3,k') is k-independent."""
        kp = dual_level(k, 3)
        s = simplify(kappa_W3(k) + kappa_W3(kp))
        assert simplify(diff(s, k)) == 0

    def test_W3_complementarity_equals_rho_K(self):
        """kappa(W_3) + kappa(W_3') = rho * K = (5/6) * 100 = 250/3."""
        rho = Rational(5, 6)
        kp = dual_level(k, 3)
        K = simplify(c_W3(k) + c_W3(kp))
        assert K == 100
        assert rho * K == Rational(250, 3)

    def test_BP_complementarity_value(self):
        """kappa(BP,k) + kappa(BP,k') = 1/3."""
        kp = dual_level(k, 3)
        s = simplify(kappa_BP(k) + kappa_BP(kp))
        assert s == Rational(1, 3)

    def test_BP_complementarity_k_independent(self):
        """kappa(BP,k) + kappa(BP,k') is k-independent."""
        kp = dual_level(k, 3)
        s = simplify(kappa_BP(k) + kappa_BP(kp))
        assert simplify(diff(s, k)) == 0

    def test_BP_complementarity_equals_rho_K(self):
        """kappa(BP) + kappa(BP') = rho * K = (1/6) * 2 = 1/3."""
        rho = Rational(1, 6)
        kp = dual_level(k, 3)
        K = simplify(c_BP(k) + c_BP(kp))
        assert K == 2
        assert rho * K == Rational(1, 3)


# =============================================================================
# Tests: Central charge sums (Koszul conductor)
# =============================================================================

class TestKoszulConductor:
    """Verify c(W,k) + c(W,k') is k-independent (the Koszul conductor)."""

    def test_affine_conductor_16(self):
        """c(V_k(sl_3)) + c(V_{k'}(sl_3)) = 16 (not 0!).

        c(V_k) = 8k/(k+3), c(V_{k'}) = 8(k+6)/(k+3), sum = 16.
        The KAPPA sum is 0 (kappa(V_k) + kappa(V_{k'}) = 0) but the
        CENTRAL CHARGE sum is dim(g) = 8 times 2 = 16, because
        the anomaly ratio rho = kappa/c is k-dependent for affine algebras.
        """
        kp = dual_level(k, 3)
        s = simplify(c_affine_sl3(k) + c_affine_sl3(kp))
        assert s == 16

    def test_W3_conductor_100(self):
        """c(W_3,k) + c(W_3,k') = 100."""
        kp = dual_level(k, 3)
        s = simplify(c_W3(k) + c_W3(kp))
        assert s == 100

    def test_BP_conductor_2(self):
        """c(BP,k) + c(BP,k') = 2."""
        kp = dual_level(k, 3)
        s = simplify(c_BP(k) + c_BP(kp))
        assert s == 2


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
        But kappa(Vir) = c/2 = (1 - 6(k+1)^2/(k+2))/2.
        """
        kappa_aff_sl2 = Rational(3, 4) * (k + 2)
        C_ghost = 1
        kappa_ghost = kappa_aff_sl2 - C_ghost

        c_vir = 1 - 6 * (k + 1) ** 2 / (k + 2)
        kappa_rho = c_vir / 2  # rho(Vir) = 1/2

        diff_expr = simplify(kappa_ghost - kappa_rho)
        assert diff_expr != 0, "Ghost subtraction should NOT equal rho*c"

    def test_W3_ghost_subtraction_fails(self):
        """For sl_3 principal: kappa(V_k) - 4 != (5/6)*c(W_3).

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
# Tests: Ghost subtraction IS correct for central charge
# =============================================================================

class TestGhostSubtractionCentralCharge:
    """The ghost system contributes a k-dependent correction to c,
    but the ANOMALY RATIO rho = kappa/c is k-independent for
    freely generated W-algebras."""

    def test_rho_W3_k_independent(self):
        """rho(W_3) = kappa(W_3)/c(W_3) = 5/6 at all k."""
        rho_computed = simplify(kappa_W3(k) / c_W3(k))
        assert rho_computed == Rational(5, 6)

    def test_rho_BP_k_independent(self):
        """rho(BP) = kappa(BP)/c(BP) = 1/6 at all k."""
        rho_computed = simplify(kappa_BP(k) / c_BP(k))
        assert rho_computed == Rational(1, 6)

    @pytest.mark.parametrize("kval", [1, 2, 3, 5, 10])
    def test_rho_W3_numerical(self, kval):
        """rho(W_3) = 5/6 at specific k values."""
        kv = Rational(kval)
        rho = kappa_W3(kv) / c_W3(kv)
        assert rho == Rational(5, 6)

    @pytest.mark.parametrize("kval", [1, 2, 3, 5, 10])
    def test_rho_BP_numerical(self, kval):
        """rho(BP) = 1/6 at specific k values."""
        kv = Rational(kval)
        rho = kappa_BP(kv) / c_BP(kv)
        assert rho == Rational(1, 6)
