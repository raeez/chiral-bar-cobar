"""Comprehensive tests for the canonical W_N central charge formula.

Tests the Fateev-Lukyanov formula:
    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

and flags any module in compute/lib/ that uses the WRONG simple formula
    c = (N-1)(1 - N(N+1)/(k+N))
which gives c(W_2, k=1) = -1 instead of the correct -7.
"""

import importlib
import sys
from fractions import Fraction
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from compute.lib.wn_central_charge_canonical import (
    c_wn_fl, kappa_wn_fl, complementarity_sum,
    kappa_complementarity_sum, ff_dual_level,
)


# ============================================================
# 1. Formula correctness
# ============================================================

class TestFormulaCorrectness:
    """Verify the canonical formula against known values."""

    def test_virasoro_k1(self):
        # VERIFIED: [DC] chapters/examples/w_algebras.tex:1434 gives
        # c_Vir(k) = 13 - 6(k+2) - 6/(k+2), so k=1 gives -7.
        # [LC] W_2 = Vir, so c_wn_fl(2, 1) must match the same value.
        assert c_wn_fl(2, 1) == Fraction(-7)

    def test_virasoro_k2(self):
        assert c_wn_fl(2, 2) == Fraction(-25, 2)

    def test_virasoro_k10(self):
        assert c_wn_fl(2, 10) == Fraction(-119, 2)

    def test_virasoro_k100(self):
        # 1 - 6*101^2/102 = 1 - 61206/102 = (102-61206)/102 = -61104/102 = -10184/17
        assert c_wn_fl(2, 100) == Fraction(-10184, 17)

    def test_w3_k1(self):
        # VERIFIED: [DC] chapters/examples/w_algebras_deep.tex:2914 gives
        # c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N); at (N, k) = (3, 1)
        # this evaluates to 2 - 24 * 9 / 4 = -52.
        assert c_wn_fl(3, 1) == Fraction(-52)

    def test_w3_k5(self):
        assert c_wn_fl(3, 5) == Fraction(-145)

    def test_w4_k1(self):
        assert c_wn_fl(4, 1) == Fraction(-189)

    def test_w5_k1(self):
        assert c_wn_fl(5, 1) == Fraction(-496)

    def test_w6_k1(self):
        assert c_wn_fl(6, 1) == Fraction(-1075)

    def test_critical_level_raises(self):
        with pytest.raises(ValueError):
            c_wn_fl(2, -2)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_not_simple_formula(self, N):
        """The canonical formula must NOT equal the simple formula for N >= 2, k=1."""
        correct = c_wn_fl(N, 1)
        simple = Fraction(N - 1) * (1 - Fraction(N * (N + 1), 1 + N))
        if N == 2:
            # correct = -7, simple = -1
            assert correct != simple, f"N={N}: formulas agree but shouldn't"
        else:
            assert correct != simple, f"N={N}: formulas agree but shouldn't"


# ============================================================
# 2. Complementarity
# ============================================================

class TestComplementarity:
    """Verify Freudenthal-de Vries identity."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_complementarity_sum(self, N):
        expected = Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))
        assert complementarity_sum(N) == expected

    @pytest.mark.parametrize("N,k", [(2, 1), (2, 5), (3, 1), (3, 10), (4, 3), (5, 2)])
    def test_complementarity_at_specific_k(self, N, k):
        kp = ff_dual_level(N, k)
        assert c_wn_fl(N, k) + c_wn_fl(N, kp) == complementarity_sum(N)

    def test_virasoro_complementarity_26(self):
        """c + c' = 26 for Virasoro (N=2)."""
        # VERIFIED: [DC] chapters/examples/w_algebras.tex:1452 proves
        # c(k) + c(-k-4) = 26 for Virasoro. [CF] chapters/examples/w_algebras.tex:2290
        # lifts this to kappa via kappa = c(H_N - 1), with H_2 - 1 = 1/2.
        assert complementarity_sum(2) == 26

    def test_w3_complementarity_100(self):
        assert complementarity_sum(3) == 100

    def test_kappa_virasoro_13(self):
        """kappa + kappa' = 13 for Virasoro."""
        assert kappa_complementarity_sum(2) == 13

    def test_kappa_w3_250_over_3(self):
        assert kappa_complementarity_sum(3) == Fraction(250, 3)

    def test_kappa_w4_533_over_2(self):
        assert kappa_complementarity_sum(4) == Fraction(533, 2)

    def test_kappa_w5_9394_over_15(self):
        assert kappa_complementarity_sum(5) == Fraction(9394, 15)


# ============================================================
# 3. Kappa values
# ============================================================

class TestKappa:

    def test_kappa_vir_k1(self):
        assert kappa_wn_fl(2, 1) == Fraction(-7, 2)

    def test_kappa_w3_k1(self):
        assert kappa_wn_fl(3, 1) == Fraction(-130, 3)

    def test_kappa_w4_k1(self):
        assert kappa_wn_fl(4, 1) == Fraction(-819, 4)


# ============================================================
# 4. Cross-module consistency detector
# ============================================================

class TestCrossModuleConsistency:
    """Detect any module using the wrong simple formula.

    Any function that computes c(W_2, k=1) and returns -1 instead of -7
    is using the wrong formula.
    """

    MODULES_WITH_C_WN = [
        ("compute.lib.ds_cascade_shadows", "c_WN", (2, Fraction(1))),
        ("compute.lib.ds_transferred_shadows", "c_WN", (2, Fraction(1))),
        ("compute.lib.ds_shadow_cascade_engine", "c_WN", (2, Fraction(1))),
        ("compute.lib.ds_arithmetic_transformation_engine", "c_WN_principal", (2, Fraction(1))),
        ("compute.lib.ds_nonprincipal_shadows", "c_WN_principal", (2, Fraction(1))),
        ("compute.lib.w_infinity_shadow_limit", "c_wn_principal", (2, Fraction(1))),
        ("compute.lib.w_infinity_shadow_limit_deep", "c_WN", (2, Fraction(1))),
    ]

    @pytest.mark.parametrize("mod_name,func_name,args", MODULES_WITH_C_WN,
                             ids=[m[0].split('.')[-1] for m in MODULES_WITH_C_WN])
    def test_module_gives_correct_virasoro(self, mod_name, func_name, args):
        """Each module's c(W_2, k=1) must equal -7, not -1."""
        try:
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            result = func(*args)
            assert result == Fraction(-7), (
                f"{mod_name}.{func_name}(2, 1) = {result}. "
                f"Expected -7. If -1, the module uses the WRONG simple formula. "
                f"Correct: c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)"
            )
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Cannot import: {e}")
