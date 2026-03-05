"""Tests for W_3 bar complex extended computation (w3_bar_extended.py).

Verifies:
1. PBW basis dimensions match the generating function
2. All generator-pair OPE products match ground truth
3. Skew symmetry W_{(0)}T = 2*dW
4. DS complementarity c + c' = 100
5. Bar chain group dimensions (combinatorial)
6. Known bar cohomology ground truth H^1=2, H^2=5, H^3=16, H^4=52

The bar cohomology values come from the CHIRAL bar complex (involving
configuration space forms and residue calculus). The current module
verifies all algebraic ingredients but does not yet implement the
full chiral bar differential needed to independently compute H^n.
"""

import pytest
import numpy as np

from compute.lib.w3_bar_extended import (
    VACUUM,
    State,
    state_weight,
    make_state,
    vbar_basis,
    dim_vbar,
    dim_vbar_gf,
    bar_chain_dim,
    bar_chain_table,
    W3VacuumModule,
    verify_mu_generators,
    verify_skew_symmetry,
    verify_ds_central_charge,
    chain_dimension_analysis,
)

# Standard states
T: State = ((2,), ())
W: State = ((), (3,))
dT: State = ((3,), ())
dW: State = ((), (4,))


# =========================================================================
# PBW basis and V-bar dimensions
# =========================================================================

class TestVbarBasis:
    """PBW basis enumeration for the W3 vacuum module."""

    def test_weight_0_empty(self):
        """No V-bar states at weight 0 (vacuum excluded)."""
        assert dim_vbar(0) == 0

    def test_weight_1_empty(self):
        """No V-bar states at weight 1 (no modes with weight 1)."""
        assert dim_vbar(1) == 0

    def test_weight_2(self):
        """Weight 2: only L_{-2}|0>."""
        assert dim_vbar(2) == 1
        b = vbar_basis(2)
        assert b[2] == [((2,), ())]

    def test_weight_3(self):
        """Weight 3: L_{-3}|0> and W_{-3}|0>."""
        assert dim_vbar(3) == 2
        b = vbar_basis(3)
        states = sorted(b[3])
        assert len(states) == 2

    def test_weight_4(self):
        """Weight 4: L_{-4}, L_{-2}^2, W_{-4}."""
        assert dim_vbar(4) == 3

    def test_weight_5(self):
        """Weight 5: L_{-5}, L_{-3}L_{-2}, W_{-5}, W_{-3}L_{-2}."""
        assert dim_vbar(5) == 4

    def test_weight_6(self):
        """Weight 6: 8 states (from GF)."""
        assert dim_vbar(6) == 8

    def test_weight_7(self):
        """Weight 7: 10 states (from GF)."""
        assert dim_vbar(7) == 10

    def test_weight_8(self):
        """Weight 8: 17 states (from GF)."""
        assert dim_vbar(8) == 17

    def test_gf_matches_direct(self):
        """GF formula matches direct PBW enumeration through weight 15."""
        gf = dim_vbar_gf(15)
        for h in range(0, 16):
            assert gf[h] == dim_vbar(h), f"Mismatch at weight {h}"

    def test_manuscript_gf_values(self):
        """The GF prod_{n>=2} 1/(1-q^n) * prod_{n>=3} 1/(1-q^n) - 1
        gives 1,2,3,4,8,10,17 at h=2,...,8.

        NOTE: The manuscript TABLE at w_algebras_deep.tex line 402
        says 1,2,4,6,11,16,26 — this is WRONG. The GF formula
        (same file, line 412) gives the values tested here.
        """
        expected = {2: 1, 3: 2, 4: 3, 5: 4, 6: 8, 7: 10, 8: 17}
        gf = dim_vbar_gf(8)
        for h, val in expected.items():
            assert gf[h] == val, f"GF dim at h={h}: got {gf[h]}, expected {val}"


# =========================================================================
# State utilities
# =========================================================================

class TestStateUtils:
    def test_vacuum_weight(self):
        assert state_weight(VACUUM) == 0

    def test_T_weight(self):
        assert state_weight(T) == 2

    def test_W_weight(self):
        assert state_weight(W) == 3

    def test_make_state_sorts(self):
        assert make_state((2, 3), (4, 5)) == ((3, 2), (5, 4))

    def test_multi_mode_weight(self):
        s = make_state((2, 3), (3,))
        assert state_weight(s) == 8


# =========================================================================
# W3VacuumModule: mode algebra
# =========================================================================

class TestModeAlgebra:
    """Verify Virasoro and W-mode actions on states."""

    @pytest.fixture
    def mod(self):
        return W3VacuumModule(10, c_val=7.0)

    def test_L_minus2_vacuum(self, mod):
        """L_{-2}|0> = T."""
        result = mod._L_on_state(-2, VACUUM)
        assert T in result
        assert abs(result[T] - 1.0) < 1e-12

    def test_W_minus3_vacuum(self, mod):
        """W_{-3}|0> = W."""
        result = mod._W_on_state(-3, VACUUM)
        assert W in result
        assert abs(result[W] - 1.0) < 1e-12

    def test_L0_on_T(self, mod):
        """L_0|T> = 2|T> (T has weight 2)."""
        result = mod._L_on_state(0, T)
        assert abs(result.get(T, 0) - 2.0) < 1e-12

    def test_L0_on_W(self, mod):
        """L_0|W> = 3|W> (W has weight 3)."""
        result = mod._L_on_state(0, W)
        assert abs(result.get(W, 0) - 3.0) < 1e-12

    def test_L1_on_T(self, mod):
        """L_1|T> = 0 (T is primary)."""
        result = mod._L_on_state(1, T)
        for s, c in result.items():
            assert abs(c) < 1e-12, f"L_1|T> has nonzero component at {s}"

    def test_L1_on_W(self, mod):
        """L_1|W> = 0 (W is primary)."""
        result = mod._L_on_state(1, W)
        for s, c in result.items():
            assert abs(c) < 1e-12, f"L_1|W> has nonzero component at {s}"

    def test_L_minus1_on_T(self, mod):
        """L_{-1}|T> = dT = L_{-3}|0>."""
        result = mod._L_on_state(-1, T)
        assert abs(result.get(dT, 0) - 1.0) < 1e-12

    def test_L2_on_T(self, mod):
        """L_2|T> = c/2 |0> (central charge)."""
        result = mod._L_on_state(2, T)
        assert abs(result.get(VACUUM, 0) - 3.5) < 1e-12  # c=7 -> c/2=3.5


# =========================================================================
# OPE products: mu(a,b) = sum_{k>=0} a_{(k)}b
# =========================================================================

class TestMuProducts:
    """Verify all 4 generator-pair mu products against ground truth."""

    @pytest.fixture
    def mod(self):
        return W3VacuumModule(10, c_val=7.0)

    def test_mu_TT_vacuum(self, mod):
        """mu(T,T) vacuum component = c/2."""
        _, vac = mod.compute_mu(T, T)
        assert abs(vac - 3.5) < 1e-10

    def test_mu_TT_T_coeff(self, mod):
        """mu(T,T) has coefficient 2 for T."""
        vbar, _ = mod.compute_mu(T, T)
        idx = mod._vbar_to_idx[T]
        assert abs(vbar[idx] - 2.0) < 1e-10

    def test_mu_TT_dT_coeff(self, mod):
        """mu(T,T) has coefficient 1 for dT."""
        vbar, _ = mod.compute_mu(T, T)
        idx = mod._vbar_to_idx[dT]
        assert abs(vbar[idx] - 1.0) < 1e-10

    def test_mu_TW_vacuum(self, mod):
        """mu(T,W) vacuum component = 0."""
        _, vac = mod.compute_mu(T, W)
        assert abs(vac) < 1e-10

    def test_mu_TW_W_coeff(self, mod):
        """mu(T,W) has coefficient 3 for W."""
        vbar, _ = mod.compute_mu(T, W)
        idx = mod._vbar_to_idx[W]
        assert abs(vbar[idx] - 3.0) < 1e-10

    def test_mu_TW_dW_coeff(self, mod):
        """mu(T,W) has coefficient 1 for dW."""
        vbar, _ = mod.compute_mu(T, W)
        idx = mod._vbar_to_idx[dW]
        assert abs(vbar[idx] - 1.0) < 1e-10

    def test_mu_WT_vacuum(self, mod):
        """mu(W,T) vacuum component = 0."""
        _, vac = mod.compute_mu(W, T)
        assert abs(vac) < 1e-10

    def test_mu_WT_W_coeff(self, mod):
        """mu(W,T) has coefficient 3 for W."""
        vbar, _ = mod.compute_mu(W, T)
        idx = mod._vbar_to_idx[W]
        assert abs(vbar[idx] - 3.0) < 1e-10

    def test_mu_WT_dW_coeff(self, mod):
        """mu(W,T) has coefficient 2 for dW."""
        vbar, _ = mod.compute_mu(W, T)
        idx = mod._vbar_to_idx[dW]
        assert abs(vbar[idx] - 2.0) < 1e-10

    def test_mu_WW_vacuum(self, mod):
        """mu(W,W) vacuum component = c/3."""
        _, vac = mod.compute_mu(W, W)
        assert abs(vac - 7.0 / 3.0) < 1e-10

    def test_mu_WW_T_coeff(self, mod):
        """mu(W,W) has coefficient 2 for T."""
        vbar, _ = mod.compute_mu(W, W)
        idx = mod._vbar_to_idx[T]
        assert abs(vbar[idx] - 2.0) < 1e-10

    def test_mu_WW_dT_coeff(self, mod):
        """mu(W,W) has coefficient 1 for dT."""
        vbar, _ = mod.compute_mu(W, W)
        idx = mod._vbar_to_idx[dT]
        assert abs(vbar[idx] - 1.0) < 1e-10

    def test_mu_WW_L4_coeff(self, mod):
        """mu(W,W) L_{-4}|0> coefficient = 3/5 - 3/5*alpha (with alpha=16/(22+5c))."""
        vbar, _ = mod.compute_mu(W, W)
        alpha = 16.0 / (22.0 + 5.0 * 7.0)
        expected = 0.6 - 0.6 * alpha
        idx = mod._vbar_to_idx[((4,), ())]
        assert abs(vbar[idx] - expected) < 1e-8

    def test_mu_WW_L22_coeff(self, mod):
        """mu(W,W) L_{-2}^2|0> coefficient = alpha = 16/(22+5c)."""
        vbar, _ = mod.compute_mu(W, W)
        alpha = 16.0 / (22.0 + 5.0 * 7.0)
        idx = mod._vbar_to_idx[((2, 2), ())]
        assert abs(vbar[idx] - alpha) < 1e-8


# =========================================================================
# Skew symmetry
# =========================================================================

class TestSkewSymmetry:
    def test_W0T_equals_2dW(self):
        """W_{(0)}T = 2*partial(W) = 2*dW."""
        results = verify_skew_symmetry(c_val=7.0)
        assert results["W_{(0)}T = 2*dW"]

    def test_W0T_no_spurious(self):
        """W_{(0)}T has no components other than dW."""
        results = verify_skew_symmetry(c_val=7.0)
        for key, val in results.items():
            assert val, f"Failed: {key}"


# =========================================================================
# DS complementarity
# =========================================================================

class TestDSComplementarity:
    def test_complementarity_sum_100(self):
        """c(k) + c(-k-6) = 100 for W3 DS reduction."""
        results = verify_ds_central_charge()
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_ds_formula_k1(self):
        """At k=1: c = 2 - 24*9/4 = 2 - 54 = -52."""
        c = 2 - 24 * (1 + 2)**2 / (1 + 3)
        assert abs(c - (-52.0)) < 1e-12

    def test_ds_formula_k0(self):
        """At k=0: c = 2 - 24*4/3 = 2 - 32 = -30."""
        c = 2 - 24 * (0 + 2)**2 / (0 + 3)
        assert abs(c - (-30.0)) < 1e-12


# =========================================================================
# n-th products (individual poles)
# =========================================================================

class TestNthProducts:
    """Verify individual n-th products a_{(k)}b."""

    @pytest.fixture
    def mod(self):
        return W3VacuumModule(10, c_val=7.0)

    def test_T3T_quartic_pole(self, mod):
        """T_{(3)}T = c/2 |0> (quartic pole)."""
        v = mod.compute_nth_product(T, T, 3)
        assert abs(v[0] - 3.5) < 1e-10
        # No other components
        for i in range(1, mod.total_dim):
            assert abs(v[i]) < 1e-10

    def test_T1T_simple(self, mod):
        """T_{(1)}T = 2T."""
        v = mod.compute_nth_product(T, T, 1)
        idx = mod._state_to_idx[T]
        assert abs(v[idx] - 2.0) < 1e-10

    def test_T0T_derivative(self, mod):
        """T_{(0)}T = dT = L_{-3}|0>."""
        v = mod.compute_nth_product(T, T, 0)
        idx = mod._state_to_idx[dT]
        assert abs(v[idx] - 1.0) < 1e-10

    def test_W5W_sixth_order_pole(self, mod):
        """W_{(5)}W = c/3 |0>."""
        v = mod.compute_nth_product(W, W, 5)
        assert abs(v[0] - 7.0 / 3.0) < 1e-10

    def test_W3W(self, mod):
        """W_{(3)}W = 2T."""
        v = mod.compute_nth_product(W, W, 3)
        idx = mod._state_to_idx[T]
        assert abs(v[idx] - 2.0) < 1e-10


# =========================================================================
# Bar chain group dimensions
# =========================================================================

class TestBarChainDims:
    """Bar chain group dimensions B^n_h."""

    def test_B0_dim(self):
        """B^0 = V-bar (no OS factor needed)."""
        # B^0_h = dim V-bar_h * 0! = dim V-bar_h * 1
        gf = dim_vbar_gf(10)
        for h in range(2, 11):
            assert bar_chain_dim(0, h, gf) == gf[h]

    def test_B1_min_weight(self):
        """B^1 starts at weight 4 (two V-bar states, each >= 2)."""
        gf = dim_vbar_gf(10)
        assert bar_chain_dim(1, 3, gf) == 0
        assert bar_chain_dim(1, 4, gf) > 0

    def test_B1_weight_4(self):
        """B^1 at h=4: only T tensor T, times OS dim = 1! = 1."""
        gf = dim_vbar_gf(10)
        assert bar_chain_dim(1, 4, gf) == 1  # 1 tuple * 1! = 1

    def test_B1_weight_5(self):
        """B^1 at h=5: tuples (T, L3/W3) and (L3/W3, T), each 1*2 + 2*1 ways,
        times OS dim 1! = 1."""
        gf = dim_vbar_gf(10)
        # weight 5 = 2+3 only, so 1*2 + 2*1 = 4 ordered pairs, but actually
        # conv = sum d(h1)*d(h2) for h1+h2=5: d(2)*d(3) + d(3)*d(2) = 1*2+2*1=4
        assert bar_chain_dim(1, 5, gf) == 4

    def test_B2_min_weight(self):
        """B^2 starts at weight 6 (three V-bar states, each >= 2)."""
        gf = dim_vbar_gf(10)
        assert bar_chain_dim(2, 5, gf) == 0
        assert bar_chain_dim(2, 6, gf) > 0

    def test_os_factor_scales(self):
        """OS^n factor is n!, so B^n at min weight scales with n!."""
        gf = dim_vbar_gf(20)
        # Min weight for B^n = 2*(n+1), single tuple T^{n+1}
        for n in range(0, 5):
            d = bar_chain_dim(n, 2 * (n + 1), gf)
            import math
            # 1 tuple * n!
            assert d == math.factorial(n)

    def test_chain_table_nonempty(self):
        """Chain table has entries."""
        tab = bar_chain_table(3, 10)
        assert len(tab) > 0


# =========================================================================
# Known bar cohomology ground truth
# =========================================================================

class TestBarCohomologyGroundTruth:
    """Document the known bar cohomology values.

    These values come from the CHIRAL bar complex involving configuration
    space forms and residue calculus (tab:bar-dimensions in examples_summary.tex,
    KNOWN_BAR_DIMS in bar_complex.py).

    The chiral bar complex differential has not been implemented in this
    module — independent verification of these values from the algebraic
    ingredients remains an open computational task.
    """

    KNOWN_H = {1: 2, 2: 5, 3: 16, 4: 52}

    def test_H1_ground_truth(self):
        """H^1(B(W3)) = 2 (generators T, W)."""
        assert self.KNOWN_H[1] == 2

    def test_H2_ground_truth(self):
        """H^2(B(W3)) = 5."""
        assert self.KNOWN_H[2] == 5

    def test_H3_ground_truth(self):
        """H^3(B(W3)) = 16."""
        assert self.KNOWN_H[3] == 16

    def test_H4_ground_truth(self):
        """H^4(B(W3)) = 52."""
        assert self.KNOWN_H[4] == 52

    def test_exponential_growth(self):
        """H^n grows roughly as ~3.2^n (between 3^n and 4^n)."""
        ratios = [self.KNOWN_H[n + 1] / self.KNOWN_H[n] for n in range(1, 4)]
        for r in ratios:
            assert 2.0 < r < 5.0, f"Growth ratio {r} outside expected range"

    def test_H5_unknown(self):
        """H^5 is not yet computed — this is the target.

        Conj:w3-algebraicity in genus_expansions.tex predicts the GF
        P_{W3}(x) is algebraic. With 4 data points (2,5,16,52),
        the simplest algebraic relation would be degree 2 or 3.
        Computing H^5 would test whether the sequence satisfies
        a low-order recurrence.

        Candidate predictions from algebraic GF fitting:
        - If P satisfies a quadratic: H^5 ~ 170-180
        - If P has same discriminant Delta=(1-3x)(1+x) as sl2/Vir/betagamma: H^5 ~ 170
        """
        assert 5 not in self.KNOWN_H


# =========================================================================
# Verification helper integration tests
# =========================================================================

class TestVerificationHelpers:
    """Integration tests calling the module's verify_* functions."""

    def test_verify_mu_generators_all_pass(self):
        results = verify_mu_generators(c_val=7.0, verbose=False)
        for name, ok in results.items():
            assert ok, f"verify_mu_generators failed: {name}"

    def test_verify_mu_generators_c100(self):
        """Verify at c=100 (the complementary central charge at k=-7)."""
        results = verify_mu_generators(c_val=100.0, verbose=False)
        for name, ok in results.items():
            assert ok, f"verify_mu_generators(c=100) failed: {name}"

    def test_verify_skew_symmetry(self):
        results = verify_skew_symmetry(c_val=7.0)
        for name, ok in results.items():
            assert ok, f"verify_skew_symmetry failed: {name}"

    def test_verify_ds_complementarity(self):
        results = verify_ds_central_charge()
        for name, ok in results.items():
            assert ok, f"verify_ds_central_charge failed: {name}"


# =========================================================================
# Consistency checks across central charge values
# =========================================================================

class TestCentralChargeConsistency:
    """Verify OPE products at multiple central charge values."""

    @pytest.mark.parametrize("c_val", [0.0, 2.0, 7.0, 25.0, 50.0, 100.0])
    def test_mu_TT_vacuum_scales_with_c(self, c_val):
        """mu(T,T) vacuum = c/2 for any c."""
        mod = W3VacuumModule(8, c_val)
        _, vac = mod.compute_mu(T, T)
        assert abs(vac - c_val / 2) < 1e-8

    @pytest.mark.parametrize("c_val", [2.0, 7.0, 50.0, 100.0])
    def test_mu_WW_vacuum_scales_with_c(self, c_val):
        """mu(W,W) vacuum = c/3 for any c."""
        mod = W3VacuumModule(8, c_val)
        _, vac = mod.compute_mu(W, W)
        assert abs(vac - c_val / 3) < 1e-8

    @pytest.mark.parametrize("c_val", [2.0, 7.0, 50.0])
    def test_mu_TW_c_independent(self, c_val):
        """mu(T,W) W-coefficient = 3 independent of c."""
        mod = W3VacuumModule(8, c_val)
        vbar, _ = mod.compute_mu(T, W)
        idx = mod._vbar_to_idx[W]
        assert abs(vbar[idx] - 3.0) < 1e-8
