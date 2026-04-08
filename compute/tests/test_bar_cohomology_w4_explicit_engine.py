"""Tests for compute/lib/bar_cohomology_w4_explicit_engine.py.

Explicit bar cohomology H*(B(W_4)) at weights 0 through 6.

Verification paths:
  1. Direct PBW enumeration vs generating function (two independent methods)
  2. Cross-check against _wn_vacuum_dims(N=4) from ds_spectral_sequence.py
  3. Cross-check W_3 vacuum dims against _wn_vacuum_dims(N=3)
  4. Symbolic OPE structure against w4_bar.py and w4_ds_ope_extraction.py
  5. Numerical evaluation at specific c values
  6. Classical limits (c -> inf) of structure constants
  7. Complementarity c(k) + c(-k-8) = 246

References:
  Hornfeck, Nucl. Phys. B 407 (1993) 57
  w4_ds_ope_extraction.py: known Hornfeck formulas
  w3_bar.py: W_3 bar complex (for comparison)
  ds_spectral_sequence.py: _wn_vacuum_dims (independent implementation)
"""

import math

import pytest
from sympy import Rational, Symbol, expand, simplify, sqrt

from compute.lib.bar_cohomology_w4_explicit_engine import (
    VACUUM,
    bar_chain_dim,
    bar_chain_table,
    bar_diff_deg1,
    bar_euler_char,
    channel_decomposition,
    compare_h1_w3_vs_w4,
    g334_squared,
    g334_squared_float,
    g444_squared,
    g444_squared_float,
    h1_dimension_lower_bound,
    h1_generators_by_weight,
    irrationality_analysis,
    state_weight,
    vbar_basis,
    vbar_basis_labels,
    verify_augmentation_dims,
    verify_bar_diff_deg1,
    verify_channel_decomposition,
    verify_curvature,
    verify_irrationality_weight,
    verify_skew_symmetry,
    verify_vacuum_dims,
    virasoro_vacuum_dims,
    w3_vacuum_dims,
    w4_augmentation_dim,
    w4_augmentation_dims,
    w4_central_charge,
    w4_complementarity_sum,
    w4_curvature,
    w4_full_nth_products,
    w4_kappa,
    w4_vacuum_dims,
    weight4_full_basis,
    weight4_gram_matrix,
)


# ============================================================================
# Module import
# ============================================================================

class TestImport:
    def test_module_loads(self):
        import compute.lib.bar_cohomology_w4_explicit_engine
        assert hasattr(compute.lib.bar_cohomology_w4_explicit_engine, 'w4_vacuum_dims')


# ============================================================================
# Vacuum module dimensions
# ============================================================================

class TestVacuumDims:
    """Verify W_4 vacuum module dimensions by multiple paths."""

    def test_dim_0(self):
        """dim V_0 = 1 (vacuum)."""
        assert w4_vacuum_dims(8)[0] == 1

    def test_dim_1(self):
        """dim V_1 = 0 (no weight-1 states)."""
        assert w4_vacuum_dims(8)[1] == 0

    def test_dim_2(self):
        """dim V_2 = 1: just L_{-2}|0>."""
        assert w4_vacuum_dims(8)[2] == 1

    def test_dim_3(self):
        """dim V_3 = 2: L_{-3}|0> and W3_{-3}|0>."""
        assert w4_vacuum_dims(8)[3] == 2

    def test_dim_4(self):
        """dim V_4 = 4: L_{-4}, L_{-2}^2, W3_{-4}, W4_{-4}."""
        assert w4_vacuum_dims(8)[4] == 4

    def test_dim_5(self):
        """dim V_5 = 5: L_{-5}, L_{-3}L_{-2}, W3_{-5}, L_{-2}W3_{-3}, W4_{-5}."""
        assert w4_vacuum_dims(8)[5] == 5

    def test_dim_6(self):
        """dim V_6 = 10."""
        assert w4_vacuum_dims(8)[6] == 10

    def test_cross_check_ds_spectral_sequence(self):
        """Cross-check against _wn_vacuum_dims(N=4) from ds_spectral_sequence."""
        from compute.lib.ds_spectral_sequence import _wn_vacuum_dims
        wn_dims = _wn_vacuum_dims(4, 10)
        our_dims = w4_vacuum_dims(10)
        for h in range(11):
            assert our_dims.get(h, 0) == wn_dims.get(h, 0), (
                f"Mismatch at h={h}: ours={our_dims.get(h,0)}, ds_ss={wn_dims.get(h,0)}")

    def test_pbw_enumeration_matches_gf(self):
        """PBW basis count must equal generating function dimension."""
        basis = vbar_basis(8)
        vdims = w4_augmentation_dims(8)
        for h in range(2, 9):
            assert len(basis.get(h, [])) == vdims.get(h, 0), (
                f"PBW/GF mismatch at h={h}")

    def test_w3_cross_check(self):
        """Our W_3 dims must match _wn_vacuum_dims(N=3)."""
        from compute.lib.ds_spectral_sequence import _wn_vacuum_dims
        wn3 = _wn_vacuum_dims(3, 10)
        our_w3 = w3_vacuum_dims(10)
        for h in range(11):
            assert our_w3.get(h, 0) == wn3.get(h, 0)

    def test_virasoro_cross_check(self):
        """Our Virasoro dims must match _wn_vacuum_dims(N=2)."""
        from compute.lib.ds_spectral_sequence import _wn_vacuum_dims
        wn2 = _wn_vacuum_dims(2, 10)
        our_vir = virasoro_vacuum_dims(10)
        for h in range(11):
            assert our_vir.get(h, 0) == wn2.get(h, 0)

    def test_w4_exceeds_w3_at_h4(self):
        """W_4 has one more state than W_3 at weight 4 (the W_4 primary)."""
        w3d = w3_vacuum_dims(8)
        w4d = w4_vacuum_dims(8)
        assert w4d[4] - w3d[4] == 1

    def test_w4_exceeds_virasoro_at_h4(self):
        """W_4 has 2 more states than Virasoro at weight 4."""
        vd = virasoro_vacuum_dims(8)
        w4d = w4_vacuum_dims(8)
        assert w4d[4] - vd[4] == 2  # W3_{-4} and W4_{-4}

    def test_verify_vacuum_dims_all_pass(self):
        """All internal verification checks pass."""
        results = verify_vacuum_dims()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# Augmentation ideal
# ============================================================================

class TestAugmentationDims:
    def test_vbar_0_vanishes(self):
        """V-bar at weight 0 is empty (vacuum subtracted)."""
        assert w4_augmentation_dim(0) == 0

    def test_vbar_1_vanishes(self):
        assert w4_augmentation_dim(1) == 0

    def test_vbar_2(self):
        assert w4_augmentation_dim(2) == 1

    def test_vbar_3(self):
        assert w4_augmentation_dim(3) == 2

    def test_vbar_4(self):
        assert w4_augmentation_dim(4) == 4

    def test_verify_all_pass(self):
        results = verify_augmentation_dims()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# PBW basis labels
# ============================================================================

class TestPBWBasis:
    def test_vacuum_weight(self):
        assert state_weight(VACUUM) == 0

    def test_basis_labels_h2(self):
        labels = vbar_basis_labels(4)
        assert len(labels[2]) == 1
        assert "L_{-2}" in labels[2][0]

    def test_basis_labels_h4_has_w4(self):
        labels = vbar_basis_labels(4)
        w4_found = any("W4_{-4}" in lab for lab in labels[4])
        assert w4_found, "W4_{-4}|0> must be in the weight-4 basis"

    def test_basis_count_h6(self):
        basis = vbar_basis(6)
        assert len(basis[6]) == 10


# ============================================================================
# Central charge
# ============================================================================

class TestCentralCharge:
    def test_complementarity_sum(self):
        """c(k) + c(-k-8) = 246."""
        k = Symbol('k')
        total = simplify(w4_central_charge(k) + w4_central_charge(-k - 8))
        assert total == 246

    def test_complementarity_constant(self):
        assert w4_complementarity_sum() == 246

    def test_c_at_k1(self):
        """c(1) = 3 - 60*16/5 = 3 - 192 = -189."""
        assert w4_central_charge(1) == -189

    def test_c_at_k2(self):
        """c(2) = 3 - 60*25/6 = 3 - 250 = -247."""
        assert w4_central_charge(2) == -247


# ============================================================================
# Curvature and kappa
# ============================================================================

class TestCurvature:
    def test_m0_T(self):
        c = Symbol('c')
        assert w4_curvature(c)["T"] == c / 2

    def test_m0_W3(self):
        c = Symbol('c')
        assert w4_curvature(c)["W3"] == c / 3

    def test_m0_W4(self):
        c = Symbol('c')
        assert w4_curvature(c)["W4"] == c / 4

    def test_kappa(self):
        c = Symbol('c')
        assert expand(w4_kappa(c) - Rational(13, 12) * c) == 0

    def test_kappa_is_sum_of_curvatures(self):
        c = Symbol('c')
        curv = w4_curvature(c)
        total = curv["T"] + curv["W3"] + curv["W4"]
        assert expand(total - w4_kappa(c)) == 0

    def test_verify_all_pass(self):
        results = verify_curvature()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# Structure constants
# ============================================================================

class TestStructureConstants:
    def test_g334_squared_symbolic(self):
        c = Symbol('c')
        g = g334_squared(c)
        # At c=0: g334^2 = 0 (double zero)
        assert g.subs(c, 0) == 0

    def test_g444_squared_symbolic(self):
        c = Symbol('c')
        g = g444_squared(c)
        assert g.subs(c, 0) == 0

    def test_g334_squared_positive_unitary(self):
        """g334^2 > 0 for c > 0 (unitary regime)."""
        for c_val in [1.0, 10.0, 100.0, 1000.0]:
            assert g334_squared_float(c_val) > 0

    def test_g444_squared_positive_above_half(self):
        """g444^2 > 0 for c > 1/2."""
        for c_val in [1.0, 10.0, 100.0]:
            assert g444_squared_float(c_val) > 0

    def test_g444_squared_zero_at_ising(self):
        """g444^2 = 0 at c = 1/2 (Ising point)."""
        assert abs(g444_squared_float(0.5)) < 1e-14

    def test_classical_limit_g334(self):
        """g334^2 -> 10 as c -> infinity."""
        val = g334_squared_float(1e8)
        assert abs(val - 10.0) < 0.01

    def test_classical_limit_g444(self):
        """g444^2 -> 48/25 = 1.92 as c -> infinity."""
        val = g444_squared_float(1e8)
        assert abs(val - 1.92) < 0.01

    def test_g334_cross_check_ds_ope(self):
        """Cross-check g334^2 against w4_ds_ope_extraction.c334_squared_formula."""
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula
        c = Symbol('c')
        ours = g334_squared(c)
        theirs = c334_squared_formula(c)
        assert simplify(ours - theirs) == 0

    def test_g444_cross_check_ds_ope(self):
        """Cross-check g444^2 against w4_ds_ope_extraction.c444_squared_formula."""
        from compute.lib.w4_ds_ope_extraction import c444_squared_formula
        c = Symbol('c')
        ours = g444_squared(c)
        theirs = c444_squared_formula(c)
        assert simplify(ours - theirs) == 0


# ============================================================================
# Bar differential at degree 1
# ============================================================================

class TestBarDiffDeg1:
    def setup_method(self):
        self.c = Symbol('c')
        self.g334 = Symbol('g334')
        self.g444 = Symbol('g444')

    def test_TT_vacuum(self):
        """d(T tensor T): vacuum component = c/2."""
        vac, _ = bar_diff_deg1("T", "T", self.c, self.g334, self.g444)
        assert vac["vac"] == self.c / 2

    def test_TT_T_coefficient(self):
        """d(T tensor T): T coefficient = 2."""
        _, bar0 = bar_diff_deg1("T", "T", self.c, self.g334, self.g444)
        assert bar0["T"] == 2

    def test_TW3_no_vacuum(self):
        """d(T tensor W3): no vacuum contribution (orthogonal primaries)."""
        vac, _ = bar_diff_deg1("T", "W3", self.c, self.g334, self.g444)
        assert len(vac) == 0

    def test_TW3_W3_coefficient(self):
        """d(T tensor W3): W3 coefficient = 3 (conformal weight)."""
        _, bar0 = bar_diff_deg1("T", "W3", self.c, self.g334, self.g444)
        assert bar0["W3"] == 3

    def test_TW4_W4_coefficient(self):
        """d(T tensor W4): W4 coefficient = 4 (conformal weight)."""
        _, bar0 = bar_diff_deg1("T", "W4", self.c, self.g334, self.g444)
        assert bar0["W4"] == 4

    def test_W3W3_vacuum(self):
        """d(W3 tensor W3): vacuum = c/3 (sixth-order pole)."""
        vac, _ = bar_diff_deg1("W3", "W3", self.c, self.g334, self.g444)
        assert vac["vac"] == self.c / 3

    def test_W3W3_contains_g334(self):
        """d(W3 tensor W3): the W4 coefficient involves g334."""
        _, bar0 = bar_diff_deg1("W3", "W3", self.c, self.g334, self.g444)
        assert bar0["W4"] == self.g334

    def test_W4W4_vacuum(self):
        """d(W4 tensor W4): vacuum = c/4 (eighth-order pole)."""
        vac, _ = bar_diff_deg1("W4", "W4", self.c, self.g334, self.g444)
        assert vac["vac"] == self.c / 4

    def test_W4W4_T_ward_identity(self):
        """d(W4 tensor W4): T coefficient = 2 (Ward identity).

        For a weight-h primary: C_T = (2h/c) * <W_h|W_h> = (2*4/c)*(c/4) = 2.
        """
        _, bar0 = bar_diff_deg1("W4", "W4", self.c, self.g334, self.g444)
        assert bar0["T"] == 2

    def test_W4W4_contains_g444(self):
        """d(W4 tensor W4): the W4 self-coupling involves g444."""
        _, bar0 = bar_diff_deg1("W4", "W4", self.c, self.g334, self.g444)
        assert bar0["W4"] == self.g444

    def test_verify_all_pass(self):
        results = verify_bar_diff_deg1()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# Skew-symmetry
# ============================================================================

class TestSkewSymmetry:
    def test_W3_0_T(self):
        """W3_{(0)}T = 2 dW3 from skew-symmetry."""
        c = Symbol('c')
        _, bar0 = bar_diff_deg1("W3", "T", c)
        assert bar0.get("dW3") == 2

    def test_W4_0_T(self):
        """W4_{(0)}T = 3 dW4 from skew-symmetry."""
        c = Symbol('c')
        _, bar0 = bar_diff_deg1("W4", "T", c)
        assert bar0.get("dW4") == 3

    def test_verify_all_pass(self):
        results = verify_skew_symmetry()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# Channel decomposition
# ============================================================================

class TestChannelDecomposition:
    def test_TT_only_T_channel(self):
        """T x T maps entirely to the T-channel."""
        channels = channel_decomposition("T", "T")
        assert len(channels["W3"]) == 0
        assert len(channels["W4"]) == 0

    def test_W3W3_has_W4_channel(self):
        """W3 x W3 has a non-trivial W4-channel from g334."""
        channels = channel_decomposition("W3", "W3")
        assert len(channels["W4"]) > 0

    def test_W3W3_W4_channel_irrational(self):
        """The W4-channel of W3 x W3 involves g334 (irrational source)."""
        g334 = Symbol('g334')
        channels = channel_decomposition("W3", "W3", g334=g334)
        has_g334 = any(expand(v).has(g334) for v in channels["W4"].values())
        assert has_g334

    def test_W4W4_has_W4_channel(self):
        channels = channel_decomposition("W4", "W4")
        assert len(channels["W4"]) > 0

    def test_verify_all_pass(self):
        results = verify_channel_decomposition()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# Irrationality analysis
# ============================================================================

class TestIrrationality:
    def test_g334_enters_at_weight_6(self):
        """g334 first appears at weight 6 = wt(W3) + wt(W3) = 3 + 3."""
        irr = irrationality_analysis()
        g334_weights = [e["weight"] for e in irr.values() if e["has_g334"]]
        assert min(g334_weights) == 6

    def test_g444_enters_at_weight_8(self):
        """g444 first appears at weight 8 = wt(W4) + wt(W4) = 4 + 4."""
        irr = irrationality_analysis()
        g444_weights = [e["weight"] for e in irr.values() if e["has_g444"]]
        assert min(g444_weights) == 8

    def test_low_weights_rational(self):
        """At weights 2-5, the bar differential has purely rational coefficients."""
        irr = irrationality_analysis()
        for entry in irr.values():
            if entry["weight"] < 6:
                assert not entry["has_g334"] and not entry["has_g444"]

    def test_verify_all_pass(self):
        results = verify_irrationality_weight()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# Bar chain dimensions
# ============================================================================

class TestBarChainDims:
    def test_B0_equals_vbar(self):
        """B^0_h = dim V-bar_h (just the augmentation ideal)."""
        vdims = w4_augmentation_dims(8)
        for h in range(2, 9):
            assert bar_chain_dim(0, h) == vdims.get(h, 0)

    def test_B1_minimum_weight(self):
        """B^1_h = 0 for h < 4 (need 2 elements, each weight >= 2)."""
        assert bar_chain_dim(1, 2) == 0
        assert bar_chain_dim(1, 3) == 0

    def test_B1_4(self):
        """B^1_4: only pair is (T, T) at weight (2,2), times OS^1 = 1!."""
        assert bar_chain_dim(1, 4) == 1

    def test_B1_5(self):
        """B^1_5: pairs at weight 5 are (2,3) and (3,2).
        dim V-bar_2 = 1, dim V-bar_3 = 2. Count: 1*2 + 2*1 = 4. OS^1 = 1.
        """
        assert bar_chain_dim(1, 5) == 4

    def test_B2_minimum_weight(self):
        """B^2_h = 0 for h < 6 (need 3 elements, each weight >= 2)."""
        assert bar_chain_dim(2, 4) == 0
        assert bar_chain_dim(2, 5) == 0

    def test_B2_6(self):
        """B^2_6: only triple is (2,2,2), count = 1*1*1 = 1, OS^2 = 2! = 2."""
        assert bar_chain_dim(2, 6) == 2

    def test_B3_minimum_weight(self):
        """B^3_h = 0 for h < 8."""
        assert bar_chain_dim(3, 6) == 0
        assert bar_chain_dim(3, 7) == 0

    def test_B3_8(self):
        """B^3_8: quadruples (2,2,2,2), count = 1, OS^3 = 3! = 6."""
        assert bar_chain_dim(3, 8) == 6


# ============================================================================
# H^1 generators
# ============================================================================

class TestH1Generators:
    def test_h1_at_weight_2(self):
        gens = h1_generators_by_weight()
        assert gens[2] == ["T"]

    def test_h1_at_weight_3(self):
        gens = h1_generators_by_weight()
        assert gens[3] == ["W_3"]

    def test_h1_at_weight_4(self):
        """Weight 4: both W_4 (primary) and Lambda (composite)."""
        gens = h1_generators_by_weight()
        assert "W_4" in gens[4]
        assert "Lambda" in gens[4]
        assert len(gens[4]) == 2

    def test_h1_lower_bounds(self):
        assert h1_dimension_lower_bound(2) == 1
        assert h1_dimension_lower_bound(3) == 1
        assert h1_dimension_lower_bound(4) == 2

    def test_w4_has_more_h1_generators_than_w3(self):
        """W_4 has strictly more H^1 generators than W_3 at weight 4."""
        comp = compare_h1_w3_vs_w4()
        assert comp["difference"] == 1
        assert comp["total_W4_up_to_4"] > comp["total_W3_up_to_4"]


# ============================================================================
# Weight-4 Gram matrix (AP26)
# ============================================================================

class TestWeight4Gram:
    def test_lambda_w4_orthogonal(self):
        """Lambda and W_4 are orthogonal in the BPZ metric."""
        gram = weight4_gram_matrix()
        assert gram["gram_matrix"][("Lambda", "W_4")] == 0

    def test_lambda_norm(self):
        """<Lambda|Lambda> = c(5c+22)/10."""
        c = Symbol('c')
        gram = weight4_gram_matrix(c)
        assert expand(gram["gram_matrix"][("Lambda", "Lambda")] - c * (5*c + 22) / 10) == 0

    def test_w4_norm(self):
        """<W_4|W_4> = c/4."""
        c = Symbol('c')
        gram = weight4_gram_matrix(c)
        assert gram["gram_matrix"][("W_4", "W_4")] == c / 4

    def test_weight4_full_basis_dim(self):
        """Full weight-4 basis has dimension 4."""
        b = weight4_full_basis()
        assert b["dimension"] == 4
        assert len(b["states"]) == 4


# ============================================================================
# Euler characteristic
# ============================================================================

class TestEulerChar:
    def test_chi_h2(self):
        """chi(B^*_2) = dim B^0_2 = 1."""
        chi = bar_euler_char(8)
        assert chi[2] == 1

    def test_chi_h3(self):
        """chi(B^*_3) = dim B^0_3 = 2."""
        chi = bar_euler_char(8)
        assert chi[3] == 2

    def test_chi_h4(self):
        """chi(B^*_4) = B^0_4 - B^1_4 = 4 - 1 = 3."""
        chi = bar_euler_char(8)
        assert chi[4] == 3


# ============================================================================
# OPE structure cross-checks
# ============================================================================

class TestOPEStructure:
    def test_leading_poles(self):
        """Leading pole of W_s x W_s has mode index 2s - 1."""
        products = w4_full_nth_products()
        assert max(products[("T", "T")].keys()) == 3      # 2*2-1
        assert max(products[("W3", "W3")].keys()) == 5     # 2*3-1
        assert max(products[("W4", "W4")].keys()) == 7     # 2*4-1

    def test_two_point_normalization(self):
        """Leading pole coefficient = c/s for spin-s primary."""
        c = Symbol('c')
        products = w4_full_nth_products(c)
        assert products[("T", "T")][3]["vac"] == c / 2
        assert products[("W3", "W3")][5]["vac"] == c / 3
        assert products[("W4", "W4")][7]["vac"] == c / 4

    def test_primary_weight_from_T_OPE(self):
        """T_{(1)}W_s = s * W_s (conformal weight extraction)."""
        products = w4_full_nth_products()
        assert products[("T", "W3")][1]["W3"] == 3
        assert products[("T", "W4")][1]["W4"] == 4

    def test_w3w3_lambda_coefficient(self):
        """Lambda coefficient in W3 x W3: 16/(22+5c)."""
        c = Symbol('c')
        products = w4_full_nth_products(c)
        expected = Rational(16) / (22 + 5*c)
        assert products[("W3", "W3")][1]["Lambda"] == expected

    def test_w3w3_matches_w3_bar(self):
        """W3 x W3 OPE in W_4 must match w3_bar.py (same subalgebra)."""
        from compute.lib.w3_bar import w3_nth_products
        c = Symbol('c')
        w3_products = w3_nth_products()
        w4_products = w4_full_nth_products(c)
        # Check T-sector matches (modes 5, 3, 2 in W3 x W3)
        for n in [5, 3, 2]:
            for state in w3_products[("W", "W")].get(n, {}):
                if state == "vac":
                    assert w4_products[("W3", "W3")][n]["vac"] == w3_products[("W", "W")][n]["vac"]
                elif state in ("T", "dT"):
                    assert w4_products[("W3", "W3")][n][state] == w3_products[("W", "W")][n][state]

    def test_w4w4_ward_identity(self):
        """C_{4,4;2;0,6} = 2: T at pole 6 in W4 x W4."""
        products = w4_full_nth_products()
        assert products[("W4", "W4")][5]["T"] == 2

    def test_w3w4_T_at_pole5_vanishes(self):
        """C_{3,4;2;0,5} = 0: T does not appear at pole 5 in W3 x W4.

        This is the mixed-primary orthogonality condition.
        """
        products = w4_full_nth_products()
        w3w4 = products[("W3", "W4")]
        # Mode 4 corresponds to pole 5. T should not be present.
        if 4 in w3w4:
            assert "T" not in w3w4[4]


# ============================================================================
# Numerical evaluation
# ============================================================================

class TestNumerical:
    def test_kappa_at_c24(self):
        """kappa(W_4) = 13*24/12 = 26 at c = 24."""
        c = Symbol('c')
        val = float(w4_kappa(c).subs(c, 24))
        assert abs(val - 26.0) < 1e-10

    def test_g334_squared_at_c100(self):
        """g334^2 at c=100 from both sympy and float agree."""
        c = Symbol('c')
        sym_val = float(g334_squared(c).subs(c, 100))
        flt_val = g334_squared_float(100.0)
        assert abs(sym_val - flt_val) < 1e-10

    def test_g444_squared_at_c100(self):
        c = Symbol('c')
        sym_val = float(g444_squared(c).subs(c, 100))
        flt_val = g444_squared_float(100.0)
        assert abs(sym_val - flt_val) < 1e-10

    def test_g334_is_generically_irrational(self):
        """sqrt(g334^2) is generically irrational (not a perfect square)."""
        # At c = 100: g334^2 = 42*10000*522 / (124*768*346) = ...
        # This is a rational number whose square root is irrational.
        from fractions import Fraction
        c = Fraction(100)
        g_sq = (Fraction(42) * c**2 * (5*c + 22)
                / ((c + 24) * (7*c + 68) * (3*c + 46)))
        # Check it is not a perfect square of a rational
        from math import isqrt
        num = g_sq.numerator
        den = g_sq.denominator
        sqrt_num = isqrt(num)
        sqrt_den = isqrt(den)
        is_perfect_square = (sqrt_num * sqrt_num == num and
                             sqrt_den * sqrt_den == den)
        assert not is_perfect_square, "g334^2 should not be a perfect square at c=100"
